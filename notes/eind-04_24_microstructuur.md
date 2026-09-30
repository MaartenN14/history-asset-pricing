STATUS 04_24_microstructuur F6c words=5865 prose=PASS open=1 cijfer=9,0 min=8,5

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,6 -> F6c 9,0.

# Eindbeoordeling 04_24_microstructuur

## Eerste herziening (workflow §12)

Eerste F6-beoordeling van dit college; er is geen vorig cijfer. Gelezen: de volledige .md,
celuitvoer via `tools/nb_outputs.py`, `notes/taal-04_24_microstructuur.md` en de
statusregel van `notes/feiten-04_24_microstructuur.md` (open=1, Acharya-Pedersen 1,1%).
`prose_stats --check`: PASS (5667 woorden, zinslengte 19,4, alinea 53).

## De drie verbeteringen met het meeste effect

1. **Twee vaktermfouten in de theorie herstellen (helderheid 8,5 → 9,0).** De insider
   koopt niet "de helft van de positie die hij zonder prijsimpact zou willen" (zonder
   prijsimpact is die positie oneindig bij risiconeutraliteit), maar de helft van de
   positie $(v-p_0)/\lambda$ waarbij de prijs tot $v$ zou stijgen, zoals een monopolist
   de helft van de concurrerende hoeveelheid levert (04_24_microstructuur.md:313 en
   :390–391). In de Glosten-Milgrom-sessie heet $\E[V\mid\mathcal F_n]$ "middenkoers",
   terwijl de middenkoers $(a+b)/2$ daar in het algemeen van afwijkt (na één koop 100,385
   tegen 100,40) (:604, :622, :643). Tegelijk de 5% bij :1164 een herkomst geven (de alpha
   van 5,4% vóór 2003).
2. **Replicatie: getallen uit de lopende tekst naar de tabel en de verwachte afwijking
   compleet maken (replicatie 8,5 → 9,0).** De admonition noemt $g_1$ en de alpha van de
   factor bij "Wat", maar geeft er bij "Verwachte afwijking" geen verwachting voor
   (:932–935), terwijl het oordeel juist op die twee punten "gedeeltelijk" zegt
   (:1179–1182). De alinea's :1030–1034, :1107–1110 en :1159–1165 dragen elk drie tot vijf
   getallen die al in de tabel "Origineel en hier" staan of erin horen.
3. **Hardop-toets en de Engelse inline-quote (taal 8,5 → 9,0).** Drie zinnen (zie het
   taaloordeel onderaan) herschrijven, en de inline Engelse quote bij :1215–1216
   parafraseren of als blokcitaat met inleiding zetten.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,6

| criterium | gewicht | deelcijfer |
|---|---|---|
| 1 Helderheid | 25% | 8,5 |
| 2 Opbouw en rode draad | 20% | 9,0 |
| 3 Taal | 20% | 8,5 |
| 4 Toy-voorbeeld | 10% | 8,5 |
| 5 Code en figuren | 10% | 8,5 |
| 6 Replicatie en empirie | 10% | 8,5 |
| 7 Oefeningen | 5% | 9,0 |
| **Eindcijfer (gewogen)** | | **8,6** (8,625) |

### 1 Helderheid (8,5)

*Goed.* Het bewijs van Glosten-Milgrom rekent de spreadformule direct terug naar het toy
(0,80 en 0,77, "Glosten-Milgrom: de spread als adverse selectie"). Kyle één ronde heeft
stapkoppen die zeggen wat elke stap oplevert, en de naverteller-alinea erna geeft
20.000 euro en 16 → 8. Roll krijgt bij de formule meteen $-0{,}16$ en de orde $10^{-5}$.

*Aanmerkingen.*
- Kyle: het evenwicht met één handelsronde: "In het bewijs neemt de insider $\lambda$ als
  gegeven en koopt hij de helft van de positie die hij zonder prijsimpact zou willen."
  (:390–391) Onjuist: zonder prijsimpact is de gewenste positie oneindig. Ook
  "koopt daarom, net als een monopolist, minder dan zonder prijsimpact" (:313) zegt
  daardoor niets.
