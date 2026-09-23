# Verbeterplan taal en didactiek

Status: goedgekeurd door de eigenaar op 2026-09-23 (alle aanbevelingen in §7). De
eenmalige voorbereiding uit §6 is uitgevoerd; de pilots (§7) kunnen starten.

Basis: volledige lezing van L8 (CAPM), L12 (consumptie-CAPM) en L20 (voorspelbaarheid),
steekproeven uit L2, L34 en `index.md`, een meting over alle 40 lectures
(`tools/prose_stats.py`), en vergelijking met twee QuantEcon-lectures
(`lucas_model`, `markov_asset`).

Dit plan verandert de **vorm** van de lectures: zinnen, alinea's, ordening binnen de
vaste kopjes, code-leesbaarheid. Daarnaast wordt geschrapt volgens de schraptoets van
STYLE §11.11, en boven 6.000 woorden gesplitst. Getallen die de tekst of een tabel
aanhaalt, blijven reproduceerbaar en gelijk, tenzij het rapport het verschil verklaart.
Presentatie mag veranderen (STYLE §11.11, uitvoerregel).
*Oorspronkelijk (2026-09-23, vervallen 2026-09-23 avond):* ~~Het verandert niet de
inhoud: welke papers, welke replicaties, welke getallen, welke notatie, welke vaste
kopjes. Resultaten in tabellen en figuren moeten na de herziening identiek zijn, tenzij
een taak hieronder expliciet iets toevoegt.~~

---

## 0. Samenvatting

De lectures zijn inhoudelijk rijk en de vaste opbouw uit STYLE.md werkt. Het probleem zit in
de uitvoering van de tekst en in de hoeveelheid per lecture:

1. **Zinnen en alinea's zijn te lang en te vol.** Gemiddeld 20 woorden per zin, één op de
   tien zinnen boven 35 woorden, 579 zinnen boven 40 woorden. Alinea's van 60 tot 70
   woorden met drie gedachten. QuantEcon: alinea's van één tot drie zinnen, één gedachte.
2. **Vertaald Engels.** Veel zinnen zijn in het Engels gedacht en woord voor woord
   vertaald: "de nul" voor de nulhypothese (37 keer), "Noteer dat" (30), "Twee dingen zijn
   hier te zien" (33), "Dit is de reden dat" (26), "epistemisch" (38), "precies" als
   stopwoord (312). Zie §3.12.
3. **Projectjargon lekt naar de lezer.** "Motief 1", "het 2%-motief", "L4", "Deel V",
   "de trap" komen 120 keer voor. De lezer heeft PLAN.md niet gelezen en weet niet wat
   "motief 3" is; `index.md` nummerde de motieven niet eens.
4. **Aanspreekvorm wisselt.** "U" in deel 0 en I (140 keer), "je" in L11, L15, L20 (118
   keer), soms in dezelfde alinea. STYLE.md §7 vraagt geen van beide.
5. **Engelse citaten en gedachtestreepjes als bindmiddel.** 638 lange aanhalingen, 650
   gedachtestreepjes, 1549 puntkomma's. Veel citaten staan onvertaald midden in een
   Nederlandse zin.
6. **Te veel stof per lecture.** L8 behandelt Sharpe-Lintner-Mossin, Black, Sharpe en
   Treynor, Jensen, GRS met bewijs, Fama-MacBeth, Shanken, errors-in-variables met bewijs,
   Miller-Scholes, BJS en drie replicaties. QuantEcon doet één model per lecture.
7. **Afleidingen zonder adem.** Vergelijking volgt op vergelijking zonder de zin die zegt
   wat er staat. Geen routekaart aan het begin van de theorie, geen "wat we nu hebben"
   aan het eind. Bewijzen van een halve pagina staan open in de hoofdtekst.
8. **Toy-voorbeelden niet altijd handrekenbaar.** L8 vraagt een matrixinversie, twee
   beleggers en marktclearing tegelijk, met breuken als 27/14 en 28/2025. L12 en L34
   laten zien hoe het wel kan.
9. **Getallenbrij in de replicatie.** Alinea's met tien tot vijftien getallen en
   $t$-waarden; de lezer kan niet zien of de replicatie geslaagd is.
10. **Code te compact.** Eenregelige trucs (`np.eye(n)[ranks * n // N] * n / N`,
    dubbele `argsort`), tabelbouw verweven met rekenwerk, cellen zonder aan- of
    afkondiging.
11. **Structuur binnen de kopjes is los.** Het Overzicht begint met drie alinea's
    geschiedenis voordat de lezer weet wat de lecture beweert; de imports-cel onderbreekt
    de eerste drie tekstsecties; Theorie heeft zes tot tien subsecties zonder vaste
    volgorde; het toy-voorbeeld leunt op een formule die pas later wordt afgeleid. Zie
    §3.13.

De oplossing is een herziening per lecture in twee taken (§5): eerst structuur en code,
dan taal. Eén set regels (§3) staat nu als STYLE.md §11, zodat nieuwe en herziene
lectures dezelfde meetlat hebben (§8).

---

## 1. Diagnose

### 1.1 Wat goed is en blijft

- De vaste opbouw (Waar we zijn → Overzicht → Intuïtie → Toy → Theorie → Simulatie →
  Replicatie → Wat er brak → Oefeningen). De kopjes blijven.
- Het replicatieblok met "verwachte afwijking". Uniek en waardevol.
- Figuurbijschriften die interpreteren in plaats van aslabels herhalen.
- "Wat er brak" met de vier vaste elementen en de twee lezingen.
- De intuïtiesecties zijn vaak echt goed (L2 muntworp, L12 eiland met boom, L34
  driehonderd onderzoekers). Dat niveau moet de rest van de lecture ook halen.
- De wiskunde klopt en is op niveau. Dit plan raakt geen afleiding inhoudelijk.

### 1.2 Taal

Meting over alle 40 lectures (lopende tekst zonder code, wiskunde en tabellen):

| metriek | nu (typisch per lecture) | doel |
|---|---|---|
| zinslengte gemiddeld | 20 woorden | ≤ 17 |
| zinslengte 90e percentiel | 35 | ≤ 28 |
| zinnen > 40 woorden | 10 tot 23 | ≤ 2 |
| alinealengte gemiddeld | 50 tot 70 woorden | ≤ 45 |
| "motief N", "L4", "Deel V" | 0 tot 9 | 0 |
| "u" / "je" | tot 39 / tot 29 | 0 |
| calques (§3.12) | 0 tot 12 | 0 |
| "precies", "ruwweg" en co | 4 tot 15 | ≤ 6 |
| aanhalingen van 25+ tekens | 4 tot 35 | ≤ 5 |
| gedachtestreepjes | 0 tot 59 | ≤ 10 |

Concrete patronen, met vindplaats:

**Stapelzinnen met puntkomma's en drie citaten** (L20, Overzicht):

> Stambaugh liet zien dat de voorspellende regressie in kleine steekproeven omhoog
> vertekend is; Hodrick en Valkanov dat de $t$-waarden van lange-horizonregressies met
> overlappende waarnemingen te optimistisch zijn; en Goyal en Welch dat vrijwel geen
> enkele voorspeller het historische gemiddelde *uit de steekproef* verslaat.
> Daartegenover staan drie verdedigingen: Cochrane's argument dat niet de aanwezigheid
> van rendementsvoorspelbaarheid maar de *afwezigheid* van dividendvoorspelbaarheid het
> bewijs levert, het argument van Campbell en Thompson dat een kleine $R^2$ economisch
> groot kan zijn, en de methode van Ferreira en Santa-Clara die het rendement in drie
> stukken knipt en elk stuk apart voorspelt.

