# e1-p2

How does the residual order of z^q + F over F_2 change under random point blowups that keep the order q, for q = 2 and q = 4 and q = 8 and n = 2, 3, 4 variables? How many steps go up by more than the bound p^(e-1) of Moh, and what are the kangaroo points?

- Experiment: E1. Node: SG00000016.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e1-p2.yaml`, sha256 90966cbf6b0c.
- Seed: 20261124002.
- The host and the wall time are in `record.json`.

The run did 2454000 random walks with 7051981 point blowups in 9 cases. At each step the order of f stays q.

## Results

A kangaroo point is a step at which the residual order goes up. The bound of Moh for one step is p^(e-1). The stability bound is d0 + p^(e-1), with d0 the residual order at the start of the walk.

| p | n | q | walks | steps | kangaroo points | largest increase | p^(e-1) | steps over p^(e-1) | walks over d0 + p^(e-1) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 2 | 500000 | 580121 | 6770 | 1 | 1 | 0 | 0 |
| 2 | 3 | 2 | 489000 | 2360914 | 4516 | 1 | 1 | 0 | 0 |
| 2 | 4 | 2 | 58000 | 264994 | 472 | 1 | 1 | 0 | 0 |
| 2 | 2 | 4 | 272000 | 361101 | 1021 | 2 | 2 | 0 | 0 |
| 2 | 3 | 4 | 84000 | 378763 | 348 | 2 | 2 | 0 | 0 |
| 2 | 4 | 4 | 111000 | 623688 | 419 | 2 | 2 | 0 | 0 |
| 2 | 2 | 8 | 500000 | 621449 | 979 | 4 | 4 | 0 | 0 |
| 2 | 3 | 8 | 349000 | 1386934 | 577 | 4 | 4 | 0 | 0 |
| 2 | 4 | 8 | 91000 | 474017 | 109 | 4 | 4 | 0 | 0 |

## The change of the residual order

Each entry is a change d' - d and the number of steps with that change.

| p | n | q | changes |
|---|---|---|---|
| 2 | 2 | 2 | -5: 2681, -4: 9198, -3: 17102, -2: 104361, -1: 206345, 0: 233664, +1: 6770 |
| 2 | 3 | 2 | -5: 3687, -4: 9886, -3: 34506, -2: 169248, -1: 304371, 0: 1834700, +1: 4516 |
| 2 | 4 | 2 | -5: 515, -4: 1232, -3: 5886, -2: 24330, -1: 40093, 0: 192466, +1: 472 |
| 2 | 2 | 4 | -11: 25, -10: 218, -9: 839, -8: 1908, -7: 2668, -6: 5819, -5: 9390, -4: 21844, -3: 31089, -2: 60276, -1: 99879, 0: 126125, +1: 937, +2: 84 |
| 2 | 3 | 4 | -11: 7, -10: 79, -9: 283, -8: 655, -7: 1258, -6: 2940, -5: 5049, -4: 11098, -3: 15755, -2: 31591, -1: 45350, 0: 264350, +1: 306, +2: 42 |
| 2 | 4 | 4 | -11: 19, -10: 109, -9: 394, -8: 859, -7: 1992, -6: 4454, -5: 7670, -4: 16389, -3: 23219, -2: 46024, -1: 61682, 0: 460458, +1: 357, +2: 62 |
| 2 | 2 | 8 | -23: 1, -22: 10, -21: 53, -20: 126, -19: 224, -18: 470, -17: 840, -16: 1372, -15: 1702, -14: 2518, -13: 3319, -12: 4801, -11: 5887, -10: 8425, -9: 10950, -8: 16092, -7: 19101, -6: 25513, -5: 32356, -4: 44921, -3: 53723, -2: 76971, -1: 101526, 0: 209569, +1: 652, +2: 169, +3: 144, +4: 14 |
| 2 | 3 | 8 | -23: 2, -22: 9, -21: 36, -20: 65, -19: 159, -18: 280, -17: 557, -16: 956, -15: 1442, -14: 2069, -13: 3067, -12: 4347, -11: 6029, -10: 8659, -9: 11891, -8: 17346, -7: 22065, -6: 29918, -5: 35943, -4: 52662, -3: 64152, -2: 94357, -1: 121512, 0: 908834, +1: 390, +2: 113, +3: 53, +4: 21 |
| 2 | 4 | 8 | -23: 1, -22: 3, -21: 4, -20: 11, -19: 32, -18: 67, -17: 130, -16: 196, -15: 336, -14: 533, -13: 804, -12: 1129, -11: 1592, -10: 2357, -9: 3213, -8: 4708, -7: 6223, -6: 8520, -5: 10475, -4: 15383, -3: 19656, -2: 27975, -1: 35191, 0: 335369, +1: 71, +2: 30, +3: 5, +4: 3 |

## How the walks stop

| p | n | q | depth | the order drops at each point | residual order 0 | cap |
|---|---|---|---|---|---|---|
| 2 | 2 | 2 | 12 | 102266 | 397710 | 12 |
| 2 | 3 | 2 | 139548 | 0 | 335670 | 13782 |
| 2 | 4 | 2 | 1400 | 0 | 35339 | 21261 |
| 2 | 2 | 4 | 258 | 103452 | 168283 | 7 |
| 2 | 3 | 4 | 17799 | 15395 | 48151 | 2655 |
| 2 | 4 | 4 | 20592 | 3826 | 53216 | 33366 |
| 2 | 2 | 8 | 860 | 249954 | 249180 | 6 |
| 2 | 3 | 8 | 44644 | 105232 | 168981 | 30143 |
| 2 | 4 | 8 | 13605 | 10351 | 33933 | 33111 |

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
