# L35 — Machine learning in de cross-sectie: onderzoeksnotities (gepauzeerd)

Status: nog geen lecturebestand geschreven, myst.yml en references.bib niet aangeraakt.
Een tijdelijk prototype `sim_a.py` staat in de scratchpad (niet in de repo).

## 1. Bib-entries

### Al in references.bib (niet opnieuw toevoegen)
GuKellyXiu2020, KellyPruittSu2019, KozakNagelSantosh2020, MartinNagel2022, ClarkWest2007,
CampbellThompson2008, FengGiglioXiu2020, JensenKellyPedersen2023, ChenZimmermann2022,
HarveyLiuZhu2016, McLeanPontiff2016, GoyalWelch2008, BrittenJones1999, SantaClara2026.
Geen daarvan heeft een `TODO verify`-note.

### Nieuw, DOI via Crossref geverifieerd (titel/journal/jaar/volume/pagina's gecontroleerd)
```bibtex
@article{LettauPelger2020,
  author  = {Lettau, Martin and Pelger, Markus},
  title   = {Factors That Fit the Time Series and Cross-Section of Stock Returns},
  journal = {The Review of Financial Studies},
  year    = {2020},
  volume  = {33},
  number  = {5},
  pages   = {2274--2325},
  doi     = {10.1093/rfs/hhaa020}
}
@article{ChenPelgerZhu2024,
  author  = {Chen, Luyang and Pelger, Markus and Zhu, Jason},
  title   = {Deep Learning in Asset Pricing},
  journal = {Management Science},
  year    = {2024},
  volume  = {70},
  number  = {2},
  pages   = {714--750},
  doi     = {10.1287/mnsc.2023.4695}
}
@article{KellyMalamudZhou2024,
  author  = {Kelly, Bryan and Malamud, Semyon and Zhou, Kangying},
  title   = {The Virtue of Complexity in Return Prediction},
  journal = {The Journal of Finance},
  year    = {2024},
  volume  = {79},
  number  = {1},
  pages   = {459--503},
  doi     = {10.1111/jofi.13298}
}
@article{KellyXiu2023,
  author  = {Kelly, Bryan and Xiu, Dacheng},
  title   = {Financial Machine Learning},
  journal = {Foundations and Trends in Finance},
  year    = {2023},
  volume  = {13},
  number  = {3--4},
  pages   = {205--363},
  doi     = {10.1561/0500000064}
}
@book{Nagel2021,
  author    = {Nagel, Stefan},
  title     = {Machine Learning in Asset Pricing},
  publisher = {Princeton University Press},
  year      = {2021},
  doi       = {10.23943/princeton/9780691218700.001.0001}
}
@article{AvramovChengMetzker2023,
  author  = {Avramov, Doron and Cheng, Si and Metzker, Lior},
  title   = {Machine Learning vs. Economic Restrictions: Evidence from Stock Return Predictability},
  journal = {Management Science},
  year    = {2023},
  volume  = {69},
  number  = {5},
  pages   = {2587--2619},
  doi     = {10.1287/mnsc.2022.4449}
}
@article{Tibshirani1996,
  author  = {Tibshirani, Robert},
  title   = {Regression Shrinkage and Selection via the Lasso},
  journal = {Journal of the Royal Statistical Society: Series B (Methodological)},
  year    = {1996},
  volume  = {58},
  number  = {1},
  pages   = {267--288},
  doi     = {10.1111/j.2517-6161.1996.tb02080.x}
}
@article{HoerlKennard1970,
  author  = {Hoerl, Arthur E. and Kennard, Robert W.},
  title   = {Ridge Regression: Biased Estimation for Nonorthogonal Problems},
  journal = {Technometrics},
  year    = {1970},
  volume  = {12},
  number  = {1},
  pages   = {55--67},
  doi     = {10.1080/00401706.1970.10488634}
}
@article{ZouHastie2005,
  author  = {Zou, Hui and Hastie, Trevor},
  title   = {Regularization and Variable Selection via the Elastic Net},
  journal = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
  year    = {2005},
  volume  = {67},
  number  = {2},
  pages   = {301--320},
  doi     = {10.1111/j.1467-9868.2005.00503.x}
}
@article{Breiman2001,
  author  = {Breiman, Leo},
  title   = {Random Forests},
  journal = {Machine Learning},
  year    = {2001},
  volume  = {45},
  number  = {1},
  pages   = {5--32},
  doi     = {10.1023/A:1010933404324}
}
@article{Friedman2001,
  author  = {Friedman, Jerome H.},
  title   = {Greedy Function Approximation: A Gradient Boosting Machine},
  journal = {The Annals of Statistics},
  year    = {2001},
  volume  = {29},
  number  = {5},
  pages   = {1189--1232},
  doi     = {10.1214/aos/1013203451}
}
@article{BelkinHsuMaMandal2019,
  author  = {Belkin, Mikhail and Hsu, Daniel and Ma, Siyuan and Mandal, Soumik},
  title   = {Reconciling Modern Machine-Learning Practice and the Classical Bias--Variance Trade-Off},
  journal = {Proceedings of the National Academy of Sciences},
  year    = {2019},
  volume  = {116},
  number  = {32},
  pages   = {15849--15854},
  doi     = {10.1073/pnas.1903070116}
}
@article{EhsaniLinnainmaa2022,
  author  = {Ehsani, Sina and Linnainmaa, Juhani T.},
  title   = {Factor Momentum and the Momentum Factor},
  journal = {The Journal of Finance},
  year    = {2022},
  volume  = {77},
  number  = {3},
  pages   = {1877--1919},
  doi     = {10.1111/jofi.13131}
}
```
Friedman2001 pagina's 1189–1232 komen uit de GKX-referentielijst; Crossref gaf geen pagina's.
Rahimi-Recht 2007 (random features, NIPS) heeft geen DOI gevonden; alleen opnemen als `@inproceedings` met url, of weglaten.

