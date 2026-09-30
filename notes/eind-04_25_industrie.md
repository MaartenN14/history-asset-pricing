STATUS 04_25_industrie F6c words=5679 prose=PASS open=2 cijfer=9,1 min=9,0

**Eindcijfer van record: 9,1** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,9 -> F6c 9,1.

# Eindbeoordeling 04_25_industrie

## Eerste herziening (workflow §12)

Eerste herziening van dit college; er is geen vorig cijfer. Gelezen: de .md volledig,
celuitvoer via `tools/nb_outputs.py` (`$TEMP/F6-04_25_industrie-out.txt`), `prose_stats --check`
(PASS, 5566 woorden, zinnen gemiddeld 18,2, geen zin > 40, 0 telegram, 3 "Wie"-zinnen).

## De drie verbeteringen met het meeste effect

1. **De stelling van Berk en Green en haar bewijs precies maken** (helderheid 8,5 → 9,0).
   `lectures/04_25_industrie.md:310` beweert zonder voorbehoud "In evenwicht beheert de
   beheerder actief tot $C'(q_{a,t}) = \phi_t$", maar dat geldt alleen in het inwendige
   geval met indexdeel; in het randgeval zonder index (bewijs r. 330–331, eerste bullet
   r. 349–351: $2b\,q = 0{,}04 \neq 0{,}03$) geldt het niet. Zet het voorbehoud in de
   stelling ("zolang het fonds een indexdeel heeft"). Maak ook de Lagrangiaan in stap 2
   (r. 324–327) navolgbaar: schrijf de Lagrangiaan uit, zeg dat $\lambda^f = 0$ in het
   inwendige geval (complementariteit) en dat $\lambda^p > 0$; nu staat er een term
   $-\lambda^f f$ zonder herkomst. Leg bij r. 293 in één bijzin uit waarvoor
   $\lim C'(q) > 1$ dient (het fonds blijft eindig groot).
2. **French' 0,67% juist benoemen** (replicatie 8,5 → 9,0; ook helderheid). R. 954–955
   noemt $-0{,}67\%$ "de kostentelling van French voor de gemiddelde actieve dollar",
   en de replicatietabel r. 1038 zet het als origineel naast de nettoalpha van actieve
   fondsen. French meet 0,67% van de *totale* marktwaarde (zoals r. 261–264 correct
   zegt); per actieve dollar is het verlies groter. Herschrijf de zin en de tabelcel
   (bijv. "wat de gemiddelde belegger door actief zoeken verloor"), of vergelijk met de
   nettoalpha van Fama en French (2010), die de admonition als $-0{,}5$ tot $-1\%$ noemt.
3. **Eén naam voor verwachte vaardigheid in rekenvoorbeeld en code** (code en figuren
   9,0 → 9,5; helderheid). Het model noemt de onbekende vaardigheid $a$ en de verwachte
   $\phi_t$, maar de code r. 364 heet de verwachte vaardigheid `a` en de uitvoer drukt
   "na herwaardering naar a = 4%" af (r. 379), terwijl de tekst r. 385 spreekt van "een
   beheerder met drie procent vaardigheid" en r. 356 van "Schat de markt zijn vaardigheid
   ... op 4%". Noem de variabele `phi` en zeg in r. 385 "verwachte vaardigheid". Maak
   r. 373 leesbaar met een benoemde `q_active_new = phi_new / (2 * b)`.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,9

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,5 |
| | **Eindcijfer (gewogen)** | | **8,9** |

(2,125 + 1,80 + 1,80 + 0,95 + 0,90 + 0,85 + 0,475 = 8,90.)

### 1. Helderheid van de uitleg (8,5)

*Goed.*
- Sharpes rekenkunde: stelling in één zin (r. 192–193), bewijs in drie regels, en
  $\Theta = 0{,}5$ uit het toy direct naast het bewijs (r. 228–230).
- Berk en Green: het getallenvoorbeeld (r. 344–357) met 4, 4,5 en 8 miljard maakt het
  evenwicht tastbaar, en de vergelijkende statiek in $b$ en $f$ (r. 389–396) krijgt
  richting én reden (H6), tot en met de mooie observatie dat $f q_t$ niet van $f$ afhangt.
- Standaardfout van alpha: het getal staat naast de formule (1,02; 100 en 25 jaar,
  r. 479–487), precies zoals H4 vraagt.

*Aanmerkingen.*
- Theorie, Het model van Berk en Green, r. 310: "In evenwicht beheert de beheerder
  actief tot $C'(q_{a,t}) = \phi_t$" — geldt alleen in het inwendige geval (zie
  verbetering 1); de stelling is dus niet in één zin juist (H3).
