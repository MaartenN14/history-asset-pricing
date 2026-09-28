STATUS 00_01_rendementen F6c words=5510 prose=PASS open=0 cijfer=9,3 min=8,5
Cijfer van record 9,3: F6c gaf 9,4, plafond is de F6-projectie bij volledige oplossing (§11.3).

# Ronde 9+

Vorige ronde: 8,7

Eindbeoordeling (F6) van `lectures/00_01_rendementen.md` na de taalredactie, met verse
ogen. `prose_stats --check`: PASS (5.448 woorden, zin gemiddeld 16,4, p90 26, één zin
boven 40, alinea 49, colon_mid 1,5, wie_open 3). `open` telt de feitelijke fouten; die
zijn er niet (zie onder). Het eindcijfer 8,9 haalt de 9,0 net niet. Taal en code/figuren
staan op 8,5 en trekken het omlaag.

## De drie verbeteringen met het meeste effect

1. **Taal: de zichtbare sjablonen weg** (taal 8,5 → 9,0). De taalredacteur heeft de
   dubbele punten vervangen door "namelijk" (r. 70, 131, 204, 661), en de inlossing van
   de intuïtie komt drie keer in dezelfde vorm ("De verwachting uit de intuïtie klopt
   dus", r. 319; "komt ook de derde verwachting uit de intuïtie uit", r. 446; "Ook de
   eerste verwachting uit de intuïtie komt dus uit", r. 514), terwijl STYLE §11.12
   hoogstens twee toestaat. De motiefnaam "de standaardfout van 2%" staat vijf keer in
   de lopende tekst (r. 45, 198, 396, 520, 901). Herschrijf de bestaande zinnen; er
   hoeft geen zin bij.
2. **Code en figuren: presentatielabels in het Nederlands** (8,5 → 9,0). De tabellen en
   de legenda noemen de reeksen "value-weighted markt" en "equal-weighted" (r. 785–786,
   833–834) en de kolom "SE van het gemiddelde" (r. 779), terwijl de tekst
   "waardegewogen" en "gelijkgewogen" zegt. Dat zijn twee namen voor hetzelfde begrip
   (H7), en figuren en tabellen horen Nederlands te zijn.
3. **Helderheid en replicatie: twee getallen die de lezer niet kan terugvinden** (helderheid
   9,0 → 9,5, replicatie 9,0 → 9,5). Op r. 391 staat "Stap 4 deelde door drie en kwam op
   18,7%", maar stap 4 (r. 161–165) geeft alleen $\hat\sigma^2 = 0{,}035$ en noemt geen
   18,7%. Op r. 794–795 "past" een gat van 2,2 procentpunt bij een halve variantie van
   2,6 zonder dat de tekst zegt waar het verschil van 0,4 vandaan komt. Zet 18,7% in stap 4
   (of als tabelregel in de toy-cel, [onderzoek B]) en zeg op r. 795 dat het recept een
   benadering is die bij maanden met een crash als 1929–1932 minder goed past.

Na punten 1 en 2 komt het eindcijfer op 9,1, en na alle drie op 9,3.

## Cijfers

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,5 |

Gewogen: 2,25 + 1,80 + 1,70 + 0,95 + 0,85 + 0,90 + 0,475 = 8,925, dus **8,9**.
Geen deelcijfer onder 8,5. Taal staat boven 8 en blokkeert dus niet. Lengte 5.448 woorden,
onder de 6.000.

## Per criterium

### 1. Helderheid van de uitleg (9,0)

*Goed.*
- Theorie, "Meetkundig, rekenkundig en de variance drag": de alinea na de stelling zegt
  uitdrukkelijk dat er vier symbolen voor twee grootheden zijn ($\nu$, $\mu_g$, $\mu_a$,
  $\mu$). Dat haalt de grootste bron van verwarring weg.
- "Annualisatie en de wortel-$t$-regel" en "Het kernresultaat": bij elke formule staat
  een uitgerekend getal (0,04 per dag, 0,65 per jaar, 2 procentpunt, 44 en 400 jaar).
- "Merton (1980)": $W_t$, drift en maximum-likelihoodschatter krijgen vóór de stelling
  een naam en een betekenis.

*Aanmerkingen.*
- Het kernresultaat, r. 390–391: "Stap 4 deelde door drie en kwam op 18,7%, maar daar
  ging het om de drie jaren zelf en hier om het proces waaruit ze komen." Stap 4 noemt
  18,7% niet, zodat de lezer terugbladert en het getal niet vindt.
- Het kernresultaat, r. 386–393: de alinea bevat $s^2$, $s$, de deler $T-1$, de 18,7%
  en de standaardfout van 13,2 procentpunt in vijf zinnen; ze is te dicht [onderzoek B].
- Opzet, r. 227–230: "Die van het simpele rendement ligt er dicht bij, met 18,34%
  tegen 18,32% per jaar voor de maandreeks over de hele eeuw (de dagtabel in de
  replicatie)." De tabel waar het getal staat, is de vergelijking van maand- en dagdata,
  niet een "dagtabel"; de verwijzing wijst naar een naam die in de replicatie niet
  voorkomt.

*Beter uitleggen.* Het verschil tussen $\hat\sigma$ met deler $T$ (stap 4) en $s$ met
deler $T-1$ (kernresultaat) verdient één regel in de toy-tabel, zodat beide getallen
naast elkaar staan. Bij de tabel met varianties (r. 544–548) mag de lezer horen dat de
andere maandautocorrelaties (−0,074 bij lag 3, 0,069 bij lag 5) elkaar grotendeels
opheffen, omdat de benadering alleen lag 1 neemt.

*Voor een 9.* Het cijfer is 9,0; voor een 9,5: 18,7% in stap 4 of de toy-tabel
(`00_01_rendementen.md:161–165`, `:390–391`) [onderzoek B], en "de dagtabel" vervangen
door de naam van de tabel die bedoeld is (`:229–230`).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- De intuïtie voorspelt drie dingen (r. 100–104) en de theorie lost ze elk op een
  vaste plek in (r. 319, 446, 514).
- De toy-getallen keren terug in de theorie (r. 318, r. 389) en de replicatie (22,9% op
  r. 792), en de simulatie gebruikt de 20% uit de intuïtie.
- "Wat er brak" verbindt de meetlat met het motief risico of vergissing via een
  concreet getal (vierhonderd jaar) en sluit af met de overgang naar Bachelier.

*Aanmerkingen.*
- Overzicht, r. 36: "Wat meten we als we een gemiddeld rendement uitrekenen, en hoe
  nauwkeurig?" De vraag staat zes regels eerder bijna woordelijk in "Welke vraag staat
  open" (r. 30–31) [onderzoek B].
- Overzicht, r. 62–65: "Door de hele reeks loopt de vraag theorie of feit, dus of een
  model een theorie is die getoetst wordt of een feit dat op een verklaring wacht." De
  motief-alinea volgt het sjabloon dat onderzoek B in vier colleges vond [onderzoek B],
  en staat los van de Fisher-Lorie-alinea ervoor.

*Beter uitleggen.* Het Overzicht kan direct met het antwoord beginnen; de vraag staat al
in de admonition erboven.

*Voor een 9.* Het cijfer is 9,0; voor een 9,5: laat het Overzicht met de bewering
beginnen (`00_01_rendementen.md:36`) [onderzoek B].

### 3. Taal (8,5)

*Goed.*
- Het ritme is sterk verbeterd: zinnen gemiddeld 16,4 woorden, de staccatoreeksen uit
  onderzoek B zijn weg (r. 150–153 en r. 811–817 lopen nu met voegwoorden).
- De "Wie …"-zinnen zijn teruggebracht tot drie, en de meeste waarom-alinea's openen
  niet meer met een handelende persoon als stoplap.
- "Waarom zou dit waar zijn?" staat nog maar twee keer buiten het kopje.

*Aanmerkingen.*
- Intuïtie, r. 69–71: "Ze kan twee vragen stellen, namelijk hoeveel lucht er in totaal
  is langsgekomen en hoe hard de wind schommelt." "Namelijk" vervangt hier, en op
  r. 131, r. 204 en r. 661, een dubbele punt; vier keer valt het op als reparatie.
- Toy-voorbeeld, r. 132–134: "**Het recept**, dat de theorie als eerste afleidt, zegt
  hoeveel, want het meetkundig gemiddelde is ongeveer het rekenkundig gemiddelde min een
  halve variantie." "Want" geeft hier geen reden maar de inhoud van het recept.
- Theorie, r. 319: "De verwachting uit de intuïtie klopt dus, want het gat groeit met de
  schommelingen"; r. 446: "Daarmee komt ook de derde verwachting uit de intuïtie uit";
  r. 514: "Ook de eerste verwachting uit de intuïtie komt dus uit". Drie keer dezelfde
  vaste wending, waar §11.12 er hoogstens twee toestaat.
- Motiefnaam, r. 396: "Dat getal is de standaardfout van 2% waar de hele reeks om
  draait"; daarnaast bij naam op r. 45, 198, 520 en 901. Vijf keer, waar §11.12 er twee
  toestaat (het kopje op r. 360 niet meegeteld).
- Replicatie, r. 816–817: "Maandelijks herbalanceren verkoopt na elke sprong omhoog en
  koopt na elke sprong omlaag, zodat het dat heen-en-weer als rendement boekt."
  Herbalanceren als handelend onderwerp, en "het dat" struikelt.
- Theorie, r. 303–304: "dat in de standaardfoutstelling kortweg $\mu$ heet". Een
  samenstelling die niemand zegt.

*Beter uitleggen.* Geen inhoudelijk punt; de taalpunten zijn herschrijvingen van
bestaande zinnen.

*Voor een 9.* Vervang de vier "namelijk"-constructies door een gewone bijzin of een
toegestane dubbele punt (`00_01_rendementen.md:70`, `:131`, `:204`, `:661`); geef de
drie inlossingen elk een eigen vorm en laat er één zonder verwijzing naar de intuïtie
(`:319`, `:446`, `:514`) [onderzoek D]; breng de motiefnaam terug naar twee keer, en
beschrijf elders wat hij betekent (`:396`, `:520`, `:901`); herschrijf `:132–134` en
`:816–817` (zie de hardop-toets).

### 4. Toy-voorbeeld (9,5)

*Goed.*
- Vier handstappen met alle tussenuitkomsten, in vijf minuten na te rekenen.
- Eén mechanisme en één nog niet afgeleide formule (het recept), vooraf aangekondigd.
- Tabel hand/code met een slotzin die het getal duidt (bijna twee procentpunt per jaar).

*Aanmerkingen.* Geen.

*Beter uitleggen.* De $\hat\sigma = 18{,}7\%$ uit stap 4 hoort als getal in de stap
zelf, omdat de theorie ernaar terugverwijst (zie criterium 1).

### 5. Code en figuren (8,5)

*Goed.*
- Elke cel heeft een zin ervoor en erna; de simulatielus laat het proces zien
  (`step`, `observed`, `returns_k`) met commentaar in de wiskundetaal.
- Vóór beide figuren staat waarop te letten (r. 664–666, 825–826), en de bijschriften
  zeggen wat te zien is.
- `annual_summary` wordt hergebruikt voor maand-, dag- en periodedata.

*Aanmerkingen.*
- Replicatie, r. 785–786: `"value-weighted markt": annual_summary(value_weighted),` en
  `"equal-weighted (10 size-decielen)": annual_summary(equal_weighted),` zijn
  rijlabels van een presentatietabel in het Engels, terwijl de tekst "waardegewogen" en
  "gelijkgewogen" zegt.
- Figuur, r. 833–834: `{"value-weighted": (1 + value_weighted).cumprod(),` en
  `"equal-weighted": (1 + equal_weighted).cumprod()}` worden de legenda van de figuur.
- Replicatie, r. 779: `"SE van het gemiddelde": sd_ann / np.sqrt(years),` is een Engelse
  afkorting als kolomkop.
- Simulatie, r. 627–629: de commentaren staan niet onder elkaar uitgelijnd; klein, maar
  zichtbaar in de enige cel die het proces laat zien.

*Beter uitleggen.* Geen.

*Voor een 9.* Nederlandse labels in de tabellen en de legenda: "waardegewogen markt",
"gelijkgewogen (10 grootte-decielen)", "standaardfout gemiddelde"
(`00_01_rendementen.md:779`, `:785–786`, `:833–834`).

### 6. Replicatie en empirie (9,0)

*Goed.*
- Admonition compleet en onder de 250 woorden, met een toetsbare verwachte afwijking
  (binnen één procentpunt, gelijkgewogen hoger).
- Oordeel begint met **Geslaagd** en verwijst naar die verwachting; de tabel zet
  origineel en hier naast elkaar met een 95%-interval.
- De twee illustraties op echte data (maand tegen dag, clustering) maken Merton
  empirisch zichtbaar.

*Aanmerkingen.*
- Replicatie, r. 793–795: "Het rekenkundig gemiddelde ligt ruim twee procentpunt boven
  het meetkundige, wat past bij een halve variantie van $0{,}229^2/2 \approx 2{,}6$
  procentpunt." Het gat is 2,2, het recept 2,6; "past bij" dekt 0,4 procentpunt zonder
  uitleg.
- "Dezelfde eeuw, maand- en dagdata", r. 898–902: "De dagreeks heeft 22 keer zoveel
  waarnemingen, maar de standaardfout van het gemiddelde daalt alleen van 1,83 naar 1,75
  procentpunt." De alinea draagt vijf getallen (22; 1,83; 1,75; 1,83; 20%), boven de
  drie per alinea.

*Beter uitleggen.* Bij het interval van 2% tot 17% (r. 822) mag één zin zeggen waarom
het interval van het rekenkundig gemiddelde ook voor het meetkundige geldt; nu staat er
"een vaste halve variantie lager", wat alleen klopt als de variantie bekend is.

*Voor een 9.* Het cijfer is 9,0; voor een 9,5: de 0,4 procentpunt verklaren of "past
bij" vervangen door "in de orde van" (`00_01_rendementen.md:793–795`), en in `:898–902`
één getalpaar laten staan.

### 7. Oefeningen (9,5)

*Goed.*
- Instap is een directe variatie op het toy (volgorde en een groter verlies), afleiding
  van Merton in discrete tijd, en uitbreiding van de replicatie naar drie perioden.
- Elke uitwerking eindigt met een les ("Een positief gemiddeld rendement zegt dus nog
  niets over het vermogen aan het eind"; een veranderd meetkundig gemiddelde is geen
  veranderd verwacht rendement).

*Aanmerkingen.*
- Uitwerking 2, r. 1138–1139: "Let wel dat het hier om het totaalrendement gaat en niet
  om de premie". "Let wel dat" is een stijve opening; het is een taalpunt, geen
  inhoudelijk.

*Beter uitleggen.* Geen.

## Feitelijke fouten

Nagerekend tegen de celuitvoer (`tools/nb_outputs.py` op het notebook, uitvoer in
`$TEMP/F6-00_01_rendementen-out.txt`) en met de hand: toy (5%; 3,2280%; 1,772 pp;
4,32 tegen 2,59; recept 0,0325), $s = 22{,}9\%$ en 13,2 pp (2,64 keer 5%),
$e^{0{,}0047 \cdot 1200} \approx 280$, $1{,}02^{100} = 7{,}24$, 0,04 per dag en
$0{,}04\sqrt{263} = 0{,}65$ (cel: 0,0399 en 0,6471; 26.296/100,08 = 263 dagen), de
tabel met benodigde jaren (44, 400, 1600, 400, 1600), de simulatie (1,99 pp; 14% naar
0,9%), $VR \approx 1{,}17$ en 2,0 naar 2,2 pp (maand-lag-1 0,085), excess kurtosis 17
(cel 16,99) en $\sqrt{19/2} \approx 3{,}1$, 18,34% tegen 18,32%, de replicatie (9,46%;
+0,46 pp; SE 3,9 pp; interval 1,8% tot 17,1%; volatiliteit 22,9%), 22 keer zoveel
waarnemingen (26.296/1.201) en 1,83 naar 1,75, de autocorrelaties (alle onder 0,09,
8 van 12 onder 0,03, absoluut 0,30 tot 0,33), 11,6% en 11,7% met 1,8 en 3,9 in "Wat er
brak", de oefeningen (1,77 naar 2,93 pp; 0,16% tegen 0,13%; 84%; binnen 0,24 pp; t =
0,01; 9,46% naar 10,92%; 764 jaar).

