# 05. The characteristic 0 base

The project does not start from zero. In 2026, two independent Lean formalizations of resolution of singularities in characteristic 0 were published:

| | `resolutionorg/hironaka` | riemann-lean, `Development/ResolutionOfSingularities` |
|---|---|---|
| Authors | Claude agents operated by Resolution (Chris Elliott, Billy Snikkers, Adam Newgas) | Levent Alpöge (release of 2026-11-20), mirrored in `tamnd/riemann-lean` at `9110120c` |
| Published | created 2026-09-30, last push 2026-10-20 (commit `044d89c9`) | 2026-11-20 |
| Licence | **Apache-2.0** | **none**; copyright stays with the author (`NOTICE.md`) |
| Toolchain | Lean `v4.35.0`, Mathlib tag `v4.35.0` | Lean `v4.33.1`, Mathlib `0df444a3` |
| Size | 1,732 Lean files (about 420,000 lines), algebraic and analytic | 499 files, about 140,300 lines, algebraic only |
| `sorry` | none | none |
| Statement check | `Challenge/` files, `comparator.json`, comparator CI, `scripts/check_axioms.lean` | `Statements.lean` only |
| Documentation | docstrings with a `Source statement:` line, blueprint, API docs, `formalization.yaml`, `references.bib` | no comments |
| Method | order reduction after Włodarczyk 2005 and Kollár 2007, re-run on analytic manifolds | Kollár 2007 (tuned ideals, D-balanced ideals, going-up invariant) |

**Decision (settles Q-01 of document 16 in principle):** `resolutionorg/hironaka` is the **primary base**, because it has a licence, a current toolchain, docstrings and a comparator setup. riemann-lean is the **second base**. The project does not copy it. It uses it for one cross-check theorem (5.6), which needs no licence because the project only states and checks a bridge against a fetched dependency and does not redistribute the code. The rest of this document is about the primary base unless it says otherwise.

## 5.1 The facts of the primary base

Measured on 2026-11-23 with `gh api` on the default branch.

| Fact | Value |
|---|---|
| Libraries | `Hironaka` (the proofs), `HironakaExamples` (worked examples of the sources, imported by nothing in `Hironaka`), `Challenge` (the main statements with `sorry`, which import only the `Defs.lean` files) |
| `Hironaka/Scheme/` | 72 files for `BlowUp`, 66 for `BlowUpSequence`, 42 for `Smooth`, 39 for `Snc`, 31 for `IdealSheaf`, 9 for `ProjectiveBundle`, plus `FiniteType`, `ReducedEquidimensional`, `DisjointIntegralComponents`, `Resolution` |
| `Hironaka/Algebra/` | 77 files for `Local`, 16 for `RegularSmooth`, plus `Derivative`, `Smooth`, `SymmetricAlgebra`, `Proj` |
| `Hironaka/Resolution/Algebraic/` | 412 files: `Wlo05` 111, `Kol07` 105, `MaximalContact` 32, `Monomial` 31, `MarkedOrderReduction` 31, `OrderReduction` 25, `Stage` 19, `BoundaryClearing` 17, `Hir64` 15, `Snc` 12 |
| `Hironaka/Resolution/Analytic/` and the manifold and analytic space folders | about 700 files (not needed by this project, except as a model) |
| Axioms | `propext`, `Classical.choice`, `Quot.sound`, checked by the comparator and by `scripts/check_axioms.lean` |
| Second kernel | the comparator workflow exists; the `nanoda` replay is disabled in its CI at the commit above |

The `Scheme/` and `Algebra/` folders (382 files) are where the characteristic-free foundations are: blowups, blowup sequences, simple normal crossings, ideal sheaves, regular and smooth local rings. That count is an upper bound. Some of those files assume char 0, and step 5 of 5.5 measures how many.

## 5.2 The top statements

The challenge files state the main theorems against the `Defs.lean` vocabulary only. `Challenge/Standard.lean` imports only Mathlib and restates the two definitions it needs:

