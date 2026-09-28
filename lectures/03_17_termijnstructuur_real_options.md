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

(03-17-termijnstructuur-real-options)=

# Brennan-Schwartz, Vasicek, CIR en Longstaff-Schwartz

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1977–2001, met het zwaartepunt tussen 1977 en 1992.

**Wat we al weten.** [Black, Scholes en Merton](#02-09-black-scholes) prijsden een
optie door haar na te maken met aandeel en obligatie. Dat vraagt een onderliggende
waarde die te koop is, en een constante rente.
[Basu, Banz en Rosenberg](#03-16-vroege-anomalieen) vonden kenmerken die rendementen
voorspelden buiten het CAPM om. Die barst blijft hier even liggen.

**Welke vraag staat open.** Hoe krijgt een claim een prijs als de variabele die haar
drijft niet te koop is, zoals de korte rente, of als de claim een keuze bevat, zoals
het sluiten van een mijn?
```

## Overzicht

Hoe krijgt een obligatie een prijs als de korte rente niet te koop is? Door haar af te
dekken met andere obligaties die aan dezelfde renteschok hangen: dan bieden alle
obligaties dezelfde vergoeding per eenheid risico. Met één bron van onzekerheid bewegen
alle rentes echter samen, en in de data heeft de curve drie factoren. Hetzelfde argument
prijst ook een mijn met de keuze om te sluiten en een Amerikaanse optie. In deze lecture:

- rekenen we een obligatie in een renteboom uit;

- leiden we af dat één marktprijs van risico alle obligaties prijst, met de formules van
  Vasicek en CIR, en passen we hetzelfde argument kort toe op een mijn en op
  Amerikaanse opties;

- simuleren we hoe goed veertig jaar maanddata de rentedynamiek vastleggen;

- zetten we Vasicek en CIR, geschat op de driemaandsrente, naast de waargenomen curve,
  en repliceren we Litterman en Scheinkman {cite}`LittermanScheinkman1991` en tabel 1
  van Longstaff en Schwartz {cite}`LongstaffSchwartz2001`.

{cite:t}`Vasicek1977` liet met een arbitrageargument zien dat alle obligaties dezelfde
vergoeding per eenheid renterisico bieden, en gaf een formule voor de hele curve.
{cite:t}`CoxIngersollRoss1985` leidden een positieve rente af uit een evenwicht.
{cite:t}`BrennanSchwartz1979` voegden de lange yield als tweede factor toe, in een model
dat alleen numeriek op te lossen is. {cite:t}`LongstaffSchwartz1992` bouwden een
tweefactormodel met gesloten formules. {cite:t}`DuffieKan1996` lieten zien wat Vasicek,
CIR en Longstaff-Schwartz delen: ze zijn *affien* (de log-prijs van een obligatie is
lineair in de factoren). Op een grondstof werd dezelfde wiskunde de theorie van *real
options* (opties in een project: wachten, sluiten, opgeven)
{cite}`BrennanSchwartz1985,McDonaldSiegel1986`. De lijn eindigt bij *least-squares Monte
Carlo* (LSM: doorgaan gewaardeerd met een regressie op gesimuleerde paden). Zo werd
Black-Scholes een methode voor alles wat van een onzekere toestand afhangt. Santa-Clara
noemt dit de UCLA-lijn, naar zijn mentoren Brennan en Schwartz {cite}`SantaClara2026`.

Op de vraag theorie of feit zijn deze modellen relatieve waarderingsregels, zoals
Black-Scholes. Ze zeggen wat een obligatie waard is *gegeven* het renteproces en één
marktprijs van risico, en worden getoetst op de correlatie tussen rentes en de vorm van
de curve.

## Intuïtie: waarom zou dit waar zijn?

De korte rente is een prijs, geen activum. Vasiceks uitweg was dat alle obligaties met
dezelfde renteschok bewegen. Een handelaar die een lange obligatie koopt en een kortere
verkoopt in de juiste verhouding, heft die schok op en moet de korte rente verdienen. Dus
bieden beide obligaties hetzelfde extra rendement per eenheid risico. Die ene verhouding,
de *marktprijs van risico*, is alles wat de markt over voorkeuren hoeft te vertellen.

Trekt de rente terug naar een gemiddelde, dan hangt de vorm van de curve af van waar de
rente nu staat. Onzekerheid duwt lange yields omlaag: een verre euro wint meer bij een
rentedaling dan hij verliest bij een even grote stijging. Een beloning voor renterisico
duwt ze omhoog.

Een kopermijn is een reeks opties op koper: delven als de prijs de kosten dekt, sluiten
als dat niet zo is. Een netto contante waarde met de verwachte koperprijs rekent alsof de
mijn in verliesjaren doorwerkt, en onderschat haar. Wie vandaag investeert, geeft
bovendien de keuze op om te wachten.

Een Amerikaanse optie wordt uitgeoefend zodra dat meer oplevert dan doorgaan. Longstaff en
Schwartz schatten doorgaan met een regressie op gesimuleerde paden, en een geschatte regel
is nooit beter dan de beste.

Dat leidt tot vier verwachtingen. Lange yields liggen onder de verwachte korte rente als
alleen onzekerheid telt, en erboven als beleggers een beloning voor renterisico vragen.
Met één bron van onzekerheid bewegen alle rentes perfect samen. Een mijn met de keuze om
te sluiten is meer waard dan haar netto contante waarde, en een project start pas ruim
boven de kosten. En LSM benadert de juiste prijs van onderen.

## Toy-voorbeeld: een renteboom van drie perioden

We beginnen met de imports-cel, de enige van deze lecture.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import optimize, stats

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** De korte rente per periode heet $i_t$, want $r$ is in de reeks het netto
simpele rendement. In de renteboom, naar {cite:t}`HoLee1986`, begint $i$ op 5% en gaat
ze elke periode met risiconeutrale kans $\tfrac12$ drie procentpunt omhoog of omlaag. We
prijzen een obligatie die op $t = 3$ één euro uitkeert.

| $t = 0$ | $t = 1$ | $t = 2$ |
|---|---|---|
| 5% | 8% / 2% | 11% / 5% / $-1$% |

**Het recept.** We rekenen achterwaarts: een claim is op $t$ de verwachte waarde in de
volgende knopen waard, gedeeld door $1 + i_t$. De theorie leidt dat af als
[](#eq-termijnstructuur-real-options-prijs).

**Stap 1: de obligatie op $t = 2$.** Eén periode voor de vervaldag is ze
$1/1{,}11 = 0{,}900901$, $1/1{,}05 = 0{,}952381$ of $1/0{,}99 = 1{,}010101$ waard.

**Stap 2: de obligatie op $t = 1$.** In de hoge knoop
$\tfrac12(0{,}900901 + 0{,}952381)/1{,}08 = 0{,}858001$, in de lage
$\tfrac12(0{,}952381 + 1{,}010101)/1{,}02 = 0{,}962001$.

**Stap 3: de obligatie vandaag.** $p(0,3) = \tfrac12(0{,}858001 + 0{,}962001)/1{,}05 =
0{,}866668$. Op dezelfde manier is $p(0,2) = \tfrac12(1/1{,}08 + 1/1{,}02)/1{,}05 =
0{,}907771$.

**Stap 4: de yields.** De *yield* is het rendement per jaar tot de vervaldag,
$(1/p)^{1/\tau} - 1$ bij een looptijd van $\tau$ jaar: 5,000%, 4,957% en 4,886% op één,
twee en drie jaar. De curve daalt, terwijl de verwachte korte rente overal 5% is. Dat komt
doordat $1/(1+i)$ bol is in $i$: het *convexiteitseffect*.

De code loopt de boom achteruit door en zet de handberekening ernaast.

```{code-cell} ipython3
i_tree = [np.array([0.05]), np.array([0.08, 0.02]), np.array([0.11, 0.05, -0.01])]
q_rate = 0.5


def roll_back(values, rates):
    """Discount next-period node values one step back in a recombining rate tree."""
    return q_rate * (values[:-1] + values[1:]) / (1 + rates)


bond_t2 = 1 / (1 + i_tree[2])                      # zero paying 1 at t = 3, valued at t = 2
bond_t1 = roll_back(bond_t2, i_tree[1])
bond_t0 = roll_back(bond_t1, i_tree[0])[0]
bond2_t0 = roll_back(1 / (1 + i_tree[1]), i_tree[0])[0]   # zero paying 1 at t = 2
zero_prices = [1 / (1 + i_tree[0][0]), bond2_t0, bond_t0]
yields_toy = [(1 / p) ** (1 / n) - 1 for n, p in zip([1, 2, 3], zero_prices)]

hand = {"p op t=1, hoge knoop": 0.858001, "p op t=1, lage knoop": 0.962001,
        "p(0,2)": 0.907771, "p(0,3)": 0.866668, "yield 2 jaar (%)": 4.957,
        "yield 3 jaar (%)": 4.886}
code = {"p op t=1, hoge knoop": bond_t1[0], "p op t=1, lage knoop": bond_t1[1],
        "p(0,2)": bond2_t0, "p(0,3)": bond_t0, "yield 2 jaar (%)": round(100 * yields_toy[1], 3),
        "yield 3 jaar (%)": round(100 * yields_toy[2], 3)}
pd.DataFrame({"met de hand": hand, "code": code}).round(6)
```

De twee kolommen zijn gelijk. De lezer weet nu het mechanisme in het klein: onzekerheid
over de rente maakt een verre euro duurder dan de verwachte rente zegt, dus ligt de
driejaarsyield 0,114 procentpunt onder de verwachte korte rente. Oefening 4 rekent met
dezelfde methode een mijn met de keuze om te sluiten uit.

## Theorie

De kernlijn van deze lecture is de termijnstructuur. We leiden eerst af dat één
renteschok alle obligaties dezelfde marktprijs van risico geeft, en dat elke prijs dan aan
één partiële differentiaalvergelijking voldoet. Dan volgt de affiene oplossing, met Vasicek
en CIR, en wat die over de curve voorspellen. Dat toetsen simulatie en replicatie. Daarna
passen we hetzelfde argument kort toe op een mijn en op Amerikaanse opties (LSM).

### Opzet en notatie

Vanaf hier is $i_t$ de *instantane korte rente*: de continu samengestelde rente op een
oneindig korte lening, bijvoorbeeld 5% per jaar. Een constante rente, bij de mijn en bij
LSM, heet ook $i$. $p(t,T)$ is de prijs op $t$ van een *nulcouponobligatie* (één euro op
$T$, verder niets), $\tau = T - t$ haar looptijd en $y(t,T) = -\log p(t,T)/\tau$ haar
yield. Partiële afgeleiden schrijven we als $\partial_t p$, $\partial_i p$ en
$\partial_{ii} p$. Vasiceks $\alpha$, $\gamma$ en $q$ (geen risiconeutrale kans) heten hier
$\kappa$, $\theta$ en $\lambda$. De aannames:

1. de korte rente is de enige toestandsvariabele, en volgt onder de werkelijke kansen
   $\mathrm{d}i_t = \mu(i_t)\,\mathrm{d}t + \sigma(i_t)\,\mathrm{d}W_t$;

2. obligaties van elke looptijd worden continu verhandeld, zonder transactiekosten, en
   short gaan mag;

3. er is geen arbitrage.

### Obligatieprijzen als risiconeutrale verwachting

*Waarom zou dit waar zijn?* Een belegger die zijn geld elke dag tegen de korte rente
uitzet, weet vooraf niet wat hij over tien jaar heeft. Een obligatie belooft een vast
bedrag. Onder risiconeutrale kansen leveren beide gemiddeld hetzelfde op, dus kost de
obligatie de verwachte discontering van één euro. Omdat discontering bol is in de rente,
maakt onzekerheid de obligatie duurder dan bij een vaste rente.

Volgens de fundamentele stelling, [](#eq-apt-no-arbitrage-martingaal), is elke
arbitragevrije prijs een verdisconteerde verwachting onder een martingaalmaat. Met een
payoff van één euro en continue discontering wordt dat

```{math}
:label: eq-termijnstructuur-real-options-prijs
p(t,T) = \E^{\mathbb{Q}}_t\!\left[\exp\!\Big(-\int_t^T i_s\,\mathrm{d}s\Big)\right]
       = \E_t\!\left[\frac{m_T}{m_t}\right].
```

In woorden: de obligatie kost de risiconeutrale verwachting van de disconteringsfactor
over haar looptijd, met $\mathbb{Q}$ de risiconeutrale maat uit
[](#02-09-black-scholes). Met de stochastische discontofactor (SDF) $m$ (het gewicht van een
euro in elke toekomstige toestand) is dat de verwachte $m_T/m_t$. De renteboom was deze
formule in drie stappen.

Omdat $e^{-x}$ bol is, geldt $\E^{\mathbb{Q}}[e^{-X}] > e^{-\E^{\mathbb{Q}}[X]}$ (Jensens
ongelijkheid): onzekerheid verhoogt de prijs en verlaagt de yield. In de boom was dat
$5{,}000\% - 4{,}886\% = 0{,}114$ procentpunt op drie jaar. Een termijnstructuurmodel is
een keuze voor het proces van $i$ onder $\mathbb{Q}$.

### Het kernresultaat: één marktprijs van risico

*Waarom zou dit waar zijn?* Een handelaar koopt een tienjaarsobligatie en verkoopt een
tweejaarsobligatie. Stijgt de rente, dan verliest hij op de eerste en wint hij op de
tweede. In de juiste verhouding heffen die elkaar op. De positie is zonder risico en moet
de korte rente opleveren. Biedt de tienjaarsobligatie per eenheid risico meer, dan koopt
iedereen haar, en stijgt haar prijs tot het verschil weg is.

Itô's lemma uit [](#thm-black-scholes-ito), de kettingregel plus kromming maal variantie,
geeft voor $p = p(i,t;T)$

$$
\frac{\mathrm{d}p}{p} = \mu_p\,\mathrm{d}t - \sigma_p\,\mathrm{d}W,
\qquad
\mu_p = \frac{\partial_t p + \mu\,\partial_i p + \tfrac12\sigma^2\,\partial_{ii} p}{p},
\qquad
\sigma_p = -\frac{\sigma\,\partial_i p}{p} .
$$

In woorden: $\mu_p$ is het verwachte rendement van de obligatie en $\sigma_p$ haar
volatiliteit. Een obligatie daalt als de rente stijgt ($\partial_i p < 0$), dus
$\sigma_p$ is positief.

:::{prf:theorem} Eén marktprijs van renterisico
:label: thm-termijnstructuur-real-options-lambda

Onder aannames 1 tot en met 3 bestaat er een functie $\lambda(i,t)$, onafhankelijk van de
looptijd $T$, zodat voor elke obligatie

```{math}
:label: eq-termijnstructuur-real-options-lambda
\frac{\mu_p(t,T) - i}{\sigma_p(t,T)} = \lambda(i,t).
```
:::

In woorden: het extra rendement per eenheid volatiliteit is voor elke looptijd hetzelfde.
Het bewijs is de positie van de handelaar.

:::{prf:proof}
:class: dropdown

Neem twee looptijden $T_1 \neq T_2$ en houd $w$ euro in obligatie 1 en $1-w$ in
obligatie 2 (aanname 2). De positie verandert met
$\big(w\mu_{p,1} + (1-w)\mu_{p,2}\big)\mathrm{d}t - \big(w\sigma_{p,1} +
(1-w)\sigma_{p,2}\big)\mathrm{d}W$. Met $w = \sigma_{p,2}/(\sigma_{p,2} -
\sigma_{p,1})$ verdwijnt de enige schok (aanname 1), en moet de positie $i$ verdienen
(aanname 3): $w\mu_{p,1} + (1-w)\mu_{p,2} = i$. Invullen van $w$ geeft
$(\mu_{p,1} - i)/\sigma_{p,1} = (\mu_{p,2} - i)/\sigma_{p,2}$. Omdat $T_1$ en $T_2$
willekeurig waren, hangt deze verhouding niet van de looptijd af. $\square$
:::

Invullen van $\mu_p$ en $\sigma_p$ in $\mu_p - i = \lambda\sigma_p$ geeft de
*termijnstructuur-PDE*:

```{math}
:label: eq-termijnstructuur-real-options-pde
\partial_t p + \big(\mu(i) + \lambda\,\sigma(i)\big)\,\partial_i p
+ \tfrac12 \sigma(i)^2\,\partial_{ii} p - i\,p = 0,
\qquad p(i,T;T) = 1 .
```

In woorden: tijdsverval, drift en kromming maal variantie leveren samen de korte rente
op. In [](#eq-black-scholes-pde) verdween de drift, omdat het aandeel zelf in de hedge
zat. De rente is geen activum, dus hier blijft de *risiconeutrale drift*
$\mu + \lambda\sigma$ staan. Volgens Feynman-Kac ([](#thm-black-scholes-feynman-kac)) is
de oplossing een verdisconteerde verwachting: [](#eq-termijnstructuur-real-options-prijs).

Het verwachte extra rendement van een obligatie is $\lambda\sigma_p$. Een positieve
$\lambda$ geeft een *term premium* (het verwachte extra rendement van een lange obligatie
boven een reeks korte): bij $\lambda = 0{,}3$ en 5% volatiliteit $0{,}3 \cdot 5\% =
1{,}5$ procentpunt per jaar. Zoals de intuïtie voorspelde, vertelt één getal alles over
voorkeuren. Vasicek nam $\lambda$ constant.

### De affiene klasse: Duffie en Kan

*Waarom zou dit waar zijn?* Een belegger houdt een obligatie terwijl de rente één
procentpunt stijgt. Stijgen drift en variantie van de rente onder $\mathbb{Q}$ lineair met
de rente, dan verliest hij daarbij op elk renteniveau hetzelfde percentage. De log-prijs
daalt dan lineair in de rente.

:::{prf:theorem} Affiene termijnstructuur
:label: thm-termijnstructuur-real-options-affien

Stel dat de korte rente onder $\mathbb{Q}$ voldoet aan

$$
\mathrm{d}i_t = (a_0 + a_1 i_t)\,\mathrm{d}t + \sqrt{b_0 + b_1 i_t}\;\mathrm{d}W^{\mathbb{Q}}_t .
$$

Dan is $p(t,T) = \exp\!\big(A(\tau) - B(\tau)\, i_t\big)$, met

```{math}
:label: eq-termijnstructuur-real-options-riccati
B'(\tau) = 1 + a_1 B(\tau) - \tfrac12 b_1 B(\tau)^2,
\qquad
A'(\tau) = -a_0 B(\tau) + \tfrac12 b_0 B(\tau)^2,
\qquad A(0) = B(0) = 0 .
```
:::

In woorden: $B(\tau)$ is de gevoeligheid van de log-prijs voor de korte rente, een soort
duration, en $A(\tau)$ vangt het verwachte pad van de rente en het convexiteitseffect. De
yield $y = (B i_t - A)/\tau$ is dus affien (lineair plus een constante) in $i_t$. De
vergelijking voor $B$ is een Riccati-vergelijking (met een kwadratische term), die voor
$A$ daarna een integraal.

:::{prf:proof}
:class: dropdown

Probeer $p = \exp(A(\tau) - B(\tau) i)$. Omdat $\tau = T - t$, is
$\partial_t p = (-A' + B' i)p$, en verder $\partial_i p = -Bp$ en
$\partial_{ii} p = B^2 p$. Invullen in [](#eq-termijnstructuur-real-options-pde), met
risiconeutrale drift $a_0 + a_1 i$ en variantie $b_0 + b_1 i$, en delen door $p$ geeft

$$
-A' + B'i - (a_0 + a_1 i) B + \tfrac12 (b_0 + b_1 i) B^2 - i = 0
\quad\text{voor alle } i .
$$

Een functie $c_0 + c_1 i$ is alleen overal nul als $c_0 = c_1 = 0$. De coëfficiënt van
$i$ geeft de vergelijking voor $B'$, de constante die voor $A'$. De eindvoorwaarde
$p(i,T;T) = 1$ voor alle $i$ geeft $A(0) = B(0) = 0$. $\square$
:::

{cite:t}`DuffieKan1996` bewezen dit voor een vector factoren $\mathbf{x}_t$, bijvoorbeeld
de korte rente en haar volatiliteit: dan is $\log p = A(\tau) -
\mathbf{b}(\tau)'\mathbf{x}_t$. Vasicek, CIR en Longstaff-Schwartz zijn speciale gevallen.
Eén factor heeft een scherpe consequentie.

:::{prf:corollary} Eén factor, perfect gecorreleerde yields
:label: cor-termijnstructuur-real-options-correlatie

In elk eenfactormodel met $y(t,T) = (B(\tau)i_t - A(\tau))/\tau$ is
$\mathrm{d}y = (B(\tau)/\tau)\,\mathrm{d}i + (\ldots)\,\mathrm{d}t$. Yieldveranderingen
van alle looptijden zijn dus lokaal perfect gecorreleerd, en een
principale-componentenanalyse op yieldveranderingen vindt één component.
:::

In woorden: elke yield beweegt met een vast veelvoud van dezelfde schok, zoals de
intuïtie voorspelde. Dit toetst de replicatie.

### Vasicek: een terugtrekkende rente met normale schokken

*Waarom zou dit waar zijn?* De eenvoudigste terugtrekkende rente is een veer met
schokken van vaste grootte: staat de rente boven haar gemiddelde, dan trekt de drift haar
omlaag. Met normale schokken is ook de som van de rentes over de looptijd normaal, en voor
een normale $X$ is $\E[e^{-X}]$ bekend.

Vasicek nam $\mathrm{d}i = \kappa(\theta - i)\,\mathrm{d}t + \sigma\,\mathrm{d}W$ en een
constante $\lambda$. Hier is $\kappa$ de snelheid van terugtrekken, bijvoorbeeld 0,15 per
jaar (halfwaardetijd $\log 2/0{,}15 = 4{,}6$ jaar), $\theta$ het gemiddelde, bijvoorbeeld
5%, en $\sigma$ de volatiliteit, bijvoorbeeld 1,5% per jaar. Onder $\mathbb{Q}$ is de
drift $\kappa(\theta^{*} - i)$, met $\theta^{*} = \theta + \lambda\sigma/\kappa$. In
[](#thm-termijnstructuur-real-options-affien) is dus $a_0 = \kappa\theta^{*}$,
$a_1 = -\kappa$, $b_0 = \sigma^2$ en $b_1 = 0$.

:::{prf:proposition} Vasicek-obligatieprijs
:label: thm-termijnstructuur-real-options-vasicek

```{math}
:label: eq-termijnstructuur-real-options-vasicek
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa},
\qquad
A(\tau) = \Big(\theta^{*} - \frac{\sigma^2}{2\kappa^2}\Big)\big(B(\tau) - \tau\big)
          - \frac{\sigma^2 B(\tau)^2}{4\kappa},
```

en de yield van een oneindig lange obligatie is
$y_\infty = \theta^{*} - \sigma^2/(2\kappa^2)$, onafhankelijk van $i_t$.
:::

:::{prf:proof}
:class: dropdown

$B' = 1 - \kappa B$ met $B(0) = 0$ geeft $B = (1 - e^{-\kappa\tau})/\kappa$. Dan is
$\int_0^\tau B = (\tau - B)/\kappa$. Uitschrijven van het kwadraat geeft
$\int_0^\tau B^2 = \kappa^{-2}\int_0^\tau (1 - 2e^{-\kappa s} + e^{-2\kappa s})\,\mathrm{d}s
= \kappa^{-2}\big(\tau - 2B + (1 - e^{-2\kappa\tau})/(2\kappa)\big)$. Met
$(1 - e^{-2\kappa\tau})/(2\kappa) = B(1 + e^{-\kappa\tau})/2 = B - \kappa B^2/2$ volgt

$$
\int_0^\tau B^2 = \frac{1}{\kappa^2}\Big(\tau - 2B + B - \frac{\kappa B^2}{2}\Big)
                = \frac{\tau - B}{\kappa^2} - \frac{B^2}{2\kappa} .
$$

Integreren van $A' = -\kappa\theta^{*}B + \tfrac12\sigma^2 B^2$ geeft
$A = \theta^{*}(B - \tau) + \tfrac{\sigma^2}{2\kappa^2}(\tau - B) - \tfrac{\sigma^2 B^2}{4\kappa}$,
wat [](#eq-termijnstructuur-real-options-vasicek) is. Voor $\tau \to \infty$ gaat
$B \to 1/\kappa$, dus $B i/\tau \to 0$ en $-A/\tau \to \theta^{*} - \sigma^2/(2\kappa^2)$.
$\square$
:::

In woorden: de lange yield is het gemiddelde $\theta$, plus de term premium
$\lambda\sigma/\kappa$, min het convexiteitseffect $\sigma^2/(2\kappa^2)$. Met de getallen
hierboven en $\lambda = 0{,}3$ is dat $5\% + 3\% - 0{,}5\% = 7{,}5\%$. Zoals de intuïtie
voorspelde, ligt de lange yield zonder beloning ($\lambda = 0$) onder $\theta$, en met
beloning erboven. Stijgt $\sigma$, dan stijgt
de premie lineair en het convexiteitseffect kwadratisch. Stijgt $\kappa$, dan krimpen
beide, omdat verre rentes minder onzeker zijn. Op de korte rente reageert de lange yield
niet.

De rente is stationair normaal verdeeld, met standaarddeviatie $\sigma/\sqrt{2\kappa}$,
hier 2,7%, en kan dus negatief worden. In 1977 was dat een schoonheidsfout, na 2014, met
negatieve rentes op Duitse en Zwitserse staatsobligaties, een eigenschap.

### Cox, Ingersoll en Ross: de vierkantswortel

*Waarom zou dit waar zijn?* Is de variantie evenredig met de rente, dan is de schok bij
$i = 0$ nul, terwijl de drift $\kappa\theta$ de rente omhoog duwt. De rente kan dus niet
onder nul.

{cite:t}`CoxIngersollRoss1985` namen
$\mathrm{d}i = \kappa(\theta - i)\,\mathrm{d}t + \sigma\sqrt{i}\,\mathrm{d}W$. De rente
raakt nul nooit als $2\kappa\theta \ge \sigma^2$, de *Feller-voorwaarde*. Het model valt
in [](#thm-termijnstructuur-real-options-affien) met $b_0 = 0$ en $b_1 = \sigma^2$. Met
een marktprijs van risico $\lambda\sqrt{i}$ is de risiconeutrale drift
$\kappa\theta - \kappa^{*}i$, met $\kappa^{*} = \kappa - \lambda\sigma$, en

```{math}
:label: eq-termijnstructuur-real-options-cir
B(\tau) = \frac{2(e^{h\tau} - 1)}{(h + \kappa^{*})(e^{h\tau} - 1) + 2h},
\quad
e^{A(\tau)} = \left[\frac{2h\, e^{(\kappa^{*} + h)\tau/2}}
                     {(h + \kappa^{*})(e^{h\tau} - 1) + 2h}\right]^{2\kappa\theta/\sigma^2},
\quad
h = \sqrt{\kappa^{*2} + 2\sigma^2}.
```

In woorden: dezelfde vorm als Vasicek, maar $B$ hangt ook van de volatiliteit af, via
de hulpgrootheid $h$ (0,16 bij de simulatiegetallen hieronder), die bepaalt hoe snel $B$
naar zijn limiet $2/(h + \kappa^{*})$ loopt. De oneindig lange yield is
$2\kappa\theta/(h + \kappa^{*})$. Bij $\kappa^{*} < \kappa$ ligt het risiconeutrale
gemiddelde $\kappa\theta/\kappa^{*}$ boven $\theta$: een positieve term premium. Bij
$\kappa^{*} > \kappa$ ligt het eronder, en is de premie negatief.

De code implementeert de yields van beide modellen.

```{code-cell} ipython3
def vasicek_yield(i_now, tau, kappa, theta, sigma, lam):
    """Continuously compounded Vasicek zero yield; lam > 0 means a positive term premium."""
    theta_q = theta + lam * sigma / kappa
    B = (1 - np.exp(-kappa * tau)) / kappa
    A = (theta_q - sigma**2 / (2 * kappa**2)) * (B - tau) - sigma**2 * B**2 / (4 * kappa)
    return (B * i_now - A) / tau


def cir_yield(i_now, tau, kappa, theta, sigma, kappa_q):
    """Continuously compounded CIR zero yield with risk-neutral mean reversion kappa_q."""
    h = np.sqrt(kappa_q**2 + 2 * sigma**2)
    denom = (h + kappa_q) * (np.exp(h * tau) - 1) + 2 * h
    B = 2 * (np.exp(h * tau) - 1) / denom
    A = (2 * kappa * theta / sigma**2) * np.log(2 * h * np.exp((kappa_q + h) * tau / 2) / denom)
    return (B * i_now - A) / tau
```

Beide functies werken ook op arrays van looptijden en rentes.

### Wat het voorspelt: paden en curves

Vasicek laat de rente onder nul zakken en CIR niet, en in beide lopen alle curves naar
dezelfde lange yield. Dat laat een exacte simulatie zien. We nemen $\kappa = 0{,}15$ en
$\theta = 5\%$, de startrente van de boom, en $\lambda = 0{,}3$. Vasicek krijgt $\sigma = 1{,}5\%$, CIR dezelfde volatiliteit bij $i = \theta$. We
simuleren 5000 paden van dertig jaar vanaf 2%.

```{code-cell} ipython3
vas = dict(kappa=0.15, theta=0.05, sigma=0.015, lam=0.3)    # parameters from the theory
sigma_cir = vas["sigma"] / np.sqrt(vas["theta"])              # same volatility at i = theta


def simulate_vasicek(i0, kappa, theta, sigma, dt, n_steps, n_paths, rng):
    """Exact simulation of an Ornstein-Uhlenbeck short rate."""
    a = np.exp(-kappa * dt)
    sd = sigma * np.sqrt((1 - a**2) / (2 * kappa))
    rate = np.empty((n_paths, n_steps + 1))
    rate[:, 0] = i0
    for t in range(n_steps):
        rate[:, t + 1] = theta + a * (rate[:, t] - theta) + sd * rng.standard_normal(n_paths)
    return rate


def simulate_cir(i0, kappa, theta, sigma, dt, n_steps, n_paths, rng):
    """Exact simulation of a CIR short rate via the noncentral chi-square transition."""
    c = sigma**2 * (1 - np.exp(-kappa * dt)) / (4 * kappa)
    df = 4 * kappa * theta / sigma**2
    rate = np.empty((n_paths, n_steps + 1))
    rate[:, 0] = i0
    for t in range(n_steps):
        rate[:, t + 1] = c * rng.noncentral_chisquare(df, rate[:, t] * np.exp(-kappa * dt) / c)
    return rate
```

De tweede cel simuleert en vat de paden samen, met $\kappa^{*} = \kappa - \lambda\sigma$
voor CIR.

```{code-cell} ipython3
dt_m, years = 1 / 12, 30
paths_vas = simulate_vasicek(0.02, vas["kappa"], vas["theta"], vas["sigma"], dt_m, 12 * years, 5000, rng)
paths_cir = simulate_cir(0.02, vas["kappa"], vas["theta"], sigma_cir, dt_m, 12 * years, 5000, rng)
kappa_q_cir = vas["kappa"] - vas["lam"] * sigma_cir
h_cir = np.sqrt(kappa_q_cir**2 + 2 * sigma_cir**2)
term_premium = vas["lam"] * vas["sigma"] / vas["kappa"]
convexity = vas["sigma"]**2 / (2 * vas["kappa"]**2)
long_yield = {"Vasicek": vas["theta"] + term_premium - convexity,
              "CIR": 2 * vas["kappa"] * vas["theta"] / (h_cir + kappa_q_cir)}

pd.DataFrame(
    {
        name: [np.mean(paths.min(axis=1) < 0), np.mean(paths < 0), paths.min(), long_yield[name]]
        for name, paths in [("Vasicek", paths_vas), ("CIR", paths_cir)]
    },
    index=["fractie paden ooit negatief", "fractie maanden negatief", "laagste rente",
           "oneindig lange yield"],
).round(4)
```

Van de Vasicek-paden zakt 58% minstens één maand onder nul, 4,7% van alle maanden is
negatief, en de laagste rente is $-6{,}7\%$. Geen CIR-pad komt onder nul. De oneindig
lange yield is 7,5% bij Vasicek en 5,2% bij CIR, vooral omdat de prijs van risico bij CIR
$\lambda\sqrt{i}$ is: bij 5% maar $0{,}3 \cdot 0{,}22 = 0{,}067$.

Let in de figuur rechts op waar de curves van één model heen lopen.

```{code-cell} ipython3
:label: cel-termijnstructuur-real-options-paden
:tags: [hide-input]

tau_grid = np.linspace(0.25, 30, 120)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
months = np.arange(paths_vas.shape[1]) / 12
for k in range(15):
    axes[0].plot(months, 100 * paths_vas[k], color=hap.plotting.COLORS[0], lw=0.7, alpha=0.7)
    axes[0].plot(months, 100 * paths_cir[k], color=hap.plotting.COLORS[1], lw=0.7, alpha=0.7)
axes[0].axhline(0, color="black", lw=0.8)
axes[0].plot([], [], color=hap.plotting.COLORS[0], label="Vasicek")
axes[0].plot([], [], color=hap.plotting.COLORS[1], label="CIR")
axes[0].set_title("Vijftien paden van de korte rente, start op 2%")
axes[0].set_xlabel("Jaren")
axes[0].set_ylabel("Korte rente (%)")
axes[0].legend()

for i0, ls in [(0.01, "-"), (0.05, "--"), (0.09, ":")]:
    axes[1].plot(tau_grid, 100 * vasicek_yield(i0, tau_grid, vas["kappa"], vas["theta"], vas["sigma"], vas["lam"]),
                 color=hap.plotting.COLORS[0], ls=ls, label=f"Vasicek, i = {i0:.0%}")
    axes[1].plot(tau_grid, 100 * cir_yield(i0, tau_grid, vas["kappa"], vas["theta"], sigma_cir, kappa_q_cir),
                 color=hap.plotting.COLORS[1], ls=ls, label=f"CIR, i = {i0:.0%}")
axes[1].set_title("Modelcurves bij drie korte rentes")
axes[1].set_xlabel("Looptijd (jaren)")
axes[1].set_ylabel("Yield (%)")
axes[1].legend(ncol=2)
plt.show()
```

:::{figure} #cel-termijnstructuur-real-options-paden
:label: fig-termijnstructuur-real-options-paden
:width: 100%

Links: Vasicek-paden zakken onder nul, CIR-paden niet. Rechts: de korte rente bepaalt de
vorm, maar alle curves van één model lopen naar dezelfde lange yield.
:::

### Hetzelfde argument voor een mijn: real options

*Waarom zou dit waar zijn?* Een mijneigenaar die termijncontracten op koper verkoopt, dekt
zijn koperrisico af. De afgedekte mijn verdient dan de rente, zoals bij Black en Scholes.
Wie koper in voorraad heeft, geniet wel de *convenience yield* (het voordeel van het fysiek
bezitten van de grondstof), en die verlaagt de risiconeutrale groei van de koperprijs,
zoals een dividend.

Laat $\mathrm{d}S = \mu S\,\mathrm{d}t + \sigma S\,\mathrm{d}W$, met $\delta$ de
convenience yield, bijvoorbeeld 1% per jaar. Brennan en Schwartz noemen haar $\kappa$,
maar die letter is hier de snelheid van terugtrekken. Onder $\mathbb{Q}$ groeit de
koperprijs met $i - \delta$. Een open mijn produceert $n$ pond per jaar tegen kosten $a$
per pond (niet de $a_0$ en $a_1$ van de affiene stelling). Zonder vaste kosten,
belastingen en uitputting voldoet haar waarde $V(S,t)$ aan

```{math}
:label: eq-termijnstructuur-real-options-mijn
\tfrac12\sigma^2 S^2\,\partial_{SS} V + (i - \delta) S\,\partial_S V + \partial_t V - iV
+ n(S - a) = 0 .
```

In woorden: dit is de PDE van Black en Scholes met groei $i - \delta$ en een dividend
$n(S - a)$ per jaar. Een gesloten mijn mist dat dividend. Waar de eigenaar opent of
sluit, verschillen de waarden van open en gesloten mijn de wisselkosten (*value
matching*) en zijn ze even steil (*smooth pasting*). Zoals de intuïtie voorspelde, is de
mijn meer waard dan haar netto contante waarde: in de koperboom van oefening 4 bijna
twee keer zoveel.

::::{note} De getallen van Brennan en Schwartz, en de drempel van McDonald en Siegel
:class: dropdown

{cite:t}`BrennanSchwartz1985` losten het volledige model numeriek op (hun tabellen 1
en 2):

| grootheid | Brennan en Schwartz |
|---|---|
| voorraad, productie, variabele kosten | 15 jaar, 10 miljoen pond per jaar, 50 dollarcent per pond |
| convenience yield, variantie koperprijs, rente | 1%, 8%, 10% per jaar |
| openen / sluiten / opgeven bij een koperprijs van | 76 / 44 / 20 dollarcent |
| waarde van de keuze om te sluiten, bij 50 cent | 0,89 miljoen dollar, 12% van een mijn die altijd produceert |

Wie vandaag investeert, geeft de keuze op om later, met meer informatie, te beslissen.
Voor een project met waarde $V$ (een nieuwe $V$, niet de mijnwaarde) die onder
$\mathbb{Q}$ met $i - \delta$ groeit en volatiliteit $\sigma$ heeft, en onomkeerbare
kosten $I$, vonden {cite:t}`McDonaldSiegel1986` de drempel

:::{prf:proposition} De drempel van McDonald en Siegel
:label: thm-termijnstructuur-real-options-wachten

Het is optimaal te investeren zodra $V \ge V^{*}$, met

```{math}
:label: eq-termijnstructuur-real-options-drempel
V^{*} = \frac{\eta}{\eta - 1}\, I,
\qquad
\eta = \frac12 - \frac{i - \delta}{\sigma^2}
       + \sqrt{\Big(\frac{i - \delta}{\sigma^2} - \frac12\Big)^2 + \frac{2i}{\sigma^2}} > 1 .
```
:::

Het bewijs: de optie om te investeren is $F = cV^{\eta}$, met $\eta$ de positieve wortel
van $\tfrac12\sigma^2\eta(\eta - 1) + (i - \delta)\eta - i = 0$. Value matching
($cV^{*\eta} = V^{*} - I$) en smooth pasting ($c\eta V^{*\eta - 1} = 1$) geven samen
$V^{*} = \eta I/(\eta - 1)$. $\eta$ is de elasticiteit van de optiewaarde naar $V$. Bij
$i = \delta = 4\%$ en $\sigma = 20\%$ is $\eta = \tfrac12 + \sqrt{\tfrac14 + 2} = 2$, dus
$V^{*} = 2I$, waar de netto contante waarde $V^{*} = I$ zegt. Meer onzekerheid verhoogt
de drempel, een hogere $\delta$ verlaagt haar.
::::

### Hetzelfde argument voor een Amerikaanse optie: LSM

*Waarom zou dit waar zijn?* De houder van een Amerikaanse put beslist op elk moment:
uitoefenen of doorgaan. Doorgaan is de verwachte waarde van zijn latere kasstromen, en een
regressie op gesimuleerde paden schat die verwachting. Voorspelt de regressie slecht, dan
oefent hij soms verkeerd uit, en daalt de waarde.

Laat de put met uitoefenprijs $K$ uitoefenbaar zijn op $J$ momenten
$t_1 < \dots < t_J = T$. Doorgaan is op $t_k$ waard (vergelijking 1 van het artikel):

```{math}
:label: eq-termijnstructuur-real-options-doorgaan
G(t_k) = \E^{\mathbb{Q}}\!\left[\sum_{j > k} e^{-i(t_j - t_k)}\, x(t_j)\,\middle|\,\mathcal{F}_{t_k}\right],
```

met $x(t_j)$ de kasstroom op $t_j$ onder de optimale strategie en $\mathcal{F}_{t_k}$ de
informatie op $t_k$. LSM schat $G$ op $t_{J-1}$, dan $t_{J-2}$, enzovoort, met een
regressie van de verdisconteerde latere kasstroom op basisfuncties van $S$. Alleen paden
in het geld gaan de regressie in, en een pad wordt uitgeoefend waar $K - S$ de geschatte
$G$ overtreft.

:::{prf:proposition} LSM is een ondergrens
:label: thm-termijnstructuur-real-options-ondergrens

Voor elke eindige keuze van basisfuncties en uitoefenmomenten en elke vaste verzameling
regressiecoëfficiënten is de gemiddelde LSM-waarde over $N \to \infty$ paden hoogstens de
waarde van de Amerikaanse optie.
:::

:::{prf:proof}
De LSM-regel is een stoptijd: hij beslist op $t_k$ met de informatie van $t_k$. De
Amerikaanse optiewaarde is het supremum over alle stoptijden van de verwachte
verdisconteerde opbrengst. Met vaste coëfficiënten convergeert het gemiddelde naar de
verwachte opbrengst van deze ene stoptijd, en die is hoogstens het supremum. $\square$
:::

In woorden: LSM benadert de optiewaarde met veel paden van onderen, zoals de intuïtie
voorspelde (Proposition 1 van {cite:t}`LongstaffSchwartz2001`). De replicatie toetst dat
met één tabel.

```{admonition} Samengevat
:class: tip

- Drijft één renteschok alle obligaties, dan bieden ze dezelfde marktprijs van risico,
  [](#eq-termijnstructuur-real-options-lambda), en lost elke prijs
  [](#eq-termijnstructuur-real-options-pde) op.

- In de affiene klasse is de log-prijs lineair in de rente,
  [](#eq-termijnstructuur-real-options-riccati). Bij Vasicek is de lange yield 7,5%,
  [](#eq-termijnstructuur-real-options-vasicek). Eén factor geeft perfect gecorreleerde
  yields.

- Hetzelfde argument prijst een mijn, [](#eq-termijnstructuur-real-options-mijn), en
  een Amerikaanse optie met LSM, dat een ondergrens geeft.

- De simulatie hierna vraagt: hoe goed leggen veertig jaar maanddata $\kappa$, $\theta$
  en $\sigma$ vast, en daarmee de lange yield?
```

## Simulatie: hoe goed is de rentedynamiek te schatten?

Veertig jaar maanddata leggen de volatiliteit van de rente tot op enkele procenten vast,
maar de snelheid van terugtrekken niet eens tot op een factor twee. Hoe goed kan de
replicatie dus schatten, als het model klopt?

Per maand is de Vasicek-rente een *AR(1)-proces*: de rente van volgende maand is een
constante plus $b$ maal de rente van nu, plus een normale schok, met
$b = e^{-\kappa/12} = 0{,}9876$ bij $\kappa = 0{,}15$. Omdat die schok normaal is en voor
elke maand even groot, is kleinste kwadraten exacte maximum likelihood. We trekken 2000 steekproeven van 40 jaar uit het model van de theorie
en schatten elke steekproef.

```{code-cell} ipython3
def fit_vasicek(rate, dt):
    """Exact-discretisation (AR(1) OLS) Vasicek estimates; works on the last axis."""
    x, y = rate[..., :-1], rate[..., 1:]
    xm, ym = x.mean(-1, keepdims=True), y.mean(-1, keepdims=True)
    b = ((x - xm) * (y - ym)).sum(-1) / ((x - xm) ** 2).sum(-1)
    c = ym[..., 0] - b * xm[..., 0]
    resid_sd = (y - c[..., None] - b[..., None] * x).std(-1)
    kappa = -np.log(b) / dt
    return kappa, c / (1 - b), resid_sd * np.sqrt(2 * kappa / (1 - b**2))


samples = simulate_vasicek(vas["theta"], vas["kappa"], vas["theta"], vas["sigma"], dt_m, 480, 2000, rng)
k_hat, th_hat, s_hat = fit_vasicek(samples, dt_m)
yinf_hat = th_hat + vas["lam"] * s_hat / k_hat - s_hat**2 / (2 * k_hat**2)
yinf_true = long_yield["Vasicek"]

estimates_sim = np.array([k_hat, th_hat, s_hat, yinf_hat])
pd.DataFrame(
    {
        "waar": [vas["kappa"], vas["theta"], vas["sigma"], yinf_true],
        "5%-kwantiel": np.percentile(estimates_sim, 5, axis=1),
        "mediaan": np.percentile(estimates_sim, 50, axis=1),
        "95%-kwantiel": np.percentile(estimates_sim, 95, axis=1),
    },
    index=["kappa", "theta", "sigma", "lange yield"],
).round(4)
```

Het 90%-interval van $\hat\kappa$ loopt van 0,10 tot 0,54, bijna drie keer de ware 0,15
breed. Dat van $\hat\sigma$ loopt van 1,43% tot 1,59%, een tiende van de ware 1,5%. De
lange yield erft de onzekerheid van de drift: van 4,2% tot 9,8% rond een ware 7,5%.

Let in de figuur links op de breedte en de lange rechterstaart, rechts op hoe smal de
verdeling is.

```{code-cell} ipython3
:label: cel-termijnstructuur-real-options-schatting
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].hist(k_hat, bins=60, range=(0, 1), color=hap.plotting.COLORS[0], edgecolor="white")
axes[0].axvline(vas["kappa"], color="black", lw=1.2, label="ware waarde")
axes[0].axvline(np.median(k_hat), color=hap.plotting.COLORS[1], ls="--", lw=1.2, label="mediaan schatting")
axes[0].set_title("Snelheid van terugtrekken $\\hat\\kappa$, 40 jaar maanddata")
axes[0].set_xlabel("$\\hat\\kappa$ (per jaar)")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].legend()
axes[1].hist(100 * s_hat, bins=60, color=hap.plotting.COLORS[2], edgecolor="white")
axes[1].axvline(100 * vas["sigma"], color="black", lw=1.2, label="ware waarde")
axes[1].set_title("Volatiliteit $\\hat\\sigma$, dezelfde steekproeven")
axes[1].set_xlabel("$\\hat\\sigma$ (% per jaar)")
axes[1].set_ylabel("Aantal steekproeven")
axes[1].legend()
plt.show()
```

:::{figure} #cel-termijnstructuur-real-options-schatting
:label: fig-termijnstructuur-real-options-schatting
:width: 100%

Links een brede, scheve verdeling rond een te hoge mediaan, rechts een smalle rond de
ware waarde.
:::

Hier komt de standaardfout van 2% uit [Rendementen en hun statistiek](#00-01-rendementen)
terug: een gemiddeld aandelenrendement ligt na een eeuw maar op twee procentpunt vast,
de variantie wel scherp. Zo ook hier: de drift $\kappa(\theta - i)$ wordt alleen beter
met een langere periode, de volatiliteit met elke extra maand.

De mediaan van $\hat\kappa$ ligt met 0,24 ruim boven de ware 0,15. Een geschatte
AR(1)-coëfficiënt is in een korte steekproef naar beneden vertekend, en een lagere $b$
geeft een hogere $\hat\kappa$: een persistente rente lijkt sneller terug te trekken dan
ze doet.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Vasicek, *An Equilibrium Characterization of the Term Structure*, Journal of
Financial Economics 1977 {cite}`Vasicek1977`; Cox, Ingersoll & Ross, *A Theory of the
Term Structure of Interest Rates*, Econometrica 1985 {cite}`CoxIngersollRoss1985`;
Litterman & Scheinkman, *Common Factors Affecting Bond Returns*, Journal of Fixed Income
1991 {cite}`LittermanScheinkman1991`; Longstaff & Schwartz, *Valuing American Options by
Simulation*, Review of Financial Studies 2001 {cite}`LongstaffSchwartz2001`.

**Wat.** De Vasicek- en CIR-curve naast de waargenomen curve; tabel 2 van Litterman en
Scheinkman (drie factoren verklaren gemiddeld 98,4% van de variantie); de eerste rij van
tabel 1 van Longstaff en Schwartz (een Amerikaanse put).

**Data hier.** De maandelijkse driemaandsrente uit FRED en de nulcouponcurve van
Gürkaynak, Sack en Wright {cite}`GurkaynakSackWright2007`, 1 tot 30 jaar. Voor LSM
gesimuleerde paden, zoals in het artikel.

**Verschil met het origineel.** Vasicek en CIR schatten niets; wij schatten met maximum
likelihood op een maandgemiddelde T-billrente. Litterman en Scheinkman gebruikten
wekelijkse excess rendementen over 1984–1988, wij maandelijkse yieldveranderingen.

**Verwachte afwijking.** Drie componenten verklaren meer dan 95%, de correlatie tussen 1-
en 10-jaarsveranderingen ligt duidelijk onder één, en Vasicek zit met de 10-jaarsyield in
1981 en 2021 meer dan een procentpunt naast de curve, in tegengestelde richting. LSM ligt
binnen twee standaardfouten van een binomiale boom.
```

### Vasicek en CIR op de driemaandsrente

We schatten Vasicek als AR(1), met standaardfouten via de *deltamethode* (de standaardfout
van een functie van geschatte parameters, via haar afgeleiden). CIR schatten we met
maximum likelihood op de niet-centrale $\chi^2$-dichtheid van de overgang.

```{code-cell} ipython3
short = (hap_data.fred("TB3MS")["TB3MS"] / 100).loc["1971-08":]   # 3-month T-bill, monthly average
short.index = short.index + pd.offsets.MonthEnd(0)
dt_m = 1 / 12

# Vasicek: exact AR(1) with delta-method standard errors
ols = sm.OLS(short.values[1:], sm.add_constant(short.values[:-1])).fit()
c_hat, b_hat = ols.params
cov_cb = ols.cov_params()
kappa_v = -np.log(b_hat) / dt_m
theta_v = c_hat / (1 - b_hat)
sigma_v = np.std(ols.resid, ddof=2) * np.sqrt(2 * kappa_v / (1 - b_hat**2))
grad_kappa = np.array([0.0, -1 / (b_hat * dt_m)])
grad_theta = np.array([1 / (1 - b_hat), c_hat / (1 - b_hat) ** 2])
se_kappa_v = np.sqrt(grad_kappa @ cov_cb @ grad_kappa)
se_theta_v = np.sqrt(grad_theta @ cov_cb @ grad_theta)


# CIR: maximum likelihood with the noncentral chi-square transition density
def cir_negloglik(log_params, x, dt):
    kappa, theta, sigma = np.exp(log_params)
    c = 2 * kappa / (sigma**2 * (1 - np.exp(-kappa * dt)))
    df = 4 * kappa * theta / sigma**2
    nonc = 2 * c * x[:-1] * np.exp(-kappa * dt)
    return -np.sum(np.log(2 * c) + stats.ncx2.logpdf(2 * c * x[1:], df, nonc))


fit_cir = optimize.minimize(cir_negloglik, np.log([0.2, 0.04, 0.08]), args=(short.values, dt_m),
                            method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-8, "fatol": 1e-8})
kappa_c, theta_c, sigma_c = np.exp(fit_cir.x)

pd.DataFrame(
    {
        "Vasicek": [kappa_v, theta_v, sigma_v, se_kappa_v, se_theta_v, np.nan],
        "CIR": [kappa_c, theta_c, sigma_c, np.nan, np.nan, 2 * kappa_c * theta_c / sigma_c**2],
    },
    index=["kappa", "theta", "sigma", "SE kappa", "SE theta", "Feller 2*kappa*theta/sigma^2"],
).round(4)
```

De tabel bevestigt de simulatie: de volatiliteit ligt scherp vast, de drift niet. De
snelheid van terugtrekken heeft bij Vasicek een $t$-waarde van maar
$0{,}1003/0{,}0608 = 1{,}6$, en het gemiddelde $\theta$ heeft een standaardfout van twee
procentpunt, [de standaardfout van 2%](#00-01-rendementen) voor de rente. De
Feller-verhouding van CIR ligt net boven één, omdat de rente jarenlang bij nul lag.

### De modelcurve naast de waargenomen curve

De marktprijs van risico zit alleen in de curve. We kiezen per model één constante
$\lambda$ (voor CIR één $\kappa^{*}$) die de kwadratische afstand tot de GSW-yields van 1
tot 10 jaar over alle maanden minimaliseert.

```{code-cell} ipython3
gsw_month = hap_data.gsw().resample("ME").last()
maturities = np.arange(1, 31)
yield_cols = [f"SVENY{m:02d}" for m in maturities]
curves = gsw_month[yield_cols].loc["1971-08":]
common = curves.index.intersection(short.index)
fit_block = curves.loc[common, yield_cols[:10]]
mask = fit_block.notna().to_numpy()
i_now = short.loc[common].to_numpy()[:, None]
tau10 = maturities[None, :10].astype(float)


def mse_vasicek(lam):
    model = vasicek_yield(i_now, tau10, kappa_v, theta_v, sigma_v, lam)
    return np.mean((model - fit_block.to_numpy())[mask] ** 2)


def mse_cir(kappa_q):
    model = cir_yield(i_now, tau10, kappa_c, theta_c, sigma_c, kappa_q)
    return np.mean((model - fit_block.to_numpy())[mask] ** 2)


lam_v = optimize.minimize_scalar(mse_vasicek, bounds=(-5, 5), method="bounded")
kq_c = optimize.minimize_scalar(mse_cir, bounds=(-0.5, 1.0), method="bounded")

dates = ["1981-09-30", "2000-06-30", "2008-12-31", "2021-06-30", str(common[-1].date())]
rows = []
for date in dates:
    i_date = short.loc[date]
    for m in (1, 5, 10):
        rows.append({
            "datum": date[:7], "looptijd": m,
            "GSW": curves.loc[date, f"SVENY{m:02d}"],
            "Vasicek": vasicek_yield(i_date, m, kappa_v, theta_v, sigma_v, lam_v.x),
            "CIR": cir_yield(i_date, m, kappa_c, theta_c, sigma_c, kq_c.x),
        })
fit_table = pd.DataFrame(rows).set_index(["datum", "looptijd"])
fit_table["fout Vasicek"] = fit_table["Vasicek"] - fit_table["GSW"]
fit_table["fout CIR"] = fit_table["CIR"] - fit_table["GSW"]
print(f"Vasicek: lambda = {lam_v.x:.3f}, RMSE = {1e4 * np.sqrt(lam_v.fun):.0f} bp, "
      f"lange yield = {vasicek_yield(0.0, 1e4, kappa_v, theta_v, sigma_v, lam_v.x):.2%}")
print(f"CIR: kappa* = {kq_c.x:.3f}, RMSE = {1e4 * np.sqrt(kq_c.fun):.0f} bp")
(100 * fit_table).round(2)
```

De tabel geeft yields in procenten. Beide modellen zitten gemiddeld ruim een procentpunt
naast de curve, en hun grootste fouten liggen aan de lange kant in 1981, 2008 en 2021.
Let in de figuur op de afstand tussen de zwarte lijn en de modellen aan de lange kant.

```{code-cell} ipython3
:label: cel-termijnstructuur-real-options-curves
:tags: [hide-input]

fig, axes = plt.subplots(2, 3, figsize=(12, 7.5))
tau_fine = np.linspace(0.25, 30, 120)
for ax, date in zip(axes.flat, dates):
    obs = curves.loc[date].dropna()
    i_date = short.loc[date]
    ax.plot(maturities[: len(obs)], 100 * obs.to_numpy(), color="black", lw=2, label="GSW")
    ax.plot(tau_fine, 100 * vasicek_yield(i_date, tau_fine, kappa_v, theta_v, sigma_v, lam_v.x),
            color=hap.plotting.COLORS[0], label="Vasicek")
    ax.plot(tau_fine, 100 * cir_yield(i_date, tau_fine, kappa_c, theta_c, sigma_c, kq_c.x),
            color=hap.plotting.COLORS[1], ls="--", label="CIR")
    ax.scatter([0.25], [100 * i_date], color=hap.plotting.COLORS[3], zorder=3, label="3-mnd rente")
    ax.set_title(date[:7])
    ax.set_xlabel("Looptijd (jaren)")
    ax.set_ylabel("Yield (%)")
axes.flat[0].legend()

ax = axes.flat[5]
ten = curves.loc[common, "SVENY10"]
ax.plot(ten.index, 100 * ten, color="black", lw=1.2, label="GSW 10 jaar")
ax.plot(common, 100 * vasicek_yield(short.loc[common].to_numpy(), 10.0, kappa_v, theta_v, sigma_v, lam_v.x),
        color=hap.plotting.COLORS[0], lw=1, label="Vasicek 10 jaar")
ax.set_title("10-jaarsyield door de tijd")
ax.set_xlabel("Jaar")
ax.set_ylabel("Yield (%)")
ax.legend()
fig.suptitle("Eenfactormodellen met constante marktprijs van risico naast de GSW-curve")
plt.tight_layout()
plt.show()
```

:::{figure} #cel-termijnstructuur-real-options-curves
:label: fig-termijnstructuur-real-options-curves
:width: 100%

In 1981 zet Vasicek de 10-jaarsyield te laag, in 2021 te hoog. CIR zit in 2008 te laag.
Rechtsonder: de 10-jaarsyield van het model volgt de korte rente, de waargenomen
10-jaarsyield beweegt trager en op eigen kracht.
:::

Vasicek zet de lange yield vast op één getal, hier 8,3%. Daardoor verklaart het model
een hoge lange yield niet samen met een hoge korte rente (1981), en een lage lange yield
niet samen met een korte rente van nul (2021).

CIR maakt de omgekeerde fout. Bij een hoge rente stijgt de curve te steil (1981), en bij
een rente van nul schakelt de vierkantswortel de volatiliteit uit, zodat de curve te vlak
blijft (2008). Beide fouten zijn [](#cor-termijnstructuur-real-options-correlatie) in de
vorm van een curve.

### Drie factoren: level, slope en curvature

Drijft één factor de curve, dan vindt een principale-componentenanalyse op
yieldveranderingen één component. We rekenen haar uit op maandelijkse veranderingen van 1
tot 10 en van 1 tot 30 jaar.

```{code-cell} ipython3
pca_cols = yield_cols[:10]
changes = curves[pca_cols].dropna().diff().dropna()
eigval, eigvec = np.linalg.eigh(np.cov(changes.to_numpy().T))
order = np.argsort(eigval)[::-1]
eigval, eigvec = eigval[order], eigvec[:, order]
sign_at_10y = np.sign(eigvec[-1])        # eigenvectors have arbitrary sign
eigvec = eigvec * sign_at_10y            # orient: positive loading at 10 years

long_changes = curves[yield_cols].dropna().diff().dropna()
eigval_30 = np.sort(np.linalg.eigvalsh(np.cov(long_changes.to_numpy().T)))[::-1]

pca_table = pd.DataFrame(
    {
        "Litterman-Scheinkman 1991": [89.5, 8.5, 2.0, 98.4],
        f"hier, 1-10 jaar, {changes.index[0]:%Y-%m}–{changes.index[-1]:%Y-%m}":
            np.append(100 * eigval[:3] / eigval.sum(), 100 * eigval[:3].sum() / eigval.sum()),
        f"hier, 1-30 jaar, {long_changes.index[0]:%Y-%m}–{long_changes.index[-1]:%Y-%m}":
            np.append(100 * eigval_30[:3] / eigval_30.sum(), 100 * eigval_30[:3].sum() / eigval_30.sum()),
    },
    index=["factor 1 (level)", "factor 2 (slope)", "factor 3 (curvature)", "totaal drie factoren"],
).round(1)
corr_1_10 = changes["SVENY01"].corr(changes["SVENY10"])
print(f"correlatie van maandelijkse veranderingen 1 en 10 jaar: {corr_1_10:.2f} (eenfactormodel: 1)")
pca_table
```

De verdeling tot 30 jaar is bijna die van Litterman en Scheinkman. De iets hogere totalen
komen deels door de Svensson-curve van GSW (een gladde functie met zes parameters,
per dag door de waargenomen yields gelegd), die ruis uit de kleine componenten filtert. De correlatie tussen 1- en 10-jaarsveranderingen is 0,69. Let in de figuur op hoe
vaak elke lijn van teken wisselt.

```{code-cell} ipython3
:label: cel-termijnstructuur-real-options-pca
:tags: [hide-input]

fig, ax = plt.subplots()
labels = ["level", "slope", "curvature"]
for j in range(3):
    ax.plot(np.arange(1, 11), eigvec[:, j], marker="o", label=f"component {j + 1} ({labels[j]})")
ax.axhline(0, color="black", lw=0.8)
ax.set_title("Ladingen van de eerste drie principale componenten van yieldveranderingen")
ax.set_xlabel("Looptijd (jaren)")
ax.set_ylabel("Lading")
ax.legend()
plt.show()
```

:::{figure} #cel-termijnstructuur-real-options-pca
:label: fig-termijnstructuur-real-options-pca
:width: 90%

De eerste component heeft positieve ladingen op alle looptijden, licht aflopend: een
bijna parallelle verschuiving (*level*). De tweede verandert tussen vier en vijf jaar van
teken: kort en lang bewegen tegengesteld (*slope*). De derde is positief aan beide
uiteinden en negatief in het midden (*curvature*). Dat zijn de vormen uit figuur 2 van
Litterman en Scheinkman.
:::

De tabel zet de uitkomsten naast de verwachting uit het replicatieblok.

```{code-cell} ipython3
first_pc_one_sign = bool(np.all(eigvec[:, 0] > 0))
second_pc_sign_changes = int(np.sum(np.diff(np.sign(eigvec[:, 1])) != 0))
error_1981 = fit_table.loc[("1981-09", 10), "fout Vasicek"]
error_2021 = fit_table.loc[("2021-06", 10), "fout Vasicek"]
pd.DataFrame(
    {
        "verwacht": ["> 95", "> 95", "ja", "1", "duidelijk < 1", "> 1", "> 1", "ja"],
        "hier": [pca_table.iloc[3, 1], pca_table.iloc[3, 2], "ja" if first_pc_one_sign else "nee",
                 second_pc_sign_changes, round(corr_1_10, 2), round(100 * abs(error_1981), 2),
                 round(100 * abs(error_2021), 2), "ja" if error_1981 * error_2021 < 0 else "nee"],
    },
    index=["drie componenten, 1-10 jaar (%)", "drie componenten, 1-30 jaar (%)",
           "component 1: één teken", "component 2: tekenwisselingen", "correlatie 1 en 10 jaar",
           "|fout Vasicek| 10 jaar, 1981 (pp)", "|fout Vasicek| 10 jaar, 2021 (pp)",
           "fouten tegengesteld van teken"],
)
```

**Geslaagd.** Elke verwachting uit het replicatieblok komt uit: drie componenten verklaren
99,9% en 98,9%, de correlatie ligt ver onder één, en Vasicek zit in 1981 en 2021 ruim een
procentpunt naast de curve, in tegengestelde richting. Dat de eerste component negen tiende
verklaart, laat zien waarom Vasicek als benadering bruikbaar was.

### LSM tegen een binomiale boom

De put uit tabel 1 van Longstaff en Schwartz heeft $S = 36$, $K = 40$, $\sigma = 0{,}20$,
$T = 1$ en $i = 6\%$, en is vijftig keer per jaar uitoefenbaar. Maatstaf is een binomiale
boom van 5000 stappen waarin elke honderdste stap uitoefenbaar is. LSM gebruikt 100.000
paden, de helft *antithetisch* (elk pad met zijn spiegelbeeld). De regressoren zijn een
constante en nul tot drie gewogen *Laguerre-polynomen* van $x = S/K$: veeltermen in $x$,
vermenigvuldigd met $e^{-x/2}$, zodat de regressie goed geconditioneerd blijft.

```{code-cell} ipython3
def binomial_put(S0, K, rate, sigma, T, n_steps, exercise_every=1):
    """CRR binomial American/Bermudan put; exercise allowed every `exercise_every` steps."""
    dt = T / n_steps
    up = np.exp(sigma * np.sqrt(dt))
    q = (np.exp(rate * dt) - 1 / up) / (up - 1 / up)
    disc = np.exp(-rate * dt)
    S = S0 * up ** np.arange(n_steps, -n_steps - 1, -2)
    V = np.maximum(K - S, 0.0)
    for step in range(n_steps - 1, -1, -1):
        S = S[:-1] / up
        V = disc * (q * V[:-1] + (1 - q) * V[1:])
        if step % exercise_every == 0:
            V = np.maximum(V, K - S)
    return V[0]


def lsm_put(S0, K, rate, sigma, T, n_exercise, n_paths, n_laguerre, rng):
    """Longstaff-Schwartz LSM value of a Bermudan put with antithetic paths.

    Regressors: a constant plus the first `n_laguerre` weighted Laguerre polynomials
    of S/K (the scaling keeps the regression well conditioned).
    """
    dt = T / n_exercise
    z = rng.standard_normal((n_paths // 2, n_exercise))
    z = np.vstack([z, -z])
    S = S0 * np.exp(np.cumsum((rate - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z, axis=1))
    cash = np.maximum(K - S[:, -1], 0.0)
    when = np.full(len(S), n_exercise)
    for k in range(n_exercise - 1, 0, -1):
        payoff = K - S[:, k - 1]
        itm = payoff > 0
        x = S[itm, k - 1] / K
        y = cash[itm] * np.exp(-rate * dt * (when[itm] - k))
        w = np.exp(-x / 2)
        basis = np.column_stack([np.ones_like(x), w, w * (1 - x), w * (1 - 2 * x + x**2 / 2)])
        design = basis[:, : n_laguerre + 1]
        coef, *_ = np.linalg.lstsq(design, y, rcond=None)
        exercise_now = payoff[itm] > design @ coef           # exercise beats continuation
        idx = np.flatnonzero(itm)[exercise_now]              # paths that exercise at step k
        cash[idx], when[idx] = payoff[idx], k
    pv = cash * np.exp(-rate * dt * when)
    return pv.mean(), pv.std(ddof=1) / np.sqrt(len(pv))
```

De tweede cel rekent boom, Black-Scholes-put en LSM uit en zet ze naast het artikel.

```{code-cell} ipython3
bermudan_tree = binomial_put(36, 40, 0.06, 0.20, 1.0, 5000, exercise_every=100)
d1 = (np.log(36 / 40) + (0.06 + 0.02) * 1.0) / 0.20
european_bs = 40 * np.exp(-0.06) * stats.norm.cdf(-(d1 - 0.20)) - 36 * stats.norm.cdf(-d1)

lsm = {}
for n_lag in range(4):
    lsm[n_lag] = lsm_put(36, 40, 0.06, 0.20, 1.0, 50, 100_000, n_lag, rng)

pd.DataFrame(
    {
        "origineel": [4.478, 3.844, np.nan, np.nan, np.nan, 4.472, 0.010],
        "hier": [bermudan_tree, european_bs] + [lsm[n][0] for n in range(4)] + [lsm[3][1]],
    },
    index=["Bermuda-put: eindige differenties / boom", "Europese put",
           "LSM, constante", "LSM, constante + 1 Laguerre", "LSM, constante + 2 Laguerre",
           "LSM, constante + 3 Laguerre", "standaardfout LSM (3 Laguerre)"],
).round(4)
```

**Geslaagd.** Boom en Europese put vallen samen met het artikel, en LSM met drie
polynomen ligt binnen één standaardfout van de boom. Met minder basisfuncties ligt LSM
eronder, met alleen een constante bijna vijftien cent, zoals
[](#thm-termijnstructuur-real-options-ondergrens) voorspelt.

## Wat er brak, en wat daarna kwam

**Wat de modellen verklaren.** Veel, en blijvend. Eén arbitrageargument geeft elke
obligatie en obligatieoptie een consistente prijs, en sinds Duffie en Kan is elk later
model een keuze van factoren. Dezelfde PDE maakte van investeringen opties, en LSM maakte
Amerikaanse opties op veel factoren rekenbaar. De eerste principale component verklaart
89% van de variantie.

**Waar het breekt.** Eén factor met een constante marktprijs van risico past kort en
lang niet tegelijk: Vasicek zit met de 10-jaarsyield in 1981 2,3 procentpunt te laag en in
2021 1,8 te hoog. Veranderingen in de 1- en 10-jaarsyield correleren 0,69, niet één.
Daaronder ligt [de standaardfout van 2%](#00-01-rendementen) in rentevorm: de drift is
na ruim vijftig jaar nauwelijks gemeten ($t = 1{,}6$ voor $\hat\kappa$).

**Risico of vergissing?** De Chicago-lezing (prijzen belonen risico dat door de tijd
varieert) zegt dat de marktprijs van risico niet constant is. Na tien jaar inflatie
eisten beleggers in 1981 een hoge vergoeding voor renterisico, in 2021 een lage, en de
fout is een gemeten risicopremie. De Yale-lezing (prijzen wijken af door vergissingen en
beperkte arbitrage) zegt dat beleggers recente inflatie extrapoleren, of dat
pensioenfondsen en centrale banken kopen ongeacht de prijs. Scheiden vraagt de
stochastische discontofactor in crises als 1979–1981, 2008 en 2022, en die zijn te
schaars. Wie in 1981 een lange obligatie tegen 15% kocht, droeg in de termen van
Santa-Clara een beprijsd risico, of dacht iets te weten wat de prijs niet wist. De data
kiezen niet.

**Wat er daarna kwam.** De term premium wordt later een eigen onderzoeksobject
([](#05-28-termijnstructuur-premies)). Eerst keert het vak terug naar de cross-sectie,
waar Fama en French de anomalieën van Basu, Banz en Rosenberg in één regressie
samenbrachten: [](#04-18-fama-french).

## Oefeningen

:::{exercise}
:label: ex-termijnstructuur-real-options-1

**Instap: een Amerikaanse put op de obligatie.** Neem de renteboom en de
driejaarsobligatie uit het toy-voorbeeld. Een Amerikaanse put op die obligatie met
uitoefenprijs $K = 0{,}87$ is uit te oefenen op $t = 0$, $1$ en $2$.

1. Bereken met de hand wat de put waard is, door op elke datum uitoefenen met doorgaan
   te vergelijken.
2. Wat is een Europese put met expiratie op $t = 2$ waard? Waarom verschillen de twee?
:::

:::{solution} ex-termijnstructuur-real-options-1
:class: dropdown

**(1)** Op $t = 2$ ligt de obligatie overal boven 0,87. Op $t = 1$ levert uitoefenen in
de hoge knoop $0{,}87 - 0{,}858001 = 0{,}011999$, en doorgaan niets. Op $t = 0$ levert
uitoefenen $0{,}87 - 0{,}866668 = 0{,}003332$, en wachten $\tfrac12(0{,}011999 + 0)/1{,}05 = 0{,}005714$. De houder wacht,
en de put is $0{,}005714$ waard.

**(2)** Nul, om dezelfde reden als op $t = 2$ hierboven. De code rekent beide na.

```{code-cell} ipython3
K_put = 0.87
put_t2 = np.maximum(K_put - bond_t2, 0.0)
continue_t1 = roll_back(put_t2, i_tree[1])
put_t1 = np.maximum(K_put - bond_t1, continue_t1)
continue_t0 = roll_back(put_t1, i_tree[0])[0]
pd.Series({
    "uitoefenen op t=1, hoge knoop": K_put - bond_t1[0],
    "direct uitoefenen op t=0": K_put - bond_t0,
    "wachten op t=0": continue_t0,
    "Amerikaanse put": max(K_put - bond_t0, continue_t0),
    "Europese put, expiratie t=2": roll_back(continue_t1, i_tree[0])[0],
}).round(6).to_frame("waarde")
```

Wat dit leert: een obligatie trekt naar haar nominale waarde, dus haar renterisico krimpt
met de tijd, en een obligatieoptie vraagt een model van de hele curve. Uitoefenen tegen
doorgaan is de beslissing die LSM met een regressie neemt.
:::

:::{exercise}
:label: ex-termijnstructuur-real-options-2

**Afleiding: Vasicek zonder Riccati.** Neem onder $\mathbb{Q}$
$\mathrm{d}i = \kappa(\theta^{*} - i)\,\mathrm{d}t + \sigma\,\mathrm{d}W^{\mathbb{Q}}$.

1. Laat zien dat $X = \int_t^T i_s\,\mathrm{d}s$ normaal verdeeld is met gemiddelde
   $\theta^{*}\tau + (i_t - \theta^{*})B(\tau)$ en variantie
   $\sigma^2\big[(\tau - B)/\kappa^2 - B^2/(2\kappa)\big]$. Leid daaruit
   [](#eq-termijnstructuur-real-options-vasicek) af.
2. Controleer het met Monte Carlo: 20.000 paden met dagelijkse stappen, $\kappa = 0{,}15$,
   $\theta = 5\%$, $\sigma = 1{,}5\%$, $\lambda = 0{,}3$, $i_0 = 2\%$ en $\tau = 5$.
3. Hoeveel verlaagt het convexiteitseffect de 30-jaarsyield en de oneindig lange yield?
:::

:::{solution} ex-termijnstructuur-real-options-2
:class: dropdown

**(1)** De oplossing van de Ornstein-Uhlenbeck-vergelijking is
$i_s = \theta^{*} + (i_t - \theta^{*})e^{-\kappa(s-t)} + \sigma\int_t^s e^{-\kappa(s-u)}\,\mathrm{d}W_u$.
Integreren en de integratievolgorde verwisselen geeft
$X = \theta^{*}\tau + (i_t - \theta^{*})B(\tau) + \sigma\int_t^T B(T-u)\,\mathrm{d}W_u$.
Dat is normaal, met variantie $\sigma^2\int_0^\tau B^2$ uit het bewijs van
[](#thm-termijnstructuur-real-options-vasicek). Met
$\E[e^{-X}] = \exp(-\E[X] + \tfrac12\Var(X))$ volgt

$$
\log p = -\theta^{*}\tau - (i_t - \theta^{*})B + \frac{\sigma^2}{2\kappa^2}(\tau - B) - \frac{\sigma^2B^2}{4\kappa}
       = \Big(\theta^{*} - \frac{\sigma^2}{2\kappa^2}\Big)(B - \tau) - \frac{\sigma^2B^2}{4\kappa} - B\,i_t .
$$

**(2) en (3)** De code simuleert de rente onder $\mathbb{Q}$ en integreert haar met de
trapeziumregel.

```{code-cell} ipython3
kappa, theta, sigma, lam, i0, tau = 0.15, 0.05, 0.015, 0.3, 0.02, 5.0
theta_q = theta + lam * sigma / kappa
n_paths, n_steps = 20_000, 252 * 5
step = tau / n_steps
a = np.exp(-kappa * step)
sd = sigma * np.sqrt((1 - a**2) / (2 * kappa))
rate = np.full(n_paths, i0)
integral = np.zeros(n_paths)
for _ in range(n_steps):
    rate_next = theta_q + a * (rate - theta_q) + sd * rng.standard_normal(n_paths)
    integral += 0.5 * (rate + rate_next) * step
    rate = rate_next
discount = np.exp(-integral)
closed = np.exp(-tau * vasicek_yield(i0, tau, kappa, theta, sigma, lam))
print(f"Monte Carlo: {discount.mean():.5f} (s.e. {discount.std(ddof=1) / np.sqrt(n_paths):.5f}), "
      f"gesloten vorm: {closed:.5f}")

B30 = (1 - np.exp(-kappa * 30)) / kappa
convexity_30 = sigma**2 / (2 * kappa**2) * (1 - B30 / 30) - sigma**2 * B30**2 / (4 * kappa * 30)
print(f"convexiteit 30 jaar: {convexity_30:.2%};  oneindig lang: {sigma**2 / (2 * kappa**2):.2%}")
```

De Monte-Carloprijs 0,82983 ligt 0,7 standaardfout (0,00043) onder de gesloten vorm 0,83013.
Het convexiteitseffect verlaagt de 30-jaarsyield met 0,34 en de oneindig lange yield met
0,50 procentpunt, klein naast de term premium van 3 procentpunt. Wat dit leert: de affiene formule is Jensens ongelijkheid uit
het toy-voorbeeld, toegepast op een normale integraal van de rente.
:::

:::{exercise}
:label: ex-termijnstructuur-real-options-3

**Twee deelsteekproeven.** Herhaal de replicatie op 1971-08 t/m 1999-12 en op 2000-01 t/m
2026-08.

1. Schat Vasicek in beide perioden, met standaardfouten voor $\hat\kappa$ en
   $\hat\theta$.
2. Bereken per periode de correlatie tussen 1- en 10-jaarsveranderingen en het aandeel van
   de eerste principale component (1–10 jaar).
3. Welke parameter verschilt het meest? Past één eenfactormodel op beide perioden?
:::

:::{solution} ex-termijnstructuur-real-options-3
:class: dropdown

```{code-cell} ipython3
def vasicek_with_se(x, dt=1 / 12):
    """Vasicek AR(1) estimates with delta-method standard errors."""
    fit = sm.OLS(x[1:], sm.add_constant(x[:-1])).fit()
    c, b = fit.params
    cov = fit.cov_params()
    kappa = -np.log(b) / dt
    g_kappa = np.array([0.0, -1 / (b * dt)])
    g_theta = np.array([1 / (1 - b), c / (1 - b) ** 2])
    return {
        "kappa": kappa, "SE kappa": np.sqrt(g_kappa @ cov @ g_kappa),
        "theta": c / (1 - b), "SE theta": np.sqrt(g_theta @ cov @ g_theta),
        "sigma": np.std(fit.resid, ddof=2) * np.sqrt(2 * kappa / (1 - b**2)),
    }


periods = {"1971-1999": ("1971-08", "1999-12"), "2000-2026": ("2000-01", "2026-08")}
rows_sub = {}
for label, (start, end) in periods.items():
    est = vasicek_with_se(short.loc[start:end].to_numpy())
    block = changes.loc[start:end]
    ev = np.sort(np.linalg.eigvalsh(np.cov(block.to_numpy().T)))[::-1]
    est["corr 1j-10j"] = block["SVENY01"].corr(block["SVENY10"])
    est["aandeel PC1"] = ev[0] / ev.sum()
    rows_sub[label] = est
subsamples = pd.DataFrame(rows_sub)
for name in ("kappa", "theta"):
    diff = subsamples.loc[name].diff().iloc[-1]
    se = np.sqrt((subsamples.loc[f"SE {name}"] ** 2).sum())
    print(f"verschil in {name}: {diff:.4f}, in standaardfouten: {diff / se:.2f}")
subsamples.round(4)
```

Vóór 2000 is $\hat\kappa = 0{,}28$ (standaardfout 0,14) en $\hat\theta = 6{,}8\%$, daarna
$0{,}10$ (0,07) en 1,3%. Dat zijn verschillen van $-1{,}15$ en $-2{,}86$
standaardfouten. De volatiliteit daalt van 2,0% naar 0,65%, de correlatie tussen 1- en
10-jaarsveranderingen van 0,76 naar 0,56, het aandeel van de eerste component van 0,93
naar 0,91. Wat dit leert: één eenfactormodel met vaste parameters past niet op
beide perioden, en de breuk is het scherpst in de tweede momenten, die goed meetbaar zijn.
:::

:::{exercise}
:label: ex-termijnstructuur-real-options-4

**Een mijn met de keuze om te sluiten.** Een mijn produceert één pond koper op $t = 1$ en
één op $t = 2$, tegen kosten $a = 1{,}00$ per pond. De koperprijs is $S_0 = 1{,}00$ en
gaat per periode met factor $u = 1{,}2$ omhoog of $d = 0{,}8$ omlaag ($d$ is hier de
daalfactor, niet het dividend). De risicovrije rente is $R^{f} = 5\%$ per periode; koper
is een verhandeld activum zonder convenience yield.

1. Bereken de risiconeutrale kans $q$ en de netto contante waarde als de mijn altijd
   produceert.
2. Bereken de waarde als de eigenaar in elke knoop mag sluiten. Wat is de keuze waard?
3. Openen kost 0,20. Wat zeggen beide waarderingen?
:::

:::{solution} ex-termijnstructuur-real-options-4
:class: dropdown

**(1)** $q = (1 + R^{f} - d)/(u - d) = (1{,}05 - 0{,}8)/0{,}4 = 0{,}625$, zoals $\pi^{*}$ in
[](#03-11-apt-no-arbitrage). Onder $q$ is de verwachte koperprijs $1{,}05$ op $t = 1$ en
$1{,}1025$ op $t = 2$, dus de netto contante waarde is
$0{,}05/1{,}05 + 0{,}1025/1{,}1025 = 0{,}140590$.

**(2)** Op $t = 2$ levert de mijn $\max(S - a, 0)$: $0{,}44$, $0$ of $0$. Op $t = 1$ levert
doorwerken in de hoge knoop $0{,}20 + 0{,}625 \cdot 0{,}44/1{,}05 = 0{,}461905$; in de lage
knoop $-0{,}20$, dus daar gaat de mijn dicht. Vandaag is ze
$0{,}625 \cdot 0{,}461905/1{,}05 = 0{,}274943$ waard, en de keuze
$0{,}274943 - 0{,}140590 = 0{,}134354$ (op onafgeronde getallen).

**(3)** De netto contante waarde (0,14) verwerpt het project, de waardering met de keuze
(0,27) accepteert het. De code rekent het na.

```{code-cell} ipython3
mine = dict(S0=1.00, u=1.2, d=0.8, R_f=0.05, cost=1.00)
q_mine = (1 + mine["R_f"] - mine["d"]) / (mine["u"] - mine["d"])
S1 = mine["S0"] * np.array([mine["u"], mine["d"]])
S2 = mine["S0"] * np.array([mine["u"] ** 2, mine["u"] * mine["d"], mine["d"] ** 2])
value_t2 = np.maximum(S2 - mine["cost"], 0.0)
continuation_t1 = (q_mine * value_t2[:-1] + (1 - q_mine) * value_t2[1:]) / (1 + mine["R_f"])
value_t1 = np.maximum(S1 - mine["cost"] + continuation_t1, 0.0)      # close the mine if negative
value_flexible = (q_mine * value_t1[0] + (1 - q_mine) * value_t1[1]) / (1 + mine["R_f"])
npv_rigid = sum((mine["S0"] * (1 + mine["R_f"]) ** t - mine["cost"]) / (1 + mine["R_f"]) ** t
                for t in (1, 2))
pd.DataFrame({
    "met de hand": {"q": 0.625, "NCW zonder keuze": 0.140590,
                    "mijn met keuze om te sluiten": 0.274943, "waarde van de keuze": 0.134354},
    "code": {"q": q_mine, "NCW zonder keuze": npv_rigid,
             "mijn met keuze om te sluiten": value_flexible,
             "waarde van de keuze": value_flexible - npv_rigid},
}).round(6)
```

Wat dit leert: de keuze om te sluiten verdubbelt bijna de waarde van de mijn, en een
netto contante waarde met de verwachte koperprijs rekent alsof de mijn in verliesjaren
doorwerkt.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
