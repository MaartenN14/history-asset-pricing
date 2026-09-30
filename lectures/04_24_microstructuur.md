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

(04-24-microstructuur)=

# Kyle, Glosten-Milgrom en liquiditeit
```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1984–2015. Het college loopt van Rolls impliciete spread en de modellen van
Kyle en van Glosten en Milgrom tot de liquiditeitsfactoren en de race om snelheid in de hoogfrequente
handel.

**Wat we al weten.** In [](#02-06-efficiente-markten) zagen we dat een prijs die alle
informatie bevat geen evenwicht kan zijn als informatie geld kost, de paradox van
Grossman en Stiglitz. [](#04-23-behavioral) liet zien dat noise traders prijzen van hun
waarde kunnen wegduwen en dat arbitrage daar grenzen aan heeft. Wat nog ontbrak, was een
model van het handelsmechanisme zelf, dat zegt wie de prijs zet en wat die weet over de
handelaar aan de andere kant.

**Welke vraag staat open.** Hoe komt private informatie via de handel in de prijs, en
krijgen beleggers een hoger verwacht rendement voor de kosten van handelen tegen iemand
die meer weet?
```

## Overzicht

Dit college vraagt hoe private informatie via de handel in de prijs komt, en of
beleggers betaald krijgen voor de kosten die dat meebrengt. Een market maker die weet
dat een deel van zijn klanten meer weet, moet een spread en een prijsimpact rekenen,
zodat de prijs de informatie geleidelijk opneemt. Illiquiditeit gaat samen met hogere
verwachte en lagere gelijktijdige rendementen, maar de premie op liquiditeitsrisico is
na publicatie niet meer te zien.

- We leiden de spread van Glosten en Milgrom af en het evenwicht van Kyle, met één en met
  vele handelsronden.
- We vertalen die theorie met de maten van Roll en Amihud naar dagkoersen, en volgen hoe
  liquiditeit als niveau en als risico in verwachte rendementen komt.
- We simuleren hoe vaak de Roll-maat in een kwartaal of een jaar niet te berekenen is.
- We repliceren op vijftig grote Amerikaanse aandelen dat illiquiditeit piekt in 2008 en
  maart 2020 en samengaat met lage marktrendementen {cite}`Amihud2002`, en op de reeks van
  Pástor en Stambaugh dat liquiditeit in crisismaanden instort.

Tot het midden van de jaren tachtig was de prijs in de theorie een getal dat "de markt"
zette, zonder bied- of laatkoers en zonder een handelaar die hem noteerde. Glosten en
Milgrom
{cite}`GlostenMilgrom1985` lieten in 1985 zien dat een concurrerende *market maker* (een
handelaar die altijd bereid is te kopen en te verkopen) toch een spread moet rekenen. De
reden is dat een deel van zijn tegenpartijen beter geïnformeerd is. Kyle {cite}`Kyle1985`
liet in
hetzelfde jaar zien hoe een insider zijn informatie verstopt achter ongeïnformeerde
*order flow* (de som van alle koop- en verkooporders). Beide modellen zijn theorieën met
toetsbare voorspellingen, maar de empirie die volgde, van Roll {cite}`Roll1984b` tot
Pástor en
Stambaugh {cite}`PastorStambaugh2003`, maakte van liquiditeit een risicofactor en daarmee
een feit dat nog op een verklaring wacht. Santa-Clara zet dat feit in zijn lijst van wat we
weten zo neer {cite}`SantaClara2026`:

> Liquidity is priced, and it disappears when you need it.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een handelaar die iedereen bedient die wil kopen of verkopen. De meeste klanten
handelen om redenen die niets met de waarde van het aandeel te maken hebben, zoals een
pensioenfonds dat geld nodig heeft. Een klein deel weet iets, en de handelaar kan de
groepen niet uit elkaar houden. Verkoopt hij aan elke koper tegen de gemiddelde waarde,
dan verliest hij stelselmatig aan de geïnformeerde kopers, want die kopen juist als het
aandeel meer waard is.

Hij verkoopt daarom tegen de waarde gegeven dat iemand wil kopen, en koopt tegen de
waarde gegeven dat iemand wil verkopen. Het verschil is geen winstmarge, maar een premie
die de ongeïnformeerde klanten betalen voor wat de handelaar aan de geïnformeerde
verliest. Na een reeks kooporders gelooft hij in goed nieuws, zodat zijn koersen omhoog
schuiven en de spread kleiner wordt naarmate hij zekerder is.

Kyle voegde de strategie van de insider toe. Een insider die de waarde kent, wil veel
kopen, maar elke extra order drijft de koers op en verraadt hem. Hij verstopt zijn orders
daarom tussen die van de ongeïnformeerde handelaren, en hoe meer ruis er is, hoe meer hij
kan kopen zonder op te vallen. Zijn winst komt uit de zak van de ongeïnformeerde
handelaren.

