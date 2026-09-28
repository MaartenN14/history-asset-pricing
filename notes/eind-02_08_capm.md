STATUS 02_08_capm F6c words=5732 prose=PASS open=0 cijfer=9,0 min=9

# Ronde 9+

Vorige ronde: 8,6

Eindbeoordeling (F6) van `lectures/02_08_capm.md` na de taalredactie. Gelezen: het
college volledig, `plannen/kaart-rollen.md`, `plannen/rubriek-didactiek.md`, STYLE §11.12,
de treffers voor dit college in `notes/onderzoek-D-meetbaar.md` (de andere vier onderzoeken
noemen het college niet). Alle codecellen opnieuw uitgevoerd met `HAP_OFFLINE=1`; de
getallen hieronder komen uit die uitvoer.

## De drie verbeteringen met het meeste effect

1. **Replicatie, oordeelstabel (lectures/02_08_capm.md:1035).** De rij "na BJS" schrijft
   de French-decielen "GRS 4,20 > 1,52" toe. Voor de tien decielen is GRS 2,03 tegen een
   grens van 1,84 ($p = 0{,}028$); 4,20 tegen 1,52 hoort bij de 25 size/BM-portefeuilles
   (zo staat het ook goed op regel 484). Rij corrigeren of de GRS van de 25 er apart bij
   noemen. Verwacht: replicatie 8,5 → 9.
2. **"De rand" dekt twee begrippen (regel 42 tegen 375–377 en 410–412).** De redactie
   maakte van "de rand" een alias voor de efficiënte grens, maar de zero-beta-portefeuille
   $z$ ligt op het ondoelmatige deel van de minimum-variantierand, en "elk verwacht
   rendement op de rand is haalbaar" (412) geldt alleen voor die hele rand. Het kopje
   "de markt ligt op de rand" (329) mag blijven; de alias op regel 42 moet de rand van
   minimale variantie noemen, of het theorema van Black moet "minimum-variantierand"
   zeggen, zoals het bewijs op regel 400 al doet. Verwacht: helderheid 8,5 → 9.
3. **"Excess" in figuren en tabel, plus drie stroeve zinnen.** De y-as heet twee keer
   "Gemiddeld excess rendement" (816, 1071) en de kolom "gem. excess (% p.m.)" (943) staat
   in de getoonde tabel; de tekst zegt sinds de redactie overal "overrendement". Dat moet
   om (H7; figuren en tabellen zijn Nederlands). Daarnaast de zinnen op 252–253, 367–368
   en 482–484 (zie het taaloordeel). Verwacht: code en figuren 8,5 → 9, taal 8,5 → 9.

Met alle drie: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,0.

**Oordeel over de oude termen.** "Excess" moet om (punt 3). "De rand" in het kopje mag
blijven, omdat regel 42 de alias invoert; het probleem is de inhoud van de alias, niet het
kopje. "Marktclearing" in de stapkoppen (137, 288) is geen oude term: de tekst gebruikt het
woord zelf ook (42, 273) en regel 31 zegt al wat het betekent. Eén uitleg bij de eerste
keer op regel 42 ("vraag gelijk aan aanbod voor elk aandeel") is genoeg; dat telt niet als
aanmerking.

## Eindcijfer: 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,80 + 1,70 + 0,90 + 0,85 + 0,85 + 0,45 = 8,675, dus 8,7. Geen deelcijfer
onder 8,5; taal blokkeert niet. Lengte: 5.634 woorden proza, onder de 6.000.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- Theorie, "Het kernresultaat": de vraag van één belegger wordt het recept uit het toy, met
  de schalen 1/2 en 1/6 erbij (254), en $\theta_m$ krijgt twee getallen, 4,5 in het toy en
  3,0 in de kalibratie van de simulatie (319–322).
- "Hoe het getoetst wordt: Fama en MacBeth": waarom de standaardfout klopt (een portefeuille
  met bèta één en kosten nul) en hoe groot ze is (0,21% per maand, 2,5% per jaar).
- "Geschatte bèta's": $\kappa = 0{,}52$, het intercept 3,4% per jaar te hoog, en bij
  $n = 50$ is $\kappa = 0{,}98$; elke formule heeft haar getal.

