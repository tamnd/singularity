"""Referee 63: Hahn field model of a run along the Euclid word of theta = sqrt(2) - 1.

Checks Theorem 3.2 (a), (b), (c) and Proposition 4.1 of note 54 and the divisibility step of
Theorem 5.1, for random f in F_p[y0, z0][X, W], with planar translations; and the same with
linear translations (a_j = c b_j) as a control.
usage: hahn63.py p D ntrials levels mode seed     mode in planar, sparse, linear, adv
"""
import sys, random, math
from math import comb

TH = math.sqrt(2) - 1


def val(e):
    return e[0] + TH * e[1]


def run_word(levels):
    """returns lists Y[m], Z[m] (exponents of y_m, z_m in y0, z0), chart, M[m]"""
    Y, Z, M = [(1, 0)], [(0, 1)], [(0, 0)]
    charts = []
    for m in range(levels):
        y, z = Y[-1], Z[-1]
        if val(y) > val(z):  # z-chart: y_{m+1} = y_m / z_m, z_{m+1} = z_m, L = z_{m+1}
            charts.append('z')
            Y.append((y[0] - z[0], y[1] - z[1])); Z.append(z); L = z
        else:
            charts.append('y')
            Z.append((z[0] - y[0], z[1] - y[1])); Y.append(y); L = y
        M.append((M[-1][0] + L[0], M[-1][1] + L[1]))
    return Y, Z, M, charts


def to_level(e, y, z):
    """write the Laurent monomial e in y0, z0 as y_m^s z_m^t, with y_m = y, z_m = z"""
    det = y[0] * z[1] - y[1] * z[0]
    s = (e[0] * z[1] - e[1] * z[0]) // det
    t = (y[0] * e[1] - y[1] * e[0]) // det
    assert s * y[0] + t * z[0] == e[0] and s * y[1] + t * z[1] == e[1]
    return s, t


class P:
    """elements: dict {(a, b): c mod p}; polynomials in X, W: dict {(k, l, a, b): c}"""
    def __init__(self, p):
        self.p = p

    def add(self, d, key, c):
        c %= self.p
        if not c:
            return
        s = (d.get(key, 0) + c) % self.p
        if s:
            d[key] = s
        else:
            d.pop(key, None)

    def mul(self, A, B):
        out = {}
        for (a1, b1), c1 in A.items():
            for (a2, b2), c2 in B.items():
                self.add(out, (a1 + a2, b1 + b2), c1 * c2)
        return out

    def hasse(self, f, k, l):
        out = {}
        for (i, j, a, b), c in f.items():
            if i >= k and j >= l:
                self.add(out, (i - k, j - l, a, b), c * comb(i, k) * comb(j, l))
        return out

    def evaluate(self, f, phi, psi):
        D = max([i for (i, j, a, b) in f] + [0])
        E = max([j for (i, j, a, b) in f] + [0])
        PX = [{(0, 0): 1}]
        for _ in range(D):
            PX.append(self.mul(PX[-1], phi))
        PW = [{(0, 0): 1}]
        for _ in range(E):
            PW.append(self.mul(PW[-1], psi))
        cache = {}
        out = {}
        for (i, j, a, b), c in f.items():
            if (i, j) not in cache:
                cache[(i, j)] = self.mul(PX[i], PW[j])
            for (u, v), cc in cache[(i, j)].items():
                self.add(out, (u + a, v + b), c * cc)
        return out

    def subst_lin(self, f, phi, psi, Mm):
        """F_m = f(phi + Mm X, psi + Mm W) as dict {(k, l, a, b): c}"""
        out = {}
        D = max(i + j for (i, j, a, b) in f)
        for k in range(D + 1):
            for l in range(D + 1 - k):
                h = self.hasse(f, k, l)
                if not h:
                    continue
                hv = self.evaluate(h, phi, psi)
                sh = (Mm[0] * (k + l), Mm[1] * (k + l))
                for (a, b), c in hv.items():
                    self.add(out, (k, l, a + sh[0], b + sh[1]), c)
        return out


def lead(d):
    if not d:
        return None
    e = min(d, key=val)
    return e, d[e]


def vmin(d):
    return min(map(val, d)) if d else math.inf


def rand_f(Pp, rng, D, adversarial, c):
    p = Pp.p
    f = {}
    if adversarial:
        # (X - c W)^D + y0 z0 * (random of degree < D) + random constant term
        for s in range(D + 1):
            Pp.add(f, (s, D - s, 0, 0), comb(D, s) * pow(-c, D - s, p))
        for _ in range(4):
            i = rng.randint(0, D - 1); j = rng.randint(0, D - 1 - i)
            Pp.add(f, (i, j, 1 + rng.randint(0, 2), 1 + rng.randint(0, 2)), rng.randrange(1, p))
    else:
        for _ in range(rng.randint(3, 8)):
            i = rng.randint(0, D); j = rng.randint(0, D - i)
            Pp.add(f, (i, j, rng.randint(0, 3), rng.randint(0, 3)), rng.randrange(1, p))
        if max([i + j for (i, j, a, b) in f] + [0]) < D:
            Pp.add(f, (D, 0, rng.randint(0, 2), rng.randint(0, 2)), 1)
    return f


