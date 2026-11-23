# 06. The Lean statements and how to trust them

A Lean proof is worth as much as its statement. For an open problem this risk is the main one: a wrong statement can be easy to prove, and a wrong statement that is easy to prove looks exactly like a solved open problem. This document fixes the Lean form of every main statement of the project, and the battery of checks that each statement passes before any proof of it counts.

The statements live in one file per family, `Singularity/Statements/*.lean`, that imports only Mathlib and `Singularity/Statements/Basic.lean`. That file is small, has comments, and is the file that a referee reads. Each statement is a `def ... : Prop`. A proof is a separate `theorem` in another file. The statement files are pinned in `manifests/statements.sha256` and compared with `lake comparator` (09.6).

## 6.1 The vocabulary

All names are in the namespace `Singularity`. Where Mathlib or the char 0 base (document 05) has the notion, the statement uses it and does not redefine it.

```lean
import Mathlib

open AlgebraicGeometry CategoryTheory

universe u

namespace Singularity

/-- The points of `X` whose local ring is regular. -/
def regularLocus (X : Scheme.{u}) : Set X :=
  {x | IsRegularLocalRing (X.presheaf.stalk x)}

/-- `X` is regular: every local ring is a regular local ring. -/
def IsRegularScheme (X : Scheme.{u}) : Prop :=
  ∀ x : X, IsRegularLocalRing (X.presheaf.stalk x)

/-- `π : Y ⟶ X` is a resolution of singularities of `X` (Definition 3.1). -/
structure IsResolution {X Y : Scheme.{u}} (π : Y ⟶ X) : Prop where
  regular : IsRegularScheme Y
  proper : IsProper π
  isIso_over : ∃ U : X.Opens, (U : Set X) = regularLocus X ∧ IsIso (π ∣_ U)
  dense : Dense (π.base ⁻¹' regularLocus X)

/-- A variety over `k`, in the sense of the project: reduced, separated, of finite type. -/
class IsVariety {k : Type u} [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) : Prop where
  reduced : IsReduced X
  finiteType : LocallyOfFiniteType f
  quasiCompact : QuasiCompact f
  separated : IsSeparated f
```

`isIso_over` asks for the regular locus to be open and for `π` to be an isomorphism over it. Openness is a theorem for excellent schemes (Grothendieck, EGA IV 7.8.6), and the project proves it once for varieties over a field (target `regularLocus_isOpen`, tier T1 of document 07). It is in the statement on purpose: a reader sees the full claim without the theorem.

## 6.2 The main statements

```lean
/-- Resolution of singularities holds for varieties of dimension at most `n` in characteristic `p`. -/
def ResolutionInDim (p n : ℕ) : Prop :=
  ∀ (k : Type u) [Field k] [CharP k p] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsVariety X f],
    topologicalKrullDim X ≤ n → ∃ (Y : Scheme.{u}) (π : Y ⟶ X), IsResolution π

/-- The open problem: resolution in every dimension and every characteristic. -/
def ResolutionOfSingularities : Prop :=
  ∀ p n : ℕ, (p = 0 ∨ p.Prime) → ResolutionInDim.{u} p n

/-- The first open case. -/
def ResolutionDimFourCharP : Prop :=
  ∀ p : ℕ, p.Prime → ResolutionInDim.{u} p 4
```

The strong and embedded forms add a `BlowupSequence` (the structure of document 05, generalized to any field) with conditions on the centres:

```lean
/-- Strong resolution: a sequence of blowups with regular centres over the singular locus,
    whose total exceptional locus is a strict normal crossings divisor. -/
def StrongResolutionInDim (p n : ℕ) : Prop :=
  ∀ (k : Type u) [Field k] [CharP k p] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsVariety X f],
    topologicalKrullDim X ≤ n →
    ∃ s : BlowupSequence X,
      IsResolution s.topMap ∧ s.CentersOver (regularLocus X)ᶜ ∧ s.CentersRegular ∧
      IsStrictNormalCrossings (reducedPreimage s.topMap (singularLocusCloseds X))

/-- Embedded resolution of a closed subscheme of a regular scheme of dimension at most `n`. -/
def EmbeddedResolutionInDim (p n : ℕ) : Prop := ...

/-- Principalization of an ideal on a regular scheme with a normal crossings boundary. -/
def PrincipalizationInDim (p n : ℕ) : Prop := ...

/-- Local uniformization of every valuation of the function field of an integral variety. -/
def LocalUniformizationInDim (p n : ℕ) : Prop := ...

/-- The core problem P1 of 3.4: hypersurfaces `z^p + g(x_1, ..., x_n) = 0`. -/
def PurelyInseparableHypersurfaceResolution (p n : ℕ) : Prop := ...
```

