STATUS 02_06_efficiente_markten F6 words=5444 prose=PASS open=2 cijfer=8,3 min=8

# Eindbeoordeling (F6): Fama en de efficiënte markt

## Eindcijfer: 8,3

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,60 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 = 8,33, dus 8,3.
Lengte: 5.444 woorden, net onder de 5.500.

## Feitelijke fouten

Nagerekend met `uv run python -c ...` en tegen de celuitvoer (`tools/nb_outputs.py`):
het toy (116; 76; 92; 96; 4,35%, 3,45%, 5,26%; risicocorrectie 4; $q = 0{,}4$ en
$0{,}4 \cdot 116 + 0{,}6 \cdot 76 = 92$; covariantie $1 - 1{,}0435$), de helling
$\phi - 1 = -0{,}5$ en de uitvoer $-0{,}500$ en $-0{,}001$, de Sharpe-ratio
$0{,}6/4{,}5 = 0{,}13$, 3,6 pp rond 7,2%, $\sigma/\mu = 7{,}5$ en de drempel 3 bij
$\mu_t = 1{,}5\%$, $R^2 = 0{,}44\%$, $N^* = 3{,}84/0{,}004425 = 868$ (ruim 72 jaar),
$7{,}84/R^2 = 1772$ (bijna 150 jaar), de powertabel (60% na 100 jaar; grootste
verschil 6 punten bij 75 jaar; onder 2 bij 150; halve kans rond 80 jaar), het
filter (12,9 pp voorsprong, voorspeld 13,9, FB 1,7; ruim acht na kosten; 48
transacties per jaar), de deelperiodes (6, 13, 21, $-11$, SPY $-16$ pp), Jensen
($-0{,}3\%$, $t = -0{,}7$; Contrafund 1,4%, $t = 1{,}3$; T. Rowe $t = -2{,}28$;
bèta 1,01; 535 maanden is 44 jaar), de oefeningen ($k = 4/11$; 10%, 6,45%, 8,51%;
33%; $2^{22} = 4.194.304$, simulatie 3,5 promille ernaast; $c^*$ 0,27% tot 0,41%,
alleen lang 0,16% en 0,27%; 6,8% tegen 10,4%). Twee beweringen kloppen niet.

1. **Replicatie, na de eerste filtertabel.** "Bij hen is de voorsprong vanaf 1%
   weg, op de index pas vanaf 10%." Op de index ligt het 3%-filter al 1,0 pp onder
   buy-and-hold (0,1014 tegen 0,1115); bij 5% ligt het er weer 2,9 pp boven. De
   voorsprong verdwijnt dus niet pas bij 10%, maar wordt vanaf 3% grillig.
2. **Overzicht.** "In 1970 bracht Fama beide samen in een overzichtsartikel. Met dat
   artikel begint het tijdvak van deze lecture." Het kader "Waar we zijn" geeft als
   jaartal 1965–1970, en de lecture opent met Fama (1965) en Samuelson (1965). Het
   tijdvak begint in 1965; het artikel van 1970 sluit het af.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- Toy-voorbeeld: de SDF krijgt naam, betekenis en getallen (0,8 en 1,2) voordat hij
  iets doet, en de risicocorrectie van 4 op 116 tegen 76 maakt voorspelbaarheid
  zonder vergissing tastbaar.
- "Wat het niet verbiedt": de propositie krijgt direct een getal (Sharpe-ratio 0,13,
  SDF-schommeling 13% per maand), en de positiviteitsvoorwaarde wordt in de
  simulatie met $\sigma/\mu = 7{,}5$ uitgerekend.
- "Het kernresultaat": het AR(1)-voorbeeld met $\phi = 0{,}5$ laat de stelling in
  één regel en één tabel zien.

*Aanmerkingen*
- Toy en Theorie: "De rente is nul, $R^f = 1$" en
  "$\frac{1}{R^{f}_{t+1}} = \E_t[m_{t+1}]$". Hier is $R^f$ bruto; de setup-tabel
  reserveert $R^f$ voor de netto rente. De afwijking wordt nergens genoemd.
- Opzet, definitie 3: "Log-rendementen volgen een **random walk** als de $r_{t+1}$
  onafhankelijk en identiek verdeeld zijn". In de setup is $r$ het netto simpele
  rendement en krijgt een logrendement een eigen symbool ($\ell$).
- "Hoe het getoetst wordt": "Wie steeds de richting van gisteren volgt, verdient per
  dag ongeveer $\rho_1 \sigma \sqrt{2/\pi}$". Formule zonder herkomst en zonder
  getal; het getal (13,9 pp) komt pas in de replicatie, en daar met een extra
  $-\mu$.
