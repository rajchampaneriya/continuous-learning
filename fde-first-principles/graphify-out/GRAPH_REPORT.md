# Graph Report - fde-first-principles  (2026-11-14)

## Corpus Check
- 85 files · ~84,882 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 61 file(s) not represented in the graph (top: .feature 15, .jsonl 14, .drawio 12)
- WARNING: 61 of 180 files seen (34%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 1890 nodes · 5357 edges · 107 communities (87 shown, 20 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 896 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ecdf2131`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- Version
- test_ontology.py
- Domain expert (SME) review
- test_escalation_metrics.py
- app.py
- version_c3.py
- compute_entitlements
- Review Studio server
- summary
- test_c3_provider.py
- version_c3
- test_policy_rules.py
- test_escalation_rules.py
- test_report_metrics.py
- refresh_versions
- test_review_flow.py
- import_cases.py
- Capabilities
- Day 9 · Run all three: success, cost, latency
- Studio evidence frame
- RunResult
- Review dashboard (when do humans help?)
- RunStore
- test_guardrails.py
- Build a workflow, not an agent: B + safety router + policy verifier
- acme_metrics.py
- Rule 8 · ₹500 limit is per customer over 30 days
- lab.py
- Day 1 · One model call: tokens, time and randomness
- test_adapter_contract.py
- test_version_d.py
- acme.py
- load_business_rules
- load_cases
- Acme Fibre (fictional Pune broadband ISP)
- test_simulator_http.py
- Grader mutation tests
- Day 8: agent loop and failures
- suggest_mode
- Day 7 · Why 30 test cases can lie: error bars
- version_b
- service.py
- load_cases
- Acme labelled test set (cases.jsonl)
- Evaluation report (release decision)
- RedactingSerializer
- then
- Rate
- Day 06 notebook (one-llm-call)
- test_expert_review.py
- workflow.py
- Dataset card (Acme test set)
- studio-c3.yaml
- ReviewStore
- policy_violations
- config
- Safety router
- KB slow speed and technician
- KB new installation
- KB search queries
- Project config
- C3Provider
- versions.py
- c3-agent.yaml
- judge_round1.py
- studio-offline.yaml
- version-b.yaml
- eval_checks
- embed
- offline-direct.yaml
- Load customer card and outages
- Step 6 · check claims and facts
- Expert reviews data and errors are fixed
- Day 09 notebook (success-cost-latency)
- Version parameter and legacy round alias
- _sim_run
- test_cases_data.py
- pytest
- Evaluation evidence Quarto site
- Adapter
- score
- test_simulator_persistence.py
- review_record
- common.py
- studio-declarative.yaml
- define_term
- scored
- when
- Scenario: OWL reasoner inherits class properties and respects overrides
- _script
- ScriptedModel
- costs_inr
- fixture
- Day 08 notebook (agent-loop-from-scratch)

## God Nodes (most connected - your core abstractions)
1. `server()` - 129 edges
2. `policy_violations()` - 63 edges
3. `Version` - 61 edges
4. `score()` - 58 edges
5. `RunInput` - 50 edges
6. `RunResult` - 46 edges
7. `VersionRegistry` - 42 edges
8. `build_decision_envelope()` - 39 edges
9. `SimulationService` - 36 edges
10. `compute_entitlements()` - 35 edges

## Surprising Connections (you probably didn't know these)
- `Similarity search (cosine, top 3)` --semantically_similar_to--> `search_kb()`  [AMBIGUOUS] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio → lab/acme_tools.py
- `run_agent()` --semantically_similar_to--> `run_agent()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/08-agent-loop-from-scratch/notebook.ipynb → lab/version_c3.py
- `version_b()` --semantically_similar_to--> `version_b()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/notebook.ipynb → lab/version_b.py
- `ask()` --semantically_similar_to--> `chat()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/01-an-llm-call-is-http/notebook.ipynb → lab/llm.py
- `run_agent()` --semantically_similar_to--> `run_agent()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/08-agent-loop-from-scratch/notebook.ipynb → lab/agent.py

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

## Communities (107 total, 20 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.19
Nodes (12): Tool result appended as a 'tool' message, _cache_file(), chat(), _chat_anthropic(), _chat_api(), _env(), _key(), _load() (+4 more)

### Community 1 - "Version"
Cohesion: 0.11
Nodes (8): OfflineProvider, DirectAdapter, VersionBAdapter, OrchestratedAdapter, RecordedProvider, manifest_diff(), Version, Deps

### Community 2 - "test_ontology.py"
Cohesion: 0.07
Nodes (44): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), KnowledgeArticle and PolicyRule IRIs (documentedIn, enforcesRule), _alias_index(), _asserted_store(), _bool_value(), concept_labels() (+36 more)

### Community 3 - "Domain expert (SME) review"
Cohesion: 0.17
Nodes (14): Examples from the expert's review (worst fails, what good looks like), draft_cases(), Engine audits the test set: c44 vs r20/p06a, Domain expert (SME) review, Acme Fibre reply policy (policy.md), cases_multiturn.jsonl (40 conversations), outages.json (current outages by area), unasked_outage() (+6 more)

### Community 4 - "test_escalation_metrics.py"
Cohesion: 0.23
Nodes (12): Scenario Outline: The grader summary reports escalation recall and precision, bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is() (+4 more)

### Community 5 - "app.py"
Cohesion: 0.15
Nodes (8): highlight(), pipeline(), case_choices(), score_page(), _refresh_case_choices(), simulator_page(), version_choices(), Simulator page

### Community 6 - "version_c3.py"
Cohesion: 0.07
Nodes (33): run_agent(), conversation(), customer_text(), intent_guide(), amounts_asked_for(), extract_json(), build_decision_envelope(), _envelope_brief() (+25 more)

### Community 7 - "compute_entitlements"
Cohesion: 0.08
Nodes (28): Ephemeral per-case ABox (one customer), Static TBox (shared meaning, zero PII), Varun's ₹300 credit: three agents, three meanings, data/acme/ontology.ttl, data/acme/business_rules.json (commercial thresholds), Concession (refund, credit, waiver, discount value), Credit, Discount (also: सूट, छूट, ರಿಯಾಯಿತಿ) (+20 more)

### Community 8 - "Review Studio server"
Cohesion: 0.07
Nodes (19): server(), batch_rev(), batch_status(), case_editor(), _ed_save(), edit_case(), _export(), _keys() (+11 more)

### Community 9 - "summary"
Cohesion: 0.11
Nodes (15): Day 05 notebook (a-grader-you-can-trust), Day 10 notebook (read-the-failures), passed(), Run provenance (.meta.json: model, prompt fingerprint, settings), scoreboard(), show(), Safety scoreboard (safe, missed escalations, human intervention, passed), Day 11 notebook (recommendation-first-draft) (+7 more)

### Community 10 - "test_c3_provider.py"
Cohesion: 0.05
Nodes (34): ClaudeCodeProvider, make_provider(), _result(), _trace(), user_prompt(), Workflow, draft(), fetch() (+26 more)

### Community 11 - "version_c3"
Cohesion: 0.13
Nodes (13): version_c3(), Scenario Outline: The envelope shows the outage only when the customer reports one, Scenario: The customer-record tools show the outage when the customer reports one, Scenario: The customer-record tools withhold the outage when it is out of scope, test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes(), customer_writes(), envelope_is_built() (+5 more)

### Community 12 - "test_policy_rules.py"
Cohesion: 0.12
Nodes (18): @known_gap scenarios as strict xfail, other_customer_details(), Feature: The grader enforces the Acme Fibre reply policy, @known_gap Scenario Outline: Known gaps the grader does not handle yet, @known_gap Scenario Outline: Known gaps in the concession check, @known_gap Scenario Outline: Known gaps in the restated-request check, Scenario Outline: A reply must not give away another customer's details, Scenario Outline: An amount the customer asked for, restated in a hand-off, is not granted (+10 more)

### Community 13 - "test_escalation_rules.py"
Cohesion: 0.13
Nodes (20): Failure category: unapproved offer, Scenario: An amount the agent wrote in an earlier turn is not the customer's ask, Scenario: No rule fires on any case the experts labelled "no human needed", Scenario Outline: A draft that offers more than its decision allows goes to a person, agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes() (+12 more)

### Community 14 - "test_report_metrics.py"
Cohesion: 0.18
Nodes (14): banner(), demo(), escalated(), escalated_by_code(), layer_fired(), no_gate(), nothing(), save() (+6 more)

### Community 15 - "refresh_versions"
Cohesion: 0.17
Nodes (16): case_list(), _fail(), _keep_current_visible(), _name_candidate(), _pass(), _prefill_key(), progress(), refresh_versions() (+8 more)

### Community 16 - "test_review_flow.py"
Cohesion: 0.15
Nodes (14): validate_verdict(), check_fired(), ctx(), fail_no_critique(), fail_no_mode(), hint(), none_selected(), not_yet_grouped() (+6 more)

### Community 17 - "import_cases.py"
Cohesion: 0.22
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 18 - "Capabilities"
Cohesion: 0.12
Nodes (23): HttpAdapter, DeclarativeAdapter, _button(), render_comparison(), render_detail(), render_result(), _text(), _topology() (+15 more)

### Community 19 - "Day 9 · Run all three: success, cost, latency"
Cohesion: 0.16
Nodes (16): version_a(), Cost levers (check each against the pass rate), ₹ per resolved email (what really drives cost), Fixed monthly costs spread over all emails, Costs hidden inside today's estimate, Latency not counted (tool time, network, queues, cold start), Cost drivers measured in the notebook, Per-email costs beyond tokens (+8 more)

### Community 20 - "Studio evidence frame"
Cohesion: 0.22
Nodes (3): Evidence, mask(), nonempty()

### Community 21 - "RunResult"
Cohesion: 0.11
Nodes (20): SimulationService, RunInput, _apply_retention(), sim_pipe(), sim_step_detail(), sim_version_banner(), sim_version_status(), test_adapter_errors_and_timeouts_are_saved() (+12 more)

### Community 22 - "Review dashboard (when do humans help?)"
Cohesion: 0.20
Nodes (10): Code saves, Agent hours per 1,000 emails, Disagreement rates, What triggered the escalations (layer analysis), Escalation rate, Failure categories (expert), Review dashboard (when do humans help?), Routing by escalation rule (+2 more)

### Community 23 - "RunStore"
Cohesion: 0.27
Nodes (3): _json(), _now(), RunStore

### Community 24 - "test_guardrails.py"
Cohesion: 0.20
Nodes (10): email_from(), flags(), human_chooses(), model_drafts(), not_called(), outcome(), reason(), run() (+2 more)

### Community 25 - "Build a workflow, not an agent: B + safety router + policy verifier"
Cohesion: 0.11
Nodes (22): Day 11 ADR-001 diagram, Open question: which failures come from model size vs prompt or grader? (P4, P5), ADR-001: How Acme Fibre should answer customer emails, Day 10: C on hosted glm-5.3-flash, held-out, Open question: how good is searched context for B? (project 2), ADR-001 diagram: B with a safety router and a policy check, Human support queue, Gates before replies go out unreviewed (+14 more)

### Community 26 - "acme_metrics.py"
Cohesion: 0.13
Nodes (8): eval_checks(), label_hash(), to_record(), build_frame(), fig_html(), layer_of(), demo_verdict(), main()

### Community 27 - "Rule 8 · ₹500 limit is per customer over 30 days"
Cohesion: 0.15
Nodes (16): Round 1 Principal Engineer review of the Acme Fibre email drafting solution, Safe-send capture rate (new north-star metric), Concept → KB retrieval gain (with alias leakage caveat), Multilingual lexical layer (SKOS labels), KB02 · Late payment fee, KB04 · Refunds and credits, KB06 · Outage credit, KB11 · Retention offer (+8 more)

### Community 28 - "lab.py"
Cohesion: 0.14
Nodes (13): _bool(), export_to_excel(), _history(), _item(), load_lab(), _payments(), _put(), read_review_log() (+5 more)

### Community 29 - "Day 1 · One model call: tokens, time and randomness"
Cohesion: 0.13
Nodes (19): Day 01 notebook (an-llm-call-is-http), ask(), Deep Dive into LLMs like ChatGPT (Karpathy), inference chapter, Ollama /api/chat endpoint, qwen3:4b local model, Per-step agent trace, Forward Deployed Engineer (FDE) mindset, Local models on Ollama (zero cost) (+11 more)

### Community 30 - "test_adapter_contract.py"
Cohesion: 0.12
Nodes (6): pinned(), scripted_adapter(), ScriptedResponse, ScriptedSession, valid_contract(), world()

### Community 31 - "test_version_d.py"
Cohesion: 0.13
Nodes (19): claim_amounts(), fill_offers(), route(), thread_of(), ThreadStore, version_d(), watchdog(), case() (+11 more)

### Community 32 - "acme.py"
Cohesion: 0.10
Nodes (22): Customer card context (name, area, plan), Tool dispatch FUNCTIONS[name](**args), Load customer card and outages (code, no model), KB01 · Billing cycle and due dates, Acme help articles (kb.md), customer_card(), data_root(), first_name() (+14 more)

### Community 33 - "load_business_rules"
Cohesion: 0.36
Nodes (4): _deep_update(), _default_rules(), load_business_rules(), _rules_at()

### Community 34 - "load_cases"
Cohesion: 0.20
Nodes (4): Scenario: Every intent has a definition, every_intent_defined(), labelled_cases(), world()

### Community 35 - "Acme Fibre (fictional Pune broadband ISP)"
Cohesion: 0.10
Nodes (18): Proposed controlled workflow (deterministic routing + one drafting step), Five discoveries, five architecture pivots, Building effective agents (Anthropic), Email-to-reply decision map, Workflow patterns: prompt chaining, routing, agent, Business Graph Engine (graph computes, LLM verbalizes), Today: passive prompt glossary (LLM does the joins), acme:Plan catalog (Basic ₹699, Plus ₹999, Pro ₹1,499) (+10 more)

### Community 36 - "test_simulator_http.py"
Cohesion: 0.15
Nodes (11): Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout(), test_loopback_http_is_allowed_only_when_explicitly_allowlisted() (+3 more)

### Community 37 - "Grader mutation tests"
Cohesion: 0.12
Nodes (20): Mutation testing of the grader, Scenario Outline: The grader catches a reply that was broken on purpose, Feature: Mutation tests for the grader, Scenario Outline: The grader ignores changes that keep the reply correct, @known_gap Scenario Outline: Known gaps: correct replies the grader still fails, _add_each_banned(), _append(), _cases_where() (+12 more)

### Community 38 - "Day 8: agent loop and failures"
Cohesion: 0.13
Nodes (16): Final answer JSON {intent, reply, needs_human}, Gave-up fallback at MAX_STEPS, Stop condition: reply has no tool_calls, MAX_STEPS = 6 step limit, qwen3:4b local model (temperature 0), Act: does it hold on emails we never looked at?, Decide: which single fix matters most?, Observe: what does a pass rate hide? (+8 more)

### Community 39 - "suggest_mode"
Cohesion: 0.32
Nodes (5): initial_mode(), suggest_mode(), review_page(), _prefill(), Review page

### Community 40 - "Day 7 · Why 30 test cases can lie: error bars"
Cohesion: 0.12
Nodes (16): Stage 4 · Statistical evaluation: 'How sure are we?', Stage 5 · System-level evaluation: 'Does the whole system work?', Stage 6 · Agentic AI evaluation: 'Does the agent finish the job?', Stage 7 · Continuous production evaluation: 'Is it still working for users?', A statistical approach to model evaluations (Anthropic), Seeing Theory: basic probability and frequentist inference, Phase 4 · Empirical verdict, Version B + glossary experiment (B_glossary) (+8 more)

### Community 42 - "version_b"
Cohesion: 0.21
Nodes (9): What the model sees (Version B context), Scoreboard on 84 cases: A vs B, Version A pipeline: keyword match then fill a template, KB article context (INTENT_KB by expected intent), Building block: the augmented LLM (Anthropic, Building effective agents), Context engineering (the context is the product), Oracle context (B got the expected intent's articles), Day 6 · Version B: one model call with the right context (+1 more)

### Community 43 - "service.py"
Cohesion: 0.16
Nodes (3): redact(), secret_values(), sample_spread()

### Community 44 - "load_cases"
Cohesion: 0.16
Nodes (12): Day 04 notebook (rules-baseline), classify(), load_cases(), save_results(), api_usage(), use(), all_cases(), main() (+4 more)

### Community 45 - "Acme labelled test set (cases.jsonl)"
Cohesion: 0.12
Nodes (18): Acme Review Studio, tests/features/guardrails.feature (BDD guardrails), import_cases.py (lab data → workbook), runs/ versioned persistence, Critique Shadowing workflow, Day 03 notebook (test-set-first), Seven intents, problems() (+10 more)

### Community 46 - "Evaluation report (release decision)"
Cohesion: 0.15
Nodes (16): Evaluation report (release decision), Step-6 check hits, Expert pass rate, Missed escalation, Model needs-human flag recall, Routing accuracy, Unneeded escalation, Unsafe auto-send (+8 more)

### Community 51 - "then"
Cohesion: 0.15
Nodes (16): cases_run(), routing(), shows_round(), check_headroom(), check_offer_eligibility(), cites(), customer_writes(), marked_out_of_steps() (+8 more)

### Community 53 - "Day 06 notebook (one-llm-call)"
Cohesion: 0.47
Nodes (5): Day 06 notebook (one-llm-call), evaluate(), unit(), user_message(), version_b()

### Community 54 - "test_expert_review.py"
Cohesion: 0.19
Nodes (11): Feature: The grader agrees with the expert's round-2 review, Scenario Outline: The retention offer is pre-approved (c44), Scenario Outline: The expert's verdict and the grader's agree, a_draft_handed_off(), a_draft_sent(), checks_that_fail(), given_test_case(), grader_flags() (+3 more)

### Community 55 - "workflow.py"
Cohesion: 0.14
Nodes (4): AppSettings, Settings, State, service()

### Community 56 - "Dataset card (Acme test set)"
Cohesion: 0.13
Nodes (9): banner(), html_table(), provenance_table(), sha256(), tiles(), workbook_sheet(), Dataset card (Acme test set), Reports overview page (index.qmd) (+1 more)

### Community 57 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 58 - "ReviewStore"
Cohesion: 0.17
Nodes (8): ReviewStore, score_rounds(), load(), test_dataset_banner_omits_run_progress_but_keeps_warnings(), test_provenance_uses_full_hashes_and_escapes_values(), test_reports_select_versions_and_keep_the_round_alias(), test_legacy_reviews_migrate_and_round_trip_through_excel(), test_snapshot_collection_preserves_runs_and_reviews()

### Community 59 - "policy_violations"
Cohesion: 0.08
Nodes (17): Failure category: unsupported-amount false positive, KB03 · Payment methods, KB05 · Outages and restoration updates, KB13 · Router and Wi-Fi password, amounts(), _limit_context(), _negated(), not_english() (+9 more)

### Community 60 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 61 - "Safety router"
Cohesion: 0.09
Nodes (31): guard_hits(), decide(), Unsafe-to-automate case category, acme:AccountAction requiresRole AccountHolder, Amount guard (C3 only, not yet a router), acme:EscalationTrigger (planned), acme:PuneServiceArea (8 areas), Failure category: over-escalation on an answerable case (+23 more)

### Community 68 - "C3Provider"
Cohesion: 0.19
Nodes (3): c3_output(), C3Provider, AgentLoopAdapter

### Community 69 - "versions.py"
Cohesion: 0.10
Nodes (10): Lab, canonical(), case_hash(), digest(), lab_snapshot(), _sheet_hashes(), VersionRegistry, system_prompt() (+2 more)

### Community 70 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 71 - "judge_round1.py"
Cohesion: 0.17
Nodes (6): _parse_json_text(), judge_prompt(), main(), work(), run_judge(), use_data_root()

### Community 72 - "studio-offline.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 73 - "version-b.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 77 - "eval_checks"
Cohesion: 0.18
Nodes (15): chip(), customer_chips(), case_header(), cur(), draft_meta(), email_card(), expected_card(), guard_try_result() (+7 more)

### Community 78 - "embed"
Cohesion: 0.20
Nodes (7): qwen3:4b chat model (reads text only), Similarity search (cosine, top 3), embeddinggemma (EMBED_MODEL), Embeddings and retrieval, Hinglish handling, Recall@3 (retrieval metric), embed()

### Community 79 - "offline-direct.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 80 - "Load customer card and outages"
Cohesion: 0.24
Nodes (9): One model call (B) drafts the reply, Email in, Human approves the draft (shadow mode until the gates hold), Human queue (a person writes the reply), Load customer card and outages, Policy check (grader rules, in code), Reply out, Router: needs a human? (rules + 1 model call) (+1 more)

### Community 81 - "Step 6 · check claims and facts"
Cohesion: 0.35
Nodes (5): amounts(), claim_checks(), _flag(), check(), Policy verifier

### Community 82 - "Expert reviews data and errors are fixed"
Cohesion: 0.40
Nodes (5): Build LLM judge from expert examples, Error analysis: error rates, patterns, specialised judges, Expert reviews data and errors are fixed, Repeat on material change or periodic review, Principal domain expert

### Community 83 - "Day 09 notebook (success-cost-latency)"
Cohesion: 0.38
Nodes (4): Day 09 notebook (success-cost-latency), cost_inr(), percentile(), row()

### Community 85 - "_sim_run"
Cohesion: 0.23
Nodes (12): default_sim_step(), case_of(), replay_sources(), selected_sim_version(), _sim_case(), sim_fields(), sim_history_controls(), sim_optional_inputs() (+4 more)

### Community 86 - "test_cases_data.py"
Cohesion: 0.18
Nodes (8): cases_regional.jsonl (52 regional-language cases), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 87 - "pytest"
Cohesion: 0.21
Nodes (5): icon(), Elements, test_icons_have_no_network_or_accessible_name(), test_pipeline_keyboard_order_and_untrusted_details(), pytest_bdd_apply_tag()

### Community 88 - "Evaluation evidence Quarto site"
Cohesion: 0.18
Nodes (3): tests/features/report_metrics.feature, load_thresholds(), Evaluation evidence Quarto site

### Community 90 - "score"
Cohesion: 0.11
Nodes (19): Three graders: factual grounding, escalation correctness, response quality, Day 07 notebook (error-bars), Phase 0 · Baseline audit, Phase 1 · Rich TBox schema, term_misread failure tag, Failure category x version table, Failure category: grader wrong, failures.csv (tuning failures with note and category) (+11 more)

### Community 91 - "test_simulator_persistence.py"
Cohesion: 0.22
Nodes (3): compare_reviews(), service(), test_review_comparison_puts_new_missed_escalations_first()

### Community 92 - "review_record"
Cohesion: 0.14
Nodes (14): review_record(), run_case(), _ha(), _he(), _hh(), resume(), _run_missing(), worker() (+6 more)

### Community 95 - "common.py"
Cohesion: 0.19
Nodes (5): direct_output(), no_draft(), validate_draft(), _endpoint(), endpoint_origin()

### Community 96 - "studio-declarative.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 98 - "define_term"
Cohesion: 0.22
Nodes (7): Phase 2 · Graph engine core, Phase 3 · Wire grader and router, Meaning flow: policy.md + kb.md → ontology.ttl → pyoxigraph → glossary(), pyoxigraph (in-process RDF store, SPARQL 1.1), check_entitlement(), define_term(), test_version_c3_tools_and_decision_envelope()

### Community 99 - "scored"
Cohesion: 0.25
Nodes (6): score_boxes(), score_confusion(), score_modes(), score_plot(), score_rules(), scored()

### Community 100 - "when"
Cohesion: 0.25
Nodes (8): run_case(), read(), read_round(), when, spec, edges, nodes, agent_finishes()

### Community 101 - "Scenario: OWL reasoner inherits class properties and respects overrides"
Cohesion: 0.25
Nodes (5): reason_owl_rl(), Scenario: OWL reasoner inherits class properties and respects overrides, check_inherited_props(), check_inherited_role(), check_override_false()

### Community 102 - "_script"
Cohesion: 0.36
Nodes (6): _reply_turn(), _script(), _search_turn(), searches_every_step_and_after(), searches_every_step_then_replies(), searches_once_then_replies()

### Community 103 - "ScriptedModel"
Cohesion: 0.29
Nodes (3): lab(), ScriptedModel, world()

### Community 104 - "costs_inr"
Cohesion: 0.40
Nodes (5): Error cost (INR, per 1,000 emails), costs_inr, missed_escalation, unneeded_escalation, unsafe_auto_send

### Community 105 - "fixture"
Cohesion: 0.50
Nodes (3): runs(), world(), world()

### Community 106 - "Day 08 notebook (agent-loop-from-scratch)"
Cohesion: 0.67
Nodes (3): Day 08 notebook (agent-loop-from-scratch), run_agent(), show()

## Ambiguous Edges - Review These
- `version_b()` → `Failure category: unsupported-amount false positive`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `search_kb()` → `Similarity search (cosine, top 3)`  [AMBIGUOUS]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio · relation: semantically_similar_to
- `run_agent()` → `Failure category: unapproved offer`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `Pitch claim: deterministic workflow topology with hard guarantees` → `Build a workflow, not an agent: B + safety router + policy verifier`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Open question: which failures come from model size vs prompt or grader? (P4, P5)` → `ADR-001: How Acme Fibre should answer customer emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/day11-adr.drawio · relation: conceptually_related_to
- `ADR-001: How Acme Fibre should answer customer emails` → `Pitch claim: drafts cut handle time 40-60% in Phase 1`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: Option A missed 40 of 40 (0% safety)`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: router adds under 500 ms and ₹0.10 per 1,000 emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Author's unease: instinct favours C`  [AMBIGUOUS]
  1-measure-before-you-believe/12-article/article.md · relation: conceptually_related_to
- `Pitch claim: drafts cut handle time 40-60% in Phase 1` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Cost is not the issue (B ≈ ₹1.60/day, C ≈ ₹10/day)` → `Pitch claim: agent fails unit economics`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Open question: can a learned classifier route escalations better? (project 3)` → `Roadmap claim: transformer classifier drops router latency from 500 ms to under 20 ms`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to

## Knowledge Gaps
- **31 isolated node(s):** `fde-first-principles`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate`, `Latency not counted (tool time, network, queues, cold start)`, `Per-email costs beyond tokens` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 465 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `server()` connect `Review Studio server` to `test_ontology.py`, `app.py`, `test_c3_provider.py`, `refresh_versions`, `test_review_flow.py`, `Capabilities`, `RunResult`, `acme_metrics.py`, `lab.py`, `acme.py`, `load_business_rules`, `suggest_mode`, `service.py`, `ReviewStore`, `Safety router`, `eval_checks`, `Expert reviews data and errors are fixed`, `_sim_run`, `pytest`, `test_simulator_persistence.py`, `review_record`, `scored`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Version` be split into smaller, more focused modules?**
  _Cohesion score 0.10801393728222997 - nodes in this community are weakly interconnected._
- **Why does `policy_violations()` connect `policy_violations` to `load_business_rules`, `define_term`, `test_ontology.py`, `Domain expert (SME) review`, `version_c3.py`, `compute_entitlements`, `summary`, `service.py`, `test_policy_rules.py`, `Load customer card and outages`, `Step 6 · check claims and facts`, `RunResult`, `Build a workflow, not an agent: B + safety router + policy verifier`, `score`, `Rule 8 · ₹500 limit is per customer over 30 days`, `test_version_d.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `version_b()` and `Failure category: unsupported-amount false positive`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `search_kb()` and `Similarity search (cosine, top 3)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._