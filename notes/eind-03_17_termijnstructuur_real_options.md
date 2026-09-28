STATUS 03_17_termijnstructuur_real_options F6c words=5678 prose=PASS open=0 cijfer=9,0 min=9,0

# Ronde 9+

Vorige ronde: 8,9

Eindbeoordeling F6 van `lectures/03_17_termijnstructuur_real_options.md` na de taalredactie
(`notes/taal-03_17_termijnstructuur_real_options.md`), met verse ogen en met de gewichten
van ronde 9+ (helderheid 25, opbouw 20, taal 20, toy 10, code en figuren 10, replicatie 10,
oefeningen 5). `prose_stats --check`: 5.552 woorden, PASS (sent_mean 15,9; één zin boven 40
woorden, de opsomming in het Overzicht; semicol 13; colon_mid 2,3; wie_open 3).

## De drie verbeteringen met het meeste effect

1. **Taal (8,5 → 9).** "term premium" wordt "termijnpremie" (STYLE §3, zoals equity premium
   aandelenpremie werd) en "Itô's lemma" wordt "het lemma van Itô" (vaste-termentabel).
   Herschrijf daarnaast de CIR-opener (r. 458) en de Santa-Clara-zin (r. 1219–1221), en breng
   de alinea's op r. 568–572 en r. 785–788 terug tot hoogstens drie getallen per alinea.
2. **Helderheid (8,5 → 9).** Leg in één bijzin uit waarom LSM met drie polynomen 0,005 bóven
   de boom ligt, hoewel de stelling een ondergrens belooft (r. 1192–1195). Houd de twee
   betekenissen van de termijnpremie uit elkaar: 1,5 pp verwacht overrendement per jaar
   (r. 316–319) tegenover 3 pp in de lange yield (r. 443, r. 1332). Laat de alinea op
   r. 217–222 de eigen vraag beantwoorden.
3. **Opbouw (8,5 → 9).** Beperk de verwachtingen in de intuïtie (r. 99–104) tot de kern. Laat
   de simulatie ook de lengte van de echte steekproef gebruiken (55 jaar in plaats van 40,
   r. 745 en r. 768), of zeg in één zin waarom het 40 jaar is.

## Eindcijfer: 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,70 + 1,70 + 0,90 + 0,90 + 0,90 + 0,45 = 8,675, dus 8,7. Laagste
deelcijfer 8,5. De eis van ronde 9+ (≥ 9,0, geen deelcijfer onder 8,5) is **niet gehaald**.
Taal blokkeert niet (≥ 8). De daling ten opzichte van 8,9 komt niet door de redactie, want
die heeft de tekst merkbaar natuurlijker gemaakt. Ze komt door de nieuwe gewichten (taal
20% in plaats van 15%), door de strengere lat voor een 9 en door drie punten die verse ogen
nu vinden (LSM boven de boom, de dubbele termijnpremie en de CIR-opener).

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed.*
- Theorie, "Het kernresultaat": het argument van de handelaar gaat vóór de stelling, en het
  bewijs is die positie. Elke aanname staat bij de stap die haar gebruikt ("(aanname 2)",
  "(aanname 1)", "(aanname 3)").
- Getallen bij de formules: halfwaardetijd 4,6 jaar, $5\% + 3\% - 0{,}5\% = 7{,}5\%$, stationaire
  standaarddeviatie 2,7%, $h = 0{,}16$, $0{,}3 \cdot 0{,}22 = 0{,}067$ en $\eta = 2$, $V^* = 2I$.
- Vergelijkende statiek met richting en reden, bij Vasicek (r. 447–449) en bij McDonald-Siegel
  (r. 679–681).

*Aanmerkingen.*
- LSM tegen een binomiale boom: "LSM met drie polynomen ligt binnen één standaardfout van de
  boom. Met minder basisfuncties ligt LSM eronder". Volgens de tabel ligt de waarde met drie
  polynomen (4,4829) juist bóven de boom (4,4779), terwijl de stelling op r. 705–711 en de
  intuïtie (r. 103–104) een ondergrens beloven. De lezer ziet een tegenspraak die de tekst
  niet benoemt.
