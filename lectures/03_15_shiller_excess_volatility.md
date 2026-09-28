---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(03-15-shiller-excess-volatility)=

# Shiller en LeRoy-Porter: excess volatility

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1981–1988.

**Wat we al weten.** In [](#01-03-williams-ddm) werd de prijs van een aandeel de
contante waarde van de verwachte dividenden. Bij een constante discontovoet
beweegt de prijs dan alleen als er nieuws over dividenden komt. In
[](#03-14-roll) bleek dat een theorie over prijzen pas iets zegt als vaststaat
tegen welke maatstaf ze getoetst wordt. Voor de contante waarde ligt die
maatstaf voor de hand: de dividenden die later werkelijk kwamen.

**Welke vraag staat open.** Bewegen aandelenprijzen meer dan de latere
dividenden kunnen rechtvaardigen?
```

## Overzicht

Bewegen aandelenprijzen meer dan de latere dividenden kunnen rechtvaardigen?
Volgens Shiller wel, met een factor vijf tot dertien: een rationele prijs is een
voorspelling en beweegt hoogstens zo veel als wat ze voorspelt. Die factor hangt
sterk af van keuzes die de stelling niet voorschrijft. Wat overblijft, is een
kleinere overschrijding die hetzelfde feit is als voorspelbare rendementen. In
deze lecture:

- rekenen we met drie dividenden na dat een rationele prijs over alle mogelijke
  toestanden minder varieert dan de ex-post rationele prijs, en dat die volgorde
  langs één pad kan omdraaien,

- bewijzen we de variantiegrens en lezen we Shillers tabel,

- behandelen we drie kritieken: kleine steekproeven {cite}`Flavin1983`,
  niet-stationaire dividenden {cite}`Kleidon1986,MarshMerton1986`, en het
  antwoord in logs {cite}`CampbellShiller1988,West1988`,

- simuleren we hoe vaak Shillers toets alarm slaat in economieën met exact
  rationele prijzen,

- repliceren we Shillers figuur 1 en zijn variantieratio op `hap.data.shiller()`,
  en meten we hoe sterk die ratio van zulke keuzes afhangt.

In juni 1981 publiceerde Robert Shiller in de *American Economic Review* een
artikel met een vraag als titel: *Do Stock Prices Move Too Much to be Justified
by Subsequent Changes in Dividends?* {cite}`Shiller1981`. Een maand eerder had
Econometrica het artikel van Stephen LeRoy en Richard Porter geplaatst, dat
onafhankelijk hetzelfde idee uitwerkte {cite}`LeRoyPorter1981`. In Shillers
tabel 2 bewoog de reële S&P-koers over 1871–1979 5,6 keer zo veel als het model
toestaat, de Dow Jones over 1928–1979 13,3 keer. Dit werk bepaalde het tijdvak,
omdat het de discussie over efficiënte markten verlegde. Die ging tot dan over
voorspelbare rendementen op korte termijn, waar de data weinig tegen de theorie
inbrachten. Shiller keek naar het niveau van prijzen, waar de afwijking groot en
zichtbaar was.

Bij elk model vragen we *theorie of feit*: is dit een theorie die getoetst wordt,
of een feit dat op een verklaring wacht? Het contante-waardemodel van Williams,
met een constante discontovoet, was een theorie die getoetst werd. Na Shiller is
*excess volatility* (overmatige beweeglijkheid: koersen die meer bewegen dan hun
fundamentele waarde) een feit met twee concurrerende verklaringen. Ofwel bewegen
de discontovoeten, ofwel reageren prijzen te sterk.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een weersvoorspeller. Elke ochtend noemt hij de temperatuur van
vanmiddag, en achteraf leggen we zijn voorspellingen naast de metingen. Werkt hij
goed, dan zijn zijn fouten onvoorspelbaar: uit zijn eigen getal valt niet af te
leiden of hij te hoog of te laag zit. De gemeten temperatuur is dan de
voorspelling plus een fout die er los van staat. Twee losstaande bronnen van
variatie tellen op, dus de metingen schommelen minstens zo veel als de
voorspellingen.

Shiller paste dat toe op de beurs. Onder het model van Williams is de koers van
vandaag de beste voorspelling van één getal: de contante waarde van alle
dividenden die het aandeel daarna werkelijk uitkeert. Dat getal kennen we pas
achteraf, maar met een eeuw data is het voor elk jaar bij benadering uit te
rekenen. Shiller noemde het de *ex-post rationele prijs* (de prijs die een
belegger met volledige kennis van de toekomstige dividenden had betaald). Zijn
koersen goede voorspellingen daarvan, dan bewegen ze niet meer dan de ex-post
rationele prijs.

Zijn figuur maakte meer indruk dan de ongelijkheid. De koers schiet op en neer,
de ex-post rationele prijs loopt als een rustige lijn door het midden. Dividenden
schommelen weinig rond hun groeipad, en een contante waarde middelt die
schommelingen uit over decennia. De crash van 1929–1932 is in de ex-post
rationele prijs nauwelijks te zien, want de dividenden lagen in de jaren dertig
maar enkele jaren onder hun trend. Volgens Shiller was de daling vanaf 1929 niet
te verklaren uit latere dividenden.

Toch zit er een addertje onder het gras, en dat vulde de jaren tachtig. De
ongelijkheid gaat over de spreiding over alle toestanden die hadden kunnen
gebeuren. Gemeten wordt de spreiding langs de tijd, over het ene pad dat wel
gebeurde. Die twee zijn alleen gelijk als de wereld *stationair* is: een eeuw uit
één pad lijkt dan op honderd trekkingen uit dezelfde verdeling. Volgen dividenden
een *random walk* (elk jaar een blijvende schok), dan kan een volkomen rationele
koers langs de tijd wilder bewegen dan de ex-post rationele prijs.

Wat verwachten we dus?

- Over toestanden varieert een rationele prijs hoogstens zo veel als de ex-post
  rationele prijs. Meer informatie maakt de prijs beweeglijker, maar nooit boven
  dat plafond.

- Langs de tijd kan een rationele prijs meer bewegen, vooral als dividenden
  blijvende schokken krijgen.

- Beweegt de koers toch te veel, dan beweegt de discontovoet of reageert de koers
  te sterk. Een prijs-dividend-ratio die te veel beweegt, voorspelt dan latere
  rendementen.

## Toy-voorbeeld: drie dividenden en twee informatiestructuren

De eerste cel laadt de bibliotheken en zet een vaste toevalsgenerator voor de
simulatie.

```{code-cell} ipython3
import itertools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

Een aandeel keert op $t = 1, 2, 3$ een dividend uit en is daarna niets meer
waard. De opzet:

| grootheid | waarde |
|---|---|
| dividenden $d_1, d_2, d_3$ | onafhankelijk $5$ of $15$, elk met kans $\tfrac12$: verwachting $10$, variantie $25$ |
| discontovoet $r$ | $25\%$: een euro één periode later is $1/1{,}25 = 0{,}8$ waard |
| gerealiseerd pad | $(d_1, d_2, d_3) = (15, 5, 15)$ |
| informatie A | niemand weet iets vooruit |
| informatie B | het volgende dividend is één periode vooruit bekend |

Het recept: de ex-post rationele prijs $p^*_t$ is de contante waarde van de
dividenden die werkelijk kwamen. Achterwaarts is dat
$p^*_t = 0{,}8\,(d_{t+1} + p^*_{t+1})$, met $p^*_3 = 0$. De stappen:

1. **$p^*$ langs het pad.** $p^*_2 = 0{,}8 \times 15 = 12$,
   $p^*_1 = 0{,}8 \times (5 + 12) = 13{,}6$ en
   $p^*_0 = 0{,}8 \times (15 + 13{,}6) = 22{,}88$.

2. **Prijs onder A.** Elk dividend is $10$ in verwachting, dus
   $p_0 = 8 + 6{,}4 + 5{,}12 = 19{,}52$ in elke toestand, en $\Var(p^A_0) = 0$.

3. **Prijs onder B.** $p_0 = 0{,}8\,d_1 + 0{,}64 \times 10 + 0{,}512 \times 10
   = 0{,}8\,d_1 + 11{,}52$, dus $\Var(p^B_0) = 0{,}64 \times 25 = 16$.

4. **$p^*$ over de acht toestanden.** $p^*_0 = 0{,}8\,d_1 + 0{,}64\,d_2 + 0{,}512\,d_3$,
   dus $\Var(p^*_0) = 25 \times (0{,}64 + 0{,}4096 + 0{,}262144) = 32{,}7936$.

5. **Voorspelfout onder B.** $u_0 = p^*_0 - p^B_0 = 0{,}64\,(d_2 - 10) + 0{,}512\,(d_3 - 10)$
   hangt niet af van $d_1$ en dus niet samen met $p^B_0$. Haar variantie is
   $16{,}7936$, en $16 + 16{,}7936 = 32{,}7936$.

6. **Langs de tijd.** Op het pad is $p^* = (22{,}88;\ 13{,}6;\ 12)$ met variantie
   $23{,}01$, en prijs B $= (23{,}52;\ 10{,}4;\ 12)$ met variantie $34{,}16$.

De cel hieronder rekent de zes stappen na, met de acht even waarschijnlijke paden
als toestanden.

```{code-cell} ipython3
discount = 0.8                                     # 1 / (1 + 0.25)
weights = discount ** np.arange(1, 4)              # 0.8, 0.64, 0.512
states = np.array(list(itertools.product([5.0, 15.0], repeat=3)))   # 8 equally likely paths

path = np.array([15.0, 5.0, 15.0])                               # step 1, backward
pstar_2 = discount * path[2]
pstar_1 = discount * (path[1] + pstar_2)
pstar_path = np.array([discount * (path[0] + pstar_1), pstar_1, pstar_2])
price_A = np.full(8, 10.0 * weights.sum())                       # step 2
price_B = discount * states[:, 0] + 10.0 * weights[1:].sum()     # step 3
pstar_0 = states @ weights                                       # step 4
error_B = pstar_0 - price_B                                      # step 5
cov_B = np.mean((price_B - price_B.mean()) * error_B)
price_B_path = discount * path + 10.0 * np.array([0.64 + 0.512, 0.64, 0.0])   # step 6

pd.DataFrame(
    {
        "met de hand": [22.88, 13.6, 12.0, 0.0, 16.0, 32.79, 16.79, 0.0, 23.01, 34.16],
        "code": [*pstar_path, price_A.var(), price_B.var(), pstar_0.var(),
                 error_B.var(), cov_B, pstar_path.var(), price_B_path.var()],
    },
    index=["p*_0 langs het pad", "p*_1 langs het pad", "p*_2 langs het pad",
           "Var(p_0) onder A", "Var(p_0) onder B", "Var(p*_0)",
           "Var(u_0) onder B", "Cov(p_0, u_0) onder B",
           "Var langs de tijd, p*", "Var langs de tijd, B"],
).round(2)
```

Code en hand geven dezelfde getallen, ook de covariantie van nul tussen prijs en
voorspelfout. Wat we nu weten: over toestanden geldt $0 \le 16 \le 32{,}79$, dus
meer informatie maakt de prijs beweeglijker maar nooit beweeglijker dan $p^*$.
Langs het ene pad is prijs B wél beweeglijker dan $p^*$, zonder dat er iets fout
is.

## Theorie

We leiden eerst de variantiegrens af: een rationele prijs is een voorspelling van
$p^*$ en varieert daarom minder. Daarna lezen we wat Shiller mat, en welke keuze
de berekening van $p^*$ vraagt. Dan volgen de drie kritieken: kleine
steekproeven, niet-stationaire dividenden, en het antwoord in logs. De kern: de
grens gaat over toestanden, de meting over de tijd.

### Opzet: de ex-post rationele prijs

De rationele prijs is de verwachting van de ex-post rationele prijs. De notatie
is die van [](#00-00-setup): $p_t$ is de reële prijs ex dividend op $t$ en
$d_{t+1}$ het dividend tussen $t$ en $t+1$, beide niveaus. De discontovoet $r$
is constant, en $\delta = 1/(1+r)$ is de constante discontofactor: $0{,}8$ in het
toy-voorbeeld, $0{,}954$ bij Shillers $4{,}8\%$. Shiller schrijft hoofdletters en
$\gamma$ voor $\delta$; in deze reeks is $\gamma$ de risicoaversie. Onder de
*transversaliteitsvoorwaarde* (de verdisconteerde prijs in de verre toekomst gaat
naar nul: bij $\delta = 0{,}954$ weegt een prijs over honderd jaar nog minder dan
1% mee) geldt, zoals in [](#01-03-williams-ddm),

```{math}
:label: eq-shiller-excess-volatility-ddm
p_t = \E_t\!\left[\sum_{j=1}^{\infty} \delta^{j} d_{t+j}\right] .
```

In woorden: de prijs is de verwachte som van alle toekomstige dividenden, elk
verdisconteerd met $\delta$ per jaar. Laat de verwachting weg, en er ontstaat de
ex-post rationele prijs (bij Shiller de *perfect-foresight price*):

```{math}
:label: eq-shiller-excess-volatility-pstar
p^*_t = \sum_{j=1}^{\infty} \delta^{j} d_{t+j}
\qquad\Longleftrightarrow\qquad
p^*_t = \delta\,\bigl(d_{t+1} + p^*_{t+1}\bigr).
```

Links staat de som van wat werkelijk kwam, rechts dezelfde som achterwaarts, zoals
in stap 1 van het toy-voorbeeld. Samen zeggen
[](#eq-shiller-excess-volatility-ddm) en [](#eq-shiller-excess-volatility-pstar)
dat $p_t = \E_t[p^*_t]$: de prijs is de beste voorspelling van $p^*_t$ met de
informatie van $t$.

### De variantiegrens

Een rationele prijs varieert hoogstens zo veel als $p^*$, en het verschil is de
variantie van de voorspelfout.

*Waarom zou dit waar zijn?* Stel dat de fout $p^*_t - p_t$ positief samenhangt
met de prijs: hoge prijzen blijken achteraf nog te laag. Een belegger die dat
ziet, koopt als de prijs hoog is, en drijft hem op tot de samenhang weg is. In
evenwicht staat de fout dus los van de prijs. Een losstaande fout voegt variantie
toe aan de uitkomst en kan er niets van afhalen, dus $p^*$ varieert meer dan $p$.

:::{prf:theorem} Variantiegrens (Shiller; LeRoy-Porter)
:label: thm-shiller-excess-volatility-bound

Laat $\mathcal I_t$ de informatie van de markt op $t$ zijn,
$p_t = \E[p^*_t \mid \mathcal I_t]$ en $\E[(p^*_t)^2] < \infty$. Dan is

```{math}
:label: eq-shiller-excess-volatility-bound
\Var(p^*_t) = \Var(p_t) + \Var(p^*_t - p_t) \;\ge\; \Var(p_t).
```
:::

Het bewijs gebruikt alleen dat de voorspelfout $u_t = p^*_t - p_t$ gemiddeld nul
is gegeven $\mathcal I_t$. Daardoor is haar covariantie met alles wat op $t$
bekend is nul, ook met $p_t$, en tellen de varianties op.

:::{prf:proof}
:class: dropdown

Omdat $p_t$ bekend is op $t$ en $\E[u_t \mid \mathcal I_t] = \E[p^*_t\mid\mathcal
I_t] - p_t = 0$, geeft de wet van iteratieve verwachtingen

$$
\Cov(p_t, u_t) = \E\bigl[(p_t - \E p_t)\,\E[u_t \mid \mathcal I_t]\bigr] = 0 .
$$

Dus $\Var(p^*_t) = \Var(p_t + u_t) = \Var(p_t) + \Var(u_t) \ge \Var(p_t)$. $\square$
:::

In woorden: wat de dividenden achteraf waard bleken, varieert zo veel als de prijs
plus de voorspelfout. In het toy-voorbeeld is dat $32{,}79 = 16 + 16{,}79$.
Hetzelfde argument geeft de ondergrens van LeRoy en Porter. Een voorspelling met
minder informatie, bijvoorbeeld alleen de dividendhistorie, varieert minder dan
de marktprijs. In het toy-voorbeeld is A de kleinste informatieverzameling en B de
grotere: $0 \le 16 \le 32{,}79$. Zoals de intuïtie voorspelde, maakt meer
informatie de prijs beweeglijker, maar nooit boven $p^*$.

De stelling gaat over de variantie over toestanden op één datum $t$. Shiller mat
de variantie langs de tijd. Die twee vallen samen als de reeksen stationair zijn:
dan hangen de momenten niet van $t$ af, en schat het tijdgemiddelde het gemiddelde
over toestanden. Onder die aanname luidt de grens $\sigma(p) \le \sigma(p^*)$.

### Wat Shiller mat

Shiller vond op de S&P een koers die ruim vijf keer zo veel beweegt als $p^*$, en
op de Dow dertien keer. Omdat koersen en dividenden over een eeuw exponentieel
groeien, detrendeerde hij beide eerst. Hij regresseerde $\ln p_t$ op een
constante en de tijd, met helling $b$, en deelde koers en dividend door
$e^{b(t-T)}$, met $T = 1979$ als basisjaar. Voor de gedetrendeerde reeksen is de
passende discontovoet $\bar r = \E(d)/\E(p)$. Dat volgt uit
[](#eq-shiller-excess-volatility-ddm) met onvoorwaardelijke verwachtingen, want
$\E(p) = \E(d)\,\delta/(1-\delta) = \E(d)/r$. De statistiek is de verhouding
$\sigma(p)/\sigma(p^*)$ van de gedetrendeerde *niveaus*. In tabel 2 van het artikel
is dat 50,12 gedeeld door 8,968, dus 5,59 voor de S&P over 1871–1979. De
replicatie zet zijn getallen naast de onze.

Shiller gaf ook een grens voor prijs*veranderingen*:
$\sigma(\Delta p) \le \sigma(d)/\sqrt{2\bar r}$. In woorden: hoe beweeglijker het
dividend en hoe lager de discontovoet, hoe meer de koers van jaar op jaar mag
bewegen, maar niet meer dan dat. Die grens is het maximum van $\sigma(\Delta p)$
over alle informatiestructuren bij gegeven $\sigma(d)$. In tabel 2 was ze voor de
S&P ruim vijf keer en voor de Dow ruim zeven keer overschreden.

### Hoe het getoetst wordt: de eindwaarde

Elke meting van $p^*$ hangt af van een gekozen eindwaarde, want de som in
[](#eq-shiller-excess-volatility-pstar) loopt tot oneindig en de data houden op.

*Waarom zou dit waar zijn?* Een onderzoeker die $p^*$ voor 1871 uitrekent, telt
de dividenden tot 1979 op en moet voor de rest iets invullen. Voor 1871 weegt die
rest nauwelijks, want hij ligt ver weg en wordt zwaar verdisconteerd. Voor 1975 is
de rest bijna alles. Hoe dichter bij het eind van de steekproef, hoe meer de keuze
bepaalt. Kiest hij een beweeglijke eindwaarde, dan stijgt de gemeten variantie van
$p^*$, en daalt de ratio.

Met een steekproef tot $T$ is de berekenbare versie

```{math}
:label: eq-shiller-excess-volatility-eindig
p^{*(T)}_t = \sum_{j=1}^{T-t} \delta^{j} d_{t+j} + \delta^{T-t}\, \tilde p_T ,
```

de dividenden tot $T$ plus een eindwaarde $\tilde p_T$, over $T - t$ jaar
verdisconteerd. Shiller nam het steekproefgemiddelde van de gedetrendeerde prijs.
Met $\delta = 0{,}954$ is $\delta^{108} = 0{,}0063$, dus in 1871 weegt die keuze
nauwelijks mee. Er zijn twee alternatieven, elk met een eigen gevolg:

- **De werkelijke eindprijs, $\tilde p_T = p_T$.** Dan geldt de stelling exact in
  eindige horizon, want $p_t = \E_t[p^{*(T)}_t]$ volgt uit dezelfde iteratie als in
  [](#01-03-williams-ddm). De keerzijde: aan het eind van de steekproef erft
  $p^{*(T)}$ de beweeglijkheid van $p_T$, en de gemeten variantie van $p^*$ stijgt.

- **Het gemiddelde of een extrapolatie, $\tilde p_T = \bar p$.** Dan staat de
  voorspelfout niet meer exact los van $p_t$, want $\bar p$ gebruikt de hele
  steekproef. Shiller liet in zijn Nobellezing zien dat die keuze vóór 1980
  nauwelijks doorwerkt {cite}`Shiller2014`.

De replicatie laat zien dat de ratio over 1871–2025 met ruim een derde daalt als
we van de gemiddelde naar de werkelijke eindwaarde overstappen. Het getal 5,59
bevat dus meer dan de ongelijkheid alleen.

### Kritiek 1: kleine steekproeven (Flavin)

In een eindige steekproef valt de gemeten variantie van $p^*$ te laag uit, en
slaat de toets te vaak alarm.

*Waarom zou dit waar zijn?* Wie een steekproefvariantie berekent, meet de
spreiding rond het steekproefgemiddelde. Een reeks die langzaam rond haar
gemiddelde schommelt, trekt dat steekproefgemiddelde met zich mee, en de gemeten
spreiding daalt. Hoe persistenter de reeks, hoe groter de onderschatting. Omdat
$p^*$ een gewogen som over decennia is, is het persistenter dan $p$. De gemeten
$\sigma(p^*)$ zakt dus sterker dan $\sigma(p)$, en de ratio stijgt.

{cite:t}`Flavin1983` liet zien dat toetsen op variantiegrenzen in kleine
steekproeven daardoor vaak sterk naar verwerping vertekend zijn. Na correctie
verdwijnt een groot deel van de excess volatility. Neem een AR(1)-reeks: elke
waarde is $\phi$ maal de vorige plus een schok. Over $T$ waarnemingen is de
verwachte steekproefvariantie dan ongeveer

$$
\E\bigl[\hat\sigma^2\bigr] \approx \Var(x)\Bigl[1 - \frac{1}{T}\,\frac{1+\phi}{1-\phi}\Bigr].
$$

Bij $\phi = 0{,}95$ en $T = 100$ is de correctieterm $39/100$: de variantie valt
39% te laag uit, en $p^*$ is persistenter dan dat. Dit is de standaardfout van 2%
uit [](#00-01-rendementen) in een andere gedaante: een gemiddelde is slecht te
meten, en hier bederft het ook een tweede moment. Een variantie is doorgaans goed
te schatten, maar niet rond het gemiddelde van een zeer persistente reeks.

### Kritiek 2: niet-stationaire dividenden (Kleidon; Marsh en Merton)

Volgen dividenden een random walk, dan beweegt een volkomen rationele prijs langs
de tijd meer dan $p^*$, terwijl de grens over toestanden blijft gelden.

*Waarom zou dit waar zijn?* Bij een random walk verhoogt een dividendschok de
verwachting van alle toekomstige dividenden. Beleggers passen de prijs daarom in
één keer volledig aan. De ex-post rationele prijs bevatte de schok al voordat hij
kwam, want hij is opgebouwd uit de latere dividenden. Hij laat de schok geleidelijk
binnenlopen naarmate die dichterbij komt. Langs de tijd springt de rationele prijs
dus, en glijdt $p^*$.

{cite:t}`Kleidon1986` betoogde daarom dat Shillers figuur geen bewijs is: ook bij
rationele prijzen en een constante discontovoet is $p^*$ gladder. Grenzen die wel
gelden bij niet-stationaire dividenden werden voor de S&P volgens hem niet
geschonden. De volgende propositie maakt het mechanisme exact.

:::{prf:proposition} Rationele prijzen bij random-walk-dividenden
:label: thm-shiller-excess-volatility-kleidon

Laat $d_{t+1} = d_t + \varepsilon_{t+1}$, met $\varepsilon$ onafhankelijk en
gelijk verdeeld, gemiddelde nul en variantie $\sigma^2$, en een constante
discontovoet $r > 0$. Dan verhouden de standaarddeviaties van de jaarlijkse
veranderingen van de rationele prijs en van $p^*$ zich als

```{math}
:label: eq-shiller-excess-volatility-kleidon
\frac{\sigma(\Delta p)}{\sigma(\Delta p^*)} = \sqrt{1 + \frac{2}{r}} \;>\; 1 .
```
:::

Het bewijs splitst $p^*_t$ in de rationele prijs plus een voorspelfout die alleen
uit toekomstige schokken bestaat. Een verandering in $p$ is één schok gedeeld door
$r$. Een verandering in $p^*$ is een verdisconteerde som van latere schokken, en
die is kleiner.

:::{prf:proof}
:class: dropdown

*Stap 1: de prijs.* $\E_t d_{t+j} = d_t$, dus
$p_t = d_t\sum_{j\ge1}\delta^j = d_t\,\delta/(1-\delta) = d_t/r$.

*Stap 2: de voorspelfout bestaat uit toekomstige schokken.* Met
$d_{t+j} - d_t = \sum_{k=1}^{j}\varepsilon_{t+k}$ en verwisselen van de sommen is
$u_t = p^*_t - p_t = \sum_{k\ge1}\varepsilon_{t+k}\,\delta^k/(1-\delta)$.

*Stap 3: de grens over toestanden blijft gelden.* Gegeven de informatie op $0$
heeft $p_t = d_0/r + \sum_{s\le t}\varepsilon_s/r$ variantie $t\sigma^2/r^2$. De
schokken in $u_t$ liggen na $t$, dus
$\Var_0(p^*_t) = \Var_0(p_t) + \Var(u_t) \ge \Var_0(p_t)$.

*Stap 4: de veranderingen.* $\Delta p_{t+1} = \varepsilon_{t+1}/r$. Uit
$p^*_t = \delta(d_{t+1} + p^*_{t+1})$ volgt
$\Delta p^*_{t+1} = r\,p^*_t - d_{t+1} = r\,u_t - \varepsilon_{t+1}$, omdat
$r\,p_t = d_t$. Met $r/(1-\delta) = 1/\delta$ is
$r\,u_t = \sum_{k\ge1}\delta^{k-1}\varepsilon_{t+k}$, dus
$\Delta p^*_{t+1} = \sum_{m\ge1}\delta^m\varepsilon_{t+1+m}$.

*Stap 5: de verhouding.* De varianties zijn $\sigma^2/r^2$ en
$\sigma^2\delta^2/(1-\delta^2)$. Hun quotiënt is
$(1-\delta^2)/(r^2\delta^2) = \bigl((1+r)^2 - 1\bigr)/r^2 = 1 + 2/r$. $\square$
:::

In woorden: hoe lager de discontovoet, hoe sterker de rationele prijs reageert op
een blijvende schok, terwijl $p^*$ die schok over meer jaren uitsmeert. Bij
Shillers $\bar r = 0{,}048$ is de verhouding $\sqrt{1 + 2/0{,}048} = 6{,}5$. Een
volkomen rationele prijs beweegt dan van jaar op jaar zes en een half keer zo veel
als $p^*$. Dat is een verhouding van *veranderingen*, Shillers 5,59 een verhouding
van gedetrendeerde *niveaus*: de orde van grootte is gelijk, de statistiek niet.
Bij een hogere $r$ daalt de
verhouding, maar bij $10\%$ is ze nog $\sqrt{21} = 4{,}6$.

De propositie zegt niet dat Shiller ongelijk heeft. Ze zegt dat zijn statistiek
niets onderscheidt als dividenden een *eenheidswortel* hebben (schokken die
blijvend zijn, zoals bij een random walk). De variantie langs de tijd groeit dan
met de lengte van de steekproef en schat geen vaste grootheid. Shiller nam aan dat
dividenden stationair rond een bekende trend schommelen. Dan geldt de stelling, en
de simulatie laat zien dat de toets dan werkt. Welke van de twee werelden de onze
is, valt met honderd jaar data nauwelijks te beslissen.

{cite:t}`MarshMerton1986` gaven de niet-stationariteit een economische reden:
*dividend smoothing* (managers passen het dividend langzaam aan hun inschatting
van de blijvende winst aan, en verlagen het liever niet). Het dividend wordt dan
een gewogen som van vroegere koersen. Onder zo'n beleid zijn rationele koersen
niet-stationair, en wijst de steekproefversie van Shillers ongelijkheid de
verkeerde kant op. Shiller antwoordde dat de dividendreeks er over een eeuw
stationair rond een trend uitziet. Het debat liep vast op de vraag welk proces een
onderzoeker mag veronderstellen.

### Het antwoord: een grens in logs

Een grens op de log-prijs-dividend-ratio ontloopt de discussie over trends, en wat
die grens overschrijdt, is voorspelbaarheid van rendementen.

*Waarom zou dit waar zijn?* De bezwaren van Kleidon en van Marsh en Merton gaan
over niveaus die groeien. De verhouding van prijs en dividend groeit niet: stijgt
het dividend blijvend en de koers mee, dan blijft de verhouding gelijk. Delen
beide dezelfde trend, dan schommelt de verhouding rond een vast niveau, ook als
elk van beide een random walk volgt. Een onderzoeker die de verhouding gebruikt in
plaats van de niveaus, hoeft dus niets te detrenden.

Vanaf hier zijn kleine letters logs: $p_t$ is de log van de prijs, $d_t$ de log
van het dividend, en $pd_t = p_t - d_t$ de log-prijs-dividend-ratio. Het
logrendement is $\ell_{t+1} = \log R_{t+1}$. Campbell en Shiller
{cite}`CampbellShiller1988` loglineariseerden het rendement: ze benaderden het logrendement door een lineaire
functie van de log-ratio, rond haar gemiddelde $\overline{pd}$. Met
$\rho = e^{\overline{pd}}/(1+e^{\overline{pd}})$, ongeveer $0{,}96$ bij een
gemiddelde prijs-dividend-ratio van 25, en een constante $\kappa$ geeft dat

```{math}
:label: eq-shiller-excess-volatility-cs
pd_t = \kappa + \Delta d_{t+1} - \ell_{t+1} + \rho\, pd_{t+1}
     = \frac{\kappa}{1-\rho} + \sum_{j\ge0}\rho^{j}\bigl(\Delta d_{t+1+j} - \ell_{t+1+j}\bigr).
```

In woorden: een hoge ratio vandaag betekent hoge dividendgroei later, of lage
rendementen later. Dat is een identiteit die achteraf geldt, en dus ook in
verwachting op $t$. Bij constante verwachte rendementen is
$pd_t = \E_t[pd^*_t]$, met de ex-post rationele log-ratio
$pd^*_t = \text{constante} + \sum_{j\ge0}\rho^j\Delta d_{t+1+j}$.
[](#thm-shiller-excess-volatility-bound) geeft dan $\Var(pd) \le \Var(pd^*)$, nu
voor grootheden die stationair kunnen zijn.

Campbell en Shiller {cite}`CampbellShiller1987` werkten dit uit met
vectorautoregressies (VAR's: elke reeks geregresseerd op de vorige waarden van alle
reeksen). Voor aandelen bewoog de werkelijke verhouding van koers en dividend veel
meer dan de verhouding die hun VAR met constante discontovoet voorspelde. West
{cite}`West1988` leidde een grens af die ook geldt als koers en dividend een
eenheidswortel hebben: onverwachte koersveranderingen mogen niet meer variëren dan
het dividendnieuws toelaat. Die grens was duidelijk en significant
geschonden.

Vermenigvuldig de tweede vorm van [](#eq-shiller-excess-volatility-cs) met
$pd_t - \overline{pd}$ en neem verwachtingen. Links ontstaat
$\E[pd_t(pd_t - \overline{pd})] = \Var(pd_t)$. Rechts valt de constante weg, omdat
$\E[pd_t - \overline{pd}] = 0$, en wordt elke som een covariantie met $pd_t$:

```{math}
:label: eq-shiller-excess-volatility-decompositie
\Var(pd_t) = \Cov\!\Bigl(pd_t, \sum_{j\ge0}\rho^j \Delta d_{t+1+j}\Bigr)
           - \Cov\!\Bigl(pd_t, \sum_{j\ge0}\rho^j \ell_{t+1+j}\Bigr).
```

In woorden: alle beweging van de ratio komt terug als voorspelling van latere
dividendgroei, of als voorspelling van latere rendementen met een minteken.
Varieert $pd$ meer dan dividendnieuws kan dragen, dan zit het verschil in de
tweede covariantie. Een ratio die te veel beweegt, voorspelt dus rendementen, zoals
de intuïtie verwachtte. {cite:t}`Cochrane1992` en {cite:t}`Cochrane2011` maakten
daarvan het centrale punt: excess volatility en voorspelbare rendementen zijn één
feit, twee keer gemeten. In [](#04-20-voorspelbaarheid) wordt deze decompositie
geschat.

```{admonition} Samengevat
:class: tip

- Een rationele prijs is een voorspelling van $p^*$ en varieert over toestanden
  minder, [](#eq-shiller-excess-volatility-bound). Meer informatie maakt de prijs
  beweeglijker, tot het plafond $p^*$.

- De meting van $p^*$ vraagt een eindwaarde,
  [](#eq-shiller-excess-volatility-eindig). Die keuze weegt zwaarder naarmate het
  eind van de steekproef nadert.

- In een eindige steekproef valt de gemeten variantie van een persistente $p^*$ te
  laag uit (Flavin): 39% bij $\phi = 0{,}95$ en $T = 100$.

- Bij random-walk-dividenden beweegt een rationele prijs langs de tijd
  $\sqrt{1 + 2/r}$ keer zo veel als $p^*$,
  [](#eq-shiller-excess-volatility-kleidon): 6,5 bij $r = 4{,}8\%$, 4,6 bij
  $r = 10\%$. Een lagere $r$ maakt de factor groter, een hogere kleiner.

- In logs geldt de grens voor de prijs-dividend-ratio, en wat erboven uitsteekt,
  is voorspelbaarheid van rendementen,
  [](#eq-shiller-excess-volatility-decompositie).

- De simulatie hierna vraagt hoe vaak Shillers toets alarm slaat in een economie
  met exact rationele prijzen.
```

## Simulatie: hoe vaak slaat Shillers toets alarm?

Shillers toets werkt als dividenden stationair rond een bekende trend schommelen,
en slaat altijd vals alarm als ze een random walk volgen. We passen zijn
procedure, zoals in 1981, toe op drie kunstmatige economieën waarin de prijs per
constructie de rationele verwachting van $p^*$ is. De discontovoet is 7% op de
gedetrendeerde dividenden (in niveaus $1{,}07 \times 1{,}015 - 1 = 8{,}6\%$), de
steekproef 109 jaar, zo lang als Shillers S&P-reeks. Dat zijn andere getallen dan
de 25% en drie perioden van het toy-voorbeeld, omdat de toets hier op een eeuw
jaardata moet lijken. De vraag over steekproeven:
hoe vaak valt $\sigma(p)/\sigma(p^*)$ boven één, terwijl de prijzen rationeel zijn?

Eerst een hulpfunctie die $p^*$ achterwaarts oplost met het recept van het
toy-voorbeeld, [](#eq-shiller-excess-volatility-pstar), op één pad of op een matrix
van paden tegelijk.

```{code-cell} ipython3
def ex_post_price(div, gross_rate, terminal):
    """Ex-post rational price p*_t = (d_{t+1} + p*_{t+1}) / R_{t+1}, solved backward.

    ``div[..., i]`` is the dividend received at the end of period ``i`` (so it
    belongs to the price at the start of ``i``); ``gross_rate`` broadcasts
    against ``div``; ``terminal`` is p* after the last period.
    """
    div = np.asarray(div, dtype=float)
    rate = np.broadcast_to(np.asarray(gross_rate, dtype=float), div.shape)
    out = np.empty_like(div)
    nxt = np.asarray(terminal, dtype=float)
    for i in range(div.shape[-1] - 1, -1, -1):
        nxt = (div[..., i] + nxt) / rate[..., i]
        out[..., i] = nxt
    return out
```

Met `ex_post_price(path, 1.25, 0.0)` geeft ze de 22,88, 13,6 en 12 uit stap 1. De
tweede functie volgt Shillers stappen: een exponentiële trend op de log-koers,
$\bar r = \bar d/\bar p$, het gemiddelde als eindwaarde, en dan de ratio. Dezelfde
functie gebruiken we straks op de echte data.

```{code-cell} ipython3
def shiller_test(P, D, terminal="mean", detrend="price", rate=None):
    """Shiller (1981) variance-bound statistic, vectorised over rows.

    ``P[:, i]`` is the real price at the start of year ``i``, ``D[:, i]`` the
    real dividend paid during year ``i``.  Both are detrended by an exponential
    trend fitted to log prices (or log dividends), p* is solved backward with
    discount rate mean(d)/mean(p) unless ``rate`` is given, and the terminal
    value is the sample mean of detrended prices (or the last price).
    """
    P, D = np.atleast_2d(P), np.atleast_2d(D)
    n_paths, T = P.shape
    t = np.arange(T) - (T - 1)                 # years relative to the last year
    log_base = np.log(P if detrend == "price" else D)

    b = np.empty(n_paths)                      # OLS slope of the log trend, per path
    for i in range(n_paths):
        b[i] = np.polyfit(t, log_base[i], deg=1)[0]
    trend = np.exp(b)[:, None]
    p = P / trend**t                           # detrended price
    d = D / trend ** (t + 1)                   # detrended dividend

    if rate is None:
        rbar = d.mean(axis=1) / p.mean(axis=1)
    else:
        rbar = np.full(n_paths, rate)
    if terminal == "mean":
        end = p.mean(axis=1)
    else:
        end = p[:, -1]
    pstar = ex_post_price(d, 1 + rbar[:, None], end)

    ratio = p.std(axis=1) / pstar.std(axis=1)
    corr = np.empty(n_paths)
    for i in range(n_paths):
        corr[i] = np.corrcoef(p[i], pstar[i])[0, 1]
    return {"ratio": ratio, "corr": corr, "rbar": rbar, "b": b, "p": p, "pstar": pstar}
```

De functie geeft naast de ratio ook de correlatie, $\bar r$, de trendgroei $b$ en
de gedetrendeerde reeksen terug, voor de replicatie. De drie economieën hebben
alle een trendgroei van 1,5% per jaar, dicht bij Shillers $b = 0{,}0148$:

- **(a) Kleidon.** Log-dividenden volgen een random walk met drift 1,5% en
  volatiliteit 12% per jaar. Met $G = \E[d_{t+1}/d_t]$ is de rationele prijs
  $p_t = d_t\,\delta G/(1-\delta G)$.

- **(b) Shiller.** Dividenden schommelen stationair rond een *bekende* trend: de
  afwijkingen volgen een AR(1) met $\phi = 0{,}5$, en de prijs is
  $p_t = \bar d\,\delta/(1-\delta) + (d_t - \bar d)\,\delta\phi/(1-\delta\phi)$.

- **(c) Flavin.** Hetzelfde als (b), maar met $\phi = 0{,}9$: stationair, maar zeer
  persistent.

De eerste cel bouwt economie (a), met 5 000 paden.

```{code-cell} ipython3
n_sim, T_sim, r_sim = 5_000, 109, 0.07
delta_sim = 1 / (1 + r_sim)
years = np.arange(T_sim)

# (a) log random walk dividends
mu_d, sigma_d = 0.015, 0.12
G = np.exp(mu_d + sigma_d**2 / 2)
level = np.exp(np.cumsum(rng.normal(mu_d, sigma_d, size=(n_sim, T_sim + 1)), axis=1))
P_rw = level[:, :-1] * delta_sim * G / (1 - delta_sim * G)
D_rw = level[:, 1:]
```

De rij `level` is het dividendniveau, en de koers is er een vast veelvoud van. De
volgende cel bouwt (b) en (c) met één functie voor de stationaire economie.

```{code-cell} ipython3
def stationary_economy(phi, sigma=0.05, dbar=1.0, trend=1.015):
    x = np.empty((n_sim, T_sim + 1))
    x[:, 0] = rng.normal(0.0, sigma / np.sqrt(1 - phi**2), n_sim)
    shocks = rng.normal(0.0, sigma, size=(n_sim, T_sim + 1))
    for i in range(1, T_sim + 1):
        x[:, i] = phi * x[:, i - 1] + shocks[:, i]
    price = dbar * delta_sim / (1 - delta_sim) + x[:, :-1] * delta_sim * phi / (1 - delta_sim * phi)
    return price * trend**years, (dbar + x[:, 1:]) * trend ** (years + 1)


economies = {
    "(a) random walk": (P_rw, D_rw),
    "(b) stationair, phi=0.5": stationary_economy(0.5),
    "(c) stationair, phi=0.9": stationary_economy(0.9),
}
```

De lus maakt de AR(1)-afwijkingen jaar na jaar aan. Nu passen we de toets toe op
elk pad en vatten we de verdeling van de ratio samen.

```{code-cell} ipython3
ratios = {}
summary = pd.DataFrame(columns=["aandeel ratio > 1", "5e percentiel", "mediaan", "95e percentiel"])
for name, (P, D) in economies.items():
    ratio = shiller_test(P, D)["ratio"]
    ratios[name] = ratio
    summary.loc[name] = [np.mean(ratio > 1), np.percentile(ratio, 5),
                         np.median(ratio), np.percentile(ratio, 95)]
summary.astype(float).round(3)
```

In (b) valt de ratio in geen enkele steekproef boven één: de toets werkt waarvoor
hij ontworpen is. In (c) slaat hij in bijna een op de vijf steekproeven vals
alarm. In (a) ligt de ratio in elke steekproef boven één. De figuur toont de drie
verdelingen. Let op de zwarte lijn bij één en op Shillers eigen 5,59 (gestreept).

```{code-cell} ipython3
:label: cel-shiller-excess-volatility-simulatie
:tags: [hide-input]

fig, ax = plt.subplots(figsize=(9, 4))
bins = np.logspace(np.log10(0.1), np.log10(20), 70)
for name, values in ratios.items():
    ax.hist(values, bins=bins, histtype="step", lw=1.6, label=name)
ax.axvline(1.0, color="black", lw=1.2)
for value, style in [(5.59, "--"), (13.28, ":")]:
    ax.axvline(value, color="grey", lw=1.0, ls=style)
ax.set_xscale("log")
ax.set_xlabel(r"$\sigma(p)/\sigma(p^*)$ volgens Shillers procedure (log-schaal)")
ax.set_ylabel("Aantal steekproeven")
ax.set_title("Rationele prijzen, 109 jaar: waar valt Shillers statistiek?")
ax.legend()
plt.show()
```

:::{figure} #cel-shiller-excess-volatility-simulatie
:label: fig-shiller-excess-volatility-simulatie
:width: 95%

In alle drie de economieën zijn prijzen exact rationeel. Rechts van de zwarte lijn
liggen dus alleen schendingen die de toets verzint. Bij random-walk-dividenden (a)
ligt de hele verdeling rechts, rond een factor 2,6. Bij stationaire dividenden (b)
werkt de toets zoals bedoeld. Bij persistente dividenden (c) schuift de verdeling
op naar de grens: de onderschatting van Flavin.
:::

Persistentie maakt de toets onbetrouwbaar zonder dat er een eenheidswortel nodig
is. In (c) slokt het steekproefgemiddelde van een persistente $p^*$ een groot deel
van zijn variantie op. In (a) werkt het mechanisme van
[](#thm-shiller-excess-volatility-kleidon): de rationele prijs springt, $p^*$
glijdt. De formule geldt hier niet letterlijk. De dividenden groeien geometrisch
met drift, en de toets meet gedetrendeerde niveaus in plaats van veranderingen.
Daarom ligt de mediaan van 2,6 onder $\sqrt{1 + 2/0{,}07} = 5{,}4$. Shillers 5,59 ligt boven het 95e percentiel
van (a), 4,04. De simulatie weerlegt Shiller dus niet. Zijn getal bewijst alleen
iets voor wie gelooft dat dividenden rond een bekende trend schommelen.

De laatste controle is die van de stelling zelf: over toestanden, op een vaste
datum, moet de grens ook in (a) gelden. We rekenen $p^*$ uit met de ware $r$ en de
rationele eindprijs, en vergelijken de variantie over de 5 000 paden op drie data.

```{code-cell} ipython3
P_T = level[:, -1] * delta_sim * G / (1 - delta_sim * G)
pstar_rw = ex_post_price(D_rw, 1 + r_sim, P_T)

check = pd.DataFrame(
    {
        "Var(p_t) over paden": [P_rw[:, t].var() for t in (10, 50, 100)],
        "Var(p*_t) over paden": [pstar_rw[:, t].var() for t in (10, 50, 100)],
    },
    index=pd.Index([10, 50, 100], name="datum t"),
)
check["grens geldt"] = check.iloc[:, 0] <= check.iloc[:, 1]
check.round(2)
```

Op elke datum is $\Var(p_t) \le \Var(p^*_t)$ over de paden, zoals
[](#thm-shiller-excess-volatility-bound) eist. Langs de tijd laten dezelfde paden
allemaal het omgekeerde zien. Dat zijn stap 4 en stap 6 van het toy-voorbeeld, op
schaal.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Robert J. Shiller, *Do Stock Prices Move Too Much to be Justified by
Subsequent Changes in Dividends?*, American Economic Review 1981
{cite}`Shiller1981`, met de varianten uit zijn Nobellezing {cite}`Shiller2014`.

**Wat.** Figuur 1 (gedetrendeerde reële S&P-koers tegen $p^*$, 1871–1979) en
tabel 2, kolom 1: $\sigma(p)/\sigma(p^*) = 5{,}59$, met correlatie, trendgroei en
$\bar r$. Daarnaast de gevoeligheid voor eindwaarde, trend en discontovoet, en de
log-lineaire grens van Campbell en Shiller.

**Data hier.** Shillers maandreeks via `hap.data.shiller()`, reëel met de CPI,
1871–2025, met de januarikoers als prijs en het twaalfmaandsdividend van december
als dividend van dat jaar. De reële korte rente komt uit
`hap.data.goyal_welch("annual")`.

**Verschil met het origineel.** Shiller defleerde met de groothandelsprijsindex
(WPI), die veel beweeglijker is dan de CPI. De Dow-reeks is niet gratis
beschikbaar, dus we tonen de S&P over 1928–1979 als benadering.

**Verwachte afwijking.** Op 1871–1979 ligt de ratio tussen 3 en 7, met $b$ en
$\bar r$ binnen enkele tienden van een procentpunt, een correlatie onder 0,5, en
over 1928–1979 een hogere ratio, zoals bij Shiller de Dow. Een ander *teken* van $\sigma(p) - \sigma(p^*)$ wijst op een fout in de code, en
volgens Kleidon varieert de ratio over redelijke keuzes met minstens een factor
vijf, met de log-lineaire ratio veel dichter bij één.
```

De eerste cel bouwt een jaarreeks: januarikoers, decemberdividend, het reële
rendement uit de totaalrendementsindex en de reële korte rente.

```{code-cell} ipython3
shiller_raw = hap_data.shiller()
jan = shiller_raw[shiller_raw.index.month == 1]
dec = shiller_raw[shiller_raw.index.month == 12]

annual = pd.DataFrame(
    {
        "P": jan["real_price"].to_numpy(),
        "TR": jan["real_total_return_price"].to_numpy(),
        "cpi": jan["cpi"].to_numpy(),
    },
    index=jan.index.year,
).join(pd.Series(dec["real_dividend"].to_numpy(), index=dec.index.year, name="D"))

rf_nominal = hap_data.goyal_welch("annual")["Rfree"]
annual["rf_real"] = (1 + pd.Series(rf_nominal.to_numpy(), index=rf_nominal.index.year)) / (
    annual["cpi"].shift(-1) / annual["cpi"]
) - 1
annual["R"] = annual["TR"].shift(-1) / annual["TR"] - 1

data = annual.loc[1871:2025]
print(f"steekproef {data.index[0]}–{data.index[-1]}, {len(data)} jaren; "
      f"ontbrekend: {int(data[['P', 'D', 'R', 'rf_real']].isna().sum().sum())}")
columns = ["P", "D", "R", "rf_real"]
overview = pd.DataFrame(
    {
        "gemiddelde": data[columns].mean(),
        "standaarddeviatie": data[columns].std(),
        "minimum": data[columns].min(),
        "maximum": data[columns].max(),
    }
)
overview.index = ["reële koers", "reëel dividend", "reëel rendement", "reële korte rente"]
overview.round(4)
```

De steekproef telt 155 jaren zonder ontbrekende waarden. Het gemiddelde reële
rendement is 8,6% per jaar, de gemiddelde reële rente 1,7%. Eerst de originele
steekproef, met Shillers conventies.

```{code-cell} ipython3
def run(start, end, **kwargs):
    sub = data.loc[start:end]
    out = shiller_test(sub["P"].to_numpy(), sub["D"].to_numpy(), **kwargs)
    return {key: value[0] for key, value in out.items()}


orig = run(1871, 1979)
short = run(1928, 1979)
pd.DataFrame(
    {
        "hier (S&P)": [orig["ratio"], orig["corr"], orig["b"], orig["rbar"], short["ratio"]],
        "Shiller 1981, tabel 2": [50.12 / 8.968, 0.3918, 0.0148, 0.0480, 13.28],
        "verwachting": ["3 tot 7", "onder 0,5", "enkele tienden pp", "enkele tienden pp",
                        "boven de eerste rij"],
    },
    index=["sigma(p)/sigma(p*), 1871–1979", "Corr(p, p*), 1871–1979",
           "trendgroei b, 1871–1979", "r-streep, 1871–1979",
           "sigma(p)/sigma(p*), 1928–1979 (Shiller: Dow)"],
).round(4)
```

**Geslaagd.** Elke rij valt binnen de verwachting uit het replicatieblok, en de
kortere steekproef geeft ook hier de hogere ratio. Dat onze ratio's lager
uitvallen dan die van Shiller, kan aan de deflator liggen: een beweeglijker prijsindex zoals de WPI maakt een reële
prijsreeks beweeglijker. Met de data hier is dat niet na te gaan.

Voor de figuur rekenen we ook twee versies van $p^*$ zonder detrending uit, met de
koers van januari 2025 als eindwaarde. De eerste verdisconteert tegen het
gemiddelde reële rendement. De tweede verdisconteert tegen de reële korte rente
plus een constante premie, en heeft dus elk jaar een andere discontovoet.

```{code-cell} ipython3
full = run(1871, 2025)
sub = data.loc[1871:2024]
r_const = data["R"].mean()
premium = r_const - data["rf_real"].mean()
pstar_const = ex_post_price(sub["D"].to_numpy(), 1 + r_const, data.loc[2025, "P"])
pstar_rates = ex_post_price(
    sub["D"].to_numpy(), 1 + sub["rf_real"].to_numpy() + premium, data.loc[2025, "P"]
)
```

De premie is het verschil tussen gemiddeld rendement en gemiddelde rente,
$0{,}0860 - 0{,}0168 = 0{,}069$: vrijwel de $6{,}92\%$ die
[](#03-13-equity-premium-puzzle) tot 2024 vindt. Let in de figuur links op de afstand tussen koers
en $p^*$, en rechts op de momenten waarop de lijnen bewegen.

```{code-cell} ipython3
:label: cel-shiller-excess-volatility-figuur1
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
yrs = data.index
axes[0].plot(yrs, full["p"], lw=1.4, label="koers $p$")
axes[0].plot(yrs, full["pstar"], lw=1.6, ls="--", label="ex-post rationele prijs $p^*$")
axes[0].axvline(1979, color="grey", lw=0.8)
axes[0].set_xlabel("Jaar")
axes[0].set_ylabel("Gedetrendeerd reëel niveau")
axes[0].set_title("Shillers figuur 1, bijgewerkt tot 2025")
axes[0].legend()

axes[1].plot(sub.index, sub["P"], lw=1.4, label="koers $p$")
axes[1].plot(sub.index, pstar_const, lw=1.6, ls="--", label="$p^*$, constante $r$")
axes[1].plot(sub.index, pstar_rates, lw=1.2, ls=":", label="$p^*$, reële rente + premie")
axes[1].set_yscale("log")
axes[1].set_xlabel("Jaar")
axes[1].set_ylabel("Reëel niveau (log-schaal)")
axes[1].set_title("Niet gedetrendeerd, twee discontovoeten")
axes[1].legend()
plt.show()
```

:::{figure} #cel-shiller-excess-volatility-figuur1
:label: fig-shiller-excess-volatility-figuur1
:width: 100%

Links: de gedetrendeerde reële S&P-koers en $p^*$ met Shillers conventies; de
verticale lijn markeert het einde van zijn steekproef. Het beeld van 1981
overleeft: $p^*$ kabbelt, de koers niet. Rechts: dezelfde data zonder detrending,
met $p^*$ tegen een constant rendement en tegen de reële rente plus premie.
Tijdvariërende rentes maken $p^*$ beweeglijker, maar volgen de grote bewegingen
van de koers maar deels.
:::

Nu de gevoeligheid. Elke rij van de tabel hieronder is een verdedigbare keuze die
in de stelling niet voorkomt. De log-lineaire rijen gebruiken als ratio de log van
de januarikoers min de log van het dividend van het jaar ervoor, en $pd^*_t$ uit
[](#eq-shiller-excess-volatility-cs) met gedemeende dividendgroei, zonder
detrending. De eerste cel definieert die log-lineaire grens.

```{code-cell} ipython3
def loglinear_bound(start, end, terminal="last"):
    """Campbell-Shiller variance bound on log price-dividend ratios."""
    yrs = np.arange(start, end + 1)
    pd_ratio = np.log(data.loc[yrs, "P"].to_numpy() / data.loc[yrs - 1, "D"].to_numpy())
    growth = np.log(data.loc[yrs, "D"].to_numpy() / data.loc[yrs - 1, "D"].to_numpy())
    rho = np.exp(pd_ratio.mean()) / (1 + np.exp(pd_ratio.mean()))
    x = pd_ratio - pd_ratio.mean()
    end_value = x[-1] if terminal == "last" else 0.0
    # pd*_t = (g_{t+1} - mean g) + rho * pd*_{t+1}: ex_post_price with R = 1/rho and scaled growth
    xstar = ex_post_price((growth - growth.mean()) / rho, 1 / rho, end_value)
    return x.std() / xstar.std(), np.corrcoef(x, xstar)[0, 1]
```

De functie lost $pd^*$ achterwaarts op met dezelfde `ex_post_price`, met $1/\rho$
in de rol van $1 + r$. De volgende cel draait Shillers toets met andere
steekproeven, eindwaarden, trends en discontovoeten.

```{code-cell} ipython3
se_mean_R = data["R"].std() / np.sqrt(len(data))
rows = {
    "1871–1979, Shiller-conventies": run(1871, 1979),
    "1928–1979, Shiller-conventies": run(1928, 1979),
    "1871–2025, Shiller-conventies": full,
    "1871–2025, eindwaarde = laatste koers": run(1871, 2025, terminal="last"),
    "1871–2025, trend op dividenden": run(1871, 2025, detrend="dividend"),
    "1871–2025, r-streep − 2 SE": run(1871, 2025, rate=full["rbar"] - 2 * se_mean_R),
    "1871–2025, r-streep + 2 SE": run(1871, 2025, rate=full["rbar"] + 2 * se_mean_R),
}
table = pd.DataFrame(columns=["sigma(p)/sigma(p*)", "Corr(p, p*)"])
for label, result in rows.items():
    table.loc[label] = [result["ratio"], result["corr"]]
print(f"SE van het gemiddelde reële rendement: {se_mean_R:.4f}")
```

De standaardfout van het gemiddelde rendement is 1,4 procentpunt, en de twee
laatste rijen verschuiven $\bar r$ met twee keer dat bedrag. De laatste cel voegt de
rente-variant uit de figuur toe, gedetrendeerd met dezelfde trend, en de drie
log-lineaire rijen.

```{code-cell} ipython3
b_sub = shiller_test(sub["P"].to_numpy(), sub["D"].to_numpy())["b"][0]
trend_sub = np.exp(b_sub) ** (np.arange(len(sub)) - (len(sub) - 1))
p_detrended = sub["P"].to_numpy() / trend_sub
pstar_rates_detrended = pstar_rates / trend_sub
table.loc["1871–2024, reële rente + premie"] = [
    p_detrended.std() / pstar_rates_detrended.std(),
    np.corrcoef(p_detrended, pstar_rates_detrended)[0, 1],
]
for label, (start, end, term) in {
    "log-lineair 1872–2024, eindwaarde = laatste": (1872, 2024, "last"),
    "log-lineair 1872–2024, eindwaarde = gemiddelde": (1872, 2024, "mean"),
    "log-lineair 1872–1979": (1872, 1979, "last"),
}.items():
    table.loc[label] = loglinear_bound(start, end, term)

table.astype(float).round(3)
```

**Geslaagd**, ook voor de tweede verwachting. Op dezelfde data en met dezelfde
stelling loopt de ratio van 0,55 tot 9,8, veel meer dan de verwachte factor vijf.
De keuzes met het grootste effect zijn die welke Kleidon en Marsh en Merton
aanwezen:

- **Trend.** Een trend op de dividenden in plaats van op de koers maakt de ratio
  over 1871–2025 vijf keer zo groot. De dividenden groeiden langzamer dan de koers,
  zodat de koers na 1980 ver boven zijn trend komt te liggen.

- **Eindwaarde.** De werkelijke koers als eindwaarde laat de ratio zakken naar
  1,1, omdat $p^*$ na 1990 de koersstijging erft.

- **Steekproef.** De keuze van de steekproef bepaalt of de jaren negentig erin
  zitten.

- **Discontovoet.** Met de reële korte rente plus een constante premie is $p^*$ na
  detrending beweeglijker dan de koers (ratio 0,83). In niveaus is de grens dan
  niet geschonden. Wat overblijft, is dat $p^*$ en de koers maar deels samen
  bewegen (correlatie 0,59).

Ook de standaardfout van 2% uit [](#00-01-rendementen) doet mee: een gemiddeld
rendement is slecht meetbaar. De discontovoet is zo'n gemiddelde, en twee
standaardfouten verschuiven de ratio van 0,55 naar 2,36. Met een discontovoet twee
standaardfouten lager is de grens niet eens geschonden. Een tweede moment is goed
meetbaar, maar deze statistiek bouwt het tweede moment van $p^*$ op uit een eerste
moment dat dat niet is.

De log-lineaire grens is het robuuste antwoord, en ze zegt iets bescheideners. De
log-prijs-dividend-ratio beweegt 1,1 tot 1,9 keer zo veel als de dividendgroei kan
rechtvaardigen, afhankelijk van de eindwaarde. Dat is geen factor dertien, maar
het ligt boven één. Wat erboven uitsteekt, moet volgens
[](#eq-shiller-excess-volatility-decompositie) uit voorspelbare rendementen komen:
in [](#01-03-williams-ddm) voorspelde de prijs-dividend-ratio het
tienjaarsrendement, en niet de tienjaarsgroei van dividenden.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De variantiegrens is een van de weinige resultaten in
het vak die uit bijna niets volgen: een voorspelling beweegt nooit meer dan wat ze
voorspelt. Ze verlegde de toets van efficiëntie van de vraag of iemand morgen rijk
kan worden, waarop het antwoord nee was, naar de vraag of koersniveaus passen bij
fundamentele waarde. En ze leverde een beeld op, de koers tegen $p^*$, dat een
generatie economen overtuigde. Dat rendementen op korte termijn onvoorspelbaar
zijn, zoals in [](#02-06-efficiente-markten), betekent nog niet dat prijzen juist
zijn.

**Waar het breekt.** Niet in de ongelijkheid, maar in haar meting. Onze replicatie
geeft 3,9 op Shillers steekproef, en tussen 0,55 en 9,3 over 1871–2025, afhankelijk
van keuzes die de stelling niet voorschrijft. Een random-walk-economie met exact
rationele prijzen schendt de gedetrendeerde toets in elke steekproef. De robuuste
log-lineaire versie blijft boven één, maar is geen factor vijf tot dertien. Wat
overeind blijft, is een kwalitatief feit: de prijs-dividend-ratio beweegt meer dan
dividendnieuws kan dragen, en dat surplus is hetzelfde als voorspelbare
rendementen.

**Risico of vergissing?** De Chicago-lezing, met Cochrane
{cite}`Cochrane1992,Cochrane2011` als woordvoerder: de discontovoet varieert.
Verworpen is de constante $r$ van Williams, niet de rationaliteit van beleggers.
In recessies eisen beleggers meer, dus zijn prijzen laag en rendementen daarna
hoog. De Yale-lezing komt van Shiller zelf {cite}`Shiller2014`: de benodigde
discontovoet beweegt wild op momenten dat geen gemeten rente beweegt. Ook hier
volgt de rente-variant van $p^*$ de koers maar matig (correlatie 0,59). Koersen
reageren volgens Shiller eerder op wisselende stemmingen, *animal spirits*. Beide
lezingen voorspellen een grote rendementscovariantie in
[](#eq-shiller-excess-volatility-decompositie). Alleen een onafhankelijke meting
van de discontovoet scheidt ze, en die bestaat nog altijd nauwelijks.

**Wat er daarna kwam.** Als de markt als geheel te veel beweegt, zouden ook
aandelen die goedkoop zijn ten opzichte van winst of boekwaarde later meer moeten
opbrengen. Dat vonden Basu, Banz en Rosenberg in de cross-sectie,
[](#03-16-vroege-anomalieen).

## Oefeningen

:::{exercise}
:label: ex-shiller-excess-volatility-1

**Een derde informatiestructuur.** Neem het toy-voorbeeld en voeg structuur C
toe: op $t = 0$ zijn $d_1$ en $d_2$ al bekend, $d_3$ niet.

1. Bereken $\Var(p^C_0)$ over de acht toestanden met de hand.
2. Controleer de keten $\Var(p^A_0) \le \Var(p^B_0) \le \Var(p^C_0) \le \Var(p^*_0)$
   en de decompositie $\Var(p^*_0) = \Var(p^C_0) + \Var(p^*_0 - p^C_0)$ in code.
3. Welke informatiestructuur geeft $\Var(p_0) = \Var(p^*_0)$, en wat is dan de
   voorspelfout?
:::

:::{solution} ex-shiller-excess-volatility-1
:class: dropdown

**(1)** $p^C_0 = 0{,}8\,d_1 + 0{,}64\,d_2 + 0{,}512 \times 10$, dus
$\Var(p^C_0) = 25 \times (0{,}64 + 0{,}4096) = 26{,}24$.

**(2)** De code rekent de keten en de decompositie na.

```{code-cell} ipython3
price_C = 0.8 * states[:, 0] + 0.64 * states[:, 1] + 0.512 * 10
chain = [price_A.var(), price_B.var(), price_C.var(), pstar_0.var()]
print("A, B, C, p* :", np.round(chain, 4), "  oplopend:", bool(np.all(np.diff(chain) >= 0)))
print("Var(p*) - Var(p_C) - Var(u_C) =",
      round(pstar_0.var() - price_C.var() - (pstar_0 - price_C).var(), 12))
```

De keten loopt op en de decompositie sluit op nul.

**(3)** Volledige kennis van $d_1, d_2, d_3$: dan is $p_0 = p^*_0$ en de
voorspelfout overal nul.

Wat dit leert: elke extra informatie maakt de rationele prijs beweeglijker, en
$p^*$ is het plafond dat bij volledige informatie hoort. Een koers boven dat
plafond kan dus niet uit meer informatie komen.
:::

:::{exercise}
:label: ex-shiller-excess-volatility-2

**Twee grenzen.** Gebruik [](#thm-shiller-excess-volatility-kleidon) en
[](#thm-shiller-excess-volatility-bound).

1. Bereken $\sigma(\Delta p)/\sigma(\Delta p^*)$ voor $r \in \{0{,}02;\ 0{,}048;\ 0{,}10\}$.
2. Simuleer één pad van 200 000 jaar met $d_{t+1} = d_t + \varepsilon_{t+1}$,
   $\varepsilon \sim N(0,1)$ en $r = 0{,}048$. Benader $p^*_t$ met 400 termen plus
   de rationele eindprijs, en vergelijk de gemeten ratio met de formule.
3. Bewijs de ondergrens van LeRoy en Porter: voor een kleinere
   informatieverzameling $\mathcal H_t \subseteq \mathcal I_t$ is
   $\Var(\E[p^*_t \mid \mathcal H_t]) \le \Var(p_t)$.
:::

:::{solution} ex-shiller-excess-volatility-2
:class: dropdown

**(1) en (2)** De formule is $\sqrt{1 + 2/r}$: $\sqrt{101} = 10{,}05$,
$\sqrt{42{,}67} = 6{,}53$ en $\sqrt{21} = 4{,}58$. De code rekent die na en meet de
ratio op het lange pad.

```{code-cell} ipython3
for r_val in (0.02, 0.048, 0.10):
    print(f"r = {r_val:5.3f}: formule {np.sqrt(1 + 2 / r_val):6.2f}")

r_ex, n_long, horizon = 0.048, 200_000, 400
delta_ex = 1 / (1 + r_ex)
d_long = np.cumsum(rng.normal(0.0, 1.0, n_long))
p_long = d_long / r_ex
m = n_long - horizon
pstar_long = delta_ex**horizon * p_long[horizon:]            # rational terminal price
for j in range(1, horizon + 1):                               # p*_t = sum_j delta^j d_{t+j}
    pstar_long = pstar_long + delta_ex**j * d_long[j:j + m]
print(f"gesimuleerd (r = 0.048): "
      f"{np.diff(p_long[:m]).std() / np.diff(pstar_long).std():.2f}")
```

De gesimuleerde ratio, 6,54, ligt vlak bij de formule, 6,53.

**(3)** Omdat $\mathcal H_t \subseteq \mathcal I_t$, geeft de wet van iteratieve
verwachtingen $\E[p^*_t \mid \mathcal H_t] = \E[p_t \mid \mathcal H_t]$. Pas nu de
variantiegrens toe met $p_t$ in de rol van $p^*_t$ en $\mathcal H_t$ in de rol van
$\mathcal I_t$: $\Var(\E[p_t \mid \mathcal H_t]) \le \Var(p_t)$.

Wat dit leert: juist bij de lage discontovoeten waarmee Shiller rekende, is de
tijdreeks van een rationele prijs het beweeglijkst ten opzichte van $p^*$. En de
grens heeft twee kanten: minder informatie geeft een rustiger prijs.
:::

:::{exercise}
:label: ex-shiller-excess-volatility-3

**De naoorlogse steekproef.** Herhaal de gevoeligheidstabel voor 1950–2025:
Shillers conventies, de laatste koers als eindwaarde, de trend op dividenden, en
de log-lineaire grens met beide eindwaarden. Is de conclusie "de prijs beweegt
te veel" in alle vijf varianten dezelfde?
:::

:::{solution} ex-shiller-excess-volatility-3
:class: dropdown

De functies `run` en `loglinear_bound` doen het werk.

```{code-cell} ipython3
post = {
    "Shiller-conventies": run(1950, 2025)["ratio"],
    "eindwaarde = laatste koers": run(1950, 2025, terminal="last")["ratio"],
    "trend op dividenden": run(1950, 2025, detrend="dividend")["ratio"],
    "log-lineair, laatste": loglinear_bound(1950, 2024, "last")[0],
    "log-lineair, gemiddelde": loglinear_bound(1950, 2024, "mean")[0],
}
pd.Series(post, name="sigma(p)/sigma(p*), 1950–2025").round(3)
```

De ratio ligt in alle varianten boven één, maar de omvang verschilt met ruim een
factor negen: van 1,34 (log-lineair, laatste eindwaarde) tot 12,1 (trend op
dividenden).

Wat dit leert: het teken van excess volatility is robuust over steekproeven en
conventies, de omvang niet. Met ruim zeventig jaar zeer persistente data is dat
wat Flavin en Kleidon zouden voorspellen.
:::
