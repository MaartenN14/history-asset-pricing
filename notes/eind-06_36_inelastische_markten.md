STATUS 06_36_inelastische_markten F6c words=5877 prose=PASS open=0 cijfer=9,1 min=9,0

**Eindcijfer van record: 9,1** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,9 -> F6c 9,1.

Eindbeoordeling F6 van `lectures/06_36_inelastische_markten.md`, gelezen na F1, F23 en F4T.
Getallen nagerekend tegen de celuitvoer (`$TEMP/F6-06_36_inelastische_markten-out.txt`) en met de hand.

## De drie verbeteringen met het meeste effect

1. **Het mechanisme achter de OLS-vertekening en de toy-slotzin kloppen maken** (helderheid 8,8 → 9,1).
   Regel 459-460 zegt dat bij gedeeld optimisme "alle sectoren samen" kopen terwijl de prijs stijgt; bij een vast aanbod ($\sum_i S_i f_{i,t} = 0$) koopt per saldo niemand, en de regressie ziet juist een prijsbeweging zonder bijbehorende flow ($f_{E,t} = u_{E,t} - u_{S,t} \approx 0$). Dat botst met regel 100-102 en 468. Regel 216-217 schrijft een multiplier van vijf toe aan mandaten, terwijl in geval 1 de actieve belegger geen mandaat heeft, maar even inelastisch is (zie Feitelijke fouten).
2. **Leeswijzers bij de figuren aanvullen** (code en figuren 8,8 → 9,2).
   Het rechterpaneel van de Financial Accounts-figuur (netto aankopen per sector in de tijd) wordt vóór noch na de figuur genoemd (r. 807-808, 837). Vóór de flow-simulatiefiguur staat alleen iets over het rechterpaneel (r. 554). De aanwijzing vóór de GIV-figuur (r. 685) leest als telegram.
3. **De laatste taalpunten oplossen door te herschrijven** (taal 8,8 → 9,1).
   "haar" voor een formule (r. 1042), drie hardop-zinnen (zie Taal na de redactie), "In de SDF-termen van" (r. 348), een spatie aan het begin van r. 853 en een dubbele spatie in r. 959.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,9

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,8 |
| 4 | Toy-voorbeeld | 10% | 9,2 |
| 5 | Code en figuren | 10% | 8,8 |
| 6 | Replicatie en empirie | 10% | 8,8 |
| 7 | Oefeningen | 5% | 9,2 |
| | **Gewogen eindcijfer** | | **8,9** (8,90) |

## 1. Helderheid van de uitleg: 8,8

*Goed*
- Opzet: elk symbool krijgt naam en orde van grootte ($\zeta$ met 0,2 uit het toy, $\Delta F$ met de 0,8 uit het toy, r. 246-250).
- Kernresultaat en CARA: het getal staat naast de formule (5% en 0,05% bij $\zeta = 0{,}2$ en 20, r. 302-303; $\zeta \approx 20$, honderd keer 0,2, r. 341-342), en de richting krijgt een economische reden (r. 342-346).
- GIV: de kansgrens wordt uitgerekend (0,013, schijnbare multiplier bijna 80, r. 462-466), zodat de omvang van de vertekening zichtbaar wordt.

*Aanmerkingen*
- Granular instrumental variables: "Als iedereen tegelijk optimistisch wordt, kopen alle sectoren samen terwijl de prijs stijgt, zodat een regressie vraag ziet die nauwelijks op de prijs reageert." Bij een vast aanbod kopen niet alle sectoren samen; de gemeten flow blijft rond nul terwijl de prijs beweegt.
- Toy-voorbeeld: "Een multiplier van vijf vraagt dus alleen dat bijna al het vermogen aan een mandaat vastzit." In geval 1 zit 60% bij een actieve belegger zonder mandaat; wat telt is dat iedereen elasticiteit 0,2 heeft.
- Opzet: "Omdat kleine letters hier logveranderingen zijn, schrijven we de prijs als $P_t$ en is $p = \Delta \log P$ de procentuele prijsverandering." Daarna zijn $c_t$ en $f_{i,t}$ klein zonder log te zijn; de afwijking van de setupnotatie wordt maar half aangekondigd.

