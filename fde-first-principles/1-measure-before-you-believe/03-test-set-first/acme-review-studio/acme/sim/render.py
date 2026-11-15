"""Escaped HTML renderers for simulator topologies and evidence.

Views are chosen by implementation model (``RENDERERS``) and, inside a run, per span (``SPAN_VIEWS``), so a
step bound to an agent loop opens as a turn timeline. Anything no renderer claims falls back to the span tree.
"""
from __future__ import annotations

import html
import json
from collections import defaultdict
from typing import Any, Callable

from .service import compare_results, manifest_diff
from .trace import Capabilities, RunResult, Span, Topology
from .versions import Version

# Span attributes shown only when the version declares the capability that produces them.
_GATED_ATTRS = {"system_prompt": "prompts", "user_prompt": "prompts", "envelope": "envelope"}
_HIDDEN_ATTRS = {"step", "recorded_response"}


def _text(value: Any) -> str:
    if isinstance(value, (dict, list, tuple)):
        value = json.dumps(value, ensure_ascii=False, indent=2, default=str)
    return html.escape(str(value if value is not None else "—"), quote=True)


def _button(span: Span, selected: str | None, target: str) -> str:
    return (f'<button type="button" class="sim-span st-{_text(span.status)} '
            f'{"selected" if span.id == selected else ""}" data-step="{_text(span.id)}" '
            f'data-target="{_text(target)}"><b>{_text(span.name)}</b>'
            f'<span>{_text(span.kind)} · {_text(span.status)} · {span.ms} ms</span></button>')


def _tree(spans: list[Span], selected: str | None, target: str, parent: str | None = None) -> str:
    children: dict[str | None, list[Span]] = defaultdict(list)
    for span in spans:
        children[span.parent].append(span)

    def branch(node: str | None) -> str:
        items = []
        for span in children.get(node, []):
            items.append("<li>" + _button(span, selected, target) + branch(span.id) + "</li>")
        return "<ul>" + "".join(items) + "</ul>" if items else ""

    return '<div class="sim-tree">' + branch(parent) + "</div>"


def _topology(result: RunResult, topology: Topology, selected: str | None, target: str) -> str:
    spans = {span.attrs.get("step"): span for span in result.spans if span.attrs.get("step")}
    buttons = []
    for node in topology.nodes:
        step = str(node["id"])
        span = spans.get(step) or Span(id=f"step-{step}", parent=None, kind="step",
                                      name=str(node["name"]), status="skipped", ms=0,
                                      attrs={"step": step, "detail": "Not run"})
        buttons.append(_button(span, selected, target))
    edges = " · ".join(f'{_text(edge["source"])} → {_text(edge["target"])}'
                       for edge in topology.edges)
    roots = {span.id for span in result.spans if span.parent is None and not span.attrs.get("step")}
    extra = ([span for span in result.spans if span.parent is not None or span.id in roots]
             if roots else [])
    return ('<div class="sim-topology" aria-label="Workflow steps">' + "".join(buttons) + "</div>"
            + (f'<div class="muted mt-2">Connections: {edges}</div>' if edges else "")
            + ('<h4>Other run evidence</h4>' + _tree(extra, selected, target) if extra else ""))


def _children(spans: list[Span], parent: str | None) -> list[Span]:
    return [span for span in spans if span.parent == parent]


def _allows(capabilities: Capabilities | None, name: str) -> bool:
    return capabilities is None or bool(getattr(capabilities, name))


def _tool_row(tool: Span, selected: str | None, target: str) -> str:
    args = tool.attrs.get("arguments")
    return (f'<li>{_button(tool, selected, target)}'
            f'<div class="muted">Arguments: <code>{_text(args)}</code></div>'
            f'<details><summary>Result</summary><pre class="prompt">{_text(tool.attrs.get("result"))}</pre>'
            "</details></li>")


