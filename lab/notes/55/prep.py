"""Lab for note 55: Frobenius preparation of resonant faces.

Polynomials are dicts {exponent tuple: coefficient mod p}.  Exact tests for
torus critical points use Groebner bases over F_p (sympy), with the
Rabinowitsch variable t.  Over F_p, a Groebner basis equal to [1] certifies
that there is no solution over the algebraic closure.

Usage: python prep.py SEED COUNT   (writes JSON lines to stdout)
"""
import itertools, json, random, sys
from sympy import symbols, groebner, Poly

T = symbols('t')
XS = symbols('x1 x2 x3')


def padd(a, b, p):
    r = dict(a)
    for e, c in b.items():
        r[e] = (r.get(e, 0) + c) % p
        if r[e] == 0:
            del r[e]
    return r


def pmul(a, b, p):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(i + j for i, j in zip(e1, e2))
            r[e] = (r.get(e, 0) + c1 * c2) % p
    return {e: c for e, c in r.items() if c}


def ppow(a, k, p, n):
    r = {tuple([0] * n): 1}
    for _ in range(k):
        r = pmul(r, a, p)
    return r


def compose(h, images, p, n):
    """h(images[0], ..., images[n-1])"""
    cache = {}
    out = {}
    for e, c in h.items():
        term = {tuple([0] * n): c}
        for i, k in enumerate(e):
            if k:
                key = (i, k)
                if key not in cache:
                    cache[key] = ppow(images[i], k, p, n)
                term = pmul(term, cache[key], p)
        out = padd(out, term, p)
    return out


def clean(h, p):
    return {e: c for e, c in h.items() if any(i % p for i in e)}


def deriv(h, i, p):
    r = {}
    for e, c in h.items():
        if e[i] % p:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = (c * e[i]) % p
    return {e: c for e, c in r.items() if c}


def to_sym(h, n):
    return sum(c * Poly({e: 1}, *XS[:n]).as_expr() for e, c in h.items())


def has_torus_crit(h, p, n, off_zero=False):
    """True iff the gradient of h vanishes at a point of the torus over the
    algebraic closure of F_p (and h != 0 there, if off_zero)."""
    gens = [to_sym(deriv(h, i, p), n) for i in range(n)]
    gens = [g for g in gens if g != 0]
    mon = 1
    for v in XS[:n]:
        mon *= v
    if off_zero:
        mon *= to_sym(h, n)
    G = groebner(gens + [1 - T * mon], T, *XS[:n], modulus=p, order='grevlex')
    return G.exprs != [1]


def resonant(h, p, n):
    S = {tuple(i % p for i in e) for e in h}
    S.discard(tuple([0] * n))
    for w in itertools.product(range(p), repeat=n):
        if all(sum(a * b for a, b in zip(w, c)) % p == 1 for c in S):
            return False
    return True


def faces(h, wt, n):
    """Initial forms of the faces of conv(supp h) of positive dimension.
    All exponents lie on <wt, a> = D, so every face is a compact face of
    the Newton polyhedron."""
    E = list(h)
    out = {tuple(sorted(E))}
    if n == 3:
        for a, b in itertools.combinations(E, 2):
            d = [a[i] - b[i] for i in range(3)]
            u = (wt[1] * d[2] - wt[2] * d[1], wt[2] * d[0] - wt[0] * d[2],
                 wt[0] * d[1] - wt[1] * d[0])
            for s in (1, -1):
                vals = [s * sum(u[i] * e[i] for i in range(3)) for e in E]
                m = min(vals)
                F = tuple(sorted(e for e, v in zip(E, vals) if v == m))
                if len(F) >= 2:
                    out.add(F)
    return [{e: h[e] for e in F} for F in out if len(F) >= 2]


def vertex_ok(h, p):
    return all(any(i % p for i in e) for e in h)


def nondeg(h, p, n, wt):
    if not h or not vertex_ok(h, p):
        return False
    for f in sorted(faces(h, wt, n), key=len, reverse=True):
        if has_torus_crit(f, p, n):
            return False
    return True


def evalp(h, v, p):
    s = 0
    for e, c in h.items():
        t = c
        for vi, k in zip(v, e):
            t = t * pow(vi, k, p) % p
        s += t
    return s % p


def rational_torus_crit(h, p, n):
    ders = [deriv(h, i, p) for i in range(n)]
    for v in itertools.product(range(1, p), repeat=n):
        if all(evalp(d, v, p) == 0 for d in ders):
            return True
    return False


def monomials(wt, D, n):
    rng = [range(D // w + 1) for w in wt]
    return [a for a in itertools.product(*rng)
            if sum(x * y for x, y in zip(a, wt)) == D]


def proj_reps(m, p):
    """Nonzero vectors of F_p^m with first nonzero entry 1."""
    out = []
    for v in itertools.product(range(p), repeat=m):
        nz = [x for x in v if x]
        if nz and nz[0] == 1:
            out.append(v)
    return out


def det(M, p):
    m = len(M)
    if m == 1:
        return M[0][0] % p
    if m == 2:
        return (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % p
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])) % p


