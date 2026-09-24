STATUS 01_03_williams_ddm F5c words=5446 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling: 01_03_williams_ddm (F5a)

Gelezen als eerstejaars PhD-student die L1 en L2 heeft gelezen. Ter controle van de
aansluiting: "Waar we zijn" en "Wat er brak" van 01_02_bachelier en 01_04_markowitz.
De aansluiting klopt aan beide kanten: Bachelier sluit af met "een theorie van wat een
prijs *hoort* te zijn", Markowitz opent met "Williams had geen theorie van $r$, en hij
bekeek elk aandeel apart". Beide staan zo in deze lecture.

`prose_stats`: 5.365 woorden (onder 5.500), gemiddelde zinslengte 14,8, één zin boven 40
woorden, 7 puntkomma's, PASS.

## Eindcijfer: 8,2

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,15, afgerond 8,2.

## 1. Helderheid van de uitleg: 8

*Goed*
- **Opzet en aannames / Van de definitie van rendement naar de contante waarde**: het
  onderscheid tussen identiteit (neemt niets aan) en model (constante $r$) wordt
  expliciet gemaakt en draagt de hele lecture. De wet van iteratieve verwachtingen krijgt
  een regel uitleg ("wat we vandaag verwachten dat we morgen zullen verwachten").
- **Het kernresultaat**: de rationele bel krijgt naam, definitie en twee uitgerekende
  getallen (verdubbeling in 7,3 tegen 14,2 jaar). De notatiewissel ten opzichte van L2
  (kleine letters zijn hier bedragen, geen logs) wordt benoemd.
- **Replicatie**: "Wat betekent één log-punt? Een prijs-dividend-ratio van 54 in plaats
  van 20" maakt een abstracte coëfficiënt concreet.

*Aanmerkingen*
- **Opzet en aannames**: "Voor Amerikaanse aandelen is hij reëel 7 tot 8% per jaar: de
  simulatie meet 6,8% als gemiddeld logrendement, en dat is als gewoon gemiddelde
  ongeveer 8,4%." Beide gemeten getallen vallen buiten het genoemde bereik (zie
  Feitelijke fouten).
- **Replicatie, warning**: "Een onverwachte koersstijging verhoogt namelijk tegelijk de
  ratio en het rendement van dat jaar, zodat de fouten in regressor en rendement samen
  bewegen." Samen bewegende fouten alleen geven geen bias; de tweede schakel (de
  persistentie 0,89 wordt in een kleine steekproef te laag geschat, en die fout lekt via
  de correlatie in de helling) ontbreekt. De lezer weet daarna niet waarom de helling
  juist *te groot* is.
- **Replicatie, na het oordeel**: "De rest, ongeveer $1 - 0{,}15 - 0{,}38 = 0{,}47$
  log-punt, zit volgens de identiteit vooral in de prijs-dividend-ratio aan het eind van
  de tien jaar ... In logs geldt die optelling bij benadering." De getoonde identiteit is
  een som van breuken in niveaus; waarom de drie hellingen samen 1 moeten zijn, wordt
  nergens gezegd.
- **PVGO**: "Deze $b$ is een andere dan de bel $b_t$ hierboven, maar we volgen de gangbare
  notatie." Het wordt gemeld, maar de lezer moet in dezelfde lecture twee betekenissen
  van $b$ vasthouden.

*Beter uitleggen*
- Waarom de hellingen optellen tot één: één zin dat de log-versie van de identiteit
  zegt "log PD vandaag ≈ som dividendgroei − som rendementen + log PD over tien jaar",
  en dat regressie van elk van die termen op log PD dus hellingen geeft die samen 1 zijn.
- Stambaugh-bias: de ontbrekende schakel in één zin, met richting: $\hat\rho$ is naar
  beneden vertekend, de fouten correleren positief, dus de rendementshelling wordt
  negatiever.

*Voor een 9*
- Opzet en aannames: het bereik "7 tot 8%" gelijktrekken met de gemeten 6,8% (log) en
  8,4% (gewoon gemiddelde), of één van beide als het bedoelde getal noemen.
- Replicatie, warning: de schakel "te lage geschatte persistentie → vertekende helling"
  toevoegen.
