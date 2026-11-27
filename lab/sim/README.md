# The lab simulator

`labsim` is a small Python package for the computations of note 03 and of Volume 7 of the handbook. It uses only the standard library of Python 3. The engine of `sing lab` stays the tool for the large runs. The simulator is for single examples, for certificates and for the test bank.

## What it does

- Fields: F_p and F_{p^k}, with the q-th root (the inverse of the Frobenius map). An element of F_{p^k} is an int code, and the codes 0 to p - 1 are the prime field. In an expression, `#c` is the element with the code c.
- Polynomials: a ring with named variables, a parser for `+ - * ^` and parentheses, the order, the order along a coordinate stratum, the derivatives, the translations (with the theorem of Lucas) and the substitutions.
- Cleaning of z^q + F: `clean(F, q)` removes the monomials with all exponents divisible by q and gives h with F = G - h^q, so the change z -> z + h takes z^q + F to z^q + G.
- Charts: `Point(F, q, E).chart(j, t, centre)` is the x_j-chart of the blowup with the centre V(x_i, i in centre), followed by the translations t and the cleaning. With no centre it is the point blowup. The new divisor is {j} together with the old components through the new point: the i in E with i not in the centre or t_i = 0. The option `strip_units` divides by the q-th power units of the translated coordinates.
- Invariants: the monomial factor r, the residual factor G and the residual order d; the generators of Theta(F), Theta-tilde(G) and Theta-tilde_C(G); rho and the type tau = d - rho; the hypotheses (H1) and (H2) of Theorem 3.16 of note 03; nu^G along a coordinate stratum (Lemma 3.13.1 of the handbook); the test "a monomial in E times a unit"; and a change to a free coordinate X = x + lam w + gamma, with the cleaning in the new coordinates.
- Random walks: `walk` and `survey` make point blowups with random charts and random translations from a seed. `survey` counts the failures of Theorem 3.7 (rho is d - 1 or d), Theorem 3.12 (rho does not go up), Corollary 3.13 (d' <= d + 1) and Corollary 3.14 (a kangaroo point is a type switch). These statements are for q = p.
- Certificates: `certificate.make` writes a chart sequence in the format of target (e.1) of note 11, and `certificate.check` computes each step again. The folder `certificates/` has the kangaroo point and the first six steps of the cycle of Hauser and Perlega.

The invariant rho uses first derivatives. It is the invariant of note 03 only for q = p. For q = p^e with e > 1 (as in the cycle of Hauser and Perlega, q = 8) the simulator gives d and the charts, and rho has no meaning.

Each step is a real chart of a blowup, with the translations and the cleaning. This is the correction K3 of note 12 for the simulator of Bérczi.

## Use

```sh
cd lab/sim
python3 -m unittest discover -s tests -t .
python3 -m labsim step -p 2 -vars x,y -f "x^3*y + x*y^3" -divisor x,y -chart x -t y=1
python3 -m labsim step -p 2 -vars x,y,w -f "y^2*w + y^3" -divisor w -chart x -centre x,y -nu x,y
python3 -m labsim walk -p 3 -n 4 -walks 200 -seed 1
python3 -m labsim check certificates/hp-cycle-p2.json
```

In Python:

```python
from labsim import Point, Ring, invariants
R = Ring.over(2, "x,y")
P = Point(R("x^3*y + x*y^3"), 2, {"x", "y"})
s = P.chart("x", {"y": 1})
print(s.F, s.h, invariants(s.F, s.E))
```

## The test bank

Each test checks the values that the notes and the handbook give.

| Test | Source | What it checks |
|---|---|---|
| `test_note03.KangarooTest` | note 03, the kangaroo point of Hauser | g = x^3 y + x y^3, p = 2: d = rho = 2, tau = 0; after the x-chart with t_y = 1 the cleaning drops x^2 y^2 with h = xy, E' = {x}, r' = (2, 0), G' = y^3, d' = 3, rho' = 2, tau' = 1 |
| `test_note03.Example317Test` | note 03, Example 3.17 | g = y^2 w + y^3, C = V(x, y): d = 3, rho = 2, (H1) holds, (H2) fails with ord_C = 2 and ord_0 = 3; the x-chart gives y^2 w + x y^3, E' = {x, w} and rho' = 3 |
| `test_note03.WalkTest` | note 03, Theorems 3.7 and 3.12, Corollaries 3.13 and 3.14 | random walks for p = 2, 3, 5 and n = 3, 4 with no failure |
| `test_hauser_perlega.CycleTest` | Hauser and Perlega, the Lean file `HauserPerlegaCycle.lean` | the 20 steps of the cycle for p = 2, q = 8: the cleaning h = xw, the divisors, the residual orders 6, 5, 5, 5, 5, 4, 4, the term counts 9 and 136, and the final form x^12 y^2128 u^84 w^60 (w^4 (1 + y^14 Q) + x^5 y^14 A) |
| `test_hauser_perlega.Section3Test` | Hauser and Perlega, section 3 | d goes from 5 to 7, with 3 terms |
| `test_handbook.Example31321Test` | handbook, Example 3.13.21 | rho = a - 1, nu^G_C = a, (H1) and (H2), the three kinds of chart, the run (4, 4), (1, 4), (1, 1) for p = 5, a = 2, and a run with no end for a > p |
| `test_handbook.Example3149Test` | handbook, Example 3.14.9 | rho = d = p and the same G along random words, nu^G = p, p - 1, p - 2 on the curves, the surfaces and V(x4), and the numbers for p = 3 |
| `test_handbook.Example31518Test` | handbook, Example 3.15.18 | both origin charts fix g, rho = 1, d = 2, nu^G = 2 on the corner curves |
| `test_counterexamples.Note38Test` | note 38, Proposition 5.1 and Corollary 5.4 | rho = 1 at each point of random words with b_m != 0, and neither partial derivative is a monomial times a unit |
| `test_counterexamples.Note40Test` | note 40, Theorem 2.3 | for p = 5, 7, 11 and over F_25: the invariants, only (0, 0) keeps rho, nu^G <= 1 on the corner surfaces with the maximum 1, and nu^G = 3, 3, 0, 3 on V(x, w, y), V(x, w, z), V(y, z), V(x, w) |
| `test_counterexamples.Note42Test` | note 42, Example 3.1 | d = 4, rho = 3, both origin charts fix g, only (0, 0) keeps rho, the maximum 1 on the corner surfaces, nu^G = 4 on the corner curves |
| `test_field_poly`, `test_cli` | | the fields, the polynomials, the cleaning, the charts, the command line and the stored certificates |

## Limits

- nu^G is computed along coordinate strata. For other strata, change the coordinates first with `free_coordinate` or `Poly.substitute`.
- The free lines of `invariants.lines` are the lines over the given field. A test over F_p does not cover the lines over the algebraic closure.
- A random walk uses only point centres and the points over the field of the ring.
