STATUS 01_03_williams_ddm F6c words=5470 prose=PASS open=0 cijfer=8,7 min=8,5

# Eindbeoordeling (F6): Williams en het dividend discount model

## Eindcijfer: 8,3

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,60 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,33, dus 8,3.
Lengte: 5.446 woorden, net onder de 5.500.

## Feitelijke fouten

Nagerekend en in orde: het toy (24,00; 21,00; 87,5%), $\ln2/\ln1{,}10 = 7{,}3$ en
$\ln2/\ln1{,}05 = 14{,}2$, de Gordon-tabel (+25%, +26,2%, −16,7%) en het rooster
(20,80 tot 21,20; 14,86 tot 35,33), PVGO (40; 10; 27,27; −2,73), de kalibratie
(1,61%; 11,5%; 0,93; 6,82%; 1,42; 154), 19,5 en de rekenkundige correctie (2,3%;
8,4%; ongeveer 17), de simulatie (12,5 tot 40,8; factor 2,1; 36% en 109%; 14,1 tot
30,8), het panel (145; 1871–2015; 9,9 in 1917; 86,2 in 2025; 0,89), de regressies
($R^2$ 5% en 12%; CAPE 2,06 keer; 135 vanaf 1881), 0,375 + 0,15 = 0,53, de
oefeningen (17,33; 20,33; 85,2%; 15,3%; 17,5%; 25,6/28,6/37,0/74,1; jaar 30;
PVGO-tabel; $-0{,}063$, $t = -3{,}50$; 0,026, $t = 2{,}02$; 71 waarnemingen).

1. **Wat er brak, "Waar het breekt".** "Het enige symbool dat Williams als gegeven
   nam, verklaart het grootste deel van de beweging." Volgens de eigen
   decompositie in de replicatie verklaart het rendement 0,38 van één log-punt, de
   dividendgroei 0,15, en blijft 0,47 in de latere ratio. Op de tienjaarshorizon
   is dat het grootste verklaarde deel, niet het grootste deel.
2. **Theorie, "Opzet en aannames".** "De simulatie meet 6,8% als gemiddeld
   logrendement." De 6,82% komt uit Shillers data (de kalibratiecel), niet uit de
   simulatie; de simulatie neemt het getal als gegeven.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- "Van de definitie van rendement naar de contante waarde": het onderscheid
  identiteit/model is scherp en keert overal terug.
- "De gevoeligheid die alles bepaalt": de tabel met één procentpunt verschuiving
  maakt $1/(r-g)$ voelbaar.
- De rationele bel krijgt een verdubbelingstijd in jaren (7,3 tegen 14,2).

*Aanmerkingen*
- Replicatie: "Bij benadering is de log-ratio van vandaag de som van tien jaar
  log-dividendgroei, min de som van tien jaar log-rendementen, plus de log-ratio over
  tien jaar." De benadering (log-linearisering, discontering met $\rho$) wordt niet
  genoemd; de lezer kan de 0,47 niet controleren.
- Replicatie, warning: "Via die samenhang lekt de te lage persistentie in de
  helling". De Stambaugh-bias in vier zinnen, zonder getal voor de grootte.
- Opzet: "De simulatie meet 6,8%" (zie feitelijke fouten).
- Wat er brak: "verklaart het grootste deel van de beweging" (zie feitelijke fouten).

*Beter uitleggen*
- De log-identiteit: één regel met de benadering en haar orde van grootte, of de
  zin "ongeveer, want de latere ratio telt met een factor iets onder één".
- Stambaugh: één getal voor de verwachte bias bij 145 waarnemingen en
  autocorrelatie 0,89, of de zin dat de richting blijft.

### 2. Opbouw en rode draad (8)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord ("niet de verwachte dividenden
  maar de discontovoet beweegt").
- De voorspelling uit de intuïtie (hoge PD, snelle dividendgroei) is precies wat de
  replicatie toetst en verwerpt.
- $r - g = 5$ pp loopt van toy via Gordon-tabel naar de simulatie (5,2 pp).

*Aanmerkingen*
- Vier vooruitverwijzingen buiten "Wat er daarna kwam" (twee keer
  [](#05-33-fama-vs-shiller), twee keer [](#04-20-voorspelbaarheid)); STYLE §11.3
  staat er hoogstens twee toe.
- PVGO en de CAPE-regressie zijn zijpaden: de PVGO wordt in simulatie en replicatie
  niet meer gebruikt, en CAPE krijgt geen verwachte afwijking.

*Beter uitleggen*
- Eén zin bij de PVGO die zegt waarom ze in deze lecture staat (waar $g$ vandaan
  komt), of haar verplaatsen naar een oefening.

### 3. Taal (8,5)

*Goed*
- Het beeld van de boomgaard en "Een aandeel is een stuk papier" maken de
  intuïtie concreet in gewone taal.
- Eén naam per begrip: "discontovoet", "boekhoudkundige identiteit", "model van
  Williams".

*Aanmerkingen*
- Theorie: "Hoe hoger de dividenden, hoe hoger de prijs; hoe hoger het rendement
  waarmee ze verdisconteerd worden, hoe lager." Puntkomma-constructies (zeven in
  de lecture) en één zin boven 40 woorden.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Zes handstappen met ronde getallen (elke term exact één), tabel hand/code, en de
  les "een waardering is vooral een uitspraak over een verre toekomst".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- De toy-cel benoemt elk tussenresultaat (`terminal`, `terminal_pv`).
- Figuur met de hyperbool bij drie waarden van $r$ legt de scheefheid uit.

*Aanmerkingen*
- Replicatie: de regressietabel noemt de helling "de tweede parameter, na het
  intercept" en leest `fit.params.iloc[1]`; een benoemde parameter (`"log_pd"`)
  zou de code als de regressievergelijking laten lezen.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8,5)