def _turn_timeline(spans: list[Span], parent: str, selected: str | None, target: str,
                   capabilities: Capabilities | None = None) -> str:
    """One row per model turn, its tool calls with results, then the escalation sources."""
    nested = _children(spans, parent)
    rows = []
    for turn in (span for span in nested if span.kind == "model_call"):
        attrs = turn.attrs
        usage = []
        if attrs.get("tokens_in") is not None:
            usage.append(f'{attrs["tokens_in"]} in / {attrs.get("tokens_out", 0)} out')
        if attrs.get("stop_reason"):
            usage.append(f'stop: {attrs["stop_reason"]}')
        tools = [span for span in _children(spans, turn.id) if span.kind == "tool_call"]
        tool_rows = ("".join(_tool_row(tool, selected, target) for tool in tools)
                     if tools and _allows(capabilities, "tool_calls") else "")
        rows.append(f"<li>{_button(turn, selected, target)}"
                    + (f'<div class="muted">{_text(" · ".join(usage))}</div>' if usage else "")
                    + (f'<ul class="sim-tools" aria-label="Tool calls">{tool_rows}</ul>' if tool_rows else "")
                    + "</li>")
    guards = [span.name for span in nested if span.kind == "guard"]
    return ('<div class="sim-timeline"><ol>' + "".join(rows) + "</ol>"
            f'<div><b>Escalation sources</b> · {_text(", ".join(guards) or "none")}</div></div>')


def _exchange(result: RunResult, span: Span, selected: str | None, target: str,
              capabilities: Capabilities | None = None) -> str:
    """Exchange inspector: the request, the validated response, redacted headers and any remote trace."""
    attrs = span.attrs
    head = (f'{attrs.get("method", "POST")} {attrs.get("url", "")} · {attrs.get("status_code", "—")} · '
            f'{span.ms / 1000:.1f} s · {attrs.get("bytes", 0)} B')
    schema = "schema ✓" if result.state in {"completed", "waiting_for_human"} else "schema not validated"
    remote = [item for item in result.spans if item.parent == span.id]
    trace = (f'<details><summary>Remote trace · {len(remote)} spans</summary>'
             f'{_tree(result.spans, selected, target, parent=span.id)}</details>'
             if remote and _allows(capabilities, "remote_trace") else "")
    return (f'<div class="sim-exchange">{_button(span, selected, target)}<div><code>{_text(head)}</code></div>'
            f'<details><summary>Request</summary><pre class="prompt">{_text(attrs.get("request"))}</pre></details>'
            f'<details><summary>Response · {_text(schema)}</summary>'
            f'<pre class="prompt">{_text(attrs.get("response"))}</pre></details>'
            f'<div class="muted">Headers: {_text(attrs.get("headers"))}</div>{trace}</div>')


def _has_turns(span: Span, spans: list[Span]) -> bool:
    return any(child.kind == "model_call" for child in _children(spans, span.id))


def _span_tree_view(result: RunResult, topology: Topology, selected: str | None, target: str,
                    capabilities: Capabilities | None) -> str:
    return '<h4>Run spans</h4>' + _tree(result.spans, selected, target)


def _step_graph_view(result: RunResult, topology: Topology, selected: str | None, target: str,
                     capabilities: Capabilities | None) -> str:
    if not topology.nodes:
        return _span_tree_view(result, topology, selected, target, capabilities)
    return _topology(result, topology, selected, target)


def _turn_view(result: RunResult, topology: Topology, selected: str | None, target: str,
               capabilities: Capabilities | None) -> str:
    parts = []
    for root in _children(result.spans, None):
        parts.append(_button(root, selected, target))
        parts.append(_turn_timeline(result.spans, root.id, selected, target, capabilities)
                     if _has_turns(root, result.spans) else _tree(result.spans, selected, target, parent=root.id))
    return '<h4>Agent turn timeline</h4>' + "".join(parts)


def _exchange_view(result: RunResult, topology: Topology, selected: str | None, target: str,
                   capabilities: Capabilities | None) -> str:
    parts = [_exchange(result, root, selected, target, capabilities) if root.kind == "http"
             else _button(root, selected, target) + _tree(result.spans, selected, target, parent=root.id)
             for root in _children(result.spans, None)]
    return '<h4>HTTP exchange</h4>' + "".join(parts)


