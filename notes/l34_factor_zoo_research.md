# L34 — De factor zoo: onderzoeksnotities (gepauzeerd)

## Status bij pauze
- `lectures/06_34_factor_zoo.md` is AL geschreven (volledige code + theorie + toy + simulatie + replicatieblok),
  maar **nooit uitgevoerd**. Resultaatafhankelijke alinea's staan als placeholders `**[RESULTAAT-...]**`
  (SIM-A, SIM-B, 1, FIG, 2, 3A, 3B, 4, BRAK, OEF2). Het replicatieblok ("Verwachte afwijking") staat vast — niet wijzigen.
- Nog te doen: `HAP_OFFLINE=1 uv run jupytext --execute --to ipynb lectures/06_34_factor_zoo.md`, placeholders invullen
  met de outputgetallen, woorden tellen (doel 4000–6000), myst.yml (Deel VI `- title:` + `- file: lectures/06_34_factor_zoo.md`
  uit commentaar; lees myst.yml vlak ervoor opnieuw), cross-refs/cite-keys handmatig controleren.
- `.ipynb` bestaat nog niet (jupytext --execute maakt hem).

## Toegevoegde bib-entries (onderaan references.bib, al weggeschreven; DOI's via Crossref geverifieerd)
- `HouXueZhang2020` — Replicating Anomalies, RFS 33(5) 2019–2133, doi 10.1093/rfs/hhy131
- `JensenKellyPedersen2023` — Is There a Replication Crisis in Finance?, JF 78(5) 2465–2518, doi 10.1111/jofi.13249
- `FengGiglioXiu2020` — Taming the Factor Zoo: A Test of New Factors, JF 75(3) 1327–1370, doi 10.1111/jofi.12883
- `NovyMarx2013` — The Other Side of Value: The Gross Profitability Premium, JFE 108(1) 1–28, doi 10.1016/j.jfineco.2013.01.003
- `NovyMarxVelikov2016` — A Taxonomy of Anomalies and Their Trading Costs, RFS 29(1) 104–147, doi 10.1093/rfs/hhv063
- `BenjaminiYekutieli2001` — The Control of the FDR in Multiple Testing under Dependency, Ann. Stat. 29(4) 1165–1188,
  doi 10.1214/aos/1013699998 (pagina's via Wikipedia, Crossref gaf geen pagina's)
- `Holm1979` — A Simple Sequentially Rejective Multiple Test Procedure, Scand. J. Stat. 6(2) 65–70, geen DOI,
  url JSTOR 4615733 (gegevens via Wikipedia; JSTOR/Crossref niet bereikbaar)

Al aanwezig en gebruikt: HarveyLiuZhu2016, McLeanPontiff2016, HouXueZhang2015, FamaFrench2015, ChenZimmermann2022,
Cochrane2011, SantaClara2026, BenjaminiHochberg1995, BarrasScailletWermers2010, Black1993, LoMacKinlay1990,
FamaFrench1993, Carhart1997, ICI2020.

## Geverifieerde gepubliceerde getallen (met vindplaats)
- **McLean-Pontiff 2016**, samenvatting (Crossref-abstract): 97 variabelen; "Portfolio returns are 26% lower out-of-sample
  and 58% lower post-publication. The out-of-sample decline is an upper bound estimate of data mining effects. We estimate
  a 32% (58%–26%) lower return from publication-informed trading." Ook: grotere daling bij hogere in-sample rendementen;
  "investors learn about mispricing from academic publications".
- **Harvey-Liu-Zhu 2016** (volledige tekst, Duke-pdf): abstract "A new factor needs to clear a much higher hurdle, with a
  t-statistic greater than 3.0. We argue that most claimed research findings in financial economics are likely false."
  §3 (data): "we focus on 313 articles, among which are 250 published articles. We catalogue 316 different factors."
  Bespreking figuur 3: Bonferroni 1,96 → 3,78 in 2012 (4,00 in 2032); Holm volgt Bonferroni nauw; BHY (FDR 1%)
  stabiliseert op 3,39 na 2010; BHY 5%: 2,78 in 2012, 2,81 in 2032; "minimum threshold t-statistic for 5% significance is
  about 2.8". Subgroep 124 factoren (≥2000, Fama-MacBeth): Bonferroni 3,54, Holm 3,20, BHY 3,23 (1%) / 2,67 (5%).
  Tabel 4 (voorbeeld 10 p-waarden): cutoffs BHY 0,85%, Holm 0,60%, Bonferroni 0,5%. BHY met c(M)=Σ1/j.
- **Hou-Xue-Zhang 2020 (RFS)**, samenvatting (Crossref): 452 anomalieën; NYSE-breekpunten + VW; 65% haalt |t|≥1,96 niet,
  inclusief 96% van trading frictions; bij drempel 2,78 → 82%; gerepliceerde magnitudes veel kleiner.
  (NBER-versie w23394 wijkt af: 447 anomalieën, 64%, t=3 → 85% — niet gebruiken.)
- **Jensen-Kelly-Pedersen 2023**, samenvatting (Crossref): Bayesiaans model; "The majority of asset pricing factors
  (i) can be replicated; (ii) can be clustered into 13 themes ...; (iii) work out-of-sample in ... 93 countries; and
  (iv) have evidence that is strengthened (not weakened) by the large number of observed factors."
- **Cochrane 2011** abstract: "Now we have a zoo of new factors."
- **Feng-Giglio-Xiu 2020** abstract: "While most of these new factors are found to be redundant relative to the existing
  factors, a few—such as profitability—have statistically significant explanatory power beyond the hundreds of factors
  proposed in the past"; LASSO-selectie instabiel.