## 2. Gepubliceerde getallen — geverifieerd uit de RFS-PDF van Gu-Kelly-Xiu (2020)
(PDF opgehaald van dachxiu.chicagobooth.edu/download/ML.pdf; open access)

- Data (p. 2226, 2248): CRSP, maart 1957 – december 2016 (60 jaar), "nearly 30,000" aandelen,
  gemiddeld >6.200 per maand; 94 karakteristieken, 8 macrovariabelen (Welch-Goyal: dp, ep, bm,
  ntis, tbl, tms, dfy, svar), 74 industriedummies; $z = x_t \otimes c_{i,t}$ → 94×(8+1)+74 = 920 covariaten.
  Karakteristieken per maand cross-sectioneel gerankt naar [-1,1].
- Splitsing (p. 2249): training 1957–1974, validatie 1975–1986, test 1987–2016; jaarlijkse herschatting,
  training groeit met 1 jaar, validatie 12 jaar rollend. Geen cross-validatie (tijdsvolgorde).
- OOS R² (vgl. 19, p. 2246): noemer = som van gekwadrateerde excess rendementen *zonder demeaning*;
  tegen het historische gemiddelde ligt de maandelijkse R² ruwweg 3 procentpunt hoger (voetnoot 34:
  OLS-3 tegen historisch gemiddelde = 3,74% per maand).
- Tabel 1 (p. 2250), maandelijkse OOS R² in %, alle aandelen:
  OLS+H −3,46; OLS-3+H 0,16; PLS 0,27; PCR 0,26; ENet+H 0,11; GLM+H 0,19; RF 0,33; GBRT+H 0,34;
  NN1 0,33; NN2 0,39; NN3 0,40; NN4 0,39; NN5 0,36.
  Top-1000: OLS+H −11,28 … NN3 0,70. Bottom-1000: OLS+H −1,30 … NN3 0,45.
