# How to use this toolkit

A practical guide, from the day you copy the repo into a company to the end of your first year. If you only read one other file, read [BELIEFS.md](BELIEFS.md). This guide tells you what to do; that file tells you why.

## What you need

- A private git repository in the company (copy this one into it).
- Python 3.9 or later, for `bin/pom`. No packages to install.
- An approved AI assistant is optional. Claude Code provides `/okr-review`, `/gemba` and `/term-review`; ChatGPT can perform equivalent work using [CHATGPT.md](CHATGPT.md). The templates and `bin/pom` work without either.
- One person who owns the operating model, usually the head of product. In this guide that person is "you".

## The year at a glance

| When | What happens | Who | Files and tools |
|---|---|---|---|
| Weeks 1 to 2 | Agree the beliefs | You and leadership | `BELIEFS.md`, `decision-log.md` |
| Weeks 1 to 6 | Diagnose | You | `templates/diagnosis.md`, `model/diagnose.md` |
| 2 to 3 weeks before each term | Strategy check, then teams draft OKRs | Leadership, then each team | `strategy.md`, `product-strategy.md`, `objectives.csv`, `krs.csv`, `bin/pom check`, `/okr-review` |
| First 3 weeks of the term | Measure every baseline | Each team | `kpi-definitions.csv`, `krs.csv` |
| Every gemba (weekly to monthly) | Inspect the work, raise blockers | Each team, with management | `/gemba`, `checkins.csv`, `actions.csv`, `gembas/` |
| Between gembas | Answer every blocker | Management | `actions.csv` |
| Last week of the term | Term review | Each team | `bin/pom report`, `/term-review` |
| After the term | Strategy update and pre-mortem | Leadership | `decision-log.md`, `product-strategy.md`, `templates/premortem.md` |

The default term is four months (three terms a year). Set it to the company's cadence, anywhere from a quarter to six months.

---

## Step 1. Copy the repo and set it up

```
git clone <this repo> product-operating-model
cd product-operating-model
python3 -m unittest discover -s tests        # should end with OK
bin/pom report examples/fictional --today 2027-03-29
```

Read the fictional example's [README](examples/fictional/README.md) and the report it produces. Ten minutes with it is the fastest way to see what everything is for.

Then remove what doesn't fit the company: nothing in the repo is mandatory except the idea that agents challenge and people decide.

## Step 2. Agree the beliefs (weeks 1 to 2)

Run one session with the leadership team on [BELIEFS.md](BELIEFS.md). For each belief, mark *we hold this*, *we don't*, or *we'll test it*. Write the result in `decision-log.md`.

Spend most of the time on the beliefs people disagree with. If leadership doesn't hold, say, 2.7 (management answers every blocker before the next gemba), the gemba will turn into a status meeting. It is better to know now and design around it.

Ask your company-approved assistant (Claude Code, or ChatGPT following `CHATGPT.md`):
> Read BELIEFS.md and draft five questions for the leadership session that will surface where we disagree. Don't propose answers.

## Step 3. Diagnose (weeks 1 to 6)

Before installing anything, learn how decisions actually get made. Follow [model/diagnose.md](model/diagnose.md) and fill in `templates/diagnosis.md`. Grade every finding: A measured, B reported, C estimated, ? unknown.

By the end you should know, for each team:

- **Its maturity level** (0 roadmap-driven, 1 introducing, 2 practising, 3 learning), from what you observe, not what the team says. See [model/maturity.md](model/maturity.md).
- **Its limiting condition**: autonomy, clarity, sponsorship, expertise or trust.
- **Whether it can measure its product.** If it can only count releases, it is *not instrumented*, and its first term's job is to build measurement.

Write each team into `pom.json`:

```json
{"id": "payments", "name": "Payments", "maturity": 1,
 "maturity_evidence": "First term with OKRs; KRs were features last year (A)",
 "instrumented": false}
```

**Start small.** At level 0, run OKRs with one pilot team only. Pick a team with someone who already practises learning loops; it will move faster than the organisation, so don't take its pace as the norm.

## Step 4. Check the strategy (2 to 3 weeks before the term)

OKRs need something to point at. Fill in `strategy.md` (where we play, how we win) and `product-strategy.md` (one page per theme: problem, business value, user value, leading indicators, first and next).

Write every strategic choice as a hypothesis with a horizon and a sign of being wrong. If the company has no written strategy, write what you hear, mark it grade B or C, and say so. A rough strategy that people can argue with beats a missing one.

If the company already has a strategy deck, start from it instead of a blank page. Follow [model/intake.md](model/intake.md), or run:
```
/intake workspace/2027-T1 strategy <deck or document>
```
It drafts `strategy.draft.md` and `product-strategy.draft.md` in `reviews/intake/` with the source's wording, and a report of the gaps: choices with no evidence, no horizon or no sign of being wrong, and team work with no choice above it. The strategy owner decides what goes into the real files.