Twee zinnen, 110 woorden, zes papers. Zie §4 voor de herschrijving.

**Vertaald Engels** (overal): "Onder de nul" (the null), "de omvang van de toets" (size
of the test), "Noteer dat" (note that), "Twee dingen staan er ook" (two things also
stand out), "Dit is de reden dat" (this is the reason that), "Dat is wat 'een theorie
van de discontovoet' betekent" (that is what X means), "in de taal van Cochrane" (in the
language of), "het hart van deze lecture" (the heart of), "tot vandaag" (to this day),
"Leg dit naast" (lay this next to), "aan het eind van de dag", "Les:" (Lesson:),
"Cochrane's" (Nederlands: Cochranes). De volledige lijst staat in §3.12.

**Projectjargon** (L8): "Dat is motief 3 in zijn zuiverste vorm", "De tweede tabel is
motief 1 in de cross-sectie", "de getallen die in L4 als gegeven werden verondersteld".
(L12): "alle drie horen bij het 2%-motief", "de rampenmodellen van Deel V". (L20): "Hier
sluit motief 1 zich."

**Aanspreekvorm door elkaar** (L12, Intuïtie): "Stel u een eiland voor met één boom.
[...] Hoeveel nut een euro geeft, hangt af van hoe rijk je bent". (L8): "De variantie
van dat gemiddelde meet u met de tijdreeks"; (L20): "kun je dat met een eeuw data
aantonen".

**Telegramstijl** (L8): "Nu rijen maal kolom:", "Terug:", "Nu de cross-sectie en GRS."
(L12): "Nu de econometrie.", "Tot slot de controle."

**Onvertaalde Engelse citaten in een Nederlandse zin** (L20): 'regressies op de
dividendopbrengst "less than 5% of monthly or quarterly return variances", maar "often
explain more than 25% of the variances of two- to four-year returns"'. (L34): twee
citaten van Santa-Clara van elk twee regels, onvertaald.

**Gekunstelde woordkeus**: "bestaansobject", "restpost", "vastgeknoopt", "de
puntschatting zegt zelfs iets meer dan alles", "de gewichten zijn verrassend rond"
(STYLE §7 verbiedt "verrassend"), "het eigen risico telt eenvoudigweg niet mee",
"epistemische wending".

**Vooruitverwijzingen in de hoofdtekst** (L8 verwijst in de theorie naar L13, L14, L26;
L12 naar L13 en "Deel V"). Wie van voren naar achteren leest, kan er niets mee.

### 1.3 Didactiek

**Stof per lecture.** L8 bevat vijf stellingen of proposities met bewijs, twee
admonitions met formules, drie replicaties en drie oefeningen met elk drie deelvragen.
Dat is een blok van een PhD-cursus, niet één lecture. L10 (7350 woorden proza) en L11
zijn vergelijkbaar. De vaste kopjes zijn niet het probleem; de hoeveelheid onder elk
kopje is dat.

**Toy-voorbeeld.** STYLE §1 vraagt "met pen en papier na te rekenen". L8 vraagt
$\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^e$ voor een 3×3-matrix, marktclearing over
twee beleggers, en bèta's als 9/7 en 27/14. L20 werkt met afwijkingen van gemiddelden,
wat abstract is maar wel narekenbaar. L12 (twee toestanden, lineair 2×2-stelsel) en L34
(tien $t$-waarden in een tabel) zijn de maat.

**Afleidingen.** De cursieve regel "*Waarom zou dit waar zijn?*" is er overal, maar is
vaak een samengeperst bewijs in woorden ("stap 3 en 4 zijn pure meetkunde") in plaats
van een economisch beeld. Daarna volgen vergelijkingen zonder de zin die zegt wat er
staat. QuantEcon houdt strak het patroon: één of twee zinnen motivatie, de vergelijking,
één of twee zinnen die haar in woorden lezen.

**Signposting.** Theorie-secties hebben zes tot tien subsecties zonder routekaart vooraf
en zonder tussenbalans. De lezer weet halverwege niet meer waar de afleiding heen gaat.

**Bewijzen.** GRS staat in een dropdown, maar errors-in-variables (L8), zero-beta (L8),
Cochrane-identiteit (L20) en de consumptiebèta (L12) staan open. In de praktijk is elk
bewijs boven zes regels een onderbreking van de hoofdlijn.

**Replicatie-tekst.** L8, alinea na de SML-tabel: twaalf getallen, vier $t$-waarden,
drie subperiodes in één alinea van 180 woorden. De conclusie staat pas aan het eind.
Een tabel origineel/hier/verschil plus twee zinnen oordeel is leesbaarder en eerlijker.

**Code.** Voorbeelden uit L8:

```python
ranks = np.argsort(np.argsort(ts_betas(R[form], f[form])))
onehot = np.eye(n_port)[ranks * n_port // n_stocks] * n_port / n_stocks
P = R @ onehot
```

Slim, kort, en voor een lezer die de lecture leest om te *leren* ondoorgrondelijk. In
L12 bouwt `gmm_euler` in 35 regels een tweestaps-GMM met geconcentreerde $\beta$,
grid-search en `minimize_scalar` in één functie. QuantEcon zet het model in een klasse
met benoemde velden, de operator in een aparte functie, en de iteratie in een zichtbare
lus.

**Cellen zonder tekst ertussen.** L8 toy: drie codecellen achter elkaar, dan één alinea
die alles tegelijk bespreekt.

**Oefeningen.** Op niveau, maar zonder instap. Oefening 1 is meteen een afleiding met
drie deelvragen.

### 1.4 Structuur per notebook

De vaste kopjes zijn goed en blijven. De beoordeling per sectie, met wat er binnen het
kopje beter kan:

| sectie | oordeel | wat beter kan |
|---|---|---|
| Waar we zijn in het verhaal | goed | "Wat we al weten" verwijst nu vaak naar drie of vier lectures; twee is genoeg |
| Overzicht | zwak | begint met geschiedenis en citaties; de lezer weet pas aan het eind wat de lecture beweert. QuantEcon opent met de vraag en een lijst van wat komt |
| imports-cel | hinderlijk | staat tussen Overzicht en Intuïtie; onderbreekt drie tekstsecties |
| Intuïtie | goed | taalregels toepassen; verder niets |
| Toy-voorbeeld | wisselend | L12 en L34 goed; L8 te zwaar; leunt soms op een formule die pas in Theorie komt |
| Theorie | te vol | zes tot tien subsecties zonder vaste volgorde, geen routekaart, geen samenvatting; numerieke oplossingen staan soms in Simulatie |
| Simulatie | soms dubbel | L12 en L20 hebben twee simulaties; één vraag over steekproeven is genoeg |
| Replicatie | blok te lang | het replicatieblok is een muur van 300 tot 400 woorden vóór de eerste code |
| Wat er brak | goed | alleen taalregels |
| Oefeningen | zwaar | geen instap-oefening; slotzin ontbreekt of wisselt |

Overwogen en afgewezen: (a) het toy-voorbeeld ná de kern van de theorie zetten, zoals
QuantEcon (theorie → voorbeeld → code). Afgewezen omdat de volgorde toy → theorie de
reden is dat de reeks bestaat; het werkt zodra het toy-voorbeeld écht elementair is en
hoogstens één formule als recept gebruikt. (b) Een samenvatting aan het einde van de
lecture. Afgewezen omdat "Wat er brak" die rol al vervult; de samenvatting hoort na de
theorie, waar de lezer hem nodig heeft. (c) Leerdoelen bovenaan. Afgewezen omdat "Welke
vraag staat open" dat al doet. (d) Lectures splitsen. Toegestaan boven 6.000 woorden (STYLE §11.11; besluit 2026-09-23 avond).

