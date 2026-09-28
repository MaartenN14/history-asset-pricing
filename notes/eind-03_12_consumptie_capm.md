STATUS 03_12_consumptie_capm F6c words=5612 prose=PASS open=0 cijfer=9,2 min=9

# Eindbeoordeling: Lucas, Breeden en de SDF (F6)

## Ronde 9+

Vorige ronde: 8,7

Gelezen na de taalredactie (`notes/taal-03_12_consumptie_capm.md`). `prose_stats --check`: 5.469 woorden, PASS (zinslengte 16,9 gemiddeld, dubbele punt 3,5 per 1000, twaalf alinea's van één zin, bijna alle als overgang of celaankondiging). Getallen nagerekend tegen `nb_outputs` (15 cellen). Het punt uit controle 2 ("Daarboven", H8) is opgelost. Weging nu 25/20/20/10/10/10/5.

## De drie verbeteringen met het meeste effect

1. **Vier plekken in Theorie rechtzetten waar een woord of symbool iets anders zegt dan de wiskunde** (criterium 1, 8,5 → 9). De Lucas-operator is een gewogen *som*, geen gewogen gemiddelde (r. 333). De voorwaarde $\delta < 1$ is voldoende, niet nodig (r. 363–366). De $\gamma$ van Hansen en Singleton botst met de onze (r. 229). $R^m$ verschijnt in de propositie zonder naam (r. 399).
2. **De taal op de laatste plekken natuurlijk maken** (criterium 3, 8,5 → 9). Het gaat om de drie hardop-zinnen hieronder, "leverage (hefboom)" [onderzoek C], de SDF-definitie met dubbele punt tussen haakjes [onderzoek C], "lags" tegen "vertraging", vijf keer "op vier decimalen nul" [onderzoek C] en de tweede "standaardfout van 2%" zonder link.
3. **De slotclaim in "Waar het breekt" laten passen bij de waarschuwing en de simulatie** (criterium 2 en 6, 9 → 9,5). "De simulatie laat zien dat dit geen artefact van een kleine steekproef is" botst met de waarschuwing dat tijdsaggregatie $J_T$ te groot maakt. Ook noemt de tekst een verwerping "zeldzaam" terwijl de simulatie er één op de tien geeft.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,8** |

(0,25·8,5 + 0,2·9 + 0,2·8,5 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 8,775, afgerond 8,8.)

## 1. Helderheid van de uitleg (8,5)

*Goed.*
- Toy-voorbeeld: de lagere prijs-dividend-ratio in de hoge toestand krijgt een richting en een reden (rente ruim acht procentpunt hoger, rente-effect wint bij $\gamma = 2$), en oefening 1 keert het om voor $\gamma < 1$ (H6).
- Wat het voorspelt: rente en premie bij lognormale groei. Elke formule krijgt een getal (drempel 14,7, rente 8,6%, premie 0,25%), en de rente wordt ontleed in groei en voorzorgssparen.
- Hoe het getoetst wordt: GMM. De Euler-fout wordt eerst in woorden ingevoerd (een fout die niet mag samenhangen met wat de belegger wist), daarna pas als moment met Kronecker-product en een voorbeeld ($N = 2$, $L = 3$, zes momenten).

*Aanmerkingen.*
- Evenwicht in de Lucas-boom: "De ratio van vandaag is het gewogen gemiddelde van één plus de ratio van morgen, met als gewicht de kans maal $\beta g^{1-\gamma}$." De gewichten tellen op tot hoogstens $\delta < 1$ (in het toy 0,94 en 0,98). Dat is een gewogen som; juist dat de som onder één blijft, maakt $T$ een contractie. De redacteur signaleerde het en liet het staan.
- Evenwicht in de Lucas-boom: "Groeit het sneller, dan is [](#eq-consumptie-capm-contante-waarde) oneindig, zoals het Gordon-model ontploft bij $g \ge r$." $\delta$ is een supremum over toestanden en $\delta < 1$ is voldoende. Groeit het nut-gewogen dividend in één toestand sneller dan $1/\beta$, dan kan de prijs nog eindig zijn.
- Opzet en aannames: "Hansen en Singleton schrijven het nut als $c^{\gamma}/\gamma$ met $\gamma < 1$ en zetten $\alpha = \gamma - 1$." Dezelfde letter $\gamma$ betekent hier iets anders dan in de rest van het college (H7).
- Wat het voorspelt: rente en premie bij lognormale groei. $\log \E[R^{m}] - \log (1 + R^f) = \gamma\phi\sigma^2$ gebruikt $R^m$ zonder naam. Pas in het bewijs blijkt dat het het rendement op het aandeel in de boom is, en het subscript $m$ botst met de SDF $m_{t+1}$ (kaart §3).
- Idem: "Een hogere $\gamma$ versterkt beide krachten, zodat de rente met $\gamma$ stijgt zolang $\gamma < \mu/\sigma^2$ en daarboven het voorzorgssparen wint." Dat beide krachten sterker worden, verklaart niet waarom de rente eerst stijgt. De reden is dat de groeiterm lineair in $\gamma$ is en de voorzorgsterm kwadratisch.

*Beter uitleggen.* Waarom de gewichten van $T$ optellen tot $\delta$ en wat dat met de eindigheid van de prijs te maken heeft: één bijzin bij r. 333 met het toy-getal 0,98. Bij de rente: "lineair tegen kwadratisch" als reden voor de drempel.

*Voor een 9.* "gewogen som" in r. 333; "voldoende" en "in elke toestand" bij r. 363–366; de nutsfunctie van Hansen en Singleton met een eigen letter (r. 229–230); $R^m$ bij de propositie één keer benoemen als rendement op de boom, met een ander symbool of de zin dat $m$ hier de markt is (r. 392–399); de "zodat"-zin bij r. 421 herschrijven.

## 2. Opbouw en rode draad (9)

*Goed.*
- Overzicht stelt de vraag (waar komt de discontovoet vandaan) en geeft het antwoord (consumptie, maar te glad). De routekaart noemt de Euler-vergelijking de kern, en "Samengevat" sluit Theorie af.
- De drie voorspellingen uit de intuïtie worden elk op hun plek ingelost, elke keer in een andere vorm: de rente bij $\gamma\mu$ (r. 418–419), de covariantie bij de consumptiebèta (r. 496–498), de kleine premie met 0,25% (r. 431–433).
- Toy-getallen keren terug ($\delta = 0{,}9808$, stap 3 bij de rentevoet, stap 2 in de Lucas-operator), en de simulatie gebruikt precies de lognormale boom uit de propositie. De replicatie leest $\hat\beta > 1$ met de simulatie in de hand. 5.469 woorden.

*Aanmerkingen.*
- Wat er brak, en wat daarna kwam: "De simulatie laat zien dat dit geen artefact van een kleine steekproef is, want als het model waar is, zijn de schattingen wel onnauwkeurig, maar is een verwerping zeldzaam en zwak." De simulatie gaf één verwerping op de tien, en de waarschuwing vlak ervoor zegt dat tijdsaggregatie de $J$-statistieken te groot maakt. Die tweede bron van verwerping laat de simulatie buiten beschouwing, zodat de claim sterker is dan de simulatie draagt.
- Simulatie en Replicatie: elke figuur wordt drie keer uitgelegd, in de zin ervoor, het bijschrift en de alinea erna (r. 786–787, 816–823; r. 976–978, 999–1007) [onderzoek C, D4].

*Beter uitleggen.* Wat de simulatie wél uitsluit (een kleine steekproef alleen levert geen $J$ van 42 op; het 95e percentiel is 11,7) en wat niet (tijdsaggregatie).

## 3. Taal (8,5)

*Goed.* Na de redactie leest het college grotendeels als gesproken Nederlands. De intuïtie met het eiland heeft handelende onderwerpen en voegwoorden ("zodat de markt alleen de prijs vastlegt"), en de Euler-alinea (r. 236–240) is een voorbeeld van H1. Motiefnamen staan elk hoogstens twee keer, er is geen "Wie …"-zin en geen gedachtestreepje.

*Aanmerkingen.*
- Overzicht: "Deze jaren vonden het antwoord in consumptie, want een euro morgen is weinig waard als morgen een goede dag is, en veel als het een slechte dag is." Jaren vinden geen antwoord.
- Overzicht: "De *stochastic discount factor* (SDF, stochastische discontofactor: de willekeurige variabele waarmee we een toekomstige payoff verdisconteren) is dan de verhouding van marginale nutten" [onderzoek C]. Een definitie met dubbele punt tussen haakjes midden in de zin.
- Wat het voorspelt, lognormale groei: "Hier is $\phi$ de *leverage* (hefboom) van het dividend op consumptie" [onderzoek C]. Verderop staat alleen "hefboom", dus de Engelse term is overbodig.
- Replicatie tegen oefening 3: "twee tot zes lags als instrumenten" en "één lag" (r. 841–843) tegen "één vertraging van alle drie de variabelen" (r. 1207). Twee namen voor één begrip (H7).
- "op vier decimalen nul" staat vijf keer (r. 823, 943, 1049, 1072, 1250) en is daarmee een vaste wending geworden [onderzoek C].
- Vergelijking met 1983: "Hier zien we de standaardfout van 2% in zijn scherpste vorm" zonder link naar `#00-01-rendementen` (kaart §3).
- Wat het voorspelt, lognormale groei: "en een andere kalibratie geeft een andere drempel." Dit is een ingeplakte reparatiezin uit de vorige ronde (§11.12). Direct daarna herhaalt de volgende zin dezelfde $\mu$ en $\sigma$.
- Evenwicht in de Lucas-boom: "Deze stap laat daarom zien wanneer de Lucas-boom zo'n prijs heeft." Een zin over de tekst in plaats van over de boom.
- Overzicht: de opsomming "In dit college: …" met puntkomma's telt als één zin van 88 woorden (`sent_gt40 = 1`).

*Voor een 9.* De drie zinnen uit de hardop-toets herschrijven (r. 36–37, 105–107, 476–477); "leverage" schrappen (r. 385); de SDF-definitie in twee zinnen (r. 39–41); één term voor lags (r. 841–843, 1207); "op vier decimalen nul" hoogstens twee keer, elders "$p < 0{,}0001$" of "verwerpt ruim" (r. 823, 943, 1049, 1072, 1250); link bij r. 1045; de reparatiebijzin bij r. 424 schrappen; r. 313–314 over de boom laten gaan; de opsomming in het Overzicht met punten.

## 4. Toy-voorbeeld (9)

*Goed.* Breuken met noemers hoogstens 27, oplossing door optellen, PD 25 en 27 als hele getallen; tabel hand/code met de Euler-controle; de slotzin zegt wat het getal betekent (een gladde consumptie levert bijna geen premie). Eén mechanisme per uitkomst, en het rente-effect wordt in dezelfde alinea verklaard.

*Aanmerkingen.*
- Stap 4: de premie: "Vanuit de lage toestand is het verwachte rendement $(0{,}25 \cdot 1{,}04 \cdot 26 + 0{,}75 \cdot 0{,}96 \cdot 28)/27 = 0{,}99704$, tegen $0{,}99687$". Een premie van basispunten vraagt vijf decimalen; stap 3 en 4 bevatten samen meer dan tien getallen per alinea [onderzoek C, D5].
- "De twee kolommen zijn gelijk, op de afronding van de premie na." De eerste zin na de tabel zegt wat de lezer al ziet, niet wat het toy bewijst [onderzoek C, D2].

*Beter uitleggen.* Stap 3 en 4 kunnen in een kleine tabel (toestand, $\E[m]$, rente, verwacht rendement, premie), zodat de alinea's alleen de redenering dragen.

## 5. Code en figuren (9)

*Goed.* `euler_moments` maakt het Kronecker-product zichtbaar met een lus over activa; `gmm_euler` concentreert $\beta$ uit met commentaar dat zegt waarom; elke cel heeft een zin ervoor en erna; beide figuren hebben een leeswijzer vooraf en een bijschrift dat de conclusie trekt.

*Aanmerkingen.*
- Vergelijking met 1983: de kolom "verwerpt origineel" toont "ja (chi2(3) = 30.08)" met decimale punt in een Nederlandse presentatietabel.
- Zie opbouw: de drievoudige uitleg van beide figuren [onderzoek C, D4].

## 6. Replicatie en empirie (9)

*Goed.* Admonition met bron, wat, data, verschil en verwachte afwijking in ruim 150 woorden; tabel origineel/hier met omgerekende $\alpha$; oordeel "Geslaagd" dat naar het voorspelde patroon verwijst; rij (d) koppelt aan de figuur. De getallen staan in tabellen, en de proza verwijst naar kolommen.

*Aanmerkingen.*
- Replicatie-admonition: "Zij gebruikten maanddata 1959–1978, twee tot zes lags als instrumenten en in 1983 maximum likelihood." Rij (d) komt uit tabel 5 met NLAG = 0 (r. 1012–1013), dus het bereik is nul tot zes.
- De verwachte afwijking noemt de tijdsaggregatie niet, terwijl de waarschuwing onderaan zegt dat die onze $J$ te groot maakt. Juist dat hoort bij "wat verwachten we anders dan het origineel".

## 7. Oefeningen (9)

*Goed.* Instap als variatie op het toy (persistentie en $\gamma$), afleiding met controle op de gesimuleerde economie (consumptiebèta en 411 jaar voor $t = 2$), uitbreiding van de replicatie (jaardata en coronakwartalen). Elke uitwerking eindigt met een les in een gewone zin.

*Aanmerkingen.*
- Oefening 3: "instrumenten: constante en één vertraging van alle drie de variabelen" (zie taal, H7).

## Feitelijke fouten

Nagerekend tegen `nb_outputs`: toy (PD 25/27, rente 7,98% en −0,31%, premie 2,0 en 1,7 bp, $\delta = 0{,}9808$), rente 8,6% en drempel 14,7, premie 0,25% en 1,47% (cel 1,48%), simulatie (mediaan 2,8, 5–95% van −2,9 tot 11,9, SD 4,2 tegen SE 1,5, verwerping 9,8%, 95e percentiel $J$ 11,7, $\hat\beta > 1$ in 28,6%), $16/\sqrt{70} = 1{,}9$, volatiliteitsverhouding 16, 1947–2019 (c) $\hat\gamma = 17{,}3$ en $\hat\beta = 1{,}08$, nulpunt 75,2, oefening 2 (0,0145 tegen 0,0147, 411 jaar), oefening 3 (17 → 2,3 → −2,3). Het bewijs van de propositie klopt ($\tfrac12\sigma^2(\phi^2 - (\phi-\gamma)^2 + \gamma^2) = \gamma\phi\sigma^2$). Geen vakterm is door de redactie van betekenis veranderd, maar één onjuiste term bleef staan.

1. **r. 333** "het gewogen gemiddelde": de gewichten tellen op tot hoogstens $\delta < 1$. Juist is "gewogen som". Omdat een gewogen gemiddelde met gewichten die tot één optellen geen contractie geeft, staat de term haaks op de stelling eronder.
2. **r. 363–366** "Groeit het sneller, dan is … oneindig": $\delta < 1$ is een voldoende voorwaarde (supremum over toestanden). Oneindig is de prijs pas als het nut-gewogen dividend overal, of via de keten in verwachting, te snel groeit.
3. **r. 841** "twee tot zes lags": rij (d) komt uit tabel 5 met NLAG = 0 (r. 1012–1013).
4. **r. 1074–1075** "geen artefact van een kleine steekproef … een verwerping zeldzaam en zwak": de simulatie geeft 9,8% verwerpingen en bevat geen tijdsaggregatie, die volgens de waarschuwing (r. 1052–1054) $J$ opblaast. De claim is sterker dan de simulatie. Juist is dat een kleine steekproef alleen geen $J$ van 42 verklaart (95e percentiel 11,7).

## Navertelling in vijf zinnen

Rubinstein, Lucas en Breeden maakten de discontovoet de verhouding van marginale nutten, zodat de prijs van elk activum de verwachte payoff is, gewogen met $\beta(c_{t+1}/c_t)^{-\gamma}$. In een Lucas-boom volgt daaruit een unieke prijs-dividend-ratio die beweegt omdat de rente beweegt, een rente die stijgt met verwachte groei, en een premie gelijk aan $\gamma$ maal de covariantie met consumptiegroei. Omdat consumptie glad is, is die premie bij redelijke $\gamma$ klein (0,25% bij $\gamma = 2$). Hansen toetste de Euler-vergelijking met GMM zonder de economie op te lossen; een simulatie laat zien dat $\hat\gamma$ op zeventig jaar data slecht gemeten is en de $J$-toets wat te vaak verwerpt. Op Amerikaanse data verwerpt de toets het model met aandelen en T-bill samen ruim, en de premie alleen vraagt een $\gamma$ van 75 of meer, zodat het consumptie-CAPM als theorie is verworpen. Dit klopt met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk vloeiender gemaakt: telegramzinnen, "Wie"-zinnen, "*Waarom zou dit waar zijn?*" in Theorie en de vaste wendingen zijn weg, en verwijswoorden kloppen ("haar" voor premie en lezing is verdwenen). Er is geen vakterm van betekenis veranderd. "Verklaren" voor "dragen" en "waarderen" voor "prijzen" zijn juist. Wel bleef "gewogen gemiddelde" staan (feitelijke fout 1). Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 36–37: "Deze jaren vonden het antwoord in consumptie, want een euro morgen is weinig waard als morgen een goede dag is, en veel als het een slechte dag is." → "Tussen 1976 en 1983 vonden economen het antwoord in consumptie. Een euro morgen is weinig waard als morgen een goede dag is, en veel op een slechte dag."
2. r. 105–107: "We rekenen de prijs van de boom, de rente en de premie uit in een economie met twee toestanden, en de eerste cel laadt de pakketten die we in het hele college nodig hebben." → "We rekenen de prijs van de boom, de rente en de premie uit in een economie met twee toestanden. Eerst laden we de pakketten voor het hele college."
3. r. 476–477: "De consumptiebèta $\beta_{i,\Delta c}$, met twee indices, is een regressiecoëfficiënt, terwijl $\beta$ zonder index de subjectieve discontofactor blijft." → "Schrijf $\beta_{i,\Delta c}$ voor de regressiecoëfficiënt van $R^e_i$ op $\Delta c$; met de discontofactor $\beta$ deelt ze alleen de letter."

Bij volledige oplossing van alle punten: 9,2

## Controle 1

Gecontroleerd: `notes/rapport-03_12_consumptie_capm.md` sectie R9-1, tegen het college (één
keer volledig gelezen) en tegen `nb_outputs` (F6c-03_12_consumptie_capm-out.txt, 15 cellen)
en `prose_stats`/`nb_numbers`.

**Feitelijke fouten (4/4 opgelost).**
1. r. 333 "gewogen gemiddelde" → "gewogen som", met rijsom hoogstens 0,98 (toy:
   $\max(9/13+1/4;\ 3/13+3/4)=0{,}9808$, r. 374, nagerekend). Opgelost.
2. r. 363–369 $\delta<1$ heet nu expliciet voldoende maar niet nodig, met de voorwaarde
   langs de keten in plaats van in elke toestand apart. Opgelost.
3. r. 850–851 admonition: "nul tot zes lags" (tabel 4 NLAG = 2, tabel 1 NLAG = 6, tabel 5
   NLAG = 4 en 0, r. 1021–1022: bereik klopt). Opgelost.
4. r. 1081–1091 "Waar het breekt": nieuwe zin zegt dat een kleine steekproef $J = 42$ niet
   verklaart (95e percentiel 11,7, vier tegen zes vrijheidsgraden, nagerekend tegen cel 5
   en cel 9: 11,737 en 42,17) en dat tijdsaggregatie $J$ vergroot maar de $\gamma$ in de
   tientallen niet verklaart; "zeldzaam en zwak" geschrapt. Opgelost.

**Criterium 1, "Voor een 9" (5/5 opgelost).** "gewogen som" (zie boven); Hansen-Singleton
nut nu $c^{1+\alpha}/(1+\alpha)$ met eigen letter $\alpha$ (r. 232–235, $\hat\alpha=-0{,}931
\to \hat\gamma = 0{,}931$, klopt tegen cel 12 "gamma origineel" (a) 0,931); $R^m$ vóór de
propositie benoemd als rendement op de boom met "het subscript $m$ voor markt staat en niet
voor de SDF" (r. 394–395); de "zodat"-zin bij de rentedrempel herschreven met "lineair...
kwadratisch" (r. 429–431).

**Criterium 3, "Voor een 9" (9/9 opgelost).** Drie hardop-zinnen herschreven (r. 36–37,
104–105, 483–484, nagenoeg woordelijk als voorgesteld); "leverage" geschrapt (nu alleen
"hefboom", r. 391; de Engelse dict-key in code telt niet mee); SDF-definitie in twee
zinnen zonder dubbele punt (r. 38–40); één term "lag(s)" in de admonition en oefening 3
(r. 850–852, 1221); "op vier decimalen nul" nul keer meer aangetroffen; link bij de tweede
"standaardfout van 2%" (r. 1054, naar `#00-01-rendementen`); reparatiebijzin "andere
kalibratie" geschrapt; Lucas-boom-opener gaat nu over de boom (r. 314–317); Overzicht-
opsomming nu vijf bullets in plaats van één zin met puntkomma's.

**Bonus, niet vereist voor het plafond maar wel opgelost.** Criterium 2/6: figuurbijschrift
en -aankondiging minder drievoudig uitgelegd; criterium 6: verwachte afwijking noemt nu het
effect van kwartaaldata (kleinere SE, grotere $J$); criterium 5: "verwerpt origineel" met
komma (30,08; 10,93; 366,22, cel 12); criterium 7: oefening 3 gebruikt nu "lag" (H7).

**Nieuwe punten.** Geen; geen verslechtering gevonden, geen nieuwe feitelijke fout.

**Getallencontrole.** `prose_stats --check`: PASS, 5.612 woorden (was 5.469). `nb_numbers`:
18 meldingen (was 22), alle handmatige tussenstappen van het toy-voorbeeld die elders door
de code worden bevestigd, geen nieuwe. De vier herstelde punten kloppen tegen `nb_outputs`:
cel 5 geeft 95e percentiel $J$ = 11,737 (afgerond 11,7), cel 9 geeft $J$(c, 1947–2019) =
42,1686 (afgerond 42), de toy-rijsom 0,9808 volgt uit stap 1 (9/13+1/4 = 0,9423,
3/13+3/4 = 0,9808), en $\delta < 1$ voldoende-niet-nodig is een wiskundige eigenschap van
het bewijs, geen celgetal.

### Cijfers (Controle 1)

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9,5 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9,5 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **9,2** |

(0,25·9 + 0,2·9,5 + 0,2·9 + 0,1·9 + 0,1·9 + 0,1·9,5 + 0,05·9 = 9,15, afgerond 9,2 — gelijk
aan "bij volledige oplossing van alle punten" hierboven.)
