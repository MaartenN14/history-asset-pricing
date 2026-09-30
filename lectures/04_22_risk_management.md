---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

(04-22-risk-management)=

# VaR, RiskMetrics en LTCM

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1994–1998, van RiskMetrics tot de redding van Long-Term Capital Management,
met een nasleep tot de Bazelse regels van 2016.

**Wat we al weten.** [ARCH, GARCH en realized volatility](#04-21-volatiliteit) maakten
het tweede moment van dag tot dag voorspelbaar, omdat volatiliteit clustert. Uit [de
momentumcrashes](#04-19-momentum) weten we bovendien dat een strategie met een mooie
Sharpe-ratio in drie maanden driekwart van de belegde waarde kan verliezen.

**Welke vraag staat open.** Kan een bank of fonds met een voorspelbaar tweede moment zijn
kans op grote verliezen meten en begrenzen, en waarom was dat in 1998 niet genoeg?
```

## Overzicht

Kan een bank met een voorspelbare volatiliteit meten en begrenzen hoeveel ze op een slechte
dag verliest? Voor een gewone slechte dag wel, maar het getal dat daarvoor werd bedacht zegt
niets over verliezen voorbij de grens, is met een jaar data nauwelijks te toetsen en mist de
spiraal van hefboom en onderpand. In dit college:

- definiëren we Value-at-Risk en Expected Shortfall en bewijzen we dat alleen de tweede
  spreiding altijd beloont
- schatten we het kwantiel met een voorspelbare volatiliteit en leiden we de backtests van
  Kupiec en Christoffersen af
- simuleren we hoe weinig een backtest van één jaar ziet, en hoe vaak dezelfde convergence
  trade bij een hogere hefboom failliet gaat
- backtesten we vier VaR-modellen op de Amerikaanse aandelenmarkt van 1990 tot 2026 en
  bekijken we de spreads van 1998.

In oktober 1994 publiceerde J.P. Morgan RiskMetrics, een methode met gratis data
{cite}`JPMorganReuters1996`. Daarmee kon elke handelaar de *Value-at-Risk* van zijn
portefeuille uitrekenen (VaR, het verlies dat met een gegeven kans, zeg 99%, over een
gegeven
horizon niet wordt overschreden). In 1996 maakte het Bazelse Comité VaR tot grondslag van
het
kapitaal tegen marktrisico, met een regel om de modellen achteraf te toetsen
{cite}`BCBS1996a,BCBS1996b`. De toetsen kwamen van {cite:t}`Kupiec1995` en
{cite:t}`Christoffersen1998`. Nadat {cite:t}`ArtznerDelbaenEberHeath1999` hadden laten zien
dat VaR spreiding kan bestraffen, stapte het Comité in 2016 over op *Expected Shortfall*
(ES,
het gemiddelde verlies voorbij het kwantiel) {cite}`BCBS2016`. Zo werd risicobeheer een
eigen vak, met een eigen leerboek {cite}`Jorion2006` en met eigen afdelingen bij banken en
toezichthouders {cite}`SantaClara2026`. Toch ging in september 1998 Long-Term Capital
Management (LTCM)
bijna
failliet, een fonds met Robert Merton en Myron Scholes onder zijn partners dat alles had wat
het vak voorschreef {cite}`Lowenstein2000`.

Al die regels en toetsen gaan over een meetinstrument en niet over een theorie van
prijzen, zodat VaR buiten de tegenstelling theorie of feit valt. Een backtest toetst
daarom geen evenwicht, maar alleen of een voorspeld kwantiel zo vaak wordt overschreden
als het belooft.

## Intuïtie: waarom zou dit waar zijn?

Een bank met honderden posities wil na elke handelsdag één getal dat zegt hoeveel ze
morgen kan verliezen. Een 99%-VaR van 40 miljoen betekent dat het verlies op één dag op de
honderd groter mag zijn. Dat getal telt obligaties, valuta en aandelen op in één munt en
beloont posities die elkaar opheffen. Omdat het verwachte rendement over één dag
verwaarloosbaar is, vraagt het alleen de volatiliteit van morgen. Het slecht meetbare
verwachte rendement telt dus niet mee, en alleen de goed meetbare volatiliteit blijft
over.

Toch heeft het getal drie zwakke plekken. De eerste is dat VaR niets zegt over de dagen
die de grens overschrijden, terwijl juist die dagen tellen.
{cite:t}`ArtznerDelbaenEberHeath1999` maakten dat punt al, en Pedro Santa-Clara herhaalt
het in de terugblik op zijn loopbaan die deze reeks volgt {cite}`SantaClara2026`.
De tweede is dat een kans van 1% slecht te controleren is, want een jaar van 250
handelsdagen geeft gemiddeld 2,5 overschrijdingen, en een model dat maar 98% dekt, geeft
er vaak niet meer dan vijf. De derde is dat VaR twee obligaties samen riskanter kan noemen
dan elk apart.

LTCM kocht effecten die net iets goedkoper waren dan vrijwel identieke andere en verkocht de
duurdere, vooral staatsobligaties van de G-7-landen. Zo'n *convergence trade* (een positie
die winst
maakt als twee prijzen naar elkaar toe bewegen) verdient een fractie van een procent,
zodat er
pas met geleend geld iets aan te verdienen valt. Op 31 augustus 1998 stond er meer dan 125
miljard dollar op de balans, tegen 4,8 miljard eigen vermogen begin dat jaar, een hefboom
van
meer dan 25 {cite}`PresidentsWorkingGroup1999`.

Verbreden de spreads, dan ziet het fonds dat dagelijks in zijn waardering
(*mark-to-market*).
Tegenpartijen vragen dan extra onderpand, en het fonds moet verkopen voordat de prijzen
convergeren. Is het fonds groot, of hebben veel fondsen dezelfde positie, dan drukt die
verkoop de prijs verder de verkeerde kant op, zodat het verlies de volgende verkoop
afdwingt.
Santa-Clara noemt hefboom, dagelijkse waardering en een termijn samen het recept voor ruïne
{cite}`SantaClara2026`.

Uit dit beeld volgen drie verwachtingen. Een backtest van één jaar laat een verkeerd model
vaak
passeren, omdat een kans van 1% in 250 dagen te weinig uitkomsten geeft. De VaR van twee
posities met een kleine kans op een groot verlies komt hoger uit dan de som van de losse
VaR's,
maar een maat die de staart middelt, doet dat niet. Ten slotte gaat dezelfde trade bij een
hogere hefboom vaker failliet, en nog vaker als de eigen verkopen de prijs bewegen.

## Toy-voorbeeld: twee posities, twee obligaties en een convergence trade

Het toy-voorbeeld bestaat uit drie kleine rekensommen die samen het college dragen. Deel
(a) laat zien waarom VaR bij normale verliezen werkt, deel (b) hoe ze spreiding kan
bestraffen en deel (c) hoe hefboom en eigen verkopen een fonds tot stoppen dwingen. Eerst
laden we de pakketten die het hele college gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model
from scipy import stats
from scipy.special import xlogy

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

We gebruiken één recept dat de theorie pas daarna afleidt, namelijk dat de VaR van een
normaal verlies met verwachting nul gelijk is aan $z_\alpha$ maal de standaarddeviatie,
met $z_{0{,}99} = 2{,}3263$. De tabel geeft de opzet van de drie delen.

| deel | opzet | wat we berekenen |
|---|---|---|
| (a) twee posities | 100 miljoen in A (dagvolatiliteit 1,5%) en 50 miljoen in B (1,0%), correlatie 0,4, verwacht rendement nul | 99%-VaR samen en apart |
| (b) twee obligaties | elk levert 2 op, of verliest 100 bij faillissement (kans 4%), onafhankelijk | 95%-VaR en 95%-ES van één en van twee |
| (c) convergence trade | eigen vermogen 100, positie 2500 (hefboom 25), spread duration 5, haircut 2% | drempels in basispunten en de verliesspiraal |

**(a) Twee posities.** De posities hebben standaarddeviaties van 1,5 en 0,5 miljoen, zodat

$$
\sigma_p^2 = 1{,}5^2 + 0{,}5^2 + 2 \times 0{,}4 \times 1{,}5 \times 0{,}5 = 3{,}10,
\qquad \sigma_p = 1{,}7607,
$$

en de 99%-VaR is $2{,}3263 \times 1{,}7607 = 4{,}096$ miljoen. Apart tellen de VaR's op tot
4,653 miljoen, zodat spreiding 0,557 miljoen scheelt. Bazel liet in 1996 de VaR van één
dag met
de wortel uit de tijd opschalen naar tien dagen {cite}`BCBS1996a`, en dan wordt ze
$\sqrt{10} \times 4{,}096 = 12{,}95$.

**(b) Twee obligaties.** Bij 95% is de VaR het kleinste verlies $x$ waarvoor de kans op
een
groter verlies hoogstens 5% is. Voor één obligatie is $P(L > -2) = 4\%$, dus de VaR is $-2$,
een winst. Twee onafhankelijke obligaties verliezen $-4$ met kans $0{,}9216$, 98 met kans
$0{,}0768$ en 200 met kans $0{,}0016$. Omdat nu $P(L > -4) = 7{,}84\%$, springt de VaR
naar 98,
ver boven de som van de losse VaR's. De Expected Shortfall op 95% middelt over de
slechtste 5%,

$$
\mathrm{ES}_1 = \frac{0{,}04 \times 100 + 0{,}01 \times (-2)}{0{,}05} = 79{,}6,
\qquad
\mathrm{ES}_2 = \frac{0{,}0016 \times 200 + 0{,}0484 \times 98}{0{,}05} = 101{,}26,
$$

en omdat 101,26 kleiner is dan $2 \times 79{,}6 = 159{,}2$, ziet ES het voordeel van
spreiden
wel.

**(c) Een convergence trade.** Het fonds neemt met eigen vermogen 100 een positie van 2500
in
een spread met *spread duration* 5, zodat het verlies 5 maal de verbreding maal de positie
is.
De tegenpartij eist een *haircut* (het deel van de positie dat met eigen geld gefinancierd
moet
zijn) van 2%, dus het vermogen moet minstens 50 blijven. Elk basispunt kost
$2500 \times 5 \times 0{,}0001 = 1{,}25$. De *margin call* (de eis om onderpand bij te
storten
of te verkopen) komt daardoor na 40 basispunten, en na 80 is het vermogen op. Bij hefboom 10
komen margin call en ruïne pas na 160 en 200 basispunten.

Stel nu dat elke verkoop van 100 de spread met 1 basispunt verbreedt, en dat het fonds op de
grens van 50 nog 10 basispunten tegenwind krijgt. Het verliest dan 12,5, zodat de positie
nog
$37{,}5/0{,}02 = 1875$ mag zijn en er 625 verkocht moet worden. Die verkoop verbreedt de
spread
met 6,25 basispunten en kost op de resterende positie $1875 \times 5 \times 0{,}000625 = 5{,}86$.
Daarna moet er nog 293 verkocht worden, wat 2,32 kost. Omdat elke ronde minder dan de
helft van de vorige kost, voegen de resterende rondes samen nog 1,3 toe. Zo komt het
proces uit op een verlies van 22,0 in plaats van 12,5, bij een verbreding van 21,0
basispunten waarvan het fonds de helft zelf veroorzaakte.

De codecel rekent de drie delen na en zet de uitkomsten naast de handberekening.

```{code-cell} ipython3
:label: cel-risk-management-toy

# (a) parametric VaR of two positions (millions)
w = np.array([100.0, 50.0])
sig = np.array([0.015, 0.010])
rho = 0.4
cov = np.array([[sig[0]**2, rho * sig[0] * sig[1]],
                [rho * sig[0] * sig[1], sig[1]**2]])
z99 = stats.norm.ppf(0.99)
sd_p = np.sqrt(w @ cov @ w)
var_p = z99 * sd_p
var_each = z99 * w * sig


def var_es_discrete(losses, probs, alpha):
    """VaR and Expected Shortfall at level alpha of a discrete loss distribution."""
    order = np.argsort(losses)
    loss, p = np.asarray(losses, float)[order], np.asarray(probs, float)[order]
    cdf = np.cumsum(p)
    var = loss[np.searchsorted(cdf, alpha - 1e-12)]
    # probability mass of each loss that lies beyond the alpha-quantile
    tail_mass = np.clip(cdf - np.maximum(cdf - p, alpha), 0.0, None)
    return var, (tail_mass * loss).sum() / (1 - alpha)


# (b) two bonds with 4% default probability
var_1, es_1 = var_es_discrete([-2.0, 100.0], [0.96, 0.04], 0.95)
var_2, es_2 = var_es_discrete([-4.0, 98.0, 200.0], [0.96**2, 2 * 0.96 * 0.04, 0.04**2], 0.95)

# (c) levered convergence trade: thresholds in bp, then a fire-sale spiral
E0, D, H, KAPPA = 100.0, 5.0, 0.02, 1e-6       # kappa: spread widening per unit sold
call_25, ruin_25 = 1e4 * (1 - H * 25) / (25 * D), 1e4 / (25 * D)
call_10, ruin_10 = 1e4 * (1 - H * 10) / (10 * D), 1e4 / (10 * D)

X, E = 2500.0, 50.0 - 2500.0 * D * 0.0010       # at the margin limit, then a 10bp shock
spread_move, round_losses = 10.0, []
while True:
    X_new = max(E, 0.0) / H
    sold = X - X_new
    if sold < 1e-9:
        break
    widening = KAPPA * sold
    loss_round = X_new * D * widening
    E -= loss_round
    spread_move += 1e4 * widening
    round_losses.append(loss_round)
    X = X_new

hand = {"sigma portefeuille": 1.7607, "VaR 99% samen": 4.096, "som losse VaR's": 4.653,
        "VaR 99% over tien dagen": 12.95, "VaR 95% één obligatie": -2.0,
        "ES 95% één obligatie": 79.6, "VaR 95% twee obligaties": 98.0,
        "ES 95% twee obligaties": 101.26, "margin call bij L = 25 (bp)": 40.0,
        "ruïne bij L = 25 (bp)": 80.0, "margin call bij L = 10 (bp)": 160.0,
        "ruïne bij L = 10 (bp)": 200.0, "spiraal, verlies ronde 1": 5.86,
        "spiraal, verlies ronde 2": 2.32, "spiraal, totaal verlies": 22.0,
        "spiraal, verbreding (bp)": 21.0}
code = [sd_p, var_p, var_each.sum(), var_p * np.sqrt(10), var_1, es_1, var_2, es_2,
        call_25, ruin_25, call_10, ruin_10, round_losses[0], round_losses[1], 50 - E, spread_move]
pd.DataFrame({"met de hand": list(hand.values()), "code": code}, index=list(hand)).round(4)
```

De twee kolommen zijn gelijk, op de afronding van de spiraal na. VaR beloont spreiding dus
zolang verliezen normaal verdeeld zijn, maar draait dat om bij een kleine kans op een
groot verlies. Deel (c) laat bovendien zien dat de hefboom, niet de trade, bepaalt na
hoeveel basispunten het fonds moet stoppen.

## Theorie

We definiëren eerst VaR en Expected Shortfall en rekenen ze uit voor een normaal verlies,
zodat ook het recept uit het toy-voorbeeld is afgeleid. Daarna volgt de kern, namelijk dat
VaR niet subadditief is en ES wel. Vervolgens schatten we het kwantiel met een
voorspelbare volatiliteit en toetsen we het achteraf, met weinig kracht per jaar. Tot slot
leiden we af na hoeveel spreadverbreding een gehefboomde arbitrageur moet stoppen, en hoe
zijn eigen verkopen dat versnellen.

### Opzet: VaR en Expected Shortfall

Beide maten vatten het verlies van morgen samen in één getal, maar ze gebruiken de staart
verschillend. Laat $W_t$ de waarde van een portefeuille zijn en $L_{t+1} = -(W_{t+1} - W_t)$
het
verlies, met kansen $P_t$ conditioneel op de informatie op $t$.

:::{prf:definition} Value-at-Risk en Expected Shortfall
:label: def-risk-management-var

De Value-at-Risk en de Expected Shortfall op betrouwbaarheid $\alpha \in (0,1)$ zijn

```{math}
:label: eq-risk-management-var
\mathrm{VaR}_{\alpha,t} = \inf\left\{x \in \mathbb{R} : P_t\!\left(L_{t+1} > x\right) \le 1-\alpha\right\},
```

```{math}
:label: eq-risk-management-es
\mathrm{ES}_{\alpha,t} = \frac{1}{1-\alpha}\int_\alpha^1 \mathrm{VaR}_{u,t}\,\mathrm{d}u ,
```

terwijl bij een continue verdeling $\mathrm{ES}_{\alpha,t} = \E_t\!\left[L_{t+1} \mid L_{t+1} \ge \mathrm{VaR}_{\alpha,t}\right]$. De ES is dan het
verwachte verlies op de dagen waarop de VaR wordt overschreden.
:::

De VaR is dus het kleinste verlies dat hoogstens met kans $1-\alpha$ wordt overschreden,
waarbij
een $\alpha$ van 0,95 of 0,99 gebruikelijk is. De ES middelt alle VaR's boven $\alpha$ en
is daarmee het
gemiddelde verlies op de slechtste fractie $1-\alpha$ van de dagen. De integraalvorm werkt
ook
bij atomen, zoals bij de obligaties uit het toy-voorbeeld. Voor een normaal verlies liggen
beide maten een vast aantal standaarddeviaties boven het gemiddelde, de ES verder dan de
VaR.

:::{prf:proposition} VaR en ES onder normaliteit
:label: prop-risk-management-normaal

Is $L_{t+1} \sim \mathcal{N}(\mu_L, \sigma^2)$ gegeven de informatie op $t$, dan is

```{math}
:label: eq-risk-management-normaal
\mathrm{VaR}_{\alpha} = \mu_L + \sigma z_\alpha,
\qquad
\mathrm{ES}_{\alpha} = \mu_L + \sigma \frac{\varphi(z_\alpha)}{1-\alpha},
\qquad z_\alpha = \Phi^{-1}(\alpha),
```

waarbij de ES-factor $\varphi(z_\alpha)/(1-\alpha)$ altijd groter is dan $z_\alpha$. De ES ligt dus verder in
de staart dan de VaR.
:::

:::{prf:proof}
Schrijf $L = \mu_L + \sigma Z$; een stijgende affiene transformatie behoudt kwantielen.
Voor de ES is $\E[Z \mid Z \ge z_\alpha] = \frac{1}{1-\alpha}\int_{z_\alpha}^\infty z\varphi(z)\,\mathrm{d}z = \frac{\varphi(z_\alpha)}{1-\alpha}$,
omdat $\varphi'(z) = -z\varphi(z)$. $\square$
:::

Bij $\alpha = 0{,}99$ is de VaR-factor 2,326, het getal uit het toy-voorbeeld, en de
ES-factor
$\varphi(2{,}326)/0{,}01 \approx 2{,}665$. Bij $\alpha = 0{,}975$ is de ES-factor 2,338,
bijna de
VaR-factor bij 99%. Daarom koos het Comité in 2016 een ES op 97,5% (paragraaf 181(b) van
{cite}`BCBS2016`). Onder een normale verdeling blijft het kapitaal dan gelijk, en alleen
dikke
staarten kosten meer.

### Het kernresultaat: VaR is niet coherent, ES wel

*Waarom zou dit waar zijn?* Een risicomaat zegt hoeveel kapitaal een bank naast een
positie moet aanhouden. Een positie die altijd slechter uitpakt, vraagt meer kapitaal.
Twee keer dezelfde positie vraagt twee keer zoveel, en een euro contant verlaagt het
vereiste kapitaal met een euro. Twee posities samen mogen niet meer vragen dan apart, want
anders daalt het vereiste kapitaal als een bank zich in afdelingen opsplitst, en worden
limieten per afdeling zinloos.

:::{prf:definition} Coherente risicomaat
:label: def-risk-management-coherent

Een risicomaat $\rho$ kent aan elk verlies een kapitaalbedrag in $\mathbb{R}$ toe. Ze is coherent
{cite}`ArtznerDelbaenEberHeath1999` als voor alle $L_1, L_2$, $c \ge 0$ en $k \in \mathbb{R}$ geldt:

1. *monotoniteit*, $L_1 \le L_2$ bijna zeker $\Rightarrow \rho(L_1) \le \rho(L_2)$
2. *subadditiviteit*, $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$
3. *positieve homogeniteit*, $\rho(cL_1) = c\,\rho(L_1)$
4. *translatie-invariantie*, $\rho(L_1 + k) = \rho(L_1) + k$.
:::

:::{prf:theorem} VaR is niet coherent, ES wel
:label: thm-risk-management-coherentie

VaR voldoet aan (1), (3) en (4), maar niet in het algemeen aan (2). ES voldoet aan alle
vier. Zijn $(L_1, L_2)$ gezamenlijk normaal, dan is VaR voor $\alpha \ge 1/2$ subadditief.
:::

Het origineel formuleert de axioma's voor toekomstige nettowaarden, en omdat wij met
verliezen
werken, draaien de tekens om. Het bewijsidee is dat een kwantiel van een som niet begrensd
wordt
door de losse kwantielen. ES is daarentegen een supremum van verwachtingen, en een
supremum van
een som is hoogstens de som van de suprema.

:::{prf:proof}
:class: dropdown

*VaR.* (1), (3) en (4) volgen omdat kwantielen behouden blijven onder stijgende
transformaties. Toy-voorbeeld (b) is een tegenvoorbeeld voor (2), want $98 > -4$.

*ES.* (1), (3) en (4) erft ES via [](#eq-risk-management-es). Voor (2) gebruiken we de
duale vorm {cite}`AcerbiTasche2002`

$$
\mathrm{ES}_\alpha(L) = \sup\left\{\E[L\,\xi] : 0 \le \xi \le \tfrac{1}{1-\alpha},\ \E[\xi] = 1\right\}.
$$

Het supremum wordt bereikt door $\xi$ maximaal te maken op de slechtste fractie $1-\alpha$ van
de uitkomsten, fractioneel op een atoom op de grens, wat het gemiddelde van de bovenste
kwantielen geeft. Een supremum van een som is hoogstens de som van de suprema, dus
$\mathrm{ES}_\alpha(L_1+L_2) \le \mathrm{ES}_\alpha(L_1) + \mathrm{ES}_\alpha(L_2)$, bij de twee obligaties 101,26 tegen $2 \times 79{,}6$.

*Normaal.* Nu is $\mathrm{VaR}_\alpha(L_1+L_2) = \mu_1 + \mu_2 + z_\alpha\sigma_{12}$ met
$\sigma_{12} = \sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2} \le \sigma_1 + \sigma_2$. Omdat
$z_\alpha \ge 0$ voor $\alpha \ge 1/2$, is dat hoogstens de som van de losse VaR's. $\square$
:::

De stelling bewijst dus wat we bij twee obligaties verwachtten, want samen krijgen ze een
VaR van 98 in plaats van $-4$, terwijl hun ES van 159,2 naar 101,26 daalt. Het normale
geval verklaart waarom de
praktijk het probleem lang niet zag, want bij aandelen en valuta gedraagt VaR zich netjes.
Het gaat pas mis bij een kleine kans op een groot verlies, zoals bij kredietrisico,
verkochte opties en convergence trades.

### Wat het voorspelt: het kwantiel uit een voorspelbare volatiliteit

Met een voorspelbare volatiliteit is het kwantiel van morgen op drie manieren te schatten,
die
verschillen in waar de vorm van de staart vandaan komt. Met posities $\mathbf{w}$ in dollar,
covariantiematrix $\boldsymbol{\Sigma}_t$ en verwachte rendementen nul is de parametrische
VaR

```{math}
:label: eq-risk-management-parametrisch
\mathrm{VaR}_{\alpha,t} = z_\alpha \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma}_t \mathbf{w}} ,
```

het recept van toy-deel (a) voor een hele portefeuille. De drie manieren zijn:

- **parametrisch**, met [](#eq-risk-management-parametrisch). Zo werkte RiskMetrics, dat het
  verwachte dagrendement op nul zette (p. 92–93 van {cite}`JPMorganReuters1996`) en met 95%
  rekende, terwijl Bazel 99% eiste.
- **historische simulatie**, die de rendementen van de afgelopen $K$ dagen op de huidige
  posities
  toepast en het empirische kwantiel afleest. Dat vraagt geen verdelingsaanname, maar een
  crash
  telt $K$ dagen mee en valt er dan in één keer uit.
- **filtered historical simulation**
  {cite}`HullWhite1998,BaroneAdesiGiannopoulosVosper1999`,
  die de staart haalt uit historische rendementen gedeeld door de volatiliteit van toen,
  en het
  niveau uit de volatiliteit van morgen.

RiskMetrics zocht voor 480 reeksen één volatiliteitsschatter die snel op schokken reageert
en
geen parameters per reeks vraagt. Het koos de *exponentially weighted moving average*
(EWMA),

```{math}
:label: eq-risk-management-ewma
\sigma_{t+1}^2 = \lambda\,\sigma_t^2 + (1-\lambda)\,r_t^2
= (1-\lambda)\sum_{j=0}^{\infty} \lambda^j r_{t-j}^2 ,
```

waarin elke dag ouder een factor $\lambda$ minder weegt. Een hogere $\lambda$ maakt de
schatting
dus trager. RiskMetrics koos $\lambda = 0{,}94$ voor dagdata, de waarde die de
voorspelfout over
alle reeksen minimaliseert (§5.3.2.2 van {cite}`JPMorganReuters1996`). Dan dragen de laatste
$\ln 0{,}01/\ln 0{,}94 \approx 74$ dagen 99% van het gewicht, zodat een crash na een
kwartaal
vrijwel vergeten is.

Vergelijk dat met GARCH(1,1) uit [het vorige college](#04-21-volatiliteit)
{cite}`Engle1982,Bollerslev1986`,

```{math}
:label: eq-risk-management-garch
\sigma_{t+1}^2 = \omega + a\, r_t^2 + b\,\sigma_t^2 ,
```

met $a$ en $b$ in plaats van $\alpha$ en $\beta$, die hier al bezet zijn. EWMA is het geval
$\omega = 0$, $a = 1-\lambda$ en $b = \lambda$. Dan is $a + b = 1$, het *integrated*
GARCH-model
van {cite:t}`EngleBollerslev1986`, waarin een schok nooit uitdooft. Voor één dag vooruit
maakt
dat weinig uit, omdat dan vooral telt hoe snel het model op een schok reageert.

### Hoe het getoetst wordt: Kupiec en Christoffersen

Een VaR-model wordt achteraf getoetst door te tellen hoe vaak het verlies de VaR
overschreed, en
of die overschrijdingen clusteren. Geeft een model elke dag het juiste kwantiel, dan is de
kans
op een overschrijding elke dag $p = 1-\alpha$, wat er eerder ook gebeurde. De reeks
overschrijdingen (*hit sequence*) $I_{t+1} = \mathbb{1}\{L_{t+1} > \mathrm{VaR}_{\alpha,t}\}$
bestaat dan uit onafhankelijke muntworpen.

:::{prf:proposition} Hits zijn Bernoulli
:label: prop-risk-management-hits

Is $\mathrm{VaR}_{\alpha,t}$ het ware conditionele $\alpha$-kwantiel van een continu verdeeld
verlies, dan zijn de $I_{t+1}$ onafhankelijke Bernoulli-variabelen met kans $1-\alpha$. Hun
aantal in $T$ dagen is dan binomiaal verdeeld.
:::

:::{prf:proof}
Per definitie is $P_t(I_{t+1} = 1) = 1-\alpha$, en $I_1, \dots, I_t$ zitten in de informatie
op $t$, dus $P(I_{t+1} = 1 \mid I_1, \dots, I_t) = 1-\alpha$. Dan is de kans op elk patroon
het product van de marginale kansen. $\square$
:::

{cite:t}`Kupiec1995` toetste het aantal. Met $x$ overschrijdingen in $T$ dagen en fractie
$\hat\pi = x/T$ vergelijkt de *proportion-of-failures*-toets de kans op de waargenomen reeks
onder $p$ met die onder $\hat\pi$,

```{math}
:label: eq-risk-management-kupiec
\mathrm{LR}_{\mathrm{pof}} = -2\ln\frac{(1-p)^{T-x}p^{x}}{(1-\hat\pi)^{T-x}\hat\pi^{x}}
\;\overset{a}{\sim}\; \chi^2_1 ,
```

en hoe verder $\hat\pi$ van $p$ ligt, hoe groter de statistiek. Boven 3,84 verwerpt de
toets op
5%. {cite:t}`Christoffersen1998` toetste ook het patroon. Laat $n_{ij}$ tellen hoe vaak
$I_t = i$ werd gevolgd door $I_{t+1} = j$, met $\hat\pi_{01} = n_{01}/(n_{00}+n_{01})$,
$\hat\pi_{11} = n_{11}/(n_{10}+n_{11})$ en $\hat\pi$ de totale fractie. Tegen een
Markov-keten
als alternatief is

```{math}
:label: eq-risk-management-christoffersen
\mathrm{LR}_{\mathrm{ind}} = -2\ln\frac{(1-\hat\pi)^{n_{00}+n_{10}}\hat\pi^{n_{01}+n_{11}}}
{(1-\hat\pi_{01})^{n_{00}}\hat\pi_{01}^{n_{01}}(1-\hat\pi_{11})^{n_{10}}\hat\pi_{11}^{n_{11}}}
\;\overset{a}{\sim}\; \chi^2_1,
\qquad
\mathrm{LR}_{\mathrm{cc}} = \mathrm{LR}_{\mathrm{pof}} + \mathrm{LR}_{\mathrm{ind}}
\;\overset{a}{\sim}\; \chi^2_2 .
```

De eerste statistiek wordt groot als een overschrijding vaker op een overschrijding volgt
dan
op een rustige dag. De tweede toetst aantal en patroon samen (*conditional coverage*), zodat
een statisch model met het juiste totaal toch kan falen.

Bazel telt alleen het aantal. Over 250 dagen staat het verkeerslicht op groen bij 0 tot 4
overschrijdingen, op geel bij 5 tot 9 en op rood bij 10 of meer. In het gele gebied stijgt
de
vermenigvuldigingsfactor op het kapitaal, die minimaal 3 is, en in het rode gebied met 1
{cite}`BCBS1996a,BCBS1996b`. Het Comité schreef zelf dat zulke toetsen een goed model maar
beperkt van een slecht model kunnen onderscheiden (p. 5 van {cite}`BCBS1996b`). De cel
hieronder programmeert
beide
toetsen en zet de zones naast de binomiale kansen.

```{code-cell} ipython3
def kupiec_lr(hits, p=0.01):
    """Kupiec (1995) proportion-of-failures LR statistic; hits along the last axis."""
    # TODO: naar hap.stats
    hits = np.asarray(hits, float)
    T, x = hits.shape[-1], hits.sum(axis=-1)
    pi_hat = x / T
    return -2 * ((xlogy(T - x, 1 - p) + xlogy(x, p)) - (xlogy(T - x, 1 - pi_hat) + xlogy(x, pi_hat)))


