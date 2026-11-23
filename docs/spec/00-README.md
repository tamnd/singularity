# Spec 2161: Singularity

Resolution of singularities in characteristic $p$, dimension $\ge 4$, in Lean, in public.

Written 2026-11-23. This is a research and design spec. Change of 2026-11-23: the Lean package moved from `tamnd/singularity` to its own repository, `tamnd/singularity-lean`. Where a document says `tamnd/singularity` for Lean code, read `tamnd/singularity-lean`.

## The project in one paragraph

Four repositories:
- `tamnd/singularity`: the map of nodes, the paper records, the lab specs, the trust records and the site sources;
- `tamnd/singularity-lean`: the Lean package `Singularity`;
- `tamnd/singularity-agent`: `sing`, the toolchain and the model roles;
- `tamnd/singularity-handbook`: a textbook for mathematicians, as PDF and EPUB.

Together they work toward one goal: prove `ResolutionDimFourCharP` in Lean. On the way they formalize the theory that the problem rests on (about 140 sources, document 07), and they publish everything at https://singularity.tamnd.com. The open case is a research bet. The library, the first formal proofs in dimensions 2 and 3, and the handbook are worth doing if the bet fails (document 02).

## What changed in 2026

1. **Char 0 resolution is in Lean twice.** `resolutionorg/hironaka` is Apache-2.0 and Lean v4.35.0, and has about 420,000 lines covering Hironaka, Kollár and Włodarczyk. riemann-lean (2026-11-20) has an independent proof. The project starts from the first and checks it against the second (document 05).
2. **There are statements to bridge to.**
   - google-deepmind/formal-conjectures stated the open problem in September 2026.
   - AxiomMath/Stacks (November 2026) has blowups, excellence and a model-written proof for excellent surfaces.
   - The project's statement is proved equivalent to each where they overlap (06.4).
3. **The obstructions are sharper.** New results show that:
   - Moh's stability theorem is false;
   - Nash blowups fail in dimension $\ge 4$ (Annals 2026);
   - weighted blowups fail for char 2 pinch points;
   - defect is the core obstruction of local uniformization.

   Three claimed general proofs exist (Hironaka 2017, Yi Hu, Tian 2026), and none is accepted (document 01).
4. **AI search on this exact problem has started.** Bérczi (February 2026) used AlphaEvolve to find ranking functions in dimension 4, char 3. The project's lab scales this up, with certificates checked in Lean (document 13).

## The documents

| Doc | Title | Read it for |
|---|---|---|
| [01](01-research-2026.md) | The state of the field, November 2026 | the sourced literature: status, claims, dimension 3, valuations, invariants, obstructions, Lean |
| [02](02-the-goal.md) | The goal | the levels of success G1 to G6, non-goals, what would show the plan is wrong |
| [03](03-the-problem.md) | The problem, mathematically | definitions, the char 0 proof, how char $p$ breaks, the core problems P1 and P2 |
| [04](04-routes.md) | The routes to dimension 4 | routes R1 to R9, their obstructions, first nodes and weights; Target T |
| [05](05-the-char-zero-base.md) | The characteristic 0 base | hironaka and riemann-lean: facts, statements, use, cross-check |
| [06](06-lean-statements.md) | The Lean statements and how to trust them | the statements, the fidelity battery F1 to F7, the bridges, the claim policy |
| [07](07-corpus.md) | The corpus | 142 rows of sources in tiers T0 to T8, the paper record, the first ten |
| [08](08-architecture.md) | Architecture | the repositories, the map, the flows |
| [09](09-singularity-repo.md) | `tamnd/singularity` | layout, Lean rules, toolchain pin, CI, upstreaming |
| [10](10-singularity-agent.md) | `tamnd/singularity-agent` | `sing`, the roles, the queue, budgets, evaluation |
| [11](11-singularity-handbook.md) | The handbook | volumes 0 to 9, the chapter format, `shb` |
| [12](12-site.md) | The site | pages, doors, rules, the Worker |
| [13](13-computation-lab.md) | The computation lab | tools, specs, experiments E1 to E9, certificates |
| [14](14-trust.md) | Trust | rows Q0 to Q8, the top theorems, threats, disclosure, registration |
| [15](15-milestones.md) | Milestones | S0 (2026-12-15) to S9, exit criteria, risks |
| [16](16-open-questions.md) | Open questions | Q-01 to Q-17, and the questions for experts |

**Reading order.**
- Mathematicians: 03, 04, 01, 06, 07.
- Engineers: 02, 05, 08, 09, 10, 14, 15.
- Everyone: 16.

## Decisions made in this spec

1. The main statement uses **regular**, not smooth, over **every field**, for reduced separated varieties, with density and an isomorphism over the regular locus (06.1). It is bridged to the perfect-field, integral, smooth form of formal-conjectures (06.4).
2. **hironaka is the base.** It is a Lake dependency at a pinned commit, with a fork for the `CharZero` split. riemann-lean is used only for a cross-check (05).
3. **The pin is Lean v4.35.0 with the Mathlib tag v4.35.0**, followed by monthly bumps (09.3).
4. **Hypotheses, not axioms.** A published theorem that is not yet proved is a named `Prop` with its own fidelity check (09.2).
5. **No claim on the open problem** is made until the policy of 06.6 is met: two kernels, the fidelity battery, and two outside experts.
6. **The lab produces data, not proofs.** A counterexample counts only as a Lean-checked certificate (13.4).
7. **The claimed proofs** are tested only by the cheap lab test E9. They are never used as hypotheses (01, 1.2).
8. **Style.** Text follows ASD-STE100: short sentences, no "we", no em or en dashes.

## The first four weeks (milestone S0, 2026-12-15)

1. Create the four repositories. Add hironaka as a pinned dependency and build it on a project machine.
2. Write `Singularity/Statements/` (06.1) and run F1 to F3.
3. Copy the site skeleton from riemann-agent. Deploy `/problem/`, `/map/` and `/trust/` to singularity.tamnd.com.
4. Send the letters to experts (Q-05) and to the author of riemann-lean (05.6). Register in Palomar (Q-13).
5. Start the `reader` role on the [S] and [U] items of 01, beginning with Moh 1987 and Hauser-Perlega 2019.
