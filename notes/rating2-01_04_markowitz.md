# Beoordeling: 01_04_markowitz (Markowitz, Roy en Tobin)

Maatstaf: `plannen/rubriek-didactiek.md`. Gelezen als eerstejaars PhD-student die
de eerdere lectures heeft gelezen maar niet paraat heeft. Kalibratie gelijk aan
`rating2-00_01_rendementen.md` en `rating2-01_02_bachelier.md`: hetzelfde gebrek
krijgt dezelfde aftrek.

## 1. Eindcijfer: 7,9

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 7 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 7 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 8 |
| | **gewogen** | | **7,85 → 7,9** |

Geen deelcijfer onder 5 op criterium 1 of 2, dus geen plafond.

## 2. Per criterium

### 1. Helderheid van de uitleg (8)

**Goed**
- *Het kernresultaat: de efficiënte rand*: elke tussenstap krijgt een
  toy-getal ($A = 128{,}125$, $D = 15{,}625$ tegen $AC = 65{,}5$, $\lambda = 0{,}368$,
  $\delta = -0{,}0125$, variantie 0,0243, $\sigma = 15{,}6\%$ tegen 20% voor A
  alleen). Alle getallen kloppen bij narekenen.
- *Een risicovrij activum: Tobin en Roy*: de tangentportefeuille met de hand
  ($1/3$, $2/9$, $4/9$; $S_{\max} = 0{,}529$), en Roys grens met een getal (2,4
  standaarddeviaties, grens 17% tegen 0,8% onder normaliteit).
- *Overzicht* en *Hoe het toegepast wordt*: de standaardfout van 2% uit L1 wordt
  in één regel herhaald ($20/\sqrt{100} = 2$ procentpunt), net als de stelling van
  Merton. Zo hoort een geleend resultaat terug te komen.

**Aanmerkingen**
- *Het kernresultaat*: "$A = \mathbf{1}'\boldsymbol{\Sigma}^{-1}\mathbf{1},\quad
  B = \mathbf{1}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu},\quad
  C = \boldsymbol{\mu}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}$". In het toy
  heten de activa A, B en C. Zinnen als "Activum B heeft het hoogste verwachte
  rendement" en "In het toy-voorbeeld is $A = 128{,}125$" staan een paar alinea's
  uit elkaar; de lezer moet steeds nagaan of een activum of een scalar bedoeld is.
- *Hoe het toegepast wordt*, punt 2: "$\boldsymbol{\Sigma}^{-1}$ is groot in de
  richtingen waarin activa sterk gecorreleerd zijn." Geen getal en geen
  exemplaar, terwijl het toy er een heeft (de $-6{,}25$ bij A en B).
- *Wat het voorspelt: alleen covariantie wordt beloond*: "De helft van het
  risico is weg te diversifiëren, de andere helft niet." Klopt in
  standaarddeviatie (19,0% naar 9,5%), niet in variantie (75% weg). De maat wordt
  niet genoemd.
- *Opzet en aannames*: "Er zijn $N$ risicovolle activa met netto rendementen
  $\mathbf{R}_{t+1}$". In [](#00-01-rendementen) was $R$ het *bruto* rendement.
  De lecture bespreekt bruto tegen netto, maar zegt niet dat de letter van
  betekenis wisselt.
- Figuurbijschrift *fig-markowitz-simulatie*: "De afstand is geen pech maar bias:
  de schatter maximaliseert mee over zijn eigen fout." Onduidelijk wat
  "maximaliseert mee over" betekent; de tekst erna (elk extra activum is een
  extra kans op een toevallig hoog gemiddelde) is helderder.

**Beter uitleggen**
- De bias $\E[\hat{S}^2_{\max}] \approx S^2_{\max} + N/T$: waar de $N/T$ vandaan
  komt. Eén zin (elk geschat gemiddelde draagt ruis met variantie $1/T$ in
  Sharpe-eenheden, en de optimalisator telt $N$ van die kwadraten op) zou de formule
  van een bewering tot een gevolg maken.
- Waarom de minimum-variantieportefeuille in de replicatie "wint" terwijl het
  verschil met 1/N (0,165 tegen 0,158) een vijfde van de standaardfout is: één
  zin dat het teken, niet de grootte, het resultaat is.

### 2. Opbouw en rode draad (8)

