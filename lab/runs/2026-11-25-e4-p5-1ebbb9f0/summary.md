# e4-p5

On the walks of e1-p5 with q = p = 5, do the Cossart-Piltant invariants omega and iota = (m, omega, kappa) go up under a point blowup, and does a jump of epsilon meet the condition of Theorem 3.13(1) of Cossart-Piltant, for n = 3 (dimension 3) and n = 4 (dimension 4)?

- Experiment: E4. Node: SG00000014.
- Tool: sing-lab, in sing dev, commit a9f346e548a0.
- Spec: `e4-p5.yaml`, sha256 1ebbb9f0ef18.
- Walks: the walks of `e1-p5.yaml`, sha256 54c44a97c686. The run makes the same walks again from the same seed.
- Cases: only the cases of that spec with n = 3 and q = 5, or n = 4 and q = 5.
- Seed: 20261124005.
- The host and the wall time are in `record.json`.

The run tests 4 invariants of Cossart and Piltant [CP19] on 668209 steps of 144000 walks in 2 cases, with q = p. A candidate fails at a step when its value after the blowup is larger than its value before, or, for a bound, when the step breaks the bound.

## The invariants

The equation is h = Z^p + F with F clean, so the coordinates are well adapted [CP19, Definition 2.24]. E is the divisor, F = prod_{j in E} x_j^(r_j) G, and in(F) is the initial form of F. The engine computes these invariants at each point of a walk.

- m(x) = p, the multiplicity. A walk keeps the order p, so m = p at each point.
- delta(x) = ord F / p [CP19, Definition 2.11].
- epsilon(x) = ord F - sum r_j = ord G, the residual order d [CP19, Definition 2.25].
- omega(x) = epsilon(x) - 1 if dF/dU_j != 0 for some x_j not in E, with F = in(F), and omega(x) = epsilon(x) otherwise [CP19, (1.11) and Definition 2.68].
- kappa(x) = 1 if omega(x) = 0, and kappa(x) >= 2 otherwise [CP19, Definition 2.68]. The engine does not split the values >= 2.

## The candidates

- `cp-omega`: omega of Cossart-Piltant [CP19, (1.11) and Definition 2.68]: omega = epsilon - 1 if dF/dU_j != 0 for some x_j not in E, with F the initial form of the clean F, and omega = epsilon otherwise. Here epsilon = d is the residual order. The candidate fails when omega goes up, at any step.
- `cp-iota`: iota = (m, omega, kappa) of Cossart-Piltant [CP19, (2.76) and Definition 2.68] in the lexicographic order, with kappa = 1 if omega = 0 and kappa >= 2 otherwise. On a walk m = p, so iota goes up exactly when omega goes up. [CP19, Theorem 3.13] says that iota does not go up under a permissible blowup when m(x) = p and omega(x) > 0, and a point is a permissible centre. The scope is the steps from a point with omega(x) > 0, the hypothesis of [CP19, Theorem 3.13].
- `cp-eps-jump`: the condition of [CP19, Theorem 3.13(1)] for a point centre: if epsilon goes up at a step from a point with omega(x) > 0, then omega(x) = epsilon(x) and delta(x) = ord F / p is an integer. The candidate fails at a step where epsilon goes up and one of the two conditions does not hold. The scope is the steps from a point with omega(x) > 0, the hypothesis of [CP19, Theorem 3.13].
- `d-over-q`: d/q, the residual order divided by q. Along one walk q does not change, so this candidate fails exactly at the kangaroo points.

## Results

| candidate | steps in the scope | steps out of the scope | failures | the first failure |
|---|---|---|---|---|
| `cp-omega` | 668209 | 0 | 0 | none |
| `cp-iota` | 643116 | 25093 | 0 | none |
| `cp-eps-jump` | 643116 | 25093 | 0 | none |
| `d-over-q` | 668209 | 0 | 21 | p = 5, n = 3, q = 5, walk 3774, step 1: 3/5 to 4/5 |

## Dimension 3 and dimension 4

The case n = 3 is a threefold z^p + g(x1, x2, x3), the case of the theorem of Cossart and Piltant. The case n = 4 is its analogue in dimension 4. For each candidate that is a value, the table gives the steps in the scope where the value goes up, stays the same and goes down, and the share of the steps where it goes down.

