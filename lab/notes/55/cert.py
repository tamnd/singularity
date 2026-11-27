"""Certificates for the failures of prep.py in the standard weight.

For a form h of degree D (weight (1,...,1)), Theorem 55.6 says: if the
projective critical set Crit(h) in P^{n-1} is not contained in the union of
n hyperplanes in general position, then no change of coordinates (of any
kind) followed by a cleaning makes z^p + g nondegenerate, for any g with
initial form h.  If it is contained in such a union, we search the changes
x = A x' whose coordinate hyperplanes cover Crit(h), over a field F_q in
which all points of Crit(h) are rational, and test the edges exactly.

Usage: python cert.py run.jsonl ...
"""
import itertools, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import lcm
from sympy import groebner, factor_list, Poly, symbols, gcd as sgcd
from gfq import GF, uroots, mcompose, mclean, meval, mderiv, edge_has_torus_crit
from prep import deriv, to_sym, XS, faces

X1, X2, X3 = XS


def crit_points_n2(h, p):
    """distinct points of V(h_x, h_y) in P^1 over the closure; returns
    (number, splitting degree, list over F_q)"""
    hx, hy = to_sym(deriv(h, 0, p), 2), to_sym(deriv(h, 1, p), 2)
    a = Poly(hx.subs(X2, 1), X1, modulus=p)
    b = Poly(hy.subs(X2, 1), X1, modulus=p)
    g = a.gcd(b)
    fl = g.factor_list()[1] if g.degree() > 0 else []
    k = lcm(1, *[Poly(f, X1, modulus=p).degree() for f, _ in fl]) if fl else 1
    inf = (hx.subs({X1: 1, X2: 0}) % p == 0) and (hy.subs({X1: 1, X2: 0}) % p == 0)
    count = sum(Poly(f, X1, modulus=p).degree() for f, _ in fl) + (1 if inf else 0)
    if g.is_zero:
        return None, None
    return count, k


def eliminant(I, var, others, p):
    G = groebner(I, *others, var, modulus=p, order='lex')
    if G.exprs == [1]:
        return 'empty'
    last = G.exprs[-1]
    if last.free_symbols <= {var}:
        return Poly(last, var, modulus=p)
    return None


def crit_points_n3(h, p):
    """Projective critical points of h in P^2 over the closure of F_p.
    Returns (F, list of points) or (None, reason)."""
    ders = [to_sym(deriv(h, i, p), 3) for i in range(3)]
    charts = []
    # chart x3 = 1
    I = [d.subs(X3, 1) for d in ders]
    I = [d for d in I if d != 0]
    e2 = eliminant(I, X2, [X1], p)
    e1 = eliminant(I, X1, [X2], p)
    if e2 is None or e1 is None:
        return None, 'positive dimensional'
    polys = [e for e in (e1, e2) if e != 'empty']
    # chart x3 = 0, x2 = 1
    J = [d.subs({X3: 0, X2: 1}) for d in ders]
    J = [Poly(d, X1, modulus=p) for d in J if d != 0]
    gJ = None
    if J:
        gJ = J[0]
        for d in J[1:]:
            gJ = gJ.gcd(d)
        if gJ.degree() > 0:
            polys.append(gJ)
    else:
        return None, 'line x3=0 critical'
    degs = []
    for P in polys:
        for f, _ in P.factor_list()[1]:
            degs.append(Poly(f, *P.gens, modulus=p).degree())
    k = lcm(1, *degs)
    if p ** k > 20000:
        return None, 'field too big (k=%d)' % k
    F = GF(p, k)
    hF = {e: F.frompf(c) for e, c in h.items()}
    dF = [mderiv(F, hF, i) for i in range(3)]
    pts = []
    if e1 != 'empty':
        r1 = uroots(F, [F.frompf(int(c)) for c in reversed(e1.all_coeffs())])
        r2 = uroots(F, [F.frompf(int(c)) for c in reversed(e2.all_coeffs())])
        for a in r1:
            for b in r2:
                if all(meval(F, d, (a, b, 1)) == 0 for d in dF):
                    pts.append((a, b, 1))
    if gJ is not None and gJ.degree() > 0:
        for a in uroots(F, [F.frompf(int(c)) for c in reversed(gJ.all_coeffs())]):
            pts.append((a, 1, 0))
    if all(meval(F, d, (1, 0, 0)) == 0 for d in dF):
        pts.append((1, 0, 0))
    return F, pts


def line_through(F, a, b):
    # cross product
    return (F.sub(F.mul(a[1], b[2]), F.mul(a[2], b[1])),
            F.sub(F.mul(a[2], b[0]), F.mul(a[0], b[2])),
            F.sub(F.mul(a[0], b[1]), F.mul(a[1], b[0])))


def on(F, l, v):
    return F.add(F.add(F.mul(l[0], v[0]), F.mul(l[1], v[1])), F.mul(l[2], v[2])) == 0


def normalize(F, l):
    for c in l:
        if c:
            ic = F.inv(c)
            return tuple(F.mul(ic, x) for x in l)


