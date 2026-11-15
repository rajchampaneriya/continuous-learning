"""Grounding recall: does the envelope's grounded_kb_ids cover each case's kb_sources?

Usage (from fde-first-principles/): uv run python -m lab.grounding_report [--suite NAME]
Counts only KB ids; non-KB sources like "-" or "P5" are ignored.
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from .acme import data_root, load_cases
from .version_c3 import build_decision_envelope

KB_ID = re.compile(r"^KB\d+$")

SUITES: Dict[str, str] = {
    "base": "cases.jsonl",
    "abuse": "cases_abuse.jsonl",
    "multiturn": "cases_multiturn.jsonl",
    "regional": "cases_regional.jsonl",
    "threads": "cases_threads.jsonl",
}


def kb_only(sources: List[str]) -> List[str]:
    return [s for s in (sources or []) if KB_ID.match(s)]


def recall_for(cases: List[dict]) -> tuple[float, int, int, List[str]]:
    """Return (recall, hits, total, misses) for one suite of cases."""
    hits = total = 0
    misses: List[str] = []
    for case in cases:
        want = kb_only(case.get("kb_sources") or [])
        if not want:
            continue
        envelope = build_decision_envelope(case)
        got = set(envelope.get("grounded_kb_ids") or [])
        for kid in want:
            total += 1
            if kid in got:
                hits += 1
            else:
                misses.append(f"{case['id']}:{kid}")
    return (hits / total if total else 1.0), hits, total, misses


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", choices=sorted(SUITES), help="report one suite only")
    args = parser.parse_args()

    for suite, filename in SUITES.items():
        if args.suite and suite != args.suite:
            continue
        path = data_root() / filename
        if not path.exists():
            continue
        cases = load_cases(path)
        recall, hits, total, misses = recall_for(cases)

        per_intent: Dict[str, List[int]] = defaultdict(lambda: [0, 0])
        for case in cases:
            want = kb_only(case.get("kb_sources") or [])
            if not want:
                continue
            envelope = build_decision_envelope(case)
            got = set(envelope.get("grounded_kb_ids") or [])
            for kid in want:
                per_intent[case["expected_intent"]][1] += 1
                if kid in got:
                    per_intent[case["expected_intent"]][0] += 1

        print(f"{suite}: {hits}/{total} = {recall:.0%}")
        for intent, (h, t) in sorted(per_intent.items()):
            print(f"  {intent}: {h}/{t} = {h / t:.0%}")
        if misses:
            print("  misses: " + ", ".join(misses))


if __name__ == "__main__":
    main()
