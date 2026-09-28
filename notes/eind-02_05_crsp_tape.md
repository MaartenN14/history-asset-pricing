STATUS 02_05_crsp_tape F6c words=5671 prose=PASS open=0 cijfer=9,0 min=9,0

# Ronde 9+

Vorige ronde: 8,5

Eindbeoordeling F6 van `lectures/02_05_crsp_tape.md` (De CRSP-tape: data als machine), na
de taalredactie. Gelezen: alleen de .md; getallen nagerekend met de hand en tegen de
nagerekende celuitvoer uit de vorige ronde (de .ipynb is niet geopend).
`prose_stats --check`: PASS (5498 woorden, zin gemiddeld 16,9, p90 27, geen zin > 40,
alinea 49, colon_mid 0,9, tmpl 2, wie_open 2).

## De drie verbeteringen met het meeste effect

1. **Eén naam voor de weging, ook in kop, legenda en tabel (taal 8,5 → 9; code en figuren
   8,5 → 9).** De proza zegt nu overal gelijk- en waardegewogen, maar de kop op
   02_05_crsp_tape.md:412 ("Weging: equal-weighted tegenover value-weighted") en de
   legenda's op :841–844 ("value-weighted markt", "equal-weighted, alle bedrijven",
   "kleinste deciel, equal-weighted", "kleinste deciel, value-weighted") zijn Engels. Dat
   moet om: figuurteksten zijn Nederlands (rubriek, "wat niet meetelt" 3) en H7 vraagt één
   naam per begrip. De afkortingen EW en VW staan in de formule op :426 en in vier
   tabellen (:578–579, :778, :810, :962) zonder dat de tekst ze invoert; zet ze als alias
   tussen de bestaande haakjes op :136 en :297 ("*equal-weighted*, EW"). Splits daarbij
   `measure` (:575–601, 27 regels) in een deciel- en een marktdeel [onderzoek A].
2. **De bovengrens in de eerste replicatie goed onderbouwen (helderheid 8,5 → 9).** De
   admonition op :743–746 zegt dat het weegverschil in het kleinste deciel een bovengrens
   is "want alleen gelijkgewogen weging geeft dat deciel gewicht". Die reden gaat over de
   weging tússen decielen, terwijl de bovengrens over het verschil bínnen het deciel gaat,
   en de voorwaarde (de andere bronnen zijn niet negatief) staat pas op :829. Herschrijf
   de zin met de juiste reden en de voorwaarde. Herschrijf ook :988–989 (zie taal).
3. **Een tabel origineel/hier in "Wat weging met een eeuw doet" (replicatie 8,5 → 9).** De
   eerste replicatie heeft geen tabel origineel/hier; het getal van Fisher en Lorie
   (9,0%, 1926–1960) staat alleen in een verwijzing. Zet het meetkundige gemiddelde van de
   marktreeks en van `ew_all` over dezelfde jaren naast de 9,0%, of zeg in de admonition
   dat deze replicatie geen origineel getal nabootst en alleen de weging meet.

## Eindcijfer: 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

8,5·0,25 + 9·0,20 + 8,5·0,20 + 9·0,10 + 8,5·0,10 + 8,5·0,10 + 9·0,05 = 8,675 → 8,7.
Laagste deelcijfer 8,5; taal ≥ 8 blokkeert niet. Streefcijfer 9,0 niet gehaald.

## 1. Helderheid van de uitleg (8,5)

*Goed*
- **Het kernresultaat.** De stelling krijgt meteen het toy-getal (15 procentpunt, :289–291)
  en het Nasdaq-getal (1,7 procentpunt per maand, :295–296), en de simulatie toetst haar
  per deciel met de exacte vorm $h(0{,}01 - r^{\text{s}})/(1-h)$ (:649).
- **Wat het voorspelt.** De survivorship-formule wordt eerst in woorden gelezen (:341–344),
  dan met twee bedrijven doorgerekend (9,5% tegen 0,012%) en asymptotisch met een getal na
  een eeuw (5,3%).
- **Weging.** Herbalanceringswinst en bid-ask bias krijgen elk een uitgerekend getal (10%
  en drie procentpunt per jaar, :448–457).

*Aanmerkingen*
- **Replicatie → Wat weging met een eeuw doet, admonition (:743–746).** "Het weegverschil
  in het kleinste deciel is een bovengrens voor de fout door ontbrekende delisting returns,
  want alleen gelijkgewogen weging geeft dat deciel gewicht." De reden klopt niet bij de
  bewering (zie verbetering 2).
