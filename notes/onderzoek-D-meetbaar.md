Status: onderzoek D (taal, meetbaarheid) afgerond 2026-09-28. Niets gewijzigd in lectures/ of tools/. Testscripts: $TEMP/onderzoek-D-test.py en onderzoek-D-test2.py.

# Onderzoek D: welke taalpatronen zijn meetbaar, en welke drempels duwen verkeerd

Gelezen: W = `01_03_williams_ddm.md`, C = `02_08_capm.md`, E = `03_13_equity_premium_puzzle.md`,
R = `00_01_rendementen.md` (volledig), `tools/prose_stats.py` (volledig), STYLE §7 en §11,
`plannen/rubriek-didactiek.md`, `plannen/kaart-rollen.md` §5.

Meetmethode: het testscript maskeert code, math-blokken, kopjes, tabellen en directive-regels,
vervangt inline-wiskunde door `X` en houdt de regelnummers gelijk. De regexen hieronder draaien op
die gemaskeerde tekst. "Treffers" zijn alle vier de colleges samen, met de verdeling W/C/E/R.
"Vals" betekent: de regex vindt het patroon, maar de zin is in orde. Die telling heb ik met de hand
gedaan op de getoonde vindplaatsen.

## 0. Uitgangscijfers (huidige prose_stats en extra maten)

| college | sent_mean | p90 | para_mean | zinnen ≤ 6 woorden | alinea's van één zin | `: ` + kleine letter midden in een zin | dash | stopw |
|---|---|---|---|---|---|---|---|---|
| W | 14,8 | 25 | 45 | 10% | 20 van 125 (16%) | 71 (13,1 per 1000 w) | 0 | 0 |
| C | 14,4 | 23 | 42 | 12% | 26 van 128 (20%) | 66 (12,4 per 1000 w) | 0 | 1 |
| E | 15,2 | 24 | 45 | 9% | 25 van 118 (21%) | 55 (10,3 per 1000 w) | 0 | 1 |
| R | 14,3 | 22 | 43 | 10% | 26 van 118 (22%) | 71 (14,0 per 1000 w) | 0 | 1 |

Alle vier de colleges zitten ruim onder de zinsdrempel van 17 en tegen de alineadrempel van 45 aan.
Gedachtestreepjes zijn helemaal verdwenen, en de dubbele punt heeft hun rol overgenomen. De cijfers
laten zien wat de drempels hebben gedaan: de schrijvers zijn niet tot de grens gegaan maar eroverheen
gesprongen.

## 1. Top-10 taalpatronen, gerangschikt op frequentie maal hinder

### 1. De dubbele punt als universeel bindmiddel (55–71 per college)