```lean
def Scheme.IdealSheafData.IsEffectiveCartier {X : Scheme.{u}} (J : X.IdealSheafData) : Prop :=
  ∀ x : X, ∃ U : X.affineOpens, x ∈ U.1 ∧
    ∃ g ∈ nonZeroDivisors Γ(X, U), J.ideal U = Ideal.span {g}

def Scheme.Hom.IsBlowUpAlong {X B : Scheme.{u}} (π : B ⟶ X) (I : X.IdealSheafData) : Prop :=
  (I.comap π).IsEffectiveCartier ∧
    ∀ {Y : Scheme.{u}} (f : Y ⟶ X), (I.comap f).IsEffectiveCartier → ∃! g : Y ⟶ B, g ≫ π = f

theorem exists_isBlowUpAlong_smooth {k : Type u} [Field k] [CharZero k]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] [QuasiCompact f]
    [IsSeparated f] [IsIntegral X] :
    ∃ (X' : Scheme.{u}) (π : X' ⟶ X) (I : X.IdealSheafData),
      π.IsBlowUpAlong I ∧ (I.support : Set X) = (f.smoothLocus : Set X)ᶜ ∧
      Smooth (π ≫ f) ∧ IsProper π ∧ IsIso (π ∣_ f.smoothLocus)
```

The other algebraic main theorems, from `comparator.json`:

| Source | Lean name |
|---|---|
| Hironaka 1964, Main Theorem I | `exists_support_eq_singularLocus_isRegular_blowUp`, and its weak form `exists_dense_isIso_restrict_isRegular_blowUp` |
| Hironaka 1964, Main Theorem II (order reduction) and II(N) (principalization) | `exists_blowUpSequence_ord_weakTransformSeq_lt`, `exists_blowUpSequence_weakTransformSeq_eq_top` |
| Hironaka 1964, Corollaries 1 and 3 | `exists_blowUpSequence_forall_exists_stalkIdeal_weakTransformSeq_eq_top`, `exists_blowUpSequence_isInvertible_isSncBoundary_radical_comap` |
| Kollár 2007, Theorems 27, 35, 36 | `exists_strong_resolution`, `exists_functorial_principalization`, `exists_functorial_resolution` |
| Włodarczyk 2005, Theorem 1.0.2 | `exists_functorial_embeddedDesingularization` |

The statements use `IsRegularAt` and `IsResolution` from `Hironaka/Scheme/Defs.lean`, and a local `FiniteType` class. Two of their choices matter for this project:

1. **"Non-singular" is read as `Smooth (π ≫ f)`.** Over a field of char 0 this is the same as regular (Stacks 00TV). In char p over an imperfect field it is not (3.3.6). So the char p statement of the project (06.1) uses regularity and must have a bridge lemma "regular and of finite type over a perfect field implies smooth" before it can use any base theorem in char p. That lemma is in Mathlib's reach and is node T1 of document 07.
2. **`[IsIntegral X]` and `[IsSeparated f]`.** The base resolves integral separated schemes. The project's `IsVariety` (06.1) asks for reduced and separated. The bridge of 5.6 passes from integral to reduced through the finitely many irreducible components, with `DisjointIntegralComponents.lean` of the base as the model.

## 5.3 How the proof is built

The algebraic proof follows Włodarczyk's 2005 paper and Kollár's book. The marked ideal $(I, b)$ is reduced by order reduction (`OrderReduction`, `MarkedOrderReduction`), through maximal contact (`MaximalContact`) and the coefficient ideal, with the boundary cleared (`BoundaryClearing`) and the monomial case at the end (`Monomial`). The functorial forms (`Kol07`, `Wlo05`) add independence of the choices and descent.

The steps that use char 0 are the ones of 3.2: the derivative lowers the order by exactly one, and a hypersurface of maximal contact exists. Everything that only handles blowups, sequences of blowups, normal crossings and the combinatorics of the monomial case does not use char 0. The second base has the same split. It states the key lemma in a form that is weaker than char 0:

```lean
theorem idealOrder_derivIdeal_of_isUnit_natCast ... (hunit : ∀ n : ℕ, 1 ≤ n → IsUnit ((n : ℕ) : R))
    {I : Ideal R} {r : ℕ} (hr : 1 ≤ r) (hI : idealOrder I = (r : ℕ∞)) :
    idealOrder (derivIdeal k I) = ((r - 1 : ℕ) : ℕ∞)
```

In riemann-lean about 150 of the 499 files use `CharZero`, and 23 carry the hypothesis in this `IsUnit` form. The same count for the primary base is step 5 of 5.5.

## 5.4 What the project takes from it

