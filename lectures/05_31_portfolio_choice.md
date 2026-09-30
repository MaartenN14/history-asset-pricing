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

(05-31-portfolio-choice)=

# Parametrische portefeuilles en idiosyncratisch risico

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 2001–2016, van de stijgende idiosyncratische volatiliteit bij Campbell, Lettau, Malkiel en Xu tot de gemeenschappelijke factor erin bij Herskovic, Kelly, Lustig en Van Nieuwerburgh. Daartussen liggen de parametrische portefeuilles van Brandt en Santa-Clara (2006) en van Brandt, Santa-Clara en Valkanov (2009).

**Wat we al weten.** Markowitz gaf een exacte theorie van portefeuillekeuze, maar de optimale portefeuille die uit steekproefgemiddelden werd geschat, verloor van de portefeuille met gelijke gewichten ([](#01-04-markowitz)). Intussen stapelden de feiten zich op. Kenmerken als size, value en momentum voorspellen rendementen in de cross-sectie, en in [](#05-30-wisselkoersen) werkten dezelfde signalen ook in valuta.

**Welke vraag staat open.** Hoe bouwt een belegger een portefeuille op feiten die hij slecht kan meten, zonder dat de optimalisator de schattingsfout uitvergroot? En welk risico telt daarbij mee?
```

## Overzicht

Hoe zet een belegger een handvol slecht gemeten feiten om in portefeuillegewichten? Hij
schat niet de verwachte rendementen van duizenden aandelen, maar een paar coëfficiënten
die de gewichten rechtstreeks aan kenmerken en voorspellers koppelen. Dat dempt de
schattingsfout van Markowitz, al kan zo'n regel niet zien of de premie van gisteren morgen
nog bestaat. Welk risico de markt beloont, blijft open, want het resultaat dat de
gemiddelde variantie van aandelen het marktrendement voorspelt, bleef later niet overeind.
In dit college doen we vier dingen:

- we laten met de hand zien dat een regel die op een voorspeller reageert, een vaste mix
  van twee rendementsreeksen is;
- we leiden af dat de coëfficiënten met GMM te schatten zijn en dat hun ruis groeit met
  het aantal kenmerken, niet met het aantal aandelen;
- we simuleren 500 aandelen met kleine premies en vergelijken de regel met 1/N en met
  Markowitz;
- we repliceren de parametrische portefeuille van Brandt, Santa-Clara en Valkanov op 100
  size/BM-portefeuilles, en de regressie van Goyal en Santa-Clara op 49
  industrieportefeuilles.

Rond 2000 vroeg de portefeuilletheorie om de verwachte rendementen van alle activa,
terwijl de empirie zei dat die rendementen met een paar kenmerken samenhangen.
{cite:t}`BrandtSantaClara2006` maakten van een dynamisch probleem een statisch probleem
door geschaalde rendementsreeksen als extra activa toe te voegen.
{cite:t}`BrandtSantaClaraValkanov2009` deden hetzelfde in de cross-sectie, met drie
coëfficiënten voor duizenden aandelen. Santa-Clara noemt dat achteraf een poging om
portefeuillekeuze te bevrijden van de vloek van de dimensionaliteit
{cite}`SantaClara2026`. Het tweede spoor begon toen {cite:t}`GoyalSantaClara2003` vonden
dat de gemiddelde variantie van aandelen het marktrendement voorspelt. De marktvariantie
deed dat niet, in strijd met [](#02-08-capm), maar ook dat resultaat hield geen stand
{cite}`BaliCakiciYanZhang2005,WeiZhang2005`. Idiosyncratische volatiliteit bleef intussen
een raadsel
{cite}`CampbellLettauMalkielXu2001,AngHodrickXingZhang2006,HerskovicKellyLustigVanNieuwerburgh2016`.
Op de vraag theorie of feit geeft dit college dus feiten als antwoord. De regel gebruikt
kenmerken zonder ze te verklaren, en voor de volatiliteitsfeiten zijn er meer theorieën
dan data om ze te scheiden.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een belegger die gelooft dat kleine, goedkope aandelen met een goed afgelopen
jaar beter renderen. Markowitz vraagt hem een verwacht rendement voor elk van duizenden
aandelen en een covariantiematrix met een miljoen elementen, en de optimalisator zoekt
daarin juist de slechtst geschatte richtingen op. Brandt, Santa-Clara en Valkanov vragen
alleen hoeveel hij van de markt wil afwijken per eenheid "klein", "goedkoop" en "goed
jaar". Dat zijn drie getallen, en omdat hij ze uit alle aandelen tegelijk schat, middelt
de bedrijfsspecifieke ruis grotendeels weg.

Afwijken van de markt in verhouding tot een kenmerk komt neer op de markt houden plus een
portefeuille die aandelen met een hoog kenmerk koopt en met een laag kenmerk verkoopt. De
belegger kiest dus tussen een paar portefeuilles en niet tussen duizenden aandelen. In de
tijd werkt het net zo. Wie meer aandelen houdt als de dividendopbrengst hoog is, bezit
naast de markt een vaste positie in de markt geschaald met de dividendopbrengst, en die
positie is gewoon een activum met een eigen rendementsreeks. Zo wordt het dynamische
probleem van Merton een statisch probleem van Markowitz.

De regel helpt tegen schattingsfout, omdat twee aandelen met dezelfde kenmerken hetzelfde
gewicht krijgen, wat hun historische gemiddelde ook was. Om dezelfde reden wint 1/N van
mean-variance, en de parametrische portefeuille zit tussen die twee in.

Goyal en Santa-Clara vroegen welk risico de markt beloont. Voor een gediversifieerde
belegger is dat alleen marktrisico, maar de meeste huishoudens bezitten een handvol
aandelen, en voor hen is bedrijfsspecifiek risico gewoon risico. Stijgt de onzekerheid
over individuele bedrijven, dan eisen ze misschien een hogere premie op de hele markt.

We verwachten daarom dat de parametrische regel de markt verslaat zodra de steekproef lang
genoeg is om de premies te zien. Van schattingsfout zou hij veel minder last moeten hebben
dan Markowitz. Als het argument over huishoudens klopt, gaat bovendien een hoge gemiddelde
variantie van aandelen vooraf aan een hoog marktrendement, terwijl de marktvariantie
weinig zegt.

## Toy-voorbeeld: een voorspeller met twee waarden, drie aandelen met één kenmerk

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize, signal

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

Het voorbeeld heeft twee delen, één in de tijd en één in de cross-sectie, en beide keren
blijkt de regel een vaste mix van een paar rendementsreeksen.

### (a) Dynamisch wordt statisch

Hier stuurt een voorspeller de positie in de tijd. Eén risicovol activum heeft
overrendement $r_{t+1}$, en
een voorspeller $x_t$ neemt met gelijke kans de waarden $-1$ (laag) en $+1$ (hoog) aan. De
belegger maximaliseert
kwadratisch nut $\E[w_t r_{t+1} - \tfrac{\gamma}{2}(w_t r_{t+1})^2]$ met
risicoaversiecoëfficiënt $\gamma = 5$. De tabel bevat alles wat hij nodig heeft, met $s(x) = \E[r_{t+1}^2 \mid x] = \sigma^2 + \mu(x)^2$
het tweede moment.

| | laag, $x_t = -1$ | hoog, $x_t = +1$ |
|---|---|---|
| kans | 1/2 | 1/2 |
| verwacht overrendement $\mu(x)$ | 2% | 10% |
| conditionele variantie $\sigma^2$ | 0,04 | 0,04 |
| tweede moment $s(x)$ | 0,0404 | 0,05 |

We hebben één formule nodig, de optimale positie bij kwadratisch nut, $w = \mu/(\gamma s)$,
of in matrixvorm $\boldsymbol{\theta} = \gamma^{-1}\E[\tilde{\mathbf{R}}\tilde{\mathbf{R}}']^{-1}\E[\tilde{\mathbf{R}}]$.
De theorie leidt die formule straks als eerste af.

1. Per toestand is $w_{\text{laag}} = 0{,}02/(5 \cdot 0{,}0404) = 0{,}09901$ en
   $w_{\text{hoog}} = 0{,}10/(5 \cdot 0{,}05) = 0{,}40$.
2. Als tweede activum nemen we $x_t r_{t+1}$, een strategie die in de hoge toestand één
   eenheid koopt en in de lage toestand één eenheid verkoopt. Voor de twee betalingen
   $\tilde{\mathbf{R}}_{t+1} = (r_{t+1},\, x_t r_{t+1})'$ geldt, omdat $x^2 = 1$,

$$
\E[\tilde{\mathbf{R}}] = \begin{pmatrix} \tfrac12(0{,}02 + 0{,}10) \\ \tfrac12(0{,}10 - 0{,}02)\end{pmatrix}
= \begin{pmatrix} 0{,}06 \\ 0{,}04 \end{pmatrix},
\qquad
\E[\tilde{\mathbf{R}}\tilde{\mathbf{R}}'] =
\begin{pmatrix} 0{,}0452 & 0{,}0048 \\ 0{,}0048 & 0{,}0452 \end{pmatrix},
$$

   met $\E[r^2] = \tfrac12(0{,}0404 + 0{,}05)$ en $\E[x r^2] = \tfrac12(0{,}05 - 0{,}0404)$.
3. De determinant is $0{,}0452^2 - 0{,}0048^2 = 0{,}00202$, zodat de vaste mix gelijk is aan

$$
\theta = \frac{1}{5 \cdot 0{,}00202}
\begin{pmatrix} 0{,}0452 \cdot 0{,}06 - 0{,}0048 \cdot 0{,}04 \\ -0{,}0048 \cdot 0{,}06 + 0{,}0452 \cdot 0{,}04 \end{pmatrix}
= \frac{1}{0{,}0101}\begin{pmatrix} 0{,}00252 \\ 0{,}00152\end{pmatrix}
= \begin{pmatrix} 0{,}24950 \\ 0{,}15050 \end{pmatrix}.
$$

4. De regel die daarbij hoort, is $w_t = \theta_0 + \theta_1 x_t$, dus $0{,}24950 - 0{,}15050 = 0{,}09901$
   in de lage en $0{,}24950 + 0{,}15050 = 0{,}40$ in de hoge toestand.
5. Het verwachte nut is met de voorspeller $\sum_x \tfrac12\,\mu(x)^2/(2\gamma s(x)) = \tfrac12(0{,}00099 + 0{,}02) = 0{,}010495$.
   Zonder voorspeller is de beste vaste positie $\E[r]/(\gamma\E[r^2]) = 0{,}2655$, met
   verwacht nut $\E[r]^2/(2\gamma\E[r^2]) = 0{,}0036/0{,}452 = 0{,}007965$.

De cel rekent dezelfde stappen na en zet hand en code naast elkaar.

```{code-cell} ipython3
gamma = 5.0
prob = np.array([0.5, 0.5])
mu_state = np.array([0.02, 0.10])            # E[r | low], E[r | high]
x_state = np.array([-1.0, 1.0])
s_state = 0.04 + mu_state**2                 # E[r^2 | x]

# conditional optimum, state by state
w_conditional = mu_state / (gamma * s_state)

# static optimum over the two payoffs (r, x r)
payoff = np.column_stack([np.ones(2), x_state])          # (r, x r) = payoff * r
mean_managed = (prob * mu_state) @ payoff
second_moment = (payoff.T * (prob * s_state)) @ payoff
theta_managed = np.linalg.solve(second_moment, mean_managed) / gamma
w_static = theta_managed[0] + theta_managed[1] * x_state

utility_timing = prob @ (mu_state**2 / (2 * gamma * s_state))
utility_fixed = (prob @ mu_state) ** 2 / (2 * gamma * (prob @ s_state))

pd.DataFrame(
    {"met de hand": [0.09901, 0.40, 0.24950, 0.15050, 0.09901, 0.40, 0.010495, 0.007965],
     "code": [*w_conditional, *theta_managed, *w_static, utility_timing, utility_fixed]},
    index=["w laag, per toestand", "w hoog, per toestand", "theta0", "theta1",
           "w laag = theta0 - theta1", "w hoog = theta0 + theta1",
           "verwacht nut met voorspeller", "verwacht nut zonder voorspeller"],
).round(6)
```

Code en hand geven dezelfde getallen. Een vaste mix van twee rendementsreeksen doet dus
precies wat de belegger doet die per toestand opnieuw optimaliseert, en ongeveer een kwart
van zijn verwachte nut komt van de voorspeller.

### (b) Een parametrische regel met drie aandelen

Drie aandelen hebben marktgewichten $\bar w_i$ en één kenmerk, het momentum van het
afgelopen jaar. Over de cross-sectie is het gemiddelde momentum 5% en de standaarddeviatie
15%, zodat het gestandaardiseerde kenmerk $\hat x_i$ de waarden $-1$, $0$ en $1$ krijgt.
De regel van Brandt, Santa-Clara en Valkanov tilt elk marktgewicht op in verhouding tot
het kenmerk,

$$
w_i(\theta) = \bar w_i + \frac{\theta\, \hat{x}_i}{N},\qquad N = 3 .
$$

| aandeel | marktgewicht $\bar w_i$ | momentum | $\hat x_i$ | rendement periode 1 | rendement periode 2 |
|---|---|---|---|---|---|
| 1 | 0,5 | −10% | −1 | −3% | 4% |
| 2 | 0,3 | 5% | 0 | 1% | 1% |
| 3 | 0,2 | 20% | 1 | 6% | −5% |

1. Omdat de $\hat x_i$ optellen tot nul, tellen de gewichten altijd op tot één. Bij
   $\theta = 0$ zijn ze $(0{,}5;\ 0{,}3;\ 0{,}2)$, bij $\theta = 1{,}5$ zijn ze $(0;\ 0{,}3;\ 0{,}7)$.
2. In periode 1 rendeert de portefeuille bij $\theta = 0$ precies $0{,}5(-0{,}03) + 0{,}3(0{,}01) + 0{,}2(0{,}06) = 0$
   en bij $\theta = 1{,}5$ precies $0{,}3(0{,}01) + 0{,}7(0{,}06) = 4{,}5\%$.
3. Met CRRA-nut $u(R) = R^{1-\gamma}/(1-\gamma)$ en $\gamma = 5$, het nut dat Brandt,
   Santa-Clara en
   Valkanov zelf gebruiken, is het gerealiseerde nut
   $u(1{,}000) = -0{,}25$ en $u(1{,}045) = -1/(4 \cdot 1{,}19252) = -0{,}20964$.
4. Het portefeuillerendement is $\bar R + \theta\, r^{x}$, met $r^{x} = \tfrac13(0{,}03 + 0 + 0{,}06) = 3\%$
   het rendement van een kenmerkportefeuille die aandeel 3 koopt en aandeel 1 verkoopt.
   Bij één periode stijgt het nut daarom met elke extra eenheid $\theta$ zolang $r^x > 0$,
   al blijft het onder nul, zodat één periode geen optimum oplevert.
5. In periode 2 is $\bar R = 1{,}3\%$ en $r^x = -3\%$. Het gemiddelde nut $\tfrac12[u(1 + 0{,}03\theta) + u(1{,}013 - 0{,}03\theta)]$
   is maximaal waar de twee brutorendementen gelijk zijn, bij $\theta^{\ast} = 0{,}013/0{,}06 = 0{,}2167$.

De cel berekent de gewichten, het nut en het optimum over twee perioden.

```{code-cell} ipython3
w_bar = np.array([0.5, 0.3, 0.2])
momentum_raw = np.array([-0.10, 0.05, 0.20])
x_hat = (momentum_raw - momentum_raw.mean()) / momentum_raw.std(ddof=1)
returns_1 = np.array([-0.03, 0.01, 0.06])
returns_2 = np.array([0.04, 0.01, -0.05])

def toy_policy(theta):
    """BSV weights for the three-stock example."""
    return w_bar + theta * x_hat / len(x_hat)

def crra(R, g=5.0):
    return R ** (1 - g) / (1 - g)

def mean_utility(theta):
    """Average realised CRRA utility over the two periods."""
    return (crra(1 + toy_policy(theta) @ returns_1) + crra(1 + toy_policy(theta) @ returns_2)) / 2

theta_star = optimize.minimize_scalar(lambda th: -mean_utility(th), bounds=(-5, 5), method="bounded").x
pd.DataFrame(
    {"met de hand": [1.0, 0.7, 1.045, -0.25, -0.20964, 0.03, 0.013 / 0.06],
     "code": [x_hat[2], toy_policy(1.5)[2], 1 + toy_policy(1.5) @ returns_1,
              crra(1 + toy_policy(0.0) @ returns_1), crra(1 + toy_policy(1.5) @ returns_1),
              x_hat @ returns_1 / 3, theta_star]},
    index=["x_hat aandeel 3", "w3 bij theta = 1,5", "R_p bij theta = 1,5", "nut bij theta = 0",
           "nut bij theta = 1,5", "r^x in periode 1", "theta* over twee perioden"],
).round(4)
```

Ook hier geven code en hand dezelfde getallen. Omdat de kenmerkportefeuille in de ene
periode wint en in de andere verliest, kiest de belegger een kleine positieve
$\theta^{\ast} = 0{,}2167$. Het gewicht op aandeel 3 stijgt daardoor met $\theta^{\ast}/3$,
ruim zeven procentpunt, en dat op aandeel 1 zakt evenveel.

## Theorie

De theorie volgt twee sporen. Het eerste laat zien dat een conditionele portefeuilleregel
een statische keuze is tussen *managed portfolios*, rendementsreeksen die met een signaal
zijn geschaald, eerst in de tijd en dan in de cross-sectie. Daaruit volgt waarom de regel
de schattingsfout van Markowitz indamt, want zijn ruis groeit met het aantal kenmerken $K$
en niet met het aantal aandelen $N$. Het tweede spoor splitst de gemiddelde variantie van
aandelen in een markt- en een afwijkingsdeel en formuleert zo de toets van Goyal en
Santa-Clara.

### Brandt en Santa-Clara: een conditionele regel als vaste mix

Een belegger die zijn positie lineair aanpast aan wat hij
ziet, verdient elke periode een vaste combinatie van producten van signaal en rendement.
Zo'n product is een rendementsreeks met schatbare momenten, net als een aandeel. Een vaste
mix van vaste reeksen kiezen is precies het probleem van Markowitz, en zolang de regel elke
toestand apart kan behandelen, kost die omweg de belegger niets.

Stel dat er $N$ risicovolle activa zijn met overrendementen $\mathbf{r}_{t+1}$. Daarnaast
zijn er $K$ conditioneringsvariabelen $\mathbf{x}_t$ die op $t$ bekend zijn, met een
constante als eerste element en bijvoorbeeld de dividendopbrengst als tweede. Een lineaire
regel is $\mathbf{w}_t = \boldsymbol{\Theta}\mathbf{x}_t$, met $\boldsymbol{\Theta}$ een
$N \times K$-matrix van coëfficiënten. Het rendement van de portefeuille is dan

```{math}
:label: eq-portfolio-choice-managed
\mathbf{w}_t'\mathbf{r}_{t+1} = \mathbf{x}_t'\boldsymbol{\Theta}'\mathbf{r}_{t+1}
= \boldsymbol{\theta}'\left(\mathbf{x}_t \otimes \mathbf{r}_{t+1}\right),
\qquad \boldsymbol{\theta} = \mathrm{vec}(\boldsymbol{\Theta}) .
```

Het rendement van de regel is dus een vaste combinatie van $NK$ managed portfolios
$\tilde{\mathbf{R}}_{t+1} = \mathbf{x}_t \otimes \mathbf{r}_{t+1}$, waarin activum $i$ met
variabele $k$ is geschaald. {cite:t}`BrandtSantaClara2006` werken met een
mean-variance-benadering van het nut. Wij nemen kwadratisch nut in het tweede moment,
omdat de gelijkwaardigheid dan exact is.

:::{prf:proposition} Conditionele keuze als statische keuze (Brandt-Santa-Clara)
:label: thm-portfolio-choice-bsc

Laat de toestand $z_t$ waarden aannemen in $\{z^1, \dots, z^K\}$ met kansen $p_k > 0$, en laat $\boldsymbol{\mu}_k = \E[\mathbf{r}_{t+1} \mid z_t = z^k]$ en $\mathbf{S}_k = \E[\mathbf{r}_{t+1}\mathbf{r}_{t+1}' \mid z_t = z^k]$ positief definiet zijn. De belegger maximaliseert $\E[\mathbf{w}_t'\mathbf{r}_{t+1} - \tfrac{\gamma}{2}(\mathbf{w}_t'\mathbf{r}_{t+1})^2]$.

1. De conditioneel optimale regel is $\mathbf{w}^{\ast}(z^k) = \gamma^{-1}\mathbf{S}_k^{-1}\boldsymbol{\mu}_k$.
2. Laat $\mathbf{x}_t = \mathbf{A}\,\mathbf{e}(z_t)$, met $\mathbf{e}(z^k)$ de $k$-de eenheidsvector en $\mathbf{A}$ een inverteerbare $K\times K$-matrix. Het statische probleem $\max_{\boldsymbol{\theta}} \E[\boldsymbol{\theta}'\tilde{\mathbf{R}}] - \tfrac{\gamma}{2}\E[(\boldsymbol{\theta}'\tilde{\mathbf{R}})^2]$ heeft de unieke oplossing
   ```{math}
   :label: eq-portfolio-choice-bsc-theta
   \boldsymbol{\theta}^{\ast} = \frac1\gamma\,\E\!\left[\tilde{\mathbf{R}}\tilde{\mathbf{R}}'\right]^{-1}\E\!\left[\tilde{\mathbf{R}}\right],
   ```
   en de bijbehorende regel $\boldsymbol{\Theta}^{\ast}\mathbf{x}_t$ is in elke toestand gelijk aan $\mathbf{w}^{\ast}(z_t)$.
3. Is $z_t$ continu en $\mathbf{x}_t = (1, z_t)'$, dan levert [](#eq-portfolio-choice-bsc-theta) de beste regel binnen de klasse van affiene regels.
:::

:::{prf:proof}
:class: dropdown

(1) Gegeven $z_t = z^k$ is het doel $\mathbf{w}'\boldsymbol{\mu}_k - \tfrac{\gamma}{2}\mathbf{w}'\mathbf{S}_k\mathbf{w}$, strikt concaaf, met eerste-ordevoorwaarde $\boldsymbol{\mu}_k = \gamma\mathbf{S}_k\mathbf{w}$. (2) Neem eerst $\mathbf{A} = \mathbf{I}$. Dan is $\boldsymbol{\theta}'\tilde{\mathbf{R}}_{t+1} = \boldsymbol{\theta}_k'\mathbf{r}_{t+1}$ in toestand $k$, met $\boldsymbol{\theta}_k$ het $k$-de blok van $\boldsymbol{\theta}$. Met de wet van de herhaalde verwachtingen is het doel $\sum_k p_k\big(\boldsymbol{\theta}_k'\boldsymbol{\mu}_k - \tfrac{\gamma}{2}\boldsymbol{\theta}_k'\mathbf{S}_k\boldsymbol{\theta}_k\big)$, een som van $K$ problemen die elk alleen van hun eigen blok afhangen en elk door (1) worden opgelost. Tegelijk is $\E[\tilde{\mathbf{R}}\tilde{\mathbf{R}}']$ blokdiagonaal met blokken $p_k\mathbf{S}_k$, en $\E[\tilde{\mathbf{R}}]$ heeft blokken $p_k\boldsymbol{\mu}_k$, zodat [](#eq-portfolio-choice-bsc-theta) blok voor blok $\gamma^{-1}\mathbf{S}_k^{-1}\boldsymbol{\mu}_k$ geeft.

Voor algemene $\mathbf{A}$ is $\tilde{\mathbf{R}}^{A} = (\mathbf{A}\otimes\mathbf{I})\tilde{\mathbf{R}}$. De verzameling bereikbare rendementen $\{\boldsymbol{\theta}'\tilde{\mathbf{R}}^{A}\}$ is dezelfde, en dus ook het optimale rendement en de regel, met $\boldsymbol{\theta}^{A} = (\mathbf{A}'\otimes\mathbf{I})^{-1}\boldsymbol{\theta}^{\ast}$. Uniciteit volgt uit de positieve definietheid van $\E[\tilde{\mathbf{R}}\tilde{\mathbf{R}}']$. (3) Elke affiene regel is van de vorm $\boldsymbol{\theta}'\tilde{\mathbf{R}}$ en het doel is strikt concaaf in $\boldsymbol{\theta}$, zodat [](#eq-portfolio-choice-bsc-theta) de eerste-ordevoorwaarde is. $\square$

:::

Het bewijs werkt, omdat een indicator voor de toestand het statische probleem opknipt in
$K$ losse problemen, één per toestand. Een inverteerbare transformatie $\mathbf{A}$ van
die indicatoren verandert de bereikbare rendementen niet. In het toy-voorbeeld is
$\mathbf{A} = \begin{pmatrix}1 & 1\\ -1 & 1\end{pmatrix}$, zodat $\theta_0 = 0{,}24950$
het gemiddelde en $\theta_1 = 0{,}15050$ het halve verschil van de twee conditionele
posities is.

Vergelijking [](#eq-portfolio-choice-bsc-theta) is de coëfficiënt van een regressie van de
constante 1 op $\tilde{\mathbf{R}}_{t+1}$ zonder intercept {cite}`BrittenJones1999`, zodat
een gewone regressie de gewichten al oplevert. Gratis is de truc toch niet, want met $N$
activa en $K$ variabelen is het statische probleem een
Markowitz-probleem in $NK$ activa, met alle schattingsfout van dien.

### Brandt, Santa-Clara en Valkanov: de cross-sectie in drie parameters

In de cross-sectie verschilt de conditioneringsvariabele niet tussen perioden maar tussen
aandelen, en dan volstaan $K$ coëfficiënten voor duizenden aandelen. Verschillen verwachte
rendementen alleen via kenmerken, dan hangt ook de optimale afwijking van de markt alleen
van die kenmerken af. Neemt de belegger die afwijking lineair, met dezelfde coëfficiënten
voor elk aandeel, dan heeft het probleem evenveel onbekenden als er kenmerken zijn.

Op elk tijdstip $t$ zijn er $N_t$ aandelen, in het artikel gemiddeld 3.680 per maand
{cite}`BrandtSantaClaraValkanov2009`, met
marktgewichten $\bar w_{i,t}$ als benchmark. Elk aandeel heeft $K$ kenmerken, bijvoorbeeld
de log marktwaarde, en die worden per maand over de cross-sectie gestandaardiseerd tot
gemiddelde nul en standaarddeviatie één, $\hat{\mathbf{x}}_{i,t}$. De regel is

```{math}
:label: eq-portfolio-choice-bsv
w_{i,t}(\boldsymbol{\theta}) = \bar w_{i,t} + \frac{1}{N_t}\,\boldsymbol{\theta}'\hat{\mathbf{x}}_{i,t} .
```

De deling door $N_t$ houdt de totale afwijking van de markt gelijk als het aantal aandelen
groeit, en door de standaardisatie blijft $\boldsymbol{\theta}$ over de tijd
vergelijkbaar. Omdat $\sum_i \hat{\mathbf{x}}_{i,t} = \mathbf{0}$, tellen de gewichten op
tot één, en het portefeuillerendement is

```{math}
:label: eq-portfolio-choice-rp
R_{p,t+1}(\boldsymbol{\theta}) = \bar R_{t+1} + \boldsymbol{\theta}'\mathbf{r}^{x}_{t+1},
\qquad
\mathbf{r}^{x}_{t+1} = \frac{1}{N_t}\sum_{i=1}^{N_t}\hat{\mathbf{x}}_{i,t}\,R_{i,t+1} .
```

Hier is $\bar R_{t+1}$ het brutorendement van de markt. De vector $\mathbf{r}^{x}_{t+1}$
bevat de rendementen van $K$ kenmerkportefeuilles die niets kosten, omdat ze aandelen met
een hoog kenmerk kopen en met een laag kenmerk verkopen. In het toy-voorbeeld was $r^x$ in
de eerste periode 3%, en de regel is dus de cross-sectionele versie van
[](#eq-portfolio-choice-managed), een statische keuze tussen de markt en $K$ managed
portfolios.

{cite:t}`BrandtSantaClaraValkanov2009` schatten $\boldsymbol{\theta}$ met CRRA-nut en
$\gamma = 5$, zoals in het toy-voorbeeld. Er komt geen verwacht rendement en geen
covariantiematrix aan te pas, en omdat het nut de hele verdeling ziet, tellen ook
scheefheid en dikke staarten mee. De schatter maximaliseert het gemiddelde gerealiseerde
nut in de steekproef,

```{math}
:label: eq-portfolio-choice-doel
\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta}}\ \frac{1}{T}\sum_{t=0}^{T-1}
u\!\left(\bar R_{t+1} + \boldsymbol{\theta}'\mathbf{r}^{x}_{t+1}\right),
\qquad u(R) = \frac{R^{1-\gamma}}{1-\gamma} .
```

:::{prf:proposition} Eerste-ordevoorwaarden en asymptotische verdeling
:label: thm-portfolio-choice-bsv-gmm

Laat $\{(\bar R_{t+1}, \mathbf{r}^{x}_{t+1})\}$ stationair en ergodisch zijn. Laat verder $\boldsymbol{\theta}_0$ het unieke maximum van $\E[u(\bar R_{t+1} + \boldsymbol{\theta}'\mathbf{r}^{x}_{t+1})]$ in het inwendige van een compacte verzameling zijn, en schrijf $\mathbf{h}_{t+1}(\boldsymbol{\theta}) = u'(R_{p,t+1}(\boldsymbol{\theta}))\,\mathbf{r}^{x}_{t+1}$. Dan

1. voldoet $\hat{\boldsymbol{\theta}}$ aan de $K$ momentvoorwaarden $\frac1T\sum_t \mathbf{h}_{t+1}(\hat{\boldsymbol{\theta}}) = \mathbf{0}$, de steekproefversie van
   ```{math}
   :label: eq-portfolio-choice-foc
   \E\!\left[u'\!\left(R_{p,t+1}(\boldsymbol{\theta}_0)\right)\mathbf{r}^{x}_{t+1}\right] = \mathbf{0};
   ```
2. geldt, als $\mathbf{h}_{t+1}(\boldsymbol{\theta}_0)$ geen autocorrelatie heeft,
   ```{math}
   :label: eq-portfolio-choice-avar
   \sqrt{T}\,(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0) \xrightarrow{d}
   \mathcal{N}\!\left(\mathbf{0},\ \mathbf{G}^{-1}\mathbf{V}\mathbf{G}^{-1}\right),
   \quad
   \mathbf{G} = \E\!\left[u''(R_{p})\,\mathbf{r}^{x}\mathbf{r}^{x\prime}\right],
   \quad
   \mathbf{V} = \E\!\left[u'(R_{p})^2\,\mathbf{r}^{x}\mathbf{r}^{x\prime}\right].
   ```
:::

:::{prf:proof}
:class: dropdown

(1) Het doel in [](#eq-portfolio-choice-doel) is glad en strikt concaaf in $\boldsymbol{\theta}$ zolang $R_p > 0$, want $u'' < 0$, en de gradiënt is $\frac1T\sum_t u'(R_{p,t+1})\mathbf{r}^{x}_{t+1}$. Het maximum ligt dus waar die gradiënt nul is. Consistentie volgt uit de uniforme wet van de grote aantallen voor het doel en de identificatievoorwaarde (een uniek maximum).

(2) Een middelwaardestelling rond $\boldsymbol{\theta}_0$ geeft $\mathbf{0} = \frac1T\sum_t \mathbf{h}_{t+1}(\boldsymbol{\theta}_0) + \big[\frac1T\sum_t\partial\mathbf{h}_{t+1}(\bar{\boldsymbol{\theta}})/\partial\boldsymbol{\theta}'\big](\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0)$, met $\bar{\boldsymbol{\theta}}$ tussen $\hat{\boldsymbol{\theta}}$ en $\boldsymbol{\theta}_0$ en $\partial\mathbf{h}_{t+1}/\partial\boldsymbol{\theta}' = u''(R_{p,t+1})\mathbf{r}^{x}_{t+1}\mathbf{r}^{x\prime}_{t+1}$. De haakjesterm convergeert naar $\mathbf{G}$, en $\frac{1}{\sqrt T}\sum_t\mathbf{h}_{t+1}(\boldsymbol{\theta}_0)$ convergeert naar $\mathcal{N}(\mathbf{0}, \mathbf{V})$ door een centrale limietstelling voor martingaalverschillen. Vermenigvuldigen met $-\mathbf{G}^{-1}$ geeft [](#eq-portfolio-choice-avar). Bij autocorrelatie vervangt een Newey-West-schatter $\mathbf{V}$. $\square$
:::

De schatter is dus een exact geïdentificeerde GMM-schatter {cite}`Hansen1982`, en de
sandwichformule [](#eq-portfolio-choice-avar) levert de standaardfouten die we in de
replicatie gebruiken. De voorwaarde [](#eq-portfolio-choice-foc) heeft bovendien een
economische lezing. Met $m_{t+1} \propto u'(R_{p,t+1})$ staat er
$\E[m_{t+1}\mathbf{r}^{x}_{t+1}] = 0$, zodat het marginale nut van de belegger zelf de $K$
kenmerkportefeuilles een prijs van nul geeft. Dat is de waarderingsvergelijking $p = \E[mx]$
uit [](#05-26-sdf-unificatie), toegepast op betalingen die niets kosten.

### Wat het voorspelt: ruis van orde $K$ in plaats van $N$

De parametrische regel schat $K$ getallen, elk voor een portefeuille die over alle
aandelen middelt. Markowitz laat daarentegen $N$ slecht geschatte gemiddelden door
$\boldsymbol{\Sigma}^{-1}$ uitvergroten. Twee berekeningen maken dat verschil concreet.
Laat het overrendement van aandeel $i$ gelijk zijn aan
$R^{e}_{i,t+1} = \beta_i f_{t+1} + \boldsymbol{\lambda}'\hat{\mathbf{x}}_{i,t} + \varepsilon_{i,t+1}$,
met marktfactor $f$, premies $\boldsymbol{\lambda}$ per eenheid kenmerk en onafhankelijke
idiosyncratische ruis met variantie $\sigma_\varepsilon^2$. Dan is

$$
\mathbf{r}^{x}_{t+1} = \Big(\tfrac1{N}\textstyle\sum_i \hat{\mathbf{x}}_{i,t}\beta_i\Big) f_{t+1}
+ \Big(\tfrac1{N}\textstyle\sum_i \hat{\mathbf{x}}_{i,t}\hat{\mathbf{x}}_{i,t}'\Big)\boldsymbol{\lambda}
+ \tfrac1{N}\textstyle\sum_i \hat{\mathbf{x}}_{i,t}\varepsilon_{i,t+1}.
$$

De laatste term heeft variantie $\sigma_\varepsilon^2/N$ per kenmerk. Bij ruis van 12% per
maand en 500 aandelen, zoals in de simulatie, is de standaarddeviatie van die term
$12/\sqrt{500} \approx 0{,}54\%$ per maand in plaats van 12%. Het gemiddelde van een
kenmerkportefeuille is dus veel beter te schatten dan dat van één aandeel. Ook de
opwaartse vertekening van de Sharpe-ratio in de steekproef groeit met $K/T$ in plaats van
de $N/T$ uit [](#01-04-markowitz) {cite}`JobsonKorkie1980`, omdat de optimalisator maar
$K$ richtingen heeft om ruis in te vinden. Bij duizend aandelen en drie kenmerken scheelt
dat een factor van ruim driehonderd.

De schatter wordt dus stabieler naarmate hij over meer aandelen middelt, al betaalt de
belegger daarvoor met de aanname dat alleen lineaire verschillen in $\hat{\mathbf{x}}$
tellen. Of de regel de markt ook verslaat, hangt af van de premies $\boldsymbol{\lambda}$
ten opzichte van de resterende ruis. In de simulatie staat 0,03% per maand tegen 0,54%,
en daar blijkt hoe lang de belegger moet wachten.

Met mean-variance in plaats van CRRA-nut wordt het verband met Markowitz exact.
Maximaliseren we $\E[R_p] - \tfrac{\gamma}{2}\Var(R_p)$, dan is

```{math}
:label: eq-portfolio-choice-mv
\boldsymbol{\theta}^{\mathrm{mv}} = \boldsymbol{\Sigma}_x^{-1}\Big(\frac{1}{\gamma}\boldsymbol{\mu}_x - \Cov(\mathbf{r}^{x}, \bar R)\Big),
\qquad \boldsymbol{\mu}_x = \E[\mathbf{r}^{x}],\ \boldsymbol{\Sigma}_x = \Var(\mathbf{r}^{x}) .
```

De regel vraagt dus naar $K$ kenmerkportefeuilles zoals Markowitz naar activa vraagt, plus
een hedgeterm voor de benchmark. De matrix die de regel inverteert, is maar $K\times K$ en
bevat rendementen waaruit de ruis grotendeels is weggemiddeld, terwijl Markowitz de
$N\times N$-matrix van [](#01-04-markowitz) inverteert. Stijgt
$\gamma$, dan krimpt de speculatieve term $\boldsymbol{\mu}_x/\gamma$ en blijft de
belegger dichter bij de markt. Oefening 2 leidt de formule af.

De afleiding negeert short-beperkingen en kosten, en daarom krijgt de regel
in de praktijk twee aanpassingen. De lineaire regel kan negatieve gewichten geven, vooral
voor kleine aandelen met een klein marktgewicht, en een
long-only-versie kapt die af en normaliseert:

```{math}
:label: eq-portfolio-choice-longonly
w^{+}_{i,t} = \frac{\max(0, w_{i,t})}{\sum_j \max(0, w_{j,t})} .
```

Omdat het doel met afgekapte gewichten niet meer glad is, schatten we
$\boldsymbol{\theta}$ dan met een zoekmethode zonder afgeleiden. Transactiekosten komen in
het doel als $c\sum_i |w_{i,t+1} - w^{\mathrm{drift}}_{i,t}|$, met $w^{\mathrm{drift}}$
het gewicht na de koersbeweging. Met de kosten in het doel kiest de schatter van
{cite:t}`BrandtSantaClaraValkanov2009` vanzelf een regel met minder omzet. Hij
maximaliseert dan het *certainty equivalent* na kosten, het zekere rendement dat de
belegger even hoog waardeert als de strategie.

### Goyal en Santa-Clara: welk risico voorspelt de markt?

Goyal en Santa-Clara toetsen of de gemiddelde variantie van individuele aandelen het
marktrendement voorspelt, naast of in plaats van de marktvariantie. Volgens het CAPM zou
alleen de marktvariantie dat doen, maar voor de onvolledig gespreide huishoudens uit de
intuïtie telt juist het bedrijfsspecifieke risico.

De variantie van aandeel $i$ in maand $t$ meten we met dagrendementen, $\hat\sigma^2_{i,t} = \sum_{d \in t} R_{i,d}^2$,
en voor de markt op dezelfde manier. De toets van {cite:t}`GoyalSantaClara2003` is

```{math}
:label: eq-portfolio-choice-gsc
R^{e}_{m,t+1} = a + b\,V_t + c\,\hat\sigma^2_{m,t} + e_{t+1},
\qquad
V_t = \frac{1}{N_t}\sum_{i=1}^{N_t}\hat\sigma^2_{i,t} ,
```

met $R^{e}_{m,t+1}$ het overrendement van de markt en $V_t$ de gelijkgewogen gemiddelde
variantie van de aandelen. Volgens de hypothese is $b$ positief en $c$ hooguit klein. Dat
$V_t$ grotendeels idiosyncratisch is, volgt uit een identiteit.

:::{prf:proposition} Decompositie van de gemiddelde variantie
:label: thm-portfolio-choice-clmx

Laat $w_i \geq 0$ met $\sum_i w_i = 1$ en $R_m = \sum_i w_i R_i$. Dan geldt voor elke verdeling van de rendementen

```{math}
:label: eq-portfolio-choice-clmx
\sum_i w_i \Var(R_i) = \Var(R_m) + \sum_i w_i \Var(R_i - R_m) .
```
:::

:::{prf:proof}
$\Var(R_i) = \Var(R_m) + \Var(R_i - R_m) + 2\Cov(R_m, R_i - R_m)$. Weeg met $w_i$ en tel op. De kruisterm wordt $2\Cov\!\big(R_m, \sum_i w_i R_i - R_m\big) = 2\Cov(R_m, 0) = 0$. $\square$
:::

De gemiddelde variantie van aandelen is dus de marktvariantie plus de gemiddelde variantie
van hun afwijkingen van de markt. Alleen die tweede term kan idiosyncratisch zijn.
{cite:t}`CampbellLettauMalkielXu2001` gebruikten deze decompositie en vonden dat de
bedrijfsspecifieke component tussen 1962 en 1997 meer dan verdubbelde, en veel sterker
steeg dan de markt- en de industriecomponent. Voor individuele aandelen domineert de
tweede term, want Goyal en Santa-Clara schatten in een gestileerde kalibratie dat
idiosyncratisch risico bijna 85% van de gemiddelde aandeelvariantie is.

Voor de replicatie is een gevolg van belang. Vervangen we aandelen door portefeuilles van
elk $n$ aandelen met idiosyncratische variantie $s^2$, dan bevat de afwijking $R_p - R_m$
nog maar $s^2/n$ aan idiosyncratische variantie, zodat een replicatie met portefeuilles
vooral marktvariantie meet. Over het oorspronkelijke resultaat vond de latere literatuur
drie dingen:

- {cite:t}`BaliCakiciYanZhang2005` lieten zien dat het vooral uit kleine Nasdaq-aandelen
  kwam en verdween als de steekproef tot eind 2001 liep, en {cite:t}`WeiZhang2005` dat het
  op de jaren negentig rustte;
- {cite:t}`AngHodrickXingZhang2006` vonden in de cross-sectie het omgekeerde van een
  premie, want aandelen met hoge idiosyncratische volatiliteit renderen zeer slecht, met
  een verschil in FF3-alpha van −1,31% per maand tussen het hoogste en het laagste kwintiel;
- {cite:t}`HerskovicKellyLustigVanNieuwerburgh2016` vonden een sterke gemeenschappelijke
  factor in idiosyncratische volatiliteit die met het inkomensrisico van huishoudens
  samenhangt, en aandelen met de laagste bèta op die factor verdienen 5,4% per jaar meer
  dan die met de hoogste.

```{warning}
De gemiddelde variantie is zeer persistent, en de schokken erin zijn negatief gecorreleerd met het marktrendement. Dat zijn de voorwaarden voor de Stambaugh-bias uit [](#04-20-voorspelbaarheid). Overlappende horizonnen tellen bovendien dezelfde maand meermaals en geven te kleine standaardfouten, en oefening 4 meet beide effecten.
```

```{admonition} Samengevat
:class: tip

- Een affiene conditionele regel is een vaste mix van managed portfolios, en bij eindig veel toestanden geeft [](#eq-portfolio-choice-bsc-theta) de conditioneel optimale portefeuille.
- De parametrische regel [](#eq-portfolio-choice-bsv) is een keuze tussen de markt en $K$ kenmerkportefeuilles, en $\hat{\boldsymbol{\theta}}$ is een GMM-schatter met standaardfouten uit [](#eq-portfolio-choice-avar).
- De ruis in $\hat{\boldsymbol{\theta}}$ groeit met $K/T$ in plaats van $N/T$, en een hogere $\gamma$ trekt de regel naar de markt omdat de speculatieve term in [](#eq-portfolio-choice-mv) krimpt.
- De gemiddelde variantie is de marktvariantie plus de variantie van de afwijkingen ([](#eq-portfolio-choice-clmx)), en bij portefeuilles in plaats van aandelen krimpt die tweede term.
```

## Simulatie: drie parameters tegen vijfhonderd gemiddelden

Hoe lang moet de steekproef zijn voordat drie kleine premies de parametrische regel van
1/N laten winnen? En hoe slecht doet Markowitz het met 500 geschatte gemiddelden? We
simuleren een wereld met 500 aandelen en drie kenmerken, size, value en momentum, die per
aandeel een AR(1) volgen en in de cross-sectie standaardnormaal zijn. Het overrendement is

$$
R^{e}_{i,t+1} = \beta_i f_{t+1} + \boldsymbol{\lambda}'\mathbf{x}_{i,t} + \varepsilon_{i,t+1} .
$$

| parameter | waarde |
|---|---|
| aantal aandelen $N$ | 500 |
| persistentie van size, value en momentum | 0,99; 0,97; 0,90 per maand |
| premie $\boldsymbol{\lambda}$ per standaarddeviatie kenmerk | −0,03%; 0,03%; 0,03% per maand |
| marktfactor $f$ | gemiddeld 0,5%, volatiliteit 4,5% per maand |
| bèta's $\beta_i$ | normaal, gemiddelde 1, standaarddeviatie 0,3 |
| idiosyncratische ruis $\varepsilon$ | 12% per maand |
| beleggingsperiode na de schatting | 240 maanden |
| relatieve risicoaversie $\gamma$ | 5, zoals in het toy-voorbeeld |

De premies zijn klein, want één standaarddeviatie in een kenmerk is 0,36% per jaar waard
tegen 42% idiosyncratische volatiliteit per jaar. Een belegger schat op $T$ maanden en
belegt daarna met 1/N, dat in deze wereld de rol van de markt speelt, met de parametrische
regel of met mean-variance op de 500 steekproefgemiddelden.

Omdat de steekproefcovariantie bij $T < N$ niet inverteerbaar is, gebruikt Markowitz een
geschat éénfactormodel, $\boldsymbol{\Sigma} = v_f\mathbf{b}\mathbf{b}' + \mathrm{diag}(\mathbf{s}^2)$,
met de factorvariantie $v_f$, de bèta's $\mathbf{b}$ en de restvarianties $\mathbf{s}^2$.
De inverse van zo'n matrix staat met de Woodbury-formule in gesloten vorm op papier,
zodat de cel geen $N\times N$-matrix hoeft te inverteren. De cel zet het model op en
simuleert 80 werelden voor vensters van 120 en 240 maanden.

```{code-cell} ipython3
N_STOCKS, K_CHAR, RF_M, T_TEST, GAMMA = 500, 3, 0.003, 240, 5.0
LAMBDA = np.array([-0.0003, 0.0003, 0.0003])
RHO_X = np.array([0.99, 0.97, 0.90])
SIG_EPS, MU_F, SIG_F = 0.12, 0.005, 0.045

def simulate_stocks(n_months):
    """Persistent characteristics X[t] and excess returns R[t] earned over month t+1."""
    x0 = rng.standard_normal((N_STOCKS, K_CHAR))
    noise = rng.standard_normal((n_months, N_STOCKS, K_CHAR))
    X = np.empty_like(noise)
    for k in range(K_CHAR):  # AR(1): X[t] = rho X[t-1] + sqrt(1 - rho^2) noise[t], started from x0
        X[:, :, k] = signal.lfilter([np.sqrt(1 - RHO_X[k] ** 2)], [1, -RHO_X[k]], noise[:, :, k],
                                    axis=0, zi=RHO_X[k] * x0[None, :, k])[0]
    beta = 1 + 0.3 * rng.standard_normal(N_STOCKS)
    f = MU_F + SIG_F * rng.standard_normal(n_months)
    R = np.outer(f, beta) + X @ LAMBDA + SIG_EPS * rng.standard_normal((n_months, N_STOCKS))
    return X, R

def fit_theta(rbar, rx, gamma=GAMMA):
    """Maximise average CRRA utility of rbar + rx @ theta (gross returns) over theta."""
    def neg_utility(theta):
        Rp = rbar + rx @ theta
        return 1e6 if np.any(Rp <= 0) else -np.mean(Rp ** (1 - gamma)) / (1 - gamma)

    def gradient(theta):
        Rp = np.maximum(rbar + rx @ theta, 1e-6)
        return -(Rp ** (-gamma)) @ rx / len(Rp)

    return optimize.minimize(neg_utility, np.zeros(rx.shape[1]), jac=gradient, method="BFGS").x

def sharpe_ce(excess, rf=RF_M, gamma=GAMMA):
    """Annualised Sharpe ratio and CRRA certainty-equivalent excess return."""
    Rp = np.maximum(1 + rf + excess, 1e-4)
    ce = np.mean(Rp ** (1 - gamma)) ** (1 / (1 - gamma)) - 1 - rf
    return np.sqrt(12) * excess.mean() / excess.std(), 12 * ce

def one_world(T):
    """Estimate on T months, evaluate the next T_TEST months."""
    X, R = simulate_stocks(T + T_TEST)
    Xs = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
    rx = np.einsum("tnk,tn->tk", Xs, R) / N_STOCKS
    bench = R.mean(axis=1)
    theta = fit_theta(1 + RF_M + bench[:T], rx[:T])

    train = R[:T]
    m_hat, fm = train.mean(axis=0), bench[:T] - bench[:T].mean()
    b = (train - m_hat).T @ fm / (fm @ fm)
    s2, vf = (train - m_hat - np.outer(fm, b)).var(axis=0), fm.var()
    Dm, Db = m_hat / s2, b / s2                       # Woodbury inverse of vf*bb' + diag(s2)
    w_mv = (Dm - Db * (b @ Dm) * vf / (1 + vf * (b @ Db))) / GAMMA
    return [*sharpe_ce(bench[T:]), *sharpe_ce(bench[T:] + rx[T:] @ theta),
            *sharpe_ce(R[T:] @ w_mv), *theta]

COLUMNS = ["SR 1/N", "CE 1/N", "SR BSV", "CE BSV", "SR MV", "CE MV", "theta size", "theta waarde", "theta mom"]
N_WORLDS = 80
sim_rows = [[T, *one_world(T)] for T in (120, 240) for _ in range(N_WORLDS)]
```

De tweede cel voegt vensters van 360 en 600 maanden toe. Per venster staan in de tabel de
mediaan van Sharpe-ratio (SR) en certainty equivalent (CE), de kans dat de regel 1/N
verslaat en de spreiding van $\hat\theta$ voor size.

```{code-cell} ipython3
sim_rows += [[T, *one_world(T)] for T in (360, 600) for _ in range(N_WORLDS)]
sim = pd.DataFrame(sim_rows, columns=["T", *COLUMNS])
summary = sim.groupby("T").median()[COLUMNS[:6]]
summary["P(SR BSV > SR 1/N)"] = sim.assign(w=sim["SR BSV"] > sim["SR 1/N"]).groupby("T")["w"].mean()
summary["SD theta size"] = sim.groupby("T")["theta size"].std()
summary.round(3)
```

Mean-variance op 500 gemiddelden is kansloos. De mediane Sharpe-ratio blijft tussen 0,09
en 0,15, en het certainty equivalent zakt ver onder nul, omdat de CRRA-belegger in vrijwel
elke wereld ergens zijn vermogen verliest. Dat is het probleem van [](#01-04-markowitz) op
grote schaal, met $N/T$ tussen 0,8 en 4.

De figuur toont links hoe ver de parametrische regel van 1/N wegloopt, en rechts hoe de
verdeling van $\hat\theta$ voor size smaller wordt als het venster groeit.

```{code-cell} ipython3
:label: cel-portfolio-choice-sim-a
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
for col, label, colour in [("SR 1/N", "1/N", hap.plotting.COLORS[3]),
                           ("SR BSV", "parametrisch (K = 3)", hap.plotting.COLORS[0]),
                           ("SR MV", "mean-variance (N = 500)", hap.plotting.COLORS[1])]:
    q = sim.groupby("T")[col].quantile([0.25, 0.5, 0.75]).unstack()
    axes[0].plot(q.index, q[0.5], marker="o", color=colour, label=label)
    axes[0].fill_between(q.index, q[0.25], q[0.75], color=colour, alpha=0.15)
axes[0].set_xlabel("Schattingsvenster T (maanden)")
axes[0].set_ylabel("Sharpe-ratio buiten de steekproef (per jaar)")
axes[0].set_title("(a) Sharpe-ratio over 240 maanden erna")
axes[0].legend()
for T, colour in zip((120, 600), (hap.plotting.COLORS[5], hap.plotting.COLORS[0])):
    axes[1].hist(sim.loc[sim["T"] == T, "theta size"], bins=20, alpha=0.55, color=colour, label=f"T = {T}")
axes[1].set_xlabel("Geschatte theta voor size")
axes[1].set_ylabel("Aantal gesimuleerde werelden")
axes[1].set_title("(b) Verdeling van de schatter")
axes[1].legend()
fig.tight_layout()
plt.show()
```

:::{figure} #cel-portfolio-choice-sim-a
:label: fig-portfolio-choice-sim-a
:width: 100%

Links de mediaan en de interkwartielafstand van de Sharpe-ratio buiten de steekproef, over 80 werelden per venster. De parametrische regel loopt pas van 1/N weg als het venster lang genoeg is om drie kleine premies te zien. Rechts de schatter van $\theta$ voor size, waarvan de verdeling bij tien jaar data ruim aan beide kanten van nul ligt en bij vijftig jaar veel smaller is.
:::

De parametrische regel wint niet vanzelf. Bij tien jaar data verslaat hij 1/N in iets meer
dan de helft van de werelden, en zijn certainty equivalent is lager. De standaarddeviatie
van $\hat\theta_{\text{size}}$ is dan nog 3,7, en bij vijftig jaar is die gezakt tot 1,7
en verslaat de regel 1/N in beide maten. De regel verslaat de markt van deze wereld dus,
zoals de intuïtie verwachtte, maar pas bij een steekproef die langer is dan de meeste
beleggers hebben.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Michael Brandt, Pedro Santa-Clara en Rossen Valkanov, *Parametric Portfolio Policies: Exploiting Characteristics in the Cross-Section of Equity Returns*, Review of Financial Studies 2009 {cite}`BrandtSantaClaraValkanov2009`.

**Wat.** Tabel 1 en tabel 3 van het artikel. Dat zijn de lineaire en de long-only-regel met size, boek-marktwaarde en momentum en $\gamma = 5$, geschat vanaf januari 1964 met statistieken over 1974–2002.

**Data hier.** De 100 size/BM-portefeuilles van French als activa, met log marktwaarde, log B/M en het eigen rendement over de voorgaande elf maanden als kenmerken, en ter controle de 25 size-momentumportefeuilles. De benchmark is de waardegewogen portefeuille van dezelfde activa, en buiten de steekproef herschatten we $\theta$ elk jaar op alle data vanaf 1964.

**Verschil met het origineel.** Portefeuilles hebben veel minder spreiding in kenmerken en veel minder idiosyncratisch risico dan aandelen, en hun momentum is het rendement van de portefeuille zelf. Daardoor is de omzet niet vergelijkbaar met die bij aandelen.

**Verwachte afwijking.** De tekens moeten die van het artikel zijn, $\theta_{\text{size}} < 0$, $\theta_{\text{B/M}} > 0$ en $\theta_{\text{mom}} > 0$, en in de steekproef moet de regel de benchmark duidelijk verslaan. Na 2002 verwachten we een kleiner voordeel of geen, omdat de size- en valuepremie zwak waren en de standaardfout van een Sharpe-ratio over 23 jaar ongeveer $\sqrt{1/23} \approx 0{,}21$ is.
```

De eerste cel laadt beide sets portefeuilles en zet ze om in een paneel met
gestandaardiseerde kenmerken, marktgewichten en het rendement van de maand erna.

```{code-cell} ipython3
rf_monthly = hap_data.market_monthly()["RF"]

def load_size_bm():
    """100 size/BM portfolios: returns, total market cap and three characteristics."""
    R = hap_data.french("100_Portfolios_10x10")
    firms = hap_data.french("100_Portfolios_10x10", table=4)
    avg_cap = hap_data.french("100_Portfolios_10x10", table=5)
    bm = hap_data.french("100_Portfolios_10x10", table=6, percent=False)
    chars = {"log ME": np.log(avg_cap.where(avg_cap > 0)),
             "log B/M": np.log(bm.where(bm > 0)),
             "momentum": np.log1p(R).shift(1).rolling(11).sum()}
    return R, firms * avg_cap, chars

def load_size_momentum():
    """25 size/momentum portfolios: returns, total market cap and two characteristics."""
    R = hap_data.french("25_Portfolios_ME_Prior_12_2")
    firms = hap_data.french("25_Portfolios_ME_Prior_12_2", table=4)
    avg_cap = hap_data.french("25_Portfolios_ME_Prior_12_2", table=5)
    prior = hap_data.french("25_Portfolios_ME_Prior_12_2", table=7)
    return R, firms * avg_cap, {"log ME": np.log(avg_cap.where(avg_cap > 0)), "momentum": prior}

def characteristic_panel(R, size, chars, min_assets=10):
    """Month-t characteristics and weights with month-(t+1) returns, standardised per month."""
    nxt = R.shift(-1)
    valid = nxt.notna() & (size > 0)
    for c in chars.values():
        valid &= c.notna()
    n_t = valid.sum(axis=1).to_numpy()
    keep = (n_t >= min_assets) & rf_monthly.reindex(R.index).shift(-1).notna().to_numpy()
    mask = valid.to_numpy()[keep]
    n = n_t[keep].astype(float)

    Z = np.stack([c.to_numpy()[keep] for c in chars.values()], axis=-1)
    Z = np.where(mask[..., None], Z, 0.0)
    mean = Z.sum(axis=1) / n[:, None]
    sd = np.sqrt((np.where(mask[..., None], Z - mean[:, None, :], 0.0) ** 2).sum(axis=1) / (n[:, None] - 1))
    Xs = np.where(mask[..., None], (Z - mean[:, None, :]) / sd[:, None, :], 0.0)

    cap = np.where(mask, size.to_numpy()[keep], 0.0)
    r = np.where(mask, nxt.to_numpy()[keep], 0.0)
    return {"date": pd.DatetimeIndex(R.index.to_series().shift(-1).to_numpy()[keep]),
            "X": Xs, "wbar": cap / cap.sum(axis=1, keepdims=True), "r": r, "n": n,
            "rf": rf_monthly.reindex(R.index).shift(-1).to_numpy()[keep], "names": list(chars)}

def policy_returns(panel):
    """Gross benchmark return and the K characteristic-portfolio returns (eq. rp)."""
    rbar = 1 + (panel["wbar"] * panel["r"]).sum(axis=1)
    rx = np.einsum("tnk,tn->tk", panel["X"], panel["r"]) / panel["n"][:, None]
    return rbar, rx

size_bm = characteristic_panel(*load_size_bm())
size_mom = characteristic_panel(*load_size_momentum())
{name: (p["date"][0].strftime("%Y-%m"), p["date"][-1].strftime("%Y-%m"), round(p["n"].mean(), 1))
 for name, p in [("100 size/BM", size_bm), ("25 size/momentum", size_mom)]}
```

De functie `characteristic_panel` standaardiseert elk kenmerk per maand over de
portefeuilles die in die maand bestaan, zoals [](#eq-portfolio-choice-bsv) vraagt. Omdat
niet elke size/BM-combinatie elke maand aandelen bevat, zijn gemiddeld 98 van de 100
size/BM-portefeuilles per maand bruikbaar, en de 25 size-momentumportefeuilles zijn altijd
compleet. Daarna
schatten we $\theta$ op 1964–2002, met standaardfouten uit [](#eq-portfolio-choice-avar).

```{code-cell} ipython3
def theta_standard_errors(theta, rbar, rx, gamma=GAMMA):
    """Sandwich standard errors G^-1 V G^-1 / T from the proposition."""
    Rp = rbar + rx @ theta
    h = (Rp ** (-gamma))[:, None] * rx
    G = np.einsum("t,tk,tl->kl", -gamma * Rp ** (-gamma - 1), rx, rx) / len(Rp)
    V = h.T @ h / len(Rp)
    G_inv = np.linalg.inv(G)
    return np.sqrt(np.diag(G_inv @ V @ G_inv.T / len(Rp)))

def month_end(month):
    """'2002-12' -> Timestamp('2002-12-31'), so that end months are inclusive."""
    return pd.Timestamp(month) + pd.offsets.MonthEnd(0)

def subset(panel, start, end):
    idx = (panel["date"] >= pd.Timestamp(start)) & (panel["date"] <= month_end(end))
    return {k: (v[idx] if isinstance(v, (np.ndarray, pd.DatetimeIndex)) else v) for k, v in panel.items()}

IN_START, IN_END = "1964-01", "2002-12"
theta_rows = {}
for name, panel in [("100 size/BM", size_bm), ("25 size/momentum", size_mom)]:
    ins = subset(panel, IN_START, IN_END)
    rbar, rx = policy_returns(ins)
    theta = fit_theta(rbar, rx)
    se = theta_standard_errors(theta, rbar, rx)
    for k, char in enumerate(panel["names"]):
        theta_rows[(name, char)] = {"theta": theta[k], "standaardfout": se[k], "t": theta[k] / se[k]}
theta_table = pd.DataFrame(theta_rows).T
theta_table.round(3)
```

De tekens zijn die van het artikel. Size ligt dicht bij de gepubliceerde waarde, momentum
ongeveer een halve standaardfout erboven en B/M 1,6 standaardfout erboven. Size is na 39
jaar data met $t = -1{,}8$ niet op 5% significant, wat de simulatie al liet verwachten, en
op de size-momentumportefeuilles verdwijnt size terwijl momentum blijft.

Vervolgens evalueren we de regel, de long-only-versie en de benchmark over 1974–2002, de
periode waarover het artikel rapporteert.

```{code-cell} ipython3
def weights(panel, theta):
    return panel["wbar"] + np.einsum("tnk,k->tn", panel["X"], theta) / panel["n"][:, None]

def long_only(W):
    W = np.maximum(W, 0.0)
    return W / W.sum(axis=1, keepdims=True)

def fit_theta_long_only(panel, start_theta, gamma=GAMMA):
    """Re-estimate theta with truncated weights (non-smooth, so Nelder-Mead)."""
    def neg_utility(theta):
        Rp = 1 + (long_only(weights(panel, theta)) * panel["r"]).sum(axis=1)
        return -np.mean(Rp ** (1 - gamma)) / (1 - gamma)
    return optimize.minimize(neg_utility, start_theta, method="Nelder-Mead",
                             options={"xatol": 1e-3, "fatol": 1e-8, "maxiter": 2000}).x

def turnover(W, r):
    """Average sum |w_{t+1} - drifted w_t| per month."""
    grown = W[:-1] * (1 + r[:-1])
    drift = grown / grown.sum(axis=1, keepdims=True)
    return np.abs(W[1:] - drift).sum(axis=1).mean()

def evaluate(gross, rf, gamma=GAMMA):
    excess = gross - 1 - rf
    ce = np.mean(gross ** (1 - gamma)) ** (1 / (1 - gamma)) - 1
    return {"gem. overrendement (% p.j.)": 1200 * excess.mean(), "vol (% p.j.)": 100 * np.sqrt(12) * excess.std(ddof=1),
            "Sharpe (p.j.)": np.sqrt(12) * excess.mean() / excess.std(ddof=1),
            "CE (% p.j.)": 1200 * ce, "SE Sharpe": np.sqrt(12 / len(gross))}

ins = subset(size_bm, IN_START, IN_END)
rbar_in, rx_in = policy_returns(ins)
theta_in = theta_table.loc["100 size/BM", "theta"].to_numpy()
theta_lo = fit_theta_long_only(ins, theta_in)

REPORT_START = "1974-01"                      # BSV report their statistics for 1974-2002
rep = subset(size_bm, REPORT_START, IN_END)
rbar_rep, rx_rep = policy_returns(rep)
W_rep, W_lo_rep = weights(rep, theta_in), long_only(weights(rep, theta_lo))

def weight_stats(W, r):
    return {"som negatieve w": np.minimum(W, 0).sum(axis=1).mean(), "fractie w < 0": (W < 0).mean(),
            "omzet (p.j.)": 12 * turnover(W, r)}

in_sample = pd.DataFrame({
    "VW-benchmark": {**evaluate(rbar_rep, rep["rf"]), **weight_stats(rep["wbar"], rep["r"])},
    "parametrisch": {**evaluate(rbar_rep + rx_rep @ theta_in, rep["rf"]), **weight_stats(W_rep, rep["r"])},
    "parametrisch, long-only": {**evaluate(1 + (W_lo_rep * rep["r"]).sum(axis=1), rep["rf"]),
                                **weight_stats(W_lo_rep, rep["r"])},
}).T
print("theta long-only (1964-2002):", theta_lo.round(3))
in_sample.round(3)
```

De regel haalt in de steekproef bijna drie keer de Sharpe-ratio van de benchmark. De
positie is wel extreem, met gemiddeld 180% van het vermogen short en een omzet van negen
keer het vermogen per jaar. Die omzet komt uit de momentumterm, omdat het momentum van een
portefeuille elke maand verschuift terwijl size en B/M nauwelijks bewegen.

De long-only-versie haalt het grootste deel van de omzet weg. De schatting van die versie
uit de `print` is $(2{,}38;\ 19{,}24;\ 5{,}31)$ en lijkt niet op die van de
lineaire regel, want size wisselt van teken en B/M is bijna vier keer zo groot. Toch liggen
Sharpe-ratio en certainty equivalent dicht bij het artikel, omdat afkappen en normaliseren
de schaal van $\theta$ niet meer vastleggen.

Buiten de steekproef herschatten we $\theta$ elk januari op alle data vanaf 1964 en
beleggen we het jaar erna met die schatting. De cel toont de schattingen in vijf jaren.

```{code-cell} ipython3
def expanding_oos(panel, start="1974-01", long_only_too=False):
    """Re-estimate theta every January on all data from IN_START until then; return OOS gross returns."""
    rbar, rx = policy_returns(panel)
    out = subset(panel, start, "2100-12")
    years = sorted(set(out["date"].year))
    gross, gross_lo, path = [], [], {}
    for year in years:
        past = (panel["date"] >= pd.Timestamp(IN_START)) & (panel["date"] < pd.Timestamp(f"{year}-01-01"))
        now = panel["date"].year == year
        theta = fit_theta(rbar[past], rx[past])
        path[year] = theta
        gross.append(rbar[now] + rx[now] @ theta)
        if long_only_too:
            sub_past, sub_now = subset(panel, IN_START, f"{year - 1}-12"), subset(panel, f"{year}-01", f"{year}-12")
            th_lo = fit_theta_long_only(sub_past, theta)
            gross_lo.append(1 + (long_only(weights(sub_now, th_lo)) * sub_now["r"]).sum(axis=1))
    result = {"date": out["date"], "policy": np.concatenate(gross), "bench": rbar[panel["date"] >= pd.Timestamp(start)],
              "rf": out["rf"], "theta": pd.DataFrame(path, index=panel["names"]).T}
    if long_only_too:
        result["long_only"] = np.concatenate(gross_lo)
    return result

oos_bm = expanding_oos(size_bm, long_only_too=True)
oos_bm["theta"].iloc[[0, 8, 16, 29, -1]].round(2)
```

Tot 2003 houden de drie coëfficiënten hun teken en blijft size ongeveer gelijk, terwijl
B/M eerst stijgt en momentum wat zakt. Daarna kruipt size naar nul en zakt B/M. De
volgende cel vat de prestaties buiten de
steekproef samen, apart voor 1974–2002 en voor de jaren na het artikel.

```{code-cell} ipython3
oos_mom = expanding_oos(size_mom)
oos_parts = {}
for label, (s, e) in {"1974-2002": ("1974-01", "2002-12"), "2003-eind": ("2003-01", "2100-12")}.items():
    for name, res, series in [("100 size/BM", oos_bm, ["bench", "policy", "long_only"]),
                              ("25 size/momentum", oos_mom, ["bench", "policy"])]:
        idx = (res["date"] >= pd.Timestamp(s)) & (res["date"] <= month_end(e))
        for key in series:
            oos_parts[(label, name, {"bench": "VW-benchmark", "policy": "parametrisch",
                                     "long_only": "parametrisch, long-only"}[key])] = evaluate(res[key][idx], res["rf"][idx])
print(f"buiten de steekproef: {oos_bm['date'][0]:%Y-%m} t/m {oos_bm['date'][-1]:%Y-%m}, {len(oos_bm['date'])} maanden")
pd.DataFrame(oos_parts).T.round(3)
```

Over 1974–2002 verslaat de regel ook buiten de steekproef de benchmark ruim, op beide sets
portefeuilles, maar na 2002 blijft hij overal achter. Links in de figuur is de knik bij
2003 in de lijn van de regel te zien, rechts de lijn van size, die daarna naar nul kruipt.

```{code-cell} ipython3
:label: cel-portfolio-choice-bsv
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
wealth = pd.DataFrame({key: np.log(oos_bm[col]).cumsum() for key, col in
                       [("VW-benchmark", "bench"), ("parametrisch", "policy"), ("parametrisch, long-only", "long_only")]},
                      index=oos_bm["date"])
wealth.plot(ax=axes[0], color=[hap.plotting.COLORS[3], hap.plotting.COLORS[0], hap.plotting.COLORS[2]])
axes[0].axvline(pd.Timestamp("2003-01-01"), color="black", lw=0.8, ls="--")
axes[0].set_xlabel("Jaar")
axes[0].set_ylabel("Cumulatief log brutorendement")
axes[0].set_title("(a) Buiten de steekproef vanaf 1974, 100 size/BM")
oos_bm["theta"].plot(ax=axes[1], marker=".")
axes[1].axhline(0, color="black", lw=0.8)
axes[1].set_xlabel("Jaar van belegging (theta geschat op alle eerdere data)")
axes[1].set_ylabel("Geschatte theta")
axes[1].set_title("(b) Jaarlijks herschatte theta, 100 size/BM")
fig.tight_layout()
plt.show()
```

:::{figure} #cel-portfolio-choice-bsv
:label: fig-portfolio-choice-bsv
:width: 100%

Links het cumulatieve log brutorendement vanaf 1974 van de benchmark, de parametrische regel en de long-only-versie. Tot 2003 (stippellijn) loopt de regel duidelijk weg, daarna niet meer. Rechts de jaarlijks herschatte $\theta$. In de vijf jaren die de cel erboven toont, ligt size tot 2003 tussen −1,0 en −1,4 en in 2026 op −0,30. B/M stijgt van 3,5 tot 5,2 en zakt daarna tot 2,7, terwijl momentum tussen 2,2 en 3,2 blijft.
:::

De tabel zet over 1974–2002 de belangrijkste getallen uit tabel 1 en 3 van het artikel
naast die uit de cellen hierboven.

| grootheid | origineel | hier |
|---|---|---|
| $\hat\theta_{\text{size}}$ (standaardfout) | −1,451 (0,548) | −1,37 (0,76) |
| $\hat\theta_{\text{B/M}}$ (standaardfout) | 3,606 (0,921) | 5,00 (0,86) |
| $\hat\theta_{\text{mom}}$ (standaardfout) | 1,772 (0,743) | 2,18 (0,75) |
| Sharpe-ratio regel / benchmark, in de steekproef | 1,048 / 0,438 | 1,11 / 0,39 |
| certainty equivalent regel / benchmark (% per jaar) | 17,5 / 6,4 | 19,0 / 5,7 |
| gemiddelde som van negatieve gewichten | −128% | −180% |
| fractie negatieve gewichten | 47% | 39% |
| omzet per jaar | 0,99 | 9,0 (long-only 1,37) |
| long-only: Sharpe-ratio / certainty equivalent (%) | 0,690 / 10,3 | 0,68 / 10,0 |
| buiten de steekproef: Sharpe-ratio / certainty equivalent (%) | 0,941 / 11,8 | 1,02 / 16,3 |
| 2003–2026: Sharpe-ratio regel / benchmark | – | 0,62 / 0,72 |
| 2003–2026: certainty equivalent regel / benchmark (%) | – | 0,9 / 6,6 |
| 2003–2026: overrendement / volatiliteit regel (%) | – | 14 / 23 |
| 2003–2026: long-only, Sharpe-ratio / CE (%) | – | 0,64 / 4,3 |
| 2003–2026: 25 size/momentum, Sharpe-ratio regel / benchmark | – | 0,65 / 0,74 |

Gedeeltelijk geslaagd. De tekens en de orde van grootte van $\hat\theta$ kloppen, en ook
verslaat de regel de benchmark in en buiten de steekproef over
1974–2002. De posities en vooral de omzet wijken af, omdat portefeuilles andere kenmerken
hebben dan aandelen.

Na 2002, buiten elke steekproef die het artikel kon zien, verslaat de benchmark juist de
regel, en dat geldt ook voor de long-only-versie en de size-momentumregel. Het certainty
equivalent van de regel zakt het diepst, omdat hij veel meer volatiliteit neemt voor een
iets hoger
overrendement. Met een standaardfout van ongeveer 0,21 is geen van die verschillen van nul
te
onderscheiden, maar de richting is overal dezelfde, zodat het verwachte kleine voordeel een
klein nadeel werd.

### Gemiddelde variantie en het marktrendement

```{admonition} Replicatie
:class: seealso

**Bron.** Amit Goyal en Pedro Santa-Clara, *Idiosyncratic Risk Matters!*, Journal of Finance 2003 {cite}`GoyalSantaClara2003`.

**Wat.** Tabel II: regressies van het maandelijkse waardegewogen overrendement van de markt op de variantie van de vorige maand, augustus 1963 tot december 1999, met Newey-West-$t$-waarden.

**Data hier.** Dagrendementen van de 49 industrieportefeuilles van French voor de gemiddelde variantie en van de marktportefeuille voor de marktvariantie, over 1963–1999 en tot eind 2025.

**Verschil met het origineel.** Het artikel middelt over alle aandelen van CRSP, wij over 49 industrieën van tientallen tot honderden aandelen. Volgens [](#eq-portfolio-choice-clmx) is het meeste bedrijfsspecifieke risico dan al weggediversifieerd, zodat onze $V_t$ vooral industrie- en marktvariantie meet.

**Verwachte afwijking.** Omdat onze $V_t$ weinig bedrijfsspecifiek is, verwachten we een zwakke of geen voorspelling, ook in 1963–1999, en een afwijkingsterm die een duidelijk kleiner deel van $V_t$ is dan bij aandelen.
```

We berekenen de maandvariantie uit gekwadrateerde dagrendementen en schatten de drie
regressies uit het artikel over drie perioden.

```{code-cell} ipython3
industries_daily = hap_data.french("49_Industry_Portfolios", "daily")
market_daily = hap_data.market_daily()["Mkt"]

def monthly_realised_variance(daily):
    """Sum of squared daily returns per calendar month (at least 15 trading days)."""
    month = daily.index.to_period("M")
    variance = (daily**2).groupby(month).sum(min_count=15)
    return variance.set_axis(variance.index.to_timestamp(how="end").normalize())

ind_var = monthly_realised_variance(industries_daily)
ew_index = industries_daily.mean(axis=1)
deviation = monthly_realised_variance(industries_daily.sub(ew_index, axis=0)).mean(axis=1)
gsc = pd.DataFrame({
    "V": ind_var.mean(axis=1),
    "markt": monthly_realised_variance(market_daily),
    "EW-index": monthly_realised_variance(ew_index),
    "afwijking": deviation,
})
gsc["R_e volgende maand"] = hap_data.market_monthly()["Mkt-RF"].shift(-1).reindex(gsc.index)
gsc = gsc.dropna()

periods = {"1963-08 t/m 1999-12": ("1963-08", "1999-12"), "1963-08 t/m 2025-12": ("1963-08", "2025-12"),
           "2000-01 t/m 2025-12": ("2000-01", "2025-12")}
rows = {}
for label, (s, e) in periods.items():
    d = gsc.loc[s:e]
    for spec in (["V"], ["markt"], ["V", "markt"]):
        fit = hap.stats.newey_west(d["R_e volgende maand"], d[spec])
        rows[(label, " + ".join(spec))] = {
            "b (V)": fit.params.get("V", np.nan), "t (V)": fit.tvalues.get("V", np.nan),
            "c (markt)": fit.params.get("markt", np.nan), "t (markt)": fit.tvalues.get("markt", np.nan),
            "R2 (%)": 100 * fit.rsquared, "maanden": int(fit.nobs)}
pd.DataFrame(rows).T.round(3)
```

In geen van de drie perioden is een helling significant, en over de hele steekproef en
over 2000–2025 blijven alle $t$-waarden in absolute waarde onder één. De
volgende cel meet hoeveel van $V_t$ uit de afwijkingsterm komt en hoe persistent $\log V_t$
is.

```{code-cell} ipython3
d = gsc.loc["1963-08":"2025-12"]
log_v = np.log(d["V"])
share = (d["afwijking"] / d["V"])
pd.Series({
    "gem. aandeel afwijkingsterm in V, 1963-1999": share.loc[:"1999-12"].mean(),
    "gem. aandeel afwijkingsterm in V, 2000-2025": share.loc["2000-01":].mean(),
    "AR(1) van log V": log_v.autocorr(),
    "SD innovatie log V": (log_v - log_v.autocorr() * log_v.shift(1)).std(),
    "corr(R_e,t , innovatie log V_t)": hap_data.market_monthly()["Mkt-RF"].reindex(d.index).corr(log_v.diff()),
}).round(3)
```

De afwijkingsterm is over 1963–1999 gemiddeld 59% van $V_t$, en $\log V_t$ heeft een
autocorrelatie van 0,74 met schokken die negatief met het marktrendement samenhangen. De
figuur laat zien hoe dicht de drie reeksen bij elkaar liggen.

```{code-cell} ipython3
:label: cel-portfolio-choice-gsc
:tags: [hide-input]

fig, ax = plt.subplots()
annual = lambda s: np.sqrt(12 * s.rolling(12).mean()) * 100
ax.plot(gsc.index, annual(gsc["V"]), label="gemiddelde variantie, 49 industrieën")
ax.plot(gsc.index, annual(gsc["markt"]), label="marktvariantie", color=hap.plotting.COLORS[1])
ax.plot(gsc.index, annual(gsc["afwijking"]), label="afwijkingsterm (industrie-specifiek)", color=hap.plotting.COLORS[2])
hap.plotting.timeline_axis(ax)
hap.plotting.recession_shading(ax)
ax.set_xlabel("Jaar")
ax.set_ylabel("Volatiliteit (% per jaar, 12-maands gemiddelde)")
ax.set_title("Gemiddelde, markt- en industrie-specifieke variantie")
ax.legend()
plt.show()
```

:::{figure} #cel-portfolio-choice-gsc
:label: fig-portfolio-choice-gsc
:width: 90%

Volatiliteit op jaarbasis, als twaalfmaands voortschrijdend gemiddelde van de maandvariantie uit dagrendementen, met NBER-recessies in grijs. De gemiddelde variantie van de 49 industrieën ligt steeds boven die van de markt, en de afwijkingsterm is het industriespecifieke deel uit [](#eq-portfolio-choice-clmx). De drie reeksen bewegen grotendeels samen, zodat het idiosyncratische deel bij industrieportefeuilles voor een groot deel een schaduw van het marktrisico is.
:::

De tabel zet de regressies over 1963–1999 naast die uit tabel II van het artikel, met de
helling en tussen haakjes de $t$-waarde. In de laatste regel komt het idiosyncratische
deel bij Goyal en Santa-Clara uit een kalibratie en bij ons uit de afwijkingsterm.

| regressie | origineel | hier |
|---|---|---|
| alleen $V_t$ | 0,336 (2,57) | −0,25 (−0,33) |
| alleen marktvariantie | −0,597 (−1,07) | −0,46 (−0,52) |
| samen, helling op $V_t$ | 0,478 (3,86) | 1,39 (0,52) |
| samen, helling op marktvariantie | −1,449 (−2,70) | −2,16 (−0,63) |
| idiosyncratisch deel van $V_t$ | bijna 85% | 59% |

Niet geslaagd, en dat hadden we vooraf ook verwacht. Met industrieportefeuilles is van het
resultaat niets over, al hebben de hellingen in de gezamenlijke regressie wel de tekens
uit het artikel. Dat bewijst weinig in beide richtingen, want het ging Goyal en
Santa-Clara om bedrijfsspecifieke variantie, en die hebben wij grotendeels weggemiddeld.
De replicatie laat wel zien dat de gemiddelde variantie van industrieën het
marktrendement niet voorspelt, en oefening 4 laat zien hoe gemakkelijk dezelfde data met
overlappende
horizonnen toch "significant" worden.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De parametrische regel is geen evenwichtstheorie maar een
beslisregel, en juist daarin slaagt hij waar Markowitz faalde. Hij zet een handvol
feiten om in gewichten zonder dat de schattingsfout van duizenden gemiddelden de
portefeuille overneemt. Op honderd portefeuilles gaf hij de tekens en de orde van grootte
van de coëfficiënten uit het artikel, en tot 2002 ook buiten de steekproef een ruime
voorsprong op de markt. Santa-Clara vindt de regel dichter bij wat kwantitatieve
vermogensbeheerders werkelijk doen dan enig model uit de literatuur {cite}`SantaClara2026`.

**Waar het breekt.** Een parametrische regel is zo goed als de premies die hij uitbuit, en
die zijn slecht gemeten en niet stabiel. Na 2002 blijft de regel op beide sets
portefeuilles achter bij de benchmark. Het tweede spoor brak harder, want het resultaat
van Goyal en Santa-Clara hield in latere
steekproeven geen stand, en op onze industriedata is er zelfs in hun eigen periode niets
van te zien.

**Risico of vergissing?** Beide feiten laten beide lezingen toe. In de Chicago-lezing
belonen size, value en momentum risico's die het CAPM mist, en is de krimp na 2002 pech of
een lagere prijs van risico. In de Yale-lezing meten de kenmerken vergissingen, en kochten
arbitrageurs de premie na publicatie weg. Bij idiosyncratische volatiliteit eisen
onvolledig gediversifieerde huishoudens een premie, of worden volatiele aandelen als loten
overgewaardeerd. Scheiden kan alleen door te meten of de rendementen samenhangen met het
marginale nut in slechte tijden, en dat lukt met portefeuilledata niet. Zo blijft open of
een belegger met zo'n regel risico met een premie draagt, of alleen denkt iets te weten
wat de prijs niet weet.

**Wat er daarna kwam.** In 2008 bleek dat de hefboom waarmee zulke strategieën worden
uitgevoerd, van intermediairs komt. Hun balans is zelf een factor met een risicopremie, en
dat is het onderwerp van [](#05-32-intermediaries).

## Oefeningen

:::{exercise}
:label: ex-portfolio-choice-1

**Een zwakkere voorspeller.** Neem het toy-voorbeeld (a), maar laat de hoge toestand een verwacht overrendement van 6% hebben in plaats van 10%. De lage toestand en de conditionele variantie blijven gelijk.

1. Bereken met de hand de conditionele posities $w_{\text{laag}}$ en $w_{\text{hoog}}$.
2. Bereken $\theta_0$ en $\theta_1$ zonder het statische probleem opnieuw op te lossen, en controleer het resultaat met de code.
:::

:::{solution} ex-portfolio-choice-1
:class: dropdown

**(1)** De lage toestand verandert niet, dus $w_{\text{laag}} = 0{,}09901$. In de hoge toestand is $s = 0{,}04 + 0{,}06^2 = 0{,}0436$ en $w_{\text{hoog}} = 0{,}06/(5 \cdot 0{,}0436) = 0{,}27523$.

**(2)** Omdat $x_t = \pm 1$, is $\theta_0$ het gemiddelde en $\theta_1$ het halve verschil van de twee posities, dus $\theta_0 = (0{,}27523 + 0{,}09901)/2 = 0{,}18712$ en $\theta_1 = (0{,}27523 - 0{,}09901)/2 = 0{,}08811$. De code lost het statische probleem wel op en vindt hetzelfde.

```{code-cell} ipython3
mu_weak = np.array([0.02, 0.06])
s_weak = 0.04 + mu_weak**2
w_weak = mu_weak / (gamma * s_weak)
theta_weak = np.linalg.solve((payoff.T * (prob * s_weak)) @ payoff, (prob * mu_weak) @ payoff) / gamma
pd.DataFrame({"met de hand": [0.09901, 0.27523, 0.18712, 0.08811], "code": [*w_weak, *theta_weak]},
             index=["w laag", "w hoog", "theta0", "theta1"]).round(5)
```

Van 0,15050 naar 0,08811 is de coëfficiënt $\theta_1$ op het managed activum ruim gehalveerd. Het gewicht op een voorspeller schaalt dus mee met hoeveel die voorspeller over het verwachte rendement zegt.
:::

:::{exercise}
:label: ex-portfolio-choice-2

**De mean-variance-benadering van de parametrische regel.** Laat $R_p = \bar R + \boldsymbol{\theta}'\mathbf{r}^x$ het brutorendement van de regel zijn.

1. Leid [](#eq-portfolio-choice-mv) af door $\E[R_p] - \tfrac{\gamma}{2}\Var(R_p)$ te maximaliseren.
2. Laat zien dat bij kwadratisch nut in het tweede moment, $\E[R_p - 1] - \tfrac{\gamma}{2}\E[(R_p-1)^2]$, de oplossing $\boldsymbol{\theta} = \E[\mathbf{r}^x\mathbf{r}^{x\prime}]^{-1}\big(\gamma^{-1}\boldsymbol{\mu}_x - \E[\mathbf{r}^x(\bar R - 1)]\big)$ is, en dat dit met $\bar R = 1$ precies [](#eq-portfolio-choice-bsc-theta) is.
3. Bereken $\boldsymbol{\theta}^{\mathrm{mv}}$ op de data van de 100 size/BM-portefeuilles over 1964–2002 en vergelijk met de CRRA-schatting. Waar komt het verschil vandaan?
:::

:::{solution} ex-portfolio-choice-2
:class: dropdown

**(1)** Er geldt $\E[R_p] = \E[\bar R] + \boldsymbol{\theta}'\boldsymbol{\mu}_x$ en $\Var(R_p) = \Var(\bar R) + 2\boldsymbol{\theta}'\Cov(\mathbf{r}^x, \bar R) + \boldsymbol{\theta}'\boldsymbol{\Sigma}_x\boldsymbol{\theta}$. De afgeleide naar $\boldsymbol{\theta}$ is $\boldsymbol{\mu}_x - \gamma\Cov(\mathbf{r}^x, \bar R) - \gamma\boldsymbol{\Sigma}_x\boldsymbol{\theta}$, en die nul stellen geeft [](#eq-portfolio-choice-mv).

**(2)** Nu is $\E[R_p - 1] = \E[\bar R - 1] + \boldsymbol{\theta}'\boldsymbol{\mu}_x$ en $\E[(R_p - 1)^2] = \E[(\bar R-1)^2] + 2\boldsymbol{\theta}'\E[\mathbf{r}^x(\bar R-1)] + \boldsymbol{\theta}'\E[\mathbf{r}^x\mathbf{r}^{x\prime}]\boldsymbol{\theta}$. De afgeleide naar $\boldsymbol{\theta}$ is $\boldsymbol{\mu}_x - \gamma\E[\mathbf{r}^x(\bar R-1)] - \gamma\E[\mathbf{r}^x\mathbf{r}^{x\prime}]\boldsymbol{\theta}$, en die nul stellen geeft de oplossing. Met $\bar R = 1$ is de benchmark de risicovrije rente, in overrendementen nul, en valt de middelste term weg.

**(3)** De cel berekent beide schattingen op dezelfde data.

```{code-cell} ipython3
Sigma_x = np.cov(rx_in, rowvar=False)
cov_bench = np.array([np.cov(rx_in[:, k], rbar_in)[0, 1] for k in range(rx_in.shape[1])])
theta_mv = np.linalg.solve(Sigma_x, rx_in.mean(axis=0) / GAMMA - cov_bench)
pd.DataFrame({"CRRA": theta_in, "mean-variance": theta_mv}, index=size_bm["names"]).round(3)
```

De mean-variance-benadering geeft $(-1{,}18;\ 4{,}64;\ 2{,}47)$ tegen $(-1{,}37;\ 5{,}00;\ 2{,}18)$ met CRRA-nut, dus dezelfde tekens en orde van grootte. Het verschil komt uit de hogere momenten die CRRA-nut wel ziet. De kenmerkportefeuilles zijn scheef en hebben dikke staarten, en een belegger met $\gamma = 5$ straft een linkerstaart zwaarder af dan de variantie doet. Momentum kent de forse crashes uit [](#04-19-momentum) en krijgt daarom bij CRRA een kleiner gewicht. In de kern is de parametrische regel dus een Markowitz-probleem in drie activa, met een correctie voor staartrisico.
:::

:::{exercise}
:label: ex-portfolio-choice-3

**Transactiekosten.** Neem de parametrische regel op de 100 size/BM-portefeuilles, buiten de steekproef. In de replicatie zette hij negen keer het vermogen per jaar om, en de vraag is wat dat kost.

1. Bereken voor elke maand de omzet $\sum_i |w_{i,t+1} - w^{\mathrm{drift}}_{i,t}|$ van de regel en van de benchmark.
2. Trek kosten van $c \in \{0;\ 0{,}25;\ 0{,}5;\ 1\}\%$ per eenheid omzet af en rapporteer Sharpe-ratio en certainty equivalent.
3. Bij welke $c$ is de regel buiten de steekproef, van 1974 tot nu, niet meer beter dan de benchmark? Wat zegt dat over een schatter die kosten negeert?
:::

:::{solution} ex-portfolio-choice-3
:class: dropdown

De cel berekent de omzet, trekt de kosten af en zoekt het kostenniveau waarbij de voorsprong in Sharpe-ratio verdwijnt.

```{code-cell} ipython3
def turnover_series(W, r):
    grown = W[:-1] * (1 + r[:-1])
    return np.r_[0.0, np.abs(W[1:] - grown / grown.sum(axis=1, keepdims=True)).sum(axis=1)]

def net_of_costs(panel, theta, cost):
    W = weights(panel, theta)
    gross = 1 + (W * panel["r"]).sum(axis=1)
    bench = 1 + (panel["wbar"] * panel["r"]).sum(axis=1)
    return (gross - cost * turnover_series(W, panel["r"]),
            bench - cost * turnover_series(panel["wbar"], panel["r"]))

oos_panel = subset(size_bm, "1974-01", "2100-12")
theta_oos_path = oos_bm["theta"].reindex(oos_panel["date"].year).to_numpy()
W_oos = oos_panel["wbar"] + np.einsum("tnk,tk->tn", oos_panel["X"], theta_oos_path) / oos_panel["n"][:, None]
turn_policy = turnover_series(W_oos, oos_panel["r"])
turn_bench = turnover_series(oos_panel["wbar"], oos_panel["r"])

def oos_sharpe_gap(c):
    """OOS Sharpe ratio of the policy minus that of the benchmark, both net of costs c."""
    net = 1 + (W_oos * oos_panel["r"]).sum(axis=1) - c * turn_policy
    bench = 1 + (oos_panel["wbar"] * oos_panel["r"]).sum(axis=1) - c * turn_bench
    return evaluate(net, oos_panel["rf"])["Sharpe (p.j.)"] - evaluate(bench, oos_panel["rf"])["Sharpe (p.j.)"]

cost_rows = {}
for c in (0.0, 0.0025, 0.005, 0.01):
    gross_in, bench_in = net_of_costs(ins, theta_in, c)
    net_oos = 1 + (W_oos * oos_panel["r"]).sum(axis=1) - c * turnover_series(W_oos, oos_panel["r"])
    cost_rows[f"c = {100 * c:.2f}%"] = {
        "Sharpe in-sample policy": evaluate(gross_in, ins["rf"])["Sharpe (p.j.)"],
        "Sharpe in-sample benchmark": evaluate(bench_in, ins["rf"])["Sharpe (p.j.)"],
        "Sharpe OOS policy": evaluate(net_oos, oos_panel["rf"])["Sharpe (p.j.)"],
        "Sharpe OOS benchmark": evaluate(net_oos, oos_panel["rf"])["Sharpe (p.j.)"] - oos_sharpe_gap(c),
        "CE OOS policy (% p.j.)": evaluate(net_oos, oos_panel["rf"])["CE (% p.j.)"]}
print(f"gem. omzet per maand: policy {turn_policy.mean():.3f}, benchmark {turn_bench.mean():.3f}")
print(f"break-evenkosten out-of-sample: {100 * optimize.brentq(oos_sharpe_gap, 0.0, 0.05):.2f}% per eenheid omzet")
pd.DataFrame(cost_rows).T.round(3)
```

De benchmark zet gemiddeld 0,048 van het vermogen per maand om en de regel 0,81, zodat vrijwel alle omzet van de kenmerkposities komt. In de steekproef (1964–2002) blijft de regel bij elke kostenpost ruim boven de benchmark, met bij 1% per eenheid omzet nog een Sharpe-ratio van 0,67 tegen 0,29. Buiten de steekproef is de voorsprong zonder kosten 0,84 tegen 0,53, maar hij verdwijnt bij 0,79% per eenheid omzet, en bij 1% is het certainty equivalent negatief. Een schatter die kosten negeert, kiest $\theta$ alsof omzet gratis is, en daarom nemen Brandt, Santa-Clara en Valkanov de kosten op in het doel zelf.
:::

:::{exercise}
:label: ex-portfolio-choice-4

**Overlap en persistentie.** Een variabele die niets voorspelt, kan met overlappende horizonnen toch "significant" lijken.

1. Simuleer 5000 steekproeven van 437 maanden, zo lang als die van Goyal en Santa-Clara. Het overrendement van de markt is i.i.d. met gemiddeld 0,6% en volatiliteit 4,5% per maand, en $\log V_{t+1} = 0{,}74\log V_t + 0{,}50\,\eta_{t+1}$ met $\Corr(\eta_{t+1}, R^{e}_{m,t+1}) = -0{,}31$, ongeveer zoals op de industriedata gemeten. Regresseer het cumulatieve rendement over $h \in \{1, 3, 6, 12\}$ maanden op $V_t$ en rapporteer hoe vaak de helling eenzijdig op 2,5% significant positief is, met OLS- en met Newey-West-standaardfouten ($h$ lags).
2. Herhaal de regressie op de echte data over 1963–1999 en vergelijk de verhouding tussen de OLS- en de Newey-West-$t$-waarde met de simulatie.
3. Wat moet een onderzoeker die in 2003 alleen de twaalfmaandsregressie met OLS-standaardfouten rapporteert, volgens de simulatie als "significant" beschouwen?
:::

:::{solution} ex-portfolio-choice-4
:class: dropdown

**(1)** De cel simuleert de wereld zonder voorspelbaarheid en telt de onterechte verwerpingen.

```{code-cell} ipython3
T_GSC, N_GSC = 437, 5000
PHI_V, SD_V, CORR_RV, MU_M, SD_M = 0.74, 0.50, -0.31, 0.006, 0.045
HORIZONS_GSC = (1, 3, 6, 12)

def simulate_gsc(n_samples, n_months, burn=100):
    """Unpredictable market returns and a persistent log average variance with leverage-type correlation."""
    total = burn + n_months + max(HORIZONS_GSC)
    eps = rng.standard_normal((n_samples, total))
    eta = CORR_RV * eps + np.sqrt(1 - CORR_RV**2) * rng.standard_normal((n_samples, total))
    log_v = signal.lfilter([SD_V], [1, -PHI_V], eta, axis=1)[:, burn:]
    return np.exp(log_v), (MU_M + SD_M * eps)[:, burn:]

def slope_tstats(y, x, lags):
    """Row-wise slope t-values of y on x: OLS and Newey-West with `lags` lags."""  # TODO: naar hap.stats
    xd = x - x.mean(axis=1, keepdims=True)
    sxx = (xd**2).sum(axis=1)
    beta = (xd * y).sum(axis=1) / sxx
    u = y - y.mean(axis=1, keepdims=True) - beta[:, None] * xd
    se_ols = np.sqrt((u**2).sum(axis=1) / (x.shape[1] - 2) / sxx)
    g = xd * u
    s = (g**2).sum(axis=1)
    for j in range(1, lags + 1):
        s += 2 * (1 - j / (lags + 1)) * (g[:, j:] * g[:, :-j]).sum(axis=1)
    return beta / se_ols, beta / (np.sqrt(s) / sxx)

V_sim, r_sim = simulate_gsc(N_GSC, T_GSC)
t_ols, t_nw = {}, {}
for h in HORIZONS_GSC:
    y = np.stack([r_sim[:, t + 1:t + 1 + h].sum(axis=1) for t in range(T_GSC)], axis=1)
    t_ols[h], t_nw[h] = slope_tstats(y, V_sim[:, :T_GSC], lags=h)

reject = pd.DataFrame(
    {"OLS": {h: np.mean(t_ols[h] > 1.96) for h in HORIZONS_GSC},
     "Newey-West (h lags)": {h: np.mean(t_nw[h] > 1.96) for h in HORIZONS_GSC}}
).rename_axis("horizon h (maanden)")
search = np.mean(np.max(np.stack(list(t_ols.values())), axis=0) > 1.96)
print(f"minstens één van de vier OLS-horizonnen 'significant' positief: {search:.1%}")
reject.round(3)
```

Bij één maand verwerpt de toets in 2,8% (OLS) en 3,6% (Newey-West) van de steekproeven, dicht bij de nominale 2,5%. Met overlappende twaalfmaandsrendementen vindt 18,8% met OLS een significant positieve helling, met Newey-West nog 6,7%. Wie de beste van vier horizonnen rapporteert, vindt in 25,8% van de werelden iets.

**(2)** De tweede cel doet dezelfde regressies op de echte data en zet de verhouding van de $t$-waarden naast de mediaan uit de simulatie.

```{code-cell} ipython3
d = gsc.loc["1963-08":"1999-12"]
r_next = hap_data.market_monthly()["Mkt-RF"]
overlap_rows = {}
for h in HORIZONS_GSC:
    cumulative = r_next.rolling(h).sum().shift(-h).reindex(d.index)
    frame = pd.concat([cumulative.rename("y"), d["V"]], axis=1).dropna()
    t_o, t_n = slope_tstats(frame["y"].to_numpy()[None, :], frame["V"].to_numpy()[None, :], lags=h)
    overlap_rows[h] = {"t OLS": float(t_o[0]), "t Newey-West": float(t_n[0]),
                       "verhouding": float(t_o[0] / t_n[0])}
sim_ratio = {h: np.median(np.abs(t_ols[h]) / np.abs(t_nw[h])) for h in HORIZONS_GSC}
pd.DataFrame(overlap_rows).T.assign(**{"verhouding in simulatie (mediaan)": pd.Series(sim_ratio)}).round(3)
```

Bij één maand is er niets te zien, maar bij drie en zes maanden geeft OLS $t$-waarden van 2,44 en 2,70, terwijl Newey-West op 1,60 en 1,53 blijft. De verhouding tussen de twee (1,5 tot 1,8 bij $h \geq 3$) ligt in de buurt van de mediaan uit de simulatie voor dezelfde horizonnen.

**(3)** Een onderzoeker die in 2003 alleen de twaalfmaandsregressie met OLS had gerapporteerd, had $t = 1{,}83$ gevonden. Volgens de simulatie bewijst die waarde niets, omdat overlap en persistentie samen een variabele zonder informatie vaak genoeg zo'n $t$-waarde geven.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
