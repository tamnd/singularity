"""Polynomials in n variables over a finite field.

A polynomial is a dict from exponent tuples to nonzero field elements, wrapped in the class Poly. The class Ring has the field and the names of the variables, and parses and prints polynomials.
"""

import re
from functools import lru_cache

from .field import field as _field


def binom_mod(n, k, p):
    """The binomial coefficient C(n, k) mod p, by the theorem of Lucas."""
    if k < 0 or k > n:
        return 0
    r = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        num = den = 1
        for i in range(b):
            num = num * (a - i) % p
            den = den * (i + 1) % p
        r = r * num * pow(den, p - 2, p) % p
        n //= p
        k //= p
    return r


@lru_cache(maxsize=1 << 16)
def binomial_terms(F, a, t):
    """The terms (s, c) of (X + t)^a = sum_s c X^s over the field F. Only the s with C(a, s) != 0 mod p occur."""
    if t == 0:
        return ((a, 1),)
    p = F.p
    digits = []
    m = a
    while m:
        digits.append(m % p)
        m //= p
    out = [(0, 1)]
    place = 1
    for dgt in digits:
        nxt = []
        for s, c in out:
            for b in range(dgt + 1):
                cb = binom_mod(dgt, b, p)
                if cb:
                    nxt.append((s + b * place, c * cb % p))
        out = nxt
        place *= p
    return tuple((s, F.mul(F.from_int(c), F.pow(t, a - s))) for s, c in out)


class Ring:
    """The polynomial ring F[x_1, ..., x_n] with named variables."""

    def __init__(self, F, names):
        if isinstance(names, str):
            names = [v.strip() for v in names.split(",") if v.strip()]
        self.F = F
        self.names = list(names)
        self.n = len(self.names)
        if len(set(self.names)) != self.n:
            raise ValueError("the names of the variables must be distinct")

    @classmethod
    def over(cls, p, names, k=1):
        return cls(_field(p, k), names)

    def index(self, v):
        """The index of a variable, given by its name or its index."""
        if isinstance(v, int):
            if not 0 <= v < self.n:
                raise IndexError(v)
            return v
        return self.names.index(v)

    def indices(self, vs):
        return frozenset(self.index(v) for v in vs)

    def zero(self):
        return Poly(self, {})

    def const(self, c):
        return Poly(self, {(0,) * self.n: c} if c else {})

    def var(self, v):
        e = [0] * self.n
        e[self.index(v)] = 1
        return Poly(self, {tuple(e): 1})

    def monomial(self, exps, c=1):
        return Poly(self, {tuple(exps): c} if c else {})

    def parse(self, text):
        """Parse an expression with + - * ^ ** and parentheses. A coefficient is an integer, read mod p, or #c for the field element with the code c."""
        return _Parser(self, text).parse()

    def __call__(self, text):
        return self.parse(text)

    def __eq__(self, other):
        return isinstance(other, Ring) and self.F is other.F and self.names == other.names

    def __hash__(self):
        return hash((id(self.F), tuple(self.names)))


