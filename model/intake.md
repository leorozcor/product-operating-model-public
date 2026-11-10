# Intake: start from the documents people already have

*Serves: 1.5 control the conditions, not the content; 4.4 grade the evidence; 3.2 outcomes over outputs.*

Most companies already have a strategy deck and an OKR spreadsheet. Asking them to retype both into new files is a cost, and it throws away the history in their check-in columns. Intake reads what exists, maps it onto this model, and lists what is missing. People then decide what to keep.

## Rules

- **Read, map, ask. Never fill a gap by guessing.** A blank, "TBA", "x", "Z" or a template placeholder stays blank. Say it is missing.
- **Intake writes drafts only**, in `<workspace>/reviews/intake/`. It never writes `objectives.csv`, `krs.csv`, `strategy.md` or `product-strategy.md`. The team (or the strategy owner) reads the draft, changes it, and copies the rows in themselves.
- **Keep the source's words.** Copy objective and KR text as written. Rewrites go in the intake report as suggestions, never into the draft rows.
- **Cite every row.** Each drafted row names its source: file, tab, cell or slide. If a number can't be traced to a cell, it doesn't go in.
- **Don't translate status into confidence.** "On Track" is not "green". Status answers "are we doing the plan?"; confidence answers "will the outcome happen?". Leave `confidence` blank and record the status in the note.
- **Grade only what you know.** `evidence_grade` stays blank unless the source says how the value was obtained (a linked dashboard, a survey with its N, "estimated").
- **The snapshot date matters.** Record when the file was last changed and whether it was read before, during or after the term. A sheet read after the term can't supply frozen start confidences.
- **Company data stays in the company's workspace.** Intake output is company data.

## What to look for in a strategy document

Strategy decks rarely use the toolkit's headings, but they usually contain the same parts. Map what you find; don't add what you don't.

| Usually found as | Goes to | Notes |
|---|---|---|
| Status markers: WIP, draft, "to be revised", a "what is missing" or "next steps" slide | Intake report: sources table | A work-in-progress deck is grade B at best for every choice in it. Its own list of what is missing is the best start for the gaps section. |
| A map of related strategies (group, unit, tech, data, brand, people, roll-out) | Intake report | Ask which ones are authoritative and which this strategy must serve. Don't import them. |
| Context: market and technology trends, competitors, "what this means for us" | `strategy.md`: Where we play, and the evidence column | Trends are context, not choices. Keep only the ones a choice depends on, and grade them. |
| Mission, purpose | `strategy.md`: Purpose and vision | Quote it. |
| Vision statement, "how the experience will change", "from … to …" pictures | `strategy.md`: Purpose and vision | Keep the before/after pairs; they are often the clearest statement of intent. |
| Horizons ("now: modernise; next: transactions"), "we need to succeed in this one or else …" | `strategy.md`: How we win, one row per horizon | A horizon with a dependency ("this only works if that succeeds") is a hypothesis with a sign of being wrong. |
| Who we create value for, per customer group (end users, business customers, internal teams), with the value promised to each | `strategy.md`: Where we play; `product-strategy.md`: User value and Business value | A platform area often serves internal teams first. Name each group; don't merge them. |
| Strategic objectives, must-wins, pillars, "the objectives behind our KRs", priorities for the year | `strategy.md`: How we win (`S1`, `S2`…) | Rewrite as "we believe … so we will …" **in the report**, not in the draft. The draft keeps the source wording. Top metrics named next to them go to `top_metrics` candidates. |
| Core beliefs and product principles | Intake report, compared with `BELIEFS.md` | Don't import. Note where the company's principles agree with or contradict the toolkit's beliefs; that is a question for the beliefs session in `HOW_TO_USE.md`. |
| "From … to …" pairs about ways of working (outputs to outcomes, handovers to cross-functional teams) | `templates/diagnosis.md` and the intake report | A statement of intended change, not evidence that it happened. |
| "What it is / what it is not", out of scope, consciously excluded | `strategy.md`: What we will not do | Often the most useful slide. |
| Evidence: surveys, interviews, benchmarks, with N and dates | "Evidence today" column, graded | A survey with N and a date is B. A benchmark of other companies is B for them, C for us. No source is ?. |
| User pain points, jobs, opportunity, "the crux of the problem" | `product-strategy.md`: The problem, User value | Keep the user's words if quoted. |
| One page per product or theme: job to be done, what it is, for whom, value provided | `product-strategy.md`: one theme each | These pages usually lack leading indicators and "first and next". Say so per theme. |
| A theme summary with business value, user value, leading indicators, first, next | `product-strategy.md`: the same headings | The closest match to the toolkit's template. Copy as written. |
| KPIs with "why this KPI", ladders of metrics | `product-strategy.md`: Leading indicators; `kpi-definitions.csv` | A KPI with a reason is worth more than a list. Draft definitions only where the source defines them. |
| Sequenced steps or phases with a "key achievement" and metrics per step (validate, prepare, nail, scale) | `product-strategy.md`: First and next; product hypotheses | Each step's key achievement is a hypothesis to test before the next step. |
| Focus areas per team or squad | Candidate objectives for each team's draft, and the `strategy_hypothesis` link | A team focus area with no strategic objective above it is an orphan. Say so. |
| Validation plans (a small beta, then a larger share of users, then everyone) | Candidate guardrail and outcome KRs | Rollout percentages are commitments; what must stay healthy during the rollout is a guardrail. |
| Roadmaps by half-year or now / next / later, milestone lists | Intake report | Output plans. Context for commitments; the dates are not KRs until a team makes them one. |
| Dependencies on other units: what we ask of them, what they ask of us | Intake report; `templates/dependency-handshake.md` | Each ask is a candidate handshake or a blocker for `actions.csv`. |
| Staffing and budget, split between running the business and investment | Intake report: capacity split | Use the split to answer the strategic, tactical and operational question in `strategy-cascade.md`. Don't copy figures into drafts. |
| Risks, issues and open discussion points | Intake report: questions; `templates/premortem.md` | Risks named before the term are frozen predictions. Date them. |
| Delivery timelines, component lists, architecture diagrams, positioning maps | Nowhere by default | Mention them in the report as context. |

