"""Re-grade a finished run from its turns.jsonl alone.

    python -m redteam.report <run>

Every verdict is recomputed with lab code from the logged case and row — never
trusted from the run — and compared with the verdict logged at run time; a
mismatch means the log or the checks changed underneath us. Writes report.md
and summary.json next to the log, and prints the markdown.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List


def run_dir(run: str, root: Path | None = None) -> Path:
    return (root or Path("data/redteam")) / run


def regrade(lines: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """One entry per line: the recomputed verdict, the logged one, whether they agree."""
    from redteam.scorers import verdict

    replies: Dict[str, List[str]] = defaultdict(list)
    out: List[Dict[str, Any]] = []
    for line in lines:
        replies[line["conversation"]].append(line["row"].get("reply") or "")
        v = verdict(line, replies[line["conversation"]])
        logged = line.get("verdict")
        out.append({"conversation": line["conversation"], "turn": line.get("turn"),
                    "objective": line.get("objective", ""), "recomputed": v, "logged": logged,
                    "match": logged is None or logged == v})
    return out


def summary(graded: List[Dict[str, Any]]) -> Dict[str, Any]:
    def n(pred) -> int:
        return sum(1 for g in graded if pred(g))

    by_objective = {obj: {"turns": n(lambda g, obj=obj: g["objective"] == obj),
                          "objective_met": n(lambda g, obj=obj: g["objective"] == obj
                                             and g["recomputed"]["objective_met"]),
                          "unattended": n(lambda g, obj=obj: g["objective"] == obj
                                          and g["recomputed"]["unattended"]),
                          "handoff": n(lambda g, obj=obj: g["objective"] == obj
                                       and g["recomputed"]["handoff"])}
                    for obj in sorted({g["objective"] for g in graded} - {""})}
    return {"turns": len(graded), "objective_met": n(lambda g: g["recomputed"]["objective_met"]),
            "unattended": n(lambda g: g["recomputed"]["unattended"]),
            "handoff": n(lambda g: g["recomputed"]["handoff"]),
            "verdict_mismatches": n(lambda g: not g["match"]), "by_objective": by_objective}


def markdown(run: str, graded: List[Dict[str, Any]], s: Dict[str, Any]) -> str:
    lines = [f"# Red-team run `{run}`", "",
             f"- turns: {s['turns']}  objective met: {s['objective_met']}  "
             f"unattended: {s['unattended']}  hand-offs: {s['handoff']}  "
             f"verdict mismatches: {s['verdict_mismatches']}", "",
             "| objective | turns | met | unattended | hand-offs |", "| --- | --- | --- | --- | --- |"]
    for obj, o in s["by_objective"].items():
        lines.append(f"| {obj} | {o['turns']} | {o['objective_met']} | {o['unattended']} | {o['handoff']} |")
    lines += ["", "| conversation | turn | objective | verdict | fired |", "| --- | --- | --- | --- | --- |"]
    for g in graded:
        v = g["recomputed"]
        flag = "" if g["match"] else " **LOG MISMATCH**"
        lines.append(f"| {g['conversation'][:8]} | {g['turn']} | {g['objective']} | "
                     f"{'MET' if v['objective_met'] else 'held'}{flag} | {v['why']} |")
    return "\n".join(lines) + "\n"


def compare_markdown(run_a: str, run_b: str) -> str:
    """Both versions side by side, paired on the same attacks (plan reporting rule 5)."""
    s = {}
    for run in (run_a, run_b):
        path = run_dir(run) / "turns.jsonl"
        lines = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l]
        s[run] = summary(regrade(lines))
    head = [f"# `{run_a}` vs `{run_b}`", "",
            "| metric | " + " | ".join(s.keys()) + " |", "| --- | --- | --- |",
            f"| turns | {s[run_a]['turns']} | {s[run_b]['turns']} |",
            f"| objective met | {s[run_a]['objective_met']} | {s[run_b]['objective_met']} |",
            f"| unattended | {s[run_a]['unattended']} | {s[run_b]['unattended']} |",
            f"| hand-offs | {s[run_a]['handoff']} | {s[run_b]['handoff']} |",
            f"| verdict mismatches | {s[run_a]['verdict_mismatches']} | {s[run_b]['verdict_mismatches']} |",
            "", "| objective | met a | unatt a | met b | unatt b |", "| --- | --- | --- | --- | --- |"]
    objs = sorted(set(s[run_a]["by_objective"]) | set(s[run_b]["by_objective"]))
    for obj in objs:
        a = s[run_a]["by_objective"].get(obj, {})
        b = s[run_b]["by_objective"].get(obj, {})
        head.append(f"| {obj} | {a.get('objective_met', 0)} | {a.get('unattended', 0)} | "
                    f"{b.get('objective_met', 0)} | {b.get('unattended', 0)} |")
    return "\n".join(head) + "\n"


def main(argv: List[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) == 2:
        md = compare_markdown(argv[0], argv[1])
        out = run_dir(argv[0]) / f"compare-{argv[1]}.md"
        out.write_text(md, encoding="utf-8")
        print(md, end="")
        return 0
    if len(argv) != 1:
        print("usage: python -m redteam.report <run> [second-run-for-compare]", file=sys.stderr)
        return 2
    path = run_dir(argv[0]) / "turns.jsonl"
    lines = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l]
    graded = regrade(lines)
    s = summary(graded)
    md = markdown(argv[0], graded, s)
    out = path.parent
    (out / "report.md").write_text(md, encoding="utf-8")
    (out / "summary.json").write_text(json.dumps(s, indent=1) + "\n", encoding="utf-8")
    print(md, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
