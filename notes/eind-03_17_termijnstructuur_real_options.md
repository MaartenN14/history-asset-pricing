STATUS 03_17_termijnstructuur_real_options F6c words=5111 prose=PASS open=0 cijfer=8,9 min=8,5

# Eindbeoordeling F6: Brennan-Schwartz, Vasicek, CIR en Longstaff-Schwartz (03_17_termijnstructuur_real_options)

Cijfer van record volgens `plannen/rubriek-didactiek.md` en `plannen/kaart-rollen.md` §8.
Zelfde kalibratie als de beoordelingen van 03_10–03_12 en 03_16.

## De drie verbeteringen met het meeste effect

1. **Opbouw (7,5 → 8,5).** De lecture draagt vier modelfamilies (termijnstructuur,
   affiene klasse, real options, LSM), negen theoriesubsecties, een toy met twee
   mechanismen en drie empirische lijnen in twee replicatieblokken, op 5.402 woorden.
   Kies één kernlijn (de termijnstructuur: toy-renteboom, Vasicek/CIR, simulatie,
   curve en PCA) en maak van de mijn en LSM de tweede, kortere lijn: de koperboom als
   oefening, McDonald-Siegel en de tabel van Brennan-Schwartz in een dropdown, LSM
   met één tabel. Zeg in de routekaart welke lijn de kern is.
2. **Replicatie (8 → 8,5).** De getallen uit de lopende tekst halen: de alinea na de
   schattingstabel (negen getallen), de alinea na de curvetabel en de twee alinea's
   na de figuur. Verwijs naar de tabel en geef één conclusie.
3. **Helderheid (8,5 → 9).** De fout over Duffie-Kan in het Overzicht herstellen, één
   naam kiezen voor "lange yield"/"lange rente", en Laguerre-polynomen en de
   Svensson-curve in één bijzin uitleggen.

Samen: 2,70 + 1,70 + 1,275 + 0,80 + 0,80 + 0,85 + 0,45 = 8,575, dus 8,6.

## Eindcijfer: 8,2

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 7,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,55 + 1,50 + 1,275 + 0,80 + 0,80 + 0,80 + 0,45 = 8,175, dus 8,2.
Laagste deelcijfer 7,5: het streefcijfer (8,5, geen deelcijfer onder 8) is niet
gehaald. Lengte: 5.402 woorden volgens `prose_stats` (PASS), 98 onder de grens. De twee
zinnen boven 40 woorden die `prose_stats` telt, zijn lijsten en formules, geen echte
stapelzinnen. Replicatieblokken: samen 304 woorden, elk onder 250.

## Feitelijke fouten

Nagerekend met de hand en tegen de celuitvoer (`tools/nb_outputs.py`; de notebook is
na de .md bijgewerkt). Correct: de renteboom (0,900901; 0,952381; 1,010101; 0,858001;
0,962001; 0,866668; 0,907771; yields 4,957% en 4,886%; 0,114 pp); de koperboom
($q = 0{,}625$; 1,05 en 1,1025; NCW 0,140590; 0,461905; 0,274943; keuze 0,134354,
bijna de helft); $0{,}3 \cdot 5\% = 1{,}5$ pp; de afleiding van de PDE en de tekens van
de risiconeutrale drift (Vasicek $\theta^* = \theta + \lambda\sigma/\kappa$, CIR
$\kappa^* = \kappa - \lambda\sigma$); het Vasicek-bewijs ($B(1 + e^{-\kappa\tau})/2 =
B - \kappa B^2/2$); $\log 2/0{,}15 = 4{,}6$; $5\% + 3\% - 0{,}5\% = 7{,}5\%$; 2,7%;
$h = 0{,}16$ en 5,16%; $0{,}3 \cdot 0{,}22 = 0{,}067$; de padsimulatie (58%, 4,7%,
$-6{,}7\%$); McDonald-Siegel ($\eta = 2$, $V^* = 2I$; $-\delta$ in $\eta = 1$); de
simulatie ($b = 0{,}9876$; 0,10–0,54; 1,43–1,59%; 4,2–9,8%; mediaan 0,24); de
schattingen (0,10 met SE 0,06, $t = 1{,}65$, halfwaardetijd 6,9 jaar; 4,2% met SE 2,0;
1,5%; CIR 0,05 en 1,03); de curvetabel ($\lambda = 0{,}35$, 8,3%, 115 en 124 bp;
$-2{,}32$ en $+1{,}79$; CIR $+1{,}45$ en $-1{,}86$; 2000 en 2026 binnen 0,84 pp); de PCA
(91,7/7,3/0,9 en 89,0/7,7/2,3; 99,9% en 98,9%; correlatie 0,69); LSM (Europese put
3,844 nagerekend met Black-Scholes; boom 4,478; 4,330 → 4,483; 0,148 te laag; 0,005
binnen één SE; spreiding 0,066 → 0,008; 4,60 en 4,475); de oefeningen (0,011999;
0,003332; 0,005714; Europees nul; 0,82962 tegen 0,83013, 1,2 SE; convexiteit 0,34 en
0,50 pp; 0,28 (0,14) en 6,8% tegen 0,10 (0,07) en 1,3%; $-1{,}15$ en $-2{,}86$ SE; 2,0%
→ 0,65%; 0,76 → 0,56). Niet tegen de bron gecontroleerd: de tabel van Brennan en
Schwartz (76/44/20 cent, 0,89 miljoen, 12%) en de verdeling 89,5/8,5/2,0 van Litterman
en Scheinkman. Tabel 1 van Longstaff en Schwartz (4,478; 3,844; 4,472; 0,010) klopt
met het artikel.

