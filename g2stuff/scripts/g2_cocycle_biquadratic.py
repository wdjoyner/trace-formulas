"""The character kappa(t_*) for the biquadratic tori of split G_2 (paper, Section 7, Propositions 7.6D-7.6E).

Source: T. Hales, The Subregular Germ of Orbital Integrals, Ch. I, Section 5. For split G_2 the inner twist
A_sigma is trivial, and Equation I.5.3 reads
        nu^{-1} n^{-1} w_sigma^{-1}  in  N_inf N T_sigma^{w_sigma^{-1}},
where h^{-1} g = t n nu (n upper unipotent, nu lower unipotent in the 8x8 model of Section A.4).
By Hales' Remark I.5.6 the torus part is read off from leading principal minors.

Part 1. T_sigma for w_sigma = s_alpha, s_beta (Hales' Corollary I.5.4: alpha^vee(-n_alpha) etc.),
        s_zeta and -1. For -1: T_sigma^{w^{-1}} = alpha^vee(R) beta^vee(Q).
Part 2. R and Q on the beta = 3 divisor E_(0,alpha,delta) (z(alpha) = w(eps) = w(zeta) = 0) in the
        coordinates z(beta), w(gamma), w(delta), via (1.21b) and the lambda = 0 formulas after (1.22):
        R = z(alpha)^{-4} R_E (1 + O(z(alpha))),  Q = z(alpha)^{-6} Q_E (1 + O(z(alpha))).
Part 3. High-precision check of R_E and Q_E from the exact all-order relations (1.21a), with
        exact exponentials, as z(alpha) -> 0 on the patch Z_(0,alpha,delta).
Part 4. The X-part of R_E: the norm identities behind (P(X), d_alpha)_F in Proposition 7.6E.
Runs in about a minute.
"""
import sys, os
import sympy as sp
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_g2_coordinates_and_galois as V

r_names, theta, _factor, s_a, s_b = V.build_setup()
na, nb, ng, nd, ne, nz = NS = sp.symbols('n_a n_b n_g n_d n_e n_z')
n = sp.eye(8)
for rn, s in zip(r_names, NS):
    n = n * theta(rn, s)
ninv = n.inv()
t1, t2 = sp.symbols('t1 t2')
TOR = lambda x, y: sp.diag(x, y / x, x**2 / y, 1, 1, y / x**2, x / y, 1 / x)   # alpha^vee(x) beta^vee(y)


def torus_part(w):
    M = sp.expand(ninv * w.inv())
    m1, m2 = sp.factor(M[:1, :1].det()), sp.factor(M[:2, :2].det())
    D = TOR(m1, m2)
    mins = [M[:k, :k].det() for k in range(1, 9)]
    for k in range(8):
        dk = mins[0] if k == 0 else mins[k] / mins[k - 1]
        assert sp.simplify(dk - D[k, k]) == 0
    return m1, m2


print("Part 1: T_sigma^{w^{-1}} = alpha^vee(x) beta^vee(y) from principal minors")
x, y = torus_part(s_a)
assert sp.simplify(x + na) == 0 and sp.simplify(y - 1) == 0
print("  w = s_alpha:  alpha^vee(-n_alpha)   [Hales, Cor. I.5.4, with n_alpha = 1/z(W_+, alpha)]")
x, y = torus_part(s_b)
assert sp.simplify(x - 1) == 0 and sp.simplify(y + nb) == 0
print("  w = s_beta:   beta^vee(-n_beta)")
x, y = torus_part(s_b * s_a * s_b * s_a * s_b)
print("  w = s_zeta:   alpha^vee(%s) beta^vee(Q)" % sp.factor(x))
w0 = (s_a * s_b) ** 3
assert sp.simplify(w0 * TOR(t1, t2) * w0.inv() - TOR(t1, t2).inv()) == sp.zeros(8, 8)
R, Q = (sp.expand(v) for v in torus_part(w0))
assert sp.expand(y - Q) == 0
print("  w = -1:       alpha^vee(R) beta^vee(Q) with")
print("     R =", R)
print("     Q =", Q)

print("\nPart 2: leading behavior on E_(0,alpha,delta)")
a, b, zA, zB, wg, wd, we, wz = sp.symbols('a b zA zB wg wd we wz')
g_, d_, e_, z_ = a + b, 2 * a + b, 3 * a + b, 3 * a + 2 * b
Z1, Z2, Z3 = a * zA, b * zB, g_ * zA / (1 + b * wg)
NA, NB, NG = 1 / Z1, 1 / Z2, 1 / (Z2 * Z3)
ND, NE, NZ = sp.symbols('ND NE NZ')
sol = sp.solve([
    sp.Eq(wd, (d_ * ND + 2 * a / (Z1 * Z2 * Z3)) * Z1**2 * Z2 / (a**2 * b)),
    sp.Eq(we, (e_ * NE + 3 * a * ND / Z1) * Z1**3 * Z2 / (a**3 * b)),
    sp.Eq(wz, (z_ * NZ - 3 * a * NG**2 / Z1 - 3 * a * ND / (Z1 * Z2) + b * NE / Z2 + 3 * g_ * ND / (Z2 * Z3))
          * Z1**3 * Z2**2 / (a**3 * b**2)),
], [ND, NE, NZ], dict=True)[0]
sub = {na: NA, nb: NB, ng: NG, nd: sol[ND], ne: sol[NE], nz: sol[NZ]}
F1 = 1 + b * wg + a * z_ * wd          # 1 + beta w(gamma) + alpha zeta w(delta)
F2 = 1 + b * wg + g_ * e_ * wd         # 1 + beta w(gamma) + gamma eps w(delta)
lead = {}
for name, P, k in (('R', R, 4), ('Q', Q, 6)):
    PE = sp.together(P.subs(sub).subs({we: 0, wz: 0}) * zA**k)
    val = sp.factor(sp.simplify(PE.subs(zA, 0)))
    assert val != 0 and sp.simplify(sp.limit(PE, zA, 0) - val) == 0
    lead[name] = val
    print("  %s_E =" % name, val)
