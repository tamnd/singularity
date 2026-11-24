# e1-hp-cycle-p2

Does sing-lab give the residual orders of one cycle of the first example of Section 4 of Hauser and Perlega (arXiv:1802.05010), with d = 2, a = b = r = 0, s = 1, lambda = 1, A = 1 and Q = 0?

- Experiment: E1. Node: SG00000017.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `lab/specs/e1-hp-cycle-p2.yaml`, sha256 5f991b2a0287.
- The host and the wall time are in `record.json`.

Source: Hauser and Perlega, arXiv:1802.05010, Section 4, first example (p = 2, n = 5, ord f = 8), with the choices of the question.

The run starts from one given equation z^8 + F over F_2 and does 20 given point blowups. At each step the order of f stays q.

| step | label | chart | residual order | the source | terms of F |
|---|---|---|---|---|---|
| 0 | start | start | 2 | 2 | 2 |
| 1 | (1) | x-chart, y -> y+1, u -> u+1 | 6 | 6 | 9 |
| 2 | (2) | x-chart | 5 | 5 | 9 |
| 3 | (3) | u-chart | 5 |  | 9 |
| 4 | (4) | v-chart | 5 |  | 9 |
| 5 | (5) | w-chart, y -> y+1, v -> v+1 | 5 |  | 136 |
| 6 | (6) | u-chart | 4 | 4 | 136 |
| 7 | (7) | y-chart | 4 |  | 136 |
| 8 | (7) | y-chart | 4 |  | 136 |
| 9 | (7) | y-chart | 4 |  | 136 |
| 10 | (7) | y-chart | 4 |  | 136 |
| 11 | (7) | y-chart | 4 |  | 136 |
| 12 | (7) | y-chart | 4 |  | 136 |
| 13 | (7) | y-chart | 4 |  | 136 |
| 14 | (7) | y-chart | 4 |  | 136 |
| 15 | (7) | y-chart | 4 |  | 136 |
| 16 | (7) | y-chart | 4 |  | 136 |
| 17 | (7) | y-chart | 4 |  | 136 |
| 18 | (7) | y-chart | 4 |  | 136 |
| 19 | (7) | y-chart | 4 |  | 136 |
| 20 | (7) | y-chart | 4 | 4 | 136 |

The engine gives the value of the source at each step where the source gives a value.

The bound of Moh for one step is p^(e-1) = 4. The sequence has 1 step where the residual order goes up, and 0 of them go up by more than the bound.

`steps.json` has the polynomial, the divisor and the invariants after each step.

## Notes

The paper writes the equations with unspecified units A and B, a series Q and a constant lambda. This run fixes them as in the question, so B and the later values of A and Q are the ones that the blowups give. The paper gives the residual order after the steps (1), (2), (6) and (7). In this run the residual order is 2 at the start and 4 after the step (7).

This is a computation on one example. It does not prove a statement.
