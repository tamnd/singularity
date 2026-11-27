import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# F2: z^{2p} + x0 x1 z^{2p-1} + x0^{2p-1} x1^{2p}, E = {x0, x1}; one step of the rule with MONO=0 and MONO=1
import lib51
from lib51 import *
for p in (3, 5, 7):
    m = 2 * p
    a = [ONE] + [{} for _ in range(m)]
    a[1] = {(1, 1, 0): 1}; a[m] = {(m - 1, m, 0): 1}
    f = F(a, set(), p); E = {0, 1}
    for mono in (False, True):
        lib51.MONO = mono
        S, t = rule_centre(f, a, E)
        pts = points_over(f, a, E, S)
        print("p=%d MONO=%s iota=%s centre S=%s" % (p, mono, iota(f, a, E), S),
              ["chart%d lam%s a1=%s a%d=%s same=%s" % (j, l, d[1], m, d[m], d == a) for j, l, nu, d, E2 in pts] or "drop")

# F3: z^{2p} + x0^2 x1 z^{2p-2} + x0^{2p} x1, E = {x1}; the max locus of iota is the curve V(z,x0,x1)
print("F3")
for p in (3, 5, 7):
    m = 2 * p
    a = [ONE] + [{} for _ in range(m)]
    a[2] = {(2, 1, 0): 1}; a[m] = {(m, 1, 0): 1}
    f = F(a, set(), p); E = {1}
    for div in (False, True):
        lib51.DIV = div
        S, t = rule_centre(f, a, E)
        pts = points_over(f, a, E, S)
        print("p=%d DIV=%s iota=%s regime=%s centre S=%s" % (p, div, iota(f, a, E)[0], iota(f, a, E)[1], S),
              ["chart%d lam%s E'=%s same=%s" % (j, l, sorted(E2), d == a and E2 == E) for j, l, nu, d, E2 in pts] or "drop")

# F4: z^{2p} + x0^2 x2 z^{2p-2} + x1^{2p+1}, E = {}: follow the chart x2 origin under the rule (DIV on)
print("F4")
lib51.DIV = True
for cls in ("plain", "res"):
    lib51.CLS = cls
    for p in (3, 5, 7):
        m = 2 * p
        a = [ONE] + [{} for _ in range(m)]
        a[2] = {(2, 0, 1): 1}; a[m] = {(0, 2 * p + 1, 0): 1}
        f = F(a, set(), p); E = set()
        hist = []
        for step in range(12):
            io, r = iota(f, a, E)
            S, t = rule_centre(f, a, E)
            pts = points_over(f, a, E, S)
            hist.append("R%d%s S=%s" % (r, (io[0], str(io[1])), S))
            nxt = [(d, E2) for j, l, nu, d, E2 in pts if j == 2 and all(x == 0 for x in l)]
            if not pts:
                hist.append("drop"); break
            if not nxt:
                hist.append("other points only: %d" % len(pts)); break
            a, E = nxt[0]
        print(cls, "p=%d" % p, " | ".join(hist), "| a2 =", a[2] if a[2] else None)
