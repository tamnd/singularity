# Contributing

Thank you for your help. This file tells how to send a change.

## Before you start

1. Read `docs/spec/00-README.md`. It gives the plan and the decisions.
2. Find the milestone of your change. Each milestone has a tracking issue with the label `milestone`.
3. For a large change, open an issue first.

## A pull request

1. Make a branch from `main`.
2. Keep one subject in one pull request.
3. Give the pull request one `area/*` label and one `type/*` label, and the milestone.
4. Run `python3 scripts/style.py`. It must print nothing.
5. Run `sing check -content .` when you change `blueprint/` or `papers/`.

## The writing rules

The text follows ASD-STE100 technical English.

1. Write short sentences. Use one idea in one sentence.
2. Use the active voice.
3. Do not use an em dash or an en dash. Use a comma, a colon or a new sentence.
4. Do not break a line in the middle of a sentence. Write each paragraph on one line.
5. Do not add a page break.
6. Write math in `$...$`.
7. Write the names of theorems with more than one author with a hyphen: Cossart-Piltant.

## Statements and claims

A change to a statement in `Singularity/Statements/` of singularity-lean needs a review by two people. A claim that the open case is proved needs the full policy of spec 06.6.
