# Changelog

Each release has a section. The newest release is first.

## Unreleased

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
