# 11. tamnd/singularity-handbook: The Singularity Handbook

The handbook is the theory of resolution of singularities, written as a set of textbooks. It is written in the voice and to the standard of an expert: each chapter defines its objects, states its results in standard notation with numbers, proves them as a mathematician proves them, and ends with notes and references. Its readers are graduate students and working mathematicians who do not read Lean. It comes as PDF and EPUB volumes, and the site has the same text in HTML.

It differs from the riemann handbook in one way: there the mathematics is extracted from a finished Lean proof. Here most of the mathematics exists in papers and books, and the Lean proof is being written. So each chapter follows the published proof, says where the Lean proof stands, and links each result to its node.

## 11.1 The volumes

| | Volume | Main sources | Chapters (estimate) |
|---|---|---|---|
| 0 | Guide: how to read, the problem and its status, notation, the map, an index of Lean names | this spec | 5 |
| 1 | Commutative algebra for resolution: regular rings, completion and the Cohen structure theorem, excellence, Hilbert-Samuel functions and multiplicity, Rees algebras and integral closure, differential operators and Hasse-Schmidt derivations, $p$-bases and Frobenius (Kunz) | Matsumura, Stacks Project, Grothendieck EGA IV, Huneke-Swanson | 12 |
| 2 | Resolution in characteristic 0: the order, maximal contact, coefficient ideals, the invariant, the monomial case, functoriality; weighted blowups | Kollár 2007, Włodarczyk 2005, Bierstone-Milman 1997, Encinas-Hauser 2002, Abramovich-Temkin-Włodarczyk 2019, McQuillan 2019; the char 0 base | 10 |
| 3 | Valuations: Zariski-Riemann spaces, the Abhyankar inequality, key polynomials (MacLane, Vaquié, Herrera Govantes-Olalla Acosta-Mahboub-Spivakovsky), ramification and defect (Kuhlmann) | Zariski-Samuel II, Vaquié, Kuhlmann | 9 |
| 4 | Curves and surfaces in every characteristic: normalization, Lipman's theorem, Abhyankar, embedded surfaces (Cossart-Jannsen-Saito) | Lipman 1978, Cutkosky 2004, Cossart-Jannsen-Saito | 8 |
| 5 | Local uniformization: Zariski in char 0, Abhyankar valuations (Knaf-Kuhlmann), inseparable local uniformization (Temkin), the Teissier program, Zariski patching in dimension $\leq 3$ | Zariski 1940, 1944; Knaf-Kuhlmann 2005; Temkin 2013; Teissier 2014 | 8 |
| 6 | Threefolds in positive characteristic: the Cossart-Piltant proof; Cutkosky's proof for $p > 5$ | Cossart-Piltant 2008, 2009; Cutkosky 2009 | 10 |
| 7 | Invariants in positive characteristic: the characteristic polyhedron, Moh's bound, kangaroo points, Hironaka's and Giraud's maximal contact, idealistic exponents, Rees algebras and elimination (Villamayor, Benito, Bravo, Encinas), the idealistic filtration program (Kawanoue-Matsuki) | Hironaka 1967, Cossart-Schober, Hauser 2010, Hauser-Perlega, Benito-Villamayor, Kawanoue-Matsuki | 10 |
| 8 | Alterations: de Jong, Gabber's $\ell'$ alterations, Temkin's $p$-alterations; what they give for cohomology and motives | de Jong 1996, Illusie-Laszlo-Orgogozo 2014, Temkin 2017 | 6 |
| 9 | The open problem: dimension 4 in characteristic $p$; the routes of document 04 and the results of the project, with their status | this project | grows |

The volume list follows the tiers of document 07, so a reader can learn the subject in the order in which the project formalizes it. Each volume has a release when all its chapters are at status `reviewed` (11.3). Volume 9 is the exception: it is released at each project milestone, as a research report.

## 11.2 A chapter

A chapter is a folder `content/<NN-volume>/<NN-chapter>/` with an `intro.md` and one file per section, as in the riemann handbook. A section opens with front matter:

```markdown
---
title: Moh's bound
nodes: [SG3KQ7M2PA, SG7Y2N0QBE]
sources: [moh1987stability, hauser2010problem]
status: drafted        # drafted | checked | reviewed
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Moh's bound

<One paragraph: what this section proves and why the problem needs it.>

**Theorem (Moh).** Let $f = z^{p^e} + \dots$ ...

Node: SG3KQ7M2PA · Lean: `Singularity.Residual.moh_bound` (status: stated)

*Proof.* ... $\square$
```

Each theorem has a `Node:` line with its tag and its Lean name, and the builder writes the current status from `records/status.json` of `tamnd/singularity` at build time. A statement that has no Lean proof yet says so in that line. The text never claims more than the status.

## 11.3 Who writes and who checks

The `writer` role drafts from the papers, the map and the Lean code. A draft becomes `checked` when a second model pass and the script checks find no problem: every cited result exists in the source at the given place, every `Node:` line resolves, the numbers are consistent, the style rules hold. It becomes `reviewed` when a person with the right background has read it and signed it in `reviewed_by`. Only `reviewed` chapters go into a numbered release. Drafts are in the `-dev` builds and on the site with a banner.

Volumes 2, 4 and 6 have proofs in the literature that are long and, in places, hard to follow. The handbook may give a different proof than the paper when the Lean proof does, and then it says so and gives both references.

## 11.4 The builder

`shb` is the builder, in Python, as `rhb` of the riemann handbook: it reads the Markdown, numbers the statements (`shb number --write`), checks the links and the `Node:` lines, writes LaTeX with `tex/handbook.sty`, runs LuaLaTeX, and writes the EPUB. It starts as a copy of `rhb` with the riemann-specific parts removed. The output goes to `build/singularity-handbook-<NN-volume>-<version>.{pdf,epub}`, and each release is a GitHub release. `EDITION` records the commits of `tamnd/singularity` and of the base that the edition describes.
