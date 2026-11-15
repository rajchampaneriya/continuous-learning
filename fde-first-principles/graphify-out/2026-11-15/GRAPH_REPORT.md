# Graph Report - fde-first-principles  (2026-11-15)

## Corpus Check
- 100 files · ~93,059 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 78 file(s) not represented in the graph (top: .jsonl 27, .feature 19, .drawio 12)
- WARNING: 78 of 214 files seen (36%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2058 nodes · 5870 edges · 105 communities (78 shown, 27 thin omitted)
- Extraction: 84% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 903 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `935f1050`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- Version
- ontology.py
- RunResult
- test_escalation_metrics.py
- version_choices
- version_d.py
- compute_entitlements
- Review Studio server
- Day 09 notebook (success-cost-latency)
- test_c3_provider.py
- version_c3
- test_policy_rules.py
- test_escalation_rules.py
- direct.py
- render.py
- test_review_flow.py
- import_cases.py
- RunResult
- Day 9 · Run all three: success, cost, latency
- Studio evidence frame
- RunResult
- Review dashboard (when do humans help?)
- test_simulator_feature.py
- test_adapter_contract.py
- Build a workflow, not an agent: B + safety router + policy verifier
- acme_metrics.py
- test_report_metrics.py
- app.py
- FDE First Principles learning log
- ScriptedResponse
- test_version_d.py
- acme_tools.py
- business_rules.py
- load_cases
- ADR-001 diagram: B with a safety router and a policy check
- test_simulator_http.py
- test_grader_mutations.py
- Day 8: agent loop and failures
- acme.py
- Standard error of an accuracy: sqrt(p(1-p)/n)
- version_b
- service.py
- load_cases
- acme_metrics.py
- Evaluation report (release decision)
- test_gate_draft.py
- then
- Rate
- _sim_run
- run_agent
- Dataset card (Acme test set)
- studio-c3.yaml
- ReviewStore
- config
- Safety router
- KB slow speed and technician
- test_holdout_run.py
- KB new installation
- KB search queries
- Project config
- C3Provider
- versions.py
- c3-agent.yaml
- Stage 4 · Statistical evaluation: 'How sure are we?'
- studio-offline.yaml
- version-b.yaml
- test_ontology.py
- test_guardrails.py
- eval_checks
- offline-direct.yaml
- Load customer card and outages
- Acme labelled test set (cases.jsonl)
- Embedding model rubric (why embeddinggemma)
- C3Provider
- HttpAdapter
- test_cases_data.py
- pytest
- Adapter
- Review dashboard (when do humans help?)
- Tags
- Day 06 notebook (one-llm-call)
- app.py
- fixture
- studio-declarative.yaml
- Version parameter and legacy round alias
- rescore.py
- reason_owl_rl
- Failure analysis

## God Nodes (most connected - your core abstractions)
1. `server()` - 134 edges
2. `policy_violations()` - 66 edges
3. `Version` - 64 edges
4. `score()` - 60 edges
5. `RunResult` - 53 edges
6. `RunInput` - 51 edges
7. `build_decision_envelope()` - 46 edges
8. `VersionRegistry` - 42 edges
9. `compute_entitlements()` - 41 edges
10. `load_cases()` - 41 edges

## Surprising Connections (you probably didn't know these)
- `Similarity search (cosine, top 3)` --semantically_similar_to--> `search_kb()`  [AMBIGUOUS] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio → lab/acme_tools.py
- `version_b()` --semantically_similar_to--> `version_b()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/notebook.ipynb → lab/version_b.py
- `ask()` --semantically_similar_to--> `chat()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/01-an-llm-call-is-http/notebook.ipynb → lab/llm.py
- `extract_json()` --semantically_similar_to--> `Answer JSON schema {intent, reply, needs_human}`  [INFERRED] [semantically similar]
  lab/llm.py → 1-measure-before-you-believe/06-one-llm-call/notebook.ipynb
- `Parked: privacy preservation LLM judge (binary)` --semantically_similar_to--> `other_customer_details()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/05-a-grader-you-can-trust/later.md → lab/evals.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Release gate metrics from acme_metrics and thresholds.yml** — 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_evaluation_report_metric_expert_pass_rate, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_evaluation_report_metric_routing_accuracy, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_evaluation_report_metric_missed_escalation, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_evaluation_report_metric_unsafe_auto_send, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_readme_release_gates_thresholds [EXTRACTED 1.00]
- **Round 1 failure modes and their fixes** — 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_mode1_amount_check_false_positive, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_mode2_model_over_escalation, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_mode3_unapproved_retention_offer, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_measurement_framework, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_fix_order [EXTRACTED 1.00]
- **Acme concession taxonomy and the ₹500 limit** — concept_concession, concept_refund_term, concept_credit_term, concept_discount_term, concept_double_payment_refund, concept_outage_credit, concept_retention_offer, concept_late_fee_waiver, concept_refund_limit_500 [EXTRACTED 1.00]
- **ADR-001 reply pipeline** — 1_measure_before_you_believe_11_recommendation_first_draft_diagram_load_customer_card, concept_safety_router, 1_measure_before_you_believe_11_recommendation_first_draft_diagram_search_help_articles, lab_version_b_version_b, concept_policy_verifier, concept_shadow_mode [EXTRACTED 1.00]
- **ADR-001 falsification triggers** — 1_measure_before_you_believe_11_recommendation_first_draft_decision_change_mind_router_misses, 1_measure_before_you_believe_11_recommendation_first_draft_decision_change_mind_c_stronger_model, 1_measure_before_you_believe_11_recommendation_first_draft_decision_change_mind_searched_context, 1_measure_before_you_believe_11_recommendation_first_draft_decision_recommendation [EXTRACTED 1.00]
- **Business Graph Engine runtime: concept linker → entitlements → decision envelope → guard, prompt, grader** — lab_ontology_extract_concepts, lab_ontology_compute_entitlements, lab_version_c3_build_decision_envelope, 1_measure_before_you_believe_08_agent_loop_from_scratch_business_graph_engine_plan_amount_guard, lab_version_c3_version_c3, lab_evals_policy_violations [EXTRACTED 1.00]
- **What must match between the chat and embedding models** — 1_measure_before_you_believe_06_one_llm_call_day6_embedding_compatibility_same_embedding_model, 1_measure_before_you_believe_06_one_llm_call_day6_embedding_compatibility_same_input_format, 1_measure_before_you_believe_06_one_llm_call_day6_embedding_compatibility_both_handle_hinglish, 1_measure_before_you_believe_06_one_llm_call_day6_embedding_compatibility_fits_context_limit, 1_measure_before_you_believe_06_one_llm_call_day6_embedding_compatibility_fit_in_memory [EXTRACTED 1.00]
- **Day 10 OODA error-analysis loop** — 1_measure_before_you_believe_10_read_the_failures_day10_read_the_failures_observe, 1_measure_before_you_believe_10_read_the_failures_day10_read_the_failures_orient, 1_measure_before_you_believe_10_read_the_failures_day10_read_the_failures_decide, 1_measure_before_you_believe_10_read_the_failures_day10_read_the_failures_act, 1_measure_before_you_believe_10_read_the_failures_readme_ooda_loop [EXTRACTED 1.00]
- **Recommended workflow: email in → card → router → search → B draft → policy check → shadow approval → reply out** — 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_email_in, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_load_customer_card_outages, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_router_needs_human, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_search_help_articles, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_draft_reply_b, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_policy_check, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_human_approves_draft, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_reply_out, 1_measure_before_you_believe_11_recommendation_first_draft_day11_adr_human_queue [EXTRACTED 1.00]
- **Grading the grader: three bugs fixed and locked in by regression tests** — 1_measure_before_you_believe_05_a_grader_you_can_trust_notebook_otp_safety_advice_false_alarm, 1_measure_before_you_believe_05_a_grader_you_can_trust_notebook_kb_times_as_fix_promises, 1_measure_before_you_believe_05_a_grader_you_can_trust_notebook_cross_sentence_refund, 1_measure_before_you_believe_05_a_grader_you_can_trust_notebook_grader_regression_tests, lab_evals_policy_violations [EXTRACTED 1.00]
- **score(): four yes/no checks that must all pass** — lab_evals_score, 1_measure_before_you_believe_05_a_grader_you_can_trust_day5_grader_explained_intent_ok, 1_measure_before_you_believe_05_a_grader_you_can_trust_day5_grader_explained_facts_ok, 1_measure_before_you_believe_05_a_grader_you_can_trust_day5_grader_explained_policy_ok, 1_measure_before_you_believe_05_a_grader_you_can_trust_day5_grader_explained_human_ok, 1_measure_before_you_believe_05_a_grader_you_can_trust_day5_grader_explained_passed [EXTRACTED 1.00]
- **Version C agent loop cycle (model call, tool dispatch, result back, stop or step limit)** — lab_llm_chat, 1_measure_before_you_believe_08_agent_loop_from_scratch_agent_loop_tool_dispatch, 1_measure_before_you_believe_08_agent_loop_from_scratch_agent_loop_tool_result_message, 1_measure_before_you_believe_08_agent_loop_from_scratch_agent_loop_stop_condition, 1_measure_before_you_believe_08_agent_loop_from_scratch_notebook_max_steps, 1_measure_before_you_believe_08_agent_loop_from_scratch_agent_loop_final_answer, lab_agent_run_agent [EXTRACTED 1.00]
- **What drives the cost of one resolved email** — 1_measure_before_you_believe_09_success_cost_latency_day9_success_cost_latency_cost_per_resolved_email, 1_measure_before_you_believe_09_success_cost_latency_day9_success_cost_latency_measured_cost_drivers, 1_measure_before_you_believe_09_success_cost_latency_day9_success_cost_latency_hidden_cost_drivers, 1_measure_before_you_believe_09_success_cost_latency_day9_success_cost_latency_per_email_costs_beyond_tokens, 1_measure_before_you_believe_09_success_cost_latency_day9_success_cost_latency_fixed_monthly_costs [EXTRACTED 1.00]
- **Seven stages of AI evaluation evolution** — 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage1_traditional_testing, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage2_early_ml_eval, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage3_foundation_model_eval, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage4_statistical_eval, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage5_system_level_eval, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage6_agentic_eval, 1_measure_before_you_believe_07_error_bars_day7_evolution_of_ai_evals_stage7_continuous_production_eval [EXTRACTED 1.00]
- **@known_gap scenario groups run as strict xfail** — concept_known_gap_xfail, tests_features_policy_rules_known_gaps, tests_features_policy_rules_known_gaps_restated_request, tests_features_policy_rules_known_gaps_concession, tests_features_grader_mutations_known_gaps [EXTRACTED 1.00]
- **Project 1 · Measure before you believe: the 12 days** — concept_measure_before_you_believe, fde_day_01, fde_day_02, fde_day_03, fde_day_04, fde_day_05, fde_day_06, fde_day_07, fde_day_08, fde_day_09, fde_day_10, fde_day_11, fde_day_12 [EXTRACTED 1.00]
- **Five discoveries that turn an agent into a workflow** — 1_measure_before_you_believe_02_workflow_or_agent_acme_fiber_storyboard_pivot_remove_ai_classification, 1_measure_before_you_believe_02_workflow_or_agent_acme_fiber_storyboard_pivot_fact_retrieval, 1_measure_before_you_believe_02_workflow_or_agent_acme_fiber_storyboard_pivot_verified_sources, 1_measure_before_you_believe_02_workflow_or_agent_acme_fiber_storyboard_pivot_guardrails, 1_measure_before_you_believe_02_workflow_or_agent_acme_fiber_storyboard_pivot_measure_before_committing [EXTRACTED 1.00]
- **Everything Version B feeds the model in one call** — 1_measure_before_you_believe_06_one_llm_call_notebook_system_prompt, 1_measure_before_you_believe_06_one_llm_call_notebook_customer_card_context, 1_measure_before_you_believe_06_one_llm_call_notebook_kb_article_context, 1_measure_before_you_believe_06_one_llm_call_notebook_answer_schema, lab_version_b_version_b, lab_llm_chat [EXTRACTED 1.00]
- **Expert review → policy and tests feedback loop** — 1_measure_before_you_believe_03_test_set_first_acme_review_studio_readme_critique_shadowing_loop, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_readme_review_page, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_readme_eval_workbook, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_label_corrections, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_reports_round1_principal_engineer_review_fix_order, concept_domain_expert_review, 1_measure_before_you_believe_03_test_set_first_acme_review_studio_readme_report_metrics_feature [INFERRED 0.85]
- **needs_human escalation triggers** — concept_needs_human_escalation, data_acme_policy_rule_06, data_acme_policy_rule_09, data_acme_policy_rule_11, acme_kb15, acme_kb16, lab_escalation_escalation_triggers [INFERRED 0.85]
- **₹500 money limit across policy, KB and grader** — concept_refund_limit_500, data_acme_policy_rule_03, data_acme_policy_rule_08, data_acme_policy_rule_13, acme_kb04, acme_kb16, lab_evals_reveals_limit, lab_escalation_amounts_asked_for [INFERRED 0.85]
- **ADR-001 options: chosen guarded B vs rejected A, plain B and C** — 1_measure_before_you_believe_11_recommendation_first_draft_decision_recommendation, 1_measure_before_you_believe_11_recommendation_first_draft_decision_rejected_option_a_rules, 1_measure_before_you_believe_11_recommendation_first_draft_decision_rejected_plain_b, 1_measure_before_you_believe_11_recommendation_first_draft_decision_rejected_option_c_agent [INFERRED 0.85]
- **Version C3 escalation sources (rule, guard, offer, model)** — lab_escalation_escalation_triggers, lab_version_c3_offers_not_allowed, lab_evals_not_english, lab_version_c3_run_agent, tests_features_escalation_rules_every_escalation_records_source [INFERRED 0.85]

## Communities (105 total, 27 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.18
Nodes (12): _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key(), _load() (+4 more)

### Community 1 - "Version"
Cohesion: 0.16
Nodes (8): OrchestratedAdapter, RecordedProvider, pin_status(), version_heading(), manifest_diff(), Version, sim_version_banner(), test_banner_counts_current_pins_and_names_the_bound_component()

### Community 2 - "ontology.py"
Cohesion: 0.11
Nodes (24): KnowledgeArticle and PolicyRule IRIs (documentedIn, enforcesRule), Concept → KB retrieval gain (with alias leakage caveat), Multilingual lexical layer (SKOS labels), acme:Plan catalog (Basic ₹699, Plus ₹999, Pro ₹1,499), KB02 · Late payment fee, outage_for(), _alias_index(), _asserted_store() (+16 more)

### Community 3 - "RunResult"
Cohesion: 0.27
Nodes (3): _json(), _now(), RunStore

### Community 4 - "test_escalation_metrics.py"
Cohesion: 0.17
Nodes (15): Safety scoreboard (safe, missed escalations, human intervention, passed), summary(), Feature: Escalation is reported as recall and precision, not just human_ok, Scenario Outline: The grader summary reports escalation recall and precision, bot_escalates(), cases(), _graded(), human_ok_is() (+7 more)

### Community 5 - "version_choices"
Cohesion: 0.12
Nodes (11): case_choices(), review_page(), score_page(), _refresh_case_choices(), score_boxes(), _settings(), simulator_page(), version_choices() (+3 more)

### Community 6 - "version_d.py"
Cohesion: 0.05
Nodes (46): conversation(), customer_text(), kb_by_id(), load_customers(), lookup_customer(), amounts_asked_for(), percent_asks_in_rupees(), other_customer_details() (+38 more)

### Community 7 - "compute_entitlements"
Cohesion: 0.06
Nodes (36): Examples from the expert's review (worst fails, what good looks like), Business Graph Engine (graph computes, LLM verbalizes), Ephemeral per-case ABox (one customer), Static TBox (shared meaning, zero PII), Meaning flow: policy.md + kb.md → ontology.ttl → pyoxigraph → glossary(), pyoxigraph (in-process RDF store, SPARQL 1.1), Varun's ₹300 credit: three agents, three meanings, data/acme/ontology.ttl (+28 more)

### Community 8 - "Review Studio server"
Cohesion: 0.05
Nodes (44): default_sim_step(), server(), _apply_retention(), batch_rev(), batch_status(), case_editor(), case_list(), _ed_save() (+36 more)

### Community 9 - "Day 09 notebook (success-cost-latency)"
Cohesion: 0.32
Nodes (5): Day 09 notebook (success-cost-latency), cost_inr(), percentile(), row(), run_agent()

### Community 10 - "test_c3_provider.py"
Cohesion: 0.10
Nodes (20): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+12 more)

### Community 11 - "version_c3"
Cohesion: 0.13
Nodes (15): unasked_outage(), Scenario Outline: The expert's verdict and the grader's agree, Scenario Outline: The envelope shows the outage only when the customer reports one, Feature: The area outage is in scope only when the customer reports that their service is down, Scenario: The customer-record tools show the outage when the customer reports one, Scenario Outline: A reply mentions the area outage only when the customer reported one, grader_scores(), agent_finishes() (+7 more)

### Community 12 - "test_policy_rules.py"
Cohesion: 0.05
Nodes (51): Day 05 notebook (a-grader-you-can-trust), Failure category: unapproved offer, Failure category: unsupported-amount false positive, KB03 · Payment methods, KB04 · Refunds and credits, KB05 · Outages and restoration updates, KB06 · Outage credit, KB11 · Retention offer (+43 more)

### Community 13 - "test_escalation_rules.py"
Cohesion: 0.15
Nodes (16): Scenario: An amount the agent wrote in an earlier turn is not the customer's ask, Scenario: No rule fires on any case the experts labelled "no human needed", agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes(), envelope_decides(), every_labelled_case() (+8 more)

### Community 14 - "direct.py"
Cohesion: 0.11
Nodes (5): direct_output(), DirectAdapter, VersionBAdapter, DeclarativeAdapter, endpoint_origin()

### Community 15 - "render.py"
Cohesion: 0.22
Nodes (16): _allows(), _button(), _children(), _exchange(), _exchange_view(), _has_turns(), render_grade(), _text() (+8 more)

### Community 16 - "test_review_flow.py"
Cohesion: 0.13
Nodes (17): initial_mode(), suggest_mode(), validate_verdict(), _prefill(), check_fired(), ctx(), fail_no_critique(), fail_no_mode() (+9 more)

### Community 17 - "import_cases.py"
Cohesion: 0.24
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 18 - "RunResult"
Cohesion: 0.24
Nodes (19): render_comparison(), render_detail(), render_result(), _span_tree_view(), _step_graph_view(), Capabilities, RunResult, Topology (+11 more)

### Community 19 - "Day 9 · Run all three: success, cost, latency"
Cohesion: 0.09
Nodes (33): classify(), version_a(), Seeing Theory: basic probability and frequentist inference, Today: passive prompt glossary (LLM does the joins), Phase 4 · Empirical verdict, Cost levers (check each against the pass rate), ₹ per resolved email (what really drives cost), Fixed monthly costs spread over all emails (+25 more)

### Community 20 - "Studio evidence frame"
Cohesion: 0.25
Nodes (3): Evidence, mask(), nonempty()

### Community 21 - "RunResult"
Cohesion: 0.11
Nodes (20): SimulationService, RunInput, sim_pipe(), sim_step_detail(), sim_version_status(), run_case(), test_adapter_errors_and_timeouts_are_saved(), test_c3_concurrent_versions_read_their_own_lab_snapshots() (+12 more)

### Community 22 - "Review dashboard (when do humans help?)"
Cohesion: 0.20
Nodes (8): Error cost (INR, per 1,000 emails), Agent hours per 1,000 emails, Escalation rate, costs_inr, missed_escalation, unneeded_escalation, unsafe_auto_send, review_minutes_per_case

### Community 23 - "test_simulator_feature.py"
Cohesion: 0.16
Nodes (19): read(), read_round(), approve(), batch_offline(), batch_started(), c3_version(), finished_on(), _freeze() (+11 more)

### Community 24 - "test_adapter_contract.py"
Cohesion: 0.12
Nodes (7): AppSettings, Settings, pinned(), scripted_adapter(), valid_contract(), world(), world()

### Community 25 - "Build a workflow, not an agent: B + safety router + policy verifier"
Cohesion: 0.16
Nodes (14): Day 11 ADR-001 diagram, Open question: which failures come from model size vs prompt or grader? (P4, P5), ADR-001: How Acme Fibre should answer customer emails, Open question: how good is searched context for B? (project 2), ADR self-check, 5-minute CTO readout (pitch script), ADR-001 executive readout (9 slides), Documenting Architecture Decisions (Michael Nygard) (+6 more)

### Community 26 - "acme_metrics.py"
Cohesion: 0.12
Nodes (9): banner(), html_table(), provenance_table(), sha256(), tiles(), workbook_sheet(), Dataset card (Acme test set), Reports overview page (index.qmd) (+1 more)

### Community 27 - "test_report_metrics.py"
Cohesion: 0.16
Nodes (16): cases_run(), demo(), escalated(), escalated_by_code(), no_gate(), nothing(), routing(), save() (+8 more)

### Community 28 - "app.py"
Cohesion: 0.09
Nodes (18): _bool(), export_to_excel(), _history(), _item(), load_lab(), _payments(), _put(), read_review_log() (+10 more)

### Community 29 - "FDE First Principles learning log"
Cohesion: 0.12
Nodes (20): Day 01 notebook (an-llm-call-is-http), ask(), Deep Dive into LLMs like ChatGPT (Karpathy), inference chapter, Ollama /api/chat endpoint, qwen3:4b local model, draft_cases(), Per-step agent trace, Forward Deployed Engineer (FDE) mindset (+12 more)

### Community 31 - "test_version_d.py"
Cohesion: 0.06
Nodes (33): canonical_offer(), fill_offers(), route(), thread_of(), ThreadStore, version_d(), watchdog(), customer_writes() (+25 more)

### Community 32 - "acme_tools.py"
Cohesion: 0.14
Nodes (13): Tool dispatch FUNCTIONS[name](**args), Tool result appended as a 'tool' message, Day 08 notebook (agent-loop-from-scratch), run_agent(), show(), KB01 · Billing cycle and due dates, KB16 · Talking to a human, Acme help articles (kb.md) (+5 more)

### Community 33 - "business_rules.py"
Cohesion: 0.14
Nodes (9): Phase 1 · Rich TBox schema, Phase 2 · Graph engine core, Phase 3 · Wire grader and router, _deep_update(), _default_rules(), months_since(), outage_exceeds_hours(), _parse_date() (+1 more)

### Community 34 - "load_cases"
Cohesion: 0.17
Nodes (9): intent_guide(), Scenario Outline: The guide's edge cases match the expert labels, Scenario: Every intent has a definition, Feature: One written convention decides the intent label, Scenario Outline (@known_gap): Labels that disagree with the guide, case_is_labelled(), every_intent_defined(), labelled_cases() (+1 more)

### Community 35 - "ADR-001 diagram: B with a safety router and a policy check"
Cohesion: 0.15
Nodes (10): Proposed controlled workflow (deterministic routing + one drafting step), Five discoveries, five architecture pivots, Building effective agents (Anthropic), Email-to-reply decision map, Workflow patterns: prompt chaining, routing, agent, ADR-001 diagram: B with a safety router and a policy check, Human support queue, Search the help articles (retrieved, not oracle context) (+2 more)

### Community 36 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout() (+4 more)

### Community 37 - "test_grader_mutations.py"
Cohesion: 0.08
Nodes (30): Mutation testing of the grader, Feature: The grader agrees with the expert's round-2 review, Scenario Outline: The retention offer is pre-approved (c44), Scenario Outline: The grader catches a reply that was broken on purpose, Feature: Mutation tests for the grader, Scenario Outline: The grader ignores changes that keep the reply correct, @known_gap Scenario Outline: Known gaps: correct replies the grader still fails, a_draft_handed_off() (+22 more)

### Community 38 - "Day 8: agent loop and failures"
Cohesion: 0.10
Nodes (22): Final answer JSON {intent, reply, needs_human}, Gave-up fallback at MAX_STEPS, Stop condition: reply has no tool_calls, MAX_STEPS = 6 step limit, issue_refund tool (data-changing, deferred), qwen3:4b local model (temperature 0), Act: does it hold on emails we never looked at?, Decide: which single fix matters most? (+14 more)

### Community 39 - "acme.py"
Cohesion: 0.09
Nodes (17): Day 04 notebook (rules-baseline), Day 07 notebook (error-bars), Day 10 notebook (read-the-failures), passed(), scoreboard(), show(), Load customer card and outages (code, no model), Day 11 notebook (recommendation-first-draft) (+9 more)

### Community 42 - "version_b"
Cohesion: 0.15
Nodes (12): What the model sees (Version B context), Scoreboard on 84 cases: A vs B, Version A pipeline: keyword match then fill a template, Customer card context (name, area, plan), KB article context (INTENT_KB by expected intent), Building block: the augmented LLM (Anthropic, Building effective agents), A statistical approach to model evaluations (Anthropic), Context engineering (the context is the product) (+4 more)

### Community 43 - "service.py"
Cohesion: 0.07
Nodes (12): guard_hits(), Lab, no_draft(), validate_draft(), redact(), RedactingSerializer, secret_values(), compare_results() (+4 more)

### Community 44 - "load_cases"
Cohesion: 0.13
Nodes (18): Run provenance (.meta.json: model, prompt fingerprint, settings), data_root(), fingerprint(), git_commit(), load_cases(), save_results(), kb_only(), main() (+10 more)

### Community 45 - "acme_metrics.py"
Cohesion: 0.16
Nodes (4): eval_checks(), build_frame(), fig_html(), layer_of()

### Community 46 - "Evaluation report (release decision)"
Cohesion: 0.17
Nodes (15): Evaluation report (release decision), Step-6 check hits, Expert pass rate, Missed escalation, Routing accuracy, Unneeded escalation, Unsafe auto-send, Where every case went (run → escalated/sent → right/missed/unneeded) (+7 more)

### Community 50 - "test_gate_draft.py"
Cohesion: 0.14
Nodes (10): check_draft(), asked_for_money(), draft_check_reports(), model_drafts(), _reply(), test_an_unrepairable_draft_escalates(), fake_chat(), test_the_gate_repairs_a_granting_draft() (+2 more)

### Community 51 - "then"
Cohesion: 0.11
Nodes (25): banner(), layer_fired(), no_step_4_prompt(), Scenario: OWL reasoner inherits class properties and respects overrides, check_business_rule_cooldown(), check_inherited_props(), check_inherited_role(), check_override_false() (+17 more)

### Community 52 - "Rate"
Cohesion: 0.25
Nodes (3): Rate, wilson(), Model needs-human flag recall

### Community 54 - "_sim_run"
Cohesion: 0.19
Nodes (13): make_provider(), case_of(), provider_status(), replay_sources(), selected_sim_version(), _sim_case(), sim_fields(), sim_history_controls() (+5 more)

### Community 55 - "run_agent"
Cohesion: 0.39
Nodes (7): run_agent(), _call(), _draft_only(), _gate(), _parse(), _repair(), system_prompt_d()

### Community 56 - "Dataset card (Acme test set)"
Cohesion: 0.18
Nodes (3): tests/features/report_metrics.feature, load_thresholds(), Evaluation evidence Quarto site

### Community 57 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 58 - "ReviewStore"
Cohesion: 0.16
Nodes (9): ReviewStore, _export(), score_rounds(), load(), test_dataset_banner_omits_run_progress_but_keeps_warnings(), test_provenance_uses_full_hashes_and_escapes_values(), test_reports_select_versions_and_keep_the_round_alias(), test_legacy_reviews_migrate_and_round_trip_through_excel() (+1 more)

### Community 60 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 61 - "Safety router"
Cohesion: 0.11
Nodes (23): acme:AccountAction requiresRole AccountHolder, Amount guard (C3 only, not yet a router), acme:EscalationTrigger (planned), acme:PuneServiceArea (8 areas), Failure category: missed escalation, Open question: can a learned classifier route escalations better? (project 3), KB10 · Cancellation and notice period, KB12 · Shifting your connection (+15 more)

### Community 63 - "test_holdout_run.py"
Cohesion: 0.26
Nodes (6): use_data_root(), _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 68 - "C3Provider"
Cohesion: 0.13
Nodes (7): ClaudeCodeProvider, OfflineProvider, _parse_json_text(), _result(), to_record(), demo_verdict(), main()

### Community 69 - "versions.py"
Cohesion: 0.14
Nodes (9): canonical(), case_hash(), digest(), lab_snapshot(), label_hash(), _sheet_hashes(), VersionRegistry, Version lifecycle, drift and audit (+1 more)

### Community 70 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 71 - "Stage 4 · Statistical evaluation: 'How sure are we?'"
Cohesion: 0.14
Nodes (9): Critique Shadowing workflow, Stage 1 · Traditional software testing: 'Is it correct?', Stage 2 · Early machine learning evaluation: 'How accurate is it?', Stage 3 · Foundation model evaluation: 'Is it good, safe, and grounded?', Stage 4 · Statistical evaluation: 'How sure are we?', Stage 5 · System-level evaluation: 'Does the whole system work?', Stage 6 · Agentic AI evaluation: 'Does the agent finish the job?', Stage 7 · Continuous production evaluation: 'Is it still working for users?' (+1 more)

### Community 72 - "studio-offline.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 73 - "version-b.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 74 - "test_ontology.py"
Cohesion: 0.08
Nodes (41): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), load_business_rules(), concept_labels(), concept_provenance(), define(), glossary() (+33 more)

### Community 75 - "test_guardrails.py"
Cohesion: 0.07
Nodes (31): amounts(), claim_checks(), _flag(), _trace(), user_prompt(), Workflow, check(), decide() (+23 more)

### Community 77 - "eval_checks"
Cohesion: 0.13
Nodes (17): chip(), highlight(), icon(), customer_chips(), case_header(), cur(), draft_meta(), email_card() (+9 more)

### Community 79 - "offline-direct.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 80 - "Load customer card and outages"
Cohesion: 0.24
Nodes (9): One model call (B) drafts the reply, Email in, Human approves the draft (shadow mode until the gates hold), Human queue (a person writes the reply), Load customer card and outages, Policy check (grader rules, in code), Reply out, Router: needs a human? (rules + 1 model call) (+1 more)

### Community 81 - "Acme labelled test set (cases.jsonl)"
Cohesion: 0.09
Nodes (30): Acme Review Studio, import_cases.py (lab data → workbook), runs/ versioned persistence, Round 1 Principal Engineer review of the Acme Fibre email drafting solution, Safe-send capture rate (new north-star metric), Day 03 notebook (test-set-first), Seven intents, problems() (+22 more)

### Community 83 - "Embedding model rubric (why embeddinggemma)"
Cohesion: 0.24
Nodes (6): qwen3:4b chat model (reads text only), Similarity search (cosine, top 3), embeddinggemma (EMBED_MODEL), Embeddings and retrieval, Hinglish handling, Recall@3 (retrieval metric)

### Community 84 - "C3Provider"
Cohesion: 0.21
Nodes (3): c3_output(), C3Provider, AgentLoopAdapter

### Community 86 - "test_cases_data.py"
Cohesion: 0.18
Nodes (8): load_outages(), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 87 - "pytest"
Cohesion: 0.15
Nodes (9): meaning_card(), fact_rows(), origin(), pipeline(), Elements, test_icons_have_no_network_or_accessible_name(), test_meaning_card_shows_provenance_sources_and_clickable_rules(), test_pipeline_keyboard_order_and_untrusted_details() (+1 more)

### Community 89 - "Review dashboard (when do humans help?)"
Cohesion: 0.22
Nodes (7): Code saves, Disagreement rates, What triggered the escalations (layer analysis), Failure categories (expert), Review dashboard (when do humans help?), Routing by escalation rule, code_saves()

### Community 91 - "Day 06 notebook (one-llm-call)"
Cohesion: 0.47
Nodes (5): Day 06 notebook (one-llm-call), evaluate(), unit(), user_message(), version_b()

### Community 92 - "app.py"
Cohesion: 0.16
Nodes (13): compare_reviews(), review_record(), sample_spread(), run_case(), _run_missing(), worker(), one(), _run_one() (+5 more)

### Community 95 - "fixture"
Cohesion: 0.40
Nodes (4): runs(), semantic_data(), world(), world()

### Community 96 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 99 - "rescore.py"
Cohesion: 0.50
Nodes (6): _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before()

### Community 104 - "Failure analysis"
Cohesion: 0.12
Nodes (12): Build LLM judge from expert examples, Error analysis: error rates, patterns, specialised judges, Expert reviews data and errors are fixed, Repeat on material change or periodic review, Principal domain expert, Phase 0 · Baseline audit, Version B + glossary experiment (B_glossary), term_misread failure tag (+4 more)

## Ambiguous Edges - Review These
- `version_b()` → `Failure category: unsupported-amount false positive`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `search_kb()` → `Similarity search (cosine, top 3)`  [AMBIGUOUS]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio · relation: semantically_similar_to
- `run_agent()` → `Failure category: unapproved offer`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `Open question: which failures come from model size vs prompt or grader? (P4, P5)` → `ADR-001: How Acme Fibre should answer customer emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/day11-adr.drawio · relation: conceptually_related_to
- `ADR-001: How Acme Fibre should answer customer emails` → `Pitch claim: drafts cut handle time 40-60% in Phase 1`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Cost is not the issue (B ≈ ₹1.60/day, C ≈ ₹10/day)` → `Pitch claim: agent fails unit economics`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Pitch claim: deterministic workflow topology with hard guarantees`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Author's unease: instinct favours C`  [AMBIGUOUS]
  1-measure-before-you-believe/12-article/article.md · relation: conceptually_related_to
- `Pitch claim: drafts cut handle time 40-60% in Phase 1` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: Option A missed 40 of 40 (0% safety)`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: router adds under 500 ms and ₹0.10 per 1,000 emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Open question: can a learned classifier route escalations better? (project 3)` → `Roadmap claim: transformer classifier drops router latency from 500 ms to under 20 ms`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to

## Knowledge Gaps
- **31 isolated node(s):** `fde-first-principles`, `KB03 · Payment methods`, `KB13 · Router and Wi-Fi password`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 511 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `server()` connect `Review Studio server` to `Version`, `versions.py`, `version_choices`, `version_d.py`, `Failure analysis`, `test_ontology.py`, `service.py`, `acme_metrics.py`, `eval_checks`, `render.py`, `test_review_flow.py`, `app.py`, `RunResult`, `RunResult`, `_sim_run`, `pytest`, `ReviewStore`, `app.py`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles`, `KB03 · Payment methods`, `KB13 · Router and Wi-Fi password` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ontology.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10953058321479374 - nodes in this community are weakly interconnected._
- **Why does `policy_violations()` connect `test_policy_rules.py` to `ontology.py`, `version_d.py`, `compute_entitlements`, `version_c3`, `Day 9 · Run all three: success, cost, latency`, `RunResult`, `test_simulator_feature.py`, `Build a workflow, not an agent: B + safety router + policy verifier`, `test_version_d.py`, `business_rules.py`, `test_grader_mutations.py`, `acme.py`, `service.py`, `run_agent`, `test_ontology.py`, `test_guardrails.py`, `Load customer card and outages`, `Acme labelled test set (cases.jsonl)`, `Failure analysis`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `version_b()` and `Failure category: unsupported-amount false positive`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `search_kb()` and `Similarity search (cosine, top 3)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._