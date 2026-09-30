STATUS 04_21_volatiliteit F6c words=5796 prose=PASS open=0 cijfer=9,1 min=9,0

**Eindcijfer van record: 9,1** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,8 -> F6c 9,1.

# Eindbeoordeling 04_21_volatiliteit

## Eerste herziening (workflow §12)

Eerste herziening van dit college; er is geen vorig cijfer. Gelezen: de volledige .md
(na F1, F23 en F4T), notes/taal-04_21_volatiliteit.md, de celuitvoer via
`tools/nb_outputs.py`. `prose_stats --check`: PASS (5.639 woorden, zinslengte 17,1,
geen zin boven 40, alinea 43, 1 stopwoord, 3 dubbele punten midden in de zin).

## De drie verbeteringen met het meeste effect

1. **Vier fouten in vaktermen en beweringen herstellen** (zie "Feitelijke fouten"): de
   VIX is de *wortel* van de risiconeutrale verwachte variantie (r. 429 en 563),
   *realized volatility* is geen som van kwadraten maar de wortel ervan (r. 58–60), het
   negatieve teken paste niet bij French, Schwert en Stambaugh (r. 1451 tegen r. 497–499),
   en Merton voorspelde niet dat volatiliteit voorspelbaar is, alleen dat ze meetbaar is
   (r. 1292–1294). Verwacht deelcijfer helderheid: 8,5 → 9,0; oefeningen 9,0 → 9,5.
2. **Taal afmaken**: de ontbrekende punt in r. 1053 ("maandvariantie Voor de logaritme"),
   "haar voorspellingen" voor een zaak in de figuurtitel (r. 1076), en de drie zinnen uit
   de hardop-toets hieronder (r. 1298, 1302–1303, 1441). Verwacht deelcijfer taal:
   8,5 → 9,0.
3. **Replicatie-oordelen expliciet maken**: GARCH/GJR (r. 911) en HAR-RV (r. 1052–1062)
   hebben geen oordeel dat met Geslaagd / Gedeeltelijk / Niet geslaagd begint, en bij HAR
   ontbreekt dat "vorige maand" in niveaus en logs een hogere $R^2$ haalt dan HAR-RV (0,173
   tegen 0,162; 0,422 tegen 0,414), wat de verwachte afwijking ("slechter dan beide") maar
   half waarmaakt. Verwacht deelcijfer replicatie: 8,5 → 9,0.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,8

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Gewogen eindcijfer** | | **8,8** (8,775) |

Het streefcijfer (≥ 9,0, geen deelcijfer onder 8,5) is nog niet gehaald; taal (8,5)
blokkeert niet.

### 1. Helderheid van de uitleg — 8,5

*Goed.*
- Opzet: ARCH en GARCH: het waarom is een handeling ("schat een belegger de variantie van
  morgen het best met recente gekwadrateerde schokken") en de vergelijking volgt eruit.
- Het kernresultaat: getal naast de formule (φ = 0,9 met 6,58 dagen in het toy, 0,989 met
  61 dagen in de replicatie) en een economische consequentie (maandhorizon tegen
  jaarhorizon, langetermijnbelegger tegen risicomanager).
- Risico en rendement: de vuistregel rekent de 700 maanden uit en koppelt ze aan de
  standaardfout van 2%, met de reden (het rendement staat links en neemt zijn ruis mee).

*Aanmerkingen.*
- Overzicht, r. 58–60: "Daarna maakte *realized volatility* (gerealiseerde volatiliteit,
  de som van gekwadrateerde intradagrendementen) de variantie bijna waarneembaar" — de som
  van kwadraten is de gerealiseerde *variantie*; de volatiliteit is de wortel.
- De VIX als prijs van een variance swap, r. 429: "De VIX is de risiconeutrale verwachting
  van de variantie over de komende dertig dagen" — de stelling zelf (r. 452) zegt terecht
  $\mathrm{VIX}^2$; de VIX is de wortel, op jaarbasis en in procenten.
- Gerealiseerde variantie en HAR-RV, r. 411: "Gerealiseerde volatiliteit dooft langzamer
  uit dan de meetkundige daling van GARCH." — binnen twee alinea's wisselen "realized
  variance", "gerealiseerde variantie" en "gerealiseerde volatiliteit" voor wat telkens de
  variantie is (H7).
