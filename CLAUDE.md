# Rules for agents working in this repo

This repo is a product operating model toolkit: beliefs, model pages, templates, a checker (`bin/pom`) and agent commands. Read `BELIEFS.md` before doing anything substantive. It explains why the rules below exist. For OKR work also read `model/okrs.md` (KR types including guardrails, objective kinds, partners, check-in grades) and `model/maturity.md` (levels, uninstrumented teams).

## Who decides

- **Agents challenge; people decide.** You may review, ask, draft and propose. You may not approve.
- **Never edit a team's OKRs** (`objectives.csv`, `krs.csv`) or the strategy files (`strategy.md`, `product-strategy.md`). Write reviews and proposals next to them in `reviews/`.
- **`decision-log.md` is append-only.** You may append a decision only when a named person made it, and only after approval. Never edit or remove an entry.
- **Drafts in `reviews/` may be written without approval**: they are proposals, and people decide what to do with them. Every other write needs approval after you show the exact text or rows. `CHATGPT.md` applies the same rules.
- **Intake drafts go in `reviews/intake/`.** When reading a company's existing strategy documents or OKR sheets (`model/intake.md`), draft there only. The team or strategy owner copies rows into the real files themselves. Leave gaps blank, never turn a status word into a confidence colour, and never set a start confidence or a maturity level.
- `checkins.csv` is append-only. Show proposed new rows and obtain approval before appending; never rewrite or delete old check-ins.
- For `actions.csv`, show proposed new blocker rows and obtain approval before appending. Existing action rows may be updated **only** in `owner`, `status`, `answered` and `answer`, and only after approval. Never change an action's ID, original date, team or blocker text; never delete an action. Git history preserves the old state.

## Evidence

- Every number carries a grade: **A** measured, **B** reported, recalled or sampled, **C** estimated now, **?** unknown. No C-grade number is presented as an outcome.
- In `checkins.csv`, fill `evidence_grade` only when you know how the value was obtained; otherwise leave it blank and say so. Never guess a grade. `bin/pom report` marks C and ? values as estimates.
- Don't invent numbers, names, dates or quotes. If something is missing, say it is missing.
- Frozen predictions (`start_confidence`, hypotheses written before the term) are never edited after the term starts.
- Be stricter with conclusions that flatter the team, the leader or the strategy.

## Stance by maturity

Read each team's level in `pom.json` and follow `model/maturity.md`: listen at 0, coach at 1, challenge at 2, adversarial at 3. The level is never a score; never rank teams or assess individuals.

## Confidentiality

- Use only an AI environment the company has approved for its data.
- The public toolkit repository holds no company data. Company workspaces live in the company's private copy.
- Company data in a workspace stays in that workspace. Don't copy it into other repos, prompts for third-party services or public places.
- Examples in `examples/` are fictional and must stay fictional. Don't add real company names, people or figures to them.
- `sources.md` credits frameworks by others. Paraphrase them; don't paste their text.

## Checks

```
python3 -m unittest discover -s tests
bin/pom check <workspace> [--today YYYY-MM-DD]
bin/pom report <workspace> [--today YYYY-MM-DD]
```

Run the tests after any change to `bin/pom`. Keep `bin/pom` standard-library only.