def translations(rng, p, levels, mode, c):
    T = []
    for j in range(levels):
        if mode == 'linear':
            b = rng.randrange(p)
            T.append(((c * b) % p, b))
        elif mode == 'sparse':
            b = rng.randrange(p)
            if rng.random() < 0.25 or j == levels - 1:
                a = (c * b + rng.randrange(1, p)) % p
            else:
                a = (c * b) % p
            T.append((a, b))
        else:
            T.append((rng.randrange(p), rng.randrange(p)))
    return T


def main():
    p, D, ntrials, levels = map(int, sys.argv[1:5])
    mode = sys.argv[5]
    seed = int(sys.argv[6])
    rng = random.Random(seed)
    Pp = P(p)
    Y, Z, M, charts = run_word(levels + 1)
    S = dict(trials=0, exact=0, failA=0, failB=0, failC=0, dom_checked=0, dom_fail=0, div_checked=0, div_fail=0, zero=0)
    last = 5
    for t in range(ntrials):
        c = rng.randrange(p)
        adv = rng.random() < 0.5
        f = rand_f(Pp, rng, D, adv, c)
        T = translations(rng, p, levels, 'sparse' if mode == 'sparse' else mode, c)
        phis, psis = [{}], [{}]
        for j in range(levels):
            ph, ps = dict(phis[-1]), dict(psis[-1])
            a, b = T[j]
            Pp.add(ph, M[j + 1], a); Pp.add(ps, M[j + 1], b)
            phis.append(ph); psis.append(ps)
        n = levels
        S['trials'] += 1
        # values at Phi_n, with exactness bounds for Phi_infinity
        Dt = max(i + j for (i, j, a, b) in f)
        der = {}
        for k in range(Dt + 1):
            for l in range(Dt + 1 - k):
                h = Pp.hasse(f, k, l)
                if h:
                    der[(k, l)] = (h, Pp.evaluate(h, phis[n], psis[n]))
        vMn1 = val(M[n + 1])

        def exact_val(k, l):
            # f^{[k,l]}(Phi_inf) - f^{[k,l]}(Phi_n) has value >= min over (k',l') > (k,l) of v(f^{[k',l']}(Phi_n)) + v(M_{n+1})
            h, hv = der[(k, l)]
            bound = math.inf
            for (k2, l2), (h2, hv2) in der.items():
                if (k2, l2) != (k, l) and k2 >= k and l2 >= l:
                    bound = min(bound, vmin(hv2) + vMn1)
            vv = vmin(hv)
            return (vv, lead(hv)) if vv < bound - 1e-9 else (None, None)

        vals = {}
        ok = True
        for kl in der:
            vv, ld = exact_val(*kl)
            if vv is None:
                ok = False
                break
            vals[kl] = (vv, ld)
        if not ok:
            if not der[(0, 0)][1]:
                S['zero'] += 1
            continue
        S['exact'] += 1
        lam = [min([vals[(k, s - k)][0] for k in range(s + 1) if (k, s - k) in vals] + [math.inf]) for s in range(Dt + 1)]
        V = lam[0]
        # (a)
        if Dt >= 1 and not V < lam[1] + 1 + TH:
            S['failA'] += 1
        # (c) chain
        for s in range(1, Dt + 1):
            if not lam[s - 1] < lam[s] + 1 + TH:
                S['failC'] += 1
                break
        # (b): leading term of f(Phi_m) for the last levels equals that of f(Phi_inf)
        L_inf = vals[(0, 0)][1]
        for m in range(n - last, n + 1):
            if lead(Pp.evaluate(f, phis[m], psis[m])) != L_inf:
                S['failB'] += 1
                break
        # Proposition 4.1 and the divisibility of Theorem 5.1, at the last levels, for f and for f_X, f_W
        nus = {}
        for name, ff in (('f', f), ('fX', Pp.hasse(f, 1, 0)), ('fW', Pp.hasse(f, 0, 1))):
            if not ff:
                continue
            Lff = lead(Pp.evaluate(ff, phis[n], psis[n]))
            S['dom_checked'] += 1
            fail = False
            for m in range(n - last + 1, n + 1):
                Fm = Pp.subst_lin(ff, phis[m], psis[m], M[m])
                nu = Lff[0]
                if (0, 0, nu[0], nu[1]) not in Fm or Fm[(0, 0, nu[0], nu[1])] != Lff[1]:
                    fail = True; break
                s0, t0 = to_level(nu, Y[m], Z[m])
                if s0 < 0 or t0 < 0:
                    fail = True; break
                for (k, l, a, b), cc in Fm.items():
                    if (k, l, a, b) == (0, 0, nu[0], nu[1]):
                        continue
                    # monomial a,b of y0 z0 times X^k W^l; X = x_m (already includes M_m)
                    s, tt = to_level((a, b), Y[m], Z[m])
                    if not (s > s0 and tt > t0):
                        fail = True; break
                if fail:
                    break
            if fail:
                S['dom_fail'] += 1
            nus[name] = Lff[0]
        if 'fX' in nus and 'fW' in nus:
            S['div_checked'] += 1
            m = n
            a = to_level(nus['fX'], Y[m], Z[m]); b = to_level(nus['fW'], Y[m], Z[m])
            if not ((a[0] <= b[0] and a[1] <= b[1]) or (b[0] <= a[0] and b[1] <= a[1])):
                S['div_fail'] += 1
    print('p', p, 'D', D, 'levels', levels, 'mode', mode, S, flush=True)


if __name__ == '__main__':
    main()
