STATUS 02_06_efficiente_markten F6c words=5812 prose=PASS open=0 cijfer=9,0 min=8,7
Open punt (SPY-cel zonder reden voor vijf tickers) door de orchestrator opgelost met één bijzin over de offline cache, 2026-09-28.

# Ronde 9+

Vorige ronde: 8,8

Eindbeoordeling (F6) van `lectures/02_06_efficiente_markten.md` na de taalredactie.
`prose_stats --check`: PASS (5.709 woorden, zinnen gemiddeld 16,7, p90 27, geen zin
boven 40, alinea gemiddeld 50, 7 puntkomma's, 0 "Wie"-openers, tmpl 2). De vorige 8,8
gold onder de oude gewichten (helderheid 30, taal 15). Onder de nieuwe gewichten en de
strengere taaleis (hardop-toets, §11.12) komt het college op 8,7. Geen feitelijke fouten.

## De drie verbeteringen met het meeste effect

1. **Taal (8,5 → 9): de zinnen uit de hardop-toets en de nog geldige ritmepunten
   herschrijven.** Het gaat om ongeveer tien zinnen: 02_06:261–265, :535–536, :561–562,
   :794–795, :904–905, :69–70, :89–90, :226–228, :1003–1004 en :1108–1109 (zie
   criterium 3). Geen inhoud erbij; herschrijven van de bestaande zin volstaat.
2. **Helderheid (8,5 → 9): drie plekken waar de lezer moet reconstrueren.** De volgorde
   "steeds minder" bij de drie woorden (02_06:261), de sprong van "bijna 24% per jaar"
   (02_06:573) naar "13,9 voorspeld" als *voorsprong* (02_06:925, met $-\mu$), en de
   symbolen $\omega$ en $c$ van Grossman en Stiglitz zonder orde van grootte
   (02_06:585–588).
3. **Code en figuren (8,5 → 9): de cachetruc en de leeswijzers.** De regel
   `hap_data.yahoo(["SPY", "TLT", "GLD", "QQQ", "IWM"], ...)["SPY"]` (02_06:981) laadt
   vier tickers die niet gebruikt worden; de leeswijzers "Let in de figuur ..." staan
   aan het eind van een alinea met een andere conclusie (02_06:727–730, :932–933).

Met deze drie: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,0.

## Deelcijfers

| nr | criterium | gewicht | deelcijfer | bijdrage |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 | 2,125 |
| 2 | Opbouw en rode draad | 20% | 9 | 1,800 |
| 3 | Taal | 20% | 8,5 | 1,700 |
| 4 | Toy-voorbeeld | 10% | 9 | 0,900 |
| 5 | Code en figuren | 10% | 8,5 | 0,850 |
| 6 | Replicatie en empirie | 10% | 9 | 0,900 |
| 7 | Oefeningen | 5% | 9 | 0,450 |
| | **Eindcijfer** | | **8,7** | 8,725 |

Taal is 8,5 en blokkeert dus niet; het streefcijfer 9,0 is niet gehaald.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- Toy-voorbeeld: de SDF krijgt naam, betekenis en getallen (0,8 en 1,2) voordat hij
  iets doet, $R^f$ wordt expliciet bruto genoemd met de afwijking van de setup
  (02_06:133–134), en de risicocorrectie van 4 op 116 tegen 76 maakt voorspelbaarheid
  zonder vergissing tastbaar.
- "Hoe het getoetst wordt": de filterformule $\rho_1\sigma_d\sqrt{2/\pi}$ krijgt nu
  herkomst, symboolnaam en een getal (0,095% per dag, bijna 24% per jaar).
- "Wat het niet verbiedt": direct na de propositie de Sharpe-ratio 0,13 en de
  SDF-schommeling van 13% per maand; de verdediger van efficiëntie die "alleen een SDF
  hoeft te kiezen" maakt de propositie handelbaar.

*Aanmerkingen*
- Opzet: drie woorden voor onvoorspelbaar. "De drie woorden zeggen steeds minder over
  wat een handelaar met het verleden kan." De definitie noemt ze in de volgorde fair
  game, martingaal, random walk; de zin loopt de andere kant op (random walk eerst),
  en "wat een handelaar met het verleden kan" laat het werkwoord weg.
- Opzet: "Bij een fair game daarentegen helpt het hem alleen niet om de afwijking van
  het vereiste rendement te voorspellen." "Alleen niet" is dubbelzinnig: bedoeld is
  "helpt het hem alleen bij die afwijking niet".
- Hoe het getoetst wordt: "Een fractie $\omega$ van de beleggers betaalt een bedrag
  $c$ voor een signaal over de waarde van het aandeel". Twee symbolen zonder orde van
  grootte; $\omega$ komt daarna niet meer terug.
- Hoe het getoetst wordt: "is dat $0{,}175 \cdot 0{,}68\% \cdot 0{,}80 \approx
  0{,}095\%$ per dag, bijna 24% per jaar." In de replicatie heet de voorspelling "13,9"
  en is ze een voorsprong op buy-and-hold ($-\mu$ in de formule van criterium 1). De
  lezer moet zelf zien dat 24% min het marktrendement ongeveer 13,9 is.
- Opzet, na de propositie: "autocorrelaties en variance ratios (de variantie over
  meerdere perioden gedeeld door het aantal perioden maal de eenperiodevariantie),
  meten eerste en tweede momenten." De definitie tussen haakjes breekt de zin
  [onderzoek B].

