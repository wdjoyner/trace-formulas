# sl2bar-characters

Character relations between supercuspidal representations of SL(2, F), F p-adic, and genuine supercuspidal representations of its metaplectic covers. Two papers by David Joyner, each reconstructed and revised with AI assistance in November 2026 from unfinished notes.

## Summaries

**Two-orbit unramified elliptic character relations for depth-zero representations of metaplectic covers of SL(2)** (`character_relations_depth_zero.tex`; notes of about 2000; by David Joyner, Argon and ChatGPT). Here the cover is n-fold with n ≥ 3 odd and prime to the residue characteristic p, and F contains the n-th roots of unity. The SL(2, F)-conjugacy classes of maximal compact subgroups correspond to the two vertex orbits of the Bruhat–Tits tree. The paper shows, by continuous group cohomology, that the cover splits uniquely over both of them. Using these two splittings it compares the characters of ordinary and genuine depth-zero supercuspidal representations, induced from either vertex orbit, on the two classes of unramified elliptic tori.

- Because the preimage of such a torus in the cover is abelian and splits uniquely, the genuine and ordinary characters agree there. Composing with the n-th power map gives an n-th power character identity at all regular elements of the torus, including those with central reduction.
- A fixed-ball computation on the tree gives complementary closed formulas for the two vertex orbits near ±I. Their sum is the constant −2θ(±I), which comes from restricting a depth-zero supercuspidal of GL(2, F) to SL(2, F).
- The results are illustrated over ℚ₇ with n = 3.

**Notes on characters of supercuspidal representations of the twofold metaplectic cover of SL(2, F), F p-adic** (`character_relations_twofold.tex`; notes of 1996, based on conversations with Jeff Adams and Jason Schultz; Draft 2, November 26, 2026). For the twofold cover and odd residue characteristic, both the ordinary and the genuine supercuspidals considered are compactly induced from a maximal compact subgroup. Their characters become weighted sums over the fixed vertices of the element on the tree.

- The two canonical compact splittings of the cover do not agree on their common Iwahori subgroup. Their ratio is a quadratic residue character, computed from the Kubota cocycle.
- On regular elliptic elements this gives the genuine character in terms of the ordinary one, up to an explicit sign. The sign is trivial at the lift attached to the inducing vertex type.
- For generic depth-zero supercuspidals there are closed formulas on the unramified elliptic tori, with a sign depending on the vertex orbit and on q modulo 4. These characters vanish at split elements with regular reduction.
- The rest of the split torus and positive depth remain open.

## Files

| File | What it is |
|---|---|
| `character_relations_depth_zero.tex`, `.pdf` | The odd-degree paper |
| `revision_log.md` | Revision history of the odd-degree paper |
| `verify_sl2bar_characters.py` | Finite consistency checks for the odd-degree paper (finite-field character tables and related statements); not a proof |
| `character_relations_twofold.tex`, `.pdf` | The twofold-cover notes |
| `character_relations_twofold_revision_log.tex`, `.pdf` | Revision log of the twofold-cover notes |
| `referee-report_draft1_carbon.md` | Referee report by Carbon (Gemini) on Draft 1 of the twofold-cover notes, incorporated in Draft 2 |
| `twofold_cover_check.py` | Exact checks over ℚ_p of the Kubota cocycle, the compact splittings and the lifted torus and Weyl elements; run by `../run_checks.py` |

## Status

AI-assisted working drafts, not independently refereed. The AI contributions are described in each paper's Acknowledgments and in the revision logs.

## License

Text and LaTeX: CC BY 4.0. Scripts: MIT.