*Beter uitleggen*
- Het verschil tussen "flow" als geldstroom (r. 41), als vraagverschuiving bij de oude prijs (r. 249) en als gemeten netto aankoop (replicatie) is de kern van het meetprobleem. Regel 308-310 zegt het, maar een lezer heeft er een getal uit het toy bij nodig (de 1 in het fonds, de 0,8 vraagverschuiving, de nul netto aankopen van de markt).
- GIV-bewijs, stap 2 tot 4 staan in één alinea; een lezer mist bij stap 4 waarom $\Cov(p, \eta + u_E)$ gelijk is aan $(\sigma_\eta^2 + \sigma_u^2/N)/\zeta$ (de $u_S$-$u_E$-covariantie uit stap 2).

*Voor een 9*
- lectures/06_36_inelastische_markten.md:459-461 herschrijven zodat de regressie een prijsbeweging zonder netto flow ziet.
- lectures/06_36_inelastische_markten.md:216-217 herschrijven naar "iedereen even inelastisch als het mandaatfonds".
- lectures/06_36_inelastische_markten.md:236 één bijzin dat $c_t$ en $f_{i,t}$ fracties zijn, geen logs.

## 2. Opbouw en rode draad: 9,0

*Goed*
- Overzicht stelt de vraag (één dollar, hoeveel marktwaarde) en geeft het antwoord met de onzekerheid (vijf, tussen twee en acht), r. 30-33.
- Intuïtie doet drie voorspellingen (mandaten, passief, OLS te inelastisch, r. 104-107) die in Theorie worden ingelost (r. 304-306, 595-597, 464-466).
- $\zeta = 0{,}2$ loopt van toy via lemma en stelling naar de GIV-simulatie (r. 246, 304, 634); 5.674 woorden.

*Aanmerkingen*
- Samengevat: "De simulatie laat zien hoe ver $\hat\zeta^{\mathrm{OLS}}$ en $\hat\zeta^{\mathrm{GIV}}$ in 104 kwartalen van de ware 0,2 af liggen." Dat is een vooruitblik, geen resultaat uit de theorie.
- Wat een lage elasticiteit verandert: de dropdown-simulatie van een eeuw kwartaaldata staat midden in Theorie, vóór Samengevat; dat is verdedigbaar, maar de sectie wordt daardoor de langste van het college.

*Beter uitleggen*
- De koppeling tussen de GIV-simulatie (2 tot 8) en het Overzicht ("alles tussen twee en acht") wordt pas in r. 721-725 gelegd; een halve zin in het Overzicht dat dit interval uit de simulatie komt, sluit de cirkel.

## 3. Taal: 8,8

*Goed*
- prose_stats PASS: zinnen gemiddeld 17,1 woorden, één zin boven 40, geen gedachtestreepjes, geen puntkomma's, geen "Wie"-openingen.
- De redactie heeft verwijswoorden en regeltaal opgeruimd (Theorie, kernresultaat: "Een instroom drijft de prijs dus op" in plaats van een formulezin).
- Motiefnamen: "de standaardfout van 2%" één keer, "risico of vergissing" één keer als kop.

*Aanmerkingen*
- Oefeningen, uitwerking 2: "De cel berekent de formule en zet haar naast de robuuste spreiding van de simulatie." "haar" voor een zaak (STYLE §11.12).
- Opzet (SDF-alinea): "In de SDF-termen van [](#05-33-fama-vs-shiller) is de vraagcurve volledig vlak." Vertaald aandoende constructie.
- Simulatie: "Links in de figuur telt de afstand tussen de twee histogrammen, rechts de verdeling van de multiplier, die smaller wordt naarmate $T$ groeit." Telegramachtig, "telt" zonder duidelijk onderwerp.
- Veertien S&P 500-toevoegingen: "De tabel zet latere gemiddelden op een rij, als geciteerde getallen met verschillende vensters." Stijve bijstelling; r. 853 begint bovendien met een spatie.
- Replicatie, oordeel: "Geslaagd, al gaat het oordeel over het teken en het ontbreken van een groot effect, niet over een multiplier." Regeltaal ("het oordeel gaat over").

