STATUS 03_15_shiller_excess_volatility F6c words=5748 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: Vorig: 8,8. Ronde 9+: T, F6 8,7 -> F6c 9,0. Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Ronde 9+

Vorige ronde: 8,8

Eindbeoordeling (F6) van `lectures/03_15_shiller_excess_volatility.md` na de taalredactie,
met de gewichten van ronde 9+ (helderheid 25, opbouw 20, taal 20, toy 10, code en figuren 10,
replicatie 10, oefeningen 5). Bij twijfel geldt het lagere cijfer. Vindplaatsen zijn
regelnummers in `lectures/03_15_shiller_excess_volatility.md`.

## De drie verbeteringen met het meeste effect

1. **Taal (8,5 → 9).** Eén naam voor het verwijderen van de trend: nu staan er vier vormen
   naast elkaar ("detrendeerde hij" op 319, "gedetrendeerd(e)" op 321, 325, 355, 467, 587,
   662, 766, 805, 949, 1002, 1075 en in de figuur, "trendcorrectie" op 898, 952, 963, 1040,
   "geen trend te verwijderen" op 497). Daarnaast de vier zinnen uit de hardop-toets
   herschrijven (158–159, 591–592, 1047–1049, 1062–1064) en "namelijk" als vervanger van de
   dubbele punt terugbrengen (acht keer).
2. **Helderheid (8,5 → 9).** De openingszin van de simulatie (583–584) laat de toets
   "werken" bij stationaire dividenden, terwijl economie (c), ook stationair, in 19,8% van
   de steekproeven vals alarm geeft. Verder botst "de tweede verwachting" (1024) met "de
   tweede verwachting uit de intuïtie" (466), en West (1988) krijgt geen getal of exemplaar
   (530–531).