Geen onjuiste bewering. Twee onnauwkeurigheden, geen fouten:
- r. 545: "$N = 1200$ maanden"; de reeks heeft er 1.201. Zonder gevolg.
- r. 794–795: het gat van 2,2 pp "past bij" 2,6 pp; zie criterium 6.

## Navertelling in vijf zinnen

Een gemiddeld rendement meet het verwachte rendement, en omdat aandelen ongeveer 20%
per jaar schommelen, kent een eeuw data dat gemiddelde maar op twee procentpunt na. Het
meetkundig gemiddelde ligt een halve variantie onder het rekenkundige, zodat de
schommelingen ook de groei van een vermogen afremmen. Merton liet zien dat vaker meten
de schatting van de variantie scherper maakt maar die van het gemiddelde niet, omdat de
drift alleen uit het eerste en laatste punt van het pad volgt. De eerste meting van
Fisher en Lorie (9,0%) is met de data van Kenneth French na te rekenen, maar had een interval van
ongeveer 2% tot 17%. Daardoor valt uit rendementen wel af te lezen dát er een premie is,
maar niet hoe groot hij is of of hij risico of vergissing beloont.

Dat komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het formulierritme uit onderzoek B grotendeels weggehaald: de
etiketten "In woorden:" en "Wat dit leert:" zijn weg, de korte hoofdzinnen zijn met
voegwoorden verbonden, en de tekst leest nu overwegend als gesproken academisch
Nederlands. Wat overblijft, zijn sporen van de reparatie zelf: dubbele punten zijn
"namelijk" geworden, "want" wordt als bindmiddel gebruikt waar geen reden volgt, en
de inlossing van de intuïtie heeft één vaste vorm. Daarom een 8,5 en geen 9.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 131–134: "Achter het voorbeeld zit één ongelijkheid, namelijk dat het rekenkundig
   gemiddelde boven het meetkundige ligt. **Het recept**, dat de theorie als eerste
   afleidt, zegt hoeveel, want het meetkundig gemiddelde is ongeveer het rekenkundig
   gemiddelde min een halve variantie."
   → "Het voorbeeld draait om één ongelijkheid: het rekenkundig gemiddelde ligt boven het
   meetkundige. Hoeveel het scheelt, zegt **het recept** dat de theorie als eerste
   afleidt, want volgens dat recept is het meetkundig gemiddelde ongeveer het
   rekenkundige min een halve variantie."
