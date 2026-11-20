# Graph Report - continuous-learning  (2026-11-16)

## Corpus Check
- 215 files · ~154,842 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 101 file(s) not represented in the graph (top: .jsonl 33, .feature 21, .drawio 18)
- WARNING: 101 of 322 files seen (31%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2596 nodes · 5872 edges · 168 communities (137 shown, 31 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 387 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a90401dd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- run.py
- test_report_metrics.py
- versioned-simulator.md
- test_guardrails.py
- server
- test_out_of_steps.py
- re
- VersionRegistry
- ontology.py
- RunInput
- test_ontology.py
- Span
- test_review_flow.py
- evaluation-report.qmd
- version_c3.py
- ThreadStore
- Acme Review Studio
- Span
- app.py
- validate_ontology_ops
- chip
- test_c3_provider.py
- DataFrame
- pytest
- C3Provider
- direct.py
- Harness design
- terms
- load_lab
- test_simulator_http.py
- test_simulator_feature.py
- test_escalation_metrics.py
- test_escalation_rules.py
- when
- compute_entitlements
- RunStore
- Version
- test_grader_mutations.py
- ZAVAAirlines Fabric Data Agents - Q&A
- import_cases.py
- otel.py
- kb.md
- load_customers
- json
- refresh_versions
- Workflow
- studio-c3.yaml
- ADR-001: Support Email Automation Strategy
- json
- .adapter
- rescore.py
- review_record
- test_redteam_adapter.py
- acme_metrics.py
- config
- studio-declarative.yaml
- lab/version_d.py
- promote.py
- c3-agent.yaml
- Later: an ontology layer for Acme Fibre
- DirectAdapter
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
- kb_by_id
- load_business_rules
- ReviewStore
- adapter.py
- Day 10 · Read the failures, not the averages
- personas
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
- main
- test_redteam_checks.py
- _LogScorer
- Ranked actionable findings
- scorers.py
- AcmeAdapter
- service.py
- Red teaming D5 with PyRIT · plan
- AcmeAgentTarget
- HttpAdapter
- team-c3.yaml
- version-d.yaml
- Implementation plan
- team-offline.yaml
- Rate
- redteam/checks.py
- Build phases
- O1
- O2
- O3
- O4
- O5
- O6
- O7
- O8
- d1-split-three.yaml
- d2-split-five.yaml
- d3-fresh-thread.yaml
- d4-repeat-waiver.yaml
- d5-repeat-retention.yaml
- d6-third-party-joins.yaml
- d7-third-party-first.yaml
- d8-action-claimed.yaml
- RedactingSerializer
- R0 spike — PyRIT 1.1.0 around Version D
- objectives
- _no_ledger
- cblack-D5-glm53flash/report.md
- cwhite-D5-glm53flash/report.md
- replay-D5-glm53flash/report.md
- smoke-D-glm53flash/report.md
- FINDINGS.md
- redteam/NOTES-for-SME.md

## God Nodes (most connected - your core abstractions)
1. `server()` - 135 edges
2. `Version` - 76 edges
3. `RunResult` - 63 edges
4. `RunInput` - 50 edges
5. `when` - 50 edges
6. `Span` - 46 edges
7. `policy_violations()` - 42 edges
8. `load_business_rules()` - 42 edges
9. `build_decision_envelope()` - 40 edges
10. `SimulationService` - 37 edges

## Surprising Connections (you probably didn't know these)
- `Risks, open decisions and what is needed from you` --references--> `promote()`  [INFERRED]
  kata-use-cases/Red teaming D5 with PyRIT · plan.md → fde-first-principles/redteam/promote.py
- `Testing approach` --references--> `RunResult`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `Rounds become versions` --references--> `ReviewStore`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/store.py
- `Adding an implementation model` --references--> `Adapter`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/sim/trace.py
- `Architecture` --references--> `pipeline()`  [INFERRED]
  kata-use-cases/versioned-simulator.md → fde-first-principles/1-measure-before-you-believe/03-test-set-first/acme-review-studio/acme/ui_bits.py

## Import Cycles
- None detected.

## Communities (168 total, 31 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.17
Nodes (13): run_agent(), _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key() (+5 more)

### Community 1 - "run.py"
Cohesion: 0.13
Nodes (17): load_scripts(), load_seeds(), main(), must_survive(), persona_customer(), rewrite_case(), rewrite_ok(), _run_a() (+9 more)

### Community 2 - "test_report_metrics.py"
Cohesion: 0.12
Nodes (23): banner(), cases_run(), code_saves(), demo(), escalated(), escalated_by_code(), layer_fired(), missed() (+15 more)

### Community 3 - "versioned-simulator.md"
Cohesion: 0.05
Nodes (39): ClaudeCodeProvider, Accessibility, Adding an implementation model, Compare mode, Decisions to record, Demo in three minutes, Done when, Drift and pinning (+31 more)

### Community 4 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 5 - "server"
Cohesion: 0.06
Nodes (25): server(), batch_rev(), batch_status(), case_editor(), _ed_save(), edit_case(), _fail(), _keys() (+17 more)

### Community 6 - "test_out_of_steps.py"
Cohesion: 0.15
Nodes (17): customer_writes(), marked_out_of_steps(), model_called(), not_marked_out_of_steps(), one_more_turn(), person_gets_it(), reply_is(), reply_is_empty() (+9 more)

### Community 7 - "re"
Cohesion: 0.08
Nodes (14): amounts(), claim_checks(), eval_checks(), _flag(), guard_hits(), export_to_excel(), _item(), _put() (+6 more)

### Community 8 - "VersionRegistry"
Cohesion: 0.13
Nodes (11): Lab, team_topology(), version_d_topology(), canonical(), case_hash(), digest(), lab_snapshot(), label_hash() (+3 more)

### Community 9 - "ontology.py"
Cohesion: 0.11
Nodes (22): duplicate_payment_amount(), _alias_index(), _alias_pattern(), _bool_value(), customer_subgraph(), _data_cache(), cached(), get() (+14 more)

### Community 10 - "RunInput"
Cohesion: 0.14
Nodes (18): SimulationService, RunInput, test_adapter_errors_and_timeouts_are_saved(), test_c3_concurrent_versions_read_their_own_lab_snapshots(), test_release_requires_current_graded_cases_and_retired_resume_stays_held(), test_retention_removes_expired_runs_and_checkpoints_but_keeps_held_runs(), test_secrets_are_redacted_from_runs_checkpoints_and_logs(), test_snapshot_collection_preserves_runs_and_reviews() (+10 more)

### Community 11 - "test_ontology.py"
Cohesion: 0.11
Nodes (24): draft_check_reports(), world(), answer_is(), check_business_rule_cooldown(), check_headroom(), check_inherited_props(), check_inherited_role(), check_offer_eligibility() (+16 more)

### Community 12 - "Span"
Cohesion: 0.15
Nodes (25): render_comparison(), render_detail(), render_result(), compare_results(), Capabilities, RunResult, Topology, sim_comparison() (+17 more)

### Community 13 - "test_review_flow.py"
Cohesion: 0.13
Nodes (17): initial_mode(), suggest_mode(), validate_verdict(), _prefill(), check_fired(), ctx(), fail_no_critique(), fail_no_mode() (+9 more)

### Community 14 - "evaluation-report.qmd"
Cohesion: 0.08
Nodes (22): At a glance, Composition, Escalation rules, Label review, Provenance, What this set can't tell you, Where the cases come from, Examples from the expert's review (+14 more)

### Community 15 - "version_c3.py"
Cohesion: 0.09
Nodes (21): customer_text(), extract_json(), check_entitlement(), _envelope_brief(), _grants(), lookup_customer_c3(), _offer_mention(), offers_not_allowed() (+13 more)

### Community 16 - "ThreadStore"
Cohesion: 0.07
Nodes (28): canonical_offer(), claim_amounts(), fill_offers(), route(), _slot_norm(), thread_of(), ThreadStore, customer_writes() (+20 more)

### Community 17 - "Acme Review Studio"
Cohesion: 0.09
Nodes (21): Acme Review Studio, How the Claude Code call works, Project layout, Reference Review layout, Reports (Quarto), Reviewing the C3 agent's drafts, Run it, Set up (once) (+13 more)

### Community 18 - "Span"
Cohesion: 0.18
Nodes (21): _allows(), _button(), _children(), _descendants(), _exchange(), _exchange_view(), _has_turns(), render_grade() (+13 more)

### Community 19 - "app.py"
Cohesion: 0.13
Nodes (9): compare_reviews(), sample_spread(), highlight(), case_choices(), score_page(), _refresh_case_choices(), simulator_page(), version_choices() (+1 more)

### Community 20 - "validate_ontology_ops"
Cohesion: 0.11
Nodes (21): meaning_checks(), validate_ontology_ops(), _finding(), test_article_individual_ids_cannot_be_swapped(), test_knowledge_article_drift_has_actionable_files(), test_legacy_kb_binding_must_match_the_concept(), test_legacy_policy_rule_checks_include_the_concession_limit(), test_policy_individual_numbers_cannot_be_swapped() (+13 more)

### Community 21 - "chip"
Cohesion: 0.14
Nodes (17): chip(), icon(), customer_chips(), review_page(), case_header(), cur(), draft_meta(), email_card() (+9 more)

### Community 22 - "test_c3_provider.py"
Cohesion: 0.11
Nodes (19): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+11 more)

### Community 23 - "DataFrame"
Cohesion: 0.18
Nodes (4): Evidence, mask(), nonempty(), 6. Every recommended metric — why / how / decision

### Community 24 - "pytest"
Cohesion: 0.07
Nodes (14): version_c3(), case_is_labelled(), every_intent_defined(), labelled_cases(), world(), test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes(), agent_finishes() (+6 more)

### Community 26 - "direct.py"
Cohesion: 0.11
Nodes (9): c3_output(), direct_output(), no_draft(), validate_draft(), AgentLoopAdapter, turn_spans(), DeclarativeAdapter, VersionDAdapter (+1 more)

### Community 27 - "Harness design"
Cohesion: 0.22
Nodes (6): not_english(), reveals_limit(), _ngrams(), prompt_leak(), _words(), Harness design

### Community 28 - "terms"
Cohesion: 0.12
Nodes (20): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), _asserted_store(), concept_labels(), concept_provenance(), define(), policy_rules() (+12 more)