3. **Code en figuren (8,5 → 9).** De simulatiefiguur tekent een gestippelde lijn bij 13,28
   (740) die noch de leeswijzer (729–730) noch het bijschrift (754–758) noemt. Daarnaast is
   `shiller_test` (623–658) met ruim dertig regels lang, en de trendschatting kan eruit
   [onderzoek A].

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,80 + 1,70 + 0,90 + 0,85 + 0,90 + 0,45 = 8,725, dus 8,7.
Lengte: 5.648 woorden volgens `prose_stats` (PASS; zinnen gemiddeld 16,4, geen zin boven
40, dubbele punt 1,1 per 1000, 10 eenzinsalinea's). Replicatieblok: ongeveer 200 woorden.

Het lagere cijfer dan de vorige ronde (8,8) komt uit de strengere lat van ronde 9+
(§11.12, hardop-toets, taal nu 20%), niet uit een verslechtering. Alle punten van de vorige
ronde over helderheid, code en replicatie zijn opgelost (6,5 tegen 5,59 benoemd als
veranderingen tegen niveaus, de grens $\sigma(d)/\sqrt{2\bar r}$ geduid, de discontovoet in
de simulatie met trend, de Dow-rij in de tabel, `polyfit` en correlatie als lus, geen
`describe()`, zichtbare lus in oefening 2, zin vóór de importcel).

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Intuïtie**: de weersvoorspeller maakt de ongelijkheid concreet, en het addertje
  (toestanden tegen tijd) staat al vóór de theorie klaar.
- **De variantiegrens**: de economische reden staat vóór de stelling (een belegger die een
  samenhang tussen fout en prijs ziet, handelt die weg), en direct erna het toy-getal
  $32{,}79 = 16 + 16{,}79$.
- **Kritiek 2**: de vergelijking van 6,5 met Shillers 5,59 zegt nu uitdrukkelijk dat de
  orde van grootte gelijk is en de statistiek niet (466–468).

*Aanmerkingen*
- Simulatie: "Shillers toets werkt als dividenden stationair rond een bekende trend
  schommelen, en slaat altijd vals alarm als ze een random walk volgen." (583–584) Economie
  (c) is stationair rond een bekende trend en geeft in 19,8% van de steekproeven vals
  alarm; de zin spreekt de eigen tabel tegen.
- Replicatie: "**Geslaagd**, ook voor de tweede verwachting." (1024) Bedoeld is het tweede
  deel van de verwachte afwijking (de factor vijf van Kleidon), maar de lezer kent "de
  tweede verwachting" als die uit de intuïtie (466).
- Het antwoord in logs: "Die grens was duidelijk en significant geschonden." (530–531)
  Geen getal of exemplaar.
- Wat Shiller mat: "Hij regresseerde $\ln p_t$ op een constante en de tijd, met helling
  $b$" (319–320). De orde van grootte van $b$ (ongeveer 1,5% per jaar) volgt pas op 663.

*Beter uitleggen*
- Wanneer de toets werkt: de lezer moet uit de simulatie afleiden dat het om stationair
  én weinig persistent gaat; de openingszin kan dat meteen zeggen.
- Wat West precies toetste en hoe groot de schending was: één getal of één
  vergelijking (onverwachte koersveranderingen tegen dividendnieuws) is genoeg.

*Voor een 9*
- `03_15_shiller_excess_volatility.md:583–584` de conclusie beperken tot stationaire en
  weinig persistente dividenden (herschrijven, geen zin erbij).
- `:1024` "de tweede verwachting" vervangen door wat bedoeld is (de spreiding over
  keuzes).
- `:530–531` West 1988 één getal of exemplaar geven.
- `:319–320` $b$ bij de eerste keer een getal geven.

### 2. Opbouw en rode draad (9)

*Goed*
- **Overzicht** stelt de vraag, geeft het antwoord (factor vijf tot dertien, maar sterk
  afhankelijk van keuzes) en noemt het overblijvende feit.
- De drie verwachtingen uit de intuïtie worden in gewone zinnen ingelost (308, 466, 548),
  zonder vaste formule.
- De toy-getallen keren terug in de theorie (302, 306) en de simulatie (617, 793), en de
  routekaart (223–227) en Samengevat omsluiten de theorie.

*Aanmerkingen*
- Waar we zijn en Overzicht: "Bewegen aandelenprijzen meer dan de latere dividenden kunnen
  rechtvaardigen?" staat woordelijk op 30–31 en 36 [onderzoek A]. Geen aftrek, wel een
  gemiste kans.

*Beter uitleggen*
- Niets wezenlijks; de lezer kan de kern na het Overzicht benoemen.

### 3. Taal (8,5)

*Goed*
- De redactie heeft de vaste etiketten weggehaald ("Waarom zou dit waar zijn?" in Theorie,
  vijf van de zes "In woorden:", "Wat we nu weten"); vaste wendingen en motiefnamen staan
  elk hoogstens twee keer, geen motief als handelend onderwerp.
- Verband met voegwoorden in plaats van dubbele punten (1,1 per 1000), geen
  gedachtestreepjes, geen "Wie"-zinnen, geen "haar/zij" voor zaken.
- De onderzoekspunten over "overleeft", "Wat overblijft, is", "definieert het tijdvak",
  "detrending" en "gedemeend" zijn opgelost [onderzoek A].

*Aanmerkingen*
- Wat Shiller mat: "Omdat koersen en dividenden over een eeuw exponentieel groeien,
  detrendeerde hij beide eerst." (318–319) STYLE §3 schrijft "de trend verwijderen" voor.
- Replicatie: "Voor de figuur rekenen we ook twee versies van $p^*$ zonder trendcorrectie
  uit" (898), en "zonder trendcorrectie" (952, 963), "na trendcorrectie" (1040), naast
  "Niet gedetrendeerd" in de figuurtitel (940). Vier namen voor één handeling (H7).
- Toy-voorbeeld: "Daarmee rekenen we zes stappen uit:" (158–159). Stappen reken je niet uit.
- Simulatie: "omdat de toets hier op een eeuw jaardata moet lijken." (591–592) Niet de
  toets, maar de kunstmatige data moeten op een eeuw jaarcijfers lijken.
- Replicatie: "maar deze statistiek bouwt het tweede moment van $p^*$ op uit een eerste
  moment dat dat niet is." (1048–1049)
- Wat er brak: "De grens verlegde de toets van efficiëntie van de vraag of iemand morgen
  rijk kan worden, waarop het antwoord nee was, naar de vraag of koersniveaus passen bij
  fundamentele waarde." (1062–1065) Drie keer "van" en een ingeschoven bijzin.
- Replicatie: "Elke rij valt binnen de verwachting uit het replicatieblok" (892):
  regeltaal (§11.12).
- Verschil met het origineel: "De Dow-reeks is niet gratis beschikbaar, dus we tonen de
  S&P over 1928–1979 als benadering." (816–817) Engelse "so"-volgorde [onderzoek A].
- "namelijk" staat acht keer, vaak als vervanger van de weggehaalde dubbele punt (88, 530,
  549, 1062, 1077); hardop valt dat op.

*Beter uitleggen*
- n.v.t. (taal).

*Voor een 9*
- `:319` "verwijderde hij bij beide eerst de trend"; `:898, 952, 963, 1040` en de titel op
  940 één familie laten gebruiken (zie oordeel over "trendcorrectie" hieronder).
- `:158–159`, `:591–592`, `:1048–1049`, `:1062–1065` herschrijven (voorstellen onder
  "Taal na de redactie").
- `:892` "binnen de verwachting uit het replicatieblok" → "binnen wat we verwachtten";
  `:816–817` "Omdat de Dow-reeks niet gratis is, tonen we als benadering de S&P over
  1928–1979" [onderzoek A].
- Twee of drie "namelijk" terug naar een gewone bijzin of een punt.

**Oordeel over "trendcorrectie".** De betekenis is niet veranderd: het gaat overal om het
wegdelen van dezelfde exponentiële trend, en "trendcorrectie" is gangbaar Nederlands. Het
is dus geen feitelijke fout, maar wel een taalpunt om twee redenen. Ten eerste schrijft
STYLE §3 "de trend verwijderen" voor, en de redacteur week daarvan af op aanraden van
[onderzoek A] (dat zelf "zonder trendcorrectie" voorstelde); de regel en het onderzoek
spreken elkaar hier tegen. Ten tweede staat "trendcorrectie" naast "gedetrendeerd",
"detrendeerde" en "trend verwijderen", zodat de lezer vier namen voor één handeling krijgt
(H7). Advies: het bijvoeglijk "gedetrendeerd" houden (het is de vakterm en staat in figuur
en tabel), het werkwoord op 319 vervangen door "verwijderde de trend", en de vier keer
"trendcorrectie" vervangen door "zonder (of na verwijdering van) de trend". Wil de eigenaar
"trendcorrectie" toestaan, dan hoort dat in STYLE §3, en dan nog in één vorm per college.

### 4. Toy-voorbeeld (9)

*Goed*
- Drie dividenden, twee informatiestructuren en zes handstappen, in vijf minuten na te
  rekenen; de tabel hand/code klopt tot op de covariantie van nul.
- De slotzin (215–219) zegt wat de getallen betekenen, inclusief de omkering langs het pad.
- Stap 4 en stap 6 komen letterlijk terug in de controle van de simulatie (793).

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Niets.

### 5. Code en figuren (8,5)

*Goed*
- `ex_post_price` leest als de achterwaartse recursie en wordt hergebruikt voor de toy, de
  simulatie en de log-lineaire grens (979–980 zegt hoe).
- De AR(1) en de trendschatting zijn zichtbare lussen; elke cel heeft een zin ervoor en
  erna.
- Figuur 1 heeft een leeswijzer (917–918) en een bijschrift dat zegt wat te zien is.

*Aanmerkingen*
- Simulatie: "De figuur toont de drie verdelingen, met een zwarte lijn bij één en Shillers
  eigen 5,59 gestreept." (729–730) De code tekent ook een gestippelde lijn bij 13,28 (740),
  die nergens wordt genoemd.
- `shiller_test` (623–658) telt ruim dertig regels; de trendschatting kan een eigen functie
  worden [onderzoek A].

*Beter uitleggen*
- Wat de 13,28-lijn is (Shillers Dow-waarde) en waarom hij in een figuur over 109 jaar
  S&P-achtige data staat.

*Voor een 9*
- `:729–730` en `:754–758` de 13,28-lijn noemen, of `:740` die lijn weglaten.
- `:635–642` de trendschatting in een kleine functie zetten [onderzoek A].

### 6. Replicatie en empirie (9)

*Goed*
- Het replicatieblok geeft bron, wat, data, verschil en verwachte afwijking in ongeveer 200
  woorden, en de tabel origineel/hier heeft een kolom met de verwachting, nu inclusief de
  Dow-rij.
- De gevoeligheidstabel maakt de kern van het college zichtbaar (0,55 tot 9,8 op dezelfde
  data), en elke keuze krijgt een economische reden.
- Het oordeel begint met Geslaagd en verwijst naar de verwachting.

*Aanmerkingen*
- "Op dezelfde data en met dezelfde stelling loopt de ratio van 0,55 tot 9,8" (1025)
  tegenover "tussen 0,55 en 9,3 over 1871–2025" (1073). De 9,8 hoort bij 1928–1979; zeg dat
  [onderzoek A].
- "volgens Kleidon varieert de ratio over redelijke keuzes met minstens een factor vijf"
  (823–824) is niet tegen de bron gecontroleerd.

*Beter uitleggen*
- Welke rij de bovenkant van de spreiding geeft (1025).

### 7. Oefeningen (9)

*Goed*
- Instap op het toy (structuur C), een afleiding (Kleidon-ratio en de ondergrens van
  LeRoy-Porter) en een uitbreiding van de replicatie (1950–2025).
- Elke uitwerking eindigt met wat ze leert, zonder vaste wending (1129–1135, 1185–1187,
  1215–1219).

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Niets.

## Feitelijke fouten

Nagerekend met de hand en tegen de celuitvoer (`tools/nb_outputs.py`). Correct: het toy
(12; 13,6; 22,88; 19,52; 16; 32,7936; 16,7936; langs het pad 23,01 en 34,16, met de hand
nagerekend); $\delta = 0{,}954$ en $\delta^{108} = 0{,}0063$; $50{,}12/8{,}968 = 5{,}59$;
de Flavin-term $39/100$; $\sqrt{1+2/0{,}048} = 6{,}53$, $\sqrt{21} = 4{,}58$,
$\sqrt{1+2/0{,}07} = 5{,}44$; $1{,}07 \times 1{,}015 - 1 = 8{,}6\%$; $\rho = 25/26 = 0{,}96$;
de simulatie (0%, 19,8%, 100%; mediaan 2,63; 95e percentiel 4,04; de grens geldt op
$t = 10, 50, 100$); de replicatie (155 jaren; 8,6% en 1,7%; 3,93 tegen 5,59; correlatie
0,36; $b$ en $\bar r$ binnen 0,13 en 0,24 procentpunt; 9,83 tegen 13,28;
$0{,}0860 - 0{,}0168 = 0{,}069$; 0,554 tot 9,829; $9{,}329/1{,}813 = 5{,}1$; 1,105; ruim een
derde lager ($1{,}81 \to 1{,}11$); 0,83 en 0,59; SE 0,0143; 0,55 en 2,36; log-lineair 1,15 tot
1,90); oefening 1 (26,24), oefening 2 (10,05; 6,53; 4,58; gesimuleerd 6,54), oefening 3
(1,34 tot 12,1, factor 9,05). Het bewijs van de Kleidon-propositie en de afleiding van de
decompositie kloppen. De taalredactie heeft geen vakterm van betekenis laten veranderen;
"trendcorrectie" betekent hetzelfde als "de trend verwijderen" (zie Taal).

Geen fouten gevonden. Twijfelachtig, niet geteld:
- 583–584: "Shillers toets werkt als dividenden stationair rond een bekende trend
  schommelen" is te ruim, gezien 19,8% vals alarm in de stationaire economie (c) (zie
  Helderheid).
