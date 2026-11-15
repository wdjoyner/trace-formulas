"""Independent exact shell-sum checks for g2stuff Draft 6 (2026-11-15).

Scope: algebra and meromorphic continuation of explicitly defined local
Mellin integrals. NOT a proof of Langlands-Shelstad principal-value
compatibility or of X_3. No files from the repository are imported.
Requires SymPy, runs with ordinary Python 3.
"""
import sympy as sp

q, z = sp.symbols('q z', positive=True)
S = sp.symbols('S', positive=True)
w = sp.symbols('w')
G = lambda x: x/(1-x)

# A shell v(y)=k has measure (1-1/q) q^{-k}.
exterior = (1-1/q)*G(q**(1-z))
assert sp.simplify(exterior.subs(z,0) + 1) == 0

# Ordinary convergent compact-torus integral (quadratic nonsplit cases).
I_s_unram = 1 + (1-1/q)*G(1/q)
I_s_ram = (1-1/q) + 1 + (1-1/q)*G(1/q)
assert sp.simplify(I_s_unram-(q+1)/q) == 0
assert sp.simplify(I_s_ram-2) == 0

# Quadratic projective-line factor. Under xi -> 1/xi, dx dy/y^2 is invariant.
# Unram: p_K = p OF + sqrt(d) p OF. Ram: p_K = p OF + sqrt(d) OF.
Z_00 = (1-1/q)/(1-q**(1-z))
Z_11 = (1/q)*(1-1/q)*q**(1-z)/(1-q**(1-z))
Z_10 = (1/q)*Z_00
I_xi_unram = sp.factor((Z_00+Z_11).subs(z,0))
I_xi_ram = sp.factor((Z_00+Z_10).subs(z,0))
assert sp.simplify(I_xi_unram+2/q) == 0
assert sp.simplify(I_xi_ram+(q+1)/q**2) == 0

# The cyclic cubic projective-line factor has 3 variables a,b,c.
# Unram: discriminant D is a unit times p^{3min(v(b),v(c))}.
# Ram:  D/Delta_K is a unit times (b^3 - pi*u*c^3).
# The first chart uses a,b,c in OF; the inverted second chart uses p_K.
Zc_unram = (1-q**(-2))/(1-q**(1-3*z))
I_P1_unram = sp.factor((Zc_unram + q**(-1)*(1-q**(-2))*q**(1-3*z)/(1-q**(1-3*z))).subs(z,0))
Zc_ram = (1-q**(-1))*(1+q**(-z))/(1-q**(1-3*z))
I_P1_ram = sp.factor(((1+1/q)*Zc_ram).subs(z,0))
assert sp.simplify(I_P1_unram+2*(q+1)/q**2) == 0
assert sp.simplify(I_P1_ram+2*(q+1)/q**2) == 0

# Unramified cubic character omega_F(pi)=w (w^2+w+1=0).
B1_u = (1-1/q)*(G(w*S/q)+G(1/(q*S**4))+G(w**2*q*S**3))+(1-2/q)
B2_u = -q/(q+1)+(1-2/q)+(1-1/q)*(G(w/q**2)+G(w**2/q))
B1u_0 = sp.together(B1_u.subs(S,1))
B1u_prime = sp.together(sp.diff(B1_u,S).subs(S,1))
prod_u = sp.together(B1u_prime*B2_u-12/(q**2-1))
minimal = w**2+w+1
for expr in (B1u_0, prod_u):
    num, den = sp.fraction(sp.factor(expr))
    remainder = sp.rem(sp.Poly(num, w),sp.Poly(minimal,w))
    assert remainder.is_zero, (expr,remainder)

# Tamely ramified cubic character is a nontrivial residue character.
# Shell integrals with v != 0 vanish by finite-field orthogonality.
B1_r = -1/q+(1-1/q)*G(1/(q*S**4))
B1r_0 = sp.simplify(B1_r.subs(S,1))
B1r_prime = sp.simplify(sp.diff(B1_r,S).subs(S,1))
B2r_div_chi2 = -q/(q+1)-1/q
assert B1r_0 == 0
assert sp.simplify(B1r_prime+4/(q-1)) == 0
assert sp.simplify(B2r_div_chi2+(q**2+q+1)/(q*(q+1))) == 0

# Combine independent shell factors. Chi_3(2) has modulus one.
JQ_u = -sp.Rational(1,4)*(q-1)/q*12/(q**2-1)
JQ_r_mag = sp.Rational(1,4)*(q-1)/q*(-B1r_prime)*(-B2r_div_chi2)
assert sp.simplify(-JQ_u-3/(q*(q+1))) == 0
assert sp.simplify(JQ_r_mag-(q*q+q+1)/(q*q*(q+1))) == 0
assert sp.simplify((-I_P1_unram)*(-JQ_u)-6/q**3)==0
assert sp.simplify((-I_P1_ram)*JQ_r_mag-2*(q*q+q+1)/q**4)==0

# Quadratic Hilbert-factor I_t via finite-field Legendre sum, exact for Q_p.
for p in (5,7,11,13,17,19,23,31):
    eps = next(a for a in range(2,p) if sp.legendre_symbol(a,p)==-1)
    assert sum(sp.legendre_symbol((a*a-eps)%p,p) for a in range(p)) == -1
    It_ram = -sp.Rational(2,p)
    It_unram = -sp.Rational(p+1,p*p)
    C10 = sp.sqrt(p)*It_ram*2*I_xi_ram.subs(q,p)
    C01 = sp.sqrt(p)*It_ram*I_s_unram.subs(q,p)*I_xi_unram.subs(q,p)
    C11 = p*It_unram*2*I_xi_ram.subs(q,p)
    assert sp.simplify(C10-4*(p+1)/p**sp.Rational(5,2))==0
    assert sp.simplify(C01-4*(p+1)/p**sp.Rational(5,2))==0
    assert sp.simplify(C11-2*(p+1)**2/p**3)==0

print('All independent shell-sum identities verified symbolically.')
print('Quadratic I_xi: unram =',I_xi_unram,'; ram =',I_xi_ram)
print('Cubic I_P1(K): both =',I_P1_unram)
print('Cubic unram B1(1)=0, B1\'(1)*B2(1)=12/(q^2-1).')
print('Cubic tame ram B1\'(1)=',B1r_prime,'; B2(1)/chi_3(2)=',sp.factor(B2r_div_chi2))
print('Claim 8.3H magnitudes recover 6/q^3 and 2(q^2+q+1)/q^4 under stated regularization.')
print('WARNING: LS principal-value compatibility / geometry NOT checked.')