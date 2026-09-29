STATUS 03_11_apt_no_arbitrage F6c words=5763 prose=PASS open=0 cijfer=9,2 min=9

**Eindcijfer van record: 9,2** (F6c). Verloop: Vorig: 9,0. Ronde 9+: T, F6 9,0 (1 feitfout) -> F6c 9,2 (plafond 9,3). Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Eindbeoordeling: Ross, APT en de fundamentele stelling (F6)

## Ronde 9+

Vorige ronde: 9,0

Gelezen na de taalredactie (notes/taal-03_11_apt_no_arbitrage.md). `prose_stats --check`: 5.712 woorden, PASS. De twee zinnen boven 40 woorden die `prose_stats` telt, zijn splitsartefacten (een getal met punt vóór een zin, r. 336–340, 1238–1240, en het replicatieblok). De langste echte zin telt 38 woorden (r. 87–89). Alle getallen in de proza zijn nagerekend tegen `nb_outputs`. De redactie heeft geen vakterm van betekenis veranderd: "prijst/geprijsd" werd "waardeert juist / verkeerd gewaardeerd", "geprijsde factoren" werd "factoren met een premie", en beide vervangingen zijn inhoudelijk juist. Wel ontstond daardoor een naamsverschil tussen proza en tabellen (punt 1 hieronder). Oordeel: de taal is niet verslechterd, maar vloeiender geworden (35 verbindingswoorden tegen 16, gemiddeld 16,3 woorden per zin tegen 14,3). Een handvol zinnen klinkt nog stroef.

## De drie verbeteringen met het meeste effect

