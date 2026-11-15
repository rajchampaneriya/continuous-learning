# Graph Report - continuous-learning  (2026-11-15)

## Corpus Check
- 158 files · ~126,371 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 85 file(s) not represented in the graph (top: .jsonl 27, .feature 18, .drawio 18)
- WARNING: 85 of 249 files seen (34%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 1997 nodes · 4515 edges · 118 communities (101 shown, 17 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 357 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9369a673`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- DataFrame
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
- route
- Acme Review Studio
- validate_ontology_ops
- app.py
- RunResult
- chip
- test_c3_provider.py
- acme_metrics.py
- pytest
- lab.py
- OrchestratedAdapter
- evals.py
- test_router_rules.py
- direct.py
- test_simulator_http.py
- ui_bits.py
- test_escalation_metrics.py
- test_escalation_rules.py
- when
- Round 1 — Principal Engineer Review of the Acme Fibre Email Drafting Solution
- RunStore
- version_c4.py
- test_grader_mutations.py
- ZAVAAirlines Fabric Data Agents - Q&A
- import_cases.py
- test_version_d.py
- kb.md
- load_customers
- judge_round1.py
- refresh_versions
- Ranked actionable findings
- studio-c3.yaml
- ADR-001: Support Email Automation Strategy
- json
- .adapter
- load_business_rules
- review_record
- Day 10 · Read the failures, not the averages
- config
- studio-declarative.yaml
- build_decision_envelope
- c3-agent.yaml
- Later: an ontology layer for Acme Fibre
- Implementation plan
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
- mask
- ScriptedResponse
- Rate
- AGENTS.md
- fde-first-principles/README.md
- test_expert_review.py
- Holdout set
- article.md
- Conversation Summary
- Continuous Learning
- rescore.py
- subsets.py
- Later: grader ideas parked on day 5
- Agent 365
- Backtracking
- checks.py
- Boosted Trees at the Chai Stall
- CLAUDE.md
- .claude/CLAUDE.md
- use_data_root
- fde-first-principles
- HttpAdapter
- run_agent

## God Nodes (most connected - your core abstractions)
1. `server()` - 128 edges
2. `Version` - 61 edges
3. `RunInput` - 52 edges
4. `RunResult` - 49 edges
5. `VersionRegistry` - 40 edges
6. `build_decision_envelope()` - 40 edges
7. `policy_violations()` - 38 edges
8. `when` - 38 edges
9. `SimulationService` - 35 edges
10. `ReviewStore` - 32 edges

## Surprising Connections (you probably didn't know these)
- `Rounds become versions` --references--> `ReviewStore`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/store.py
- `Testing approach` --references--> `RunResult`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `Adding an implementation model` --references--> `Adapter`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `How the BDD tests work` --references--> `policy_violations()`  [INFERRED]
  AGENTS.md → fde-first-principles/lab/evals.py
- `Architecture` --references--> `RunInput`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py

## Import Cycles
- None detected.

## Communities (118 total, 17 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.16
Nodes (14): run_agent(), _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), extract_json() (+6 more)

### Community 2 - "test_report_metrics.py"
Cohesion: 0.08
Nodes (28): ReviewStore, score_rounds(), load(), banner(), cases_run(), code_saves(), demo(), escalated() (+20 more)

### Community 3 - "versioned-simulator.md"
Cohesion: 0.04
Nodes (41): ClaudeCodeProvider, _parse_json_text(), _result(), Accessibility, Adding an implementation model, Compare mode, Decisions to record, Demo in three minutes (+33 more)

### Community 4 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 5 - "server"
Cohesion: 0.05
Nodes (33): sample_spread(), default_sim_step(), server(), batch_rev(), batch_status(), case_editor(), case_of(), _ed_save() (+25 more)

### Community 6 - "test_out_of_steps.py"
Cohesion: 0.07
Nodes (28): world(), version_c3(), test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes(), customer_writes(), marked_out_of_steps(), model_called(), not_marked_out_of_steps() (+20 more)

### Community 7 - "service.py"
Cohesion: 0.08
Nodes (10): direct_output(), no_draft(), validate_draft(), DeclarativeAdapter, redact(), RedactingSerializer, secret_values(), manifest_diff() (+2 more)

### Community 8 - "VersionRegistry"
Cohesion: 0.13
Nodes (11): Lab, canonical(), case_hash(), digest(), lab_snapshot(), label_hash(), _sheet_hashes(), VersionRegistry (+3 more)

### Community 9 - "ontology.py"
Cohesion: 0.13
Nodes (21): _alias_index(), _alias_pattern(), _asserted_store(), _bool_value(), customer_subgraph(), _data_cache(), cached(), get() (+13 more)

### Community 10 - "RunInput"
Cohesion: 0.13
Nodes (17): RunInput, run_case(), run_case(), test_adapter_errors_and_timeouts_are_saved(), test_c3_concurrent_versions_read_their_own_lab_snapshots(), test_release_requires_current_graded_cases_and_retired_resume_stays_held(), test_retention_removes_expired_runs_and_checkpoints_but_keeps_held_runs(), test_secrets_are_redacted_from_runs_checkpoints_and_logs() (+9 more)

### Community 11 - "test_ontology.py"
Cohesion: 0.10
Nodes (27): knowledge_page(), meaning_concept_card(), _meaning_concept_changed(), meaning_rule_detail(), concept_labels(), concept_provenance(), define(), policy_rules() (+19 more)

### Community 12 - "Span"
Cohesion: 0.16
Nodes (25): _button(), render_comparison(), render_detail(), render_result(), _text(), _topology(), _tree(), branch() (+17 more)

### Community 13 - "test_review_flow.py"
Cohesion: 0.13
Nodes (17): initial_mode(), suggest_mode(), validate_verdict(), _prefill(), check_fired(), ctx(), fail_no_critique(), fail_no_mode() (+9 more)

### Community 14 - "evaluation-report.qmd"
Cohesion: 0.08
Nodes (22): At a glance, Composition, Escalation rules, Label review, Provenance, What this set can't tell you, Where the cases come from, Examples from the expert's review (+14 more)

### Community 15 - "version_c3.py"
Cohesion: 0.07
Nodes (26): intent_guide(), kb_by_id(), load_kb(), escalate(), get_article(), lookup_customer(), search_kb(), _words() (+18 more)

### Community 16 - "route"
Cohesion: 0.19
Nodes (8): route(), thread_of(), ThreadStore, version_d(), test_ledger_catches_claim_built_over_turns(), test_ledger_does_not_leak_across_single_email_cases(), test_ledger_thread_stays_with_human(), test_threads_suite_ledger_matches_labels()

### Community 17 - "Acme Review Studio"
Cohesion: 0.09
Nodes (21): Acme Review Studio, How the Claude Code call works, Project layout, Reference Review layout, Reports (Quarto), Reviewing the C3 agent's drafts, Run it, Set up (once) (+13 more)

### Community 18 - "validate_ontology_ops"
Cohesion: 0.12
Nodes (17): validate_ontology_ops(), run_ops_validation(), Checks, Code changes, Concept card, Demo in three minutes, Design: a Meaning tab in Acme Review Studio, Done when (+9 more)

### Community 19 - "app.py"
Cohesion: 0.11
Nodes (11): make_provider(), compare_reviews(), case_choices(), review_page(), score_page(), provider_status(), _refresh_case_choices(), simulator_page() (+3 more)

### Community 20 - "RunResult"
Cohesion: 0.15
Nodes (5): SimulationService, AppSettings, world(), service(), service()

### Community 21 - "chip"
Cohesion: 0.16
Nodes (16): eval_checks(), chip(), highlight(), customer_chips(), case_header(), cur(), draft_meta(), email_card() (+8 more)

### Community 22 - "test_c3_provider.py"
Cohesion: 0.12
Nodes (17): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+9 more)

### Community 23 - "acme_metrics.py"
Cohesion: 0.09
Nodes (9): banner(), build_frame(), fig_html(), html_table(), layer_of(), provenance_table(), sha256(), tiles() (+1 more)

### Community 24 - "pytest"
Cohesion: 0.17
Nodes (4): case_is_labelled(), every_intent_defined(), labelled_cases(), world()

### Community 25 - "lab.py"
Cohesion: 0.08
Nodes (13): _bool(), _history(), _item(), load_lab(), _payments(), _review_row_formulas(), _split(), c3_output() (+5 more)

### Community 26 - "OrchestratedAdapter"
Cohesion: 0.21
Nodes (4): OrchestratedAdapter, RecordedProvider, Version, Settings

### Community 27 - "evals.py"
Cohesion: 0.08
Nodes (18): load_customers(), escalation_triggers(), percent_asks_in_rupees(), _trigger(), amounts(), _limit_context(), other_customer_details(), _plan_in_sentence() (+10 more)

### Community 28 - "test_router_rules.py"
Cohesion: 0.18
Nodes (8): draft_check_reports(), world(), customer_writes(), router_does_not_fire(), router_fast_path(), router_fires(), test_a_retention_repeat_on_a_cancellation_is_not_money(), world()

### Community 29 - "direct.py"
Cohesion: 0.09
Nodes (7): OfflineProvider, AgentLoopAdapter, DirectAdapter, VersionBAdapter, pinned(), scripted_adapter(), valid_contract()

### Community 30 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout() (+4 more)

### Community 31 - "ui_bits.py"
Cohesion: 0.21
Nodes (5): icon(), pipeline(), Elements, test_icons_have_no_network_or_accessible_name(), test_pipeline_keyboard_order_and_untrusted_details()

### Community 32 - "test_escalation_metrics.py"
Cohesion: 0.21
Nodes (11): bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is(), recall_is() (+3 more)

### Community 33 - "test_escalation_rules.py"
Cohesion: 0.13
Nodes (17): agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes(), customer_writes(), envelope_decides(), escalation_sources_are(), every_labelled_case() (+9 more)

### Community 34 - "when"
Cohesion: 0.07
Nodes (26): run_case(), run_email(), read(), read_round(), when, _approved(), _negated(), not_english() (+18 more)

### Community 35 - "Round 1 — Principal Engineer Review of the Acme Fibre Email Drafting Solution"
Cohesion: 0.20
Nodes (10): 1. Round 1 evaluation summary, 2. Qualitative failure analysis (evidence first, categories after), 3. Quantitative measurement framework, 4. Measurement report, 5. Principal Engineer's assessment, LLM-as-judge validation (Mode 3's instrument), Mode 1 — Deterministic Step-6 "unsupported amount" false positives (5 cases: c02, c22, c44, c54, c77), Mode 2 — Model over-escalation on answerable cases (2 cases: c23, c79) (+2 more)

### Community 36 - "RunStore"
Cohesion: 0.22
Nodes (3): _json(), _now(), RunStore

### Community 37 - "version_c4.py"
Cohesion: 0.15
Nodes (12): customer_text(), run_agent(), _answer(), _finish(), system_prompt(), _envelope_brief_c4(), _excerpt(), run_agent() (+4 more)

### Community 38 - "test_grader_mutations.py"
Cohesion: 0.17
Nodes (15): _add_each_banned(), _append(), _cases_where(), _drop_each_fact(), grader_fails(), grader_flags(), grader_passes(), mutate() (+7 more)

### Community 39 - "ZAVAAirlines Fabric Data Agents - Q&A"
Cohesion: 0.11
Nodes (17): 10. Unstructured Data Support, 11. Consistent Responses Across Teams, Excel, and Copilot Studio, 12. Fabric Data Agent as Knowledge Source, 13. Direct OneLake Access vs Data Agents, 14. Architecture Responsibilities, 15. External AI Access Pattern, 16. Fabric Data Agents vs Power BI Copilot, 1. Improve Query Generation Accuracy (+9 more)

### Community 40 - "import_cases.py"
Cohesion: 0.13
Nodes (15): export_to_excel(), _put(), read_review_log(), _restore_chart(), _export(), _add_headers(), _copy_style(), import_cases() (+7 more)

### Community 41 - "test_version_d.py"
Cohesion: 0.29
Nodes (9): fill_offers(), case(), test_claim_amounts_double_payment_claim_has_no_verb(), test_gate_fills_waiver_sentence_with_amount(), test_gate_needs_approval_goes_to_a_person(), test_gate_refuses_repeat_offer_in_thread(), test_router_fast_path_on_legal_threat(), test_router_worker_path_when_no_rule_fires() (+1 more)

### Community 42 - "kb.md"
Cohesion: 0.12
Nodes (16): KB01 · Billing cycle and due dates, KB02 · Late payment fee, KB03 · Payment methods, KB04 · Refunds and credits, KB05 · Outages and restoration updates, KB06 · Outage credit, KB07 · Slow speed or no internet: first checks, KB08 · Technician visits (+8 more)

### Community 43 - "load_customers"
Cohesion: 0.19
Nodes (7): cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 44 - "judge_round1.py"
Cohesion: 0.33
Nodes (4): judge_prompt(), main(), work(), run_judge()

### Community 45 - "refresh_versions"
Cohesion: 0.14
Nodes (20): _apply_retention(), case_list(), _fail(), _keep_current_visible(), _keys(), move(), _name_candidate(), _next() (+12 more)

### Community 46 - "Ranked actionable findings"
Cohesion: 0.08
Nodes (27): _trace(), user_prompt(), check(), draft(), fetch(), human(), receive(), route() (+19 more)

### Community 47 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 48 - "ADR-001: Support Email Automation Strategy"
Cohesion: 0.12
Nodes (15): 5-Minute Executive Readout for Acme Fibre, ADR-001: Support Email Automation Strategy, Core Operating Reality, Phased Operational Strategy:, Principal Engineer Insights:, Slide 1: Executive Summary & Recommendation, Slide 2: Three Competing Paradigms Evaluated, Slide 3: Empirical Scorecard (Statistical Error Bars) (+7 more)

### Community 49 - "json"
Cohesion: 0.10
Nodes (21): data_root(), fingerprint(), git_commit(), load_cases(), save_results(), score(), summary(), kb_only() (+13 more)

### Community 50 - ".adapter"
Cohesion: 0.35
Nodes (7): replay_sources(), selected_sim_version(), sim_fields(), sim_replay_options(), _sim_run(), sim_run_control(), sim_version_status()

### Community 51 - "load_business_rules"
Cohesion: 0.13
Nodes (12): load_outages(), outage_for(), _deep_update(), _default_rules(), duplicate_payment_amount(), load_business_rules(), months_since(), outage_exceeds_hours() (+4 more)

### Community 52 - "review_record"
Cohesion: 0.33
Nodes (6): review_record(), _run_missing(), worker(), one(), _run_one(), selected_review_version()

### Community 54 - "Day 10 · Read the failures, not the averages"
Cohesion: 0.15
Nodes (11): 1 · Learn (about 15 minutes), 2 · Build (about 70 minutes), 3 · Record (5 minutes or less), Before you start: three things the day 9 numbers hide, Day 10 · Read the failures, not the averages, Done when, How I used AI, In my words (+3 more)

### Community 55 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 56 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 57 - "build_decision_envelope"
Cohesion: 0.14
Nodes (10): canonical_offer(), _slot_norm(), customer_writes(), gate_escalates(), grant_sentences(), model_returns_slots(), reply_contains(), test_canonical_offer_maps_to_the_catalogue() (+2 more)

### Community 59 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 60 - "Later: an ontology layer for Acme Fibre"
Cohesion: 0.17
Nodes (10): Decision: where the ontology lives (2026-10-28), Do we need it now, How to prove it first (measure before you believe), Later: an ontology layer for Acme Fibre, Recommended tool: pyoxigraph, Sketch, When it becomes worth building, Acme Fibre reply policy (+2 more)

### Community 61 - "Implementation plan"
Cohesion: 0.14
Nodes (13): Implementation plan, Out of scope until project 6, Phase 0: Measure the problem (no new code), Phase 1: Write the ontology (definitions only), Phase 2: Loader and tests, Phase 3: Version B with the glossary, Phase 4: Version C with a lookup tool (optional), Phase 5: Decide with evidence (+5 more)

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
Cohesion: 0.14
Nodes (10): Acme Fibre: the project brief (fictional), The files, conversation(), customer_card(), first_name(), load_meta(), load_results(), system_prompt() (+2 more)

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

### Community 104 - "rescore.py"
Cohesion: 0.50
Nodes (6): _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before()

### Community 107 - "Later: grader ideas parked on day 5"
Cohesion: 0.40
Nodes (4): Grader false positives still open, Graders to add, Later: grader ideas parked on day 5, Test cases to add

### Community 108 - "Agent 365"
Cohesion: 0.40
Nodes (4): Agent 365, Governance, Identity, observability

### Community 109 - "Backtracking"
Cohesion: 0.50
Nodes (4): Backtracking, Covered, Source, Understand recursion visually

### Community 110 - "checks.py"
Cohesion: 0.36
Nodes (6): amounts(), claim_checks(), _flag(), guard_hits(), decide(), guard_try_result()

### Community 116 - "use_data_root"
Cohesion: 0.29
Nodes (5): _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 120 - "run_agent"
Cohesion: 0.14
Nodes (15): check_draft(), run_agent(), _call(), _draft_only(), _gate(), _parse(), _repair(), system_prompt_d() (+7 more)

## Knowledge Gaps
- **1 isolated node(s):** `fde-first-principles`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 853 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `server()` connect `server` to `test_report_metrics.py`, `VersionRegistry`, `ontology.py`, `RunInput`, `test_ontology.py`, `Span`, `test_review_flow.py`, `version_c3.py`, `validate_ontology_ops`, `app.py`, `chip`, `ui_bits.py`, `import_cases.py`, `refresh_versions`, `Ranked actionable findings`, `.adapter`, `load_business_rules`, `review_record`, `checks.py`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_report_metrics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `claim_checks()` connect `checks.py` to `Round 1 — Principal Engineer Review of the Acme Fibre Email Drafting Solution`, `evals.py`, `Ranked actionable findings`, `service.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Version` (e.g. with `AgentLoopAdapter` and `DirectAdapter`) actually correct?**
  _`Version` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `versioned-simulator.md` be split into smaller, more focused modules?**
  _Cohesion score 0.044326241134751775 - nodes in this community are weakly interconnected._