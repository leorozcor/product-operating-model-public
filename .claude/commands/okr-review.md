---
description: Review a team's draft OKRs for the coming term, at the stance its maturity level calls for
argument-hint: <workspace> <team-id>
---

You are reviewing draft OKRs for team `$2` in the workspace `$1` (default: the current folder). Read `CLAUDE.md` and `BELIEFS.md` first if you have not.

## Steps

1. Read `pom.json` and find the team's maturity level. If the team is missing, stop and say so.
2. Run `bin/pom check $1` and keep its findings for this team. They are mechanical. Don't repeat them one by one; group them.
3. Read the team's rows in `objectives.csv` and `krs.csv`, plus `strategy.md` and `product-strategy.md`.
4. Review at the stance for the team's level (see `model/maturity.md`):
   - **Level 0, listen.** Don't critique the OKRs. Ask up to five questions about how the team decides what to work on and what it would need to try outcome KRs. Point to `model/diagnose.md`.
   - **Level 1, coach, never grade.** Pick the **one or two** changes that would help most, explain why in plain words, and show a rewritten example for one KR. Milestone KRs are fine if labelled as commitments. If the team is not instrumented, the most helpful change is usually a *measure* commitment.
   - **Level 2, challenge.** Go through each objective: is the narrative enough for an outsider? Which outcome KRs are outputs in disguise? Which baselines are graded C or ?, and can they be measured before the term? Is the commitment share above the level's limit? Are there shared KRs with other teams, and are the partners named in `partners`? Does each platform or migration objective have a guardrail?
   - **Level 3, adversarial.** Do all of level 2, then argue the other side: what result would show the strategy hypothesis is wrong, and does any KR measure it? Which KR could be hit without the objective being true? Where is the plan flattering? Ask for frozen start confidences on every KR.
5. For every objective, check the link up: which strategy hypothesis does it serve? If none, say whether you think the strategy or the objective is missing something.
6. Write the review to `reviews/<term>/<team>-okr-review.md` in the workspace with: a three-line summary, the findings grouped by objective, the questions for the team, and the `bin/pom check` output in a collapsed section at the end.

## Rules

- **Never edit `objectives.csv`, `krs.csv` or any strategy file.** Suggest rewrites in the review; the team decides.
- Never grade the team or compare it with other teams. The maturity level is not a score.
- Don't invent numbers. If a baseline is missing, say it is missing; don't propose one unless the data is in the workspace, and then grade it.
- Be kind, not nice: plain, specific, no padding, no blame.
- Keep the review under one page at levels 0 and 1.
