# Beoordeling: 00_01_rendementen (Rendementen en hun statistiek)

Maatstaf: `plannen/rubriek-didactiek.md`. Gelezen als eerstejaars PhD-student die
[](#00-00-setup) heeft gelezen maar niet paraat heeft.

## 1. Eindcijfer: 7,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 7 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 7 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 8 |
| | **gewogen** | | **7,35 → 7,4** |

Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

## 2. Per criterium

### 1. Helderheid van de uitleg (7)

**Goed**
- *Het kernresultaat: de standaardfout van 2%*: formule, dan direct het getal
  ($20/\sqrt{100} = 2$), het 95%-interval (2% tot 10%) en met
  `eq-rendementen-jaren` de 44 tegen 400 jaar. Elke formule waarvan de grootte
  ertoe doet, krijgt hier een uitgerekend getal.
- *Meetkundig, rekenkundig en de variance drag*: de waarderingsvergelijking
  $p_t = \E_t[m_{t+1}x_{t+1}]$ wordt in één zin herhaald, met $x$ en $m$ benoemd.
  Dat is precies hoe een geleend resultaat moet terugkomen.
- *Merton (1980)*: vóór de stelling worden $W_t$, $\nu$ en de dubbele betekenis
  van $\sigma$ expliciet benoemd; na de stelling staat het getal (14% tegen 0,9%).

**Aanmerkingen**
- *Dezelfde eeuw, maand- en dagdata*: "Die valt op dagbasis lager uit, 17,1% tegen
  18,3%, omdat de maandreeks positieve autocorrelatie bevat." Dit is inhoudelijk
  verkeerd toegeschreven. De standaarddeviatie van maandrendementen hangt niet af
  van de autocorrelatie *tussen* maanden, maar van de autocorrelatie van de
  dagrendementen *binnen* een maand. De lezer leert hier een verkeerd mechanisme.
- *Merton (1980)*: "Een dataset van 26 296 dagrendementen bevat daarover evenveel
  informatie als twee koersen" en vier zinnen later "bij 25 200 dagwaarnemingen
  0,9%." Twee aantallen dagwaarnemingen zonder uitleg dat de eerste de echte
  reeks is en de tweede $100 \times 252$.
- *Wanneer de aannames niet gelden*: "is in onze data ruim negentien. De *excess
  kurtosis* is de kurtosis min drie: nul onder normaliteit en ruim zestien", terwijl
  *Dezelfde eeuw* "De excess kurtosis springt intussen van 7,4 naar 16,1" meldt en
  de uitwerking van oefening 3 "De excess kurtosis daalt van 17,0 op dagbasis".
  Drie getallen voor dezelfde grootheid; dat het verschil van simpele
  versus logrendementen komt, staat nergens.
- *Wanneer de aannames niet gelden*: "bij Amerikaanse aandelen is de
  autocorrelatie van maandrendementen bij lag 1 ongeveer $0{,}09$", tegen *Wat er
  wél in de data zit*: "De autocorrelatie van het rendement is bij elke lag kleiner
  dan 0,09". De lezer weet niet of 0,09 een bovengrens of een schatting is.
- *Annualisatie en de wortel-$t$-regel*: "een Sharpe-ratio van ongeveer 0,04 ...
  Over een dag is het signaal dus een dertigste van de ruis". 0,04 is een
  vijfentwintigste; de twee getallen passen niet op elkaar.
- *Het kernresultaat*: "Stel die gelijk aan $t$ en los op naar $T$." Het symbool
  $t$ is in dezelfde lecture ook de tijdindex ($P_t$, $\ell_{t+1}$); hier is het
  een $t$-waarde, zonder dat dat gezegd wordt.
- *Wat er brak, en wat daarna kwam*: "In 1863 publiceerde een Parijse
  beursemployé de observatie dat de koersuitslag met de wortel van de tijd
  groeit". De naam ontbreekt.
- *Overzicht*: "Deze lecture is daarop een uitzondering." Onduidelijk waarop
  "daarop" slaat: op de vraag "theorie of feit" of op de controverses.

**Beter uitleggen**
- Het verschil tussen maand- en dagvolatiliteit: één zin dat het om
  autocorrelatie van dagrendementen binnen de maand gaat, met de variance ratio
  $(18{,}3/17{,}1)^2 \approx 1{,}15$ als getal.
- Kurtosis: één zin welke reeks (simpel of log, welke periode) welk getal geeft,
  zodat 16, 16,1 en 17,0 niet als tegenspraak lezen.
- "Stabiele Paretiaanse verdeling" (warning over Mandelbrot): "stabiel" krijgt
  geen betekenis; één bijzin (som van zulke variabelen heeft weer dezelfde
  verdeling) volstaat.

### 2. Opbouw en rode draad (8)

**Goed**
- *Overzicht*: stelt de vraag en geeft meteen het antwoord (twee procentpunt,
  interval van ongeveer vier procentpunt naar weerszijden), gevolgd door een
  routekaart die de secties volgt.
- *Intuïtie*: eindigt met drie expliciete voorspellingen; de theorie lost ze
  zichtbaar in ("Zo lost de stelling de eerste voorspelling uit de intuïtie in",
  "Zoals de intuïtie voorspelde").
- De 20%-volatiliteit en de 2 procentpunt lopen van intuïtie via theorie en
  simulatie naar replicatie en *Wat er brak*; de toy-volatiliteit (23%) wordt in
  de simulatie en de replicatie (22,9%) teruggehaald.

**Aanmerkingen**
- *Theorie*: het blok "Samengevat" staat aan het eind van de theorie, niet aan
  het eind van de lecture. Na de replicatie en *Wat er brak* volgt geen
  samenvatting van wat de lezer nu weet.
- *Replicatie op echte data*: "Welke reeks is de tegenhanger van de 9,0%?" De
  rechtvaardiging dat de value-weighted reeks de replicatie is, komt pas ná de
  resultaattabel; in het replicatieblok staat alleen "dezelfde beurs, dezelfde
  periode, dezelfde CRSP-bron".
- *Toy-voorbeeld*: "Stap 5 is een voorproef op de tweede vraag van de lecture".
  Het toy draagt daarmee twee mechanismen (drag en standaardfout), terwijl het
  zelf aankondigt dat het er één heeft.
- Theoriesubsecties beginnen met een vraag en een intuïtie, niet met hun
  conclusie (bijv. *Merton (1980)*: "Helpt het om vaker te kijken?"). Alleen
  *Wanneer de aannames niet gelden* geeft "Het antwoord vooraf".

**Beter uitleggen**
- De premie (6%) in intuïtie en theorie en de drift (8%) in de simulatie zijn
  verschillende grootheden; de simulatie zegt het ("De drift is een
  totaalrendement, geen premie"), maar niet waarom niet gewoon 6% is gekozen.

### 3. Taal (7)

**Goed**
- *Intuïtie*: korte zinnen, één gedachte per zin, de windmeter als beeld
  consequent volgehouden.
- Engelse vaktermen krijgen bij de eerste keer een Nederlandse omschrijving
  (*variance drag*, *equity premium*, bid-ask bounce, delistings).
- Geen u/je in de hele lecture.

**Aanmerkingen**
- *Het kernresultaat*: "De naam zegt 2%; bedoeld is een standaardfout van twee
  procentpunt op een gemiddeld rendement." De lecture erkent zelf dat haar
  eigen label ("de standaardfout van 2%") onjuist is en gebruikt het toch negen
  keer. Dat is projectjargon.
- *Opzet: twee soorten rendement* (warning): "bijna een halve procentpunt in één
  maand" en *Replicatie*: "het is een halve procentpunt". Procentpunt is een
  het-woord: "een half procentpunt".
- *Merton (1980)*, bewijs: "De increments $\ell_i = \dots$ zijn onafhankelijk" en
  "want de increments telescoperen". Onvertaald Engels (aanwassen, stappen).
- *Waar we zijn in het verhaal*: "Dit is geen tijdvak maar een meetlat, waarmee we
  de rest van de reeks wegen." Gemengde metafoor: met een meetlat meet je, je
  weegt niet.
- Wisselende namen voor hetzelfde begrip: meetkundig gemiddelde, samengesteld
  rendement, groeitempo, "samengesteld (meetk.)" (tabelkolom). De lecture
  benoemt de synoniemen in *Meetkundig, rekenkundig*, maar gebruikt ze daarna
  toch door elkaar.

**Beter uitleggen**
- Geen; de taal hindert het begrip nergens ernstig.

### 4. Toy-voorbeeld (7)

**Goed**
- *Toy-voorbeeld*: drie getallen, elke stap met de hand in minder dan vijf
  minuten na te rekenen, met zes decimalen zodat de lezer kan controleren.
- De tabel "met de hand / code" staat er, en de slotzin zegt wat de lezer nu weet.
- Stap 3 verbindt logrendementen met de vuistregel "20% verlies vraagt 25% winst".

**Aanmerkingen**
- *Toy-voorbeeld*: "Eén formule leiden we pas in de theorie af". Er zijn er twee:
  ook stap 5 gebruikt "$s/\sqrt{T}$ ... de theorie bewijst hem hieronder".
- Stap 4 deelt door $T$, stap 5 door $T-1$: "In stap 4 deelden we door $T = 3$,
  omdat de drag over deze drie jaren zelf gaat." Het onderscheid is correct, maar
  legt in een toy van één mechanisme een tweede subtiliteit neer.
- Slotzin: "weet nu dat het meetkundig gemiddelde een halve variantie onder het
  rekenkundige ligt, dat logrendementen optellen, en dat drie jaar niets zegt over
  het gemiddelde." Drie lessen, geen één.

**Beter uitleggen**
- Waarom de benadering hier zo goed klopt (0,022 procentpunt) bij $\sigma$ van
  23%: de lezer verwacht bij zulke grote uitslagen een slechtere benadering; één
  zin met de derde-ordeterm zou dat oplossen.

### 5. Code en figuren (7)

**Goed**
- Toy-cel: benoemde tussenresultaten (`arith`, `geom`, `geom_via_log`,
  `drag_approx`) die één op één de handstappen volgen.
- *Simulatie*: tabel zet simulatie en theorie in aangrenzende kolommen; figuur
  heeft een leeswijzer vooraf ("Let op de breedte van de histogrammen") en een
  bijschrift dat zegt wat te zien is.
- *Dezelfde eeuw*: na de tabel worden alle kolomnamen (`nobs`, `mean_ann`, ...)
  uitgelegd.

**Aanmerkingen**
- *Simulatie*: `agg = steps.reshape(len(block), n_years * k, per_year // k).sum(axis=2)`
  plus het opknippen in acht blokken "om geheugen te sparen". Een reshape-truc die
  de aggregatie verbergt; het proces (dagen optellen tot een periode) is niet als
  lus zichtbaar.
- *Replicatie*, laadcel: "Maandelijks herbalanceren van kleine aandelen verhoogt
  het gemeten rendement (bid-ask bounce, rebalanceringspremie)." Inhoudelijke
  argumentatie in een codecommentaar in plaats van in de tekst; ook "414 in plaats
  van 420 maanden" staat alleen in het commentaar.
- *Replicatie*: `"""Compounded and arithmetic annual return with the standard error."""`
  Engelse docstring in een Nederlandse lecture.
- *Replicatie*, figuur: `ax.axhline(1.09 ** (len(value_weighted) / 12), ...)`. De
  "stippellijn" is een horizontale lijn op het eindvermogen over de hele periode.
  Een groeipad van 9% per jaar zou het vergelijkt met de reeksen laten zien; nu
  is de lijn alleen aan de rechterrand betekenisvol.
- *Toy-voorbeeld*: de eerste cel (imports) heeft geen zin erna.
- Bijschrift simulatiefiguur: "de twee histogrammen liggen exact over elkaar". De
  lezer ziet één kleur en kan denken dat een reeks ontbreekt; de leeswijzer
  waarschuwt daar niet voor.

**Beter uitleggen**
- Waarom `agg.mean(axis=1) * k` voor elke $k$ exact hetzelfde getal geeft: één
  zin vóór de cel dat het gemiddelde van de geaggregeerde stappen altijd
  (eindpunt − beginpunt)/100 is.

### 6. Replicatie en empirie (8)

**Goed**
- *Replicatie*-blok: bron, wat, data, verschil en verwachte afwijking, elk
  benoemd, ruim binnen 250 woorden, met een tekenvoorspelling ("Komt hij lager
  uit, dan zit er een fout in de code").
- Tabel origineel/hier/verschil, en een oordeel dat begint met **Geslaagd.** en
  expliciet naar de verwachte afwijking verwijst.
- De standaardfout die in 1964 ontbrak, wordt toegevoegd en omgezet in een
  interval (4% tot 19%): de replicatie draagt de kernboodschap.

**Aanmerkingen**
- *Replicatie*-blok: "French begint zes maanden later en herbalanceert
  maandelijks". Geldt voor de equal-weighted decielen, niet voor de
  value-weighted markt, die juist de replicatie is. De zin suggereert een
  verschil dat voor de hoofdreeks niet bestaat.
- *Replicatie*-blok: "De value-weighted markt moet binnen ongeveer één
  procentpunt van 9,0% uitkomen". De marge wordt niet onderbouwd (welke kant op,
  waarom één en niet twee), terwijl de weging principieel verschilt van
  Fisher-Lorie.
- *Replicatie*: "De standaardfout van het gemiddelde is 3,9 procentpunt voor de
  value-weighted reeks en 5,5 voor de equal-weighted reeks." en verder 22,9%,
  2,6, 9,46%, 12,9%, 11,7%, 4% tot 19%: veel getallen in lopende tekst die al
  in de tabel staan.
- *Dezelfde eeuw*: "de standaardfout van het gemiddelde daalt alleen van 1,83 naar
  1,67 procentpunt" wordt verklaard met de verkeerde autocorrelatie (zie
  criterium 1).

**Beter uitleggen**
- Waarom een koop-en-houd-portefeuille met gelijke bedragen op de value-weighted
  markt lijkt: dat argument hoort in het replicatieblok onder "Verschil", niet
  ná de tabel.

### 7. Oefeningen (8)

**Goed**
- Drie typen aanwezig: instap als variatie op het toy (volgorde omkeren, −30%),
  afleiding van Merton in discrete tijd (ex-rendementen-1, deel 1), uitbreiding van
  de replicatie op drie perioden (ex-rendementen-2).
- Elke uitwerking eindigt met "Wat dit leert".
- Ex-rendementen-2 levert een echte vondst op (rekenkundig gelijk, meetkundig
  stijgend door dalende volatiliteit) die de drag uit de theorie hergebruikt.

**Aanmerkingen**
- Uitwerking ex-rendementen-1: "In ongeveer 0,2% van de eeuwen concludeert een
  onderzoeker ... dat aandelen minder opbrengen dan niets." Analytisch is dat
  $\Phi(-3) \approx 0{,}13\%$; "ongeveer 0,2%" is de simulatieruis, niet de
  waarde. Narekenen en de analytische waarde erbij zetten.
- Uitwerking ex-rendementen-2: "zou elke periode driehonderdduizend jaar moeten
  duren". Getal alleen in proza, en het is een artefact van een verschil van
  bijna nul; de vraag (3) ("Wat zou er waargenomen moeten worden") wordt zo
  eigenlijk niet beantwoord.
- Uitwerking ex-rendementen-3: "De excess kurtosis daalt van 17,0 op dagbasis",
  tegen 16,1 in de lecture (zie criterium 1).

**Beter uitleggen**
- Vraag 3 van ex-rendementen-2: welk *verschil* realistisch te detecteren is
  (bijv. 2 procentpunt ≈ enkele honderden jaren) als hoofdantwoord, niet als
  bijzin.

## 3. De drie verbeteringen met het meeste effect

1. **Helderheid (7 → 8):** de autocorrelatieverklaring in *Dezelfde eeuw*
   corrigeren (dagrendementen binnen de maand, met $VR \approx 1{,}15$) en de
   getallen gelijktrekken: 26 296 tegen 25 200 waarnemingen, kurtosis 16/16,1/17,0,
   lag-1 "ongeveer 0,09" tegen "kleiner dan 0,09", Sharpe 0,04 tegen "een
   dertigste". Plus de naam van de beursemployé uit 1863. Eindcijfer +0,3.
2. **Opbouw (8 → 9):** een Samengevat aan het eind van de lecture, de
   VW-rechtvaardiging vóór de replicatietabel, en stap 5 uit het toy halen (of
   expliciet als los blok na het toy). Dit verhoogt ook Toy naar 8. Eindcijfer
   +0,3.
3. **Taal (7 → 8):** het label "standaardfout van 2%" vervangen door "de
   standaardfout van twee procentpunt", "een half procentpunt", "increments"
   vertalen, en per begrip één naam kiezen (meetkundig gemiddelde). Eindcijfer
   +0,15.

## 4. Navertelling in vijf zinnen

Een gemiddeld rendement kan rekenkundig of meetkundig zijn; het meetkundige ligt
ongeveer een halve variantie lager, en alleen het rekenkundige schat de
verwachting die in waarderingsformules staat. De standaardfout van een gemiddeld
rendement is $\sigma/\sqrt{T}$, dus bij 20% volatiliteit en een eeuw data twee
procentpunt, wat een 95%-interval van ongeveer 2% tot 10% rond een premie van 6%
geeft. Volgens Merton (1980) helpt vaker waarnemen niet, omdat de geschatte drift
alleen van begin- en eindkoers afhangt, terwijl de variantie met de frequentie
steeds scherper wordt; simulatie en dag- versus maanddata bevestigen dat.
Autocorrelatie en dikke staarten veranderen daar weinig aan. De replicatie van
Fisher en Lorie (1964) slaagt (9,46% tegen 9,0%), maar met een standaardfout van
3,9 procentpunt zei dat beroemde getal weinig meer dan dat het positief was.

Dit komt overeen met het Overzicht.