### Community 29 - "load_lab"
Cohesion: 0.06
Nodes (18): _bool(), _history(), load_lab(), _payments(), read_review_log(), _split(), AppSettings, judge_prompt() (+10 more)

### Community 30 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout() (+4 more)

### Community 31 - "test_simulator_feature.py"
Cohesion: 0.08
Nodes (31): meaning_card(), fact_rows(), origin(), pipeline(), approve(), batch_offline(), batch_started(), c3_version() (+23 more)

### Community 32 - "test_escalation_metrics.py"
Cohesion: 0.21
Nodes (11): bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is(), recall_is() (+3 more)

### Community 33 - "test_escalation_rules.py"
Cohesion: 0.13
Nodes (17): agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes(), customer_writes(), envelope_decides(), escalation_sources_are(), every_labelled_case() (+9 more)

### Community 34 - "when"
Cohesion: 0.08
Nodes (28): Codebase knowledge graph, Debugging in VS Code, Environment setup, How the BDD tests work, Repository layout, Running the tests, run_case(), when (+20 more)

### Community 35 - "compute_entitlements"
Cohesion: 0.12
Nodes (9): months_since(), outage_exceeds_hours(), _parse_date(), _limit_context(), compute_entitlements(), excluded_from_limit(), ask_excluded(), compute_for_customer() (+1 more)

