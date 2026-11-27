"""Volume 7 of the handbook: Examples 3.13.21, 3.14.9 and 3.15.18."""

import random
import unittest

from labsim import Point, Ring, hypotheses, invariants, nu_G, residual


class Example31321Test(unittest.TestCase):
    """n = 3, Delta = {y, z}, g = x^a y^b z^c with a >= 2, p not dividing a, a + b >= p."""

    def cases(self):
        return [(5, 2, 4, 4), (5, 3, 4, 2), (3, 2, 1, 1), (3, 4, 1, 1), (7, 3, 5, 6)]

    def test_invariants_and_centre(self):
        for p, a, b, c in self.cases():
            R = Ring.over(p, "x,y,z")
            F, E = R(f"x^{a}*y^{b}*z^{c}"), {"y", "z"}
            iv = invariants(F, E)
            self.assertEqual((iv.d, iv.rho), (a, a - 1))
            self.assertEqual(nu_G(F, E, {"x", "y"}), a)
            h = hypotheses(F, E, {"x", "y"})
            self.assertTrue(h.h1 and h.h2)

    def test_charts(self):
        for p, a, b, c in self.cases():
            R = Ring.over(p, "x,y,z")
            P = Point(R(f"x^{a}*y^{b}*z^{c}"), p, {"y", "z"})
            C = {"x", "y"}
            for t in range(1, p):
                s = P.chart("y", {"x": t}, C)
                self.assertEqual(invariants(s.F, s.E).rho, 0)
            s = P.chart("x", centre=C)
            self.assertEqual(s.E, R.indices({"x", "y", "z"}))
            self.assertEqual(residual(s.F, s.E).G, R.const(1))
            self.assertEqual(invariants(s.F, s.E).rho, 0)
            s = P.chart("y", centre=C)
            self.assertEqual(s.F, R(f"x^{a}*y^{a + b - p}*z^{c}"))

    def run_corner(self, p, a, b, c, steps):
        """Blow up V(x, y) and V(x, z) in turn, at the origin, while the order along the centre is at least p."""
        R = Ring.over(p, "x,y,z")
        P = Point(R(f"x^{a}*y^{b}*z^{c}"), p, {"y", "z"})
        seen = [(b, c)]
        for m in range(steps):
            L = "yz"[m % 2]
            if P.F.order_along({"x", L}) < p:
                return seen, False
            P = P.blowup(L, centre={"x", L})
            e = next(iter(P.F.terms))
            seen.append((e[1], e[2]))
        return seen, True

    def test_numbers(self):
        # p = 5, a = 2, b = c = 4: (4, 4), (1, 4), (1, 1), then the corner curves have order 3 < 5.
        seen, more = self.run_corner(5, 2, 4, 4, 10)
        self.assertEqual(seen, [(4, 4), (1, 4), (1, 1)])
        self.assertFalse(more)
        R = Ring.over(5, "x,y,z")
        F = R("x^2*y*z")
        self.assertEqual((F.order_along({"x", "y"}), F.order_along({"x", "z"})), (3, 3))

    def test_infinite_when_a_greater_than_p(self):
        seen, more = self.run_corner(3, 4, 1, 1, 30)
        self.assertTrue(more)
        self.assertEqual(seen[-1], (16, 16))


class Example3149Test(unittest.TestCase):
    """n = 4, Delta = {1, 2, 3}, g = x1 x4^p + x1^2 x2 x3 x4^(p-2)."""

    def test_words(self):
        for p in (3, 5, 7):
            R = Ring.over(p, "x1,x2,x3,x4")
            G = R(f"x4^{p} + x1*x2*x3*x4^{p - 2}")
            rng = random.Random(p)
            for _ in range(5):
                P = Point(R(f"x1*x4^{p} + x1^2*x2*x3*x4^{p - 2}"), p, {"x1", "x2", "x3"})
                for _ in range(8):
                    iv = invariants(P.F, P.E)
                    self.assertEqual((iv.rho, iv.d), (p, p))
                    self.assertEqual(residual(P.F, P.E).G, G)
                    for s, t in (("x1", "x2"), ("x1", "x3"), ("x2", "x3")):
                        self.assertEqual(nu_G(P.F, P.E, {"x4", s, t}), p)
                    for s in ("x1", "x2", "x3"):
                        self.assertEqual(nu_G(P.F, P.E, {"x4", s}), p - 1)
                    self.assertEqual(nu_G(P.F, P.E, {"x4"}), p - 2)
                    P = P.blowup(rng.choice(["x1", "x2", "x3"]))

    def test_numbers_p3(self):
        R = Ring.over(3, "x1,x2,x3,x4")
        P = Point(R("x1*x4^3 + x1^2*x2*x3*x4"), 3, {"x1", "x2", "x3"}).blowup("x2")
        self.assertEqual(P.F, R("x1*x2*(x4^3 + x1*x2*x3*x4)"))
        self.assertEqual(residual(P.F, P.E).r, (1, 1, 0, 0))
        self.assertEqual(P.F.order_along({"x4", "x1", "x2"}), 5)
        self.assertEqual(nu_G(P.F, P.E, {"x4", "x1", "x2"}), 3)
        self.assertEqual(nu_G(P.F, P.E, {"x4", "x1"}), 2)


class Example31518Test(unittest.TestCase):
    """p >= 3, g = x^2 y^(p-2) z^(p-2), Delta = {y, z}."""

    def test(self):
        for p in (3, 5, 7, 11):
            R = Ring.over(p, "x,y,z")
            g = R(f"x^2*y^{p - 2}*z^{p - 2}")
            E = {"y", "z"}
            P = Point(g, p, E)
            self.assertEqual(P.blowup("y").F, g)
            self.assertEqual(P.blowup("z").F, g)
            iv = invariants(g, E)
            self.assertEqual((iv.rho, iv.d), (1, 2))
            self.assertEqual((nu_G(g, E, {"x", "y"}), nu_G(g, E, {"x", "z"})), (2, 2))


if __name__ == "__main__":
    unittest.main()
