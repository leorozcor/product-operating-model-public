# OKRs: narratives, key results and initiatives

*Serves: 3.1 what, why, for whom and how we'll know; 3.2 outcomes over outputs; 1.5 control the conditions.*

This page adapts Ravi Mehta's Narratives, Commitments and Tasks to OKRs. In this toolkit "tasks" are called **initiatives**.

## The shape of an objective

Each objective has:

- **The objective**: one sentence, qualitative, about a change for customers or the business.
- **A narrative**: a short paragraph that keeps the context in front of everyone. Why this, why now, for whom, what we believe, and what we are not doing. A reader who wasn't in the planning meeting should understand the objective from the narrative alone.
- **The strategy hypothesis it serves** and **the top-level metrics** it should move.
- **Two to four key results**, each of one type (below).
- **Initiatives**: the team's current best guesses about how to move the KRs. They can change any time without changing the OKR.

## Three kinds of key result

| Type | What it is | How it is tracked | Example |
|---|---|---|---|
| **Outcome** | A measurable change in behaviour or results. Probabilistic: the team may miss it while doing everything right. | Value against baseline and target, plus confidence each check-in. | Share of jobs completed on first visit from 61% to 70% |
| **Commitment** | Something the team will do by a date. Deterministic. Used when the objective can't be measured yet, or the work truly is a must-do. | Done or not done by the due date. Kind: *think it* (a decision or design), *build it*, *launch it*, or a *date*. | Move all customers to the new billing platform by 30 April |
| **Stretch** | An outcome KR the team doesn't expect to hit. Flagged so nobody is punished for missing it. At most one per objective. | Like an outcome. | Weekly active technicians from 4,000 to 6,000 |
| **Guardrail** | A metric that must stay inside a limit during the term, usually while something risky happens. `target` is the limit. | Value and confidence each check-in. | Weekly active accounts stay within 2% of January during the migration |

Commitment kinds: *think it* (a decision or design), *build it*, *launch it*, a *date*, or *measure* (we can see the outcome we care about, for a team that can't measure it yet; see `maturity.md`).

## Kinds of objective

Each objective has a `kind` in `objectives.csv`:

- **product** (default): changes customer or business behaviour. Commitments count toward the team's commitment share.
- **platform** or **migration**: rebuilding or moving something. Commitments are the honest form here and don't count toward the commitment share, but the objective needs **at least one guardrail or outcome KR**, so the move can't quietly cost customers. (A migration is a withdrawal from users' goodwill; the guardrail checks the balance.)
- **statutory**: legal or regulatory change with a fixed date. Commitments don't count toward the share. Ongoing compliance (for example "security findings fixed in time") belongs in health metrics, not OKRs, unless it is breached.

## Shared key results

When another team shares a KR or has to supply part of it, name it in `partners` (separated by `;`). `bin/pom report` lists shared KRs so each gemba can ask whether the partner teams have the work in their plans. Unplanned partner work is one of the most common blockers.

Rules of thumb:

- An outcome KR that starts with a verb like *launch*, *build* or *deliver* is probably an output. Rewrite it as the change you expect, or make it an honest commitment. `bin/pom check` flags these.
- An outcome KR needs a baseline, a target, a unit, a check-in cadence, an owner and an evidence grade for the baseline. A C-grade baseline is a reason to measure before the term starts.
- **Baselines have a deadline.** `baseline_due` in `pom.json` (default three weeks into the term). After it, an outcome KR without a baseline is an error at every level: measure it, or turn it into a *measure* commitment. Define each metric once in `kpi-definitions.csv`.
- **All commitments met with no initiatives done is a win.** Initiatives are hypotheses, not promises.
- Commitments are useful and also a maturity signal. A high share of commitments is fine for a team introducing OKRs, a warning for a practising team and a red flag for a learning team. It often means the team is being managed as a delivery unit.
- **Caution:** 100% commitments combined with low trust tends to produce sandbagging: teams promise only what they are sure to deliver.

## The chain

```
Objective ─► Key results ─► Initiatives ─► Insights
   why          how we'll know    what we try      what we learned (fed back at gembas and the term review)
```

## Check-ins

Each outcome KR gets a check-in at its cadence, usually at the gemba: the current value, its evidence grade (A measured, B reported, recalled or sampled, C estimated, ? unknown), a confidence colour and one line of note. A value graded C or ? is an estimate: `bin/pom report` marks it and asks for a measurement before the term review, because no estimate is reported as an outcome. From maturity level 2, the checker warns when a measured KR's value has no grade.

- **Green**: we expect to hit it.
- **Yellow**: at risk; we know what we are changing.
- **Red**: we don't expect to hit it unless something changes, often something outside the team.

A yellow is healthy. Two yellows in a row with no change of plan is not. A green that is far behind its glidepath late in the term is a watermelon candidate.
