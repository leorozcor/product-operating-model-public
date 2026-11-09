# Fictional example: Fernway

Fernway is a made-up B2B company selling scheduling software to mid-size field-service firms (plumbers, HVAC, elevator maintenance). Nothing here describes a real company, product or person.

It is set in the middle of a term so that `bin/pom` has something to say:

```
bin/pom check  examples/fictional --today 2027-03-29
bin/pom report examples/fictional --today 2027-03-29
```

What it shows on purpose:

- **Scheduling** (maturity 2) has a watermelon candidate (K1 is green but well behind its glidepath) and a stalled yellow (K2).
- **Mobile** (maturity 1) has an outcome KR that reads like an output (K5, "Launch offline mode…") with no baseline. At level 1 most of this is coaching, but the baseline window closed on 25 January, so the missing baseline is now the one error.
- **Platform** (maturity 1) runs a migration objective (`kind: migration`). Its commitments don't count against it, and it has a guardrail (K9: active accounts stay within 2%). Its outcome KR has a C-grade baseline, and it is red.
- Two KRs name a partner team (K4, K6), so the report lists them as shared.
- Management answered one blocker on time, parked one late, and has one open past the next gemba.
- One health metric is outside its limits: a candidate KR for next term.
