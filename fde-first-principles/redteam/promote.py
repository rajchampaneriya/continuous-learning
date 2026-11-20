"""Turn confirmed findings into draft regression cases (plan step: promote).

    uv run python -m redteam.promote <run>

Reads the triage rows a person marked `human_score=real`, drafts one lab-schema
case per finding (reviewed: false, tagged redteam) in
data/acme/cases_redteam.jsonl, and blind-appends a random half to
data/acme/holdout/cases_holdout.jsonl — appended without ever being read or
printed here. Prints counts only.
"""
from __future__ import annotations

import csv
import json
import random
import sys
from pathlib import Path
from typing import Dict, List

from lab.acme import data_root
from redteam.scorers import expected_handoff
from redteam.triage import load_lines

DRAFTS_FILE = "cases_redteam.jsonl"
HOLDOUT_APPEND = "holdout/cases_holdout.jsonl"


def draft_case(line: Dict) -> Dict:
    case, row = line["case"], line["row"]
    fired = line.get("verdict", {}).get("fired", [])
    return {"id": f"rt-{line['conversation'][:8]}-t{line.get('turn')}",
            "customer_id": case.get("customer_id"), "conversation_type": "email",
            "message": case.get("message"), "history": case.get("history", []),
            "expected_intent": row.get("intent", ""),
            "must_include": [], "must_not": [],
            "needs_human": bool(expected_handoff(line)), "concession_allowed": False,
            "tags": ["redteam", line.get("objective", "")], "reviewed": False,
            "language": "English", "difficulty": "TBD",
            "rationale": f"red-team finding ({line.get('strategy')}): {', '.join(fired) or 'human-judged'}"}


def promote(run: str, seed: int = 1701) -> Dict[str, int]:
    triage_path = Path("data/redteam") / run / "triage.csv"
    with triage_path.open(encoding="utf-8", newline="") as fh:
        confirmed = [r for r in csv.DictReader(fh) if r["human_score"] == "real"]
    lines = {(l["conversation"][:12], l.get("turn")): l for l in load_lines(run)}

    drafts_path = data_root() / DRAFTS_FILE
    existing = {json.loads(l)["id"] for l in drafts_path.read_text(
        encoding="utf-8").splitlines()} if drafts_path.exists() else set()
    # The holdout is never read back, so a ledger in the run dir is the only
    # record of which findings were already sealed there.
    ledger_path = Path("data/redteam") / run / "promoted.json"
    ledger = set(json.loads(ledger_path.read_text(encoding="utf-8"))) if ledger_path.exists() else set()

    keep, seal = [], []
    for r in confirmed:
        line = lines.get((r["conversation"], int(r["turn"] or 0)))
        if not line:
            continue
        case = draft_case(line)
        if case["id"] in existing or case["id"] in ledger:
            continue
        (seal if random.Random(seed).random() < 0.5 else keep).append(case)
        ledger.add(case["id"])

    with drafts_path.open("a", encoding="utf-8") as fh:
        for c in keep:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    if seal:  # blind append: never read, never printed
        holdout = data_root() / HOLDOUT_APPEND
        holdout.parent.mkdir(parents=True, exist_ok=True)
        with holdout.open("a", encoding="utf-8") as fh:
            for c in seal:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    ledger_path.write_text(json.dumps(sorted(ledger), ensure_ascii=False) + "\n", encoding="utf-8")
    return {"confirmed": len(confirmed), "kept": len(keep), "sealed": len(seal)}


def main(argv: List[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print("usage: python -m redteam.promote <run>", file=sys.stderr)
        return 2
    print(json.dumps(promote(argv[0])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
