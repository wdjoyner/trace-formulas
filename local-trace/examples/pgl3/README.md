# PGL(3): a rank-two test of Hypothesis (R)

This directory holds the computation behind Appendix A of the revised paper.

* `building.py` handles the Bruhat–Tits building of PGL(3, Q_p). A vertex is a homothety class of lattices, stored in a canonical Hermite normal form. The vector distance between two vertices is read off from elementary divisors. The file also enumerates balls around the base vertex.
* `pgl3_check.py` runs all the checks below in about 6 seconds (needs numpy and sympy). `python3 run_checks.py` at the top of the repository runs it together with the other checks.

The element γ is the companion matrix of a cubic that is irreducible mod p. So γ generates the unramified cubic extension, it has depth 0, and its only fixed vertex is the base vertex v₀.

| | Result | How it is established |
|---|---|---|
| 1 | Displacement table N(λ, μ) = #{v : d(v₀,v) = λ, d(v,γv) = μ}, closed form (A.2) | Matches the building for every v with l₁ ≤ 6 when q = 2 (86 017 vertices) and every v with l₁ ≤ 4 when q = 3 (62 193 vertices). The check script redoes this at radius 4 (q = 2) and radius 3 (q = 3). Not proved. The table is unchanged for three other elements of γK₁. |
| 2 | Orbital integrals O_γ(f_ν), counted on the building | Agree with (A.2) |
| 3 | T-independent part I(χ, γ), closed form (A.4) | Exact (sympy), given (A.2). It has double poles only on the root walls, and I·ρ is smooth and positive |
| 4 | ∫ f_ν^∨ I dμ = O_γ(f_ν) | Numerically exact (error about 1e-13) for 12 values of ν, q = 2 and q = 3. **No singular part.** |
| 5 | The truncated kernel I^T is one exponential polynomial in T on the whole cone, as (4.7A) predicts | It has 19 frequencies, all of the form T ↦ wT − w′T. Its constant term is (A.4). The individual Weyl terms are only piecewise exponential polynomials (they switch along ⟨T,α₁⟩ = ⟨T,α₂⟩); the switching cancels in the sum. |
| 6 | **Hypothesis (R), as stated, fails** | Some oscillatory coefficients times ρ have simple poles along the non-root subtori z_i³ = 1, where ρ ≠ 0. These coefficients cancel in pairs whose frequencies coincide on those subtori. |

So for PGL(3) the conclusion of Theorem 4.5(b) holds for this γ, while its hypothesis (R) does not. In rank two the singular pieces are Dirichlet kernels across a one-dimensional subtorus H, multiplied by a character of H that moves with T. Riemann–Lebesgue along H makes them tend to zero. In SL(2) the set H is a point, and this mechanism leaves an atom instead.