- **Replicatie → Shumway (:988).** "De rij $r^{\text{s}} = -100\%$ is de premie zelf, 0,31%
  per maand." Waarom de schrappingskans bij $-100\%$ gelijk is aan de premie ($h \cdot 1$),
  moet de lezer zelf afleiden.
- **Weging (:426).** $R^{\text{EW}}$ en $R^{\text{VW}}$ verschijnen zonder dat de tekst de
  afkortingen noemt.

*Beter uitleggen*
- De break-even-tabel: één bijzin dat de stelling $h = \text{premie}/|r^{\text{s}}|$ geeft,
  zodat bij $-100\%$ de kans gelijk is aan de premie.
- De bovengrens: de reden (binnen het deciel is EW − VW de som van size-premie, bid-ask
  bias en delisting-fout) en de voorwaarde op één plek.

*Voor een 9*
- 02_05_crsp_tape.md:743–746: reden en voorwaarde van de bovengrens herschrijven.
- 02_05_crsp_tape.md:988–989: de rij $-100\%$ in één bijzin verklaren (in dezelfde zin).
- 02_05_crsp_tape.md:136 en :297: EW en VW als alias tussen de bestaande haakjes.

## 2. Opbouw en rode draad (9)

*Goed*
- **Overzicht en Intuïtie.** De vraag en het antwoord staan vooraan (:37–41); de intuïtie
  voorspelt teken (te hoog), plaats (kleine aandelen) en het effect van meer jaren (weinig),
  en de theorie lost elk ervan in een gewone zin in (:384–386, :388–394, :679–681).
- **Routekaart en Samengevat.** Theorie opent met vier stappen (:194–199) en sluit met een
  Samengevat die per resultaat de richting geeft.
- **Lengte.** 5498 woorden, binnen de 6.000.

*Aanmerkingen*
- **Herhaling van één boodschap.** Dat meer data de fout niet wegnemen staat op :40–41,
  :88–89, :388–394, :729–730 en :1025–1026. De formuleringen verschillen nu, maar :1025–1026
  ("omdat de ene fout blijft staan en de andere niet sneller afneemt dan de ruis") herhaalt
  :40–41 nog vrijwel inhoudelijk [onderzoek A, deels opgelost].

*Beter uitleggen*
- Niets wezenlijks; de lezer weet na het Overzicht wat komt.

## 3. Taal (8,5)

*Goed*
- **Verband.** De redactie heeft de telegramzinnen en "Nu …"-aankondigingen weggewerkt
  (:623, :668–669, :940–941); zinnen lopen met voegwoorden door [onderzoek A: :626–628,
  :672/942, :189–190 opgelost].
- **Mengtaal in de proza.** "Gelijkgewogen" en "waardegewogen" staan nu in de lopende tekst,
  met de Engelse term één keer tussen haakjes (:136, :297) [onderzoek A P6 opgelost in de
  proza].
- **Sjablonen.** "In woorden:" en de dubbele "Zoals de intuïtie voorspelde" zijn weg; motief-
  namen elk hoogstens twee keer; drie "Wie …"-zinnen.

*Aanmerkingen*
- **Weging (:412).** "Weging: equal-weighted tegenover value-weighted" — de kop spreekt de
  tekst eronder tegen (H7) [onderzoek A P6, nog open].
- **Overzicht (:40–41).** "Meer data lossen dat niet op, omdat de fout door ontbrekende
  delisting returns blijft staan en die van overlevenden hoogstens even snel krimpt als de
  ruis." Te dicht voor een openingsalinea, vóór het begrip overlevenden is ingevoerd.
- **Replicatie (:829–830).** "… is 3,77 procentpunt wel een bovengrens voor wat de weging
  via ontbrekende delisting returns in dit deciel kan doen." Wat "de weging kan doen via"
  iets, zegt niemand hardop.
- **Replicatie → Shumway (:988–989).** "Ze verdwijnt als 0,57% van het kleinste deciel per
  maand verdwijnt met een ontbrekend rendement van $-55\%$." Twee keer "verdwijnt" met twee
  betekenissen.
- **Weging met een eeuw (:832).** "Het gelijkgewogen marktrendement is dus vooral een
  uitspraak over het kleinste deciel" opent een alinea met "dus" zonder direct antecedent
  [onderzoek A, nog open]. :803 "Toch is geen enkel aandeel anders gemeten." sluit beter
  aan dan vroeger, maar het contrast (met de zesvoudige eindwaarde) staat twee zinnen terug.

*Beter uitleggen*
- Taal is geen uitlegpunt; zie de hardop-toets hieronder.

