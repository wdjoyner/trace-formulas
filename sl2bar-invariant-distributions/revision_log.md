# Revision log: preservation-first revision, Draft 2

Paper: *A hitch-hiker's guide to genuine invariant distributions on metaplectic covers of SL(2) over a p-adic field* (D. Joyner, 1994).
Draft 2 prepared by Claude (Anthropic), November 24, 2026, from Draft 1 (ChatGPT, November 2026). Theorem numbers in this log are Draft 2 numbers unless marked "1994"; Section 9 has the concordance.
Files: `sl2bar-invariant-distributions.tex` and `.pdf` (60 pages), `conjecture_status.md`, `scripts/`.

**Location (November 24, 2026).** At the author's direction Draft 2 now sits at the top of `sl2bar-invariant-distributions/` and replaces the manuscript that was there, the "Draft 3" synthesis of the 1994 notes with the 2001 article, together with its LaTeX revision log. The file was renamed from `sl2bar-invariant-distributions-2026.tex` to `sl2bar-invariant-distributions.tex`, and the subdirectory `preservation-revision/` was removed. The replaced files are in the git history (last commit containing them: `28667a8`). Where this log says "the other path" or "the synthesis" it means that replaced manuscript. The only change to the paper in this step is the bibliography entry and one sentence in Section 9 that describe the synthesis as an earlier revision.

This log holds everything that the style guide keeps out of the paper: what was wrong in earlier versions, what changed, how each statement was verified, which citations were checked and how, the numbering concordance, and the agenda for Draft 3.

## 1. What I read, and what I did not

Read in full:

- Draft 1 of this path (then at `preservation-revision/sl2bar-invariant-distributions-2026.tex`), its README and revision log. The attached file was byte-identical to the repository copy.
- Draft 3 of the other path (the file then named `sl2bar-invariant-distributions.tex` at the top of the directory), and the referee report `referee-2026-11/report-claude.md`.
- `joyner-math-paper-style-guide.md` (Draft 2 of the guide, from the repository; it was not attached to the request).
- The proof of the image theorem for split orbital integrals in `sl2bar-unitary-dual/revised/sl2bar-unitary-dual-2026.tex`.

Skimmed (introductions, main statements, READMEs): `sl2bar-characters`, `sl2bar-trace`, `sl2bar-unitary-dual`, `metaplectic-jl`.

Not read: the 1994 source in `original-1994/` beyond what Draft 1 reproduces, the `mult-one` directory, and the body of the `metaplectic-jl` book.

**Caveat on the literature.** I consulted the papers listed in Section 7 through a web-fetch tool that returns an automated extract of the arXiv version, not the PDF itself. Theorem numbers are therefore those of the arXiv versions, and I could not obtain page numbers. Where the request asked for theorem numbers and page references, the paper gives theorem numbers only. Every such citation should be rechecked against the published version before submission.

## 2. AI usage

- ChatGPT (OpenAI): Draft 1. Source preservation, the 62 "not verified" markers, the section of elementary corrections.
- Claude (Anthropic): Draft 2. Literature search, restatement and status of all 62 statements, the new proofs listed in Section 5, the three scripts, the exposition, this log.
- No other AI system contributed to Draft 2. No human or AI referee has read Draft 2.

The author line is unchanged (David Joyner). AI credit is in the first sentence of the abstract and in the Acknowledgments.

## 3. Substantive changes from Draft 1

Structure. All six original sections are kept, with their titles and all of their statements in the original order. Statements are renumbered consecutively within each section (Section 9). Draft 1's Section 7 (corrections) is dissolved: its content moved to where it belongs (Proposition 4.4, the proof of Theorem 5.10(a), Propositions 6.1, 6.2, 6.5). New Sections 7 to 11: status and dependency diagram, worked examples, connections, open problems, summary. Unnumbered sections: literature review, notation table, glossary, acknowledgments.

Section 1. New statement of main results, restrictions on n and p, numbering convention. Example 1.1.

Section 2. The Hilbert symbol properties (H1) to (H5) are stated once. New: Proposition 2.7 (center of the covering torus for every p, index, Lagrangians), Lemma 2.12 (Weyl action), Lemma 2.13 (n-th power section). Lemma 2.3(c),(e), Lemmas 2.8, 2.10, 2.15, 2.18, 2.21, Corollary 2.22 are corrected or sharpened (Section 4 below). Conjecture 2.17 of 1994 is now Theorem 2.25.

