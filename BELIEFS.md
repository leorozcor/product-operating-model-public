# Beliefs behind this operating model

This toolkit is built on a set of beliefs about how product organisations learn. They are written down here so that the repo still makes sense when it is copied into a company and nobody can ask the author what he meant.

**Whose beliefs.** They are Luis Orozco's working beliefs about product and organisations, restated from his talks, his practice leading product teams, and books he anchors on. They are a snapshot that a company can read, argue with and change.

**How to read the labels.** Each belief carries one of three labels, and the difference matters:

- **Principle**: a commitment. The model is designed around it. Changing it changes the model.
- **Hypothesis**: a causal claim that could be wrong. Each one says what would count against it. Watch for that evidence.
- **Heuristic**: a quick tool. Use it when it helps and drop it when it doesn't.

**When you deploy this in a company**, read this file with the leadership team before installing anything. Mark each belief: *we hold this*, *we don't*, or *we'll test it*. Record disagreements in `decision-log.md`. A belief the leadership doesn't hold will quietly turn the rituals into theatre. It is better to know that on day one.

---

## 1. What a product operating model is

**1.1 An operating model is conditions, not process** (principle). A product operating model exists to create better conditions for teams to solve real problems. It does not exist to add processes. Every template and ritual in this repo should be judged by whether it improves those conditions. If it doesn't, cut it.
*In this model:* the rituals are small (a 10 to 15 minute gemba, a term review), and the agents refuse to grade a team on whether it filled in forms.

**1.2 Principles over processes** (principle). Teams should share a few principles they understand rather than a long process they follow. Processes break when the situation changes; principles let people decide well in a situation nobody planned for.
*In this model:* each model page starts with the principle it serves, so a team can adapt the mechanics without losing the point.

**1.3 Structure needs meaning, or it is just watering** (principle). OKRs, squads and operating models are watering. Meaning, trust and respect for what the structure is for are the soil. Watering bad soil produces nothing.
*In this model:* the toolkit starts with a diagnosis (`model/diagnose.md`), not with an OKR rollout.

**1.4 Soil before water** (heuristic). Before adding an intervention, find the limiting condition. Is it trust, clarity of direction, sponsorship, skills, or the incentives?

**1.5 Control the conditions, not the answer** (principle). In complex systems, control over outcomes is mostly an illusion, and demanding certainty produces only the appearance of certainty. Complicated systems are different: a monthly invoicing run should be predictable, and there certainty is a legitimate demand. Know which one you are in.
*In this model:* outcome key results are tracked by confidence, not by percent complete. Commitments are used where the work really is deterministic.

## 2. Trust and the conditions for empowerment

