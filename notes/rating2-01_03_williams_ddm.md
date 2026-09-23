# Beoordeling: 01_03_williams_ddm (Williams en het dividend discount model)

Maatstaf: `plannen/rubriek-didactiek.md`. Gelezen als eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft. Kalibratie gelijk aan
de andere `rating2-*`-bestanden: hetzelfde gebrek krijgt dezelfde aftrek.

## 1. Eindcijfer: 7,9

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 8 |
| | **gewogen** | | **7,85 → 7,9** |

Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

## 2. Per criterium

### 1. Helderheid van de uitleg (8)

**Goed**
- *Opzet en aannames*: de notatiewissel ten opzichte van L2 wordt expliciet
  gemeld ("Let op de wissel ten opzichte van [](#01-02-bachelier). Daar waren
  kleine letters logs"), en de dubbele $b$ (bel en inhoudingspercentage) ook.
  Precies wat de rubriek vraagt.
- *Wat het voorspelt: het Gordon-groeimodel*: de gevoeligheidstabel (21,00 →
  26,25 / 26,50 / 17,50) en de duration (22 jaar, met de rekensom
  $(1 + 2 + 3 + 21 \times 25)/24$) geven de abstracte bewering "de prijs hangt
  aan $r - g$" een getal. Alle getallen kloppen bij narekenen.
- *Simulatie*: de kalibratie wordt uitgelegd tot en met de correctie van
  log- naar rekenkundige gemiddelden (6,1 in plaats van 5,2 procentpunt, ratio 17
  in plaats van 19,5), en er staat waarom die keuze de conclusie niet raakt.

**Aanmerkingen**
- *Waar we zijn in het verhaal*: "Cowles liet zien dat beleggingsadviseurs de
  markt niet verslaan, Kendall dat weekkoersen geen patroon hebben." L2 zegt
  letterlijk: "Dat Kendall nulcorrelaties vond, is een hardnekkig misverstand".
  De lecture herhaalt het misverstand dat haar voorganger rechtzet.
- *Simulatie*: "Met een halve eeuw data zit een analist er dus tot een factor
  drie naast". De eigen getallen geven 12,5 en 40,8 rond 19,5: hoogstens een factor
  2,1 naast. De factor drie is de breedte van het interval, niet de fout.
- *Simulatie*: "loopt het interval tussen het 5e en het 95e percentiel van
  ongeveer 13 tot ongeveer 40", twee alinea's later "$12{,}5$ tegen $19{,}5$" en
  "$40{,}8$". Afgerond en exact door elkaar voor hetzelfde getal.
- *Replicatie*, warning: "de log-prijs-dividend-ratio van het ene jaar hangt met
  een autocorrelatie van 0,91 samen met die van het volgende." Geen cel berekent
  dit getal.
- *Het kernresultaat*: "Maar het is een keuze, en veertig jaar later valt het vak
  erover uiteen." Welk moment (1978? Shiller 1981?) wordt niet gezegd.

**Beter uitleggen**
- *Replicatie*: "Samen is dat 0,15 log-punt, tegen 0,38 log-punt minder
  rendement." De lezer die de identiteit net heeft geleerd, verwacht dat de twee
  samen één log-punt verklaren. Eén zin dat de rest in de prijs-dividend-ratio over
  tien jaar zit (die zelf persistent is, 0,91), zou de rekensom sluiten.
- Transversaliteit: waarom een rationele bel in een markt met eindig veel
  aandelen en eindig vermogen zou kunnen bestaan of niet. Eén zin (de bel moet
  sneller groeien dan de economie) zou het verband met "$g$ begrensd door de
  groei van het bbp" leggen.

### 2. Opbouw en rode draad (8)

**Goed**
- *Overzicht*: vraag en antwoord in de eerste drie zinnen ("De data verwerpen dat
  antwoord in die vorm: niet de verwachte dividenden maar de discontovoet
  beweegt"), gevolgd door een routekaart die de secties volgt.
- Het getal $r - g = 5$ procentpunt loopt door: toy (21,00 eindwaarde),
  gevoeligheidstabel (dezelfde 21,00), rooster, en simulatie ("bijna de 5
  procentpunt van het toy-voorbeeld"). De overgang simulatie → replicatie is
  expliciet ("De simulatie hield $r$ vast en liet $g$ onzeker. De replicatie
  hierna vraagt het omgekeerde").
- Het onderscheid identiteit / model wordt vooraan gezet, in de theorie
  uitgewerkt en in *Wat er brak* teruggehaald. Subsecties openen met hun
  conclusie.

**Aanmerkingen**
- *Theorie*: het blok "Samengevat" staat aan het eind van de theorie, niet aan
  het eind van de lecture. Zelfde aftrek als in de andere lectures.
- *PVGO*: "Simulatie en replicatie werken daarna weer met $g$ als één getal." De
  lecture zegt zelf dat deze subsectie een zijpad is; samen met de rationele bel
  zijn het twee zijpaden in de theorie die de rode draad (constante $r$ →
  toetsbare PD-voorspelling) onderbreken.
- *Simulatie*: de simulatie toont gevoeligheid voor een geschatte $g$, maar de
  replicatie verwerpt constante $r$. De simulatie draagt daardoor niet bij aan
  het hoofdresultaat; ze staat naast de lijn, niet erop.

**Beter uitleggen**
- Waarom de simulatie $g$ schat en niet $r$, terwijl de lecture uitkomt op "$r$
  beweegt": één zin in de simulatie-inleiding over wat dit voor het
  hoofdargument betekent.

### 3. Taal (7)

**Goed**
- *Intuïtie*: "Een aandeel is een stuk papier. Het geeft geen nut, het gaat niet
  stuk, en niemand kan erin wonen." Kort, beeldend en natuurlijk.
- Eén naam per begrip bewust vastgelegd: "we noemen hem verder alleen de
  discontovoet", en de lecture houdt zich daaraan.
- Engelse termen krijgen een Nederlandse omschrijving (rational bubble,
  retention ratio, PVGO, CAPE).

**Aanmerkingen**
- Calques: "Meer dan het krediet krijgt" (*more than it gets credit for*, in
  *Wat er brak*); "doet het meeste werk" (*does most of the work*, idem); "Ook
  dan is het veel te weinig om het werk te doen" (ex-williams-ddm-3); "Neem nu
  verwachtingen op $t$" (*take expectations*); "Ver van de asymptoot is de
  functie vlak en vergeeflijk" (*forgiving*, figuurbijschrift).
- Projectjargon: "Die onzekerheid heet in deze reeks de standaardfout van 2%" en
  "Ook hier geldt de standaardfout van 2%". Zelfde aftrek als in de andere
  lectures.
- *Wat er brak*: "In de vorm 'earnings yield plus groei' wordt die nog dagelijks
  gebruikt." Onvertaald Engels, terwijl "winstrendement" bestaat.

**Beter uitleggen**
- Geen; de taal hindert het begrip nergens ernstig.

### 4. Toy-voorbeeld (8)

**Goed**
- *Toy-voorbeeld*: zes stappen, elk met de hand na te rekenen, en een slimme
  keuze ($g = r$ in de eerste fase) waardoor de eerste drie termen elk 1,00 zijn.
  Stap 5 laat zien dat 21,00 exact is.
- Eén recept, expliciet aangekondigd en later afgeleid; tabel hand/code; slotzin
  met wat de lezer nu weet.
- Het toy wordt in de theorie hergebruikt (gevoeligheidstabel, duration,
  instapoefening).

**Aanmerkingen**
- *Toy-voorbeeld*: "Weeg elk dividend met zijn aandeel in de prijs: dan ligt het
  zwaartepunt van deze waardering 22 jaar in de toekomst. De theorie rekent dat
  getal na". Een tweede resultaat dat pas later wordt afgeleid; de lezer moet het
  in het toy op gezag aannemen.
- Slotzin: "weet nu twee dingen: de prijs komt vooral uit de eindwaarde, en de
  eindwaarde hangt af van het kleine verschil $r - g$." Het tweede wordt in het toy
  niet getoond (er wordt maar één $g$ doorgerekend); dat gebeurt pas in de
  gevoeligheidstabel en de instapoefening.

**Beter uitleggen**
- Een stap 7 met $g = 4\%$ (nu de instapoefening) zou het tweede "ding" in het
  toy zelf laten zien.

### 5. Code en figuren (8)

**Goed**
- Toy-cel: benoemde tussenresultaten (`dividends`, `discounted`, `d_next`,
  `terminal`, `terminal_pv`) met commentaar dat naar de stappen verwijst.
- `gordon` en het rooster: zichtbare dubbele lus in plaats van broadcasting; de
  simulatie markeert `finite = g_hat < r_true  # anders: oneindige prijs`.
- Figuren met leeswijzer vooraf ("Let links op de lange staart naar rechts, en
  rechts op hoe steil de hyperbool wordt vlak voor $g = r$") en een bijschrift
  achteraf; de scatter krijgt ook een zin erna.

**Aanmerkingen**
- Engelse docstrings: `"""Gordon growth price of a claim on a dividend growing at
  g forever."""`, `"""Overlapping h-year forward growth and return, against log
  PD."""`. Zelfde aftrek als elders.
- Uitwerking ex-williams-ddm-3: `for kolom in ("dividendgroei", "rendement"):`
  naast Engelse namen (`frame`, `rows_ex`, `fit`). Taalwissel in variabelenamen.
- *PVGO*: zeven `print`-regels in plaats van een tabel met hand/code, terwijl de
  rest van de lecture dat format gebruikt.
- De vergelijkingstabel in *Replicatie* (0,015; $t = 1{,}63$; 0,05; $-0{,}038$ ...)
  staat in markdown en wordt niet door code gevuld; zie criterium 6.

**Beter uitleggen**
- Waarom `lags=horizon - 1` bij `hap.newey_west`: dat staat in de tekst (één
  vertraging per gedeeld jaar), maar de functie en haar uitvoer (`params.iloc[1]`
  is de helling) worden niet geïntroduceerd.

### 6. Replicatie en empirie (8)

**Goed**
- *Replicatie*-blok: bron, wat, data, verschil en verwachte afwijking, met een
  falsifieerbare tegenhypothese ("Een significant positieve dividendcoëfficiënt
  ... zou Williams' lezing juist steunen").
- Omdat er geen origineel getal bestaat, zet de lecture een tabel Williams /
  verwacht / hier neer. Dat is een eerlijke vervanging van origineel/hier.
- Oordeel begint met **Geslaagd.** en verwijst naar de verwachting; de warning
  over overlap en de Stambaugh-bias begrenst het oordeel.

**Aanmerkingen**
- *Replicatie*: de tabel "| dividendgroei: coëfficiënt | positief, significant |
  niet significant | 0,015 ($t = 1{,}63$) |" is met de hand overgetypt uit de
  regressiecel. Zelfde aftrek als de hellingtabel in L2.
- *Replicatieblok*: "met een $R^2$ rond tien procent". De onderbouwing ("Ook
  onder de andere lezing verklaart de prijs-dividend-ratio maar een klein deel")
  is geen reden voor tien en niet voor vijf of twintig.
- *Replicatie*: de CAPE-regressie heeft geen verwachte afwijking en geen oordeel;
  "Dat sterkere verband zegt weinig" staat er achteraf.

**Beter uitleggen**
- Wat "één log-punt" in de praktijk is: het voorbeeld 54 in plaats van 20 staat
  er, maar pas in de tweede alinea na de tabel. Vóór de tabel geplaatst zou de
  coëfficiënt 0,015 direct leesbaar zijn.

### 7. Oefeningen (8)

**Goed**
- Instap is het toy met $g = 4\%$, met de hand (inclusief de observatie dat
  $1{,}331$ wegvalt) en in code.
- Ex-williams-ddm-1 bevat een echte afleiding (de bel lost de
  differentievergelijking op) en ex-williams-ddm-3 breidt de replicatie uit
  (naoorlogs, vijf jaar).
- Elke uitwerking eindigt met "Wat dit leert".

**Aanmerkingen**
- Uitwerking ex-williams-ddm-1 (3): de vraag "Vanaf welk jaar is meer dan de
  helft van de prijs bel?" wordt alleen door `print(...)` beantwoord; de tekst
  noemt het jaar en de gevraagde prijs-dividend-ratio's na 10, 25 en 50 jaar
  niet.
- Uitwerking ex-williams-ddm-2: "De 0,94 in de tabel is daarom betekenisloos" en
  bij 12% "loopt de optimale $b$ naar de asymptoot ... en explodeert de prijs". Twee
  van de drie gevallen hebben geen goed gedefinieerd optimum; de opgave ("bepaal
  het inhoudingspercentage $b$ dat de prijs maximaliseert") voorziet dat niet.

**Beter uitleggen**
- Ex-williams-ddm-2 (2): de vraag omzetten naar "voor welke $b$ stijgt de prijs,
  en waarom" zou de les (teken van $\mathrm{ROE} - r$) zonder raster-artefact
  opleveren.

## 3. De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9):** Kendall in de admonition in lijn brengen met L2, de
   "factor drie" corrigeren (fout hoogstens een factor twee; de factor drie is
   de intervalbreedte), één zin over het ontbrekende deel van de 0,15 + 0,38
   log-punt, en de autocorrelatie 0,91 laten berekenen. Eindcijfer +0,3.
2. **Opbouw (8 → 9):** een Samengevat aan het eind van de lecture, en in de
   simulatie-inleiding één zin die haar aan het hoofdargument (constante $r$)
   koppelt. Eindcijfer +0,2.
3. **Taal (7 → 8):** de calques vervangen ("meer dan het krediet krijgt", "het
   werk doen", "verwachtingen nemen", "vergeeflijk", "earnings yield") en
   "standaardfout van 2%" als label schrappen. Eindcijfer +0,15.

## 4. Navertelling in vijf zinnen

Williams (1938) stelde dat een aandeel de contante waarde van zijn verwachte
dividenden waard is; dat volgt uit de definitie van rendement plus twee
aannames, een constante discontovoet en transversaliteit (geen bel). Gordon en
Shapiro brachten dat terug tot $p = d_1/(r - g)$, waardoor zichtbaar wordt dat de
prijs vooral aan het kleine, slecht gemeten verschil $r - g$ hangt, en een
geschatte $g$ de waardering een factor twee of meer kan laten afwijken. De
boekhoudkundige identiteit zelf is niet te verwerpen, maar het model van
Williams wel: bij constante $r$ moet een hoge prijs-dividend-ratio door snelle
dividendgroei gevolgd worden. Op Shillers data sinds 1871 voorspelt de
prijs-dividend-ratio echter het tienjaarsrendement ($R^2 \approx 0{,}12$) en
nauwelijks de dividendgroei, dus $r$ is geen constante maar een tijdreeks. Of
die bewegende $r$ risico of vergissing is, laat de lecture open voor de rest van
de reeks.

Dit komt overeen met het Overzicht.
