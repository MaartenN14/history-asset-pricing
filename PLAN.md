# PLAN — Geschiedenis van asset pricing als QuantEcon-lectures

Bron van de rode draad: Pedro Santa-Clara, *What I learned about asset pricing* (LinkedIn, 2026),
<https://www.linkedin.com/pulse/what-i-learned-asset-pricing-pedro-santa-clara-apjce/>.
Stijlvoorbeeld: *Advanced Quantitative Economics with Python* (Sargent & Stachurski),
<https://python-advanced.quantecon.org/intro.html>.

Dit document is de bron van waarheid voor alle agents. `STYLE.md` (door de stijl-agent) regelt de vorm;
dit document regelt de inhoud en de volgorde.

## 1. Vaste keuzes

| Onderwerp | Keuze |
|---|---|
| Taal | Lecturetekst in het **Nederlands**. Vaktermen mogen Engels blijven (stochastic discount factor, momentum, carry) waar een Nederlandse vertaling gekunsteld is; eerste keer kort toelichten. Code, variabelen en docstrings in het Engels. |
| Formaat | **Jupyter Book 2 (MyST)**. Elke lecture is een MyST-`.md` in `lectures/`, gepaard (jupytext) met een `.ipynb` waarin de gebruiker werkt en debugt. |
| Data | **Gratis echte data met lokale cache** (`data/cache/*.parquet`, gecommit). Loaders in `src/hap/data.py`. Simulatie waar geen data bestaat. Geen WRDS/CRSP. |
| Niveau | **PhD-niveau wiskunde, intuïtie voorop.** Elke afleiding begint met "waarom zou dit waar zijn?" en eindigt met code/figuur die het resultaat tastbaar maakt. |
| Omvang | ~37 lectures, één per hoofdonderwerp, chronologisch zoals de post. Richtlengte per lecture: 4000–6000 woorden tekst + code + oefeningen. |
| Oefeningen | 2–4 oefeningen op problem-set-niveau per lecture, met uitwerkingen in opklapbare blokken. |
| Bronnen | `references.bib` met DOI/links; per lecture wordt het kernresultaat van 1–2 papers **gerepliceerd** (tabel/figuur) op gratis data of via simulatie. |
| Tooling | `uv` voor projectbeheer; `git` met één commit per lecture; elke lecture wordt end-to-end uitgevoerd als test. |

## 2. Rode draad

De post is chronologisch én thematisch: elk tijdvak levert (a) een **theorie**, (b) een **machine/dataset**, en
(c) een **barst** die het volgende tijdvak motiveert. Drie motieven lopen door alles heen en moeten in elke
lecture zichtbaar terugkomen waar relevant:

1. **De standaardfout van 2%.** Het gemiddelde rendement is met een eeuw data nog steeds slecht gemeten;
   variantie daarentegen is goed meetbaar. Dit verklaart waarom volatiliteit voorspelbaar is en rendement
   nauwelijks, waarom de equity premium een puzzel blijft, en waarom de factor zoo mogelijk is.
2. **Risico versus vergissing.** Chicago (Fama: tijdvariërende discontovoeten) tegenover Yale/Harvard
   (Shiller, Shleifer: mispricing en limits of arbitrage). Beide zijn het eens over de feiten.
3. **Van theorie-met-tests naar feiten-met-concurrerende-theorieën.** CAPM → SDF-pluralisme → machine learning
   zonder theorie → flows en inelastische markten.

Praktijkmotief (Santa-Clara): *"Everything I made that lasted came from bearing risk that was priced.
Everything I lost came from thinking I knew something the price did not."*

Elke lecture opent met een blok **"Waar we zijn in het verhaal"** (jaartal, wat we al weten, welke vraag open
staat) en sluit met **"Wat er brak, en wat daarna kwam"** (brug naar de volgende lecture).

## 3. Lecture-overzicht

Naamgeving: `lectures/<deel>_<nr>_<slug>.md`, bijv. `lectures/02_07_capm.md`. Nummering is doorlopend (L0–L37).

### Deel 0 — Toolkit

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L0 | `00_00_setup` | Opzet, data en conventies | Projectstructuur, `hap`-pakket, databronnen (French, Shiller, FRED, Goyal-Welch, OSAP, GSW, yfinance), notatie | alle loaders | — |
| L1 | `00_01_rendementen` | Rendementen en hun statistiek | Log vs. simpel, annualisatie, √t, standaardfout van het gemiddelde (**het 2%-motief**), autocorrelatie, dikke staarten | Shiller 1871–, French markt 1926– | Fisher-Lorie ~9% nominaal, SE ≈ 2% |

