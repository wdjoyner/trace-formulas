# Rank-two check of the vertex decomposition

`brion_check.py` (under 2 seconds, pure Python, exact rational arithmetic) checks Lemmas 3.5A–3.5B of the revised paper for SL(3) and PGL(3). For PGL(3) the dominant cone is not unimodular in the root coordinates.

1. **Vertex terms are independent of T.** The truncated sum S(T) = Σ_{λ∈𝒜_A(T)} c(λ)ψ(λ) equals Σ_Q ψ(T_Q) R_Q, with the R_Q independent of T. This is checked for c = 1 and for Macdonald's weights c(λ) = Q_λ. The four R_Q are fitted from four values of T, and the prediction is then verified exactly on all other T in the lattice L_0.
2. **R_G is the full-cone sum.** It equals the sum over the whole dominant cone.
3. **The strict inequalities matter.** With "≤" in place of "<" in the truncation, the same R_Q no longer work.
4. **The degenerate character ψ = 1** gives a polynomial in T on L_0.

This tests the combinatorial part of Proposition 3.6 in rank two. It does not test the representation-theoretic input (Casselman's asymptotics). The rank-two check of Hypothesis (R) on the building of PGL(3) is in `../pgl3/`.
