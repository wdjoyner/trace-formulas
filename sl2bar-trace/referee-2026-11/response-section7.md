# Response to the referee report on Section 7 (ChatGPT, November 2026)

Report: [`report-chatgpt-section7.md`](report-chatgpt-section7.md), on Section 7 of `revised/sl2bar-trace-2026.pdf` as of 2026-11-11 (102 pages).
Response by D. Joyner and Claude. Statement numbers are those of the revised `sl2bar-trace-2026.pdf` (105 pages); no statement or equation number of the refereed draft has changed.

We thank the referee. The report confirms the computations of Section 7 and finds one error of statement, four gaps of justification and several places where a citation claimed more than it gives. We accept all of them. Each claim of the report that we could check was checked before acting on it; where we could not check a source, this is said below.

## Summary

| Report item | Verdict | Action |
|---|---|---|
| E1 (pt 20). Theorem 7.13(c): "every term is an eigendistribution" | Correct, an error of statement | Part (c) reworded; it now says the sums are in general not eigendistributions and that S_ell is stable, not equivariant |
| G1 (pts 2, 3). Finite-rank argument and uniform Gauss-shell lemma | Accepted | Two-lattice argument written out; new Lemma 7.5′ with proof, dyadic case included |
| G2, C1 (pt 4). Archimedean kernel and trace; reduction to c ≠ 0 | Accepted | The citation is replaced by a direct proof that K_f is a Schwartz function; the reduction is written out |
| J1 (pt 5). Thomas's Theorem 1C is up to sign | Correct | The text now says the comparison does not confirm the sign |
| pt 5. Comparison with [Th13, Theorem D]; "changes ψ by a square class" | Correct | Reworded as the referee asks; the square-class sentence is removed |
| pt 7, R1. Display the cancellation of log|a| | Accepted | New display in the proof of Lemma 7.8(c) |
| J2 (pt 8). Lemma 7.8(d) is a compatibility, not an existence statement | Correct | Said in Remark 2026.18 |
| G3, C2, C3 (pt 9). (N5) unproved; [GS16] excludes dyadic places | Correct; we verified the statement about [GS16] | Remark 2026.18 rewritten: the needed theorem is formulated as a problem, [GS16] is no longer cited in support, new reference [Sz16] |
| G4, C4 (pts 10–12). Packets: conventions and sources | Accepted | Conventions stated; the general stable-sum statement is now marked as expected, not known to us in this form; [GS12, §5] and [Ad, §15] cited |
| R4 (pt 13). A worked dyadic example | Accepted | New Example 7.A(e), the referee's example |
| J3 (pts 16, 21). Li's ½ + ½: coefficients, not distributions | Correct | Reworded in the list of results, after Theorem 7.7 and after Proposition 7.12 |
| pt 17. PID hypothesis in the headline of Proposition 7.10 | Accepted | Added |
| R4 (pt 18). Table of the four values in Example 7.E | Accepted | Added |
| pt 19. Dependency on (N5) before Theorem 7.13 | Accepted, and the theorem improved | New paragraph; (N5) is now assumed only in part (c) |
| R2. Equivariance, stability, transfer | Accepted | New paragraph at the start of Section 7 |
| R3. Regular set versus all test functions | Already in place | No change beyond G1, G2 |

## 1. The error

**E1, point 20 (Theorem 7.13(c)).** The referee is right. Part (c) listed the characters of the individual distributions J^st(γ,·), I_A(a(t),·), J^κ_unip(z,·), but its first sentence said "every term of (a)", and S_ell and the sums over t and κ are terms of (a). They are sums over indices with different characters. Part (c) now speaks of "the individually indexed distributions occurring in (a)", and adds that the displayed sums are in general not eigendistributions and that S_ell is stable for the twisted action and not an eigendistribution for the ordinary one. No computation changes.

## 2. Proposition 7.5

**Points 2, 3 (finite places).** Both requests are met.
- The two-lattice argument is in the proof: a vector fixed by K′ is supported in a bounded set because the (n(u),1) act by ψ(uξ²); its Fourier transform is too, because the conjugates by (w,1) lie in K′; so it is constant modulo a lattice. One detail beyond the report: the conjugate of (n(u),1) by (w,1) lies over K_m but might differ from the section by a sign; the sign is a character of u, hence trivial for u ∈ 2ϖ^m𝒪, and the proof uses those u. The finite-rank decomposition and the formula for the trace are written out.
- **New Lemma 7.5′.** If ψ is trivial on ϖ^{n₀}𝒪 and not on ϖ^{n₀−1}𝒪, and e = ord(2), the integral of ψ(aξ²) over the shell ord(ξ) = −j vanishes when 2j ≥ ord(a) − n₀ + 2 + 2e. The proof is the substitution ξ ↦ ξ(1+u) with u ∈ ϖ^r𝒪, r = n₀ − 1 − m − e, m = ord(a) − 2j. The bound depends on a only through ord(a), which gives the uniformity. For ℚ₂ it gives stabilization from M = 1 for a = 1 and from M = 2 for a = 2, the referee's two observations, and the values 1+i and √2(1+i) agree with ours. The lemma is numbered 7.5′ so that the numbers of the report stay valid.

**Point 4 (archimedean places).** We agree that "smooth vectors are Schwartz functions" does not give a Schwartz kernel in two variables, and that [Mak] was not a reference for it. We could not open [Th08] beyond its abstract and statements, so we did not verify the pointer to its §12.2 and do not cite it. Instead the proof now shows directly that K_f is a Schwartz function: in the coordinates (α,c,d) on {c ≠ 0}, K_f(ξ,η) is the integral over c of the partial Fourier transform of a compactly supported smooth function, evaluated at (ξ²/c, η²/c), times ψ(−2ξη/c). What is still quoted is the standard fact that an operator with a Schwartz kernel is of trace class with trace the integral over the diagonal. The reduction to c ≠ 0 is written out as the referee describes.