Het verbod op gedachtestreepjes (dash = 0 in alle vier) heeft de dubbele punt overbelast. Die
verbindt nu oorzaak, gevolg, uitleg, voorbeeld en tegenstelling. De lezer moet bij elke dubbele punt
zelf raden welk verband er bedoeld is.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| W:38 | De data verwerpen dat antwoord in die vorm: niet de verwachte dividenden maar de discontovoet beweegt. | De data verwerpen dat antwoord in die vorm, want niet de verwachte dividenden bewegen, maar de discontovoet. |
| W:232 | Dat is een wissel ten opzichte van [](#01-02-bachelier), waar kleine letters logs waren: de som van Williams telt bedragen op, geen logs. | In [](#01-02-bachelier) stonden kleine letters voor logs. Hier niet, omdat de som van Williams bedragen optelt en geen logs. |
| W:1050 | De eindwaarde daalt 17,5%, van 21,00 naar 17,33: één procentpunt minder groei maakt $r - g$ een vijfde groter | De eindwaarde daalt 17,5%, van 21,00 naar 17,33, omdat één procentpunt minder groei $r - g$ een vijfde groter maakt |
| E:100 | Dat is de standaardfout van 2% uit [](#00-01-rendementen): over negentig jaar ligt een gemiddeld rendement maar op twee procentpunt na vast. | Hier keert de standaardfout van 2% uit [](#00-01-rendementen) terug. Na negentig jaar ligt een gemiddeld rendement maar op twee procentpunt na vast. |

**Automatisch: ja, als dichtheid.** Regex `:\s+[a-z]` per alinea, gedeeld door het aantal woorden.
Treffers: 263 (W 71, C 66, E 55, R 71). Vals: 32 zijn sjabloonlabels ("In woorden:", "Wat dit
leert:", "Het bewijsidee:"), die als label mogen blijven maar de dichtheid wel opdrijven. Van de rest
is naar schatting de helft verdedigbaar (een steekproef van tien per college gelezen: 5, 4, 6 en 5
waren in orde). De check meet dus een dichtheid en geen fouten. Drempelvoorstel: hoogstens 8 per
1000 woorden, met de labels niet meegeteld.

### 2. Staccato: te korte zinnen en alinea's van één zin (9–12% van de zinnen ≤ 6 woorden, 16–22% van de alinea's één zin)

Door de gemiddelde zinslengte onder 17 te houden en de alinea's onder 45 woorden, knippen
schrijvers bijzinnen los. De losse zin begint dan vaak met "En" of "Maar" (13 treffers), of komt als
eigen alinea achter de vorige.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| R:828 | Dat verschil scheidt twee effecten niet. Kleine aandelen deden het beter. En bij kleine aandelen springt de slotkoers heen en weer tussen bied- en laatkoers | Achter dat verschil zitten twee effecten die we niet kunnen scheiden. Kleine aandelen deden het beter, en bij kleine aandelen springt de slotkoers heen en weer tussen bied- en laatkoers |
| W:353 | Williams liet de bel weg door hem niet te noemen. Dat is verdedigbaar: bij elke $B_0 > 0$ hoort een andere prijs […]. Maar het blijft een keuze. | Williams liet de bel weg door hem niet te noemen. Dat is verdedigbaar, want zonder de voorwaarde legt het model de prijs niet vast. Toch blijft het een keuze. |
| E:58 | Mehra en Prescott schreven het paper in 1979 en publiceerden het in 1985. Het schat niets. Het kalibreert een Lucas-economie op de Amerikaanse consumptie […] | Mehra en Prescott schreven het artikel in 1979 en publiceerden het in 1985. Het schat niets, maar kalibreert een Lucas-economie op de Amerikaanse consumptie […] |
| C:1093 | Het maakte van de markt de natuurlijke maatstaf, en van het indexfonds de natuurlijke belegging. En bèta verklaart veel van de schommelingen: […] | Het maakte van de markt de natuurlijke maatstaf en van het indexfonds de natuurlijke belegging. Bovendien verklaart bèta veel van de schommelingen […] |

**Automatisch: deels.** Drie maten werken: (a) het aandeel zinnen van zes woorden of minder,
(b) het aantal alinea's van één zin, en (c) `(?:^|[.!?]\s+)(En|Maar) ` als zinsopening.
Maat (c) gaf 13 treffers (W 2, C 5, E 1, R 5), waarvan 3 vals (vraagzinnen in oefeningen en de
retorische "En hoe hard schommelt de wind?"). Een lijst van zinnen van hoogstens vijf woorden is als
foutlijst onbruikbaar: van de 125 treffers is meer dan de helft vals. Dat komt door zinnen die een
display-vergelijking in stukken knipt ("Na X stappen staat er"), door lijstnummers en door
"In deze lecture:". Die knip zit ook in `stats_for`: de zinslengte wordt daardoor te laag gemeten,
wat de druk naar staccato niet verklaart maar wel verbergt.

### 3. Sjablonen die elke alinea dezelfde vorm geven (≈ 19 per college, plus 19 celaankondigingen)

STYLE §11.6 tot en met §11.8 schrijven vaste formules voor: "In woorden:" (W 7, C 8, E 6, R 9),
"*Waarom zou dit waar zijn?*" (5 à 6), "Wat dit leert:", "Het bewijsidee:", "Zoals de intuïtie
voorspelde", "De twee kolommen zijn gelijk", en per codecel een aankondiging. Elke formule apart is
correct Nederlands, maar in deze dichtheid leest de tekst als een formulier.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| W:150, C:166, R:168 | De codecel rekent dezelfde stappen na en zet de handberekening ernaast. / De code rekent hetzelfde na en zet de handgetallen ernaast. / De codecel rekent dezelfde getallen na en zet ze naast de handberekening. | Afwisselen, of de cel zonder aankondiging laten volgen op de laatste stap: "Ter controle doet de code hetzelfde." |
| E:192 | De twee kolommen zijn gelijk. De lezer weet nu waar de kleine premie vandaan komt. | Hand en code komen overeen. De kleine premie komt dus voort uit twee kleine getallen: […] |
| R:189 | Wat de lezer nu weet: het meetkundig gemiddelde ligt ongeveer een halve variantie onder het rekenkundige. | Het meetkundig gemiddelde ligt dus ongeveer een halve variantie onder het rekenkundige. |
| W:216 | In woorden: het rendement is wat de koper morgen terugkrijgt, dividend plus verkoopprijs, gedeeld door wat hij vandaag betaalde. | Het rendement is dus wat de koper morgen terugkrijgt, dividend plus verkoopprijs, gedeeld door wat hij vandaag betaalde. |

**Automatisch: ja, als telling.** De lijst is letterlijk: `In woorden:|Waarom zou dit waar zijn\?|Wat
dit leert:|[Zz]oals de intuïtie voorspelde|Het bewijsidee:|\b[Dd]e lezer\b`. Treffers: 74 (W 17, C 18,
E 19, R 20), vals 0. Celaankondigingen:
`\b[Dd]e (code|codecel|cel|eerste cel|volgende cel|laatste cel)\b[^.]{0,40}\b(rekent|zet|bouwt|laadt|herhaalt|simuleert|volgt|past|legt|trekt|meldt|werkt)\b`
gaf 19 treffers (W 8, C 6, E 1, R 4), vals 0. Of een treffer stoort, hangt af van de dichtheid. Ik
stel daarom plafonds voor en geen verbod.

### 4. "Wie …, …" en "Een belegger die …" als vervanging van je en u (16 en 12 treffers)

Het verbod op je en u, samen met het STYLE-voorbeeld "wie sorteert op bèta", heeft een eigen
tic opgeleverd. Elke "*Waarom zou dit waar zijn?*" begint met "Een belegger die" (H1 vraagt een
handelend onderwerp), en generieke uitspraken beginnen met "Wie". Twee op rij leest als een
spreukenboek.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| W:188 | Wie het toy narekent, weet nu dat de prijs vooral uit de eindwaarde komt | De prijs komt dus vooral uit de eindwaarde |
| R:731 | Wie een $t$-waarde op dagrendementen zonder die kanttekening rapporteert, rapporteert de onzekerheid van iets anders dan hij beweert te meten. | Een $t$-waarde op dagrendementen zonder die kanttekening meet de onzekerheid van iets anders dan het gemiddelde. |
| C:1107 | Wie niet kan lenen, betaalt bewust meer voor hoge bèta, zoals voor elke andere dienst. Wie wel kan lenen, verdient die meerprijs […] | Beleggers die niet kunnen lenen, betalen bewust meer voor hoge bèta, zoals voor elke andere dienst. Beleggers die dat wel kunnen, verdienen die meerprijs […] |
| R:74 | Wie elke seconde meet in plaats van elk uur, krijgt 3600 keer zoveel getallen over dezelfde lucht. | Meet ze elke seconde in plaats van elk uur, dan krijgt ze 3600 keer zoveel getallen over dezelfde lucht. |

**Automatisch: ja.** Regex `(?:^|[.!?]\s+)(Wie)\b` gaf 16 treffers (W 5, C 3, E 1, R 7), waarvan
0 vals. Regex `\b[Ee]en (belegger|onderzoeker|koper|analist) die\b` gaf 12 (W 2, C 3, E 2, R 5), ook
0 vals. Naar mijn oordeel stoort ongeveer de helft. Plafondvoorstel: hoogstens 4 Wie-openers per
college, en nooit twee Wie-zinnen achter elkaar.

### 5. Vertaald Engels dat niet op de calque-lijst staat (10 treffers, en een lek in een bestaande regex)

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| C:617 | De remedie is de reden dat asset pricing nog altijd met portefeuilles werkt. | Daarom werken onderzoekers nog altijd met portefeuilles. |
| W:262 | Dat onderscheid draagt de hele lecture | Om dat onderscheid draait de hele lecture |
| W:991 | Het enige symbool dat Williams als gegeven nam, draagt ruim twee keer zoveel van de beweging als de dividendgroei. | Juist de discontovoet, die Williams als gegeven nam, verklaart ruim twee keer zoveel van de beweging als de dividendgroei. |
| C:1118 | Dat een CAPM-toets eigenlijk de gekozen index toetst, werd het punt van [](#03-14-roll). | Dat een CAPM-toets eigenlijk de gekozen index toetst, liet Roll zien, in [](#03-14-roll). |
| R:87 | Een verlies van 20% en een winst van 25% heffen elkaar op in niveaus | Een verlies van 20% en een winst van 25% heffen elkaar in euro's op |
| E:475 | Een belegger die lang gaat in aandelen en kort in de obligatie, betaalt vandaag niets. | Een belegger die aandelen koopt met geld dat hij tegen de obligatierente leent, betaalt vandaag niets. |
| W:612 | Voor het hoofdargument doet dat ertoe. | Dat is van belang voor het hoofdargument. |
| W:908 | Zo komt het uit: de helling is negatief […] | Dat klopt: de helling is negatief […] |

Het lek zit in de bestaande CALQUES-regex `\b(Dit|Dat) is de reden dat\b`. Die mist C:617, omdat
daar "De remedie" het onderwerp is.

**Automatisch: ja, als uitgebreide lijst.**
`\bis de reden dat|\bhet punt van\b|\bdoet ertoe\b|\bdraagt (de hele|ruim|het)\b|\bin niveaus\b|Zo komt het uit|\bRij maal kolom\b|\blang gaat? in\b`
gaf 10 treffers (W 4, C 3, R 3), waarvan 1 vals: R:809 "van de orde van" is gewoon Nederlands en gaat
daarom uit de lijst. R:455 en R:525 ("Zo lost de theorie de … voorspelling uit de intuïtie in") zijn
geen calque maar projectjargon uit H12 ("inlossen") dat in de lopende tekst is gelekt. Die horen op
de jargonlijst: `\blost\b[^.]{0,60}\bin\b[.:]`.

### 6. Engelse vakwoorden waar een gangbaar Nederlands woord bestaat (29 treffers), met wisselende namen tussen colleges

R gebruikt "value-weighted" (8) en "equal-weighted" (5), terwijl C "waardegewogen" en "gelijkgewogen"
schrijft. Verder komen voor: "size" (6; "op size gesorteerd"), "paper" (2), "short" (2),
"pre-ranking" (2), "finance", "asset pricing", en "het toy" als zelfstandig naamwoord.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| R:756 | Die is dus de replicatie, de maandelijks herbalanceerde equal-weighted reeks de controle. | De waardegewogen markt is dus de replicatie, en de maandelijks geherbalanceerde gelijkgewogen reeks dient als controle. |
| E:58 | Mehra en Prescott schreven het paper in 1979 | Mehra en Prescott schreven het artikel in 1979 |
| R:373 | In de finance knelt dat | In de financiële economie knelt dat |
| C:1248 | afhankelijk van de vraag of de basisactiva op size zijn gesorteerd | afhankelijk van de vraag of de basisactiva op grootte zijn gesorteerd |

**Automatisch: ja, als woordenlijst met voorkeursvorm.**
`\b(finance|asset pricing|paper|short|size|value-weighted|equal-weighted|pre-ranking|toy)\b(?!-voorbeeld)`
gaf 29 treffers (W 2, C 9, E 3, R 15), waarvan 4 vals: "short-restricties" (C:228) en "size/BM" als
naam van een Frenchreeks (C:862, E:792, C:931) zijn gangbaar. Een uitzondering voor `size/BM` en
`short-` maakt de lijst schoon. Deze lijst hoort bij STYLE §3 (vaste termen), zodat ze ook tussen
colleges één naam afdwingt.

### 7. Telegramzinnen zonder persoonsvorm (8 via de regex, minstens 6 daarbuiten)

STYLE §11.1 verbiedt telegramstijl, maar prose_stats controleert het niet.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| C:960 | Nu de cross-sectie en GRS. | Dan volgen de cross-sectie en de GRS-toets. |
| E:912 | Eerst de data en de Sharpe-ratio van de markt. | Eerst laden we de data en berekenen we de Sharpe-ratio van de markt. |
| R:1130 | Dan het verschil tussen de eerste en de laatste periode. | Dan toetsen we het verschil tussen de eerste en de laatste periode. |
| W:976 | **Wat het model verklaart.** Veel. | **Wat het model verklaart.** Het model verklaart veel. |
| E:1076 | **Waar het breekt.** Op getallen die we zelf hebben nagerekend. | **Waar het breekt.** Het model breekt op getallen die we zelf hebben nagerekend. |

**Automatisch: ja voor de opener-vorm, nee voor de rest.**
`(?:^|[.!?]\s+)((?:Eerst|Dan|Daarna|Nu|Ten slotte|Tot slot) (?:de|het|een|twee|drie)\b[^.!?:]{0,70}[.])`
gaf 8 treffers (W 1, C 3, E 2, R 2), waarvan 0 vals. De regex mist de antwoorden op het eigen
vetgedrukte kopje ("Veel.", "Kwalitatief alles wat het moest verklaren.", "Op getallen die …",
"Niet in de boekhoudkundige identiteit maar …", "Beide, voor een andere vraag."). Die zijn te vangen
met een tweede regel: `\*\*[^*]+\.\*\*\s+[A-Z][^.]{0,60}\.` op een alinea-opening, waarna een mens
kijkt of er een persoonsvorm in staat. Zonder woordsoortherkenning is "zin zonder persoonsvorm"
niet betrouwbaar te meten.

### 8. "Dat is / Dit is / Dat zijn" als zinsopening (21 treffers)

H8 laat verwijzen naar de vorige zin toe, maar de vorm "Dat is X" is vaak een Engelse
identiteitszin ("That is the …"). Er staat dan een koppelwerkwoord waar een inhoudswerkwoord hoort.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| W:145 | Dat is exact, want $1{,}331 \times 21 = 27{,}951$. | Die deling gaat precies op, want $1{,}331 \times 21 = 27{,}951$. |
| E:680 | De historische premie heeft een standaardfout van 1,76 procentpunt. Dat is de standaardfout van 2% uit [](#00-01-rendementen). | De historische premie heeft een standaardfout van 1,76 procentpunt, in de orde van de standaardfout van 2% uit [](#00-01-rendementen). |
| R:95 | Dat is een kalibratie, geen meting: | Die 6% is een kalibratie, geen meting. |
| C:430 | Dat is het speciale geval waarin iedereen tegen $R^{f}$ kan lenen. | Die uitkomst hoort bij het speciale geval waarin iedereen tegen $R^{f}$ kan lenen. |

**Automatisch: ja.** `(?:^|[.!?]\s+)((?:Dat|Dit) (?:is|zijn|was|geldt|betekent)\b)` gaf 21 treffers
(W 8, C 4, E 5, R 4), waarvan 0 vals. Ongeveer de helft is in orde. Plafondvoorstel: hoogstens 5 per
college, en de schrijver vervangt de rest door het ding zelf, zoals H8 al vraagt.

### 9. "exact" als verplichte vervanger van "precies" (18 treffers)

"Precies" staat op de stopwoordenlijst (stopw 0–1 per college). Schrijvers gebruiken daarom
"exact", ook waar het Nederlands "precies" of "net zo goed" zegt.

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| C:164 | C heeft de laagste Sharpe-ratio (0,20 tegen 0,40), maar ligt even exact op de lijn. | C heeft de laagste Sharpe-ratio (0,20 tegen 0,40), maar ligt net zo goed precies op de lijn. |
| C:196 | de verwachte rendementen die de markt doen ruimen liggen exact op een lijn in bèta. | de verwachte rendementen waarbij de markt ruimt, liggen precies op één rechte lijn in bèta. |
| W:145 | Dat is exact | Die deling gaat precies op |

**Automatisch: ja.** `\bexact\b` gaf 18 treffers (W 3, C 8, E 3, R 4), waarvan ongeveer 9 vals: in
de wiskundige betekenis ("exact 1,99", "geldt exact") is het woord goed. De oplossing is geen nieuwe
check. De bestaande drempel moet anders, zie §3.

### 10. Motiefnamen als los ingeschoven naamwoordgroep (4 van de 4 zijn stroef)

| vindplaats | zoals het staat | natuurlijker |
|---|---|---|
| C:58 | In de vraag theorie of feit die de reeks doorloopt, is het CAPM zuiver theorie | Bij de vraag die de hele reeks terugkomt, theorie of feit?, is het CAPM zuiver theorie |
| R:63 | Door de reeks loopt de vraag theorie of feit: is een model een theorie die getoetst wordt, of een feit dat op een verklaring wacht? | Door de reeks loopt de vraag "theorie of feit?": is een model een theorie die getoetst wordt, of een feit dat op een verklaring wacht? |
| W:1003 | Bij theorie of feit vraagt de reeks steeds: | Bij de vraag "theorie of feit?" gaat het steeds om het volgende: |
| E:66 | Voor *theorie of feit* is dit het kantelpunt. | Voor de vraag "theorie of feit?" is dit het kantelpunt. |

**Automatisch: ja, als vindlijst.** `((?:\b\w+\s+){0,2}\*?(?:theorie of feit|risico of vergissing)\*?)`
gaf 4 treffers in de lopende tekst (de vetgedrukte kopjes "**Risico of vergissing?**" niet
meegeteld), waarvan 0 vals. STYLE §11.3 wil de letterlijke naam, maar zegt niet hoe die in een zin
past. Met aanhalingstekens en een vraagteken ("de vraag 'theorie of feit?'") loopt de zin wel.

### Getest en afgewezen als check

| patroon | regex | treffers | vals | oordeel |
|---|---|---|---|---|
| van-ketens (drie keer "van") | `\bvan\b(?:\s+\S+){1,3}\s+van\b(?:\s+\S+){1,3}\s+van\b` | 4 | 2 ("van 6% loopt het van 2% tot 10%: van") | te zeldzaam; de colleges hebben hier geen probleem |
| passief met wordt/werd | `\b(wordt\|worden\|werd\|werden)\b(?:\s+[^\s.]+){0,5}?\s+ge\w+(d\|t\|en)\b` | 13 | ongeveer 10 zijn gewoon Nederlands | alleen W:50 en W:537 ("gevolgd worden door") storen; geen check |
| naamwoordstijl (-ing/-heid/-atie + van) | `\b\w{3,}(ing\|heid\|atie)\s+van\s+(de\|het\|een)\b` | 18 | ongeveer 16 ("verdeling van de", "autocorrelatie van de") | ruis |
| herhaalde zinsopener | eerste woord van opeenvolgende zinnen | 16–31 paren per college | bijna alle | "De" opent 16–20% van de zinnen, normaal voor Nederlands |
| zinnen ≤ 5 woorden als foutlijst | lengte na splitsen | 125 | meer dan de helft (knip door display-math, lijstnummers) | alleen bruikbaar als percentage, zie patroon 2 |

**Niet automatisch te vangen** (alleen met een lezer): scheve woordvolgorde ("Zo getoetst en
verworpen werd het pas decennia later", W:1006), elliptische zinnen ("Beide beleggers houden dus de
markt en verschillen alleen in hoeveel", C:195), vage werkwoorden ("Het restant staat tegen $R^f$",
C:243) en beeldspraak die net niet klopt ("de puzzel hangt aan één getal", E:99). Die vragen een
leesronde door iemand met Nederlands als moedertaal, met de opdracht "hardop lezen".

## 2. Overzicht: automatisch te vangen

| # | patroon | automatisch | treffers (W/C/E/R) | vals |
|---|---|---|---|---|
| 1 | dubbele punt midden in een zin | ja, als dichtheid | 263 (71/66/55/71) | 32 labels; van de rest ~50% verdedigbaar |
| 2 | staccato | deels (percentages) | En/Maar-opening 13 | 3 |
| 3 | sjablonen | ja | 74 + 19 celaankondigingen | 0 |
| 4 | Wie- en "een belegger die"-constructies | ja | 16 + 12 | 0 (stoort in ~50%) |
| 5 | calques buiten de lijst | ja (lijst uitbreiden) | 10 | 1 |
| 6 | Engelse vakwoorden | ja (woordenlijst) | 29 | 4 |
| 7 | telegramzinnen | deels | 8 | 0 (mist ≥ 6) |
| 8 | "Dat is"-openers | ja (plafond) | 21 | 0 (stoort in ~50%) |
| 9 | "exact" | ja, maar de oplossing zit in de drempel | 18 | ~9 |
| 10 | motiefnamen | ja (vindlijst) | 4 | 0 |

## 3. Drempels in prose_stats.py die schade doen

1. **`sent_mean: 17`, samen met `sent_p90: 28`.** Gemeten 14,3–15,2, met 9–12% zinnen van zes woorden
   of minder. De schrijvers mikken ver onder de grens, en het resultaat is staccato (patroon 2) en
   losgeknipte "En/Maar"-zinnen. Nederlandse academische prose loopt goed bij gemiddeld 16–20
   woorden. **Voorstel:** `sent_mean` hoogstens 20, `sent_p90` hoogstens 30 en `sent_gt40` op 2
   laten. Daarnaast een ondergrens als waarschuwing: hoogstens 8% zinnen van zes woorden of minder.
   Eerst wel de splitsing repareren, zodat een zin die door een display-vergelijking loopt niet als
   twee korte zinnen telt.
2. **`dash: 10` zonder colon-maat.** De gedachtestreepjes staan op 0. De dubbele punt heeft hun rol
   overgenomen (10–14 per 1000 woorden), en daarmee is de onduidelijkheid alleen verplaatst.
   **Voorstel:** een nieuwe metriek `colon_mid`, een dubbele punt gevolgd door een kleine letter,
   zonder de sjabloonlabels, met als maximum 8 per 1000 woorden.
3. **`para_mean: 45`.** Gemeten 42–45, precies tegen de grens, met 16–22% alinea's van één zin.
   STYLE §11.1 vraagt drie tot zes zinnen per alinea, en de huidige drempel werkt die regel tegen.
   **Voorstel:** `para_mean` hoogstens 60, plus een nieuwe `para_one` (alinea's van één zin buiten
   admonitions en lijsten) met als maximum 10% van de alinea's.
4. **`stopw` telt "precies".** Het resultaat is "exact" in niet-wiskundige zinnen (patroon 9).
   **Voorstel:** "precies" van de lijst halen en de rest (ruwweg, inderdaad, in feite, letterlijk)
   op 6 houden. Of "precies" en "exact" samen tellen, met een maximum van 8.
5. **`u_form`/`je_form: 0` zonder tegenwicht.** Het verbod zelf werkt, maar het STYLE-voorbeeld
   "wie sorteert op bèta" is een tic geworden (patroon 4). **Voorstel:** een nieuwe `wie_open` met
   een maximum van 4, en STYLE §11.2 een tweede voorbeeld geven met een concreet onderwerp
   ("beleggers", "de onderzoeker", "we").
6. **CALQUES werkt met letterlijke vormen.** `(Dit|Dat) is de reden dat` mist "De remedie is de reden
   dat" (C:617). **Voorstel:** de regex verruimen tot `\bis de reden dat\b` en de lijst van patroon 5
   toevoegen.
7. **STYLE-regels die de tool niet controleert.** Het gaat om "hoogstens drie getallen per alinea"
   (alinea's met meer dan drie getallen: W 9, C 19, E 23, R 19; veel daarvan in replicatie en
   oefeningen, dus eerst uitzoeken hoeveel vals zijn), "per alinea hoogstens één dus" (0–1
   overtredingen, dus geen probleem) en telegramstijl (patroon 7). **Voorstel:** alleen
   `telegram` als harde check toevoegen. Getallen per alinea eerst als rapportage, zonder drempel.

## 4. Aanbevelingen

**prose_stats.py**

- Zet de drempels om: `sent_mean` 17 → 20, `sent_p90` 28 → 30, `para_mean` 45 → 60, en haal
  "precies" uit `stopw`.
- Voeg `colon_mid` toe (maximum 8 per 1000 woorden, sjabloonlabels niet meegeteld), plus `para_one`
  (maximum 10%) en `short6` (zinnen van zes woorden of minder, maximum 8%, alleen als waarschuwing).
- Voeg `wie_open` (maximum 4), `dat_is_open` (maximum 5) en `template` toe. Voor `template` geldt:
  "In woorden:" hoogstens 4, en "de lezer" 0.
- Voeg `telegram` toe (maximum 0), met de regex van patroon 7.
- Breid CALQUES uit met de lijst van patroon 5. Voeg de jargonvorm "lost … in" toe, en verruim
  "(Dit|Dat) is de reden dat" tot "is de reden dat".
- Voeg een lijst `ANGLICISMS` toe met voorkeursvorm (value-weighted → waardegewogen,
  equal-weighted → gelijkgewogen, size → grootte, paper → artikel, finance → financiële economie,
  toy → toy-voorbeeld), en laat `--where` die met regelnummer tonen.
- Repareer de zinssplitsing: een zin die over een display-vergelijking heen loopt, telt als één zin.

**STYLE.md**

- §11.1: vervang "Richtlengte 12 tot 20" door "gemiddeld 16 tot 20; wissel af, en knip geen bijzin
  los om het gemiddelde te halen". Voeg toe: "De dubbele punt is geen vervanging voor het
  gedachtestreepje. Gebruik 'want', 'omdat' of 'dus' als het verband zo heet."
- §11.2: zet naast "wie sorteert op bèta" een voorbeeld met een concreet onderwerp, en schrijf erbij
  dat "Wie …, …" hoogstens vier keer per college voorkomt. Haal "precies" uit de stopwoorden.
- §11.3: schrijf een motiefnaam in de lopende tekst als vraag tussen aanhalingstekens ("de vraag
  'theorie of feit?'").
- §11.4: neem de calques van patroon 5 en de anglicismen van patroon 6 op in de tabel.
- §11.6 en §11.8: "In woorden:" en de celaankondiging zijn richtlijnen en geen formules. Varieer ze,
  of laat ze weg als de vorige zin het al zegt. Schrap "Wat de lezer nu weet:" als vaste formule.

**Schrijversprompt**

- Voeg één opdracht toe: "Lees elke alinea na het schrijven hardop. Voeg een losgeknipte zin die met
  En, Maar of Dat is begint weer samen met de vorige zin, en vervang een dubbele punt door het
  voegwoord dat het verband noemt."
- Laat de schrijver `prose_stats --where` draaien op de nieuwe lijsten, en elke treffer boven het
  plafond herschrijven of in het rapport verantwoorden. Een drempel onderschrijden is geen doel.
