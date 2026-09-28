# Onderzoek E: de lezer, taal en consistentie

Gelezen als Nederlandstalige PhD-student die het boek voor het eerst leest, in deze volgorde:
`01_04_markowitz`, `02_09_black_scholes`, `03_10_merton_icapm`, `03_14_roll` (alleen .md).
Regelnummers verwijzen naar de .md-bestanden in `lectures/`. Afkortingen: MW = 01_04_markowitz,
BS = 02_09_black_scholes, ME = 03_10_merton_icapm, RO = 03_14_roll.

Algemene indruk: de wiskunde en de getallen lezen goed, en veel zinnen zijn helder. Dat ik stok,
komt zelden door lange zinnen. Het komt door drie dingen: Engels dat woord voor woord vertaald is
(maar niet op de calque-lijst staat), zinnen die er alleen staan omdat een regel ze eist, en eigennamen of
voornaamwoorden die als onderwerp iets doen wat ze in het Nederlands niet kunnen. Roll leest het
soepelst, Black-Scholes het stroefst.

---

## 1. Top-10 taalpatronen

Gerangschikt op frequentie maal hinder. Per voorbeeld: vindplaats, de zin zoals hij staat, en een
herschrijving met dezelfde inhoud en ongeveer dezelfde lengte.

### 1. Nieuwe calques die niet op de lijst van STYLE §11.4 staan (±30 plekken)

De bekende calques zijn weg, maar er zijn nieuwe voor in de plaats gekomen. Dit is de grootste bron
van "zo zeg je dat niet".

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| BS:324 | "Geen arbitrage eist dat het de rente verdient" | "Omdat arbitrage niet mag bestaan, moet het de rente verdienen" |
| BS:607 | "We prijzen een *at-the-money* call en put" | "We berekenen de prijs van een *at-the-money* call en put" |
| BS:29 | "Kan een optie geprijsd worden zonder te weten ..." | "Is de prijs van een optie te bepalen zonder te weten ..." |
| BS:345 | "Leggen we het CAPM op elk moment van het leven van de optie op" | "Laten we het CAPM gedurende de hele looptijd van de optie gelden" |
| BS:248 | "Dat is Bacheliers proces met de reparatie van Osborne en Samuelson" | "Dat is Bacheliers proces, met de correctie van Osborne en Samuelson" |
| BS:1050 | "We nemen 42 vertragingen" | "We nemen 42 lags" |
| MW:290 | "De factor ½ houdt de afgeleide schoon." | "De factor ½ maakt de afgeleide eenvoudiger." |
| MW:321 | "op dat feit draait de tweede helft van deze lecture" | "om dat feit draait de tweede helft van dit hoofdstuk" |
| ME:505 | "... [](#eq-merton-icapm-vraag) kiezen en de markt ruimt" | "... kiezen en vraag en aanbod op de markt gelijk zijn" |
| ME:518 | "marktruiming zegt dat de som van alle vragen de markt is" | "in evenwicht is de som van alle vragen gelijk aan de markt" |
| ME:568 | "dat variabelen die de beleggingskansen voorspellen beprijsde factoren leveren" | "dat variabelen die de beleggingskansen voorspellen factoren met een risicopremie opleveren" |
| ME:848 | "Bij γ = 2 bindt de grens van 0,99." | "Bij γ = 2 is de grens van 0,99 bindend." |
| ME:282 | "Het bewijsidee is het recept van het toy-voorbeeld. Werk achterwaarts." | "Het bewijs volgt het recept van het toy-voorbeeld: reken terug vanaf de laatste periode." |
| ME:369 | "Het bewijs gaat na dat die gok de HJB-vergelijking oplost." (drie regels na "procentuele gok" in de betekenis *weddenschap*) | "Het bewijs gaat na dat deze proefoplossing de HJB-vergelijking oplost." |
| ME:957 | "Het teken is dus goed te leren, de grootte niet." | "Het teken is dus goed te schatten, de grootte niet." |
| ME:1286 | "De hedgevraag hangt aan de helling van het rendement op een voorspeller" | "De hedgevraag hangt af van de helling van het rendement op een voorspeller" |
| RO:385 | "In een CAPM-wereld hangt elke premie aan de covariantie met de markt" | "In een CAPM-wereld hangt elke premie af van de covariantie met de markt" |
| RO:88 | "Verwerpt hij, dan weet hij niet of ..." | "Verwerpt hij het model, dan weet hij niet of ..." |
| ME:26 | "De barst die openblijft, is de ene periode van het CAPM." | "De zwakke plek is dat het CAPM maar één periode kent." |
| ME:108 | "... heeft twee perioden: er is dan één morgen om zich tegen in te dekken." | "... heeft twee perioden: er is dan één toekomstige periode om zich tegen in te dekken." ("één morgen" leest als *één ochtend*) |

