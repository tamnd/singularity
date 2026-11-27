"""The counterexamples of notes 38, 40 and 42 (n = 4, the corner {y, z}, the free coordinates x and w)."""

import random
import unittest

from labsim import Point, Ring, free_coordinate, invariants, is_clean, is_monomial_times_unit, lines, nu_G

E = {"y", "z"}


def corner_lines_max(g, K):
    """The largest nu^G on V(X, y) and V(X, z) over the free lines X = x + lam w and X = w."""
    return max(nu_G(free_coordinate(g, "x", "w", lam), E, {"x", L}) for lam in lines(K) for L in "yz")


class Note38Test(unittest.TestCase):
    """Proposition 5.1 and Corollary 5.4: Y = y^(p-2) z^(p-2), g = x^2 Y + F, a_m = 0 and random b_m."""

    def run_word(self, p, F, steps, seed):
        R = Ring.over(p, "x,w,y,z")
        K = R.F
        P = Point(R(f"x^2*y^{p - 2}*z^{p - 2}") + R(F), p, E)
        rng = random.Random(seed)
        out = []
        for m in range(steps):
            L = rng.choice("yz") if m > 1 else "yz"[m]
            P = P.blowup(L, {"w": rng.choice(list(K.nonzero()))})
            out.append(P)
        return R, out

    def test_rho_one(self):
        for p in (3, 5):
            for F in (f"w*y^{p}*z^{p}", f"x*w*y^{p}*z^{p}"):
                R, pts = self.run_word(p, F, 20, p)
                for P in pts:
                    self.assertEqual(invariants(P.F, P.E).rho, 1)
                    self.assertEqual(P.E, R.indices(E))
                # One translation in x gives rho = 0 at once.
                self.assertEqual(invariants(pts[-1].blowup("y", {"x": 1}).F, E).rho, 0)

    def test_derivatives_not_monomial(self):
        for p in (3, 5):
            _, pts = self.run_word(p, f"x*w*y^{p}*z^{p}", 20, p + 1)
            for P in pts:
                self.assertFalse(is_monomial_times_unit(P.F.deriv("x"), E))
                self.assertFalse(is_monomial_times_unit(P.F.deriv("w"), E))


class Note40Test(unittest.TestCase):
    """Theorem 2.3: p >= 5, g = x w (x + w) y^(p-3) z^(p-3)."""

    def test(self):
        for p, k in ((5, 1), (7, 1), (11, 1), (5, 2)):
            R = Ring.over(p, "x,w,y,z", k)
            K = R.F
            g = R(f"x*w*(x + w)*y^{p - 3}*z^{p - 3}")
            # 1. g is clean, r = (p-3, p-3), d = 3, rho = 2, type 1.
            self.assertTrue(is_clean(g, p))
            iv = invariants(g, E)
            self.assertEqual((iv.r, iv.d, iv.rho, iv.tau), ((0, 0, p - 3, p - 3), 3, 2, 1))
            # 2. The y-step and the z-step at the origin fix g, and only (0, 0) keeps rho.
            P = Point(g, p, E)
            for L in "yz":
                self.assertEqual(P.blowup(L).F, g)
                if p ** k <= 25:
                    keep = [(a, b) for a in K.elements() for b in K.elements() if invariants(P.blowup(L, {"x": a, "w": b}).F, E).rho == 2]
                    self.assertEqual(keep, [(0, 0)])
            # 3. nu^G on V(X, y) and V(X, z) is at most 1 for each free line, with the maximum 1.
            self.assertEqual(corner_lines_max(g, K), 1)
            # Also with a shift X = x + lam w + gamma(y, z).
            for gamma in ("y", "z^2", "y*z"):
                for lam in (0, 1, None):
                    G = free_coordinate(g, "x", "w", lam, R(gamma))
                    self.assertLessEqual(max(nu_G(G, E, {"x", L}) for L in "yz"), 1)
            # 4. The curves and the referee strata.
            self.assertEqual(nu_G(g, E, {"x", "w", "y"}), 3)
            self.assertEqual(nu_G(g, E, {"x", "w", "z"}), 3)
            self.assertEqual(nu_G(g, E, {"y", "z"}), 0)
            self.assertEqual(nu_G(g, E, {"x", "w"}), 3)


class Note42Test(unittest.TestCase):
    """Example 3.1: p >= 5, g = y^(p-4) z^(p-4) (x^4 + y z w^3)."""

    def test(self):
        for p in (5, 7):
            R = Ring.over(p, "x,w,y,z")
            K = R.F
            g = R(f"y^{p - 4}*z^{p - 4}*(x^4 + y*z*w^3)")
            iv = invariants(g, E)
            self.assertEqual((iv.d, iv.rho), (4, 3))
            P = Point(g, p, E)
            for L in "yz":
                self.assertEqual(P.blowup(L).F, g)
                keep = [(a, b) for a in K.elements() for b in K.elements() if invariants(P.blowup(L, {"x": a, "w": b}).F, E).rho == 3]
                self.assertEqual(keep, [(0, 0)])
            self.assertEqual(corner_lines_max(g, K), 1)
            self.assertEqual(nu_G(g, E, {"x", "w", "y"}), 4)
            self.assertEqual(nu_G(g, E, {"x", "w", "z"}), 4)


if __name__ == "__main__":
    unittest.main()