- Een Glosten-Milgrom-sessie: "De figuur toont links de krimpende spread en rechts zes
  middenkoersen" (:622–623); de reeks is $\E[V\mid\mathcal F_n]$, niet $(a+b)/2$.
- Kyle: het evenwicht met één handelsronde: "In de markt van Kyle bevat de prijs na één
  ronde precies de helft van de informatie van de insider" (:311). "Informatie" is hier
  de variantie; de zin zegt het pas bij :394.
- Pástor-Stambaugh: "zodat 22 jaar data een premie van 5% per jaar aantonen noch
  uitsluiten." (:1164–1165) Waar de 5% vandaan komt, staat er niet.
- Wat er brak: "Een risicopremie wordt in crises betaald en een vergissing verdwijnt na
  publicatie" (:1213). "In crises betaald" leest alsof de houder in crises iets ontvangt,
  terwijl hij dan juist verliest.

*Beter uitleggen.* De recursie van Kyle (:419–435) komt zonder één regel over wat
$\alpha_n$ doet vóór de formule; de uitleg staat pas bij :446. De stap in de numerieke
oplossing naar een derdegraadsvergelijking in $\lambda$ (codecommentaar :470) mist in de
tekst. Toy-stap 4 (:140–142) laat $0{,}36 = 0{,}6\cdot0{,}6$ en $0{,}52$ uit de lucht
vallen.

*Voor een 9.* 04_24_microstructuur.md:390–391 en :313 (positie waarbij de prijs $v$
bereikt); :604, :622, :643 ("verwachte waarde" of "prijs" in plaats van middenkoers);
:311 ("de helft van de onzekerheid, gemeten als variantie"); :1164 (herkomst 5%); :1213.

### 2 Opbouw en rode draad (9,0)

*Goed.* Overzicht stelt de vraag en geeft het antwoord inclusief het negatieve deel (premie
na publicatie weg). De intuïtie voorspelt vier dingen (spread grootst bij onzekerheid,
krimpt per order, illiquide hoger rendement, koersdaling bij onverwachte droogte), en
alle vier worden ingelost (:298, :399, :752–755, :1030). Toy-getallen keren terug in
Theorie (0,77, 20.000 euro), de GM-sessie en de Roll-simulatie (0,80 euro, $\rho_1$).

*Aanmerkingen.*
- Theorie (routekaart): "De theorie gaat in drie stappen van de handelsvloer naar
  verwachte rendementen." (:226) De vierde subsectie "Marktontwerp" (:804–814) valt buiten
  de routekaart en wordt later niet meer gebruikt.

*Beter uitleggen.* De Roll-schatting in de replicatie (60 tot 170 bp, :982–983) en het
selectie-effect uit de simulatie (:908–909) worden niet aan elkaar gekoppeld; dat is het
moment waarop de simulatie haar nut bewijst.

### 3 Taal (8,5)

*Goed.* PASS op alle tellingen; zinslengte 19,4 met afwisseling, geen gedachtestreepjes,
motiefnaam één keer bij naam en niet als onderwerp, vier of minder "Wie"-zinnen. De
redactie heeft verbanden met voegwoorden hersteld zonder vaktermen te vervangen; geen
geval zoals "de rand" gevonden.

*Aanmerkingen.*
- Glosten-Milgrom: "Zo krijgt de stelling van Samuelson uit [](#02-06-efficiente-markten),
  dat een prijs die een verwachte waarde is onvoorspelbaar verandert, een precieze
  informatieverzameling." (:305–307)
- Marktbrede illiquiditeit (figuur): "Onder zijn maart 2020 en oktober tot december 2008
  de grootste uitschieters, zodat de liquiditeit verdwijnt in de maanden waarin beleggers
  moesten verkopen." (:1064–1065)
- Wat er brak: "Wie illiquide activa houdt, verzekert dan de markt en krijgt daarvoor
  betaald, en dan was dat risico na 2003 kleiner of zien we alleen ruis." (:1205–1206)
- Wat er brak: *"should not assume he can sell them at the price in the last valuation
  report"* (:1215–1216), Engels inline, niet geparafraseerd en geen blokcitaat.

*Beter uitleggen.* Geen inhoudelijk punt; zie de herschrijvingen onderaan.