### 2. Regeltaal die in de tekst lekt (±20 plekken)

Zinnen die een STYLE-regel bijna letterlijk nazeggen. Voor de lezer zijn het rare zinnen, omdat
ze verwijzen naar een structuur die hij niet kent ("het blok", "de steekproefvraag").

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| MW:776 | "De vraag over steekproeven: hoeveel daarvan levert een belegger die ..." | "Hoeveel daarvan haalt een belegger die ..." |
| RO:659 | "De vraag over steekproeven: kan hij met vijftig jaar data zien of ..." | "Kan hij met vijftig jaar data zien of ..." |
| RO:786 | "Het antwoord op de steekproefvraag is dus nee." | "De onderzoeker kan het dus niet zien." |
| BS:101 | "We beginnen met de imports-cel, de enige van deze lecture." | "De eerste cel laadt de pakketten voor het hele hoofdstuk." |
| ME:109 | idem, letterlijk | idem |
| RO:111 | "De imports-cel staat hier." | weglaten, of dezelfde zin als bij MW:115 |
| BS:206 | "De lezer weet nu het argument van de lecture in het klein:" | "Daarmee staat het hele argument al in het klein:" |
| BS:398 | "Daarbij werkt aanname 1, een constante σ." | "Daarvoor is aanname 1 nodig: σ is constant." |
| BS:439 | "De formule is in beide richtingen te lezen." (daarna alleen "stijgt") | "De formule laat zien hoe de prijs op elke invoer reageert." |
| RO:59 | "Dat werk definieert het tijdvak omdat het de status van het CAPM verandert." | "Met dit werk begint een nieuwe fase, omdat het de status van het CAPM veranderde." |
| ME:58 | "Dat werk definieert het tijdvak, omdat het de asset pricing dynamisch maakte." | "Met dit werk begint een nieuwe fase: asset pricing werd dynamisch." |
| ME:1058 | "Alle tekens en ordes van grootte kloppen, zoals de verwachte afwijking eiste." | "Alle tekens en ordes van grootte kloppen, zoals we vooraf verwachtten." |
| RO:1084 | "... en het intercept nul, zoals de verwachte afwijking eiste." | "... en het intercept nul, zoals verwacht." |
| RO:1088 | "Dat was de onzekerheid die het blok noemde." | "Die onzekerheid hadden we vooraf al genoemd." |
| ME:143 | "(Theorie leidt die vorm af)" | "(de theorie hieronder leidt die vorm af)" |

### 3. De motiefnamen als eigennaam of als handelend onderwerp (9 plekken)

Wie het boek voor het eerst leest, weet niet dat "de standaardfout van 2%" een eigennaam is. Letterlijk
genomen zijn deze zinnen onzin, dus de lezer stokt en leest terug.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| RO:746 | "Volgens de standaardfout van 2% is dat slecht gemeten:" | "Zo'n gemiddelde is slecht gemeten, zoals elk gemiddeld rendement:" |
| RO:630 | "Hier keert de standaardfout van 2% om." | "Hier ligt het andersom dan bij gemiddelde rendementen." |
| ME:1267 | "Het verschil is zelf de standaardfout van 2%." | "Het verschil komt zelf voort uit de onnauwkeurigheid van gemiddelde rendementen." |
| ME:993 | "Dit is de standaardfout van 2% in dynamische vorm." | "Dit is hetzelfde meetprobleem als bij het gemiddelde rendement, nu over de tijd." |
| MW:69 | "Op de vraag theorie of feit (is dit een theorie die getoetst wordt, of een feit dat op een verklaring wacht?) is het antwoord: een *theorie van keuze* ..." | "Markowitz levert een theorie van keuze, geen uitspraak over prijzen die je kunt toetsen." |
| BS:66 | "Op de vraag theorie of feit is Black-Scholes een theorie die getoetst wordt, maar een relatieve." | "Black-Scholes is een toetsbare theorie, maar een relatieve." |
| ME:63 | "Op de vraag theorie of feit is het ICAPM een theorie met een open plek." | "Het ICAPM is een theorie met een open plek." |
| RO:60 | "In de termen van theorie of feit: het CAPM was een theorie met toetsen en werd ..." | "Het CAPM was een getoetste theorie en werd ..." |
| RO:1107 | "In de termen van theorie of feit is het CAPM geen getoetste theorie meer" | "Het CAPM is daarmee geen getoetste theorie meer" |