- Het kernresultaat: "Een positieve $\lambda$ geeft een *term premium* (het verwachte extra
  rendement van een lange obligatie boven een reeks korte): bij $\lambda = 0{,}3$ en 5%
  volatiliteit $0{,}3 \cdot 5\% = 1{,}5$ procentpunt per jaar." Op r. 443 heet het verschil in
  de lange yield ($\lambda\sigma/\kappa$ = 3 pp) ook "de term premium", en op r. 1332 opnieuw
  ("de term premium van 3 procentpunt"). Hier heeft één naam twee grootheden (H7).
- Cox, Ingersoll en Ross: "Een rente die niet negatief kan worden, krijgt een variantie die
  evenredig is met de rente." Oorzaak en gevolg zijn omgedraaid (zie Feitelijke fouten).
- Obligatieprijzen als risiconeutrale verwachting: "Een belegger die zijn geld elke dag tegen
  de korte rente uitzet, weet vooraf niet wat hij over tien jaar heeft, terwijl een obligatie
  een vast bedrag belooft." De zin beantwoordt de vraag ervoor ("Waarom maakt onzekerheid over
  de rente een obligatie duurder?") niet. Dat doet pas de derde zin (H1).
- Zelfde subsectie: "Een termijnstructuurmodel is daarom niets anders dan een keuze voor het
  proces van $i$ onder $\mathbb{Q}$." "Daarom" hangt aan Jensens ongelijkheid, maar de
  bewering volgt uit de prijsformule (H8).
- De affiene klasse: "een soort duration" (r. 351) staat er zonder uitleg; "een
  principale-componentenanalyse op yieldveranderingen vindt één component" (r. 385) is de
  eerste keer en krijgt geen bijzin; "(vergelijking 1 van het artikel)" (r. 692) komt vóór
  het artikel genoemd wordt (r. 721) (H2).

*Beter uitleggen.* Bij LSM ontbreekt waarom een geschatte regel boven de boom kan uitkomen:
de coëfficiënten worden op dezelfde paden geschat als waarop ze worden toegepast, en de
stelling geldt voor vaste coëfficiënten. Bij de termijnpremie ontbreekt het onderscheid
tussen de premie in het verwachte rendement en die in de yield. Voor een oneindig lange
obligatie is $\sigma_p = \sigma/\kappa = 10\%$, zodat beide 3 pp zijn, en die ene zin zou de
twee getallen verbinden.

*Voor een 9.*
- lectures/03_17_termijnstructuur_real_options.md:1192–1195. Eén bijzin: de drie polynomen
  liggen 0,005 boven de boom, binnen één standaardfout, omdat in-sample geschatte coëfficiënten
  licht opwaarts vertekenen. De stelling geldt voor vaste coëfficiënten.
- :316–319, :443, :1332. Noem de 1,5 pp "de premie in het verwachte rendement" en de 3 pp "de
  premie in de lange yield", met de verbindende zin hierboven.
- :458–460. Herstel oorzaak en gevolg (zie Feitelijke fouten).
- :217–222 en :243. De alinea opent met het antwoord (onzekerheid verhoogt de verwachte
  disconteringsfactor, omdat die bol is). Vervang "daarom" door een verwijzing naar de
  prijsformule.
- :351, :385, :692. "Duration" in een bijzin (gemiddelde looptijd, gevoeligheid voor de
  rente), PCA in een bijzin, en "vergelijking 1 van Longstaff en Schwartz" met citatie.

### 2. Opbouw en rode draad (8,5)

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in de eerste alinea. De routekaart zegt dat
  de termijnstructuur de kern is.
