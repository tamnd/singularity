# e1-hp-section3

Does sing-lab give the residual orders of the example of Section 3 of Hauser and Perlega (arXiv:1802.05010), where the residual order goes from 5 to 7 under one point blowup?

- Experiment: E1. Node: SG00000016.
- Tool: sing-lab, in sing dev, commit b52a81e9d961.
- Spec: `lab/specs/e1-hp-section3.yaml`, sha256 ab2c5464c5ce.
- The host and the wall time are in `record.json`.

Source: Hauser and Perlega, Cycles of singularities appearing in the resolution problem in positive characteristic, arXiv:1802.05010, Section 3.

The run starts from one given equation z^4 + F over F_2 and does 1 given point blowup. At each step the order of f stays q.

| step | label | chart | residual order | the source | terms of F |
|---|---|---|---|---|---|
| 0 | start | start | 5 | 5 | 3 |
| 1 | point blowup | x-chart, y -> y+1 | 7 | 7 | 3 |

The engine gives the value of the source at each step where the source gives a value.

The bound of Moh for one step is p^(e-1) = 2. The sequence has 1 step where the residual order goes up, and 0 of them go up by more than the bound.

`steps.json` has the polynomial, the divisor and the invariants after each step.

## Notes

The paper uses this example to show that the step of the proof of Moh with the bound floor(d/p^r) p^r + p^r is false. Here d = 5 and p^r = 2, so that bound is 6, and the residual order after the blowup is 7. The increase 2 is not more than the bound p^(e-1) = 2 of Moh.

This is a computation on one example. It does not prove a statement.
