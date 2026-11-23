---
title: Resolution of singularities in characteristic p
description: A Lean project on the open case of resolution of singularities, dimension 4 and higher in positive characteristic.
eyebrow: Open problem
lead: Each variety over a field of characteristic 0 has a resolution of singularities, by Hironaka (1964). In characteristic $p > 0$ the same statement is known in dimension at most 3 and is open in dimension 4 and higher.
doors:
  - title: I know the mathematics
    path: problem/
    text: The statements, the known cases, the open case and the routes.
  - title: I referee
    path: trust/
    text: The checks that a claim must pass, and the state of each check.
  - title: I am a student
    path: learn/
    text: Paths through the handbook, from regular rings to the open case.
  - title: I know Lean
    path: code/
    text: The package, the pinned toolchain and the statement files.
  - title: I am a program
    path: llms.txt
    text: A text map of the site, and the data in JSON at /api/.
---
This project states the open problem in Lean 4 with Mathlib, builds a library of the known cases, and tries the research routes on a map of nodes. Each node has a status that a tool computes from the Lean build. A person does not set the status by hand.

The open case is not proved. No result on this site is a proof of it. When a node of the open problem changes status, the [trust page](/trust/) shows which checks passed.

The project has three repositories. [tamnd/singularity](https://github.com/tamnd/singularity) has the map, the paper records and this site. [tamnd/singularity-lean](https://github.com/tamnd/singularity-lean) has the Lean code. [tamnd/singularity-agent](https://github.com/tamnd/singularity-agent) has the `sing` command, which checks the map and builds the site.
