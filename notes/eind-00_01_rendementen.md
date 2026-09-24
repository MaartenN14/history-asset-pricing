STATUS 00_01_rendementen F6c words=5085 prose=PASS open=0 cijfer=8,7 min=8,5

# Eindbeoordeling (F6): Rendementen en hun statistiek

## Eindcijfer: 8,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,70 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,43, dus 8,4.
Lengte: 4.967 woorden, onder de 5.500.

## Feitelijke fouten

Nagerekend met `uv run python -c ...` en tegen de celuitvoer (`tools/nb_outputs.py`):
toy (5%, 3,2280%, 1,772 pp, 4,32 tegen 2,59), $s = 22{,}9\%$ en 13,2 pp,
$e^{0{,}0047\cdot1200}\approx 281$, $1{,}02^{100} = 7{,}24$, $\sqrt{2/100}$ en
$\sqrt{2/25200}$, $VR \approx 1{,}17$ en 2,0 naar 2,2 pp, $\sqrt{19/2}\approx 3{,}1$,
0,04 maal $\sqrt{263} = 0{,}65$, 22 keer zoveel waarnemingen, 1,83 naar 1,75, de
replicatietabel (9,46%; +0,46 pp; 12,91%; interval 1,8% tot 17,1%), de
autocorrelaties (8 van 12 onder 0,03), de oefeningen (0,16% tegen 0,13%, 84%,
binnen 0,24 pp, 9,46% naar 10,92%, 764 jaar). Alles klopt, op één bewering na.

1. **Theorie, "Opzet: twee soorten rendement".** "De notatie van [](#00-00-setup)
   reserveert kleine letters voor log-grootheden." Dat staat er niet. De setup zegt:
   "Zonder aankondiging zijn alle grootheden niveaus, en is $r$ het netto simpele
   rendement. Een logrendement krijgt een eigen symbool, bijvoorbeeld $\ell$." Wat
   deze lecture doet ($r$ simpel, $\ell$ log) is juist de setup-conventie; de
   gegeven reden is onjuist.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- Toy-voorbeeld en "Het kernresultaat": elk getal is uitgerekend, en de drie
  toy-jaren komen terug als schatting van $\sigma$ ($s = 22{,}9\%$, standaardfout
  13,2 pp). Het verschil tussen delen door 3 en door 2 krijgt een zin.
- "Merton (1980)": $W_t$, drift, ML-schatter krijgen een naam en een getal voordat
  de stelling komt; de relatieve fout 14% tegen 0,9% maakt het resultaat tastbaar.
- "Wanneer de aannames niet gelden": de twee formules met verschillende eenheden
  van $\sigma$ worden expliciet uit elkaar gehaald.

*Aanmerkingen*
- Opzet: "De notatie van [](#00-00-setup) reserveert kleine letters voor
  log-grootheden." Onjuist (zie boven); een lezer die de setup openslaat, raakt
  in de war over wat $r$ is.
- Opzet: "Laat $P_t$ de prijs zijn en $D_{t+1}$ het dividend". De setup-tabel
  schrijft $p_t$ en $d_t$; de afwijking wordt niet genoemd.
- Opzet: "vanaf hier is $\sigma$ de volatiliteit van het logrendement. Die van het
  simpele rendement ligt er dicht bij". Maar [](#eq-rendementen-se) en de
  replicatie rekenen met simpele rendementen; "dicht bij" krijgt geen getal.
- Theorie: vier symbolen voor bijna hetzelfde, $\nu$, $\mu$, $\mu_a$, $\mu_g$,
  binnen twee subsecties.

*Beter uitleggen*
- Het verschil tussen $\sigma$ van log en simpel rendement: één getal (bijvoorbeeld
  22,9% simpel tegen het log-equivalent in de replicatie) zou "dicht bij" vervangen.
- De bid-ask bounce als verklaring voor de equal-weighted afwijking: één zin
  waarom maandelijks herbalanceren die sprongen als rendement boekt.

### 2. Opbouw en rode draad (8,5)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord (twee procentpunt, volatiliteit
  bijna exact).
- Intuïtie doet drie voorspellingen, en de theorie lost ze elk met naam in ("Zo lost
  de theorie de derde voorspelling uit de intuïtie in", "Zo lost de stelling de
  eerste voorspelling ... in").
- 20% volatiliteit loopt door intuïtie, theorie, simulatie en oefeningen.

*Aanmerkingen*
- Toy-voorbeeld: het behandelt de variance drag, niet het kernresultaat (de
  standaardfout). De kern krijgt zijn toy-getal pas in de theorie.
- "Dezelfde eeuw, maand- en dagdata" en "clustering van volatiliteit" vallen buiten
  het replicatieblok en hebben geen verwachte afwijking.

*Beter uitleggen*
- Eén zin bij het toy-voorbeeld dat de drie jaren later ook de standaardfout
  dragen, zodat de lezer de brug verwacht.

### 3. Taal (8,5)

*Goed*
- Korte zinnen (gemiddeld 14,2 woorden), geen u/je, geen stapelzinnen.
- Termen krijgen bij eerste gebruik een Nederlandse uitleg (*variance drag*,
  *excess kurtosis*, *bid-ask bounce*).

*Aanmerkingen*
- Simulatie: "De vraag over steekproeven: wat gebeurt er ..." Koploze zin.
- Toy: "Het mechanisme is één ongelijkheid" en "Daarna wordt er nergens meer
  geïmporteerd." Losse, wat houterige meldingen.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Drie getallen, vier handstappen, één recept dat vooraf als nog niet afgeleid is
  aangekondigd, tabel hand/code, en een zin "Wat de lezer nu weet".

*Aanmerkingen*
- Zie criterium 2: het toy draagt niet het kernresultaat.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- Elke cel heeft een zin ervoor en erna; figuren hebben "Let op" vooraf en een
  bijschrift dat zegt wat te zien is.
- `annual_summary` en `describe_frequency` lezen als de formules.

*Aanmerkingen*
- Simulatie: `observed = log_price[:, ::step]` in een lus over blokken van 250
  paden. Leesbaar met commentaar, maar het blokken is geheugentechniek die de
  wiskunde verbergt.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8,5)

