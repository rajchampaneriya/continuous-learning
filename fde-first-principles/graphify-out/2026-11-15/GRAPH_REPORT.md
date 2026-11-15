# Graph Report - fde-first-principles  (2026-11-15)

## Corpus Check
- 99 files · ~90,918 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 77 file(s) not represented in the graph (top: .jsonl 27, .feature 18, .drawio 12)
- WARNING: 77 of 212 files seen (36%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2004 nodes · 5675 edges · 110 communities (90 shown, 20 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 904 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `50535690`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- Version
- ontology.py
- Domain expert (SME) review
- test_escalation_metrics.py
- version_choices
- version_c3.py
- excluded_from_limit
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
- define
- test_guardrails.py
- Build a workflow, not an agent: B + safety router + policy verifier
- acme_metrics.py
- Rule 8 · ₹500 limit is per customer over 30 days
- app.py
- FDE First Principles learning log
- ScriptedResponse
- test_version_d.py
- acme.py
- compute_entitlements
- load_cases
- Day 3 · Write the test set before the system
- test_simulator_http.py
- Grader mutation tests
- Day 8: agent loop and failures
- load_cases
- Day 7 · Why 30 test cases can lie: error bars
- version_b
- service.py
- load_cases
- LLM as judge
- Evaluation report (release decision)
- test_gate_draft.py
- then
- Rate
- Day 06 notebook (one-llm-call)
- test_expert_review.py
- run_agent
- Dataset card (Acme test set)
- studio-c3.yaml
- ReviewStore
- Rule 4 · Never ask for OTP, password or full card number
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
- judge_round1.py
- studio-offline.yaml
- version-b.yaml
- test_ontology.py
- ._build
- eval_checks
- embed
- offline-direct.yaml
- Load customer card and outages
- Round 1 Principal Engineer review of the Acme Fibre email drafting solution
- Expert reviews data and errors are fixed
- test_gate_slots.py
- Version parameter and legacy round alias
- version_d.py
- test_cases_data.py
- pytest
- Day 1 · One model call: tokens, time and randomness
- Workflow
- score
- evals.py
- Acme Review Studio architecture/UX review (16 Oct 2026)
- test_router_rules.py
- studio-declarative.yaml
- Day 8 · Version C: an agent loop from scratch
- rescore.py
- when
- then
- _script
- Rule 5 · Never share another customer's details
- Failure analysis
- price_discount_rupees
- Day 08 notebook (agent-loop-from-scratch)
- Elements

## God Nodes (most connected - your core abstractions)
1. `server()` - 131 edges
2. `policy_violations()` - 66 edges
3. `Version` - 61 edges
4. `score()` - 60 edges
5. `RunInput` - 50 edges
6. `RunResult` - 46 edges
7. `build_decision_envelope()` - 46 edges
8. `VersionRegistry` - 42 edges
9. `load_cases()` - 41 edges
10. `compute_entitlements()` - 40 edges

## Surprising Connections (you probably didn't know these)
- `Similarity search (cosine, top 3)` --semantically_similar_to--> `search_kb()`  [AMBIGUOUS] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio → lab/acme_tools.py
- `version_b()` --semantically_similar_to--> `version_b()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/06-one-llm-call/notebook.ipynb → lab/version_b.py
- `ask()` --semantically_similar_to--> `chat()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/01-an-llm-call-is-http/notebook.ipynb → lab/llm.py
- `run_agent()` --semantically_similar_to--> `run_agent()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/08-agent-loop-from-scratch/notebook.ipynb → lab/agent.py
- `run_agent()` --semantically_similar_to--> `run_agent()`  [INFERRED] [semantically similar]
  1-measure-before-you-believe/09-success-cost-latency/notebook.ipynb → lab/agent.py

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

## Communities (110 total, 20 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.16
Nodes (13): Tool result appended as a 'tool' message, _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key() (+5 more)

### Community 1 - "Version"
Cohesion: 0.08
Nodes (10): OfflineProvider, DirectAdapter, VersionBAdapter, HttpAdapter, OrchestratedAdapter, RecordedProvider, RedactingSerializer, Version (+2 more)

### Community 2 - "ontology.py"
Cohesion: 0.14
Nodes (20): KnowledgeArticle and PolicyRule IRIs (documentedIn, enforcesRule), acme:PuneServiceArea (8 areas), KB12 · Shifting your connection, _asserted_store(), _bool_value(), customer_subgraph(), _data_cache(), cached() (+12 more)

### Community 3 - "Domain expert (SME) review"
Cohesion: 0.17
Nodes (13): Acme Review Studio, Acme_Fibre_Grounded_Draft_Eval.xlsx (eval workbook), draft_cases(), Engine audits the test set: c44 vs r20/p06a, SYSTEM_C agent prompt, Acme Fibre (fictional Pune broadband ISP), Domain expert (SME) review, Hinglish customer emails (+5 more)

### Community 4 - "test_escalation_metrics.py"
Cohesion: 0.22
Nodes (12): Scenario Outline: The grader summary reports escalation recall and precision, bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is() (+4 more)

### Community 5 - "version_choices"
Cohesion: 0.18
Nodes (9): case_choices(), review_page(), score_page(), _refresh_case_choices(), score_boxes(), simulator_page(), version_choices(), Review page (+1 more)

### Community 6 - "version_c3.py"
Cohesion: 0.08
Nodes (25): conversation(), amounts_asked_for(), extract_concepts(), build_decision_envelope(), check_entitlement(), _envelope_brief(), _grants(), offer_decisions() (+17 more)

### Community 7 - "excluded_from_limit"
Cohesion: 0.15
Nodes (16): Ephemeral per-case ABox (one customer), Varun's ₹300 credit: three agents, three meanings, Concession (refund, credit, waiver, discount value), Credit, Discount (also: सूट, छूट, ರಿಯಾಯಿತಿ), Double payment refund, Late-fee waiver, Outage credit (+8 more)

### Community 8 - "Review Studio server"
Cohesion: 0.06
Nodes (30): server(), batch_rev(), batch_status(), case_editor(), case_of(), _ed_save(), edit_case(), _ha() (+22 more)

### Community 9 - "summary"
Cohesion: 0.09
Nodes (18): Day 05 notebook (a-grader-you-can-trust), Day 07 notebook (error-bars), Day 09 notebook (success-cost-latency), cost_inr(), percentile(), row(), Day 10 notebook (read-the-failures), passed() (+10 more)

### Community 10 - "test_c3_provider.py"
Cohesion: 0.10
Nodes (19): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+11 more)

### Community 11 - "version_c3"
Cohesion: 0.13
Nodes (13): unasked_outage(), customer_reported_outage(), Scenario Outline: The envelope shows the outage only when the customer reports one, Feature: The area outage is in scope only when the customer reports that their service is down, Scenario: The customer-record tools show the outage when the customer reports one, Scenario Outline: A reply mentions the area outage only when the customer reported one, agent_finishes(), customer_writes() (+5 more)

### Community 12 - "test_policy_rules.py"
Cohesion: 0.10
Nodes (25): Failure category: unsupported-amount false positive, @known_gap scenarios as strict xfail, amounts(), policy_violations(), _promises_concession(), reveals_limit(), unearned_concession(), Feature: The grader enforces the Acme Fibre reply policy (+17 more)

### Community 13 - "test_escalation_rules.py"
Cohesion: 0.12
Nodes (21): not_english(), Scenario: An amount the agent wrote in an earlier turn is not the customer's ask, Scenario Outline: Every escalation records where it came from, Scenario: No rule fires on any case the experts labelled "no human needed", agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes() (+13 more)

### Community 14 - "test_report_metrics.py"
Cohesion: 0.20
Nodes (13): demo(), escalated(), escalated_by_code(), layer_fired(), nothing(), routing(), save(), sent() (+5 more)

### Community 15 - "refresh_versions"
Cohesion: 0.17
Nodes (16): _apply_retention(), case_list(), _fail(), _keep_current_visible(), _name_candidate(), _pass(), progress(), refresh_versions() (+8 more)

### Community 16 - "test_review_flow.py"
Cohesion: 0.13
Nodes (17): initial_mode(), suggest_mode(), validate_verdict(), _prefill(), check_fired(), ctx(), fail_no_critique(), fail_no_mode() (+9 more)

### Community 17 - "import_cases.py"
Cohesion: 0.23
Nodes (11): _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main(), _put_note() (+3 more)

### Community 18 - "Capabilities"
Cohesion: 0.16
Nodes (21): AgentLoopAdapter, _button(), render_comparison(), render_detail(), render_result(), _text(), _topology(), _tree() (+13 more)

### Community 19 - "Day 9 · Run all three: success, cost, latency"
Cohesion: 0.14
Nodes (19): version_a(), Today: passive prompt glossary (LLM does the joins), Cost levers (check each against the pass rate), ₹ per resolved email (what really drives cost), Fixed monthly costs spread over all emails, Costs hidden inside today's estimate, Latency not counted (tool time, network, queues, cold start), Cost drivers measured in the notebook (+11 more)

### Community 20 - "Studio evidence frame"
Cohesion: 0.20
Nodes (3): Evidence, mask(), nonempty()

### Community 21 - "RunResult"
Cohesion: 0.08
Nodes (26): review_record(), SimulationService, Adapter, RunInput, RunResult, AppSettings, run_case(), one() (+18 more)

### Community 22 - "Review dashboard (when do humans help?)"
Cohesion: 0.22
Nodes (11): build_frame(), layer_of(), Code saves, Agent hours per 1,000 emails, Disagreement rates, What triggered the escalations (layer analysis), Escalation rate, Failure categories (expert) (+3 more)

### Community 23 - "define"
Cohesion: 0.14
Nodes (13): knowledge_page(), meaning_concept_card(), meaning_rule_detail(), _alias_index(), concept_labels(), concept_provenance(), define(), policy_rules() (+5 more)

### Community 24 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 25 - "Build a workflow, not an agent: B + safety router + policy verifier"
Cohesion: 0.12
Nodes (19): Day 11 ADR-001 diagram, Open question: which failures come from model size vs prompt or grader? (P4, P5), ADR-001: How Acme Fibre should answer customer emails, Day 10: C on hosted glm-5.3-flash, held-out, Open question: how good is searched context for B? (project 2), Open question: do numbers hold on a stronger model and real emails? (project 6), ADR self-check, 5-minute CTO readout (pitch script) (+11 more)

### Community 26 - "acme_metrics.py"
Cohesion: 0.13
Nodes (5): fig_html(), html_table(), provenance_table(), workbook_sheet(), Dataset card (Acme test set)

### Community 27 - "Rule 8 · ₹500 limit is per customer over 30 days"
Cohesion: 0.18
Nodes (16): Failure category: unapproved offer, KB04 · Refunds and credits, KB06 · Outage credit, KB11 · Retention offer, ₹500 refund/credit limit, duplicate_payment_amount(), _retention_offer_rupees(), Scenario Outline: A draft that offers more than its decision allows goes to a person (+8 more)

### Community 28 - "app.py"
Cohesion: 0.06
Nodes (19): _bool(), export_to_excel(), _history(), _item(), load_lab(), _payments(), _put(), read_review_log() (+11 more)

### Community 29 - "FDE First Principles learning log"
Cohesion: 0.20
Nodes (11): qwen3:4b local model, Forward Deployed Engineer (FDE) mindset, Local models on Ollama (zero cost), Project 1 · Measure before you believe, fde-coach learn (daily drop and progress manager), FDE First Principles learning log, Project 6 · Back to the customer, Project 4 · Backprop by hand (micrograd) (+3 more)

### Community 31 - "test_version_d.py"
Cohesion: 0.13
Nodes (19): claim_amounts(), fill_offers(), money_asked(), route(), thread_of(), ThreadStore, version_d(), case() (+11 more)

### Community 32 - "acme.py"
Cohesion: 0.13
Nodes (17): Customer card context (name, area, plan), user_message(), Tool dispatch FUNCTIONS[name](**args), KB01 · Billing cycle and due dates, Acme help articles (kb.md), customer_card(), first_name(), kb_by_id() (+9 more)

### Community 33 - "compute_entitlements"
Cohesion: 0.11
Nodes (17): Phase 2 · Graph engine core, Phase 3 · Wire grader and router, data/acme/business_rules.json (commercial thresholds), _deep_update(), _default_rules(), load_business_rules(), months_since(), outage_exceeds_hours() (+9 more)

### Community 34 - "load_cases"
Cohesion: 0.19
Nodes (8): Scenario Outline: The guide's edge cases match the expert labels, Scenario: Every intent has a definition, Feature: One written convention decides the intent label, Scenario Outline (@known_gap): Labels that disagree with the guide, case_is_labelled(), every_intent_defined(), labelled_cases(), world()

### Community 35 - "Day 3 · Write the test set before the system"
Cohesion: 0.11
Nodes (19): Proposed controlled workflow (deterministic routing + one drafting step), Five discoveries, five architecture pivots, Building effective agents (Anthropic), Email-to-reply decision map, Workflow patterns: prompt chaining, routing, agent, Day 03 notebook (test-set-first), Seven intents, problems() (+11 more)

### Community 36 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), Response, run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout() (+4 more)

### Community 37 - "Grader mutation tests"
Cohesion: 0.15
Nodes (17): Scenario Outline: The grader catches a reply that was broken on purpose, @known_gap Scenario Outline: Known gaps: correct replies the grader still fails, _add_each_banned(), _append(), _cases_where(), _change_intent(), _drop_each_fact(), grader_fails() (+9 more)

### Community 38 - "Day 8: agent loop and failures"
Cohesion: 0.13
Nodes (17): Final answer JSON {intent, reply, needs_human}, Gave-up fallback at MAX_STEPS, Stop condition: reply has no tool_calls, MAX_STEPS = 6 step limit, qwen3:4b local model (temperature 0), Act: does it hold on emails we never looked at?, Decide: which single fix matters most?, Observe: what does a pass rate hide? (+9 more)

### Community 39 - "load_cases"
Cohesion: 0.19
Nodes (9): Day 04 notebook (rules-baseline), classify(), data_root(), load_cases(), kb_only(), main(), recall_for(), system_prompt() (+1 more)

### Community 40 - "Day 7 · Why 30 test cases can lie: error bars"
Cohesion: 0.18
Nodes (12): Stage 4 · Statistical evaluation: 'How sure are we?', Stage 5 · System-level evaluation: 'Does the whole system work?', Stage 6 · Agentic AI evaluation: 'Does the agent finish the job?', Stage 7 · Continuous production evaluation: 'Is it still working for users?', A statistical approach to model evaluations (Anthropic), Seeing Theory: basic probability and frequentist inference, Phase 4 · Empirical verdict, Confidence interval (+4 more)

### Community 42 - "version_b"
Cohesion: 0.22
Nodes (9): What the model sees (Version B context), Scoreboard on 84 cases: A vs B, Version A pipeline: keyword match then fill a template, KB article context (INTENT_KB by expected intent), Building block: the augmented LLM (Anthropic, Building effective agents), Context engineering (the context is the product), Oracle context (B got the expected intent's articles), Day 6 · Version B: one model call with the right context (+1 more)

### Community 43 - "service.py"
Cohesion: 0.06
Nodes (13): direct_output(), no_draft(), validate_draft(), DeclarativeAdapter, endpoint_origin(), redact(), secret_values(), State (+5 more)

### Community 44 - "load_cases"
Cohesion: 0.13
Nodes (15): Run provenance (.meta.json: model, prompt fingerprint, settings), fingerprint(), git_commit(), save_results(), summary(), api_usage(), use(), all_cases() (+7 more)

### Community 45 - "LLM as judge"
Cohesion: 0.25
Nodes (5): Critique Shadowing workflow, Stage 1 · Traditional software testing: 'Is it correct?', Stage 2 · Early machine learning evaluation: 'How accurate is it?', Stage 3 · Foundation model evaluation: 'Is it good, safe, and grounded?', LLM as judge

### Community 46 - "Evaluation report (release decision)"
Cohesion: 0.10
Nodes (23): load_thresholds(), Evaluation report (release decision), Step-6 check hits, Error cost (INR, per 1,000 emails), Expert pass rate, Missed escalation, Model needs-human flag recall, Routing accuracy (+15 more)

### Community 50 - "test_gate_draft.py"
Cohesion: 0.14
Nodes (10): check_draft(), asked_for_money(), draft_check_reports(), model_drafts(), _reply(), test_an_unrepairable_draft_escalates(), fake_chat(), test_the_gate_repairs_a_granting_draft() (+2 more)

### Community 51 - "then"
Cohesion: 0.14
Nodes (16): banner(), cases_run(), no_gate(), runs(), unsafe(), customer_writes(), marked_out_of_steps(), model_called() (+8 more)

### Community 53 - "Day 06 notebook (one-llm-call)"
Cohesion: 0.50
Nodes (4): Day 06 notebook (one-llm-call), evaluate(), unit(), version_b()

### Community 54 - "test_expert_review.py"
Cohesion: 0.19
Nodes (11): Feature: The grader agrees with the expert's round-2 review, Scenario Outline: The retention offer is pre-approved (c44), Scenario Outline: The expert's verdict and the grader's agree, a_draft_handed_off(), a_draft_sent(), checks_that_fail(), given_test_case(), grader_flags() (+3 more)

### Community 55 - "run_agent"
Cohesion: 0.19
Nodes (12): run_agent(), customer_text(), extract_json(), _answer(), _finish(), run_agent(), _call(), _draft_only() (+4 more)

### Community 56 - "Dataset card (Acme test set)"
Cohesion: 0.12
Nodes (7): tests/features/report_metrics.feature, banner(), sha256(), tiles(), Reports overview page (index.qmd), Demo round (make_demo_runs.py), Evaluation evidence Quarto site

### Community 57 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 58 - "ReviewStore"
Cohesion: 0.17
Nodes (9): ReviewStore, _export(), score_rounds(), load(), test_dataset_banner_omits_run_progress_but_keeps_warnings(), test_provenance_uses_full_hashes_and_escapes_values(), test_reports_select_versions_and_keep_the_round_alias(), test_legacy_reviews_migrate_and_round_trip_through_excel() (+1 more)

### Community 59 - "Rule 4 · Never ask for OTP, password or full card number"
Cohesion: 0.13
Nodes (7): Examples from the expert's review (worst fails, what good looks like), KB03 · Payment methods, KB05 · Outages and restoration updates, KB13 · Router and Wi-Fi password, _approved(), _negated(), Scenario Outline: The grader names the policy rule a broken reply breaks

### Community 60 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 61 - "Safety router"
Cohesion: 0.10
Nodes (25): guard_hits(), decide(), tests/features/guardrails.feature (BDD guardrails), Unsafe-to-automate case category, acme:AccountAction requiresRole AccountHolder, Amount guard (C3 only, not yet a router), acme:EscalationTrigger (planned), Failure category: missed escalation (+17 more)

### Community 63 - "test_holdout_run.py"
Cohesion: 0.29
Nodes (5): _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 68 - "C3Provider"
Cohesion: 0.09
Nodes (15): c3_output(), C3Provider, ClaudeCodeProvider, make_provider(), _parse_json_text(), _result(), replay_sources(), selected_sim_version() (+7 more)

### Community 69 - "versions.py"
Cohesion: 0.09
Nodes (14): Lab, _json(), _now(), RunStore, canonical(), case_hash(), digest(), lab_snapshot() (+6 more)

### Community 70 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 71 - "judge_round1.py"
Cohesion: 0.33
Nodes (4): judge_prompt(), main(), work(), run_judge()

### Community 72 - "studio-offline.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 73 - "version-b.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 74 - "test_ontology.py"
Cohesion: 0.17
Nodes (17): validate_ontology_ops(), Scenario: operational governance has zero catalog drift, check_ops_clean(), _finding(), run_ops_validation(), semantic_data(), test_entitlement_article_follows_the_concept_link(), test_entitlement_articles_allow_multiple_links_but_not_missing_links() (+9 more)

### Community 75 - "._build"
Cohesion: 0.18
Nodes (12): _trace(), user_prompt(), draft(), fetch(), human(), log(), receive(), route() (+4 more)

### Community 77 - "eval_checks"
Cohesion: 0.10
Nodes (23): eval_checks(), chip(), icon(), customer_chips(), case_header(), cur(), draft_meta(), email_card() (+15 more)

### Community 78 - "embed"
Cohesion: 0.24
Nodes (6): qwen3:4b chat model (reads text only), Similarity search (cosine, top 3), embeddinggemma (EMBED_MODEL), Embeddings and retrieval, Hinglish handling, Recall@3 (retrieval metric)

### Community 79 - "offline-direct.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 80 - "Load customer card and outages"
Cohesion: 0.24
Nodes (9): One model call (B) drafts the reply, Email in, Human approves the draft (shadow mode until the gates hold), Human queue (a person writes the reply), Load customer card and outages, Policy check (grader rules, in code), Reply out, Router: needs a human? (rules + 1 model call) (+1 more)

### Community 81 - "Round 1 Principal Engineer review of the Acme Fibre email drafting solution"
Cohesion: 0.22
Nodes (9): amounts(), claim_checks(), _flag(), check(), Round 1 Principal Engineer review of the Acme Fibre email drafting solution, Safe-send capture rate (new north-star metric), Concept → KB retrieval gain (with alias leakage caveat), Multilingual lexical layer (SKOS labels) (+1 more)

### Community 82 - "Expert reviews data and errors are fixed"
Cohesion: 0.40
Nodes (5): Build LLM judge from expert examples, Error analysis: error rates, patterns, specialised judges, Expert reviews data and errors are fixed, Repeat on material change or periodic review, Principal domain expert

### Community 83 - "test_gate_slots.py"
Cohesion: 0.14
Nodes (10): canonical_offer(), _slot_norm(), customer_writes(), gate_escalates(), grant_sentences(), model_returns_slots(), reply_contains(), test_canonical_offer_maps_to_the_catalogue() (+2 more)

### Community 85 - "version_d.py"
Cohesion: 0.20
Nodes (7): intent_guide(), lookup_customer_c3(), _without_outage(), _envelope_brief_d(), _record_block(), _user_content(), Scenario: The customer-record tools withhold the outage when it is out of scope

### Community 86 - "test_cases_data.py"
Cohesion: 0.17
Nodes (9): cases_regional.jsonl (52 regional-language cases), load_outages(), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script() (+1 more)

### Community 87 - "pytest"
Cohesion: 0.14
Nodes (10): highlight(), meaning_card(), fact_rows(), origin(), pipeline(), Elements, test_icons_have_no_network_or_accessible_name(), test_meaning_card_shows_provenance_sources_and_clickable_rules() (+2 more)

### Community 88 - "Day 1 · One model call: tokens, time and randomness"
Cohesion: 0.29
Nodes (8): Day 01 notebook (an-llm-call-is-http), ask(), Deep Dive into LLMs like ChatGPT (Karpathy), inference chapter, Ollama /api/chat endpoint, Per-step agent trace, Temperature, seed and randomness, Tokens in, tokens out and latency, Day 1 · One model call: tokens, time and randomness

### Community 89 - "Workflow"
Cohesion: 0.27
Nodes (5): Deps, Workflow, demo_verdict(), main(), world()

### Community 90 - "score"
Cohesion: 0.16
Nodes (14): 20 SME-reviewed ground-truth scenarios, Three graders: factual grounding, escalation correctness, response quality, Failure category x version table, Failure category: grader wrong, failures.csv (tuning failures with note and category), Grader false alarms ('5-7 working days', 'Rs. 100'), Acme labelled test set (cases.jsonl), Grader (+6 more)

### Community 91 - "evals.py"
Cohesion: 0.22
Nodes (3): percent_asks_in_rupees(), _plan_in_sentence(), _alias_pattern()

### Community 92 - "Acme Review Studio architecture/UX review (16 Oct 2026)"
Cohesion: 0.18
Nodes (5): _run_missing(), worker(), selected_review_version(), _settings(), Acme Review Studio architecture/UX review (16 Oct 2026)

### Community 95 - "test_router_rules.py"
Cohesion: 0.22
Nodes (6): customer_writes(), router_does_not_fire(), router_fast_path(), router_fires(), test_a_retention_repeat_on_a_cancellation_is_not_money(), world()

### Community 96 - "studio-declarative.yaml"
Cohesion: 0.15
Nodes (12): adapter, config, model, provider, timeout_s, implementation, inputs, label (+4 more)

### Community 98 - "Day 8 · Version C: an agent loop from scratch"
Cohesion: 0.15
Nodes (12): Business Graph Engine (graph computes, LLM verbalizes), Phase 0 · Baseline audit, Phase 1 · Rich TBox schema, Static TBox (shared meaning, zero PII), Meaning flow: policy.md + kb.md → ontology.ttl → pyoxigraph → glossary(), Version B + glossary experiment (B_glossary), pyoxigraph (in-process RDF store, SPARQL 1.1), term_misread failure tag (+4 more)

### Community 99 - "rescore.py"
Cohesion: 0.50
Nodes (6): _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before()

### Community 100 - "when"
Cohesion: 0.15
Nodes (12): read(), read_round(), when, glossary(), Scenario: the glossary holds definitions, never customer records, read_reply(), apply_commercial_rule_override(), ask_glossary() (+4 more)

### Community 101 - "then"
Cohesion: 0.15
Nodes (11): reason_owl_rl(), Scenario: OWL reasoner inherits class properties and respects overrides, check_business_rule_cooldown(), check_headroom(), check_inherited_props(), check_inherited_role(), check_offer_eligibility(), check_override_false() (+3 more)

### Community 102 - "_script"
Cohesion: 0.36
Nodes (6): _reply_turn(), _script(), _search_turn(), searches_every_step_and_after(), searches_every_step_then_replies(), searches_once_then_replies()

### Community 104 - "Failure analysis"
Cohesion: 0.33
Nodes (4): Error analysis as an OODA loop, Case c04: C claimed a processed cancellation, scored safe, Failure analysis, OODA loop (observe, orient, decide, act)

### Community 105 - "price_discount_rupees"
Cohesion: 0.40
Nodes (4): acme:Plan catalog (Basic ₹699, Plus ₹999, Pro ₹1,499), KB09 · Plan upgrades and downgrades, Acme plans: Basic, Plus, Pro, price_discount_rupees()

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
- `Open question: which failures come from model size vs prompt or grader? (P4, P5)` → `ADR-001: How Acme Fibre should answer customer emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/day11-adr.drawio · relation: conceptually_related_to
- `ADR-001: How Acme Fibre should answer customer emails` → `Pitch claim: drafts cut handle time 40-60% in Phase 1`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Pitch claim: deterministic workflow topology with hard guarantees`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Build a workflow, not an agent: B + safety router + policy verifier` → `Author's unease: instinct favours C`  [AMBIGUOUS]
  1-measure-before-you-believe/12-article/article.md · relation: conceptually_related_to
- `Pitch claim: drafts cut handle time 40-60% in Phase 1` → `Phased rollout: shadow mode, then automated egress per intent`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Cost is not the issue (B ≈ ₹1.60/day, C ≈ ₹10/day)` → `Pitch claim: agent fails unit economics`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: Option A missed 40 of 40 (0% safety)`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `ADR-001 evidence table (day 9 runs)` → `Pitch claim: router adds under 500 ms and ₹0.10 per 1,000 emails`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
- `Open question: can a learned classifier route escalations better? (project 3)` → `Roadmap claim: transformer classifier drops router latency from 500 ms to under 20 ms`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to

## Knowledge Gaps
- **31 isolated node(s):** `fde-first-principles`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate`, `Latency not counted (tool time, network, queues, cold start)`, `Per-email costs beyond tokens` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 495 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `server()` connect `Review Studio server` to `ontology.py`, `version_choices`, `refresh_versions`, `test_review_flow.py`, `Capabilities`, `RunResult`, `define`, `app.py`, `acme.py`, `compute_entitlements`, `ReviewStore`, `Safety router`, `C3Provider`, `versions.py`, `test_ontology.py`, `eval_checks`, `Expert reviews data and errors are fixed`, `pytest`, `Acme Review Studio architecture/UX review (16 Oct 2026)`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Version` be split into smaller, more focused modules?**
  _Cohesion score 0.07609427609427609 - nodes in this community are weakly interconnected._
- **Why does `policy_violations()` connect `test_policy_rules.py` to `ontology.py`, `Domain expert (SME) review`, `version_c3.py`, `summary`, `version_c3`, `test_escalation_rules.py`, `RunResult`, `Build a workflow, not an agent: B + safety router + policy verifier`, `Rule 8 · ₹500 limit is per customer over 30 days`, `test_version_d.py`, `compute_entitlements`, `Grader mutation tests`, `service.py`, `run_agent`, `Rule 4 · Never ask for OTP, password or full card number`, `test_ontology.py`, `._build`, `Load customer card and outages`, `version_d.py`, `score`, `evals.py`, `Day 8 · Version C: an agent loop from scratch`, `when`, `Rule 5 · Never share another customer's details`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `version_b()` and `Failure category: unsupported-amount false positive`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `search_kb()` and `Similarity search (cosine, top 3)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._