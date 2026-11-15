# Graph Report - continuous-learning  (2026-11-15)

## Corpus Check
- 158 files · ~127,420 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 85 file(s) not represented in the graph (top: .jsonl 27, .feature 18, .drawio 18)
- WARNING: 85 of 249 files seen (34%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2024 nodes · 4608 edges · 127 communities (107 shown, 20 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 360 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `50535690`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- test_simulator_persistence.py
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
- test_review_flow.py
- evaluation-report.qmd
- version_c3.py
- test_gate_slots.py
- Acme Review Studio
- Lab
- app.py
- ThreadStore
- chip
- test_c3_provider.py
- acme_metrics.py
- pytest
- providers.py
- direct.py
- evals.py
- terms
- test_adapter_contract.py
- test_simulator_http.py
- pytest
- test_escalation_metrics.py
- test_escalation_rules.py
- test_policy_rules.py
- load_business_rules
- RunStore
- Version
- test_grader_mutations.py
- ZAVAAirlines Fabric Data Agents - Q&A
- import_cases.py
- build_decision_envelope
- kb.md
- load_customers
- judge_round1.py
- refresh_versions
- Workflow
- studio-c3.yaml
- ADR-001: Support Email Automation Strategy
- json
- .adapter
- score
- review_record
- acme_metrics.py
- config
- studio-declarative.yaml
- version_d.py
- route
- c3-agent.yaml
- Later: an ontology layer for Acme Fibre
- test_router_rules.py
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
- acme.py
- run_agent
- Notes for the subject-matter expert
- save_verdict
- Acme Fibre: the project brief (fictional)
- AGENTS.md
- fde-first-principles/README.md
- test_expert_review.py
- Holdout set
- article.md
- Conversation Summary
- Continuous Learning
- subsets.py
- Later: grader ideas parked on day 5
- Agent 365
- Backtracking
- Boosted Trees at the Chai Stall
- CLAUDE.md
- .claude/CLAUDE.md
- use_data_root
- fde-first-principles
- run_agent
- resume
- ScriptedResponse
- ClaudeCodeProvider
- case_of
- The problem

## God Nodes (most connected - your core abstractions)
1. `server()` - 130 edges
2. `Version` - 61 edges
3. `RunInput` - 51 edges
4. `RunResult` - 49 edges
5. `VersionRegistry` - 40 edges
6. `build_decision_envelope()` - 40 edges
7. `policy_violations()` - 38 edges
8. `load_business_rules()` - 38 edges
9. `when` - 38 edges
10. `SimulationService` - 35 edges

## Surprising Connections (you probably didn't know these)
- `Checks` --references--> `validate_ontology_ops()`  [INFERRED]
  kata-use-cases/semantic-explorer.md → fde-first-principles/lab/ontology.py
- `Drift in the original model` --references--> `validate_ontology_ops()`  [INFERRED]
  kata-use-cases/semantic-explorer.md → fde-first-principles/lab/ontology.py
- `What the first draft proposed and why it's dropped` --references--> `validate_ontology_ops()`  [INFERRED]
  kata-use-cases/semantic-explorer.md → fde-first-principles/lab/ontology.py
- `Testing approach` --references--> `RunResult`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `Rounds become versions` --references--> `ReviewStore`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/store.py

## Import Cycles
- None detected.

## Communities (127 total, 20 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.19
Nodes (12): _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key(), _load() (+4 more)

### Community 1 - "test_simulator_persistence.py"
Cohesion: 0.12
Nodes (13): _bool(), export_to_excel(), _history(), _item(), load_lab(), _payments(), _put(), read_review_log() (+5 more)

### Community 2 - "test_report_metrics.py"
Cohesion: 0.06
Nodes (43): ReviewStore, _export(), score_rounds(), load(), Acme Review Studio review, Architecture, Delivered, P1 — Parsed model output lacks local schema validation (+35 more)

### Community 3 - "versioned-simulator.md"
Cohesion: 0.05
Nodes (38): Accessibility, Adding an implementation model, Compare mode, Decisions to record, Demo in three minutes, Done when, Drift and pinning, Extensibility (+30 more)

### Community 4 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 5 - "server"
Cohesion: 0.07
Nodes (16): server(), batch_rev(), batch_status(), _meaning_card_rule_selected(), meaning_checks(), _meaning_concept_changed(), _meaning_rule_changed(), _refresh_shared_versions() (+8 more)

### Community 6 - "test_out_of_steps.py"
Cohesion: 0.07
Nodes (27): version_c3(), test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes(), customer_writes(), marked_out_of_steps(), model_called(), not_marked_out_of_steps(), one_more_turn() (+19 more)

### Community 7 - "service.py"
Cohesion: 0.09
Nodes (6): redact(), RedactingSerializer, secret_values(), Settings, State, log()

### Community 8 - "VersionRegistry"
Cohesion: 0.14
Nodes (6): canonical(), case_hash(), digest(), lab_snapshot(), _sheet_hashes(), VersionRegistry

### Community 9 - "ontology.py"
Cohesion: 0.15
Nodes (17): _alias_index(), _bool_value(), customer_subgraph(), _data_cache(), cached(), get(), domain_edges(), _edge_metadata() (+9 more)

### Community 10 - "RunInput"
Cohesion: 0.11
Nodes (18): SimulationService, RunInput, run_case(), sim_version_banner(), run_case(), test_adapter_errors_and_timeouts_are_saved(), test_c3_concurrent_versions_read_their_own_lab_snapshots(), test_release_requires_current_graded_cases_and_retired_resume_stays_held() (+10 more)

### Community 11 - "test_ontology.py"
Cohesion: 0.12
Nodes (29): validate_ontology_ops(), answer_is(), check_business_rule_cooldown(), check_headroom(), check_inherited_props(), check_inherited_role(), check_offer_eligibility(), check_ops_clean() (+21 more)

### Community 12 - "Span"
Cohesion: 0.15
Nodes (25): _button(), render_comparison(), render_detail(), render_result(), _text(), _topology(), _tree(), branch() (+17 more)

### Community 13 - "test_review_flow.py"
Cohesion: 0.16
Nodes (13): check_fired(), ctx(), fail_no_critique(), fail_no_mode(), hint(), none_selected(), not_yet_grouped(), off() (+5 more)

### Community 14 - "evaluation-report.qmd"
Cohesion: 0.08
Nodes (22): At a glance, Composition, Escalation rules, Label review, Provenance, What this set can't tell you, Where the cases come from, Examples from the expert's review (+14 more)

### Community 15 - "version_c3.py"
Cohesion: 0.09
Nodes (26): conversation(), customer_text(), extract_json(), build_decision_envelope(), check_entitlement(), _envelope_brief(), _grants(), lookup_customer_c3() (+18 more)

### Community 16 - "test_gate_slots.py"
Cohesion: 0.15
Nodes (9): canonical_offer(), fill_offers(), customer_writes(), gate_escalates(), grant_sentences(), model_returns_slots(), reply_contains(), test_canonical_offer_maps_to_the_catalogue() (+1 more)

### Community 17 - "Acme Review Studio"
Cohesion: 0.09
Nodes (21): Acme Review Studio, How the Claude Code call works, Project layout, Reference Review layout, Reports (Quarto), Reviewing the C3 agent's drafts, Run it, Set up (once) (+13 more)

### Community 18 - "Lab"
Cohesion: 0.23
Nodes (9): amounts(), claim_checks(), _flag(), guard_hits(), Lab, direct_output(), no_draft(), validate_draft() (+1 more)

### Community 19 - "app.py"
Cohesion: 0.11
Nodes (10): eval_checks(), initial_mode(), suggest_mode(), highlight(), case_choices(), score_page(), _refresh_case_choices(), simulator_page() (+2 more)

### Community 20 - "ThreadStore"
Cohesion: 0.18
Nodes (5): thread_of(), ThreadStore, version_d(), test_ledger_catches_claim_built_over_turns(), test_threads_suite_ledger_matches_labels()

### Community 21 - "chip"
Cohesion: 0.14
Nodes (17): chip(), icon(), customer_chips(), review_page(), case_header(), cur(), draft_meta(), email_card() (+9 more)

### Community 22 - "test_c3_provider.py"
Cohesion: 0.12
Nodes (17): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+9 more)

### Community 23 - "acme_metrics.py"
Cohesion: 0.06
Nodes (32): banner(), Evidence, html_table(), mask(), nonempty(), provenance_table(), Rate, sha256() (+24 more)

### Community 24 - "pytest"
Cohesion: 0.17
Nodes (4): case_is_labelled(), every_intent_defined(), labelled_cases(), world()

### Community 25 - "providers.py"
Cohesion: 0.19
Nodes (3): OfflineProvider, _result(), to_record()

### Community 26 - "direct.py"
Cohesion: 0.09
Nodes (8): c3_output(), C3Provider, AgentLoopAdapter, DirectAdapter, VersionBAdapter, DeclarativeAdapter, endpoint_origin(), Span

### Community 27 - "evals.py"
Cohesion: 0.08
Nodes (20): load_customers(), outage_for(), amounts(), _approved(), _limit_context(), _negated(), not_english(), other_customer_details() (+12 more)

### Community 28 - "terms"
Cohesion: 0.07
Nodes (35): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), _asserted_store(), concept_labels(), concept_provenance(), define(), glossary() (+27 more)

