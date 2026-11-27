# Note 59: referee report on note 57

## The claims

`checks.py` is the evidence for the numerical checks [C] of research note 59, the referee report on note 57. It is independent code. It does not import the scripts of note 57 in `../57`.

- Section 4 (Example 3.11 of note 57): the root theta for p = 3, 5, the values nu(theta - c) for the two choices of c, and the identity that shows that F = k(x_1, x_2, theta, x_4) is rational. The 35 products X^j s^k with j <= 6 and k <= 4 are linearly independent over F_p modulo X^200 for p = 2, 3 [C].
- Section 5 (Section 4 of note 57): the leading exponents of Proposition 4.1(b), the values of ElHitti and Ghezzi and their bound.
- Section 7: the Perron algorithm on (1, sqrt 2). All outputs agree with note 57, except where Sections 4 and 5 of note 59 give a correction.

## The files

- `checks.py`: truncated series over F_p in x_1, x_2 with exponents in Q^2 and the weights (1, sqrt 2), and the checks above.

## Run

From the root of the repository:

```sh
python3 lab/notes/59/checks.py
```

## Expected output

Key lines:

```text
Ex 3.11, p=3: nu(f(theta)) >= inf; nu(theta)=2.000; nu(theta - (-x1 x3)) = 4.000 (expected 2p-2 = 4)
Ex 3.11, p=5: nu(f(theta)) >= inf; nu(theta)=2.000; nu(theta - (-x1 x3)) = 8.000 (expected 2p-2 = 8)
EG p=2: nu(P_0..P_5) = ['1', '1/4', '17/16', '273/64', '4369/256', '69905/1024']; binomial balance of recursion holds: True; bound (Omega-2)/p = -7/15 < -1/p^2: True
transcendence test p=2: 35 products X^j s^k (j<=6, k<=4) have rank 35 mod X^200
transcendence test p=3: 35 products X^j s^k (j<=6, k<=4) have rank 35 mod X^200
```

## Run time

Less than 1 second.

## Dependencies

Python 3 and its standard library only.

## Changes from the original

Only the first comment line is changed: it names the scripts of note 57 in place of their absolute path. The code is not changed.
