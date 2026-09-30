STATUS 04_18_fama_french F6c words=5936 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,5 -> F6c 9,0.

# Eindbeoordeling 04_18_fama_french

## Eerste herziening (workflow §12)

Eerste herziening van dit college; er is geen vorig cijfer. Gelezen: de .md volledig,
celuitvoer via `tools/nb_outputs.py`, `notes/taal-04_18_fama_french.md`.
`prose_stats --check`: PASS (5651 woorden, zinnen gemiddeld 16,9, geen zin > 40,
dubbele punt 0,9 per 1000, drie alinea's van één zin, één "Wie"-zin).

## De drie verbeteringen met het meeste effect

1. **Maak "goede fit" eenduidig en herstel de slotzin van het toy-voorbeeld.** De
   propositie over de mechanische fit gaat over de *cross-sectionele* $R^2$ met vrije
   premies, en de simulatie laat zien dat GRS (premies vast) 98% van de nepmodellen
   verwerpt. Toch zegt de toy-slotzin (04_18_fama_french.md:221-223) dat die propositie
   gaat over "een kleine alpha", zegt het Overzicht (r. 45) "factoren uit dezelfde
   sortering verklaren de sorteringen bijna vanzelf" en zegt Wat er brak (r. 1156) "op 25
   sorteringen is een kleine alpha deels constructie". Die laatste bewering steunt alleen
   op het raster-argument van r. 456-458, niet op de propositie of de simulatie. Eén naam
   per soort fit (cross-sectionele $R^2$ tegenover tijdreeks-alpha) en de toy-zin laten
   verwijzen naar wat het toy wél laat zien (met $T = K$ past elke portefeuille perfect).
   Verwacht: helderheid 9,0, opbouw 9,0, toy 8,5.
2. **Toy: één mechanisme en een juiste les.** Stap 4-5 gebruiken drie maanden
   factorrealisaties die niets met de zes aandelen te maken hebben; het toy heeft daardoor
   twee mechanismen (constructie en regressie). Ofwel stap 4-5 bouwen op de toy-factoren
   (bijvoorbeeld de maand uit stap 1-3 als eerste waarneming), ofwel de slotzin maakt
   expliciet dat stap 5 alleen het vrijheidsgradenpunt illustreert (r. 157-175, 221-223).
   Verwacht: toy 9,0.
3. **Herstel de feitelijke en notationele slordigheden.** $\ell_i$ voor de lading botst
   met de vaste notatie ($\ell = \log R$, 00_00_setup.md:228), r. 470-521 en oefening 2;
   het causale "omdat" bij klein-groei (r. 930); de transpositie $\boldsymbol{\mu}_H =
   \rho\mathbf{Z}_H'\boldsymbol{\lambda}$ in de uitwerking van oefening 2 (r. 1237) en
   `np.linalg.solve(H_loadings.T, ...)` in de cel (r. 1253), dat $\mathbf{L}_H^{-\top}$
   gebruikt waar de afleiding $\mathbf{L}_H^{-1}$ geeft. Verwacht: helderheid 9,0, code
   en figuren 9,0, oefeningen 9,0.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,5

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 8,5 |
| | **Eindcijfer** (8,45 afgerond) | | **8,5** |

Niet klaar: eindcijfer onder 9,0 en toy (8,0) onder 8,5. Taal blokkeert niet.

### 1. Helderheid (8,5)

*Goed.* De koers als thermometer van het verwachte rendement (Intuïtie, r. 75-79) is een
voorspellende uitleg met richting. Het theorema over nul alpha's, een lineaire SDF en de
Sharpe-ratio (Theorie, "Het driefactormodel als bèta- en als SDF-model") heeft een
economisch waarom vóór de formule en een kort, correct bewijs. De Daniel-Titman-sectie
zegt vooraf welke portefeuille de werelden scheidt en waarom.

*Aanmerkingen.*
- Toy-voorbeeld, r. 221-223: "De alpha van nul uit stap 5 is de kleinste versie van
  {prf:ref}`prop-fama-french-mechanisch` hieronder, die zegt dat een kleine alpha minder
  bewijst naarmate de factoren de testportefeuilles beter opspannen." De propositie gaat
  over de cross-sectionele $R^2$ met vrije premies, niet over tijdreeks-alpha's.
- Theorie, "Kenmerken of covarianties", r. 470-472: "De lading op een factor $f$ met
  gemiddelde nul is $\ell_i$". $\ell$ is in de reeks het log rendement (H7, notatie §3).
- Theorie, SDF, r. 371-373: "De SDF in [](#eq-fama-french-sdf) is laag in maanden waarin
  de factoren boven hun gemiddelde uitkomen. Een factor weegt daarin zwaarder naarmate zijn
  premie per eenheid variantie hoger is." Dat klopt alleen als $\mathbf{b}$ positief is en
  $\boldsymbol{\Sigma}_f$ diagonaal; met gecorreleerde factoren telt de combinatie
  $\mathbf{b}'\mathbf{f}$.
- Replicatie, r. 930: "Klein-groei heeft een alpha van $-0{,}47\%$ per maand
  ($t = -5{,}09$), omdat de standaardfout krimpt met de wortel van de steekproefomvang."
  De standaardfout verklaart de $t$-waarde, niet de alpha.

*Beter uitleggen.* De lezer moet weten welke "fit" er in elke sectie bedoeld is: de
cross-sectionele $R^2$ met vrije premies (die de propositie ontkracht) of de tijdreeks-alpha
met vaste premies (die GRS toetst en die in de simulatie wél onderscheid maakt). Bij het
theorema ontbreekt een getal: hoe groot is $S_f$ tegenover de Sharpe-ratio van de markt op
de steekproef van Fama en French (H4)?

*Voor een 9.* Toy-slotzin herschrijven (04_18_fama_french.md:221-223); één naam per soort
fit door Overzicht (r. 45), Theorie-inleiding (r. 229-231) en Wat er brak (r. 1156); ander
symbool voor de lading (r. 470-521, 1214-1242); r. 371-373 in termen van
$\mathbf{b}'\mathbf{f}$; r. 930 het verband omzetten.

### 2. Opbouw en rode draad (8,5)

*Goed.* Overzicht stelt de vraag en geeft het antwoord met getallen (een kwart naar een
tiende procent). Routekaart aan het begin van Theorie en Samengevat aan het eind. De
voorspelling uit de Intuïtie (r. 93-95) wordt in de Daniel-Titman-sectie (r. 540-542) en
bij GRS (r. 394-395) ingelost, en de simulatie volgt precies de twee zwaktes. 5651 woorden.

*Aanmerkingen.*
- Overzicht, r. 45-46: "bewijzen we dat factoren uit dezelfde sortering de sorteringen
  bijna vanzelf verklaren". De propositie gaat over willekeurige factoren $\mathbf{g}$ en
  niet over de sortering; het sorteringsargument staat pas in r. 456-458.
- Wat er brak, r. 1155-1156: "Daaronder ligt de zwakte uit de simulatie, want op 25
  sorteringen is een kleine alpha deels constructie." De simulatie liet het omgekeerde zien
  voor de tijdreekstoets: GRS verwerpt 98% van de nepmodellen.

*Beter uitleggen.* De rode draad "een goede fit bewijst weinig" heeft twee takken (mechanische
cross-sectionele fit; kenmerk tegenover covariantie). De tweede tak geldt voor tijdreeks-
alpha's, de eerste niet. Eén zin in de Theorie-routekaart die dat onderscheid maakt, draagt
de hele lecture.

*Voor een 9.* Overzicht r. 45-46 en Wat er brak r. 1155-1156 laten zeggen wat propositie en
simulatie werkelijk tonen; zie verbetering 1.

### 3. Taal (8,5)

*Goed.* De redactie heeft de calques en telegramzinnen weggewerkt; de meeste alinea's lezen
als gesproken Nederlands (bijvoorbeeld Simulatie, r. 715-719: "De toets doet dus wat hij
moet doen, en juist daarom scheidt hij de werelden niet."). Motiefnamen elk hoogstens twee
keer, één "Wie"-zin, geen u/je. Geen vakterm van betekenis veranderd: "efficiënte grens" en
"minimum-variantierand" komen niet voor, en "elke efficiënte index" bij Roll (r. 859-860)
is juist.

*Aanmerkingen.*
- Replicatie, r. 930 (zie helderheid): het verkeerde "omdat".
- Intuïtie, r. 75: "Dat verhoudingen met de koers winnen, ligt voor de hand zodra we
  bedenken wat een koers is." "Verhoudingen met de koers" is vaag voor kenmerken met de
  koers in de noemer.
- Replicatie, r. 1075-1076: "Voor factorpremies geldt [de standaardfout van 2%] dus in
  maandvorm." "In maandvorm" zegt niet wat het motief hier betekent.
- Wat er brak, r. 1169-1171: "Wie in 1993 een waardefonds kocht, werd betaald voor risico
  of wist iets wat de prijs niet wist, en de data kunnen dat niet beslissen." De prijs die
  iets weet, is een beeld dat hardop stroef klinkt.

*Beter uitleggen.* Geen inhoudelijk tekort; zie de hardop-toets hieronder.

*Voor een 9.* De drie zinnen van de hardop-toets herschrijven (r. 75, 930, 1169-1171) en
r. 1075-1076 laten zeggen dat één decennium een standaardfout heeft van ongeveer even groot
als de premie.

### 4. Toy-voorbeeld (8,0)

*Goed.* Met de hand na te rekenen in vijf minuten; de breekpunten met lineaire interpolatie
kloppen met `np.percentile`; tabel hand/code met tien regels die precies gelijk zijn. De
toy-getallen keren terug in Theorie (aandeel C is 1% van de marktwaarde, r. 258-259) en in
oefening 1.

*Aanmerkingen.*
- Toy-voorbeeld, r. 157-158: "Voor de regressie nemen we drie maanden factorrealisaties en
  het overrendement van één portefeuille." De drie maanden staan los van de zes aandelen;
  het toy heeft daardoor twee mechanismen.
- Toy-voorbeeld, r. 221-223: de slotzin koppelt de alpha van nul aan de verkeerde
  propositie (zie helderheid).

*Beter uitleggen.* Wat het toy leert, is dat de constructie elke doorsnede even zwaar weegt
(C is 1% van de markt en een derde van SMB) en dat met $T = K$ elke alpha nul is. De slotzin
moet één van die twee lessen noemen, niet een stelling over cross-sectionele fit.

*Voor een 9.* Stap 4-5 laten aansluiten op de toy-factoren of expliciet als tweede, los
voorbeeld aankondigen; slotzin herschrijven (04_18_fama_french.md:157-158, 221-223).

### 5. Code en figuren (8,5)

*Goed.* Elke cel heeft een zin ervoor en erna; `ff_factors` leest als vergelijking
[](#eq-fama-french-factoren); de figuren hebben een leeswijzer vooraf ("links liggen ...
over elkaar, terwijl rechts ...", r. 717-719) en een bijschrift dat de conclusie geeft.

*Aanmerkingen.*
- Simulatie, r. 625-626: `size_q, value_q = groups(...), groups(...)` en
  `small, value_3 = groups(...) == 1, groups(...)` op één regel; compact en moeilijk te
  lezen.
- Simulatie, r. 643-644: de eigenwaardewortel `noise_root` staat zonder zin die zegt dat
  dit een matrixwortel van $\sigma_\varepsilon^2\mathbf{W}\mathbf{W}'$ is.
- Oefening 2, r. 1253: `dt_loading @ np.linalg.solve(H_loadings.T, expected["kenmerkwereld"][26:28])`
  rekent $\boldsymbol{\ell}_w'\mathbf{L}_H^{-\top}\boldsymbol{\mu}_H$, terwijl de afleiding
  $\boldsymbol{\ell}_w'\mathbf{L}_H^{-1}\boldsymbol{\mu}_H$ geeft. Numeriek verwaarloosbaar
  (buitendiagonaal $-0{,}047$ en $-0{,}046$), maar code en wiskunde lopen uiteen.
- Replicatie, r. 1012-1014: de list comprehension met `np.broadcast_to` en een
  voorwaardelijke expressie is een truc waar de wiskunde één regel is.

*Beter uitleggen.* Eén zin bij `noise_root` dat alle 29 portefeuilles dezelfde aandelen
delen en dus gecorreleerde ruis hebben (staat in r. 608-610, maar niet bij de regel zelf).

*Voor een 9.* r. 625-626 uitschrijven; r. 1253 `np.linalg.solve(H_loadings, ...)`
gebruiken; r. 1012-1014 splitsen in twee benoemde stappen.

### 6. Replicatie en empirie (8,5)

*Goed.* Admonition compleet en kort (bron, wat, data, verschil, verwachte afwijking). Twee
tabellen origineel/hier; het oordeel voor tabel 9a begint met "De replicatie is geslaagd"
en verwijst naar de verwachte 0,05 (r. 985-986). De decennia-analyse maakt de standaardfout
zichtbaar met foutbalken.

*Aanmerkingen.*
- Replicatie, r. 1061-1063: "Wat de tekens betreft is de replicatie geslaagd. Naast grootte
  en B/M is bèta insignificant, B/M is significant positief en grootte negatief, maar
  zwakker dan in het origineel." Grootte is naast B/M niet significant ($t = -1{,}38$) en de
  hellingen zijn half zo groot; dat is gedeeltelijk geslaagd, en de verwachte afwijking
  (r. 885-887) noemde die halvering niet.
- Replicatie, tabel bij r. 1051-1059: de rij met bèta, log ME en log B/M samen ontbreekt,
  terwijl "bèta insignificant naast grootte en B/M" precies op die rij steunt ($-0{,}11$,
  $t = -0{,}30$ in de celuitvoer).
- Replicatie, r. 929-932: vier getallen in lopende tekst die ook in de tabel staan.

*Beter uitleggen.* De verwachte afwijking voor tabel III moet de kleinere hellingen door
portefeuilles in plaats van aandelen al noemen, zodat het oordeel ernaar kan verwijzen.

*Voor een 9.* Oordeel tabel III als "Gedeeltelijk geslaagd" met verwijzing naar de
verwachte afwijking (r. 885-887, 1061-1065); rij met drie regressoren toevoegen aan de tabel
(r. 1051-1059).

### 7. Oefeningen (8,5)

*Goed.* Instap (oefening 1) is een variatie op het toy, afleiding (oefening 2) veralgemeent
de propositie, uitbreiding (oefening 3) zet momentum tegen het model. Elke uitwerking eindigt
met een les.

*Aanmerkingen.*
- Oefening 2, r. 1236-1238: "$\boldsymbol{\mu}_H = \rho\mathbf{Z}_H'\boldsymbol{\lambda}$ met
  $\mathbf{L}_H = \rho\mathbf{Z}_H$". Met portefeuilles in de rijen van $\mathbf{L}_H$ is
  het $\rho\mathbf{Z}_H\boldsymbol{\lambda}$; met het accent volgt
  $\mathbf{L}_H^{-1}\boldsymbol{\mu}_H = \boldsymbol{\lambda}$ niet.
- Oefening 2, r. 1220: "$\boldsymbol{\alpha}_w^{\text{kenmerk}}$" vet voor een scalair.

*Beter uitleggen.* In oefening 2 zeggen of de rijen van $\mathbf{L}_H$ en $\mathbf{Z}_H$ de
portefeuilles of de factoren zijn.

*Voor een 9.* Transpositie herstellen (04_18_fama_french.md:1237) en de code in r. 1253 er
gelijk aan maken; scalaire alpha niet vet (r. 1220).

## Feitelijke fouten

Nagerekend tegen de celuitvoer (`$TEMP/F6-04_18_fama_french-out.txt`). Alle getallen in de
proza kloppen met de cellen: toy (breekpunten 0,55 en 1,0; SMB 1,333; HML 2,5; markt 1,50;
ladingen 1, 1, 0,5), simulatie (0,19 en 38%; 0,05 en 6,8/8,8%; DT 0,71/0,09, 0,13/0,01,
$-0{,}11$ en 95%, voorspeld $-0{,}12$; $R^2$ 0,86/0,83, $p = 0{,}12$, factor 16, 98%),
replicatie (0,26 naar 0,09; GRS 1,43/$p = 0{,}086$ en 1,99; $-0{,}47$/$-5{,}09$; $F = 3{,}63$;
verschil 0,033/0,045; alle zeven hier-waarden van tabel III; HML vóór 1963 $t = 2{,}17$;
SMB na 1993 0,04/$t = 0{,}25$), oefeningen (2,333/4,0/1,53; 0,26 tegen 0,65; 0,85, 1,00,
$t = 5{,}56$, HML-lading $-0{,}24$). Het theorema, beide proposities en hun bewijzen zijn
correct.

1. **r. 221-223 (onjuist).** De propositie wordt verkeerd weergegeven: ze gaat over de
   cross-sectionele $R^2$ met vrije premies, niet over "een kleine alpha".
2. **r. 930 (onjuist verband).** De alpha van $-0{,}47\%$ komt niet door de krimpende
   standaardfout; de $t$-waarde wel.
3. **r. 1237 (onjuist).** $\boldsymbol{\mu}_H = \rho\mathbf{Z}_H'\boldsymbol{\lambda}$ moet
   $\rho\mathbf{Z}_H\boldsymbol{\lambda}$ zijn.
4. **r. 1253 (onjuist, numeriek verwaarloosbaar).** `solve(H_loadings.T, ...)` in plaats
   van `solve(H_loadings, ...)`; de uitkomst $-0{,}1177$ verandert hooguit in de vierde
   decimaal.
5. **r. 1166-1167 (onzeker).** "Beide lezingen verklaren hetzelfde feit, dat de winstgroei
   sneller naar het gemiddelde terugkeert dan de koersen verwachten." "Dan de koersen
   verwachten" is de Yale-lezing; in de Chicago-lezing verwachten koersen niets verkeerd.
   Het gedeelde feit is de hogere gemiddelde opbrengst van kleine en waardeaandelen met
   zwakke winsten.

Geen vakterm van betekenis veranderd door de taalredactie.

## Navertelling in vijf zinnen

Fama en French lieten in 1992 met Fama-MacBeth-regressies zien dat grootte en B/M de
spreiding in gemiddelde rendementen verklaren en bèta niet. In 1993 bouwden ze daaruit SMB en
HML, en een tijdreeksregressie op markt, SMB en HML is precies een toets op een lineaire SDF
in die drie factoren, met GRS als toets op alle alpha's tegelijk. Op de 25 size/BM-
portefeuilles krimpen de prijsfouten van 0,26 naar 0,09% per maand en verwerpt GRS het model
niet, maar een goede cross-sectionele fit bewijst weinig, omdat elke gecorreleerde factor met
vrije premies dezelfde fit geeft. Bovendien kan een beloond kenmerk er op gesorteerde
portefeuilles uitzien als een beloonde covariantie, en alleen een portefeuille die lading en
kenmerk loskoppelt (Daniel en Titman) kan dat scheiden. Tot 2026 wordt het model verworpen
door klein-groei, is SMB na publicatie verdwenen en blijft momentum onverklaard, terwijl de
vraag risico of vergissing open blijft.

Dit wijkt af van het Overzicht op één punt: het Overzicht belooft dat factoren uit
dezelfde sortering de sorteringen "bijna vanzelf" verklaren, terwijl de lecture dat bewijst
voor de cross-sectionele $R^2$ en niet voor de tijdreeks-alpha.

## Taal na de redactie

De redactie heeft haar werk gedaan: geen telegramzinnen meer, verband met voegwoorden,
verwijswoorden eenduidig, geen calques. In de bronregel staan nog enkele losgeraakte
woorden op een eigen regel (r. 274, 325, 536, 823, 995, 1062, 1069, 1144-1146, 1170); dat is
onzichtbaar in de gerenderde tekst maar maakt de .md slordig.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 75: "Dat verhoudingen met de koers winnen, ligt voor de hand zodra we bedenken wat een
   koers is." Herschrijving: "Dat juist kenmerken met de koers in de noemer winnen, ligt
   voor de hand zodra we bedenken wat een koers is."
2. r. 930: "Klein-groei heeft een alpha van −0,47% per maand (t = −5,09), omdat de
   standaardfout krimpt met de wortel van de steekproefomvang." Herschrijving: "Klein-groei
   heeft een alpha van −0,47% per maand, en omdat de standaardfout krimpt met de wortel van
   de steekproefomvang, is de t-waarde nu −5,09."
3. r. 1169-1171: "Wie in 1993 een waardefonds kocht, werd betaald voor risico of wist iets
   wat de prijs niet wist, en de data kunnen dat niet beslissen." Herschrijving: "Een
   belegger die in 1993 een waardefonds kocht, werd betaald voor risico of profiteerde van
   de vergissing van anderen, en de data kunnen niet zeggen welk van de twee."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Gelezen: plannen/kaart-rollen.md (§4,5,6,8), dit bestand volledig, R9-1 in
notes/rapport-04_18_fama_french.md, de .md volledig, en `nb_outputs.py` tegen
`$TEMP/F6c-04_18_fama_french-out.txt`. `prose_stats --check`: PASS (5936 woorden,
zinnen gemiddeld 17,2, geen zin > 40).

**Drie verbeteringen.**
1. Toy-slotzin (nu r. 222-226) noemt de twee echte lessen (C is 1% van de markt en een derde
   van de kleine kant van SMB; met $T=K$ is elke alpha nul), niet meer de verkeerde
   propositie. Overzicht (r. 42-47), Theorie-routekaart (r. 230-237) en Wat er brak
   (r. 1172-1174) noemen nu allebei de cross-sectionele $R^2$ met vrije premies en de
   tijdreeks-alpha met vaste premies, en Wat er brak zegt de simulatie-uitkomst juist. Opgelost.
2. Stap 4-5 (r. 156-159) expliciet aangekondigd als los tweede voorbeeld dat alleen het
   vrijheidsgradenpunt toont. Opgelost.
3. Notatie $\ell_i \to \beta_i$ door Theorie, Daniel-Titman en oefening 2 (r. 478-529,
   1249-1262), consistent met de bestaande $\beta$-notatie voor ladingen. Scalaire alpha in
   de propositie niet meer vet; in oefening 2 vet voor de vectorversie. $\mu_H =
   \rho\mathbf{Z}_H\boldsymbol{\lambda}$ met $\mathbf{B}_H = \rho\mathbf{Z}_H$ (r. 1256-1259)
   geeft nu correct $\mathbf{B}_H^{-1}\boldsymbol{\mu}_H = \boldsymbol{\lambda}$; nagerekend,
   klopt algebraïsch. `solve(H_loadings, ...)` (r. 1273) zonder `.T`. Opgelost.

**Feitelijke fouten (5).** (1) r. 221-223 propositie: opgelost, zie boven. (2) r. 930 "omdat":
nu r. 941-942, verband omgezet zoals voorgesteld. Opgelost. (3) r. 1237 transpositie: opgelost,
zie boven. (4) r. 1253 `.T`: opgelost; cel-uitvoer bevestigt $-0{,}1176$ (was $-0{,}1177$),
tekst noemt $-0{,}12\%$, klopt. (5) r. 1166-1167 Yale/Chicago: nu r. 1184-1185, "de hogere
gemiddelde opbrengst van kleine en waardeaandelen met zwakke winsten" als gedeeld feit.
Opgelost. Geen nieuwe feitelijke fout gevonden; nb_outputs-cijfers (tabel III rij bèta+ME+B/M
$-0{,}11$/$-0{,}30$, $-0{,}07$/$-1{,}73$, $0{,}24$/$2{,}74$; GRS 1,43/$p=0{,}086$ en 1,99/
$p=0{,}004$; oefening 2 $-0{,}1216$/$-0{,}1176$/$-0{,}1114$) kloppen alle met de tekst.

**Voor een 9, per criterium.** Helderheid: alle vijf punten opgelost (toy-slotzin, één naam
per fit, ander symbool, $\mathbf{b}'\mathbf{f}$ met correctie voor samenhang in r. 375-379,
r. 930-verband). Opbouw: Overzicht en Wat er brak opgelost. Taal: de drie hardop-zinnen
(r. 76, 941-942, 1187-1189) letterlijk volgens de voorstellen herschreven; r. 1090-1094
noemt nu de standaardfout per decennium ongeveer even groot als de premie. Toy: stap 4-5
aangekondigd, slotzin herschreven. Code en figuren: r. 632-635 uitgeschreven, r. 1273 `.T`
weg, r. 1022-1026 `as_panel` als benoemde stap. Replicatie: oordeel tabel III nu "gedeeltelijk
geslaagd" (r. 1079) met verwijzing naar de kleinere hellingen, rij bèta+log ME+log B/M
toegevoegd (r. 1075-1077). Oefeningen: transpositie hersteld, code gelijk, scalaire alpha niet
vet. Alle "Voor een 9"-punten van alle zeven criteria: opgelost.

**Aanmerkingen zonder "voor een 9".** $S_f$ tegenover de Sharpe-ratio van de markt (helderheid,
alleen "Beter uitleggen"): terecht afgewezen, geen cel of bron levert het. r. 929-932 (vier
getallen in lopende tekst, replicatie): geen "voor een 9"-punt, telt niet mee voor het plafond.

**Navertelling en taal na de redactie.** Geen afwijking van de bedoeling. De losse woorden in
de bronregel zijn opnieuw gevouwen (witruimte, geen inhoudsverandering).

Geen enkel punt is verslechterd; geen nieuw feitelijk punt.

## Eindcijfer van record (F6c): 9,0

Plafondregel (§11.3): elk criterium had een "voor een 9"-punt en dat punt is opgelost, dus
elk deelcijfer stijgt naar het cijfer dat de beoordelaar in het vooruitzicht stelde (9,0 per
criterium). Het weeggemiddelde is dan ook 9,0, ruim onder het genoemde plafond van 9,1 "bij
volledige oplossing van alle punten".

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Eindcijfer** | | **9,0** |

Klaar: eindcijfer ≥ 9,0, geen deelcijfer onder 8,5, taal blokkeert niet.
