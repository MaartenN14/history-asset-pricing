STATUS 01_04_markowitz F6c words=5387 prose=PASS open=0 cijfer=8,7 min=8,5

# Eindbeoordeling (F6): Markowitz, Roy en Tobin

## Eindcijfer: 8,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,70 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,43, dus 8,4.
Lengte: 5.403 woorden, onder de 5.500.

## Feitelijke fouten

Nagerekend en in orde: $\boldsymbol\Sigma^{-1}$ (28,125; −6,25; 12,5; 100), de
gewichten 7/41, 2/41, 32/41 en 8,83%; $A, B, C, D$ (128,125; 7,0625; 0,51125;
15,625; $AC = 65{,}5$); $\lambda = 0{,}368$, $\delta = -0{,}0125$, 15,6% (22% minder
dan 20%); $C/B = 7{,}24\%$ en de fondsgewichten; de tangentportefeuille (1/3, 2/9,
4/9; 8,22%; 0,529; 11,76%); Roy (2,4 standaarddeviaties; 17%; 0,8%); de
diversificatietabel (19,05; 9,53); $N/T = 0{,}083$ tegen 0,021; de simulatie (0,50;
0,47; 0,16; 0,39); 757 en 637 maanden, $1/\sqrt{637} = 0{,}04$; 3,3 keer de
standaarddeviatie; de DGU-vergelijking (gat 0,10; 0,30; 0,54; verschillen 0,077 en
0,055 onder $2 \times 0{,}04$); posities (21; 1158); oefeningen (9/49, 4/49, 36/49,
8,57%; $\mu_z = 0{,}0200$; 0,239 tegen 0,104; 7,6 tegen 72). Een eigen simulatie
bevestigt dat bij $T = 120$ vrijwel geen steekproef boven 1/N uitkomt (0 tot 0,05%).

