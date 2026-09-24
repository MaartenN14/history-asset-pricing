STATUS 02_08_capm F5c words=5495 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling 02_08_capm: Het CAPM

## Eindcijfer: 8,1

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·7 + 0,1·8 + 0,05·9 = 8,05, afgerond 8,1.

## 1. Helderheid van de uitleg (8)

*Goed*
- "Het kernresultaat": de premieformule [](#eq-capm-premie) krijgt twee getallen, het
  toy ($4{,}5 \cdot 0{,}0138 = 6{,}22\%$) en echte data ($\theta_m \approx 0{,}06/0{,}04 =
  1{,}5$), en een zin wat er gebeurt als $\theta_m$ of $\sigma_m$ verandert.
- "Geschatte bèta's": [](#eq-capm-eiv) wordt meteen doorgerekend ($\sigma_u^2 = 0{,}082$,
  $\kappa = 0{,}52$, intercept 3,4% per jaar te hoog, $\kappa = 0{,}98$ bij $n = 50$).
- "Fama en MacBeth": waarom de eenvoudige standaardfout klopt (een portefeuille met
  kosten nul en bèta één), met de grootte ($0{,}045/\sqrt{480} = 0{,}21\%$ per maand) en de
  Shanken-correctie als getal (1,02).

*Aanmerkingen*
- "Overzicht": "Het *Capital Asset Pricing Model* is de eerste theorie in deze reeks die
  niet zegt wat een belegger moet doen, maar wat prijzen zijn." De lezer heeft net
  02_06 gelezen, waar Samuelson en de SDF-prijsvergelijking al zeggen wat prijzen zijn,
  en in 01_03 Williams. De bewering vraagt een afbakening (de eerste
  *evenwichtstheorie* van verwachte rendementen).
- "GRS-toets": "de ML-schatter van de covariantiematrix" en "een Hotelling-$T^2$" staan
  er zonder regel uitleg; "ML" wordt nergens uitgeschreven.
- "Zonder vrij lenen": "Als elke belegger een portefeuille op de
  minimum-variantierand houdt". Waarom hij dat doet (mean-variance zonder risicovrij
  activum) staat er niet; de lezer moet het uit 01_04 halen.
- "Wat er brak", risicolezing: "Wie wel kan lenen, verdient de premie als beloning
  {cite}`FrazziniPedersen2014`." Welke premie (de alfa van lage bèta met hefboom) blijft
  open; "de premie" heette tot dan toe de marktpremie.
- "Hoe het getoetst wordt: de tijdreeks en GRS": de GRS-toets krijgt geen uitgerekend
  voorbeeld in theorie of simulatie; het eerste GRS-getal verschijnt pas in de
  replicatietabel.

*Beter uitleggen*
- GRS: één zin wat "ML" is (delen door $T$) en dat de $F$-verdeling de kleine-steekproefvorm
  van een $\chi^2$-toets op alle alfa's samen is.
- Frazzini-Pedersen: één zin welke strategie (lage bèta met hefboom, hoge bèta short)
  die beloning oplevert.

*Voor een 9*: baken de "eerste theorie"-zin in het Overzicht af; leg ML en Hotelling
in één regel uit bij de GRS-stelling; zeg in de zero-beta-stelling waarom beleggers op
de rand zitten; benoem de premie in de risicolezing van "Wat er brak"; geef GRS een
getal in de simulatie of in de theorie (bijvoorbeeld wat een alfa van 0,2% per maand
op tien portefeuilles oplevert).

## 2. Opbouw en rode draad (8)

*Goed*
- "Overzicht" stelt de vraag en geeft het antwoord (evenredig met bèta); de intuïtie
  voorspelt drie dingen (rechte lijn door $R^f$ en de markt, eigen risico telt niet, één
  prijs van risico) en de theorie verwijst terug ("Zoals de intuïtie voorspelde").