2. r. 816–817: "Maandelijks herbalanceren verkoopt na elke sprong omhoog en koopt na elke
   sprong omlaag, zodat het dat heen-en-weer als rendement boekt."
   → "Een portefeuille die elke maand herbalanceert, verkoopt na elke sprong omhoog en
   koopt na elke sprong omlaag, en boekt het heen-en-weer zo als rendement."
3. r. 62–63: "Door de hele reeks loopt de vraag theorie of feit, dus of een model een
   theorie is die getoetst wordt of een feit dat op een verklaring wacht."
   → "Door de hele reeks loopt de vraag of we met een theorie te maken hebben die we
   kunnen toetsen, of met een feit dat nog op een verklaring wacht."

## Controle 1

Ronde 9+, F6c. Controle van `notes/rapport-00_01_rendementen.md` §R9-1 tegen de huidige
tekst van `lectures/00_01_rendementen.md` (5.510 woorden, `prose_stats --check` PASS,
sent_mean 16,6, p90 26, één zin boven 40 zoals al bij F6, colon_mid 2,0, wie_open 3,
semicol 3, stopw 0, calque 0).

**De drie verbeteringen met het meeste effect**
1. Taal, zichtbare sjablonen — opgelost. "Namelijk" komt nergens meer voor (r. 70, 131,
   204, 661 oud herschreven, twee met een dubbele punt vóór opsomming/verklaring); de
   drie inlossingen van de intuïtie (r. 319, 446, 514 oud) hebben elk een eigen vorm
   (variance drag zonder verwijzing naar de intuïtie, het kernresultaat via de ruis/
   signaal-verhouding, Merton via de meetpaal), geen ervan gebruikt nog de vaste wending;
   de motiefnaam "de standaardfout van 2%" staat nu twee keer bij naam in lopende tekst
   (r. 46, 544) plus het kopje (r. 375, telt niet mee), binnen de grens van STYLE §11.12.