*Aanmerkingen*
- Overzicht: "marktclearing en de efficiënte grens van Markowitz (hierna kortweg de rand)"
  tegen Zero-beta-CAPM: "dan bestaat er een portefeuille $z$ op de rand met
  $\Cov(r_z, r_m) = 0$". De zero-beta-portefeuille ligt niet op de efficiënte grens.
- "Hoe het getoetst wordt: de tijdreeks en GRS": "en de $F$-verdeling is de exacte vorm van
  een $\chi^2$-toets op alle alpha's samen in een eindige steekproef." Drie begrippen in één
  bijzin; de lezer krijgt niet mee wat "exacte vorm" hier betekent.

*Beter uitleggen*
- Replicatie, oordeelstabel: "$\gamma_0$ 0,27 (FM 0,48, al als overrendement)". Regel 543–545
  zegt dat Fama en MacBeth $\gamma_0 = R^f$ toetsten met ruwe rendementen; een halve zin dat
  hun 0,48 al $\gamma_0 - R^f$ is, maakt de vergelijking leesbaar.
- Toy: de tabelrij "risicovrij belegger 1" toont −187,5. Dat een minteken lenen betekent,
  staat nergens.

*Voor een 9*
- lectures/02_08_capm.md:42 en :375–377, :410–412: één naam voor de efficiënte grens en een
  andere voor de minimum-variantierand (H7).
- lectures/02_08_capm.md:482–484: de GRS-zin in tweeën, met de betekenis van de
  $F$-verdeling in gewone woorden.
- lectures/02_08_capm.md:1039: de 0,48 van FM benoemen als overrendement.

### 2. Opbouw en rode draad (9)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord in de eerste twee zinnen; de routekaart
  (200–205) en "Samengevat" (629–646) staan waar ze horen.
- Het toy draait Markowitz om en levert precies de 10%, 14% en 4% van [](#01-04-markowitz);
  de simulatie noemt de 6,22% van het toy als ijkpunt (655).
- De simulatie opent met haar conclusie (650–651) en de slotsectie haalt de simulatie terug
  (1101–1102).

*Aanmerkingen*
- "Geschatte bèta's: waarom de lijn te vlak lijkt": "*Waarom zou dit waar zijn?* Een
  onderzoeker regresseert gemiddelde rendementen op geschatte bèta's." De `###` opent met een
  vast etiket in plaats van met de bewering (H9); de zin erna doet het werk al.

### 3. Taal (8,5)

*Goed*
- De redactie heeft de "In woorden:"- en "Het bewijsidee:"-formules vervangen door gewone
  zinnen met "dus" (270, 446); het college leest nu als doorlopende uitleg.
- Verband met voegwoorden in plaats van knippen: "Wil iedereen samen meer van een aandeel dan
  er is, dan stijgt de prijs en daalt het verwachte rendement tot vraag en aanbod weer gelijk
  zijn." (235–237)
- Eén naam per begrip in de proza: "overrendement" overal, "alpha", motiefnamen elk één keer.

*Aanmerkingen*
- "Het kernresultaat": "Zo komen we terug bij de separatiestelling uit [](#01-04-markowitz),
  volgens welke iedereen de tangentportefeuille houdt, aangevuld met lenen of uitlenen."
  ("volgens welke" is schrijftaal.)
- "Zonder vrij lenen": "Deze redenering maakte {cite:t}`Black1972` exact, en hij liet zien dat
  er zelfs geen risicovrij activum voor nodig is." ("maakte exact" is vertaald *made
  precise*.)
- Toy, stap 5: "Toch ligt C, met de laagste Sharpe-ratio (0,20 tegen 0,40), even precies op
  de lijn als A en B." ("even precies" struikelt; nog geldig uit [onderzoek D], C:164.)
- Toy: "De code rekent hetzelfde na en zet de handgetallen ernaast." Dezelfde zin staat in
  vrijwel elk college [onderzoek D], C:166.
- "Wat er brak": "Wie niet kan lenen, betaalt dan bewust meer voor hoge bèta, ..., en wie wel
  kan lenen, verdient die meerprijs ...". Met regel 85 en 623 zijn dat vier "wie"-zinnen, de
  bovengrens [onderzoek D], C:1107; "Beleggers die niet kunnen lenen" ontlast.
- "Zonder vrij lenen": "en dat is het speciale geval waarin iedereen tegen $R^{f}$ kan lenen"
  [onderzoek D], C:430, deels opgelost; "dat" verwijst naar een hele bijzin.