### Community 29 - "test_adapter_contract.py"
Cohesion: 0.11
Nodes (7): AppSettings, pinned(), scripted_adapter(), valid_contract(), world(), world(), service()

### Community 30 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout() (+4 more)

### Community 31 - "pytest"
Cohesion: 0.21
Nodes (8): meaning_card(), fact_rows(), origin(), pipeline(), Elements, test_icons_have_no_network_or_accessible_name(), test_meaning_card_shows_provenance_sources_and_clickable_rules(), test_pipeline_keyboard_order_and_untrusted_details()

### Community 32 - "test_escalation_metrics.py"
Cohesion: 0.21
Nodes (11): bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is(), recall_is() (+3 more)

### Community 33 - "test_escalation_rules.py"
Cohesion: 0.16
Nodes (13): agent_replied(), customer_earlier_wrote(), customer_now_writes(), customer_writes(), escalation_sources_are(), every_labelled_case(), model_drafts(), needs_human_is() (+5 more)

### Community 34 - "test_policy_rules.py"
Cohesion: 0.10
Nodes (21): make_c3(), run_case(), run_email(), read(), read_round(), when, agent_finishes(), envelope_decides() (+13 more)

### Community 35 - "load_business_rules"
Cohesion: 0.12
Nodes (14): _deep_update(), _default_rules(), duplicate_payment_amount(), load_business_rules(), months_since(), outage_exceeds_hours(), _parse_date(), _rules_at() (+6 more)