*Voor een 9*
- 02_05_crsp_tape.md:412: kop "Weging: gelijkgewogen tegenover waardegewogen".
- 02_05_crsp_tape.md:40–41, :829–830, :988–989: herschrijven (zie hardop-toets).
- 02_05_crsp_tape.md:803 en :832: het contrast en de conclusie aan de zin ervoor vastmaken.

## 4. Toy-voorbeeld (9)

*Goed*
- **Vijf aandelen, vier perioden.** Met de hand na te rekenen in vijf minuten, één
  mechanisme, tabel hand/code (:179–184) en een slotzin met betekenis (:187–190).
- **Terugkeer.** Het toy is "het kleinste geval van de stelling" (:289–291) en keert terug
  in oefening 1.

*Aanmerkingen*
- Geen. De simulatie kalibreert op Shumway ($-30\%$, 2%) en niet op het toy; dat is hier
  terecht.

*Beter uitleggen*
- Niets.

## 5. Code en figuren (8,5)

*Goed*
- **Leeswijzers.** Vóór beide figuren staat waarop te letten (:681–683, :832–834), erna een
  bijschrift dat zegt wat te zien is.
- **Code leest als de wiskunde.** `total_returns`, `survivor_bias` en `draw_universe`
  volgen de formules; de lus over maanden is zichtbaar; de tweelingtrekking wordt uitgelegd
  (:604–606).

*Aanmerkingen*
- **Figuur weging (:841–844).** De legenda's "value-weighted markt", "equal-weighted, alle
  bedrijven", "kleinste deciel, equal-weighted", "kleinste deciel, value-weighted" zijn
  figuurtekst en dus Nederlands te maken; het bijschrift eronder zegt al "gelijkgewogen".
- **Simulatie (:575–601).** `measure` telt 27 regels, boven de 25 van §11.8 [onderzoek A].
- **Tabellen.** Kolommen "EW premie", "VW markt (Mkt)", "EW - VW" gebruiken afkortingen die
  de tekst niet invoert (zie helderheid).

*Beter uitleggen*
- Niets aan de figuren zelf.

*Voor een 9*
- 02_05_crsp_tape.md:841–844: legenda's "waardegewogen markt", "gelijkgewogen, alle
  bedrijven", "kleinste deciel, gelijkgewogen", "kleinste deciel, waardegewogen".
- 02_05_crsp_tape.md:575–601: `measure` splitsen in decielmeting en marktmeting.

## 6. Replicatie en empirie (8,5)

*Goed*
- **Shumway.** Tabel origineel/hier met verschilkolom (:927–934), oordeel "Geslaagd" dat naar
  de aangekondigde 0,2 procentpunt verwijst (:937), en een eerlijke zin over welke rij een
  onafhankelijke toets is (:905–907).
- **Break-even.** De vraag "hoe kwetsbaar is die premie" krijgt een getal (0,57% per maand)
  en een vergelijking met Shumway en Warthers 2,95%.

*Aanmerkingen*
- **Wat weging met een eeuw doet.** Er is geen tabel origineel/hier; "Alle drie de
  verwachtingen van hierboven komen uit." (:818) verwijst naar de admonition, maar de
  verwachting over de reconstructie is al op :799 afgehandeld.
- **Getallen in lopende tekst (:970–973).** "18,6 tegen 10,3 procentpunt per jaar tot 1962
  … ruim twee procentpunt … vier procentpunt … 0,8 procentpunt" — vijf getallen in één
  alinea, die in de tabel erboven staan.

*Beter uitleggen*
- Zeg in de admonition wat deze replicatie van Fisher en Lorie nabootst en wat niet.

*Voor een 9*
- 02_05_crsp_tape.md:743–758: tabel origineel/hier of een expliciete zin dat er geen
  origineel getal wordt nagebootst (verbetering 3); reden van de bovengrens herstellen.
- 02_05_crsp_tape.md:970–973: terugbrengen tot twee getallen en naar de tabel verwijzen.

## 7. Oefeningen (9)

*Goed*
- **Instap, afleiding, uitbreiding.** Oefening 1 varieert het toy ($v = 0$), oefening 2
  breekt het bewijs (drift, discrete waarneming), oefening 3 breidt de replicatie uit.
- **Les.** Elke uitwerking sluit met wat ze leert (:1073–1075, :1122–1123, :1170–1171).

*Aanmerkingen*
- Geen.

## Feitelijke fouten

1. **Replicatie, admonition (:745–746).** "want alleen gelijkgewogen weging geeft dat
   deciel gewicht" — onjuiste onderbouwing: het weegverschil in het kleinste deciel is het
   verschil binnen het deciel, en de bovengrens geldt alleen als size-premie en bid-ask
   bias niet negatief zijn (:829). Voorstel: reden en voorwaarde samen noemen.
