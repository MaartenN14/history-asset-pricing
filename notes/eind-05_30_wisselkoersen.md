STATUS 05_30_wisselkoersen F6c words=5836 prose=PASS open=2 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

# Eerste herziening (workflow §12)

Eindbeoordeling F6 van `lectures/05_30_wisselkoersen.md` (1384 regels), na F1, F23 en F4T.
Geen vorig cijfer. Getallen nagerekend tegen `$TEMP/F6-05_30_wisselkoersen-out.txt`
(18 cellen) en met de hand (toy, lognormale premie, Fama-helling, peso-rekensom,
simulatiegrenzen).

## De drie verbeteringen met het meeste effect

1. **Eén naam voor index en correlatiegrens (helderheid 8,5 → 9,0).** De
   risk-sharing-index is gedefinieerd als $1 - \Var(\Delta s)/(\Var(\log m) + \Var(\log m^*))$
   (r.306), maar vanaf r.344 heet de correlatiegrens $1 - \Var(\Delta s)/(2a^2)$ ook
   "index" (r.345, simulatietitel r.640, replicatiekolommen r.1061, oefening 2.3), terwijl
   het toy (r.175–177) juist laat zien dat index en correlatie verschillen. Eén zin bij
   r.318–327 dat $1 - V/(2a^2)$ een ondergrens is voor beide en gelijk aan de index bij
   $\sigma = \sigma^* = a$, en daarna overal één woord. Samen met punt 2 en 3 onder
   helderheid (toy-stap 1, Fama-bewijs).
2. **Hardop-zinnen en getallenalinea's (taal 8,5 → 9,0).** Vijf zinnen herschrijven
   (zie het taaloordeel en r.84, r.1147–1150), en de replicatiealinea's met zes tot acht
   getallen (r.982–987, r.1066–1072, r.1120–1124) terugbrengen tot drie getallen, met de
   rest in de tabel die er al staat.
3. **Replicatie sluitend maken (replicatie 8,5 → 9,0).** Een rij Fama-helling (origineel
   uit Fama 1984) in de vergelijkingstabel (r.1135–1143), momentum en value opnemen in
   "Verwachte afwijking" (r.831–834), en "28% in het najaar van 2008" (r.1149, r.1169)
   in lijn brengen met de cel (−26,6% aug–dec, drawdown −28,0% tot januari 2009).

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Gewogen** | | **8,675 → 8,7** |

Laagste deelcijfer 8,5 (helderheid, taal, toy, replicatie); taal blokkeert niet.

### 1. Helderheid (8,5)

*Goed.*
- Getal naast de formule vrijwel overal: $a = 0{,}47$ bij SR een half (r.341), 0,98 en
  71% (r.345–346), de lognormale premie 0,0153 tegen exact 0,0152 (r.501–503), $b \approx
  -\tfrac13$ bij $\beta = -0{,}62$ (r.927–928), $1{,}62$ keer het renteverschil (r.942).
- Elk resultaat heeft een economische richting: "De buitenlandse munt stijgt dus in
  precies die toestanden waarin marginaal nut in het buitenland hoog is" (r.278–279);
  de drie Fama-gevolgen als lijst met betekenis (r.436–449).
- Geleende resultaten in één regel herhaald: HJ-grens (r.332–334), CIP-afleiding
  (r.358–371).

*Aanmerkingen.*
- Toy-voorbeeld, r.151–153: "Het land met de rustigere SDF heeft de hogere rente, omdat
  daar minder uit voorzorg wordt gespaard." In het toy komt de hogere rente uit de lagere
  $\E[m^*]$, die zo gekozen is; de theorie zegt later zelf "Of die munt ook de hogere rente
  heeft, hangt af van hoe de rente met de variantie beweegt" (r.505–506), en oefening 1 is
  een tegenvoorbeeld (rustiger SDF, gelijke rentes). De algemene bewering in stap 1 is dus
  te sterk.