- Idem, r. 324–327: "$f - \lambda^p(C'(q_a) - \phi_t + f) - \lambda^f f = 0$" — de
  Lagrangiaan staat er niet, de term $-\lambda^f f$ is niet te herleiden en
  complementariteit ($\lambda^f = 0$ bij $q_I > 0$) wordt niet genoemd.
- Idem, r. 293: "$\lim_{q\to\infty} C'(q) > 1$" — voorwaarde zonder betekenis (H2).
- Idem, r. 385: "ondanks een beheerder met drie procent vaardigheid" — 3% is $\phi$,
  de verwachte vaardigheid, niet $a$ (H7).
- Replicatie, r. 954–955: "de $-0{,}67\%$ die de kostentelling van French voor de
  gemiddelde actieve dollar geeft" — onjuiste noemer (zie Feitelijke fouten).

*Beter uitleggen.*
- Waarom r. 419–422 de werkversie uit 2012 (2 miljoen dollar) aanhaalt en niet het
  gepubliceerde getal uit 2015, dat ernaast geciteerd wordt: één bijzin volstaat, of
  gebruik het gepubliceerde getal.
- R. 946–950: de verklaring "SMB en HML zijn papieren portefeuilles zonder kosten"
  verklaart de negatieve alpha's van de small-cap- en extended-fondsen, maar de
  Growth-index heeft $+1{,}11\%$ (FF3) en $+0{,}91\%$ (Carhart); zeg dat dezelfde reden
  bij een negatieve HML-lading de andere kant op werkt.

*Voor een 9.* Verbetering 1 (r. 293, 310, 324–327) en 3 (r. 356, 364, 385), en de
noemer bij French (r. 954–955).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Het Overzicht stelt de vraag en geeft het antwoord in de eerste twee zinnen (r. 38–40).
- De Intuïtie voorspelt dat vaardigheid in de omvang zichtbaar wordt en niet in het
  rendement (r. 102–104), en de theorie lost dat na de code in (r. 384–387); de tweede
  voorspelling (staart van sterren door toeval, r. 104–107) wordt in de simulatie ingelost.
- Routekaart (r. 181–188) en Samengevat staan waar ze horen; 5566 woorden.

*Aanmerkingen.*
- Overzicht, r. 41–42: "dat kosten het nettorendement het best voorspellen, is een
  waarneming" — die waarneming wordt nergens in het college getoond of geciteerd; alleen
  r. 404–405 (Carhart: factoren en kosten verklaren de persistentie) komt in de buurt.
- Simulatie, r. 621: "Die laatste groep verliest twee keer de kosten van X en Y uit het
  toy-voorbeeld." — de terugkeer van het toy is hier een los aanknopingspunt, geen
  kalibratie (H11 is formeel vervuld, maar de draad is dun).

*Beter uitleggen.* Laat r. 41–42 verwijzen naar wat Carhart vond (r. 404–405), of
formuleer het Overzicht zo dat het die zin inlost.

### 3. Taal (9,0)

*Goed.*
- Leest vlot, met voegwoorden in plaats van knippen; `prose_stats` schoon (0 telegram,
  0 calques, 0 gedachtestreepjes, dubbele punten binnen de norm).
- Motiefnamen elk hoogstens één keer, geen motief als onderwerp; "Wie"-zinnen 3.
- Sterke slotzinnen, zoals r. 1057 "De rekenkunde zegt immers niets over wie wint, maar
  alles over wat het kost."

*Aanmerkingen.*
- Overzicht, r. 43: "Of er daarnaast een restje vaardigheid overblijft, is een feit met
  concurrerende verklaringen." — een of-vraag is geen feit.
- Overzicht, r. 45–46: "rekenen we met drie beleggers en twee aandelen na dat de actieve
  beleggers samen vóór kosten precies de markt halen" — gescheiden werkwoord met een
  dat-zin erachter hapert.
- Wat er brak, r. 1072: "Data over waarop beleggers hun geld verplaatsen
  zouden de lezingen kunnen scheiden, maar die zijn omstreden." — "data over waarop" is
  geen gesproken Nederlands.
- Simulatie, r. 786: "Als teller is de bootstrap zwak" — "teller" is onduidelijk.
- Theorie, r. 419–422: "In een eerdere werkversie van hetzelfde onderzoek uit 2012
  voegde de gemiddelde beheerder zo ongeveer 2 miljoen dollar per jaar toe" — leest
  alsof de beheerder in de werkversie iets toevoegde; "zo ongeveer" is spreektaal.