### Community 36 - "RunStore"
Cohesion: 0.16
Nodes (3): _json(), _now(), RunStore

### Community 37 - "Version"
Cohesion: 0.12
Nodes (9): OfflineProvider, OrchestratedAdapter, RecordedProvider, MultiAgentAdapter, pin_status(), version_heading(), manifest_diff(), Version (+1 more)

### Community 38 - "test_grader_mutations.py"
Cohesion: 0.16
Nodes (15): _add_each_banned(), _append(), _cases_where(), _drop_each_fact(), grader_fails(), grader_flags(), grader_passes(), mutate() (+7 more)

### Community 39 - "ZAVAAirlines Fabric Data Agents - Q&A"
Cohesion: 0.11
Nodes (17): 10. Unstructured Data Support, 11. Consistent Responses Across Teams, Excel, and Copilot Studio, 12. Fabric Data Agent as Knowledge Source, 13. Direct OneLake Access vs Data Agents, 14. Architecture Responsibilities, 15. External AI Access Pattern, 16. Fabric Data Agents vs Power BI Copilot, 1. Improve Query Generation Accuracy (+9 more)

### Community 40 - "import_cases.py"
Cohesion: 0.22
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 41 - "otel.py"
Cohesion: 0.16
Nodes (16): _attributes(), _hex(), _layout(), place(), _name(), _provider_name(), _span_attributes(), to_otlp() (+8 more)

