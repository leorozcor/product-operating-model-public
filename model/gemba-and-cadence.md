# Gembas and term cadence

*Serves: 2.7 gembas build trust between layers; 2.5 make uncertainty visible before failure.*

## Terms, not quarters

A term is the period an OKR set covers. It runs from a quarter to six months; **four months is the default** (three terms a year). Fit it to the company's planning and budget cadence, not the other way round.

## The gemba

"Gemba" means the place where the work happens. A gemba is an inspection of the work, **not a reporting meeting**. It is short, team-led, and in front of the team's own board.

- **Length:** 10 to 15 minutes.
- **Cadence:** weekly, or at the end of every sprint. Monthly works only with short terms (see below).
- **Who:** the team presents; their manager and someone who can act on cross-team blockers attend.

The team answers three questions:

1. **What did we achieve or learn** since the last gemba? Include check-ins on the KRs.
2. **Which hypotheses do we test next?**
3. **What blocks us**, especially what we can't solve ourselves: coordination with other teams, resourcing, competing priorities, input from other parts of the organisation.

## Management's half of the deal

- Every blocker raised goes into `actions.csv` with an owner on the management side.
- Management works on it **before the next gemba** and **always answers**, even if the answer is "we don't know, park it". A parked item counts as answered; silence does not.
- The share of blockers answered before the next gemba is reported every term. It is a trust signal and it measures management, not the team.

Over enough cycles this speeds up learning and builds trust, because the team knows it will get an answer.

## Cadence checks

| Situation | Why it matters |
|---|---|
| Monthly gembas with six-month terms | Only about six gembas a term. A blocker raised in month one can wait a month for an answer, and a watermelon can stay hidden for most of the term. Consider shorter terms or a lighter fortnightly gemba. |
| Terms shorter than ~10 weeks | Little time for outcome KRs to move; teams drift to commitments. |
| Terms longer than ~6 months | Hypotheses go stale before they are tested. |

`bin/pom check` warns about these.

## What a gemba is not

- Not a status update for management. If people prepare slides, it has become one.
- Not a place to assign blame for a red. Red is information.
- Not a planning session. Decisions that need more than a few minutes get their own slot.