### 4. De verplichte terugkoppeling naar de intuïtie als vaste formule (±14 plekken)

"Zoals de intuïtie voorspelde" en varianten staan tien keer in vier colleges, plus een vaste
slotzin in elke intuïtiesectie. Eén keer per college helpt; vier keer wordt een tic, en "de
intuïtie verwachtte" maakt van een sectie een persoon.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| MW:527 | "Zo lost de theorie de tweede voorspelling van de intuïtie in." | "Ook de tweede voorspelling van het begin klopt dus." |
| ME:286 | "Dat is de eerste voorspelling van de intuïtie." | "Zo komt de eerste voorspelling uit." |
| ME:753 | "Dat de getrokken lijn stijgt, is de tweede voorspelling van de intuïtie." | "De getrokken lijn stijgt, zoals we aan het begin voorspelden." |
| RO:620 | "Zoals de intuïtie verwachtte, is het meeste dus niet systematisch" | "Zoals verwacht is het meeste dus niet systematisch" |
| RO:336 | "Dat is de eerste voorspelling van de intuïtie: ook in de data ligt de lijn exact." | "Ook in de data ligt de lijn dus exact." |
| ME:100 / RO:103 | "We verwachten dus drie dingen." (identiek in twee colleges) | variëren, of de drie verwachtingen direct als lijst geven |

### 5. Dubbelepuntopeners en telegramstijl (±40 plekken)

"In woorden:" staat 23 keer (MW 10, BS 8, RO 5), "De bewering:" vier keer in MW en "Het
bewijsidee:" zeven keer. Samen met korte telegramzinnen geeft dat een opsommerig ritme.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| MW:268 | "De bewering: elke belegger die aanname 1 volgt, kiest een portefeuille op één vaste rand, ..." | "We laten zien dat elke belegger die aanname 1 volgt, een portefeuille op één vaste rand kiest, ..." |
| MW:488 | "In woorden: de premie per eenheid risico, onafhankelijk van de schaal van w." | "Dit is de premie per eenheid risico; de schaal van w doet er niet toe." |
| BS:727 | "Nu de eigenlijke vraag." | "Dan nu de vraag waar het om gaat." |
| RO:957 | "Nu de vijftig aandelen." | "Dan de vijftig aandelen." |
| RO:233 | "Ten slotte Rolls tweede vraag: welk deel van de variantie is systematisch?" | "Ten slotte behandelen we Rolls tweede vraag: welk deel van de variantie is systematisch?" |
| BS:159 | "Stap 5: waar p bleef. Nergens." | "Stap 5: de kans p komt nergens voor." |

### 6. Tekstonderdelen en data als handelend onderwerp (±14 plekken)

Dit volgt uit "de zaak zelf als onderwerp" (STYLE §11.2): simulaties vragen, data kiezen, kolommen
overstemmen en een figuur verwerpt.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| BS:1154 | "De data van deze lecture kiezen niet." | "Met deze data is niet te kiezen tussen de twee." |
| ME:1303 | "de data van deze lecture beslissen dat niet" | "met deze data is dat niet te beslissen" |
| RO:744 | "De steekproefkolommen overstemmen dat verschil." | "In de steekproeven valt dat verschil weg in de ruis." |
| RO:911 | "De rechterfiguur verwerpt alleen de efficiëntie van de index" | "Rechts wordt alleen de efficiëntie van de index verworpen" |
| BS:1151 | "Scheiden vraagt de *stochastic discount factor* ... in crashtoestanden" | "Om ze te scheiden, moet je de SDF in crashtoestanden kennen" |
| ME:1302 | "Scheiden vraagt of verwachte rendementen meebewegen met consumptie" | "Om ze te scheiden, moet je weten of verwachte rendementen meebewegen met consumptie" |
| BS:869 | "Zo vraagt het dividend geen aanname." | "Zo hoeven we over het dividend niets aan te nemen." |
| MW:768, BS:647, ME:865, RO:652 | "De simulatie hierna vraagt: ..." | "De simulatie hierna gaat na ..." |

