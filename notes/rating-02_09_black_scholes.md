STATUS 02_09_black_scholes F5c words=5199 prose=PASS open=0 cijfer=9,0 min=8,5

# Beoordeling 02_09_black_scholes: Black-Scholes-Merton en de CBOE

## Eindcijfer: 8,3

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 0,3·8,5 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,30.

## 1. Helderheid van de uitleg (8,5)

*Goed*
- "Intuïtie": Blacks eigen getalvoorbeeld (vijftig cent per euro, twee calls tegen één
  aandeel) maakt het hele argument concreet vóór er een formule staat.
- "Theorie": elk resultaat krijgt een getal uit toy of voorbeeld: $\Phi(d_2)$ tegen
  $0{,}648$ in de boom, delta $0{,}624$, $\tfrac12\sigma^2 = 2$ procentpunt, vega
  $19{,}7 \times 0{,}05 \approx 0{,}99$ euro.
- "Simulatie": de vuistregel van Derman en Kamal wordt in één regel herleid tot de
  standaardfout $\sigma/\sqrt{2N}$ van een volatiliteitsschatting, en krijgt meteen
  haar getal ($0{,}44$ euro).

*Aanmerkingen*
- "Toy-voorbeeld", tabel: "risicovrij bruto rendement per stap $R^{f}$ | 1,02", en
  "Opzet en aannames": "de rente $r$ is continu samengesteld". De lecture meldt één
  afwijking van de notatietabel ($S_t$ voor $p_t$), maar niet deze twee: in de
  notatietabel is $R^f$ netto en $r$ het netto simpele rendement.
- "Opzet en aannames": "In [](#01-02-bachelier) heette ze $P_t$. $C(S,t)$ en $P(S,t)$
  zijn de waarden van een call en een put". $P$ staat in twee opeenvolgende zinnen
  voor koers en put.
- "Replicatie": de figuuras "Log-moneyness $\log(K/F)$" en de kolommen "IV 90%" gebruiken
  $k = \log(K/F)$, dat alleen in de code (`otm["k"]`) gedefinieerd wordt.
- "Replicatie" (VRP): `lags=42` zonder zin waarom (overlap van 21 dagen); de lezer
  ziet niet waarom een gewone standaardfout hier fout zou zijn.

*Beter uitleggen*
- De overlap in de VRP-reeks: één zin dat opeenvolgende dagen 20 van de 21 dagen
  gerealiseerde volatiliteit delen, en daarom Newey-West met ruim twee keer die lengte.

*Voor een 9*: meld in "Opzet en aannames" ook $R^f$ bruto (in de boom) en $r$ continu;
gebruik een andere letter dan $P$ voor Bacheliers koers of laat de verwijzing weg;
definieer log-moneyness in de tekst vóór de smirk-tabel; één zin bij de 42 vertragingen.

## 2. Opbouw en rode draad (8)

*Goed*
- "Intuïtie" doet drie voorspellingen (prijs stijgt met $\sigma$ en niet met $\mu$;
  P&L van een frequente hedger gemiddeld nul ongeacht de drift; één implied volatility),
  en theorie, simulatie en replicatie lossen ze in die volgorde in, de laatste als
  barst.
- Toy-getallen lopen door in de theorie ($q = 0{,}6$, $0{,}648$, $0{,}624$) en de
  simulatie gebruikt de call uit de theorie ($4{,}49$, vega $19{,}7$).
- Routekaart en "Samengevat" staan op hun plek; 5.013 woorden, onder de grens.

