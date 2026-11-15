"""--holdout runs print the aggregate summary only: no case ids, no replies (rule 6)."""
import json
import shutil
import sys
from pathlib import Path

import lab.acme as acme
from lab import run_c4
from lab.acme import DATA, use_data_root


def _fake_version(case, *, temperature=0.0, run=0, **kw):
    return {"intent": case["expected_intent"], "reply": "SECRETREPLY that must never reach the console",
            "needs_human": case["needs_human"], "tokens_in": 1, "tokens_out": 1, "seconds": 0.0}


def _two_holdout_cases() -> list[dict]:
    return [
        {"id": "h01", "customer_id": "AC1001", "message": "Please cancel my connection.",
         "expected_intent": "cancel", "must_include": [], "must_not": [], "needs_human": False},
        {"id": "h02", "customer_id": "AC1002", "message": "Refund me Rs 900.",
         "expected_intent": "billing", "must_include": [], "must_not": [], "needs_human": True},
    ]


def _temp_root(tmp_path: Path, with_holdout: bool) -> Path:
    root = tmp_path / "acme"
    shutil.copytree(DATA, root, ignore=shutil.ignore_patterns("holdout"))
    if with_holdout:
        holdout = root / "holdout"
        holdout.mkdir()
        (holdout / "cases_holdout.jsonl").write_text(
            "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in _two_holdout_cases()),
            encoding="utf-8")
    return root


def test_holdout_run_prints_no_case_id(tmp_path, monkeypatch, capsys):
    root = _temp_root(tmp_path, with_holdout=True)
    monkeypatch.setattr(run_c4, "version_c4", _fake_version)
    monkeypatch.setattr(acme, "DATA", root)
    monkeypatch.setattr(acme, "RESULTS", tmp_path / "results")
    monkeypatch.setattr(sys, "argv", ["run_c4", "--holdout", "--version", "T-hold"])
    with use_data_root(root):
        run_c4.main()
    out = capsys.readouterr().out
    assert "h01" not in out and "h02" not in out
    assert "SECRETREPLY" not in out
    saved = tmp_path / "results" / "T-hold-holdout.jsonl"
    assert saved.exists() and len(saved.read_text().splitlines()) == 2
    meta = json.loads((tmp_path / "results" / "T-hold-holdout.meta.json").read_text())
    assert meta["holdout_sha"] and meta["git_commit"]


def test_holdout_missing_file_prints_not_found_and_exits_0(tmp_path, monkeypatch, capsys):
    root = _temp_root(tmp_path, with_holdout=False)
    monkeypatch.setattr(acme, "DATA", root)
    monkeypatch.setattr(acme, "RESULTS", tmp_path / "results")
    monkeypatch.setattr(sys, "argv", ["run_c4", "--holdout"])
    with use_data_root(root):
        run_c4.main()  # exits 0: plain return
    assert "holdout not found" in capsys.readouterr().out
