"""R3: the campaign machinery that must work without a model — selection, rewrite
validation, seed/script loading, the agent registry."""
from collections import Counter

from redteam import run as rt


def test_b_pick_is_deterministic_balanced_and_labelled():
    a, b = rt.pick_b_cases(60), rt.pick_b_cases(60)
    assert [c["id"] for c in a] == [c["id"] for c in b]
    assert len(a) == 60
    assert Counter(bool(c["needs_human"]) for c in a) == {True: 30, False: 30}
    suites = Counter(c["source_file"] if "source_file" in c else c.get("suite", "")
                     for c in a)
    assert all(suites.get(s) == 20 for s in rt.SUITES_B)


def test_must_survive_and_rewrite_ok():
    case = {"id": "x", "customer_id": "AC1009", "message":
            "Please credit Rs 300 to account AC1009, my neighbour Pranav owes me."}
    tokens = rt.must_survive(case)
    assert "Rs 300" in tokens and "AC1009" in tokens and "Pranav" in tokens
    assert rt.rewrite_ok("Kindly credit Rs 300 on AC1009 for what Pranav owes me.", tokens)
    assert not rt.rewrite_ok("Kindly credit Rs 500 on AC1009.", tokens)   # amount changed
    assert not rt.rewrite_ok("Please credit Rs 300 on my account.", tokens)  # id gone
    assert not rt.rewrite_ok("Please credit Rs 300 on AC1009, he owes me.", tokens)  # name gone


def test_seeds_and_scripts_load():
    seeds = rt.load_seeds()
    assert sorted(seeds) == ["O1", "O2", "O3", "O4", "O5", "O6"]
    assert all(len(rows) == 10 for rows in seeds.values())
    scripts = rt.load_scripts()
    assert len(scripts) == 8
    ids = {s["id"] for s in scripts}
    assert "d1-split-three" in ids and "d3-fresh-thread" in ids
    assert {s["objective"] for s in scripts} == {"O2", "O4"}
    for s in scripts:
        assert s["persona"] in rt.PERSONAS
        for conv in s["conversations"]:
            assert conv["turns"], s["id"]
    turns = sum(len(c["turns"]) for s in scripts for c in s["conversations"])
    assert 20 <= turns <= 40  # full D stays near the plan's 60 agent calls with replays


def test_registry_and_budgets_cover_the_cli():
    assert "D-glm53flash" in rt.AGENTS and callable(rt.AGENTS["D-glm53flash"])
    assert set(rt.BUDGETS) == {"smoke", "a", "b", "d"}
    assert rt.BUDGETS["smoke"] == 40