*Beter uitleggen*
- Geen inhoudelijk punt; de taal staat de uitleg nergens in de weg.

*Voor een 9*
- lectures/06_36_inelastische_markten.md:1042, 348, 685-686, 852-854, 944 herschrijven (zie Taal na de redactie); spatie r. 853 en dubbele spatie r. 959 weg.

## 4. Toy-voorbeeld: 9,2

*Goed*
- Toy-voorbeeld, stap 1 tot 5: in vijf minuten met de hand na te rekenen (50,4; 40,32; 0,08; 20; 308; 164), één mechanisme.
- Tabel hand/code met exact evenwicht (cel 2: 4,00/0,2597/0,4878; exact 3,95/0,259/0,487).
- Stap 5 maakt de verschuiving naar passief zichtbaar en keert terug in Theorie (r. 597) en oefening 1.

*Aanmerkingen*
- Toy-voorbeeld, slot: "Een multiplier van vijf vraagt dus alleen dat bijna al het vermogen aan een mandaat vastzit." (zie helderheid).

*Beter uitleggen*
- Het toy gebruikt twee "instromen" (1 in het fonds, 0,8 naar aandelen); de multiplier is per dollar naar aandelen. Eén bijzin in stap 3 dat 5 de multiplier per dollar vraagverschuiving is, voorkomt dat de lezer 4/1 uitrekent.

## 5. Code en figuren: 8,8

*Goed*
- `toy_market` en `simulate_giv` lezen als de wiskunde (benoemde tussenresultaten `price`, `flows`, `flow_eq`, `giv`).
- De GIV-tabel zet de mediaan naast de kansgrens uit de formule, zodat code en stelling elkaar controleren.
- Elke rekencel heeft een zin ervoor en erna.

*Aanmerkingen*
- Netto aankopen en rendementen: "Links in de figuur staat de puntenwolk met de stippellijn van helling 5 ernaast." Het rechterpaneel (netto aankopen per sector, voortschrijdend) wordt nergens genoemd, ook niet na de figuur (r. 837).
- Wat een lage elasticiteit verandert: "In de figuur schuiven rechts de histogrammen naar links naarmate $\zeta$ daalt." Het linkerpaneel krijgt vooraf geen leeswijzer.
- `naive_researcher` berekent $R^2$ in één compacte uitdrukking (r. 538); een benoemd tussenresultaat leest beter.

*Voor een 9*
- lectures/06_36_inelastische_markten.md:807-808 en 837: zeg vooraf waarop te letten in het rechterpaneel en erna wat te zien is.
- lectures/06_36_inelastische_markten.md:554: leeswijzer voor het linkerpaneel.
- lectures/06_36_inelastische_markten.md:685: leeswijzer als volledige zin.

## 6. Replicatie en empirie: 8,8

*Goed*
- Admonition compleet in 216 woorden, met een verwachte afwijking die vooraf teken en grootte vastlegt.
- Twee tabellen origineel/hier (GK tegen OLS; Petajisto en Greenwood-Sammon tegen de veertien toevoegingen), met SE.
- Oordelen beginnen met "Gedeeltelijk geslaagd" en "Geslaagd" en verwijzen naar de verwachting (positief teken; dichter bij Greenwood en Sammon).

*Aanmerkingen*
- Admonition, verwachte afwijking: "Een negatief teken wijst op een fout in de datering." Onduidelijk bij welke meting (flowregressie of inclusies); datering hoort bij de inclusies.
- Netto aankopen: "De fondsaankopen hebben de duidelijkste positieve helling, 7,3 over de hele steekproef ($t = 2{,}8$), en ook de beleggingsfondsen afzonderlijk zijn significant." Getallen in lopende tekst die al in de tabel staan (ook r. 807, 933-934).

*Voor een 9*
- lectures/06_36_inelastische_markten.md:740 het teken aan de inclusies koppelen.
- lectures/06_36_inelastische_markten.md:803-807 en 933-934 getallen naar de tabellen verwijzen of beperken tot het ene getal waarop het oordeel rust.

