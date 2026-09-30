STATUS 06_36_inelastische_markten F4 open=2 punten=15

# Feitencontrole 06_36_inelastische_markten (F23)

Bronnen: nb_outputs (celuitvoer), nb_numbers (12 meldingen: toy-handstappen en geciteerde GK-getallen), handberekening, en externe controle voor de open punten uit rapport §F1 (HHL via AEA-abstract; KRY en KY via de werkversies; GK via zoekresultaten).

## Open punten (onjuist, onzeker)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie | status F4 |
|---|---|---|---|---|---|---|
| 1 | 578 | Figuurtekst: volatiliteit "tot ruim 24% bij $\zeta = 0{,}1$" | onjuist | cel 3: theorie 23,96, mediaan 23,95 | "bijna 24%" | opgelost: bijna 24% |
| 2 | 666 | "OLS heeft bij elke $T$ en $N$ een mediaan van 0,013, precies de kansgrens" | onjuist | cel 5: Zipf 0,0126 tot 0,0131; "bijna gelijk" 0,0001 (kansgrens 0,0001) | "bij Zipf 0,013 en bij bijna gelijke sectoren 0,0001, telkens de kansgrens" | opgelost: 0,013 (Zipf) en 0,0001 (bijna gelijk), telkens de kansgrens |
| 3 | 465 | GK vinden "multipliers tussen 3,5 en 8" | onjuist (waarschijnlijk) | GK2021: 3 tot 8 (zoekresultaten; Table 2: 7,1 en 5,3) | "tussen 3 en 8"; raakt ook r. 712 ("dezelfde bandbreedte") | opgelost: 3 tot 8, ook in Simulatie (spreiding 3 tot 8) |
| 4 | 791 | "Alleen de fondsaankopen hebben een duidelijk positieve helling" | onjuist | cel 8: beleggingsfondsen 5,9 ($t = 2{,}2$) | "De fondsaankopen hebben de duidelijkste positieve helling" | opgelost: duidelijkste positieve helling; beleggingsfondsen ook significant |
| 5 | 404-405 | latente vraag verklaart 81% van de variantie van rendementen, aanbodkant 12% | onzeker | KY-werkversie (SSRN 2537559): aanbod 8% (2008: 5,0%), aum-veranderingen 29%; 81/12 niet teruggevonden | tabel in de JPE-versie controleren of aanpassen | opgelost: 81/12 geschrapt, kwalitatief (grootste deel / klein deel) |
| 6 | 358 | institutioneel: meer dan \$100 miljoen, samen 68 procent van de beurs | onzeker | \$100 miljoen bevestigd (13F-drempel); 68% niet teruggevonden | bron per getal controleren | opgelost: 68% geschrapt, 13F-meldplicht als reden |
| 7 | 393 | VanDerBeck2026: prijsimpact per kwartaal drie keer zo groot als op lange termijn | onzeker | niet opgehaald | controleren, anders weglaten | opgelost: 'drie keer' geschrapt, alleen richting (lange termijn kleiner) |
| 8 | 62 | Santa-Clara: belangrijkste open vraag van dit decennium | onzeker | LinkedIn-post, niet opgehaald | parafrase controleren | verzacht: 'hoort bij de grote open vragen' |
| 9 | 74 | Shleifer: abnormaal rendement "groter naarmate indexfondsen meer moesten kopen" | onzeker | uit geheugen; Shleifers dwarsdoorsnee was zwak | verzachten of controleren | opgelost: tijdreeks na 1976 (indexfondsen), ~3% uit eigen tabel; kruisdoorsnede-bewering geschrapt |
| 10 | 852 | CHL (werkversie 2013): 5,0% junirendement na herindeling | onzeker | geen bron ingezien | controleren | open: getal in geciteerde codetabel, geen bron ingezien; ongewijzigd |
| 11 | 846-847 | Petajisto tabel 1: 10,3 (1990-2000) en 4,6 (2001-2005) | onzeker | consistent met gemiddelde 8,8; splitsing niet ingezien | controleren | open: consistent met 8,8; splitsing niet ingezien; ongewijzigd |
| 12 | 793 | pensioenfondsen en verzekeraars negatief "omdat ze tegen de markt in herbalanceren" | onzeker | hellingen niet significant ($t = -1{,}2$; $-1{,}0$); oorzaak niet getoetst | "wat past bij herbalanceren" | opgelost: 'niet significant, wat past bij herbalanceren' |
| 13 | 391 | KRY: elasticiteiten "tussen nul en één" | onzeker | hedgefondsen "rond 0,5" bevestigd (werkversie, rijkdomsgewogen); bereik niet letterlijk teruggevonden | bereik controleren | opgelost: 'ver onder twintig', hedgefondsen ~0,5 behouden |

