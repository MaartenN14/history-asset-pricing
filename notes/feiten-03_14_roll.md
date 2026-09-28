STATUS 03_14_roll F2 open=1

# Feitencontrole 03_14_roll

Gecontroleerd: `lectures/03_14_roll.md` volledig, tegen `uv run python tools/nb_outputs.py
lectures/03_14_roll.ipynb` (HAP_OFFLINE=1), `lectures/03_13_equity_premium_puzzle.md` en
`lectures/03_15_shiller_excess_volatility.md` (volledig, als vorige/volgende), de
aangehaalde plekken in `lectures/02_08_capm.md`, `lectures/01_04_markowitz.md`,
`lectures/00_00_setup.md`, `lectures/00_01_rendementen.md`, `lectures/02_07_event_studies.md`
en `lectures/04_18_fama_french.md`, `references.bib`, en externe bronnen (webzoekopdrachten)
voor de cijfers van Roll (1977, 1984, 1988) en Shanken (1987).

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Waar we zijn in het verhaal | "Jaartal. 1977–1988." + "De toetsen van Black, Jensen, Scholes, Fama en MacBeth vonden een lijn die te vlak is." + "consumptiemodellen uit [](#03-13-equity-premium-puzzle) konden de premie ... niet verklaren" | `lectures/02_08_capm.md` r.51/60-61 ("... in de stijl van Black, Jensen en Scholes en van Fama en MacBeth" / "de lijn was te vlak"); `lectures/03_13_equity_premium_puzzle.md` r.983-999 ("Waar het breekt") | ok | — |
| Overzicht | "In maart 1977 publiceerde Richard Roll een kritiek van bijna vijftig pagina's ... {cite}`Roll1977`" | `references.bib` r.516-524 (JFE 1977, vol. 4, nr. 2, pp. 129-176 = 48 pag.); web (ideas.repec.org, JFE v4y1977i2p129-176): maart 1977 bevestigd | ok | — |
| Overzicht | "Het weer in Florida verklaarde weinig van de prijs van sinaasappelsap {cite}`Roll1984`" (jaartal 1984, geen specifiek getal) | `references.bib` r.527-535 (Roll1984, *Orange Juice and Weather*, AER 1984); web: Roll (1984) vond adjusted R² ≈ 0,02 voor weer | ok | Klopt kwalitatief en is bewust vaag: de lecture citeert geen specifiek percentage en meldt zelf (r.626-628) dat de primaire tekst niet is ingezien; de gebruikte secundaire bron `BoudoukhRichardsonShenWhitelaw2007` bestaat en behandelt dit onderwerp (bib r.2595-2603). |
| Overzicht | "markt en industrie verklaarden weinig van de rendementen van losse aandelen {cite}`Roll1988`" | zie sectie "Rolls tweede vraag" hieronder | ok | — |
| Toy-voorbeeld | Alle getallen (λ=0,368; δ=−0,01248; bèta's 1,6053/0,0921; μ_z=3,39%; helling 6,61%; gelijkgewogen bèta's 1,8333/0,1667; helling 6,0%; intercept 3,33%; R²=0,9868) | `tools/nb_outputs.py` cel 2 (exact gelijk, incl. λ=0,368, δ=−0,0125 afgerond, R²=0,9868); intern consistent met `lectures/01_04_markowitz.md` (A=128,125; B=7,0625; C=0,51125; D=15,625; w_tan=(1/3;2/9;4/9) bij R^f=2%) | ok (per sectie) | — |
| Theorie: Opzet | "[](#00-00-setup)", "Het subscript $m$ staat in deze lecture voor de marktportefeuille, niet voor de stochastic discount factor" (dubbele betekenis expliciet gemeld) | `lectures/00_00_setup.md` Notatie-tabel (r.163-225): $m$ = SDF | ok | Auteur meldt de dubbele betekenis zelf, zoals STYLE §11 vereist (H5). |
| Theorie: Rolls stelling | {prf:ref}`prop-capm-beta` en {prf:ref}`thm-capm-zerobeta` bestaan en zeggen wat hier beweerd wordt | `lectures/02_08_capm.md` r.337-344 (prop-capm-beta: lijn door oorsprong ⇔ $p$ = tangentportefeuille) en r.372-385 (thm-capm-zerobeta, Black) | ok | — |
| Theorie: Bijna-efficiënte proxy's | "{cite:t}`RollRoss1994` ...", "Volgens {cite:t}`KandelStambaugh1995` ..." | `references.bib` r.2551-2571 (jaartallen 1994/1995 kloppen, titels passen bij de bewering) | ok | — |
| Theorie: Bijna-efficiënte proxy's | Alle getallen in de admonition-dropdown ({cite:t}`Stambaugh1982` obligaties/vastgoed/duurzame consumptiegoederen; {cite:t}`Shanken1987` proxy van aandelen+staatsobligaties, correlatie boven 0,7) | `references.bib` r.2573-2593; web (Boston Fed working paper, ScienceDirect): Shanken (1987) verwerpt de gezamenlijke hypothese CAPM-en-correlatie-boven-0,7 met een proxy van aandelen + staatsobligaties | ok | Shanken-claim expliciet extern geverifieerd en correct. |
| Theorie: Numerieke uitwerking (100 activa) | marktpremie 0,66%, volatiliteit 4,69%, Sharpe 0,49 p.j., ρ*=0,62 | `tools/nb_outputs.py` cel 3: 0,6608 / 4,6931 / 0,4877 / 0,6225 | ok | — |
| Theorie: Numerieke uitwerking | "tot 1,7 keer de ware premie bij correlatie 0,75. Daarna valt de helling snel naar nul bij correlatie 0,62" (dit is de door de schrijver gemelde correctie van "bijna driemaal") | `tools/nb_outputs.py` cel 4: hoogste helling/premie=1,715 bij correlatie 0,748; helling nul bij correlatie 0,623 | ok | De correctie naar 1,7×/0,75 is juist en komt exact overeen met de celuitvoer; het oude "bijna driemaal" stond niet meer in de tekst. |
| Theorie: tweede vraag ($R^2$) | "de gemiddelde gecorrigeerde $R^2$ is ongeveer 0,35 met maanddata en 0,20 met dagdata {cite}`Roll1988`" | web (Wiley/AFA, samenvatting Roll 1988 *R²*, JoF): "average adjusted R² is only about 0.35 with monthly data and 0.20 with daily data", voor grote aandelen | ok | Extern geverifieerd tegen de bron (samenvatting): correct. |
| Theorie: tweede vraag | "Rolls rede van 1987" | web: Roll (1988) *R²* was zijn Presidential Address 1987 voor de American Finance Association, gepubliceerd in 1988 | ok | Correct — geen verwarring tussen redejaar (1987) en publicatiejaar (1988). |
| Theorie: tweede vraag | "Die lezing ontlenen we aan {cite:t}`BoudoukhRichardsonShenWhitelaw2007`, want de primaire tekst hebben we niet kunnen inzien." | `references.bib` r.2595-2603 (bestaat, juiste titel/jaar) | ok | — |
| Theorie: tweede vraag | Verwijzing "Hier keert [de standaardfout van 2%](#00-01-rendementen) om" | `lectures/00_01_rendementen.md` r.364-406 (sectielabel is `sec-rendementen-standaardfout`, niet `00-01-rendementen`) | onzeker (niet meegeteld in open) | De link wijst naar het paginalabel van de hele lecture i.p.v. naar het specifieke sectielabel `sec-rendementen-standaardfout`; de bewering zelf (dat daar de standaardfout van 2% staat) klopt inhoudelijk, dus dit is een precisiepunt, geen feitenfout. |
| Simulatie | Alle getallen in de samenvattingstabel (intercepten 0,08%/−0,34%, band 0,22%–1,0%, sd 0,14–0,20%, mediaan 0,05%→−0,11%/0,14%, σ_m/√T=0,19%) | `tools/nb_outputs.py` cel 7 | ok | — |
| Replicatie: admonition | Bron- en jaartalvermeldingen Roll1977/Roll1988; dataomschrijving (25 size/BM, CRSP-index, 10/49 industrieportefeuilles, 50 aandelen uit [](#02-07-event-studies)) | `lectures/02_07_event_studies.md` r.777-823 (exact dezelfde 50 tickers, uit dezelfde SPLITS-lijst) | ok | Tickerlijst van `INDUSTRY_49`/`INDUSTRY_10` in 03_14 komt letterlijk overeen met de 50 unieke tickers uit de splitsingenlijst van 02_07. |
| Replicatie: tautologie 25 size/BM | Steekproef "1963-07 tot 2026-07"; som |gewichten| tangent 13,8; intercept/helling/R² per proxy (o.a. tangent Sharpe 1,39; Roll-Ross-proxy correlatie 0,89/Sharpe 1,23; CRSP helling −0,37%, intercept 1,16%, R²=0,08, gem. marktexcess 0,60% met SE 0,16%) | `tools/nb_outputs.py` cel 9-10 | ok | Intercept 1,16% komt bovendien overeen met het getal dat `lectures/04_18_fama_french.md` r.23-24 aanhaalt voor dezelfde CRSP-regressie. |
| Replicatie: $R^2$ van portefeuilles en aandelen | Portefeuille-R² (0,54/0,62/0,73); aandelen-R² (25%/35%/40% maand, 33%/41% dag); jaartabel 2002-2025 (laagste 2017=0,15, hoogste 2020=0,56; hoogste jaren 2020/2011/2022/2008 met vol. 24-40%; correlatie 0,82) | `tools/nb_outputs.py` cellen 12, 14, 18-19 | ok | Rangorde van de vier hoogste jaren komt exact overeen met de celuitvoer. |
| Replicatie: $R^2$ | Rijlabel "49 industrieën" bij de gemiddelde-$R^2$-tabel/figuur | `tools/nb_outputs.py` cel 12: `aantal`=47 voor die rij (2 van de 49 kolommen zijn na `dropna` weg) | ok, met kanttekening | Geen feitenfout: het getal 47 staat zelf zichtbaar in de "aantal"-kolom van dezelfde tabel, dus zelfverklarend; "49 industrieën" is de naam van de French-dataset, niet een telling. Geen aanpassing nodig. |
| Replicatie: slotvergelijking | Tabel origineel/hier: (a) R²=1/intercept 0 vs. 1,000/0,000; (b) 0,35/0,20 vs. 0,349/0,411 | `tools/nb_outputs.py` cel 16 | ok | — |
| Wat er brak | "R² van 1 ... CRSP-index een $R^2$ van 0,08"; "markt en industrie maar 35 tot 40%" | `tools/nb_outputs.py` cellen 10, 14 | ok | — |
| Wat er brak | "{cite:t}`JagannathanWang1996` met de groei van arbeidsinkomen"; "{cite:t}`MorckYeungYu2000` lezen bedrijfsspecifieke beweging als informatie" | `references.bib` r.2606-2625 (jaartallen/titels kloppen: conditional CAPM met arbeidsinkomen resp. synchronous stock movements) | ok | — |
| Wat er brak | "Dat onderzochten Shiller en LeRoy en Porter, in [](#03-15-shiller-excess-volatility)." | `lectures/03_15_shiller_excess_volatility.md` r.18-31, 59-65: Shiller (1981) en LeRoy-Porter (1981), zelfde onderwerp, zelfde "Waar we zijn"-verwijzing terug naar 03-14-roll | ok | — |
| Oefening ex-roll-1 | Alle handberekeningen (d, Σd, Var(R_d)=0,00023867, Cov=0,0011259, c*=4,718, ρ*=0,785, w*=(0,302;0,002;0,696), Sharpe-ratio 78,5%, intercept 0,07333) | `tools/nb_outputs.py` cel 17 | ok | — |
| Oefening ex-roll-2 | "0,15 in 2017 tot 0,56 in 2020", "24 tot 40%", "correlatie ... 0,82" | `tools/nb_outputs.py` cellen 18-19 | ok | — |
| Oefening ex-roll-3 | "37%", intercept 0,74%, helling 0,98%, gem. excess 2,55%; in-sample R²=1; CRSP R²=0,11; Sharpe 0,88 vs. 0,62 | `tools/nb_outputs.py` cel 20 | ok | — |
| Naadpunt (buiten deze lecture) | `lectures/04_21_volatiliteit.md` r.429-430: "Wie elke seconde meet, meet vooral *microstructuurruis*: de waargenomen prijs is de efficiënte prijs plus een fout $u$ (bid-ask bounce, afronding), zoals in [](#03-14-roll)." | `lectures/03_14_roll.md` volledig doorzocht op "bid-ask", "spread", "microstructu*", "bounce" — geen van deze termen komt voor; Roll(1984) in déze lecture is uitsluitend de sinaasappelsap-weerstudie (AER), niet de bid-ask-spreadschatter (die staat apart in `references.bib` als `Roll1984b`, r.3097-3105, en wordt in 03_14 niet aangehaald) | **niet herleidbaar** | 03_14_roll bevat geen bid-ask-spread- of microstructuurruis-inhoud (meer); de verwijzing in 04_21 is dus stale. Twee opties, niet zelf uitgevoerd: (1) één zin toevoegen in L14 (bijv. bij "Wat er brak" of een dropdown) die Rolls bid-ask-spreadschatter {cite}`Roll1984b` en de link met microstructuurruis kort noemt; of (2) de verwijzing in `04_21_volatiliteit.md` r.430 aanpassen naar een andere of geen cross-ref. |

## Samenvatting

Alle jaartallen, namen, citaties en getallen in `lectures/03_14_roll.md` zijn herleid tot
`tools/nb_outputs.py`, een getoonde handberekening, of een externe bron, en kloppen. De twee
open punten van de schrijver zijn nagelopen:

1. **Roll (1988) en Roll (1984, secundair).** De cijfers 0,35 (maand) en 0,20 (dag) voor
   Roll (1988) zijn extern geverifieerd tegen de samenvatting van het origineel en correct.
   Roll (1984, sinaasappelsap) wordt terecht zonder specifiek getal en met bronvermelding
   ("primaire tekst niet ingezien") aangehaald; de gebruikte secundaire bron bestaat en past.
   Er is in deze lecture geen Roll (1984) bid-ask-spreadformule om te controleren — zie het
   naadpunt hieronder.
2. **04_21_volatiliteit.md → 03_14_roll (microstructuurruis).** Bevestigd als stale
   cross-ref; zie de tabelrij "Naadpunt" hierboven voor de twee voorgestelde oplossingen.
3. **"1,7 keer de ware premie bij correlatie 0,75".** Correct en exact gelijk aan de
   celuitvoer (1,715 bij 0,748); de oude formulering ("bijna driemaal") is niet meer aanwezig.

Eén punt telt mee in `open=`: de stale verwijzing vanuit 04_21_volatiliteit.md. De
"49 industrieën"/aantal=47-kanttekening en de precisie van de `#00-01-rendementen`-link zijn
genoteerd maar niet meegeteld, omdat de onderliggende beweringen zelf kloppen.

STATUS 03_14_roll F2 open=1