### 7. "Zij/haar/diens" voor zaken, met dubbelzinnigheid (±30 plekken)

Portefeuille, hedgevraag, Brownse beweging, consumptie en tangentportefeuille zijn "zij", proxy is
"hij". In Nederlands-Nederlands leest dat formeel of Vlaams. Staan er twee zaken in één zin, dan weet de
lezer niet meer wie wie is.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| RO:877 | "Zijn correlatie met de tangentportefeuille is ook zijn fractie van haar Sharpe-ratio" | "De correlatie van deze proxy met de tangentportefeuille is ook het deel van de Sharpe-ratio van die portefeuille dat hij haalt" |
| RO:643 | "haar correlatie met de tangentportefeuille maal diens Sharpe-ratio" | "de correlatie met de tangentportefeuille maal de Sharpe-ratio van die tangentportefeuille" ("diens" is voor personen) |
| BS:307 | "Met de schok verdwijnt ook haar verwachting, en dus μ." | "Met de schok verdwijnt ook het verwachte rendement, en dus μ." |
| ME:231 | "Merton liet zien dat zij de portefeuilleregels hieronder niet verandert" | "Merton liet zien dat consumptie de portefeuilleregels hieronder niet verandert" |
| ME:245 | "In [](#02-09-black-scholes) heette zij W_t" | "In [](#02-09-black-scholes) heette die W_t" |
| MW:1074 | "In de steekproef belooft mean-variance meer dan 1/N ..., erbuiten levert zij minder." | "..., erbuiten levert ze minder." of "..., erbuiten minder." |

### 8. Komma-ketens en ingeschoven bijzinnen (±12 plekken)

Dit ontstaat waar gedachtestreepjes en puntkomma's weg moesten: de zin blijft even lang, maar nu met
komma's.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| MW:700 | "Wie ε draagt, draagt dus risico dat hij gratis had kunnen wegdiversifiëren, en geen belegger die kan spreiden, wil hem daarvoor betalen, zoals de intuïtie voorspelde." | "Wie ε draagt, draagt risico dat hij gratis had kunnen wegdiversifiëren. Geen belegger die kan spreiden, betaalt hem daarvoor." |
| BS:1128 | "Uit één argument, dat wat zonder risico is de rente verdient, volgt een formule met ..." | "Het hele model rust op één argument: wat zonder risico is, verdient de rente. Daaruit volgt een formule met ..." |
| RO:28 | "Het bezwaar dat de markt niet waarneembaar is, dat in de APT-discussie terugkwam, begint hier." | "Hier begint het bezwaar dat de markt niet waarneembaar is. Het keert terug in de discussie over de APT." |
| ME:88 | "Het extra deel heet de *hedgevraag* (*hedging demand*: het deel van de portefeuille dat vermogen levert wanneer de beleggingskansen, kortweg de kansen, verslechteren)." | "Het extra deel heet de *hedgevraag* (*hedging demand*). Het levert vermogen op wanneer de beleggingskansen verslechteren; hierna heten die kortweg de kansen." |
| BS:831 | "Een voordeel in volatiliteit is dus meetbaar op een manier waarop een voordeel in gemiddeld rendement dat bijna nooit is." | "Een voordeel in volatiliteit is dus te meten, een voordeel in gemiddeld rendement bijna nooit." |
| MW:648 | "Dat de markt het ook niet doet, vraagt een evenwicht, en dat heeft Markowitz niet." | "Dat de markt er ook niet voor betaalt, volgt pas uit een evenwichtsmodel, en dat heeft Markowitz niet." |

### 9. Beeldspraak en registerwissels die niet landen (±12 plekken)

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| MW:467 (ook MW:619, MW:760, RO:417) | "... houdt iedereen dezelfde risicovolle portefeuille, en alleen de dosis verschilt." | "... houdt iedereen dezelfde risicovolle portefeuille; alleen het bedrag dat erin gaat verschilt." |
| MW:1147 | "Dat verschil is ruis: hier zit hefboom op een schattingsfout" | "Dat verschil is ruis: hier wordt een schattingsfout met hefboom vergroot" |
| BS:255 | "Een Brownse beweging schudt echter zo hard dat ..." | "Een Brownse beweging beweegt echter zo grillig dat ..." |
| RO:595 | "dan beweegt elk aandeel vooral op eigen houtje" | "dan beweegt elk aandeel vooral op zichzelf" |
| MW:101 | "het risicovolle mandje met de beste verhouding tussen premie en risico" | "de risicovolle portefeuille met de beste verhouding tussen premie en risico" |
| RO:92 | "Geeft een index die bijna de markt is dan niet bijna de goede lijn? Nee." | "Geeft een index die bijna de markt is dan niet bijna de goede lijn? Dat blijkt niet zo te zijn." |

