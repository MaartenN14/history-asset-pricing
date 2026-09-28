STATUS 03_11_apt_no_arbitrage F6c-2 words=5419 prose=PASS open=0 cijfer=9,0 min=9

# Eindbeoordeling: Ross, APT en de fundamentele stelling (F6)

## De drie verbeteringen met het meeste effect

1. **Eén kern en één naam** (criteria 1 en 2, 8 → 9). De routekaart zegt "Daarna volgt de kern: de APT van Ross", maar de `###` heet "Het kernresultaat: de fundamentele stelling". Kies één kern. Geef het begrip "pricing error" één naam en één symbool: de theorie schrijft $\eta_i$ ("ook alpha genoemd"), de simulatie $\alpha_i$ en "alpha".
2. **De replicatie laten oordelen over de vraag van Roll en Ross** (criterium 6, 8 → 9). De verwachte afwijking stelt drempels voor PCA en $R^2$, maar niets over het aantal geprijsde factoren. Dat is de vraag uit het blok. Het oordeel "Geslaagd" dekt daardoor niet de uitkomst van één geprijsde component in de cross-sectie tegen "3 à 4". In de tabel origineel/hier zijn vier van de zes cellen onder "origineel" leeg.
3. **Het getal van 200 aandelen per portefeuille herleiden** (feitelijke fout 1). Het argument dat de alpha van 0,09% binnen de Huberman-grens valt, rust erop.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,2** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,15, afgerond 8,2.)

## 1. Helderheid van de uitleg (8)

*Goed.*
- De drie namen van de discontering worden aan het toy-voorbeeld uitgerekend: $m_g = 0{,}6667$, $m_s = 1{,}25$, $\pi^{*}_s = 0{,}5556$, met de zin die zegt waarom de risiconeutrale kans op *slecht* boven 0,4 ligt (Opzet en aannames).
- De exacte APT wordt op de call uit het toy-voorbeeld toegepast: $1{,}50 = 1{,}1111 + 2{,}6875 \cdot 0{,}1447$. Het resultaat krijgt zo een getal dat de lezer al kent.
- De Huberman-grens krijgt twee gevolgen met een getal ($\sqrt{0{,}00002} = 0{,}45\%$ per maand) en een zin die ze samenvat ("Voor wie één aandeel wil prijzen, zegt de APT bijna niets").

*Aanmerkingen.*
- Routekaart van Theorie: "Daarna volgt de kern: de APT van Ross, exact en met ruis." De kop luidt echter "### Het kernresultaat: de fundamentele stelling". De lezer weet niet welke van de twee de kern is.
- De APT met ruis: "Neem de *pricing errors* (het deel van het verwachte rendement dat de factoren niet verklaren, ook alpha genoemd, in de formules $\eta_i$)." In de simulatie heet dezelfde grootheid $\alpha_i$ en "alpha". Eén begrip, twee namen, twee symbolen.
- Opmerking APT en SDF: "Neem $m = a - \mathbf{b}'\mathbf{f}$ met $a = 1/(1+R^{f})$, $\boldsymbol{\Omega} = \Var(\mathbf{f})$ en $\mathbf{b} = a\,\boldsymbol{\Omega}^{-1}\boldsymbol{\lambda}$." Drie symbolen in één zin, zonder getal. Voor het toy-voorbeeld is $m$ na te rekenen, maar dat gebeurt niet.
- Replicatie: "In de Huberman-grens is $N$ het aantal aandelen in een portefeuille". In de stelling is $N$ het aantal activa in de economie. De bewering geldt voor de gelijkgewogen portefeuille van $N$ aandelen, maar dat moet de lezer zelf reconstrueren.

*Beter uitleggen.* Waarom een lineaire $m$ een optie een negatieve prijs kan geven: één getal met het toy-voorbeeld volstaat. Welke $N$ bij de 25 portefeuilles hoort, en waar dat getal vandaan komt.

*Voor een 9.* De kern in de routekaart en de kop gelijktrekken. Eén naam (alpha of pricing error) en één symbool voor het hele stuk. De SDF-opmerking met het toy-voorbeeld narekenen of schrappen.

## 2. Opbouw en rode draad (8)

*Goed.*
- De drie verwachtingen aan het eind van de intuïtie worden alle drie met naam ingelost ("Zoals de intuïtie voorspelde, ligt de optieprijs vast", "telt alleen de factorbèta's", "de derde verwachting uit de intuïtie").
- De toy-getallen keren terug in theorie (q, $m$, $\pi^\ast$, CRR-kans 0,4444, APT met de call) en in oefening 1.
- De simulatie beantwoordt één steekproefvraag, en de figuur maakt beide kanten van de Huberman-grens zichtbaar.

