STATUS onderzoek-A-idioom klaar colleges=00_00,02_05,03_10,03_15

# Onderzoek A: idioom en vertaal-Nederlands

Gelezen: `lectures/00_00_setup.md`, `02_05_crsp_tape.md`, `03_10_merton_icapm.md`,
`03_15_shiller_excess_volatility.md` (elk één keer volledig), STYLE §7 en §11,
`plannen/rubriek-didactiek.md`, `plannen/kaart-rollen.md` §5, de drempels in
`tools/prose_stats.py`, `plannen/workflow-herziening.md` §2.1, §2.4, §9, §10.

Meting (`prose_stats`): gemiddelde zinslengte 14,5 / 14,8 / 14,1 / 15,5 woorden, p90
22–23. Samen ongeveer 1.440 zinnen. Alle vier geven PASS; geen enkele calque uit de lijst.
De tekst voldoet dus aan elke meetbare regel en leest toch niet als gewoon Nederlands.
De patronen hieronder vallen allemaal buiten wat `prose_stats` meet.

Telling per college (00_00 / 02_05 / 03_10 / 03_15, grep):

| patroon | 00 | 05 | 10 | 15 |
|---|---|---|---|---|
| "In woorden" | 1 | 7 | 0 | 6 |
| "*Waarom zou dit waar zijn?*" | 2 | 4 | 5 | 5 |
| "Let (in de figuur) op" / "De vraag bij het kijken" | 2 | 2 | 3 | 1 |
| "zij/haar" (ook voor personen) | 6 | 2 | 14 | 4 |
| "dus" (proza en wiskunde) | 13 | 24 | 25 | 27 |
| "equal-/value-weighted" | 1 | 43 | 0 | 0 |
| "myopisch" | 0 | 0 | 29 | 0 |

---

## 1. Top-10 taalpatronen

De volgorde houdt rekening met hoe vaak een patroon voorkomt en hoe storend het is.
Elk voorbeeld staat zoals het in de tekst staat, met daarna een herschrijving van
ongeveer dezelfde lengte.

### P1. Hakkerige hoofdzinnen: het verband tussen de zinnen is weggeknipt

Veel alinea's bestaan uit een reeks korte hoofdzinnen zonder voegwoord. De lezer moet
zelf raden of de volgende zin een oorzaak, een gevolg, een tegenstelling of een voorbeeld
geeft. Bij hardop lezen klinkt dat als een opsomming van losse beweringen. Dit patroon komt
het vaakst voor. Naar schatting kan 10–12% van alle zinnen beter worden samengevoegd met
de vorige of de volgende zin.

- **00_00:66–71** "Iemand formuleert een theorie. Dan komt er een bron van data waarmee die
  theorie voor het eerst te toetsen is: (...). En dan blijkt er een feit te zijn dat het
  model niet aankan. Dat feit is de barst, en de barst opent het volgende hoofdstuk."
  → "Iemand formuleert een theorie, en daarna komt er data waarmee die theorie voor het eerst
  te toetsen is: (...). Vroeg of laat duikt er een feit op dat het model niet aankan. Die
  barst opent het volgende hoofdstuk."
- **02_05:229–231** "Het herbeleggen van dividenden is een keuze. Die keuze scheidt de 9,0%
  van Fisher en Lorie, met herbelegde dividenden, van hun 6,9% zonder herbelegging"
  → "Of dividenden worden herbelegd, is een keuze. Die keuze verklaart het verschil tussen
  de 9,0% van Fisher en Lorie (herbelegd) en hun 6,9% (niet herbelegd)"
- **02_05:872–875** "Het kleinste deciel equal-weighted eindigt ruim een orde van grootte
  boven hetzelfde deciel value-weighted. Het zijn dezelfde aandelen. Alleen de weging binnen
  het deciel en het maandelijks herbalanceren verschillen."
  → "Gelijk gewogen eindigt het kleinste deciel ruim een orde van grootte hoger dan naar
  marktwaarde gewogen, hoewel het om dezelfde aandelen gaat. Alleen de weging en het
  maandelijks herbalanceren verschillen."