1. **Overzicht, geschiedenisalinea.** "{cite:t}`BrennanSchwartz1979` voegden de lange
   rente als tweede factor toe, [...] {cite:t}`DuffieKan1996` lieten zien dat ze
   allemaal *affien* zijn". Het tweefactormodel van Brennan en Schwartz (korte en
   lange rente) is niet affien; het werd numeriek opgelost. De theorie zegt het zelf
   goed: "Vasicek, CIR en Longstaff-Schwartz zijn speciale gevallen", zonder
   Brennan-Schwartz.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Het kernresultaat.** De hedge van de handelaar (tien- tegen tweejaarsobligatie)
  draagt waarom-alinea en bewijs, en de term premium krijgt direct een getal
  ($0{,}3 \cdot 5\% = 1{,}5$ procentpunt).
- **Vasicek.** Elke parameter krijgt een naam en een orde van grootte ("bijvoorbeeld
  0,15 per jaar (halfwaardetijd [...] 4,6 jaar)"), de lange yield wordt in drie termen
  uitgerekend ($5\% + 3\% - 0{,}5\% = 7{,}5\%$) en in beide richtingen gelezen ("Stijgt
  $\sigma$ [...] Stijgt $\kappa$").
- Botsende letters worden gemeld waar ze botsen: $d$ ("de daalfactor, niet het
  dividend"), $q$ ("niet de kans uit de koperboom"), de convenience yield ("Brennan en
  Schwartz noemen haar $\kappa$") en $V$ ("een nieuwe $V$, niet de mijnwaarde").

*Aanmerkingen*
- Overzicht: "lieten zien dat ze allemaal *affien* zijn" (feitelijke fout 1).
- Eén begrip, twee namen: "lange yield" (Vasicek, Samengevat) en "lange rente" ("Omdat
  de lange rente vastzit, verklaart Vasicek een hoge lange rente niet samen met een
  hoge korte"; bijschrift: "de waargenomen lange rente beweegt trager").
- Least-squares Monte Carlo: "een constante en drie gewogen Laguerre-polynomen, zoals
  in het artikel". Wat een Laguerre-polynoom is en waarom gewogen, staat alleen in de
  code.
- Drie factoren: "komen deels door de gladde Svensson-curve van GSW". Svensson niet
  uitgelegd.
- $a$ is de kosten per pond in de koperboom en de mijn-PDE, en $a_0$, $a_1$ zijn de
  driftcoëfficiënten van de affiene stelling. Niet gemeld.

*Beter uitleggen*
- Laguerre: één bijzin ("veeltermen in $S/K$, vermenigvuldigd met $e^{-x/2}$ zodat de
  regressie goed geconditioneerd blijft").

*Voor een 9*
- Feitelijke fout 1 herstellen (Overzicht).
- Eén naam voor de lange yield (Replicatie, figuurbijschrift).
- Laguerre en Svensson in één bijzin uitleggen (Least-squares Monte Carlo; Drie
  factoren).

### 2. Opbouw en rode draad (7,5)

*Goed*
- Het Overzicht geeft vraag en antwoord in twee zinnen en noemt de draad: "Hetzelfde
  argument prijst een mijn met de keuze om te sluiten."
- De vier verwachtingen uit de intuïtie worden elk ingelost ("Zoals de intuïtie
  voorspelde, ligt de lange yield zonder beloning ($\lambda = 0$) onder $\theta$";
  "zoals de intuïtie voorspelde" bij de correlatie, bij McDonald-Siegel en bij LSM).
- De renteboom komt terug in de theorie (Jensen, 0,114 pp) en in oefening 1; de
  simulatie beantwoordt één vraag en de replicatie sluit erop aan ($t = 1{,}6$ voor
  $\hat\kappa$).
- De naden kloppen: 03_16 eindigt met "de rente en de waarde van flexibiliteit, in
  [](#03-17-termijnstructuur-real-options)", 04_18 begint met "[](#03-17-...) keek naar
  de prijs van de tijd; hier keren we terug naar de cross-sectie".

*Aanmerkingen*
- Vier modelfamilies in één lecture: termijnstructuur, affiene klasse, real options
  (mijn en investeringsdrempel) en LSM. Theorie telt negen `###`-delen. De
  routekaart zegt "We leiden vier dingen af", maar wat de kern is voor de *vraag* van
  de lecture (hoe krijgt een obligatie een prijs), blijft na de mijn en LSM onduidelijk.
- Het toy draagt twee losse mechanismen (renteboom en koperboom).
- Real options hebben geen simulatie en geen replicatie; hun enige empirie is een
  tabel uit Brennan en Schwartz midden in de theorie ("losten het volledige model
  numeriek op (hun tabellen 1 en 2)").
- Twee replicatieblokken en drie empirische lijnen (curvefit, PCA, LSM), met LSM als
  aparte replicatie zonder band met de simulatie.

*Beter uitleggen*
- Eén zin na de routekaart die zegt welke lijn de kern is en welke een toepassing van
  hetzelfde argument.

*Voor een 9*
- Eén kernlijn (termijnstructuur) met toy, theorie, simulatie en replicatie; de mijn
  en McDonald-Siegel naar een oefening of dropdown; LSM terugbrengen tot de stelling en
  één tabel (Theorie → Real options, Least-squares Monte Carlo; Replicatie → LSM).
- Het toy tot de renteboom beperken; de koperboom als oefening.

### 3. Taal (8,5)

*Goed*
- Korte, heldere zinnen (gemiddeld 15 woorden), vrijwel geen puntkomma's in lopende
  tekst, geen u/je.
- Engelse vaktermen krijgen bij de eerste keer een Nederlandse uitleg (*convenience
  yield*, *term premium*, *value matching*, *smooth pasting*, *antithetisch*).

*Aanmerkingen*
- Telegramstijl (STYLE §11.1): "Eerst de imports-cel, de enige van deze lecture."
- "Wat er brak": "De Chicago-lezing: de marktprijs van risico is niet constant." en
  "De Yale-lezing:" zonder bijzin wat de kampen zijn (zelfde aanmerking als bij
  03_10–03_12).
- Overzicht: "Zo werd Black-Scholes een methode voor alles wat van een onzekere
  toestand afhangt: voor Santa-Clara de UCLA-lijn van zijn mentoren Brennan en
  Schwartz". Het deel na de dubbele punt is geen zin.
- "Real options": "verschillen de waarden van open en gesloten mijn precies de
  wisselkosten". "Precies" in de betekenis van "exact" mag, maar hier is het
  overbodig.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De telegramzin en de Santa-Clara-zin tot volledige zinnen maken; Chicago en Yale in
  één bijzin duiden (Toy-voorbeeld, Overzicht, Wat er brak).

### 4. Toy-voorbeeld (8)

*Goed*
- Opzet-tabel, recept met verwijzing naar [](#eq-termijnstructuur-real-options-prijs),
  zes stappen die met de hand narekenbaar zijn, één cel, tabel hand/code.
- De slotzin zegt wat de lezer weet, en de laatste zin maakt de keuze tastbaar ("Kost
  openen 0,20, dan verwerpt de netto contante waarde het project en accepteert de
  waardering met de keuze het").

*Aanmerkingen*
- Twee mechanismen in één toy: het convexiteitseffect in een renteboom en de waarde
  van de keuze om te sluiten in een koperboom. De rubriek vraagt één mechanisme.
- De slotalinea draagt daardoor twee lessen.

*Beter uitleggen*
- Geen.

*Voor een 9*
- Het toy tot de renteboom beperken en de koperboom als oefening of als klein
  voorbeeld bij Real options zetten.

### 5. Code en figuren (8)

*Goed*
- `simulate_vasicek` en `simulate_cir` simuleren exact met zichtbare lussen; `lsm_put`
  volgt het algoritme stap voor stap; `binomial_put` laat de achterwaartse lus zien.
- Elke figuur heeft een leeswijzer vooraf en een bijschrift dat de uitkomst zegt.

*Aanmerkingen*
- Parameters als losse globals: "`KAPPA, THETA, SIGMA_V = 0.15, 0.05, 0.015`" en
  "`S0, u, d, R_f, cost = 1.00, 1.2, 0.8, 0.05, 1.00`" (STYLE §11.8 vraagt een dict of
  dataclass).
- Compacte trucs: "`idx = np.flatnonzero(itm)[payoff[itm] > design @ coef]`" in
  `lsm_put` en "`eigvec = eigvec * np.sign(eigvec[-1])`" bij de PCA.
- De cel van de LSM-figuur rekent twintig herhalingen, tekent en bouwt daarna nog een
  tabel: rekenwerk en presentatie in één cel.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De parameters in dicts; de uitoefenstap in `lsm_put` in twee benoemde regels
  (welke paden, welke beslissing); de LSM-herhalingen in een eigen cel (Least-squares
  Monte Carlo; Replicatie → LSM).

### 6. Replicatie en empirie (8)

*Goed*
- Beide blokken hebben een toetsbare verwachte afwijking, en de eindtabel zet elke
  verwachting naast de uitkomst; de oordelen beginnen met "Geslaagd".
- PCA en LSM hebben een tabel origineel/hier met de getallen van de artikelen
  (89,5/8,5/2,0/98,4; 4,478/3,844/4,472/0,010).
- De curvefiguur laat de fout van één factor in één oogopslag zien, en de tekst legt
  haar terug aan de correlatiestelling.

*Aanmerkingen*
- Getallen in lopende tekst: "Vasicek schat $\hat\kappa = 0{,}10$ per jaar
  (halfwaardetijd ongeveer 7 jaar), met standaardfout 0,06: een $t$-waarde van maar 1,6.
  $\hat\theta = 4{,}2\%$ heeft een standaardfout van 2,0 procentpunt [...]
  $\hat\sigma = 1{,}5\%$ [...] CIR vindt $\hat\kappa = 0{,}05$ en een Feller-verhouding
  van 1,03": negen getallen in één alinea. Ook "Vasicek zit met de 10-jaarsyield in
  1981 2,3 procentpunt te laag en in 2021 1,8 te hoog. Gemiddeld zit Vasicek 115
  basispunten naast [...] CIR 124" en de twee alinea's na de curvefiguur.
- Twee replicatieblokken; de LSM-replicatie staat los van de simulatie en van de
  vraag van de lecture.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De getallen in de drie genoemde alinea's vervangen door een verwijzing naar de tabel
  en één conclusie per alinea (Vasicek en CIR op de driemaandsrente; De modelcurve).
- De LSM-replicatie inkorten tot tabel en oordeel, of naar een oefening.

### 7. Oefeningen (9)

*Goed*
- Oefening 1 varieert het toy (een Amerikaanse put op de obligatie), oefening 2 leidt
  Vasicek af zonder Riccati en controleert met Monte Carlo, oefening 3 herhaalt de
  replicatie op twee deelsteekproeven; elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen*
- Oefening 3 vraagt ook het aandeel van de eerste component per periode; de uitwerking
  noemt het niet (0,93 en 0,91).

*Beter uitleggen*
- Geen.

## Navertelling in vijf zinnen

Als één renteschok alle obligaties drijft, bieden ze dezelfde marktprijs van risico, en
voldoet elke obligatieprijs aan één PDE, met als oplossing een risiconeutrale
verwachting van de disconteringsfactor. In de affiene klasse (Vasicek, CIR) is de
log-prijs lineair in de rente, en ligt de lange yield vast: gemiddelde plus premie min
convexiteit. Hetzelfde argument prijst een mijn met de keuze om te sluiten, laat een
project pas bij ongeveer twee keer de kosten starten, en LSM schat de waarde van
doorgaan met een regressie en geeft een ondergrens. Veertig jaar data leggen de
volatiliteit scherp vast maar de drift niet, en op echte data zit een eenfactormodel met
constante prijs van risico in 1981 en 2021 meer dan een procentpunt naast de curve. De
curve heeft drie factoren (level, slope, curvature), en LSM reproduceert tabel 1 van
Longstaff en Schwartz.

Dit komt overeen met het Overzicht; de navertelling laat zien dat de lecture vier
verhalen vertelt die alleen het arbitrageargument delen.

## Controle 1

Gecontroleerd tegen `notes/rapport-03_17_termijnstructuur_real_options.md` §F6-1, de
lecture en de nieuwe celuitvoer. `prose_stats`: 5.111 woorden (was 5.402), PASS.
Replicatieblok: 205 woorden.

**Proza tegen cel.** Oefening 2: Monte Carlo 0,82983 met standaardfout 0,00043 tegen
0,83013; $(0{,}83013 - 0{,}82983)/0{,}00043 = 0{,}70$, zoals de tekst zegt ("0,7
standaardfout"). Oefening 4 (koperboom): 0,625; 0,140590; 0,274943; 0,134354, gelijk
aan de toy van F6. LSM-tabel: 4,4779; 3,8443; 4,3299 → 4,4829; SE 0,0094, gelijk aan
F6. Oefening 3: aandeel eerste component 0,93 → 0,91, zoals de tekst zegt. Replicatie,
simulatie en theoriegetallen ongewijzigd.

| punt | status | vindplaats |
|---|---|---|
| Fout 1: Duffie-Kan en Brennan-Schwartz | opgelost | "voegden de lange yield als tweede factor toe, in een model dat alleen numeriek op te lossen is"; Duffie-Kan dekken Vasicek, CIR en Longstaff-Schwartz |
| Eén kernlijn, routekaart | opgelost | "De kernlijn van deze lecture is de termijnstructuur." |
| Toy met twee mechanismen | opgelost | toy alleen de renteboom; koperboom is oefening 4 met tabel hand/code |
| Mijn, McDonald-Siegel, Brennan-Schwartz | opgelost | korte subsectie; tabel en drempel in één dropdown |
| LSM terugbrengen | opgelost | vergelijking voor doorgaan, ondergrens-stelling, één tabel; algoritme, tweede blok en herhalingsfiguur weg |
| Twee replicatieblokken | opgelost | één blok, LSM erin |
| Getallen in de lopende tekst van de replicatie | opgelost | één getal blijft ($t = 1{,}6$, uit de tabel afgeleid) |
| Eén naam voor de lange yield | opgelost | ook in bijschrift en "Wat er brak" |
| Laguerre, Svensson | opgelost | elk een bijzin |
| $a$ tegen $a_0$, $a_1$ | opgelost | "(niet de $a_0$ en $a_1$ van de affiene stelling)" |
| Telegramzin, Santa-Clara-zin, "precies" | opgelost | |
| Chicago en Yale | opgelost | elk een bijzin |
| Parameters in dicts | opgelost | `vas`, `mine` |
| Uitoefenstap `lsm_put`, tekenkeuze PCA | opgelost | benoemde regels |
| Rekenwerk en presentatie LSM | opgelost | herhalingscel weg |
| Oefening 3: aandeel eerste component | opgelost | |

Geen nieuwe feitelijke fouten. Twee kleine verslechteringen:
- Opzet en notatie: "Vasiceks $\alpha$, $\gamma$ en $q$ (niet de kans uit de koperboom)".
  De koperboom staat nu pas in oefening 4; de lezer kent hem hier niet.
- Twee nieuwe puntkomma's in lopende tekst: "wat die over de curve voorspellen; dat
  toetsen simulatie en replicatie" (routekaart) en "een dividend $n(S - a)$ per jaar;
  een gesloten mijn mist dat dividend" (Real options).

Wat blijft voor een 9 op opbouw: de theorie telt nog negen `###`-delen en de replicatie
drie lijnen (curve, PCA, LSM), al zijn mijn en LSM nu kort. Dezelfde aftrek als bij
03_10–03_12 en 03_16.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8,5 | 9 |
| 2 | Opbouw | 7,5 | 8,5 |
| 3 | Taal | 8,5 | 9 |
| 4 | Toy | 8 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 8 | 9 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,70 + 1,70 + 1,35 + 0,90 + 0,90 + 0,90 + 0,45 = 8,90. **Eindcijfer van record
8,9, laagste deelcijfer 8,5.** Streefcijfer gehaald. De twee kleine verslechteringen
kosten nog geen halve punt, maar de schrijver kan ze in één handeling herstellen
(de verwijzing naar de koperboom schrappen, twee puntkomma's splitsen).