### Community 42 - "kb.md"
Cohesion: 0.12
Nodes (16): KB01 · Billing cycle and due dates, KB02 · Late payment fee, KB03 · Payment methods, KB04 · Refunds and credits, KB05 · Outages and restoration updates, KB06 · Outage credit, KB07 · Slow speed or no internet: first checks, KB08 · Technician visits (+8 more)

### Community 43 - "load_customers"
Cohesion: 0.18
Nodes (8): load_outages(), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 44 - "json"
Cohesion: 0.20
Nodes (9): run_judge(), load_meta(), compare_markdown(), main(), markdown(), regrade(), run_dir(), summary() (+1 more)

### Community 45 - "refresh_versions"
Cohesion: 0.19
Nodes (14): _apply_retention(), case_list(), _keep_current_visible(), _name_candidate(), progress(), refresh_versions(), _release_version(), _retire_version() (+6 more)

### Community 46 - "Workflow"
Cohesion: 0.16
Nodes (14): Deps, _trace(), Workflow, check(), decide(), draft(), fetch(), human() (+6 more)

### Community 47 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 48 - "ADR-001: Support Email Automation Strategy"
Cohesion: 0.12
Nodes (15): 5-Minute Executive Readout for Acme Fibre, ADR-001: Support Email Automation Strategy, Core Operating Reality, Phased Operational Strategy:, Principal Engineer Insights:, Slide 1: Executive Summary & Recommendation, Slide 2: Three Competing Paradigms Evaluated, Slide 3: Empirical Scorecard (Statistical Error Bars) (+7 more)

### Community 49 - "json"
Cohesion: 0.10
Nodes (22): data_root(), fingerprint(), git_commit(), load_cases(), load_results(), save_results(), summary(), kb_only() (+14 more)

### Community 50 - ".adapter"
Cohesion: 0.19
Nodes (16): make_provider(), case_of(), provider_status(), replay_sources(), selected_sim_version(), _sim_case(), sim_fields(), sim_history_controls() (+8 more)

### Community 51 - "rescore.py"
Cohesion: 0.19
Nodes (11): _approved(), _negated(), _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before() (+3 more)

### Community 52 - "review_record"
Cohesion: 0.43
Nodes (7): review_record(), run_case(), _run_missing(), worker(), one(), _run_one(), selected_review_version()

### Community 53 - "test_redteam_adapter.py"
Cohesion: 0.14
Nodes (20): fake_adapter(), fake_agent(), _fresh_world(), handle_system_prompt(), handle_two_earlier(), ledger_matches_run_d(), _line(), logged_adapter() (+12 more)