- **03_15:1041–1044** "De log-lineaire grens is het robuuste antwoord, en ze zegt iets
  bescheideners. De log-prijs-dividend-ratio beweegt 1,1 tot 1,9 keer zo veel als de
  dividendgroei kan rechtvaardigen, afhankelijk van de eindwaarde. Dat is geen factor
  dertien, maar het ligt boven één."
  → "De log-lineaire grens is robuuster en zegt ook minder. Afhankelijk van de eindwaarde
  beweegt de log-prijs-dividendratio 1,1 tot 1,9 keer zo veel als de dividendgroei
  rechtvaardigt. Dat is geen factor dertien, maar wel meer dan één."

### P2. Sjabloonzinnen die rechtstreeks uit de regels komen

Vaste formules die STYLE letterlijk voorschrijft of in de hand werkt, keren tientallen
keren terug. Voorbeelden zijn "In woorden:" (14 keer), "*Waarom zou dit waar zijn?*" (16),
"Zoals de intuïtie voorspelde" en "Dat is de N-de voorspelling van de intuïtie" (6),
"Let in de figuur op" (8), "Wat we nu weten:" of "We weten nu" (3), "Code en hand geven
dezelfde getallen" (3) en "Wat dit leert:" (11). Samen zijn dat ongeveer 65 zinnen. Elke
formule afzonderlijk is correct. Door de herhaling leest het college als een ingevuld
formulier, en dat is wat een lezer "niet normaal" noemt.

- **02_05:224** "In woorden: wat de houder op $t+1$ heeft, gedeeld door wat hij op $t$
  betaalde." → "De teller is wat de houder op $t+1$ bezit, de noemer wat hij op $t$
  betaalde."
- **03_15:300** "In woorden: wat de dividenden achteraf waard bleken, varieert zo veel als de
  prijs plus de voorspelfout." → "De achteraf gemeten waarde varieert dus evenveel als
  prijs en voorspelfout samen."
- **03_10:286 / 562 / 753** "Dat is de eerste voorspelling van de intuïtie." / "Dat was de
  derde voorspelling van de intuïtie." / "Dat de getrokken lijn stijgt, is de tweede
  voorspelling van de intuïtie." → "Zo verwachtten we het: de horizon doet er dan niet toe."
  / "Dat is de verzekering uit de intuïtie, nu met een prijs." / "De getrokken lijn stijgt,
  zoals we verwachtten."
- **02_05:300 en 389** Twee keer "Zoals de intuïtie voorspelde, ..." binnen negentig
  regels. → Bij de tweede keer: "Opnieuw is de fout positief en het grootst bij kleine,
  volatiele aandelen."
- **00_00:368–369** "De vraag bij het kijken: hoe lang blijft de reeks boven of onder die
  lijn?" → "Kijk vooral hoe lang de reeks boven of onder die lijn blijft."
- **03_15:213** "Wat we nu weten: over toestanden geldt $0 \le 16 \le 32{,}79$, dus ..."
  → "Over toestanden geldt dus $0 \le 16 \le 32{,}79$: ..."

### P3. Verwijswoorden zonder eenduidig antecedent

Wanneer een lange zin in tweeën wordt geknipt of een zin achteraf wordt ingevoegd, gaat
"die", "dat", "het" of "hij" naar iets wat niet in de vorige zin staat. H8 bestaat, maar
controleert alleen zinnen die met "Dat is" of "Dit is" beginnen.

- **02_05:61–62** "Maar elke meetbeslissing heeft een voorspelbaar teken, en die fout kan
  groter zijn dan de standaardfout van 2%" ("die fout" is nog niet genoemd; een beslissing
  heeft geen teken) → "Maar elke meetkeuze vertekent in een voorspelbare richting, en die
  vertekening kan groter zijn dan de standaardfout van 2%"
- **02_05:1003–1005** "Of de huidige data die rendementen bevatten, is zonder CRSP niet vast
  te stellen." ("data die rendementen bevatten" leest als een bijzin. Bedoeld zijn de
  delisting returns van drie zinnen eerder.) → "Of de huidige French-data de delisting
  returns van die aandelen bevatten, is zonder CRSP niet na te gaan."
- **00_00:113–116** "Het is geen vierde motief, maar de kant van risico of vergissing die een
  belegger voelt. Wat hij verdiende en behield, kwam uit het dragen van beloond risico."
  ("hij" lijkt op "een belegger" te slaan, maar bedoeld is Santa-Clara.) → "Het is geen
  vierde motief, maar de kant van risico of vergissing die een belegger zelf ondervindt.
  Santa-Clara's blijvende winst kwam van risico dat beloond werd."
