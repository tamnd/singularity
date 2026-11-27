# Note 57: zero defect projections and independent defect

## The claims

These scripts are the evidence for the numerical checks [C] of research note 57.

- Section 3.4, Example 3.11, numerical check [C]: for 12 random h in F_p[x_1, ..., x_4] and p = 2, 3, the leading term of h(x_1, x_2, s(x_1), s(x_2)) is that of h_0 = h(x_1, x_2, P_3, P_4) (Proposition 3.6), and the Perron algorithm of Lemma 3.4 needs 1 to 3 steps. Script: `ca_family.py`.
- Section 4.1 [C, consistent with the proof]: the leading exponent of vartheta_0 - s is (1/2, 1/2) in the coordinates (t, z) for p = 2 and (1/3, 2/3) for p = 3. Script: `dist_tests.py`.
- Section 4.3 [C, arithmetic only]: the values nu(P_i) of ElHitti and Ghezzi for p = 2, 3, 5 and the bound D <= (Omega - 2)/p < -1/p^2. Script: `dist_tests.py`.
- Section 4.4, Example A [C]: for p = 2, 3 and six partial sums vartheta_k, vartheta^p - vartheta - 1/t is the single tail term and nu(vartheta - vartheta_k) = -1/p^(k+1), so the defect is independent. Script: `dist_tests.py`.

Note 59 checks the same values with its own code, in `../59`.

## The files

- `hahn.py`: truncated series over F_p with exponents in Z^2 or Q^2 (a small Hahn field).
- `ca_family.py`: the CA family K = F_p(x_1, x_2, s(x_1), s(x_2)) with nu(x_1) = 1, nu(x_2) = sqrt 2 and s(x) = sum x^(n!).
- `dist_tests.py`: the distances of the Artin-Schreier extensions of Section 4.

## Run

From the root of the repository:

```sh
python3 lab/notes/57/ca_family.py
python3 lab/notes/57/dist_tests.py
```

## Expected output

`ca_family.py` ends each prime with these lines:

```text
p=2: 12 polynomials, leading term of h equals that of h0 in all cases
p=3: 12 polynomials, leading term of h equals that of h0 in all cases
```

`dist_tests.py` prints, among other lines:

```text
   sup = 0-, the idempotent cut: independent defect
   leading exponent of theta0 - s in (t,z)-coordinates: ('1/2', '1/2'), value 1.2071
   leading exponent of theta0 - s in (t,z)-coordinates: ('1/3', '2/3'), value 1.2761
EG example, p=2: Omega=16/15, distance <= -7/15 = -0.46667 < -1/p^2 = -0.25000 < 0: dependent
```

## Run time

Each script takes less than 1 second.

## Dependencies

Python 3 and its standard library only.

## Changes from the original

The scripts find `hahn.py` in their own folder. The original scripts used an absolute path. The mathematics is not changed.