The bodies of the elided statements follow the same pattern and are written in the S0 milestone (document 15). Each has a short docstring that gives the informal statement it means, with a reference.

### 6.2.1 The decisions in these statements

| Decision | Choice | Why |
|---|---|---|
| Regular or smooth | regular | over an imperfect field a regular variety can have no smooth model (3.3.6); for perfect `k` the project proves `IsRegularScheme Y ↔ Smooth (π ≫ f)` as a check |
| Proper or projective | proper in `IsResolution`; projective by blowups in `StrongResolutionInDim` | the weak form is the one with the least hypotheses; the strong form is what the methods give |
| Dimension | `topologicalKrullDim X ≤ n` | the dimension of the underlying space; equal to the Krull dimension of each affine piece for varieties, a check theorem |
| Field | any field with `CharP k p` | the theorem is about all fields; reduction to perfect or algebraically closed `k` is a theorem, not a hypothesis |
| Universe | `k`, `X` and `Y` in one universe `u` | as in both char 0 bases; a theorem that lowers or raises the universe is a check |
| Separated | required | standard; hironaka asks for it too (`[IsSeparated f]`), riemann-lean does not |
| Reduced or integral | reduced `X`, no condition on `Y` beyond regular | formal-conjectures and hironaka ask for integral `X` (and formal-conjectures for integral `Y` and `BirationalOver`); for reduced `X` the components are resolved one by one, and the bridges of 6.4 prove that the forms agree |
| Reduced | required | a non-reduced scheme has no regular modification that is an isomorphism over a dense open in the usual sense; the statement for `X_red` is the standard one |

## 6.3 The fidelity battery

A statement is *trusted* only after it passes every check below. The results are rows of `records/fidelity.json`, and the site shows them (document 12, page Trust).

