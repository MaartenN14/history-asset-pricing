STATUS 02_07_event_studies F5c words=4885 prose=PASS open=0 cijfer=8,8 min=8,5

# Beoordeling 02_07_event_studies: De event study

## Eindcijfer: 8,2

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8,5 + 0,2·8 + 0,15·8,5 + 0,1·8 + 0,1·7 + 0,1·8 + 0,05·9 = 8,18, afgerond 8,2.

## 1. Helderheid van de uitleg (8,5)

*Goed*
- "Intuïtie": de vergelijking met het motief is uitgerekend (0,024% per dag tegen 1%
  ruis; 1% tegen 2%; factor 21, dus $21^2 \approx 440$ keer minder waarnemingen). De
  wortel die daar tegen de onderzoeker werkt, werkt hier voor hem.
- "Het kernresultaat": elke term van [](#eq-eventstudies-varcar) krijgt een naam in de
  formule zelf (fout in $\hat\alpha_i$, fout in $\hat\beta_{i,m}$) en een getal (8% bij
  $L_2 = 21$, 50% bij het jaarvenster).
- "Wat het voorspelt" en "Hoe het faalt": de krachtformule, de clusterfactor en de
  lange-horizonbias krijgen elk hun uitgerekende geval (61% en 25%; 1,86 en 29%; $0{,}17$
  en $2{,}7$).

*Aanmerkingen*
- "Opzet: eventtijd en het marktmodel": "Met {cite:t}`MacKinlay1997` gebruiken we netto
  rendementen $R_{i,\tau}$". In de notatietabel van de reeks is $R$ het bruto rendement
  en $r$ het netto; de lecture meldt de afwijking van de tijdsindex, maar niet deze.
- "Wat het voorspelt": "De toetsstatistiek (bij {cite:t}`MacKinlay1997` onder een andere
  naam)". Welke naam ($\theta_1$) staat er niet; wie het artikel erbij pakt, zoekt.
- "Opzet": "De residuele volatiliteit $\sigma_{\varepsilon_i}$ is voor grote Amerikaanse
  aandelen ongeveer 1,8% per dag." Het getal komt uit de eigen replicatiesteekproef
  (achteraf gekozen groeiaandelen, met TSLA en SMCI), niet uit een doorsnee van grote
  aandelen.
- "Wat het voorspelt", halfwaardetijd: de begrippen en drie bronnen staan er, maar geen
  getal dat de lezer zelf kan narekenen of dat later terugkomt.

*Beter uitleggen*
- De bron van 1,8%: één bijzin dat het de replicatiesteekproef is.

*Voor een 9*: meld in "Opzet" dat $R_{i,\tau}$ hier netto is (afwijking van de
notatietabel); noem $\theta_1$ bij MacKinlay; zeg bij 1,8% waar het getal vandaan komt.

## 2. Opbouw en rode draad (8)

*Goed*
- "Overzicht" stelt de vraag en geeft het antwoord; "Intuïtie" doet twee toetsbare
  voorspellingen (CAR-vorm rond de splitsing; 1% met enkele tientallen events bij een
  bekende dag), en de theorie en simulatie verwijzen er expliciet naar terug.
- Toy-getallen lopen door: de factor 4,9 tegen 3 keert terug in de simulatie ("63%"),
  de CAAR van 2% als effectgrootte ("99,2%"), en de toy-functies in oefening 1.
- Routekaart en "Samengevat" op hun plek, en de theorie eindigt met de twee
  faalwijzen die "Wat er brak" weer oppakt. 4.636 woorden.