### 10. Het productieproces in de tekst (7 plekken)

Zinnen die melden wat de schrijver niet kon openen. Voor de lezer zijn ze onbegrijpelijk: "niet tegen de
bron te houden" is een mengsel van *naast de bron leggen* en *tegen het licht houden*.

| vindplaats | staat er | natuurlijk Nederlands |
|---|---|---|
| BS:656 | "Hun tabellen hebben we niet kunnen raadplegen." | schrappen, of "We volgen de latere, bekendere analyse van Derman en Kamal." |
| BS:721 | "de getallen van Derman en Kamal zijn niet tegen de bron te houden" | "de getallen van Derman en Kamal controleren we hier niet" |
| BS:859 | "de getallen van de bronnen zijn niet tegen de bron te houden" | "de getallen van de bronnen gelden voor een andere periode" |
| BS:1031 | "Hun getallen zijn niet tegen de bron te houden, dus we toetsen teken en vorm." | "We vergelijken geen niveaus, alleen teken en vorm." |
| MW:938-940 | "Hun FF-vierfactordataset heeft 24 reeksen ... Die dataset ligt het dichtst bij onze 25 portefeuilles. Voor de industrieën hebben we hun getallen niet." | "Hun dataset die het meest op onze 25 portefeuilles lijkt, telt 24 reeksen; voor industrieën rapporteren ze geen getallen." |

**Losse taalfouten** (geen patroon, wel storend):
- MW:378 "terwijl aandelen alleen hetzelfde verwachte rendement met 20% risico levert": het werkwoord moet *leveren* zijn.
- MW:1039 en ME:559 "het het": herschrijf tot "doet minimum-variantie het beste" en "vermogen levert als dat het minst nodig is".
- RO:643 "diens" (zie patroon 7).

---

## 2. Vaktermen

| term zoals nu | vindplaats | probleem | voorstel |
|---|---|---|---|
| lecture (17×: "deze lecture") | overal | Engels woord in een Nederlands boek; de eigenaar zegt zelf "college" | "dit hoofdstuk" of "dit college", overal gelijk |
| efficiënte rand, minimum-variantierand | MW:97 e.v., RO:254 | "rand" is geen gangbare term; Nederlandse leerboeken zeggen "efficiënte grens" | "efficiënte grens" (bij de eerste keer *efficient frontier*) |
| excess rendement / overrendement | ME 8×, RO 12×, tegenover MW 6× "overrendement" | H7 tussen colleges; "excess rendement" is half vertaald | kies één: "overrendement" (Nederlands) of "excess return" (Engels laten); tabel in STYLE §3 aanpassen |
| hedgen / afdekken / indekken | BS 64× hedg-, ME 91× hedg- en 7× "indekken", BS:85 "afgedekte" | drie werkwoorden voor één handeling; "omdat ze indekken" (ME:93) is onovergankelijk | "hedgen" (STYLE §3 laat hedge Engels), "zich indekken" alleen wederkerend |
| prijzen, geprijsd (to price) | BS:29, BS:607 | "prijzen" betekent in het Nederlands *loven* | "waarderen", "de prijs bepalen van" |
| beprijsd (risico, factor) | ME:568, 1282, 1298 | calque van *priced* | "met een risicopremie", of *priced* laten staan |
| marktruiming, de markt ruimt | ME:505, 518, 527 | *market clearing* woord voor woord | "evenwicht op de markt", "vraag gelijk aan aanbod" |
| in-sample (12×) tegenover "in de steekproef" | RO 12×; MW gebruikt "in de steekproef" | inconsistent tussen colleges | "in de steekproef" / "buiten de steekproef", overal |
| scalars | RO:135 | Engels | "getallen" (zoals MW:327) |
| critique (titel) | RO:16, tegenover "kritiek" op RO:55 | Engels/Frans in de titel, Nederlands in de tekst | "Roll: de kritiek en de R²" |
| vertragingen (lags) | BS:1050 | niemand zegt dit | "lags" |
| horizons | ME:1010, 1117, 1236 | Engels meervoud | "horizonnen" |
| standaardafwijking | ME:1243, 1272 | H7: overal elders "standaarddeviatie" | "standaarddeviatie" |
| observaties | ME:1471 | elders "waarnemingen" | "waarnemingen" |
| koop-en-houdbelegger | ME:1262 | geforceerd | "buy-and-hold-belegger" |
| Itô's lemma / de regel van Itô | BS:43 e.v., ME:320 | twee namen in twee colleges | "het lemma van Itô" overal |
| stochastic discount factor / SDF / stochastische discontofactor | BS:1152, BS:345, kaart §3 | drie vormen; BS:1152 definieert de term pas in het slot | één vorm voor het hele boek; definitie bij de eerste keer in het college |
| equity premium | BS:1275, 1297, 1304 | elders "premie op aandelen" (RO:26) | "aandelenpremie" |
| ingeprijsde variantie | BS:514, 1020, 1030 | marktjargon dat als calque leest | "implied variantie" of "de variantie die in de prijs zit" |
| attenuatie | RO:748 | onvertaald en niet uitgelegd | "verzwakking door meetfout (*attenuation bias*)" |
| Horizon-irrelevantie | ME:273 | gekunstelde samenstelling met koppelteken | "Irrelevantie van de horizon" |
| kanteling (tilt) | RO:557, 663 e.v. | acceptabel, maar een econoom zegt "tilt" | laten staan, of bij de eerste keer "(*tilt*)" erbij |
| small en value | RO:1284 | Engels zonder uitleg in dit college | bij de eerste keer uitleggen (STYLE §3) |
| mean-variance-portefeuille / mean-variance-efficiënt | MW, RO:37 | prima om Engels te laten, maar wel consequent | laten |
| payoff, proxy, P&L, Greeks, smirk, implied volatility, prior, posterior | BS, RO, ME | goed dat deze Engels blijven | laten |
| euro tegenover dollar | BS:74, 1146 e.v. (euro, bij Black 1989 en de S&P); MW:1108 (dollar) | anachronistisch en inconsistent | dollar bij Amerikaanse data |