- **03_10:1295–1296** "Dat de dividendopbrengst rendementen voorspelt, draagt de hele
  hedgevraag, en het feit laat twee lezingen toe." → "De hele hedgevraag rust op één feit:
  de dividendopbrengst voorspelt rendementen. Dat feit laat twee lezingen toe."

### P4. Werkwoordloze aankondigingen en fragmenten (telegramstijl)

STYLE §11.1 verbiedt dit, maar het wordt niet gemeten en komt vooral voor vóór codecellen
en in "Wat er brak".

- **02_05:626–628** "Nu de gemeten rendementen van het kleinste en het grootste deciel, per
  jaar, gemiddeld over de honderd steekproeven." → "De volgende cel geeft de jaarrendementen
  van het kleinste en het grootste deciel, gemiddeld over honderd steekproeven."
- **02_05:672 / 942** "Ten slotte het marktrendement zelf." / "Nu de size-premie per
  deelperiode, met 1981 als grens." → "Ten slotte kijken we naar het marktrendement zelf." /
  "Daarna splitsen we de size-premie in deelperioden, met 1981 als grens."
- **03_15:949 / 861** "Nu de gevoeligheid." / "Eerst de originele steekproef, met Shillers
  conventies." → "Hoe gevoelig is die ratio?" / "We beginnen met de originele steekproef en
  Shillers conventies."
- **03_10:1285 en 03_15:1060** "Niet in de wiskunde, maar in de invoer." / "Niet in de
  ongelijkheid, maar in haar meting." → "Het model breekt niet op de wiskunde maar op de
  invoer." / "Niet de ongelijkheid bezwijkt, maar de meting ervan."
- **02_05:189–190** "Dezelfde vijf aandelen, en de markt verloor 14% of won 13%, afhankelijk
  van één beslissing" (Engels: "Same five stocks, and ...") → "Met dezelfde vijf aandelen
  verloor de markt 14% of won ze 13%, afhankelijk van één beslissing"
- **00_00:1120** "Eerst de afleiding." → "We beginnen met de afleiding."

### P5. Definities tussen haakjes midden in de zin

H2 en H10 vragen naam, betekenis, orde van grootte en een voorbeeld "in dezelfde zin". Het
resultaat is een haakje van twaalf tot dertig woorden dat de hoofdzin onderbreekt. Hardop
verliest de lezer daardoor de draad.

- **03_10:87–89** "Het extra deel heet de *hedgevraag* (*hedging demand*: het deel van de
  portefeuille dat vermogen levert wanneer de beleggingskansen, kortweg de kansen,
  verslechteren)." → "Het extra deel heet de *hedgevraag* (*hedging demand*). Het levert
  vermogen op wanneer de beleggingskansen verslechteren. Die noemen we voortaan kortweg de
  kansen."
- **03_15:233–236** "Onder de *transversaliteitsvoorwaarde* (de verdisconteerde prijs in de
  verre toekomst gaat naar nul: bij $\delta = 0{,}954$ weegt een prijs over honderd jaar
  nog minder dan 1% mee) geldt, zoals in (...)," → "De *transversaliteitsvoorwaarde* zegt
  dat de verdisconteerde prijs in de verre toekomst naar nul gaat. Bij $\delta = 0{,}954$
  weegt een prijs over honderd jaar nog minder dan 1% mee. Dan geldt, zoals in (...),"
- **02_05:408–409** "Eén fout werkt de andere kant op: *look-ahead bias* (vertekening doordat
  een strategie informatie gebruikt die op het beslismoment nog niet bestond)." → "Eén fout
  werkt de andere kant op. Bij *look-ahead bias* gebruikt een strategie informatie die op
  het beslismoment nog niet bestond."
- **03_10:649–651** "We kalibreren op een jaarlijks VAR (*vector autoregression*, een
  regressie van elke variabele op de vertraagde waarden)." → "We kalibreren op een jaarlijks
  VAR (*vector autoregression*). Daarin is elke variabele geregresseerd op de vorige waarden
  van alle variabelen."

### P6. Engels-Nederlandse mengtaal

Engelse bijvoeglijke naamwoorden staan als onderwerp in een Nederlandse zin
("Equal-weighted ligt ..."). Engelse werkwoorden worden vernederlandst ("detrenden",
"gedemeend"). "Equal-/value-weighted" staat 43 keer in 02_05, terwijl "gelijk gewogen" en
"naar marktwaarde gewogen" (of "gelijkgewogen" en "marktgewogen") in het Nederlands gewoon
zijn. "Myopisch" (29 keer in 03_10) is aanvaardbaar vakjargon. Laat het staan, maar gebruik
het niet als bijwoord.

