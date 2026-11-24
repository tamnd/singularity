# e1-p3

How does the residual order of z^q + F over F_3 change under random point blowups that keep the order q, for q = 3 and q = 9 and n = 2, 3, 4 variables? How many steps go up by more than the bound p^(e-1) of Moh, and what are the kangaroo points?

- Experiment: E1. Node: SG00000016.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e1-p3.yaml`, sha256 08768f1a6cba.
- Seed: 20261124003.
- The host and the wall time are in `record.json`.

The run did 4221000 random walks with 12480541 point blowups in 6 cases. At each step the order of f stays q.

## Results

A kangaroo point is a step at which the residual order goes up. The bound of Moh for one step is p^(e-1). The stability bound is d0 + p^(e-1), with d0 the residual order at the start of the walk.

| p | n | q | walks | steps | kangaroo points | largest increase | p^(e-1) | steps over p^(e-1) | walks over d0 + p^(e-1) |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 1000000 | 1320396 | 1804 | 1 | 1 | 0 | 0 |
| 3 | 3 | 3 | 1000000 | 4716878 | 1541 | 1 | 1 | 0 | 0 |
| 3 | 4 | 3 | 267000 | 1322391 | 354 | 1 | 1 | 0 | 0 |
| 3 | 2 | 9 | 1000000 | 1204267 | 1104 | 3 | 3 | 0 | 0 |
| 3 | 3 | 9 | 800000 | 3156967 | 449 | 3 | 3 | 0 | 0 |
| 3 | 4 | 9 | 154000 | 759642 | 57 | 3 | 3 | 0 | 0 |

## The change of the residual order

Each entry is a change d' - d and the number of steps with that change.

| p | n | q | changes |
|---|---|---|---|
| 3 | 2 | 3 | -8: 433, -7: 4314, -6: 10286, -5: 16080, -4: 51208, -3: 99491, -2: 218512, -1: 468744, 0: 449524, +1: 1804 |
| 3 | 3 | 3 | -8: 742, -7: 6162, -6: 13108, -5: 30370, -4: 94031, -3: 163299, -2: 354586, -1: 628755, 0: 3424284, +1: 1541 |
| 3 | 4 | 3 | -8: 278, -7: 1984, -6: 3893, -5: 10860, -4: 29902, -3: 47564, -2: 109520, -1: 163101, 0: 954935, +1: 354 |
| 3 | 2 | 9 | -25: 13, -24: 41, -23: 131, -22: 300, -21: 554, -20: 976, -19: 1681, -18: 2380, -17: 3097, -16: 4431, -15: 5594, -14: 7238, -13: 9140, -12: 12394, -11: 15503, -10: 21315, -9: 26398, -8: 33124, -7: 41484, -6: 52801, -5: 64500, -4: 83573, -3: 107970, -2: 126000, -1: 186146, 0: 396379, +1: 627, +2: 457, +3: 20 |
| 3 | 3 | 9 | -26: 1, -25: 11, -24: 35, -23: 83, -22: 200, -21: 407, -20: 796, -19: 1426, -18: 2180, -17: 3088, -16: 4467, -15: 5959, -14: 7985, -13: 10496, -12: 14257, -11: 18676, -10: 25416, -9: 32611, -8: 42955, -7: 51989, -6: 67144, -5: 81111, -4: 112413, -3: 139267, -2: 181907, -1: 245246, 0: 2106392, +1: 277, +2: 146, +3: 26 |
| 3 | 4 | 9 | -25: 2, -24: 2, -23: 13, -22: 33, -21: 68, -20: 139, -19: 233, -18: 421, -17: 598, -16: 878, -15: 1245, -14: 1642, -13: 2192, -12: 2967, -11: 3793, -10: 5024, -9: 6400, -8: 8557, -7: 10278, -6: 13515, -5: 16351, -4: 23336, -3: 29317, -2: 40747, -1: 50394, 0: 541440, +1: 36, +2: 16, +3: 5 |

## How the walks stop

| p | n | q | depth | the order drops at each point | residual order 0 | cap |
|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 3023 | 302902 | 693811 | 264 |
| 3 | 3 | 3 | 258993 | 100873 | 607393 | 32741 |
| 3 | 4 | 3 | 36475 | 2577 | 134403 | 93545 |
| 3 | 2 | 9 | 2047 | 510041 | 487894 | 18 |
| 3 | 3 | 9 | 104855 | 245984 | 353765 | 95396 |
| 3 | 4 | 9 | 22764 | 17905 | 46117 | 67214 |

## The files

- `histogram.json`: the counts of each case.
- `examples.json`: the first examples of each increase in each case, and the first walks over the stability bound. Each example has the polynomial, the divisor, the chart and the translations, so you can check it again with `sing lab step`.

## Notes

The family random-sparse draws F as a sum of 2 to 6 terms with coefficients in 1..p-1. Each term has a total degree in the range of the case, and its exponent vector is uniform among those of that degree. The engine cleans F and draws again when F is zero or ord F < q. The divisor is all the variables x1..xn. At each step the walk takes a point at random among the points over F_p of the exceptional divisor where the order of f stays q, in the n charts. A walk stops after 12 blowups, when no such point exists, when the residual order is 0, or at a cap. The caps are 400 terms, 200000 terms in one expansion and the total degree 400. The number of walks of each case makes a run of about 20 to 40 minutes on 4 threads of a project machine.

## What the data does not show

- The lab computes the residual order in the given coordinates x1, ..., xn, after it removes the q-th powers from F (the cleaning of z). The bound of Moh is about well chosen coordinates. So a step over the bound in this data is not a counterexample to the theorem of Moh. It is an example to check in other coordinates.
- The walks use only the points over F_p of the exceptional divisor, in the n charts. The same point can be in more than one chart.
- A walk stops at a cap of the spec. So the data has fewer large polynomials than the family.
- This is data from examples. It does not prove a statement.
