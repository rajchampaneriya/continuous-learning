"""Simulator runs export as OTLP/JSON traces with OpenTelemetry GenAI attributes."""
from datetime import datetime, timezone

from acme.sim.otel import to_otlp
from acme.sim.trace import RunResult, Span
from acme.sim.versions import Version

VERSION = Version(id="abcdef123456", label="1.0.0", status="candidate", created_at="", content={
    "name": "team-c3", "implementation": "multi_agent", "adapter": "team",
    "config": {"provider": "c3", "model": "anthropic:glm-5.3-flash"}})


def run(state="completed"):
    return RunResult(run_id="0123456789abcdef0123456789abcdef", version_id=VERSION.id, state=state,
                     output={"decision": "send", "outcome": "sent", "intent": "outage", "reasons": []},
                     usage={"latency_s": 0.5, "tokens_in": 22, "tokens_out": 9}, spans=[
        Span(id="specialist", parent=None, kind="agent", name="Draft", status="ok", ms=100,
             attrs={"agent": "Network", "envelope": {"headroom": 320}}),
        Span(id="specialist:turn-0", parent="specialist", kind="model_call", name="Turn 1", status="ok", ms=300,
             attrs={"tokens_in": 10, "tokens_out": 4, "stop_reason": "tool_use", "system_prompt": "SYSTEM"}),
        Span(id="specialist:turn-0:tool-0", parent="specialist:turn-0", kind="tool_call", name="lookup_customer",
             status="error", ms=0, attrs={"arguments": {"customer_id": "AC1001"}, "result": {"error": "boom"}}),
        Span(id="handoff-2", parent=None, kind="handoff", name="Network → Reviewer", status="ok", ms=0,
             attrs={"from": "Network", "to": "Reviewer"}),
    ])


def spans_of(payload):
    return payload["resourceSpans"][0]["scopeSpans"][0]["spans"]


def attrs_of(span):
    return {item["key"]: next(iter(item["value"].values())) for item in span["attributes"]}


def test_run_exports_as_one_trace_with_genai_operations_and_nested_timing():
    start = datetime(2026, 11, 15, tzinfo=timezone.utc)
    spans = spans_of(to_otlp(run(), VERSION, started_at=start, case_id="c19"))
    by_name = {span["name"]: span for span in spans}
    root = by_name["run team-c3"]
    assert {span["traceId"] for span in spans} == {"0123456789abcdef0123456789abcdef"}
    assert "parentSpanId" not in root and all(len(span["spanId"]) == 16 for span in spans)
    assert {span["parentSpanId"] for span in spans if span is not root} <= {span["spanId"] for span in spans}

    agent, chat, tool = (by_name["invoke_agent Network"], by_name["chat anthropic:glm-5.3-flash"],
                         by_name["execute_tool lookup_customer"])
    assert attrs_of(agent)["gen_ai.operation.name"] == "invoke_agent"
    assert attrs_of(agent)["gen_ai.agent.name"] == "Network"
    assert attrs_of(chat).items() >= {"gen_ai.operation.name": "chat", "gen_ai.provider.name": "anthropic",
                                   "gen_ai.request.model": "anthropic:glm-5.3-flash",
                                   "gen_ai.usage.input_tokens": "10", "gen_ai.usage.output_tokens": "4"}.items()
    assert chat["kind"] == 3 and attrs_of(tool)["gen_ai.tool.name"] == "lookup_customer"
    assert tool["status"]["code"] == 2 and attrs_of(root)["acme.case.id"] == "c19"
    assert chat["parentSpanId"] == agent["spanId"] and tool["parentSpanId"] == chat["spanId"]
    # The agent span covers its slower model call, and the handoff starts after the agent ends.
    assert int(agent["endTimeUnixNano"]) - int(agent["startTimeUnixNano"]) == 300_000_000
    assert by_name["Network → Reviewer"]["startTimeUnixNano"] == agent["endTimeUnixNano"]
    assert int(root["endTimeUnixNano"]) - int(root["startTimeUnixNano"]) == 500_000_000


def test_prompts_and_tool_content_are_exported_only_on_request():
    hidden = str(to_otlp(run(), VERSION))
    assert "SYSTEM" not in hidden and "AC1001" not in hidden and "headroom" not in hidden
    shown = str(to_otlp(run(), VERSION, include_content=True))
    assert "gen_ai.system_instructions" in shown and "gen_ai.tool.call.arguments" in shown and "AC1001" in shown


def test_failed_runs_mark_the_root_span_as_an_error():
    root = spans_of(to_otlp(run("failed"), VERSION))[0]
    assert root["status"] == {"code": 2, "message": "Run failed"}
