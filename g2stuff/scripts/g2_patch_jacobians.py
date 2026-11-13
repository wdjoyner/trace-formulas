# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Check the patch formulas of Section 3 and the Igusa forms of Section 4 (and (8.1), (8.4), (8.5)).

Coordinates on Z: lam w(rho) = x(rho) z(a)^{m_a} z(b)^{m_b}, w(simple) = 1.
omega_Z = d lam ^ dx(a) ^ dx(b) ^ dx(g) ^ dx(d) ^ dx(e) ^ dx(z).
"""
import sympy as sp

za, zb, lam = sp.symbols('z_a z_b lam')
x = {r: sp.Symbol('x_' + r) for r in 'abgdez'}
w = {r: sp.Symbol('w_' + r) for r in 'gdez'}
m = {'a': (1, 0), 'b': (0, 1), 'g': (1, 1), 'd': (2, 1), 'e': (3, 1), 'z': (3, 2)}


def rel(r):  # lam * w(r) = x(r) z_a^ma z_b^mb
    ma, mb = m[r]
    return x[r] * za**ma * zb**mb, (w[r] if r in w else 1)


def express(gens, solve_for):
    """Solve relations for the non-generator coordinates in terms of generators."""
    allc = [lam, za, zb] + list(x.values()) + list(w.values())
    eqs = []
    for r in m:
        lhs, wr = rel(r)
        eqs.append(sp.Eq(lam * wr, lhs))
    sol = sp.solve(eqs, solve_for, dict=True)
    return sol


def check_patch(name, gens):
    others = [c for c in [lam, za, zb] + list(x.values()) + list(w.values()) if c not in gens]
    sols = express(gens, others)
    sols = [s for s in sols if all(s[c] != 0 for c in [lam])]
    s = sols[0]
    print(f"\n== {name}: generators {gens}")
    for c in others:
        print(f"   {c} = {sp.factor(s[c])}")
    return s


# Section 3 patch formulas
p1 = check_patch('x(a)!=0', [x['a'], x['b'], zb, x['g'], x['d'], x['e'], x['z']])
p2 = check_patch('x(b)!=0', [x['a'], x['b'], za, x['g'], x['d'], x['e'], x['z']])
p3 = check_patch('x(g)!=0', [x['a'], x['b'], x['g'], w['g'], x['d'], x['e'], x['z']])
p4 = check_patch('w(z)!=0', [za, zb, w['g'], w['d'], w['e'], w['z'], x['z']])
p5 = check_patch('z(a)!=0, x(e)!=0', [za, zb, x['b'], w['g'], w['d'], w['e'], x['z']])


def omega_on(gens, sub):
    funcs = [lam] + [x[r] for r in 'abgdez']
    F = [sp.sympify(f).subs(sub) if f not in gens else f for f in funcs]
    J = sp.Matrix([[sp.diff(f, g) for g in gens] for f in F])
    return sp.factor(J.det())


print("\n==== Igusa forms omega_Z / (d gens) on fundamental patches ====")
cases = {
    'Z_{a,b}': [lam, x['a'], x['b'], x['g'], x['d'], x['e'], x['z']],
    'Z_a': [lam, x['a'], zb, x['g'], x['d'], x['e'], x['z']],
    'Z_b': [lam, za, x['b'], x['g'], x['d'], x['e'], x['z']],
    'Z_(0,a,g)': [za, zb, x['g'], w['g'], x['d'], x['e'], x['z']],
    'Z_(0,a,d)': [za, zb, w['g'], w['d'], x['d'], x['e'], x['z']],
    'Z_(0,a,e)': [za, zb, w['g'], w['d'], w['e'], x['e'], x['z']],
    'Z_(0,a,z) = Z_(0,b,z)': [za, zb, w['g'], w['d'], w['e'], w['z'], x['z']],
    'Z_empty (Lemma 3.5 corrected: lam, z, all w)': [lam, za, zb, w['g'], w['d'], w['e'], w['z']],
}
for name, gens in cases.items():
    others = [c for c in [lam, za, zb] + list(x.values()) + list(w.values()) if c not in gens]
    s = express(gens, others)
    s = [t for t in s if t.get(lam, 1) != 0][0]
    print(f"{name}: det = {omega_on(gens, s)}")

# Paper's Lemma 3.5 generators for S1 = Delta: lam, x(a), x(b), w(g..z).  Are the x's regular?
gens = [lam, x['a'], x['b'], w['g'], w['d'], w['e'], w['z']]
others = [c for c in [lam, za, zb] + list(x.values()) + list(w.values()) if c not in gens]
s = express(gens, others)[0]
print("\nLemma 3.5 as printed, S1 = Delta: x(g) =", sp.factor(s[x['g']]), "(not regular at lam = 0)")

# ---- Section 8: E = E_(0,b,z), divisor z_b = 0 on the w(z)!=0 patch ----
print("\n==== Section 8 checks ====")
gens = [za, zb, w['g'], w['d'], w['e'], w['z'], x['z']]
others = [c for c in [lam, za, zb] + list(x.values()) + list(w.values()) if c not in gens]
s = [t for t in express(gens, others) if t.get(lam, 1) != 0][0]
detw = omega_on(gens, s)
unit = sp.factor(s[lam] / zb**2)           # lam = unit * z_b^2
omegaE = sp.factor(detw / zb**7 * unit**(-4))  # residue-type form, beta = 4: omega/(z_b^{b-1}) * unit^{-beta}
print("lam =", s[lam], "; unit =", unit)
print("omega_E coefficient (in dz_a dw_g dw_d dw_e dw_z dx_z):", omegaE)
# (8.4): omega_O3 = d x(a) d x(g) d x(d) / lam^2 in the variables z_a, w_g, w_d (others fixed)
J = sp.Matrix([[sp.diff(s[x[r]], v) for v in (za, w['g'], w['d'])] for r in 'agd'])
print("(8.4) coefficient dx_a dx_g dx_d / lam^2 =", sp.factor(J.det() / s[lam]**2))
