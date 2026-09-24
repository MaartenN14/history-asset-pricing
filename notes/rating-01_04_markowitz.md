STATUS 01_04_markowitz F5c words=5395 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling: 01_04_markowitz (F5a)

Gelezen als eerstejaars PhD-student die L0 t/m L3 heeft gelezen. Ter controle van de
aansluiting: "Waar we zijn" en "Wat er brak" van 01_03_williams_ddm en 02_05_crsp_tape.
De aansluiting klopt: L3 sluit af met "Markowitz verplaatste de vraag: niet langer wat
één aandeel waard is, maar welke portefeuille", en deze lecture opent met "Williams had
geen theorie van $r$, en hij bekeek elk aandeel apart". Deze lecture verwijst door naar
de CRSP-tape van 1964, en 02_05 opent met "Die theorie strandt op de invoer: verwachte
rendementen zijn slecht meetbaar".

`prose_stats`: 5.432 woorden (onder 5.500, maar krap), gemiddelde zinslengte 14,9, één
zin boven 40 woorden, 8 puntkomma's, één stopwoord, PASS.

## Eindcijfer: 8,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·9 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,35, afgerond 8,4.

## 1. Helderheid van de uitleg: 8

*Goed*
- **Het kernresultaat**: bij bijna elke formule staat het toy-getal ($A = 128{,}125$,
  $D = 15{,}625$ "bijna een kwart van het maximum", $\lambda = 0{,}368$ en
  $\delta = -0{,}0125$ bij 10%, $\sigma = 15{,}6\%$ op de rand). De lezer kan elke stap
  narekenen.
- **Een risicovrij activum**: de tangentportefeuille wordt met de hand uitgerekend
  (1/3; 2/9; 4/9) en de uitkomst krijgt een betekenis ("Activum B heeft het hoogste
  verwachte rendement en krijgt toch maar 22%").
- **Waar het strandt**: de drie redenen zijn genummerd en elk krijgt een getal
  (6,3 procentpunt bij tien jaar; de −6,25 uit het toy; $N/T = 0{,}083$, vier keer de ware
  $S^2_{\max}$).

*Aanmerkingen*
- **Het kernresultaat**: "Let wel: de schuine $A$, $B$, $C$ en $D$ zijn getallen, geen
  activa. De activa staan rechtop: activum A, B en C." De lecture kiest zelf dezelfde
  letters voor activa en scalairen, en de lezer moet daarna op cursief letten
  (bijvoorbeeld "In het toy-voorbeeld is $A = 128{,}125$" direct na "activum A").
- **Replicatie, voorbehoud**: "Het verschil tussen mean-variance en 1/N buiten de
  steekproef is 0,077 bij de industrieën en 0,055 bij de 25 portefeuilles, beide onder
  twee standaardfouten (0,08)." De 0,04 is de standaardfout van één Sharpe-ratio, niet
  van het verschil tussen twee; de lezer krijgt een toets die niet klopt, ook al klopt de
  conclusie.
- **Waar het strandt**: "Bij een risicotolerantie van 50 (de parameter in hun
  mean-variance-nut: hoe hoger, hoe minder variantie weegt)". Het getal 50 heeft geen
  schaal; de lezer weet niet of dat voorzichtig of gewaagd is.

*Beter uitleggen*
- Bij het voorbehoud: één zin dat de standaardfout van een *verschil* van Sharpe-ratio's
  van de correlatie tussen de strategieën afhangt, en dat 0,08 een ruwe drempel is.
- Bij Chopra-Ziemba: één zin wat 50 betekent (bijvoorbeeld welk aandeel aandelen zo'n
  belegger kiest), of het getal weglaten.

*Voor een 9*
- Het kernresultaat: andere letters voor de vier scalairen of voor de activa, zodat de
  "Let wel"-zin vervalt.
- Replicatie, voorbehoud: de drempel als ruwe drempel benoemen of de standaardfout van
  het verschil geven.
- Waar het strandt: de risicotolerantie van 50 een betekenis geven of schrappen.

## 2. Opbouw en rode draad: 9