Section 3. New: Definition 3.1 (the character chi_sigma), Proposition 3.3 (Weyl-fixed data), Lemma 3.11 and Theorem 3.12 (Gindikin–Karpelevich formula, with proof), Corollary 3.13, Theorems 3.14 and 3.15 (cited inputs), Theorem 3.16 (complete reducibility, tame), Corollary 3.28, Theorem 3.29 (unitary and tempered duals, tame), Lemma 3.32 (pseudo-coefficients). The five conjectures of 1994 (3.3, 3.5, 3.13, 3.15, 3.16) are now Theorems 3.6, 3.8, 3.23, 3.25, 3.27, with stated hypotheses. Figure 1.

Section 4. The Abel transform and Phi_f are introduced. Lemma 4.9(1) is proved for p not dividing 2n. Lemma 4.14 is restated for all sigma and proved. Proposition 4.4 and Example 4.5 on kernels.

Section 5. Lemma 5.4 is now a theorem with proof (tame). The three Paley–Wiener theorems are restated on the irreducible duals with compatibility relations. Definitions 5.9, 5.13, 5.16. Corollary 5.11. "Four transforms" paragraph.

Section 6. Proposition 6.1 with the constant term. Proposition 6.2 with the product. Theorem 6.4 made conditional, Proposition 6.5 unconditional.

## 4. Corrections to earlier versions

These are the errors found in the 1994 text or in Draft 1. The paper states only the corrected mathematics.