*Aanmerkingen*
- "Simulatie" opent met een vraag en een bronnenverantwoording ("De theorie belooft
  exacte replicatie ... Hoe groot is de fout bij $N$ hedgemomenten ... Hun tabellen
  hebben we niet kunnen raadplegen."), niet met haar conclusie.
- "Simulatie": de controle op het voorbeeld van Derman en Kamal krijgt een oordeel
  "**Gedeeltelijk geslaagd.**" zonder replicatieblok ervoor. De lezer ziet drie
  oordelen in twee secties en weet niet welke replicaties zijn en welke controles.
- De alinea "Hier komt de standaardfout van 2% ... terug" in de simulatie en de slotalinea
  van de VRP-replicatie maken hetzelfde punt twee keer (tweede momenten zijn goed
  meetbaar), met verschillende getallen ($t \approx 5$ en $t = 12{,}8$ tegen $1{,}8$).

*Beter uitleggen*
- Eén zin bovenaan de simulatie met de uitkomst (spreiding volgt $1/\sqrt{N}$, drift
  laat geen spoor).

*Voor een 9*: laat "Simulatie" openen met haar conclusie; noem de Derman-Kamal-cel een
controle van de code (zonder oordeel "Gedeeltelijk geslaagd") of geef haar een blok;
houd het motief-argument op één plek.

## 3. Taal (8)

*Goed*
- Korte zinnen (gemiddeld 14,4 woorden, geen zin boven 40); geen u/je.
- Vaktermen krijgen ter plekke een Nederlandse omschrijving (*replicatie*, P&L,
  *risiconeutrale kansmaat*, *variance risk premium*).

*Aanmerkingen*
- "Overzicht": "Dit werk definieert het tijdvak" (vertaald Engels; zelfde punt als in
  02_05).
- "Wat er brak": "Een nieuwe markt prijsde zichzelf ermee binnen enkele jaren."
  Calque van "priced itself"; "prijsde" is geen gangbare vervoeging.
- "Theorie", note: "Legt men het CAPM op elk moment van het leven van de optie op"; "men"
  naast de "we" van de rest.
- "Hoe het getoetst wordt": "Zodra handelaren in implied volatility quoteren";
  "quoteren" is jargon waar "noteren" of "prijzen opgeven" volstaat.
- Elf puntkomma's; enkele verbinden twee zelfstandige zinnen ("De werkelijke kansen zijn
  niet fout; ze doen er voor de prijs alleen niet toe").

*Voor een 9*: herschrijf "definieert het tijdvak" en "prijsde zichzelf"; "men" naar "we";
"quoteren" naar Nederlands; knip de puntkomma-zinnen.

## 4. Toy-voorbeeld (9)

*Goed*
- Eén mechanisme (replicatie per knoop), met de hand na te rekenen, tabel hand/code met
  tien identieke regels, en de slotzin "De lezer weet nu het argument van de lecture in
  het klein".
- Stap 6 laat zien waarom de oude methode faalt: bij $p = 0{,}8$ moet de optie per stap
  $1{,}2527$ verdienen tegen $1{,}06$ voor het aandeel.

*Aanmerkingen*
- "Stap 2": "$\Delta = 8{,}9/19{,}8 = 0{,}4495$, waarde $5{,}2353$". $B$ ontbreekt, dus deze
  knoop is niet met de hand na te rekenen zonder het recept opnieuw toe te passen. Met
  zes stappen en drie niveaus zit het toy aan de bovenkant van vijf minuten.

*Voor een 9,5 of hoger*: geef in stap 2 en 3 ook $B$.

## 5. Code en figuren (8)

*Goed*
- De boomcel leest als het recept (`delta_at`, `bond_at`, achterwaartse lus), en
  `delta_hedge_pnl` heeft een zichtbare lus met premie, financiering en herbalancering.
- Vóór elke figuur staat waarop te letten ("Let links op de breedte van de verdelingen
  en rechts op de helling"; "Let erop dat geen enkele kromme horizontaal loopt").
- Controles in de code zelf: pariteit, PDE-residu en inverse ($10^{-15}$).

*Aanmerkingen*
- `cel-black-scholes-hedgefout` (hide-input) draait een tweede simulatie over zeven
  frequenties; het resultaat ($-0{,}48$) staat alleen in de figuurtitel en in de zin
  erna. Rekenwerk in een verborgen figuurcel.
- Eerste replicatiecel: ruim dertig regels met `groupby.apply`, `pivot_table`,
  booleaanse maskers en de Black-76-truc in één cel; de tekst ervoor dekt de stappen,
  maar de cel zelf heeft geen tussenuitvoer.
- Meerdere cellen mengen `print`-regels met een tabel (voorbeeld-call, Derman-Kamal,
  replicatie, VRP).
- `fig-black-scholes-smirk`: "Alle krommen dalen links van de termijnkoers" is
  dubbelzinnig (ze dalen van links naar rechts, ook rechts van de termijnkoers).

*Voor een 9*: haal de frequentiesimulatie uit de figuurcel naar een zichtbare cel met
een tabel; splits de eerste replicatiecel (termijnkoers per expiratie tonen, dan
implied volatility); vervang de `print`-regels door tabellen; herformuleer de
figuurtekst.

## 6. Replicatie en empirie (8)

*Goed*
- Twee replicatieblokken met bron, wat, data, verschil en verwachte afwijking, elk
  onder 250 woorden.
- Beide oordelen beginnen met "Geslaagd" en staan naast een tabel verwacht/hier.
- De smirk-replicatie meet precies wat de theorie zegt dat constant moet zijn, en de
  VRP-replicatie toetst [](#eq-black-scholes-hedge-pnl) op data: een mooie sluiting van
  de trap.

*Aanmerkingen*
- Geen enkel getal uit de originelen: "Hun tabellen hebben we niet ingezien, dus we
  noemen er geen getallen uit." en bij de smirk alleen het teken. De tabellen zijn
  verwacht/hier met kwalitatieve verwachtingen ("> 0, grootst"), geen origineel/hier.
- VRP-blok, verwachte afwijking: "Een negatief gemiddelde betekent een fout in de code."
  Dat is geen verwachte afwijking. De verschillen (S&P 500 tegen de hele markt, 30
  kalenderdagen tegen 21 handelsdagen) krijgen geen richting of grootte.
- "De grootste negatieve maanden vallen, zoals verwacht, in 2020 en 2008." De uitvoer
  noemt ook 2025-03 als vierde; de tekst laat het weg.

*Voor een 9*: neem ten minste één getal per bron op (de helling bij Rubinstein of
Constantinides-Jackwerth-Perrakis; het gemiddelde van Carr en Wu) of zeg per rij
waarom alleen het teken te toetsen is; vervang de zin over de fout in de code door een
verwachte richting van de twee verschillen; noem 2025-03.

## 7. Oefeningen (9)

*Goed*
- Instap op het toy ($K = 110$), afleiding (gamma en vega uit de pariteit, P&L bij de
  verkeerde volatiliteit), uitbreiding van de replicatie (VRP per deelperiode,
  benodigde jaren tegen 43 jaar voor de equity premium).
- Elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Oefening 1.2 (CRR-convergentie) is een tweede uitbreiding van het toy in plaats van
  een variatie; de uitwerking verklaart de tekenwisseling, maar de $\pm 1/n$-lijnen
  worden niet gemotiveerd.

## Feitelijke fouten

Geen gevonden.

Nagerekend en correct: de hele boom (knopen, $\Delta$, $B$, $10{,}3603$; $q = 0{,}6$;
$0{,}216$ en $0{,}432$; $7{,}475$ / $7{,}0439$; $20{,}3648$ / $19{,}1902$; $1{,}2527$ en
$1{,}06$); $\Phi(d_2)$-analoog $0{,}648$; Itô-bewijs ($\Var(Q_n) = 2th$); PDE en
Feynman-Kac; formule en putformule; tabel van Greeks; P&L-propositie en de benadering
vega $\times (\sigma_i - \sigma_g)$ ($0{,}99$); call $4{,}49$, delta $0{,}56$, vega
$19{,}7$; Derman-Kamal-regel en $0{,}44$; simulatie (0,4295 / 0,4432; factor 1,96;
1,86 / 0,92 / 0,43; $-0{,}019$ met $t \approx -2{,}3$; kwantiel $-3{,}25$; 41% van de
premie); motief-rekensom ($0{,}20$; $0{,}04$ en $t \approx 5$; $0{,}17$); smirk (11
september 2026 was een vrijdag, dus het weekend-argument klopt; 4521 opties, 28
expiraties, 19 van 19; 21 / 9 / 3 punten); VRP (9188 dagen; 19,5 / 15,5 / 4,0; $t$ 12,8;
85%; $1{,}8$); oefeningen (4,7018; fout 0,33 en 0,005; $\pm 0{,}99$, spreiding 0,43 /
0,61 / 0,55; 4,85 en 3,15, $t$ 15,0 en 6,1; 0,33 en 2,0 jaar; 42,7 jaar).

## De drie verbeteringen met het meeste effect

1. **Replicatie met ten minste één origineel getal per bron en een echte verwachte
   afwijking** (beide replicatieblokken, VRP-blok vooral). Replicatie 8 → 9.
2. **Simulatie opent met haar conclusie, en de Derman-Kamal-cel heet een controle**
   ("Simulatie"); het motief-argument over tweede momenten op één plek. Opbouw 8 → 9.
3. **Notatie en definities**: $R^f$ bruto en $r$ continu melden als afwijking, $P$ niet
   dubbel gebruiken, log-moneyness en de 42 vertragingen uitleggen; daarbij de drie
   calques ("definieert het tijdvak", "prijsde zichzelf", "quoteren"). Helderheid
   8,5 → 9, taal 8 → 9.

## Navertelling in vijf zinnen

Een optie is waard wat het kost om haar na te maken met aandeel en obligatie, en daarom
doet het verwachte rendement van het aandeel er niet toe, alleen de volatiliteit. In een
binomiale boom is dat met de hand te zien; in continue tijd levert de delta-hedge via
Itô een PDE zonder $\mu$, met als oplossing de Black-Scholes-formule als verdisconteerde
verwachting onder risiconeutrale kansen. Wie verkoopt tegen de verkeerde volatiliteit,
verdient het variantieverschil gewogen met gamma, en discreet hedgen laat een spreiding
over die met $1/\sqrt N$ daalt, terwijl de drift geen spoor nalaat. Op echte SPY-opties
is de implied volatility niet constant maar hoger bij lage uitoefenprijzen, het sterkst
bij korte looptijden. Implied volatility ligt gemiddeld vier punten boven de daarna
gerealiseerde, een premie die veel scherper gemeten is dan de equity premium. Dit komt
overeen met het Overzicht.

## Controle 1

Gecontroleerd op de versie na F5-1 (5.199 woorden, `--check` PASS). Alleen de eigen
punten. Nieuwe getallen nagerekend: $B$ in stap 2 en 3 ($-39{,}2647$; $-73{,}0681$;
$-23{,}0969$); $\log 0{,}9 = -0{,}105$; helling $-0{,}48$ (tabel $-0{,}4773$); termijnkoers
bij 2,26 jaar 8,7% boven spot. Geen feitelijke fouten.

**1. Helderheid**
- $R^f$ bruto en $r$ continu niet gemeld: **opgelost** ("wijken op drie punten af").
- $P$ dubbel: **opgelost** (verwijzing naar Bacheliers $P_t$ weg).
- Log-moneyness alleen in de code: **opgelost** (definitie met getal vóór de tabel).
- 42 vertragingen: **opgelost** (overlap van 20 van 21 dagen, twee keer de overlap).

**2. Opbouw**
- Simulatie opent niet met conclusie: **opgelost**.
- Derman-Kamal-oordeel: **opgelost** ("een controle van de code, geen replicatie").
- Motief-argument twee keer: **opgelost** (VRP-slotalinea verwijst terug naar de
  simulatie).

**3. Taal**
- "definieert het tijdvak": **opgelost**.
- "prijsde zichzelf": **opgelost**.
- "men": **opgelost**.
- "quoteren": **opgelost**.
- Puntkomma's tussen zinnen: **opgelost** (voorbeeld "niet fout. Ze doen ...").

**4. Toy**
- $B$ ontbreekt in stap 2 en 3: **opgelost**.

**5. Code en figuren**
- Frequentiesimulatie in verborgen figuurcel: **opgelost** (zichtbare cel met tabel).
- Eerste replicatiecel te dik: **opgelost** (termijnkoersen eerst getoond, dan implied
  volatility).
- `print`-regels: **opgelost** in de genoemde cellen (in de uitwerkingen staan er nog
  drie; die vielen buiten mijn punt).
- Smirk-figuurtekst dubbelzinnig: **opgelost** ("Van diepe puts naar de termijnkoers
  dalen alle krommen").

**6. Replicatie**
- Geen getal uit de originelen: **deels**. Er staat nog geen getal, maar beide blokken
  zeggen nu waarom alleen teken en vorm te toetsen zijn.
- "fout in de code" als verwachte afwijking: **opgelost** (richting door hele markt tegen
  S&P 500; 30 kalenderdagen ≈ 21 handelsdagen).
- 2025-03 weggelaten: **opgelost**.

**7. Oefeningen**
- $\pm 1/n$ niet gemotiveerd: **opgelost**. Het bezwaar "tweede uitbreiding" is door de
  schrijver met STYLE §11.7 afgewezen; dat telt niet meer mee.

**Nieuwe cijfers**

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 8,5 | 9 |
| 2 | Opbouw | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 9 |
| 4 | Toy | 10% | 9 | 9,5 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie | 10% | 8 | 8,5 |
| 7 | Oefeningen | 5% | 9 | 9 |

Eindcijfer: 0,3·9 + 0,2·9 + 0,15·9 + 0,1·9,5 + 0,1·9 + 0,1·8,5 + 0,05·9 = 9,00, **9,0**.
Laagste deelcijfer 8,5. Streefcijfer gehaald.

Wat nog ontbreekt voor een 9 op replicatie: één geverifieerd getal uit Rubinstein,
Constantinides-Jackwerth-Perrakis of Carr-Wu.
