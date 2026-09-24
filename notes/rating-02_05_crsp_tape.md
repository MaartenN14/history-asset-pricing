STATUS 02_05_crsp_tape F5c words=5133 prose=PASS open=1 cijfer=8,9 min=8,5

# Beoordeling 02_05_crsp_tape: De CRSP-tape, data als machine

## Eindcijfer: 8,0

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·8 + 0,1·8 + 0,1·7 + 0,1·8 + 0,05·9 = 7,95, afgerond 8,0.

## 1. Helderheid van de uitleg (8)

*Goed*
- "Het kernresultaat": stelling, bewijsidee in één zin, bewijs, en dan het toy als
  kleinste geval ($0{,}2 \times 0{,}75 = 15$ procentpunt) en een realistisch getal
  (1,6 procentpunt per maand bij Nasdaq). Zo hoort het.
- "Wat het voorspelt": de survivorship-formule krijgt twee uitgerekende gevallen (9,5% en
  0,012%) en een cel die ze nacontroleert; $x_0 = 1$ wordt vertaald naar "een koers van
  2,7 keer de drempel".
- Elke nieuwe term krijgt ter plekke een definitie: *delisting return*, $\plim$,
  *look-ahead bias*, $\Cov_{\text{cs}}$, aanpassingsfactor $k$.

*Aanmerkingen*
- "Intuïtie": "De vraag van Engel lijkt eenvoudig". Engel komt nergens eerder of later
  voor. De lezer weet niet wie dat is (Louis Engel van Merrill Lynch, die de vraag aan
  Lorie stelde) of welke vraag bedoeld is.
- "Intuïtie", slotzin: "extra waarnemingen maken de ruis kleiner, maar de vertekening
  niet kleiner dan die ruis." De zin zegt het omgekeerde van wat bedoeld is (de
  vertekening blijft staan terwijl de ruis krimpt) en is na twee keer lezen nog
  dubbelzinnig.
- "Shumway: de delisting return": de toets gebruikt "de voorspelling $h\,|D|$", niet de
  stelling $h(\mu_a - D)$. Voor de kleinste Nasdaq-portefeuille is $\mu_a$ 3,79% per maand,
  dus niet verwaarloosbaar ten opzichte van $|D| = 55\%$. Met de volle formule komt de
  Nasdaq-correctie op ongeveer 1,73 in plaats van 1,62. De lezer ziet niet waarom de
  benadering hier mag, terwijl de sectie juist de formule wil toetsen.