## Juist (samengevat per sectie)

- Toy (r. 108-149): 50,4; 40,32; 40,8; 0,8; 4%; 5; 308; 0,26%; 0,32 = 1/3,08; vijftien keer (5/0,325 = 15,4); 87,5; 1,64; 0,49%; 0,61; "verdubbelt bijna" (0,325 naar 0,61). Cel 2 stemt overeen; exact evenwicht 3,95/0,259/0,487.
- Lemma en stelling (r. 248-301): bewijzen nagerekend; 0,4 voor 60/40; $p = 4\%$; 5% en 0,05%.
- CARA (r. 317-340): formule, bewijs en $R^f$ netto kloppen; $\zeta \approx 20$, honderd keer 0,2, een vijfde van de premie.
- KY-stelling (r. 370-394): $\zeta = 1 - \beta_0(1-w)$ en de voorwaarde kloppen; $\beta_0 = 1$ en $0$ kloppen.
- GIV-stelling en bewijs (r. 434-451): alle variantie- en covariantiestappen nagerekend; kansgrens 0,013 bij $N = 20$ Zipf, schijnbare multiplier 77 ("bijna 80").
- Excess volatility (r. 475-493): formules kloppen; cel 3: 7,0% en 13,4%, 1,9 keer, 93%, 18% bij $\zeta = 1$; halfwaardetijd ruim drie jaar (13,5 kwartalen).
- Passief, inkoop (r. 585-599): $(1/\zeta - 1)\Delta F$, 4 bij $\zeta = 0{,}2$. HHL (twee derde, 11 procent) bevestigd via AEA-abstract; ICI2020 "evenveel" conform 04_25 r. 22 en 85 (rapport-punt 1 en 2: opgelost).
- Simulatie (r. 620-713): GIV-mediaan 0,20 bij Zipf en $T \ge 104$; bijna gelijk 0,01 tot 0,07 (0,013 tot 0,069); hoogstens 1 op 5 (0,19); interval 0,12-0,51, multiplier ongeveer 2 tot 8; 400 kwartalen 0,15-0,29; figuurtekst klopt.
- Replicatie (r. 715-935): 298 kwartalen, ETF 1993, 7,3 ($t = 2{,}8$), $R^2$ 3% (2,6%), 16,4 ($t = 3{,}6$), alle sectoren $t = 1{,}0$; GK 7,08 (1,86) en 5,28 (1,10) bevestigd (7,1/1,9; 5,3/1,1); Tesla 51% in 23 handelsdagen; 3,1% ($t = 1{,}8$); $-4{,}0\%$ ($t = -1{,}55$); tabel 5,7/4,0 en 2,2/2,2; 14 toevoegingen geteld; Petajisto 8,8 en GS 0,8; GS 7,4% gepubliceerd voor de jaren negentig; Harris-Gurel bekend.
- Oefeningen: 1,25; 2; 0,7; 1,4; 1,43; 1,43%/0,43%; 0,05%/-0,95%; SE 0,074/0,146/0,040; T = 230/884/66; "bijna zestig jaar" (57,5); lead-lag 2,1; 14,0; -10,5; $t = -3{,}0$ kloppen met cellen 13-15.
- Tesla 16 november en 21 december 2020 en de datums in INCLUSIONS zijn consistent met de persberichten (geen nieuwe bron geraadpleegd).

## Cross-refs

| regel | verwijzing | status |
|---|---|---|
| 23 | 05-33-fama-vs-shiller, 06-35-machine-learning | juist (labels bestaan) |
| 342, 347 | 05-33 (SDF) en prop-fama-vs-shiller-equivalentie met $\xi$ | juist (05_33 r. 309-317) |
| 407 | 06-34-factor-zoo | juist |
| 488 | 03-15-shiller-excess-volatility | juist |
| 493 | 05-33-fama-vs-shiller | juist |
| 582 | 00-01-rendementen | juist |
| 589 | 04-25-industrie | juist (r. 22, 85: evenveel) |
| 601 | 02-06-efficiente-markten | juist (label bestaat) |
| 606-607 | 04-23-behavioral, 05-32-intermediaries | juist (labels bestaan) |
| 724, 866 | 02-07-event-studies, 50 aandelen | juist (02_07 r. 625, 851) |
| 958 | "Chicago-lezing", "Yale-lezing" | juist (05_33 r. 74, 79) |
| 970 | 07-37-llms-en-efficientie | juist (label bestaat) |
| diverse | prf:ref naar eigen stellingen | juist |
