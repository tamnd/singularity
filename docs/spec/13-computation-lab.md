# 13. The computation lab

Resolution in char p is a subject where examples have decided the direction more than once: Narasimhan's example ended the hope for maximal contact, Moh's and Hauser's examples showed that the residual order can go up, Cutkosky's examples showed that local monomialization fails. A project that wants new results needs a fast way to test an idea on many examples before it spends months on a proof. The lab is that tool. Its results are data, not proofs. A result enters the map only as a node of kind `example`, `counterexample` or `conjecture`. A counterexample becomes a theorem when Lean checks it (13.4).

## 13.1 Tools

| Tool | Use | Note |
|---|---|---|
| Singular | standard bases in char p, blowups in charts, primary decomposition | `resolve.lib` is char 0 only; the lab uses its blowup and chart procedures, not its algorithm |
| Macaulay2 | Rees algebras, integral closure, Hilbert-Samuel functions, the `ReesAlgebra` and `Normaliz` packages | |
| OSCAR (Julia) | polyhedral geometry, toric charts, a modern interface | |
| SageMath | glue, MacLane-Vaquié key polynomials for valuations (`sage.rings.valuation`) | |
| `sing-lab` (Rust) | the inner loops: Newton and characteristic polyhedra, residual orders of $z^p + g$, random blowup walks; millions of examples per hour | written by the project, in `singularity-agent/lab/` |
| Lean | checks a certificate (13.4) | |

## 13.2 Specs and runs

A lab job is a spec file in `tamnd/singularity/lab/specs/<name>.yaml`:

```yaml
name: residual-order-walks-p3-n4
question: Does the residual order of z^3 + g(x1..x4) increase by more than 1 under one permissible point blowup?
tool: sing-lab
inputs:
  p: 3
  n: 4
  g: { family: random-sparse, degree: [4, 24], terms: [2, 8], seed: 20261123 }
  walks: { count: 1000000, depth: 12, centre: [point, regular-curve-in-max-locus] }
outputs: [histogram of increases, first 100 examples of each increase]
node: SG7Y2N0QBE      # Moh's one-step bound (01, 1.6)
```

`sing lab run` runs it in a container with pinned images and no network, and writes `lab/runs/<id>/` with the spec hash, the image digests, the seed, the wall time, the outputs and a short summary. A run is reproducible from its record.

## 13.3 The first experiments

| Id | Question | Route | Why it matters |
|---|---|---|---|
| E1 | The distribution of the change of the residual order of $z^p + g(x_1, \dots, x_n)$ under permissible blowups, for $p \in \{2, 3, 5, 7\}$ and $n \in \{2, 3, 4\}$; check Moh's one-step bound; collect every kangaroo point; reproduce the cycles of Hauser-Perlega | R1, R5 | the main data of the core problem P1 |
| E2 | For each candidate secondary invariant (the list grows from 04), test monotonicity on the walks of E1; record the first failure | R1, R5 | kills bad invariants in hours, not months |
| E3 | Search for analogues of Narasimhan's example: hypersurfaces whose maximal order locus is not contained in a smooth hypersurface, with $n = 4, 5$ | R3 | maps where weak maximal contact must be used |
| E4 | Recompute the invariants of the Cossart-Piltant proof for random threefolds of the form $z^p + g(x, y)$ with $g$ of 3 variables (dim 3 case), and compare with the dimension 4 analogues | R1 | shows which dim 3 invariants still drop in dim 4 |
| E5 | Key polynomials and defect for valuations on $k(x_1, \dots, x_4)$ given by generating sequences over $\mathbb{F}_p$; find valuations with defect that are centred at a point of a 4-fold | R2 | the hard cases of local uniformization |
| E6 | The IFP invariant of Kawanoue-Matsuki and the elimination invariant of Villamayor-Benito on the same examples | R3 | compares the programs on the same data |
| E7 | Weighted blowups in char p: for the weighted centre that ATW would choose, how often does the char 0 invariant drop anyway, and how does it fail | R4 | measures how far the weighted method is from working |
| E8 | Reproduce Bérczi's AlphaEvolve result (arXiv:2602.06553) on $z^3 + g + z^2 h$ in dimension 4, then test his two conjectures on the walks of E1 with all permissible centres, not only those of his simulator | R5 | the one published search of this kind; a check of it and a first extension |
| E9 | The invariants of the claimed proofs (01, 1.2), where they can be computed, on the obstruction list of 01, 1.6 | all | a cheap test of a long claim |

## 13.4 Certificates: from computation to Lean

A computation that finds a specific example (a hypersurface, a blowup sequence, a point where an invariant goes up) can be checked in Lean when it comes with a certificate:

- **Charts.** A blowup of $\mathbb{A}^n_{\mathbb{F}_p}$ in a coordinate centre is given by explicit chart maps. The strict transform in a chart is a polynomial computation, checked by `ring` or `decide` over $\mathbb{F}_p$.
- **Orders.** "The order of $f$ at the origin is $a$" means $f \in \mathfrak{m}^a$ and $f \notin \mathfrak{m}^{a+1}$, which reduces to the coefficients of $f$, a finite check.
- **Regularity.** "The strict transform is regular at the points of the chart over the origin" follows from the Jacobian criterion with an explicit combination $\sum c_i \partial_i f + c f = 1$ in the local ring, checked by `linear_combination`.
- **Increase of an invariant.** A kangaroo example is the composite of the above.

So a counterexample to a conjecture of the lab becomes a Lean theorem (`Singularity.Examples.*`) with status `proved`, and it can refute a node. The `refuter` role writes these theorems from lab outputs.

## 13.5 What the lab does not do

It does not decide that a statement is true. A conjecture with a billion supporting examples has status `open`. The lab also does not run an algorithm on the problem and call the output a resolution, except as a certified example in the sense of 13.4.