### 1.5 Wat QuantEcon anders doet

Bekeken: *Lucas model* (advanced) en *Asset Pricing: Finite State Models* (intermediate).

| QuantEcon | HAP nu | overnemen? |
|---|---|---|
| Alinea's van 1 tot 3 zinnen, veel witruimte | 4 tot 8 zinnen, 60 tot 70 woorden | ja |
| Overzicht: de vraag, dan een lijst van wat komt | drie alinea's geschiedenis | ja |
| Motivatie → vergelijking → lezing in woorden | vergelijking → vergelijking | ja |
| Eén model per lecture; twee lectures voor Lucas | vijf tot acht papers per lecture | ja, via budget (§3.11) |
| Code: klasse voor het model, functie voor de operator, zichtbare lus, docstring | compacte functies met trucs | ja |
| "Here's the code" vóór elke cel, één zin erna | cellen achter elkaar | ja |
| Oefening in één zin, oplossing volledig | drie deelvragen | deels: oefening 1 kort, 2 en 3 mogen zwaar |
| Geen intuïtiesectie, geen geschiedenis, geen samenvatting | wel | niet overnemen; HAP is hier beter |
| Engels | Nederlands | n.v.t. |

---

## 2. Uitgangspunten

1. **Schrappen volgens de schraptoets.** Een passage blijft alleen als de vraag van de
   lecture haar nodig heeft, als een andere lecture haar aanhaalt, of als ze het motief
   draagt. De rest wordt geschrapt of een oefening. Richtlengte 4.000 tot 5.500 woorden,
   bindend; boven 6.000 woorden na schrappen wordt gesplitst. Zie STYLE §11.11.
   *Oorspronkelijk (2026-09-23, vervallen 2026-09-23 avond):* ~~Inhoud blijft. Geen
   paper, replicatie, stelling of getal verdwijnt. Wat te veel is voor de hoofdlijn,
   verhuist naar een `{note}` met `:class: dropdown`, naar een oefening, of naar een
   `{prf:proof}` met `:class: dropdown`.~~
2. **Uitvoer volgens de uitvoerregel.** Getallen die de tekst of een tabel aanhaalt,
   blijven reproduceerbaar en gelijk, tenzij het rapport het verschil verklaart.
   Presentatie mag veranderen. Zie STYLE §11.11.
   *Oorspronkelijk (2026-09-23, vervallen 2026-09-23 avond):* ~~Uitvoer blijft identiek.
   Tabellen en getallen in de output veranderen niet door deze herziening. Code mag
   herschreven worden voor leesbaarheid, maar `tools/nb_outputs.py` moet vóór en na
   dezelfde tekstuitvoer geven, op de toevoegingen na die het plan noemt.~~
3. **De vaste kopjes blijven.** STYLE §1 blijft bindend. Er komt één nieuw blok bij
   ("Samengevat") en de imports-cel verhuist (§3.13).
4. **Één lecture, één agent.** Agents raken alleen hun eigen `lectures/<slug>.md` en
   `.ipynb`. STYLE.md, template en `index.md` zijn eenmalig vooraf aangepast (§6).
5. **Meetbaar waar het kan.** `tools/prose_stats.py --check` is onderdeel van de
   oplevering. Wat niet meetbaar is, staat in de afvinklijst (§5, taak B).

---

## 3. Regels (staan als STYLE.md §11)

### 3.1 Zinnen en alinea's

- Eén gedachte per zin. Richtlengte 12 tot 20 woorden; nooit boven 30 zonder reden, nooit
  boven 40.
- Een zin met een puntkomma wordt bijna altijd twee zinnen. Puntkomma's alleen in
  opsommingen van gelijksoortige korte delen.
- Het gedachtestreepje is geen bindmiddel. "X — en dat is Y" wordt "X. Dat is Y." Een
  tussenzin tussen streepjes wordt een aparte zin of vervalt. Maximaal tien per lecture,
  alleen voor een echte terzijde.
- Een alinea heeft één idee en drie tot zes zinnen. Een alinea die twee ideeën bevat,
  wordt gesplitst op de plek waar het tweede idee begint.
- Geen telegramstijl. "Nu rijen maal kolom:" wordt "Vermenigvuldig nu rij voor rij uit:".
  "Terug:" wordt "Terugsubstitueren geeft". "Nu de econometrie." wordt "Nu komt de
  econometrische vraag: hoe goed is $\gamma$ te schatten uit zeventig jaar data?"
- Een opsomming van drie of meer parallelle items (drie kritieken, vier aannames, drie
  replicaties) wordt een lijst, niet een zin.

### 3.2 Aanspreekvorm en toon