*Voor een 9.* :305–307, :1064–1065, :1205–1206 herschrijven; :1215–1216 parafraseren.

### 4 Toy-voorbeeld (8,5)

*Goed.* Twee tabellen met parameters, handstappen met getallen, tabel hand/code met
`assert`; de winstverdeling bij Kyle telt op tot nul en de zin erna zegt waarom het
verlies van de market maker toeval is.

*Aanmerkingen.*
- Glosten-Milgrom met één transactie: "Na een koop is het oordeel $0{,}6$ en de kans op
  een volgende koop $0{,}52$, zodat de laatkoers $98 + 4\cdot0{,}36/0{,}52 = 100{,}77$
  wordt" (:140–142). Twee tussengetallen zonder berekening.
- Toy-voorbeeld (slot): "De spread van 0,80 euro is wat een ongeïnformeerde klant voor een
  aan- en verkoop betaalt, alleen omdat een op de vijf handelaren de waarde kent." (:221–222)
  De slotzin duidt alleen het Glosten-Milgrom-deel; het Kyle-getal 0,0002 (2 euro per
  10.000 aandelen) krijgt geen betekenis-zin.

*Beter uitleggen.* Het toy bevat twee mechanismen; dat is verdedigbaar omdat beide
modellen de kern zijn, maar dan moet elk een eigen slotzin hebben.

*Voor een 9.* :140 ($0{,}6\cdot0{,}6+0{,}4\cdot0{,}4 = 0{,}52$ en $0{,}6\cdot0{,}6 = 0{,}36$
zichtbaar); :220–222 één zin over wat $\lambda$ voor de insider betekent.

### 5 Code en figuren (8,5)

*Goed.* Elke cel heeft een zin ervoor en erna; de simulatielussen van Kyle en
Glosten-Milgrom zijn zichtbaar en lezen als de recursie. Figuurteksten zeggen wat te zien
is.

*Aanmerkingen.*
- Numerieke oplossing: `# lambda solves -2 a s2 dt L^3 + 2 s2 dt L^2 + 2 a S L - S = 0`
  (:470) De kubische vergelijking staat niet in de tekst; `np.roots` met filter is een
  truc voor de lezer. Ook de terugschaling in `out.attrs["profit"]` (:483) is niet te
  volgen zonder afleiding.
- Figuur Roll: "Een langere steekproef helpt maar met een factor $\sqrt{T}$, zodat de curve
  van een kwartaal naar een jaar nauwelijks verschuift." (:900–902) Bij $s/\sigma_e =
  0{,}45$ daalt de fractie van 0,336 naar 0,206; "nauwelijks" geldt alleen in het grijze
  gebied.
- Kyle-figuur: `resid_var / 1.0` (:547) is een overbodige deling.

*Beter uitleggen.* Eén zin vóór de recursiecel die zegt dat de eerste twee vergelijkingen
samen een derdegraadsvergelijking in $\lambda_n$ geven en dat de wortel met
$\alpha_n\lambda_n < \tfrac12$ de tweede-ordevoorwaarde haalt.