- Tabel 2 (p. 2253): jaarlijkse R² ongeveer een orde groter (NN4 3,60; RF 3,28; OLS+H −34,86).
- Tabel 3 (p. 2253): Diebold-Mariano (aangepast: cross-sectioneel gemiddelde foutverschil, NW-se, vgl. 20).
  Alleen NN's significant beter dan lineaire modellen; met Bonferroni (kritieke waarde 2,64) alleen marginaal.
- Architecturen (p. 2244): NN1 = 32; NN2 = 32,16; NN3 = 32,16,8; NN4 = 32,16,8,4; NN5 = +2; ReLU;
  regularisatie: L1, Adam learning-rate shrinkage, early stopping, batch normalization, ensembles over seeds.
- Tabel 5 (p. 2263): bottom-up S&P 500 OOS R² maandelijks: OLS-3+H −0,22; GLM 0,71; NN3 1,80.
- Timing S&P 500 (p. 2228/2264, tabel 6): Sharpe 0,77 (NN3) tegen 0,51 buy-and-hold.
- Tabel 7 (p. 2266), value-weighted decile H–L, 1987–2016: Sharpe OLS-3+H 0,61; PLS 0,72; PCR 0,88;
  ENet+H 0,39; GLM+H 0,76; RF 0,98; GBRT+H 0,81; NN1 1,17; NN2 1,16; NN3 1,20; NN4 1,35; NN5 1,15.
  NN4 H–L: 2,3% per maand (27,1% p.j.), vol 5,8% per maand → Sharpe 1,35 (p. 2265).
- Equal-weighted (Internet Appendix tabel A.9, genoemd p. 2265): NN4 Sharpe 2,45; OLS-3 0,83 (p. 2228).
  Zonder aandelen onder NYSE-20%-percentiel (tabel A.10): NN4 EW Sharpe 1,69 (p. 2267).
- Tabel 8 (p. 2267): turnover NN1–NN5 110–130% per maand (p. 2268); max drawdown NN4 VW 51,78%, EW 14,72%;
  FF5+Mom-alpha NN4 VW 1,76%/maand, t = 6,00.
- Belangrijkste voorspellers (p. 2254): prijstrends (mom1m, mom12m, chmom, indmom, maxret, mom36m),
  liquiditeit (turn, mvel1, dolvol, ill, zerotrade, baspread), risico (retvol, idiovol, beta, betasq).
- Simulatie-appendix (Internet Appendix A): in de hoofdtekst alleen beschreven (p. 2229): één DGP met
  lineaire additieve predictoren, één met niet-lineaire transformaties en paarsgewijze interacties;
  lineaire methoden winnen in de eerste, bomen/NN in de tweede. De exacte parameterisatie van de
  appendix is NIET geverifieerd (appendix niet opgehaald).

## 3. Andere papers: wat geverifieerd is (abstract-niveau)
- Kozak-Nagel-Santosh (NBER w24070 abstract): robuuste SDF met een economisch gemotiveerde prior die
  laag-variantie-PC's krimpt; een characteristics-sparse SDF vat de cross-sectie slecht; een handvol PC's
  wel. Geen getallen geverifieerd.
- Martin-Nagel (NBER w26586 abstract): als het aantal karakteristieken het aantal activa nadert, lijken
  rendementen ex post voorspelbaar; investeerders gebruiken optimaal ridge/Lasso-achtige leerregels;
  "Standard in-sample tests of market efficiency reject the no-predictability null with high probability,
  despite the fact that investors optimally use the information available to them in real time. In
  contrast, out-of-sample tests retain their economic meaning."
- Kelly-Malamud-Zhou (NBER w30217 abstract): eenvoudige modellen onderschatten voorspelbaarheid ten
  opzichte van complexe modellen met meer parameters dan observaties; empirisch op US-marktrendement.
  Geen getallen geverifieerd (Wiley 403).
