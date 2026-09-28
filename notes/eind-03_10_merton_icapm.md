STATUS 03_10_merton_icapm F6c-2 words=5497 prose=PASS open=0 cijfer=8,9 min=8

# Eindbeoordeling: Merton, continue tijd en het ICAPM (F6)

## De drie verbeteringen met het meeste effect

1. **Code leesbaar maken** (criterium 5, 7 → 8). `kim_omberg` (broadcast-trucs `np.broadcast`/`np.broadcast_to`), de simulatiecel van `ols_var` (circa 55 regels, rekenen en presentatie in één cel) en `posterior_predictive` (`transpose(0, 2, 1)`) splitsen en benoemen. De `# TODO: naar hap.stats` uit de docstring halen.
2. **De Kim-Omberg-stap dragen met een getal en een beeld** (criterium 1, 8 → 9). Bij `eq-merton-icapm-riccati` staat alleen dat $B$ en $C$ negatief worden. Vóór de numerieke oplossing ontbreken de waarden van $\theta$ en $\sigma_\eta$ voor de illustratieve kalibratie ($\theta = 0{,}34$). "Hoe groot is het effect?" in het kernresultaat leent $h = 0{,}339$ uit een tabel die pas later komt.
3. **De replicatietabellen vullen** (criterium 6, 8 → 9). In de Barberis-tabel voor parameteronzekerheid zijn vier van de vijf cellen onder "origineel" leeg, en de Campbell-Viceira-tabel zegt alleen "tot 2". Rijen zonder origineel weglaten, of het getal uit het artikel noemen.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,1** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·7 + 0,1·8 + 0,05·9 = 8,05, afgerond 8,1.)

## 1. Helderheid van de uitleg (8)

*Goed.*
- Toy-voorbeeld: elke stap staat er met getallen, en de theorie haalt die getallen terug: $w^\ast = 0{,}10/(2\cdot 0{,}0676) = 0{,}7396$ tegen 0,8333 (De Merton-portefeuille). Geval A en geval B komen terug in het bewijs van Samuelson en bij het teken van de hedgevraag.
- De hedgevraag: "Het teken volgt de intuïtie, met één voorwaarde erbij." Het teken van $g_x$ wordt in drie zinnen afgeleid en aan geval B en B' gekoppeld.
- Symbolen krijgen een orde van grootte: $\kappa = 0{,}083$ met een halfwaardetijd van 8 jaar, $\delta = -0{,}8$ bij $\gamma = 5$.

*Aanmerkingen.*
- Het kernresultaat, "Hoe groot is het effect?": "Met $\gamma = 5$, $\sigma = 18\%$ en $h = 0{,}339$ op twintig jaar uit de Kim-Omberg-tabel hieronder". Het getal komt uit een tabel die de lezer nog niet heeft gezien, met een kalibratie die nog niet is ingevoerd.
- Wat het voorspelt: "Bij $\gamma > 1$ en $\theta > 0$ worden ze negatief, dus is de hedgevraag positief zodra $\rho < 0$." Wat $B$ en $C$ economisch zijn, staat er niet. $g_\eta/g = B + C\eta$ staat alleen in de dropdown.
- Numerieke oplossing: "$\sigma_z = \SD(\varepsilon_2)\sqrt{2\kappa/(1-\phi^2)}$ en $\sigma_\eta = b\,\sigma_z/\sigma$". De vertaling voert drie symbolen in zonder de getallen die eruit volgen.
- $J_t$ betekent in De Merton-portefeuille de partiële afgeleide naar de tijd, en in het bewijs van Samuelson de waardefunctie op tijdstip $t$ ($J_T(W)$, $J_{t+1}(W)$).

*Beter uitleggen.* Welke $\theta$ en $\sigma_\eta$ de illustratieve kalibratie geeft (één regel, twee getallen). Wat $C$ zegt: hoe sterk de waarde van de toekomst reageert als de Sharpe-ratio stijgt.

*Voor een 9.* Het voorbeeld in "Hoe groot is het effect?" verplaatsen naar na de tabel van Numerieke oplossing, of een getal gebruiken dat de lezer al kent. $\theta$ en $\sigma_\eta$ als getal onder de VAR-tabel. Eén zin met de economische betekenis van $B + C\eta$ in de hoofdtekst van Wat het voorspelt.

## 2. Opbouw en rode draad (8)