**Point 5.** Agreed on all three counts. (i) The text now says that [Th08, Theorem 1C], being stated up to sign, confirms the absolute value and the Weil index and says nothing about the sign (−c, D⁻)_v, which rests on our computation. (ii) For [Th13, Theorem D] it says that the two characters stand in the same relation and that no equality between the coordinate factors was verified. (iii) The sentence about a change of ψ by a square class is removed.

## 3. Lemma 7.8 and the condition (N5)

**Points 6–8.** The referee's independent derivation agrees with ours, including the role of |a|^{−λ}. The scalar cancellation is now one displayed equation, with the notation (H̃ = −½ log|a| − u′, ρ̇/ρ = d_a + log|a|) stated just before it. Remark 2026.18 now says that part (d) is a necessary compatibility and not an existence statement.

**Point 9.** We verified the referee's statement about Goldberg–Szpruch: the paper assumes that the residue characteristic is prime to n ([arXiv:1411.6134](https://arxiv.org/abs/1411.6134), introduction). The earlier draft said that (N5) is what "one expects from the local coefficients of [Sz09, GS16]"; for the dyadic places that sentence had no basis in [GS16], and it is removed. Remark 2026.18 now formulates what is needed as a problem: for every local field of characteristic 0, including the dyadic ones, factors of the form r_v(χ_ψχ, λ) = C_v(χ)·F_v(χ², λ) that satisfy (N1)–(N4). It says that the literature we know does not contain this, and what [Sz09] and [GS16] do and do not give. One addition: Szpruch's later preprint "On Shahidi local coefficients matrix" ([arXiv:1609.08122](https://arxiv.org/abs/1609.08122), new reference [Sz16]) computes Plancherel measures without the assumption on the residue characteristic when 4 ∤ n. We have read only its abstract and have not worked out what it gives for (N5); the remark says so.

(N5) remains a hypothesis. We did not find a proof and did not find a counterexample.

## 4. The packets after Proposition 7.12

**Points 10–12.** The paragraph now states its conventions: the packets are those of the theta correspondence for the character ψ′, with π⁺ the lift from PGL(2) and π⁻ the lift of the Jacquet–Langlands transfer from the anisotropic SO(3). The general statement (the stable combination of a cuspidal packet is the sum) is now given as what one expects, with the remark that we know no reference stating it for all packets in terms of the action ⋆ and that it is the local character identity of the endoscopic transfer [Li19]. The two cases checked directly remain, with the sources the referee names: [GS12, §5] for the Steinberg packet and [Ad, §15] for the real discrete series.

Two remarks on sources.
- The referee reports from Gan–Savin that the special representation is the lift of the trivial representation of the anisotropic SO(3) and that the odd Weil representation is the lift of the Steinberg representation. This agrees with the tower argument (both r⁺ and r⁻ come from O(1), hence both lift to the split SO(3)). The text now says which member is which. Our draft had not labeled them, so nothing was wrong, but our own working assumption had been the opposite labeling.
- The pinpoint references [GS12, §5] and [Ad, §15, (15.7)–(15.8)] are the referee's. We did not open either paper in this round. The multiplicity statements are now attributed to [Wa80, Wa91] "as recounted in [GS12]", and the text says we have not checked them against the originals.

## 5. Lemmas 7.1–7.3, Lemma 7.6, Theorem 7.7, Proposition 7.10

**Point 13.** The referee's example (γ with entries 3/5, ∓4/5 and h with det h = 2, (2,16/5)₂ = −1) is now Example 7.A(e), credited, with the signs at ∞ and at 5 added: +1 and −1, in agreement with the product formula. It is in the script.

**Points 14, 15.** No change needed.

**Point 16 (Li's Théorème 5.2.6).** Agreed. The text after Theorem 7.7 now says that the comparison is one of the decomposition and of the coefficients only, that Li's terms are stable distributions on SO(3) applied to transfers and ours are distributions on the cover, and that matching them requires the transfer and its normalization. The same change is made in the list of results at the start of the section and after Proposition 7.12 ("the same two-term form" in place of "exactly the shape").

**Points 17, 18.** The PID hypothesis is in the first line of Proposition 7.10. Example 7.E has the table of the four values, 1.57726, 0.16864, −0.15668, −0.31886, each with its sign pattern and a representative class; they add up to γ_E + log 2 = 2c_S. The referee's two values agree with ours to all digits given.

## 6. Theorem 7.13

**Point 19.** The dependency map is a new paragraph before the theorem. Writing it showed that parts (a) and (b) do not use (N5) at all, so the hypothesis is now made only in part (c). This is a small improvement of the theorem over the refereed draft.

**Point 21, R2.** The section now begins with a paragraph that separates equivariance under ordinary conjugation, stability under the twisted action, and endoscopic transfer, and says which of the three is proved for which terms.

## 7. Points where we differ from the report, or that remain open

- We differ on nothing of substance.
- **Open:** the existence of normalizing factors with (N1)–(N5) at the dyadic and ramified places (G3). This is the one hypothesis of Section 7.
- **Open:** a reference, or a proof, for the stable-sum statement for all cuspidal packets (G4). It is not used in any proof.
- **Not verified by us:** the pinpoint citations to [GS12] and [Ad] taken from the report; the content of [Th08, §12.2]; the normalizations of [Th08], [Th13] against ours; the original papers [Wa80], [Wa91].
- The script `checks/sec7_n2_check.py` has 35 checks (33 before): Lemma 7.5′ at 2, 3, 5 with the two dyadic values, and Example 7.A(e); the check of Example 7.E now includes the table.
