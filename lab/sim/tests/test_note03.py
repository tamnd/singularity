"""Note 03: the kangaroo point of Hauser, Example 3.17, and random walks for Theorems 3.7 and 3.12 and Corollaries 3.13 and 3.14."""

import unittest

from labsim import Point, Ring, hypotheses, invariants, residual, survey, theta_tilde


class KangarooTest(unittest.TestCase):
    """p = 2, E = {x, y}, g = x^3 y + x y^3, the x-chart with t_y = 1."""

    def setUp(self):
        self.R = Ring.over(2, "x,y")
        self.P = Point(self.R("x^3*y + x*y^3"), 2, {"x", "y"})

    def test_start(self):
        R = self.R
        iv = invariants(self.P.F, self.P.E)
        self.assertEqual((iv.r, iv.d, iv.rho, iv.tau), ((1, 1), 2, 2, 0))
        self.assertEqual(residual(self.P.F, self.P.E).G, R("x^2 + y^2"))
        self.assertEqual([g for g in theta_tilde(self.P.F, self.P.E)], [R("x^2 + y^2")] * 2)

    def test_chart(self):
        R = self.R
        s = self.P.chart("x", {"y": 1})
        self.assertEqual(s.raw, R("x^2*y^3 + x^2*y^2"))
        self.assertEqual(s.h, R("x*y"))
        self.assertEqual(s.F, R("x^2*y^3"))
        self.assertEqual(s.E, R.indices({"x"}))
        iv = invariants(s.F, s.E)
        self.assertEqual((iv.r, iv.d, iv.rho, iv.tau), ((2, 0), 3, 2, 1))
        self.assertEqual(residual(s.F, s.E).G, R("y^3"))

    def test_type_switch(self):
        # Corollary 3.14: d' = d + 1, rho' = rho = d, tau = 0 and tau' = 1.
        a = invariants(self.P.F, self.P.E)
        s = self.P.chart("x", {"y": 1})
        b = invariants(s.F, s.E)
        self.assertEqual(b.d, a.d + 1)
        self.assertEqual((a.rho, b.rho, a.tau, b.tau), (a.d, a.d, 0, 1))


class Example317Test(unittest.TestCase):
    """p = 2, E = {w}, g = y^2 w + y^3, C = V(x, y): (H1) holds, (H2) fails, and rho goes up in the x-chart."""

    def setUp(self):
        self.R = Ring.over(2, "x,y,w")
        self.F = self.R("y^2*w + y^3")
        self.E = {"w"}

    def test_invariants(self):
        iv = invariants(self.F, self.E)
        self.assertEqual((iv.r, iv.d, iv.rho), ((0, 0, 0), 3, 2))

    def test_hypotheses(self):
        h = hypotheses(self.F, self.E, {"x", "y"})
        self.assertEqual((h.rho, h.ord_C_theta, h.ord_C_theta_C, h.ord_0_theta_C), (2, 2, 2, 3))
        self.assertTrue(h.h1)
        self.assertFalse(h.h2)

    def test_chart(self):
        R = self.R
        s = Point(self.F, 2, self.E).chart("x", centre={"x", "y"})
        self.assertEqual(s.F, R("y^2*w + x*y^3"))
        self.assertEqual(s.E, R.indices({"x", "w"}))
        iv = invariants(s.F, s.E)
        self.assertEqual((iv.d, iv.rho), (3, 3))


class WalkTest(unittest.TestCase):
    """Random walks with q = p: no failure of rho in {d - 1, d}, rho' <= rho, d' <= d + 1, and each kangaroo point is a type switch."""

    def check(self, p, names, walks, seed):
        s = survey(Ring.over(p, names), walks, 8, seed)
        self.assertGreater(s.steps, 50)
        self.assertEqual((s.dichotomy_fail, s.rho_up, s.moh_fail, s.switch_fail), (0, 0, 0, 0), s)
        return s

    def test_p2(self):
        self.check(2, "x,y,z", 300, 1)
        self.check(2, "x,y,z,w", 300, 2)

    def test_p3(self):
        # These seeds give kangaroo points, so Corollary 3.14 is tested on walks too.
        s3 = self.check(3, "x,y,z", 300, 3)
        s4 = self.check(3, "x,y,z,w", 200, 4)
        self.assertGreater(s3.kangaroo + s4.kangaroo, 0)

    def test_p5(self):
        self.check(5, "x,y,z", 200, 5)


if __name__ == "__main__":
    unittest.main()
