"""Distance computations for Artin-Schreier extensions (Problem V6 test cases)."""
import math, sys
from fractions import Fraction as Fr
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hahn import Ring

def example_A(p, M=6):
    """theta = sum_{i=1..M} t^(-1/p^i); theta^p - theta - 1/t = -t^(-1/p^M)."""
    R = Ring(p, (1.0,), 10.0)
    th = R.clean({(Fr(-1, p**i),): 1 for i in range(1, M + 1)})
    resid = R.sub(R.sub(R.power(th, p), th), R.mono((-1,)))
    print(f"Example A, p={p}: theta^p-theta-1/t = {resid}")
    for k in range(M):
        thk = R.clean({(Fr(-1, p**i),): 1 for i in range(1, k + 1)})
        d = R.val(R.sub(th, thk))
        print(f"   v(theta - theta_{k}) = {d:.6f}  (= -1/p^{k+1} = {-1/p**(k+1):.6f})")
    print("   sup = 0-, the idempotent cut: independent defect")

def p_root(R, s):
    p = R.p
    return R.clean({tuple(a / p for a in e): c for e, c in s.items()})

def example_C_rank_one(p, it=8):
    """Rank-one replacement of Example C: v(t)=1, v(z)=sqrt 2, s = sum t^(n!).
    Root of X^p - z^(p-1) X - s^p via X = s + (z^(p-1) X)^(1/p)."""
    R = Ring(p, (1.0, math.sqrt(2)), 12.0)
    s = R.clean({(Fr(n), Fr(0)): 1 for n in (1, 2, 6, 24)})
    zp1 = R.mono((0, p - 1))
    X = dict(s)
    for _ in range(it):
        X = R.add(s, p_root(R, R.mul(zp1, X)))
    res = R.sub(R.sub(R.power(X, p), R.mul(zp1, X)), R.power(s, p))
    e, c = R.lead(R.sub(X, s))
    print(f"Example C, rank-one replacement, p={p}: residual value >= {R.val(res):.3f}")
    print(f"   leading exponent of theta0 - s in (t,z)-coordinates: {tuple(str(a) for a in e)}, value {R.val_mono(e):.4f}")
    print(f"   exponent not in Z^2, so the value group grows by index p: e = p, no defect")

def eg_bound(p):
    """ElHitti-Ghezzi: nu1(1/x - f) < (1/p)(Omega) - 2/p with Omega = sum_j p^(-4j)."""
    Om = Fr(p**4, p**4 - 1)
    b = Om / p - Fr(2, p)
    print(f"EG example, p={p}: Omega={Om}, distance <= {b} = {float(b):.5f} < -1/p^2 = {-1/p**2:.5f} < 0: dependent")
    vals = [sum(Fr(p)**(4*j - 2*i) for j in range(i)) for i in range(1, 6)]
    print(f"   nu(P_i), i=1..5: {[str(v) for v in vals]}")

if __name__ == '__main__':
    for p in (2, 3):
        example_A(p)
    for p in (2, 3):
        example_C_rank_one(p)
    for p in (2, 3, 5):
        eg_bound(p)
