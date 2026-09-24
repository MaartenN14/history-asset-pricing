STATUS 02_09_black_scholes F6 words=5172 prose=PASS open=0 cijfer=8,5 min=8

# Eindbeoordeling (F6): Black-Scholes-Merton en de CBOE

## Eindcijfer: 8,5

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8,5 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,55 + 1,70 + 1,275 + 0,85 + 0,85 + 0,80 + 0,45 = 8,475, dus 8,5.
Lengte: 5.172 woorden, onder de 5.500.

## Feitelijke fouten

Nagerekend met `uv run python -c ...` en tegen de celuitvoer: de boom (alle
$\Delta$, $B$ en waarden per knoop; $C_0 = 10{,}3603$; $q = 0{,}6$; $0{,}216$ en
$0{,}432$; 7,475 en 7,0439; 20,3648 en 19,1902; 1,2527 en 1,06), $\tfrac12\sigma^2
= 2$ pp, $q^3 + 3q^2(1-q) = 0{,}648$, de call (4,49; delta 0,56; vega 19,7; 20 cent
per punt; $19{,}7 \cdot 0{,}05 = 0{,}99$), de vuistregel ($\sqrt{\pi/2} = 1{,}253$;
0,44 euro bij $N = 63$), de controle van Derman en Kamal (1 à 3% onder de regel;
factor 1,96; binnen 1,4 SE), de hedgetabel (1,86, 0,92, 0,43; $t = -2{,}3$; 0,4%
van de premie; $-3{,}25$ is 72%; ruim 40%), de helling $-0{,}48$ over bijna twee
decaden, de tien jaar opties ($0{,}43/\sqrt{120} = 0{,}04$, $t \approx 5$;
$0{,}17$), de smirk (19 van 19; 21, 9 en 3 punten; ATM 7 tot 12% bij de vier
kortste; 11 september 2026 is een vrijdag; $\log 0{,}9 = -0{,}105$), de VRP (19,5%,
15,5%, 4,0 punten, $t = 12{,}8$, 85%; de vier slechtste maandeinden), de oefeningen
(4,7018; CRR-fout 0,33 en 0,005, binnen $\pm 1/n$ voor alle $n \le 200$ en
alternerend; $\pm 0{,}99$; 0,43, 0,61, 0,55; 4,85 en 3,15; $t$ 15,0 en 6,1; 0,33
en 2,0 jaar; 42,7 jaar). Geen fouten gevonden.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- Opzet: de drie afwijkingen van de setup-notatie ($S_t$, $R^f$ bruto in de boom,
  $r$ continu) staan er in één alinea.
- Itô: het lemma krijgt meteen een getal (twee procentpunt bij 20%) en een
  terugverwijzing naar het verschil tussen rekenkundig en meetkundig gemiddelde.
- "Wat een hedger verdient": de benadering vega maal $\sigma_i - \sigma_g$ wordt
  afgeleid en uitgerekend (0,99 euro), en keert terug in oefening 2.

*Aanmerkingen*
- "Wat het voorspelt": "Die wereld heet de *risiconeutrale kansmaat*
  $\mathbb{Q}$". De maat en de risiconeutrale kansen werden al in
  [](#02-06-efficiente-markten) ingevoerd (toy-vooruitblik en de stelling over de
  maat $Q$); hier worden ze opnieuw ingevoerd zonder terugverwijzing.
- Toy: "stijgfactor $u$ / daalfactor $d$". In de setup is $d_t$ het dividend; die
  afwijking staat niet bij de drie genoemde.
- Simulatie: "Wie $N$ keer hedget, meet de volatiliteit in feite uit $N$
  waarnemingen, met een standaardfout van ongeveer $\sigma/\sqrt{2N}$. Maal de vega
  is dat, op een factor $\sqrt{\pi/2}$ na, de spreiding". De factor wordt genoemd,
  niet uitgelegd.