def _descendants(spans: list[Span], parent: str) -> list[Span]:
    found = _children(spans, parent)
    for span in list(found):
        found.extend(_descendants(spans, span.id))
    return found


def _swimlane_view(result: RunResult, topology: Topology, selected: str | None, target: str,
                   capabilities: Capabilities | None) -> str:
    """One row per agent and one column per top-level span, so handoffs read left to right in run order."""
    roots = _children(result.spans, None)
    lanes = list(dict.fromkeys(str(span.attrs.get("agent") or span.name) for span in roots if span.kind == "agent"))
    if not lanes:
        return _span_tree_view(result, topology, selected, target, capabilities)
    rows = []
    for lane in lanes:
        cells = []
        for span in roots:
            cell = ""
            if span.kind == "agent" and str(span.attrs.get("agent") or span.name) == lane:
                tools = [item.name for item in _descendants(result.spans, span.id) if item.kind == "tool_call"]
                cell = _button(span, selected, target) + (
                    f'<div class="muted">Tools: {_text(", ".join(tools))}</div>'
                    if tools and _allows(capabilities, "tool_calls") else "")
            elif span.kind == "handoff" and span.attrs.get("from") == lane:
                cell = _button(span, selected, target)
            cells.append(f"<td>{cell}</td>")
        rows.append(f'<tr><th scope="row">{_text(lane)}</th>{"".join(cells)}</tr>')
    other = [span for span in roots if span.kind not in {"agent", "handoff"}]
    return ('<h4>Agent swimlanes</h4><div class="table-responsive">'
            '<table class="table table-sm sim-lanes" aria-label="Agent swimlanes"><tbody>'
            + "".join(rows) + "</tbody></table></div>"
            + ("<h4>Other run evidence</h4>" + "".join(_button(span, selected, target) for span in other)
               if other else ""))


View = Callable[[RunResult, Topology, str | None, str, Capabilities | None], str]

# Implementation model -> run view. Anything else falls back to the span tree.
RENDERERS: dict[str, View] = {
    "orchestrated": _step_graph_view,
    "declarative": _step_graph_view,
    "agent_loop": _turn_view,
    "multi_agent": _swimlane_view,
    "api": _exchange_view,
}

NestedView = Callable[[RunResult, Span, str | None, str, Capabilities], str]

# Chosen per span, so a step bound to another implementation model shows that model's view inside it.
SPAN_VIEWS: list[tuple[Callable[[Span, list[Span]], bool], NestedView]] = [
    (_has_turns, lambda result, span, selected, target, caps:
        '<div class="mt-2"><b>Agent turn timeline</b></div>'
        + _turn_timeline(result.spans, span.id, selected, target, caps)),
]


def render_result(result: RunResult, topology: Topology, implementation: str,
                  selected: str | None, target: str = "sim_step_click",
                  capabilities: Capabilities | None = None) -> str:
    view = RENDERERS.get(implementation, _span_tree_view)
    return view(result, topology, selected, target, capabilities)


def render_detail(result: RunResult, selected: str | None, capabilities: Capabilities,
                  target: str = "sim_step_click") -> str:
    span = next((item for item in result.spans if item.id == selected), None)
    if span is None:
        return '<div class="muted">Select a span to inspect its evidence.</div>'
    output = [f'<div><b>{_text(span.name)}</b> · {_text(span.kind)} · {_text(span.status)} · {span.ms} ms</div>']
    attrs = {key: value for key, value in span.attrs.items()
             if key not in _HIDDEN_ATTRS and value is not None
             and (key not in _GATED_ATTRS or getattr(capabilities, _GATED_ATTRS[key]))}
    for key, value in attrs.items():
        output.append(f'<details open><summary>{_text(key.replace("_", " ").title())}</summary>'
                      f'<pre class="prompt">{_text(value)}</pre></details>')
    if _children(result.spans, span.id):
        nested = next((view for matches, view in SPAN_VIEWS if matches(span, result.spans)), None)
        output.append(nested(result, span, selected, target, capabilities) if nested else
                      '<div class="mt-2"><b>Nested evidence</b></div>'
                      + _tree(result.spans, selected, target, parent=span.id))
    return "".join(output)


