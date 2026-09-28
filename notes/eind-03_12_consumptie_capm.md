STATUS 03_12_consumptie_capm F6c-2 words=5211 prose=PASS open=0 cijfer=8,7 min=8

# Eindbeoordeling: Lucas, Breeden en de SDF (F6)

## De drie verbeteringen met het meeste effect

1. **Het toy-voorbeeld handrekenbaar maken** (criterium 4, 8 → 9). Stap 2 rekent met noemers 49, 637 en 16/637 en de regel van Cramer. STYLE §11.7 vraagt noemers onder 100. Getallen kiezen waarbij de gewichten eenvoudige breuken zijn, of het stelsel in één regel met afgeronde decimalen oplossen.
2. **De replicatie na het oordeel uit de lopende tekst halen** (criterium 6, 8 → 9). "Onze standaardfout is 6,2, de hunne 1,57 bij een schatting van 1,51" en "een standaardfout van 67 bij Hansen en Singleton ... rond hun 58" herhalen de tabel in proza, met vijf getallen per alinea. Het oordeel kan naar de tabel verwijzen.
3. **De losse eindzin verplaatsen en de brug naar de simulatie verhelderen** (criterium 2, 8 → 9). "In de vraag theorie of feit is het consumptie-CAPM een theorie die met één toets werd verworpen." staat na "Wat er daarna kwam" als losse alinea. In de simulatie-inleiding is "of op ruim één basispunt zoals in het toy-voorbeeld" een vergelijking met een andere economie (Markov-groei, $\gamma = 2$), die de lezer niet kan plaatsen.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,1** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·8 + 0,1·8 + 0,1·8 + 0,05·9 = 8,05, afgerond 8,1.)

## 1. Helderheid van de uitleg (8)

*Goed.*
- Toy-voorbeeld: "In de hoge toestand is de prijs-dividend-ratio *lager*, hoewel de verwachte groei hoger is." De zin daarna noemt het rente-effect en het groei-effect, en oefening 1 leest het resultaat in beide richtingen (H6).
- Wat het voorspelt, lognormale groei: elke formule krijgt een getal met kalibratie ($\gamma < 14{,}7$, 8,6% rente, 0,25% premie), en de rente wordt ontleed in groei en voorzorgssparen.
- Opzet en aannames: de vertaling van Hansen en Singletons $\alpha$ naar $\gamma$ staat vooraf, met het getal ($\hat\alpha = -0{,}931$ is $\hat\gamma = 0{,}931$).

*Aanmerkingen.*
- Simulatie: "Zonder die hefboom bleef de premie steken op $4 \cdot 0{,}035^2 = 0{,}49\%$, of op ruim één basispunt zoals in het toy-voorbeeld." Het tweede deel vergelijkt met een andere economie. Welk scenario "of" beschrijft, is niet te zeggen.
- Evenwicht in de Lucas-boom: "Laat de groei $g_{t+1} = d_{t+1}/d_t$ afhangen van een Markov-toestand $s_t$ met overgangskans $Q(s, \mathrm{d}s')$." De maattheoretische notatie komt één keer voor en wordt meteen weer tot een som teruggebracht.
- Hoe het getoetst wordt: de alinea vóór de GMM-code ("De code volgt de stelling in twee stappen ...") stapelt vier implementatiedetails (concentreren van $\beta$, rooster, $\hat{\mathbf{S}}$ zonder autocovarianties, de kolommen van `D`). De lezer moet ze onthouden tot de code.
- Vergelijking met 1983: "Hun kolom "probability" is de verdelingsfunctie van $\chi^2$, dus .9999 betekent verwerping." De kolom staat niet in de tabel hier; de zin verwijst naar iets wat de lezer niet ziet.

*Beter uitleggen.* Waarom de simulatie een hefboom $\phi = 3$ nodig heeft: één zin met het getal van de premie met en zonder hefboom volstaat, zonder het toy-voorbeeld erbij te halen.

