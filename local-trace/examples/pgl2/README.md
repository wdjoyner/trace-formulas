# PGL(2) worked example

`pgl2_worked_example.pdf` computes I(χ,γ) in closed form for G = PGL(2) and every type of regular elliptic γ (unramified of depth r, ramified unit of depth r, ramified of odd valuation).

`pgl2_check.py` verifies, for q = 3:

1. elliptic orbital integrals, by counting vertices v of the Bruhat–Tits tree with d(v, γv) = n;
2. Plancherel inversion with Macdonald's constant Q = 1 + 1/q;
3. the spectral identity O_γ(f) = ∫ f^∨ I(χ,γ) dμ for n ≤ 7;
4. the exact truncation statement.

Run with `python3 pgl2_check.py` (about 3 seconds; needs NumPy).