*Goed.*
- Het Overzicht geeft vraag en antwoord in twee zinnen. Van de drie voorspellingen aan het eind van de intuïtie worden er twee in Theorie met naam ingelost ("Dat is de eerste voorspelling", "Dat was de derde voorspelling").
- De routekaart noemt vijf resultaten en wijst de kern aan. Samengevat verwijst per regel naar het label.
- Simulatie, replicatie en Wat er brak draaien om dezelfde grootheid: de hedgevraag bij $\gamma = 5$ op twintig jaar (0,339 in het model, 0,223 op de data).

*Aanmerkingen.*
- Met 5.483 woorden zit de lecture net onder de grens van 5.500. Theorie draagt vijf stellingen, een numerieke oplossing en een tweede numerieke controle met een rooster ("Klopt de vertaling van een jaarlijks VAR naar continue tijd?"). Die controle is nodig voor niets dat daarna komt, behalve `solve_rebalancing`, dat ook in de replicatie had kunnen staan.
- De tweede voorspelling ("stijgt de fractie met de horizon") wordt niet met naam ingelost.
- De replicatie heeft drie delen en drie oordelen. Het derde deel (parameteronzekerheid) is een tweede verhaal naast de hedgevraag.

*Voor een 9.* De roostercontrole in Numerieke oplossing terugbrengen tot één zin met het grootste verschil. De tweede voorspelling expliciet inlossen bij de figuur `fig-merton-icapm-horizon`.

## 3. Taal (8)

*Goed.* Korte zinnen (gemiddeld 14,2 woorden), geen verboden woorden of calques volgens `prose_stats`. Het Engelse abstract van Merton is geparafraseerd ("Merton schreef het in zijn abstract").

*Aanmerkingen.*
- Toy-voorbeeld, stap 4: "In de dure toestand is er geen premie, de belegger houdt $w = 0$ en $q_{\text{duur}} = 1$." Twee zinnen met een komma aan elkaar.
- Replicatie, Barberis' VAR: "Op die ene $t$-waarde rust de hele literatuur over horizoneffecten." Een retorische overdrijving.
- Wat er brak: "Het ICAPM gaf elk later meerfactormodel een theoretische vergunning". Beeldspraak die de volgende bijzin toch moet uitleggen.
- Wisselende namen: "beleggingskansen", "kansen" en "de toekomst" voor hetzelfde begrip; "hedgefractie" $h$ naast "hedgevraag".

*Voor een 9.* Stap 4 splitsen. "Kansen" één keer als alias van "beleggingskansen" invoeren en daarna één naam gebruiken. De overdrijving in Barberis' VAR schrappen.

## 4. Toy-voorbeeld (9)

*Goed.* Opzettabel, vijf stappen van één regel met getallen, één codecel, tabel hand/code die tot vier decimalen overeenkomt. Eén niet-afgeleide formule (het recept voor $q$), die Theorie als eerste afleidt. De slotzin zegt wat de lezer nu weet.

*Aanmerkingen.* $\sqrt{2{,}25 \cdot 26/25}$ is net geen handwerk, maar wel te doen.

## 5. Code en figuren (7)

*Goed.* Vóór elke figuur staat waarop te letten ("Let in de figuur op de afstand tussen de getrokken en de gestreepte lijn"). De Runge-Kutta-lus en de achterwaartse recursie in `solve_rebalancing` zijn zichtbare lussen. De parameters staan in een dict (`illustrative`).

*Aanmerkingen.*
- Numerieke oplossing: `shape = np.broadcast(sigma, kappa, theta, sig_l, rho).shape` en `np.broadcast_to(myopic, np.shape(out))`. Trucs die alleen de simulatie nodig heeft.
- Simulatie: de cel met `ols_var` beslaat circa 55 regels en combineert een functie, een simulatielus, de schatting en de presentatietabel. De docstring eindigt met `# TODO: naar hap.stats`.
- Parameteronzekerheid: `C = C_hat + L_x @ Z @ L_sigma.transpose(0, 2, 1)`. Een compacte batchmatrixtruc.
- De cel met `solve_rebalancing` combineert rekenwerk en de controletabel.

*Voor een 9.* De simulatiecel splitsen in functie, simulatie en tabel. De TODO verwijderen. De broadcast-logica in `kim_omberg` vervangen door een lus over parametersets.

## 6. Replicatie en empirie (8)

*Goed.* Het blok heeft alle vijf onderdelen en een toetsbare verwachte afwijking ("Een negatieve helling of een positieve correlatie is een fout in de code"). Drie tabellen origineel/hier, drie oordelen die met Geslaagd of Gedeeltelijk geslaagd beginnen en naar de verwachting verwijzen. Het verschil met Barberis wordt in standaardfouten uitgedrukt (0,5).