*Voor een 9.* De "of"-bijzin in de simulatie schrappen. De implementatiealinea bij GMM terugbrengen tot wat de lezer nodig heeft om de tabel te lezen, en de rest als commentaar in de code. De zin over "probability" schrappen of de kolom tonen.

## 2. Opbouw en rode draad (8)

*Goed.*
- De routekaart wijst de Euler-vergelijking als kern aan, en de kop "Het kernresultaat: de Euler-vergelijking" bevestigt dat.
- De drie verwachtingen uit de intuïtie worden met naam ingelost: "de eerste voorspelling uit de intuïtie" (rente), "Zoals de intuïtie voorspelde, groeit de premie met de covariantie", "de derde voorspelling uit de intuïtie, nu met een getal".
- De simulatie gebruikt de lognormale boom uit de theorie, en de rente van 8,6% is al in de theorie uitgerekend. De replicatie leest de $\hat\beta > 1$ met de simulatie in de hand.

*Aanmerkingen.*
- Wat er brak: de alinea "In de vraag theorie of feit is het consumptie-CAPM een theorie die met één toets werd verworpen." staat na "Wat er daarna kwam", als losse slotzin.
- Theorie heeft zeven `###`-delen. "Williams met een theorie van de discontovoet" begint met een zin over de stap in plaats van met de bewering ("Deze stap laat zien waarom ...").
- De toy-getallen keren in de theorie terug ($\delta = 0{,}9654$, stap 3 bij de rente), maar de simulatie kiest andere ($\beta = 0{,}98$, $\gamma = 4$). De reden staat erbij, maar de draad van het toy-voorbeeld houdt daar op.

*Voor een 9.* De slotzin over theorie of feit in "Waar het breekt" opnemen. "Williams met een theorie van de discontovoet" laten openen met de bewering: de discontovoet volgt uit $\beta$, $\gamma$ en consumptie.

## 3. Taal (8)

*Goed.* Gemiddeld 13,9 woorden per zin, geen verboden woorden en geen calques volgens `prose_stats`. De intuïtie met het eiland is concreet en heeft een handelend onderwerp ("Wie vandaag een vrucht niet opeet maar belegt").

*Aanmerkingen.*
- Vergelijking met 1983: "In de simulatie verwierp de toets een waar model in één op de tien steekproeven, hier met een $p$-waarde die op vier decimalen nul is." Een frequentie en een $p$-waarde worden als gelijksoortig tegenover elkaar gezet.
- Kop "Williams met een theorie van de discontovoet": geen natuurlijke Nederlandse kop.
- Overzicht: "Het model heet het *consumption CAPM* (hier consumptie-CAPM: ...)". De Engelse term eerst, terwijl de lecture verder alleen de Nederlandse gebruikt.
- Wat er brak: "De Chicago-lezing, die prijzen als rationele beloning voor risico leest: de theorie is juist, maar de specificatie is te arm." Een bijzin plus dubbelepunt plus tegenstelling in één zin.

*Voor een 9.* De vergelijkingszin in "Vergelijking met 1983" herschrijven tot twee zinnen die elk één ding zeggen. Een kop die de bewering noemt ("De discontovoet krijgt een theorie").

## 4. Toy-voorbeeld (8)

*Goed.* Opzettabel met de overgangsmatrix, vier stappen met getallen, één codecel, tabel hand/code met de Euler-controle, en een slotzin die zegt wat de lezer weet. De toy-uitkomst (ratio lager in de hoge toestand) koppelt aan de replicatie van Williams.