1. **Theorie, "Opzet en aannames".** "Ook de risicovrije rente $R^{f}$ is netto,
   dus 2% is 0,02; andere lectures schrijven $R^{f}$ soms bruto (1,02)." De setup
   legt voor de hele reeks vast dat $R^{f}$ netto is ("de risicovrije rente $R^f$ is
   netto (0,02 bij 2%)"), en geen lecture van dit deel schrijft $R^f$ bruto.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- Theorie: $\lambda$, $\delta$, $A$ tot $D$ krijgen elk een toy-getal; de
  lezer kan de parabool met de hand narekenen.
- "Een risicovrij activum": de tangentportefeuille in vijf handregels, met de
  verklaring waarom kleine aandelen maar 22% krijgen.
- "Waar het strandt": drie genummerde redenen, elk met een getal (6,3 pp; −6,25;
  $N/T = 0{,}083$).

*Aanmerkingen*
- Opzet: "Er zijn $N$ risicovolle activa met netto rendementen $\mathbf{R}_{t+1}$
  (10% is 0,10, terwijl $R$ in [](#00-01-rendementen) bruto was)". De setup-tabel
  definieert $R$ als bruto voor de hele reeks; de afwijking wordt als verschil
  met één lecture gebracht in plaats van met de afspraak.
- "Waar het strandt", punt 1: "Met $T$ jaren data"; punt 3: "Bij tien activa en
  120 maanden is $N/T = 0{,}083$ per maand". $T$ wisselt binnen één lijst van jaren
  naar maanden.
- "Hoe zwaar de drie soorten fouten wegen": "Bij een risicotolerantie van 50 in
  hun mean-variance-nut". Het getal 50 heeft geen schaal of betekenis voor de lezer.
- Theorie: $\lambda$ is hier een Lagrange-multiplicator; in de setup-tabel is
  $\lambda_f$ de prijs van risico.

*Beter uitleggen*
- Chopra-Ziemba: één zin wat risicotolerantie 50 betekent, bijvoorbeeld welk deel
  van het vermogen zo'n belegger in aandelen zou houden.
- De bias $N/T$: één zin waarom $1/T$ de variantie van een geschatte Sharpe-ratio is
  (gemiddelde gedeeld door $\sigma$, standaardfout $1/\sqrt T$).

### 2. Opbouw en rode draad (8,5)

*Goed*
- Overzicht met vraag en antwoord, inclusief de wending dat minimum-variantie wint.
- De twee voorspellingen uit de intuïtie worden in de theorie met naam ingelost.
- Het toy draagt de hele theorie, tot en met Roy en de zero-beta-oefening; de
  simulatie is gekalibreerd op de replicatie (tien sterk gecorreleerde activa).

*Aanmerkingen*
- Vier vooruitverwijzingen buiten "Wat er daarna kwam" (twee keer
  [het CAPM](#02-08-capm), [](#04-20-voorspelbaarheid),
  [](#05-31-portfolio-choice)); STYLE §11.3 staat er hoogstens twee toe.

*Beter uitleggen*
- Geen.

### 3. Taal (8,5)

*Goed*
- Korte, heldere zinnen; Engelse vaktermen (*efficient frontier*, *safety first*)
  krijgen een Nederlandse uitleg.

*Aanmerkingen*
- Vier subsecties openen met "De bewering:". Dat wordt een formule.
- "Mean-variance beweegt ook veel wilder" en "In beide datasets verliest
  mean-variance van 1/N": de strategie heet afwisselend "mean-variance",
  "de mean-variance-portefeuille" en "de optimalisator".

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Vijf handstappen met exacte breuken (7/41), inclusief de 2x2-inversie in woorden,
  tabel hand/code, en de les dat een mengsel veiliger is dan het veiligste
  activum.

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `rolling_oos` maakt de tijdsvolgorde zichtbaar ("alleen maanden vóór t").
- De simulatiecel scheidt de drie bronnen van schade in drie kolommen.

*Aanmerkingen*
- Figuur "Beloofde en geleverde Sharpe-ratio": de figuurcel trekt 2000 nieuwe
  steekproeven in plaats van de tabel te hergebruiken; tabel en figuur zijn dus
  niet dezelfde getallen.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8,5)

*Goed*
- Blok volledig; de verwachte afwijking is een ordening, en het oordeel
  "Geslaagd" toetst precies die ordening.
- Het voorbehoud over de standaardfout van een verschil is eerlijk en kort.

*Aanmerkingen*
- "Voor de industrieën hebben we hun getallen niet." De helft van de replicatie
  heeft geen origineel.
- De positietabel en de conclusie "de winnaar is ... de minimum-variantieportefeuille"
  vallen buiten de verwachte afwijking.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy, de zero-beta-afleiding met handgetallen, krimpen als
  uitbreiding van de replicatie; elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De notatie in lijn brengen met de setup: $R$ netto als afwijking van de
   reeksafspraak noemen, de bewering over bruto $R^f$ schrappen, en $T$ binnen
   "Waar het strandt" één eenheid geven (helderheid 8 → 8,5).
2. Chopra-Ziemba's risicotolerantie een betekenis geven, of de zin tot de
   verhouding elf en eenentwintig terugbrengen (helderheid → 8,5).
3. Twee vooruitverwijzingen schrappen (opbouw 8,5 → 9).

## Navertelling in vijf zinnen

Markowitz maakte van risico de covariantie met de portefeuille: een mengsel kan
veiliger zijn dan het veiligste activum, en de efficiënte rand is een parabool
waarop elke portefeuille een mengsel van twee fondsen is. Met Tobins risicovrije
activum houdt iedereen dezelfde tangentportefeuille en verschilt alleen de dosis;
Roys safety-first komt bij dezelfde portefeuille uit. In een grote portefeuille
blijft alleen de gemiddelde covariantie over. In de praktijk moeten
$\boldsymbol\mu$ en $\boldsymbol\Sigma$ geschat worden, en de fout in
$\boldsymbol\mu$ maakt de geschatte optimale portefeuille slechter dan 1/N. Op
French-data bevestigt de replicatie van DGU die ordening, en wint de
minimum-variantieportefeuille, die $\boldsymbol\mu$ niet gebruikt.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-01_04_markowitz.md` §F6-1 en de lecture.

| punt | status | vindplaats |
|---|---|---|
| Fout 1: "$R^f$ soms bruto" | opgelost | bijzin geschrapt |
| Verbetering 1: notatie, $T$ één eenheid | opgelost | Opzet: "in de notatie van [](#00-00-setup): $r$ is netto ..., $R = 1 + r$ bruto, en de risicovrije rente $R^{f}$ netto"; rendementen heten overal $r$ (ook Roy: $r_{\min}$); "Tien jaarwaarnemingen", "$T = 120$ maandwaarnemingen" |
| Verbetering 2: Chopra-Ziemba | opgelost | "In een van hun rekenvoorbeelden ... elf keer ... eenentwintig keer"; het getal 50 is weg |
| Verbetering 3: vooruitverwijzingen | opgelost | nog twee buiten "Wat er daarna kwam" (02-08 in het Overzicht, 04-20) |
| $\lambda$ als Lagrange-multiplicator | opgelost | "deze $\lambda$ is een Lagrange-multiplicator, niet de prijs van risico" |
| "De bewering:" als vaste opening | niet | blijft een punt bij criterium 3 |
| Figuurcel trekt nieuwe steekproeven | niet | blijft een punt bij criterium 5 |
| Naadpunten 3, 4, 6 en 8 | opgelost | zie boven |
| Naadpunt 10 | opgelost | Waar we zijn: "schommelingen in $r$ meer van de prijsbeweging verklaren dan de dividenden" |

Geen verslechteringen en geen nieuwe feitelijke fouten. Na de hernoeming naar $r$
zijn de vergelijkingen van Roy en de 1/N-variantie nagekeken; ze kloppen.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8,5 | 9 |
| 3 | Taal | 8,5 | 8,5 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 8,5 |
| 6 | Replicatie | 8,5 | 8,5 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,80 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,68. **Eindcijfer 8,7,
laagste deelcijfer 8,5.**
