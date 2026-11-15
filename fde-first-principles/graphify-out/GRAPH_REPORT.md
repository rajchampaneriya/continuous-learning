# Graph Report - fde-first-principles  (2026-11-15)

## Corpus Check
- 107 files · ~96,256 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 78 file(s) not represented in the graph (top: .jsonl 27, .feature 19, .drawio 12)
- WARNING: 78 of 221 files seen (35%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2160 nodes · 6128 edges · 105 communities (80 shown, 25 thin omitted)
- Extraction: 85% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 883 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `057d570e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- llm.py
- ._build
- ontology.py
- otel.py
- test_escalation_metrics.py
- version_choices
- run_agent
- Rule 2 · No exact outage fix time; share ticket ID
- Review Studio server
- Rule 8 · ₹500 limit is per customer over 30 days
- test_c3_provider.py
- version_c3
- policy_violations
- test_escalation_rules.py
- Version
- version_b
- test_review_flow.py
- import_cases.py
- RunResult
- Day 9 · Run all three: success, cost, latency
- Studio evidence frame
- RunResult
- Evaluation report (release decision)
- test_simulator_feature.py
- Safety router
- Build a workflow, not an agent: B + safety router + policy verifier
- acme_metrics.py
- version-d.yaml
- app.py
- FDE First Principles learning log
- ScriptedResponse
- route
- lab/version_d.py
- business_rules.py
- load_cases
- Day 3 · Write the test set before the system
- test_simulator_http.py
- test_grader_mutations.py
- needs_human escalation
- policy_violations
- Day 7 · Why 30 test cases can lie: error bars
- version_b
- versions.py
- load_cases
- Adapter
- then
- test_gate_draft.py
- test_report_metrics.py
- Rate
- Day 1 · One model call: tokens, time and randomness
- _script
- Ontology layer for Acme Fibre
- studio-c3.yaml
- ReviewStore
- config
- Rule 11 · Only the account holder can change the account
- KB slow speed and technician
- compare_reviews
- KB new installation
- KB search queries
- Project config
- test_holdout_run.py
- versions.py
- c3-agent.yaml
- fixture
- studio-offline.yaml
- version-b.yaml
- test_ontology.py
- test_guardrails.py
- eval_checks
- offline-direct.yaml
- OrchestratedAdapter
- Acme labelled test set (cases.jsonl)
- Embedding model rubric (why embeddinggemma)
- Response
- run_agent
- test_cases_data.py
- pytest
- Review dashboard (when do humans help?)
- review_record
- test_expert_review.py
- rescore.py
- team-c3.yaml
- Scenario: OWL reasoner inherits class properties and respects overrides
- team-offline.yaml
- judge_round1.py
- version_c3

## God Nodes (most connected - your core abstractions)
1. `server()` - 136 edges
2. `Version` - 76 edges
3. `policy_violations()` - 66 edges
4. `RunResult` - 60 edges
5. `score()` - 60 edges
6. `RunInput` - 49 edges
7. `build_decision_envelope()` - 46 edges
8. `Span` - 44 edges
9. `load_cases()` - 41 edges
10. `compute_entitlements()` - 41 edges

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

## Communities (105 total, 25 thin omitted)

### Community 0 - "llm.py"
Cohesion: 0.16
Nodes (13): Tool result appended as a 'tool' message, _cache_file(), chat(), _chat_anthropic(), _chat_api(), embed(), _env(), _key() (+5 more)

### Community 1 - "._build"
Cohesion: 0.09
Nodes (20): amounts(), claim_checks(), _flag(), guard_hits(), ClaudeCodeProvider, _parse_json_text(), _result(), _trace() (+12 more)

### Community 2 - "ontology.py"
Cohesion: 0.07
Nodes (36): knowledge_page(), _meaning_card_rule_selected(), meaning_concept_card(), meaning_rule_detail(), KnowledgeArticle and PolicyRule IRIs (documentedIn, enforcesRule), Concept → KB retrieval gain (with alias leakage caveat), Multilingual lexical layer (SKOS labels), acme:Plan catalog (Basic ₹699, Plus ₹999, Pro ₹1,499) (+28 more)

### Community 3 - "otel.py"
Cohesion: 0.17
Nodes (16): _attributes(), _hex(), _layout(), place(), _name(), _provider_name(), _span_attributes(), to_otlp() (+8 more)

### Community 4 - "test_escalation_metrics.py"
Cohesion: 0.22
Nodes (12): Scenario Outline: The grader summary reports escalation recall and precision, bot_escalates(), cases(), _graded(), human_ok_is(), human_rate_is(), _percent(), precision_is() (+4 more)

### Community 5 - "version_choices"
Cohesion: 0.20
Nodes (5): review_page(), score_boxes(), _settings(), Review page, Acme Review Studio architecture/UX review (16 Oct 2026)

### Community 6 - "run_agent"
Cohesion: 0.09
Nodes (27): Day 08 notebook (agent-loop-from-scratch), run_agent(), show(), run_agent(), customer_text(), extract_json(), _envelope_brief(), _grants() (+19 more)

### Community 7 - "Rule 2 · No exact outage fix time; share ticket ID"
Cohesion: 0.20
Nodes (9): Varun's ₹300 credit: three agents, three meanings, KB05 · Outages and restoration updates, KB06 · Outage credit, Credit, Double payment refund, Outage credit, Scenario: automatic money and retention offer don't count toward ₹500, answer_is() (+1 more)

### Community 8 - "Review Studio server"
Cohesion: 0.05
Nodes (50): default_sim_step(), server(), _apply_retention(), batch_rev(), batch_status(), case_editor(), case_list(), case_of() (+42 more)

### Community 9 - "Rule 8 · ₹500 limit is per customer over 30 days"
Cohesion: 0.19
Nodes (16): Failure category: unapproved offer, KB04 · Refunds and credits, KB11 · Retention offer, ₹500 refund/credit limit, _retention_offer_rupees(), Feature: Escalation rules run as code before the model drafts a reply, Scenario Outline: Routine emails are left to the model, Scenario Outline: A rule sends the email to a person (+8 more)

### Community 10 - "test_c3_provider.py"
Cohesion: 0.10
Nodes (19): c3_fails(), c3_given_case(), c3_given_history(), c3_replies(), draft_cites(), draft_needs_human(), draft_reason(), draft_says() (+11 more)

### Community 11 - "version_c3"
Cohesion: 0.17
Nodes (11): build_decision_envelope(), Scenario Outline: The envelope shows the outage only when the customer reports one, Scenario: The customer-record tools show the outage when the customer reports one, agent_finishes(), customer_writes(), envelope_is_built(), envelope_shows(), lookup_result_shows() (+3 more)

### Community 12 - "policy_violations"
Cohesion: 0.10
Nodes (25): @known_gap scenarios as strict xfail, not_english(), _promises_concession(), reveals_limit(), unearned_concession(), Scenario Outline: Declines, hand-offs and automatic entitlements are not promises, Feature: The grader enforces the Acme Fibre reply policy, @known_gap Scenario Outline: Known gaps the grader does not handle yet (+17 more)

### Community 13 - "test_escalation_rules.py"
Cohesion: 0.14
Nodes (19): Scenario: An amount the agent wrote in an earlier turn is not the customer's ask, Scenario Outline: Every escalation records where it came from, Scenario: No rule fires on any case the experts labelled "no human needed", agent_finishes(), agent_replied(), customer_earlier_wrote(), customer_now_writes(), envelope_decides() (+11 more)

### Community 14 - "Version"
Cohesion: 0.06
Nodes (19): AgentLoopAdapter, DirectAdapter, raw_response(), turn_spans(), usage_of(), VersionBAdapter, _ms(), MultiAgentAdapter (+11 more)

### Community 15 - "version_b"
Cohesion: 0.15
Nodes (14): What the model sees (Version B context), Scoreboard on 84 cases: A vs B, Version A pipeline: keyword match then fill a template, KB article context (INTENT_KB by expected intent), Building block: the augmented LLM (Anthropic, Building effective agents), Acme Fibre (fictional Pune broadband ISP), KB09 · Plan upgrades and downgrades, Context engineering (the context is the product) (+6 more)

### Community 16 - "test_review_flow.py"
Cohesion: 0.12
Nodes (18): eval_checks(), initial_mode(), suggest_mode(), validate_verdict(), _prefill(), check_fired(), ctx(), fail_no_critique() (+10 more)

### Community 17 - "import_cases.py"
Cohesion: 0.24
Nodes (11): _restore_chart(), _add_headers(), _copy_style(), import_cases(), import_customers(), import_policy(), _last_row(), main() (+3 more)

### Community 18 - "RunResult"
Cohesion: 0.14
Nodes (38): HttpAdapter, _allows(), _button(), _children(), _descendants(), _exchange(), _exchange_view(), _has_turns() (+30 more)

### Community 19 - "Day 9 · Run all three: success, cost, latency"
Cohesion: 0.15
Nodes (16): classify(), version_a(), Cost levers (check each against the pass rate), ₹ per resolved email (what really drives cost), Fixed monthly costs spread over all emails, Costs hidden inside today's estimate, Latency not counted (tool time, network, queues, cold start), Cost drivers measured in the notebook (+8 more)

### Community 20 - "Studio evidence frame"
Cohesion: 0.20
Nodes (5): Evidence, mask(), nonempty(), Papermill for report parameters, Version parameter and legacy round alias

### Community 21 - "RunResult"
Cohesion: 0.10
Nodes (25): SimulationService, RunInput, replay_sources(), selected_sim_version(), sim_fields(), sim_replay_options(), _sim_run(), sim_run_control() (+17 more)

### Community 22 - "Evaluation report (release decision)"
Cohesion: 0.09
Nodes (18): load_thresholds(), Evaluation report (release decision), Step-6 check hits, Error cost (INR, per 1,000 emails), Routing accuracy, Unsafe auto-send, Evaluation evidence Quarto site, Agent hours per 1,000 emails (+10 more)

### Community 23 - "test_simulator_feature.py"
Cohesion: 0.06
Nodes (41): run_case(), read(), read_round(), approve(), batch_offline(), batch_started(), c3_version(), finished_on() (+33 more)

### Community 24 - "Safety router"
Cohesion: 0.12
Nodes (15): 20 SME-reviewed ground-truth scenarios, Unsafe-to-automate case category, Amount guard (C3 only, not yet a router), One model call (B) drafts the reply, Email in, Human approves the draft (shadow mode until the gates hold), Human queue (a person writes the reply), Load customer card and outages (+7 more)

### Community 25 - "Build a workflow, not an agent: B + safety router + policy verifier"
Cohesion: 0.15
Nodes (16): Day 11 ADR-001 diagram, Open question: which failures come from model size vs prompt or grader? (P4, P5), ADR-001: How Acme Fibre should answer customer emails, Open question: how good is searched context for B? (project 2), ADR-001 diagram: B with a safety router and a policy check, Human support queue, Search the help articles (retrieved, not oracle context), ADR self-check (+8 more)

### Community 26 - "acme_metrics.py"
Cohesion: 0.08
Nodes (11): tests/features/report_metrics.feature, banner(), fig_html(), html_table(), provenance_table(), sha256(), tiles(), workbook_sheet() (+3 more)

### Community 27 - "version-d.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 28 - "app.py"
Cohesion: 0.11
Nodes (13): export_to_excel(), _put(), read_review_log(), make_provider(), case_choices(), score_page(), _export(), provider_status() (+5 more)

### Community 29 - "FDE First Principles learning log"
Cohesion: 0.20
Nodes (11): qwen3:4b local model, Forward Deployed Engineer (FDE) mindset, Local models on Ollama (zero cost), Project 1 · Measure before you believe, fde-coach learn (daily drop and progress manager), FDE First Principles learning log, Project 6 · Back to the customer, Project 4 · Backprop by hand (micrograd) (+3 more)

### Community 31 - "route"
Cohesion: 0.06
Nodes (32): canonical_offer(), fill_offers(), route(), thread_of(), ThreadStore, watchdog(), customer_writes(), gate_escalates() (+24 more)

### Community 32 - "lab/version_d.py"
Cohesion: 0.06
Nodes (33): Tool dispatch FUNCTIONS[name](**args), KB01 · Billing cycle and due dates, Acme help articles (kb.md), first_name(), intent_guide(), kb_by_id(), load_kb(), escalate() (+25 more)

### Community 33 - "business_rules.py"
Cohesion: 0.16
Nodes (8): Phase 2 · Graph engine core, Phase 3 · Wire grader and router, _deep_update(), _default_rules(), months_since(), outage_exceeds_hours(), _parse_date(), _rules_at()

### Community 34 - "load_cases"
Cohesion: 0.15
Nodes (9): pytest_bdd_apply_tag(), Scenario Outline: The guide's edge cases match the expert labels, Scenario: Every intent has a definition, Feature: One written convention decides the intent label, Scenario Outline (@known_gap): Labels that disagree with the guide, case_is_labelled(), every_intent_defined(), labelled_cases() (+1 more)

### Community 35 - "Day 3 · Write the test set before the system"
Cohesion: 0.14
Nodes (15): Proposed controlled workflow (deterministic routing + one drafting step), Five discoveries, five architecture pivots, Building effective agents (Anthropic), Email-to-reply decision map, Workflow patterns: prompt chaining, routing, agent, Day 03 notebook (test-set-first), Seven intents, problems() (+7 more)

### Community 36 - "test_simulator_http.py"
Cohesion: 0.14
Nodes (12): _endpoint(), run(), Session, test_endpoints_reject_untrusted_urls(), test_http_rejects_oversized_and_invalid_drafts(), test_http_sends_auth_without_persisting_secrets(), test_http_stream_stops_after_timeout(), test_loopback_http_is_allowed_only_when_explicitly_allowlisted() (+4 more)

### Community 37 - "test_grader_mutations.py"
Cohesion: 0.08
Nodes (28): Examples from the expert's review (worst fails, what good looks like), KB03 · Payment methods, KB13 · Router and Wi-Fi password, Mutation testing of the grader, _approved(), _negated(), Scenario Outline: The grader catches a reply that was broken on purpose, Feature: Mutation tests for the grader (+20 more)

### Community 38 - "needs_human escalation"
Cohesion: 0.23
Nodes (11): Final answer JSON {intent, reply, needs_human}, Gave-up fallback at MAX_STEPS, Stop condition: reply has no tool_calls, acme:EscalationTrigger (planned), MAX_STEPS = 6 step limit, Failure category: missed escalation, KB15 · Account security, KB16 · Talking to a human (+3 more)

### Community 39 - "policy_violations"
Cohesion: 0.08
Nodes (23): Three graders: factual grounding, escalation correctness, response quality, Day 05 notebook (a-grader-you-can-trust), Failure category: grader wrong, Failure category: unsupported-amount false positive, passed(), scoreboard(), show(), Grader false alarms ('5-7 working days', 'Rs. 100') (+15 more)

### Community 40 - "Day 7 · Why 30 test cases can lie: error bars"
Cohesion: 0.13
Nodes (15): Stage 4 · Statistical evaluation: 'How sure are we?', Stage 5 · System-level evaluation: 'Does the whole system work?', Stage 6 · Agentic AI evaluation: 'Does the agent finish the job?', Stage 7 · Continuous production evaluation: 'Is it still working for users?', A statistical approach to model evaluations (Anthropic), Seeing Theory: basic probability and frequentist inference, Phase 4 · Empirical verdict, Meaning flow: policy.md + kb.md → ontology.ttl → pyoxigraph → glossary() (+7 more)

### Community 42 - "version_b"
Cohesion: 0.18
Nodes (11): Day 06 notebook (one-llm-call), Customer card context (name, area, plan), evaluate(), unit(), user_message(), version_b(), Load customer card and outages (code, no model), conversation() (+3 more)

### Community 43 - "versions.py"
Cohesion: 0.05
Nodes (23): _bool(), _history(), _item(), load_lab(), _payments(), _review_row_formulas(), _split(), OfflineProvider (+15 more)

### Community 44 - "load_cases"
Cohesion: 0.08
Nodes (28): Day 04 notebook (rules-baseline), Day 07 notebook (error-bars), Day 09 notebook (success-cost-latency), cost_inr(), percentile(), row(), Day 10 notebook (read-the-failures), Run provenance (.meta.json: model, prompt fingerprint, settings) (+20 more)

### Community 46 - "then"
Cohesion: 0.14
Nodes (17): pinned(), valid_contract(), banner(), pass_rate(), shows_round(), unsafe(), check_business_rule_cooldown(), concept_is_matched() (+9 more)

### Community 50 - "test_gate_draft.py"
Cohesion: 0.14
Nodes (10): check_draft(), asked_for_money(), draft_check_reports(), model_drafts(), _reply(), test_an_unrepairable_draft_escalates(), fake_chat(), test_the_gate_repairs_a_granting_draft() (+2 more)

### Community 51 - "test_report_metrics.py"
Cohesion: 0.15
Nodes (17): scripted_adapter(), cases_run(), demo(), escalated(), escalated_by_code(), layer_fired(), missed(), no_gate() (+9 more)

### Community 52 - "Rate"
Cohesion: 0.29
Nodes (3): Rate, wilson(), Model needs-human flag recall

### Community 54 - "Day 1 · One model call: tokens, time and randomness"
Cohesion: 0.36
Nodes (8): Day 01 notebook (an-llm-call-is-http), ask(), Deep Dive into LLMs like ChatGPT (Karpathy), inference chapter, Ollama /api/chat endpoint, draft_cases(), Temperature, seed and randomness, Tokens in, tokens out and latency, Day 1 · One model call: tokens, time and randomness

### Community 55 - "_script"
Cohesion: 0.36
Nodes (6): _reply_turn(), _script(), _search_turn(), searches_every_step_and_after(), searches_every_step_then_replies(), searches_once_then_replies()

### Community 56 - "Ontology layer for Acme Fibre"
Cohesion: 0.13
Nodes (11): Business Graph Engine (graph computes, LLM verbalizes), Ephemeral per-case ABox (one customer), Phase 0 · Baseline audit, Phase 1 · Rich TBox schema, Static TBox (shared meaning, zero PII), pyoxigraph (in-process RDF store, SPARQL 1.1), issue_refund tool (data-changing, deferred), data/acme/ontology.ttl (+3 more)

### Community 57 - "studio-c3.yaml"
Cohesion: 0.12
Nodes (15): adapter, config, timeout_s, adapter, implementation, model, implementation, inputs (+7 more)

### Community 58 - "ReviewStore"
Cohesion: 0.17
Nodes (8): ReviewStore, score_rounds(), load(), test_dataset_banner_omits_run_progress_but_keeps_warnings(), test_provenance_uses_full_hashes_and_escapes_values(), test_reports_select_versions_and_keep_the_round_alias(), test_legacy_reviews_migrate_and_round_trip_through_excel(), test_snapshot_collection_preserves_runs_and_reviews()

### Community 60 - "config"
Cohesion: 0.15
Nodes (12): adapter, config, auth, endpoint, model, output_schema, provider, timeout_s (+4 more)

### Community 61 - "Rule 11 · Only the account holder can change the account"
Cohesion: 0.13
Nodes (20): acme:AccountAction requiresRole AccountHolder, acme:PuneServiceArea (8 areas), KB10 · Cancellation and notice period, KB12 · Shifting your connection, Account holder, Concession (refund, credit, waiver, discount value), Customer, Discount (also: सूट, छूट, ರಿಯಾಯಿತಿ) (+12 more)

### Community 63 - "compare_reviews"
Cohesion: 0.33
Nodes (4): compare_reviews(), score_regressions(), store_rev(), test_review_comparison_puts_new_missed_escalations_first()

### Community 68 - "test_holdout_run.py"
Cohesion: 0.29
Nodes (5): _fake_version(), _temp_root(), test_holdout_missing_file_prints_not_found_and_exits_0(), test_holdout_run_prints_no_case_id(), _two_holdout_cases()

### Community 69 - "versions.py"
Cohesion: 0.08
Nodes (14): Lab, _json(), _now(), RunStore, canonical(), case_hash(), digest(), lab_snapshot() (+6 more)

### Community 70 - "c3-agent.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 71 - "fixture"
Cohesion: 0.40
Nodes (4): runs(), semantic_data(), world(), world()

### Community 72 - "studio-offline.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 73 - "version-b.yaml"
Cohesion: 0.18
Nodes (10): adapter, config, model, provider, temperature, timeout_s, implementation, inputs (+2 more)

### Community 74 - "test_ontology.py"
Cohesion: 0.08
Nodes (35): data/acme/business_rules.json (commercial thresholds), outage_for(), load_business_rules(), _limit_context(), _record_facts(), compute_entitlements(), excluded_from_limit(), glossary() (+27 more)

### Community 75 - "test_guardrails.py"
Cohesion: 0.13
Nodes (13): email_from(), flags(), human_chooses(), lab(), model_drafts(), not_called(), outcome(), reason() (+5 more)

### Community 77 - "eval_checks"
Cohesion: 0.19
Nodes (13): chip(), customer_chips(), cur(), draft_meta(), email_card(), expected_card(), reply_card(), mark() (+5 more)

### Community 79 - "offline-direct.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 80 - "OrchestratedAdapter"
Cohesion: 0.08
Nodes (12): c3_output(), C3Provider, DeclarativeAdapter, OrchestratedAdapter, RecordedProvider, RedactingSerializer, Deps, Workflow (+4 more)

### Community 81 - "Acme labelled test set (cases.jsonl)"
Cohesion: 0.14
Nodes (14): Acme Review Studio, Acme_Fibre_Grounded_Draft_Eval.xlsx (eval workbook), import_cases.py (lab data → workbook), runs/ versioned persistence, Expert pass rate, Missed escalation, Round 1 Principal Engineer review of the Acme Fibre email drafting solution, Safe-send capture rate (new north-star metric) (+6 more)

### Community 83 - "Embedding model rubric (why embeddinggemma)"
Cohesion: 0.24
Nodes (6): qwen3:4b chat model (reads text only), Similarity search (cosine, top 3), embeddinggemma (EMBED_MODEL), Embeddings and retrieval, Hinglish handling, Recall@3 (retrieval metric)

### Community 85 - "run_agent"
Cohesion: 0.07
Nodes (31): Today: passive prompt glossary (LLM does the joins), Per-step agent trace, SYSTEM_C agent prompt, qwen3:4b local model (temperature 0), Act: does it hold on emails we never looked at?, Decide: which single fix matters most?, Observe: what does a pass rate hide?, Orient: have we seen this failure before? (+23 more)

### Community 86 - "test_cases_data.py"
Cohesion: 0.19
Nodes (8): cases_regional.jsonl (52 regional-language cases), cases(), _problems(), test_cases_match_the_customer_record(), test_labels_are_valid(), check(), test_language_label_matches_the_script(), test_regional_cases_carry_an_english_gloss()

### Community 87 - "pytest"
Cohesion: 0.15
Nodes (11): highlight(), icon(), meaning_card(), fact_rows(), origin(), pipeline(), case_header(), Elements (+3 more)

### Community 89 - "Review dashboard (when do humans help?)"
Cohesion: 0.17
Nodes (12): build_frame(), layer_of(), Code saves, Unneeded escalation, Where every case went (run → escalated/sent → right/missed/unneeded), Disagreement rates, What triggered the escalations (layer analysis), Escalation rate (+4 more)

### Community 92 - "review_record"
Cohesion: 0.17
Nodes (11): render_grade(), review_record(), sample_spread(), run_case(), _run_missing(), worker(), one(), _run_one() (+3 more)

### Community 95 - "test_expert_review.py"
Cohesion: 0.13
Nodes (17): tests/features/guardrails.feature (BDD guardrails), BDD policy specs, unasked_outage(), Feature: Escalation is reported as recall and precision, not just human_ok, Feature: The grader agrees with the expert's round-2 review, Scenario Outline: The retention offer is pre-approved (c44), Scenario Outline: The expert's verdict and the grader's agree, Feature: The area outage is in scope only when the customer reports that their service is down (+9 more)

### Community 99 - "rescore.py"
Cohesion: 0.50
Nodes (6): _approved_old(), _cases_by_id(), main(), _negated_old(), _one(), _run_before()

### Community 100 - "team-c3.yaml"
Cohesion: 0.17
Nodes (11): adapter, config, max_steps, model, provider, temperature, timeout_s, implementation (+3 more)

### Community 101 - "Scenario: OWL reasoner inherits class properties and respects overrides"
Cohesion: 0.22
Nodes (6): reason_owl_rl(), Scenario: OWL reasoner inherits class properties and respects overrides, check_inherited_props(), check_inherited_role(), check_override_false(), inspect_reasoned_ontology()

### Community 102 - "team-offline.yaml"
Cohesion: 0.20
Nodes (9): adapter, config, model, provider, timeout_s, implementation, inputs, label (+1 more)

### Community 104 - "judge_round1.py"
Cohesion: 0.10
Nodes (14): judge_prompt(), main(), work(), run_judge(), Build LLM judge from expert examples, Critique Shadowing workflow, Error analysis: error rates, patterns, specialised judges, Expert reviews data and errors are fixed (+6 more)

### Community 107 - "version_c3"
Cohesion: 0.29
Nodes (3): version_c3(), test_blank_or_cut_off_reply_is_never_sendable(), agent_finishes()

## Ambiguous Edges - Review These
- `version_b()` → `Failure category: unsupported-amount false positive`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `search_kb()` → `Similarity search (cosine, top 3)`  [AMBIGUOUS]
  1-measure-before-you-believe/06-one-llm-call/day6-embedding-compatibility.drawio · relation: semantically_similar_to
- `run_agent()` → `Failure category: unapproved offer`  [AMBIGUOUS]
  1-measure-before-you-believe/10-read-the-failures/notebook.ipynb · relation: references
- `Open question: can a learned classifier route escalations better? (project 3)` → `Roadmap claim: transformer classifier drops router latency from 500 ms to under 20 ms`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/presentation.md · relation: conceptually_related_to
- `Pitch claim: router adds under 500 ms and ₹0.10 per 1,000 emails` → `ADR-001 evidence table (day 9 runs)`  [AMBIGUOUS]
  1-measure-before-you-believe/11-recommendation-first-draft/pitch.md · relation: conceptually_related_to
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

## Knowledge Gaps
- **31 isolated node(s):** `fde-first-principles`, `KB03 · Payment methods`, `KB13 · Router and Wi-Fi password`, `Fixed monthly costs spread over all emails`, `Costs hidden inside today's estimate` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 553 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `server()` connect `Review Studio server` to `lab/version_d.py`, `._build`, `ontology.py`, `otel.py`, `versions.py`, `version_choices`, `judge_round1.py`, `test_ontology.py`, `eval_checks`, `Version`, `review_record`, `test_review_flow.py`, `RunResult`, `RunResult`, `pytest`, `ReviewStore`, `app.py`, `compare_reviews`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `server()` (e.g. with `.all()` and `version_token()`) actually correct?**
  _`server()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fde-first-principles`, `KB03 · Payment methods`, `KB13 · Router and Wi-Fi password` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `._build` be split into smaller, more focused modules?**
  _Cohesion score 0.09446693657219973 - nodes in this community are weakly interconnected._
- **Why does `policy_violations()` connect `policy_violations` to `lab/version_d.py`, `business_rules.py`, `ontology.py`, `test_grader_mutations.py`, `run_agent`, `Rule 2 · No exact outage fix time; share ticket ID`, `Rule 8 · ₹500 limit is per customer over 30 days`, `test_ontology.py`, `versions.py`, `policy_violations`, `Acme labelled test set (cases.jsonl)`, `RunResult`, `Safety router`, `Build a workflow, not an agent: B + safety router + policy verifier`, `Ontology layer for Acme Fibre`, `route`, `test_expert_review.py`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `version_b()` and `Failure category: unsupported-amount false positive`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `search_kb()` and `Similarity search (cosine, top 3)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._