- Grossman en Stiglitz: "Een fractie $\lambda$ van de beleggers betaalt een bedrag
  $c$". Twee symbolen zonder orde van grootte, en $\lambda$ botst met $\lambda_f$ uit
  de setup.
- Jensen-replicatie: "De regressie is het CAPM: het verwachte excess rendement van
  een fonds is evenredig met zijn bèta op de markt." Het CAPM en de bèta komen pas
  in [](#02-08-capm); één regel is hier de hele uitleg.

*Beter uitleggen*
- De filterformule: één zin dat $\E[\operatorname{sign}(x)\,y] = \rho\sigma\sqrt{2/\pi}$
  voor twee normale variabelen, en het getal voor 1957–1962 er meteen bij.
- Grossman-Stiglitz: één getallenvoorbeeld (bijvoorbeeld $c$ als fractie van het
  bruto voordeel), of het mechanisme zonder symbolen.

### 2. Opbouw en rode draad (8)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord (alleen samen met een model
  toetsbaar).
- De drie verwachtingen uit de intuïtie worden elk met naam ingelost ("Dat is de
  eerste verwachting uit de intuïtie", de tweede bij de premie, de derde bij
  Grossman-Stiglitz).
- De toestandsafhankelijke premie loopt van het toy (3,45% tegen 5,26%) naar de
  simulatie ("Net als in het toy-voorbeeld").

*Aanmerkingen*
- De simulatie toetst een voorspellende regressie op $s_t$, de replicatie
  filterregels op de index. Toy, simulatie en replicatie delen het idee, niet de
  toets of de getallen.
- De theorie draagt vijf delen, waaronder een eigen Samuelson-simulatie; met de
  Jensen-replicatie erbij heeft de lecture twee empirische lijnen.
- Overzicht: "Met dat artikel begint het tijdvak" (zie feitelijke fouten).

*Beter uitleggen*
- Eén zin bij de overgang naar de replicatie die zegt waarom het filter en niet de
  regressie uit de simulatie wordt gerepliceerd (het filter omzeilt de joint
  hypothesis bijna).

### 3. Taal (8,5)

*Goed*
- Korte zinnen (gemiddeld 14,4 woorden), geen u/je; *fair game*, *joint
  hypothesis* en *limits of arbitrage* krijgen bij eerste gebruik een Nederlandse
  uitleg; het citaat van Fama (1991) staat als blokcitaat met inleiding.
- De motieven zeggen ter plekke wat ze betekenen ("De figuur laat risico of
  vergissing zien in een wereld waarin het antwoord bekend is").

*Aanmerkingen*
- Risico of vergissing: "het is een meetfout door niet-synchrone handel, die
  verdwijnt bij een verhandelbaar instrument gebruikt." Ongrammaticaal.
- Dertien puntkomma's, onder meer "Voor 80% kans is ... nodig, bijna
  honderdvijftig jaar; 0,84 is het 80%-kwantiel".

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Twee perioden, vier dividenden, achterwaarts rekenen in drie regels; tabel hand
  tegen code; "Wat we nu weten" koppelt het toy aan de joint hypothesis.

*Aanmerkingen*
- De "Vooruitblik" met $q$ voegt een tweede begrip toe dat pas in de theorie
  (maat $Q$) betekenis krijgt.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `filter_positions` leest als de regel van Alexander, met een zichtbare lus en
  benoemde toestanden.
- Powerfiguur: vooraf "Let in de figuur links op ... rechts op", het bijschrift zegt
  wat te zien is.

*Aanmerkingen*
- `hap_data.yahoo(["SPY", "TLT", "GLD", "QQQ", "IWM"], "1993-01-01")["SPY"]`: vier
  tickers worden geladen en niet gebruikt, zonder uitleg.
- `hap.stats.newey_west(y, X, lags=0)`: een Newey-West-aanroep zonder lags; de tekst
  zegt niet welke standaardfout de $t$-waarden dragen.
- Filterfiguur: vooraf alleen "De figuur zet beide reeksen naast elkaar." Geen
  aanwijzing waarop te letten.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8,5)

*Goed*
- Fama-Blume-blok met drie toetsbare criteria, waarvan de eerste een formule is;
  oordeel "Geslaagd op criterium 1" met 12,9 tegen voorspeld 13,9.
- Jensen-blok met een controle (VFINX) en een tabel origineel/hier.

*Aanmerkingen*
- "zes procentpunt per jaar tot 1956, dertien in het venster van Fama en Blume,
  eenentwintig in 1963–1989": getallen uit de tabel herhaald in lopende tekst, net
  als "12,9 ... 13,9 ... 1,7" en de Jensen-alinea.