2. **Afronding (:366–367 en :479–480).** "een size-premie van negen procentpunt" bij 9,5%
   min 0,012%, en "vijf procentpunt" (5,5) naast "vijftien" (14,5): de afronding gaat de
   ene keer omlaag, de andere keer omhoog. Voorstel: "ruim negen", "vijfenhalf", "veertienenhalf"
   of overal één decimaal.

Nagerekend en juist: toy (2,0; −1,0; −15,0; 0,0 → −3,50%; +0,25%; +3,13%; cumulatief
−14,17%, +0,98%, +12,88%); 0% en −4,55%, +10% en −45% (:224–226); 15 procentpunt (:290);
$0{,}0295 \times 0{,}588 = 1{,}73$ (:296); $e^1 = 2{,}7$; $2\Phi(0{,}447) - 1 = 0{,}345$ en
9,5%; 0,012%; $\sqrt{\pi/2} = 1{,}25$; $2\Phi(0{,}2) - 1 = 0{,}159$ en 5,3%; $\tfrac12 \times
0{,}25 \times 0{,}8 = 10\%$; $s^2 = 0{,}25\%$ per maand → drie procentpunt per jaar; teken van
$-N\Cov_{\text{cs}}$; voorspelde fout $h(0{,}01 - r^{\text{s}})/(1-h)$ (:649) volgt uit
$\mu_a$; 3,2% schrappingen per jaar; 5,5 procentpunt (≈ 5,7 SD); 1,44% en 5,43 procentpunt;
11,97% → 12,00%; 11,63% tegen 11,55% (binnen 0,1); 3,1 procentpunt en eindwaarde ×5,9;
12,30% tegen 10,33%; 3,77 met $t = 5{,}2$; 5,21 = 21,28 − 16,07; 21,28/12 = 1,77%;
5,21/1,0177 = 5,12; 5,12 × 0,3177 = 1,63 tegen 1,45; 2,95 × 0,5879 = 1,73 tegen 1,82;
18,6 tegen 10,3; 3,9 met SE 0,76; 0,31% en 0,31/0,55 = 0,57%; 10%, 54%, 39%; 11,7% en SE 3,9
over 1926–1960 en 6,9% (00_01:736, :954–955); oefeningen (−20%; 0,368/0,345; 9,3/9,5%;
8,0 → 3,1 → 0,6 met SE 1,1).

## Navertelling in vijf zinnen

Een rendementsdatabase is geen neutrale meting: hoe ze dividenden, splits en vooral
verdwenen bedrijven behandelt, bepaalt het gemiddelde dat eruit komt. Mist de database het
laatste rendement van geschrapte aandelen, dan ligt het gemiddelde te hoog met de
schrappingskans maal het gemiste verlies, en een steekproef van alleen overlevenden maakt
zelfs uit een nulrendement een positief rendement. Omdat kleine aandelen het vaakst
verdwijnen, ontstaat zo een size-premie die in een gelijkgewogen gemiddelde vol doorwerkt
en in een waardegewogen nauwelijks, en meer jaren data halen haar niet weg. In de
French-data ligt het gelijkgewogen marktrendement 3,1 procentpunt per jaar hoger, vrijwel
geheel via het kleinste deciel, en de correcties van Shumway volgen uit de formule met
twee getallen. De size-premie verdwijnt na 1981 en is klein genoeg om door een plausibele
schrappingskans zonder geregistreerd laatste rendement verklaard te worden. Dit komt
overeen met het Overzicht.

## Oordeel over de taal na de redactie

De redactie heeft gewerkt: de tekst leest nu grotendeels als gesproken academisch
Nederlands, de telegramzinnen en vaste formules uit de vorige ronde zijn weg, en de
Engelse weegtermen zijn in de proza vervangen. Wat blijft, zijn de Engelse kop en legenda's
en enkele te dichte of dubbelzinnige zinnen. Hardop-toets, drie zinnen die nog niet
natuurlijk klinken:

1. :40–41 "Meer data lossen dat niet op, omdat de fout door ontbrekende delisting returns
   blijft staan en die van overlevenden hoogstens even snel krimpt als de ruis."
   → "Meer data helpen niet: de fout door ontbrekende laatste rendementen blijft elk jaar
   even groot, en de fout door alleen overlevenden te tellen krimpt niet sneller dan de
   ruis."
2. :829–830 "… is 3,77 procentpunt wel een bovengrens voor wat de weging via ontbrekende
   delisting returns in dit deciel kan doen."
   → "… kunnen ontbrekende delisting returns in dit deciel hoogstens 3,77 procentpunt van
   het weegverschil verklaren."
