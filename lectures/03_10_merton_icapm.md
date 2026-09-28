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

(03-10-merton-icapm)=

# Merton: continue tijd en het ICAPM

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1969–1973, met een uitloop naar 2000.

**Wat we al weten.** In het CAPM uit [](#02-08-capm) houdt iedereen dezelfde
risicoportefeuille, en is de marktbèta de enige maat voor risico. In
[](#02-09-black-scholes) leverde de stochastische calculus de prijs van een optie. Merton gebruikte
die wiskunde al vanaf 1969 voor de portefeuillekeuze, het onderwerp van deze lecture. De barst die openblijft, is de ene periode van het CAPM. Echte beleggers
beleggen een leven lang, en verwachte rendementen verschuiven onderweg.

**Welke vraag staat open.** Belegt iemand met een lange horizon anders dan iemand
met een korte, en wat betekent dat voor de prijzen?
```

## Overzicht

Belegt een langetermijnbelegger anders, en verandert dat de prijzen? Alleen als de
beleggingskansen in de tijd veranderen. Dan houdt hij naast de marktportefeuille
een hedgeportefeuille tegen slechter wordende kansen, en beloont het verwachte
rendement naast de marktbèta ook de bèta op de variabelen die die kansen
beschrijven. In deze lecture:

- rekenen we in een model van twee perioden uit dat een voorspelbaar rendement de
  vraag naar aandelen verhoogt, en een onvoorspelbaar rendement niet;

- leiden we af dat de horizon bij onafhankelijke rendementen niet uitmaakt, wat
  de optimale portefeuille in continue tijd is, en hoe de hedgevraag en de
  prijsvergelijking van het ICAPM daaruit volgen;

- simuleren we hoe goed een eeuw data de hedgevraag meet;

- repliceren we het VAR van {cite:t}`Barberis2000`, de horizonallocaties in de
  geest van {cite:t}`CampbellViceira1999` en het effect van parameteronzekerheid.

In 1969 verschenen twee artikelen over hetzelfde probleem: hoe verdeelt iemand
die een leven lang belegt zijn vermogen over een veilig en een risicovol activum?
Samuelson loste het op in discrete tijd {cite}`Samuelson1969`, zijn student Merton
in continue tijd {cite}`Merton1969`. Bij onafhankelijke rendementen deed de horizon
er in beide gevallen niet toe. In 1973 liet Merton de beleggingskansen zelf bewegen
en leidde hij het *intertemporal CAPM* (ICAPM) af {cite}`Merton1973b`. Dat werk
definieert het tijdvak, omdat het de asset pricing dynamisch maakte. Toen de
dividendopbrengst rendementen bleek te voorspellen, rekenden
{cite:t}`KimOmberg1996` en {cite:t}`CampbellViceira1999` de hedgevraag uit.

Op de vraag theorie of feit is het ICAPM een theorie met een open plek. Het zegt
welke vorm een prijsvergelijking heeft, maar niet welke variabelen erin horen.
Daardoor staat het elk meerfactormodel toe waarvan de factoren iets over de
toekomst voorspellen. De empirie van deze lecture toetst daarom de vraagkant, de
hedgevraag, en niet de prijsvergelijking zelf.

## Intuïtie: waarom zou dit waar zijn?

Een oude volkswijsheid zegt dat wie jong is meer in aandelen moet beleggen, omdat
slechte jaren over een lange periode uitmiddelen. Samuelson vond dat een
drogreden. Komen de rendementen elk jaar uit dezelfde verdeling, dan staat een
belegger elk jaar voor hetzelfde probleem. Vindt hij een verlies van tien procent
even erg, ongeacht of hij rijk of arm is, dan verandert er alleen de schaal. Hij kiest dan
elk jaar hetzelfde percentage, hoeveel jaren er ook nog komen.

Merton keek naar wat er gebeurt als rendementen voorspelbaar zijn. Na een
koersstijging zijn aandelen duur, is de dividendopbrengst laag en is het verwachte
rendement voor de komende jaren lager. Na een crash is het omgekeerd. Een aandeel
is dan twee dingen tegelijk. Het is een gok met een positieve verwachting, zoals
bij Markowitz. Het is ook een verzekering: het levert veel op in de toestand
waarin elke euro daarna weinig kan verdienen.

Een belegger die slechte uitkomsten zwaar weegt, waardeert die verzekering. Hij
koopt meer aandelen dan de som voor één periode voorschrijft, de *myopische vraag*
(bijziend: alsof alleen de volgende periode telt). Het extra deel heet de
*hedgevraag* (*hedging demand*: het deel van de portefeuille dat vermogen levert
wanneer de beleggingskansen, kortweg de kansen, verslechteren). Hoe meer toekomst er is om zich tegen
in te dekken, hoe groter zij wordt. Een belegger met logaritmisch nut let alleen
op het groeitempo van zijn vermogen en dekt zich niet in.

Die extra vraag werkt door in de prijzen. Als alle beleggers aandelen extra waarderen omdat ze indekken,
betalen ze er meer voor, en daalt het verwachte rendement. Een activum zonder
marktrisico dat goed indekt, verdient dan minder dan de risicovrije rente. Een
activum zonder marktrisico dat juist verliest wanneer de kansen verslechteren,
verdient meer. Merton schreef het in zijn abstract: verwachte rendementen kunnen
van de rente afwijken, ook zonder enig marktrisico {cite}`Merton1973b`.

We verwachten dus drie dingen. Bij onafhankelijke rendementen is de
aandelenfractie gelijk voor elke horizon. Als rendementen dalen na een stijging,
stijgt de fractie met de horizon, voor een belegger die risicomijdender is dan
iemand met logaritmisch nut. En in evenwicht krijgt een activum een lagere premie
naarmate het beter indekt tegen slechtere kansen.

## Toy-voorbeeld: twee perioden en een voorspelbaar rendement

Het kleinste geval waarin een hedgevraag kan bestaan, heeft twee perioden: er is
dan één morgen om zich tegen in te dekken. We beginnen met de imports-cel, de
enige van deze lecture.

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

**Opzet.** Het vermogen na een periode met fractie $w$ in aandelen is
$W(1 + wR^{e})$, met $R^{e}$ het excess rendement.

| grootheid | waarde |
|---|---|
| beginvermogen $W_0$ | 1 |
| nut over het eindvermogen | $u(W_2) = W_2^{1-\gamma}/(1-\gamma)$ met $\gamma = 2$, dus $-1/W_2$ |
| risicovrije rente $R^{f}$ | 0 |
| excess rendement in periode 1 | $+36\%$ of $-16\%$, elk met kans $\tfrac12$ |
| periode 2, geval A (onafhankelijk) | weer $+36\%$ of $-16\%$ |
| periode 2, geval B, na $+36\%$ ("duur") | $+20\%$ of $-20\%$, geen premie |
| periode 2, geval B, na $-16\%$ ("goedkoop") | weer $+36\%$ of $-16\%$ |

Periode 1 heeft een verwacht excess rendement van 10% en een standaarddeviatie van
26%. In geval B hangen de schok in het rendement en de schok in het verwachte
rendement negatief samen, zoals bij aandelen en de dividendopbrengst.

**Het recept.** Wie in periode 2 optimaal belegt, heeft op $t = 1$ de waarde
$-q/W_1$, met $q = \E[(1 + wR^{e})^{-1}]$ bij de optimale $w$ (Theorie leidt die vorm af). Een lagere $q$ is een
betere toekomst. In de eerste-ordevoorwaarde van periode 1 weegt $q$ elke uitkomst (stap 4 schrijft
die voorwaarde uit).

**Stap 1, myopisch.** De eerste-ordevoorwaarde
$0{,}36\,(1+0{,}36w)^{-2} = 0{,}16\,(1-0{,}16w)^{-2}$ geeft
$(1+0{,}36w)/(1-0{,}16w) = \sqrt{2{,}25} = 1{,}5$, dus $w = 0{,}50/0{,}60 = 0{,}8333$.

**Stap 2, de waarde van de toekomst.** Met $w = 5/6$ is
$q = \tfrac12/1{,}3 + \tfrac12/(13/15) = 25/26 = 0{,}9615$.

**Stap 3, geval A.** De toekomst geeft in beide toestanden dezelfde $q$. Die valt
weg uit de eerste-ordevoorwaarde, dus $w_0 = 0{,}8333$.

**Stap 4, geval B.** In de dure toestand is er geen premie. De belegger houdt daar
$w = 0$, dus $q_{\text{duur}} = 1$. In de goedkope toestand is $q_{\text{goedkoop}} = 25/26$.
De voorwaarde wordt
$0{,}36\,q_{\text{duur}}(1+0{,}36w)^{-2} = 0{,}16\,q_{\text{goedkoop}}(1-0{,}16w)^{-2}$,
dus $k = (1+0{,}36w)/(1-0{,}16w) = \sqrt{2{,}25 \cdot 26/25} = 1{,}5297$ en
$w_0 = (k-1)/(0{,}36 + 0{,}16k) = 0{,}5297/0{,}6048 = 0{,}8759$.

**Stap 5, omgekeerd.** Laat een stijging de markt goedkoop maken en een daling duur
(geval B'). Dan is $k = \sqrt{2{,}25 \cdot 25/26} = 1{,}4709$ en
$w_0 = 0{,}4709/0{,}5953 = 0{,}7909$.

In geval B houdt de belegger $0{,}8759 - 0{,}8333 = 0{,}0426$ meer in aandelen, ruim
vijf procent meer dan de myopische fractie, bij dezelfde verdeling van het rendement in periode 1. Dat
verschil is de hedgevraag. Het aandeel levert 36% op in de toestand waarin het
vermogen daarna niets meer kan verdienen, en daar is een euro het meest waard. De code
rekent hetzelfde uit, ook voor log-nut.

```{code-cell} ipython3
def continuation(up, down, w, gamma):
    """q = E[(1 + w R^e)^(1-gamma)] for two equally likely excess returns."""
    return 0.5 * (1 + w * up) ** (1 - gamma) + 0.5 * (1 + w * down) ** (1 - gamma)


def two_state_weight(up, down, q_up=1.0, q_down=1.0, gamma=2.0):
    """Optimal risky share with a zero interest rate, two equally likely excess returns and CRRA.

    q_up and q_down scale the marginal value of wealth in the state that
    follows each outcome; with q_up = q_down the problem is myopic.
    """
    k = (-up * q_up / (down * q_down)) ** (1 / gamma)
    return (k - 1) / (up - k * down)


def toy_table(gamma):
    w_good = two_state_weight(0.36, -0.16, gamma=gamma)
    q_good = continuation(0.36, -0.16, w_good, gamma)
    q_dear = continuation(0.20, -0.20, two_state_weight(0.20, -0.20, gamma=gamma), gamma)
    return {
        "myopisch (een periode)": w_good,
        "A: onafhankelijk": two_state_weight(0.36, -0.16, q_good, q_good, gamma),
        "B: stijging -> duur": two_state_weight(0.36, -0.16, q_dear, q_good, gamma),
        "B': stijging -> goedkoop": two_state_weight(0.36, -0.16, q_good, q_dear, gamma),
        "q goedkoop": q_good,
        "q duur": q_dear,
    }


hand = pd.Series({"myopisch (een periode)": 0.8333, "A: onafhankelijk": 0.8333,
                  "B: stijging -> duur": 0.8759, "B': stijging -> goedkoop": 0.7909,
                  "q goedkoop": 0.9615, "q duur": 1.0})
pd.DataFrame({"met de hand": hand, "code, gamma = 2": toy_table(2.0),
              "code, gamma = 1 (log)": toy_table(1.0)}).round(4)
```

De code geeft tot op vier decimalen de handberekening. In de kolom voor
logaritmisch nut is $q = 1$ in elke toestand, en zijn alle vier de allocaties gelijk
aan de myopische 1,7361. We weten nu dat een voorspelbaar rendement de vraag naar
aandelen verschuift, dat het teken afhangt van hoe rendement en kansen samen
bewegen, en dat log-nut ongevoelig is voor beide.

## Theorie

We leiden vijf resultaten af. Eerst de stelling van Samuelson: bij onafhankelijke
rendementen maakt de horizon niet uit. Daarna volgen de optimale portefeuille in
continue tijd en de hedgevraag die erbij komt als de beleggingskansen bewegen. De
kern is de vierde stap: tel de vraag van alle beleggers op, en er volgt het ICAPM.
Tot slot rekenen we de hedgevraag uit in een markt met een voorspelbaar rendement.

### Opzet en aannames

De belegger maximeert het verwachte nut van zijn eindvermogen $W_T$ op horizon $T$,
met nut $W^{1-\gamma}/(1-\gamma)$. Dat is *CRRA-nut* (constante relatieve
risicoaversie): hij vindt een procentueel verlies even erg bij elk vermogen, en
$\gamma$ is bijvoorbeeld 2, zoals in het toy-voorbeeld. Consumptie laten we weg.
Merton liet zien dat zij de portefeuilleregels hieronder niet verandert
{cite}`Merton1969`. In discrete tijd groeit
het vermogen met $W_{t+1} = W_t(1 + R^{f} + w_tR^{e}_{t+1})$.

In continue tijd is $r$ de continu samengestelde rente, zoals in
[](#02-09-black-scholes). Het risicovolle activum volgt

```{math}
:label: eq-merton-icapm-prijs
\frac{dS_t}{S_t} = \mu\,dt + \sigma\,dZ_t .
```

Het aandeel groeit gemiddeld met $\mu$ per jaar en schommelt met volatiliteit
$\sigma$, in het toy-voorbeeld een premie $\mu - r$ van 10% bij $\sigma = 26\%$.
$Z_t$ is een standaard Brownse beweging. In [](#02-09-black-scholes) heette zij
$W_t$, maar hier is $W$ het vermogen. Met fractie $w_t$ in aandelen beweegt het
vermogen volgens

```{math}
:label: eq-merton-icapm-budget
dW_t = \left[\, r + w_t(\mu - r) \,\right] W_t\,dt + w_t\,\sigma\,W_t\,dZ_t .
```

Het vermogen groeit met de rente plus de premie op het deel in aandelen, en
schommelt met dat deel. Dit is de vermogensvergelijking van {cite:t}`Merton1969`,
in onze symbolen. De *waardefunctie* is het beste verwachte nut vanaf vermogen $W$
op tijdstip $t$:

```{math}
:label: eq-merton-icapm-doel
J(W, t) = \max_{\{w_s\}_{s \ge t}} \E_t\!\left[\frac{W_T^{1-\gamma}}{1-\gamma}\right].
```

### Samuelson: wanneer de horizon er niet toe doet

*Waarom zou dit waar zijn?* Een belegger wiens vermogen verdubbelt, verdubbelt
elke positie en kiest dezelfde procentuele gok. Komen de rendementen elk jaar uit
dezelfde verdeling, dan is het probleem van volgend jaar een geschaalde kopie van
dat van dit jaar. Hij kiest dan hetzelfde percentage. Alleen als sommige
toestanden van morgen betere kansen bieden dan andere, kan de toekomst de keuze
van vandaag verschuiven.

:::{prf:theorem} Horizon-irrelevantie (Samuelson 1969, Merton 1969)
:label: thm-merton-icapm-samuelson

Laat de belegger $\E_0[W_T^{1-\gamma}/(1-\gamma)]$ maximeren, met $R^{f}$ constant
en $R^{e}_{t+1}$ onafhankelijk en gelijk verdeeld over de tijd. Laat $w^{\ast}$ het
eenperiodige probleem $\max_w \E[(1 + R^{f} + wR^{e})^{1-\gamma}]/(1-\gamma)$
oplossen. Dan is $w_t = w^{\ast}$ optimaal voor elke $t$ en elke horizon $T$.
:::

Het bewijsidee is het recept van het toy-voorbeeld. Werk achterwaarts. Op elk
tijdstip is de waardefunctie $q_{t+1}W^{1-\gamma}/(1-\gamma)$, met $q_{t+1}$ een
getal. Een constante factor verandert het maximum niet, dus vindt de belegger elke
periode $w^{\ast}$. In geval A was $q = 25/26$ in beide toestanden.
Dat is de eerste voorspelling van de intuïtie.

:::{prf:proof}
:class: dropdown

Noem de waardefunctie in discrete tijd $V_t(W)$; $J_t$ is verderop een afgeleide.
Op $t = T$ is $V_T(W) = W^{1-\gamma}/(1-\gamma)$, dus $q_T = 1$. Stel
$V_{t+1}(W) = q_{t+1}W^{1-\gamma}/(1-\gamma)$ met $q_{t+1} > 0$ een getal. Dan is

$$
V_t(W) = \max_w \E_t\!\left[q_{t+1}\frac{\left(W(1 + R^{f} + wR^{e}_{t+1})\right)^{1-\gamma}}{1-\gamma}\right]
= q_{t+1}W^{1-\gamma}\,\max_w \frac{\E\!\left[(1 + R^{f} + wR^{e})^{1-\gamma}\right]}{1-\gamma} .
$$

De tweede gelijkheid gebruikt dat $q_{t+1}$ geen toevalsvariabele is, en dat de
verdeling van $R^{e}_{t+1}$ niet van eerdere uitkomsten afhangt (de aanname van
onafhankelijkheid). Het maximum ligt dus in $w^{\ast}$, los van $W$ en $t$, en
$q_t = q_{t+1}\,\E[(1 + R^{f} + w^{\ast}R^{e})^{1-\gamma}] > 0$. $\square$
:::

Het bewijs wijst ook aan waar het misgaat. Hangt $q_{t+1}$ af van een toestand die
met $R^{e}_{t+1}$ samenhangt, dan mag hij niet buiten de verwachting en weegt hij
de uitkomsten. Dat was geval B van het toy-voorbeeld.

### De Merton-portefeuille

*Waarom zou dit waar zijn?* Een belegger die elk ogenblik mag bijsturen, kijkt
steeds maar een ogenblik vooruit. Over zo'n kort interval tellen alleen de
verwachting en de variantie van het rendement. Hij koopt aandelen tot de extra
premie niet meer opweegt tegen de extra variantie. Hoe risicomijdender hij is of
hoe wilder het aandeel beweegt, hoe minder hij koopt.

Het principe van Bellman zegt dat een optimaal plan ook vanaf elk later moment
optimaal is: $J(W_t,t) = \max_w \E_t[J(W_{t+dt},t+dt)]$. Trek $J(W_t,t)$ aan beide
kanten af, en er staat $0 = \max_w \E_t[dJ]$. De regel van Itô
uit [](#02-09-black-scholes) schrijft $dJ$ uit, met $J_t$, $J_W$ en $J_{WW}$ de
partiële afgeleiden:

$$
dJ = J_t\,dt + J_W\,dW + \tfrac12 J_{WW}\,(dW)^2 ,
\qquad (dW)^2 = w^2\sigma^2W^2\,dt .
$$

Omdat $\E_t[dZ_t] = 0$, volgt de *Hamilton-Jacobi-Bellman-vergelijking*
(HJB-vergelijking: de Bellman-vergelijking in continue tijd)

```{math}
:label: eq-merton-icapm-hjb
0 = \max_{w}\Big\{ J_t + J_W\,W\left[r + w(\mu - r)\right] + \tfrac12 J_{WW}\,w^2\sigma^2 W^2 \Big\},
\qquad J(W,T) = \frac{W^{1-\gamma}}{1-\gamma} .
```

Bij de beste keuze verandert de waarde gemiddeld niet: rente en premie verhogen
haar, en de variantie verlaagt haar via de kromming $J_{WW} < 0$. De uitdrukking
is kwadratisch in $w$, en de eerste-ordevoorwaarde is

```{math}
:label: eq-merton-icapm-foc
w^{\ast} = -\frac{J_W}{W J_{WW}}\cdot\frac{\mu - r}{\sigma^2} .
```

De belegger koopt de premie per eenheid variantie, maal de risicotolerantie van
zijn waardefunctie. Die tolerantie kan verschillen van die van zijn nut, en in dat
verschil zitten alle horizoneffecten.

:::{prf:theorem} Merton-portefeuille
:label: thm-merton-icapm-merton

Laat $\mu$, $\sigma$ en $r$ constant zijn en de belegger
[](#eq-merton-icapm-doel) maximeren onder [](#eq-merton-icapm-budget). Dan is de
optimale fractie in het risicovolle activum

```{math}
:label: eq-merton-icapm-merton
w^{\ast} = \frac{\mu - r}{\gamma\,\sigma^2} ,
```

onafhankelijk van $W$, $t$ en $T$.
:::

Het bewijsidee: probeer een waardefunctie van dezelfde vorm als het nut, $W^{1-\gamma}$
maal een functie van de tijd. Die heeft dezelfde relatieve risicoaversie $\gamma$,
en [](#eq-merton-icapm-foc) geeft dan [](#eq-merton-icapm-merton). Het bewijs gaat
na dat die gok de HJB-vergelijking oplost.

:::{prf:proof}
:class: dropdown

Probeer $J(W,t) = f(t)\,W^{1-\gamma}/(1-\gamma)$ met $f > 0$ en $f(T) = 1$. Dan is
$J_W = f\,W^{-\gamma}$ en $J_{WW} = -\gamma f\,W^{-\gamma-1}$, dus
$-J_W/(WJ_{WW}) = 1/\gamma$ en [](#eq-merton-icapm-foc) geeft
[](#eq-merton-icapm-merton). Invullen in [](#eq-merton-icapm-hjb) en delen door
$W^{1-\gamma}$ geeft

$$
0 = \frac{f'}{1-\gamma} + f\left[r + \frac{(\mu-r)^2}{2\gamma\sigma^2}\right],
$$

met oplossing $f(t) = \exp\{(1-\gamma)[r + (\mu-r)^2/(2\gamma\sigma^2)](T-t)\}$ en
$f(T) = 1$. Dat een gladde oplossing van de HJB-vergelijking ook de waardefunctie
is, volgt uit een standaard verificatiestelling. $\square$
:::

Met de getallen van het toy-voorbeeld is $w^{\ast} = 0{,}10/(2 \cdot 0{,}0676) = 0{,}7396$.
In de wereld met twee uitkomsten was het 0,8333, door de scheefheid van die
uitkomsten. Een hogere premie verhoogt $w^{\ast}$, een hogere $\gamma$ of $\sigma$
verlaagt hem.

Houdt één representatieve belegger de hele markt ($w^{\ast} = 1$),
dan zegt [](#eq-merton-icapm-merton) dat $\mu_m - r = \gamma\sigma_m^2$: de
marktpremie is risicoaversie maal variantie, 8% bij $\gamma = 2$ en $\sigma_m = 20\%$.

Met $N$ risicovolle activa, verwachte rendementen $\boldsymbol{\mu}$ en
covariantiematrix $\boldsymbol{\Sigma}$ wordt het
$\mathbf{w}^{\ast} = \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - r\mathbf{1})/\gamma$.
Dat is de separatiestelling uit [](#01-04-markowitz): iedereen houdt twee fondsen,
de risicovrije rente en dezelfde tangentportefeuille, in een verhouding die van
$\gamma$ afhangt. Markowitz had daarvoor normaliteit of kwadratisch nut nodig, in
continue tijd volgt het voor elk CRRA-nut.

### De hedgevraag

*Waarom zou dit waar zijn?* Laat het verwachte rendement afhangen van een
*toestandsvariabele* $x_t$, bijvoorbeeld de dividendopbrengst. De waarde van de
toekomst hangt dan af van vermogen én beleggingskansen. Een belegger die slechte
kansen vreest, koopt extra van een activum dat stijgt wanneer de kansen
verslechteren. Stijgen aandelen juist dan, dan gaat zijn aandelenfractie omhoog.

Laat $\mu_t = \mu(x_t)$ en

```{math}
:label: eq-merton-icapm-staat
dx_t = \mu_x(x_t)\,dt + \sigma_x(x_t)\,dZ^{x}_t ,
\qquad dZ_t\,dZ^{x}_t = \rho\,dt .
```

De toestand heeft een eigen drift $\mu_x$ en volatiliteit $\sigma_x$, en haar
schokken hangen met correlatie $\rho$ samen met die van het aandeel. Voor de
dividendopbrengst is $\rho$ sterk negatief, want een koersstijging verlaagt de
opbrengst. De waardefunctie is nu $J(W,x,t)$, en de HJB-vergelijking krijgt drie
termen erbij:

```{math}
:label: eq-merton-icapm-hjb-x
0 = \max_{w}\Big\{ J_t + J_W W\left[r + w(\mu - r)\right] + \tfrac12 J_{WW}w^2\sigma^2W^2
+ J_x \mu_x + \tfrac12 J_{xx}\sigma_x^2 + J_{Wx}\,w\,\sigma \sigma_x\rho\,W \Big\} .
```

De eerste twee nieuwe termen beschrijven hoe de kansen zelf bewegen. De laatste is
nieuw voor de keuze: de covariantie tussen vermogen en kansen, gewogen met hoe de
waarde van een euro verandert als de kansen veranderen ($J_{Wx}$).

:::{prf:theorem} Myopische en hedgevraag (Merton 1973)
:label: thm-merton-icapm-hedging

In het model [](#eq-merton-icapm-prijs)–[](#eq-merton-icapm-staat), met $J$ strikt
concaaf in $W$, is de optimale fractie

```{math}
:label: eq-merton-icapm-hedge
w^{\ast} = \underbrace{-\frac{J_W}{WJ_{WW}}\cdot\frac{\mu(x)-r}{\sigma^2}}_{\text{myopische vraag}}
\;\; \underbrace{-\;\frac{J_{Wx}}{WJ_{WW}}\cdot\frac{\rho\,\sigma_x}{\sigma}}_{\text{hedgevraag}} .
```
:::

:::{prf:proof}
Differentieer de uitdrukking tussen accolades in [](#eq-merton-icapm-hjb-x) naar
$w$ en stel het resultaat nul:
$J_W W(\mu - r) + J_{WW}w\sigma^2W^2 + J_{Wx}\sigma \sigma_x\rho W = 0$. Oplossen naar $w$
geeft [](#eq-merton-icapm-hedge). $\square$
:::

De eerste term is de Merton-portefeuille. De tweede heeft twee factoren.
$\rho\sigma_x/\sigma$ is de regressiecoëfficiënt van $dx$ op het rendement: hoeveel
de kansen bewegen per procent koersbeweging. De factor $-J_{Wx}/(WJ_{WW})$ zegt
hoeveel gewicht de belegger daaraan hecht. Bij CRRA-nut is $J = g(x,t)W^{1-\gamma}/(1-\gamma)$
met $g > 0$, en wordt die factor $g_x/(\gamma g)$. Bij log-nut is
$J = \log W + h(x,t)$, dus $J_{Wx} = 0$ en is er geen hedgevraag.

Het teken volgt de intuïtie, met één voorwaarde erbij. Neem $\gamma > 1$ en laat een
hogere $x$ betere kansen betekenen. Een hogere $J$ vraagt dan, omdat $1 - \gamma < 0$,
een lagere $g$, dus $g_x < 0$. Bij $\rho < 0$ is de hedgevraag positief: geval B van
het toy-voorbeeld. Draai $\rho$ om en zij wordt negatief, zoals in geval B'
(0,7909 onder 0,8333). Bij $\gamma < 1$ draait het teken ook om (oefening
[](#ex-merton-icapm-1)).

### Het kernresultaat: het intertemporele CAPM

*Waarom zou dit waar zijn?* Tel de vraag van alle beleggers op. Elke belegger
houdt de twee fondsen van Markowitz plus een hedgeportefeuille. In evenwicht moet
het totaal gelijk zijn aan de marktportefeuille. Een activum dat goed indekt, is
gewild. Wat gewild is, wordt duur, en wat duur is, heeft een laag verwacht
rendement.

Laat er $N$ risicovolle activa zijn en één toestandsvariabele $x$, met
$\Cov(d\mathbf{R}, dx) = \boldsymbol{\sigma}_{Rx}\,dt$. Uitgebreid naar $N$ activa
kiest belegger $k$ met vermogen $W_k$

```{math}
:label: eq-merton-icapm-vraag
\mathbf{w}_k = T_k\,\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - r\mathbf{1})
+ H_k\,\boldsymbol{\Sigma}^{-1}\boldsymbol{\sigma}_{Rx},
\qquad
T_k = -\frac{J^k_W}{W_kJ^k_{WW}},\quad H_k = -\frac{J^k_{Wx}}{W_kJ^k_{WW}} .
```

Elke belegger houdt de tangentportefeuille, geschaald met zijn risicotolerantie
$T_k$, en de hedgeportefeuille $\boldsymbol{\Sigma}^{-1}\boldsymbol{\sigma}_{Rx}$,
geschaald met zijn hedgebehoefte $H_k$. De hedgeportefeuille is de portefeuille die
zo sterk mogelijk met $dx$ meebeweegt. Merton noemde dit de
*drie-fondsenstelling*: risicovrije rente, markt en hedgeportefeuille. Met $K$
toestandsvariabelen zijn het $K + 2$ fondsen. $T_k$ is hier de risicotolerantie, niet
de horizon $T$.

:::{prf:theorem} ICAPM (Merton 1973)
:label: thm-merton-icapm-icapm

Als alle beleggers dezelfde $\boldsymbol{\mu}$, $\boldsymbol{\Sigma}$ en
$\boldsymbol{\sigma}_{Rx}$ zien, [](#eq-merton-icapm-vraag) kiezen en de markt
ruimt, dan geldt voor elk activum $i$

```{math}
:label: eq-merton-icapm-icapm
\mu_i - r = \beta_{i,m}\,\lambda_m + \beta_{i,x}\,\lambda_x ,
```

met $(\beta_{i,m}, \beta_{i,x})$ de meervoudige regressiecoëfficiënten van $dR_i$ op
het marktrendement en op $dx$, en $\lambda_m$, $\lambda_x$ gelijk voor alle activa.
:::

Het verwachte excess rendement is de marktbèta maal de marktpremie plus de
toestandsbèta maal de prijs van toestandsrisico. De index $m$ staat hier voor de
markt, zoals in [](#02-08-capm). Het bewijsidee: marktruiming zegt dat de som van
alle vragen [](#eq-merton-icapm-vraag) de markt is. Vermenigvuldig met
$\boldsymbol{\Sigma}$, en de verwachte excess rendementen blijken een combinatie
van twee covarianties: met de markt en met $dx$. Herschrijven naar bèta's geeft
[](#eq-merton-icapm-icapm).

:::{prf:proof}
:class: dropdown

Laat $M = \sum_k W_k$ en $\mathbf{w}_m$ de marktgewichten. Marktruiming zegt
$M\mathbf{w}_m = \sum_k W_k\mathbf{w}_k$. Vul [](#eq-merton-icapm-vraag) in en
vermenigvuldig met $\boldsymbol{\Sigma}$:

$$
M\,\boldsymbol{\Sigma}\mathbf{w}_m
= \Big(\textstyle\sum_k W_kT_k\Big)(\boldsymbol{\mu} - r\mathbf{1})
+ \Big(\textstyle\sum_k W_kH_k\Big)\boldsymbol{\sigma}_{Rx} .
$$

$\boldsymbol{\Sigma}\mathbf{w}_m$ is de vector van covarianties met het
marktrendement, $\boldsymbol{\sigma}_{Rm}$. Met de vermogensgewogen gemiddelden
$\bar{T} = \sum_kW_kT_k/M$ en $\bar{H} = \sum_kW_kH_k/M$ volgt

$$
\boldsymbol{\mu} - r\mathbf{1} = \frac{1}{\bar T}\,\boldsymbol{\sigma}_{Rm}
- \frac{\bar H}{\bar T}\,\boldsymbol{\sigma}_{Rx} .
$$

Met $\mathbf{F} = (dR_m, dx)'$ en $\mathbf{b} = (1/\bar T, -\bar H/\bar T)'$ is dat
$\boldsymbol{\mu} - r\mathbf{1} = \Cov(d\mathbf{R}, \mathbf{F}')\,\mathbf{b}$. Schrijf
$\Cov(d\mathbf{R}, \mathbf{F}') = \mathbf{B}\,\Var(\mathbf{F})$, met in de rijen van
$\mathbf{B}$ de meervoudige bèta's (niet te verwarren met $B(\tau)$ hieronder). Dan is
$\boldsymbol{\mu} - r\mathbf{1} = \mathbf{B}\boldsymbol{\lambda}$ met
$\boldsymbol{\lambda} = \Var(\mathbf{F})\,\mathbf{b}$, voor alle activa gelijk.
Toegepast op de markt ($\beta_{m,m} = 1$, $\beta_{m,x} = 0$) geeft dit
$\lambda_m = \mu_m - r$. $\square$
:::

De covariantiepremie $b_x = -\bar H/\bar T$ uit het bewijs heeft een vast teken. Laat een hogere $x$ betere
kansen betekenen en laat de beleggers $\gamma > 1$ hebben. Dan is $\bar H < 0$, en
krijgt een positieve covariantie met $dx$ een positieve premie. Een activum dat
stijgt wanneer de kansen verbeteren, levert vermogen wanneer het het minst nodig
is, en moet meer opleveren. Een activum dat stijgt wanneer de kansen verslechteren,
zoals het aandeel uit het toy-voorbeeld, is een verzekering en brengt minder op.
Dat was de derde voorspelling van de intuïtie. De prijs van risico $\lambda_x$
mengt $b_x$ met de covariantie tussen $dx$ en de markt, en bij $\rho < 0$ ligt haar
teken niet vast.

Merton nam de rente als toestandsvariabele en een lange obligatie als
hedgeportefeuille. In het algemeen zegt het ICAPM niet welke $x$ het zijn, alleen
dat variabelen die de beleggingskansen voorspellen beprijsde factoren leveren.
{cite:t}`Breeden1979` voegde alle toestandsvariabelen samen tot één, de
consumptiegroei. Of die ene factor de prijzen draagt, komt aan bod in
[](#03-12-consumptie-capm).

### Wat het voorspelt: een mean-reverting Sharpe-ratio

*Waarom zou dit waar zijn?* Stel dat de Sharpe-ratio van de markt terugkeert naar
haar gemiddelde. Na een slechte periode worden de kansen beter, maar niet voor
altijd. Hoe langer de horizon, hoe meer van die toekomstige kansen de belegger wil
indekken, tot de horizon ruim voorbij de terugkeertijd ligt. De hedgevraag stijgt
dus met de horizon en vlakt dan af.

Schrijf $\mu_t - r = \sigma\eta_t$, met $\eta_t$ de *Sharpe-ratio* (premie per
eenheid volatiliteit). Kim en Omberg schrijven $\lambda$, maar die letter is in
deze reeks een prijs van risico. Laat

```{math}
:label: eq-merton-icapm-ou
d\eta_t = \kappa(\theta - \eta_t)\,dt + \sigma_\eta\,dZ^{\eta}_t ,
\qquad dZ_t\,dZ^{\eta}_t = \rho\,dt .
```

De Sharpe-ratio keert met snelheid $\kappa$ terug naar haar gemiddelde $\theta$ en
schommelt met $\sigma_\eta$. Bij een jaarlijkse persistentie van 0,92 is
$\kappa = -\log 0{,}92 = 0{,}083$, een halfwaardetijd van $\log 2/0{,}083 \approx 8$
jaar. Met $\tau = T - t$ noteren we de resterende horizon.

:::{prf:theorem} Hedgevraag bij een mean-reverting Sharpe-ratio (Kim-Omberg 1996)
:label: thm-merton-icapm-kimomberg

Onder [](#eq-merton-icapm-prijs), [](#eq-merton-icapm-ou) en CRRA-nut over het
eindvermogen is

```{math}
:label: eq-merton-icapm-ko
w^{\ast}(\eta,\tau) = \frac{\eta}{\gamma\sigma}
+ \frac{\rho\,\sigma_\eta}{\gamma\,\sigma}\,\big[B(\tau) + C(\tau)\,\eta\big],
```

waarbij $B$ en $C$, met $B(0) = C(0) = 0$ en $\delta \equiv (1-\gamma)/\gamma$
($-0{,}8$ bij $\gamma = 5$), voldoen aan

```{math}
:label: eq-merton-icapm-riccati
\begin{aligned}
C'(\tau) &= \delta\,(1 + \rho\sigma_\eta C)^2 - 2\kappa C + \sigma_\eta^2 C^2 ,\\
B'(\tau) &= \delta\,\rho\sigma_\eta B\,(1 + \rho\sigma_\eta C) + \kappa\theta C - \kappa B + \sigma_\eta^2 BC .
\end{aligned}
```
:::

De eerste term van [](#eq-merton-icapm-ko) is de myopische vraag, de tweede de
hedgevraag. $B + C\eta$ meet hoe sterk de waarde van de toekomst meebeweegt met de
Sharpe-ratio. $B$ en $C$ volgen uit *Riccati-vergelijkingen* (kwadratisch in de
onbekende), die {cite:t}`KimOmberg1996` in gesloten vorm oplosten. Bij $\gamma = 1$
blijven $B$ en $C$ nul. Bij $\gamma > 1$ en $\theta > 0$ worden ze negatief, dus is
de hedgevraag positief zodra $\rho < 0$. Ze beginnen bij nul en groeien in absolute
waarde naar een grens: de hedgevraag groeit met de horizon en vlakt af.

:::{prf:proof}
:class: dropdown

Schrijf $J = g(\eta,\tau)W^{1-\gamma}/(1-\gamma)$. Met $x = \eta$,
$\mu - r = \sigma\eta$ en $\sigma_x = \sigma_\eta$ geeft
[](#thm-merton-icapm-hedging) $w^{\ast} = [\eta + (g_\eta/g)\rho\sigma_\eta]/(\gamma\sigma)$.
Vul $w^{\ast}$ in [](#eq-merton-icapm-hjb-x) in en deel door $W^{1-\gamma}g/(1-\gamma)$.
Probeer $g = \exp\{A(\tau) + B(\tau)\eta + \tfrac12 C(\tau)\eta^2\}$, zodat
$g_\eta/g = B + C\eta$. De vergelijking wordt een kwadratisch polynoom in $\eta$ dat
voor elke $\eta$ nul is. De coëfficiënten van $\eta^2$ en $\eta$ geven
[](#eq-merton-icapm-riccati), die van $\eta^0$ bepaalt $A$, dat niet in de
portefeuille voorkomt. De randvoorwaarde $J(W,T) = W^{1-\gamma}/(1-\gamma)$ geeft
$B(0) = C(0) = 0$.

Het teken: bij $\gamma > 1$ is $C'(0) = \delta < 0$, en in $C = 0$ is steeds
$C' = \delta < 0$, dus $C$ blijft negatief. Zolang $B = 0$ is $B' = \kappa\theta C < 0$,
dus ook $B$ wordt negatief en blijft dat. $\square$
:::

### Numerieke oplossing

We kalibreren
op een jaarlijks VAR (*vector autoregression*, een regressie van elke variabele op
de vertraagde waarden). Vanaf hier zijn kleine letters logs: $z_t$ is de log
dividendopbrengst min haar gemiddelde, en $\ell^{e}_{t+1}$ het log excess
rendement.

```{math}
:label: eq-merton-icapm-var
\ell^{e}_{t+1} = a + b\,z_t + \varepsilon_{1,t+1},
\qquad
z_{t+1} = \phi\,z_t + \varepsilon_{2,t+1},
\qquad
\Corr(\varepsilon_1,\varepsilon_2) = \rho .
```

Een hoge dividendopbrengst voorspelt een hoog rendement ($b > 0$), en een
koersstijging verlaagt de dividendopbrengst ($\rho < 0$). Dat is de structuur van
geval B. De illustratieve parameters liggen niet ver van de data:

| $a$ | $b$ | $\phi$ | $\SD(\varepsilon_1)$ | $\SD(\varepsilon_2)$ | $\rho$ | log risicovrije rente |
|---|---|---|---|---|---|---|
| 4,5% | 0,08 | 0,92 | 18% | 15% | −0,9 | 2% |

Om [](#thm-merton-icapm-kimomberg) te gebruiken, vertalen we naar continue tijd. Het
verwachte simpele excess rendement is het log-rendement plus $\tfrac12\sigma^2$ (want
$\E[e^{\ell}] = e^{\E[\ell] + \sigma^2/2}$ bij een normaal $\ell$),
dus $\eta_t = (a + bz_t + \tfrac12\sigma^2)/\sigma$ met $\sigma = \SD(\varepsilon_1)$.
Verder is $\kappa = -\log\phi$, $\sigma_z = \SD(\varepsilon_2)\sqrt{2\kappa/(1-\phi^2)}$
en $\sigma_\eta = b\,\sigma_z/\sigma$. Zo heeft het continue proces dezelfde stationaire
variantie als het jaarlijkse: $\sigma_z^2/(2\kappa) = \SD(\varepsilon_2)^2/(1-\phi^2)$. Met
de tabel is $\theta = (0{,}045 + 0{,}0162)/0{,}18 = 0{,}34$ en
$\sigma_\eta = 0{,}08 \cdot 0{,}156/0{,}18 = 0{,}069$. De cel lost [](#eq-merton-icapm-riccati) op met
Runge-Kutta van orde vier, voor vier waarden van $\gamma$.

```{code-cell} ipython3
def var_to_continuous(a, b, phi, s1, s2, rho):
    """Map the annual VAR (log excess return on demeaned log D/P) to Kim-Omberg inputs."""
    kappa = -np.log(phi)
    sigma_z = s2 * np.sqrt(2 * kappa / (1 - phi**2))
    return {"sigma": s1, "kappa": kappa, "theta": (a + 0.5 * s1**2) / s1,
            "sig_l": b * sigma_z / s1, "rho": rho}


def kim_omberg(gamma, horizons, sigma, kappa, theta, sig_l, rho, lam=None, dt=0.02):
    """Myopic and hedging demand from the Kim-Omberg Riccati system (RK4).

    Parameters are floats, or arrays of equal length with one entry per parameter
    set. Returns (myopic, hedge), one row per horizon, evaluated at the Sharpe
    ratio `lam` (default: the long-run mean theta).
    """
    lam = theta if lam is None else lam
    delta = (1 - gamma) / gamma
    B = np.zeros(np.shape(theta))   # one B and one C per parameter set
    C = np.zeros(np.shape(theta))

    def rhs(B, C):
        dB = (delta * rho * sig_l * B * (1 + rho * sig_l * C)
              + kappa * theta * C - kappa * B + sig_l**2 * B * C)
        dC = delta * (1 + rho * sig_l * C) ** 2 - 2 * kappa * C + sig_l**2 * C**2
        return dB, dC

    steps = np.rint(np.asarray(horizons) / dt).astype(int)
    out, step = [], 0
    for target in steps:
        while step < target:
            k1 = rhs(B, C)
            k2 = rhs(B + dt / 2 * k1[0], C + dt / 2 * k1[1])
            k3 = rhs(B + dt / 2 * k2[0], C + dt / 2 * k2[1])
            k4 = rhs(B + dt * k3[0], C + dt * k3[1])
            B = B + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            C = C + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            step += 1
        out.append(rho * sig_l * (B + C * lam) / (gamma * sigma))
    myopic = lam / (gamma * sigma)  # the same at every horizon
    return np.array([myopic] * len(out)), np.array(out)


illustrative = dict(a=0.045, b=0.08, phi=0.92, s1=0.18, s2=0.15, rho=-0.9)
ko_params = var_to_continuous(**illustrative)

horizons = [1, 5, 10, 20, 50]
rows = {}
for gamma in [1, 2, 5, 10]:
    myopic, hedge = kim_omberg(gamma, horizons, **ko_params)
    rows[f"gamma = {gamma}: myopische vraag"] = myopic
    rows[f"gamma = {gamma}: hedgevraag"] = hedge
pd.DataFrame(rows, index=[f"H = {h} jaar" for h in horizons]).T.round(3)
```

Bij $\gamma = 1$ is de hedgevraag op elke horizon nul, zoals onder de stelling vastgesteld. Bij
$\gamma = 5$ is de myopische vraag 0,378 en de hedgevraag op twintig jaar 0,339:
bijna een verdubbeling. Bij $\gamma = 10$ is de hedgevraag op vijftig jaar groter
dan de myopische vraag zelf. {cite:t}`CampbellViceira1999` vonden dezelfde orde
van grootte: de hedgevraag kan de vraag naar aandelen verdubbelen.

De hedgevraag van 0,339 bij $\gamma = 5$ op twintig jaar bepaalt ook hoe groot het
ICAPM-effect is. Houdt één representatieve
belegger de hele markt, dan zegt [](#eq-merton-icapm-vraag) met één activum
$1 = (\mu_m - r)/(\gamma\sigma^2) + h$, met $h$ de hedgefractie. Dus is
$\mu_m - r = \gamma\sigma^2(1 - h)$. Met $\gamma = 5$, $\sigma = 18\%$ en $h = 0{,}339$
is dat $0{,}162 \cdot 0{,}661 = 10{,}7\%$ in plaats van $16{,}2\%$, bij een vaste $h$.
Het verzekeringsmotief drukt de marktpremie dan met een derde.

Let in de figuur op de afstand tussen de getrokken en de gestreepte lijn van
dezelfde kleur. Dat de getrokken lijn stijgt, is de tweede voorspelling van de
intuïtie.

```{code-cell} ipython3
:label: cel-merton-icapm-horizon
:tags: [hide-input]

horizon_grid = np.arange(0.5, 50.01, 0.5)
fig, ax = plt.subplots()
for colour, gamma in zip(hap.plotting.COLORS, [2, 5, 10]):
    myopic, hedge = kim_omberg(gamma, horizon_grid, **ko_params)
    ax.plot(horizon_grid, myopic + hedge, color=colour, label=f"totaal, $\\gamma$ = {gamma}")
    ax.plot(horizon_grid, myopic, color=colour, ls="--", lw=1.1,
            label=f"myopisch, $\\gamma$ = {gamma}")
ax.set_xlabel("Horizon (jaren)")
ax.set_ylabel("Fractie van het vermogen in aandelen")
ax.set_title("Kim-Omberg: de hedgevraag groeit met de horizon")
ax.legend(ncol=3)
plt.show()
```

:::{figure} #cel-merton-icapm-horizon
:label: fig-merton-icapm-horizon
:width: 90%

Optimale aandelenfractie bij de gemiddelde Sharpe-ratio. De gestreepte lijnen zijn
de myopische vraag, die niet van de horizon afhangt. Het verschil met de getrokken
lijn is de hedgevraag. Die begint bij nul en groeit over de eerste twintig jaar
bijna rechtlijnig. Daarna vlakt zij af, maar op vijftig jaar ligt zij nog onder de
grens voor een oneindige horizon (oefening 2).
:::

Ter controle lossen we het jaarlijkse probleem ook direct op, zoals
{cite:t}`Barberis2000`, achterwaarts op een rooster van 21 punten voor $z$:

$$
q(z, k) = \max_{w\in[0,\,0{,}99]}\ \E\Big[\big(e^{r}(1 - w + w\,e^{\ell^{e}_{k+1}})\big)^{1-\gamma}\,q(z_{k+1}, k+1)\Big],
\qquad q(\cdot, K) = 1 .
$$

Dat is de recursie uit het bewijs van [](#thm-merton-icapm-samuelson) met een $q$ die van
de toestand afhangt.

```{code-cell} ipython3
def solve_rebalancing(gamma, n_years, draw, sd_z, rf=0.02, z0=(0.0,), n_grid=21, n_bisect=20):
    """Backward induction for an annually rebalancing CRRA investor.

    `draw(grid)` returns arrays (log excess return, next state), both of shape
    (n_grid, n_draws), conditional on each grid point. Returns the optimal
    stock share at the states `z0` for horizons 1, ..., n_years.
    """
    grid = np.linspace(-3 * sd_z, 3 * sd_z, n_grid)
    log_excess, z_next = draw(grid)
    gross_excess = np.exp(log_excess)
    Q, shares = np.ones(n_grid), []
    for _ in range(n_years):
        Q_next = np.interp(z_next, grid, Q)
        lo, hi = np.zeros(n_grid), np.full(n_grid, 0.99)
        for _ in range(n_bisect):
            mid = (lo + hi) / 2
            growth = 1 - mid[:, None] + mid[:, None] * gross_excess
            slope = (growth ** (-gamma) * (gross_excess - 1) * Q_next).mean(axis=1)
            lo, hi = np.where(slope > 0, mid, lo), np.where(slope > 0, hi, mid)
        w = (lo + hi) / 2
        growth = np.exp(rf) * (1 - w[:, None] + w[:, None] * gross_excess)
        Q = (growth ** (1 - gamma) * Q_next).mean(axis=1)
        shares.append(np.interp(z0, grid, w))
    return np.array(shares)


def normal_shocks(s1, s2, rho, n_draws):
    cov = np.array([[s1**2, rho * s1 * s2], [rho * s1 * s2, s2**2]])
    return rng.standard_normal((n_draws, 2)) @ np.linalg.cholesky(cov).T


p = illustrative
shocks = normal_shocks(p["s1"], p["s2"], p["rho"], 5000)
sd_z = p["s2"] / np.sqrt(1 - p["phi"] ** 2)
def known(grid):
    """Log excess returns and next states at each grid point, parameters known."""
    return (p["a"] + p["b"] * grid[:, None] + shocks[:, 0],
            p["phi"] * grid[:, None] + shocks[:, 1])


check_horizons = [1, 2, 5, 10, 20]
check = {}
for gamma in [5, 10]:
    grid_share = solve_rebalancing(gamma, 20, known, sd_z)[:, 0]
    myopic, hedge = kim_omberg(gamma, check_horizons, **ko_params)
    check[f"rooster, gamma = {gamma}"] = grid_share[np.array(check_horizons) - 1]
    check[f"Kim-Omberg, gamma = {gamma}"] = myopic + hedge
pd.DataFrame(check, index=[f"H = {h}" for h in check_horizons]).T.round(3)
```

Het grootste verschil tussen de twee methoden is 1,6 procentpunt, bij $\gamma = 10$
op twintig jaar. Bij $\gamma = 2$ bindt de grens van 0,99.

```{admonition} Samengevat
:class: tip

- Bij onafhankelijke rendementen is de aandelenfractie gelijk voor elke horizon,
  [](#thm-merton-icapm-samuelson).

- In continue tijd is die fractie $(\mu - r)/(\gamma\sigma^2)$, [](#eq-merton-icapm-merton):
  hoger bij een hogere premie, lager bij meer risicoaversie of volatiliteit.

- Bewegen de kansen, dan komt er een hedgevraag bij, [](#eq-merton-icapm-hedge),
  positief bij $\gamma > 1$ en $\rho < 0$, nul bij log-nut.

- In evenwicht beloont het verwachte rendement de marktbèta en de bèta op de
  toestandsvariabele, [](#eq-merton-icapm-icapm).

- De simulatie hierna vraagt hoe goed een eeuw data de hedgevraag meet.
```

## Simulatie: wat een eeuw data over de hedgevraag zegt

Alles hierboven veronderstelde dat de belegger $b$, $\phi$ en $\rho$ kent. Hoe goed meet hij zijn hedgevraag
met een eeuw jaarcijfers, als de voorspelbaarheid echt is? We trekken 1000 steekproeven van 100
jaar uit het illustratieve VAR en schatten telkens de parameters met OLS. Daarmee
rekenen we de hedgevraag uit voor $\gamma = 5$ en twintig jaar, alsof de schatting
de waarheid is.

```{code-cell} ipython3
# TODO: naar hap.stats
def ols_var(r_next, z):
    """OLS of the two-equation VAR; columns of the inputs are independent samples.

    z has length n (the state at t = 0, ..., n-1); r_next has length n-1 and
    r_next[t] is the return earned between t and t+1. Returns intercepts,
    slopes, residual std devs, residual correlation and the standard error of
    the return slope.
    """
    x, y1, y2 = z[:-1], r_next, z[1:]
    xd = x - x.mean(axis=0)
    sxx = (xd**2).sum(axis=0)
    b = (xd * (y1 - y1.mean(axis=0))).sum(axis=0) / sxx
    phi = (xd * (y2 - y2.mean(axis=0))).sum(axis=0) / sxx
    e1 = y1 - y1.mean(axis=0) - b * xd
    e2 = y2 - y2.mean(axis=0) - phi * xd
    n = len(x)
    s1, s2 = np.sqrt((e1**2).sum(axis=0) / (n - 2)), np.sqrt((e2**2).sum(axis=0) / (n - 2))
    rho = (e1 * e2).sum(axis=0) / ((n - 2) * s1 * s2)
    a = y1.mean(axis=0) - b * x.mean(axis=0)
    c = y2.mean(axis=0) - phi * x.mean(axis=0)
    return {"a": a, "b": b, "c": c, "phi": phi, "s1": s1, "s2": s2, "rho": rho,
            "se_b": s1 / np.sqrt(sxx)}
```

De steekproeven starten na 200 jaar aanloop, zodat $z$ uit zijn stationaire
verdeling begint.

```{code-cell} ipython3
n_samples, n_years, burn = 1000, 100, 200
z = np.zeros(n_samples)
z_path, r_path = [], []
for t in range(burn + n_years + 1):
    eps = normal_shocks(p["s1"], p["s2"], p["rho"], n_samples)
    r_next = p["a"] + p["b"] * z + eps[:, 0]
    if t >= burn:
        z_path.append(z)
        r_path.append(r_next)
    z = p["phi"] * z + eps[:, 1]
z_path, r_path = np.array(z_path), np.array(r_path)

est = ols_var(r_path[:-1], z_path)
est_cont = var_to_continuous(est["a"] + est["b"] * z_path[:-1].mean(axis=0), est["b"],
                             np.minimum(est["phi"], 0.995), est["s1"], est["s2"], est["rho"])
myopic_hat, hedge_hat = kim_omberg(5, [20], **est_cont)
myopic_true, hedge_true = kim_omberg(5, [20], **ko_params)
```

Elke steekproef levert nu een eigen hedgevraag op. De tabel vat de 1000 schattingen
samen.

```{code-cell} ipython3
pd.DataFrame(
    {
        "waarheid": [p["b"], p["phi"], float(hedge_true[0]), float(myopic_true[0])],
        "gemiddelde schatting": [est["b"].mean(), est["phi"].mean(),
                                 hedge_hat[0].mean(), myopic_hat[0].mean()],
        "5%-kwantiel": [np.quantile(est["b"], 0.05), np.quantile(est["phi"], 0.05),
                        np.quantile(hedge_hat[0], 0.05), np.quantile(myopic_hat[0], 0.05)],
        "95%-kwantiel": [np.quantile(est["b"], 0.95), np.quantile(est["phi"], 0.95),
                         np.quantile(hedge_hat[0], 0.95), np.quantile(myopic_hat[0], 0.95)],
    },
    index=["b", "phi", "hedgevraag (H = 20, gamma = 5)", "myopische vraag (gamma = 5)"],
).round(3)
```

De geschatte hedgevraag is zowel onzeker als vertekend. De ware waarde is 0,339,
maar in 90% van de steekproeven ligt de schatting ergens tussen 0,143 en 0,850.
Gemiddeld komt zij uit op 0,450, te hoog. De volgende cel telt hoe vaak de helling
significant is en hoe vaak de hedgevraag een verkeerd teken krijgt.

```{code-cell} ipython3
pd.Series({
    "fractie steekproeven met t(b) > 1,96": np.mean(est["b"] / est["se_b"] > 1.96),
    "fractie steekproeven met hedgevraag < 0": np.mean(hedge_hat[0] < 0),
}).round(3)
```

De helling is in maar 55,5% van de steekproeven significant, terwijl de
voorspelbaarheid per constructie echt is. Een negatieve hedgevraag komt vrijwel
niet voor. Het teken is dus goed te leren, de grootte niet. Let in de figuur op
waar de gestreepte lijn links ligt ten opzichte van de zwarte.

```{code-cell} ipython3
:label: cel-merton-icapm-steekproef
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
axes[0].hist(est["b"], bins=40, edgecolor="white")
axes[0].axvline(p["b"], color="black", lw=1.6, label="ware $b$")
axes[0].axvline(est["b"].mean(), color=hap.plotting.COLORS[1], ls="--", lw=1.6,
                label="gemiddelde schatting")
axes[0].set_xlabel("Geschatte $b$ (helling van rendement op log D/P)")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].set_title("Stambaugh-bias in 100 jaar data")
axes[0].legend()
axes[1].hist(hedge_hat[0], bins=40, edgecolor="white")
axes[1].axvline(float(hedge_true[0]), color="black", lw=1.6, label="ware hedgevraag")
axes[1].set_xlabel("Geschatte hedgevraag ($\\gamma$ = 5, horizon 20 jaar)")
axes[1].set_ylabel("Aantal steekproeven")
axes[1].set_title("Wat de belegger denkt dat hij moet indekken")
axes[1].legend()
plt.show()
```

:::{figure} #cel-merton-icapm-steekproef
:label: fig-merton-icapm-steekproef
:width: 100%

Links: de OLS-schatter van $b$ over 1000 steekproeven van 100 jaar. Het gemiddelde
ligt boven de ware 0,08. De schatter van $\phi$ valt te laag uit, en via de sterk
negatieve correlatie tussen de schokken duwt die fout $\hat b$ omhoog: de bias van
{cite:t}`Stambaugh1999`. Rechts: de hedgevraag die een belegger uit zijn eigen
steekproef afleidt, van minder dan de helft tot tweeënhalf keer de ware waarde.
:::

Dit is [de standaardfout van 2%](#00-01-rendementen) in dynamische vorm. De
spreiding komt van de grootheden die over verwachte rendementen gaan: $\hat b$ voor
de hedgevraag en $\hat a$ voor de myopische vraag. Volatiliteiten en $\rho$ zijn over
een eeuw goed bepaald.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Nicholas Barberis, *Investing for the Long Run when Returns Are
Predictable*, Journal of Finance 2000 {cite}`Barberis2000`; John Campbell en Luis
Viceira, Quarterly Journal of Economics 1999 {cite}`CampbellViceira1999`.

**Wat.** (1) Barberis' tabel II: het maandelijkse VAR van het log excess rendement
op de dividendopbrengst, 1952–1995. (2) De conclusie van Campbell en Viceira dat
de hedgevraag de vraag naar aandelen fors verhoogt, tot een verdubbeling, en
(3) die van Barberis dat parameteronzekerheid de allocatie op lange horizons drukt.

**Data hier.** Goyal-Welch via `hap.data.goyal_welch`: maandelijks voor (1),
jaarlijks 1927–2025 voor (2) en (3).

**Verschil met het origineel.** Barberis gebruikt de NYSE-index, Goyal-Welch de
S&P 500, beide van CRSP. Campbell en Viceira gebruiken Epstein-Zin-nut met
consumptie, Barberis maanddata tot tien jaar, wij CRRA-nut over het eindvermogen en
jaardata tot twintig jaar.

**Verwachte afwijking.** (1) Een positieve helling binnen één standaardfout van
0,51, $\phi$ rond 0,98 en een correlatie tussen −0,9 en −1. Een negatieve helling
of een positieve correlatie is een fout in de code. (2)–(3) Een positieve
hedgevraag die met de horizon groeit, kleiner dan een verdubbeling omdat de
helling over de hele eeuw zwakker is dan over 1952–1995, en met parameteronzekerheid een lagere
allocatie op elke horizon.
```

### Barberis' VAR

We schatten het maandelijkse VAR met OLS. Met de vlakke prior van Barberis valt het
posterior gemiddelde samen met OLS, zodat de twee kolommen vergelijkbaar zijn.

```{code-cell} ipython3
gw_monthly = hap_data.goyal_welch("monthly")
monthly = pd.DataFrame(
    {
        "excess": np.log1p(gw_monthly["CRSP_SPvw"]) - np.log1p(gw_monthly["Rfree"]),
        "dy": gw_monthly["D12"] / gw_monthly["Index"],
    }
).loc["1952-06":"1995-12"]

# z[t] is the dividend yield at the end of month t, r_next[t] the return over month t+1
mon = ols_var(monthly["excess"].to_numpy()[1:, None], monthly["dy"].to_numpy()[:, None])
mon = {k: float(v[0]) for k, v in mon.items()}
dy_lag = monthly["dy"].to_numpy()[:-1]
se_phi = mon["s2"] / np.sqrt(((dy_lag - dy_lag.mean()) ** 2).sum())

pd.DataFrame(
    {
        "Barberis (2000), tabel II": [0.5118, 0.2129, 0.9774, 0.0091, 0.0017, -0.9351],
        "hier (OLS)": [mon["b"], mon["se_b"], mon["phi"], se_phi, mon["s1"] ** 2, mon["rho"]],
    },
    index=["helling rendement op D/P", "  standaardfout", "phi (D/P op D/P)", "  standaardfout",
           "residuvariantie rendement", "correlatie schokken"],
).round(4)
```

**Geslaagd.** Alle tekens en ordes van grootte kloppen, zoals de verwachte
afwijking eiste. Onze helling ligt $(0{,}5118 - 0{,}4058)/0{,}2129 = 0{,}5$
standaardfout onder die van Barberis, bij een andere index. Ook in zijn eigen
steekproef is de $t$-waarde van de helling maar $0{,}5118/0{,}2129 = 2{,}4$.

### Horizonallocaties op een eeuw jaarcijfers

Nu schatten we het jaarlijkse VAR over 1927–2025, de invoer voor de horizonallocaties.

```{code-cell} ipython3
gw_annual = hap_data.goyal_welch("annual").loc["1926":"2025"]
log_dp = gw_annual["dp"].to_numpy()
excess_next = (np.log1p(gw_annual["CRSP_SPvw"]) - np.log1p(gw_annual["Rfree"])).to_numpy()[1:]
dp_mean = log_dp[:-1].mean()
z_annual = log_dp - dp_mean

ann = ols_var(excess_next[:, None], z_annual[:, None])
ann = {k: float(v[0]) for k, v in ann.items()}
rf_annual = float(np.log1p(gw_annual["Rfree"]).mean())
ann_cont = var_to_continuous(ann["a"], ann["b"], ann["phi"], ann["s1"], ann["s2"], ann["rho"])

pd.DataFrame(
    {"schatting": [ann["a"], ann["b"], ann["se_b"], ann["b"] / ann["se_b"], ann["phi"],
                   ann["s1"], ann["s2"], ann["rho"], rf_annual, z_annual[-1]]},
    index=["a (gem. log excess rendement)", "b", "  standaardfout", "  t-waarde", "phi",
           "sd rendementsschok", "sd D/P-schok", "correlatie schokken",
           "gem. log risicovrije rente", "log D/P eind 2025 min gemiddelde"],
).round(4)
```

Over de hele eeuw voorspelt de dividendopbrengst zwak: de helling heeft een
$t$-waarde van 1,07. De persistentie (0,924) en de negatieve correlatie tussen de
schokken (−0,856) zijn er nog wel. Zoals in de simulatie zijn de tweede momenten
goed bepaald, en het verwachte rendement niet. Deze schattingen gaan in Kim-Omberg,
voor drie risicoaversies.

```{code-cell} ipython3
horizons = [1, 5, 10, 20, 50]
cv_table = {}
for gamma in [2, 5, 10]:
    myopic, hedge = kim_omberg(gamma, horizons, **ann_cont)
    cv_table[(f"gamma = {gamma}", "myopische vraag")] = myopic
    cv_table[(f"gamma = {gamma}", "hedgevraag")] = hedge
    cv_table[(f"gamma = {gamma}", "totaal / myopisch")] = (myopic + hedge) / myopic
pd.DataFrame(cv_table, index=[f"H = {h}" for h in horizons]).T.round(3)
```

De volgende tabel zet de verhouding totaal/myopisch naast de verdubbeling van
Campbell en Viceira.

```{code-cell} ipython3
pd.DataFrame(
    {"origineel (Campbell-Viceira)": ["tot 2"],
     "hier": [cv_table[("gamma = 10", "totaal / myopisch")][4]]},
    index=["totaal / myopisch, gamma = 10, H = 50"],
).round(3)
```

**Geslaagd.** De hedgevraag is positief en groeit met de horizon, en blijft bij
realistische horizons onder de verdubbeling, zoals de verwachte afwijking zei. De
verdubbeling komt pas bij vijftig jaar en $\gamma = 10$ in zicht.

Dat een zo zwakke helling toch zo'n hedgevraag geeft, komt van twee dingen: de
correlatie van $-0{,}86$ en een halfwaardetijd van
$\log 2/(-\log 0{,}924) \approx 8{,}8$ jaar. Een klein maar persistent effect telt
op over een lange horizon.

### Parameteronzekerheid volgens Barberis

{cite:t}`Barberis2000` liet de belegger het verwachte nut middelen over de
posterior verdeling van alle parameters, in plaats van de puntschatting te
gebruiken. Met een vlakke prior is de posterior standaard. De covariantiematrix
van de schokken is *invers-Wishart* (de verdeling van de inverse van een
steekproefcovariantiematrix), en de coëfficiënten zijn normaal rond de
OLS-schatting. Per trekking is de coëfficiëntenmatrix $\hat{\mathbf C} + \mathbf L_X\mathbf Z\mathbf L_\Sigma'$,
met $\mathbf Z$ standaardnormaal en $\mathbf L$ de Cholesky-factoren. We trekken 5000
parametersets met elk één schok. Zoals bij Barberis
leert de belegger later niets bij.

```{code-cell} ipython3
def posterior_predictive(r_next, z, n_draws):
    """Draws of (a, b, c, phi) and one VAR shock per draw under a flat prior (Barberis 2000)."""
    X = np.column_stack([np.ones(len(z) - 1), z[:-1]])
    Y = np.column_stack([r_next, z[1:]])
    C_hat = np.linalg.solve(X.T @ X, X.T @ Y)
    resid = Y - X @ C_hat
    Sigma = stats.invwishart(df=len(Y) - 3, scale=resid.T @ resid).rvs(n_draws, random_state=rng)
    L_sigma = np.linalg.cholesky(Sigma)
    L_x = np.linalg.cholesky(np.linalg.inv(X.T @ X))
    Z = rng.standard_normal((n_draws, 2, 2))
    L_sigma_t = np.transpose(L_sigma, axes=(0, 2, 1))  # L_Sigma' for each draw
    C = C_hat + L_x @ Z @ L_sigma_t                    # matrix-normal around OLS
    e = rng.standard_normal((n_draws, 2))
    eps = (L_sigma @ e[:, :, None])[:, :, 0]          # one VAR shock per draw
    return C, eps


C_draws, eps_draws = posterior_predictive(excess_next, z_annual, 5000)
pd.DataFrame(
    {"gemiddelde": [C_draws[:, 1, 0].mean(), C_draws[:, 1, 1].mean()],
     "standaarddeviatie": [C_draws[:, 1, 0].std(), C_draws[:, 1, 1].std()],
     "kans < 0": [np.mean(C_draws[:, 1, 0] < 0), np.mean(C_draws[:, 1, 1] < 0)],
     "kans > 1": [np.mean(C_draws[:, 1, 0] > 1), np.mean(C_draws[:, 1, 1] > 1)]},
    index=["b (posterior)", "phi (posterior)"],
).round(3)
```

De posterior van $b$ is even breed als haar gemiddelde. In 14,1% van de trekkingen
is de helling negatief, en voorspelt een hoge dividendopbrengst dus lage
rendementen. In 4,2% is $\phi > 1$, en keert de dividendopbrengst niet terug. De volgende cel lost
het probleem op met de parameters vast en met de posterior, vanaf een gemiddelde
dividendopbrengst en vanaf die van eind 2025.

```{code-cell} ipython3
shocks_ann = normal_shocks(ann["s1"], ann["s2"], ann["rho"], 5000)
sd_z_ann = ann["s2"] / np.sqrt(1 - ann["phi"] ** 2)
start_states = (0.0, z_annual[-1])

def point(grid):
    """Draws with the VAR parameters fixed at their OLS estimates."""
    return (ann["a"] + ann["b"] * grid[:, None] + shocks_ann[:, 0],
            ann["c"] + ann["phi"] * grid[:, None] + shocks_ann[:, 1])


def predictive(grid):
    """Draws from the posterior predictive: one parameter set and one shock per draw."""
    return (C_draws[:, 0, 0] + C_draws[:, 1, 0] * grid[:, None] + eps_draws[:, 0],
            C_draws[:, 0, 1] + C_draws[:, 1, 1] * grid[:, None] + eps_draws[:, 1])


share_point = solve_rebalancing(5, 20, point, sd_z_ann, rf=rf_annual, z0=start_states)
share_bayes = solve_rebalancing(5, 20, predictive, sd_z_ann, rf=rf_annual, z0=start_states)

show = np.array([1, 2, 5, 10, 15, 20])
pd.DataFrame(
    {
        ("D/P op gemiddelde", "parameters bekend"): share_point[show - 1, 0],
        ("D/P op gemiddelde", "parameteronzekerheid"): share_bayes[show - 1, 0],
        ("D/P zoals eind 2025", "parameters bekend"): share_point[show - 1, 1],
        ("D/P zoals eind 2025", "parameteronzekerheid"): share_bayes[show - 1, 1],
    },
    index=[f"H = {h}" for h in show],
).round(3)
```

Met parameteronzekerheid ligt de allocatie op elke horizon lager. De figuur zet de
vier kolommen uit. Let op de afstand tussen de getrokken en de gestreepte lijn van
dezelfde kleur.

```{code-cell} ipython3
:label: cel-merton-icapm-barberis
:tags: [hide-input]

years = np.arange(1, 21)
fig, ax = plt.subplots()
for j, (label, colour) in enumerate([("D/P op gemiddelde", hap.plotting.COLORS[0]),
                                     ("D/P zoals eind 2025", hap.plotting.COLORS[1])]):
    ax.plot(years, share_point[:, j], color=colour, label=f"{label}, parameters bekend")
    ax.plot(years, share_bayes[:, j], color=colour, ls="--",
            label=f"{label}, parameteronzekerheid")
ax.set_xlabel("Horizon (jaren), jaarlijkse herbalancering")
ax.set_ylabel("Fractie van het vermogen in aandelen")
ax.set_title("Horizonallocaties, $\\gamma$ = 5, VAR op 1927–2025")
ax.legend()
plt.show()
```

:::{figure} #cel-merton-icapm-barberis
:label: fig-merton-icapm-barberis
:width: 90%

Optimale aandelenfractie bij jaarlijkse herbalancering, met de parameters vast
(getrokken) of met de posterior verdeling (gestreept), vanaf een gemiddelde
dividendopbrengst (blauw) of vanaf de lage dividendopbrengst van eind 2025 (rood).
In alle vier de gevallen stijgt de lijn met de horizon. Parameteronzekerheid
verlaagt de allocatie en haalt een klein deel van de stijging weg.
:::

De eerste tabel vat de verschillen per beginstand samen, over alle twintig horizons.

```{code-cell} ipython3
gap = share_point - share_bayes  # parameters fixed minus parameter uncertainty
pd.DataFrame(
    {"kleinste verschil": gap.min(axis=0), "grootste verschil": gap.max(axis=0),
     "fractie H = 1, parameters bekend": share_point[0],
     "D/P in standaardafwijkingen": [0.0, z_annual[-1] / sd_z_ann]},
    index=["D/P op gemiddelde", "D/P zoals eind 2025"],
).round(3)
```

Met parameteronzekerheid ligt de allocatie op elke horizon lager: vanaf een
gemiddelde dividendopbrengst twee à drie procentpunt, vanaf eind 2025 ruim één à
twee. De tweede tabel zet de overallocatie op tien jaar naast die van Barberis.

```{code-cell} ipython3
pd.DataFrame(
    {"origineel (Barberis)": ["> 30%"],
     "hier": [share_point[9, 0] / share_bayes[9, 0] - 1]},
    index=["H = 10: overallocatie zonder onzekerheid (relatief)"],
).round(3)
```

**Gedeeltelijk geslaagd.** Teken en ordening zijn zoals verwacht. Maar de veel
vlakkere lijnen van Barberis zien we niet, en zijn overallocatie van meer dan
dertig procent voor een koop-en-houdbelegger met risicoaversie 10
({cite:t}`Barberis2000`, p. 246) is hier 4,5%. Die 4,5% geldt voor $\gamma = 5$
met jaarlijkse herbalancering, dus de vergelijking geeft alleen een orde van
grootte.

Het verschil is zelf [de standaardfout van 2%](#00-01-rendementen). Barberis' dynamische figuur 5
gebruikt de tienjaarssteekproef 1986–1995, en zijn koop-en-houdgetal komt uit 44
jaar maanddata. Wij hebben honderd jaar, en daarmee een smallere posterior. In
oefening 3 is het effect op dertig jaar data wel groot.

Vanaf de lage dividendopbrengst van eind 2025, bijna twee standaardafwijkingen
onder het gemiddelde, is de allocatie op één jaar ongeveer half zo groot.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Merton maakte van portefeuillekeuze een dynamisch
probleem en van asset pricing een theorie met meer dan één bron van risico. Uit
[](#thm-merton-icapm-samuelson) volgt dat jong zijn op zich geen reden is voor meer
aandelen. Uit [](#thm-merton-icapm-hedging) volgt wat wel een reden is: het indekken
van veranderende beleggingskansen. Het ICAPM gaf elk
later meerfactormodel een theoretische grond: een factor is beprijsd als hij
de beleggingskansen voorspelt.

**Waar het breekt.** Niet in de wiskunde, maar in de invoer. De hedgevraag hangt
aan de helling van het rendement op een voorspeller, een uitspraak over een
verwacht rendement. Over 1927–2025 heeft die helling een $t$-waarde van 1,07, en
toch zegt de theorie dat een belegger met $\gamma = 5$ op twintig jaar 0,223 extra
in aandelen houdt. De simulatie liet zien hoe ver een eeuw data ernaast kan zitten.
Een verwacht rendement is alleen te leren uit een lange kalenderperiode, hoe vaak
er ook gemeten wordt {cite}`Merton1980`. Daarnaast noemt het ICAPM zijn
toestandsvariabelen niet, en een model dat elke voorspeller als factor toelaat, is
moeilijk te verwerpen.

**Risico of vergissing?** Dat de dividendopbrengst rendementen voorspelt, draagt de
hele hedgevraag, en het feit laat twee lezingen toe. De Chicago-lezing (de prijs is
juist en beloont risico): de prijs van risico varieert. Na een crash zijn beleggers armer en risicomijdender en eisen
ze een hogere premie. De langetermijnbelegger die dan bijkoopt, draagt beprijsd
risico, en zijn hedgevraag is Mertons verzekering. De Yale-lezing (de prijs zit
ernaast): prijzen schieten door, en de dividendopbrengst voorspelt omdat de vergissing zich herstelt. Dan is
dezelfde extra positie een weddenschap dat de belegger meer weet dan de prijs. Het
VAR scheidt de twee niet, want beide geven $b > 0$ en $\rho < 0$. Scheiden vraagt of
verwachte rendementen meebewegen met consumptie en recessies, en de data van deze
lecture beslissen dat niet.

**Wat er daarna kwam.** Merton liet open welke factoren het zijn. Ross liet in 1976
zien dat een factormodel ook zonder voorkeuren volgt, alleen uit de afwezigheid van
arbitrage: zie [](#03-11-apt-no-arbitrage).

## Oefeningen

:::{exercise}
:label: ex-merton-icapm-1

**Instap: het toy-voorbeeld met een andere risicoaversie.** Neem geval B van het
toy-voorbeeld.

1. Laat met de hand zien dat bij log-nut ($\gamma = 1$) de myopische fractie
   1,7361 is, dat $q = 1$ in beide toestanden, en dat de hedgevraag nul is.
2. Bereken met `toy_table` de hedgevraag (w0 in geval B min de myopische fractie) voor $\gamma \in \{0{,}5;\ 2;\ 5;\ 10\}$.
   Voor welke $\gamma$ is zij negatief, en waarom?
:::

:::{solution} ex-merton-icapm-1
:class: dropdown

**(1)** De voorwaarde $0{,}36/(1+0{,}36w) = 0{,}16/(1-0{,}16w)$ geeft
$0{,}20 = 0{,}1152\,w$, dus $w = 1{,}7361$. Bij $\gamma = 1$ is
$q = \E[(1+wR^{e})^{0}] = 1$ in elke toestand, dus valt $q$ weg en is $w_0$ gelijk
aan de myopische fractie.

**(2)**

```{code-cell} ipython3
records = []
for gamma in [0.5, 1.0, 2.0, 5.0, 10.0]:
    row = toy_table(gamma)
    records.append({
        "gamma": gamma,
        "myopisch": row["myopisch (een periode)"],
        "w0 voorspelbaar": row["B: stijging -> duur"],
        "hedgevraag": row["B: stijging -> duur"] - row["myopisch (een periode)"],
        "hedge / myopisch": row["B: stijging -> duur"] / row["myopisch (een periode)"] - 1,
        "q goedkoop": row["q goedkoop"],
        "q duur": row["q duur"],
    })
pd.DataFrame(records).set_index("gamma").round(4)
```

Bij $\gamma = 0{,}5$ is de hedgevraag negatief. Dan is $1 - \gamma > 0$, en betekent
een betere toekomst een hogere $q$: $q_{\text{goedkoop}} = 1{,}0833 > 1 = q_{\text{duur}}$.
Het marginale nut van vermogen is dan het hoogst in de goedkope toestand. Het
aandeel levert daar weinig, dus houdt de belegger minder. Bij $\gamma > 1$ is het
teken positief, en relatief tot de myopische vraag groeit de hedgevraag met
$\gamma$. Wat dit leert: de hedgevraag is geen eigenschap van het activum alleen,
maar van het activum samen met hoe de belegger zijn toekomst weegt.
:::

:::{exercise}
:label: ex-merton-icapm-2

**Afleiding: de lange horizon in gesloten vorm.** Neem [](#eq-merton-icapm-riccati).

1. Laat zien dat de stationaire waarde $C_\infty = \lim_{\tau\to\infty} C(\tau)$ een
   wortel is van
   $\sigma_\eta^2(1 + \delta\rho^2)\,C^2 + 2(\delta\rho\sigma_\eta - \kappa)\,C + \delta = 0$,
   en leid $B_\infty$ af in termen van $C_\infty$.
2. Welke wortel is de limiet voor $\gamma > 1$?
3. Bereken de hedgevraag op oneindige horizon voor de illustratieve parameters en
   $\gamma = 5$, en vergelijk met Runge-Kutta bij $\tau = 200$ jaar.
:::

:::{solution} ex-merton-icapm-2
:class: dropdown

**(1)** Stel $C' = 0$ en groepeer naar machten van $C$. Stel $B' = 0$ en los op:

$$
B_\infty = \frac{\kappa\theta C_\infty}{\kappa - \sigma_\eta^2 C_\infty - \delta\rho\sigma_\eta(1 + \rho\sigma_\eta C_\infty)} .
$$

**(2)** Bij $\gamma > 1$ is $\delta < 0$, dus het product van de wortels is negatief
zolang $1 + \delta\rho^2 > 0$. Er is één negatieve en één positieve wortel. $C$
begint in nul en blijft negatief, dus de limiet is de negatieve wortel.

**(3)**

```{code-cell} ipython3
gamma = 5
delta = (1 - gamma) / gamma
kp = ko_params
quad_a = kp["sig_l"] ** 2 * (1 + delta * kp["rho"] ** 2)
quad_b = 2 * (delta * kp["rho"] * kp["sig_l"] - kp["kappa"])
C_inf = (-quad_b - np.sqrt(quad_b**2 - 4 * quad_a * delta)) / (2 * quad_a)
B_inf = kp["kappa"] * kp["theta"] * C_inf / (
    kp["kappa"] - kp["sig_l"] ** 2 * C_inf
    - delta * kp["rho"] * kp["sig_l"] * (1 + kp["rho"] * kp["sig_l"] * C_inf))
hedge_inf = kp["rho"] * kp["sig_l"] * (B_inf + C_inf * kp["theta"]) / (gamma * kp["sigma"])
myopic_200, hedge_200 = kim_omberg(gamma, [200], **kp)

pd.DataFrame(
    {"waarde": [C_inf, B_inf, hedge_inf, float(hedge_200[0]), float(myopic_200[0])]},
    index=["C oneindig", "B oneindig", "hedgevraag, oneindige horizon",
           "hedgevraag, Runge-Kutta bij 200 jaar", "myopische vraag"],
).round(4)
```

Op oneindige horizon is de
hedgevraag groter dan de myopische vraag. Wat dit leert: het horizoneffect is
begrensd, en de grens hangt aan $\theta$ en $\sigma_\eta$, twee grootheden over
verwachte rendementen.
:::

:::{exercise}
:label: ex-merton-icapm-3

**Uitbreiding van de replicatie: een kortere steekproef.** Herhaal de replicatie op
de jaarlijkse Goyal-Welch-data met rendementen over 1996–2025, met $\gamma = 10$ (bij
$\gamma = 5$ loopt de allocatie hier tegen de grens van 0,99).

1. Schat het VAR en rapporteer $\hat b$, zijn $t$-waarde en $\hat\phi$.
2. Bereken de aandelenfractie bij een gemiddelde dividendopbrengst op 1, 5 en 10
   jaar, met parameters vast en met parameteronzekerheid, voor deze steekproef en
   voor 1927–2025.
:::

:::{solution} ex-merton-icapm-3
:class: dropdown

```{code-cell} ipython3
recent = hap_data.goyal_welch("annual").loc["1995":"2025"]
dp_recent = recent["dp"].to_numpy()
z_recent = dp_recent - dp_recent[:-1].mean()
excess_recent = (np.log1p(recent["CRSP_SPvw"]) - np.log1p(recent["Rfree"])).to_numpy()[1:]

rec = {k: float(v[0]) for k, v in ols_var(excess_recent[:, None], z_recent[:, None]).items()}
shocks_rec = normal_shocks(rec["s1"], rec["s2"], rec["rho"], 5000)
sd_z_rec = rec["s2"] / np.sqrt(1 - min(rec["phi"], 0.995) ** 2)
rf_recent = float(np.log1p(recent["Rfree"]).mean())

def point_rec(grid):
    return (rec["a"] + rec["b"] * grid[:, None] + shocks_rec[:, 0],
            rec["c"] + rec["phi"] * grid[:, None] + shocks_rec[:, 1])


C_rec, eps_rec = posterior_predictive(excess_recent, z_recent, 5000)

def bayes_rec(grid):
    return (C_rec[:, 0, 0] + C_rec[:, 1, 0] * grid[:, None] + eps_rec[:, 0],
            C_rec[:, 0, 1] + C_rec[:, 1, 1] * grid[:, None] + eps_rec[:, 1])


h = np.array([1, 5, 10])
short = {
    "1996-2025, parameters bekend": solve_rebalancing(10, 10, point_rec, sd_z_rec, rf=rf_recent)[h - 1, 0],
    "1996-2025, parameteronzekerheid": solve_rebalancing(10, 10, bayes_rec, sd_z_rec, rf=rf_recent)[h - 1, 0],
    "1927-2025, parameters bekend": solve_rebalancing(10, 10, point, sd_z_ann, rf=rf_annual)[h - 1, 0],
    "1927-2025, parameteronzekerheid": solve_rebalancing(10, 10, predictive, sd_z_ann, rf=rf_annual)[h - 1, 0],
}
print(f"1996-2025: b = {rec['b']:.3f}, t = {rec['b'] / rec['se_b']:.2f}, phi = {rec['phi']:.3f}")
pd.DataFrame(short, index=[f"H = {k}" for k in h]).T.round(3)
```

De laatste dertig jaar lijken voorspelbaarder: $\hat b = 0{,}358$ met een $t$-waarde
van 2,60, maar een veel minder persistente dividendopbrengst ($\hat\phi = 0{,}647$). Dat spreekt de verwachte
afwijking niet tegen, want die ging over de helling over de hele eeuw. Bij tien jaar
bindt voor de belegger met de puntschatting de grens van 0,99.

Op vijf jaar houdt de belegger met parameteronzekerheid zeventien procentpunt minder
dan wie de puntschatting gelooft (0,649 tegen 0,817). Op de eeuwsteekproef is dat
verschil ruim één procentpunt, want met honderd observaties is de posterior veel
smaller. Wat dit leert: hoe korter de geschiedenis, hoe meer van het horizoneffect een
illusie van de puntschatting is.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
