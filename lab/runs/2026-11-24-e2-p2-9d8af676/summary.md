# e2-p2

Which candidate secondary invariants go up under a point blowup on the walks of e1-p2, and at which step does each one fail first?

- Experiment: E2. Node: SG00000013.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e2-p2.yaml`, sha256 9d8af676b3fd.
- Walks: the walks of `e1-p2.yaml`, sha256 90966cbf6b0c. The run makes the same walks again from the same seed.
- Seed: 20261124002.
- The host and the wall time are in `record.json`.

The run tests 6 candidates on 7051981 steps of 2454000 walks in 9 cases. A candidate fails at a step when its value after the blowup is larger than its value before.

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
| `d-n` | 7051981 | 429546 | p = 2, n = 2, q = 2, walk 8, step 2: (1, 1) to (1, 2) |
| `d-over-q` | 7051981 | 15211 | p = 2, n = 2, q = 2, walk 80, step 1: 2/2 to 3/2 |
| `d-minus-pr-moh` | 7051981 | 40277 | p = 2, n = 2, q = 2, walk 80, step 1: 2 - 1 = 1 to 3 - 1 = 2 |
| `d-minus-pr-g` | 7051981 | 110268 | p = 2, n = 2, q = 2, walk 33, step 0: 2 - 2 = 0 to 2 - 1 = 1 |
| `d-minus-r` | 7051981 | 37106 | p = 2, n = 2, q = 2, walk 80, step 1: (2, 0) to (3, 0) |
| `moh-rounded` | 7051981 | 111 | p = 2, n = 3, q = 4, walk 1196, step 2: d = 1, p^rF = 2 to d = 3, p^rF = 2 |

## Failures in each case

| p | n | q | steps | `d-n` | `d-over-q` | `d-minus-pr-moh` | `d-minus-pr-g` | `d-minus-r` | `moh-rounded` |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 2 | 580121 | 83067 | 6770 | 6770 | 19063 | 6770 | 0 |
| 2 | 3 | 2 | 2360914 | 145498 | 4516 | 4516 | 23986 | 4516 | 0 |
| 2 | 4 | 2 | 264994 | 16931 | 472 | 472 | 2521 | 472 | 0 |
| 2 | 2 | 4 | 361101 | 43148 | 1021 | 5246 | 9798 | 5246 | 0 |
| 2 | 3 | 4 | 378763 | 18019 | 348 | 2252 | 6379 | 2252 | 24 |
| 2 | 4 | 4 | 623688 | 23720 | 419 | 3253 | 6839 | 3253 | 34 |
| 2 | 2 | 8 | 621449 | 44180 | 979 | 9767 | 17396 | 7567 | 0 |
| 2 | 3 | 8 | 1386934 | 43817 | 577 | 6307 | 20211 | 5480 | 41 |
| 2 | 4 | 8 | 474017 | 11166 | 109 | 1694 | 4075 | 1550 | 12 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. It is the same file as in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of e1-p2 again from the same seed and tests each candidate at each step. The candidates (a) to (d) of the question are d-n, d-over-q, d-minus-pr-moh and d-minus-r. d-minus-pr-g is a second form of (c) with r computed on in(G) and not on in(F). moh-rounded is the bound floor(d/p^r) p^r + p^r of the proof of Moh, which Hauser and Perlega show to be false. A failure of moh-rounded is a step where d' is larger than that bound.

## What the data does not show

- A candidate with no failure on these walks is not proved to go down. The walks are a small sample, in the given coordinates, at the points over F_p only.
- A failure is in the given coordinates. It shows that the candidate in this form does not work. It does not show that no form of the idea works.
- This is data from examples. It does not prove a statement.
