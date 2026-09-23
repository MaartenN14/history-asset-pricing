# Beoordeling: 00_01_rendementen — Rendementen en hun statistiek

Maatstaf: `plannen/rubriek-didactiek.md`. Lezer: eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft.

## Eindcijfer: 7,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 7 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 7 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 8 |

Gewogen: 0,3·7 + 0,2·8 + 0,15·7 + 0,1·7 + 0,1·7 + 0,1·8 + 0,05·8 = 7,35 → 7,4.
Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

---

## 1. Helderheid van de uitleg — 7

**Goed**
- *Het kernresultaat: de standaardfout van 2%*: formule, direct ingevuld
  ($20/\sqrt{100} = 2$), daarna het 95%-interval en de twee rekensommen
  (44 jaar, 400 jaar). Precies wat de rubriek vraagt: bij elke formule waarvan de
  grootte ertoe doet staat een getal.
- *Merton (1980)*: na de stelling de relatieve fout van de variantie concreet
  ($\sqrt{2/100} = 14\%$ tegen 0,9%) en het beeld "evenveel informatie als twee
  koersen".
- *Toy-voorbeeld*: alle getallen uitgerekend, zodat latere verwijzingen
  ("$5\% - 1{,}75\% = 3{,}25\%$") iets concreets oproepen.

**Aanmerkingen**
- *Intuïtie*: "Wie niet zegt welk gemiddelde hij bedoelt, zit er bij 20%
  volatiliteit over een eeuw al een factor zeven naast." De factor zeven wordt
  nergens uitgerekend; ook in *Meetkundig, rekenkundig en de variance drag*
  ("dat is over een eeuw de factor zeven uit de intuïtie") blijft hij een
  bewering.
- *Meetkundig, rekenkundig en de variance drag*: het symbool $\sigma$ wisselt van
  betekenis. In de stelling staat $\sigma_\ell$ (log) naast $\sigma$ (simpel);
  in *Het kernresultaat* is $\sigma$ de SD van simpele rendementen; in de stelling
  van Merton ("$d\ell_t = \nu\,dt + \sigma\,dW_t$") is $\sigma$ weer de
  log-volatiliteit, zonder dat dat gezegd wordt.
- *Annualisatie en de wortel-$t$-regel*: "de Sharpe-ratio $\nu\sqrt{k}/\sigma_\ell$
  groeit met $\sqrt{k}$." De Sharpe-ratio wordt hier voor het eerst genoemd en
  niet gedefinieerd.
- *Opzet: twee soorten rendement*, warning: "Dat is een halve procentpunt in één
  maand, en over een eeuw honderden procenten." Het tweede deel is vaag en niet
  na te rekenen.
- *Wanneer de aannames niet gelden*: "Die wordt $\sigma\sqrt{VR(T)}/\sqrt{T}$ in
  plaats van $\sigma/\sqrt{T}$." $VR$ is gedefinieerd in perioden $q$ (maanden),
  $T$ is in jaren; de lezer moet zelf bedenken dat de maandautocorrelatie van
  0,09 hier op jaarrendementen wordt toegepast.
- *Wanneer de aannames niet gelden*: "De variantie van $\hat\sigma^2$ is dan
  $\sigma^4(\kappa-1)/N$" komt zonder herkomst of één-regel-argument.
- *Replicatie*: "Het beroemde 9,0% had dus een 95%-interval van ongeveer 2% tot
  17%." Het interval gebruikt de standaardfout van het *rekenkundig* gemiddelde
  rond een *meetkundig* gemiddelde, precies de verwarring waartegen de lecture
  waarschuwt.
- *Overzicht*: "de standaardfout van 2%: bij 20% volatiliteit per jaar is het
  gemiddelde na een eeuw op twee procentpunt na bekend". Een standaardfout van
  2 is geen onzekerheid van 2; het 95%-interval is ±4. De formulering zet de
  lezer op het verkeerde been tot *Het kernresultaat*.