def det3(F, M):
    m = F.mul
    a = m(M[0][0], F.sub(m(M[1][1], M[2][2]), m(M[1][2], M[2][1])))
    b = m(M[0][1], F.sub(m(M[1][0], M[2][2]), m(M[1][2], M[2][0])))
    c = m(M[0][2], F.sub(m(M[1][0], M[2][1]), m(M[1][1], M[2][0])))
    return F.add(F.sub(a, b), c)


def inverse3(F, M):
    d = det3(F, M)
    idt = F.inv(d)
    C = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r = [k for k in range(3) if k != i]
            c = [k for k in range(3) if k != j]
            minor = F.sub(F.mul(M[r[0]][c[0]], M[r[1]][c[1]]), F.mul(M[r[0]][c[1]], M[r[1]][c[0]]))
            if (i + j) % 2:
                minor = F.neg(minor)
            C[j][i] = F.mul(minor, idt)
    return C


def covers(F, pts):
    """All triples of independent lines (as coefficient vectors) covering
    pts, where lines through <= 1 point are enumerated over F."""
    pts = [normalize(F, v) for v in pts]
    rich = set()
    for a, b in itertools.combinations(pts, 2):
        rich.add(normalize(F, line_through(F, a, b)))
    rich = list(rich)
    allLines = None
    out = []
    # choose lines: a line meeting <= 1 point can be any line through that point
    def lines_through(v):
        i = next(j for j in range(3) if v[j])
        iv = F.inv(v[i])
        bs = []
        for j in range(3):
            if j != i:
                l = [0, 0, 0]
                l[j] = 1
                l[i] = F.neg(F.mul(v[j], iv))
                bs.append(tuple(l))
        res = [bs[1]]
        for t in list(F.elements())[:60]:
            res.append(normalize(F, tuple(F.add(a, F.mul(t, b)) for a, b in zip(bs[0], bs[1]))))
        return res
    def rec(chosen, remaining):
        if len(chosen) == 3:
            if not remaining and det3(F, chosen) != 0:
                out.append(tuple(chosen))
            return len(out) > 200
        if not remaining:
            cand = rich + [normalize(F, l) for l in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (1, 2 % F.q, 3 % F.q)] if any(l)]
        else:
            v = remaining[0]
            cand = [l for l in rich if on(F, l, v)] + lines_through(v)[:60]
        for l in cand:
            rem = [u for u in remaining if not on(F, l, u)]
            if rec(chosen + [l], rem):
                return True
        return False
    rec([], pts)
    return out


def prepared_by(F, h, lines, p):
    """new coordinates x'_i = lines[i](x); substitute x = A^{-1} x' and test"""
    Minv = inverse3(F, [list(l) for l in lines])
    n = 3
    images = []
    for i in range(3):
        im = {}
        for j in range(3):
            if Minv[i][j]:
                e = [0] * 3
                e[j] = 1
                im[tuple(e)] = Minv[i][j]
        images.append(im)
    hF = {e: F.frompf(c) for e, c in h.items()}
    g = mclean(F, mcompose(F, hF, images, n))
    if not g:
        return False, None
    for f in faces(g, (1, 1, 1), 3):
        E = sorted(f)
        # is it a segment?
        a0 = E[0]
        d = [[e[i] - a0[i] for i in range(3)] for e in E[1:]]
        rank2 = any(
            any(x[i] * y[j] - x[j] * y[i] for i in range(3) for j in range(3))
            for x, y in itertools.combinations(d, 2))
        if rank2:
            continue  # the whole face: covered by the choice of lines
        if edge_has_torus_crit(F, f, 3):
            return False, g
    return True, g


def main():
    for fn in sys.argv[1:]:
        for line in open(fn):
            r = json.loads(line)
            if r['prepared'] or tuple(r['wt']) not in ((1, 1), (1, 1, 1)):
                continue
            p, n = r['p'], r['n']
            h = {tuple(e): c for e, c in r['h']}
            out = dict(p=p, n=n, D=r['D'], h=r['h'], off_zero=r['off_zero'])
            if n == 2:
                c, k = crit_points_n2(h, p)
                out['crit_points'] = c
                out['verdict'] = 'preparable over closure' if c is not None and c <= 2 else 'certified unpreparable'
            else:
                F, pts = crit_points_n3(h, p)
                if F is None:
                    out['verdict'] = 'undecided: ' + pts
                else:
                    out['q'] = F.q
                    out['crit_points'] = len(pts)
                    cov = covers(F, pts)
                    if not cov:
                        out['verdict'] = 'certified unpreparable'
                    else:
                        ok = False
                        for lines in cov:
                            res, g = prepared_by(F, h, lines, p)
                            if res:
                                ok = True
                                out['lines'] = lines
                                break
                        out['verdict'] = ('prepared over F_%d' % F.q) if ok else 'cover exists, no preparation found'
            print(json.dumps(out), flush=True)


if __name__ == '__main__':
    main()
