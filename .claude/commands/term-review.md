---
description: Draft a team's end-of-term review and the proposed strategy changes for leadership
argument-hint: <workspace> <team-id>
---

Workspace: `$1`. Team: `$2`. Read `model/term-review.md` and `BELIEFS.md` (section 4) first.

## Steps

1. Run `bin/pom report $1 --today <term end date from pom.json>` and keep this team's lines.
2. Read the team's objectives, KRs, check-ins, gemba notes, actions and the strategy files.
3. Draft `reviews/<term>/<team>-term-review.md` from `templates/term-review.md`:
   - **Results against frozen predictions.** Use `start_confidence` from `krs.csv` as the frozen forecast. Show each result with the evidence grade from its latest check-in (`evidence_grade` in `checkins.csv`; if blank, say the grade is unknown). **No C-grade number is presented as an outcome**: say "estimated" and why.
   - **What we learned**: only from gemba notes and check-in notes. Where the record is thin, say so instead of filling in.
   - **Hypotheses tested**: for each strategy or product hypothesis the team's objectives served, mark stronger, weaker or untested, with the evidence. Be stricter with conclusions that flatter the team or the strategy.
   - **Blockers and answers** from the report.
   - **Capacity split**: leave blank for the team to fill in unless the notes say.
   - **Proposed strategy changes**: at most three, each linked to evidence. These are proposals.
   - **Maturity signals**: copy the report's row. Don't propose a new level; list what changed since last term.
4. List the watermelon candidates and late first non-greens as questions for the retrospective: was the risk visible earlier, and what made it hard to say?
5. Show the draft and say what is missing. The team edits and owns it.

## Rules

- **Never edit `strategy.md`, `product-strategy.md` or `decision-log.md`.** Leadership decides on proposed changes and records them there.
- Never rewrite a frozen prediction to match the result.
- Never rank teams.
- If a whole term of evidence suggests no change to the strategy at all, say that this is itself worth discussing.