def render_grade(grade: dict[str, Any]) -> str:
    """The grade row: each check as a written mark, so status never depends on colour."""
    if not grade:
        return '<div class="muted">Grade is available after the run completes.</div>'

    def mark(value: Any) -> str:
        return "✓" if value is True else "✗" if value is False else "—"

    checks = grade.get("eval")
    if checks:
        parts = [f'intent {mark(checks.get("intent_ok"))}', f'routing {mark(checks.get("routing_ok"))}',
                 f'model escalation {mark(checks.get("model_escalation_ok"))}',
                 "must include ✓" if not checks.get("missing") else "missing: " + ", ".join(checks["missing"]),
                 "banned phrases ✓" if not checks.get("banned") else "banned: " + ", ".join(checks["banned"])]
    else:
        parts = [grade.get("eval_status") or "not graded"]
    policy = grade.get("policy")
    parts.append("policy: " + (", ".join(policy) or "none") if policy is not None
                 else f'policy: {grade.get("policy_status") or "not graded"}')
    return ('<div class="sim-grade"><b>Grade</b> ' + _text(" · ".join(parts)) + "</div>"
            f'<details><summary>Full grade</summary><pre>{_text(grade)}</pre></details>')


def pin_status(version: Version, drift: list[str]) -> tuple[int, int] | None:
    """How many of the version's pins still match the current files, as (current, total)."""
    pins = version.pins
    if "code" not in pins:
        return None
    workbook = version.content["knowledge"]["workbook"]
    items = {"code", "model", "prompt:system", "guards", "workbook", *pins.get("code_files", {}),
             *(key for key in pins if key.startswith("sheet:")),
             *(f"lab:{name}" for name in pins.get("lab_files", {}))}
    aliases = {workbook: "workbook", "working-copy model": "model", "working-copy guards": "guards"}
    changed = {"code" if item.startswith("code (") else aliases.get(item, item) for item in drift}
    return len(items - changed), len(items)


def version_heading(version: Version) -> str:
    """`name label · implementation › bound component · status · id`, as in the Simulator banner."""
    slot = (version.content.get("slots") or {}).get("draft") or {}
    model = version.implementation.replace("_", " ")
    if slot.get("implementation"):
        model += " › " + str(slot["implementation"]).replace("_", " ")
    name = f"{version.name} {version.label}".strip()
    return f"{name} · {model} · {version.status} · {version.id}"


def render_comparison(left: RunResult, right: RunResult, left_version: Version, right_version: Version) -> str:
    diff = compare_results(left, right)
    changes = manifest_diff(left_version, right_version)
    lines = []
    for key in ("decision", "reasons", "intent", "grade", "usage"):
        if key in diff:
            lines.append(f'<tr><th scope="row">{_text(key.title())}</th>'
                         f'<td><pre>{_text(diff[key]["left"])}</pre></td>'
                         f'<td><pre>{_text(diff[key]["right"])}</pre></td></tr>')
    words = []
    for word in diff["reply_diff"]:
        text = _text(word[2:])
        if word.startswith("+ "):
            words.append(f"<ins>{text}</ins>")
        elif word.startswith("- "):
            words.append(f"<del>{text}</del>")
        elif word.startswith("  "):
            words.append(text)
    manifest = "".join(f'<li><b>{_text(item["field"])}</b>: {_text(item["left"])} → {_text(item["right"])}</li>'
                       for item in changes) or "<li>No manifest differences.</li>"
    return (f'<details><summary>Manifest differences</summary><ul>{manifest}</ul></details>'
            '<div class="table-responsive"><table class="table table-sm sim-compare"><thead><tr>'
            f'<th>Field</th><th>{_text(left_version.name)} · {_text(left.version_id)}</th>'
            f'<th>{_text(right_version.name)} · {_text(right.version_id)}</th></tr></thead>'
            f'<tbody>{"".join(lines)}</tbody></table></div>'
            f'<div><b>Reply diff:</b> {" ".join(words) or "No reply."}</div>')
