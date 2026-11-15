"""Task 5: the Gate checks the model's draft for grant or action-claim sentences."""
import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

import lab.version_d
from lab.version_c3 import build_decision_envelope
from lab.version_d import check_draft, run_agent

scenarios("features/gate_draft.feature")


@pytest.fixture
def world():
    return {}


@given("customer AC1009 asked for money")
def asked_for_money(world):
    world["case"] = {"id": "t-draft", "customer_id": "AC1009",
                     "message": "I paid ₹999 twice this month. Give me a ₹500 credit."}
    world["envelope"] = build_decision_envelope(world["case"])


@when(parsers.parse('the model drafts "{draft}"'))
def model_drafts(world, draft):
    world["hits"] = check_draft(draft, world["case"], world["envelope"])


@then(parsers.parse("the draft check reports {detector}"))
def draft_check_reports(world, detector):
    want = [] if detector == "none" else [detector]
    assert [h["detector"] for h in world["hits"]] == want, world["hits"]


def _reply(content):
    return {"content": content, "tokens_in": 10, "tokens_out": 10, "seconds": 0.1,
            "stop_reason": "stop", "message": {"role": "assistant", "content": content},
            "tool_calls": []}


def test_the_gate_repairs_a_granting_draft(monkeypatch):
    """A draft that grants money gets one repair call; the repaired reply is what ships."""
    calls = []

    def fake_chat(msgs, tools=None, temperature=0.0, run=0, model=None, timeout=None, **options):
        calls.append(msgs)
        if len(calls) == 1:
            content = json.dumps({"intent": "billing", "reply": "We will refund your ₹500 now.",
                                  "needs_human": False, "offers": []})
        else:
            content = json.dumps({"intent": "billing",
                                  "reply": "A customer representative will look at your request.",
                                  "needs_human": False, "offers": []})
        return _reply(content)

    monkeypatch.setattr(lab.version_d, "chat", fake_chat)
    case = {"id": "t-repair", "customer_id": "AC1009",
            "message": "I paid ₹999 twice this month. Give me a ₹500 credit."}
    output, trace = run_agent(case, persist_cache=False)
    assert output["draft_repaired"] is True
    assert "refund" not in output["reply"].lower()
    assert not any("gate:" in s for s in output["escalation_sources"]), output["escalation_sources"]
    assert len(calls) == 2


def test_an_unrepairable_draft_escalates(monkeypatch):
    """If the repair still grants, the Gate escalates instead of shipping it."""
    calls = []

    def fake_chat(msgs, tools=None, temperature=0.0, run=0, model=None, timeout=None, **options):
        calls.append(msgs)
        content = json.dumps({"intent": "billing", "reply": "We will refund your ₹500 now.",
                              "needs_human": False, "offers": []})
        return _reply(content)

    monkeypatch.setattr(lab.version_d, "chat", fake_chat)
    case = {"id": "t-unrepair", "customer_id": "AC1009",
            "message": "I paid ₹999 twice this month. Give me a ₹500 credit."}
    output, trace = run_agent(case, persist_cache=False)
    assert "gate:draft_grant" in output["escalation_sources"], output["escalation_sources"]
    assert output["needs_human"] is True
    assert output["draft_repaired"] is True  # the repair call ran; the reply still granted