- Lettau-Pelger (NBER w24858 abstract): RP-PCA = PCA plus straf op pricing errors in gemiddelden; vindt
  zwakke factoren met hoge Sharpe die PCA mist; OOS maximale Sharpe van vijf factoren "more than twice as
  large as with PCA".
- Chen-Pelger-Zhu (arXiv 1904.00745 abstract): deep NN, no-arbitrage als criterium, adversariële
  test-assets, macro-toestanden; verslaat alle benchmarks OOS in Sharpe, verklaarde variatie en pricing
  errors. Geen getallen.
- Kelly-Pruitt-Su (NBER w24540 abstract): IPCA, latente factoren met loadings lineair in karakteristieken;
  vier IPCA-factoren verklaren de cross-sectie beter dan bestaande modellen; slechts acht karakteristieken
  significant; anomalie-alfa's klein en insignificant.
- Avramov-Cheng-Metzker: NIETS geverifieerd behalve bibgegevens (SSRN, INFORMS en Semantic Scholar-abstract
  geblokkeerd). Inhoudelijke claim (ML-winst zit in microcaps/distressed/moeilijk verhandelbaar, veel kleiner
  na filters) moet in de tekst als "volgens de samenvatting van het paper, niet door ons nagerekend" of
  eerst worden geverifieerd.
- Santa-Clara-post (LinkedIn): niet opgehaald; de claim "ML ongeveer twee keer zo goed als lineair" en
  "What we don't know #6" niet letterlijk geverifieerd. Andere lectures citeren de post letterlijk
  (bijv. 05_32); voor L35 eerst de posttekst ophalen of parafraseren zonder aanhalingstekens.
- WebSearch-budget van de sessie is op; WebFetch werkt nog voor open URL's.

## 4. Data en loaders (lokaal gecontroleerd, HAP_OFFLINE=1)
- `hap.osap()` : 1926-01 – 2024-12, 1188 × 212 long-short signalen (decimalen, float32). 133 signalen
  compleet vanaf 1965, 158 compleet vanaf 1975 t/m 2024-12; in 2024 ~195–198 niet-leeg.
- `hap.osap("signaldoc")` : kolommen o.a. signal, Year, Cat.Signal, SampleStartYear, SampleEndYear, T-Stat.
- `hap.french("100_Portfolios_10x10", table=0)` VW-rendementen; table=4 aantal firma's; table=5
  gemiddelde marktkap; table=6 met `percent=False` = VW gemiddelde BE/ME (alle in cache, 1926-07 –).
- `hap.newey_west` bruikbaar voor DM/Clark-West-t; `hap.sharpe`, `hap.summary_stats` beschikbaar.
- scikit-learn 1.9.0 geïnstalleerd; 8 cores (maar parallelle agents → marge houden).
- Labels in buurlectures: `eq-voorspelbaarheid-oos`, `eq-voorspelbaarheid-cw`, `eq-voorspelbaarheid-ct`
  (04_20); `eq-sdf-unificatie-b-lambda`, `prop-sdf-unificatie-b-lambda`, `thm-sdf-unificatie-factor` (05_26);
  PCA in 03_11: `eq-apt-no-arbitrage-ck`, `fig-apt-no-arbitrage-pca`. 05_31 bestaat (alleen .md),
  labels `eq-portfolio-choice-bsv`. 06_34 bestaat nog niet.
- myst.yml: Deel VI-blok nog uitgecommentarieerd; buurregels in Deel V gebruiken `.md`.

