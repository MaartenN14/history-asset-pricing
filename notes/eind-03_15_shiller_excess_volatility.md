STATUS 03_15_shiller_excess_volatility F6c words=5425 prose=PASS open=0 cijfer=8,8 min=8,5

# Eindbeoordeling (F6): Shiller en LeRoy-Porter (03_15_shiller_excess_volatility)

Cijfer van record, zelfde kalibratie als L13 (en het L12-anker van de tweede
beoordelaar). Bij twijfel het lagere cijfer.

## De drie verbeteringen met het meeste effect

1. **Code** (8 → 9). In `shiller_test` de OLS-trend leesbaar schrijven (`np.polyfit`
   per rij of een benoemde lus) en de correlatie niet via `zip`-comprehension; de
   tabellen in de simulatie en de gevoeligheidstabel zonder dict-comprehensions
   opbouwen; `describe()` vervangen door een Nederlandse tabel; in oefening 2
   `sliding_window_view` vervangen door een zichtbare lus of `np.convolve` met één
   zin; een zin vóór de imports-cel.
2. **Helderheid** (8,5 → 9). Bij de Kleidon-propositie zeggen dat 6,5 een
   verhouding van *veranderingen* is en Shillers 5,59 een verhouding van
   gedetrendeerde *niveaus*; de bovengrens $\sigma(d)/\sqrt{2\bar r}$ in één zin
   duiden; de "raadselachtige uitkomsten" van Campbell en Shiller (1987) en de
   schending bij West (1988) elk met één getal of exemplaar.
3. **Replicatie** (8,5 → 9). De rij 1928–1979 (9,83) met Shillers Dow-waarde
   (13,28) in de tabel origineel/hier zetten en beoordelen; de getallen uit de
   alinea onder die tabel naar de tabel verplaatsen.

Samen: 2,70 + 1,70 + 1,35 + 0,85 + 0,90 + 0,90 + 0,425 = 8,825, dus 8,8.

## Eindcijfer: 8,5

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 9 |
| 4 | Toy-voorbeeld | 10% | 8,5 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 8,5 |

Gewogen: 2,55 + 1,70 + 1,35 + 0,85 + 0,80 + 0,85 + 0,425 = 8,525, dus 8,5.
Lengte: 5.283 woorden volgens `prose_stats` (PASS). Replicatieblok: 202 woorden.

## Feitelijke fouten

Nagerekend met de hand en tegen de celuitvoer (`tools/nb_outputs.py`). Correct: het
toy ($p^*$ = 12; 13,6; 22,88; $p^A_0 = 19{,}52$; 16; $25 \cdot 1{,}311744 = 32{,}7936$;
16,7936; langs het pad 23,01 en 34,16); $\delta = 1/1{,}048 = 0{,}954$,
$0{,}954^{100} < 1\%$, $\delta^{108} = 0{,}0063$; $50{,}12/8{,}968 = 5{,}59$,
$355{,}9/26{,}80 = 13{,}28$, $25{,}24/4{,}777 = 5{,}3$, $239{,}5/32{,}56 = 7{,}4$;
$\E(p) = \E(d)/r$; de Flavin-term $1{,}95/0{,}05/100 = 0{,}39$; het bewijs van de
Kleidon-propositie (stap 2 tot 5, $(1-\delta^2)/(r^2\delta^2) = 1 + 2/r$);
$\sqrt{1 + 2/0{,}048} = 6{,}5$, $\sqrt{21} = 4{,}6$, $\sqrt{1 + 2/0{,}07} = 5{,}4$;
$\rho = 25/26 = 0{,}96$; de afleiding van de decompositie; de simulatie (0%, 19,8%,
100%; mediaan 2,6; 95e percentiel 4,04); de replicatie (155 jaren; 8,6% en 1,7%;
3,93 tegen 5,59; $b$ en $\bar r$ binnen 0,13 en 0,24 procentpunt; 0,36;
$0{,}0860 - 0{,}0168 = 0{,}069$; 0,55 tot 9,8; $9{,}33/1{,}81 = 5{,}1$; 1,1; 0,83 en
0,59; SE 1,4; 0,55 en 2,36; log-lineair 1,1 tot 1,9; $1{,}81 \to 1{,}11$ is ruim een
derde lager); oefening 1 (26,24), oefening 2 (10,05; 6,53; 4,58; gesimuleerd 6,54),
oefening 3 (1,34 tot 12,1, factor 9,05). De verwijzing naar
[](#01-03-williams-ddm) (de ratio voorspelt het tienjaarsrendement, niet de
dividendgroei) klopt met die lecture. Shillers tabel 2 en de toeschrijving
"volgens Kleidon ... minstens een factor vijf" zijn niet tegen de bron
gecontroleerd.

