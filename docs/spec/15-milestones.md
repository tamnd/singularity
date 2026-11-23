# 15. Milestones

Each milestone has a goal, exit criteria that a tool can check (or a named person signs), and a release. The dates are targets set on 2026-11-23. The levels G1 to G6 are those of document 02, and the tiers T0 to T8 are those of document 07.

| Milestone | Target | Goal | Exit criteria | Release |
|---|---|---|---|---|
| S0 | 2026-12-15 | the three repositories, the statements, the site | `Singularity/Statements/` builds; F1 to F3 of 06.3 pass for `ResolutionInDim`, `ResolutionDimFourCharP` and P1; `sing index`, `sing status`, `sing site build` work; singularity.tamnd.com shows `/problem/`, `/map/` (tiers T0 to T8 as nodes, most `stated` or not yet stated), `/trust/`; hironaka is a pinned Lake dependency and builds; the letter to the author of riemann-lean (05.6) is sent | singularity v0.1.0, agent v0.1.0 |
| S1 | 2027-01-31 | the char 0 base and the bridges | Q1 to Q4 **yes** for the main theorems of hironaka on a project machine, with the `nanoda` replay on; `resolutionInDim_zero` (06.4) proved from hironaka and, in the cross-check package, from riemann-lean; the bridge to formal-conjectures (06.4) proved; `records/base-charzero.json` (05.5, step 5) complete; the `CharZero` split done for `Scheme/BlowUp`, `Scheme/BlowUpSequence` and `Scheme/Snc` | v0.2.0; handbook Vol. 0 draft |
| S2 | 2027-03-31 | tier T1 and dimension 1 | `regularLocus_isOpen` for varieties; finiteness of normalization for varieties; Hilbert-Samuel function and multiplicity; `resolutionInDim_one` proved for every $p$; F1 to F6 for `ResolutionInDim` done (two outside reviewers) | v0.3.0; handbook Vol. 1 chapters 1 to 6 checked |
| S3 | 2027-04-30 | the lab and the core invariants | `sing lab` with Singular, Macaulay2 and `sing-lab`; experiments E1, E2 run and published; tier T4 nodes for order, residual order and Newton polyhedra `proved`; Moh's one-step bound `stated`, with a proof plan; the Hauser-Perlega cycle (01, 1.6) checked in Lean as a certified example; E8 run | v0.4.0 |
| S4 | 2027-07-31 | surfaces | `resolutionInDim_two` (Lipman, for varieties first, then all excellent surfaces) proved, either from the AxiomMath/Stacks proof after a human review and a bridge (Q-07), or by the project; embedded resolution of surfaces stated, half of its nodes proved | v0.5.0; handbook Vol. 2 checked, Vol. 4 drafted |
| S5 | 2027-10-31 | valuations and local uniformization | tier T2 proved (Zariski-Riemann space, Abhyankar inequality, key polynomials); `localUniformization_abhyankar` proved; Temkin's inseparable local uniformization stated, with its nodes | v0.6.0; Vol. 3 checked |
| S6 | 2028-03-31 | threefolds | `resolutionInDim_three` (Cossart-Piltant) proved, or `proved-mod` with at most five named hypotheses; Moh's one-step bound proved; the dimension 3 invariants of Cossart-Piltant compared with dimension 4 in the lab (E4) | v1.0.0; Vol. 6 drafted |
| S7 | 2028-06-30 | the first research result (G4) | at least one new node on a route (04) of the size of a paper lemma, proved in Lean, with a preprint that an outside expert has read | v1.1.0; Vol. 9 first report |
| S8 | 2028-12-31 | alterations and the full library (G1) | de Jong's theorem proved; tiers T1 to T7 at least 90% `proved` | v1.2.0; Vols. 1 to 8 released |
| S9 | open | the open case (G5) | `ResolutionDimFourCharP` proved and all nine trust rows **yes** | v2.0.0 |

The research routes (04) run from S3 on, in parallel with the library. They take about a third of the agent budget from S3, and more as the library is finished. Each milestone report says what each route found, including the negative results.

## 15.1 What can slip and what cannot

- The **statements and the trust tooling** (S0) cannot slip, because every later result depends on them.
- The **order of the library** can change. If surfaces turn out cheaper than valuations, S4 and S5 trade places.
- **S6 is the largest risk of the library.** The Cossart-Piltant papers are long and use many special computations. The plan budgets six months, and it allows a `proved-mod` result, with named hypotheses, at the milestone.
- **S7 is a research milestone.** If no route gives a new result by then, the milestone report says so, and the project re-plans with the experts (02.6).

## 15.2 The budget

The agent budget starts at 200 dollars a day (10.6) and is raised by the owner when the measured cost per proved node shows that it pays. The trust workflow and the full builds need a rented machine for a few hours each week. The first measurement of cost per node is an exit criterion of S2.