*Goed*
- **Overzicht**: vraag en antwoord in de eerste alinea, inclusief de wending ("Maar
  $\boldsymbol{\mu}$ is zo slecht te schatten ...") en de winnaar (minimum-variantie).
- **Intuïtie → Theorie**: twee voorspellingen, allebei zichtbaar ingelost ("zoals de
  eerste voorspelling van de intuïtie zei", "Zo lost de theorie de tweede voorspelling van
  de intuïtie in").
- **Dezelfde getallen**: het toy draagt de hele theorie; de simulatie meet 0,50 "dicht bij
  de 0,529 van het toy-voorbeeld" en lijkt op de industrieën uit de replicatie; de
  posities in de replicatie worden teruggekoppeld aan "punt 2 in de theorie". Elke
  subsectie opent met "De bewering:".

*Aanmerkingen*
- **Een risicovrij activum: Tobin en Roy**: de Roy-alinea (Bienaymé-Tsjebysjev, 17%
  tegen 0,8%) is een zijtak die daarna niet meer terugkomt.
- **Replicatie**: na oordeel, voorbehoud, figuur en positietabel volgt nog een tip; de
  sectie is lang voor een lecture op 5.432 woorden.

*Beter uitleggen*
- Niets wezenlijks; de kern is na het Overzicht te benoemen.

## 3. Taal: 8

*Goed*
- Korte zinnen (gemiddeld 14,9 woorden), geen u/je, geen calques.
- Beeldend waar het helpt: "Wie op geschatte gemiddelden jaagt, jaagt op ruis", "hier zit
  hefboom op een schattingsfout".
- Vaste namen worden vastgehouden: "efficiënte rand", "tangentportefeuille", "1/N".

*Aanmerkingen*
- **Overzicht**: "Dit werk definieert het tijdvak omdat het de vraag verplaatst".
  Projecttaal, dezelfde als in L2 en L3.
- **Replicatie**: Engels en jargon stapelen zich op: "mean-variance-portefeuille",
  "size/BM", "long positie", "short verkopen", "FF-vierfactordataset". Elk is uitgelegd of
  gangbaar, maar samen maken ze de replicatie minder Nederlands dan de theorie.
- **Replicatie-admonition**: "Hun FF-vierfactordataset (24 reeksen van de French-website,
  vanaf juli 1963) komt qua bron, begin en aantal reeksen het dichtst bij onze 25
  portefeuilles." Tussenvoeging plus opsomming in één zin.

*Voor een 9*
- Overzicht: "definieert het tijdvak" vervangen door wat er gebeurt.
- Replicatie: waar het kan een Nederlandse naam ("gemiddelde-variantieportefeuille" of
  vaker "de geoptimaliseerde portefeuille"; "lange/korte positie").
- Replicatie-admonition: de zin over de FF-vierfactordataset splitsen.

## 4. Toy-voorbeeld: 9

*Goed*
- Eén mechanisme (een mengsel is veiliger dan het veiligste activum), in vijf stappen
  met hand en code; de blokstructuur van $\boldsymbol{\Sigma}$ maakt de inverse met de
  hand haalbaar.
- Eén nog niet afgeleide formule (het recept $\boldsymbol{\Sigma}^{-1}\mathbf{1}$), als
  zodanig aangekondigd.
- Stap 5 laat zien dat elke covariantie met de portefeuille gelijk is (0,32/41), wat de
  theorie later als eerste-ordevoorwaarde terugziet.

*Aanmerkingen*
- De $2\times2$-inverse en de rijsommen maken het toy aan de lange kant van vijf minuten.
  Klein.

## 5. Code en figuren: 8

*Goed*
- Toy- en theoriecellen zetten hand en code naast elkaar in één tabel; commentaar
  verwijst naar stap en vergelijking (`# stap 3`, `# eq-markowitz-tangent`).
- `rolling_oos` toont de rollende schatting als zichtbare lus met "alleen maanden vóór
  $t$".
- Vóór elke figuur staat waarop te letten; het bijschrift bij de simulatiefiguur legt de
  bias uit ("de optimalisator kiest de gewichten juist waar de schattingsfout het
  gemiddelde toevallig hoog maakte").

*Aanmerkingen*
- **Simulatie, `draw_moments` en `tangency`**: `rng.standard_normal((n_sim, T, n_assets))
  @ chol.T`, `demeaned.transpose(0, 2, 1) @ demeaned`, `mu_hat[..., None])[..., 0]` en
  `np.broadcast_to` zijn gevectoriseerde trucs; de wiskunde (trek, schat, optimaliseer)
  zit erachter verstopt.
- **Simulatie, `oos_sharpe`**: `((w @ Sigma_true) * w).sum(axis=1)` voor
  $\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}$ per rij; het commentaar helpt, de vorm niet.
- **Simulatietabel**: kolomnamen "alleen Sigma geschat", "alleen mu geschat" in
  code-notatie.
- **Oefening 3, uitwerking**: de codecel staat zonder zin ervoor.

*Voor een 9*
- Simulatie: één steekproef per lusiteratie (of een benoemde hulpfunctie per
  steekproef), zodat trekken, schatten en optimaliseren als drie regels leesbaar zijn.
- Simulatietabel: "alleen $\boldsymbol{\Sigma}$ geschat" en "alleen $\boldsymbol{\mu}$
  geschat" in woorden ("covariantie geschat", "gemiddelden geschat").

## 6. Replicatie en empirie: 8

*Goed*
- Admonition compleet; de verwachte afwijking is scherp ("Het niveau wijkt af, de
  ordening niet") en noemt de standaardfout vooraf (0,04), zodat "alleen teken en ordening
  zijn informatief" een eerlijke verwachting is.
- Oordeel begint met "**Geslaagd.**" en koppelt aan die ordening; tabel origineel/hier met
  de DGU-rij ertussen.
- De positietabel verklaart het falen met het mechanisme uit de theorie in plaats van met
  een bewering.

*Aanmerkingen*
- **Oordeel en voorbehoud**: "0,10 bij de industrieën, 0,30 bij de 25 portefeuilles. DGU
  vinden 0,54 ... 0,077 bij de industrieën en 0,055 ... (0,08) ... 0,165 bij de
  industrieën en 0,239 ... 0,158 per maand voor 1/N is 0,55 per jaar." Negen getallen in
  drie alinea's, bijna alle al in de tabellen.
- **Posities**: "tot ruim 2100% long ... ruim 2100% short ... 7,5 maal ... meer dan
  honderdduizend procent ... 72 maal" herhaalt de positietabel.
- **Voorbehoud**: de drempel "twee standaardfouten (0,08)" is de standaardfout van één
  Sharpe-ratio, niet van het verschil (zie criterium 1).

*Voor een 9*
- Oordeel, voorbehoud en posities: naar de tabellen verwijzen, hoogstens het gat
  (0,10 tegen 0,30) in de tekst.
- Voorbehoud: de drempel correct benoemen.

## 7. Oefeningen: 9

*Goed*
- Instap varieert het toy (correlatie A-B op nul) met hand- en codecontrole.
- Oefening 1 is een afleiding (covariantie op de rand, zero-beta-rendement = 2%), met een
  verklaring waarom dat geen toeval is en een brug naar Black (1972).
- Oefening 3 breidt de replicatie uit (krimpen) en eindigt met een scherpe les ("hoeveel
  hij hem *niet* moet geloven").

*Aanmerkingen*
- Geen die het cijfer drukken.

## De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9)**: andere letters voor de scalairen $A$–$D$ of de activa, de
   drempel "twee standaardfouten (0,08)" correct benoemen, en de risicotolerantie van 50
   een betekenis geven. Eindcijfer +0,3.
2. **Taal (8 → 9)**: "definieert het tijdvak" weg, minder Engels in de replicatie, de
   FF-zin in de admonition splitsen. Eindcijfer +0,15.
3. **Replicatie (8 → 9)**: de getallen in oordeel, voorbehoud en positie-alinea naar de
   tabellen. Eindcijfer +0,1.

## Navertelling in vijf zinnen

Markowitz liet zien dat het risico van een activum zijn covariantie met de portefeuille is,
zodat een mengsel veiliger kan zijn dan het veiligste activum. De efficiënte rand is een
parabool en elke portefeuille erop is een mengsel van twee fondsen; met Tobins
risicovrije activum houdt iedereen dezelfde tangentportefeuille en verschilt alleen de
dosis. In een grote portefeuille blijft alleen covariantie over, dus eigen risico hoeft
niet beloond te worden. In de praktijk moet $\boldsymbol{\mu}$ geschat worden, en die
schattingsfout, versterkt door $\boldsymbol{\Sigma}^{-1}$, maakt de geoptimaliseerde
portefeuille slechter dan 1/N, in simulatie en op French-data. De
minimum-variantieportefeuille, die $\boldsymbol{\mu}$ niet gebruikt, doet het het best.

Dit komt overeen met het Overzicht.

## Feitelijke fouten

Nagerekend met `uv run python` op `hap.data`, met dezelfde toevalsgenerator in dezelfde
volgorde als de lecture. Kloppen: toy (determinant 0,0032; inverse; rijsommen 21,875 /
6,25 / 100; gewichten 7/41, 2/41, 32/41; 0,32/41; 8,83%), $A$–$D$ (128,125; 7,0625;
0,51125; 15,625; $AC = 65{,}5$), $\lambda$ en $\delta$ bij 10% (0,368; −0,0125; 0,0243;
15,6%), $B/A = 5{,}51\%$, $C/B = 7{,}24\%$, fondsen (0,274; 0,159; 0,566), tangent
(1,5 / 1,0 / 2,0; 1/3, 2/9, 4/9; $S_{\max} = 0{,}529$; 8,22%; 11,76%), Roy (2,4; 17%;
0,8%), 1/N-bodem (19,0% en 9,5%), $20/\sqrt{10} = 6{,}3$, $N/T = 0{,}083$ tegen 0,021,
simulatie (0,503 en 0,472; medianen 0,16 bij 60 en 0,39 bij 600 maanden, altijd onder
1/N), replicatie (757 en 637 maanden; SE 0,04; 1/N 0,158 en 0,159; mean-variance 0,081 en
0,104; minimum-variantie 0,165 en 0,239; in de steekproef 0,185 en 0,402; gaten 0,10 en
0,30; standaarddeviatie mean-variance 3,3 keer die van 1/N; posities +2103% / −2122%,
brutopositie 7,5; bij 25: +115 800%, brutopositie 72, omzet 72), $0{,}158\sqrt{12} =
0{,}55$, instap (9/49, 4/49, 36/49; 8,57%), oefening 1 ($\mu_z = 0{,}0200$), oefening 3
($\phi = 1$: 0,104 en 72; $\phi = 0$: 0,239).

Geen feitelijke fouten gevonden.

Geen fout maar het noemen waard:
- **Replicatie, voorbehoud**: "twee standaardfouten (0,08)" gebruikt de standaardfout van
  één Sharpe-ratio als die van een verschil (zie criterium 1).
- **Bijschrift simulatiefiguur**: "meestal onder 1/N". Nagerekend ligt bij $T = 120$ de
  geleverde Sharpe-ratio in alle 2000 steekproeven onder 1/N; "meestal" onderschat het
  resultaat.

Niet nagegaan: de DGU-getallen uit tabel 3 (0,1753; 0,5364; −0,0031) en de
Chopra-Ziemba-verhoudingen (11 en 21), die niet in de repository staan.

## Controle 1

Alleen de eigen punten nagekeken, op de huidige `lectures/01_04_markowitz.md`, met
§F5-1 van `notes/rapport-01_04_markowitz.md` als wegwijzer. `prose_stats`: 5.395 woorden,
geen zin boven 40 woorden, PASS.

| crit. | punt | status | vindplaats nu |
|---|---|---|---|
| 1 | dezelfde letters voor activa en voor de scalairen $A$–$D$ | opgelost | de activa heten nu aandelen, kleine aandelen en obligaties (toy-tabel, theorie, figuur, oefeningen); de "Let wel"-zin is weg |
| 1/6 | drempel "twee standaardfouten (0,08)" | opgelost | Replicatie, voorbehoud: "kleiner dan twee keer de standaardfout van één Sharpe-ratio. Dat is een ruwe drempel: de standaardfout van een verschil hangt af van hoe sterk de twee strategieën samen bewegen." |
| 1 | risicotolerantie van 50 zonder betekenis | deels | nu met richting ("Hoe hoger de risicotolerantie, hoe minder variantie weegt ... hoe duurder een fout daarin is"); het getal 50 heeft nog geen schaal |
| 2 | Roy-alinea als zijtak; lange replicatie | niet / deels | Roy ongewijzigd; de tip is ingekort en de positie-alinea is korter. Dit waren aanmerkingen bij een 9 en ze drukken het cijfer niet |
| 3 | "definieert het tijdvak" | opgelost | "Dit werk verplaatste de vraag" |
| 3 | Engels en jargon in de replicatie | deels | "long/short" is vervangen door "grootste positieve/negatieve gewicht" en "negatieve gewichten verbieden"; "mean-variance(-portefeuille)" blijft als vaste naam, en is in het Overzicht ingevoerd |
| 3 | FF-zin in de admonition | opgelost | in twee zinnen gesplitst |
| 5 | gevectoriseerde trucs in de simulatie | opgelost | `one_sample(T)`, `tangency` en een zichtbare lus per steekproef ("trekken en schatten", "optimaliseren"); `sharpe_true` leest als $\sqrt{12}\,\mathbf{w}'\boldsymbol{\mu}/\sqrt{\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}}$ |
| 5 | kolomnamen "alleen Sigma/mu geschat" | opgelost | "alleen covarianties geschat", "alleen gemiddelden geschat", "gemiddelden en covarianties geschat" |
| 5 | oefening 3: codecel zonder zin ervoor | opgelost | er staat nu een inleidende zin vóór de cel |
| 6 | getallen in oordeel, voorbehoud en positie-alinea | opgelost | het oordeel noemt alleen het gat (0,10 naar 0,30) en verwijst naar kolommen; de positie-alinea zonder getallen ("meer dan twintig maal het vermogen") |
| — | bijschrift "meestal onder 1/N" (geen fout, wel genoemd) | opgelost | "in deze figuur ook onder 1/N" |

Nagerekend, omdat de simulatiecode is herschreven: de nieuwe lus trekt de toevalsgetallen
in dezelfde volgorde en geeft dezelfde uitkomsten (medianen 0,161 / 0,231 / 0,301 / 0,388;
in de figuur ligt de geleverde Sharpe-ratio in 100% van de steekproeven onder 1/N en onder
het ware optimum). Geen verslechteringen en geen nieuwe feitelijke fouten.

### Deelcijfers na controle 1

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |

**Eindcijfer: 9,0** (was 8,4). Laagste deelcijfer 9. Open feitelijke fouten: 0.
