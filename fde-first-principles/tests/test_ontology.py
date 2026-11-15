"""Step definitions for features/ontology.feature and business graph engine tests."""
import json
import re
import shutil

import pytest
from pytest_bdd import parsers, scenarios, then, when

from lab.acme import DATA, use_data_root
from lab.business_rules import load_business_rules
from lab.evals import policy_violations, score
from lab.ontology import (
    PREFIXES,
    _asserted_store,
    _store,
    compute_entitlements,
    concept_labels,
    concept_provenance,
    customer_subgraph,
    define,
    domain_edges,
    excluded_from_limit,
    extract_concepts,
    glossary,
    plans,
    policy_rules,
    pune_service_areas,
    terms,
    validate_ontology_ops,
)
from lab.version_c3 import (
    build_decision_envelope,
    check_entitlement,
    define_term,
    run_agent,
    search_kb_c3,
)

scenarios("features/ontology.feature")


@pytest.fixture
def world():
    return {}


@when("the grader asks which kinds of money are excluded from the limit")
def ask_excluded(world):
    world["answer"] = ", ".join(excluded_from_limit())


@when(parsers.parse('an agent looks up "{word}"'))
def look_up(world, word):
    world["definition"] = define(word)


@when(parsers.parse('the engine extracts concepts from "{text}"'))
def extract_concepts_from(world, text):
    world["concepts"] = [c["term"] for c in extract_concepts(text)]


@then(parsers.parse('"{concept}" is matched'))
def concept_is_matched(world, concept):
    assert concept in world["concepts"], world["concepts"]


@when("a prompt asks for the glossary")
def ask_glossary(world):
    world["glossary"] = glossary()


@when("the reasoner inspects the ontology")
def inspect_reasoned_ontology(world):
    world["terms"] = terms()


@when("operations validates the ontology against live catalogs and business rules")
def run_ops_validation(world):
    world["ops"] = validate_ontology_ops()


@when(parsers.parse('the engine computes entitlements for customer "{customer_id}"'))
def compute_for_customer(world, customer_id):
    world["entitlements"] = compute_entitlements(customer_id)


@when(parsers.parse(
    "business operations raises the concession limit to {limit:d} rupees and lowers minimum tenure to {min_tenure:d} months"
))
def apply_commercial_rule_override(world, limit, min_tenure):
    world["rules_override"] = {
        "concession_limit": {"max_rupees_30_days": limit},
        "offers": {
            "retention offer": {"min_tenure_months": min_tenure},
            "late-fee waiver": {"min_tenure_months": min_tenure},
        },
    }


@then(parsers.parse('the answer is "{expected}"'))
def answer_is(world, expected):
    assert world["answer"] == expected


@then(parsers.parse('it gets the definition of "{term}"'))
def gets_definition(world, term):
    assert world["definition"] is not None and world["definition"]["term"] == term


@then(parsers.parse('the definition cites "{source}"'))
def cites(world, source):
    assert source in (world["definition"]["source"] or "")


@then("there is no definition")
def no_definition(world):
    assert world["definition"] is None


@then(parsers.parse('it contains "{text}"'))
def contains(world, text):
    assert text in world["glossary"]


@then("it contains no customer id")
def no_customer_id(world):
    assert not re.search(r"\bAC\d{4}\b", world["glossary"])


@then(parsers.parse('"{term}" inherits countsTowardLimit true'))
def check_inherited_props(world, term):
    info = world["terms"][term]
    assert info["counts_toward_limit"] is True


@then(parsers.parse('"{term}" has a {months:d}-month cooldown from business_rules.json'))
def check_business_rule_cooldown(world, term, months):
    assert world["terms"][term]["once_per_months"] == months


@then(parsers.parse('"{term}" overrides countsTowardLimit to false'))
def check_override_false(world, term):
    assert world["terms"][term]["counts_toward_limit"] is False


@then(parsers.parse('"{term}" inherits requiresRole "{role}"'))
def check_inherited_role(world, term, role):
    assert world["terms"][term]["requires_role"] == role


@then("the operational health check passes with zero drift errors")
def check_ops_clean(world):
    assert world["ops"]["ok"] is True, world["ops"]["drift_errors"]
    assert world["ops"]["stewardship_coverage"] == 1.0


