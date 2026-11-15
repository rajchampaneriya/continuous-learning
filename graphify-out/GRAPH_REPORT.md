# Graph Report - continuous-learning  (2026-11-15)

## Corpus Check
- 207 files · ~148,710 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 100 file(s) not represented in the graph (top: .jsonl 33, .feature 20, .drawio 18)
- WARNING: 100 of 313 files seen (32%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2410 nodes · 5337 edges · 153 communities (129 shown, 24 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 403 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `80cb4f19`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- acme_metrics.py
- test_report_metrics.py
- versioned-simulator.md
- test_guardrails.py
- server
- test_out_of_steps.py
- service.py
- VersionRegistry
- ontology.py
- RunInput
- test_ontology.py
- Span
- pytest
- evaluation-report.qmd
- version_c3.py
- json
- Acme Review Studio
- validate_ontology_ops
- version_c4.py
- test_redteam_adapter.py
- chip
- test_c3_provider.py
- DataFrame
- pytest
- lab.py
- DirectAdapter
- evals.py
- run.py
- test_simulator_http.py
- test_gate_slots.py
- test_escalation_metrics.py
- test_escalation_rules.py
- when
- redteam/checks.py
- RunStore
- adapter.py
- test_grader_mutations.py
- ZAVAAirlines Fabric Data Agents - Q&A
- import_cases.py
- http.py
- kb.md
- pick_b_cases
- Implementation plan
- re
- .adapter
- studio-c3.yaml
- ADR-001: Support Email Automation Strategy
- json
- personas
- load_business_rules
- compute_entitlements
- test_router_rules.py
- config
- studio-declarative.yaml
- ThreadStore
- extract_concepts
- c3-agent.yaml
- Later: an ontology layer for Acme Fibre
- data_root
- Day 12 · Article: measure before you believe
- Word Search
- gates
- studio-offline.yaml
- version-b.yaml
- Day 3 · Write the test set before the system
- Day 8 · Version C: an agent loop from scratch
- Day 9 · Run all three: success, cost, latency
- Day 11 · The recommendation, first draft (an ADR)
- Think, Build & Repeat
- Combination Sum
- Combination Sum II
- Letter Combinations of a Phone Number
- N-Queens
- Palindrome Partitioning
- Permutations
- Subsets
- Subsets II
- Day 1 · An LLM call is just an HTTP request
- Day 2 · Workflow or agent? Map the decisions first
- offline-direct.yaml
- Day 5 · A grader you can trust
- Day 6 · Version B: one model call with the right context
- Day 7 · Why 30 test cases can lie: error bars
- Spoken script
- 🎙️ Spoken Script & Presentation Guide
- Adapter
- Day 4 · Version A: rules and templates (the honest baseline)
- ADR-001: How Acme Fibre should answer customer emails
- cwhite-D5-glm53flash/report.md
- ._build
- ScriptedResponse
- define
- AGENTS.md
- fde-first-principles/README.md
- test_expert_review.py
- Holdout set
- article.md
- Conversation Summary
- Continuous Learning
- subsets.py
- app.py
- Later: grader ideas parked on day 5
- Agent 365
- Backtracking
- json
- Boosted Trees at the Chai Stall
- main
- CLAUDE.md
- .claude/CLAUDE.md
- C3Provider
- fde-first-principles
- review_record
- run_agent
- AcmeAgentTarget
- Workflow
- Red teaming D5 with PyRIT · plan
- C3Provider
- O1
- O2
- O3
- O4
- O5
- O6
- O7
- O8
- resume
- The problem
- d1-split-three.yaml
- OrchestratedAdapter
- d2-split-five.yaml
- d3-fresh-thread.yaml
- d4-repeat-waiver.yaml
- d5-repeat-retention.yaml
- test_adapter_contract.py
- Acme Fibre: the project brief (fictional)
- objectives
- d6-third-party-joins.yaml
- d7-third-party-first.yaml
- d8-action-claimed.yaml
- Response
- cblack-D5-glm53flash/report.md
- replay-D5-glm53flash/report.md
- smoke-D-glm53flash/report.md
- FINDINGS.md
- redteam/NOTES-for-SME.md

## God Nodes (most connected - your core abstractions)
1. `server()` - 128 edges
2. `Version` - 61 edges
3. `RunInput` - 52 edges
4. `RunResult` - 49 edges
5. `when` - 46 edges
6. `policy_violations()` - 42 edges
7. `VersionRegistry` - 40 edges
8. `build_decision_envelope()` - 40 edges
9. `SimulationService` - 35 edges
10. `data_root()` - 34 edges

## Surprising Connections (you probably didn't know these)
- `R0 · Spike and pin` --references--> `AcmeAgentTarget`  [INFERRED]
  kata-use-cases/Red teaming D5 with PyRIT · plan.md → fde-first-principles/redteam/spike.py
- `Rounds become versions` --references--> `ReviewStore`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/store.py
- `Testing approach` --references--> `RunResult`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `Scoring and metrics` --references--> `unsupported_number()`  [INFERRED]
  kata-use-cases/Red teaming D5 with PyRIT · plan.md → fde-first-principles/redteam/checks.py
- `How the BDD tests work` --references--> `policy_violations()`  [INFERRED]
  AGENTS.md → fde-first-principles/lab/evals.py

## Import Cycles
- None detected.

## Communities (153 total, 24 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.19
Nodes (12): _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key(), _load() (+4 more)

### Community 1 - "acme_metrics.py"
Cohesion: 0.14
Nodes (5): build_frame(), fig_html(), layer_of(), tiles(), workbook_sheet()

### Community 2 - "test_report_metrics.py"
Cohesion: 0.06
Nodes (43): ReviewStore, _export(), score_rounds(), load(), Acme Review Studio review, Architecture, Delivered, P1 — Parsed model output lacks local schema validation (+35 more)

### Community 3 - "versioned-simulator.md"
Cohesion: 0.05
Nodes (35): ClaudeCodeProvider, Accessibility, Compare mode, Decisions to record, Demo in three minutes, Done when, Drift and pinning, Goals and non-goals (+27 more)

### Community 4 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 5 - "server"
Cohesion: 0.06
Nodes (40): server(), _apply_retention(), batch_rev(), batch_status(), case_editor(), case_list(), case_of(), _ed_save() (+32 more)

### Community 6 - "test_out_of_steps.py"
Cohesion: 0.07
Nodes (27): version_c3(), test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes(), customer_writes(), marked_out_of_steps(), model_called(), not_marked_out_of_steps(), one_more_turn() (+19 more)

### Community 7 - "service.py"
Cohesion: 0.10
Nodes (4): redact(), RedactingSerializer, secret_values(), State

### Community 8 - "VersionRegistry"
Cohesion: 0.17
Nodes (7): canonical(), case_hash(), digest(), lab_snapshot(), label_hash(), _sheet_hashes(), VersionRegistry

### Community 9 - "ontology.py"
Cohesion: 0.18
Nodes (16): _asserted_store(), _bool_value(), customer_subgraph(), _data_cache(), cached(), get(), domain_edges(), _edge_metadata() (+8 more)

### Community 10 - "RunInput"
Cohesion: 0.11
Nodes (18): SimulationService, RunInput, run_case(), run(), test_adapter_errors_and_timeouts_are_saved(), test_c3_concurrent_versions_read_their_own_lab_snapshots(), test_release_requires_current_graded_cases_and_retired_resume_stays_held(), test_retention_removes_expired_runs_and_checkpoints_but_keeps_held_runs() (+10 more)

### Community 11 - "test_ontology.py"
Cohesion: 0.18
Nodes (15): answer_is(), check_headroom(), check_inherited_props(), check_inherited_role(), check_offer_eligibility(), check_ops_clean(), check_overridden_entitlement(), check_override_false() (+7 more)

### Community 12 - "Span"
Cohesion: 0.16
Nodes (25): _button(), render_comparison(), render_detail(), render_result(), _text(), _topology(), _tree(), branch() (+17 more)

### Community 13 - "pytest"
Cohesion: 0.06
Nodes (26): initial_mode(), pipeline(), _prefill(), check_fired(), ctx(), fail_no_critique(), fail_no_mode(), hint() (+18 more)

### Community 14 - "evaluation-report.qmd"
Cohesion: 0.08
Nodes (22): At a glance, Composition, Escalation rules, Label review, Provenance, What this set can't tell you, Where the cases come from, Examples from the expert's review (+14 more)

### Community 15 - "version_c3.py"
Cohesion: 0.07
Nodes (27): conversation(), customer_card(), first_name(), intent_guide(), kb_by_id(), load_customers(), load_results(), escalate() (+19 more)

### Community 16 - "json"
Cohesion: 0.10
Nodes (19): main(), promote(), check_quality(), load_lines(), main(), triage_rows(), action_claim_fires(), agent_replies() (+11 more)

### Community 17 - "Acme Review Studio"
Cohesion: 0.09
Nodes (21): Acme Review Studio, How the Claude Code call works, Project layout, Reference Review layout, Reports (Quarto), Reviewing the C3 agent's drafts, Run it, Set up (once) (+13 more)

### Community 18 - "validate_ontology_ops"
Cohesion: 0.10
Nodes (18): reason_owl_rl(), validate_ontology_ops(), run_ops_validation(), Build on what already exists, Checks, Code changes, Concept card, Demo in three minutes (+10 more)

### Community 19 - "version_c4.py"
Cohesion: 0.09
Nodes (24): customer_text(), run_agent(), extract_json(), _envelope_brief(), _grants(), offers_not_allowed(), run_agent(), _answer() (+16 more)

### Community 20 - "test_redteam_adapter.py"
Cohesion: 0.16
Nodes (18): fake_adapter(), fake_agent(), finished_run(), _fresh_world(), handle_two_earlier(), ledger_matches_run_d(), _line(), logged_adapter() (+10 more)

### Community 21 - "chip"
Cohesion: 0.15
Nodes (16): chip(), customer_chips(), cur(), draft_meta(), email_card(), expected_card(), guard_try_result(), _prefill_key() (+8 more)

### Community 22 - "test_c3_provider.py"
Cohesion: 0.11
Nodes (19): make_provider(), c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason() (+11 more)

### Community 23 - "DataFrame"
Cohesion: 0.06
Nodes (31): banner(), Evidence, html_table(), mask(), nonempty(), provenance_table(), Rate, sha256() (+23 more)

### Community 24 - "pytest"
Cohesion: 0.22
Nodes (4): case_is_labelled(), every_intent_defined(), labelled_cases(), world()

### Community 25 - "lab.py"
Cohesion: 0.12
Nodes (13): _bool(), export_to_excel(), _history(), _item(), load_lab(), _payments(), _put(), read_review_log() (+5 more)

### Community 27 - "evals.py"
Cohesion: 0.07
Nodes (28): amounts(), _approved(), _limit_context(), _negated(), not_english(), other_customer_details(), _plan_in_sentence(), policy_violations() (+20 more)

### Community 28 - "run.py"
Cohesion: 0.15
Nodes (16): use(), AcmeAdapter, main(), load_scripts(), load_seeds(), main(), _no_ledger(), persona_customer() (+8 more)

### Community 30 - "test_simulator_http.py"
Cohesion: 0.18
Nodes (9): Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout(), test_redirect_cannot_send_auth_to_a_different_allowlisted_origin(), test_secret_bearing_endpoints_are_rejected_before_freezing(), version() (+1 more)

### Community 31 - "test_gate_slots.py"
Cohesion: 0.13
Nodes (11): canonical_offer(), fill_offers(), _slot_norm(), customer_writes(), gate_escalates(), grant_sentences(), model_returns_slots(), reply_contains() (+3 more)

### Community 32 - "test_escalation_metrics.py"
Cohesion: 0.18
Nodes (12): summary(), bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is() (+4 more)

### Community 33 - "test_escalation_rules.py"
Cohesion: 0.13
Nodes (17): agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes(), customer_writes(), envelope_decides(), escalation_sources_are(), every_labelled_case() (+9 more)

### Community 34 - "when"
Cohesion: 0.10
Nodes (20): run_case(), run_email(), read(), read_round(), when, apply_commercial_rule_override(), inspect_reasoned_ontology(), customer_wrote() (+12 more)

### Community 35 - "redteam/checks.py"
Cohesion: 0.09
Nodes (19): load_kb(), action_claim(), allowed_numbers(), _as_float(), _ngrams(), _numbers(), prompt_leak(), _record_numbers() (+11 more)

### Community 36 - "RunStore"
Cohesion: 0.22
Nodes (3): _json(), _now(), RunStore

### Community 37 - "adapter.py"
Cohesion: 0.13
Nodes (4): find_system_prompt(), RefusedSystemPrompt, TurnLog, verdict()

### Community 38 - "test_grader_mutations.py"
Cohesion: 0.15
Nodes (16): _add_each_banned(), _append(), _cases_where(), _drop_each_fact(), grader_fails(), grader_flags(), grader_passes(), mutate() (+8 more)

### Community 39 - "ZAVAAirlines Fabric Data Agents - Q&A"
Cohesion: 0.11
Nodes (17): 10. Unstructured Data Support, 11. Consistent Responses Across Teams, Excel, and Copilot Studio, 12. Fabric Data Agent as Knowledge Source, 13. Direct OneLake Access vs Data Agents, 14. Architecture Responsibilities, 15. External AI Access Pattern, 16. Fabric Data Agents vs Power BI Copilot, 1. Improve Query Generation Accuracy (+9 more)

### Community 40 - "import_cases.py"
Cohesion: 0.24
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 41 - "http.py"
Cohesion: 0.12
Nodes (6): VersionBAdapter, _endpoint(), HttpAdapter, DeclarativeAdapter, endpoint_origin(), test_loopback_http_is_allowed_only_when_explicitly_allowlisted()

### Community 42 - "kb.md"
Cohesion: 0.12
Nodes (16): KB01 · Billing cycle and due dates, KB02 · Late payment fee, KB03 · Payment methods, KB04 · Refunds and credits, KB05 · Outages and restoration updates, KB06 · Outage credit, KB07 · Slow speed or no internet: first checks, KB08 · Technician visits (+8 more)

### Community 43 - "pick_b_cases"
Cohesion: 0.18
Nodes (6): must_survive(), pick_b_cases(), rewrite_case(), rewrite_ok(), test_b_pick_is_deterministic_balanced_and_labelled(), test_must_survive_and_rewrite_ok()

### Community 44 - "Implementation plan"
Cohesion: 0.14
Nodes (13): Implementation plan, Out of scope until project 6, Phase 0: Measure the problem (no new code), Phase 1: Write the ontology (definitions only), Phase 2: Loader and tests, Phase 3: Version B with the glossary, Phase 4: Version C with a lookup tool (optional), Phase 5: Decide with evidence (+5 more)

### Community 45 - "re"
Cohesion: 0.22
Nodes (9): amounts(), claim_checks(), _flag(), guard_hits(), Lab, direct_output(), no_draft(), validate_draft() (+1 more)

### Community 46 - ".adapter"
Cohesion: 0.18
Nodes (13): icon(), review_page(), case_header(), replay_sources(), selected_sim_version(), sim_fields(), sim_history_controls(), sim_pipe() (+5 more)

### Community 47 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 48 - "ADR-001: Support Email Automation Strategy"
Cohesion: 0.12
Nodes (15): 5-Minute Executive Readout for Acme Fibre, ADR-001: Support Email Automation Strategy, Core Operating Reality, Phased Operational Strategy:, Principal Engineer Insights:, Slide 1: Executive Summary & Recommendation, Slide 2: Three Competing Paradigms Evaluated, Slide 3: Empirical Scorecard (Statistical Error Bars) (+7 more)

### Community 49 - "json"
Cohesion: 0.20
Nodes (9): fingerprint(), git_commit(), save_results(), api_usage(), all_cases(), main(), _p(), paired_metrics() (+1 more)

### Community 50 - "personas"
Cohesion: 0.10
Nodes (19): customer_id, stands_for, customer_id, stands_for, customer_id, stands_for, personas, clean_long_tenure (+11 more)

### Community 51 - "load_business_rules"
Cohesion: 0.23
Nodes (8): _deep_update(), _default_rules(), load_business_rules(), _rules_at(), system_prompt_d(), black_box(), pack(), white_box()

### Community 52 - "compute_entitlements"
Cohesion: 0.14
Nodes (8): load_outages(), outage_for(), duplicate_payment_amount(), months_since(), outage_exceeds_hours(), _parse_date(), compute_entitlements(), compute_for_customer()

### Community 54 - "test_router_rules.py"
Cohesion: 0.18
Nodes (8): draft_check_reports(), world(), customer_writes(), router_does_not_fire(), router_fast_path(), router_fires(), test_a_retention_repeat_on_a_cancellation_is_not_money(), world()

### Community 55 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 56 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 57 - "ThreadStore"
Cohesion: 0.12
Nodes (19): claim_amounts(), money_asked(), route(), thread_of(), ThreadStore, version_d(), watchdog(), case() (+11 more)

### Community 58 - "extract_concepts"
Cohesion: 0.29
Nodes (4): _alias_index(), _alias_pattern(), extract_concepts(), extract_concepts_from()

### Community 59 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 60 - "Later: an ontology layer for Acme Fibre"
Cohesion: 0.17
Nodes (10): Decision: where the ontology lives (2026-10-28), Do we need it now, How to prove it first (measure before you believe), Later: an ontology layer for Acme Fibre, Recommended tool: pyoxigraph, Sketch, When it becomes worth building, Acme Fibre reply policy (+2 more)

### Community 61 - "data_root"
Cohesion: 0.23
Nodes (8): data_root(), load_cases(), kb_only(), main(), recall_for(), all_cases(), main(), test_grounding_recall_at_least_90_percent_per_suite()

### Community 62 - "Day 12 · Article: measure before you believe"
Cohesion: 0.17
Nodes (11): 1 · Learn (about 40 minutes), 2 · Write and publish (about 185 minutes), 3 · Record (optional for an article), Before you start, Day 12 · Article: measure before you believe, Done when, How I used AI, Set up (+3 more)

### Community 63 - "Word Search"
Cohesion: 0.18
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, Pattern Takeaway, Problem, Related, Solutions, Visual (+2 more)

### Community 64 - "gates"
Cohesion: 0.18
Nodes (10): costs_inr, missed_escalation, unneeded_escalation, unsafe_auto_send, gates, missed_escalations, pass_rate_ci_low, routing_accuracy (+2 more)

### Community 65 - "studio-offline.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 66 - "version-b.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 67 - "Day 3 · Write the test set before the system"
Cohesion: 0.18
Nodes (11): 1 · Learn (about 30 minutes), 2 · Build (about 90 minutes), 3 · Record (5 minutes or less), Day 3 · Write the test set before the system, Done when, Ground truth · 20 SME-reviewed scenarios, How I used AI, In my words (+3 more)

### Community 68 - "Day 8 · Version C: an agent loop from scratch"
Cohesion: 0.20
Nodes (10): 1 · Learn (about 30 minutes), 2 · Build (about 60 minutes), 3 · Record (5 minutes or less), Day 8 · Version C: an agent loop from scratch, Done when, How I used AI, In my words, Set up (+2 more)

### Community 69 - "Day 9 · Run all three: success, cost, latency"
Cohesion: 0.20
Nodes (10): 1 · Learn (about 25 minutes), 2 · Build (about 70 minutes), 3 · Record (5 minutes or less), Day 9 · Run all three: success, cost, latency, Done when, How I used AI, In my words, Set up (+2 more)

### Community 70 - "Day 11 · The recommendation, first draft (an ADR)"
Cohesion: 0.18
Nodes (10): 1 · Learn (about 15 minutes), 2 · Build (about 45 minutes), 3 · Record (5 minutes or less), Before you start: what your evidence already says, Day 11 · The recommendation, first draft (an ADR), Done when, How I used AI, In my words (+2 more)

### Community 71 - "Think, Build & Repeat"
Cohesion: 0.18
Nodes (10): Continuous operational-state evaluation with policy-driven action orchestration, Cross-domain enterprise contextual federation, Eval enhancements, generative orchastration - copilot studio, oAuth Identity Passthrough, Problem 1, Problem 2, Problem 3 (+2 more)

### Community 72 - "Combination Sum"
Cohesion: 0.20
Nodes (10): Combination Sum, Complexity, E-Prime Pseudocode, Greg Tang Explains, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 73 - "Combination Sum II"
Cohesion: 0.20
Nodes (10): Combination Sum II, Complexity, E-Prime Pseudocode, Greg Tang Explains, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 74 - "Letter Combinations of a Phone Number"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, Letter Combinations of a Phone Number, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 75 - "N-Queens"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, N-Queens, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 76 - "Palindrome Partitioning"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, Palindrome Partitioning, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 77 - "Permutations"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, Pattern Takeaway, Permutations, Problem, Related, Solutions (+2 more)

### Community 78 - "Subsets"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains Visually, Subsets, Pattern Takeaway, Problem, Related, Solutions (+2 more)

### Community 79 - "Subsets II"
Cohesion: 0.20
Nodes (10): Complexity, E-Prime Pseudocode, Greg Tang Explains, Pattern Takeaway, Problem, Related, Solutions, Subsets II (+2 more)

### Community 80 - "Day 1 · An LLM call is just an HTTP request"
Cohesion: 0.20
Nodes (10): 1 · Learn (about 20 minutes), 2 · Build (about 40 minutes), 3 · Record (5 minutes or less), Day 1 · An LLM call is just an HTTP request, Done when, How I used AI, In my words, Set up (+2 more)

### Community 81 - "Day 2 · Workflow or agent? Map the decisions first"
Cohesion: 0.20
Nodes (9): 1 · Learn (about 20 minutes), 2 · Build (about 40 minutes), 3 · Record (5 minutes or less), Day 2 · Workflow or agent? Map the decisions first, Done when, How I used AI, In my words, Video (+1 more)

### Community 82 - "offline-direct.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 83 - "Day 5 · A grader you can trust"
Cohesion: 0.20
Nodes (9): 1 · Learn (about 25 minutes), 2 · Build (about 50 minutes), 3 · Record (5 minutes or less), Day 5 · A grader you can trust, Done when, How I used AI, In my words, Video (+1 more)

### Community 84 - "Day 6 · Version B: one model call with the right context"
Cohesion: 0.20
Nodes (10): 1 · Learn (about 25 minutes), 2 · Build (about 60 minutes), 3 · Record (5 minutes or less), Day 6 · Version B: one model call with the right context, Done when, How I used AI, In my words, Set up (+2 more)

### Community 85 - "Day 7 · Why 30 test cases can lie: error bars"
Cohesion: 0.20
Nodes (9): 1 · Learn (about 30 minutes), 2 · Build (about 85 minutes), 3 · Record (5 minutes or less), Day 7 · Why 30 test cases can lie: error bars, Done when, How I used AI, In my words, Video (+1 more)

### Community 86 - "Spoken script"
Cohesion: 0.20
Nodes (9): Part 1: The question and the loop (0:00 to 0:30), Part 2: Observe (0:30 to 1:30), Part 3: Orient (1:30 to 2:30), Part 4: Decide and act (2:30 to 3:45), Part 5: What it does not prove and the next loop (3:45 to 4:45), Pitch timeline, Q&A cheat sheet, Readout details (+1 more)

### Community 87 - "🎙️ Spoken Script & Presentation Guide"
Cohesion: 0.20
Nodes (9): 5-Minute CTO Readout: Acme Fibre Support Automation, 🎯 Executive Q&A Defense Cheat-Sheet, Part 1: The Decision & Bottom Line (0:00 – 0:45), Part 2: The Empirical Evidence (0:45 – 1:45), Part 3: Architecture Walkthrough (1:45 – 3:15), Part 4: Go-Live Gates & Risk Controls (3:15 – 4:00), Part 5: What Would Change My Mind & Next Steps (4:00 – 4:45), ⏱️ Pitch Timeline & Structure (+1 more)

### Community 89 - "Adapter"
Cohesion: 0.20
Nodes (5): Adapter, Adding an implementation model, Extensibility, Extension points, Trace interoperability

### Community 90 - "Day 4 · Version A: rules and templates (the honest baseline)"
Cohesion: 0.20
Nodes (9): 1 · Learn (about 30 minutes), 2 · Build (about 60 minutes), 3 · Record (5 minutes or less), Day 4 · Version A: rules and templates (the honest baseline), Done when, How I used AI, In my words, Video (+1 more)

### Community 91 - "ADR-001: How Acme Fibre should answer customer emails"
Cohesion: 0.22
Nodes (8): ADR-001: How Acme Fibre should answer customer emails, Consequences, Context, Decision, Evidence (from day 9), Open questions (projects 2 to 6), Options, What would change my mind

### Community 94 - "._build"
Cohesion: 0.27
Nodes (11): _trace(), check(), decide(), draft(), fetch(), human(), log(), receive() (+3 more)

### Community 96 - "define"
Cohesion: 0.15
Nodes (12): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), concept_labels(), concept_provenance(), define(), policy_rules(), look_up() (+4 more)

### Community 97 - "AGENTS.md"
Cohesion: 0.29
Nodes (6): Codebase knowledge graph, Debugging in VS Code, Environment setup, How the BDD tests work, Repository layout, Running the tests

### Community 99 - "test_expert_review.py"
Cohesion: 0.20
Nodes (8): a_draft_handed_off(), a_draft_sent(), checks_that_fail(), given_test_case(), grader_flags(), grader_scores(), _names(), world()

### Community 100 - "Holdout set"
Cohesion: 0.50
Nodes (3): File, Holdout set, Rules

### Community 101 - "article.md"
Cohesion: 0.29
Nodes (6): Explore the project, My recommendation, and what would change my mind, Three ways to build it, What I measured, What the customer asked for, What the failures taught me

### Community 102 - "Conversation Summary"
Cohesion: 0.29
Nodes (6): Conversation Summary, Correct Answers, Correct Mapping, Explanation, Question 1, Question 2

### Community 103 - "Continuous Learning"
Cohesion: 0.29
Nodes (6): Approach, Areas of Exploration, Continuous Learning, Engineering Principles, Repository Philosophy, Watch & Read

### Community 106 - "app.py"
Cohesion: 0.12
Nodes (10): eval_checks(), suggest_mode(), validate_verdict(), highlight(), case_choices(), score_page(), _refresh_case_choices(), simulator_page() (+2 more)

### Community 107 - "Later: grader ideas parked on day 5"
Cohesion: 0.40
Nodes (4): Grader false positives still open, Graders to add, Later: grader ideas parked on day 5, Test cases to add

### Community 108 - "Agent 365"
Cohesion: 0.40
Nodes (4): Agent 365, Governance, Identity, observability

### Community 109 - "Backtracking"
Cohesion: 0.50
Nodes (4): Backtracking, Covered, Source, Understand recursion visually

### Community 110 - "json"
Cohesion: 0.11
Nodes (13): _parse_json_text(), judge_prompt(), main(), work(), run_judge(), load_meta(), compare_markdown(), main() (+5 more)

### Community 112 - "main"
Cohesion: 0.09
Nodes (7): HandoffScorer, main(), _RowScorer, UnattendedViolationScorer, HandoffScorer, _lines(), _LogScorer

### Community 116 - "C3Provider"
Cohesion: 0.26
Nodes (6): use_data_root(), _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 119 - "review_record"
Cohesion: 0.23
Nodes (10): compare_results(), review_record(), sample_spread(), run_case(), _run_missing(), worker(), one(), _run_one() (+2 more)

### Community 120 - "run_agent"
Cohesion: 0.10
Nodes (13): amounts_asked_for(), escalation_triggers(), percent_asks_in_rupees(), _trigger(), build_decision_envelope(), check_draft(), asked_for_money(), model_drafts() (+5 more)

### Community 122 - "AcmeAgentTarget"
Cohesion: 0.09
Nodes (8): AcmeAgentTarget, Go or no-go, LabLLMTarget, pyrit 1.1.0 API notes (docs are stale), R0 spike — PyRIT 1.1.0 around Version D, The six questions, AcmeAgentTarget, LabLLMTarget

### Community 124 - "Workflow"
Cohesion: 0.16
Nodes (6): OfflineProvider, _result(), Deps, to_record(), Workflow, main()

### Community 126 - "Red teaming D5 with PyRIT · plan"
Cohesion: 0.11
Nodes (17): At a glance, Attack campaign, Build phases, From finding to fix, R0 · Spike and pin, R1 · Threat model as data, R2 · Adapter, scorers and run log, R3 · Static campaigns (+9 more)

### Community 127 - "C3Provider"
Cohesion: 0.21
Nodes (3): c3_output(), C3Provider, AgentLoopAdapter

### Community 131 - "O1"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O1

### Community 132 - "O2"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O2

### Community 133 - "O3"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O3

### Community 134 - "O4"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O4

### Community 135 - "O5"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O5

### Community 136 - "O6"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O6

### Community 137 - "O7"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O7

### Community 138 - "O8"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O8

### Community 139 - "resume"
Cohesion: 0.25
Nodes (8): default_sim_step(), _ha(), _he(), _hh(), resume(), show_saved_run(), _sim_load(), _to_sim()

### Community 141 - "The problem"
Cohesion: 0.40
Nodes (5): user_prompt(), _settings(), sim_step_detail(), P1 — Mutable process globals can mix evaluation conditions, The problem

### Community 142 - "d1-split-three.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 143 - "OrchestratedAdapter"
Cohesion: 0.22
Nodes (3): OrchestratedAdapter, RecordedProvider, Version

### Community 144 - "d2-split-five.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 145 - "d3-fresh-thread.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 147 - "d4-repeat-waiver.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 148 - "d5-repeat-retention.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 149 - "test_adapter_contract.py"
Cohesion: 0.13
Nodes (6): AppSettings, Settings, pinned(), scripted_adapter(), valid_contract(), world()

### Community 152 - "d6-third-party-joins.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 153 - "d7-third-party-first.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 154 - "d8-action-claimed.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

## Knowledge Gaps
- **1 isolated node(s):** `fde-first-principles`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1053 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `claim_checks()` connect `re` to `test_report_metrics.py`, `DataFrame`, `._build`, `service.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `acme_metrics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `3. Quantitative measurement framework` connect `DataFrame` to `re`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Version` (e.g. with `AgentLoopAdapter` and `DirectAdapter`) actually correct?**
  _`Version` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_report_metrics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05548654244306418 - nodes in this community are weakly interconnected._