- Hoe glad mogen wisselkoersen zijn?, r.344–346: "Een wisselkoersvolatiliteit van 10% en
  een SDF-volatiliteit van 50% geven een index van $1 - 0{,}1^2/(2 \cdot 0{,}5^2) = 0{,}98$".
  Dit is de correlatiegrens [](#eq-wisselkoersen-rhomin), niet de index
  [](#eq-wisselkoersen-bcs); de twee vallen alleen samen bij $\sigma = \sigma^* = a$, wat
  nergens staat (H7).
- De Fama-decompositie, r.431–433: "Voor de laatste bewering geldt $rx = (i^* - i) +
  \Delta s$". De propositie (r.412–422) bevat alleen de formule voor $\beta$; het bewijs
  bewijst drie beweringen die pas ná het bewijs in de lijst staan (r.438–443) (H3, H8).
- Simulatie, r.654: `VOL_EQ = 0.16` komt in de proza niet voor; de lezer weet niet dat een
  aandelenvolatiliteit van 16% de onzekerheid van de Sharpe-ratio bepaalt (H2).
- De wisselkoers als verhouding van twee SDF's, r.249: "Een wisselkoers heeft geen waarde
  los van de twee SDF's, want hij is hun verhouding." "Geen waarde" laat zich lezen als
  "is waardeloos"; bedoeld is dat de verandering volledig vastligt.

*Beter uitleggen.* Het verschil tussen de risk-sharing-index en de correlatiegrens:
één zin met de voorwaarde $\sigma = \sigma^* = a$ en het toy als voorbeeld van een index
onder één bij correlatie één. Waarom de rustiger munt in dit toy een hogere rente heeft
(gekozen $\E[m^*]$), met de verwijzing naar $b$ als de plek waar het algemeen wordt.

*Voor een 9.*
- `lectures/05_30_wisselkoersen.md:318` — zin dat $1 - V/(2a^2)$ index én correlatie
  begrenst en gelijk is aan de index bij $\sigma = \sigma^* = a$; daarna één naam in
  r.345, r.640–648, r.700, r.1040–1061, r.1245.
- `lectures/05_30_wisselkoersen.md:151` — "omdat" vervangen door de constructie
  ($\E[m^*]$ gekozen lager), zonder algemene wet.
- `lectures/05_30_wisselkoersen.md:412` — de drie gevolgen in de propositie opnemen,
  of het bewijs beperken tot de formule en de gevolgen na de lijst bewijzen.
- `lectures/05_30_wisselkoersen.md:646` — de 16% aandelenvolatiliteit in de zin noemen.

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in de tweede zin (r.38–40); routekaart
  (r.218–224) en Samengevat (r.624–638) staan waar ze horen.
- H11 sterk: toygetallen keren terug in de notatie (r.245), het lognormale model
  (r.463–464, r.501–503) en de simulatiekalibratie (r.646–648).
- H12 ingelost in gewone zinnen: "De telling uit de intuïtie komt dus uit" (r.349–350),
  "Het teken uit de intuïtie klopt dus" (r.504–505), trap en lift terug in de figuur
  (r.1033–1034). 5.622 woorden, onder de grens.

*Aanmerkingen.*
- Theorie, r.541–622: de drie laatste `###` (carry-portefeuilles, crashrisico, momentum
  en value) zijn een literatuuroverzicht met veertien getallen uit artikelen, waarvan zes
  in F23/F4 onzeker bleven. Ze dragen de rode draad minder dan de eerste vijf `###`.

*Beter uitleggen.* Niets wezenlijks; de opbouw is te volgen zonder terugbladeren.

### 3. Taal (8,5)

*Goed.*
- `prose_stats` PASS: zinslengte gemiddeld 16,5, geen zin boven 40, alinea gemiddeld 50
  woorden, geen gedachtestreepjes, motiefnamen binnen de grens (risico of vergissing 2×,
  standaardfout van 2% 1×, theorie of feit 1×).
- Verband met voegwoorden in de afleidingen: "Is de helling negatief, dan moet de premie
  harder bewegen dan de verwachte depreciatie en er tegenin gaan" (r.407–408).
- De taalredactie heeft geen vakterm van betekenis veranderd (index, correlatiegrens,
  premie, SDF, HML$_{FX}$ nagelopen); het probleem in punt 1 van de verbeteringen staat los
  van de redactie.

*Aanmerkingen.*
- Overzicht, r.55–57: "waarmee de oude macrovraag of landen hun risico delen met twee
  standaarddeviaties te beantwoorden is."
- Overzicht, r.62–64: "De verworpen theorie werd zo een feit waarvoor daarna concurrerende
  verklaringen kwamen, en dat maakt carry tot theorie of feit in zuivere vorm."
- Intuïtie, r.84: "Vervolgens tellen we." (telegramachtig).
- Momentum en value in valuta (replicatie), r.1126–1127: "Om zo'n portefeuille van
  kenmerken die elk een ander risico dragen, draait het bij Barroso en Santa-Clara."
- Vergelijking met de originelen, r.1147 en r.1150: "Alle verwachtingen uit het
  replicatieblok komen uit." en "maar daar ging de verwachting niet over" (regeltaal,
  §11.12).
- Carry-portefeuilles, r.982–987; Brandt, Cochrane en Santa-Clara op G10-data,
  r.1066–1072; Momentum en value, r.1120–1124: zes tot acht getallen per alinea (grens
  drie).

*Beter uitleggen.* n.v.t.

*Voor een 9.* `lectures/05_30_wisselkoersen.md:55`, `:62`, `:84`, `:1126`, `:1147`,
`:1150` herschrijven; `:982`, `:1066`, `:1120` terug naar drie getallen per alinea met
verwijzing naar de tabel boven de alinea.

### 4. Toy-voorbeeld (8,5)

*Goed.*
- Tabel "met de hand / code" met veertien gelijke waarden (cel 2); alles is in vijf
  minuten na te rekenen.
- Slotzin zegt wat het getal betekent: "Een frank die in slechte tijden daalt, is voor een
  Amerikaan dus riskant en levert het hele renteverschil als premie op" (r.211–213).
- Stap 3 (controle dat $m$ de frankbelegging op 1,0000 prijst) maakt de identiteit
  voelbaar vóór de afleiding.

*Aanmerkingen.*
- Toy-voorbeeld, r.146–149: "De wisselkoers is de verhouding van de twee SDF's, zodat
  $S_{t+1}/S_t = m^*/m$ in elke toestand, en de theorie leidt dat als eerste af." en
  stap 6 (r.169–173) gebruiken twee nog niet afgeleide formules (identiteit en index),
  naast de geleende premieformule in stap 5; de rubriek staat er één toe.
- Twee mechanismen in één toy: carry-premie (stap 4–5) en risk sharing (stap 6).
- Stap 1, r.152–153: zie helderheid (rente en voorzorg).

*Voor een 9.* `lectures/05_30_wisselkoersen.md:169` — stap 6 inkorten tot de drie
standaarddeviaties en de index pas in Theorie (r.318) uitrekenen, of expliciet zeggen
dat de identiteit de enige nog niet afgeleide formule is en de index als definitie
aankondigen; `:151` zoals onder helderheid.

### 5. Code en figuren (9,0)

*Goed.*
- Elke hoofdcel heeft een zin ervoor en erna; vóór elke figuur staat waarop te letten
  ("In de figuur gaat het om de dikke lijn van HML$_{FX}$ in het grijze najaar van 2008",
  r.1004–1006), erna wat te zien is.
- Code leest als de wiskunde: `fx_growth = m_foreign / m_home`, `rx_next = rate_diff +
  ds_next`, `implied_corr` volgt [](#eq-wisselkoersen-rhomin).
- Tabellen en figuurteksten in het Nederlands.

*Aanmerkingen.*
- Oefening 2, uitwerking, r.1257: "**(2) en (3)**" staat als enige zin vóór de codecel.
- Oefening 3, uitwerking, r.1283–1286: codecel zonder zin ervoor.
- `sort_portfolios`, r.955: `np.ceil(ranks.mul(n_groups).div(count, axis=0))` is een
  compacte truc zonder commentaar over wat een groep is.

*Beter uitleggen.* Kleine punten; geen ervan blokkeert het volgen.

### 6. Replicatie en empirie (8,5)

*Goed.*
- Admonition compleet (bron, wat, data, verschil, verwachte afwijking) in ruim 200
  woorden (r.813–835).
- Tabel origineel/hier met standaardfouten (cel 14) en een oordeel dat met "Geslaagd"
  begint en de standaardfout gebruikt (r.1147–1152).
- De Fama-alinea koppelt het resultaat aan de decompositie en aan de standaardfout van 2%
  met uitleg ter plekke (r.930–942).

*Aanmerkingen.*
- Vergelijking met de originelen, r.1136–1142: de tabel heeft geen rij voor de
  Fama-helling, terwijl Fama (1984) als eerste bron staat (r.816).
- Replicatie, r.831–834: "Verwachte afwijking" noemt momentum en value niet, waardoor het
  oordeel moet zeggen "maar daar ging de verwachting niet over" (r.1150).
- Vergelijking met de originelen, r.1148–1149: "HML$_{FX}$ verloor in het najaar van 2008
  28%" — zie feitelijke fouten.
- Getallen in lopende tekst in plaats van in de tabel (r.982–987, r.1066–1072,
  r.1120–1124).

*Voor een 9.* `lectures/05_30_wisselkoersen.md:1136` rij Fama-helling toevoegen;
`:831` verwachte afwijking voor momentum en value; `:1149` en `:1169` het 2008-getal
gelijktrekken met cel 10.

### 7. Oefeningen (9,0)

*Goed.*
- Instap is een variatie op het toy met een scherpe les ("Een renteverschil is dus een
  symptoom en geen oorzaak", r.1230–1231).
- Afleiding (oefening 2) en twee replicatie-uitbreidingen (3 en 4), elk met een slotzin
  die zegt wat het leert (r.1312–1314, r.1381–1383).

*Aanmerkingen.*
- Oefening 1, r.1203: "De rentes zijn nu gelijk. Waarom verdient de carry trade toch een
  premie". Bij gelijke rentes is er volgens de definitie in r.61–62 geen carry trade;
  bedoeld is de frankbelegging.

*Beter uitleggen.* Geen.

## Feitelijke fouten (nagerekend)

1. `lectures/05_30_wisselkoersen.md:1148–1149` en `:1169`: "verloor in het najaar van
   2008 28%" / "verloor 28% in 2008". Cel 10: aug–dec 2008 −26,6% (log, cumulatief);
   −28,0% is de drawdown juni 2007–dec 2009 met het dal in januari 2009. r.1001–1002 zegt
   het wel juist. Klein, maar het getal staat twee keer verkeerd toegeschreven.
2. `lectures/05_30_wisselkoersen.md:1086–1087`: "met prijsindices die drie maanden
   achterlopen". De code (`value_signal = -(real_fx.shift(3) - real_fx.shift(63))`,
   r.1107) laat de hele reële wisselkoers, ook de spotkoers, drie maanden achterlopen.
   Beschrijving onnauwkeurig.
3. Conceptueel (geen rekenfout): `:151–153`, de algemene bewering dat de rustiger SDF de
   hogere rente heeft; zie helderheid.

Nagerekend en juist: toy (alle veertien waarden, ook $\Cov = -0{,}0204$ en index
0,8048), $a = 0{,}47$, 0,98 en 71%, lognormale premie 0,0153/0,0152, $b \approx -0{,}31$
bij $\beta = -0{,}62$, simulatiegrens 0,978, 0,87 bij SR 0,2, 0,50 bij SR 0,1,
nulpunt bij SR 0,07, peso 37%/0,115/8,5%, $\pi = 0{,}0106$ en 2%, zeven verwerpingen van
$\beta = 1$, alle replicatie- en oefengetallen tegen cel 7–18. Zes brongetallen uit
artikelen (LRV 0,54 en 70%, LV 2007, Menkhoff 2012a 90%, Burnside 0,911, BSC "een half",
BNP 81%, BCS 11,5–12,9%) blijven onzeker volgens `notes/feiten-05_30_wisselkoersen.md`;
Menkhoff 2012a (meer dan 90%) en 2012b (tot 10% per jaar) komen overeen met de abstracts.

## Navertelling in vijf zinnen

Een wisselkoersverandering is het verschil van de log-SDF's van twee landen, zodat
wisselkoersen iets zeggen over hoe marginaal nut tussen landen samenbeweegt. Omdat SDF's
volgens de HJ-grens met minstens zo'n 47% per jaar schommelen en wisselkoersen maar met
tien procent, moeten de SDF's van landen voor 98% samenbewegen, wat botst met de lage
correlatie van consumptiegroei. UIP faalt: de Fama-helling is negatief ($-0{,}62$ gepoold
op G10-data), wat betekent dat de premie volatieler is dan de verwachte depreciatie en er
tegenin beweegt, en in een lognormaal model levert de munt van het land met de rustigste
SDF die premie op. Carry verdient een Sharpe-ratio van 0,44, maar is links scheef en
verloor in 2008 ruim een kwart, en na 2008 is de premie niet meer aantoonbaar, zodat
risico en vergissing met deze standaardfouten niet te scheiden zijn. Momentum en value
voegen weinig gecorreleerde premies toe, en een mix van kenmerken verdunt het crashrisico
zonder het weg te nemen.

Wijkt niet af van het Overzicht.

## Taal na de redactie

De redactie heeft de zinsbouw goed rechtgetrokken (PASS, geen zin boven 40, weinig
dubbele punten) en geen vakterm van betekenis veranderd. Wat overblijft zijn enkele
zinnen die nog als geschreven in plaats van gesproken klinken, twee regeltaalresten in het
oordeel, en getallenalinea's in de replicatie.

Hardop-toets, drie zinnen met herschrijving:

1. r.55–57: "waarmee de oude macrovraag of landen hun risico delen met twee
   standaarddeviaties te beantwoorden is."
   → "Brandt, Cochrane en Santa-Clara maakten er in 2006 een meetinstrument van, zodat
   twee standaarddeviaties, die van de wisselkoers en die van de SDF, volstaan om de oude
   macrovraag te beantwoorden of landen hun risico delen."
2. r.62–64: "De verworpen theorie werd zo een feit waarvoor daarna concurrerende
   verklaringen kwamen, en dat maakt carry tot theorie of feit in zuivere vorm."
   → "Zo werd een verworpen theorie een vast feit waarvoor pas achteraf verklaringen
   werden gezocht, en bij carry ging het feit dus zuiver aan de theorie vooraf."
3. r.1126–1127: "Om zo'n portefeuille van kenmerken die elk een ander risico dragen,
   draait het bij Barroso en Santa-Clara."
   → "Barroso en Santa-Clara bouwen precies zo'n portefeuille uit kenmerken die elk een
   ander risico dragen."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Controleur van record (F6c) na F6b. Getallen nagelopen tegen `$TEMP/F6c-05_30_wisselkoersen-out.txt` (196 regels) en tegen getallen in de tekst.

**Getallencontrole.** Alle gewijzigde of nieuwe getallen herleidbaar: aug-dec 2008 -26,6% (cel 10) en drawdown 28% tot januari 2009; gepoolde Fama-helling -0,62, SE 0,38, t -4,23; SEK 0,16 met SE 1,11; Sharpe HML 0,44 (SE 0,15), value 0,47, momentum 0,07 (verschil 0,25 < 2 x 0,15); grens NZD 0,975 en CAD 0,991, G10-gemiddelde 0,980 en 0,914 bij markt min 2 SE; mix 0,52 en scheefheid -0,71; toy (0,8048, corr 1) en $1-0{,}01/(2\log 1{,}25)=0{,}978$. Geen niet-herleidbaar getal; de zes onzekere brongetallen uit F23 blijven onzeker en tellen niet opnieuw.

**Per punt.**
- Feit 1 (28% in najaar 2008): opgelost, nu 26,6% (aug-dec) en 28% als drawdown, in Vergelijking, Geslaagd en Wat er brak ("ruim een kwart").
- Feit 2 (value-vertraging): opgelost, "de hele reële wisselkoers drie maanden achter".
- Feit 3 / toy stap 1 (rustiger SDF, hogere rente): opgelost, $\E[m^*]$ is gekozen, algemeen via $b$.
- Verbetering 1 (index versus grens): opgelost. Zin bij de ondergrens zegt dat de uitdrukking index en correlatie begrenst en samenvalt bij $\sigma=\sigma^*=a$, toy als voorbeeld; daarna "grens" in proza, simulatie, tabelkolommen en oefening 2. Kleine rest: Overzicht en vergelijkingsrij noemen de gerepliceerde grootheid nog "index" (Brandt e.a. tabel 2), wat verdedigbaar is.
- Verbetering 2 (hardop en getallenalinea's): grotendeels opgelost. De zes zinnen zijn herschreven; carry-, BCS- en momentum-alinea's hebben nu hoogstens drie tot vier getallen. De alinea's na de Fama-tabel en na de crisiscel bevatten nog meer getallen, maar dat was geen punt en is niet verslechterd.
- Verbetering 3 (replicatie sluitend): opgelost. Fama-rij met "onder nul" als origineel, verwachte afwijking noemt momentum en value, 2008-getal gelijkgetrokken.
- Fama-propositie (H3, H8): opgelost, drie gevolgen in de propositie en een bewijs met Gevolg 1-3.
- VOL_EQ: opgelost (16% en zijn rol in de Simulatie-zin). "Geen waarde los van": opgelost.
- Toy stap 6 en de niet-afgeleide formules: opgelost (recept noemt de identiteit als enige, index als definitie). Twee mechanismen in één toy: open, geen Voor-een-9-punt.
- Opbouw (drie literatuur-###): open, geen Voor-een-9-punt.
- Code (commentaar `sort_portfolios`, zinnen bij oefening 2 en 3) en oefening 1 ("frankbelegging"): opgelost.
- Verslechtering: geen. Geen nieuwe feitelijke fout; afleidingen (Fama-gevolgen 1-3, ondergrens via $\sigma\sigma^*\ge a^2$) nagerekend.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 | 9,0 |
| 3 | Taal | 20% | 8,5 | 9,0 |
| 4 | Toy-voorbeeld | 10% | 8,5 | 9,0 |
| 5 | Code en figuren | 10% | 9,0 | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 | 9,0 |
| 7 | Oefeningen | 5% | 9,0 | 9,0 |
| | **Gewogen** | | 8,7 | **9,0** |

Plafond (§11.3): cijfers stijgen alleen waar de beoordelaar een punt had, tot zijn vooruitzicht; het eindcijfer is hoogstens 9,0. Laagste deelcijfer 9,0; taal blokkeert niet. Open: twee (twee mechanismen in het toy; literatuur-### in Theorie), beide zonder Voor-een-9-punt.

