"""Step definitions for tests/features/simulator.feature: versions pin what runs, offline and scripted."""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml
from pytest_bdd import given, parsers, scenarios, then, when

from acme.lab import load_lab
from acme.sim.render import render_detail, render_result
from acme.sim.service import SimulationService
from acme.sim.trace import RunInput
from acme.store import AppSettings

ROOT = Path(__file__).parents[1]

scenarios("features/simulator.feature")


class Tags(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.stack, self.tool_rows = [], 0
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        if tag == "li" and self.stack and dict(self.stack[-1][1]).get("aria-label") == "Tool calls":
            self.tool_rows += 1
        if tag in {"ul", "li"}:
            self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag in {"ul", "li"} and self.stack:
            self.stack.pop()


@pytest.fixture
def world(tmp_path):
    lab = load_lab(ROOT / "data" / "Acme_Fibre_Grounded_Draft_Eval.xlsx")
    service = SimulationService(ROOT, lab, AppSettings(tmp_path / "settings.json"), runs_dir=tmp_path / "runs")
    return {"service": service, "versions": {}}


def _freeze(world, ref: str):
    if ref not in world["versions"]:
        name, label = ref.split("@")
        for path in sorted((ROOT / "workflows").glob("*.yaml")):
            manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
            if manifest.get("name") == name and str(manifest.get("label")) == label:
                world["versions"][ref] = world["service"].registry.freeze(
                    world["service"].registry.load_manifest(path))
                break
        else:
            raise AssertionError(f"No manifest under workflows/ for {ref}")
    return world["versions"][ref]


def _run(world, ref: str, case_id: str):
    service = world["service"]
    return service.run(_freeze(world, ref).id, RunInput.from_case(service.lab.case(case_id)))


@given(parsers.parse('version "{ref}" is frozen'))
def frozen(world, ref):
    _freeze(world, ref)


@when(parsers.parse('I run case "{case_id}" against "{ref}"'))
def run_case(world, case_id, ref):
    world["ref"], world["result"] = ref, _run(world, ref, case_id)


@then("the run's version id is the frozen version's id")
def run_version(world):
    assert world["result"].version_id == _freeze(world, world["ref"]).id


@then("the run's pins equal the version's pins")
def run_pins(world):
    assert world["result"].pins == _freeze(world, world["ref"]).pins


@given(parsers.parse('a batch of {count:d} cases is running against "{ref}"'))
def batch_started(world, count, ref):
    cases = [case["id"] for case in world["service"].lab.cases[:count]]
    half = count // 2
    world.update(ref=ref, pending=cases[half:], batch=[_run(world, ref, case_id) for case_id in cases[:half]])


@when("another session switches the working copy to Claude Code")
def switch_to_claude(world):
    world["service"].settings.provider = "claude-code"
    world["batch"] += [_run(world, world["ref"], case_id) for case_id in world["pending"]]


@then("every run in the batch used the offline drafter")
def batch_offline(world):
    version_id = _freeze(world, world["ref"]).id
    assert len(world["batch"]) == 10
    assert {run.version_id for run in world["batch"]} == {version_id}
    assert {run.output["provider"] for run in world["batch"] if run.output.get("model_called")} == {"offline"}


@given(parsers.parse('case "{case_id}" is held for review on "{ref}"'))
def held(world, case_id, ref):
    world["ref"], world["result"] = ref, _run(world, ref, case_id)
    assert world["result"].state == "waiting_for_human"


@given("the working copy now uses the C3 drafter")
def working_copy_c3(world):
    world["service"].settings.provider = "c3"


@when("I approve the held draft")
def approve(world):
    world["result"] = world["service"].resume(world["result"].run_id, {"action": "approve"})


@then(parsers.parse('the run finishes on "{ref}"'))
def finished_on(world, ref):
    result = world["result"]
    assert result.state == "completed"
    assert result.version_id == _freeze(world, ref).id
    assert result.output["outcome"] == "sent_after_review"
    assert result.output["provider"] == "offline"


def _script_c3(monkeypatch):
    """C3 calls two tools on its first turn, then returns its final JSON."""
    monkeypatch.setenv("LLM_ANTHROPIC_KEY", "not-a-real-key")
    calls = []

    def scripted_chat(messages, **kwargs):
        calls.append(kwargs)
        if len(calls) == 1:
            tools = [{"function": {"name": "lookup_customer", "arguments": {"customer_id": "AC1001"}}},
                     {"function": {"name": "search_kb", "arguments": {"query": "outage"}}}]
            return {"content": "", "tool_calls": tools,
                    "message": {"role": "assistant", "content": "", "tool_calls": tools},
                    "tokens_in": 10, "tokens_out": 4, "seconds": 0.1}
        content = json.dumps({"intent": "outage", "reply": "Thank you. The team will check.",
                              "needs_human": False})
        return {"content": content, "tool_calls": [], "message": {"role": "assistant", "content": content},
                "tokens_in": 12, "tokens_out": 5, "seconds": 0.1}

    monkeypatch.setattr("lab.version_c3.chat", scripted_chat)


@given(parsers.parse('version "{ref}" binds the C3 agent loop to step 5'))
def c3_version(world, ref, monkeypatch):
    version = _freeze(world, ref)
    assert version.content["slots"]["draft"]["adapter"] == "lab-c3"
    _script_c3(monkeypatch)
    world["ref"] = ref


@when(parsers.parse('I run case "{case_id}" and open step 5'))
def open_step_5(world, case_id):
    service = world["service"]
    world["result"] = _run(world, world["ref"], case_id)
    version = _freeze(world, world["ref"])
    world["capabilities"] = service.adapter(version).capabilities(version)
    world["detail"] = render_detail(world["result"], "step-5", world["capabilities"])


@then("I see one row per tool call with its result")
def tool_rows(world):
    tools = [span for span in world["result"].spans if span.kind == "tool_call"]
    assert len(tools) == 2
    assert Tags(world["detail"]).tool_rows == len(tools)
    assert all(span.name in world["detail"] for span in tools)
    assert world["detail"].count("<summary>Result</summary>") == len(tools)


@then("no prompt inspector is shown for step 4")
def no_step_4_prompt(world):
    step_4 = render_detail(world["result"], "step-4", world["capabilities"])
    assert "Prompt" not in step_4


@given(parsers.parse('version "{ref}" runs a triage, specialist and reviewer team on the C3 agent loop'))
def team_version(world, ref, monkeypatch):
    version = _freeze(world, ref)
    assert (version.implementation, version.content["config"]["provider"]) == ("multi_agent", "c3")
    _script_c3(monkeypatch)


@then("I see one swimlane per agent, joined by handoffs in run order")
def swimlanes(world):
    service, result = world["service"], world["result"]
    version = _freeze(world, world["ref"])
    adapter = service.adapter(version)
    world["view"] = render_result(result, adapter.topology(version), version.implementation, None,
                                  capabilities=adapter.capabilities(version))
    roots = [(span.kind, span.attrs.get("agent") or span.attrs.get("to")) for span in result.spans
             if span.parent is None]
    assert roots == [("agent", "Triage"), ("handoff", "Network"), ("agent", "Network"),
                     ("handoff", "Reviewer"), ("agent", "Reviewer")]
    lanes = [row.split("</th>")[0].split(">")[-1] for row in world["view"].split("<tr>")[1:]]
    assert lanes == ["Triage", "Network", "Reviewer"]


@then("the specialist's lane lists its tool calls")
def lane_tools(world):
    network = world["view"].split("<tr>")[2]
    assert "Tools: lookup_customer, search_kb" in network


@then("the run is graded like any other version")
def graded(world):
    result = world["result"]
    assert result.state == "completed" and result.output["intent"] == "outage"
    assert result.grade["eval"]["intent_ok"] is True
