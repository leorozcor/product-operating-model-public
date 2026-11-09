# Term review and strategy update

*Serves: 4.1 strategy and OKRs refine each other; 4.3 freeze, then test; 4.4 grade every number.*

## The team's term review

At the end of each term every team writes `term-review.md` (template in `templates/`). It covers:

1. **Results against frozen predictions.** For each KR: baseline, target, the confidence forecast at the start, the result, and its evidence grade. No C-grade number is presented as an outcome.
2. **What we learned.** Which initiatives worked, which didn't, which were changed or stopped and why.
3. **Hypotheses tested.** For each strategy hypothesis the team's objectives served: stronger, weaker, or untested, with the evidence.
4. **What blocked us** and whether management answered (from `actions.csv`).
5. **How we spent the term:** a rough split between strategic, tactical and operational work.
6. **Proposed changes to the product strategy.** Proposals only.

`bin/pom report` produces the mechanical parts: confidence trends, watermelon candidates, stalled yellows, overdue commitments, management answers, health breaches.

## Leadership's strategy update

Once a term leadership reads the term reviews together and, for each proposed change, records a decision in `decision-log.md`: **accepted**, **rejected** or **parked**, with the reason and the evidence grade. Accepted changes are then made to `product-strategy.md` (and rarely to `strategy.md`) by the person who owns that document.

Questions for the update:

- Which strategy hypotheses did this term's evidence strengthen or weaken?
- Which objectives were orphans, and does that point to a gap in the strategy?
- Where did several teams hit the same blocker? That is a system problem.
- Did the capacity split match intent?
- What will we freeze for next term?

## Pre-mortem before the next term

Before freezing the next term's OKRs, run a short pre-mortem (`templates/premortem.md`): imagine the term has failed and list why. It is a cheap counterweight to optimism.
