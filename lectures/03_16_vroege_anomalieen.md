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

(03-16-vroege-anomalieen)=

# Basu, Banz en Rosenberg

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1960–1993, met het zwaartepunt tussen 1977 en 1985.

**Wat we al weten.** [Het CAPM](#02-08-capm) zegt dat alleen bèta het verwachte
rendement bepaalt. De eerste toetsen vonden een security market line die te vlak
was, maar wel positief. [Shiller](#03-15-shiller-excess-volatility) liet daarna
zien dat de markt als geheel meer beweegt dan haar dividenden rechtvaardigen. Die
barst zat in de tijdreeks van één index.

**Welke vraag staat open.** Voorspellen eenvoudige kenmerken van een aandeel, zoals
de winst-koersverhouding, de marktwaarde of de boekwaarde, het gemiddelde rendement
beter dan bèta?
```

## Overzicht

Voorspellen kenmerken als de winst-koersverhouding, de marktwaarde en de boekwaarde
het rendement beter dan bèta? In de steekproeven van de eerste onderzoekers wel:
goedkope en kleine aandelen hadden een positieve CAPM-*alpha* (het deel van het
gemiddelde rendement dat bèta niet verklaart). Maar hetzelfde patroon past bij een
gemist risico, bij een vergissing van de markt en bij toeval.

In deze lecture:

- rekenen we met vijf aandelen na hoe een sortering een alpha oplevert;

- laten we zien dat een sortering een regressie zonder vorm is, en een
  Fama-MacBeth-helling op een kenmerk een long-short-portefeuille;

- bewijzen we met Berk dat marktwaarde het verwachte rendement voorspelt, ook als
  elke prijs klopt, en hoe een gezocht kenmerk een grote $t$-waarde maakt;

- simuleren we een echte premie die onzichtbaar blijft, en een zichtbare premie die
  niet bestaat;

- repliceren we de CAPM-alpha's van E/P-, B/M- en size-portefeuilles in de
  oorspronkelijke steekproeven en daarna, en het januari-effect van Keim.

Tussen 1977 en 1985 verschenen vier artikelen die telkens één kenmerk naast bèta
legden. Zo nam {cite:t}`Basu1977` de koers-winstverhouding, {cite:t}`Banz1981` de
marktwaarde en {cite:t}`Reinganum1981` beide tegelijk. Daarna namen
{cite:t}`RosenbergReidLanstein1985` de verhouding van boekwaarde tot marktwaarde, na
een voorloper van {cite:t}`Stattman1980`. Ook vond {cite:t}`Keim1983` een groot deel
van het size-effect in januari, en {cite:t}`Bhandari1988` hetzelfde patroon voor de
schuldgraad. Het woord *anomalie* (een regelmaat in gemiddelde rendementen die het
heersende model niet verklaart) kreeg in deze jaren zijn betekenis. Aan het eind van
het tijdvak kwamen de eerste waarschuwingen tegen datamining
{cite}`LoMacKinlay1990,Black1993`.

Deze artikelen definiëren het tijdvak omdat ze het antwoord op de vraag theorie of
feit verschoven. Het CAPM bleef een getoetste theorie, maar nu met een lijst
afwijkingen: feiten zonder een model dat ze vooraf had voorspeld.

## Intuïtie: waarom zou dit waar zijn?

In juli 1960 vroeg S. Francis Nicholson analisten en zakenmensen welke aandelen het
over drie tot tien jaar beter zouden doen: die met een koers boven 25 keer de winst,
of die onder 12 keer {cite}`Nicholson1960`. Bijna tien tegen één verwachtten ze meer
van de dure aandelen. Meer stelde zijn enquête niet vast. De latere literatuur citeert
Nicholson daarnaast als vroeg bewijs dat juist de goedkope het beter deden. Zijn
tabellen hebben we niet kunnen inzien, dus die uitkomst nemen we niet over. Er was
toen nog geen model om beter aan te meten. Zeventien jaar later stelde Basu dezelfde
vraag, nu met bèta's.

Waarom zou een goedkoop aandeel meer opleveren? Het eerste verhaal is een rekensom.
De koers is de contante waarde van de toekomstige kasstromen. Van twee bedrijven met
dezelfde verwachte winst is het riskantere goedkoper, *omdat* beleggers er meer
rendement voor eisen. Een lage koers ten opzichte van de winst is dan een hoge
discontovoet. Ziet het CAPM dat risico niet, dan verschijnt het als alpha.

Het tweede verhaal is psychologie. Beleggers extrapoleren: bedrijven met slechte
recente winsten worden te somber gewaardeerd, bedrijven met mooie groeiverhalen te
optimistisch. De koers-winstverhouding meet dan de vergissing, en het hogere
rendement van goedkope aandelen is de trage correctie. De verwachting van Nicholsons
analisten past in dat beeld, net als het werk van De Bondt en Thaler in
[](#04-23-behavioral).

Beide verhalen voorspellen hetzelfde feit, dus sorteren kan ze niet scheiden. Het kan
hooguit laten zien *dat* er iets is, en zelfs dat is onzeker, want gemiddelde
rendementen zijn slecht gemeten. We verwachten dus drie dingen:

1. Goedkope en kleine aandelen hebben een positieve CAPM-alpha, ook als hun bèta niet
   hoger is.

2. Een kenmerk dat met de koers is berekend, voorspelt het verwachte rendement, ook
   als elke prijs klopt.

3. Een kenmerk dat in de data is gezocht, heeft in die data een grote $t$-waarde en
   daarbuiten niet.

## Toy-voorbeeld: vijf aandelen, twee portefeuilles

Het toy-voorbeeld laat zien hoe een sortering op E/P een alpha oplevert. We laden
eerst de pakketten voor de hele lecture.

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

**Opzet.** Vijf aandelen, één periode. Van elk kennen we de bèta, de
winst-koersverhouding E/P (winst gedeeld door koers, het omgekeerde van de
koers-winstverhouding), de marktwaarde ME aan het begin van de periode en het
gerealiseerde netto rendement $r$. De risicovrije rente is $R^{f} = 1\%$. Het subscript $m$ staat voor de
marktportefeuille, niet voor de SDF.

| aandeel | $\beta_{i,m}$ | E/P | ME | $r$ |
|---|---|---|---|---|
| A | 1,10 | 3% | 500 | 5,0% |
| B | 1,00 | 5% | 250 | 6,1% |
| C | 0,90 | 6% | 125 | 7,0% |
| D | 0,80 | 9% | 75 | 8,0% |
| E | 0,55 | 12% | 50 | 10,0% |

**Het recept.** De gerealiseerde Jensen-alpha over één periode is het excess
rendement min bèta maal het excess marktrendement:
$\alpha_i = (r_i - R^{f}) - \beta_{i,m}(r_m - R^{f})$, het CAPM uit [](#02-08-capm)
met een restterm.

**Stap 1, de markt.** De marktgewichten zijn ME gedeeld door 1000:
$(0{,}50;\ 0{,}25;\ 0{,}125;\ 0{,}075;\ 0{,}05)$. Het marktrendement is
$0{,}50 \cdot 5 + 0{,}25 \cdot 6{,}1 + 0{,}125 \cdot 7 + 0{,}075 \cdot 8 + 0{,}05
\cdot 10 = 6{,}0\%$, het excess marktrendement dus $5{,}0\%$. De marktgewogen bèta
is $0{,}55 + 0{,}25 + 0{,}1125 + 0{,}06 + 0{,}0275 = 1{,}000$, zoals het hoort.

**Stap 2, de alpha per aandeel.** $\alpha_A = 4{,}0 - 1{,}10 \cdot 5 = -1{,}50\%$,
$\alpha_B = 5{,}1 - 5{,}00 = 0{,}10\%$, $\alpha_C = 6{,}0 - 4{,}50 = 1{,}50\%$,
$\alpha_D = 7{,}0 - 4{,}00 = 3{,}00\%$ en $\alpha_E = 9{,}0 - 2{,}75 = 6{,}25\%$.
Marktgewogen tellen ze op tot nul: de markt heeft ten opzichte van zichzelf geen
alpha.

**Stap 3, de sortering.** Portefeuille H bevat de twee aandelen met de hoogste E/P
(D en E), portefeuille L de twee met de laagste (A en B), elk gelijkgewogen. C valt
tussen de breekpunten. De long-short-portefeuille H − L koopt H en verkoopt L short,
en kost dus niets.

| | bèta | excess rendement | CAPM-voorspelling | alpha |
|---|---|---|---|---|
| H = (D, E) | 0,675 | 8,00% | 3,375% | 4,625% |
| L = (A, B) | 1,050 | 4,55% | 5,250% | −0,700% |
| H − L | −0,375 | 3,45% | −1,875% | 5,325% |

**Stap 4, de alpha van H − L.** Het excess rendement van H − L is
$8{,}00 - 4{,}55 = 3{,}45\%$, haar bèta $0{,}675 - 1{,}050 = -0{,}375$. Haar alpha is
$3{,}45 - (-0{,}375)(5{,}0) = 5{,}325\%$, het verschil van de twee alpha's. Het ruwe
rendementsverschil van 3,45% onderschat de alpha, want het CAPM voorspelt voor H − L een negatief
rendement: de goedkope aandelen hebben een lagere bèta.

De code rekent hetzelfde na en kijkt welke aandelen een sortering op marktwaarde
kiest.

```{code-cell} ipython3
:label: cel-vroege-anomalieen-toy

toy = pd.DataFrame(
    {"beta": [1.10, 1.00, 0.90, 0.80, 0.55],
     "E/P": [0.03, 0.05, 0.06, 0.09, 0.12],
     "ME": [500.0, 250.0, 125.0, 75.0, 50.0],
     "r": [0.050, 0.061, 0.070, 0.080, 0.100]},
    index=list("ABCDE"),
)
rf_toy = 0.01
weights = toy["ME"] / toy["ME"].sum()
r_market = weights @ toy["r"]
toy["alpha"] = toy["r"] - rf_toy - toy["beta"] * (r_market - rf_toy)

def toy_portfolio(stocks):
    """Equal-weighted beta, excess return, CAPM prediction and alpha."""
    g = toy.loc[stocks]
    beta, excess = g["beta"].mean(), g["r"].mean() - rf_toy
    return pd.Series({"bèta": beta, "excess": excess,
                      "CAPM": beta * (r_market - rf_toy), "alpha": g["alpha"].mean()})

high_ep, low_ep = toy.nlargest(2, "E/P").index, toy.nsmallest(2, "E/P").index
sorted_toy = pd.DataFrame({"H": toy_portfolio(high_ep), "L": toy_portfolio(low_ep)}).T
sorted_toy.loc["H - L"] = sorted_toy.loc["H"] - sorted_toy.loc["L"]
print("zelfde portefeuilles bij sortering op ME:", set(toy.nsmallest(2, "ME").index) == set(high_ep))
pd.DataFrame(
    {"met de hand": [0.06, 1.0, 0.0, 0.04625, -0.007, -0.375, 0.0345, 0.05325],
     "code": [r_market, weights @ toy["beta"], weights @ toy["alpha"], *sorted_toy["alpha"].iloc[:2],
              *sorted_toy.loc["H - L", ["bèta", "excess", "alpha"]]]},
    index=["marktrendement", "marktbèta", "marktgewogen alpha", "alpha H", "alpha L",
           "bèta H - L", "excess H - L", "alpha H - L"],
).round(5)
```

De code en de handberekening geven dezelfde getallen. Een sortering op marktwaarde
kiest dezelfde twee portefeuilles, want de goedkoopste aandelen zijn ook de kleinste.
Of dit een E/P- of een size-effect is, was de vraag van {cite:t}`Reinganum1981`. Wat
we nu weten: een sortering meet de alpha van een kenmerk, maar niet welk kenmerk het
werk doet. Of 5,3% toeval is, zegt één periode niet. Daarvoor is een tijdreeks nodig.

## Theorie

We leiden vier dingen af. Eerst is een portefeuillesortering een regressie zonder
vorm, met voor hoog min laag een Jensen-alpha en een eigen standaardfout. Dan
blijkt een Fama-MacBeth-helling op een kenmerk een long-short-portefeuille.
De kern volgt daarna: volgens Berk voorspelt marktwaarde het verwachte rendement
zodra verwachte rendementen verschillen. Tot slot laten we zien hoe een kenmerk dat
in de data is gezocht een grote $t$-waarde maakt.

### Opzet: sorteren als regressie zonder vorm

Een portefeuillesortering schat het verwachte rendement als functie van een
kenmerk, zonder die functie een vorm op te leggen. We schrijven $z_{i,t}$ voor een
kenmerk van aandeel $i$ dat op $t$ bekend is, zoals E/P, $\log \mathrm{ME}$ of B/M,
en $R^{e}_{i,t+1}$ voor het excess rendement daarna.

*Waarom zou dit waar zijn?* Een onderzoeker wil weten of aandelen met een hoge E/P
later meer opleveren. Hij zet de aandelen op volgorde van E/P, deelt de rij in tien
groepen en neemt per groep het gemiddelde rendement. Stijgt dat gemiddelde van groep
tot groep, dan stijgt het verwachte rendement met E/P, welke vorm het verband ook
heeft.

Laat $\mu(z) = \E[R^{e}_{i,t+1} \mid z_{i,t} = z]$ het verwachte excess rendement bij
kenmerk $z$ zijn, en $q_0 < q_1 < \dots < q_J$ de breekpunten, bijvoorbeeld de
decielen van $z_{i,t}$ op $t$. Met $N_{j,t}$ aandelen in vakje $j$ is het
gelijkgewogen rendement van portefeuille $j$

```{math}
:label: eq-vroege-anomalieen-sort
R^{e}_{j,t+1} = \frac{1}{N_{j,t}} \sum_{i:\ q_{j-1} < z_{i,t} \le q_j} R^{e}_{i,t+1},
\qquad
\E\!\left[R^{e}_{j,t+1}\right] = \E\!\left[\mu(z_{i,t}) \mid q_{j-1} < z_{i,t} \le q_j\right].
```

In woorden: portefeuille $j$ verdient gemiddeld de waarde van $\mu$ op vakje $j$, dus
het tijdgemiddelde schat $\mu$ vakje voor vakje, als een histogram. Meer vakjes geven
minder vertekening en meer ruis. Tien decielen kiezen voor weinig ruis. De prijs is
dat een effect bij de kleinste paar procent van de aandelen, zoals dat van Banz, over
het hele eerste deciel wordt uitgesmeerd.

### De alpha van een long-short-portefeuille

De alpha van hoog min laag zegt of een kenmerk iets toevoegt aan het CAPM. Haar
standaardfout is ongeveer de residuele volatiliteit gedeeld door $\sqrt{T}$.

*Waarom zou dit waar zijn?* Een belegger koopt de hoogste portefeuille en verkoopt de
laagste short. Levert dat meer op dan het verschil in bèta rechtvaardigt, dan voegt
het kenmerk iets toe. Hoe langer hij de positie volgt, hoe kleiner de toevalsfout in
zijn gemiddelde.

Laat $r^{\mathrm{LS}}_{t+1} = R^{e}_{J,t+1} - R^{e}_{1,t+1}$ het rendement zijn van de
hoogste min de laagste portefeuille. Over $T$ maanden schatten we

```{math}
:label: eq-vroege-anomalieen-ls
r^{\mathrm{LS}}_{t+1} = \alpha_{\mathrm{LS}} + \beta_{\mathrm{LS}}\, R^{e}_{m,t+1} + \varepsilon_{t+1}.
```

In woorden: hoog min laag verdient een alpha plus bèta maal het excess
marktrendement. Dit is de CAPM-regressie uit [](#eq-capm-tijdreeks) op één reeks.
Omdat OLS lineair is in de afhankelijke variabele, is
$\hat\alpha_{\mathrm{LS}} = \hat\alpha_J - \hat\alpha_1$, zoals in stap 4 van het
toy-voorbeeld. Zijn de residuen onafhankelijk van de markt, met variantie
$\sigma_\varepsilon^2$, dan is de variantie van $\hat\alpha_{\mathrm{LS}}$ het
$(1,1)$-element van $\sigma_\varepsilon^2(\mathbf{X}'\mathbf{X})^{-1}$, met
$\mathbf{X}$ een kolom enen naast de marktrendementen:

```{math}
:label: eq-vroege-anomalieen-se
\Var\!\left(\hat\alpha_{\mathrm{LS}}\right)
= \frac{\sigma_\varepsilon^2}{T}\left(1 + \frac{\hat\mu_m^2}{\hat\sigma_m^2}\right),
```

met $\hat\mu_m$ en $\hat\sigma_m$ het steekproefgemiddelde en de standaarddeviatie
van het excess marktrendement. In woorden: de standaardfout is de residuele
volatiliteit gedeeld door $\sqrt{T}$, met een kleine correctie voor de Sharpe-ratio
van de markt.

Met de marktpremie van de simulatie hieronder, 0,5% per maand bij 4,5% volatiliteit,
is die Sharpe-ratio 0,11 en de correctieterm 1,01. Bij een
residuele volatiliteit van 5% per maand en veertig jaar data is de standaardfout
$5/\sqrt{480} \approx 0{,}23\%$ per maand, bijna 3% per jaar. Dat is de standaardfout
van 2% uit [](#00-01-rendementen), nu voor een alpha. De steekproeven van Basu
(veertien jaar) en van Rosenberg, Reid en Lanstein (twaalf jaar) konden dus alleen
grote effecten significant maken.

### Fama-MacBeth met kenmerken

Een Fama-MacBeth-regressie op een kenmerk doet hetzelfde als een sortering, met
rechte lijnen als gewichten in plaats van stapfuncties.

*Waarom zou dit waar zijn?* In [](#02-08-capm) was de maandelijkse Fama-MacBeth-helling
op bèta het rendement van een portefeuille die niets kost en bèta één heeft. Een
onderzoeker die bèta door E/P vervangt, krijgt als helling het rendement van een
portefeuille die hoge E/P koopt en lage E/P short verkoopt. De gewichten stijgen
lineair met E/P, dus de uitersten wegen zwaarder dan in een sortering.

Per maand draaien we over de aandelen $i = 1, \dots, N$ de regressie

```{math}
:label: eq-vroege-anomalieen-fm
R^{e}_{i,t+1} = \gamma_{0,t+1} + \gamma_{1,t+1}\,\hat\beta_{i,m} + \gamma_{2,t+1}\, z_{i,t} + \eta_{i,t+1}.
```

In woorden: $\gamma_{2,t+1}$ is wat een eenheid kenmerk die maand opleverde, bij
gegeven bèta. We rapporteren het tijdgemiddelde $\bar\gamma_2$ met de standaardfout
uit de tijdreeks van de hellingen. In de code is dat `hap.stats.fama_macbeth`.

:::{prf:proposition} Een Fama-MacBeth-helling is een long-short-portefeuille
:label: prop-vroege-anomalieen-fm

Elke OLS-helling in een cross-sectionele regressie van $\mathbf{R}^{e}_{t+1}$ is het
rendement van een portefeuille die niets kost, blootstelling één heeft aan haar eigen
regressor en blootstelling nul aan de andere. Voor een constante en één niet-constant
kenmerk $\mathbf{z}_t$ is de helling $\hat\gamma_{z,t+1} = \sum_i w_{i,t} R^{e}_{i,t+1}$, met

```{math}
:label: eq-vroege-anomalieen-fmgewichten
w_{i,t} = \frac{z_{i,t} - \bar z_t}{\sum_j \left(z_{j,t} - \bar z_t\right)^2},
\qquad \sum_i w_{i,t} = 0, \qquad \sum_i w_{i,t}\, z_{i,t} = 1 ,
```

:::

De index $z$ staat voor het kenmerk. In [](#eq-vroege-anomalieen-fm) is dat de helling
$\gamma_{2,t+1}$. Staat bèta in de regressie, dan heeft de portefeuille bèta nul. Het
bewijsidee: een helling is een covariantie gedeeld door een variantie, en die breuk
is een gewogen som van rendementen.

:::{prf:proof}
:class: dropdown

Voor een regressie op een constante en één variabele is
$\hat\gamma_z = \sum_i (z_i - \bar z) R^{e}_i / \sum_j (z_j - \bar z)^2$. De gewichten
tellen op tot nul omdat $\sum_i (z_i - \bar z) = 0$, en
$\sum_i (z_i - \bar z) z_i = \sum_i (z_i - \bar z)^2$ geeft blootstelling één. Met
meer regressoren is $\hat{\boldsymbol{\gamma}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{R}^{e}$.
De rijen van $(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'$ zijn de gewichten, en
$(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{X} = \mathbf{I}$ zegt dat rij $k$
blootstelling één heeft aan regressor $k$ en nul aan de rest. $\square$
:::

In het toy-voorbeeld is de gemiddelde E/P 7%. De afwijkingen zijn
$(-0{,}04;\ -0{,}02;\ -0{,}01;\ 0{,}02;\ 0{,}05)$ en hun kwadratensom is $0{,}005$, dus
de gewichten zijn $(-8, -4, -2, 4, 10)$. Dat is de richting van H − L, maar met C
erbij en zwaardere uitersten. De cel haalt de gewichten uit de OLS-matrix.

```{code-cell} ipython3
z_toy = toy["E/P"]
X_toy = np.column_stack([np.ones(5), z_toy])
fm_weights = np.linalg.solve(X_toy.T @ X_toy, X_toy.T)[1]      # second row of (X'X)^-1 X'
deviation = z_toy - z_toy.mean()
print(f"som w = {fm_weights.sum():.4f}, som w z = {fm_weights @ z_toy:.4f}")
pd.DataFrame({"gewicht uit OLS": fm_weights, "formule": deviation / (deviation**2).sum()},
             index=toy.index).round(4)
```

De gewichten uit OLS en uit de formule zijn gelijk, tellen op tot nul en geven
blootstelling één aan E/P. Met twee kenmerken tegelijk beantwoordt Fama-MacBeth de
vraag van Reinganum, E/P of size, in één regressie. De prijs is lineariteit: extreme
kenmerkwaarden krijgen extreme gewichten.

Rosenberg gebruikte dezelfde regressie voor een risicomodel
{cite}`RosenbergMcKibben1973,Rosenberg1974`. Zijn bedrijf Barra bracht in 1975 het
eerste commerciële multifactor-risicomodel voor Amerikaanse aandelen uit. Het nam van
de maandelijkse hellingen op bedrijfstak, omvang, B/P en schuldgraad niet het slecht
gemeten gemiddelde, maar de goed gemeten covariantiematrix: de standaardfout van 2%
uit [](#00-01-rendementen) in omgekeerde richting.

### Het kernresultaat: marktwaarde voorspelt verwacht rendement

Verschillen verwachte rendementen tussen bedrijven, om welke reden ook, dan voorspelt
marktwaarde ze, ook als elke prijs klopt {cite}`Berk1995`.

*Waarom zou dit waar zijn?* Neem twee bedrijven met dezelfde verwachte kasstroom.
Beleggers eisen van het ene een hoger rendement en betalen er daarom minder voor. Wie
op marktwaarde sorteert, sorteert dus deels op verwacht rendement, zonder dat iemand
zich vergist. Mist het toetsmodel het risico dat die rendementen drijft, dan
verschijnt het gemiste deel als alpha van kleine bedrijven. Het omgekeerde, een
wereld waarin marktwaarde niet met verwacht rendement correleert, zou volgens Berk de
anomalie zijn.

Het eenvoudigste model is het Gordon-model $p = d_1/(r - g)$ uit
[](#01-03-williams-ddm): het dividend van volgend jaar gedeeld door discontovoet min
groei. Hier heeft bedrijf $i$ een verwachte kasstroom $C_i$ volgend jaar, een
gemeenschappelijke groeivoet $g$ en een eigen discontovoet $k_i > g$, gelijk aan het
verwachte rendement van het aandeel:

```{math}
:label: eq-vroege-anomalieen-gordon
\mathrm{ME}_i = \frac{C_i}{k_i - g},
\qquad
\log \mathrm{ME}_i = \log C_i - \log\left(k_i - g\right).
```

In woorden: de log marktwaarde is de log kasstroom min de log van het verschil
tussen discontovoet en groei. Een hogere $k_i$ maakt het bedrijf kleiner.

:::{prf:theorem} Marktwaarde voorspelt alpha (Berk)
:label: thm-vroege-anomalieen-berk

Laat [](#eq-vroege-anomalieen-gordon) gelden. Een onderzoeker kent elk aandeel een
verwacht rendement $\hat k_i$ toe met een model, en $k_i = \hat k_i + \alpha_i$. Is
$\alpha_i$ niet ontaard en onafhankelijk van $\hat k_i$ en van $\log C_i$, dan is
$\Cov(\log \mathrm{ME}_i, \alpha_i) < 0$: kleine bedrijven hebben gemiddeld een
positieve alpha ten opzichte van het model, ook al is elke prijs correct.
:::

Geeft het model elk aandeel hetzelfde verwachte rendement, dan zegt de stelling dat
marktwaarde en verwacht rendement negatief correleren. Het bewijsidee: bij gegeven
$\hat k_i$ daalt de marktwaarde in $\alpha_i$, en de kasstroom voegt alleen ruis toe.

:::{prf:proof}
:class: dropdown

Schrijf $\psi(x) = \log(x - g)$, strikt stijgend op $x > g$. Omdat $\log C_i$
onafhankelijk is van $\alpha_i$, is
$\Cov(\log \mathrm{ME}_i, \alpha_i) = -\Cov(\psi(\hat k_i + \alpha_i), \alpha_i)$.

*Stap 1: een stijgende functie correleert positief met haar argument.* Voor een
strikt stijgende $\phi$ en een onafhankelijke kopie $a'$ van $a$ is
$2\Cov(\phi(a), a) = \E[(\phi(a) - \phi(a'))(a - a')] > 0$, want de integrand is
nooit negatief en positief zodra $a \ne a'$.

*Stap 2: conditioneren op het model.* Gegeven $\hat k_i$ is $a \mapsto \psi(\hat k_i + a)$
strikt stijgend, dus stap 1 geeft $\Cov(\psi, \alpha \mid \hat k) > 0$. De wet van de
totale covariantie voegt $\Cov(\E[\psi \mid \hat k], \E[\alpha \mid \hat k])$ toe, en die
is nul omdat $\E[\alpha \mid \hat k]$ constant is. $\square$
:::

Hoe sterk is de correlatie? Een lineaire benadering rond het gemiddelde $\bar k$
geeft $\Cov(\log \mathrm{ME}, k) \approx -\Var(k)/(\bar k - g)$, uitgewerkt in de
tweede oefening. In de simulatie hieronder is de correlatie maar $-0{,}19$, omdat
bedrijven vooral in de omvang van hun kasstromen verschillen. Size is dus een ruisige
thermometer van verwacht rendement. E/P en B/M zijn betere thermometers, want hun
teller (winst, boekwaarde) schaalt mee met het kasstroomniveau en haalt zo een deel
van die ruis weg.

Dit lost de tweede verwachting uit de intuïtie in, met een verfijning. De stelling
werkt voor elke $\alpha_i$, ook voor een alpha die ontstaat doordat beleggers kasstromen
te zwaar verdisconteren. Een correlatie tussen marktwaarde en alpha bewijst dus risico noch
vergissing.

### Data snooping: Lo en MacKinlay

Een kenmerk dat in de data is gezocht, maakt in diezelfde data een grote $t$-waarde,
ook als er niets is.

*Waarom zou dit waar zijn?* Een onderzoeker kiest een kenmerk omdat het in de data
iets leek te doen. Dan sorteert hij deels op de toevalsfout in de rendementen die hij
daarna toetst: de aandelen met de grootste positieve fout komen in de hoogste
portefeuille, die met de grootste negatieve in de laagste. De $t$-waarde van hoog min
laag stijgt, en buiten de steekproef valt ze terug naar nul.

Het artikel van {cite:t}`LoMacKinlay1990` liet met berekeningen, simulaties en twee
empirische voorbeelden zien dat dit effect groot kan zijn. Hun eigen formules hebben we niet in
de primaire bron kunnen nalezen. Hieronder staat een eigen, eenvoudiger versie van
hetzelfde mechanisme.

:::{prf:proposition} Sorteren op een kenmerk dat met de steekproefalpha correleert
:label: prop-vroege-anomalieen-snooping

Laat $N$ aandelen ware alpha nul hebben, met residuen met variantie $\sigma^2$ die
onafhankelijk zijn over aandelen en perioden. Laat $s_i$ de over de aandelen
gestandaardiseerde alpha's uit $T$ perioden zijn, en het kenmerk
$z_i = \rho\, s_i + \sqrt{1-\rho^2}\,\nu_i$, met $\nu_i$ onafhankelijk
standaardnormaal. Koop de fractie $p$ met de hoogste $z$ en verkoop de fractie $p$
met de laagste, elk gelijkgewogen met $n = pN$ aandelen. Voor grote $N$ en onder
normaliteit is de verwachte $t$-waarde van de long-short-alpha *in dezelfde
steekproef*

```{math}
:label: eq-vroege-anomalieen-snooping
\E[t_{\mathrm{LS}}] \approx \rho\,\sqrt{2n}\;\frac{\varphi(q_p)}{p},
\qquad q_p = \Phi^{-1}(1-p),
```

met $\varphi$ en $\Phi$ de dichtheid en de verdelingsfunctie van de standaardnormale
verdeling. Buiten de steekproef is de verwachte $t$-waarde nul.
:::

Het bewijsidee: de sortering kiest aandelen met een $s_i$ die gemiddeld
$\rho\,\varphi(q_p)/p$ standaarddeviaties van nul ligt.

:::{prf:proof}
:class: dropdown

Omdat OLS lineair is, is de long-short-alpha het verschil van de gemiddelde
$\hat\alpha_i$ in de twee groepen. Voor gezamenlijk normale $(s_i, z_i)$ met
correlatie $\rho$ is $\E[s \mid z] = \rho z$, en $\E[z \mid z > q_p] = \varphi(q_p)/p$,
de verwachting van een afgeknotte standaardnormale. De verwachte alpha is dus
$2\rho\,\mathrm{sd}(\hat\alpha)\,\varphi(q_p)/p$, met
$\mathrm{sd}(\hat\alpha) \approx \sigma/\sqrt{T}$. De residuele variantie van de
long-short-portefeuille is $2\sigma^2/n$, dus haar alpha heeft standaardfout
$\sqrt{2/n}\,\sigma/\sqrt{T}$. De correctie uit [](#eq-vroege-anomalieen-se) is
verwaarloosbaar. Delen geeft [](#eq-vroege-anomalieen-snooping). Buiten de
steekproef zijn de residuen onafhankelijk van $z$, dus de verwachte alpha is nul.
$\square$
:::

In woorden: de verwachte $t$-waarde is evenredig met de correlatie $\rho$ tussen
kenmerk en steekproeffout, en groeit met de wortel van het aantal aandelen per poot.
Met $N = 1000$ en decielen is $p = 0{,}1$, $n = 100$ en
$\varphi(1{,}2816)/0{,}1 = 1{,}755$, dus $\E[t] \approx 24{,}8\,\rho$. Bestaat één
procent van de variantie van het kenmerk uit steekproeffout ($\rho^2 = 0{,}01$, dus
$\rho = 0{,}1$), dan is de verwachte $t$ al 2,5. Wie een kenmerk overneemt uit eerder
onderzoek op dezelfde jaren, sorteert net zo goed deels op die steekproeffout.

De grovere vorm is veel kenmerken proberen. Met $K$ onafhankelijke kandidaten zonder
effect haalt minstens één een $t$ boven 1,96 met kans $1 - 0{,}975^{K}$ (eenzijdig),
bij $K = 20$ al 40%. Daarom las {cite:t}`Black1993` de size- en waarde-effecten als
waarschijnlijke datamining: regelmaten zonder een theorie die ze vooraf voorspelde.
Dit lost de derde verwachting uit de intuïtie in. De systematische versie van het
argument is [](#06-34-factor-zoo).

```{admonition} Samengevat
:class: tip

- Een sortering schat het verwachte rendement vakje voor vakje,
  [](#eq-vroege-anomalieen-sort). De alpha van hoog min laag heeft een standaardfout
  van ongeveer $\sigma_\varepsilon/\sqrt{T}$, na veertig jaar nog 0,23% per maand,
  [](#eq-vroege-anomalieen-se).

- Een Fama-MacBeth-helling op een kenmerk is een long-short-portefeuille met
  blootstelling één, [](#eq-vroege-anomalieen-fmgewichten).

- Marktwaarde correleert negatief met elke alpha ten opzichte van een onvolledig
  model, ook bij correcte prijzen ({prf:ref}`thm-vroege-anomalieen-berk`). Meer
  spreiding in kasstroomniveaus maakt die correlatie zwakker.

- Een kenmerk met correlatie $\rho$ met de steekproeffout geeft bij duizend aandelen
  in decielen een verwachte $t$ van ongeveer $24{,}8\,\rho$,
  [](#eq-vroege-anomalieen-snooping), en erbuiten nul.

- De simulatie vraagt: hoe vaak geeft een steekproef een significante kenmerk-alpha
  die geen vergissing van de markt is?
```

## Simulatie: een size-effect zonder anomalie, en een anomalie zonder effect

Hoe vaak vindt een onderzoeker een significante kenmerk-alpha in een wereld zonder
vergissingen? In de eerste wereld zijn alle prijzen correct, maar toetst hij met het
CAPM terwijl er een tweede risico is. In de tweede geldt het CAPM exact, maar kiest
hij zijn kenmerk op basis van de steekproef. Het antwoord: de echte premie in de
eerste wereld ziet hij in minder dan een op de vijf steekproeven. In de tweede ziet
hij in ruim negen op de tien een premie die niet bestaat.

### (a) Een wereld met twee risico's

Er zijn 1000 aandelen. Elk heeft een CAPM-bèta $\beta_{i,m}$ en een blootstelling
$\delta_i$ aan een tweede beprijsde factor $h$ die onafhankelijk is van de markt,
bijvoorbeeld een faillissements- of recessierisico:

$$
R^{e}_{i,t+1} = \beta_{i,m} f_{m,t+1} + \delta_i f_{h,t+1} + \varepsilon_{i,t+1}.
$$

| symbool | betekenis | waarde |
|---|---|---|
| $\beta_{i,m}$ | CAPM-bèta | $1 + 0{,}3\,\mathcal{N}(0,1)$, begrensd op $[0{,}2;\ 1{,}8]$ |
| $\delta_i$ | blootstelling aan $h$ | uniform op $[0;\ 1{,}5]$ |
| $\E[f_m]$, $\SD(f_m)$ | premie en volatiliteit van de markt | 0,5% en 4,5% per maand |
| $\E[f_h]$, $\SD(f_h)$ | premie en volatiliteit van $h$ | 0,4% en 3% per maand |
| $\SD(\varepsilon)$ | eigen volatiliteit van een aandeel | 10% per maand |
| $k_i$ | verwacht rendement per jaar | $3\% + 12\,(0{,}5\%\,\beta_{i,m} + 0{,}4\%\,\delta_i)$ |
| $g$ | groei van de kasstroom | 2% per jaar |
| $\log C_i$ | kasstroomniveau, los van risico | $\mathcal{N}(0;\ 1{,}5^2)$ |

Op het ware tweefactormodel is er geen alpha. De marktwaarde volgt uit
[](#eq-vroege-anomalieen-gordon), met een gemiddeld verwacht rendement van
$3 + 12\,(0{,}5 + 0{,}4 \cdot 0{,}75) = 12{,}6\%$ per jaar. We sorteren eenmalig op
marktwaarde in tien portefeuilles van honderd aandelen. De eerste cel bouwt de
aandelen en meet hoe sterk marktwaarde met verwacht rendement correleert.

```{code-cell} ipython3
def alpha_t(returns, factors):
    """OLS intercepts and t-statistics of every column of `returns` (T x K) on `factors` (T or T x L)."""
    X = np.column_stack([np.ones(len(returns)), factors])
    coef, *_ = np.linalg.lstsq(X, returns, rcond=None)
    resid = returns - X @ coef
    s2 = (resid**2).sum(axis=0) / (len(returns) - X.shape[1])
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[0, 0])
    return coef[0], coef[0] / se


n_stocks, n_groups, T_sim, n_samples = 1000, 10, 480, 1000
sim = {"lam_m": 0.005, "sd_m": 0.045,      # market premium and volatility per month
       "lam_h": 0.004, "sd_h": 0.030,      # premium and volatility of the second factor h
       "sd_eps": 0.10}                     # idiosyncratic volatility per month

beta_i = np.clip(1.0 + 0.3 * rng.standard_normal(n_stocks), 0.2, 1.8)
delta_i = rng.uniform(0.0, 1.5, n_stocks)
k_i = 0.03 + 12 * (sim["lam_m"] * beta_i + sim["lam_h"] * delta_i)      # expected return per year
log_me = rng.normal(0.0, 1.5, n_stocks) - np.log(k_i - 0.02)

group = pd.qcut(log_me, n_groups, labels=False)           # size decile, 0 = smallest
count = np.bincount(group)
beta_p = pd.Series(beta_i).groupby(group).mean().to_numpy()
delta_p = pd.Series(delta_i).groupby(group).mean().to_numpy()

pd.DataFrame(
    {"correlatie met log ME": [np.corrcoef(log_me, x)[0, 1] for x in (k_i, beta_i, delta_i)]},
    index=["verwacht rendement k", "bèta", "delta"],
).round(3)
```

De correlatie tussen $\log \mathrm{ME}$ en het verwachte rendement is $-0{,}19$: zwak,
want het kasstroomniveau bepaalt de meeste spreiding in marktwaarde, maar met het
teken van {prf:ref}`thm-vroege-anomalieen-berk`. De volgende cel trekt 1000
steekproeven van veertig jaar en schat telkens de alpha van klein min groot, op het
CAPM en op het ware model.

```{code-cell} ipython3
berk = {"CAPM": [], "tweefactor": []}
for _ in range(n_samples):
    f_m = sim["lam_m"] + sim["sd_m"] * rng.standard_normal(T_sim)
    f_h = sim["lam_h"] + sim["sd_h"] * rng.standard_normal(T_sim)
    noise = sim["sd_eps"] / np.sqrt(count) * rng.standard_normal((T_sim, n_groups))
    port = np.outer(f_m, beta_p) + np.outer(f_h, delta_p) + noise
    smb = port[:, 0] - port[:, -1]
    berk["CAPM"].append(alpha_t(smb, f_m))
    berk["tweefactor"].append(alpha_t(smb, np.column_stack([f_m, f_h])))
berk = {k: np.array(v) for k, v in berk.items()}          # (n_samples, 2): alpha, t

pd.DataFrame(
    {model: {"gem. alpha klein - groot (% p.m.)": 100 * v[:, 0].mean(),
             "theorie (% p.m.)": 100 * (delta_p[0] - delta_p[-1]) * sim["lam_h"] if model == "CAPM" else 0.0,
             "gem. t": v[:, 1].mean(),
             "fractie t > 1.96": np.mean(v[:, 1] > 1.96)}
     for model, v in berk.items()}
).T.round(3)
```

Zoals in stap 4 van het toy-voorbeeld, waar H − L 5,325% alpha had bij een negatieve
bèta, is de alpha van klein min groot hier het verschil van twee alpha's. Op het CAPM
is ze gemiddeld 0,076% per maand, tegen 0,079% volgens de theorie: het verschil in
$\delta$ tussen de uiterste portefeuilles maal de premie van $h$. Die alpha haalt
$t > 1{,}96$ maar in 18,6% van de steekproeven. Op het ware model haalt ze de drempel
in 2,4%, zoals bij een eenzijdige toets hoort.

Een correct beprijsd verschil van bijna een procentpunt per jaar blijft na veertig
jaar dus meestal onzichtbaar: de standaardfout van 2% uit [](#00-01-rendementen).

### (b) Kiezen wat werkt

Nu geldt het CAPM exact, met dezelfde marktpremie van 0,5% en volatiliteit van 4,5%
per maand. Er zijn 500 aandelen zonder alpha en 100 kandidaat-kenmerken die pure ruis
zijn. Voor elk kenmerk vormt de onderzoeker een long-short-portefeuille van de 50
hoogste en de 50 laagste aandelen en schat hij de CAPM-alpha over twintig jaar. Hij
rapporteert het kenmerk met de hoogste $t$. Ter vergelijking volgt de cel ook één
kenmerk dat vooraf is gekozen, en ze kijkt naar de twintig jaar erna.

```{code-cell} ipython3
n_sn, n_leg, T_in, T_out, n_cand, n_rep = 500, 50, 240, 240, 100, 400


def long_short_weights(z, n_leg):
    """Weights +1/n_leg on the n_leg highest and -1/n_leg on the n_leg lowest values in each row of z."""
    rank = stats.rankdata(z, axis=-1) - 1                  # 0 = lowest value
    n = z.shape[-1]
    weights = np.zeros(z.shape)
    weights[rank >= n - n_leg] = 1 / n_leg
    weights[rank < n_leg] = -1 / n_leg
    return weights


snoop = []
for _ in range(n_rep):
    beta = 1.0 + 0.3 * rng.standard_normal(n_sn)
    f = sim["lam_m"] + sim["sd_m"] * rng.standard_normal(T_in + T_out)
    R = np.outer(f, beta) + sim["sd_eps"] * rng.standard_normal((T_in + T_out, n_sn))
    candidates = rng.standard_normal((n_cand, n_sn))       # 100 pure-noise characteristics
    P = R @ long_short_weights(candidates, n_leg).T
    _, t_in = alpha_t(P[:T_in], f[:T_in])
    _, t_out = alpha_t(P[T_in:], f[T_in:])
    best = np.argmax(t_in)                                 # the characteristic that "works" best
    snoop.append((t_in[0], t_in[best], t_out[best]))       # candidate 0 plays the pre-chosen one
snoop = pd.DataFrame(snoop, columns=["één kenmerk", "beste van 100, in de steekproef",
                                     "beste van 100, erna"])

snoop.describe().loc[["mean", "std"]].T.assign(
    **{"fractie t > 1.96": (snoop > 1.96).mean(), "fractie t > 3": (snoop > 3).mean()}
).round(3)
```

Eén vooraf gekozen kenmerk gedraagt zich zoals het hoort, met een gemiddelde $t$ rond
nul en een standaarddeviatie rond één. Het beste van honderd haalt in de steekproef
in 93,2% van de gevallen $t > 1{,}96$ en in 13,8% zelfs $t > 3$. In de twintig jaar
erna is er niets van over. Dit is geen anomalie die na publicatie verdwijnt, maar een
die nooit heeft bestaan.

Let in de figuur links op de afstand tussen de twee verdelingen, en rechts op waar
het beste kenmerk ligt, in en na de steekproef.

```{code-cell} ipython3
:label: cel-vroege-anomalieen-sim
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
bins = np.linspace(-4, 7, 45)
axes[0].hist(berk["CAPM"][:, 1], bins=bins, alpha=0.65, label="t(alpha), CAPM")
axes[0].hist(berk["tweefactor"][:, 1], bins=bins, alpha=0.65, label="t(alpha), ware tweefactormodel")
axes[0].axvline(1.96, color="black", lw=1, ls="--")
axes[0].set_title("(a) Klein min groot in een wereld zonder mispricing")
axes[0].set_xlabel("t-waarde van de alpha (1000 steekproeven van 40 jaar)")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].legend()

bins = np.linspace(-4, 6, 45)
for column in snoop.columns:
    axes[1].hist(snoop[column], bins=bins, alpha=0.55, label=column)
axes[1].axvline(1.96, color="black", lw=1, ls="--")
axes[1].set_title("(b) Het beste van 100 ruiskenmerken")
axes[1].set_xlabel("t-waarde van de CAPM-alpha (400 steekproeven)")
axes[1].set_ylabel("Aantal steekproeven")
axes[1].legend()
fig.tight_layout()
plt.show()
```

:::{figure} #cel-vroege-anomalieen-sim
:label: fig-vroege-anomalieen-sim
:width: 100%

Links: bij correcte prijzen geeft een sortering op marktwaarde een CAPM-alpha,
omdat marktwaarde de gemiste risicofactor meet. Op het ware model verdwijnt ze. Dat
de CAPM-verdeling meestal onder de stippellijn valt, is de standaardfout van 2% uit
[](#00-01-rendementen). Rechts: een wereld zonder alpha. Het beste kenmerk ligt in de
steekproef ver rechts van nul en valt daarna terug op de verdeling van een
willekeurig kenmerk. Samen tonen de panelen het dilemma van dit tijdvak: een echte
premie kan onzichtbaar zijn, en een zichtbare premie onecht.
:::

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** S. Basu, Journal of Finance 1977 {cite}`Basu1977`; Rolf W. Banz, Journal of
Financial Economics 1981 {cite}`Banz1981`; Barr Rosenberg, Kenneth Reid en Ronald
Lanstein, *Persuasive Evidence of Market Inefficiency*, Journal of Portfolio
Management 1985 {cite}`RosenbergReidLanstein1985`; Donald B. Keim, Journal of
Financial Economics 1983 {cite}`Keim1983`.

**Wat.** De kernbevindingen zoals de auteurs ze samenvatten, in de tabel onder de
cellen. Hun tabelwaarden per portefeuille hebben we niet in de primaire bronnen
kunnen nalezen, dus we toetsen teken, orde van grootte en rangorde.

**Data hier.** Decielen op E/P, B/M en marktwaarde uit de Kenneth French Data
Library, value- en equal-weighted, met markt en risicovrije rente, via `hap.data`.
Elke oorspronkelijke steekproef zetten we naast de jaren na publicatie, tot 2026-07.

**Verschil met het origineel.** French sorteert NYSE, AMEX en Nasdaq op
NYSE-breekpunten, jaarlijks eind juni, terwijl Basu en Banz NYSE-aandelen gebruikten
en Keim dagelijkse abnormale rendementen op NYSE en AMEX. Rosenberg, Reid en Lanstein
hielden size, E/P en bedrijfstak constant, wat een decielsortering op B/M niet doet.

**Verwachte afwijking.** In de oorspronkelijke steekproeven heeft elke
long-short-portefeuille (hoog min laag E/P en B/M, klein min groot) een positieve
CAPM-alpha, en een ander teken wijst op een fout in de code. Na publicatie verwachten
we kleinere value-weighted alpha's, en in Keims periode het grootste deel van de
size-premie in januari.
```

De eerste cel laadt de decielen en bouwt de long-short-portefeuilles.

```{code-cell} ipython3
market = hap_data.market_monthly()
rf_month, mkt_excess = market["RF"], market["Mkt-RF"]
deciles = ["Lo 10", "2-Dec", "3-Dec", "4-Dec", "5-Dec", "6-Dec", "7-Dec", "8-Dec", "9-Dec", "Hi 10"]
datasets = {"E/P": "Portfolios_Formed_on_E-P", "B/M": "Portfolios_Formed_on_BE-ME",
            "size": "Portfolios_Formed_on_ME"}


def excess_deciles(name, weighting):
    """Decile excess returns; value- (table 0) or equal-weighted."""
    table = 0 if weighting == "VW" else "Equal-Weight"
    return hap_data.french(name, table=table)[deciles].sub(rf_month, axis=0).dropna()


panels = {}
for sort, name in datasets.items():
    for w in ("VW", "EW"):
        panels[(sort, w)] = excess_deciles(name, w)


def long_short(sort, weighting):
    """High-minus-low for E/P and B/M, small-minus-big for size."""
    p = panels[(sort, weighting)]
    return p["Lo 10"] - p["Hi 10"] if sort == "size" else p["Hi 10"] - p["Lo 10"]
```

De tweede cel schat per kenmerk, periode en weging de CAPM-alpha met $t$-waarde,
bèta, gemiddelde en de standaardfout van dat gemiddelde, in procent per maand.

```{code-cell} ipython3
def capm_row(series):
    """CAPM alpha, t, beta, mean and SE of one excess or long-short return series (% per month)."""
    series = series.dropna()
    alpha, t = alpha_t(series.to_numpy(), mkt_excess.loc[series.index].to_numpy())
    beta = np.polyfit(mkt_excess.loc[series.index], series, 1)[0]
    return {"alpha (% p.m.)": 100 * alpha, "t(alpha)": t, "bèta": beta,
            "gem. (% p.m.)": 100 * series.mean(),
            "SE gem.": 100 * series.std() / np.sqrt(len(series)), "maanden": len(series)}


periods = {
    "E/P": {"Basu 1957-04/1971-03": ("1957-04", "1971-03"), "na publicatie 1978/2026": ("1978-01", "2026-07"),
            "volledig 1951/2026": ("1951-07", "2026-07")},
    "B/M": {"RRL 1973-01/1984-09": ("1973-01", "1984-09"), "na publicatie 1985/2026": ("1985-01", "2026-07"),
            "volledig 1926/2026": ("1926-07", "2026-07")},
    "size": {"Banz 1936/1975": ("1936-01", "1975-12"), "na publicatie 1982/2026": ("1982-01", "2026-07"),
             "volledig 1926/2026": ("1926-07", "2026-07")},
}
rows = {}
for sort, spans in periods.items():
    for label, (a, b) in spans.items():
        for w in ("VW", "EW"):
            rows[(sort, label, w)] = capm_row(long_short(sort, w).loc[a:b])
ls_table = pd.DataFrame(rows).T
ls_table.index.names = ["sortering", "periode", "weging"]
ls_table.round(3)
```

De tabel hieronder zet de bevindingen van de auteurs naast de alpha's uit de cel, in
procent per maand met de $t$-waarde tussen haakjes.

| | origineel | hier, oorspronkelijke steekproef | hier, na publicatie |
|---|---|---|---|
| E/P, Basu 1957–1971 | lage koers-winstverhouding: hoger rendement, ook na correctie voor risico | VW 0,46 (1,76), EW 0,89 (4,53) | VW 0,29 (1,58), EW 0,60 (4,64) |
| B/M, RRL 1973–1984 | hoge boekwaarde-koersverhouding: significant abnormaal rendement | VW 1,42 (3,31), EW 1,49 (4,07) | VW 0,09 (0,40), EW 1,12 (5,98) |
| size, Banz 1936–1975 | kleine bedrijven: hoger rendement na correctie voor risico, vooral de allerkleinste | VW 0,23 (0,72), EW 0,59 (1,64) | VW −0,14 (−0,68), EW −0,02 (−0,11) |

**Geslaagd.** Het teken is in alle zes combinaties van kenmerk en weging positief,
zoals de verwachte afwijking eiste. Dat lost de eerste verwachting uit de intuïtie
in. Na publicatie zijn de value-weighted alpha's kleiner, en voor size niet van nul
te onderscheiden, ook zoals verwacht. Het effect is overal groter bij
equal-weighting, want alle drie de kenmerken zijn het sterkst bij kleine aandelen. De long-short-bèta van E/P en B/M is in de
oorspronkelijke steekproef negatief: goedkope aandelen waren in CAPM-zin niet
riskanter.

De B/M-alpha van 1,42% per maand, ongeveer 17% per jaar, is groot genoeg om in
twaalf jaar significant te zijn. Over de volle eeuw verklaart het CAPM de
value-weighted B/M-premie grotendeels, met een alpha van 0,14% en een
long-short-bèta van 0,44.

Voor size in Banz' periode is de alpha op French' brede eerste deciel niet
significant, omdat Banz' effect in een kleinere groep bedrijven zat. Ook
{cite:t}`AsnessFrazziniIsrael2018` vinden op de huidige CRSP-data een zwakker
decielverschil dan Banz, met $t = 1{,}82$. Zij wijten dat aan datafouten die CRSP na
zijn artikel heeft gecorrigeerd.

De figuur toont dezelfde alpha's per deciel. Let op de vorm: stijgt de alpha van
deciel 1 naar deciel 10, en is het profiel na publicatie vlakker?

```{code-cell} ipython3
:label: cel-vroege-anomalieen-decielen
:tags: [hide-input]

decile_periods = {"E/P": list(periods["E/P"].items())[:2], "B/M": list(periods["B/M"].items())[:2],
                  "size": list(periods["size"].items())[:2]}
fig, axes = plt.subplots(1, 3, figsize=(12, 4.0), sharey=True)
for ax, (sort, spans) in zip(axes, decile_periods.items()):
    for (label, (a, b)), color, shift in zip(spans, hap.plotting.COLORS, (-0.12, 0.12)):
        table = pd.DataFrame({d: capm_row(panels[(sort, "VW")][d].loc[a:b]) for d in deciles}).T
        se_alpha = table["alpha (% p.m.)"] / table["t(alpha)"]
        ax.errorbar(np.arange(1, 11) + shift, table["alpha (% p.m.)"], yerr=2 * se_alpha,
                    fmt="o", capsize=2, color=color, label=label)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_title(f"CAPM-alpha per {sort}-deciel (value-weighted)")
    ax.set_xlabel("Deciel (1 = laagste kenmerk)")
    ax.set_xticks(range(1, 11))
    ax.legend(loc="upper left")
axes[0].set_ylabel("Alpha (% per maand, ± 2 SE)")
fig.tight_layout()
plt.show()
```

:::{figure} #cel-vroege-anomalieen-decielen
:label: fig-vroege-anomalieen-decielen
:width: 100%

CAPM-alpha's per deciel in de oorspronkelijke steekproef en na publicatie. Voor E/P
lopen de alpha's in Basu's periode op van rond nul in de laagste decielen naar
duidelijk positief in de hoogste. Voor B/M lopen ze in de periode van Rosenberg, Reid
en Lanstein vrijwel monotoon van negatief naar positief. Voor size springt alleen het
kleinste deciel eruit, met een foutbalk die nul bevat. Na publicatie zijn alle drie
de profielen vlakker.
:::

### Het januari-effect

Keim vond over 1963–1979 dat bijna vijftig procent van het size-effect in januari
zat, waarvan meer dan de helft in de eerste handelsweek. De cel splitst klein min
groot naar januari en de overige maanden. De bijdrage van januari is het
januarigemiddelde gedeeld door de som van de twaalf maandgemiddelden, alleen
gerapporteerd als beide delen niet negatief zijn.

```{code-cell} ipython3
def january_split(series):
    """Mean and t of January versus February-December returns, and January's share of the annual sum."""
    jan, rest = series[series.index.month == 1], series[series.index.month != 1]
    annual = jan.mean() + 11 * rest.mean()
    both_positive = min(jan.mean(), rest.mean()) >= 0
    return {"januari (% p.m.)": 100 * jan.mean(), "t januari": jan.mean() / (jan.std() / np.sqrt(len(jan))),
            "feb-dec (% p.m.)": 100 * rest.mean(), "t feb-dec": rest.mean() / (rest.std() / np.sqrt(len(rest))),
            "jaarpremie (%)": 100 * annual, "bijdrage januari": jan.mean() / annual if both_positive else np.nan,
            "jaren": len(jan)}


january_periods = {"Keim 1963-1979": ("1963-01", "1979-12"), "1926-1962": ("1926-07", "1962-12"),
                   "na 1980": ("1980-01", "2026-07")}
january_rows = {}
for label, (a, b) in january_periods.items():
    for w in ("VW", "EW"):
        january_rows[(label, w)] = january_split(long_short("size", w).loc[a:b])
january = pd.DataFrame(january_rows).T
january.round(3)
```

**Geslaagd.** In Keims periode valt in beide wegingen ongeveer vier vijfde van de
jaarpremie in januari (kolom bijdrage januari), meer dan de bijna vijftig procent van
Keim, die met voor risico gecorrigeerde dagrendementen werkte. Over 1926–1962 draagt januari
eveneens het grootste deel. Na 1980 is januari nog positief, maar doen kleine aandelen het in de
andere maanden slechter dan grote, zodat de jaarpremie vrijwel verdwijnt.

Een premie die alleen in januari wordt betaald, is moeilijk als risicopremie te
verdedigen. De gangbare verklaringen zijn institutioneel: verkopen in december om
fiscale verliezen te nemen, en *window dressing* (fondsbeheerders die verliezers
verkopen vóór ze hun portefeuille rapporteren).

## Wat er brak, en wat daarna kwam

**Wat het CAPM verklaart.** Nog steeds veel. Over de volle eeuw verklaart het de
value-weighted B/M-premie grotendeels, met een alpha van 0,14% ($t = 0{,}83$). De
anomalieën zijn verschillen van enkele
tienden van een procent per maand, met standaardfouten van dezelfde orde. Geen van de
vier artikelen stelde een ander model voor. Reinganum las zijn resultaten zelfs als
een verkeerd gespecificeerd evenwichtsmodel, niet als inefficiëntie, omdat de
abnormale rendementen minstens twee jaar aanhielden.

**Waar het breekt.** Goedkope aandelen hadden in de oorspronkelijke steekproeven
positieve CAPM-alpha's, terwijl hun long-short-bèta rond nul of negatief lag. Het
scherpste feit uit onze replicatie is de value-weighted B/M-alpha van 1,42% per
maand ($t = 3{,}31$) in de twaalf jaar van Rosenberg, Reid en Lanstein. Keims
seizoenspatroon is een barst van een andere soort: ongeveer vier vijfde van de
size-premie in één maand.

**Risico of vergissing?** Rosenberg, Reid en Lanstein kozen in hun titel de
vergissing: een goedkoop aandeel is een fout van de markt. De andere lezing kwam van
{cite:t}`Reinganum1981` en later {cite:t}`Berk1995`: een lage koers ten opzichte van
winst, boekwaarde of omvang *is* een hoge discontovoet. De simulatie laat zien dat
beide lezingen hetzelfde patroon geven. Scheiden kan alleen met een maat voor het
gemiste risico die niet uit prijzen komt, en die had niemand. Het januari-effect en
het verdwijnen na publicatie passen slecht bij een risicopremie, maar wel bij
datamining. Dat de equal-weighted waarde-alpha na 1985 bleef, pleit daar weer tegen.
Voor een belegger is het de vraag van Santa-Clara uit [](#00-00-setup): droeg wie in 1985 value kocht een
beprijsd risico, of dacht hij iets te weten wat de prijs niet wist? Dezelfde
transactie kan beide zijn geweest.

**Wat er daarna kwam.** Zeven jaar later zouden Fama en French al deze kenmerken in
één regressie zetten en er twee overhouden. Eerst wendde de theorie zich naar een
ander prijsprobleem, waarin toestandsvariabelen de rol van kenmerken overnemen: de
rente en de waarde van flexibiliteit, in [](#03-17-termijnstructuur-real-options).

## Oefeningen

:::{exercise}
:label: ex-vroege-anomalieen-1

**Instap: een bredere sortering.** Zet in het toy-voorbeeld ook aandeel C in
portefeuille H, zodat H = (C, D, E) en L = (A, B).

1. Bereken met de hand de bèta, het excess rendement en de alpha van H en van H − L,
   en controleer het antwoord met `toy_portfolio`.
2. Waarom is de alpha van H − L kleiner dan 5,325%?
:::

:::{solution} ex-vroege-anomalieen-1
:class: dropdown

**(1)** H heeft bèta $(0{,}90 + 0{,}80 + 0{,}55)/3 = 0{,}75$, excess rendement
$(6 + 7 + 9)/3 = 7{,}33\%$ en alpha $(1{,}50 + 3{,}00 + 6{,}25)/3 = 3{,}58\%$. H − L
heeft bèta $0{,}75 - 1{,}05 = -0{,}30$, excess rendement $7{,}33 - 4{,}55 = 2{,}78\%$
en alpha $2{,}78 + 0{,}30 \cdot 5 = 4{,}28\%$, gelijk aan $3{,}58 - (-0{,}70)$.

```{code-cell} ipython3
broad = pd.DataFrame({"H": toy_portfolio(["C", "D", "E"]), "L": toy_portfolio(low_ep)}).T
broad.loc["H - L"] = broad.loc["H"] - broad.loc["L"]
broad.round(5)
```

**(2)** C heeft een kleinere alpha (1,50%) dan D en E en verdunt het gemiddelde van
H. Wat dit leert: een brede uiterste portefeuille smeert een effect in de uitersten
uit, zoals het effect van Banz in French' brede eerste deciel.
:::

:::{exercise}
:label: ex-vroege-anomalieen-2

**De orde van grootte van Berk.** Neem het model van
{prf:ref}`thm-vroege-anomalieen-berk` met de parameters uit simulatie (a).

1. Leid met een eerste-ordebenadering van $\log(k - g)$ rond $\bar k$ af dat
   $\Cov(\log \mathrm{ME}, k) \approx -\Var(k)/(\bar k - g)$ en
   $\Corr(\log \mathrm{ME}, k) \approx -\SD(k)/\left((\bar k - g)\,\SD(\log \mathrm{ME})\right)$.
2. Bereken beide benaderingen voor `k_i` en `log_me` en vergelijk ze met de
   steekproefwaarden.
3. Hoe verandert de correlatie als de spreiding van $\log C_i$ halveert?
4. Simuleer veertig jaar maandrendementen van de 1000 losse aandelen en draai
   Fama-MacBeth met de ware bèta en de gestandaardiseerde $\log \mathrm{ME}$, met en
   zonder $\delta$. Wat moet de coëfficiënt op $\log \mathrm{ME}$ met $\delta$ erbij
   zijn?
:::

:::{solution} ex-vroege-anomalieen-2
:class: dropdown

**(1)** Met $\psi(k) = \log(k-g) \approx \psi(\bar k) + (k - \bar k)/(\bar k - g)$ en de
onafhankelijkheid van $\log C$ is
$\Cov(\log \mathrm{ME}, k) = -\Cov(\psi(k), k) \approx -\Var(k)/(\bar k - g)$. Delen
door $\SD(k)\,\SD(\log \mathrm{ME})$ geeft de correlatie.

**(2) en (3)**

```{code-cell} ipython3
def berk_approximation(log_cash_sd):
    log_me_alt = log_cash_sd / 1.5 * (log_me + np.log(k_i - 0.02)) - np.log(k_i - 0.02)
    cov_approx = -k_i.var() / (k_i.mean() - 0.02)
    return {"cov steekproef": np.cov(log_me_alt, k_i)[0, 1], "cov benadering": cov_approx,
            "corr steekproef": np.corrcoef(log_me_alt, k_i)[0, 1],
            "corr benadering": cov_approx / (k_i.std() * log_me_alt.std())}


pd.DataFrame({"SD log C = 1.5": berk_approximation(1.5), "SD log C = 0.75": berk_approximation(0.75)}).round(4)
```

De benadering ligt dicht bij de steekproefwaarden. Het verschil komt van de kromming
van de logaritme. Bij een halvering van de kasstroomspreiding wordt de correlatie
bijna twee keer zo sterk. Wat dit leert: hoe minder ruis in het kasstroomniveau, hoe
beter marktwaarde het verwachte rendement meet, en daarom meten B/M en E/P het beter
dan marktwaarde alleen.

**(4)**

```{code-cell} ipython3
f_m = sim["lam_m"] + sim["sd_m"] * rng.standard_normal(T_sim)
f_h = sim["lam_h"] + sim["sd_h"] * rng.standard_normal(T_sim)
stock_returns = pd.DataFrame(np.outer(f_m, beta_i) + np.outer(f_h, delta_i)
                             + sim["sd_eps"] * rng.standard_normal((T_sim, n_stocks)))


def as_panel(values):
    """One-row characteristic frame, broadcast over all periods by fama_macbeth."""
    return pd.DataFrame([values], columns=stock_returns.columns)


size_z = (log_me - log_me.mean()) / log_me.std()
specs = {"bèta + log ME": {"bèta": as_panel(beta_i), "log ME": as_panel(size_z)},
         "bèta + delta + log ME": {"bèta": as_panel(beta_i), "delta": as_panel(delta_i),
                                   "log ME": as_panel(size_z)}}
fm_sim = {}
for name, chars in specs.items():
    out = hap.stats.fama_macbeth(stock_returns, chars, lags=0)
    out.attrs = {}                                   # drop metadata so pd.concat accepts the tables
    fm_sim[name] = out[["estimate", "tstat"]].assign(estimate=lambda d: 100 * d["estimate"])
pd.concat(fm_sim).round(3)
```

Met $\delta$ erbij is de ware coëfficiënt op $\log \mathrm{ME}$ nul, want het
verwachte rendement is lineair in bèta en $\delta$. In deze steekproef is hij zonder
$\delta$ negatief, $-0{,}027\%$ per maand per standaarddeviatie ($t = -1{,}57$), en met
$\delta$ vrijwel nul ($t = 0{,}54$). Zonder $\delta$ neemt marktwaarde dus een deel van
de rol van de gemiste factor over, maar na veertig jaar niet significant. Wat dit
leert: een kenmerk verklaart rendementen die bèta niet verklaart zolang de beprijsde
blootstelling ontbreekt, en ook dat effect is een gemiddelde met een grote
standaardfout.
:::

:::{exercise}
:label: ex-vroege-anomalieen-3

**Is value ook een januari-effect?** {cite:t}`Bhandari1988` vond zijn
schuldgraad-effect vooral in januari.

1. Pas `january_split` toe op de hoog-min-laag-portefeuilles van E/P en B/M,
   equal- en value-weighted, voor 1963–1984 en voor 1985–2026.
2. Zit de waarde-premie net zo sterk in januari als de size-premie?
3. Wat zegt het verschil over de vraag van {cite:t}`Reinganum1981`: zijn E/P en B/M
   gewoon size?
:::

:::{solution} ex-vroege-anomalieen-3
:class: dropdown

```{code-cell} ipython3
value_periods = {"1963-1984": ("1963-07", "1984-12"), "1985-2026": ("1985-01", "2026-07")}
value_rows = {}
for sort in ("E/P", "B/M"):
    for label, (a, b) in value_periods.items():
        for w in ("VW", "EW"):
            value_rows[(sort, label, w)] = january_split(long_short(sort, w).loc[a:b])
pd.DataFrame(value_rows).T.round(3)
```

**(2)** In 1963–1984 zit de value-weighted waarde-premie net als de size-premie voor
ongeveer twee derde in januari: 65% voor E/P en 67% voor B/M. Equal-weighted is dat
24% en 45%, met significante premies in de overige maanden.

**(3)** Na 1985 verdient de equal-weighted B/M-portefeuille 0,78% per maand buiten
januari ($t = 4{,}17$), terwijl de size-premie buiten januari verdween. Een effect
buiten januari is niet simpelweg size, al beslist één sortering dat niet definitief.
Wat dit leert: het seizoenspatroon is een tweede dimensie waarop anomalieën
verschillen, die jaargemiddelden verbergen.
:::

:::{exercise}
:label: ex-vroege-anomalieen-4

**Voegt size iets toe naast bèta?** Banz stelde zijn vraag in de vorm van
[](#eq-vroege-anomalieen-fm).

1. Draai Fama-MacBeth op de tien value-weighted size-decielen, met per deciel een
   rollende bèta uit de voorgaande 60 maanden en de log van zijn gemiddelde
   bedrijfsgrootte ten opzichte van het decielgemiddelde, beide bekend vóór de maand.
   Doe dat voor 1936–1975, met en zonder size, en na 1982.
2. Kan deze cross-sectie bèta en omvang scheiden?
:::

:::{solution} ex-vroege-anomalieen-4
:class: dropdown

```{code-cell} ipython3
size_vw = panels[("size", "VW")]
avg_size = hap_data.french("Portfolios_Formed_on_ME", table=5)[deciles]
log_rel_size = np.log(avg_size).sub(np.log(avg_size).mean(axis=1), axis=0).shift(1)
rolling_beta = (size_vw.rolling(60).cov(mkt_excess.loc[size_vw.index])
                .div(mkt_excess.loc[size_vw.index].rolling(60).var(), axis=0).shift(1))


def fm_size(a, b, with_size=True):
    """Fama-MacBeth on the ten size deciles over [a, b] (estimates in % per month)."""
    chars = {"bèta": rolling_beta.loc[a:b]}
    if with_size:
        chars["log relatieve size"] = log_rel_size.loc[a:b]
    out = hap.stats.fama_macbeth(size_vw.loc[a:b], chars, lags=0)
    out.attrs = {}                     # drop metadata so pd.concat accepts the tables
    return out[["estimate", "tstat", "n_periods"]].assign(estimate=lambda d: 100 * d["estimate"])


pd.concat({
    ("Banz 1936-1975", "bèta"): fm_size("1936-01", "1975-12", with_size=False),
    ("Banz 1936-1975", "bèta + size"): fm_size("1936-01", "1975-12"),
    ("na 1982", "bèta + size"): fm_size("1982-01", "2026-07"),
}).round(3)
```

**(1)** In Banz' periode is de coëfficiënt op de log relatieve omvang negatief, het
teken van Banz, maar niet significant. De helling op bèta zakt van positief zonder
size naar negatief met size. Na 1982 is de size-coëfficiënt positief en niet
significant.

**(2)** Nee. Tien portefeuilles die op omvang zijn gesorteerd, hebben bèta's die bijna
perfect met hun omvang samenhangen, dus de regressie kan de twee niet uit elkaar
houden. Wat dit leert: een cross-sectie die op één kenmerk is gesorteerd, heeft maar
één dimensie. Om bèta en omvang te scheiden zijn portefeuilles nodig die op beide
tegelijk zijn gesorteerd.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
