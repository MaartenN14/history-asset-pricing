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

(02-09-black-scholes)=

# Black-Scholes-Merton en de CBOE

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1961–1973.

**Wat we al weten.** Bachelier leidde in [](#01-02-bachelier) de eerste
optieformule af door een verwachting te nemen. Waarom een verwachting zonder
correctie voor risico de prijs is, kon hij niet zeggen. Het CAPM uit [](#02-08-capm) gaf een prijs van
risico, maar vroeg daarvoor het verwachte rendement, het slechtst meetbare getal
van de reeks.

**Welke vraag staat open.** Kan een optie gewaardeerd worden zonder dat we weten welk rendement het aandeel verwacht? Speelt het dan nog een rol hoe risicoavers beleggers zijn?
```

## Overzicht

Wat is een optie waard als niemand weet welk rendement het aandeel verwacht? Ze is
evenveel waard als het kost om de optie met aandeel en obligatie na te maken, en die
kosten hangen af van de volatiliteit, maar niet van het verwachte rendement en ook niet
van de risicoaversie. In dit college:

- maken we in een binomiale boom van drie stappen een call na, en zien we dat de
  kans op een stijging nergens in de prijs voorkomt;

- leiden we met het lemma van Itô de partiële differentiaalvergelijking af, en daaruit
  de Black-Scholes-formule als verdisconteerde verwachting;

- berekenen we wat een handelaar verdient die met de verkeerde volatiliteit hedget;

- simuleren we hoe groot de spreiding van de P&L (winst of verlies) is als niet continu
  maar dagelijks,
  wekelijks of maandelijks wordt gehedgd;

- repliceren we de *smirk* van Rubinstein {cite}`Rubinstein1994` (opties met een
  lage uitoefenprijs zijn relatief duur) op opties op SPY, een beursfonds dat de
  S&P 500 volgt. Daarna zetten we de VIX, de volatiliteitsindex die de CBOE uit
  indexopties afleidt, naast de daarna gerealiseerde volatiliteit.

In de jaren zestig rekenden Sprenkle {cite}`Sprenkle1961`, Boness
{cite}`Boness1964` en Samuelson {cite}`Samuelson1965b` de verwachte opbrengst van
een optie uit, maar ze bleven alle drie zitten met een verwacht rendement of een
discontovoet die niemand kon meten. In 1973 verschenen het artikel van Fischer
Black en Myron Scholes {cite}`BlackScholes1973` en dat van Robert Merton
{cite}`Merton1973`, en in april van dat jaar opende in Chicago de CBOE, de eerste beurs
voor gestandaardiseerde opties. Hun formule was de eerste waarderingsregel die niet uit
evenwicht volgt maar uit *replicatie* (namaken met andere effecten).

Black-Scholes is een theorie die zich laat toetsen, maar een relatieve, want ze zegt niet
wat een aandeel waard is, alleen wat een optie waard is *gegeven* het aandeel. Daarom
breekt ze ook op een andere
plek dan het CAPM, namelijk niet in het gemiddelde maar in de volatiliteit, en die is goed
meetbaar.

## Intuïtie: waarom zou dit waar zijn?

Black legde het idee zelf uit met een getal {cite}`Black1989`. Stel dat een call
vijftig cent stijgt als het aandeel een dollar stijgt, en vijftig cent daalt als het aandeel
een dollar daalt. Een handelaar verkoopt dan twee calls en koopt één aandeel. Wat hij op het
aandeel wint, verliest hij op de calls, en omgekeerd, zodat zijn positie voor kleine
bewegingen zonder risico is.

Een positie zonder risico moet de rente opleveren, want anders leent iedereen geld om de
positie op te zetten, of neemt iedereen juist de omgekeerde positie in. Daarmee ligt ook
de prijs van de call vast.

Belangrijk is vooral wat er niet in de redenering zit, zoals de vraag of het aandeel
waarschijnlijk stijgt. Een optimistische verwachting zit al in de koers van het aandeel en
hoeft dus niet nog eens in de optie. Ook risicoaversie speelt geen rol, omdat de gehedgde
positie geen risico heeft.

Wel van belang is hoe hard het aandeel beweegt, omdat de verhouding van twee calls op één
aandeel maar even klopt. Na elke beweging moet de handelaar bijstellen, en hoe wilder het
aandeel, hoe meer dat bijstellen kost. Daarom is de volatiliteit de enige grootheid over
de toekomst die de markt moet inschatten.

Uit deze redenering volgen drie voorspellingen. De prijs van een optie stijgt met de
volatiliteit, maar verandert niet als het verwachte rendement verandert. Een handelaar die
vaak bijstelt, houdt een kleine P&L over die gemiddeld vrijwel nul is, ongeacht de drift.
Als het model klopt, geven ten slotte alle opties op hetzelfde aandeel dezelfde
volatiliteit terug.

## Toy-voorbeeld: een binomiale boom van drie stappen

De eerste cel laadt de pakketten voor het hele college.

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

**Opzet.** Een aandeel stijgt per stap met factor $u$ of daalt met factor $d$, en een
Europese call (alleen op de einddatum uit te oefenen) met uitoefenprijs $K$ loopt na drie
stappen af. De werkelijke kans op een stijging, $p$, laten we open.

| grootheid | waarde |
|---|---|
| koers nu $S_0$ | 100 |
| stijgfactor $u$ / daalfactor $d$ | 1,1 / 0,9 |
| risicovrij bruto rendement per stap $R^{f}$ | 1,02 |
| uitoefenprijs $K$ | 100 |

De tabel hieronder geeft de koers in elke knoop. In de laatste rij staat de payoff na drie
stappen.

| stap | koersen (van veel naar weinig stijgingen) |
|---|---|
| 0 | 100 |
| 1 | 110; 90 |
| 2 | 121; 99; 81 |
| 3 | 133,1; 108,9; 89,1; 72,9 |
| payoff $(S_3 - K)^{+}$ | 33,1; 8,9; 0; 0 |

**Het recept.** In elke knoop zoeken we $\Delta$ aandelen en $B$ dollar in
obligaties die in beide volgende knopen de waarde van de optie geven. Dan is $\Delta = (C_{\text{op}} - C_{\text{neer}})/(S(u-d))$,
de uitslag van de optie gedeeld door die van het aandeel, en vullen de obligaties aan tot
de payoff, zodat $B = (C_{\text{op}} - \Delta S u)/R^{f}$. De optie kost daarom evenveel
als die portefeuille, $\Delta S + B$.

**Stap 1: knoop $S_2 = 121$.** Hier is $\Delta = (33{,}1 - 8{,}9)/24{,}2 = 1$ en
$B = (33{,}1 - 133{,}1)/1{,}02 = -98{,}0392$. De portefeuille, en dus de optie, is daar
$121 - 98{,}0392 = 22{,}9608$ waard.

**Stap 2: knoop $S_2 = 99$.** Nu is $\Delta = 8{,}9/19{,}8 = 0{,}4495$ en $B = (8{,}9 - 0{,}4495 \cdot 108{,}9)/1{,}02 = -39{,}2647$,
zodat de optie $5{,}2353$ waard is. In $S_2 = 81$ is alles nul, omdat geen pad vanuit die
knoop boven $K$ eindigt.

**Stap 3: een stap terug.** In $S_1 = 110$ is $\Delta = (22{,}9608 - 5{,}2353)/22 = 0{,}8057$
en $B = -73{,}0681$, dus is de optie daar $15{,}5594$ waard. In $S_1 = 90$ is $\Delta = 5{,}2353/18 = 0{,}2908$
en $B = -23{,}0969$, met een waarde van $3{,}0796$.

**Stap 4: de wortel.** In de wortel is $\Delta_0 = (15{,}5594 - 3{,}0796)/20 = 0{,}62399$
en $B_0 = -52{,}0388$. De call kost vandaag dus $C_0 = 100\,\Delta_0 + B_0 = 62{,}3991 -
52{,}0388 = 10{,}3603$.

**Stap 5: waar $p$ bleef.** De kans $p$ is in geen enkele stap gebruikt. Neem nu $q = (R^{f} - d)/(u - d) = 0{,}6$,
want onder $q$ verdient het aandeel precies de rente, $0{,}6 \cdot 1{,}1 + 0{,}4 \cdot 0{,}9 =
1{,}02$. De verdisconteerde verwachting onder $q$ geeft dan dezelfde prijs, $(0{,}216
\cdot 33{,}1 + 0{,}432 \cdot 8{,}9)/1{,}02^3 = 10{,}3603$.

**Stap 6: de oude methode.** Sprenkle en Boness namen de verwachte payoff onder de
werkelijke kans. Bij $p = 0{,}5$ is die $7{,}475$, tegen de rente verdisconteerd
$7{,}0439$, en bij $p = 0{,}8$ is ze $20{,}3648$, verdisconteerd $19{,}1902$. Om op
$10{,}3603$ uit te komen, is dus bij elke $p$ een andere discontovoet nodig. Bij $p = 0{,}8$
verwacht de
optie per stap een bruto rendement van $(20{,}3648/10{,}3603)^{1/3} = 1{,}2527$, terwijl
het aandeel $0{,}8 \cdot 1{,}1 + 0{,}2 \cdot 0{,}9 = 1{,}06$ verwacht.

De code loopt de boom achteruit door en zet de handberekening ernaast.

```{code-cell} ipython3
toy = dict(S0=100.0, u=1.1, d=0.9, R_f=1.02, K=100.0, n=3)
S0, u, d, R_f, K, n = toy["S0"], toy["u"], toy["d"], toy["R_f"], toy["K"], toy["n"]
q_toy = (R_f - d) / (u - d)

value, delta_at, bond_at = {}, {}, {}
for j in range(n + 1):                          # terminal nodes, j = number of up-moves
    value[(n, j)] = max(S0 * u**j * d ** (n - j) - K, 0.0)
for step in range(n - 1, -1, -1):               # walk back through the tree
    for j in range(step + 1):
        S = S0 * u**j * d ** (step - j)
        up, down = value[(step + 1, j + 1)], value[(step + 1, j)]
        delta_at[(step, j)] = (up - down) / (S * (u - d))
        bond_at[(step, j)] = (up - delta_at[(step, j)] * S * u) / R_f
        value[(step, j)] = delta_at[(step, j)] * S + bond_at[(step, j)]

payoff_toy = np.array([value[(n, j)] for j in range(n + 1)])
up_moves = np.arange(n + 1)
expected_payoff = {p: stats.binom.pmf(up_moves, n, p) @ payoff_toy for p in (0.5, q_toy, 0.8)}

hand = {"Delta in S2 = 121": 1.0, "B in S2 = 121": -98.0392, "Delta_0": 0.6240, "B_0": -52.0388,
        "C_0 (replicatie)": 10.3603, "q": 0.6, "C_0 (verwachting onder q)": 10.3603,
        "p = 0,5: E_p[payoff] / R_f^3": 7.0439, "p = 0,8: E_p[payoff] / R_f^3": 19.1902,
        "p = 0,8: rendement optie per stap": 1.2527}
code = {"Delta in S2 = 121": delta_at[(2, 2)], "B in S2 = 121": bond_at[(2, 2)],
        "Delta_0": delta_at[(0, 0)], "B_0": bond_at[(0, 0)], "C_0 (replicatie)": value[(0, 0)],
        "q": q_toy, "C_0 (verwachting onder q)": expected_payoff[q_toy] / R_f**n,
        "p = 0,5: E_p[payoff] / R_f^3": expected_payoff[0.5] / R_f**n,
        "p = 0,8: E_p[payoff] / R_f^3": expected_payoff[0.8] / R_f**n,
        "p = 0,8: rendement optie per stap": (expected_payoff[0.8] / value[(0, 0)]) ** (1 / n)}
pd.DataFrame({"met de hand": hand, "code": code}).round(4)
```

De twee kolommen zijn gelijk, en daarmee staat het argument van dit college al in het
klein op tafel. De prijs $10{,}3603$ volgt uit namaken, en het verwachte rendement van
aandeel en optie mag elke waarde hebben zonder dat die prijs verandert.

## Theorie

We leiden vier dingen af. Eerst hebben we het lemma van Itô nodig, de rekenregel voor
functies van een Brownse beweging. Daarna volgt de kern, de delta-hedge, die in continue
tijd doet wat de boom per knoop deed en daardoor een partiële differentiaalvergelijking
zonder $\mu$ oplevert. De oplossing daarvan is de Black-Scholes-formule, en uit dezelfde
vergelijking volgt ook wat een handelaar verdient die de verkeerde volatiliteit gebruikt.
Tot slot toetsen we het model met de implied volatility.

### Opzet en aannames

We wijken op vier punten af van de notatietabel van de reeks. De aandelenkoers heet $S_t$
in plaats van $p_t$, zoals in de optieliteratuur, en in de boom was $R^{f}$ het bruto
rendement per stap (1,02), niet de netto rente. Verder is $r$ hier de continu
samengestelde rente en geen netto rendement, zodat een dollar in een jaar groeit tot
$e^{r}$. Ook $d$ is in de boom de daalfactor en niet het dividend, terwijl een dividend
hier $\delta$ heet, als rendement op de koers. $C(S,t)$ en $P(S,t)$ zijn de waarden van
een call en een put, en $\tau = T - t$ is de resterende looptijd. We maken vier aannames:

1. het aandeel volgt een *geometrische Brownse beweging* (de logaritme van de koers
   is een Brownse beweging met drift), met constante volatiliteit $\sigma$, zoals in de
   vergelijking onder deze lijst;

2. de rente $r$ is continu samengesteld en constant;

3. handel is continu en zonder transactiekosten, en short verkopen is toegestaan;

4. het aandeel keert geen dividend uit.

```{math}
:label: eq-black-scholes-gbm
\mathrm{d}S_t = \mu\, S_t\, \mathrm{d}t + \sigma\, S_t\, \mathrm{d}W_t .
```

Volgens [](#eq-black-scholes-gbm) groeit de koers gemiddeld met $\mu$ per jaar,
bijvoorbeeld 10%, en schommelt hij met $\sigma$ per jaar, bijvoorbeeld 20%. De schok
$\mathrm{d}W_t$ is die van een Brownse beweging en werkt evenredig met de koers. Dit
koersproces is dat van Bachelier, met de correctie van Osborne {cite}`Osborne1959` en
Samuelson {cite}`Samuelson1965b`, waardoor de koers positief blijft.

### Het gereedschap: het lemma van Itô

Het lemma van Itô zegt hoe een functie van de koers, bijvoorbeeld de waarde van een optie,
meebeweegt als de koers beweegt. Voor gladde paden telt alleen de eerste afgeleide, maar
een Brownse beweging schudt zo hard dat het kwadraat van de uitslag even groot is als de
drift. Volgens Regnaults wet uit [](#01-02-bachelier) is de uitslag over een interval $h$
namelijk van orde $\sqrt{h}$, en het kwadraat dus van orde $h$. Daardoor telt ook de
kromming van de functie mee, en bij een bolle functie duwt die kromming de waarde omhoog.

:::{prf:theorem} Het lemma van Itô
:label: thm-black-scholes-ito

Laat $\mathrm{d}X_t = a_t\,\mathrm{d}t + b_t\,\mathrm{d}W_t$ en laat $f(x,t)$ twee
keer continu differentieerbaar zijn in $x$ en één keer in $t$. Dan geldt

```{math}
:label: eq-black-scholes-ito
\mathrm{d}f(X_t,t) = \Bigl(f_t + a_t f_x + \tfrac12 b_t^2 f_{xx}\Bigr)\mathrm{d}t
                    + b_t f_x \,\mathrm{d}W_t .
```
:::

In woorden: de verandering van $f$ is de gewone kettingregel plus een term
$\tfrac12 b^2 f_{xx}$, de kromming maal de variantie van de schok. Die extra term ontstaat
omdat de som van gekwadrateerde aangroeiingen van $W$ over $[0,t]$ naar de vaste waarde
$t$ convergeert, zodat $(\mathrm{d}W)^2 = \mathrm{d}t$.

:::{prf:proof}
:class: dropdown

Neem constante $a$ en $b$, verdeel $[0,t]$ in $n$ stukjes van lengte $h = t/n$ en
ontwikkel $f$ tot de tweede orde in elk stukje. In
$(\delta X_j)^2 = a^2h^2 + 2ab\,h\,\delta W_j + b^2(\delta W_j)^2$ verdwijnen de
eerste twee termen na sommatie over $n = t/h$ stukjes. Voor
$Q_n = \sum_j (\delta W_j)^2$ (met $\delta W_j$ de aangroei in stukje $j$) geldt $\E[Q_n] = t$ en, omdat
$\Var((\delta W_j)^2) = 2h^2$ en de stukjes onafhankelijk zijn,
$\Var(Q_n) = 2th \to 0$. De som van gekwadrateerde aangroeiingen convergeert dus in
$L^2$ naar de *deterministische* waarde $t$: $(\mathrm{d}W)^2 = \mathrm{d}t$. Met
$f_{xx}$ als gewicht geeft hetzelfde argument
$\sum_j f_{xx}(\delta W_j)^2 \to \int f_{xx}\,\mathrm{d}s$, en de restterm van orde
$h^{3/2}$ per stukje verdwijnt. $\square$
:::

Een eerste toepassing is $f = \log S$, waarvoor geldt dat
$\mathrm{d}\log S_t = (\mu - \tfrac12\sigma^2)\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$.
Het verwachte log-rendement ligt dus $\tfrac12\sigma^2$ onder $\mu$, bij $\sigma = 20\%$
twee procentpunt, en dat is precies het verschil tussen rekenkundig en meetkundig
gemiddelde uit [](#00-01-rendementen). Over een looptijd $\tau$ is $\log S_T$ normaal
verdeeld, zodat de koers op expiratie lognormaal is.

### Het kernresultaat: de delta-hedge

*Waarom zou dit waar zijn?* Een handelaar houdt een optie en verkoopt er een aantal
aandelen tegenover. Omdat de optie en het aandeel door dezelfde schok worden gedreven,
heft die schok zich op als hij het aantal aandelen goed kiest. Er blijft dan een positie
zonder risico over, en die moet de rente verdienen. Met de schok verdwijnt ook $\mu$,
want de verkochte aandelen hebben precies de verwachte stijging $\mu S C_S\,\mathrm{d}t$
van de optie tegenover zich.

Het lemma van Itô met $a = \mu S$ en $b = \sigma S$ geeft de beweging van de call:
$\mathrm{d}C = (C_t + \mu S C_S + \tfrac12\sigma^2S^2C_{SS})\,\mathrm{d}t +
\sigma S C_S\,\mathrm{d}W$. De handelaar vormt de positie $\Pi = C - \Delta S$, die over een kort interval verandert met

$$
\mathrm{d}\Pi
 = \Bigl(C_t + \mu S\, C_S + \tfrac12\sigma^2 S^2 C_{SS} - \mu S \Delta\Bigr)\mathrm{d}t
   + \sigma S\bigl(C_S - \Delta\bigr)\mathrm{d}W .
$$

Met $\Delta = C_S$ verdwijnen de $\mathrm{d}W$-term en beide termen met $\mu$, en dat is
het recept uit de boom, maar dan met een afgeleide in plaats van een verschilquotiënt. De
rest, $\mathrm{d}\Pi = (C_t + \tfrac12\sigma^2S^2C_{SS})\,\mathrm{d}t$,
is zonder risico. Omdat arbitrage niet mag bestaan, moet die rest de rente verdienen, dus
$\mathrm{d}\Pi = r(C - SC_S)\,\mathrm{d}t$. Gelijkstellen van beide uitdrukkingen geeft

```{math}
:label: eq-black-scholes-pde
\frac{\partial C}{\partial t} + r S \frac{\partial C}{\partial S}
 + \frac12 \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} - r C = 0,
\qquad C(S,T) = (S - K)^{+} .
```

In de vergelijking heffen tijdsverval, groei tegen de rente en kromming maal variantie
elkaar op, en $\mu$ komt er niet in voor. De intuïtie had dus gelijk, want twee beleggers
die het oneens zijn over $\mu$ maar eens over $\sigma$, komen op dezelfde prijs. De stap
waarin $\Delta$ vastgehouden wordt, steunt op aanname 3, continue handel. Formeel vraagt
die stap een *zelffinancierende* strategie (aanpassingen van de aandelenpositie worden uit
de obligatiepositie betaald), en Merton maakte dat exact en vond dezelfde vergelijking
{cite}`Merton1973`.

```{note}
Black en Scholes vonden de vergelijking eerst via het CAPM uit [](#02-08-capm). De
bèta van de optie is $\beta_{C,\text{mkt}} = (SC_S/C)\,\beta_{S,\text{mkt}}$, met "mkt" de markt (de letter $m$ is
in de reeks de stochastische discontofactor). Laten we het CAPM gedurende de hele looptijd van de optie gelden, dan valt de marktpremie weg. Merton liet zien dat arbitrage alleen al volstaat, en hij bewees ook zonder model dat een call minstens
$\max(0, S - Ke^{-r\tau})$ waard is. Een Amerikaanse call (op elk moment uit te oefenen) op
een aandeel zonder dividend wordt daarom nooit vroeg uitgeoefend, want verkopen levert meer op.
```

### Wat het voorspelt: de Black-Scholes-formule

De Black-Scholes-formule volgt als we de prijs als verwachting schrijven. De vergelijking
[](#eq-black-scholes-pde) is namelijk dezelfde als in een wereld waarin het aandeel met
$r$ groeit in plaats van met $\mu$, en in die wereld is de prijs de verdisconteerde
verwachte payoff, net als in de boom onder $q$. Omdat de vergelijking in beide werelden
dezelfde is, is de prijs dat ook.

De kansen in die wereld heten de *risiconeutrale kansmaat* $\mathbb{Q}$ (de kansen
waaronder elk verhandeld activum de rente verdient). Deze kansmaat is de maat $Q$ uit
[](#thm-efficiente-markten-martingaal), waaronder prijzen na verdisconteren met de rente
martingalen zijn, en in de boom was dat de kans $q = 0{,}6$ in plaats van de werkelijke
$p$. Onder $\mathbb{Q}$ verandert alleen de drift, want $\mu$ wordt $r$ en $\sigma$ blijft
gelijk. De Brownse beweging die bij die kansen hoort, is $W^{\mathbb{Q}}_t = W_t + (\mu - r)t/\sigma$.
De werkelijke kansen zijn niet fout, maar voor de prijs spelen ze geen rol, omdat de PDE
ze niet bevat.

:::{prf:proposition} Feynman-Kac (informeel)
:label: thm-black-scholes-feynman-kac

Laat onder $\mathbb{Q}$ gelden dat $\mathrm{d}S_s = rS_s\,\mathrm{d}s
+ \sigma S_s\,\mathrm{d}W^{\mathbb{Q}}_s$. Als $C$ [](#eq-black-scholes-pde) oplost
en voldoende regelmatig is, dan

```{math}
:label: eq-black-scholes-rn
C(S,t) = e^{-r\tau}\,\E^{\mathbb{Q}}\!\left[(S_T - K)^{+} \,\middle|\, S_t = S\right].
```
:::

:::{prf:proof}
Laat $M_s = e^{-r(s-t)} C(S_s, s)$ de verdisconteerde optiewaarde zijn. Het lemma van Itô onder $\mathbb{Q}$ geeft

$$
\mathrm{d}M_s = e^{-r(s-t)}\Bigl(C_t + rS\,C_S + \tfrac12\sigma^2S^2 C_{SS} - rC\Bigr)\mathrm{d}s
               + e^{-r(s-t)}\sigma S\,C_S\,\mathrm{d}W^{\mathbb{Q}}_s .
$$

De $\mathrm{d}s$-term is nul door [](#eq-black-scholes-pde), dus $M$ is een martingaal. Daarom is $C(S,t) = M_t = \E^{\mathbb{Q}}[M_T] = e^{-r\tau}\E^{\mathbb{Q}}[(S_T-K)^{+}]$.
$\square$
:::

De prijs is dus Bacheliers verwachting, maar dan onder de kansen waarin het aandeel de
rente verdient. Bachelier had de berekening, terwijl Black, Scholes en Merton de
rechtvaardiging hadden. Als we die verwachting uitrekenen onder een lognormale $S_T$ en
daarbij aanname 1 gebruiken, een constante $\sigma$, volgt de formule.

:::{prf:theorem} De Black-Scholes-formule
:label: thm-black-scholes-formule

De waarde van een Europese call is

```{math}
:label: eq-black-scholes-call
C(S,t) = S\,\Phi(d_1) - K e^{-r\tau}\,\Phi(d_2),
\qquad
d_{1} = \frac{\log(S/K) + (r + \tfrac12\sigma^2)\tau}{\sigma\sqrt{\tau}},
\qquad d_2 = d_1 - \sigma\sqrt{\tau},
```

met $\Phi$ de standaardnormale verdelingsfunctie.
:::

In woorden: de call is een aandeel maal $\Phi(d_1)$ min een lening van
$Ke^{-r\tau}$ maal $\Phi(d_2)$. Daarbij is $\Phi(d_1)$ de delta, het aantal aandelen in de
replicerende portefeuille, en $\Phi(d_2)$ de risiconeutrale kans op uitoefening, die in de
boom $q^3 + 3q^2(1-q) = 0{,}648$ was, bij een delta van $0{,}624$.

:::{prf:proof}
:class: dropdown

Onder $\mathbb{Q}$ is $S_T = S\exp[(r - \tfrac12\sigma^2)\tau + \sigma\sqrt{\tau}Z]$
met $Z \sim \mathcal{N}(0,1)$, en de call wordt uitgeoefend als $Z > -d_2$. De
tweede term van [](#eq-black-scholes-rn) is dus $Ke^{-r\tau}\Phi(d_2)$. De eerste
is, na het kwadraat af te maken,

$$
e^{-r\tau}\E\!\left[S_T\,\mathbf{1}\{Z > -d_2\}\right]
 = S \int_{-d_2}^{\infty} \frac{e^{-(z - \sigma\sqrt{\tau})^2/2}}{\sqrt{2\pi}}\,\mathrm{d}z
 = S\,\Phi(d_2 + \sigma\sqrt{\tau}) = S\,\Phi(d_1).
$$

Voor de delta vallen bij differentiëren de termen met $\partial d_i/\partial S$
tegen elkaar weg, omdat $S\varphi(d_1) = Ke^{-r\tau}\varphi(d_2)$. $\square$
:::

Uit de formule is af te lezen hoe de prijs op elke invoer reageert. Stijgt $\sigma$, dan
stijgt de call, omdat de kans op een grote uitslag omhoog toeneemt terwijl het verlies
onder $K$ op nul begrensd blijft. Stijgt $r$, dan stijgt de call ook, want de
uitoefenprijs wordt later betaald en is vandaag minder waard. Stijgt $\mu$, dan gebeurt er
niets.

Een tweede voorspelling, de put-call-pariteit, heeft helemaal geen model nodig. Een
gekochte call plus een verkochte put met dezelfde $K$ en $T$ betaalt altijd $S_T - K$, en
dat is ook de payoff van een termijncontract. Wat hetzelfde betaalt, kost hetzelfde,
ongeacht het koersproces.

:::{prf:theorem} Put-call-pariteit
:label: thm-black-scholes-pariteit

Voor Europese opties geldt onder elk koersproces

```{math}
:label: eq-black-scholes-pariteit
C_t - P_t = e^{-r\tau}\,(F_t - K),
```

met $F_t$ de termijnkoers. Zonder dividend is $F_t = S_te^{r\tau}$, en bij een dividendrendement $\delta$ is $F_t = S_te^{(r-\delta)\tau}$.
:::

:::{prf:proof}
Is de linkerkant groter, verkoop dan de call, koop de put en koop het termijncontract.
Dat levert vandaag het verschil op, en op $T$ is de netto payoff
$-(S_T-K)^{+} + (K-S_T)^{+} + S_T - K = 0$. Omgekeerd voor een kleinere linkerkant.
$\square$
:::

Call min put is dus de contante waarde van termijnkoers min uitoefenprijs, en daaruit
volgt de put, $P = Ke^{-r\tau}\Phi(-d_2) - S\Phi(-d_1)$. Omdat de pariteit geen
model gebruikt, halen we er in de replicatie de termijnkoers uit, zonder aanname
over het dividend.

### Wat een hedger verdient

Een handelaar die een optie verkoopt en met de delta hedget, wint of verliest naargelang
het aandeel hard of rustig beweegt. Tegen kleine bewegingen is hij gedekt, maar de optie
is bol in de koers, zodat hij bij een grote beweging, omhoog of omlaag, op de optie meer
verliest dan hij op de aandelen wint. Daartegenover staat het tijdsverval, want de optie
wordt elke dag iets minder waard en dat wint hij. Beweegt het aandeel harder dan de prijs
aannam, dan verliest hij per saldo, en beweegt het rustiger, dan wint hij.

De gevoeligheden van de optieprijs heten de *Greeks*. De tabel hieronder geeft ze voor een
call en een put.

| Greek | definitie | call | put |
|---|---|---|---|
| delta $\Delta$ | $\partial V/\partial S$ | $\Phi(d_1)$ | $\Phi(d_1) - 1$ |
| gamma $\Gamma$ | $\partial^2 V/\partial S^2$ | $\varphi(d_1)/(S\sigma\sqrt{\tau})$ | idem |
| vega $\nu$ | $\partial V/\partial \sigma$ | $S\varphi(d_1)\sqrt{\tau}$ | idem |
| theta $\Theta$ | $\partial V/\partial t$ | $-\frac{S\varphi(d_1)\sigma}{2\sqrt{\tau}} - rKe^{-r\tau}\Phi(d_2)$ | $-\frac{S\varphi(d_1)\sigma}{2\sqrt{\tau}} + rKe^{-r\tau}\Phi(-d_2)$ |
| rho $\rho$ | $\partial V/\partial r$ | $K\tau e^{-r\tau}\Phi(d_2)$ | $-K\tau e^{-r\tau}\Phi(-d_2)$ |

met $\varphi$ de standaardnormale dichtheid. In deze termen luidt
[](#eq-black-scholes-pde) $\Theta + rS\Delta + \tfrac12\sigma^2S^2\Gamma = rV$, zodat het
tijdsverval precies de verwachte winst uit kromming compenseert. Maar wat gebeurt er met
de *P&L* (winst of verlies) van een handelaar die de verkeerde volatiliteit
gebruikt?

:::{prf:proposition} De P&L van een delta-hedge bij de verkeerde volatiliteit
:label: thm-black-scholes-hedge-pnl

Het aandeel volgt [](#eq-black-scholes-gbm) met gerealiseerde volatiliteit $\sigma_g$.
Een handelaar verkoopt een optie tegen de Black-Scholes-prijs bij $\sigma_i$ en hedget
continu met de delta bij $\sigma_i$. Zijn verdisconteerde P&L op $T$ is

```{math}
:label: eq-black-scholes-hedge-pnl
e^{-rT}\,\mathrm{PL}_T = \frac12 \int_0^T e^{-rs}\,\bigl(\sigma_i^2 - \sigma_g^2\bigr)\,
                 S_s^2\,\Gamma_i(S_s,s)\,\mathrm{d}s .
```
:::

De P&L is dus het verschil tussen de variantie in de optieprijs en de gerealiseerde
variantie, gewogen met de gamma langs het pad. Het bewijs trekt de waarde van de optie af
van die van de hedgeportefeuille $H$, waarna de $\mathrm{d}S$-termen wegvallen en de PDE
bij $\sigma_i$ alleen het variantieverschil overlaat.

:::{prf:proof}
:class: dropdown

Laat $V$ de Black-Scholes-waarde bij $\sigma_i$ zijn en $H$ de hedgeportefeuille, met
$H_0 = V_0$ en $\mathrm{d}H = \Delta_i\,\mathrm{d}S + r(H - \Delta_i S)\,\mathrm{d}t$.
Itô onder de werkelijke dynamiek geeft
$\mathrm{d}V = (V_t + \tfrac12\sigma_g^2 S^2\Gamma_i)\,\mathrm{d}t + \Delta_i\,\mathrm{d}S$,
en de PDE bij $\sigma_i$ geeft
$V_t = rV - rS\Delta_i - \tfrac12\sigma_i^2S^2\Gamma_i$. Aftrekken van beide geeft

$$
\mathrm{d}(H - V) = r(H - V)\,\mathrm{d}t
 + \tfrac12\bigl(\sigma_i^2 - \sigma_g^2\bigr)S^2\Gamma_i\,\mathrm{d}t .
$$

De $\mathrm{d}S$-termen vallen weg, want daarvoor dient de hedge. Vermenigvuldigen met $e^{-rt}$
en integreren geeft het resultaat, met $\mathrm{PL}_T = H_T - V_T$ en $V_T$ de payoff.
$\square$
:::

Bij $\sigma_i = \sigma_g$ is de P&L in elk pad nul, want dan is de hedge precies de
replicatie. Verkoopt
de handelaar te duur, dan verdient hij gemiddeld ongeveer de vega maal
$\sigma_i - \sigma_g$. Dat volgt als we $S^2\Gamma$ op de beginwaarde vasthouden, omdat
$\sigma_i^2 - \sigma_g^2 \approx 2\sigma(\sigma_i - \sigma_g)$ en $\sigma S^2\Gamma\tau$
precies de vega uit de tabel is. Voor de call uit het
voorbeeld hieronder geeft dat $19{,}7 \cdot 0{,}05 \approx 0{,}99$ dollar bij vijf
volatiliteitspunten te duur, al hangt het precieze bedrag van het pad af. Een gehedgde
verkoper
van opties verkoopt dus gerealiseerde variantie tegen de prijs $\sigma_i^2$.

### Hoe het getoetst wordt: implied volatility

Het model wordt getoetst via de enige invoer die niet op het scherm staat. Van de vijf
invoergrootheden van de formule zijn er vier af te lezen, namelijk koers, uitoefenprijs,
looptijd en rente, maar $\sigma$ niet. Uit de marktprijs van een optie is $\sigma$ daarom
terug te rekenen, en omdat de prijs stijgt in $\sigma$, hoort bij elke prijs precies één
waarde.

De *implied volatility* $\sigma^{\text{imp}}(K,T)$ is de $\sigma$ die
$C^{\text{BS}}(S,K,T,r,\sigma) = C^{\text{markt}}$ oplost. Klopt het model, dan is
ze voor elke $K$ en $T$ op hetzelfde aandeel gelijk, en dat is een scherpe, falsifieerbare
voorspelling. Zodra handelaren hun prijzen in implied volatility
opgeven, is de formule bovendien een meetlat, waarop ook afwijkingen van het model worden
uitgedrukt.

De code implementeert [](#eq-black-scholes-call), de put via de pariteit en de
Greeks uit de tabel.

```{code-cell} ipython3
def bs_price(S, K, T, r, sigma, kind="call"):
    """Black-Scholes (1973) price of a European call or put on a non-dividend stock."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call = S * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)
    price = np.where(np.asarray(kind) == "call", call, call - S + K * np.exp(-r * T))
    return float(price) if price.ndim == 0 else price


def bs_greeks(S, K, T, r, sigma, kind="call"):
    """Delta, gamma, vega, theta (per year) and rho of a European option."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    pdf, disc = stats.norm.pdf(d1), K * np.exp(-r * T)
    sign = 1.0 if kind == "call" else -1.0
    return {
        "delta": stats.norm.cdf(d1) - (0.0 if kind == "call" else 1.0),
        "gamma": pdf / (S * sigma * np.sqrt(T)),
        "vega": S * pdf * np.sqrt(T),
        "theta": -S * pdf * sigma / (2 * np.sqrt(T)) - sign * r * disc * stats.norm.cdf(sign * d2),
        "rho": sign * T * disc * stats.norm.cdf(sign * d2),
    }
```

`bs_price` geeft de prijs, en omdat de soort ook als array mag komen, waardeert de functie
een hele keten calls en puts in één aanroep, wat de replicatie gebruikt. `bs_greeks` geeft
de vijf gevoeligheden uit de tabel. De inverse in de volgende cel zoekt $\sigma$ met
bisectie, wat werkt omdat de prijs monotoon stijgt in $\sigma$. Is de prijs bij het midden
te laag, dan ligt de oplossing erboven.

```{code-cell} ipython3
def implied_vol(price, S, K, T, r, kind="call", n_iter=60):
    """Invert Black-Scholes for sigma by bisection on arrays; NaN outside the no-arbitrage bounds."""
    lo = np.full(np.shape(price), 1e-4)
    hi = np.full(np.shape(price), 5.0)
    inside = (bs_price(S, K, T, r, lo, kind) <= price) & (price <= bs_price(S, K, T, r, hi, kind))
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        below = bs_price(S, K, T, r, mid, kind) < price
        lo, hi = np.where(below, mid, lo), np.where(below, hi, mid)
    sigma = np.where(inside, 0.5 * (lo + hi), np.nan)
    return float(sigma) if sigma.ndim == 0 else sigma
```

We waarderen een *at-the-money* call en put (uitoefenprijs gelijk aan de koers) op
drie maanden, bij 20% volatiliteit en 4%
rente, en controleren daarna pariteit, PDE en inverse.

```{code-cell} ipython3
example = dict(S=100.0, K=100.0, T=0.25, r=0.04, sigma=0.20)
greeks = pd.DataFrame(
    {kind: {"prijs": bs_price(**example, kind=kind), **bs_greeks(**example, kind=kind)}
     for kind in ("call", "put")}
)
call_g = greeks["call"]
S_ex, K_ex, T_ex, r_ex, sigma_ex = (example[k] for k in ("S", "K", "T", "r", "sigma"))
parity_gap = call_g["prijs"] - greeks.loc["prijs", "put"] - (S_ex - K_ex * np.exp(-r_ex * T_ex))
pde_gap = (call_g["theta"] + r_ex * S_ex * call_g["delta"]
           + 0.5 * sigma_ex**2 * S_ex**2 * call_g["gamma"] - r_ex * call_g["prijs"])
recovered_sigma = implied_vol(call_g["prijs"], S_ex, K_ex, T_ex, r_ex)
checks = pd.DataFrame({"call": {"pariteitsresidu": parity_gap, "PDE-residu": pde_gap,
                                "teruggevonden sigma": recovered_sigma}})
pd.concat([greeks, checks]).round(4)
```

De call kost $4{,}49$, met delta $0{,}56$ en vega $19{,}7$, zodat één volatiliteitspunt
ongeveer twintig cent waard is. De drie controlerijen onderaan tonen dat pariteitsresidu
en PDE-residu nul zijn en dat
de inverse $\sigma = 0{,}20$ terugvindt.

```{admonition} Samengevat
:class: tip

- Een delta-hedge met $\Delta = C_S$ verwijdert het risico en daarmee $\mu$; de prijs
  volgt [](#eq-black-scholes-pde). In de boom was $\Delta_0 = 0{,}624$.

- De prijs is de verdisconteerde verwachte payoff onder de risiconeutrale kansen,
  [](#eq-black-scholes-rn), en uitgerekend [](#eq-black-scholes-call): $4{,}49$ voor
  de at-the-money call op drie maanden bij $\sigma = 20\%$.

- Een handelaar die met de verkeerde volatiliteit verkoopt, verdient het variantieverschil gewogen
  met gamma, [](#eq-black-scholes-hedge-pnl).

- Het model voorspelt één implied volatility per aandeel, voor elke $K$ en $T$.

- De simulatie hierna meet hoe groot de fout is als niet continu maar $N$ keer wordt gehedgd, en of de drift een spoor nalaat.
```

## Simulatie: discreet hedgen van een verkochte optie

Een handelaar die niet continu maar $N$ keer hedget, houdt een P&L over waarvan de
spreiding daalt met $1/\sqrt{N}$, terwijl de drift van het aandeel daarin vrijwel geen
spoor nalaat. Deze simulatie laat dat zien. Boyle en Emanuel analyseerden die spreiding
als eersten {cite}`BoyleEmanuel1980`, maar we volgen de latere analyse van Derman en
Kamal {cite}`DermanKamal1999`, die de spreiding van de P&L in één vuistregel samenvatten.

```{math}
:label: eq-black-scholes-dk
\SD\bigl(\text{P\&L}\bigr) \;\approx\; \sqrt{\frac{\pi}{4}}\;\frac{\nu\,\sigma}{\sqrt{N}} .
```

De spreiding van de P&L daalt dus met de wortel van het aantal hedgemomenten en is
evenredig met de vega. Dat komt doordat een handelaar met $N$ hedgemomenten de
volatiliteit uit $N$ waarnemingen meet, met een standaardfout van ongeveer
$\sigma/\sqrt{2N}$, die hij maal de vega als winst of verlies boekt. Hij weegt de
gekwadrateerde koersbewegingen daarbij niet gelijk maar met de gamma van dat moment, en een
ongelijk gewogen schatting is onnauwkeuriger dan een gelijk gewogen. Voor een
at-the-money optie levert het gemiddelde van de gekwadrateerde gamma over de looptijd
precies de extra factor $\sqrt{\pi/2}$. Bij de call uit de vorige cel en dagelijks hedgen
($N = 63$) geeft de regel $0{,}44$ dollar.

De functie boekt premie, delta, financiering en payoff, en het aandeel groeit er met $\mu$
en niet met $r$.

```{code-cell} ipython3
def delta_hedge_pnl(n_hedges, n_paths, S0, K, T, r, mu, sigma_true,
                    sigma_price, sigma_hedge=None, kind="call"):
    """Terminal P&L of selling one option at sigma_price and delta-hedging it
    n_hedges times at sigma_hedge while the stock follows GBM with sigma_true."""
    sigma_hedge = sigma_price if sigma_hedge is None else sigma_hedge
    dt = T / n_hedges
    S = np.full(n_paths, S0)
    delta = bs_greeks(S, K, T, r, sigma_hedge, kind)["delta"]
    cash = bs_price(S0, K, T, r, sigma_price, kind) - delta * S
    for i in range(1, n_hedges + 1):
        z = rng.standard_normal(n_paths)
        S = S * np.exp((mu - 0.5 * sigma_true**2) * dt + sigma_true * np.sqrt(dt) * z)
        cash = cash * np.exp(r * dt)
        if i < n_hedges:
            new_delta = bs_greeks(S, K, T - i * dt, r, sigma_hedge, kind)["delta"]
            cash = cash - (new_delta - delta) * S
            delta = new_delta
    payoff = np.maximum(S - K, 0.0) if kind == "call" else np.maximum(K - S, 0.0)
    return cash + delta * S - payoff
```

Eerst controleren we de code op het voorbeeld van Derman en Kamal, een at-the-money call
op één maand ($S_0 = K = 100$, $r = 5\%$, $\sigma = 20\%$) op een aandeel dat met de rente
groeit, met $N = 21$ en $N = 84$ en 50 000 paden.

```{code-cell} ipython3
dk_rows = []
premium_dk = bs_price(100.0, 100.0, 1 / 12, 0.05, 0.20)
vega_dk = bs_greeks(100.0, 100.0, 1 / 12, 0.05, 0.20)["vega"]
for n in (21, 84):
    pnl = delta_hedge_pnl(n, 50_000, 100.0, 100.0, 1 / 12, 0.05, 0.05, 0.20, 0.20)
    dk_rows.append({
        "N": n,
        "gemiddelde P&L": pnl.mean(),
        "SE gemiddelde": pnl.std(ddof=1) / np.sqrt(len(pnl)),
        "SD P&L": pnl.std(ddof=1),
        "SD / premie": pnl.std(ddof=1) / premium_dk,
        "vuistregel": np.sqrt(np.pi / 4) * vega_dk * 0.20 / np.sqrt(n),
    })
dk_table = pd.DataFrame(dk_rows).set_index("N")
dk_table["callpremie"] = premium_dk
dk_table["vega per volatiliteitspunt"] = vega_dk / 100
dk_table.round(4)
```

De gesimuleerde spreiding ligt 1 à 3% onder de vuistregel ($0{,}4295$ tegen $0{,}4432$),
en vier keer zo vaak hedgen halveert de spreiding, want $0{,}4295/0{,}2190 = 1{,}96$. Het
gemiddelde ligt binnen anderhalve standaardfout van nul. Dit controleert de code en is
geen replicatie, want we vergelijken de simulatie met de vuistregel van Derman en Kamal en
niet met de getallen in hun artikel.

Nu komen we bij de eigenlijke vraag. We verkopen de call uit de theorie (drie maanden,
$\sigma = 20\%$, $r = 4\%$) en hedgen dagelijks, wekelijks of maandelijks, terwijl het
aandeel met $\mu = 10\%$ groeit, zodat een effect van de drift zichtbaar zou worden.

```{code-cell} ipython3
T_sim, r_sim, mu_sim, sigma_sim, n_paths = 0.25, 0.04, 0.10, 0.20, 50_000
vega_sim = bs_greeks(100.0, 100.0, T_sim, r_sim, sigma_sim)["vega"]
frequencies = {"dagelijks": 63, "wekelijks": 13, "maandelijks": 3}

pnl_by_freq = {
    name: delta_hedge_pnl(n, n_paths, 100.0, 100.0, T_sim, r_sim, mu_sim, sigma_sim, sigma_sim)
    for name, n in frequencies.items()
}
hedge_table = pd.DataFrame(
    {
        name: {
            "N": frequencies[name],
            "gemiddelde P&L": pnl.mean(),
            "SE gemiddelde": pnl.std(ddof=1) / np.sqrt(n_paths),
            "SD P&L": pnl.std(ddof=1),
            "vuistregel": np.sqrt(np.pi / 4) * vega_sim * sigma_sim / np.sqrt(frequencies[name]),
            "5%-kwantiel": np.quantile(pnl, 0.05),
        }
        for name, pnl in pnl_by_freq.items()
    }
).T
hedge_table.round(4)
```

De spreiding daalt van $1{,}86$ dollar bij maandelijks via $0{,}92$ naar $0{,}43$ bij
dagelijks hedgen. Bij dagelijks hedgen
is het gemiddelde $-0{,}002$, met een standaardfout van $0{,}002$. Bij wekelijks en
maandelijks hedgen is het klein, maar toch statistisch niet nul, met $-0{,}019$ bij
maandelijks en $t \approx -2{,}3$. Dat bedrag is minder dan een half procent van de premie
van $4{,}49$, en of het van de drift of van het discrete hedgen komt, kan deze simulatie
niet scheiden. Het echte risico zit in de staart, want het 5%-kwantiel van de
maandelijkse hedger ligt op $-3{,}25$, bijna driekwart van de premie.

Hoe snel daalt de spreiding? We herhalen de simulatie met 10 000 paden voor zeven
frequenties en schatten de helling van log-spreiding op log-$N$.

```{code-cell} ipython3
n_grid = np.array([3, 6, 13, 26, 63, 126, 252])
sd_grid = np.array([
    delta_hedge_pnl(n, 10_000, 100.0, 100.0, T_sim, r_sim, mu_sim, sigma_sim, sigma_sim).std(ddof=1)
    for n in n_grid
])
slope_sd = np.polyfit(np.log(n_grid), np.log(sd_grid), 1)[0]
grid_table = pd.DataFrame(
    {"SD P&L": sd_grid, "vuistregel": np.sqrt(np.pi / 4) * vega_sim * sigma_sim / np.sqrt(n_grid)},
    index=pd.Index(n_grid, name="N"),
)
grid_table.loc["helling log-log", "SD P&L"] = slope_sd
grid_table.round(4)
```

De helling is $-0{,}48$ en ligt dus dicht bij de $-0{,}5$ van de vuistregel. De figuur
toont links de verdelingen uit de vorige tabel, waarbij het om hun breedte gaat, en rechts
deze zeven punten, waarbij het om de helling gaat.

```{code-cell} ipython3
:label: cel-black-scholes-hedgefout
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
bins = np.linspace(-6, 4, 81)
for i, (name, pnl) in enumerate(pnl_by_freq.items()):
    axes[0].hist(pnl, bins=bins, density=True, histtype="step", lw=1.6,
                 color=hap.plotting.COLORS[i], label=f"{name} (N = {frequencies[name]})")
axes[0].set_title("Verdeling van de P&L, verkochte call op 3 maanden")
axes[0].set_xlabel("P&L op expiratie (dollar per optie)")
axes[0].set_ylabel("Dichtheid")
axes[0].legend()

axes[1].loglog(n_grid, sd_grid, "o", color=hap.plotting.COLORS[0], label="simulatie")
axes[1].loglog(n_grid, np.sqrt(np.pi / 4) * vega_sim * sigma_sim / np.sqrt(n_grid),
               color=hap.plotting.COLORS[1], label=r"vuistregel $\propto 1/\sqrt{N}$")
axes[1].set_title(f"Standaarddeviatie tegen hedgefrequentie (helling {slope_sd:.2f})")
axes[1].set_xlabel("Aantal hedgemomenten $N$ (log-schaal)")
axes[1].set_ylabel("SD van de P&L (log-schaal)")
axes[1].legend()
plt.show()
```

:::{figure} #cel-black-scholes-hedgefout
:label: fig-black-scholes-hedgefout
:width: 95%

Links is de P&L bij elke frequentie gemiddeld vrijwel nul, maar bij maandelijks hedgen is de spreiding ruim veertig procent van de premie. Rechts volgt de spreiding over bijna twee decaden in $N$ de $1/\sqrt{N}$-wet. De drift van 10% per jaar
verschuift de verdelingen niet zichtbaar.
:::

Net als $p$ in de boom speelt $\mu$ in de simulatie vrijwel geen rol. De prijs en de
hedgefout hangen af van de volatiliteit, niet van de drift.

Hier komt de standaardfout van 2% uit [](#00-01-rendementen) terug, want bij 20%
volatiliteit ligt een gemiddeld rendement na een eeuw data maar op twee
procentpunt nauwkeurig vast. Voor volatiliteit ligt dat anders. Stel dat een handelaar
tien jaar lang elke maand één optie verkoopt, telkens één volatiliteitspunt te duur, zodat
hij per optie de vega maal $0{,}01$ verwacht, ofwel $0{,}20$ dollar. Hedget hij dagelijks,
dan is de standaardfout van zijn gemiddelde na
120 opties $0{,}43/\sqrt{120} = 0{,}04$, en is zijn voordeel met $t \approx 5$
zichtbaar. Hedget hij maandelijks, dan is die standaardfout $1{,}86/\sqrt{120} =
0{,}17$, en is het voordeel na tien jaar niet van ruis te onderscheiden. Een
voordeel in volatiliteit is dus meetbaar op een manier waarop een voordeel in
gemiddeld rendement dat bijna nooit is. Wel gelden er twee voorbehouden. Een handelaar die
weinig hedget, verliest het voordeel in de spreiding van de P&L, en in deze simulatie is
$\sigma$ constant, terwijl de volatiliteit in werkelijkheid zelf onzeker is.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Mark Rubinstein, *Implied Binomial Trees*, Journal of Finance 1994
{cite}`Rubinstein1994`. Emanuel Derman en Iraj Kani, *The Volatility Smile and Its
Implied Tree*, 1994 {cite}`DermanKani1994`.

**Wat.** De *smirk* houdt in dat sinds de crash van 1987 de implied volatility van
S&P 500-indexopties hoger is naarmate de uitoefenprijs lager is
{cite}`ConstantinidesJackwerthPerrakis2008`. Derman en Kani beschrijven hetzelfde
patroon voor opties uit 1994.

**Data hier.** We gebruiken een momentopname van de SPY-optieketen met 28 expiraties via `hap.data.yahoo_options` en de rente uit FRED. De termijnkoers per expiratie halen we uit de pariteit.

**Verschil met het origineel.** Rubinstein had Europese indexopties rond de crash, terwijl we één dag hebben, bijna veertig jaar later, en Amerikaanse opties op een ETF met dividend. De periode vóór 1987 is met gratis data niet te repliceren.

**Verwachte afwijking.** Alleen teken en vorm zijn te toetsen, want de niveaus
hangen van de dag af.
Tot één jaar ligt de implied volatility op 90% van de termijnkoers boven die op de
termijnkoers, het steilst bij de kortste looptijden.
```

We laden de keten, halen per expiratie de termijnkoers uit de pariteit, en rekenen
voor elke *out-of-the-money* optie (een put onder of een call boven de
termijnkoers) de implied volatility uit. We kiezen juist die opties, omdat de premie voor
vroege uitoefening van Amerikaanse opties daar het kleinst is. Als onderliggende waarde
nemen we de verdisconteerde termijnkoers, zoals in de variant van Black voor
termijncontracten {cite}`Black1976`, zodat het dividend geen aanname vraagt.

```{code-cell} ipython3
chain = hap_data.yahoo_options("SPY", 28)
spot = float(chain["spot"].iloc[0])
valuation = pd.Timestamp(chain.index.max().date()) + pd.Timedelta(hours=16)
r_cc = np.log1p(hap_data.fred("DGS3MO")["DGS3MO"].dropna().loc[:valuation].iloc[-1] / 100)

quotes = chain.reset_index()
quotes = quotes[(quotes["bid"] > 0) & (quotes["ask"] > quotes["bid"])].copy()
quotes["mid"] = 0.5 * (quotes["bid"] + quotes["ask"])
quotes["T"] = ((quotes["expiry"] + pd.Timedelta(hours=16) - valuation).dt.total_seconds()
               / (365.25 * 86400))
quotes = quotes[quotes["T"] > 2 / 365]
quotes["DF"] = np.exp(-r_cc * quotes["T"])


def parity_forward(group):
    """Median forward from put-call parity over strikes within 5% of spot."""
    wide = group.pivot_table(index="strike", columns="kind", values="mid").dropna()
    wide = wide[np.abs(np.log(wide.index / spot)) < 0.05]
    return float(np.median(wide.index + (wide["call"] - wide["put"]) / group["DF"].iloc[0]))


forwards = quotes.groupby("expiry").apply(parity_forward, include_groups=False).rename("F")
quotes = quotes.join(forwards, on="expiry")
forward_table = pd.DataFrame({"F": forwards, "F / spot - 1": forwards / spot - 1})
forward_table.index = forward_table.index.date
forward_table.iloc[[0, 9, 18, 27]].round(4)
```

De termijnkoers ligt bij korte looptijden vrijwel op de spot en bij ruim twee jaar bijna
9% hoger, wat overeenkomt met rente min dividend over die looptijd. Nu selecteren we de
out-of-the-money opties en rekenen we hun implied volatility uit.

```{code-cell} ipython3
otm = quotes[((quotes["kind"] == "put") & (quotes["strike"] < quotes["F"]))
             | ((quotes["kind"] == "call") & (quotes["strike"] >= quotes["F"]))].copy()
otm = otm[otm["mid"] >= 0.05]
otm["k"] = np.log(otm["strike"] / otm["F"])
# Black (1976): discounted forward as the underlying, so no dividend assumption is needed
otm["iv"] = implied_vol(otm["mid"].to_numpy(), (otm["DF"] * otm["F"]).to_numpy(),
                        otm["strike"].to_numpy(), otm["T"].to_numpy(), r_cc, otm["kind"].to_numpy())
otm = otm.dropna(subset=["iv"])
pd.Series({"waarderingsmoment": str(valuation), "spot": round(spot, 2), "r (continu)": round(r_cc, 4),
           "OTM-opties": len(otm), "expiraties": otm["expiry"].nunique()})
```

De momentopname is van 11 september 2026 en levert 4521 bruikbare opties over 28
expiraties. We meten de uitoefenprijs als *log-moneyness* $k = \log(K/F)$, de procentuele
afstand tot de termijnkoers, zodat 90% van de termijnkoers overeenkomt met $k = \log 0{,}9 \approx -0{,}105$.
De tabel hieronder geeft per expiratie de implied
volatility bij 90%, 95%, 100% en 105% van de termijnkoers.

```{code-cell} ipython3
def iv_at(group, k):
    """Linearly interpolated implied vol at log-moneyness k (NaN outside the quoted range)."""
    g = group.sort_values("k")
    return float(np.interp(k, g["k"], g["iv"])) if g["k"].min() <= k <= g["k"].max() else np.nan


smile_table = pd.DataFrame(
    {
        expiry: {
            "T (jaar)": g["T"].iloc[0],
            "F / spot - 1": g["F"].iloc[0] / spot - 1,
            "IV 90%": iv_at(g, np.log(0.90)),
            "IV 95%": iv_at(g, np.log(0.95)),
            "IV ATM": iv_at(g, 0.0),
            "IV 105%": iv_at(g, np.log(1.05)),
        }
        for expiry, g in otm.groupby("expiry")
    }
).T
smile_table["skew 90%-ATM"] = smile_table["IV 90%"] - smile_table["IV ATM"]
smile_table.index = smile_table.index.date
within_year = smile_table[smile_table["T (jaar)"] <= 1.0].dropna(subset=["skew 90%-ATM"])
smile_table.round(4)
```

Black-Scholes voorspelt één getal per rij, maar elke rij daalt van links naar rechts. De
vier kortste expiraties hebben geen put op 90%, en hun at-the-money-volatiliteit is
onbetrouwbaar laag (7 tot 12%), omdat we de looptijd in kalenderdagen tellen en er
een weekend in zit. De tabel hieronder zet de helling op drie looptijden naast de
verwachting uit het replicatieblok.

```{code-cell} ipython3
def skew_near(years):
    """Skew IV(90%) - IV(ATM) at the expiry closest to the given maturity."""
    return smile_table["skew 90%-ATM"].iloc[np.argmin(np.abs(smile_table["T (jaar)"] - years))]


pd.DataFrame(
    {
        "verwacht": ["> 0, grootst", "> 0", "> 0, kleinst", "alle", ""],
        "hier": [skew_near(7 / 365.25), skew_near(49 / 365.25), skew_near(1.0),
                 (within_year["skew 90%-ATM"] > 0).sum(), len(within_year)],
    },
    index=["helling 90%-ATM, een week", "helling 90%-ATM, zeven weken",
           "helling 90%-ATM, een jaar", "expiraties tot 1 jaar met helling > 0",
           "expiraties tot 1 jaar met een put op 90%"],
).round(4)
```

**Geslaagd.** Het teken klopt met de verwachting uit het replicatieblok, want bij alle
negentien expiraties tot een jaar ligt de implied volatility op 90% boven die op de
termijnkoers. De helling daalt bovendien met de looptijd, van 21 volatiliteitspunten bij
een
week via 9 bij zeven weken naar 3 bij een jaar.

Links gaat het in de figuur om de helling per looptijd, die bij de kortste looptijd het
steilst is en bij twee jaar het vlakst. Rechts is de vraag of er ergens op het oppervlak
een strook ligt waar de kleur niet met de uitoefenprijs verandert.

```{code-cell} ipython3
:label: cel-black-scholes-smirk
:tags: [hide-input]

targets = [1 / 12, 0.25, 0.5, 1.0, 2.0]
expiry_T = otm.groupby("expiry")["T"].first()
chosen = [expiry_T.index[np.argmin(np.abs(expiry_T.to_numpy() - t))] for t in targets]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
for i, expiry in enumerate(chosen):
    g = otm[(otm["expiry"] == expiry) & (otm["k"].between(-0.35, 0.15))].sort_values("k")
    axes[0].plot(np.exp(g["k"]) * 100, g["iv"] * 100, ".-", ms=3, lw=1.0,
                 color=hap.plotting.COLORS[i], label=f"{expiry.date()} (T = {g['T'].iloc[0]:.2f})")
axes[0].axvline(100, color="black", lw=0.8, ls="--")
axes[0].set_title("Implied volatility van SPY-opties: de smirk")
axes[0].set_xlabel("Uitoefenprijs (% van de termijnkoers)")
axes[0].set_ylabel("Implied volatility (%)")
axes[0].legend(fontsize=8)

surface = otm[otm["k"].between(-0.35, 0.15) & (otm["T"] <= 2.5)]
contour = axes[1].tricontourf(surface["k"], surface["T"], surface["iv"] * 100, levels=14, cmap="viridis")
fig.colorbar(contour, ax=axes[1], label="Implied volatility (%)")
axes[1].set_title("Het implied-volatility-oppervlak")
axes[1].set_xlabel(r"Log-moneyness $\log(K/F)$")
axes[1].set_ylabel("Looptijd (jaar)")
plt.show()
```

:::{figure} #cel-black-scholes-smirk
:label: fig-black-scholes-smirk
:width: 95%

Links zou onder Black-Scholes elke kromme een horizontale lijn op dezelfde hoogte zijn. In werkelijkheid dalen alle krommen van diepe puts naar de termijnkoers, het steilst bij de kortste looptijd, zodat puts ver onder de termijnkoers duur zijn in volatiliteitstermen. Rechts staat hetzelfde als oppervlak, en daar is de helling in de uitoefenprijs overal aanwezig en vlakt ze af met de looptijd.
:::

De tweede replicatie gaat over wat een gehedgde verkoper van opties gemiddeld verdient, en
volgens [](#eq-black-scholes-hedge-pnl) is dat het verschil tussen de variantie in de
optieprijs en de gerealiseerde variantie.

```{admonition} Replicatie
:class: seealso

**Bron.** Robert Whaley, *The Investor Fear Gauge*, Journal of Portfolio Management
2000 {cite}`Whaley2000`. Peter Carr en Liuren Wu, *Variance Risk Premiums*, Review
of Financial Studies 2009 {cite}`CarrWu2009`.

**Wat.** Het gaat om het teken van de *variance risk premium* (de variantie in de optieprijs min de daarna gerealiseerde variantie). Whaley werkt met de oude VIX op S&P 100-opties en Carr en Wu met
variantieswaps die ze uit opties op indices en aandelen samenstellen, over een kortere
periode. Hun niveaus gaan dus over andere instrumenten en jaren dan onze vergelijking, en
daarom toetsen we alleen teken en vorm.

**Data hier.** We gebruiken de VIX uit FRED vanaf 1990 en de dagelijkse marktfactor van Kenneth French. Daaruit berekenen we per dag de gerealiseerde volatiliteit over de volgende 21 handelsdagen.

**Verschil met het origineel.** De VIX meet de verwachte volatiliteit van de S&P 500
over dertig kalenderdagen, en we vergelijken met de hele Amerikaanse markt over 21
handelsdagen. Dertig kalenderdagen zijn ongeveer 21 handelsdagen.

**Verwachte afwijking.** Het verschil moet gemiddeld
positief zijn, met een Newey-West-$t$-waarde ruim boven twee, en positief op een ruime meerderheid van de dagen. In crisismaanden zoals eind 2008 en begin 2020 moet het omslaan.
```

We berekenen het verschil per dag en schatten het gemiddelde. Opeenvolgende dagen
delen 20 van de 21 dagen gerealiseerde volatiliteit, zodat de verschillen sterk
samenhangen en een gewone standaardfout te klein is. De Newey-West-standaardfout
corrigeert daarvoor, en we nemen 42 lags, twee keer de lengte van het venster van 21
dagen.

```{code-cell} ipython3
vix = (hap_data.fred("VIXCLS")["VIXCLS"].dropna() / 100).rename("VIX")
log_mkt = np.log1p(hap_data.market_daily()["Mkt"])
realized_fwd = np.sqrt(252 * log_mkt.pow(2).rolling(21).mean().shift(-21)).rename("RV volgende 21 dagen")

vrp = vix.to_frame().join(realized_fwd, how="inner").dropna()
vrp["verschil"] = vrp["VIX"] - vrp["RV volgende 21 dagen"]
nw = hap.newey_west(vrp["verschil"], pd.Series(1.0, index=vrp.index, name="const"),
                    lags=42, add_constant=False)
monthly_vrp = vrp.resample("ME").last()
worst_months = ", ".join(f"{d:%Y-%m}" for d in monthly_vrp["verschil"].nsmallest(4).index)
```

De tabel zet de uitkomst naast de verwachting uit het replicatieblok.

```{code-cell} ipython3
pd.DataFrame(
    {
        "verwacht": ["", "", "", "", "> 0", "", "> 2", "meerderheid", "> 0", "2008, 2020"],
        "hier": [
            f"{vrp.index[0]:%Y-%m-%d} t/m {vrp.index[-1]:%Y-%m-%d}", len(vrp),
            round(vrp["VIX"].mean(), 4), round(vrp["RV volgende 21 dagen"].mean(), 4),
            round(vrp["verschil"].mean(), 4), round(float(nw.bse.iloc[0]), 4),
            round(float(nw.tvalues.iloc[0]), 4), round((vrp["verschil"] > 0).mean(), 4),
            round((vrp["VIX"] ** 2 - vrp["RV volgende 21 dagen"] ** 2).mean(), 4), worst_months,
        ],
    },
    index=["periode", "handelsdagen", "gemiddelde VIX", "gemiddelde RV",
           "gemiddeld verschil (vol)", "Newey-West SE", "Newey-West t",
           "fractie dagen VIX > RV", "gemiddeld verschil (variantie)",
           "meest negatieve maandeinden"],
)
```

**Geslaagd.** Elke verwachting uit het replicatieblok komt uit. De VIX ligt gemiddeld ruim
boven de daarna gerealiseerde volatiliteit, met een $t$-waarde ver boven twee, en ligt
ook op de meeste dagen erboven, maar in 2008 en 2020 slaat het verschil om. De figuur laat
zien waar dat
gebeurt.

```{code-cell} ipython3
:label: cel-black-scholes-vrp
:tags: [hide-input]

fig, axes = plt.subplots(2, 1, figsize=(10, 6.2), sharex=True, height_ratios=[2, 1])
axes[0].plot(monthly_vrp.index, monthly_vrp["VIX"] * 100, lw=1.2, label="VIX (implied, 30 dagen)")
axes[0].plot(monthly_vrp.index, monthly_vrp["RV volgende 21 dagen"] * 100, lw=1.2,
             label="gerealiseerde volatiliteit, volgende 21 handelsdagen")
axes[0].set_title("Implied tegen daarna gerealiseerde volatiliteit, 1990 tot heden")
axes[0].set_ylabel("Volatiliteit (% per jaar)")
axes[0].legend()
axes[1].bar(monthly_vrp.index, monthly_vrp["verschil"] * 100, width=25,
            color=np.where(monthly_vrp["verschil"] > 0, hap.plotting.COLORS[0], hap.plotting.COLORS[1]))
axes[1].axhline(0, color="black", lw=0.8)
axes[1].set_title("Verschil (VIX min gerealiseerd), op maandeinde")
axes[1].set_xlabel("Jaar")
axes[1].set_ylabel("Volatiliteitspunten")
plt.show()
```

:::{figure} #cel-black-scholes-vrp
:label: fig-black-scholes-vrp
:width: 95%

De VIX ligt meestal boven de volatiliteit die daarna optreedt, zodat opties in die zin gemiddeld duur zijn. De negatieve staven zijn zeldzaam maar groot, zodat een verkoper van opties in de meeste maanden een beetje verdient en in enkele maanden veel verliest.
:::

De meest negatieve maandeinden zijn februari 2020, september en augustus 2008 en
maart 2025. Met $t = 12{,}8$ blijkt uit de data wat de simulatie voor een voordeel in
volatiliteit al liet zien, namelijk dat een premie op tweede momenten scherp te meten is.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Het model gaf de eerste optieprijs waarin de voorkeuren van
beleggers niet voorkomen. Alles volgt uit het argument dat een positie zonder risico de
rente verdient, en de formule vraagt vier grootheden die op het scherm staan en één die
geschat moet worden. Binnen enkele jaren
gebruikten de handelaren op de nieuwe beurs de formule. Het model verklaart waarom het
verwachte
rendement geen rol speelt, en waarom een optie meer waard is als het aandeel wilder
beweegt. De simulatie liet bovendien zien hoe robuust de kern is, omdat de drift vrijwel
geen spoor nalaat en de spreiding van de P&L de $1/\sqrt{N}$-wet volgt.

**Waar het breekt.** Het model voorspelt één volatiliteit per aandeel, maar de markt geeft
er een per uitoefenprijs en looptijd. Op onze handelsdag lag de implied
volatility op 90% van de termijnkoers bij alle negentien expiraties tot een jaar
boven die op de termijnkoers, en het verschil liep van 21 volatiliteitspunten bij een
week tot 3 bij een jaar. Implied volatility wordt zo een oppervlak. Dure diepe puts
betekenen dat de
risiconeutrale verdeling een grote daling waarschijnlijker maakt dan de lognormale, met
andere woorden een dikkere linkerstaart heeft. Deze afwijking is geen schattingsprobleem,
want tweede momenten zijn goed meetbaar.

**Risico of vergissing?** Volgens de Chicago-lezing is de prijs juist en een beloning voor
risico, omdat koersen sprongen maken en de volatiliteit stijgt als koersen dalen. Een
diepe put verzekert dan tegen de toestanden waarin een dollar het meest waard is, en omdat
zo'n sprong niet weg te hedgen is, eist wie het risico draagt een premie. Volgens de
Yale-lezing zit de prijs ernaast, want sinds 1987 is er structurele vraag naar
bescherming, terwijl verkopers van puts beperkt kapitaal hebben. Daardoor ligt de prijs
boven wat het risico rechtvaardigt. Constantinides, Jackwerth en Perrakis
vonden na de crash strategieën die elke risicomijdende belegger zou verkiezen, en
lezen dat als mispricing {cite}`ConstantinidesJackwerthPerrakis2008`. Om beide lezingen te
scheiden, is de stochastische discontofactor (hoe zwaar een dollar in elke toestand weegt)
in crashtoestanden nodig, en die toestanden komen in een eeuw data te weinig voor. Uit de
data van dit college valt dus niet te kiezen.

**Wat er daarna kwam.** Merton had dezelfde wiskunde in continue tijd al vanaf
1969 gebruikt voor de portefeuillekeuze van beleggers, en in 1973 leidde hij er in
[](#03-10-merton-icapm) het evenwicht van de hele markt mee af. Open bleef waarom beleggers
zoveel voor bescherming tegen een crash betalen, en dat vraagt een model dat zegt in welke
toestanden beleggers geld het hardst nodig hebben.

## Oefeningen

:::{exercise}
:label: ex-black-scholes-1

**Instap: de boom gevarieerd.** Neem het toy-voorbeeld met $K = 110$.

1. Bereken $C_0$ met de hand, met de risiconeutrale kans $q$.
2. Maak de boom fijner, zoals Cox, Ross en Rubinstein {cite}`CoxRossRubinstein1979`:
   $n$ stappen over $T = 0{,}25$, met $u = e^{\sigma\sqrt{T/n}}$,
   $d = 1/u$ en $R^{f} = e^{rT/n}$, bij $S = K = 100$, $r = 4\%$ en $\sigma = 20\%$.
   Teken het verschil met [](#eq-black-scholes-call) voor $n = 1, \dots, 200$.
:::

:::{solution} ex-black-scholes-1
:class: dropdown

**(1)** Alleen het pad met drie stijgingen eindigt boven 110, met payoff $23{,}1$. De call kost dus $C_0 = 0{,}216 \cdot 23{,}1/1{,}061208 = 4{,}7018$.

**(2)** De code rekent (1) na en tekent de convergentie.

```{code-cell} ipython3
payoff_110 = np.maximum(toy["S0"] * toy["u"] ** up_moves * toy["d"] ** (toy["n"] - up_moves) - 110.0, 0.0)
price_110 = stats.binom.pmf(up_moves, toy["n"], q_toy) @ payoff_110 / toy["R_f"] ** toy["n"]
print(f"C_0 bij K = 110: {price_110:.4f}")


def crr_call(S, K, T, r, sigma, n):
    """Cox-Ross-Rubinstein binomial price of a European call."""
    dt = T / n
    up = np.exp(sigma * np.sqrt(dt))
    q = (np.exp(r * dt) - 1 / up) / (up - 1 / up)
    j = np.arange(n + 1)
    terminal = np.maximum(S * up ** (2 * j - n) - K, 0.0)
    return np.exp(-r * T) * stats.binom.pmf(j, n, q) @ terminal


n_steps = np.arange(1, 201)
bs_exact = bs_price(100.0, 100.0, 0.25, 0.04, 0.20)
errors = np.array([crr_call(100.0, 100.0, 0.25, 0.04, 0.20, k) - bs_exact for k in n_steps])

fig, ax = plt.subplots()
ax.plot(n_steps, errors, lw=1.0)
ax.plot(n_steps, 1.0 / n_steps, color=hap.plotting.COLORS[1], ls="--", label=r"$\pm 1/n$")
ax.plot(n_steps, -1.0 / n_steps, color=hap.plotting.COLORS[1], ls="--")
ax.set_ylim(-0.3, 0.3)
ax.set_title("Binomiale callprijs min Black-Scholes")
ax.set_xlabel("Aantal stappen $n$")
ax.set_ylabel("Prijsverschil (dollar)")
ax.legend()
plt.show()
print(f"fout bij n = 3: {errors[2]:.4f}; n = 50: {errors[49]:.4f}; n = 200: {errors[199]:.5f}")
```

De fout blijft binnen de stippellijnen $\pm 1/n$ en daalt dus ongeveer als $1/n$, van $0{,}33$ bij drie stappen tot een halve cent bij tweehonderd. Ze wisselt daarbij van teken, omdat de uitoefenprijs afwisselend op en tussen eindknopen valt. De boom en de formule blijken dus hetzelfde idee, replicatie per knoop, en de formule is de limiet van de boom.
:::

:::{exercise}
:label: ex-black-scholes-2

**Afleiding: verkopen tegen de verkeerde volatiliteit.**

1. Toon met [](#eq-black-scholes-pariteit) aan dat gamma en vega van call en put
   gelijk zijn.
2. Het aandeel beweegt met 20%. Een handelaar verkoopt de call op drie maanden uit
   de simulatie tegen 15% of 25%, en hedget dagelijks met die implied volatility of
   met de werkelijke 20%. Voorspel met [](#eq-black-scholes-hedge-pnl) de gemiddelde
   P&L en welke hedge de kleinste spreiding geeft. Controleer met een simulatie.
:::

:::{solution} ex-black-scholes-2
:class: dropdown

**(1)** $P = C - S + Ke^{-r\tau}$, en $-S + Ke^{-r\tau}$ is lineair in $S$ en hangt
niet van $\sigma$ af, zodat de tweede afgeleide naar $S$ en de afgeleide naar $\sigma$ voor call en put gelijk zijn. Ook zonder te rekenen is dat te zien, want call min put is een termijncontract.

**(2)** De gemiddelde P&L is ongeveer $\nu(\sigma_i - \sigma_g) = \pm 0{,}99$.
Wie met de werkelijke volatiliteit hedget, legt het premieverschil vast, zodat alleen de spreiding door discreet hedgen overblijft. Wie met $\sigma_i$ hedget, heeft daarnaast de padafhankelijke
term uit de propositie.

```{code-cell} ipython3
wrong_rows = []
for sigma_i in (0.15, 0.25):
    premium_gap = (bs_price(100.0, 100.0, T_sim, r_sim, sigma_i)
                   - bs_price(100.0, 100.0, T_sim, r_sim, sigma_sim)) * np.exp(r_sim * T_sim)
    for label, sigma_h in (("hedge bij implied", sigma_i), ("hedge bij werkelijke", sigma_sim)):
        pnl = delta_hedge_pnl(63, n_paths, 100.0, 100.0, T_sim, r_sim, mu_sim,
                              sigma_sim, sigma_i, sigma_hedge=sigma_h)
        wrong_rows.append({"sigma_i": sigma_i, "hedge": label, "gemiddelde P&L": pnl.mean(),
                           "SD P&L": pnl.std(ddof=1), "premieverschil": premium_gap,
                           "vega x (sigma_i - sigma_g)": vega_sim * (sigma_i - sigma_sim)})
pd.DataFrame(wrong_rows).set_index(["sigma_i", "hedge"]).round(4)
```

Bij verkoop tegen 15% verliest de handelaar gemiddeld $0{,}98$ à $1{,}00$ dollar, en bij verkoop tegen 25% wint hij $1{,}00$. Met de werkelijke volatiliteit is de spreiding $0{,}43$, net als in de simulatie, maar met de implied volatility is ze $0{,}61$ en $0{,}55$. Een gehedgde optie is dus een weddenschap op gerealiseerde variantie, en een handelaar die met de eigen $\sigma_i$ hedget, laat de uitkomst afhangen van waar de koers zich ophoudt.
:::

:::{exercise}
:label: ex-black-scholes-3

**Is de variance risk premium stabiel?** Splits de steekproef in 1990–2007 en
2008–heden. Bereken per periode het gemiddelde verschil tussen VIX en gerealiseerde
volatiliteit met een Newey-West-standaardfout. Bereken met niet-overlappende
maanddata het aantal jaren $T^{*} = (1{,}96\,\SD/\text{gemiddelde})^2$ dat nodig is
voor significantie. Vergelijk met een aandelenpremie van 6% bij 20% volatiliteit.
:::

:::{solution} ex-black-scholes-3
:class: dropdown

```{code-cell} ipython3
periods = {"1990-2007": vrp.loc[:"2007"], "2008-heden": vrp.loc["2008":]}
rows = []
for name, sample in periods.items():
    fit = hap.newey_west(sample["verschil"], pd.Series(1.0, index=sample.index, name="const"),
                         lags=42, add_constant=False)
    monthly = sample["verschil"].resample("ME").last().dropna()
    rows.append({
        "periode": name,
        "gemiddeld verschil": sample["verschil"].mean(),
        "NW SE": float(fit.bse.iloc[0]),
        "NW t": float(fit.tvalues.iloc[0]),
        "maanden": len(monthly),
        "jaren nodig (maanddata)": (1.96 * monthly.std(ddof=1) / monthly.mean()) ** 2 / 12,
    })
equity_years = (1.96 * 0.20 / 0.06) ** 2
print(f"jaren nodig voor een equity premium van 6% bij sigma = 20%: {equity_years:.1f}")
pd.DataFrame(rows).set_index("periode").round(4)
```

Het verschil is in beide periodes positief en scherp gemeten: $4{,}85$ punten over
1990–2007 ($t = 15{,}0$) en $3{,}15$ punten vanaf 2008 ($t = 6{,}1$). Voor
significantie is met maanddata een derde van een jaar nodig (1990–2007) en twee jaar (vanaf 2008), terwijl de aandelenpremie 43 jaar nodig heeft. De kleinere premie na 2008 past bij beide lezingen, namelijk arbitrageurs die een bekende vergissing wegnemen, of een crashrisico dat blijft en daarom beloond blijft. Het meetprobleem van een gemiddeld rendement geldt dus niet voor een premie op tweede momenten.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
