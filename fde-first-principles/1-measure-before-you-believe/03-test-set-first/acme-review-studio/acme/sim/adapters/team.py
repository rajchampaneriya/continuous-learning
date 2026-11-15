"""A multi-agent team: triage hands the case to a specialist, who hands the draft to a reviewer.

Each agent is an ``agent`` span and each transfer a ``handoff`` span, both at the top level in the order they
happened, so the swimlane renderer can lay them out without knowing the team.
"""
from __future__ import annotations

import threading
import time
from typing import Any

from acme.providers import C3Provider, OfflineProvider

from ..trace import Capabilities, RunInput, RunResult, Span, Topology
from ..versions import Version
from .common import direct_output
from .direct import DirectAdapter, raw_response, turn_spans, usage_of

TRIAGE, REVIEWER = "Triage", "Reviewer"
# Intent -> the specialist agent that drafts the reply.
SPECIALISTS = {"billing": "Billing", "outage": "Network", "speed": "Network", "cancel": "Account",
               "upgrade": "Account", "relocation": "Account", "other": "General"}


def team_topology() -> dict[str, Any]:
    specialists = sorted(set(SPECIALISTS.values()))
    return {"nodes": [TRIAGE, *specialists, REVIEWER],
            "edges": [[TRIAGE, name] for name in specialists] + [[name, REVIEWER] for name in specialists]}


def triage(message: str) -> tuple[str, list[str]]:
    """Route by the offline keyword table: the intent and the words that matched it."""
    text = message.lower()
    matches = {intent: [word for word in words if word in text]
               for intent, words in OfflineProvider.KEYWORDS.items()}
    intent = max(matches, key=lambda key: len(matches[key]))
    return (intent, matches[intent]) if matches[intent] else ("other", [])


def _ms(started: float) -> int:
    return int((time.monotonic() - started) * 1000)


class MultiAgentAdapter(DirectAdapter):
    implementation = "multi_agent"

    def _provider(self, version: Version):
        config = version.content["config"]
        if config["provider"] != "c3":
            return OfflineProvider()
        return C3Provider(model=config["model"], lab_root=self.registry.lab_root,
                          data_root=self.registry.lab_data(version), temperature=config["temperature"],
                          max_steps=config["max_steps"], timeout=config["timeout_s"], persist_cache=False)

    def capabilities(self, version: Version) -> Capabilities:
        c3 = version.content["config"]["provider"] == "c3"
        return Capabilities(prompts=c3, tool_calls=c3, envelope=c3)

    def topology(self, version: Version) -> Topology:
        team = team_topology()
        return Topology(nodes=[{"id": name, "name": name} for name in team["nodes"]],
                        edges=[{"source": source, "target": target} for source, target in team["edges"]])

    def start(self, version: Version, run_input: RunInput, run_id: str, sample: int = 0,
              recorded: dict[str, Any] | None = None,
              cancelled: threading.Event | None = None) -> RunResult:
        if recorded is not None:
            raise ValueError("This adapter does not support recorded replay")
        lab, config = self.registry.load_lab(version), version.content["config"]
        provider = self._provider(version)
        model = getattr(provider, "model", "")

        started = time.monotonic()
        intent, matched = triage(run_input.message)
        specialist = SPECIALISTS[intent]
        spans = [Span(id="triage", parent=None, kind="agent", name="Classify", status="ok", ms=_ms(started),
                      attrs={"agent": TRIAGE, "routed_intent": intent, "matched_words": matched})]
        customer = lab.customers.get(run_input.customer_id)
        if not customer:
            output = direct_output(lab, config, run_input, None, provider=provider.name, model=model)
            spans.append(Span(id="triage:verify", parent="triage", kind="guard", name="Verify account",
                              status="stop", ms=0, attrs={"reason": output["reasons"][0]}))
            return RunResult(run_id=run_id, version_id=version.id, state="completed", output=output, spans=spans)
        spans.append(Span(id="handoff-1", parent=None, kind="handoff", name=f"{TRIAGE} → {specialist}",
                          status="ok", ms=0, attrs={"from": TRIAGE, "to": specialist, "reason": f"intent {intent}"}))

        result = provider.draft("", "", {"message": run_input.message, "customer": customer,
                                         "outage": lab.outage_for(customer), "case_id": run_input.case_id,
                                         "customer_id": run_input.customer_id, "history": run_input.history,
                                         "sample": sample, "routed_intent": intent})
        if result["error"]:
            raise RuntimeError(result["error"])
        raw = raw_response(result)
        draft_ms = int(float(result.get("latency_s") or 0) * 1000)
        spans.append(Span(id="specialist", parent=None, kind="agent", name="Draft", status="ok", ms=draft_ms,
                          attrs={"agent": specialist, "model": model, "envelope": raw.get("envelope"),
                                 "draft_intent": (result["output"] or {}).get("intent")}))
        children = turn_spans(raw, "specialist", prefix="specialist:")
        spans.extend(children or [Span(id="specialist:draft", parent="specialist", kind="model_call",
                                       name="Draft reply", status="ok", ms=draft_ms,
                                       attrs={"tokens_in": raw.get("tokens_in"),
                                              "tokens_out": raw.get("tokens_out")})])
        spans.append(Span(id="handoff-2", parent=None, kind="handoff", name=f"{specialist} → {REVIEWER}",
                          status="ok", ms=0, attrs={"from": specialist, "to": REVIEWER, "reason": "draft ready"}))

        started = time.monotonic()
        output = direct_output(lab, config, run_input, result["output"], provider=provider.name, model=model)
        escalate = output["decision"] == "escalate"
        spans.append(Span(id="reviewer", parent=None, kind="agent", name="Escalate" if escalate else "Approve",
                          status="escalate" if escalate else "ok", ms=_ms(started),
                          attrs={"agent": REVIEWER, "decision": output["decision"], "reasons": output["reasons"]}))
        spans.extend(Span(id=f"reviewer:reason-{number}", parent="reviewer", kind="guard", name=reason,
                          status="escalate", ms=0) for number, reason in enumerate(output["reasons"]))
        return RunResult(run_id=run_id, version_id=version.id, state="completed", output=output, spans=spans,
                         usage=usage_of(raw, result))