`cp-omega`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 5 | 3 | 5 | 554376 | 0 | 0 | 402889 | 151487 | 27.3% |
| 5 | 4 | 5 | 113833 | 0 | 0 | 85278 | 28555 | 25.1% |

`cp-iota`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 5 | 3 | 5 | 531702 | 22674 | 0 | 380215 | 151487 | 28.5% |
| 5 | 4 | 5 | 111414 | 2419 | 0 | 82859 | 28555 | 25.6% |

`d-over-q`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 5 | 3 | 5 | 554376 | 0 | 18 | 394488 | 159870 | 28.8% |
| 5 | 4 | 5 | 113833 | 0 | 3 | 83895 | 29935 | 26.3% |

The change of epsilon, the residual order, in each case (each entry is a change and the number of steps):

| p | n | q | walks | steps | kangaroo points | changes |
|---|---|---|---|---|---|---|
| 5 | 3 | 5 | 122000 | 554376 | 18 | -14: 1, -13: 43, -12: 164, -11: 492, -10: 833, -9: 1469, -8: 2826, -7: 3970, -6: 7275, -5: 10046, -4: 16569, -3: 22209, -2: 38580, -1: 55393, 0: 394488, +1: 18 |
| 5 | 4 | 5 | 22000 | 113833 | 3 | -14: 1, -13: 9, -12: 22, -11: 113, -10: 201, -9: 309, -8: 579, -7: 857, -6: 1393, -5: 1907, -4: 3159, -3: 4066, -2: 7619, -1: 9700, 0: 83895, +1: 3 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, and the invariants before and after the step (the field `cp`), so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. They are the counts of the same cases in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of the cases n = 3 and n = 4 with q = p of e1-p5 again from the same seed. At each step it computes the invariants of Cossart and Piltant (arXiv:1412.0868, key CP19) for f = z^p + F with F clean. The multiplicity m is p on each step. ord F is p times delta (Def. 2.11). epsilon is ord F minus the sum of the divisor exponents (Def. 2.25), which is the residual order d. omega is epsilon - 1 when a term of the initial form of F has an exponent prime to p in a variable outside the divisor, and epsilon otherwise (Def. 2.68 with (2.44)). kappa is 1 when omega = 0 and at least 2 otherwise (Def. 2.68). The engine does not compute kappa in 2, 3, 4 (Def. 5.1) or the projection invariants. cp-omega fails when omega goes up, at each step. cp-iota fails when (m, omega, kappa) goes up in the lexicographic order. cp-eps-jump fails when epsilon goes up and epsilon(x) = omega(x) with delta(x) an integer does not hold. Both count only steps with omega(x) > 0, the scope of Theorem 3.13. d-over-q is the candidate of E2, for comparison. The engine does not check condition (E) of the paper (Def. 2.32), and it uses point centres and points over F_p only.

## What the data does not show

- This is data from examples. It does not prove a statement.
- The walks use only point centres, and only the points over F_p of the exceptional divisor, in the n charts. [CP19, Theorem 3.13] is about all points over x and all permissible centres, also curves and surfaces.
- The engine does not check condition (E) of [CP19, Definition 2.32]: that the points of multiplicity p of the hypersurface lie over E. Theorem 3.13 assumes it. A failure of cp-iota or cp-eps-jump at a point where (E) fails is not a counterexample to the theorem.
- The values of omega and epsilon do not depend on the well adapted coordinates [CP19, Remark 2.69, and the handbook, Volume 6, Proposition 3.2.4(5)]. So, unlike the bound of Moh in E1, a failure is not only a matter of coordinates. Each failure must be checked by hand, with condition (E), before it counts for anything.
- The engine computes kappa only as 1 or >= 2. The values 2, 3 and 4 of kappa for n = 3 [CP19, Definition 5.1] and the invariants of the projection need a well chosen coordinate, which the engine cannot choose. So the run does not test the decrease of the Projection Theorem [CP19, Theorem 5.5].
- A candidate with no failure on these walks is not proved to go down or to stay. The walks are a small sample, and a walk stops at a depth or a cap.
