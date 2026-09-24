STATUS 02_06_efficiente_markten F5c words=5444 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling 02_06_efficiente_markten: Fama en de efficiënte markt

## Eindcijfer: 8,0

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 8 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·8 + 0,1·8 + 0,1·8 + 0,1·8 + 0,05·8 = 8,00.

## 1. Helderheid van de uitleg (8)

*Goed*
- "Wat het voorspelt": de premieformule [](#eq-efficiente-markten-premie) krijgt meteen
  het toy-getal (covariantie $1 - 1{,}0435$, premie 4,35%), en de maat $Q$ wordt
  teruggevoerd op de $q = 0{,}4$ uit stap 4.
- "Wat het niet verbiedt": de propositie krijgt een uitgerekend getal (Sharpe-ratio
  $0{,}6/4{,}5 = 0{,}13$, "De SDF hoeft dan maar 13% per maand te schommelen") en het
  Fama-citaat van 1991 staat als blokcitaat na een Nederlandse parafrase.
- "Simulatie": $N^{*} \approx 3{,}84/0{,}0044 \approx 870$ maanden wordt vertaald naar
  jaren, naar een halve kans, en naar 80% kans; het geleende resultaat
  [](#eq-bachelier-power) wordt in één regel herhaald.

*Aanmerkingen*
- "Simulatie", na de controlecel: "Hij is negatief in één op de honderdduizend maanden.
  Bij de gemiddelde premie vraagt dat een schok van $\sigma/\mu = 4{,}5/0{,}6 = 7{,}5$
  standaarddeviaties." De tweede zin verklaart de eerste niet: een schok van 7,5
  standaarddeviaties komt eens in de $3\cdot 10^{13}$ maanden voor. De negatieve maanden
  vallen in toestanden met een hoge $|\mu_t|$ (zie Feitelijke fouten).
- "Simulatie", slotalinea: "Een persistente $x_t$ spreidt in een eindige steekproef
  minder rond haar steekproefgemiddelde". $x_t$ komt in deze lecture nergens voor; de
  voorspeller heet $s_t$.
- "Replicatie op echte data", oordeel: "en na 0,1% per transactie nog ruim acht, tegen
  1,7 bij Fama en Blume." De 1,7 is hun voorsprong *vóór* commissies; de zin zet hem
  naast ons getal *na* kosten.
- Jensen-replicatie: "De regressie is hier het model van risico: het CAPM, met de markt
  als enige factor." Het CAPM komt pas in 02_08; de lezer krijgt geen regel wat het
  zegt (verwacht excess rendement evenredig met bèta) en waarom alpha dan een maat is
  voor vaardigheid.
- "Simulatie": "Voor 80% kans is $(1{,}96 + 0{,}84)^2/R^2$". De 0,84 krijgt geen naam
  (het 80%-kwantiel van de standaardnormale verdeling).
- "Opzet: drie woorden": autocorrelaties "toetsen dus de fair game ten opzichte van de
  koersgeschiedenis". Ze toetsen een gevolg ervan (ongecorreleerdheid, deel (ii)), niet
  de fair game zelf.

*Beter uitleggen*
- Waarom de SDF soms negatief is: één zin dat dat gebeurt in maanden waarin de premie
  $\mu_t$ ver boven haar gemiddelde ligt (bij $\mu_t = 1{,}5\%$ is de drempel drie
  standaarddeviaties).
- Het CAPM bij Jensen: één regel wat het model zegt en wat alpha dan meet.

*Voor een 9*: herschrijf de twee zinnen over $m < 0$ na de controlecel in "Simulatie";
vervang $x_t$ door $s_t$ in de slotalinea van "Simulatie"; zet in het oordeel van de
filterreplicatie voor-kosten naast voor-kosten (12,9 tegen 1,7); geef het CAPM één regel
in het Jensen-blok; noem 0,84 bij de 80%-berekening.

## 2. Opbouw en rode draad (8)

*Goed*
- "Overzicht" stelt de vraag en geeft het antwoord ("alleen te toetsen samen met een
  model"); "Intuïtie" doet drie genummerde voorspellingen, en de theorie lost ze elk
  expliciet in ("Dat is de eerste/tweede/derde verwachting uit de intuïtie").
- Het toy draagt door: de 3,45% en 5,26% keren terug in de simulatie, de $q = 0{,}4$ bij
  de maat $Q$, en oefening 1 bouwt op dezelfde tabel.
- Routekaart en "Samengevat" op hun plaats; de simulatie opent met haar antwoord ("in
  zes van de tien economieën"). 5.395 woorden, net onder de grens.

*Aanmerkingen*
- "Theorie", routekaart: "We leiden vier dingen af." Daarna volgen vijf onderdelen
  (drie woorden, Samuelson, SDF-martingaal, elk patroon, toetsen), en de telling past op
  geen enkele indeling.
- De replicatie meet een mechanisme dat de theorie niet heeft behandeld. Niet-synchrone
  handel verschijnt pas in "Verwachte afwijking", en "Waarom wint een klein filter bij
  positieve autocorrelatie?" staat pas na het oordeel. De theorie levert alleen
  de propositie dat geen filter buy-and-hold verslaat.
- De simulatie (voorspelregressie op $s_t$) heeft geen tegenhanger op echte data; toy,
  simulatie en replicatie delen daardoor maar ten dele hun getallen.
- De Jensen-replicatie toetst de sterke vorm, die in "Theorie" alleen een tabelregel
  krijgt ("hier kort").

*Beter uitleggen*
- Eén zin aan het eind van "Hoe het getoetst wordt" dat een index door niet-synchrone
  handel autocorrelatie kan hebben die een filter oogst, zodat de replicatie een
  voorspelling toetst die de theorie al deed.

*Voor een 9*: laat de routekaart het aantal onderdelen noemen dat volgt; verplaats de
autocorrelatie-uitleg ("Waarom wint een klein filter") naar vóór het oordeel of naar
"Hoe het getoetst wordt"; koppel het Jensen-blok in één zin aan de sterke vorm uit de
tabel van Fama.

## 3. Taal (8)

*Goed*
- Korte zinnen (gemiddeld 14,5 woorden, geen zin boven 40); geen u/je.
- Engelse vaktermen krijgen ter plekke een Nederlandse uitleg (*joint hypothesis*,
  *niet-synchrone handel*, *limits of arbitrage*, variance ratios).
- De motieven worden ter plekke uitgelegd ("theorie of feit (is dit een theorie die
  getoetst wordt, of een feit dat op een verklaring wacht?)").

*Aanmerkingen*
- "Overzicht": "Dat artikel definieert het tijdvak." Vertaald Engels ("defines the
  era"), dezelfde calque als in 02_05.
- "men" naast de "we" van de rest: "Nieuws is wat men nog niet wist", "het model van
  risico dat men erbij neemt", "niet in iets wat men had kunnen kopen", "zodra men een
  verhandelbaar instrument gebruikt", "een index die men niet kon kopen. Toen men die
  index kon kopen".
- "Overzicht": "In januari 1965 verscheen het proefschrift ... in het januarinummer van
  de *Journal of Business*": januari twee keer in één zin.
- Wisselende namen: de stelling heet "Martingaal na verdiscontering", de sectie en
  "Samengevat" zeggen "na weging met de SDF"; het model van de onderzoeker heet
  "constant-rendementmodel", "het constante model" en "een constant verwacht
  rendement".

*Voor een 9*: "Dat artikel definieert het tijdvak" naar natuurlijk Nederlands; "men"
door "we" of een lijdende vorm; één keer januari; één naam voor de weging met de SDF en
één voor het constante model.

## 4. Toy-voorbeeld (8)

*Goed*
- Twee perioden, twee toestanden, rente nul: alles in vijf minuten na te rekenen
  (116, 76, 92; 4,35%, 3,45%, 5,26%), met een tabel hand/code.
- De slotzin zegt wat de lezer nu weet en geeft de *joint hypothesis* een naam "in het
  klein".

*Aanmerkingen*
- Stap 4 voegt een tweede idee toe dat pas in "Theorie" wordt afgeleid: de
  risiconeutrale kansen $q$ en de rij "E^Q_0[p_1]" in de tabel.
- "Na slecht nieuws is de spreiding van 40 groot ten opzichte van een prijs van 76".
  De spreiding is na goed nieuws ook 40; dat de risicocorrectie in beide gevallen 4 is
  en alleen relatief verschilt, staat pas in de uitwerking van oefening 1.

*Voor een 9*: laat stap 4 weg of maak er één zin vooruitblik van; zeg in de slotalinea
dat de risicocorrectie na goed en slecht nieuws gelijk is (4) en dat alleen de prijs
waardoor gedeeld wordt verschilt.

## 5. Code en figuren (8)

*Goed*
- `filter_positions` is een zichtbare lus die de regel van Alexander stap voor stap
  volgt; de Samuelson-cel en `slope_tstats` lezen als de wiskunde, met docstrings.
- Beide figuren hebben een leeswijzer ervoor ("Let in de figuur links op de afstand
  tussen de twee soorten punten") en een figuurtekst die zegt wat te zien is.

*Aanmerkingen*
- Toy-cel: `dict(zip(toy_economy((0.8, 1.2)), hand))` koppelt de handwaarden via de
  volgorde van de sleutels aan de rijen; een truc die de lezer moet ontcijferen.
- `filter_performance`: `held.ne(0).idxmax()` als "eerste signaal" zonder commentaar.
- Filtertabel: "hier: buy-and-hold" verschilt per filter (7,4% tot 11,2%), omdat elk
  filter vanaf zijn eerste signaal telt. De tekst zegt dat niet, en de figuur trekt het
  gemiddelde van die acht als één lijn.
- Presentatietabellen tonen code-achtige rijlabels ("E_0[R_1] - 1", "spot: S_{t+1} -
  S_t", "rho_1 dagrendement").

*Voor een 9*: schrijf de handkolom als expliciet woordenboek; commentaar bij
`idxmax`; één zin onder de filtertabel over de wisselende buy-and-hold (of reken
buy-and-hold over het volle venster); leesbare Nederlandse rijlabels in de toy- en
Samuelson-tabel.

## 6. Replicatie en empirie (8)

*Goed*
- Twee blokken met bron, wat, data, verschil en verwachte afwijking, elk onder 250
  woorden; de filterreplicatie formuleert drie toetsbare criteria vooraf.
- De deelperiodetabel maakt het niet-synchrone-handelargument hard: de voorsprong stijgt
  met $\rho_1$ (6, 13, 21 procentpunt) en keert om op SPY (−16).
- Het Jensen-oordeel begint met "Geslaagd", verwijst naar de verwachting en vertaalt de
  standaardfout naar een loopbaan (1,4/1,3 ≈ 1 procentpunt na 44 jaar).

*Aanmerkingen*
- Filtertabel: de kolom "origineel: na commissies" (−103,6% voor het 0,5%-filter) staat
  naast "hier: na 0,1% per transactie". Het blok zegt dat wij met hun alternatief van
  0,1% rekenen, maar hun 0,1%-resultaten staan niet in de tabel; de twee kolommen zijn
  niet vergelijkbaar.
- "Ook criteria 2 en 3 kloppen." Het oordeel over twee van de drie criteria begint niet
  met Geslaagd / Gedeeltelijk / Niet geslaagd.
- Criterium 1, "op de index ruimer dan hun 1,7 procentpunt", is geen verwachte
  afwijking met een grootte: elk getal boven 1,7 slaagt.
- Jensen-tabel: gemiddelde bèta 1,009 tegen 0,840 bij Jensen; de tekst zegt niets over
  dat verschil (zijn fondsen hielden kas).

*Voor een 9*: vervang de kolom "na commissies" door hun 0,1%-resultaten, of label hem
als niet vergelijkbaar; laat het oordeel over criteria 2 en 3 met "Geslaagd" beginnen;
geef bij criterium 1 een verwachte orde van grootte (bijvoorbeeld uit $\rho_1 \approx
0{,}17$); één zin over het bètaverschil.

## 7. Oefeningen (8)

*Goed*
- Precies de drie typen: instap op het toy (1), afleiding van het Samuelson-effect (2),
  uitbreiding van de replicatie (3); elke uitwerking eindigt met "Wat dit leert".
- Oefening 1 knoopt het toy aan de propositie ($\SD(m)/\E(m) = k$) en aan de grens van
  arbitrage (33%).

*Aanmerkingen*
- Oefening 3.2 vraagt "Herhaal met een filter dat alleen lang gaat", dus de break-even
  $c^{*}$; de uitwerking geeft alleen het rendement vóór kosten van die variant, geen
  $c^{*}$ en geen transacties per jaar.
- Oefening 2.1: de variantie $\phi^{2(T-t-1)}\sigma_S^2$ wordt gevraagd, maar de
  uitwerking stopt bij $F_{t+1} - F_t = \phi^{T-t-1}\nu_{t+1}$.

*Voor een 9*: laat `long_only_performance` ook het aantal transacties teruggeven en
reken $c^{*}$ voor de lange variant; sluit 2.1 af met de variantiestap.

## Feitelijke fouten

1. **"Simulatie", alinea na de controlecel**: "Hij is negatief in één op de
   honderdduizend maanden. Bij de gemiddelde premie vraagt dat een schok van
   $\sigma/\mu = 4{,}5/0{,}6 = 7{,}5$ standaarddeviaties." De fractie klopt (nagerekend:
   $1{,}17\cdot10^{-5}$), de verklaring niet. Bij de gemiddelde premie is de kans
   $P(Z > 7{,}5) = 3\cdot10^{-14}$. De negatieve maanden komen vrijwel geheel uit
   toestanden met $|\mu_t|$ twee à drie standaarddeviaties van $s_t$ van het gemiddelde
   (bij $\mu_t = 1{,}5\%$ is de drempel 3 standaarddeviaties, kans $1{,}3\cdot10^{-3}$).

Nagerekend en correct: toy (116, 76, 92, 96; 4,35%, 3,45%, 5,26%; $q = 0{,}4$; premie via
covariantie 4,35%); bewijzen van de hiërarchie, Samuelson, martingaal na weging, elke-SDF
(inclusief $\SD(m)/\E(m) = |\mu|/\sigma$) en de filterpropositie; AR(1)-termijnprijs en
helling $-0{,}5$; Sharpe 0,13; SD van $\E_t[R^e]$ 3,6 procentpunt per jaar rond 7,2%;
$R^2 = 0{,}44\%$; $N^{*} \approx 870$ maanden (72 jaar) en 1780 (148 jaar);
verwerpingsfracties en verschil simulatie/formule (grootst bij 75 jaar, 6 punten; onder
2 bij 150; halve kans rond 80 jaar); Fama 1965 72 pagina's (JB 38, 34–105);
filtertabel (12,9 en 8,1 procentpunt; 1,7 bij FB; 48 transacties; voorsprong weg vanaf 10%
op de index, vanaf 1% bij FB); deelperioden (5,9 / 12,9 / 20,8 / −11,3 / −12,7 / −16,3,
monotoon in $\rho_1$); Jensen-tabel (−0,3% met $t = -0{,}7$; Contrafund 1,4% met
$t = 1{,}3$; T. Rowe $t = -2{,}3$; 535 maanden); oefening 1 ($k = 4/11$; 6,45%, 8,51%;
33%); oefening 2 ($2^{22} \approx 4{,}19$ miljoen, afwijking 3,5 promille); oefening 3
(0,27% en 0,41%; 6,8% tegen 10,4%). De gepubliceerde waarden van Fama en Blume (1966) en
Jensen (1968) zijn niet tegen de papers gecontroleerd.

## De drie verbeteringen met het meeste effect

1. **Helderheid op vijf plekken** ("Simulatie" en de replicaties): de verklaring van
   $m < 0$, $x_t$ → $s_t$, voor-kosten naast voor-kosten (12,9 tegen 1,7), één regel
   CAPM bij Jensen, de 0,84 benoemen. Helderheid 8 → 9; lost de feitelijke fout op.
2. **Replicatie vergelijkbaar maken**: de kolom "na commissies" vervangen of labelen,
   de oordelen over criteria 2 en 3 in de vaste vorm, een grootte bij criterium 1, het
   bètaverschil. Replicatie 8 → 9.
3. **Theorie en replicatie verbinden**: het autocorrelatie-mechanisme van het filter en
   de niet-synchrone handel in "Hoe het getoetst wordt", en een kloppende routekaart.
   Opbouw 8 → 9.

## Navertelling in vijf zinnen

Een prijs die de verwachting van een latere uitbetaling is, verandert onvoorspelbaar
(Samuelson), maar voor aandelen geldt dat pas na weging met de SDF, zodat een
risicopremie die met de toestand beweegt voorspelbaarheid geeft zonder dat iemand zich
vergist. Omdat elk patroon zonder arbitrage een SDF heeft, is efficiëntie alleen samen met
een model van risico te toetsen (de joint hypothesis). In een rationele economie vindt een
onderzoeker met een constant-rendementmodel na een eeuw in zes van de tien gevallen
"inefficiëntie", omdat een kleine $R^2$ zo'n lange steekproef vraagt. Filterregels
verslaan buy-and-hold op de index van 1957–1962 ruim, maar dat is autocorrelatie door
niet-synchrone handel, die op een verhandelbare SPY verdwijnt en voor een belegger nooit
na kosten te halen was. Actieve fondsen verslaan de markt ook veertig jaar na Jensen niet
aantoonbaar. Dit komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen de lecture na F5-1 (5.444 woorden, `--check` PASS). Alleen de eigen
punten.

**Feitelijke fout 1 (m < 0)**: *opgelost*. De tekst zegt nu dat 7,5 standaarddeviaties
"vrijwel nooit" voorkomt en dat de negatieve maanden in toestanden met een hoge premie
vallen (drempel 3 standaarddeviaties bij $\mu_t = 1{,}5\%$).

**1. Helderheid**
- $x_t$ → $s_t$: *opgelost*.
- Voor-kosten naast voor-kosten in het filteroordeel: *opgelost* (12,9 tegen voorspeld 13,9
  en tegen 1,7; ruim acht na 0,1% als aparte zin).
- CAPM bij Jensen: *opgelost* (één regel, met de koppeling aan de sterke vorm).
- De 0,84: *opgelost* (80%-kwantiel).
- Autocorrelaties "toetsen de fair game": *opgelost* ("een gevolg van de fair game, deel
  (ii): ongecorreleerdheid").

**2. Opbouw**
- Routekaart "vier dingen": *opgelost* ("vijf dingen").
- Mechanisme van de replicatie ontbrak in de theorie: *opgelost* ("Hoe het getoetst
  wordt" geeft autocorrelatie → filterwinst, $\rho_1\sigma\sqrt{2/\pi}$, en niet-synchrone
  handel).
- Simulatie zonder tegenhanger op echte data: *niet*, afgewezen met STYLE §11.7 en
  §11.11. Dit punt stond niet in mijn "Voor een 9" en telt niet mee voor het cijfer.
- Jensen en de sterke vorm: *opgelost*.

**3. Taal**
- "definieert het tijdvak": *opgelost* ("Met dat artikel begint het tijdvak").
- "men": *opgelost* (geen meer).
- Januari twee keer: *opgelost*.
- Wisselende namen: *opgelost* ("Martingaal na weging met de SDF"; "het constante model"
  vanaf de simulatie, daar gedefinieerd).

**4. Toy**
- Stap 4 met $Q$: *opgelost* (als "Vooruitblik" gemarkeerd; de theorie leidt het af).
- Risicocorrectie gelijk: *opgelost* ($120 - 116 = 80 - 76 = 4$).

**5. Code en figuren**
- `dict(zip(...))`: *opgelost* (expliciet woordenboek).
- `idxmax` zonder commentaar: *opgelost*.
- Wisselende buy-and-hold: *opgelost* (zin onder de tabel; de figuur neemt buy-and-hold
  over het hele venster).
- Code-achtige rijlabels: *opgelost* (Nederlandse labels in toy-, Samuelson- en
  deelperiodetabel).

**6. Replicatie**
- Kolom "na commissies" niet vergelijkbaar: *opgelost* langs de tweede weg die ik noemde:
  de kolom heet "na volle commissies (niet vergelijkbaar)" en de tekst zegt het. De
  0,1%-resultaten van Fama en Blume zijn niet in het project beschikbaar.
- Oordeel criteria 2 en 3: *opgelost* ("**Geslaagd** op criteria 2 en 3").
- Criterium 1 zonder grootte: *opgelost* ($252(\rho_1\sigma\sqrt{2/\pi} - \mu)$, voorspeld
  13,9, gemeten 12,9; nagerekend: $252(0{,}1752 \cdot 0{,}0068 \cdot 0{,}798 - 0{,}0004)
  \approx 0{,}139$).
- Bètaverschil: *opgelost* (1,01 tegen 0,84, "waarschijnlijk meer kas").

**7. Oefeningen**
- 3.2 zonder $c^{*}$: *opgelost* ($c^{*}$ alleen lang 0,16% en 0,27%, negatief na 1990).
- 2.1 zonder variantiestap: *opgelost*.

Geen verslechteringen, geen nieuwe feitelijke fouten.

| nr | criterium | gewicht | F5a | Controle 1 |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 8 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 8 | 9 |

**Eindcijfer: 9,0.**
