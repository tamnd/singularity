"""The cycle of Hauser and Perlega (arXiv:1802.05010, lab/specs/e1-hp-cycle-p2.yaml, Singularity/Example/HauserPerlegaCycle.lean), their example of section 3 (lab/specs/e1-hp-section3.yaml), and the certificates of note 11."""

import json
import unittest

from labsim import Point, Ring, residual
from labsim import certificate

CYCLE = [
    # (chart, translations, divisor after, residual order after, number of terms after)
    ("x", {"y": 1, "u": 1}, "x,w", 6, 9),
    ("x", {}, "x,w", 5, 9),
    ("u", {}, "x,u,w", 5, 9),
    ("v", {}, "x,u,v,w", 5, 9),
    ("w", {"y": 1, "v": 1}, "x,u,w", 5, 136),
    ("u", {}, "x,u,w", 4, 136),
] + [("y", {}, "x,y,u,w", 4, 136)] * 14


class CycleTest(unittest.TestCase):
    def setUp(self):
        self.R = Ring.over(2, "x,y,u,v,w")
        self.P = Point(self.R("x^4*y^4*w^6*(w^2 + x^3*u^10)"), 8, {"x", "y", "u", "w"})

    def test_start(self):
        res = residual(self.P.F, self.P.E)
        self.assertEqual((res.r, res.d, len(self.P.F)), ((4, 4, 0, 0, 6), 2, 2))

    def test_cycle(self):
        R, P = self.R, self.P
        for n, (j, t, div, d, terms) in enumerate(CYCLE, 1):
            s = P.chart(j, t)
            self.assertTrue(s.multiplicity_kept)
            if n == 1:
                self.assertEqual(s.h, R("x*w"))
            else:
                self.assertEqual(s.h, R.zero())
            P = Point(s.F, 8, s.E)
            res = residual(P.F, P.E)
            self.assertEqual(P.E, R.indices(div.split(",")), n)
            self.assertEqual((res.d, len(P.F)), (d, terms), n)
            if n == 4:
                self.assertEqual(res.r[R.index("v")], 30)
        # F7 = x^12 y^2128 u^84 w^60 (w^4 (1 + y^14 Q) + x^5 y^14 A) with A(0) = 1.
        res = residual(P.F, P.E)
        self.assertEqual(res.r, (12, 2128, 84, 0, 60))
        G = res.G
        self.assertEqual(G.coefficient((0, 0, 0, 0, 4)), 1)
        self.assertEqual(G.coefficient((5, 14, 0, 0, 0)), 1)
        self.assertEqual(G.initial_form(), R("w^4"))
        self.assertTrue(all(e[1] >= 14 for e in G.terms if e != (0, 0, 0, 0, 4)))

    def test_strip_units(self):
        # Dividing by the q-th power units keeps the residual order and the divisor.
        P, Q = self.P, self.P
        for j, t, div, d, _ in CYCLE[:6]:
            P = P.blowup(j, t)
            Q = Q.blowup(j, t, strip_units=True)
            self.assertEqual(Q.E, P.E)
            self.assertEqual(residual(Q.F, Q.E).d, d)
        self.assertLess(len(Q.F), len(P.F))


class Section3Test(unittest.TestCase):
    def test_step(self):
        R = Ring.over(2, "x,y,w")
        P = Point(R("x^2*y^2*w^3*(w*(x+y)^4 + x^13)"), 4, {"x", "y", "w"}).cleaned()
        self.assertEqual(residual(P.F, P.E).d, 5)
        s = P.chart("x", {"y": 1})
        self.assertEqual(residual(s.F, s.E).d, 7)
        self.assertEqual(len(s.F), 3)
        self.assertEqual(s.E, R.indices({"x", "w"}))


class CertificateTest(unittest.TestCase):
    def setUp(self):
        self.R = Ring.over(2, "x,y,u,v,w")
        self.P = Point(self.R("x^4*y^4*w^6*(w^2 + x^3*u^10)"), 8, {"x", "y", "u", "w"})
        self.cert = certificate.make(self.P, [(j, t) for j, t, *_ in CYCLE[:7]])

    def test_round_trip(self):
        cert = json.loads(certificate.dumps(self.cert))
        self.assertEqual(certificate.check(cert), [])
        self.assertEqual([s["d"] for s in cert["steps"]], [6, 5, 5, 5, 5, 4, 4])
        self.assertEqual(cert["steps"][0]["h"], "x*w")

    def test_faults(self):
        cert = json.loads(certificate.dumps(self.cert))
        cert["steps"][1]["d"] = 6
        cert["steps"][2]["divisor"] = ["x", "w"]
        cert["steps"][3]["F"] = "x^9"
        faults = certificate.check(cert)
        self.assertEqual({f.split(":")[0] for f in faults}, {"step 2", "step 3", "step 4"}, faults)

    def test_coordinate_step(self):
        R = Ring.over(2, "x,y,w")
        P = Point(R("y^2*w + y^3"), 2, {"w"})
        cert = certificate.make(P, [("x", {}, {"x", "y"})])
        self.assertEqual(cert["steps"][0]["chart"], "coordinate")
        self.assertEqual(certificate.check(cert), [])

    def test_bad_centre(self):
        R = Ring.over(2, "x,y,w")
        cert = certificate.make(Point(R("y^2*w + y^3"), 2, {"w"}), [("x", {}, {"x", "y"})])
        cert["steps"][0]["centre"] = ["x", "w"]
        self.assertTrue(certificate.check(cert))


if __name__ == "__main__":
    unittest.main()
