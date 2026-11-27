"""Hasse-derivative version of the characteristic 0 maximal contact tower,
at one point (the origin), over F_p, with truncated power series.

Polynomials: dict {exponent tuple: coefficient mod p}.
Level k: an ideal I_k (list of generators) on a regular germ of dim n-k+1
(coordinates after eliminating chosen variables), with order e_k.
  MC test (Lemma 56.9): Delta^{e-1}(I) has an element of order 1 iff the
  degree-e part of some generator has a monomial with an exponent not
  divisible by p.  (Generators are random combinations, see below.)
  If it passes, pick h = D^{(alpha)} g of order 1, H = V(h), solve h=0 for a
  variable with nonzero linear coefficient, and form Kollar's coefficient ideal
  C = sum_{j<e} (Delta^j I |_H)^{e!/(e-j)}, marker e!, then I_{k+1} = C.
Ideals are represented by a few random F_p-combinations of generators, and
powers A^m by random products of m random elements of A (enough to compute
orders and the MC test with high probability).
"""
import random, itertools, math, sys

class Ring:
    def __init__(s, n, p, T):
        s.n, s.p, s.T = n, p, T
    def trunc(s, f):
        return {e: c for e, c in f.items() if c % s.p and sum(e) <= s.T}
    def add(s, f, g, a=1):
        h = dict(f)
        for e, c in g.items():
            h[e] = (h.get(e, 0) + a * c) % s.p
        return {e: c for e, c in h.items() if c}
    def mul(s, f, g):
        h = {}
        p, T = s.p, s.T
        for e1, c1 in f.items():
            d1 = sum(e1)
            for e2, c2 in g.items():
                if d1 + sum(e2) > T: continue
                e = tuple(a + b for a, b in zip(e1, e2))
                h[e] = (h.get(e, 0) + c1 * c2) % p
        return {e: c for e, c in h.items() if c}
    def pow(s, f, m):
        r = {tuple([0] * s.n): 1}
        b = f
        while m:
            if m & 1: r = s.mul(r, b)
            m >>= 1
            if m: b = s.mul(b, b)
        return r
    def order(s, f):
        return min((sum(e) for e in f), default=math.inf)
    def part(s, f, d):
        return {e: c for e, c in f.items() if sum(e) == d}
    def binom(s, a, b):
        # Lucas
        p, r = s.p, 1
        while a or b:
            x, y = a % p, b % p
            if y > x: return 0
            r = r * math.comb(x, y) % p
            a //= p; b //= p
        return r
    def hasse(s, f, al):
        h = {}
        for e, c in f.items():
            if all(x >= y for x, y in zip(e, al)):
                b = 1
                for x, y in zip(e, al):
                    b = b * s.binom(x, y) % s.p
                    if not b: break
                if b:
                    ee = tuple(x - y for x, y in zip(e, al))
                    h[ee] = (h.get(ee, 0) + c * b) % s.p
        return {e: c for e, c in h.items() if c}

def multi_indices(n, d):
    for c in itertools.combinations_with_replacement(range(n), d):
        a = [0] * n
        for i in c: a[i] += 1
        yield tuple(a)

def mc_test(R, gens, e):
    """Return (pass?, h) with h = D^alpha g of order 1, from the degree-e parts."""
    for g in gens:
        F = R.part(g, e)
        for b, c in F.items():
            for j in range(R.n):
                if b[j] % R.p:
                    al = list(b); al[j] -= 1
                    h = {}
                    for d in range(1, R.T - (e - 1) + 1):
                        pass
                    h = R.hasse(g, tuple(al))
                    return True, h
    return False, None

def solve_and_restrict(R, h, polys):
    """h has order 1; pick variable i with nonzero linear coefficient,
    solve x_i = phi(others) mod deg T+1, substitute into polys.
    Returns new ring of n-1 variables and the restricted polys."""
    n, p = R.n, R.p
    lin = {e: c for e, c in h.items() if sum(e) == 1}
    i = min(e.index(1) for e in lin)
    ei = tuple(1 if k == i else 0 for k in range(n))
    c = h[ei]; cinv = pow(c, p - 2, p)
    rest = {e: (-cv * cinv) % p for e, cv in h.items() if e != ei}
    # phi as series in all n vars but with x_i eliminated iteratively
    phi = {}
    for it in range(R.T + 1):
        new = subst(R, rest, i, phi)
        if new == phi: break
        phi = new
    out = [drop(subst(R, f, i, phi), i) for f in polys]
    return Ring(n - 1, p, R.T), out

def subst(R, f, i, phi):
    """substitute x_i = phi (phi has no x_i) into f, truncated."""
    res = {}
    byk = {}
    for e, c in f.items():
        k = e[i]
        ee = list(e); ee[i] = 0
        byk.setdefault(k, {})[tuple(ee)] = c
    powc = {0: {tuple([0] * R.n): 1}}
    for k in sorted(byk):
        if k not in powc:
            m = max(powc)
            q = powc[m]
            while m < k:
                q = R.mul(q, phi); m += 1; powc[m] = q
        res = R.add(res, R.mul(byk[k], powc[k]))
    return res

def drop(f, i):
    return {e[:i] + e[i + 1:]: c for e, c in f.items()}

def rand_comb(R, gens, k=3):
    out = []
    for _ in range(k):
        r = {}
        for g in gens:
            r = R.add(r, g, random.randrange(1, R.p))
        out.append(r)
    return out

def delta_j(R, gens, j):
    out = []
    for g in gens:
        for al in multi_indices(R.n, j):
            d = R.hasse(g, al)
            if d: out.append(d)
    return out

def tower(R, gens, maxlev=4, ncomb=3, verbose=False):
    """Returns list of (level, dim, order, status)."""
    log = []
    level = 1
    while True:
        e = min(R.order(g) for g in gens) if gens else math.inf
        if e == math.inf or e > R.T:
            log.append((level, R.n, '>T', 'stop: order beyond truncation'))
            return log
        if e == 0:
            log.append((level, R.n, 0, 'unit ideal'))
            return log
        if R.n == 1:
            log.append((level, 1, e, 'dim 1, end'))
            return log
        ok, h = mc_test(R, gens, e)
        if not ok:
            log.append((level, R.n, e, 'FAIL: degree-e part in k[x^p]'))
            return log
        log.append((level, R.n, e, 'pass'))
        if level >= maxlev:
            return log
        # coefficient ideal (Kollar): sum_j (Delta^j I|_H)^{e!/(e-j)}
        L = math.factorial(e)
        comps = []
        for j in range(e):
            Dj = delta_j(R, gens, j) if j else list(gens)
            comps.append((j, rand_comb(R, Dj, ncomb)))
        allp = [g for _, cs in comps for g in cs]
        R2, rest = solve_and_restrict(R, h, allp)
        newgens = []
        pos = 0
        for j, cs in comps:
            rc = rest[pos:pos + len(cs)]; pos += len(cs)
            m = L // (e - j)
            o = min(R2.order(g) for g in rc)
            if o == math.inf or o * m > R2.T:
                continue
            for _ in range(ncomb):
                prod = {tuple([0] * R2.n): 1}
                for _ in range(m):
                    a = {}
                    for g in rc:
                        a = R2.add(a, g, random.randrange(1, R2.p))
                    prod = R2.mul(prod, a)
                newgens.append(prod)
        if not newgens:
            log.append((level + 1, R2.n, '>T', 'stop: order beyond truncation'))
            return log
        R, gens = R2, rand_comb(R2, newgens, ncomb)
        level += 1