- **02_05:682–683** "Equal-weighted zonder delisting returns ligt een procentpunt te hoog,
  met alleen overlevenden bijna vijf." → "Gelijk gewogen ligt het marktrendement zonder
  delisting returns een procentpunt te hoog, met alleen overlevenden bijna vijf."
- **02_05:803–804** "Equal-weighted ligt rekenkundig 3,1 procentpunt hoger" → "Het gelijk
  gewogen gemiddelde ligt rekenkundig 3,1 procentpunt hoger"
- **03_15:498–499** "Een onderzoeker die de verhouding gebruikt in plaats van de niveaus,
  hoeft dus niets te detrenden." → "Wie de verhouding gebruikt in plaats van de niveaus,
  hoeft dus geen trend te verwijderen."
- **03_15:951–952** "en $pd^*_t$ (...) met gedemeende dividendgroei, zonder detrending" →
  "en $pd^*_t$ (...) met de dividendgroei min haar gemiddelde, zonder trendcorrectie"
- **02_05:422–423** "Daarom duwen de fouten van kleine aandelen het equal-weighted
  gemiddelde vol omhoog, en het value-weighted nauwelijks." → "Daarom tillen de fouten van
  kleine aandelen het gelijk gewogen gemiddelde volledig op, en het marktgewogen nauwelijks."

### P7. "dus" als het Engelse "so": universele verbinder, vaak met hoofdzinvolgorde

Er staan 89 keer "dus" in vier colleges. In proza vervangt het "daardoor", "daarom",
"zodat" en "want". Na een komma volgt vaak de Engelse volgorde ", dus de metingen
schommelen" waar formeel Nederlands inversie of "zodat" heeft. Daarnaast eindigen veel
alinea's met een slotzin van de vorm "X is dus Y". In 02_05:316, 349, 371 en 437 gebeurt dat
vier keer binnen 120 regels.

- **03_15:85–86** "Twee losstaande bronnen van variatie tellen op, dus de metingen
  schommelen minstens zo veel als de voorspellingen." → "Twee losstaande bronnen van variatie
  tellen op, zodat de metingen minstens zo veel schommelen als de voorspellingen."
- **02_05:321–322** "Er is geen drift, dus het ware verwachte logrendement is nul." →
  "Omdat er geen drift is, is het ware verwachte logrendement nul."
- **03_15:811–812** "De Dow-reeks is niet gratis beschikbaar, dus we tonen de S&P over
  1928–1979 als benadering." → "Omdat de Dow-reeks niet gratis is, tonen we als benadering de
  S&P over 1928–1979."
- **02_05:1121–1122** "wordt bij maandelijkse waarneming niet geschrapt, dus de selectie is
  iets milder." → "wordt bij maandelijkse waarneming niet geschrapt, zodat de selectie iets
  milder is."

### P8. Leenvertaalde collocaties en beeldspraak

Deze combinaties zijn woord voor woord correct, maar een Nederlandse econoom zou ze niet
zo zeggen.

- **00_00:104–105** "In 2013 kregen Fama en Shiller samen de Nobelprijs, en dat was een
  juiste beschrijving van de stand van het vak." → "In 2013 kregen Fama en Shiller samen de
  Nobelprijs, en dat gaf de stand van het vak goed weer."
- **03_10:58–59 en 03_15:65** "Dat werk definieert het tijdvak" / "Dit werk bepaalde het
  tijdvak" (Engels: "defines the era") → "Met dat werk begint het tijdvak" / "Dit werk
  stempelde het tijdvak"
- **03_15:942–943** "Het beeld van 1981 overleeft: $p^*$ kabbelt, de koers niet." → "Het
  beeld van 1981 blijft overeind: $p^*$ kabbelt, de koers niet."
- **03_10:1302–1303** "Scheiden vraagt of verwachte rendementen meebewegen met consumptie en
  recessies" (het werkwoord klopt niet) → "Om ze te scheiden, moeten we weten of verwachte
  rendementen meebewegen met consumptie en recessies"
- **03_10:26** "De barst die openblijft, is de ene periode van het CAPM." → "De barst zit in
  de ene periode van het CAPM."
- **02_05:68–69** "Maar wie het probeert, krijgt van de data drie vragen terug." → "Maar wie
  het probeert, stuit op drie vragen."
