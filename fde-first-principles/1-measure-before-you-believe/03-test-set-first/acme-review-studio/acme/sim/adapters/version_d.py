"""Adapter for the lab's rule-first Version D agent."""
from __future__ import annotations

import threading
import time
from contextlib import nullcontext
from typing import Any

from acme.providers import c3_output

from .common import direct_output
from ..trace import RunInput, RunResult, Span
from ..versions import Version
from .direct import AgentLoopAdapter, turn_spans


def version_d_topology() -> dict[str, Any]:
    return {"nodes": ["Router", "Worker", "Gate"],
            "edges": [["Router", "Worker"], ["Worker", "Gate"], ["Router", "Gate"]]}


class VersionDAdapter(AgentLoopAdapter):
    """Run Version D against the frozen lab data and expose its model/tool trace."""

    def __init__(self, registry, checkpoints, log_path):
        super().__init__(registry, checkpoints, log_path)
        self._thread_stores: dict[int, Any] = {}
        self._thread_locks: dict[int, threading.RLock] = {}
        self._thread_state_lock = threading.Lock()

    def start(self, version: Version, run_input: RunInput, run_id: str, sample: int = 0,
              recorded: dict[str, Any] | None = None,
              cancelled: threading.Event | None = None) -> RunResult:
        if recorded is not None:
            raise ValueError("This adapter does not support recorded replay")
        if cancelled is not None and cancelled.is_set():
            raise TimeoutError("Version D run was cancelled")

        from lab import version_d
        from lab.acme import use_data_root

        lab, config = self.registry.load_lab(version), version.content["config"]
        model = config["model"]
        customer = lab.customers.get(run_input.customer_id)
        if not customer:
            output = direct_output(lab, config, run_input, None, provider="c3", model=model)
            return RunResult(run_id=run_id, version_id=version.id, state="completed", output=output,
                             spans=[Span(id="verify", parent=None, kind="guard", name="Verify account",
                                         status="stop", ms=0, attrs={"reason": output["reasons"][0]})])

        case = dict(run_input.case or {})
        case.update(id=run_input.case_id, customer_id=run_input.customer_id,
                    message=run_input.message, history=run_input.history)
        store = None
        lock = nullcontext()
        if case.get("thread_id"):
            from lab.version_d import ThreadStore

            with self._thread_state_lock:
                store = self._thread_stores.get(sample)
                if store is None:
                    store = self._thread_stores[sample] = ThreadStore()
                lock = self._thread_locks.setdefault(sample, threading.RLock())

        with lock, use_data_root(self.registry.lab_data(version)):
            routed = version_d.route(case, store=store)
            started = time.monotonic()
            draft, turns = version_d.run_agent(
                case, temperature=config["temperature"], run=sample, model=model,
                max_steps=config["max_steps"], timeout=config["timeout_s"],
                persist_cache=False, store=store,
            )
            if store is not None:
                store.record_asked(case, sum(version_d.money_asked(case)))

            tool_calls = [{"name": call[0], "result": call[2]}
                          for turn in turns for call in turn.get("tool_calls", [])]
            row = {**draft, "tool_calls": tool_calls}
            customer_outage = lab.outage_for(customer)
            normalized = c3_output(row, customer_outage)
            normalized["cited_sources"] = list(dict.fromkeys(["CRM", *normalized["cited_sources"]]))
            output = direct_output(lab, config, run_input, normalized, provider="c3", model=model)
            output.update({key: draft[key] for key in
                           ("path", "offers_filled", "offers_raw", "escalation_sources") if key in draft})

        elapsed_ms = int(sum(float(turn.get("seconds") or 0) * 1000 for turn in turns))
        spans = [
            Span(id="agent", parent=None, kind="agent", name="Version D agent loop",
                 status="escalate" if output["decision"] == "escalate" else "ok", ms=elapsed_ms,
                 attrs={"agent": "Version D", "path": routed["path"], "envelope": routed["envelope"]}),
            *turn_spans({"turns": turns, "escalation_sources": draft.get("escalation_sources")}, "agent"),
        ]
        usage = {"latency_s": round(time.monotonic() - started, 3), "cost_usd": None,
                 "tokens_in": sum(int(turn.get("tokens_in") or 0) for turn in turns),
                 "tokens_out": sum(int(turn.get("tokens_out") or 0) for turn in turns)}
        return RunResult(run_id=run_id, version_id=version.id, state="completed", output=output,
                         spans=spans, usage=usage)