def block_matrices(m, p):
    """Invertible m x m matrices up to column scaling and column order."""
    if m == 1:
        return [((1,),)]
    reps = proj_reps(m, p)
    out = []
    for cols in itertools.combinations(reps, m):
        M = tuple(tuple(cols[j][i] for j in range(m)) for i in range(m))
        if det(M, p):
            out.append(M)
    return out


def group_elements(wt, D, p, n, rng, max_nonlin=150):
    """Weight-preserving substitutions x_i -> (linear part) + (nonlinear
    part).  Yields (kind, images)."""
    blocks = {}
    for i, w in enumerate(wt):
        blocks.setdefault(w, []).append(i)
    blist = sorted(blocks.items())
    lin_choices = [block_matrices(len(idx), p) for _, idx in blist]
    # nonlinear monomials for each variable
    nonlin = []
    for i in range(n):
        ms = []
        for a in monomials(wt, wt[i], n):
            if sum(a) >= 2:
                ms.append(a)
        nonlin.append(ms)
    nl_slots = [(i, a) for i in range(n) for a in nonlin[i]]
    if p ** len(nl_slots) <= max_nonlin:
        nl_vecs = list(itertools.product(range(p), repeat=len(nl_slots)))
    else:
        nl_vecs = [tuple([0] * len(nl_slots))] + [
            tuple(rng.randrange(p) for _ in nl_slots) for _ in range(max_nonlin)]
    zero = tuple([0] * len(nl_slots))
    for nlv in [zero] + [v for v in nl_vecs if v != zero]:
        for mats in itertools.product(*lin_choices):
            images = [dict() for _ in range(n)]
            for (w, idx), M in zip(blist, mats):
                for r, i in enumerate(idx):
                    for c, j in enumerate(idx):
                        if M[r][c]:
                            e = [0] * n
                            e[j] = 1
                            images[i][tuple(e)] = M[r][c]
            for (i, a), c in zip(nl_slots, nlv):
                if c:
                    images[i] = padd(images[i], {a: c}, p)
            yield ('linear' if nlv == zero else 'frobenius'), images


def prepare(h, wt, D, p, n, rng):
    tried = 0
    for kind, images in group_elements(wt, D, p, n, rng):
        g = clean(compose(h, images, p, n), p)
        tried += 1
        if not g:
            continue
        if rational_torus_crit(g, p, n):
            continue
        if nondeg(g, p, n, wt):
            return kind, images, g, tried
    return None, None, None, tried


WEIGHTS = {2: [(1, 1), (1, 2), (1, 3), (2, 3)],
           3: [(1, 1, 1), (1, 1, 2), (1, 2, 2), (1, 2, 3)]}


def main():
    seed, count = int(sys.argv[1]), int(sys.argv[2])
    ps = [int(a) for a in sys.argv[3].split(',')] if len(sys.argv) > 3 else [2, 3, 5]
    ns = [int(a) for a in sys.argv[4].split(',')] if len(sys.argv) > 4 else [2, 3]
    rng = random.Random(seed)
    for p in ps:
        for n in ns:
            for wt in WEIGHTS[n]:
                for D in (p, 2 * p, 3 * p):
                    if n == 3 and p == 5 and D > 10:
                        continue
                    if n == 3 and p == 3 and D > 6 and wt == (1, 1, 1):
                        continue
                    mons = [a for a in monomials(wt, D, n) if any(i % p for i in a)]
                    if len(mons) < 2:
                        continue
                    found, attempts = 0, 0
                    while found < count and attempts < 40 * count:
                        attempts += 1
                        if rng.random() < 0.5:
                            k = rng.randint(2, min(5, len(mons)))
                            sup = rng.sample(mons, k)
                            h = {a: rng.randrange(1, p) for a in sup}
                        else:
                            h = {a: rng.randrange(p) for a in mons}
                            h = {a: c for a, c in h.items() if c}
                        if len(h) < 2 or not resonant(h, p, n):
                            continue
                        if not has_torus_crit(h, p, n):
                            continue
                        found += 1
                        off = has_torus_crit(h, p, n, off_zero=True)
                        kind, images, g, tried = prepare(h, wt, D, p, n, rng)
                        rec = dict(p=p, n=n, wt=wt, D=D,
                                   h=sorted([list(e), c] for e, c in h.items()),
                                   off_zero=off, prepared=kind, tried=tried)
                        if kind:
                            rec['images'] = [sorted([list(e), c] for e, c in im.items()) for im in images]
                            rec['g'] = sorted([list(e), c] for e, c in g.items())
                        print(json.dumps(rec), flush=True)


if __name__ == '__main__':
    main()