*Aanmerkingen.*
- Stap 2: "De regel van Cramer geeft met determinant $\tfrac{4}{13}\cdot\tfrac{13}{49} - \tfrac{12}{49}\cdot\tfrac{3}{13} = \tfrac{16}{637}$". Noemers boven 100; het handwerk kost meer dan vijf minuten.
- Het recept bevat naast $p_t = \E_t[m_{t+1}x_{t+1}]$ ook de recursie voor $\mathrm{PD}_i$. Die volgt uit het recept, maar de lezer krijgt twee formules.
- Het toy-voorbeeld levert drie uitkomsten (PD, rente, premie) met twee mechanismen (rente-effect tegen groei-effect, en de kleine premie).

*Voor een 9.* Een kalibratie met kleinere noemers, of $y_h$ en $y_l$ als decimaal met één regel oplossing.

## 5. Code en figuren (8)

*Goed.* Eén functie `gmm_euler` voor simulatie en replicatie, met de tweestapsprocedure als zichtbare lus. De simulatieparameters staan in een dict (`tree`). Vóór elke figuur staat waarop te letten ("Let in de figuur links op hoe ver de schattingen van de zwarte lijn bij 4 liggen").

*Aanmerkingen.*
- Hoe het getoetst wordt: `np.einsum("tn,tl->tnl", scaled, Z).reshape(T, N * L)` en `a, b = (x.mean(axis=0) for x in euler_moments(gamma, gc, R, Z))`. Compacte constructies waar een lus over activa en instrumenten de Kronecker-stapeling zichtbaar had gemaakt.
- De datacel in "De data" beslaat circa 45 regels: FRED, marktdata, deflatie en de samenvattingstabel in één cel.
- Wat het aandelenrendement alleen vraagt: `roots[label] = (optimize.brentq(...) if crossing.size else np.nan)` is een meerregelige conditionele expressie.

*Voor een 9.* De datacel splitsen in bouwen en samenvatten. De Kronecker-stapeling met een benoemd tussenresultaat of een korte lus.

## 6. Replicatie en empirie (8)

*Goed.* Het blok noemt de tabellen en paginanummers van Hansen en Singleton, en de verwachte afwijking is een patroon met foutsignaal ("Draait (a) of (c) om, dan zit er een fout in de code"). De tabel origineel/hier heeft SE en $p$-waarde. Het oordeel begint met "Geslaagd" en verwijst naar de verwachte afwijking. De waarschuwing over tijdsaggregatie zegt welke kant de fout op gaat.

*Aanmerkingen.*
- Na het oordeel: "Onze standaardfout is 6,2, de hunne 1,57 bij een schatting van 1,51." en "met een standaardfout van 67 bij Hansen en Singleton. ... Het interval rond hun 58". De getallen uit de tabel komen terug in lopende tekst, meer dan drie per alinea.
- In de tabel staat onder "(d) alleen de premie" een origineel van 58,25 met SE, en hier een nulpunt zonder SE. Die rij vergelijkt een schatting met een wortel van een steekproefmoment.

*Voor een 9.* Het oordeel laten verwijzen naar de tabel en de getallen uit de proza halen. Bij rij (d) in een voetnoot zeggen dat "hier" een nulpunt is zonder standaardfout.

## 7. Oefeningen (9)

*Goed.* Oefening 1 varieert het toy-voorbeeld in $\gamma$ en persistentie, oefening 2 is een afleiding met controle op de simulatie, oefening 3 breidt de replicatie uit naar coronakwartalen en jaardata. Elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen.* Oefening 1 heet niet "Instap", hoewel ze dat is; bij oefening 2 zijn deelvragen 2 en 3 samen uitgewerkt.

## Feitelijke fouten

Geen gevonden.