### Community 36 - "RunStore"
Cohesion: 0.22
Nodes (3): _json(), _now(), RunStore

### Community 37 - "Version"
Cohesion: 0.15
Nodes (4): HttpAdapter, OrchestratedAdapter, RecordedProvider, Version

### Community 38 - "test_grader_mutations.py"
Cohesion: 0.17
Nodes (15): _add_each_banned(), _append(), _cases_where(), _drop_each_fact(), grader_fails(), grader_flags(), grader_passes(), mutate() (+7 more)

### Community 39 - "ZAVAAirlines Fabric Data Agents - Q&A"
Cohesion: 0.11
Nodes (17): 10. Unstructured Data Support, 11. Consistent Responses Across Teams, Excel, and Copilot Studio, 12. Fabric Data Agent as Knowledge Source, 13. Direct OneLake Access vs Data Agents, 14. Architecture Responsibilities, 15. External AI Access Pattern, 16. Fabric Data Agents vs Power BI Copilot, 1. Improve Query Generation Accuracy (+9 more)

### Community 40 - "import_cases.py"
Cohesion: 0.24
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 41 - "build_decision_envelope"
Cohesion: 0.33
Nodes (3): kb_only(), main(), recall_for()

### Community 42 - "kb.md"
Cohesion: 0.12
Nodes (16): KB01 · Billing cycle and due dates, KB02 · Late payment fee, KB03 · Payment methods, KB04 · Refunds and credits, KB05 · Outages and restoration updates, KB06 · Outage credit, KB07 · Slow speed or no internet: first checks, KB08 · Technician visits (+8 more)

