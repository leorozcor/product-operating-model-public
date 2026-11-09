"""Tests for bin/pom. Run: python3 -m unittest discover -s tests"""

import importlib.machinery
import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_loader = importlib.machinery.SourceFileLoader("pom", os.path.join(ROOT, "bin", "pom"))
_spec = importlib.util.spec_from_loader("pom", _loader)
pom = importlib.util.module_from_spec(_spec)
_loader.exec_module(pom)

EXAMPLE = os.path.join(ROOT, "examples", "fictional")
TODAY = date(2027, 3, 29)

OBJ_HEADER = "objective_id,team,objective,narrative,strategy_hypothesis,top_metrics\n"
KR_HEADER = "kr_id,team,objective_id,type,kr,baseline,target,unit,cadence,owner,evidence_grade,commitment_kind,due,start_confidence\n"
GOOD_OBJ = 'O1,t,Customers finish the job,"Why this, why now",P1,NPS\n'
GOOD_KR = "K1,t,O1,outcome,Completion from 50% to 60%,50,60,%,weekly,PM,A,,,yellow\n"


def workspace(level=2, cadence="weekly", start="2027-01-04", end="2027-04-30",
              objectives=GOOD_OBJ, krs=GOOD_KR, checkins="", actions="", health="",
              teams=None, extra=None, obj_header=OBJ_HEADER, kr_header=KR_HEADER,
              checkin_header="date,kr_id,value,confidence,note\n"):
    d = tempfile.mkdtemp()
    config = {"company": "Test", "term": {"name": "T", "start": start, "end": end},
              "gemba": {"cadence": cadence}, "teams": teams or [{"id": "t", "maturity": level}]}
    config.update(extra or {})
    with open(os.path.join(d, "pom.json"), "w") as f:
        json.dump(config, f)
    files = {
        "objectives.csv": obj_header + objectives,
        "krs.csv": kr_header + krs,
        "checkins.csv": checkin_header + checkins,
        "actions.csv": "action_id,raised,team,blocker,owner,status,answered,answer\n" + actions,
        "health.csv": "metric,team,lower,upper,value,date\n" + health,
    }
    for name, text in files.items():
        with open(os.path.join(d, name), "w") as f:
            f.write(text)
    return d


def findings(d, today=None):
    return pom.check(pom.Workspace(d), today)


def messages(d, severity=None, today=None):
    return [f"{f.where}: {f.message}" for f in findings(d, today) if severity in (None, f.severity)]


KIND_OBJ_HEADER = "objective_id,team,kind,objective,narrative,strategy_hypothesis,top_metrics\n"
PARTNER_KR_HEADER = KR_HEADER.rstrip("\n") + ",partners\n"


class CleanControl(unittest.TestCase):
    """A positive control: a well-formed set should raise no errors or warnings."""

    def test_clean_workspace_has_no_errors_or_warnings(self):
        d = workspace()
        self.addCleanup(shutil.rmtree, d)
        self.assertEqual(messages(d, "error"), [])
        self.assertEqual(messages(d, "warn"), [])