Geen fouten gevonden. Twijfelachtig, niet geteld:
- Kritiek 2: "zes en een half keer zo veel als $p^*$, in dezelfde orde als Shillers
  tabel". De 6,5 is $\sigma(\Delta p)/\sigma(\Delta p^*)$; Shillers 5,59 is
  $\sigma(p)/\sigma(p^*)$ op gedetrendeerde niveaus. De simulatie zegt dat later zelf
  ("De formule geldt hier niet letterlijk"), maar de vergelijking hier legt twee
  verschillende statistieken naast elkaar.
- Bijschrift figuur 1: "Tijdvariërende rentes maken $p^*$ beweeglijker, maar niet op
  de momenten dat de koers beweegt", en in "Wat er brak": "volgt de rente-variant
  van $p^*$ de koers slecht (correlatie 0,59)". Die 0,59 is hoger dan de 0,46 van
  Shillers conventies over dezelfde periode.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Intuïtie**: de weersvoorspeller maakt de ongelijkheid concreet (fout los van de
  voorspelling, dus de metingen schommelen meer), en het slot geeft drie
  verwachtingen die later met naam worden ingelost.
- **Opzet** en **Hoe het getoetst wordt**: elk symbool krijgt een getal
  ($\delta = 0{,}954$; een prijs over honderd jaar weegt minder dan 1%;
  $\delta^{108} = 0{,}0063$), en de transversaliteitsvoorwaarde krijgt een exemplaar.
- **Kritiek 1**: de Flavin-formule krijgt direct een getal (39% te laag bij
  $\phi = 0{,}95$, $T = 100$) en wordt aan de standaardfout van 2% gekoppeld.

*Aanmerkingen*
- Kritiek 2: "Een volkomen rationele prijs beweegt dan van jaar op jaar zes en een
  half keer zo veel als $p^*$, in dezelfde orde als Shillers tabel." Veranderingen
  tegen niveaus (zie twijfelachtig).
- Wat Shiller mat: "bovengrens $\sigma(d)/\sqrt{2\bar r}$" en "wij gebruiken haar
  alleen als getal". De lezer krijgt geen zin over wat de grens betekent.
- Het antwoord in logs: "vonden voor aandelen raadselachtige uitkomsten" en "vond
  haar duidelijk en significant geschonden". Twee resultaten zonder exemplaar of
  getal.
- Simulatie, (b) en (c): "De discontovoet is 7%". In deze economieën wordt de prijs
  gerekend op de gedetrendeerde dividenden; in niveaus is de effectieve discontovoet
  hoger (ongeveer $1{,}07 \cdot 1{,}015 - 1$). Dat de toets het gedetrendeerde model
  toetst, staat nergens.

*Beter uitleggen*
- Waarom 6,5 en 5,59 niet hetzelfde meten: één bijzin bij de propositie volstaat.

*Voor een 9*
- De vergelijking met Shillers tabel beperken tot een orde van grootte en de
  statistiek benoemen (Kritiek 2, alinea na de propositie).
- De grens $\sigma(d)/\sqrt{2\bar r}$ in één zin lezen (Wat Shiller mat).
- Campbell-Shiller 1987 en West 1988 elk één getal of één concreet resultaat geven
  (Het antwoord: een grens in logs).

### 2. Opbouw en rode draad (8,5)

