# Beoordeling: 01_04_markowitz — Markowitz, Roy en Tobin

Maatstaf: `plannen/rubriek-didactiek.md`. Lezer: eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft. Kalibratie gelijk aan
de beoordelingen van 00_01, 01_02 en 01_03.

## Eindcijfer: 7,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 7 |

Gewogen: 0,3·8 + 0,2·8 + 0,15·7 + 0,1·8 + 0,1·7 + 0,1·8 + 0,05·7 = 7,70 → 7,7.
Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

---

## 1. Helderheid van de uitleg — 8

**Goed**
- *Het kernresultaat: de efficiënte rand*: elke abstracte grootheid krijgt een
  toy-getal. $A = 128{,}125$ is "de som uit stap 3", $D = 15{,}625$ tegen
  $AC = 65{,}5$, $\lambda = 0{,}368$ en $\delta = -0{,}0125$ bij 10%, en de helling
  "een procentpunt extra rendement kost bij 10% ongeveer ... 0,0074 extra
  variantie". Hier doet de lecture wat de rubriek voor een 10 vraagt.
- *Een risicovrij activum: Tobin en Roy*: de tangentportefeuille met de hand
  ($\mathbf{w}_{\mathrm{tan}} = (1/3;\ 2/9;\ 4/9)'$, $S_{\max} = 0{,}529$),
  vergeleken met de 0,4 van de Amerikaanse markt. De Roy-grens krijgt een
  exemplaar (17% tegen 0,8% onder normaliteit).
- *Hoe het toegepast wordt*: de bias $N/T$ wordt direct vertaald ("$N/T = 0{,}083$
  per maand, vier keer de ware $S^2_{\max}$ van 0,021").

**Aanmerkingen**
- *Opzet en aannames*: "Er zijn $N$ risicovolle activa met bruto rendementen
  $\mathbf{R}_{t+1}$, verwachting $\boldsymbol{\mu} = \E[\mathbf{R}_{t+1}]$".
  Twee zinnen later: "Het toy-voorbeeld rekent met netto rendementen". De
  randformules (minimum bij $B/A = 5{,}51\%$, $C/B = 7{,}24\%$) kloppen alleen met
  netto $\boldsymbol{\mu}$. "Voor $\boldsymbol{\Sigma}$ en voor premies maakt die
  keuze niets uit" dekt $A$, $B$, $C$ en $D$ niet.
- *Hoe het toegepast wordt*: "een variantie scherper wordt met meer waarnemingen
  per jaar ... en een gemiddelde niet [](#00-00-setup)." Dat resultaat (Merton)
  staat in [](#00-01-rendementen); dezelfde verkeerde verwijzing staat in oefening 3
  ("Dat is de les uit [](#00-00-setup)").
- *Risico of vergissing?*: "Santa-Clara ([](#00-00-setup)) zegt het zo". Wie
  Santa-Clara is, staat er niet; de lezer moet de eerste lecture openen.
- *Opzet en aannames*: "Mean-variance is dus een tweede-orde benadering van elk
  nut". Het "dus" volgt niet uit de zin ervoor (die over kwadratisch nut en
  normaliteit gaat); de Taylor-redenering is een derde rechtvaardiging, geen
  gevolg.
- *Het kernresultaat*: "en de bèta-vorm van het CAPM staat al op papier". Het CAPM
  is in de reeks nog niet behandeld; de lezer krijgt een verwijzing naar iets
  dat hij niet kent.
- *Replicatie*: "wat past bij een twintig jaar langere steekproef." Waarom een
  langere steekproef bij een vast venster van 120 maanden het niveau positief
  maakt, wordt niet uitgelegd.

**Beter uitleggen**
- In de *Opzet* één keer kiezen: $\boldsymbol{\mu}$ is het verwachte netto
  rendement, en zeggen dat bruto rendementen $A$ ongemoeid laten maar $B$ en $C$
  verschuiven.
- Santa-Clara in een bijzin plaatsen (wie, welke uitspraak).
- Bij de bèta-vorm één zin dat dit de vorm is die [het CAPM](#02-08-capm) later
  een economische betekenis geeft.

## 2. Opbouw en rode draad — 8

**Goed**
- *Overzicht* stelt de vraag en geeft het antwoord ("een activum is zo riskant als
  zijn covariantie met de rest van de portefeuille"), met routekaart.
- De twee voorspellingen uit *Intuïtie* worden zichtbaar ingelost ("Zo lost de
  theorie de eerste voorspelling van de intuïtie in"; "Zo lost de theorie de
  tweede voorspelling van de intuïtie in"), en de derde uitspraak over
  idiosyncratisch risico ook ("zoals de intuïtie voorspelde").
- Theoriesecties openen met hun conclusie ("De bewering: ..."). De toy-getallen
  lopen door tot in de replicatie ("in het toy-voorbeeld 8,83% tegen 10% voor het
  veiligste activum, wint hier van beide") en oefening 1.

**Aanmerkingen**
- Het *Samengevat*-blok staat aan het eind van *Theorie*, niet aan het eind van
  de lecture (zelfde aftrek als bij de eerdere lectures).
- *Een risicovrij activum*: de alinea over de Hansen-Jagannathan-grens en de
  stochastische disconteringsfactor is een vooruitblik die de lecture niet
  gebruikt.
- *Intuïtie*: Roy en de ongelijkheid van Bienaymé-Tchebycheff worden hier al
  uitgelegd en in de theorie opnieuw; de intuïtie wordt daardoor lang (vier
  personen, twee notes).

**Beter uitleggen**
- Een *Samengevat* aan het eind met de replicatiegetallen (0,081 tegen 0,158 per
  maand).

## 3. Taal — 7

**Goed**
- Eén naam per begrip wordt expliciet vastgelegd: "volatiliteit is hetzelfde
  woord voor hetzelfde getal"; "(hierna 1/N)"; "(hierna de
  mean-variance-portefeuille)".
- Het Engelse citaat van Friedman staat als blokcitaat met inleiding.
- Korte, heldere zinnen in *Intuïtie* ("Honderd aandelen van banken die op elkaar
  lijken, zijn niet gespreid.").

**Aanmerkingen**
- *Overzicht*: "In juli kwam A. D. Roy in *Econometrica* vanuit een ander
  principe, beperk de kans op een ramp, bij bijna dezelfde meetkunde uit" — een
  gebiedende wijs midden in een zin, en het werkwoord pas aan het eind.
- *Simulatie*: "Gemiddelden veel erger dan covarianties: die rangorde vonden ook
  {cite:t}`ChopraZiemba1993`, en die rangorde is de standaardfout van 2% in zijn
  zuiverste vorm: het gemiddelde is de zwakke schakel, niet het tweede moment."
  Zinsfragment gevolgd door twee dubbele punten.
- Engelse termen zonder Nederlandse naam: "excess rendementen", "in-sample",
  "out-of-sample", "bruto exposure", "breakeven-venster", "risk-parityfondsen",
  "safety-first-belegger".
- *Replicatie*: "tot het einde van de snapshot" — projectjargon.
- Zichtbare spelling zonder trema in uitvoer en figuren: "efficiente rand",
  "10 industrieen", "De efficiente rand van drie activa".

**Beter uitleggen**
- "in de steekproef" / "buiten de steekproef" consequent gebruiken (de lecture
  doet dat al één keer: "de optimalisatie in de steekproef").

## 4. Toy-voorbeeld — 8

**Goed**
- Eén mechanisme, expliciet aangekondigd ("een mengsel van riskante activa kan
  veiliger zijn dan het veiligste activum"), met één nog niet afgeleide formule
  als recept.
- Slim gekozen getallen: C correleert met niets, zodat de inverse in een
  $2\times2$-blok en een getal uiteenvalt, en de gewichten exacte breuken zijn
  ($7/41$, $2/41$, $32/41$).
- Tabel hand/code en een slotzin met wat de lezer nu weet.

**Aanmerkingen**
- *Opzet*, tabel: "| A (aandelen) | 10{,}0% | 20{,}0% |". De accolades staan
  buiten wiskundemodus en worden letterlijk weergegeven ("10{,}0%").
- *Stap 2*: "Het blok heeft determinant $0{,}04 \cdot 0{,}09 - 0{,}02^2 =
  0{,}0032$" en direct daarna de inverse. De regel voor de inverse van een
  $2\times2$-matrix (diagonaal wisselen, teken omdraaien, delen door de
  determinant) staat er niet; $0{,}09/0{,}0032 = 28{,}125$ moet de lezer zelf
  vinden.

**Beter uitleggen**
- Eén regel met de $2\times2$-inverse en één uitgerekend element.

## 5. Code en figuren — 7

**Goed**
- De toy-cellen verwijzen naar de handstappen en vergelijkingen
  (`# Sigma^{-1} 1, stap 3`, `# eq-markowitz-frontier`).
- `rolling_oos` toont het rollende venster als zichtbare lus, met
  `# alleen maanden vóór t`.
- Vóór elke figuur staat waarop te letten ("Let op de afstand tussen elk activum
  en de rand"; "Let op hoe onrustig de mean-variance-lijn is"), erna een
  bijschrift.

**Aanmerkingen**
- *Simulatie*: `Sigma_hat = np.einsum("sti,stj->sij", demeaned, demeaned) / (T - 1)`
  en `np.linalg.solve(Sigma_hat, mu_hat[..., None])[..., 0]` — compacte
  tensor-trucs zonder commentaar bij de eerste; de lezer ziet niet dat hier per
  steekproef een covariantiematrix wordt geschat.
- *Replicatie*: `oos_industry.tail(3).round(4)` gevolgd door "De laatste drie
  maanden laten zien dat de mean-variance-portefeuille veel wilder beweegt".
  Drie rijen zijn geen bewijs voor een uitspraak over de hele reeks.
- *Replicatie*: `rf = hap_data.market_monthly()["RF"]` overschrijft de scalar
  `rf = 0.02` uit de theorie; wie een toy-cel opnieuw draait, krijgt een fout.
- *Replicatie*, vergelijkingstabel: de kolom "minimum-variantie out-of-sample"
  voor DGU is `[np.nan, np.nan, np.nan]`, zonder zin waarom.

**Beter uitleggen**
- Eén commentaarregel bij de `einsum`: "$\hat{\boldsymbol\Sigma}$ per steekproef,
  als som van uitproducten".
- De standaarddeviatie van de drie strategieën als bewijs voor "wilder" noemen;
  die staat al in de volgende tabel.

## 6. Replicatie en empirie — 8

**Goed**
- Blok met bron, wat, data, verschil en verwachte afwijking binnen 250 woorden,
  met een verwachting die de precisie meeneemt ("alleen teken, ordening en orde
  van grootte zijn informatief").
- Oordeel begint met **Geslaagd.**, verwijst naar de voorspelde ordening, en
  voegt een eerlijk voorbehoud toe ("geen van de afzonderlijke verschillen ...
  groter dan twee standaardfouten").
- De positieanalyse (2100% long, bruto exposure 7,5 en 72) maakt het mechanisme
  zichtbaar.

**Aanmerkingen**
- De tabel "origineel/hier" vergelijkt geen gelijke cellen: DGU's rijen zijn
  "S&P-sectoren (N = 11)", "internationaal (N = 9)" en "FF-vierfactor (N = 24)",
  onze rijen 10 industrieën en 25 size/BM. De lezer kan niet per rij zien hoe ver
  we van het origineel liggen.
- "Het gat tussen belofte en levering groeit met $N$: van 0,10 bij de
  industrieën naar 0,30 bij de 25 portefeuilles." Deze verschillen staan in geen
  tabel.
- "Ons out-of-sample niveau blijft positief waar dat van DGU soms negatief wordt,
  wat past bij een twintig jaar langere steekproef." De verwachte afwijking
  voorspelde het niveau niet; de verklaring komt achteraf.

**Beter uitleggen**
- In het blok zeggen welke DGU-rij als tegenhanger van welke eigen rij geldt
  (S&P-sectoren ↔ 10 industrieën, FF-vierfactor ↔ 25 size/BM), en de
  gat-kolom (in-sample min out-of-sample) aan de tabel toevoegen.

## 7. Oefeningen — 7

**Goed**
- Instap is een variatie op de toy (correlatie A-B op nul), met de les in één zin.
- Oefening 1 (zero-beta) is een echte afleiding die op de toy-getallen landt
  ($\mu_z = 2{,}00\%$) en naar {cite:t}`Black1972` wijst.
- Oefening 3 breidt de replicatie uit (shrinkage) en toont eerlijk dat het
  tussengebied zich niet netjes gedraagt.

**Aanmerkingen**
- *Oefening 2, uitwerking (3)*: "Wie vijf keer zoveel activa optimaliseert, heeft
  ongeveer vijf keer zoveel geschiedenis nodig". De eigen tabel geeft 2880 maanden
  bij $N = 5$ en 3840 bij $N = 25$: vijf keer zoveel activa, 1,3 keer zoveel data.
  De les spreekt de uitkomst tegen.
- *Oefening 2, uitwerking (2)*: "De conclusie hangt dus niet aan de details van de
  kalibratie." Eén kalibratie met 200 herhalingen, die de tekst zelf "onrustig"
  noemt, draagt die bewering niet.
- *Oefening 3, uitwerking*: "Dat is de les uit [](#00-00-setup)" — verkeerde
  verwijzing (zie criterium 1).

**Beter uitleggen**
- In oefening 2 de les baseren op de $N/T$-bias bij vast $T$ (de kolom "mv bij
  T=120": 0,294 → 0,149), die de tabel wél laat zien.

---

## De drie verbeteringen met het meeste effect op het cijfer

1. **Helderheid (8 → 9):** bruto/netto in de *Opzet* rechttrekken, de verwijzingen
   naar [](#00-01-rendementen) herstellen, Santa-Clara plaatsen en het "dus" bij
   de Taylor-benadering weghalen. Effect op het eindcijfer ≈ +0,3.
2. **Taal (7 → 8):** de Roy-zin en het fragment over Chopra-Ziemba herschrijven,
   Nederlandse namen voor in/out-of-sample en exposure, trema's in labels, en
   "snapshot" eruit. Effect ≈ +0,15.
3. **Code (7 → 8):** commentaar bij de `einsum`-regels, `tail(3)` vervangen door
   een echte maat, `rf` niet overschrijven, de NaN-kolom verklaren.
   Effect ≈ +0,1.

## Navertelling in vijf zinnen

Markowitz verving de vraag hoe riskant één aandeel is door de vraag hoe riskant
de portefeuille wordt, en dan telt alleen de covariantie van een activum met de
rest. De efficiënte portefeuilles vormen een parabool in variantie en verwacht
rendement, elk is een mengsel van twee fondsen, en een mengsel kan veiliger zijn
dan het veiligste activum. Met een risicovrij activum houdt iedereen dezelfde
tangentportefeuille met de hoogste Sharpe-ratio (Tobin), wat Roy vanuit
rampvermijding ook vond, en in een grote portefeuille verdwijnt het
idiosyncratische risico. In de praktijk moeten de verwachte rendementen geschat
worden, en die fout is zo groot dat de geschatte optimale portefeuille slechter
presteert dan 1/N. De replicatie van DeMiguel, Garlappi en Uppal bevestigt dat,
en de minimum-variantieportefeuille, die geen gemiddelden gebruikt, doet het
het best.

Wijkt niet af van het Overzicht; de rol van de minimum-variantieportefeuille als
winnaar staat daar niet, maar volgt uit de lecture.
