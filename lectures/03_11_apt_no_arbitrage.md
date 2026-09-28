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

(03-11-apt-no-arbitrage)=

# Ross, APT en de fundamentele stelling

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1976–1987.

**Wat we al weten.** Black, Scholes en Merton waardeerden in [](#02-09-black-scholes)
een optie zonder iets over voorkeuren te weten, door die na te maken uit aandeel en
obligatie. Merton gaf het CAPM in [](#03-10-merton-icapm) meer factoren, maar die
factoren kwamen uit de hedgebehoeften van een belegger, en daarvoor moeten we zijn
nutsfunctie kennen.

**Welke vraag staat open.** Hoeveel kunnen we over prijzen zeggen als we alleen aannemen
dat er geen geld op straat ligt?
```

## Overzicht

Wat volgt er uit de aanname dat er geen *arbitrage* bestaat (een strategie die niets
kost, nooit verlies geeft en soms winst)? Het antwoord heeft twee delen. Ten eerste is
geen arbitrage hetzelfde als het bestaan van een positieve *stochastic discount factor*
(SDF, de willekeurige variabele waarmee payoffs van morgen worden verdisconteerd). Ten
tweede zijn verwachte rendementen lineair in de factorbèta's als de rendementen een
factorstructuur hebben, en daarvoor zijn evenwicht noch nutsfunctie nodig. Die
algemeenheid heeft een prijs, want de stelling zegt niet welke discontofactor het is, en
de APT zegt niet welke factoren. In dit college:

- waarderen we in een markt met twee toestanden een call op twee manieren, en bouwen we
  de arbitrage die ontstaat als de call te duur is.

- bewijzen we de fundamentele stelling: geen arbitrage dan en slechts dan als er
  positieve toestandsprijzen bestaan.

- leiden we de arbitrageprijstheorie (APT) van Ross af, eerst exact en dan met eigen
  ruis per aandeel.

- simuleren we waarom een verkeerd gewaardeerd aandeel met tien jaar data onzichtbaar
  blijft, terwijl een gespreide portefeuille vrijwel juist gewaardeerd is.

- repliceren we de vraag van Roll en Ross {cite}`RollRoss1980`, hoeveel factoren een
  premie dragen, met principale componenten van de 25 portefeuilles van French,
  gesorteerd op omvang en boekwaarde/marktwaarde.

Pedro Santa-Clara noemt het idee dat twee dingen met dezelfde payoffs dezelfde prijs
hebben het derde grote idee van het vak, na efficiëntie en evenwicht
{cite}`SantaClara2026`. Stephen Ross maakte er in 1976 een theorie van verwachte
rendementen van {cite}`Ross1976`, en Philip Dybvig en Ross gaven het geheel in 1987 zijn
naam, de *fundamentele stelling van asset pricing* {cite}`DybvigRoss1987`. Met dit werk
begint een nieuw tijdvak, omdat het prijzen losmaakt van voorkeuren.

Of iets theorie of feit is, hangt hier af van het soort uitspraak. Het CAPM is
een theorie die getoetst wordt en kan falen, maar de fundamentele stelling is een
wiskundige equivalentie en kan dat niet. De APT zit ertussen, want ze zegt meer dan de
stelling (er is een factorstructuur), maar minder dan het CAPM (welke factoren en
hoeveel, zegt ze niet). Over die leegte ging het debat van de jaren tachtig.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een markt waarin het morgen alleen goed of slecht kan gaan. Een obligatie keert
in beide gevallen hetzelfde uit, een aandeel veel als het goed gaat en weinig als het
slecht gaat. Met die twee is elke uitkering van morgen na te maken, want wie alleen iets
wil in de goede toestand, koopt aandelen en verkoopt zoveel obligaties dat de slechte
toestand op nul uitkomt.

Een derde activum, zoals een optie, voegt dan niets toe, en zijn prijs ligt vast omdat
het evenveel moet kosten als het pakket dat hetzelfde uitkeert. Kost het meer, dan
verkoopt een handelaar het en koopt hij het pakket, zodat hij vandaag geld ontvangt en
morgen niets hoeft te betalen. Die verkoopdruk duwt de prijs omlaag tot het verschil weg
is.

Het argument werkt ook andersom. Als alle prijzen onderling kloppen, bestaat er een
lijstje van twee getallen, namelijk de prijs van een euro die alleen komt als het goed
gaat en de prijs van een euro die alleen komt als het slecht gaat. Elke prijs is dan
uitkering maal die toestandsprijzen. Beide getallen moeten positief zijn, want kostte
een euro in de slechte toestand niets, dan kocht iedereen er onbeperkt van en steeg de
prijs.

Ross zag dat hetzelfde argument werkt met factoren in plaats van toestanden. Aandelen
bewegen samen omdat een handvol grote krachten ze allemaal raakt, zoals de conjunctuur,
de rente en de olieprijs, maar daarnaast beweegt elk aandeel om eigen redenen. Met
honderden aandelen is een portefeuille te bouwen die niet blootstaat aan de grote
krachten en waarin de eigen bewegingen elkaar uitmiddelen, zodat hij bijna risicovrij
is. Lag zijn verwachte rendement toch boven de rente, dan kochten handelaars die
portefeuille tot het verschil verdween.

Uit deze redenering volgen drie verwachtingen. De optie kost exact wat het pakket kost,
en elke andere prijs geeft een arbitrage. Verwachte rendementen stijgen lineair met de
blootstelling aan de grote krachten, en alleen daarmee. Dat laatste geldt echter voor
gespreide portefeuilles en niet voor elk los aandeel, want een enkel aandeel kan fors
verkeerd gewaardeerd zijn zonder dat er gratis geld ligt.

## Toy-voorbeeld: twee toestanden, drie activa en een arbitrage

We laden eerst de pakketten die het hele college gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** Morgen is de toestand *goed* (fysieke kans 0,6) of *slecht* (kans 0,4).
Obligatie en aandeel worden verhandeld tegen de prijzen hieronder, en het derde activum
is een call op het aandeel met uitoefenprijs 1. Wat moet de call kosten?

| activum | payoff goed | payoff slecht | prijs $p$ |
|---|---|---|---|
| obligatie | 1{,}00 | 1{,}00 | 0{,}90 |
| aandeel | 1{,}40 | 0{,}60 | 0{,}86 |
| call (uitoefenprijs 1) | 0{,}40 | 0{,}00 | ? |

**Het recept.** Een *toestandsprijs* is de prijs van één euro die alleen in één toestand
wordt uitbetaald. Elke prijs is dan de som van uitkering maal toestandsprijs,
$p = q_g x_g + q_s x_s$, en dat recept leidt de theorie als eerste af.

**Stap 1: toestandsprijzen.** Voor de obligatie geldt $q_g + q_s = 0{,}90$ en voor het
aandeel $1{,}40\,q_g + 0{,}60\,q_s = 0{,}86$. Trekken we $0{,}6$ keer de eerste
vergelijking van de tweede af, dan blijft $0{,}80\,q_g = 0{,}32$ over, dus
$q_g = 0{,}40$ en $q_s = 0{,}50$.

**Stap 2: de rente.** De obligatie kost $q_g + q_s$ en keert in beide toestanden één
euro uit. Daarom is $1 + R^{f} = 1/0{,}90 = 1{,}1111$ en $R^{f} = 11{,}1\%$.

**Stap 3: de call.** De call keert alleen in de goede toestand iets uit. Daarom is
$p_{\text{call}} = 0{,}40 \cdot 0{,}40 + 0{,}50 \cdot 0 = 0{,}16$.

**Stap 4: replicatie.** Zoek $\theta_b$ obligaties en $\theta_a$ aandelen met
$\theta_b + 1{,}40\,\theta_a = 0{,}40$ en $\theta_b + 0{,}60\,\theta_a = 0$. Dat geeft
$\theta_a = 0{,}5$ en $\theta_b = -0{,}3$, en het pakket kost
$-0{,}3 \cdot 0{,}90 + 0{,}5 \cdot 0{,}86 = 0{,}16$.

**Stap 5: een arbitrage.** Noteert de call $0{,}20$, dan verkopen we de call en kopen we
het pakket uit stap 4. Vandaag ontvangen we $0{,}20 - 0{,}16 = 0{,}04$, terwijl de
payoff morgen in beide toestanden nul is.

De cel rekent dezelfde stappen na en zet hand en code naast elkaar.

```{code-cell} ipython3
prob = np.array([0.6, 0.4])                  # physical probabilities (good, bad)
X = np.array([[1.00, 1.40, 0.40],            # payoffs in state 'goed': bond, stock, call
              [1.00, 0.60, 0.00]])           # payoffs in state 'slecht'
p_traded = np.array([0.90, 0.86])            # prices of bond and stock

q = np.linalg.solve(X[:, :2].T, p_traded)    # state prices: p = X'q
gross_rf = 1 / q.sum()                       # 1 + R^f
theta = np.linalg.solve(X[:, :2], X[:, 2])   # replicating portfolio: bond, stock

p_quoted = np.array([0.90, 0.86, 0.20])      # the call is overpriced
holdings = np.array([theta[0], theta[1], -1.0])  # sell the call, buy the replica

hand = {"q goed": 0.40, "q slecht": 0.50, "1 + R^f": 1.1111, "call via q'x": 0.16,
        "call via replicatie": 0.16, "obligaties in replicatie": -0.3,
        "aandelen in replicatie": 0.5, "arbitrage: kasstroom vandaag": 0.04,
        "arbitrage: payoff goed": 0.0, "arbitrage: payoff slecht": 0.0}
code = [q[0], q[1], gross_rf, q @ X[:, 2], theta @ p_traded, theta[0], theta[1],
        -holdings @ p_quoted, X[0] @ holdings, X[1] @ holdings]
pd.DataFrame({"met de hand": list(hand.values()), "code": code}, index=hand.keys()).round(4)
```

De twee kolommen zijn gelijk, terwijl de kansen 0,6 en 0,4 in geen enkele stap
voorkwamen. Op die observatie bouwden {cite:t}`CoxRoss1976` hun risiconeutrale
waardering. Twee verhandelde activa leggen dus de prijs van de call vast, en elke andere
prijs levert gratis geld op.

## Theorie

Alles in deze sectie steunt op de fundamentele stelling, die zegt dat er geen arbitrage
is dan en slechts dan als er positieve toestandsprijzen zijn, en waaruit het recept van
het toy-voorbeeld volgt. Daarop bouwen we verder met de vraag wanneer die prijzen uniek
zijn en hoe de stelling over veel perioden werkt. Het belangrijkste gevolg is de APT van
Ross, die zegt wat de stelling voor verwachte rendementen betekent, eerst exact en dan
met ruis, en we sluiten af met de manier waarop factoren en hun premies geschat worden.

### Opzet en aannames

Er is één periode met $S$ toestanden en $N$ activa. Prijzen
$\mathbf{p} \in \mathbb{R}^{N}$ gelden op $t$ en payoffs op $t+1$, maar omdat er maar
één periode is, laten we de tijdsindex weg. De payoffs staan in een $S \times N$-matrix
$\mathbf{X}$, waarin element $X_{s,i}$ de uitkering van activum $i$ in toestand $s$ is.
De payoff $x_i$ is de toevalsvariabele die in toestand $s$ de waarde $X_{s,i}$ aanneemt.
In het toy-voorbeeld is $S = 2$ en $N = 3$. Een portefeuille
$\boldsymbol{\theta} \in \mathbb{R}^{N}$ (negatieve elementen zijn short) kost
$\mathbf{p}'\boldsymbol{\theta}$ en keert $\mathbf{X}\boldsymbol{\theta}$ uit. De
fysieke kansen zijn $\pi_s > 0$. We schrijven $\mathbf{z} \geq \mathbf{0}$ als elk
element niet-negatief is en $\mathbf{z} \gg \mathbf{0}$ als elk element strikt positief
is.

:::{prf:definition} Arbitrage, toestandsprijzen, SDF, risiconeutrale maat
:label: def-apt-no-arbitrage-begrippen

1. Een *arbitrage* is een $\boldsymbol{\theta}$ met
   $\mathbf{p}'\boldsymbol{\theta} \leq 0$ en
   $\mathbf{X}\boldsymbol{\theta} \geq \mathbf{0}$, waarbij niet zowel
   $\mathbf{p}'\boldsymbol{\theta} = 0$ als
   $\mathbf{X}\boldsymbol{\theta} = \mathbf{0}$.
2. Een vector toestandsprijzen (*state prices*) is een $\mathbf{q} \gg \mathbf{0}$ met
   $\mathbf{p} = \mathbf{X}'\mathbf{q}$.
3. Een SDF (stochastische discontofactor) is een $m$ met
   $p_i = \E[m x_i] = \sum_s \pi_s m_s X_{s,i}$ voor alle $i$.
4. Is er een risicovrij activum (payoff $\mathbf{1}$, prijs $1/(1+R^{f})$), dan heet een
   kansvector $\boldsymbol{\pi}^{*} \gg \mathbf{0}$ met $p_i = \E^{*}[x_i]/(1+R^{f})$
   voor alle $i$ een *equivalente martingaalmaat*
   (risiconeutrale maat).
:::

"Equivalent" betekent hier dat $\pi^{*}_s > 0$ in elke toestand waarin $\pi_s > 0$.
Toestandsprijzen, SDF en risiconeutrale kansen zijn vertalingen van elkaar:

```{math}
:label: eq-apt-no-arbitrage-drie-namen
p_i \;=\; \sum_{s} q_s X_{s,i}
    \;=\; \E\!\left[m\, x_i\right]
    \;=\; \frac{\E^{*}\!\left[x_i\right]}{1+R^{f}},
\qquad
m_s = \frac{q_s}{\pi_s},
\qquad
\pi^{*}_s = q_s \left(1+R^{f}\right).
```

In woorden: een prijs is uitkering maal toestandsprijs, of verwachte uitkering gewogen
met de SDF, of risiconeutraal verwachte uitkering verdisconteerd tegen de rente. De SDF
is de toestandsprijs per eenheid kans, en de risiconeutrale kans is de toestandsprijs
per euro van de obligatie. In het toy-voorbeeld:

$$
m_g = \frac{0{,}40}{0{,}6} = 0{,}6667, \quad m_s = \frac{0{,}50}{0{,}4} = 1{,}25,
\qquad
\pi^{*}_g = 0{,}40 \cdot 1{,}1111 = 0{,}4444, \quad \pi^{*}_s = 0{,}50 \cdot 1{,}1111 = 0{,}5556.
$$

De SDF is hoog in *slecht*, omdat een euro daar meer waard is. De risiconeutrale kans op
*slecht* ligt daarom boven de fysieke kans van 0,4, en daarin zit de risicopremie van
het aandeel.

### Het kernresultaat: de fundamentele stelling

*Waarom zou dit waar zijn?* Stel dat een claim op een euro alleen in de slechte toestand
niets kost. Een handelaar koopt er dan onbeperkt van, want hij kan er alleen aan
verdienen. Die vraag drijft de prijs op tot ze positief is. Omgekeerd kost elk pakket
dat nergens verlies en ergens winst geeft een positief bedrag, zolang elke
toestandsprijs positief is. Een markt zonder arbitrage en positieve toestandsprijzen
horen dus bij elkaar.

:::{prf:theorem} Fundamentele stelling van asset pricing (eindig)
:label: thm-apt-no-arbitrage-fundamenteel

De volgende uitspraken zijn equivalent:

1. Er is geen arbitrage.
2. Er bestaan toestandsprijzen $\mathbf{q} \gg \mathbf{0}$ met
   $\mathbf{p} = \mathbf{X}'\mathbf{q}$.
3. Er bestaat een strikt positieve SDF: $m \gg 0$ met $\mathbf{p} = \E[m\,\mathbf{x}]$.

Als er een risicovrij activum is, zijn ze bovendien equivalent met

4. Er bestaat een equivalente martingaalmaat $\boldsymbol{\pi}^{*}$.
:::

Het bewijs loopt in twee richtingen. Dat (2) arbitrage uitsluit, volgt al uit de laatste
stap van de redenering hierboven. Voor de omgekeerde richting kijken we naar alle
combinaties van kasstroom vandaag en payoffs morgen die de markt kan maken. Zonder
arbitrage is geen daarvan overal niet-negatief en ergens positief. Een scheidend
hypervlak tussen die combinaties en de positieve payoffs heeft dan een normaalvector met
positieve elementen, en die elementen zijn de toestandsprijzen. De equivalentie met (3)
en
(4) is [](#eq-apt-no-arbitrage-drie-namen).

:::{prf:proof}
:class: dropdown

*Stap 1: positieve toestandsprijzen sluiten arbitrage uit.* Stel
$\mathbf{p} = \mathbf{X}'\mathbf{q}$ met $\mathbf{q} \gg \mathbf{0}$ en
$\mathbf{X}\boldsymbol{\theta} \geq \mathbf{0}$. Dan is
$\mathbf{p}'\boldsymbol{\theta} = \mathbf{q}'\mathbf{X}\boldsymbol{\theta} \geq 0$, met
gelijkheid alleen als $\mathbf{X}\boldsymbol{\theta} = \mathbf{0}$. Er is dus geen
arbitrage.

*Stap 2: de haalbare kasstromen raken het positieve orthant niet.* We verzamelen alle
kasstromen die de markt kan maken. Laat

$$
M = \left\{ \left(-\mathbf{p}'\boldsymbol{\theta},\;
      \mathbf{X}\boldsymbol{\theta}\right) : \boldsymbol{\theta} \in
      \mathbb{R}^{N} \right\} \subset \mathbb{R}^{1+S}.
$$

Het eerste element is de kasstroom vandaag, de overige $S$ die van morgen. Geen
arbitrage betekent $M \cap \mathbb{R}^{1+S}_{+} = \{\mathbf{0}\}$. Laat
$\Delta = \{\mathbf{z} \in \mathbb{R}^{1+S}_{+} : \sum_j z_j = 1\}$ de simplex zijn. Dan
is $M$ een gesloten deelruimte, $\Delta$ compact en convex, en
$M \cap \Delta = \emptyset$.

*Stap 3: een scheidend hypervlak.* De scheidingsstelling voor een gesloten en een
compacte convexe verzameling geeft een $\boldsymbol{\phi}$ en $c_1 < c_2$ met
$\boldsymbol{\phi}'\mathbf{y} \leq c_1$ op $M$ en
$\boldsymbol{\phi}'\mathbf{z} \geq c_2$ op $\Delta$. Een lineaire functie die op een
deelruimte naar boven begrensd is, is daar nul. Dus $\boldsymbol{\phi} \perp M$ en
$c_2 > 0$. De eenheidsvectoren liggen in $\Delta$, dus $\phi_j \geq c_2 > 0$ voor elke
$j$.

*Stap 4: de normaalvector geeft de toestandsprijzen.* Schrijf
$\boldsymbol{\phi} = (\phi_0, \boldsymbol{\phi}_{1:S})$. Loodrecht op $M$ staan betekent
$\phi_0\,\mathbf{p} = \mathbf{X}'\boldsymbol{\phi}_{1:S}$. Dan is
$\mathbf{q} = \boldsymbol{\phi}_{1:S}/\phi_0 \gg \mathbf{0}$ met
$\mathbf{p} = \mathbf{X}'\mathbf{q}$.

*Stap 5: de drie namen.* Volgens [](#eq-apt-no-arbitrage-drie-namen) is
$m_s = q_s/\pi_s$ strikt positief als $q_s$ dat is. Met een risicovrij activum is
$\pi^{*}_s = q_s(1+R^{f})$ een strikt positieve kansvector, en omgekeerd. $\square$
:::

In het toy-voorbeeld is $\mathbf{q} = (0{,}40;\ 0{,}50) \gg \mathbf{0}$, dus is de markt
met de call op 0,16 arbitragevrij. Bij 0,20 waardeert geen enkele $\mathbf{q}$ alle drie
de activa juist, en dan belooft de stelling een arbitrage, namelijk die van stap 5. De
optieprijs ligt dus vast zodra de toestandsprijzen vastliggen, en daarmee komt de eerste
verwachting uit de intuïtie uit.

### Uniciteit: complete en incomplete markten

Toestandsprijzen liggen alleen vast als elke payoff na te maken is. Neem een markt met
drie toestanden maar alleen obligatie en aandeel. Een handelaar die een euro alleen in
de middelste toestand wil, kan die niet namaken, en dus zegt geen enkele waargenomen
prijs wat zo'n euro kost. De toestandsprijzen kunnen in die richting schuiven, zodat een
claim die daarvan afhangt een bandbreedte van prijzen heeft in plaats van één prijs.

:::{prf:theorem} Volledigheid en uniciteit
:label: thm-apt-no-arbitrage-uniek

Stel dat er geen arbitrage is. De markt heet *compleet* als elke payoff
$\mathbf{y} \in \mathbb{R}^{S}$ te repliceren is, dus als
$\operatorname{rang} \mathbf{X} = S$. De toestandsprijzen, en dus de SDF en de
risiconeutrale maat, zijn uniek dan en slechts dan als de markt compleet is.
:::

:::{prf:corollary} Prijsgrenzen in een incomplete markt
:label: cor-apt-no-arbitrage-grenzen

Voor een niet-repliceerbare payoff $\mathbf{y}$ is elke prijs in het open interval

```{math}
:label: eq-apt-no-arbitrage-grenzen
\left( \inf_{\mathbf{q} \gg \mathbf{0},\; \mathbf{X}'\mathbf{q} = \mathbf{p}}
       \mathbf{q}'\mathbf{y},\;\;
       \sup_{\mathbf{q} \gg \mathbf{0},\; \mathbf{X}'\mathbf{q} = \mathbf{p}}
       \mathbf{q}'\mathbf{y} \right)
```

verenigbaar met een markt zonder arbitrage.
:::

:::{prf:proof}
:class: dropdown

De oplossingen van $\mathbf{X}'\mathbf{q} = \mathbf{p}$ vormen de verzameling
$\mathbf{q}_0 + \ker \mathbf{X}'$. Die kern is $\{\mathbf{0}\}$ dan en slechts dan als
$\mathbf{X}$ rang $S$ heeft. Bij rang $S$ is er hoogstens één oplossing, en volgens
[](#thm-apt-no-arbitrage-fundamenteel) precies één strikt positieve. Bij lagere rang
nemen we een $\mathbf{k} \neq \mathbf{0}$ in de kern, en dan is
$\mathbf{q}_0 + \varepsilon\mathbf{k}$ voor kleine $|\varepsilon|$ ook strikt positief
en waardeert die vector alle activa juist.

Voor de grenzen: voeg $\mathbf{y}$ met prijs $p_y$ toe. Volgens de stelling is de
uitgebreide markt arbitragevrij dan en slechts dan als een $\mathbf{q} \gg \mathbf{0}$
ook $\mathbf{q}'\mathbf{y} = p_y$ haalt. De haalbare waarden zijn het lineaire beeld van
een relatief open convexe verzameling, dus een open interval. $\square$
:::

De grenzen in [](#eq-apt-no-arbitrage-grenzen) zijn het laagste en het hoogste bedrag
$\mathbf{q}'\mathbf{y}$ over alle toestandsprijzen die de markt toelaat. Volgens de
dualiteitsstelling van lineaire programmering is de bovengrens de prijs van het
goedkoopste pakket dat overal minstens $\mathbf{y}$ uitkeert, en de eerste oefening
laat dat met getallen zien. Omdat echte markten incompleet
zijn, garandeert de stelling daar wel een positieve SDF, maar niet welke.

### Veel perioden: de binomiale knoop

Een boom met veel perioden is een reeks één-periodemarkten, en Harrison en Kreps bewezen
dat de stelling dan per knoop geldt {cite}`HarrisonKreps1979`. Harrison en Pliska
brachten dat naar continue tijd {cite}`HarrisonPliska1981`. Met $A_t$ de waarde van een
doorgerolde spaarrekening en $d_{t+1}$ het dividend luidt de stelling

```{math}
:label: eq-apt-no-arbitrage-martingaal
\frac{p_t}{A_t} = \E^{*}_t\!\left[\frac{p_{t+1} + d_{t+1}}{A_{t+1}}\right],
\qquad
A_t = \prod_{j=1}^{t} \left(1 + R^{f}_{j}\right).
```

Zonder dividend is de prijs, gemeten in spaarrekeningen, dus een *martingaal* onder
$\boldsymbol{\pi}^{*}$, en met dividend geldt dat voor de waarde van het aandeel plus
herbelegde dividenden. Bij zo'n reeks is de beste voorspelling van morgen, onder die
kansen, de waarde van vandaag.

In de binomiale boom van Cox, Ross en Rubinstein {cite}`CoxRossRubinstein1979`, uit
[](#02-09-black-scholes), is elke knoop een kopie van ons toy-voorbeeld. Het aandeel
gaat met factor $u$ omhoog of met factor $d$ omlaag, waarbij $d$ hier de daalfactor is
en niet het dividend. De risiconeutrale kans op omhoog is dan

```{math}
:label: eq-apt-no-arbitrage-crr-q
\pi^{*} = \frac{1 + R^{f} - d}{u - d}.
```

Die kans ligt tussen nul en één, en de knoop is dus arbitragevrij, dan en slechts dan
als $d < 1 + R^{f} < u$. In het toy-voorbeeld is per euro aandeel
$u = 1{,}40/0{,}86 = 1{,}6279$ en $d = 0{,}60/0{,}86 = 0{,}6977$, en dat geeft

$$
\pi^{*} = \frac{1{,}1111 - 0{,}6977}{1{,}6279 - 0{,}6977} = \frac{0{,}4134}{0{,}9302} = 0{,}4444,
$$

de risiconeutrale kans die hierboven uit [](#eq-apt-no-arbitrage-drie-namen) volgde.

### Wat het voorspelt: de APT met een exacte factorstructuur

Ross paste het argument van het toy-voorbeeld toe op factoren in plaats van toestanden.
Daar was de call een combinatie van obligatie en aandeel, en had ze daardoor geen vrije
prijs. Hangen alle rendementen alleen af van $K$ gemeenschappelijke schokken, dan kan
een handelaar een portefeuille maken die niets kost en geen risico draagt, door $K$
factorbèta's en het budget op nul te zetten. Dat zijn $K+1$ voorwaarden, zodat er vanaf
$K+2$ activa zo'n portefeuille overblijft. Heeft die een positief verwacht rendement,
dan koopt de handelaar er onbeperkt van tot dat rendement nul is. Daarom stijgt het
verwachte
rendement lineair met de bèta op elke factor.

We maken dit argument nu formeel. Laat de bruto rendementen voldoen aan

```{math}
:label: eq-apt-no-arbitrage-factormodel
R_i = \mu_i + \sum_{k=1}^{K} \beta_{i,k} f_k + \varepsilon_i,
\qquad \E[f_k] = 0,\quad \E[\varepsilon_i] = 0,\quad \Cov(f_k, \varepsilon_i) = 0.
```

Het rendement bestaat dus uit een verwachting $\mu_i$, plus *factorbèta's* $\beta_{i,k}$
(in de literatuur *factor loadings*) maal schokken $f_k$ die alle aandelen raken, plus
een eigen schok $\varepsilon_i$. Een factorschok $f_k$ is bijvoorbeeld de onverwachte
groei van de industriële productie. In matrixvorm is
$\mathbf{R} = \boldsymbol{\mu} + \mathbf{B}\mathbf{f} + \boldsymbol{\varepsilon}$, met
$\mathbf{B}$ de $N \times K$-matrix van factorbèta's. In deze sectie zijn de $f_k$
schokken met verwachting nul, terwijl het in de replicatie factorrendementen zijn met
een premie als verwachting. Een portefeuille $\mathbf{w}$ met
$\mathbf{w}'\mathbf{1} = 0$ kost niets, omdat hij evenveel leent als hij belegt.

:::{prf:theorem} Exacte APT
:label: thm-apt-no-arbitrage-exact

Stel $\boldsymbol{\varepsilon} = \mathbf{0}$ in [](#eq-apt-no-arbitrage-factormodel) en
er is geen arbitrage. Dan bestaan $\lambda_0$ en
$\boldsymbol{\lambda} \in \mathbb{R}^{K}$ met

```{math}
:label: eq-apt-no-arbitrage-apt
\boldsymbol{\mu} = \lambda_0\mathbf{1} + \mathbf{B}\boldsymbol{\lambda}.
```
:::

:::{prf:proof}
Schrijf $\boldsymbol{\mu} = \lambda_0\mathbf{1} + \mathbf{B}\boldsymbol{\lambda}
+
  \boldsymbol{\eta}$, met $\boldsymbol{\eta}$ het residu van de projectie op $[\mathbf{1},
  \mathbf{B}]$, dus $\boldsymbol{\eta}'\mathbf{1} = 0$ en $\boldsymbol{\eta}'\mathbf{B}
  = \mathbf{0}$. De portefeuille $\mathbf{w} =
  \boldsymbol{\eta}$ kost niets en levert in elke toestand $\boldsymbol{\eta}'\mathbf{R}
  = \boldsymbol{\eta}'\boldsymbol{\eta}$ op. Is $\boldsymbol{\eta} \neq
  \mathbf{0}$, dan is dat een zekere winst zonder kosten: arbitrage. Dus $\boldsymbol{\eta}
  = \mathbf{0}$. $\square$
:::

In woorden: verwachte rendementen liggen op een vlak in de factorbèta's. Met een
risicovrij activum is $\lambda_0 = 1 + R^{f}$, want dat heeft bèta nul. Dan is
$\lambda_k$ de *prijs van risico* van factor $k$: het extra verwachte rendement per
eenheid bèta. In overrendementen staat er
$\E[R^{e}_i] = \sum_k \beta_{i,k}\lambda_k$. Alleen de factorbèta's tellen dus mee,
precies zoals de tweede verwachting uit de intuïtie zei.

Het toy-voorbeeld is een exacte APT met één factor, namelijk de schok in het rendement
van het aandeel. Omdat het aandeel op zijn eigen schok bèta 1 heeft, is $\lambda_1$ zijn
verwachte rendement min $1 + R^{f}$. De bèta van de call is de afwijking van de call ten
opzichte van de eigen verwachting, gedeeld door die van het aandeel in dezelfde
toestand.

| | rendement goed | verwacht rendement | afwijking goed |
|---|---|---|---|
| aandeel | $1{,}40/0{,}86 = 1{,}6279$ | $(0{,}6 \cdot 1{,}40 + 0{,}4 \cdot 0{,}60)/0{,}86 = 1{,}2558$ | $0{,}3721$ |
| call | $0{,}40/0{,}16 = 2{,}5000$ | $0{,}6 \cdot 2{,}50 = 1{,}5000$ | $1{,}0000$ |

Daarmee is $\lambda_1 = 1{,}2558 - 1{,}1111 = 0{,}1447$ en
$\beta_{\text{call},1} = 1{,}0000/0{,}3721 = 2{,}6875$, en de APT voorspelt het
verwachte rendement van de call exact:

$$
\E[R_{\text{call}}] = \frac{0{,}6 \cdot 0{,}40}{0{,}16} = 1{,}50
= \underbrace{1{,}1111}_{1+R^{f}} + \underbrace{2{,}6875}_{\beta_{\text{call},1}} \cdot \underbrace{0{,}1447}_{\lambda_1}.
$$

```{prf:remark} APT en SDF
:label: rem-apt-no-arbitrage-sdf

Een factormodel met prijzen van risico is hetzelfde als een SDF die lineair is in de
factoren. Neem $m = a - \mathbf{b}'\mathbf{f}$ met $a = 1/(1+R^{f})$,
$\boldsymbol{\Omega} = \Var(\mathbf{f})$ en
$\mathbf{b} = a\,\boldsymbol{\Omega}^{-1}\boldsymbol{\lambda}$. Dan is
$\E[m R^{e}_i] = a\,\E[R^{e}_i] - \mathbf{b}'\Cov(\mathbf{f}, R^{e}_i) = a\left(\E[R^{e}_i] - \boldsymbol{\lambda}'\boldsymbol{\beta}_i\right)$,
en dat is nul dan en slechts dan als [](#eq-apt-no-arbitrage-apt) geldt. Niets
garandeert echter dat deze lineaire $m$ positief is. In het toy-voorbeeld is de factor
de schok in het aandeel, $+0{,}3721$ in *goed* en $-0{,}5581$ in *slecht*. Met
$a = 0{,}9$, $\Omega = 0{,}2077$ en $b = 0{,}9 \cdot 0{,}1447/0{,}2077 = 0{,}6271$ geeft
ze exact de SDF van het toy-voorbeeld: $0{,}9 - 0{,}6271 \cdot 0{,}3721 = 0{,}6667$ en
$0{,}9 + 0{,}6271 \cdot 0{,}5581 = 1{,}25$. Een toestand waarin de factor meer dan
$0{,}9/0{,}6271 = 1{,}435$ boven zijn verwachting uitkomt, kreeg een negatieve $m$. Een
lineaire SDF waardeert dus de activa waarop ze geschat is juist, maar kan een diep
uit-het-geld optie op de factor een negatieve prijs geven. De APT is daarom zwakker dan
[](#thm-apt-no-arbitrage-fundamenteel), want ze beperkt verwachte rendementen en niet
alle prijzen.
```

### De APT met ruis: de grens van Huberman

Met eigen ruis per aandeel is de portefeuille $\boldsymbol{\eta}$ niet meer risicovrij,
maar eigen ruis middelt uit, want bij gewichten van orde $1/N$ daalt de eigen variantie
met $1/N$. De *pricing errors* zijn het deel van het verwachte rendement dat de factoren
niet verklaren, in de formules $\eta_i$. Zijn die groot en talrijk, dan bundelt een
handelaar ze tot een portefeuille die steeds meer opbrengt en steeds minder risico
draagt naarmate $N$ groeit. Wie dat uitsluit, laat dus toe dat één aandeel fors
verkeerd gewaardeerd is, maar niet dat veel aandelen het tegelijk zijn.

We bekijken een rij economieën met de eerste $N$ activa uit een oneindige rij. We nemen
aan dat de covariantiematrix $\mathbf{V}^{N}$ van de eigen ruis een begrensde grootste
eigenwaarde heeft: $\omega_{\max}(\mathbf{V}^{N}) \leq \bar\sigma^2$, met
$\omega_{\max}$ de grootste eigenwaarde. In de *strikte* factorstructuur van Ross is
$\mathbf{V}^{N}$ diagonaal, terwijl in de *benaderende* factorstructuur van
{cite:t}`ChamberlainRothschild1983` aandelen in dezelfde bedrijfstak ook samen mogen
bewegen, zolang geen richting onbegrensd veel eigen variantie verzamelt.

:::{prf:definition} Asymptotische arbitrage
:label: def-apt-no-arbitrage-asymptotisch

Een rij portefeuilles $\mathbf{w}^{N}$ met $\mathbf{w}^{N\prime}\mathbf{1} = 0$ is een
*asymptotische arbitrage* als (langs een deelrij)
$\E[\mathbf{w}^{N\prime}\mathbf{R}^{N}] \to \infty$ en
$\Var(\mathbf{w}^{N\prime}\mathbf{R}^{N}) \to 0$.
:::

:::{prf:theorem} Huberman-grens
:label: thm-apt-no-arbitrage-huberman

Laat $\boldsymbol{\eta}^{N}$ het residu zijn van de projectie van $\boldsymbol{\mu}^{N}$
op $[\mathbf{1}, \mathbf{B}^{N}]$. Als $\omega_{\max}(\mathbf{V}^{N}) \leq \bar\sigma^2$
voor alle $N$ en er geen asymptotische arbitrage bestaat, dan is er een $c < \infty$ met

```{math}
:label: eq-apt-no-arbitrage-huberman
\sum_{i=1}^{N} \left(\eta^{N}_{i}\right)^2 \;\leq\; c \qquad \text{voor alle } N.
```
:::

De som van de gekwadrateerde pricing errors blijft dus begrensd, hoeveel aandelen er ook
bijkomen. {cite:t}`Huberman1982` bewijst dat door $\boldsymbol{\eta}^{N}$ te schalen
tot een portefeuille waarvan het verwachte rendement groeit en de variantie krimpt zodra
die som onbegrensd is.

:::{prf:proof}
:class: dropdown

Stel dat $\boldsymbol{\eta}^{N\prime}\boldsymbol{\eta}^{N}$ langs een deelrij naar
oneindig gaat. Kies dan
$\mathbf{w}^{N} = \boldsymbol{\eta}^{N}/(\boldsymbol{\eta}^{N\prime}\boldsymbol{\eta}^{N})^{3/4}$.

*Kosten nul.* $\mathbf{w}^{N\prime}\mathbf{1} = 0$ omdat
$\boldsymbol{\eta}^{N} \perp \mathbf{1}$. *Geen factorrisico.*
$\mathbf{w}^{N\prime}\mathbf{B}^{N} = \mathbf{0}$ omdat
$\boldsymbol{\eta}^{N} \perp \mathbf{B}^{N}$.

*Verwachting groeit.*
$\mathbf{w}^{N\prime}\boldsymbol{\mu}^{N} = \mathbf{w}^{N\prime}\boldsymbol{\eta}^{N} =
(\boldsymbol{\eta}^{N\prime}\boldsymbol{\eta}^{N})^{1/4}
\to \infty$. *Variantie krimpt.* $\mathbf{w}^{N\prime}\mathbf{V}^{N}\mathbf{w}^{N} \leq
\bar\sigma^2\,\mathbf{w}^{N\prime}\mathbf{w}^{N} = \bar\sigma^2
(\boldsymbol{\eta}^{N\prime}\boldsymbol{\eta}^{N})^{-1/2} \to 0$.
Samen vormen deze eigenschappen een asymptotische arbitrage, en dat is in strijd met de
aanname. $\square$
:::

De grens heeft twee gevolgen die in tegengestelde richting wijzen. Het eerste gaat over
portefeuilles, het tweede over losse aandelen.

1. **Gespreide portefeuilles worden juist gewaardeerd.** Een portefeuille met
   $\mathbf{w}'\mathbf{1} = 1$ heeft pricing error $\mathbf{w}'\boldsymbol{\eta}$.
   Volgens Cauchy-Schwarz is die hoogstens $\|\mathbf{w}\|\sqrt{c}$, en voor de
   gelijkgewogen portefeuille is dat $\sqrt{c/N} \to 0$. Met de $c = 0{,}002$ uit de
   simulatie hierna en $N = 100$ is dat hoogstens $\sqrt{0{,}00002} = 0{,}45\%$ per
   maand.
2. **Losse aandelen niet noodzakelijk.** Het aantal aandelen met $\eta_i^2 \geq \zeta$
   is hoogstens $c/\zeta$. Dat is een vast getal, dus een verdwijnende fractie als $N$
   groeit, maar elk van die aandelen mag fors verkeerd gewaardeerd zijn.

Daarmee komt ook de derde verwachting uit de intuïtie uit, want portefeuilles zijn juist
gewaardeerd en losse aandelen niet noodzakelijk. Over één aandeel zegt de APT daardoor
bijna niets, maar over een gespreide portefeuille bijna alles.

### Hoe het getoetst wordt: factoren en premies schatten

Factoren zijn uit de covarianties te halen. Raakt een factor veel aandelen, dan groeit
de variantie die hij in de cross-sectie veroorzaakt mee met het aantal aandelen, terwijl
de eigen ruis niet meegroeit. Een onderzoeker die de covariantiematrix ontbindt, ziet
bij veel aandelen dus $K$ richtingen boven de rest uitsteken, en die richtingen zijn de
factoren.

Chamberlain en Rothschild bewezen dat bij een benaderende factorstructuur met $K$
factoren de covariantiematrix $K$ eigenwaarden heeft die met $N$ groeien
{cite}`ChamberlainRothschild1983`. De bijbehorende eigenvectoren, de *principale
componenten* (de portefeuilles met de grootste variantie, elk loodrecht op de vorige),
schatten de factorbèta's op een rotatie na.

De premies volgen in twee stappen. Eerst geeft een tijdreeksregressie van elk
testactivum (in de replicatie een van de 25 portefeuilles) op de factoren de bèta's.
Daarna regresseren we elke maand de rendementen op die bèta's, zodat het gemiddelde van
de hellingen de premies $\lambda_k$ schat. Met die methode toetsten Fama en MacBeth het
CAPM {cite}`FamaMacBeth1973`, en in essentie deden Roll en Ross hetzelfde
{cite}`RollRoss1980`.

```{admonition} Samengevat
:class: tip

- Geen arbitrage dan en slechts dan als er positieve toestandsprijzen zijn, en dus een
  positieve SDF, [](#eq-apt-no-arbitrage-drie-namen). In het toy-voorbeeld is
  $\mathbf{q} = (0{,}40;\ 0{,}50)$.

- De prijzen zijn uniek dan en slechts dan als de markt compleet is. Anders ligt een
  prijs in [](#eq-apt-no-arbitrage-grenzen).

- Met een exacte factorstructuur zijn verwachte rendementen lineair in de bèta's,
  [](#eq-apt-no-arbitrage-apt). In het toy-voorbeeld heeft de call bèta 2,6875.

- Met ruis blijft de som van de gekwadrateerde pricing errors begrensd,
  [](#eq-apt-no-arbitrage-huberman), zodat portefeuilles juist gewaardeerd zijn en losse
  aandelen niet noodzakelijk.

- De simulatie hierna vraagt of een onderzoeker dat verschil met tien jaar data kan
  zien.
```

## Simulatie: pricing errors van losse aandelen en portefeuilles

Kan een onderzoeker met tien jaar maanddata een verkeerd gewaardeerd aandeel herkennen,
en een verkeerd gewaardeerde portefeuille? We bouwen een wereld die aan
[](#eq-apt-no-arbitrage-huberman) voldoet. In de simulatie heet de pricing error zoals
gebruikelijk $\alpha_i$ of alpha (de $\eta_i$ van de theorie). Twintig aandelen hebben
een alpha van 1% per maand en alle andere een alpha van nul, ongeacht $N$. De som
$\sum_i \alpha_i^2 = 20 \times 0{,}01^2 = 0{,}002$ blijft dus begrensd.

| grootheid | waarde |
|---|---|
| factoren | 3; maandvolatiliteit 4,5%, 3% en 3%; premie 0,5%, 0,3% en 0,3% per maand |
| bèta's | $\beta_{i,1} \sim \mathcal{N}(1;\ 0{,}3^2)$, $\beta_{i,2}, \beta_{i,3} \sim \mathcal{N}(0;\ 0{,}5^2)$ |
| eigen ruis | 8% per maand, onafhankelijk |
| verkeerd gewaardeerd | 20 aandelen met alpha 1% per maand (12% per jaar) |
| steekproef | $T = 120$ maanden, 100 steekproeven per $N$ |

De functie schat per steekproef de alpha's met tijdreeksregressies op de drie factoren
en telt hoe vaak $|t| > 1{,}96$.

```{code-cell} ipython3
sim = {
    "premium": np.array([0.005, 0.003, 0.003]),     # factor premia per month
    "volatility": np.array([0.045, 0.030, 0.030]),  # factor volatility per month
    "sigma_eps": 0.08,                              # idiosyncratic volatility per month
    "n_bad": 20,                                    # number of mispriced stocks
    "alpha_bad": 0.01,                              # their alpha per month
}


def simulate_pricing_errors(N, T=120, n_rep=100):
    """Estimate alphas of N stocks, sim["n_bad"] of them mispriced, on T months of data.

    Returns the rejection rates of individual alphas and the true and estimated
    alpha of the equal-weighted portfolio across n_rep samples.
    """
    lam, vol, sigma_eps = sim["premium"], sim["volatility"], sim["sigma_eps"]
    n_bad, alpha_bad = sim["n_bad"], sim["alpha_bad"]
    B = np.column_stack([rng.normal(1.0, 0.3, N), rng.normal(0.0, 0.5, (N, 2))])
    alpha = np.zeros(N)
    alpha[:n_bad] = alpha_bad
    reject_bad, reject_good, alpha_ew_hat = [], [], []
    for _ in range(n_rep):
        f = lam + vol * rng.standard_normal((T, 3))
        excess = alpha + f @ B.T + sigma_eps * rng.standard_normal((T, N))
        design = np.column_stack([np.ones(T), f])
        coef, *_ = np.linalg.lstsq(design, excess, rcond=None)
        resid = excess - design @ coef
        se = np.sqrt((resid**2).sum(axis=0) / (T - 4) * np.linalg.inv(design.T @ design)[0, 0])
        t_alpha = coef[0] / se
        reject_bad.append(np.mean(np.abs(t_alpha[:n_bad]) > 1.96))
        reject_good.append(np.mean(np.abs(t_alpha[n_bad:]) > 1.96))
        alpha_ew_hat.append(coef[0].mean())
    return {
        "N": N,
        "som alpha^2": float(alpha @ alpha),
        "RMS alpha": float(np.sqrt(alpha @ alpha / N)),
        "alpha gelijkgewogen (waar)": float(alpha.mean()),
        "SD geschatte alpha gelijkgewogen": float(np.std(alpha_ew_hat)),
        "SE alpha per aandeel": float(se.mean()),
        "verworpen, verkeerd gewaardeerd": float(np.mean(reject_bad)),
        "verworpen, juist gewaardeerd": float(np.mean(reject_good)),
    }


N_grid = [25, 50, 100, 200, 400, 800, 1600, 3200]
pricing = pd.DataFrame([simulate_pricing_errors(N) for N in N_grid]).set_index("N")
pricing.round(4)
```

De tabel laat zien dat de standaardfout van één alpha rond 0,75% per maand blijft,
welke $N$ ook, zodat een alpha van 12% per jaar maar in ruim een kwart van de
steekproeven wordt gevonden. Bij de gelijkgewogen portefeuille krimpen daarentegen de
ware alpha en de spreiding van de geschatte alpha allebei naarmate $N$ groeit.

De figuur zet die twee kanten van de Huberman-grens naast elkaar, met bovenaan twee
lijnen die vlak blijven en onderaan twee die dalen.

```{code-cell} ipython3
:label: cel-apt-no-arbitrage-pricing
:tags: [hide-input]

fig, ax = plt.subplots()
ax.plot(pricing.index, np.full(len(pricing), 0.01) * 100, ls="--",
        label="alpha van een verkeerd gewaardeerd aandeel (waar)")
ax.plot(pricing.index, pricing["SE alpha per aandeel"] * 100, marker="o",
        label="standaardfout van de alpha van één aandeel")
ax.plot(pricing.index, pricing["alpha gelijkgewogen (waar)"] * 100, ls="--",
        label="alpha van de gelijkgewogen portefeuille (waar)")
ax.plot(pricing.index, pricing["SD geschatte alpha gelijkgewogen"] * 100, marker="o",
        label="steekproefspreiding van de geschatte alpha, gelijkgewogen")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Aantal aandelen N (log-schaal)")
ax.set_ylabel("Procent per maand (log-schaal)")
ax.set_title("Pricing errors: een aandeel blijft groot, de portefeuille verdwijnt")
ax.legend()
plt.show()
```

:::{figure} #cel-apt-no-arbitrage-pricing
:label: fig-apt-no-arbitrage-pricing
:width: 90%

De bovenste twee lijnen laten zien dat de twintig verkeerd gewaardeerde aandelen hun
alpha van 1% per maand houden, terwijl de standaardfout van die alpha met tien jaar data
0,75% is, hoe groot $N$ ook is. Volgens de onderste twee lijnen daalt de ware alpha van
de gelijkgewogen portefeuille, $0{,}2/N$, met $1/N$ en de schattingsfout met
$1/\sqrt{N}$. Voor gespreide portefeuilles zijn de pricing error en de onzekerheid
erover dus allebei klein, maar voor een los aandeel allebei groot.
:::

Een los aandeel blijft onherkenbaar, want meer aandelen helpen het niet. Zijn
standaardfout hangt alleen af van het aantal maanden $T$:

$$
\frac{\sigma_\varepsilon}{\sqrt{T}} = \frac{0{,}08}{\sqrt{120}} = 0{,}0073.
$$

Dat is [de standaardfout van 2%](#00-01-rendementen) in een andere gedaante. Ook hier
wordt een gemiddelde alleen nauwkeuriger met de wortel van het aantal maanden, en niet
met het aantal aandelen.

De juist gewaardeerde aandelen worden in ongeveer 5% van de steekproeven verworpen,
zoals het hoort, maar bij 3200 aandelen zijn dat er veel meer dan de echte vondsten:

$$
3180 \times 0{,}052 \approx 166 \text{ valse vondsten}, \qquad 20 \times 0{,}284 \approx 5{,}7 \text{ echte}.
$$

Voor portefeuilles is het beeld omgekeerd. De som van de gekwadrateerde pricing errors
blijft 0,002, maar hun RMS (wortel van het gemiddelde kwadraat) zakt van 0,89% bij 25
aandelen naar 0,08% bij 3200, zoals [](#eq-apt-no-arbitrage-huberman) toestaat. De APT
verbiedt dus niet dat er aan één aandeel iets te verdienen valt, maar wel dat het zonder
risico kan.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Richard Roll en Stephen Ross, *An Empirical Investigation of the Arbitrage
Pricing Theory*, Journal of Finance 1980 {cite}`RollRoss1980`. Als schatter gebruiken we
de principale componenten van {cite:t}`ChamberlainRothschild1983`.

**Wat.** Hun samenvatting meldt minstens drie en waarschijnlijk vier factoren met een
premie in dagrendementen van losse aandelen over 1962–1972. Wij repliceren de vorm van
die vraag, dus hoeveel statistische factoren er zijn, of ze een premie dragen en hoe ze
zich verhouden tot de factoren van {cite:t}`FamaFrench1993`: markt (Mkt), klein min
groot (SMB) en waarde min groei (HML).

**Data hier.** De 25 size/BM-portefeuilles en de drie factoren van French komen
maandelijks vanaf 1963-07 via `hap.data.french`. Alle rendementen staan in excess van de
risicovrije rente.

**Verschil met het origineel.** Roll en Ross gebruikten 1260 aandelen in 42 groepen van
dertig, factoranalyse en GLS {cite}`ConnorKorajczyk1995`, terwijl wij 25 portefeuilles,
principale componenten en OLS gebruiken. De portefeuilles zijn gesorteerd op de
kenmerken achter SMB en HML, wat de vergelijking helpt maar elke uitspraak over het
aantal factoren verzwakt.

**Verwachte afwijking.** De eerste component verklaart meer dan 75% van de variantie en
correleert meer dan 0,9 met Mkt-RF. Wijkt dat af, dan zit er een fout in de code. De
componenten en de French-factoren verklaren elkaar met $R^2$ boven 0,85, maar het aantal
componenten met een premie kan afwijken van de drie à vier van Roll en Ross, omdat onze
testactiva op omvang en waarde gesorteerd zijn.
```

We laden de portefeuilles en de factoren en maken overrendementen.

```{code-cell} ipython3
ports = hap_data.french("25_Portfolios_5x5")
ff3 = hap_data.french("F-F_Research_Data_Factors")
sample = ports.join(ff3, how="inner").loc["1963-07":]
excess = sample[ports.columns].sub(sample["RF"], axis=0)
factors = sample[["Mkt-RF", "SMB", "HML"]]
assert excess.notna().all().all()

pd.Series({"begin": f"{excess.index[0]:%Y-%m}", "eind": f"{excess.index[-1]:%Y-%m}",
           "T (maanden)": len(excess), "N (portefeuilles)": excess.shape[1]})
```

De steekproef loopt van 1963-07 tot 2026-07 en telt 757 maanden. Nu ontbinden we de
covariantiematrix van de 25 overrendementen. Omdat een eigenvector maar op een
schaalfactor na vastligt, schalen we de eerste zo dat de gewichten optellen tot één, en
de hogere zo dat er één euro long en één euro short staat. Het teken kiezen we zo dat de
eerste component positief correleert met de markt, de andere met HML.

```{code-cell} ipython3
eigval, eigvec = np.linalg.eigh(np.cov(excess.to_numpy(), rowvar=False))
order = np.argsort(eigval)[::-1]
eigval, eigvec = eigval[order], eigvec[:, order]

n_pc = 5
pc_names = [f"PC{k}" for k in range(1, n_pc + 1)]
first = eigvec[:, 0] / eigvec[:, 0].sum()                    # long-only: weights sum to one
long_short = np.abs(eigvec[:, 1:n_pc]).sum(axis=0) / 2        # size of the long (= short) leg
higher = eigvec[:, 1:n_pc] / long_short                       # one euro long, one euro short
weights = np.column_stack([first, higher])
pcs = pd.DataFrame(excess.to_numpy() @ weights, index=excess.index, columns=pc_names)
for k, name in enumerate(pc_names):
    anchor = factors["Mkt-RF"] if k == 0 else factors["HML"]
    if pcs[name].corr(anchor) < 0:
        pcs[name] *= -1
        weights[:, k] *= -1
```

De tabel hieronder zet de eigenwaarden en hun aandeel in de variantie op een rij.

```{code-cell} ipython3
pd.DataFrame(
    {"eigenwaarde": eigval[:n_pc], "aandeel variantie": eigval[:n_pc] / eigval.sum(),
     "cumulatief": np.cumsum(eigval[:n_pc]) / eigval.sum()},
    index=pc_names,
).round(4)
```

De eerste component verklaart 83% van de variantie en de eerste drie samen 93%. De
figuur toont de gewichten over het 5×5-raster, en daarin valt vooral de richting op
waarin de kleuren van de tweede en derde component verlopen.

```{code-cell} ipython3
:label: cel-apt-no-arbitrage-loadings
:tags: [hide-input]

fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), layout="constrained")
for k, ax in enumerate(axes):
    grid = weights[:, k].reshape(5, 5)
    bound = np.abs(grid).max()
    image = ax.imshow(grid, cmap="RdBu", vmin=-bound, vmax=bound)
    ax.set_xticks(range(5), ["laag", "2", "3", "4", "hoog"])
    ax.set_yticks(range(5), ["klein", "2", "3", "4", "groot"])
    ax.grid(False)
    ax.set_title(f"Gewichten van PC{k + 1}")
    ax.set_xlabel("Boekwaarde/marktwaarde")
    ax.set_ylabel("Omvang")
    fig.colorbar(image, ax=ax, shrink=0.8)
plt.show()
```

:::{figure} #cel-apt-no-arbitrage-loadings
:label: fig-apt-no-arbitrage-loadings
:width: 100%

De eerste component is long in alle 25 portefeuilles, iets zwaarder in kleine aandelen,
en is dus een marktportefeuille. De tweede is short in klein-groei en long in
groot-waarde, de derde long in klein-waarde en short in groot-groei. Hun gradiënten
lopen langs de diagonalen van het raster, zodat het mengsels van waarde en omvang zijn
en geen zuivere SMB of HML.
:::

De correlaties maken dat mengsel zichtbaar.

```{code-cell} ipython3
pd.concat([pcs.iloc[:, :3], factors], axis=1).corr().loc[pc_names[:3], factors.columns].round(3)
```

PC1 correleert 0,93 met de markt, terwijl PC2 en PC3 elk samenhangen met zowel SMB als
HML. De $R^2$ van de ene set op de andere laat zien of beide sets dezelfde ruimte
opspannen.

```{code-cell} ipython3
def r_squared(y, X):
    """R^2 of an OLS regression of y on X with an intercept."""
    design = np.column_stack([np.ones(len(X)), X])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    resid = y - design @ coef
    return 1 - resid @ resid / ((y - y.mean()) @ (y - y.mean()))


pcs3 = pcs.iloc[:, :3]
r2 = {}
for c in factors.columns:
    r2[f"{c} op PC1, PC2, PC3"] = r_squared(factors[c].to_numpy(), pcs3.to_numpy())
for c in pcs3.columns:
    r2[f"{c} op Mkt-RF, SMB, HML"] = r_squared(pcs3[c].to_numpy(), factors.to_numpy())
pd.Series(r2, name="R-kwadraat").round(3)
```

Alle zes de $R^2$'s liggen boven 0,89, hoewel de componenten niets weten van boekwaarden
of marktkapitalisaties. Ze zien alleen covarianties, en daarin zitten drie dominante
richtingen die grotendeels de ruimte opspannen van de factoren die Fama en French in
1993 met de hand bouwden.

Omdat de componenten zelf portefeuilles van overrendementen zijn, is hun gemiddelde
direct een schatting van de premie.

```{code-cell} ipython3
ts = hap.summary_stats(pd.concat([pcs, factors], axis=1))[["mean", "se_mean"]].astype(float)
ts["t"] = ts["mean"] / ts["se_mean"]
(ts[["mean", "se_mean"]] * 100).assign(t=ts["t"]).rename(
    columns={"mean": "gemiddelde (%/mnd)", "se_mean": "SE (%/mnd)", "t": "t-waarde"}).round(3)
```

De tabel laat zien dat PC1 tot en met PC3 een significant gemiddelde hebben en PC4 en
PC5 niet. De standaardfout van PC1 is maal twaalf ruim 2% per jaar, zodat de premie ook
met de volle steekproef niet tot op het procentpunt bekend is.

De tweede schatting volgt Roll en Ross, met eerst de bèta's van de 25 portefeuilles op
de componenten en dan per maand een cross-sectionele regressie op die bèta's. De functie
toont die maandelijkse regressies als lus. Daarnaast vragen we of de factoren alpha's
overlaten, en daarom zet de tabel het model met drie componenten naast het
driefactormodel, met de GRS-toets van Gibbons, Ross en Shanken (of alle alpha's samen
nul zijn).

```{code-cell} ipython3
def two_pass(test_excess, factor_returns):
    """Full-sample betas, then one cross-sectional OLS regression per month.

    Same estimates as hap.fama_macbeth(..., lags=0) with constant betas, without
    statsmodels; TODO: naar hap.stats.
    """
    R = test_excess.to_numpy()
    F = factor_returns.to_numpy()
    coef, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(F)), F]), R, rcond=None)
    Z = np.column_stack([np.ones(R.shape[1]), coef[1:].T])   # N x (K+1): constant and betas
    gammas = []
    for month in range(len(R)):                               # one regression per month
        slopes, *_ = np.linalg.lstsq(Z, R[month], rcond=None)
        gammas.append(slopes)
    gammas = np.array(gammas)                                 # T x (K+1): monthly slopes
    estimate = gammas.mean(axis=0)
    se = gammas.std(axis=0, ddof=1) / np.sqrt(len(gammas))
    return pd.DataFrame({"estimate": estimate, "se": se, "tstat": estimate / se},
                        index=["constante", *factor_returns.columns])


fm_pc3 = two_pass(excess, pcs.iloc[:, :3])
fm_ff3 = two_pass(excess, factors)
alpha_tests = {name: hap.grs_test(excess, f) for name, f in
               [("PC1-3", pcs.iloc[:, :3]), ("Mkt, SMB, HML", factors)]}

pd.DataFrame({
    "PC1-3": [*(fm_pc3["estimate"] * 100), alpha_tests["PC1-3"]["mean_abs_alpha"] * 100,
              alpha_tests["PC1-3"]["grs"], alpha_tests["PC1-3"]["pvalue"]],
    "Mkt, SMB, HML": [*(fm_ff3["estimate"] * 100), alpha_tests["Mkt, SMB, HML"]["mean_abs_alpha"] * 100,
                      alpha_tests["Mkt, SMB, HML"]["grs"], alpha_tests["Mkt, SMB, HML"]["pvalue"]],
}, index=["constante (%/mnd)", "premie factor 1 (%/mnd)", "premie factor 2 (%/mnd)",
          "premie factor 3 (%/mnd)", "gem. |alpha| (%/mnd)", "GRS", "p-waarde GRS"]).round(3)
```

De tabel laat zien dat geen van beide modellen de premies goed vangt. Beide laten een
constante ver boven nul over, het driefactormodel zelfs met een negatieve marktpremie,
en de GRS-toets verwerpt beide. Met drie componenten draagt alleen PC3 een significante
premie.

Dat lijkt de simulatie tegen te spreken, waar gespreide portefeuilles vrijwel juist
gewaardeerd waren, maar het is geen tegenspraak. Voor een gelijkgewogen portefeuille van
$n$ aandelen staat de Huberman-grens een pricing error tot $\sqrt{c/n}$ toe, en de
constante $c$ is onbekend. Voor 25 portefeuilles verbiedt de grens daarom geen enkele
alpha van eindige grootte. Zelfs de kleine $c$ uit de simulatie laat een alpha van 0,09%
per maand toe tot portefeuilles van

$$
n = \frac{c}{0{,}0009^2} = \frac{0{,}002}{0{,}00000081} \approx 2469
$$

aandelen elk. Met 757 maanden data is zo'n alpha wel meetbaar, maar de APT verbiedt hem
niet.

Eerst toetsen we de vier drempels die we vooraf stelden. Roll en Ross rapporteerden geen
principale componenten en geen Fama-French-factoren, zodat er hiervoor geen origineel
bestaat en alleen onze verwachting telt.

```{code-cell} ipython3
r2_smb_hml_on_pcs = min(r2["SMB op PC1, PC2, PC3"], r2["HML op PC1, PC2, PC3"])
r2_pcs_on_ff3 = min(r2[f"{c} op Mkt-RF, SMB, HML"] for c in pcs3.columns)

pd.DataFrame({
    "verwacht (ondergrens)": [0.75, 0.9, 0.85, 0.85],
    "hier": [eigval[0] / eigval.sum(), pcs["PC1"].corr(factors["Mkt-RF"]),
             r2_smb_hml_on_pcs, r2_pcs_on_ff3],
}, index=["aandeel variantie PC1", "correlatie PC1 met Mkt-RF",
          "laagste R2 van SMB en HML op PC1-3",
          "laagste R2 van PC1-3 op Mkt-RF, SMB, HML"]).round(3)
```

Alle vier liggen boven hun ondergrens, dus vergelijken we nu met het origineel hoeveel
factoren een premie dragen.

```{code-cell} ipython3
priced_ts = int((ts.loc[pc_names, "t"].abs() > 1.96).sum())
priced_cs = int((fm_pc3.loc[pc_names[:3], "tstat"].abs() > 1.96).sum())

pd.DataFrame({"origineel (Roll en Ross)": ["3 à 4", "3 à 4"],
              "hier": [priced_ts, priced_cs]},
             index=["componenten met een premie, tijdreeks",
                    "componenten met een premie, cross-sectie (K = 3)"])
```

**Gedeeltelijk geslaagd.** De vier vooraf gestelde drempels worden gehaald, want de
eerste component is de markt en drie componenten spannen vrijwel dezelfde ruimte op als
Mkt, SMB en HML. Het aantal componenten met een premie wijkt af, zoals we vooraf al
mogelijk achtten. In de tijdreeks zijn het er drie, maar in de cross-sectie met drie
componenten maar één, tegen drie à vier bij Roll en Ross. Bij andere $K$ verschuift dat
getal weer, zoals de derde oefening laat zien. Critici van Roll en Ross voerden precies aan
dat het aantal factoren met een premie van de toets en de testactiva afhangt.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De fundamentele stelling is geen model dat kan breken, maar
de grammatica van elk later model. Ze verklaart waarom een optie een prijs heeft zonder
nutsfunctie, waarom risiconeutraal rekenen werkt, en waarom $p = \E[mx]$ met een
positieve $m$ volgt uit het ontbreken van gratis geld. De APT voegt een voorspelling toe
die in de data overeind blijft, namelijk dat een paar richtingen van covariantie de
cross-sectie domineren en dat principale componenten ze terugvinden. In onze 25
portefeuilles zijn dat markt, omvang en waarde. Factorbèta's werden de taal van
risicomodellen.

**Waar het breekt.** Het model breekt op twee plekken. Shanken liet zien dat de
Huberman-grens niet bestand is tegen herverpakken {cite}`Shanken1982`, want dezelfde
economie kan in de ene set testactiva aan de grens voldoen en in een lineaire combinatie
ervan niet. Een grens op een oneindige som is met eindige data bovendien niet te
toetsen. Dybvig en Ross antwoordden {cite}`DybvigRoss1985` dat het CAPM er niet beter
voor staat, omdat de marktportefeuille waarop het steunt niet waarneembaar is
{cite}`Roll1977`. De tweede plek is onze replicatie, waarin drie componenten 93% van de
variantie verklaren maar een constante van 0,84% per maand en alpha's overlaten die de
GRS-toets verwerpt.

**Risico of vergissing?** De APT kiest geen kant. Volgens de Chicago-lezing, die prijzen
als rationeel ziet, zijn SMB en HML dominante richtingen van covariantie en dus risico
dat niet weg te diversifiëren is, zodat de APT er een premie op voorspelt. Volgens de
Yale-lezing, die ruimte laat voor vergissingen van beleggers, ontstaat ook een factor
als beleggers systematisch te enthousiast zijn over groeiaandelen, omdat die vergissing
alle groeiaandelen tegelijk beweegt. Wie zo'n gemeenschappelijke verkeerde prijs
wegarbitreert, draagt het factorrisico, en daar gelden de *limits of arbitrage*
(de grenzen aan wat arbitrageurs met beperkt kapitaal kunnen rechtzetten). De kampen
zouden alleen te scheiden zijn met een premie zonder covariantie, en zulke data zijn
schaars.

**Wat er daarna kwam.** De fundamentele stelling garandeert een positieve SDF maar wijst
er geen aan. Lucas en Breeden gaven $m$ een economische inhoud door de SDF aan
consumptie te binden, in [](#03-12-consumptie-capm).

## Oefeningen

:::{exercise}
:label: ex-apt-no-arbitrage-1

**Instap: een incomplete markt.** Voeg aan het toy-voorbeeld een derde toestand *midden*
toe. De obligatie keert $(1;\ 1;\ 1)$ uit in (goed, midden, slecht) en kost $0{,}90$.
Het aandeel keert $(1{,}40;\ 1{,}00;\ 0{,}60)$ uit en kost $0{,}86$. De call met
uitoefenprijs 1 keert $(0{,}40;\ 0;\ 0)$ uit.

1. Bepaal met de hand alle strikt positieve toestandsprijzen die obligatie en aandeel
   juist waarderen, en leid daaruit het interval van arbitragevrije callprijzen af.
2. Controleer het interval met `scipy.optimize.linprog`, door $\mathbf{q}'\mathbf{y}$ te
   minimaliseren en te maximaliseren onder $\mathbf{X}'\mathbf{q} = \mathbf{p}$ en
   $\mathbf{q} \geq \mathbf{0}$.
:::

:::{solution} ex-apt-no-arbitrage-1
:class: dropdown

**(1)** De voorwaarden zijn $q_g + q_m + q_s = 0{,}90$ en
$1{,}40\,q_g + 1{,}00\,q_m + 0{,}60\,q_s = 0{,}86$. Trek de eerste van de tweede af:
$0{,}40\,q_g - 0{,}40\,q_s = -0{,}04$, dus $q_g = q_s - 0{,}10$. Invullen in de eerste
geeft $q_m = 1{,}00 - 2q_s$. Strikte positiviteit vraagt $0{,}10 < q_s < 0{,}50$. De
toestandsprijzen vormen het open lijnstuk van $(0;\ 0{,}80;\ 0{,}10)$ naar
$(0{,}40;\ 0;\ 0{,}50)$. De callprijs is $0{,}40\,q_g = 0{,}40\,(q_s - 0{,}10)$ en ligt
dus in $(0;\ 0{,}16)$.

**(2)**

```{code-cell} ipython3
X3 = np.array([[1.00, 1.40],
               [1.00, 1.00],
               [1.00, 0.60]])
p3 = np.array([0.90, 0.86])
call3 = np.array([0.40, 0.00, 0.00])

bounds = [optimize.linprog(sign * call3, A_eq=X3.T, b_eq=p3, bounds=[(0, None)] * 3)
          for sign in (1, -1)]
lower, upper = bounds[0].fun, -bounds[1].fun
super_rep = np.linalg.solve(np.array([[1.00, 1.40], [1.00, 0.60]]), np.array([0.40, 0.00]))

pd.Series({"ondergrens": lower, "bovengrens": upper,
           "q bij bovengrens (goed)": bounds[1].x[0], "q bij bovengrens (midden)": bounds[1].x[1],
           "q bij bovengrens (slecht)": bounds[1].x[2],
           "payoff super-replicatie (midden)": X3[1] @ super_rep,
           "kosten super-replicatie": p3 @ super_rep}).round(4)
```

De grenzen zijn 0 en 0,16. De bovengrens is de prijs van het pakket uit stap 4 van het
toy-voorbeeld, want dat pakket maakt de call in *goed* en *slecht* na en keert in
*midden* 0,20 extra uit. In een incomplete markt legt arbitrage dus geen prijs vast maar
een interval, en elke prijs daarbinnen hoort bij een andere SDF.
:::

:::{exercise}
:label: ex-apt-no-arbitrage-2

**Afleiding: de één-stapsboom.** Een aandeel kost 1 en keert morgen $u$ of $d$ uit, met
$u > d$. Een obligatie kost 1 en keert $1 + R^{f}$ uit.

1. Leid [](#eq-apt-no-arbitrage-crr-q) af uit [](#eq-apt-no-arbitrage-drie-namen).
2. Laat met [](#thm-apt-no-arbitrage-fundamenteel) zien dat de markt arbitragevrij is
   dan en slechts dan als $d < 1 + R^{f} < u$. Geef voor $1 + R^{f} \geq u$ een
   expliciete arbitrage.
:::

:::{solution} ex-apt-no-arbitrage-2
:class: dropdown

**(1)** Onder $\boldsymbol{\pi}^{*}$ verdient het aandeel de rente:
$\pi^{*} u + (1 - \pi^{*}) d = 1 + R^{f}$. Oplossen naar $\pi^{*}$ geeft
[](#eq-apt-no-arbitrage-crr-q).

**(2)** Toestandsprijzen lossen $q_u + q_d = 1/(1+R^{f})$ en $u\,q_u + d\,q_d = 1$ op.
Dat geeft

$$
q_u = \frac{1 - d/(1+R^{f})}{u - d}, \qquad q_d = \frac{u/(1+R^{f}) - 1}{u - d}.
$$

Beide zijn strikt positief dan en slechts dan als $d < 1 + R^{f} < u$. Volgens de
stelling is dat equivalent met geen arbitrage. Is $1 + R^{f} \geq u$, dan verkopen we
één aandeel short en beleggen we de opbrengst in de obligatie. Vandaag kost dat niets,
en morgen levert het $1 + R^{f} - u \geq 0$ op in de goede toestand en
$1 + R^{f} - d > 0$ in de slechte. De voorwaarde voor een zinnige binomiale boom is dus
de fundamentele stelling in de kleinste vorm.
:::

:::{exercise}
:label: ex-apt-no-arbitrage-3

**Uitbreiding: andere testactiva.** Herhaal de principale-componentenanalyse van de
replicatie op de 49 bedrijfstakportefeuilles van French
(`hap_data.french("49_Industry_Portfolios")`). Gebruik de data vanaf 1969-07 en alleen
de bedrijfstakken zonder ontbrekende waarden.

1. Welk deel van de variantie verklaart de eerste component, en welk de eerste drie?
2. Wat is de $R^2$ van Mkt-RF, SMB en HML op de eerste drie componenten?
3. Wat zegt het verschil met de 25 size/BM-portefeuilles over de vraag hoeveel factoren
   de economie heeft?
4. Schat voor de 25 size/BM-portefeuilles de premies met `two_pass` op de eerste $K = 1$
   tot en met 5 componenten. Hoeveel premies zijn significant per $K$?
:::

:::{solution} ex-apt-no-arbitrage-3
:class: dropdown

```{code-cell} ipython3
industries = hap_data.french("49_Industry_Portfolios")
ind = industries.join(ff3, how="inner").loc["1969-07":]
ind_excess = ind[industries.columns].dropna(axis=1).sub(ind["RF"], axis=0)
ind_factors = ind[["Mkt-RF", "SMB", "HML"]]

val, vec = np.linalg.eigh(np.cov(ind_excess.to_numpy(), rowvar=False))
val, vec = val[::-1], vec[:, ::-1]
ind_pcs = ind_excess.to_numpy() @ vec[:, :3]

pd.Series({
    "aantal bedrijfstakken": ind_excess.shape[1],
    "aandeel variantie PC1": val[0] / val.sum(),
    "aandeel variantie PC1-3": val[:3].sum() / val.sum(),
    **{f"R2 {c} op PC1-3": r_squared(ind_factors[c].to_numpy(), ind_pcs)
       for c in ind_factors.columns},
}).round(3)
```

De eerste component is ook hier de markt, want de $R^2$ van Mkt-RF op de eerste drie
componenten is 0,92. Toch verklaart die component maar 55% van de variantie, tegen 83%
bij de size/BM-portefeuilles. De eerste drie componenten verklaren SMB voor 17% en HML
voor 3%. Bedrijfstakken zijn niet op omvang en boekwaarde gesorteerd, zodat hun
dominante richtingen andere zijn, vermoedelijk sectorcontrasten. Welke factoren een
principale-componentenanalyse vindt, is dus een eigenschap van de testactiva, en dat is
de empirische kant van de kritiek van {cite:t}`Shanken1982`.

**(4)**

```{code-cell} ipython3
t_values = pd.DataFrame({f"K = {K}": two_pass(excess, pcs.iloc[:, :K])["tstat"]
                         for K in range(1, n_pc + 1)}).reindex(["constante", *pc_names])
t_values.round(2)
```

Het aantal significante premies is achtereenvolgens 0, 2, 1, 1 en 3. Met alleen PC1 is
de constante significant en de premie op PC1 nul, zodat de security market line van
[](#02-08-capm), de lijn van gemiddeld rendement tegen bèta, ook hier vlak is. Het
aantal factoren met een premie hangt dus ook af van hoeveel componenten de onderzoeker
in de regressie opneemt.
:::
