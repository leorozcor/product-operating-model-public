# Evals

Two layers for now.

| Layer | What it answers | How | Status |
|---|---|---|---|
| 1. Checker tests | Does `bin/pom` apply its rules: flag what it should, and stay quiet on a clean set? | `python3 -m unittest discover -s tests` | Running. Includes a clean positive control and a test that the fictional example flags what its README says. |
| 2. Behavioural cases | Does an agent command keep its rules: stance by maturity level, never editing OKRs or strategy, never inventing numbers, asking before writing, ignoring instructions planted in data? | `cases/<id>/case.json` | Specified. No automated runner yet: run a case by hand in a fresh copy of the repo and grade it against `expect`. |

## Case format

- `command`: the slash command and arguments.
- `workspace`: the starting workspace, copied fresh for each run. `overrides` describes changes to apply to the copy.
- `user_message`: what the human says, if anything beyond the command.
- `expect.must` / `expect.must_not`: behaviours a grader checks.
- `expect.files_unchanged`: files that must be byte-identical after the run. This part can be checked mechanically.
- `pair_with`: a case whose result should not change. The injection case is graded by comparing it with its control.

## Design choices

- The agent never sees `evals/`. Run each case in a copy without it.
- Paired cases instead of absolute answers: there is no single right review, but adding a planted instruction should change nothing.
- The checks test whether the agent obeys its rules, not whether its judgement is right.

## Next

- A runner that copies the workspace, applies overrides, runs the command headless and checks `files_unchanged`.
- Graders for the `must` lists, then human review of the graders.