| Item (1994 number) | Problem | Correction in Draft 2 |
|---|---|---|
| Lemma 2.3(c) | "splits over K_m for all m ≥ n" has no proof, and is doubtful for highly ramified F | Existence of m_0, with proof. Tame: m_0 = 0. The bound m ≥ n is not asserted. I expect a counterexample for F = Q_3(zeta_9), n = 3 (the Hilbert symbol is nontrivial on U_4 × U_5), but did not verify it (level 3). |
| Lemma 2.3(e) | Center called {±1} × mu_n | It is the preimage of {±1}, of order 2n. It is a direct product iff (−1,−1)_n = 1. Fails for n ≡ 2 (4) with (−1,−1)_2 = −1, e.g. Q_2, n = 2 (cyclic of order 4). Script W1. |
| Lemma 2.3(g), 2.8(f) | "largest abelian subgroup contains h(F^{×N})" | The center of the torus is exactly the preimage of h(F^{×nu}), every p (Prop. 2.7). |
| Remark after 2.3 | Vague | Centralizer of a regular a equals the torus iff a is central in the torus. |
| Lemma 2.6(a) | "the maximal subgroup" | A maximal one. Lagrangians are not unique (Q_7, n = 3 has four). The right hypothesis is p ∤ nu, which the 1994 text had. |
| Lemma 2.6(b) | O^{×N} = mu_{q−1}^d (1 + pi^{re+1} O) | False when mu_p ⊂ F. Correct: mu_{q−1}^d · U_1^{p^r}. The subgroup is isotropic but not maximal. |
| Lemma 2.7(b) | Index (q−1,d) q^{er} | Correct index is nu·|nu|^{−1} = d·p^r·q^{er}. The 1994 value misses the factor p^r = |mu_{p^r}|. Scripts W2, W3. |
| Eq. (2.9) | G(Q_p) = ∏ k_v^× | That is A(Q_p). |
| §2.1.2 | cover of G(Q_p) "is a subgroup of" the product of covers | It is a quotient of the product. |
| Lemma 2.9 | "a mod Z(G(Q_p)) is well defined" | The valuations of the torus part are well defined. |
| §2.1.3 | "(K,1) is a subgroup if p | n" | Reversed, and in any case false. For p ∤ n the subgroup is s(K), with Kubota's kappa. |
| Lemma 2.11, 2.14 | Irreducibility only, multiplicities m_i | Full Stone–von Neumann statement with dimension nu·|nu|^{−1/2}; multiplicities are 1. |
| Cor. 2.15 | Trace supported on the maximal abelian subgroup | Sharper: supported on the center, where it is d·omega. |
| Jacobson topology | "canonical surjection A^ ↪ Prim" | Surjection; topology is the pullback. |
| Lemma 2.21 | Factors written as Ind(chi^w delta^{1/2}) | Stated with the normalized Jacquet module: sigma and sigma^w. |
| Theorem 3.4, Conj. 3.5 | "chi^w = chi ⇒ reducible with two constituents" | One Weyl-fixed class (chi_sigma = 1) gives an irreducible representation. Moen proved irreducibility for alpha = 1 and only remarked on the other three. |
| Prop. 3.2(2) | "n = 2" appears twice | Assumed n = 4 in the second line. Unverified. |
| Lemma 3.11 | "I(mu^w) is the contragredient of I(mu)" | The contragredient is not genuine for n > 2. Replaced by the Hermitian dual (as in Draft 3 of the other path). |
| Conj. 3.13 | "mu(x) = |x|^s" has no meaning for a genuine character; one point | Condition chi_sigma = |·|. One point for n odd, [F^×:F^{×2}] points for n even. |
| Lemma 3.14 | Range 0 ≤ Re s ≤ 1/n, "image of J" | Re s > 0, image of T, any unitary sigma_0. |
| Conj. 3.16 | Image special and spherical; kernel non-tempered | Kernel special, not spherical; image non-tempered, spherical, unitary. "the special representation" is unique only for n odd. |
| Lemma 3.17 | Multiplicity one; "M independent of Pi" | Multiplicity m ≥ 1 allowed; the remark is flagged as unverified. |
| §3.5 | "countably many reducible unitary principal series" | Finitely many: [F^×:F^{×2}] − 1 for n odd, none for n even. |
| §4.1 | Xi defined by ∫ delta(xk)^{−1/2} dk; bounds c_1 ≤ Xi ≤ c_2(1+sigma)^N | Xi(x) = ∫ delta(kx)^{1/2} dk; bounds with q^{−m}. C_K was defined inside C_c. |
| Lemma 4.5, 4.6 | Stated with A^N and with C-bar, H-invariants | The right group is the center Z-bar. Image is C_c^∞(Z-bar)^W. |
| Lemma 4.10 | tr chi(a)^{−1}; only for chi ≠ chi^w | omega(w z w^{−1}); valid for every sigma (it is the character of the full induced representation). |
| Lemmas 5.1–5.7 | "h ∈ C_c(Pi_u) trig polynomial" for the Schwartz case too | Finite support on components; Laurent polynomials (C_c^∞) or smooth functions (Schwartz). |
| Theorem 5.8 | "regular on Pi_ad as a variety" | Pi_ad is not a variety at reducible points. Condition (PW2) on the sum over constituents. |
| Theorem 5.9 | (3) "finite Laurent series" independent of (2); "h arbitrary on the discrete part" | Complementary-series values are the continuation of the same Laurent polynomial; pi_nt and one of pi^± are determined. |
| Prop. 6.1 | T = D^m u | Needs a constant term (already noted in Draft 1). |
| Prop. 6.2, Thm 6.3 | Direct sum | Unrestricted product (already noted in Draft 1). |
| Draft 1, Section 7.2 | "radical is the two-torsion subgroup, quotient (Z/N)^2" | Correct for tame; Draft 2 proves the general statement and drops "p ∤ n" in favor of p ∤ nu. |
| Draft 1 bibliography | Flicker 1980 title "covering groups of SL(2)" | The paper is on covering groups of GL(2). |
| Draft 1 bibliography | [J2] Israel J. Math. 66 (1988) | Changed to volume 61. From memory (level 3); please confirm. |

Notation changes: N → nu (N also denoted the unipotent radical), pi → varpi for the uniformizer, K_n, U_n → K_m, U_m, chi ∈ Pi(A-bar) → sigma, I_{A_0}(chi) → I(sigma), I → T for the intertwining operator.

## 5. Original results and new results

Original (1994): every numbered statement of the 1994 manuscript is kept, in the same order. In 1994 numbering these are 2.1–2.22, 3.1–3.17, 4.1–4.10, 5.1–5.10 and 6.1–6.3. Section 9 gives their Draft 2 numbers. Seven of them were conjectures in 1994 (2.17, 3.3, 3.5, 3.13, 3.15, 3.16, 4.8) and are now theorems or propositions with stated hypotheses.

New in Draft 2 (my proofs, not refereed):

