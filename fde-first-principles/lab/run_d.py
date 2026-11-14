"""Run Version D (router and workers) against the Acme test sets, paired against C4.

Usage, from fde-first-principles/:

    LLM_MAX_CALLS=2000 uv run python -m lab.run_d              # 256 emails + threads suite
    LLM_MAX_CALLS=2000 uv run python -m lab.run_d --limit 3    # smoke test
    uv run python -m lab.run_d --only c01                      # single case, prints the reply

Measures, per the Version D plan:
- same 256 emails as C4 (base, abuse, multiturn, regional), then the interleaved-threads suite
  (cases_threads.jsonl) with the ThreadStore ledger carrying claims across turns;
- p50/p95 seconds and tokens against the saved C4 run;
- the Watchdog flip gate: zero cases C4 answered safely that D breaks, or promotion is blocked.
"""
from __future__ import annotations

import argparse
import json
import statistics
import time

from .acme import DATA, RESULTS, load_cases, save_results
from .evals import score, summary
from .llm import api_usage, use
from .version_d import ThreadStore, version_d, watchdog

MODEL = "anthropic:glm-5.3-flash"
CASE_FILES = ["cases.jsonl", "cases_abuse.jsonl", "cases_multiturn.jsonl", "cases_regional.jsonl"]
THREADS_FILE = "cases_threads.jsonl"
VERSION = "D-glm53flash"
BASELINE = "C4-glm53flash"


def all_cases() -> list[dict]:
    out = []
    for name in CASE_FILES + [THREADS_FILE]:
        for case in load_cases(DATA / name):
            out.append({**case, "source_file": name})
    return out


def _p(scores: list[float], q: float) -> float:
    return round(statistics.quantiles(scores, n=20, method="inclusive")[int(q * 20) - 1], 1) if len(scores) >= 2 else round(scores[0], 1)


def paired_metrics(rows: list[dict], baseline: str = BASELINE) -> dict:
    """D vs the saved C4 run: p50/p95 seconds and mean tokens per case (paired by case id)."""
    path = RESULTS / f"{baseline}.jsonl"
    if not path.exists():
        return {"baseline": baseline, "note": "baseline run not found; skipped"}
    base = {json.loads(line)["case"]: json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
    pairs = [(r, base[r["case"]]) for r in rows if r["case"] in base]
    if not pairs:
        return {"baseline": baseline, "note": "no shared cases; skipped"}
    d_s = [r["seconds"] for r, _ in pairs]
    b_s = [b["seconds"] for _, b in pairs]
    return {
        "baseline": baseline, "n_pairs": len(pairs),
        "seconds_p50": _p(d_s, .50), "baseline_seconds_p50": _p(b_s, .50),
        "seconds_p95": _p(d_s, .95), "baseline_seconds_p95": _p(b_s, .95),
        "tokens_in_mean": round(sum(r["tokens_in"] for r, _ in pairs) / len(pairs)),
        "baseline_tokens_in_mean": round(sum(b["tokens_in"] for _, b in pairs) / len(pairs)),
        "fast_path_share": round(sum(1 for r, _ in pairs if r.get("path") == "fast") / len(pairs), 3),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="run only the first N cases")
    ap.add_argument("--only", type=str, default=None, help="run one case id and print the reply")
    ap.add_argument("--version", type=str, default=VERSION, help="results file name")
    ap.add_argument("--baseline", type=str, default=BASELINE, help="C4 run to pair against")
    args = ap.parse_args()

    cases = all_cases()
    if args.only:
        cases = [c for c in cases if c["id"] == args.only]
    elif args.limit:
        cases = cases[: args.limit]

    use(MODEL)
    store = ThreadStore(log_path=RESULTS / f"{args.version}-threads.jsonl")
    rows: list[dict] = []
    started = time.time()
    for i, case in enumerate(cases, 1):
        t0 = time.time()
        row = version_d(case, temperature=0.0, run=0, store=store)
        s = score(case, row)
        rows.append({"case": case["id"], "source_file": case["source_file"],
                     "customer_id": case["customer_id"], **row})
        print(f"[{i}/{len(cases)}] {case['id']} ({case['source_file']}, {row.get('path')}) "
              f"{'PASS' if s['passed'] else 'FAIL ' + ','.join(k for k in ('intent_ok','facts_ok','policy_ok','human_ok') if not s[k])}"
              f" {row['seconds']:.0f}s", flush=True)
        if args.only:
            print(json.dumps({k: row.get(k) for k in ("intent", "reply", "needs_human", "offers_filled",
                                                      "path", "escalation_sources")}, indent=2,
                             ensure_ascii=False))

    scores = [score(next(c for c in cases if c["id"] == r["case"]), r) for r in rows]
    print("\n== overall ==", flush=True)
    print(json.dumps(summary(scores), indent=1, default=str))
    for name in CASE_FILES + [THREADS_FILE]:
        part = [s for s, r in zip(scores, rows) if r["source_file"] == name]
        if part:
            print(f"\n== {name} (n={len(part)}) ==")
            print(json.dumps(summary(part), indent=1, default=str))

    print("\n== paired vs C4 ==")
    print(json.dumps(paired_metrics(rows, args.baseline), indent=1))

    gate = watchdog(rows, {c["id"]: c for c in cases}, baseline=args.baseline)
    print("\n== watchdog (flip gate; safe-in-C4 cases D must not break) ==")
    print(json.dumps(gate, indent=1))

    path = save_results(args.version, rows, meta={
        "model": MODEL, "temperature": 0.0, "files": CASE_FILES + [THREADS_FILE],
        "n_total": len(rows), "wall_seconds": round(time.time() - started, 1),
        "api_usage": api_usage(), "watchdog": gate,
    })
    print(f"\nsaved {len(rows)} rows -> {path}")


if __name__ == "__main__":
    main()
