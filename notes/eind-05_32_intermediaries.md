STATUS 05_32_intermediaries F6c words=5373 prose=PASS open=1 cijfer=9,0 min=8,9

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

# Eerste herziening (workflow §12)

Eindbeoordeling F6 van `lectures/05_32_intermediaries.md` (verse ogen, na F1, F23 en F4T).
Celuitvoer nagerekend via `tools/nb_outputs.py` (19 cellen). `prose_stats --check`: PASS
(5089 woorden, zinsgemiddelde 17,1, geen zin > 40, alinea-gemiddelde 48).

## De drie verbeteringen met het meeste effect

1. **Twee stille betekenisverschuivingen in de symbolen oplossen (helderheid 8,5 → 9,0).**
   (a) $\varepsilon$ is in het toy een vraagelasticiteit (impact $S/(\varepsilon W)$), in het
   Brunnermeier-Pedersen-model een vraaghelling (impact $(z-x)/\varepsilon$); "net als in het
   toy-voorbeeld" (05_32_intermediaries.md:229–231) verdoezelt dat de BP-$\varepsilon$ de toy-$\varepsilon W$
   is. (b) In "Wat het voorspelt" wordt $\eta$ ongemerkt van $E/A$ het *aandeel van de
   intermediair in het totale vermogen* (regel 543–546); één bijzin ("omdat de intermediair alle
   activa houdt, is zijn eigen vermogen gedeeld door de activa ook zijn aandeel in het totale
   vermogen") is nodig. Daarnaast het vertrekpunt 0,4 noemen in "Halveert de kapitaalratio tot
   $\eta = 0{,}2$" (regel 532) en zeggen waarom $z = 7$ drie evenwichten heeft terwijl
   voorwaarde 3 van de propositie daar niet geldt ($z x_0/\varepsilon = 0{,}93 < K_0$; de
   margespiraal met $\theta = 2$ maakt het verschil; regel 252 en 317).
2. **Replicatietabel en oordeel methodisch zuiver maken (replicatie 8,5 → 9,0; oefeningen
   8,5 → 9,0 samen met de oefening-3-conclusie).** De rij "$\lambda_\eta$ op alle testactiva"
   (regel 933) zet de GMM-schatting van HKM ($t = 2{,}56$) naast onze *tweestaps*-schatting (3,44,
   Shanken-$t$ 1,94), terwijl de eigen GMM-schatting (4,94, $t = 2{,}44$, cel 14) de vergelijkbare
   is. De AEM-prijs van risico (62% per jaar in het origineel; hier 8,8% per kwartaal, cel 14)
   staat nergens in tabel of tekst, hoewel de admonition een positief teken als verwachting
   noemt. Het oordeel (regel 937) koppelt niet expliciet aan de verwachte lagere $t$.
3. **Taal- en figuurresten wegwerken (taal 8,5 → 9,0; code en figuren 8,5 → 9,0).** De drie
   hardop-zinnen hieronder herschrijven; Engels in figuurtekst ("intermediary-risico" regel 667,
   "Credit-" regel 739, FRED-codes BAA10Y/TEDRATE als legenda regel 738); de compacte
   set-comprehension voor de nulpunten (regel 299–301) uitschrijven, zodat de uitvoer geen
   `np.float64(...)` meer toont (cel 3).

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 8,5 |
| | **Gewogen eindcijfer** | | **8,7** (8,65) |

Taal ≥ 8, dus geen blokkade. De ondergrens (geen deelcijfer onder 8,5) is gehaald, het
eindcijfer van 9,0 niet.

### 1. Helderheid (8,5)

*Goed.*
- Toy-voorbeeld: elke stap heeft een getal, en stap 4 legt met $(1-h)/h = 9$ en $80 \times
  9/2000 = 0{,}36$ uit waarom de spiraal convergeert; die 0,36 keert terug in de multiplier
  (Marktliquiditeit en financieringsliquiditeit, regel 273–275).
- Kapitaalratio en risicopremie: bewijs in drie zinnen, met direct het getal $5{,}8\%$ bij
  $\eta = 0{,}5$ en de richting van $\gamma$ met reden.
- Wat het voorspelt: de puzzel "leverage is het omgekeerde van de kapitaalratio en toch
  krijgen beide een positieve prijs" wordt benoemd en met twee concrete meetverschillen opgelost.

*Aanmerkingen.*
- Marktliquiditeit en financieringsliquiditeit: "Speculanten kopen $x \ge 0$ en buitenstaanders
  met vraaghelling $\varepsilon$ nemen de rest, zodat de prijskorting $\Delta = v - p = (z -
  x)/\varepsilon$ is, net als in het toy-voorbeeld." Zelfde symbool, andere betekenis dan de
  "vraagelasticiteit" $\varepsilon = 2$ uit de toy-tabel (H2, H7).
- Wat het voorspelt: "Omdat zijn vermogen het totale vermogen maal zijn aandeel daarin is,
  krijgen een daling van het totale vermogen en een daling van dat aandeel elk een eigen
  beloning." Het "aandeel" is hier $\eta$, eerder gedefinieerd als $E/A$; de brug ontbreekt.
- Numerieke oplossing: "Halveert de kapitaalratio tot $\eta = 0{,}2$, dan stijgt de premie van
  7,6% naar 27,1%" — het vertrekpunt 0,4 staat er niet, en Samengevat noemt 5,8% bij 0,5.
- Figuur `fig-intermediaries-bp`: "Bij $z = 7$ en $z = 10$ liggen een liquide en een illiquide
  evenwicht naast elkaar" — bij $z = 7$ geldt voorwaarde 3 van de propositie niet, en het
  illiquide evenwicht is 0,11 in plaats van $z/\varepsilon = 0{,}117$ (cel 3).
- Broker-dealer-leverage: "Het zijn verschillende metingen van hetzelfde begrip, en daardoor
  bijna onafhankelijke factoren." Het "daardoor" is geen oorzaak; verschillende metingen van
  hetzelfde begrip zouden juist gecorreleerd moeten zijn (H1, H8).
- Overzicht: "schokken in hun kapitaalratio krijgen een positieve prijs, al is die slecht
  gemeten." "die" kan de prijs of de kapitaalratio zijn (H8).
- "Haircut" (toy, Intuïtie) en "marge" (BP-model, Samengevat) voor hetzelfde $h$, zonder
  alias tussen haakjes (H7).

*Beter uitleggen.* De vertaling van toy naar BP-model: welke toy-grootheid is $x_0$ en welke
$\varepsilon$ (dan klopt ook $G' = x_0/(\varepsilon h) = 80/(2000 \times 0{,}1) = 0{,}4$ tegen 0,36
en ziet de lezer waar het verschil $(1-h)$ vandaan komt). En waarom $\eta = E/A$ in HKM ook
het vermogensaandeel is.

*Voor een 9.* 05_32_intermediaries.md:229–231 (ε), :543–546 (η als aandeel), :532 (vanaf 0,4),
:317 (z = 7), :804–805 (daardoor), :31–33 (die).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Overzicht stelt de vraag en geeft een voorzichtig ja met de twee kernbeweringen; routekaart
  aan het begin van Theorie (regel 198–203) en Samengevat aan het eind.
- De intuïtie voorspelt "sneller dan evenredig" en "positieve prijs in aandelen en obligaties
  tegelijk"; de eerste wordt ingelost bij regel 532–535, de tweede bij regel 567–569.
- De toy-getallen (haircut 10%, opname 2000, 0,36) keren terug in de multiplier en in de
  fire-sale-dropdown; de simulatie kalibreert op de HKM-bèta's en -prijzen die de replicatie
  toetst. 5089 woorden.

*Aanmerkingen.*
- Intuïtie: "geldt dat teken in aandelen en obligaties tegelijk." De replicatie toetst
  obligaties nooit apart; ze zitten alleen in de gemengde testset, zodat de tweede voorspelling
  empirisch niet expliciet wordt ingelost.

*Beter uitleggen.* Eén zin in De cross-sectie over het teken van de prijs op de vijf
obligatieportefeuilles, of de voorspelling in de Intuïtie beperken tot "in elke activaklasse
dezelfde prijs".

### 3. Taal (8,5)

*Goed.* Zinslengte en afwisseling op orde (gem. 17,1), geen dubbele punten als lijm, geen
telegramzinnen; motiefnamen elk één keer, twee "Wie"-zinnen. Vaktermen zijn door de redactie
niet van betekenis veranderd (leverage, kapitaalratio, boek- en marktleverage, haircut, SDF
gecontroleerd tegen de definities en de code).

*Aanmerkingen.*
- Numerieke oplossing: "Het deel dat sneller groeit, komt uit de volatiliteit, want die stijgt
  zelf als de kapitaalratio daalt."
- Wat er brak: "In onze data krijgt het model in elk geval op het teken gelijk." (de redactie
  meldt deze calque als herschreven, maar de wending staat er nog).
- Broker-dealer-leverage: "Het zijn verschillende metingen van hetzelfde begrip, en daardoor
  bijna onafhankelijke factoren."
- Marktliquiditeit: "... wordt de eerste impact ongeveer anderhalf keer zo groot, en zo werd de
  eerste prijsdaling van 0,9% in het toy-voorbeeld in totaal 1,35 procentpunt." Twee keer
  "toy-voorbeeld" in één zin en "werd ... in totaal 1,35 procentpunt" klinkt geknipt.
- Figuurtekst: "intermediary-risico" (regel 667) naast "intermediairrisico" in de proza;
  "Credit- en financieringsspreads" (regel 739).

*Beter uitleggen.* Geen inhoudelijk punt.

*Voor een 9.* 05_32_intermediaries.md:442, :1033–1034, :804–805, :273–275, :667, :739.

### 4. Toy-voorbeeld (9,0)

*Goed.* Met de hand na te rekenen, één geleende formule (prijsimpact) expliciet als zodanig
aangekondigd, tabel hand/code met zeven identieke regels (cel 2), en een slotzin met betekenis
(1,35 procentpunt extra, 31% eigen vermogen weg). De tegenstelling kapitaalratio/leverage wordt
hier al gezaaid.

*Aanmerkingen.*
- Toy-voorbeeld, stap 5: "en de tweede verkoop $62{,}91 - 55{,}30 = 7{,}62$." Met de getoonde
  afrondingen is het verschil 7,61; de 7,62 komt uit de onafgeronde 7,616.
- Stap 5 voegt een tweede mechanisme (margespiraal) toe binnen het toy; verdedigbaar, maar het
  maakt het toy zwaarder dan "één mechanisme".

*Beter uitleggen.* De afronding in stap 5 consistent maken (drie decimalen, of 7,61).

### 5. Code en figuren (8,5)

*Goed.* Elke cel heeft een zin ervoor en erna; `deleverage` en `fire_sale` lezen als het
proces (zichtbare lus per ronde); figuurbijschriften zeggen wat te zien is.

*Aanmerkingen.*
- Marktliquiditeit, cel `cel-intermediaries-bp`: `roots = sorted(set([0.0] if gap[0] == 0 else
  []) | set(np.round(roots, 6)))` is een compacte truc, en de uitvoer toont
  "`[0.0, np.float64(0.033333), np.float64(0.11)]`".
- Simulatie, figuurtitel: "Kans op een significante prijs van intermediary-risico in 50 jaar
  kwartaaldata".
- De kapitaalratio in de tijd: legenda "BAA10Y" en "TEDRATE" als ruwe FRED-codes.
- De cross-sectie: `gmm_sdf` bouwt matrices `d` en `a` zonder uitleg in tekst of commentaar;
  de één-regel-definitie van `bond_returns` (regel 829) is moeilijk te lezen.

*Beter uitleggen.* Eén commentaarregel bij `d` en `a` (Jacobiaan en selectiematrix van de
momentvoorwaarden) en de houdrendementformule in woorden vóór de cel.

*Voor een 9.* 05_32_intermediaries.md:299–304, :667, :738–739, :829, :889–890.

### 6. Replicatie en empirie (8,5)

*Goed.* Drie admonitions met bron, wat, data, verschil en verwachte afwijking binnen de
lengte; tabel origineel/hier; het dieptepunt 2,23% in februari 2009 en $\lambda_\eta$ op FF25 met
GMM 6,96 tegen 7 zijn overtuigend; de voorspelbaarheid wordt eerlijk als niet significant
gerapporteerd.

*Aanmerkingen.*
- Tabel: "$\lambda_\eta$ op alle testactiva, 1970–2012 (% per kwartaal) | 9 ($t = 2{,}56$) |
  3,44 (Shanken-$t$ 1,94)" — origineel is GMM, hier tweestaps; de GMM-schatting hier is 4,94
  ($t = 2{,}44$, cel 14).
- Broker-dealer-leverage, admonition: "de prijs van leverage-risico moet positief zijn" — de
  AEM-$\lambda$ (4,76 tot 10,34% per kwartaal, cel 14) staat niet in tekst of tabel, en de
  vergelijking met 62% per jaar ontbreekt.
- De cross-sectie: "De replicatie is gedeeltelijk geslaagd, want het dieptepunt ligt waar het
  moet liggen en het teken is overal positief." Het oordeel verwijst niet naar de verwachte
  lagere $t$.

*Beter uitleggen.* Dat de obligaties uit een geschatte curve komen en zes activaklassen
ontbreken, verklaart het lagere niveau bij "alle testactiva"; dat verband staat in de
admonition maar niet bij het oordeel.

*Voor een 9.* 05_32_intermediaries.md:933 (GMM naast GMM), :935 (rij AEM-$\lambda$ toevoegen),
:937–941 (oordeel koppelen aan verwachte afwijking).

### 7. Oefeningen (8,5)

*Goed.* Instap op het toy (oefening 1), afleiding met multiplier en eindige differentie
(oefening 2), uitbreiding van de replicatie (oefening 3); elke uitwerking eindigt met een les.

*Aanmerkingen.*
- Oefening 3, uitwerking: "Het resultaat hangt dus niet af van 2008, maar wel van de testactiva
  en de methode." Cel 19 laat zien dat de tweestapsschatting op FF25 van 10,57 (1970–2006) naar
  2,62 (1970–2025) zakt en met momentum van 9,08 naar 0,22; de conclusie volgt niet uit de
  tabel (zie Feitelijke fouten).
- Oefening 2(2): de rij $x_0 = 8$ (multiplier $1/60$, hoekevenwicht) krijgt geen woord, terwijl
  de vraag bij $x_0 = 8$ begint.

*Voor een 9.* 05_32_intermediaries.md:1160 (conclusie herschrijven: het teken blijft, het niveau
hangt af van de periode na 2006, de testactiva en de methode), :1132 (één zin over $x_0 = 8$).

## Feitelijke fouten (nagerekend tegen de celuitvoer)

1. **05_32_intermediaries.md:1160** — "Het resultaat hangt dus niet af van 2008". Cel 19:
   $\lambda$ tweestaps FF25 10,57 → 2,62, FF25+momentum 9,08 → 0,22; GMM 8,82 → 5,68 en 9,21 →
   4,79. Het resultaat hangt sterk af van de periode na 2006; alleen het teken is robuust.
2. **05_32_intermediaries.md:395** — "zit er dus een orde van grootte naast". Cel 4: 0,1% tegen
   12,4% is een factor ruim honderd, twee ordes van grootte (tegen de vaste haircut, 4,7%, nog
   steeds een factor 47).
3. **05_32_intermediaries.md:138** — "$62{,}91 - 55{,}30 = 7{,}62$" is met de getoonde getallen
   7,61 (afrondingsinconsistentie; cel 2 geeft 7,616).

Verder nagerekend en juist: toy (3,347%, 1,35 pp, 31%, 4,12%, leverage 8), BP-evenwichten en
12,5, fire sale (0,1% → 12%; 1,03 en 1,68), HK-premie 5,8%, 7,6% → 27,1%, $\eta_{\text{krit}} =
0{,}198$, simulatie (10%, 50%, 28%/ruim een kwart), kapitaalratio 2,23% feb 2009, 8,2% → 4,1%,
correlaties −0,33/−0,14/0,06/0,76, boekleverage 47,0 → 22,6, marktleverage 22 → 38 → 19,8,
factoren −0,35/−0,44, tabel cross-sectie, voorspelbaarheid (4,1 pp, −1,36, −1,43), oefening 1
(1,67 → 1,58; 4,62; 54%) en oefening 2 (0,2167; 0,0222; 0,625; 0,044; 16,5%; 4,8). Geen vakterm
van betekenis veranderd.

## Navertelling in vijf zinnen

1. In 2008 zaten de verliezen bij gehefboomde dealers, en een intermediair aan zijn
   financieringsgrens versterkt een prijsdaling doordat verlies en hogere haircuts tot
   gedwongen verkopen leiden.
2. Omdat markt- en financieringsliquiditeit elkaar versterken, kan dezelfde markt liquide of
   illiquide zijn, met een multiplier die groeit met de bestaande positie en de margegevoeligheid.
3. Als alleen intermediairs het risico kunnen dragen, is de premie omgekeerd evenredig met hun
   kapitaalratio, en doordat de volatiliteit meestijgt, groeit ze sneller dan evenredig tot aan
   een crashpunt.
4. Het marginale nut van de intermediair geeft een factormodel met een positieve prijs voor
   schokken in de kapitaalratio, en de data geven dat teken, al is de schatting afhankelijk van
   testactiva en methode en ziet een tweestapstoets zelfs een nutteloze factor vaak als significant.
5. Het model verklaart de mechaniek van 2008 goed, maar loopt vast op de meting: leverage en
   kapitaalratio krijgen beide een positieve prijs, zijn bijna ongecorreleerd, en de HKM-factor
   lijkt sterk op het marktrendement.

Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft goed werk gedaan: het college leest grotendeels als gesproken academisch
Nederlands, met voegwoorden in plaats van knippen en zonder sjabloonzinnen. Eén gemelde
herschrijving is niet doorgekomen. Hardop-toets, drie zinnen met herschrijving:

1. Regel 442: "Het deel dat sneller groeit, komt uit de volatiliteit, want die stijgt zelf als
   de kapitaalratio daalt." → "Dat de premie sneller dan evenredig groeit, komt door de
   volatiliteit, die zelf stijgt als de kapitaalratio daalt."
2. Regel 1033–1034: "In onze data krijgt het model in elk geval op het teken gelijk." → "In
   onze data heeft het model in elk geval het teken goed."
3. Regel 804–805: "Het zijn verschillende metingen van hetzelfde begrip, en daardoor bijna
   onafhankelijke factoren." → "Ze meten hetzelfde begrip op een andere manier, en als factoren
   zijn ze toch bijna onafhankelijk."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Getallencontrole: alle door de schrijver toegevoegde of gewijzigde getallen herleid tegen `nb_outputs` (cellen 2, 3, 4, 14, 19) of tegen een berekening uit getallen in de tekst: GMM 4,94 ($t$ 2,44), 6,96 ($t$ 3,10), AEM 8,79 (Shanken-$t$ 2,08) en $R^2$ 0,41, 4,98/1,61, 0,22 tegen 0,85; 7,61; 0,11 in cel 3; $7 \times 8/60 = 0{,}93$; 0,4 tegen 0,36 via $(1-h)/h$; twee ordes van grootte (0,1% naar 12%); oefening 3 (10,57 naar 2,62; 0,22; GMM 4,79 tot 5,68). Geen niet-herleidbaar getal. `prose_stats --check`: PASS (5373 woorden, zinsgemiddelde 17,5, geen zin > 40).

Per punt uit de beoordeling:
- Feitelijke fout 1 (oefening 3, "niet af van 2008"): opgelost; het teken blijft, het niveau hangt af van de jaren na 2006, testactiva en methode.
- Feitelijke fout 2 (orde van grootte): opgelost, "twee ordes van grootte".
- Feitelijke fout 3 (7,62): opgelost, 7,61.
- Verbetering 1a ($\varepsilon$): opgelost, vraaghelling is het toy-$\varepsilon W = 2000$, met de vertaling $x_0 = 80$ en 0,4 tegen 0,36.
- Verbetering 1b ($\eta$ als aandeel): opgelost, bijzin bij de HKM-SDF. Vertrekpunt 0,4: opgelost. $z = 7$: opgelost, bijschrift zegt dat voorwaarde 3 voldoende is en niet nodig, met de margespiraal als reden.
- Verbetering 2 (replicatietabel): grotendeels opgelost. De rij is nu GMM naast GMM, de AEM-rij staat erin en het oordeel koppelt aan de verwachte afwijking. Deels: 62% per jaar staat naast 8,79% per kwartaal zonder omrekening.
- Verbetering 3 (taal en figuren): opgelost; de drie hardop-zinnen, "intermediairrisico", Baa- en TED-spread, "Krediet-" en de nulpunten-lus zijn herschreven. `gmm_sdf` heeft commentaar bij `d` en `a`, en de houdrendementformule staat in woorden.
- Aanmerking opbouw (obligaties niet apart getoetst): opgelost, Intuïtie beperkt en het oordeel benoemt het.
- Overzicht "die", haircut/marge-alias, oefening 2(2) ($x_0 = 8$): opgelost. Toy stap 5 als tweede mechanisme: door de beoordelaar zelf verdedigbaar genoemd, geen aftrek.
- Verslechtering of nieuwe feitelijke fout: geen.

Hardop-toets opnieuw (drie alinea's: Numerieke oplossing, Broker-dealer-leverage, Wat er brak): de herschreven zinnen lezen natuurlijk. Open: één klein punt, de eenheid van de AEM-vergelijking.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,9 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Gewogen eindcijfer** | | **9,0** (8,99) |

Taal ≥ 8, geen blokkade; geen deelcijfer onder 8,5. Binnen de plafonds van de beoordelaar (9,0 per criterium, 9,1 bij volledige oplossing).