### Deel I — Before there was a field (1863–1959)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L2 | `01_02_bachelier` | Regnault, Bachelier en de random walk | √t-schaling, Brownse beweging, diffusievergelijking, Bachelier-optieformule; Cowles, Working, Kendall: variance-ratio- en runs-tests | Shiller, French daily | Regnault √t-wet; Cowles 1933 (voorspellers verslaan de markt niet — simulatie/French); Kendall 1953 autocorrelaties |
| L3 | `01_03_williams_ddm` | Williams en het dividend discount model | Present value, Gordon-groei, de identiteit prijs = verwachte dividenden / discontovoet; voorbereiding op Campbell-Shiller | Shiller | P/D-ratio versus gerealiseerde dividendgroei |
| L4 | `01_04_markowitz` | Markowitz, Roy en Tobin | Mean-variance, efficient frontier, diversificatie als covariantiebeheer, safety-first, separatiestelling; schattingsfout in gemiddelden (Michaud-effect) | French 10 industrieën / 25 portefeuilles | Frontier in-sample vs. out-of-sample; 1/N |

### Deel II — The Chicago–MIT decade (1960–1973)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L5 | `02_05_crsp_tape` | De CRSP-tape: data als machine | Wat een rendementsdatabase is (delistings, survivorship, total return), Compustat, Fisher-Lorie | French markt, size-portefeuilles | Fisher-Lorie cumulatieve rendementen 1926– |
| L6 | `02_06_efficiente_markten` | Fama en de efficiënte markt | Fama 1965/1970, drie vormen, joint hypothesis, martingaal vs. random walk, Samuelson 1965 | French daily/monthly | Autocorrelaties, variance ratios (Lo-MacKinlay) |
| L7 | `02_07_event_studies` | De event study | FFJR 1969, Ball-Brown 1968; marktmodel, abnormale rendementen, CAR, standaardfouten, clustering | yfinance (recente events) + simulatie | FFJR-stijl CAR rond aankondigingen |
| L8 | `02_08_capm` | Het CAPM | Sharpe-Lintner-Mossin-Treynor afleiding, Black zero-beta, Jensen-alpha, Sharpe-ratio, Black-Jensen-Scholes, Fama-MacBeth 1973 | French 25 size/BM, bèta-gesorteerde portefeuilles | Security market line te vlak (BJS 1972); Fama-MacBeth |
| L9 | `02_09_black_scholes` | Black-Scholes-Merton en de CBOE | Replicatie, PDE, risiconeutrale waardering, Greeks, implied volatility; Merton 1973 | yfinance optieketens (S&P 500 ETF) | Implied-volatility-oppervlak; delta-hedge-simulatie |

### Deel III — Theory and first cracks (1973–1985)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L10 | `03_10_merton_icapm` | Merton: continue tijd en het ICAPM | Merton 1969/1971/1973, HJB, myopische vs. hedging-vraag, ICAPM | simulatie | Merton-portefeuille onder stochastische opportunity set |
| L11 | `03_11_apt_no_arbitrage` | Ross, APT en de fundamentele stelling | APT, factorstructuur, Cox-Ross-Rubinstein binomiaal, Harrison-Kreps-Pliska: geen arbitrage ⇔ martingaalmaat; "twee dingen met dezelfde payoff hebben dezelfde prijs" | French factoren, simulatie | Binomiaal → BS-convergentie; APT-schatting via PCA op French 25 |
| L12 | `03_12_consumptie_capm` | Lucas, Breeden en de SDF | Lucas 1978 boom, Euler-vergelijking, CCAPM, Hansen-Singleton GMM | FRED consumptie, Shiller | Lucas-boom prijsfunctie; GMM-schatting van γ |
| L13 | `03_13_equity_premium_puzzle` | Mehra-Prescott en Hansen-Jagannathan | Equity premium puzzle, risk-free rate puzzle, HJ-bounds, "risk aversion in the thirties" | FRED consumptie, Shiller | HJ-bound-figuur; vereiste γ |
| L14 | `03_14_roll` | Roll: de critique en de R² | Roll 1977 (CAPM niet toetsbaar), Roll 1984 (sinaasappelsap), Roll 1988 (R²) | French, yfinance, weerdata optioneel | R² van marktmodellen; efficiëntie van de proxy |
| L15 | `03_15_shiller_excess_volatility` | Shiller en LeRoy-Porter: excess volatility | Variance bounds, ex-post rationele prijs, kritiek (Kleidon, Marsh-Merton) en antwoord | Shiller | Shiller 1981 figuur: P vs. P* |
| L16 | `03_16_vroege_anomalieen` | Basu, Banz en Rosenberg | P/E, size, B/M; BARRA-risicomodellen; datamining-waarschuwing | French size/BM/E-P portefeuilles | Size- en waarde-premies 1963– |
| L17 | `03_17_termijnstructuur_real_options` | Brennan-Schwartz, Vasicek, CIR en Longstaff-Schwartz | Affiene modellen, real options (mijn), least-squares Monte Carlo | FRED/GSW yields | Vasicek-fit; LSM voor Amerikaanse put |

