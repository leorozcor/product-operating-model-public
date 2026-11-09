# Product operating model toolkit

A concept-stage toolkit for running product strategy, OKRs, gembas and term reviews, and for feeding what teams learn back into strategy. It is plain files (Markdown, CSV, JSON), a small checker, and agent commands for Claude Code. Nothing is tied to a vendor tool.

**Status:** concept stage (phase 1). Not yet used in a real company. Expect to adapt it.

**Public edition.** This repository is the public edition of a toolkit that is maintained privately. It gets updates in periodic releases, later and in batches, not continuously.

**Keep company data out of this public repository.** Copy it into a private repository inside the company and keep workspaces, OKRs and strategy there. The public edition ignores `workspace/` by default; a company that wants to version-control its workspace should deliberately remove that ignore entry in its private fork.

**Before publishing an update:** Review new files, examples, code, tests and commit history for confidential documents, real employer or client figures, private people, secrets, and descriptions that could identify or judge a former employer. Replace these with independent fictional examples or neutral diagnostic questions. Check third-party attribution and permissions. Removing a line in a later commit does not erase the earlier public history.

## Start here

**New here? Read [HOW_TO_USE.md](HOW_TO_USE.md)**: the whole thing step by step, from copying the repo into a company to the end of the first year.

1. **[BELIEFS.md](BELIEFS.md)**: what this model assumes about product organisations, labelled principle, hypothesis or heuristic. Read it with the leadership team before installing anything.
2. **[model/loop.md](model/loop.md)**: the loop, who owns each step, and the rules that hold across it.
3. The other model pages:
   - [diagnose.md](model/diagnose.md): what to learn before introducing anything
   - [strategy-cascade.md](model/strategy-cascade.md): strategy down to initiatives and learning back up; strategic, tactical and operational work
   - [okrs.md](model/okrs.md): narratives; outcome, commitment and stretch KRs; initiatives
   - [gemba-and-cadence.md](model/gemba-and-cadence.md): terms and the 15-minute gemba
   - [term-review.md](model/term-review.md): the term review and the strategy update
   - [maturity.md](model/maturity.md): OKR maturity levels 0 to 3 and what changes at each
   - [teams-and-dependencies.md](model/teams-and-dependencies.md): team decision boundaries, cross-functional partners and dependency agreements
   - [discovery-and-evidence.md](model/discovery-and-evidence.md): turning product risks and initiatives into credible learning
4. **[examples/fictional/](examples/fictional/)**: a made-up company mid-term, to see everything working.

## The loop

```
Diagnose ─► Strategy ─► Term OKRs ─► Gembas ─► Term review ─► Strategy update ─┐
              ▲                                                                 │
              └──────────────────────────── evidence ◄───────────────────────────┘
```

## Deploying it in a company

1. Copy this repo into the company's own repository. The examples are fictional and can stay.
2. Read `BELIEFS.md` with leadership and mark each belief: *we hold this*, *we don't*, or *we'll test it*. Record the result in a `decision-log.md`.
3. Diagnose for a few weeks with `templates/diagnosis.md` (see `model/diagnose.md`). Decide each team's maturity level from what you observe.
4. Create a workspace folder for the term, for example `workspace/2027-T1/`, and copy the templates into it: `pom.json`, `strategy.md`, `product-strategy.md`, `objectives.csv`, `krs.csv`, `checkins.csv`, `actions.csv`, `health.csv`, `kpi-definitions.csv`, `decision-log.md`. Set the term dates in `pom.json`; nothing else holds dates, so a copied workspace can't carry an old term's calendar.
5. Teams draft OKRs. Run `bin/pom check workspace/2027-T1` and `/okr-review workspace/2027-T1 <team>`.
6. Run gembas. Use `/gemba … prepare` before and `/gemba … record` after. Management answers blockers in `actions.csv`.
7. At the end of the term, run `bin/pom report … --today <end date>` and `/term-review … <team>`. Leadership records strategy decisions in `decision-log.md`.

## AI assistants

The core model, templates and Python checker work without an AI assistant. Claude Code commands live in `.claude/commands/`; ChatGPT can follow the same workflows using [CHATGPT.md](CHATGPT.md), without assuming Claude slash commands are available. Use only a company-approved AI environment for company data.

## Tools

| Tool | What it does | Edits files? |
|---|---|---|
| `bin/pom check <workspace> [--today D]` | Checks an OKR set: narratives, orphans, KR types, baselines and the baseline window, output-like KRs, commitment share by maturity, guardrails on migrations, measurement for uninstrumented teams, partner teams, cadence | No |
| `bin/pom report <workspace> [--today D]` | Confidence trends, values with evidence grades, estimated results, watermelon candidates, stalled yellows, overdue commitments, blockers answered before the next gemba, health breaches, maturity signals | No |
| `/okr-review <workspace> <team>` | Reviews draft OKRs at the stance the team's maturity calls for | Writes a review in `reviews/` |
| `/gemba <workspace> <team> prepare\|record` | A facilitator brief, or a gemba note and new rows from notes | Prepare: no. Record: approved additions and existing action-status updates only |
| `/term-review <workspace> <team>` | Drafts the term review and proposed strategy changes | Writes a draft in `reviews/` |

Agents never edit a team's OKRs or the strategy. See [CLAUDE.md](CLAUDE.md) for shared safeguards and [CHATGPT.md](CHATGPT.md) for the ChatGPT adapter.

```
python3 -m unittest discover -s tests            # checker tests
bin/pom check examples/fictional --today 2027-03-29
bin/pom report examples/fictional --today 2027-03-29
```

Python 3.9 or later, standard library only.

## Phase 2 (not built)

`/diagnose`, `/strategy-challenge` and `/strategy-update` commands, and an automated runner for the behavioural evals in [evals/](evals/).

## Credits

The toolkit is inspired by a number of private and public sources. See [sources.md](sources.md): frameworks by others are paraphrased and credited; examples are fictional.

## Licence and attribution

- **Text, models, templates, examples and evals:** [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0).
- **Code** (`bin/pom` and `tests/`): [MIT](LICENSE-CODE).

Copyright (c) 2026 Luis Orozco. When you reuse or adapt the text, credit it like this, and say whether you changed it:

> Based on the Product Operating Model toolkit by Luis Orozco (https://github.com/leorozcor/product-operating-model-public), licensed under CC BY 4.0.

Frameworks by others credited in [sources.md](sources.md) remain theirs and are not covered by these licences.
