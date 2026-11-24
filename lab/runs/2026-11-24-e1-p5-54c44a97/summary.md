# e1-p5

How does the residual order of z^q + F over F_5 change under random point blowups that keep the order q, for q = 5 and q = 25 and n = 2, 3, 4 variables? How many steps go up by more than the bound p^(e-1) of Moh, and what are the kangaroo points?

- Experiment: E1. Node: SG00000016.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e1-p5.yaml`, sha256 54c44a97c686.
- Seed: 20261124005.
- The host and the wall time are in `record.json`.

The run did 1148000 random walks with 2023166 point blowups in 6 cases. At each step the order of f stays q.

## Results

A kangaroo point is a step at which the residual order goes up. The bound of Moh for one step is p^(e-1). The stability bound is d0 + p^(e-1), with d0 the residual order at the start of the walk.

| p | n | q | walks | steps | kangaroo points | largest increase | p^(e-1) | steps over p^(e-1) | walks over d0 + p^(e-1) |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 2 | 5 | 611000 | 763039 | 185 | 1 | 1 | 0 | 0 |
| 5 | 3 | 5 | 122000 | 554376 | 18 | 1 | 1 | 0 | 0 |
| 5 | 4 | 5 | 22000 | 113833 | 3 | 1 | 1 | 0 | 0 |
| 5 | 2 | 25 | 306000 | 339174 | 70 | 4 | 5 | 0 | 0 |
| 5 | 3 | 25 | 71000 | 203520 | 4 | 4 | 5 | 0 | 0 |
| 5 | 4 | 25 | 16000 | 49224 | 0 | 0 | 5 | 0 | 0 |

## The change of the residual order

Each entry is a change d' - d and the number of steps with that change.

| p | n | q | changes |
|---|---|---|---|
| 5 | 2 | 5 | -14: 17, -13: 198, -12: 724, -11: 1976, -10: 3309, -9: 4701, -8: 8377, -7: 12550, -6: 22236, -5: 31959, -4: 51791, -3: 72263, -2: 114712, -1: 193254, 0: 244787, +1: 185 |
| 5 | 3 | 5 | -14: 1, -13: 43, -12: 164, -11: 492, -10: 833, -9: 1469, -8: 2826, -7: 3970, -6: 7275, -5: 10046, -4: 16569, -3: 22209, -2: 38580, -1: 55393, 0: 394488, +1: 18 |
| 5 | 4 | 5 | -14: 1, -13: 9, -12: 22, -11: 113, -10: 201, -9: 309, -8: 579, -7: 857, -6: 1393, -5: 1907, -4: 3159, -3: 4066, -2: 7619, -1: 9700, 0: 83895, +1: 3 |
| 5 | 2 | 25 | -71: 1, -70: 1, -69: 1, -67: 3, -66: 3, -65: 7, -64: 9, -63: 14, -62: 18, -61: 26, -60: 24, -59: 40, -58: 51, -57: 52, -56: 78, -55: 91, -54: 124, -53: 153, -52: 166, -51: 212, -50: 234, -49: 269, -48: 313, -47: 362, -46: 398, -45: 393, -44: 482, -43: 504, -42: 562, -41: 627, -40: 683, -39: 652, -38: 764, -37: 833, -36: 824, -35: 953, -34: 1047, -33: 1175, -32: 1291, -31: 1374, -30: 1609, -29: 1763, -28: 1972, -27: 2045, -26: 2404, -25: 2514, -24: 2781, -23: 2961, -22: 3205, -21: 3425, -20: 3922, -19: 4047, -18: 4567, -17: 4882, -16: 5398, -15: 5761, -14: 6533, -13: 6824, -12: 7562, -11: 8017, -10: 8723, -9: 9490, -8: 10271, -7: 10997, -6: 12045, -5: 13534, -4: 13631, -3: 15118, -2: 16332, -1: 21147, 0: 110810, +1: 18, +2: 22, +3: 18, +4: 12 |
| 5 | 3 | 25 | -67: 2, -65: 1, -64: 1, -62: 3, -61: 1, -60: 6, -59: 9, -58: 6, -57: 9, -56: 16, -55: 15, -54: 26, -53: 30, -52: 41, -51: 39, -50: 59, -49: 63, -48: 81, -47: 76, -46: 83, -45: 133, -44: 114, -43: 182, -42: 151, -41: 185, -40: 200, -39: 240, -38: 246, -37: 246, -36: 313, -35: 334, -34: 332, -33: 356, -32: 398, -31: 474, -30: 551, -29: 534, -28: 612, -27: 691, -26: 759, -25: 778, -24: 953, -23: 996, -22: 1085, -21: 1147, -20: 1342, -19: 1408, -18: 1584, -17: 1707, -16: 1826, -15: 1999, -14: 2269, -13: 2419, -12: 2716, -11: 2923, -10: 3440, -9: 3648, -8: 3904, -7: 4277, -6: 4804, -5: 5183, -4: 5563, -3: 6191, -2: 6669, -1: 7769, 0: 119298, +2: 1, +3: 2, +4: 1 |
| 5 | 4 | 25 | -62: 2, -61: 2, -58: 2, -57: 5, -54: 4, -53: 6, -52: 10, -51: 11, -50: 9, -49: 16, -48: 15, -47: 20, -46: 33, -45: 25, -44: 27, -43: 33, -42: 36, -41: 45, -40: 46, -39: 42, -38: 48, -37: 52, -36: 68, -35: 56, -34: 83, -33: 87, -32: 98, -31: 105, -30: 126, -29: 133, -28: 135, -27: 138, -26: 175, -25: 206, -24: 208, -23: 199, -22: 230, -21: 281, -20: 271, -19: 346, -18: 326, -17: 374, -16: 449, -15: 437, -14: 496, -13: 521, -12: 545, -11: 673, -10: 714, -9: 802, -8: 903, -7: 1026, -6: 1107, -5: 1283, -4: 1411, -3: 1563, -2: 1777, -1: 1917, 0: 29466 |

## How the walks stop

| p | n | q | depth | the order drops at each point | residual order 0 | cap |
|---|---|---|---|---|---|---|
| 5 | 2 | 5 | 469 | 264212 | 346293 | 26 |
| 5 | 3 | 5 | 28243 | 24523 | 61599 | 7635 |
| 5 | 4 | 5 | 4498 | 991 | 8226 | 8285 |
| 5 | 2 | 25 | 459 | 173314 | 131539 | 688 |
| 5 | 3 | 25 | 1532 | 26010 | 20981 | 22477 |
| 5 | 4 | 25 | 313 | 2959 | 2175 | 10553 |

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
