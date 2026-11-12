# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact check of the identity behind Lemma 6.7 of route-b-draft.tex.

With c(y) = (1 - a*y)/(1 - y), a = 1/q, and l(y) = y*c'(y)/c(y), the lemma
uses
    l(y) + l(1/y) = -(1 - a^2) / ((1 - a*y)*(1 - a/y)),
and on |y| = 1 the denominator is |1 - a*y|^2. The script also checks that
l(y) + l(1/y) is the derivative that appears in the proof.
"""
import sys

import sympy as sp

y, a, q, xi = sp.symbols("y a q xi", positive=True)
c = lambda t: (1 - a * t) / (1 - t)
_t = sp.Symbol("t")
_ell = sp.simplify(_t * sp.diff(c(_t), _t) / c(_t))
ell = lambda t: _ell.subs(_t, t)

lhs = ell(y) + ell(1 / y)
rhs = -(1 - a**2) / ((1 - a * y) * (1 - a / y))
ok1 = sp.simplify(lhs - rhs) == 0

# d/dxi [ log c(q^xi / y) - log c(y q^-xi) ] at xi = 0, with a = 1/q
F = sp.log(c(q**xi / y)) - sp.log(c(y * q**(-xi)))
deriv = sp.diff(F, xi).subs(xi, 0).subs(a, 1 / q)
ok2 = sp.simplify(deriv - sp.log(q) * lhs.subs(a, 1 / q)) == 0

print("l(y) + l(1/y) = -(1 - a^2)/((1 - a y)(1 - a/y)):", ok1)
print("derivative in the proof = log(q) * (l(y) + l(1/y)):", ok2)
sys.exit(0 if (ok1 and ok2) else 1)
