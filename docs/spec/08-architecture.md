# 08. Architecture

The project has four repositories and one site. It follows the shape of the riemann project (`tamnd/riemann`, `tamnd/riemann-lean`, `tamnd/riemann-agent`, `tamnd/riemann-handbook`). The Lean package is in `tamnd/singularity-lean`. The map, the records and the pages are in `tamnd/singularity`.

## 8.1 The repositories

| Repository | Holds | Language | Licence |
|---|---|---|---|
| `tamnd/singularity` | the blueprint (the map of statements and their dependencies); the paper records; the trust and fidelity records; the pages of the site; the deploy workflow | Markdown, YAML, JSON | prose CC BY-SA 4.0; data Apache-2.0 |
| `tamnd/singularity-lean` | the Lean package `Singularity` | Lean 4 | Apache-2.0 (as Mathlib) |
| `tamnd/singularity-agent` | `sing`, the toolchain: index the Lean code, check the trust rows, run the agent roles, run the computations, build and check the site | Go | MIT, as riemann-agent |
| `tamnd/singularity-handbook` | The Singularity Handbook: the mathematics, written as a textbook by and for mathematicians, as PDF and EPUB volumes; `shb`, the builder | Markdown, LaTeX, Python | prose CC BY-SA 4.0; builder MIT |

The site is https://singularity.tamnd.com. `sing site build` writes it from `tamnd/singularity` and from the release files of the handbook. The workflow `deploy` of `tamnd/singularity` deploys it to the Cloudflare Worker `singularity`, which serves static files only (the same `wrangler.jsonc` shape as riemann, document 12).

The char 0 base is `resolutionorg/hironaka` (Apache-2.0), a Lake dependency of `tamnd/singularity` at a pinned commit (document 05). A fork, `tamnd/hironaka`, holds the changes that weaken `CharZero` (05.5, step 5), one branch per change, offered upstream. A small package `singularity-crosscheck`, in `tamnd/singularity/crosscheck/`, depends on a pinned commit of riemann-lean for the second proof of 05.6 and is not imported by `Singularity`.

## 8.2 The boxes

```
                 literature (arXiv, journals, books)
                          │ ingest (sing paper add)
                          ▼
 ┌───────────────── tamnd/singularity ─────────────────────────────┐
 │  papers/   ──►  blueprint/  ◄──►  Singularity/ (Lean)            │
 │  (records)      (the map:          Statements/  Base/  Algebra/   │
 │                 nodes + edges)     Valuation/  Blowup/  ...       │
 │      ▲               ▲   │                 │                      │
 │      │               │   ▼                 ▼  lake build, CI      │
 │  records/  ◄─────────┴── sing index / sing trust / sing fidelity  │
 │  (trust, fidelity, status, runs)                                  │
 │  site/ (pages)                                                    │
 └──────┬────────────────────────▲───────────────────────────────────┘
        │ sing site build         │ pull requests from agent roles
        ▼                         │
 singularity.tamnd.com    tamnd/singularity-agent (sing: roles, lab, site)
        ▲                         │
        │ release files           ▼
 tamnd/singularity-handbook ◄── chapters (writer role + people)
```

## 8.3 The central object: the map

The *map* is a directed acyclic graph. Its nodes are mathematical statements and definitions; its edges are "uses". It is the blueprint of the project, and every other part reads it.

A node is one YAML file in `blueprint/nodes/`, named by a stable tag (`SG` followed by 8 characters of base 32, as Math 2.0 tags):

```yaml
tag: SG3KQ7M2PA
kind: theorem            # definition | theorem | lemma | conjecture | example | counterexample
title: Moh's bound on the increase of the residual order
statement: |
  Let $f = z^{p^e} + g$ ... Then after a permissible blowup the residual order increases by at most $p^{e-1}$.
sources:
  - paper: moh1987stability
    loc: "Theorem 1"
uses: [SG7Y2N0QBE, SGM4T9X1CD]
lean:
  statement: Singularity.Residual.moh_bound
  proof: Singularity.Residual.moh_bound   # absent while open
tier: T4
route: [R1, R5]
status: computed       # never written by hand; see below
math2: RZ66X0NAM5      # the Math 2.0 node, when there is one
```

The status is computed by `sing index` from the Lean environment and the records, never written by hand:

| Status | Meaning |
|---|---|
| `stated` | the Lean statement exists and builds |
| `faithful` | the statement passed the fidelity battery (06.3) for its level |
| `proved` | a Lean proof exists, depends on the three standard axioms only, and every node it uses is `proved` |
| `proved-mod` | a Lean proof exists that takes named nodes as hypotheses (for example a published theorem that is not yet formalized); the site lists them |
| `open` | the statement is an open problem; no proof is claimed |
| `refuted` | a Lean proof of the negation exists |

This is the pattern of the Lean blueprints (Massot's `leanblueprint`, used for FLT and for many 2024 to 2026 projects) and of the "DAG of pinned statements" that the large AI formalizations of 2026 used (document 01). The differences: the nodes are data, not LaTeX; the status is computed; and the map includes the open problem and the research routes, so it is also the plan.

## 8.4 The four flows

1. **Ingest.** `sing paper add <arXiv id | DOI>` writes `papers/<key>.yaml` with metadata, the licence class, and a list of the numbered results of the paper. The `reader` role (document 10) proposes a node for each result that the project needs, with its uses. A person accepts or edits.
2. **Formalize.** The `stater` role writes the Lean statement of a node; the fidelity battery runs; the `prover` role works on the proof; `sing index` computes the status. Each step is a pull request to `tamnd/singularity`, built by CI.
3. **Explore.** The `explorer` and `refuter` roles run computations in the lab (document 13): invariants of examples, searches for counterexamples, tests of conjectured inequalities. A result is a `lab/runs/<id>/` record and, when it matters, a new node of kind `example`, `counterexample` or `conjecture`.
4. **Explain.** The `writer` role and people write the handbook chapters from the map and the Lean code. The `explainer` role writes docstrings and the L2 text of each node on the site.

## 8.5 Cross-cutting decisions

- **Lean is the source of truth for status.** No status, count or claim on the site or in the handbook is written by hand. Each comes from a record that a tool wrote (the rule of riemann).
- **Pinned everything.** Lean and Mathlib are pinned in `lean-toolchain` and `lake-manifest.json`. The char 0 base is pinned by commit. Each paper record pins the version it read (arXiv version number).
- **One writing style.** Plain technical English (ASD-STE100), no em dash and no en dash, no "we" in the content of the site and the handbook, math in `$...$`. The style script of riemann is reused. In the handbook, names of theorems with several authors use a hyphen (Cossart-Piltant), as in the riemann handbook.
- **People decide.** The agent proposes pull requests. A person merges. Statements of the open problems and their changes need two people (06.3, F6).
- **Budgets are explicit.** Every model call is in a ledger with its cost, under a daily and a per-run budget in `agent.yaml` (riemann-agent's rule: no file, no budget, no calls).