*Beter uitleggen*
- Geen inhoudelijk punt; alle aanmerkingen zijn zinsbouw.

*Voor een 9*
- lectures/02_08_capm.md:252–253, :367–368, :482–484 herschrijven (zie het taaloordeel
  onderaan).
- lectures/02_08_capm.md:164 en :1106–1107 zoals hierboven.

*Nog geldig uit onderzoek D*: C:164, C:166, C:430, C:1107 (hierboven). Opgelost: C:617,
C:960, C:1093, C:1118, C:1248; de alinea's van één zin (0 volgens prose_stats) en de dubbele
punt midden in een zin (5,3 per 1000 woorden). "Pre-ranking" (625, 705) staat nog, maar
wordt op 625 uitgelegd; dat laat ik staan.

### 4. Toy-voorbeeld (9)

*Goed*
- Vijf handstappen, één mechanisme, hoogstens één nog niet afgeleide formule (het recept,
  en de tekst zegt dat de theorie het afleidt).
- De tabel "met de hand"/"code" is kolom voor kolom gelijk (nagerekend: 4,5; 8%, 12%, 2%;
  −187,5; 0,013827; 6,22%; 9/7, 27/14, 9/28; 0,857).
- Slotzin zegt wat het getal betekent: beide beleggers houden de markt en de premies liggen
  op een lijn in bèta.

*Aanmerkingen*
- Toy, stap 3: "De rij van C geeft $x_C = 0{,}02/0{,}01 = 2$, waarna de rijen van A en B
  $x_B = 1$ en $x_A = 1{,}5$ opleveren." Het 2×2-stelsel voor A en B staat niet uitgeschreven;
  met de hand kost dat de lezer een minuut zoeken. Klein.

### 5. Code en figuren (8,5)

*Goed*
- `fama_macbeth_gammas` houdt de maandlus zichtbaar en noemt de gewichten die achter
  $\gamma_j$ zitten, precies zoals de tekst op 547–553 het uitlegt.
- Elke cel heeft een zin ervoor en erna; vóór beide figuren staat waarop te letten.

*Aanmerkingen*
- Simulatiefiguur: `ax.set_ylabel("Gemiddeld excess rendement (% per maand)")` (816), en
  dezelfde as in de replicatiefiguur (1071). De tekst zegt "overrendement".
- Replicatie, tijdreekstabel: kolom `"gem. excess (% p.m.)"` (943) staat in de getoonde
  tabel.

*Voor een 9*
- lectures/02_08_capm.md:816, :943, :1060–1061, :1071: "excess" → "overrendement" (let op:
  de kolomnaam wordt op 1060–1061 in de figuurcel gebruikt en moet mee).

### 6. Replicatie en empirie (8,5)

*Goed*
- Admonition in vijf onderdelen, binnen 250 woorden, met een verwachte afwijking die per
  periode wordt afgelopen.
- Oordeel begint met "Gedeeltelijk geslaagd" en staat in een tabel verwacht/hier/oordeel.
- Uitleg van de mislukte jaren dertig (grootte en bèta vallen samen), die oefening 3 toetst.

*Aanmerkingen*
- Oordeelstabel, rij "na BJS": "French-decielen $\gamma_1$ 0,28 bij premie 0,60; alpha
  laagste deciel 0,21 ($t = 2{,}53$); GRS 4,20 > 1,52". Feitelijke fout, zie onder.
- Oordeel: "De tabel meet elke periode aan de verwachte afwijking". Grenst aan regeltaal
  (STYLE §11.12); "aan wat we verwachtten" leest natuurlijker.

*Voor een 9*
- lectures/02_08_capm.md:1035: GRS van de decielen (2,03 > 1,84) of die van de 25 size/BM
  (4,20 > 1,52) met de juiste verzameling.

### 7. Oefeningen (9)

*Goed*
- Instap (variatie op het toy), afleiding ($\sigma_u^2$ en de minimale $n$), uitbreiding van
  de replicatie; elke uitwerking eindigt met wat ze leert (1163–1164, 1212–1214, 1246–1250).
- Oefening 3 laat zien dat de keuze van basisactiva het antwoord verandert, precies de zwakte
  die de replicatie noemt.

*Aanmerkingen*
- Geen.

## Feitelijke fouten