## 7. Oefeningen: 9,2

*Goed*
- Instap (stap 5 met andere getallen, plus HHL en inkoop), afleiding (standaardfout van GIV), uitbreiding van de replicatie (lead-lag).
- Elke uitwerking eindigt met een les (strategische reactie dempt maar heft niet op; GIV leeft van idiosyncratische schokken; OLS scheidt prijsdruk en najagen niet).
- Uitkomsten kloppen met de cellen (1,43% en 0,43%; SE 0,074, 230 kwartalen; 14,0 en −10,5).

*Aanmerkingen*
- Oefening 2, uitwerking: "De cel berekent de formule en zet haar naast de robuuste spreiding van de simulatie." (taalpunt, zie boven).

## Feitelijke fouten

1. **r. 459-460 (onjuist mechanisme).** "kopen alle sectoren samen terwijl de prijs stijgt": in het model is $\sum_i S_i f_{i,t} = 0$, en uit stap 1 van het bewijs volgt $f_{E,t} = u_{E,t} - u_{S,t}$, dus de gemeenschappelijke schok verdwijnt uit de gemeten flow en zit alleen in de prijs. De regressie ziet een prijsbeweging zonder flow, niet een koopgolf. Tegenstrijdig met r. 100-102 en 468-470.
2. **r. 216-217 (onnauwkeurig).** De multiplier van vijf in geval 1 ontstaat doordat beide beleggers elasticiteit 0,2 hebben; de actieve belegger (60% van de markt) heeft geen mandaat. "alleen dat bijna al het vermogen aan een mandaat vastzit" is dus geen noodzakelijke en in het toy geen gebruikte voorwaarde.

Nagerekend en juist: toy (cel 2), $\zeta \approx 20$, kansgrens 0,013 en factor ruim vijftien ($77/5$), volatiliteit 7,0/13,4/bijna 24 en 1,9 keer (cel 3: 7,01; 13,43; 23,96; 1,92), 93% en 18% (0,926; 0,1805), OLS-medianen 0,013 en 0,0001, GIV 0,12-0,51 en 0,15-0,29, hoogstens een op de vijf (max 0,19), 298 kwartalen en ETF vanaf 1993, 7,3/2,8, 16,4/3,6, $R^2$ 3%, $t = 1{,}0$ voor alle sectoren, Tesla 51% over 23 dagen, 3,1% ($t = 1{,}8$), −4,0% ($t = -1{,}55$), 5,7/4,0 en 2,2/2,2, oefeningen (cel 13-15). Geen vakterm door de redactie van betekenis veranderd ("flow", "instroom", "marktelasticiteit", "multiplier" en "granular" houden hun betekenis).

## Navertelling in vijf zinnen

1. In de standaardtheorie is de vraagcurve voor aandelen vlak, zodat flows zonder nieuws de prijs niet bewegen, maar inclusies in de S&P 500 lieten sinds Shleifer zien dat ze dat wel doen.
2. Bij een vast aanbod beweegt de prijs met de flow als fractie van de marktwaarde gedeeld door de marktelasticiteit, dus $M = 1/\zeta$, en mandaatfondsen met elasticiteit $1-\theta$ maken $\zeta$ klein.
3. Een mean-variance-belegger heeft $\zeta \approx 20$, Koijen-Yogo en Gabaix-Koijen meten iets onder één en rond 0,2, wat een multiplier van ongeveer vijf geeft.
4. Een gewone regressie meet de elasticiteit niet, omdat gemeenschappelijke vraagschokken haar naar nul trekken, terwijl GIV met de eigen schokken van grote spelers wel werkt, maar in 104 kwartalen alleen tot een interval van 2 tot 8.
5. Op eigen data is het teken van de flow-rendementsrelatie positief maar niet causaal, en het inclusie-effect is recent bijna verdwenen, wat een puzzel blijft voor de hypothese; of de multiplier risico of vergissing meet, blijft open.

