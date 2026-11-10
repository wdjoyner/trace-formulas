# SL(2) check

`sl2_check.py` (about 2 seconds; needs NumPy; reuses the tree code in `../pgl2/`) checks, for G = SL(2, Q_3) and K = SL(2, Z_3):

1. Plancherel inversion with Macdonald's constant Q = 1 + 1/q;
2. for the unramified elliptic γ = [[0,−1],[1,0]] and the other SL(2)-class γ′ in its stable class,

       O_γ(f)  = ½ ∫ f^∨ I_st dμ + ½ f^∨(χ₀),
       O_γ′(f) = ½ ∫ f^∨ I_st dμ − ½ f^∨(χ₀),

   where χ₀ is the unramified quadratic character (z = −1);
3. the atom-free limit I = Σₙ O_γ(fₙ) Γ_χ(aₙ) misses exactly the atom ½ f^∨(χ₀);
4. for a ramified elliptic γ there is no atom.

**Why it matters.** χ₀ is a non-regular unitary character (sχ₀ = χ₀) at which the Plancherel density does *not* vanish; the unitary principal series i(χ₀) is reducible (R-group of order 2). The spectral side of the main identity therefore needs a point mass at χ₀: the 1997 statement "O_γ(f) = ∫ f^∨ I(χ,γ) dμ with I a rational function" fails for SL(2). The atom is the κ-orbital integral: Φ^κ_f(γ) = f^∨(χ₀), which is the fundamental lemma for the unit element of the Hecke algebra of SL(2). See §§4 and 6 of the revised paper.
