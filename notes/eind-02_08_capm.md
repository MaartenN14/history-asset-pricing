STATUS 02_08_capm F6 words=5495 prose=PASS open=1 cijfer=8,3 min=8

# Eindbeoordeling (F6): Het CAPM

## Eindcijfer: 8,3

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,60 + 1,275 + 0,90 + 0,85 + 0,80 + 0,45 = 8,28, dus 8,3.
Lengte: 5.495 woorden, vijf onder de 5.500.

## Feitelijke fouten

Nagerekend met `uv run python -c ...` en tegen de celuitvoer: het toy
($\boldsymbol{\Sigma}\mathbf{w}_m = (4; 6; 1)/225$; premies 8%, 12%, 2%, gelijk aan
10%, 14%, 4% min de 2% van [](#01-04-markowitz); $x = (1{,}5; 1; 2)$; posities
$(112{,}5; 75; 150)$ en $(187{,}5; 125; 250)$; lenen 187,5; $\sigma_m^2 = 28/2025$;
6,22%; bèta's $9/7$, $27/14$, $9/28$; 86% eigen risico; Sharpe 0,20 en 0,40),
$\theta_m \approx 0{,}06/0{,}04 = 1{,}5$, $0{,}045/\sqrt{480} = 0{,}21\%$ per maand
en 2,5% per jaar, Shanken $1{,}018$, $\sigma_u^2 = 0{,}082$, $\kappa = 0{,}52$,
0,29% en 3,4% per jaar, $\kappa = 0{,}98$ bij $n = 50$, GRS 4,20 tegen 1,52, de
simulatie (0,316 tegen 0,318; 0,298 tegen 0,287; 0,594 en 0,015; 2,465 = 2,465;
18%; 95,7%; 0,22 tegen 0,30), de replicatie (bèta 1,69 tot 0,91, SE 0,29 tot
0,58, alle alfa's $|t| < 1{,}4$; alle bullets van het oordeel; GRS in alle drie
late steekproeven boven de grens; $R^2$ 0,81 tot 0,93), de oefeningen ($\theta_m =
4$; 5,53%; 7,11%, 10,67%, 1,78%; 150 en 150; minimale $n$ 18 en 33; 0,74; 0,80;
$t = 1{,}05$). Eén bewering klopt niet.

1. **Theorie, "Opzet en aannames".** "Er zijn $N$ risicovolle activa met netto
   rendementen $\mathbf{R}$ ... Zoals in [](#01-04-markowitz) zijn rendementen
   netto, anders dan de bruto conventie van [](#00-01-rendementen)." Beide lectures
   volgen de setup: $r$ is netto, $R = 1 + r$ bruto ([](#01-04-markowitz), Opzet:
   "$r$ is netto (10% is 0,10), $R = 1 + r$ bruto"; [](#00-01-rendementen), Opzet:
   "Zoals in [](#00-00-setup) is $r$ het netto simpele rendement"). Er is geen
   "bruto conventie" in L1 die hier wordt verlaten; deze lecture wijkt zelf af door
   $R$ netto te schrijven, en de gegeven reden is onjuist.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- Toy-voorbeeld: marktclearing in vijf handstappen, met de premies die precies de
  gegeven rendementen van [](#01-04-markowitz) terugleveren. Het "omdraaien" van
  Markowitz is daardoor zichtbaar.
- "Geschatte bèta's": $\kappa$ krijgt een getal (0,52), de helling halveert, het
  intercept staat 3,4% per jaar te hoog; bij $n = 50$ is $\kappa = 0{,}98$.
- Fama-MacBeth: waarom de standaardfout klopt (een portefeuille met bèta één en
  kosten nul), met het getal 2,5% per jaar en de Shanken-correctie 1,02.

*Aanmerkingen*
- Opzet: "Zoals in [](#01-04-markowitz) zijn rendementen netto, anders dan de bruto
  conventie van [](#00-01-rendementen)" (zie feitelijke fouten). Een lezer die L4
  openslaat, vindt daar $R$ bruto.
- Het symbool $m$ staat hier voor de markt ($\beta_{i,m}$, $R_m$), terwijl de setup
  en [](#02-06-efficiente-markten) $m$ voor de SDF gebruiken; niet genoemd.
- Zero-beta, bewijs stap 2: "$\lambda_m$ en $\delta_m$ de schaduwprijzen". L4 zei
  erbij dat deze $\lambda$ niet de prijs van risico $\lambda_f$ is; hier ontbreekt
  die zin.
- Premie en standaardfout: "met een marktvolatiliteit van ongeveer 20%" (voor
  $\theta_m$) en "Met een marktvolatiliteit van 4,5% per maand" (voor de
  standaardfout, 15,6% per jaar) zijn twee waarden voor dezelfde grootheid zonder
  toelichting.
- "Jensens alfa" wordt als nieuw begrip ingevoerd, terwijl
  [](#02-06-efficiente-markten) dezelfde regressie al als replicatie draaide.

*Beter uitleggen*
- Eén zin dat hier $R$ netto is en $m$ de markt, als bewuste afwijking van de
  setup, of de setup-letters gebruiken.
- De GRS-verdeling: één zin waarom de $F$-verdeling pas exact is bij normale
  residuen, met het gevolg voor de 1,52.

### 2. Opbouw en rode draad (8)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord (bèta maal de marktpremie).
- De drie verwachtingen uit de intuïtie (rechte lijn, eigen risico onbeloond, één
  prijs) worden na de stelling met naam ingelost.
- Toy-getallen lopen door ($\theta_m = 4{,}5$, 6,22%, schaal 1/2 en 1/6), en de
  simulatie kalibreert erop ("iets boven de 6,22% van het toy-voorbeeld").

*Aanmerkingen*
- De theorie draagt acht resultaten (vraag, CAPM, premie, efficiëntie,
  zero-beta, GRS, Fama-MacBeth, attenuatie) in 5.495 woorden, op de grens van de
  lengte. GRS en de Shanken-correctie komen buiten het jaartal 1961–1973 zonder dat
  het kader een uitloop noemt.
- De replicatie gebruikt drie verzamelingen testactiva en negen steekproeven; de
  kern (BJS 1931–1965) slaagt niet, en het oordeel steunt op de periode erna.

*Beter uitleggen*
- Eén zin aan het begin van de replicatie die zegt welke steekproef de
  hoofdtoets is en welke illustratie.

### 3. Taal (8,5)

*Goed*
- Korte zinnen (gemiddeld 14,4 woorden); het mandje in de intuïtie is gewone taal
  voor de tangentportefeuille.
- De motieven worden ter plekke uitgelegd ("Hier betekent de vraag: is de vlakke
  lijn een correcte evenwichtsprijs, of een prijs die ernaast zit?").

*Aanmerkingen*
- Kernresultaat: "Het restant staat tegen $R^{f}$ (aanname 3)." Vertaald
  Engels ("at the risk-free rate") en onduidelijk.
- "alfa" hier, "alpha" in [](#02-06-efficiente-markten): twee spellingen voor
  hetzelfde begrip in opeenvolgende lectures.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Twee beleggers, drie activa, vijf handstappen, één mechanisme (marktclearing),
  één nog niet afgeleid recept vooraf aangekondigd, tabel hand/code, en de zin
  "Beide beleggers houden dus de markt en verschillen alleen in hoeveel".

*Aanmerkingen*
- Stap 3 (het stelsel $\boldsymbol{\Sigma}\mathbf{x} = \boldsymbol{\mu}^e$ oplossen)
  kost de lezer net meer dan vijf minuten.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `fama_macbeth_gammas` toont de lus over de maanden en noemt de gewichten achter
  $\gamma_j$, zoals de tekst ze uitlegt.
- Beide figuren hebben vooraf "Let ... op" en een bijschrift dat zegt wat te zien is.

*Aanmerkingen*
- `@dataclass class CapmWorld` voor één set parameters: een klasse waar een dict of
  losse constanten volstaan.
- `sml_test` geeft veertien grootheden terug en roept
  `hap.stats.fama_macbeth(excess, {"beta": betas.to_frame().T}, lags=0)` aan met een
  interface die de tekst niet uitlegt.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8)

*Goed*
- Blok volledig, met een verwachte afwijking die per periode is te toetsen; tabel
  origineel/hier voor BJS en Fama-MacBeth.
- Oordeel "Gedeeltelijk geslaagd" per periode, eerlijk ook waar het niet lukt, met
  een verklaring (grootte en bèta vallen samen) die oefening 3 toetst.

*Aanmerkingen*
- Het oordeel staat in vijf bullets vol getallen die ook in de tabellen staan
  (0,28 tegen 0,60; 0,21 en 2,53; 4,20 en 1,52; −0,12 en −0,76; −0,39 en 0,44;
  1,06 en 0,93; 0,78 en 0,96; 0,48 en 2,55; 0,27).
- Drie subperiodes hebben geen originele premie (`np.nan`), zonder uitleg.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy ($\theta_2 = 5$), afleiding van de attenuatie met minimale
  portefeuillegrootte, uitbreiding van de replicatie met andere basisactiva; elke
  uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De notatiezin corrigeren: $R$ netto en $m$ als markt als bewuste afwijking van
   de setup noemen, of $r$ en een andere letter voor de markt gebruiken; de
   volatiliteit van 20% en 4,5% per maand verzoenen (helderheid 8 → 8,5).
2. Het oordeel in een tabel verwacht/hier per periode zetten in plaats van vijf
   getallenbullets (replicatie 8 → 8,5).
3. Eén theoriedeel inkorten (de Shanken-alinea of het bewijs van GRS naar een
   dropdown) en de hoofdsteekproef van de replicatie aanwijzen (opbouw 8 → 8,5).

## Navertelling in vijf zinnen

Als alle beleggers mean-variance optimaliseren met dezelfde verwachtingen en vrij
kunnen lenen, houdt iedereen de tangentportefeuille, en marktclearing maakt die
gelijk aan de markt. Dan is het verwachte excess rendement van elk activum zijn
bèta maal de marktpremie, en die premie is de geaggregeerde risicoaversie maal de
marktvariantie. Zonder vrij lenen blijft de lijn recht, maar met een hoger
intercept en een kleinere helling (Black). Geschatte bèta's maken de lijn op
aandelen vlakker, maar op bèta-portefeuilles niet, en de premie blijft ook dan maar
op ongeveer 2,5 procentpunt per jaar nauwkeurig. Op echte data is de lijn na 1965
vlakker dan het CAPM voorspelt en verwerpt GRS het model; over 1931–1965 is het
beeld gemengd.

Dit komt overeen met het Overzicht, dat de vlakke lijn het centrale feit van het
tijdvak noemt; de eigen replicatie vindt dat feit pas na 1965.

## Controle

Gecontroleerd tegen `notes/rapport-02_08_capm.md` §F6-1 en de lecture.

STATUS 02_08_capm F6c words=5367 prose=PASS open=1 cijfer=8,6 min=8,5

| punt | status | vindplaats |
|---|---|---|
| Fout 1: netto/bruto-bewering over L4 en L1 | opgelost | Opzet: "netto rendementen $\mathbf{r}$ en een risicovrije rente $R^{f}$ (2% is 0,02), zoals in [](#00-00-setup)"; alle ruwe rendementen zijn nu $r$ |
| Verbetering 1: notatie, $m$, volatiliteit | opgelost | "Het subscript $m$ staat hier voor de marktportefeuille, niet voor de SDF"; $\theta_m = 0{,}006/0{,}002025 \approx 3{,}0$ met 4,5% per maand (nagerekend: 2,96); schaduwprijzen "niet de prijs van risico" |
| Verbetering 2: oordeel in een tabel | opgelost | tabel periode/verwacht/hier/oordeel; getallen gelijk aan de celuitvoer |
| Verbetering 3: inkorten, hoofdsteekproef | opgelost | Shanken in één zin ($(0{,}6/4{,}5)^2 = 1{,}8\% \approx 2\%$); "De hoofdsteekproef is die na BJS" |
| Naadpunt 3 ($R$ netto) | opgelost | zie fout 1 |
| Naadpunt 4 ($m$ als markt) | opgelost | zie verbetering 1 |
| Naadpunt 5 (alfa) | opgelost | overal "alpha", ook in de celuitvoer |
| Naadpunt 6 (Jensen dubbel) | deels | terugverwijzing toegevoegd, maar met een onjuiste bewering (nieuwe fout 2) |
| Naadpunt 9 ($\lambda_m$) | opgelost | zie verbetering 1 |
| Naadpunt 10 (20% tegen 4,5%) | opgelost | één kalibratie; de 20% staat alleen nog in de lezing van het motief uit L1 |

**Nieuwe feitelijke fout.**

2. **Theorie, "Hoe het getoetst wordt: de tijdreeks en GRS".** "Jensen, wiens
   fondsen [](#02-06-efficiente-markten) al gebruikte, paste de toets toe op 115
   beleggingsfondsen". L6 gebruikte niet Jensens fondsen maar zijn regressie, op
   zeven hedendaagse fondsen en VFINX (1982–2026). Juist is: "wiens toets
   [](#02-06-efficiente-markten) al op zeven hedendaagse fondsen herhaalde".

Blijft staan, klein: "Het restant staat tegen $R^{f}$" (taal); `CapmWorld` en de
interface van `sml_test` (code).

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 8,5 | 8,5 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 8,5 |
| 6 | Replicatie | 8 | 8,5 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,70 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,575. **Eindcijfer 8,6,
laagste deelcijfer 8,5.** Helderheid blijft 8,5 en niet hoger door de nieuwe fout
in de Jensen-zin.