### Deel IV — The empirical turn (1985–2000)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L18 | `04_18_fama_french` | Fama-French 1992/1993 | Sorts, SMB/HML-constructie, drie-factormodel, GRS-toets, LSV-mispricing-debat | French 25 + factoren | FF 1993 tabel; GRS |
| L19 | `04_19_momentum` | Jegadeesh-Titman, Carhart en momentum crashes | Constructie, Carhart 4F, Fama's "premier embarrassment", Barroso-Santa-Clara 2015 | French momentum-portefeuilles | JT 1993 winners-losers; crash 2009; vol-managed momentum |
| L20 | `04_20_voorspelbaarheid` | Voorspelbaarheid van rendementen | FF 1988, Campbell-Shiller-decompositie, Stambaugh-bias, Goyal-Welch OOS, Cochrane 2008, Ferreira-Santa-Clara sum-of-parts | Goyal-Welch, Shiller | Lange-horizon regressies; OOS R²; sum-of-parts |
| L21 | `04_21_volatiliteit` | ARCH, GARCH, realized volatility en de VIX | Engle, Bollerslev, ABDL realized vol, 1987, smirk, VIX; MIDAS risk-return (Ghysels-Santa-Clara-Valkanov) | French daily, FRED VIX | GARCH-fit; realized vol; MIDAS risico-rendement |
| L22 | `04_22_risk_management` | VaR, RiskMetrics en LTCM | VaR/ES, backtests, "leverage + mark-to-market + deadline = ruïne", convergence trades | French daily, FRED spreads | VaR-backtest 1998; LTCM-stijl spread-trade-simulatie |
| L23 | `04_23_behavioral` | Behavioral finance en limits of arbitrage | Prospect theory, De Bondt-Thaler, myopic loss aversion, DSSW noise traders, Shleifer-Vishny, Odean, BSV/DHS/HS | French lange-termijn reversal, simulatie | DSSW-simulatie; long-term reversal |
| L24 | `04_24_microstructuur` | Kyle, Glosten-Milgrom en liquiditeit | Adverse selectie, Kyle-λ, spreads, Amihud, Pástor-Stambaugh, Budish | yfinance daily (Amihud), simulatie | Kyle-evenwicht; Amihud-illiquiditeit tijdreeks |
| L25 | `04_25_industrie` | De industrie als financier: indexfondsen, DFA, AQR | Jensen 1968, Carhart 1997, FF 2010 bootstrap; kosten en belastingen; passief > actief in 2019 | French factoren + gesimuleerde fondsen | Bootstrap-alpha-verdeling |

### Deel V — The pluralist field (2000–2013)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L26 | `05_26_sdf_unificatie` | Cochrane: p = E[mx] | SDF, bèta-representaties, mean-variance-frontier, HJ-bounds, factormodellen als SDF, GMM-toetsen | French 25 + factoren | SDF-schatting met FF-factoren |
| L27 | `05_27_drie_antwoorden` | Habit, long-run risk en rampen | Campbell-Cochrane, Bansal-Yaron (Epstein-Zin), Barro/Rietz; observationele equivalentie | simulatie, FRED | Elk model gesimuleerd: equity premium, P/D, voorspelbaarheid |
| L28 | `05_28_termijnstructuur_premies` | Fama-Bliss, Cochrane-Piazzesi en het string-model | Expectations hypothesis faalt, forward-rate-factor, Santa-Clara-Sornette | GSW yields | Fama-Bliss en CP-regressies |
| L29 | `05_29_opties_crashrisico` | Opties en crashrisico | Santa-Clara-Yan 2010, Saretto-Santa-Clara 2009 (marges), variance risk premium | yfinance opties, FRED VIX | Variance risk premium; short-put strategie |
| L30 | `05_30_wisselkoersen` | Wisselkoersen: risk sharing, carry, momentum, value | Brandt-Cochrane-Santa-Clara 2006, Barroso-Santa-Clara 2015, UIP-puzzel | FRED wisselkoersen en rentes | Carry-portefeuilles; risk-sharing-index |
| L31 | `05_31_portfolio_choice` | Parametrische portefeuilles en idiosyncratisch risico | Brandt-Santa-Clara 2006, Brandt-Santa-Clara-Valkanov 2009, Goyal-Santa-Clara 2003 | French 25/100, OSAP | Parametric portfolio policy; average variance-regressie |
| L32 | `05_32_intermediaries` | 2008 en intermediary asset pricing | Brunnermeier-Pedersen, He-Krishnamurthy, Adrian-Etula-Muir | He-Kelly-Manela factor, FRED | Cross-sectie met intermediary-factor |
| L33 | `05_33_fama_vs_shiller` | Fama, Shiller en "Discount Rates" | 2013 Nobel; dezelfde feiten, twee theorieën; Cochrane 2011 | Shiller, Goyal-Welch | Tijdvariërende discontovoeten vs. sentiment |

