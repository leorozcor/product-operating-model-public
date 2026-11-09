---
description: Prepare for a team's gemba, or record one from the facilitator's notes
argument-hint: <workspace> <team-id> [prepare|record] [notes...]
---

A gemba is an inspection of the work, not a reporting meeting: 10 to 15 minutes, team-led, three questions. Read `model/gemba-and-cadence.md` if you have not.

Workspace: `$1`. Team: `$2`. Mode: `$3` (default `prepare`).

## prepare

Write a one-screen brief for the facilitator, not for management:

1. Run `bin/pom report $1` and keep only this team's lines.
2. List the team's KRs with their last confidence and trend, and any signal from the report (watermelon candidate, stalled yellow, red, overdue commitment).
3. List blockers from `actions.csv` that management owes this team an answer on, oldest first, and say which ones are past the next gemba.
4. Suggest **at most three** questions worth asking, based on the signals. Phrase them as questions to the team, never as verdicts. A green far behind its glidepath gets "what do you know that the numbers don't show?", not "this is a watermelon".
5. Print the brief. Don't write files in prepare mode.

## record

The facilitator gives you notes from the gemba (the rest of the arguments, or pasted text).

1. Draft `gembas/<date>-<team>.md` from `templates/gemba-note.md`, using only what the notes say.
2. Draft the new rows for `checkins.csv` (date, kr_id, value, confidence, evidence_grade, note; leave the grade blank if the notes don't say how the value was obtained) and `actions.csv` (one per blocker the team can't solve itself, status `open`, with the management owner named in the notes or left blank).
3. **Show the draft rows and the note to the facilitator and wait for approval before writing any file.** Then append the rows; never rewrite or delete existing rows, except the approved action updates in step 4.
4. If an earlier blocker was answered or assigned at the gemba, show the exact changes to its existing `actions.csv` row (`owner`, `status`, `answered`, `answer`) and apply only after approval. **Update the existing row; do not append a duplicate action.** Keep the original ID, raised date, team and blocker text unchanged.

## Rules

- Never invent a value or a confidence colour. If the notes don't give one, leave it out and say so.
- Never assess individual people.
- Blockers belong to management. Phrase them so a manager can act on them.
- "We don't know, park it" is a valid answer and counts as answered.
