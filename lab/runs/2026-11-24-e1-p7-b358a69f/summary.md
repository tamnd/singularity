# e1-p7

How does the residual order of z^q + F over F_7 change under random point blowups that keep the order q, for q = 7 and q = 49 and n = 2, 3, 4 variables? How many steps go up by more than the bound p^(e-1) of Moh, and what are the kangaroo points?

- Experiment: E1. Node: SG00000016.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e1-p7.yaml`, sha256 b358a69f6151.
- Seed: 20261124007.
- The host and the wall time are in `record.json`.

The run did 2578000 random walks with 4331049 point blowups in 6 cases. At each step the order of f stays q.

## Results

A kangaroo point is a step at which the residual order goes up. The bound of Moh for one step is p^(e-1). The stability bound is d0 + p^(e-1), with d0 the residual order at the start of the walk.

| p | n | q | walks | steps | kangaroo points | largest increase | p^(e-1) | steps over p^(e-1) | walks over d0 + p^(e-1) |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 2 | 7 | 1000000 | 1212765 | 90 | 1 | 1 | 0 | 0 |
| 7 | 3 | 7 | 320000 | 1387347 | 12 | 1 | 1 | 0 | 0 |
| 7 | 4 | 7 | 37000 | 185885 | 3 | 1 | 1 | 0 | 0 |
| 7 | 2 | 49 | 1000000 | 1055815 | 68 | 6 | 7 | 0 | 0 |
| 7 | 3 | 49 | 178000 | 395724 | 0 | 0 | 7 | 0 | 0 |
| 7 | 4 | 49 | 43000 | 93513 | 0 | 0 | 7 | 0 | 0 |

## The change of the residual order

Each entry is a change d' - d and the number of steps with that change.

| p | n | q | changes |
|---|---|---|---|
| 7 | 2 | 7 | -20: 2, -19: 71, -18: 217, -17: 512, -16: 1180, -15: 2394, -14: 3578, -13: 4892, -12: 7226, -11: 9537, -10: 13514, -9: 18042, -8: 26687, -7: 34581, -6: 48906, -5: 61783, -4: 87069, -3: 112375, -2: 149790, -1: 237106, 0: 393213, +1: 90 |
| 7 | 3 | 7 | -20: 4, -19: 25, -18: 54, -17: 190, -16: 473, -15: 900, -14: 1445, -13: 2184, -12: 3406, -11: 4601, -10: 6508, -9: 8787, -8: 13208, -7: 17208, -6: 24760, -5: 30366, -4: 44373, -3: 56023, -2: 81095, -1: 115270, 0: 976455, +1: 12 |
| 7 | 4 | 7 | -20: 1, -19: 4, -18: 8, -17: 23, -16: 57, -15: 129, -14: 158, -13: 302, -12: 460, -11: 626, -10: 888, -9: 1169, -8: 1607, -7: 1967, -6: 2919, -5: 3358, -4: 5211, -3: 6765, -2: 10390, -1: 12686, 0: 137154, +1: 3 |
| 7 | 2 | 49 | -138: 1, -137: 3, -136: 3, -135: 1, -134: 3, -133: 4, -132: 6, -131: 7, -130: 5, -129: 6, -128: 5, -127: 11, -126: 15, -125: 15, -124: 15, -123: 24, -122: 27, -121: 32, -120: 20, -119: 38, -118: 37, -117: 38, -116: 52, -115: 55, -114: 61, -113: 75, -112: 98, -111: 89, -110: 104, -109: 109, -108: 134, -107: 141, -106: 169, -105: 172, -104: 224, -103: 209, -102: 277, -101: 318, -100: 300, -99: 324, -98: 374, -97: 383, -96: 397, -95: 440, -94: 474, -93: 475, -92: 544, -91: 576, -90: 584, -89: 645, -88: 673, -87: 711, -86: 729, -85: 730, -84: 773, -83: 868, -82: 911, -81: 881, -80: 953, -79: 1002, -78: 1056, -77: 1116, -76: 1148, -75: 1215, -74: 1213, -73: 1318, -72: 1342, -71: 1358, -70: 1494, -69: 1526, -68: 1609, -67: 1683, -66: 1772, -65: 1857, -64: 1971, -63: 1971, -62: 2041, -61: 2293, -60: 2413, -59: 2422, -58: 2705, -57: 2807, -56: 2969, -55: 2941, -54: 3226, -53: 3268, -52: 3591, -51: 3692, -50: 3901, -49: 4068, -48: 4411, -47: 4393, -46: 4630, -45: 4860, -44: 4938, -43: 5150, -42: 5354, -41: 5792, -40: 5930, -39: 6117, -38: 6554, -37: 6735, -36: 7036, -35: 7396, -34: 7685, -33: 7975, -32: 8402, -31: 8516, -30: 9115, -29: 9550, -28: 9857, -27: 10366, -26: 10760, -25: 11094, -24: 11664, -23: 12145, -22: 12809, -21: 13237, -20: 13753, -19: 14575, -18: 15144, -17: 15507, -16: 16400, -15: 17005, -14: 17561, -13: 18085, -12: 19117, -11: 19273, -10: 20396, -9: 21128, -8: 21748, -7: 23492, -6: 23270, -5: 24236, -4: 25113, -3: 25928, -2: 26914, -1: 34699, 0: 337596, +1: 13, +2: 11, +3: 15, +4: 12, +5: 8, +6: 9 |
| 7 | 3 | 49 | -138: 1, -130: 1, -129: 1, -128: 1, -126: 2, -125: 2, -124: 2, -123: 3, -122: 2, -121: 2, -120: 4, -119: 3, -118: 7, -117: 4, -116: 8, -115: 12, -114: 9, -113: 5, -112: 11, -111: 15, -110: 10, -109: 22, -108: 18, -107: 20, -106: 26, -105: 40, -104: 25, -103: 36, -102: 41, -101: 52, -100: 50, -99: 37, -98: 60, -97: 76, -96: 72, -95: 90, -94: 82, -93: 101, -92: 102, -91: 114, -90: 113, -89: 135, -88: 125, -87: 147, -86: 151, -85: 160, -84: 155, -83: 183, -82: 199, -81: 204, -80: 230, -79: 234, -78: 252, -77: 251, -76: 280, -75: 274, -74: 275, -73: 297, -72: 322, -71: 353, -70: 335, -69: 375, -68: 371, -67: 375, -66: 428, -65: 455, -64: 471, -63: 479, -62: 510, -61: 575, -60: 560, -59: 558, -58: 650, -57: 636, -56: 663, -55: 742, -54: 741, -53: 826, -52: 840, -51: 880, -50: 1000, -49: 964, -48: 1088, -47: 1070, -46: 1154, -45: 1218, -44: 1279, -43: 1286, -42: 1398, -41: 1440, -40: 1443, -39: 1546, -38: 1623, -37: 1732, -36: 1773, -35: 1829, -34: 1973, -33: 2020, -32: 2054, -31: 2301, -30: 2352, -29: 2352, -28: 2481, -27: 2646, -26: 2789, -25: 2884, -24: 3022, -23: 3109, -22: 3315, -21: 3641, -20: 3714, -19: 3871, -18: 3979, -17: 4144, -16: 4413, -15: 4584, -14: 4853, -13: 4996, -12: 5307, -11: 5396, -10: 5739, -9: 5961, -8: 6280, -7: 6363, -6: 6738, -5: 7056, -4: 7519, -3: 7732, -2: 8256, -1: 8974, 0: 204088 |
| 7 | 4 | 49 | -134: 1, -130: 1, -119: 1, -117: 2, -115: 1, -114: 2, -113: 3, -112: 3, -111: 3, -110: 5, -109: 4, -108: 2, -107: 1, -106: 7, -105: 9, -104: 10, -103: 3, -102: 4, -101: 5, -100: 15, -99: 16, -98: 12, -97: 16, -96: 12, -95: 14, -94: 20, -93: 20, -92: 34, -91: 24, -90: 30, -89: 27, -88: 39, -87: 35, -86: 44, -85: 40, -84: 33, -83: 51, -82: 72, -81: 66, -80: 54, -79: 59, -78: 61, -77: 72, -76: 72, -75: 73, -74: 69, -73: 71, -72: 71, -71: 87, -70: 90, -69: 109, -68: 99, -67: 114, -66: 100, -65: 113, -64: 116, -63: 127, -62: 130, -61: 153, -60: 134, -59: 153, -58: 153, -57: 184, -56: 168, -55: 169, -54: 190, -53: 178, -52: 219, -51: 239, -50: 214, -49: 239, -48: 229, -47: 238, -46: 245, -45: 299, -44: 311, -43: 303, -42: 315, -41: 323, -40: 307, -39: 331, -38: 381, -37: 365, -36: 373, -35: 400, -34: 409, -33: 420, -32: 537, -31: 490, -30: 515, -29: 511, -28: 510, -27: 534, -26: 569, -25: 650, -24: 658, -23: 705, -22: 724, -21: 811, -20: 823, -19: 851, -18: 923, -17: 1020, -16: 1052, -15: 1114, -14: 1137, -13: 1197, -12: 1299, -11: 1339, -10: 1536, -9: 1528, -8: 1581, -7: 1739, -6: 1789, -5: 1935, -4: 2018, -3: 2126, -2: 2284, -1: 2464, 0: 46528 |

## How the walks stop

| p | n | q | depth | the order drops at each point | residual order 0 | cap |
|---|---|---|---|---|---|---|
| 7 | 2 | 7 | 1547 | 481023 | 517414 | 16 |
| 7 | 3 | 7 | 63617 | 81425 | 141159 | 33799 |
| 7 | 4 | 7 | 7346 | 2788 | 10584 | 16282 |
| 7 | 2 | 49 | 745 | 577065 | 404588 | 17602 |
| 7 | 3 | 49 | 777 | 60834 | 34902 | 81487 |
| 7 | 4 | 49 | 183 | 7468 | 3243 | 32106 |

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