- De VIX als prijs van een variance swap, r. 472–474: "Dat de VIX gemiddeld boven de latere
  volatiliteit ligt, is de variance risk premium uit [](#fig-black-scholes-vrp)." — het
  begrip wordt geleend zonder regel uitleg (H2).
- Wat er brak, r. 1292–1294: "Dat volatiliteit voorspelbaar is en rendementen nauwelijks,
  is een feit dat Mertons wiskunde in [](#00-01-rendementen) al voorspelde." — Merton
  toonde dat de variantie *meetbaar* is (zo staat het ook in r. 24–25), niet dat ze
  voorspelbaar is.
- Simulatie, r. 846–848: "... pas na 150 jaar in ruim driekwart, zoals de vuistregel liet
  verwachten." — de vuistregel (r. 533) noemt bijna zestig jaar, het Overzicht (r. 40)
  "meer dan zeventig jaar"; nergens staat waarom de simulatie langer nodig heeft
  (Student-$t$-schokken, gewogen schatter).

*Beter uitleggen.* De lezer moet bij de VIX weten dat het getal een volatiliteit op
jaarbasis is, en bij de variance risk premium in één zin wat die premie is (VIX² min de
latere gerealiseerde variantie, gemiddeld positief). Het verband tussen de "bijna zestig
jaar" van de vuistregel en de "meer dan zeventig jaar" van de simulatie vraagt één
bijzin.

*Voor een 9.* lectures/04_21_volatiliteit.md:58–60 (realized variance),
:429 en :563 (VIX²), :411 en :366–369 (één naam voor de variantiemaat), :474 (variance risk
premium in één regel), :1292–1294 (meetbaar, niet voorspelbaar), :846–848 en :40 (60
tegen 70 jaar verbinden).

### 2. Opbouw en rode draad — 9,0

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in twee zinnen (voorspelbaar; beloning te
  klein tegenover de ruis).
- De intuïtie voorspelt drie dingen (terugzakken naar een vast niveau, asymmetrie, kleine
  positieve helling) en elk komt terug: r. 295–297, r. 356–358, r. 527–529.
- Toy-getallen keren terug: φ = 0,9 en 6,58 dagen in Theorie, $\alpha = 0{,}10$ in de
  simulatie, $h_4 = 0{,}762$ en 1,5596 in oefening 1. Routekaart en Samengevat staan op hun
  plaats; 5.639 woorden.

*Aanmerkingen.*
- Overzicht, r. 39–40: "een toets zelfs met de ware variantie meer dan zeventig jaar data
  nodig heeft" tegenover Theorie, r. 533: "bijna zestig jaar, en dat met de ware variantie"
  — twee getallen voor dezelfde boodschap zonder verbinding.

*Beter uitleggen.* Niets meer dan de koppeling hierboven; de lijn beschrijving → toets is
helder.

### 3. Taal — 8,5

*Goed.*
- Zinslengte gemiddeld 17,1 met afwisseling, geen zin boven 40, alinea's gemiddeld 43
  woorden; verband met voegwoorden ("want", "zodat", "terwijl").
- De redactie heeft de "haar"-fouten in de lopende tekst en de sjabloonopeningen goed
  opgeruimd; motiefnamen elk hoogstens één keer.
- Geen vakterm is door de taalredactie een alias geworden voor een ander begrip; de
  term-fouten hieronder bij "Feitelijke fouten" zijn inhoudelijk (zie daar).

*Aanmerkingen.*
- Replicatie, HAR-RV tegen GARCH, r. 1052–1053: "verklaren de modellen 16 tot 24% van de
  variatie in het niveau van de volgende maandvariantie Voor de logaritme is dat 41 tot
  48%" — punt ontbreekt.
- Replicatie, HAR-RV tegen GARCH, r. 1076 (figuurtitel): "Maandelijkse gerealiseerde
  volatiliteit en haar voorspellingen" — "haar" voor een zaak (§11.12).
- Oefeningen, r. 1441: "De Student-$t$-versie wint ruim achthonderd punten log-likelihood
  met ongeveer zes vrijheidsgraden." — "wint ... met" leest als de marge.
- Wat er brak, r. 1298: "Het model breekt twee keer op een handvol extreme dagen of
  maanden."
- Wat er brak, r. 1302–1303: "Zelfs met de ware variantie is meer dan zeventig jaar nodig om
  vaker wel dan niet significant te zijn." — het onderwerp ($\gamma$) ontbreekt.

*Beter uitleggen.* Zie de hardop-toets onderaan.

*Voor een 9.* lectures/04_21_volatiliteit.md:1053, :1076, :1298, :1302–1303, :1441.

### 4. Toy-voorbeeld — 9,5

*Goed.*
- Vier dagen, één mechanisme, zeven genummerde handstappen die in vijf minuten na te
  rekenen zijn; alle getallen kloppen met de celuitvoer.
- Tabel hand/code met assert; slotzin zegt wat het getal betekent (ruim drie keer het
  langetermijnniveau, halvering pas na 6,58 dagen).
- Stap 6 en 7 geven de meerstapsvoorspelling vóór de stelling, zodat het theorema herkenning
  wordt.

*Aanmerkingen.*
- Toy-voorbeeld, r. 127: "Het recept, dat de theorie straks als eerste afleidt" — de
  theorie motiveert GARCH (r. 195–199) maar leidt het niet af; "als eerste invoert" dekt het.

*Beter uitleggen.* Niets.

### 5. Code en figuren — 9,0

*Goed.*
- Elke cel heeft een aankondiging en een zin erna; de toy-cel en de simulatielus lezen als
  de recursie.
- Figuren hebben een bijschrift dat zegt wat te zien is (sim-garch, garch-markt met de
  sprong van 2% naar 6 à 7%, midas met de cumulatieve gewichten).
- De crashtabel rond 19 oktober 1987 maakt het "blind voor de eerste dag" direct zichtbaar.

*Aanmerkingen.*
- Simulatie, r. 742–743: `expected_s = ...` en `H_BAR * expected_s * (DAYS_M + (g - 1) * geometric.sum())`
  — de ware maandvariantie (lognormale verwachting van $s$ plus de meetkundige som van de
  GARCH-component) staat nergens in de proza; r. 736–737 zegt alleen "legt de vier
  voorspellingen vast".
- Replicatie, r. 1076: figuurtitel met "haar" (zie taal).

*Beter uitleggen.* Eén zin vóór de cel die zegt dat de ware maandvariantie de verwachting
is van $s$ maal de som van de verwachte dagvarianties, met dezelfde meetkundige daling als
in [](#eq-volatiliteit-kstap).

### 6. Replicatie en empirie — 8,5

*Goed.*
- Drie admonitions met bron, wat, data, verschil en verwachte afwijking; elk ruim onder
  250 woorden.
- GARCH/GJR: tabel origineel/hier met persistentie, halfwaardetijd, $\delta$ en $\alpha$.
- MIDAS: de uitvoertabel zet GSV en hier naast elkaar, en de analyse zonder 1929–1933
  (1,97, $t = 1{,}6$) wijst de oorzaak aan.

*Aanmerkingen.*
- GARCH en GJR, r. 911: "Beide kernresultaten komen terug, want de persistentie ligt
  tussen 0,97 en 1 ..." — geen oordeel dat met Geslaagd begint.
- HAR-RV tegen GARCH, r. 1052–1057: geen oordeel (Geslaagd / Gedeeltelijk), en "Alleen de
  voorspelling "vorige maand" doet het slechter dan het historische gemiddelde" verzwijgt
  dat "vorige maand" in niveaus en logs boven HAR-RV uitkomt, terwijl de verwachte
  afwijking "slechter dan beide" zei.
- Ghysels, Santa-Clara en Valkanov, r. 1242–1248: zeven getallen in twee alinea's die al in
  de tabel staan ("0,83 geven met $t = 0{,}8$", "0,45 voor één maand en 0,75 à 1,0").

*Beter uitleggen.* Bij HAR welk deel van de verwachting uitkomt en welk niet; bij MIDAS de
getallen in de tabel laten staan en in de proza alleen de rangorde en het teken noemen.

*Voor een 9.* lectures/04_21_volatiliteit.md:911, :1052–1062, :1242–1248.

### 7. Oefeningen — 9,0

*Goed.*
- Instap (oefening 1, GJR op het toy, gemiddelde precies 1,5596), afleiding (oefening 2,
  kurtosis en $\rho_1$, met simulatie die klopt: 3,162 tegen 3,166), twee uitbreidingen van
  de replicatie (oefening 3 en 4).
- Elke uitwerking sluit met een les (GARCH middelt, staarten zijn een aparte keuze, de
  prijs hangt af van extreme maanden).

*Aanmerkingen.*
- Oefening 4, r. 1450–1451: "Dat negatieve teken paste bij French, Schwert en Stambaugh."
  — r. 497–499 zegt dat zij een positief verband vonden (zie Feitelijke fouten).

*Beter uitleggen.* Niets buiten de correctie.

## Feitelijke fouten

Alle getallen in de proza zijn nagerekend tegen $TEMP/F6-04_21_volatiliteit-out.txt en
kloppen (toy; 0,213; 0,21% en ruim twintig keer; 0,0015 en 0,45; 1,7/2,0/2,2 en RMSE ≈ 1,3;
0,462 en 0,773; 0,989/0,983, 61/41, 0,113 (9,8), 0,105/0,036, ruim vier keer; 2,1/2,4,
−17,4, −7,2, 7,1; 16–24% en 41–48%, GJR best in alle drie; 0,19 ($t$ 0,17), 0,83 ($t$ 0,77),
0,45, 0,75–0,99, 2,85 ($t$ 1,5), 1,97 ($t$ 1,6); ruim achthonderd punten, ν = 5,9, 56 jaar;
0,51/0,64, 1,28 en 2,06 ($t$ 2,0), elf maanden). Nagerekend met de hand: 700 maanden
(711), $\rho_1 = 0{,}277$, 50% en 21% gewicht, factor drie voor $t = 6{,}7$, GSV-gewichten
31% / 74% / 86% na één, drie, vier maanden, identiteiten in oefening 2 en de VIX-afleiding.

1. r. 429 en r. 563: "De VIX is de risiconeutrale verwachting van de variantie" — onjuist;
   dat is $\mathrm{VIX}^2$ (zoals r. 452 zelf schrijft). Correctie: "Het kwadraat van de
   VIX is ...". (In deze herziening herschreven.)
2. r. 58–60: *realized volatility* gedefinieerd als "de som van gekwadrateerde
   intradagrendementen" — onjuist; dat is de realized variance, de volatiliteit is de
   wortel. (Stond er al vóór de herziening.)
3. r. 1451: "Dat negatieve teken paste bij French, Schwert en Stambaugh." — in tegenspraak
   met r. 497–499 ("vonden een positief maar insignificant verband"). De vorige versie
   sprak van "de resultaten van French, Schwert en Stambaugh terugkrijgen"; de herschrijving
   heeft de betekenis veranderd. Correctie: het negatieve teken komt uit de herberekening
   van Ghysels, Santa-Clara en Valkanov met de schatter van French, Schwert en Stambaugh.
4. r. 1292–1294: "een feit dat Mertons wiskunde ... al voorspelde" — onjuist; Merton liet
   zien dat de variantie scherper te *meten* is dan het gemiddelde, niet dat ze voorspelbaar
   is. Correctie: "... en dat de variantie beter te meten is dan het gemiddelde, volgt al
   uit Mertons wiskunde".

Geen vakterm werd door de taalredactie een alias van een ander begrip (efficiënte grens,
persistentie, halfwaardetijd, QML, integrated variance zijn consistent); fout 3 is wel een
betekenisverandering bij het herschrijven.

## Navertelling in vijf zinnen

Volatiliteit klontert, en GARCH beschrijft dat met een variantie die elke dag een deel van
de laatste schok en van zichzelf meeneemt, zodat de voorspelling meetkundig met factor
$\alpha+\beta$ terugzakt naar een vast niveau. Op een eeuw Amerikaanse dagrendementen is die
persistentie 0,99 (halfwaardetijd twee tot drie maanden) en reageert de variantie ruim vier
keer sterker op dalingen dan op stijgingen, maar geen enkel model zag 19 oktober 1987
aankomen. Gerealiseerde variantie en de VIX meten de variantie scherper of vooruitkijkend,
en buiten de steekproef verklaren GARCH en HAR bijna de helft van de variatie in de
logaritme van de maandvariantie. De beloning voor variantie is daarentegen nauwelijks te
zien, omdat de ruis in het maandrendement zo groot is dat ook met de ware variantie meer
dan zeventig jaar nodig is en meetfout de helling naar nul drukt. Op de French-data slaagt
de MIDAS-replicatie niet ($\gamma = 0{,}19$), en de uitkomst hangt aan de jaren dertig.
Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijker gemaakt: de lopende tekst leest als gesproken
academisch Nederlands, de sjabloonopeningen zijn weg en "haar" voor zaken staat alleen nog in
een figuurtitel. Er is één slordigheid (ontbrekende punt, r. 1053). Hardop-toets, drie zinnen
die nog niet natuurlijk klinken:

1. r. 1441: "De Student-$t$-versie wint ruim achthonderd punten log-likelihood met ongeveer
   zes vrijheidsgraden." → "Met Student-$t$-schokken, die ongeveer zes vrijheidsgraden
   krijgen, stijgt de log-likelihood met ruim achthonderd punten."
2. r. 1298: "Het model breekt twee keer op een handvol extreme dagen of maanden." → "Het
   model schiet twee keer tekort, en beide keren door een handvol extreme dagen of maanden."
3. r. 1302–1303: "Zelfs met de ware variantie is meer dan zeventig jaar nodig om vaker wel
   dan niet significant te zijn." → "Zelfs met de ware variantie is $\gamma$ pas na meer dan
   zeventig jaar vaker wel dan niet significant."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Controle van `notes/rapport-04_21_volatiliteit.md`, sectie "R9-1 (F6b, ronde 9+)", tegen
het college en tegen `uv run python tools/nb_outputs.py lectures/04_21_volatiliteit.ipynb`.

**Feitelijke fouten.**
1. r. 429 en 563, VIX i.p.v. VIX² — opgelost. Overzicht, Theorie en Samengevat schrijven
   nu overal "het kwadraat van de VIX" als de risiconeutrale verwachte variantie.
2. r. 58–60, *realized volatility* gedefinieerd als som van kwadraten — opgelost. Nu "de
   gerealiseerde variantie (realized variance, de som van gekwadrateerde
   intradagrendementen, met als wortel de realized volatility)".
3. r. 1451, negatief teken toegeschreven aan French, Schwert en Stambaugh — opgelost.
   Oefening 4 zegt nu dat die auteurs zelf een positief verband rapporteerden en dat het
   negatieve teken uit de herberekening van Ghysels, Santa-Clara en Valkanov met hun
   schatter komt.
4. r. 1292–1294, Merton zou voorspelbaarheid hebben voorspeld — opgelost. "Wat er brak"
   scheidt nu meetbaarheid (Mertons wiskunde) van voorspelbaarheid (een apart feit).

**Drie verbeteringen.**
1. Helderheid — opgelost, alle zes "Voor een 9"-punten: RV/volatiliteit (58–60), VIX²
   (429/563), één naam "gerealiseerde variantie" (411, 366–369), variance risk premium in
   één zin (474), meetbaar-niet-voorspelbaar (1292–1294), en 60 tegen 70 jaar verbonden
   (846–848 met 40).
2. Taal — opgelost, alle vijf punten: de zin met de ontbrekende punt (1053) is herschreven
   zonder telegramstijl, de figuurtitel zegt "twee voorspellingen" in plaats van "haar"
   (1076), en de drie hardop-zinnen (1298, 1302–1303, 1441) zijn letterlijk volgens het
   voorstel herschreven.
3. Replicatie — opgelost, alle drie punten: GARCH/GJR opent met "Geslaagd" (911), HAR-RV
   met "Gedeeltelijk geslaagd" plus de aanvulling dat "vorige maand" in zowel niveau als
   logaritme boven HAR-RV uitkomt (1052–1062; celuitvoer bevestigt RV vorige maand
   0,173/0,422 tegen HAR-RV 0,162/0,414, en "vorige maand" als enige met een negatieve OOS
   $R^2$ t.o.v. het historisch gemiddelde), en de GSV-sectie opent met "Niet geslaagd"
   terwijl de zeven getallen uit de proza naar de tabel zijn verplaatst (1242–1248).

**Overige "Voor een 9"-punten en aanmerkingen.**
- Opbouw (r. 39–40 tegenover 533, geen koppeling): opgelost. Overzicht zegt nu expliciet
  "in de simulatie", en r. 841–843 verbindt de uitkomst met de "bijna zestig jaar" van de
  vuistregel en geeft de reden (de gewogen schatter geeft extreme maanden weinig gewicht).
  Geen hoger cijfer dan de bestaande 9,0 was beloofd, blijft 9,0.
- Toy (r. 127, "afleidt"): opgelost, nu "als eerste invoert". Was al 9,5 zonder hoger
  cijfer in het vooruitzicht, blijft 9,5.
- Code en figuren (r. 742–743, ware maandvariantie niet in de proza): opgelost, de zin
  voor de cel (r. 730–733) legt nu uit dat de ware maandvariantie de verwachte $s$ maal de
  som van 22 verwachte dagvarianties is, met dezelfde meetkundige daling als
  [](#eq-volatiliteit-kstap). Geen hoger cijfer dan de bestaande 9,0 was beloofd, blijft
  9,0.

**Nieuwe punten.** Geen. De herziening voegt geen nieuwe getallen toe; de enige nieuwe
kwalitatieve bewering (RV vorige maand boven HAR-RV in beide maten) is gecontroleerd tegen
cel 14 van `nb_outputs.py` en klopt. Geen verslechtering gevonden.

## Eindcijfer van record (F6c): 9,1

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,5 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,95 + 0,90 + 0,90 + 0,475 = 9,075 -> 9,1. Geen deelcijfer
onder 8,5; taal blokkeert niet. Gelijk aan het plafond van 9,1 uit F6.
