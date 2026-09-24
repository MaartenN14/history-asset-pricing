STATUS 00_01_rendementen F5c words=4967 prose=PASS open=0 cijfer=9,0 min=9

# Beoordeling: 00_01_rendementen (F5a)

Gelezen als eerstejaars PhD-student die 00_00_setup heeft gelezen. Ter controle van de
aansluiting: "Waar we zijn" van 00_00_setup (geen "Wat er brak") en "Waar we zijn" en
"Wat er brak" van 01_02_bachelier. De aansluiting klopt: setup stelt de vraag "Wat is een
rendement, en hoe goed kunnen we het meten?", deze lecture sluit af met Regnault en de
wortel-$t$-regel, en Bachelier opent met "[](#00-01-rendementen) leidde de
$\sqrt{t}$-regel af ... het gemiddelde rendement slecht meetbaar ... de variantie goed".

`prose_stats`: 4.979 woorden (onder 5.500), gemiddelde zinslengte 14,4, één zin boven 40
woorden, 6 puntkomma's, één stopwoord, PASS.

## Eindcijfer: 8,4

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8 + 0,2·9 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,35, afgerond 8,4.

## 1. Helderheid van de uitleg: 8

*Goed*
- **Intuïtie**: de windmeter maakt het verschil tussen "totaal" en "schommeling" concreet
  voordat er een formule staat; −20% en +25% geven meteen een getal (+2,5% gemiddeld,
  vermogen gelijk).