**Goed**
- *Intuïtie*: twee voorspellingen, allebei expliciet ingelost ("Zo lost de
  theorie de eerste voorspelling van de intuïtie in", "Zo lost de theorie de
  tweede voorspelling van de intuïtie in").
- Het toy draagt de hele lecture: dezelfde drie activa voor de rand, de
  tangentportefeuille, Roys voorbeeld, de figuur, de instapoefening en de
  zero-beta-oefening; de replicatie grijpt terug op de 8,83%.
- Theoriesubsecties openen met "De bewering:", dus met hun conclusie. De
  simulatie is een "karikatuur van de tien industrieportefeuilles uit de
  replicatie", zodat simulatie en replicatie op elkaar aansluiten.

**Aanmerkingen**
- *Theorie*: het blok "Samengevat" staat aan het eind van de theorie, niet aan
  het eind van de lecture. Zelfde aftrek als in L1 en L2.
- *Intuïtie*: de sectie bevat naast de intuïtie ook Markowitz in de
  bibliotheek, de Friedman-note, Roys oorlogsverleden en Tobin. "Roy had in de
  oorlog gediend en schreef, naar eigen zeggen, voor mensen voor wie een slechte
  uitkomst het einde is." Geschiedenis en intuïtie lopen door elkaar, waardoor de
  twee voorspellingen pas na zeventig regels komen.
- *Overzicht*: de kernboodschap van de tweede helft (schattingsfout in
  $\boldsymbol{\mu}$ maakt de theorie in de praktijk onbruikbaar) staat alleen
  in de laatste routepunt en in één bijzin ("daar slaat de standaardfout van 2%
  hard toe"). Het antwoord op de openingsvraag noemt haar niet.

**Beter uitleggen**
- Waarom de lecture van Markowitz (keuze) naar de CRSP-tape (meting) gaat:
  *Wat er daarna kwam* noemt de overgang, maar het Overzicht niet.

### 3. Taal (7)

**Goed**
- *Intuïtie*: "Honderd aandelen van banken die op elkaar lijken, zijn niet
  gespreid. Drie activa die niets met elkaar te maken hebben, zijn dat wel."
  Kort en idiomatisch.
- Friedmans Engelse citaat staat als blokcitaat met inleiding en parafrase.
- Vaktermen krijgen bij de eerste keer een Nederlandse omschrijving
  (*efficient frontier*, *idiosyncratisch risico*, kapitaalmarktlijn).

**Aanmerkingen**
- Projectjargon, nu als slogan: "Die verhoudingen zijn de standaardfout van 2%,
  vertaald naar portefeuillekeuze" en "is de standaardfout van 2% in zijn
  zuiverste vorm". Zelfde aftrek als in L1 en L2 (bedoeld: twee procentpunt).
- Anglicismen zonder noodzaak: "Short gaan mag", "bruto exposure", "turnover
  (omzet)", "een impliciete prior op $\boldsymbol{\mu}$", oefeningtitel "De
  replicatie uitbreiden: shrinkage", "safety first", "risk parity". Elk apart
  toegelicht, maar samen een Engels register.
- *Het kernresultaat*: "De rest van de subsectie gaat van de
  eerste-ordevoorwaarde naar de kern." Metatekst die niets toevoegt.
- *Opzet en aannames*: "Risico betekent hier standaarddeviatie; volatiliteit is
  hetzelfde woord voor hetzelfde getal." Twee namen voor één begrip, bewust
  ingevoerd; de lecture gebruikt daarna beide.

**Beter uitleggen**
- Geen; de taal hindert het begrip nergens ernstig.

### 4. Toy-voorbeeld (9)

**Goed**
- *Toy-voorbeeld*: drie activa, een $2\times2$-inverse met uitgelegde regel, en
  breuken ($7/41$, $2/41$, $32/41$) die de lezer exact kan narekenen, binnen vijf
  minuten.
- Eén mechanisme, expliciet aangekondigd ("een mengsel van riskante activa kan
  veiliger zijn dan het veiligste activum"), één recept dat de theorie als eerste
  afleidt, tabel hand/code en een slotzin met wat de lezer nu weet.
- Stap 5 (alle covarianties met de portefeuille zijn gelijk) laat al zien wat de
  eerste-ordevoorwaarde later algemeen zegt.

**Aanmerkingen**
- *Toy-voorbeeld*, stap 2: "Buiten de diagonaal staat een *negatief* getal waar
  de covariantie positief is. Daar zit de hele theorie in". Een sterke bewering
  die het toy zelf niet laat zien: de gewichten van de minimum-variantie- en de
  tangentportefeuille zijn allemaal positief, dus de lezer ziet nergens twee
  activa "tegen elkaar in" gezet. Dat gebeurt pas in de replicatie (2100% long
  en short).

**Beter uitleggen**
- Geen verdere; het toy is op QuantEcon-niveau.

### 5. Code en figuren (7)

**Goed**
- Toy- en theoriecellen volgen de wiskunde regel voor regel, met labels in het
  commentaar (`# stap 3`, `# eq-markowitz-frontier`, `# eq-markowitz-tangent`).
- `rolling_oos`: de rollende schatting als zichtbare lus met
  `past = values[t - window:t]  # alleen maanden vóór t`; het vooruitkijkende
  karakter is in de code te zien.
- Elke figuur heeft een leeswijzer vooraf ("Let op de afstand tussen de twee
  verdelingen en op de ligging van de zwarte lijn") en een bijschrift achteraf.

**Aanmerkingen**
- *Simulatie*: `np.einsum("sti,stj->sij", demeaned, demeaned) / (T - 1)`,
  `np.linalg.solve(Sigma_hat, mu_hat[..., None])[..., 0]` en
  `np.einsum("ij,jk,ik->i", w, Sigma_true, w)`. Compacte trucs, al staat er
  commentaar bij; dezelfde einsum-regel staat drie keer in de lecture.
- Engelse docstrings: `"""Annualised out-of-sample Sharpe ratio under the TRUE
  moments."""`, `"""Fully invested maximum-Sharpe weights; rows are independent
  samples."""` enz. Zelfde aftrek als in L1 en L2.
- *Replicatie*: `oos_industry.tail(3).round(4)`, met erna "De laatste drie
  maanden zijn alleen een controle dat de drie reeksen gevuld zijn." Een cel
  zonder didactische functie.
- *Replicatie*, positiecel: de lus van `rolling_oos` wordt opnieuw geschreven om
  de gewichten te bewaren. Dubbele code die uit elkaar kan gaan lopen.
- `sharpe_table`: `.assign(**{"Sharpe-ratio mean-variance in de steekproef": ...})`.
  Truc die een scalar als kolom herhaalt.

**Beter uitleggen**
- Waarom `oos_sharpe` onder de *ware* momenten rekent: één zin vóór de cel
  ("we kennen de ware wereld, dus we kunnen exact meten wat de gewichten
  opleveren") zou het verschil met een steekproef-Sharpe vastleggen.

### 6. Replicatie en empirie (8)

**Goed**
- *Replicatie*-blok: bron, wat, data, verschil en verwachte afwijking, met een
  kwantitatieve reden waarom alleen teken en ordening informatief zijn
  (SE $\approx 0{,}04$ bij 637 maanden).
- Tabel origineel/hier met elk origineel naast zijn tegenhanger en een
  afgeleide kolom (gat in minus buiten). Oordeel begint met **Geslaagd.** en
  verwijst naar de voorspelde ordening.
- Het voorbehoud staat er eerlijk bij: "geen van de afzonderlijke verschillen
  ... groter dan twee standaardfouten".

**Aanmerkingen**
- *Replicatie*, vergelijkingscel: `# minimum-variantie van DGU is hier niet
  overgenomen`. Het blok voorspelt "minimum-variantie minstens zo goed als 1/N",
  maar de tabel laat de originele waarden leeg, zodat die voorspelling niet
  tegen DGU te toetsen is.
- *Replicatie*: "Buiten de steekproef blijft ons niveau positief, waar dat van
  DGU bij twee van de drie datasets negatief wordt. Het replicatieblok liet het
  niveau open, en een verklaring hebben we niet". De verwachte afwijking is zo
  ruim geformuleerd dat een tekenwissel in het niveau haar niet raakt.
- Getallen in lopende tekst: "14,5% per maand tegen 4,3%", "0,165 bij de
  industrieën en 0,239", "ruim 2100% long", "7,5 maal", "72 maal", "meer dan
  honderdduizend procent". Deels niet in een tabel met die eenheid.

**Beter uitleggen**
- Waarom S&P-sectoren (N = 11) de tegenhanger van tien French-industrieën zijn:
  één zin over wat DGU's dataset precies is.

### 7. Oefeningen (8)

**Goed**
- Instap is het toy met correlatie nul, met de hand en in code, en een les die
  het mechanisme versterkt.
- Ex-markowitz-1 is een mooie afleiding (covariantie op de rand, zero-beta) met
  een uitkomst die precies 2% blijkt en een verwijzing naar Black (1972).
- Ex-markowitz-3 breidt de replicatie uit (shrinkage) en laat zien dat $\phi = 0$
  de minimum-variantieportefeuille is. Elke uitwerking eindigt met "Wat dit
  leert".

**Aanmerkingen**
- Uitwerking ex-markowitz-2: "Het rooster is te grof om de laatste twee te
  scheiden, en met tweehonderd herhalingen is de mediaan zelf ook nog onrustig."
  De vergelijking met DGU in (2) rust daarmee op een getal waarvan de uitwerking
  zelf zegt dat het onbetrouwbaar is.
- Uitwerking ex-markowitz-3: "Bij $\phi = 0{,}5$ is de Sharpe-ratio vrijwel nul
  en de brutopositie ruim honderd". De oefening vraagt "Bij welke $\phi$ is het
  resultaat het beste", maar het tussengebied blijkt slecht gedefinieerd; de
  vraag had dat moeten voorkomen (doelvolatiliteit in de opgave).

**Beter uitleggen**
- Ex-markowitz-2 (3): de gevraagde "één zin" staat er, maar de uitwerking
  gebruikt drie alinea's; de kernzin (bias schaalt met $N/T$) kan vooraan.

## 3. De drie verbeteringen met het meeste effect

1. **Helderheid (8 → 9):** de scalars $A, B, C, D$ hernoemen zodat ze niet met
   de activa A, B, C botsen, bij punt 2 van *Hoe het toegepast wordt* het
   toy-getal $-6{,}25$ als exemplaar gebruiken, en zeggen in welke maat "de helft
   van het risico" bedoeld is. Eindcijfer +0,3.
2. **Opbouw (8 → 9):** een Samengevat aan het eind van de lecture, de
   geschiedenis uit de Intuïtie naar het Overzicht of een note verplaatsen, en de
   schattingsfout in het antwoord van het Overzicht opnemen. Eindcijfer +0,2.
3. **Taal (7 → 8):** "standaardfout van 2%" als slogan vervangen door twee
   procentpunt, en de anglicismen terugbrengen (short gaan → short verkopen of
   negatieve gewichten, turnover → omzet, exposure → brutopositie, prior →
   voorafgaande overtuiging, shrinkage → krimpen). Eindcijfer +0,15.

## 4. Navertelling in vijf zinnen

Markowitz (1952) liet zien dat het risico van een activum zijn covariantie met de
portefeuille is, zodat een mengsel veiliger kan zijn dan het veiligste activum en
alle efficiënte portefeuilles op één rand liggen die uit twee fondsen is op te
bouwen. Tobin voegde een risicovrij activum toe, waardoor iedereen dezelfde
tangentportefeuille houdt en alleen de dosis verschilt; Roy kwam via een
veiligheid-eerst-criterium bij dezelfde portefeuille uit. In een grote
portefeuille verdwijnt het eigen risico en blijft alleen de gemiddelde
covariantie over, zodat alleen covariantie beloond hoeft te worden. In de
praktijk moet $\boldsymbol{\mu}$ geschat worden, en die fout is zo groot en
wordt door $\boldsymbol{\Sigma}^{-1}$ zo versterkt dat de geschatte optimale
portefeuille buiten de steekproef slechter presteert dan 1/N, zoals simulatie en
replicatie van DeMiguel, Garlappi en Uppal laten zien. De
minimum-variantieportefeuille, die $\boldsymbol{\mu}$ niet gebruikt, doet het
daarom het best.

Dit komt overeen met het Overzicht, met één verschuiving: het Overzicht legt
het zwaartepunt bij de theorie, terwijl de lecture na lezing vooral beweert dat
de invoer de theorie in de praktijk onbruikbaar maakt.