*Beter uitleggen*
- Bij de drie woorden: één zin die de volgorde van sterk (random walk) naar zwak (fair
  game) noemt, zodat de propositie "Van sterk naar zwak" aansluit.
- Bij de filterformule: zeg dat de 24% wat de handelaar *verdient* is en dat de
  voorsprong op buy-and-hold daar het gemiddelde rendement van aftrekt; dan herkent de
  lezer de 13,9 in de replicatie.
- Grossman en Stiglitz: een orde van grootte voor $c$ (bijvoorbeeld als fractie van het
  bruto voordeel), of het mechanisme zonder $\omega$.

*Voor een 9*
- 02_06:261–265: volgorde en werkwoord ("wat een handelaar met het verleden kan
  voorspellen").
- 02_06:572–574 en 02_06:925: verband tussen 24% per jaar en de voorspelde voorsprong
  van 13,9 procentpunt.
- 02_06:585–588: orde van grootte voor $c$, of $\omega$ weglaten.
- 02_06:289–291: de definitie van de variance ratio uit de haakjes, of vervangen door de
  verwijzing naar [](#01-02-bachelier) [onderzoek B].

### 2. Opbouw en rode draad (9)

*Goed*
- Overzicht: vraag, antwoord ("alleen te toetsen samen met een model ervan") en vijf
  stappen; het jaartal klopt nu met het kader (1970 sluit het tijdvak af).
- De drie verwachtingen uit de intuïtie worden elk in een andere vorm ingelost
  (02_06:380, :453, :591), en de toy-getallen keren terug in de theorie ($p_0 = 100$,
  $q = 0{,}4$, 4,35%) en in de simulatie (3,45% tot 5,26%).
- De overgang naar de replicatie zegt waarom het filter en niet de regressie wordt
  gerepliceerd (02_06:840–841). Lengte 5.709, onder de 6.000.

*Aanmerkingen*
- Overzicht: "Wat betekent het dat een prijs alle informatie weerspiegelt, en valt dat
  te toetsen?" herhaalt vrijwel woordelijk de open vraag uit het kader
  (02_06:31–32) [onderzoek B].

*Beter uitleggen*
- Geen.

### 3. Taal (8,5)

*Goed*
- De taalredactie heeft de staccato-plekken uit onderzoek B grotendeels opgelost:
  "Wat het model verklaart" en "Waar het breekt" openen nu met een volledige zin
  (02_06:1093, :1102), de SDF-alinea na de simulatiecel verbindt met "maar" en "want"
  (02_06:680–686), en "Met Fama en Blume delen we alleen de uitkomst ..." (02_06:928)
  leest natuurlijk.
- Motiefnamen elk hoogstens twee keer ("de standaardfout van 2%" op :800 en :1088,
  "risico of vergissing" op :777 en :1111, "theorie of feit" op :69), nergens als
  handelend onderwerp; geen "Wie"-zinnen, geen regeltaal, "In woorden:" en "Wat dit
  leert" elk één keer.
- Het tarwevoorbeeld bij Samuelson (02_06:300–304) en de verdediger van efficiëntie
  (02_06:459–464) lezen als gesproken uitleg.

*Aanmerkingen*
- Theorie, Opzet: "De drie woorden zeggen steeds minder over wat een handelaar met het
  verleden kan." (elliptisch, zie ook criterium 1).
- Hoe het getoetst wordt: "Daarom zegt een filter dat buy-and-hold verslaat meer dan
  een voorspellende regressie." Bij hardop lezen hoort de lezer eerst "een filter dat
  buy-and-hold verslaat meer dan ...".
- Hoe het getoetst wordt: "Voor de zwakke vorm is de filterregel de favoriete toets,
  omdat die de joint hypothesis grotendeels omzeilt." "Favoriete" van wie, en "die"
  kan de vorm of de toets zijn.
- Simulatie: "Bij $N^*$ is de toets gemiddeld net significant, wat ongeveer de helft
  kans op verwerping geeft." "De helft kans" is geen Nederlands.
- Replicatie: "Hun kolom na volle commissies is echter niet vergelijkbaar met onze
  0,1%." "Echter" contrasteert met niets in de zin ervoor; de zin leest als
  ingeplakte reparatiezin.
- Overzicht: "Bij de vraag theorie of feit, oftewel of we een theorie hebben die
  getoetst wordt of een feit dat op een verklaring wacht, is het antwoord hier
  ongewoon." Lange tussenzin met "oftewel" [onderzoek B].
- Intuïtie: "Dat is voorspelbaarheid, en toch vergist niemand zich." "Dat is"-opener
  [onderzoek B].
- Toy: "Dat is de *joint hypothesis* in het klein (gezamenlijke hypothese, de stelling
  dat elke toets van efficiëntie tegelijk een toets is van een model van het vereiste
  rendement)." Definitie van twintig woorden tussen haakjes na de clou [onderzoek B].
- Replicatie: "Ook een moderne index is dus iets trager dan een fonds dat werkelijk
  wordt verhandeld." "Trager dan een fonds" [onderzoek B].
- Wat er brak: "zeventig (formule) tot tachtig jaar (simulatie) data" hoort in een zin,
  niet in haakjes [onderzoek B]. In dezelfde alinea: "Efficiëntie alleen zegt niet of
  dat een inefficiëntie is of een meetfout" (efficiëntie die niet zegt of iets een
  inefficiëntie is, leest als woordspel).

