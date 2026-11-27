"""Independent tools for note 60 (referee of note 55).

Polynomials over F_p are dicts {exponent tuple: coefficient in 0..p-1}.
Exact tests use sympy Groebner bases over F_p with a Rabinowitsch variable;
point counts use galois (finite fields F_{p^k}).
"""
import itertools
import sympy as sp

XS = sp.symbols('x1 x2 x3 x4')
TT = sp.Symbol('t')


def norm(h, p):
    return {a: c % p for a, c in h.items() if c % p}


def add(f, g, p):
    r = dict(f)
    for a, c in g.items():
        r[a] = (r.get(a, 0) + c) % p
    return norm(r, p)


def mul(f, g, p):
    r = {}
    for a, c in f.items():
        for b, d in g.items():
            e = tuple(i + j for i, j in zip(a, b))
            r[e] = (r.get(e, 0) + c * d) % p
    return norm(r, p)


def power(f, k, p, n):
    r = {tuple([0] * n): 1}
    for _ in range(k):
        r = mul(r, f, p)
    return r


def compose(h, images, p, n):
    """h(images[0], ..., images[n-1]); images are polynomials in n variables."""
    cache = {}
    res = {}
    for a, c in h.items():
        term = {tuple([0] * n): c}
        for i, ai in enumerate(a):
            if ai:
                key = (i, ai)
                if key not in cache:
                    cache[key] = power(images[i], ai, p, n)
                term = mul(term, cache[key], p)
        res = add(res, term, p)
    return res


def clean(h, p):
    return {a: c for a, c in h.items() if any(ai % p for ai in a)}


def deriv(h, i, p):
    r = {}
    for a, c in h.items():
        if a[i] % p:
            b = list(a)
            b[i] -= 1
            r[tuple(b)] = (c * a[i]) % p
    return norm(r, p)


def resonant(h, p, n):
    S = list(h)
    for w in itertools.product(range(p), repeat=n):
        if all(sum(wi * ai for wi, ai in zip(w, a)) % p == 1 for a in S):
            return False
    return True


def sym(h, n):
    return sp.Add(*[c * sp.Mul(*[XS[i] ** a[i] for i in range(n)]) for a, c in h.items()])


def torus_test(h, p, n, mode='crit'):
    """True if there is a torus point over the algebraic closure with:
    mode 'crit': grad h = 0; 'off': grad h = 0, h != 0; 'sing': grad h = 0, h = 0."""
    ders = [deriv(h, i, p) for i in range(n)]
    gens = [sym(d, n) for d in ders if d]
    mon = sp.Mul(*XS[:n])
    hs = sym(h, n)
    if mode == 'off':
        mon = mon * hs
    if mode == 'sing':
        gens.append(hs)
    if not gens:
        gens = [sp.Integer(0)]
    G = sp.groebner(gens + [1 - TT * mon], TT, *XS[:n], modulus=p, order='grevlex')
    return list(G.exprs) != [1]


def faces(h, n):
    """Faces of the convex hull of supp(h), for h weighted homogeneous (support in an
    affine hyperplane with positive normal), n = 2 or 3.  Returns list of sub-dicts."""
    S = sorted(h)
    if len(S) == 1:
        return [dict(h)]
    if n == 2:
        return [dict(h), {S[0]: h[S[0]]}, {S[-1]: h[S[-1]]}]
    P = {a: (a[0], a[1]) for a in S}

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    pts = [P[a] for a in S]
    collinear = all(cross(pts[0], pts[1], q) == 0 for q in pts)
    # choose two distinct projected points for collinearity test
    distinct = sorted(set(pts))
    collinear = all(cross(distinct[0], distinct[1], q) == 0 for q in distinct)
    out = [dict(h)]
    if collinear:
        ends = [distinct[0], distinct[-1]]
        for e in ends:
            out.append({a: h[a] for a in S if P[a] == e})
        return out
    edges = set()
    verts = set()
    for u, v in itertools.combinations(distinct, 2):
        cr = [cross(u, v, q) for q in distinct]
        if all(c >= 0 for c in cr) or all(c <= 0 for c in cr):
            on = frozenset(q for q, c in zip(distinct, cr) if c == 0)
            edges.add(on)
    for e in edges:
        out.append({a: h[a] for a in S if P[a] in e})
        es = sorted(e)
        verts.add(es[0])
        verts.add(es[-1])
    for v in verts:
        out.append({a: h[a] for a in S if P[a] == v})
    return out


def nondeg_all_faces(h, p, n, top_only=False):
    """True if no face of conv(supp h) has a torus critical point."""
    if not h:
        return False
    fs = faces(h, n)
    if top_only:
        fs = fs[:1]
    for f in fs:
        if torus_test(f, p, n, 'crit'):
            return False
    return True


def from_json(hl):
    return {tuple(a): c for a, c in hl}