- "Weging", [](#eq-crsp-tape-bonus): de herbalanceringswinst staat er als gelijkheid,
  maar volgt uit de benadering $g \approx \mu - \sigma^2/2$; die stap ontbreekt.
- "Wat het voorspelt": "Na een eeuw is dat voor het kleine bedrijf nog
  $1{,}25 \times 0{,}50/\sqrt{100} = 6{,}3\%$ per jaar." De asymptoot wordt gebruikt alsof
  hij exact is (zie Feitelijke fouten).

*Beter uitleggen*
- Engel: één zin in het Overzicht wie hij was en welke vraag hij stelde.
- De Shumway-toets: of met $h(\mu_a - D)$ rekenen, of één zin waarom $\mu_a$ weg mag.
- De herbalanceringswinst: één regel dat $g \approx \mu - \sigma^2/2$.

*Voor een 9*: introduceer Engel ("Overzicht" of "Intuïtie", eerste zin); herschrijf de
slotzin van "Intuïtie"; reken in "Shumway" met de volle formule of motiveer de
benadering; markeer [](#eq-crsp-tape-bonus) als benadering; gebruik bij $T = 100$ de
exacte formule (5,3%) of noem 6,3% uitdrukkelijk de grens voor grote $T$.

## 2. Opbouw en rode draad (8)

*Goed*
- "Overzicht" stelt de vraag en geeft het antwoord; "Intuïtie" voorspelt drie dingen
  (te hoog, vooral klein, krimpt niet met data) en de theorie verwijst er twee keer
  expliciet naar terug ("Zoals de intuïtie voorspelde").
- Dezelfde getallen lopen door: het toy ($h = 1/5$, $D = -75\%$) is het kleinste geval
  van de stelling en keert terug in oefening 1; $D = -30\%$ van Shumway zit in de
  simulatie en in de replicatie.
- Routekaart aan het begin van "Theorie", "Samengevat" aan het eind, en de simulatie
  opent met haar conclusie ("meet ... een premie van vijf procentpunt").
- 4.927 woorden, onder de grens.

*Aanmerkingen*
- "Wat weging met een eeuw doet": de eerste replicatie meet het verschil tussen
  equal- en value-weighted, een bijthema uit de laatste theoriesectie. Het blok zegt
  niet waarom dit de toets is van de kernvraag (verdwenen bedrijven); die koppeling komt
  pas in de slotzin ("waar de fouten uit de theorie het grootst zijn").
- "Weging" in "Theorie" brengt twee nieuwe effecten ("Twee effecten komen daar nog bij":
  herbalanceringswinst en bid-ask bias) die in simulatie en replicatie niet meer apart
  worden gemeten. De Samengevat noemt ze niet.

*Beter uitleggen*
- In het eerste replicatieblok één zin: de weging is de meetbare schaduw van de
  delisting-fout, omdat die fout in het kleinste deciel zit.

*Voor een 9*: koppel de eerste replicatie in haar "Wat" aan de kernvraag; laat de
herbalanceringswinst en de bid-ask bias ofwel terugkomen (bijvoorbeeld in de
meetkundig/rekenkundig-kolom van de replicatie), ofwel schrap ze uit "Weging".

## 3. Taal (8)

*Goed*
- Korte zinnen (gemiddeld 14,6 woorden); geen u/je; heldere werkwoorden ("De tape ...
  meet").
- De drie motieven worden ter plekke uitgelegd ("de standaardfout van 2%: de onzekerheid
  die een eeuw jaarrendementen met 20% volatiliteit in een gemiddelde laat").

*Aanmerkingen*
- "Intuïtie": "maar de vertekening niet kleiner dan die ruis" (zie criterium 1): een
  zin die door haar bouw iets anders zegt dan bedoeld.
- "Shumway": "Zet men elk ontbrekend rendement op $-100\%$"; "men" is stijf naast de
  "we" van de rest van de lecture.
- Twaalf puntkomma's; enkele stapelen twee gedachten ("Equal-weighted geeft het
  kleinste deciel veel gewicht, omdat daar de meeste bedrijven zitten; value-weighted
  geeft het weinig.").
- "Overzicht": "Dat werk definieert het tijdvak" is vertaald Engels ("defines the era").

*Voor een 9*: herschrijf de slotzin van "Intuïtie"; vervang "men" door "we"; knip de
puntkomma-zinnen in "Replicatie"; "Dat werk definieert het tijdvak" naar natuurlijk
Nederlands ("Met dat werk begint het tijdvak").

## 4. Toy-voorbeeld (8)

*Goed*
- Vijf aandelen, vier perioden, alles met de hand; stappen 1 tot 5 zijn in vijf minuten
  na te rekenen en de codecel geeft een tabel hand/code met identieke getallen.
- De slotzin zegt wat de lezer nu weet: "de markt verloor 14% of won 13%, afhankelijk
  van één beslissing".

*Aanmerkingen*
- Meer dan één mechanisme: dividend, split, delisting return en survivorship zitten
  in één voorbeeld. Dividend en split zijn het recept, niet het punt, maar ze kosten
  twee rijen en twee stappen.

*Voor een 9*: haal dividend en split uit het toy (of maak er één regel "recept" van
vóór de tabel) zodat het toy alleen de twee selectiefouten toont.

## 5. Code en figuren (7)

*Goed*
- Toy-cel en `survivor_bias` lezen als de wiskunde, met docstrings.
- Beide figuren hebben een leeswijzer ervoor ("Let links op het kleine eind van de
  lijnen") en een figuurtekst die zegt wat te zien is.
- Presentatietabellen hebben Nederlandse kolomnamen.

*Aanmerkingen*
- `cel-crsp-tape-simfuncties`: `simulate` is ruim veertig regels met twee woordenboeken
  van arrays, vijf metingen en een tweede-doorgang-vlag. De truc om de toevalsgenerator
  terug te zetten (`state = rng.bit_generator.state`, twee keer `simulate`) is een
  compacte truc die de lezer niet uit de wiskunde herkent.
- `size_deciles` en `decile_mean`: `rankdata` op `np.where(mask, key, np.inf)` en
  `np.bincount` op samengestelde celindices zijn trucs; de tekst ervoor zegt alleen
  "de hulpfuncties".
- "Hoe kwetsbaar is die premie?": de cel mengt `print`-uitvoer met een tabel; de
  aandelen van het kleinste deciel in 1956/1976/2026 horen in de tabel.

*Beter uitleggen*
- Eén zin bij `simulate` over de rol van `last_delist` vóór de cel, niet alleen erna.

*Voor een 9*: splits `simulate` in een functie die paden en schrappingen genereert en
één die meet (dan is de overleversteekproef een filter achteraf en verdwijnt de
state-truc); schrijf `size_deciles`/`decile_mean` met een zichtbare lus of met een zin
die de truc uitlegt; vervang de `print`-regels door een tabel.

## 6. Replicatie en empirie (8)

*Goed*
- Twee replicatieblokken met bron, wat, data, verschil en verwachte afwijking, elk ruim
  onder 250 woorden, en een tabel origineel/hier voor Shumway.
- Elk oordeel begint met "Geslaagd" en verwijst naar de verwachting (0,1 procentpunt;
  0,2 procentpunt; verdwijnen na 1981).
- De break-even-cel maakt de kernvraag kwantitatief: 0,57% per maand bij $D = -55\%$.

*Aanmerkingen*
- "Wat weging met een eeuw doet": "Vanaf het vierde deciel is het verschil niet van nul
  te onderscheiden." Volgens de tabel al vanaf het derde (zie Feitelijke fouten).
- Size-premie per deelperiode: "Over de volle eeuw scheelt de weging vier procentpunt,
  meer dan de standaardfout van elk van beide." Het verschil van twee premies moet tegen
  de standaardfout van het verschil worden gezet, niet tegen die van elk afzonderlijk.
- "Shumway": de tolerantie van 0,2 procentpunt wordt gehaald met 0,197; met de volle
  formule (zie criterium 1) verschuiven beide afwijkingen. Het oordeel hangt dus aan de
  benadering.

*Voor een 9*: corrigeer "vierde" in "derde"; bereken de standaardfout van EW-premie min
VW-premie uit de maandelijkse verschilreeks; toets Shumway met $h(\mu_a - D)$ of noem de
benadering in de verwachte afwijking.

## 7. Oefeningen (9)

*Goed*
- Precies de drie typen: instap op het toy (oefening 1), afleiding met drift en discrete
  waarneming (oefening 2), uitbreiding van de replicatie per deelperiode (oefening 3).
- Elke uitwerking eindigt met "Wat dit leert", en oefening 2 verklaart het teken van de
  afwijking.

*Aanmerkingen*
- Oefening 2.1: de uitwerking zegt waar het bewijs misgaat, maar niet in welke richting
  de fout verandert bij positieve drift; een halve zin zou de afleiding afmaken.

## Feitelijke fouten

1. **"Wat het voorspelt"**: "Na een eeuw is dat voor het kleine bedrijf nog
   $1{,}25 \times 0{,}50/\sqrt{100} = 6{,}3\%$ per jaar." Dat is de asymptoot voor grote
   $T$. De exacte formule [](#eq-crsp-tape-survivorship) met $x_0 = 1$, $\sigma = 0{,}5$,
   $T = 100$ geeft $P = 2\Phi(0{,}2) - 1 = 0{,}159$ en een fout van
   $0{,}01 \times (1/0{,}159 - 1) = 5{,}3\%$ per jaar. De benadering zit er 1 procentpunt
   naast.
2. **"Wat weging met een eeuw doet"**, oordeel: "Vanaf het vierde deciel is het verschil
   niet van nul te onderscheiden." In de tabel heeft het derde deciel $t = 1{,}18$ (0,40
   procentpunt, SE 0,34). Het klopt vanaf het derde deciel; alleen deciel 1 ($t = 5{,}2$)
   en 2 ($t = 2{,}1$) zijn significant.

Nagerekend en correct: alle toy-getallen (2,0 / −1,0 / −15,0 / 0,0; −3,50 / +0,25 /
+3,13; −14,17 / +0,98 / +12,88; −4,55%); stelling 1 en het bewijs; overleefkans 0,345 en
fout 9,5% / 0,012%; asymptoot $\sqrt{\pi/2}\,\sigma/\sqrt T$; $-N\Cov_{\text{cs}}$ in
[](#eq-crsp-tape-ewvw); bonusvoorbeeld 10%; bid-ask 0,25% per maand ≈ 3% per jaar;
simulatie (5,48 / 14,54 / SD 1,0; 1,44% en 5,43; 12,29 → 13,30 / 16,95; 11,97 → 12,00);
replicatie (11,63 / 11,55; 3,1; factor 5,9; 3,77 met $t$ 5,2; kleinste deciel EW/VW
eindwaarde factor 25, "ruim een orde van grootte"); Shumway-tabel (1,62 / 1,82; 1,56 /
1,45); deelperioden (18,6 / 10,3; SE 2,4–2,6; 9,2 − 5,2); break-even 0,31% en 0,57%;
10% / 54% / 39% in het kleinste deciel; oefeningen 1–3. De gepubliceerde tabelwaarden
van Shumway (1997) en Shumway en Warther (1999) zijn niet tegen de papers gecontroleerd.

## De drie verbeteringen met het meeste effect

1. **Simulatiecode leesbaar maken** (`cel-crsp-tape-simfuncties` en de hulpfuncties):
   genereren en meten scheiden, de state-truc weg, de decielfuncties uitleggen. Code en
   figuren 7 → 8,5.
2. **Helderheid op vijf plekken**: Engel introduceren, de slotzin van "Intuïtie", de
   Shumway-toets met $h(\mu_a - D)$, de herbalanceringswinst als benadering, de
   eeuw-waarde exact (5,3%). Helderheid 8 → 9; lost feitelijke fout 1 op.
3. **Replicatie aan de kernvraag koppelen en precies maken**: het weegblok zegt waarom
   de weging de delisting-fout zichtbaar maakt, "derde" in plaats van "vierde" deciel,
   standaardfout van het premieverschil. Opbouw 8 → 9, replicatie 8 → 9; lost feitelijke
   fout 2 op.

## Navertelling in vijf zinnen

Een rendementsdatabase moet dividenden, splits en vooral het laatste rendement van
verdwenen bedrijven meetellen, anders valt het gemiddelde te hoog uit. De fout is de
schrappingskans maal het gemiste verlies, en bij een steekproef van overlevers nog veel
groter; beide zitten bij kleine aandelen en krimpen niet met meer data. In een gesimuleerd
universum zonder size-premie maken deze fouten een premie van 5 tot 15 procentpunt, en
look-ahead keert het teken om. Op French-data verschuift de weging het marktrendement
van een eeuw met 3,1 procentpunt, bijna geheel via het kleinste deciel, en de
gepubliceerde Shumway-correcties volgen uit $h\,|D|$. De size-premie is na 1981 weg en
zou met een bescheiden aantal ontbrekende delisting returns helemaal verklaard kunnen
worden. Dit komt overeen met het Overzicht.

## Controle 1

Gecontroleerd op de versie na F5-1 (5.133 woorden, `--check` PASS). Alleen de eigen
punten. Nieuwe getallen nagerekend: Nasdaq $0{,}0295 \times (0{,}0379 + 0{,}55) = 1{,}734$;
Shumway $12h = 5{,}21/1{,}0177 = 5{,}119$ en $5{,}119 \times (0{,}0177 + 0{,}30) = 1{,}627$;
eeuw-rij $P = 0{,}1585$, fout $5{,}31\%$; meetkundig 12,30 tegen 10,33; weegverschil
van de premie 3,93 met SE 0,76; break-even 0,31% per maand bij $D = -100\%$.

**Feitelijke fouten**
1. Eeuw-waarde 6,3%: **opgelost** (exacte formule, 5,3%, en een derde rij in de cel).
2. "vierde" deciel: **opgelost** ("derde").
3. Nieuw: "Wat weging met een eeuw doet", alinea na het oordeel: "Binnen dat deciel doet
   equal-weighted het bovendien nog eens beter, door de bid-ask bias, de
   herbalanceringswinst en de ontbrekende delisting returns." Het verschil in de tabel
   is een verschil in *rekenkundig* gemiddelde (3,77 punt). De herbalanceringswinst
   verhoogt alleen de meetkundige groei; de lecture zegt zelf bij
   [](#eq-crsp-tape-bonus): "Het verwachte rendement stijgt daardoor niet." De
   herbalanceringswinst hoort niet in deze opsomming (wel in de alinea over het
   meetkundig gemiddelde, waar ze al staat).

**1. Helderheid**
- Engel niet geïntroduceerd: **opgelost** (naam geschrapt; de vraag staat nu zonder
  persoon).
- Slotzin "Intuïtie": **opgelost** ("De vertekening blijft staan, of krimpt hoogstens
  even snel als de ruis"; klopt met beide stellingen).
- Shumway met $h|D|$: **opgelost** (stelling $h(\mu_a - D)$ met $\mu_a$ per maand).
- Herbalanceringswinst als gelijkheid: **opgelost** ("Met $g \approx \mu - \tfrac12\sigma^2$
  ... geldt bij benadering").
- Eeuw-asymptoot: **opgelost**.

**2. Opbouw**
- Weegreplicatie los van de kernvraag: **opgelost** ("De weging is de meetbare schaduw van
  de delisting-fout").
- Herbalanceringswinst en bid-ask niet teruggekomen: **opgelost** (Samengevat; meetkundig
  tegen rekenkundig in de replicatie), met de kanttekening van feitelijke fout 3.

**3. Taal**
- Slotzin "Intuïtie": **opgelost**.
- "men": **opgelost**.
- Puntkomma-zinnen in "Replicatie": **opgelost** (één nieuwe in "Wat het voorspelt":
  "per jaar; de cel hierboven rekent het na", klein).
- "Dat werk definieert het tijdvak": **opgelost**.

**4. Toy**
- Te veel mechanismen: **deels**. Dividend en split zijn samengevoegd tot één stap
  "recept"; ze blijven, met de verwijzing naar STYLE §11.7 (het toy gebruikt de ene
  formule die de theorie als eerste afleidt). Aanvaard.

**5. Code en figuren**
- `simulate` met state-truc: **opgelost** (`draw_universe`, `last_delisting`, `measure`;
  `copy.deepcopy(rng)` met een zin ervoor).
- `size_deciles`/`decile_mean`: **opgelost** (benoemde tussenresultaten, lus over tien
  decielen, zin vóór de cel).
- `print` in de break-even-cel: **opgelost** (aparte tabel).

**6. Replicatie**
- "vierde" deciel: **opgelost**.
- SE van het premieverschil: **opgelost** (kolommen "EW - VW" en "SE EW - VW"; 3,9 met SE
  0,8).
- Oordeel hangt aan de benadering: **opgelost** (beide binnen 0,2 punt met de volle
  formule: 0,09 en 0,18).
- Nieuw: feitelijke fout 3.

**7. Oefeningen**
- Oefening 2.1 zonder richting: **opgelost** ("Bij positieve drift ... de fout blijft
  positief, maar wordt kleiner").

**Nieuwe cijfers**

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 8 | 9 |
| 2 | Opbouw | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy | 10% | 8 | 8,5 |
| 5 | Code en figuren | 10% | 7 | 9 |
| 6 | Replicatie | 10% | 8 | 8,5 |
| 7 | Oefeningen | 5% | 9 | 9 |

Eindcijfer: 0,3·9 + 0,2·9 + 0,15·9 + 0,1·8,5 + 0,1·9 + 0,1·8,5 + 0,05·9 = 8,90, **8,9**.
Laagste deelcijfer 8,5. Streefcijfer gehaald; één feitelijke fout open.

Wat nog moet: de herbalanceringswinst uit de opsomming van bronnen van het rekenkundige
verschil halen (feitelijke fout 3). Dan replicatie 9.
