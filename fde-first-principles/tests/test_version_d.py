"""Version D: router, gate and thread ledger — no LLM calls (route/gate/watchdog only)."""
from __future__ import annotations

import pytest

from lab.acme import DATA, load_cases
from lab.evals import policy_violations
from lab.version_d import (
    ThreadStore,
    claim_amounts,
    fill_offers,
    route,
    watchdog,
)


_n = iter(range(1000))


def case(cid: str, message: str, **kw) -> dict:
    return {"id": kw.pop("case_id", f"x{next(_n)}"), "customer_id": cid, "message": message, **kw}


def test_claim_amounts_double_payment_claim_has_no_verb():
    # m40's wording: money figures with no refund/credit verb — the ledger must still count them
    # (one ₹999 refund claimed; that alone is above the ₹500 headroom).
    assert claim_amounts("I think I was charged twice.\n\nOctober. Two payments of ₹999.") == [999]
    assert claim_amounts("Why is my bill ₹699?") == []
    assert sum(claim_amounts("Please credit me ₹300.")) == 300


def test_router_fast_path_on_legal_threat():
    r = route(case("AC1002", "See you in consumer court."))
    assert r["path"] == "fast"
    assert any("legal" in s for s in r["sources"])


def test_router_worker_path_when_no_rule_fires():
    r = route(case("AC1002", "The ₹300 extra on last month's bill was wrong. Please credit me ₹300."))
    assert r["path"] == "worker" and r["sources"] == []


def test_ledger_catches_claim_built_over_turns():
    store = ThreadStore()
    first = {**case("AC1002", "Please credit me ₹300."), "thread_id": "T1"}
    assert route(first, store=store)["path"] == "worker"
    store.record_asked(first, sum(claim_amounts(first["message"])))
    assert store.asked_so_far("T1") == 300
    second = {**case("AC1002", "Please also credit this month's ₹300."), "thread_id": "T1"}
    r = route(second, store=store)
    assert r["path"] == "fast"
    assert "rule:money_above_headroom_ledger" in r["sources"]


def test_ledger_thread_stays_with_human():
    store = ThreadStore()
    store.mark_open({**case("AC1002", "again"), "thread_id": "T1"}, "test")
    r = route({**case("AC1002", "Where is my reply?"), "thread_id": "T1"}, store=store)
    assert r["path"] == "fast" and "rule:thread_with_human" in r["sources"]


def test_ledger_does_not_leak_across_single_email_cases():
    store = ThreadStore()
    a = case("AC1002", "Please credit me ₹300.")
    store.record_asked(a, 300)
    b = case("AC1002", "Please also credit this month's ₹300.")  # no thread_id -> own thread
    assert route(b, store=store)["path"] == "worker"


def test_gate_fills_waiver_sentence_with_amount():
    c = case("AC1005", "Please waive the ₹100 late fee.", case_id="t-waiver")
    r = route(c)
    decisions = r["envelope"]["offer_decisions"]["late-fee waiver"]
    if decisions["status"] != "offer":
        pytest.skip("AC1005 not currently waiver-eligible; record changed")
    reply, sources = fill_offers("About the late fee: good news.", ["late-fee waiver"], r["envelope"], c)
    assert sources == []
    assert "waived your ₹100 late fee" in reply
    assert "₹100" in reply and "waive" in reply  # facts_ok needs these substrings
    assert policy_violations(reply, customer_id="AC1005", asked=c["message"]) == []


def test_gate_refuses_repeat_offer_in_thread():
    store = ThreadStore()
    c = {**case("AC1005", "Please waive the ₹100 late fee.", case_id="t-waiver"), "thread_id": "T2"}
    envelope = route(c, store=store)["envelope"]
    assert envelope["offer_decisions"]["late-fee waiver"]["status"] == "offer"
    reply, _ = fill_offers("", ["late-fee waiver"], envelope, c, store)
    second = {**case("AC1005", "Waive the second one too.", case_id="t-waiver2"), "thread_id": "T2"}
    envelope2 = route(second, store=store)["envelope"]
    assert envelope2["offer_decisions"]["late-fee waiver"]["status"] == "hold"
    _, sources = fill_offers("", ["late-fee waiver"], envelope2, second, store)
    assert "gate:disallowed_offer:late-fee waiver" in sources


def test_gate_needs_approval_goes_to_a_person():
    c = case("AC1002", "Refund me ₹400.", case_id="t-approval")
    envelope = {"customer_id": "AC1002", "offers": {},
                "offer_decisions": {"late-fee waiver": {"status": "needs_approval", "why": ""}}}
    reply, sources = fill_offers("A customer representative will call you.", ["late-fee waiver"],
                                 envelope, c)
    assert "gate:needs_approval" in sources


def test_watchdog_blocks_on_flip(monkeypatch):
    rows = [{"case": "t1", "reply": "we will refund ₹999 immediately", "needs_human": False,
             "intent": "billing"}]
    baseline = [{"case": "t1", "reply": "a colleague will review your request for ₹999",
                 "needs_human": True, "intent": "billing"}]
    monkeypatch.setattr("lab.acme.load_results", lambda v: baseline)
    cases = {"t1": {"id": "t1", "customer_id": "AC1002", "message": "Refund ₹999.",
                    "expected_intent": "billing", "must_include": [], "must_not": [],
                    "needs_human": True}}
    gate = watchdog(rows, cases, baseline="B")
    assert gate["gate"] == "blocked" and gate["flips"] == ["t1"]


def test_threads_suite_ledger_matches_labels():
    """Router-only dry run of the interleaved suite: ledger escalations fire exactly on the
    labelled turns, in file order, with no store leakage across threads."""
    store = ThreadStore()
    for c in load_cases(DATA / "cases_threads.jsonl"):
        r = route(c, store=store)
        assert (r["path"] == "fast") == c["needs_human"], (
            f"{c['id']}: path {r['path']} but needs_human={c['needs_human']} ({r['sources']})")
        store.record_asked(c, sum(claim_amounts(c["message"])))