- 1095: "Dat vonden Basu, Banz en Rosenberg in de cross-sectie" na "goedkoop ten opzichte
  van winst of boekwaarde". Basu (koers-winst) en Rosenberg c.s. (boekwaarde) passen; Banz
  ging over marktwaarde (kleine aandelen). Nagaan in [](#03-16-vroege-anomalieen).
- 823–824: de toeschrijving "volgens Kleidon ... minstens een factor vijf" is niet tegen de
  bron gecontroleerd.

## Navertelling in vijf zinnen

Een rationele prijs is de beste voorspelling van de contante waarde van de dividenden die
later werkelijk komen, en een voorspelling varieert over toestanden nooit meer dan wat ze
voorspelt. Shiller mat in 1981 dat de gedetrendeerde S&P-koers vijf keer zo veel bewoog als
die ex-post rationele prijs, en concludeerde dat koersen te veel bewegen. De grens gaat
echter over toestanden en de meting over de tijd, en in kleine steekproeven met persistente
of niet-stationaire dividenden slaat de toets vals alarm, zoals Flavin, Kleidon en Marsh en
Merton lieten zien en de simulatie bevestigt. Op echte data hangt de ratio sterk af van
eindwaarde, trend, steekproef en discontovoet (0,55 tot 9,8), maar de robuuste log-lineaire
versie van Campbell en Shiller blijft boven één. Dat surplus is hetzelfde feit als
voorspelbare rendementen, en of het uit bewegende discontovoeten of uit overreactie komt,
laat de data nog open. Dat stemt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk natuurlijker gemaakt: de sjablonen zijn weg, de
dubbele punten zijn voegwoorden geworden en de verwijswoorden kloppen. Wat overblijft, zijn
enkele zinnen die de herschrijving stroef heeft gemaakt, "namelijk" als nieuwe lijm, en de
vier namen voor het verwijderen van de trend. De hardop-toets levert drie zinnen op die een
econoom zo niet zou zeggen:

1. "Daarmee rekenen we zes stappen uit:" (158–159) → "In zes stappen rekenen we daarmee
   alles uit."
2. "Dat zijn andere getallen dan de 25% en drie perioden van het toy-voorbeeld, omdat de
   toets hier op een eeuw jaardata moet lijken." (589–592) → "Die getallen wijken af van
   de 25% en de drie perioden van het toy-voorbeeld, omdat de kunstmatige data hier op een
   eeuw jaarcijfers moeten lijken."
3. "Een tweede moment is goed meetbaar, maar deze statistiek bouwt het tweede moment van
   $p^*$ op uit een eerste moment dat dat niet is." (1047–1049) → "Een tweede moment is goed
   meetbaar, maar deze statistiek bouwt de variantie van $p^*$ op uit een gemiddelde, en
   dat is slecht meetbaar."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Controle van ronde 9+ (R9-1, rapport §"R9-1 (F6b, ronde 9+)") tegen de punten van F6.
Getallen gecontroleerd met `tools/nb_outputs.py`: "trendcorrectie" komt nergens meer voor
(grep leeg); de celuitvoer van de vergelijkingstabel (r. 895–903) bevat `0.0148`
(trendgroei $b$, 1871–1979) en `13.2800` (Shiller: Dow, 1928–1979), zoals de tekst op
:320 en :740–741/:767–768 nu ook zegt. `prose_stats --check`: PASS, woorden 5.748.

**Helderheid (was 8,5, vooruitzicht 9).**
- `:583–584` (nu 586–587) opgelost: de opening onderscheidt nu snel uitdovende
  afwijkingen (toets werkt) van persistente afwijkingen (vals alarm) en random walk
  (altijd alarm); spreekt de eigen tabel niet meer tegen.
- `:1024` (nu 1039) opgelost: "de tweede verwachting" → "de verwachte spreiding over
  keuzes".
- `:530–531` opgelost: West 1988 krijgt een exemplaar (vernieuwingen tegen een
  voorspeller met alleen dividendhistorie, omgekeerd op de S&P); bewust geen getal, want
  niet uit een cel of gecontroleerde bron (STYLE §11.11).
- `:319–320` opgelost: $b$ krijgt bij de eerste vermelding het getal 0,0148 (≈1,5%/jaar).
- Alle vier punten opgelost → 9.

**Opbouw (was 9, geen punt).** Ongewijzigd 9. Aanmerking (Overzicht/Waar we zijn
herhaalt de vraag woordelijk) was geen "Voor een 9"-punt; toch verholpen (Overzicht
herhaalt de vraag niet meer letterlijk).

**Taal (was 8,5, vooruitzicht 9).**
- `:319` opgelost: "verwijderde hij bij beide eerst de trend" (exact het voorstel).
- `trendcorrectie`-familie opgelost: "trendcorrectie" komt nergens meer voor (grep
  leeg); "detrendeerde" (werkwoord) is weg, alleen het bijvoeglijke "gedetrendeerd(e)"
  blijft, zoals geadviseerd.
- Vier hardop-zinnen opgelost: 158–159, 591–592 (nu 594), 1048–1049 (nu 1065) en
  1062–1065 (nu 1080–1082) zijn herschreven, grotendeels volgens de voorgestelde tekst.
- `:892` opgelost: "binnen wat we verwachtten"; `:816–817` opgelost: Dow-zin met "Omdat".
- "namelijk" van 8 naar 3 (meer dan de gevraagde twee of drie minder).
- Alle punten opgelost → 9.

**Toy-voorbeeld (was 9, geen punt).** Ongewijzigd 9.

**Code en figuren (was 8,5, vooruitzicht 9).**
- `:729–730`/`:754–758` opgelost: de 13,28-lijn wordt nu genoemd, zowel in de
  leeswijzer ("zijn Dow-waarde 13,28 gestippeld") als in het bijschrift ("13,28 (Dow,
  kortere steekproef)").
- `:635–642` opgelost: de trendschatting staat nu in een eigen functie (`log_trend`),
  los van `shiller_test`.
- Beide punten opgelost → 9.

**Replicatie (was 9, geen punt).** Ongewijzigd 9. De twee twijfelpunten uit F6 zijn
verholpen (0,55/9,8 kregen hun rij; de Kleidon-toeschrijving "minstens een factor vijf"
is nu onze eigen verwachting, niet meer aan Kleidon toegeschreven), maar dat waren geen
fouten en geen "Voor een 9"-punten.

**Oefeningen (was 9, geen punt).** Ongewijzigd 9.

**Feitelijke fouten.** Geen gevonden en geen nieuwe. De twijfelpunten van F6 (583–584;
1095 Basu/Banz/Rosenberg; 823–824 Kleidon-toeschrijving) zijn ofwel opgelost (583–584,
823–824) ofwel bewust ongewijzigd gelaten omdat ze bij 03_16 horen (1095). Geen
verslechtering aangetroffen.

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: alle deelcijfers 9 → eindcijfer 9,0.

