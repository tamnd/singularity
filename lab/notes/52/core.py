"""Independent core for note 52: exact arithmetic over F_q (q = p or p^2),
polynomials in x, w, y, z as dicts {(i, l, j, k): c}, steps, cleaning, r, G, d, rho, nu^G.
Written from the definitions of handbook Vol 7, Sections 3.15 and 3.17, not from the scripts of note 50."""
import random, itertools

class F:
    def __init__(self, p, e=1):
        self.p, self.e = p, e
        q = p ** e
        self.q = q
        if e == 1:
            self.add = [[(a + b) % p for b in range(q)] for a in range(q)]
            self.mul = [[(a * b) % p for b in range(q)] for a in range(q)]
        else:
            # F_{p^2} = F_p[t]/(t^2 - n), n a non-residue
            n = next(c for c in range(2, p) if pow(c, (p - 1) // 2, p) == p - 1) if p > 2 else None
            assert n is not None
            def dec(a): return a % p, a // p
            def enc(u, v): return (u % p) + p * (v % p)
            self.add = [[enc(dec(a)[0] + dec(b)[0], dec(a)[1] + dec(b)[1]) for b in range(q)] for a in range(q)]
            def m(a, b):
                (u, v), (s, t) = dec(a), dec(b)
                return enc(u * s + n * v * t, u * t + v * s)
            self.mul = [[m(a, b) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(q) if self.mul[a][b] == 1) for a in range(1, q)]
        self.one = 1
    def fromint(self, k):
        return k % self.p
    def rand(self, nonzero=False):
        return random.randrange(1 if nonzero else 0, self.q)

def padd(K, f, g, s=1):
    """f + s*g, s an element of K"""
    h = dict(f)
    for mo, c in g.items():
        c2 = K.mul[s][c] if s != 1 else c
        v = K.add[h.get(mo, 0)][c2]
        if v: h[mo] = v
        else: h.pop(mo, None)
    return h

def binom_row(K, n, a):
    """coefficients of (X + a)^n : list of (exponent, coeff)"""
    out = []
    from math import comb
    apow = [1]
    for _ in range(n): apow.append(K.mul[apow[-1]][a])
    for s in range(n + 1):
        c = K.mul[K.fromint(comb(n, s))][apow[n - s]]
        if c: out.append((s, c))
    return out

def step(K, g, chart, a, b):
    """blow up, chart 'y' (y=y', z=y'z', x=y'(x'+a), w=y'(w'+b)) or 'z', divide by L^p, clean"""
    p = K.p
    h = {}
    cache = {}
    for (i, l, j, k), c in g.items():
        if (i, a) not in cache: cache[(i, a)] = binom_row(K, i, a)
        if (l, b) not in cache: cache[(l, b)] = binom_row(K, l, b)
        e = i + l + j + k - p
        if chart == 'y':
            yy, zz = e, k
        else:
            yy, zz = j, e
        assert e >= 0, "ord < p"
        for s, cs in cache[(i, a)]:
            cc = K.mul[c][cs]
            for t, ct in cache[(l, b)]:
                mo = (s, t, yy, zz)
                v = K.add[h.get(mo, 0)][K.mul[cc][ct]]
                if v: h[mo] = v
                else: h.pop(mo, None)
    return clean(K, h)

def clean(K, g):
    p = K.p
    return {mo: c for mo, c in g.items() if not all(e % p == 0 for e in mo)}

def deriv(K, g, idx, log=False):
    out = {}
    for mo, c in g.items():
        e = mo[idx]
        if e % K.p == 0: continue
        if log:
            nm = mo
        else:
            nm = list(mo); nm[idx] -= 1; nm = tuple(nm)
        out[nm] = K.mul[c][K.fromint(e)]
    return out

def invariants(K, g):
    """returns dict with r, G, d, rho, initial form, orders on curves/surfaces"""
    gens = [deriv(K, g, 0), deriv(K, g, 1), deriv(K, g, 2, True), deriv(K, g, 3, True)]
    allm = [mo for h in gens for mo in h]
    if not allm:
        return None
    ry = min(mo[2] for mo in allm); rz = min(mo[3] for mo in allm)
    for mo in g: assert mo[2] >= ry and mo[3] >= rz, "Y does not divide g"
    rho = min(sum(mo) - ry - rz for mo in allm)
    G = {(i, l, j - ry, k - rz): c for (i, l, j, k), c in g.items()}
    d = min(sum(mo) for mo in G)
    inG = {mo: c for mo, c in G.items() if sum(mo) == d}
    res = dict(ry=ry, rz=rz, rho=rho, d=d, G=G, inG=inG, ordg=min(sum(mo) for mo in g))
    res['binary'] = all(mo[2] == 0 and mo[3] == 0 for mo in inG)
    res['curve_y'] = min(i + l + j for (i, l, j, k) in G)   # V(x, w, y)
    res['curve_z'] = min(i + l + k for (i, l, j, k) in G)   # V(x, w, z)
    res['surf_y'] = min(i + j for (i, l, j, k) in G)        # V(x, y)
    res['surf_z'] = min(i + k for (i, l, j, k) in G)        # V(x, z)
    return res

def linchange(K, g, c):
    """new coordinates X = x + c w, W = w, i.e. substitute x = X - c W; then clean"""
    negc = K.neg[c]
    h = {}
    for (i, l, j, k), co in g.items():
        # (X + negc W)^i
        for s, cs in binom_row(K, i, 0) if negc == 0 else binom_xy(K, i, negc):
            pass
    return None

def binom_xy(K, n, a):
    """(X + a W)^n: list of (power of X, power of W, coeff)"""
    from math import comb
    apow = [1]
    for _ in range(n): apow.append(K.mul[apow[-1]][a])
    return [(s, n - s, K.mul[K.fromint(comb(n, s))][apow[n - s]]) for s in range(n + 1)
            if K.mul[K.fromint(comb(n, s))][apow[n - s]]]

def subst_x(K, g, c):
    """substitute x = X + c W (W = w); returns poly in (X, W, y, z), cleaned"""
    h = {}
    for (i, l, j, k), co in g.items():
        for s, t, cs in binom_xy(K, i, c):
            mo = (s, l + t, j, k)
            v = K.add[h.get(mo, 0)][K.mul[co][cs]]
            if v: h[mo] = v
            else: h.pop(mo, None)
    return clean(K, h)

def val(mo2, theta):
    return mo2[0] + theta * mo2[1]