## 5. Plan (kort)
- **Toy** (orthogonaal design, X'X = 10·I, rendementen in %): x1 = (−2,−1,0,1,2), x2 = (1,−2,0,2,−1),
  r = (−3,−2,1,0,4). z = X'r = (16,−3). OLS b = (1,6; −0,3), fit (−3,5; −1; 0; 1; 3,5), SSE 3,5, SST 30.
  Ridge λ=10: b = z/20 = (0,8; −0,15). LASSO (½SSE + λ|b|₁, λ=5): soft-threshold → b = (1,1; 0)
  (sklearn Lasso alpha=1, n=5). Elastic net: soft(z,λ1)/(10+λ2). Boom met één split: beste split
  x1 ≤ −0,5 → voorspelling −2,5 (aandelen 1–2) en 5/3 (3–5), SSE 9,167 (uniek; alle andere splits groter).
- **Theorie**: bias-variantie; ridge/LASSO/EN gesloten vorm bij orthogonale X; PCR/PLS; bomen/bagging/
  RF/boosting; feedforward NN (ReLU, L1/L2, early stopping); GKX-OOS-R² zonder demeaning vs.
  eq-voorspelbaarheid-oos; IPCA $r_{i,t+1} = z_{i,t}'\Gamma f_{t+1} + \varepsilon$; KNS-prior
  $\mu \sim N(0, \kappa^2/\tau\,\Sigma^2)$ → $\hat b = (\Sigma + \gamma I)^{-1}\bar\mu$ als `{prf:proposition}`,
  plus equivalentie met ridge-regressie van 1 op factorrendementen (Britten-Jones; Sherman-Morrison
  → proportioneel); Martin-Nagel-argument.
- **Simulatie (a)** GKX-achtig: N=500, T=180, 20 gerankte AR(1)-karakteristieken, x_t AR(1) 0,95,
  features c ⊗ (1,x) = 40; lineair g = c1 + c2 + c3·x, niet-lineair g = (c1² − 1/3), c1·c2, sign(c3·x),
  geschaald tot sd 0,02; ruis β_i v_t + t5-ruis sd 0,10 (R² ≈ 2–3%). Train 108 / validatie 36 / test 36
  maanden; OLS, ridge, LASSO, EN, RF, HistGB, MLP; meerdere replicaties, één cel per wereld (<60 s: timing
  nog niet gemeten). Zeggen dat de DGP geïnspireerd is op, niet gelijk aan, GKX-appendix.
- **Simulatie (b)** Martin-Nagel: cashflow y_t = Xθ + e, θ ~ N(0, g/J·I), Bayesiaanse (ridge) investeerders;
  prijs = X θ̃_t; rendement = X(θ − θ̃_t) + e. In-sample F-toets verwerpt vaak; real-time OOS R² ≤ 0.
  Figuur tegen J/N.
- **Simulatie (c)** KMZ: random Fourier features, ridgeless (duale vorm, T×T), P/T van 0,1 tot 10;
  OOS R² (dip bij P/T=1) en Sharpe van timingstrategie; ~100 replicaties.
- **Replicatie (1)** OSAP factor timing: features per (signaal, maand): eigen r_t, gemiddelde t−11..t−1,
  t−35..t−12, 12m-vol, cross-sectioneel gemiddelde r_t en 12m; gepoolde modellen OLS/ridge/LASSO/RF/HistGB;
  expanding window vanaf 1990, herschatting per 5 jaar, laatste 5 jaar validatie; GKX-OOS-R², DM-t via
  hap.newey_west, long-short kwintielen op voorspelling met Sharpe ± SE; subperiodes 1990–2004 / 2005–2024.
  Waarschuwing: signaalselectie heeft look-ahead (McLean-Pontiff).
- **Replicatie (2)** KNS op 158 complete OSAP-signalen 1975–2024: schatten 1975–2004, test 2005–2024;
  L2 in signaalruimte met CV (contiguous folds, KNS cross-sectionele R²), sparse in signalen
  (Lasso op $\Sigma^{-1/2}\mu$ vs $\Sigma^{1/2}$) vs top-k PC's met L2; OOS R² en Sharpe van SDF-portefeuille.
- **(3) IPCA** op French 100 (size, BE/ME): eventueel als oefening.
- Verwachte afwijking (vast te leggen vóór draaien): niet-lineair > OLS OOS maar kleine R²-winst;
  L2-SDF in PC-ruimte > sparse in signaalruimte; winsten zwakker na 2005.