*Aanmerkingen.*
- De Campbell-Viceira-tabel heeft als origineel twee keer "tot 2".
- De Barberis-tabel voor parameteronzekerheid: vier van de vijf cellen onder "origineel (Barberis)" zijn leeg.
- Onder het derde oordeel staan getallen weer in lopende tekst: "tienjaarssteekproef 1986–1995", "44 jaar maanddata", "honderd jaar".

*Voor een 9.* In de tabellen origineel/hier alleen rijen met een origineel; eind 2025 en D/P in sd in een aparte tabel. Voor Campbell-Viceira hun getal bij een vergelijkbare $\gamma$ noemen.

## 7. Oefeningen (9)

*Goed.* Instap met een variatie op het toy-voorbeeld, een afleiding van de gesloten vorm met numerieke controle, een uitbreiding van de replicatie naar 1996–2025. Elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen.* In oefening 3 is deelvraag 2 alleen op vijf jaar in woorden uitgewerkt.

## Feitelijke fouten

1. Replicatie, Parameteronzekerheid volgens Barberis: "met parameteronzekerheid ligt de allocatie op elke horizon twee à drie procentpunt lager". Dat geldt voor de kolom "D/P op gemiddelde" (1,9 tot 3,3 pp). Voor "D/P zoals eind 2025" is het verschil 1,2 tot 1,9 pp (0,222 − 0,210 tot 0,364 − 0,345).

Nagerekend en correct: de toy-stappen (0,8333; 25/26; 1,5297; 0,8759; 0,7909; +5,1%; 1,7361 bij log-nut), $w^\ast = 0{,}7396$, 8% marktpremie, 10,7% tegen 16,2%, $\kappa = 0{,}083$ en 8 jaar, de Riccati-vergelijkingen (opnieuw afgeleid uit de HJB-vergelijking) en de vierkantsvergelijking voor $C_\infty$, 0,378 en 0,339, het grootste roosterverschil van 1,6 pp, de simulatie (0,143–0,850; 0,450; 55,5%), 0,5 en 2,4 bij Barberis, $t = 1{,}07$, 0,924, −0,856, 8,8 jaar, 14,1%, 4,2%, 4,5%, −1,86 sd, 0,483, oefening 3 (0,358; 2,60; 0,647; 0,649 tegen 0,817).

## Navertelling in vijf zinnen

Samuelson en Merton lieten in 1969 zien dat de horizon niet uitmaakt voor een CRRA-belegger zolang rendementen onafhankelijk zijn: hij kiest elk jaar hetzelfde percentage, in continue tijd $(\mu - r)/(\gamma\sigma^2)$. Zijn rendementen voorspelbaar, dan houdt een belegger met $\gamma > 1$ naast de myopische vraag een hedgevraag aan in activa die stijgen wanneer de beleggingskansen verslechteren; bij aandelen en de dividendopbrengst is die positief en groeit hij met de horizon. Tel die vraag op over alle beleggers, en het verwachte rendement beloont naast de marktbèta de bèta op elke toestandsvariabele: het ICAPM, dat niet zegt welke variabelen dat zijn. In een illustratief VAR kan de hedgevraag de vraag naar aandelen bijna verdubbelen, maar een eeuw data meet haar slecht, omdat ze hangt aan een helling die maar in de helft van de steekproeven significant is. Op de Goyal-Welch-data is de hedgevraag positief en kleiner dan een verdubbeling, en parameteronzekerheid drukt de allocatie maar een paar procentpunt, omdat een eeuw data de posterior smal maakt.

De navertelling komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen `rapport-03_10_merton_icapm.md` §F6-1 en de huidige lecture en notebook. `prose_stats --check`: 5.493 woorden, PASS. De `nb_outputs` van de oude en de nieuwe versie verschillen alleen in celgrenzen en in de gesplitste Barberis- en Campbell-Viceira-tabellen; Kim-Omberg, simulatie en replicatie geven dezelfde waarden.