**Beter uitleggen**
- De factor zeven: één regel $e^{0{,}02 \times 100} \approx 7{,}4$ (of
  $1{,}02^{100}$) bij de eerste vermelding.
- $\sigma$ tegenover $\sigma_\ell$: één zin bij de stelling van Merton dat $\sigma$
  daar de volatiliteit van het logrendement is, en in de tekst één vaste naam per
  symbool.
- Sharpe-ratio: naam en betekenis (verwacht rendement gedeeld door
  standaarddeviatie) en één getal, bijvoorbeeld de dagwaarde uit dezelfde alinea
  (0,04/1 ≈ 0,04 per dag, ≈ 0,6 per jaar).
- Het interval rond 9,0%: zeggen dat het een benadering is die de standaardfout
  van het rekenkundig gemiddelde leent, of het interval om het rekenkundige
  gemiddelde leggen.
- $\sigma^4(\kappa-1)/N$: één regel dat de variantie van een gekwadrateerde
  normale/niet-normale waarneming $\E[\ell^4] - \sigma^4 = (\kappa - 1)\sigma^4$
  is.

## 2. Opbouw en rode draad — 8

**Goed**
- *Overzicht* stelt de vraag en geeft het antwoord in de tweede zin
  ("dat is na een eeuw data nog maar op twee procentpunt na bekend, terwijl de
  volatiliteit bijna exact vastligt"), gevolgd door een routekaart.
- *Intuïtie* doet twee expliciete voorspellingen ("We verwachten dus twee
  dingen"), en de theorie lost ze zichtbaar in ("Zo lost de stelling de eerste
  voorspelling uit de intuïtie in").
- De standaardfout van 2% loopt als één draad van toy (13 procentpunt bij drie
  jaar) via theorie en simulatie (0,02 in de tabel) naar de replicatie (3,9 en
  1,8) en *Wat er brak*.

**Aanmerkingen**
- Het *Samengevat*-blok staat aan het eind van *Theorie*, niet aan het eind van
  de lecture; na *Replicatie* en *Wat er brak* volgt geen samenvatting.
- Niet elke sectie begint met haar conclusie. *Dezelfde eeuw, maand- en
  dagdata* begint met "Houdt de stelling van Merton stand op echte data?",
  *Wat er wél in de data zit* met "Geldt de wortel-$t$-regel op echte data, en
  klonteren de schommelingen?"; het antwoord komt pas na de tabel.
- *Wanneer de aannames niet gelden* is een lange zijtak (autocorrelatie,
  kurtosis, stabiele verdelingen) binnen de theorie; de rode draad zakt daar weg.
- *Simulatie*: "De volatiliteit ligt dicht bij de 23% van het toy-voorbeeld."
  De toy (23%), simulatie (20%, drift 8%) en replicatie gebruiken verwante maar
  niet dezelfde getallen; de koppeling wordt geclaimd, niet gebruikt.

**Beter uitleggen**
- Een kort *Samengevat* aan het eind van de lecture (of het bestaande blok daarheen)
  met het replicatiegetal erin.
- De twee empirische subsecties openen met hun uitkomst ("De dagreeks verbetert de
  standaardfout nauwelijks: 1,83 naar 1,67").

## 3. Taal — 7

**Goed**
- Korte zinnen en concrete beelden in *Intuïtie* (windmeter, $0{,}80 \times 1{,}25 = 1$).
- Engelse vaktermen krijgen bij eerste gebruik een Nederlandse uitleg
  (*variance drag*, *equity premium*, delistings).
- Geen u/je; de lezer wordt als "wie" of "een onderzoeker" aangesproken.

**Aanmerkingen**
- *Overzicht*: "In 1964 rapporteerden Lawrence Fisher en James Lorie op de verse
  CRSP-tape (het Center for Research in Security Prices, dat de koersen van alle
  NYSE-aandelen vanaf 1926 op magneetband zette) het gemiddelde rendement op
  Amerikaanse aandelen over 1926–1960" — stapelzin met een lange tussenzin.
- *Replicatie*: "Als meting was de eerste betrouwbare meting van het
  aandelenrendement nauwelijks informatiever dan de vraag of het getal positief
  is." Dubbel "meting", en een meting vergeleken met een vraag.
- *Wat er brak*: "de bron geeft te weinig water voor twee emmers" — beeld dat meer
  vraagt dan het uitlegt.
- *Opzet*, warning: "verliest makkelijk een alpha" — calque.
- Twee namen voor één begrip: "vertraging" in de tekst, "lag" in de tabelindex
  (*Wat er wél in de data zit*); "meetkundig gemiddelde" naast "samengesteld
  rendement" en "samengesteld (meetk.)"; "standaardfout van 2%" naast
  "2 procentpunt".
- *Intuïtie*: "Aandelenrendementen zijn wind." Het beeld schiet door; het
  gemiddelde rendement als "afgelegde afstand" van wind klopt niet met "hoeveel
  lucht is er langsgekomen".

**Beter uitleggen**
- Eén naam per begrip vastleggen ("meetkundig gemiddelde"; "vertraging" ook in de
  tabel).
- De CRSP-uitleg uit de zin halen en als eigen zin ervoor zetten.

## 4. Toy-voorbeeld — 7

**Goed**
- Drie getallen, met de hand in vijf minuten na te rekenen; elke stap met
  tussenuitkomst.
- Tabel "met de hand" naast "code".
- Slotzin wat de lezer nu weet ("Wie dit narekent, weet nu drie dingen").

**Aanmerkingen**
- Meer dan één mechanisme: rekenkundig tegen meetkundig, logadditiviteit,
  variance drag én standaardfout. De rubriek vraagt één mechanisme; de toy zegt
  zelf "Deze drie getallen bevatten al de hoofdpunten van de lecture".
- "Deel de kwadratensom door $T-1 = 2$ in plaats van door drie." Twee
  variantie-definities (ddof 0 in stap 4, ddof 1 in stap 5) zonder zin waarom.
- Twee niet hier afgeleide formules (drag-recept en $s/\sqrt T$), waar de rubriek
  er hoogstens één toestaat; de tweede wordt naar [de vorige lecture] verwezen.

**Beter uitleggen**
- Eén zin bij stap 5 waarom de standaardfout door $T-1$ deelt en de drag door
  $T$.
- Overweeg de standaardfout uit de toy te halen of expliciet als tweede, los
  mechanisme te markeren.

## 5. Code en figuren — 7

**Goed**
- De toy-cel heeft benoemde tussenresultaten (`arith`, `geom`, `drag_approx`).
- Vóór beide figuren staat waarop te letten ("Let op de breedte van de
  histogrammen", "Let op waar de twee lijnen eindigen"), erna wat te zien is.
- `annual_summary` leest als de formules uit de theorie.

**Aanmerkingen**
- *Simulatie*: `agg = steps.reshape(len(block), n_years * k, per_year // k).sum(axis=2)`
  is een compacte truc die het aggregeren verbergt; er staat geen commentaar bij.
- *Dezelfde eeuw*: de kolommen `nobs`, `mean_ann`, `std_ann`, `se_mean_ann`
  komen uit `hap.summary_stats` en worden niet toegelicht.
- *Oefening 3*: de variabele `rows` wordt hergebruikt (eerder de rijnamen van de
  toy-tabel) en `(excess_kurtosis + 2)` staat voor $\kappa - 1$ zonder commentaar.
- *Wat er wél in de data zit*: de variance-ratio-cel heeft geen zin erna die de
  tabel leest; de interpretatie komt na de volgende cel samen.

**Beter uitleggen**
- Eén commentaarregel bij de `reshape`: "tel per blok van `per_year // k` dagen
  de logrendementen op".
- Eén regel onder de Merton-tabel die de `summary_stats`-kolommen benoemt.

## 6. Replicatie en empirie — 8

**Goed**
- Replicatieblok met bron, wat, data, verschil en verwachte afwijking, onder 250
  woorden, en een toetsbare eis ("Komt hij lager uit, dan zit er een fout in de
  code").
- Tabel origineel/hier/verschil.
- Oordeel begint met **Geslaagd.** en verwijst naar de aangekondigde marge.

**Aanmerkingen**
- *Replicatie*, blok: "Zonder herbelegging was het 6,9%." Dit getal wordt niet
  gerepliceerd en leidt af.
- *Replicatie*: "Het beroemde 9,0% had dus een 95%-interval van ongeveer 2% tot
  17%" — zie criterium 1; de kernboodschap van de replicatie rust op een gemengd
  interval.
- *Dezelfde eeuw* en *Honderdvijftig jaar*: veel getallen in lopende tekst
  ("van 1,83 naar 1,67 procentpunt ... (17,1% tegen 18,3%) ... van 7,4 naar
  16,1"), die deels in de tabel staan en deels (verschil, halve variantie) niet.

**Beter uitleggen**
- Bij de equal-weighted uitkomst (12,9%) de aangekondigde verwachting ("moet
  hoger uitkomen") één keer letterlijk terughalen, zodat het oordeel naar de
  verwachting verwijst en niet alleen naar het teken.

## 7. Oefeningen — 8

**Goed**
- Instap is een variatie op de toy (volgorde omdraaien, −30%).
- Oefening 1 vraagt een afleiding (Merton in discrete tijd), oefening 2 breidt de
  replicatie uit naar drie perioden.
- Elke uitwerking eindigt met "Wat dit leert".

**Aanmerkingen**
- *Oefening 1, uitwerking (2)*: "$T^{*} = (t\,\Delta\mu^{-1}\sigma)^2$" — ongewone
  schrijfwijze van een formule die in de theorie al leesbaar stond.
- *Oefening 3*: de uitwerking gebruikt $\sqrt{(\kappa-1)/N}$ met een kurtosis uit
  ongeveer honderd jaarwaarnemingen, terwijl de tekst zelf zegt dat die "zeer
  onnauwkeurig" is; de les wordt daardoor zwakker dan geformuleerd.

**Beter uitleggen**
- In oefening 1(2) gewoon [](#eq-rendementen-jaren) invullen met de getallen.

---

## De drie verbeteringen met het meeste effect op het cijfer

1. **Helderheid (7 → 8):** reken de factor zeven uit, leg $\sigma$ tegenover
   $\sigma_\ell$ vast (vooral in de stelling van Merton), definieer de
   Sharpe-ratio, en zet het interval rond 9,0% op de juiste standaardfout.
   Effect op het eindcijfer ≈ +0,3.
2. **Opbouw (8 → 9):** een *Samengevat* aan het eind van de lecture, en de
   empirische subsecties openen met hun uitkomst in plaats van met een vraag.
   Effect ≈ +0,2.
3. **Toy (7 → 8):** beperk de toy tot rekenkundig/meetkundig/log/drag en haal de
   standaardfout eruit (of markeer hem als apart), met één zin over $T$ tegen
   $T-1$. Effect ≈ +0,1.

## Navertelling in vijf zinnen

Een rendement kun je simpel of logaritmisch meten; logrendementen tellen op over
de tijd, simpele rendementen over activa. Het meetkundig gemiddelde, wat een
belegger echt overhoudt, ligt ongeveer een halve variantie onder het rekenkundige,
en dat scheelt bij 20% volatiliteit twee procentpunt per jaar. De standaardfout
van een gemiddeld rendement is $\sigma/\sqrt{T}$, dus na een eeuw nog 2
procentpunt, en volgens Merton helpt vaker meten daar niet bij, wel bij de
variantie. De replicatie van Fisher en Lorie (9,0% over 1926–1960) lukt binnen een
halve procentpunt, maar dat getal had een standaardfout van bijna 4 procentpunt.
Daarom valt met rendementsdata wel te zeggen óf er een premie is, maar niet hoe
groot hij is.

Wijkt niet af van het Overzicht.
