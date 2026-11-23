---
title: Trust
description: The checks that each Lean result must pass before the project calls it proved, and the state of each check.
lead: A Lean proof is only as good as its statement and its build. These checks say what a reader can trust.
---
A check is "not run" until the trust workflow runs it on a project machine. The rows come from `records/trust.json`, and a person does not edit them.

The statements of the open problem also need the fidelity checks F1 to F7: the file builds with no axioms, positive instances, negative instances, a triviality attack, a round trip to English, a human review by two experts, and a pinned hash of the statement file.