*Beter uitleggen*
- Geen inhoudelijk punt; de aanmerkingen vragen herschrijven, geen nieuwe zinnen.

*Voor een 9*
- 02_06:261–265, :535–536, :561–562, :794–795, :904–905 (hardop-toets, zie onderaan).
- 02_06:69–70, :89–90, :226–228, :1003–1004, :1107–1109 [onderzoek B].
- 02_06:568–576: vijf getallen in één alinea (0,175; 0,68%; 0,80; 0,095%; 24%); de
  kalibratie kan naar een eigen zin of de tabel van de replicatie [onderzoek B].

### 4. Toy-voorbeeld (9)

*Goed*
- Twee perioden, vier dividenden, achterwaarts rekenen in drie regels, met de hand in
  vijf minuten na te rekenen.
- Tabel "met de hand" tegen "code" voor beide economieën; de slotzin maakt er de joint
  hypothesis in het klein van.
- De risicocorrectie van 4 op 76 tegen 116 legt de voorspelbaarheid uit met één
  deling.

*Aanmerkingen*
- Toy: "**Vooruitblik.** Met gewichten $q = \tfrac12 \cdot 0{,}8 = 0{,}4$ ..." voegt een
  tweede begrip toe dat pas in de theorie betekenis krijgt. Het wordt daar wel
  ingelost (02_06:432–434), dus geen aftrek onder 9.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `filter_positions` leest als de regel van Alexander, met een zichtbare lus en
  benoemde toestanden; `filter_performance` benoemt `held`, `gross` en `switches`.
- De SDF-controlecel (02_06:666–677) laat de propositie numeriek zien ("moet 0 zijn",
  "moet 1 zijn"); beide figuren hebben een bijschrift dat zegt wat te zien is.
- Elke cel heeft een zin ervoor en erna; de robuuste standaardfouten van
  `newey_west(..., lags=0)` worden in de tekst benoemd (02_06:1031–1032).

*Aanmerkingen*
- Replicatie, deelperiodes: `spy = hap_data.yahoo(["SPY", "TLT", "GLD", "QQQ",
  "IWM"], "1993-01-01")["SPY"]  # shared cached download; only SPY is used`. Vier
  tickers geladen om een cache te delen; de lezer ziet een truc [onderzoek B].