- **Novy-Marx 2013** abstract: "Profitability, as measured by gross profits-to-assets, has roughly the same power as
  book-to-market predicting the cross-section of average returns."
- **Novy-Marx-Velikov 2016** (NBER-samenvatting, deels): prestaties na transactiekosten; buy/hold spread meest effectieve
  kostenbeperking; anomalieën met lage omzet blijven significant.
- **Santa-Clara 2026** (LinkedIn, via WebFetch-samenvatting): >300 kenmerken in 2011; HLZ "with that many tries, a
  t-statistic of two means nothing and the bar should be three"; MP "fall by about a quarter out of sample and by well
  over half after publication"; What we don't know #4: "Why published anomalies decay, and by how much" + "if it is
  arbitrage, factor investing is self-defeating at scale; if it is mining, most of the literature is noise. We do not know
  the split."; #6 "Whether machine-learning alphas are real" (Gu-Kelly-Xiu).

## Niet kunnen verifiëren
- Chen-Zimmermann 2022 abstract (SSRN/nowpublishers 403; GitHub-README zonder cijfers). In tekst alleen SignalDoc-kolommen
  en eigen vergelijking gebruiken; zeggen dat het abstract niet kon worden ingezien.
- HXZ 2015 exacte aantallen anomalieën; FF2015 alleen via L26-citaat ("the value factor ... becomes redundant").
- MP-regressiecoëfficiënten zelf (alleen percentages).
- Santa-Clara-citaten komen uit een WebFetch-samenvatting (niet de ruwe pagina).

## Data/loaders (alles gecacht, offline OK)
- `hap.data.osap("portfolios")`: 1188 maanden × 212 signalen, 1926-01–2024-12, decimalen.
- `hap.data.osap("signaldoc")`: filter `Cat.Signal == "Predictor"` (212, sluit 1-op-1 aan op portfolios);
  kolommen `Year`, `SampleStartYear`, `SampleEndYear`, `T-Stat` (188 niet-NaN, min 1,77), `Stock Weight` (184 EW / 28 VW),
  `Signal Rep Quality` (158 good), `Predictability in OP` (165 clear / 47 likely). Numeriek maken met `pd.to_numeric`.
- `hap.data.french("F-F_Research_Data_5_Factors_2x3")` (vanaf 1963-07) + `"F-F_Momentum_Factor"` (kolom `Mom`).
- Verkennende run (niet in lecture): per signaal gemiddelde in-sample 0,69%/m, OOS 0,41% (−40%), post 0,30% (−57%);
  in-sample t>1,96: 88%, t>3: 58%; post t>1,96: 30%. FF5+UMD alfa 1963–2024: |t|>1,96 167, >3 123, Bonferroni 99 van 212
  (dus ~47%, mogelijk géén minderheid bij BHY → als afwijking bespreken; post-publicatie-alfa's ook gerapporteerd).

## Plan (zoals in het geschreven bestand)
- Toy 1: t = A 4,10 (echt), B 2,79, C 2,70, D 2,45, E 2,20, F 1,60, G 1,10, H 0,80, I −0,50, J −1,30 →
  naïef ABCDE, t>3 A, Bonferroni A (drempel 2,807), Holm AB, BH ABCD, BHY A (c(10)=2,929).
- Toy 2: α̂=1%, t=2,5, s=0,4%, prior N(0,τ²): τ=0,4% → 0,5% (SD 0,283%, P>0 = 0,961); τ=0,2% → 0,2%.
- Theorie: FWER/FDR; Bonferroni+Holm (bewijs); BHY onder afhankelijkheid (bewijs); HLZ-aanpak; truncatie
  E[t|t>c]=δ+λ(c−δ), daling D(δ) (D=100%/60%/28,5%/8,7%/1,4% bij δ=0/1/2/3/4); MP-decompositie; normale shrinkage +
  corollarium selectie; EB-momenten; JKP; FF5-waarderingsidentiteit; q-model (investerings-FOC, propositie met bewijs);
  FGX double selection; Novy-Marx-Velikov; smart beta (verwijs L25, ICI2020).
- Simulatie (a): 300 onderzoekers × 20 nulsignalen, 240/60/240 maanden, publiceer t>2 → histogram + afgeknotte normale;
  daling-curve D(δ) vs simulatie met MP-lijnen 26/58%. (b) 300 signalen (50% nul, rest N(0,4%;0,3%)), 500 universa,
  RMSE ruw vs EB en bias na selectie.
- Replicatie: (1) MP-panel met signaal-FE en per maand geclusterde SE; (2) t-verdeling in-sample vs post + HLZ-drempels
  (M=212); (3a) EB met nul-gecentreerde prior, overlevers; (3b) afgeknotte-normale MLE op gerapporteerde T-Stat → voorspelde
  daling door selectie vs waargenomen; (4) FF5+UMD-alfa's (1963–2024 en post-publicatie) met Bonferroni/Holm/BH/BHY.
- Oefeningen: (1) δ voor 26%/58%; (2) MP met vijfjaarsperiode-FE; (3) Sharpe 0,5 → jaren voor t=1,96/3/3,78; impliciete M bij 3,78 (~319).
- Labels: pagina `06-34-factor-zoo`; cross-refs o.a. `thm-industrie-bh`, `prop-sdf-unificatie-b-lambda`,
  `eq-fama-french-factoren`, `05-33-fama-vs-shiller` (bestaat nog niet), `01-03-williams-ddm`, `04-24-microstructuur`.
