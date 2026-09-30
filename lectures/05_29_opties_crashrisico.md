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

(05-29-opties-crashrisico)=

# Opties en crashrisico

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1976–2010. Het college loopt van Mertons sprongmodel tot het werk van
Santa-Clara en Yan.

**Wat we al weten.** In [](#02-09-black-scholes) bleken diepe puts duur, en lag de VIX
gemiddeld vier volatiliteitspunten boven de volatiliteit die daarna werd gerealiseerd. De
rampenmodellen uit [](#05-27-drie-antwoorden) laten een kleine kans op een grote crash de
aandelenpremie dragen. Een eeuw rendementen bevat echter te weinig crashes om dat te
toetsen.

**Welke vraag staat open.** Optieprijzen worden elke dag opnieuw vastgesteld. Kunnen ze
meten hoeveel beleggers betalen om van crashrisico af te komen, en is die prijs een beloning
voor risico of een vergissing?
```

## Overzicht

Wat kost verzekering tegen een crash, en wat zegt die prijs over de aandelenpremie?
Optieprijzen geven een crash een risiconeutrale kans die een veelvoud is van de werkelijke,
zodat een flink deel van de aandelenpremie crashpremie is. De winst van wie die verzekering
verkoopt, is in rendementsdata echter niet te meten. In dit college:

- lezen we uit de kromming van optieprijzen de risiconeutrale verdeling af;
- leiden we af waarom de variance risk premium positief is, hoe sprongen de smirk maken en
  welk deel van de aandelenpremie crashpremie is;
- simuleren we een verkoper van puts en vragen we welke Sharpe-ratio twintig jaar data hem
  laten zien;
- repliceren we de linksscheve risiconeutrale verdeling van SPY, de voorspelregressie van
  Bollerslev, Tauchen en Zhou {cite}`BollerslevTauchenZhou2009` en het rendement van de
  Cboe PutWrite-index.

Merton gaf in 1976 een prijsformule voor opties
op een koers die kan springen {cite}`Merton1976`, en twee jaar later lieten Breeden en
Litzenberger zien dat optieprijzen de hele risiconeutrale verdeling bevatten
{cite}`BreedenLitzenberger1978`. In 2010 haalden Pedro Santa-Clara en Shu Yan uit dagelijkse
optieprijzen de aandelenpremie die beleggers op elk moment eisen, met een model waarin
volatiliteit en crashintensiteit in de tijd variëren {cite}`SantaClaraYan2010`. Daarmee
verschoof de vraag
uit [](#03-13-equity-premium-puzzle) van een gerealiseerd gemiddelde naar een prijs die de
optiemarkt elke dag vaststelt. Rond dezelfde tijd toonden Saretto en Santa-Clara dat puts
verkopen op papier uitstekend
rendeert, maar dat marge-eisen de verkoper dwingen te sluiten juist wanneer de verzekering
uitbetaalt {cite}`SarettoSantaClara2009`. Dat puts duur zijn, betwist niemand, maar of die
prijs een beloning voor risico is of een fout die arbitrageurs zonder kapitaal laten
bestaan, daarover heeft nog geen theorie het laatste woord.

## Intuïtie: waarom zou dit waar zijn?

Op 19 oktober 1987 verloor de S&P 500 ruim twintig procent op één dag. Bij een
dagvolatiliteit van ongeveer één procent is dat onder Black-Scholes een uitschieter van
twintig standaarddeviaties, met een kans die praktisch nul is. Sinds die dag zijn puts ver
onder de koers duur, gemeten in volatiliteit. Dat patroon, te zien in
[](#fig-black-scholes-smirk), heet de *smirk* (een implied volatility die daalt naarmate de
uitoefenprijs stijgt), en Bates zag erin de angst voor een nieuwe crash {cite}`Bates2000`.

Waarom is die angst wel in optieprijzen te zien en nauwelijks in rendementen? Een optieprijs
weegt hoe waarschijnlijk een toestand is en hoeveel een dollar in die toestand waard is. In
een crash is iedereen tegelijk armer, zodat een dollar die dan wordt uitbetaald veel waard
is.
Daarom kost een put zoveel als hij zou kosten bij een veel grotere crashkans. Die opgeblazen
kans heet de *risiconeutrale* kans (de kans waaronder elke belegging gemiddeld de rente
oplevert), en het verschil met de werkelijke kans is de prijs van crashrisico.

Een verkoper van die verzekering verdient meestal een beetje en verliest zelden veel. Zijn
gemiddelde hangt dus af van gebeurtenissen die in twintig jaar één keer of nooit voorkomen.
Verkoopt hij met geleend geld, dan moet hij bovendien onderpand bijstorten zodra de markt
daalt, zodat hij gedwongen stopt op het slechtste moment.

We verwachten daarom dat puts gemiddeld minder opleveren dan de rente, en dat de verwachte
variantie onder risiconeutrale kansen hoger is dan de werkelijke. Een verkoper van puts
verdient dan een positieve premie, maar in een korte steekproef zonder crash lijkt die
premie
veel groter dan ze is. In de termen van Santa-Clara draagt de verkoper risico waarvoor een
premie wordt betaald, maar een onderzoeker die de hoge Sharpe-ratio van een rustige
periode als bewijs neemt, denkt meer te weten dan de markt die de optieprijs vaststelt
{cite}`SantaClara2026`.

## Toy-voorbeeld: normaal op, normaal neer, crash

We laden eerst de pakketten die de rest van het college gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import factorial
from scipy import optimize, special, stats

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

We nemen een Lucas-boom als in [](#03-12-consumptie-capm), waarin de markt een claim op
consumptie is, zodat het bruto rendement van de markt gelijk is aan de consumptiegroei
$g$. Er zijn drie
toestanden, en de representatieve belegger heeft CRRA-nut met $\gamma = 4$ en
$\beta = 0{,}97$.

| toestand | groei $g$ | kans $p$ |
|---|---|---|
| op | $1{,}10$ | $0{,}65$ |
| neer | $0{,}95$ | $0{,}33$ |
| crash | $0{,}60$ | $0{,}02$ |

**Het recept.** De *stochastische discontofactor* (SDF: de toestandsafhankelijke factor
waarmee payoffs worden verdisconteerd) is $m = \beta g^{-\gamma}$, en de prijs van een
payoff
$x$ is $\E[mx]$. De risiconeutrale kans van toestand $s$ is $q_s = p_s m_s/\E[m]$. Die
kansen
tellen op tot één, en elke prijs is de verwachte payoff onder $q$ gedeeld door
het bruto $R^f = 1/\E[m]$ ($1 + R^f$ in de setup).

**Stap 1, de SDF.** Per toestand is $m_{\text{op}} = 0{,}97/1{,}10^4 = 0{,}97/1{,}4641 = 0{,}6625$,
$m_{\text{neer}} = 0{,}97/0{,}8145 = 1{,}1909$ en $m_{\text{crash}} = 0{,}97/0{,}1296 = 7{,}4846$.
In de crash is een dollar dus ruim elf keer zoveel waard als in de goede toestand.

**Stap 2, de rente.** De verwachte SDF is $\E[m] = 0{,}65 \cdot 0{,}6625 + 0{,}33 \cdot 1{,}1909 +
0{,}02 \cdot 7{,}4846 = 0{,}4306 + 0{,}3930 + 0{,}1497 = 0{,}9733$. De rente is dan
$R^{f} = 1/0{,}9733 = 1{,}0274$.

**Stap 3, de risiconeutrale kansen.** $q_{\text{crash}} = 0{,}1497/0{,}9733 = 0{,}1538$,
en op
dezelfde manier is $q_{\text{op}} = 0{,}4424$ en $q_{\text{neer}} = 0{,}4038$. De crash
krijgt
dus $0{,}1538/0{,}02 = 7{,}7$ keer zijn werkelijke kans.

**Stap 4, de markt.** De prijs is $\E[mg] = 0{,}65 \cdot 0{,}7288 + 0{,}33 \cdot 1{,}1314 +
0{,}02 \cdot 4{,}4908 = 0{,}9369$ en de verwachte payoff is $\E[g] = 1{,}0405$. Het verwachte
rendement is dan $1{,}0405/0{,}9369 = 1{,}1106$ en de aandelenpremie
$1{,}1106 - 1{,}0274 = 8{,}32\%$. Zonder crashtoestand, met de kansen herschaald tot
$0{,}65/0{,}98 = 0{,}663$ en $0{,}33/0{,}98 = 0{,}337$, geeft dezelfde rekensom $2{,}44\%$.

**Stap 5, een put en een call.** Een put met uitoefenprijs $0{,}90$ betaalt alleen in de
crash uit, en wel $0{,}30$. Hij kost $0{,}02 \cdot 7{,}4846 \cdot 0{,}30 = 0{,}0449$ en
betaalt gemiddeld $0{,}0060$ uit, een bruto rendement van $0{,}1336$ en dus een gemiddeld
verlies van $86{,}6\%$. Een call met uitoefenprijs $1{,}05$ kost
$0{,}65 \cdot 0{,}6625 \cdot 0{,}05 = 0{,}0215$ en betaalt gemiddeld $0{,}0325$ uit, een
bruto rendement van $1{,}5094$ en dus een gemiddelde winst van $50{,}9\%$.

**Stap 6, de variantie.** Neem als gerealiseerde variantie $(\log g)^2$, dus $0{,}0091$,
$0{,}0026$ en $0{,}2609$. Onder $p$ is de verwachting $0{,}0120$, onder $q$ is ze
$0{,}4424 \cdot 0{,}0091 + 0{,}4038 \cdot 0{,}0026 + 0{,}1538 \cdot 0{,}2609 = 0{,}0452$, en
het verschil van $0{,}0332$ komt vrijwel geheel uit de crash.

De code rekent de zes stappen na en zet de uitkomsten naast de handberekening.

```{code-cell} ipython3
beta_toy, gamma_toy = 0.97, 4.0
growth = np.array([1.10, 0.95, 0.60])          # gross market return = consumption growth
prob = np.array([0.65, 0.33, 0.02])            # physical probabilities: up, down, crash

m_toy = beta_toy * growth ** (-gamma_toy)      # step 1: SDF per state
Em = prob @ m_toy                              # step 2
Rf_toy = 1 / Em
q_toy = prob * m_toy / Em                      # step 3: risk-neutral probabilities


def expected_return(x, p=prob, m=m_toy):
    """Expected gross return E[x] / E[m x] of a payoff x."""
    return (p @ x) / (p @ (m * x))


premium = expected_return(growth) - Rf_toy                        # step 4
p_no_crash = prob[:2] / prob[:2].sum()                            # same economy without the crash
premium_no_crash = expected_return(growth[:2], p_no_crash, m_toy[:2]) - 1 / (p_no_crash @ m_toy[:2])
put_toy = np.maximum(0.90 - growth, 0.0)                          # step 5
call_toy = np.maximum(growth - 1.05, 0.0)
rv_toy = np.log(growth) ** 2                                      # step 6
vrp_toy = q_toy @ rv_toy - prob @ rv_toy

hand = {"m crash": 7.4846, "E[m]": 0.9733, "R^f": 1.0274, "q crash": 0.1538,
        "aandelenpremie": 0.0832, "premie zonder crash": 0.0244, "prijs put 0,90": 0.0449,
        "E[R] put 0,90": 0.1336, "E[R] call 1,05": 1.5094, "variance risk premium": 0.0332}
code = {"m crash": m_toy[2], "E[m]": Em, "R^f": Rf_toy, "q crash": q_toy[2],
        "aandelenpremie": premium, "premie zonder crash": premium_no_crash,
        "prijs put 0,90": prob @ (m_toy * put_toy), "E[R] put 0,90": expected_return(put_toy),
        "E[R] call 1,05": expected_return(call_toy), "variance risk premium": vrp_toy}
pd.DataFrame({"met de hand": hand, "code": code}).round(4)
```

De code en de handberekening komen overeen. Omdat de markt de crash waardeert alsof hij
bijna acht keer zo vaak voorkomt als hij doet, verliest de put gemiddeld 86,6%, komt ruim
twee derde van de aandelenpremie uit de crash en vrijwel de hele premie op variantie.

## Theorie

De theorie gaat van optieprijzen naar de prijs van crashrisico. De kromming van
optieprijzen geeft de risiconeutrale dichtheid, en daaruit volgen de
momenten en het teken van de variance risk premium. Mertons sprongmodel verklaart de smirk
en
splitst de aandelenpremie in een diffusiedeel en een crashdeel. Tot slot volgen de
rendementen van opties en de verkopers met hefboom.

### Opzet en notatie

De notatie volgt [](#02-09-black-scholes). De indexprijs heet $S_t$, en $C_t(K,T)$ en
$P_t(K,T)$ zijn de prijzen van Europese calls en puts met uitoefenprijs $K$, expiratie $T$
en
looptijd $\tau = T - t$. De rente $r$ is continu samengesteld en constant, in de simulatie
3%
per jaar, en $F_t = S_t e^{(r-\delta)\tau}$ is de termijnkoers bij dividendrendement
$\delta$. De werkelijke kansmaat heet $\mathbb P$ en de risiconeutrale $\mathbb Q$, met
dichtheden $p(s)$ en $q(s)$ voor $S_T$. Zoals in het toy-voorbeeld krijgt elke toestand
onder
$\mathbb Q$ het gewicht van de SDF $m_T$,

$$
\E^{\mathbb Q}_t[X] = \frac{\E_t[m_T X]}{\E_t[m_T]}, \qquad \E_t[m_T] = e^{-r\tau}.
$$

### Breeden-Litzenberger: de verdeling zit in de kromming

Uit de prijzen van calls bij alle uitoefenprijzen volgt de hele risiconeutrale verdeling.
Een handelaar die een call met uitoefenprijs $K - h$ koopt, er twee met $K$ verkoopt en een
met $K + h$ koopt, heeft een *butterfly* (een driehoekige payoff rond $K$). Gedeeld door
$h^2$ betaalt die één dollar als de koers bij $K$ eindigt, zoals een Arrow-Debreu-effect uit
[](#03-11-apt-no-arbitrage). Zijn prijs is dus de verdisconteerde kans op die toestand
{cite}`BreedenLitzenberger1978`.

:::{prf:theorem} Breeden-Litzenberger
:label: thm-opties-crashrisico-bl

Laat $S_T$ onder $\mathbb Q$ een continue dichtheid $q$ hebben, en laat
$C_t(K) = e^{-r\tau}\E^{\mathbb Q}_t[(S_T - K)^{+}]$ voor alle $K > 0$. Dan geldt

```{math}
:label: eq-opties-crashrisico-bl
\frac{\partial C_t}{\partial K} = -e^{-r\tau}\,\mathbb Q_t(S_T > K),
\qquad
\frac{\partial^2 C_t}{\partial K^2} = e^{-r\tau}\, q(K).
```
:::

:::{prf:proof}
Schrijf $C_t(K) = e^{-r\tau}\int_K^\infty (s - K)\, q(s)\,\mathrm ds$. De integrand is
nul in $s = K$, dus de regel van Leibniz geeft
$\partial C_t/\partial K = -e^{-r\tau}\int_K^\infty q(s)\,\mathrm ds$, en nog eens
differentiëren geeft $e^{-r\tau} q(K)$ omdat $q$ continu is. Put-call-pariteit
$C_t - P_t = e^{-r\tau}(F_t - K)$ is lineair in $K$, dus voor puts geldt dezelfde tweede
afgeleide.
$\square$
:::

De helling van de callprijs is dus min de verdisconteerde kans dat de call uitbetaalt, en
de kromming is de verdisconteerde dichtheid. Met ook $p$ in handen volgt de SDF als functie
van de index, $\E_t[m_T \mid S_T = s] = e^{-r\tau}\, q(s)/p(s)$, de continue vorm van de
factor $7{,}7$ uit het toy-voorbeeld. Jackwerth schatte zo de risicoaversie uit S&P
500-opties over 1986–1995 {cite}`Jackwerth2000`. Na de crash van 1987 vond hij op een deel
van de index negatieve waarden, dus een SDF die daar stijgt in plaats van daalt. Hij
schreef dat vooral aan mispricing toe, en het verschijnsel heet sindsdien de *pricing
kernel puzzle*.

Een praktisch bezwaar is dat een tweede afgeleide ruis versterkt, omdat een prijsfout
$\varepsilon$ een fout in de dichtheid van orde $\varepsilon/h^2$ wordt. De numerieke
oplossing hieronder laat zien hoe snel dat misgaat.

### Modelvrije momenten

Omdat elke butterfly een toestand is, is elke payoff die alleen van $S_T$ afhangt een
portefeuille van opties. De risiconeutrale verwachting van zo'n payoff is daardoor in de
markt
af te lezen, en dat geldt ook voor de momenten van het rendement.

:::{prf:proposition} Spanning en risiconeutrale momenten
:label: prop-opties-crashrisico-momenten

Voor elke twee keer differentieerbare $H$ geldt, met $F = F_t$ en $Q(K)$ de
out-of-the-money-optie ($P_t(K)$ voor $K < F$, $C_t(K)$ voor $K \geq F$),

```{math}
:label: eq-opties-crashrisico-spanning
e^{-r\tau}\E^{\mathbb Q}_t[H(S_T)] = e^{-r\tau}H(F) + \int_0^\infty H''(K)\, Q(K)\,\mathrm dK .
```

Met $\ell = \log(S_T/F)$, het log rendement ten opzichte van de termijnkoers, zijn dus ook
de eerste drie momenten prijzen:
$\E^{\mathbb Q}_t[\ell] = -e^{r\tau}\int_0^\infty Q(K)K^{-2}\,\mathrm dK$,
$\E^{\mathbb Q}_t[\ell^2] = e^{r\tau}\int_0^\infty 2\bigl(1 - \log\tfrac KF\bigr)K^{-2}Q(K)\,\mathrm dK$ en
$\E^{\mathbb Q}_t[\ell^3] = e^{r\tau}\int_0^\infty \bigl(6\log\tfrac KF - 3\log^2\tfrac KF\bigr)K^{-2}Q(K)\,\mathrm dK$.
:::

Het bewijs is een Taylorontwikkeling van $H$ rond $F$ met integraalrestterm, waarin elke
restterm de payoff van een optie buiten het geld is. Het eerste moment levert de
VIX-formule uit [](#thm-volatiliteit-vix) op, want zonder sprongen is de risiconeutrale
verwachte variantie min
tweemaal $\E^{\mathbb Q}_t[\ell]$. Met het tweede en derde moment vonden Bakshi, Kapadia en
Madan dat
afzonderlijke aandelen veel minder linksscheef zijn dan de index
{cite}`BakshiKapadiaMadan2003`.
De linkerstaart is dus een eigenschap van het marktrisico, dat niet weg te diversifiëren
valt.

### De variance risk premium

Opties zijn gemiddeld duur, omdat de variantie hoog is op de momenten dat een dollar veel
waard is. Een *variance swap* betaalt op $T$ de gerealiseerde variantie min een vaste
prijs uit.
Het contract kost niets om aan te gaan, zodat die vaste prijs de risiconeutrale verwachting
van de variantie is. Met $\mathrm{RV}_{t,T}$ de gerealiseerde
variantie over $[t, T]$ definiëren we

```{math}
:label: eq-opties-crashrisico-vrp
\mathrm{VRP}_t \equiv \E^{\mathbb Q}_t\!\left[\mathrm{RV}_{t,T}\right] - \E_t\!\left[\mathrm{RV}_{t,T}\right].
```

De premie is dus het bedrag waarmee de risiconeutrale verwachte variantie boven de
werkelijke
ligt. Carr en Wu gebruiken het omgekeerde teken {cite}`CarrWu2009`, maar wij volgen
Bollerslev, Tauchen en Zhou, zodat het getal positief is als opties duur zijn.

:::{prf:proposition} Het teken van de variance risk premium
:label: prop-opties-crashrisico-vrp

Voor elke payoff $X$ met eindige verwachting geldt
$\E^{\mathbb Q}_t[X] - \E_t[X] = \Cov_t(m_T, X)/\E_t[m_T]$. In het bijzonder is
$\mathrm{VRP}_t > 0$ dan en slechts dan als $\Cov_t(m_T, \mathrm{RV}_{t,T}) > 0$.
:::

:::{prf:proof}
$\E^{\mathbb Q}_t[X] = \E_t[m_T X]/\E_t[m_T] = \bigl(\E_t[m_T]\E_t[X] + \Cov_t(m_T,X)\bigr)/\E_t[m_T]$.
$\square$
:::

De SDF is hoog als de markt daalt, en de variantie ook, door het *leverage effect*
(volatiliteit stijgt na dalingen) uit [](#04-21-volatiliteit). Samen maken ze de premie
positief,
wat de verwachting uit het begin van het college bevestigt. In het toy-voorbeeld is ze
$0{,}0332$, en op
echte data lag ze in [](#fig-black-scholes-vrp) gemiddeld rond vier volatiliteitspunten.
Bollerslev, Tauchen en Zhou vonden bovendien dat een hoge premie na 1990 hoge latere
marktrendementen voorspelde {cite}`BollerslevTauchenZhou2009`.

### Sprongen: het model van Merton

Een sprong in de koers maakt vooral diepe puts duur, omdat hij de linkerstaart dikker maakt
en omdat een optieverkoper zich er niet tegen kan hedgen. De delta-hedge uit
[](#02-09-black-scholes) werkt alleen als de koers continu beweegt. Een sprong laat geen
tijd
om bij te stellen, zodat de optieprijs afhangt van hoe beleggers sprongrisico waarderen.
Merton schreef onder $\mathbb Q$

```{math}
:label: eq-opties-crashrisico-merton-sde
\frac{\mathrm dS_t}{S_{t-}} = (r - \delta - \lambda\kappa)\,\mathrm dt + \sigma\,\mathrm dW_t + (J - 1)\,\mathrm dN_t,
\qquad \log J \sim \mathcal N(\mu_J, \delta_J^2).
```

Hier telt $N$ de sprongen, met intensiteit $\lambda$ (in de simulatie $0{,}165$ per jaar,
ongeveer eens in de zes jaar). De factor $J$ is de koers na een sprong gedeeld door de
koers ervoor,
in
de simulatie gemiddeld $0{,}70$, en $\kappa = \E[J - 1] = e^{\mu_J + \delta_J^2/2} - 1$ is
de
gemiddelde relatieve sprong. De term $-\lambda\kappa$ compenseert de verwachte sprong, zodat
de index onder $\mathbb Q$ de rente blijft verdienen {cite}`Merton1976`.

:::{prf:theorem} Mertons prijsformule
:label: thm-opties-crashrisico-merton

Laat $C^{\mathrm{BS}}$ de Black-Scholes-formule zijn bij rente $r_n$ en volatiliteit
$\sigma_n$. Onder [](#eq-opties-crashrisico-merton-sde) met $\delta = 0$ is

```{math}
:label: eq-opties-crashrisico-merton
C_t = \sum_{n=0}^{\infty} \frac{e^{-\lambda'\tau}(\lambda'\tau)^n}{n!}\,
      C^{\mathrm{BS}}\!\left(S_t, K, \tau;\ r_n, \sigma_n\right),
\qquad
\lambda' = \lambda(1+\kappa),\quad
\sigma_n^2 = \sigma^2 + \frac{n\delta_J^2}{\tau},\quad
r_n = r - \lambda\kappa + \frac{n\log(1+\kappa)}{\tau},
```
:::

Het bewijs conditioneert op het aantal sprongen $n$. Gegeven $n$ is $\log S_T$ normaal, met
dezelfde verwachting en variantie als onder Black-Scholes met $r_n$ en $\sigma_n$, en
middelen
over de Poisson-kansen geeft de formule. De optieprijs is dus een gewogen gemiddelde van
Black-Scholes-prijzen in werelden met nul, één of meer sprongen. Zo'n mengsel van normale
verdelingen heeft dikke staarten, met $\mu_J < 0$ vooral links, zodat diepe puts een hoge
implied volatility krijgen, het sterkst bij korte looptijden.

Merton nam aan dat sprongrisico diversifieerbaar is, zodat sprongen onder $\mathbb Q$ even
vaak voorkomen als onder $\mathbb P$, maar de data spreken dat tegen. Bates vond op
S&P 500-futuresopties dat stochastische volatiliteit zonder sprongen de scheefheid alleen
met
onplausibele parameters verklaart {cite}`Bates2000`. Pan schatte de index en de optieprijzen
in één model en vond een premie op sprongrisico die stijgt als de markt volatiel wordt
{cite}`Pan2002`.

### Hoeveel van de aandelenpremie is crashpremie?

Als crashes onder $\mathbb Q$ vaker of dieper zijn dan onder $\mathbb P$, betalen beleggers
voor crashrisico een eigen premie, naast de premie voor gewone schommelingen. Het deel van
de
drift dat de verwachte sprong compenseert, verschilt daardoor tussen de twee maten, en dat
verschil is het extra rendement voor sprongen.

:::{prf:proposition} Ontbinding van de aandelenpremie
:label: prop-opties-crashrisico-premie

Laat onder $\mathbb P$ gelden
$\mathrm dS_t/S_{t-} = (\mu - \lambda^{\mathbb P}\kappa^{\mathbb P})\,\mathrm dt + \sigma\,\mathrm dW^{\mathbb P}_t + (J-1)\,\mathrm dN_t$,
met sprongintensiteit $\lambda^{\mathbb P}$ en gemiddelde sprong $\kappa^{\mathbb P}$. Onder
$\mathbb Q$ geldt dezelfde vorm met $r$, $W^{\mathbb Q}_t = W^{\mathbb P}_t + \eta t$,
$\lambda^{\mathbb Q}$ en $\kappa^{\mathbb Q}$, waarin $\eta$ de prijs per eenheid
diffusierisico is. Dan

```{math}
:label: eq-opties-crashrisico-premie
\mu - r = \underbrace{\sigma\eta}_{\text{diffusiepremie}}
        + \underbrace{\lambda^{\mathbb Q}\,\lvert\kappa^{\mathbb Q}\rvert - \lambda^{\mathbb P}\,\lvert\kappa^{\mathbb P}\rvert}_{\text{crashpremie}}
        \qquad (\kappa^{\mathbb P}, \kappa^{\mathbb Q} < 0).
```
:::

:::{prf:proof}
Schrijf de $\mathbb Q$-dynamiek uit in $W^{\mathbb P}$ met
$\sigma\,\mathrm dW^{\mathbb Q} = \sigma\,\mathrm dW^{\mathbb P} + \sigma\eta\,\mathrm dt$. Een
maatwissel verandert de paden niet, dus de driftterm is in beide schrijfwijzen dezelfde:
$\mu - \lambda^{\mathbb P}\kappa^{\mathbb P} = r - \lambda^{\mathbb Q}\kappa^{\mathbb Q} + \sigma\eta$. $\square$
:::

De aandelenpremie bestaat dus uit een vergoeding $\sigma\eta$ voor gewone schommelingen (in
de kalibratie hieronder $3{,}5\%$ bij $\sigma = 15\%$) en een crashpremie. Santa-Clara en
Yan schatten
beide dagelijks uit S&P 500-opties van 1996 tot en met 2002 {cite}`SantaClaraYan2004`. De
tabel zet hun hoofdgetallen uit de werkdocumentversie naast onze kalibratie.

| grootheid | Santa-Clara en Yan | onze kalibratie |
|---|---|---|
| volatiliteit | $18{,}3\%$ diffusie | $15\%$ diffusie, $18{,}3\%$ met sprongen |
| sprongintensiteit onder $\mathbb Q$ (per jaar) | $0{,}165$ | $0{,}165$ |
| sprongintensiteit onder $\mathbb P$ (per jaar) | $0{,}078$ | $0{,}078$ |
| gemiddelde sprong onder $\mathbb Q$ | $-31{,}6\%$ | $-30\%$ |
| aandelenpremie | $10{,}1\%$ | $6{,}1\%$ |
| waarvan crashpremie | $2{,}9\%$ | $2{,}6\%$ |

Crashes zijn bij Santa-Clara en Yan onder $\mathbb Q$ twee keer zo waarschijnlijk als onder
$\mathbb P$, zodat beleggers crashes zwaarder wegen dan hun kans. Het crashdeel is iets
minder dan
een derde van de premie en schommelt tussen nul en bijna twee derde. De gepubliceerde versie
meldt bovendien dat de uit opties afgeleide premie latere marktrendementen voorspelt
{cite}`SantaClaraYan2010`.

In hun steekproef was het gerealiseerde overrendement van de S&P 500 $-2{,}2\%$ per jaar,
zodat zeven jaar rendementen niets over de premie zeggen en zeven jaar optieprijzen wel.
Over zo'n korte horizon speelt [de standaardfout van 2%](#00-01-rendementen) in versterkte
vorm, want bij een
volatiliteit van $18{,}3\%$ heeft een gemiddeld rendement over zeven jaar een
standaardfout van $0{,}183/\sqrt 7 = 6{,}9$ procentpunt.

### Verwachte optierendementen

Een verkoper van puts ontvangt precies wat de koper gemiddeld verliest, dus voordat we de
verkoper bekijken, ordenen we de verwachte rendementen van opties. Als de SDF daalt in de
index, leveren calls meer op dan de index en puts minder dan de
rente.
Het effect is sterker naarmate de optie verder in de staart ligt. Een call is namelijk een
gehefboomde claim op de goede toestanden en een put op de slechte, en goede toestanden zijn
goedkoop terwijl slechte duur zijn.

:::{prf:theorem} Coval-Shumway
:label: thm-opties-crashrisico-cs

Laat $m_T = m(S_T)$ niet-stijgend zijn in $S_T$, en schrijf $\E[R_x] = \E[x]/\E[m x]$
voor het verwachte bruto rendement van een payoff $x(S_T) \geq 0$. Dan geldt voor
$K_1 < K_2$:

1. calls verslaan de index, en meer naarmate de uitoefenprijs hoger ligt,
   $\E[R_{C(K_2)}] \geq \E[R_{C(K_1)}] \geq \E[R_S]$;
2. puts blijven onder de rente, en meer naarmate de uitoefenprijs lager ligt,
   $\E[R_{P(K_1)}] \leq \E[R_{P(K_2)}] \leq R^{f}$.
:::

Het bewijs schrijft elke optie als de vorige payoff maal een monotone functie van $S_T$,
bijvoorbeeld $(S_T - K)^{+} = S_T (1 - K/S_T)^{+}$. Twee functies van $S_T$ met
tegengestelde
monotonie hebben een negatieve covariantie, zodat een factor die stijgt in $S_T$ het
verwachte
rendement verhoogt en een factor die daalt het verlaagt.

Het toy-voorbeeld laat de ordening al zien. De call met uitoefenprijs $1{,}05$ levert
$50{,}9\%$ op, ruim boven de $11{,}1\%$ van de markt, en de put met $0{,}90$ verliest
gemiddeld $86{,}6\%$. Coval en Shumway vonden dat S&P 500-opties deze ordening consequent
vertonen {cite}`CovalShumway2001`. Een *straddle* (een call plus een put met dezelfde
uitoefenprijs en looptijd) met bèta nul verloor bij hen ongeveer drie procent per week,
terwijl zo'n positie onder het CAPM de
rente zou moeten verdienen. Broadie, Chernov en Johannes relativeerden die verliezen,
omdat het gemiddelde rendement van een put zo onzeker is dat zulke verliezen met
Black-Scholes verenigbaar blijven
{cite}`BroadieChernovJohannes2009`.

### Marges en de verkoper van puts

Een verkoper van puts met hefboom gaat al failliet bij een crash die veel kleiner is dan de
daling waarbij hij het volle notionele bedrag moet betalen. Deze verkoper is de
gehefboomde arbitrageur
uit [](#04-22-risk-management), maar dan met een verlies dat in één sprong komt. Laat een
belegger met eigen vermogen $E$ een aantal $n$ puts verkopen met uitoefenprijs
$K = (1-k)S_0$ tegen premie $P_0 = p_0 S_0$, en noem $L = nK/E$ zijn *notionele hefboom*
(de nominale verplichting per dollar eigen vermogen).

:::{prf:proposition} Ruïnedrempel van een verkochte put
:label: prop-opties-crashrisico-ruine

Een onmiddellijke daling van de index met een fractie $j$ vaagt het eigen vermogen
minstens weg zodra

```{math}
:label: eq-opties-crashrisico-ruine
j \;\geq\; j^{*} = k + p_0 + \frac{1-k}{L} ,
```

zodat een volledig gecollateraliseerde verkoper ($L \leq 1$) niet failliet kan gaan. Een
verkoper met $L = 5$ en $k = 5\%$ gaat failliet bij een crash van ongeveer $24\%$.
:::

:::{prf:proof}
Na de daling is de put minstens zijn intrinsieke waarde $K - (1-j)S_0$ waard, en het
verlies ten opzichte van de ontvangen premie is minstens $n\bigl(K - (1-j)S_0 - P_0\bigr)$.
Dit is minstens $E = nK/L$ als $(1-k) - (1-j) - p_0 \geq (1-k)/L$. $\square$
:::

De drempel daalt dus met $1/L$, net als de verbreding waarbij het gehefboomde fonds in
[](#prop-risk-management-drempel) moet stoppen, terwijl de
Sharpe-ratio niet van $L$ afhangt. De *margin call* (de eis om onderpand bij te storten, op
straffe van gedwongen sluiting) komt nog eerder, omdat de beurs een buffer boven de
intrinsieke waarde eist. Saretto en Santa-Clara namen die regels mee voor opties op de S&P
500 van 1985 tot 2002 {cite}`SarettoSantaClara2009`. In hun werkdocumentversie verdient een
verkochte put op 10% onder de koers gemiddeld $59{,}1\%$ van de ontvangen premie per
maand, met een scheefheid van
$-11{,}06$. Die scheefheid is het mechanisme van de propositie, want één crash vaagt in één
keer jaren premie weg.

Als transactiekosten en margin calls worden meegenomen, wordt de Sharpe-ratio van sommige
van
de beste strategieën negatief. De auteurs concluderen dat optiemarkten grote mispricings
bevatten die door die kosten en marge-eisen niet weg te arbitreren zijn. Die conclusie
volgt de logica van Shleifer en Vishny uit [](#04-23-behavioral) en de verliesspiraal uit
[](#eq-risk-management-spiraal), waarin een arbitrageur die verliest moet verkopen, zodat
de prijs verder van zijn waarde raakt.

### Numerieke oplossing: een gekalibreerd sprongmodel

Een concrete kalibratie laat zien dat één crashtoestand genoeg is voor een steile smirk en
een crashpremie van ruim twee procentpunt. We kiezen de orde van grootte van Santa-Clara en
Yan:

- een diffusievolatiliteit van 15% en een rente van 3% per jaar;
- een gemiddelde sprong van $-30\%$ met spreiding $\delta_J = 10\%$;
- een sprongintensiteit van $0{,}165$ per jaar onder $\mathbb Q$ en $0{,}078$ onder
  $\mathbb P$;
- een diffusiepremie $\sigma\eta$ van 3,5%.

De code rekent [](#thm-opties-crashrisico-merton) uit met de Black-formule voor opties op
een
termijnkoers, zodat dezelfde functies straks ook op SPY-opties werken.

```{code-cell} ipython3
def black_price(F, K, T, sigma, DF, kind="call"):
    """Black (1976) price of a European option on a forward F with discount factor DF."""
    s = sigma * np.sqrt(T)
    d1 = (np.log(F / K) + 0.5 * s**2) / s
    call = DF * (F * special.ndtr(d1) - K * special.ndtr(d1 - s))
    return np.where(np.asarray(kind) == "call", call, call - DF * (F - K))


def implied_vol(price, F, K, T, DF, kind="call", n_iter=80):
    """Invert black_price for sigma by vectorised bisection."""
    lo, hi = np.full(np.shape(price), 1e-4), np.full(np.shape(price), 5.0)
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        below = black_price(F, K, T, mid, DF, kind) < price
        lo, hi = np.where(below, mid, lo), np.where(below, hi, mid)
    return 0.5 * (lo + hi)


def merton_price(S, K, T, r, sigma, lam, mu_j, delta_j, kind="call", n_max=40):
    """Merton (1976) jump-diffusion price as a Poisson mixture of Black-Scholes prices."""
    T = np.maximum(T, 1e-8)
    kappa = np.exp(mu_j + 0.5 * delta_j**2) - 1
    lam_prime = lam * (1 + kappa) * T
    price = 0.0
    for n in range(n_max):
        sigma_n = np.sqrt(sigma**2 + n * delta_j**2 / T)
        r_n = r - lam * kappa + n * np.log1p(kappa) / T
        weight = np.exp(-lam_prime) * lam_prime**n / factorial(n)
        price = price + weight * black_price(S * np.exp(r_n * T), K, T, sigma_n, np.exp(-r_n * T), kind)
    return price


def merton_log_density(x, T, r, sigma, lam, mu_j, delta_j, n_max=40):
    """Risk-neutral density of log(S_T / S_0) in the Merton model."""
    kappa = np.exp(mu_j + 0.5 * delta_j**2) - 1
    dens = 0.0
    for n in range(n_max):
        mean = (r - lam * kappa - 0.5 * sigma**2) * T + n * mu_j
        dens = dens + stats.poisson.pmf(n, lam * T) * stats.norm.pdf(x, mean, np.sqrt(sigma**2 * T + n * delta_j**2))
    return dens


R_SIM, SIGMA_SIM, DELTA_J = 0.03, 0.15, 0.10
MU_J = np.log(0.70) - 0.5 * DELTA_J**2          # mean jump E[J - 1] = -30%
LAM_Q, LAM_P, ETA_SIGMA = 0.165, 0.078, 0.035    # jump intensities per year; diffusive premium
KAPPA = np.exp(MU_J + 0.5 * DELTA_J**2) - 1
jump_premium = (LAM_P - LAM_Q) * KAPPA
qv_q = SIGMA_SIM**2 + LAM_Q * (MU_J**2 + DELTA_J**2)
qv_p = SIGMA_SIM**2 + LAM_P * (MU_J**2 + DELTA_J**2)
print(f"kappa = {KAPPA:.4f}; sprongpremie = {jump_premium:.4f}; diffusiepremie = {ETA_SIGMA:.4f}; "
      f"equity premium = {jump_premium + ETA_SIGMA:.4f}")
print(f"verwachte variantie Q: {qv_q:.4f} (vol {np.sqrt(qv_q):.4f}); P: {qv_p:.4f} (vol {np.sqrt(qv_p):.4f})")

moneyness = np.array([0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10])
smirk_table = pd.DataFrame(
    {
        f"T = {label}": implied_vol(
            merton_price(100.0, 100.0 * moneyness, T, R_SIM, SIGMA_SIM, LAM_Q, MU_J, DELTA_J),
            100.0 * np.exp(R_SIM * T), 100.0 * moneyness, T, np.exp(-R_SIM * T))
        for label, T in (("1 maand", 1 / 12), ("3 maanden", 0.25), ("1 jaar", 1.0))
    },
    index=pd.Index(moneyness, name="K / S"),
)
(100 * smirk_table).round(2)
```

Volgens [](#prop-opties-crashrisico-premie) is de crashpremie
$(0{,}165 - 0{,}078) \cdot 0{,}30 = 2{,}61\%$, ruim twee vijfde van een aandelenpremie van
$6{,}11\%$. De risiconeutrale volatiliteit is $21{,}4\%$ en de werkelijke $18{,}3\%$, een
variance risk premium van ruim drie volatiliteitspunten. In de tabel daalt de implied
volatility bij één maand van $42{,}3\%$ op 80% van de spot naar $16{,}7\%$ at-the-money,
terwijl ze bij een jaar veel vlakker loopt. De diffusiespreiding groeit namelijk met de
looptijd, terwijl één sprong even groot
blijft, zodat een sprong van $-30\%$ over een jaar veel minder uitsteekt en het mengsel
[](#eq-opties-crashrisico-merton) dichter bij een normale verdeling komt.

Daarna gaan we de omgekeerde weg. We simuleren twee miljoen koersen op één maand onder
$\mathbb Q$ en nemen de tweede differentie uit [](#thm-opties-crashrisico-bl) van de
gesimuleerde, de exacte en de afgeronde callprijzen.

```{code-cell} ipython3
T_BL, N_MC = 1 / 12, 2_000_000
n_jumps = rng.poisson(LAM_Q * T_BL, N_MC)
log_ret = ((R_SIM - LAM_Q * KAPPA - 0.5 * SIGMA_SIM**2) * T_BL
           + SIGMA_SIM * np.sqrt(T_BL) * rng.standard_normal(N_MC)
           + n_jumps * MU_J + np.sqrt(n_jumps) * DELTA_J * rng.standard_normal(N_MC))
S_T = 100.0 * np.exp(log_ret)
DF_BL = np.exp(-R_SIM * T_BL)


def breeden_litzenberger(K, C, DF):
    """Density of S_T from call prices on an equally spaced strike grid (central second difference)."""
    dK = K[1] - K[0]
    return K[1:-1], (C[2:] - 2 * C[1:-1] + C[:-2]) / (dK**2 * DF)


bl_rows, bl_curves = [], {}
for dK in (2.0, 1.0, 0.25):
    K_grid = np.arange(50.0, 125.0 + dK / 2, dK)
    C_exact = merton_price(100.0, K_grid, T_BL, R_SIM, SIGMA_SIM, LAM_Q, MU_J, DELTA_J)
    C_mc = DF_BL * np.array([np.maximum(S_T - k, 0.0).mean() for k in K_grid])
    C_quote = C_exact + rng.uniform(-0.005, 0.005, len(K_grid))      # half-cent quote rounding
    K_mid, _ = breeden_litzenberger(K_grid, C_exact, DF_BL)
    true = merton_log_density(np.log(K_mid / 100.0), T_BL, R_SIM, SIGMA_SIM, LAM_Q, MU_J, DELTA_J) / K_mid
    for label, C in (("exacte prijzen", C_exact), ("Monte Carlo, 2 mln paden", C_mc),
                     ("exact + afronding 0,5 cent", C_quote)):
        _, dens = breeden_litzenberger(K_grid, C, DF_BL)
        bl_rows.append({"Delta K": dK, "prijzen": label,
                        "RMSE dichtheid": np.sqrt(np.mean((dens - true) ** 2)),
                        "max |fout|": np.abs(dens - true).max(),
                        "massa": np.sum(dens) * dK})
        bl_curves[(dK, label)] = (K_mid, dens, true)
pd.DataFrame(bl_rows).set_index(["Delta K", "prijzen"]).round(5)
```

Met exacte prijzen daalt de fout met $\Delta K^2$, en met Monte Carlo-prijzen blijft ze door
simulatieruis steken. Een afronding op een halve cent laat de fout daarentegen exploderen,
want bij $\Delta K = 0{,}25$ is de RMSE $0{,}113$, 57 keer zoveel als bij $\Delta K = 2$.
Dichtere uitoefenprijzen maken het dus erger, en daarom fitten we in de replicatie eerst een
gladde smile.

De figuur toont links de smirk per looptijd en rechts de tweede bult in de dichtheid rond
een koers van 70.

```{code-cell} ipython3
:label: cel-opties-crashrisico-merton
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
for i, col in enumerate(smirk_table.columns):
    axes[0].plot(100 * smirk_table.index, 100 * smirk_table[col], "o-", color=hap.plotting.COLORS[i], label=col)
axes[0].axhline(100 * SIGMA_SIM, color="black", lw=0.8, ls="--", label="diffusievolatiliteit")
axes[0].set_title("(a) Implied volatility in het Merton-model")
axes[0].set_xlabel("Uitoefenprijs (% van de spot)")
axes[0].set_ylabel("Implied volatility (%)")
axes[0].legend()

K_mid, dens_mc, true = bl_curves[(1.0, "Monte Carlo, 2 mln paden")]
_, dens_noise, _ = bl_curves[(0.25, "exact + afronding 0,5 cent")]
lognormal = stats.lognorm.pdf(K_mid, s=smirk_table.loc[1.00, "T = 1 maand"] * np.sqrt(T_BL),
                              scale=100.0 * np.exp((R_SIM - 0.5 * smirk_table.loc[1.00, "T = 1 maand"] ** 2) * T_BL))
axes[1].plot(K_mid, true, color="black", lw=1.6, label="ware Q-dichtheid")
axes[1].plot(K_mid, dens_mc, ".", ms=4, color=hap.plotting.COLORS[0], label="Breeden-Litzenberger uit Monte Carlo (ΔK = 1)")
axes[1].plot(K_mid, lognormal, color=hap.plotting.COLORS[1], ls="--", label="lognormaal bij ATM-volatiliteit")
axes[1].set_yscale("log")
axes[1].set_ylim(1e-5, 0.2)
axes[1].set_title("(b) Risiconeutrale dichtheid, looptijd 1 maand")
axes[1].set_xlabel("Koers op expiratie $S_T$")
axes[1].set_ylabel("Dichtheid (log-schaal)")
axes[1].legend(fontsize=8)
fig.tight_layout()
plt.show()
```

:::{figure} #cel-opties-crashrisico-merton
:label: fig-opties-crashrisico-merton
:width: 100%

Links: één crashtoestand volstaat voor een smirk die steil is bij korte en vlak bij lange
looptijden. Rechts: de risiconeutrale dichtheid heeft een tweede bult rond 70, de crash, die
de lognormale verdeling met dezelfde at-the-money-volatiliteit volledig mist.
:::

De risiconeutrale dichtheid is dus tweetoppig, en Breeden-Litzenberger vindt de tweede top
uit
gesimuleerde prijzen terug. Een belegger die alleen de at-the-money-volatiliteit kent, ziet
de crash niet.

```{admonition} Samengevat
:class: tip

- De kromming van callprijzen is de verdisconteerde risiconeutrale dichtheid,
  [](#eq-opties-crashrisico-bl), en uit dezelfde prijzen volgen de momenten,
  [](#eq-opties-crashrisico-spanning).
- De variance risk premium [](#eq-opties-crashrisico-vrp) is positief omdat de variantie hoog
  is als de SDF hoog is, en groter naarmate de volatiliteit sterker stijgt na dalingen.
- Sprongen maken de smirk, het steilst bij korte looptijden, [](#eq-opties-crashrisico-merton).
  Een hogere $\lambda^{\mathbb Q}$ bij gelijke $\lambda^{\mathbb P}$ verhoogt de crashpremie in
  [](#eq-opties-crashrisico-premie), in onze kalibratie 2,6 van 6,1 procentpunt.
- Een hogere hefboom $L$ verlaagt de crash die een verkoper van puts ruïneert,
  [](#eq-opties-crashrisico-ruine).

```

## Simulatie: dertig jaar puts verkopen

We willen weten welke Sharpe-ratio een onderzoeker met twintig jaar data ziet bij het
verkopen van puts, terwijl de crashpremie uit de numerieke oplossing werkelijk bestaat. Een
belegger verkoopt elke maand een put op 5% onder de koers, en in een tweede variant
at-the-money, zoals de Cboe PutWrite-index. In de *gecollateraliseerde* variant staat de
uitoefenprijs in kas, zodat hij niet failliet kan gaan.

In de *gehefboomde* variant stort hij een veelvoud van een gestileerde marge-eis en wordt
hij
dagelijks gewaardeerd met [](#eq-opties-crashrisico-merton). Zakt zijn vermogen onder de
eis,
dan wordt hij *uitgeschud*, wat betekent dat hij tegen de dagprijs moet terugkopen en
stoppen. We simuleren tweeduizend paden van dertig jaar, met prijzen uit $\mathbb Q$ en
koersen uit $\mathbb P$, en noemen een sprong van meer dan $-15\%$ een crash.

```{code-cell} ipython3
def merton_put_fast(S, K, tau):
    """Merton put price with the simulation parameters, truncated at 8 jumps (enough for tau <= 1 month)."""
    return merton_price(S, K, tau, R_SIM, SIGMA_SIM, LAM_Q, MU_J, DELTA_J, kind="put", n_max=8)


def margin_requirement(S, K, P):
    """Stylised naked short-put margin: premium plus max(15% of spot minus OTM amount, 10% of strike)."""
    return P + np.maximum(0.15 * S - np.maximum(S - K, 0.0), 0.10 * K)


N_PATHS, YEARS, DAYS_M, OTM = 2000, 30, 21, 0.05
DT, TAU = 1 / 252, 21 / 252
MULTIPLES = np.array([10.0, 5.0, 3.0, 2.0, 1.5])[:, None]      # capital as multiple of initial margin
MU_P = R_SIM + ETA_SIGMA + jump_premium                        # physical expected return


def step(S):
    """One trading day of the physical jump-diffusion; returns new price and a crash flag (jump below -15%)."""
    n = rng.poisson(LAM_P * DT, len(S))
    jump = n * MU_J + np.sqrt(n) * DELTA_J * rng.standard_normal(len(S))
    diffusion = (MU_P - LAM_P * KAPPA - 0.5 * SIGMA_SIM**2) * DT + SIGMA_SIM * np.sqrt(DT) * rng.standard_normal(len(S))
    return S * np.exp(diffusion + jump), (n > 0) & (jump < np.log(0.85))


S = np.full(N_PATHS, 100.0)
equity = np.ones((len(MULTIPLES), N_PATHS))
alive = np.ones_like(equity, dtype=bool)
put_ret, atm_ret, mkt_ret, crash, notional = [], [], [], [], []
for month in range(12 * YEARS):
    S0 = S.copy()
    K, K_atm = (1 - OTM) * S0, S0
    P0, P0_atm = merton_put_fast(S0, K, TAU), merton_put_fast(S0, K_atm, TAU)
    contracts = equity / (MULTIPLES * margin_requirement(S0, K, P0))
    cash = equity + contracts * P0
    notional.append(np.where(alive, contracts * K / np.maximum(equity, 1e-12), np.nan))
    crashed = np.zeros(N_PATHS, dtype=bool)
    for day in range(1, DAYS_M + 1):
        S, flag = step(S)
        crashed |= flag
        cash = cash * np.exp(R_SIM * DT)
        P_t = merton_put_fast(S, K, TAU - day * DT) if day < DAYS_M else np.maximum(K - S, 0.0)
        marked = cash - contracts * P_t
        if day < DAYS_M:
            # during the month: a margin call forces a close-out at today's price
            call = alive & (marked < contracts * margin_requirement(S, K, P_t))
        else:
            # expiry: the seller is ruined only if the payout exceeds his cash
            call = alive & (marked <= 0)
            # expiry without ruin: the marked-to-market equity funds next month
            equity = np.where(alive & ~call, marked, equity)
        # close-out: equity is what is left after buying back, floored at zero
        equity = np.where(call, np.maximum(marked, 0.0), equity)
        alive &= ~call
    growth_rf = np.exp(R_SIM * TAU)
    put_ret.append(((K + P0) * growth_rf - np.maximum(K - S, 0.0)) / K - 1)
    atm_ret.append(((K_atm + P0_atm) * growth_rf - np.maximum(K_atm - S, 0.0)) / K_atm - 1)
    mkt_ret.append(S / S0 - 1)
    crash.append(crashed)

put_ret, atm_ret, mkt_ret, crash = map(np.array, (put_ret, atm_ret, mkt_ret, crash))
rf_month = np.exp(R_SIM * TAU) - 1
p0_start = float(merton_put_fast(100.0, 95.0, TAU))
print(f"{N_PATHS} paden x {YEARS} jaar; crashes per jaar: {crash.mean() * 12:.4f}")
print(f"put 5% OTM bij S = 100: premie {p0_start:.4f}, initiële marge "
      f"{float(margin_requirement(100.0, 95.0, p0_start)):.4f}")
```

Crashes komen $0{,}076$ keer per jaar voor, dicht bij de kalibratie. De put op 5% onder de
koers kost bij een index van 100 een premie van $0{,}51$, tegen een marge-eis van $10{,}51$.

Voor de gecollateraliseerde strategieën berekenen we de Sharpe-ratio, de scheefheid en de
maximale drawdown, per pad en over alle paden samen.

```{code-cell} ipython3
def path_stats(returns):
    """Annualised Sharpe ratio, monthly skewness and maximum drawdown per path (columns)."""
    excess = returns - rf_month
    wealth = np.cumprod(1 + returns, axis=0)
    return {"Sharpe": np.sqrt(12) * excess.mean(0) / excess.std(0, ddof=1),
            "scheefheid": stats.skew(returns, axis=0),
            "max drawdown": (wealth / np.maximum.accumulate(wealth, axis=0) - 1).min(0)}


strategies = {"markt": mkt_ret, "short put ATM, gecollateraliseerd": atm_ret,
              "short put 5% OTM, gecollateraliseerd": put_ret}
pooled = {name: np.sqrt(12) * (r - rf_month).mean() / (r - rf_month).std() for name, r in strategies.items()}
sim_summary = pd.DataFrame(
    {name: {"Sharpe (populatie)": pooled[name],
            "Sharpe, mediaan per 30 jaar": np.median(path_stats(r)["Sharpe"]),
            "Sharpe, 5%-kwantiel": np.quantile(path_stats(r)["Sharpe"], 0.05),
            "Sharpe, 95%-kwantiel": np.quantile(path_stats(r)["Sharpe"], 0.95),
            "scheefheid (mediaan)": np.median(path_stats(r)["scheefheid"]),
            "max drawdown (mediaan)": np.median(path_stats(r)["max drawdown"])}
     for name, r in strategies.items()}
).T
sim_summary.round(3)
```

Over alle paden samen heeft de verkoper van puts op 5% onder de koers een Sharpe-ratio van
$0{,}326$, tegen $0{,}355$ voor de markt. Omdat in dit model alleen de sprongen onder
$\mathbb Q$ duurder zijn en de gewone schommelingen niet, is die Sharpe-ratio een ondergrens
voor wat een verkoper haalt in een markt waarin ook schommelingen in de volatiliteit een
premie dragen. De maandelijkse scheefheid van de verkochte put is
$-10{,}5$, dicht bij de waarde van Saretto en Santa-Clara. Per pad van dertig jaar loopt
de Sharpe-ratio van de verkoper tussen het 5%- en het 95%-kwantiel van nul tot $1{,}79$.

De tweede tabel geeft voor de gehefboomde verkoper de notionele hefboom en de kans om binnen
dertig jaar uitgeschud te worden.

```{code-cell} ipython3
margin_summary = pd.DataFrame(
    {"kapitaal / initiële marge": MULTIPLES.ravel(),
     "notionele hefboom (gem.)": np.nanmean(np.array(notional), axis=(0, 2)),
     "P(uitgeschud binnen 30 jaar)": 1 - alive.mean(1)}
).set_index("kapitaal / initiële marge")
margin_summary.round(3)
```

Een verkoper die tien keer de marge stort, heeft een hefboom onder één en wordt in een
half procent van
de
paden uitgeschud. Bij vijf keer de marge, een hefboom van $1{,}8$, gebeurt dat al in 80% van
de paden. Ruïne vraagt bij die hefboom volgens [](#prop-opties-crashrisico-ruine) een crash
van ruim 58%, maar de margin call komt veel eerder, omdat een sprong van $-30\%$ de put
diep in het geld brengt. Uitgeschud worden is hier dus bijna hetzelfde als de eerste crash
meemaken.

Welke Sharpe-ratio ziet dan een onderzoeker met twintig jaar data? We knippen elk pad na 240
maanden af en splitsen de steekproeven naar de vraag of er een crash in zat.

```{code-cell} ipython3
window = 240
ex20 = put_ret[:window] - rf_month
sharpe20 = np.sqrt(12) * ex20.mean(0) / ex20.std(0, ddof=1)
no_crash = crash[:window].sum(0) == 0
p_theory = np.exp(-window * crash.mean())
pd.DataFrame(
    {"fractie steekproeven": [no_crash.mean(), 1 - no_crash.mean()],
     "Sharpe mediaan": [np.median(sharpe20[no_crash]), np.median(sharpe20[~no_crash])],
     "Sharpe 90%-kwantiel": [np.quantile(sharpe20[no_crash], 0.9), np.quantile(sharpe20[~no_crash], 0.9)],
     "fractie Sharpe > 2 x populatie": [np.mean(sharpe20[no_crash] > 2 * pooled["short put 5% OTM, gecollateraliseerd"]),
                                        np.mean(sharpe20[~no_crash] > 2 * pooled["short put 5% OTM, gecollateraliseerd"])]},
    index=["geen crash in 20 jaar", "minstens één crash"],
).round(3)
```

Zonder crash ligt de mediane Sharpe-ratio van de verkoper op $1{,}85$, met minstens één
crash
op $0{,}28$. Links in de figuur liggen de twee histogrammen ver uit elkaar, en rechts
stijgt de kans op
uitschudden steil met de hefboom.

```{code-cell} ipython3
:label: cel-opties-crashrisico-shortput
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
bins = np.linspace(-0.5, 4.0, 46)
axes[0].hist(sharpe20[no_crash], bins=bins, alpha=0.6, color=hap.plotting.COLORS[0], label="geen crash in de steekproef")
axes[0].hist(sharpe20[~no_crash], bins=bins, alpha=0.6, color=hap.plotting.COLORS[1], label="minstens één crash")
axes[0].axvline(pooled["short put 5% OTM, gecollateraliseerd"], color="black", lw=1.2, label="populatie")
axes[0].set_title("(a) Sharpe-ratio van short puts over 20 jaar")
axes[0].set_xlabel("Geannualiseerde Sharpe-ratio")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].legend()
axes[1].plot(margin_summary["notionele hefboom (gem.)"], margin_summary["P(uitgeschud binnen 30 jaar)"], "o-")
for mult, row in margin_summary.iterrows():
    axes[1].annotate(f"{mult:g}x marge", (row["notionele hefboom (gem.)"], row["P(uitgeschud binnen 30 jaar)"]),
                     textcoords="offset points", xytext=(6, -10), fontsize=8)
axes[1].set_title("(b) Kans om binnen 30 jaar uitgeschud te worden")
axes[1].set_xlabel("Notionele hefboom (strike x contracten / eigen vermogen)")
axes[1].set_ylabel("Fractie paden")
fig.tight_layout()
plt.show()
```

:::{figure} #cel-opties-crashrisico-shortput
:label: fig-opties-crashrisico-shortput
:width: 100%

Links: twintig jaar verkochte puts zonder crash geven een Sharpe-ratio rond de twee, met één
crash rond de populatiewaarde van een derde. Rechts: de kans om uitgeschud te worden stijgt
steil met de hefboom, lang voordat het vermogen op nul staat.
:::

De twee verdelingen overlappen nauwelijks, zodat de Sharpe-ratio van een steekproef vooral
meet of er een crash in zat. In 21,4% van de steekproeven komt geen crash voor, zoals een
Poisson-proces voorspelt, want $e^{-20 \cdot 0{,}076} = 0{,}22$. In elk van die steekproeven
is de Sharpe-ratio meer dan het dubbele van de populatiewaarde.

Een onderzoeker met zo'n steekproef rapporteert een significante anomalie. De gebruikelijke
standaardfout van een Sharpe-ratio over twintig jaar is $\sqrt{(1 + 1{,}85^2/2)/20} = 0{,}37$,
zodat hij een $t$-waarde rond vijf vindt, maar die formule veronderstelt dunne staarten.
Net als een gemiddeld rendement over enkele decennia is ook de Sharpe-ratio dus slecht
gemeten zodra het rendement van zeldzame crashes afhangt. Dat een rustige steekproef de
premie overdrijft, verwachtten we al, maar niet dat de overdrijving zo groot zou zijn.

## Replicatie op echte data

### De risiconeutrale verdeling van SPY

```{admonition} Replicatie
:class: seealso

**Bron.** Breeden en Litzenberger, *Prices of State-Contingent Claims Implicit in Option
Prices*, Journal of Business 1978 {cite}`BreedenLitzenberger1978`; Bakshi, Kapadia en
Madan, *Stock Return Characteristics, Skew Laws, and the Differential Pricing of
Individual Equity Options*, Review of Financial Studies 2003 {cite}`BakshiKapadiaMadan2003`.

**Wat.** De bevinding dat de risiconeutrale verdeling van de index sterk linksscheef is,
vergeleken met de werkelijke verdeling over dezelfde horizon.

**Data hier.** De SPY-optieketen van 11 september 2026 met expiraties op 28 en 98 dagen, de
driemaandsrente en dagrendementen van de markt over 1926–2026, alle via `hap.data`.

**Verschil met het origineel.** Bakshi, Kapadia en Madan gebruikten OEX-opties en modelvrije
momenten, wij één dag opties op een ETF met een SVI-fit (de vijfparametervorm van Gatheral
voor de totale implied variance). Buiten de genoteerde uitoefenprijzen extrapoleren we niet.

**Verwachte afwijking.** Niveaus hangen van de dag af, maar de risiconeutrale scheefheid
moet voor beide looptijden negatief zijn en negatiever dan de historische, en de dichtheid
nergens negatief. Een positieve scheefheid wijst op een fout in de code.
```

We laden de optieketen en de rente, en bepalen per expiratie de termijnkoers uit
put-call-pariteit en de implied volatility van de opties buiten het geld.

```{code-cell} ipython3
chain = hap_data.yahoo_options("SPY", 28)
spot = float(chain["spot"].iloc[0])
valuation = pd.Timestamp(chain.index.max().date()) + pd.Timedelta(hours=16)
r_cc = float(np.log1p(hap_data.fred("DGS3MO")["DGS3MO"].dropna().loc[:valuation].iloc[-1] / 100))

quotes = chain.reset_index()
quotes = quotes[(quotes["bid"] > 0) & (quotes["ask"] > quotes["bid"])].copy()
quotes["mid"] = 0.5 * (quotes["bid"] + quotes["ask"])
quotes["T"] = (quotes["expiry"] + pd.Timedelta(hours=16) - valuation).dt.total_seconds() / (365.25 * 86400)


def smile_for_expiry(target_T):
    """OTM quotes, parity forward and implied vols for the expiry closest to target_T."""
    expiry_T = quotes.groupby("expiry")["T"].first()
    expiry = expiry_T.index[np.argmin(np.abs(expiry_T.to_numpy() - target_T))]
    g = quotes[quotes["expiry"] == expiry]
    T, DF = float(g["T"].iloc[0]), float(np.exp(-r_cc * g["T"].iloc[0]))
    wide = g.pivot_table(index="strike", columns="kind", values="mid").dropna()
    near = wide[np.abs(np.log(wide.index / spot)) < 0.05]
    F = float(np.median(near.index + (near["call"] - near["put"]) / DF))
    otm = g[((g["kind"] == "put") & (g["strike"] < F)) | ((g["kind"] == "call") & (g["strike"] >= F))]
    otm = otm[otm["bid"] >= 0.05].sort_values("strike").copy()
    otm["iv"] = implied_vol(otm["mid"].to_numpy(), F, otm["strike"].to_numpy(), T, DF, otm["kind"].to_numpy())
    otm["k"] = np.log(otm["strike"] / F)
    atm = float(np.interp(0.0, otm["k"], otm["iv"]))
    otm = otm[otm["k"].between(-5 * atm * np.sqrt(T), 3 * atm * np.sqrt(T))]
    return {"expiry": expiry, "T": T, "DF": DF, "F": F, "atm": atm, "otm": otm}


def svi_total_variance(k, a, b, rho, m, s):
    """Gatheral's raw SVI parametrisation of total implied variance w(k) = sigma^2 T."""
    return a + b * (rho * (k - m) + np.sqrt((k - m) ** 2 + s**2))


def rn_density(sm, n_grid=2001):
    """Breeden-Litzenberger density of log(S_T/F) from an SVI smile, inside the quoted strike range."""
    otm, T = sm["otm"], sm["T"]
    k_obs, w_obs = otm["k"].to_numpy(), otm["iv"].to_numpy() ** 2 * T
    fit = optimize.least_squares(lambda p: svi_total_variance(k_obs, *p) - w_obs,
                                 x0=[w_obs.min(), 0.1, -0.5, 0.0, 0.1],
                                 bounds=([-1, 0, -0.999, -1, 1e-4], [1, 5, 0.999, 1, 2]))

    def smile(kk):
        return np.sqrt(np.maximum(svi_total_variance(kk, *fit.x), 1e-10) / T)

    k = np.linspace(k_obs.min(), k_obs.max(), n_grid)
    K = sm["F"] * np.exp(k)
    C = black_price(sm["F"], K, T, smile(k), sm["DF"])
    dens_K = np.gradient(np.gradient(C, K), K) / sm["DF"]
    rmse = np.sqrt(np.mean((smile(k_obs) - otm["iv"].to_numpy()) ** 2))
    inner = slice(3, -3)                                         # one-sided differences at the grid edges
    return k[inner], (dens_K * K)[inner], smile, rmse            # density of k = log(S_T / F)


def moments(x, f):
    """Mass, mean, annualisable s.d., skewness and excess kurtosis of a density on a grid."""
    mass = np.trapezoid(f, x)
    f = f / mass
    mu = np.trapezoid(x * f, x)
    sd = np.sqrt(np.trapezoid((x - mu) ** 2 * f, x))
    return {"massa binnen strikes": mass, "sd": sd,
            "scheefheid": np.trapezoid((x - mu) ** 3 * f, x) / sd**3,
            "exces-kurtosis": np.trapezoid((x - mu) ** 4 * f, x) / sd**4 - 3}


smiles = {label: smile_for_expiry(T) for label, T in (("1 maand", 1 / 12), ("3 maanden", 0.25))}
print(f"waarderingsmoment {valuation}, spot {spot:.2f}, r = {r_cc:.4f}")
```

De koers was op het waarderingsmoment $764{,}29$ en de rente $3{,}82\%$. Voor beide
looptijden
fitten we nu de smile, nemen de tweede afgeleide en vergelijken de momenten met die van
historische rendementen over dezelfde horizon.

```{code-cell} ipython3
daily_log = np.log1p(hap_data.market_daily()["Mkt"])
rn_rows, densities = {}, {}
for label, sm in smiles.items():
    k, dens, smile, rmse = rn_density(sm)
    densities[label] = (k, dens, smile)
    mom = moments(k, dens)
    h = int(round(sm["T"] * 252))
    rn_rows[f"Q, {label} ({sm['expiry'].date()})"] = {
        "T (jaar)": sm["T"], "aantal opties": len(sm["otm"]), "fitfout (vol)": rmse,
        "massa binnen strikes": mom["massa binnen strikes"],
        "min. dichtheid": dens.min(), "vol (jaarbasis)": mom["sd"] / np.sqrt(sm["T"]),
        "scheefheid": mom["scheefheid"], "exces-kurtosis": mom["exces-kurtosis"]}
    for period, sample in (("1926-2026", daily_log), ("1990-2026", daily_log.loc["1990":])):
        agg = sample.rolling(h).sum().iloc[h - 1::h]
        rn_rows[f"P, {label}, {period}"] = {
            "T (jaar)": h / 252, "aantal opties": np.nan, "fitfout (vol)": np.nan,
            "massa binnen strikes": np.nan, "min. dichtheid": np.nan,
            "vol (jaarbasis)": agg.std() * np.sqrt(252 / h), "scheefheid": agg.skew(), "exces-kurtosis": agg.kurt()}
pd.DataFrame(rn_rows).T.round(4)
```

De tabel hieronder zet de risiconeutrale en de historische momenten naast de verwachting.

| grootheid | verwachting | 1 maand | 3 maanden |
|---|---|---|---|
| scheefheid onder $\mathbb Q$ | negatief | $-1{,}23$ | $-1{,}30$ |
| historische scheefheid, 1926–2026 | minder negatief | $-0{,}61$ | $-0{,}55$ |
| laagste waarde van de dichtheid | niet negatief | $0{,}103$ | $0{,}014$ |

**Geslaagd.** Het teken klopt voor beide looptijden, en de optiemarkt maakt de linkerstaart
ongeveer twee keer zo scheef als een eeuw data. De grootte is minder robuust, want over
1990–2026
is de historische kwartaalscheefheid $-1{,}33$, even negatief als de risiconeutrale, terwijl
de momenten rechtstreeks uit de prijzen met [](#prop-opties-crashrisico-momenten) een
scheefheid van $-2{,}1$ en $-2{,}3$ geven (oefening 3). De eeuw blijft de maatstaf, omdat
een scheefheid uit ruim drie decennia kwartalen vooral meet hoeveel crisiskwartalen erin
vielen.

Rechts in de figuur ligt de linkerstaart ver boven de normale verdeling met dezelfde
at-the-money-volatiliteit.

```{code-cell} ipython3
:label: cel-opties-crashrisico-spy-dichtheid
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
for i, (label, sm) in enumerate(smiles.items()):
    k, dens, smile = densities[label]
    otm = sm["otm"]
    axes[0].plot(otm["k"], 100 * otm["iv"], ".", ms=4, color=hap.plotting.COLORS[i], alpha=0.6)
    axes[0].plot(k, 100 * smile(k), color=hap.plotting.COLORS[i], label=f"{label}, SVI-fit")
    x = np.linspace(k.min(), k.max(), 400)
    normal = stats.norm.pdf(x, -0.5 * sm["atm"] ** 2 * sm["T"], sm["atm"] * np.sqrt(sm["T"]))
    axes[1].plot(k, dens, color=hap.plotting.COLORS[i], label=f"Q-dichtheid, {label}")
    axes[1].plot(x, normal, color=hap.plotting.COLORS[i], ls="--", lw=1, label=f"normaal bij ATM-vol, {label}")
axes[0].set_title("(a) Implied volatility van SPY-opties")
axes[0].set_xlabel(r"Log-moneyness $\log(K/F)$")
axes[0].set_ylabel("Implied volatility (%)")
axes[0].legend()
axes[1].set_yscale("log")
axes[1].set_ylim(1e-3, None)
axes[1].set_title("(b) Breeden-Litzenberger-dichtheid van $\\log(S_T/F)$")
axes[1].set_xlabel(r"$\log(S_T/F)$")
axes[1].set_ylabel("Dichtheid (log-schaal)")
axes[1].legend(fontsize=8)
fig.tight_layout()
plt.show()
```

:::{figure} #cel-opties-crashrisico-spy-dichtheid
:label: fig-opties-crashrisico-spy-dichtheid
:width: 100%

Links: de SVI-fit volgt de genoteerde implied volatilities op ongeveer een tiende
volatiliteitspunt. Rechts: de risiconeutrale dichtheid van SPY heeft een linkerstaart die
ordes van grootte dikker is dan de normale verdeling, en een rechterstaart die dunner is.
:::

Binnen de genoteerde uitoefenprijzen ligt $99{,}1\%$ (één maand) en $98{,}7\%$ (drie
maanden) van de massa, zodat de fit weinig mist. De dikke linkerstaart is de crash uit de
numerieke oplossing, nu in marktprijzen.

### De variance risk premium als voorspeller

```{admonition} Replicatie
:class: seealso

**Bron.** Bollerslev, Tauchen en Zhou, *Expected Stock Returns and Variance Risk Premia*,
Review of Financial Studies 2009 {cite}`BollerslevTauchenZhou2009`.

**Wat.** Tabel 2: regressies van het geannualiseerde overrendement over $h$ maanden op de
variance risk premium, januari 1990 tot december 2007, met Hodrick-$t$-waarden.

**Data hier.** $\mathrm{VRP}_t = \mathrm{VIX}_t^2/12 - \mathrm{RV}_t$ in maand-$\%^2$, met
$\mathrm{RV}_t$ de som van gekwadrateerde dagelijkse log-rendementen van de markt in maand
$t$, via `hap.data`. De steekproef loopt door tot juli 2026.

**Verschil met het origineel.** Het origineel berekent $\mathrm{RV}$ uit
vijfminutenrendementen, zodat onze versie ruiziger is. Onze Newey-West-$t$-waarden met $h-1$
lags vallen doorgaans hoger uit dan die van Hodrick.

**Verwachte afwijking.** Op 1990–2007 een positieve helling bij elke horizon, in de orde van
de gepubliceerde, met $t > 2$ bij drie maanden en de hoogste $R^2$ tussen drie en zes
maanden. Een negatieve helling op 1990–2007 wijst op een fout in de code.
```

We bouwen de premie uit de VIX en de gerealiseerde variantie en schatten de regressie voor
drie perioden en zes horizonnen.

```{code-cell} ipython3
vix = hap_data.fred("VIXCLS")["VIXCLS"].dropna()
implied_var = (vix.resample("ME").last() ** 2 / 12).rename("IV")            # monthly, %^2
realized_var = ((100 * daily_log) ** 2).resample("ME").sum().rename("RV")   # monthly, %^2
market_m = hap_data.market_monthly()
excess_log = (np.log1p(market_m["Mkt"]) - np.log1p(market_m["RF"])).rename("rx")
btz = implied_var.to_frame().join(realized_var, how="inner").join(excess_log, how="inner").dropna()
btz["VRP"] = btz["IV"] - btz["RV"]

btz_rows = []
for period, sl in (("1990-2007", slice("1990", "2007")), ("1990-2026", slice("1990", None)),
                   ("2008-2026", slice("2008", None))):
    sample = btz.loc[sl]
    res = hap.long_horizon_regression(1200 * sample["rx"], sample["VRP"], horizons=(1, 2, 3, 4, 6, 12),
                                      method="newey-west")
    res["helling (BTZ-schaal)"] = res["beta"] / res.index   # annualised % return averaged over h months
    res["adj. R2"] = 1 - (1 - res["r2"]) * (res["nobs"] - 1) / (res["nobs"] - 2)
    res["periode"] = period
    btz_rows.append(res.reset_index())
btz_table = pd.concat(btz_rows).set_index(["periode", "horizon"])
print(f"{btz.index[0]:%Y-%m} t/m {btz.index[-1]:%Y-%m}: gemiddelde IV {btz['IV'].mean():.2f}, "
      f"RV {btz['RV'].mean():.2f}, VRP {btz['VRP'].mean():.2f} (maand-%^2); VRP > 0 in "
      f"{(btz['VRP'] > 0).mean():.1%} van de maanden")
btz_table.rename(columns={"beta": "helling", "se": "standaardfout", "tstat": "t-waarde",
                          "r2": "R2", "nobs": "waarnemingen"}).round(3)
```

De schattingen over 1990–2007 staan hieronder naast die uit tabel 2 van het origineel. De
$t$-waarden zijn niet één op één vergelijkbaar, omdat de twee methoden verschillen.

| horizon (maanden) | helling origineel | helling hier | $t$ origineel (Hodrick) | $t$ hier (Newey-West) | aangepaste $R^2$ origineel | aangepaste $R^2$ hier |
|---|---|---|---|---|---|---|
| 1 | $0{,}39$ | $0{,}42$ | $1{,}76$ | $1{,}66$ | $1{,}07\%$ | $1{,}3\%$ |
| 3 | $0{,}47$ | $0{,}45$ | $2{,}86$ | $3{,}68$ | $6{,}82\%$ | $5{,}3\%$ |
| 6 | $0{,}30$ | $0{,}35$ | $2{,}15$ | $3{,}69$ | $5{,}42\%$ | $7{,}2\%$ |
| 12 | $0{,}12$ | $0{,}22$ | $1{,}00$ | $2{,}24$ | $1{,}23\%$ | $5{,}3\%$ |

**Geslaagd** voor 1990–2007. De hellingen hebben het goede teken en de gepubliceerde orde
van
grootte, de $t$-waarde bij drie maanden ligt ruim boven twee en de hoogste $R^2$ valt bij
zes
maanden. Daarna houdt het verband op, want over 1990–2026 is geen enkele helling significant
($t \leq 0{,}6$).

Het linkerpaneel toont de diep negatieve maanden, het rechter de $t$-waarden die na 2007
wegzakken.

```{code-cell} ipython3
:label: cel-opties-crashrisico-btz
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
axes[0].bar(btz.index, btz["VRP"], width=25,
            color=np.where(btz["VRP"] > 0, hap.plotting.COLORS[0], hap.plotting.COLORS[1]))
axes[0].set_ylim(-80, 90)
axes[0].axvline(pd.Timestamp("2007-12-31"), color="black", lw=0.8, ls="--")
axes[0].set_title("(a) Variance risk premium, VIX$^2$/12 min gerealiseerde variantie")
axes[0].set_xlabel("Jaar")
axes[0].set_ylabel("Maandvariantie (%$^2$), afgekapt op -80")
for i, period in enumerate(["1990-2007", "1990-2026", "2008-2026"]):
    axes[1].plot(btz_table.loc[period].index, btz_table.loc[period, "tstat"], "o-",
                 color=hap.plotting.COLORS[i], label=period)
axes[1].axhline(1.96, color="black", lw=0.8, ls="--")
axes[1].set_title("(b) Voorspelt de VRP het overrendement?")
axes[1].set_xlabel("Horizon (maanden)")
axes[1].set_ylabel("Newey-West $t$-waarde van de helling")
axes[1].legend()
fig.tight_layout()
plt.show()
```

:::{figure} #cel-opties-crashrisico-btz
:label: fig-opties-crashrisico-btz
:width: 100%

Links: de variance risk premium is meestal positief, en de negatieve maanden zijn
crisismaanden waarin de gerealiseerde variantie de VIX inhaalt (de twee diepste zijn
afgekapt). Rechts: de voorspelkracht van vóór 2007 is daarna verdwenen.
:::

De premie is in 87% van de maanden positief. In oktober 2008 en maart 2020 schoot de
gerealiseerde variantie echter ver boven de VIX en werd de premie diep negatief. Na oktober
2008 volgden nog verdere verliezen, maar na maart 2020 juist hoge rendementen. Een
voorspeller die de crash zelf als lage premie meet, kan dus ver naast zitten op de momenten
die het gemiddelde bepalen. Dat weerlegt niet dat de premie
positief is omdat de SDF en de variantie samen stijgen ([](#prop-opties-crashrisico-vrp)),
maar het laat zien hoe dun achttien jaar bewijs is,
net
als bij de voorspellers uit [](#04-20-voorspelbaarheid) die buiten de steekproef faalden.

### Verkopers van puts in het echt: de Cboe PutWrite-index

```{admonition} Replicatie
:class: seealso

**Bron.** Saretto en Santa-Clara, *Option Strategies: Good Deals and Margin Calls*,
Journal of Financial Markets 2009 {cite}`SarettoSantaClara2009`; Israelov en Nielsen,
*Covered Calls Uncovered*, Financial Analysts Journal 2015 {cite}`IsraelovNielsen2015b`;
Cboe, methodologie van de PutWrite-index {cite}`Cboe2026`.

**Wat.** De bewering dat indexputs verkopen een aantrekkelijke verhouding tussen rendement en
risico heeft, met een extreme linkerstaart. De PUT-index verkoopt elke maand at-the-money
SPX-puts, gedekt door schatkistpapier, en de BuyWrite-index BXM verkoopt calls.

**Data hier.** Dagelijkse niveaus van `^PUT`, `^BXM` en `^SP500TR` via `hap.data.yahoo(...)`,
als maandrendementen van september 1996 tot juni 2026. De waarden vóór de lancering in 2007
zijn teruggerekend.

**Verschil met het origineel.** Saretto en Santa-Clara gebruikten afzonderlijke contracten,
puts buiten het geld en expliciete marges, terwijl de PUT-index at-the-money is en zonder
hefboom werkt.

**Verwachte afwijking.** PUT heeft een lagere volatiliteit dan de S&P 500, een negatievere
scheefheid, een hogere kurtosis en een Sharpe-ratio binnen één standaardfout. In 2008 en
begin 2020 verliest PUT een groot deel van wat de index verliest, ondanks een bèta ver onder
één.
```

We berekenen de overrendementen, de samenvattende statistieken, de verliezen in de twee
crises en een regressie van elke strategie op de index.

```{code-cell} ipython3
levels = hap_data.yahoo(["^GSPC", "^PUT", "^BXM"], "1986-01-01").join(hap_data.yahoo("^SP500TR", "1986-01-01"))
monthly = levels[["^SP500TR", "^PUT", "^BXM"]].resample("ME").last().pct_change()
monthly.columns = ["S&P 500 (total return)", "PutWrite (PUT)", "BuyWrite (BXM)"]
cboe = monthly.join(market_m["RF"], how="inner").loc["1996-09":"2026-06"].dropna()
cboe_excess = cboe.drop(columns="RF").sub(cboe["RF"], axis=0)

stats_cboe = hap.summary_stats(cboe_excess).drop(columns=["start", "end"]).astype(float)
stats_cboe["SE Sharpe"] = np.sqrt((1 + stats_cboe["sharpe_ann"] ** 2 / 2) / (stats_cboe["nobs"] / 12))
for name in cboe_excess:
    dd = hap.drawdowns(cboe[name])
    fit = hap.newey_west(cboe_excess[name], cboe_excess["S&P 500 (total return)"], lags=3)
    stats_cboe.loc[name, "max drawdown"] = dd.attrs["max_drawdown"]
    stats_cboe.loc[name, "nov 2007 - feb 2009"] = (1 + cboe[name].loc["2007-11":"2009-02"]).prod() - 1
    stats_cboe.loc[name, "feb - mrt 2020"] = (1 + cboe[name].loc["2020-02":"2020-03"]).prod() - 1
    stats_cboe.loc[name, "alpha (jaar)"] = 12 * fit.params.iloc[0]
    stats_cboe.loc[name, "t(alpha)"] = fit.tvalues.iloc[0]
    stats_cboe.loc[name, "beta"] = fit.params.iloc[1]
print(f"{cboe.index[0]:%Y-%m} t/m {cboe.index[-1]:%Y-%m}, {len(cboe)} maanden")
labels_nl = {"mean_ann": "gem. overrendement (jaar)", "std_ann": "volatiliteit (jaar)",
             "sharpe_ann": "Sharpe-ratio (jaar)", "SE Sharpe": "standaardfout Sharpe",
             "skew": "scheefheid", "kurtosis": "exces-kurtosis", "beta": "bèta"}
stats_cboe[["mean_ann", "std_ann", "sharpe_ann", "SE Sharpe", "skew", "kurtosis", "max drawdown",
            "nov 2007 - feb 2009", "feb - mrt 2020", "alpha (jaar)", "t(alpha)", "beta"]].rename(
    columns=labels_nl).T.round(3)
```

Over 358 maanden haalde PUT een iets hogere Sharpe-ratio dan de index, bij een veel lagere
volatiliteit. De tabel hieronder zet de verwachtingen naast de uitkomsten.

| grootheid | verwachting | S&P 500 | PUT |
|---|---|---|---|
| volatiliteit per jaar | PUT lager | $15{,}4\%$ | $10{,}5\%$ |
| scheefheid | PUT negatiever | $-0{,}55$ | $-1{,}66$ |
| scheefheid, één put 10% onder de koers (origineel) | veel negatiever dan PUT | | $-11{,}06$ |
| exces-kurtosis | PUT hoger | $0{,}8$ | $6{,}8$ |
| Sharpe-ratio (standaardfout) | verschil onder één standaardfout | $0{,}58$ ($0{,}20$) | $0{,}62$ ($0{,}20$) |
| november 2007 – februari 2009 | groot deel van de index | $-51\%$ | $-32\%$ |
| februari – maart 2020 | groot deel van de index | $-19{,}6\%$ | $-19{,}8\%$ |
| bèta op de index | ver onder één | $1$ | $0{,}58$ |

**Geslaagd.** Alle verwachtingen komen uit. Het verschil in Sharpe-ratio is een vijfde van
één standaardfout, zodat dertig jaar data de twee strategieën niet kunnen onderscheiden,
terwijl de staart van PUT wel duidelijk meetbaar is. Bij Saretto en Santa-Clara is de
scheefheid ruim zes keer zo extreem, omdat PUT
at-the-money
verkoopt en het rendement op het volle onderpand meet in plaats van op de premie. Tegen de
index geregresseerd heeft PUT
een alpha van 1,3% per jaar met $t = 1{,}1$.

De figuur laat zien dat de PutWrite-index in 2020 even diep valt als de S&P 500 en
in 2008 ongeveer twee derde zo diep.

```{code-cell} ipython3
:label: cel-opties-crashrisico-put-index
:tags: [hide-input]

fig, axes = plt.subplots(2, 1, figsize=(10, 6.2), sharex=True, height_ratios=[2, 1])
for i, name in enumerate(cboe_excess):
    dd = hap.drawdowns(cboe[name])
    axes[0].plot(dd.index, dd["wealth"], color=hap.plotting.COLORS[i], label=name)
    axes[1].plot(dd.index, 100 * dd["drawdown"], color=hap.plotting.COLORS[i], lw=1.2)
axes[0].set_yscale("log")
axes[0].set_title("Verkopers van indexopties tegen de S&P 500, 1996-2026")
axes[0].set_ylabel("Waarde van 1 dollar (log-schaal)")
axes[0].legend()
axes[1].set_title("Drawdown")
axes[1].set_xlabel("Jaar")
axes[1].set_ylabel("Drawdown (%)")
plt.show()
```

:::{figure} #cel-opties-crashrisico-put-index
:label: fig-opties-crashrisico-put-index
:width: 95%

De PutWrite-index loopt tot 2020 gelijk op met de S&P 500 bij twee derde van de
volatiliteit, en valt in 2020 even diep en in 2008 ongeveer twee derde zo diep. Het onderste
paneel toont hoe diep, gemeten vanaf de vorige top.
:::

Na 2020 blijft de PutWrite-index achter, omdat een verkoper van verzekering niet meedoet met
een sterk stijgende markt. Israelov en Nielsen vonden in de BuyWrite-strategie dat de
verkochte volatiliteit een Sharpe-ratio van bijna één had, maar slechts 10% van het risico
droeg {cite}`IsraelovNielsen2015b`. De premie is dus reëel, maar in een indexproduct
verdund door aandelenrisico.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Sprongen verklaren de smirk, de ordening van Coval en Shumway
volgt uit een
dalende SDF, en de variance risk premium heeft het teken dat het leverage effect voorspelt.
Santa-Clara en Yan haalden uit zeven jaar optieprijzen een aandelenpremie van tien procent,
waarvan bijna een derde crashpremie, in een steekproef met een negatief gerealiseerd
overrendement. Op echte data vonden we de linksscheve risiconeutrale verdeling terug, net
als
de voorspelkracht van de premie over 1990–2007.

**Waar het breekt.** Twee meetbare feiten passen niet in dit beeld. De voorspelkracht van de
variance risk premium verdwijnt na 2007, zodat de $t$-waarde bij drie maanden over 1990–2026
nog maar $0{,}6$ is. Daarnaast is de hoge beloning voor het verkopen van puts in dertig jaar
indexdata niet te meten, omdat de Sharpe-ratio's van $0{,}62$ en $0{,}58$ minder dan een
standaardfout verschillen. De optiemarkt meet de *prijs* van crashrisico dus goed, maar
levert geen bewijs dat die prijs te hoog is.

**Risico of vergissing?** In de Chicago-lezing zijn crashes de toestanden waarin een dollar
het meest waard is, en beloont de premie een risico dat niet te hedgen is en in crises
duurder
wordt, zoals Pan vond. In de Yale-lezing wijst de stijgende SDF van Jackwerth op mispricing.
Saretto en Santa-Clara lazen hun resultaten als mispricings die kosten en marges in stand
houden, *limits of arbitrage* (de grenzen aan wat arbitrageurs met beperkt kapitaal kunnen
corrigeren) in zuivere vorm. Om de lezingen te scheiden is de SDF in crashtoestanden nodig,
en die toestanden zijn zeldzaam, zodat de data van dit college geen uitsluitsel geven.
Santa-Clara zelf staat met één been in elk kamp, want hij schatte de premie als beloning
voor
risico en liet zien dat marges die premie onbereikbaar maken.

**Wat er daarna kwam.** Hetzelfde patroon, vaak een beetje winnen en zelden veel verliezen,
bleek ook in de valutamarkt te bestaan. Daar verdient de *carry trade* (lenen in een valuta
met lage rente en beleggen in een valuta met hoge rente) een premie die in crises in één
keer
verdampt, zoals [](#05-30-wisselkoersen) laat zien.

## Oefeningen

:::{exercise}
:label: ex-opties-crashrisico-1

**Een zeldzamere crash.** Halveer in het toy-voorbeeld de crashkans tot $0{,}01$ en geef de
toestand "op" de kans $0{,}66$. Groei, $\beta$ en $\gamma$ blijven gelijk.

1. Bereken $\E[m]$ en $q_{\text{crash}}$.
2. Bereken de prijs en het verwachte bruto rendement van de put met uitoefenprijs $0{,}90$.
   Waarom verandert dat rendement niet?
:::

:::{solution} ex-opties-crashrisico-1
:class: dropdown

De SDF hangt niet van de kansen af, dus $\E[m] = 0{,}66 \cdot 0{,}6625 + 0{,}33 \cdot 1{,}1909 +
0{,}01 \cdot 7{,}4846 = 0{,}9051$ en $q_{\text{crash}} = 0{,}0748/0{,}9051 = 0{,}0827$. De put
kost $0{,}01 \cdot 7{,}4846 \cdot 0{,}30 = 0{,}0225$ en verwacht $0{,}0030$ terug, zodat zijn
verwachte bruto rendement weer $0{,}1336 = 1/m_{\text{crash}}$ is.

```{code-cell} ipython3
prob_rare = np.array([0.66, 0.33, 0.01])
Em_rare = prob_rare @ m_toy
put_price_rare = prob_rare @ (m_toy * put_toy)
pd.Series({"E[m]": Em_rare, "q crash": prob_rare[2] * m_toy[2] / Em_rare,
           "prijs put 0,90": put_price_rare, "E[R] put 0,90": (prob_rare @ put_toy) / put_price_rare,
           "1 / m crash": 1 / m_toy[2]}).round(4)
```

De code bevestigt de handberekening. Het verwachte rendement van een put die alleen in de
crash uitbetaalt, meet hoeveel een dollar in de crash waard is. Hoe vaak de crash voorkomt,
doet er niet toe.
:::

:::{exercise}
:label: ex-opties-crashrisico-2

**Crashpremies uit een machtsfunctie-SDF.** De index is een claim op consumptie, zoals in
het toy-voorbeeld. Laat op een sprongmoment de SDF met factor $J^{-\gamma}$ springen, met $\log J \sim \mathcal N(\mu_J, \delta_J^2)$ onder $\mathbb P$ en
intensiteit $\lambda^{\mathbb P}$.

1. Toon aan dat $\lambda^{\mathbb Q} = \lambda^{\mathbb P}\exp(-\gamma\mu_J + \tfrac12\gamma^2\delta_J^2)$
   en dat $\log J$ onder $\mathbb Q$ normaal is met gemiddelde $\mu_J - \gamma\delta_J^2$ en
   dezelfde spreiding.
2. Welke $\gamma$ geeft bij de sprongverdeling van de simulatie de verhouding
   $\lambda^{\mathbb Q}/\lambda^{\mathbb P} = 0{,}165/0{,}078$, en wat is dan de gemiddelde
   sprong onder $\mathbb Q$?
:::

:::{solution} ex-opties-crashrisico-2
:class: dropdown

**(1)** De risiconeutrale kans op een sprong ter grootte $j$ is de werkelijke kans maal
$j^{-\gamma}$, de sprong in de SDF, dus $\lambda^{\mathbb Q} f^{\mathbb Q}(j) = \lambda^{\mathbb P}
f(j)\, j^{-\gamma}$. Integreren geeft $\lambda^{\mathbb Q} = \lambda^{\mathbb P}\E[J^{-\gamma}]$, en
met $x = \log j$ geeft het kwadraat afmaken in
$\exp\bigl(-(x-\mu_J)^2/2\delta_J^2 - \gamma x\bigr)$ een normale dichtheid met gemiddelde
$\mu_J - \gamma\delta_J^2$.

**(2)** We lossen de vergelijking voor $\gamma$ numeriek op.

```{code-cell} ipython3
ratio = LAM_Q / LAM_P
gamma_jump = optimize.brentq(lambda g: -g * MU_J + 0.5 * g**2 * DELTA_J**2 - np.log(ratio), 0.0, 20.0)
mean_jump_q = np.exp(MU_J - gamma_jump * DELTA_J**2 + 0.5 * DELTA_J**2) - 1
print(f"lambda^Q / lambda^P = {ratio:.3f}  ->  gamma = {gamma_jump:.3f}")
print(f"gemiddelde sprong onder P: {KAPPA:.4f}, onder Q: {mean_jump_q:.4f}")
```

Een risicoaversie van ongeveer twee verdubbelt de intensiteit en maakt de gemiddelde crash
iets dieper, $-31{,}4\%$ tegen $-30\%$, dicht bij de $-31{,}6\%$ van Santa-Clara en Yan. Een
crashpremie van deze omvang vraagt dus geen extreme risicoaversie, alleen grote crashes die
met de consumptie samenvallen, zoals bij Rietz en Barro in [](#05-27-drie-antwoorden).
:::

:::{exercise}
:label: ex-opties-crashrisico-3

**Modelvrije scheefheid.** Bereken voor de twee SPY-expiraties uit de replicatie de eerste
drie risiconeutrale momenten met [](#prop-opties-crashrisico-momenten), rechtstreeks uit de
midkoersen van opties buiten het geld (trapeziumregel, zonder fit). Vergelijk volatiliteit en
scheefheid met die van de Breeden-Litzenberger-dichtheid. Welke geeft de extreemste getallen,
en waarom?
:::

:::{solution} ex-opties-crashrisico-3
:class: dropdown

```{code-cell} ipython3
bkm_rows = {}
for label, sm in smiles.items():
    otm, T, F = sm["otm"], sm["T"], sm["F"]
    K, Q_price = otm["strike"].to_numpy(), otm["mid"].to_numpy()
    x, growth_T = np.log(K / F), np.exp(r_cc * T)
    mean_r = -growth_T * np.trapezoid(Q_price / K**2, K)
    second = growth_T * np.trapezoid(2 * (1 - x) * Q_price / K**2, K)
    third = growth_T * np.trapezoid((6 * x - 3 * x**2) * Q_price / K**2, K)
    var = second - mean_r**2
    bkm_rows[label] = {"vol modelvrij": np.sqrt(var / T),
                       "scheefheid modelvrij": (third - 3 * mean_r * second + 2 * mean_r**3) / var**1.5,
                       "vol BL-dichtheid": moments(*densities[label][:2])["sd"] / np.sqrt(T),
                       "scheefheid BL-dichtheid": moments(*densities[label][:2])["scheefheid"]}
pd.DataFrame(bkm_rows).T.round(4)
```

De modelvrije momenten zijn allebei extremer. De volatiliteit is bij één maand $14{,}8\%$
tegen $12{,}3\%$ voor de dichtheid. De scheefheid heeft hetzelfde teken, maar is met
$-2{,}14$ en $-2{,}26$ veel negatiever dan de $-1{,}23$ en $-1{,}30$ van de dichtheid. De dichtheid houdt op bij de laagste
genoteerde put, terwijl in [](#eq-opties-crashrisico-spanning) de prijs van die put nog de
waarde van alle toestanden daaronder bevat. Afkappen onderschat dus beide momenten en vooral het derde,
maar de randnoteringen hebben ook de breedste marge tussen bied en laat. De linkerstaart is
daardoor ook in optieprijzen het slechtst gemeten deel van de verdeling.
:::
