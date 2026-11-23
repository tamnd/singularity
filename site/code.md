---
title: The code
description: The Lean package singularity-lean, its pinned toolchain and the statement files.
lead: The Lean code is in tamnd/singularity-lean. It builds with Lean 4 and Mathlib at a pinned tag.
---
## Build

```sh
git clone https://github.com/tamnd/singularity-lean
cd singularity-lean
lake exe cache get
lake build
```

## Layout

| Directory | Content |
|---|---|
| `Singularity/Statements/` | the statements of the problem: the vocabulary, the main statements and the core case |
| `Singularity/Fidelity/` | the positive and the negative instances of the fidelity checks |
| `scripts/Export.lean` | writes the record of the build, with the axioms of each declaration |

The statement files are pinned by hash in `manifests/statements.sha256`. A change to a statement file must change the hash in the same pull request.

## Contribute

Each pull request refers to a milestone issue of [tamnd/singularity](https://github.com/tamnd/singularity/issues). A proof must use the standard axioms only. A `sorry` can be in a pull request, but the map shows the node as `stated` until the `sorry` is gone.