class CheckRules(unittest.TestCase):
    def run_ws(self, **kw):
        d = workspace(**kw)
        self.addCleanup(shutil.rmtree, d)
        return d

    def test_missing_narrative_is_warning_at_level_1_and_error_at_level_2(self):
        obj = "O1,t,Customers finish the job,,P1,NPS\n"
        self.assertTrue(any("no narrative" in m for m in messages(self.run_ws(level=1, objectives=obj), "warn")))
        self.assertTrue(any("no narrative" in m for m in messages(self.run_ws(level=2, objectives=obj), "error")))

    def test_orphan_objective(self):
        obj = 'O1,t,Customers finish the job,"Why",,NPS\n'
        self.assertTrue(any("orphan" in m for m in messages(self.run_ws(objectives=obj), "warn")))

    def test_too_many_objectives_at_level_1(self):
        objs = "".join(f'O{i},t,Objective {i},"Why",P1,NPS\n' for i in range(1, 5))
        krs = "".join(f"K{i},t,O{i},outcome,X from 1 to 2,1,2,n,weekly,PM,A,,,green\n" for i in range(1, 5))
        self.assertTrue(any("4 objectives" in m for m in messages(self.run_ws(level=1, objectives=objs, krs=krs), "warn")))
        self.assertFalse(any("objectives; keep" in m for m in messages(self.run_ws(level=2, objectives=objs, krs=krs))))

    def test_outcome_missing_fields(self):
        kr = "K1,t,O1,outcome,Completion up,,60,%,,PM,A,,,\n"
        msgs = messages(self.run_ws(krs=kr), "error")
        self.assertTrue(any("missing baseline, cadence" in m for m in msgs))

    def test_output_verb(self):
        kr = "K1,t,O1,outcome,Launch the new checkout,0,1,release,weekly,PM,A,,,\n"
        self.assertTrue(any("reads like an output" in m for m in messages(self.run_ws(krs=kr), "warn")))

    def test_output_verb_not_flagged_mid_sentence(self):
        kr = "K1,t,O1,outcome,Share of users who build a schedule from 10% to 20%,10,20,%,weekly,PM,A,,,\n"
        self.assertFalse(any("reads like an output" in m for m in messages(self.run_ws(krs=kr))))

    def test_c_grade_baseline(self):
        kr = "K1,t,O1,outcome,Completion from 50% to 60%,50,60,%,weekly,PM,C,,,\n"
        self.assertTrue(any("graded C" in m for m in messages(self.run_ws(krs=kr), "warn")))

    def test_bad_grade(self):
        kr = "K1,t,O1,outcome,Completion from 50% to 60%,50,60,%,weekly,PM,D,,,\n"
        self.assertTrue(any("evidence_grade must be" in m for m in messages(self.run_ws(krs=kr), "error")))

    def test_commitment_needs_due_and_kind(self):
        kr = GOOD_KR + "K2,t,O1,commitment,Migrate billing,,,,,PM,,,,\n"
        msgs = messages(self.run_ws(krs=kr), "error")
        self.assertTrue(any("needs a due date" in m for m in msgs))
        self.assertTrue(any("commitment_kind must be" in m for m in msgs))

    def test_two_stretches(self):
        kr = GOOD_KR + "".join(f"S{i},t,O1,stretch,Users from 1 to 9,1,9,n,weekly,PM,A,,,\n" for i in (1, 2))
        self.assertTrue(any("2 stretch KRs" in m for m in messages(self.run_ws(krs=kr), "warn")))

    def test_commitment_share_by_level(self):
        krs = GOOD_KR + "".join(f"C{i},t,O1,commitment,Do thing {i},,,,,PM,,date,2027-04-01,\n" for i in (1, 2))
        self.assertTrue(any("delivery unit" in m for m in messages(self.run_ws(level=3, krs=krs), "warn")))
        self.assertTrue(any("delivery unit" in m for m in messages(self.run_ws(level=2, krs=krs), "warn")))
        self.assertFalse(any("delivery unit" in m for m in messages(self.run_ws(level=1, krs=krs))))

    def test_unknown_objective_and_team(self):
        kr = "K1,t,O9,outcome,Completion from 50% to 60%,50,60,%,weekly,PM,A,,,\n"
        self.assertTrue(any("O9" in m for m in messages(self.run_ws(krs=kr), "error")))
        obj = 'O1,nobody,Customers,"Why",P1,NPS\n'
        self.assertTrue(any("not in pom.json" in m for m in messages(self.run_ws(objectives=obj), "error")))

    def test_monthly_gemba_with_six_month_term(self):
        d = self.run_ws(cadence="monthly", start="2027-01-01", end="2027-06-30")
        self.assertTrue(any("monthly gembas" in m for m in messages(d, "warn")))
        d = self.run_ws(cadence="weekly", start="2027-01-01", end="2027-06-30")
        self.assertFalse(any("monthly gembas" in m for m in messages(d)))

    def test_term_length(self):
        self.assertTrue(any("under ~10 weeks" in m for m in messages(self.run_ws(start="2027-01-01", end="2027-02-15"))))
        self.assertTrue(any("over ~6 months" in m for m in messages(self.run_ws(start="2027-01-01", end="2027-09-30"))))

    def test_bad_checkin_and_action(self):
        d = self.run_ws(checkins="2027-02-01,K1,55,blue,\n2027-02-01,K9,1,green,\n",
                        actions="A1,2027-02-01,t,Blocker,,closed,,\n")
        msgs = messages(d, "error")
        self.assertTrue(any("confidence must be" in m for m in msgs))
        self.assertTrue(any("kr_id is not in" in m for m in msgs))
        self.assertTrue(any("status must be" in m for m in msgs))

    def test_example_has_no_errors_before_the_baseline_window_closes(self):
        self.assertEqual([f for f in findings(EXAMPLE, date(2027, 1, 20)) if f.severity == "error"], [])

    def test_example_flags_k5_after_the_baseline_window(self):
        errors = [f"{f.where}: {f.message}" for f in findings(EXAMPLE, TODAY) if f.severity == "error"]
        self.assertEqual(len(errors), 1)
        self.assertIn("KR K5", errors[0])