## Step 5. Set up the term workspace

```
mkdir -p workspace/2027-T1
cp templates/*.csv templates/pom.json templates/decision-log.md workspace/2027-T1/
cp templates/strategy.md templates/product-strategy.md workspace/2027-T1/
```

The public edition's `.gitignore` excludes `workspace/`. In the company's private copy, remove that line so workspaces are committed: git history is the audit trail for check-ins, actions and decisions.

In `workspace/2027-T1/pom.json`, set the term dates, the gemba cadence (`weekly`, `sprint` or `monthly`), the teams, and optionally `baseline_due` (default: three weeks after the term starts). Dates live only here, so an old term's calendar can't sneak into a new one.

## Step 6. Teams draft their OKRs

If the teams already plan in an OKR spreadsheet, bring it in first rather than retyping it:
```
/intake workspace/2027-T1 okrs <exported sheet> payments
```
It recognises the common sheet shapes, drafts rows in `reviews/intake/` with a `source` column, keeps blanks blank, and lists what each team still has to fill in. The team edits the draft and copies its rows into `objectives.csv` and `krs.csv`. Mid-term, it can also bring in the check-in history; start confidences can't be recovered and stay blank.

Each team writes its rows in `objectives.csv` and `krs.csv`. The short version of [model/okrs.md](model/okrs.md):

- **One to three objectives per team.** Each with a **narrative**: why this, why now, for whom, what we believe, what we're not doing.
- Each objective names the **strategy hypothesis** it serves and its **kind**: `product`, `platform`, `migration` or `statutory`.
- **Two to four key results**, each one of:
  - **outcome**: a change in behaviour, with baseline, target, unit, cadence, owner and evidence grade;
  - **commitment**: something done by a date, of kind `think`, `build`, `launch`, `date` or `measure`;
  - **stretch**: an outcome nobody expects to hit, at most one per objective;
  - **guardrail**: a metric that must stay inside a limit, required on platform and migration objectives.
- Name **partner teams** on shared KRs.
- Write a **start confidence** (green, yellow, red) for every KR. It is frozen once the term starts.
- Define each metric once in `kpi-definitions.csv`: owner, data owner, source, frequency, unit.

Then check and review:

```
bin/pom check workspace/2027-T1
```

```
/okr-review workspace/2027-T1 payments
```

The checker is mechanical: missing narratives, outputs disguised as outcomes, commitment share too high for the team's level, migrations without a guardrail, and so on. The review is a conversation at the stance the team's level calls for: listening at 0, coaching at 1, challenging at 2, adversarial at 3. It writes to `reviews/` and never edits the team's OKRs. The team decides what to change.

Before freezing, run a 20-minute pre-mortem with `templates/premortem.md`.

### Before freezing: agree material dependencies

A partner name in `krs.csv` is not a commitment. For consequential shared KRs, briefly agree the needed contribution, capacity trade-off, acceptance evidence, due date and escalation owner with the other team. Use [model/teams-and-dependencies.md](model/teams-and-dependencies.md) and, if useful, [templates/dependency-handshake.md](templates/dependency-handshake.md). Don't create a meeting or document for a trivial dependency.

## Step 7. Measure the baselines (first three weeks)

Every outcome and guardrail KR needs a baseline by `baseline_due`. After that date, `bin/pom check` reports a missing baseline as an error, at every level. Either measure it, or turn the KR into a `measure` commitment.

Teams marked `"instrumented": false` are exempt, as long as they have at least one `measure` commitment: "we can see weekly completed jobs per customer by week 6". When measurement exists, set `instrumented` to `true` for the next term.

## Step 8. Run gembas (every week, sprint or month)

A gemba is 10 to 15 minutes in front of the team's board. It is an inspection of the work, not a status meeting. Details in [model/gemba-and-cadence.md](model/gemba-and-cadence.md).

**Before**, the facilitator runs:
```
/gemba workspace/2027-T1 payments prepare
```
This prints a one-screen brief: KR confidence and trends, signals worth asking about, and blockers management still owes an answer on. It writes nothing.

**During**, the team answers three questions:
1. What did we achieve or learn? (with check-ins: value, evidence grade and confidence for each KR)
2. Which hypotheses do we test next?
3. What blocks us, especially what we can't solve ourselves?

**After**, the facilitator pastes their notes:
```
/gemba workspace/2027-T1 payments record <notes>
```
Claude drafts the gemba note, the new `checkins.csv` rows and the new `actions.csv` rows, shows them, and writes them only after the facilitator approves. It never invents a value or a colour.

**Between gembas**, management works every open blocker in `actions.csv` and answers it before the next gemba: `solved`, `decided`, or `parked` ("we don't know, park it" counts as an answer). This is the part that builds trust. The term report measures it.