@then(parsers.parse("the remaining 30-day headroom is {headroom:d} rupees"))
def check_headroom(world, headroom):
    assert world["entitlements"]["concession_headroom_rupees"] == headroom


@then(parsers.parse('eligibility for "{offer}" is {eligible}'))
def check_offer_eligibility(world, offer, eligible):
    expected = eligible.strip().lower() == "true"
    assert world["entitlements"]["offers"][offer]["eligible"] is expected


@then(parsers.parse('customer "{customer_id}" has {headroom:d} rupees of headroom and is eligible for "{offer}"'))
def check_overridden_entitlement(world, customer_id, headroom, offer):
    report = compute_entitlements(customer_id, rules=world["rules_override"])
    assert report["concession_headroom_rupees"] == headroom
    assert report["offers"][offer]["eligible"] is True


def test_domain_edges_and_ephemeral_subgraph_isolation():
    edges = domain_edges("retention offer")
    assert edges is not None
    assert "concession" in edges["superclasses"]
    assert "once-only offer" in edges["superclasses"]
    assert "KB11" in edges["kb_articles"]
    assert 10 in edges["policy_rules"]
    assert edges["owner_team"] == "Customer Retention & Lifecycle"
    assert plans()["Pro"]["price_rupees"] == 1499
    assert len(pune_service_areas()) == 8

    # Ephemeral customer subgraph must never leak into the shared TBox _store()
    base_size = len(_store())
    sub = customer_subgraph("AC1032")
    assert len(sub) > base_size
    assert len(_store()) == base_size


def test_concept_provenance_distinguishes_stated_and_inherited_facts():
    facts = concept_provenance("retention offer")
    assert facts is not None
    assert {
        (fact["property"], fact["value"], fact["origin"])
        for fact in facts
    } >= {
        ("countsTowardLimit", "false", "stated"),
        ("enforcesRule", "PolicyRule10", "stated"),
        ("enforcesRule", "PolicyRule3", "inherited"),
        ("enforcesRule", "PolicyRule8", "inherited"),
    }
    assert any(fact["property"] == "definition" and fact["origin"] == "stated" for fact in facts)
    assert next(fact for fact in facts
                if fact["property"] == "enforcesRule" and fact["value"] == "PolicyRule8")["inherited_from"] == "discount"
    assert next(fact for fact in facts
                if fact["property"] == "enforcesRule" and fact["value"] == "PolicyRule3")["inherited_from"] == "concession"
    assert concept_provenance("unknown concept") is None


def test_policy_rules_and_semantic_drift_are_visible():
    labels = concept_labels()
    assert labels["छूट"] == "discount"
    assert labels["late fee maaf"] == "late-fee waiver"

    policy = policy_rules()
    assert set(policy) == set(range(1, 14))
    assert "More than 12 months" in policy[10]

    health = validate_ontology_ops()
    assert health["ok"] is True
    assert health["drift_errors"] == []
    assert health["semantic_findings"] == []


@pytest.fixture
def semantic_data(tmp_path):
    for name in ("ontology.ttl", "business_rules.json", "policy.md", "kb.md", "customers.json", "outages.json"):
        shutil.copy2(DATA / name, tmp_path / name)
    with use_data_root(tmp_path):
        yield tmp_path


def _write_rules(path, rules):
    (path / "business_rules.json").write_text(json.dumps(rules, indent=2), encoding="utf-8")


def _finding(health, text):
    return next(finding for finding in health["findings"] if text in finding["finding"])


def test_legacy_policy_rule_checks_include_the_concession_limit(semantic_data):
    rules = load_business_rules()
    rules["concession_limit"]["policy_rules"] = [999]
    rules["offers"]["retention offer"]["policy_rules"] = [8, 10]
    _write_rules(semantic_data, rules)

    health = validate_ontology_ops()
    assert health["ok"] is False
    for concept in ("concession limit", "retention offer"):
        finding = _finding(health, f"{concept} policy rules differ")
        assert "business_rules.json" in finding["file_to_fix"]
        assert "ontology.ttl" in finding["file_to_fix"]