*Beter uitleggen.* Geen inhoudelijk punt; de taalredactie heeft geen vakterm van
betekenis veranderd (gecontroleerd: nettoalpha, closet indexer, tracking error, false
discovery rate, persistentie, overlevenden blijven consistent).

### 4. Toy-voorbeeld (9,5)

*Goed.* Met de hand in twee minuten na te rekenen (r. 137–144), één mechanisme, tabel
hand/code met zes identieke regels, en een slotzin met betekenis (r. 175–177). De
getallen keren terug in Theorie ($c_j$, $\Theta = 0{,}5$).

*Aanmerkingen.* Geen.

*Beter uitleggen.* Niets nodig.

### 5. Code en figuren (9,0)

*Goed.*
- `alpha_tstats`, `bootstrap_t` en `benjamini_hochberg` lezen als het algoritme (r. 632–769);
  de bootstrap trekt zichtbaar dezelfde maanden voor alle fondsen.
- Elke figuur heeft een leeswijzer ervoor (r. 675–677, 819–820, 967–969) en een
  bijschrift dat zegt wat te zien is.

*Aanmerkingen.*
- Theorie, r. 364: "`a, b, f = 0.03, 0.005, 0.01          # skill, cost per $bn, fee`" —
  `a` is hier $\phi$ (verwachte vaardigheid), niet de $a$ uit het model.
- Idem, r. 373: "`q_total_new = (a_new * a_new / (2 * b) - b * (a_new / (2 * b))**2) / f`"
  — compacte herhaling in plaats van een benoemd tussenresultaat.

*Beter uitleggen.* Zie verbetering 3.

### 6. Replicatie en empirie (8,5)

*Goed.*
- Admonition compleet (bron, wat, data, verschil, verwachte afwijking) met een
  controlepunt (VTSMX moet licht negatief zijn) dat uitkomt (r. 871–873, 946).
- Tabel origineel/hier (r. 1036–1041) en een oordeel dat begint met "Gedeeltelijk
  geslaagd" en naar de selectie op overleven verwijst (r. 1043–1048).
- De power-berekening bij de persistentie (r. 1033–1034) voorkomt de verkeerde conclusie.

*Aanmerkingen.*
- Replicatie, r. 954–955 en tabel r. 1038: "kosten $0{,}67\%$ (French)" als origineel
  naast de nettoalpha van actieve fondsen — French' getal is per dollar marktwaarde,
  niet per actieve dollar.
- Replicatie, r. 946–958 en r. 1030–1034: veel getallen in lopende tekst (tot zes per
  alinea), terwijl ze in de tabellen al staan.
- Replicatie, r. 874: "in plaats van $-0{,}5$ tot $-1\%$" — deze verwachting staat niet
  in de tabel r. 1038, waar het origineel $-1{,}1\%$ (Jensen) is; twee verschillende
  ijkpunten voor dezelfde grootheid.

*Beter uitleggen.* Kies één ijkpunt voor "gemiddelde nettoalpha" (het getal van Fama en
French 2010, met citaat) en gebruik dat in admonition en tabel.

*Voor een 9.* Verbetering 2 (r. 954–955, 1038) en één ijkpunt (r. 874, 1038); laat in
r. 946–958 de tekst verwijzen naar de tabel in plaats van zes getallen te herhalen.

### 7. Oefeningen (9,5)

*Goed.* Instap als variant op het toy met particulieren (ex-industrie-1), afleiding van
de expliciete Berk-en-Green-oplossing (ex-industrie-2), uitbreiding van de replicatie
(ex-industrie-3); elke uitwerking eindigt met een les (r. 1118–1120, 1160–1161, 1196–1198).
Getallen kloppen met de celuitvoer.

*Aanmerkingen.* Geen.

*Beter uitleggen.* In ex-industrie-2 (2) staat de nieuwe omvang (5,1 miljard) alleen in de
uitvoer; één getal in de proza zou de slotzin r. 1159 ("de omvang met 13%") verankeren.

## Feitelijke fouten

Nagerekend tegen de celuitvoer: toy (4; 7,5; −1,25; 3,0; 0,9), Berk en Green (4; 3; 4,5;
8 miljard; 78%), SE-alpha (1,02; 100 en 25 jaar; 1,12 na twintig jaar), simulatie (2,0%
= 28 fondsen; 36%; 28/100 "iets meer dan een kwart"; 0,80/0,04/0,02; BH 16 zonder
onterechte; 0,032–0,085; "een derde" en "85%"), replicatie (367 maanden; −0,19; 0,53 met
$t = 1{,}36$; 14%; 0,74 tegen −0,03; 95%; 0,13/−0,37/0,51/0,59/0,86; ~145 jaar klopt voor
0,51), oefeningen (2,67; 1,77; 3,19%; 13,2%; 0,60/0,18; 0 BH; 0,046 ≈ 0,05). Alles juist,
op twee punten na:

1. **r. 954–955 en r. 1038**: French' 0,67% wordt "de kostentelling ... voor de
   gemiddelde actieve dollar" genoemd. French (2008) rapporteert 0,67% van de *totale*
   marktwaarde (r. 261–262 zegt dat zelf correct); per actieve dollar is het verlies
   groter. Correctie: "voor de gemiddelde belegger" of het getal per actieve dollar.
2. **r. 310**: de stelling zegt onvoorwaardelijk $C'(q_{a,t}) = \phi_t$, terwijl het
   bewijs (r. 330–331) en het getallenvoorbeeld zonder index (r. 349–351, $C'(4) = 0{,}04
   \neq 0{,}03$) het randgeval tonen waar dat niet geldt. Correctie: voorbehoud
   "zolang $q_{I,t} > 0$" in de stelling.

Geen vakterm van betekenis veranderd door de taalredactie.

## Navertelling in vijf zinnen

Dat actief beheer gemiddeld verliest, volgt uit een optelsom: vóór kosten halen de
actieve beleggers samen de markt, na hun hogere kosten blijven ze achter. Vaardigheid
kan toch bestaan, want in het model van Berk en Green stroomt er geld naar een vaardige
beheerder tot de belegger niets extra's meer overhoudt, zodat vaardigheid in omvang en
vergoeding zichtbaar wordt en niet in rendement of persistentie. Eén fonds is niet te
beoordelen omdat de standaardfout van alpha na twintig jaar nog ruim een procentpunt is,
dus de literatuur toetst de hele cross-sectie met de bootstrap van Fama en French en de
false discovery rate van Barras, Scaillet en Wermers. Een simulatie met bekende waarheid
laat zien dat deze methoden het aandeel vaardige fondsen sterk onderschatten bij korte
steekproeven. Op 50 overlevende fondsen lijken de alpha's positief, maar dat is de
selectie op overleven, zodat de echte data de vraag niet beslissen. Dit sluit aan bij
het Overzicht.

## Taal na de redactie

De redactie heeft goed werk gedaan: de tekst leest als gesproken academisch Nederlands,
de tellingen zijn schoon, en geen vakterm is van betekenis veranderd. Hardop-toets, drie
zinnen die nog niet natuurlijk klinken:

1. r. 43: "Of er daarnaast een restje vaardigheid overblijft, is een feit met
   concurrerende verklaringen." → "Of er daarnaast een restje vaardigheid overblijft,
   is een open vraag, want de data laten meer dan één verklaring toe."
2. r. 45–46: "rekenen we met drie beleggers en twee aandelen na dat de actieve beleggers
   samen vóór kosten precies de markt halen;" → "laten we met drie beleggers en twee
   aandelen zien dat de actieve beleggers samen vóór kosten precies de markt halen;"
3. r. 1072: "Data over waarop beleggers hun geld verplaatsen zouden de lezingen kunnen
   scheiden, maar die zijn omstreden." → "Data over de redenen waarom beleggers hun geld
   verplaatsen, zouden de lezingen kunnen scheiden, maar die data zijn omstreden."

Bij volledige oplossing van alle punten: 9,2

## Controle 1

Gecontroleerd tegen `tools/nb_outputs.py` (`$TEMP/F6c-04_25_industrie-out.txt`) en tegen de
sectie R9-1 in `notes/rapport-04_25_industrie.md`. Alle getallen die de schrijver toevoegde of
wijzigde herleiden naar de celuitvoer: versie 1/2 van Berk-Green (4; 3; 4,5; 45 mln; na
herwaardering 8 mld, 78%), $\phi_1 = 3{,}19\%$, $q_0 = 4{,}5$, $q_1 = 5{,}1$ mld (ex-industrie-2),
replicatietabel (Carhart-alpha $0{,}53\%$, $t=1{,}36$, 14% met $t>2$, VTSMX CAPM $-0{,}19\%$).
Geen niet-herleidbaar getal, geen nieuw feitelijk punt.

### Feitelijke fouten (F6)

1. French 0,67% als kostentelling "per actieve dollar": **opgelost**. R. 972 en de tabel
   vergelijken nu met Jensens $-1{,}1\%$ na kosten; French blijft in Theorie correct als
   percentage van de marktwaarde (r. 263–265).
