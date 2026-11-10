# Using this toolkit with ChatGPT

This is the ChatGPT counterpart to `.claude/commands/`. It uses the **same operating model, workspace files, Python checker and human decision rights**. It is not a second version of the framework.

## Before using company material

Use only a ChatGPT environment and GitHub connection approved by the company for the information being processed. A private GitHub repo does not, by itself, establish that sending its content to an AI service is permitted. Do not copy company workspaces to a personal repository or paste secrets, personal data or confidential third-party material into an unapproved account.

ChatGPT does not automatically execute Claude Code slash commands or necessarily read this file when a conversation begins. In a company-approved ChatGPT Project, provide the instructions below and explicitly ask it to read the live repository files. If GitHub or a local file tool is unavailable, supply the minimum relevant files or work from a dated extract; state that the result is not verified against the live repo.

## Project instruction to copy

> You are assisting with this company's Product Operating Model toolkit. First read the current `README.md`, `BELIEFS.md`, `CHATGPT.md`, `CLAUDE.md`, `model/loop.md`, `model/okrs.md`, `model/maturity.md` and other task-relevant model pages from the company's private copy of this repository. The company workspace, not your memory, is the source of truth. Apply the same human-approval, evidence, maturity and confidentiality rules irrespective of AI provider. Challenge and draft; never decide for a team or leadership. Drafts in `reviews/` may be written without approval because they are proposals, not decisions; say where you wrote them. Before any other file write, show the exact proposed change and wait for explicit human approval. If file or shell access is unavailable, give a review or patch and say what you could not verify.

## Shared rules

- **People decide.** Never modify `objectives.csv`, `krs.csv`, `strategy.md` or `product-strategy.md`. `decision-log.md` is append-only: append a decision only when a named person made it, after approval, and never edit or remove an entry. Reviews and proposals belong in `reviews/`.
- **Review drafts are free; everything else needs approval.** Drafts in `reviews/` (OKR reviews, term reviews) may be written without approval: they are proposals, and people decide what to do with them. Every other write, including gemba notes, new CSV rows and management-action updates, needs explicit approval after you show the complete text or exact rows. These are the same rules Claude follows in `CLAUDE.md`.
- `checkins.csv` is append-only. Add new blockers to `actions.csv`; an existing action may have only its `owner`, `status`, `answered` and `answer` fields updated after approval. Do not change its identity, raised date, team or original blocker. Git history records changes.
- Grade evidence: **A** measured; **B** reported, recalled or sampled; **C** estimated; **?** unknown. Never present an estimate as an observed result. In `checkins.csv`, fill `evidence_grade` only when you know how the value was obtained; otherwise leave it blank and say so. `bin/pom report` marks C and ? values as estimates. Do not invent figures, names, dates, quotations or causality. Preserve predictions frozen at the start of the term.
- **Intake drafts only.** When reading existing strategy documents or OKR sheets, write drafts in `reviews/intake/` and nowhere else; the team copies rows into its files. Leave gaps blank, keep status words out of the confidence field, and never set start confidences or maturity levels.
- Read each team's maturity level from `pom.json` and use `model/maturity.md`: **listen** at 0, **coach** at 1, **challenge** at 2, **adversarially test assumptions** at 3. Never rank teams or assess individuals.
- Do not assume tools ran. If shell execution is available, use `python3 -m unittest discover -s tests` after code changes and `bin/pom check <workspace>` / `bin/pom report <workspace> [--today YYYY-MM-DD]` for analysis. Otherwise show the commands for a person to run and distinguish observed results from unverified expectations.

## Five equivalent workflows (plain-language prompts)

**Review OKRs:** “Review `<workspace>` for team `<team-id>` using `.claude/commands/okr-review.md` as the workflow specification. Use the team's maturity stance, the checker output if available, and the strategy files. Write the draft to `reviews/<term>/<team-id>-okr-review.md`, show it, and do not edit the OKRs.”

**Prepare a gemba:** “Prepare a one-screen facilitator brief for `<team-id>` in `<workspace>`, following `.claude/commands/gemba.md` in `prepare` mode. Use current KR trends, management blockers and no more than three useful questions. Read-only; do not write.”

**Record a gemba:** “Using these facilitator notes, follow `.claude/commands/gemba.md` in `record` mode for `<team-id>` in `<workspace>`. Show the proposed gemba note, `checkins.csv` additions, `actions.csv` additions and any updates to existing actions. Include each value's evidence grade only when the notes say how it was obtained. Wait for approval before writing; leave unknown values blank.”

**Bring in existing documents:** “Following `.claude/commands/intake.md` and `model/intake.md`, read `<source files>` (mode `strategy` or `okrs`) and draft workspace files for `<workspace>` in `<workspace>/reviews/intake/`, with a `source` column on every drafted row and an intake report from `templates/intake/`. Copy wording as written, leave every gap blank, don't turn status words into confidence colours, and don't write any other file.”

**Review a term:** “Draft the term review for `<team-id>` in `<workspace>` following `.claude/commands/term-review.md`. Compare outcomes to the frozen forecast, use each result's latest check-in grade (say when it is unknown), expose contrary findings and propose up to three strategy changes. Write the draft to `reviews/<term>/<team-id>-term-review.md` and show it; do not edit strategy or the decision log.”

These Claude command files are **workflow specifications**, not commands ChatGPT can invoke as slash commands. The same templates and `bin/pom` remain usable with no AI assistant at all.

## Verify and hand off

After an approved write, read back the edited file, run relevant checks when available, and report exact paths and Git commit/PR links only when observed. If no write access is available, provide the patch rather than suggesting it was saved. Keep drafts concise and label assumptions, unknowns and human decisions clearly.
