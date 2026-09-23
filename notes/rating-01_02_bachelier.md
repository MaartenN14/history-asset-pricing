# Beoordeling: 01_02_bachelier — Regnault, Bachelier en de random walk

Maatstaf: `plannen/rubriek-didactiek.md`. Lezer: eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft.

## Eindcijfer: 7,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 7 |
| 2 | Opbouw en rode draad | 20% | 7 |
| 3 | Taal | 15% | 6 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 7 |
| 7 | Oefeningen | 5% | 8 |

Gewogen: 0,3·7 + 0,2·7 + 0,15·6 + 0,1·8 + 0,1·7 + 0,1·7 + 0,05·8 = 7,00 → 7,0.
Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

---

## 1. Helderheid van de uitleg — 7

**Goed**
- *Wat het voorspelt: de kans om een niveau te raken*: de stelling krijgt een
  economisch exemplaar (verkooporder 10 euro boven 100, 31% tegen 62%) én een
  telling op de zestien toy-paden.
- *Wat het voorspelt: Bacheliers optieprijs*: na de formule direct 7,98 euro, en
  een expliciete waarschuwing dat $\sigma$ hier een bedrag is ("Voor een aandeel
  van 100 met 20% volatiliteit per jaar is $\sigma \approx 20$ euro per
  $\sqrt{\text{jaar}}$").
- *Simulatie*: de vuistregel $T^* = (1{,}96/\rho)^2$ met een tabel van drie
  uitgerekende gevallen.

**Aanmerkingen**
- *Intuïtie*: "Bij de helft van de periode verhoudt de *écart* zich als 1 tot
  1,41; bij een derde als 1 tot 1,73; bij een kwart als 1 tot 2." Onduidelijk
  wat zich tot wat verhoudt; de lezer moet de richting raden.
- *Het kernresultaat*, en elders: $\sigma$ heeft drie betekenissen (5% per maand
  in de Opzet, de stap-SD in Donsker, euro's per $\sqrt{\text{jaar}}$ bij
  Bachelier). De waarschuwing staat er, maar pas halverwege de optiesectie.
- *Bacheliers optieprijs*: "de optie is na te maken met het aandeel en kas, en
  daarom mag men rekenen alsof de verwachte koerswinst nul is." De sprong van
  repliceerbaarheid naar verwachting nul krijgt de lezer niet mee.
- *Bacheliers eigen notatie*: "Daarmee voorspelde hij voor een maand een *écart
  probable* van $\pm 46$ centimes". Uit $k = 5$ per $\sqrt{\text{dag}}$ is 46
  niet na te rekenen zonder het aantal dagen en de factor 0,6745.
- *Hoe het getoetst wordt*: "Dat is de standaardfout van 2% uit
  [](#00-00-setup)" — dat resultaat werd afgeleid in [](#00-01-rendementen).
- *Simulatie*, warning: "is groot genoeg om ruis van 0,06 te produceren." Waar
  0,06 vandaan komt (twee keer $1/\sqrt{1216} \approx 0{,}029$) staat er niet.
- *Replicatie*, eerste blok: "2,73 frank per maand," gevolgd door een lege regel
  en dan "maal $\sqrt{3}$ en $\sqrt{12}$, gaf 4,73 en 9,45". De zin breekt in
  twee alinea's.
- *Replicatie Kendall*: de originele waarde "0.13" voor Kendalls gemiddelde
  $\rho_1$ staat alleen in de code; in de tekst staat nergens waarover gemiddeld
  is.
- *Replicatie Kendall*: "De runs-test kijkt alleen naar de tekens en is daardoor
  gevoelig voor positieve autocorrelatie die de dikke staarten verbergen." Het
  mechanisme (dikke staarten domineren de correlatiecoëfficiënt) blijft impliciet.

**Beter uitleggen**
- Regnaults verhoudingen: "de écart over de hele periode is 1,41 keer die over
  de helft".
- Martingaalconditie: één zin dat een optie die met aandeel en kas na te maken is
  dezelfde prijs moet hebben ongeacht de verwachte koerswinst, en dat men die
  daarom op nul mag zetten; of expliciet naar [](#02-09-black-scholes) verwijzen.
- *Écart probable*: $0{,}6745 \times 5 \times \sqrt{2\pi} \times \sqrt{30}
  \approx 46$ uitschrijven.
- De ruis van 0,06 herleiden tot $2/\sqrt{T}$.

## 2. Opbouw en rode draad — 7

**Goed**
- *Overzicht* stelt de vraag ("Hoe beweegt een koers als niemand de volgende
  stap kan voorspellen?") en geeft het antwoord in de volgende zin.
- *Intuïtie* doet drie voorspellingen, en de theorie lost elk ervan expliciet in
  ("Zoals de intuïtie voorspelde"; "De derde voorspelling uit de intuïtie").
- De toy van vier stappen komt terug in het reflectieprincipe en in de oefening
  met de scheve munt.

**Aanmerkingen**
- De theorie draagt vijf lijnen (Donsker, diffusievergelijking, reflectie,
  optieprijs met Black-Scholes-vergelijking, drie toetsen). Reflectie en
  optieprijs komen in simulatie en replicatie niet meer terug; de draad
  √t → toets wordt twee keer onderbroken.
- Het *Samengevat*-blok staat aan het eind van *Theorie*, niet aan het eind van
  de lecture.
- Theoriesecties openen met een vraag, niet met de conclusie: "Wat blijft er van
  de wandeling over als de stappen kleiner en talrijker worden?", "Hoe groot is
  de kans dat de koers vóór een bepaalde datum ooit een niveau $a$ raakt?".
- Twee replicaties (Regnault; Kendall plus Lo-MacKinlay) met elk eigen blok en
  oordeel; de lezer moet zelf de koppeling maken met de simulatievraag.
- *Wat er brak*: "Er is dus een theorie van de ruis en geen theorie van de
  waarde." De belangrijkste breuk wordt pas hier voor het eerst genoemd; de
  lecture heeft haar nergens voorbereid.

**Beter uitleggen**
- Eén zin aan het eind van de optiesectie die zegt waarom de lecture nu naar
  toetsen overstapt (de optieformule is niet toetsbaar zonder optieprijzen).
- Een *Samengevat* aan het eind met de replicatiegetallen (helling 0,51; VR(2)
  0,950 na 1985).

## 3. Taal — 6

**Goed**
- *Intuïtie*: korte, concrete zinnen met de muntworp.
- Franse citaten zijn vertaald of met inleiding als blokcitaat gezet.
- Vaktermen krijgen bij eerste gebruik uitleg (*barrièreopties*, *maximale
  drawdown*, *onderscheidend vermogen*).

**Aanmerkingen**
- Spelfout, meermaals: "*arithmetische Brownse beweging*" (Nederlands:
  aritmetische).
- Engels meervoud en wisselende namen: "horizons" (*Toy-voorbeeld*, *Replicatie*)
  naast "horizonnen" in de vorige lecture; "lags" ("over veel lags") naast
  "vertraging".
- *Overzicht*: "Bachelier definieert het tijdvak, omdat alleen hij een model
  leverde waaruit het feit volgt, en meteen ook optieprijzen." Het tweede deel
  hangt grammaticaal los.
- *Toy-voorbeeld*: "Eerst de imports-cel, de enige van de lecture." Zinsfragment
  en anglicisme.
- *Wat er brak*: "De tweede breuk is kleiner en empirisch, en zelf gemeten" en
  "Eerst het gat, niet de barst." Projectjargon (barst/gat) dat de lezer niet kan
  plaatsen.
- *Oefening 3, uitwerking*: "De afwijking is zichtbaar verdwenen, en tegelijk
  statistisch niet te onderscheiden van: er is niets veranderd." Kromme zin.
- *Risico of vergissing?*: "Later heet dit de *joint hypothesis*" — Engelse term
  zonder Nederlandse naam.
- Veel Franse termen zonder vaste Nederlandse naam naast elkaar (*écart*,
  *écart probable*, *options à prime*, *coefficient d'instabilité*, *employé*).

**Beter uitleggen**
- Eén Nederlandse naam kiezen voor *écart* na de eerste vermelding (de lecture
  doet dat half: "gemiddelde absolute afwijking") en die consequent gebruiken.

## 4. Toy-voorbeeld — 8

**Goed**
- Vier stappen, zestien paden, met de hand in vijf minuten te tellen; tabel van
  de verdeling.
- Eén mechanisme: variantie telt op, dus SD groeit met $\sqrt n$.
- Tabel hand/code en een slotzin ("De lezer weet nu dat ...").

**Aanmerkingen**
- "Op dezelfde manier is $\E|S_1| = 1$, $\E|S_2| = 1$ en $\E|S_3| = 1{,}50$."
  Drie van de vier waarden worden niet met de hand voorgedaan.
- "**Het recept.** Voor lange wandelingen nadert die verhouding
  $\sqrt{2/\pi} \approx 0{,}798$" staat ná de stappen in plaats van ervoor, en
  voegt een tweede grootheid (de écart) toe naast de variantie.

**Beter uitleggen**
- $\E|S_2| = (2 \cdot 1 + 0 \cdot 2 + 2 \cdot 1)/4 = 1$ in één regel voordoen.

## 5. Code en figuren — 7

**Goed**
- `ar1_paths` toont de AR(1)-recursie als zichtbare lus.
- De reflectie-cel telt letterlijk na wat de stelling zegt, met commentaar
  ("raakt het pad ooit +2?").
- Vóór de figuren staat een leeswijzer ("Let op de bundel, niet op één pad";
  "Let op waar de lijnen de verticale lijn van Lo en MacKinlay kruisen").

**Aanmerkingen**
- *Replicatie Kendall*: `def runs_test(r):  # TODO: naar hap.stats` —
  werkaantekening in lecturecode.
- *Simulatie*, figuurcel: `ax.axvline(23.4, ...)` — hardgecodeerd getal in plaats
  van `T_lm / 52`.
- *Replicatie*: de cel `comparison_lm` bouwt kolommen door lijsten aan elkaar te
  plakken (`[0.13] + [1.08, 1.16, 1.22, 1.22] + [1.42, 1.28, 1.14]`); welke waarde
  bij welke rij hoort, is moeilijk te zien.
- Kolomnamen in het Engels of als code (`E|dev|`, `SD(dev)`, `nobs`) zonder
  toelichting.

**Beter uitleggen**
- De originele waarden als woordenboek met rijnaam → waarde schrijven.

## 6. Replicatie en empirie — 7

**Goed**
- Twee volledige blokken met falsifieerbare eis ("binnen een factor twee,
  waar een lineaire wet een factor acht zou geven"; "VR(2) daalt van het kleinste
  naar het grootste kwintiel").
- Tabellen origineel/hier, voor Regnault en voor Lo-MacKinlay.
- Oordelen beginnen met **Geslaagd.** en verwijzen naar de verwachting.

**Aanmerkingen**
- *Replicatie Regnault*: "zijn overeenstemming van een half procent halen we
  niet. Voor French voorspelt de maandwaarde maal $\sqrt{12}$ een jaarwaarde die
  ruim tien procent te laag is." Op Regnaults eigen toets is de replicatie dus
  hooguit gedeeltelijk, terwijl het oordeel onvoorwaardelijk **Geslaagd** is.
- *Replicatie Regnault*: "Zonder $h = 1$ zakt de Shiller-helling naar ongeveer
  0,54" en "Tussen twaalf en zestig maanden is de Shiller-helling 0,475" — getallen
  die in geen tabel staan.
- *Replicatie Kendall/Lo-MacKinlay*: het blok verwacht "$z$-waarden rond de twee";
  de uitkomst is "tussen 1,2 en 2,0". Het oordeel noemt dat "iets onder de hunne"
  zonder het aan de verwachting te toetsen.
- Kendalls 0,13 tegen onze 0,030 is een factor vier verschil; het blok voorspelde
  over Kendall niets, en "Ook Kendalls orde van grootte houdt stand" is ruim.

**Beter uitleggen**
- In het Regnault-oordeel onderscheiden: helling geslaagd, eigen
  extrapolatietoets gedeeltelijk.
- De verwachte afwijking voor Kendall in het blok zetten (sectorindices, dun
  verhandeld → hoger).

## 7. Oefeningen — 8

**Goed**
- Instap is een variatie op de toy (scheve munt) met code die de zestien paden
  herweegt.
- Oefening 1 (VR van een AR(1)) en 2 (putprijs, impliciete Bachelier-volatiliteit)
  zijn echte afleidingen; oefening 3 breidt de replicatie uit na 1985.
- Elke uitwerking eindigt met "Wat dit leert".

**Aanmerkingen**
- *Oefening 1, uitwerking*: "De geschatte waarden liggen boven de theoretische,
  en de $z$-waarde daalt met $q$." De vaste tekst beschrijft één willekeurige
  trekking alsof het een regel is.
- *Oefening 3, uitwerking*: "hier loopt een vraag voor het eerst in deze reeks
  niet stuk op de data, maar op het ontbreken ervan" — de les gaat over de reeks,
  niet over de oefening.

**Beter uitleggen**
- In oefening 1 zeggen dat het om één pad gaat en dat een ander zaad andere
  getallen geeft.

---

## De drie verbeteringen met het meeste effect op het cijfer

1. **Helderheid (7 → 8):** de sprong repliceerbaarheid → verwachting nul in één
   zin, de écart-verhoudingen en de 46 centimes uitrekenen, de ruis van 0,06
   herleiden, de juiste verwijzing voor de standaardfout van 2%, en de gebroken
   zin in het replicatieblok herstellen. Effect op het eindcijfer ≈ +0,3.
2. **Taal (6 → 7):** "aritmetische", "horizonnen", "vertraging", projectjargon
   (barst/gat) eruit, en de krommen zinnen in *Overzicht* en oefening 3
   herschrijven. Effect ≈ +0,15.
3. **Opbouw (7 → 8):** reflectie en optieprijs expliciet als zijstap markeren of
   aan de toetsen koppelen, een *Samengevat* aan het eind, en de breuk
   "theorie van de ruis, geen theorie van de waarde" al in *Overzicht* of
   *Intuïtie* aankondigen. Effect ≈ +0,2.

## Navertelling in vijf zinnen

Regnault mat in 1863 dat de koersafwijking met de wortel van de tijd groeit, en
Bachelier bewees in 1900 dat dat volgt uit een random walk, die in de limiet een
Brownse beweging wordt. Uit dat model volgen ook de kans om een koersniveau te
raken (twee keer de kans om erboven te eindigen) en een optieprijs die alleen van
de spreiding afhangt, $0{,}4\,\sigma\sqrt\tau$ op het geld. De random walk is
toetsbaar via autocorrelaties, runs en vooral de variance ratio, maar kleine
afwijkingen vragen decennia data. Op Amerikaanse data klopt de $\sqrt t$-wet
(helling 0,51), en de variance ratios van Lo en MacKinlay repliceren, met grotere
afwijkingen bij kleine aandelen, die na 1985 verdwenen of van teken wisselden.
Het model zegt niets over het niveau van een prijs, en daarom is een theorie van
waarde nodig.

Wijkt niet af van het Overzicht, behalve dat de laatste zin (geen theorie van het
niveau) daar niet staat.