*Goed*
- Blok volledig (bron, wat, data, verschil, verwachte afwijking); tabel
  origineel/hier met 95%-interval; oordeel "Geslaagd" met verwijzing naar het ene
  procentpunt uit het blok.
- De boodschap "Het beroemde 9,0% zei dus weinig meer dan dat het rendement
  positief was" volgt direct uit de tabel.

*Aanmerkingen*
- "De equal-weighted variant ligt zoals verwacht hoger: 12,9%, bijna vier
  procentpunt boven de 9,0%." Getallen in lopende tekst die ook in de tabel staan.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy, afleiding van Merton zonder continue tijd, uitbreiding van de
  replicatie naar drie perioden; elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De onjuiste bewering over de setup-notatie vervangen door wat de setup zegt, en
   $P_t, D_{t+1}$ in lijn brengen of de afwijking in één zin noemen (helderheid
   8 → 8,5).
2. Het verschil tussen de $\sigma$ van log- en simpel rendement met één getal
   uitrekenen, en $\nu$, $\mu$, $\mu_a$, $\mu_g$ in één zin naast elkaar zetten
   (helderheid → 8,5).
3. De maand/dagtabel een eigen verwachting geven of expliciet als illustratie van
   Merton aankondigen (opbouw 8,5 → 9).

## Navertelling in vijf zinnen

Een gemiddeld rendement is na een eeuw jaarcijfers maar op ongeveer twee
procentpunt nauwkeurig, omdat de standaardfout $\sigma/\sqrt{T}$ is en
$\sigma \approx 20\%$ groot is tegen een premie van ongeveer 6%. Volgens Merton
helpt vaker meten daar niet bij: de drift hangt alleen af van begin- en eindkoers,
terwijl de variantie met elke extra waarneming scherper wordt. Het meetkundig
gemiddelde ligt een halve variantie onder het rekenkundige; beide zijn juist, voor
een andere vraag. Fisher en Lorie's 9,0% over 1926–1960 is na te bouwen (9,46%),
maar had een 95%-interval van ongeveer 2% tot 17%. Volatiliteit klontert en is
voorspelbaar, het rendement nauwelijks.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-00_01_rendementen.md` §F6-1 en de lecture.

| punt | status | vindplaats |
|---|---|---|
| Fout 1: setup-notatie | opgelost | Opzet: "Zoals in [](#00-00-setup) is $r$ het netto simpele rendement, en krijgt het *logrendement* een eigen symbool" |
| Verbetering 1: notatie $p_t$, $d_{t+1}$ | opgelost | Opzet: "beide als niveaus, zoals in de hele reeks"; Merton met $d\log p_t$ |
| Verbetering 2: $\sigma$ log/simpel, vier symbolen | opgelost | 18,34% tegen 18,32% (klopt met de nieuwe tabelrij 0,1834/0,1832); "Vier symbolen, twee grootheden" |
| Verbetering 3: maand/dagtabel | opgelost | "geen replicatie maar illustraties van [](#thm-rendementen-merton)", met verwachting |
| Naadpunt 1 (kleine letters) | opgelost | zie fout 1 |
| Naadpunt 2 ($P_t$, $D_{t+1}$) | opgelost | geen $P_t$ of $D_{t+1}$ meer in de lecture |
| Naadpunt 5 (premie 6% tegen 8%) | opgelost | Intuïtie: 6% als kalibratie, Mehra-Prescott 6,18%, setup 8,3% op French-data, verschil door de periode |
| Naadpunt 6 ($T$, $N$) | opgelost | $T$ overal jaren, $N$ waarnemingen ($\sigma\sqrt{VR(N)}/\sqrt N$) |

Overige aanmerkingen: de koploze simulatiezin, de importmelding, de EW-getallen in
de tekst, de bid-ask bounce en de brug van toy naar standaardfout zijn opgelost. De
blokverwerking in de simulatiecel is met reden afgewezen (looptijd en geheugen);
dat blijft een klein punt bij criterium 5.

Geen verslechteringen en geen nieuwe feitelijke fouten. Nagerekend: 18,34 en 18,32
uit de celuitvoer; $N = 1200$ en $VR \approx 1{,}17$ zijn ongewijzigd.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8,5 | 8,5 |
| 3 | Taal | 8,5 | 9 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 8,5 |
| 6 | Replicatie | 8,5 | 9 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,70 + 1,35 + 0,90 + 0,85 + 0,90 + 0,45 = 8,70. **Eindcijfer 8,7,
laagste deelcijfer 8,5.** Opbouw blijft 8,5: het toy draagt de variance drag, niet
het kernresultaat. De brug maakt dat zichtbaar maar lost het niet op.
