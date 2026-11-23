# 14. Trust

The project will produce a large amount of Lean code, much of it written by models. The claims it makes must survive a hostile referee. This document is the trust report that the site shows (`/trust/`), in the form of riemann's: a list of questions, how each one is checked, and the current answer. The answer of each row is one of **yes**, **no**, **open** (a person must decide), **not run**.

## 14.1 The questions

| Row | Question | Check | Where |
|---|---|---|---|
| Q0 | Is the source the one that the site describes? | the site build records the commit of `tamnd/singularity` and the pin of the base; `sing site check` refuses a mismatch | CI |
| Q1 | Does it build? | `lake build` of `Singularity` at the pinned toolchain, from a clean cache, on a machine of the project | `trust` workflow |
| Q2 | Which axioms do the top theorems use? | `#print axioms` and the constant walk of `rh trust`, for each `proved` node; each must be `propext`, `Classical.choice`, `Quot.sound` only | `trust` workflow |
| Q3 | Does a second kernel accept it? | `lean4checker --fresh` on the modules of the top theorems, and `lake comparator --paranoid`, which replays the export in the independent checkers (lean4lean, nanoda) | `trust` workflow, weekly |
| Q4 | Do the proved theorems have the pinned statements? | `lake comparator` against `Singularity/Statements/`, with `lake check` for the package; the same for the base with its own `comparator.json` | `trust` workflow |
| Q5 | Do the statements mean what the docstrings say? | the fidelity battery of 06.3 | `records/fidelity.json` |
| Q6 | Which published theorems are still hypotheses? | the list of `proved-mod` hypotheses (09.2.2) used by each top theorem | `records/status.json` |
| Q7 | Has a person read the proof? | the handbook sections of the top theorems at status `reviewed`, with names | handbook |
| Q8 | Has someone outside the project reproduced Q1 to Q4? | a link to an independent run | by hand |

Q0 to Q4 are mechanical and run on every release. Q5 to Q8 need people. The site shows all nine, for each top theorem separately, and the home page shows the row of the open problem.

## 14.2 The top theorems

The trust report covers these theorems (more are added as the map grows):

| Theorem | Meaning |
|---|---|
| `Singularity.resolutionInDim_zero` | char 0, every dimension (the bridge of 06.4), proved from hironaka and again from riemann-lean (05.6) |
| `Singularity.resolutionInDim_one` | every char, dimension 1 |
| `Singularity.resolutionInDim_two` | every char, dimension 2 (Lipman) |
| `Singularity.embeddedResolution_surfaces` | embedded surfaces (Abhyankar, Cossart-Jannsen-Saito) |
| `Singularity.resolutionInDim_three` | every char, dimension 3 (Cossart-Piltant) |
| `Singularity.alteration` | de Jong's theorem |
| `Singularity.localUniformization_abhyankar` | Knaf-Kuhlmann |
| `Singularity.inseparableLocalUniformization` | Temkin |
| the nodes of `ResolutionDimFourCharP` and of P1 | the open problem and the core case |

## 14.3 Threats and answers

| Threat | Answer |
|---|---|
| A wrong statement that is easy to prove | the fidelity battery, F4 in particular, and the freeze of 06.3 |
| A kernel bug used by a generated proof (the "Summer of Soundness Bugs" of July and August 2026, document 01) | Q3 with two independent kernels; a pinned toolchain that has the fixes; the scan of 09.2.1 for escape hatches; a weekly replay |
| A hidden axiom in a dependency | the constant walk of Q2 covers the base and Mathlib, not only the project |
| A change to a statement in a large pull request | the hash manifest of 09.6 and the `statement-change` label |
| A hypothesis that is never discharged and is false | each `proved-mod` hypothesis is a named statement with its own fidelity check and a source; a false published theorem is a real risk in this field (some claimed proofs were withdrawn), so each hypothesis lists the expert status of its source |
| A generated proof that nobody understands | Q7; the handbook is part of the trust, not decoration |
| Prompt injection from a paper | 10.7 |
| A model that reports success it did not reach | the role checks of 10.3 are run by `sing`, not by the model; the run record has the build log |

## 14.4 Disclosure

Every merged pull request that a role wrote has the role, the model and the run id in its body and as a commit trailer. Every handbook section names its drafter and its reviewers. The README and the site say plainly that much of the code and the text is written by models and checked by Lean and by people, and which checks a given result has passed. This follows the norms that the field wrote down in 2025 and 2026 (document 01: disclose how a result was made, keep it independently checkable, keep people responsible).

## 14.5 Registration

The project publishes a `formalization.yaml` at the root of `tamnd/singularity`, in the schema of the Mathlib Initiative that hironaka uses (version `v0.4`), with each source, its relationship (`formalizes`, `uses`, `states`) and its author endorsement state, and registers the main statements in the Palomar registry. The trust rows of each registered statement link to the site. The statements that the project takes from other projects (06.4) are listed there with their source commit.
