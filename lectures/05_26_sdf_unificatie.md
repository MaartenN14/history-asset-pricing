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

(05-26-sdf-unificatie)=

# Cochrane: p = E[mx]

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1987–2013, van Hansen en Richard (1987) via Hansen en Jagannathan (1997)
en het handboek van Cochrane (2001, herziene druk 2005) tot Kan, Robotti en Shanken (2013).

**Wat we al weten.** Het vak had inmiddels meer feiten dan theorieën. De consumptie-SDF
haalde de Hansen-Jagannathan-grens niet ([](#03-13-equity-premium-puzzle)), het
driefactormodel paste maar wachtte op een verklaring, en momentum paste in geen enkel
model. In [](#04-25-industrie) zagen we dat beleggers inmiddels betalen voor precies die
factoren, terwijl elk model zijn eigen toets had: GRS, Fama-MacBeth of GMM op de
Euler-vergelijking.

**Welke vraag staat open.** Zijn deze modellen en toetsen verschillende theorieën, of
verschillende uitspraken over hetzelfde object, en hoe vergelijken we ze dan?
```

## Overzicht

Zijn het CAPM, het consumptie-CAPM, de APT en het driefactormodel verschillende theorieën?
Nee, want elk model is een keuze voor de *stochastic discount factor* $m$ in $p = \E[mx]$
(SDF, stochastische discontofactor: de willekeurige variabele waarmee een toekomstige
payoff wordt verdisconteerd). Daardoor zijn alle modellen met één meetlat te vergelijken.
In dit college:

- rekenen we in een economie met drie toestanden de unieke SDF in de payoff-ruimte met de
  hand uit;
- bewijzen we dat die SDF, de mean-variance-frontier en een bèta-representatie hetzelfde
  zeggen, en dat een lineair factormodel een bèta-model is;
- leiden we de Hansen-Jagannathan-afstand af, een maat voor hoe fout een model is;
- simuleren we hoe vaak een overbodige factor een significante premie krijgt terwijl zijn
  gewicht in $m$ nul is;
- schatten we met GMM (de gegeneraliseerde momentenmethode) de SDF van het CAPM, FF3 en
  FF3 plus momentum op 35 portefeuilles, naast de consumptie-SDF.

Dat zo'n $m$ bestaat, wisten we al uit de fundamentele stelling van
[](#03-11-apt-no-arbitrage). Hansen en Richard bewezen in 1987 dat een SDF, een rendement
op de frontier en een bèta-representatie drie vormen van hetzelfde zijn
{cite}`HansenRichard1987`. Tien jaar later maakten Hansen en Jagannathan er een maat van
voor modellen die niet alle portefeuilles goed waarderen {cite}`HansenJagannathan1997`.
Cochrane ordende in zijn handboek van 2001 het hele vak rond $p = \E[mx]$
{cite}`Cochrane2005`, en daarmee begon een tijdvak waarin het vak modellen meet in plaats
van toetst. Voor de vraag theorie of feit is die verschuiving het scharnier, want niemand
vraagt dan nog welk model waar is, alleen hoe ver elk model ernaast zit. Kan, Robotti en
Shanken lieten in 2013 zien dat zelfs grote verschillen in fit tussen modellen vaak niet
significant zijn {cite}`KanRobottiShanken2013`.

## Intuïtie: waarom zou dit waar zijn?

Stel dat de prijzen op een markt onderling consistent zijn, zodat dezelfde uitkering
hetzelfde kost en een dubbele uitkering het dubbele. Dan is de prijs een lineaire functie
van de uitkering, en zo'n functie is altijd een gewogen som over de toestanden. Die
gewichten vormen een discontofactor. Er is geen nutsfunctie en geen evenwicht voor nodig,
alleen de wet van één prijs.

Meestal zijn er veel van zulke discontofactoren, omdat de gewichten kunnen verschuiven in
richtingen die bij geen enkel verhandeld activum de prijs veranderen. Precies één ervan is
zelf na te maken met de verhandelde activa, en dat is de kleinste. Elke andere is dezelfde
plus ruis die geen prijs verandert. Omdat die kleinste discontofactor een portefeuille is,
ligt het rendement ervan op de frontier van Markowitz.

Daarna volgt de stap die het vak veranderde. Verwachte rendementen die lineair zijn in een
paar bèta's, komen neer op een discontofactor die lineair is in een paar factoren. Het CAPM,
het consumptie-CAPM en Fama-French verschillen dan alleen in de variabelen die in de
discontofactor mogen staan.

Daaruit volgen twee verwachtingen. Ten eerste is de kleinste discontofactor laag in
toestanden waarin de activa veel uitkeren, omdat een extra euro daar het minst waard is.
Ten tweede krijgt een factor die meebeweegt met een van de factoren in de discontofactor
een premie, ook als hij zelf niets toevoegt. Hoe sterker hij meebeweegt, hoe hoger die
premie, terwijl zijn eigen gewicht nul blijft, zodat significante premies weinig zeggen
over hoeveel factoren nodig zijn.

## Toy-voorbeeld: drie toestanden, twee activa

We nemen drie toestanden met kansen $\pi = (\tfrac14, \tfrac12, \tfrac14)$ en twee
verhandelde activa. Prijzen gelden op $t$ en payoffs op $t+1$, maar de tijdsindex laten we
weg. De eerste codecel laadt de pakketten voor het hele college.

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

| Activum | payoff in 1 | payoff in 2 | payoff in 3 | prijs $p$ |
|---|---|---|---|---|
| obligatie | 1{,}00 | 1{,}00 | 1{,}00 | 0{,}95 |
| aandeel | 1{,}50 | 1{,}00 | 0{,}50 | 0{,}90 |

Er zijn drie toestanden en maar twee prijzen, dus de markt is incompleet. Volgens
[](#thm-apt-no-arbitrage-uniek) is de SDF alleen in een complete markt uniek, zodat er hier
veel SDF's bestaan.

**Het recept.** De payoffs van alle portefeuilles vormen de *payoff-ruimte*
$\underline{X} = \{c_1\mathbf{1} + c_2 x_a\}$, met $x_a$ de payoff van het aandeel. We
zoeken het element $x^*$ daarvan waarmee elke prijs een verwachting wordt,
$p(x) = \E[x^* x]$. Met $\mathbf{G}$ de matrix van tweede momenten en $\mathbf{p}$ de
prijzen is $x^* = \mathbf{c}'\mathbf{x}$ met $\mathbf{c} = \mathbf{G}^{-1}\mathbf{p}$. Die
formule leidt de theorie straks als eerste af.

**Stap 1: de tweede momenten.** Het aandeel heeft $\E[x_a] = \tfrac14 \cdot 1{,}5 + \tfrac12 \cdot 1 + \tfrac14 \cdot 0{,}5 = 1$
en $\E[x_a^2] = \tfrac14 \cdot 2{,}25 + \tfrac12 \cdot 1 + \tfrac14 \cdot 0{,}25 = 1{,}125$.
De matrix van tweede momenten en de inverse ervan zijn dan

$$
\mathbf{G} = \begin{pmatrix} 1 & 1 \\ 1 & 1{,}125 \end{pmatrix},
\qquad
\det\mathbf{G} = 0{,}125,
\qquad
\mathbf{G}^{-1} = \begin{pmatrix} 9 & -8 \\ -8 & 8 \end{pmatrix}.
$$

**Stap 2: de gewichten.** De gewichten zijn $\mathbf{c} = (9 \cdot 0{,}95 - 8 \cdot 0{,}90;\ -8 \cdot 0{,}95 + 8 \cdot 0{,}90) = (1{,}35;\ -0{,}40)$.
Daaruit volgt $x^* = 1{,}35 - 0{,}40\,x_a = (0{,}75;\ 0{,}95;\ 1{,}15)$.

**Stap 3: de controle.** $\E[x^*] = 0{,}1875 + 0{,}475 + 0{,}2875 = 0{,}95$ is de prijs
van de obligatie, en $\E[x^* x_a] = 0{,}28125 + 0{,}475 + 0{,}14375 = 0{,}90$ is die van
het aandeel. De risicovrije rente is dan $R^f = 1/\E[x^*] = 1{,}0526$.

**Stap 4: alle andere SDF's.** De vector $\varepsilon = (1;\ -1;\ 1)$ heeft
$\E[\varepsilon] = \tfrac14 - \tfrac12 + \tfrac14 = 0$ en $\E[\varepsilon x_a] = \tfrac14 \cdot 1{,}5 - \tfrac12 + \tfrac14 \cdot 0{,}5 = 0$.
Daarom waardeert $m = x^* + k\,\varepsilon = (0{,}75 + k;\ 0{,}95 - k;\ 1{,}15 + k)$ beide
activa goed, en die $m$ is strikt positief zolang $k \in (-0{,}75;\ 0{,}95)$.

**Stap 5: de kleinste volatiliteit.** Omdat $\E[x^*\varepsilon] = \E[\varepsilon] = 0$, is
$\Var(m) = \Var(x^*) + k^2\Var(\varepsilon)$, met $\Var(\varepsilon) = 1$ en
$\Var(x^*) = 0{,}9225 - 0{,}9025 = 0{,}02$. Van alle SDF's heeft $x^*$ dus de kleinste
volatiliteit, met $\sigma(x^*)/\E[x^*] = 0{,}1414/0{,}95 = 0{,}1489$, en dat getal blijkt in
de theorie de Hansen-Jagannathan-grens van deze economie.

De codecel rekent dezelfde stappen na en zet hand en code naast elkaar. Ze bewaart ook het
rendement $R^*$ en de bèta van het aandeel, die de theorie als voorbeeld gebruikt.

```{code-cell} ipython3
prob = np.array([0.25, 0.50, 0.25])
X = np.array([[1.0, 1.5],        # state 1: bond, stock
              [1.0, 1.0],        # state 2
              [1.0, 0.5]])       # state 3
p = np.array([0.95, 0.90])
eps = np.array([1.0, -1.0, 1.0])


def E(v):
    return prob @ v


def cov(a, b):
    return E((a - E(a)) * (b - E(b)))


G = X.T @ (prob[:, None] * X)                 # second-moment matrix E[x x']
c = np.linalg.solve(G, p)                     # x* = X c
x_star = X @ c
R_f = 1 / E(x_star)
R_star = x_star / E(x_star**2)                # p(x*) = E[x*^2]
R_a = X[:, 1] / p[1]
beta_a = cov(R_a, R_star) / cov(R_star, R_star)
assert np.allclose(X.T @ (prob * eps), 0) and np.isclose(beta_a * (E(R_star) - R_f), E(R_a) - R_f)

hand = {"c_1": 1.35, "c_2": -0.40, "x* in toestand 1": 0.75, "x* in toestand 3": 1.15,
        "E[x*] (prijs obligatie)": 0.95, "E[x* x_a] (prijs aandeel)": 0.90, "R^f": 1.0526,
        "Var(x*)": 0.02, "sigma(x*)/E[x*]": 0.1489}
code = [c[0], c[1], x_star[0], x_star[2], E(x_star), E(x_star * X[:, 1]), R_f,
        cov(x_star, x_star), np.sqrt(cov(x_star, x_star)) / E(x_star)]
pd.DataFrame({"met de hand": list(hand.values()), "code": code}, index=list(hand)).round(4)
```

De twee kolommen zijn gelijk, en de SDF is laag in toestand 1, waar het aandeel veel
uitkeert, en hoog in toestand 3, waar een extra euro het meest waard is. Welke $k$ de
markt gebruikt, volgt niet uit de prijzen. Een optie die alleen in toestand 3 uitkeert,
krijgt daardoor voor elke $k$ een andere prijs, zoals de eerste oefening laat zien.

## Theorie

De afleiding gaat van één prijsfunctie naar één meetlat. De kern is dat de wet van één prijs
precies één SDF in de payoff-ruimte oplevert, de $x^*$ uit het toy-voorbeeld. Daaruit volgen
de frontier en de bèta-representatie, en een lineair factormodel blijkt een bèta-model met
een vaste sleutel tussen gewichten $b$ en premies $\lambda$. Tot slot schatten we zulke
modellen met GMM en meten we met de Hansen-Jagannathan-afstand hoe fout ze zijn.

### Opzet: payoffs als Hilbertruimte

We werken met één periode zonder tijdsindex, zoals in [](#03-11-apt-no-arbitrage). Met
$\E_t$ in plaats van $\E$ geldt alles voorwaardelijk. Payoffs zijn stochastische
variabelen met een eindig tweede moment, en samen vormen ze de ruimte $L^2$. Het inproduct
is $\E[xy]$ en de norm $\|x\| = \sqrt{\E[x^2]}$. Deze meetkundige taal komt van
{cite:t}`HansenRichard1987`, en {cite:t}`Cochrane2005` neemt ze over.

De payoff-ruimte $\underline{X} \subset L^2$ bevat de payoffs van alle portefeuilles van
verhandelde activa. We nemen aan dat die ruimte gesloten is (aanname A1) en dat de *wet
van één prijs* geldt, zodat de prijsfunctie $p$ op $\underline{X}$ lineair is (aanname
A2). Die tweede aanname is zwakker dan de afwezigheid van arbitrage, want ze zegt niets
over positieve prijzen. Een rendement heeft prijs één, $p(R) = 1$, en een overrendement
prijs nul, $p(R^e) = 0$.

### Stelling 1: er is precies één SDF in de payoff-ruimte

Ook zonder rekenwerk is te zien dat er maar één zo'n SDF bestaat. Een handelaar die de
prijs van elke portefeuille kent, zoekt per toestand een gewicht zodat elke prijs de
gewogen verwachting van de payoff wordt. Omdat prijzen lineair zijn, lukt dat altijd met
een gewicht dat zelf een portefeuille is. Als er een tweede zo'n portefeuille bestond, zou
het verschil elke portefeuille de prijs nul geven. Dat geldt ook voor het verschil zelf,
en een payoff met tweede moment nul is gelijk aan nul.

:::{prf:theorem} Riesz-representatie van de prijsfunctie
:label: thm-sdf-unificatie-xstar

Laat $\underline{X}$ een gesloten deelruimte van $L^2$ zijn en $p$ een continue lineaire
prijsfunctie op die ruimte. Dan gelden drie uitspraken.

1. Er bestaat precies één $x^* \in \underline{X}$ met $p(x) = \E[x^* x]$ voor alle $x \in \underline{X}$.
2. Een $m \in L^2$ is een SDF, $p(x) = \E[mx]$ voor alle $x \in \underline{X}$, dan en
   slechts dan als $m = x^* + \varepsilon$ met $\E[\varepsilon x] = 0$ voor alle $x \in \underline{X}$.
3. $x^*$ is de orthogonale projectie van elke SDF op $\underline{X}$, en $\E[m^2] \ge \E[x^{*2}]$.
   Als $\mathbf{1} \in \underline{X}$ geldt bovendien $\E[m] = \E[x^*]$ en $\sigma(m) \ge \sigma(x^*)$.

Neem een eindig-dimensionaal geval met basis $\mathbf{x} = (x_1, \dots, x_N)'$, prijzen
$\mathbf{p}$ en inverteerbare $\mathbf{G} = \E[\mathbf{x}\mathbf{x}']$. Dan is

```{math}
:label: eq-sdf-unificatie-xstar
x^* = \mathbf{p}'\mathbf{G}^{-1}\mathbf{x} .
```
:::

Vergelijking [](#eq-sdf-unificatie-xstar) zegt dat $x^*$ de portefeuille met gewichten
$\mathbf{G}^{-1}\mathbf{p}$ is, in het toy-voorbeeld $(1{,}35;\ -0{,}40)$.

:::{prf:proof}
:class: dropdown

*Bestaan: $x^*$ lost een lineair stelsel op.* In eindige dimensie stellen we
$x^* = \mathbf{c}'\mathbf{x}$ en eisen we $\E[x^* x_i] = p_i$ voor elke basisvector. Dat is
$\mathbf{G}\mathbf{c} = \mathbf{p}$, dus $\mathbf{c} = \mathbf{G}^{-1}\mathbf{p}$, wat
[](#eq-sdf-unificatie-xstar) geeft. Lineariteit van $p$ (A2) brengt de gelijkheid van de
basis over op heel $\underline{X}$. In oneindige dimensie is dit de representatiestelling van
Riesz voor de Hilbertruimte $\underline{X}$, die gesloten is (A1).

*Uniciteit: het verschil heeft norm nul.* Als $x^*$ en $y^*$ in $\underline{X}$ allebei
werken, is $\E[(x^* - y^*)x] = 0$ voor alle $x \in \underline{X}$, ook voor
$x = x^* - y^*$. Dan is $\E[(x^* - y^*)^2] = 0$.

*Karakterisering: de rest staat loodrecht op de payoffs.* Als $m$ een SDF is, is
$\varepsilon = m - x^*$ orthogonaal aan $\underline{X}$ omdat
$\E[mx] - \E[x^*x] = p(x) - p(x) = 0$. Omgekeerd waardeert $x^* + \varepsilon$ met zo'n
$\varepsilon$ alles goed. Omdat $\varepsilon \perp \underline{X}$, is $x^*$ de projectie van
$m$ en geldt $\E[m^2] = \E[x^{*2}] + \E[\varepsilon^2]$. Als $\mathbf{1} \in \underline{X}$,
is $\E[\varepsilon] = \E[\varepsilon \cdot \mathbf{1}] = 0$, zodat $m$ en $x^*$ hetzelfde
gemiddelde hebben en ook de varianties optellen. $\square$
:::

De fundamentele stelling ([](#thm-apt-no-arbitrage-fundamenteel)) zegt dat er een positieve
$m$ bestaat zodra arbitrage onmogelijk is. Deze stelling voegt toe dat er altijd één
kanonieke $m$ is. De keuzevrijheid uit [](#thm-apt-no-arbitrage-uniek) is precies de ruimte
$\underline{X}^{\perp}$ loodrecht op alle payoffs, in het toy-voorbeeld de veelvouden van
$\varepsilon$. De minimum-variantie-SDF achter de Hansen-Jagannathan-grens
([](#thm-equity-premium-puzzle-frontier)) is punt 3, toegepast op de constante en de
rendementen. Positief hoeft $x^*$ niet te zijn, en in de replicatie wordt de geschatte SDF
af en toe negatief.

### Stelling 2: $R^*$ ligt op de frontier

Het rendement van $x^*$ ligt op de *mean-variance-frontier* (de minimum-variantierand, met
bij elk gemiddelde de kleinste variantie). Omdat $x^*$ het kortste element is dat alle
prijzen goed geeft, heeft het rendement ervan het kleinste tweede moment van alle
rendementen. Elk rendement kost namelijk één, zodat $\E[x^*R] = 1$ en Cauchy-Schwarz
$\|R\| \ge 1/\|x^*\|$ geeft, precies de norm van $R^* = x^*/\E[x^{*2}]$. Een belegger die
een hoger gemiddelde wil, schuift van dat punt af langs de enige richting die het
gemiddelde verandert. We definiëren

```{math}
:label: eq-sdf-unificatie-rstar
R^* = \frac{x^*}{p(x^*)} = \frac{x^*}{\E[x^{*2}]},
\qquad
R^{e*} = \operatorname{proj}\left(\mathbf{1} \mid \underline{R}^{e}\right),
```

met $\underline{R}^e$ de ruimte van overrendementen. Zo is $R^*$ de SDF geschaald tot prijs
één, en is $R^{e*}$ het overrendement dat het dichtst bij de constante één ligt. Omdat
$R^{e*}$ een projectie van de constante is, geldt $\E[R^e] = \E[R^{e*}R^e]$ voor elk
overrendement.

:::{prf:theorem} Orthogonale decompositie van Hansen en Richard
:label: thm-sdf-unificatie-frontier

Neem aan dat $\E[R^{e*}] \neq 0$. Dan is elk rendement $R$ te schrijven als

```{math}
:label: eq-sdf-unificatie-decompositie
R = R^* + w\,R^{e*} + n,
\qquad
\E[n] = \E[nR^*] = \E[nR^{e*}] = 0,
```

met $w$ een scalair en $n$ een overrendement. $R$ ligt op de mean-variance-frontier
dan en slechts dan als $n = 0$. In het bijzonder ligt $R^*$ op de frontier: het is
het rendement met het kleinste tweede moment.
:::

:::{prf:proof}
:class: dropdown

*Stap 1: drie richtingen staan loodrecht op elkaar.* (a) $R^*$ staat loodrecht op elk
overrendement, want $\E[R^* R^e] = \E[x^*R^e]/\E[x^{*2}] = p(R^e)/\E[x^{*2}] = 0$. In het
bijzonder is $\E[R^*R^{e*}] = 0$. (b) Voor elk overrendement $n \perp R^{e*}$ geldt
$\E[n] = \E[n \cdot \mathbf{1}] = \E[n\,R^{e*}] + \E[n(\mathbf{1} - R^{e*})] = 0 + 0$,
omdat $\mathbf{1} - R^{e*}$ loodrecht op de hele ruimte $\underline{R}^e$ staat.

*Stap 2: elk rendement valt zo uiteen.* $R - R^*$ kost $1 - 1 = 0$ en is dus een
overrendement. Kies $w = (\E[R] - \E[R^*])/\E[R^{e*}]$ en $n = R - R^* - wR^{e*}$. Dan is
$n$ een overrendement met $\E[n] = 0$. Uit de projectie-eigenschap volgt
$\E[nR^{e*}] = \E[n] = 0$, en uit (a) volgt $\E[nR^*] = 0$.

*Stap 3: de frontier is $n = 0$.* Uit [](#eq-sdf-unificatie-decompositie) en de
orthogonaliteiten volgt $\E[R] = \E[R^*] + w\,\E[R^{e*}]$. Voor het tweede moment geldt

$$
\E[R^2] = \E[R^{*2}] + w^2\,\E[R^{e*2}] + \E[n^2] .
$$

Rendementen met hetzelfde gemiddelde hebben dezelfde $w$, dus minimale variantie precies
als $n = 0$. Met $w = 0$ en $n = 0$ is dat $R^*$, het kleinste tweede moment. $\square$
:::

Volgens [](#eq-sdf-unificatie-decompositie) bestaat elk rendement uit $R^*$, een
hoeveelheid $w$ van de richting die het gemiddelde verhoogt, en ruis $n$ die alleen
variantie kost. De frontier is daarom de lijn $\{R^* + wR^{e*}\}$. Zo keert de
twee-fondsenstelling van [](#01-04-markowitz) terug, want elke portefeuille op de frontier
mengt twee vaste fondsen, $R^*$ zelf en het rendement $R^* + R^{e*}$, dat de richting die
het gemiddelde verhoogt bij $R^*$ optelt. De bèta-representatie volgt nu zonder evenwicht.

:::{prf:corollary} SDF, frontier en bèta zijn equivalent
:label: cor-sdf-unificatie-beta

Definieer de nulbèta-rente $R^0 = \E[R^{*2}]/\E[R^*]$. Dan geldt voor elk rendement

```{math}
:label: eq-sdf-unificatie-beta-rstar
\E[R] = R^0 + \beta_{R,R^*}\left(\E[R^*] - R^0\right),
\qquad
\beta_{R,R^*} = \frac{\Cov(R, R^*)}{\Var(R^*)} .
```

Als $\mathbf{1} \in \underline{X}$ is $R^0 = R^f$. Omgekeerd: als een rendement
$R^{mv}$ een bèta-representatie heeft voor alle activa, dan ligt $R^{mv}$ op de
frontier en is $m = a + b R^{mv}$ een SDF voor geschikte $a, b$ (mits
$R^{mv}$ niet de minimum-variantieportefeuille is).
:::

:::{prf:proof}
:class: dropdown

*Stap 1: de bèta-vorm.* Uit $x^* = R^*/\E[R^{*2}]$ en $p(R) = 1$ volgt
$\E[R^*R] = \E[R^{*2}]$ voor elk rendement. Schrijf het linkerlid als
$\Cov(R, R^*) + \E[R^*]\E[R]$, dan volgt $\E[R] = R^0 - \Cov(R, R^*)/\E[R^*]$. Voor
$R = R^*$ geeft dit $\E[R^*] - R^0 = -\Var(R^*)/\E[R^*]$, en de eerste gedeeld door de
tweede geeft [](#eq-sdf-unificatie-beta-rstar).

*Stap 2: de constante is de rente.* Met $\mathbf{1} \in \underline{X}$ is $\E[x^*] = 1/R^f$.
Daaruit volgt $R^0 = \E[R^{*2}]/\E[R^*] = (1/\E[x^{*2}])/(\E[x^*]/\E[x^{*2}]) = R^f$.

*Stap 3: de omkering.* Een bèta-representatie op $R^{mv}$ zegt dat $\E[R_i]$ affien is in
$\Cov(R_i, R^{mv})$. Kies $a, b$ zodat $\E[(a + bR^{mv})R_i] = 1$ voor twee rendementen met
verschillende bèta, en lineariteit geeft het voor alle. $\square$
:::

Het verwachte rendement daalt dus met de bèta op $R^*$, omdat $R^*$ een verzekering is die
het meest uitkeert in de toestand waarin het aandeel het minst oplevert, en daarom minder
verdient dan de rente. In het toy-voorbeeld is $p(x^*) = \E[x^{*2}] = 0{,}9225$, zodat

$$
R^* = \frac{x^*}{0{,}9225} = (0{,}8130;\ 1{,}0298;\ 1{,}2466), \qquad
\E[R^*] = \frac{0{,}95}{0{,}9225} = 1{,}0298 ,
$$

minder dan de risicovrije rente van 1,0526. Het aandeel heeft $\E[R_a] = 1/0{,}90 = 1{,}1111$
en dus een overrendement van 0,0585. Omdat $x^*$ lineair is in $x_a$ met helling $-0{,}40$,
is $\Cov(x_a, x^*) = -0{,}40 \cdot 0{,}125 = -0{,}05$, en daarmee

$$
\beta_{a,R^*} = \frac{-0{,}05}{0{,}02} \cdot \frac{0{,}9225}{0{,}90} = -2{,}5625,
\qquad
\beta_{a,R^*}\left(\E[R^*] - R^f\right) = -2{,}5625 \cdot (-0{,}022821) = 0{,}0585 .
$$

Dat is precies het overrendement van het aandeel, en ook $R^0 = (1/0{,}9225)/1{,}0298$ is
gelijk aan $R^f$. Omdat het aandeel het enige risicovolle activum is, ligt het zelf op de
frontier. De Sharpe-ratio ervan haalt de Hansen-Jagannathan-grens daarom precies, want
$0{,}0585/0{,}3928 = 0{,}1489 = \sigma(x^*)/\E[x^*]$.

De bèta-vorm van het CAPM ([](#prop-capm-beta)) en de SDF van Fama en French
([](#thm-fama-french-sdf)) zijn speciale gevallen. Het CAPM zegt namelijk alleen dat de
marktportefeuille voor een zekere $w$ gelijk is aan $R^* + wR^{e*}$.

### Stelling 3: lineaire factormodellen zijn bèta-modellen

Een SDF die lineair is in een paar factoren, is hetzelfde als een bèta-model op die
factoren. Een overrendement kost niets, dus moet $\E[mR^e] = 0$ gelden, en die verwachting
valt uiteen in het product van de gemiddelden plus een covariantie. Is $m$ lineair in
factoren, dan zijn die covarianties, op een schaal na, gelijk aan bèta's. Een activum dat
verliest wanneer $m$ hoog is, moet daardoor een hoger gemiddeld rendement bieden.

:::{prf:theorem} Van $m = a + \mathbf{b}'\mathbf{f}$ naar $\E[R^e] = \boldsymbol{\beta}'\boldsymbol{\lambda}$
:label: thm-sdf-unificatie-factor

Laat $\mathbf{f}$ een vector van $K$ factoren zijn met inverteerbare
$\boldsymbol{\Sigma}_f = \Var(\mathbf{f})$. Schrijf $\boldsymbol{\beta}_i = \boldsymbol{\Sigma}_f^{-1}\Cov(\mathbf{f}, R^e_i)$
voor de meervoudige regressiebèta's.

1. Als $m = a + \mathbf{b}'\mathbf{f}$ met $\E[m] \neq 0$ alle overrendementen goed
   waardeert, dan is

   ```{math}
   :label: eq-sdf-unificatie-lambda
   \E\!\left[R^e_i\right] = \boldsymbol{\beta}_i'\boldsymbol{\lambda},
   \qquad
   \boldsymbol{\lambda} = -\frac{\boldsymbol{\Sigma}_f\,\mathbf{b}}{\E[m]} .
   ```

2. Omgekeerd: als $\E[R^e_i] = \boldsymbol{\beta}_i'\boldsymbol{\lambda}$ voor alle $i$, dan
   waardeert $m = 1 - \boldsymbol{\lambda}'\boldsymbol{\Sigma}_f^{-1}(\mathbf{f} - \E\mathbf{f})$
   alle overrendementen goed, met $\E[m] = 1$.
:::

:::{prf:proof}
*Van $m$ naar bèta.* Uit $\E[mR^e_i] = 0$ volgt $0 = \E[m]\E[R^e_i] + \Cov(m, R^e_i) = \E[m]\E[R^e_i] + \mathbf{b}'\Cov(\mathbf{f}, R^e_i)$.
Met $\Cov(\mathbf{f}, R^e_i) = \boldsymbol{\Sigma}_f\boldsymbol{\beta}_i$ volgt $\E[R^e_i] = -\mathbf{b}'\boldsymbol{\Sigma}_f\boldsymbol{\beta}_i/\E[m] = \boldsymbol{\beta}_i'\boldsymbol{\lambda}$.
*Van bèta naar $m$.* Invullen geeft $\E[mR^e_i] = \E[R^e_i] - \boldsymbol{\lambda}'\boldsymbol{\Sigma}_f^{-1}\Cov(\mathbf{f}, R^e_i) = \E[R^e_i] - \boldsymbol{\lambda}'\boldsymbol{\beta}_i = 0$.
$\square$
:::

Volgens [](#eq-sdf-unificatie-lambda) is de premie van een factor een gewogen som van alle
gewichten in $\mathbf{b}$, met als weging de covariantie van die factor met elk van de
andere. Het minteken staat er omdat een hoge $m$ slechte tijden aangeeft. Met alleen
overrendementen ligt de schaal van $m$ niet vast, dus normaliseren we tot $m = 1 - \mathbf{b}'(\mathbf{f} - \E\mathbf{f})$,
zoals in [](#thm-fama-french-sdf). Dan wordt de vertaalsleutel

```{math}
:label: eq-sdf-unificatie-sleutel
\boldsymbol{\lambda} = \boldsymbol{\Sigma}_f\,\mathbf{b},
\qquad
\mathbf{b} = \boldsymbol{\Sigma}_f^{-1}\boldsymbol{\lambda} .
```

Vergelijking [](#eq-sdf-unificatie-sleutel) vertaalt gewichten in premies met de
covariantiematrix van de factoren. Voor een verhandelde factor is de premie gelijk aan
zijn gemiddelde overrendement, zodat $\mathbf{b} = \boldsymbol{\Sigma}_f^{-1}\E[\mathbf{f}]$.
In de simulatie geeft dat voor markt, SMB en HML gewichten van ongeveer 3,5, 0,65 en 4,9.

Daarmee past de hele eerste helft van dit boek in één tabel. Het subscript $m$ bij $R^e_m$
staat daarin voor de markt, niet voor de SDF.

| Model | factoren in $m$ | wat de theorie over $\mathbf{b}$ zegt | college |
|---|---|---|---|
| CAPM | $R^e_m$ | $b = \E[R^e_m]/\sigma^2_m$; de markt is $R^* + wR^{e*}$ | [](#02-08-capm) |
| consumptie-CAPM | $\Delta c$ (lineair benaderd) | $b$ is de risicoaversie $\gamma$, $a$ volgt uit de tijdsvoorkeur en $R^f$ | [](#03-12-consumptie-capm) |
| ICAPM | $R^e_m$ en toestandsvariabelen $\mathbf{z}$ | gewichten uit hedgebehoeften; welke $\mathbf{z}$ zegt de theorie niet | [](#03-10-merton-icapm) |
| APT | $K$ dominante covariantierichtingen | $\mathbf{b}$ vrij; alleen $K$ klein | [](#03-11-apt-no-arbitrage) |
| FF3 | $R^e_m$, SMB, HML | $\mathbf{b} = \boldsymbol{\Sigma}_f^{-1}\E[\mathbf{f}]$ want verhandeld | [](#04-18-fama-french) |

De derde kolom zegt van boven naar beneden steeds minder over $\mathbf{b}$, want het
consumptie-CAPM legt $\mathbf{b}$ vast met een voorkeursparameter, terwijl voor FF3 alleen
de eis overblijft dat een verhandelde factor zichzelf goed waardeert. De modellen worden
zo steeds minder een theorie die iets verbiedt, en steeds meer een beschrijving van
feiten.

### De prijs van risico $b$ tegenover de premie $\lambda$

Premie en gewicht meten iets anders, wat zichtbaar wordt als een onderzoeker een factor
toevoegt die sterk met HML meebeweegt. Die factor krijgt een premie, omdat hij in dezelfde
slechte tijden verliest als HML. De premie $\lambda_j$ is de beloning per eenheid bèta en
is niet nul zodra de factor met de SDF samenhangt, ook via een andere factor. Het gewicht
$b_j$ meet de eigen bijdrage van factor $j$, gegeven alle andere. Zit alleen HML in $m$,
dan heeft de nieuwe factor een grote $\lambda$ en een $b$ van nul.

:::{prf:proposition} Wat $b$ en $\lambda$ toetsen
:label: prop-sdf-unificatie-b-lambda

Normaliseer $m = 1 - \mathbf{b}'(\mathbf{f} - \E\mathbf{f})$. Dan geldt

```{math}
:label: eq-sdf-unificatie-b-lambda
\lambda_j = -\Cov(f_j, m),
\qquad
b_j = 0 \iff m \text{ is een lineaire functie van } \mathbf{f}_{-j} \text{ alleen}.
```

Dus zegt $\lambda_j \neq 0$ dat $f_j$ met de SDF samenhangt en een premie heeft, terwijl
$b_j \neq 0$ zegt dat $f_j$ nodig is om de activa te waarderen, gegeven de andere factoren.
Als de factoren ongecorreleerd zijn, vallen de twee vragen samen.
:::

:::{prf:proof}
$\Cov(f_j, m) = -\sum_k \Cov(f_j, f_k)\,b_k = -(\boldsymbol{\Sigma}_f\mathbf{b})_j = -\lambda_j$.
De tweede uitspraak is de definitie van $\mathbf{b}$ als coëfficiënt van $f_j$ in $m$.
Is $\boldsymbol{\Sigma}_f$ diagonaal, dan is $\lambda_j = \sigma_j^2 b_j$. $\square$
:::

De tweede verwachting uit de intuïtie komt dus uit, want hoe sterker een overbodige factor
met een factor uit $m$ correleert, hoe groter zijn premie, terwijl zijn gewicht nul
blijft. Cochrane concludeert daarom dat een onderzoeker die wil weten of een factor nodig
is, $b$ toetst en niet $\lambda$ {cite}`Cochrane2005`. De simulatie bouwt dat voorbeeld
na.

### GMM voor lineaire SDF-modellen

Omdat $\E[mR^e] = 0$ lineair is in $\mathbf{b}$, wordt GMM een gewogen regressie van
gemiddelde overrendementen op hun covarianties met de factoren, zonder intercept, en die
schatter levert straks de simulatie en tabel (1) van de replicatie. Het is
dezelfde soort momentvoorwaarde als de Euler-vergelijking van [](#03-12-consumptie-capm).
Neem $T$ waarnemingen, $N$ testactiva, bijvoorbeeld 25 size/BM-portefeuilles, en
$\bar{\mathbf{f}}$ het steekproefgemiddelde van de factoren. De momenten zijn dan

```{math}
:label: eq-sdf-unificatie-momenten
\mathbf{g}_T(\mathbf{b}) = \frac1T\sum_t \mathbf{R}^e_t\left(1 - (\mathbf{f}_t - \bar{\mathbf{f}})'\mathbf{b}\right)
= \bar{\mathbf{R}}^e - \mathbf{C}\,\mathbf{b},
\qquad
\mathbf{C} = \widehat{\Cov}(\mathbf{R}^e, \mathbf{f}') \in \mathbb{R}^{N \times K}.
```

De prijsfout $\mathbf{g}_T$ is dus het gemiddelde overrendement min het deel dat de
covarianties verklaren. Minimaliseren van $\mathbf{g}_T'\mathbf{W}\mathbf{g}_T$ geeft

```{math}
:label: eq-sdf-unificatie-bhat
\hat{\mathbf{b}} = \left(\mathbf{C}'\mathbf{W}\mathbf{C}\right)^{-1}\mathbf{C}'\mathbf{W}\bar{\mathbf{R}}^e ,
```

een gewogen regressie van $\bar{\mathbf{R}}^e$ op de kolommen van $\mathbf{C}$. De eerste
stap neemt $\mathbf{W} = \mathbf{I}$ en de tweede $\mathbf{W} = \hat{\mathbf{S}}^{-1}$,
met $\hat{\mathbf{S}}$ de geschatte covariantiematrix van de momenten uit
[](#thm-consumptie-capm-gmm). Onder het model is $J_T = T\mathbf{g}_T'\hat{\mathbf{S}}^{-1}\mathbf{g}_T$
dan $\chi^2(N-K)$-verdeeld.

Ook $\bar{\mathbf{f}}$ is geschat, en de afgeleide van het moment naar $\E\mathbf{f}$ is
$\E[\mathbf{R}^e]\mathbf{b}'$. Daarom bouwen we $\hat{\mathbf{S}}$ uit

```{math}
:label: eq-sdf-unificatie-h
\mathbf{h}_t = \mathbf{R}^e_t\left(1 - (\mathbf{f}_t - \bar{\mathbf{f}})'\hat{\mathbf{b}}\right)
+ \bar{\mathbf{R}}^e\,(\mathbf{f}_t - \bar{\mathbf{f}})'\hat{\mathbf{b}},
```

waarin de tweede term corrigeert voor de geschatte factorgemiddelden. Die correctie is
klein, omdat $\bar{\mathbf{R}}^e$ klein is ten opzichte van de rendementen zelf. De
variantie van de schatter is $\widehat{\Var}(\hat{\mathbf{b}}) = T^{-1}(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W}\hat{\mathbf{S}}\mathbf{W}\mathbf{C}(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}$.
De premies zijn $\hat{\boldsymbol{\lambda}} = \hat{\boldsymbol{\Sigma}}_f\hat{\mathbf{b}}$,
waarbij we $\hat{\boldsymbol{\Sigma}}_f$ als bekend behandelen. Dat mag, omdat een
covariantiematrix na een paar honderd maanden veel nauwkeuriger gemeten is dan een
gemiddelde.

### Stelling 4: de Hansen-Jagannathan-afstand

De Hansen-Jagannathan-afstand meet hoe ver de SDF van een model van de dichtstbijzijnde
geldige SDF ligt. Die afstand is tegelijk de grootste prijsfout van het model op een
portefeuille met norm één. Met genoeg data verwerpt $J$ elk model, dus is de bruikbare
vraag hoe fout een model is. Anders dan bij $J$ is de weegmatrix voor alle modellen
dezelfde, zodat een model zijn afstand niet kan verkleinen door ruisiger momenten.

:::{prf:theorem} Hansen-Jagannathan-afstand
:label: thm-sdf-unificatie-hj

Laat $\underline{X}$ opgespannen worden door $\mathbf{x}$ met prijzen $\mathbf{p}$ en
$\mathbf{G} = \E[\mathbf{x}\mathbf{x}']$ inverteerbaar, en laat
$\mathcal{M} = \{m \in L^2 : \E[m\mathbf{x}] = \mathbf{p}\}$ de verzameling SDF's zijn.
Voor een kandidaat $y \in L^2$ met prijsfouten $\mathbf{g} = \E[y\mathbf{x}] - \mathbf{p}$ geldt

```{math}
:label: eq-sdf-unificatie-hj
\delta(y) \equiv \min_{m \in \mathcal{M}} \|y - m\|
= \max_{x \in \underline{X},\ \|x\| = 1} \left|\E[yx] - p(x)\right|
= \sqrt{\mathbf{g}'\mathbf{G}^{-1}\mathbf{g}} .
```

Voor een familie $y(\mathbf{b})$ is de HJ-afstand van het model $\min_{\mathbf{b}}\delta(y(\mathbf{b}))$.
Die minimalisatie is GMM met $\mathbf{W} = \mathbf{G}^{-1}$.
:::

:::{prf:proof}
:class: dropdown

*Stap 1: de afstand is de lengte van het deel in de payoff-ruimte.* Door
[](#thm-sdf-unificatie-xstar) is $\mathcal{M} = x^* + \underline{X}^{\perp}$. Schrijf
$y - x^* = u + v$ met $u \in \underline{X}$ en $v \perp \underline{X}$. Voor
$m = x^* + e$ met $e \perp \underline{X}$ is $\|y - m\|^2 = \|u\|^2 + \|v - e\|^2$,
minimaal bij $e = v$, met waarde $\|u\|$. Nu is $u = \mathbf{c}'\mathbf{x}$ met
$\mathbf{c} = \mathbf{G}^{-1}\E[\mathbf{x}(y - x^*)] = \mathbf{G}^{-1}\mathbf{g}$, dus
$\|u\|^2 = \mathbf{c}'\mathbf{G}\mathbf{c} = \mathbf{g}'\mathbf{G}^{-1}\mathbf{g}$.

*Stap 2: dezelfde waarde is de grootste prijsfout.* Een payoff $x = \boldsymbol{\alpha}'\mathbf{x}$
heeft prijsfout $\boldsymbol{\alpha}'\mathbf{g}$ en norm
$\sqrt{\boldsymbol{\alpha}'\mathbf{G}\boldsymbol{\alpha}}$. Cauchy-Schwarz in het
$\mathbf{G}$-inproduct geeft $|\boldsymbol{\alpha}'\mathbf{g}| = |(\mathbf{G}^{1/2}\boldsymbol{\alpha})'(\mathbf{G}^{-1/2}\mathbf{g})| \le \sqrt{\boldsymbol{\alpha}'\mathbf{G}\boldsymbol{\alpha}}\sqrt{\mathbf{g}'\mathbf{G}^{-1}\mathbf{g}}$,
met gelijkheid voor $\boldsymbol{\alpha} \propto \mathbf{G}^{-1}\mathbf{g}$. $\square$
:::

Volgens [](#eq-sdf-unificatie-hj) volgt de afstand alleen uit de prijsfouten $\mathbf{g}$
en de tweede momenten van de payoffs. Met overrendementen is $\mathbf{p} = \mathbf{0}$ en
$\mathbf{G} = \E[\mathbf{R}^e\mathbf{R}^{e\prime}]$. Een afstand van 0,3 in maanddata
betekent een prijsfout van 30% per maand op een portefeuille met $\sqrt{\E[x^2]} = 1$, dus
1,5% per maand bij een volatiliteit van 5%. Een model kan $J$ verlagen door
$\hat{\mathbf{S}}$ op te blazen, maar $\delta$ niet, omdat de afstand een ruisige
kandidaat niet beloont {cite}`HansenJagannathan1997`.

In een steekproef is $\hat\delta$ ook voor het ware model groter dan nul, dus moeten we
weten hoe groot die ruisbodem is voordat we een geschatte afstand beoordelen. Onder een
juist model is $\sqrt{T}\mathbf{g}_T(\hat{\mathbf{b}}) \to N(\mathbf{0}, \mathbf{P}\mathbf{S}\mathbf{P}')$
met $\mathbf{P} = \mathbf{I} - \mathbf{C}(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W}$.
Daardoor is $T\hat\delta^2$ een gewogen som van $\chi^2(1)$-variabelen, met als gewichten de
eigenwaarden van $\mathbf{G}^{-1/2}\mathbf{P}\mathbf{S}\mathbf{P}'\mathbf{G}^{-1/2}$,
zodat we de $p$-waarde door simulatie vinden. De ruisbodem ligt ongeveer bij
$\sqrt{(N-K)/T}$, voor 35 portefeuilles en 757 maanden dus rond 0,2. Zolang $\mathbf{S}$
dicht bij $\mathbf{G}$ ligt, zijn de $N-K$ gewichten namelijk ongeveer één, zodat
$\E[T\hat\delta^2] \approx N - K$.

:::{note} Conditionele modellen zijn ook factormodellen
:class: dropdown

Vermenigvuldig $0 = \E_t[m_{t+1}R^e_{t+1}]$ met een signaal $z_t$ dat op $t$ bekend is,
bijvoorbeeld de dividend-prijsratio. Onvoorwaardelijke verwachtingen geven dan
$0 = \E[m_{t+1}(z_tR^e_{t+1})]$, zodat een conditioneel model een onvoorwaardelijk model op
een grotere payoff-ruimte is {cite}`HansenRichard1987`. Een CAPM met
$m_{t+1} = a_t - b_t R^e_{m,t+1}$ en $a_t, b_t$ lineair in $z_t$ wordt zo een model met
factoren $R^e_m$, $z_t$ en $z_tR^e_{m,t+1}$. Jagannathan en Wang {cite}`JagannathanWang1996`
verklaarden op die manier, met menselijk kapitaal erbij, een groot deel van de spreiding in
gemiddelde rendementen. De tweede oefening schat zo'n model.
:::

```{admonition} Samengevat
:class: tip

- De wet van één prijs geeft precies één SDF in de payoff-ruimte,
  $x^* = \mathbf{p}'\mathbf{G}^{-1}\mathbf{x}$ ([](#eq-sdf-unificatie-xstar)); elke andere
  SDF is $x^*$ plus ruis en heeft een hogere volatiliteit.
- $R^*$ ligt op de frontier, en het verwachte rendement daalt met de bèta op $R^*$
  ([](#eq-sdf-unificatie-beta-rstar)), omdat $R^*$ een verzekering is.
- Een lineaire SDF is een bèta-model met $\boldsymbol{\lambda} = \boldsymbol{\Sigma}_f\mathbf{b}$
  ([](#eq-sdf-unificatie-sleutel)). Correleert een factor sterker met een factor uit $m$, dan
  stijgt zijn premie terwijl zijn gewicht gelijk blijft ([](#eq-sdf-unificatie-b-lambda)).
- De HJ-afstand ([](#eq-sdf-unificatie-hj)) is de grootste prijsfout op een portefeuille met
  norm één, en ligt in een steekproef rond $\sqrt{(N-K)/T}$ als het model juist is.
- GMM op $\E[mR^e] = 0$ is een gewogen regressie van gemiddelde overrendementen op hun
  covarianties met de factoren ([](#eq-sdf-unificatie-bhat)), en $J$ is onder het model
  $\chi^2(N-K)$-verdeeld.
```

## Simulatie: een overbodige factor met een significante premie

Hoe vaak lijkt een overbodige factor nodig als een onderzoeker naar de premie van die
factor kijkt, en hoe vaak als hij naar het gewicht kijkt? We bouwen een economie waarin
FF3 de ware SDF geeft, met correlaties van 0,3 tussen markt en SMB en van $-0{,}2$ tussen
markt en HML. De overige kalibratie staat in de tabel en volgt de orde van grootte van
echte maanddata, want drie toestanden zijn te weinig voor een GMM-schatting.

| per maand | markt | SMB | HML |
|---|---|---|---|
| gemiddelde | 0,60% | 0,20% | 0,35% |
| volatiliteit | 4,5% | 3,0% | 3,0% |
| ladingen van de 25 testactiva | rond 1 | van 1,2 tot −0,2 | van −0,4 tot 0,8 |

De testactiva hebben precies $\E[R^e_i] = \boldsymbol{\beta}_i'\E[\mathbf{f}]$. Ze laden
bovendien met $\theta_i \sim N(0;\ 0{,}5^2)$ op een schok $u$ zonder premie, met een
volatiliteit van 3%, zoals een contrast tussen bedrijfstakken. Die schok speelt de rol van
$\varepsilon$ uit het toy-voorbeeld, want hij beweegt rendementen zonder een prijs te
veranderen. De onderzoeker krijgt een vierde, verhandelde factor aangeboden,
$g = \mathrm{HML} + u$. Die is overbodig ($b_g = 0$), maar correleert
$0{,}03/\sqrt{0{,}03^2 + 0{,}03^2} = 0{,}71$ met HML en heeft daardoor een premie
$\lambda_g = \E[\mathrm{HML}] = 0{,}35\%$ per maand.

We schatten het vierfactormodel op 1000 steekproeven van vijftig jaar, met tweestaps-GMM en
met Fama-MacBeth zonder intercept. De eerste cel definieert de schatters volgens
[](#eq-sdf-unificatie-bhat) en [](#eq-sdf-unificatie-hj).

```{code-cell} ipython3
:label: cel-sdf-unificatie-gmm

# TODO: naar hap.stats (GMM for linear SDF models, HJ distance, Fama-MacBeth without intercept)
CHI2_DRAWS = rng.chisquare(1, (4000, 50))          # shared draws for weighted chi-square p-values


def linear_sdf_gmm(Re, F, weight="efficient"):
    """GMM for m = 1 - b'(f - E f) on excess returns Re (T x N) and factors F (T x K).

    weight = "efficient": two-step GMM, J test.  weight = "hj": W = E[Re Re']^-1,
    Hansen-Jagannathan distance with a simulated p-value.  Standard errors account for
    the estimated factor means; lambda = Sigma_f b treats Sigma_f as known.
    """
    T, N = Re.shape
    Fc = F - F.mean(axis=0)
    ebar = Re.mean(axis=0)
    C = Re.T @ Fc / T                                      # Cov(R^e, f'), N x K

    def estimate(W):
        return np.linalg.solve(C.T @ W @ C, C.T @ W @ ebar)

    def spectral(b):
        h = Re * (1 - Fc @ b)[:, None] + np.outer(Fc @ b, ebar)
        return h.T @ h / T

    if weight == "hj":
        W = np.linalg.inv(Re.T @ Re / T)
    else:
        W = np.linalg.inv(spectral(estimate(np.eye(N))))
    b = estimate(W)
    S = spectral(b)
    V = np.linalg.inv(C.T @ W @ C)
    cov_b = V @ C.T @ W @ S @ W @ C @ V / T
    Sigma_f = Fc.T @ Fc / T
    g = ebar - C @ b
    out = {"b": b, "se_b": np.sqrt(np.diag(cov_b)), "lam": Sigma_f @ b,
           "se_lam": np.sqrt(np.diag(Sigma_f @ cov_b @ Sigma_f)), "g": g,
           "sd_m": np.sqrt(b @ Sigma_f @ b)}
    if weight == "hj":
        P = np.eye(N) - C @ V @ C.T @ W
        root = np.linalg.cholesky(W)
        weights = np.clip(np.linalg.eigvalsh(root.T @ P @ S @ P.T @ root), 0.0, None)
        out["hj"] = np.sqrt(g @ W @ g)
        # p-value: simulated weighted sum of chi2(1) draws, weights = eigenvalues above
        out["p_hj"] = np.mean(CHI2_DRAWS[:, :N] @ weights >= T * g @ W @ g)
    else:
        out["J"] = T * g @ W @ g
        out["p_J"] = stats.chi2.sf(out["J"], N - F.shape[1])
    return out


def fama_macbeth_no_const(Re, F):
    """Full-sample multiple-regression betas, then monthly cross-sections without intercept."""
    T = len(Re)
    betas = np.linalg.lstsq(np.column_stack([np.ones(T), F]), Re, rcond=None)[0][1:].T
    lam_t = np.linalg.lstsq(betas, Re.T, rcond=None)[0].T
    return lam_t.mean(axis=0), lam_t.std(axis=0, ddof=1) / np.sqrt(T)
```

De functie `linear_sdf_gmm` geeft $\hat{\mathbf{b}}$, de premies en ofwel $J$ ofwel de
HJ-afstand terug. De volgende cel bouwt de economie en trekt de 1000 steekproeven.

```{code-cell} ipython3
mu_f = np.array([0.006, 0.002, 0.0035])
sd_f = np.array([0.045, 0.030, 0.030])
Sigma_f_true = np.array([[1.0, 0.3, -0.2], [0.3, 1.0, 0.0], [-0.2, 0.0, 1.0]]) * np.outer(sd_f, sd_f)
chol_f = np.linalg.cholesky(Sigma_f_true)
B_true = np.column_stack([1 + 0.1 * rng.standard_normal(25),
                          np.repeat(np.linspace(1.2, -0.2, 5), 5),
                          np.tile(np.linspace(-0.4, 0.8, 5), 5)])
gamma_u = 0.5 * rng.standard_normal(25)
sd_u, sd_eps = 0.03, 0.015
mu_R = B_true @ mu_f
b_ff3 = np.linalg.solve(Sigma_f_true, mu_f)


def draw_economy(T, unpriced_shock=True):
    """T months of FF3 factors, the unpriced shock u, and 25 test assets priced by FF3."""
    f = mu_f + rng.standard_normal((T, 3)) @ chol_f.T
    u = sd_u * rng.standard_normal(T)
    R = mu_R + (f - mu_f) @ B_true.T + sd_eps * rng.standard_normal((T, 25))
    if unpriced_shock:
        R = R + np.outer(u, gamma_u)
    return R, f, u


rows_a = []
for _ in range(1000):
    R, f, u = draw_economy(600)
    F4 = np.column_stack([f, f[:, 2] + u])                # Mkt, SMB, HML, g = HML + u
    est = linear_sdf_gmm(R, F4)
    lam_fm, se_fm = fama_macbeth_no_const(R, F4)
    rows_a.append({"t(b_HML)": est["b"][2] / est["se_b"][2], "t(b_g)": est["b"][3] / est["se_b"][3],
                   "t(lambda_g) GMM": est["lam"][3] / est["se_lam"][3], "t(lambda_g) FM": lam_fm[3] / se_fm[3],
                   "b_g": est["b"][3], "lambda_g FM (%)": 100 * lam_fm[3], "p_J": est["p_J"]})
sim_a = pd.DataFrame(rows_a)

print(f"ware b (FF3) = {b_ff3.round(2)}, ware b_g = 0, ware lambda_g = {100 * mu_f[2]:.2f}% per maand")
print(f"J verwerpt het ware model (5%) in {(sim_a['p_J'] < 0.05).mean():.1%} van de steekproeven")
t_cols = sim_a.filter(like="t(")
pd.DataFrame({"mediaan t": t_cols.median(), "fractie |t| > 1.96": (t_cols.abs() > 1.96).mean()}).round(3)
```

De tabel geeft per toets de mediane $t$-waarde en hoe vaak $|t| > 1{,}96$. De toets op $b_g$
verwerpt in ongeveer 6% van de steekproeven, dicht bij de 5% van de nulhypothese. De premie
$\lambda_g$ is met beide methoden in ongeveer de helft van de steekproeven significant. $J$
verwerpt het ware model in 4,4% van de gevallen en heeft dus het juiste niveau. De figuur
hieronder zet de twee verdelingen van $t$-waarden naast de gestreepte grenzen bij $\pm 1{,}96$.

```{code-cell} ipython3
:label: cel-sdf-unificatie-sim-b-lambda
:tags: [hide-input]

fig, ax = plt.subplots()
bins = np.linspace(-5, 7, 61)
ax.hist(sim_a["t(b_g)"], bins=bins, alpha=0.6, label="$t$ van $b_g$ (GMM)")
ax.hist(sim_a["t(lambda_g) FM"], bins=bins, alpha=0.6, label="$t$ van $\\lambda_g$ (Fama-MacBeth)")
for c in (-1.96, 1.96):
    ax.axvline(c, color="black", ls="--", lw=1)
ax.set_xlabel("$t$-waarde voor de overbodige factor $g$")
ax.set_ylabel("Aantal steekproeven")
ax.set_title("Een overbodige factor: premie vaak significant, gewicht in $m$ niet")
ax.legend()
plt.show()
```

:::{figure} #cel-sdf-unificatie-sim-b-lambda
:label: fig-sdf-unificatie-sim-b-lambda
:width: 90%

De factor $g$ voegt niets toe aan de ware SDF, maar correleert met HML. Zijn gewicht $b_g$ is
zelden significant, zoals onder de nulhypothese hoort, maar zijn premie $\lambda_g$ in de
helft van de steekproeven, omdat hij terecht de premie van HML erft.
:::

De $t$-waarden van $b_g$ liggen rond nul en die van $\lambda_g$ rond twee. De premie is
niet fout geschat, want 0,35% per maand is de ware waarde, maar ze beantwoordt een andere
vraag dan het gewicht. Dat ze maar in de helft van de steekproeven significant is, volgt
uit de rekensom achter [de standaardfout van 2%](#00-01-rendementen), want bij een
factorvolatiliteit van 4,2% is de standaardfout na vijftig jaar
$4{,}2/\sqrt{600} \approx 0{,}17\%$ per maand, de helft van de premie.

:::{note} Hoe groot is een HJ-afstand door toeval alleen?
:class: dropdown

Dezelfde economie zonder $u$ laat zien hoe groot een geschatte HJ-afstand wordt als het model
juist is. We schatten FF3 (waar) en het CAPM (fout) op 1000 steekproeven van twintig en van
vijftig jaar.

```{code-cell} ipython3
Sigma_R = B_true @ Sigma_f_true @ B_true.T + sd_eps**2 * np.eye(25)
W_pop = np.linalg.inv(Sigma_R + np.outer(mu_R, mu_R))


def population_hj(columns):
    """Population HJ distance of the linear SDF in the selected true factors."""
    C = (B_true @ Sigma_f_true)[:, columns]
    b = np.linalg.solve(C.T @ W_pop @ C, C.T @ W_pop @ mu_R)
    g = mu_R - C @ b
    return np.sqrt(max(g @ W_pop @ g, 0.0))


rows_b = []
for T in (240, 600):
    for _ in range(1000):
        R, f, _ = draw_economy(T, unpriced_shock=False)
        ff3_fit, capm_fit = linear_sdf_gmm(R, f, "hj"), linear_sdf_gmm(R, f[:, :1], "hj")
        rows_b.append({"T": T, "HJ FF3": ff3_fit["hj"], "HJ CAPM": capm_fit["hj"],
                       "p FF3": ff3_fit["p_hj"], "p CAPM": capm_fit["p_hj"]})
sim_b = pd.DataFrame(rows_b)

print(f"populatie: HJ FF3 = {population_hj([0, 1, 2]):.3f}, HJ CAPM = {population_hj([0]):.3f}")
sim_b.assign(reject_ff3=sim_b["p FF3"] < 0.05, reject_capm=sim_b["p CAPM"] < 0.05).groupby("T").agg(**{
    "mediaan HJ FF3 (waar)": ("HJ FF3", "median"), "mediaan HJ CAPM (fout)": ("HJ CAPM", "median"),
    "verwerpt FF3 (5%)": ("reject_ff3", "mean"), "verwerpt CAPM (5%)": ("reject_capm", "mean"),
}).round(3)
```

In de populatie is de afstand van het CAPM 0,14, bij 5% volatiliteit een alpha van 0,7% per
maand. Toch heeft het ware model na twintig jaar een mediane afstand van 0,31, dicht bij de
ruisbodem, en verwerpt de toets het CAPM dan maar in een op de zes steekproeven. Een
geschatte HJ-afstand hoort daarom naast de ruisbodem te staan, niet naast nul.
:::

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Cochranes handboek {cite}`Cochrane2005` voor GMM op lineaire SDF-modellen, en
Hansen en Jagannathan {cite}`HansenJagannathan1997` voor de afstand. Fama en French
{cite}`FamaFrench2015` vonden dat HML overbodig wordt zodra winstgevendheid en investeringen
in het model staan.

**Wat.** (1) $\hat{\mathbf{b}}$, $J$ en de HJ-afstand van CAPM, FF3 en FF3+UMD op 25
size/BM- en tien momentumportefeuilles. (2) De volatiliteit van de geschatte SDF naast de
Hansen-Jagannathan-grens, en (3) de overbodigheid van HML als uitspraak over $b$.

**Data hier.** Kenneth French Data Library via `hap.data.french`, maandelijks van 1963-07
tot en met 2026-07, als overrendementen. De bestandsnamen staan in de codecel.

**Verschil met het origineel.** Hansen en Jagannathan evalueerden andere modellen, en Fama en
French toetsten met GRS op andere sorteringen. Wij nemen alle factoren uit het
vijffactorbestand en schatten $\hat{\mathbf{S}}$ zonder autocorrelatietermen.

**Verwachte afwijking.** $J$ verwerpt het CAPM ($p < 0{,}01$), UMD halveert ongeveer de
FF3-prijsfout op momentum met $t(b) > 2$, en de HJ-afstand daalt naar FF3+UMD maar blijft
boven de ruisbodem. De FF3+UMD-SDF heeft een jaarvolatiliteit boven 0,8 maar onder de grens,
en in FF5+UMD is $\lambda_{\mathrm{HML}}$ significant en $b_{\mathrm{HML}}$ niet.
```

We laden de portefeuilles en de factoren en kijken eerst naar het gemiddelde overrendement
van de uiterste momentumdecielen.

```{code-cell} ipython3
ff5 = hap_data.french("F-F_Research_Data_5_Factors_2x3")
umd = hap_data.french("F-F_Momentum_Factor")["Mom"].rename("UMD")
rf = ff5["RF"]
size_bm = hap_data.french("25_Portfolios_5x5").sub(rf, axis=0)
momentum = hap_data.french("10_Portfolios_Prior_12_2").sub(rf, axis=0)
momentum.columns = [f"MOM {c}" for c in momentum.columns]

panel = (size_bm.join(momentum, how="inner")
         .join(ff5.drop(columns="RF"), how="inner").join(umd, how="inner")
         .loc["1963-07":"2026-07"])
assert panel.notna().all().all()
test_25, test_10 = list(size_bm.columns), list(momentum.columns)
test_35 = test_25 + test_10
models = {"CAPM": ["Mkt-RF"], "FF3": ["Mkt-RF", "SMB", "HML"], "FF3+UMD": ["Mkt-RF", "SMB", "HML", "UMD"]}
T_obs = len(panel)

mom_stats = hap.stats.summary_stats(panel[[test_10[0], test_10[-1]]])[["mean", "se_mean"]].astype(float) * 100
print(f"{panel.index[0]:%Y-%m} t/m {panel.index[-1]:%Y-%m}: T = {T_obs}, N = {len(test_35)}; "
      f"ruisbodem sqrt((N-K)/T) = {np.sqrt((35 - 1) / T_obs):.3f} (K = 1) tot {np.sqrt((35 - 4) / T_obs):.3f} (K = 4)")
mom_stats.rename(columns={"mean": "gem. overrendement (% p.m.)", "se_mean": "SE (% p.m.)"}).round(3)
```

De verliezers- en winnaarsdecielen verschillen ruim een procentpunt per maand, met
standaardfouten van een kwart tot een derde procentpunt. Het momentumverschil is daarmee een
van de weinige gemiddelden in de cross-sectie die de meetonzekerheid overleven. De ruisbodem
ligt voor deze 35 portefeuilles tussen 0,20 en 0,21, afhankelijk van het aantal factoren.

### (1) SDF-schattingen, $J$-toets en HJ-afstand

De eerste tabel schat elk model op de 25 size/BM-portefeuilles alleen en op alle 35, met
$J$, de HJ-afstand en de gemiddelde absolute prijsfout.

```{code-cell} ipython3
fits, summary_rows = {}, {}
for tests_label, tests in {"25 size/BM": test_25, "25 size/BM + 10 momentum": test_35}.items():
    Re = panel[tests].to_numpy()
    for name, cols in models.items():
        F = panel[cols].to_numpy()
        eff, hj = linear_sdf_gmm(Re, F), linear_sdf_gmm(Re, F, "hj")
        fits[(tests_label, name)] = eff
        row = {"J": eff["J"], "df": len(tests) - len(cols), "p(J)": eff["p_J"],
               "HJ-afstand": hj["hj"], "p(HJ)": hj["p_hj"],
               "gem. |fout| 25 (% p.m.)": 100 * np.abs(hj["g"][:25]).mean()}
        if len(tests) == 35:
            row["gem. |fout| 10 mom. (% p.m.)"] = 100 * np.abs(hj["g"][25:]).mean()
        summary_rows[(tests_label, name)] = row
pd.DataFrame(summary_rows).T.round(3)
```

Op alle 35 portefeuilles verwerpt $J$ elk model, en de HJ-afstanden dalen maar van 0,41
naar 0,36, zodat ze dicht bij elkaar en ruim boven de ruisbodem liggen. Op de 25
portefeuilles alleen laat $J$ FF3+UMD nog met $p = 0{,}02$ door, omdat de tien
momentumportefeuilles de toets strenger maken. Dat $J$ ook FF3 op de 25 portefeuilles
alleen verwerpt, komt door de fout in de hoek klein-groei uit [](#04-18-fama-french).

FF3 brengt de prijsfout op de 25 size/BM-portefeuilles terug tot ruim een tiende
procentpunt per maand. Op de momentumportefeuilles is de fout ruim twee keer zo groot, en
zelfs groter dan onder het CAPM. Winnaars hebben namelijk een negatieve HML-lading, zoals
de derde oefening van [](#04-18-fama-french) laat zien, zodat HML hun voorspelde rendement
verlaagt. De tweede tabel geeft per model de gewichten $b$, de premies $\lambda$ en het
gemiddelde van elke factor.

```{code-cell} ipython3
b_rows = {}
for name, cols in models.items():
    est = fits[("25 size/BM + 10 momentum", name)]
    for j, col in enumerate(cols):
        b_rows[(name, col)] = {"b": est["b"][j], "t(b)": est["b"][j] / est["se_b"][j],
                               "lambda (% p.m.)": 100 * est["lam"][j], "t(lambda)": est["lam"][j] / est["se_lam"][j],
                               "gem. factor (% p.m.)": 100 * panel[col].mean()}
pd.DataFrame(b_rows).T.round(2)
```

UMD halveert de prijsfout op de momentumportefeuilles, met een $t$-waarde van 4,6 voor zijn
$b$. De premies liggen meestal dicht bij het gemiddelde van de factor, zoals uit
[](#thm-fama-french-sdf) volgt voor verhandelde factoren. SMB in FF3+UMD is de uitzondering,
met een premie van 0,32% tegen een gemiddelde van 0,19% per maand.

### (2) De geschatte SDF en de Hansen-Jagannathan-grens

De geschatte SDF $\hat m_t = 1 - \hat{\mathbf{b}}'(\mathbf{f}_t - \bar{\mathbf{f}})$ is een
portefeuille van de factoren. Als het model de gemiddelden van verhandelde factoren precies
waardeert, is $\hat{\mathbf{b}} = \boldsymbol{\Sigma}_f^{-1}\E[\mathbf{f}]$, de
tangentgewichten uit [](#eq-markowitz-tangent). Dan is $\sigma(\hat m)/\E[\hat m]$ de
maximale Sharpe-ratio van de factoren, en haalt de SDF de Hansen-Jagannathan-grens met
gelijkheid. Omdat GMM ook de testactiva moet waarderen, geldt dat hier maar bij
benadering, en de tabel zet alle maten met $\sqrt{12}$ op jaarbasis.

```{code-cell} ipython3
mkt = panel["Mkt-RF"]
all_returns = panel[test_35 + models["FF3+UMD"]].to_numpy()
mean_all = all_returns.mean(axis=0)
sr_max_35 = np.sqrt(12 * mean_all @ np.linalg.solve(np.cov(all_returns, rowvar=False, bias=True), mean_all))

bound_rows = {}
for name, cols in models.items():
    F = panel[cols].to_numpy()
    mu = F.mean(axis=0)
    bound_rows[f"factor-SDF {name}"] = {
        "sigma(m)/E[m] per jaar": np.sqrt(12) * fits[("25 size/BM + 10 momentum", name)]["sd_m"],
        "max. Sharpe van de factoren per jaar": np.sqrt(12 * mu @ np.linalg.solve(np.cov(F, rowvar=False, bias=True).reshape(len(cols), len(cols)), mu)),
    }
bound_rows["Sharpe-ratio markt"] = {"sigma(m)/E[m] per jaar": np.nan,
                                    "max. Sharpe van de factoren per jaar": np.sqrt(12) * mkt.mean() / mkt.std(ddof=0)}
sd_m_consumption = 10 * 0.036                          # gamma * sigma(dc), see 03_13
bound_rows["consumptie-SDF, gamma = 10, sigma(dc) = 3,6%"] = {"sigma(m)/E[m] per jaar": sd_m_consumption,
                                                              "max. Sharpe van de factoren per jaar": np.nan}
bound_rows["HJ-grens, 35 portefeuilles + 4 factoren"] = {
    "sigma(m)/E[m] per jaar": np.nan, "max. Sharpe van de factoren per jaar": sr_max_35}
b_umd = fits[("25 size/BM + 10 momentum", "FF3+UMD")]["b"]
F_umd = panel[models["FF3+UMD"]]
m_hat = 1 - (F_umd - F_umd.mean()) @ b_umd
print(f"maanden met m-dak < 0 (FF3+UMD): {(m_hat < 0).mean():.1%}; min = {m_hat.min():.2f} in {m_hat.idxmin():%Y-%m}, "
      f"max = {m_hat.max():.2f} in {m_hat.idxmax():%Y-%m}")
pd.DataFrame(bound_rows).T.round(3)
```

De tabel zet de volatiliteit van elke factor-SDF naast de maximale Sharpe-ratio van
dezelfde factoren, en de twee kolommen liggen dicht bij elkaar. De FF3+UMD-SDF schommelt
met 1,04 per jaar ongeveer honderd procent. De consumptie-SDF met $\gamma = 10$ haalt met
0,36 niet eens de Sharpe-ratio van de markt. Links in de figuur staan de balken naast de
gestreepte grens, en rechts volgt de geschatte SDF door de tijd, met zijn pieken en de
maanden onder nul.

```{code-cell} ipython3
:label: cel-sdf-unificatie-mhat
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw={"width_ratios": [1, 1.6]})
labels = ["consumptie\n$\\gamma = 10$", "markt\n(Sharpe)", "SDF\nCAPM", "SDF\nFF3", "SDF\nFF3+UMD"]
values = [sd_m_consumption, np.sqrt(12) * mkt.mean() / mkt.std(ddof=0)] + [
    np.sqrt(12) * fits[("25 size/BM + 10 momentum", n)]["sd_m"] for n in models]
axes[0].bar(labels, values, color=[hap.plotting.COLORS[7]] * 2 + [hap.plotting.COLORS[0]] * 3)
axes[0].axhline(sr_max_35, color=hap.plotting.COLORS[1], ls="--", lw=1.4,
                label="HJ-grens, 35 portefeuilles (binnen de steekproef)")
axes[0].set_ylabel("$\\sigma(m)/E[m]$ of Sharpe-ratio, per jaar")
axes[0].set_xlabel("Kandidaat")
axes[0].set_title("Hoe volatiel moet $m$ zijn?")
axes[0].legend(loc="upper left")

axes[1].plot(m_hat.index, m_hat, lw=0.8, color=hap.plotting.COLORS[0])
axes[1].axhline(0, color="black", lw=0.8)
hap.plotting.recession_shading(axes[1])
axes[1].set_xlabel("Jaar")
axes[1].set_ylabel("$\\hat m_t$")
axes[1].set_title("De geschatte SDF van FF3+UMD, met NBER-recessies")
fig.tight_layout()
plt.show()
```

:::{figure} #cel-sdf-unificatie-mhat
:label: fig-sdf-unificatie-mhat
:width: 100%

Links haalt de consumptie-SDF met $\gamma = 10$ de Sharpe-ratio van de markt niet
([](#03-13-equity-premium-puzzle)), terwijl de factor-SDF's die halen, FF3 en FF3+UMD ruim. Ze blijven onder
de grens van de 35 portefeuilles, die door overfitting overschat is. Rechts piekt de
geschatte SDF in maanden waarin de markt valt of momentum crasht, en is ze een enkele keer
negatief.
:::

Het contrast met de consumptie-SDF is groot, want die haalde de Sharpe-grens van de markt
pas bij $\gamma = 15$, met een rente van dertig procent
([](#03-13-equity-premium-puzzle)). Een SDF uit vier factorportefeuilles haalt die grens
moeiteloos, maar niemand kan zeggen welk risico of welke voorkeur erachter zit. Het
maximum valt in januari 2001, bij een momentumcrash, en in januari 1976 is de SDF
negatief. Een negatieve SDF waardeert de testactiva goed, maar geeft sommige opties op de
factoren een negatieve prijs ([](#rem-apt-no-arbitrage-sdf)).

### (3) $b$ tegenover $\lambda$: is HML overbodig?

De laatste tabel voegt RMW en CMA toe en zet het gewicht $b$ van elke factor naast zijn
premie volgens GMM en volgens Fama-MacBeth.

```{code-cell} ipython3
Re35 = panel[test_35].to_numpy()
lambda_rows = {}
for name, cols in {"FF3+UMD": models["FF3+UMD"],
                   "FF5+UMD": ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "UMD"]}.items():
    F = panel[cols].to_numpy()
    est = linear_sdf_gmm(Re35, F)
    lam_fm, se_fm = fama_macbeth_no_const(Re35, F)
    for j, col in enumerate(cols):
        lambda_rows[(name, col)] = {"b": est["b"][j], "t(b)": est["b"][j] / est["se_b"][j],
                                    "lambda GMM (% p.m.)": 100 * est["lam"][j],
                                    "t(lambda) GMM": est["lam"][j] / est["se_lam"][j],
                                    "lambda FM (% p.m.)": 100 * lam_fm[j], "t(lambda) FM": lam_fm[j] / se_fm[j]}
    lambda_rows[(name, "J (p)")] = {"b": est["J"], "t(b)": est["p_J"]}
pd.DataFrame(lambda_rows).T.round(2)
```

In FF3+UMD hebben markt, HML en UMD een significante $b$ én $\lambda$, terwijl SMB geen
significante $b$ heeft. Met RMW en CMA erbij gebeurt met HML wat
[](#prop-sdf-unificatie-b-lambda) voorspelt. De premie $\lambda_{\mathrm{HML}}$ blijft
significant met GMM en met Fama-MacBeth, maar het gewicht $b_{\mathrm{HML}}$ niet.

HML hangt dus samen met de SDF, maar voegt gegeven RMW en CMA weinig toe, en dat is de
overbodigheid van Fama en French uitgedrukt in $b$. Het gewicht verschuift naar RMW
($t = 3{,}0$) en, onnauwkeurig, naar CMA. Een onderzoeker die alleen de Fama-MacBeth-kolom
las, zou het omgekeerde concluderen, namelijk dat HML nodig is en CMA met een premie van nul
overbodig. De tabel hieronder zet de verwachtingen uit het replicatieblok naast de
uitkomsten.

| verwachting | hier |
|---|---|
| $J$ verwerpt het CAPM, $p < 0{,}01$ | $p(J) = 0{,}00$ op 25 en op 35 portefeuilles |
| UMD halveert de FF3-fout op momentum, $t(b) > 2$ | van 0,264 naar 0,124% per maand, $t(b) = 4{,}59$ |
| HJ-afstand daalt en blijft boven de ruisbodem van 0,2 | 0,410, 0,394 en 0,361 |
| SDF-volatiliteit FF3+UMD boven 0,8 en onder de grens | 1,036 per jaar, grens 1,738 |
| FF5+UMD: $\lambda_{\mathrm{HML}}$ significant, $b_{\mathrm{HML}}$ niet | $t(\lambda) = 3{,}08$ en $2{,}72$, $t(b) = 0{,}68$ |

**Geslaagd.** Alle vijf verwachtingen uit het replicatieblok komen uit, en geen teken draait
om. De replicatie bevestigt de rangorde van de modellen en laat ook zien hoe dicht hun
afstanden bij elkaar liggen.

## Wat er brak, en wat daarna kwam

**Wat het raamwerk verklaart.** Alles wat in dit boek tot hier gebeurde, past in één taal.
CAPM, consumptie-SDF, APT en Fama-French zijn uitspraken over $m$. Frontier, bèta en SDF
zijn drie vormen van dezelfde meetkunde, en GRS, Fama-MacBeth en de Euler-GMM zijn
momentvoorwaarden $\E[mR^e] = 0$ met een andere weging. Het raamwerk leverde gereedschap
dat bleef, namelijk de HJ-grens voor economische modellen, de HJ-afstand om foute modellen
te rangschikken, en $b$ tegenover $\lambda$ om te bepalen welke factor nodig is.

**Waar het breekt.** Het raamwerk zegt niet welke $m$ de juiste is. Op onze 35 portefeuilles
verwerpt $J$ zelfs FF3+UMD, en de HJ-afstanden van drie heel verschillende modellen liggen
dicht bij elkaar en ruim boven de ruisbodem. De factor-SDF die de activa het best waardeert,
schommelt ongeveer honderd procent per jaar en heeft geen economische interpretatie. De
consumptie-SDF heeft die interpretatie wel, maar haalt de grens niet. Prijzen verklaren en
prijzen begrijpen zijn zo twee verschillende projecten geworden.

**Risico of vergissing?** De SDF-taal is neutraal, en daarin zit zowel de kracht als de
beperking ervan. In de Chicago-lezing is $\hat m_t$ hoog in recessies en crashes, zodat
markt, value en momentum beloningen zijn voor risico in slechte tijden. In de Yale-lezing
is een SDF niets meer dan een gewichtenvector die de gemeten gemiddelden reproduceert. Als
beleggers systematisch dezelfde vergissing maken over groei, bestaat er ook een lineaire
$m$ die de activa dan even goed waardeert, met dezelfde covarianties met de factoren.
Beide lezingen voorspellen dezelfde $J$ en HJ-afstand, en alleen een onafhankelijke meting
van de marginale waarde van geld zou ze scheiden. Voor een belegger blijft de vraag die
Pedro Santa-Clara in zijn terugblik stelt ([](#00-00-setup)): draagt de koper van de
tangentportefeuille een risico met een premie, of denkt hij iets te weten wat de prijs
niet weet?

**Wat er daarna kwam.** Drie onderzoeksprogramma's probeerden een economische $m$ te bouwen
die volatiel genoeg is om de Hansen-Jagannathan-grens te halen zonder de rente te laten
ontsporen: gewoontevorming, langetermijnrisico en rampen, in [](#05-27-drie-antwoorden).

## Oefeningen

:::{exercise}
:label: ex-sdf-unificatie-1

**Instap: welke SDF gebruikt de markt?** Neem het toy-voorbeeld. Een put op het aandeel met
uitoefenprijs 1 heeft payoff $(0;\ 0;\ 0{,}5)$.

1. Bereken de prijs van de put met $x^*$ en met $m = x^* + k\varepsilon$, en geef het interval
   van prijzen dat past bij strikt positieve SDF's.
2. Bereken $R^{e*}$ uit [](#eq-sdf-unificatie-rstar) en controleer
   $\E[R^e] = \E[R^{e*}R^e]$ voor het overrendement van het aandeel.
:::

:::{solution} ex-sdf-unificatie-1
:class: dropdown

**(1)** De put keert alleen in toestand 3 uit, dus $\E[mx] = \tfrac14 \cdot 0{,}5\,(1{,}15 + k) = 0{,}125\,(1{,}15 + k)$.
Bij $x^*$ is dat $0{,}14375$, en voor $k \in (-0{,}75;\ 0{,}95)$ ligt de prijs tussen
$0{,}05$ en $0{,}2625$.

**(2)** Met één risicovol activum is $\underline{R}^e$ de lijn door $R^e_a$. De projectie van
de constante daarop is $R^{e*} = (\E[R^e_a]/\E[(R^e_a)^2])\,R^e_a$.

```{code-cell} ipython3
put = np.array([0.0, 0.0, 0.5])
k_bounds = np.array([-0.75, 0.95])
Re_a = R_a - R_f
Re_star = E(Re_a) / E(Re_a**2) * Re_a
put_bounds = [E((x_star + k * eps) * put) for k in k_bounds]
print(f"prijs put met x*: {E(x_star * put):.5f}; interval bij positieve m: ({put_bounds[0]:.4f}, {put_bounds[1]:.4f})")
print(f"E[R^e] = {E(Re_a):.5f}, E[R^e* R^e] = {E(Re_star * Re_a):.5f}")
```

De code bevestigt beide antwoorden. De prijzen leggen $x^*$ en de frontier vast, maar de prijs
van alles buiten de payoff-ruimte hangt af van een keuze van $m$ die de data niet maken. Een
prijsmodel is precies zo'n keuze.
:::

:::{exercise}
:label: ex-sdf-unificatie-2

**Afleiding en uitbreiding: een conditioneel CAPM.** Neem als signaal $z_t$ de log
dividend-prijsratio `dp` uit `hap.data.goyal_welch("monthly")`, een maand vertraagd en
gestandaardiseerd. Gebruik de 35 portefeuilles van de replicatie over 1963-07 tot en met 2025-12.

1. Schrijf $m_{t+1} = a_t - b_t R^e_{m,t+1}$ met $a_t = a_0 + a_1 z_t$ en $b_t = b_0 + b_1 z_t$
   als onvoorwaardelijk lineair model. Welke momentvoorwaarden komen erbij als ook de
   geschaalde payoffs $z_tR^e_{t+1}$ testactiva worden?
2. Schat het met `linear_sdf_gmm` en vergelijk $J$, HJ-afstand en prijsfouten met CAPM en FF3.
3. Is $b_1$ significant?
:::

:::{solution} ex-sdf-unificatie-2
:class: dropdown

**(1)** Uitschrijven geeft $m_{t+1} = a_0 + a_1 z_t - b_0R^e_{m,t+1} - b_1 z_tR^e_{m,t+1}$,
een lineair model met factoren $R^e_m$, $z_t$ en $z_tR^e_{m,t+1}$. Met de geschaalde
payoffs als testactiva komen de momenten $\E[m_{t+1}z_tR^e_{t+1}] = 0$ uit de note erbij,
maar de code hieronder houdt de 35 portefeuilles als testactiva.

```{code-cell} ipython3
dp = hap_data.goyal_welch("monthly")["dp"]
z = dp.shift(1).reindex(panel.index).loc[:"2025-12"]
z = (z - z.mean()) / z.std()
sub = panel.loc[z.index]
cond_factors = pd.DataFrame({"Mkt-RF": sub["Mkt-RF"], "z": z, "z x Mkt-RF": z * sub["Mkt-RF"]})
candidates = {"CAPM": sub[["Mkt-RF"]], "conditioneel CAPM": cond_factors, "FF3": sub[models["FF3"]]}
rows_ex2 = {}
for name, frame in candidates.items():
    eff, hj = linear_sdf_gmm(sub[test_35].to_numpy(), frame.to_numpy()), linear_sdf_gmm(sub[test_35].to_numpy(), frame.to_numpy(), "hj")
    rows_ex2[name] = {"J": eff["J"], "p(J)": eff["p_J"], "HJ": hj["hj"], "gem. |fout| (% p.m.)": 100 * np.abs(hj["g"]).mean(),
                      "t(b) laatste factor": eff["b"][-1] / eff["se_b"][-1]}
pd.DataFrame(rows_ex2).T.round(3)
```

**(2)** Het conditionele CAPM verlaagt de gemiddelde prijsfout nauwelijks en blijft ver boven FF3, terwijl $J$ het nog steeds verwerpt. Leerzaam is het contrast tussen de twee maten, want $J$
daalt van 127 naar 55, terwijl de HJ-afstand maar een paar procent daalt. Extra ruisige
factoren blazen $\hat{\mathbf{S}}$ op en verlagen zo $J$, maar niet $\delta$. **(3)** Ja, $b_1$
heeft een $t$-waarde van $2{,}3$. Een conditioneel model is in de SDF-taal dus een
onvoorwaardelijk model met meer factoren, en hoort met dezelfde meetlat te worden beoordeeld
als elk ander factormodel.
:::

:::{exercise}
:label: ex-sdf-unificatie-3

**Uitbreiding van de replicatie: hoe zeker is een cross-sectionele $R^2$?** Kan, Robotti en
Shanken {cite}`KanRobottiShanken2013` waarschuwen dat grote verschillen in cross-sectionele
$R^2$ vaak niet significant zijn. Ga dat na voor de modellen van de replicatie.

1. Bereken voor het CAPM, FF3 en FF3+UMD op de 35 portefeuilles de OLS-$R^2$ van gemiddelde
   overrendementen op bèta's uit de volle steekproef, met intercept.
2. Trek 500 bootstrapsteekproeven van maanden (met teruglegging), herhaal (1) per steekproef,
   en rapporteer het 90%-interval van $R^2_{\mathrm{FF3+UMD}} - R^2_{\mathrm{FF3}}$ en van
   $R^2_{\mathrm{FF3}} - R^2_{\mathrm{CAPM}}$.
3. Vergelijk met de conclusie uit de HJ-afstanden.
:::

:::{solution} ex-sdf-unificatie-3
:class: dropdown

```{code-cell} ipython3
def cs_r2(Re, F):
    """Cross-sectional OLS R^2 of mean excess returns on full-sample betas, with intercept."""
    T = len(Re)
    betas = np.linalg.lstsq(np.column_stack([np.ones(T), F]), Re, rcond=None)[0][1:].T
    Z = np.column_stack([np.ones(Re.shape[1]), betas])
    means = Re.mean(axis=0)
    resid = means - Z @ np.linalg.lstsq(Z, means, rcond=None)[0]
    return 1 - resid.var() / means.var()


factor_arrays = {name: panel[cols].to_numpy() for name, cols in models.items()}
point = {name: cs_r2(Re35, F) for name, F in factor_arrays.items()}
boot = []
for _ in range(500):
    idx = rng.integers(0, T_obs, T_obs)
    boot.append({name: cs_r2(Re35[idx], F[idx]) for name, F in factor_arrays.items()})
boot = pd.DataFrame(boot)
diffs = {"FF3+UMD - FF3": boot["FF3+UMD"] - boot["FF3"], "FF3 - CAPM": boot["FF3"] - boot["CAPM"]}
print("R2:", {k: round(v, 3) for k, v in point.items()})
pd.DataFrame({k: v.quantile([0.05, 0.5, 0.95]) for k, v in diffs.items()}).T.round(3)
```

De bootstrap schat de bèta's per steekproef opnieuw, als ruwe versie van de inferentie van
Kan, Robotti en Shanken. De $R^2$ stijgt van 0,11 via 0,50 naar 0,76, en beide verschillen
zijn in meer dan 95% van de steekproeven positief. Het interval is wel breed, zodat de 26
procentpunt die UMD in de puntschatting toevoegt, verenigbaar is met acht en met ruim
veertig.

De HJ-afstanden gaven dezelfde rangorde, maar lagen dicht bij elkaar. Een hoge $R^2$ met vrij
intercept kan bovendien samengaan met verkeerde premies ([](#prop-fama-french-mechanisch)).
Een rangorde van modellen is dus pas een resultaat als ze de steekproefonzekerheid overleeft.
:::
