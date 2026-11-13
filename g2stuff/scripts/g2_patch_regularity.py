# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Check that each fundamental patch of Section 4 is an open subset of affine space in the listed
generators: every coordinate of Z must be a monomial in the generators, with negative exponents
only on generators that are inverted on the patch (the ones required to be nonzero)."""
import sympy as sp
za, zb, lam = sp.symbols('z_a z_b lam')
x = {r: sp.Symbol('x_' + r) for r in 'abgdez'}
w = {r: sp.Symbol('w_' + r) for r in 'gdez'}
m = {'a': (1, 0), 'b': (0, 1), 'g': (1, 1), 'd': (2, 1), 'e': (3, 1), 'z': (3, 2)}
eqs = [sp.Eq(lam * (w[r] if r in w else 1), x[r] * za**m[r][0] * zb**m[r][1]) for r in m]
allc = [lam, za, zb] + list(x.values()) + list(w.values())
patches = {
 'Z_ab':  ([lam, x['a'], x['b'], x['g'], x['d'], x['e'], x['z']], [x['a'], x['b']]),
 'Z_a':   ([lam, x['a'], zb, x['g'], x['d'], x['e'], x['z']], [x['a'], zb]),
 'Z_b':   ([lam, za, x['b'], x['g'], x['d'], x['e'], x['z']], [za, x['b']]),
 'Z_empty': ([lam, za, zb, w['g'], w['d'], w['e'], w['z']], [za, zb]),
}
for s2, other in (('a', zb), ('b', za)):
    gl = {'g': [za, zb, x['g'], w['g'], x['d'], x['e'], x['z']],
          'd': [za, zb, w['g'], x['d'], w['d'], x['e'], x['z']],
          'e': [za, zb, w['g'], w['d'], w['e'], x['e'], x['z']],
          'z': [za, zb, w['g'], w['d'], w['e'], w['z'], x['z']]}
    for sig, gens in gl.items():
        patches[f'Z_(0,{s2},{sig})'] = (gens, [other, x[sig], w[sig]])
for name, (gens, inv) in patches.items():
    others = [c for c in allc if c not in gens]
    sol = [s for s in sp.solve(eqs, others, dict=True) if s.get(lam, 1) != 0][0]
    bad = []
    for c in others:
        e = sp.factor(sol[c])
        num, den = sp.fraction(e)
        if any(sp.degree(den, g) > 0 for g in gens if g not in inv):
            bad.append((c, e))
    print(f"{name}: {'regular' if not bad else 'NOT regular: ' + str(bad)}")