1. Proposition 2.7: center and index for every p; existence and index of Lagrangians.
2. Lemma 2.3(e): structure of the center of the cover.
3. Lemma 2.8(c), 2.10(b): the wild index and the failure of maximality.
4. Lemmas 2.12, 2.13: Weyl action on the trivial section; n-th power section.
5. Proposition 3.3: Weyl-fixed classes form a torsor of order [F^×:F^{×2}]; chi_sigma quadratic (n odd) or trivial (n even).
6. Lemma 3.11, Theorem 3.12, Corollary 3.13: Gindikin–Karpelevich formula from the cocycle.
7. Theorems 3.16, 3.23, 3.25, 3.27, Corollary 3.28, Theorem 3.29: deductions from cited theorems (GS16, He25, BJ13).
8. Lemma 3.32: pseudo-coefficients.
9. Lemma 4.14: character of full principal series for every sigma and p.
10. Lemma 5.4(b), Theorem 5.10(b): surjectivity up to reducible points (using the proof of the unitary-dual manuscript for Lemma 4.9(1)).
11. Theorem 5.14(b): PW_ad → PW_u is a bijection.
12. Definitions 5.9, 5.13, 5.16 and the translation of Li's space in Theorem 5.17(b).

Taken from Draft 1: Propositions 4.4, 6.1, 6.2, 6.5 (rewritten). Taken from Draft 3 of the other path after rechecking: Lemma 4.8, Lemma 3.21, Theorem 3.27(a),(b), the algebraic factorization.

## 6. Verification levels

Level 1: derived independently by me. Level 1s: level 1 and checked by a script in `scripts/`. Level 2: checked against a source through the extract described in Section 1. Level 3: memory.

| Statement | Level | Note |
|---|---|---|
| 2.1 cocycle | 2, 1s | Random triples: C1 (tame), W1 (Q_2). Not a proof. |
| 2.2, 2.3(a),(f) | 1s | C2 |
| 2.3(b) Kubota splitting | 1s | C9 (random). Proof is in the unitary-dual manuscript; I did not recheck it. |
| 2.3(c) | 1 | |
| 2.3(e) | 1s | W1 for Q_2 |
| 2.7 | 1s | C3 tame; W2, W3 for the index formula |
| Index formula [F^×:F^{×m}] = m·|mu_m|·|m|^{−1} | 3 | Neukirch II (5.8) from memory; instances checked in W2, W3 |
| (H3) nondegeneracy, (H4) | 3 | Standard; Weil XIII §5, Serre Local Fields XIV |
| 2.8, 2.10 | 1s | C4, W2, W3 |
| 2.12, 2.13 | 1s | C5, C6, C7 |
| 2.17, 2.18, 2.21, 2.22 | 1 | |
| 2.19, 2.20 | 3 | Gelbart–Knapp not consulted; lemma numbers removed |
| 2.25 | 2 + outline | KS23 Thm 3.4 checked; Bernstein's argument recalled, not rechecked |
| 2.29–2.32 | 2 | KS23 extract confirms the geometric lemma and BZ77 2.9, 2.13 for covers |
| 3.3 | 1s | C8 enumerates the four classes for 11 pairs (p,n) |
| 3.4, 3.7 | 2 | Moen's Theorem 1 and remark, from an OCR extract of the PJM scan |
| 3.5, 3.9 | none | Remark 2026.1, 2026.2 |
| 3.6, 3.8 | 2 | GS16 Thm 5.2; Sz19 Prop 5.5; Sz24 §3.1 |
| 3.11, 3.12, 3.13 | 1s | C10 checks the lifted Iwasawa decomposition and the averaging; S1 the zeros |
| 3.14 | 2 | GS16 Thm 5.1, Sz19 Thm 5.7. Identification of chi^n with chi_sigma: Remark 2026.3 |
| 3.15 | 2 | He25 extract (French original). A 2025 preprint, not yet published as far as I know |
| 3.16, 3.23, 3.25, 3.28, 3.29 | 1 given 3.14, 3.15 | |
| 3.18, 3.19, 3.22 | none | Remarks 2026.4, 2026.5 |
| 3.20, 3.21 | 1 | |
| 3.24 | 2 | Ban–Jantzen abstracts; theorem numbers not obtained |
| 3.27(a)–(c) | 1 given 3.15, 3.24 | Unitarity of pi_nt by a limit argument (please check) |
| 3.27(d) | 3 | Remark 2026.6 |
| 3.30 | 1 for the weakened statement | Remark 2026.7 |
| 3.32 | 1 | |
| 4.2 | 2 | Li12 introduction and table of contents |
| 4.3 | none | Remark 2026.8 |
| 4.6, 4.11, 4.12 | 3 | Li12 §2 and BJ13 (Casselman criterion) not read in detail |
| 4.8 | 1 | |
| 4.9(1) | 1 | Proof read and rechecked in the unitary-dual manuscript |
| 4.9(2) continuity | 3 | Silberger §4.4 |
| 4.13 | 3 | |
| 4.14 | 1 | |
| 5.1–5.8 | 1 | |
| 5.10(a),(b) | 1 | (a) uses KS23 3.4, 3.9 for finiteness of cuspidals |
| 5.10(c) | 2 | Li14 §3.4 says the BDK arguments adapt. No written proof found. Remark 2026.9 |
| 5.10(d) | 2 | Li12 Thm 5.8.10 statement checked |
| 5.14(a),(b) | 1 | |
| 5.17(a) | 1 given 4.9(2) | |
| 5.17(b),(c) | 2, outline | Remark 2026.10 |
| 6.1, 6.2, 6.5 | 1 | |
| 6.4 | 1 given 5.17(b),(c) | |
| Example 5.12, 8.1 | 1s | S2, S3. The table of fixed-vector dimensions for SL(2,F) is from memory |
| Example 8.4 | 1s | W1–W3 |
| Remark 8.5 | 2 | Depends on Remark 2026.3 in the wild case |

