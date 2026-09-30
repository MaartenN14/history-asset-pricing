STATUS 04_23_behavioral F6c words=5757 prose=PASS open=1 cijfer=9,0 min=8,5

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,6 -> F6c 9,0.

## Eerste herziening (workflow §12)

Eerste herziening van dit college; er is geen vorig cijfer. Gelezen: de .md volledig, celuitvoer
uit `$TEMP/F4T-04_23_behavioral-out-na.txt` (de uitvoer na F4T; `nb_outputs.py` opnieuw draaien
werd door de omgeving geweigerd), `prose_stats --check` PASS (5479 woorden, zinnen gemiddeld
16,1, geen zin > 40, alinea gemiddeld 44).

**Vakterm-controle na de taalredactie.** Geen vakterm is van betekenis veranderd. "Evaluatieperiode"
($h^{*}$) en "horizon" ($h$) blijven gescheiden, "herverkooprisico", "fondsuitstroom",
"sophisticated" en "risicomijdend van eerste orde" staan overal in dezelfde betekenis. Alle
proposities zijn nagerekend en kloppen in hun huidige formulering.

## De drie verbeteringen met het meeste effect

1. **Symbolen die twee dingen betekenen, en drie premies zonder verband** (helderheid 8,5 → 9,0,
   opbouw 8,5 → 9,0). $\lambda$ is in Prospect theory en Myopic loss aversion de verliesaversie
   (2,25) en in DSSW de positie $\lambda^{i}_t$, $\lambda^{n}_t$ (04_23_behavioral.md:363, 373);
   $r$ is in DSSW het dividend en de risicovrije rente (357) en in de joint hypothesis het log
   rendement (743), naast $r^{f}$ bij Benartzi-Thaler (266). Een regel in de DSSW-opzet die
   $\lambda^{j}_t$ als positie aankondigt ("niet de verliesaversie") volstaat. Daarnaast rekent de
   theorie met 6% ↔ een jaar, de simulatie met 4,87% (log) ↔ 6,8 maanden en de replicatie met
   6,7% ↔ 7,5 maanden (795–803, 844, 1102). Dat een lagere premie hier een *kortere* $h^{*}$
   geeft dan in de theorie, terwijl [](#eq-behavioral-bt) het omgekeerde zegt, komt door de
   volledige CPT en de risicovolle obligatie; één zin aan het begin van de simulatie moet dat
   zeggen.
2. **Getallen uit de replicatieproza naar de tabellen, en de "exact"-claim corrigeren**
   (replicatie 8,5 → 9,0, taal 8,5 → 9,0). De alinea's 971–974, 1102–1105 en 1107–1109
   dragen elk zes of zeven getallen, terwijl de tabellen erboven ze al geven. Laat per alinea
   hoogstens drie staan (het oordeel en het getal waar het op rust). Corrigeer "We rekenen de
   CPT-waarde bovendien exact uit" (1054–1055): de code rekent op 20 000 bootstraptrekkingen.
3. **De drie terugverwijzingen naar de intuïtie variëren en de tweede een naam geven** (taal
   8,5 → 9,0, opbouw mee). "De verwachting uit de intuïtie klopt dus" (317), "daarmee klopt ook
   het tweede vermoeden uit de intuïtie" (467–468) en "dat hadden we in de intuïtie ook
   verwacht" (773) zijn drie vormen van dezelfde vaste wending, en "het tweede vermoeden" is een
   genummerde verwachting (H12). Zeg bij het resultaat zelf wat er voorspeld was. Maak bij
   Shleifer-Vishny de voorspelling en het resultaat gelijk: de intuïtie zegt "als arbitrageurs
   veel hebben ingezet" (100–101), het resultaat spreekt over $a$ ("naarmate inleggers sneller
   vluchten", 703–704).

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Eindcijfer (gewogen)** | | **8,6** (8,575) |

Geen deelcijfer onder 8,5; taal blokkeert niet. Het streefcijfer 9,0 is niet gehaald.

### 1. Helderheid van de uitleg (8,5)

*Goed.*
- Theorie/Myopic loss aversion: formule en getal staan naast elkaar (5,75% benaderd, 6,14%
  exact bij een jaar), en de tabel laat de benadering over alle horizonnen zien.
- Theorie/DSSW: het voorbeeld van één periode (0,95 tegen 0,90; 2,5 tegen 0,5 stuks; −0,19
  tegen 0,0125) maakt "meer verdienen en toch slechter af" concreet voordat de propositie komt.
- Theorie/Joint hypothesis: de bewering staat vooraan ("twee beschrijvingen van hetzelfde
  getal") en $\varrho$ krijgt een eigen symbool om botsing met $\rho_t$ te vermijden.

*Aanmerkingen.*
- Theorie/DSSW (363): "Jongeren kiezen hun positie $\lambda_t$ om $\E_t[w] - \gamma\Var_t(w)$ te
  maximaliseren" — $\lambda$ was tot hier de verliesaversie 2,25, en de regel 366–368 waarschuwt
  wel voor $\gamma$ en $\mu$ maar niet voor $\lambda$ en $r$.
- Theorie/Myopic loss aversion (311–312): "en daalt de evaluatieperiode bij een gegeven premie
  met het kwadraat van die premie" — "bij een gegeven premie" en "met die premie" spreken
  elkaar tegen; bedoeld is dat $h^{*}$ daalt met het kwadraat van de premie.
- Replicatie/Benartzi-Thaler (1104–1105): "De reële waarde ligt net onder de verwachte
  ondergrens van een half jaar, terwijl $\lambda = 2{,}5$ de periode naar 9,6 maanden brengt."
  — 9,6 is de nominale waarde, maar de zin gaat over de reële (7,6).
- Theorie/Joint hypothesis (747, 752): $\phi$ krijgt geen orde van grootte en bij
  $(1-\varrho\phi)$ staat geen getal (H4).

*Beter uitleggen.* De lezer ziet in de simulatie 6,8 maanden bij 4,87% en herinnert zich uit
de theorie een jaar bij 6%. Zonder een zin over het verschil (volledige CPT met kansweging en
kromming, obligaties met 7,5% volatiliteit in plaats van een risicovrije belegging, logs)
lijkt de simulatie de propositie tegen te spreken. Een getal bij $(1-\varrho\phi)$, bijvoorbeeld
$\varrho = 0{,}96$, $\phi = 0{,}94$ geeft ongeveer 0,10, maakt de coëfficiënt van
[](#eq-behavioral-joint) tastbaar.

*Voor een 9.* Kondig in de DSSW-opzet $\lambda^{j}_t$ en $r$ aan (04_23_behavioral.md:363–368);
herschrijf 311–312 en 1104–1105; zet één zin over de drie premies aan het begin van de
simulatie (800–803); geef $\phi$ een orde van grootte (746–747).

### 2. Opbouw en rode draad (8,5)

*Goed.*
- Overzicht stelt de vraag en geeft in de tweede zin het antwoord, inclusief het voorbehoud
  (risico en vergissing zijn niet te scheiden).
- Routekaart aan het begin van Theorie en Samengevat aan het eind; de simulatie volgt direct
  uit de laatste bullet.
- 5479 woorden, ruim onder de grens; het toy (munt) keert terug in oefening 1 en de parameters
  in de simulatie.

*Aanmerkingen.*
- Intuïtie (100–101): "Verder verwachten we dat een extra schok de prijs harder omlaag duwt als
  arbitrageurs veel hebben ingezet." — het resultaat (702–704) varieert $a$, niet de inzet
  $D_1$: "Een extra schok duwt de prijs dus harder omlaag naarmate inleggers sneller vluchten".
- Simulatie (844): "Bij de premie van 1926–1990, 4,87% per jaar in logs, is $h^{*} = 6{,}8$
  maanden." — de toy- en theoriegetallen (6%, een jaar) keren hier niet terug, en de afwijking
  in richting wordt niet benoemd (H11).

*Beter uitleggen.* Welke premie waar geldt: 6% (rekenvoorbeeld), 4,87% (log, 1926–1990, bron
van de momenten), 6,7% (rekenkundig, S&P 500 min langlopende obligaties). Eén zin per
overgang volstaat.

*Voor een 9.* Laat intuïtie en resultaat bij Shleifer-Vishny over dezelfde grootheid gaan
(04_23_behavioral.md:100–101 of 702–704); verbind de premie van de simulatie met die van de
theorie (800–803, 844).

### 3. Taal (8,5)

*Goed.*
- `prose_stats` schoon: gemiddelde zin 16,1, p90 26, geen zin boven 40, alinea gemiddeld 44,
  geen gedachtestreepjes, geen u/je, geen "Wie"-openingen.
- Motiefnamen elk één keer ("theorie of feit" 65, "de standaardfout van 2%" 797, "Risico of
  vergissing?" 1164), telkens met betekenis.
- De redactie heeft de verwijswoorden rechtgezet ("haar" voor zaken is weg) en de
  "In de figuur gaat het om"-reeks gevarieerd.

*Aanmerkingen.*
- Theorie/DSSW (466–468): "Ze verdienen dus meer en zijn toch slechter af, en daarmee klopt ook
  het tweede vermoeden uit de intuïtie." — genummerde verwachting en de derde vorm van dezelfde
  vaste wending (ook 317 en 773).
- Replicatie/De Bondt-Thaler (971–974): "Over 1933–1980 verdient het gelijkgewogen
  decielverschil 1,36% per maand ($t = 3{,}45$) en de factor 0,38% ($t = 1{,}95$)." — samen
  met de volgende zin zeven getallen in één alinea (≤ 3).
- Replicatie/Benartzi-Thaler (1102–1109): twee alinea's met elk vier tot zes getallen.
- Wat er brak (1160–1161): "De evaluatieperiode van Benartzi en Thaler ligt binnen twee
  standaardfouten van de premie ergens tussen 2,5 en 41 maanden." — "ligt binnen … ergens
  tussen" leest als twee zinnen in elkaar.
- Overzicht (64–66): "In de termen van theorie of feit zijn dit geen modellen die een toets
  verwerpt, maar concurrerende verklaringen" — "in de termen van" plus enkelvoud "verwerpt"
  bij "modellen" leest stroef.

*Beter uitleggen.* Geen inhoudelijk punt; alleen de getallenlast en de vaste terugverwijzingen.

*Voor een 9.* Getallen uit 971–974, 1102–1105 en 1107–1109 naar de tabellen of naar
hoogstens drie per alinea; de drie intuïtie-terugverwijzingen (317, 467–468, 773) elk anders
en zonder nummer; 1160–1161 en 64–66 herschrijven (zie hardop-toets).

### 4. Toy-voorbeeld (9,0)

*Goed.*
- In vijf minuten na te rekenen: twee machten, drie producten, en de tabel hand/code staat
  naast elkaar met een assert in de cel.
- De slotzin zegt wat het getal betekent (bijna acht keer minder erg in één keer afgerekend) en
  verbindt het met de theorie.
- Het tweede toy (DSSW, één periode) volgt hetzelfde recept.

*Aanmerkingen.*
- Toy (142–144): "Een kans van een half telt bij hen als 0,4206 voor een winst en als 0,4540
  voor een verlies" — de kansweging is een tweede mechanisme met een formule die pas in de
  theorie komt ([](#eq-behavioral-weging)).

*Beter uitleggen.* Niets wezenlijks; de kansweging kan als "ter vergelijking" gemarkeerd
blijven.

### 5. Code en figuren (8,5)

*Goed.*
- `cpt_equal` en `repeated_bet` lezen als de wiskunde; de DSSW- en SV-functies benoemen hun
  tussenresultaten (`gap`, `lam_i`, `excess`, `prices`, `foc`).
- Elke figuur heeft een zin ervoor en een onderschrift dat zegt wat te zien is.

*Aanmerkingen.*
- Simulatie (816–819): `for i in range(0, len(m), 50):  # blokken van 50 parametersets houden
  het geheugengebruik klein` met 3-D broadcasting en `reshape` — compacter dan de wiskunde.
- Replicatie (1070, 1079): `boot_idx = rng.integers(0, 10**9, ...)` en `idx = boot_idx %
  len(data)` — truc om dezelfde trekkingen over steekproeven van ongelijke lengte te
  hergebruiken, niet uitgelegd.
- Replicatie (983–984): `dbt_windows` met `.year.map(lambda …)` en `groupby(...).apply(lambda
  x: (1 + x).prod() - 1)` in één regel; 696 idem voor de SV-tabel.

*Beter uitleggen.* Eén zin vóór de bootstrapcel over waarom de indices modulo de
steekproeflengte worden genomen.

*Voor een 9.* Splits 983–984 en 696 in benoemde tussenstappen en licht de modulo-truc toe
(04_23_behavioral.md:1062–1063, 1070).

### 6. Replicatie en empirie (8,5)

*Goed.*
- Twee admonitions met bron, wat, data, verschil en verwachte afwijking; tabel origineel/hier
  bij beide.
- Oordelen "Geslaagd" en "Gedeeltelijk geslaagd" staan vooraan en verwijzen naar de verwachte
  afwijking (volatielere obligatiereeks).
- De controle dat LT_Rev uit de zes portefeuilles volgt (0,0001) en de ±2 SE-kolommen maken van
  de replicatie een les over meetfout.

*Aanmerkingen.*
- Benartzi-Thaler, Verschil (1054–1055): "We rekenen de CPT-waarde bovendien exact uit in plaats
  van op twintig punten van de verdeling." — niet juist, zie Feitelijke fouten.
- Getallen in lopende tekst (971–980, 1102–1109), zie taal.
- Simulatie (800–801): "Het gemiddelde en de volatiliteit komen uit 1926–1990." — zonder bron
  voor 9,35%, 20,32%, 4,48% en 7,53%.

*Beter uitleggen.* Waarom het gelijkgewogen decielverschil de maatstaf voor "Geslaagd" is
terwijl de factor over zestien perioden $t = 1{,}66$ haalt: één bijzin volstaat.

*Voor een 9.* "exact" corrigeren (04_23_behavioral.md:1054–1055), bron bij de momenten
(800–801), getallen uit de proza naar de tabellen (971–980, 1102–1109).

### 7. Oefeningen (9,0)

*Goed.*
- Instap is een variatie op het toy (oefening 1), oefening 3 is een afleiding, oefening 4 breidt
  de replicatie uit en levert het januari-argument dat Wat er brak gebruikt.
- Elke uitwerking eindigt met wat ze leert.

*Aanmerkingen.*
- Oefening 3, vraag 3 ("Gebruik (2) om de onzekerheid in $h^{*}$ uit te drukken") wordt in de
  uitwerking met de benadering direct uitgerekend, niet via (2).

*Beter uitleggen.* Niets wezenlijks.

## Feitelijke fouten

Nagerekend tegen de celuitvoer: alle getallen in toy, theorie, DSSW-voorbeeld en -simulatie,
Shleifer-Vishny, simulatie, beide replicaties en de oefeningen kloppen met de uitvoer of met de
hand (o.a. $\kappa = 0{,}675$, wortels 0,183 en 0,492, maximum 0,0354, $\mu_{\min} = 0{,}222$,
$\lambda = 2{,}34$ en 88,9, $h^{*}$ 23,5/11,1/6,4, SE 2,3 p.p. = $12 \times 0{,}375/1{,}954$). Alle
afleidingen (BT-benadering, DSSW-prijs en -rendementsverschil, SV-prijs en -voorwaarde, joint
hypothesis) opnieuw doorgerekend: juist.

1. **Onjuist (klein).** 04_23_behavioral.md:1054–1055, "We rekenen de CPT-waarde bovendien exact
   uit". De cel (1070–1081) rekent op 20 000 bootstraptrekkingen per horizon; dat is een
   Monte-Carlo-benadering, geen exacte waarde. Voorstel: "op 20 000 getrokken reeksen in plaats
   van op twintig punten van de verdeling".
2. **Niet herleidbaar.** 800–801 en cel 8: de momenten 9,35%, 20,32%, 4,48%, 7,53% (en daaruit
   4,87% en 6,8 maanden) hebben geen bron. Bron noemen (vermoedelijk Benartzi-Thaler 1993,
   of Ibbotson) of afleiden uit `gw`.
3. **Onzeker.** 1045–1046, "tussen 9 en 13 maanden, en zonder kansweging en met een lineaire
   waardefunctie op 8 maanden" — niet in F23 tegen NBER w4369 nagekeken (feiten-bestand, rij
   14 dekt alleen 6,5% en 1,4%).

## Navertelling in vijf zinnen

Verliesaverse beleggers weigeren een gunstige gok die ze in een bundel wel aannemen, en als ze
hun portefeuille elk jaar bekijken, eisen ze ongeveer de historische aandelenpremie. Arbitrageurs
drukken verkeerde prijzen niet weg, omdat het sentiment van morgen onvoorspelbaar is (DSSW) en
inleggers na een verlies hun geld terugtrekken (Shleifer-Vishny), zodat een schok zichzelf
versterkt. Noise traders kunnen zo meer verdienen en bij gematigd optimisme zelfs overleven,
maar dat zien we pas na een eeuw of meer. Een voorspelbaar rendement na een lage prijs ziet er
bij risico en bij vergissing hetzelfde uit, dus prijzen alleen beslissen de vraag niet. In de
data vinden we de omkering en de korte evaluatieperiode terug, maar de omkering is grotendeels
HML en januari, en de evaluatieperiode is vooral een schatting van een slecht gemeten premie.
Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft de zichtbare sjablonen weggehaald en de verwijswoorden rechtgezet; het college
leest grotendeels als gesproken academisch Nederlands. Wat overblijft zijn getallenrijke
replicatiealinea's en een vaste terugverwijzing naar de intuïtie die drie keer in een andere
vorm terugkomt. Geen vakterm is door de redactie van betekenis veranderd.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. 04_23_behavioral.md:466–468: "Ze verdienen dus meer en zijn toch slechter af, en daarmee
   klopt ook het tweede vermoeden uit de intuïtie."
   → "Ze verdienen dus meer en zijn toch slechter af, omdat ze vijf keer zoveel risico dragen
   voor vijf keer zoveel winst."
2. 04_23_behavioral.md:1160–1161: "De evaluatieperiode van Benartzi en Thaler ligt binnen twee
   standaardfouten van de premie ergens tussen 2,5 en 41 maanden."
   → "Schuift de premie twee standaardfouten op, dan loopt de evaluatieperiode van Benartzi en
   Thaler uiteen van 2,5 tot 41 maanden."
3. 04_23_behavioral.md:200–201: "De belegger vindt hetzelfde risico dus bijna acht keer minder
   erg als hij het in één keer afrekent."
   → "Rekent de belegger de twee worpen in één keer af, dan weegt hetzelfde risico bijna acht
   keer zo licht."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Gelezen: plannen/kaart-rollen.md (§4, §5, §6, §8), dit bestand volledig, notes/rapport-04_23_behavioral.md
sectie "R9-1 (F6b, ronde 9+)", en het college (lectures/04_23_behavioral.md) volledig, één keer.
Getallen gecontroleerd tegen `tools/nb_outputs.py` (`$TEMP/F6c-04_23_behavioral-out.txt`) en tegen de hand:
4,87%/6,8 maanden (cel "premie 1926-1990"), 6,68→6,7% en 7,50/5,69→7,5/5,7 maanden (BT-tabel), 81%/t=2,20
(deciel 1-10 gelijkgewogen, 80,662/2,197), 0,375/1,954 en 2,3 p.p. SE, 0,0001 (LT_Rev uit zes), 0,15%/t=1,08
(1981-2026, 0,148/1,075), FF3-alpha −0,03%/HML 0,78, en met de hand $1-0{,}9638\cdot0{,}941=0{,}093$. Alle
kloppen. De momenten 9,35/20,32/4,48/7,53% staan alleen in code (`MOMENTS_1926_1990`), niet in de proza, en
de tekst noemt nu de bron (Goyal-Welch 1926–1990) — geen niet-herleidbaar getal meer. Geen nieuw of
verslechterd getal gevonden.

**Feitelijke fouten (F6).**
1. "exact" (1054–1055): **opgelost**. De Verschil-regel zegt nu "op 20 000 getrokken reeksen per horizon
   in plaats van op twintig punten van de verdeling", en `N_BOOT = 20_000` in de code klopt daarmee.
2. Niet herleidbaar, momenten (800–801): **opgelost**. Bron (Goyal-Welch 1926–1990) staat er nu bij; de
   getallen zelf blijven codeconstanten, zoals bij elke andere hyperparameter.
3. Onzeker, 9–13 en 8 maanden (1045–1046): **niet opgelost**. Niet na te gaan zonder de pdf van NBER
   w4369; onveranderd, geen feitelijke fout aangetoond.

**Drie verbeteringen.**
1. Symbolen/drie premies: **opgelost**. De DSSW-opzet kondigt $\lambda^{j}_t$ als positie en $r$ als
   dividend = risicovrije rente aan (367–373); de joint hypothesis zegt dat $r_{t+1}$ daar het log
   rendement is. Na de eerste simulatiecel staat nu een alinea (863–868) die 4,87% (log, simulatie) aan
   6,7% (rekenkundig, replicatie) koppelt en zegt waarom $h^{*}$ hier toch korter is dan het jaar uit de
   theorie (risicovolle obligatie, volledige CPT).
2. Getallen replicatieproza / "exact": **opgelost**. De DBT- en beide BT-alinea's dragen nu hoogstens drie
   getallen; "9,6 maanden" is vervangen door een verwijzing naar de kolom $\lambda = 2{,}5$.
3. Terugverwijzingen intuïtie: **opgelost**. Vier verschillende vormen zonder nummer (Myopic, DSSW-toy,
   Shleifer-Vishny, joint), en intuïtie en resultaat bij Shleifer-Vishny gaan nu beide over de snelheid
   waarmee inleggers vluchten ($a$, 100–101 en 713–715).

**Voor een 9, per criterium.**
- Helderheid: DSSW-aankondiging, 311–312, 1104–1105 en $\phi$/$(1-\varrho\phi)$ (Cochrane 2008: 0,9638,
  0,941, 0,093) — alle vier **opgelost**.
- Opbouw: Shleifer-Vishny-intuïtie en -resultaat over dezelfde grootheid, premie simulatie aan premie
  theorie verbonden — beide **opgelost**.
- Taal: getallen uit 971–974/1102–1109 naar de tabellen of ≤3 per alinea, drie terugverwijzingen gevarieerd,
  1160–1161 en 64–66 herschreven — alle **opgelost** (1160–1161 en 200–201 vrijwel letterlijk de
  hardop-toets-suggestie; 466–468 anders opgelost, met de reden direct genoemd in plaats van een
  terugverwijzing).
- Code en figuren: DBT-cel gesplitst (`months`, `window`, `compound`), modulo-truc toegelicht (prozaalinea
  1098–1102 en codecommentaar) — **opgelost**.
- Replicatie: "exact" gecorrigeerd, bron bij de momenten, getallen naar de tabellen — **opgelost**.

**Aanmerkingen zonder "Voor een 9".** Toy (kansweging) en Oefening 3 (vraag 3 nu expliciet via (2), met
aparte uitwerking) zijn beide aangepast; deze criteria stonden al op 9,0 en blijven dat (plafond).
De niet in "Voor een 9" genoemde aanmerking over de broadcasting/reshape in de simulatiecel (816–819) is
deels verbeterd met een toegevoegd commentaar bij de vorm van `x`, maar dat was geen voorwaarde voor 9,0.

**Hardop-toets.** Alle drie geciteerde zinnen herschreven; 1160–1161 en 200–201 vrijwel letterlijk de
voorgestelde herformulering, 466–468 anders maar zonder de genummerde "tweede vermoeden"-verwijzing.

Geen verslechtering en geen nieuwe feitelijke fout gevonden. Alle "Voor een 9"-punten van de vijf
criteria met een concreet actiepunt zijn opgelost; alleen feitelijke fout 3 (onzeker, structureel niet
natrekbaar) blijft open en raakt geen van de zeven criteria rechtstreeks.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Eindcijfer (gewogen)** | | **9,0** |

Geen deelcijfer onder 8,5; taal blokkeert niet. Streefcijfer 9,0 gehaald.
