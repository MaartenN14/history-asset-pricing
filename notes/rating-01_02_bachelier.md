STATUS 01_02_bachelier F5c words=5453 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling: 01_02_bachelier (F5a)

Gelezen als eerstejaars PhD-student die L0 en L1 heeft gelezen. Ter controle van de
aansluiting: "Waar we zijn" en "Wat er brak" van 00_01_rendementen en 01_03_williams_ddm.
De aansluiting klopt: L1 sluit af met Regnault in 1863, "37 jaar vóór Bachelier", en deze
lecture opent daarmee; L3 opent met "prijsveranderingen zijn vrijwel onvoorspelbaar ...
Cowles ... Kendall ... een theorie van de ruis, maar geen theorie van het koersniveau",
precies wat hier in "Waar het breekt" staat.

`prose_stats`: 5.407 woorden (onder 5.500, maar krap), gemiddelde zinslengte 15,3, geen
zin boven 40 woorden, 15 puntkomma's, één stopwoord, één Engels citaat, PASS.

## Eindcijfer: 8,2

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,15, afgerond 8,2.

## 1. Helderheid van de uitleg: 8

*Goed*
- **Opzet en aannames**: de notatiewissel ("*Vanaf hier zijn kleine letters logs*") en de
  Bachelier-volatiliteit $v$ krijgen naam, eenheid en orde van grootte ("bij een aandeel
  van 100 met 20% volatiliteit ongeveer 20 euro").
- **Het kernresultaat**: $\E|Z| = \sqrt{2/\pi}$ wordt in één regel afgeleid en direct
  teruggekoppeld aan het toy ("vier stappen zitten nog 6% onder de limiet").
- **Hoe het getoetst wordt**: de standaardfout van $VR(q)$ wordt voor $q = 2, 4, 8, 16$
  uitgerekend bij de 1216 weken van Lo en MacKinlay; het motief "de standaardfout van 2%"
  wordt ter plekke uitgelegd ("Een toets die alleen varianties vergelijkt, heeft daardoor
  scherpte").

*Aanmerkingen*
- **Het kernresultaat, *Waarom zou dit waar zijn?***: "De uitschieters van losse dagen
  middelen weg, en zijn maandrendement wordt normaal verdeeld, hoe scheef de dagrendementen
  ook zijn." Dat klopt alleen bij onafhankelijke dagrendementen; L1 liet zien dat
  maandrendementen een extra kurtosis van 6,5 hebben, en deze lecture zegt zelf in de
  replicatie dat "wisselende volatiliteit ... maandveranderingen dikke staarten" geeft (zie
  Feitelijke fouten).
- **Replicatie Regnault, oordeel**: "Dan is de gemiddelde absolute afwijking klein ten
  opzichte van de standaarddeviatie: bij één maand is $\E|\cdot|/\SD$ gelijk aan $0{,}71$,
  bij twaalf maanden $0{,}73$ ... Zo start de extrapolatie van Regnault te laag." De
  redenering waarom een *stijgende* verhouding de extrapolatie te laag laat starten, moet de
  lezer zelf afmaken.
- **Overzicht / Intuïtie**: "afwijking" wordt losjes gebruikt ("de afwijking groeit met de
  wortel van de tijd", "1,41 keer zo veel afwijking"), terwijl Stap 3 afspreekt dat
  $\E|\cdot|$ de gemiddelde absolute afwijking is en "spreiding" de standaarddeviatie.

*Beter uitleggen*
- De kurtosis-kanttekening bij de intuïtie: één bijzin dat de benadering geldt bij
  onafhankelijke stappen, en dat clusterende volatiliteit haar vertraagt.
- De Regnault-afwijking: één zin die de twee getallen aan elkaar knoopt (bij één maand
  ligt $\E|\cdot|$ relatief lager dan bij twaalf, dus maal $\sqrt{12}$ onderschat).

*Voor een 9*
- Het kernresultaat, *Waarom zou dit waar zijn?*: "wordt normaal verdeeld" beperken tot
  onafhankelijke stappen.
- Replicatie Regnault: de laatste stap van de redenering uitschrijven, met de juiste
  0,70.
- Overzicht en Intuïtie: "afwijking" en "spreiding" gebruiken zoals Stap 3 ze vastlegt.

## 2. Opbouw en rode draad: 8

*Goed*
- **Overzicht**: vraag ("Hoe beweegt een koers als niemand de volgende stap kan
  voorspellen?") en antwoord (wortel van de tijd, optie uit de afwijking, niets over het
  niveau) in drie zinnen.
- **Intuïtie → Theorie → Replicatie**: drie voorspellingen, waarvan de theorie er twee
  zichtbaar inlost ("Zoals de intuïtie voorspelde") en de replicatie de derde ("De
  voorspelling uit de intuïtie, autocorrelaties van nul, houdt dus bijna stand").
- **Dezelfde getallen**: de 1216 weken van Lo en MacKinlay lopen van theorie via simulatie
  naar replicatie; het toy wordt ook gebruikt voor het reflectieprincipe (0,375).

*Aanmerkingen*
- **Wat het voorspelt: de kans om een niveau te raken**: het reflectieprincipe heeft een
  stelling, een bewijs en een codecel, maar komt in simulatie, replicatie en "Wat er brak"
  alleen als opsomming terug. Het is een zijtak.
- **Replicatie op echte data**: twee replicaties met elk een admonition, oordeel, tabel en
  figuur. Samen met de lengte van 5.407 woorden, net onder de grens, maakt dat de
  empirie het zwaarste deel; de kern (de random walk als feit zonder niveau) komt pas in
  "Wat er brak" terug.
- **Hoe het getoetst wordt**: opent met "De random walk toetsen we op twee manieren", een
  aankondiging, niet de conclusie van de subsectie.

*Beter uitleggen*
- Waarom de raakkans in deze lecture staat: één zin die haar aan de replicatie of aan
  Bacheliers barrièreopties koppelt, of haar inkorten.

*Voor een 9*
- Reflectieprincipe: inkorten tot resultaat plus toy-controle, of een rol geven in de
  rest van de lecture.
- Hoe het getoetst wordt: openen met de conclusie (de variance ratio bundelt kleine
  autocorrelaties en gebruikt alleen varianties).

## 3. Taal: 8

*Goed*
- Korte zinnen (gemiddeld 15,3, geen boven 40 woorden), geen u/je, geen calques.
- Franse citaten staan als blokcitaat of cursief met Nederlandse inleiding of uitleg
  (Regnaults wet, *l'espérance mathématique du spéculateur est nulle*).
- **Simulatie**: "*onderscheidend vermogen*, de kans dat de toets de foute nulhypothese
  verwerpt" voert een Nederlandse term in en houdt hem vast.

*Aanmerkingen*
- **Overzicht**: "Bachelier definieert het tijdvak, omdat hij als enige een model gaf
  waaruit de meting volgt." Projecttaal, dezelfde als in L3.
- **Wat er brak**: "**Waar het breekt.** Vooral hier: de random walk zegt iets over
  *veranderingen*". "Vooral hier" is een stopwoord zonder verwijzing.
- 15 puntkomma's, twee keer zoveel als in L1 en L3; bijvoorbeeld "Het recept. ... nadert
  die verhouding $\sqrt{2/\pi} \approx 0{,}798$; de theorie leidt dat als eerste af" en "De
  afwijking is verdwenen; een omgekeerd teken is niet aangetoond".
- "afwijking" voor twee begrippen (zie criterium 1).

*Voor een 9*
- Overzicht: "definieert het tijdvak" vervangen door wat er gebeurt.
- Wat er brak: "Vooral hier:" schrappen.
- De puntkomma's in Toy, Replicatie en Wat er brak vervangen door punten.

## 4. Toy-voorbeeld: 9

*Goed*
- Zestien paden, in vijf minuten met de hand te tellen; variantie en $\E|S_n|$ per stap.
- Eén nog niet afgeleide formule ($\sqrt{2/\pi}$), als zodanig aangekondigd.
- Tabel hand/code en één zin wat de lezer nu weet; het toy keert terug bij het
  reflectieprincipe en bij de Donsker-limiet.

*Aanmerkingen*
- De kolom `E|S_n| / sqrt(n)` staat in de code-tabel maar niet in de handkolommen; de
  handwaarden staan alleen in Stap 4. Klein.

## 5. Code en figuren: 8

*Goed*
- Elke cel heeft een zin ervoor en erna; vóór elke figuur staat waarop te letten ("Let op
  de bundel, niet op één pad", "Let op waar de lijnen de verticale lijn van Lo en MacKinlay
  kruisen").
- `ar1_paths` toont de AR(1)-recursie als zichtbare lus; `bachelier_call` leest als
  [](#eq-bachelier-call).
- Het bijschrift bij de power-figuur trekt een les ("Wie beweert dat een markt efficiënt
  is, zegt dus altijd: met de data die ik heb").

*Aanmerkingen*
- **Replicatie Regnault, tabel**: kolomnamen `"E|dev|"`, `"SD(dev)"`, `"nobs"`,
  `"Regnault: E|dev|(1)*sqrt(h)"` zijn code-notatie in een presentatietabel.
- **Replicatie Kendall, tabel**: `"rho_1"` ... `"rho_5"`, `"SE onder H0"`, `"nobs"`.
- **Vergelijkingscel Lo-MacKinlay**: tupels `(origineel, hier, z origineel, z hier)` in
  een dict met regels van meer dan 100 tekens; leest als een truc, niet als een tabel.

*Voor een 9*
- Regnault- en Kendall-tabel: kolomnamen in woorden ("gem. absolute afwijking",
  "standaarddeviatie", "waarnemingen", "$\rho_1$").
- Vergelijkingscel: de originelen als eigen kleine tabel of lijst per kolom.

## 6. Replicatie en empirie: 8

*Goed*
- Beide admonitions zijn compleet en noemen een falsifieerbare eis (factor twee; de
  rangorde over kwintielen).
- Beide oordelen beginnen met "Geslaagd ... gedeeltelijk geslaagd" en koppelen aan de
  verwachte afwijking.
- Tabel origineel/hier bij beide; de naoorlogse en interbellum-steekproef geven context
  zonder het oordeel te verwateren.

*Aanmerkingen*
- **Replicatie Regnault, oordeel**: "De French-helling van 0,511 ... De Shiller-helling van
  0,577 ... ($0{,}0529 \cdot \sqrt{12} \approx 0{,}183$ tegen $0{,}199$) ... $0{,}71$, bij
  twaalf maanden $0{,}73$, tegen $0{,}80$". Acht getallen in één alinea.
- **Replicatie Kendall**: "Onze eerste weekautocorrelatie is $0{,}030$, onder de ongeveer
  $0{,}13$ ... $0{,}085$ bij een standaardfout van $0{,}029$ ... 0,7%" en in de VR-alinea
  "$VR(2) = 0{,}950$ met $z = -1{,}2$". Getallen die in de tabellen staan, herhaald in
  proza.

*Voor een 9*
- Beide oordelen: naar de tabel verwijzen en hoogstens de getallen noemen die het oordeel
  dragen (helling; rangorde).
- Regnault: de verhouding $\E|\cdot|/\SD$ als kolom in de tabel in plaats van in proza.

## 7. Oefeningen: 9

*Goed*
- Instap varieert het toy (scheve munt) en verbindt de uitkomst met een keuze in de
  replicatie (gemiddelde aftrekken).
- Oefening 1 is een afleiding (gesloten $VR(q)$ voor een AR(1)); oefening 3 breidt de
  replicatie uit naar na 1986.
- Elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen die het cijfer drukken.

## De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9)**: "wordt normaal verdeeld" in de intuïtie van het kernresultaat
   beperken tot onafhankelijke stappen, de Regnault-redenering over $\E|\cdot|/\SD$
   afmaken (met 0,70), en "afwijking" en "spreiding" gebruiken zoals Stap 3 ze
   vastlegt. Eindcijfer +0,3.
2. **Opbouw (8 → 9)**: het reflectieprincipe inkorten of een rol geven, en "Hoe het
   getoetst wordt" met de conclusie openen. Eindcijfer +0,2.
3. **Taal (8 → 9)**: "definieert het tijdvak" en "Vooral hier:" weg, puntkomma's naar
   punten. Eindcijfer +0,15.

## Navertelling in vijf zinnen

Regnault mat in 1863 dat de koersafwijking met de wortel van de tijd groeit, en
Bachelier gaf daar in 1900 een model voor: de random walk, die in de limiet een Brownse
beweging wordt. Daaruit volgen de kans om een niveau te raken en een optieprijs die
evenredig is met $v\sqrt{\tau}$ en voor korte looptijden nauwelijks van Black-Scholes
verschilt. De toets is de variance ratio, die kleine autocorrelaties bundelt maar, zoals
de simulatie laat zien, tientallen jaren data nodig heeft. Op echte data houdt de
$\sqrt{t}$-wet stand (helling 0,51) en zijn autocorrelaties klein; de variance ratios van
Lo en MacKinlay boven één, sterker bij kleine ondernemingen, repliceren en zijn na 1985
grotendeels verdwenen. Het model zegt niets over het niveau van de koers, en of de
afwijkingen risico of vergissing zijn, beslissen de gratis data niet.

Dit komt overeen met het Overzicht.

## Feitelijke fouten

Nagerekend met `uv run python` op `hap.data`, met dezelfde toevalsgenerator in dezelfde
volgorde als de lecture. Kloppen: toy (Var 4; $\E|S_n|$ = 1; 1; 1,5; 1,5; verhoudingen
1,000 / 0,707 / 0,866 / 0,750; $\sqrt{8/\pi} = 1{,}60$), reflectie (0,375 geteld en
gespiegeld; 31% en 62%), optie (7,98; maand hooguit 0,027 verschil; jaar 110: −0,34 op
3,96), $1/\sqrt{1200} = 0{,}029$, $VR(4) = 1{,}15$, LM-standaardfouten (0,029 / 0,054 /
0,085 / 0,126), simulatie onder H0 (1,000; 0,0281; 0,0287; 4,3%), power (grootste afwijking
bij vijf jaar 2,8 pp; $T^*$ 96 / 1537 / 9604), Regnault (2,73·√3 = 4,73, 2,73·√12 = 9,46;
hellingen 0,511 en 0,577; French-kolom 0,037–0,042; jaar 11,5% te laag; 0,183 tegen
0,199), autocorrelaties (week 0,030 op 5223 weken; maand 0,085), VR op LM-steekproef
(1,066 / 1,150 / 1,219 / 1,211, $z$ 1,63 / 2,00 / 1,84 / 1,22), na 1986 (0,950, $z = -1{,}2$),
interbellum (574 weken), kwintielen (1,205 → 1,016, monotoon ook bij $q$ = 4 en 8), Wat
er brak (91 maanden; 4270 weken), oefening 1 (1,222; 1,4151; $z$ 4,51 en 3,29), oefening 3
(1,143 → 1,017; $z$ 2,50; max $t$ 1,28; 280 en 487 maanden; 0,075).

1. **Replicatie Regnault, oordeel**: "bij één maand is $\E|\cdot|/\SD$ gelijk aan
   $0{,}71$". Nagerekend: $0{,}0373/0{,}0529 = 0{,}7048$, afgerond **0,70**. (Bij twaalf
   maanden klopt 0,73.)
2. **Het kernresultaat, *Waarom zou dit waar zijn?***: "zijn maandrendement wordt normaal
   verdeeld, hoe scheef de dagrendementen ook zijn." Voor echte maandrendementen onjuist:
   de extra kurtosis van het maandelijkse logrendement is 6,5 (L1, nagerekend op
   `market_monthly`), omdat dagrendementen niet onafhankelijk zijn (clusterende
   volatiliteit, die deze lecture zelf in de replicatie noemt).

Niet nagegaan: Kendalls gemiddelde eerste weekautocorrelatie van "ongeveer 0,13" en de
originelen uit Lo en MacKinlay tabel 1a en 2 (niet in de repository).

## Controle 1

Alleen de eigen punten nagekeken, op de huidige `lectures/01_02_bachelier.md`.
`prose_stats`: 5.453 woorden, 0 puntkomma's, PASS. De `engquote`-telling (2) komt van
kolomnamen tussen aanhalingstekens in code, niet van Engelse citaten.

| crit. | punt | status | vindplaats nu |
|---|---|---|---|
| 1 | "maandrendement wordt normaal verdeeld" (feitelijke fout 2) | opgelost | Het kernresultaat: "Zijn die onafhankelijk, dan ... bij benadering normaal verdeeld. Clusterende volatiliteit vertraagt dat, zoals de replicatie laat zien." |
| 1 | E\|·\|/SD 0,71 (feitelijke fout 1) en onafgemaakte redenering | opgelost | Replicatie Regnault, oordeel: "stijgt van 0,70 bij één maand naar 0,73 ... Regnault neemt die lage maandverhouding mee naar de jaarhorizon, waar ze hoger ligt. Daardoor valt zijn jaarwaarde te laag uit." |
| 1/3 | "afwijking" en "spreiding" door elkaar | opgelost | Overzicht, Intuïtie en oefeningen gebruiken nu "spreiding" voor de standaarddeviatie en "gemiddelde absolute afwijking" voor E\|·\| |
| 2 | reflectieprincipe is een zijtak | deels | het krijgt nu een rol ("het eerste resultaat dat de verdeling van het hele pad nodig heeft ... Daarom vroeg de stelling van Donsker meer"); stelling, bewijs en codecel staan er nog volledig |
| 2 | "Hoe het getoetst wordt" opent met aankondiging | opgelost | "De hoofdtoets is de variance ratio. Ze bundelt veel kleine autocorrelaties en gebruikt alleen varianties" |
| 3 | "definieert het tijdvak" | opgelost | "Zonder Bachelier was Regnaults regel een meting gebleven." |
| 3 | "Vooral hier:" | opgelost | "De zwaarste breuk:" |
| 3 | 15 puntkomma's | opgelost | 0 |
| 5 | kolomnamen Regnault-tabel | deels | "waarnemingen", "standaarddeviatie", "gem. abs. afwijking" zijn beter; "Regnault: maand x sqrt(h)" en "gem. abs. afw. / sqrt(h)" blijven afgekort |
| 5 | kolomnamen Kendall-tabel | opgelost | "waarnemingen", "standaardfout bij random walk", "ρ(1)" ... |
| 5 | vergelijkingscel met tupels | opgelost | originelen als lijsten `original`, `original_z` per kolom |
| 6 | getallen in Regnault-oordeel | deels | 0,183 tegen 0,199 is weg, $\E\|\cdot\|/\SD$ staat nu als kolom in de tabel; de hellingen en 0,70 / 0,73 / 0,80 staan nog in de tekst, maar dragen het oordeel |
| 6 | getallen in Kendall- en VR-alinea's | opgelost | 0,030 en "$VR(2) = 0{,}950$ met $z = -1{,}2$" zijn weg; alleen 0,085 en Kendalls 0,13 blijven |

Geen verslechteringen en geen nieuwe feitelijke fouten. De drie punten die deels zijn
opgelost, gaan over details binnen een criterium dat verder in orde is. Ze drukken de
deelcijfers niet onder 9. Zo is ook in L1 met een punt dat deels was opgelost omgegaan.

### Deelcijfers na controle 1

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |

**Eindcijfer: 9,0** (was 8,2). Laagste deelcijfer 9. Open feitelijke fouten: 0 (beide opgelost).