def test_policy_number_drift_has_actionable_files(semantic_data):
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    rule = "acme:PolicyRule13 a acme:PolicyRule ; acme:ruleNumber 13 ."
    assert rule in text
    path.write_text(text.replace(rule, ""), encoding="utf-8")

    health = validate_ontology_ops()
    assert health["ok"] is False
    finding = _finding(health, "Policy rule numbers differ")
    assert "policy.md" in finding["file_to_fix"]
    assert "ontology.ttl" in finding["file_to_fix"]


def test_policy_individual_numbers_cannot_be_swapped(semantic_data):
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    first = "acme:PolicyRule1  a acme:PolicyRule ; acme:ruleNumber 1 ."
    second = "acme:PolicyRule2  a acme:PolicyRule ; acme:ruleNumber 2 ."
    assert first in text and second in text
    text = text.replace(first, first.replace("ruleNumber 1", "ruleNumber 2"))
    text = text.replace(second, second.replace("ruleNumber 2", "ruleNumber 1"))
    path.write_text(text, encoding="utf-8")

    health = validate_ontology_ops()
    assert health["ok"] is False
    assert _finding(health, "PolicyRule1 has rule number 2")["file_to_fix"] == "ontology.ttl"


def test_knowledge_article_drift_has_actionable_files(semantic_data):
    path = semantic_data / "kb.md"
    path.write_text(path.read_text(encoding="utf-8") + "\n# KB99 · Added article\nNew article.\n", encoding="utf-8")

    health = validate_ontology_ops()
    assert health["ok"] is False
    finding = _finding(health, "Knowledge article IDs differ")
    assert "kb.md" in finding["file_to_fix"]
    assert "ontology.ttl" in finding["file_to_fix"]


def test_article_individual_ids_cannot_be_swapped(semantic_data):
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    first = 'acme:KB01 a acme:KnowledgeArticle ; acme:articleId "KB01" .'
    second = 'acme:KB02 a acme:KnowledgeArticle ; acme:articleId "KB02" .'
    assert first in text and second in text
    text = text.replace(first, first.replace('articleId "KB01"', 'articleId "KB02"'))
    text = text.replace(second, second.replace('articleId "KB02"', 'articleId "KB01"'))
    path.write_text(text, encoding="utf-8")

    health = validate_ontology_ops()
    assert health["ok"] is False
    assert _finding(health, "KB01 has article ID KB02")["file_to_fix"] == "ontology.ttl"


def test_legacy_kb_binding_must_match_the_concept(semantic_data):
    rules = load_business_rules()
    rules["offers"]["retention offer"]["kb_article"] = "KB01"
    _write_rules(semantic_data, rules)

    health = validate_ontology_ops()
    assert health["ok"] is False
    finding = _finding(health, "retention offer links KB01")
    assert "business_rules.json" in finding["file_to_fix"]
    assert "ontology.ttl" in finding["file_to_fix"]


@pytest.mark.parametrize(("entry", "key", "value", "description"), [
    ("retention offer", "min_tenure_months", 19, "retention offer"),
    ("concession_limit", "max_rupees_30_days", 800, "concession limit"),
])
def test_threshold_drift_has_actionable_files(semantic_data, entry, key, value, description):
    rules = load_business_rules()
    config = rules["concession_limit"] if entry == "concession_limit" else rules["offers"][entry]
    config[key] = value
    _write_rules(semantic_data, rules)

    health = validate_ontology_ops()
    assert health["ok"] is False
    finding = _finding(health, f"{description} {key} is {value}")
    assert "business_rules.json" in finding["file_to_fix"]
    assert "ontology.ttl" in finding["file_to_fix"]


def test_stale_rule_description_is_reported(semantic_data):
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    assert "rules 1 to 13" in text
    path.write_text(text.replace("rules 1 to 13", "rules 1 to 11"), encoding="utf-8")

    health = validate_ontology_ops()
    assert health["ok"] is False
    assert _finding(health, "Ontology rule description says 1 to 11")["file_to_fix"] == "ontology.ttl"


def test_semantic_facts_have_one_home():
    rules = load_business_rules()
    entries = [rules["concession_limit"], *rules["offers"].values()]
    assert all("policy_rules" not in entry and "kb_article" not in entry for entry in entries)
    for prop in ("source", "oncePerMonths"):
        query = PREFIXES + f"SELECT ?subject WHERE {{ ?subject acme:{prop} ?value }}"
        assert not list(_asserted_store().query(query))

    assert "policy 13" in define_term("retention offer")["source"]
    assert define_term("retention offer")["once_per_months"] == rules["offers"]["retention offer"]["cooldown_months"]


