"""The fields, the polynomials and the cleaning."""

import itertools
import unittest

from labsim import Ring, binom_mod, clean, field, is_clean
from labsim.charts import chart_map, new_divisor


class FieldTest(unittest.TestCase):
    def test_axioms(self):
        for p, k in [(2, 1), (3, 1), (2, 2), (2, 3), (3, 2), (5, 2), (7, 2)]:
            K = field(p, k)
            els = list(K.elements())
            self.assertEqual(len(els), p ** k)
            for a, b in itertools.product(els[:12], els[:12]):
                self.assertEqual(K.mul(a, b), K.mul(b, a))
                self.assertEqual(K.add(a, b), K.add(b, a))
                self.assertEqual(K.sub(K.add(a, b), b), a)
            for a in K.nonzero():
                self.assertEqual(K.mul(a, K.inv(a)), 1)
                self.assertEqual(K.pow(a, K.size - 1), 1)
            # The Frobenius map is additive, and root inverts it.
            for a, b in itertools.product(els[:10], els[:10]):
                self.assertEqual(K.pow(K.add(a, b), p), K.add(K.pow(a, p), K.pow(b, p)))
            for a in els:
                self.assertEqual(K.pow(K.root(a, p * p), p * p), a)

    def test_prime_subfield(self):
        K = field(5, 2)
        for a, b in itertools.product(range(5), range(5)):
            self.assertEqual(K.mul(a, b), a * b % 5)
            self.assertEqual(K.add(a, b), (a + b) % 5)

    def test_shared_instance(self):
        self.assertIs(field(3, 2), field(3, 2))


class PolyTest(unittest.TestCase):
    def test_lucas(self):
        from math import comb
        for p in (2, 3, 5, 7):
            for n in range(40):
                for k in range(n + 1):
                    self.assertEqual(binom_mod(n, k, p), comb(n, k) % p)

    def test_parse_and_print(self):
        R = Ring.over(3, "x,y")
        f = R("(x + y)^3 - x^3")
        self.assertEqual(f, R("y^3"))
        self.assertEqual(R("2*x*y + x*y"), R.zero())
        g = R("x^2*y + 2*y^5 - 1")
        self.assertEqual(R(str(g)), g)
        R9 = Ring.over(3, "x", 2)
        self.assertEqual(R9(str(R9("#5*x + #7"))), R9("#5*x + #7"))

    def test_translate_and_substitute(self):
        R = Ring.over(5, "x,y")
        f = R("x^7*y + 3*x*y^2")
        self.assertEqual(f.translate({"x": 2}), f.substitute({"x": R("x + 2")}))
        self.assertEqual(f.translate({"x": 2}).translate({"x": 3}), f)

    def test_derivatives(self):
        R = Ring.over(3, "x,y")
        f = R("x^3*y + x^2*y^4")
        self.assertEqual(f.deriv("x"), R("2*x*y^4"))
        self.assertEqual(f.log_deriv("y"), R("x^3*y + x^2*y^4"))
        self.assertEqual(f.order(), 4)
        self.assertEqual(f.order_along({"x"}), 2)


class CleanTest(unittest.TestCase):
    def test_clean_removes_powers(self):
        R = Ring.over(2, "x,y")
        G, h = clean(R("x^2*y^2 + x^2*y^3 + 1"), 2)
        self.assertEqual(G, R("x^2*y^3"))
        self.assertEqual(h, R("x*y + 1"))
        self.assertTrue(is_clean(G, 2))

    def test_clean_identity(self):
        # z^q + F = (z + h)^q + G after the cleaning, so F = G - h^q, over F_p and F_{p^k}.
        for p, k, q in [(3, 1, 3), (3, 1, 9), (2, 2, 4), (5, 2, 5)]:
            R = Ring.over(p, "x,y", k)
            K = R.F
            F = R.monomial((q, 2 * q), K.size - 1) + R.monomial((q, 1), 1) + R.const(min(2, K.size - 1))
            G, h = clean(F, q)
            self.assertEqual(G - h ** q, F)

    def test_chart_is_the_substitution(self):
        R = Ring.over(3, "x,y,w")
        F = R("x^2*y^2 + w^3*y + x^4")
        raw = chart_map(F, 3, 0, {1: 2})
        sub = F.substitute({"y": R("x*(y + 2)"), "w": R("x*w")})
        self.assertEqual(raw.times_monomial((3, 0, 0)), sub)

    def test_divisor_update(self):
        self.assertEqual(new_divisor({0, 1, 2}, 0, {1: 1}, {0, 1, 2}), frozenset({0, 2}))
        self.assertEqual(new_divisor({1, 2}, 0, {1: 1}, {0, 1}), frozenset({0, 2}))
        self.assertEqual(new_divisor({1, 2}, 0, {}, {0, 1}), frozenset({0, 1, 2}))


if __name__ == "__main__":
    unittest.main()
