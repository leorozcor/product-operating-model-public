# OKR maturity

*Serves: 2.2 trust distributes judgment; 1.4 soil before water.*

Teams don't all start in the same place. The toolkit changes what it asks for, and how hard the agents push, according to each team's maturity level. **OKR maturity can't outrun trust**: don't move a team up a level because the calendar says so.

Maturity is **judged per team, observed and not self-declared**, and recorded in `pom.json`. It is never used to rank teams.

| Level | Name | What the team does | What the toolkit asks | Agent stance |
|---|---|---|---|---|
| 0 | Roadmap-driven | Delivers a roadmap of features; success is shipping on time. | Diagnose only. At most one pilot team tries OKRs. | **Listen.** Ask questions, don't critique. |
| 1 | Introducing | Writes OKRs for the first terms; many KRs are milestones. | Narratives, at most three objectives, a top metric per objective. Milestone KRs are allowed if labelled as commitments. | **Coach, never grade.** Explain one improvement at a time. |
| 2 | Practising | Outcome KRs with baselines; check-ins at gembas. | Full KR checks, shared KRs between teams, glidepaths, health metrics. | **Challenge.** Push on outputs disguised as outcomes and on weak evidence. |
| 3 | Learning | OKRs test strategy; results change the strategy. | Frozen hypotheses, predictions against results, strategy updates, explicit bets. | **Adversarial.** Argue the other side, look for flattering conclusions. |

## Signals to look at (listed, not scored)

- Share of outcome KRs with a baseline, a target and a cadence.
- Share of outcome KRs versus commitments.
- How early in the term the first yellow or red appears. Late is a warning.
- How often initiatives are changed or stopped during the term. Never is a warning.
- Whether the product strategy changed after the last term review.
- Share of blockers management answered before the next gemba.

`bin/pom report` lists these per team. A person decides the level.

## When the product can't be measured yet

Some companies have almost no product instrumentation: they can count releases and pull requests, but not what customers do. OKRs are then a lever to build measurement, and the first term should say so.

- Mark the team `"instrumented": false` in `pom.json`.
- Give it one or more *measure* commitments: "we can see weekly completed jobs per customer by week 6".
- `bin/pom check` then waives baselines for that team and warns if it has no measure commitment.
- Once measurement exists, set `instrumented` back to true and the normal baseline rules apply from the next term.

A team at level 1 with no instrumentation is not failing. It is doing the work that makes level 2 possible.

## Diagnostic patterns (illustrative)

These are hypothetical situations to help teams ask better questions. They are not case studies or evaluations of a current or former employer.

- **Guidance and practice may diverge.** Compare the intended OKR approach with actual team objectives and check-ins. If many KRs describe deliverables, coach toward outcomes rather than treating a written standard as evidence of maturity.
- **Templates are not learning loops.** Ask whether teams discuss results, what surprised them, and what changed afterwards. A completed spreadsheet alone doesn't establish learning.
- **Status and confidence answer different questions.** Ask not just whether a KR is "on track" but how confident the team is, and what new evidence would change that confidence.
- **Migrations may require commitments.** Pair necessary milestones with customer-value or product-health guardrails.
- **Qualitative learning matters before instrumentation.** Capture trade-offs, unknowns and changes of mind while teams build reliable measurement.
- **Pilots do not define organisational maturity.** Observe whether practices survive beyond a single team or champion before scaling them.

## Commitment share by level

`bin/pom check` warns when the share of commitments among a team's KRs is above these defaults (change them in `pom.json`). KRs under platform, migration and statutory objectives don't count; see `okrs.md`.

| Level | Warn above |
|---|---|
| 0 or 1 | no limit |
| 2 | 50% |
| 3 | 30% |
