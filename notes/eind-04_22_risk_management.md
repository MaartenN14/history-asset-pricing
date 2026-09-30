STATUS 04_22_risk_management F6c words=5926 prose=PASS open=0 cijfer=9,0 min=8,5

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

## Eerste herziening (workflow §12)

Eerste herziening van dit college; er is geen vorig cijfer. Gelezen: de volledige .md,
de celuitvoer (`tools/nb_outputs.py`), kaart-rollen, rubriek, STYLE §11.12 en
notes/taal-04_22_risk_management.md. Getallen in toy, simulatie, replicatie en oefeningen
zijn nagerekend tegen de celuitvoer; op twee interpretaties na (zie "Feitelijke fouten")
kloppen ze.

## De drie verbeteringen met het meeste effect

1. **Maak de theta van de simulatie zichtbaar en herstel de verklaring bij de fire sale**
   (helderheid 8,5 → 9,0; toy 8,5 → 9,0 via H11). In de simulatie is
   $\theta = XD\kappa/h = L \times 5 \times 0{,}0002/0{,}02 = 0{,}05\,L$, dus 0,5 bij
   hefboom 10, precies 1 bij hefboom 20 en 1,25 bij hefboom 25. Dat is exact de grens uit
   [](#prop-risk-management-spiraal) ("Bij $\theta \ge 1$ divergeert de reeks") en verklaart
   waarom de ruïnelijnen juist boven hefboom 20 uiteenlopen. De huidige reden ("omdat
   $\theta$ alleen groot is bij een fonds dat vaak tegen zijn limiet aan zit",
   lectures/04_22_risk_management.md:924–925) klopt niet: $\theta$ hangt af van de positie,
   niet van hoe vaak de limiet bindt. Herschrijf die zin met de twee redenen (theta 0,5 en
   een fonds dat bij hefboom 10 bijna nooit tegen de limiet aanloopt, margin call 0,9%).
   Noem daarbij dat $\kappa$ in de simulatie twee keer die van het toy is (toy: 1 bp per 100
   bij vermogen 100, dus 1 bp per eenheid beginvermogen; simulatie: 2 bp).
2. **Haal de genummerde verwachtingen weg** (taal 8,5 → 9,0; opbouw blijft 9,0). H12 vraagt
   voorspellingen zonder nummering; nu verwijst de tekst vier keer met een rangtelwoord
   terug ("Dat bevestigt de tweede verwachting", r. 408; "de helft van de derde
   verwachting", r. 640; "De eerste verwachting klopt dus", r. 818–819; "Daarmee klopt ook
   de derde verwachting", r. 925). Zeg telkens wat er voorspeld werd ("dat twee obligaties
   samen een hogere VaR krijgen, zien we nu bewezen") en herschrijf daarbij de drie zinnen
   uit de hardop-toets hieronder.
3. **Eén naam voor diversificatie en één voor dispersie** (helderheid, samen met 1 naar
   9,0). "Spreiding" betekent op r. 41, 157, 268 en 684 diversificatie en op r. 79–80
   ("vraagt het alleen de spreiding van morgen", "de goed meetbare spreiding") de
   standaarddeviatie. In de Intuïtie staan beide betekenissen binnen vier regels
   (r. 78–80: "beloont posities die elkaar opheffen … alleen de goed meetbare spreiding
   blijft over"). Gebruik op r. 79–80 "volatiliteit" of "standaarddeviatie"; dat punt stond
   al vóór de taalredactie in de tekst en is dus geen redactiefout.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Eindcijfer** | | **8,7** (8,725) |

### 1. Helderheid van de uitleg: 8,5

*Goed.*
- Opzet: VaR en Expected Shortfall. De definitie geeft de integraalvorm en direct de
  lezing "verwachte verlies op de dagen waarop de VaR wordt overschreden"; het getal
  staat naast de formule (2,326 en 2,665 bij 99%, 2,338 bij 97,5%), met de economische
  reden voor de keuze van 97,5% door het Comité.
- Het kernresultaat: VaR is niet coherent, ES wel. Elk axioma krijgt een reden in
  één zin (afdelingen opsplitsen), en het tegenvoorbeeld is toy (b) met dezelfde
  getallen (98 tegen −4, 101,26 tegen 159,2).
- Hoe het getoetst wordt. De standaardfout van 0,63 procentpunt (63% van de kans zelf)
  maakt het zwakke punt van de backtest in één getal zichtbaar.

*Aanmerkingen.*
- Simulatie, Vier goede jaren: "Bij hefboom 10 of minder is er geen verschil, omdat
  $\theta$ alleen groot is bij een fonds dat vaak tegen zijn limiet aan zit." $\theta$ hangt
  af van de positie en dus van de hefboom, niet van de frequentie van de margin call.
- Intuïtie: "Omdat het verwachte rendement over één dag verwaarloosbaar is, vraagt het
  alleen de spreiding van morgen." Twee alinea's eerder en daarna betekent "spreiding"
  diversificatie (H7).
- Opzet: "$\mathrm{VaR}_{\alpha,t} = \inf\{\ell \in \mathbb{R} : \dots\}$" en de coherente
  risicomaat met "$m \in \mathbb{R}$": $\ell$ is volgens de setup het log rendement en $m$ de
  stochastische discontofactor. Hier geen verwarring in de afleiding, wel een botsing
  met de notatie van het boek (H2).
- Intuïtie: "De eerste is volgens Santa-Clara dat VaR niets zegt over de dagen die de
  grens overschrijden". Wie Santa-Clara is (en waarom een leerboek uit 2026 de bron is
  van een punt uit 1999) blijft onvermeld.

*Beter uitleggen.* De lezer krijgt de spiraalformule met toy-theta 0,625 mee, maar niet
dat de simulatie met $\kappa = 2$ bp per eenheid voorbij $\theta = 1$ komt. Eén getal
(theta bij hefboom 10, 20 en 25) maakt de fire-sale-tabel begrijpelijk. De dubbele
betekenis van "spreiding" vraagt een tweede woord.

*Voor een 9.*
- lectures/04_22_risk_management.md:922–927: theta per hefboom noemen en de reden
  herschrijven (verbetering 1).
- lectures/04_22_risk_management.md:79–80: "spreiding" wordt "volatiliteit"
  (verbetering 3).
- lectures/04_22_risk_management.md:82–85: Santa-Clara in een bijzin plaatsen (auteur
  van het leerboek dat dit college volgt) of het punt aan Artzner e.a. toeschrijven.

### 2. Opbouw en rode draad: 9,0

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in drie delen (geen staart, geen
  toetskracht, geen spiraal), en de drie delen dragen het hele college.
- Toy-getallen keren terug: 40 en 80 bp in de propositie, in de replicatie van de
  spreads en in oefening 1; toy (b) als tegenvoorbeeld; $\theta = 0{,}625$ in de spiraal.
- 5.717 woorden, routekaart en Samengevat op hun plaats; de replicatie verbindt de
  spreads van 1998 met de drempels uit het toy.

*Aanmerkingen.*
- Simulatie: "Daarmee klopt ook de derde verwachting, want dezelfde trade gaat bij een
  hogere hefboom vaker failliet". De voorspellingen worden met rangtelwoorden ingelost
  (H12, zie taal).
- Theorie, Samengevat: "Een backtest telt overschrijdingen, [](#eq-risk-management-kupiec),
  en wint kracht met de wortel van het aantal dagen $T$." De wortelregel staat niet in
  Theorie; de sectie noemt alleen de standaardfout van één jaar.

*Beter uitleggen.* De kalibratie van de fondssimulatie wijkt op $\kappa$ af van het toy
zonder dat de tekst het zegt; de lezer denkt dezelfde spiraal te zien.

### 3. Taal: 8,5

*Goed.*
- De redactie heeft staccato goed opgelost: de Intuïtie leest als een verhaal met
  "omdat", "want" en "zodat"; de lengte van de zinnen varieert.
- Motiefnamen blijven onder de grens (theorie of feit één keer, de standaardfout van 2%
  één keer, risico of vergissing als kop), geen motief als handelend onderwerp, geen
  "Wie …"-zinnen, "Waarom zou dit waar zijn?" twee keer.
- Geen vakterm van betekenis veranderd: coherent, subadditief, haircut, spread duration,
  margin call en Expected Shortfall worden overal in hun eigen betekenis gebruikt.

*Aanmerkingen.*
- Theorie, kernresultaat: "Dat bevestigt de tweede verwachting." Rangtelwoord als
  verwijzing, en "Dat" slaat op een bewijs in een dropdown (H8, H12).
- Theorie, arbitrageur: "Ze zegt dus niets over de kans om te overleven, en dat is de
  helft van de derde verwachting." Regeltaal.
- Simulatie, Een jaar backtest: "de toetsen laten de foute modellen na een jaar vaker
  passeren dan dat ze hen verwerpen." "Hen" voor modellen.
- Simulatie, Vier goede jaren: "De figuur toont dat als de afstand tussen de twee
  ruïnelijnen boven hefboom 20."
- Replicatie, figuurtekst: "en haast groen in de rustige jaren".
- Replicatie VaR: "Teken en rangorde kloppen met de verwachte afwijking." Het
  admonition-label als verwijzing (§11.12, randgeval).

*Beter uitleggen.* Niet van toepassing.

*Voor een 9.* De vier rangtelwoordverwijzingen (r. 408, 640, 818–819, 925) en de zinnen
op r. 758–759, 926–927 en 1088 herschrijven; "met de verwachte afwijking" op r. 1039
wordt "met wat we vooraf verwachtten".

### 4. Toy-voorbeeld: 8,5

*Goed.*
- Tabel met de opzet van de drie delen, daarna handstappen met tussenresultaten en een
  tabel hand/code die op de afronding na gelijk is (cel 2).
- De enige nog niet afgeleide formule (normale VaR) wordt vooraf genoemd.
- Slotzin zegt wat de getallen betekenen (VaR beloont spreiding alleen bij normale
  verliezen; de hefboom bepaalt de drempel).

*Aanmerkingen.*
- Toy-voorbeeld: "Drie kleine rekensommen laten de drie zwakke plekken zien." Drie
  mechanismen in plaats van één, en deel (c) heeft met drempels plus spiraal zelf twee.
- Toy-voorbeeld (c): "Daarna moet er nog 293 verkocht worden, wat 2,32 kost. Zo komt het
  proces uit op een verlies van 22,0". Van ronde 2 naar het totaal springt de tekst over
  de resterende rondes heen; na te rekenen in vijf minuten is dat niet.

*Beter uitleggen.* Bij de spiraal ontbreekt de zin dat de reeks convergeert omdat elke
ronde ongeveer 0,4 keer de vorige is (5,86 → 2,32), wat de lezer het totaal van 22
laat schatten zonder code.

*Voor een 9.* lectures/04_22_risk_management.md:199–202: de verhouding tussen de
rondes noemen, zodat 12,5 + 5,86 + 2,32 + ≈1,3 in de hand optelt; en in de Simulatie
(r. 912–915) zeggen hoe $\kappa$ zich verhoudt tot die van het toy.

### 5. Code en figuren: 9,0

*Goed.*
- Elke cel heeft een zin ervoor en erna; `run_fund` leest als het model (vermogen
  bijwerken, verkopen tot de eis geldt, maandelijks herbalanceren).
- De figuren krijgen een leeswijzer vooraf ("Wat in de figuur telt, is de hoogte van de
  lijnen bij de stippellijn van één jaar") en een onderschrift dat zegt wat te zien is.
- Presentatietabellen en figuurteksten zijn Nederlands.

*Aanmerkingen.*
- Toy-cel: `tail_mass = np.clip(cdf - np.maximum(cdf - p, alpha), 0.0, None)` is een
  compacte truc zonder commentaar.
- Figuur kracht, paneel (b): de Kupiec-statistiek wordt inline opnieuw geschreven in
  plaats van `kupiec_lr` aan te roepen.

*Beter uitleggen.* Een regel commentaar bij `tail_mass` ("kansmassa van elk verlies boven
het kwantiel") volstaat.

### 6. Replicatie en empirie: 9,0

*Goed.*
- Beide admonitions volgen Bron, Wat, Data, Verschil, Verwachte afwijking, binnen 250
  woorden.
- De VaR-tabel zet hier naast een juist model, met rode jaren en $\mathrm{LR}_{\mathrm{ind}}$
  tegen de kritieke waarde; het oordeel begint met "Geslaagd" en koppelt aan de
  verwachting.
- De verklaring van 2008 tegenover 2020 (geleidelijke opbouw tegen een sprong uit rust)
  is economisch en past bij de figuur.

*Aanmerkingen.*
- De spreads van 1998: "De Baa-spread verbreedde met 103, de Aaa-spread met 84 en de
  TED-spread met 87 basispunten, terwijl de tienjaarsrente daalde." Herhaalt de celtabel
  in lopende tekst.

*Beter uitleggen.* Bij de spreads is er geen origineel getal om naast het eigen getal te
zetten; één zin die dat zegt, maakt het ontbreken van de kolom "origineel" begrijpelijk.

### 7. Oefeningen: 9,0

*Goed.*
- Instap op het toy (hefboom 15 en 20) met de Aaa-beweging van 84 bp als brug naar de
  replicatie.
- Afleiding van de ES van een Student-$t$ met numerieke controle.
- Uitbreiding van de replicatie met GARCH-t en FHS; elke uitwerking eindigt met wat het
  getal leert.

*Aanmerkingen.*
- Oefening 3: "Toch wordt ook FHS in 2020 vaker overschreden dan bij een juist model
  hoort." Zie "Feitelijke fouten".

## Feitelijke fouten

Nagerekend: toy (a) tot en met (c), de Bazelse tabel (95,88%, 99,99%, 44% groen, 24%
kracht), de standaardfout 0,63 pp, de simulatie (8,8%, 46%, 15%, Sharpe 0,58, scheefheid
−21, 27%, 0,88, ruïne 0,2%/11,3%/23,6%), GARCH (0,092; 0,905), de backtesttabel, de
jaren 1998/2008/2020, de spreads (103, 84, 87; 6,6 en 2,9 SD's), oefening 1 (16,1) en 2
(1,066; 1,005; 2,65). Alles klopt met de celuitvoer. De hefboom "meer dan 25" is de
berekening van het PWG-rapport zelf (feiten #16) en is juist.

1. **r. 924–925, verkeerde reden.** "Bij hefboom 10 of minder is er geen verschil, omdat
   $\theta$ alleen groot is bij een fonds dat vaak tegen zijn limiet aan zit." Met
   $\theta = XD\kappa/h$ en $\kappa = 2$ bp is $\theta = 0{,}5$ bij hefboom 10 en 1,25 bij
   hefboom 25; theta hangt af van de positie, niet van de frequentie van de limiet. De
   juiste reden is tweeledig: bij hefboom 10 komt de limiet bijna nooit in beeld (margin
   call 0,9%, cel 8) en is $\theta$ klein, terwijl vanaf hefboom 20 $\theta \ge 1$ en de
   spiraal volgens de propositie divergeert.
2. **r. 1383–1384, overtrokken.** "Toch wordt ook FHS in 2020 vaker overschreden dan bij
   een juist model hoort." FHS heeft in 2020 4 overschrijdingen (cel 19) tegen 2,5
   verwacht; bij een juist model is $P(X \ge 4) \approx 0{,}24$ over 250 dagen, en 4 ligt in
   de groene zone. Voorstel: "Ook FHS wordt in 2020 iets vaker overschreden dan verwacht,
   maar blijft groen."

## Navertelling in vijf zinnen

VaR maakte van risico één getal per dag dat alleen de volatiliteit van morgen nodig
heeft, en werd daarom na 1996 de basis van het bankkapitaal. Het getal zegt niets over
verliezen voorbij de grens en kan bij een kleine kans op een groot verlies spreiding
bestraffen, terwijl Expected Shortfall dat niet doet en in 2016 VaR opvolgde. Een
backtest van één jaar heeft te weinig overschrijdingen om een fout model te vangen, en
op de Amerikaanse aandelenmarkt worden statische modellen ruim drie keer te vaak
overschreden en aanpassende modellen twee keer, vooral in 2020. Een gehefboomde
convergence trade met een goede Sharpe-ratio gaat failliet naarmate de hefboom stijgt,
en eigen gedwongen verkopen verdubbelen die kans bij hoge hefboom. Dat is wat LTCM in
1998 overkwam, toen de spreads waarop het wedde zes standaarddeviaties van 1997
bewogen. Dit strookt met het Overzicht.

## Taal na de redactie

De taalredactie heeft het college duidelijk natuurlijker gemaakt en geen vakterm van
betekenis veranderd (de dubbele betekenis van "spreiding" stond er al vóór de redactie).
Wat overblijft, is de sjabloonachtige inlossing van genummerde verwachtingen en een paar
zinnen die hardop haperen.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 758–759: "de toetsen laten de foute modellen na een jaar vaker passeren dan dat ze
   hen verwerpen." Herschrijving: "na een jaar laten beide toetsen elk fout model vaker
   door dan dat ze het verwerpen."
2. r. 926–927: "De figuur toont dat als de afstand tussen de twee ruïnelijnen boven
   hefboom 20." Herschrijving: "In de figuur is dat de afstand tussen de twee
   ruïnelijnen boven hefboom 20."
3. r. 639–641: "Ze zegt dus niets over de kans om te overleven, en dat is de helft van
   de derde verwachting. De andere helft is de eigen prijsdruk." Herschrijving: "Ze zegt
   dus niets over de kans om te overleven, zodat een hogere hefboom het fonds al
   kwetsbaarder maakt voordat zijn eigen verkopen meetellen."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Gecontroleerd: de volledige F6b-diff (kopie van vóór F6b tegen de huidige .md) en de
celuitvoer (`tools/nb_outputs.py`, cellen 2, 7 en 8) voor elk getal dat de schrijver heeft
toegevoegd of gewijzigd. Geen nieuw feitelijk punt, geen verslechtering.

**Feitelijke fouten**
1. Theta/fire sale (r. 934–941): opgelost. Nieuwe alinea geeft
   $\theta = XD\kappa/h \approx 0{,}05\,L$ ($\kappa$ = 2 bp, twee keer het toy), 0,5 bij
   hefboom 10 (margin call 0,9%, klopt met cel 7/8: P(margin call) bij $L=10$ = 0,009),
   precies 1 bij hefboom 20 en groter dan 1 bij 25; de oude foute reden is geschrapt.
2. FHS 2020 (r. 1400–1401): opgelost. "Ook FHS wordt in 2020 iets vaker overschreden dan
   verwacht, maar blijft daar groen"; 4 overschrijdingen tegen 2,5 verwacht (cel 19) blijft
   in de groene zone, zoals voorgesteld.

**Drie verbeteringen**
1. Theta zichtbaar maken: opgelost, zie Feitelijke fout 1.
2. Genummerde verwachtingen weg: opgelost. Alle vier rangtelwoordverwijzingen (bij de
   twee-obligaties-stelling, de Sharpe-ratio-alinea, de backtestkracht-alinea en de
   fire-sale-alinea) herschrijven naar wat er voorspeld werd; geen "eerste/tweede/derde
   verwachting" meer in de tekst.
3. Spreiding versus volatiliteit (r. 79–80): opgelost. "Volatiliteit van morgen" en "de
   goed meetbare volatiliteit"; "spreiding" betekent nu overal in het college
   diversificatie.

**Overige "Voor een 9"-punten**
- Santa-Clara (r. 82–86): opgelost, punt toegeschreven aan Artzner e.a. (1999), Santa-Clara
  als auteur van de gevolgde terugblik.
- Toy, rondes (r. 199–202): opgelost. "Omdat elke ronde minder dan de helft van de vorige
  kost, voegen de resterende rondes samen nog 1,3 toe"; 12,5 + 5,86 + 2,32 + 1,3 ≈ 22,0,
  klopt met cel 2, en 2,32/5,86 ≈ 0,40 < 0,5 klopt met "minder dan de helft".
- Simulatie-$\kappa$ vs. toy (in dezelfde fire-sale-alinea): opgelost.
- Hardop-zinnen (backtest-alinea en fire-sale-alinea) en "met wat we vooraf verwachtten"
  (replicatie-VaR): opgelost, vrijwel letterlijk de voorgestelde herschrijving.
- Figuurtekst bij de jaren-figuur ("... en in de rustige jaren meestal groen"): opgelost.

**Aanmerkingen zonder eigen "voor een 9" (meegenomen, geen verslechtering)**
- Notatie $\ell$/$m$ → $x$/$k$ in de VaR- en coherentie-definitie: opgelost.
- Wortelregel nu ook in Theorie zelf (bij Kupiec), niet alleen in Samengevat: opgelost.
- Code: commentaar bij `tail_mass` en bij de inline Kupiec-statistiek in paneel (b):
  opgelost.
- Spreads 1998: opsomming ingekort, zin toegevoegd over het ontbrekende originele getal:
  opgelost; de TED-spread (87 bp) staat niet meer in die zin maar blijft in de celtabel en
  in de SD-vergelijking verderop, dus geen feitelijke fout.
- Toy-intro, "drie mechanismen i.p.v. één": deels. Uitleg per deel (a/b/c) toegevoegd,
  niet herstructureerd tot één mechanisme; de schrijver noemt dat expliciet buiten
  F6b-scope.

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
| | **Eindcijfer** | | **9,0** |

Alle drie de verbeteringen, beide feitelijke fouten en alle "voor een 9"-punten van F6 zijn
opgelost; de plafondregel (§11.3) staat toe dat elk deelcijfer naar het in het vooruitzicht
gestelde cijfer stijgt. Eén Aanmerking (toy-intro, drie mechanismen) is deels opgelost maar
had geen eigen "voor een 9" en houdt het deelcijfer niet tegen. Eindcijfer 9,0, gelijk aan
"bij volledige oplossing van alle punten" in de F6-beoordeling.