Nagerekend en correct: toy-voorbeeld (9/13, 12/49, 3/13, 36/49; determinant 16/637; 325/16 en 343/16; 19,3125 en 20,4375; 0,924556 en 1,041233; 0,915576 en 0,971581; 9,22% en 2,93%; 1,09385, 1,08783, 1,09235; 1,03364, 1,02795, 1,02937; premies 1,4 en 1,2 bp), ruim zes procentpunt, 3%, $\delta = 0{,}9654$, de afleiding van $\gamma\phi\sigma^2$, $\gamma < 14{,}7$, $\log(1+R^f) = 0{,}0824$ en 8,6%, 0,25%, 0,49% en 1,5%, simulatie (mediaan 2,8; −3 tot 12; SE 1,5 tegen SD 4,2; 9,8%; 11,7 boven 9,49; 29%; $16/\sqrt{70} = 1{,}9$), zestien keer zo volatiel, $\hat\gamma = 17$ en $\hat\beta = 1{,}08$, $\gamma \approx 75$, factor vijf in de standaardfout, oefening 1 ($\beta/(1-\beta) = 24$), oefening 2 (0,0145 en 0,0147; 0,00016; circa 400 jaar), oefening 3 (17, 2, negatief).

## Navertelling in vijf zinnen

De Euler-vergelijking zegt dat een prijs de verwachte payoff is, gewogen met de verhouding van marginale nutten $m_{t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$; dat is de positieve SDF waarvan de fundamentele stelling alleen het bestaan gaf. In een Lucas-boom volgen daaruit een unieke prijs-dividend-ratio, een rente die met verwachte groei stijgt, en een premie $\gamma\phi\sigma^2$ die klein is omdat consumptie glad is. Benaderd wordt dat het consumptie-CAPM: de premie is de consumptiebèta maal $\gamma$ maal de variantie van consumptiegroei. Hansen toetste de Euler-vergelijking met GMM, en een simulatie laat zien dat die toets op zeventig jaar data $\gamma$ slecht meet en een waar model te vaak verwerpt. Op Amerikaanse kwartaaldata verwerpt de toets het model voor aandelen en T-bill samen overtuigend, en de premie alleen vraagt een risicoaversie in de tientallen of is helemaal niet te verklaren.

De navertelling komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen `rapport-03_12_consumptie_capm.md` §F6-1 en de huidige lecture en notebook. `prose_stats --check`: 5.249 woorden, PASS. In `nb_outputs` veranderen alleen de toy-cel en oefening 1; simulatie, replicatie en oefeningen 2 en 3 zijn identiek.

**Toy-voorbeeld, proza tegen cel (herkalibratie $g_l = 0{,}96$).** Alles met de hand nagerekend en gelijk aan de cel: gewichten 9/13, 1/4, 3/13, 3/4; optellen geeft $y_h = 26$, $y_l = 28$, dus PD 25 en 27; SDF 0,8876 en 25/24; $\E_h[m] = 0{,}9261$, rente 7,98%; $\E_l[m] = 1{,}0032$, rente −0,31%; rendementen 1,0816 en 1,0752, verwacht 1,0800 tegen 1,0798 (2,0 bp, code 1,9967); vanuit laag 0,99704 tegen 0,99687 (1,7 bp, code 1,7068); renteverschil 8,29 ("ruim acht"); schommeling 4%; $\delta = 0{,}9808$ in "Evenwicht in de Lucas-boom". Geen oude toy-getallen (19,3; 20,4; 9,22; 2,93; 0,9654; 12/49) meer in de tekst. Oefening 1 gebruikt $g_l = 0{,}96$ en $\gamma \in \{0{,}5; 1; 2; 3\}$; de conclusie in de uitwerking klopt met de nieuwe tabel.

| punt | status | toelichting |
|---|---|---|
| Verbetering 1: toy handrekenbaar | opgelost | Noemers hoogstens 27, oplossing door optellen, geen Cramer. |
| Verbetering 2: replicatie na het oordeel | opgelost | De getallen 6,2 / 1,57 / 1,51 / 67 / 58 zijn uit de proza; de tekst verwijst naar de kolommen met standaardfouten en naar rij (d). |
| Verbetering 3a: losse slotzin | opgelost | De zin over theorie of feit opent nu "Wat er daarna kwam". |
| Verbetering 3b: brug naar de simulatie | opgelost | "of op ruim één basispunt zoals in het toy-voorbeeld" is geschrapt. |
| Naadpunt 4 (14,7 tegen 13,8) | opgelost, met een kleine verslechtering | De bijzin verklaart het verschil met de kalibratie. Maar "met de momenten van {cite:t}`Mehra2003` in [](#03-13-equity-premium-puzzle) wordt het 13,8" haalt een getal uit de volgende lecture naar voren, wat STYLE §11.3 verbiedt ("Geen inhoud uit een latere lecture gebruiken"). De uitleg in L13 volstaat; de bijzin hier kan terug naar alleen 14,7. Geen effect op het cijfer. |

Niet gedaan: de GMM-implementatiealinea inkorten, de zin over de kolom "probability", de kop "Williams met een theorie van de discontovoet".

**Cijfers na controle 1 (cijfer van record)**

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8 |
| 2 | Opbouw | 8 | 8 |
| 3 | Taal | 8 | 8 |
| 4 | Toy-voorbeeld | 8 | 9 |
| 5 | Code en figuren | 8 | 8 |
| 6 | Replicatie | 8 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,1 | **8,3** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·9 + 0,05·9 = 8,25, afgerond 8,3.) Voor 8,5: de GMM-alinea terugbrengen tot wat de tabel nodig heeft en de zin over "probability" schrappen (helderheid naar 9).

