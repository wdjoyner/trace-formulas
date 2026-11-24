# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks of the Paley-Wiener examples of Draft 2 (Sections 5 and 8).

Run:  python3 spherical_trace_check.py

Notation: X is the Satake parameter (X = chi_sigma(varpi) on the cover,
X = chi(h(varpi)) for SL(2,F) itself), q the residue cardinality,
c(X) = (1 - X/q)/(1 - X) the Gindikin-Karpelevich factor (Theorem 3.12).

S1  c(X) c(1/X) vanishes exactly at X = q and X = 1/q, and has its only
    pole at X = 1 (reducibility at s = +-1/n, irreducibility at s = 0 when
    chi_sigma = 1).
S2  Macdonald's formula for SL(2,F) (the case n = 1; Example 8.1): for m >= 1,
      P_m(X) = q^m [ X^m c(1/X) + X^(-m) c(X) ]
    equals the Laurent polynomial sum_{|j|<=m} X^j - (1/q) sum_{|j|<=m-1} X^j,
    it is invariant under X -> 1/X, and P_m(q) = q^(2m-1)(q+1), the number
    of cosets in K h(varpi^m) K / K (trace on the trivial representation).
S3  The relations of Example 5.12 at the two reducibility points of the
    unramified component of SL(2,F), for the Euler-Poincare function
    e_K + e_K' - e_I and for e_K - e_K', from the table of dimensions of
    fixed vectors.
"""
from fractions import Fraction as Fr
import sys


def c(X, q):
    return (1 - X / q) / (1 - X)


def s1():
    ok = True
    for q in (3, 5, 7, 9, 13):
        q = Fr(q)
        ok &= c(q, q) == 0 and c(1 / q, q) * c(q, q) == 0
        for X in (Fr(2), Fr(-1), Fr(1, 3) + 5, -q, q * q):
            if X not in (q, 1 / q, 1):
                ok &= c(X, q) * c(1 / X, q) != 0
    return ok


def s2():
    ok = True
    for q in (3, 5, 7):
        q = Fr(q)
        for m in range(1, 7):
            for X in (Fr(2), Fr(-3), Fr(5, 7), Fr(-1), q, 1 / q):
                if X == q:      # limit value: c(1/X) is finite, c(X) = 0
                    lhs = q**m * (X**m * c(1 / X, q))
                elif X == 1 / q:
                    lhs = q**m * (X**(-m) * c(X, q))
                else:
                    lhs = q**m * (X**m * c(1 / X, q) + X**(-m) * c(X, q))
                rhs = q**m * (sum(X**j for j in range(-m, m + 1))
                              - sum(X**j for j in range(-m + 1, m)) / q)
                ok &= lhs == rhs
                Y = 1 / X
                rhs2 = q**m * (sum(Y**j for j in range(-m, m + 1))
                               - sum(Y**j for j in range(-m + 1, m)) / q)
                ok &= rhs == rhs2
            Pq = q**m * (sum(q**j for j in range(-m, m + 1)) - sum(q**j for j in range(-m + 1, m)) / q)
            ok &= Pq == q**(2 * m - 1) * (q + 1)
    return ok


def s3():
    # dimensions of (K, K', I)-fixed vectors, SL(2,F), unramified component
    dims = {"I(chi) irreducible": (1, 1, 2), "trivial": (1, 1, 1), "Steinberg": (0, 0, 1),
            "pi+": (1, 0, 1), "pi-": (0, 1, 1)}
    ep = {k: v[0] + v[1] - v[2] for k, v in dims.items()}
    df = {k: v[0] - v[1] for k, v in dims.items()}
    ok = ep == {"I(chi) irreducible": 0, "trivial": 1, "Steinberg": -1, "pi+": 0, "pi-": 0}
    ok &= df == {"I(chi) irreducible": 0, "trivial": 0, "Steinberg": 0, "pi+": 1, "pi-": -1}
    # additivity at the reducible points: constituents sum to the generic value
    ok &= ep["trivial"] + ep["Steinberg"] == ep["I(chi) irreducible"] == ep["pi+"] + ep["pi-"]
    ok &= df["trivial"] + df["Steinberg"] == df["I(chi) irreducible"] == df["pi+"] + df["pi-"]
    return ok


def main():
    res = {"S1 zeros and poles of c(X)c(1/X)": s1(),
           "S2 Macdonald formula and its Laurent form": s2(),
           "S3 separating functions at reducibility points (n = 1)": s3()}
    bad = 0
    for k, ok in res.items():
        print("%-60s %s" % (k, "ok" if ok else "FAIL")); bad += not ok
    print("\n%d failure(s)" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
