# singularity

Resolution of singularities in characteristic $p$, in public.

The open problem: every variety of dimension 4 or more over a field of characteristic $p > 0$ has a resolution of singularities. Hironaka proved the case of characteristic 0 in 1964. In characteristic $p$, the problem is solved up to dimension 3 (Abhyankar, Cossart-Piltant) and is open from dimension 4. This project states the problem in Lean 4, formalizes the theory that the problem rests on, and works on the open case in the open.

The site is https://singularity.tamnd.com.

## The repositories

| Repository | Content |
|---|---|
| singularity (this repository) | the map of the problem, the paper records, the lab specs, the trust records, the spec and the pages of the site |
| [singularity-lean](https://github.com/tamnd/singularity-lean) | the Lean package `Singularity`: the statements, the bridges, the library and the work on dimension 4 |
| [singularity-agent](https://github.com/tamnd/singularity-agent) | `sing`, the toolchain: it checks the map and the records, and it builds and checks the site |
| [singularity-handbook](https://github.com/tamnd/singularity-handbook) | The Singularity Handbook, a textbook for mathematicians, as PDF and EPUB |

## Status

No proof of the open case exists, in Lean or on paper. The site shows the status of each statement. A tool computes each status from the Lean build and the records. No status is written by hand.

The work goes in milestones. Each milestone has a tracking issue with the label `milestone`.

| Milestone | Goal | Release |
|---|---|---|
| S0 | statements, repositories and site | v0.1.0 |
| S1 | the char 0 base and the bridges | v0.2.0 |
| S2 | tier T1 and dimension 1 | v0.3.0 |
| S3 | the lab and the core invariants | v0.4.0 |
| S4 | surfaces | v0.5.0 |
| S5 | valuations and local uniformization | v0.6.0 |
| S6 | threefolds | v0.7.0 |
| S7 | the first research result | v0.8.0 |
| S8 | alterations and the full library | v0.9.0 |
| S9 | the open case | v1.0.0 |

## Layout

| Path | Content |
|---|---|
| `docs/spec/` | the design spec, documents 00 to 16 |
| `blueprint/nodes/` | the map: one YAML file for each statement or definition |
| `papers/` | one YAML record for each source of the corpus |
| `records/` | the records that tools write: trust, status, runs |
| `site/` | the pages of the site, in Markdown |
| `lab/` | the specs and the runs of the computation lab |
| `scripts/` | the style check and small helpers |

## Rules

1. The Lean build is the source of truth for status. A claim on the site or in the handbook comes from a record that a tool wrote.
2. A published theorem that is not proved in Lean yet is a named hypothesis, not an axiom.
3. No claim on the open case is made until the policy of spec 06.6 is met: two kernels, the fidelity battery and two outside experts.
4. The text follows ASD-STE100 technical English. Run `python3 scripts/style.py` before a pull request.

## Licences

The prose is CC BY-SA 4.0. The data and the scripts are Apache-2.0. The texts are in `LICENSES/`.