After mapping, answer three questions in the report: which strategic choices have no evidence; which have no sign of being wrong; and which team work has no strategic choice above it.

## What to look for in an OKR spreadsheet

OKR sheets come in a few recurring shapes. Recognising the shape first tells you which columns to trust. `templates/intake/okr-column-map.csv` lists common headers and where they go.

### Shape 1: the confidence grid

One tab per team. A header block with the team and its channel. Columns for objective, key result, starting point, term target and often a year-end target, initiatives, partner teams and supplier teams. Then a row of dated or numbered columns (week, sprint or checkpoint) where each cell holds a value, a fill colour for confidence, and sometimes a note on the row below. A legend defines the colours as confidence: roughly, we expect to hit it; we might miss it and should consider changing plans; we won't hit it and should rethink. Below the OKRs: health metrics with min and max, and a section listing other teams' key results this team contributes to.

- Each dated cell with a value is a check-in: `checkins.csv` date from the column header, value from the cell, confidence from the fill colour **only if the legend defines colours as confidence**. Read fills with a script where you can, and say it was done that way.
- Note rows under a KR are check-in notes. Keep them whole. They often carry the best evidence of learning in the file.
- Key initiatives are not KRs. List them in the report under the objective.
- Partner and supplier columns go to `partners`, separated by `;`. A dependencies section is a candidate for `templates/dependency-handshake.md`.
- Health metric rows with min and max go to `health.csv` as `lower` and `upper`.
- A "closed" or "done" colour on a commitment means it was met; on an outcome it means the team stopped tracking it. Ask which.
- Column headers sometimes carry dates from an older term that the sheet was copied from. Ignore header dates when they fall outside the term in `pom.json`, and say so.

### Shape 2: the status tracker

