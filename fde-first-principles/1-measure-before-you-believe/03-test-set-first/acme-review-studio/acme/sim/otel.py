"""Export a simulator run as an OpenTelemetry trace in OTLP/JSON, using the GenAI semantic conventions.

Model calls become ``chat`` spans, tool calls ``execute_tool`` spans and agents ``invoke_agent`` spans, so the
file loads into any OTLP backend (a collector, Jaeger, Langfuse, Azure Monitor) without a custom mapping. Adapters
record durations rather than timestamps, so children are laid out one after another from their parent's start.
Prompts, tool arguments and results, and HTTP bodies are content and are exported only on request.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

from .trace import RunResult, Span
from .versions import Version

SCOPE = {"name": "acme.sim", "version": "1"}
_INTERNAL, _CLIENT = 1, 3
_ERROR = 2
_OPERATIONS = {"model_call": "chat", "tool_call": "execute_tool", "agent": "invoke_agent"}
# Span attributes that carry customer, prompt or remote content.
_CONTENT = {"system_prompt", "user_prompt", "arguments", "result", "request", "response", "envelope",
            "recorded_response", "headers", "detail"}


def _hex(text: str, length: int) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:length]


def _value(value: Any) -> dict[str, Any]:
    if isinstance(value, bool):
        return {"boolValue": value}
    if isinstance(value, int):
        return {"intValue": str(value)}
    if isinstance(value, float):
        return {"doubleValue": value}
    if isinstance(value, str):
        return {"stringValue": value}
    if isinstance(value, (list, tuple)) and all(isinstance(item, (str, bool, int, float)) for item in value):
        return {"arrayValue": {"values": [_value(item) for item in value]}}
    return {"stringValue": json.dumps(value, ensure_ascii=False, default=str)}


def _attributes(values: dict[str, Any]) -> list[dict[str, Any]]:
    return [{"key": key, "value": _value(value)} for key, value in values.items() if value is not None]


def _layout(spans: list[Span], start: int) -> tuple[dict[str, tuple[int, int]], int]:
    children: dict[str | None, list[Span]] = defaultdict(list)
    for span in spans:
        children[span.parent].append(span)
    times: dict[str, tuple[int, int]] = {}

    def place(span: Span, begin: int) -> int:
        cursor = begin
        for child in children[span.id]:
            cursor = place(child, cursor)
        end = max(begin + span.ms * 1_000_000, cursor)
        times[span.id] = (begin, end)
        return end

    cursor = start
    for root in children[None]:
        cursor = place(root, cursor)
    return times, cursor


def _provider_name(config: dict[str, Any]) -> str:
    model = str(config.get("model") or "")
    return model.split(":", 1)[0] if ":" in model else str(config.get("provider") or "")


def _span_attributes(span: Span, config: dict[str, Any], include_content: bool) -> dict[str, Any]:
    attrs = span.attrs
    values: dict[str, Any] = {"acme.span.id": span.id, "acme.span.kind": span.kind,
                              "acme.span.name": span.name, "acme.span.status": span.status}
    operation = _OPERATIONS.get(span.kind)
    if operation:
        values["gen_ai.operation.name"] = operation
    if span.kind == "model_call":
        values.update({"gen_ai.provider.name": _provider_name(config), "gen_ai.request.model": config.get("model"),
                       "gen_ai.usage.input_tokens": attrs.get("tokens_in"),
                       "gen_ai.usage.output_tokens": attrs.get("tokens_out"),
                       "gen_ai.response.finish_reasons": [attrs["stop_reason"]] if attrs.get("stop_reason") else None})
        if include_content and attrs.get("system_prompt"):
            values["gen_ai.system_instructions"] = [{"type": "text", "content": attrs["system_prompt"]}]
        if include_content and attrs.get("user_prompt"):
            values["gen_ai.input.messages"] = [{"role": "user", "parts": [
                {"type": "text", "content": attrs["user_prompt"]}]}]
    elif span.kind == "tool_call":
        values.update({"gen_ai.tool.name": span.name, "gen_ai.tool.type": "function"})
        if include_content:
            values.update({"gen_ai.tool.call.arguments": attrs.get("arguments"),
                           "gen_ai.tool.call.result": attrs.get("result")})
    elif span.kind == "agent":
        values["gen_ai.agent.name"] = str(attrs.get("agent") or span.name)
    elif span.kind == "http":
        values.update({"http.request.method": attrs.get("method"), "url.full": attrs.get("url"),
                       "http.response.status_code": attrs.get("status_code"),
                       "http.response.body.size": attrs.get("bytes")})
    for key, value in attrs.items():
        if key in {"tokens_in", "tokens_out", "stop_reason", "method", "url", "status_code", "bytes"}:
            continue
        if key not in _CONTENT or include_content:
            values["acme." + re.sub(r"[^a-z0-9_.]", "_", key.lower())] = value
    return values


def _name(span: Span, config: dict[str, Any]) -> str:
    if span.kind == "model_call":
        return f"chat {config.get('model') or ''}".strip()
    if span.kind == "tool_call":
        return f"execute_tool {span.name}"
    if span.kind == "agent":
        return f"invoke_agent {span.attrs.get('agent') or span.name}"
    return span.name


def to_otlp(result: RunResult, version: Version, *, started_at: datetime | None = None,
            case_id: str | None = None, include_content: bool = False) -> dict[str, Any]:
    """The run as an OTLP ``ExportTraceServiceRequest`` in its JSON encoding, under one root span."""
    config = version.content.get("config") or {}
    trace_id = result.run_id if re.fullmatch(r"[0-9a-f]{32}", result.run_id) else _hex(result.run_id, 32)
    root_id = _hex(result.run_id + "/", 16)
    start = int((started_at or datetime.now(timezone.utc)).timestamp() * 1_000_000_000)
    times, end = _layout(result.spans, start)
    latency = result.usage.get("latency_s")
    if isinstance(latency, (int, float)):
        end = max(end, start + int(latency * 1_000_000_000))
    ids = {span.id: _hex(f"{result.run_id}/{span.id}", 16) for span in result.spans}
    output = result.output or {}
    spans = [{
        "traceId": trace_id, "spanId": root_id, "name": f"run {version.name}", "kind": _INTERNAL,
        "startTimeUnixNano": str(start), "endTimeUnixNano": str(end),
        "attributes": _attributes({
            "acme.run.id": result.run_id, "acme.run.state": result.state, "acme.case.id": case_id,
            "acme.decision": output.get("decision"), "acme.outcome": output.get("outcome"),
            "acme.intent": output.get("intent"), "acme.reasons": output.get("reasons"),
            "gen_ai.usage.input_tokens": result.usage.get("tokens_in"),
            "gen_ai.usage.output_tokens": result.usage.get("tokens_out"),
            "acme.cost_usd": result.usage.get("cost_usd"), "acme.audit": result.audit or None,
            "acme.drift": result.drift or None}),
        "status": {"code": _ERROR, "message": "Run failed"} if result.state == "failed" else {},
    }]
    for span in result.spans:
        begin, finish = times[span.id]
        error = span.status == "error"
        spans.append({
            "traceId": trace_id, "spanId": ids[span.id], "parentSpanId": ids.get(span.parent, root_id),
            "name": _name(span, config), "kind": _CLIENT if span.kind in {"model_call", "http"} else _INTERNAL,
            "startTimeUnixNano": str(begin), "endTimeUnixNano": str(finish),
            "attributes": _attributes(_span_attributes(span, config, include_content)),
            "status": {"code": _ERROR, "message": str(span.attrs.get("error") or span.name)} if error else {},
        })
    resource = _attributes({"service.name": "acme-review-studio", "service.version": version.label or version.id,
                            "acme.version.id": version.id, "acme.version.name": version.name,
                            "acme.implementation": version.implementation, "acme.adapter": version.adapter})
    return {"resourceSpans": [{"resource": {"attributes": resource},
                               "scopeSpans": [{"scope": SCOPE, "spans": spans}]}]}
