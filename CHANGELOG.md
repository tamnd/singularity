# Changelog

Each release has a section. The newest release is first.

## Unreleased

## 0.2.4 - 2026-11-24

- The node SG0000002B (the normal locus of a domain with a finite normalization) with its Lean proof.
- The node SG0000002C (integral curves have a resolution in each characteristic) with its Lean proof `Singularity.Curves.integralResolutionInDim_one`. The resolution is the normalization. The node SG0000001A uses SG0000002C and SG0000001Y. Its status stays stated, because the general case needs the reduction to integral varieties.
- `records/lean.json` from tamnd/singularity-lean at 4ab4320, with the files `Singularity/Algebra/NormalLocus.lean` and `Singularity/Curves/Resolution.lean`. It has 109 declarations, and each uses only the three standard axioms.
- The release v0.2.4 of tamnd/singularity-lean.

## 0.2.3 - 2026-11-24

- The papers Eis95 (Eisenbud, Commutative Algebra with a View Toward Algebraic Geometry) and Lan02 (Lang, Algebra).
- The nodes SG00000028 (the integral closure of a polynomial ring in a purely inseparable extension is finite), SG00000029 (the integral closure of a polynomial ring in each finite extension is finite) and SG0000002A (the normalization of an affine curve over each field is a Dedekind domain), each with its Lean proof.
- The node SG0000000M (finiteness of normalization, the theorem of E. Noether) now has a precise statement and its Lean proof `Singularity.Algebra.finite_integralClosure`. Before this change its Lean name was a placeholder that did not exist.
- `records/lean.json` from tamnd/singularity-lean at 1ef1ad1, with the file `Singularity/Algebra/NormalizationCharP.lean`. It has 92 declarations, and each uses only the three standard axioms.
- The release v0.2.3 of tamnd/singularity-lean.

## 0.2.2 - 2026-11-24

- The nodes SG00000024 (normal schemes of dimension at most 1 are regular), SG00000025 (finiteness of the integral closure in the separable case) and SG00000026 (finiteness of normalization in characteristic 0), each with its Lean proof. The node SG0000000M uses SG00000025, and the node SG0000001A uses SG00000024.
- `records/lean.json` from tamnd/singularity-lean at 756fa03, with the files `Singularity/Algebra/Normalization.lean` and `Singularity/Scheme/NormalDimOne.lean`. It has 74 declarations, and each uses only the three standard axioms.
- The node SG00000027, the normalization of an affine curve in characteristic 0 is a Dedekind domain, with its Lean proof.
- `records/lean.json` from tamnd/singularity-lean at 0cb57d5, with the file `Singularity/Curves/Affine.lean`. It has 76 declarations.
- The release v0.2.2 of tamnd/singularity-lean.

## 0.2.1 - 2026-11-24

- The nodes SG00000021 (the quotient of a regular local ring by a parameter), SG00000022 (regular local rings of dimension 1) and SG00000023 (a regular local ring is a unique factorization domain, planned). The node SG0000000J has its Lean proof, and its statement is now the domain part only. The node SG0000001A uses SG00000022.
- `records/lean.json` from tamnd/singularity-lean at 0df69ef, with the file `Singularity/Algebra/Regular.lean`. It has 69 declarations.
- `records/trust.json`: the replay with leanchecker passes on both packages. Q3 stays open, because the replay uses the same kernel.
- The release v0.2.1 of tamnd/singularity-lean, with `Singularity/Algebra/Regular.lean`.

## 0.2.0 - 2026-11-23

- The nodes SG0000001Y (the reduction to integral varieties, a named hypothesis), SG0000001Z (integral varieties in characteristic 0) and SG00000020 (Hironaka's theorem in the form of formal-conjectures). The nodes SG0000000D and SG0000000E have their Lean proofs.
- `records/lean.json` from tamnd/singularity-lean at 453191c, with the declarations of the base package. `records/base-charzero.json` is the record of the base package alone.
- `records/trust.json`, the first trust report. Q1, Q2 and Q6 are yes. Q3 and Q4 are not run yet.
- The paper records AM69, FC, HirLean and Mathlib, for the citations of the handbook.
- The release v0.2.0 of tamnd/singularity-lean, with the workflow `trust` for the replay of both packages.

## 0.1.0 - 2026-11-23

- The spec, documents 00 to 16.
- The style check `scripts/style.py`.
- The workflows: lint, scorecard and dependency updates.
- The first map: the blueprint nodes, the routes and the paper records for the corpus.
- The site pages `/problem/`, `/map/`, `/trust/` and `/papers/`, and the deploy of https://singularity.tamnd.com to Cloudflare from the main branch.
- The Lean names of the fidelity nodes, the node SG0000001W for dimension 0 and the node SG0000001X for the fidelity of P1.
- `records/lean.json`, the record of the Lean build. The map takes the status of each node from this record.