*Voor een 9.* :452–455 (zin over de kubische vergelijking); :900–902 ("in het grijze
gebied nauwelijks"); :547.

### 6 Replicatie en empirie (8,5)

*Goed.* Admonition met alle vijf onderdelen, binnen 250 woorden; tabel origineel/hier met
zeven rijen; oordeel begint met "Gedeeltelijk geslaagd". De voor/na-publicatiesplitsing
van de alpha is een sterke, eerlijke toets.

*Aanmerkingen.*
- Replicatie (Verwachte afwijking): "Het teken van $g_2$ moet negatief zijn, met een
  $t$-waarde ruim boven twee in absolute waarde." (:932–935) Geen verwachting voor $g_1$
  (met 24 jaar van vijftig overlevers: niet significant) en voor de alpha (kleiner dan
  7,5 door historische bèta's), terwijl het oordeel juist daarop "gedeeltelijk" zegt.
- Marktbrede illiquiditeit: "met een overrendement dat ruim 13 procentpunt lager ligt in
  dezelfde maand, met een $t$-waarde van bijna $-8$." (:1031–1032) Getallen in proza die
  al in de tabel staan.
- Pástor-Stambaugh: "Sinds 2004 is de alpha $-0{,}8\%$ per jaar met een standaardfout van
  3%" (:1163–1164), niet in de tabel "Origineel en hier".
- Wat er brak: "elders een orde van grootte te hoog" (:1197), zonder cel of bron voor de
  werkelijke spread.

*Beter uitleggen.* Het oordeel zegt niet of de afwijkingen binnen de verwachting vallen;
na aanvulling van de verwachte afwijking kan het dat in één zin.

*Voor een 9.* :932–935 (verwachting $g_1$ en alpha); :1177 rij splitsen in 1968–2003 en
2004–2025; :1030–1034 en :1159–1165 getallen terug naar de tabel; :1197 bron of cel.

### 7 Oefeningen (9,0)

*Goed.* Instap op het toy (ex-microstructuur-1), afleiding (ex-microstructuur-2),
uitbreiding van de replicatie (ex-microstructuur-3); elke uitwerking eindigt met een
les ("valt statistisch niet meer op", "geen enkel decennium kan die bevestigen").

*Aanmerkingen.* Geen.

*Beter uitleggen.* Ex-microstructuur-2 geeft $t \approx 2{,}6$ na twintig dagen, de tekst
bij :575 $4{,}1$; één bijzin dat het verschil van één naar vijftig ronden komt, voorkomt
verwarring.

## Feitelijke fouten

Nagerekend tegen `$TEMP/F6-04_24_microstructuur-out.txt`. Alle toy-getallen, de Kyle-tabel
(0,5 / 0,9506), de simulatiegetallen (0,528/0,531, 1,024, 0,950, $t\approx4{,}1$), Roll
(46%/48%, 427 van 1168, 60–170 bp, 2020/2008), ILLIQ (factor ~29), $g_1$, $g_2$, AR(1),
PS-maanden en correlaties, alpha's en oefeningsuitkomsten kloppen. De GM-spreadformule
en het bewijs zijn nagerekend en juist.

1. **Onjuist**, :390–391 (en :313): "de helft van de positie die hij zonder prijsimpact
   zou willen". Zonder prijsimpact is de optimale positie van een risiconeutrale insider
   oneindig; juist is de helft van $(v-p_0)/\lambda$, de positie waarbij de prijs tot $v$
   stijgt.
2. **Onjuist (vakterm)**, :604/:622/:643: $\E[V\mid\mathcal F_n]$ heet "middenkoers". Na
   één koop is $(a+b)/2 = 100{,}385$ tegen $\E[V] = 100{,}40$; de as zegt wel correct
   "Verwachte waarde na de order".
3. **Onnauwkeurig**, :900–902: "nauwelijks verschuift" klopt niet buiten het grijze gebied
   (0,336 → 0,206 bij $s/\sigma_e = 0{,}45$).
4. **Niet herleidbaar**, :1197: "een orde van grootte te hoog", geen cel of bron voor de
   werkelijke spread van deze aandelen. Ook :1160–1161 ("Stambaugh schrijft in zijn
   bestand") heeft geen cel die dat toont.
5. **Onzeker (uit F23, open)**, :800–801: Acharya-Pedersen 1,1% per jaar, bron geciteerd
   maar niet ingezien.

## Navertelling in vijf zinnen

Een market maker die weet dat een deel van zijn klanten beter geïnformeerd is, moet een
spread rekenen die het grootst is bij de grootste onzekerheid en krimpt naarmate orders
informatie prijsgeven, zonder dat hij kosten maakt. In Kyles model verstopt een insider
zijn orders achter ruis, de prijs neemt per ronde de helft of bij doorlopende handel alle
informatie op, en de noise traders betalen zijn winst. Roll en Amihud vertalen spread en
prijsimpact naar dagdata, maar Rolls maat is vaak ongedefinieerd en ILLIQ ruisend.
Liquiditeit komt als niveau en als risico in verwachte rendementen, en op vijftig
aandelen en de reeks van Pástor en Stambaugh piekt illiquiditeit in crises met lage
gelijktijdige rendementen. De premie op liquiditeitsrisico is na publicatie niet meer te
zien, zodat risico of vergissing onbeslist blijft. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft goed werk gedaan: verbanden lopen via voegwoorden, er zijn geen
telegramzinnen of regeltaal meer, en er is geen vakterm van betekenis veranderd (de
"middenkoers"-fout staat in code en figuurtitel en is niet door de redactie
ingevoerd). Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. :305–307 "Zo krijgt de stelling van Samuelson uit [...], dat een prijs die een verwachte
   waarde is onvoorspelbaar verandert, een precieze informatieverzameling."
   Herschrijving: "Zo zegt het model ook voor wie de stelling van Samuelson uit [...]
   geldt: een prijs die een verwachte waarde is, verandert onvoorspelbaar voor wie alleen
   de orderhistorie kent."
2. :1064–1065 "..., zodat de liquiditeit verdwijnt in de maanden waarin beleggers moesten
   verkopen." Herschrijving: "Onder zijn maart 2020 en oktober tot december 2008 de
   grootste uitschieters, precies de maanden waarin veel beleggers moesten verkopen."
3. :1205–1206 "Wie illiquide activa houdt, verzekert dan de markt en krijgt daarvoor
   betaald, en dan was dat risico na 2003 kleiner of zien we alleen ruis."
   Herschrijving: "Houders van illiquide activa verzekeren in die lezing de markt en
   worden daarvoor betaald, zodat het risico na 2003 kleiner was of we alleen ruis zien."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Gecontroleerd: de huidige `lectures/04_24_microstructuur.md` tegen de F6-punten, de F6b-diff
(`04_24_microstructuur-ijk-2.md` vs. huidig) en `$TEMP/F6c-04_24_microstructuur-out.txt`.

**Feitelijke fouten**
1. Kyle-positie (:313/:390–391): **opgelost.** "de helft van de positie $(v-p_0)/\lambda$
   waarbij de prijs tot $v$ zou stijgen", monopolist-vergelijking behouden.
2. Middenkoers (:604/:622/:643): **opgelost.** Variabele `mid` -> `value_path`, tekst en
   astitel spreken van "verwachte waarde"/"pad van de verwachte waarde"; geen "middenkoers"
   meer in het bestand (gecontroleerd met grep).
3. Roll-figuur, "nauwelijks" (:900–902): **opgelost.** Nu "in het grijze gebied ...
   nauwelijks, en pas bij grotere spreads daalt ze zichtbaar".
4. Niet herleidbaar (:1197, :1160–1161): **opgelost.** "orde van grootte te hoog" ->
   "opgeblazen" met mechanisme (alle negatieve autocorrelatie, selectie-effect); de bewering
   over Stambaughs bestand is geschrapt.
5. Acharya-Pedersen 1,1% (:800–801): **open, ongewijzigd.** Bron blijft geciteerd zonder
   inzage; geen nieuwe fout, geen verslechtering.

**Helderheid.** Alle vijf "Voor een 9"-punten opgelost: :390–391/:313 (zie boven), :604 e.v.
(zie boven), :311 nu "de helft van de onzekerheid ... gemeten als variantie", :1164 (5%
vervangen door verwijzing naar de gesourcete 5,4% van vóór 2003), :1213 herschreven naar
"vergoedt verliezen in crises". De drie "Beter uitleggen"-punten zijn ook verwerkt: uitleg
van $\alpha_n$ staat nu vóór de recursie (en niet meer dubbel erna), de derdegraadsvergelijking
krijgt een zin vóór de code, en toy-stap 4 toont $0{,}6\cdot0{,}6+0{,}4\cdot0{,}4=0{,}52$ en
$0{,}6\cdot0{,}6=0{,}36$.

**Opbouw.** De aanmerking (routekaart zonder marktontwerp) is opgelost: de routekaart noemt
nu "en sluit af met het marktontwerp van vandaag". Het "beter uitleggen"-punt (Roll-spreads
loskoppeling van het selectie-effect) is opgelost met de toegevoegde zin over jaren met een
negatieve schatting.

**Taal.** Alle vier "Voor een 9"-zinnen herschreven (:305–307, :1064–1065, :1205–1206) en de
Engelse inline-quote geparafraseerd zonder blokcitaat. Geen nieuwe telegramzin of calque
gezien; `prose_stats --check` geeft PASS (5865 woorden, zinslengte 19,1).

**Toy-voorbeeld.** Beide "Voor een 9"-punten opgelost: stap 4 toont de tussenstappen
$0{,}36$ en $0{,}52$, en een nieuwe zin duidt $\lambda$ als kost voor de insider.

**Code en figuren.** Alle drie "Voor een 9"-punten opgelost: een zin vóór de recursiecel
noemt de derdegraadsvergelijking en de wortelkeuze $\alpha_n\lambda_n < \tfrac12$, de
Roll-figuurtekst is genuanceerd (zie Helderheid/Feitelijke fouten 3), en `resid_var / 1.0`
is `resid_var` geworden.

**Replicatie en empirie.** Alle vier "Voor een 9"-punten opgelost: verwachting voor $g_1$ en
de alpha toegevoegd bij "Verwachte afwijking"; de tabel "Origineel en hier" heeft nu de
rijen vóór publicatie (5,4, $t=2{,}72$, 1968–2003) en na publicatie ($-0{,}81$, standaardfout
3,03, $t=-0{,}27$, 2004–2025), die exact overeenkomen met de celuitvoer (regels 196–203 van
`$TEMP/F6c-04_24_microstructuur-out.txt`); de getallen "13 procentpunt" en "$t\approx-8$" uit
:1030–1034 en de "5%"/"-0,8%" uit :1159–1165 zijn uit de lopende tekst gehaald (het eerste
paar stond al in de celuitvoer, het tweede paar staat nu in de tabel); :1197 is geen
niet-herleidbare orde-van-grootte-claim meer.

**Oefeningen.** Het "beter uitleggen"-punt is opgelost: één zin koppelt $t\approx2{,}6$ (één
ronde, ex-microstructuur-2) aan de $4{,}1$ bij vijftig ronden.

**Getallencontrole.** Nieuw of gewijzigd: de alpha's vóór/na publicatie (5,4/$t=2{,}72$ en
$-0{,}81$/3,03/$-0{,}27$) kloppen tegen de celuitvoer; de toy-tussenstappen $0{,}36$ en
$0{,}52$ zijn nagerekende arithmetiek ($0{,}6^2=0{,}36$, $0{,}6^2+0{,}4^2=0{,}52$). Geen
niet-herleidbaar getal aangetroffen. Geen nieuwe punten (geen verslechtering, geen nieuwe
feitelijke fout).

## Eindcijfer van record (F6c): 9,0

| criterium | gewicht | deelcijfer F6 | deelcijfer F6c |
|---|---|---|---|
| 1 Helderheid | 25% | 8,5 | 9,0 |
| 2 Opbouw en rode draad | 20% | 9,0 | 9,0 |
| 3 Taal | 20% | 8,5 | 9,0 |
| 4 Toy-voorbeeld | 10% | 8,5 | 9,0 |
| 5 Code en figuren | 10% | 8,5 | 9,0 |
| 6 Replicatie en empirie | 10% | 8,5 | 9,0 |
| 7 Oefeningen | 5% | 9,0 | 9,0 |
| **Eindcijfer (gewogen)** | | **8,6** | **9,0** (9,00) |

Plafondregel (§11.3): Opbouw en Oefeningen stonden al op 9,0 zonder expliciet "Voor een
9"-cijfer; hun aanmerkingen zijn verwerkt, maar zonder gestelde hogere ceiling blijven ze op
9,0. Alle overige vijf criteria hadden een expliciet "Voor een 9" en zijn met alle genoemde
punten opgelost, dus naar 9,0. Het gewogen eindcijfer 9,00 blijft onder de 9,1 die de
beoordelaar noemde bij volledige oplossing van alle punten (dat cijfer veronderstelde
kennelijk ook ruimte boven 9,0 voor Opbouw en Oefeningen, die de plafondregel hier niet
toestaat). Open blijft: Acharya-Pedersen 1,1% (Feitelijke fouten 5), onzeker zonder inzage
in de bron.