- Replicatie, alinea "Wat betekent één log-punt?": één zin die zegt waarom 0,15 + 0,38 +
  rest = 1.

## 2. Opbouw en rode draad: 8

*Goed*
- **Overzicht**: vraag ("Wat is een aandeel waard?") en antwoord ("niet de verwachte
  dividenden maar de discontovoet beweegt") staan in de eerste vier zinnen.
- **Intuïtie → Theorie → Replicatie**: de intuïtie doet een voorspelling (hoge ratio →
  snelle dividendgroei), de theorie leidt haar af in "Hoe het getoetst wordt", de
  replicatie toetst en verwerpt haar. De rode draad is volledig gesloten.
- **Dezelfde getallen**: toy ($r = 10\%$, $g = 5\%$), gevoeligheidstabel (de eindwaarde van
  het toy als zelfstandig aandeel, 21,00), PVGO ($r = 10\%$, $g = 5\%$) en simulatie
  ($r - g = 5{,}2$, "bijna de 5 procentpunt van het toy-voorbeeld").

*Aanmerkingen*
- **Simulatie**: de conclusie (een waardering uit geschatte $g$ zit tot een factor twee
  naast) wordt nergens meer gebruikt. "Wie vindt dat de prijs-dividend-ratio niet bij de
  dividenden past, moet eerst weten hoeveel ruis er al zit" belooft een koppeling met de
  replicatie, maar Replicatie en "Wat er brak" komen er niet op terug.
- **Hoe het getoetst wordt**: begint met een vraag, "Waar in het model zit iets wat de data
  kunnen tegenspreken?", niet met de conclusie van de subsectie.
- **Replicatie, slot**: na figuur en oordeel volgt nog een CAPE-regressie met eigen
  getallen. Het slot van de replicatie is daardoor een uitbreiding, niet het oordeel.
- Lengte 5.365 woorden: onder de grens, maar er is weinig ruimte.

*Beter uitleggen*
- De lezer krijgt niet mee waarom de simulatie in deze lecture staat en niet in een
  lecture over schatten; één zin in de replicatie of in "Wat er brak" die de breedte van
  12,5–40,8 terugkoppelt aan het lezen van de prijs-dividend-ratio volstaat.

*Voor een 9*
- Simulatie → Replicatie/Wat er brak: de simulatieconclusie één keer terug laten komen,
  of de brugzin "Voor het hoofdargument doet dat ertoe" waarmaken.
- Hoe het getoetst wordt: de subsectie openen met haar conclusie (bij constante $r$ moet
  een hoge ratio door snelle dividendgroei gevolgd worden).
- Replicatie: de CAPE-uitbreiding korter of vóór het oordeel, zodat de sectie op het
  oordeel eindigt.

## 3. Taal: 8

*Goed*
- Korte zinnen (gemiddeld 14,8 woorden), geen u/je, geen calques gevonden door de tool.
- **Intuïtie**: "Een aandeel is een stuk papier. Het geeft geen nut, het gaat niet stuk,
  en niemand kan erin wonen." Natuurlijk, beeldend Nederlands.
- "discontovoet" wordt consequent gebruikt; de gelijkstelling met verwacht rendement wordt
  eenmaal gemaakt en daarna niet meer gewisseld ("We noemen hem verder alleen de
  discontovoet").

*Aanmerkingen*
- **Simulatie**: "Die rij kiest $r$." Te gecomprimeerd; "die rij" verwijst naar een
  tabelrij twee zinnen terug.
- **Overzicht**: "Het werk definieert het tijdvak omdat een prijs voor het eerst uit een
  model volgt en niet uit een gewoonte." Projecttaal ("definieert het tijdvak").
- **Hoe het getoetst wordt**: "In woorden: een hoge prijs-dividend-ratio vandaag wordt,
  langs het pad dat werkelijk komt, gevolgd door snelle dividendgroei (in de tellers),
  door lage rendementen (in de noemers), of door een ratio die over $K$ jaar nog steeds
  hoog is." Stapelzin met twee tussenvoegingen, de langste van de lecture.
- **PVGO**: $b$ voor twee begrippen (zie criterium 1).

*Beter uitleggen*
- Geen inhoudelijk gat; het gaat om drie zinnen die de lezer twee keer moet lezen.

*Voor een 9*
- Simulatie: "Die rij kiest $r$" uitschrijven (welk getal, waarvoor).
- Overzicht: "definieert het tijdvak" vervangen door wat er gebeurt.
- Hoe het getoetst wordt: de stapelzin in twee of drie zinnen splitsen.

## 4. Toy-voorbeeld: 9

*Goed*
- In vijf minuten na te rekenen: de keuze groei = discontovoet in de eerste fase maakt elke
  term 1,00, en $1{,}331 \times 21 = 27{,}951$ is exact.
- Precies één nog niet afgeleide formule, $d/(r-g)$, en die wordt als zodanig aangekondigd.
- Tabel hand/code en een zin wat de lezer nu weet (87,5% van de prijs komt uit de
  eindwaarde; delen door een klein getal).

*Aanmerkingen*
- Geen die het cijfer drukken. De PD van 24 uit Stap 6 wordt later niet meer gebruikt.

*Beter uitleggen*
- Niets nodig.

## 5. Code en figuren: 8

*Goed*
- Elke cel heeft een zin ervoor en erna; de hoofdtekstcellen lezen als de wiskunde
  (`dividends`, `discounted`, `terminal`, `terminal_pv`).
- **Simulatie**: vóór de figuur staat waarop te letten ("links op de lange staart naar
  rechts, en rechts op hoe steil de hyperbool wordt"), de figuur hergebruikt dezelfde
  20 000 steekproeven als de tabel.
- **Replicatie**: de cel met de drie kolommen "Williams / verwacht / hier" maakt het
  oordeel controleerbaar.

*Aanmerkingen*
- **Replicatie, vergelijkingscel**: `"rond 0.10"` in een Nederlandse presentatietabel met
  decimale punt, terwijl de tekst "rond tien procent" en elders komma's gebruikt.
- **Simulatie, tabellen**: kolomnamen `"SE van g-dak"`, `"PD 5e pct"`, `"std.dev."`,
  `"aandeel g-dak > r"` zijn afkortingen die de lezer moet ontcijferen.
- **Simulatie, figuur rechts**: drie hyperbolen voor $r$ = 6%, 6,82% en 8%, maar de tekst
  vóór de figuur zegt niet waarom drie waarden van $r$ en wat hun verschil laat zien.

*Beter uitleggen*
- Bij de rechterfiguur: één zin dat de extra krommen tonen hoe de asymptoot meeschuift
  met $r$ (en dus dat een onzekere $r$ hetzelfde doet als een onzekere $g$).

*Voor een 9*
- Replicatie, vergelijkingscel: "rond 0,10" of "rond 10%".
- Simulatie: kolomnamen voluit ("standaardfout van $\hat g$", "5e percentiel", ...).
- Simulatie, zin vóór de figuur: zeggen waarom drie waarden van $r$.

## 6. Replicatie en empirie: 8

*Goed*
- Admonition compleet (bron, wat, data, verschil, verwachte afwijking) en ruim onder 250
  woorden; eerlijk dat het boek geen tijdreekstoets bevat.
- Oordeel begint met "**Geslaagd.**" en koppelt elk getal aan de verwachting.
- De warning over overlap (≈14 onafhankelijke perioden) en persistentie is terecht en
  concreet.

*Aanmerkingen*
- **Oordeel**: "de dividendcoëfficiënt (0,015, $t = 1{,}63$, $R^2$ 0,05) is niet
  significant, de rendementscoëfficiënt ($-0{,}038$, $t = -2{,}21$) is negatief en
  significant, en de $R^2$ van 0,12 ligt rond tien procent." Zes getallen in lopende tekst
  die al in de tabel erboven staan.
- **CAPE-alinea**: "de helling is $-0{,}059$ met $t = -4{,}52$, en de $R^2$ van 0,24" herhaalt
  de tabel in proza.
- **Wat er brak**: dezelfde getallen een derde keer ("$R^2 \approx 5\%$, $t = 1{,}63$ ...
  $R^2 \approx 12\%$ ... $t = -2{,}21$").

*Beter uitleggen*
- Niets inhoudelijks; het gaat om waar de getallen staan.

*Voor een 9*
- Oordeel en CAPE-alinea: naar de tabel verwijzen in plaats van de getallen te herhalen;
  in "Wat er brak" hoogstens één getal per kanaal.

## 7. Oefeningen: 9

*Goed*
- Instap is een variatie op het toy (4% in plaats van 5%), met hand- en codecontrole.
- Oefening 1 bevat een afleiding (de bel lost dezelfde vergelijking op), oefening 3 is een
  uitbreiding van de replicatie (naoorlogs, vijf jaar).
- Elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- **Instap, uitwerking (2)**: "de eindwaarde is omgekeerd evenredig met dat verschil" klopt
  niet helemaal, want ook $d_4$ daalt (1,04 in plaats van 1,05); de eindwaarde daalt 17,5%,
  niet de 16,7% die omgekeerde evenredigheid geeft. Klein.

## De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9)**: het bereik "7 tot 8%" in Opzet en aannames rechtzetten, de
   Stambaugh-schakel (te laag geschatte persistentie) in de warning toevoegen, en in één
   zin uitleggen waarom 0,15 + 0,38 + 0,47 = 1. Eindcijfer +0,3.
2. **Opbouw (8 → 9)**: de simulatieconclusie terug laten komen in replicatie of "Wat er
   brak", "Hoe het getoetst wordt" met de conclusie openen, en de replicatie op het oordeel
   laten eindigen (CAPE korter of eerder). Eindcijfer +0,2.
3. **Taal (8 → 9)**: "Die rij kiest $r$", "definieert het tijdvak" en de stapelzin in "Hoe het
   getoetst wordt" herschrijven. Eindcijfer +0,15.

## Navertelling in vijf zinnen

Uit de definitie van rendement volgt een identiteit: de prijs is de verdisconteerde som van
dividenden plus een eindwaarde, en die kan niet fout zijn. Williams voegde een constante
discontovoet toe; met de transversaliteitsvoorwaarde (geen bel) is de prijs dan de contante
waarde van alle verwachte dividenden, en bij constante groei het Gordon-model
$\E_t[d_{t+1}]/(r-g)$. Omdat $r - g$ klein is, is elke waardering zeer gevoelig voor $g$ en
$r$, en groei voegt alleen waarde toe als het rendement op investeringen boven $r$ ligt. Bij
constante $r$ moet een hoge prijs-dividend-ratio door snelle dividendgroei gevolgd worden,
maar op Shillers data voorspelt de ratio vooral lage rendementen. Dus is $r$ geen constante
maar een tijdreeks, en of dat risico of vergissing is, laten de data open.

Dit komt overeen met het Overzicht.

## Feitelijke fouten

Nagerekend met `uv run python` op `hap.data.shiller()` en de formules uit de tekst.
Kloppen: toy (24,00; 21,00; 87,5%), gevoeligheidstabel en rooster (26,25; 26,50; 17,50;
20,80–21,20; 14,86–35,33), bel-verdubbeling (7,3 en 14,2 jaar), PVGO-voorbeeld (40; 27,27;
−2,73) en PVGO-formule, kalibratie (n = 154; 1,61%, 11,5%, SE 0,93; 6,82%, SE 1,42; std
17,6%), halve-variantiecorrectie (2,3%; 8,4%; ratio ≈ 17), ware ratio 19,5, simulatie-
percentielen (T = 50: 12,5 / 19,5 / 40,8; T = 100: 14,1 / 30,8) en afgeleide verhoudingen
(2,1; −36%; +109%), PD-uitersten (9,9 in 1917; 86,2 in 2025), panel (145 waarnemingen,
1871–2015, autocorrelatie 0,89), regressies (0,015, t 1,63, R² 0,05; −0,0375, t −2,21,
R² 0,12), CAPE (−0,059, t −4,52, R² 0,24, start 1881), oefening 1 (41,20; PD 25,6 / 28,6 /
37,0 / 74,1; jaar 30), oefening 2 (55,56; 41,67; −13,89; 83,33; 27,78; 111,11; 37,04),
oefening 3 (−0,063, t −3,50; 0,026, t 2,02; −0,045; n = 71).

1. **Opzet en aannames**: "Voor Amerikaanse aandelen is hij reëel 7 tot 8% per jaar: de
   simulatie meet 6,8% als gemiddeld logrendement, en dat is als gewoon gemiddelde
   ongeveer 8,4%." Het genoemde bereik bevat geen van beide gemeten getallen (6,82% en
   6,82 + 17,6²/200 = 8,37%). Het bereik moet ruwweg 7 tot 8,5% zijn, of de zin moet één
   van beide maatstaven kiezen.

Geen fout maar het noemen waard: in de Intuïtie is "ongeacht wat de buurman voor de
zijne betaalde" als uitleg van Williams' boomgaardbeeld een toevoeging van de lecture; het
vers dat Williams aanhaalde ("An orchard for fruit ...") noemt geen buurman. De zin leest
alsof het Williams' eigen beeld is.

## Controle 1

Alleen de eigen punten nagekeken, op de huidige `lectures/01_03_williams_ddm.md`.
`prose_stats`: 5.446 woorden, PASS.

| crit. | punt | status | vindplaats nu |
|---|---|---|---|
| 1 | "7 tot 8%" tegen 6,8% en 8,4% (feitelijke fout 1) | opgelost | Opzet en aannames: "reëel ongeveer 8,4% per jaar als gewoon gemiddelde. De simulatie meet 6,8% als gemiddeld logrendement." |
| 1 | Stambaugh: ontbrekende schakel persistentie → helling | opgelost | Warning: "In een korte steekproef wordt die persistentie te laag geschat ... lekt de te lage persistentie in de helling: de rendementshelling valt negatiever uit" |
| 1 | waarom 0,15 + 0,38 + 0,47 = 1 | opgelost | Replicatie, alinea na "Wat betekent één log-punt?": identiteit in logs, drie hellingen tellen op tot ongeveer één |
| 1/3 | $b$ voor bel en inhoudingspercentage | opgelost | bel heet nu $B_t$, ook in oefening 1 (de Engelse variabelenaam `b_t` in de code telt niet mee) |
| 2 | simulatieconclusie niet hergebruikt | opgelost | Wat er brak: "Ruis in de schatting van $g$ verklaart dat niet: ... tot een factor twee naast ... de ratio liep van 10 tot 86" |
| 2 | "Hoe het getoetst wordt" opent met vraag | opgelost | opent nu met "Het model wordt toetsbaar in de prijs-dividend-ratio: ..." |
| 2 | replicatie eindigt op CAPE, niet op oordeel | opgelost | volgorde nu: regressies, figuur, CAPE, log-punt, warning, vergelijkingstabel, **Geslaagd.** |
| 3 | "Die rij kiest $r$" | opgelost | "Dat getal nemen we als $r$." |
| 3 | "definieert het tijdvak" | opgelost | "Daarom begint het tijdvak hier." |
| 3 | stapelzin "langs het pad dat werkelijk komt" | opgelost | in vier zinnen gesplitst |
| 5 | "rond 0.10" | opgelost | "rond 10%" |
| 5 | afgekorte kolomnamen simulatie en kalibratie | opgelost | "standaardfout geschatte g", "PD 5e percentiel", "standaarddeviatie", "standaardfout gemiddelde" |
| 5 | waarom drie waarden van $r$ in de figuur | opgelost | zin vóór de figuur: "de asymptoot schuift mee met $r$, dus een onzekere $r$ doet hetzelfde als een onzekere $g$" |
| 6 | getallen in oordeel, CAPE-alinea en Wat er brak | opgelost | oordeel verwijst naar de tabel; CAPE-alinea zonder getallen; Wat er brak alleen $R^2$ |
| 7 | instap (2): "omgekeerd evenredig" negeert lagere $d_4$ | opgelost | "De eindwaarde daalt 17,5% ... en $d_4$ wordt iets kleiner" (nagerekend: 17,33/21,00 = 0,825) |

Geen verslechteringen en geen nieuwe feitelijke fouten. Klein restpunt, zonder aftrek: in
Opzet en aannames staan 8,4% en 6,8% nu naast elkaar zonder de zin die zegt dat het
verschil de halve variantie is; die staat pas in de simulatie.

### Deelcijfers na controle 1

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |

**Eindcijfer: 9,0** (was 8,2). Laagste deelcijfer 9. Open feitelijke fouten: 0.