- Geen "u" en geen "je/jij/jouw" in de lopende tekst. Alternatieven: "we" voor de
  gezamenlijke afleiding ("we delen door $p_t$"), de onpersoonlijke vorm ("wie sorteert op
  bèta, ...", "een belegger die ...", "de lezer"), of gewoon de zaak zelf als onderwerp.
- "Stel u een eiland voor" wordt "Denk aan een eiland met één boom" of "Er is een eiland
  met één boom".
- In oefeningen de gebiedende wijs: "Bereken", "Laat zien", "Simuleer".
- Verboden: verrassend, eenvoudigweg, zoals bekend, triviaal, eenvoudig te zien,
  "let op dat", "merk op dat" als stopwoord. Wat opvalt, wordt gewoon gezegd.
- Stopwoorden: "precies", "ruwweg", "inderdaad", "in feite", "letterlijk" samen hoogstens
  zes keer per lecture. "Precies" alleen als het "exact" betekent. Per alinea hoogstens één
  "dus".

### 3.3 Projectjargon en verwijzingen

- De drie motieven hebben een vaste naam die `index.md` introduceert en die in de
  lectures letterlijk zo terugkomt:
  - "de standaardfout van 2%" (niet "motief 1", niet "het 2%-motief");
  - "risico of vergissing" (niet "motief 2");
  - "theorie of feit" (niet "motief 3", niet "epistemische status/wending").
  Waar een lecture het motief aanroept, zegt de zin wat het hier betekent:
  "De tweede tabel is motief 1 in de cross-sectie" wordt "De tweede tabel laat zien dat
  de standaardfout van 2% ook hier het laatste woord heeft: na veertig jaar data is de
  marktpremie nog steeds op 2,5 procentpunt na onbekend."
- Geen "L4", "L26", "Deel V" in de tekst. Altijd een cross-ref met de titel of een
  omschrijving: "in [de lecture over Markowitz](#01-04-markowitz)", "in de lectures over
  habit, long-run risk en rampen".
- Geen "de trap", "laag 1", "de didactische trap". Dat is bouwtaal.
- Vooruitverwijzingen: hoogstens twee per lecture buiten "Wat er daarna kwam", en dan als
  belofte in één bijzin ("we komen daar in [](#03-14-roll) op terug"). Geen inhoud uit een
  latere lecture gebruiken om een punt in deze lecture te maken.

### 3.4 Citaten en vaktermen

- Een Engels citaat komt niet midden in een Nederlandse zin. Twee opties: (a) parafrase in
  het Nederlands met de bron erbij; (b) het citaat als blokcitaat (`> ...`) met erboven
  één Nederlandse zin die zegt wat er staat. Optie (b) alleen als de letterlijke
  formulering ertoe doet (Santa-Clara, Fama, Cochranes "dog that did not bark").
- Getallen uit een paper worden in de tekst in het Nederlands genoemd met de tabel als
  bron; de Engelse zin eromheen hoeft niet mee.
- Vaktermen volgens STYLE §3: eerste keer cursief met uitleg tussen haakjes. Dat geldt ook
  voor Nederlandse termen die een PhD-student niet vanzelf kent: "affiene combinatie",
  "harmonisch gemiddelde", "MA(4)-proces", "Wishart-verdeeld", "idempotente projectie".
  Eén zin uitleg of een `{note}`.

### 3.5 Getallen

- Hoogstens drie getallen per alinea in lopende tekst. Meer getallen horen in een tabel
  (Markdown-tabel voor handgetallen, DataFrame voor uitkomsten).
- Elke vergelijking origineel/hier wordt een tabel met kolommen "origineel", "hier",
  en, waar zinvol, "verschil" of "SE". De tekst eronder geeft in twee tot vier zinnen het
  oordeel tegen de "verwachte afwijking" uit het replicatieblok: geslaagd, gedeeltelijk,
  mislukt, en waarom.
- $t$-waarden en $p$-waarden in de lopende tekst alleen als ze de conclusie dragen.

### 3.6 Vergelijkingen en afleidingen

- Elke `## Theorie` begint met een routekaart van drie tot vijf regels: "We leiden drie
  dingen af: (1) ..., (2) ..., (3) .... Het eerste is de kern; de andere twee zijn nodig
  voor de toetsen." Dat is de enige plek waar een lijst van wat komen gaat hoort.
- Het vaste ritme per stap: één of twee zinnen die zeggen waarom we de stap zetten, de
  vergelijking, één zin die de vergelijking in woorden leest ("Links staat de prijs, rechts
  de verwachte payoff gewogen met hoe hard een euro morgen nodig is"). Twee vergelijkingen
  direct achter elkaar alleen als de tweede een herschrijving van de eerste is.
- "*Waarom zou dit waar zijn?*" is een economisch beeld van twee tot vijf zinnen, niet een
  samenvatting van de bewijsstappen. Toets: iemand die de wiskunde overslaat, moet na deze
  regels het teken en de richting van het resultaat kunnen raden.
- Hoofdtekst: maximaal drie `{prf:theorem}` of `{prf:proposition}` met open bewijs.
  Elk bewijs langer dan zes regels gaat in `{prf:proof}` met `:class: dropdown`; de
  hoofdtekst houdt de stelling en één alinea bewijsidee.
- Nevenresultaten (Shanken-correctie, Treynor-maat, Rubinstein-opmerking, Valkanov)
  worden een `{note}` met `:class: dropdown` en een sprekende titel, of een oefening.
- Na de laatste theorie-subsectie, vóór `## Simulatie`, een blok:

  ````markdown
  ```{admonition} Samengevat
  :class: tip
  - Eén regel per resultaat, drie tot vijf regels, met het label van de vergelijking.
  - De laatste regel zegt wat de simulatie hierna toetst.
  ```
  ````

### 3.7 Toy-voorbeeld

- Handrekenbaar betekent: geen matrixinversie groter dan 2×2, geen breuken met noemers
  boven 100, elke stap op één regel narekenbaar. Twee toestanden of twee activa, hooguit
  drie.
- Eén mechanisme per toy. L8 doet nu twee dingen tegelijk (marktclearing én de SML). Kies
  het mechanisme dat de lecture draagt en laat de rest aan de theorie of aan oefening 1.
- Hoogstens één formule die nog niet is afgeleid, gegeven als recept in woorden en
  symbolen. Theorie leidt precies die formule als eerste af.
- Vorm: (1) de opzet in een tabel, (2) de stappen met de getallen erbij, één regel per
  stap, (3) één codecel die de getallen reproduceert, (4) een tabel "met de hand / code"
  als laatste expressie, (5) één zin die zegt wat de lezer nu weet. Geen drie codecellen
  achter elkaar.

### 3.8 Simulatie en replicatie

- De simulatie begint met drie zinnen: welke wereld we bouwen, wat daarin per constructie
  waar is, en welke vraag over steekproeven we stellen. Daarna pas parameters.
- Eén simulatie, één steekproefvraag. Een tweede simulatie wordt een oefening of een
  dropdown-note. Een numerieke oplossing van het model (fixed-point-iteratie, rooster)
  hoort in Theorie onder "### Numerieke oplossing".
- Elke codecel krijgt één zin ervoor en één zin erna. De zin erna leest het resultaat.
- Het replicatieblok is hoogstens 250 woorden; elk onderdeel hoogstens twee zinnen.
  Reekscodes en datumdetails staan in de codecel.
- De replicatie-uitkomst staat in één tabel origineel/hier (§3.5). Het oordeel volgt in
  een alinea die begint met "Geslaagd", "Gedeeltelijk geslaagd" of "Niet geslaagd".
- Subperiodes en robuustheidsvarianten die het oordeel niet veranderen, gaan naar een
  `{note}` met dropdown of een oefening.

### 3.9 Code

- Leesbaar boven kort. Geen `argsort(argsort())`, geen `np.eye(n)[idx]`-trucs, geen
  dict-comprehensions van meer dan één regel om een tabel te bouwen.
- Eén bewerking per regel waar de lezer moet kunnen volgen; tussenresultaten krijgen een
  naam die zegt wat ze zijn (`pre_ranking_beta`, niet `b0`).
- Rekenwerk en presentatie gescheiden: eerst de cel die rekent, dan de cel die de tabel of
  figuur maakt. Een cel van meer dan 25 regels wordt gesplitst, tenzij het één functie is.
- Een model met parameters wordt een kleine `dataclass` of een dict met benoemde velden,
  zoals QuantEcon's `LucasTree`.
- Lussen die de lezer moet zien (fixed-point-iteratie, Fama-MacBeth per maand, expanding
  window) blijven lussen.
- Functies krijgen een docstring van één regel in het Engels. Een `# TODO: naar hap.stats`
  blijft staan.
- Kolomnamen in presentatietabellen zijn Nederlands en volledig.

### 3.10 Oefeningen

- Oefening 1 is een instap: varieer het toy-voorbeeld en zeg wat er met het resultaat
  gebeurt. Eén of twee deelvragen, antwoord in tien regels.
- Oefening 2 is de afleiding; oefening 3 breidt de replicatie uit. Beide mogen zwaar zijn,
  maar elke deelvraag is één concrete vraag met één antwoord.
- Elke uitwerking eindigt met één zin die begint met "Wat dit leert:".

### 3.11 Lengte-budget

- Lopende tekst ≤ 5500 woorden zoals `tools/prose_stats.py` telt. Nu 4600 tot 7350.
- Hoofdtekst theorie: ≤ 3 stellingen met open bewijs, ≤ 6 subsecties.
- Wat erboven zit, verhuist in deze volgorde: naar een dropdown-`{note}`, naar een
  oefening, naar de lecture waar het beter past (alleen met melding in het rapport; de
  andere lecture wordt niet aangepast). Schrappen is niet aan de orde.

### 3.12 Vertaald Engels

De tekst is op veel plaatsen in het Engels gedacht en daarna vertaald. Dat geeft zinnen
die grammaticaal kloppen maar die geen Nederlandse econoom zo zou zeggen. De toets voor
de agent: "zou ik dit zo zeggen tegen een collega, in het Nederlands?"

Tellingen over alle 40 lectures op 2026-09-23 en de vervanging:

| calque | keer | Nederlands |
|---|---|---|
| "de nul" (the null) | 37 | de nulhypothese |
| "de omvang van de toets" (size of the test) | 2 | het werkelijke significantieniveau; hoe vaak de toets een waar model verwerpt |
| "marginaal (significant)" | tientallen | net wel / net niet significant |
| "Noteer dat" (note that) | 30 | weglaten, of "Let wel:" |
| "Onthoud dat" (remember that) | 4 | weglaten, of "Bedenk dat" |
| "Twee/Drie dingen zijn hier te zien" (two things ...) | 33 | Deze figuur laat twee dingen zien. / Er valt nog iets op. |
| "Dit is de reden dat" (this is the reason that) | 26 | Daarom |
| "Dat is wat X betekent" (that is what X means) | 4 | Dat betekent X |
| "in de taal van X" (in the language of) | 5 | in de termen van X; zoals X het zegt |
| "het hart van" (the heart of) | 2 | de kern van |
| "tot vandaag" (to this day) | 3 | nog altijd; tot op de dag van vandaag |
| "Leg dit naast" (lay this next to) | 1 | Vergelijk dit met |
| "de hele inhoud van" (the whole content of) | 2 | meer zegt X niet |
| "het punt (is)" (the point) | 13 | waar het om gaat |
| "aan het eind van de dag" | 1 | uiteindelijk |
| "Les:" (Lesson:) | 2 | Wat dit leert: |
| "Neem nu de data" (now take) | 6 | Kijk nu naar de data |
| "het interessante deel" | 1 | daar zit het interessante |
| "de vraag is of" (als stoplap) | 17 | de vraag gewoon stellen |
| "epistemisch(e status/wending)" | 38 | "theorie of feit"; is dit een theorie die getoetst wordt of een feit dat op een verklaring wacht? |
| "bestaansobject", "restpost", "vastgeknoopt" | 4 | iets waarvan alleen het bestaan is bewezen; sluitpost; gekoppeld aan |
| "precies" (exactly, als stopwoord) | 312 | schrappen, tenzij het "exact" betekent |
| "ruwweg" (roughly) | 24 | ongeveer |
| "in feite", "letterlijk", "inderdaad" | 16 | schrappen |
| "Cochrane's", "Merton's", "Sharpe's" | tientallen | Cochranes, Mertons, Sharpes (apostrof alleen na a, i, o, u, y en na een s-klank) |

Zinsbouw naar Engels model, niet automatisch meetbaar:

- Cleft-zinnen: "Het is de toets die dit belangrijk maakt" → "Juist de toets maakt dit
  belangrijk".
- "Wat X doet, is Y" → "X Y".
- Nominale stijl: "de afwezigheid van dividendvoorspelbaarheid" → "dat dividenden niet
  voorspelbaar zijn"; "de aanwezigheid van" → "dat er ... is".
- Engelse metaforen als gewone tekst: "de hond die niet blaft" mag één keer als naam van
  Cochranes argument, met uitleg; daarna "het ontbreken van dividendvoorspelbaarheid".
- "X is de reden dat Y" → "Door X geldt Y" of "Daarom Y".
- "Er is een economisch argument achter" (there is an argument behind) → "Daar zit een
  economisch argument achter".
- Lijdende vorm in ketens ("wordt ... gebruikt ... wordt ... geschat") → bedrijvend waar
  het onderwerp bekend is.

`tools/prose_stats.py --where lectures/<slug>.md` geeft de vindplaatsen van de meetbare
calques met regelnummer.

### 3.13 Structuur binnen de vaste kopjes

De kopjes van STYLE §1 blijven. Binnen de kopjes gelden deze afspraken (STYLE §11.7):

1. **Overzicht** krijgt een vaste micro-opbouw: (1) de vraag en het antwoord van deze
   lecture in twee zinnen; (2) een lijst van drie tot vijf punten met wat we afleiden,
   simuleren en repliceren; (3) één alinea geschiedenis met de citaties. Reden: de lezer
   weet dan in tien regels wat de lecture beweert, zoals bij QuantEcon.
2. **De imports-cel verhuist** naar het begin van `## Toy-voorbeeld`. Reden: de eerste
   drie secties worden doorlopende tekst; de cel staat waar de eerste code staat.
3. **Theorie** volgt waar mogelijk de `###`-volgorde: Opzet en aannames → Het
   kernresultaat → Wat het voorspelt → Hoe het getoetst wordt. Reden: elke lecture over
   een getoetst model heeft precies deze vier delen, en de lezer weet dan altijd in welk
   deel hij zit. Synthese-lectures (L38, L39) en zuiver theoretische lectures wijken af.
4. **Numerieke oplossingen** (fixed-point-iteratie, roosters) horen in Theorie, niet in
   Simulatie. Simulatie beantwoordt één vraag over steekproeven.
5. **Toy-voorbeeld** gebruikt hoogstens één nog niet afgeleide formule, als recept.
   Theorie leidt die formule als eerste af. Reden: nu leunt L12 en L20 op "de vergelijking
   die we in de theorie afleiden", en dat is een cirkel.
6. **Replicatieblok** hoogstens 250 woorden. Reden: het blok is nu een muur van 300 tot
   400 woorden vóór de eerste code; reekscodes en datumdetails horen in de codecel.
7. **Waar we zijn in het verhaal** verwijst in "Wat we al weten" naar hoogstens twee
   eerdere lectures.
8. **Oefeningen**: instap, afleiding, uitbreiding (§3.10).

Overwogen en afgewezen: toy ná de theoriekern; samenvatting aan het einde; leerdoelen
bovenaan; lectures splitsen (boven 6.000 woorden, STYLE §11.11). Zie §1.4.

### 3.14 Helderheidsregels (STYLE.md §11.10)

De regels in §3.1 tot §3.13 maken de tekst leesbaar. Of de uitleg ook *helder* is, is
een oordeel dat geen regel afdwingt. Wel is het te sturen. Uit de lezing van L8, L12 en
L20 komen twaalf verschillen tussen passages die werkten en passages die niet werkten.
Ze staan uitgeschreven, met controlevraag, in STYLE.md §11.10 (H1 tot H12). Kort:

| regel | wat een heldere passage deed | wat een onheldere passage deed |
|---|---|---|
| H1 waarom is een handeling | "koop een klein extra stukje, betaal met minder consumptie" (L12) | "stap 3 en 4 zijn pure meetkunde" (L8) |
| H2 symbolen en geleende resultaten hier uitgelegd | "$\rho$ = 25/26 = 0,96 bij een P/D van 25" (L20) | $\lambda_m = (A\mu_m - B)/D$ uit L4 zonder herhaling (L8) |
| H3 één stelling, één bewering | CAPM-stelling met vier benoemde stappen (L8) | GRS-stelling met $F$-verdeling én Sharpe-identiteit én schatterkeuze (L8) |
| H4 getal naast de formule | "$4^2/20^2 = 4\%$ van de variantie" (L20) | Shanken-correctie zonder getal tot drie alinea's later (L8) |
| H5 aannames waar ze werken | "omdat $m$ niet de minimum-variantieportefeuille is" (L8, Black) | aannames 1 tot 4 bovenaan, daarna nooit aangeroepen |
| H6 beide richtingen | "$\gamma < 1$: ratio stijgt met groei; $\gamma > 1$: daalt" (L12) | "de helling wordt naar nul getrokken" zonder de andere kant |
| H7 één naam per begrip | | dividend-prijsratio / dividendopbrengst / $dp$ / D/P door elkaar (L20) |
| H8 "dat" verwijst naar de vorige zin | | "Dat is precies het patroon", "Die vorm is blijven hangen" (L8) |
| H9 conclusie vooraan | "De tabel bevat al het hele probleem" als eerste zin (L12) | BJS-conclusie na 180 woorden getallen (L8) |
| H10 abstracties met exemplaar | "instrumenten: een constante, vorige consumptiegroei en vorig rendement" (L12) | "$L$ instrumenten in $z_t$" zonder voorbeeld |
| H11 toy-getallen komen terug | $\gamma_m = 4{,}5$ uit het toy in de theorie (L8) | toy-getallen die daarna nooit meer voorkomen |
| H12 intuïtie voorspelt, theorie lost in | "aandelen moeten daarom een hoger rendement bieden, evenredig met..." (L12) | intuïtie zonder voorspelling, theorie zonder terugverwijzing |

Daarnaast de **navertel-toets**: de koude lezer schrijft na elke sectie in twee of drie
zinnen op wat hij geleerd heeft. Wijkt dat af van wat de schrijver bedoelde, dan was de
uitleg niet helder, welke regels er ook zijn gevolgd. Dit is de enige toets die
helderheid zelf meet in plaats van vorm.

---

## 4. Voorbeelden vóór en na

**A. Stapelzin (L20, Overzicht)**

Na:

> De twintig jaar daartussen zijn het interessante deel. Er kwamen drie kritieken.
> Stambaugh liet zien dat de geschatte helling in kleine steekproeven te hoog uitvalt.
> Hodrick en Valkanov lieten zien dat de $t$-waarden bij lange horizons te mooi zijn.
> Goyal en Welch lieten zien dat bijna geen enkele voorspeller buiten de steekproef het
> historische gemiddelde verslaat.
>
> Daar staan drie verdedigingen tegenover. Cochrane draaide het bewijs om: niet de
> voorspelbaarheid van rendementen is het bewijs, maar het ontbreken van voorspelbaarheid
> van dividenden. Campbell en Thompson lieten zien dat een kleine $R^2$ economisch groot
> kan zijn. Ferreira en Santa-Clara knipten het rendement in drie stukken en voorspelden
> elk stuk apart.

Citaties blijven op dezelfde plekken; ze zijn hier weggelaten. (De eerste zin bevat nog
"het interessante deel"; beter: "In de twintig jaar daartussen gebeurde het meeste.")

**B. Projectjargon (L8)**

Voor: "Dat is motief 3 in zijn zuiverste vorm — een *theorie met tests*."
Na: "Het CAPM is daarmee het zuiverste voorbeeld van een theorie die zich laat toetsen:
één voorspelling, één getal dat nul moet zijn."

Voor: "De tweede tabel is motief 1 in de cross-sectie."
Na: "De tweede tabel laat zien dat de standaardfout van 2% ook in de cross-sectie het
laatste woord heeft."

**C. Aanspreekvorm, telegramstijl en calques (L12, L8, L20)**

Voor: "Stel u een eiland voor met één boom. [...] hangt af van hoe rijk je bent".
Na: "Denk aan een eiland met één boom. [...] hangt af van hoe rijk iemand is".

Voor: "De variantie van dat gemiddelde meet u met de tijdreeks van de portefeuille".
Na: "De variantie van dat gemiddelde volgt uit de tijdreeks van die portefeuille".

Voor: "Nu rijen maal kolom:" Na: "Vermenigvuldig nu rij voor rij uit:".

Voor: "Onder de nul ziet een op de vijf steekproeven een rendementshelling groter dan in
de data". Na: "Onder de nulhypothese vindt een op de vijf steekproeven een grotere
rendementshelling dan de data laten zien."

Voor: "Drie dingen zijn hier te zien, en alle drie horen bij het 2%-motief."
Na: "De figuur laat drie dingen zien. Alle drie komen neer op de standaardfout van 2%."

Voor: "Dit is wat 'een theorie van de discontovoet' betekent". Na: "Dat betekent 'een
theorie van de discontovoet'".

**D. Getallenbrij naar tabel (L8, replicatie BJS)**

Voor: één alinea van 180 woorden met twaalf getallen en drie subperiodes.

Na:

| periode | helling $\hat\gamma_1$ | marktpremie | intercept $\hat\gamma_0$ |
|---|---|---|---|
| BJS 1931–1965, aandelen | 1,08 | 1,42 | 0,36 ($t = 6{,}5$) |
| hier 1931–1965, portefeuilles | 1,06 | 0,93 | −0,06 |
| hier 1931–1939 | 2,67 | 0,84 | −1,82 |
| hier 1957–1965 | −0,76 | 0,58 | 1,79 |

> Over de hele periode vinden wij dus geen te vlakke lijn. De subperiodes laten zien
> waarom: de jaren dertig belonen hoge bèta's ruim, en onze basisactiva zijn op grootte
> gesorteerd, zodat hoge bèta en kleine bedrijven in die jaren samenvallen. Vanaf 1939
> is het patroon van BJS er wel: de helling daalt en het intercept stijgt, in 1957–1965
> zelfs met het verkeerde teken. **Gedeeltelijk geslaagd**: het teken klopt zodra de
> jaren dertig buiten beschouwing blijven, zoals het replicatieblok voorspelde.

**E. Vergelijking met lees-zin (L8, GRS)**

Na de GRS-formule:

> In woorden: de teller meet hoe ver de alfa's gezamenlijk van nul liggen, gewogen met
> hoe sterk ze samenhangen. De noemer corrigeert voor hoe goed de markt zelf het in de
> steekproef deed. Een grote waarde zegt dat er een combinatie van de testactiva bestaat
> die de markt duidelijk verslaat.

**F. Code (L8, simulatie)**

Voor:

```python
ranks = np.argsort(np.argsort(ts_betas(R[form], f[form])))
onehot = np.eye(n_port)[ranks * n_port // n_stocks] * n_port / n_stocks
P = R @ onehot
```

Na:

```python
pre_ranking_beta = ts_betas(R[form], f[form])
group = pd.qcut(pre_ranking_beta, n_port, labels=False)     # 0 = laagste bèta
P = np.column_stack([R[:, group == g].mean(axis=1) for g in range(n_port)])  # gelijkgewogen
```

Zelfde uitvoer, drie regels die een lezer kan navertellen.

**G. Overzicht (nieuwe micro-opbouw, L8)**

> Welk verwacht rendement hoort bij welk risico als iedereen doet wat Markowitz
> voorschrijft? Het CAPM antwoordt: alleen de meebeweging met de markt wordt beloond, en
> voor iedereen tegen dezelfde prijs. In deze lecture:
>
> - leiden we het CAPM af uit de tangentportefeuille en marktclearing;
> - laten we zien dat een toets van het CAPM een toets is van één uitspraak: de markt is
>   mean-variance-efficiënt;
> - simuleren we waarom toetsen op individuele aandelen een te vlakke lijn vinden, ook
>   als het CAPM waar is;
> - repliceren we Black, Jensen en Scholes (1972) en Fama en MacBeth (1973) op
>   French-data.
>
> Tussen 1961 en 1966 schreven Treynor, Sharpe, Lintner en Mossin het model grotendeels
> onafhankelijk van elkaar op {cite}`...`. Het definieert het tijdvak omdat het de eerste
> theorie is die niet zegt wat een belegger moet doen, maar wat prijzen zijn.

---

## 5. Werkorder per lecture (voor bouw-agents)

Eén agent per lecture. Vooraf lezen: dit plan volledig, STYLE.md (in het bijzonder §11),
`lectures/_template.md` (het voorbeeld van de nieuwe vorm), de lecture zelf, en van de
lecture ervoor en erna alleen "Waar we zijn" en "Wat er brak". De lecture ervoor en erna
worden niet aangepast.

Bestanden die de agent mag aanraken: `lectures/<slug>.md` en `lectures/<slug>.ipynb`.
Niets anders. Ontbreekt iets in `hap` of in de bib: melden, niet oplossen.

### Taak 0: nulmeting (geen wijziging)

```powershell
uv run python tools/prose_stats.py lectures/<slug>.md
uv run python tools/prose_stats.py --where lectures/<slug>.md
git show HEAD:lectures/<slug>.ipynb > "$env:TEMP/voor.ipynb"
uv run python tools/nb_outputs.py "$env:TEMP/voor.ipynb" > "$env:TEMP/voor.txt"
```

In het rapport: de regel uit `prose_stats` en een lijst van de vijf grootste problemen
van deze lecture, elk met vindplaats (kopje) en welke regel uit §3 erop slaat.

### Taak A: structuur, didactiek en code

In deze volgorde, zodat er geen tekst wordt gepolijst die daarna verhuist:

1. **Stofreductie (§3.6, §3.11).** Kies de hoofdlijn: welke drie stellingen dragen de
   lecture? Verplaats de rest naar dropdown-notes of oefeningen. Bewijzen boven zes regels
   in dropdown. Noteer elke verplaatsing in het rapport.
2. **Overzicht (§3.13).** Herschrijf naar vraag en antwoord, lijst, één alinea
   geschiedenis. Verplaats de imports-cel naar het begin van het toy-voorbeeld.
3. **Routekaart en Samengevat (§3.6).** Voeg de routekaart toe aan het begin van
   `## Theorie` en het blok "Samengevat" aan het eind. Orden de `###`-subsecties waar
   mogelijk als Opzet → Kernresultaat → Wat het voorspelt → Hoe het getoetst wordt.
4. **Toy-voorbeeld (§3.7).** Als het niet handrekenbaar is: vereenvoudig tot één
   mechanisme. Vorm: opzet-tabel, stappen, één codecel, tabel hand/code, één zin.
   Hoogstens één nog niet afgeleide formule, als recept.
5. **Lees-zinnen (§3.6).** Elke genummerde vergelijking krijgt de zin die haar in woorden
   leest, als die er nog niet staat.
6. **Simulatie (§3.8).** Eén simulatie, één steekproefvraag. Numerieke oplossingen naar
   Theorie; een tweede simulatie naar een oefening of dropdown.
7. **Cellen (§3.8).** Elke codecel één zin ervoor en één erna.
8. **Tabellen (§3.5, §3.8).** Getallenalinea's in simulatie en replicatie worden tabel
   plus oordeel. Replicatieblok inkorten tot 250 woorden. Replicatie-oordeel begint met
   "Geslaagd" / "Gedeeltelijk geslaagd" / "Niet geslaagd".
9. **Code (§3.9).** Herschrijf voor leesbaarheid. Voor de uitvoer geldt de uitvoerregel
   van STYLE §11.11: aangehaalde getallen blijven gelijk, presentatie mag veranderen,
   elk verschil staat in het rapport. *Oorspronkelijk:* ~~Uitvoer moet identiek
   blijven.~~
10. **Oefeningen (§3.10).** Oefening 1 wordt een instap; elke uitwerking eindigt met
    "Wat dit leert:".

Verificatie (uitvoer letterlijk in het rapport):

```powershell
uv run jupytext --sync lectures/<slug>.md
$env:HAP_OFFLINE = "1"
uv run jupytext --execute --to ipynb lectures/<slug>.md
uv run python tools/nb_outputs.py lectures/<slug>.ipynb > "$env:TEMP/na.txt"
git diff --no-index "$env:TEMP/voor.txt" "$env:TEMP/na.txt"
```

De diff mag alleen verschillen tonen die in het rapport als bedoeld staan (nieuwe
hand/code-tabel, andere kolomnamen, verplaatste cellen). Een veranderd getal is een
fout.

Commit: `L<nr> <slug>: structuur, toy en code herzien volgens verbeterplan`.

### Taak B: taal

Herschrijf alle lopende tekst volgens §3.1 tot en met §3.5 en §3.12, kopje voor kopje,
inclusief admonitions, figuurbijschriften, oefeningen en uitwerkingen. Inhoud, volgorde
van argumenten en citaties blijven; alleen de zinnen veranderen. Bijzondere aandacht:

- "Waar we zijn in het verhaal": drie alinea's van elk hoogstens vier korte zinnen,
  hoogstens twee verwijzingen naar eerdere lectures.
- "Wat er brak": de vier vetgedrukte elementen blijven; elk hoogstens 120 woorden.
- Elke `{cite}` blijft op een plek waar hij bij de bewering hoort.
- Loop `prose_stats --where` na en los elke treffer op; controleer daarna de niet-meetbare
  calques uit §3.12 met de hand.

Verificatie:

```powershell
uv run python tools/prose_stats.py --check lectures/<slug>.md
uv run jupytext --sync lectures/<slug>.md
$env:HAP_OFFLINE = "1"
uv run jupytext --execute --to ipynb lectures/<slug>.md
uv run jupyter book build --html 2>&1 | Select-String -Pattern "<slug>|⛔|⚠"
```

`prose_stats --check` moet PASS geven. Een FAIL op `words` mag alleen blijven staan met
een regel in het rapport waarom de stof niet verder verplaatst kon worden.

Afvinklijst: STYLE.md §11.9. In het rapport alleen de punten die niet voldoen, plus
"overige: ok".

Commit: `L<nr> <slug>: taal herschreven volgens verbeterplan`.

In taak A en B past de schrijver ook de helderheidsregels H1 tot H12 toe (STYLE.md
§11.10). Taak C controleert ze.

### Taak C: koude lezer

Een **aparte agent**, die het rapport van taak A en B en de diagnose uit dit plan niet
heeft gezien. Hij krijgt alleen: de herziene `lectures/<slug>.md`, STYLE.md §11.10, en de
opdracht hieronder. Hij wijzigt niets.

Opdracht voor de lezer (letterlijk mee te geven):

> Lees `lectures/<slug>.md` van voren naar achteren als een eerstejaars PhD-student die
> de eerdere lectures heeft gelezen maar niet paraat heeft. Schrijf
> `notes/lezer-<slug>.md` met drie delen.
>
> 1. **Navertel-toets.** Na elke `##`-sectie, en in Theorie na elke `###`, twee of drie
>    zinnen: wat beweert de sectie en wat heb ik geleerd? Schrijf op wat je begreep, niet
>    wat er staat.
> 2. **De twaalf controles** uit STYLE.md §11.10, H1 tot H12. Per regel een lijst van
>    vindplaatsen: het kopje en de zin waar het misgaat, letterlijk geciteerd. Een lege
>    lijst is ook een antwoord.
> 3. **Waar ik het spoor kwijtraakte.** De drie plekken waar je niet meer wist waarom
>    deze stap nu kwam, met de zin waar dat begon.
>
> Geen stijlopmerkingen, geen wiskundige correcties, geen herschrijfvoorstellen: alleen
> wat je begreep en waar je vastliep.

Daarna lost de **schrijvende agent** (dezelfde als taak A en B) elk punt op of wijst het
af met één regel reden. Van de navertel-toets meldt hij elke sectie waar de samenvatting
van de lezer afwijkt van wat de sectie moest zeggen, en wat hij daaraan heeft veranderd.

Verificatie na de correcties: dezelfde commando's als taak B (`prose_stats --check`,
sync, execute offline, build), plus `nb_outputs`-diff tegen de versie na taak A.

Commit: `L<nr> <slug>: helderheid na lezersreview`. Het bestand `notes/lezer-<slug>.md`
wordt in dezelfde commit verwijderd; de inhoud staat samengevat in het rapport.

Voor de pilots is één lezersronde genoeg. Blijkt na de pilot dat de lezer per lecture
meer dan tien punten vindt, dan krijgt elke lecture een tweede ronde.

### Rapport (max 50 regels)

1. Nulmeting en eindmeting uit `prose_stats` (twee regels).
2. Top-5 problemen uit taak 0 en wat ermee is gebeurd.
3. Wat is verplaatst (naar dropdown, oefening, of "past beter in L<nr>").
4. De `nb_outputs`-diff, samengevat, met de bedoelde verschillen benoemd.
5. Afvinklijst: alleen wat niet voldoet.
6. Lezersreview: aantal punten per H-regel, de secties waar de navertel-toets afweek, en
   wat is afgewezen met reden.
7. Commit-hashes.
8. Open punten: wat de agent niet kon oplossen zonder STYLE.md, `hap` of een andere
   lecture aan te raken.

---

## 6. Eenmalige voorbereiding (uitgevoerd 2026-09-23)

1. **STYLE.md §11** toegevoegd: taal, vertaald Engels, afleidingen, structuur binnen de
   kopjes, code, en de aanvulling op de afvinklijst.
2. **`lectures/_template.md`** herschreven als voorbeeld van de nieuwe vorm: Overzicht
   met vraag en antwoord, imports-cel bij het toy-voorbeeld, toy met opzet-tabel en tabel
   hand/code, routekaart, lees-zinnen, bewijs in dropdown, "Samengevat", één simulatie
   met één vraag, replicatieblok kort met tabel origineel/hier en oordeel, drie
   oefeningen (instap, afleiding, uitbreiding) met "Wat dit leert:". De template is nog
   niet opnieuw uitgevoerd; dat gebeurt bij de eerste pilot.
3. **`lectures/index.md`** herschreven: de drie thema's hebben hun vaste naam, korte
   zinnen, geen "u", het Santa-Clara-citaat als blokcitaat met Nederlandse inleiding.
4. **`tools/prose_stats.py`** (met `--check` en `--where`) en **`tools/nb_outputs.py`**.
5. **BOUW.md**: verwijzing naar deze werkorder voor herzieningen.

Niets is gecommit; de eigenaar beslist over de commit van de voorbereiding.

---

## 7. Volgorde, pilots en besluiten

**Besluiten van de eigenaar (2026-09-23).** Alle aanbevelingen zijn overgenomen:

1. Stofreductie: schrappen volgens de schraptoets (STYLE §11.11) (besluit eigenaar,
   2026-09-23 avond). *Oorspronkelijk:* ~~taal plus verplaatsen naar dropdowns en
   oefeningen; niets schrappen.~~
2. Splitsen boven 6.000 woorden na schrappen (STYLE §11.11) (besluit eigenaar,
   2026-09-23 avond). *Oorspronkelijk:* ~~Lectures niet splitsen; na de pilot van L8
   opnieuw bekijken.~~

*Aanleiding voor de wijziging van besluit 1 en 2 (2026-09-23 avond).* De vier herziene
pilots groeiden van ongeveer 5.000 naar 7.000 tot 8.100 woorden, omdat schrappen
verboden was. De rubriek trekt voortaan niet af voor projectkeuzes (rubriek, "Wat niet
meetelt").
3. Aanspreekvorm: geen "u", geen "je"; "we" en de onpersoonlijke vorm.
4. Engelse citaten: parafrase; blokcitaat alleen waar de bewoording telt.
5. "Samengevat"-blok als vast element.
6. Extra, op verzoek: aandacht voor vertaald Engels (§3.12) en de structuur binnen de
   kopjes (§3.13). De imports-cel verhuist naar het toy-voorbeeld.
7. Los van dit plan, maar vóór de eindbuild: de TOC in `myst.yml` verwijst voor L0 tot
   L22 naar `.ipynb` en daarna naar `.md`. Advies: overal `.md`.

**Pilot.** Drie lectures eerst, elk door een eigen agent, daarna review door de eigenaar
vóór de rest start: L8 (CAPM; zwaarste stofreductie), L12 (consumptie-CAPM; toy en
intuïtie zijn al goed, dus de winst zit in taal, structuur en code) en L20
(voorspelbaarheid; veel citaten en getallen). Na de pilot worden §3 en §8 bijgesteld
waar de praktijk dat vraagt.

**Daarna.** Batches van vijf lectures parallel (aparte bestanden, geen gedeelde staat;
`references.bib` wordt niet aangeraakt). Per batch één gezamenlijke build aan het eind;
parallelle builds gaven eerder geheugenfouten. Volgorde: deel 0 en I eerst (meeste
"u"-vormen en streepjes), dan II tot VII, synthese als laatste (L38, L39 verwijzen naar
alles).

---

## 8. Meetlat

Drempels van `tools/prose_stats.py --check`, per lecture:

| metriek | maximum | hard of richtwaarde |
|---|---|---|
| words (alle lezerstekst, ook dropdowns en uitwerkingen) | 5500 | hard (STYLE §11.11); geen overschrijding met reden. *Tot 2026-09-23 avond:* ~~richtwaarde; overschrijding met reden in rapport~~ |
| sent_mean | 17 | richtwaarde |
| sent_p90 | 28 | richtwaarde |
| sent_gt40 | 2 | hard |
| para_mean | 45 | richtwaarde |
| dash | 10 | hard |
| semicol | 15 | richtwaarde |
| motief, Lnum, deel | 0 | hard |
| u_form, je_form | 0 | hard |
| taboo | 0 | hard |
| stopw (precies, ruwweg, inderdaad, in feite, letterlijk) | 6 | hard |
| calque (lijst in het script) | 0 | hard |
| engquote | 5 | hard |

Nulmeting over alle 40 lectures op 2026-09-23: zie de uitvoer van
`uv run python tools/prose_stats.py`. Ter referentie de drie pilots vóór de herziening:

| lecture | words | sent_mean | sent_p90 | sent_gt40 | para_mean | dash | semicol | motief | Lnum | u | je | engquote |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 02_08_capm | 6389 | 20,3 | 35 | 20 | 59 | 38 | 57 | 3 | 5 | 3 | 0 | 16 |
| 03_12_consumptie_capm | 5822 | 19,9 | 35 | 14 | 57 | 29 | 45 | 0 | 0 | 3 | 4 | 6 |
| 04_20_voorspelbaarheid | 5473 | 19,9 | 34 | 14 | 59 | 7 | 40 | 2 | 0 | 0 | 9 | 16 |

Het script is een hulpmiddel, geen rechter: een lecture die alle drempels haalt maar
niet leest als één verhaal, is niet klaar. De afvinklijst in STYLE.md §11.9 en de review
van de eigenaar na de pilot blijven leidend.