2. Stelling Berk-Green zonder voorbehoud: **opgelost**. R. 314: "Zolang het fonds een
   indexdeel heeft ($q_{I,t} > 0$) ... $C'(q_{a,t}) = \phi_t$." Nagerekend: het bewijs
   (stap 2) geeft de Lagrangiaan, de twee eerste-ordevoorwaarden, $\lambda^f = 0$ door
   complementariteit in het inwendige geval ($\lambda^p = 1 > 0$, dus $C'(q_a)=\phi_t$) en
   $\lambda^f > 0$, $C'(q_a) < \phi_t$ in het randgeval — wiskundig consistent met de drie
   numerieke voorbeelden (versie 1 zonder index: $\phi = bq+f$).

### Drie verbeteringen (F6)

1. Stelling + Lagrangiaan + bijzin bij $\lim C'(q)>1$: **opgelost** (zie boven; r. 293 heeft
   nu de bijzin "zodat het fonds eindig groot blijft").
2. French-noemer: **opgelost** (zie Feitelijke fouten 1); ook één ijkpunt voor "gemiddelde
   nettoalpha" gebruikt (Jensen $-1,1\%$) in admonition (r. 888) én tabel (r. 1056) — het
   eerdere tweede ijkpunt ($-0,5$ tot $-1\%$ zonder bron) is weg.
3. Eén naam voor verwachte vaardigheid: **opgelost**. Code r. 374–384 gebruikt `phi`,
   `phi_new`, en de benoemde `q_active_new = phi_new / (2 * b)`; tekst r. 396–397 zegt
   "verwachte vaardigheid van drie procent" in plaats van "a".

### Overige punten uit de rubriek

- Helderheid, r. 385 (a vs phi): opgelost (zie boven).
- Helderheid, Growth-index bij negatieve HML-lading: opgelost, r. 966–967 legt de
  symmetrische reden uit.
- Helderheid, werkversie 2012 (r. 433–435): deels — "zo ongeveer" weg en de zin leest niet
  meer alsof de beheerder in de werkversie zelf iets toevoegde, maar het gepubliceerde
  getal uit 2015 is niet toegevoegd (schrijver: niet geverifieerd, kaart §6). Geen
  feitelijke fout, blijft een kleine aanmerking.
- Opbouw, Overzicht r. 42–43 (waarneming zonder bron): opgelost, verwijst nu naar Carhart.
- Opbouw, Simulatie r. 634 (dunne toy-draad): niet gewijzigd, zoals gemeld; dit was geen
  "Voor een 9"-punt en geen feitelijke fout, dus geen aftrek.
- Taal, hardop-toets (r. 43, 46–47, 1090): alle drie **opgelost**, letterlijk volgens het
  voorstel van de eindbeoordelaar.
- Taal, "Als teller is de bootstrap zwak" (r. 799): opgelost ("Om vaardige fondsen te
  tellen").
- Replicatie, getallen in lopende tekst (r. 969–976): **deels** — het paragraaf noemt nu
  vier getallen in plaats van tot zes, en verwijst expliciet naar de tabel ("de tabel aan
  het eind zet de getallen naast de originelen"); niet volledig teruggebracht tot een
  tabelverwijzing zonder herhaling, maar geen feitelijke fout.
- Oefeningen, ex-industrie-2 (2) (omvang alleen in uitvoer): opgelost, r. 1178–1179 noemt
  "van 4,5 naar 5,1 miljard dollar", klopt met cel 16.

Geen verslechtering gevonden; geen nieuwe feitelijke fout.

## Eindcijfer van record (F6c): 9,1

| nr | criterium | gewicht | deelcijfer | F6 | toelichting |
|---|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 | 8,5 | alle "Voor een 9"-punten en aanmerkingen opgelost |
| 2 | Opbouw en rode draad | 20% | 9,0 | 9,0 | geen punt in het vooruitzicht gesteld, ongewijzigd |
| 3 | Taal | 20% | 9,0 | 9,0 | geen punt in het vooruitzicht gesteld, ongewijzigd |
| 4 | Toy-voorbeeld | 10% | 9,5 | 9,5 | geen aanmerking |
| 5 | Code en figuren | 10% | 9,5 | 9,0 | verbetering 3 opgelost en geverifieerd |
| 6 | Replicatie en empirie | 10% | 9,0 | 8,5 | feitelijke fout en ijkpunt opgelost; getallen-in-tekst deels |
| 7 | Oefeningen | 5% | 9,5 | 9,5 | ex-industrie-2 (2) opgelost |
| | **Eindcijfer (gewogen)** | | **9,1** | 8,9 | |

(2,25 + 1,80 + 1,80 + 0,95 + 0,95 + 0,90 + 0,475 = 9,125 -> 9,1.)
