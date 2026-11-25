# e4-p2

On the walks of e1-p2 with q = p = 2, do the Cossart-Piltant invariants omega and iota = (m, omega, kappa) go up under a point blowup, and does a jump of epsilon meet the condition of Theorem 3.13(1) of Cossart-Piltant, for n = 3 (dimension 3) and n = 4 (dimension 4)?

- Experiment: E4. Node: SG00000014.
- Tool: sing-lab, in sing dev, commit a9f346e548a0.
- Spec: `e4-p2.yaml`, sha256 b049ce95142e.
- Walks: the walks of `e1-p2.yaml`, sha256 90966cbf6b0c. The run makes the same walks again from the same seed.
- Cases: only the cases of that spec with n = 3 and q = 2, or n = 4 and q = 2.
- Seed: 20261124002.
- The host and the wall time are in `record.json`.

The run tests 4 invariants of Cossart and Piltant [CP19] on 2625908 steps of 547000 walks in 2 cases, with q = p. A candidate fails at a step when its value after the blowup is larger than its value before, or, for a bound, when the step breaks the bound.

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
| `cp-omega` | 2625908 | 0 | 0 | none |
| `cp-iota` | 1355563 | 1270345 | 0 | none |
| `cp-eps-jump` | 1355563 | 1270345 | 0 | none |
| `d-over-q` | 2625908 | 0 | 4988 | p = 2, n = 3, q = 2, walk 76, step 0: 2/2 to 3/2 |

## Dimension 3 and dimension 4

The case n = 3 is a threefold z^p + g(x1, x2, x3), the case of the theorem of Cossart and Piltant. The case n = 4 is its analogue in dimension 4. For each candidate that is a value, the table gives the steps in the scope where the value goes up, stays the same and goes down, and the share of the steps where it goes down.

`cp-omega`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 2 | 2360914 | 0 | 0 | 1820873 | 540041 | 22.9% |
| 2 | 4 | 2 | 264994 | 0 | 0 | 191301 | 73693 | 27.8% |

`cp-iota`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 2 | 1188490 | 1172424 | 0 | 648449 | 540041 | 45.4% |
| 2 | 4 | 2 | 167073 | 97921 | 0 | 93380 | 73693 | 44.1% |

`d-over-q`:

| p | n | q | steps in the scope | out of the scope | up | same | down | share down |
|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 2 | 2360914 | 0 | 4516 | 1834700 | 521698 | 22.1% |
| 2 | 4 | 2 | 264994 | 0 | 472 | 192466 | 72056 | 27.2% |

The change of epsilon, the residual order, in each case (each entry is a change and the number of steps):

| p | n | q | walks | steps | kangaroo points | changes |
|---|---|---|---|---|---|---|
| 2 | 3 | 2 | 489000 | 2360914 | 4516 | -5: 3687, -4: 9886, -3: 34506, -2: 169248, -1: 304371, 0: 1834700, +1: 4516 |
| 2 | 4 | 2 | 58000 | 264994 | 472 | -5: 515, -4: 1232, -3: 5886, -2: 24330, -1: 40093, 0: 192466, +1: 472 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, and the invariants before and after the step (the field `cp`), so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. They are the counts of the same cases in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of the cases n = 3 and n = 4 with q = p of e1-p2 again from the same seed. At each step it computes the invariants of Cossart and Piltant (arXiv:1412.0868, key CP19) for f = z^p + F with F clean. The multiplicity m is p on each step. ord F is p times delta (Def. 2.11). epsilon is ord F minus the sum of the divisor exponents (Def. 2.25), which is the residual order d. omega is epsilon - 1 when a term of the initial form of F has an exponent prime to p in a variable outside the divisor, and epsilon otherwise (Def. 2.68 with (2.44)). kappa is 1 when omega = 0 and at least 2 otherwise (Def. 2.68). The engine does not compute kappa in 2, 3, 4 (Def. 5.1) or the projection invariants. cp-omega fails when omega goes up, at each step. cp-iota fails when (m, omega, kappa) goes up in the lexicographic order. cp-eps-jump fails when epsilon goes up and epsilon(x) = omega(x) with delta(x) an integer does not hold. Both count only steps with omega(x) > 0, the scope of Theorem 3.13. d-over-q is the candidate of E2, for comparison. The engine does not check condition (E) of the paper (Def. 2.32), and it uses point centres and points over F_p only.

## What the data does not show

- This is data from examples. It does not prove a statement.
- The walks use only point centres, and only the points over F_p of the exceptional divisor, in the n charts. [CP19, Theorem 3.13] is about all points over x and all permissible centres, also curves and surfaces.
- The engine does not check condition (E) of [CP19, Definition 2.32]: that the points of multiplicity p of the hypersurface lie over E. Theorem 3.13 assumes it. A failure of cp-iota or cp-eps-jump at a point where (E) fails is not a counterexample to the theorem.
- The values of omega and epsilon do not depend on the well adapted coordinates [CP19, Remark 2.69, and the handbook, Volume 6, Proposition 3.2.4(5)]. So, unlike the bound of Moh in E1, a failure is not only a matter of coordinates. Each failure must be checked by hand, with condition (E), before it counts for anything.
- The engine computes kappa only as 1 or >= 2. The values 2, 3 and 4 of kappa for n = 3 [CP19, Definition 5.1] and the invariants of the projection need a well chosen coordinate, which the engine cannot choose. So the run does not test the decrease of the Projection Theorem [CP19, Theorem 5.5].
- A candidate with no failure on these walks is not proved to go down or to stay. The walks are a small sample, and a walk stops at a depth or a cap.