### Deel VI — The factor zoo and the machines (2011–2026)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L34 | `06_34_factor_zoo` | De factor zoo | Harvey-Liu-Zhu (t≥3), McLean-Pontiff (decay), Hou-Xue-Zhang, FF5, smart beta | OSAP (Chen-Zimmermann), French FF5 | Post-publicatie-decay; multiple-testing-drempels |
| L35 | `06_35_machine_learning` | Machine learning in de cross-sectie | Gu-Kelly-Xiu, IPCA, Kozak-Nagel-Santosh, Martin-Nagel | OSAP + French | Penalized regression vs. OLS OOS-R²; sparse SDF |
| L36 | `06_36_inelastische_markten` | Demand systems en inelastische markten | Koijen-Yogo, Gabaix-Koijen ($1 flow → $5), passief beleggen | FRED/Fed flow of funds, Shiller | Flow-prijs-elasticiteit illustratie |

### Deel VII — The machines, again (2026)

| # | Slug | Titel | Kern | Data | Replicatie |
|---|---|---|---|---|---|
| L37 | `07_37_llms_en_efficientie` | LLM's, advies en efficiëntie | Grossman-Stiglitz, D'Acunto et al., Lopez-Lira-Tang, Cao et al., Eisfeldt et al.; halfwaardetijd van informatie | yfinance, simulatie | ChatGPT-event-study-stijl; Grossman-Stiglitz-evenwicht |

### Synthese

| # | Slug | Titel | Kern |
|---|---|---|---|
| L38 | `08_38_wat_we_weten` | Wat we weten | De 11 stellingen uit de post, elk met één empirische demonstratie en verwijzing naar de lecture waar het bewezen werd |
| L39 | `08_39_wat_we_niet_weten` | Wat we niet weten | De 13 open vragen, elk met de data die de puzzel laat zien en de concurrerende verklaringen |

## 4. Databronnen (gratis)

| Bron | Inhoud | Loader |
|---|---|---|
| Kenneth French Data Library | Factoren (FF3/5, momentum), portefeuilles op size/BM/momentum/E-P, industrieën, daily/monthly, internationaal | `hap.data.french(name)` |
| Shiller online data | S&P prijs, dividenden, winsten, CAPE, rente, 1871– | `hap.data.shiller()` |
| Goyal-Welch predictors | Voorspellers 1871–, jaarlijks/maandelijks | `hap.data.goyal_welch()` |
| FRED | Consumptie, CPI, rentes, VIX, wisselkoersen, spreads | `hap.data.fred(series)` |
| Gürkaynak-Sack-Wright | Zero-coupon yields 1961– | `hap.data.gsw()` |
| Open Source Asset Pricing (Chen-Zimmermann) | 200+ anomalie-portefeuilles | `hap.data.osap()` |
| He-Kelly-Manela | Intermediary capital factor | `hap.data.hkm()` |
| yfinance | Recente prijzen, optieketens | `hap.data.yahoo(...)` |

Alle loaders schrijven naar `data/cache/` (parquet) en lezen bij voorkeur uit de cache; `HAP_OFFLINE=1` verbiedt downloads.

## 5. Werkwijze

1. **Stijl-agent (Opus)** schrijft `STYLE.md` (opbouw, notatie, admonitions, citatiestijl, code-conventies,
   figuurstijl), een templatelecture, `references.bib`-conventies, `myst.yml`, en het skelet van `src/hap/`.
2. **Bouw-agents (Opus)** werken lectures één voor één uit volgens `PLAN.md` + `STYLE.md`; elke lecture
   wordt uitgevoerd (`uv run jupytext --execute` / `nbclient`) voordat hij wordt gecommit.
3. **Review-agent** toetst per lecture: rode draad aanwezig, notatie conform, replicatie klopt, oefeningen
   met uitwerkingen, `.md` en `.ipynb` gesynchroniseerd.
4. Volgorde van bouwen: L0–L1 eerst (toolkit en dataloaders), daarna delen I–VII in volgorde, synthese als laatste.
