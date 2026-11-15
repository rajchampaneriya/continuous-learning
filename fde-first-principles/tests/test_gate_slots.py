"""Step definitions for features/gate_slots.feature, plus the canonical-name unit checks."""
import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from lab.version_c3 import build_decision_envelope
from lab.version_d import canonical_offer, fill_offers

scenarios("features/gate_slots.feature")


@pytest.fixture
def world():
    return {}


@given(parsers.parse('customer {customer} writes "{message}"'))
def customer_writes(world, customer, message):
    world["case"] = {"id": "t-slot", "customer_id": customer, "message": message}


@when(parsers.parse('the model returns the slots "{slots}"'))
def model_returns_slots(world, slots):
    world["envelope"] = build_decision_envelope(world["case"])
    raw = [s.strip() for s in slots.split(",")] if slots != "none" else []
    draft = "About your billing: a customer representative will call you."
    world["reply"], world["sources"] = fill_offers(draft, raw, world["envelope"], world["case"])


@then(parsers.parse('the reply contains "{sentence}"'))
def reply_contains(world, sentence):
    assert sentence.lower() in world["reply"].lower(), world["reply"]


@then(parsers.parse("the reply has {n:d} grant sentences"))
def grant_sentences(world, n):
    assert world["reply"].count("(KB") == n, world["reply"]


@then(parsers.parse('the Gate escalates with "{sources}"'))
def gate_escalates(world, sources):
    want = [] if sources == "none" else [sources]
    assert world["sources"] == want, world["sources"]


def test_canonical_offer_maps_to_the_catalogue():
    assert canonical_offer("retention offer (KB11)") == "retention offer"
    assert canonical_offer("  Late fee waiver ") == "late-fee waiver"
    assert canonical_offer("late fee waiver") == "late-fee waiver"
    assert canonical_offer("Double Payment Refund (KB04)") == "double payment refund"
    assert canonical_offer("retention   offer") == "retention offer"
    assert canonical_offer("outage credit (KB06)") == "outage credit"
    assert canonical_offer("free month") is None
    assert canonical_offer("") is None


def test_gate_saves_canonical_filled_and_raw_offers(monkeypatch):
    # The model copies the brief's "(KB11)" label and adds one name outside the catalogue.
    answer = json.dumps({"intent": "cancel", "reply": "A customer representative will call you.",
                         "needs_human": True, "offers": ["retention offer (KB11)", "free month"]})

    def fake_chat(messages, **kwargs):
        return {"content": answer, "tool_calls": [], "message": {"role": "assistant", "content": answer},
                "tokens_in": 0, "tokens_out": 0, "seconds": 0.0, "stop_reason": "end_turn"}

    monkeypatch.setattr("lab.version_d.chat", fake_chat)
    from lab.version_d import run_agent
    case = {"id": "t-gate-slots", "customer_id": "AC1009",
            "message": "Please close the connection, we're vacating the house."}
    output, _ = run_agent(case)
    assert output["offers_filled"] == ["retention offer"]
    assert output["offers_raw"] == ["retention offer (KB11)", "free month"]
    assert "gate:unknown_slot" in output["escalation_sources"]
