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

(02-07-event-studies)=

# De event study

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1968–1997, van de eerste event studies op de CRSP-tape tot het
methodologische overzicht van MacKinlay. In die dertig jaar werd de event study het
standaardinstrument om te meten hoe koersen op nieuws reageren.

**Wat we al weten.** [Het vorige college](#02-06-efficiente-markten) formuleerde de
efficiënte-marktheorie van Fama, waarin prijzen alle beschikbare informatie weerspiegelen. Een toets van die theorie is altijd ook een toets van een model voor het
"normale" rendement, en die koppeling heet de *joint hypothesis* (gezamenlijke hypothese). De toetsen daar
zochten patronen in de rendementsreeks zelf, op dagkoersen van de dertig Dow
Jones-aandelen {cite}`Fama1965,FamaBlume1966`. Voor een studie van honderden
aandelen rond hun eigen nieuws lagen de data klaar op [de
CRSP-tape](#02-05-crsp-tape), met maandrendementen van elk NYSE-aandeel sinds 1926.

**Welke vraag staat open.** Zit publiek nieuws al in de prijs op het moment dat het
bekend wordt, of loopt de prijs erachteraan? Het lastige is dat niemand weet wat het
aandeel zonder dat nieuws had gedaan.
```

## Overzicht

Hoe meten we of een prijs nieuws verwerkt vóór of nadat het nieuws bekend wordt? We
leggen alle gebeurtenissen op tijd nul, trekken van elk rendement af wat het aandeel
normaal zou doen, en middelen de rest. Zo gemeten verwerken prijzen publiek nieuws snel,
en grotendeels al vóór de publicatie. In dit college:

- leiden we af hoeveel ruis er in een abnormaal rendement zit, inclusief de
  *schattingsfout* (de toevallige fout in de geschatte alpha en bèta van het marktmodel);

- bouwen we daaruit een toets en een formule voor zijn toetskracht, en zien we dat de
  toets faalt bij events op dezelfde dag, en over lange horizonnen doordat een *modelfout*
  (een verkeerd model voor het normale rendement) zich daar opstapelt;

- simuleren we, zoals Brown en Warner, hoe vaak de toets een effect van 1% vindt;

- repliceren we de figuur van Fama, Fisher, Jensen en Roll op 102
  aandelensplitsingen uit 2004–2025, waarin de koers vóór de ex-datum stijgt en daarna
  niet meer. Het moment van publicatie zelf meten we daar niet, want dat bewijs komt van
  Ball en Brown.

Twee artikelen zetten de toon. {cite:t}`BallBrown1968` vonden dat 85 tot 90%
van de informatie in het jaarcijfer al vóór de publicatie in de koers zat, via
snellere kanalen (p. 176). {cite:t}`FamaFisherJensenRoll1969` (FFJR) bouwden bij
hun studie van splitsingen het instrument dat sindsdien *event study* heet, een studie
van het koersgedrag in *eventtijd*, waarin elke gebeurtenis op dag of maand nul ligt,
ongeacht de kalenderdatum. Het idee was ouder ({cite:t}`MacKinlay1997` noemt
{cite:t}`Dolley1933` als waarschijnlijk eerste studie), maar FFJR voegden de correctie
voor de markt en het middelen in eventtijd toe. Daardoor werd de efficiënte-marktheorie
toetsbaar op nieuws. De event study is zelf geen theorie die getoetst wordt, maar een
meetinstrument dat feiten levert voor de vraag die de hele reeks stelt, theorie of feit.
Die feiten zijn altijd afwijkingen van een model.

## Intuïtie: waarom zou dit waar zijn?

Een aandelensplitsing verandert niets. Een bedrijf dat één aandeel van 400 dollar
vervangt door vier aandelen van 100 dollar, heeft dezelfde fabrieken, dezelfde
winst en dezelfde eigenaren. In een rationele markt verandert de waarde van het
bedrijf op de splitsingsdatum dus niet.

Toch is een splitsing niet informatieloos. Bedrijven splitsen vooral nadat de
koers flink is gestegen, vaak samen met een hogere dividenduitkering. De
aankondiging kan dus iets *zeggen*, ook al *doet* ze niets. FFJR zagen daarin een
laboratorium, want een splitsing is een gebeurtenis zonder
economische inhoud, maar met mogelijke informatie. In een efficiënte markt komt die
informatie in de prijs zodra ze bekend wordt, zodat een belegger die het aandeel daarna
koopt, er niets bijzonders meer mee verdient.

Om dat te toetsen moeten we eerst weten wat het aandeel *zonder* het nieuws had gedaan.
Stijgt de markt die maand 5% en het aandeel 6%, dan is het nieuws hooguit 1% waard. FFJR
schatten daarom over een rustige periode hoe sterk het aandeel met de markt meebeweegt,
en dat verband heet het *marktmodel*. Het werkelijke rendement min wat het marktmodel
voorspelt, is het *abnormale rendement*, en de som daarvan over de dagen rond het event
heet het *cumulatieve abnormale rendement* (CAR).

Eén event zegt weinig, want een aandeel beweegt op een gewone dag 1 à 2% om redenen die
niemand kent, en een nieuwsfeit van 1% verdwijnt in die ruis. Daarom middelt een
onderzoeker honderd splitsingen, elk op hun eigen dag nul. Omdat de ruis per event
onafhankelijk is, krimpt ze in het gemiddelde met de wortel van het aantal events,
terwijl het signaal bij elk event op dezelfde dag staat en niet krimpt. Zo vindt een
toets een effect van 1% met enkele tientallen events als de dag bekend is, maar niet als
het venster weken beslaat.

Dezelfde wortel kennen we uit de standaardfout van 2% in [het college over
rendementen](#00-01-rendementen), waar het gemiddelde rendement bij een volatiliteit van
20% per jaar na honderd jaar data nog op 2 procentpunt onzeker is. Daar werkt de wortel
tegen de onderzoeker, hier werkt hij ervoor.

Een premie van 6% per jaar is 0,024% per dag, en tegen een dagelijkse marktruis van 1%
geeft dat een verhouding van 0,024 tussen signaal en ruis. Een nieuwsfeit van 1% op een
bekende dag staat tegen 2% ruis van één aandeel, zodat de verhouding daar 0,5 is. Die
verhouding is ruim twintig keer gunstiger, en daarom zijn er
ongeveer vierhonderd keer minder waarnemingen nodig ($21^2 \approx 440$).

De redenering heeft twee zwakke plekken. De ruis middelt alleen weg als events op
verschillende dagen vallen, en het normale
rendement komt uit een model dat verkeerd kan zijn. Zo'n modelfout is iets anders dan de
toevallige schattingsfout in de bèta, omdat ze niet verdwijnt met meer data. Over drie
dagen maakt een kleine modelfout niets uit, maar over drie jaar stapelt ze zich op tot
een abnormaal rendement dat er niet is.

Een event study meet ook *wanneer* een prijs reageert. Met maanddata zagen FFJR
alleen dat de reactie binnen een maand lag. Volgens Santa-Clara, die de latere literatuur
samenvat, ging de halfwaardetijd van
nieuws, de tijd waarin de helft van de prijsreactie binnen is, van dagen in 1969 via uren
in 2000 naar seconden nu {cite}`SantaClara2026`. In
zijn woorden:

> the event-study half-lives that were days in 1969 and hours in 2000 are now
> seconds for anything in a filing, a transcript or a satellite image.

Een splitsing heeft twee datums, de aankondiging en enkele weken later de *ex-datum*, de
eerste handelsdag waarop het aandeel gesplitst noteert. Omdat het nieuws in de
aankondiging zit, verwachten we dat het CAR vóór en rond de aankondiging stijgt, dat het
abnormale rendement op de ex-datum nul is en dat het CAR daarna vlak blijft. De
replicatie kent alleen de ex-datum, zodat we de stijging daar vóór dag 0 verwachten.

## Toy-voorbeeld: drie aandelen, vijf plus drie dagen

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

Drie aandelen, A, B en C, hebben elk een event op dag $\tau = 0$. We schatten het
marktmodel op een *schattingsvenster* van vijf dagen ($\tau = -6, \dots, -2$) en
meten abnormale rendementen in een *eventvenster* van drie dagen
($\tau = -1, 0, +1$). Alle rendementen staan in procenten.

| $\tau$ | $-6$ | $-5$ | $-4$ | $-3$ | $-2$ | | $-1$ | $0$ | $+1$ |
|---|---|---|---|---|---|---|---|---|---|
| markt $r_m$ | $-2{,}0$ | $-1{,}0$ | $0{,}0$ | $1{,}0$ | $2{,}0$ | | $1{,}0$ | $-1{,}0$ | $1{,}0$ |
| A | $-1{,}4$ | $-1{,}4$ | $0{,}1$ | $0{,}6$ | $2{,}6$ | | $1{,}5$ | $1{,}0$ | $1{,}3$ |
| B | $-1{,}0$ | $0{,}0$ | $-1{,}0$ | $1{,}0$ | $1{,}0$ | | $0{,}5$ | $1{,}5$ | $0{,}5$ |
| C | $-3{,}3$ | $-0{,}8$ | $0{,}2$ | $2{,}2$ | $2{,}7$ | | $2{,}0$ | $0{,}5$ | $1{,}1$ |

Op dag 0 daalt de markt 1%, terwijl alle drie de aandelen stijgen, en daar zit dus het
event. Hoe groot het is en hoe zeker we dat weten, rekenen we in vijf stappen uit.

**Het recept.** De variantie van een CAR over $L_2$ dagen is niet
$L_2\hat\sigma^2_{\varepsilon_i}$, met $\hat\sigma^2_{\varepsilon_i}$ de restvariantie
van het marktmodel, maar

$$
\hat\sigma^2_{\varepsilon_i} \times \Bigl[L_2 + \frac{L_2^2}{L_1} + \frac{(S^*_m - L_2\hat\mu_m)^2}{S_{mm}}\Bigr],
$$

met $L_1$ de lengte van het schattingsvenster. Verder zijn $\hat\mu_m$ en $S_{mm}$ het
gemiddelde van de markt en de kwadratensom rond dat gemiddelde, en is $S^*_m$ de som van
de markt in het eventvenster. De twee extra termen komen van de fout in de geschatte
$\hat\alpha_i$ en
$\hat\beta_{i,m}$. Die fout is op elke dag van het eventvenster dezelfde, zodat ze in het
CAR $L_2$ keer meetelt en de term van $\hat\alpha_i$ met $L_2^2$ groeit.

**Stap 1: het marktmodel.** De markt heeft in het schattingsvenster gemiddelde
$\hat\mu_m = 0$ en $S_{mm} = 10$. Omdat het gemiddelde nul is, geeft OLS $\hat\alpha_i = \bar r_i$
en
$\hat\beta_{i,m} = \sum r_m r_i / 10$. Voor A is $\hat\alpha_A = 0{,}5/5 = 0{,}1$ en
$\hat\beta_{A,m} = (2{,}8 + 1{,}4 + 0 + 0{,}6 + 5{,}2)/10 = 1{,}0$.

**Stap 2: de restvariantie.** De residuen van A zijn
$(0{,}5;\ -0{,}5;\ 0;\ -0{,}5;\ 0{,}5)$, met kwadratensom 1. Gedeeld door
$L_1 - 2 = 3$ geeft dat $\hat\sigma^2_{\varepsilon_A} = 0{,}3333$. Voor alle drie de
aandelen ziet de berekening er zo uit:

| aandeel | $\sum r_i$ | $\sum r_m r_i$ | $\hat\alpha_i$ | $\hat\beta_{i,m}$ | residuen | $\hat\sigma^2_{\varepsilon_i}$ |
|---|---|---|---|---|---|---|
| A | $0{,}5$ | $10$ | $0{,}1$ | $1{,}0$ | $0{,}5;\ -0{,}5;\ 0;\ -0{,}5;\ 0{,}5$ | $1/3 = 0{,}3333$ |
| B | $0$ | $5$ | $0$ | $0{,}5$ | $0;\ 0{,}5;\ -1;\ 0{,}5;\ 0$ | $1{,}5/3 = 0{,}5$ |
| C | $1{,}0$ | $15$ | $0{,}2$ | $1{,}5$ | $-0{,}5;\ 0{,}5;\ 0;\ 0{,}5;\ -0{,}5$ | $1/3 = 0{,}3333$ |

**Stap 3: abnormale rendementen.** Voor A is het abnormale rendement op dag 0 gelijk aan
$1{,}0 - 0{,}1 - 1{,}0 \times (-1{,}0) = 1{,}9$. De tabel geeft ze voor alle drie de
aandelen en alle drie de dagen.

| | $\widehat{AR}_{-1}$ | $\widehat{AR}_{0}$ | $\widehat{AR}_{+1}$ | $\widehat{CAR}$ |
|---|---|---|---|---|
| A | $0{,}4$ | $1{,}9$ | $0{,}2$ | $2{,}5$ |
| B | $0{,}0$ | $2{,}0$ | $0{,}0$ | $2{,}0$ |
| C | $0{,}3$ | $1{,}8$ | $-0{,}6$ | $1{,}5$ |

Het gemiddelde CAR, het CAAR, is $2{,}0\%$. Of dat meer is dan toeval, hangt af van de
ruis in elk CAR, en die volgt uit het recept.

**Stap 4: de variantie van een CAR.** Met $S^*_m = 1$ geeft het recept niet 3 maar $3 +
9/5 + 1/10 = 4{,}9$, en het grootste deel van de extra ruis komt van de fout in
$\hat\alpha_i$ (9/5), omdat vijf schattingsdagen weinig zijn tegen drie eventdagen. Voor A
en C is de variantie daardoor
$4{,}9 \times 0{,}3333 = 1{,}6333$, voor B $2{,}45$.

**Stap 5: de toets.** De variantie van het CAAR is
$(1{,}6333 + 2{,}45 + 1{,}6333)/9 = 0{,}6352$, zodat $J_1 = 2{,}0/\sqrt{0{,}6352} = 2{,}509$.
Een onderzoeker die de schattingsfout vergeet, deelt door
$\sqrt{3{,}5/9} = 0{,}6236$ en vindt $3{,}207$.

De code doet dezelfde vijf stappen en zet de uitkomsten naast de handberekening.

```{code-cell} ipython3
m_est = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])   # market, estimation window tau = -6..-2
m_evt = np.array([1.0, -1.0, 1.0])              # market, event window tau = -1..+1
R_est = {"A": [-1.4, -1.4, 0.1, 0.6, 2.6], "B": [-1.0, 0.0, -1.0, 1.0, 1.0],
         "C": [-3.3, -0.8, 0.2, 2.2, 2.7]}
