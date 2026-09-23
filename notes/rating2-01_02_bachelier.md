# Beoordeling: 01_02_bachelier (Regnault, Bachelier en de random walk)

Maatstaf: `plannen/rubriek-didactiek.md`. Gelezen als eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft. Kalibratie gelijk aan
`rating2-00_01_rendementen.md`: hetzelfde gebrek krijgt dezelfde aftrek.

## 1. Eindcijfer: 7,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 7 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 7 |
| | **gewogen** | | **7,40 → 7,4** |

Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

## 2. Per criterium

### 1. Helderheid van de uitleg (7)

**Goed**
- *Wat het voorspelt: de kans om een niveau te raken*: de stelling krijgt
  meteen een getal (verkooporder 10 euro boven 100, 31% tegen 62%) en wordt op
  de zestien toy-paden nageteld (0,375).
- *Wat het voorspelt: Bacheliers optieprijs*: $\sigma$ in euro per
  $\sqrt{\text{jaar}}$ wordt vertaald naar een aandeel van 100 (20 euro) en de
  formule levert 7,98 euro; de martingaalconditie krijgt een exemplaar (eerlijk
  kansspel).
- *Hoe het getoetst wordt*: bij elke toets een orde van grootte (SE 0,029 bij
  een eeuw maanddata; 12 900 runs met SE 80; $VR(4) = 1{,}15$ bij $\rho_1 = 0{,}1$;
  SE's 0,029 tot 0,126 bij 1216 weken).

**Aanmerkingen**
- *Opzet en aannames*: "Het symbool $\sigma$ is steeds een standaarddeviatie per
  tijdseenheid, maar van drie verschillende grootheden." De lecture zegt het
  eerlijk, maar laat de lezer drie betekenissen bijhouden. Hetzelfde geldt voor
  $S$ (positie in het toy, prijsniveau bij Bachelier), $T$ (steekproefomvang en
  vervaldag), $p$ (log-prijs en dichtheid: "in deze note is $p$ een dichtheid,
  geen log-prijs") en $R$ (aantal runs, elders bruto rendement).
- *Overzicht*: "dat de spreiding van de koers recht evenredig is met de wortel
  van de verstreken tijd", terwijl *Toy-voorbeeld* stap 3 vastlegt: "Regnault
  sprak niet over de standaarddeviatie maar over de *écart* ... en 'spreiding' is
  de standaarddeviatie." Regnaults wet wordt dus eerst met het verkeerde woord
  ingevoerd.
- *Waar we zijn in het verhaal*: "de regel werd in 1863 gemeten, veertig jaar
  voordat een theorie hem verklaarde." Bachelier is 1900: 37 jaar. De lecture
  zelf zegt elders "vijf jaar vóór Einstein" en L1 "37 jaar vóór Bachelier".
- *Replicatie* (Kendall), codecommentaar: "Kendall (1953) had 22 reeksen: 19
  Britse industrie-indices (...), tarwe in Chicago en katoen in New York." Dat
  zijn er 21.
- *Wat er brak*: "Volgens de simulatie worden zulke afwijkingen pas na dertig
  jaar weekdata zichtbaar". De gemeten $VR(2)$ van het kleinste kwintiel (1,205)
  hoort bij $\rho \approx 0{,}2$, en de eigen tabel zegt dat die na 1,8 jaar
  zichtbaar is. De conclusie volgt niet uit de getallen van de lecture.
- *Runs*: "Op dagdata oordeelt de runs-test veel scherper dan de eerste
  autocorrelatie." De dagelijkse $\rho_1$ en haar $z$-waarde worden in de tekst
  niet genoemd; de lezer moet zelf in de Kendall-tabel zoeken.

**Beter uitleggen**
- Donsker: waarom "in verdeling convergeren van het hele pad" meer is dan de
  centrale limietstelling per tijdstip. Eén exemplaar (het maximum van het pad,
  dat het reflectieprincipe nodig heeft) zou laten zien waarom het ertoe doet.
- Runs-test: waarom "te weinig runs" positieve autocorrelatie betekent, met een
  mini-voorbeeld van acht tekens.

### 2. Opbouw en rode draad (8)

**Goed**
- *Intuïtie*: drie voorspellingen, alle drie zichtbaar ingelost ("Zoals de
  intuïtie voorspelde, groeit de spreiding", optie "zoals de intuïtie voorspelde:
  wie de looptijd verviervoudigt, betaalt het dubbele", autocorrelaties "houdt dus
  bijna stand").
- Het toy komt terug in de theorie: $\sqrt{8/\pi} \approx 1{,}60$ tegen 1,50, en
  het reflectieprincipe op dezelfde zestien paden. De simulatie gebruikt de 1216
  weken van Lo en MacKinlay, die de replicatie weer oppakt.
- Theoriesubsecties openen met hun conclusie ("De kans dat de koers vóór een
  bepaalde datum ooit een niveau $a$ raakt, is ongeveer twee keer ...").

**Aanmerkingen**
- *Theorie*: het blok "Samengevat" staat aan het eind van de theorie; na twee
  replicaties en *Wat er brak* volgt geen samenvatting van de hele lecture.
- *Theorie*: "Simulatie en replicatie toetsen daarna alleen de kern: zijn
  koersveranderingen ongecorreleerd, en groeit de spreiding met de wortel van de
  tijd?" De optieprijs, een van de drie voorspellingen, wordt niet getoetst ("Toetsen
  kunnen we de optieformule hier niet"); de rode draad valt daar even weg.
- Lengte: vier ingeklapte notes, twee replicatieblokken en drie toetsen. De kern
  (random walk → $\sqrt{t}$ → variance ratio) raakt op plaatsen ondergesneeuwd,
  vooral in de tweede replicatie (Kendall, runs, drie steekproeven, kwintielen).

**Beter uitleggen**
- Waarom de optieprijs in een lecture over de random walk als toets staat: één
  zin in het Overzicht dat de optieformule het gevolg is en de autocorrelatie de
  toets.

### 3. Taal (7)

**Goed**
- *Intuïtie*: korte zinnen, de muntwerper als beeld, Regnaults Franse citaat met
  inleiding en parafrase.
- *Hoe het getoetst wordt*: "Iedereen kan de slotkoers van morgen met een kleine
  fout voorspellen ... Wie het niveau toetst, toetst dus niets." Helder en
  idiomatisch.
- Franse blokcitaten van Bachelier staan met inleiding, zoals de rubriek vraagt.

**Aanmerkingen**
- *Hoe het getoetst wordt*: "Dat is de standaardfout van 2% uit
  [](#00-01-rendementen), van de andere kant bekeken". Zelfde projectjargon als in
  L1 (bedoeld: twee procentpunt).
- Uitwerking ex-bachelier-1: "een ander zaad geeft andere getallen". Letterlijk
  vertaald *seed*.
- *Replicatie*: "Op de veertig jaar ná hun publicatie is $VR(2) = 0{,}950$".
  Calque van *on the forty years*; Nederlands is "in de veertig jaar".
- *Osborne*-note: "Arithmetische Brownse beweging", tegen "*aritmetische Brownse
  beweging*" in *Opzet en aannames*. Twee spellingen van één term.
- Wisselende namen: spreiding / afwijking / écart / gemiddelde absolute
  afwijking, terwijl stap 3 één naamgeving vastlegt (zie criterium 1).

**Beter uitleggen**
- Geen; de taal hindert het begrip nergens ernstig.

### 4. Toy-voorbeeld (8)

**Goed**
- *Toy-voorbeeld*: zestien paden, een verdelingstabel, en elke stap in minder dan
  vijf minuten na te rekenen.
- Eén niet-afgeleide formule, expliciet als "Het recept" aangekondigd
  ($\sqrt{2/\pi}$), en de theorie lost haar in.
- Tabel hand/code en een slotzin "De lezer weet nu ...".

**Aanmerkingen**
- *Toy-voorbeeld*, stap 3 en 4: "$\E|S_n|/\sqrt{n}$ loopt van $1{,}000$ via
  $0{,}707$ en $0{,}866$ naar $0{,}750$. Ze schommelt". Een tweede grootheid die
  zich anders gedraagt dan de eerste; de lezer krijgt naast het mechanisme
  (variantie lineair) ook een afwijking te verwerken.
- "Het recept" eindigt met een zin over de replicatie ("Daarom schatten we in de
  replicatie één helling over vier horizonnen"), die in het toy nog niet te
  plaatsen is.

**Beter uitleggen**
- Waarom $\E|S_2| = \E|S_1| = 1$: de lezer schrikt dat twee stappen niet meer
  afwijking geven dan één; één zin (de helft van de paden keert terug naar nul)
  zou dat wegnemen.

### 5. Code en figuren (7)

**Goed**
- Toy-cel: `positions`, `final`, `var_by_code` volgen de handstappen; commentaar
  "kolom n-1 bevat S_n" voorkomt een indexfout bij de lezer.
- `ar1_paths`: de AR(1)-recursie staat als zichtbare lus, zoals de rubriek vraagt
  waar het proces ertoe doet.
- Elke figuur heeft een leeswijzer vooraf ("Let op de bundel, niet op één pad";
  "Let op waar de lijnen de verticale lijn van Lo en MacKinlay kruisen") en een
  bijschrift achteraf.

**Aanmerkingen**
- *Replicatie*: `def runs_test(r):  # TODO: naar hap.stats`. Een TODO in een
  gepubliceerde lecture.
- *Replicatie*: de tabel "| 3, 12, 60 | 0,54 |" en "| 12, 60 | 0,475 |" staat in
  markdown en wordt door geen cel berekend. De lezer kan haar niet nagaan.
- Engelse docstrings: `"""Bachelier (1900) call price under arithmetic Brownian
  motion, zero rate."""`, `"""Wald-Wolfowitz runs test on the signs of a return
  series."""` enz. Zelfde aftrek als in L1.
- *Replicatie*, Regnault-cel: het commentaar "écart 2,73 frank per maand na
  correctie voor coupon en report" bevat broninformatie die in de tekst hoort.
- *Simulatie*: `ax.text(24.5, 0.05, "Lo-MacKinlay (23 jaar)", fontsize=9)`.
  Hard-gecodeerde positie naast een berekende lijn.
- Uitwerking ex-bachelier-1: `print(f"limiet (1+rho)/(1-rho) = ...")` is een
  aparte cel voor één getal dat de tekst erna toch noemt.

**Beter uitleggen**
- `hap.variance_ratio` levert `vr`, `z2` en meer; vóór het eerste gebruik
  (simulatie) zou één zin moeten zeggen wat de functie teruggeeft. Dat staat nu
  pas in *Hoe het getoetst wordt*, zonder de sleutelnamen.

### 6. Replicatie en empirie (8)

**Goed**
- Twee volledige replicatieblokken met bron, wat, data, verschil en verwachte
  afwijking, en een falsifieerbare eis (factor twee tegen factor acht; rangorde
  over kwintielen).
- Tabellen origineel/hier voor beide, en oordelen die met **Geslaagd** beginnen
  en naar de verwachting verwijzen ("zoals het replicatieblok voorspelde").
- Het resultaat na 1985 ($VR(2) = 0{,}950$) en de kwintielrangorde voegen iets toe
  aan het origineel.

**Aanmerkingen**
- *Replicatie* (Lo-MacKinlay): "**Geslaagd op de puntschattingen en de rangorde**".
  Voor de kwintielen liggen de niveaus 0,2 lager (1,205 tegen 1,42); het
  replicatieblok verwachtte "kleiner" zonder grootte. Het oordeel is voor de
  kwintielen royaal.
- *Replicatieblok* Regnault: "voor Shiller hoger door de maandmiddeling". Geen
  grootte, dus niet toetsbaar; 0,577 kan elke uitkomst boven 0,55 goedpraten.
- Getallen in lopende tekst: "Bij $q = 4$ en $q = 8$ klopt dat (2,0 en 1,8), bij
  $q = 2$ en $q = 16$ liggen ze lager (1,6 en 1,2)", "0,030 tegen 0,13", "van
  1,205 bij het kleinste kwintiel naar 1,016". Die staan deels al in de tabel.
- De hellingtabel voor Shiller (zie criterium 5) is niet gereproduceerd.

**Beter uitleggen**
- Waarom maandelijkse waardegewogen kwintielen de afwijking "kleiner maken": één
  getal (bijvoorbeeld wat een weekautocorrelatie van 0,3 op maandbasis nog
  oplevert) zou de verwachte afwijking toetsbaar maken.

### 7. Oefeningen (7)

**Goed**
- Instap is een directe variatie op het toy (scheve munt) en verbindt het met de
  keuze in de replicatie om te demeanen.
- Ex-bachelier-1 is een echte afleiding (gesloten $VR(q)$ voor een AR(1)) en
  ex-bachelier-3 een uitbreiding van de replicatie.
- Elke uitwerking eindigt met "Wat dit leert".

**Aanmerkingen**
- Uitwerking ex-bachelier-1: "De tabel toont één gesimuleerd pad; een ander zaad
  geeft andere getallen." Daarna volgen toch precieze getallen (4,51; 3,29; 1,42)
  en de les "wie afhankelijkheid zoekt, kiest de horizon waarop het signaal
  groeit, niet die waarop de statistiek het grootst oogt". De uitkomst was dat
  $q = 2$ de grootste $z$ geeft; de les lijkt het omgekeerde te zeggen en rust op
  één ruizig pad.
- Uitwerking ex-bachelier-3: "de verschuiving die we zien is 0,06 tot 0,10".
  Voor het grootste kwintiel is de verschuiving vrijwel nul (1,016 naar 1,017).
- Uitwerking ex-bachelier-2 (1): "Voor $K < S_t$ is $-d < 0$ en domineert de
  tweede term, zodat $P_t > 0$ blijft." Geen bewijs; $P_t = \E[(K - S_T)^+] \ge 0$
  zou in één regel volstaan.

**Beter uitleggen**
- Vraag 3 van ex-bachelier-1: de verwachte $z$ als functie van $q$ analytisch
  (via de SE-formule van Lo en MacKinlay) in plaats van uit één pad.

## 3. De drie verbeteringen met het meeste effect

1. **Helderheid (7 → 8):** symbolen ontdubbelen ($S$, $T$, $p$, $R$, en de drie
   $\sigma$'s met een index), "spreiding" consequent als standaarddeviatie, en de
   feitelijke tegenstrijdigheden rechtzetten: "veertig jaar", 22 tegen 21 reeksen,
   en de conclusie "pas na dertig jaar zichtbaar" tegenover het kwintiel met
   $\rho \approx 0{,}2$. Eindcijfer +0,3.
2. **Opbouw (8 → 9):** een Samengevat aan het eind van de lecture, en de tweede
   replicatie inkorten tot wat de kern draagt (markt-VR, kwintielrangorde, na
   1985). Eindcijfer +0,2.
3. **Taal (7 → 8):** "standaardfout van 2%" → twee procentpunt, "zaad" → seed of
   startwaarde, "Op de veertig jaar" → "In de veertig jaar", één spelling van
   aritmetisch, één naam voor $\E|\cdot|$. Eindcijfer +0,15.

## 4. Navertelling in vijf zinnen

Regnault mat in 1863 dat de gemiddelde koersafwijking met de wortel van de tijd
groeit, en Bachelier leidde dat in 1900 af uit een random walk die in de limiet
een Brownse beweging wordt. Uit hetzelfde model volgen het reflectieprincipe
(een niveau raken is twee keer zo waarschijnlijk als erboven eindigen) en een
optieprijs van ongeveer $0{,}4\,\sigma\sqrt{\tau}$ zonder risicoaversie of
verwacht rendement. De random walk toets je op veranderingen, niet op niveaus,
en de variance ratio is daarvoor de hoofdtoets; kleine autocorrelaties vragen
wel tientallen tot honderden jaren data. Op Amerikaanse data klopt de
$\sqrt{t}$-wet (helling 0,51), en de afwijkingen die Lo en MacKinlay vonden
repliceren, zijn groter bij kleine aandelen en na 1985 van teken gewisseld. Het
model is een theorie van de ruis en niet van de waarde; of de afwijkingen risico
of vergissing zijn, kunnen de gratis data niet beslissen.

Dit komt overeen met het Overzicht.