3. :988–989 "Ze verdwijnt als 0,57% van het kleinste deciel per maand verdwijnt met een
   ontbrekend rendement van $-55\%$."
   → "De premie is weg als elke maand 0,57% van het kleinste deciel van de beurs gaat met
   een ontbrekend rendement van $-55\%$."

## Controle 1

Gecontroleerd: alleen `lectures/02_05_crsp_tape.md` (eenmaal volledig gelezen, nu 5671 woorden),
tegen de punten hierboven en tegen `notes/rapport-02_05_crsp_tape.md` §"R9-1 (F6b, ronde 9+)".
Celuitvoer gecontroleerd met `uv run python tools/nb_outputs.py lectures/02_05_crsp_tape.ipynb`.

**Extra controle (Fisher & Lorie 9,0% tegen de markt, 1926-1960).** Cel `fisher_lorie` (:839-844)
geeft in de celuitvoer VW markt (Mkt) hier = 0,0939 en EW alle bedrijven hier = 0,1287
(origineel 0,09 in beide rijen). De tekst erna (:846-849) citeert dat correct: "vier tienden van
een procentpunt boven de 9,0%" voor waardegewogen (0,39 pp verschil) en "bijna vier procentpunt"
voor gelijkgewogen (3,87 pp verschil). Klopt.

**Feitelijke fouten**
1. Admonition bovengrens: opgelost. De Replicatie-admonition (:770-775) geeft nu de reden
   (weegverschil binnen het kleinste deciel = size-premie + bid-ask bias + fout door
   ontbrekende delisting returns) en de voorwaarde (eerste twee niet negatief) samen.
2. Afronding: opgelost. "ruim negen procentpunt" (:376), "vijfenhalf" en "veertienenhalf"
   (:493-494).

**Drie verbeteringen (F6)**
1. Eén naam voor de weging: opgelost. Kop :424 "Weging: gelijkgewogen tegenover waardegewogen";
   EW/VW als alias op :136 en :306-307; figuurlegenda's (:889-894) in het Nederlands;
   `measure` gesplitst in `decile_returns`, `market_returns` en een korte `measure` (11 regels,
   onder de 25 van §11.8).
2. Bovengrens goed onderbouwen: opgelost, zie feitelijke fout 1.
3. Tabel origineel/hier: opgelost. Nieuwe cel `fisher_lorie` (:839-844) met origineel/hier/
   verschil; de admonition zegt vooraf wat wordt vergeleken (:770-771).

**Helderheid, Voor een 9** — alle drie opgelost: bovengrens-reden (zie boven); Shumway-rij
$r^{\text{s}}=-100\%$ verklaard met de bijzin "omdat de cel $h = \text{premie}/|r^{\text{s}}|$
rekent" (:1038-1040); EW/VW als alias op :136 en :306-307.

**Taal, Voor een 9** — alle drie opgelost: kop :424; hardop-zinnen herschreven (:40-42 met
"want" i.p.v. de oude dubbele punt-achtige constructie, :874-878 tot "kunnen ontbrekende
delisting returns in dit deciel hoogstens 3,77 procentpunt van het weegverschil verklaren",
:1038-1040 zonder dubbel "verdwijnt"); "Toch"-contrast en "dus"-opening vastgemaakt
(:830-834 één zin met "terwijl geen enkel aandeel anders is gemeten"; :880-881 opent nu met
"Omdat het kleinste deciel ..." i.p.v. "dus").

**Code en figuren, Voor een 9** — beide opgelost: legenda's (:889-894) Nederlands; `measure`
gesplitst (zie boven).

**Replicatie, Voor een 9** — beide opgelost: tabel origineel/hier (cel `fisher_lorie`);
:970-973 (nu :1020-1023) teruggebracht van vijf naar twee getallen (18,6; 10,3) plus "ruim
vijf standaardfouten" in plaats van drie losse procentpunten.

**Opbouw, aanmerking herhaling (:1025-1026, nu in "Wat er brak").** Verder opgelost: de
verklarende bijzin is geschrapt, de zin verwijst nu alleen nog naar de standaardfout van 2%.
Criterium stond al op het maximum van 9 en blijft daar.

**Nieuwe punten.** Geen. Geen verslechtering en geen nieuwe feitelijke fout gevonden bij het
opnieuw lezen van het college.

## Eindcijfer: 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Alle zeven deelcijfers 9 (elk had een punt bij de eindbeoordelaar met plafond 9, op Opbouw,
Toy en Oefeningen na, die al op 9 stonden) → eindcijfer 9,0. Laagste deelcijfer 9,0; taal 9
blokkeert niet. Streefcijfer 9,0 gehaald.
