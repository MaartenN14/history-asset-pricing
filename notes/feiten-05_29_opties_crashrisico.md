STATUS 05_29_opties_crashrisico F4 open=0 punten=15

# Feitencontrole 05_29_opties_crashrisico (F23)

Methode: `tools/nb_numbers.py` tegen de celuitvoer van `05_29_opties_crashrisico.ipynb`
(51 gemelde getallen, stuk voor stuk nagelopen), plus de vijf open punten uit
`notes/rapport-05_29_opties_crashrisico.md` §F1. Externe bronnen alleen voor die open
punten en voor getallen met bronvermelding zonder cel: NBER WP 10912 (Santa-Clara en Yan
2004, `w10912.pdf`) en de werkdocumentversie van Saretto en Santa-Clara
(`anderson.ucla.edu/.../santa_clara_option.pdf`).

## Samenvatting per sectie (juiste rijen gebundeld)

| nr | regel | bewering | oordeel | bron of cel | correctie |
|---|---|---|---|---|---|
| 1 | 122–163 | Toy-voorbeeld: alle tien getallen in de handberekening (m, E[m], R^f, q, premies, put/call-prijs en -rendement, VRP) | juist | cel 2 (tabel "met de hand"/"code", beide kolommen gelijk) | geen |
| 2 | 201–204 | "verlies van 86,6% op de put", "ruim twee derde van de aandelenpremie", "vrijwel de hele premie op variantie" | juist | afgeleid uit cel 2 (0,1336−1=−86,6%; 0,0449/... zie put; VRP 0,0332 vs premie 0,0832) | geen |
| 3 | 450–453 | sprongintensiteiten 0,165 (ℚ) en 0,078 (ℙ), aandelenpremie 10,1%, crashpremie 2,9% (SCY) | juist | NBER WP10912 r. 947, 973, 990 (exacte tekstmatch, incl. "iets minder dan een derde") | geen |
| 4 | 451, 920(bron) | gemiddelde sprong onder ℚ −31,6% (SCY) | juist | NBER WP10912 r. 920: "The average jump size is -31.6 percent" | geen |
| 5 | 461 | gerealiseerd overrendement S&P 500 in SCY-steekproef −2,2%/jaar | juist | NBER WP10912 r. 973: "-2.2 percent" (letterlijke match) | geen |
| 6 | 464 | standaardfout 7 jaar bij 18,3% vol: 0,183/√7=6,9 pp | juist | rekenkundig (0,183/2,6458=0,0692) | geen |
| 7 | 610–636 | kalibratie: kappa −0,30, sprongpremie 2,61%, diffusiepremie 3,5%, equity premium 6,11%, vol ℚ 21,4%, vol ℙ 18,3% | juist | cel 3 print | geen |
| 8 | 621–639 | smirk-tabel: 42,3% (1 mnd, 80% spot), 16,7% (1 mnd, ATM) | juist | cel 3 tabel (42.34, 16.73) | geen |
| 9 | 682–684 | RMSE bij ΔK=0,25 is 0,113, 57× die bij ΔK=2 | juist | cel 4 (0,11315 / 0,00198 = 57,2) | geen |
| 10 | 827–829 | crashes 0,076/jaar; put-premie 0,51; marge-eis 10,51 | juist | cel 6 print (0.0762, 0.5113, 10.5113) | geen |
| 11 | 868–873 | Sharpe verkoper 0,33 vs markt 0,36; scheefheid −10,5; kwantielen 0 tot 1,79 | juist na F4 (tekst nu 0,326 tegen 0,355, zoals de cel print) | cel 7 (0,326/0,355 op 3 decimalen — 0,355 ligt op de afrondingsgrens 0,35/0,36; −10,485; −0,003/1,793) | zie punt 15 hieronder |
| 12 | 882–887 | hefboom 0,904 (10×marge) en 0,80% uitgeschud; hefboom 1,808 (5×marge) en 80% uitgeschud; ruïne bij ≥58% | juist | cel 8 + prop-ruine (j*=0,05+0,0051+0,95/1,808=0,581) | geen |
| 13 | 909–910, 953–958 | Sharpe zonder crash 1,85, met crash 0,28; SE=√((1+1,85²/2)/20)=0,37; e^(−20·0,076)=0,22; 21,4% zonder crash | juist | cel 9 (1.852, 0.284, 0.214) + rekenkundig (0,368→0,37; e^-1,52=0,219→0,22) | geen |
| 14 | 1060–1093 | spot 764,29, r=3,82%; massa 99,1%/98,7%; scheefheid ℚ −1,23/−1,30; scheefheid ℙ (1990-2026) −0,61 kwartaal/−1,33 kwartaal | juist | cel 11–12 | geen |
| 15 | 1197–1211 | BTZ-tabel (helling, t, R² voor h=1,3,6,12, 1990-2007) en "t≤0,6" over 1990-2026 | juist | cel 14 (round(3) komt overeen, incl. horizon-12 rij 0,22/2,24/5,3%) | geen |
| 16 | 1250–1255 | VRP positief in 87% v.d. maanden; 1990-2026 geen helling significant | juist | cel 14 print (86,6%→87%) | geen |
| 17 | 1313–1329 | Cboe-tabel (vol, scheefheid, kurtosis, Sharpe+SE, drawdowns, bèta, alpha 1,3%/t=1,1) | juist | cel 16 (alle 12 cijfers matchen op afronding) | geen |
| 18 | 1421–1424, 1468–1477 | oefening 1 (0,9051; 0,0827; 0,0225; 0,1336) en oefening 2 (γ≈2,015; sprong ℚ −31,4%) | juist | cel 18–19 | geen |
| 19 | 1499–1511 | oefening 3: modelvrije scheefheid −2,1/−2,3 | juist | cel 20 (−2,1386/−2,2638) | geen |
| 20 | 24–26 | "Waar we zijn": VIX gemiddeld vier volatiliteitspunten boven de latere volatiliteit | juist | 02_09_black_scholes, cel "gemiddeld verschil (vol)" = 0,0399 (3,99 ≈ 4 punten) | geen |
| 21 | 349 | VRP op echte data "gemiddeld rond vier volatiliteitspunten" ([fig-black-scholes-vrp]) | juist | zelfde cel als 20 (0,0399) | geen |
| 22 | 308–311 | Bakshi-Kapadia-Madan: aandelen veel minder linksscheef dan de index (geen cijfer aangehaald) | juist | kwalitatieve, breed bekende bevinding uit BKM (2003); geen getal om te herleiden | geen |