def christoffersen_lr(hits, p=0.01):
    """Christoffersen (1998) independence and conditional-coverage LR statistics."""
    # TODO: naar hap.stats
    hits = np.asarray(hits, float)
    h0, h1 = hits[..., :-1], hits[..., 1:]
    n00, n01 = ((1 - h0) * (1 - h1)).sum(-1), ((1 - h0) * h1).sum(-1)
    n10, n11 = (h0 * (1 - h1)).sum(-1), (h0 * h1).sum(-1)
    pi01, pi11 = n01 / np.maximum(n00 + n01, 1), n11 / np.maximum(n10 + n11, 1)
    pi = (n01 + n11) / (n00 + n01 + n10 + n11)
    lr_ind = -2 * ((xlogy(n00 + n10, 1 - pi) + xlogy(n01 + n11, pi))
                   - (xlogy(n00, 1 - pi01) + xlogy(n01, pi01) + xlogy(n10, 1 - pi11) + xlogy(n11, pi11)))
    return lr_ind, kupiec_lr(hits, p) + lr_ind


k = np.arange(11)
basel = pd.DataFrame({"overschrijdingen": k,
                      "P(X <= k), p = 1%": stats.binom.cdf(k, 250, 0.01),
                      "P(X >= k), p = 2%": stats.binom.sf(k - 1, 250, 0.02),
                      "LR_pof": kupiec_lr(np.array([np.r_[np.ones(i), np.zeros(250 - i)] for i in k]))})