2. Code en figuren, Nederlandse labels — opgelost. Tabel en legenda zeggen nu
   "waardegewogen markt", "gelijkgewogen (10 grootte-decielen)" en "standaardfout
   gemiddelde"; ook de figuurlegenda ("waardegewogen"/"gelijkgewogen") en de
   admonition zijn Nederlands. De commentaaruitlijning in de simulatiecel is
   gelijkgetrokken.
3. Helderheid/replicatie, twee ontraceerbare getallen — opgelost. $\hat\sigma = 18{,}7\%$
   staat nu in stap 4 zelf; het gat van 2,2 tegen 2,6 procentpunt heet "in de orde van"
   met de crash van 1929–1932 als reden voor het verschil.

**Voor een 9 / overige aanmerkingen uit F6**
- Helderheid, "de dagtabel" — opgelost: "de tabel met maand- en dagdata in de
  replicatie" (twee keer).
- Opbouw, Overzicht-vraag dubbel met "Welke vraag staat open" — opgelost: het Overzicht
  begint nu met de bewering in plaats van de vraag.
- Opbouw, motief-alinea "theorie of feit" los van Fisher-Lorie — opgelost: de alinea
  volgt nu op de Merton-zin en sluit af met een verwijzing terug naar de 9,0% van
  Fisher en Lorie.
