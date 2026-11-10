# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Shared exact p-adic helpers for the sl2bar-trace checks: valuations and the
quadratic Hilbert symbol (a, b)_v of nonzero rationals, v a prime or "inf"."""
from fractions import Fraction as Fr

INF = "inf"


# ---------------------------------------------------------------- arithmetic
def vp(x, p):
    """p-adic valuation of a nonzero rational."""
    x = Fr(x)
    assert x != 0
    num, den, v = x.numerator, x.denominator, 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def unit_mod(x, p, m):
    """x = p^v u with u a p-adic unit; return u mod p^m (as an int)."""
    x = Fr(x)
    v = vp(x, p)
    u = x / Fr(p) ** v
    M = p ** m
    return (u.numerator * pow(u.denominator, -1, M)) % M


def legendre(a, p):
    a %= p
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


def hilbert(a, b, v):
    """Quadratic Hilbert symbol (a, b)_v for nonzero rationals a, b."""
    a, b = Fr(a), Fr(b)
    assert a != 0 and b != 0
    if v == INF:
        return -1 if (a < 0 and b < 0) else 1
    p = v
    al, be = vp(a, p), vp(b, p)
    if p != 2:
        u, w = unit_mod(a, p, 1), unit_mod(b, p, 1)
        s = (-1) ** (al * be * ((p - 1) // 2))
        return s * legendre(u, p) ** be * legendre(w, p) ** al
    u, w = unit_mod(a, 2, 3), unit_mod(b, 2, 3)
    eps = lambda z: ((z - 1) // 2) % 2
    om = lambda z: ((z * z - 1) // 8) % 2
    return (-1) ** ((eps(u) * eps(w) + al * om(w) + be * om(u)) % 2)