*Goed*
- Blok volledig, met een expliciete voorwaarde die Williams zou steunen.
- Tabel Williams/verwacht/hier, oordeel "Geslaagd" met de drie verwachtingen.

*Aanmerkingen*
- De interpretatie van één log-punt (54 tegen 20; 0,38; 0,15; 0,47) staat in lopende
  tekst in plaats van in een tabel.
- De CAPE-regressie heeft geen verwachte afwijking.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy, de bel met een kantelpunt, PVGO met drie ROE's, de replicatie
  op een andere steekproef; elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De log-identiteit met de benadering noemen en "het grootste deel" corrigeren
   naar wat de getallen zeggen (helderheid 8 → 8,5).
2. Twee van de vier vooruitverwijzingen schrappen en PVGO of CAPE inkorten
   (opbouw 8 → 8,5).
3. De log-punt-interpretatie in een tabel zetten en CAPE een verwachting geven
   (replicatie 8,5 → 9).

## Navertelling in vijf zinnen

Williams stelde in 1938 dat een aandeel de contante waarde van zijn dividenden
waard is; dat volgt uit een boekhoudkundige identiteit plus de aanname van een
constante discontovoet en transversaliteit. Het Gordon-model maakt er
$d_1/(r-g)$ van, en omdat $r - g$ klein is, verandert één procentpunt de prijs
met een kwart. Groei voegt alleen waarde toe als het rendement op ingehouden winst
boven $r$ ligt. Zelfs met bekende $r$ geeft een uit data geschatte $g$ een
waardering die tot een factor twee naast kan zitten. Op Shillers data voorspelt
een hoge prijs-dividend-ratio lage rendementen en geen snelle dividendgroei, dus
$r$ is geen constante.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-01_03_williams_ddm.md` §F6-1 en de lecture.

| punt | status | vindplaats |
|---|---|---|
| Fout 1: "het grootste deel van de beweging" | opgelost | Wat er brak: "draagt ruim twee keer zoveel van de beweging als de dividendgroei" (0,38 tegen 0,15 is 2,5) |
| Fout 2: "De simulatie meet 6,8%" | opgelost | "Shillers data, waarop de simulatie kalibreert, geven 6,8%" |
| Verbetering 1: log-identiteit met benadering | opgelost | "de exacte log-vorm van Campbell en Shiller weegt latere jaren met een factor iets onder één ... De 0,47 is dus een orde van grootte." |
| Verbetering 2: vooruitverwijzingen, PVGO/CAPE | opgelost | nog twee buiten "Wat er daarna kwam" (04-20 bij Campbell-Shiller, 05-33 bij risico of vergissing); CAPE kreeg een verwachting en een oordeel |
| Verbetering 3: log-punt in een tabel | opgelost | tabel 0,15 / 0,38 / 0,47 / 1 (nagerekend) |
| Stambaugh-getal | niet | buiten de top drie; blijft een klein punt bij criterium 1 |
| Helling benoemd in de code | opgelost | `params["log_pd"]`, uitvoer gelijk |
| Naadpunt 2 ($p_t$, $d_t$) | opgelost | Opzet: "De notatie is die van [](#00-00-setup): $R = 1 + r$ is bruto, $r$ netto en simpel, en $p_t$ en $d_t$ zijn niveaus in euro" |
| Naadpunt 9 (eerste getoetste model) | opgelost | "Zo getoetst en verworpen werd het pas decennia later, na het CAPM" |
| Naadpunt 10 | opgelost | zie fout 1 |

Geen verslechteringen en geen nieuwe feitelijke fouten. De nieuwe bewering dat de
toetsen van constante $r$ na het CAPM kwamen, klopt (Campbell-Shiller en
Fama-French, 1988).

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 8,5 | 8,5 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 9 |
| 6 | Replicatie | 8,5 | 9 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,70 + 1,275 + 0,90 + 0,90 + 0,90 + 0,45 = 8,68. **Eindcijfer 8,7,
laagste deelcijfer 8,5.** Opbouw blijft 8,5, omdat de PVGO een zijpad blijft.