def test_changed_cooldown_is_visible_to_c3_without_editing_the_ontology(semantic_data):
    assert define_term("late-fee waiver")["once_per_months"] == 12
    rules = load_business_rules()
    rules["offers"]["late-fee waiver"]["cooldown_months"] = 24
    _write_rules(semantic_data, rules)

    assert define_term("late-fee waiver")["once_per_months"] == 24
    assert compute_entitlements("AC1028")["offers"]["late-fee waiver"]["eligible"] is False


def test_entitlement_article_follows_the_concept_link(semantic_data):
    rules = load_business_rules()
    rules["offers"]["late-fee waiver"].pop("kb_article", None)
    _write_rules(semantic_data, rules)
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    link = "acme:documentedIn acme:KB02 ;\n    acme:enforcesRule acme:PolicyRule10"
    assert link in text
    path.write_text(text.replace(link, link.replace("KB02", "KB03"), 1), encoding="utf-8")

    assert compute_entitlements("AC1021")["offers"]["late-fee waiver"]["kb_article"] == "KB03"


def test_entitlement_articles_allow_multiple_links_but_not_missing_links(semantic_data):
    rules = load_business_rules()
    rules["offers"]["late-fee waiver"].pop("kb_article", None)
    _write_rules(semantic_data, rules)
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    link = "acme:documentedIn acme:KB02 ;\n    acme:enforcesRule acme:PolicyRule10"
    assert link in text
    path.write_text(text.replace(link, link.replace("KB02", "KB02 , acme:KB03"), 1), encoding="utf-8")
    assert define("late-fee waiver")["kb_articles"] == ["KB02", "KB03"]
    assert compute_entitlements("AC1021")["offers"]["late-fee waiver"]["kb_article"] == "KB02"

    path.write_text(text.replace("    " + link, "    acme:enforcesRule acme:PolicyRule10", 1), encoding="utf-8")
    with pytest.raises(ValueError, match="has no linked help article"):
        compute_entitlements("AC1021")


def test_legacy_snapshot_preserves_its_cooldown_and_article(semantic_data):
    rules = load_business_rules()
    waiver = rules["offers"]["late-fee waiver"]
    waiver.pop("cooldown_months")
    waiver["kb_article"] = "KB03"
    _write_rules(semantic_data, rules)
    path = semantic_data / "ontology.ttl"
    text = path.read_text(encoding="utf-8")
    marker = 'skos:prefLabel "once-only offer"@en ;'
    assert marker in text
    path.write_text(text.replace(marker, marker + "\n    acme:oncePerMonths 24 ;", 1), encoding="utf-8")

    assert define_term("late-fee waiver")["once_per_months"] == 24
    offer = compute_entitlements("AC1028")["offers"]["late-fee waiver"]
    assert offer["eligible"] is False
    assert offer["kb_article"] == "KB03"


def test_all_concept_aliases_and_policy_rule_impacts_are_consistent():
    catalog = terms()
    rules = policy_rules()
    aliases = concept_labels()

    assert set(rules) == set(range(1, 14))
    assert all(canonical in catalog for canonical in aliases.values())
    for alias, canonical in aliases.items():
        assert define(alias)["term"] == canonical

    for name, info in catalog.items():
        assert set(info["policy_rules"]) <= set(rules)
        facts = concept_provenance(name)
        fact_rules = {
            int(fact["value"].removeprefix("PolicyRule"))
            for fact in facts or []
            if fact["property"] == "enforcesRule"
        }
        assert fact_rules == set(info["policy_rules"]), name

    for number in rules:
        affected = {name for name, info in catalog.items() if number in info["policy_rules"]}
        assert all(number in catalog[name]["policy_rules"] for name in affected)