- Taal, herbalanceren als handelend onderwerp en "standaardfoutstelling" — opgelost,
  beide herschreven zoals de hardop-toets voorstelde.
- Beter uitleggen, overige lags — opgelost in de bestaande zin ("de hogere lags heffen
  elkaar grotendeels op"); ook $N \approx 1200$ in plaats van $N = 1200$.
- Beter uitleggen, interval van het meetkundig gemiddelde — opgelost met een
  verwijzing naar de precisie van Mertons variantieschatter.
- Replicatie, vijf getallen in één alinea — opgelost: nog één getalpaar (1,83/1,75), de
  rest in woorden.
- Oefeningen, "Let wel dat" — opgelost: "overigens".

**Feitelijke fouten** — geen. De onnauwkeurigheid $N = 1200$ maanden (F6, criterium 6) is
verholpen tot $N \approx 1200$.

**Hardop-toets** — de drie geciteerde zinnen (toy-alinea met "namelijk"/"want", de
herbalanceer-zin, de motief-alinea "theorie of feit") zijn herschreven volgens het
voorstel in "Taal na de redactie"; bij het hardop lezen van Intuïtie, het kernresultaat
en de replicatie viel geen nieuwe zin op.

**Nieuwe punten** — geen (geen verslechtering, geen feitelijke fout gevonden).

### Cijfers (Controle 1)

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,5 |
| 2 | Opbouw en rode draad | 20% | 9,5 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,5 |
| 6 | Replicatie en empirie | 10% | 9,5 |
| 7 | Oefeningen | 5% | 9,5 |

Gewogen: 2,375 + 1,90 + 1,80 + 0,95 + 0,95 + 0,95 + 0,475 = 9,4. Geen deelcijfer onder
8,5; taal staat boven 8 en blokkeert dus niet. Eindcijfer **9,4**.