### Community 43 - "load_customers"
Cohesion: 0.18
Nodes (8): load_outages(), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 44 - "judge_round1.py"
Cohesion: 0.27
Nodes (5): judge_prompt(), main(), work(), run_judge(), run_agent()

### Community 45 - "refresh_versions"
Cohesion: 0.20
Nodes (14): _apply_retention(), case_list(), _keep_current_visible(), _name_candidate(), _prefill_key(), progress(), refresh_versions(), _release_version() (+6 more)

### Community 46 - "Workflow"
Cohesion: 0.16
Nodes (13): Deps, _trace(), Workflow, check(), decide(), draft(), fetch(), human() (+5 more)

### Community 47 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 48 - "ADR-001: Support Email Automation Strategy"
Cohesion: 0.12
Nodes (15): 5-Minute Executive Readout for Acme Fibre, ADR-001: Support Email Automation Strategy, Core Operating Reality, Phased Operational Strategy:, Principal Engineer Insights:, Slide 1: Executive Summary & Recommendation, Slide 2: Three Competing Paradigms Evaluated, Slide 3: Empirical Scorecard (Statistical Error Bars) (+7 more)

### Community 49 - "json"
Cohesion: 0.14
Nodes (16): data_root(), fingerprint(), git_commit(), load_cases(), save_results(), summary(), api_usage(), use() (+8 more)

### Community 50 - ".adapter"
Cohesion: 0.23
Nodes (12): make_provider(), provider_status(), replay_sources(), selected_sim_version(), sim_fields(), sim_history_controls(), sim_pipe(), sim_replay_options() (+4 more)

### Community 51 - "score"
Cohesion: 0.19
Nodes (11): load_results(), score(), _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before() (+3 more)

### Community 52 - "review_record"
Cohesion: 0.28
Nodes (8): review_record(), sample_spread(), _run_missing(), worker(), one(), _run_one(), selected_review_version(), sim_outcome()

### Community 54 - "acme_metrics.py"
Cohesion: 0.15
Nodes (5): label_hash(), build_frame(), fig_html(), layer_of(), tiles()

### Community 55 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 56 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 57 - "version_d.py"
Cohesion: 0.07
Nodes (22): first_name(), intent_guide(), kb_by_id(), load_kb(), escalate(), get_article(), lookup_customer(), search_kb() (+14 more)

### Community 58 - "route"
Cohesion: 0.29
Nodes (11): route(), case(), test_claim_amounts_double_payment_claim_has_no_verb(), test_gate_fills_waiver_sentence_with_amount(), test_gate_needs_approval_goes_to_a_person(), test_gate_refuses_repeat_offer_in_thread(), test_ledger_does_not_leak_across_single_email_cases(), test_ledger_thread_stays_with_human() (+3 more)

### Community 59 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 60 - "Later: an ontology layer for Acme Fibre"
Cohesion: 0.10
Nodes (18): Decision: where the ontology lives (2026-10-28), Do we need it now, How to prove it first (measure before you believe), Implementation plan, Later: an ontology layer for Acme Fibre, Out of scope until project 6, Phase 0: Measure the problem (no new code), Phase 1: Write the ontology (definitions only) (+10 more)

### Community 61 - "test_router_rules.py"
Cohesion: 0.15
Nodes (9): world(), semantic_data(), world(), customer_writes(), router_does_not_fire(), router_fast_path(), router_fires(), test_a_retention_repeat_on_a_cancellation_is_not_money() (+1 more)

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