- "op de index pas vanaf 10%" (zie feitelijke fouten).

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op het toy ($k$), afleiding van het Samuelson-effect, uitbreiding van de
  replicatie (break-even kosten); elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. $R^f$ bruto en $r$ als logrendement in één zin als afwijking van de setup noemen
   (of $\ell$ schrijven), en de filterformule met één zin herkomst en een getal
   geven (helderheid 8 → 8,5).
2. "pas vanaf 10%" en "begint het tijdvak" corrigeren, en één brugzin tussen
   simulatie (regressie) en replicatie (filter) (opbouw 8 → 8,5).
3. De deelperiodegetallen uit de lopende tekst halen en naar de tabel verwijzen
   (replicatie 8,5 → 9).

## Navertelling in vijf zinnen

Een prijs die de verwachting van een latere uitbetaling is, verandert
onvoorspelbaar, ook als die uitbetaling voorspelbaar is (Samuelson). Voor aandelen
geldt dat pas na weging met de SDF, dus mag het verwachte rendement bewegen met de
prijs van risico, en elk patroon zonder arbitrage heeft een SDF die het verklaart.
Efficiëntie is daarom alleen samen met een model van risico te toetsen, en een
onderzoeker met het verkeerde model heeft zo'n zeventig tot tachtig jaar data nodig
om een rationele schommeling als inefficiëntie te zien. Filterregels verslaan
buy-and-hold op de index van 1957–1962 ruim, maar dat komt door niet-synchrone
handel en verdwijnt op verhandelbare instrumenten en na kosten. Fondsbeheerders
verslaan de markt niet aantoonbaar.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-02_06_efficiente_markten.md` §F6-1 en de
lecture, na de omzetting "alfa" naar "alpha".

STATUS 02_06_efficiente_markten F6c words=5457 prose=PASS open=0 cijfer=8,8 min=8,5

| punt | status | vindplaats |
|---|---|---|
| Fout 1: "pas vanaf 10%" | opgelost | "op de index wordt ze vanaf 3% grillig" |
| Fout 2: begin van het tijdvak | opgelost | "Dat artikel sluit het tijdvak af dat in 1965 begon" |
| Verbetering 1: $R^f$, $\ell$, filterformule | opgelost | toy: "Anders dan in [](#00-00-setup) is $R^f$ in deze lecture bruto"; definitie 3 en propositie met $\ell_{t+1} = \log R_{t+1}$; herkomst en getal bij $\rho_1\sigma_d\sqrt{2/\pi}$ |
| Verbetering 2: fouten en brugzin | opgelost | "We repliceren niet de voorspelregressie uit de simulatie maar het filter, omdat het filter de joint hypothesis bijna omzeilt" |
| Verbetering 3: deelperiodegetallen | opgelost | het oordeel over criteria 2 en 3 verwijst naar de tabel |
| Naadpunt 1 ($R^f$ bruto) | opgelost | zie verbetering 1 |
| Naadpunt 2 ($r$ als log) | opgelost | zie verbetering 1 |
| Naadpunt 5 (alfa) | opgelost | overal "alpha", in tekst, tabellen en celuitvoer |
| Naadpunt 9 ($\lambda$) | opgelost | Grossman-Stiglitz met $\omega$ |
| Naadpunt 12 (tijdvak) | opgelost | zie fout 2 |

Ook opgelost: de ongrammaticale zin ("die verdwijnt bij een verhandelbaar
instrument"), de puntkomma bij 0,84, een leeswijzer voor de filterfiguur ("Let in
de figuur op de afstand tussen de ronde punten en de vierkanten"), de soort
standaardfout bij Jensen, en een commentaar bij de download van vijf tickers.

Geen verslechteringen en geen nieuwe feitelijke fouten. Nagerekend:
$0{,}175 \cdot 0{,}68\% \cdot 0{,}798 = 0{,}095\%$ per dag, maal 252 is 23,9% tot
24,0%; "ruim 24%" is een afronding naar boven, geen fout. De celuitvoer is op de
kolomnamen na gelijk.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 8,5 | 9 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 9 |
| 6 | Replicatie | 8,5 | 9 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,70 + 1,35 + 0,90 + 0,90 + 0,90 + 0,45 = 8,75. **Eindcijfer 8,8,
laagste deelcijfer 8,5.** Helderheid blijft 8,5: het CAPM wordt in de
Jensen-replicatie nog steeds in één regel ingevoerd. Opbouw blijft 8,5 om de
theorie van vijf delen met twee empirische lijnen.