Als handelen zo geld kost, vragen beleggers voor illiquide aandelen een hoger rendement.
Liquiditeit verdwijnt bovendien voor iedereen tegelijk, zoals in 1987, bij de val van
LTCM in 1998 ([](#04-22-risk-management)), in 2008 en in maart 2020, en dus precies
wanneer beleggers moeten verkopen. We verwachten daarom dat de spread het grootst is bij
de grootste onzekerheid en met elke order krimpt. Verder verwachten we dat illiquide
aandelen gemiddeld meer opleveren en dat koersen dalen in een maand waarin de liquiditeit
onverwacht opdroogt.

## Toy-voorbeeld: één market maker, één order, één insider

De eerste codecel laadt de pakketten die het hele college gebruikt.

```{code-cell} ipython3
import io

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from scipy import stats

import hap
from hap import cache as hap_cache
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

### Glosten-Milgrom met één transactie

| grootheid | waarde |
|---|---|
| waarde van het aandeel morgen | $V_H = 102$ of $V_L = 98$ euro, elk met kans $\tfrac12$ |
| geïnformeerde handelaren | fractie $\mu = 0{,}2$, kopen bij $V_H$ en verkopen bij $V_L$ |
| ongeïnformeerde handelaren | kopen of verkopen met kans $\tfrac12$ |
| market maker | risiconeutraal, zonder kosten, verdient door concurrentie verwacht niets |

Omdat de market maker verwacht niets verdient, is zijn laatkoers de verwachte waarde
gegeven een kooporder en zijn biedkoers de verwachte waarde gegeven een verkooporder.
Met de regel van Bayes volgen die koersen in vijf stappen.

1. De kans op een koop is $0{,}2 + 0{,}8\cdot\tfrac12 = 0{,}6$ als de waarde hoog is en
   $0{,}8\cdot\tfrac12 = 0{,}4$ als ze laag is, zodat $P(\text{koop}) = 0{,}5$.
2. Dan is $P(H\mid\text{koop}) = 0{,}5\cdot0{,}6/0{,}5 = 0{,}6$ en
   $P(H\mid\text{verkoop}) = 0{,}4$.
3. De laatkoers is $0{,}6\cdot102 + 0{,}4\cdot98 = 100{,}40$ en de biedkoers
   $0{,}4\cdot102 + 0{,}6\cdot98 = 99{,}60$, dus de spread is $0{,}80 = \mu(V_H - V_L)$.
4. Na een koop is het oordeel $0{,}6$, zodat een volgende koop kans
   $0{,}6\cdot0{,}6 + 0{,}4\cdot0{,}4 = 0{,}52$ heeft, waarvan $0{,}6\cdot0{,}6 = 0{,}36$
   bij een
   hoge waarde. De laatkoers wordt dan $98 + 4\cdot0{,}36/0{,}52 = 100{,}77$ en de biedkoers
   $98 + 4\cdot0{,}6\cdot0{,}4/0{,}48 = 100{,}00$.
5. De verwachte volgende transactieprijs is $0{,}52\cdot100{,}77 + 0{,}48\cdot100{,}00 =
   100{,}40$, gelijk aan de huidige.

De spread krimpt dus van 0,80 naar 0,77 euro zodra de market maker iets heeft geleerd, en
de prijs die we na één koop verwachten, is de prijs van nu. Die tweede eigenschap heet de
martingaaleigenschap.

### Kyle met één handelsronde

| grootheid | waarde |
|---|---|
| liquidatiewaarde $v$ | normaal, verwachting $p_0 = 50$ euro, standaarddeviatie $\sigma_v = 4$ euro |
| order $u$ van de noise traders | normaal, verwachting nul, standaarddeviatie $\sigma_u = 10\,000$ aandelen |
| insider | kent $v$ en kiest zijn order |
| market maker | ziet alleen de totale order flow en zet één prijs |

Het evenwicht van Kyle nemen we hier over zonder afleiding, want de afleiding volgt pas in
de theorie. De insider koopt
$\beta = \sigma_u/\sigma_v$ aandelen per euro dat de waarde boven $p_0$ ligt, en de prijs
stijgt $\lambda = \sigma_v/(2\sigma_u)$ euro per aandeel order flow.

1. Hier is $\beta = 10\,000/4 = 2500$ en $\lambda = 4/20\,000 = 0{,}0002$, zodat een order
   van 10.000 aandelen de prijs 2 euro verschuift.
2. Bij $v = 53$ en $u = -4000$ koopt de insider $2500\cdot3 = 7500$ aandelen, is de order
   flow $3500$ en wordt de prijs $50 + 0{,}0002\cdot3500 = 50{,}70$.
3. De insider verdient $7500\cdot2{,}30 = 17\,250$ euro. De noise traders verkochten per
   saldo 4000 aandelen en verliezen 9200 euro, en de market maker verkocht er 3500 en
   verliest 8050 euro.

De som is nul, en dat de market maker hier verliest, is toeval, want gemiddeld speelt hij
quitte. De codecel rekent beide markten na en zet handberekening en code naast elkaar.

```{code-cell} ipython3
:label: cel-microstructuur-hand_vs_code

def gm_quotes(pi, mu, v_high, v_low):
    """Bid and ask of a zero-profit Glosten-Milgrom market maker with belief pi = P(V = v_high)."""
    buy_h, buy_l = mu + (1 - mu) / 2, (1 - mu) / 2
    post_buy = pi * buy_h / (pi * buy_h + (1 - pi) * buy_l)
    post_sell = pi * (1 - buy_h) / (pi * (1 - buy_h) + (1 - pi) * (1 - buy_l))
    return v_low + (v_high - v_low) * post_sell, v_low + (v_high - v_low) * post_buy

V_H, V_L, MU = 102.0, 98.0, 0.2
bid0, ask0 = gm_quotes(0.5, MU, V_H, V_L)
pi1 = 0.5 * 0.6 / 0.5                                  # belief after one buy order
bid1, ask1 = gm_quotes(pi1, MU, V_H, V_L)
p_buy_next = pi1 * 0.6 + (1 - pi1) * 0.4
next_price = p_buy_next * ask1 + (1 - p_buy_next) * bid1

sigma_v, sigma_u, p0 = 4.0, 10_000.0, 50.0
beta_k = sigma_u / sigma_v
lam_k = sigma_v / (2 * sigma_u)
v, u = 53.0, -4_000.0
theta = beta_k * (v - p0)                              # insider order
y = theta + u                                          # total order flow
p1 = p0 + lam_k * y
pnl = {"insider": theta * (v - p1), "noise traders": u * (v - p1), "market maker": -y * (v - p1)}

hand_vs_code = pd.DataFrame(
    {
        "met de hand": [99.60, 100.40, 0.80, 100.77, 100.00, 100.40,
                        2500, 0.0002, 50.70, 17_250, -9_200, -8_050, 0],
        "code": [bid0, ask0, ask0 - bid0, ask1, bid1, next_price,
                 beta_k, lam_k, p1, pnl["insider"], pnl["noise traders"], pnl["market maker"],
                 sum(pnl.values())],
    },
    index=[
        "GM: biedkoers", "GM: laatkoers", "GM: spread",
        "GM: laatkoers na een koop", "GM: biedkoers na een koop", "GM: verwachte volgende prijs",
        "Kyle: beta (aandelen per euro)", "Kyle: lambda (euro per aandeel)", "Kyle: prijs",
        "Kyle: winst insider", "Kyle: winst noise traders", "Kyle: winst market maker", "Kyle: som",
    ],
)
assert np.allclose(hand_vs_code["met de hand"], hand_vs_code["code"], atol=0.005)
hand_vs_code.round(4)
```

Code en handberekening komen overeen, op de afronding van de laatkoers na een koop na.
De spread van 0,80 euro is wat een ongeïnformeerde klant voor een aan- en verkoop betaalt,
alleen omdat een op de vijf handelaren de waarde kent. De prijsimpact $\lambda$ is voor de
insider een kost van dezelfde soort. Elk aandeel dat hij koopt, drijft zijn eigen
koopprijs op, zodat hij bij een voordeel van 3 euro niet onbeperkt koopt.

## Theorie

De theorie gaat in drie stappen van de handelsvloer naar verwachte rendementen en sluit
af met het marktontwerp van vandaag. Eerst
leiden we de spread van Glosten en Milgrom en het evenwicht van Kyle af. Daarna halen we
met de maten van Roll en Amihud dezelfde grootheden uit dagkoersen, en tot slot volgen we
liquiditeit als niveau en als risico. De kern is dat spread en prijsimpact geen kosten van
de market maker zijn, maar de prijs van informatie.

### Opzet en notatie

We gebruiken de symbolen van Kyle, zodat $\lambda$ de prijsimpact van order flow is en
$\beta$ de handelsintensiteit van de insider, en niet de prijs van risico of de
subjectieve discontofactor. De prijs van marktrisico heet daarom $\lambda_m$. De
liquidatiewaarde van het aandeel is $v$ (de payoff), de order van de insider $\theta$, de
order van de noise traders $u$ en de totale order flow $y = \theta + u$. Alle handelaren
zijn risiconeutraal en de rente is nul.

Bij Glosten en Milgrom komen handelaren één voor één met één aandeel, en zet de market
maker vooraf een bied- en een laatkoers. Bij Kyle dienen alle handelaren tegelijk een
marktorder in, een order zonder limietprijs, en zet de market maker één prijs op basis van
de som. Het eerste model levert dus spreads en het tweede prijsimpact, maar in beide
dwingt concurrentie de prijs naar de verwachte waarde van $v$ gegeven de order flow.

### Glosten-Milgrom: de spread als adverse selectie

De spread van Glosten en Milgrom bestaat alleen omdat een order iets verraadt over de
waarde. Een market maker die alle orders tegen dezelfde prijs uitvoert, verliest aan
geïnformeerde handelaren en wint niets terug van de rest. Omdat een koop op goed nieuws
wijst en een verkoop op slecht nieuws, speelt hij alleen quitte als zijn laatkoers boven
zijn biedkoers ligt.

:::{prf:theorem} Spread en martingaaleigenschap (Glosten-Milgrom)
:label: thm-microstructuur-gm

Laat $V \in \{V_L, V_H\}$, $\Delta V = V_H - V_L$, en laat $\pi = P(V = V_H \mid
\mathcal{F})$ het oordeel van de market maker zijn op basis van de publieke
orderhistorie $\mathcal{F}$. Een fractie $\mu$ van de handelaren is geïnformeerd, en de
rest koopt of verkoopt met kans $\tfrac12$. Dan zijn de nulwinstkoersen
$a = \E[V \mid \mathcal{F}, \text{koop}]$ en $b = \E[V \mid \mathcal{F}, \text{verkoop}]$,
met spread

```{math}
:label: eq-microstructuur-gm-spread
a - b \;=\; \frac{4\mu\,\pi(1-\pi)}{1 - \mu^2 (2\pi - 1)^2}\;\Delta V ,
```

en de reeks transactieprijzen $p_n = \E[V \mid \mathcal{F}_n]$ is een martingaal ten
opzichte van de publieke informatie, $\E[p_{n+1} \mid \mathcal{F}_n] = p_n$.
:::

:::{prf:proof}
:class: dropdown

Schrijf $q_H = \tfrac{1+\mu}{2}$ en $q_L = \tfrac{1-\mu}{2}$ voor de kans op een koop
gegeven hoge en lage waarde, zodat $q_H + q_L = 1$ en $q_H - q_L = \mu$. De kans op een
koop is $D_k = \tfrac12\bigl(1 + \mu(2\pi-1)\bigr)$ en op een verkoop
$D_v = \tfrac12\bigl(1 - \mu(2\pi-1)\bigr)$. Bayes geeft $a = V_L + \Delta V\,\pi q_H/D_k$
en $b = V_L + \Delta V\,\pi q_L / D_v$, dus

$$
a - b = \Delta V\,\pi\,\frac{q_H D_v - q_L D_k}{D_k D_v}
= \Delta V\,\pi\,\frac{(1-\pi)(q_H^2 - q_L^2)}{\tfrac14\bigl(1 - \mu^2(2\pi-1)^2\bigr)},
$$

en met $q_H^2 - q_L^2 = (q_H - q_L)(q_H + q_L) = \mu$ volgt
[](#eq-microstructuur-gm-spread). De transactieprijs na order $n$ is
$p_n = \E[V\mid\mathcal{F}_n]$, en omdat $\mathcal{F}_n \subseteq \mathcal{F}_{n+1}$, geeft
de toreigenschap $\E[p_{n+1}\mid\mathcal{F}_n] = \E[V\mid\mathcal{F}_n] = p_n$. $\square$
:::

Het bewijs past de regel van Bayes toe op beide koersen en trekt ze van elkaar af. Bij
$\pi = \tfrac12$ en $\mu = 0{,}2$ geeft [](#eq-microstructuur-gm-spread) de spread van
0,80 euro uit het toy-voorbeeld. Na één koop is $\pi = 0{,}6$, zodat de noemer $0{,}9984$
wordt en de spread $4\cdot0{,}2\cdot0{,}24\cdot4/0{,}9984 = 0{,}77$. De spread is dus het
grootst bij de grootste onzekerheid en krimpt naarmate de prijs de informatie opneemt,
terwijl een hogere $\mu$ hem breder maakt omdat elke order dan meer verraadt.

Zo'n spread bestaat zonder voorraadkosten of risicoaversie en is dus zuiver *adverse
selection* (het verlies aan beter geïnformeerde tegenpartijen), het uitgangspunt van het
leerboek van O'Hara {cite}`OHara1995`. De martingaaleigenschap geldt alleen ten opzichte
van de publieke informatie, want voor iemand die $V$ kent, loopt de prijs voorspelbaar op
of af. Het model maakt zo de stelling van Samuelson uit [](#02-06-efficiente-markten)
precies, want een prijs die een verwachte waarde is, verandert alleen onvoorspelbaar voor
wie alleen de orderhistorie kent.

### Kyle: het evenwicht met één handelsronde

In de markt van Kyle neemt de prijs na één ronde precies de helft van de onzekerheid over
$v$ weg, gemeten als variantie, hoeveel ruis er ook is. De insider weet dat zijn eigen
order de prijs opdrijft. Daarom koopt hij, zoals een monopolist de helft van de
concurrerende hoeveelheid levert, de helft van de positie waarbij de prijs tot $v$ zou
stijgen. De market maker
zet de prijs op de regressie van $v$ op $y$. Handelt de insider agressiever, dan wordt $y$
informatiever en stijgt $\lambda$, en een hogere $\lambda$ maakt de insider weer
voorzichtiger, zodat het evenwicht ligt waar die twee reacties elkaar vinden.

:::{prf:lemma} Projectietheorema
:label: thm-microstructuur-projectie

Als $(v, y)$ gezamenlijk normaal verdeeld zijn, dan is
$\E[v\mid y] = \E[v] + \frac{\Cov(v,y)}{\Var(y)}\bigl(y - \E[y]\bigr)$. De
voorwaardelijke variantie is $\Var(v\mid y) = \Var(v) - \frac{\Cov(v,y)^2}{\Var(y)}$ en
hangt niet van $y$ af.
:::

:::{prf:proof}
Laat $b = \Cov(v,y)/\Var(y)$ en $e = v - \E[v] - b(y - \E[y])$, zodat
$\Cov(e, y) = \Cov(v,y) - b\Var(y) = 0$. Omdat $(e, y)$ een lineaire transformatie van
een normale vector is, zijn $e$ en $y$ gezamenlijk normaal, en dan betekent
ongecorreleerd onafhankelijk. Dus $\E[e\mid y] = 0$ en $\Var(e\mid y) = \Var(e) =
\Var(v) - b^2\Var(y)$. $\square$
:::

:::{prf:theorem} Het Kyle-evenwicht met één ronde
:label: thm-microstructuur-kyle

Laat $v \sim N(p_0, \Sigma_0)$ en $u \sim N(0, \sigma_u^2)$ onafhankelijk zijn, met
$\sigma_v = \sqrt{\Sigma_0}$. De insider kiest $\theta$ om $\E[(v - p)\theta\mid v]$ te
maximaliseren, en de market maker zet $p = \E[v \mid y]$ met $y = \theta + u$. Er is een
uniek lineair evenwicht $\theta = \beta(v - p_0)$, $p = p_0 + \lambda y$, met

```{math}
:label: eq-microstructuur-kyle
\beta = \frac{\sigma_u}{\sigma_v},
\qquad
\lambda = \frac{\sigma_v}{2\sigma_u},
\qquad
\Sigma_1 \equiv \Var(v\mid p) = \tfrac12\Sigma_0 .
```

De verwachte winst van de insider is $\E[(v-p)\theta] = \tfrac12\sigma_v\sigma_u$. Het
verwachte verlies van de noise traders is even groot, en de market maker maakt verwacht
nul winst.
:::

:::{prf:proof}
:class: dropdown

*Stap 1: de beste order van de insider bij gegeven $\lambda$.* Neem aan dat de market
maker $p = p_0 + \lambda y$ zet met $\lambda > 0$. Voor gegeven $v$ is de verwachte winst
$\E[(v - p_0 - \lambda\theta - \lambda u)\theta \mid v] = (v - p_0)\theta -
\lambda\theta^2$, omdat $\E[u] = 0$. Die is strikt concaaf in $\theta$ zodra
$\lambda > 0$, en de eerste-ordevoorwaarde geeft $\theta = (v - p_0)/(2\lambda)$, dus
$\beta = 1/(2\lambda)$.

*Stap 2: de prijsregel van de market maker bij gegeven $\beta$.* Met
$\theta = \beta(v - p_0)$ zijn $v$ en $y = \beta(v-p_0) + u$ gezamenlijk normaal.
Volgens [](#thm-microstructuur-projectie) is $\E[v\mid y] = p_0 + \lambda y$ met

$$
\lambda = \frac{\Cov(v, y)}{\Var(y)} = \frac{\beta\Sigma_0}{\beta^2\Sigma_0 + \sigma_u^2}.
$$

*Stap 3: het vaste punt geeft $\lambda$ en $\beta$.* Substitueer $\beta = 1/(2\lambda)$,
zodat $\Sigma_0/(4\lambda) + \lambda\sigma_u^2 = \Sigma_0/(2\lambda)$, oftewel
$\lambda^2 = \Sigma_0/(4\sigma_u^2)$. De tweede-ordevoorwaarde kiest de positieve wortel
$\lambda = \sigma_v/(2\sigma_u)$, en dan is $\beta = \sigma_u/\sigma_v$. Elk lineair
evenwicht moet aan stap 1 tot en met 3 voldoen, dus het is uniek.

*Stap 4: de restvariantie en de winsten.* Volgens het lemma is $\Var(v\mid y) =
\Sigma_0 - \beta^2\Sigma_0^2/(\beta^2\Sigma_0 + \sigma_u^2)$, en met
$\beta^2\Sigma_0 = \sigma_u^2$ is dat $\Sigma_0/2$. De verwachte winst van de insider is
$\E[\beta(v-p_0)\,(v - p_0 - \lambda\beta(v-p_0) - \lambda u)] = \beta\Sigma_0(1 -
\lambda\beta) = \tfrac12\sigma_u\sigma_v$. Die van de noise traders is $\E[u(v - p)] =
-\lambda\sigma_u^2 = -\tfrac12\sigma_v\sigma_u$, en de market maker verdient
$-\E[y(v-p)] = 0$, omdat $v - \E[v\mid y]$ ongecorreleerd is met $y$. $\square$
:::

In het bewijs neemt de insider $\lambda$ als gegeven en koopt hij $(v-p_0)/(2\lambda)$, de
helft van de positie $(v-p_0)/\lambda$ waarbij de prijs tot $v$ zou stijgen. De market
maker neemt $\beta$ als gegeven en haalt
$\lambda$ uit het projectietheorema. Met de getallen uit het toy-voorbeeld
verdient de insider gemiddeld $\tfrac12\cdot4\cdot10\,000 = 20\,000$ euro en daalt de
variantie van $v$ van 16 naar 8.

De *diepte* van de markt, $1/\lambda$, stijgt met de ruis en daalt met de private
informatie. Verdubbelt $\sigma_u$, dan handelt de insider twee keer zoveel en verdient hij
twee keer zoveel, maar blijft de helft van de variantie over, zoals het beeld van de
verstopte insider deed verwachten. Meer noise traders maken de markt dus dieper en de
insider rijker, maar de prijs niet dommer. Zo ontsnapt het model aan de paradox van
Grossman en Stiglitz, omdat de verliezen van de noise traders het verzamelen van
informatie betalen.

### Kyle met vele handelsronden

Mag de insider over vele ronden handelen, dan komt zijn informatie in een constant tempo
in de prijs. Wat hij nu verraadt, kan hij later niet meer uitbuiten, dus houdt hij
informatie achter tot hij onverschillig is tussen nu en later handelen.

Kyle deelt de handelsperiode op in $N$ ronden met $\Delta t = 1/N$, waarin de noise traders
per ronde een order $\Delta u_n \sim N(0, \sigma_u^2\Delta t)$ inleggen {cite}`Kyle1985`.
De insider handelt $\Delta\theta_n = \beta_n(v - p_{n-1})\Delta t$, de prijs wordt
$p_n = p_{n-1} + \lambda_n(\Delta\theta_n + \Delta u_n)$, en $\Sigma_n$ is de onzekerheid
over $v$ die na ronde $n$ over is. De coëfficiënt $\alpha_n$, geen alpha in de gewone
betekenis, meet wat een resterend prijsverschil $v - p_n$ de insider later oplevert. Een
grote $\alpha_n$ maakt hem in ronde $n$ dus terughoudender.

:::{prf:proposition} Kyles recursie
:label: thm-microstructuur-kyle-recursie

Het lineaire evenwicht voldoet aan het stelsel differentievergelijkingen

```{math}
:label: eq-microstructuur-kyle-recursie
\begin{aligned}
\beta_n\Delta t &= \frac{1 - 2\alpha_n\lambda_n}{2\lambda_n(1 - \alpha_n\lambda_n)},
&\qquad
\lambda_n &= \frac{\beta_n\Sigma_n}{\sigma_u^2},
&\qquad
\Sigma_n &= (1 - \beta_n\lambda_n\Delta t)\,\Sigma_{n-1},\\
\alpha_{n-1} &= \frac{1}{4\lambda_n(1 - \alpha_n\lambda_n)},
&\qquad
\delta_{n-1} &= \delta_n + \alpha_n\lambda_n^2\sigma_u^2\Delta t,
&\qquad
\alpha_N &= \delta_N = 0,
\end{aligned}
```

met tweede-ordevoorwaarde $\lambda_n(1 - \alpha_n\lambda_n) > 0$. Hier is
$\alpha_n(v - p_n)^2 + \delta_n$ de verwachte resterende winst van de insider na ronde $n$.
Als $N \to \infty$, gaat $\lambda_n$ naar de constante $\sigma_v/\sigma_u$, daalt de
restonzekerheid lineair als $\Sigma(t) = (1 - t)\Sigma_0$ tot nul, en wordt de verwachte
totale winst van de insider $\sigma_v\sigma_u$.
:::

Kyle (1985, stelling 2 en 3) bewijst dit door te veronderstellen dat de resterende winst
kwadratisch is in $v - p_n$ en die veronderstelling achteruit te bevestigen vanaf
$\alpha_N = \delta_N = 0$. In de limiet verdient de insider twee
keer zoveel als in één ronde, omdat hij zijn informatie over de tijd kan spreiden.

### Numerieke oplossing van Kyles recursie

Al bij tien ronden ligt het evenwicht dicht bij de continue limiet uit de propositie, met
een constante prijsimpact en een lineair dalende onzekerheid. Per ronde geven de eerste
twee vergelijkingen samen een derdegraadsvergelijking in $\lambda_n$. We kiezen de
positieve wortel met $\alpha_n\lambda_n < \tfrac12$, omdat alleen die een positieve
$\beta_n$ en de tweede-ordevoorwaarde geeft. Omdat het stelsel homogeen is in $\Sigma$,
lossen we achteruit op vanaf $\Sigma_N = 1$. Aan het eind vermenigvuldigen we alle
$\Sigma_n$ met één factor $k$, $\lambda_n$ met $\sqrt{k}$ en $\beta_n$ met $1/\sqrt{k}$.
Dat doen we voor
1, 4, 10 en 50 ronden met $\sigma_v = \sigma_u = 1$.

```{code-cell} ipython3
def kyle_recursion(n_auctions, sigma_v=1.0, sigma_u=1.0):
    """Kyle (1985) N-auction linear equilibrium, solved backwards from Sigma_N = 1 and rescaled.

    Returns a DataFrame indexed by auction n = 1..N with lambda_n, beta_n and Sigma_n
    (posterior variance after auction n). ``attrs`` holds Sigma_0 and the insider's
    total expected profit alpha_0 Sigma_0 + delta_0.
    """
    dt, s2 = 1.0 / n_auctions, sigma_u**2
    lam, beta = np.empty(n_auctions), np.empty(n_auctions)
    sigma = np.empty(n_auctions + 1)
    sigma[-1], alpha, delta = 1.0, 0.0, 0.0
    for n in range(n_auctions - 1, -1, -1):
        # lambda solves -2 a s2 dt L^3 + 2 s2 dt L^2 + 2 a S L - S = 0 (from the first two equations)
        roots = np.roots([-2 * alpha * s2 * dt, 2 * s2 * dt, 2 * alpha * sigma[n + 1], -sigma[n + 1]])
        roots = roots[np.abs(roots.imag) < 1e-10].real
        L = roots[(roots > 0) & (alpha * roots < 0.5)].min()
        lam[n], beta[n] = L, L * s2 / sigma[n + 1]
        sigma[n] = sigma[n + 1] / (1 - beta[n] * L * dt)
        delta += alpha * L**2 * s2 * dt
        alpha = 1.0 / (4 * L * (1 - alpha * L))
    k = sigma_v**2 / sigma[0]            # homogeneity: Sigma*k, lambda*sqrt(k), beta/sqrt(k)
    out = pd.DataFrame(
        {"lambda": lam * np.sqrt(k), "beta": beta / np.sqrt(k), "Sigma": sigma[1:] * k},
        index=pd.RangeIndex(1, n_auctions + 1, name="ronde"),
    )
    out.attrs = {"Sigma_0": sigma[0] * k, "profit": alpha / np.sqrt(k) * sigma_v**2 + delta * np.sqrt(k)}
    return out

solutions = {n: kyle_recursion(n) for n in (1, 4, 10, 50)}
pd.DataFrame(
    {
        "lambda eerste ronde": [s["lambda"].iloc[0] for s in solutions.values()],
        "lambda laatste ronde": [s["lambda"].iloc[-1] for s in solutions.values()],
        "Sigma_N / Sigma_0": [s["Sigma"].iloc[-1] / s.attrs["Sigma_0"] for s in solutions.values()],
        "verwachte winst insider": [s.attrs["profit"] for s in solutions.values()],
    },
    index=pd.Index(list(solutions), name="rondes N"),
).round(4)
```

Bij $N = 1$ geeft de recursie het evenwicht van [](#thm-microstructuur-kyle) terug, met
$\lambda = 0{,}5$ en de helft van de variantie over. Naarmate $N$ groeit, gaat $\lambda$
naar 1 en de restvariantie naar nul, terwijl de verwachte winst bij 50 ronden 0,95 is.
Om te zien of de prijs zich ook in steekproeven zo gedraagt, simuleren we 20.000 markten
met 50 ronden.

```{code-cell} ipython3
kyle50 = solutions[50]
n_paths, N = 20_000, 50
dt = 1.0 / N
v_true = rng.normal(0.0, 1.0, n_paths)
price = np.zeros(n_paths)
profit = np.zeros(n_paths)
price_changes = np.empty((N, n_paths))
resid_var = np.empty(N)
for n in range(N):
    order = kyle50["beta"].iloc[n] * (v_true - price) * dt
    noise = rng.normal(0.0, np.sqrt(dt), n_paths)
    new_price = price + kyle50["lambda"].iloc[n] * (order + noise)
    profit += order * (v_true - new_price)
    price_changes[n] = new_price - price
    price = new_price
    resid_var[n] = np.var(v_true - price)

autocorr = np.corrcoef(price_changes[1:].ravel(), price_changes[:-1].ravel())[0, 1]
print(f"restvariantie na ronde 25: simulatie {resid_var[24]:.3f}, theorie {kyle50['Sigma'].iloc[24]:.3f}")
print(f"restvariantie na ronde 50: simulatie {resid_var[-1]:.3f}, theorie {kyle50['Sigma'].iloc[-1]:.3f}")
print(f"autocorrelatie opeenvolgende prijsveranderingen: {autocorr:+.4f}")
print(f"gemiddelde prijsverandering: {price_changes.mean():+.5f}")
print(f"insiderwinst per markt: gemiddelde {profit.mean():.3f} (theorie {kyle50.attrs['profit']:.3f}), "
      f"standaarddeviatie {profit.std():.3f}")
```

De gesimuleerde restvariantie is na 25 ronden 0,528 tegen 0,531 in theorie, en
opeenvolgende prijsveranderingen zijn ongecorreleerd. De prijs is dus een martingaal ten
opzichte van de order flow, ook al handelt er iemand die de uitkomst kent. De linker
figuur legt de punten van de simulatie naast de rechte lijn $1 - t$ van de continue limiet.

```{code-cell} ipython3
:label: cel-microstructuur-kyle-pad
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
for n, sol in solutions.items():
    if n == 1:
        continue
    t = np.r_[0, sol.index / n]
    axes[0].plot(t, np.r_[1.0, sol["Sigma"] / sol.attrs["Sigma_0"]], marker="o" if n == 4 else None, label=f"theorie, N = {n}")
    axes[1].plot(sol.index / n, sol["lambda"], marker="o" if n == 4 else None, label=f"N = {n}")
axes[0].plot(np.arange(1, N + 1) / N, resid_var, "k.", ms=4, label="simulatie, N = 50")
axes[0].plot([0, 1], [1, 0], color="grey", ls="--", lw=1, label="continue limiet $1-t$")
axes[0].set_title("Restonzekerheid $\\Sigma_n/\\Sigma_0$ neemt vrijwel lineair af")
axes[0].set_xlabel("Tijd binnen de handelsperiode $t = n/N$")
axes[0].set_ylabel("$\\Sigma_n / \\Sigma_0$")
axes[0].legend()
axes[1].axhline(1.0, color="grey", ls="--", lw=1, label="continue limiet $\\sigma_v/\\sigma_u$")
axes[1].set_title("Prijsimpact $\\lambda_n$ per ronde")
axes[1].set_xlabel("Tijd binnen de handelsperiode $t = n/N$")
axes[1].set_ylabel("$\\lambda_n$")
axes[1].legend()
plt.show()
```

:::{figure} #cel-microstructuur-kyle-pad
:label: fig-microstructuur-kyle-pad
:width: 100%

Links volgt de restvariantie al bij tien ronden bijna de rechte lijn $1 - t$, en de
gesimuleerde punten vallen op het theoretische pad, zodat de informatie in een constant
tempo in de prijs komt. Rechts is de prijsimpact vrijwel constant, behalve in de laatste
ronden.
:::

De figuur toont gemiddelden, maar de winst van één insider spreidt ruim, en over die
spreiding zegt de propositie niets. De standaarddeviatie van de
insiderwinst per markt is 1,024, iets meer dan het gemiddelde van 0,950, zodat een insider
met perfecte informatie na twintig handelsdagen een $t$-waarde van ongeveer
$\sqrt{20}\cdot0{,}950/1{,}024 \approx 4{,}1$ haalt. Een handelaar met een klein voordeel
heeft daar jaren voor nodig. Het probleem van [de standaardfout van 2%](#00-01-rendementen)
bestaat dus ook op de handelsvloer, want ook iemand met echte informatie kan zijn voordeel
moeilijk bewijzen.

::::{note} Een Glosten-Milgrom-sessie: een martingaal voor wie de waarde niet kent
:class: dropdown

In de markt van het toy-voorbeeld simuleren we 5000 handelsdagen van elk 60 orders,
waarbij de market maker na elke order zijn oordeel bijwerkt.

```{code-cell} ipython3
n_sessions, n_trades = 5_000, 60
q_high, q_low = MU + (1 - MU) / 2, (1 - MU) / 2
is_high = rng.random(n_sessions) < 0.5
belief = np.full(n_sessions, 0.5)
spreads = np.empty((n_sessions, n_trades))
beliefs = np.empty((n_sessions, n_trades + 1))
beliefs[:, 0] = belief
for n in range(n_trades):
    bid, ask = gm_quotes(belief, MU, V_H, V_L)
    spreads[:, n] = ask - bid
    informed = rng.random(n_sessions) < MU
    buy = np.where(informed, is_high, rng.random(n_sessions) < 0.5)
    like_high = np.where(buy, q_high, 1 - q_high)
    like_low = np.where(buy, q_low, 1 - q_low)
    belief = belief * like_high / (belief * like_high + (1 - belief) * like_low)
    beliefs[:, n + 1] = belief

value_path = V_L + (V_H - V_L) * beliefs
increments = np.diff(value_path, axis=1)
pd.DataFrame(
    {
        "gemiddelde prijsverandering": [increments.mean(), increments[is_high].mean(), increments[~is_high].mean()],
        "autocorrelatie prijsveranderingen": [
            np.corrcoef(increments[:, 1:].ravel(), increments[:, :-1].ravel())[0, 1],
            np.nan,
            np.nan,
        ],
    },
    index=["alle sessies (publieke informatie)", "sessies met V = V_H", "sessies met V = V_L"],
).round(4)
```

Over alle dagen samen is de gemiddelde prijsverandering nul, maar op dagen met een hoge
waarde loopt de prijs voorspelbaar op. Beide uitspraken zijn waar, omdat de
martingaaleigenschap bij een informatieverzameling hoort en niet bij een prijspad. De
figuur toont links de krimpende spread en rechts het pad van de verwachte waarde in zes sessies. De brede band links
laat zien hoe toevallig het tempo van prijsontdekking op één dag is.

```{code-cell} ipython3
:label: cel-microstructuur-gm-spread
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
trade_no = np.arange(1, n_trades + 1)
axes[0].fill_between(trade_no, np.percentile(spreads, 10, axis=0), np.percentile(spreads, 90, axis=0),
                     alpha=0.25, label="10e–90e percentiel")
axes[0].plot(trade_no, spreads.mean(axis=0), label="gemiddelde")
axes[0].plot(trade_no, np.median(spreads, axis=0), ls="--", label="mediaan")
axes[0].set_title("De spread krimpt naarmate informatie in de prijs komt")
axes[0].set_xlabel("Ordernummer binnen de sessie")
axes[0].set_ylabel("Spread (euro)")
axes[0].legend()
for s in range(6):
    axes[1].plot(np.arange(n_trades + 1), value_path[s], lw=1.2, color="C0" if is_high[s] else "C1")
axes[1].axhline(V_H, color="grey", ls=":", lw=1)
axes[1].axhline(V_L, color="grey", ls=":", lw=1)
axes[1].set_title("Verwachte waarde in zes sessies (blauw: $V_H$, rood: $V_L$)")
axes[1].set_xlabel("Ordernummer binnen de sessie")
axes[1].set_ylabel("Verwachte waarde na de order (euro)")
plt.show()
```

::::

### Roll: de spread uit de autocovariantie

Uit gewone transactiekoersen is de spread terug te rekenen, omdat de sprong tussen bied en
laat een negatieve autocovariantie achterlaat. De fundamentele waarde verandert
onvoorspelbaar, maar transacties vinden afwisselend tegen de biedkoers en de laatkoers
plaats. Na een transactie tegen de laatkoers volgt daarom vaker een daling dan een
stijging, en dat heen en weer springen, de *bid-ask bounce*, maakt opeenvolgende
koersveranderingen negatief gecorreleerd.

:::{prf:theorem} De Roll-maat
:label: thm-microstructuur-roll

Laat de waargenomen prijs $p_t = m_t + \tfrac{s}{2}q_t$ zijn, met efficiënte prijs
$m_t = m_{t-1} + e_t$, $e_t$ i.i.d. met variantie $\sigma_e^2$, en $q_t \in \{-1,+1\}$
i.i.d. met kans $\tfrac12$, onafhankelijk van $e$. Dan geldt

```{math}
:label: eq-microstructuur-roll
\Cov(\Delta p_t, \Delta p_{t-1}) = -\frac{s^2}{4},
\qquad\text{dus}\qquad
s = 2\sqrt{-\Cov(\Delta p_t, \Delta p_{t-1})},
```

en $\Var(\Delta p_t) = \sigma_e^2 + s^2/2$, zodat de eerste-orde-autocorrelatie
$\rho_1 = -\tfrac{s^2/4}{\sigma_e^2 + s^2/2}$ tussen $-\tfrac12$ en $0$ ligt.
:::

:::{prf:proof}
$\Delta p_t = e_t + \tfrac{s}{2}(q_t - q_{t-1})$. Omdat $e$ en $q$ onafhankelijk zijn en
$e_t$ geen autocorrelatie heeft, is
$\Cov(\Delta p_t,\Delta p_{t-1}) = \tfrac{s^2}{4}\Cov(q_t - q_{t-1},\, q_{t-1} - q_{t-2})$.
Van de vier termen is alleen $\Cov(-q_{t-1}, q_{t-1}) = -1$ ongelijk aan nul, en evenzo is
$\Var(\Delta p_t) = \sigma_e^2 + \tfrac{s^2}{4}\cdot 2$. $\square$
:::

Een spread van 0,80 euro, zoals in het toy-voorbeeld, laat volgens
[](#eq-microstructuur-roll) een autocovariantie van $-0{,}80^2/4 = -0{,}16$ achter. Op
rendementen geeft dezelfde formule de relatieve spread. Het model laat geen ruimte voor
andere autocorrelatie, zodat een positieve autocovariantie de wortel ongedefinieerd maakt
en een negatieve door overreactie als spread wordt gelezen. Het signaal is bovendien
klein, want bij een spread van één basispunt en een dagvolatiliteit van 1,5% is
$|\rho_1|$ van de orde $10^{-5}$.

### Amihud: prijsimpact uit dagdata

Ook zonder transactiedata is Kyles $\lambda$ bij benadering te meten, als koersbeweging
per dollar omzet. Grote koersbewegingen bij weinig omzet wijzen op een ondiepe markt, en
Amihud {cite}`Amihud2002` definieerde daarom voor aandeel $i$ met $D_i$ handelsdagen in een
jaar

```{math}
:label: eq-microstructuur-illiq
\mathrm{ILLIQ}_{i} = \frac{1}{D_{i}} \sum_{d=1}^{D_{i}} \frac{|r_{i,d}|}{\mathrm{DVOL}_{i,d}},
```

met $r_{i,d}$ het dagrendement en $\mathrm{DVOL}_{i,d}$ de omzet in dollars. Een aandeel
dat op een dag met 10 miljoen dollar omzet 1% beweegt, heeft die dag een ILLIQ van 0,1%
per miljoen dollar.

:::{prf:proposition} Amihuds maat in een Kyle-markt
:label: thm-microstructuur-amihud-kyle

Neem een Kyle-markt met één ronde en beginprijs $p_0 > 0$, en veronderstel dat alleen de
netto order flow wordt verhandeld, met omzet $|y|$ aandelen en dollaromzet $p_0|y|$. Dan
is op elke dag met $y \neq 0$

$$
\frac{|r|}{\mathrm{DVOL}} = \frac{\lambda|y|/p_0}{p_0|y|} = \frac{\lambda}{p_0^2},
$$

zodat ILLIQ gelijk is aan Kyles $\lambda$, uitgedrukt als rendement per dollar omzet.
:::

:::{prf:proof}
In de Kyle-markt is $p_1 - p_0 = \lambda y$ precies, dus $|r| = \lambda|y|/p_0$. Delen
door $p_0|y|$ geeft het resultaat. $\square$
:::

In echte markten komt er ook publiek nieuws in de prijs en is de omzet groter dan de netto
order flow, zodat ILLIQ alleen een ruisend signaal van $\lambda$ is. Het signaal is wel
bruikbaar, omdat de ruis over een jaar dagdata grotendeels uitmiddelt en de rangorde van
aandelen naar diepte blijft staan.

### Liquiditeit in de prijs: het niveau

Illiquide aandelen moeten meer opleveren, maar minder dan evenredig met hun spread. Een
belegger die een aandeel na $h$ jaar verkoopt, betaalt de spread één keer, dus $s/h$ per
jaar. Aandelen met hoge spreads belanden daardoor bij beleggers met een lange horizon. Voor
hen weegt de spread het minst, zodat het vereiste rendement minder hard stijgt dan de
spread. Amihud en Mendelson {cite}`AmihudMendelson1986` vonden precies dat het verwachte
rendement met de spread stijgt, maar steeds minder snel.

Amihud bracht de vraag later naar de tijdreeks, met een regressie van het overrendement
van de markt op de illiquiditeit van de markt,

$$
R^e_{m,t} = g_0 + g_1 \ln\mathrm{ILLIQ}_{m,t-1} + g_2 \ln\mathrm{ILLIQ}^{u}_{m,t} +
\varepsilon_t ,
$$

waarin $\ln\mathrm{ILLIQ}^{u}$ de onverwachte illiquiditeit is, de schok uit een AR(1).
Verwachte illiquiditeit verhoogt het verwachte overrendement, dus $g_1 > 0$. Onverwachte
illiquiditeit verlaagt het rendement in dezelfde periode, dus $g_2 < 0$, omdat een
blijvende schok het vereiste rendement voor de toekomst verhoogt en de prijs vandaag laat
dalen. Op jaardata voor NYSE-aandelen over 1964–1997 vond Amihud beide tekens.

### Liquiditeit als risico: Pástor-Stambaugh en Acharya-Pedersen

Omdat marktliquiditeit in de tijd varieert en alle aandelen tegelijk raakt, is ze ook een
risico. Ze is een toestandsvariabele zoals in het ICAPM ([](#03-10-merton-icapm)), waar
een activum dat slecht rendeert als de toestand verslechtert, meer moet opleveren. Een
aandeel dat daalt wanneer de markt illiquide wordt, verliest dus waarde op het moment dat
beleggers geld het hardst nodig hebben.

Pástor en Stambaugh {cite}`PastorStambaugh2003` maten de liquiditeit van aandeel $i$ in
maand $t$ als de coëfficiënt $\gamma_{i,t}$ in de regressie op dagdata

```{math}
:label: eq-microstructuur-ps
r^e_{i,d+1,t} = \theta_{i,t} + \phi_{i,t}\, r_{i,d,t} + \gamma_{i,t}\,
\operatorname{sign}(r^e_{i,d,t})\, v_{i,d,t} + \epsilon_{i,d+1,t},
```

met $r^e$ het rendement boven de markt, $v$ hier de dollaromzet en $\theta_{i,t}$ en
$\phi_{i,t}$ gewone regressiecoëfficiënten. Getekende omzet benadert de order flow, en in
een illiquide markt wordt een koersbeweging die door orders komt deels teruggedraaid,
zodat $\gamma_{i,t}$ negatief is. Het gemiddelde over aandelen, min het
voorspelbare deel, levert innovaties $\mathcal{L}_t$, en de *liquiditeitsbèta*
$\beta_{i,\mathcal{L}}$ is de helling daarop naast de drie Fama-French-factoren. Aandelen
met een hoge voorspelde liquiditeitsbèta leverden na correctie voor vier factoren ongeveer
7,5% per jaar meer op dan aandelen met een lage.

Acharya en Pedersen {cite}`AcharyaPedersen2005` leidden in een economie met wisselende
handelskosten $c_{i,t}$ een CAPM af voor rendementen na kosten. In bruto rendementen en in
onze notatie geeft dat

```{math}
:label: eq-microstructuur-lcapm
\E[R^e_{i}] = \E[c_i] + \lambda_m\beta_{i,1} + \lambda_m\beta_{i,2}
- \lambda_m\beta_{i,3} - \lambda_m\beta_{i,4},
```

met $\lambda_m$ de prijs van marktrisico na kosten (de verwachte marktpremie min de
handelskosten
van de markt, enkele procenten per jaar) en
$\beta_{i,1}$ de gewone marktbèta. De
andere drie bèta's belonen een aandeel dat illiquide wordt als de markt illiquide wordt
($\Cov(c_i, c_m)$), dat slecht rendeert als de markt illiquide wordt ($\Cov(r_i, c_m)$),
en dat illiquide wordt als de markt daalt ($\Cov(c_i, r_m)$). Met ILLIQ als maat voor
$c_i$ schatten ze over 1963–1999 dat liquiditeitsrisico ongeveer 1,1% per jaar bijdraagt
aan het verschil tussen de meest en de minst illiquide aandelen. De drie bèta's zijn wel
sterk gecorreleerd, zodat de verdeling over de kanalen onzeker is.

### Marktontwerp: van specialist naar batchveiling

De modellen van 1985 beschrijven een specialist, maar vandaag voeren algoritmen de orders
uit in een doorlopend orderboek. Budish, Cramton en Shim {cite}`BudishCramtonShim2015`
lieten zien dat de correlatie tussen een indexfuture en een indexfonds op de schaal van
milliseconden wegvalt. Dat levert mechanische arbitragekansen op, en concurrentie
verkleint die niet maar drijft alleen de vereiste snelheid op. Een handelaar met een
staande koers wordt na elk publiek signaal door de snelste handelaar uitgebuit, net als de
market maker van Glosten en Milgrom, en dat verlies zit in de spread. De auteurs stelden
daarom *frequent batch auctions* voor, veilingen die alle orders van bijvoorbeeld een
tiende seconde tegen één prijs uitvoeren.

```{admonition} Samengevat
:class: tip

- Een market maker tegenover beter geïnformeerden rekent een spread die bij
  $\pi = \tfrac12$ gelijk is aan $\mu\,\Delta V$ en krimpt naarmate hij leert
  ([](#eq-microstructuur-gm-spread)); een hogere $\mu$ maakt hem breder.
- In de markt van Kyle is $\lambda = \sigma_v/(2\sigma_u)$ en blijft na één ronde de helft
  van de onzekerheid over ([](#eq-microstructuur-kyle)). Meer ruis maakt de markt dieper
  en de insider rijker, maar de prijs niet minder informatief.
- De Roll-maat haalt de spread uit de autocovariantie $-s^2/4$
  ([](#eq-microstructuur-roll)), en ILLIQ benadert $\lambda$ als rendement per dollar
  omzet ([](#eq-microstructuur-illiq)).
- Liquiditeit komt als niveau en als risico in verwachte rendementen, met drie
  liquiditeitsbèta's naast de marktbèta ([](#eq-microstructuur-lcapm)).
```

## Simulatie: de Roll-schatter in eindige steekproeven

Hoe vaak is de Roll-maat in een steekproef van gewone lengte niet te berekenen? Tweede
momenten zijn meestal goed meetbaar, maar het signaal $-s^2/4$ is klein naast de variantie
van de koersveranderingen. De standaardfout van een steekproefautocovariantie is bij een
i.i.d.-benadering ongeveer $\Var(\Delta p)/\sqrt{T}$, zodat voor de kans op een positieve
en dus onbruikbare schatting geldt

```{math}
:label: eq-microstructuur-roll-kans
P\bigl(\widehat{\Cov} > 0\bigr) \approx \Phi\!\left(\sqrt{T}\,\rho_1\right),
\qquad \rho_1 = -\frac{s^2/4}{\sigma_e^2 + s^2/2}.
```

Voor de spread van 0,80 euro uit het toy-voorbeeld bij een dagvolatiliteit van 1 euro is
$\rho_1 = -0{,}16/1{,}32 = -0{,}121$. Over een kwartaal van 60 dagen is de kans dan
$\Phi(-\sqrt{60}\cdot0{,}121) = \Phi(-0{,}94) \approx 0{,}17$, maar bij $s/\sigma_e = 0{,}01$
is ze bijna een half. We simuleren het model voor 22 verhoudingen $s/\sigma_e$ tussen 0,01
en 3, met $T = 60$ en $T = 250$ dagen en 4000 steekproeven per punt.

```{code-cell} ipython3
def roll_positive_share(spread_ratio, n_days, n_samples=4_000):
    """Share of samples in which the Roll autocovariance is positive (sigma_e = 1)."""
    e = rng.normal(0.0, 1.0, (n_samples, n_days))
    q = rng.choice([-1.0, 1.0], (n_samples, n_days + 1))
    dp = e + spread_ratio / 2 * np.diff(q, axis=1)
    dp = dp - dp.mean(axis=1, keepdims=True)
    cov = (dp[:, 1:] * dp[:, :-1]).sum(axis=1) / (n_days - 1)
    return (cov > 0).mean()

ratios = np.geomspace(0.01, 3.0, 22)
roll_sim = pd.DataFrame(
    {T: [roll_positive_share(r, T) for r in ratios] for T in (60, 250)}, index=pd.Index(ratios, name="s / sigma")
)
roll_theory = pd.DataFrame(
    {T: stats.norm.cdf(np.sqrt(T) * -(ratios**2 / 4) / (1 + ratios**2 / 2)) for T in (60, 250)}, index=ratios
)
roll_sim.iloc[[0, 5, 10, 14, 17, 21]].round(3)
```

Bij $s/\sigma_e = 0{,}01$ is de autocovariantie in 46% van de kwartalen en 48% van de
jaren positief, en pas bij een verhouding rond 1 bestaat de maat bijna altijd. De figuur
zet simulatie en benadering naast elkaar, met de grote liquide aandelen in het grijze
gebied.

```{code-cell} ipython3
:label: cel-microstructuur-roll-sim
:tags: [hide-input]

fig, ax = plt.subplots()
for i, T in enumerate((60, 250)):
    ax.plot(ratios, roll_sim[T], "o", color=f"C{i}", label=f"simulatie, T = {T} dagen")
    ax.plot(ratios, roll_theory[T], "-", color=f"C{i}", lw=1, label=f"benadering, T = {T} dagen")
ax.axvspan(0.003, 0.1, color="grey", alpha=0.15, label="grote liquide aandelen")
ax.set_xscale("log")
ax.set_xlim(0.008, 3.5)
ax.set_title("Hoe vaak is de Roll-maat ongedefinieerd?")
ax.set_xlabel("Spread gedeeld door volatiliteit van de efficiënte prijs, $s/\\sigma_e$ (log-schaal)")
ax.set_ylabel("Fractie steekproeven met positieve autocovariantie")
ax.legend()
plt.show()
```

:::{figure} #cel-microstructuur-roll-sim
:label: fig-microstructuur-roll-sim
:width: 90%

Voor grote liquide aandelen (grijs gebied) is de Roll-maat in bijna de helft van de
steekproeven ongedefinieerd, ook als het model precies klopt. Een langere steekproef helpt
maar met een factor $\sqrt{T}$. In het grijze gebied verschuift de curve van een kwartaal
naar een jaar daardoor nauwelijks, en pas bij grotere spreads daalt ze zichtbaar.
:::

Benadering en simulatie liggen vrijwel op elkaar. Beide laten zien dat een variantie goed
meetbaar is, tenzij het deel dat we zoeken een honderdduizendste van het totaal
is. De ruis is
bovendien niet symmetrisch, want wie de Roll-maat alleen middelt over de jaren waarin ze
bestaat, overschat de spread stelselmatig.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Het tijdreeksdeel van Amihud {cite}`Amihud2002` (model (11)), de impliciete
spread van Roll {cite}`Roll1984b`, en de crisismaanden, de correlatie met het
marktrendement en de liquiditeitspremie van Pástor en Stambaugh {cite}`PastorStambaugh2003`.

**Wat.** Het teken van $g_2$ en $g_1$, het aandeel ongedefinieerde Roll-schattingen, de
diepste liquiditeitsmaanden en de alpha van de verhandelbare liquiditeitsfactor.

**Data hier.** Dagkoersen en volumes van vijftig grote Amerikaanse aandelen, 2002–2026,
via `hap.data.yahoo` (dezelfde vijftig als in [](#03-14-roll)), de French-factoren, en de
liquiditeitsreeksen van Stambaugh, 1962–2025, via een kleine lokale loader.

**Verschil met het origineel.** Amihud en Roll gebruikten alle NYSE-aandelen uit CRSP en
Amihud werkte met jaren, terwijl wij vijftig overlevenden ([](#02-05-crsp-tape)) per maand
volgen. De verhandelbare factor van Pástor en Stambaugh sorteert op historische in plaats
van voorspelde bèta's.

**Verwachte afwijking.** Het teken van $g_2$ moet negatief zijn, met een $t$-waarde ruim
boven twee in absolute waarde. Voor $g_1$ verwachten we met 24 jaar van vijftig overlevenden
geen significant verband. De alpha van de factor ligt lager dan in het artikel, omdat
historische bèta's de toekomstige liquiditeitsbèta met ruis meten. De diepste maanden uit het artikel moeten bij de laagste
van de bijgewerkte reeks zitten, en de correlatie van $\mathcal{L}_t$ met het
marktrendement over 1966–1999 ligt dicht bij 0,36.
```

### Amihud en Roll per aandeel

ILLIQ zet de vijftig aandelen in een plausibele volgorde, terwijl de Roll-maat vooral ruis
meet. De codecel berekent per aandeel de dagelijkse ILLIQ in basispunten per miljoen dollar
omzet en per jaar de Roll-spread uit de autocovariantie van de dagrendementen.

```{code-cell} ipython3
TICKERS = [
    "AAPL", "ADBE", "AMZN", "ANET", "APH", "AVGO", "BAC", "BRK-B", "CMG", "CPRT",
    "CRM", "CSX", "CTAS", "CVX", "DE", "DHR", "DXCM", "EW", "FAST", "FTNT",
    "GILD", "GOOGL", "IDXX", "ISRG", "KO", "LRCX", "MA", "MNST", "NFLX", "NKE",
    "NOW", "NVDA", "ODFL", "ORLY", "PANW", "PG", "QCOM", "ROST", "SBUX", "SHW",
    "SMCI", "TJX", "TSCO", "TSLA", "UNH", "UNP", "V", "WFC", "WMT", "WRB",
]
prices = hap_data.yahoo(TICKERS, start="2002-01-01", end="2026-08-01")
volume = hap_data.yahoo(TICKERS, start="2002-01-01", end="2026-08-01", field="Volume")

returns = prices.pct_change(fill_method=None).loc["2002-01-03":]
dollar_volume_mln = (prices * volume).where(volume > 0).loc[returns.index] / 1e6
illiq_daily = returns.abs() / dollar_volume_mln * 1e4       # basis points per million dollars

def first_autocov(series, min_obs=100):
    """First-order autocovariance of a return series; NaN if fewer than min_obs observations."""
    x = series.dropna().to_numpy()
    return np.cov(x[1:], x[:-1])[0, 1] if len(x) > min_obs else np.nan

autocov_year = returns.groupby(returns.index.year).agg(first_autocov)
roll_year_bp = 2 * np.sqrt(-autocov_year.where(autocov_year < 0)) * 1e4

per_stock = pd.DataFrame(
    {
        "ILLIQ 2021–2026 (bp per $ mln)": illiq_daily.loc["2021":].mean(),
        "Roll-spread 2021–2026 (bp)": roll_year_bp.loc[2021:].median(),
        "fractie jaren Roll ongedefinieerd": (autocov_year >= 0).sum() / autocov_year.notna().sum(),
    }
).sort_values("ILLIQ 2021–2026 (bp per $ mln)")
print(f"aandeel-jaren met positieve autocovariantie: {(autocov_year >= 0).sum().sum()} van "
      f"{autocov_year.notna().sum().sum()} ({(autocov_year >= 0).sum().sum() / autocov_year.notna().sum().sum():.1%})")
per_stock.iloc[[0, 1, 2, 3, 4, -5, -4, -3, -2, -1]].round(3)
```

De tabel toont de vijf meest en de vijf minst liquide namen. Apple, Tesla en Amazon zijn
het diepst en Super Micro het ondiepst, met ruim twee ordes van grootte ertussen. De
Roll-maat is in 427 van de 1168 aandeel-jaren ongedefinieerd, ruim een derde, wat past bij
de simulatie. Waar ze bestaat, geeft ze spreads van 60 tot 170 basispunten. Zulke
waarden ontstaan omdat Rolls formule alle negatieve autocorrelatie in dagrendementen meet
en niet alleen de bid-ask bounce. Bovendien tellen alleen de jaren met een negatieve
schatting mee, het selectie-effect uit de simulatie. Per jaar bekijken we daarna de
mediane Roll-spread en de mediane ILLIQ.

```{code-cell} ipython3
by_year = pd.DataFrame(
    {
        "mediane Roll-spread (bp)": roll_year_bp.median(axis=1),
        "fractie ongedefinieerd": (autocov_year >= 0).sum(axis=1) / autocov_year.notna().sum(axis=1),
        "mediane ILLIQ (bp per $ mln)": illiq_daily.groupby(illiq_daily.index.year).mean().median(axis=1),
    }
)
by_year.round(3)
```

De Roll-maat pikt de crises wel op, met de hoogste mediane spread in 2020 en 2008, vooral
omdat volatiliteit en omkeringen dan toenemen. De mediane ILLIQ daalt met ongeveer een
factor dertig, omdat deze vijftig aandelen zo sterk zijn gegroeid, zodat we die trend
eerst uit een marktbrede reeks moeten halen.

### Marktbrede illiquiditeit en het marktrendement

Marktbrede illiquiditeit piekt in 2008 en maart 2020 en gaat samen met lage gelijktijdige
marktrendementen. We nemen per aandeel per maand de logaritme van de gemiddelde ILLIQ,
trekken per aandeel het gemiddelde af en middelen over aandelen. Daarna schatten we de
maandelijkse versie van Amihuds tijdreeksregressie met Newey-West-standaardfouten.

```{code-cell} ipython3
days = illiq_daily.resample("ME").count()
log_illiq = np.log(illiq_daily.resample("ME").mean().where(days >= 15))
market_illiq = log_illiq.sub(log_illiq.mean()).mean(axis=1).rename("illiq")
deviation = (market_illiq - market_illiq.rolling(12).mean().shift(1)).rename("afwijking")

ar1 = hap.stats.newey_west(market_illiq, market_illiq.shift(1).rename("vertraagd"), lags=0)
innovation = (market_illiq - ar1.params["const"] - ar1.params["vertraagd"] * market_illiq.shift(1)).rename("innovatie")

ff3 = hap_data.market_monthly()
design = pd.concat([market_illiq.shift(1).rename("illiq vertraagd"), innovation], axis=1, sort=True)
amihud_fit = hap.stats.newey_west(ff3["Mkt-RF"].reindex(design.index), design, lags=3)

print(f"AR(1)-helling marktilliquiditeit: {ar1.params['vertraagd']:.3f}")
print("Hoogste afwijkingen van het voorgaande jaargemiddelde (log-punten):")
print(deviation.nlargest(6).round(2).to_string())
pd.DataFrame(
    {"coëfficiënt": amihud_fit.params, "NW-standaardfout": amihud_fit.bse, "t-waarde": amihud_fit.tvalues}
).round(4)
```

Het teken van $g_2$ is gerepliceerd, want een onverwachte stijging van de
marktilliquiditeit gaat samen met een fors en zeer significant lager overrendement in
dezelfde maand. Een deel daarvan zit mechanisch in de
constructie, omdat een koersdaling $|r|$ verhoogt en de dollaromzet verlaagt. De
coëfficiënt $g_1$ op de vertraagde illiquiditeit is klein, negatief en niet significant.
Om een voorspellend verband voor het marktrendement aan te tonen, zijn echter decennia nodig
([](#04-20-voorspelbaarheid)), en 24 jaar van vijftig overlevenden is daarvoor te kort. De
figuur laat onder de maanden zien waarin de illiquiditeit boven het gemiddelde van het
voorgaande jaar uitschiet.

```{code-cell} ipython3
:label: cel-microstructuur-amihud-tijd
:tags: [hide-input]

fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), sharex=True)
axes[0].plot(market_illiq.index, market_illiq, label="log-illiquiditeit (gemiddeld over aandelen)")
axes[0].set_title("Marktbrede Amihud-illiquiditeit van vijftig grote aandelen")
axes[0].set_ylabel("Log-ILLIQ t.o.v. aandeelgemiddelde")
axes[0].legend(loc="upper right")
axes[1].bar(deviation.index, deviation, width=25, color=np.where(deviation > 0, "C1", "C0"))
for date, text in [("2008-11-30", "okt.–nov. 2008"), ("2020-03-31", "maart 2020")]:
    axes[1].annotate(text, (pd.Timestamp(date), deviation.loc[date]), xytext=(10, 5), textcoords="offset points")
axes[1].set_title("Afwijking van het gemiddelde van de voorgaande twaalf maanden")
axes[1].set_ylabel("Log-punten")
hap.plotting.timeline_axis(axes[1], every=2)
axes[1].set_xlabel("Jaar")
plt.show()
```

:::{figure} #cel-microstructuur-amihud-tijd
:label: fig-microstructuur-amihud-tijd
:width: 100%

Boven daalt de illiquiditeit van deze vijftig aandelen sterk, omdat ze zo gegroeid zijn.
Onder zijn maart 2020 en oktober tot december 2008 de grootste uitschieters, precies de
maanden waarin veel beleggers moesten verkopen.
:::

### Pástor-Stambaugh

De reeks van Pástor en Stambaugh laat zien dat liquiditeit in crises instort. Omdat
`hap.data` geen loader voor deze reeks heeft, haalt de functie hieronder het bestand van
Stambaughs Wharton-pagina één keer op en bewaart het in de cache.

```{code-cell} ipython3
PS_URL = "https://finance.wharton.upenn.edu/~stambaug/liq_data_1962_2025.txt"

def pastor_stambaugh_liquidity():
    """Pastor-Stambaugh (2003) monthly liquidity series, cached as a parquet snapshot.

    Columns: agg_liq (level, their Figure 1), innov_liq (innovation L_t, eq. 8) and
    traded_liq (cap-weighted 10-1 portfolio on historical liquidity betas), decimals.
    """
    # TODO: naar hap.data (loader voor Stambaugh's Wharton-pagina)
    def build():
        text = requests.get(PS_URL, timeout=60).text
        rows = [line for line in text.splitlines() if line.strip() and not line.lstrip().startswith("%")]
        frame = pd.read_csv(io.StringIO("\n".join(rows)), sep=r"\s+", header=None,
                            names=["month", "agg_liq", "innov_liq", "traded_liq"])
        frame.index = pd.DatetimeIndex(
            pd.to_datetime(frame.pop("month").astype(str), format="%Y%m") + pd.offsets.MonthEnd(0), name="date"
        )
        return frame.mask(frame <= -99)

    return hap_cache.load_cached("pastor_stambaugh__liq_1962_2025", build)

ps = pastor_stambaugh_liquidity()
ps_market = pd.concat([ps, ff3["Mkt-RF"]], axis=1, sort=True).dropna(subset=["innov_liq", "Mkt-RF"])
print(f"reeks: {ps.index[0]:%Y-%m} t/m {ps.index[-1]:%Y-%m}")
print(f"correlatie L_t met Mkt-RF, 1966–1999: {ps_market.loc['1966':'1999', ['innov_liq', 'Mkt-RF']].corr().iloc[0, 1]:.2f}"
      f" (werkdocument: 0.36)")
print(f"correlatie L_t met Mkt-RF, 1962–2025: {ps_market[['innov_liq', 'Mkt-RF']].corr().iloc[0, 1]:.2f}")
both = pd.concat([ps["innov_liq"], innovation], axis=1, sort=True).dropna()
print(f"correlatie L_t met onze Amihud-innovatie, {both.index[0]:%Y}–{both.index[-1]:%Y}: {both.corr().iloc[0, 1]:.2f}")
ps["agg_liq"].nsmallest(6).rename("laagste liquiditeitsniveau").round(3).to_frame()
```

De drie diepste maanden uit het artikel staan ook in de bijgewerkte reeks bij de laagste.
De correlatie met het marktrendement ligt vrijwel op de gepubliceerde waarde, al
gebruiken we de French-marktfactor in plaats van de NYSE-AMEX-index. Onze Amihud-innovatie
correleert
negatief met hun liquiditeitsinnovatie, zoals het hoort bij een maat voor
*il*liquiditeit, maar zwak, omdat de twee maten verschillende kanten van liquiditeit
meten. In de figuur vallen de diepe, korte uitschieters naar beneden op.

```{code-cell} ipython3
:label: cel-microstructuur-ps
:tags: [hide-input]

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(ps.index, ps["agg_liq"], lw=1)
for date in ps["agg_liq"].nsmallest(5).index:
    ax.annotate(f"{date:%Y-%m}", (date, ps.loc[date, "agg_liq"]), xytext=(4, -10), textcoords="offset points", fontsize=8)
ax.axhline(0, color="grey", lw=0.8)
ax.set_title("Marktbrede liquiditeit volgens Pástor en Stambaugh, 1962–2025")
ax.set_xlabel("Jaar")
ax.set_ylabel("Geschaalde gemiddelde $\\hat\\gamma_t$")
hap.plotting.timeline_axis(ax, every=5)
plt.show()
```

:::{figure} #cel-microstructuur-ps
:label: fig-microstructuur-ps
:width: 100%

De liquiditeit is meestal rustig en stort af en toe diep in, bijna altijd in een bekende
crisismaand. Die asymmetrie maakt van liquiditeit een risico en niet alleen een kost.
:::

Tot slot schatten we de vierfactor-alpha van de verhandelbare factor over de hele periode
en over de jaren voor en na publicatie.

```{code-cell} ipython3
momentum = hap_data.french("F-F_Momentum_Factor")
factors4 = pd.concat([hap_data.french("F-F_Research_Data_Factors")[["Mkt-RF", "SMB", "HML"]], momentum],
                     axis=1, sort=True)
rows = {}
for start, end in [("1968", "2025"), ("1968", "2003"), ("2004", "2025")]:
    y = ps["traded_liq"].loc[start:end].dropna()
    fit = hap.stats.newey_west(y, factors4.reindex(y.index), lags=6)
    rows[f"{start}–{end}"] = {
        "maanden": len(y),
        "gemiddeld rendement (% p.j.)": 1200 * y.mean(),
        "vierfactor-alpha (% p.j.)": 1200 * fit.params["const"],
        "standaardfout alpha (% p.j.)": 1200 * fit.bse["const"],
        "t-waarde": fit.tvalues["const"],
    }
pd.DataFrame(rows).T.round(2)
```

De alpha over de hele periode is net significant, maar rust volledig op de jaren tot en
met 2003, het jaar van publicatie. Daarna is de alpha licht negatief, en de standaardfout
is zo groot dat 22 jaar data een premie als die van vóór 2003 aantonen noch
uitsluiten. De tabel hieronder zet de drie perioden naast het origineel.

### Origineel en hier

| grootheid | origineel | hier |
|---|---|---|
| $g_2$, onverwachte illiquiditeit | negatief (jaren 1964–1997) | $-0{,}135$, $t = -7{,}87$ (maanden 2002–2026) |
| $g_1$, verwachte illiquiditeit | positief | $-0{,}002$, $t = -1{,}19$ |
| persistentie van illiquiditeit | hoog, jaarlijkse AR(1) | 0,986 per maand, $0{,}986^{12} \approx 0{,}84$ per jaar |
| Roll-maat ongedefinieerd | voor een deel van de aandelen | 36,6% van de aandeel-jaren |
| diepste liquiditeitsmaanden | okt. 1987, nov. 1973, sep. 1998 | plaats 1, 2 en 5 |
| correlatie $\mathcal{L}_t$ met marktrendement, 1966–1999 | 0,36 | 0,35 |
| alpha liquiditeitsfactor (% per jaar) | 7,5 (voorspelde bèta's, 1966–1999) | 3,6, $t = 2{,}06$ (1968–2025) |
| alpha vóór publicatie (% per jaar) | | 5,4, $t = 2{,}72$ (1968–2003) |
| alpha na publicatie (% per jaar) | — | $-0{,}81$, standaardfout 3,03, $t = -0{,}27$ (2004–2025) |

Gedeeltelijk geslaagd. Het teken van $g_2$, de crisismaanden en de correlatie met het
marktrendement komen uit zoals verwacht, en de Roll-maat is in ruim een derde van de
aandeel-jaren ongedefinieerd. Dat $g_1 > 0$ niet uitkomt en de premie kleiner is dan
gepubliceerd, lag binnen de verwachting. Dat de premie na 2003 niet meer te zien is,
hadden we niet voorzien.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De microstructuurtheorie verklaart waarom er een spread is
zonder dat iemand kosten maakt en waarom grote orders de prijs bewegen. Ze verklaart ook
waarom prijzen voor het publiek een martingaal zijn terwijl insiders winst maken, en ze
zegt hoeveel private informatie in de prijs komt, de helft in één ronde en alles bij
doorlopende handel.
Daarmee kreeg de efficiënte markt een mechanisme, en via Amihud en Pástor-Stambaugh raakte
de handelsvloer verbonden met verwachte rendementen. Dat illiquiditeit in crises piekt en
samengaat met lage gelijktijdige rendementen, is robuust.

**Waar het breekt.** Het model breekt niet in zijn logica, maar bij de meting. De
Roll-maat is in ruim een derde van de aandeel-jaren
ongedefinieerd en elders opgeblazen, omdat ze alle negatieve autocorrelatie als spread
leest en alleen negatieve schattingen meetellen. ILLIQ meet Kyles $\lambda$ bovendien
alleen met veel
ruis. De premie op liquiditeitsrisico is in de twee decennia na publicatie in de
eigen factor van Pástor en Stambaugh niet meer te zien, en de standaardfout is daar te
groot om iets uit te sluiten.

**Risico of vergissing?** In de Chicago-lezing is illiquiditeit een kost die rationele
beleggers in de prijs verwerken, en liquiditeitsrisico een toestandsvariabele die in
slechte tijden toeslaat. Houders van illiquide activa verzekeren in die lezing de markt
en worden daarvoor betaald, zodat het risico na 2003 kleiner was of we alleen ruis zien.
In de
Yale-lezing is
illiquiditeit een vorm van de *limits of arbitrage* uit [](#04-23-behavioral). Prijzen
wijken af omdat arbitrageurs de posities niet kunnen volhouden, en de premie verdwijnt
zodra genoeg kapitaal de kans ziet, zoals McLean en Pontiff voor gepubliceerde anomalieën
vonden ([](#06-34-factor-zoo)).

Een risicopremie vergoedt verliezen in crises en een vergissing verdwijnt na publicatie,
maar onze replicatie laat beide zien en beslist de vraag dus niet. Santa-Clara's
praktijkles past op beide lezingen, want wie illiquide activa houdt, kan ze volgens hem
niet zomaar verkopen tegen de prijs uit de laatste waardering
{cite}`SantaClara2026`.

**Wat er daarna kwam.** De volgende vraag is wie die handelskosten betaalt en wie eraan
verdient. [](#04-25-industrie) zoekt het antwoord in de beleggingsindustrie, van actieve
fondsen die hun informatievoordeel moeten terugverdienen tot indexfondsen die zo weinig
mogelijk handelen.

## Oefeningen

:::{exercise}
:label: ex-microstructuur-1

**De spread na een reeks orders.** Neem de Glosten-Milgrom-markt uit het toy-voorbeeld. De prior is
$\pi_0 = \tfrac12$ en $\Delta V = 4$ euro.

1. Laat met [](#eq-microstructuur-gm-spread) zien dat de spread maximaal is bij
   $\pi = \tfrac12$, en bereken hem bij $\mu = 0{,}2$ en $\mu = 0{,}5$.
2. Bij $\mu = 0{,}5$ komen er drie kooporders achter elkaar. Bereken met de hand het
   oordeel $\pi_3$ en de koersen voor elke order, en controleer met code.
3. Hoeveel kooporders op rij zijn er bij $\mu = 0{,}2$ nodig voordat de spread onder
   $0{,}10$ euro zakt?
:::

:::{solution} ex-microstructuur-1
:class: dropdown

**(1)** Met $z = (2\pi-1)^2$ is $4\pi(1-\pi) = 1 - z$ en de spread
$\mu\Delta V(1-z)/(1-\mu^2 z)$. Die daalt in $z$ omdat $\mu^2 < 1$, dus het maximum ligt bij
$\pi = \tfrac12$, met spread $\mu\Delta V$, dus $0{,}80$ en $2{,}00$.

**(2)** Bij $\mu = 0{,}5$ is de likelihoodratio van een koop $0{,}75/0{,}25 = 3$, zodat de
odds $\pi/(1-\pi)$ van 1 naar 3, 9 en 27 gaan en $\pi_3 = 27/28 = 0{,}9643$.

```{code-cell} ipython3
belief_path, rows = 0.5, []
for k in range(1, 4):
    b, a = gm_quotes(belief_path, 0.5, V_H, V_L)
    belief_path = belief_path * 0.75 / (belief_path * 0.75 + (1 - belief_path) * 0.25)
    rows.append({"order": k, "bid vóór order": b, "ask vóór order": a, "oordeel na koop": belief_path})
print(pd.DataFrame(rows).round(4).to_string(index=False))

belief_path, n_buys = 0.5, 0
bid, ask = gm_quotes(belief_path, 0.2, V_H, V_L)
while ask - bid >= 0.10:
    belief_path = belief_path * 0.6 / (belief_path * 0.6 + (1 - belief_path) * 0.4)
    n_buys += 1
    bid, ask = gm_quotes(belief_path, 0.2, V_H, V_L)
print(f"\n(3) bij mu = 0.2: spread onder 0.10 na {n_buys} kooporders op rij (oordeel {belief_path:.4f})")
```

**(3)** Elke koop vermenigvuldigt de odds met $1{,}5$, en na negen kooporders op rij is de
spread onder $0{,}10$. Het tempo van prijsontdekking hangt dus af van de informatieve
waarde van één order, de likelihoodratio $(1+\mu)/(1-\mu)$.
:::

:::{exercise}
:label: ex-microstructuur-2

**Meer ruis, zelfde informatie.** Neem de Kyle-markt uit het toy-voorbeeld. Het volume van de
noise traders verdubbelt, terwijl $\sigma_v = 4$ blijft.

1. Leid uit [](#eq-microstructuur-kyle) af hoe $\beta$, $\lambda$, de verwachte
   insiderwinst en $\Var(v\mid p)$ veranderen als $\sigma_u$ verdubbelt naar $20\,000$.
2. Simuleer $200\,000$ markten voor beide waarden van $\sigma_u$ en controleer dat.
3. Wat is de verwachte $t$-waarde van de gemiddelde insiderwinst over twintig
   onafhankelijke handelsdagen, en hangt die af van $\sigma_u$?
:::

:::{solution} ex-microstructuur-2
:class: dropdown

**(1)** De winst en $\beta$ zijn evenredig met $\sigma_u$, $\lambda$ is er omgekeerd
evenredig mee en $\Var(v\mid p) = \tfrac12\sigma_v^2$ hangt er niet van af. Bij
$\sigma_u = 20\,000$ is dus $\beta = 5000$, $\lambda = 0{,}0001$, de verwachte winst
$40\,000$ en $\Var(v\mid p) = 8$. De simulatie hieronder controleert dat.

```{code-cell} ipython3
n_markets = 200_000
rows = {}
for s_u in (10_000.0, 20_000.0):
    b_k, l_k = s_u / 4.0, 4.0 / (2 * s_u)
    v_sim = rng.normal(0.0, 4.0, n_markets)
    u_sim = rng.normal(0.0, s_u, n_markets)
    y_sim = b_k * v_sim + u_sim
    p_sim = l_k * y_sim
    gain = b_k * v_sim * (v_sim - p_sim)
    slope = np.cov(v_sim, y_sim)[0, 1] / np.var(y_sim)
    rows[f"sigma_u = {s_u:,.0f}"] = {
        "lambda (regressie v op y)": slope,
        "gemiddelde winst insider": gain.mean(),
        "Var(v | p)": np.var(v_sim - p_sim),
        "t-waarde na 20 dagen": np.sqrt(20) * gain.mean() / gain.std(),
    }
pd.DataFrame(rows).round(5)
```

De winst en de standaarddeviatie daarvan schalen allebei met $\sigma_u$, zodat de
$t$-waarde na twintig dagen, ongeveer 2,6, niet van $\sigma_u$ afhangt. Ze ligt onder de
4,1 bij vijftig ronden, omdat de insider daar zijn informatie over de tijd spreidt en per
eenheid risico meer verdient. Een insider in een
drukke markt verdient meer, maar valt statistisch niet meer op.
:::

:::{exercise}
:label: ex-microstructuur-3

**Hoe stabiel is de liquiditeitspremie?** Schat met `ps["traded_liq"]` en `factors4` de
vierfactor-alpha in voortschrijdende vensters van 120 maanden, met
Newey-West-standaardfouten (6 lags) en een 95%-betrouwbaarheidsinterval. In hoeveel
procent van de vensters is de alpha significant positief, en hoeveel jaar data is er nodig
om een ware alpha van 3% per jaar met $t = 2$ te zien?
:::

:::{solution} ex-microstructuur-3
:class: dropdown

```{code-cell} ipython3
traded = ps["traded_liq"].dropna()
window_rows = []
for end in range(120, len(traded) + 1, 12):
    y = traded.iloc[end - 120:end]
    fit = hap.stats.newey_west(y, factors4.reindex(y.index), lags=6)
    alpha_ann, se_ann = 1200 * fit.params["const"], 1200 * fit.bse["const"]
    window_rows.append({"venster eindigt": f"{y.index[-1]:%Y-%m}", "alpha (% p.j.)": alpha_ann,
                        "ondergrens 95%": alpha_ann - 1.96 * se_ann, "bovengrens 95%": alpha_ann + 1.96 * se_ann})
windows = pd.DataFrame(window_rows).set_index("venster eindigt")

full_fit = hap.stats.newey_west(traded, factors4.reindex(traded.index), lags=6)
resid_vol_ann = np.sqrt(12) * full_fit.resid.std()
years_needed = (2 * resid_vol_ann / 0.03) ** 2
print(f"fractie vensters met ondergrens > 0: {(windows['ondergrens 95%'] > 0).mean():.0%}")
print(f"residuele volatiliteit: {resid_vol_ann:.1%} per jaar; jaren nodig voor t = 2 bij alpha = 3%: {years_needed:.0f}")
windows.iloc[::5].round(2)
```

De intervallen van tien jaar zijn ongeveer vijftien procentpunt breed, en slechts een
vijfde van de vensters ligt volledig boven nul. Met een residuele volatiliteit van 12,6%
per jaar is ruim zeventig jaar data nodig om een premie van 3% met $t = 2$ te zien. De
premie rust dus op het gemiddelde van een halve eeuw, en geen enkel decennium kan die op
zich bevestigen of weerleggen.
:::
