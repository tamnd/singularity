# 07. The corpus: the theories and papers to formalize

This is the list that "all related theories and papers" means (02.4). Each entry is a paper or book that some node of the map needs, with the reason it is needed. Tiers are in dependency order: a tier uses only the tiers above it, with the exceptions marked. The list is the first version. It grows when a node needs a new source, and every addition says which node asked for it.

The source tags [P], [S], [U] are those of document 01. The column **Lean** says what exists in Lean on 2026-11-23:
- **base**: in resolutionorg/hironaka (05);
- **rl**: in riemann-lean;
- **St**: in AxiomMath/Stacks (`StacksFrontier`, written by models and not reviewed, unless marked `Core`);
- **fc**: a statement in formal-conjectures;
- **ML**: in Mathlib;
- **PR**: an open Mathlib pull request;
- **none**: nothing found.

The column **Use** is the project's plan:
- **prove**: a full formal proof;
- **state**: a Lean statement used as a `proved-mod` hypothesis until proved (09.2.2);
- **ex**: certified examples (13.4);
- **read**: a source of ideas and definitions, with no theorem in the map.

## 7.1 Tier T0: references

The standard texts that define the language. They enter the map through definitions, not theorems.

| Key | Work | Why | Lean |
|---|---|---|---|
| Stacks | The Stacks project | definitions and tags for every scheme notion; AxiomMath/Stacks follows its tags | St (Core and Frontier) |
| EGA4 | Grothendieck, EGA IV (1964 to 1967) | excellence (§7), regular and smooth morphisms (§6, §17), limits (§8) | partly ML |
| Mat | Matsumura, *Commutative Ring Theory* (1986) | regular rings, Hasse-Schmidt derivations (§27), excellence (§32) | partly ML |
| BH | Bruns-Herzog, *Cohen-Macaulay Rings* (1993) | depth, Cohen-Macaulay, Hilbert-Samuel | PR (#26218 and others) |
| HS | Huneke-Swanson, *Integral Closure of Ideals, Rings, and Modules* (2006) | Rees algebras, integral closure, reductions | partly ML |
| Har | Hartshorne, *Algebraic Geometry* (1977) | the language of varieties; blowups (II.7) | partly ML |
| Liu | Liu, *Algebraic Geometry and Arithmetic Curves* (2002) | regular schemes over imperfect fields, arithmetic surfaces, Lipman's theorem in Chapter 9 | none |
| Kol07 | Kollár, *Lectures on Resolution of Singularities* (2007) | the char 0 proof (also T8) | base, rl |
| Cut04 | Cutkosky, *Resolution of Singularities*, AMS GSM 63 (2004) | char 0, surfaces, Abhyankar's method in a short form | none |
| Hau14 | Hauser, "Blowups and resolution" (2014) | blowups by universal property, char $p$ examples | none |
| CGO | Cossart-Giraud-Orbanz, LNM 1101 (1984) | resolution of surfaces, the excellent case | none |

## 7.2 Tier T1: commutative algebra and schemes

The gaps of Mathlib that every route needs. Most of this tier should go upstream (09.5).

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| Ser55 | Serre (1955); Auslander-Buchsbaum (1956) | regular local rings: localizations are regular, regular implies UFD | ML (`IsRegularLocalRing`), PR (#28683, #35561, #29802, #46021, #39510) | prove |
| Coh46 | Cohen (1946) | structure of complete local rings | PR (#44551, #44577) | prove |
| Nag62 | Nagata, *Local Rings* (1962) | Nagata rings, finiteness of normalization | St | prove |
| EGA4-7 | EGA IV §7 | excellent rings, openness of the regular locus | St (`IsExcellent`) | prove |
| Kunz69 | Kunz, Amer. J. Math. 91 (1969) | regular iff Frobenius is flat, in char $p$ | none | prove |
| Jac | the Jacobian criterion (Mat, §30; Stacks 07PF) | regularity of explicit equations, used by the certificates of 13.4 | none | prove |
| RegSm | regular and smooth (Stacks 00TV, 07NM, 038V) | smooth implies regular; regular implies smooth over a perfect field; separable base change keeps regularity | partly base | prove |
| Benn70 | Bennett, Ann. of Math. 91 (1970); Singh | the Hilbert-Samuel function does not go up under permissible blowups | none | prove |
| Hir64-perm | Hironaka (1964), Chapter II | normal flatness, permissible centres | base (char 0 form) | prove |
| Blow | Stacks 0806; Mayeux, arXiv:2609.28489 (2026) [P] | blowups: universal property, Proj of the Rees algebra, charts | base, rl, St, Mayeux | reuse and bridge |
| Cart | Stacks 01WR | effective Cartier divisors, invertible sheaves | base, PR (#44200) | reuse |
| HSDer | Hasse (1937), Schmidt; Mat §27 | Hasse-Schmidt derivations and differential operators in char $p$ | none | prove |
| Norm | normalization of schemes; finiteness for varieties | curves (T5), Lipman | ML (normalization), none for finiteness | prove |
| ZMT | Zariski's Main Theorem | proper birational maps of normal schemes | partly ML | prove |
| SNC | simple and strict normal crossings | the end state of every resolution | base, rl | reuse |
| Dim | Krull dimension of varieties | `topologicalKrullDim` bridge, dimension of fibres | partly ML | prove |

## 7.3 Tier T2: valuations

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| ZS2 | Zariski-Samuel, *Commutative Algebra* II (1960), Chapter VI | valuation rings, the Zariski-Riemann space | ML (valuations), none (Zariski-Riemann, PR #31938 closed) | prove |
| Abh56 | Abhyankar, Amer. J. Math. 78 (1956) | the Abhyankar inequality | none | prove |
| Mac36 | MacLane, Trans. AMS 40 (1936); Vaquié (2007) | key polynomials, augmented valuations | none (Sage has them) | prove |
| HMOS22 | Herrera-Mahboub-Olalla-Spivakovsky, J. Singularities 25 (2022), arXiv:1406.0657 [S] | key polynomials for simple extensions | none | prove |
| NS14 | Novacoski-Spivakovsky, arXiv:1204.4751, 1509.03122, survey 1509.06350 [P/S] | reduction of LU to rank one | none | prove |
| Nov24 | Novacoski, arXiv:2401.00182 [P] | generators of extensions of valuation rings | none | read |
| Kuh16 | Kuhlmann, J. reine angew. Math. 719 (2016), arXiv:1304.0194 [S] | tame valued fields | none | prove |
| Kuh-book | Kuhlmann, *Valuation Theory* (book draft) | defect, ramification theory | none | read |
| KR23 | Kuhlmann-Rzepka, arXiv:1811.04396 [P] | dependent and independent defect, deeply ramified fields | none | prove |
| CKR25 | Cutkosky-Kuhlmann-Rzepka, Math. Nachr. 298 (2025) [S] | independent defect iff relative Kähler differentials vanish | none | prove |
| DK20 | Dutta-Kuhlmann, Pacific J. Math. 307 (2020), arXiv:1912.06337 [S] | elimination of tame ramification | none | read |
| Kuh25 | Kuhlmann, arXiv:2503.13157 [S] | higher ramification | none | read |
| Spi90 | Spivakovsky, Amer. J. Math. 112 (1990) | valuations of function fields of surfaces | none | prove |
| Tei03 | Teissier, "Valuations, deformations and toric geometry" (2003) | graded algebra of a valuation, the toric program | none | read |

## 7.4 Tier T3: combinatorics

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| KKMS | Kempf-Knudsen-Mumford-Saint-Donat, *Toroidal Embeddings I*, LNM 339 (1973) | toric and toroidal resolution, in every characteristic | none | prove |
| Ful93 | Fulton, *Introduction to Toric Varieties* (1993); Cox-Little-Schenck (2011) | toric varieties, fans, subdivisions | partly (polyhedral cones in ML) | prove |
| Spi83 | Spivakovsky, "A solution to Hironaka's polyhedra game" (1983) | the combinatorial core of the monomial case | none | prove |
| Zei06 | Zeillinger, "A short solution to Hironaka's polyhedra game" (2006) [S] | a second strategy | none | prove |
| HSch12 | Hauser-Schicho, "A game for the resolution of singularities", arXiv:1010.0163 [S] | the char $p$ game | none | prove |
| Newt | Newton polyhedra, their faces and initial forms | every invariant of T4 | partly ML | prove |
| BFZ23 | Bérczi-Fan-Zeng, arXiv:2307.00252 [P] | learned strategies for the polyhedra game | none | read, lab |

## 7.5 Tier T4: invariants in characteristic p

The central tier. Every route uses it.

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| Hir67 | Hironaka, "Characteristic polyhedra of singularities", J. Math. Kyoto Univ. 7 (1967) [S] | the characteristic polyhedron, vertex preparation | none | prove |
| Hir70 | Hironaka, "Additive groups associated with points of a projective space", Ann. of Math. 92 (1970) [S] | the directrix and the ridge | none | prove |
| Gir75 | Giraud, "Contact maximal en caractéristique positive", Ann. Sci. ENS 8 (1975) [S] | what remains of maximal contact | none | prove |
| Nar83 | Narasimhan, Proc. AMS 87 (1983) [S] | maximal contact fails | none | ex |
| Moh87 | Moh, Publ. RIMS 23 (1987) [S] | the one-step bound on the residual order; the false stability claim | none | prove (bound), ex (failure) |
| Cos87 | Cossart, thesis and papers on the characteristic polyhedron (1980s) [U] | the polyhedron in practice | none | read |
| CJSch19 | Cossart-Jannsen-Schober, RACSAM 113 (2019), arXiv:1805.10660 [S] | the polyhedron is intrinsic | none | prove |
| CSch21 | Cossart-Schober, Collect. Math. 72 (2021), arXiv:1411.2522 [S]; arXiv:1411.4452 | a strictly decreasing invariant in dimension 2; no completion | none | prove |
| Sch | Schober, arXiv:1410.6541 (J. Algebra 565 (2021)), 1410.6543, 1708.04784 [S] | polyhedra and invariants | none | prove |
| Hau03 | Hauser, Bull. AMS 40 (2003) [S] | the char 0 proof, explained; the model for Volume 2 | none | read |
| Hau10 | Hauser, Bull. AMS 47 (2010) [P/S] | the diagnosis of char $p$ | none | read |
| Hau08 | Hauser, "Kangaroo points and oblique polynomials", arXiv:0811.4151 [S] | kangaroo points | none | prove, ex |
| HP19a | Hauser-Perlega, J. Algebraic Geom. 28 (2019), arXiv:1802.05010 [P] | the cycle that disproves Moh's stability | none | ex |
| HP19b | Hauser-Perlega, arXiv:1906.09593 [S] | the increase of the residual order, characterized | none | prove |
| HW14 | Hauser-Wagner, arXiv:1403.6789 [P] | corrected residual order for $z^p + f(x, y)$ | none | prove |
| Kaw07 | Kawanoue, Publ. RIMS 43 (2007), arXiv:math/0607009 [P] | idealistic filtrations | none | prove |
| KM10 | Kawanoue-Matsuki, arXiv:math/0612008 [P] | IFP, part II | none | prove |
| Vil07 | Villamayor, Adv. Math. 213 (2007); Rev. Mat. Iberoam. 24 (2008); arXiv:math/0606795, 0606796 [S] | Rees algebras with differential operators | none | prove |
| Vil08 | Villamayor, Publ. RIMS 44 (2008), arXiv:0712.3733 [S] | elimination algebras | none | prove |
| BV10 | Bravo-Villamayor, Adv. Math. 224 (2010), arXiv:0807.4308 [S] | stratification, simplification of the singular locus | none | prove |
| BenV13 | Benito-Villamayor, Compositio 149 (2013), arXiv:1004.1803 [P]; arXiv:1103.3462, 1103.3464 [S] | the elimination invariant in char $p$ | none | prove |
| BEP | Bravo-Encinas-Pascual-Escudero, arXiv:1802.02566, 1811.12203 [S]; Bravo-Encinas, arXiv:1912.00006 [S]; Bravo-Encinas-Guillán-Rial, arXiv:2307.11489 [S] | Nash multiplicity sequences | none | prove |
| BBE24 | Benito-Bravo-Encinas, Rev. Mat. Complut. 37 (2024), arXiv:2107.14188 [P] | the asymptotic Samuel function | none | prove |
| BBE25 | Benito-Bravo-Encinas, arXiv:2506.14993 [P] | the Samuel slope characterizes regularity | none | prove |
| MS25 | Mourtada-Schober, arXiv:2502.01239, C. R. Math. (2025) [P/S] | Teissier singularities | none | read |
| dFD20 | de Fernex-Docampo, Duke Math. J. 169 (2020), arXiv:1703.07505 [S] | differentials on arc spaces | none | read |
| Ber26 | Bérczi, arXiv:2602.06553 [P] | ranking functions found by AlphaEvolve, two conjectures | none | lab (E8), state |

## 7.6 Tier T5: curves, surfaces, threefolds

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| Curves | normalization of curves | `resolutionInDim_one` | none | prove |
| Zar39 | Zariski, Ann. of Math. 40 (1939) | surfaces in char 0 | none | read |
| Abh56s | Abhyankar, Ann. of Math. 63 (1956) | surfaces in char $p$ | none | read |
| Abh66 | Abhyankar, *Resolution of Singularities of Embedded Algebraic Surfaces* (1966; 2nd ed. 1998) | embedded surfaces; threefolds for $p > 5$ | none | read |
| Lip78 | Lipman, Ann. of Math. 107 (1978) [S] | excellent surfaces; `resolutionInDim_two` | St (`exists_isResolution_of_isExcellent_of_ringKrullDim_eq_two`) | prove, or review and bridge (Q-07) |
| Art86 | Artin, "Lipman's proof of resolution of singularities for surfaces", in *Arithmetic Geometry* (1986) | a shorter account of Lipman | none | read |
| CJS20 | Cossart-Jannsen-Saito, LNM 2270 (2020), arXiv:0905.2191 [P] | canonical embedded resolution of excellent surfaces | none | prove |
| HP24 | Hauser-Perlega, Publ. RIMS 60 (2024); Perlega, arXiv:2011.14443 [P] | embedded surfaces in 3-space, char $p$ | none | prove |
| KM16 | Kawanoue-Matsuki, arXiv:1205.4556, 1507.05195 [P] | surfaces in the IFP | none | prove |
| Cut09 | Cutkosky, Amer. J. Math. 131 (2009), arXiv:math/0606530 [P] | threefolds for $p > 5$ | none | prove |
| Cut11 | Cutkosky, Asian J. Math. 15 (2011) [S] | a key to Abhyankar's embedded surfaces | none | read |
| CP08 | Cossart-Piltant, J. Algebra 320 (2008) [P/S] | threefolds in char $p$, I | none | prove |
| CP09 | Cossart-Piltant, J. Algebra 321 (2009) [P/S] | threefolds in char $p$, II | none | prove |
| CP14 | Cossart-Piltant, RACSAM 108 (2014) [S]; arXiv:1203.2484 [S] | mixed char, small multiplicity | none | read |
| CP19 | Cossart-Piltant, J. Algebra 529 (2019), arXiv:1412.0868 [P] | quasi-excellent schemes of dimension $\le 3$ | none | prove |
| Kol20 | Kollár, arXiv:2012.05327, 2102.03162 [P] | log and projective resolution, dimension $\le 3$ | none | state |
| BMP20 | Bhatt et al., arXiv:2012.15801 [P] | MMP for threefolds in mixed char; resolution statements | none | read |

## 7.7 Tier T6: local uniformization and patching

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| Zar40 | Zariski, Ann. of Math. 41 (1940) | local uniformization in char 0 | none | prove |
| Zar44 | Zariski, Ann. of Math. 45 (1944) | patching; threefolds in char 0 | none | prove |
| Pil | Piltant, "An axiomatic version of Zariski's patching theorem" [S] | patching in a form to formalize | none | prove |
| KK05 | Knaf-Kuhlmann, Ann. Sci. ENS 38 (2005) [P] | Abhyankar valuations | none | prove |
| Cut20 | Cutkosky, arXiv:2003.06374 [P] | Abhyankar valuations, no separability | none | prove |
| KK09 | Knaf-Kuhlmann, Adv. Math. 221 (2009), arXiv:math/0702856 [P] | LU in a finite extension | none | prove |
| Tem13 | Temkin, J. Algebra 373 (2013), arXiv:0804.1554 [P] | inseparable local uniformization | none | prove |
| Tem23 | Temkin, arXiv:2301.09160 [P] | height reduction | none | prove |
| CM17 | Cutkosky-Mourtada, arXiv:1711.02726 [P] | defect as the obstruction | none | prove |
| HOST26 | Herrera Govantes-Olalla Acosta-Spivakovsky-Teissier, arXiv:2607.11223 [P] | tight extensions | none | prove |
| Tei14 | Teissier, arXiv:1401.5204 [S]; follow-ups arXiv:1807.04187, 2301.10636, 2311.12456 [S] | overweight deformations | none | state |
| Tev14 | Tevelev, "On a question of B. Teissier" (2014) [S] | a case of Teissier's conjecture | none | prove |
| Cut15 | Cutkosky, Math. Ann. 362 (2015), arXiv:1404.7459 [P] | local monomialization fails | none | ex |
| Cut21 | Cutkosky, arXiv:2111.12818 [P] | erratic behaviour in defect towers | none | ex |
| fc-LU | formal-conjectures `LocalUniformization.lean` | the statement | fc | bridge |

## 7.8 Tier T7: alterations

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| DM69 | Deligne-Mumford (1969) | stable curves and their moduli, used by de Jong | none | state (Q-08) |
| dJ96 | de Jong, Publ. Math. IHÉS 83 (1996) [S] | regular alterations | none (MingchenXia/Hironaka-lean claims it [S]) | prove |
| dJ97 | de Jong, Ann. Inst. Fourier 47 (1997) [S] | families of curves and alterations | none | read |
| AdJ97 | Abramovich-de Jong, J. Algebraic Geom. 6 (1997) [S] | smoothness, semistability, toroidal geometry | none | read |
| ILO14 | Illusie-Laszlo-Orgogozo (eds.), Astérisque 363-364 (2014), arXiv:1207.3648 [P/S] | Gabber's $\ell'$-alterations and LU prime to $\ell$ | none | prove |
| Tem17 | Temkin, Ann. of Math. 186 (2017), arXiv:1508.06255 [P/S] | $p$-alterations | none | prove |
| BR19 | Bergh-Rydh, destackification [S] | quotients of tame stacks | none | read |
| Kel17 | Kelly, Astérisque 391 (2017) [S] | what alterations replace in practice | none | read |

## 7.9 Tier T8: characteristic 0 and the modern methods

The char 0 sources are formalized in the base. They are in the corpus so that their nodes exist on the map and point to the base. The modern methods are what route R4 adapts.

| Key | Work | Why | Lean | Use |
|---|---|---|---|---|
| Hir64 | Hironaka, Ann. of Math. 79 (1964) | the theorem | base | bridge |
| Vil89 | Villamayor, Ann. Sci. ENS 22 (1989) | constructive resolution | none | read |
| BM97 | Bierstone-Milman, Invent. Math. 128 (1997) | the invariant | base | bridge |
| EV98 | Encinas-Villamayor (1998) | the algorithm | none | read |
| EH02 | Encinas-Hauser, Comment. Math. Helv. 77 (2002) | strong resolution | none | read |
| Wlo05 | Włodarczyk, JAMS 18 (2005), arXiv:math/0401401 | simple Hironaka resolution | base | bridge |
| Kol07 | Kollár (2007) | functorial resolution | base, rl | bridge |
| Tem08 | Temkin, Adv. Math. 219 (2008); Duke (2012); Israel J. Math. (2018) | quasi-excellent schemes in char 0 | none | state |
| ATW20 | Abramovich-Temkin-Włodarczyk, JEMS 22 (2020), arXiv:1709.03185 [P]; ANT 14 (2020), arXiv:1709.03206 [S] | toroidal orbifolds | none | prove |
| ATW24 | ATW, Algebra Number Theory 18 (2024), arXiv:1906.07106 [P] | weighted blowups | none | prove |
| McQ20 | McQuillan, GAFA 30 (2020) [S] | weighted blowups, independently | none | read |
| ATW-rel | ATW, arXiv:2003.03659 [P] | relative desingularization | none | read |
| Quek22 | Quek, Algebraic Geometry 9 (2022), arXiv:2005.05939 [S] | logarithmic weighted | none | read |
| AQ24 | Abramovich-Quek, Épiga 8 (2024), arXiv:2112.06361 [P] | multi-weighted | none | prove |
| ABQTW25 | arXiv:2503.13341, 2503.13345, 2503.00926 [P] | relative, logarithmic, foliated | none | read |
| Wlo22 | Włodarczyk, Adv. Math. 407 (2022), arXiv:2007.13846 [P] | cobordant blowups; toroidal in every char | none | prove |
| Wlo-cob | Włodarczyk, arXiv:2203.03090, 2301.12452, 2602.14266 [P] | cobordant blowups, Cox rings | none | read |
| TemD1 | Temkin, Dream resolution I, arXiv:2503.18205 [P] | "enough derivations" | none | prove |
| TemD2 | Temkin, Dream resolution II, arXiv:2507.11698 [P] | excellent schemes | none | state |
| AS22 | Abramovich-Schober, arXiv:2208.08951 [P] | binomial varieties, every char | none | prove |
| AQS24 | Abramovich-Quek-Schober, arXiv:2412.16426 [P] | plane curves in char $p$, tangent space growth | none | prove, ex |
| AQS25 | Abramovich-Quek-Schober, arXiv:2507.01232, Math. Scand. 132 (2026) [P] | torus actions, non-perfect fields | none | prove |
| AT26 | Abramovich-Temkin, arXiv:2602.15612 [P] | char 2 pinch points | none | ex |
| Abr25 | Abramovich, CIRM notes, arXiv:2503.17321 [P] | the char $p$ remarks 5.5.3 and 5.9.3 | none | ex |
| Pos24 | Posva, arXiv:2405.05735 [P] | 1-foliations in char $p$ | none | read |
| CDLL26 | Castillo-Duarte-Leyton-Álvarez-Liendo, Ann. of Math. 203 (2026), arXiv:2409.19767 [P] | Nash blowups fail in dimension $\ge 4$ | none | ex |
| MN26 | Martínez-Núñez, arXiv:2611.18258 [P] | T-varieties of complexity $\le 3$ | none | state (R9) |

## 7.10 Watch list: claims that are not in the corpus

These are recorded with the kind `claim` and are never used as hypotheses (01, 1.2): Hironaka 2017; Yi Hu, arXiv:2203.03842, 2507.21400, 2507.21399, 2608.10272, 2609.24047; Tian, arXiv:2608.20066. Each has a page on the site with its status and the results of lab test E9.

## 7.11 The paper record

Each paper has a file `papers/<key>.yaml` in `tamnd/singularity`:

```yaml
key: CP09
title: Resolution of singularities of threefolds in positive characteristic II
authors: [Vincent Cossart, Olivier Piltant]
where: J. Algebra 321 (2009) 1836-1976
doi: null                                # the reader role fills it
arxiv: null
read: { version: journal, by: reader, date: 2026-12-01, tag: P }
tier: T5
why: the only proof of resolution of threefolds in every char p
expert_status: accepted                  # accepted | claimed | withdrawn | disputed
uses: [CP08, Hir67, Benn70, Abh66]
results:
  - id: "Theorem 1.1"
    node: SG3P2F0ACD
    kind: theorem
    status: stated                       # computed from the map
lean_elsewhere: []                       # other formalizations, with commit
notes: Long case analysis; plan the node graph with the planner role before any proof (15, S6).
```

`expert_status` is set by a person and is shown with every `proved-mod` hypothesis that comes from the paper (14.3). 

## 7.12 Counts and order

The tiers have 142 rows (11 in T0, 16 in T1, 14 in T2, 7 in T3, 27 in T4, 17 in T5, 15 in T6, 8 in T7, 27 in T8, counting a row with several papers as one). The first ten to formalize, in order, are: RegSm, Jac, Benn70, Hir67, Moh87 (bound), Hau08 and HP19a (as certified examples), Curves, Lip78, CJS20. They give `resolutionInDim_one`, the first invariants of T4, the first counterexamples, and a start on dimension 2. They are the work of milestones S2 to S4 (document 15).