| Check | What it does | Who does it |
|---|---|---|
| F1. Elaboration | the file builds with the pinned toolchain; `#print axioms` of each statement is empty | CI |
| F2. Positive instances | proofs of the statement for known cases: regular `X` with `π = 𝟙`; curves by normalization; a cusp and a node, by hand; the char 0 case from the base (6.4) | agent `stater` and people |
| F3. Negative instances | proofs that weaker or wrong variants are false: "smooth" in place of "regular" fails for a regular non-smooth curve over $\mathbb{F}_p(t)$; dropping `dense` makes the statement true with a trivial `Y`; dropping `isIso_over` lets an alteration count as a resolution (and de Jong's theorem is known); the check is a Lean proof that the disjoint union of two copies of a regular `X` satisfies the variant and is not an `IsResolution` of `X` | agent `refuter` |
| F4. Triviality attack | a strong prover gets a budget to prove the statement in a trivial way, for example with `Y = ∅` or by exploiting a universe or a definitional quirk; a success is a failed check | agent `refuter`, budget in 10.6 |
| F5. Round trip | an independent model translates the Lean statement to English with no access to the source docstring; a person compares the result with the docstring | agent `explainer` and people |
| F6. Human review | two algebraic geometers sign that the Lean statement means the docstring; the names and dates go into `records/fidelity.json` | people |
| F7. Pinning | the statement file hash is in `manifests/statements.sha256`; `lake comparator` matches each proof to the pinned statement | CI |

The statements of the open problem (`ResolutionDimFourCharP` and `ResolutionOfSingularities`) need all seven, and F6 with reviewers from at least two of the groups named in document 01 (for example a member of the Cossart-Piltant, Hauser, Villamayor or Temkin-Abramovich-Włodarczyk circles). They are frozen after F6. A change after F6 starts the battery again.

## 6.4 The bridges: to characteristic 0 and to the other statements

The first proof of the project is

```lean
theorem resolutionInDim_zero (n : ℕ) : ResolutionInDim.{u} 0 n
```

from `AlgebraicGeometry.exists_isBlowUpAlong_smooth` of the primary base (05.2), applied to each irreducible component with its reduced structure, and glued because the components of the regular locus are disjoint. It needs: over a field of char 0, smooth over `k` implies regular, and the smooth locus of `f` is the regular locus (the field is perfect). The cross-check package (05.6) proves the same theorem a second time from `FunctorialResolution.functorialResolutionCharZero` of riemann-lean.

In 2026 there are at least four public Lean statements of resolution of singularities. Each one is a test of the project's statement, because they were written by different people for different purposes:

| Statement | Where | Form | Bridge to prove |
|---|---|---|---|
| `Scheme.HasResolution`, `resolution_of_singularities` | google-deepmind/formal-conjectures, `FormalConjectures/Wikipedia/ResolutionOfSingularities.lean` | `X` integral, separated, of finite type over a **perfect** field `k` of char `p`; `Y` integral and smooth over `k`; `π` proper and `BirationalOver`; tagged research open | `ResolutionInDim p n` for perfect `k` and integral `X` ↔ the formal-conjectures statement restricted to dimension `n` |
| its solved variants | the same file: `_of_charZero`, `_of_topologicalKrullDim_le_three`, `exists_not_hasResolution_of_not_perfectField` | the last one says that over an imperfect field a smooth model need not exist, which is F3 of 6.3 | the project proves the last one again in its own terms, as the F3 instance |
| `exists_isBlowUpAlong_smooth`, `IsResolution` | resolutionorg/hironaka (05.2) | `X` integral, separated; `Y` smooth over `k`; a single blowup | `resolutionInDim_zero` above |
| `IsResolution` (Stacks tag 0BGK), `exists_isResolution_of_isExcellent_of_ringKrullDim_eq_two` | AxiomMath/Stacks, `StacksFrontier` (written by models, not reviewed) | Noetherian integral `X`; `Y` regular; proper and birational; for excellent surfaces | `resolutionInDim_two` from it, after review (Q-07 of document 16) |

The bridges are proved in `Singularity/Bridge/`, one file per external statement. Each external statement is copied word for word into the bridge file with its source commit, so that a change upstream shows up as a failed comparison and not as a silent change of meaning. The project's own statement keeps "regular" and works over every field, because that is the open problem as the experts state it (3.1). For perfect `k` the bridge to formal-conjectures shows that the two agree. Over an imperfect field the project's statement is the stronger one, and the solved variant `exists_not_hasResolution_of_not_perfectField` explains why formal-conjectures restricts to perfect fields.

## 6.5 Misformalization risks, ranked

1. **The wrong notion of regular.** If `IsRegularLocalRing` in Mathlib or in the project had a wrong definition (for example the dimension of $\mathfrak{m}/\mathfrak{m}^2$ compared with the wrong dimension), every statement would change meaning. Check: prove the standard equivalences (regular iff the associated graded ring is a polynomial ring; regular implies domain; a localization of a regular ring at a prime is regular) as part of F2.
2. **Dimension conventions.** `topologicalKrullDim` takes values in `WithBot ℕ∞`; the empty scheme has dimension $\bot$. Check: dimension of $\mathbb{A}^n_k$ and of a hypersurface in it.
3. **The blowup.** A blowup defined by a universal property in the category of all schemes must exist and must agree with $\operatorname{Proj} \bigoplus I^n$. The base proves existence. Check: the charts of the blowup of $\mathbb{A}^2$ at the origin.
4. **Normal crossings.** The bases have strict and simple forms (riemann-lean `IsStrictNormalCrossings`, `HasSimpleNormalCrossings`; hironaka `IsSncDivisor`). Check: an equivalence on regular schemes over a perfect field, and a counterexample to their equivalence in general.
5. **Universe and size quirks.** A statement over `Type u` that is proved for `u = 0` only. Check: the theorems are universe polymorphic and `#check @theorem.{1}` works.
6. **Functoriality.** riemann-lean's `IsPullbackSequence` drops empty steps, and hironaka's `BlowUpSequence` has its own pullback. Check: the pullback of a blowup sequence along an open immersion is one in both senses.
7. **Local definitions of the base.** hironaka defines `FiniteType`, `IsRegularAt` and `IsResolution` itself. Check: each agrees with the Mathlib notion (`LocallyOfFiniteType` with `QuasiCompact`, `IsRegularLocalRing` of the stalk).

## 6.6 Claims

The project never states in its README, on the site or in a release note that it has proved an open case unless: the proof builds; the axioms are the three standard ones; two kernels accept it; the statement passed F1 to F7; and at least two experts not paid by the project have read the written proof in the handbook. Before that, the status is "a Lean proof that has passed the checks C1 to Cn", and the site says which ones (document 14).