Nagerekend tegen de opnieuw uitgevoerde cellen: toy (alle elf rijen), $\theta_m \approx 3{,}0$,
15,6% per jaar, 0,21% per maand en 2,5% per jaar, Shanken 2%, $\sigma_u^2 = 0{,}082$,
$\kappa = 0{,}52$ en 0,98, 0,29% en 3,4%, 7,2%; simulatie (0,316/0,318; 0,298/0,287; ruim
3,5% per jaar; 0,594 en 0,015; 2,465 = 2,465; 18%; 95,7%; 0,22); 54 maanden bij de eerste
sortering; replicatie (bèta 1,69 tot 0,91, SE 0,29 tot 0,58, alle $|t(\alpha)| < 1{,}4$;
rijen 1036–1039; na BJS alle hellingen niet significant en GRS overal boven de grens;
$R^2$ 0,81 tot 0,93; 757 maanden); oefeningen (4; 5,53%; 7,11/10,67/1,78%; 150 en 150; 18 en
33; 0,74; 0,80; 0,29 met $t = 1{,}05$). De fout uit de vorige ronde ("bruto conventie") is
weg. Twee punten zijn open.

1. **lectures/02_08_capm.md:1035.** "GRS 4,20 > 1,52" bij de French-decielen. Celuitvoer
   (late steekproeven): French bèta-decielen GRS 2,025, grens 1,843, $p = 0{,}028$; 25 size/BM
   GRS 4,196, grens 1,521. De verwerping klopt, de getallen horen bij de andere verzameling.
2. **lectures/02_08_capm.md:42 met :375–377 en :412.** Met "de rand" gedefinieerd als de
   efficiënte grens is "een portefeuille $z$ op de rand met $\Cov(r_z, r_m) = 0$" onjuist: de
   zero-beta-portefeuille van een efficiënte portefeuille ligt op het ondoelmatige deel van de
   minimum-variantierand, en niet elk verwacht rendement is op de efficiënte grens haalbaar.
   Ontstaan in de taalredactie (voorheen "de efficiënte rand" zonder alias).

## Navertelling in vijf zinnen

Als alle beleggers mean-variance-optimaliseren met dezelfde verwachtingen en vrij kunnen lenen,
dwingt de gelijkheid van vraag en aanbod de markt om de tangentportefeuille te zijn. Daaruit
volgt dat het verwachte overrendement van elk aandeel bèta maal de marktpremie is, met een
premie die gelijk is aan de geaggregeerde risicoaversie maal de marktvariantie. Zonder vrij
lenen blijft de lijn recht maar wordt ze vlakker, met een intercept boven de risicovrije rente
(Black). Toetsen met geschatte bèta's op losse aandelen geven ook bij een geldig CAPM een te
vlakke lijn, wat portefeuilles oplossen, al blijft de premie onnauwkeurig gemeten. Op echte data
is de lijn sinds de jaren zestig te vlak en verwerpt GRS, en of dat risico (leenbeperkingen) of
vergissing is, valt niet uit de data op te maken. Dit klopt met het Overzicht.

## Taal na de redactie

De redactie heeft gewerkt: de vaste formules zijn weg, "overrendement" is overal doorgevoerd,
de zinnen lopen met voegwoorden, en prose_stats geeft PASS (zinslengte 17,2, geen alinea van
één zin). Wat rest, is een handvol schrijftaalzinnen en de achtergebleven "excess" in figuren
en tabel. Hardop-toets op drie alinea's (Het kernresultaat, Zonder vrij lenen, GRS):

1. Regel 252–253: "Zo komen we terug bij de separatiestelling uit [](#01-04-markowitz),
   volgens welke iedereen de tangentportefeuille houdt, aangevuld met lenen of uitlenen."
   → "Dat is de separatiestelling uit [](#01-04-markowitz): iedereen houdt de
   tangentportefeuille en leent of belegt daarnaast tegen de risicovrije rente."
2. Regel 367–368: "Deze redenering maakte {cite:t}`Black1972` exact, en hij liet zien dat er
   zelfs geen risicovrij activum voor nodig is."
   → "{cite:t}`Black1972` werkte deze redenering exact uit en liet zien dat ze zelfs zonder
   risicovrij activum opgaat."