class ComparisonRules(unittest.TestCase):
    """Guardrails, objective kinds, partners, baseline window and instrumentation."""

    def run_ws(self, **kw):
        d = workspace(**kw)
        self.addCleanup(shutil.rmtree, d)
        return d

    MIGRATION_OBJ = 'O1,t,migration,Everyone on the new platform,"Why",P1,Revenue\n'
    COMMITMENTS = "".join(f"C{i},t,O1,commitment,Move batch {i},,,,,PM,,launch,2027-04-01,\n" for i in (1, 2, 3))
    GUARDRAIL = "G1,t,O1,guardrail,Weekly active accounts stay within 2%,1000,980,accounts,weekly,PM,A,,,\n"

    def test_migration_without_guardrail_warns(self):
        d = self.run_ws(level=3, obj_header=KIND_OBJ_HEADER, objectives=self.MIGRATION_OBJ, krs=self.COMMITMENTS)
        msgs = messages(d)
        self.assertTrue(any("add a guardrail KR" in m for m in msgs))
        self.assertFalse(any("delivery unit" in m for m in msgs))

    def test_migration_with_guardrail_is_clean(self):
        d = self.run_ws(level=3, obj_header=KIND_OBJ_HEADER, objectives=self.MIGRATION_OBJ,
                        krs=self.COMMITMENTS + self.GUARDRAIL)
        self.assertEqual(messages(d, "warn"), [])
        self.assertEqual(messages(d, "error"), [])

    def test_product_objective_commitments_still_count(self):
        obj = 'O1,t,product,Customers finish the job,"Why",P1,NPS\n'
        d = self.run_ws(level=3, obj_header=KIND_OBJ_HEADER, objectives=obj, krs=GOOD_KR + self.COMMITMENTS)
        self.assertTrue(any("delivery unit" in m for m in messages(d, "warn")))

    def test_bad_objective_kind(self):
        obj = 'O1,t,moonshot,Customers finish the job,"Why",P1,NPS\n'
        d = self.run_ws(obj_header=KIND_OBJ_HEADER, objectives=obj)
        self.assertTrue(any("kind must be" in m for m in messages(d, "error")))

    def test_guardrail_needs_fields_and_is_not_an_output(self):
        kr = "G1,t,O1,guardrail,Deploy failures stay under 5%,,5,%,weekly,PM,A,,,\n"
        d = self.run_ws(krs=kr)
        msgs = messages(d)
        self.assertTrue(any("guardrail KR missing baseline" in m for m in msgs))
        self.assertFalse(any("reads like an output" in m for m in msgs))

    def test_partners(self):
        teams = [{"id": "t", "maturity": 2}, {"id": "u", "maturity": 2}]
        kr = GOOD_KR.rstrip("\n") + ",u;nobody\n"
        d = self.run_ws(teams=teams, kr_header=PARTNER_KR_HEADER, krs=kr,
                        checkins="2027-02-01,K1,52,yellow,\n")
        self.assertTrue(any("partner team 'nobody'" in m for m in messages(d, "warn")))
        out = pom.report(pom.Workspace(d), TODAY)
        self.assertIn("K1 (t, with u,nobody): yellow", out)

    def test_baseline_window(self):
        kr = "K1,t,O1,outcome,Completion from ? to 60%,,60,%,weekly,PM,A,,,\n"
        d = self.run_ws(level=1, krs=kr, extra={"baseline_due": "2027-01-25"})
        before = messages(d, today=date(2027, 1, 20))
        after = messages(d, "error", today=date(2027, 2, 1))
        self.assertTrue(any("missing baseline" in m for m in before))
        self.assertFalse(any("window closed" in m for m in before))
        self.assertTrue(any("window closed on 2027-01-25" in m for m in after))

    def test_default_baseline_window_is_three_weeks(self):
        d = self.run_ws()
        self.assertEqual(pom.Workspace(d).baseline_due, date(2027, 1, 25))

    def test_uninstrumented_team(self):
        teams = [{"id": "t", "maturity": 1, "instrumented": False}]
        kr = "K1,t,O1,outcome,Completion up to 60%,,60,%,weekly,PM,,,,\n"
        d = self.run_ws(teams=teams, krs=kr, extra={"baseline_due": "2027-01-25"})
        msgs = messages(d, today=date(2027, 3, 1))
        self.assertTrue(any("no measure commitment" in m for m in msgs))
        self.assertFalse(any("baseline" in m and "KR K1" in m for m in msgs))
        kr2 = kr + "M1,t,O1,commitment,We can see weekly completion per customer,,,,,PM,,measure,2027-02-15,\n"
        d2 = self.run_ws(teams=teams, krs=kr2)
        self.assertTrue(any("baselines are waived" in m for m in messages(d2, "info")))
        self.assertFalse(any("no measure commitment" in m for m in messages(d2)))