---

## 3. Toon en consistentie

**Openingen.** Alle vier volgen hetzelfde sjabloon: vraag, antwoord, "In deze lecture:", lijst,
geschiedenis en motiefzin. Het sjabloon werkt, maar de motiefzin aan het eind van het Overzicht
(MW:69, BS:66, ME:63, RO:60) klinkt telkens aangeplakt. Het is een vraag die niemand stelde, met een
antwoord in de vorm "Op de vraag X is Y een Z". De historische alinea eindigt drie keer met een
variant van "definieert het tijdvak" (ME:58, RO:59, en BS:62 "begint een nieuw tijdvak").

**Slot van de intuïtiesectie.** Vier keer staat er een vaste slotzin: "De intuïtie doet dus twee voorspellingen" (MW:105),
"Dat leidt tot drie verwachtingen" (BS:92, waar "verwachtingen" in dit vak *expectations* betekent),
"We verwachten dus drie dingen" (ME:100, RO:103).

**Slotparagrafen.** "Wat er daarna kwam" eindigt in MW:1189, BS:1158 en ME:1308 met "...: zie
[](#...)". Dat is abrupt: een verwijzing in plaats van een zin. RO:1122-1124 doet het goed met een vraag
die het volgende college beantwoordt. "Waar het breekt. Niet in de wiskunde (maar) in de invoer." staat
bijna letterlijk in MW:1166 en ME:1285. "De data van deze lecture kiezen niet" (BS:1154) en "beslissen
dat niet" (ME:1303) sluiten het blok over risico of vergissing op dezelfde manier af. Bij Roll past het
vaste kopje "**Wat het model verklaart**" (RO:1097) niet, want Roll is geen model maar een kritiek.

**Toonsprongen binnen een college.**
- RO: "Nee." (RO:92) en "op eigen houtje" (RO:595) staan tussen "dan en slechts dan" en "Beschouw voor een proxy".
- BS: "Stap 5: waar p bleef. Nergens." (BS:159) is een grap in een verder zakelijk toy-voorbeeld.
- BS:206 "De lezer weet nu" breekt het "we" van de rest.
- "wij" naast "we": MW:936 "wij ruim twintig jaar later", BS:855, BS:1039, ME:1017, ME:1269, RO:811.
  In het replicatieblok is het contrast bedoeld; buiten dat blok hoort "we".

**Consistentie tussen colleges.**
- Toy-stappen: "Stap 1: de covariantiematrix." (MW, BS, RO) tegenover "Stap 1, myopisch." (ME:147).
- Dezelfde δ uit hetzelfde toy-voorbeeld is −0,0125 (MW:360) en −0,01248 (RO:150).
- ME:469 verwijst naar een oefening met een link (`[](#ex-merton-icapm-1)`), terwijl kaart §3 zegt dat
  oefeningslabels geen linkdoel zijn. Elders staat gewoon "oefening 2" als tekst.
- "Het recept." en "Wat dit leert:" staan in alle vier. Dat is goed voor de herkenbaarheid,
  maar "Wat dit leert:" (11×) is zelf een vertaling van *What this teaches*. Het kwam in de plaats
  van het verboden "Les:".

---

## 4. Oorzaakhypothesen

| patroon | vermoedelijke oorzaak | regel (geciteerd) |
|---|---|---|
| 1 Nieuwe calques | De calque-toets is een vaste lijst. Wat daar niet op staat, komt door `--check` en door de beoordeling. | prose_stats: `"calque": 0,  # vertaald Engels, zie CALQUES`; STYLE §11.4: "De lijst hieronder is niet volledig" (maar alleen de lijst wordt gemeten) |
| 2 Regeltaal lekt | De schrijver past de regel toe door hem uit te spreken. | STYLE §11.7: "één alinea geschiedenis: wie, wanneer, waarom dit werk het tijdvak definieert"; "**Simulatie** beantwoordt één vraag over steekproeven"; "één zin die zegt wat de lezer nu weet"; "**De imports-cel** staat aan het begin van `## Toy-voorbeeld`"; §11.6: "de laatste regel zegt wat de simulatie hierna toetst"; §11.5: "verwijst naar de 'verwachte afwijking'"; H5: "Aannames worden genoemd waar ze werken"; H6: "Elk vergelijkend resultaat wordt in beide richtingen gelezen" |
| 3 Motieven als eigennaam | De namen moeten letterlijk en in elk college staan. | STYLE §11.3: "De drie motieven heten in elke lecture letterlijk zo"; rubriek "Wat niet meetelt" 2: "Dat zijn eigennamen, geen jargon" |
| 4 Terugkoppeling intuïtie | H12 eist dat het er expliciet staat, en de beoordelaar vinkt af of het er staat. | STYLE H12: "De theorie zegt expliciet waar die verwachting wordt bevestigd"; kaart §5: "Controle: wat voorspelde de intuïtie, waar ingelost?" |
| 5 Dubbelepunten, telegram | Elke vergelijking krijgt een leeszin, en de kortste vorm is "In woorden:". De drempels op zinslengte belonen hakken. | STYLE §11.6: "één zin die de vergelijking in woorden leest"; H9: "De eerste zin van elke `###` is de vraag ... of de bewering"; prose_stats `"sent_mean": 17`, `"sent_p90": 28` |
| 6 Zaken als onderwerp | "u" en "je" zijn verboden, dus wordt de zaak het onderwerp, ook bij werkwoorden die een mens vragen. | STYLE §11.2: "Gebruik 'we' ..., de onpersoonlijke vorm ..., of de zaak zelf als onderwerp" |
| 7 zij/haar | Er is geen regel: de schrijver kiest consequent vrouwelijk voor de-woorden, en niemand meet het. | ontbreekt in STYLE en rubriek |
| 8 Komma-ketens | Streepjes en puntkomma's moesten weg, en het woordbudget laat geen extra zin toe. | STYLE §11.1: "Het gedachtestreepje is geen bindmiddel"; prose_stats `"dash": 10`, `"semicol": 15`, `"words": 5500`; workflow §2.4: "Elk *toevoegen* betaal je met schrappen elders" |
| 9 Beeldspraak | Het beeld moet de intuïtie tot een handeling maken (H1), maar de schrijver kiest woorden buiten het register. | STYLE H1: "beschrijft iemand die iets doet ... met een richting" |
| 10 Productieproces | Door de feitencontrole en de zuinigheid van §10 worden bronnen niet geopend, en dat wordt dan in de tekst gemeld. Punten van F23 worden met één extra zin opgelost. | workflow §10.3: "nooit een pdf volledig"; §2.4: "Los van de vijftien lezerspunten minstens de eerste tien op"; §9.2: "Wijs een punt alleen af met een regel uit STYLE" |
| alle | De schrijver leest de eindtekst nooit meer als lezer. Na F1 komen alleen gerichte edits, gebundeld per sectie en gezocht met grep. Taal weegt 15% en wordt afgevinkt op meetbare punten. | workflow §10.2: "Wijzigingen gebundeld: één Python-script of één Write per sectie"; §10.3: "Het college één keer volledig (`.md`), daarna alleen `grep -n` of `sed -n`"; §2.1: "Lees tot slot je eigen lecture één keer met de rubriek ernaast" (met de rubriek, niet als lezer); rubriek criterium 3: gewicht 15% |
| termen | Een deel van de vaste termen is zelf half vertaald, en andere ontbreken. | STYLE §3, notatietabel: "`$R^{e}_{t+1}$` \| excess rendement"; STYLE en workflow gebruiken zelf overal "lecture" |

---

## 5. Aanbevelingen

**STYLE.md**
1. Maak een nieuwe §11.12 "Regels blijven buiten de tekst". Verbied daarin letterlijk "vraag over steekproeven",
   "steekproefvraag", "imports-cel", "de lezer weet nu", "definieert het tijdvak", "het blok" en
   "de verwachte afwijking" als onderwerp. Sta "voorspelling van de intuïtie" hoogstens één keer
   per college toe. Zet dezelfde lijst in `CALQUES` van prose_stats.
2. Versoepel §11.3: de motiefnaam staat hoogstens één keer per college letterlijk en is nooit
   onderwerp of bron ("volgens de standaardfout van 2%"). Verder beschrijft de tekst wat het motief hier betekent.
3. Breid §3 en §11.4 uit met een tabel vaste termen: "hoofdstuk" of "college" in plaats van
   "lecture", "efficiënte grens", één keuze voor overrendement, "hedgen" (niet "indekken"),
   "waarderen" (niet "prijzen"), "evenwicht" (niet "marktruiming"), "lags", "horizonnen",
   "standaarddeviatie", "waarnemingen", "in/buiten de steekproef", "het lemma van Itô" en "dollar"
   bij Amerikaanse data. Voeg ook de nieuwe calques uit §1 van dit rapport aan de lijst toe.
4. Vul §11.2 aan: een zaak mag onderwerp zijn, maar niet van werkwoorden die een mens
   vragen (vraagt, kiest, beslist, eist, verwerpt, overstemt). Gebruik voor zaken
   "het/die/deze" of herhaal het zelfstandig naamwoord. Geen "diens", en "zij/haar" alleen als de
   verwijzing ondubbelzinnig is.
5. Pas §11.6 aan: "In woorden:" hoogstens drie keer per college, en de leeszin mag ook een
   gewone zin zijn die met het onderwerp begint. H12 en H5 vragen om de inhoud, niet om de
   formule "zoals de intuïtie voorspelde".

**Rubriek**
6. Verhoog criterium 3 (Taal) van 15% naar 20%, ten koste van opbouw (20% naar 15%), en voeg een
   hardop-toets toe. De beoordelaar noemt de zinnen die een Nederlandse econoom zo niet zou
   zeggen; zijn het er meer dan tien, dan is het deelcijfer hoogstens 7.
7. Voeg onder criterium 3 toe dat "regeltaal in de tekst", "motiefnaam als onderwerp" en
   "procesmeldingen" ("niet kunnen raadplegen") als taalfout tellen, net als calques.

**Schrijversprompt en werkwijze**
8. Voeg na F1 en na F6b een verplichte leesbeurt toe die buiten §10.3 valt. De schrijver leest het
   college één keer van boven naar beneden zonder rubriek, en herschrijft elke zin die hij niet zo tegen een
   collega zou zeggen. In het rapport staat het aantal herschreven zinnen.
9. Zet in §2.4 en §9.2: "Een punt oplossen betekent de bestaande zin herschrijven; een nieuwe zin
   alleen als er inhoud ontbreekt. Meld wat je niet kon controleren in het rapport, niet in de
   tekst."
10. Pas de drempels in prose_stats aan: `sent_mean` van 17 naar 19, en een nieuwe teller voor
    zinsopeners van de vorm "Woord woord:" (streefwaarde hoogstens acht per college). Dan verdwijnt
    de prikkel om zinnen te hakken.