The ten "Remark 2026.k" notes in the paper: (1) Prop. 3.5, (2) Prop. 3.9, (3) Theorem 3.14, (4) Lemmas 3.18–3.19, (5) Lemma 3.22, (6) Theorem 3.27(b),(d), (7) Lemma 3.30, (8) Lemma 4.3, (9) Theorem 5.10(c),(d), (10) Theorem 5.17(b),(c). Draft 1 had 62 such markers. The other 52 statements now carry a status label instead. The change of status is recorded in the table above and in `conjecture_status.md`.

## 7. Citation checks

| Key | Reference | What was checked | How |
|---|---|---|---|
| GS16 | Goldberg–Szpruch, arXiv:1411.6134v2 | Hypotheses (p ∤ n from §1.3); §3.2 torus; Lemmas 3.1, 3.2; Thm 5.1; Thm 5.2; Thms 2.1, 2.2 | Extract. Journal data (IJNT 12 (2016) 1907–1936) from memory. The extract notes a discrepancy in the constant of Thm 5.1 between statement and proof; only positivity is used here. |
| Sz19 | Szpruch, arXiv:1609.08122 | No tameness in general setup; Lemmas 3.1, 3.2 (dim = d·‖d‖^{−1/2}); Lemma 2.3; Thm 5.7 (n ≢ 0 mod 4); Prop 5.5; Cor 5.2 | Extract of the first 100k characters; §5.7 was not seen. Journal data from the author's publication list. |
| Sz24 | Szpruch, arXiv:2411.11460 | n odd, no tameness; criterion; Prop 1; Thm 1; use of Luo | Extract |
| KS23 | Kaplan–Szpruch, arXiv:2206.06905 | Thms 3.3–3.10; class of groups | Extract. Journal data from a citing paper. |
| He25 | Heiermann, arXiv:2506.21334 | Thm 1.1, Lemma 1.2, Cor 1.4, Prop 2.4, 2.6, Lemmas 3.1–3.4, Cor 3.5, Thm A.2 | Extract of the first 100k characters (of 104k) |
| Li12 | Li, arXiv:1107.1865v3 | Admitted hypotheses; Thm 2.6.4, Cor 2.6.5; Thm 5.4.1; Def 5.6.4, Prop 5.6.5, Thm 5.6.10; Thm 5.8.10, Rem 5.8.11 | Extract, in three parts. The "corrections to §4.1" of the 2024 version were not found in the extract; whether they affect §5 is unchecked. |
| Li14 | Li, arXiv:1209.4156 | §3.1–3.4, Hypothesis 3.12, non-Archimedean case "by adapting [BDK]" | Extract of the first half. Journal data from EuDML. |
| Lu20 | Luo, PJM 306 | Abstract only | Publisher page (article is behind a paywall) |
| Mc12 | McNamara, arXiv:0911.2274v2 | Thm 5.1 (Stone–von Neumann), Lemmas 5.3, 6.3, Thm 7.5, hypothesis 2n | q−1 | Extract. Numbering of the published version may differ. |
| Mo88 | Moen, PJM 135 | Hypotheses p ≠ 2, p ∤ n; Theorem 1(a),(b); remark on reducibility | OCR extract of the scan; formulas garbled |
| BJ13, BJ16 | Ban–Jantzen | Abstracts; that Casselman's criterion for covers is attributed to BJ13 by a later paper | Search results |
| GSS23, GSS26, Ga23, GGK24, Ka18, Ka21 | | Titles, abstracts, bibliographic data | Search results. GGK24 year and Ga23 pages unknown. |
| Ar80, BDK86, BZ76, BZ77, Si79, Ta75, Sc50, Ku67, Mo68, KP84, FK86, Ge76, GK82, GPS83, HC70, Di77, Fe60, Ma57, Ta83, Vi81, Se81, Sa67, Cl91, Be74, BD84, Ca95, Bl85, Ne99, Se77, We75, We09, Ar81, Ar94 | | Not consulted for this draft | Bibliographic data from Draft 1 or memory. Corrected by memory: Arthur 1981 pages, Moore pages, Sen pages (uncertain), Blondel spelling, Flicker title. |