*Goed*
- Overzicht met vraag en antwoord ("met een factor vijf tot dertien", maar "die
  factor hangt sterk af van keuzes"), een lijst en één alinea geschiedenis.
- De drie verwachtingen komen terug ("Zoals de intuïtie voorspelde, maakt meer
  informatie de prijs beweeglijker"; "zoals de intuïtie verwachtte" bij de
  decompositie; de random walk in de simulatie).
- Het toy draagt door: $32{,}79 = 16 + 16{,}79$ in de stelling, $0 \le 16 \le 32{,}79$
  bij LeRoy-Porter, en "stap 4 en stap 6 van het toy-voorbeeld, op schaal" na de
  controle in de simulatie. De simulatie verantwoordt waarom zij 7% en 109 jaar
  gebruikt.
- Naden: L14 eindigt met "Dat onderzochten Shiller en LeRoy en Porter"; L16 opent
  met "Shiller liet daarna zien dat de markt als geheel meer beweegt".

*Aanmerkingen*
- Theorie telt zeven `###`-delen, waaronder "Wat Shiller mat", een tabel met de
  resultaten van het origineel. Dat is empirie in de theorie, en de replicatie
  herhaalt dezelfde tabel.
- Kritiek 1 (Flavin) heeft geen eigen resultaat en valt samen met economie (c) van
  de simulatie; het Samengevat noemt hem niet.

*Beter uitleggen*
- Geen.

*Voor een 9*
- "Wat Shiller mat" inkorten tot de definitie van de statistiek en één getal, en de
  tabel alleen in de replicatie tonen.
- Kritiek 1 in het Samengevat opnemen of in de simulatie onderbrengen.

### 3. Taal (9)

*Goed*
- Korte zinnen (gemiddeld 15,4 woorden, p90 23), drie puntkomma's, geen
  gedachtestreepjes, geen u/je, geen calques volgens `prose_stats`.
- Vaktermen krijgen een Nederlandse uitleg bij eerste gebruik (*ex-post rationele
  prijs*, *excess volatility*, *eenheidswortel*, *dividend smoothing*, VAR).
- De motieven zeggen wat ze hier betekenen ("Na Shiller is *excess volatility* ...
  een feit met twee concurrerende verklaringen").

*Aanmerkingen*
- Replicatie: "De grootste knoppen zijn de keuzes" (vertaald *knobs*).
- Overzicht: "Het werk definieert het tijdvak" leest stijf.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (8,5)

*Goed*
- Opzet-tabel, recept, zes genummerde stappen met getallen, tabel "met de hand"/"code",
  en "Wat we nu weten" met de getallen $0 \le 16 \le 32{,}79$.
- Het toy laat beide kanten van de lecture zien: de grens over toestanden en de
  omkering langs één pad.

*Aanmerkingen*
- Twee codecellen (de hulpfunctie `ex_post_price` en de toy-cel) in plaats van één.
- Twee mechanismen: de grens over toestanden (stap 2 tot 5) en de omkering langs de
  tijd (stap 6). De slotalinea draagt beide lessen.
- De tabel "met de hand" toont 23,01 en 34,16 naast 23,0059 en 34,1561; de hand
  is afgerond, de code niet.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De hulpfunctie naar de theorie of de simulatie verplaatsen, of stap 1 met de hand
  in de toy-cel rekenen (Toy-voorbeeld).
- De "met de hand"-kolom op dezelfde decimalen als de code, of de code afronden.

### 5. Code en figuren (8)

*Goed*
- `ex_post_price` is een zichtbare achterwaartse lus en wordt in toy, simulatie,
  replicatie en de log-lineaire grens hergebruikt.
- Elke figuur heeft een leeswijzer ("Let op de zwarte lijn bij één en op Shillers
  eigen 5,59"; "Let in de figuur links op de afstand tussen koers en $p^*$") en een
  bijschrift dat zegt wat te zien is.

*Aanmerkingen*
- `shiller_test`: "`b = (base - base.mean(axis=1, keepdims=True)) @ tc / (tc @ tc)`"
  schat de OLS-trend als matrixproduct zonder naam, en
  "`corr = np.array([np.corrcoef(a, c)[0, 1] for a, c in zip(p, pstar)])`" is een
  comprehension.
- Simulatietabel en gevoeligheidstabel worden met dict-comprehensions gebouwd
  ("`{k: np.mean(v > 1) for k, v in ratios.items()}`", "`{k: {...} for k, v in
  rows.items()}`"), wat STYLE §11.8 uitsluit.
- Replicatie, eerste cel: "`data[[...]].describe()`" geeft een presentatietabel met
  Engelse rijnamen (count, mean, std).
- Oefening 2: "`np.lib.stride_tricks.sliding_window_view`" is een truc.
- De imports-cel heeft geen zin ervoor; kolomnamen "5e pct", "95e pct".

*Beter uitleggen*
- Geen.

*Voor een 9*
- Zie verbetering 1 (Simulatie; Replicatie; oefening 2; Toy-voorbeeld).

### 6. Replicatie en empirie (8,5)

*Goed*
- Replicatieblok van 202 woorden met vijf onderdelen en een kwantitatieve verwachte
  afwijking (ratio tussen 3 en 7; een ander teken wijst op een fout).
- Tabel origineel/hier met "Geslaagd" dat naar de verwachte afwijking verwijst, en
  een tweede oordeel op de tweede verwachting.
- De gevoeligheidstabel maakt het punt van de lecture meetbaar (0,55 tot 9,8), met
  de standaardfout van 2% als knop ($\bar r \pm 2$ SE).

*Aanmerkingen*
- "De Dow-reeks is niet gratis beschikbaar, dus we tonen de S&P over 1928–1979 als
  benadering." De 9,83 staat alleen in de gevoeligheidstabel, zonder Shillers 13,28
  ernaast en zonder oordeel.
- Na de tabel: "De ratio is 3,93 tegen 5,59, binnen de verwachte 3 tot 7. ... de
  correlatie van 0,36 ligt onder 0,5." Vijf getallen uit de tabel in één alinea.

*Beter uitleggen*
- Geen.

*Voor een 9*
- Zie verbetering 3 (Replicatie, eerste tabel).

### 7. Oefeningen (8,5)

*Goed*
- Oefening 1 varieert het toy (structuur C), oefening 3 breidt de replicatie uit
  naar 1950–2025; elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen*
- Oefening 2 ("Kleidon in getallen") rekent een formule na en simuleert; er is geen
  afleiding. De afleiding van [](#eq-shiller-excess-volatility-kleidon) staat al in
  de dropdown.

*Beter uitleggen*
- Geen.

*Voor een 9*
- Oefening 2 een afleidingsdeel geven, bijvoorbeeld de ongelijkheid van LeRoy en
  Porter of de decompositie [](#eq-shiller-excess-volatility-decompositie) uit de
  identiteit (oefening 2).

## Navertelling in vijf zinnen

Een rationele prijs is de voorspelling van de contante waarde van de latere
dividenden, en een voorspelling varieert over toestanden nooit meer dan wat ze
voorspelt. Shiller mat dat langs de tijd en vond een koers die vijf tot dertien keer
zo veel beweegt als de ex-post rationele prijs. Die meting hangt af van eindwaarde,
trend, discontovoet en steekproef, en bij random-walk-dividenden of persistente
reeksen slaat de toets ook bij rationele prijzen alarm. Op de data van 1871–2025
loopt de ratio van 0,55 tot 9,8, afhankelijk van die keuzes. Wat overblijft, is de
log-prijs-dividend-ratio die 1,1 tot 1,9 keer zo veel beweegt als dividendnieuws
rechtvaardigt, en dat surplus is voorspelbaarheid van rendementen.

Dit komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen `notes/rapport-03_15_shiller_excess_volatility.md` §F6-1, de
lecture en de nieuwe celuitvoer. Vergeleken met de uitvoer van F6 zijn alle
aangehaalde getallen gelijk; alleen de presentatie verschilt (toy op twee decimalen,
Nederlandse overzichtstabel, rij 1928–1979 in de tabel origineel/hier).
`prose_stats --check`: 5.425 woorden, PASS.

| punt | status | vindplaats |
|---|---|---|
| Verbetering 1, code: `shiller_test` | opgelost | `np.polyfit` in een lus, correlatie in een lus, benoemde stappen |
| Verbetering 1, code: tabellen met comprehensions | opgelost | simulatie- en gevoeligheidstabel via een lus |
| Verbetering 1, code: `describe()` | opgelost | Nederlandse tabel met gemiddelde, standaarddeviatie, minimum en maximum |
| Verbetering 1, code: `sliding_window_view` | opgelost | zichtbare lus over de 400 termen; uitkomst 6,54 ongewijzigd |
| Verbetering 1, code: zin vóór de imports-cel | opgelost | "De eerste cel laadt de bibliotheken" |
| Verbetering 2: 6,5 tegen 5,59 | opgelost | "Dat is een verhouding van *veranderingen*, Shillers 5,59 een verhouding van gedetrendeerde *niveaus*" |
| Verbetering 2: $\sigma(d)/\sqrt{2\bar r}$ | opgelost | "hoe beweeglijker het dividend en hoe lager de discontovoet, hoe meer de koers ... mag bewegen" |
| Verbetering 2: Campbell-Shiller 1987 en West 1988 | deels | elk een concreet resultaat in woorden, geen getal (afgewezen met STYLE §11.11: geen getal zonder bron) |
| Verbetering 3: Dow-rij en getallen in proza | opgelost | rij 1928–1979 (9,83 tegen 13,28) met verwachting; oordeel zonder getallen |
| Helderheid: discontovoet in de simulatie | opgelost | "7% op de gedetrendeerde dividenden (in niveaus $1{,}07 \times 1{,}015 - 1 = 8{,}6\%$)"; nagerekend |
| Opbouw: tabel in "Wat Shiller mat" | opgelost | definitie en één getal (50,12/8,968 = 5,59) |
| Opbouw: Flavin ontbreekt in Samengevat | opgelost | "39% bij $\phi = 0{,}95$ en $T = 100$" |
| Opbouw: zeven `###` | niet (afgewezen) | elke kritiek houdt een eigen *Waarom*; reden aanvaard, aftrek blijft klein |
| Taal: "knoppen", "definieert het tijdvak" | opgelost | "keuzes met het grootste effect"; "bepaalde" |
| Toy: twee cellen, decimalen | opgelost | één cel, stap 1 met de hand in de cel, beide kolommen op twee decimalen |
| Toy: twee mechanismen | niet (afgewezen) | stap 6 is het anker voor Kleidon; reden aanvaard |
| Oefening 2 zonder afleiding | opgelost | deel 3: ondergrens van LeRoy en Porter; bewijs nagelopen en juist |
| Twijfelgevallen (Kleidon; correlatie 0,59) | opgelost | "maar deels samen bewegen (correlatie 0,59)" |

Geen verslechteringen en geen nieuwe feitelijke fouten. Kanttekening, geen aftrek:
"Met `ex_post_price(path, 1.25, 0.0)` geeft ze de 22,88, 13,6 en 12 uit stap 1"
staat zonder celuitvoer; nagerekend klopt het.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8,5 | 8,5 |
| 2 | Opbouw | 8,5 | 8,5 |
| 3 | Taal | 9 | 9 |
| 4 | Toy | 8,5 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 8,5 | 9 |
| 7 | Oefeningen | 8,5 | 9 |

Gewogen: 2,55 + 1,70 + 1,35 + 0,90 + 0,90 + 0,90 + 0,45 = 8,75. **Eindcijfer 8,8,
laagste deelcijfer 8,5.** Helderheid blijft 8,5: Campbell-Shiller 1987 en West 1988
staan er zonder getal, en de theorie vraagt de lezer drie kritieken en een
log-lineaire grens na elkaar vast te houden. Opbouw blijft 8,5 om de zeven
theoriedelen.
