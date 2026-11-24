# e2-p3

Which candidate secondary invariants go up under a point blowup on the walks of e1-p3, and at which step does each one fail first?

- Experiment: E2. Node: SG00000013.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e2-p3.yaml`, sha256 e8d7d25060e0.
- Walks: the walks of `e1-p3.yaml`, sha256 08768f1a6cba. The run makes the same walks again from the same seed.
- Seed: 20261124003.
- The host and the wall time are in `record.json`.

The run tests 6 candidates on 12480541 steps of 4221000 walks in 6 cases. A candidate fails at a step when its value after the blowup is larger than its value before.

## The candidates

- `d-n`: the pair (d, N) in the lexicographic order, with N the number of terms of in(G), the initial form of the residual factor G.
- `d-over-q`: d/q, the residual order divided by q. Along one walk q does not change, so this candidate fails exactly at the kangaroo points.
- `d-minus-pr-moh`: d - p^rF, with rF the r of Moh: the largest r such that in(F) is a p^r-th power.
- `d-minus-pr-g`: d - p^rG, with rG the largest r such that in(G) is a p^r-th power (rG = 0 when d = 0).
- `d-minus-r`: the pair (d, -rF) in the lexicographic order, with rF the r of Moh.
- `moh-rounded`: the one-step bound d' <= floor(d/p^rF) p^rF + p^rF that the proof of Moh uses (Hauser-Perlega, Section 3). This is a bound, not a value that goes down.

In these definitions, F is clean, E is the divisor, F = prod x_i^(r_i) G along E, d = ord G is the residual order, and in(.) is the initial form.

## Results

| candidate | steps | failures | the first failure |
|---|---|---|---|
| `d-n` | 12480541 | 651694 | p = 3, n = 2, q = 3, walk 0, step 1: (2, 1) to (2, 2) |
| `d-over-q` | 12480541 | 5309 | p = 3, n = 2, q = 3, walk 836, step 0: 1/3 to 2/3 |
| `d-minus-pr-moh` | 12480541 | 26499 | p = 3, n = 2, q = 3, walk 836, step 0: 1 - 1 = 0 to 2 - 1 = 1 |
| `d-minus-pr-g` | 12480541 | 218976 | p = 3, n = 2, q = 3, walk 17, step 1: 3 - 3 = 0 to 2 - 1 = 1 |
| `d-minus-r` | 12480541 | 16397 | p = 3, n = 2, q = 3, walk 836, step 0: (1, 0) to (2, 0) |
| `moh-rounded` | 12480541 | 30 | p = 3, n = 3, q = 9, walk 7316, step 3: d = 2, p^rF = 3 to d = 4, p^rF = 1 |

## Failures in each case

| p | n | q | steps | `d-n` | `d-over-q` | `d-minus-pr-moh` | `d-minus-pr-g` | `d-minus-r` | `moh-rounded` |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 1320396 | 174127 | 1804 | 1804 | 48657 | 1804 | 0 |
| 3 | 3 | 3 | 4716878 | 236182 | 1541 | 1541 | 70462 | 1541 | 0 |
| 3 | 4 | 3 | 1322391 | 62609 | 354 | 354 | 14413 | 354 | 0 |
| 3 | 2 | 9 | 1204267 | 74191 | 1104 | 13942 | 38018 | 7281 | 0 |
| 3 | 3 | 9 | 3156967 | 87273 | 449 | 7462 | 41675 | 4327 | 25 |
| 3 | 4 | 9 | 759642 | 17312 | 57 | 1396 | 5751 | 1090 | 5 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. It is the same file as in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of e1-p3 again from the same seed and tests each candidate at each step. The candidates (a) to (d) of the question are d-n, d-over-q, d-minus-pr-moh and d-minus-r. d-minus-pr-g is a second form of (c) with r computed on in(G) and not on in(F). moh-rounded is the bound floor(d/p^r) p^r + p^r of the proof of Moh, which Hauser and Perlega show to be false. A failure of moh-rounded is a step where d' is larger than that bound.

## What the data does not show

- A candidate with no failure on these walks is not proved to go down. The walks are a small sample, in the given coordinates, at the points over F_p only.
- A failure is in the given coordinates. It shows that the candidate in this form does not work. It does not show that no form of the idea works.
- This is data from examples. It does not prove a statement.