- Simulatie: "zoals het hoort. Let in de figuur links op de afstand tussen de twee
  soorten punten" staat aan het eind van een alinea over de powertabel; hetzelfde bij
  "Let in de figuur op de afstand tussen de ronde punten en de vierkanten" na de zin
  over de makelaar [onderzoek B].
- `first = held.ne(0).idxmax()` is een compacte truc voor "eerste dag met een positie";
  het commentaar redt het, een benoemde hulpregel zou beter lezen.

*Beter uitleggen*
- Geen.

*Voor een 9*
- 02_06:981: alleen `["SPY"]` laden, of de cachereden in de tekst.
- 02_06:727–730 en 02_06:932–933: de leeswijzer als eigen korte alinea direct vóór de
  figuurcel [onderzoek B].

### 6. Replicatie en empirie (9)

*Goed*
- Beide blokken hebben bron, wat, data, verschil en een verwachte afwijking met
  toetsbare criteria; het filteroordeel ("Geslaagd op criterium 1", "op criteria 2 en
  3") verwijst naar die criteria.
- De deelperiodes toetsen de verklaring van niet-synchrone handel in plaats van haar
  aan te nemen: de voorsprong stijgt met $\rho_1$ en wordt negatief op SPY.
- Jensen: tabel origineel/hier, controlefonds VFINX, en de standaardfout van één
  procentpunt koppelt het resultaat aan de meetbaarheid van vaardigheid.

*Aanmerkingen*
- Replicatie: "met 12,9 procentpunt per jaar, tegen 13,9 voorspeld en 1,7 bij Fama en
  Blume. Na 0,1% per transactie blijft er ruim acht procentpunt over." Vier getallen
  in lopende tekst die in de tabel van de cel ernaast staan; acceptabel omdat het
  oordeel ze nodig heeft.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy ($k$), afleiding (Samuelson-effect), uitbreiding van de replicatie
  (break-even kosten); elke uitwerking eindigt met een les.
- Oefening 3 sluit met de zin die het college samenvat: de trend bestond alleen in een
  index die niet te kopen was.

*Aanmerkingen*
- Uitwerking 3: "Alleen lang gaan geeft een lagere $c^{*}$, 0,16% en 0,27% voor
  1990". "Voor 1990" staat vlak na "voor kosten" en leest even als dat; "vóór 1990" of
  "tot 1990".

*Beter uitleggen*
- Geen.

## Feitelijke fouten

Geen. Nagerekend (hand en `notes/feiten-02_06_efficiente_markten.md`, celuitvoer):
toy 116, 76, 92, 96, 4,35%, 3,45%, 5,26%, $q = 0{,}4$, covariantie $1 - 1{,}0435$;
$0{,}175 \cdot 0{,}68\% \cdot 0{,}798 = 0{,}095\%$ per dag, maal 252 is 23,9%;
Sharpe-ratio 0,13; $12 \cdot 0{,}3\% = 3{,}6$ pp rond 7,2%; $\sigma/\mu = 7{,}5$ en
drempel 3 bij 1,5%; $R^2 = 0{,}09/20{,}34 = 0{,}44\%$; $3{,}84/0{,}0044 = 873 \approx
870$ maanden (ruim 72 jaar); $7{,}84/0{,}0044 = 1782 \approx 1780$ (bijna 150 jaar);
60% na 100 jaar; filter 12,9 tegen 13,9 en 1,7, ruim acht na kosten, 48 transacties;
deelperiodes monotoon in $\rho_1$, SPY het grootste verlies; FB-reeks boven 1% overal
onder hun buy-and-hold 0,0986 (bijschrift klopt); Jensen $-0{,}3\%$ ($t = -0{,}7$),
Contrafund 1,4%/1,3 ≈ 1,1 pp, bèta 1,01 tegen 0,84, 44 jaar; oefening 1 $k = 4/11$,
6,45%, 8,51%, 33%; oefening 2 $2^{22} \approx 4{,}2$ miljoen; oefening 3 0,27% tot
0,41%, 6,8% tegen 10,4%. Beide fouten uit de vorige ronde (filter "pas vanaf 10%",
"begint het tijdvak") zijn hersteld.

## Navertelling in vijf zinnen

1. Een prijs die de verwachting is van een latere uitbetaling, verandert
   onvoorspelbaar (Samuelson), maar voor aandelen geldt dat pas na weging met de SDF,
   zodat verwachte rendementen rationeel voorspelbaar kunnen zijn.
2. Omdat bij elk arbitragevrij patroon een SDF te vinden is die het als risicopremie
   verklaart, is efficiëntie alleen samen met een model van risico te toetsen, en dat is
   de joint hypothesis.
3. Een onderzoeker met het verkeerde (constante) model vindt in een volledig rationele
   economie na een eeuw maanddata in zes van de tien gevallen inefficiëntie, omdat een
   $R^2$ van 0,44% zo'n zeventig tot tachtig jaar data vraagt.
4. Het 0,5%-filter versloeg de index in 1957–1962 met bijna 13 procentpunt per jaar,
   maar de voorsprong volgt de autocorrelatie van de index door niet-synchrone handel
   en verdwijnt op het verhandelbare SPY.
5. Actieve fondsen verslaan de markt niet, en of er in de jaren zestig werkelijk iets
   te verdienen was (Chicago tegen Yale), blijft open zolang niet bekend is wie tegen
   welke prijs kon handelen.

De navertelling valt samen met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk natuurlijker gemaakt: de etiketopeners in "Wat
er brak" zijn weg, de simulatieparagrafen verbinden met voegwoorden, en de telregels
zijn ruim gehaald. Wat overblijft zijn losse zinnen die op papier kloppen maar hardop
haperen, vooral in "Hoe het getoetst wordt" en de Opzet van de theorie, plus vijf
kleinere punten uit onderzoek B die de redacteur heeft laten staan.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. 02_06:561–562. "Daarom zegt een filter dat buy-and-hold verslaat meer dan een
   voorspellende regressie."
   → "Verslaat een filter buy-and-hold, dan zegt dat daarom meer dan een significante
   voorspellende regressie."
2. 02_06:261–265. "De drie woorden zeggen steeds minder over wat een handelaar met het
   verleden kan. [...] Bij een fair game daarentegen helpt het hem alleen niet om de
   afwijking van het vereiste rendement te voorspellen."
   → "Van random walk naar fair game zeggen de drie woorden steeds minder over wat een
   handelaar uit het verleden kan voorspellen. [...] Bij een fair game kan hij met het
   verleden alleen de afwijking van het vereiste rendement niet voorspellen, de
   spreiding bijvoorbeeld wel."
3. 02_06:794–795. "Bij $N^*$ is de toets gemiddeld net significant, wat ongeveer de
   helft kans op verwerping geeft."
   → "Bij $N^*$ is de toets gemiddeld net significant, zodat hij in ongeveer de helft
   van de economieën verwerpt."

## Controle 1

Controle na R9-1 (rapport `notes/rapport-02_06_efficiente_markten.md`, sectie "R9-1
(F6b, ronde 9+)"). `prose_stats --check`: PASS, 5.812 woorden (was 5.709), zinnen
gemiddeld 16,9, p90 28, geen zin boven 40, 7 puntkomma's, engquote 4, tmpl 2.
`nb_outputs` ongewijzigd volgens het rapport: alleen proza, code-commentaar en twee
variabelenamen zijn aangepast, geen celuitvoer.

**De drie verbeteringen met het meeste effect**
1. Taal (hardop-toets en ritmepunten): **opgelost**. Alle tien plekken (261–265,
   535–536, 561–562, 794–795, 904–905, 69–70, 89–90, 226–228, 1003–1004,
   1107–1109) zijn herschreven; de drie hardop-zinnen komen vrijwel woordelijk
   overeen met het voorstel van de vorige ronde.
2. Helderheid (drie plekken): **opgelost**. Volgorde en werkwoord bij de drie
   woorden (261–265: "Van random walk naar fair game ... kan voorspellen"); het
   verband 24% tegen 13,9 staat nu expliciet in de Geslaagd-zin ("13,9 (de bijna
   24% uit de theorie min het gemiddelde rendement van de index)", 940–943); bij
   Grossman-Stiglitz is $\omega$ weggelaten en staat de richting van $c$ er wel
   (591–597).
3. Code en figuren (cachetruc en leeswijzers): **deels**. De leeswijzers staan nu
   als eigen korte alinea direct vóór de figuurcel, op beide plekken (r. 741–742
   en 951–952): opgelost. De SPY-cel laadt nog vijf tickers (r. 1001); de tekst
   zegt nu dat de cel "dezelfde download van vijf ETF's als [00-00-setup]"
   gebruikt (r. 991–992), maar noemt het woord cache niet en zegt niet waarom vijf
   tickers nodig zijn in plaats van één. Een lezer die 00-00-setup niet meer voor
   ogen heeft, ziet nog steeds een niet-uitgelegde truc. Dit is de tweede optie uit
   de vorige beoordeling, maar zwak uitgevoerd: geen aftrek voor de code zelf
   (onvermijdelijk offline), wel voor de uitleg.

**Voor een 9, per criterium**
- Helderheid (4 punten): alle vier **opgelost** — volgorde/werkwoord (261–265);
  verband 24%/13,9 (574–578, 940–943); $\omega$ weg bij Grossman-Stiglitz
  (591–597); variance-ratio-definitie uit de haakjes, nu met "want" in de zin
  (289–291).
- Taal (11 punten: 5 hardop/ritme, 5 onderzoek B, 1 getallenalinea): alle elf
  **opgelost**. "Favoriete toets" → "aantrekkelijke toets" met "een filter" als
  helder antecedent (536); "echter" in de replicatie vervangen door een reden
  (920–921); de vijf onderzoek-B-zinnen herschreven (68–70 zonder "oftewel",
  87–92 zonder "Dat is"-opener, 224–227 definitie in de zin met "en ze betekent
  dat", 1024–1025 "lopen iets achter op" in plaats van "trager dan", 1132 "zonder
  model van risico" in plaats van het woordspel); de vijf getallen bij de
  filterformule staan nu in een eigen alinea (574–578) en worden in de
  Geslaagd-zin teruggenomen.
- Code en figuren (2 punten): leeswijzers **opgelost** (741–742, 951–952);
  SPY-cel **deels** (zie boven).

**Aanmerkingen zonder eigen "Voor een 9", ter controle**
- Opbouw, Overzicht herhaalt de kaderzin: **opgelost**, het overzicht opent nu met
  het antwoord in plaats van de vraag (37–40). Opbouw stond al op het plafond (9)
  en blijft 9.
- Code, `first = held.ne(0).idxmax()`: **opgelost**, hernoemd tot `first_signal`
  met commentaar in beide functies (891, 1261); niet vereist voor de 9, wel
  gedaan.
- Oefening 3, "voor 1990": **opgelost**, nu "in de twee perioden tot 1990" (1287).

**Beter uitleggen**: geen resterende punten; alle voorstellen uit de vorige ronde
vallen samen met de "Voor een 9"-lijst hierboven en zijn daar gecontroleerd.

**Feitelijke fouten**: geen. Geen celuitvoer gewijzigd, geen nieuw getal in de
proza zonder cel of bron; geen verslechtering gevonden.

**Hardop-toets**: de drie aangewezen zinnen (561–563, 260–265, 807–809) zijn
vervangen door vrijwel het voorstel van de vorige ronde en lezen nu natuurlijk. Een
nieuwe steekproef van drie alinea's (Grossman-Stiglitz r. 591–597, de SPY-cel-zin
r. 991–992, de Samuelson-alinea r. 299–305) leest hardop natuurlijk; geen nieuw
punt.

**Nieuwe deelcijfers**

| nr | criterium | gewicht | deelcijfer | bijdrage |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 | 2,25 |
| 2 | Opbouw en rode draad | 20% | 9 | 1,80 |
| 3 | Taal | 20% | 9 | 1,80 |
| 4 | Toy-voorbeeld | 10% | 9 | 0,90 |
| 5 | Code en figuren | 10% | 8,7 | 0,87 |
| 6 | Replicatie en empirie | 10% | 9 | 0,90 |
| 7 | Oefeningen | 5% | 9 | 0,45 |
| | **Eindcijfer** | | **9,0** | 8,97 |

Plafondregel toegepast: Opbouw, Toy, Replicatie en Oefeningen hadden geen "Voor
een 9" in de vorige ronde en blijven op hun oude cijfer (9). Helderheid en Taal
hadden elk een volledige lijst met punten die allemaal zijn opgelost en gaan naar
het in het vooruitzicht gestelde plafond (9). Code en figuren had een plafond van
9, maar één van de twee punten (de SPY-cel) is maar deels opgelost, dus het
deelcijfer blijft eronder op 8,7.

Taal (9) blokkeert niet. Geen deelcijfer onder 8,5. Streefcijfer 9,0 is gehaald
(ruw 8,97, afgerond 9,0); de enige rem op een hoger cijfer is de niet-expliciete
cachereden bij de SPY-cel.