*Aanmerkingen*
- "Simulatie" opent met geschiedenis en een vraag ("Brown en Warner ... maten hoe goed
  event-study-methoden werken ... De vraag over steekproeven: hoe vaak verwerpt $J_1$"),
  niet met haar conclusie. Zelfde punt als in 02_09.
- "Welke vraag staat open": "Hoe snel en hoe volledig verwerkt een prijs één publiek
  nieuwsfeit". De replicatie meet rond de ex-datum met dagdata en kan de snelheid niet
  meten ("Voor aankondigingsdatums is er geen gratis bron"). De halfwaardetijd-alinea
  in "Theorie" is daardoor een losse draad: geen getal, geen meting, niet in
  "Samengevat".
- "Hoe het faalt: de lange horizon" voorspelt een bias die groeit met $L_2$; de
  replicatie heeft een venster van 60 dagen erna maar koppelt de $-2{,}9\%$ alleen aan de
  standaardfout, niet aan $\sqrt{NL_2}\,\eta/\sigma_\varepsilon$.

*Beter uitleggen*
- Bij de $-2{,}9\%$: welke dagelijkse modelfout $\eta$ dat zou verklaren (ongeveer
  $-0{,}05\%$ per dag), zodat de lange-horizonformule een getal krijgt.

*Voor een 9*: laat "Simulatie" openen met haar uitkomst; laat de open vraag aansluiten
op wat de replicatie meet (of zeg in "Waar we zijn" dat snelheid hier alleen in
eventtijd op dagresolutie meetbaar is); koppel de $-2{,}9\%$ aan de
lange-horizonformule.

## 3. Taal (8,5)

*Goed*
- Korte zinnen (gemiddeld 15,0 woorden, geen boven 40); geen u/je; geen calques
  gemeten.
- Engelse citaten (Santa-Clara, FFJR) staan als blokcitaat na een Nederlandse
  parafrase.
- Termen krijgen ter plekke een Nederlandse omschrijving (*joint hypothesis*, *drift*,
  *bad model problem*).

*Aanmerkingen*
- "Replicatie": "Eerst de lijst met splitsingen; elke regel is
  `ticker:ex-datum:ratio`; de ex-datum is dag 0." Twee puntkomma's in één zin.
- Oefening 2, uitwerking: "een venster dat men tegenkomt"; "men" naast de "we" van de
  rest.
- "Overzicht": de zin "Voor de vraag die de reeks steeds stelt, theorie of feit,
  betekent dat: de event study is geen theorie die getoetst wordt, maar een
  meetinstrument dat feiten levert, en wat ze meet is altijd een afwijking van een
  model." stapelt drie gedachten.

*Voor een 9*: knip de puntkomma-zin en de theorie-of-feit-zin in het Overzicht; "men"
naar "we".

## 4. Toy-voorbeeld (8)

*Goed*
- Eén mechanisme (schattingsfout vergroot de variantie van een CAR), hoogstens één nog
  niet afgeleide formule (het recept, met de aankondiging dat de theorie het afleidt),
  tabel hand/code, en de zin "Wat de lezer nu weet".
- De getallen zijn zo gekozen dat alle regressies met de hand gaan ($\hat\mu_m = 0$,
  $S_{mm} = 10$, ronde bèta's).

*Aanmerkingen*
- "Stap 2": "Zo ook $\hat\alpha_B = 0$, $\hat\beta_{B,m} = 0{,}5$ ... en $\hat\alpha_C =
  0{,}2$, $\hat\beta_{C,m} = 1{,}5$". B en C krijgen alleen uitkomsten. Drie regressies
  met residuen plus het recept is ruim meer dan vijf minuten handwerk.

*Voor een 9*: laat twee aandelen (A en B) volstaan of geef voor B en C de sommen
$\sum R_m R_i$ en de residuen, zodat elke stap met de hand te volgen is.

## 5. Code en figuren (7)

*Goed*
- De toy-cel volgt de vijf stappen met commentaar per stap (`# step 1` tot `# step 5`).
- `fit_market_model` en `car_variance` lezen als de formules, met verwijzing naar
  [](#eq-eventstudies-varcar).
- Leeswijzers vóór beide figuren ("Let op hoe de lijnen naar rechts verschuiven"; "de
  helling vóór dag 0 en de helling erna") en figuurteksten die zeggen wat te zien is.

*Aanmerkingen*
- `# TODO: naar hap.stats` staat vier keer in lecturecode (`j1_test`,
  `fit_market_model`, `car_variance`, `split_tests`). Werknotities in de tekst voor de
  lezer.
- `simulate_events`: in stukjes (`chunk`) met arrays van vorm `(r, 1, T)`, een parameter
  `rho` die de lecture nergens gebruikt, en een drift `0.0003` die de tekst niet noemt.
- `split_tests`: de overlapmatrix
  `np.clip(np.minimum(b[:, None], b) - np.maximum(a[:, None], a) + 1, 0, None) / L2` en
  de gewogen $\hat{\bar\rho}$ in één regel zijn trucs; de zin vóór de cel legt het idee
  uit, niet de code.
- `cel-eventstudies-caar` (hide-input) rekent de standaardfoutband met
  `np.sum((g @ f["xtx_inv"]) * g, axis=1)`; rekenwerk in een verborgen figuurcel.
- Meerdere cellen geven `print`-uitvoer in plaats van een tabel.

*Voor een 9*: schrap de TODO-regels; haal `rho` en `chunk` uit `simulate_events` (of
gebruik `rho` in een oefening) en noem de drift; schrijf de overlap als lus of met een
zin die de broadcast uitlegt; reken de band in een zichtbare cel uit.

## 6. Replicatie en empirie (8)

*Goed*
- Het replicatieblok heeft alle vijf onderdelen, en de verwachte afwijking noemt een
  richting ("een selectie achteraf die de stijging vóór de splitsing opdrijft").
- Tabel origineel/verwachting/hier, oordeel "Geslaagd" dat de drie voorwaarden uit het
  blok één voor één afloopt.
- Drie kanttekeningen die precies de zwakke plekken benoemen (selectie, ex-datum in
  plaats van aankondiging, kleine $\hat{\bar\rho}$ met het effect op de $t$-waarde).

*Aanmerkingen*
- "De exacte waarden uit tabel 2 van FFJR konden we niet uit een toegankelijke bron
  verifiëren." De kolom "origineel" bevat daardoor alleen woorden ("stijgt gestaag",
  "vrijwel vlak"). Zelfde punt als in 02_09.
- De tabel "origineel ... of verwachting" mengt twee soorten vergelijking in één kolom.

*Voor een 9*: geef ten minste één getal uit FFJR (bijvoorbeeld hun cumulatieve residu
over de maanden vóór de splitsing, uit de figuur afgelezen en zo gemeld), of splits de
kolom in "FFJR" en "verwachting".

## 7. Oefeningen (9)

*Goed*
- Instap op het toy (eendaags venster, met de verklaring waarom $J_1$ stijgt terwijl de
  CAAR daalt), afleiding (constant-mean-model, werkelijk significantieniveau),
  uitbreiding van de replicatie (Brown en Warner op echte data).
- Elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Oefening 3: "De kracht ligt iets hoger dan de 63% van de simulatie" (69%); de
  uitwerking noemt twee tegengestelde krachten maar niet welke wint of waarom.

## Feitelijke fouten

Geen gevonden.

Nagerekend en correct: het hele toy (drie regressies, residuen, $\hat\sigma^2$ 0,3333 /
0,5 / 0,3333; AR's en CAR's 2,5 / 2,0 / 1,5; factor 4,9; $J_1 = 2{,}509$ en naïef
3,207; 28%); intuïtie (0,024%; factor 20,8; 440); $21/250 = 8\%$, 50%; kracht 61% en
25%; clusterfactor 1,86 en 29%; lange horizon 15%, 0,17 en 2,7; bewijzen van de twee
proposities; simulatie (62,9%; 99,2%; 0,4%; 3,5–6% met één uitschieter buiten
$\pm 1{,}4$ punt; 94,7% tegen 80,4%; 17,6% bij 21 dagen en $N = 100$); replicatie (102
splitsingen, 50 aandelen, 6183 dagen; 495 / 1,08 / 1,8%; 14,9% SE 3,7, $J_1$ 4,0, BMP 4,7;
$-0{,}08\%$, $J_1$ $-0{,}40$; $-2{,}9\%$ SE 1,6, $J_1$ $-1{,}84$, BMP $-1{,}18$; $\hat{\bar\rho} \le
0{,}0012$; KP 4,74 → 4,47); oefeningen (factor 1,3; $J_1 = 4{,}628$; 0,1 signaal op dag
$\pm1$; 9,2% / 7,1% / 6,0%; 4,3% en 69%). De percentages van Brown en Warner (80,4% en
13,2%), MacKinlays 0,965% en $J_1 = 9{,}28$ en Ball en Browns 85–90% zijn niet tegen de
bron gecontroleerd.

## De drie verbeteringen met het meeste effect

1. **Code opschonen** (simulatie, replicatie, CAAR-figuur): TODO-regels weg, `rho`,
   `chunk` en de drift uit `simulate_events` of uitgelegd, de overlapmatrix en de band
   zichtbaar en leesbaar, `print` naar tabellen. Code en figuren 7 → 8,5.
2. **Opbouw: simulatie opent met haar uitkomst, en de open vraag sluit aan op wat
   gemeten wordt** (halfwaardetijd-alinea een getal geven of inkorten; de $-2{,}9\%$ aan
   de lange-horizonformule koppelen). Opbouw 8 → 9.
3. **Replicatie en notatie precies maken**: één FFJR-getal of een aparte kolom
   "verwachting"; $R_{i,\tau}$ netto melden, $\theta_1$ noemen, de herkomst van 1,8%.
   Replicatie 8 → 9, helderheid 8,5 → 9.

## Navertelling in vijf zinnen

Een event study legt alle gebeurtenissen op dag nul, trekt van elk rendement af wat
het marktmodel voorspelt en middelt het restant, zodat het signaal blijft staan en de
ruis met $\sqrt N$ krimpt. De variantie van een CAR is ruis plus de schattingsfout in
alfa en bèta, en wie die fout vergeet, overschat zijn $t$-waarde. De toets vindt een
effect van 1% met enkele tientallen events als de dag bekend is, maar faalt als events
op dezelfde dag vallen of als het venster lang is, omdat een modelfout dan lineair
groeit. Op 102 recente splitsingen stijgt de koers in het jaar ervóór significant en
daarna niet meer, zoals bij FFJR. Een drift op lange horizon kan de event study niet
toewijzen aan risico of vergissing, omdat ze een model voor het normale rendement
nodig heeft. Dit komt overeen met het Overzicht; alleen de snelheid van de reactie,
die de open vraag noemt, wordt hier niet gemeten.

## Controle 1

Gecontroleerd op de versie na F5-1 (4.885 woorden, `--check` PASS). Alleen de eigen
punten. Nieuwe getallen nagerekend: $\eta = -2{,}9\%/61 = -0{,}048\%$ per dag, ongeveer
$-12\%$ per jaar ("ruim 10%"); CAAR op dag $-1$ 14,9% met SE 3,7 (gelijk aan de
toetstabel); toy-tabel $\sum R_m R_i$ = 10 / 5 / 15 en residuen van B en C; oefening 3
69% tegen 63%. Geen feitelijke fouten.

**1. Helderheid**
- $R_{i,\tau}$ netto als afwijking: **opgelost** ("Opzet").
- Naam bij MacKinlay: **opgelost** ($\theta_1$).
- Herkomst 1,8%: **opgelost** ("in de replicatiesteekproef hieronder (achteraf gekozen
  grote aandelen)").
- Halfwaardetijd zonder getal: **deels**. Er staat nu wat de eigen data kunnen zeggen
  ("binnen een dag"), ook in "Samengevat"; een gemeten getal is het niet, maar meer
  laten dagdata niet toe.

**2. Opbouw**
- Simulatie opent niet met haar conclusie: **opgelost** ("De uitkomst eerst: ... 63% ...
  vier van de vijf").
- Open vraag sluit niet aan op de replicatie: **opgelost** (vraag in "Waar we zijn" en
  Overzicht nu: zit nieuws al in de prijs, of loopt de prijs erachteraan; dat meet de
  replicatie vóór en na de ex-datum).
- $-2{,}9\%$ niet aan de lange-horizonformule gekoppeld: **opgelost**.

**3. Taal**
- Puntkomma-zin in "Replicatie": **opgelost**.
- "men": **opgelost**.
- Theorie-of-feit-zin in het Overzicht: **opgelost** (drie korte zinnen).
- Nieuw, verslechtering: "Overzicht", eerste zin: "Hoe meten we of een prijs nieuws
  verwerkt vóór of na het bekend wordt?" "Vóór het bekend wordt" is geen correcte
  constructie ("voordat het bekend wordt" of "vóór de publicatie").

**4. Toy**
- B en C alleen uitkomsten: **opgelost** (tabel met $\sum R_i$, $\sum R_m R_i$, residuen en
  $\hat\sigma^2$ voor alle drie).

**5. Code en figuren**
- TODO-regels: **opgelost**.
- `rho`, `chunk` en drift in `simulate_events`: **deels**. Alle drie staan nu uitgelegd
  (tekst, DGP-tabel, commentaar); `rho` en `chunk` blijven in de code, met een geldige
  reden (anders verschuift de toevalsgenerator en veranderen de gerapporteerde
  getallen).
- Overlap-broadcast: **opgelost** (zichtbare lus met benoemde tussenresultaten).
- Band in verborgen figuurcel: **opgelost** (zichtbare cel met `car_variance` en een
  controletabel; de figuurcel tekent alleen).
- `print`-uitvoer: **opgelost** (Series).

**6. Replicatie**
- Geen FFJR-getal: **niet** (bewust: niet geverifieerd, feitenregel). De rij voor de
  ex-datum zegt nu wel waarom FFJR daar niets hebben ("niet apart gemeten (maanddata)").
- Gemengde kolom origineel/verwachting: **opgelost** (drie kolommen).

**7. Oefeningen**
- Oefening 3, welke kracht wint: **opgelost** ("Per saldo wint de lagere gemiddelde
  volatiliteit").

**Nieuwe cijfers**

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 8,5 | 9 |
| 2 | Opbouw | 20% | 8 | 9 |
| 3 | Taal | 15% | 8,5 | 8,5 |
| 4 | Toy | 10% | 8 | 9 |
| 5 | Code en figuren | 10% | 7 | 8,5 |
| 6 | Replicatie | 10% | 8 | 8,5 |
| 7 | Oefeningen | 5% | 9 | 9 |

Eindcijfer: 0,3·9 + 0,2·9 + 0,15·8,5 + 0,1·9 + 0,1·8,5 + 0,1·8,5 + 0,05·9 = 8,83, afgerond
**8,8**. Laagste deelcijfer 8,5. Streefcijfer (≥ 8,5, niets onder 8) gehaald.

Wat nog ontbreekt voor een 9 op taal, code en replicatie: de openingszin van het
Overzicht herstellen; `simulate_events` zonder blokken (of `rho` in een oefening
gebruiken); één FFJR-getal zodra het geverifieerd is.
