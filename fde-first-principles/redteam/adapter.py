"""The red-team adapter: one PyRIT-style conversation = one email thread, logged.

Pyrit-free core so the feature tests run without the redteam dependency group:
the PyRIT PromptTarget in redteam/spike.py (and later redteam/target.py) is a
thin wrapper around `AcmeAdapter.handle`. Every send replays the earlier
customer turns into a fresh ThreadStore — the ledger is rebuilt from history,
never carried over between sends — then runs the new turn and appends one line
to the run's turns.jsonl. Replay rows are rebuilds, not events: only the new
turn is logged.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from lab.version_d import ThreadStore, version_d

Pieces = List[Dict[str, str]]  # [{"role": "customer"|"assistant"|"system", "text": str}]


class RefusedSystemPrompt(ValueError):
    """A customer cannot set the agent's system prompt."""


def find_system_prompt(pieces: Pieces) -> Optional[str]:
    return next((p["text"] for p in pieces if p.get("role") == "system"), None)


class TurnLog:
    """One JSON line per agent call: run, conversation, turn, objective, strategy,
    converters, persona, agent, the full case and the full agent row."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, line: Dict[str, Any]) -> None:
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(line, ensure_ascii=False) + "\n")

    def lines(self) -> List[Dict[str, Any]]:
        if not self.path.exists():
            return []
        return [json.loads(l) for l in self.path.read_text(encoding="utf-8").splitlines() if l]


class AcmeAdapter:
    """Runs an agent callable over a conversation as the customer would experience it."""

    def __init__(self, *, agent: Callable = version_d, agent_name: str = "D",
                 customer_id: str = "", persona: str = "", run: str = "",
                 log: Optional[TurnLog] = None) -> None:
        self.agent = agent
        self.agent_name = agent_name
        self.customer_id = customer_id
        self.persona = persona
        self.run = run
        self.log = log
        self.replies: Dict[str, List[str]] = {}  # conversation_id -> replies so far

    def handle(self, conversation_id: str, pieces: Pieces,
               *, objective: str = "", strategy: str = "",
               converters: Optional[List[str]] = None) -> Dict[str, Any]:
        """Replay the conversation's earlier customer turns into a fresh ledger,
        run the new email, log exactly one line, return the agent row."""
        system = find_system_prompt(pieces)
        if system is not None:
            raise RefusedSystemPrompt("a customer cannot set the agent's system prompt")
        history = [{"role": p["role"], "text": p["text"]} for p in pieces[:-1]
                   if p["role"] in ("customer", "assistant")]
        message = pieces[-1]["text"]

        case = {"id": f"rt-{conversation_id[:8]}-t{len(history) + 1}", "thread_id": conversation_id,
                "customer_id": self.customer_id, "history": history, "message": message}
        store = ThreadStore()
        self.last_store = store
        # Lab fidelity: version_d prices money_asked over the whole customer_text and
        # records it after every call, so — exactly like run_d's thread suite — the agent
        # callable gets each turn as a bare case and thread continuity lives in the store.
        # The conversation history stays in `case` for the log and the scorers.
        for i, turn in enumerate(history):
            if turn["role"] == "customer":
                self.agent({"id": f"rt-{conversation_id[:8]}-t{i + 1}", "thread_id": conversation_id,
                            "customer_id": self.customer_id, "history": [],
                            "message": turn["text"]}, store=store)
        self.last_case = case
        row = self.agent({**case, "history": []}, store=store)
        self.replies.setdefault(conversation_id, []).append(row["reply"])
        if self.log is not None:
            line = {"run": self.run, "conversation": conversation_id,
                    "turn": len(history) + 1, "objective": objective,
                    "strategy": strategy, "converters": converters or [],
                    "persona": self.persona, "agent": self.agent_name,
                    "case": case, "row": row}
            from redteam.scorers import verdict
            line["verdict"] = verdict(line, self.replies[conversation_id])
            self.log.append(line)
        return row