*Aanmerkingen.*
- De kern is volgens de routekaart de APT, volgens de kop de fundamentele stelling (zie 1).
- Theorie heeft zeven `###`-delen. "Veel perioden: de binomiale knoop" levert alleen een brug naar Black-Scholes en de voorwaarde $d < 1 + R^{f} < u$, die oefening 2 opnieuw afleidt.
- De replicatie opent een nieuwe lijn: "De tabel laat zien dat geen van beide modellen de premies goed vangt." Wat Samengevat over de simulatie belooft (portefeuilles zijn goed geprijsd), moet de replicatie daarna wegverklaren.

*Voor een 9.* De kern kiezen. "Veel perioden" terugbrengen tot één alinea met de CRR-kans, of naar oefening 2. In de replicatie vooraf zeggen dat de GRS-toets een tweede vraag is.

## 3. Taal (8)

*Goed.* Gemiddeld 14,1 woorden per zin, geen verboden woorden en geen calques volgens `prose_stats`. De intuïtie is concreet ("Hij heeft vandaag geld en morgen niets te betalen").

*Aanmerkingen.*
- Wat het voorspelt: "Zoals de intuïtie voorspelde, telt alleen de factorbèta's." Het werkwoord hoort meervoud te zijn.
- Definitie: "Een vector *state prices* (toestandsprijzen)". Het toy-voorbeeld had "toestandsprijs" al ingevoerd, en nu komt de Engelse term eerst.
- Replicatie: "Dat is juist wat hun critici aanvoerden." en "Het is geen tegenspraak." Twee korte zinnen die "dat" en "het" laten verwijzen naar een hele alinea.
- Wat er brak: "De fundamentele stelling is geen model dat kan breken, maar de grammatica van elk later model." Beeldspraak zonder uitleg.

*Voor een 9.* De congruentiefout herstellen, "toestandsprijzen" als eerste term in de definitie, en bij "Dat is juist wat hun critici aanvoerden" het ding zelf noemen.

## 4. Toy-voorbeeld (9)

*Goed.* Opzettabel, vijf stappen van één regel, één codecel, tabel hand/code met tien rijen die gelijk zijn. Eén recept ($p = q_g x_g + q_s x_s$), dat Theorie als eerste afleidt. Getallen met noemers onder 100. De slotzin zegt wat de lezer nu weet.

*Aanmerkingen.* De tabel hand/code koppelt een dict aan een lijst op positie (`hand` en `code`). Dat is kwetsbaar, maar raakt de lezer niet.

## 5. Code en figuren (8)

*Goed.* De maandelijkse cross-sectionele regressies in `two_pass` zijn een zichtbare lus. De simulatieparameters staan in een dict. Vóór de figuur staat waarop te letten ("let op de bovenste twee lijnen, die vlak blijven"), en het bijschrift zegt wat te zien is.

*Aanmerkingen.*
- Replicatie: de docstring van `two_pass` eindigt met "TODO: naar hap.stats".
- De PCA-cel doet in twaalf regels sorteren, schalen, tekenkeuze en presentatie. Het schalen (`long_short = np.abs(eigvec[:, 1:n_pc]).sum(axis=0) / 2`) staat in de tekst, maar de tekenkeuze in de lus niet.
- De vergelijkingscel formatteert getallen met `f"{x:.3f}".replace(".", ",")` en zet lege strings in de kolom "origineel".

*Voor een 9.* De TODO verwijderen. De PCA-cel splitsen in rekenwerk en tabel. De tabel origineel/hier zonder lege cellen opbouwen.

## 6. Replicatie en empirie (8)

*Goed.* Het blok is compact en noemt het verschil met het origineel duidelijk (1260 aandelen in 42 groepen, factoranalyse en GLS, tegen 25 portefeuilles en PCA). De verwachte afwijking heeft een toetsbare drempel met foutsignaal. De $R^2$'s van de ene set op de andere maken "rotatie van elkaar" meetbaar.

*Aanmerkingen.*
- De verwachte afwijking zegt niets over het aantal geprijsde factoren, de kern van Roll en Ross. Het oordeel: "Het aantal geprijsde factoren is geen vast getal maar hangt af van de toets." Daarmee is het belangrijkste verschil (1 tegen 3 à 4) achteraf geen afwijking meer.
- In de tabel origineel/hier zijn vier van de zes cellen onder "origineel (Roll en Ross)" leeg.
- Onder de GRS-tabel volgt een argument met getallen in lopende tekst ($c = 0{,}002$, 200 aandelen, 0,32%, 0,09%, 757 maanden).

