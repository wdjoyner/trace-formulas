# Response to the referee reports of Gemini (November 18, 2026)

Reports: [`report-gemini-master-file.md`](report-gemini-master-file.md) (on the master file only) and [`report-gemini-all-sections.md`](report-gemini-all-sections.md) (on all sections), both on `revised/sl2bar-trace-2026.pdf` as of 2026-11-16 (111 pages).
Response by D. Joyner and Claude. Each point was checked against the source by Claude before it was accepted or declined. Verification levels are those of the style guide, Section 7: level 1 is an independent derivation, level 2 a check against a source that was consulted.

The second report cites several statements by numbers that are not those of the refereed PDF (its Lemma 4.8, Proposition 7.9, Proposition 6.11, Lemma 6.5, Example 6.13 and Remark 2026.13 are Lemma 4.10, Proposition 7.10, Proposition 6.13, Lemma 6.6, Example 6.D and Remark 2026.18). The labels it quotes are correct, and the table below goes by labels.

## Mathematical points

| Point of the report | Verdict | Action |
|---|---|---|
| `prop:weil-char`, archimedean case: $a(-c^{-1})$ should be $a(c^{-1})$ | Correct (level 1). The product with $a(-c^{-1})$ is $-g$. The factorization in `lem:weil-kernel` is right. The misprint affects only a continuity statement. | Fixed. |
| Proposition 7.8′(b): uniqueness of $h_\pi$ might miss zeros or poles on the circle | Not a gap (level 1). A rational $u$ with $\lvert u\rvert=1$ on the circle satisfies $u(z)\overline{u(1/\bar z)}=1$, so a zero on the circle would also be a pole. | The argument is now written out in the proof. |
| `lem:JA-central`(c) and `prop:unipotent`(b): measure normalization | Not an issue (level 1). The report describes `lem:JA-central`(c) as using $dn_v$. It is stated with $d^\times t$, the same measure as in $Z_v$, fixed in Section 4.5. | One sentence added at the start of the proof of `prop:unipotent`(b). |
| "Critical check" on $\chi_v^2$ in Proposition 7.8′(c) | No error (level 1). The report's conclusion is right: for $\mu=\chi_{\psi_b}$, $\chi^2=1$ at every place, and $r_2$ cancels the 2-adic factor displayed in `ex:itf-Q`. | `ex:itf-Q` now states $m(\mu,\lambda)=c_\mu\,\xi(2\lambda)/\xi(2\lambda+1)$, with a pointer to Proposition 7.8′(c). |
| `prop:Mw0`, Step 3: alternative argument | The report agrees that the argument is correct. The alternative is not shorter once continuity and density are written out. | No change. |

## Consistency and LaTeX

| Point | Verdict | Action |
|---|---|---|
| Section 1.2: "defined but not evaluated" contradicts the abstract | Valid. | Reworded. The sentence now says that the factors are not evaluated in Sections 4–6 and that their explicit form is taken from Szpruch in Proposition 7.8′(c). The table row for Section 6 is reworded in the same way. |
| Glossary, "Dyadic place" | Valid. | Rewritten with the rest of the glossary. |
| $A(\mathbb A_S)$ in Section 3.3 against $A(\mathbb Q_S)$ elsewhere | Valid, cosmetic. Section 6 had two occurrences, one of them the cross-reference. | Replaced by $A(\mathbb Q_S)$ throughout. |
| Hyperlinks of Lemma 7.5′ and Proposition 7.8′ land on Proposition 7.5 and Lemma 7.8 | Valid. | `\phantomsection\label` added inside both statements, and `\shellref`, `\normref` now link to them. |
| `\Res` and `\Resid` print the same | True, and intended. `\Resid` occurs four times, in Section 5, always with a subscript $\lambda=\frac12$. | No change. |
| `mathptmx` | Already recorded in the preamble and in the revision log. | No change. The build machine has no newtx. |
| Title spelling "hitch-hiker's" | It is the title of the 1995 notes. | No change. |

## Bibliography and authorship

| Point | Verdict | Action |
|---|---|---|
| [Ga14] "published in Amer. J. Math." | Not accepted (level 2). The two reports give two different citations (139 (2017), 1457–1519, and 140 (2018), 1–36). Neither could be confirmed. arXiv:1410.7624 is Gao's thesis (National University of Singapore, 2014). His article in Amer. J. Math. 140 (2018), 83–137, has the title "The Langlands–Shahidi L-functions for Brylinski–Deligne extensions" and is a different item. | No change. |
| [Li21] | Published: Astérisque 464 (2026), Société Mathématique de France (level 2, the publisher's page). | Entry updated. The arXiv number is kept. |
| [Sz16] published in Manuscripta Math. 159 (2019), 117–159 | Plausible, and later papers cite it as "Szp19", but the pages were not confirmed (level 3). The text cites equation (5.8) of the arXiv version. | No change. To be checked against MathSciNet. |
| [Me01], [Me02] | The report agrees that they are right. | No change. |
| "Publ. Math. IHES" varies | Not so. It is used uniformly, four times. | No change. |
| "J. reine angew. Math." against "J. Reine Angew. Math." | Valid. | Unified. |
| AI disclosure in the abstract, and Claude as an author | These follow the style guide (Sections 2 and 5) and the decision of D. Joyner for this draft. The report is right that arXiv does not accept an AI system as an author. That matters only for a version submitted there. | No change. |