A guidance tab, a top-level OKR tab, one tab per team. Columns for priority, objective, key result, a status word (on track, at risk, off track), baseline, target, deadline, initiatives and a link to the top-level OKR, then period columns. Often a metric definitions block (owner, data owner, source, frequency, availability, unit, period) and health metrics graded by word.

- The status column is not confidence (see the rules above). Put the status in the check-in note and leave confidence blank.
- The link to a top-level OKR is a link up, not a strategy hypothesis. Record it in `top_metrics` or the report, and ask which hypothesis in `strategy.md` it serves.
- Metric definition columns map almost one to one onto `kpi-definitions.csv`.
- Health metrics graded by word with no numbers go to the report, not to `health.csv`: there are no limits to check against.
- If the status never changes across the whole term, say so. It is a maturity signal, not a finding about the team's results.

### Shape 3: the company or tribe sheet

One row per objective with a top-level KR or a team north star, a starting point, a term goal and an end-of-year goal, plus columns naming the teams that contribute. Sometimes a mapping tab that tags each team's work by the kind of value it creates (statutory, automation, ease of use, legacy shutdown).

- These rows usually belong in `strategy.md` (as yearly objectives under How we win) or `product-strategy.md`, not in a team's `objectives.csv`.
- A value-type mapping is a strong hint for each objective's `kind`: statutory work is `statutory`, legacy shutdown is `migration`, technical debt is often `platform`. Propose the kind in the report; the team decides.

### Translating key results

| What the source says | Likely KR type in the draft | Why |
|---|---|---|
| A metric with a starting point and a target ("from 61% to 70%") | `outcome` | |
| "Launch…", "Deploy…", "Deliver…", "N features shipped", 0 → 1, Yes/No | `commitment` (kind `launch`, `build` or `date`) | Done or not done. An outcome in disguise is still a commitment until someone names the behaviour it should change. |
| "We know whether…", "we have a plan…", "decision made", "scope agreed" | `commitment` (kind `think`) | |
| "We can see…", "instrument…", "create a baseline for…" | `commitment` (kind `measure`) | Common in teams that can't measure their product yet. See `maturity.md`. |
| "Stays above / below", "does not drop by more than…" | `guardrail` | `target` is the limit. |
| Satisfaction score with no survey yet | `outcome` with a blank baseline, plus a note | The missing survey is often owned by another team: a blocker candidate for `actions.csv`. |
| Ongoing compliance (every regulatory change released on time, security findings fixed in time) | `health.csv` by default | Unless the limit has been breached. See `strategy-cascade.md`. |

Mark every type as proposed. Sorting KRs by reading them is judgement, grade C.

## What intake produces

In `<workspace>/reviews/intake/`:

1. `intake-report.md`, from `templates/intake/okr-intake.md` or `templates/intake/strategy-intake.md`: the sources read, the shape recognised, the column map used, what was mapped, what is missing, questions for each team, and maturity signals seen in the sheets (listed, never scored).
2. Draft files with the same columns as the workspace files plus a last `source` column (file, tab, cell or slide): `objectives.draft.csv`, `krs.draft.csv`, `checkins.draft.csv`, `health.draft.csv`, `kpi-definitions.draft.csv`, `strategy.draft.md`, `product-strategy.draft.md`. Only the ones the source supports. `bin/pom` ignores the extra column; remove it when copying rows in.

Then:

- Run `bin/pom check` on a scratch copy that includes the drafts, to see what the checker would say. Don't copy drafts into the real workspace files.
- Each team reviews its rows, edits them and copies them into `objectives.csv` and `krs.csv`. The strategy owner does the same for the strategy files. Agents may append drafted `checkins.csv` and `health.csv` rows only after approval, as anywhere else.
- Maturity levels in `pom.json` are set by a person. Intake can propose `maturity_evidence` text with a grade; it never sets the level.

## Mid-term intake

When a company is already in a term, intake can bring in the history so far. Two cautions:

- Start confidences can't be recovered after the term has started. Leave `start_confidence` blank for those KRs and say why; don't backfill it from the first check-in.
- Old check-ins keep the date of their column, not the date of the intake.
