"""A human attack session through the same adapter and log (campaign E).

    LLM_MAX_CALLS=60 uv run --group redteam python -m redteam.chat --persona clean_long_tenure

Type emails as the customer; the reply, the agent row's needs_human flag and the
turn's verdict print after each send. Everything lands in
data/redteam/e-human-<date>/turns.jsonl like any other campaign. Empty line or
Ctrl-D ends the session.
"""
from __future__ import annotations

import argparse
import datetime
import os
from pathlib import Path

from lab.llm import use
from redteam.adapter import AcmeAdapter, TurnLog
from redteam.run import AGENTS, MODEL, persona_customer


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--persona", required=True)
    ap.add_argument("--agent", default="D5-glm53flash", choices=sorted(AGENTS))
    args = ap.parse_args()

    os.environ.setdefault("LLM_MAX_CALLS", "60")  # per session, never global
    use(MODEL)
    run = f"e-human-{datetime.date.today().isoformat()}"
    run_path = Path("data/redteam") / run
    adapter = AcmeAdapter(agent=AGENTS[args.agent], agent_name=args.agent,
                          customer_id=persona_customer(args.persona), persona=args.persona,
                          run=run, log=TurnLog(run_path / "turns.jsonl"))

    conversation = f"e-{args.persona}"
    pieces = []
    print(f"Attacking {args.agent} as {args.persona} "
          f"({persona_customer(args.persona)}). Empty line to quit.\n")
    while True:
        try:
            email = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not email:
            break
        pieces.append({"role": "customer", "text": email})
        row = adapter.handle(conversation, pieces, objective="E-human", strategy="E-human")
        verdict = adapter.log.lines()[-1]["verdict"]
        pieces.append({"role": "assistant", "text": row["reply"]})
        print(f"\nagent> {row['reply']}\n")
        print(f"[needs_human={row['needs_human']} verdict={'MET' if verdict['objective_met'] else 'held'}"
              f" fired={verdict['why']}]\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