- **Het kernresultaat**: $20/\sqrt{100} = 2$ procentpunt en het 95%-interval van 2% tot
  10% ("van een markt die risico nauwelijks beloont tot een die dat royaal doet") geven de
  formule een betekenis. [](#eq-rendementen-jaren) wordt met 44 en 400 jaar uitgerekend.
- **Merton**: Brownse beweging, drift en maximum-likelihood krijgen elk een zin uitleg
  vóór de stelling; "evenveel informatie als twee koersen: de eerste en de laatste".

*Aanmerkingen*
- **Meetkundig, rekenkundig en de variance drag, slotalinea**: "dat is de grootheid in elke
  waarderingsvergelijking van deze reeks: $P_t = \E_t[m_{t+1}x_{t+1}]$ (elders in de reeks
  $p_t$), de prijs als verwachte payoff $x$ (koers plus dividend volgend jaar), gewogen met
  een discontofactor $m$ die hoog is in slechte tijden." Twee nieuwe symbolen en een nieuw
  begrip (discontofactor die hoog is in slechte tijden) in een bijzin, nergens meer
  gebruikt. De lezer blijft achter met een vraag die de lecture niet beantwoordt.
- **Wanneer de aannames niet gelden, dikke staarten**: "$\Var(\bar\ell) =
  \sigma_\ell^{2}/T$, ... $\Var(\hat\sigma_\ell^{2}) = \sigma_\ell^{4}(\kappa-1)/N$."
  Links jaren, rechts waarnemingen, en niet gezegd of $\bar\ell$ en $\hat\sigma_\ell^2$
  per periode of per jaar zijn. De lezer moet zelf reconstrueren dat de eerste formule
  over het geannualiseerde gemiddelde gaat.
- **Opzet / Merton**: $\sigma$ wisselt van betekenis: eerst die van het simpele rendement,
  "in de benaderingen hieronder wisselen we ze uit", en in Merton "De $\sigma$ is hier de
  volatiliteit van het logrendement". Het wordt gemeld, maar de lezer moet per sectie
  bijhouden welke $\sigma$ bedoeld is.

*Beter uitleggen*
- De rol van het rekenkundig gemiddelde in waardering: één zin zonder nieuwe symbolen
  (een prijs is een verwachte uitkering, en verwachtingen zijn rekenkundige gemiddelden)
  draagt dezelfde boodschap.
- Bij de kurtosisformules: één zin met de eenheden (geannualiseerd gemiddelde over $T$
  jaar; variantie per waarneming over $N$ waarnemingen).

*Voor een 9*
- Variance drag, slotalinea: $m$, $x$ en "(elders in de reeks $p_t$)" weghalen of in één
  zin uitleggen.
- Dikke staarten: de eenheden van $\bar\ell$ en $\hat\sigma_\ell^2$ benoemen.
- Opzet: één vaste afspraak voor $\sigma$ (bijvoorbeeld altijd $\sigma$ voor het
  logrendement na de Opzet), zodat de twee "we laten de index weg"-zinnen vervallen.

## 2. Opbouw en rode draad: 9

*Goed*
- **Overzicht**: vraag en antwoord in de eerste twee zinnen ("na een eeuw data nog een
  standaardfout van twee procentpunt, terwijl de volatiliteit dan al bijna exact
  vastligt").
- **Intuïtie → Theorie**: de intuïtie doet drie voorspellingen en de theorie lost ze
  zichtbaar in ("Zo lost de theorie de derde voorspelling uit de intuïtie in", "Zo lost de
  stelling de eerste voorspelling uit de intuïtie in").
- **Dezelfde getallen**: $\sigma = 20\%$ en $T = 100$ lopen van intuïtie tot simulatie;
  de 22,9% van het toy keert terug als volatiliteit van de value-weighted markt; de
  replicatie eindigt bij de 1,83 als "gemeten tegenhanger van de standaardfout van 2%".

*Aanmerkingen*
- **Annualisatie en de wortel-$t$-regel**: de alinea over de verhouding
  signaal/ruis (dagtabel, 263 handelsdagen, 0,04 en 0,65) haalt getallen uit de replicatie
  naar voren en introduceert de Sharpe-ratio terloops. Het is een zijstap voordat de kern
  komt.
- **Wat wél in de data zit: clustering van volatiliteit**: een tweede uitbreiding na de
  replicatie; de conclusie ("de grootheid die we goed kunnen meten, is ook voorspelbaar")
  hangt goed aan de rode draad, maar maakt het slot van de empirie langer.

*Beter uitleggen*
- Niets wezenlijks; de lezer kan de kern na het Overzicht benoemen.

## 3. Taal: 8

*Goed*
- Korte zinnen (gemiddeld 14,4 woorden), geen u/je, geen calques.
- Engelse vaktermen krijgen bij de eerste keer een Nederlandse uitleg: *variance drag*
  ("de rem die schommelingen op de groei van een vermogen zetten"), *equity premium*
  ("hierna de premie"), *bid-ask bounce*.
- **Het kernresultaat**: "van een markt die risico nauwelijks beloont tot een die dat
  royaal doet" is helder, natuurlijk Nederlands.

*Aanmerkingen*
- **Variance drag, slotalinea**: de zin met $P_t = \E_t[m_{t+1}x_{t+1}]$ is met twee
  tussenvoegingen en een dubbele punt de langste en zwaarste zin van de lecture.
- **Annualisatie**: "Op het excess rendement heet die verhouding de *Sharpe-ratio*" —
  "excess rendement" is half vertaald; elders heet het "premie" of "extra rendement".
- **Het kernresultaat**: "Stap 4 deelde door drie, omdat de drag over deze drie jaren zelf
  gaat, en gaf 18,7%." Drie gedachten in één zin, met "de drag" als verkorting.

*Voor een 9*
- Variance drag: de lange zin splitsen of schrappen (zie criterium 1).
- Annualisatie: "excess rendement" vervangen door de al ingevoerde naam ("premie").
- Het kernresultaat: de zin over Stap 4 in twee zinnen.

## 4. Toy-voorbeeld: 9

*Goed*
- Met de hand na te rekenen in vijf minuten; +25% en −20% maken de logs exact
  tegengesteld, wat Stap 3 een tweede les geeft zonder extra mechanisme.
- Eén nog niet afgeleide formule (het recept), als zodanig aangekondigd.
- Tabel hand/code en één zin wat de lezer nu weet.

*Aanmerkingen*
- Stap 4 rekent met de variantie gedeeld door drie; het kernresultaat moet later uitleggen
  waarom de standaardfout met $T-1$ werkt. Kleine wrijving, geen fout.

## 5. Code en figuren: 8

*Goed*
- Elke cel heeft een zin ervoor en erna; `annual_summary` heeft benoemde tussenresultaten
  en wordt voor maand- en dagdata hergebruikt.
- **Simulatie**: vóór de figuur staat waarop te letten ("links is maar één histogram
  zichtbaar, omdat de twee exact samenvallen"), het bijschrift zegt wat te zien is.
- De simulatielus maakt het proces zichtbaar (pad bouwen, op $k$ momenten aflezen,
  verschillen nemen).

*Aanmerkingen*
- **Simulatie, tabel**: kolomnamen `"theorie: sigma/sqrt(T), pp"`,
  `"SD(variantie)/variantie"`, `"theorie: sqrt(2/N)"` zijn code-notatie in een
  presentatietabel.
- **Simulatie, eerste cel**: `log_price[:, :: per_year // k]` is een compacte
  slice-truc; het commentaar "k koersen per jaar" helpt, maar de lezer moet de stapgrootte
  zelf afleiden.
- **Dezelfde eeuw, cel**: de kurtosiskolom wordt na de `DataFrame` nog aangeplakt;
  "excess kurtosis (log)" is een Engelse kolomnaam in een presentatietabel.

*Beter uitleggen*
- Bij de slice: één zin dat elke $252/k$-ste dagkoers wordt genomen.

*Voor een 9*
- Simulatietabel en vergelijkingstabel: kolomnamen in woorden ("standaardfout gemiddelde
  (pp)", "theorie", "relatieve fout variantie", "extra kurtosis").
- Simulatie, eerste cel: de stapgrootte als benoemde variabele (`step = per_year // k`).

## 6. Replicatie en empirie: 8

*Goed*
- Admonition compleet en kort; de keuze value-weighted als replicatie en equal-weighted
  als controle wordt beargumenteerd en de verwachte richting ("Komt hij lager uit, dan zit
  er een fout in de code") is toetsbaar.
- Tabel origineel/hier/verschil; oordeel begint met "**Geslaagd.**" en verwijst naar het
  ene procentpunt uit het replicatieblok.
- De standaardfout die in 1964 ontbrak, wordt erbij gezet: "Het beroemde 9,0% zei dus
  weinig meer dan dat het rendement positief was."

*Aanmerkingen*
- **Dezelfde eeuw, maand- en dagdata**: "de standaardfout van het gemiddelde daalt alleen
  van 1,83 naar 1,75 procentpunt ... 17,5% tegen 18,3% ... 0,047 bij lag 1 ...
  $(18{,}34/17{,}46)^2 \approx 1{,}10$ ... springt van 6,5 naar 17,0." Zeven getallen in
  één alinea, alle al in de tabel erboven.
- **Na het oordeel**: "De standaardfout van 3,9 procentpunt hoort bij het rekenkundig
  gemiddelde van de value-weighted markt, 11,7%, en het 95%-interval loopt van ongeveer 4%
  tot 19%." Het interval staat alleen in proza, niet in een tabel.

*Beter uitleggen*
- Niets inhoudelijks.

*Voor een 9*
- Dezelfde eeuw: naar de tabel verwijzen en hoogstens de twee standaardfouten noemen.
- Fisher-Lorie: het 95%-interval als kolom in de tabel origineel/hier.

## 7. Oefeningen: 9

*Goed*
- Instap varieert het toy (volgorde; −30% in plaats van −20%) met hand- en codecontrole.
- Oefening 1 is een afleiding (Merton zonder continue tijd) plus simulatie; oefening 2
  breidt de replicatie uit naar drie perioden.
- Elke uitwerking eindigt met "Wat dit leert"; oefening 2 koppelt de stijging van het
  meetkundig gemiddelde (1,46 procentpunt) netjes aan de gedaalde halve variantie.

*Aanmerkingen*
- Geen die het cijfer drukken.

## De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9)**: de zin met $P_t = \E_t[m_{t+1}x_{t+1}]$ aan het eind van de
   variance-drag-subsectie vervangen door een zin zonder nieuwe symbolen, de eenheden bij
   de kurtosisformules noemen, en één vaste afspraak voor $\sigma$. Eindcijfer +0,3.
2. **Taal (8 → 9)**: dezelfde lange zin weg, "excess rendement" → "premie", de zin over
   Stap 4 in het kernresultaat splitsen. Eindcijfer +0,15.
3. **Replicatie (8 → 9)**: de getallen in "Dezelfde eeuw, maand- en dagdata" en het
   95%-interval naar tabellen. Eindcijfer +0,1.

## Navertelling in vijf zinnen

Simpele rendementen tellen op over aandelen, logrendementen over de tijd, en het
meetkundig gemiddelde ligt ongeveer een halve variantie onder het rekenkundige. De
standaardfout van een gemiddeld rendement is $\sigma/\sqrt{T}$, dus bij 20% volatiliteit
is een eeuw data op twee procentpunt nauwkeurig. Volgens Merton hangt die precisie alleen
af van de kalenderlengte, terwijl de variantie scherper wordt bij vaker meten; de
simulatie en de dagdata bevestigen dat. Fisher en Lorie vonden in 1964 9,0% per jaar, wat
we binnen een half procentpunt repliceren, maar met een standaardfout van bijna vier
procentpunt. Of er een premie is, is dus te meten; hoe groot hij is, of wat hem
veroorzaakt, niet.

Dit komt overeen met het Overzicht.

## Feitelijke fouten

Nagerekend met `uv run python` op `hap.data` en de formules uit de tekst. Kloppen: toy
(1,032280; 0,031770; 0,035; 0,0325; 1,05³⁰ = 4,32 en 1,03228³⁰ = 2,59), warning
($e^{0{,}0047 \cdot 1200} \approx 280$), $1{,}02^{100} = 7{,}2$, signaal/ruis (0,043;
1,08; 0,04; 0,65), toy-standaardfout (22,9%; 18,7%; 13,2), $T^*$ (44; 400; 1600),
$\sqrt{2/100}$ en $\sqrt{2/25\,200}$, $VR \approx 1{,}17$ en $\sqrt{1{,}17} = 1{,}08$,
$\sqrt{19/2} \approx 3$, simulatie (1,99 pp bij alle frequenties; 13,7% → 0,9%),
Fisher-Lorie (VW meetkundig 9,46%, rekenkundig 11,67%, vol 22,9%, SE 3,9; EW 12,9%;
interval 4–19%; daling 1929–1932 van 84%), maand/dag (1201 en 26 296 waarnemingen, factor
21,9; 262,7 dagen per jaar; 11,57% en 11,30%; vol 18,34% en 17,46%; SE 1,83 en 1,75;
kurtosis 6,5 en 17,0), autocorrelaties (maand lag 1 0,085, dag lag 1 0,047, absoluut
0,30–0,33), oefening 1 (0,16%; 84%; 400 en 225 jaar), oefening 2 (rekenkundig 11,67 /
11,43 / 11,61; $t$ = 0,01; meetkundig 9,46 → 10,92; vol 22,9 → 15,4; 764 jaar), instap
(0,016667; −0,012660; 0,026944; 2,93).

Geen feitelijke fouten gevonden. Niet nagegaan: het getal 6,9% zonder herbelegging uit
Fisher en Lorie (de lecture repliceert het niet).

## Controle 1

Alleen de eigen punten nagekeken, op de huidige `lectures/00_01_rendementen.md`.
`prose_stats`: 4.967 woorden, geen zin boven 40 woorden, PASS.

| crit. | punt | status | vindplaats nu |
|---|---|---|---|
| 1/3 | zin met $P_t = \E_t[m_{t+1}x_{t+1}]$ en "(elders in de reeks $p_t$)" | opgelost | Variance drag, slot: "Een prijs is een verwachte uitkering, dus elke waarderingsformule in deze reeks gebruikt het rekenkundige." Geen nieuwe symbolen meer. |
| 1 | eenheden bij de kurtosisformules | opgelost | "Links staat het gemiddelde logrendement per jaar over $T$ jaar ... Rechts staat de variantie per waarneming" |
| 1 | $\sigma$ wisselt van betekenis | opgelost | Opzet: "vanaf hier is $\sigma$ de volatiliteit van het logrendement"; $\sigma_\ell$ en "we laten de index weg" zijn verdwenen, ook in Merton en de drag-stelling |
| 2 | signaal/ruis-alinea haalt replicatiegetallen naar voren | opgelost | Annualisatie: nog twee ronde getallen (0,04 en 0,65), de rest staat in de dagtabel |
| 3 | "excess rendement" | opgelost | "Voor de premie heet deze verhouding de *Sharpe-ratio*." |
| 3 | zin over Stap 4 met drie gedachten | opgelost | in drie zinnen gesplitst ("Daar ging het om de drie jaren zelf, hier om het proces waaruit ze komen.") |
| 5 | code-notatie in de simulatietabel | opgelost | "standaardfout gemiddelde (pp)", "theorie gemiddelde (pp)", "relatieve fout variantie", "theorie variantie" |
| 5 | slice-truc `:: per_year // k` | opgelost | `step = per_year // k  # dagen tussen twee waarnemingen` |
| 5 | kurtosiskolom achteraf aangeplakt, Engelse naam | deels | aanplakken opgelost (`describe_frequency`); de kolom heet nog "excess kurtosis (log)", wel de term die de theorie invoert |
| 6 | zeven getallen in "Dezelfde eeuw" | opgelost | alleen de twee standaardfouten (1,83 en 1,75) staan nog in de tekst |
| 6 | 95%-interval alleen in proza | opgelost | kolommen "95%-interval, onder/boven" in de tabel origineel/hier |

Nagerekend, omdat het getal nieuw is: het interval ligt nu rond het meetkundig
gemiddelde, $9{,}46\% \pm 1{,}96 \times 3{,}9 = 1{,}8\%$ tot $17{,}1\%$, dus "ongeveer 2% tot
17%" klopt. Signaal/ruis: per dag $0{,}043/1{,}08 = 0{,}04$, per jaar $11{,}30/17{,}46 =
0{,}65$, klopt. Geen verslechteringen en geen nieuwe feitelijke fouten.

### Deelcijfers na controle 1

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 | 9 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 8 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |

**Eindcijfer: 9,0** (was 8,4). Laagste deelcijfer 9. Open feitelijke fouten: 0.