## 8. Sources not consulted (style guide 4.3)

Aritürk 1980. Moen's undated preprint (not available anywhere I looked). Kubota 1967 and Moore 1968. Flicker–Kazhdan 1986. Gelbart–Knapp 1982. Bernstein–Deligne–Kazhdan 1986 (statement recalled). Silberger's book. Luo 2020 beyond the abstract. Ban–Jantzen beyond abstracts. Gao–Gurevich–Karasiewicz. The published versions of all arXiv papers in Section 7.

## 9. Concordance

The paper numbers all statements, examples and remarks consecutively within each section. The 1994 manuscript numbered only lemmas, propositions, theorems, corollaries and conjectures. Draft 1 also counted remarks, so its numbers differ from both.

| 1994 | Draft 1 | Draft 2 |
|---|---|---|
| 2.1 | 2.1 | Lemma 2.1 |
| 2.2 | 2.2 | Lemma 2.2 |
| 2.3 | 2.3 | Lemma 2.3 |
| 2.4 | 2.5 | Corollary 2.5 |
| 2.5 | 2.6 | Lemma 2.6 |
| 2.6 | 2.7 | Lemma 2.8 |
| 2.7 | 2.9 | Lemma 2.10 |
| 2.8 | 2.10 | Lemma 2.14 |
| 2.9 | 2.11 | Lemma 2.15 |
| 2.10 | 2.12 | Lemma 2.17 |
| 2.11 | 2.13 | Lemma 2.18 |
| 2.12 | 2.14 | Lemma 2.19 |
| 2.13 | 2.15 | Lemma 2.20 |
| 2.14 | 2.17 | Lemma 2.21 |
| 2.15 | 2.18 | Corollary 2.22 |
| 2.16 | 2.19 | Lemma 2.24 |
| 2.17 (conjecture) | 2.20 | Theorem 2.25 |
| 2.18 | 2.22 | Lemma 2.27 |
| 2.19 | 2.23 | Lemma 2.29 |
| 2.20 | 2.24 | Proposition 2.30 |
| 2.21 | 2.25 | Lemma 2.31 |
| 2.22 | 2.26 | Proposition 2.32 |
| 3.1 | 3.1 | Theorem 3.4 |
| 3.2 | 3.2 | Proposition 3.5 |
| 3.3 (conjecture) | 3.3 | Theorem 3.6 |
| 3.4 | 3.4 | Theorem 3.7 |
| 3.5 (conjecture) | 3.5 | Theorem 3.8 |
| 3.6 | 3.6 | Proposition 3.9 |
| 3.7 | 3.7 | Lemma 3.10 |
| 3.8 | 3.8 | Lemma 3.18 |
| 3.9 | 3.9 | Lemma 3.19 |
| 3.10 | 3.10 | Lemma 3.20 |
| 3.11 | 3.11 | Lemma 3.21 |
| 3.12 | 3.12 | Lemma 3.22 |
| 3.13 (conjecture) | 3.13 | Theorem 3.23 |
| 3.14 | 3.14 | Lemma 3.24 |
| 3.15 (conjecture) | 3.15 | Theorem 3.25 |
| 3.16 (conjecture) | 3.16 | Theorem 3.27 |
| 3.17 | 3.17 | Lemma 3.30 |
| 4.1 | 4.1 | Lemma 4.1 |
| 4.2 | 4.2 | Lemma 4.2 |
| 4.3 | 4.3 | Lemma 4.3 |
| 4.4 | 4.4 | Lemma 4.6 |
| 4.5 | 4.5 | Lemma 4.8 |
| 4.6 | 4.6 | Lemma 4.9 |
| 4.7 | 4.7 | Lemma 4.11 |
| 4.8 (conjecture) | 4.8 | Proposition 4.12 |
| 4.9 | 4.9 | Lemma 4.13 |
| 4.10 | 4.10 | Lemma 4.14 |
| 5.1 | 5.1 | Lemma 5.1 |
| 5.2 | 5.2 | Lemma 5.2 |
| 5.3 | 5.3 | Lemma 5.3 |
| 5.4 | 5.4 | Lemma 5.4 |
| 5.5 | 5.5 | Lemma 5.6 |
| 5.6 | 5.6 | Lemma 5.7 |
| 5.7 | 5.7 | Lemma 5.8 |
| 5.8 | 5.8 | Theorem 5.10 |
| 5.9 | 5.9 | Theorem 5.14 |
| 5.10 | 5.10 | Theorem 5.17 |
| 6.1 | 6.1 | Proposition 6.1 |
| 6.2 | 6.2 | Proposition 6.2 |
| 6.3 | 6.3 | Theorem 6.4 |