### Community 90 - "Day 4 · Version A: rules and templates (the honest baseline)"
Cohesion: 0.20
Nodes (9): 1 · Learn (about 30 minutes), 2 · Build (about 60 minutes), 3 · Record (5 minutes or less), Day 4 · Version A: rules and templates (the honest baseline), Done when, How I used AI, In my words, Video (+1 more)

### Community 91 - "ADR-001: How Acme Fibre should answer customer emails"
Cohesion: 0.22
Nodes (8): ADR-001: How Acme Fibre should answer customer emails, Consequences, Context, Decision, Evidence (from day 9), Open questions (projects 2 to 6), Options, What would change my mind

### Community 92 - "acme.py"
Cohesion: 0.21
Nodes (5): customer_card(), load_meta(), system_prompt(), user_message(), version_b()

### Community 93 - "run_agent"
Cohesion: 0.31
Nodes (7): run_agent(), _call(), _draft_only(), _parse(), _repair(), system_prompt_d(), test_gate_saves_canonical_filled_and_raw_offers()

### Community 94 - "Notes for the subject-matter expert"
Cohesion: 0.50
Nodes (3): Grader questions, Grounding questions (Task 3), Notes for the subject-matter expert

### Community 95 - "save_verdict"
Cohesion: 0.22
Nodes (8): validate_verdict(), _fail(), _keys(), move(), _next(), _pass(), _prev(), save_verdict()

### Community 97 - "AGENTS.md"
Cohesion: 0.29
Nodes (6): Codebase knowledge graph, Debugging in VS Code, Environment setup, How the BDD tests work, Repository layout, Running the tests

### Community 99 - "test_expert_review.py"
Cohesion: 0.22
Nodes (7): a_draft_handed_off(), a_draft_sent(), checks_that_fail(), given_test_case(), grader_flags(), _names(), world()

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

### Community 107 - "Later: grader ideas parked on day 5"
Cohesion: 0.40
Nodes (4): Grader false positives still open, Graders to add, Later: grader ideas parked on day 5, Test cases to add

### Community 108 - "Agent 365"
Cohesion: 0.40
Nodes (4): Agent 365, Governance, Identity, observability

### Community 109 - "Backtracking"
Cohesion: 0.50
Nodes (4): Backtracking, Covered, Source, Understand recursion visually

### Community 116 - "use_data_root"
Cohesion: 0.26
Nodes (6): use_data_root(), _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 120 - "run_agent"
Cohesion: 0.17
Nodes (9): check_draft(), asked_for_money(), draft_check_reports(), model_drafts(), _reply(), test_an_unrepairable_draft_escalates(), fake_chat(), test_the_gate_repairs_a_granting_draft() (+1 more)

### Community 121 - "resume"
Cohesion: 0.25
Nodes (8): default_sim_step(), _ha(), _he(), _hh(), resume(), show_saved_run(), _sim_load(), _to_sim()

### Community 124 - "case_of"
Cohesion: 0.33
Nodes (6): case_editor(), case_of(), _ed_save(), edit_case(), _sim_case(), sim_optional_inputs()

### Community 126 - "The problem"
Cohesion: 0.40
Nodes (5): user_prompt(), _settings(), sim_step_detail(), P1 — Mutable process globals can mix evaluation conditions, The problem

## Knowledge Gaps
- **1 isolated node(s):** `fde-first-principles`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 855 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `claim_checks()` connect `Lab` to `test_report_metrics.py`, `service.py`, `Workflow`, `acme_metrics.py`, `version_d.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_simulator_persistence.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1225071225071225 - nodes in this community are weakly interconnected._
- **Why does `server()` connect `server` to `test_simulator_persistence.py`, `test_report_metrics.py`, `RunInput`, `test_ontology.py`, `Span`, `Lab`, `app.py`, `chip`, `terms`, `pytest`, `load_business_rules`, `refresh_versions`, `.adapter`, `review_record`, `acme_metrics.py`, `version_d.py`, `save_verdict`, `resume`, `case_of`, `The problem`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Version` (e.g. with `AgentLoopAdapter` and `DirectAdapter`) actually correct?**
  _`Version` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_report_metrics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05548654244306418 - nodes in this community are weakly interconnected._