class Poly:
    """A polynomial: a ring and a dict from exponent tuples to nonzero coefficients."""

    __slots__ = ("ring", "terms")

    def __init__(self, ring, terms):
        self.ring = ring
        self.terms = terms

    @property
    def F(self):
        return self.ring.F

    # Arithmetic.
    def _add_into(self, out, e, c):
        F = self.ring.F
        v = F.add(out.get(e, 0), c)
        if v:
            out[e] = v
        else:
            out.pop(e, None)

    def __add__(self, other):
        other = self._coerce(other)
        out = dict(self.terms)
        for e, c in other.terms.items():
            self._add_into(out, e, c)
        return Poly(self.ring, out)

    __radd__ = __add__

    def __neg__(self):
        F = self.ring.F
        return Poly(self.ring, {e: F.neg(c) for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        F = self.ring.F
        out = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                self._add_into(out, tuple(a + b for a, b in zip(e1, e2)), F.mul(c1, c2))
        return Poly(self.ring, out)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            raise ValueError("negative power")
        r, a = self.ring.const(1), self
        while n:
            if n & 1:
                r = r * a
            a = a * a
            n >>= 1
        return r

    def scale(self, c):
        F = self.ring.F
        if c == 0:
            return self.ring.zero()
        return Poly(self.ring, {e: F.mul(c, v) for e, v in self.terms.items()})

    def _coerce(self, other):
        if isinstance(other, Poly):
            if other.ring != self.ring:
                raise ValueError("the polynomials are in different rings")
            return other
        if isinstance(other, int):
            return self.ring.const(self.ring.F.from_int(other))
        raise TypeError(other)

    def __eq__(self, other):
        if isinstance(other, int):
            other = self.ring.const(self.ring.F.from_int(other))
        return isinstance(other, Poly) and self.ring == other.ring and self.terms == other.terms

    def __hash__(self):
        return hash(frozenset(self.terms.items()))

    def __bool__(self):
        return bool(self.terms)

    def __len__(self):
        return len(self.terms)

    # Orders and forms.
    def order(self):
        """The order at the origin. None for the zero polynomial."""
        return min(sum(e) for e in self.terms) if self.terms else None

    def order_along(self, S):
        """The order along the coordinate stratum V(x_i, i in S). None for zero."""
        S = self.ring.indices(S)
        return min(sum(e[i] for i in S) for e in self.terms) if self.terms else None

    def degree(self):
        return max(sum(e) for e in self.terms) if self.terms else None

    def initial_form(self):
        d = self.order()
        return Poly(self.ring, {e: c for e, c in self.terms.items() if sum(e) == d})

    def coefficient(self, exps):
        return self.terms.get(tuple(exps), 0)

    def deriv(self, i):
        """The partial derivative in the variable i."""
        i = self.ring.index(i)
        F = self.ring.F
        out = {}
        for e, c in self.terms.items():
            if e[i] % F.p:
                e2 = list(e)
                e2[i] -= 1
                out[tuple(e2)] = F.mul(F.from_int(e[i]), c)
        return Poly(self.ring, out)

    def log_deriv(self, i):
        """x_i times the partial derivative in x_i."""
        i = self.ring.index(i)
        F = self.ring.F
        return Poly(self.ring, {e: F.mul(F.from_int(e[i]), c) for e, c in self.terms.items() if e[i] % F.p})

    def monomial_factor(self, E):
        """The exponents r with r_i = min exponent of x_i for i in E and r_i = 0 outside E."""
        E = self.ring.indices(E)
        if not self.terms:
            return (0,) * self.ring.n
        return tuple(min(e[i] for e in self.terms) if i in E else 0 for i in range(self.ring.n))

    def divide_monomial(self, r):
        out = {}
        for e, c in self.terms.items():
            e2 = tuple(a - b for a, b in zip(e, r))
            if min(e2) < 0:
                raise ValueError("the monomial does not divide the polynomial")
            out[e2] = c
        return Poly(self.ring, out)

    def times_monomial(self, r):
        return Poly(self.ring, {tuple(a + b for a, b in zip(e, r)): c for e, c in self.terms.items()})

    def is_constant(self):
        return all(sum(e) == 0 for e in self.terms)

    def value_at_origin(self):
        return self.terms.get((0,) * self.ring.n, 0)

    def substitute(self, images):
        """Substitute the polynomial images[i] for x_i. A missing image keeps x_i."""
        R = self.ring
        imgs = [images.get(i, images.get(R.names[i])) if isinstance(images, dict) else images[i] for i in range(R.n)]
        imgs = [R.var(i) if v is None else v for i, v in enumerate(imgs)]
        powers = [dict() for _ in range(R.n)]

        def pw(i, a):
            if a not in powers[i]:
                powers[i][a] = imgs[i] ** a
            return powers[i][a]

        out = R.zero()
        for e, c in self.terms.items():
            t = R.const(c)
            for i, a in enumerate(e):
                if a:
                    t = t * pw(i, a)
            out = out + t
        return out

    def translate(self, t):
        """Substitute x_i + t_i for x_i. t is a dict from variables to field elements."""
        R, F = self.ring, self.ring.F
        shifts = {R.index(v): c for v, c in t.items() if c}
        if not shifts:
            return self
        out = {}
        for e, c in self.terms.items():
            parts = [((), c)]
            for i in range(R.n):
                if i in shifts:
                    bt = binomial_terms(F, e[i], shifts[i])
                    parts = [(pre + (s,), F.mul(cc, cs)) for pre, cc in parts for s, cs in bt]
                else:
                    parts = [(pre + (e[i],), cc) for pre, cc in parts]
            for e2, c2 in parts:
                self._add_into(out, e2, c2)
        return Poly(self.ring, out)

    # Printing.
    def __str__(self):
        if not self.terms:
            return "0"
        R, F = self.ring, self.ring.F
        parts = []
        for e in sorted(self.terms, key=lambda e: (sum(e), [-a for a in e])):
            c = self.terms[e]
            mono = "*".join(R.names[i] + (f"^{a}" if a > 1 else "") for i, a in enumerate(e) if a)
            cs = str(c) if c < F.p else f"#{c}"
            if not mono:
                parts.append(cs)
            elif c == 1:
                parts.append(mono)
            else:
                parts.append(f"{cs}*{mono}")
        return " + ".join(parts)

    def __repr__(self):
        return f"Poly({self})"


_TOKEN = re.compile(r"\s*(?:(\d+)|#(\d+)|([A-Za-z_][A-Za-z_0-9]*)|(\*\*|[-+*^()]))")


class _Parser:
    def __init__(self, ring, text):
        self.R = ring
        self.toks = []
        pos = 0
        text = text.strip()
        while pos < len(text):
            m = _TOKEN.match(text, pos)
            if not m or m.end() == pos:
                raise ValueError(f"cannot parse {text[pos:]!r}")
            num, code, name, op = m.groups()
            if num is not None:
                self.toks.append(("num", int(num)))
            elif code is not None:
                self.toks.append(("code", int(code)))
            elif name is not None:
                self.toks.append(("name", name))
            else:
                self.toks.append(("op", "^" if op == "**" else op))
            pos = m.end()
        self.i = 0

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else (None, None)

    def take(self):
        t = self.peek()
        self.i += 1
        return t

    def parse(self):
        r = self.expr()
        if self.i != len(self.toks):
            raise ValueError(f"unexpected token {self.peek()[1]!r}")
        return r

    def expr(self):
        kind, val = self.peek()
        sign = 1
        if (kind, val) in (("op", "-"), ("op", "+")):
            self.take()
            sign = -1 if val == "-" else 1
        r = self.term()
        if sign < 0:
            r = -r
        while self.peek() in (("op", "+"), ("op", "-")):
            _, op = self.take()
            t = self.term()
            r = r + t if op == "+" else r - t
        return r

    def term(self):
        r = self.factor()
        while True:
            kind, val = self.peek()
            if (kind, val) == ("op", "*"):
                self.take()
                r = r * self.factor()
            elif kind in ("num", "code", "name") or (kind, val) == ("op", "("):
                r = r * self.factor()
            else:
                return r

    def factor(self):
        base = self.atom()
        if self.peek() == ("op", "^"):
            self.take()
            kind, val = self.take()
            if kind != "num":
                raise ValueError("an exponent must be a number")
            return base ** val
        return base

    def atom(self):
        kind, val = self.take()
        R = self.R
        if kind == "num":
            return R.const(R.F.from_int(val))
        if kind == "code":
            if val >= R.F.size:
                raise ValueError(f"#{val} is not an element of {R.F}")
            return R.const(val)
        if kind == "name":
            return R.var(val)
        if (kind, val) == ("op", "("):
            r = self.expr()
            if self.take() != ("op", ")"):
                raise ValueError("missing )")
            return r
        if (kind, val) == ("op", "-"):
            return -self.factor()
        raise ValueError(f"unexpected token {val!r}")