GRADED_HEADER = "date,kr_id,value,confidence,evidence_grade,note\n"


class CheckinGrades(unittest.TestCase):
    """Evidence grades on check-in values."""

    def run_ws(self, **kw):
        d = workspace(checkin_header=GRADED_HEADER, **kw)
        self.addCleanup(shutil.rmtree, d)
        return d

    def test_bad_grade_is_an_error(self):
        d = self.run_ws(checkins="2027-02-01,K1,52,green,D,\n")
        self.assertTrue(any("evidence_grade must be" in m for m in messages(d, "error")))

    def test_missing_grade_warns_at_level_2_not_level_1(self):
        self.assertTrue(any("no evidence grade" in m for m in messages(self.run_ws(level=2, checkins="2027-02-01,K1,52,green,,\n"), "warn")))
        self.assertFalse(any("no evidence grade" in m for m in messages(self.run_ws(level=1, checkins="2027-02-01,K1,52,green,,\n"))))

    def test_commitment_needs_no_grade(self):
        kr = GOOD_KR + "C1,t,O1,commitment,Migrate billing,,,,,PM,,launch,2027-04-01,\n"
        d = self.run_ws(krs=kr, checkins="2027-02-01,C1,done,green,,\n")
        self.assertFalse(any("no evidence grade" in m for m in messages(d)))

    def test_estimate_is_flagged_in_report(self):
        d = self.run_ws(checkins="2027-03-22,K1,57,green,C,\n")
        out = pom.report(pom.Workspace(d), TODAY)
        self.assertIn("57 (C, estimate)", out)
        self.assertIn("Estimated result** K1", out)

    def test_measured_value_is_not_flagged(self):
        d = self.run_ws(checkins="2027-03-22,K1,57,green,A,\n")
        out = pom.report(pom.Workspace(d), TODAY)
        self.assertIn("57 (A)", out)
        self.assertNotIn("Estimated result", out)

    def test_old_checkins_without_column_still_work(self):
        d = workspace(checkins="2027-03-22,K1,57,green,\n")
        self.addCleanup(shutil.rmtree, d)
        self.assertEqual(messages(d, "error"), [])
        self.assertIn("| 57 |", pom.report(pom.Workspace(d), TODAY))