*Voor een 9.* De verwachte afwijking laten zeggen hoeveel geprijsde componenten er te verwachten zijn, en het oordeel daaraan koppelen. De rijen zonder origineel in een aparte tabel met drempels.

## 7. Oefeningen (9)

*Goed.* Oefening 1 is een instap op het toy-voorbeeld met een derde toestand, met handwerk en `linprog`. Oefening 2 is een afleiding met een expliciete arbitrage. Oefening 3 breidt de replicatie uit naar bedrijfstakken en naar $K = 1$ tot 5. Elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen.* Oefening 3 heeft vier deelvragen over twee verschillende datasets; de uitwerking nummert alleen (4).

## Feitelijke fouten

1. Replicatie, onder de GRS-tabel: "Met de $c = 0{,}002$ uit de simulatie en 200 aandelen per portefeuille is dat $\sqrt{0{,}00001} = 0{,}32\%$ per maand". Het aantal van 200 aandelen per portefeuille komt uit geen cel en geen citatie (niet herleidbaar). De rekensom zelf klopt.

Nagerekend en correct: toy-voorbeeld ($q = (0{,}40;\ 0{,}50)$, 11,1%, 0,16, $\theta = (-0{,}3;\ 0{,}5)$, 0,04), $m$ en $\pi^\ast$, CRR-kans 0,4444, APT met de call (1,2558; 0,3721; 2,6875; 0,1447; 1,50), $\sqrt{0{,}00002} = 0{,}45\%$, simulatie (0,75%, ruim een kwart, 0,0073, 166 en 5,7, RMS 0,89% naar 0,08%), 757 maanden, 83% en 93%, 0,93, zes $R^2$'s boven 0,89, 2,3% per jaar, negatieve marktpremie −0,545, alleen PC3 significant, 0,84% per maand, oefening 1 (lijnstuk en interval (0; 0,16), 0,20 extra in *midden*), oefening 2, oefening 3 (55%, 0,92, 17%, 3%; 0, 2, 1, 1, 3 significante premies).

## Navertelling in vijf zinnen

Geen arbitrage is hetzelfde als het bestaan van strikt positieve toestandsprijzen, en dus van een positieve SDF en een risiconeutrale maat; in een markt met twee toestanden ligt de prijs van een call daardoor vast op 0,16, en elke andere prijs geeft gratis geld. De prijzen zijn alleen uniek in een complete markt; anders geeft arbitrage een interval. Ross paste hetzelfde argument toe op factoren: bij een exacte factorstructuur zijn verwachte rendementen lineair in de factorbèta's, en met eigen ruis per aandeel blijft alleen de som van de gekwadrateerde pricing errors begrensd, zodat gespreide portefeuilles goed geprijsd zijn en losse aandelen niet per se. Een simulatie laat zien dat een los fout geprijsd aandeel met tien jaar data maar in een kwart van de steekproeven wordt gevonden, en dat valse vondsten de echte ver overtreffen. Op de 25 portefeuilles van French vinden drie principale componenten vrijwel dezelfde ruimte als markt, SMB en HML, maar hoeveel factoren een premie dragen, hangt af van de toets.

De navertelling komt overeen met het Overzicht, behalve dat de lezer twijfelt of de fundamentele stelling of de APT de kern is.

## Controle 1

Gecontroleerd tegen `rapport-03_11_apt_no_arbitrage.md` §F6-1 en de huidige lecture. `prose_stats --check`: 5.311 woorden, PASS. `nb_outputs` is identiek aan de vorige versie; alleen de tekst veranderde.