*Beter uitleggen*
- De factor $\sqrt{\pi/2}$: één zin dat de P&L per stap met $|\Delta S|$ en niet met
  $(\Delta S)^2$ schaalt, of de regel als citaat van Derman en Kamal laten staan.

### 2. Opbouw en rode draad (8,5)

*Goed*
- Overzicht stelt de vraag en geeft het antwoord (de kosten van namaken, alleen
  afhankelijk van de volatiliteit).
- Drie verwachtingen uit de intuïtie, ingelost door theorie ($\mu$ valt weg),
  simulatie (P&L rond nul, drift zonder spoor) en replicatie (één implied
  volatility, verworpen).
- De getallen lopen door: $q = 0{,}6$ en delta 0,624 van boom naar formule, de call
  van 4,49 van theorie naar simulatie en oefeningen, de P&L-propositie naar de
  VRP-replicatie.

*Aanmerkingen*
- De simulatie heeft een eigen codecontrole (Derman-Kamal) vóór de eigenlijke vraag,
  en de alinea over de standaardfout van 2% breidt uit naar een optieverkoper over
  tien jaar; samen met twee replicaties maakt dat de tweede helft voller dan de
  eerste.

*Beter uitleggen*
- Geen.

### 3. Taal (8,5)

*Goed*
- Korte zinnen, geen u/je; het getal van Black ("vijftig cent") maakt de hedge in
  gewone taal voelbaar.
- Chicago- en Yale-lezing zeggen tussen haakjes wat ze betekenen.

*Aanmerkingen*
- "de getallen van de bronnen zijn niet tegen de bron te houden" (smirk-blok),
  "Hun getallen zijn niet tegen de bron te houden" (VRP-blok), "de getallen van
  Derman en Kamal zijn niet tegen de bron te houden": een ongebruikelijke wending,
  drie keer, de eerste bijna tautologisch.
- Overzicht: "Met dit werk begint een nieuw tijdvak: het is de eerste
  waarderingsregel". "Het" verwijst naar "dit werk", bedoeld is de formule.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (8,5)

*Goed*
- Eén mechanisme (replicatie per knoop), recept vooraf, tabel hand/code, en de zin
  "De lezer weet nu het argument van de lecture in het klein".
- Stap 6 laat zien waarom de oude methode een onbekende discontovoet nodig had
  (1,2527 tegen 1,06).

*Aanmerkingen*
- Zes knopen met elk $\Delta$ en $B$ op vier decimalen, plus twee
  verwachtingswaarden: met de hand eerder vijftien minuten dan vijf.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `delta_hedge_pnl` boekt premie, delta, financiering en payoff in een zichtbare
  lus, zoals de tekst het beschrijft.
- Hedgefiguur en smirkfiguur hebben vooraf "Let ... op" en een bijschrift dat zegt
  wat te zien is.

*Aanmerkingen*
- `bs_price`: `np.where(np.asarray(kind) == "call", call, call - S + K * np.exp(-r * T))`
  en `float(price) if price.ndim == 0 else price`: compacte trucs voor
  scalar/array; de put via de pariteit staat niet als formule in de code.
- VRP-figuur: vooraf alleen "De figuur laat zien waar het omslaat."

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8)

*Goed*
- Twee blokken, elk met een verwachte afwijking die alleen teken en vorm toetst, en
  een tabel verwacht/hier; oordelen "Geslaagd" gekoppeld aan die verwachting.
- De termijnkoers uit de pariteit omzeilt de dividendaanname, en de tekst zegt
  waarom.

*Aanmerkingen*
- Geen van beide replicaties heeft een kolom "origineel": de getallen van
  Rubinstein, Whaley en Carr-Wu komen niet in de lecture.
