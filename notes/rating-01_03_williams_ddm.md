# Beoordeling: 01_03_williams_ddm — Williams en het dividend discount model

Maatstaf: `plannen/rubriek-didactiek.md`. Lezer: eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft.

## Eindcijfer: 7,2

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 6 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 7 |
| 7 | Oefeningen | 5% | 8 |

Gewogen: 0,3·6 + 0,2·8 + 0,15·7 + 0,1·8 + 0,1·8 + 0,1·7 + 0,05·8 = 7,15 → 7,2.
Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

---

## 1. Helderheid van de uitleg — 6

**Goed**
- *Wat het voorspelt: het Gordon-groeimodel*: de gevoeligheidstabel met vier
  uitgerekende gevallen en de zin "Een fout van één procentpunt in $r$ of $g$ is
  een fout van twintig procent in dat verschil".
- *Het kernresultaat*: de rationele bel krijgt een getal ("Bij $r = 10\%$
  verdubbelt de bel in ruim zeven jaar, terwijl een dividend dat met 5% groeit
  daar veertien jaar over doet").
- *Van de definitie van rendement naar de contante waarde*: de wet van iteratieve
  verwachtingen wordt in één zin herhaald ("wat we vandaag verwachten dat we
  morgen zullen verwachten, verwachten we vandaag al").

**Aanmerkingen**
- *Replicatie*: "Eén log-punt hogere prijs-dividend-ratio gaat samen met
  anderhalve tiende procentpunt extra groei per jaar." Een coëfficiënt van 0,015
  op een jaargroei in decimalen is 1,5 procentpunt per jaar, niet 0,15. De
  volgende zin ("Over tien jaar is dat samen nog geen 0,15 log-punt") en de
  rendementszin ("bijna vier procentpunt per jaar") rekenen wel met de juiste
  schaal. Een lezer die narekent, raakt hier het spoor kwijt.
- *Opzet en aannames*: "Zoals overal in de reeks is $R$ bruto en $r$ netto".
  [](#01-02-bachelier) schreef juist "*Vanaf hier zijn kleine letters logs*:
  $p_t = \log P_t$", en gebruikte $r$ voor het logrendement. Hier zijn $p_t$ en
  $d_t$ niveaus en is $r$ de discontovoet. De notatiewissel wordt niet benoemd.
- *Simulatie*: "Die onzekerheid heet in deze reeks de standaardfout van 2%
  ([](#01-02-bachelier) mat haar al)." Het resultaat werd afgeleid in
  [](#00-01-rendementen).
- *Simulatie*: $g$ en $r$ worden gekalibreerd op *log*-gemiddelden (1,61% en
  6,82%) en in de Gordon-formule gezet, die simpele verwachte groei en rendement
  vraagt. Na [](#00-01-rendementen) weet de lezer dat dat een halve variantie
  scheelt (bij rendement ongeveer 1,6 procentpunt); de lecture zegt er niets over.
- *Het kernresultaat*, warning: "de decompositie van Campbell en Shiller verderop
  in deze lecture rusten er allebei op." De decompositie komt niet in deze
  lecture; *Hoe het getoetst wordt* verwijst haar naar [](#04-20-voorspelbaarheid).
- *Toy-voorbeeld*: "Bij deze discontovoet en groeivoet ligt het zwaartepunt van een
  aandelenwaardering twintig tot dertig jaar in de toekomst." Getal zonder
  berekening.
- *Simulatie*: "Een analist met een gunstige steekproef zit niet 25% maar 100% te
  hoog." Waar 25% vandaan komt, staat nergens.
- *PVGO*: "Wat rekenwerk geeft $\mathrm{PVGO} = \dots$" — de tussenstap ontbreekt.
- *Hoe het getoetst wordt*: "Blijkt de dividendgroei onvoorspelbaar, dan moet
  volgens de boekhoudkundige identiteit het *rendement* voorspelbaar zijn." De
  kernstap van de lecture rust op een identiteit in gerealiseerde rendementen; de
  zin die dat naar verwachtingen vertaalt, ontbreekt.

**Beter uitleggen**
- De dividendcoëfficiënt als "1,5 procentpunt per jaar" lezen.
- Eén zin bij de *Opzet* die de notatie ten opzichte van [](#01-02-bachelier)
  vastlegt (hier: kleine letters zijn niveaus, $r$ is de discontovoet).
- Eén zin bij de kalibratie dat log-gemiddelden de ware $r - g$ onderschatten,
  of kalibreren op rekenkundige gemiddelden.
- Het zwaartepunt: de gewogen gemiddelde looptijd $(1+r)/(r-g) = 22$ jaar
  uitrekenen.
- Waar 25% vandaan komt: het spiegelbeeld van −33% aan de onderkant, of die zin
  vervangen door de percentielen (13 en 40 rond 19,5).

## 2. Opbouw en rode draad — 8

**Goed**
- De voorspelling uit *Intuïtie* ("Een hoge prijs-dividend-ratio ... moet dan
  gevolgd worden door snel stijgende dividenden") wordt in de theorie afgeleid en
  in de replicatie getoetst en verworpen. Voorspelling, theorie en toets vormen
  één lijn.
- Dezelfde getallen lopen door: de toy ($r = 10\%$, $g = 5\%$) komt terug in de
  gevoeligheidstabel, en de simulatie merkt op dat haar $r - g = 5{,}2$ "bijna de
  5 procentpunt van het toy-voorbeeld" is.
- Het onderscheid boekhoudkundige identiteit / model van Williams wordt in het
  *Overzicht* aangekondigd, in de theorie gemaakt en in *Wat er brak* gebruikt.

**Aanmerkingen**
- Het *Samengevat*-blok staat aan het eind van *Theorie*, niet aan het eind van
  de lecture.
- *PVGO*: "Deze subsectie is een zijstap ... Simulatie en replicatie gebruiken
  haar niet." Eerlijk gemarkeerd, maar een zijstap midden in de theorie.
- De simulatie (onzekerheid in $g$) en de replicatie (variatie in $r$) beantwoorden
  verschillende vragen; de overgang tussen de twee wordt niet gemaakt.
- *Hoe het getoetst wordt*: de alinea over Campbell en Shiller introduceert $\rho
  \approx 0{,}96$ en een variantiedecompositie die de lecture daarna niet
  gebruikt.
- De Gordon- en transversaliteitssecties openen met "*Waarom zou dit waar zijn?*"
  in plaats van met hun conclusie.

**Beter uitleggen**
- Eén zin na de simulatie die zegt dat de replicatie de andere onbekende, $r$,
  bekijkt.

## 3. Taal — 7

**Goed**
- Eén naam per begrip, expliciet vastgelegd: "we noemen hem verder alleen de
  discontovoet"; "boekhoudkundige identiteit" en "model van Williams" worden
  consequent gescheiden.
- Sterke korte zinnen: "Waarderen met dit model is delen door een klein getal dat
  niemand kent."
- Engelse termen krijgen een Nederlandse glossering (*rational bubble*,
  *retention ratio*, PVGO, CAPE).

**Aanmerkingen**
- *Waar we zijn*: "Bachelier, Cowles (adviseurs verslaan de markt niet) en Kendall
  (weekkoersen zonder patroon) wisten dat de koers van morgen niet uit die van
  vandaag volgt, maar niet waarom de koers van vandaag is wat hij is." Stapelzin
  met twee tussenzinnen.
- *Waar we zijn*: "De barst die het tijdvak achterliet, is dus een gat" en
  *Intuïtie*: "Williams zag het gat en liep eromheen." Projectjargon (barst/gat).
- *PVGO*: "Wat rekenwerk geeft" — calque van "some algebra gives".
- *Replicatie*: "Eén log-punt hogere prijs-dividend-ratio gaat samen met
  anderhalve tiende procentpunt extra groei per jaar." Ook los van de rekenfout
  een moeilijke zin.
- *Replicatie*: "Neem dat verschil niet te serieus." Spreektaal.

**Beter uitleggen**
- De barst/gat-metafoor vervangen door wat bedoeld wordt ("een theorie van
  koersveranderingen, geen theorie van het koersniveau").

## 4. Toy-voorbeeld — 8

**Goed**
- Met de hand na te rekenen in vijf minuten, met een slim gekozen groei gelijk
  aan de discontovoet ("elke term gelijk aan één").
- Eén mechanisme (verdisconteren met eindwaarde) en precies één nog niet afgeleide
  formule ($d/(r-g)$), expliciet als recept aangekondigd.
- Tabel hand/code met negen regels.

**Aanmerkingen**
- De slotzin is een zin over de code ("De twee kolommen zijn gelijk, dus de code
  doet wat de handberekening doet"), niet over wat de lezer nu weet. De les
  (87,5% zit na jaar 3) staat er wel, maar zonder "wat de lezer nu weet".
- De toy eindigt met een onbewezen getal ("twintig tot dertig jaar", zie criterium 1).

**Beter uitleggen**
- Eén zin: "Wie dit narekent, weet nu dat de prijs vooral uit de eindwaarde komt,
  en dat die van $r - g$ afhangt."

## 5. Code en figuren — 8

**Goed**
- De toy-cel leest als de wiskunde, met commentaar per regel (`# d_4`,
  `# eindwaarde op t = 3 (het recept)`).
- Het Gordon-rooster is een zichtbare dubbele lus.
- Vóór de figuren staat een leeswijzer ("Let links op de lange staart naar rechts,
  en rechts op hoe steil de hyperbool wordt"; "Let op de helling in het rechter
  paneel"), erna een bijschrift en een zin.

**Aanmerkingen**
- *Oefening 1*: `kruispunt = next(t for t in range(200) if ...)` — compacte truc.
- *Replicatie*, figuurcel: `b, a = np.polyfit(...)` overschrijft de $b$ uit de
  PVGO-sectie (en in de tekst is $b$ al tweemaal bezet).
- *Simulatie*: de figuurcel trekt nieuwe steekproeven in plaats van de $T = 50$
  uit de tabel te hergebruiken; de histogram hoort dus bij andere getallen dan de
  tabel erboven.
- Variabelenamen wisselen tussen Nederlands en Engels (`kalibratie`,
  `resultaten`, `kolom` naast `rows`, `growth`, `finite`).

**Beter uitleggen**
- De `next(...)`-regel als gewone lus met `break` schrijven.

## 6. Replicatie en empirie — 7

**Goed**
- Blok met bron, wat, data, verschil en verwachte afwijking, onder 250 woorden,
  inclusief een verwachte $R^2$ ("rond tien procent") die de uitkomst (0,12) haalt.
- Tabel "onder constante $r$ (Williams)" / "hier".
- Eerlijke waarschuwing over overlap en Stambaugh-bias met een getal
  ("ongeveer veertien onafhankelijke stukken data").

**Aanmerkingen**
- "**Niet geslaagd** voor Williams' lezing, en wel zoals het replicatieblok
  verwachtte". Het oordeel gaat over het model, niet over de replicatie; de
  lezer weet niet of de replicatie gelukt is. Het blok zelf formuleert geen
  verwachting maar een beslisregel ("Het teken beslist ... Draait dat om, dan
  ...").
- *Replicatie*: de rekenfout "anderhalve tiende procentpunt" (zie criterium 1)
  zit in de interpretatie van het hoofdresultaat.
- *CAPE*: "de coëfficiënt is $-0{,}059$ met een $t$-waarde van $-4{,}5$ en een
  $R^2$ van 0,24" — herhaalt de tabel in proza; "De steekproef begint pas in
  1881" staat niet in de tabel.

**Beter uitleggen**
- Het oordeel splitsen: "Geslaagd als toets: de uitkomst valt zoals verwacht.
  Williams' constante $r$ is verworpen."

## 7. Oefeningen — 8

**Goed**
- Instap is een variatie op de toy (4% in plaats van 5%), met de les in één zin.
- Oefening 1 (bel) en 2 (PVGO, optimale $b$) vragen afleidingen; oefening 3
  breidt de replicatie uit (naoorlogs, vijf jaar).
- Elke uitwerking eindigt met "Wat dit leert".

**Aanmerkingen**
- *Instap, uitwerking*: "Terugrekenen met $1{,}331$ geeft $1{,}04/0{,}06 =
  17{,}3333$." De vereenvoudiging ($d_4/1{,}331 = 1{,}04$) wordt niet uitgelegd.
- *Oefening 2, uitwerking*: bij ROE = 9% "wijst het raster een willekeurig punt als
  optimum aan" — de tabel toont dan een zinloos getal.

**Beter uitleggen**
- In de instap één zin: "$1{,}331 \times 1{,}04 / 1{,}331 = 1{,}04$".

---

## De drie verbeteringen met het meeste effect op het cijfer

1. **Helderheid (6 → 8):** de rekenfout "anderhalve tiende procentpunt"
   herstellen, de notatie tegenover [](#01-02-bachelier) vastleggen, de juiste
   verwijzing voor de standaardfout van 2%, "verderop in deze lecture" schrappen,
   de log/simpel-kalibratie benoemen, en "twintig tot dertig jaar" en "25%"
   uitrekenen. Effect op het eindcijfer ≈ +0,6.
2. **Taal (7 → 8):** barst/gat-jargon, "Wat rekenwerk geeft" en de stapelzin in
   *Waar we zijn* vervangen. Effect ≈ +0,15.
3. **Replicatie (7 → 8):** het oordeel over de replicatie scheiden van het oordeel
   over het model, en de verwachte afwijking als verwachting formuleren.
   Effect ≈ +0,1.

## Navertelling in vijf zinnen

Williams stelde in 1938 dat een aandeel de contante waarde is van alle verwachte
dividenden, wat volgt uit de definitie van rendement plus een constante
discontovoet en de eis dat er geen bel in de prijs zit. Gordon en Shapiro maakten
daarvan $p = d_1/(r-g)$, een formule die uiterst gevoelig is voor het kleine
verschil $r - g$, zodat een geschatte groeivoet de waardering een factor twee tot
drie laat zwerven. Onder een constante discontovoet moet een hoge
prijs-dividend-ratio worden gevolgd door snelle dividendgroei. Op Shillers data
sinds 1871 voorspelt de prijs-dividend-ratio echter vooral lage rendementen en
nauwelijks dividendgroei, dus de discontovoet is geen constante. Of die bewegende
discontovoet risico of vergissing is, laat de lecture open.

Wijkt niet af van het Overzicht.