R_evt = {"A": [1.5, 1.0, 1.3], "B": [0.5, 1.5, 0.5], "C": [2.0, 0.5, 1.1]}
L1, L2 = len(m_est), len(m_evt)
S_mm = np.sum((m_est - m_est.mean()) ** 2)
factor = L2 + L2**2 / L1 + (m_evt.sum() - L2 * m_est.mean()) ** 2 / S_mm   # the recipe

toy_fits, car, var_car, var_naive = {}, {}, {}, {}
for name in R_est:
    beta, alpha = np.polyfit(m_est, R_est[name], deg=1)                  # step 1
    resid = np.array(R_est[name]) - alpha - beta * m_est
    toy_fits[name] = (alpha, beta, resid @ resid / (L1 - 2))             # step 2
    car[name] = np.sum(np.array(R_evt[name]) - alpha - beta * m_evt)     # step 3
    var_car[name] = factor * toy_fits[name][2]                           # step 4
    var_naive[name] = L2 * toy_fits[name][2]

N = len(car)
caar = np.mean(list(car.values()))
J1 = caar / np.sqrt(sum(var_car.values()) / N**2)                        # step 5
J1_naive = caar / np.sqrt(sum(var_naive.values()) / N**2)

hand = {"CAR A": 2.5, "CAR B": 2.0, "CAR C": 1.5, "factor": 4.9,
        "CAAR": 2.0, "J1": 2.509, "J1 naief": 3.207}
code = {"CAR A": car["A"], "CAR B": car["B"], "CAR C": car["C"], "factor": factor,
        "CAAR": caar, "J1": J1, "J1 naief": J1_naive}
