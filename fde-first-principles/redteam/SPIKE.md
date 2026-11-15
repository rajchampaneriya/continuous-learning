# R0 spike — PyRIT 1.1.0 around Version D

Run: `LLM_MAX_CALLS=40 uv run --group redteam python -m redteam.spike`
(2026-11-15, agent `D` = version_d on glm-5.3-flash, attacker glm-5.3-flash
through the lab's anthropic route, persona AC1013 Neha Kale.)

Result: five single-turn `PromptSendingAttack` sends and one three-turn
`RedTeamingAttack` completed the full loop — attacker → target → agent →
scorer → verdict. Every attack ended `FAILURE`: the agent handed off or
refused, no unattended violation. Raw rows: `data/redteam/r0-spike/spike-rows.json`.

## The six questions

**1. Which method does a custom true/false scorer implement?**
`_score_piece_async(self, message_piece, *, objective) -> List[Score]` on a
subclass of `pyrit.score.true_false.true_false_scorer.MessageTrueFalseScorer`.
The constructor passes `score_aggregator=TrueFalseScoreAggregator.OR` and
`validator=ScorerPromptValidator(supported_data_types=["text"])`, and
`_build_identifier` returns `self._create_identifier(params={...},
score_aggregator=self._score_aggregator.__name__)`. `Score` needs
`score_value=str(bool)`, `score_type="true_false"`, `score_category=[...]`,
and `score_metadata=None` — a string there fails pydantic validation.

**2. Can a scorer read the conversation id, to find the logged row?**
Yes. `message_piece.conversation_id` on the assistant piece the target
returned is the same id the target stamped into that piece, so it keys
straight into the lab's row log. Proven on all six conversations.

**3. Does the refusal scorer stop or backtrack RedTeamingAttack and Crescendo?**
Not in 1.1.0. Both `PromptSendingAttack` and `RedTeamingAttack` print
`refusal_scorer was provided in AttackScoringConfig but is not used. This
parameter will be ignored.` The loop stops only on the objective scorer.
Consequence: hand-off refusal signal must come from our own scorer or the
run log, never from pyrit's refusal wiring.

**4. Does Crescendo accept this target, and which capabilities does it need?**
The constructor requires the objective target to natively support
`EDITABLE_HISTORY` and `MULTI_TURN`; `AcmeAgentTarget` declares both and is
accepted (checked against the installed source; Crescendo itself not run in
the spike). It does not require `supports_system_prompt` on the objective
target — only the adversarial target needs that.

**5. Can PyRIT's attacker target reach your attacker endpoint?**
`OpenAIChatTarget` reaches z.ai's OpenAI route but that route is unfunded —
every call returns 429 `Insufficient balance or no resource package. Please
recharge.` The lab's balance sits on the anthropic route, so the attacker
runs through `LabLLMTarget`, a `PromptTarget` wrapping `lab.llm.chat` with
`model="anthropic:<name>"`. The RedTeamingAttack attacker wrote three
coherent fraudulent emails this way. It declares `supports_multi_turn`,
`supports_editable_history` and `supports_system_prompt` — all three are
required to be allowed an adversarial system prompt.

**6. How are memory labels set and exported?**
Per attack call: `execute_async(objective=..., memory_labels={...},
next_message=...)` — flat kwargs, no `params` envelope. Memory goes through
`CentralMemory.set_memory_instance(SQLiteMemory(db_path=...))` set once per
process; the sqlite file under `data/redteam/<run>/` is the export and stays
git-ignored. Reported numbers come from the lab's own `turns.jsonl` (R2),
never from pyrit's copy of the text.

## Go or no-go

**Go.** The objective scorer found the logged row by conversation id and
steered the loop (every outcome was its verdict), and the attacker endpoint
works through `LabLLMTarget`. One deviation carried into R2: ignore
`refusal_scorer`; compute hand-off verdicts from the logged `needs_human`.

## pyrit 1.1.0 API notes (docs are stale)

- No `initialize_pyrit`, no `pyrit.orchestrator`. Attacks live in
  `pyrit.executor.attack.single_turn.prompt_sending` and
  `pyrit.executor.attack.multi_turn.{red_teaming, crescendo, pair, tree_of_attacks}`.
- Custom targets subclass `PromptTarget` and override
  `_send_prompt_to_target_async(*, normalized_conversation: List[Message])
  -> List[Message]`; `send_prompt_async` is `@final`. Keyword-only `__init__`.
- Conversations arrive as `List[Message]`, flattened with
  `m.message_pieces`; the target returns
  `[MessagePiece(role="assistant", original_value=..., converted_value=...,
  conversation_id=...).to_message()]`.
- Configs: `AttackScoringConfig(objective_scorer=, refusal_scorer=,
  auxiliary_scorers=)`, `AttackAdversarialConfig(target=, system_prompt=)`.
- `RedTeamingAttack`'s adversarial target must natively support system
  prompts; giving it one also requires multi-turn + editable history.
