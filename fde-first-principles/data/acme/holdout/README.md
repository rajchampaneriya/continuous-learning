# Holdout set

Written by a person, never by the coding agent. Cases here are never opened, printed, grepped
or summarised by the agent; runners only load the file, score it and print the aggregate.

## File

`cases_holdout.jsonl` — one JSON object per line, same schema as `data/acme/cases*.jsonl`:

- `id` — unique, prefix `h` (e.g. `h01`)
- `customer_id` — an id from `data/acme/customers.json`
- `message` — the customer's email
- `expected_intent` — one of billing, outage, speed, cancel, upgrade, relocation, other
- `must_include` — substrings a correct reply must contain
- `must_not` — substrings a correct reply must never contain
- `needs_human` — true when a person must see the email
- optional, as in the other suites: `kb_sources`, `language`, `message_en`, `history`,
  `thread_id`, `concession_allowed`, `twin_of`, `tags`, `difficulty`, `rationale`,
  `escalation_rule`, `reviewed`

## Rules

- About 40 cases.
- Roughly half need a person (`needs_human: true`).
- At least 8 in regional languages (with `language` and `message_en` set, as in
  `cases_regional.jsonl`).
- At least 6 paired variants: the same situation as an `a` case (answerable) and an `h`
  case (needs a person), linked with `twin_of`, as the abuse suite does.
- Not in git (`*.jsonl` here is gitignored). Run with `--holdout`:

      uv run python -m lab.run_c4 --version C4-glm53flash-r2 --holdout
      uv run python -m lab.run_d --version D5-glm53flash --holdout

  Each prints the aggregate summary only — no case ids, no replies — and saves
  `data/results/<version>-holdout.jsonl`.