basel["zone"] = pd.cut(basel["overschrijdingen"], [-1, 4, 9, 250], labels=["groen", "geel", "rood"])
basel.round(4)
```

De tweede kolom reproduceert tabel 2 van het Bazelse kader, met 95,88% bij vijf en 99,99%
bij
tien overschrijdingen, en daar liggen de grenzen van geel en rood. De derde kolom laat het
probleem zien, want een model dat maar 98% dekt, blijft met kans 44% groen. Kupiec
verwerpt op
5% alleen bij nul of bij zeven en meer overschrijdingen.

Het probleem is hetzelfde als bij [de standaardfout van 2%](#00-01-rendementen), maar dan
in de staart. Een kans van 1% geschat uit 250 dagen heeft een standaardfout van
$\sqrt{0{,}01 \times 0{,}99/T} = 0{,}63$ procentpunt bij $T = 250$, 63% van de kans zelf,
en die standaardfout daalt alleen met de wortel van het aantal dagen $T$. Zoals een
gemiddeld rendement een eeuw data vraagt, is één jaar veel te kort om een VaR-model te
beoordelen.

### De gehefboomde arbitrageur

*Waarom zou dit waar zijn?* Een arbitrageur met een positieve verwachte opbrengst kan
failliet
gaan zonder ongelijk te hebben. Door de hefboom is een kleine prijsbeweging een groot deel
van
zijn vermogen. Door de dagelijkse waardering is die beweging meteen een verlies, en door het
onderpand volgt meteen een gedwongen verkoop. Duwt die verkoop de prijs verder weg, dan
groeit
het verlies vanzelf.

Vanaf hier staat $L$ voor de hefboom en niet meer voor het verlies. Laat $E_t$ het eigen
vermogen zijn, $X_t = L_t E_t$ de positie met hefboom $L_t$, en
$r_{t+1} = c - D\,\Delta s_{t+1}$ het rendement per eenheid, met *carry* $c$ (de opbrengst
als er
niets gebeurt), spread duration $D$ en spreadverbreding $\Delta s_{t+1}$. Dan is

```{math}
:label: eq-risk-management-vermogen
E_{t+1} = E_t + X_t\, r_{t+1} = E_t\left(1 + L_t\, r_{t+1}\right),
```

en de tegenpartij eist $E_t \ge h X_t$ met haircut $h$. Bij hefboom 25 en duration 5 kost
elk
basispunt zo 1,25% van het vermogen, zoals in het toy-voorbeeld.

:::{prf:proposition} Drempels voor margin call en ruïne
:label: prop-risk-management-drempel

Houdt het fonds $X = L E_0$ vast met $L < 1/h$ en verwaarloosbare carry, dan komen de margin
call en de ruïne bij een cumulatieve verbreding van

```{math}
:label: eq-risk-management-drempel
\Delta s^{\mathrm{call}} = \frac{1 - hL}{L D},
\qquad
\Delta s^{\mathrm{ru\ddot{\imath}ne}} = \frac{1}{L D} .
```

Beide drempels dalen dus met $1/L$, zodat een fonds met meer hefboom eerder moet stoppen.
:::

:::{prf:proof}
Na een verbreding $\Delta s$ is $E = E_0(1 - LD\Delta s)$. Stel gelijk aan $hLE_0$,
respectievelijk nul. $\square$
:::

Met de toy-getallen geeft dat 40 en 80 basispunten. De Sharpe-ratio $\E[Xr]/\SD(Xr)$ hangt
daarentegen niet van $L$ af, want de hefboom schaalt teller en noemer even hard. Ze zegt
dus niets over de kans om te overleven, zodat een hogere hefboom het fonds al kwetsbaarder
maakt voordat zijn eigen verkopen meetellen. Om die verkopen mee te nemen, laten we een
verkoop van $q$ eenheden de spread met $\kappa q$ verbreden, terwijl het fonds precies op
de grens staat.

:::{prf:proposition} Verliesspiraal
:label: prop-risk-management-spiraal

Staat het fonds op de grens $X = E/h$ en krijgt het een exogeen verlies $\mathrm{d}E^{\mathrm{exo}} < 0$,
dan is het totale verlies in lineaire benadering

```{math}
:label: eq-risk-management-spiraal
\mathrm{d}E = \frac{\mathrm{d}E^{\mathrm{exo}}}{1 - \theta},
\qquad
\theta = \frac{X D \kappa}{h},
```

zolang $\theta < 1$. Bij $\theta \ge 1$ divergeert de reeks en stopt de spiraal pas als de
positie grotendeels is afgebouwd.
:::

:::{prf:proof}
Een verlies $\delta$ verlaagt de toegestane positie met $\delta/h$. Die verkoop verbreedt de
spread met $\kappa\delta/h$ en kost op $X$ nog $\theta\delta$, wat een verkoop van $\theta\delta/h$
en een verlies $\theta^2\delta$ oplevert, enzovoort: $\delta(1 + \theta + \theta^2 + \dots)$. $\square$
:::

Het verlies wordt dus met $1/(1-\theta)$ vergroot, en $\theta$ stijgt met de positie en de
prijsimpact en daalt met de haircut. In het toy-voorbeeld is
$\theta = 2500 \times 5 \times 10^{-6}/0{,}02 = 0{,}625$, zodat de lineaire benadering
$12{,}5/0{,}375 = 33{,}3$ geeft. Dat is meer dan de werkelijke 22,0, omdat $\theta$ daalt
naarmate de positie krimpt.

In het klein is dit het mechanisme van {cite:t}`ShleiferVishny1997`. Arbitrageurs verliezen
financiering als de prijs tegen hen beweegt, zodat ze een mispricing niet kunnen corrigeren
wanneer die het grootst is. {cite:t}`BrunnermeierPedersen2009` lieten daarnaast de haircut
met
de volatiliteit stijgen, wat de spiraal versterkt.

```{admonition} Samengevat
:class: tip