| punt | status | toelichting |
|---|---|---|
| Feitelijke fout 1 (twee à drie procentpunt) | opgelost | Nieuwe tabel met het kleinste en grootste verschil per beginstand (0,019–0,032 en 0,012–0,019); de tekst zegt "twee à drie procentpunt, vanaf eind 2025 ruim één à twee". Klopt. |
| Verbetering 1: code | opgelost | `np.broadcast` en `np.broadcast_to` weg; de simulatiecel is gesplitst in functie, simulatie en tabel, met een zin ertussen; `L_sigma_t` benoemd. De TODO staat nog als commentaarregel boven `ols_var`, niet meer in de docstring. |
| Verbetering 2: Kim-Omberg met getal | opgelost | $\theta = 0{,}34$ en $\sigma_\eta = 0{,}069$ als handberekening (nagerekend: $\sigma_z = 0{,}156$); zin over $B + C\eta$ in de hoofdtekst; "Hoe groot is het effect?" staat nu na de Kim-Omberg-tabel. Nieuwe kleine H8-zwakte: de verplaatste alinea opent met "Dat getal zegt ook hoe groot het ICAPM-effect is", na een zin die over een verdubbeling ging. |
| Verbetering 3: replicatietabellen | opgelost | Alleen rijen met origineel in de tabellen origineel/hier; de overige grootheden in een aparte tabel. Het getal van Campbell en Viceira is terecht niet toegevoegd (niet geverifieerd, STYLE §11.11). |
| Naadpunt 5 (Black-Scholes) | opgelost | "In [](#02-09-black-scholes) leverde de stochastische calculus de prijs van een optie. Merton gebruikte die wiskunde al vanaf 1969 voor de portefeuillekeuze". Strookt nu met L9. |

Niet gedaan en niet gevraagd: $J_t$ met twee betekenissen, de tweede voorspelling expliciet inlossen, de kommazin in stap 4, "vergunning", wisselende namen voor beleggingskansen.

**Cijfers na controle 1 (cijfer van record)**

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8 |
| 2 | Opbouw | 8 | 8 |
| 3 | Taal | 8 | 8 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 7 | 8 |
| 6 | Replicatie | 8 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,1 | **8,3** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·9 + 0,05·9 = 8,25, afgerond 8,3.) Helderheid blijft 8: de drie punten uit "Voor een 9" zijn gedaan, maar $J_t$ staat er nog en de verplaatste alinea opent met een onduidelijke "Dat". Voor 8,5 zijn nog nodig: de $J_t$-botsing en die openingszin (helderheid naar 9), of de tweede voorspelling inlossen bij de figuur en de kommazin in stap 4 splitsen (opbouw of taal naar 9).

## Controle 2

Gecontroleerd tegen `rapport-03_10_merton_icapm.md` §F6-2 en de huidige lecture. `prose_stats --check`: 5.497 woorden, PASS. `nb_outputs` is identiek aan controle 1.

| punt uit controle 1 | status | toelichting |
|---|---|---|
| $J_t$ met twee betekenissen | opgelost | In het Samuelson-bewijs heet de waardefunctie nu $V_t(W)$, met de zin "$J_t$ is verderop een afgeleide". |
| Opening "Dat getal" (H8) | opgelost | "De hedgevraag van 0,339 bij $\gamma = 5$ op twintig jaar bepaalt ook hoe groot het ICAPM-effect is." |
| Tweede voorspelling inlossen | opgelost | Bij de horizonfiguur: "Dat de getrokken lijn stijgt, is de tweede voorspelling van de intuïtie." |
| Kommazin in stap 4 | opgelost | Twee zinnen: "In de dure toestand is er geen premie. De belegger houdt daar $w = 0$ ..." |
| "vergunning" | opgelost | "een theoretische grond". |
| Wisselende namen voor beleggingskansen | opgelost | "de beleggingskansen, kortweg de kansen" wordt één keer ingevoerd. |
| TODO in de code | geen aftrek meer | STYLE §5 (r. 467) vraagt de regel `# TODO: naar hap.stats`; dat is een projectkeuze. |
| Rekenwerk en tabel in één cel bij `solve_rebalancing` | niet | De cel met `solve_rebalancing`, `normal_shocks`, `known` en de controletabel beslaat nog circa 48 regels. |

Geen verslechteringen, geen nieuwe feitelijke fouten.

**Cijfers na controle 2 (cijfer van record)**

| nr | criterium | controle 1 | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 9 |
| 2 | Opbouw | 8 | 9 |
| 3 | Taal | 8 | 9 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 8 | 8 |
| 6 | Replicatie | 9 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,3 | **8,9** |

(0,3·9 + 0,2·9 + 0,15·9 + 0,1·9 + 0,1·8 + 0,1·9 + 0,05·9 = 8,90.) Code blijft 8 omdat de roostercel functies, rekenwerk en tabel combineert.