### Community 54 - "acme_metrics.py"
Cohesion: 0.10
Nodes (9): banner(), build_frame(), fig_html(), html_table(), layer_of(), provenance_table(), sha256(), tiles() (+1 more)

### Community 55 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 56 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 57 - "lab/version_d.py"
Cohesion: 0.08
Nodes (17): intent_guide(), load_customers(), escalate(), amounts_asked_for(), escalation_triggers(), percent_asks_in_rupees(), _trigger(), amounts() (+9 more)

### Community 58 - "promote.py"
Cohesion: 0.19
Nodes (12): draft_case(), main(), promote(), check_quality(), load_lines(), main(), triage_rows(), _line() (+4 more)

### Community 59 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 60 - "Later: an ontology layer for Acme Fibre"
Cohesion: 0.17
Nodes (10): Decision: where the ontology lives (2026-10-28), Do we need it now, How to prove it first (measure before you believe), Later: an ontology layer for Acme Fibre, Recommended tool: pyoxigraph, Sketch, When it becomes worth building, Acme Fibre reply policy (+2 more)

### Community 61 - "DirectAdapter"
Cohesion: 0.13
Nodes (6): DirectAdapter, raw_response(), usage_of(), VersionBAdapter, _ms(), triage()

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

### Community 92 - "kb_by_id"
Cohesion: 0.10
Nodes (16): Acme Fibre: the project brief (fictional), The files, conversation(), customer_card(), first_name(), kb_by_id(), load_kb(), outage_for() (+8 more)

### Community 93 - "load_business_rules"
Cohesion: 0.16
Nodes (12): _deep_update(), _default_rules(), load_business_rules(), _rules_at(), define_term(), system_prompt_d(), black_box(), pack() (+4 more)

### Community 94 - "ReviewStore"
Cohesion: 0.23
Nodes (7): ReviewStore, _export(), load(), test_dataset_banner_omits_run_progress_but_keeps_warnings(), test_provenance_uses_full_hashes_and_escapes_values(), test_reports_select_versions_and_keep_the_round_alias(), test_legacy_reviews_migrate_and_round_trip_through_excel()

### Community 95 - "adapter.py"
Cohesion: 0.13
Nodes (6): use(), find_system_prompt(), RefusedSystemPrompt, TurnLog, main(), finished_run()

### Community 96 - "Day 10 · Read the failures, not the averages"
Cohesion: 0.10
Nodes (19): 1. Round 1 evaluation summary, 2. Qualitative failure analysis (evidence first, categories after), 3. Quantitative measurement framework, 5. Principal Engineer's assessment, Mode 1 — Deterministic Step-6 "unsupported amount" false positives (5 cases: c02, c22, c44, c54, c77), Mode 2 — Model over-escalation on answerable cases (2 cases: c23, c79), Mode 3 — Unapproved retention offer inside an escalated draft (1 case: c36), Round 1 — Principal Engineer Review of the Acme Fibre Email Drafting Solution (+11 more)

### Community 97 - "personas"
Cohesion: 0.10
Nodes (19): customer_id, stands_for, customer_id, stands_for, customer_id, stands_for, personas, clean_long_tenure (+11 more)

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
Cohesion: 0.11
Nodes (18): check_draft(), _envelope_brief_d(), _record_block(), run_agent(), _call(), _draft_only(), _gate(), _parse() (+10 more)

### Community 121 - "resume"
Cohesion: 0.25
Nodes (8): default_sim_step(), _ha(), _he(), _hh(), resume(), show_saved_run(), _sim_load(), _to_sim()

### Community 123 - "main"
Cohesion: 0.13
Nodes (4): HandoffScorer, main(), _RowScorer, UnattendedViolationScorer

### Community 124 - "test_redteam_checks.py"
Cohesion: 0.12
Nodes (11): action_claim(), repeat_grant(), _rfind_word(), action_claim_fires(), agent_replies(), customer_replies(), prompt_leak_fires(), repeat_grant_fires() (+3 more)

### Community 125 - "_LogScorer"
Cohesion: 0.15
Nodes (3): HandoffScorer, _lines(), _LogScorer