De navertelling wijkt niet af van het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijker gemaakt; de zinnen hebben verband, de regeltaal is grotendeels weg en de motiefnamen zijn beperkt. Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 685-686: "Links in de figuur telt de afstand tussen de twee histogrammen, rechts de verdeling van de multiplier, die smaller wordt naarmate $T$ groeit."
   Herschrijving: "Let links op de afstand tussen de twee histogrammen, en rechts op de verdeling van de multiplier, die smaller wordt naarmate $T$ groeit."
2. r. 852-854: "De gepubliceerde inclusie-effecten zijn in de loop van de tijd gekrompen. De tabel zet latere gemiddelden op een rij, als geciteerde getallen met verschillende vensters."
   Herschrijving: "De gepubliceerde inclusie-effecten zijn in de loop van de tijd gekrompen, zoals de gemiddelden in de tabel laten zien, al meet elke studie over een ander venster."
3. r. 944: "Geslaagd, al gaat het oordeel over het teken en het ontbreken van een groot effect, niet over een multiplier."
   Herschrijving: "Geslaagd wat het teken en het ontbreken van een groot effect betreft, maar een multiplier levert deze proef niet op."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Gecontroleerd op de stand na F6b (5.877 woorden, prose_stats PASS met één zin boven 40). Getallen tegen `$TEMP/F6c-06_36_inelastische_markten-out.txt`: kansgrens 0,013 (OLS-mediaan 0,0130 en formule 0,01305 bij $H - 1/N = 0{,}073$, twintig Zipf-sectoren), schijnbare multiplier bijna 80 (1/0,013 = 77), toy 4/0,8 = 5 en 20/100 = 0,2 zijn herleidbaar. Geschrapte getallen (7,3 met $t = 2{,}8$, $t = 1{,}8$, 4,0%, $t = -1{,}55$) staan nog in de tabellen. De nieuwe Financial Accounts-leeswijzer is kwalitatief zonder getal en kan niet tegen celuitvoer; ze is wel consistent met het figuurtype.

### Per punt

- Feitelijke fout 1 (OLS-mechanisme): opgelost; "prijs stijgt, per saldo koopt niemand extra", $f_{E,t} = u_{E,t} - u_{S,t}$, consistent met stap 1 en r. 100-102.
- Feitelijke fout 2 (toy-slot): opgelost; "hoeft niet iedereen aan een mandaat vast te zitten, als ook de actieve belegger even inelastisch is".
- Verbetering 1, 2 en 3: opgelost. Notatiebijzin ($f_{i,t}$, $c_t$ fracties), leeswijzers bij flowsim-, GIV- en Financial Accounts-figuur (beide panelen), "haar" vervangen, SDF-zin, drie hardop-zinnen, spaties.
- Aanmerkingen: flow-betekenissen met toy-getallen en GIV-stappen 2 tot 4 als aparte alinea's: opgelost; vooruitblik in Samengevat vervangen door de kansgrens: opgelost; Overzicht koppelt twee tot acht aan de simulatie: opgelost; `r2_news`: opgelost; admonition koppelt het negatieve teken aan het aankondigingsrendement: opgelost; getallen uit lopende tekst: grotendeels opgelost (3,1% blijft als steun voor het oordeel).
- Dropdown-simulatie midden in Theorie: niet verplaatst, verdedigbaar; geen aftrek.
- Verslechtering of nieuwe feitelijke fout: geen. Kleine rest: de notatiebijzin in Opzet is een lange zin en de afbreking van de regel ("de / procentuele") is cosmetisch.

## Eindcijfer van record (F6c): 9,1

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 | 9,1 |
| 2 | Opbouw en rode draad | 20% | 9,0 | 9,1 |
| 3 | Taal | 20% | 8,8 | 9,1 |
| 4 | Toy-voorbeeld | 10% | 9,2 | 9,2 |
| 5 | Code en figuren | 10% | 8,8 | 9,2 |
| 6 | Replicatie en empirie | 10% | 8,8 | 9,0 |
| 7 | Oefeningen | 5% | 9,2 | 9,2 |
| | **Gewogen eindcijfer** | | 8,9 | **9,1** (9,115) |

Plafond: eindcijfer niet boven 9,1 ("bij volledige oplossing"); geen deelcijfer onder 9,0, taal 9,1.