Any time, anyone can run:
```
bin/pom report workspace/2027-T1
```
It flags watermelon candidates (green but well behind the glidepath), late first yellows or reds, stalled yellows, reds, overdue commitments, shared KRs, unanswered blockers, health metrics outside their limits, and maturity signals per team. It lists signals; it doesn't grade teams.

### Within the term: test before investing heavily

Use [model/discovery-and-evidence.md](model/discovery-and-evidence.md) to identify the most dangerous product assumption, choose a proportionate way to test it and agree what evidence would change the decision. Capture learning in existing gemba notes and check-ins, not a mandatory new process.

## Step 9. Term review (last week of the term)

```
bin/pom report workspace/2027-T1 --today <term end date>
```

```
/term-review workspace/2027-T1 payments
```

Claude drafts the team's review in `reviews/`: results against the frozen start confidences (with evidence grades, and no C-grade number presented as an outcome), what was learned, which strategy hypotheses got stronger or weaker, blockers and answers, and at most three proposed strategy changes. The team edits and owns it.

Use the watermelons and late reds as retrospective questions: was the risk visible earlier, and what made it hard to say?

## Step 10. Strategy update (after the term)

Leadership reads the term reviews together. For each proposed strategy change, record a decision in `decision-log.md`: accepted, rejected or parked, with the evidence and its grade. The owner of `product-strategy.md` then makes the accepted changes. Agents never edit the strategy.

Questions worth asking every time:
- Which hypotheses did this term strengthen or weaken?
- Where did several teams hit the same blocker? That is a system problem.
- Which objectives were orphans, and is the strategy missing something?
- How much capacity went to strategic, tactical and operational work, and was that the intent?
- Should any team move up or down a maturity level? Look at the signals, decide as a person.

If a whole year passes without the product strategy changing, the loop isn't reaching leadership. Treat that as a finding, not a success.

Then start the next term at Step 4.

---

## Who does what

| Role | Owns | Uses |
|---|---|---|
| Head of product (you) | The operating model, the diagnosis, maturity levels, `BELIEFS.md` for this company | Everything |
| Leadership team | `strategy.md`, decisions in `decision-log.md`, answering blockers | Term reviews, `bin/pom report` |
| Each team (PM, tech lead, designer) | Its OKRs, check-ins, gemba, term review | `/okr-review`, `/gemba`, `/term-review`, `bin/pom check` |
| Gemba facilitator (often a coach or a PM) | Running the gemba, recording it | `/gemba prepare` and `record` |
| Managers above the team | Answering every blocker before the next gemba | `actions.csv` |

## Asking Claude in this repo

The commands cover the routine. For everything else, ask in plain words. Some prompts that work well:

- "Read diagnosis.md and tell me which beliefs in BELIEFS.md this organisation doesn't hold yet, with the evidence."
- "Which objectives in workspace/2027-T1 are orphans, and what do they suggest is missing from the product strategy?"
- "Compare the payments team's start confidences with its results. Where were we most overconfident?"
- "Draft the narrative for objective O2 from these notes. Keep it under 120 words and don't invent numbers."
- "Argue against the strategy hypothesis S2 using only evidence in this workspace."

What Claude won't do here, by design (see [CLAUDE.md](CLAUDE.md)): edit a team's OKRs or the strategy, write to `decision-log.md`, append rows without approval, invent numbers, rank teams or assess individuals.

## Adapting it

- **Cadence.** Monthly gembas with six-month terms leave blockers waiting a month; `bin/pom check` warns. Prefer shorter terms or a light fortnightly gemba.
- **Thresholds.** Change the commitment-share limits per level in `pom.json` (`commitment_share_warn`).
- **Language.** Rename "gemba", "terms" or "initiatives" to whatever the company already says. Keep the ideas.
- **Tools.** The CSVs import into any spreadsheet. If the company lives in Jira or a goal tool, keep this repo as the source of truth for reviews and decisions, and export to the tool, not the other way round.

## Common traps

- **Installing before diagnosing.** OKRs on a team with no trust produce sandbagged commitments and green walls.
- **Status instead of confidence.** "On Track" hides risk. Ask "Might we miss it? Do we need to change our plans?"
- **A template without the rituals.** The columns don't create learning; the gemba and management's answers do.
- **Treating a migration year as a failure of OKRs.** Commitments are honest there. Add a guardrail.
- **Reading a pilot team's pace as the organisation's.**
- **Grading teams on maturity.** It's a level for choosing how to help, not a score.

## Where to look next

- Why: [BELIEFS.md](BELIEFS.md)
- How it fits together: [model/loop.md](model/loop.md), [model/strategy-cascade.md](model/strategy-cascade.md)
- Details: [model/okrs.md](model/okrs.md), [model/gemba-and-cadence.md](model/gemba-and-cadence.md), [model/term-review.md](model/term-review.md), [model/maturity.md](model/maturity.md), [model/diagnose.md](model/diagnose.md)
- Credits: [sources.md](sources.md)
- Tests of the agents: [evals/](evals/)
