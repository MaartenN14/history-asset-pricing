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

(06-36-inelastische-markten)=

# Demand systems en inelastische markten

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1986–2025. Het tijdvak loopt van Shleifers studie van S&P 500-inclusies tot de *inelastic markets hypothesis* van Gabaix en Koijen (de vraag naar aandelen reageert nauwelijks op de prijs) en het debat over passief beleggen.

**Wat we al weten.** Koersen bewegen meer dan het dividendnieuws rechtvaardigt, en die extra beweging is statistisch hetzelfde als voorspelbare rendementen. Of dat risico of vergissing is, valt met prijzen alleen niet te beslissen ([](#05-33-fama-vs-shiller)). Het vorige college liet machines honderden voorspellers combineren zonder theorie ([](#06-35-machine-learning)). Er ontbraken gegevens over wie koopt en wie verkoopt, en een model waarin dat verschil maakt.

**Welke vraag staat open.** Hoeveel stijgt de waarde van de aandelenmarkt als er één dollar extra in stroomt? En wat zegt het antwoord over wat koersen beweegt?
```

## Overzicht

Hoeveel stijgt de waarde van de aandelenmarkt als beleggers zonder enig nieuws één dollar
extra in aandelen stoppen? Volgens Gabaix en Koijen ongeveer vijf dollar, omdat de vraag
naar aandelen nauwelijks op de prijs reageert. Dat getal is wel zo moeilijk te meten dat
een kwart eeuw data alles tussen twee en acht toelaat, zoals de simulatie in dit college
laat zien.

In de standaardtheorie van deze reeks bestaat die vraag niet eens. Daar bepaalt de
stochastische discontofactor $m$ (SDF) de prijs, en speelt de hoeveelheid die iemand wil
kopen geen rol, omdat arbitrageurs elke prijsafwijking zonder nieuws meteen wegkopen. De
vraagcurve voor aandelen is dan vlak. Dit college gaat over het onderzoek dat die vlakke
curve mat en verwierp. Het college toetst dus geen theorie, maar volgt een reeks metingen
die nog op een verklaring wachten. Het gaat om elasticiteiten, inclusie-effecten en
de prijsimpact van *flows* (geldstromen van beleggers in of uit een markt).

In dit college doen we het volgende.

- In een markt met een mandaatfonds en een actieve belegger rekenen we met de hand uit
  hoeveel één dollar de prijs opdrijft.
- We leiden de multiplier $M = 1/\zeta$ af en zien waarom standaardmodellen een
  elasticiteit van tientallen voorspellen.
- We behandelen het vraagsysteem van Koijen en Yogo en *granular instrumental variables*
  (instrumenten uit de eigen schokken van grote beleggers).
- We simuleren hoe goed OLS en GIV de elasticiteit meten in steekproeven zo lang als die
  van Gabaix en Koijen.
- Op echte data regresseren we kwartaalrendementen op de netto aandelenaankopen per
  sector, en meten we het effect van veertien recente S&P 500-toevoegingen.

In 1986 liet Shleifer zien dat aandelen bij de aankondiging van hun opname in de S&P 500
in koers stegen, terwijl hun kasstromen niet veranderden {cite}`Shleifer1986`. Koijen en
Yogo {cite}`KoijenYogo2019` schatten per institutionele belegger een vraagsysteem uit de
posities die fondsbeheerders elk kwartaal aan de SEC melden. Gabaix en Koijen
{cite}`GabaixKoijen2021` tilden die aanpak naar de hele markt, en met hun artikel werden
flows
een eigen verklaring voor koersbewegingen, naast discontovoeten en vergissingen.
Volgens Santa-Clara hoort de vraag wat de markt beweegt bij de grote open vragen van dit
decennium {cite}`SantaClara2026`.

## Intuïtie: waarom zou dit waar zijn?

Op 16 november 2020 maakte S&P Dow Jones Indices bekend dat Tesla op 21 december in de S&P
500 zou worden opgenomen. Er was geen nieuws over auto's, winst of rente. Wel stond vast
dat elk indexfonds op die dag Tesla-aandelen zou moeten kopen, ongeacht de prijs. Als de
vraagcurve vlak is, maakt dat voor de koers niets uit. Daalt de curve, dan moeten de
indexfondsen de prijs opdrijven tot iemand bereid is te verkopen.

Shleifer onderzocht in 1986 precies die situatie. Aandelen die na 1976, toen indexfondsen
opkwamen, in de index kwamen, behaalden bij de aankondiging een significant abnormaal
rendement van ongeveer 3%, terwijl dat effect daarvoor ontbrak {cite}`Shleifer1986`. Omdat
een
inclusie de kasstromen niet verandert, kan de prijs alleen stijgen doordat de vraag groter
is dan de markt tegen de oude prijs opvangt. Dat bedoelen onderzoekers met een dalende
vraagcurve.

Voor één aandeel is dat nog te begrijpen, want aandelen zonder goed substituut springen
bij opname sterker {cite}`WurglerZhuravskaya2002`. Voor de markt als geheel is er nog
minder substituut. Een belegger die aandelen verkoopt aan iemand die geld in de markt
stopt, gaat zelf meer obligaties of kas houden. Een pensioenfonds met een mandaat van
zestig procent
aandelen doet dat niet, en een indexfonds evenmin. Als bijna iedereen aan zo'n mandaat
vastzit, moet de prijs ver bewegen voordat de weinige flexibele beleggers willen verkopen.

Gabaix en Koijen maken daar een getal van. Stel dat de totale vraag naar aandelen met één
procent daalt als de prijs vijf procent stijgt. De *prijselasticiteit van de vraag* (de
procentuele daling van de gevraagde hoeveelheid per procent prijsstijging) is dan 0,2. Een
flow van één procent van de marktwaarde moet de prijs in dat geval vijf procent
opdrijven, zodat één dollar erin vijf dollar marktwaarde oplevert. Volgens Gabaix en
Koijen voorspellen de meeste modellen een honderd keer kleinere prijsimpact
{cite}`GabaixKoijen2021`.

Meten is lastig, en daarvoor zijn twee redenen. Beleggers stoppen geld in aandelen als ze
optimistisch zijn, en optimisme duwt ook de prijzen omhoog, zodat samenhang tussen
instroom en rendement nog geen oorzaak bewijst. Bovendien is elk gekocht aandeel door
iemand verkocht. De prijs beweegt dus niet doordat er gekocht wordt, maar doordat de
kopers minder op de prijs reageren dan de verkopers.

We verwachten daarom dat een instroom de prijs meer opdrijft naarmate meer vermogen aan
vaste mandaten gebonden is. Een verschuiving naar passief beleggen zou de markt dus
gevoeliger maken voor flows. Omdat optimisme prijzen en flows tegelijk beweegt, verwachten
we ook dat een gewone regressie de vraag inelastischer laat lijken dan ze is.

## Toy-voorbeeld: een passief fonds, een actieve belegger en één dollar

In deze kleine markt rekenen we uit hoeveel één dollar instroom de prijs opdrijft, eerst
met een inelastische en daarna met een elastische actieve belegger. Er zijn $S = 100$
aandelen tegen een prijs $P_0 = 1$, en twee beleggers houden ze.

| | fonds | actieve belegger | markt |
|---|---|---|---|
| aandelen bij $P_0 = 1$ | 40 | 60 | 100 |
| obligaties | 10 | – | – |
| vraaggedrag | vaste fractie $\theta = 0{,}8$ in aandelen | $Q_A = 60 - 60\,\zeta_A \log P$ | vast aanbod |
| elasticiteit | $1 - \theta = 0{,}2$ (stap 1) | $\zeta_A$ | gewogen gemiddelde |

De prijselasticiteit uit de intuïtie heet voor de actieve belegger $\zeta_A$, zodat een
prijsstijging van één procent zijn vraag met $\zeta_A$ procent verlaagt. Voor de
procentuele prijsstijging $x$ gebruiken we een recept dat de theorie later afleidt,
namelijk de extra vraag bij de oude prijs gedeeld door de som over de beleggers van
elasticiteit maal positie.

**Stap 1, de elasticiteit van het fonds.** Stijgt de prijs met één procent, dan groeit het
vermogen van het fonds naar 50,4. Volgens het mandaat hoort het dan $0{,}8 \times 50{,}4 = 40{,}32$
in aandelen te houden, terwijl zijn aandelen 40,4 waard zijn. Het verkoopt dus voor 0,08,
oftewel 0,2% van zijn positie, en zijn elasticiteit is $1 - \theta = 0{,}2$.

**Stap 2, de instroom.** Een spaarder stort 1 in het fonds. Bij de oude prijs wil het
fonds dan $0{,}8 \times 51 = 40{,}8$ in aandelen, en die extra 0,8 is de flow naar
aandelen. Omdat het aanbod vast is, stijgt de prijs tot beide beleggers samen weer 100
aandelen willen, en in eerste orde geeft dat

$$
0{,}8 = (0{,}2 \times 40 + \zeta_A \times 60)\, x .
$$

**Stap 3, geval 1 met $\zeta_A = 0{,}2$.** De haakjes zijn $8 + 12 = 20$, dus $x = 0{,}8/20 = 4\%$.
De marktwaarde stijgt met $0{,}04 \times 100 = 4$. De multiplier telt per dollar
vraagverschuiving naar aandelen, niet per dollar in het fonds, en is dus $4/0{,}8 = 5$. De
marktelasticiteit is $20/100 = 0{,}2$, en $5 = 1/0{,}2$.

**Stap 4, geval 2 met $\zeta_A = 5$.** De haakjes zijn $8 + 300 = 308$, dus $x = 0{,}8/308 = 0{,}26\%$,
en de multiplier is $0{,}26/0{,}8 = 0{,}32$, gelijk aan $1/3{,}08$. Eén elastische
belegger met drie vijfde van de markt maakt de prijsimpact dus vijftien keer kleiner.

**Stap 5, een verschuiving naar passief.** Blijf in geval 2, maar laat het fonds nu 70
aandelen houden (vermogen 87,5) en de actieve belegger 30. De marktelasticiteit daalt naar
$(0{,}2 \times 70 + 5 \times 30)/100 = 1{,}64$. Dezelfde instroom verhoogt de prijs dan
met $0{,}8/164 = 0{,}49\%$, een multiplier van 0,61.

De code hieronder rekent de drie gevallen na, zowel in eerste orde als met de exacte
evenwichtsprijs, en zet de uitkomsten naast de handberekening.

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

```{code-cell} ipython3
def toy_market(zeta_active, equity_fund=40.0, equity_active=60.0, theta=0.8, inflow=1.0):
    """First-order solution of the two-investor toy market (shares = value at P0 = 1)."""
    market = equity_fund + equity_active
    zeta = ((1 - theta) * equity_fund + zeta_active * equity_active) / market
    price_change = theta * inflow / (zeta * market)
    multiplier = price_change * market / (theta * inflow)
    return zeta, 100 * price_change, multiplier


def toy_market_exact(zeta_active, equity_fund=40.0, equity_active=60.0, theta=0.8, inflow=1.0):
    """Exact clearing price: mandate fund Q = theta*W/P and active demand Q = a - b log P."""
    wealth = equity_fund / theta

    def excess_demand(log_p):
        price = np.exp(log_p)
        fund = theta * (wealth + inflow + equity_fund * (price - 1)) / price
        active = equity_active - zeta_active * equity_active * log_p
        return fund + active - (equity_fund + equity_active)

    return 100 * (np.exp(optimize.brentq(excess_demand, -0.5, 0.5)) - 1)


toy_cases = {
    "geval 1: zeta_A = 0,2": {"zeta_active": 0.2},
    "geval 2: zeta_A = 5": {"zeta_active": 5.0},
    "geval 2, fonds met 70 aandelen": {"zeta_active": 5.0, "equity_fund": 70.0, "equity_active": 30.0},
}
by_hand = {  # (price change in %, multiplier) from steps 3 to 5
    "geval 1: zeta_A = 0,2": (0.8 / 20 * 100, 4 / 0.8),
    "geval 2: zeta_A = 5": (0.8 / 308 * 100, 1 / 3.08),
    "geval 2, fonds met 70 aandelen": (0.8 / 164 * 100, 1 / 1.64),
}
toy_rows = {}
for name, case in toy_cases.items():
    zeta, price_change, multiplier = toy_market(**case)
    hand_price, hand_multiplier = by_hand[name]
    toy_rows[name] = {"zeta markt": zeta,
                      "prijsstijging, hand (%)": hand_price, "prijsstijging, code (%)": price_change,
                      "multiplier, hand": hand_multiplier, "multiplier, code": multiplier,
                      "exact evenwicht (%)": toy_market_exact(**case)}
pd.DataFrame(toy_rows).T.round(4)
```

Code en handberekening geven dezelfde getallen, en het exacte evenwicht (laatste kolom)
wijkt nauwelijks af van de eerste-ordebenadering. Voor een multiplier van vijf hoeft dus
niet iedereen aan een mandaat vast te zitten, als ook de actieve belegger even
inelastisch is als het fonds. Bij de verschuiving naar passief
verdubbelt de multiplier bijna zonder dat iemand zijn gedrag verandert. In geval 1 maakt
dezelfde verschuiving niets uit, omdat beide beleggers daar even elastisch zijn.

## Theorie

De theorie leidt naar één formule en naar de vraag hoe die te meten is. Uit het evenwicht
bij een vast aanbod volgt dat de prijs beweegt met de instroom gedeeld door de
marktelasticiteit. Daarna zien we waarom een mean-variance-belegger een elasticiteit van
tientallen heeft, terwijl Koijen en Yogo er een onder één meten. Tot slot blijkt dat een
gewone regressie de elasticiteit niet meet en een granular instrument wel.

### Opzet: mandaten, elasticiteiten en evenwicht

*Waarom zou dit waar zijn?* Als bij een vast aanbod één belegger meer aandelen wil, moet
een ander er minder willen. Alleen een hogere prijs kan die ander daartoe bewegen. Hoe ver
de prijs moet stijgen, hangt af van hoe sterk de rest op de prijs reageert.

We volgen de eenvoudigste vorm van het model van {cite:t}`GabaixKoijen2021`, in eigen
notatie. In afwijking van de setup schrijven we de prijs als $P_t$ en is $p = \Delta \log P$
de
procentuele prijsverandering, terwijl andere kleine letters, zoals de flows $f_{i,t}$ en
later $c_t$, fracties van een positie of van de marktwaarde zijn en geen logs. Er zijn $N$
beleggers $i$ en
een vast aantal aandelen $S$. Belegger $i$ vraagt $Q_i(P_t)$ aandelen ter waarde van $E_i = P_t Q_i$,
met marktaandeel $s_i = E_i/\sum_j E_j$. Zijn prijselasticiteit is

```{math}
:label: eq-inelastische-markten-elasticiteit
\zeta_i = -\frac{\partial \log Q_i}{\partial \log P}.
```

Een elasticiteit van 0,2, zoals die van het fonds in het toy-voorbeeld, betekent dat een
prijsstijging van 1% de gevraagde hoeveelheid met 0,2% verlaagt. De elasticiteit van de
markt is het waardegewogen gemiddelde $\zeta = \sum_i s_i \zeta_i$. Een flow $\Delta F_i$
is de verandering in de dollarvraag van belegger $i$ bij ongewijzigde prijs, bijvoorbeeld
de 0,8 uit het toy-voorbeeld.

:::{prf:lemma} Een fonds met een vast mandaat
:label: thm-inelastische-markten-mandaat

Een fonds met vermogen $W = B + PQ$ (obligaties plus aandelen) dat een vaste fractie $\theta \in (0, 1]$ in aandelen houdt, heeft prijselasticiteit $\zeta = 1 - \theta$. Een instroom $\Delta F$ in het fonds verhoogt zijn vraag naar aandelen bij ongewijzigde prijs met $\theta\,\Delta F$ dollar.
:::

:::{prf:proof}
:class: dropdown

Na een prijsverandering en een instroom, maar vóór het herbalanceren, is het vermogen $W(P) = B_0 + \Delta F + Q_0 P$. Het mandaat vraagt $Q(P) = \theta W(P)/P$, zodat $\partial Q/\partial P = -\theta (B_0 + \Delta F)/P^2$. In het uitgangspunt ($\Delta F = 0$, $P = P_0$, $B_0 = (1-\theta) W_0$, $P_0 Q_0 = \theta W_0$) is dan

$$
\zeta = -\frac{P_0}{Q_0}\frac{\partial Q}{\partial P}
= \frac{\theta B_0}{P_0 Q_0} = \frac{\theta (1-\theta) W_0}{\theta W_0} = 1 - \theta .
$$

Verder is $\partial Q/\partial \Delta F = \theta / P_0$, dus $P_0\,\Delta Q = \theta\,\Delta F$. $\square$
:::

Het lemma bevestigt stap 1 van het toy-voorbeeld. Een puur aandelenindexfonds ($\theta = 1$)
heeft elasticiteit nul, terwijl een 60/40-fonds op 0,4 uitkomt. Gabaix en Koijen laten toe
dat fondsen hun aandelenfractie naar het verwachte rendement bijsturen, en toch schatten
ze de elasticiteit van instellingen rond 0,2 {cite}`GabaixKoijen2021`.

### Het kernresultaat: de flow-multiplier

Een instroom verhoogt de prijs met de instroom als fractie van de marktwaarde, gedeeld
door de marktelasticiteit. Iedere belegger vermindert zijn vraag als de prijs stijgt, en
de prijs stijgt precies zo ver dat die verminderingen samen de instroom opvangen.

:::{prf:proposition} De flow-multiplier
:label: thm-inelastische-markten-multiplier

Laat elke belegger in eerste orde vragen $\Delta Q_i / Q_i = -\zeta_i\, p + \Delta F_i / E_i$, en laat het aanbod vast zijn, $\sum_i \Delta Q_i = 0$. Een flow die alleen tussen beleggers wordt herverdeeld, beweegt de prijs dan niet, en met $\Delta F = \sum_i \Delta F_i$ en $E = \sum_i E_i$ geldt

```{math}
:label: eq-inelastische-markten-multiplier
p = \frac{1}{\zeta}\,\frac{\Delta F}{E},
\qquad
M \equiv \frac{\Delta (P S)}{\Delta F} = \frac{1}{\zeta}.
```
:::

:::{prf:proof}
:class: dropdown

Vermenigvuldig de vraag van belegger $i$ met $P_0 Q_i = E_i$ en tel op, dan is $P_0 \sum_i \Delta Q_i = -p \sum_i \zeta_i E_i + \sum_i \Delta F_i$. Het vaste aanbod maakt de linkerkant nul, dus $p \sum_i \zeta_i E_i = \Delta F$ en $p = \Delta F/(\zeta E)$ met $\zeta = \sum_i s_i \zeta_i$. De marktwaarde verandert in eerste orde met $\Delta(PS) = p\,E$, dus $\Delta(PS)/\Delta F = 1/\zeta$. $\square$
:::

Volgens [](#eq-inelastische-markten-multiplier) stijgt de prijs meer naarmate de markt
minder elastisch is. Bij $\zeta = 0{,}2$ maakt een instroom van 1% van de marktwaarde de
aandelen 5% duurder, bij $\zeta = 20$ nog maar 0,05%. In het toy-voorbeeld gaf een
instroom van 0,8% bij $\zeta = 0{,}2$ precies $p = 4\%$. Een instroom drijft de prijs dus
op, en harder naarmate meer vermogen aan een mandaat vastzit, precies zoals de
Tesla-inclusie deed vermoeden.

Voor de replicatie zijn twee kanttekeningen van belang. Netto aankopen tellen over alle
beleggers op tot de netto uitgifte, omdat elk gekocht aandeel verkocht is. In het
toy-voorbeeld kwam er 1 in het fonds en verschoof de vraag naar aandelen bij de oude prijs
met 0,8, terwijl de markt per saldo niets kocht. De prijs beweegt door die 0,8, de
verschuiving $\Delta F$, en juist die is niet waarneembaar. Verder kunnen een paar zeer
elastische hedgefondsen $\zeta$ groot
maken, als ze groot genoeg zijn.

### Waarom standaardmodellen een elasticiteit van tientallen geven

Een belegger die volgens mean-variance kiest, reageert ongeveer honderd keer sterker op de
prijs dan Gabaix en Koijen meten. Stijgt de prijs van een claim op een uitbetaling over
een jaar zonder nieuws met één procent, dan daalt het verwachte rendement met ongeveer één
procentpunt. Bij een premie van vijf procent is dat een vijfde van de premie. Omdat zijn
positie evenredig is met de premie, wil de belegger dan een vijfde minder houden.

:::{prf:proposition} Elasticiteit van een mean-variance-belegger
:label: thm-inelastische-markten-cara

Een belegger met CARA-nut en absolute risicoaversie $\gamma$ kiest $Q$ aandelen met payoff $x_{t+1} \sim N(\mu_x, \sigma_x^2)$ per aandeel, bij een netto risicovrije rente $R^{f}$. Zijn vraag is $Q = (\mu_x - (1+R^{f}) P)/(\gamma \sigma_x^2)$, en zijn prijselasticiteit is

```{math}
:label: eq-inelastische-markten-cara
\zeta = \frac{1 + R^{f}}{\E[R_{t+1}] - (1 + R^{f})},
\qquad \E[R_{t+1}] = \mu_x / P .
```
:::

:::{prf:proof}
:class: dropdown

Het eindvermogen is $W_0 (1+R^{f}) + Q(x_{t+1} - (1+R^{f}) P)$ en normaal verdeeld, dus de belegger maximaliseert $Q(\mu_x - (1+R^{f})P) - \tfrac{\gamma}{2}Q^2\sigma_x^2$, met oplossing $Q = (\mu_x - (1+R^{f}) P)/(\gamma\sigma_x^2)$. Dan is $-\partial \log Q/\partial \log P = (1+R^{f}) P/(\mu_x - (1+R^{f}) P)$, en delen van teller en noemer door $P$ geeft de formule. $\square$
:::

In de noemer van [](#eq-inelastische-markten-cara) staat de premie. Met een premie van
vijf procent per jaar en $1 + R^{f} \approx 1$ is $\zeta \approx 1/0{,}05 = 20$, honderd
keer de waarde van Gabaix en Koijen. Hoe kleiner de premie, hoe groter de elasticiteit,
omdat dezelfde prijsstijging dan een groter deel van de premie wegneemt. De waarde 20
geldt alleen voor een prijsafwijking die binnen het jaar terugloopt, omdat alleen dan de
hele stijging uit het rendement van dat ene jaar komt. Een permanente afwijking spreidt
het verlies over veel jaren en geeft daardoor een veel lagere elasticiteit.

Ook de prijsformule uit [](#05-33-fama-vs-shiller) geeft een volledig vlakke vraagcurve.
De prijs
is $P_t = \E_t[m_{t+1} x_{t+1}]$, en bij een representatieve belegger hangt $m_{t+1}$ af
van consumptie, niet van wie welk aandeel houdt. Een model waarin flows prijzen bewegen,
laat de SDF dus afhangen van de posities van specifieke beleggers, of laat hun
verwachtingen met hun flows meebewegen. Dat laatste is de dichtheid $\xi$ uit
{prf:ref}`prop-fama-vs-shiller-equivalentie`, die objectieve in subjectieve verwachtingen
omzet.

### Het vraagsysteem van Koijen en Yogo

Koijen en Yogo meten elasticiteiten per belegger door aan te nemen dat elke belegger zijn
portefeuille kiest op kenmerken van aandelen, zoals grootte en bèta, plus een eigen
voorkeur. De gewichten zijn dan per belegger uit zijn posities te schatten. De
gevoeligheid van een gewicht voor de eigen marktwaarde van het aandeel is de helling van
de vraagcurve van die belegger.

{cite:t}`KoijenYogo2019` gebruiken de kwartaalposities van instellingen die meer dan \$100 miljoen beheren en daarom hun posities elk kwartaal moeten melden. Belegger $i$ heeft vermogen $A_i$ en kiest uit een universum van aandelen $n$. Alles daarbuiten, zoals kas, heet het buitenactivum $0$, en het gewicht van aandeel $n$ ten opzichte daarvan is

```{math}
:label: eq-inelastische-markten-ky
\frac{w_i(n)}{w_i(0)} = \exp\!\Big(\beta_{0,i}\, \mathrm{me}(n) + \sum_{k} \beta_{k,i}\, x_k(n) + \beta_{K,i}\Big)\, \varepsilon_i(n),
```

met $\mathrm{me}(n)$ de log-marktwaarde, $x_k(n)$ kenmerken zoals de
boekwaarde-marktwaardeverhouding, en $\varepsilon_i(n) \ge 0$ de latente vraag (*latent
demand*). Die latente vraag is de voorkeur die de kenmerken niet verklaren. De
vergelijking heeft de vorm van een logit, waarin de gewichten met het buitenactivum
optellen tot één.

:::{prf:proposition} Elasticiteit in het logit-vraagsysteem
:label: thm-inelastische-markten-ky-elasticiteit

Houd het vermogen $A_i$ en de kenmerken $x_k(n)$ vast. De vraag daalt dan in de prijs zolang $\beta_{0,i} < 1/(1 - w_i(n))$, met als prijselasticiteit van belegger $i$ voor aandeel $n$

```{math}
:label: eq-inelastische-markten-ky-elasticiteit
\zeta_i(n) = -\frac{\partial \log Q_i(n)}{\partial \log P(n)} = 1 - \beta_{0,i}\,\big(1 - w_i(n)\big).
```
:::

:::{prf:proof}
:class: dropdown

Schrijf $\delta(n)$ voor de rechterkant van [](#eq-inelastische-markten-ky). Omdat de gewichten inclusief het buitenactivum optellen tot één, is $w_i(n) = \delta(n)/(1 + \sum_m \delta(m))$, en dus $\partial \log w_i(n)/\partial \log \delta(n) = 1 - w_i(n)$. De log-marktwaarde is $\mathrm{me}(n) = \log P(n) + \log S(n)$, zodat $\partial \log \delta(n)/\partial \log P(n) = \beta_{0,i}$. Het aantal gevraagde aandelen is $Q_i(n) = A_i w_i(n)/P(n)$, dus $\partial \log Q_i(n)/\partial \log P(n) = \beta_{0,i}(1 - w_i(n)) - 1$. $\square$
:::

Met $\beta_{0,i} = 1$ belegt iemand als een indexfonds, met elasticiteit nul bij een klein
gewicht. Met $\beta_{0,i} = 0$ houdt hij een vast dollarbedrag, met elasticiteit één. Een
elasticiteit van twintig vraagt een sterk negatieve $\beta_{0,i}$, en die vinden de
schattingen niet. Met dit systeem vinden {cite:t}`KoijenRichmondYogo2024` elasticiteiten
die daar ver onder blijven, want zelfs hedgefondsen, de meest elastische instellingen,
komen gewogen naar vermogen uit op ongeveer een half. Het gaat bovendien om de korte
termijn, en volgens {cite:t}`VanDerBeck2026` is de prijsimpact op lange termijn kleiner.

De latente vraag is zelf een vraagschok, en daarin zit het identificatieprobleem. Een
hogere vraag drijft $\mathrm{me}(n)$ op, zodat een gewone schatting van $\beta_{0,i}$ naar
boven vertekend is en de vraag inelastischer lijkt dan ze is. Koijen en Yogo
instrumenteren daarom met de universa van andere beleggers. Het instrument is de
marktwaarde die een aandeel zou hebben als die anderen gelijkgewogen binnen hun universum
zouden beleggen. Dat werkt zolang hun universa niet samenhangen met de latente vraag van
belegger $i$.

Veranderingen in de latente vraag verklaren bij hen het grootste deel van de variantie van
rendementen tussen aandelen, veranderingen aan de aanbodkant maar een klein deel
{cite}`KoijenYogo2019`. De meeste koersbewegingen van individuele aandelen zijn dus
vraagverschuivingen die geen kenmerk uit de [factor zoo](#06-34-factor-zoo) verklaart.

### Granular instrumental variables

Voor de hele markt bestaat geen instrument uit universa, maar de markt bestaat wel uit een
paar zeer grote spelers, en hun eigen schokken kunnen als instrument dienen. Verkoopt één
groot pensioenfonds na een herzien mandaat, dan komt die verkoop niet uit het sentiment en
beweegt ze toch de prijs. Het verschil tussen de groottegewogen en de gelijkgewogen flow
isoleert zulke schokken, omdat een gemeenschappelijke schok in beide gemiddelden even
groot is.

{cite:t}`GabaixKoijen2024` formaliseren dat idee. In de eenvoudigste versie heeft sector
$i$, bijvoorbeeld de pensioenfondsen, marktaandeel $S_i$ met $\sum_i S_i = 1$. Zijn flow
in procenten van zijn positie is

```{math}
:label: eq-inelastische-markten-giv-model
f_{i,t} = -\zeta\, p_t + \eta_t + u_{i,t},
```

met $\eta_t$ een gemeenschappelijke vraagschok (sentiment, macronieuws) en $u_{i,t}$
idiosyncratische schokken met variantie $\sigma_u^2$, onafhankelijk over $i$ en van
$\eta_t$. Het aanbod is vast, zodat $\sum_i S_i f_{i,t} = 0$. We schrijven $f_{E,t} = \tfrac1N \sum_i f_{i,t}$
voor de gelijkgewogen flow, en $u_{E,t}$ en $u_{S,t} = \sum_i S_i u_{i,t}$ voor de
gelijkgewogen en groottegewogen schok. De Herfindahl-index $H = \sum_i S_i^2$ is $1/N$ bij
even grote sectoren en groeit naarmate een paar sectoren domineren.

:::{prf:proposition} GIV identificeert de elasticiteit, OLS niet
:label: thm-inelastische-markten-giv

Laat $z_t = \sum_i S_i f_{i,t} - f_{E,t}$ het verschil zijn tussen de groottegewogen en de gelijkgewogen flow. Dan is de GIV-schatter $\zeta^{\mathrm{GIV}} = -\Cov(z_t, f_{E,t})/\Cov(z_t, p_t)$ gelijk aan $\zeta$ zodra $H > 1/N$, terwijl de OLS-schatter van $f_{E,t}$ op $p_t$ als kansgrens heeft

```{math}
:label: eq-inelastische-markten-ols-bias
\plim \hat\zeta^{\mathrm{OLS}} = \zeta\left(1 - \frac{\sigma_\eta^2 + \sigma_u^2/N}{\sigma_\eta^2 + \sigma_u^2 H}\right).
```
:::

:::{prf:proof}
:class: dropdown

*Stap 1: het instrument bevat alleen idiosyncratische schokken.* Het evenwicht geeft $0 = -\zeta p_t + \eta_t + u_{S,t}$, dus $p_t = (\eta_t + u_{S,t})/\zeta$. Het gelijkgewogen gemiddelde van [](#eq-inelastische-markten-giv-model) is $f_{E,t} = -\zeta p_t + \eta_t + u_{E,t}$, en omdat $-\zeta p_t + \eta_t = -u_{S,t}$, is $z_t = u_{S,t} - u_{E,t}$.

*Stap 2: het instrument is exogeen en relevant.* Met onafhankelijke $u_{i,t}$ is $\Cov(u_S, u_E) = \sigma_u^2 \sum_i S_i/N = \sigma_u^2/N = \Var(u_E)$, dus $\Cov(z, u_E) = 0$, en $\eta$ is onafhankelijk van $z$. Verder is $\Cov(z, p) = (\Var(u_S) - \Cov(u_E, u_S))/\zeta = \sigma_u^2(H - 1/N)/\zeta$.

*Stap 3: GIV meet $\zeta$.* Er geldt $\Cov(z, f_E) = -\zeta \Cov(z, p) + \Cov(z, \eta + u_E) = -\zeta\Cov(z,p)$, en $\Cov(z,p) \neq 0$ zodra $H > 1/N$.

*Stap 4: OLS is vertekend.* Uit $p = (\eta + u_S)/\zeta$ volgt $\Var(p) = (\sigma_\eta^2 + \sigma_u^2 H)/\zeta^2$. Omdat $\Cov(u_S, u_E) = \sigma_u^2/N$ uit stap 2, is $\Cov(p, \eta + u_E) = (\sigma_\eta^2 + \sigma_u^2/N)/\zeta$, dus $-\Cov(p, f_E)/\Var(p) = \zeta - \Cov(p, \eta + u_E)/\Var(p)$, en dat is de formule. $\square$
:::

Als iedereen tegelijk optimistisch wordt, stijgt de prijs, maar koopt per saldo niemand
extra, omdat het aanbod vast is. De gemeten flow is volgens stap 1 van het bewijs
$f_{E,t} = u_{E,t} - u_{S,t}$, zonder de gemeenschappelijke schok, zodat een regressie een
prijsbeweging zonder bijbehorende flow ziet, en dus vraag die nauwelijks op de prijs
reageert. Volgens
[](#eq-inelastische-markten-ols-bias) gaat de OLS-schatter daarom naar nul als zulke
gemeenschappelijke schokken domineren ($\sigma_\eta^2 \gg \sigma_u^2$). Neem $\sigma_\eta = \sigma_u = 1\%$,
twintig sectoren met Zipf-groottes ($H - 1/N = 0{,}073$) en $\zeta = 0{,}2$. De kansgrens
is dan 0,013, een schijnbare multiplier van bijna 80 terwijl de ware 5 is. Een gewone
regressie laat de vraag dus te inelastisch lijken, zoals verwacht, maar met een factor van
ruim vijftien.

Het instrument werkt dankzij het vaste aanbod. Omdat de groottegewogen flow altijd nul is,
geldt $z_t = -f_{E,t}$, en volgens stap 1 van het bewijs blijven daarin alleen
idiosyncratische schokken over. GIV haalt zijn kracht uit $H - 1/N$, de mate waarin de
markt *granular* is (gedomineerd
door een paar grote spelers), en bij even grote sectoren is het instrument nul. Omdat
sectoren in de praktijk verschillend op gemeenschappelijke schokken reageren, halen Gabaix
en Koijen die reacties eerst met hoofdcomponenten uit de flows. Op de Flow of Funds van
1993 tot 2018 vinden ze zo, afhankelijk van de specificatie, multipliers tussen 3 en 8
{cite}`GabaixKoijen2021`.

### Wat een lage elasticiteit verandert

Een lage elasticiteit maakt koersen beweeglijk en voorspelbaar, en geeft passief beleggen
en inkoop van eigen aandelen een koerseffect. Zolang flows traag terugdraaien, draaien ook
de prijsafwijkingen traag terug. De prijs-dividendverhouding voorspelt dan rendementen
zonder dat iemand een hogere premie eist.

**Excess volatility.** Vanaf hier is $\ell_{t+1}$ het log rendement. We schrijven de
log-prijs als fundamentele waarde plus opgebouwde vraagdruk, $\log P_t = v_t + c_t/\zeta$,
met $c_t$ de cumulatieve netto flow in procenten van de marktwaarde. Als $c_t$ een
stationair AR(1)-proces is met persistentie $\phi$, onafhankelijk van $v_t$, dan geldt

```{math}
:label: eq-inelastische-markten-volatiliteit
\Var(\ell_{t+1}) = \Var(\Delta v_{t+1}) + \frac{\Var(\Delta c_{t+1})}{\zeta^2},
\qquad
\E_t[\ell_{t+1}] - \E_t[\Delta v_{t+1}] = -\frac{1-\phi}{\zeta}\, c_t .
```

De eerste term is de volatiliteit die Shiller gerechtvaardigd noemde. De tweede is de
*excess volatility* uit [](#03-15-shiller-excess-volatility), en die groeit met
$1/\zeta^2$. Zijn dividenden evenredig aan de fundamentele waarde, dan is de log
prijs-dividendverhouding $c_t/\zeta$ plus een constante, en voorspelt ze rendementen met
helling $-(1-\phi)$. Zo ontstaat de voorspelbaarheid van Cochrane, en een onderzoeker die
alleen prijzen en dividenden ziet, noemt die een tijdvariërende discontovoet, net als in
[](#05-33-fama-vs-shiller).

::::{note} Een eeuw kwartaaldata uit een economie waarin flows prijzen maken
:class: dropdown

We simuleren [](#eq-inelastische-markten-volatiliteit) per kwartaal, honderd jaar lang, in 2000 steekproeven per elasticiteit. De fundamentele waarde groeit met 1,5% per kwartaal bij een volatiliteit van 3,5%. De flows krijgen elk kwartaal twee onafhankelijke schokken van 0,8% van de marktwaarde, van spaarders en uit sentiment. Ze doven uit met $\phi = 0{,}95$ per kwartaal, een halfwaardetijd van ruim drie jaar. Een onderzoeker die niets van flows weet, toetst of de prijs-dividendverhouding rendementen voorspelt.

```{code-cell} ipython3
SD_V, MU_V, SD_FLOW, SD_SENTIMENT, PHI_FLOW = 0.035, 0.015, 0.008, 0.008, 0.95
ZETAS = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 20.0]


def simulate_flow_economy(n, T, zeta):
    """Quarterly log returns ell = dv + dc / zeta with AR(1) cumulative flows c (fractions of market value).

    Returns returns (n, T), fundamental news dv (n, T) and the log price-dividend ratio minus its
    constant, c / zeta, observed at the start of each quarter (n, T).
    """
    dv = rng.normal(MU_V, SD_V, (n, T))
    shocks = rng.normal(0.0, SD_FLOW, (n, T)) + rng.normal(0.0, SD_SENTIMENT, (n, T))
    c = np.empty((n, T + 1))
    c[:, 0] = rng.normal(0.0, np.hypot(SD_FLOW, SD_SENTIMENT) / np.sqrt(1 - PHI_FLOW**2), n)
    for t in range(T):
        c[:, t + 1] = PHI_FLOW * c[:, t] + shocks[:, t]
    return dv + np.diff(c, axis=1) / zeta, dv, c[:, :-1] / zeta


def naive_researcher(r, dv, pd_ratio):
    """Row-wise statistics: annualised volatility, sigma(r)/sigma(dv), R2 of r on dv, PD slope and t-value."""
    rd, dvd = r - r.mean(1, keepdims=True), dv - dv.mean(1, keepdims=True)
    x = pd_ratio - pd_ratio.mean(1, keepdims=True)
    slope = (x * rd).sum(1) / (x**2).sum(1)
    resid = rd - slope[:, None] * x
    t_value = slope / np.sqrt((resid**2).sum(1) / (r.shape[1] - 2) / (x**2).sum(1))
    r2_news = (rd * dvd).sum(1) ** 2 / ((rd**2).sum(1) * (dvd**2).sum(1))
    return {"vol": 2 * r.std(1), "ratio": r.std(1) / dv.std(1), "r2": r2_news,
            "slope": slope, "t": t_value}


var_dc = 2 * (SD_FLOW**2 + SD_SENTIMENT**2) / (1 + PHI_FLOW)
flow_sim = {zeta: naive_researcher(*simulate_flow_economy(2000, 400, zeta)) for zeta in ZETAS}
pd.DataFrame({
    zeta: {"vol. theorie (%/jr)": 200 * np.sqrt(SD_V**2 + var_dc / zeta**2),
           "vol. mediaan (%/jr)": 100 * np.median(s["vol"]),
           "vol. 5e-95e pct": f"{100 * np.percentile(s['vol'], 5):.1f}-{100 * np.percentile(s['vol'], 95):.1f}",
           "sigma(r)/sigma(dv)": np.median(s["ratio"]), "R2 op nieuws": np.median(s["r2"]),
           "PD-helling (mediaan)": np.median(s["slope"]), "P(t < -2)": np.mean(s["t"] < -2)}
    for zeta, s in flow_sim.items()
}).T.rename_axis("zeta").round(3)
```

In de tabel stijgt de volatiliteit zoals de formule zegt, van 7,0% per jaar bij $\zeta = 5$ naar 13,4% bij $\zeta = 0{,}2$. Bij die lage elasticiteit is het rendement 1,9 keer zo beweeglijk als het nieuws, en voorspelt de prijs-dividendverhouding in 93% van de steekproeven significant. De simulatie geeft zo excess volatility en voorspelbaarheid tegelijk, zonder dat iemand zijn discontovoet verandert. In de figuur staat links de volatiliteit tegen de multiplier $1/\zeta$, en schuiven rechts de histogrammen van de $t$-waarde naar links naarmate $\zeta$ daalt.

```{code-cell} ipython3
:label: cel-inelastische-markten-flowsim
:tags: [hide-input]

inverse = 1 / np.array(ZETAS)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
vol = np.array([np.percentile(flow_sim[z]["vol"], [5, 50, 95]) for z in ZETAS])
grid_inv = np.linspace(0, 10.5, 200)
axes[0].fill_between(inverse, 100 * vol[:, 0], 100 * vol[:, 2], alpha=0.3, label="5e-95e percentiel")
axes[0].plot(inverse, 100 * vol[:, 1], "o", color=hap.plotting.COLORS[0], label="mediaan over steekproeven")
axes[0].plot(grid_inv, 200 * np.sqrt(SD_V**2 + var_dc * grid_inv**2), color="black", lw=1,
             label="theorie")
axes[0].set_title("Prijsvolatiliteit schaalt met $1/\\zeta$")
axes[0].set_xlabel("Inverse elasticiteit $1/\\zeta$ (= multiplier $M$)")
axes[0].set_ylabel("Volatiliteit van het rendement (% per jaar)")
axes[0].legend()
for i, z in enumerate([0.1, 0.2, 1.0]):
    axes[1].hist(flow_sim[z]["t"], bins=np.linspace(-7, 3, 51), histtype="step", lw=1.6,
                 color=hap.plotting.COLORS[i], label=f"$\\zeta$ = {z:g}")
axes[1].axvline(-2, color="black", lw=0.8, ls="--")
axes[1].set_title("Voorspelt de P/D-ratio rendementen? (100 jaar)")
axes[1].set_xlabel("$t$-waarde van de helling van $\\ell_{t+1}$ op de log P/D-ratio")
axes[1].set_ylabel("Aantal steekproeven")
axes[1].legend()
plt.show()
```

:::{figure} #cel-inelastische-markten-flowsim
:label: fig-inelastische-markten-flowsim
:width: 100%

Links volgt de volatiliteit de theorie, van de fundamentele 7% per jaar bij hoge
elasticiteit tot bijna 24% bij $\zeta = 0{,}1$. Rechts is de ware helling overal gelijk,
maar alleen bij een lage elasticiteit is ze in honderd jaar zichtbaar.
:::

De ware helling is overal $-(1-\phi) = -0{,}05$ per kwartaal, maar bij $\zeta = 1$ vindt maar 18% van de steekproeven ze. Net als bij [de standaardfout van 2%](#00-01-rendementen) is het effect er altijd, maar wordt het pas meetbaar als flows een groot deel van de variantie dragen. De volatiliteit meet bovendien $\Var(\Delta c)/\zeta^2$ en niet $\zeta$ zelf, zodat ze de elasticiteit niet identificeert.
::::

**Passief beleggen.** Met een aandeel $s_P$ van indexfondsen met elasticiteit nul en een
actieve rest met elasticiteit $\zeta_A$ is $\zeta = (1 - s_P)\zeta_A$. Een verschuiving
naar passief verlaagt de marktelasticiteit dus mechanisch, zoals in stap 5 van het
toy-voorbeeld. Eind 2019 bezaten indexfondsen al evenveel van de Amerikaanse beurs als
actieve fondsen {cite}`ICI2020`, zoals we in [](#04-25-industrie) zagen. Actieve beleggers
kunnen daarop agressiever gaan handelen, maar volgens {cite:t}`HaddadHuebnerLoualiche2025`
compenseren ze maar twee derde van het effect. De groei van passief maakte de vraag naar
individuele aandelen zo in twintig jaar 11 procent inelastischer.

**Inkoop van eigen aandelen.** Een onderneming die voor $\Delta F$ eigen aandelen inkoopt,
werkt in [](#eq-inelastische-markten-multiplier) als een instroom van $\Delta F$, zolang
de verkopers de opbrengst niet herbeleggen. De prijs per aandeel stijgt dan met $\Delta F/(\zeta E)$,
en de marktwaarde verandert met ongeveer $(1/\zeta - 1)\Delta F$. Bij oneindige
elasticiteit daalt de marktwaarde met de uitbetaling, zoals bij Miller en Modigliani
{cite}`MillerModigliani1961`, maar bij $\zeta = 0{,}2$ stijgt ze met $4\Delta F$.

**De tegenhanger.** Het klassieke tegenargument staat in [](#02-06-efficiente-markten) en
bij {cite:t}`GrossmanStiglitz1980`. Als flows prijzen van hun fundamentele waarde
wegduwen, loont het om geïnformeerd tegen die flows in te handelen, en juist die
handelaren maken de vraag elastisch. Een lage elasticiteit vraagt dus een verklaring
waarom zo weinig kapitaal die rol speelt. Kandidaten zijn de limits of arbitrage uit
[](#04-23-behavioral), de kapitaalbeperkingen van intermediairs uit
[](#05-32-intermediaries) en mandaten die ook professionals binden. De elasticiteit is
daarmee geen natuurconstante maar een uitkomst van het evenwicht.

```{admonition} Samengevat
:class: tip

- Een fonds met aandelenfractie $\theta$ heeft elasticiteit $1 - \theta$ ({prf:ref}`thm-inelastische-markten-mandaat`), dus een hogere $\theta$ maakt het fonds minder gevoelig voor de prijs.
- Een netto instroom verhoogt de prijs met $\Delta F/(\zeta E)$, dus $M = 1/\zeta$ ([](#eq-inelastische-markten-multiplier)), en een lagere $\zeta$ maakt koersen beweeglijker ([](#eq-inelastische-markten-volatiliteit)).
- Een mean-variance-belegger heeft $\zeta \approx 20$ ([](#eq-inelastische-markten-cara)), en een kleinere premie maakt hem nog elastischer.
- OLS van flows op prijzen gaat naar nul als gemeenschappelijke schokken domineren ([](#eq-inelastische-markten-ols-bias)), terwijl GIV $\zeta$ meet zolang $H > 1/N$.
- Met twintig Zipf-sectoren en even grote gemeenschappelijke en eigen schokken is de kansgrens van OLS 0,013 in plaats van 0,2, een schijnbare multiplier van bijna 80.
```

## Simulatie: de elasticiteit meten met OLS en GIV

Hoe dicht komen OLS en GIV bij de ware elasticiteit in een steekproef zo lang als die van
Gabaix en Koijen? We simuleren [](#eq-inelastische-markten-giv-model) met $\zeta = 0{,}2$,
de waarde uit het toy-voorbeeld, en dus met een ware multiplier van 5. Beide soorten
schokken hebben een standaarddeviatie van 1% per kwartaal. De sectoren zijn verdeeld
volgens Zipf ($S_i \propto 1/i$) of, ter vergelijking, bijna even groot ($S_i \propto i^{-0{,}1}$).
We variëren het aantal sectoren $N$ en het aantal kwartalen $T$, waarvan 104 de steekproef
van Gabaix en Koijen is.

```{code-cell} ipython3
def demean(a):
    """Subtract the time-series mean of each simulated sample."""
    return a - a.mean(axis=1, keepdims=True)


def simulate_giv(n_sim, T, N, zeta=0.2, sd_common=0.01, sd_idio=0.01, zipf=1.0):
    """OLS and GIV estimates of the elasticity in the granular flow model, one per simulated sample."""
    sizes = np.arange(1, N + 1, dtype=float) ** -zipf
    sizes /= sizes.sum()
    common = rng.normal(0.0, sd_common, (n_sim, T, 1))
    idio = rng.normal(0.0, sd_idio, (n_sim, T, N))
    price = (common[..., 0] + idio @ sizes) / zeta
    flows = -zeta * price[..., None] + common + idio
    flow_eq = flows.mean(axis=2)
    giv = flows @ sizes - flow_eq
    ols = -(demean(price) * demean(flow_eq)).sum(1) / (demean(price) ** 2).sum(1)
    iv = -(demean(giv) * demean(flow_eq)).sum(1) / (demean(giv) * demean(price)).sum(1)
    return ols, iv, (sizes**2).sum()


giv_rows, giv_draws = {}, {}
for T in (40, 104, 400):
    for N in (5, 20):
        for zipf in (1.0, 0.1):
            ols, iv, herfindahl = simulate_giv(4000, T, N, zipf=zipf)
            giv_draws[(T, N, zipf)] = (ols, iv)
            bias = 0.2 * (1 - (0.01**2 + 0.01**2 / N) / (0.01**2 + 0.01**2 * herfindahl))
            giv_rows[(T, N, "Zipf" if zipf == 1.0 else "bijna gelijk")] = {
                "H - 1/N": herfindahl - 1 / N, "OLS mediaan": np.median(ols), "OLS plim (formule)": bias,
                "GIV mediaan": np.median(iv),
                "GIV 5e-95e pct": f"{np.percentile(iv, 5):.2f} tot {np.percentile(iv, 95):.2f}",
                "P(3 < M < 8)": np.mean((iv > 1 / 8) & (iv < 1 / 3))}
pd.DataFrame(giv_rows).T.rename_axis(["T", "N", "groottes"]).round(3)
```

In de tabel ligt de mediaan van OLS bij elke $T$ en $N$ op de kansgrens uit
[](#eq-inelastische-markten-ols-bias), ongeveer 0,013 met Zipf-groottes en 0,0001 met
bijna gelijke sectoren. Meer data helpt dus niet, omdat het
om een vertekening gaat en niet om ruis. GIV heeft met Zipf-groottes een mediaan van 0,20
zodra $T \ge 104$, en het aantal sectoren maakt weinig uit, omdat $H - 1/N$ steeds
ongeveer even groot is. Met bijna gelijke sectoren is het instrument zwak. De mediaan zakt
dan naar 0,01 tot 0,07, en de multiplier valt in hoogstens een op de vijf steekproeven
tussen 3 en 8.

Links in de figuur is de afstand tussen de histogrammen van OLS en GIV de vertekening, en
rechts wordt de verdeling van de multiplier smaller naarmate $T$ groeit.

```{code-cell} ipython3
:label: cel-inelastische-markten-giv
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
bins = np.linspace(-0.3, 0.8, 56)
ols_104, iv_104 = giv_draws[(104, 20, 1.0)]
axes[0].hist(ols_104, bins=bins, alpha=0.6, label="OLS")
axes[0].hist(iv_104, bins=bins, alpha=0.6, label="GIV")
axes[0].axvline(0.2, color="black", lw=1.2, label="ware $\\zeta$ = 0,2")
axes[0].set_title("104 kwartalen, 20 sectoren (Zipf)")
axes[0].set_xlabel("Geschatte elasticiteit $\\hat\\zeta$")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].legend()
for i, T in enumerate((40, 104, 400)):
    implied = 1 / giv_draws[(T, 20, 1.0)][1]
    axes[1].hist(np.clip(implied, -5, 20), bins=np.linspace(-5, 20, 51), histtype="step", lw=1.6,
                 color=hap.plotting.COLORS[i], label=f"T = {T}")
axes[1].axvline(5, color="black", lw=1.2)
axes[1].set_title("Geïmpliceerde multiplier $1/\\hat\\zeta^{GIV}$ (afgekapt op -5 en 20)")
axes[1].set_xlabel("Multiplier $M$")
axes[1].set_ylabel("Aantal steekproeven")
axes[1].legend()
plt.show()
```

:::{figure} #cel-inelastische-markten-giv
:label: fig-inelastische-markten-giv
:width: 100%

Links ligt de OLS-schatter bij 104 kwartalen vlak bij nul, terwijl GIV rond de ware 0,2 ligt. Rechts is de multiplier uit GIV scheef verdeeld, vaak negatief of enorm bij 40 kwartalen en bijna altijd tussen 3 en 8 bij 400 kwartalen.
:::

Met 104 kwartalen ligt het 90%-interval van $\hat\zeta^{\mathrm{GIV}}$ tussen 0,12 en
0,51, een multiplier tussen ongeveer 2 en 8, en dat is ongeveer de spreiding van 3 tot 8
over de specificaties van Gabaix en Koijen. Hun vijf dollar is dus het midden van een
breed
interval, dat pas met 400 kwartalen krimpt tot 0,15 à 0,29.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Gabaix en Koijen, *In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis*, NBER-werkdocument 28967, 2021 {cite}`GabaixKoijen2021`. Voor het inclusie-effect Petajisto {cite}`Petajisto2011` en Greenwood en Sammon {cite}`GreenwoodSammon2025`.

**Wat.** De multiplier van de hele markt, 7,08 (standaardfout 1,86) en 5,28 (1,10) in tabel 2 van Gabaix en Koijen. Daarnaast het inclusie-effect van S&P 500-toevoegingen, volgens Petajisto 8,8% van aankondiging tot opname over 1990–2005 en volgens Greenwood en Sammon in het laatste decennium minder dan 1%.

**Data hier.** Netto aandelenaankopen per sector uit de Financial Accounts van de Federal Reserve via `hap.data.fred(...)`, met het marktrendement uit `hap.data.market_monthly()`. Voor de inclusies de dagkoersen van de 50 aandelen uit [](#02-07-event-studies) via `hap.data.yahoo(...)`, waarvan er veertien in de S&P 500 kwamen.

**Verschil met het origineel.** Gabaix en Koijen schatten met GIV op meer sectoren, terwijl wij gelijktijdige OLS-regressies doen, waarin flows ook op het rendement zelf reageren. Onze toevoegingen zijn grote, succesvolle aandelen (overlevenden), en we nemen aan dat elke aankondiging na sluiting kwam.

**Verwachte afwijking.** Het rendement moet een positieve helling hebben op de fondsaankopen, maar de grootte is geen causale multiplier. Een negatief aankondigingsrendement bij de inclusies wijst op een fout in de datering. Zonder Tesla hoort het inclusie-effect binnen twee standaardfouten van nul te liggen, dichter bij Greenwood en Sammon dan bij Petajisto.
```

### Netto aankopen en rendementen in de Financial Accounts

We lezen de netto aankopen per sector in als fractie van de marktwaarde, en tellen
beleggingsfondsen en ETF's op tot één reeks fondsaankopen.

```{code-cell} ipython3
FOF_SERIES = {
    "huishoudens": "HNOCESQ027S",
    "beleggingsfondsen": "BOGZ1FA653064100Q",
    "ETF's": "BOGZ1FA563064100Q",
    "pensioenfondsen": "BOGZ1FA593064105Q",
    "verzekeraars": "BOGZ1FA523064105Q",
    "buitenland": "ROWCEAQ027S",
    "uitgifte niet-fin. bedrijven": "NCBCEBQ027S",
    "alle sectoren": "BOGZ1FA893064105Q",
}
raw_flows = pd.concat({name: hap_data.fred(sid)[sid] for name, sid in FOF_SERIES.items()}, axis=1, sort=True)
market_value = hap_data.fred("BOGZ1LM893064105Q")["BOGZ1LM893064105Q"]
raw_flows.index = raw_flows.index + pd.offsets.QuarterEnd(0)          # FRED stamps the quarter start
market_value.index = market_value.index + pd.offsets.QuarterEnd(0)

# annual rate / 4 = flow in the quarter, as a fraction of the market value at the start of the quarter
flows = raw_flows.div(4 * market_value.shift(1), axis=0)
flows["fondsen"] = flows["beleggingsfondsen"] + flows["ETF's"]

monthly_market = hap_data.market_monthly()["Mkt"]
quarterly_return = ((1 + monthly_market).resample("QE").prod() - 1).where(
    monthly_market.resample("QE").count() == 3).rename("rendement")
panel = pd.concat([quarterly_return, flows], axis=1, sort=True).loc["1952-03-31":"2026-06-30"]
panel = panel.dropna(subset=["rendement", "fondsen"])

first_etf_quarter = panel.index[panel["ETF's"].ne(0).argmax()]
print(f"{panel.index[0]:%Y-%m} t/m {panel.index[-1]:%Y-%m}: {len(panel)} kwartalen; "
      f"eerste kwartaal met ETF-aankopen: {first_etf_quarter:%Y-%m}")
(100 * panel.drop(columns="rendement").describe().loc[["mean", "std", "min", "max"]]).T.round(3)
```

De steekproef telt 298 kwartalen, en de eerste ETF-aankopen vallen in 1993. Huishoudens
zijn in deze cijfers grotendeels de sluitpost, zodat hun reeks de meetfouten van de andere
sectoren erft. Daarna regresseren we het kwartaalrendement van de markt op elke reeks
afzonderlijk, met Newey-West-standaardfouten.

```{code-cell} ipython3
def flow_regression(frame, regressor, lags=4):
    """Contemporaneous regression of the quarterly market return on one flow series (Newey-West)."""
    fit = hap.newey_west(frame["rendement"], frame[[regressor]], lags=lags)
    used = frame[["rendement", regressor]].dropna()
    return {"helling": fit.params[regressor], "t (NW)": fit.tvalues[regressor], "R2": fit.rsquared,
            "sd flow (% MV)": 100 * used[regressor].std(), "kwartalen": int(fit.nobs),
            "vanaf": f"{used.index[0]:%Y}"}


regressors = ["fondsen", "beleggingsfondsen", "ETF's", "pensioenfondsen", "verzekeraars", "buitenland",
              "huishoudens", "uitgifte niet-fin. bedrijven", "alle sectoren"]
flow_table = pd.DataFrame({x: flow_regression(panel, x) for x in regressors}).T
flow_table.loc["fondsen, 1993-2018"] = flow_regression(panel.loc["1993":"2018"], "fondsen")
flow_table.loc["ETF's, 2000-2026"] = flow_regression(panel.loc["2000":], "ETF's")
flow_table.infer_objects().round(3)
```

De fondsaankopen hebben de duidelijkste positieve helling, en ook de beleggingsfondsen
afzonderlijk zijn significant. Pensioenfondsen
en verzekeraars hebben een negatieve, niet significante helling, wat past bij
herbalanceren tegen de markt in. De aankopen van alle sectoren samen, de totale
netto uitgifte, verklaren niets ($t = 1{,}0$). Links in de figuur staat de puntenwolk met
de stippellijn van helling 5 ernaast, en rechts volgen de netto aankopen per sector in de
tijd, zodat te zien is welke sectoren kopen als andere verkopen.

```{code-cell} ipython3
:label: cel-inelastische-markten-fof
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ok = panel[["fondsen", "rendement"]].dropna()
axes[0].scatter(100 * ok["fondsen"], 100 * ok["rendement"], s=14, alpha=0.6)
slope, intercept = np.polyfit(ok["fondsen"], ok["rendement"], 1)
grid_f = np.linspace(ok["fondsen"].min(), ok["fondsen"].max(), 50)
axes[0].plot(100 * grid_f, 100 * (intercept + slope * grid_f), color="black", lw=1.2,
             label=f"OLS, helling {slope:.1f}")
axes[0].plot(100 * grid_f, 100 * (ok["rendement"].mean() + 5 * (grid_f - ok["fondsen"].mean())),
             color=hap.plotting.COLORS[1], ls="--", lw=1.2, label="helling 5 (Gabaix-Koijen)")
axes[0].set_title("Kwartaalrendement tegen netto aankopen door fondsen")
axes[0].set_xlabel("Netto aankopen beleggingsfondsen + ETF's (% van de marktwaarde)")
axes[0].set_ylabel("Rendement van de markt (%)")
axes[0].legend()
for i, name in enumerate(["fondsen", "pensioenfondsen", "buitenland", "huishoudens", "uitgifte niet-fin. bedrijven"]):
    axes[1].plot(panel.index, 100 * panel[name].rolling(4).sum(), color=hap.plotting.COLORS[i], lw=1.2, label=name)
axes[1].axhline(0, color="black", lw=0.6)
axes[1].set_title("Netto aankopen per sector, voortschrijdend over vier kwartalen")
axes[1].set_xlabel("Jaar")
axes[1].set_ylabel("% van de marktwaarde per jaar")
axes[1].legend()
plt.show()
```

Links is de OLS-lijn steiler dan de lijn met helling 5, maar de punten liggen er breed
omheen. Rechts nemen de fondsen vanaf de jaren negentig de rol van koper over van de
pensioenfondsen, die tot de jaren tachtig kochten en daarna per saldo verkopen. Sinds de
jaren tachtig kopen ook ondernemingen per saldo eigen aandelen in, terwijl huishoudens
meestal verkopen. De tabel zet onze hellingen naast de schattingen van Gabaix en Koijen.

| | Gabaix en Koijen (GIV) | hier (OLS op fondsaankopen) |
|---|---|---|
| 1993–2018 | 5,28 (SE 1,10) en 7,08 (SE 1,86) | 16,4 ($t = 3{,}6$) |
| 1952–2026 | – | 7,3 ($t = 2{,}8$), $R^2$ = 3% |

Gedeeltelijk geslaagd. Het teken is positief, zoals we vooraf verwachtten, maar de helling
hangt af van de periode, van 7,3 over alle jaren tot 16,4 over die van Gabaix en Koijen.
Een OLS-helling van 7 of 16 is bovendien geen multiplier,
omdat fondsflows ook op het rendement zelf reageren, zoals oefening 3 laat zien.

### Veertien S&P 500-toevoegingen

De gepubliceerde inclusie-effecten zijn in de loop van de tijd gekrompen, zoals de
gemiddelden in de tabel laten zien, al meet elke studie over een ander venster.

```{code-cell} ipython3
published_index_effect = pd.DataFrame(
    [["Shleifer (1986), volgens Petajisto (2011)", "1976-1983", "S&P 500", "aankondiging", 3.0],
     ["Petajisto (2011), tabel 1", "1990-2000", "S&P 500", "aankondiging tot opname", 10.3],
     ["Petajisto (2011), tabel 1", "2001-2005", "S&P 500", "aankondiging tot opname", 4.6],
     ["Greenwood-Sammon (werkversie 2022)", "1980-1989", "S&P 500", "dag voor aankondiging tot dag na opname", 3.42],
     ["Greenwood-Sammon (werkversie 2022)", "1990-1999", "S&P 500", "dag voor aankondiging tot dag na opname", 7.6],
     ["Greenwood-Sammon (werkversie 2022)", "2000-2009", "S&P 500", "dag voor aankondiging tot dag na opname", 5.21],
     ["Greenwood-Sammon (werkversie 2022)", "2010-2020", "S&P 500", "dag voor aankondiging tot dag na opname", 0.8],
     ["Chang-Hong-Liskovich (werkversie 2013)", "1996-2012", "Russell 2000", "junirendement na herindeling", 5.0]],
    columns=["bron", "periode", "index", "venster", "gem. rendement toevoeging (%)"],
)
published_index_effect
```

Het effect groeit tot in de jaren negentig en verdwijnt daarna bijna. De decenniagetallen
van Greenwood en Sammon komen uit hun NBER-werkversie (w30748, 2022), en de gepubliceerde
versie noemt 7,4% voor de jaren negentig. Chang, Hong en Liskovich vergelijken aandelen
vlak boven en vlak onder de grens tussen de Russell 1000 en de Russell 2000, waar veel
meer indexgeld volgt. Die *regression discontinuity* (een vergelijking rond een grens) is
de schoonste meting van een vraagcurve die we hebben.

Nu berekenen we het abnormale rendement, het rendement min dat van de markt, voor de
veertien aandelen uit [](#02-07-event-studies) die tussen 2012 en 2024 werden toegevoegd.

```{code-cell} ipython3
EVENT_TICKERS = ["AAPL", "ADBE", "AMZN", "ANET", "APH", "AVGO", "BAC", "BRK-B", "CMG", "CPRT", "CRM", "CSX",
                 "CTAS", "CVX", "DE", "DHR", "DXCM", "EW", "FAST", "FTNT", "GILD", "GOOGL", "IDXX", "ISRG",
                 "KO", "LRCX", "MA", "MNST", "NFLX", "NKE", "NOW", "NVDA", "ODFL", "ORLY", "PANW", "PG",
                 "QCOM", "ROST", "SBUX", "SHW", "SMCI", "TJX", "TSCO", "TSLA", "UNH", "UNP", "V", "WFC",
                 "WMT", "WRB"]
# S&P Dow Jones Indices press releases: (announcement date, first trading day as a constituent)
INCLUSIONS = {
    "MNST": ("2012-06-21", "2012-06-29"), "TSCO": ("2014-01-16", "2014-01-24"),
    "AVGO": ("2014-05-05", "2014-05-08"), "IDXX": ("2017-01-03", "2017-01-05"),
    "CPRT": ("2018-06-25", "2018-07-02"), "ANET": ("2018-08-23", "2018-08-28"),
    "FTNT": ("2018-10-04", "2018-10-11"), "NOW": ("2019-11-19", "2019-11-21"),
    "WRB": ("2019-11-27", "2019-12-05"), "ODFL": ("2019-12-02", "2019-12-09"),
    "DXCM": ("2020-05-06", "2020-05-12"), "TSLA": ("2020-11-16", "2020-12-21"),
    "PANW": ("2023-06-02", "2023-06-20"), "SMCI": ("2024-03-01", "2024-03-18"),
}

prices_daily = hap_data.yahoo(EVENT_TICKERS, start="2002-01-01", end="2026-08-01")
market_daily = hap_data.market_daily()["Mkt"]
common_days = prices_daily.index.intersection(market_daily.index)
abnormal = prices_daily.pct_change(fill_method=None).loc[common_days].sub(market_daily.loc[common_days], axis=0)

event_rows = {}
for ticker, (announced, effective) in INCLUSIONS.items():
    day_one = common_days.searchsorted(pd.Timestamp(announced), side="right")   # announced after the close
    day_effective = common_days.searchsorted(pd.Timestamp(effective))
    ar = abnormal[ticker].to_numpy()
    event_rows[ticker] = {"aankondiging": announced, "opname": effective,
                          "handelsdagen tot opname": day_effective - day_one,
                          "AR dag +1 (%)": 100 * ar[day_one],
                          "CAR tot opname (%)": 100 * ar[day_one:day_effective].sum(),
                          "CAR 20 dagen vanaf opname (%)": 100 * ar[day_effective:day_effective + 20].sum()}
event_table = pd.DataFrame(event_rows).T
event_table.round(2)
```

Tesla springt eruit met 51% van aankondiging tot opname, over 23 handelsdagen. Daarom
vatten we de drie vensters samen over alle veertien aandelen en over de dertien zonder
Tesla.

```{code-cell} ipython3
def event_summary(frame):
    """Cross-sectional mean, standard error, t-value and median of event returns."""
    se = frame.std(ddof=1) / np.sqrt(len(frame))
    return pd.DataFrame({"gemiddelde": frame.mean(), "SE": se, "t": frame.mean() / se, "mediaan": frame.median()})


event_returns = event_table[["AR dag +1 (%)", "CAR tot opname (%)", "CAR 20 dagen vanaf opname (%)"]].astype(float)
pd.concat({"alle 14": event_summary(event_returns),
           "zonder Tesla": event_summary(event_returns.drop("TSLA"))}).round(2)
```

Op de eerste handelsdag na de aankondiging is het abnormale rendement gemiddeld 3,1%, en
zonder Tesla loopt het in de twintig dagen na opname deels terug, al is die daling niet
significant.
De tabel zet het rendement van aankondiging tot opname naast de gepubliceerde getallen.

| | periode | aankondiging tot opname (%) | SE |
|---|---|---|---|
| Petajisto (2011) | 1990–2005 | 8,8 | – |
| Greenwood en Sammon (werkversie) | 2010–2020 | 0,8 | – |
| hier, alle veertien | 2012–2024 | 5,7 | 4,0 |
| hier, zonder Tesla | 2012–2024 | 2,2 | 2,2 |

Geslaagd wat het teken en het ontbreken van een groot effect betreft, maar een multiplier
levert deze proef niet op. Het aankondigingsrendement is positief, en zonder Tesla ligt het
rendement tot
opname op één standaardfout van nul, dichter bij Greenwood en Sammon dan bij Petajisto.
Met veertien gebeurtenissen is de standaardfout wel zo groot als het effect dat de
literatuur zoekt. Dat het effect verdween terwijl het indexgeld sterk groeide
{cite}`GreenwoodSammon2025`, is zelf een puzzel voor de hypothese van inelastische
markten.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Eén parameter, de elasticiteit van de vraag, verbindt feiten
die elk een eigen verklaring hadden. Inclusies verhogen prijzen zonder nieuws, van
Shleifers eerste metingen tot de regression discontinuity van Chang, Hong en Liskovich.
Flows op een inelastische markt maken excess volatility en voorspelbaarheid tegelijk,
zonder dat iemand zijn discontovoet verandert. Ook passief beleggen en
inkoop van eigen aandelen krijgen een prijseffect dat de standaardtheorie niet kent.

**Waar het breekt.** Het model breekt op de meting. Een gewone regressie laat de vraag
extreem inelastisch lijken, en zelfs GIV geeft met een kwart eeuw kwartaaldata een
multiplier die ergens tussen 2 en 8 ligt. Onze OLS-helling op fondsflows ligt tussen 7 en
16, maar
is geen multiplier, omdat flows ook op rendementen reageren. Het schoonste natuurlijke
experiment
wijst bovendien de verkeerde kant op. Het inclusie-effect verdween terwijl het indexgeld
groeide, en onze toevoegingen zonder Tesla geven 2,2% met een even grote standaardfout.

**Risico of vergissing?** In de Chicago-lezing is een flow een verandering in iemands
risicobereidheid of verwachtingen, dus een discontovoetschok onder een andere naam. De
multiplier meet dan hoe schaars risicodragend kapitaal is, zoals bij de intermediairs van
[](#05-32-intermediaries), en mandaten zijn een rationele institutionele keuze. In de
Yale-lezing bewegen prijzen om redenen buiten de fundamentele waarde, en zijn inelastische
markten de limits of arbitrage van [](#04-23-behavioral) op de schaal van de hele markt.
Posities en flows van de beleggers die de prijs zetten, met instrumenten voor hun eigen
schokken, zouden de lezingen kunnen scheiden. Die gegevens bestaan echter alleen voor
instellingen. Voor een belegger die tegen een flow in koopt, blijft dus open of hij een
risicopremie verdient of iets denkt te weten wat de prijs niet weet.

**Wat er daarna kwam.** Als flows het niveau van de markt zetten en indexfondsen niet op
informatie handelen, wie maakt prijzen dan nog informatief? Santa-Clara vermoedt dat
machines de markt als geheel niet efficiënter maken, omdat dat niveau wordt gezet door
flows op een inelastische markt {cite}`SantaClara2026`. Wat taalmodellen dan wel met
prijzen doen, onderzoekt [](#07-37-llms-en-efficientie).

## Oefeningen

:::{exercise}
:label: ex-inelastische-markten-1

**Passief, strategische reactie en inkoop van eigen aandelen.** Een markt bestaat uit indexfondsen met elasticiteit nul en actieve beleggers met elasticiteit $\zeta_A = 1$. Het is stap 5 van het toy-voorbeeld met andere getallen.

1. Geef de marktelasticiteit en de multiplier als functie van het passieve aandeel $s_P$, en bereken ze voor $s_P = 0{,}2$ en $s_P = 0{,}5$.
2. De actieve beleggers compenseren twee derde van de daling in de marktelasticiteit bij de verschuiving van 0,2 naar 0,5, zoals Haddad, Huebner en Loualiche schatten. Welke $\zeta_A$ en welke multiplier horen daarbij?
3. Een onderneming koopt voor 1% van de marktwaarde eigen aandelen in, en de verkopers houden de opbrengst in kas. Hoeveel veranderen de prijs per aandeel en de marktwaarde in de markt uit (2), en bij $\zeta = 20$?
:::

:::{solution} ex-inelastische-markten-1
:class: dropdown

**(1)** Met [](#eq-inelastische-markten-multiplier) is $\zeta = (1 - s_P)\zeta_A$ en $M = 1/((1 - s_P)\zeta_A)$. Bij $s_P = 0{,}2$ is $\zeta = 0{,}8$ en $M = 1{,}25$, en bij $s_P = 0{,}5$ is $\zeta = 0{,}5$ en $M = 2$.

**(2)** Zonder reactie zou $\zeta$ met 0,3 dalen. Wordt twee derde daarvan gecompenseerd, dan daalt ze maar met 0,1 tot 0,7. Dan is $\zeta_A = 0{,}7/0{,}5 = 1{,}4$ en $M = 1/0{,}7 = 1{,}43$.

**(3)** De inkoop werkt als een instroom van 1% van de marktwaarde, zodat de prijs per aandeel met $1\%/\zeta$ stijgt en de marktwaarde met $(1/\zeta - 1) \times 1\%$ verandert. De code rekent de drie antwoorden na.

```{code-cell} ipython3
def passive_market(s_passive, zeta_active):
    """Aggregate elasticity and multiplier with zero-elasticity index funds."""
    zeta = (1 - s_passive) * zeta_active
    return zeta, 1 / zeta


print("s_P = 0.2:", passive_market(0.2, 1.0), " s_P = 0.5:", passive_market(0.5, 1.0))
zeta_after = passive_market(0.2, 1.0)[0] - (1 / 3) * (passive_market(0.2, 1.0)[0] - passive_market(0.5, 1.0)[0])
zeta_active_new = zeta_after / 0.5
print(f"met strategische reactie: zeta_A = {zeta_active_new:.2f}, M = {1 / zeta_after:.3f}")
for zeta in (zeta_after, 20.0):
    print(f"zeta = {zeta:5.2f}: prijs per aandeel +{1 / zeta:.3f}%, marktwaarde {1 / zeta - 1:+.3f}% van de marktwaarde")
```

In de markt uit (2) stijgen de prijs per aandeel en de marktwaarde met 1,43% en 0,43%, hoewel er 1% is uitgekeerd. Bij $\zeta = 20$ stijgt de prijs met 0,05% en daalt de marktwaarde met 0,95%. De strategische reactie dempt het effect van passief dus maar heft het niet op, en of inkoop waarde creëert, hangt in een inelastische markt af van de elasticiteit.
:::

:::{exercise}
:label: ex-inelastische-markten-2

**Hoeveel data heeft GIV nodig?**

1. Laat met de notatie van {prf:ref}`thm-inelastische-markten-giv` zien dat de standaardfout van $\hat\zeta^{\mathrm{GIV}}$ in grote steekproeven ongeveer $\zeta\sqrt{\sigma_\eta^2 + \sigma_u^2/N}\,/\,\big(\sigma_u\sqrt{(H - 1/N)\,T}\big)$ is.
2. Bereken die standaardfout voor $\zeta = 0{,}2$, $N = 20$ met Zipf-groottes, $\sigma_\eta = 1\%$ en $\sigma_u \in \{0{,}5\%;\ 1\%;\ 2\%\}$, bij $T = 104$, en vergelijk met de spreiding van `simulate_giv`.
3. Welke $T$ is bij elke $\sigma_u$ nodig voor een standaardfout van 0,05? Wat zegt dat over waar GIV zijn informatie vandaan haalt?
:::

:::{solution} ex-inelastische-markten-2
:class: dropdown

**(1)** Uit het bewijs van {prf:ref}`thm-inelastische-markten-giv` volgt $\hat\zeta^{\mathrm{GIV}} - \zeta = -\widehat{\Cov}(z, \eta + u_E)/\widehat{\Cov}(z, p)$. De teller heeft verwachting nul en, omdat $z$ onafhankelijk is van $\eta + u_E$, variantie $\Var(z)\Var(\eta + u_E)/T$, met $\Var(z) = \Var(u_S - u_E) = \sigma_u^2(H - 2/N + 1/N) = \sigma_u^2(H - 1/N)$ en $\Var(\eta + u_E) = \sigma_\eta^2 + \sigma_u^2/N$. De noemer convergeert naar $\sigma_u^2(H - 1/N)/\zeta$, en delen geeft de formule.

**(2) en (3)** De cel berekent de formule en zet de uitkomst naast de robuuste spreiding van de simulatie.

```{code-cell} ipython3
sizes_20 = 1 / np.arange(1, 21)
sizes_20 /= sizes_20.sum()
excess_h = (sizes_20**2).sum() - 1 / 20
rows_se = {}
for sd_idio in (0.005, 0.01, 0.02):
    se_formula = 0.2 * np.sqrt(0.01**2 + sd_idio**2 / 20) / (sd_idio * np.sqrt(excess_h * 104))
    _, iv_draws, _ = simulate_giv(4000, 104, 20, sd_idio=sd_idio)
    q25, q75 = np.percentile(iv_draws, [25, 75])
    rows_se[sd_idio] = {"SE formule (T=104)": se_formula, "IQR/1.349 simulatie": (q75 - q25) / 1.349,
                        "T voor SE = 0.05": int(np.ceil(104 * (se_formula / 0.05) ** 2))}
pd.DataFrame(rows_se).T.rename_axis("sigma_u").round(3)
```

Formule en simulatie liggen dicht bij elkaar. We gebruiken de interkwartielafstand gedeeld door 1,349, omdat een verhouding van twee schattingen dikke staarten heeft. Bij $\sigma_u = 1\%$ zijn ongeveer 230 kwartalen nodig, bijna zestig jaar, en bij grotere idiosyncratische schokken veel minder. GIV haalt zijn informatie dus uit de eigen schokken van grote spelers, die niet met de gemeenschappelijke vraag samenhangen.
:::

:::{exercise}
:label: ex-inelastische-markten-3

**Wie reageert op wie?** Gebruik `panel` uit de replicatie. Het bevat de fondsflows en het marktrendement per kwartaal.

1. Regresseer de fondsflows op het rendement van het vorige kwartaal, en het rendement op de fondsflows van het vorige kwartaal (Newey-West, vier lags).
2. Voeg aan de gelijktijdige regressie de flow van het vorige kwartaal toe.
3. Wat zeggen (1) en (2) over de causale lezing van de replicatie?
:::

:::{solution} ex-inelastische-markten-3
:class: dropdown

De cel schat de drie regressies met Newey-West-standaardfouten.

```{code-cell} ipython3
lead_lag = panel[["rendement", "fondsen"]].assign(
    rendement_vorig=panel["rendement"].shift(1), fondsen_vorig=panel["fondsen"].shift(1))
specs_ll = {"fondsen op rendement vorig kwartaal": ("fondsen", ["rendement_vorig"]),
            "rendement op fondsen vorig kwartaal": ("rendement", ["fondsen_vorig"]),
            "rendement op fondsen + fondsen vorig": ("rendement", ["fondsen", "fondsen_vorig"])}
rows_ll = {}
for label, (y, xs) in specs_ll.items():
    fit = hap.newey_west(lead_lag[y], lead_lag[xs], lags=4)
    rows_ll[label] = {**{f"b({x})": fit.params[x] for x in xs}, **{f"t({x})": fit.tvalues[x] for x in xs},
                      "R2": fit.rsquared, "N": int(fit.nobs)}
pd.DataFrame(rows_ll).T.round(3)
```

Fondsflows volgen het rendement van het vorige kwartaal ($t = 2{,}1$). Met de vorige flow erbij stijgt de gelijktijdige helling naar 14,0, en is die van de vorige flow $-10{,}5$ ($t = -3{,}0$). Dat past bij prijsdruk die deels terugloopt, maar ook bij flows die rendementen najagen. OLS scheidt die twee lezingen niet, en daarvoor is een instrument als GIV nodig.
:::
