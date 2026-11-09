# Strategy cascade, both ways

*Serves: 4.1 strategy and OKRs refine each other; 4.2 strategy is a set of falsifiable bets; 3.11 strategic impact is explicit.*

## Down: from purpose to initiatives

```
Purpose and vision                    why we exist; changes rarely
  └─ Company strategy (multi-year)    where we play and how we win
       └─ Product strategy            the product bets that deliver it; reviewed every term
            └─ Yearly objectives      what must be true by the end of the year
                 └─ Term OKRs per team    outcomes for this term, with KRs
                      └─ Initiatives      hypotheses about how to move the KRs

Alongside, not inside:  operational health (health metrics, SLAs, BAU), monitored against limits
```

Every term objective names the strategy hypothesis it serves (`strategy_hypothesis` in `objectives.csv`). An objective that serves no hypothesis is an orphan: either the strategy is missing something or the objective is not strategic. Both are worth knowing.

## Up: from the work back to strategy

1. **Gembas** surface learning and blockers every week to month. Management answers blockers before the next gemba.
2. **Term reviews** test the term's frozen hypotheses against results and say which strategy hypotheses got stronger, weaker or untested.
3. **Strategy updates** happen once a term. Leadership accepts, rejects or parks each proposed change in `decision-log.md`, with the evidence grade behind it. The company strategy changes less often, but only with evidence.

If a full year passes and the product strategy has not changed at all, the term reviews are not reaching leadership. Treat that as a finding.

## Strategic, tactical, operational

These definitions are a proposal for this toolkit, not a standard. Adapt them to the company's language.

| Kind | What it is | Where it lives | How it is judged |
|---|---|---|---|
| **Strategic** | Choices about where we play and how we win, written as falsifiable hypotheses with a horizon | `strategy.md`, `product-strategy.md` | Did the evidence over several terms support the bet? |
| **Tactical** | Yearly objectives, term OKRs and initiatives that test and deliver the strategy | `objectives.csv`, `krs.csv` | Did the outcomes move, and what did we learn? |
| **Operational** | Running the business: health metrics, SLAs, support, maintenance (BAU) | `health.csv` | Is it inside its limits? |

Operational work is not put into OKRs by default, because a KR that only says "keep things running" hides the work it should explain. The exception is a **breached limit**: when a health metric leaves its range and stays out, fixing it can become a KR for the next term. `bin/pom report` lists breached health metrics as candidates.

A useful question in any review: how much of this team's capacity went to strategic, tactical and operational work last term, and is that the split leadership intended? (See belief 4.10, urgency displaces importance.)

## Product strategy on one page

`templates/product-strategy.md` uses five parts for each strategic theme: the problem, the business value, the user value, the leading indicators, and what comes first and next. Keep it to a page per theme.