pd.DataFrame({"met de hand": hand, "code": code}).round(3)
```

De code komt op dezelfde getallen uit als de handberekening. Een abnormaal rendement is
dus een rendement min een geschat model, en die schatting voegt ruis toe die de naïeve
toets over het hoofd ziet. Met vijf schattingsdagen is de naïeve $t$-waarde daardoor 28%
te hoog.

## Theorie

We leiden eerst de verdeling van een abnormaal rendement af, en daaruit de variantie van
een CAR. Die variantie is het recept uit het toy-voorbeeld en de kern van dit college.
Daarna volgen de toets $J_1$, zijn toetskracht en de halfwaardetijd van informatie. We
sluiten af met de twee plekken waar de toets faalt, bij events op dezelfde dag en over
lange horizonnen.

### Opzet: eventtijd en het marktmodel

Een event study verandert de tijdas. Voor elk event $i = 1, \dots, N$ is $\tau = 0$
de dag van het event, ongeacht de kalenderdatum. Het schattingsvenster heeft $L_1$
dagen, meestal vele malen meer dan het eventvenster. Het eventvenster loopt
van $\tau_1$ tot $\tau_2$ en heeft $L_2 = \tau_2 - \tau_1 + 1$ dagen, meestal kort rond
het event. De vensters
overlappen niet, zodat het event de schatting van het normale rendement niet
besmet.

In de rest van de reeks loopt de tijd in kalendertijd, met rendementen van $t$ naar
$t+1$, maar hier telt $\tau$ de dagen ten opzichte van het event. We schrijven
$r_{i,\tau}$ voor het netto rendement, zonder aftrek van de risicovrije rente.
{cite:t}`MacKinlay1997` schrijft daarvoor $R$. Een ster markeert het eventvenster,
zodat $\mathbf{r}^*_i$ de vector van de $L_2$ eventrendementen is.

Een groot deel van de dagelijkse beweging van een aandeel is marktbeweging. Een
onderzoeker die die component weghaalt, houdt een residu over met minder variantie,
zodat de toets scherper wordt. Het marktmodel is dus een statistisch filter en geen
theorie over verwachte rendementen:

```{math}
:label: eq-eventstudies-marktmodel
r_{i,\tau} = \alpha_i + \beta_{i,m} r_{m,\tau} + \varepsilon_{i,\tau},
\qquad
\E[\varepsilon_{i,\tau}] = 0,
\qquad
\Var(\varepsilon_{i,\tau}) = \sigma^2_{\varepsilon_i}.
```

Volgens het model bestaat het rendement van het aandeel uit een vast deel $\alpha_i$
(hier een intercept op netto rendementen, geen afwijking van een evenwichtsmodel zoals de
Jensen-alpha), een deel dat via $\beta_{i,m}$ met de markt meebeweegt, en een residu. Bij
grote
aandelen ligt $\beta_{i,m}$ rond 1. De residuele volatiliteit $\sigma_{\varepsilon_i}$ is
in de
replicatiesteekproef hieronder (achteraf gekozen grote aandelen) gemiddeld 1,8%
per dag. Met
$\mathbf{X}_i = [\boldsymbol{\iota}\ \ \mathbf{r}_m]$, de $L_1 \times 2$-matrix
met een kolom enen ($\boldsymbol{\iota}$) en de marktrendementen, zijn de
OLS-schatters van $\mathbf{b}_i = (\alpha_i, \beta_{i,m})'$ en van de
restvariantie

$$
\hat{\mathbf{b}}_i = (\mathbf{X}_i'\mathbf{X}_i)^{-1}\mathbf{X}_i'\mathbf{r}_i,
\qquad
\hat\sigma^2_{\varepsilon_i} = \frac{1}{L_1 - 2}\,
(\mathbf{r}_i - \mathbf{X}_i\hat{\mathbf{b}}_i)'(\mathbf{r}_i - \mathbf{X}_i\hat{\mathbf{b}}_i).
$$

### Het kernresultaat: de ruis in een abnormaal rendement

*Waarom zou dit waar zijn?* Een onderzoeker die $\alpha_i$ en $\beta_{i,m}$ te hoog
schat, trekt op elke eventdag te veel af, en die fout is op alle eventdagen dezelfde.
Bij het optellen van de dagen telt de fout dus $L_2$ keer mee, zodat de variantie van
het CAR meer dan evenredig met het venster stijgt.

Het abnormale rendement is het werkelijke rendement min wat het geschatte marktmodel
voorspelt, zodat het ook de fout in $\hat{\mathbf{b}}_i$ bevat. Over het eventvenster is
het

```{math}
:label: eq-eventstudies-ar
\widehat{\mathbf{ar}}^*_i = \mathbf{r}^*_i - \mathbf{X}^*_i \hat{\mathbf{b}}_i
= \boldsymbol{\varepsilon}^*_i - \mathbf{X}^*_i\bigl(\hat{\mathbf{b}}_i - \mathbf{b}_i\bigr).
```

Hier is $\mathbf{X}^*_i$ dezelfde matrix als $\mathbf{X}_i$, maar dan met de
marktrendementen van het eventvenster. Onder de nulhypothese dat het event geen effect
heeft, is het abnormale rendement dus de ruis van de eventdagen min de schattingsfout.

:::{prf:theorem} Verdeling van abnormale rendementen
:label: thm-eventstudies-ar

Stel dat de storingen $\varepsilon_{i,\tau}$ onafhankelijk en normaal verdeeld
zijn, onafhankelijk van de marktrendementen. Dan geldt onder de nulhypothese,
conditioneel op $\mathbf{X}_i$ en $\mathbf{X}^*_i$,

```{math}
:label: eq-eventstudies-arvar
\widehat{\mathbf{ar}}^*_i \sim \mathcal{N}\bigl(\mathbf{0},\ \mathbf{V}_i\bigr),
\qquad
\mathbf{V}_i = \sigma^2_{\varepsilon_i}\Bigl(\mathbf{I} + \mathbf{X}^*_i(\mathbf{X}_i'\mathbf{X}_i)^{-1}\mathbf{X}^{*\prime}_i\Bigr).
```
:::

De variantie bestaat uit de ruis van de eventdagen, de term met $\mathbf{I}$, plus de
schattingsfout. Omdat die fout op alle eventdagen tegelijk zit, zijn de abnormale
rendementen onderling gecorreleerd.

:::{prf:proof}
Uit $\hat{\mathbf{b}}_i - \mathbf{b}_i =
(\mathbf{X}_i'\mathbf{X}_i)^{-1}\mathbf{X}_i'\boldsymbol{\varepsilon}_i$ volgt dat
$\widehat{\mathbf{ar}}^*_i$ lineair is in de normale vectoren
$\boldsymbol{\varepsilon}^*_i$ en $\boldsymbol{\varepsilon}_i$, dus normaal met
verwachting nul. Omdat de vensters niet overlappen, zijn de twee vectoren onafhankelijk
(daar werkt de aanname van onafhankelijke storingen over de tijd), zodat de kruistermen
verdwijnen:
$\Var(\widehat{\mathbf{ar}}^*_i) = \sigma^2_{\varepsilon_i}\mathbf{I} +
\mathbf{X}^*_i\,\Var(\hat{\mathbf{b}}_i)\,\mathbf{X}^{*\prime}_i$, met
$\Var(\hat{\mathbf{b}}_i) = \sigma^2_{\varepsilon_i}(\mathbf{X}_i'\mathbf{X}_i)^{-1}$.
$\square$
:::

Het CAR is de som over het venster,
$\widehat{\text{CAR}}_i = \boldsymbol{\iota}'\widehat{\mathbf{ar}}^*_i$, met
variantie $\sigma^2_{\text{CAR},i} = \boldsymbol{\iota}'\mathbf{V}_i\boldsymbol{\iota}$.
Voor het
marktmodel heeft die variantie een gesloten vorm.

:::{prf:proposition} Variantie van het CAR in het marktmodel
:label: thm-eventstudies-varcar

Laat $\hat\mu_m$ en $S_{mm} = \sum_{\tau}(r_{m,\tau} - \hat\mu_m)^2$ het gemiddelde
en de kwadratensom van de markt in het schattingsvenster zijn, en $S^*_m$ de som
van de markt in het eventvenster. Dan is

```{math}
:label: eq-eventstudies-varcar
\sigma^2_{\text{CAR},i}
= \sigma^2_{\varepsilon_i}\left[\,L_2
+ \underbrace{\frac{L_2^2}{L_1}}_{\text{fout in }\hat\alpha_i}
+ \underbrace{\frac{\bigl(S^*_m - L_2\hat\mu_m\bigr)^2}{S_{mm}}}_{\text{fout in }\hat\beta_{i,m}}
\,\right].
```
:::

De ruis groeit dus met $L_2$, de fout in $\hat\alpha_i$ met $L_2^2$ en de fout in
$\hat\beta_{i,m}$ met het kwadraat van wat de markt in het eventvenster van normaal
afwijkt. Dit is het recept uit het toy-voorbeeld, waar het $3 + 9/5 + 1/10 = 4{,}9$ gaf
in plaats van 3.

:::{prf:proof}
:class: dropdown

Schrijf $\mathbf{g} = \mathbf{X}^{*\prime}_i\boldsymbol{\iota} = (L_2,\ S^*_m)'$.
Dan is $\boldsymbol{\iota}'\mathbf{V}_i\boldsymbol{\iota} =
\sigma^2_{\varepsilon_i}\bigl(L_2 + \mathbf{g}'(\mathbf{X}_i'\mathbf{X}_i)^{-1}\mathbf{g}\bigr)$.
Voor een regressie op een constante en één regressor is
$\det(\mathbf{X}_i'\mathbf{X}_i) = L_1\sum r_{m,\tau}^2 - L_1^2\hat\mu_m^2 = L_1 S_{mm}$, en

$$
(\mathbf{X}_i'\mathbf{X}_i)^{-1}
= \frac{1}{L_1 S_{mm}}
\begin{pmatrix} \sum r_{m,\tau}^2 & -L_1\hat\mu_m \\ -L_1\hat\mu_m & L_1 \end{pmatrix}.
$$

Voor een vector $(g_1, g_2)'$ volgt, met $\sum r_{m,\tau}^2 = S_{mm} + L_1\hat\mu_m^2$,

$$
(g_1,g_2)(\mathbf{X}_i'\mathbf{X}_i)^{-1}(g_1,g_2)'
= \frac{g_1^2 S_{mm} + L_1(g_1\hat\mu_m - g_2)^2}{L_1 S_{mm}}
= \frac{g_1^2}{L_1} + \frac{(g_2 - g_1\hat\mu_m)^2}{S_{mm}} .
$$

Met $g_1 = L_2$ en $g_2 = S^*_m$ volgt [](#eq-eventstudies-varcar). $\square$
:::

Bij $L_2 = 21$ en $L_1 = 250$ voegt de term $L_2^2/L_1$ 8% toe bovenop de
ruisterm $L_2$, want $(L_2^2/L_1)/L_2 = 21/250$. Bij het jaarvenster van 250 dagen
in de replicatie, met $L_1 \approx 500$, is dat $250/500 = 50\%$. Zonder die term zijn de
$t$-waarden dus te hoog, en des te meer
naarmate het venster langer is.

### Wat het voorspelt: de toets en zijn kracht

Middelen over events maakt de toets scherper, en een langer venster maakt hem botter.
Een onderzoeker die $N$ onafhankelijke events middelt, laat het signaal staan en deelt
de variantie van de ruis door $N$, terwijl elke extra dag in het venster ruis toevoegt
zonder signaal.

Het gemiddelde CAR (het CAAR) en zijn variantie zijn

$$
\overline{\text{CAR}} = \frac{1}{N}\sum_{i=1}^N \widehat{\text{CAR}}_i,
\qquad
\bar\sigma^2 = \frac{1}{N^2}\sum_{i=1}^N \sigma^2_{\text{CAR},i} ,
$$

waarbij de variantie alleen klopt als de CAR's onafhankelijk zijn over events. De
toetsstatistiek (bij {cite:t}`MacKinlay1997` heet ze $\theta_1$) is

```{math}
:label: eq-eventstudies-j1
J_1 = \frac{\overline{\text{CAR}}}{\sqrt{\hat{\bar\sigma}^2}}
\ \xrightarrow{d}\ \mathcal{N}(0,1).
```

$J_1$ is dus een gewone $t$-waarde, het CAAR gedeeld door zijn standaardfout. In het
voorbeeld van MacKinlay, 600 winstaankondigingen van Dow Jones-bedrijven, geeft
goed nieuws op dag 0 een abnormaal rendement van 0,965% met $J_1 = 9{,}28$
(zijn tabel 1).

Omdat $J_1$ de variantie uit het schattingsvenster gebruikt, is die variantie te klein
als het event de koers onrustiger maakt, zoals bij een overnamebod, en dan verwerpt
$J_1$ te vaak. {cite:t}`BoehmerMusumeciPoulsen1991` (BMP) schatten de noemer daarom uit
de doorsnede, dus uit hoe sterk de CAR's van de $N$ events in het eventvenster zelf van
elkaar verschillen. Ze delen elk CAR eerst door zijn eigen standaardfout, zoals
{cite:t}`Patell1976`, wat $\text{SCAR}_i =
\widehat{\text{CAR}}_i/\hat\sigma_{\text{CAR},i}$ geeft. De toets wordt dan

```{math}
:label: eq-eventstudies-bmp
t_{\text{BMP}} = \frac{\overline{\text{SCAR}}}{s_{\text{SCAR}}/\sqrt{N}},
\qquad
s^2_{\text{SCAR}} = \frac{1}{N-1}\sum_{i=1}^N\bigl(\text{SCAR}_i - \overline{\text{SCAR}}\bigr)^2 .
```

$t_{\text{BMP}}$ is een gewone $t$-toets op de gestandaardiseerde CAR's, zodat een door
het event verhoogde variantie vanzelf in $s_{\text{SCAR}}$ verschijnt. Standaardiseren
geeft bovendien de zeer volatiele aandelen minder gewicht, terwijl die aandelen in $J_1$
de noemer domineren. Daarom ligt BMP in de replicatie iets hoger, op 4,7 tegen 4,0.

Hoe vaak vindt $J_1$ een echt effect? Stel dat elk event op $\tau = 0$ een
abnormaal rendement $a$ heeft, dat alle aandelen residuele volatiliteit
$\sigma_\varepsilon$ hebben en dat $L_1$ groot is. Dan is $J_1 \approx \mathcal{N}(\delta, 1)$
met

```{math}
:label: eq-eventstudies-power
\delta = \frac{\sqrt{N}\,a}{\sigma_\varepsilon\sqrt{L_2}},
\qquad
\text{kracht}(\delta) = \Phi(\delta - 1{,}96) + \Phi(-\delta - 1{,}96),
```

met $\Phi$ de standaardnormale verdelingsfunctie. De kracht stijgt dus met de wortel van
het aantal events en daalt met de wortel van de vensterlengte. Met $\sigma_\varepsilon =
2\%$, $a = 1\%$, $L_2 = 1$ en $N = 20$ is $\delta = 2{,}24$ en de kracht 61%, maar met
een venster van drie dagen zakt $\delta$ naar $1{,}29$ en de kracht naar 25%. Zo vindt
de toets, zoals we in de intuïtie verwachtten, een effect van 1% met enkele tientallen
events, zolang de dag bekend is. Een venster van $L_2$ dagen vraagt $L_2$ keer zoveel
events voor dezelfde kracht.

De vensterlengte hangt ook samen met de *halfwaardetijd* van informatie, het aantal
perioden na het event waarna de helft van de uiteindelijke prijsreactie binnen is. Die
halfwaardetijd is nooit kleiner te meten dan de resolutie van de data, zodat met
maanddata "hooguit een maand" het beste antwoord is. Met transactiedata vonden
{cite:t}`PatellWolfson1984` een eerste reactie op winst- en dividendberichten
binnen enkele minuten. Bij aandelen die live op CNBC werden besproken, reageerden
koersen binnen seconden, en was positief nieuws binnen een minuut verwerkt
{cite}`BusseGreen2002`. Bij elke
verfijning van de meetlat lag de halfwaardetijd onder de nieuwe resolutie. Met
de dagdata van de replicatie is "binnen een dag" dus het scherpste antwoord dat
we zelf kunnen geven.

### Hoe het faalt: events op dezelfde dag

Als events op dezelfde dag vallen, vindt de toets te vaak een effect. Het delen door $N$
veronderstelt namelijk dat de ruis van het ene event niets zegt over die van het andere.
Vallen honderd bankevents op dezelfde dag, dan delen ze het sectornieuws van die dag,
zodat het gemiddelde van die ruis niet meer met $N$ krimpt.

:::{prf:proposition} Variantie van een gemiddelde onder correlatie
:label: thm-eventstudies-cluster

Laat $x_1, \dots, x_N$ gelijke variantie $v$ en een gemeenschappelijke
verwachting hebben, met gemiddelde paarsgewijze correlatie
$\bar\rho = \frac{2}{N(N-1)}\sum_{i<j}\Corr(x_i, x_j)$. Dan

```{math}
:label: eq-eventstudies-cluster
\Var(\bar x) = \frac{v}{N}\bigl(1 + (N-1)\bar\rho\bigr),
\qquad
\E\Bigl[\tfrac{1}{N-1}\textstyle\sum_i (x_i - \bar x)^2\Bigr] = v(1-\bar\rho).
```
:::

Correlatie vergroot de variantie van het gemiddelde dus met factor $1 + (N-1)\bar\rho$.
Tegelijk verkleint ze de spreiding in de doorsnede met factor $1 - \bar\rho$, omdat
gedeelde ruis alle events dezelfde kant op duwt.

:::{prf:proof}
$\Var(\bar x) = N^{-2}\bigl(Nv + N(N-1)v\bar\rho\bigr)$. Verder is
$\E\sum_i(x_i-\bar x)^2 = Nv - N\Var(\bar x) = (N-1)v(1-\bar\rho)$.
$\square$
:::

Een toets die $\bar\rho$ negeert, heeft onder de nulhypothese een
standaarddeviatie van $\sqrt{1 + (N-1)\bar\rho}$ in plaats van één. Bij $N = 50$ en
$\bar\rho = 0{,}05$ is dat $1{,}86$. Een nominale toets van 5% verwerpt dan in
$2\Phi(-1{,}96/1{,}86) = 29\%$ van de gevallen, en meer events maken dat erger.

BMP lost het probleem niet op, want de noemer van die toets schat de variantie in de
doorsnede. Volgens de tweede formule van de propositie is die variantie een factor
$1 - \bar\rho$ te klein, bij $\bar\rho = 0{,}05$ dus 0,95 keer de waarde zonder
correlatie. Omdat BMP door te weinig deelt, is de $t$-waarde bij $N = 50$ niet 1,86 maar
$1{,}86/\sqrt{0{,}95} \approx 1{,}91$ keer te breed verdeeld, zodat die toets nog vaker
verwerpt. Daarom corrigeerden {cite:t}`KolariPynnonen2010` BMP met beide factoren:

```{math}
:label: eq-eventstudies-kp
t_{\text{KP}} = t_{\text{BMP}}\sqrt{\frac{1-\hat{\bar\rho}}{1 + (N-1)\hat{\bar\rho}}},
```

met $\hat{\bar\rho}$ de gemiddelde correlatie tussen de residuen in het
schattingsvenster. De $t$-waarde krimpt dus naarmate de events meer ruis delen. Omdat
events op verschillende dagen geen ruis delen, wegen we de correlatie in de replicatie
met de kalenderoverlap van de vensters.

### Hoe het faalt: de lange horizon

*Waarom zou dit waar zijn?* Een onderzoeker die het normale rendement elke dag
twee basispunten te laag schat, ziet over drie dagen niets. Over drie jaar (750
handelsdagen) loopt die fout op tot 15%,
terwijl de ruis maar met de wortel van de horizon groeit, zodat de fout het van de ruis
wint.

Mist het model het verwachte rendement elke dag met $\eta$, de modelfout, dan
heeft een CAAR over een eventvenster van $L_2$ dagen een bias $L_2\eta$. Omdat de
standaardfout bij onafhankelijke events $\sigma_\varepsilon\sqrt{L_2/N}$ is, wordt de
verwachte $t$-waarde zonder echt effect

$$
\E[J_1] \approx \frac{L_2\eta}{\sigma_\varepsilon\sqrt{L_2/N}} = \sqrt{NL_2}\ \frac{\eta}{\sigma_\varepsilon}.
$$

Met $\eta = 0{,}02\%$ per dag, $\sigma_\varepsilon = 2\%$ en $N = 100$ is dat $0{,}17$ bij
$L_2 = 3$ en $2{,}7$ bij $L_2 = 750$, een "significant" effect dat volledig uit het model
komt. Dit
*bad model problem* (een uitkomst die het benchmarkmodel meet in plaats van het event)
is de joint hypothesis van [het vorige college](#02-06-efficiente-markten) in de meest
concrete vorm. Volgens {cite:t}`BarberLyon1997` vallen lange-horizontoetsen tegen een
marktindex bovendien scheef uit, en daarom vergeleken zij met bedrijven van dezelfde
grootte en boek-marktwaardeverhouding. {cite:t}`KothariWarner2007` concluderen dat korte
event studies goed werken, maar dat lange gevoelig blijven voor het model.

```{admonition} Samengevat
:class: tip

- De variantie van een CAR is ruis plus schattingsfout,
  [](#eq-eventstudies-varcar). Een langer schattingsvenster $L_1$ verkleint de
  schattingsfout, een langer eventvenster $L_2$ vergroot beide. Hoe verder de
  markt in het eventvenster van normaal afwijkt, hoe zwaarder de fout in de bèta.

- De kracht van $J_1$ stijgt met $\sqrt{N}$ en met het effect $a$, en daalt met
  $\sqrt{L_2}$ en de residuele volatiliteit $\sigma_\varepsilon$, [](#eq-eventstudies-power).

- Events op dezelfde dag vergroten de variantie van het CAAR met
  $1 + (N-1)\bar\rho$, [](#eq-eventstudies-cluster), en meer events maken dat erger.

- Een modelfout groeit met de vensterlengte $L_2$ en de ruis met $\sqrt{L_2}$, zodat
  lange event studies het model meten.

- De halfwaardetijd is niet kleiner te meten dan de resolutie van de data, zodat met
  dagdata "binnen een dag" het scherpste antwoord is.

- De simulatie hierna meet hoe vaak $J_1$ een effect van 1% vindt bij een gegeven aantal
  events en vensterlengte.
```

## Simulatie: toetskracht zoals Brown en Warner

Met een eendaags venster vindt $J_1$ een effect van 1% bij 20 events in 63% van de
steekproeven, zoals [](#eq-eventstudies-power) voorspelt. Met een venster van 21 dagen
mist hij hetzelfde effect zelfs bij 100 events in vier van de vijf steekproeven.

{cite:t}`BrownWarner1980,BrownWarner1985` maten hoe goed event-study-methoden werken
door in echte rendementen op willekeurige datums een bekend abnormaal rendement te
injecteren en te tellen hoe vaak een toets het vond. Met dagdata en 50 aandelen vond het
marktmodel een effect van 1% op dag 0 in 80,4% van de steekproeven, maar verspreid over
de elf dagen van $-5$ tot $+5$ was dat nog 13,2% {cite}`BrownWarner1985`. Wij simuleren
in plaats daarvan, zodat we elke eigenschap van de data zelf kiezen.

We willen weten hoe vaak $J_1$ de nulhypothese verwerpt, als functie van het aantal
events $N$, de vensterlengte en de grootte van het effect. Het datagenererende proces
volgt daarvoor de eigenschappen van dagrendementen die voor de toets van belang zijn:

| eigenschap | waarde |
|---|---|
| dagvolatiliteit markt | 1% |
| residuele dagvolatiliteit | 2% (replicatie: 1,8%) |
| verdeling van schokken | $t$ met vier vrijheidsgraden, eenheidsvariantie |
| bèta's | uniform tussen 0,5 en 1,5 |
| schattingsvenster $L_1$ | 250 dagen |
| events | op verschillende kalenderdagen ($\rho = 0$) |
| normaal rendement boven de markt | 0,03% per dag, door de alpha weggefilterd |

De functie hieronder simuleert abnormale rendementen zonder effect, inclusief de
schattingsfout van het marktmodel. De markt heeft vorm `(r, 1, T)` omdat alle
events van één steekproef dezelfde marktdagen delen. Met `rho > 0` delen ze ook
residuele ruis, zoals in [](#thm-eventstudies-cluster), maar hier staat `rho` op nul.
De replicaties lopen in blokken van 250 om het geheugengebruik te beperken. De tweede
functie voegt een effect toe op dag 0
en berekent $J_1$ volgens [](#eq-eventstudies-j1).

```{code-cell} ipython3
def t_shocks(size, df=4):
    """Unit-variance Student-t draws (fat tails like daily returns)."""
    return rng.standard_t(df, size) * np.sqrt((df - 2) / df)


def simulate_events(reps, n_events, rho=0.0, L1=250, half=10, sig_m=0.01, sig_e=0.02,
                    chunk=250):
    """Null abnormal returns from an estimated market model, in chunks of replications.

    rho is the share of residual variance that all events share (0 = different days).
    Returns event-window abnormal returns (reps, N, 2*half+1) and what Var(CAR) needs.
    """
    T = L1 + 2 * half + 1
    out = {k: [] for k in ("ar", "s2", "m_evt", "m_bar", "s_mm")}
    for start in range(0, reps, chunk):
        r = min(chunk, reps - start)
        market = sig_m * t_shocks((r, 1, T))
        beta = rng.uniform(0.5, 1.5, (1, n_events, 1))
        resid = np.sqrt(1 - rho) * sig_e * t_shocks((r, n_events, T))
        resid += np.sqrt(rho) * sig_e * t_shocks((r, 1, T))
        R = 0.0003 + beta * market + resid   # 0.03% a day of normal return (the alpha)
        m_est, R_est = market[..., :L1], R[..., :L1]
        m_bar = m_est.mean(-1, keepdims=True)
        s_mm = ((m_est - m_bar) ** 2).sum(-1, keepdims=True)
        R_dev = R_est - R_est.mean(-1, keepdims=True)
        b = ((m_est - m_bar) * R_dev).sum(-1, keepdims=True) / s_mm
        a = R_est.mean(-1, keepdims=True) - b * m_bar
        out["ar"].append(R[..., L1:] - a - b * market[..., L1:])
        out["s2"].append(((R_est - a - b * m_est) ** 2).sum(-1) / (L1 - 2))
        out["m_evt"].append(market[:, 0, L1:])
        out["m_bar"].append(m_bar[:, 0, 0])
        out["s_mm"].append(s_mm[:, 0, 0])
    sim = {k: np.concatenate(v) for k, v in out.items()}
    sim.update(L1=L1, half=half)
    return sim


def j1_test(sim, lo, hi, a=0.0, n=None):
    """J1 for event window [lo, hi] over the first n events, with abnormal return a on day 0."""
    h, L1 = sim["half"], sim["L1"]
    n = n or sim["ar"].shape[1]
    window = slice(h + lo, h + hi + 1)
    L2 = hi - lo + 1
    car = sim["ar"][:, :n, window].sum(-1) + (a if lo <= 0 <= hi else 0.0)
    S_m = sim["m_evt"][:, window].sum(-1)
    factor = L2 + L2**2 / L1 + (S_m - L2 * sim["m_bar"]) ** 2 / sim["s_mm"]
    var = sim["s2"][:, :n] * factor[:, None]
    return car.sum(1) / np.sqrt(var.sum(1))
```

We simuleren 1000 steekproeven van 100 events en gebruiken daarvan de eerste $N$.
Per combinatie van $N$, venster en effect tellen we hoe vaak $|J_1| > 1{,}96$.

```{code-cell} ipython3
sim0 = simulate_events(reps=1000, n_events=100)

sizes_N = [5, 10, 20, 50, 100]
windows = {"[0,0]": (0, 0), "[-1,+1]": (-1, 1), "[-5,+5]": (-5, 5), "[-10,+10]": (-10, 10)}
effects = [0.0, 0.005, 0.01, 0.02]
rows = []
for w, (lo, hi) in windows.items():
    for n in sizes_N:
        for a in effects:
            J1_sim = j1_test(sim0, lo, hi, a, n)
            rows.append({"venster": w, "N": n, "AR dag 0": a,
                         "verwerping": np.mean(np.abs(J1_sim) > 1.96)})
power = pd.DataFrame(rows)
power.pivot_table(index=["venster", "N"], columns="AR dag 0", values="verwerping",
                  sort=False).round(3)
```

De tabel bevestigt [](#eq-eventstudies-power). Bij $N = 20$, $a = 1\%$ en een
eendaags venster is de kracht 62,9%, tegen 61% uit de formule. Een effect van 2%,
zo groot als het CAAR in het toy-voorbeeld, vindt de toets dan in 99,2% van de
steekproeven. De schattingsfout die in het toy-voorbeeld de variantie met 63%
verhoogde (4,9 tegen 3), is hier met $L_1 = 250$ en één dag verwaarloosbaar, want ze voegt
maar 0,4% toe.

In de figuur staat elk venster in een eigen paneel, zodat te zien is hoe de lijnen naar
rechts verschuiven als het venster langer wordt.

```{code-cell} ipython3
:label: cel-eventstudies-kracht
:tags: [hide-input]

fig, axes = plt.subplots(1, 4, figsize=(11, 3.6), sharey=True)
for ax, w in zip(axes, windows):
    sub = power[power["venster"] == w]
    for a in effects[1:]:
        s = sub[sub["AR dag 0"] == a]
        ax.plot(s["N"], s["verwerping"], marker="o", label=f"AR = {a:.1%}")
    s = sub[sub["AR dag 0"] == 0.0]
    ax.plot(s["N"], s["verwerping"], color="black", ls=":", marker=".", label="geen effect")
    ax.axhline(0.05, color="grey", lw=0.8)
    ax.set_xscale("log")
    ax.set_title(f"Venster {w}")
    ax.set_xlabel("Aantal events N")
axes[0].set_ylabel("Verwerpingsfrequentie (5%-toets)")
axes[-1].legend(loc="lower right")
fig.suptitle("Toetskracht van $J_1$: meer events helpt, een langer venster kost", x=0.01, ha="left")
plt.show()
```

:::{figure} #cel-eventstudies-kracht
:label: fig-eventstudies-kracht
:width: 100%

Toetskracht van $J_1$ in 1000 gesimuleerde steekproeven. Met een venster van één
dag vindt de toets een effect van 1% al in de meeste steekproeven met 20 events.
Met een venster van 21 dagen mist hij datzelfde effect zelfs met 100 events in
vier van de vijf steekproeven. De stippellijn (geen effect) blijft rond 5%, wat betekent dat de toets ook met dikke
staarten goed gespecificeerd is.
:::

Zonder effect ligt de verwerpingsfrequentie overal tussen 3,5 en 6%. Op één cel na
valt dat binnen de simulatieruis van
$1{,}96\sqrt{0{,}05 \times 0{,}95/1000} \approx 1{,}4$ procentpunt, en bij twintig
cellen is één uitschieter te verwachten. Bij $N = 50$ en een eendaags venster, de
opzet van Brown en Warner, vindt onze toets een effect van 1% in 94,7% van de
steekproeven, tegen hun 80,4%. Het verschil zit in hun steekproef van willekeurig gekozen
aandelen,
die gemiddeld volatieler zijn dan de 2% van de simulatie. Met een bekende eventdag is de
toets scherp. Is de dag maar op
een week bekend, dan zijn vijf keer zoveel events nodig.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Fama, Fisher, Jensen en Roll, *The Adjustment of Stock Prices to New
Information*, International Economic Review 1969 {cite}`FamaFisherJensenRoll1969`.

**Wat.** Hun figuur van het cumulatieve gemiddelde residu (bij ons het CAAR) in de
maanden rond de maand waarin een splitsing ingaat, voor alle splitsingen samen.

**Data hier.** Dagrendementen van 50 grote Amerikaanse aandelen met 102
splitsingen tussen 2004 en 2025, via `hap.data.yahoo(...)`, en de dagelijkse
CRSP-marktportefeuille uit de French-bibliotheek. De splitsingsdatums staan als
lijst in de code.

**Verschil met het origineel.** FFJR gebruikten maanddata van 940
NYSE-splitsingen uit 1927–1959, en wij gebruiken dagdata, een eventvenster van $-250$ tot $+60$
dagen en een marktmodel geschat op tot 250 dagen aan elke kant van dat venster. Onze aandelen zijn
gekozen omdat ze *nu* groot zijn, een selectie achteraf die de stijging vóór de
splitsing opdrijft.

**Verwachte afwijking.** De vorm moet gelijk zijn, met een CAAR dat over het jaar vóór de ex-datum positief en
significant is, een abnormaal rendement van nul op de ex-datum en daarna geen
significante drift ($|t| < 2$). Door de selectie achteraf
ligt de stijging vooraf waarschijnlijk hoger dan bij FFJR, en daarom is hun figuur de
maatstaf voor de vorm en niet voor het niveau.
```

De code begint met de lijst met splitsingen,
waarin elke regel de vorm `ticker:ex-datum:ratio` heeft en de ex-datum dag 0 is.

```{code-cell} ipython3
# Ex-dates and ratios (>= 3:2) from the Yahoo Finance split history
# (yfinance.Ticker.splits, retrieved 2026-09-12); hap.data.yahoo returns no corporate
# actions. Spin-off adjustments with ratios such as 1.05 or 1.32 are left out.
SPLITS = """
NFLX:2004-02-12:2/1 APH:2004-03-30:2/1 ODFL:2004-05-21:3/2 DHR:2004-05-21:2/1
PG:2004-06-21:2/1 QCOM:2004-08-16:2/1 BAC:2004-08-30:2/1 GILD:2004-09-07:2/1
CVX:2004-09-13:2/1 AAPL:2005-02-28:2/1 WRB:2005-04-11:3/2 ADBE:2005-05-24:2/1
UNH:2005-05-31:2/1 ORLY:2005-06-16:2/1 MNST:2005-08-09:2/1 SBUX:2005-10-24:2/1
FAST:2005-11-14:2/1 ODFL:2005-12-01:3/2 WRB:2006-04-05:3/2 NVDA:2006-04-07:2/1
MNST:2006-07-10:4/1 WFC:2006-08-14:2/1 CSX:2006-08-16:2/1 APH:2007-04-02:2/1
NKE:2007-04-03:2/1 GILD:2007-06-25:2/1 NVDA:2007-09-11:3/2 IDXX:2007-11-27:2/1
DE:2007-12-04:2/1 UNP:2008-05-29:2/1 BRK-B:2010-01-21:50/1 EW:2010-05-28:2/1
DHR:2010-06-14:2/1 ODFL:2010-08-24:3/2 TSCO:2010-09-03:2/1 FAST:2011-05-23:2/1
FTNT:2011-06-02:2/1 CSX:2011-06-16:3/1 ROST:2011-12-16:2/1 TJX:2012-02-03:2/1
MNST:2012-02-16:2/1 CPRT:2012-03-29:2/1 KO:2012-08-13:2/1 ODFL:2012-09-10:3/2
NKE:2012-12-26:2/1 GILD:2013-01-28:2/1 CRM:2013-04-18:4/1 TSCO:2013-09-27:2/1
MA:2014-01-22:10/1 AAPL:2014-06-09:7/1 UNP:2014-06-09:2/1 APH:2014-10-10:2/1
V:2015-03-19:4/1 SBUX:2015-04-09:2/1 ROST:2015-06-12:2/1 IDXX:2015-06-16:2/1
NFLX:2015-07-15:7/1 EW:2015-12-14:2/1 NKE:2015-12-24:2/1 MNST:2016-11-10:3/1
CPRT:2017-04-11:2/1 ISRG:2017-10-06:3/1 TJX:2018-11-07:2/1 WRB:2019-04-03:3/2
FAST:2019-05-23:2/1 ODFL:2020-03-25:3/2 EW:2020-06-01:3/1 AAPL:2020-08-31:4/1
TSLA:2020-08-31:5/1 APH:2021-03-05:2/1 SHW:2021-04-01:3/1 CSX:2021-06-29:3/1
NVDA:2021-07-20:4/1 ISRG:2021-10-05:3/1 ANET:2021-11-18:4/1 WRB:2022-03-24:3/2
AMZN:2022-06-06:20/1 DXCM:2022-06-13:4/1 FTNT:2022-06-23:5/1 GOOGL:2022-07-18:20/1
TSLA:2022-08-25:3/1 PANW:2022-09-14:3/1 CPRT:2022-11-04:2/1 MNST:2023-03-28:2/1
CPRT:2023-08-22:2/1 WMT:2024-02-26:3/1 ODFL:2024-03-28:2/1 NVDA:2024-06-10:10/1
APH:2024-06-12:2/1 CMG:2024-06-26:50/1 WRB:2024-07-11:3/2 AVGO:2024-07-15:10/1
CTAS:2024-09-12:4/1 SMCI:2024-10-01:10/1 LRCX:2024-10-03:10/1 ANET:2024-12-04:4/1
PANW:2024-12-16:2/1 TSCO:2024-12-20:5/1 FAST:2025-05-22:2/1 ORLY:2025-06-10:15/1
NFLX:2025-11-17:10/1 NOW:2025-12-18:5/1
"""
events = pd.DataFrame([tok.split(":") for tok in SPLITS.split()],
                      columns=["ticker", "ex_date", "ratio"])
events["ex_date"] = pd.to_datetime(events["ex_date"])
tickers = sorted(events["ticker"].unique())
pd.Series({"splitsingen": len(events), "aandelen": len(tickers),
           "eerste ex-datum": f"{events['ex_date'].min():%Y-%m}",
           "laatste ex-datum": f"{events['ex_date'].max():%Y-%m}"})
```

Er zijn 102 splitsingen van 50 aandelen. Daarna laden we de koersen en het
marktrendement.

```{code-cell} ipython3
prices = hap_data.yahoo(tickers, start="2002-01-01", end="2026-08-01")
market = hap_data.market_daily()["Mkt"].loc["2002-01-03":"2026-07-31"]
returns = prices.pct_change(fill_method=None).reindex(market.index)
pd.Series({"handelsdagen": returns.shape[0], "eerste dag": f"{returns.index[0]:%Y-%m-%d}",
           "laatste dag": f"{returns.index[-1]:%Y-%m-%d}"})
```

De reeks beslaat 6183 handelsdagen. Voor echte data hebben we het marktmodel en het
recept als functies nodig, omdat elk event een eigen schattingsvenster heeft.

```{code-cell} ipython3
def fit_market_model(r, r_m):
    """OLS market model r = alpha + beta * r_m + e.

    Returns the coefficients, the residuals, the residual variance with L1 - 2
    degrees of freedom and (X'X)^{-1}, which drives the estimation-error term.
    """
    X = np.column_stack([np.ones(len(r_m)), r_m])
    xtx_inv = np.linalg.inv(X.T @ X)
    coef = xtx_inv @ X.T @ r
    resid = r - X @ coef
    return coef, resid, resid @ resid / (len(r) - 2), xtx_inv


def car_variance(s2, xtx_inv, r_m_event):
    """Var(CAR) = s2 * (L2 + g' (X'X)^{-1} g), g = column sums of the event-window X."""
    g = np.array([len(r_m_event), np.sum(r_m_event)])
    return s2 * (len(r_m_event) + g @ xtx_inv @ g)
```

`car_variance` is [](#eq-eventstudies-varcar) in matrixvorm. Per event schatten we
nu het marktmodel, net als FFJR buiten het eventvenster, met tot 250 dagen ervóór en 250
dagen erna. Een venster alleen vooraf zou de stijging vóór de splitsing als
normaal rendement meetellen, en zo een te hoge alpha geven. Daarna berekenen we de
abnormale rendementen over
$\tau = -250, \dots, +60$.

```{code-cell} ipython3
PRE, POST, EST = 250, 60, 250
tau = np.arange(-PRE, POST + 1)
dates = returns.index
r_m = market.to_numpy()

ar_rows, fits, resid_panel = [], [], np.full((len(dates), len(events)), np.nan)
for k, (ticker, ex_date) in enumerate(events[["ticker", "ex_date"]].itertuples(index=False)):
    r = returns[ticker].to_numpy()
    i0 = dates.searchsorted(ex_date)
    before = np.arange(max(i0 - PRE - EST, 0), i0 - PRE)
    after = np.arange(i0 + POST + 1, min(i0 + POST + 1 + EST, len(dates)))
    est = np.concatenate([before, after])
    est = est[np.isfinite(r[est])]
    coef, resid, s2, xtx_inv = fit_market_model(r[est], r_m[est])
    resid_panel[est, k] = resid
    window = np.arange(i0 - PRE, i0 + POST + 1)
    ar_rows.append(r[window] - coef[0] - coef[1] * r_m[window])
    fits.append({"ticker": ticker, "start": i0 - PRE, "L1": len(est), "beta": coef[1],
                 "sigma": np.sqrt(s2), "s2": s2, "xtx_inv": xtx_inv, "r_m": r_m[window]})

AR = np.array(ar_rows)
fit_table = pd.DataFrame(fits)[["ticker", "L1", "beta", "sigma"]]
fit_table.describe().loc[["mean", "min", "max"]].round(3)
```

Het schattingsvenster telt gemiddeld 495 dagen, de gemiddelde bèta is 1,08 en de
gemiddelde residuele volatiliteit 1,8% per dag. Vervolgens berekenen we het CAAR-pad en
zijn standaardfout, waarvoor we voor elke dag
$\tau$ de variantie van het CAR van $-250$ tot $\tau$ volgens
[](#eq-eventstudies-varcar) over de events optellen.

```{code-cell} ipython3
caar_path = AR.mean(axis=0).cumsum()
var_path = np.zeros(len(tau))
for f in fits:
    for k in range(len(tau)):   # Var of CAR(-250, tau_k) for this event
        var_path[k] += car_variance(f["s2"], f["xtx_inv"], f["r_m"][:k + 1])
se_path = np.sqrt(var_path) / len(fits)
caar_table = pd.DataFrame({"CAAR": caar_path, "SE": se_path}, index=pd.Index(tau, name="tau"))
caar_table.loc[[-121, -1, 0, 60]].round(4)
```

Op dag $-1$ is het CAAR 14,9% met standaardfout 3,7 procentpunt, en de figuur toont het
hele pad van dag $-250$ tot
$+60$.

```{code-cell} ipython3
:label: cel-eventstudies-caar
:tags: [hide-input]

fig, ax = plt.subplots()
ax.fill_between(tau, caar_path - 1.96 * se_path, caar_path + 1.96 * se_path,
                alpha=0.2, label="95%-band (onafhankelijke events)")
ax.plot(tau, caar_path, label="CAAR, 102 splitsingen 2004–2025")
ax.axvline(0, color="black", lw=0.8)
ax.axhline(0, color="grey", lw=0.8)
ax.set_xlabel("Handelsdagen ten opzichte van de ex-datum")
ax.set_ylabel("Cumulatief gemiddeld abnormaal rendement")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0%}"))
ax.set_title("Aandelensplitsingen: de koers stijgt vóór de splitsing, daarna niet meer")
ax.legend(loc="upper left")
plt.show()
```

:::{figure} #cel-eventstudies-caar
:label: fig-eventstudies-caar
:width: 90%

Cumulatief gemiddeld abnormaal rendement rond 102 splitsingen van grote
Amerikaanse aandelen. Het patroon is dat van FFJR, met een gestage stijging over het jaar vóór de splitsing en
geen voortgezette stijging erna. De band veronderstelt onafhankelijke events, en de
tabel hieronder controleert die aanname.
:::

Nu volgen de toetsen per venster. Voor Kolari-Pynnönen schatten we de residuele correlatie
tussen elk paar events op de dagen waarop hun schattingsvensters overlappen
(minimaal 100). Die correlatie telt alleen voor het deel van het eventvenster dat
beide events op dezelfde kalenderdagen hebben, en daarom wegen we de correlatie met dat
gedeelde deel. Bij het jaarvenster is dat ruim
90% voor twee events die een maand na elkaar vallen, en nul voor events die jaren uit
elkaar liggen.

```{code-cell} ipython3
resid_corr = pd.DataFrame(resid_panel).corr(min_periods=100).to_numpy(copy=True)
np.fill_diagonal(resid_corr, np.nan)
starts = np.array([f["start"] for f in fits])


def split_tests(lo, hi):
    """CAAR and J1 / BMP / Kolari-Pynnonen statistics over event window [lo, hi]."""
    cols = slice(lo + PRE, hi + PRE + 1)
    L2, n = hi - lo + 1, len(fits)
    car = AR[:, cols].sum(axis=1)
    var = np.array([car_variance(f["s2"], f["xtx_inv"], f["r_m"][cols]) for f in fits])
    scar = car / np.sqrt(var)
    first_day, last_day = starts + lo, starts + hi   # event windows in calendar days
    overlap = np.zeros((n, n))
    for i in range(n):   # share of the event window that event i shares with each other event
        shared_days = np.minimum(last_day[i], last_day) - np.maximum(first_day[i], first_day) + 1
        overlap[i] = np.clip(shared_days, 0, None) / L2
    weighted_corr = overlap * np.nan_to_num(resid_corr)
    rho = np.nansum(weighted_corr) / (n * (n - 1))   # average over all pairs
    bmp = scar.mean() / (scar.std(ddof=1) / np.sqrt(n))
    return {"venster": f"[{lo},{hi}]", "CAAR": car.mean(), "SE": np.sqrt(var.sum()) / n,
            "J1": car.mean() / (np.sqrt(var.sum()) / n), "BMP": bmp, "rho": rho,
            "KP": bmp * np.sqrt((1 - rho) / (1 + (n - 1) * rho)), "% positief": (car > 0).mean()}


windows_real = [(-250, -1), (-250, -121), (-120, -1), (-1, 1), (0, 0), (1, 60), (0, 60)]
table = pd.DataFrame([split_tests(lo, hi) for lo, hi in windows_real])
table.set_index("venster").round(4)
```

De tabel heeft de vorm die FFJR vonden. Hieronder staan onze getallen naast hun
figuur.

| | FFJR (hun figuur) | verwachting hier | hier | correlatie $\hat{\bar\rho}$ en KP |
|---|---|---|---|---|
| CAAR over het jaar vóór de splitsing | stijgt gestaag | positief, $\lvert t \rvert > 2$ | 14,9% (SE 3,7), $J_1 = 4{,}0$, BMP 4,74 | 0,0012, KP 4,47 |
| abnormaal rendement op de ex-datum | niet apart gemeten (maanddata) | nul | $-0{,}08\%$, $J_1 = -0{,}40$ | 0,0000, KP 0,05 |
| CAAR na de splitsing | vrijwel vlak | $\lvert t \rvert < 2$ | $-2{,}9\%$ over $[0,60]$ (SE 1,6), $J_1 = -1{,}84$, BMP $-1{,}18$ | 0,0003, KP $-1{,}16$ |

**Geslaagd.** De drie verwachtingen komen uit, want het CAAR is vooraf
significant positief, op de ex-datum nul en daarna zonder significante drift. Wie na de
splitsing koopt, verdient er dus niets extra mee.

Het CAAR van $-2{,}9\%$ na de splitsing is het waard om nog eens te bekijken. Het is
verenigbaar met geen drift, maar ook met een negatieve drift van enkele procenten, en
honderd events zijn te weinig om die twee te onderscheiden. Dat is hetzelfde probleem
als de standaardfout van 2% uit [het college over rendementen](#00-01-rendementen), maar
dan in eventtijd. De lange-horizonformule geeft nog een lezing, want een modelfout van
$\eta = -2{,}9\%/61 \approx -0{,}05\%$ per dag, ruim 10% per jaar, zou het hele
CAAR verklaren. Of zo'n modelfout plausibel is, komt hieronder terug bij de drift. FFJR
vonden alleen een daling na splitsingen zonder dividendverhoging, en concludeerden
dat een splitsing op zichzelf geen effect heeft zodra de dividendinformatie is
meegenomen:

> once the information effects of associated dividends are properly considered,
> a split per se has no net effect on common stock returns.

Bij onze getallen horen drie kanttekeningen. De eerste gaat over de selectie, de tweede
over de datum en de derde over de toets.

- De stijging vooraf is deels de reden voor de splitsing en deels onze selectie, want
  wie in 2026 grote aandelen kiest, kiest aandelen die sterk zijn gestegen.
- We meten rond de ex-datum en niet rond de aankondiging, die enkele weken eerder valt,
  zodat de informatie in $[-120, -1]$ zit. Voor aankondigingsdatums bestaat geen gratis
  bron.
- De geschatte correlatie tussen events is klein, omdat de splitsingen over twintig
  jaar verspreid liggen, zodat Kolari-Pynnönen de $t$-waarden van BMP in de tabel
  nauwelijks verlaagt.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De event study is een van de meest succesvolle
instrumenten van de empirische financiële economie. Ze maakte de semi-sterke vorm van
efficiëntie toetsbaar (prijzen weerspiegelen alle publieke informatie), en de uitkomst was
over een halve eeuw opvallend
consistent. Op korte horizon reageren prijzen snel en in de goede richting op
publiek nieuws, en daarna valt er weinig meer te verdienen. De splitsingen
hierboven tonen dat opnieuw, zestig jaar na FFJR. Het instrument verhuisde naar het recht
en de macro-economie, en
{cite:t}`EisfeldtSchubertZhang2023` maten er zelfs de waarde van generatieve AI mee, met
de lancering van ChatGPT als event. [Het college over LLM's](#07-37-llms-en-efficientie)
pakt die lijn weer op.

**Waar het breekt.** Het instrument breekt op de lange horizon. Latere studies vonden
*drift* (een abnormaal rendement dat na het event in dezelfde richting doorloopt) na
winstaankondigingen, emissies, inkoopprogramma's en splitsingen, en onze eigen tabel
laat na de ex-datum $-2{,}9\%$ zien, niet significant maar ook niet nul. Daar wreekt de
joint hypothesis zich, want de bias van een verkeerd model groeit lineair met de horizon
en de ruis alleen met de wortel. Een abnormaal rendement over drie jaar zegt dus
evenveel over het model als over de markt.

**Risico of vergissing?** De drift laat twee lezingen toe. In de Chicago-lezing (de school
van Fama, waarin verwachte rendementen met risico
variëren) is hij een beloning voor risico dat het marktmodel niet meet, omdat bedrijven
die splitsen of hun winst zien stijgen van risicoprofiel veranderen. Een beter model zou
de drift dan doen verdwijnen. In de Yale-lezing (de school van Shiller, waarin prijzen
ernaast kunnen zitten) is hij een vergissing, want beleggers reageren te traag op
nieuws, en arbitrage is te riskant of te duur om de koers in één keer recht te zetten.
Beide lezingen voorspellen hetzelfde CAR-patroon. Alleen een onomstreden model voor het
verwachte rendement zou ze kunnen scheiden, en zo'n model levert de event study niet.

**Wat er daarna kwam.** Een kandidaat voor zo'n model bestond al als theorie. Sharpe,
Lintner en Mossin leidden het af {cite}`Sharpe1964,Lintner1965,Mossin1966`, en Jensen
gebruikte het in 1968 om fondsen te beoordelen {cite}`Jensen1968`. Of bèta werkelijk het
verwachte rendement bepaalt, werd de vraag van het volgende decennium en van het college
over [het CAPM](#02-08-capm).

## Oefeningen

:::{exercise}
:label: ex-eventstudies-1

**Instap: een venster van één dag.** Neem het toy-voorbeeld, maar meet alleen op dag 0.
Het schattingsvenster en de geschatte alpha's en bèta's blijven gelijk.

1. Bereken met het recept de variantiefactor, het gemiddelde abnormale rendement
   en $J_1$ met de hand.
2. Het CAAR daalt van 2,0 naar 1,9. Waarom stijgt $J_1$ toch?
:::

:::{solution} ex-eventstudies-1
:class: dropdown

**(1)** Met $L_2 = 1$ en $S^*_m = -1$ is de factor $1 + 1/5 + 1/10 = 1{,}3$. De
varianties zijn $1{,}3 \times 0{,}3333 = 0{,}4333$ voor A en C en $0{,}65$ voor B.
Het gemiddelde abnormale rendement is $(1{,}9 + 2{,}0 + 1{,}8)/3 = 1{,}9$. Dan is
$J_1 = 1{,}9/\sqrt{1{,}5167/9} = 4{,}628$.

```{code-cell} ipython3
factor_0 = 1 + 1 / L1 + (m_evt[1] - m_est.mean()) ** 2 / S_mm
ar_0 = [R_evt[name][1] - alpha - beta * m_evt[1] for name, (alpha, beta, _) in toy_fits.items()]
var_0 = [factor_0 * s2 for (_, _, s2) in toy_fits.values()]
J1_day0 = np.mean(ar_0) / np.sqrt(sum(var_0) / N**2)
pd.Series({"factor": factor_0, "gemiddeld AR(0)": np.mean(ar_0), "J1": J1_day0}).round(3)
```

**(2)** Het signaal zat op dag 0. De dagen $-1$ en $+1$ voegen samen maar 0,1 aan
signaal toe, terwijl elk van die dagen een volle dag ruis plus schattingsfout meebrengt.
Een kort venster rond een bekende dag is dus de sterkste toets, zoals
[](#eq-eventstudies-power) voorspelt.
:::

:::{exercise}
:label: ex-eventstudies-2

**Afleiding: de prijs van het vergeten van de schattingsfout.** In het toy-voorbeeld was
de naïeve $t$-waarde daardoor te hoog. Deze oefening zoekt de algemene vorm.

1. Leid voor het *constant-mean*-model $r_{i,\tau} = \mu_i + \varepsilon_{i,\tau}$
   (een model zonder markt, alleen een eigen gemiddelde) af dat
   $\Var(\widehat{\text{CAR}}_i) = \sigma^2_{\varepsilon_i}(L_2 + L_2^2/L_1)$.
2. Laat zien dat de naïeve toets, die $L_2\sigma^2$ gebruikt, een werkelijke
   standaarddeviatie van $\sqrt{1 + L_2/L_1}$ heeft. Bereken het werkelijke
   significantieniveau van een nominale 5%-toets voor $L_2 = 21$ en
   $L_1 = 60$, $120$, $250$.
:::

:::{solution} ex-eventstudies-2
:class: dropdown

**(1)** Met alleen een constante is $\mathbf{X}_i = \boldsymbol{\iota}$ en
$(\mathbf{X}_i'\mathbf{X}_i)^{-1} = 1/L_1$. Met $\mathbf{g} = L_2$ geeft
[](#thm-eventstudies-ar) $\sigma^2_{\varepsilon_i}(L_2 + L_2^2/L_1)$. Intuïtief heeft $\hat\mu_i$ variantie $\sigma^2/L_1$, en die fout wordt $L_2$ keer
opgeteld.

**(2)** De werkelijke variantie gedeeld door de gebruikte is
$(L_2 + L_2^2/L_1)/L_2 = 1 + L_2/L_1$. Het werkelijke significantieniveau is
$2\Phi\bigl(-1{,}96/\sqrt{1 + L_2/L_1}\bigr)$.

```{code-cell} ipython3
level = {L1_: 2 * stats.norm.cdf(-1.96 / np.sqrt(1 + 21 / L1_)) for L1_ in [60, 120, 250]}
pd.Series(level, name="werkelijk significantieniveau").rename_axis("L1").round(3)
```

Bij $L_1 = 250$ is de vertekening klein, maar bij $L_1 = 60$, een venster dat we
tegenkomen bij recente beursintroducties, verwerpt de naïeve toets bijna twee keer te
vaak. De ruis in een abnormaal rendement is dus niet alleen de ruis van de eventdag,
maar ook de onzekerheid over wat normaal was.
:::

:::{exercise}
:label: ex-eventstudies-3

**Brown en Warner op echte data.** Gebruik `returns` en `market` uit de replicatie.
Trek 300 keer een steekproef van 20 pseudo-events, elk een willekeurig aandeel op een
willekeurige handelsdag tussen 2004 en 2025, met 250 schattingsdagen ervóór.
Bereken $J_1$ voor een eendaags venster zonder effect en met een abnormaal
rendement van 1%. Vergelijk met de simulatie ([](#fig-eventstudies-kracht)). Welke
eigenschap van echte data verklaart een verschil?
:::

:::{solution} ex-eventstudies-3
:class: dropdown

```{code-cell} ipython3
first = dates.searchsorted(pd.Timestamp("2004-01-01"))
last = dates.searchsorted(pd.Timestamp("2025-12-31"))
J_null, J_alt = [], []
for _ in range(300):
    num, var_sum = 0.0, 0.0
    for _ in range(20):
        while True:   # draw until the stock has a full estimation window and day 0
            r = returns[tickers[rng.integers(len(tickers))]].to_numpy()
            i0 = rng.integers(first, last)
            est = np.arange(i0 - 250, i0)
            if np.isfinite(r[est]).all() and np.isfinite(r[i0]):
                break
        coef, _, s2, xtx_inv = fit_market_model(r[est], r_m[est])
        num += r[i0] - coef[0] - coef[1] * r_m[i0]
        var_sum += car_variance(s2, xtx_inv, r_m[i0:i0 + 1])
    J_null.append(num / np.sqrt(var_sum))
    J_alt.append((num + 20 * 0.01) / np.sqrt(var_sum))
pd.Series({"verwerping zonder effect": np.mean(np.abs(J_null) > 1.96),
           "kracht (AR = 1%)": np.mean(np.abs(J_alt) > 1.96)}).round(3)
```

De verwerping zonder effect ligt dicht bij 5%, want willekeurige dagen en aandelen
geven vrijwel onafhankelijke events. De kracht ligt iets hoger dan de 63% van de simulatie met $N = 20$, omdat de residuele
volatiliteit van deze grote aandelen (1,8%) onder de 2% van de simulatie ligt. De
spreiding in volatiliteit werkt de andere kant op, want een paar zeer volatiele aandelen
(TSLA, SMCI) domineren de noemer van $J_1$. Per saldo wint de lagere gemiddelde
volatiliteit, met 69% tegen 63%. Wat de kracht bepaalt, is dus vooral de volatiliteit
van de gekozen aandelen, en die verklaart ook waarom Brown en Warner met willekeurige
aandelen minder vonden dan onze simulatie.
:::
