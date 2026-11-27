"""Truncated generalized power series over F_p.

A series is a dict mapping an exponent vector (tuple of Fractions, coordinates
in a fixed basis of the value group) to a coefficient in F_p.  The value of a
monomial is the dot product of its exponent with a weight vector of floats.
All products are truncated at a value bound BOUND, so every computation is
exact below BOUND."""
from fractions import Fraction as Fr

class Ring:
    def __init__(self, p, weights, bound):
        self.p, self.w, self.B = p, weights, bound
    def val_mono(self, e):
        return sum(float(a) * b for a, b in zip(e, self.w))
    def clean(self, s):
        return {e: c % self.p for e, c in s.items() if c % self.p and self.val_mono(e) <= self.B}
    def add(self, a, b, sign=1):
        r = dict(a)
        for e, c in b.items():
            r[e] = r.get(e, 0) + sign * c
        return self.clean(r)
    def sub(self, a, b):
        return self.add(a, b, -1)
    def mul(self, a, b):
        r = {}
        for e1, c1 in a.items():
            v1 = self.val_mono(e1)
            for e2, c2 in b.items():
                if v1 + self.val_mono(e2) > self.B:
                    continue
                e = tuple(x + y for x, y in zip(e1, e2))
                r[e] = r.get(e, 0) + c1 * c2
        return self.clean(r)
    def power(self, a, n):
        r = {tuple(Fr(0) for _ in self.w): 1}
        for _ in range(n):
            r = self.mul(r, a)
        return r
    def scal(self, c, a):
        return self.clean({e: c * x for e, x in a.items()})
    def val(self, a):
        if not a:
            return float('inf')
        return min(self.val_mono(e) for e in a)
    def lead(self, a):
        e = min(a, key=self.val_mono)
        return e, a[e]
    def mono(self, e, c=1):
        return self.clean({tuple(Fr(x) for x in e): c})