3. Regel 482–484: "GRS meet dus hoeveel de beste portefeuille van de testactiva de
   Sharpe-ratio van de markt verslaat, geschaald met de ruis, en de $F$-verdeling is de exacte
   vorm van een $\chi^2$-toets op alle alpha's samen in een eindige steekproef."
   → "GRS meet dus hoeveel de beste portefeuille van de testactiva de Sharpe-ratio van de markt
   verslaat, geschaald met de ruis. Voor een eindige steekproef geeft de $F$-verdeling de
   exacte kritieke waarde van wat anders een $\chi^2$-toets op alle alpha's samen zou zijn."

## Controle 1

Per punt uit F6 (eindbeoordeling 8,7), tegen R9-1 (rapport) en het college zelf.

**Feitelijke fouten (2).**
1. GRS-getallen na BJS (r. 1071, was 1035): opgelost. Celuitvoer bevestigt French
   bèta-decielen GRS 2,025, grens 1,843, p = 0,028; de tekst citeert nu exact deze
   rij en laat de 4,196/1,521 van de 25 size/BM waar ze horen (r. 1054, 1059).
2. "De rand" (thm-capm-zerobeta, r. 389–403, en bewijs r. 412–441): opgelost op de
   genoemde plekken. Het theorema zegt nu expliciet dat $z$ op de minimum-variantierand,
   onder de minimum-variantieportefeuille en dus op het ondoelmatige deel ligt (r.
   395–397); bewijsstap 3 (r. 431–435) gebruikt "minimum-variantierand" tweemaal en
   legt uit waarom $z$ ondoelmatig is. Regel 42 laat de alias bewust ongewijzigd
   ("efficiënte grens van Markowitz, hierna kortweg de rand"); de tegenstrijdigheid
   die de fout veroorzaakte is opgelost doordat precies de plekken die haar
   opleverden nu "minimum-variantierand" zeggen.

**Drie verbeteringen.**
1. GRS: opgelost (zie boven).
2. "De rand": opgelost op de genoemde plekken (zie boven); zie extra controle 2
   voor twee resterende kale vermeldingen elders.
3. "Excess" en drie stroeve zinnen: opgelost. Beide y-assen (r. 847, 1107) en de
   tabelkolom (ook in de figuurcel, r. 974, 1096) heten nu "overrendement". De
   separatiezin (r. 267–268), de Black-zin (r. 385–387) en de GRS-zin (r. 508–511,
   nu in tweeën) zijn herschreven zoals voorgesteld.

**Voor een 9 / Aanmerkingen / Beter uitleggen, overige.**
- FM 0,48 als overrendement benoemd (r. 1075): opgelost.
- Minteken −187,5 uitgelegd (r. 206–209): opgelost.
- Toy stap 3, 2×2-stelsel uitgeschreven (r. 157–159): opgelost.
- Attenuatie-### opent met de bewering, niet met het etiket (r. 592–594): opgelost.
- Taal: "Wie"-zinnen op 3 (onder de grens van 4), "even precies" (r. 173), "dat is
  het speciale geval" (r. 449) en "meet elke periode aan" (r. 1066) herschreven:
  opgelost.

Geen verslechtering en geen nieuwe feitelijke fout gevonden. Geen nieuwe punten.

**Extra controle 1 (GRS-getallen).** `uv run python tools/nb_outputs.py
lectures/02_08_capm.ipynb` geeft voor "French bèta-decielen 1963-heden": GRS 2,025,
grens 1,843, p 0,028 — gelijk aan r. 1071. Geslaagd.

**Extra controle 2 ("de rand").** Op de expliciet genoemde plekken (theorema van
Black, zero-beta-portefeuille, bewijsstap 3, regel 42) klopt het onderscheid nu
overal. Twee plekken blijven met een kale "de rand"/"randportefeuilles" die, gelezen
via de alias op regel 42 (efficiënte grens), zelf weer dubbelzinnig zijn: de eerste
zin van het theorema ("dus een portefeuille op de rand", r. 394) en bewijsstap 1
("de markt ligt op de rand ... ligt ook zo'n combinatie op de rand", r. 415–418; ook
r. 407). Geen van beide beweert iets onjuists — de context ontleedt het binnen
dezelfde alinea — dus geen feitelijke fout en geen nieuw punt, maar wel dubbelzinnig;
niet in de oorspronkelijke beoordeling genoemd, dus buiten de plafondregel.

## Eindcijfer (Controle 1): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,0. Geen deelcijfer onder
8,5; taal blokkeert niet.
