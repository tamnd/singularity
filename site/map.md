---
title: The map
description: Each node of the project, with its tier, its status and the Lean declarations that it names.
lead: The map has a node for each definition, theorem and open question that the project uses. A tool computes the status of each node from the Lean build.
---
A node is `planned` when its Lean statement does not exist yet, `stated` when the statement builds and no proof exists, `defined` for a definition that builds, `proved` when the proof uses the standard axioms only and each node that it uses is proved, `proved-mod` when the proof takes named nodes as hypotheses, `open` for an open problem, and `refuted` when the negation is proved. A proof with `sorry` is never `proved`.
