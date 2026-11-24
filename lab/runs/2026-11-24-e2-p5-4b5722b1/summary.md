# e2-p5

Which candidate secondary invariants go up under a point blowup on the walks of e1-p5, and at which step does each one fail first?

- Experiment: E2. Node: SG00000013.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e2-p5.yaml`, sha256 4b5722b13600.
- Walks: the walks of `e1-p5.yaml`, sha256 54c44a97c686. The run makes the same walks again from the same seed.
- Seed: 20261124005.
- The host and the wall time are in `record.json`.

The run tests 6 candidates on 2023166 steps of 1148000 walks in 6 cases. A candidate fails at a step when its value after the blowup is larger than its value before.

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
| `d-n` | 2023166 | 108660 | p = 5, n = 2, q = 5, walk 14, step 0: (3, 1) to (3, 2) |
| `d-over-q` | 2023166 | 280 | p = 5, n = 2, q = 5, walk 2195, step 1: 5/5 to 6/5 |
| `d-minus-pr-moh` | 2023166 | 1553 | p = 5, n = 2, q = 5, walk 2195, step 1: 5 - 1 = 4 to 6 - 1 = 5 |
| `d-minus-pr-g` | 2023166 | 36976 | p = 5, n = 2, q = 5, walk 22, step 0: 5 - 5 = 0 to 3 - 1 = 2 |
| `d-minus-r` | 2023166 | 611 | p = 5, n = 2, q = 5, walk 2195, step 1: (5, 0) to (6, 0) |
| `moh-rounded` | 2023166 | 0 | none |

## Failures in each case

| p | n | q | steps | `d-n` | `d-over-q` | `d-minus-pr-moh` | `d-minus-pr-g` | `d-minus-r` | `moh-rounded` |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 2 | 5 | 763039 | 73672 | 185 | 185 | 22627 | 185 | 0 |
| 5 | 3 | 5 | 554376 | 19732 | 18 | 18 | 5958 | 18 | 0 |
| 5 | 4 | 5 | 113833 | 3888 | 3 | 3 | 683 | 3 | 0 |
| 5 | 2 | 25 | 339174 | 8043 | 70 | 1169 | 5949 | 348 | 0 |
| 5 | 3 | 25 | 203520 | 2714 | 4 | 152 | 1561 | 47 | 0 |
| 5 | 4 | 25 | 49224 | 611 | 0 | 26 | 198 | 10 | 0 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. It is the same file as in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of e1-p5 again from the same seed and tests each candidate at each step. The candidates (a) to (d) of the question are d-n, d-over-q, d-minus-pr-moh and d-minus-r. d-minus-pr-g is a second form of (c) with r computed on in(G) and not on in(F). moh-rounded is the bound floor(d/p^r) p^r + p^r of the proof of Moh, which Hauser and Perlega show to be false. A failure of moh-rounded is a step where d' is larger than that bound.

## What the data does not show

- A candidate with no failure on these walks is not proved to go down. The walks are a small sample, in the given coordinates, at the points over F_p only.
- A failure is in the given coordinates. It shows that the candidate in this form does not work. It does not show that no form of the idea works.
- This is data from examples. It does not prove a statement.