| punt | status | toelichting |
|---|---|---|
| Feitelijke fout 1 (200 aandelen per portefeuille) | opgelost | Vervangen door een getoonde terugrekening: de grens wordt pas overschreden bij $n > 0{,}002/0{,}0009^2 \approx 2469$ aandelen per portefeuille, $25 \times 2469 \approx 61\,700$ in de markt. Nagerekend, klopt. |
| Verbetering 1a: één kern | opgelost | De routekaart noemt de APT nu "wat de stelling voor verwachte rendementen voorspelt"; de kop "Het kernresultaat: de fundamentele stelling" is de enige kern. |
| Verbetering 1b: één naam voor de pricing error | deels | "Pricing error" is nu de naam, met alpha als alias in de simulatie ("de $\eta_i$ van de theorie"). Twee symbolen blijven, zoals opgedragen; in "De APT met ruis" staat "ook alpha genoemd" er nog bij. |
| Verbetering 2: replicatie oordeelt over Roll en Ross | deels | De verwachte afwijking zegt nu dat het aantal geprijsde componenten mag afwijken, en het oordeel is "Gedeeltelijk geslaagd" met de 1 tegen 3 à 4 genoemd. De tabel origineel/hier heeft nog vier lege cellen onder "origineel". |
| Verbetering 3 (= feitelijke fout 1) | opgelost | Zie boven. |
| Naadpunt 6 (Roll 1977) | opgelost | "Dybvig en Ross antwoordden dat het CAPM er niet beter voor staat, omdat de marktportefeuille waarop het steunt niet waarneembaar is {cite}`Roll1977`": een citatie, geen vooruitverwijzing. L14 zegt in "Waar we zijn" dat het bezwaar in de APT-discussie terugkwam en daar begint. |
| Taal: congruentie, *state prices*, "critici" | opgelost | "tellen alleen de factorbèta's"; "toestandsprijzen (*state prices*)"; de zin over de critici noemt het ding zelf. |

Niet gedaan: SDF-opmerking met het toy-voorbeeld, "Veel perioden" inkorten, PCA-cel splitsen, TODO in de docstring van `two_pass` (volgens het rapport vraagt STYLE §5 hem).

**Cijfers na controle 1 (cijfer van record)**

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8 |
| 2 | Opbouw | 8 | 8 |
| 3 | Taal | 8 | 9 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 8 | 8 |
| 6 | Replicatie | 8 | 8 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,2 | **8,3** |

(0,3·8 + 0,2·8 + 0,15·9 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,30.) Helderheid blijft 8 omdat de SDF-opmerking zonder getal staat en de pricing error in de theorie nog twee namen heeft; opbouw blijft 8 omdat "Veel perioden" en de GRS-wending in de replicatie ongewijzigd zijn. Voor 8,5: de SDF-opmerking narekenen met het toy-voorbeeld en "ook alpha genoemd" uit de theorie halen (helderheid naar 9).

## Controle 2

Gecontroleerd tegen `rapport-03_11_apt_no_arbitrage.md` §F6-2 en de huidige lecture. `prose_stats --check`: 5.419 woorden, PASS. In `nb_outputs` zijn alle getallen gelijk; alleen celindeling en tabelvorm veranderden.

| punt uit controle 1 | status | toelichting |
|---|---|---|
| Pricing error: twee namen in de theorie | opgelost | "ook alpha genoemd" is uit "De APT met ruis"; de alias staat alleen in de eerste zin van de simulatie. |
| Lege cellen in de tabel origineel/hier | opgelost | Twee tabellen: drempels tegen hier, en een echte tabel origineel/hier voor het aantal geprijsde componenten (3 à 4 tegen 3 en 1). |
| SDF-opmerking met het toy-voorbeeld | opgelost | Nagerekend: factor +0,3721 en −0,5581, $\Omega = 0{,}6 \cdot 0{,}3721^2 + 0{,}4 \cdot 0{,}5581^2 = 0{,}2077$, $b = 0{,}6271$, $m = 0{,}6667$ en $1{,}25$, drempel $0{,}9/0{,}6271 = 1{,}435$. Klopt. |
| PCA-cel splitsen | opgelost | Rekenwerk en tabel in aparte cellen. |
| GRS als tweede vraag aankondigen | opgelost | "Daarnaast stellen we een tweede vraag: laten de factoren alpha's over?" |
| "Veel perioden" inkorten | afgewezen met reden | De sectie draagt de martingaalvergelijking, die een latere lecture aanhaalt (schraptoets eis 2). Geen aftrek meer. |
| TODO in de docstring van `two_pass` | geen aftrek meer | STYLE §5 vraagt de regel; projectkeuze. |

Kleine verslechtering, zonder effect op het cijfer: de SDF-opmerking heeft nu twee keer "dus" in één alinea ("Een lineaire SDF prijst dus ...", "De APT is dus zwakker"), waar STYLE §11.2 er één toestaat.

**Cijfers na controle 2 (cijfer van record)**

| nr | criterium | controle 1 | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 9 |
| 2 | Opbouw | 8 | 9 |
| 3 | Taal | 9 | 9 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 8 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,3 | **9,0** |