### Community 126 - "Ranked actionable findings"
Cohesion: 0.11
Nodes (18): user_prompt(), _settings(), sim_step_detail(), Acme Review Studio review, Architecture, Delivered, P1 — Mutable process globals can mix evaluation conditions, P1 — Parsed model output lacks local schema validation (+10 more)

### Community 127 - "scorers.py"
Cohesion: 0.20
Nodes (7): _promises_concession(), unearned_concession(), check_names(), expected_handoff(), fired_checks(), objective(), verdict()

### Community 129 - "AcmeAdapter"
Cohesion: 0.16
Nodes (3): AcmeAdapter, AcmeAgentTarget, LabLLMTarget

### Community 131 - "Red teaming D5 with PyRIT · plan"
Cohesion: 0.17
Nodes (11): unsupported_number(), At a glance, Attack campaign, From finding to fix, Lessons from real deployments, Red teaming D5 with PyRIT · plan, Risks, open decisions and what is needed from you, Scoring and metrics (+3 more)

### Community 134 - "team-c3.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 135 - "version-d.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 136 - "Implementation plan"
Cohesion: 0.18
Nodes (11): Implementation plan, Out of scope until project 6, Phase 0: Measure the problem (no new code), Phase 1: Write the ontology (definitions only), Phase 2: Loader and tests, Phase 3: Version B with the glossary, Phase 4: Version C with a lookup tool (optional), Phase 5: Decide with evidence (+3 more)

### Community 137 - "team-offline.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 138 - "Rate"
Cohesion: 0.31
Nodes (4): Rate, wilson(), 4. Measurement report, LLM-as-judge validation (Mode 3's instrument)

### Community 139 - "redteam/checks.py"
Cohesion: 0.39
Nodes (5): allowed_numbers(), _as_float(), _numbers(), _record_numbers(), walk()

### Community 140 - "Build phases"
Cohesion: 0.25
Nodes (8): Build phases, R0 · Spike and pin, R1 · Threat model as data, R2 · Adapter, scorers and run log, R3 · Static campaigns, R4 · Adaptive campaign and human session, R5 · Triage and scorer check, R6 · Report, regression pack and gate

### Community 141 - "O1"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O1

### Community 142 - "O2"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O2

### Community 143 - "O3"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O3

### Community 144 - "O4"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O4

### Community 145 - "O5"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O5

### Community 146 - "O6"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O6

### Community 147 - "O7"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O7

### Community 148 - "O8"
Cohesion: 0.29
Nodes (7): checks, expected_handoff, goal, name, owasp, policy_rules, O8

### Community 149 - "d1-split-three.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 150 - "d2-split-five.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 151 - "d3-fresh-thread.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 152 - "d4-repeat-waiver.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 153 - "d5-repeat-retention.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 154 - "d6-third-party-joins.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 155 - "d7-third-party-first.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 156 - "d8-action-claimed.yaml"
Cohesion: 0.29
Nodes (6): conversations, thread, turns, id, objective, persona

### Community 158 - "R0 spike — PyRIT 1.1.0 around Version D"
Cohesion: 0.40
Nodes (4): Go or no-go, pyrit 1.1.0 API notes (docs are stale), R0 spike — PyRIT 1.1.0 around Version D, The six questions

## Knowledge Gaps
- **1 isolated node(s):** `fde-first-principles`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1118 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Round 1 — Principal Engineer Review of the Acme Fibre Email Drafting Solution` connect `Day 10 · Read the failures, not the averages` to `Rate`, `DataFrame`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13118279569892474 - nodes in this community are weakly interconnected._
- **Why does `claim_checks()` connect `re` to `Day 10 · Read the failures, not the averages`, `direct.py`, `Ranked actionable findings`, `Workflow`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `Version` (e.g. with `AgentLoopAdapter` and `DirectAdapter`) actually correct?**
  _`Version` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_report_metrics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11724137931034483 - nodes in this community are weakly interconnected._