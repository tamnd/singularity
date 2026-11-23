# 09. tamnd/singularity: the Lean package and the content

## 9.1 Layout

```
singularity/
├── README.md  CHANGELOG.md  CONTRIBUTING.md  CITATION.cff  LICENSES/
├── lakefile.toml  lean-toolchain  lake-manifest.json
├── Singularity.lean                 # imports every proved module
├── Singularity/
│   ├── Statements/                  # the pinned statements (06); comments; Mathlib + Basic only
│   │   ├── Basic.lean               # regularLocus, IsResolution, IsVariety, BlowupSequence, SNC
│   │   ├── Resolution.lean          # ResolutionInDim, Strong..., Embedded..., Principalization...
│   │   ├── LocalUniformization.lean
│   │   ├── Alterations.lean
│   │   └── Core.lean                # P1, P2 and the route-specific open statements (04)
│   ├── Base/                        # the char 0 base, extracted or re-exported (05)
│   ├── Algebra/                     # tier T1: commutative algebra not in Mathlib
│   │   ├── Excellent/  RegularRings/  HilbertSamuel/  Differential/  PBasis/  Frobenius/
│   ├── Valuation/                   # tier T2: Zariski-Riemann, Abhyankar inequality, key polynomials, defect
│   ├── Geometry/                    # tier T1: normalization, regular locus, dimension, blowup comparisons
│   ├── Combinatorics/               # tier T3: Newton and characteristic polyhedra, fans, monomial ideals
│   ├── Invariants/                  # tier T4: order, residual order, Moh, kangaroo, idealistic exponents
│   ├── Curves/  Surfaces/  Threefolds/   # tier T5: the known theorems in dim 1, 2, 3
│   ├── LocalUniformization/         # tier T6
│   ├── Alterations/                 # tier T7
│   ├── Routes/                      # tier T8: one folder per route of document 04
│   │   ├── R1Polyhedra/  R2Valuative/  R3IFP/  ...
│   ├── Examples/                    # worked examples and counterexamples, each a node
│   └── Bridge/                      # statements of the project ↔ the base and Mathlib
├── Singularity/WIP/                 # work with sorry; not imported by Singularity.lean
├── blueprint/
│   ├── nodes/*.yaml                 # the map (08.3)
│   ├── routes.yaml                  # the routes of 04 and their nodes
│   └── tiers.yaml                   # the tiers of 07
├── papers/*.yaml                    # one record per paper (07.4)
├── lab/                             # computation specs and run records (13)
├── records/                         # written by sing; never edited by hand
│   ├── status.json  trust.json  fidelity.json  axioms.json  index.json  runs.jsonl
├── manifests/
│   ├── base.yaml                    # the pin of the char 0 base and its licence state
│   └── statements.sha256
├── site/                            # pages that are not generated: home, about, trust, routes, learn
├── scripts/style.sh
├── agent.yaml                       # budget and models for sing (10.6); no file, no calls
├── wrangler.jsonc
└── .github/workflows/  check.yml  build.yml  deploy.yml  bump.yml
```

## 9.2 Rules for the Lean code

1. **No `sorry` in the main tree.** `Singularity.lean` imports everything outside `WIP/`, and CI fails on `sorry`, `admit`, a new `axiom`, `native_decide`, `implemented_by` and `@[extern]` there. A node with an unfinished proof keeps its proof in `WIP/` and has status `stated`.
2. **Hypotheses, not axioms.** A published theorem that is not yet formalized enters as a named `def ... : Prop` in `Statements/` and as a hypothesis of the theorems that use it, never as an `axiom`. The status of those theorems is `proved-mod` (08.3), and the site lists the hypotheses. This is the pattern of the riemann-lean release, whose top theorems take `ResolutionCharZero` and others in this form.
3. **Statement files are small and commented.** Everything else may be long, but a statement file has a docstring for each definition and each statement, with the informal statement and a reference.
4. **Mathlib style, Mathlib names.** The code follows the Mathlib naming and style guide, so that parts can go upstream (9.5).
5. **The weakest hypothesis.** In the char-free tiers, a lemma takes `IsUnit (n : R)` or `CharP R p` or nothing, never `CharZero` when it does not need it (05.5, step 5).

## 9.3 The toolchain pin

The primary base (`resolutionorg/hironaka`) and AxiomMath/Stacks build with Lean `v4.35.0` and the Mathlib tag `v4.35.0`. The project starts on exactly this pin, so both build without change. Lean `v4.36.0` is the current stable release (`v4.37.0-rc1` is on master), so the first bump is to `v4.36.0`, after the base moves or in the fork `tamnd/hironaka`. The cross-check package (05.6) keeps its own pin, `v4.33.1` with Mathlib `0df444a3`, the pin of riemann-lean. After that, the pin moves once a month, with the `bump` workflow: it opens a pull request with the new `lake-manifest.json`, the `porter` role fixes what breaks, and a person merges. This is the monthly bump of the Math 2.0 spec (2148, document 07).

## 9.4 CI

| Workflow | When | What |
|---|---|---|
| `check` | each pull request and push | the style script; the forbidden words scan (9.2.1); `zizmor` on the workflows |
| `build` | each pull request and push | `lake exe cache get`, `lake build`, `sing index`, `sing trust -quick` (axioms of the changed top theorems); the job uploads `records/` as an artifact |
| `deploy` | push to `main`, daily, by hand | `sing site build`, `sing site check`, `wrangler deploy`; a pull request builds and checks the site but does not deploy |
| `bump` | monthly, by hand | the toolchain bump of 9.3 |
| `trust` | weekly, by hand | the full trust run: `lake build`, `lake check`, `#print axioms` and a constant walk for every `proved` node, replay in `lean4checker --fresh`, `lake comparator --paranoid` for the pinned statements (which replays in the independent checkers lean4lean and nanoda), the cross-check package of 05.6 (document 14) |

The actions are pinned by commit hash, as in riemann.

## 9.5 Upstream

Tiers T1 to T3 (document 07) are mostly general commutative algebra and scheme theory that Mathlib does not have yet (excellent rings, Hilbert-Samuel functions, normalization of schemes, Zariski-Riemann spaces). The project writes them in Mathlib style and sends them upstream when they are stable, with the authors listed. Upstreaming is slow (Mathlib had about 2,700 open pull requests in October 2026, document 01), so the project never waits for it: a module stays in `Singularity/` until Mathlib has it, and then becomes a thin file of aliases.

## 9.6 The trusted statements

`manifests/statements.sha256` has the SHA-256 of each file in `Singularity/Statements/`. A change to one of those files fails CI unless the same pull request changes the manifest and has the label `statement-change`, which needs two approvals. `lake comparator` (in the trust workflow) checks that each top theorem has exactly the type of its pinned statement.