- Toy-getallen keren terug: 5% als startrente en $\theta$ (r. 513), 0,114 pp in Theorie
  (r. 242), de driejaarsobligatie in oefening 1.
- "Samengevat" sluit Theorie af en eindigt met de vraag van de simulatie. Lengte 5.552 woorden.

*Aanmerkingen.*
- Intuïtie: "Uit deze vier beelden volgen vier verwachtingen." Er zijn vier verwachtingen over
  drie onderwerpen (curve, mijn, LSM). De mijn en LSM zijn in Theorie aanhangsels, en de
  mijnverwachting wordt ingelost met een verwijzing naar een oefening ("in de koperboom van
  oefening 4 zelfs bijna twee keer zoveel") [onderzoek C, D3].
- Simulatie: "We trekken 2000 steekproeven van 40 jaar uit het model van de theorie". De
  replicatie gebruikt 1971-08 tot 2026-08, dus 55 jaar, en de tekst spreekt daar van "na
  vijftig jaar data" (r. 912) en "na ruim vijftig jaar" (r. 1209). De simulatie kalibreert dus
  niet op de steekproef die ze moet voorspellen (H11).
- Toy en Theorie: "De renteboom was deze formule in drie stappen." (r. 237–238), terwijl het
  toy de regel al aankondigde (r. 133–135). Het recept wordt twee keer verteld [onderzoek C,
  D2].

*Beter uitleggen.* De lezer moet na de intuïtie weten welke verwachting de replicatie toetst.
Nu zijn dat er vier, waarvan twee in een dropdown en in een oefening worden ingelost.

*Voor een 9.*
- lectures/03_17_termijnstructuur_real_options.md:99–104. Twee verwachtingen over de curve
  (lange yield onder of boven $\theta$, perfecte correlatie). Mijn en LSM krijgen elk één
  bijzin zonder eigen verwachting [onderzoek C, D3].
- :745, :753, :768 (480 maanden). Simuleer 660 maanden, of zeg waarom 40 jaar.
- :237–238. Schrap de terugverwijzing of maak er de verwijzing met het toy-getal van, die op
  r. 242 al staat [onderzoek C, D2].

### 3. Taal (8,5)

*Goed.*
- De redactie heeft de sjablonen weggehaald. "Waarom zou dit waar zijn" komt nog één keer
  voor, "In woorden:" twee keer, "zoals de intuïtie voorspelde" één keer en "Wat dit leert"
  één keer. Motiefnamen staan elk hoogstens twee keer, nergens als handelend onderwerp. Er zijn
  drie "Wie"-zinnen.
- Verband met voegwoorden en een gemiddelde zin van 15,9 woorden. De geschiedenisalinea in het
  Overzicht (r. 55–69) leest als een verhaal.
- "zij/haar" voor zaken is overal weg.

*Aanmerkingen.*
- Het kernresultaat: "Een positieve $\lambda$ geeft een *term premium* (het verwachte extra
  rendement van een lange obligatie boven een reeks korte)". Ook op r. 443, 483, 1223 en 1332.
  Zie het oordeel over Engelse vaktermen hieronder [onderzoek C, T:303–305].
- Het kernresultaat: "Itô's lemma uit [](#thm-black-scholes-ito), de kettingregel plus kromming
  maal variantie, geeft". De vaste-termentabel van STYLE §3 schrijft "het lemma van Itô" voor.
- Cox, Ingersoll en Ross: "Een rente die niet negatief kan worden, krijgt een variantie die
  evenredig is met de rente."
- Risico of vergissing: "Wie in 1981 een lange obligatie tegen 15% kocht, droeg in de termen van
  Santa-Clara een risico met een premie, of dacht iets te weten wat de prijs niet wist."