class Report(unittest.TestCase):
    def report(self, today=TODAY, **kw):
        d = workspace(**kw)
        self.addCleanup(shutil.rmtree, d)
        return pom.report(pom.Workspace(d), today)

    def test_watermelon(self):
        # 2027-03-22 is 66% into the term; 20% progress is well behind
        out = self.report(checkins="2027-03-22,K1,52,green,\n")
        self.assertIn("Watermelon candidate** K1", out)

    def test_no_watermelon_when_on_glidepath(self):
        out = self.report(checkins="2027-03-22,K1,57,green,\n")
        self.assertNotIn("Watermelon", out)

    def test_no_watermelon_early_in_term(self):
        out = self.report(checkins="2027-02-01,K1,50,green,\n")
        self.assertNotIn("Watermelon", out)

    def test_works_for_decreasing_targets(self):
        kr = "K1,t,O1,outcome,Tickets from 10 to 5,10,5,n,weekly,PM,A,,,\n"
        out = self.report(krs=kr, checkins="2027-03-22,K1,7,green,\n")
        self.assertIn("60% of the way", out)
        self.assertNotIn("Watermelon", out)

    def test_late_first_non_green(self):
        out = self.report(today=date(2027, 4, 30),
                          checkins="2027-02-01,K1,52,green,\n2027-04-20,K1,53,red,\n")
        self.assertIn("Late first non-green** K1", out)

    def test_early_yellow_is_not_late(self):
        out = self.report(checkins="2027-01-20,K1,51,yellow,\n2027-02-01,K1,52,green,\n")
        self.assertNotIn("Late first non-green", out)

    def test_stalled_yellow(self):
        out = self.report(checkins="2027-03-01,K1,53,yellow,\n2027-03-08,K1,54,yellow,\n")
        self.assertIn("Stalled yellow** K1", out)

    def test_overdue_commitment(self):
        kr = GOOD_KR + "C1,t,O1,commitment,Migrate billing,,,,,PM,,launch,2027-03-01,\n"
        self.assertIn("Overdue commitment** C1", self.report(krs=kr))
        done = self.report(krs=kr, checkins="2027-02-28,C1,done,green,\n")
        self.assertNotIn("Overdue commitment", done)

    def test_blockers_answered_on_time(self):
        actions = ("A1,2027-03-01,t,B1,VP,solved,2027-03-05,ok\n"     # on time
                   "A2,2027-03-01,t,B2,VP,parked,2027-03-20,later\n"  # late
                   "A3,2027-03-01,t,B3,VP,open,,\n"                   # open past the gemba
                   "A4,2027-03-27,t,B4,VP,open,,\n")                  # not due yet
        out = self.report(actions=actions)
        self.assertIn("Answered before the next gemba: 1 of 3 (33%)", out)
        self.assertIn("Open past the next gemba** A3", out)
        self.assertNotIn("A4", out)

    def test_parked_counts_as_answered(self):
        out = self.report(actions="A1,2027-03-01,t,B1,VP,parked,2027-03-03,we don't know\n")
        self.assertIn("1 of 1 (100%)", out)

    def test_health_breach(self):
        out = self.report(health="Latency,t,,5,7,2027-03-22\nUptime,t,99.9,,99.95,2027-03-22\n")
        self.assertIn("Outside its limits** Latency", out)
        self.assertNotIn("Outside its limits** Uptime", out)

    def test_example_report_flags_what_its_readme_says(self):
        out = pom.report(pom.Workspace(EXAMPLE), TODAY)
        for expected in ("Watermelon candidate** K1", "Stalled yellow** K2", "Red** K8", "Estimated result** K8",
                         "Open past the next gemba** A3", "Outside its limits** p95"):
            self.assertIn(expected, out)
        self.assertNotIn("-0%", out)


class Cli(unittest.TestCase):
    def test_check_exit_codes(self):
        self.assertEqual(pom.main(["check", EXAMPLE, "--today", "2027-01-20"]), 0)
        self.assertEqual(pom.main(["check", EXAMPLE, "--today", "2027-03-29"]), 1)
        d = workspace(krs="K1,t,O1,bogus,X,,,,,,,,,\n")
        self.addCleanup(shutil.rmtree, d)
        self.assertEqual(pom.main(["check", d]), 1)

    def test_missing_workspace(self):
        self.assertEqual(pom.main(["check", "/nonexistent"]), 2)


if __name__ == "__main__":
    unittest.main()
