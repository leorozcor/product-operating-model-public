# The loop

*Serves: 4.1 strategy and OKRs refine each other; 3.5 learning loops.*

```
 Diagnose ──► Strategy ──► Term OKRs ──► Gembas (weekly to monthly) ──► Term review ──► Strategy update
    ▲                                         │ blockers up, answers down                   │
    └─────────────── evidence that the diagnosis was wrong ◄───────────────────────────────┘
```

| Step | Who owns it | Artefact | Agent help |
|---|---|---|---|
| Diagnose | Product leadership | `diagnosis.md` | phase 2: `/diagnose` |
| Strategy | Leadership, with the teams | `strategy.md`, `product-strategy.md` | phase 2: `/strategy-challenge` |
| Term OKRs | Each team | `objectives.csv`, `krs.csv` | `/okr-review` |
| Gemba | Each team, management attends | `gembas/<date>-<team>.md`, `checkins.csv`, `actions.csv` | `/gemba` |
| Term review | Each team, then leadership | `term-review.md` | `/term-review` |
| Strategy update | Leadership | `decision-log.md`, then `strategy.md` | phase 2: `/strategy-update` |

Rules that hold across the loop:

1. **Diagnose before installing.** Don't introduce OKRs into a team before you know its maturity level and its limiting condition (`model/diagnose.md`).
2. **Freeze, then test.** Hypotheses and forecasts are written before the term starts and not edited afterwards. Revisions go in a new row or a new section, with a date.
3. **Confidence over status.** Check-ins report confidence (green, yellow, red) and a value, not percent complete.
4. **Every number has a grade:** A measured, B reported, recalled or sampled, C estimated, ? unknown.
5. **Agents challenge; people decide.** An agent never edits a team's OKRs or the strategy. It writes reviews and proposals next to them.
6. **Plain files, no lock-in.** Everything is Markdown, CSV and JSON so it can move into whatever tool the company uses later.
7. **Team and partner agreements are real.** Product, Engineering and Design solve the problem as peers. For material cross-team KRs, clarify contributions and decision rights before freezing the term (`model/teams-and-dependencies.md`).
8. **Test the riskiest assumption.** Initiatives are bets, not evidence. Use proportionate discovery and feed both confirming and disconfirming results into gembas and reviews (`model/discovery-and-evidence.md`).