**2.1 The Trust Pyramid** (principle; Luis's own framework). Build from the bottom up:

1. **Trust** at the base.
2. **Psychological safety**: people can say what they see without punishment.
3. **A common vision and priorities**: everyone knows where we are going and what matters most.
4. **Empowerment with alignment**: "Empowerment: yes. Free-for-all: no."
5. **Resilience** at the top: the organisation absorbs surprises and keeps learning.

Decisions are where strategy, values and culture become concrete. A level can't be skipped: empowerment without a common vision is a free-for-all, and a vision without safety never hears bad news.

**2.2 Trust distributes judgment; fear seeks control** (hypothesis). "The opposite of empowerment is not micromanagement. It is an organisation that is too afraid to let reality travel upward and judgment travel downward." Fear is not always pathological; the question is what the organisation converts it into.
*What would count against it:* teams that report bad news early and get more autonomy as a result, in a place where leaders are visibly afraid.
*In this model:* OKR maturity is never allowed to outrun trust. The agents watch for signs of fear, such as KRs that stay green until the last week, and raise them as a system problem, not a team failure.

**2.3 Autonomy needs five things at once** (hypothesis). Autonomy, clarity of direction, sponsorship, available expertise and trust are conjunctive, not additive. Each missing piece fails in its own way: autonomy without clarity drifts, clarity without sponsorship stalls, and so on.
*In this model:* the diagnosis checks all five before a team is moved up a maturity level.

**2.4 Reality before reassurance** (principle). A healthy organisation would rather learn an uncomfortable truth than keep a comforting story.
*In this model:* "red" is information, not failure. Hiding a red is the failure.

**2.5 Make uncertainty visible before failure** (principle). Watch for the "OKR watermelon": green on the outside, red inside, until it suddenly fails. Changes in confidence should surface early.
*In this model:* `bin/pom report` flags green KRs that are behind their glidepath and the first non-green that only shows up at the end of a term.

**2.6 Kind, not nice** (principle). "Nice protects immediate comfort. Kind protects the person and the quality of the work." The target is high standards with low interpersonal threat. Say it like you see it.
*In this model:* the agents challenge plainly and specifically, without grading people.

**2.7 Gembas build trust between layers** (principle). A gemba inspects the work; it is not a reporting meeting. In 10 to 15 minutes a team covers what it achieved or learned, which hypotheses it tests next, and what blocks it, especially what it can't solve itself: coordination between teams, resourcing, competing priorities, input from other parts of the organisation. Management works on those blockers before the next gemba and always answers, even with "we don't know, park it". Over enough cycles this speeds up learning and builds trust, because the team knows management has its back and will get an answer.
*In this model:* the management action log is the one place where management, not the team, is measured.

**2.8 Leadership is enabling** (principle). A product leader's job is not coding, designing or even shaping individual products; it is enabling all of that. "It's like tending a garden, but you are also a plant": the leader's own behaviour is part of the culture being shaped. Gardeners still prune and replace, so empowerment is not endless patience. The test of an empowering organisation is whether it tolerates the gardener's timeframe under pressure.

**2.9 Credibility over formal authority** (heuristic). Progress across countries and functions depends more on shared direction and credibility than on formal authority. When dealing with dependencies: high integrity, always follow up, be open about your agenda, no politics.

## 3. Product and outcomes

**3.1 What, why, for whom, and how we'll know** (principle). Good product work means knowing what is worth building, why and for whom, and how we'll know whether it worked. Every objective in this model has a narrative that answers those questions.

**3.2 Outcomes over outputs** (principle). A team is accountable for a change in customer or business behaviour, not for shipping. Initiatives are hypotheses about how to cause that change; they are not the goal.
*In this model:* the chain is objective → key results → initiatives → insights. `bin/pom check` flags outcome KRs that read like outputs.

**3.3 Measure the customer's completed job** (principle). Measure what the customer actually came to do (make a deal, get paid, finish a task), not the convenient platform event (a listing, a lead, a click). Friction anywhere in that job is part of the product problem.

**3.4 Product is innovation, and innovation is risk management** (principle). Product work manages uncertainty. Teams coach each other to reduce four risks before and during building: **value** (will they want it?), **usability** (can they use it?), **feasibility** (can we build it?) and **viability** (does it work for the business?). A fifth question is worth asking for consumer products: is it **lovable**?

**3.5 Learning loops** (principle). Concept, build, measure, learn. The loop should be short enough that a team learns several times inside a term.

**3.6 Love the problem, not the solution** (principle). Hold the outcome firmly and the route loosely. A team can change its solution several times while keeping the same goal for years.

**3.7 Not everything worth exploring deserves investment** (heuristic). Exploring is cheap; committing is not. Keep them separate.

**3.8 Start with the users' daily reality** (heuristic). In a new context, first learn how decisions actually get made, where data or tools fall short and what already works. Then set priorities and measurable goals with the teams.

**3.9 Teams are self-contained, cross-functional and accountable** (principle). A team should hold the skills to deliver its outcome without waiting on others for every step, and should own the result. Fewer, real teams beat many nominal ones.

**3.10 Close the feedback loops for the whole group** (principle). What one team learns should reach the others and leadership. A learning that stays in one team is half wasted.

**3.11 Strategic impact is explicit** (heuristic). Each objective names the top-level metric it should move (for example customer satisfaction, employee engagement, revenue or contribution). If it moves none, ask why it is an objective.

## 4. Strategy and learning

**4.1 Strategy and OKRs refine each other** (principle). Strategy sets direction for OKRs, and what OKRs teach should revise strategy. When strategy stays unchanged through several rounds of evidence, ask whether the evidence reached decision-makers and was considered. Stability can also be a deliberate, well-supported choice.
*In this model:* each term review ends with proposed strategy changes, which leadership accepts, rejects or parks in the decision log.

**4.2 Strategy is a set of falsifiable bets** (principle). Write strategic choices as hypotheses with a horizon and a sign of being wrong. "We win by X" is a slogan until it says what would show it isn't working.

**4.3 Freeze, then test** (principle). Freeze a hypothesis or a forecast before the term starts, then compare it with what happened. "A model revised after every rejection only ever explains the past."

**4.4 Grade every number** (principle). Every figure carries an evidence grade: **A** measured, **B** reported, recalled or sampled, **C** estimated now, **?** unknown. No C-grade number is ever presented as an outcome.

**4.5 Be suspicious of ideas that flatter you** (heuristic). When a conclusion flatters your own team, discipline or plan, demand more evidence, not less. Record supporting cases, counterexamples and what would falsify it.

**4.6 Know which kind of decision you face** (heuristic). Irreversible decisions justify slowing down for certainty. For reversible ones, waiting for certainty is the expensive mistake.

**4.7 Ask what the system makes rational** (heuristic). When behaviour is unhelpful, ask what the incentives, structure and information make rational. Understanding the conditions improves diagnosis without excusing harmful choices.

**4.8 The profit formula decides what product work is rational** (hypothesis). Ask what the business actually makes money from and what product behaviour that makes rational. A product strategy that fights the profit formula needs leadership to change the formula, or it will lose.
*What would count against it:* a product strategy that succeeds while rewarding the opposite of what the profit formula pays for.

**4.9 Authority follows the value model** (heuristic). A cross-cutting role, such as a platform team, only holds if the way the company measures value rewards work across units. Otherwise it collapses into coordination.

**4.10 Urgency displaces importance** (hypothesis). "Strategic slack is not unused capacity. It is the capacity from which foresight, learning and prevention are produced." An organisation running at 100% on urgent work stops learning.
*What would count against it:* a team at full utilisation that still improves its strategy term after term.
*In this model:* the term review asks how much capacity went to planned outcomes, to urgent work and to learning.

## 5. Bets, launches and forecasting

**5.1 Agree the scoreboard before launch** (heuristic). Decide which numbers will judge a launch before it ships, and who reads them.

**5.2 "Live" is not "successful"** (principle). Shipping is the start of the measurement, not the result.

**5.3 Split bundled bets** (heuristic). A bundled launch hides which half of the bet is paying. Split the case so each half can fail visibly.

**5.4 A migration needs a deposit** (heuristic). A platform migration is a withdrawal from users' goodwill, so pair it with something they value. Budget stabilisation after a migration as a planned cost, not a surprise.

**5.5 Stop tests that can only teach the wrong lesson** (heuristic). If a confusing experience will produce a false negative on demand, delay the test. A bad test can kill a good idea.

**5.6 Keep supply metrics apart from business results** (heuristic). Counting suppliers, partners or listings is not the same as measuring the business they should produce.

## 6. AI in the operating model

**6.1 AI is an amplifier** (hypothesis). It amplifies how good or bad an organisation already is. Without clear objectives, documentation and feedback, it can multiply low-value output.
*What would count against it:* weak teams that get reliably better by adopting AI tools alone.

**6.2 AI expands "could" faster than it resolves "should"** (hypothesis). When building gets cheaper, choosing badly gets more expensive. The old constraints were a brake on bad decisions. The hard problem becomes knowing what to build, not building it.
*In this model:* the agents challenge choices and evidence; they don't generate roadmaps.

**6.3 Remove friction, keep the effort** (hypothesis). AI should remove the friction that blocks learning, not the effort through which learning happens.
*In this model:* agents never write a team's OKRs or a strategy for them. They ask questions, run checks and draft notes that people then own.

**6.4 Agents challenge; people decide** (principle). Every decision in this toolkit belongs to a named person. An agent can raise, propose and record; it can't approve.

---

## Where these come from

- Luis's talks and writing on product organisations, trust and leadership, including his talk "Building a product organization with a culture of continuous discovery and delivery" (2023) and his OKR guidance.
- His practice running OKRs, terms and gembas in product organisations, including the PEAK model by ActioGlobal, which he practised but did not write. See `sources.md`.
- Books and thinkers he anchors on: Ashby (requisite variety), Goodhart (measures that become targets), Snowden (Cynefin), Christensen (the profit formula), Edmondson (psychological safety), Kim Scott (radical candour), Marty Cagan (product risks and the product operating model), and Ravi Mehta (narratives, commitments and tasks).

The model is inspired by a number of private and public sources. Private sources are not named or reproduced. What is not here, on purpose: anything about specific employers' plans, people, results or internal conflicts. Examples in this repo are fictional.