Statements of Draft 1's Section 7 (removed as a section):

| Draft 1 | Draft 2 |
|---|---|
| Prop. 7.1 (cocenter) | Proposition 4.4 |
| Example 7.2 | Examples 2.11, 2.23 |
| Prop. 7.3 (exact sequences) | used in the proof of Theorem 5.10(a) |
| Prop. 7.4 (circle) | Proposition 6.1 |
| Prop. 7.5 (product) | Proposition 6.2 |
| §7.5 (factorization) | Proposition 6.5 |
| labels `legacy:1` … `legacy:62` | descriptive labels (`lem:kubota`, …, `thm:FT-dist`) |

Statements added in Draft 2 within Sections 1 to 6 (they have no 1994 number): Example 1.1, Example 1.2, Example 1.3, Proposition 2.7, Example 2.11, Lemma 2.12, Lemma 2.13, Example 2.23, Example 2.33, Definition 3.1, Example 3.2, Proposition 3.3, Lemma 3.11, Theorem 3.12, Corollary 3.13, Theorem 3.14, Theorem 3.15, Theorem 3.16, Example 3.17, Corollary 3.28, Theorem 3.29, Example 3.31, Lemma 3.32, Example 3.33, Proposition 4.4, Example 4.5, Example 4.10, Example 4.15, Example 5.5, Definition 5.9, Corollary 5.11, Example 5.12, Definition 5.13, Example 5.15, Definition 5.16, Example 5.18, Example 6.3, Proposition 6.5, Example 6.6. Unlabeled remarks and examples take the remaining numbers. Sections 7 to 11 are new.

Equation numbers agree with the 1994 manuscript in Section 2 up to (2.12) and differ afterwards.

Between the first and the second version of Draft 2 (both dated November 24, 2026) the additions were renumbered from letters (2.B, 3.E, …) to this consecutive scheme. Nothing else changed except the notation footnote and the wording "Conjecture x.y of 1994" wherever an original number is cited.

## 10. Style guide: defaults used and points for a ruling

- Class `article`, kept from Draft 1. Times: newtx if installed, otherwise mathptmx. **The PDF in this package was built with the mathptmx fallback because newtx is not installed in my environment.** Rebuilding with newtx may move line breaks.
- Compiles with pdflatex with no errors, no undefined references and no overfull boxes. One underfull box (badness 1616) remains at Theorem 5.17.
- Numbering follows your ruling of November 24: one counter per section, shared by all statements, examples and remarks, in order of appearance. The literature review and the notation table are unnumbered sections, so the six original sections are still Sections 1 to 6.
- The notation changes from the 1994 manuscript are recorded in a footnote at the start of Section 1.1, as you asked.
- The style guide's citation-key rule is followed except for five unpublished companion manuscripts, which have keys JoUD, JoSyn, JoCh, JoTr, JoMJL.
- Status labels are separated from names by a semicolon inside theorem headings. The no-semicolon rule is otherwise observed in the prose.
- The paper refers to the scripts by file name. A commit hash can be added once this draft is merged.

