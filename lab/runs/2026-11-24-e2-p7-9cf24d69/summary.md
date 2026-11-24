# e2-p7

Which candidate secondary invariants go up under a point blowup on the walks of e1-p7, and at which step does each one fail first?

- Experiment: E2. Node: SG00000013.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `e2-p7.yaml`, sha256 9cf24d69a6d7.
- Walks: the walks of `e1-p7.yaml`, sha256 b358a69f6151. The run makes the same walks again from the same seed.
- Seed: 20261124007.
- The host and the wall time are in `record.json`.

The run tests 6 candidates on 4331049 steps of 2578000 walks in 6 cases. A candidate fails at a step when its value after the blowup is larger than its value before.

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
| `d-n` | 4331049 | 152199 | p = 7, n = 2, q = 7, walk 7, step 0: (2, 1) to (2, 2) |
| `d-over-q` | 4331049 | 173 | p = 7, n = 2, q = 7, walk 7617, step 2: 1/7 to 2/7 |
| `d-minus-pr-moh` | 4331049 | 1802 | p = 7, n = 2, q = 7, walk 7617, step 2: 1 - 1 = 0 to 2 - 1 = 1 |
| `d-minus-pr-g` | 4331049 | 51165 | p = 7, n = 2, q = 7, walk 13, step 0: 7 - 7 = 0 to 4 - 1 = 3 |
| `d-minus-r` | 4331049 | 443 | p = 7, n = 2, q = 7, walk 7617, step 2: (1, 0) to (2, 0) |
| `moh-rounded` | 4331049 | 0 | none |

## Failures in each case

| p | n | q | steps | `d-n` | `d-over-q` | `d-minus-pr-moh` | `d-minus-pr-g` | `d-minus-r` | `moh-rounded` |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 2 | 7 | 1212765 | 89708 | 90 | 90 | 26738 | 90 | 0 |
| 7 | 3 | 7 | 1387347 | 41229 | 12 | 12 | 10497 | 12 | 0 |
| 7 | 4 | 7 | 185885 | 5024 | 3 | 3 | 675 | 3 | 0 |
| 7 | 2 | 49 | 1055815 | 12420 | 68 | 1573 | 11047 | 317 | 0 |
| 7 | 3 | 49 | 395724 | 3172 | 0 | 114 | 1982 | 19 | 0 |
| 7 | 4 | 49 | 93513 | 646 | 0 | 10 | 226 | 2 | 0 |

## The files

- `candidates.json`: the counts of each candidate in each case, with the first failure. A failure has the polynomial, the divisor, the chart and the translations, so you can check it again with `sing lab step`.
- `histogram.json`: the counts of the walks. It is the same file as in the run of the walks, because the walks are the same.

## Notes

The run makes the walks of e1-p7 again from the same seed and tests each candidate at each step. The candidates (a) to (d) of the question are d-n, d-over-q, d-minus-pr-moh and d-minus-r. d-minus-pr-g is a second form of (c) with r computed on in(G) and not on in(F). moh-rounded is the bound floor(d/p^r) p^r + p^r of the proof of Moh, which Hauser and Perlega show to be false. A failure of moh-rounded is a step where d' is larger than that bound.

## What the data does not show

- A candidate with no failure on these walks is not proved to go down. The walks are a small sample, in the given coordinates, at the points over F_p only.
- A failure is in the given coordinates. It shows that the candidate in this form does not work. It does not show that no form of the idea works.
- This is data from examples. It does not prove a statement.