- VRP-oordeel: "Over 9188 handelsdagen lag de VIX gemiddeld op 19,5% en de daarna
  gerealiseerde volatiliteit op 15,5%. Het verschil van 4,0 volatiliteitspunten heeft
  $t = 12{,}8$ en is positief op 85% van de dagen." Tabelgetallen in lopende tekst.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Instap op de boom ($K = 110$ en CRR-convergentie), afleiding (gamma en vega uit de
  pariteit, verkeerde volatiliteit), uitbreiding van de replicatie (VRP per
  periode); elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. Bij $\mathbb{Q}$ in één zin terugverwijzen naar de maat uit
   [](#02-06-efficiente-markten), en $d$ als daalfactor bij de notatieafwijkingen
   zetten (helderheid 8,5 → 9).
2. Per replicatie één getal uit de bron naast het eigen getal zetten (bijvoorbeeld
   de gemiddelde VIX-min-RV van Carr en Wu), en de getallen uit de VRP-alinea
   halen (replicatie 8 → 8,5).
3. Het toy tot twee stappen inkorten of de knooptabel vooraf geven
   (toy 8,5 → 9).

## Navertelling in vijf zinnen

Een optie is waard wat het kost om haar met aandeel en obligatie na te maken, en
die kosten hangen niet af van het verwachte rendement of de risicoaversie, alleen
van de volatiliteit. In continue tijd maakt een delta-hedge de positie risicovrij,
wat een PDE zonder $\mu$ geeft, en de oplossing is de verdisconteerde verwachte
payoff onder de risiconeutrale kansen. Wie met een verkeerde volatiliteit verkoopt
en hedget, wint of verliest het variantieverschil gewogen met gamma; discreet
hedgen laat een spreiding die als $1/\sqrt{N}$ daalt, terwijl de drift vrijwel geen
spoor nalaat. Op SPY-opties is de implied volatility niet constant maar hoger bij
lage uitoefenprijzen, het sterkst bij korte looptijden. De VIX ligt gemiddeld vier
punten boven de daarna gerealiseerde volatiliteit, een premie die in enkele jaren
scherp te meten is, anders dan de aandelenpremie.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-02_09_black_scholes.md` §F6-1 en de lecture.

STATUS 02_09_black_scholes F6c words=5239 prose=PASS open=0 cijfer=8,7 min=8

| punt | status | vindplaats |
|---|---|---|
| Verbetering 1: $\mathbb{Q}$ terug naar L6, $d$ bij de afwijkingen | opgelost | "Het is de maat $Q$ uit [](#thm-efficiente-markten-martingaal)"; Opzet: "Ook $d$ is in de boom de daalfactor, niet het dividend; een dividend heet hier $\delta$" |
| Verbetering 2: getal uit de bron, getallen uit de VRP-alinea | deels | het VRP-oordeel noemt alleen de verwachtingen; een kolom "origineel" is met reden afgewezen (geen herleidbaar brongetal), dus beide replicaties blijven zonder origineel |
| Verbetering 3: toy | opgelost | knooptabel met alle koersen vóór de stappen |
| Naadpunt 4 ($m$ als markt) | opgelost | note: "$\beta_{C,\text{mkt}}$ ... (de letter $m$ is in de reeks de SDF)" |
| Naadpunt 7 ($Q$ dubbel) | opgelost | zie verbetering 1 |
| Naadpunt 8 ($d$) | opgelost | zie verbetering 1 |
| Naadpunt 11 (Merton-chronologie) | opgelost | "Merton had dezelfde wiskunde in continue tijd al vanaf 1969 gebruikt ... In 1973 leidde hij er het evenwicht van de hele markt mee af" |

Geen verslechteringen en geen nieuwe feitelijke fouten; de code is ongewijzigd.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8,5 | 9 |
| 2 | Opbouw | 8,5 | 8,5 |
| 3 | Taal | 8,5 | 8,5 |
| 4 | Toy | 8,5 | 9 |
| 5 | Code en figuren | 8,5 | 8,5 |
| 6 | Replicatie | 8 | 8 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,70 + 1,70 + 1,275 + 0,90 + 0,85 + 0,80 + 0,45 = 8,675. **Eindcijfer 8,7,
laagste deelcijfer 8.** Replicatie blijft 8: zonder brongetal is er geen tabel
origineel/hier, hoe goed de reden ook is.