- Wat het voorspelt: "Van de Vasicek-paden zakt 58% minstens één maand onder nul, en 4,7% van
  alle maanden is negatief, met $-6{,}7\%$ als laagste rente." Die alinea (r. 568–572) bevat
  negen getallen, en de alinea op r. 785–788 ("Het 90%-interval van $\hat\kappa$ loopt van 0,10
  tot 0,54 …") ook negen. De regel is hoogstens drie per alinea [onderzoek C, D5].
- Wat er brak: "De modellen verklaren veel, en blijvend." [onderzoek C, T:1174]
- Drie factoren: "De tabel zet de uitkomsten naast de verwachting uit het replicatieblok." De
  zin komt dicht bij regeltaal (het replicatieblok als bron van de verwachting). Dat geldt ook
  voor "Elke verwachting uit het replicatieblok komt uit" (r. 1110).

**Engelse vaktermen, getoetst aan STYLE §3.** De regel luidt dat een vakterm Engels blijft
"als de Nederlandse vertaling gekunsteld is of niemand hem gebruikt".
- *term premium*: **valt niet onder de uitzondering.** "Termijnpremie" is gangbaar Nederlands
  (centrale banken en het CPB gebruiken het), en het sluit aan op de titelterm
  "termijnstructuur". De vaste-termentabel maakt van het parallelle *equity premium*
  "aandelenpremie". Voorstel: "*termijnpremie* (*term premium*: …)" de eerste keer, daarna
  "termijnpremie". 05_28 gebruikt het Engelse woord één keer, dus stem die mee af (H7 over het
  boek).
- *convenience yield*: **mag blijven.** Een Nederlands equivalent ("gemaksrendement") is
  gekunsteld en wordt nauwelijks gebruikt. De eerste keer staat het cursief met uitleg
  (r. 618–619), daarna zonder cursief. Dat is conform §3.
- *short gaan*: **mag blijven.** De tekst geeft eerst de Nederlandse omschrijving, "verkopen
  zonder ze te bezitten (short gaan)" (r. 211), en de alias één keer tussen haakjes. Dat is
  precies H7, en "short gaan" is gewoon Nederlands beursjargon.
- *real options*, *value matching*, *smooth pasting*: mogen blijven, want het zijn namen van
  technieken zonder gangbaar Nederlands equivalent. Ze staan de eerste keer cursief met
  uitleg.
- *level, slope, curvature*: randgeval. Ze staan in kop, tabel en figuur (r. 1023, 1049,
  1067–1085), en "niveau, helling, kromming" is natuurlijk Nederlands. Als factornamen (zoals
  value en size in §3) en in lijn met 05_28 zijn ze te verdedigen. Voeg de Nederlandse namen
  één keer tussen haakjes toe. Geen aftrek.

*Beter uitleggen.* Niet van toepassing.

*Voor een 9.*
- lectures/03_17_termijnstructuur_real_options.md:317, :443, :483, :1223, :1332. Wordt
  "termijnpremie" [onderzoek C, T:303–305].
- :256. Wordt "Het lemma van Itô".
- :458, :1219–1221, :1199. Herschrijven (zie de hardop-toets).
- :568–572 en :785–788. Hoogstens drie getallen per alinea. De rest staat al in de tabel
  erboven [onderzoek C, D5].
- :1089 en :1110. "de verwachting uit het replicatieblok" wordt "wat we vooraf verwachtten".

### 4. Toy-voorbeeld (9)

*Goed.*
- Eén mechanisme (convexiteit in een renteboom), met de hand na te rekenen, en een tabel met
  hand en code die gelijk is (celuitvoer: 0,858001; 0,962001; 0,907771; 0,866668; 4,957; 4,886).
- De slotzin zegt wat het getal betekent (0,114 pp onder de verwachte korte rente), en het getal
  keert terug in Theorie.

*Aanmerkingen.*
- Toy-voorbeeld: "De twee kolommen zijn gelijk, en ze laten het mechanisme in het klein zien."
  Het eerste deel van de zin is overbodig [onderzoek C, D2].

*Beter uitleggen.* Niet van toepassing.

### 5. Code en figuren (9)

*Goed.*
- Elke cel heeft een zin ervoor en erna. Functies lezen als de wiskunde (`roll_back`,
  `simulate_vasicek` met een zichtbare lus, `lsm_put` met benoemde regels voor de uitoefenstap).
- Figuren met leeswijzer vooraf, een bijschrift in hele zinnen en een conclusie erna.
  "Let … op" staat twee keer.

*Aanmerkingen.*
- De curvefiguur: het bijschrift ("In 1981 zet Vasicek de 10-jaarsyield te laag, in 2021 te
  hoog.") en de alinea's erna (r. 1014–1021) zeggen deels hetzelfde [onderzoek C, D4]. Klein.

*Beter uitleggen.* Niet van toepassing.

### 6. Replicatie en empirie (9)

*Goed.*
- Het replicatieblok telt minder dan 250 woorden en noemt bron, wat, data, verschil en verwachte
  afwijking. Tabellen zetten origineel en hier naast elkaar (PCA, LSM), met een verwachtingstabel.
- Beide oordelen beginnen met **Geslaagd.** en verwijzen naar de verwachting. Getallen staan in
  tabellen.

*Aanmerkingen.*
- LSM tegen een binomiale boom: "LSM met drie polynomen ligt binnen één standaardfout van de
  boom." Dat klopt, maar de afwijking gaat de verkeerde kant op (zie helderheid).

*Beter uitleggen.* Zie helderheid, eerste punt.

### 7. Oefeningen (9)

*Goed.*
- Instap op het toy (Amerikaanse put op de obligatie), een afleiding (Vasicek zonder Riccati) en
  een uitbreiding van de replicatie (deelsteekproeven). Oefening 4 draagt de mijn.
- Elke uitwerking eindigt met een slotzin die zegt wat de oefening leert.

*Aanmerkingen.*
- Oefening 1: "Op $t = 1$ levert uitoefenen in de hoge knoop $0{,}87 - 0{,}858001 = 0{,}011999$"
  staat in zes decimalen [onderzoek C, D5].
- Oefening 3: de alinea op r. 1386–1391 bevat meer dan tien getallen.

*Beter uitleggen.* Niet van toepassing.

## Feitelijke fouten

Nagerekend tegen de celuitvoer (`$TEMP/F6-03_17_termijnstructuur_real_options-out.txt`) en met
de hand.

1. **Betekenisverschuiving door de redactie, r. 458–460.** De redactie maakte van "Is de
   variantie evenredig met de rente, dan is de schok bij $i = 0$ nul …" de zin "Een rente die
   niet negatief kan worden, krijgt een variantie die evenredig is met de rente." Als algemene
   bewering is dat onjuist: niet-negativiteit impliceert geen variantie evenredig met $i$. Het
   is de modelkeuze van CIR die de rente niet-negatief maakt. Correctie: "Cox, Ingersoll en
   Ross maken de variantie evenredig met de rente. Bij $i = 0$ is de schok dan nul, terwijl de
   drift $\kappa\theta$ de rente omhoog duwt, zodat de rente niet onder nul zakt."

Geen andere fouten. Correct bevonden: de renteboom en yields; $\log 2/0{,}15 = 4{,}6$; 7,5%; 2,7%;
$h = 0{,}16$; $0{,}3 \cdot 0{,}22 = 0{,}067$; de padsimulatie (0,5758; 0,0465; −0,0674; 7,50% en
5,16%); de simulatie ($\hat\kappa$ 0,0958–0,5364, mediaan 0,241; $\hat\sigma$ 1,43–1,59%; lange
yield 4,16–9,76%); de schattingen (0,1003/0,0608 = 1,65; SE $\theta$ 2,03 pp; Feller 1,03); de curve
($\lambda = 0{,}351$, 8,31%, 115 en 124 bp, −2,32 en +1,79, CIR −1,86 in 2008); PCA (99,9 en 98,9;
89,0/7,7/2,3; 0,69); LSM (4,4779; 3,8443; 4,3299, dus 0,148 onder de boom; 4,4829 met SE 0,0094);
$\eta = 2$; oefening 1 (0,011999; 0,003332; 0,005714; Europese put 0); oefening 2 (0,70 SE; 0,34 en
0,50 pp); oefening 3 (−1,15 en −2,86; 0,76 → 0,56; 2,0% → 0,65%; 0,93 en 0,91); oefening 4 (0,625;
0,140590; 0,461905; 0,274943; 0,134354, factor 1,96). De taalredactie heeft verder geen vakterm
van betekenis veranderd: "hedget/gehedgede", "met een premie" (voor "beprijsd") en "zwakke plek"
(voor "barst") zijn gelijkwaardig.

## Navertelling in vijf zinnen

Omdat de korte rente niet te koop is, waardeert Vasicek obligaties door obligaties tegen elkaar
te hedgen. Daaruit volgt dat alle looptijden hetzelfde overrendement per eenheid risico bieden,
en dat elke prijs één PDE oplost. In de affiene klasse (Vasicek, CIR) geeft dat gesloten
formules, waarin de lange yield gelijk is aan het gemiddelde plus een premie min een
convexiteitseffect, en waarin alle yields perfect samen bewegen. De data weerleggen dat laatste:
drie factoren, een correlatie van 0,69 en fouten van meer dan een procentpunt in 1981 en 2021.
Bovendien is de drift na vijftig jaar nauwelijks gemeten. Hetzelfde argument waardeert een mijn
met sluitoptie en, via LSM, een Amerikaanse put. Dat laatste wijkt niet af van het Overzicht.

## Taal na de redactie

De redactie heeft gewerkt. De tekst leest nu grotendeels als gesproken academisch Nederlands,
met verbanden in plaats van dubbele punten en zonder de terugkerende formules van de vorige
versie. Wat blijft: twee vaste termen (termijnpremie, het lemma van Itô), twee alinea's met te
veel getallen, en een handvol zinnen die de hardop-toets niet halen.

Hardop-toets (drie zinnen die nog niet natuurlijk klinken):

1. r. 458: "Een rente die niet negatief kan worden, krijgt een variantie die evenredig is met de
   rente."
   → "Cox, Ingersoll en Ross maken de variantie evenredig met de rente, zodat de schok bij een
   rente van nul verdwijnt."
2. r. 1219–1221: "Wie in 1981 een lange obligatie tegen 15% kocht, droeg in de termen van
   Santa-Clara een risico met een premie, of dacht iets te weten wat de prijs niet wist."
   → "Wie in 1981 een lange obligatie tegen 15% kocht, kreeg volgens Santa-Clara een vergoeding
   voor risico, of zag iets wat de markt over het hoofd zag."
3. r. 1199: "De modellen verklaren veel, en blijvend."
   → "De modellen verklaren veel, en dat is zo gebleven."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Controle van F6b/R9-1 (`notes/rapport-03_17_termijnstructuur_real_options.md`, sectie
"R9-1") tegen `lectures/03_17_termijnstructuur_real_options.md`. Elk genoemd getal
gecontroleerd tegen de tekst en tegen eerder bevestigde celuitvoer (F6); geen nieuwe
afwijking gevonden.

**Feitelijke fout.**
1. CIR-opener: **opgelost.** Nu "Cox, Ingersoll en Ross maken de variantie evenredig met
   de rente. Bij $i = 0$ is de schok dan nul, terwijl de drift $\kappa\theta$ de rente
   omhoog duwt, zodat de rente niet onder nul zakt." Oorzaak (modelkeuze) en gevolg
   (rente blijft niet-negatief) staan in de juiste volgorde.

**Helderheid (voor een 9).**
2. LSM boven de boom: **opgelost.** "LSM met drie polynomen ligt 0,005 boven de boom,
   binnen één standaardfout, en dat botst niet met [de ondergrens-stelling]. De stelling
   geldt voor vaste coëfficiënten, terwijl LSM de coëfficiënten schat op dezelfde paden
   waarop het ze toepast, zodat de regel een beetje vooruitkijkt en de waarde licht naar
   boven vertekent." Getal klopt: 4,4829 − 4,4779 = 0,0050 (beide cijfers al bevestigd
   in F6).
3. Twee premies: **opgelost.** 1,5 pp heet nu "premie in het verwachte rendement" (r.
   318), 3 pp "termijnpremie in de lange yield" (r. 446–452, herhaald r. 1349), met de
   verbindende zin ($\sigma_p = \sigma/\kappa = 10\%$, dan vallen ze samen). Consistent
   op alle vindplaatsen.
4. Obligatieprijzen: **opgelost.** De alinea opent nu met het antwoord ("Een obligatie
   kost de verwachte discontering van één euro …"), en "daarom" is vervangen door "Uit
   [de prijsformule] volgt ook dat …".
5. Duration/PCA/citatie: **opgelost.** "een soort *duration* (de procentuele
   prijsdaling per procentpunt rentestijging)"; PCA met bijzin; "vergelijking 1 van
   {cite:t}`LongstaffSchwartz2001`".

**Opbouw (voor een 9).**
6. Intuïtie-verwachtingen: **opgelost.** Twee verwachtingen over de curve; mijn en LSM
   staan als toepassingen zonder eigen verwachting.
7. Simulatie 40 vs. 55 jaar: **opgelost, met de alternatieve oplossing die het punt zelf
   aanbood** ("of zeg in één zin waarom het 40 jaar is"). Niet omgezet naar 660 maanden
   (zou de `rng`-stroom van LSM en oefening 2 veranderen), maar een zin zegt dat de
   replicatie 55 jaar heeft en dat de $t$-waarde van $\hat\kappa$ daar toont dat de drift
   ook dan slecht gemeten blijft.
8. Terugverwijzing renteboom: **opgelost.** "De renteboom was deze formule …" komt niet
   meer voor.

**Taal (voor een 9).**
9. Termijnpremie: **opgelost** op alle vindplaatsen (r. 316 eerste keer met *term
   premium* tussen haakjes, daarna Nederlands, ook r. 1349).
10. "Het lemma van Itô": **opgelost.**
11. Hardop-toets (CIR, Santa-Clara, "blijvend"): **opgelost**, alle drie zinnen
    herschreven zoals voorgesteld.
12. Getallen per alinea (paden- en schattingsalinea): **opgelost.** De padenalinea is
    gesplitst in twee kortere alinea's; de schattingsalinea vergelijkt relatief in plaats
    van de kwantielen op te sommen (die staan al in de tabel erboven).
13. "Verwachting uit het replicatieblok" → "wat we vooraf verwachtten": **opgelost.**
14. Level/slope/curvature: Nederlandse namen (niveau, helling, kromming) één keer tussen
    haakjes toegevoegd; stond al op "geen aftrek", dus geen plafondpunt, maar netjes
    meegenomen.

**Niet gedaan of verslechterd.** Geen. Geen nieuw feitelijk punt gevonden: 5,2% (CIR) en
7,5% (Vasicek) voor de oneindig lange yield sluiten aan bij de al bevestigde padentabel
(0,0516/0,0750), en 4,4829 − 4,4779 = 0,0050 is de juiste aftrekking.

## Eindcijfer: 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 9,0. Laagste deelcijfer 9. De eis van ronde 9+ (≥ 9,0, geen deelcijfer onder
8,5) is **gehaald**. Taal blokkeert niet. Alle punten uit F6 (feitelijke fout, drie
verbeteringen, "Voor een 9" en de hardop-toets) zijn opgelost, zoals de eindbeoordelaar
al in het vooruitzicht stelde ("Bij volledige oplossing van alle punten: 9,0").