1. **Eén naam voor "verkeerd gewaardeerd" en "met een premie", ook in tabellen en legenda** (helderheid 9 → 9,5). De proza zegt na de redactie "verkeerd gewaardeerd", "juist gewaardeerd" en "componenten met een premie", maar de simulatietabel en de figuur zeggen "verworpen, fout geprijsd", "verworpen, goed geprijsd" en "alpha van een fout geprijsd aandeel" (lectures/03_11_apt_no_arbitrage.md:724–725, 745), en de vergelijkingstabel zegt "geprijsde componenten" (:1046–1048). Tabellen en figuurteksten zijn lezerstekst; de labels moeten de woorden van de proza volgen.
2. **De martingaalzin corrigeren** (helderheid blijft 9,5 alleen met deze correctie; feitelijke fout 1). Na [](#eq-apt-no-arbitrage-martingaal), dat een dividend bevat, staat "De prijs, gemeten in spaarrekeningen, is dus een *martingaal*" (:413). Met dividend is dat onjuist.
3. **Vijf stroeve zinnen herschrijven** (taal 9 → 9,5). Zie de hardop-toets onderaan en de aanmerkingen bij taal (:545–546, :919–921, :868–869, :67, :578–581).

## Cijfers F6, vóór herstel (niet het eindcijfer)

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **9,0** |

(0,25·9 + 0,2·9 + 0,2·9 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 9,0.) Geen deelcijfer onder 8,5; taal boven 8.

## 1. Helderheid van de uitleg (9)

*Goed.*
- Opzet en aannames: de drie namen van de discontering worden aan het toy-voorbeeld uitgerekend ($m_g = 0{,}6667$, $m_s = 1{,}25$, $\pi^{*}_s = 0{,}5556$), met de reden waarom de risiconeutrale kans op *slecht* boven 0,4 ligt.
- Wat het voorspelt: de exacte APT wordt op de call toegepast ($1{,}50 = 1{,}1111 + 2{,}6875 \cdot 0{,}1447$), en de opmerking APT en SDF rekent de lineaire SDF na tot exact 0,6667 en 1,25 en geeft de drempel 1,435 waarboven $m$ negatief wordt.
- De APT met ruis: de Huberman-grens krijgt twee gevolgen met richting, en het eerste met een getal (0,45% per maand bij $N = 100$).

*Aanmerkingen.*
- Veel perioden: "De prijs, gemeten in spaarrekeningen, is dus een *martingaal*." Na een vergelijking met $d_{t+1}$ geldt dat alleen voor prijs plus herbeleggd dividend (feitelijke fout 1).
- Wat het voorspelt: "Heeft die een positief verwacht rendement, dan koopt hij er onbeperkt van tot dat rendement nul is." Tussen "een handelaar" en "hij" staat een zin met "zo'n portefeuille" als laatste zelfstandig naamwoord, en "portefeuille" wordt elders in het college ook "hij" (:98–99, :462–463). "Hij" is niet eenduidig (H8).
- Simulatie en Replicatie tegen de proza: "verworpen, fout geprijsd" en "geprijsde componenten, cross-sectie" naast "verkeerd gewaardeerd" en "componenten met een premie" (H7, zie verbetering 1).
- Overzicht en definitie: de SDF wordt twee keer volledig gedefinieerd, "(SDF, de willekeurige variabele waarmee payoffs van morgen worden verdisconteerd)" (:37–38) en opnieuw in de definitie (:221–222). [onderzoek B]

*Beter uitleggen.* Intuïtie: "Had hij toch een hoog verwacht rendement" (:99) zegt niet waarmee "hoog" vergeleken wordt; voor een bijna risicovrije portefeuille is de maatstaf de rente. Eén woord ("hoger dan de rente") volstaat.

## 2. Opbouw en rode draad (9)

*Goed.*
- Overzicht stelt de vraag en geeft het tweeledige antwoord met de prijs ervan ("de stelling zegt niet welke discontofactor het is, en de APT zegt niet welke factoren").
- De drie verwachtingen uit de intuïtie worden elk op hun plek ingelost, telkens anders verwoord (:339–340, :494–495, :618–620).
- De toy-getallen keren terug in theorie ($\mathbf{q}$, $m$, $\pi^{*}$, CRR-kans 0,4444, APT met de call, lineaire SDF) en in oefening 1; de $c = 0{,}002$ uit de simulatie keert terug in de replicatie.

*Aanmerkingen.*
- Theorie, routekaart: "We leiden vier dingen af. Eerst bewijzen we … Daarna gaan we na … Vervolgens leiden we af … We sluiten af met …" Een mechanische opsomming; de routekaart zegt niet wat de kern is. [onderzoek B]
- Uniciteit en Replicatie: "([](#ex-apt-no-arbitrage-1) laat dat met getallen zien)" (:396) en "([](#ex-apt-no-arbitrage-3))" (:1056). Oefeningslabels zijn volgens kaart §3 geen linkdoel; de taalredacteur meldde dit al.

*Beter uitleggen.* Niets wezenlijks; lengte 5.712 woorden, binnen de grens.

## 3. Taal (9)

*Goed.* De redactie verbond het staccato met want, zodat en maar (Intuïtie, Toy-voorbeeld, Wat er brak) zonder de betekenis te verschuiven. Geen calques, geen gedachtestreepjes of puntkomma's, "In woorden:" twee keer, motiefnamen elk hoogstens één keer en nergens als handelend onderwerp; "de standaardfout van 2%" (:780) zegt ter plekke wat het motief hier betekent.

*Aanmerkingen.*
- De APT met ruis: "Wie dat uitsluit, sluit dus niet uit dat één aandeel fors verkeerd gewaardeerd is, maar alleen dat veel aandelen dat allemaal zijn." De ontkenning loopt door in het tweede deel, waar een bevestiging bedoeld is. [onderzoek B, deels opgelost]
- Replicatie: "Of de twee sets dezelfde ruimte opspannen, meet de $R^2$ van de ene set op de andere." Voorop geplaatst lijdend voorwerp; hardop leest "de $R^2$" eerst als onderwerp van "meet" en dan als lijdend voorwerp.
- Replicatie: "De vorige cel rekent alleen, en de tabel hieronder zet de eigenwaarden en het aandeel in de variantie op een rij." Metazin over de cel. [onderzoek B]
- Overzicht: "Op de vraag theorie of feit staan hier twee soorten uitspraken naast elkaar." Stroeve voorzetselconstructie rond de motiefnaam. [onderzoek B, sjabloon]
- De APT met ruis: "Het bewijs, van {cite:t}`Huberman1982`, schaalt …" De komma's zetten "van Huberman" als losse bijstelling.

*Beter uitleggen.* Zie de hardop-toets onderaan; elk van deze zinnen is met een herschrijving van de bestaande zin op te lossen.

## 4. Toy-voorbeeld (9)

*Goed.* Opzettabel, vijf genummerde stappen met één regel rekenwerk, één recept dat Theorie als eerste afleidt, een tabel hand/code met tien gelijke rijen, en een slotzin die zegt wat het getal betekent (twee activa leggen de callprijs vast, de kansen 0,6 en 0,4 speelden geen rol).

*Aanmerkingen.* Geen die het cijfer raken.

## 5. Code en figuren (9)

*Goed.* `two_pass` toont de maandelijkse cross-sectionele regressies als lus; de simulatieparameters staan benoemd in één dict; de figuur met de pricing errors heeft een leeswijzer vooraf en een bijschrift dat zegt wat te zien is; de gewichtenfiguur van PC1–PC3 wordt in het bijschrift gelezen.

*Aanmerkingen.*
- Simulatie: "De figuur zet de twee kanten van de Huberman-grens naast elkaar. Let vooral op de bovenste twee lijnen, die vlak blijven, en de onderste twee, die dalen." De leeswijzer staat in dezelfde alinea als de conclusie over de standaardfout (:734–737). [onderzoek B]
- Tabel- en legendalabels "fout geprijsd", "goed geprijsd", "geprijsde componenten" volgen de proza niet meer (verbetering 1).

## 6. Replicatie en empirie (9)

*Goed.* Blok met bron, wat, data, verschil en verwachte afwijking; twee tabellen (vooraf gestelde drempels tegen hier, en origineel tegen hier voor het aantal componenten met een premie); oordeel "Gedeeltelijk geslaagd" gekoppeld aan wat vooraf mogelijk werd geacht; de uitleg waarom een alpha van 0,09% de simulatie niet tegenspreekt, met een getoonde terugrekening.

*Aanmerkingen.*
- Replicatie: "Met de $c = 0{,}002$ uit de simulatie overschrijdt een alpha van 0,09% per maand die grens pas bij …" De $c$ is een simulatiekeuze; het sterkere argument is dat de grens zonder bekende $c$ voor 25 portefeuilles niets verbiedt. De alinea bevat bovendien vijf getallen ($c$, 0,09%, 2469, 61 700, 757). [onderzoek B]

## 7. Oefeningen (9)

*Goed.* Instap (incomplete markt op het toy, met `linprog` als controle en de super-replicatie als bovengrens), afleiding (CRR-kans en de voorwaarde $d < 1 + R^{f} < u$ met expliciete arbitrage), uitbreiding van de replicatie (49 bedrijfstakken en $K = 1$ tot 5). Elke uitwerking eindigt met wat ze leert, na de redactie in een gewone slotzin.

*Aanmerkingen.* Geen die het cijfer raken.

## Feitelijke fouten

Nagerekend tegen `$TEMP/F6-03_11_apt_no_arbitrage-out.txt`: toy (0,40; 0,50; 1,1111; 0,16; −0,3; 0,5; 0,04), $m$ en $\pi^{*}$, CRR-kans 0,4444, $\lambda_1 = 0{,}1447$, $\beta_{\text{call}} = 2{,}6875$, $\Omega = 0{,}2077$, $b = 0{,}6271$, drempel 1,435; simulatie (SE rond 0,75%, verwerping 26–28%, 3180 × 0,052 ≈ 166, 20 × 0,284 ≈ 5,7, RMS 0,89% naar 0,08%); replicatie (1963-07 tot 2026-07, 757 maanden, 83% en 93%, correlatie 0,93, alle $R^2$ boven 0,89, PC1–PC3 significant en PC4–PC5 niet, SE PC1 × 12 ≈ 2,3%, constante 0,84%, marktpremie −0,545 in het driefactormodel, alleen PC3 significant, gem. |alpha| 0,088, 2469 en 61 700); oefeningen ((0; 0,16), 0,20 extra in *midden*, 55%, 83%, 0,92, 17%, 3%, significante premies 0, 2, 1, 1, 3, constante significant bij $K = 1$). Alles juist.

1. Veel perioden (:413–414): "De prijs, gemeten in spaarrekeningen, is dus een *martingaal*." Uit [](#eq-apt-no-arbitrage-martingaal) volgt dat alleen zonder dividend; met dividend is de waarde van prijs plus herbeleggd dividend, gemeten in spaarrekeningen, de martingaal. Ook moet erbij dat het om de verwachting onder $\boldsymbol{\pi}^{*}$ gaat. Onjuist (oud, niet door de redactie ingevoerd). Correctie: "Zonder dividend is de prijs, gemeten in spaarrekeningen, dus een martingaal onder $\boldsymbol{\pi}^{*}$."

## Navertelling in vijf zinnen

Geen arbitrage is precies hetzelfde als het bestaan van strikt positieve toestandsprijzen, en dus van een positieve SDF en, met een risicovrij activum, een risiconeutrale maat; in het toy-voorbeeld legt dat de call vast op 0,16. Die prijzen zijn alleen uniek in een complete markt; in een incomplete markt geeft arbitrage een interval, en over veel perioden wordt de verdisconteerde prijs een martingaal. Ross paste hetzelfde argument toe op factoren: met een exacte factorstructuur zijn verwachte rendementen lineair in de factorbèta's, en met eigen ruis blijft alleen de som van de gekwadrateerde pricing errors begrensd, zodat gespreide portefeuilles juist gewaardeerd zijn en losse aandelen niet noodzakelijk. De simulatie laat zien dat een los verkeerd gewaardeerd aandeel met tien jaar data onzichtbaar blijft, terwijl de fout van een gespreide portefeuille verdwijnt. Op de 25 Fama-French-portefeuilles vinden principale componenten drie richtingen die de ruimte van Mkt, SMB en HML opspannen, maar hoeveel ervan een premie dragen hangt van de toets af, en beide modellen laten alpha's over die de APT niet verbiedt. Dat komt overeen met het Overzicht.

## Taal na de redactie: hardop-toets

De redactie heeft niets verslechterd; het college leest hardop grotendeels als gesproken Nederlands. Drie zinnen die nog niet natuurlijk klinken:

1. :545–546 "Wie dat uitsluit, sluit dus niet uit dat één aandeel fors verkeerd gewaardeerd is, maar alleen dat veel aandelen dat allemaal zijn." → "Wie dat uitsluit, laat dus toe dat één aandeel fors verkeerd gewaardeerd is, maar niet dat veel aandelen het tegelijk zijn."
2. :919–921 "Of de twee sets dezelfde ruimte opspannen, meet de $R^2$ van de ene set op de andere." → "De $R^2$ van de ene set op de andere laat zien of beide sets dezelfde ruimte opspannen."
3. :868–869 "De vorige cel rekent alleen, en de tabel hieronder zet de eigenwaarden en het aandeel in de variantie op een rij." → "De tabel hieronder zet de eigenwaarden en hun aandeel in de variantie op een rij."

Bij volledige oplossing van alle punten: 9,3

## Controle 1 (F6c, ronde 9+)

Gecontroleerd tegen R9-1 in notes/rapport-03_11_apt_no_arbitrage.md en het college na de
wijzigingen (5.763 woorden, `prose_stats --check` PASS). De martingaalzin (r. 412-414) is
nagerekend: zonder dividend ($d_{t+1}=0$) geeft [](#eq-apt-no-arbitrage-martingaal) direct
$p_t/A_t = \E^{*}_t[p_{t+1}/A_{t+1}]$, de martingaaldefinitie onder $\pi^{*}$. Met dividend
geldt hetzelfde voor aandeel plus herbelegde dividenden: voor het aantal stukken $n_t$ met
$n_{t+1} = n_t(1+d_{t+1}/p_{t+1})$ geeft de vergelijking
$\E^{*}_t[n_t(p_{t+1}+d_{t+1})/A_{t+1}] = n_t p_t/A_t$, dus is $n_t p_t/A_t$ een martingaal
onder $\pi^{*}$. De correctie is juist. Het getal 2469 (Huberman-grens, replicatie) is
nagerekend: $0{,}002/0{,}0009^2 = 2469{,}1\ldots$, klopt; 61.700 is geschrapt en staat
nergens meer. Geen leftover "geprijsd"/"mispricing"-labels (grep leeg).

1. Feitelijke fout 1 (martingaal, :412-414): opgelost, correctie juist (zie boven).
2. Verbetering 1 (labels verkeerd/juist gewaardeerd, componenten met een premie): opgelost,
   overal consistent (simulatietabel, legenda, vergelijkingstabel).
3. Verbetering 3 / hardop-toets (5 stroeve zinnen, :67, :545-546, :578-581, :868-869,
   :919-921): opgelost, alle vijf letterlijk herschreven volgens het voorstel.
4. Helderheid, "hij" in Wat het voorspelt: opgelost ("koopt de handelaar").
5. Helderheid, SDF twee keer gedefinieerd: opgelost (Overzicht nu informeel, formele
   definitie alleen bij de definitie).
6. Beter uitleggen, Intuïtie "hoog": opgelost ("boven de rente").
7. Opbouw, routekaart Theorie: opgelost (kernresultaat en belangrijkste gevolg i.p.v.
   mechanische opsomming).
8. Opbouw, oefeningslabels als linkdoel: opgelost (platte tekst "de eerste/derde oefening").
9. Code en figuren, leeswijzer bij dezelfde alinea als conclusie: opgelost (eigen
   overgangsalinea vóór de figuur).
10. Code en figuren, labels volgden proza niet: opgelost (zie verbetering 1).
11. Replicatie, $c$-argument en vijf getallen in de alinea: opgelost ($c$ staat er eerst als
    onbekend, 61.700 geschrapt, de alinea telt nu drie getallen).

Geen nieuwe punten: geen verslechtering en geen nieuwe feitelijke fout gevonden.

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 | 9,5 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 |
| 3 | Taal | 20% | 9 | 9,5 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 9 | 9 |
| 6 | Replicatie en empirie | 10% | 9 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |
| | **Eindcijfer** | | **9,0** | **9,2** |

(0,25·9,5 + 0,2·9 + 0,2·9,5 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 9,225 ≈ 9,2.) Helderheid en
taal stijgen tot het cijfer dat F6 er expliciet voor in het vooruitzicht stelde
(verbetering 1+2 resp. verbetering 3, beide volledig opgelost). Opbouw, code en figuren en
replicatie hadden wel een punt, maar F6 noemde daarvoor geen vooruitzicht-cijfer, dus
blijven ze op 9 (plafondregel §11.3: geen ruimer belonen dan een verse lezer zou doen).
Cijfer van record: min(9,225, 9,3) = 9,2. Geen deelcijfer onder 8,5; taal boven 8.