assert sp.simplify(lead['R'] - F1 * F2 / (a * g_ * d_**2 * e_ * z_ * zB**2)) == 0
print("  R_E = F1 F2 / (alpha gamma delta^2 eps zeta z(beta)^2),  F1 = 1 + beta w(gamma) + alpha zeta w(delta),")
print("                                                          F2 = 1 + beta w(gamma) + gamma eps w(delta)")

print("\nPart 3: exact check with exponentials, z(alpha) -> 0 on Z_(0,alpha,delta)")
mp.mp.dps = 60
Rf = sp.lambdify(NS, R, 'mpmath'); Qf = sp.lambdify(NS, Q, 'mpmath')
LR = sp.lambdify((a, b, zB, wg, wd), lead['R'], 'mpmath'); LQ = sp.lambdify((a, b, zB, wg, wd), lead['Q'], 'mpmath')


def exact_ns(A, B, ZB, WG, WD, XD, XE, XZ, s):
    lam = XD * s**2 * ZB / WD
    xa, xb, xg = lam / s, lam / ZB, lam * WG / (s * ZB)
    Ai, Bi = mp.e**(-lam * A), mp.e**(-lam * B)
    Gi, Di, Ei, Zi = Ai * Bi, Ai**2 * Bi, Ai**3 * Bi, Ai**3 * Bi**2
    NA_ = xa / (1 - Ai); NB_ = xb / (1 - Bi); NG_ = (xg + Bi * (1 - Ai) * NA_ * NB_) / (1 - Gi)
    ND_ = (XD - 2 * Ai * Bi * (1 - Ai) * NA_ * NG_ - Bi * (1 - Ai)**2 * NA_**2 * NB_) / (1 - Di)
    NE_ = (XE - 3 * Ai**2 * Bi * (1 - Ai) * NA_ * ND_ + 3 * Ai * Bi * (1 - Ai)**2 * NA_**2 * NG_
           + Bi * (1 - Ai)**3 * NA_**3 * NB_) / (1 - Ei)
    NZ_ = (XZ + 3 * Ai * Bi * (1 - Ai) * (2 - Gi) * NA_ * NG_**2 + 3 * Ai**2 * Bi * (1 - Ai) * NA_ * NB_ * ND_
           - Ai**3 * Bi * (1 - Bi) * NB_ * NE_ - 3 * Ai**2 * Bi * (1 - Gi) * NG_ * ND_
           - 3 * Bi * (1 - Ai)**2 * (Ai + Gi - 1) * NA_**2 * NB_ * NG_ - Bi * (1 - Ai)**3 * (1 + Bi) * NA_**3 * NB_**2) / (1 - Zi)
    return NA_, NB_, NG_, ND_, NE_, NZ_


for pt in [('0.7', '-1.3', '2.1', '0.4', '-0.9', '1.7', '0.3', '-2.2'), ('3', '5', '-0.5', '2', '0.25', '-1', '4', '0.6')]:
    pt = [mp.mpf(v) for v in pt]
    s = mp.mpf('1e-15')
    n6 = exact_ns(*pt, s)
    rR = Rf(*n6) * s**4 / LR(*pt[:5]); rQ = Qf(*n6) * s**6 / LQ(*pt[:5])
    assert abs(rR - 1) < mp.mpf('1e-12') and abs(rQ - 1) < mp.mpf('1e-12')
    print("  point %s: ratios exact/predicted = %s, %s" % ([mp.nstr(v, 3) for v in pt], mp.nstr(rR, 16), mp.nstr(rQ, 16)))

print("\nPart 4: X-parts. N_{L/F} acts on root values through s_alpha.")
s_alpha = {a: -a, b: 3 * a + b}          # s_alpha on root values: alpha -> -alpha, beta -> eps
Nm = lambda expr: sp.factor(expr * expr.subs(s_alpha, simultaneous=True))
P = sp.expand(b * g_ * d_ * e_)
assert sp.simplify(Nm(a * z_) + a**2 * z_**2) == 0
assert sp.simplify(Nm(g_ * e_) - P) == 0
assert sp.simplify(Nm(d_**2) - (g_ * d_)**2) == 0
print("  N(alpha zeta) = -alpha^2 zeta^2,  N(gamma eps) = beta gamma delta eps = P,  N(delta^2) = (gamma delta)^2")
print("  gamma delta is Galois-invariant (s_alpha: gamma <-> delta; s_zeta, -1: gamma -> -delta, -gamma).")
denQ = sp.fraction(sp.factor(lead['Q']))[1]
print("  denominator of Q_E:", denQ, "-> X-part has trivial symbol (P, zeta^2, (gamma delta)^2 lie in F).")
print("\nALL CHECKS IN g2_cocycle_biquadratic.py PASSED.")