Settled on November 24: numbering (consecutive within sections, no letters), notation changes (accepted, with a footnote). Still open for a ruling: (a) whether the "Remark 2026.k" notes should stay as paragraph notes or become numbered remarks, (b) the status-label punctuation.

## 11. Research agenda for Draft 3, in order of priority

1. **Referee the new proofs.** In order: Theorem 3.12 (the lifted Iwasawa decomposition and the role of the splitting), Proposition 3.3, Proposition 2.7, Lemma 4.9(1), Theorem 5.10(b), Theorem 5.14(b), the unitarity of pi_nt in Theorem 3.27.
2. **Read the primary sources in PDF.** GS16 §3.2 and Theorem 5.1 to settle Remark 2026.3 (is their chi^n our chi_sigma in general?). He25 in full, since Theorems 3.16, 3.23, 3.25, 3.27, 3.29 all rest on it and it is a preprint. Li12 §5.6 for Theorem 5.10(b).
3. **The separation property (Problem 10.3).** Try the Euler–Poincaré function for n odd, tame, on the unramified component, starting from Example 10.10. This would make the admissible and unitary Paley–Wiener theorems unconditional up to the ramified components.
4. **The Schwartz theorem in rank one (Problem 10.4).** Write the wave-packet argument on a single circle, then treat the Weyl-fixed points.
5. **Wild torus (Problem 10.2).** Compute the cubic Hilbert symbol on Q_3(omega) exactly and exhibit a Lagrangian. Test the bound "m ≥ n" on Q_3(zeta_9).
6. **Conjecture 10.1.** At least compute mu(sigma) for F = Q_2(i), n = 4 at the unramified-type Weyl-fixed classes.
7. **Moen and Aritürk (Problem 10.5).** Obtain the sources. Derive J_mu from GS16 Theorems 2.1, 2.2.
8. **Elliptic characters (Problem 10.6)** and the comparison with `sl2bar-characters`.
9. **Local Shimura correspondence for cocenters (Problem 10.8).** Decide the relation with the trace matching in `sl2bar-unitary-dual`, which covers n odd and 4 | n while the reducibility pattern suggests PGL(2) for all even n.
10. Citations: page numbers and published theorem numbers for every level-2 entry.

## 12. Where a referee should look first

- Theorem 3.16 depends on a preprint (He25) read only through an extract.
- Theorem 5.10(c): I found an assertion, not a proof, that BDK holds for covers.
- Theorem 5.17(b): my dictionary between Li's triples and Definition 5.16 is my own reading.
- Theorem 5.17(c): the proof is an outline.
- Theorem 3.27(d) and the table of fixed vectors in Example 5.12 are from memory.
- Example 3.33 and Problem 10.8 state a heuristic (SL(2) pattern for n odd, PGL(2) pattern for n even) that is supported by the reducibility points computed here, not by a proved correspondence.


## Draft 3 — 2026-11-24

Referee: Claude; revision and assessment: ChatGPT. Addressed the seven substantive
findings: Plancherel coordinates, complex reducibility parameters, the kernel
example, density needed for PWad(d), constituent-character difference, Clifford
restriction multiplicities, and the tame splitting in the explicit model.
The previous restriction of the principal-series image theorem to p prime to
2n is unnecessary: choose congruence depth m > v_F(2). Updated the corresponding
count to [F^×:F^{×2}]. The kernel/cocenter identification and its distributional
factorization are conditional pending verification of the required geometric
density theorem. Removed three misleading dependency arrows. The Iwahori
idempotent construction is an unverified test, pending computation of the
ratio of splittings and fixed-vector dimensions. Clarified the Lagrangian
problem. The prior restriction lemma asserted multiplicity one and packet
size independent of the ambient representation; neither assertion is used.
The source was revised directly through GitHub; the PDF and scripts have
not been rebuilt or checked. Broader notation and environment consolidation
remain editorial tasks.