- **00_00:1057–1058** "Wie een rangorde van gemiddelde rendementen serieus neemt, neemt ruis
  serieus." (Engelse chiasme) → "Een rangorde van gemiddelde rendementen is hier vooral een
  rangorde van ruis."

### P9. "zij" en "haar" voor zaken

Voor de-woorden als hedgevraag, standaardfout, posterior en Brownse beweging kiest de
tekst "zij" of "haar". Formeel mag dat, maar in lopende uitleg klinkt het stijf ("Daarna
vlakt zij af"). Soms is het ook dubbelzinnig. Een natuurlijke schrijver gebruikt "ze",
"die" of het zelfstandig naamwoord. In 03_10 staat het veertien keer.

- **03_10:781–782** "Daarna vlakt zij af, maar op vijftig jaar ligt zij nog onder de grens"
  → "Daarna vlakt ze af, maar op vijftig jaar ligt ze nog onder de grens"
- **03_10:944–945** "Gemiddeld komt zij uit op 0,450, te hoog." → "Gemiddeld komt de
  schatting uit op 0,450, te hoog."
- **03_10:1165** "De posterior van $b$ is even breed als haar gemiddelde." ("haar" kan op de
  posterior of op $b$ slaan) → "De posterior van $b$ heeft een standaarddeviatie zo groot als
  het gemiddelde."
- **00_00:1006–1007** "Bereken haar ook uit de maandelijkse verschilreeks" → "Bereken die ook
  uit de maandelijkse verschilreeks"
- **03_10:245–246** "In [](#02-09-black-scholes) heette zij $W_t$" → "In (...) heette die
  $W_t$"

### P10. Engelse zinsbouw: gebiedende wijs met ", en er volgt", pseudo-cleft en naamwoordstijl

Dit patroon heeft drie vormen:

- de Engelse constructie "Do X, and you get Y";
- "Wat X, is Y", dat STYLE §11.4 zelf als calque noemt, maar dat `prose_stats` niet vangt;
- "het + infinitief + van".

- **03_10:222** "De kern is de vierde stap: tel de vraag van alle beleggers op, en er volgt
  het ICAPM." → "De kern is de vierde stap: uit de opgetelde vraag van alle beleggers volgt
  het ICAPM."
- **03_10:319–320** "Trek $J(W_t,t)$ aan beide kanten af, en er staat $0 = \max_w
  \E_t[dJ]$." → "Na aftrekken van $J(W_t,t)$ aan beide kanten staat er $0 = \max_w
  \E_t[dJ]$."
- **03_15:244–245** "Laat de verwachting weg, en er ontstaat de ex-post rationele prijs" →
  "Zonder de verwachting krijgen we de ex-post rationele prijs"
- **03_15:39–40** "Wat overblijft, is een kleinere overschrijding die hetzelfde feit is als
  voorspelbare rendementen." → "Er blijft een kleinere overschrijding over, en die is
  hetzelfde feit als voorspelbare rendementen."
- **03_15:1031–1032** "Wat overblijft, is dat $p^*$ en de koers maar deels samen bewegen" →
  "Er blijft alleen over dat $p^*$ en de koers maar deels samen bewegen"
- **03_10:1280–1281** "wat wel een reden is: het indekken van veranderende
  beleggingskansen" (naamwoordstijl en een verkeerd voorzetsel) → "wat wel een reden is: zich
  indekken tegen veranderende beleggingskansen"
- **00_00:116** "kwam uit het dragen van beloond risico" → "kwam van beloond risico dat hij
  droeg"

---

## 2. Oorzaakhypothesen

| patroon | vermoedelijke bron | regel (citaat) |
|---|---|---|
| P1, P3 | STYLE §11.1 | "Eén gedachte per zin. Richtlengte 12 tot 20 woorden, nooit boven 40." en "Een zin met een puntkomma wordt bijna altijd twee zinnen." Er staat geen ondergrens bij en geen opdracht om verband te houden. |
| P1, P3 | STYLE §11.1, gedachtestreepje | "'X — en dat is Y' wordt 'X. Dat is Y.'" Het voorbeeld zelf levert een losse "Dat is"-zin op. |
| P1 | `prose_stats.py` THRESHOLDS | `"sent_mean": 17`, `"sent_p90": 28`, `"sent_gt40": 2`, `"semicol": 15`, `"dash": 10`. Alleen bovengrenzen: korter is altijd veilig. De colleges zakken naar 14–15,5 woorden per zin. |
| P1, P3, P5 | workflow §2.1 | "Doel 4.500 tot 5.300 woorden." en "`--check` moet PASS geven, ook op words." Onder woorddruk sneuvelen eerst de goedkope woorden: voegwoorden en overgangen. |
| P3, P5 | workflow §2.4 en §9.2 | "Elk *toevoegen* betaal je met schrappen elders" en "Wijs een punt alleen af met een regel uit STYLE of 'Wat niet meetelt'." Lezerspunten worden als ingeplakte zinnen of haakjes opgelost, en een schrijver kan een punt niet om taalredenen afwijzen. |
| P3, P4, herhalingen | workflow §10.2–3 | "Wijzigingen gebundeld: één Python-script of één Write per sectie" en "daarna alleen `grep -n` of `sed -n` van hoogstens 40 regels". De schrijver past aan zonder de omringende alinea opnieuw te lezen. Gevolg: een antecedent verdwijnt, alinea's breken halverwege (02_05:297, 833) en één zin staat drie keer in 02_05 (zie §3). |
| P2 | STYLE §11.6 | "één zin die de vergelijking in woorden leest" wordt 14 keer letterlijk "In woorden:". |
| P2 | STYLE §11.10 H12 | "De theorie zegt expliciet waar die verwachting wordt bevestigd of verfijnd ('zoals de intuïtie voorspelde, ...')". Het voorbeeld is overgenomen als sjabloon. |
| P2 | STYLE §11.10 H9 en §11.7 | "de zin vóór een figuur zegt waar de lezer op moet letten" wordt "Let in de figuur op". "één zin die zegt wat de lezer nu weet" wordt "Wat we nu weten:". "Elke uitwerking eindigt met een zin die begint met 'Wat dit leert:'" |
| P5 | STYLE §11.10 H2 en H10 | "Een symbool krijgt bij de eerste keer een naam, een betekenis en een orde van grootte" en "één concreet voorbeeld in dezelfde zin". Dat dwingt tot lange haakjes midden in de zin. |
| P4 | STYLE §11.1 zonder meting | "Geen telegramstijl" staat er wel, maar `prose_stats` telt het niet. Daardoor controleert niemand het. |
| P6 | STYLE §11 en §3 ("Vaktermen blijven Engels waar een vertaling gekunsteld is", 00_00:217–219) | Er is geen lijst met welke termen Nederlands horen. "Gelijk gewogen" is niet gekunsteld. |
| P7–P10 | STYLE §11.4 is een gesloten tabel, CALQUES in `prose_stats` idem | "De lijst hieronder is niet volledig". Toch toetst de pijplijn alleen die lijst. Rubriek criterium 3 weegt 15%, en de beoordelaar leest met een afvinklijst, niet met het oor. |
| alle | rubriek en kaart-rollen §5 | "Taal: zinnen gemiddeld ≤ 17 woorden, geen zin > 40, (...), geen calques uit het Engels". De taalcontrole van F23 en F6 bestaat uit tellingen. Geen enkele rol leest hardop of vraagt: "zou een Nederlander dit zo zeggen?". |

Kern: de regels belonen korte zinnen en bepaalde verplichte zinnen, en straffen alleen
lengte. Wat de lezer als "geen normaal Nederlands" ervaart, komt vooral voort uit het
optimaliseren op die tellingen, gecombineerd met ingrepen via patches (§10) zonder de
alinea opnieuw te lezen.

---

## 3. Overige verbeterpunten

- **Drie keer dezelfde zin in 02_05.** "Meer data halen de fout niet onder de ruis: de fout
  door ontbrekende delisting returns blijft staan, en die van overlevenden krimpt hoogstens
  even snel als de ruis." staat letterlijk op 02_05:40–42, 88–90 en 1026–1028. Hij hoort
  alleen in de intuïtie. Het Overzicht en "Wat er brak" kunnen elk een eigen formulering
  krijgen.
- **Vraag dubbel in admonition en Overzicht.** De openstaande vraag staat woordelijk in de
  admonition en in de eerste zin van het Overzicht (00_00:31–32 en 37–38, 03_15:30–31 en
  36). Het sjabloon van §11.7 lokt dat uit. Het Overzicht kan de vraag parafraseren.
- **Alinea's gebroken door patches.**
  - 02_05:297–298 begint een alinea met "In de kleinste Nasdaq-aandelen", midden in de
    redenering.
  - 02_05:833 begint met "Het equal-weighted marktrendement is dus".
  - 02_05:805 plakt "Er is geen enkel aandeel anders gemeten." zonder verband achter een
    zin over variantie.
- **Toy in 03_10 (143–145) steunt op formules die nog niet zijn afgeleid.** "Het recept"
  verwijst twee keer vooruit ("Theorie leidt die vorm af", "stap 4 schrijft die voorwaarde
  uit"). Stap 1 gebruikt de eerste-ordevoorwaarde zonder afleiding. Dat zijn twee
  niet-afgeleide formules, tegen §11.7 in. Het is ook zwaar voor een instapvoorbeeld.
- **Replicatie 3 in 03_10 (1252–1265) vergelijkt ongelijke gevallen.** De tabel
  origineel/hier zet Barberis' $\gamma = 10$, koop-en-houd, naast $\gamma = 5$ met
  jaarlijks herbalanceren. De tekst geeft dat toe. Reken $\gamma = 10$ uit of laat de tabel
  weg.
- **03_10:877:** `# TODO: naar hap.stats` staat in gepubliceerde code.
- **03_15:1015 tegen 1061:** "van 0,55 tot 9,8" tegenover "tussen 0,55 en 9,3 over
  1871–2025". Controleer of 9,8 bij 1928–1979 hoort. Zo ja, zeg dat.
- **Code.**
  - `measure` in 02_05:579–606 telt 27 regels, boven de 25 van §11.8.
  - `shiller_test` in 03_15:619–655 telt ongeveer 36 regels. Het is één functie, maar de
    trendschatting kan eruit.
  - De oefentekst in 03_10:1320 zet codejargon in proza ("w0 in geval B min de myopische
    fractie").
- **Lijstinterpunctie wisselt.** Het Overzicht sluit lijstitems af met ";" in 03_10, met
  "," in 03_15 en met ";" in 00_00 en 02_05. Kies één vorm.
- **Figuren.** `fig-setup-se` (00_00:901) heeft als enige geen `:width:`. Verder zijn de
  leeswijzers goed, maar ze zijn allemaal volgens hetzelfde sjabloon geschreven (P2).
- **Didactiek sterk.** De toys van 02_05 en 03_15 zijn met de hand na te rekenen en keren
  terug in theorie en simulatie. De simulatie in 03_15 ("hoe vaak slaat de toets alarm")
  is een schoolvoorbeeld van één steekproefvraag. Niet aan tornen.

---

## 4. Aanbevelingen

### STYLE.md

1. **§11.1, zinslengte.** Vervang "Richtlengte 12 tot 20 woorden" door "Wissel korte en
   middellange zinnen af; gemiddeld 15 tot 20 woorden. Verklaart de tweede zin de eerste,
   verbind ze dan met *omdat, zodat, terwijl, maar* of een dubbele punt."
2. **§11.1, gedachtestreepje.** Vervang het voorbeeld "'X — en dat is Y' wordt 'X. Dat is
   Y.'" door "wordt 'X, en dat is Y' of 'X: Y'".
3. **§11.4, tabel uitbreiden.** Nieuwe rijen, elk met een vervanging:
   - "Doe X, en er volgt Y" → "Uit X volgt Y" of "Als we X doen, ...";
   - "Wat overblijft, is X" → "Er blijft X over";
   - ", dus + onderwerp + werkwoord" → "zodat" of "dus" met inversie;
   - "zij/haar" voor zaken → "ze/die/het";
   - werkwoordloze aankondiging "Nu de X." → "Nu kijken we naar X.";
   - "definieert het tijdvak", "overleeft", "heeft een teken", "het indekken van".
4. **§11.6 en H9, H12: functie in plaats van formule.**
   - "De leeszin na een vergelijking begint niet met 'In woorden:'."
   - "'Zoals de intuïtie voorspelde' en 'Let in de figuur op' elk hoogstens twee keer per
     college; varieer de vorm."
   - Schrap in H12 het voorbeeld tussen aanhalingstekens.
5. **H2 en H10: een lange definitie krijgt een eigen zin.** "Een definitie van meer dan acht
   woorden staat in een eigen zin direct na de term, niet tussen haakjes."
6. **§3: een lijst voor Engels of Nederlands.** Neem een korte lijst op van termen die
   Nederlands zijn (gelijk gewogen, marktgewogen, trend verwijderen) en termen die Engels
   blijven (delisting return, look-ahead bias).
7. **§11.9, afvinklijst.** Voeg toe: "Twee willekeurige alinea's per `##` hardop gelezen;
   elke zin die je hardop anders zou zeggen, is herschreven."

### tools/prose_stats.py

Nieuwe metrieken, met een voorgesteld maximum. Alle regexes gelden op lopende tekst.

| metriek | regex of lijst | max |
|---|---|---|
| `fragment` | `(?m)(?:^|(?<=\. ))(?:Nu|Eerst|Ten slotte|Daarna) (?:de|het|een|zijn|haar)\b[^.]{0,90}\.` plus `(?m)^Niet in de [^.]*, maar in` | 0 |
| `formula` | `In woorden:`, `[Zz]oals de intuïtie (voorspelde|verwachtte)`, `voorspelling van de intuïtie`, `Let (in de figuur )?op`, `Wat we nu weten`, `De vraag bij het kijken` (samen) | 5 |
| `cleft` | `(?:^|(?<=\. ))Wat [^,.]{3,60}, (?:is|was|zijn|blijkt)\b` | 1 |
| `imp_en` | `\b(?:Trek|Tel|Laat|Vermenigvuldig|Draai|Neem|Vul)\b[^.]{0,80}, en (?:er )?(?:staat|volgt|ontstaat|blijkt|wordt)` | 0 |
| `dus_svo` | `, dus (?:de|het|een|we|hij|ze|zij)\b` | 2 |
| `zij_zaak` | `\b(?:zij|haar)\b` (alleen rapporteren, drempel 6) | 6 |
| `engmix` | `(?:^|(?<=\. ))(?:Equal|Value)-weighted\b`, `\bdetrend(?:en|ing)\b`, `\bgedemeend` | 0 |
| `repeat` | elke zin van 12 of meer woorden die letterlijk twee keer voorkomt | 0 |
| `short_run` | drie opeenvolgende zinnen van minder dan 9 woorden (tellen) | 3 |

Voeg daarnaast een ondergrens toe: `sent_mean` ≥ 14. Onder de 14 woorden meldt het script
"hakkerig", zodat korter niet meer automatisch veilig is.

### Rubriek (criterium 3, Taal)

- **10:** "leest hardop als gesproken academisch Nederlands; geen sjabloonzin valt op".
- **5:** "reeksen korte hoofdzinnen zonder verband; formules die zichtbaar uit een regel
  komen".
- **Hardop-toets:** de beoordelaar leest drie willekeurige alinea's hardop en citeert elke
  zin die hij anders zou zeggen. Vanaf zes zulke zinnen is het deelcijfer hoogstens een 7.
- **Gewicht:** overweeg taal van 15% naar 20%, ten koste van opbouw (20% → 15%).

### Schrijversprompt (workflow §2.1, §2.4, §9.2, §10)

- **Eén keer volledig herlezen.** Voeg na F1 en na F6b een taalronde toe: "Lees elke
  gewijzigde `##`-sectie in zijn geheel (uitzondering op §10.3). Voeg weggevallen verbanden
  weer toe en controleer elk verwijswoord."
- **Verbanden sparen bij schrappen.** "Schrap geen voegwoorden of overgangszinnen om words te
  halen; schrap liever een alinea of voorbeeld."
- **Afwijzen om taalredenen toestaan.** Maak in §9.2 een lezerspunt ook afwijsbaar met "zou
  de zin onnatuurlijk maken".
- **Aparte taalredacteur.** Overweeg na F6c één taalredacteur per college met alleen
  STYLE §11.1 en §11.4 en deze notitie. Die schrijft alleen zinnen om en verandert niets aan
  inhoud of getallen, binnen een budget van ongeveer 15 toolaanroepen.

### Schatting van het getroffen deel

In de vier colleges staan ongeveer 1.440 zinnen:

- P1, hakkerig: ongeveer 150 zinnen (10%);
- P2, sjabloon: ongeveer 65 zinnen (4,5%);
- P3, antecedent: ongeveer 40 zinnen (3%).

Met wat overlap heeft **ongeveer 17–20% van de zinnen, grofweg één op de vijf à zes,**
last van de top-3. Tellen we P4–P10 mee, dan komt het op ongeveer 30%. Het aandeel is het
hoogst in 02_05 (P1, P2, P6) en 03_10 (P5, P9, P10), en het laagst in 00_00.
