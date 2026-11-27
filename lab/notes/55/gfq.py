"""Finite fields GF(p^k) with log tables, univariate polynomials over them,
and polynomials in several variables as dicts {exponent: element}."""
import itertools


class GF:
    def __init__(self, p, k):
        self.p, self.k, self.q = p, k, p ** k
        self.mod = self._irreducible() if k > 1 else None
        self._tables()

    # elements are ints 0..q-1, digits base p = coefficients of 1, a, a^2, ...
    def _digits(self, x):
        d = []
        for _ in range(self.k):
            d.append(x % self.p)
            x //= self.p
        return d

    def _int(self, d):
        x = 0
        for c in reversed(d):
            x = x * self.p + c
        return x

    def _irreducible(self):
        p, k = self.p, self.k
        for tail in itertools.product(range(p), repeat=k):
            f = list(tail) + [1]  # monic, f[i] coefficient of a^i
            if f[0] == 0:
                continue
            # no roots / no factors: test by checking x^(p^k) = x mod f and
            # gcd conditions; brute force for small sizes: no factor of degree <= k/2
            if self._is_irred(f):
                return f
        raise ValueError

    def _is_irred(self, f):
        p, k = self.p, len(f) - 1
        for d in range(1, k // 2 + 1):
            for tail in itertools.product(range(p), repeat=d):
                g = list(tail) + [1]
                if self._polymod(f, g) == [0] * d:
                    return False
        return True

    def _polymod(self, f, g):
        p = self.p
        f = list(f)
        dg = len(g) - 1
        while len(f) - 1 >= dg:
            c = f[-1]
            if c:
                s = len(f) - 1 - dg
                for i, gi in enumerate(g):
                    f[s + i] = (f[s + i] - c * gi) % p
            f.pop()
        f += [0] * (dg - len(f))
        return f

    def _mulraw(self, x, y):
        p, k = self.p, self.k
        a, b = self._digits(x), self._digits(y)
        r = [0] * (2 * k - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % p
        if k > 1:
            r = self._polymod(r, self.mod)
        return self._int(r[:k])

    def _tables(self):
        q = self.q
        for g in range(2, q) if q > 2 else [1]:
            exp = [1]
            x = 1
            for _ in range(q - 2):
                x = self._mulraw(x, g)
                exp.append(x)
            if len(set(exp)) == q - 1:
                break
        self.exp = exp + exp
        self.log = [None] * q
        for i, e in enumerate(exp):
            self.log[e] = i
        self.gen = g if q > 2 else 1

    def add(self, x, y):
        p = self.p
        if self.k == 1:
            return (x + y) % p
        a, b = self._digits(x), self._digits(y)
        return self._int([(u + v) % p for u, v in zip(a, b)])

    def neg(self, x):
        return self._int([(-u) % self.p for u in self._digits(x)])

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        if x == 0 or y == 0:
            return 0
        return self.exp[self.log[x] + self.log[y]]

    def inv(self, x):
        return self.exp[(self.q - 1 - self.log[x]) % (self.q - 1)]

    def pw(self, x, e):
        if e == 0:
            return 1
        if x == 0:
            return 0
        return self.exp[(self.log[x] * e) % (self.q - 1)]

    def frompf(self, c):
        """embed an element of F_p"""
        return c % self.p

    def elements(self):
        return range(self.q)


# univariate polynomials: lists of coefficients, low degree first
def utrim(f):
    f = list(f)
    while f and f[-1] == 0:
        f.pop()
    return f


def umod(F, f, g):
    f, g = utrim(f), utrim(g)
    ig = F.inv(g[-1])
    while len(f) >= len(g):
        c = F.mul(f[-1], ig)
        s = len(f) - len(g)
        for i, gi in enumerate(g):
            f[s + i] = F.sub(f[s + i], F.mul(c, gi))
        f = utrim(f)
    return f


def ugcd(F, f, g):
    f, g = utrim(f), utrim(g)
    while g:
        f, g = g, umod(F, f, g)
    return f


def uroots(F, f):
    f = utrim(f)
    out = []
    for a in F.elements():
        v, xp = 0, 1
        for c in f:
            v = F.add(v, F.mul(c, xp))
            xp = F.mul(xp, a)
        if v == 0:
            out.append(a)
    return out


# multivariate dict polynomials over F
def madd(F, a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = F.add(r.get(e, 0), c)
        if r[e] == 0:
            del r[e]
    return r


def mmul(F, a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(i + j for i, j in zip(e1, e2))
            r[e] = F.add(r.get(e, 0), F.mul(c1, c2))
    return {e: c for e, c in r.items() if c}


def mcompose(F, h, images, n):
    cache = {}
    out = {}
    one = {tuple([0] * n): 1}
    for e, c in h.items():
        term = {tuple([0] * n): c}
        for i, k in enumerate(e):
            for _ in range(k):
                term = mmul(F, term, images[i])
        out = madd(F, out, term)
    return out


def mclean(F, h):
    p = F.p
    return {e: c for e, c in h.items() if any(i % p for i in e)}


def meval(F, h, v):
    s = 0
    for e, c in h.items():
        t = c
        for vi, k in zip(v, e):
            t = F.mul(t, F.pw(vi, k))
        s = F.add(s, t)
    return s


def mderiv(F, h, i):
    p = F.p
    r = {}
    for e, c in h.items():
        if e[i] % p:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = F.mul(c, e[i] % p)
    return {e: c for e, c in r.items() if c}


def edge_has_torus_crit(F, f, n):
    """f has support on a segment a0 + j u (u primitive).  Decide whether f
    has a torus critical point over the algebraic closure, by a univariate
    gcd: x_i d_i f = sum_j c_j (a0_i + j u_i) x^(a0+ju), and x^u takes every
    value of the multiplicative group on the torus."""
    E = sorted(f)
    if len(E) == 1:
        return all(i % F.p == 0 for i in E[0])
    a0 = E[0]
    d = [E[-1][i] - a0[i] for i in range(n)]
    from math import gcd
    g = 0
    for x in d:
        g = gcd(g, abs(x))
    u = [x // g for x in d]
    polys = []
    for i in range(n):
        P = [0] * (g + 1)
        for e, c in f.items():
            j = (e[0] - a0[0]) // u[0] if u[0] else (e[1] - a0[1]) // u[1] if u[1] else (e[2] - a0[2]) // u[2]
            P[j] = F.mul(c, (a0[i] + j * u[i]) % F.p)
        polys.append(P)
    G = []
    for P in polys:
        G = ugcd(F, G, P) if G else utrim(P)
    G = utrim(G)
    if not G:
        return True
    while G and G[0] == 0:
        G = G[1:]
    return len(G) > 1