- Eén getallenlijn van begin tot eind: toy 6,22%, simulatie 0,6% per maand ("iets boven
  de 6,22% van het toy-voorbeeld"), French-premie 0,60% per maand; de
  $\sigma_m/\sqrt{T} = 2{,}5\%$ uit de theorie komt exact terug in de simulatie.
- Routekaart en "Samengevat" op hun plaats; "Wat er brak" sluit met "De simulatie liet
  zien dat dit op portefeuilles geen artefact van geschatte bèta's kan zijn".
- 5.475 woorden: onder de grens, maar met 25 woorden marge.

*Aanmerkingen*
- "Simulatie": de sectie opent met een vraag ("Wat vindt Fama-MacBeth ... als het CAPM
  per constructie exact geldt"), niet met haar conclusie (te vlak op aandelen, zuiver
  maar breed op portefeuilles).
- "Replicatie op echte data": het oordeel staat op twee plekken. Eerst
  "**Gedeeltelijk geslaagd.**", drie alinea's later "Na BJS is het resultaat eenduidig,
  ... en daar is de replicatie geslaagd."
- De laatste cel (rollende Fama-MacBeth) sluit af met "Met rollende bèta's verandert
  het beeld niet": een extra meting zonder nieuwe conclusie, in een lecture die tegen
  de woordgrens aan zit.

*Beter uitleggen*
- Het oordeel van de replicatie in één blok: per periode Geslaagd / Gedeeltelijk, met
  de verwachte afwijking ernaast.

*Voor een 9*: open "Simulatie" met het antwoord; voeg de twee oordelen samen tot één
alinea direct na de vergelijkingstabel; schrap de rollende Fama-MacBeth of maak er een
oefening van.

## 3. Taal (8)

*Goed*
- Korte zinnen (gemiddeld 14,2 woorden, geen boven 40); geen u/je.
- Het "mandje" in "Intuïtie" maakt de separatie en de marktclearing concreet zonder
  formule.
- De motieven worden ter plekke uitgelegd ("Hier betekent de vraag: is de vlakke lijn
  een correcte evenwichtsprijs, of een prijs die ernaast zit?").

*Aanmerkingen*
- Twee namen voor hetzelfde begrip: "de frontier van Markowitz", "de markt ligt op de
  frontier", "niet op hun frontier" naast "de minimum-variantierand",
  "randportefeuilles", "op de rand" (01_04 zegt "rand").
- "Theorie", routekaart: "de valkuil die beide vormgaf". "Vormgaf" leest stroef; bedoeld
  is dat de valkuil beide toetsen heeft gevormd.
- Engelse termen zonder Nederlandse uitleg: "value-weighted" ("onze markt is
  value-weighted"), "size/BM", "pre-ranking bèta's" (alleen cursief).
- "Toy-voorbeeld", slot: "De lezer weet nu het mechanisme". Meta-taal over de lezer
  in plaats van de conclusie zelf.

*Voor een 9*: één naam voor de rand (zoals in 01_04); herschrijf de routekaartzin;
"waardegewogen" of een korte uitleg bij value-weighted, en "size/BM" één keer
uitschrijven (grootte en boekwaarde/marktwaarde); laat de slotzin van het toy de
conclusie zelf zeggen.

## 4. Toy-voorbeeld (9)

*Goed*
- Eén mechanisme (marktclearing), in vijf stappen met de hand na te rekenen:
  $\theta_m = 4{,}5$, $\boldsymbol{\Sigma}\mathbf{w}_m = (4;6;1)/225$, premies 8%, 12%,
  2%, bèta's $9/7$, $27/14$, $9/28$. Nagerekend: alles klopt.
- Het draait 01_04 om ("Daar waren de verwachte rendementen gegeven ... Hier zijn het
  aanbod en de beleggers gegeven") en levert precies de rendementen die 01_04 aannam.
- Eén nog niet afgeleide formule (de vraag $\theta_k^{-1}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}$),
  als zodanig aangekondigd; tabel hand/code met elf rijen.

*Aanmerkingen*
- Stap 3: "Invullen laat zien dat $\mathbf{x} = (1{,}5;\ 1;\ 2)'$ dat doet." De lezer krijgt
  de oplossing zonder het stelsel; met de hand vinden kost meer dan vijf minuten.

## 5. Code en figuren (7)

*Goed*
- De simulatie leest als de wiskunde: `ts_betas` en `fama_macbeth_gammas` met een
  zichtbare lus over de maanden en de gewichtenmatrix die de tekst uitlegt.
- Elke cel heeft een zin ervoor en erna; beide figuren hebben een leeswijzer ("Let
  links op de gestreepte lijn door de aandelen") en een figuurtekst.

*Aanmerkingen*
- `beta_sorted_portfolios`: `pd.qcut(pre_beta.rank(method="first", ascending=False), ...)`
  en `holding.T.groupby(group.to_numpy()).mean().T` zijn trucs; de tekst ervoor zegt
  alleen "sorteren in tien groepen".
- `rolling_fama_macbeth`: `out.attrs = {}  # drop the per-period gammas so pd.concat does
  not compare them` is een bibliotheekomweg zonder verband met de wiskunde.
- `one_capm_sample`: de lokale variabele `stats = {...}` overschaduwt de geïmporteerde
  `scipy.stats`, die twee cellen later weer als module wordt gebruikt.
- `sml_table`: negen rijen maal vijftien kolommen in één tabel; de tekst citeert er een
  handvol getallen uit, de lezer moet zoeken.
- Presentatietabellen tonen code-achtige labels ("g0 aandelen", "gamma_0 (% p.m.)",
  "sd ware bèta portefeuilles", "sigma_m / wortel T (% p.j.)").

*Beter uitleggen*
- Eén zin bij `beta_sorted_portfolios` hoe de groepen worden gevormd (rangorde, hoogste
  bèta in P1, tien gelijke groepen).

*Voor een 9*: schrijf de groepsvorming in `beta_sorted_portfolios` met een zichtbare
toewijzing of leg de truc uit; haal de `attrs`-omweg uit de lecturecode (naar
`hap.stats`); hernoem `stats` in `one_capm_sample`; splits `sml_table` in een
getoonde kerntabel (γ₀, γ₁, premie, GRS, p) en de rest; leesbare labels.

## 6. Replicatie en empirie (8)

*Goed*
- Blok met bron, wat, data, verschil en verwachte afwijking, onder 250 woorden; de
  verwachte afwijking noemt een grootte (standaardfout van de premie ruim 0,3% per
  maand).
- Tabel origineel/hier voor zes perioden; het oordeel begint met "Gedeeltelijk
  geslaagd" en verwijst naar de verwachting ("zoals de verwachte afwijking
  aankondigde").
- De afwijking in 1931–1965 wordt verklaard (hoge bèta valt samen met klein in de
  size-gesorteerde basisactiva) en in oefening 3 getoetst.

*Aanmerkingen*
- "Replicatie op echte data": "Op French' bèta-decielen is de helling 0,28% tegen een
  premie van 0,60%, en het laagste bèta-deciel heeft een alfa van 0,21% per maand
  ($t = 2{,}53$). Op de 25 size/BM-portefeuilles is de helling −0,37% en het intercept
  1,16% per maand, met GRS $= 4{,}20$ tegen een 5%-grens van 1,52." Getallen in lopende
  tekst die de lezer in de brede tabel moet terugzoeken.
- Twee oordelen voor één replicatie (zie criterium 2).
- De premie wijkt sterk af (1,42 bij BJS tegen 0,93 hier; 2,20 tegen 0,84 in 1931–1939).
  De verwachte afwijking voorspelt dat niet, en de tekst zegt niet dat het de
  gelijkgewogen index van BJS is.
- 1939–1948: $\gamma_0$ is −0,39 hier tegen +0,44 bij BJS, een ander teken, terwijl de
  verwachte afwijking "het teken van de afwijking gelijk" eist; de tekst zegt alleen
  "de helling daalt en het intercept stijgt".

*Voor een 9*: één oordeelsblok met per periode het label en de verwijzing naar de
verwachting; de post-1963-getallen in een kleine eigen tabel; één zin verwachte
afwijking voor de premie (EW tegen VW); benoem het tekenverschil in 1939–1948.

## 7. Oefeningen (9)

*Goed*
- Precies de drie typen: instap op het toy (1), afleiding van de meetfoutvariantie en
  $\kappa$ (2), uitbreiding van de replicatie met andere basisactiva (3); elke
  uitwerking eindigt met "Wat dit leert".
- Oefening 1 levert een scherpe les ("bèta's zijn een eigenschap van de activa, de
  premie is een eigenschap van de beleggers"); oefening 3 laat zien dat de keuze van
  testactiva het antwoord verandert.

*Aanmerkingen*
- Uitwerking oefening 2, tabel: de kolommen "gesimuleerde helling" en "gesimuleerd
  intercept" staan ook in de rij "spreiding 0,22" (0,316 naast een voorspelde 0,222),
  terwijl de simulatie alleen de aandelenwereld met spreiding 0,30 meet.

## Feitelijke fouten

Geen gevonden.

Nagerekend en correct: toy ($\theta_m = 4{,}5$; $\boldsymbol{\Sigma}\mathbf{w}_m =
(4;6;1)/225$; premies 8/12/2%; $\mathbf{x} = (1{,}5;1;2)$; posities en 187,5 lenen en
uitlenen; $\sigma_m^2 = 28/2025$; 6,22%; bèta's; 0,00143 en 86%; Sharpe 0,20/0,40);
bewijzen van CAPM, bèta-representatie, zero-beta en de GRS-decompositie; $\theta_m
\approx 1{,}5$; GRS-grens 1,52 bij 25 en 757; FM-standaardfout 0,21% en 2,5%; Shanken
1,02; $\sigma_u^2 = 0{,}0823$, $\kappa = 0{,}522$, 0,287% en 3,4% per jaar, $\kappa = 0{,}98$
bij $n = 50$; simulatie (0,316/0,298 tegen 0,318/0,287; 0,594/0,015; 2,465 = 2,465;
0,183; 0,957; 0,305 → 0,219); tijdreekstabel (bèta 1,69–0,91, $|t| \le 1{,}36$, SE
0,29–0,58, $R^2$ 0,81–0,93); SML-tabel en alle tekstgetallen (1,06/0,93; −0,76; 0,78/0,96;
0,27; 0,28/0,60; 0,21 met $t$ 2,53; −0,37; 1,16; GRS 4,20/1,52; drie GRS-verwerpingen na
1963); rollende FM (0,80, $t$ 2,11; 0,95, $t$ 3,85, 11,4% per jaar); oefening 1 (4;
5,53%; 7,11/10,67/1,78%; 150), oefening 2 (18 en 33), oefening 3 (0,74; 0,80; 0,29 met
$t$ 1,05). De gepubliceerde waarden van BJS (1972) en Fama-MacBeth (1973) komen overeen
met wat ik ken van de papers, maar zijn niet tegen de tabellen gecontroleerd.

## De drie verbeteringen met het meeste effect

1. **Replicatiecode en -tabellen leesbaar maken** (`beta_sorted_portfolios`,
   `rolling_fama_macbeth`, `sml_table`, `one_capm_sample`): trucs uitleggen of vervangen,
   `attrs`-omweg weg, `stats` hernoemen, een smalle kerntabel. Code en figuren 7 → 8,5.
2. **Eén oordeelsblok voor de replicatie**: per periode het label, de premieafwijking
   (EW/VW) en het tekenverschil 1939–1948 benoemd, de post-1963-getallen in een tabel.
   Replicatie 8 → 9, opbouw 8 → 8,5.
3. **Helderheid op vier plekken**: "eerste theorie" afbakenen, ML/Hotelling bij GRS,
   waarom beleggers op de rand zitten (zero-beta), welke premie Frazzini-Pedersen
   bedoelen. Helderheid 8 → 9.

## Navertelling in vijf zinnen

Als alle beleggers mean-variance optimaliseren met dezelfde verwachtingen en vrij kunnen
lenen, houdt iedereen dezelfde tangentportefeuille, en marktclearing maakt die gelijk aan
de markt. Daaruit volgt dat het verwachte excess rendement bèta maal de marktpremie is,
met een premie gelijk aan de geaggregeerde risicoaversie maal de marktvariantie; zonder
vrij lenen blijft de lijn recht maar vlakker, met een intercept boven de rente. Getoetst
wordt met tijdreeksalfa's (GRS) en maandelijkse cross-sectieregressies (Fama-MacBeth),
waarbij geschatte bèta's op aandelen de lijn kunstmatig vlakker maken en portefeuilles
dat oplossen, maar de premie nooit scherper meten dan $\sigma_m/\sqrt{T}$. Op echte data
is de lijn vóór 1965 ongeveer in orde of te steil, en na 1963 op alle drie de
verzamelingen te vlak, met GRS-verwerpingen. Of die vlakke lijn een rationele prijs
(Black) of een vergissing is, scheiden de data niet. Dit komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen de lecture na F5-1 (5.495 woorden, `--check` PASS) en de uitvoer in het
notebook. Alleen de eigen punten.

**1. Helderheid**
- "Eerste theorie die zegt wat prijzen zijn": *opgelost* ("de eerste evenwichtstheorie
  van verwachte rendementen in deze reeks").
- ML en Hotelling bij GRS: *opgelost* (ML = delen door $T$; $F$ als eindige-steekproefvorm
  van een $\chi^2$-toets; Hotelling niet meer genoemd).
- Waarom beleggers op de rand zitten (zero-beta): *opgelost* (aanname 1 in de stelling).
- Welke premie bij Frazzini-Pedersen: *opgelost* (lage bèta met hefboom, hoge bèta short).
- GRS zonder getal: *opgelost* (grens 1,52, gevonden 4,20).

**2. Opbouw**
- Simulatie opent zonder conclusie: *opgelost*.
- Twee oordelen: *opgelost* (één blok "Gedeeltelijk geslaagd" met label per periode).
- Rollende Fama-MacBeth: *opgelost* (geschrapt).

**3. Taal**
- Frontier/rand: *opgelost* (overal "rand").
- "vormgaf": *opgelost*.
- value-weighted, size/BM, pre-ranking: *opgelost* (waardegewogen; één keer uitgeschreven;
  pre-ranking uitgelegd).
- Metazin aan het slot van het toy: *opgelost*.

**4. Toy**
- Stap 3 zonder stelsel: *opgelost* (rij C geeft $x_C = 2$, dan $x_B$, $x_A$).

**5. Code en figuren**
- Trucs in `beta_sorted_portfolios`: *opgelost* (`pre_ranking_betas`, benoemde rangorde en
  groepen, dict per groep; de tekst ervoor legt de stappen uit).
- `attrs`-omweg: *opgelost* (met de rollende FM geschrapt).
- `stats` overschaduwt scipy.stats: *opgelost* (`estimates`).
- `sml_table` 9×15: *opgelost* (tabel tot 1965 origineel/hier, tabel na BJS met drie rijen).
- Code-achtige labels: *opgelost* (γ0, γ1, "sd ware bèta, portefeuilles"; de sleutels van
  `sims` blijven intern).

**6. Replicatie**
- Getallen na 1963 in proza: *opgelost* (eigen tabel; het oordeel citeert er alleen uit).
- Twee oordelen: *opgelost*.
- Premieafwijking EW/VW: *opgelost* (in de verwachte afwijking en in het oordeel).
- Tekenverschil $\gamma_0$ 1939–1948: *opgelost* ("niet geslaagd", −0,39 tegen 0,44).

**7. Oefeningen**
- Misleidende simulatiekolommen in oefening 2: *opgelost* (verwijderd).

Nagerekend na de wijziging: tabel tot 1965 en tabel na BJS (γ0 0,79 / 0,38 / 1,16; γ1
−0,07 / 0,28 / −0,37; GRS 2,52 / 2,03 / 4,20, alle $p < 0{,}05$); oordeelsbullets (1948–1965
dalende helling en stijgend intercept; 1939–1948 helling 1,36 boven premie 0,84; premie
0,93/0,84/0,96 onder 1,42/2,20/1,30). Geen verslechteringen, geen nieuwe feitelijke fouten.

| nr | criterium | gewicht | F5a | Controle 1 |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 7 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |

**Eindcijfer: 9,0.** Opmerking: met 5.495 woorden zit de lecture 5 woorden onder de grens
van 5.500; elke toevoeging moet elders worden betaald.
