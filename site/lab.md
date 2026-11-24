---
title: Lab
description: The runs of the computation lab of singularity, with the question, the counts and the outputs of each run.
lead: Each run of the lab answers one question with a computation. A run is data from examples. It does not prove a statement.
---
The lab is spec 13 of the project. The tool is `sing lab` of [singularity-agent](https://github.com/tamnd/singularity-agent). The spec of each run is in `lab/specs/` and its outputs are in `lab/runs/` of the content repository. You can run a spec again with `sing lab run` and get the same outputs. Only the host and the times in `record.json` change.

The runs work with the equations $z^q + F$ over $\mathbb{F}_p$ of section 2 of [Hauser and Perlega](paper:HP19a), with $q = p^e$. The residual order is the order of $G$ in $F = \prod x_i^{r_i} G$ along the divisor ([SG00000013](node:SG00000013)). A kangaroo point is a blowup at which the residual order goes up ([SG00000016](node:SG00000016)). The bound of Moh says that one point blowup adds at most $p^{e-1}$ ([SG00000015](node:SG00000015)).

E1 makes random walks of point blowups and counts the changes of the residual order. E2 tests candidate secondary invariants on the same walks and records the first step where each one goes up. The runs `e1-hp-section3` and `e1-hp-cycle-p2` compute the examples of Hauser and Perlega again.

The lab computes in the given coordinates, at the points over $\mathbb{F}_p$ only. A step over the bound of Moh in this data is not a counterexample to the theorem of Moh, because the theorem is about well chosen coordinates. A candidate with no failure is not proved.
