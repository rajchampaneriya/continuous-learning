"""Simulator rendering is accessible and treats all trace evidence as data."""
from html.parser import HTMLParser

from acme.sim.render import (
    pin_status, render_comparison, render_detail, render_grade, render_result, version_heading,
)
from acme.sim.trace import Capabilities, RunResult, Span, Topology
from acme.sim.versions import Version


class Elements(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.elements = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def result():
    return RunResult(
        run_id="run", version_id="abcdef123456", state="completed", case_hash="same",
        output={"reply": "<script>alert(1)</script>", "decision": "send", "intent": "other"},
        spans=[
            Span(id="step-5", parent=None, kind="step", name="Draft <b>unsafe</b>", status="ok", ms=2,
                 attrs={"step": "5", "system_prompt": "<script>system</script>", "envelope": {"safe": "<b>"},
                        "recorded_response": {"secret": "not for display"}}),
            Span(id="turn", parent="step-5", kind="model_call", name="Turn 1", status="ok", ms=1),
            Span(id="tool", parent="turn", kind="tool_call", name="<img src=x>", status="error", ms=0,
                 attrs={"result": "<script>tool</script>"}),
        ],
    )


def version(version_id, name):
    return Version(id=version_id, content={"name": name, "implementation": "custom", "adapter": "offline",
                                           "config": {}, "pins": {}},
                   label="", status="candidate", created_at="")


def test_topology_buttons_and_nested_evidence_are_escaped_and_keyboard_accessible():
    run = result()
    topology = Topology(nodes=[{"id": "5", "name": "Draft"}], edges=[])
    markup = render_result(run, topology, "orchestrated", "step-5")
    markup += render_detail(run, "step-5", Capabilities(prompts=True, envelope=True, tool_calls=True))
    nodes = Elements(markup).elements
    buttons = [attrs for tag, attrs in nodes if tag == "button"]
    assert [button["data-step"] for button in buttons] == ["step-5", "turn", "tool"]
    assert all(button["type"] == "button" for button in buttons)
    assert "tool_call · error" in markup and "Agent turn timeline" in markup
    assert "&lt;script&gt;" in markup and "&lt;img" in markup
    assert not any(tag in {"script", "img"} for tag, _ in nodes)
    assert "not for display" not in markup


def test_capability_panels_and_unknown_implementations_use_span_tree():
    run = result()
    hidden = render_detail(run, "step-5", Capabilities())
    assert "System Prompt" not in hidden and "Envelope" not in hidden
    shown = render_detail(run, "step-5", Capabilities(prompts=True, envelope=True))
    assert "System Prompt" in shown and "Envelope" in shown
    fallback = render_result(run, Topology(), "unrecognized", None)
    assert "Run spans" in fallback and 'data-step="tool"' in fallback


def test_failure_without_a_step_remains_visible_in_the_topology():
    run = RunResult(run_id="failed", version_id="abcdef123456", state="failed",
                    spans=[Span(id="error", parent=None, kind="check", name="Run failed",
                                status="error", ms=0, attrs={"error": "Provider unavailable"})])
    markup = render_result(run, Topology(nodes=[{"id": "5", "name": "Draft"}]), "orchestrated", "error")
    assert 'data-step="error"' in markup and "check · error" in markup
    assert "Provider unavailable" in render_detail(run, "error", Capabilities())


def test_comparison_escapes_manifest_labels_and_reply_diff():
    left = result()
    right = RunResult(run_id="other", version_id="012345abcdef", state="completed", case_hash="same",
                      output={"reply": "<img src=x>", "decision": "escalate", "intent": "billing"})
    markup = render_comparison(left, right, version(left.version_id, "<script>name</script>"),
                               version(right.version_id, "Other"))
    assert "&lt;script&gt;name&lt;/script&gt;" in markup and "&lt;img" in markup
    assert "<ins>" in markup and "<del>" in markup
    assert not any(tag in {"script", "img"} for tag, _ in Elements(markup).elements)


def agent_run():
    return RunResult(run_id="agent", version_id="abcdef123456", state="completed", spans=[
        Span(id="agent", parent=None, kind="agent", name="C3 agent loop", status="ok", ms=5),
        Span(id="turn-0", parent="agent", kind="model_call", name="Turn 1", status="ok", ms=1,
             attrs={"tokens_in": 1840, "tokens_out": 96}),
        Span(id="turn-0:tool-0", parent="turn-0", kind="tool_call", name="lookup_customer", status="ok", ms=0,
             attrs={"arguments": {"customer_id": "AC1042"}, "result": {"plan": "Fibre 100"}}),
        Span(id="turn-0:tool-1", parent="turn-0", kind="tool_call", name="search_kb", status="ok", ms=0,
             attrs={"arguments": {"query": "late fee"}, "result": ["KB02"]}),
        Span(id="guard-0", parent="agent", kind="guard", name="legal_threat", status="escalate", ms=0),
    ])


def test_agent_loop_shows_a_turn_timeline_with_one_row_per_tool_call():
    markup = render_result(agent_run(), Topology(), "agent_loop", None, capabilities=Capabilities(tool_calls=True))
    tools = Elements(markup).elements
    assert len([attrs for tag, attrs in tools if tag == "ul" and attrs.get("aria-label") == "Tool calls"]) == 1
    assert "Agent turn timeline" in markup and "1840 in / 96 out" in markup
    assert "lookup_customer" in markup and "Fibre 100" in markup and "KB02" in markup
    assert "Escalation sources</b> · legal_threat" in markup
    hidden = render_result(agent_run(), Topology(), "agent_loop", None, capabilities=Capabilities())
    assert "lookup_customer" not in hidden


def test_api_versions_open_in_the_exchange_inspector():
    run = RunResult(run_id="http", version_id="abcdef123456", state="completed", spans=[
        Span(id="http", parent=None, kind="http", name="HTTP exchange", status="ok", ms=3400,
             attrs={"method": "POST", "url": "https://agent.example.com/acme/draft", "status_code": 200,
                    "bytes": 2100, "request": {"message": "hi"}, "response": {"intent": "<b>billing</b>"},
                    "headers": {"authorization": "[REDACTED]"}}),
        Span(id="remote:a", parent="http", kind="model_call", name="remote model", status="ok", ms=1),
    ])
    markup = render_result(run, Topology(), "api", None, capabilities=Capabilities(remote_trace=True))
    assert "POST https://agent.example.com/acme/draft · 200 · 3.4 s · 2100 B" in markup
    assert "Response · schema ✓" in markup and "[REDACTED]" in markup and "Remote trace · 1 spans" in markup
    assert "&lt;b&gt;billing" in markup
    assert "Remote trace" not in render_result(run, Topology(), "api", None, capabilities=Capabilities())


def test_grade_row_writes_each_check_and_policy_rules():
    markup = render_grade({"eval": {"intent_ok": True, "routing_ok": False, "model_escalation_ok": None,
                                    "missing": [], "banned": ["refund approved"]},
                           "policy": ["big_refund"], "policy_status": "graded"})
    assert "intent ✓ · routing ✗ · model escalation — · must include ✓ · banned: refund approved" in markup
    assert "policy: big_refund" in markup


def test_banner_counts_current_pins_and_names_the_bound_component():
    pinned = Version(id="abcdef123456", label="1.2.0", status="candidate", created_at="", content={
        "name": "studio-c3", "implementation": "orchestrated", "adapter": "studio-langgraph", "config": {},
        "slots": {"draft": {"implementation": "agent_loop"}}, "knowledge": {"workbook": "data/book.xlsx"},
        "pins": {"code": {}, "code_files": {"app.py": "x"}, "sheet:Customers": "y", "lab_files": {"policy.md": "z"}}})
    assert version_heading(pinned) == "studio-c3 1.2.0 · orchestrated › agent loop · candidate · abcdef123456"
    assert pin_status(pinned, []) == (8, 8)
    assert pin_status(pinned, ["data/book.xlsx", "lab:policy.md", "code (commit or working-tree diff)"]) == (5, 8)
    assert pin_status(version("legacy-round-1", "legacy-round-1"), []) is None


def team_run():
    return RunResult(run_id="team", version_id="abcdef123456", state="completed", spans=[
        Span(id="triage", parent=None, kind="agent", name="Classify", status="ok", ms=1, attrs={"agent": "Triage"}),
        Span(id="handoff-1", parent=None, kind="handoff", name="Triage → Billing", status="ok", ms=0,
             attrs={"from": "Triage", "to": "Billing"}),
        Span(id="specialist", parent=None, kind="agent", name="Draft", status="ok", ms=4,
             attrs={"agent": "<b>Billing</b>"}),
        Span(id="specialist:turn-0", parent="specialist", kind="model_call", name="Turn 1", status="ok", ms=1),
        Span(id="specialist:turn-0:tool-0", parent="specialist:turn-0", kind="tool_call", name="lookup_customer",
             status="ok", ms=0, attrs={"arguments": {"customer_id": "AC1042"}, "result": {}}),
        Span(id="handoff-2", parent=None, kind="handoff", name="Billing → Reviewer", status="ok", ms=0,
             attrs={"from": "<b>Billing</b>", "to": "Reviewer"}),
        Span(id="reviewer", parent=None, kind="agent", name="Approve", status="ok", ms=0, attrs={"agent": "Reviewer"}),
    ])


def test_multi_agent_versions_show_one_swimlane_per_agent_in_handoff_order():
    run = team_run()
    markup = render_result(run, Topology(), "multi_agent", None, capabilities=Capabilities(tool_calls=True))
    rows = markup.split("<tr>")[1:]
    assert [row.split("</th>")[0].split(">")[-1] for row in rows] == ["Triage", "&lt;b&gt;Billing&lt;/b&gt;", "Reviewer"]
    assert [row.count("<td>") for row in rows] == [5, 5, 5]
    assert 'data-step="handoff-1"' in rows[0] and 'data-step="handoff-2"' in rows[1]
    assert "Tools: lookup_customer" in rows[1]
    assert "Tools:" not in render_result(run, Topology(), "multi_agent", None, capabilities=Capabilities())
    assert "Agent turn timeline" in render_detail(run, "specialist", Capabilities(tool_calls=True))