1. **Blowups** (`Scheme/BlowUp`, `Scheme/ProjectiveBundle`, `Algebra/Proj`): the universal property, existence, properness, the charts, the isomorphism off the centre, strict and weak transforms. Characteristic free. Every route needs them.
2. **Blowup sequences** (`Scheme/BlowUpSequence`): towers, pullbacks, composition. Characteristic free.
3. **Simple normal crossings** (`Scheme/Snc`, `Resolution/Algebraic/Snc`): characteristic free.
4. **Regular and smooth local rings** (`Algebra/Local`, `Algebra/RegularSmooth`): some files are characteristic free, and some depend on perfect or char 0 base fields. Step 5 sorts them.
5. **The monomial case** (`Resolution/Algebraic/Monomial`): characteristic free in substance, and the end of every char p strategy.
6. **Char 0 resolution itself**, as a black box for the parts of char p arguments that pass through char 0 (the generic fibre in mixed characteristic, route R8 of document 04), and as the model for the statement and the documentation style of the project.

The derivative-based part (maximal contact, coefficient ideals, order reduction) is the template that a char p proof must replace. The `IsUnit` form gives one result to test early: **principalization of marked ideals $(I, b)$ with $b < p$** should follow from the same proof with `CharZero` weakened to "$n$ is a unit for $n \le b$", if the coefficient ideals that the proof builds keep their orders below $p$. They do not in general (3.3.3), so the exact range is a question for milestone S1. It is not a resolution theorem in char p, but it is a good first test of how well the code separates its uses of char 0.

## 5.5 Use of the primary base

1. **Depend, do not copy.** `tamnd/singularity` requires `hironaka` through Lake at a pinned commit and records it in `manifests/base.yaml`. Because the licence is Apache-2.0, the project may copy and change files later. It does that only for files it must change (step 5), keeps the copyright header, adds a `Modified by` line, and lists them in `NOTICE`.
2. **Match the toolchain.** The project pins Lean `v4.35.0` and the Mathlib tag `v4.35.0` at the start, the same as the base and as AxiomMath/Stacks (document 07.5). It bumps both together, after the base bumps or by a fork when the project needs a newer Mathlib (09.3).
3. **Check what the base claims.** Run its comparator with `comparator.json` and `scripts/check_axioms.lean` on a machine of the project, turn the disabled `nanoda` replay back on, and replay in `lean4lean`. The results go to `records/trust.json` (rows Q1 to Q4 of document 14, for the base theorems).
4. **Check that the statements are faithful.** Run the battery F1 to F7 of 06.3 on `exists_isBlowUpAlong_smooth`, `exists_strong_resolution` and `exists_functorial_principalization`. Since the base defines its own `IsRegularAt`, `IsResolution` and `FiniteType`, the battery includes a lemma that each one agrees with the Mathlib notion, where Mathlib has one.
5. **Map the char 0 boundary.** For every file of `Scheme/`, `Algebra/` and `Resolution/Algebraic/`, record whether it uses `CharZero` directly or through its imports, with `#print axioms`-style dependency walks for the instance. The output is `records/base-charzero.json` and a page on the site. Then, file by file, replace `CharZero` by the weakest hypothesis that each lemma needs, in a fork `tamnd/hironaka` with one branch per change, and offer the changes upstream.
6. **Document the boundary.** The handbook volume on char 0 (Volume 2 of document 11) explains the proof as Kollár's book does, with `Lean:` lines into the base, and marks each step as "char free", "needs $n!$ to be a unit for $n \le N$" or "needs char 0".

## 5.6 The second base, and the cross-check

The riemann-lean development is a second, independent proof of the same theorem. It was made by another team, with another method, in another style. Two independent proofs of statements that the project can show to be equivalent give a strong check on the faithfulness of both.

- **The cross-check theorem.** In a separate package `singularity-crosscheck` (not imported by `Singularity`), prove that `FunctorialResolutionCharZero` of riemann-lean implies the project's `ResolutionInDim 0 n` for every $n$, and that `exists_isBlowUpAlong_smooth` of hironaka implies it too. These are two short bridge proofs to one target. If either fails, there is a difference of meaning to explain (06.3, F2).
- **Licence.** The package fetches riemann-lean at a pinned commit and redistributes nothing from it. The project still writes to the author and asks for a licence, because a licence would let the project use the riemann-lean lemmas that hironaka lacks (for example the `IsUnit` form of the derivative lemma). Until an answer comes, nothing of it is copied into a licensed repository.
- **Toolchain.** riemann-lean is at `v4.33.1`, two minor versions behind. The cross-check package has its own pin and is built only in the weekly trust run.
- **Other parts.** riemann-lean also has developments on regular local rings, étale cohomology, discrete valuation rings and curves. The project reads them as references only.