## Controle 2

Gecontroleerd tegen `rapport-03_12_consumptie_capm.md` §F6-2 en de huidige lecture. `prose_stats --check`: 5.211 woorden, PASS. `nb_outputs` is op de celnummering na identiek aan controle 1; de toy-getallen uit controle 1 staan ongewijzigd.

| punt uit controle 1 | status | toelichting |
|---|---|---|
| Vooruitverwijzing met 13,8 (STYLE §11.3) | opgelost, met een nieuwe kleine zwakte | Alleen 14,7 bij 1,8%/3,5%, geen L13 en geen 13,8 meer. De ingevoegde zin "Een andere kalibratie geeft een andere drempel." staat nu tussen het getal en "Daarboven wint het voorzorgssparen.", zodat "Daarboven" niet meer naar de vorige zin verwijst (H8). |
| GMM-implementatiealinea | opgelost | Twee zinnen in de tekst; de details staan als commentaar in de code. |
| Zin over "probability" | opgelost | Vervangen door een toelichting bij rij (d): "hier" is een nulpunt zonder standaardfout. |
| Kop "Williams met een theorie van de discontovoet" | opgelost | "De discontovoet krijgt een theorie", met de bewering als eerste zin. |
| Slotzin theorie of feit | opgelost | Sluit nu "Waar het breekt" af. |
| Taal (vergelijkingszin, Engelse term, Chicago-zin) | opgelost | Twee zinnen; "consumptie-CAPM (in de literatuur *consumption CAPM* ...)"; Chicago-lezing gesplitst. |
| Code (Kronecker, generator, `brentq`, datacel) | opgelost | Lus over activa met benoemde blokken; datacel gesplitst in bouwen en samenvatten. |
| Hefboomzin in de simulatie | opgelost | "Met hefboom drie is ze ... drie keer zo groot" ($4 \cdot 3 \cdot 0{,}035^2 = 1{,}47\%$). Klopt. |

Geen nieuwe feitelijke fouten.

**Cijfers na controle 2 (cijfer van record)**

| nr | criterium | controle 1 | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8 |
| 2 | Opbouw | 8 | 9 |
| 3 | Taal | 8 | 9 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 9 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,3 | **8,7** |

(0,3·8 + 0,2·9 + 0,15·9 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 8,70.) Helderheid blijft 8 om de nieuwe verwijzingsfout bij "Daarboven". In L10 kostte een even kleine fout ("Dat getal") in controle 1 hetzelfde. Eén verplaatste zin lost het op.