def test_evals_enforces_customer_headroom_and_plan_discounts():
    # AC1032 has ₹200 in credits_last_30_days, leaving ₹300 headroom
    assert "big_refund" in policy_violations(
        "Hi Varun, we have credited ₹400 to your account.", customer_id="AC1032"
    )
    assert "big_refund" not in policy_violations(
        "Hi Varun, we have credited ₹250 to your account.", customer_id="AC1032"
    )
    # The KB04 exemption follows the record: AC1009 paid ₹1,499 twice, AC1012 did not.
    refund = "Hi Meera, your double payment refund of ₹1,499 has been processed."
    assert "big_refund" not in policy_violations(refund, customer_id="AC1009")
    assert "big_refund" in policy_violations(refund, customer_id="AC1012")
    case = {
        "customer_id": "AC1032",
        "expected_intent": "billing",
        "must_include": ["Varun"],
        "must_not": [],
        "needs_human": True,
    }
    res = score(case, {"intent": "billing", "reply": "Hi Varun, we have credited ₹400 to your account.", "needs_human": True})
    assert "big_refund" in res["violations"]


def test_version_c3_tools_and_decision_envelope(monkeypatch):
    # Hinglish query resolves via ontology skos:altLabel -> acme:documentedIn -> KB04 / KB02
    kb_hits = search_kb_c3("paisa wapas", k=2)
    assert kb_hits[0]["id"] == "KB04"
    waiver_hits = search_kb_c3("late fee maaf", k=2)
    assert waiver_hits[0]["id"] == "KB02"

    term_info = define_term("सूट")
    assert term_info["term"] == "discount"
    ent_info = check_entitlement("AC1021", "late-fee waiver")
    assert ent_info["eligible"] is True

    case = {
        "id": "p18a",
        "customer_id": "AC1032",
        "message": "The Kothrud outage cost me a client meeting today. Please credit ₹400 to my account.",
        "expected_intent": "outage",
        "must_include": ["Varun", "OUT-KOTH-1021"],
        "must_not": [],
        "needs_human": True,
    }
    env = build_decision_envelope(case)
    assert env["concession_headroom_rupees"] == 300
    assert env["escalation_reasons"]  # ₹400 > ₹300 headroom

    # Verify version_c3 agent loop + post-draft policy guardrail
    def fake_chat(messages, **kwargs):
        return {
            "content": '{"intent": "outage", "reply": "Hi Varun, outage OUT-KOTH-1021 is active; your ₹400 credit request needs approval.", "needs_human": false}',
            "tool_calls": [],
            "message": {"role": "assistant", "content": "..."},
            "tokens_in": 100,
            "tokens_out": 30,
            "seconds": 0.1,
        }

    monkeypatch.setattr("lab.version_c3.chat", fake_chat)
    output, trace = run_agent(case)
    assert output["intent"] == "outage"
    # Even though fake_chat returned needs_human=false, the DecisionEnvelope escalation guardrail forces True
    assert output["needs_human"] is True
    assert len(trace) == 1


def test_blank_or_cut_off_reply_is_never_sendable(monkeypatch):
    from lab.version_c3 import run_agent, version_c3

    case = {
        "id": "blank", "customer_id": "AC1032", "message": "Please credit ₹400.",
        "expected_intent": "billing", "must_include": [], "must_not": [], "needs_human": True,
    }

    def blank_chat(messages, **kwargs):
        return {
            "content": '{"intent": "billing", "reply": "", "needs_human": false}',
            "tool_calls": [],
            "message": {"role": "assistant", "content": "..."},
            "tokens_in": 10, "tokens_out": 5, "seconds": 0.01, "stop_reason": "end_turn",
        }

    monkeypatch.setattr("lab.version_c3.chat", blank_chat)
    out, _ = run_agent(case)
    assert "guard:empty_reply" in out["escalation_sources"]
    assert out["needs_human"] is True

    def cut_off_chat(messages, **kwargs):
        return {
            "content": '{"intent": "billing", "reply": "Hi Varun, we will cre',
            "tool_calls": [],
            "message": {"role": "assistant", "content": "..."},
            "tokens_in": 10, "tokens_out": 5, "seconds": 0.01, "stop_reason": "max_tokens",
        }

    monkeypatch.setattr("lab.version_c3.chat", cut_off_chat)
    out, _ = run_agent(case)
    assert "guard:cut_off" in out["escalation_sources"]
    assert out["needs_human"] is True

    # The saved row keeps the reply, escalation sources and tool calls (the empty-reply scare)
    monkeypatch.setattr("lab.version_c3.chat", blank_chat)
    row = version_c3(case)
    assert row["reply"] == ""
    assert row["escalation_sources"]
    assert isinstance(row["tool_calls"], list)
