import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os
# Rule-driven and random walks for note 51.
# usage: python3 run51.py MODE FAMILY p walks depth seed [args]
#   MODE rule : centre = largest coordinate subspace of the locus where iota = (class, omega) is maximal
#   MODE rand : random permissible coordinate centre in the adapted coordinate
#   FAMILY t44 N M | ex45 | ex46 | f1 | gen | pow
import sys, random
from lib51 import *

def iota0(f, a):
    """literal (b''): sigma* in R2, R3; slope of (P, q) in R1 (bottom layer and a_q)"""
    r, D, s = regime(f, a)
    if r in (2, 3):
        return s
    return min(Fr(order(a[i]), i) if a[i] else INF for i in range(1, f.q + 1))

def start(fam, p, m, rng, args):
    a = [ONE] + [{} for _ in range(m)]
    if fam == "t44":
        N, M = args
        a[1] = {(N, 0, 0): 1}; a[m] = {(M, 0, 0): 1}
    elif fam == "ex45":
        a[1] = {(3, 0, 0): 1}; a[m] = {(0, 4 * p + 1, 0): 1}
    elif fam == "ex46":
        a[1] = {(1, 0, 0): 1}; a[m] = {(0, 2 * p + 1, 0): 1}
    elif fam == "f1":
        a[1] = {(0, 2, 0): 1}; a[m] = {(5 * p, 0, 0): 1}
    elif fam == "gen":
        while True:
            S0 = rng.choice([(0, 1, 2), (0, 1), (0, 1), (0,), (0,)])
            a = [ONE]
            for i in range(1, m + 1):
                if rng.random() < 0.45:
                    a.append({}); continue
                a.append(rand_supp(S0, i + rng.choice([0, 0, 1, 2, 3]) * (1 if i in (1,) else 1), rng.choice([0, 1, 2]), 0.12, p, rng))
            if rng.random() < 0.5:
                c = rand_supp((0, 1, 2), rng.choice([1, 2]), 0, 0.5, p, rng)
                a = translate(a, c, p)
            if is_mult_m(a) and any(a[i] for i in range(1, m + 1) if i % p):
                break
    elif fam == "pow":
        # (z^p + b)^2 + rigid perturbation: rich in R1 and R3
        while True:
            S0 = rng.choice([(0, 1, 2), (0, 1), (0,)])
            b = rand_supp(S0, p * rng.choice([1, 2]), rng.choice([0, 1, 2]), 0.2, p, rng)
            a = [ONE] + [{} for _ in range(m)]
            a[p] = scal(b, 2, p); a[m] = mul(b, b, p)
            for i in range(1, m):
                if i % p and rng.random() < 0.3:
                    a[i] = rand_supp(S0, i * rng.choice([1, 2, 3]) // 1, rng.choice([0, 1]), 0.12, p, rng)
            if rng.random() < 0.5:
                a = translate(a, rand_supp((0, 1, 2), rng.choice([1, 2]), 0, 0.5, p, rng), p)
            if is_mult_m(a) and any(a[i] for i in range(1, m) if i % p):
                break
    return a

def main():
    mode, fam = sys.argv[1], sys.argv[2]
    p, walks, depth, seed = map(int, sys.argv[3:7])
    args = list(map(int, sys.argv[7:]))
    m = 2 * p
    rng = random.Random(seed)
    MAXT = int(4000 if p < 7 else 2500)
    st = dict(walks=0, steps=0, points=0, nu_nonzero=0, nu_nonzero_bad=0, omega_fixed_up=0,
              prep=0, dirch=0, iota_up=0, iota_eq=0, iota_down=0, omega_up=0, class_up=0,
              iota0_up=0, ties=0, drops=0, cut=0, maxlen=0, reg={1: 0, 2: 0, 3: 0},
              trans={}, centres={1: 0, 2: 0, 3: 0}, eqrun=0, eq_pos=0, mono_steps=0, unterminated=0)
    bad = []
    for wk in range(walks):
        a = start(fam, p, m, rng, args)
        f = F(a, set(), p)
        E = set()
        a, _ = adapt(f, a)
        run = 0
        for step in range(depth):
            io, r = iota(f, a, E)
            i0 = iota0(f, a)
            if mode == "rule":
                S, ties = rule_centre(f, a, E)
                st["ties"] += 1 if ties else 0
            else:
                cands = [S for S in SUBSETS if permissible(f, a, S)]
                S = rng.choice(cands)
            st["centres"][len(S)] += 1
            st["steps"] += 1
            pts = points_over(f, a, E, S)
            if not pts:
                st["drops"] += 1
                break
            om = io[1]
            if om == 0:
                st["mono_steps"] += 1
            # the fixed-coordinate value of omega at the new points (Proposition: <= om for rule centres)
            nexts = []
            for j, lams, nu, d, E2 in pts:
                st["points"] += 1
                if nu:
                    st["nu_nonzero"] += 1
                    st["nu_nonzero_bad"] += 1
                    bad.append(("nu", wk, step, S, j, lams, nu))
                wz = omega(f, d, E2)
                if mode == "rule" and wz > om:
                    st["omega_fixed_up"] += 1
                    bad.append(("omega_fixed", wk, step, S, j, lams, str(om), str(wz)))
                d2, (k, dch) = adapt(f, d)
                st["prep"] += 1 if k else 0
                st["dirch"] += 1 if dch else 0
                io2, r2 = iota(f, d2, E2)
                st["reg"][r2] += 1
                st["trans"][(r, r2)] = st["trans"].get((r, r2), 0) + 1
                if io2 > io:
                    st["iota_up"] += 1
                    if io2[0] > io[0]:
                        st["class_up"] += 1
                    bad.append(("iota_up", wk, step, S, j, lams, str(io), str(io2), k, dch))
                    if os.environ.get("DUMP"):
                        print("DUMP regimes", r, r2, str(io), str(io2), "D,s before", [str(x) for x in slopes(f, a)], "after", [str(x) for x in slopes(f, d2)], "unadapted", [str(x) for x in slopes(f, d)]); print("DUMP before", sorted(E), [sorted(x.items()) for x in a[1:]])
                        print("DUMP child-unadapted", sorted(E2), [sorted(x.items()) for x in d[1:]])
                        print("DUMP child-adapted", [sorted(x.items()) for x in d2[1:]])
                elif io2 == io:
                    st["iota_eq"] += 1
                    if io[1] > 0:
                        st["eq_pos"] += 1
                else:
                    st["iota_down"] += 1
                if io2[1] > io[1] and io2[0] == io[0]:
                    st["omega_up"] += 1
                if iota0(f, d2) > i0:
                    st["iota0_up"] += 1
                nexts.append((d2, E2, io2))
            d2, E2, io2 = rng.choice(nexts)
            run = run + 1 if io2 == io else 0
            st["eqrun"] = max(st["eqrun"], run)
            if os.environ.get("DUMPRUN") and run == int(os.environ["DUMPRUN"]):
                print("RUN", wk, step, r, str(io), S, sorted(E2), [sorted(x.items()) for x in d2[1:]])
            a, E = d2, E2
            if size(a) > MAXT:
                st["cut"] += 1
                break
        else:
            st["unterminated"] += 1
        st["walks"] += 1
    st["trans"] = {"%d>%d" % k: v for k, v in sorted(st["trans"].items())}
    print(mode, fam, p, args, st, flush=True)
    for b in bad[:12]:
        print("  BAD", b)

if __name__ == '__main__':
    main()