- VaR is een kwantiel van het verlies en ES het gemiddelde erachter. Onder normaliteit zijn ze
  $2{,}326\,\sigma$ bij 99% en $2{,}338\,\sigma$ bij 97,5%, [](#eq-risk-management-normaal).
- VaR kan spreiding bestraffen en ES niet, [](#thm-risk-management-coherentie). Dat gebeurt bij
  een kleine kans op een groot verlies.
- Het kwantiel komt uit een voorspelbare volatiliteit, en EWMA is GARCH met $a + b = 1$,
  [](#eq-risk-management-ewma). Een hogere $\lambda$ maakt de VaR trager.
- Een backtest telt overschrijdingen, [](#eq-risk-management-kupiec), en wint kracht met de
  wortel van het aantal dagen $T$.
- Margin call en ruïne komen na een verbreding die daalt met $1/L$,
  [](#eq-risk-management-drempel), en eigen prijsdruk vergroot het verlies met $1/(1-\theta)$,
  [](#eq-risk-management-spiraal).
- De simulatie vraagt hoe vaak een backtest van 250 dagen een fout model vindt, en hoe vaak
  één convergence trade binnen vijf jaar failliet gaat bij stijgende $L$ en $\kappa$.
```

## Simulatie: wat een korte steekproef over de staart zegt

Hoeveel ziet een korte steekproef van een risico dat in de staart zit? We beantwoorden die
vraag eerst voor de toezichthouder, die één jaar overschrijdingen heeft om een VaR-model
te beoordelen, en daarna voor een fonds met vier goede jaren.

### Een jaar backtest

We simuleren 2000 paden uit GARCH(1,1) met $a = 0{,}08$ en $b = 0{,}91$, een
onvoorwaardelijke volatiliteit van 16% per jaar en Student-$t$-schokken met zes
vrijheidsgraden. Vier modellen voorspellen de 99%-VaR:

- het **ware** conditionele kwantiel
- een **statisch normaal** model met de perfect gekende onvoorwaardelijke volatiliteit
- **historische simulatie** over 250 dagen
- **EWMA** met $\lambda = 0{,}94$ en het normale kwantiel.

Daarna tellen we hoe vaak Kupiec en Christoffersen op 5% verwerpen na 250, 500 en 1000
dagen.
Ook tellen we hoe vaak een model na een jaar rood is.

```{code-cell} ipython3
A_GARCH, B_GARCH = 0.08, 0.91   # daily GARCH(1,1), persistence 0.99
N_PATHS, BURN, WINDOW, T_MAX = 2000, 500, 250, 1000
NU, VOL_ANN = 6.0, 0.16
var_bar = VOL_ANN**2 / 252
n_days = BURN + WINDOW + T_MAX

z_t = rng.standard_t(NU, size=(n_days, N_PATHS)) * np.sqrt((NU - 2) / NU)
sigma2, r_sim = np.empty((n_days, N_PATHS)), np.empty((n_days, N_PATHS))
ewma2 = np.empty((n_days, N_PATHS))
sigma2[0] = ewma2[0] = var_bar
for t in range(n_days):
    r_sim[t] = np.sqrt(sigma2[t]) * z_t[t]
    if t + 1 < n_days:
        sigma2[t + 1] = var_bar * (1 - A_GARCH - B_GARCH) + A_GARCH * r_sim[t]**2 + B_GARCH * sigma2[t]
        ewma2[t + 1] = 0.94 * ewma2[t] + 0.06 * r_sim[t]**2

start = BURN + WINDOW
q_t = stats.t.ppf(0.99, NU) * np.sqrt((NU - 2) / NU)
var_models = {
    "waar": np.sqrt(sigma2[start:]) * q_t,
    "normaal, constant": np.full((T_MAX, N_PATHS), z99 * np.sqrt(var_bar)),
    "historisch 250d": np.array([-np.quantile(r_sim[t - WINDOW:t], 0.01, axis=0) for t in range(start, n_days)]),
    "EWMA 0,94": z99 * np.sqrt(ewma2[start:]),
}
hits_sim = {name: (-r_sim[start:] > v).T.astype(float) for name, v in var_models.items()}

rows = {}
for name, hits in hits_sim.items():
    for T in (250, 500, 1000):
        lr_ind, lr_cc = christoffersen_lr(hits[:, :T])
        rows[(name, T)] = {"fractie overschrijdingen": hits[:, :T].mean(),
                           "Kupiec verwerpt": (kupiec_lr(hits[:, :T]) > stats.chi2.ppf(0.95, 1)).mean(),
                           "Christoffersen verwerpt": (lr_cc > stats.chi2.ppf(0.95, 2)).mean(),
                           "rood na een jaar": (hits[:, :250].sum(axis=1) >= 10).mean()}
sim_table = pd.DataFrame(rows).T
sim_table.index.names = ["model", "T"]
sim_table.round(3)
```

Alleen het ware model komt op 1% overschrijdingen uit, en na een jaar laten beide toetsen
elk fout model vaker door dan dat ze het verwerpen. Wat in de figuur telt, is de
hoogte van de lijnen bij de stippellijn van één jaar, links gesimuleerd en rechts exact
berekend.

```{code-cell} ipython3
:label: cel-risk-management-kracht
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
for i, name in enumerate(hits_sim):
    rej = sim_table.loc[name, "Kupiec verwerpt"]
    axes[0].plot(rej.index, rej.values, "o-", color=hap.plotting.COLORS[i], label=name)
axes[0].axhline(0.05, color="black", lw=0.8, ls="--")
axes[0].set_title("(a) Verwerpingskans Kupiec (5%) in GARCH-t-wereld")
axes[0].set_xlabel("Lengte backtest (dagen)")
axes[0].set_ylabel("Fractie paden verworpen")
axes[0].legend()

T_grid = np.unique(np.geomspace(100, 10_000, 60).astype(int))
for i, coverage in enumerate([0.99, 0.985, 0.98, 0.97]):
    power = []
    for T in T_grid:
        x = np.arange(T + 1)
        pi_hat = x / T
        # Kupiec LR for every possible count x (kupiec_lr takes a hit series)
        lr = -2 * ((xlogy(T - x, 0.99) + xlogy(x, 0.01)) - (xlogy(T - x, 1 - pi_hat) + xlogy(x, pi_hat)))
        power.append(stats.binom.pmf(x, T, 1 - coverage)[lr > stats.chi2.ppf(0.95, 1)].sum())
    axes[1].plot(T_grid, power, color=hap.plotting.COLORS[i], label=f"ware dekking {coverage:.1%}")
axes[1].axvline(250, color="black", lw=0.8, ls=":")
axes[1].set_xscale("log")
axes[1].set_title("(b) Kracht van Kupiec tegen de ware dekking")
axes[1].set_xlabel("Lengte backtest (dagen, log-schaal)")
axes[1].set_ylabel("Verwerpingskans")
axes[1].legend()
fig.tight_layout()
plt.show()
```

:::{figure} #cel-risk-management-kracht
:label: fig-risk-management-kracht
:width: 100%

Links: een statisch model met perfect gekende onvoorwaardelijke volatiliteit wordt na een jaar
in minder dan de helft van de paden verworpen, en EWMA met normale staarten in een op de zeven.
Rechts, exact binomiaal: om een model dat 98% in plaats van 99% dekt met kans 80% te betrappen,
zijn enkele jaren dagdata nodig. De stippellijn is het jaar van Bazel.
:::

Zelfs het ware model wordt na 250 dagen in 8,8% van de paden verworpen in plaats van 5%,
omdat
de $\chi^2$-benadering bij 2,5 verwachte overschrijdingen grof is. Het statische model
wordt op
1,5% van de dagen overschreden en na een jaar in 46% van de paden verworpen. Dat stijgt
nauwelijks met de lengte van de backtest, want de overschrijdingen clusteren, zodat een
periode
zonder volatiliteitsgolf het goede aantal geeft.

EWMA wordt door zijn normale staart op 1,8% van de dagen overschreden, wat Kupiec na een
jaar in 15% van de paden ziet. Het rechterpaneel maakt de les algemeen. Een model met 98%
dekking wordt na 250 dagen maar met kans 24% verworpen, de 0,236 voor zeven of meer
overschrijdingen uit de Bazelse tabel plus 0,006 voor nul. Een backtest van één jaar laat
een fout model dus, zoals verwacht, meestal passeren, om dezelfde reden als bij een
gemiddeld rendement, want de standaardfout is groot naast de grootheid zelf.

### Vier goede jaren van een convergence trade

Nu zetten we [](#prop-risk-management-spiraal) op schaal, met duration 5 en haircut 2% uit
het
toy-voorbeeld. Een spreadafwijking in basispunten volgt $x_{t+1} = 0{,}99\,x_t + \eta_{t+1}$.
De
dagschok $\eta$ is normaal met een standaarddeviatie van 1,5 basispunt. Gemiddeld eens in de
drie jaar komt daar een exponentieel verdeelde sprong van gemiddeld 30 basispunten bij, en
het
gemiddelde daarvan wordt afgetrokken.

De positie levert een carry van 1% per jaar. Het fonds begint met vermogen 1, zet de positie
elke maand terug op $L$ maal het vermogen, en moet verkopen zodra $E < hX$. We simuleren
4000
paden van 1260 handelsdagen, met dezelfde schokken voor elke hefboom. Eerst kijken we wat
het
fonds uit zijn eigen rendementen over de trade kan leren.

```{code-cell} ipython3
N_FUND, T_FUND = 4000, 1260
PHI, SIG_BP, P_JUMP, MU_JUMP, CARRY, KAPPA_FS = 0.99, 1.5, 1 / 750, 30.0, 0.01, 2.0

jump = (rng.random((T_FUND, N_FUND)) < P_JUMP) * rng.exponential(MU_JUMP, (T_FUND, N_FUND))
eta = SIG_BP * rng.standard_normal((T_FUND, N_FUND)) + jump - P_JUMP * MU_JUMP
x_spread = np.zeros((T_FUND + 1, N_FUND))
for t in range(T_FUND):
    x_spread[t + 1] = PHI * x_spread[t] + eta[t]
dx_spread = np.diff(x_spread, axis=0)
r_trade = CARRY / 252 - D * dx_spread / 1e4

sr_true = np.sqrt(252) * r_trade.mean() / r_trade.std()
sr_4y = np.sqrt(252) * r_trade[:1008].mean(axis=0) / r_trade[:1008].std(axis=0)
no_jump_4y = jump[:1008].sum(axis=0) == 0
pd.Series({"Sharpe-ratio (populatie, alle paden)": sr_true,
           "volatiliteit per jaar": np.sqrt(252) * r_trade.std(),
           "scheefheid dagrendement": stats.skew(r_trade.ravel()),
           "fractie 4-jaarsrecords zonder sprong": no_jump_4y.mean(),
           "mediane Sharpe over 4 jaar, zonder sprong": np.median(sr_4y[no_jump_4y]),
           "mediane Sharpe over 4 jaar, met sprong": np.median(sr_4y[~no_jump_4y])}).round(3)
```

De trade heeft een Sharpe-ratio van 0,58, maar de scheefheid van de dagrendementen is $-21$,
zodat er bijna altijd een beetje winst is en zelden een groot verlies. In 27% van de
vierjaarsperiodes komt geen sprong voor, en daar is de mediane Sharpe-ratio met 0,88 veel
hoger. Een fonds met
vier goede jaren achter de rug, zoals LTCM in 1994–1997, kan dus met reden denken dat zijn
trade
beter is dan ze is.

De functie hieronder laat het fonds elke dag zijn vermogen bijwerken, verkopen zodra het
vermogen onder de haircut zakt en elke maand de hefboom herstellen. We draaien de functie
eerst zonder prijsdruk.

```{code-cell} ipython3
def run_fund(leverage, kappa):
    """Simulate a levered convergence-trade fund with margin constraint E >= H X and fire-sale impact."""
    E = np.ones(N_FUND)
    X = leverage * E
    impact = np.zeros(N_FUND)
    alive = np.ones(N_FUND, bool)
    called = np.zeros(N_FUND, bool)
    for t in range(T_FUND):
        d_impact = (PHI - 1) * impact
        impact += d_impact
        E = np.where(alive, E + X * (CARRY / 252 - D * (dx_spread[t] + d_impact) / 1e4), E)
        for _ in range(100):                                  # forced sales until the constraint holds
            breach = alive & (X > E / H + 1e-12)
            if not breach.any():
                break
            called |= breach
            X_new = np.where(breach, np.maximum(E, 0.0) / H, X)
            widening = kappa * (X - X_new)                    # bp
            impact += widening
            E = E - X_new * D * widening / 1e4
            X = X_new
            alive &= E > 0
            X = np.where(alive, X, 0.0)
        if (t + 1) % 21 == 0:
            X = np.where(alive, leverage * E, 0.0)
    return {"P(margin call)": called.mean(), "P(ruïne)": 1 - alive.mean(),
            "mediaan eindvermogen": np.median(np.where(alive, E, 0.0))}


LEVERAGES = [1, 5, 10, 15, 20, 25, 30]
fund_no_fs = pd.DataFrame({L: run_fund(L, 0.0) for L in LEVERAGES}).T
fund_no_fs.round(3)
```

Zonder prijsdruk stijgt de kans op ruïne binnen vijf jaar van 0,2% bij hefboom 10 naar
11,3% bij hefboom 25, terwijl de mediane eindwaarde stijgt van 1,57 naar 2,56 keer het
beginvermogen. Het typische pad beloont de hefboom dus, en de staart straft hem. In de
tweede run laat elke gedwongen verkoop van één eenheid beginvermogen de spread met 2
basispunten verbreden, een *fire sale* (een gedwongen verkoop die de prijs drukt) waarvan
de druk even snel wegebt als de rest van de spread.

```{code-cell} ipython3
fund_fs = pd.DataFrame({L: run_fund(L, KAPPA_FS) for L in LEVERAGES}).T
pd.concat({"zonder fire sale": fund_no_fs, "met fire sale": fund_fs}, axis=1).round(3)
```

Met prijsdruk blijft de kans op een margin call gelijk, want de eerste call komt vóór elke
gedwongen verkoop. De kans op ruïne stijgt bij hefboom 25 wel, van 11,3% naar 23,6%,
terwijl er bij hefboom 10 of minder geen verschil is. Dezelfde trade gaat dus bij een
hogere hefboom vaker failliet, en met eigen prijsdruk nog vaker, zoals we verwachtten.

Waarom de prijsdruk pas bij hoge hefboom telt, volgt uit $\theta$ in
[](#prop-risk-management-spiraal). De prijsimpact is hier 2 basispunten per eenheid
beginvermogen, twee keer die van het toy-voorbeeld, waar een verkoop van 100 bij vermogen
100 de spread 1 basispunt verbreedde. Bij een call is de positie ongeveer $L$ keer het
beginvermogen, zodat $\theta = XD\kappa/h \approx 0{,}05\,L$. Bij hefboom 10 is $\theta$
dus 0,5 en komt het fonds bovendien zelden aan zijn limiet, want de kans op een margin
call is daar 0,9%. Bij hefboom 20 is $\theta$ precies 1 en bij hefboom 25 al groter dan 1,
zodat de spiraal volgens de propositie divergeert. In de figuur is dat de afstand tussen
de twee
ruïnelijnen boven hefboom 20.

```{code-cell} ipython3
:label: cel-risk-management-ltcm-sim
:tags: [hide-input]

fig, ax = plt.subplots()
ax.plot(LEVERAGES, fund_no_fs["P(ruïne)"], "o-", color=hap.plotting.COLORS[0], label="ruïne, zonder fire sale")
ax.plot(LEVERAGES, fund_fs["P(ruïne)"], "o-", color=hap.plotting.COLORS[1], label="ruïne, met fire sale")
ax.plot(LEVERAGES, fund_no_fs["P(margin call)"], "s--", color=hap.plotting.COLORS[7], label="margin call (beide)")
ax.set_title(f"Zelfde trade, zelfde Sharpe-ratio ({sr_true:.2f}), andere hefboom")
ax.set_xlabel("Hefboom L (positie / eigen vermogen)")
ax.set_ylabel("Kans binnen vijf jaar")
ax.legend()
plt.show()
```

:::{figure} #cel-risk-management-ltcm-sim
:label: fig-risk-management-ltcm-sim
:width: 90%

De Sharpe-ratio van de trade is bij elke hefboom dezelfde, maar de kans op een margin call en
op ruïne binnen vijf jaar stijgt steil met de hefboom. Vanaf hefboom 25 verdubbelt de eigen
prijsdruk de kans op ruïne ruimschoots, terwijl ze tot hefboom 10 geen rol speelt.
:::


## Replicatie op echte data

### VaR-backtest 1990–2026

```{admonition} Replicatie
:class: seealso

**Bron.** Het rekenrecept komt uit RiskMetrics {cite}`JPMorganReuters1996` en de zones uit het
Bazelse backtestkader {cite}`BCBS1996b`. De toetsen zijn van {cite:t}`Kupiec1995` en
{cite:t}`Christoffersen1998`.

**Wat.** De toetsen [](#eq-risk-management-kupiec) en [](#eq-risk-management-christoffersen) op
een 99%-VaR voor één dag, met $\lambda = 0{,}94$ uit RiskMetrics. Tabel 2 van het Bazelse kader
staat al hierboven.

**Data hier.** Het dagelijkse marktrendement uit de Kenneth French Data Library via
`hap.data.market_daily()`. De backtest loopt van januari 1990 tot juli 2026.

**Verschil met het origineel.** Bazel toetst handelsresultaten met wisselende posities, en wij
een vaste positie in één index. GARCH schatten we eenmaal op 1963–1989, zodat de backtest niet
vooruitkijkt.

**Verwachte afwijking.** Het statische normale model heeft duidelijk meer dan 1%
overschrijdingen, geclusterd in crisisjaren. EWMA en GARCH zitten dichter bij 1% maar erboven,
door hun normale staart.
```

We bouwen de vier VaR-reeksen, elk met alleen informatie tot en met de dag ervoor, en
schatten
GARCH op de jaren vóór 1990.

```{code-cell} ipython3
market = hap_data.market_daily()["Mkt"].loc["1963-07-01":]
z01 = stats.norm.ppf(0.01)

var_bt = pd.DataFrame(index=market.index)
var_bt["normaal, constant"] = -(market.expanding(250).mean() + z01 * market.expanding(250).std()).shift(1)
var_bt["historisch 250d"] = -market.rolling(250).quantile(0.01).shift(1)
var_bt["EWMA 0,94"] = -z01 * np.sqrt((market**2).ewm(alpha=0.06, adjust=False).mean().shift(1))

garch = arch_model(100 * market, mean="Constant", vol="GARCH", p=1, q=1, dist="normal")
garch_fit = garch.fit(last_obs="1990-01-01", disp="off")
garch_fc = garch_fit.forecast(start="1990-01-01", horizon=1, reindex=False)
var_bt["GARCH(1,1)"] = (-(garch_fit.params["mu"] + z01 * np.sqrt(garch_fc.variance["h.1"])) / 100).shift(1)

var_bt = var_bt.loc["1990-01-01":].dropna()
loss_bt = -market.loc[var_bt.index]
hits_bt = var_bt.lt(loss_bt, axis=0).astype(int)
garch_fit.params.round(4)
```

Het GARCH-model heeft $a = 0{,}092$ en $b = 0{,}905$, een persistentie van 0,997, en ligt
dus dicht bij de EWMA van RiskMetrics, waarvoor $a + b$ precies 1 is. Daarna tellen we per
model de overschrijdingen, de toetsen en de zones per volledig jaar.

```{code-cell} ipython3
full_years = hits_bt.loc[:"2025"]
by_year = full_years.groupby(full_years.index.year)
summary_bt = {}
for name in hits_bt:
    lr_ind, lr_cc = christoffersen_lr(hits_bt[name].to_numpy())
    lr_pof = kupiec_lr(hits_bt[name].to_numpy())
    yearly_counts = by_year[name].sum()
    yearly_cc = by_year[name].apply(lambda h: christoffersen_lr(h.to_numpy())[1])
    summary_bt[name] = {"dagen": len(hits_bt), "overschrijdingen": hits_bt[name].sum(),
                        "fractie (%)": 100 * hits_bt[name].mean(),
                        "LR_pof": lr_pof, "LR_ind": lr_ind, "LR_cc": lr_cc,
                        "p-waarde cc": stats.chi2.sf(lr_cc, 2),
                        "dagen met twee op rij": int((hits_bt[name] * hits_bt[name].shift(1)).sum()),
                        "jaren groen": (yearly_counts <= 4).sum(), "jaren geel": yearly_counts.between(5, 9).sum(),
                        "jaren rood": (yearly_counts >= 10).sum(),
                        "jaren cc verworpen": (yearly_cc > stats.chi2.ppf(0.95, 2)).sum()}
pd.DataFrame(summary_bt).T.round(3)
```

De tabel hieronder zet de kern van die uitkomst naast een juist model, dat op 1% van de
dagen wordt overschreden.

| model | overschrijdingen hier (%) | juist model (%) | rode jaren (van 36) | $\mathrm{LR}_{\mathrm{ind}}$ (kritiek 3,84) |
|---|---|---|---|---|
| statisch normaal | 3,26 | 1 | 11 | 27,3 |
| historisch 250 dagen | 1,63 | 1 | 2 | 23,9 |
| EWMA 0,94 | 1,98 | 1 | 2 | 6,0 |
| GARCH(1,1) | 2,15 | 1 | 1 | 4,2 |

**Geslaagd.** Teken en rangorde kloppen met wat we vooraf verwachtten. Het statische model
wordt
ruim drie keer zo vaak overschreden als het hoort, en het heeft 29 keer twee
overschrijdingen op
rij, waar bij zijn eigen frequentie $9211 \times 0{,}0326^2 \approx 9{,}8$ te verwachten
zijn. De
aanpassende modellen zitten dichter bij 1%, maar erboven. Over 36 jaar verwerpt
Christoffersen
alle vier, omdat de toets met 9211 dagen de kracht heeft die hij met 250 mist. Voor de
crisisjaren zetten we de overschrijdingen per jaar naast elkaar.

```{code-cell} ipython3
yearly = hits_bt.groupby(hits_bt.index.year).sum()
yearly.loc[[1997, 1998, 1999, 2000, 2002, 2007, 2008, 2009, 2011, 2020, 2022]]
```

In 1998 is alleen het statische model rood, omdat de andere zich binnen weken aanpasten.
In 2008 zijn het statische en het historische model rood, en in 2020 worden ook EWMA en
GARCH rood, terwijl het statische model met 23 overschrijdingen nog ver boven hen uitkomt.
In 2008 bouwde de volatiliteit zich namelijk over maanden op, zodat EWMA en GARCH konden
meelopen, terwijl de volatiliteit in februari 2020 sprong vanuit een van de rustigste
periodes van de steekproef. Een model dat van gisteren leert, ziet zo'n sprong niet
aankomen. De eerste figuur toont de overschrijdingen per jaar als staven, met de grenzen
van geel en rood als lijnen.

```{code-cell} ipython3
:label: cel-risk-management-jaren
:tags: [hide-input]

fig, ax = plt.subplots(figsize=(11, 4.5))
years = yearly.loc[:2025].index
width = 0.2
for i, name in enumerate(yearly):
    ax.bar(years + (i - 1.5) * width, yearly.loc[:2025, name], width=width, color=hap.plotting.COLORS[i], label=name)
ax.axhline(4.5, color="black", lw=0.8, ls="--")
ax.axhline(9.5, color="black", lw=0.8)
ax.text(years[-1] + 0.5, 4.8, "geel", fontsize=8)
ax.text(years[-1] + 0.5, 9.8, "rood", fontsize=8)
ax.set_title("Overschrijdingen van de 99%-VaR per jaar, Amerikaanse aandelenmarkt")
ax.set_xlabel("Jaar")
ax.set_ylabel("Aantal overschrijdingen (verwacht 2,5)")
ax.legend(ncol=4)
plt.show()
```

:::{figure} #cel-risk-management-jaren
:label: fig-risk-management-jaren
:width: 100%

Het statische normale model is rood in elf van de 36 jaren, vooral rond 2000, rond 2008 en in 2020 en 2022, en in de rustige jaren meestal groen, omdat zijn overschrijdingen clusteren. De aanpassende modellen zijn meestal groen of geel, maar het historische model is rood in 2008 en 2022, EWMA in 2007 en 2020 en GARCH in 2020.
:::

De tweede figuur zoomt in op 2008 en 2020, en laat zien hoe snel elke VaR-lijn de verliezen
volgt.

```{code-cell} ipython3
:label: cel-risk-management-crises
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), sharey=True)
for ax, (start_c, end_c, title) in zip(axes, [("2008-06-01", "2009-06-30", "(a) 2008–2009"),
                                              ("2019-12-01", "2020-12-31", "(b) 2020")], strict=True):
    loss_c = 100 * loss_bt.loc[start_c:end_c]
    ax.plot(loss_c.index, loss_c, color=hap.plotting.COLORS[7], lw=0.7, label="verlies")
    for i, name in enumerate(var_bt):
        ax.plot(loss_c.index, 100 * var_bt.loc[start_c:end_c, name], color=hap.plotting.COLORS[i], lw=1.2, label=name)
    ax.set_title(title)
    ax.set_xlabel("Datum")
    ax.tick_params(axis="x", rotation=30)
axes[0].set_ylabel("Dagverlies en 99%-VaR (%)")
axes[0].legend(fontsize=8)
fig.tight_layout()
plt.show()
```

:::{figure} #cel-risk-management-crises
:label: fig-risk-management-crises
:width: 100%

In 2008 liep de volatiliteit in weken op en liepen EWMA en GARCH mee, terwijl het historische
model in trappen steeg en daarna een jaar te hoog bleef. In februari 2020 stond de VaR van alle
modellen laag toen de eerste grote verliezen kwamen.
:::


### De spreads van 1998

```{admonition} Replicatie
:class: seealso

**Bron.** Het rapport van de Working Group on Financial Markets van de Amerikaanse president
over LTCM, april 1999 {cite}`PresidentsWorkingGroup1999`. Een analyse van de risicobeheersing
van het fonds staat in {cite:t}`Jorion2000`.

**Wat.** Het rapport beschrijft hoe risico- en liquiditeitspremies na de Russische devaluatie
van 17 augustus 1998 wereldwijd sterk stegen (p. 12). LTCM had juist gewed dat die spreads
zouden dalen (p. 16).

**Data hier.** Dagelijkse FRED-reeksen via `hap.data.fred(...)`. We gebruiken de Baa- en
Aaa-spread van Moody's boven de tienjaarsrente, de TED-spread en de tienjaarsrente zelf.

**Verschil met het origineel.** De posities van LTCM zijn niet publiek, dus we tonen alleen dat
het soort spreads waarop het fonds wedde, verbreedde. Swap spreads staan pas vanaf juli 2000
gratis in FRED.

**Verwachte afwijking.** Alle drie de spreads verbreden tussen half augustus en half oktober
met tientallen basispunten, veel meer dan de dagschommelingen van 1997 doen verwachten. De
tienjaarsrente daalt, omdat beleggers naar kwaliteit vluchten.
```

We meten de verbreding vanaf 14 augustus tot het extreem in de drie maanden erna, en drukken
die uit in de dagschommelingen van 1997.

```{code-cell} ipython3
spreads = pd.concat([hap_data.fred(s)[s] for s in ["BAA10Y", "AAA10Y", "TEDRATE", "DGS10"]], axis=1, sort=True)
spreads = spreads.loc["1997-01-01":"1999-12-31"].dropna()
before = spreads.loc[:"1998-08-14"].iloc[-1]
crisis = spreads.loc["1998-08-17":"1998-10-31"]
extreme = pd.concat([crisis[["BAA10Y", "AAA10Y", "TEDRATE"]].max(), crisis[["DGS10"]].min()])
extreme_date = pd.concat([crisis[["BAA10Y", "AAA10Y", "TEDRATE"]].idxmax(), crisis[["DGS10"]].idxmin()])
n_days_move = pd.Series({s: len(spreads.loc["1998-08-15":extreme_date[s]]) for s in spreads})
sd_1997 = spreads.loc["1997"].diff().std()
pd.DataFrame({"14 aug 1998 (%)": before, "extreem aug-okt (%)": extreme, "datum": extreme_date.dt.date,
              "verandering (bp)": 100 * (extreme - before),
              "SD dagverandering 1997 (bp)": 100 * sd_1997,
              "in SD's (sqrt-tijd)": (extreme - before) / (sd_1997 * np.sqrt(n_days_move))}).round(2)
```

**Geslaagd.** De bedrijfsobligatiespreads verbreedden met 84 (Aaa) en 103 basispunten
(Baa), terwijl de tienjaarsrente daalde. Een getal uit het origineel staat er niet naast,
omdat het rapport de verbreding alleen beschrijft en wij laten zien dat dit soort spreads
meebewoog. Opgeschaald met de wortel uit het aantal
handelsdagen zijn de bewegingen van de bedrijfsobligatiespreads ruim zes
standaarddeviaties van 1997. De TED-spread schommelde in 1997 al sterk en blijft onder
drie. Zes standaarddeviaties bewijzen niet dat de wereld niet normaal is, want 1997 was
rustig, maar ze laten wel zien wat een model ziet dat in een rustige periode is geschat.
De figuur toont de sprong na de lijn van 17 augustus.

```{code-cell} ipython3
:label: cel-risk-management-spreads
:tags: [hide-input]

fig, ax = plt.subplots()
window = spreads.loc["1998-01-01":"1999-06-30"]
for i, s in enumerate(["BAA10Y", "AAA10Y", "TEDRATE"]):
    ax.plot(window.index, 100 * window[s], color=hap.plotting.COLORS[i], label=s)
for date, text, align in [("1998-08-17", "Rusland ", "right"), ("1998-09-23", " LTCM-consortium", "left")]:
    ax.axvline(pd.Timestamp(date), color="black", lw=0.8, ls="--")
    ax.text(pd.Timestamp(date), 0.03, text, fontsize=8, ha=align, transform=ax.get_xaxis_transform())
ax.set_title("Credit- en liquiditeitsspreads rond de crisis van 1998")
ax.set_xlabel("Datum")
ax.set_ylabel("Spread (basispunten)")
ax.legend(loc="upper left")
plt.show()
```

:::{figure} #cel-risk-management-spreads
:label: fig-risk-management-spreads
:width: 90%

Na 17 augustus verbreedden de bedrijfsobligatiespreads en de TED-spread in weken met meer dan
tachtig basispunten. De piek viel pas in oktober, na de redding van LTCM, en begin 1999 waren
de bedrijfsobligatiespreads nog niet terug op hun niveau van juli 1998.
:::

Die beweging is groot naast de drempels uit toy-deel (c). Een fonds met hefboom 25 krijgt
zijn margin call na 40 basispunten en is failliet na 80, zodat een beweging als die van de
Aaa-spread genoeg is. Met hefboom 10 had hetzelfde fonds niet eens een margin call
gekregen. De werkelijke posities en haircuts van LTCM kennen we niet, maar het rapport
beschrijft wel de afloop (p. 12–14):

- op 31 juli had het fonds 4,1 miljard dollar kapitaal
- in augustus verloor het 1,8 miljard
- op 23 september nam een consortium van veertien instellingen, bijeengebracht door de
  Federal
  Reserve Bank of New York, voor ongeveer 3,6 miljard dollar 90% van het fonds over.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** VaR gaf risicobeheer een gemeenschappelijke taal en één getal
voor
limieten en kapitaal. Het gebruikt wat goed meetbaar is, het tweede moment, en laat weg
wat dat
niet is. In onze backtest werkt dat redelijk, want de aanpassende modellen liggen op 1,6 tot
2,2% overschrijdingen tegen 3,3% voor een statisch model. Kupiec en Christoffersen maakten
een
risicomodel weerlegbaar, en de coherentie-axioma's kwamen in 2016 in de regels.

**Waar het breekt.** Het breekt op de dagen waarover het getal niets zegt. Een 99%-VaR die
in
2020 twaalf keer wordt overschreden, is geen goed model met pech. De spreads waarop LTCM
wedde,
bewogen in twee maanden ruim zes standaarddeviaties, en volgens het rapport waren de
verliezen
veel groter dan modellen uit rustiger tijden waarschijnlijk vonden (p. 12). Het diepste
gebrek
was de aanname dat een positie tegen de marktprijs kan worden gesloten. In onze simulatie
heeft
dezelfde trade daardoor een kans op ruïne van bijna nul of bijna een op vier, afhankelijk
van
hefboom en eigen prijsdruk.

**Risico of vergissing?** De Chicago-lezing ziet in de spreads van 1997 een beloning voor
liquiditeits- en crashrisico, en in augustus 1998 de slechte toestand waarvoor die
beloning werd
betaald. LTCM droeg dan risico met een premie, alleen met te weinig kapitaal. De
Yale-lezing van
{cite:t}`ShleiferVishny1997` ziet spreads die groter werden dan hun fundamentele waarde
*omdat*
arbitrageurs moesten verkopen. De posities en verkopen van arbitrageurs zouden de lezingen
kunnen scheiden, maar die data zijn niet publiek, en één episode is geen steekproef. Wel
zegt
Santa-Clara's onderscheid tussen premie en vermeend inzicht iets over het fonds. Het
rendement
kwam uit risico met een premie, en het verlies uit het geloof dat de hefboom veilig was.

**Wat er daarna kwam.** Als arbitrageurs een mispricing niet kunnen wegwerken omdat hun
financiering verdwijnt, wordt de vraag wie de prijzen dan zet en waarom beleggers zich
vergissen. Daarover gaat [het college over gedrag en de grenzen van arbitrage](#04-23-behavioral).

## Oefeningen

:::{exercise}
:label: ex-risk-management-1

**Instap: de hefboom uit het toy-voorbeeld.** Neem toy-deel (c). Duration en haircut blijven 5
en 2%, en alleen de hefboom verandert.

1. Bereken met [](#eq-risk-management-drempel) de drempels voor margin call en ruïne bij
   hefboom 15 en 20.
2. Wat is de hoogste hefboom waarbij het fonds geen margin call krijgt bij een verbreding van
   84 basispunten, de beweging van de Aaa-spread in 1998?
:::

:::{solution} ex-risk-management-1
:class: dropdown

**(1)** Bij hefboom 20 komt de margin call na $(1 - 0{,}4)/(20 \times 5) = 0{,}006$, dus 60
basispunten, en de ruïne na $1/100$, dus 100 basispunten. Bij hefboom 15 is dat
$(1 - 0{,}3)/75 \approx 0{,}00933$, dus 93,3 basispunten, en $1/75$, dus 133,3 basispunten.

**(2)** Geen margin call betekent $(1 - hL)/(LD) \ge 0{,}0084$, dus
$1 \ge L\,(h + 0{,}0084\,D) = 0{,}062\,L$, en $L \le 16{,}1$.

```{code-cell} ipython3
def thresholds_bp(leverage, duration=D, haircut=H):
    """Spread widening in basis points at which the margin call and ruin arrive."""
    call = (1 - haircut * leverage) / (leverage * duration)
    ruin = 1 / (leverage * duration)
    return 1e4 * call, 1e4 * ruin


max_leverage = 1 / (H + 0.0084 * D)
print(f"hoogste hefboom zonder margin call bij 84 bp: {max_leverage:.1f}")
pd.DataFrame({L: thresholds_bp(L) for L in (10, 15, 20, 25)},
             index=["margin call (bp)", "ruïne (bp)"]).T.round(1)
```

Van hefboom 10 naar 20 daalt de afstand tot de margin call van 160 naar 60 basispunten, dus met
meer dan de helft. Een hogere hefboom verhoogt namelijk zowel het verlies per basispunt als het
vereiste onderpand.
:::

:::{exercise}
:label: ex-risk-management-2

**ES en VaR bij dikke staarten.** Laat $L = \sigma T_\nu\sqrt{(\nu-2)/\nu}$ met $T_\nu$
Student-$t$. Dan is $\SD(L) = \sigma$, zodat alleen de staart verandert.

1. Laat zien dat $\mathrm{ES}_\alpha(T_\nu) = \dfrac{f_\nu(t_\alpha)}{1-\alpha}\cdot\dfrac{\nu + t_\alpha^2}{\nu-1}$,
   met $f_\nu$ de dichtheid en $t_\alpha$ het $\alpha$-kwantiel van $T_\nu$.
2. Bereken voor $\nu \in \{4, 6, 10, \infty\}$ de verhouding $\mathrm{ES}_{0{,}975}/\mathrm{VaR}_{0{,}99}$.
3. Wat betekent dat voor het kapitaal onder de regels van 2016 tegenover die van 1996?
:::

:::{solution} ex-risk-management-2
:class: dropdown

**(1)** Differentieer $f_\nu(t) \propto (1+t^2/\nu)^{-(\nu+1)/2}$. Dan is
$\frac{\mathrm{d}}{\mathrm{d}t}\left[\frac{\nu+t^2}{\nu-1}f_\nu(t)\right] = -t f_\nu(t)$, dus
$\int_{t_\alpha}^\infty t f_\nu(t)\,\mathrm{d}t = \frac{\nu+t_\alpha^2}{\nu-1}f_\nu(t_\alpha)$.
Deel door $1-\alpha$.

```{code-cell} ipython3
def t_scaled(alpha, nu):
    """Standardised (unit variance) Student-t VaR and ES at level alpha."""
    if np.isinf(nu):
        z = stats.norm.ppf(alpha)
        return z, stats.norm.pdf(z) / (1 - alpha)
    q = stats.t.ppf(alpha, nu)
    es = stats.t.pdf(q, nu) / (1 - alpha) * (nu + q**2) / (nu - 1)
    scale = np.sqrt((nu - 2) / nu)
    return q * scale, es * scale


es_check = stats.t.expect(lambda x: x, args=(6,), lb=stats.t.ppf(0.975, 6)) / 0.025
print(f"controle nu = 6: formule {t_scaled(0.975, 6)[1] / np.sqrt(4 / 6):.4f}, numeriek {es_check:.4f}")
pd.DataFrame({nu: {"VaR 99%": t_scaled(0.99, nu)[0], "ES 97,5%": t_scaled(0.975, nu)[1],
                   "ES 97,5% / VaR 99%": t_scaled(0.975, nu)[1] / t_scaled(0.99, nu)[0]}
              for nu in (4, 6, 10, np.inf)}).T.round(3)
```

**(2) en (3)** De verhouding stijgt van 1,005 bij normaliteit naar 1,066 bij $\nu = 4$. Bij
gelijke volatiliteit ligt de 99%-VaR van een dikstaartige verdeling al hoger, 2,65 tegen 2,33
bij $\nu = 4$, en de ES stijgt nog iets meer. De overstap laat het kapitaal onder normaliteit
dus gelijk en maakt dikke staarten duurder, precies waar Santa-Clara de zwakte van VaR zag.
:::

:::{exercise}
:label: ex-risk-management-3

**Filtered historical simulation.** Voeg aan de backtest van 1990–2026 twee modellen toe. Het
eerste is GARCH(1,1) met gestandaardiseerde Student-$t$-schokken, geschat op 1963–1989. Het
tweede is filtered historical simulation, die de rendementen deelt door de EWMA-volatiliteit en
het 1%-kwantiel over 1000 dagen vermenigvuldigt met de EWMA-volatiliteit van morgen. Rapporteer
overschrijdingen, rode jaren en de aantallen in 1998, 2008 en 2020.
:::

:::{solution} ex-risk-management-3
:class: dropdown

```{code-cell} ipython3
garch_t = arch_model(100 * market, mean="Constant", vol="GARCH", p=1, q=1, dist="t")
garch_t_fit = garch_t.fit(last_obs="1990-01-01", disp="off")
nu_hat = garch_t_fit.params["nu"]
q01_t = stats.t.ppf(0.01, nu_hat) * np.sqrt((nu_hat - 2) / nu_hat)
fc_t = garch_t_fit.forecast(start="1990-01-01", horizon=1, reindex=False)
var_garch_t = (-(garch_t_fit.params["mu"] + q01_t * np.sqrt(fc_t.variance["h.1"])) / 100).shift(1)

ewma_sd = np.sqrt((market**2).ewm(alpha=0.06, adjust=False).mean())
standardised = market / ewma_sd.shift(1)
var_fhs = -(standardised.rolling(1000).quantile(0.01) * ewma_sd).shift(1)

extra = pd.DataFrame({"GARCH-t": var_garch_t, "FHS (EWMA)": var_fhs}).reindex(var_bt.index)
hits_extra = extra.lt(loss_bt, axis=0).astype(int)
yearly_extra = hits_extra.groupby(hits_extra.index.year).sum()
pd.DataFrame({name: {"nu": nu_hat if name == "GARCH-t" else np.nan,
                     "overschrijdingen": hits_extra[name].sum(),
                     "fractie (%)": 100 * hits_extra[name].mean(),
                     "jaren rood (t/m 2025)": (yearly_extra.loc[:2025, name] >= 10).sum(),
                     "1998": yearly_extra.loc[1998, name], "2008": yearly_extra.loc[2008, name],
                     "2020": yearly_extra.loc[2020, name]} for name in extra}).T.round(3)
```

Met $t$-schokken ($\hat\nu = 7{,}4$) daalt het aantal GARCH-overschrijdingen van 198 naar 156,
maar 2020 blijft rood. FHS komt met 1,16% het dichtst bij 1%, zonder rood jaar, omdat het de
staart uit de data haalt en het niveau uit EWMA. Ook FHS wordt in 2020 iets vaker overschreden dan verwacht, maar blijft daar groen. De meeste fouten van VaR komen dus niet uit het idee zelf, maar
uit de normale staart en de trage aanpassing.
:::