## De vijf open punten uit rapport §F1 — opgelost

1. **Sharpe-SE 0,37.** √((1+1,85²/2)/20) = 0,3682 → "0,37" klopt (rij 13). Opgelost.
2. **SCY-tabel 18,3%.** NBER WP10912 (r. 920) noemt 18,3% expliciet "the average level of
   volatility" naast, niet inclusief, de sprongintensiteit (16,5%) en sprongomvang
   (−31,6%): het is de **diffusieve** volatiliteit $\sqrt{V_t}$, geen totaal inclusief
   sprongen. Overige SCY-cijfers (2,9%, 10,1%, −31,6%, −2,2%) kloppen exact, met vaak
   letterlijke tekstovereenkomst (zie rijen 3–5). **Onzeker/deels onjuist**: zie punt 14
   hieronder voor de precieze aanmerking op de tabelrij.
3. **Saretto-Santa-Clara 59,1%/−11,06.** Bevestigd, letterlijk, in de werkdocumentversie op
   `anderson.ucla.edu` (Santa-Clara en Saretto): "earns 59.1% per month on average, with a
   SR of 0.358 ... negative skewness of -11.062." De vroegere NBER-conferentieversie
   (2005) had nog 55%/−10,716 voor dezelfde strategie; de lecture citeert dus terecht een
   latere concept-versie. Opgelost, juist.
4. **Bakshi-Kapadia-Madan.** Geen getal aangehaald (zie rij 22); replicatie toetst
   inderdaad alleen het teken, wat expliciet zo staat in het replicatieblok
   ("Verwachte afwijking... negatief"). Geen correctie nodig.
5. **VIX/VRP vier volatiliteitspunten.** Bevestigd tegen 02_09_black_scholes (rijen
   20–21). Opgelost, juist.

## Aanmerkingen (open=0 na F4)

F4: punt 14 opgelost (SCY-kolom nu "18,3% diffusie"); punt 15 opgelost (drie decimalen uit de cel overgenomen, geen afronding meer op de grens).

14. **Regel 448, tabelrij "volatiliteit".** Bewering: `$18{,}3\%$ gemiddeld` (SCY-kolom)
    naast `$15\%$ diffusie, $18{,}3\%$ met sprongen` (eigen kolom). Het getal 18,3% zelf is
    juist geciteerd (zie punt 2), maar de plaatsing naast de eigen kolom nodigt uit tot een
    appels-met-peren-vergelijking: SCY's 18,3% is de diffusieve component (hoger dan de
    hier gekozen 15%), niet de totale volatiliteit inclusief sprongen (die bij SCY niet in
    de aangehaalde passage staat). Oordeel: **onzeker** (het getal klopt, de suggestie van
    vergelijkbaarheid niet). Voorgestelde correctie: "$18{,}3\%$ diffusie" ipv "$18{,}3\%$
    gemiddeld" in de SCY-kolom.
15. **Regel 868–869, "Sharpe-ratio van 0,33, tegen 0,36".** Celuitvoer (`sim_summary.round(3)`)
    geeft 0,326 en 0,355. 0,355 ligt exact op de grens tussen "0,35" en "0,36" bij afronden
    op twee decimalen; met de opgeslagen precisie (drie decimalen) is niet vast te stellen
    welke kant de vierde decimaal op valt. Oordeel: **onzeker**. Voorgestelde correctie:
    print `sim_summary` met vier decimalen, of schrijf "0,33 tegen 0,35 à 0,36".
