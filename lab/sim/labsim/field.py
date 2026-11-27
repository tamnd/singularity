"""Finite fields F_p and F_{p^k}.

An element is an int. For F_p it is the residue in 0..p-1. For F_{p^k} it is the code c = c_0 + c_1 p + ... + c_{k-1} p^{k-1} of the polynomial c_0 + c_1 a + ... + c_{k-1} a^{k-1}, where a is a root of a fixed monic irreducible polynomial of degree k. The codes 0..p-1 are the prime field.
"""

from functools import lru_cache


def _prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def _is_prime(n):
    return n >= 2 and _prime_factors(n) == [n]


def _poly_mod(a, m, p):
    """The remainder of a by the monic m. Lists of coefficients, low degree first."""
    a = [c % p for c in a]
    while len(a) >= len(m):
        c = a[-1]
        if c:
            shift = len(a) - len(m)
            for i, mi in enumerate(m):
                a[shift + i] = (a[shift + i] - c * mi) % p
        a.pop()
    while a and a[-1] == 0:
        a.pop()
    return a


def _irreducible(p, k):
    """The first monic irreducible polynomial of degree k over F_p, in a fixed order."""
    if k == 1:
        return [0, 1]

    def monics(deg):
        for code in range(p ** deg):
            yield [(code // p ** i) % p for i in range(deg)] + [1]

    for f in monics(k):
        if f[0] == 0:
            continue
        if all(_poly_mod(f, g, p) for deg in range(1, k // 2 + 1) for g in monics(deg)):
            return f
    raise ValueError("no irreducible polynomial")


class Field:
    """The field F_{p^k}. Use field(p, k) to get a shared instance."""

    def __init__(self, p, k=1):
        if not _is_prime(p):
            raise ValueError(f"{p} is not a prime")
        if k < 1:
            raise ValueError("the degree must be at least 1")
        self.p, self.k, self.size = p, k, p ** k
        if k == 1:
            self.modulus = [0, 1]
            return
        self.modulus = _irreducible(p, k)
        size = self.size
        if size > 1 << 16:
            raise ValueError("the field is too large for the tables")
        # Multiplication with logarithms to a primitive element.
        order = size - 1
        factors = _prime_factors(order)
        for g in range(p, size):
            if all(self._slow_pow(g, order // l) != 1 for l in factors):
                break
        self.generator = g
        self._exp = [0] * (2 * order)
        self._log = [0] * size
        x = 1
        for i in range(order):
            self._exp[i] = x
            self._log[x] = i
            x = self._slow_mul(x, g)
        for i in range(order, 2 * order):
            self._exp[i] = self._exp[i - order]
        self._digits = [self._decode(c) for c in range(size)]

    # Slow arithmetic on codes, used only to build the tables.
    def _decode(self, c):
        return [(c // self.p ** i) % self.p for i in range(self.k)]

    def _encode(self, v):
        return sum((int(u) % self.p) * self.p ** i for i, u in enumerate(v))

    def _slow_mul(self, a, b):
        va, vb = self._decode(a), self._decode(b)
        prod = [0] * (2 * self.k - 1)
        for i, u in enumerate(va):
            if u:
                for j, w in enumerate(vb):
                    prod[i + j] += u * w
        return self._encode(_poly_mod(prod, self.modulus, self.p))

    def _slow_pow(self, a, n):
        r = 1
        while n:
            if n & 1:
                r = self._slow_mul(r, a)
            a = self._slow_mul(a, a)
            n >>= 1
        return r

    # The field operations.
    def add(self, a, b):
        if self.k == 1:
            return (a + b) % self.p
        da, db, p = self._digits[a], self._digits[b], self.p
        return self._encode([(u + w) % p for u, w in zip(da, db)])

    def neg(self, a):
        if self.k == 1:
            return (-a) % self.p
        return self._encode([(-u) % self.p for u in self._digits[a]])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.k == 1:
            return (a * b) % self.p
        if a == 0 or b == 0:
            return 0
        return self._exp[self._log[a] + self._log[b]]

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError("0 has no inverse")
        if self.k == 1:
            return pow(a, self.p - 2, self.p)
        return self._exp[(self.size - 1 - self._log[a]) % (self.size - 1)]

    def pow(self, a, n):
        if n == 0:
            return 1
        if a == 0:
            return 0
        if self.k == 1:
            return pow(a, n, self.p) if n > 0 else pow(self.inv(a), -n, self.p)
        return self._exp[(self._log[a] * n) % (self.size - 1)]

    def from_int(self, n):
        return n % self.p

    def root(self, a, q):
        """The unique q-th root of a, for q a power of p (the inverse of the Frobenius map)."""
        e = 0
        while q > 1:
            if q % self.p:
                raise ValueError("q must be a power of p")
            q //= self.p
            e += 1
        r = a
        # x -> x^p is a bijection of order k, so the p-th root is x^(p^(k-1)).
        for _ in range(e):
            r = self.pow(r, self.p ** (self.k - 1))
        return r

    def elements(self):
        return range(self.size)

    def nonzero(self):
        return range(1, self.size)

    def __repr__(self):
        return f"F_{self.p}" if self.k == 1 else f"F_{self.p}^{self.k}"


@lru_cache(maxsize=None)
def field(p, k=1):
    """The shared instance of F_{p^k}."""
    return Field(p, k)
