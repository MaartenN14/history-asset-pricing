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

(05-30-wisselkoersen)=

# Wisselkoersen: risk sharing, carry, momentum, value

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** Het college loopt van de toetsen van Hansen en Hodrick (1980) en Fama (1984) tot
de valutaportefeuilles van Barroso en Santa-Clara (2015).

**Wat we al weten.** Elk prijsmodel is een uitspraak over een *stochastische discontofactor*
(SDF, de toestandsafhankelijke weging $m$ in $p_t = \E_t[m_{t+1}x_{t+1}]$). Volgens de
Hansen-Jagannathan-grens uit [](#03-13-equity-premium-puzzle) is die SDF minstens zo
volatiel als de hoogste Sharpe-ratio, ongeveer een half per jaar. In
[](#05-29-opties-crashrisico) verdienden strategieën die crashrisico verkopen een premie,
betaald met zeldzame grote verliezen.

**Welke vraag staat open.** Wat zeggen wisselkoersen over het samen bewegen van marginaal nut
in verschillende landen? En is de winst op lenen tegen een lage rente en beleggen tegen een
hoge rente een beloning voor risico, of een vergissing?
```

## Overzicht

Wat vertellen wisselkoersen over de SDF's van twee landen? Een wisselkoers is de verhouding
van die twee SDF's, zodat gladde wisselkoersen betekenen dat marginaal nut in landen bijna
gelijk op beweegt, en een renteverschil zonder bijbehorende depreciatie een risicopremie is.
In dit college:

- leiden we af dat de wisselkoersverandering het verschil is van twee log-SDF's, en wat dat
  zegt over internationale risk sharing;
- leiden we uit dezelfde identiteit de UIP-regressie van Fama af, en een carry-premie voor
  de
  munt van het land met de rustigste SDF;
- simuleren we hoe onzeker de ondergrens voor risk sharing is als de Sharpe-ratio geschat
  moet
  worden;
- repliceren we voor negen G10-valuta's de Fama-regressie, de carry-portefeuilles met hun
  crash
  van 2008, de index van Brandt, Cochrane en Santa-Clara, en kort momentum en value.

Dat de wisselkoers de verhouding van twee SDF's is, lieten Bekaert en Backus, Foresi en
Telmer
zien {cite}`Bekaert1996,BackusForesiTelmer2001`. Brandt, Cochrane en Santa-Clara maakten
er in 2006 een meetinstrument van {cite}`BrandtCochraneSantaClara2006`, zodat twee
standaarddeviaties, die van de wisselkoers en die van de SDF, volstaan om de oude macrovraag
te beantwoorden of landen hun risico delen. De
*uncovered interest
parity* (UIP, ongedekte rentepariteit: de verwachte depreciatie van een valuta is gelijk aan
het renteverschil) was toen al lang verworpen, meestal met het verkeerde teken
{cite}`HansenHodrick1980,Fama1984`. Daardoor is de *carry trade* (lenen in een valuta met
lage rente, beleggen in een valuta met hoge rente) winstgevend. Zo werd een verworpen
theorie een vast feit waarvoor pas achteraf verklaringen werden gezocht, en bij carry ging
het feit dus zuiver aan de theorie vooraf. Die verklaringen zijn consumptierisico
{cite}`LustigVerdelhan2007`, een
gemeenschappelijke factor {cite}`LustigRoussanovVerdelhan2011`, volatiliteitsrisico
{cite}`MenkhoffSarnoSchmelingSchrimpf2012a`, crashrisico
{cite}`BrunnermeierNagelPedersen2008`
en peso problems {cite}`BurnsideEichenbaumKleshchelskiRebelo2011`. Barroso en Santa-Clara
voegden momentum en value toe en vroegen welke combinatie een belegger zou moeten aanhouden
{cite}`BarrosoSantaClara2015b`.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een Amerikaanse en een Zwitserse belegger. Een SDF is een lijst van waarderingen,
namelijk hoeveel een extra eenheid van de eigen munt in elke toekomstige toestand waard is.
Stel dat het de Amerikaanse economie in een bepaalde toestand slecht gaat, terwijl het in
Zwitserland meevalt. Een dollar is dan voor de Amerikaan veel waard en een frank voor de
Zwitser niet bijzonder, zodat de dollar in die toestand duurder wordt ten opzichte van de
frank. De wisselkoers beweegt dus met het verschil tussen hoe hard de twee beleggers hun
eigen
munt nodig hebben.

Hoe sterk die samenhang moet zijn, volgt uit een telling. Om een Sharpe-ratio van een half
te verklaren, moet marginaal nut in elk land met minstens de helft per jaar schommelen. De
koers van de dollar tegenover de frank
beweegt echter maar met ongeveer tien procent per jaar. Twee grootheden die elk met vijftig
procent schommelen en waarvan het verschil met tien procent schommelt, moeten vrijwel altijd
samen bewegen. Als landen hun risico's slecht deelden, zouden wisselkoersen zeven keer zo
volatiel zijn. Consumptiegroei is tussen landen toch maar matig gecorreleerd, dus ofwel
meet consumptie marginaal nut slecht, ofwel zijn wisselkoersen te glad.

Bij de rente gaat het leerboek ook mis. Als de Australische rente vier procent hoger is
dan de
Japanse, zou de Australische dollar volgens UIP vier procent per jaar moeten dalen. In de
data
daalt hij gemiddeld veel minder, of stijgt hij zelfs. Een belegger die in yen leent en in
Australische dollars belegt, verdient daardoor het renteverschil en houdt het meestal.

Toch is dat geen gratis geld. Hoge-rentevaluta's horen bij landen waar weinig uit voorzorg
wordt gespaard, terwijl yen en frank als toevluchtsoord dienen. In een wereldwijde paniek,
zoals
in oktober 2008, stijgen yen en frank en vallen de Australische en de Nieuw-Zeelandse
dollar.
Handelaren zeggen dat valuta's met de trap omhoog gaan en met de lift omlaag. Een
strategie die
juist in de slechtste tijden verliest, draagt risico waarvoor een SDF een hoge premie
vraagt.
Maar als dertig jaar data geen crash bevatten, lijkt dezelfde strategie gratis geld. Dat
heet
een *peso problem* (risico dat wel in de prijzen zit maar niet in de steekproef).

Zo komen we bij risico of vergissing, een vraag die Santa-Clara zo stelt: draagt
de
belegger risico waarvoor een premie wordt betaald, of denkt hij iets te weten wat de prijs
niet weet {cite}`SantaClara2026`? Als het risico is, verwachten we twee dingen. De munt
van het land met het rustigste marginale nut heeft de hoogste rente en levert een premie
op, en die premie gaat juist in crises verloren, zodat het carry-rendement links scheef
verdeeld is.

## Toy-voorbeeld: twee landen, twee toestanden

Eerst laden we de bibliotheken die het hele college gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** Er zijn twee toestanden op $t+1$, elk met kans $\tfrac12$. De Amerikaanse SDF $m$
waardeert payoffs in dollars en de Zwitserse SDF $m^*$ payoffs in franken:

| toestand | kans | $m$ (dollar) | $m^*$ (frank) |
|---|---|---|---|
| goed   | 0{,}5 | 0{,}80 | 0{,}88 |
| slecht | 0{,}5 | 1{,}20 | 1{,}08 |

**Het recept.** Laat $S_t$ de dollarprijs van één frank zijn. De wisselkoers is de
verhouding van de twee SDF's, zodat $S_{t+1}/S_t = m^*/m$ in elke toestand. Dat is de enige
formule die de theorie pas later afleidt, want de premieformule in stap 5 kennen we al en de
index in stap 6 is een definitie.

1. *Rentes.* $R^f = 1/\E[m] = 1/1{,}00 = 1{,}00$ en $R^{f*} = 1/\E[m^*] = 1/0{,}98 = 1{,}0204$
   ($R^f$ staat in dit college kortheidshalve voor het bruto risicovrije rendement, $1 + R^f$
   in de notatie van de setup).
   De Zwitserse $\E[m^*]$ is hier lager gekozen, zodat het land met de rustigere SDF ook de
   hogere rente heeft. Of dat in het algemeen zo is, bepaalt in de theorie de parameter $b$.
2. *Wisselkoers.* $S_{t+1}/S_t$ is $0{,}88/0{,}80 = 1{,}10$ in de goede en $1{,}08/1{,}20 =
   0{,}90$ in de slechte toestand, dus de frank stijgt als het goed gaat en daalt als het slecht
   gaat.
3. *Controle.* Een dollar in de frankobligatie levert $R^{f*}S_{t+1}/S_t$ op, dat is
   $1{,}1224$
   of $0{,}9184$ dollar. De Amerikaanse SDF waardeert dat op
   $\tfrac12(0{,}80 \cdot 1{,}1224 + 1{,}20 \cdot 0{,}9184) = 1{,}0000$ dollar.
4. *UIP en carry.* De frank stijgt gemiddeld niet, want $\tfrac12(1{,}10 + 0{,}90) = 1{,}00$,
   terwijl UIP een daling tot $R^f/R^{f*} = 0{,}98$ voorspelt. Een dollar lenen en in de
   frankobligatie beleggen levert daardoor $+12{,}24\%$ of $-8{,}16\%$ op, gemiddeld
   $+2{,}04\%$.
5. *Premie.* Een premie is min de covariantie met $m$, gedeeld door $\E[m]$. De afwijkingen
   zijn $\mp 0{,}20$ voor $m$ en $\pm 0{,}102$ voor het carry-rendement, zodat $\Cov = -0{,}0204$
   en
   de premie $0{,}0204$ is, het hele renteverschil.
6. *Risk sharing.* Omdat $\Delta s = \log m^* - \log m$, is $\Var(\Delta s)$ de som van de
   twee log-SDF-varianties min twee keer hun covariantie. Brandt, Cochrane en Santa-Clara
   definiëren de risk-sharing-index als het deel van die som dat de covariantie wegwerkt.
   Met standaarddeviaties $0{,}2027$, $0{,}1024$ en $0{,}1003$ is dat
   $1 - 0{,}01007/(0{,}04110 + 0{,}01049) = 0{,}8048$.

De twee log-SDF's zijn hier perfect gecorreleerd, maar de index blijft onder één omdat hij
ook een verschil in grootte bestraft. De cel hieronder rekent dezelfde getallen na.

```{code-cell} ipython3
prob = np.array([0.5, 0.5])
m_home = np.array([0.80, 1.20])        # US SDF, values dollar payoffs
m_foreign = np.array([0.88, 1.08])     # Swiss SDF, values franc payoffs


def pvar(x):
    """Population variance under the state probabilities."""
    return prob @ (x - prob @ x) ** 2


Rf, Rf_star = 1 / (prob @ m_home), 1 / (prob @ m_foreign)
fx_growth = m_foreign / m_home                          # S_{t+1} / S_t
carry_payoff = Rf_star * fx_growth                      # dollars per dollar in the franc bill
carry_excess = carry_payoff - Rf
log_m, log_m_star, ds_toy = np.log(m_home), np.log(m_foreign), np.log(fx_growth)

code = pd.Series({
    "R^f": Rf, "R^f*": Rf_star,
    "S'/S goed": fx_growth[0], "S'/S slecht": fx_growth[1],
    "prijs frankbelegging": prob @ (m_home * carry_payoff),
    "E[S'/S]": prob @ fx_growth, "UIP-voorspelling R^f/R^f*": Rf / Rf_star,
    "carry goed": carry_excess[0], "carry slecht": carry_excess[1], "E[carry]": prob @ carry_excess,
    "SD log m": np.sqrt(pvar(log_m)), "SD log m*": np.sqrt(pvar(log_m_star)),
    "SD ds": np.sqrt(pvar(ds_toy)),
    "risk-sharing-index": 1 - pvar(ds_toy) / (pvar(log_m) + pvar(log_m_star)),
})
hand = pd.Series([1.00, 1.0204, 1.10, 0.90, 1.00, 1.00, 0.98, 0.1224, -0.0816, 0.0204,
                  0.2027, 0.1024, 0.1003, 0.8048], index=code.index)
pd.DataFrame({"met de hand": hand, "code": code}).round(4)
```

De twee kolommen zijn gelijk. Een frank die in slechte tijden daalt, is voor een Amerikaan
dus
riskant en levert het hele renteverschil als premie op. Een wisselkoers die met tien procent
schommelt, geeft naast SDF's van tien en twintig procent al een index van 0,8048.

## Theorie

De theorie volgt uit één identiteit, namelijk dat de wisselkoers de verhouding van twee
SDF's
is. Daaruit volgen twee voorspellingen. Bij gladde wisselkoersen moeten de SDF's van landen
sterk samenbewegen, en de munt van een land met rustig marginaal nut levert een premie op.
Daarna zien we hoe de UIP-regressie die premie meet, en wat de literatuur over carry,
crashes,
momentum en value vond.

### Opzet en notatie

Het binnenland is de VS, en $S_t$ is de dollarprijs van één eenheid buitenlandse munt. Met
$s_t = \log S_t$ betekent een positieve $\Delta s_{t+1}$ dat de buitenlandse munt stijgt, en
bij de G10-valuta's schommelt $\Delta s$ met zeven tot twaalf procent per jaar. De SDF
$m_{t+1}$ waardeert dollarpayoffs en $m^*_{t+1}$ payoffs in buitenlandse munt, waarbij de
ster
"buitenland" betekent en niet "optimaal". De log risicovrije rentes $i_t$ en $i^*_t$ voldoen
aan $e^{i_t} = 1/\E_t[m_{t+1}]$ en $e^{i^*_t} = 1/\E_t[m^*_{t+1}]$. Wie dollars leent en één
periode in de buitenlandse obligatie belegt, verdient het log overrendement

```{math}
:label: eq-wisselkoersen-rx
rx_{t+1} = i^*_t - i_t + \Delta s_{t+1} .
```

Dat rendement is het renteverschil plus de koerswinst op de buitenlandse munt. Het is nul
als
de munt precies zoveel daalt als het renteverschil, en in het toy-voorbeeld was het
renteverschil ongeveer twee procent en de koerswinst plus of min tien procent.

### De wisselkoers als verhouding van twee SDF's

Zodra de twee SDF's vastliggen, ligt ook de wisselkoersverandering vast, want die is hun
verhouding. Een
Amerikaan kan een buitenlandse payoff kopen door dollars om te wisselen en de opbrengst
later
terug te wisselen. Voor hem is dat een dollarpayoff maal de wisselkoersverandering, en zijn
eigen SDF moet die goed waarderen. Daardoor is $m$ maal de wisselkoersverandering een
geldige
buitenlandse SDF. Als er maar één buitenlandse SDF is, moet het deze zijn.

:::{prf:proposition} Wisselkoers en SDF's
:label: thm-wisselkoersen-identiteit

Laat $m_{t+1}$ alle verhandelde dollarpayoffs waarderen, en laat buitenlandse payoffs vrij in
dollars omgewisseld kunnen worden. Als de markten volledig zijn, zodat beide SDF's uniek zijn,
geldt

```{math}
:label: eq-wisselkoersen-identiteit
\frac{S_{t+1}}{S_t} = \frac{m^*_{t+1}}{m_{t+1}},
\qquad
\Delta s_{t+1} = \log m^*_{t+1} - \log m_{t+1} .
```
:::

:::{prf:proof}
Een buitenlandse payoff $x^*_{t+1}$ met frankprijs $P^*_t$ kost $P^*_t S_t$ dollar en levert
$x^*_{t+1} S_{t+1}$ dollar op. Omdat $m$ alle dollarpayoffs waardeert, is $P^*_t S_t = \E_t[m_{t+1} x^*_{t+1} S_{t+1}]$, en delen door $S_t$ geeft $P^*_t =  \E_t[(m_{t+1}S_{t+1}/S_t)\, x^*_{t+1}]$. Bij volledige markten is de buitenlandse SDF
uniek, zodat $m^*_{t+1} = m_{t+1}S_{t+1}/S_t$, en logaritmen geven de tweede vorm. $\square$
:::

De buitenlandse munt stijgt dus in precies die toestanden waarin marginaal nut in het
buitenland hoog is ten opzichte van thuis. Bij onvolledige markten is $m_{t+1}S_{t+1}/S_t$
nog
steeds een geldige buitenlandse SDF, zodat de rest van de theorie ook dan bruikbaar is.
Met de twee SDF's liggen ook de rentes vast, want $i_t - i^*_t = \log\E_t[m^*_{t+1}] - \log\E_t[m_{t+1}]$.

### Hoe glad mogen wisselkoersen zijn?

Hoe sterk moeten de SDF's van twee landen samenbewegen als de wisselkoers maar met tien
procent
per jaar schommelt? De variantie van een verschil is de som van de varianties min twee
keer de
covariantie. Links in [](#eq-wisselkoersen-identiteit) staat iets kleins en rechts het
verschil
van twee zeer volatiele grootheden, zodat alleen een grote covariantie dat verschil kan
wegwerken.

:::{prf:proposition} Risk-sharing-index
:label: thm-wisselkoersen-bcs

Laat [](#eq-wisselkoersen-identiteit) gelden. De risk-sharing-index van Brandt, Cochrane en
Santa-Clara {cite}`BrandtCochraneSantaClara2006` is dan het deel van de log-SDF-varianties dat
de covariantie wegwerkt:

```{math}
:label: eq-wisselkoersen-bcs
\Var(\Delta s) = \Var(\log m) + \Var(\log m^*) - 2\Cov(\log m, \log m^*),
\qquad
1 - \frac{\Var(\Delta s)}{\Var(\log m) + \Var(\log m^*)}
= \frac{2\Cov(\log m, \log m^*)}{\Var(\log m) + \Var(\log m^*)} .
```
:::

:::{prf:proof}
:class: dropdown

De eerste vergelijking is de variantie van $\log m^* - \log m$. De tweede volgt door beide
kanten te delen door $\Var(\log m) + \Var(\log m^*)$. $\square$
:::

De index is één als de twee log-SDF's gelijk zijn en nul als ze ongecorreleerd zijn. Omdat
we de SDF's niet waarnemen, hebben we een ondergrens nodig. Als beide log-SDF's een
standaarddeviatie van minstens $a$ hebben, geldt

```{math}
:label: eq-wisselkoersen-rhomin
\Corr(\log m, \log m^*) \;\geq\; 1 - \frac{\Var(\Delta s)}{2a^2}.
```

Dezelfde uitdrukking begrenst ook de index, omdat de noemer $\Var(\log m) + \Var(\log m^*)$
minstens $2a^2$ is. Bij $\SD(\log m) = \SD(\log m^*) = a$ vallen index, correlatie en
grens samen. Het toy-voorbeeld laat zien dat ze daarbuiten verschillen, want daar is de
correlatie één en de index 0,8048. Vanaf hier heet $1 - \Var(\Delta s)/(2a^2)$ kortweg de
grens. Die stijgt met $a$ en daalt met de wisselkoersvariantie, zoals de tweede oefening
laat
zien.

De waarde van $a$ komt uit de Hansen-Jagannathan-grens
[](#eq-equity-premium-puzzle-hj), die zegt dat $\SD(m)/\E[m]$ minstens gelijk is aan de
hoogste Sharpe-ratio. Die grens gaat over het niveau van $m$, en als $m$ lognormaal is met
log-standaarddeviatie $\sigma$, is $\SD(m)/\E[m] = \sqrt{e^{\sigma^2} - 1}$. Daaruit volgt

```{math}
:label: eq-wisselkoersen-logbound
\SD(\log m) \;\geq\; a = \sqrt{\log\left(1 + \mathrm{SR}^2\right)} ,
```

zodat een hogere Sharpe-ratio een volatielere SDF vraagt, met $a = 0{,}47$ bij een
Sharpe-ratio van een half.

Brandt, Cochrane en Santa-Clara rekenden met ronde getallen. Een wisselkoersvolatiliteit van
10% en een SDF-volatiliteit van 50% geven een grens van $1 - 0{,}1^2/(2 \cdot 0{,}5^2) =
0{,}98$, en zonder risk sharing zou de wisselkoers met $\sqrt{2} \cdot 0{,}5 = 71\%$ moeten
schommelen. Hun eigen schattingen voor de VS tegenover Engeland, Duitsland en Japan
bevestigen die orde van grootte, met wisselkoersvolatiliteiten van 11,5 tot 12,9% (tabel
1) en ondergrenzen voor de index van 0,98 of hoger (tabel 2). De telling uit de intuïtie
komt dus uit, want
de SDF's van landen bewegen bijna perfect samen.

Tegenover die 0,98 staan consumptiedata. Consumptiegroei is tussen landen maar matig
gecorreleerd, en reële wisselkoersen bewegen nauwelijks met relatieve consumptie
{cite}`BackusSmith1993`. Welke kant het mis heeft, zegt de grens niet.

### Gedekte en ongedekte rentepariteit

Een gedekte valutabelegging moet de dollarrente opleveren, maar over de verwachte
wisselkoers
zegt arbitrage niets. Wie dollars in franken wisselt, frankrente ontvangt en de franken op
termijn terugverkoopt, heeft een risicovrije dollarbelegging gebouwd. Laat $F_t$ de
termijnkoers zijn en $f_t = \log F_t$. Eén dollar levert dan $e^{i_t}$ op, of
$e^{i^*_t}F_t/S_t$
via de gedekte frankbelegging. Omdat arbitrage niet mag bestaan, geldt dan *covered interest
parity* (CIP, gedekte rentepariteit):

```{math}
:label: eq-wisselkoersen-cip
f_t - s_t = i_t - i^*_t ,
\qquad
rx_{t+1} = s_{t+1} - f_t .
```

De termijnpremie is dus gelijk aan het renteverschil, en het carry-rendement is de koers op
$t+1$ min de termijnkoers. UIP voegt daar de hypothese aan toe dat
$\E_t[\Delta s_{t+1}] = i_t - i^*_t$, oftewel $\E_t[rx_{t+1}] = 0$, zodat valutarisico geen
premie krijgt. De standaardtoets is de regressie

```{math}
:label: eq-wisselkoersen-fama
\Delta s_{t+1} = \alpha + \beta\,(f_t - s_t) + \varepsilon_{t+1}
= \alpha + \beta\,(i_t - i^*_t) + \varepsilon_{t+1}.
```

Onder UIP zijn $\alpha = 0$ en $\beta = 1$, zodat een renteverschil van één procentpunt een
verwachte depreciatie van één procentpunt geeft. Hansen en Hodrick {cite}`HansenHodrick1980`
toetsten of de termijnkoers een zuivere voorspeller is, met de standaardfouten voor
overlappende waarnemingen uit [](#04-20-voorspelbaarheid). Fama {cite}`Fama1984` vond
hellingen
onder nul. In het overzicht van Engel {cite}`Engel1996` is de zuiverheid van de
termijnkoers in
de periode van zwevende koersen verworpen, en Froot en Thaler namen het resultaat op in hun
reeks over anomalieën {cite}`FrootThaler1990`.

```{warning}
CIP is een arbitragerelatie, maar sinds 2008 wijkt de gedekte dollarrente meetbaar af, omdat
banken hun balans niet onbeperkt voor arbitrage inzetten. In de replicatie gebruiken we
renteverschillen in plaats van termijnkoersen en nemen we CIP dus aan.
```

### De Fama-decompositie

Een negatieve helling in [](#eq-wisselkoersen-fama) zegt iets over de risicopremie, zonder
dat
we een model van die premie nodig hebben. Het renteverschil is de som van een verwachte
depreciatie en een premie, en de helling meet hoe sterk de verwachte depreciatie met die som
meebeweegt. Is de helling negatief, dan moet de premie harder bewegen dan de verwachte
depreciatie en er tegenin gaan. Definieer daarom $q_t = \E_t[\Delta s_{t+1}]$ en
$p_t = f_t - \E_t[s_{t+1}] = -\E_t[rx_{t+1}]$, zodat $f_t - s_t = p_t + q_t$. Net als bij
Fama staat $p_t$ dus voor de premie.

:::{prf:proposition} Fama-decompositie
:label: thm-wisselkoersen-decompositie

Laat $q_t$ en $p_t$ zijn zoals hierboven. De populatiehelling van [](#eq-wisselkoersen-fama)
is dan

```{math}
:label: eq-wisselkoersen-decompositie
\beta = \frac{\Var(q) + \Cov(p, q)}{\Var(p) + \Var(q) + 2\Cov(p, q)} .
```

Dat heeft drie gevolgen:

1. een helling onder nul betekent $\Cov(p,q) < -\Var(q) \leq 0$, zodat de premie tegen de
   verwachte depreciatie in beweegt;
2. een helling onder $\tfrac12$ betekent $\Var(p) > \Var(q)$, zodat de premie volatieler is
   dan de verwachte depreciatie;
3. de helling van $rx_{t+1}$ op $i^*_t - i_t$ is $1 - \beta$.
:::

:::{prf:proof}
:class: dropdown

Schrijf $\Delta s_{t+1} = q_t + u_{t+1}$ met $\E_t[u_{t+1}] = 0$, zodat $u$ ongecorreleerd is
met $p_t + q_t$. Dan is $\beta = \Cov(q, p+q)/\Var(p+q)$, en dat is
[](#eq-wisselkoersen-decompositie). *Gevolg 1.* De noemer is positief, dus $\beta < 0$
precies als $\Var(q) + \Cov(p,q) < 0$. *Gevolg 2.* $\beta < \tfrac12$ geldt precies als
$2\Var(q) + 2\Cov(p,q) < \Var(p) + \Var(q) + 2\Cov(p,q)$, dus als $\Var(q) < \Var(p)$.
*Gevolg 3.* Omdat $rx = (i^* - i) + \Delta s$ en de helling van $\Delta s$ op $i^* - i$ gelijk
is aan $-\beta$, is de helling van $rx$ op $i^* - i$ gelijk aan $1 - \beta$. $\square$
:::

Om de eerste twee gevolgen staat het artikel van Fama bekend, en het derde vertaalt de
helling naar beleggen. Bij $\beta = 1$ verdient carry niets voorspelbaars en bij $\beta = 0$
het renteverschil. Bij $\beta = -1$ verdient carry het dubbele, omdat de hoge-rentevaluta
er dan ook nog bij stijgt. De gepoolde schatting in de replicatie ligt met $-0{,}62$
tussen $\beta = 0$ en $\beta = -1$.

### Carry als risicopremie in een lognormaal model

In een lognormaal model levert de munt van het land met de rustigste SDF een premie op.
Een land
waar marginaal nut sterk schommelt, spaart uit voorzorg en heeft daardoor een lage rente.
Zijn
munt wordt bovendien duur precies wanneer marginaal nut daar hoog is. Een belegger die
zo'n munt
aanhoudt, heeft dus een verzekering en betaalt ervoor, terwijl de munt van een land met
rustig
marginaal nut een premie oplevert. Laat $(\log m_{t+1}, \log m^*_{t+1})$ conditioneel
normaal
zijn met varianties $v_t$ en $v^*_t$ en covariantie $c_t$. In het toy-voorbeeld zijn de
varianties $0{,}0411$ en $0{,}0105$.

:::{prf:proposition} Carry-premie
:label: thm-wisselkoersen-lognormaal

Laat de log-SDF's conditioneel normaal zijn. Het verwachte log overrendement is dan

```{math}
:label: eq-wisselkoersen-premie
\E_t[rx_{t+1}] = \tfrac12\left(v_t - v^*_t\right).
```
:::

:::{prf:corollary} Premie op het bruto rendement
:label: thm-wisselkoersen-brutopremie

Onder dezelfde aanname is de log premie op het bruto rendement

```{math}
\log \E_t\!\left[e^{rx_{t+1}}\right] = v_t - c_t = -\Cov_t(\log m_{t+1}, rx_{t+1}) .
```
:::

:::{prf:proof}
:class: dropdown

Onder normaliteit is $\E_t[m] = \exp(\E_t[\log m] + \tfrac12 v_t)$, zodat
$i_t = -\E_t[\log m_{t+1}] - \tfrac12 v_t$, en hetzelfde geldt in het buitenland. Met
[](#eq-wisselkoersen-identiteit) is dan
$\E_t[rx] = i^* - i + \E_t[\log m^*] - \E_t[\log m] = \tfrac12(v - v^*)$. Omdat $rx$
conditioneel normaal is met variantie $v + v^* - 2c$, is
$\log\E_t[e^{rx}] = \tfrac12(v - v^*) + \tfrac12(v + v^* - 2c) = v - c$, en
$\Cov_t(\log m, \log m^* - \log m) = c - v$. $\square$
:::

Een Amerikaan verdient dus een premie op de munt van een land met een *minder* volatiele
SDF.
In het toy-voorbeeld is $\tfrac12(v - v^*) = \tfrac12(0{,}04110 - 0{,}01049) = 0{,}0153$,
dicht
bij de exacte log-premie $\log 1{,}0204 + \E[\Delta s] = 0{,}0202 - 0{,}0050 = 0{,}0152$.
Het
teken uit de intuïtie klopt dus. Of die munt ook de hogere rente heeft, hangt af van hoe
de rente met de variantie beweegt, en de parameter $b$ hieronder meet precies dat.

:::{prf:corollary} De Fama-helling in het lognormale model
:label: thm-wisselkoersen-helling

Neem in beide landen $\E_t[\log m_{t+1}] = -\delta - (b + \tfrac12)v_t$, zodat
$i_t = \delta + b\,v_t$. Is $v_t - v^*_t$ niet constant, dan is de populatiehelling van
[](#eq-wisselkoersen-fama)

```{math}
:label: eq-wisselkoersen-helling
\beta = 1 + \frac{1}{2b},
```

en is $\beta < 0$ precies als $-\tfrac12 < b < 0$.
:::

:::{prf:proof}
:class: dropdown

Nu is $i_t - i^*_t = b(v_t - v^*_t)$ en $\E_t[\Delta s] = (b + \tfrac12)(v_t - v^*_t)$. De
verwachte depreciatie is dus een vast veelvoud $(b + \tfrac12)/b$ van het renteverschil.
$\square$
:::

Een negatieve helling vraagt dus een rente die daalt met de SDF-variantie, maar niet te
hard.
Daar hangt een prijs aan. Volgens Backus, Foresi en Telmer {cite}`BackusForesiTelmer2001`
vraagt de anomalie in affiene modellen asymmetrische landen of rentes die met positieve kans
negatief worden, en in het model hierboven wordt $i_t$ met $b < 0$ en een onbegrensde $v_t$
inderdaad vroeg of laat negatief. Bekaert {cite}`Bekaert1996` vond het spiegelbeeld: zelfs
zijn
meest complexe model leverde geen voldoende variabele premies zonder te volatiele
wisselkoersen.

### Carry-portefeuilles en een gemeenschappelijke factor

Als valuta's verschillen in hun gevoeligheid voor een gemeenschappelijke SDF, ligt het
voor de
hand om ze op renteverschil te sorteren, zoals aandelen in [](#04-18-fama-french). Lustig en
Verdelhan {cite}`LustigVerdelhan2007` deden dat vanaf 1953 met acht portefeuilles op
jaardata.
Ze vonden een verschil van tot vijf procentpunt per jaar tussen lage en hoge rente, dat ze
met
consumptiegroeirisico verklaarden, maar wel bij een risicoaversie rond 100.

Lustig, Roussanov en Verdelhan {cite}`LustigRoussanovVerdelhan2011` zochten de factor in de
rendementen zelf. Met zes portefeuilles uit 37 valuta's over 1983–2008 haalde het verschil
tussen hoge- en lage-rentevaluta na kosten een Sharpe-ratio van 0,54 per jaar. Hun factor
HML$_{FX}$, de portefeuille met de hoogste rente min die met de
laagste,
verklaart ongeveer 70% van de verschillen in gemiddeld rendement.

Menkhoff, Sarno, Schmeling en Schrimpf {cite}`MenkhoffSarnoSchmelingSchrimpf2012a` vonden
dat
hoge-rentevaluta's verliezen als de wereldwijde valutavolatiliteit onverwacht stijgt. Die
volatiliteit verklaart meer dan 90% van de verschillen tussen vijf carry-portefeuilles,
zodat
de carry trade volatiliteitsverzekering verkoopt, net als de strategieën uit
[](#05-29-opties-crashrisico).

### Crashrisico en peso problems

Als slechte toestanden zeldzaam en extreem zijn, zit het risico niet in de standaarddeviatie
maar in de staart. Neem een overrendement per maand $r = \mu + \sigma\varepsilon + JB$, met
$\varepsilon \sim N(0,1)$, een sprong $J < 0$ en een $B$ die met kans $\pi$ gelijk is aan
één,
alle onafhankelijk. Dan is

```{math}
:label: eq-wisselkoersen-sprongen
\E[r] = \mu + \pi J, \qquad
\E\big[(r - \E r)^3\big] = \pi(1-\pi)(1-2\pi)\,J^3 < 0 \ \ (\pi < \tfrac12), \qquad
\Pr(\text{geen sprong in } T) = (1-\pi)^T .
```

Het gemiddelde daalt met de verwachte sprong, en de scheefheid is negatief zolang crashes
zeldzaam zijn, omdat alleen de sprongterm een derde moment heeft. De kans op een steekproef
zonder crash daalt exponentieel met de lengte $T$. In zo'n steekproef is de verdeling
normaal,
zodat het gemiddelde dan niet $\E[r]$ schat maar $\mu = \E[r] + \pi|J|$.

Brunnermeier, Nagel en Pedersen {cite}`BrunnermeierNagelPedersen2008` vonden met dagdata
voor
acht valuta's over 1986–2006 een $R^2$ van 81% tussen gemiddelde scheefheid en gemiddeld
renteverschil (hun figuur 2). Zij verklaren crashes uit het plotseling afbouwen van
carry-posities als financieringsliquiditeit opdroogt, het mechanisme van
[](#04-22-risk-management).

Burnside en coauteurs {cite}`BurnsideEichenbaumKleshchelskiRebelo2011` vroegen of een peso
problem de winst verklaart. Over 1976 tot 2009 had hun gelijkgewogen
carry-portefeuille van twintig valuta's een Sharpe-ratio van 0,911 (tabel 2). Volgens hen
is er
een peso problem, maar heeft de zeldzame toestand vooral een zeer hoge SDF en geen zeer
groot
verlies. De peso-simulatie aan het eind van de Simulatie laat zien waarom sprongen in het
rendement alleen niet genoeg zijn.

### Momentum en value in valuta

Carry is niet het enige kenmerk dat valutarendementen voorspelt. In een tweede artikel
vonden Menkhoff en coauteurs {cite}`MenkhoffSarnoSchmelingSchrimpf2012b` een verschil van
tot 10% per jaar tussen
valuta's die in het verleden wonnen en valuta's die verloren. Asness, Moskowitz en Pedersen
{cite}`AsnessMoskowitzPedersen2013` namen valuta's op in hun acht markten
([](#04-19-momentum)), met als value-signaal minus de verandering van de reële wisselkoers
(de afwijking van koopkrachtpariteit) over vijf jaar. Over 1979–2011 hadden hun
valutafactoren voor value en momentum Sharpe-ratio's van
0,44
en 0,32 (tabel I).

Barroso en Santa-Clara {cite}`BarrosoSantaClara2015b` schatten portefeuillegewichten als
functie van gestandaardiseerde kenmerken, met de techniek van Brandt, Santa-Clara en
Valkanov
{cite}`BrandtSantaClaraValkanov2009`. Volgens hen dragen carry, momentum, value en reversal
bij, terwijl de reële wisselkoers en de lopende rekening dat niet doen. Valuta verhoogde de
Sharpe-ratio van hun portefeuilles gemiddeld met een half, terwijl het crashrisico daalde.

```{admonition} Samengevat
:class: tip

- De wisselkoersverandering is het verschil van de log-SDF's van twee landen,
  [](#eq-wisselkoersen-identiteit).
- Gladde wisselkoersen vragen sterk gecorreleerde SDF's. De ondergrens voor de correlatie
  stijgt met de Sharpe-ratio, omdat die volatielere SDF's vraagt, en daalt met de
  wisselkoersvariantie, [](#eq-wisselkoersen-rhomin).
- Een negatieve UIP-helling betekent een premie die volatieler is dan de verwachte depreciatie
  en er tegenin beweegt, [](#eq-wisselkoersen-decompositie).
- De munt van het land met de rustigste SDF levert een premie op, [](#eq-wisselkoersen-premie),
  en zeldzame crashes maken die premie links scheef, [](#eq-wisselkoersen-sprongen).
- De simulatie vraagt hoe goed de ondergrens voor de SDF-correlatie te meten is als de
  Sharpe-ratio uit dertig tot honderd jaar maanddata wordt geschat.
```

## Simulatie: de grens met een geschatte Sharpe-ratio

Hoe onzeker is de grens als de Sharpe-ratio uit de data geschat moet worden? De grens
gebruikt een goed gemeten tweede moment, de wisselkoersvolatiliteit, en een slecht gemeten
Sharpe-ratio.

We nemen een ware Sharpe-ratio van een half, een aandelenvolatiliteit van 16% en een
wisselkoersvolatiliteit van 10%, zoals die van $\Delta s$ in het toy-voorbeeld. De
aandelenvolatiliteit bepaalt hoe ver het geschatte gemiddelde, en daarmee de geschatte
Sharpe-ratio, van de ware waarde afligt. De ware grens is dan
$1 - 0{,}01/(2\log 1{,}25) = 0{,}978$. Per steekproef van $T$ jaar maanddata trekken we
een normaal steekproefgemiddelde en een
geschaalde $\chi^2$-variantie, omdat de maandrendementen onafhankelijk en normaal verdeeld
zijn.

```{code-cell} ipython3
SR_TRUE, VOL_EQ, VOL_FX, N_SIM = 0.5, 0.16, 0.10, 100_000


def implied_corr(sharpe, vol_fx):
    """Lower bound on Corr(log m, log m*) with both SDF log-vols at the lognormal HJ bound."""
    a2 = np.log1p(np.asarray(sharpe) ** 2)
    return 1 - vol_fx**2 / (2 * a2)


rho_true = implied_corr(SR_TRUE, VOL_FX)
bcs_draws, bcs_rows = {}, {}
for years in (30, 50, 100):
    T = 12 * years
    mean_eq = rng.normal(SR_TRUE * VOL_EQ / 12, VOL_EQ / np.sqrt(12 * T), N_SIM)
    var_eq = VOL_EQ**2 / 12 * rng.chisquare(T - 1, N_SIM) / (T - 1)
    var_fx = VOL_FX**2 / 12 * rng.chisquare(T - 1, N_SIM) / (T - 1)
    sr_hat = np.sqrt(12) * mean_eq / np.sqrt(var_eq)
    vol_fx_hat = np.sqrt(12 * var_fx)
    rho_hat = implied_corr(sr_hat, vol_fx_hat)
    bcs_draws[years] = rho_hat
    bcs_rows[f"{years} jaar"] = {
        "Sharpe-ratio 5%": np.percentile(sr_hat, 5), "Sharpe-ratio 95%": np.percentile(sr_hat, 95),
        "vol. wisselkoers 5%": np.percentile(vol_fx_hat, 5),
        "vol. wisselkoers 95%": np.percentile(vol_fx_hat, 95),
        "grens 5%": np.percentile(rho_hat, 5), "grens mediaan": np.median(rho_hat),
        "P(grens < 0,9)": np.mean(rho_hat < 0.9), "P(grens < 0)": np.mean(rho_hat < 0),
    }
print(f"ware ondergrens voor de correlatie: {rho_true:.3f}")
pd.DataFrame(bcs_rows).T.round(3)
```

De mediaan van de geschatte grens ligt op de ware waarde, en de wisselkoersvolatiliteit is
nauwelijks onzeker, want bij dertig jaar ligt ze met 90% kans tussen 9,4 en 10,6%. In de
figuur
gaat het om de linkerstaart, die langer wordt naarmate de steekproef korter is.

```{code-cell} ipython3
:label: cel-wisselkoersen-sim-bcs
:tags: [hide-input]

fig, ax = plt.subplots()
bins = np.linspace(0.5, 1.0, 101)
for k, (years, draws) in enumerate(bcs_draws.items()):
    ax.hist(np.clip(draws, 0.5, 1.0), bins=bins, histtype="step", lw=1.6, density=True,
            color=hap.plotting.COLORS[k], label=f"{years} jaar maanddata")
ax.axvline(rho_true, color="black", ls="--", lw=1, label="ware ondergrens")
ax.set_xlabel("Geschatte ondergrens voor Corr(log m, log m*) (afgekapt op 0,5)")
ax.set_ylabel("Dichtheid")
ax.set_title("De grens voor risk sharing als de Sharpe-ratio geschat moet worden")
ax.legend(loc="upper left")
plt.show()
```

:::{figure} #cel-wisselkoersen-sim-bcs
:label: fig-wisselkoersen-sim-bcs
:width: 90%

De verdeling van de geschatte ondergrens voor de SDF-correlatie. De massa ligt dicht bij de
ware waarde, omdat de grens ongevoelig is voor de SDF-volatiliteit zolang die groot is ten
opzichte van de wisselkoers. De linkerstaart komt van steekproeven waarin de Sharpe-ratio
toevallig laag uitvalt.
:::

Ook met dertig jaar data valt de grens in 93% van de steekproeven boven de 0,9. De
onzekerheid
zit in de Sharpe-ratio, en de grens is daar sterk niet-lineair in. Een Sharpe-ratio van 0,2,
bij dertig jaar ongeveer het 5%-kwantiel, geeft nog een grens van 0,87. Bij een Sharpe-ratio
van 0,1 zakt de grens naar 0,50, en onder 0,07 wordt hij negatief. De puzzel verdwijnt dus
pas
als de ware Sharpe-ratio veel lager is dan we denken, net als bij de aandelenpremie.

:::{note} Hoe vaak ziet dertig jaar carry er gratis uit?
:class: dropdown

We nemen een strategie *zonder* risicopremie. In normale maanden verdient ze $\mu = -\pi J$ met
een volatiliteit van 2,5% per maand, ongeveer die van een G10-carry-portefeuille. Met kans
$\pi = 1/360$ per maand crasht ze met $J = -30\%$, gemiddeld één keer per dertig jaar.

```{code-cell} ipython3
YEARS_PESO, SIGMA_PESO, JUMP, N_PESO = 30, 0.025, -0.30, 20_000
T_peso = 12 * YEARS_PESO


def peso_samples(pi, n=N_PESO):
    """Monthly returns with zero true mean: normal months earn -pi*J, crashes of size JUMP."""
    crash = rng.random((n, T_peso)) < pi
    returns = -pi * JUMP + SIGMA_PESO * rng.standard_normal((n, T_peso)) + JUMP * crash
    mean, sd = returns.mean(axis=1), returns.std(axis=1, ddof=1)
    skew = ((returns - mean[:, None]) ** 3).mean(axis=1) / returns.std(axis=1) ** 3
    return {"no_crash": ~crash.any(axis=1), "sharpe": np.sqrt(12) * mean / sd,
            "t": mean / (sd / np.sqrt(T_peso)), "skew": skew}


PI_BASE = 1 / 360
peso = peso_samples(PI_BASE)
nc = peso["no_crash"]
pd.Series({
    "P(geen crash), simulatie": nc.mean(),
    "P(geen crash), (1-pi)^T": (1 - PI_BASE) ** T_peso,
    "gem. Sharpe-ratio zonder crash": peso["sharpe"][nc].mean(),
    "theorie: pi|J| sqrt(12) / sigma": PI_BASE * abs(JUMP) * np.sqrt(12) / SIGMA_PESO,
    "P(t > 2 | geen crash)": np.mean(peso["t"][nc] > 2),
    "P(t > 2), alle steekproeven": np.mean(peso["t"] > 2),
    "mediane scheefheid zonder crash": np.median(peso["skew"][nc]),
    "mediane scheefheid met crash": np.median(peso["skew"][~nc]),
}).round(3)
```

In 37% van de steekproeven valt geen crash. Het gemiddelde is dan naar boven vertekend en de
scheefheid nul, zodat de onderzoeker het risico niet ziet. De schijnbare Sharpe-ratio is echter
klein, $\pi|J|\sqrt{12}/\sigma = 0{,}115$, en maar 8,5% van die steekproeven haalt $t > 2$. De
figuur toont links de Sharpe-ratio met en zonder crash, en rechts wat er gebeurt als crashes
vaker komen.

```{code-cell} ipython3
:label: cel-wisselkoersen-sim-peso
:tags: [hide-input]

pis = np.array([1 / 1200, 1 / 720, 1 / 480, 1 / 360, 1 / 240, 1 / 180, 1 / 120])
sim_nc, sim_sr = [], []
for pi in pis:
    draw = peso_samples(pi, n=4_000)
    sim_nc.append(draw["no_crash"].mean())
    sim_sr.append(draw["sharpe"][draw["no_crash"]].mean() if draw["no_crash"].any() else np.nan)
pi_grid = np.linspace(1 / 1500, 1 / 100, 200)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
bins = np.linspace(-0.6, 0.8, 57)
axes[0].hist(peso["sharpe"][nc], bins=bins, alpha=0.6, label="steekproeven zonder crash")
axes[0].hist(peso["sharpe"][~nc], bins=bins, alpha=0.6, label="steekproeven met crash")
axes[0].axvline(0, color="black", lw=0.8)
axes[0].set_title("(a) Sharpe-ratio over 30 jaar, ware premie nul")
axes[0].set_xlabel("Geschatte Sharpe-ratio (per jaar)")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].legend()
axes[1].plot(360 * pi_grid, (1 - pi_grid) ** T_peso, color="C0", label="P(geen crash in 30 jaar)")
axes[1].plot(360 * pi_grid, pi_grid * abs(JUMP) * np.sqrt(12) / SIGMA_PESO, color="C1",
             label="Sharpe-ratio zonder crash (theorie)")
axes[1].scatter(360 * pis, sim_nc, color="C0", s=18, zorder=3)
axes[1].scatter(360 * pis, sim_sr, color="C1", s=18, zorder=3, label="simulatie")
axes[1].set_title("(b) De afruil van een peso problem, J = −30%")
axes[1].set_xlabel("Verwacht aantal crashes per 30 jaar")
axes[1].set_ylabel("Kans respectievelijk Sharpe-ratio")
axes[1].legend()
fig.tight_layout()
plt.show()
```

Links ziet een strategie zonder premie er in ruim een derde van de steekproeven winstgevend en
symmetrisch uit. Rechts stijgt de schijnbare Sharpe-ratio met de kans op een crash, terwijl de
kans op een steekproef zonder crash daalt. Voor de Sharpe-ratio van 0,44 uit de replicatie is
$\pi = 0{,}44 \cdot 0{,}025/(0{,}30\sqrt{12}) = 0{,}0106$ per maand nodig, één crash per acht
jaar. De kans op dertig jaar zonder crash is dan $(1 - 0{,}0106)^{360} \approx 2\%$. Een peso
problem zit dus in de *prijs* van de slechte toestand, een zeer hoge SDF, en niet in een
onwaarschijnlijk grote sprong in het rendement.
:::

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Fama {cite}`Fama1984` voor de UIP-regressie, Lustig, Roussanov en Verdelhan
{cite}`LustigRoussanovVerdelhan2011` voor de carry-portefeuilles, en Brandt, Cochrane en
Santa-Clara {cite}`BrandtCochraneSantaClara2006` voor de risk-sharing-index.

**Wat.** De UIP-regressie [](#eq-wisselkoersen-fama) per valuta en gepoold, HML$_{FX}$ uit
tabel 1 van Lustig e.a. en de index uit tabel 2 van Brandt e.a. Daarnaast kort momentum en
value zoals in tabel I van Asness, Moskowitz en Pedersen {cite}`AsnessMoskowitzPedersen2013`.

**Data hier.** Spotkoersen, driemaandsrentes en prijsindices van FRED voor negen valuta's tegenover de dollar over 1976–2025, waarbij de euro pas in 1999 begint. Voor de Sharpe-ratio
gebruiken we de marktfactor en 25 portefeuilles van French.

**Verschil met het origineel.** We hebben geen termijnkoersen en nemen dus CIP aan, zonder
transactiekosten. De originelen gebruiken meer valuta's en meer portefeuilles, en Brandt e.a.
schatten per land een SDF, waar wij de Amerikaanse Sharpe-ratio voor beide landen nemen.

**Verwachte afwijking.** Hellingen onder één, de meeste negatief, en een gepoolde helling onder
nul. Carry-portefeuilles die monotoon stijgen, een Sharpe-ratio van HML$_{FX}$ tussen 0,3 en
0,7 met negatieve scheefheid en een verlies van tien procent of meer in 2008, en een grens
boven 0,9 voor elke valuta. Voor momentum en value positieve Sharpe-ratio's die binnen twee
standaardfouten van die van Asness e.a. liggen.
```

### De data

We laden de spotkoersen op maandeinde en de korte rentes, en berekenen per valuta het
renteverschil en het carry-rendement van de maand erna.

```{code-cell} ipython3
FX_CODES = {  # FRED id, True if quoted as USD per foreign unit
    "GBP": ("DEXUSUK", True), "JPY": ("DEXJPUS", False), "CHF": ("DEXSZUS", False),
    "CAD": ("DEXCAUS", False), "AUD": ("DEXUSAL", True), "NZD": ("DEXUSNZ", True),
    "NOK": ("DEXNOUS", False), "SEK": ("DEXSDUS", False), "EUR": ("DEXUSEU", True),
}
CURRENCIES = list(FX_CODES)
MONTHS = pd.date_range("1976-01-31", "2025-12-31", freq="ME")


def fred_month_end(code):
    """Last available observation of each month."""
    return hap_data.fred(code)[code].dropna().resample("ME").last()


def fred_rate(code):
    """Monthly OECD short rate as a decimal per year, stamped at month end."""
    return hap_data.fred(code)[code].dropna().resample("ME").mean() / 100


log_spot = pd.DataFrame(
    {c: (1 if usd_per_unit else -1) * np.log(fred_month_end(code)) for c, (code, usd_per_unit) in FX_CODES.items()}
).reindex(MONTHS)

rates = pd.DataFrame({
    "USD": fred_rate("IR3TIB01USM156N"),
    "GBP": fred_rate("IR3TIB01GBM156N"),
    "JPY": fred_rate("IR3TCD01JPM156N").loc[:"2002-03"].combine_first(fred_rate("IR3TIB01JPM156N")),
    "CHF": fred_rate("IRSTCI01CHM156N").loc[:"1999-06"].combine_first(fred_rate("IR3TIB01CHM156N")),
    "CAD": fred_rate("IR3TIB01CAM156N"),
    "AUD": fred_rate("IR3TIB01AUM156N"),
    "NZD": fred_rate("IR3TIB01NZM156N"),
    "NOK": fred_rate("IR3TIB01NOM156N"),
    "SEK": fred_rate("IR3TIB01SEM156N"),
    "EUR": fred_rate("IR3TIB01DEM156N").loc["1999":],
}).reindex(MONTHS)

rate_diff = rates[CURRENCIES].sub(rates["USD"], axis=0) / 12    # i*_t - i_t per month, known at t
ds_next = log_spot.diff().shift(-1)                               # Delta s_{t+1}, stored at t
rx_next = (rate_diff + ds_next).where(ds_next.notna())            # carry excess return t -> t+1, stored at t

pd.DataFrame({
    "eerste maand": rx_next.apply(lambda x: x.first_valid_index()).dt.strftime("%Y-%m"),
    "maanden": rx_next.notna().sum(),
    "gem. renteverschil (%/jr)": 1200 * rate_diff.mean(),
    "vol. wisselkoers (%/jr)": 100 * np.sqrt(12) * log_spot.diff().std(),
}).round(2)
```

De wisselkoersvolatiliteiten liggen tussen ongeveer 7% (Canada) en 12% (Nieuw-Zeeland),
dezelfde orde van grootte als bij Brandt, Cochrane en Santa-Clara en in het toy-voorbeeld.

### De Fama-regressie

We schatten [](#eq-wisselkoersen-fama) op maanddata met Newey-West-standaardfouten. De
gepoolde
schatting haalt per valuta het gemiddelde eraf en clustert de standaardfouten per maand,
omdat
alle valuta's tegen dezelfde dollar bewegen.

```{code-cell} ipython3
fama_rows = {}
for c in CURRENCIES:
    fit = hap.stats.newey_west(ds_next[c], -rate_diff[c], lags=3)
    b, se = fit.params.iloc[1], fit.bse.iloc[1]
    fama_rows[c] = {"helling": b, "SE": se, "t (helling = 0)": b / se, "t (helling = 1)": (b - 1) / se,
                    "R2 (%)": 100 * fit.rsquared, "maanden": int(fit.nobs)}

panel = pd.DataFrame({"ds": ds_next.stack(), "fwd": (-rate_diff).stack()}).dropna()
panel_dm = panel - panel.groupby(level=1).transform("mean")
pooled = sm.OLS(panel_dm["ds"], panel_dm[["fwd"]]).fit(
    cov_type="cluster", cov_kwds={"groups": panel_dm.index.get_level_values(0).factorize()[0]}
)
b, se = pooled.params.iloc[0], pooled.bse.iloc[0]
fama_rows["gepoold"] = {"helling": b, "SE": se, "t (helling = 0)": b / se, "t (helling = 1)": (b - 1) / se,
                        "R2 (%)": 100 * pooled.rsquared, "maanden": int(pooled.nobs)}
fama_table = pd.DataFrame(fama_rows).T
fama_table.round(2)
```

Acht van de negen hellingen zijn negatief, en alleen de Zweedse kroon heeft een kleine
positieve helling (0,16) met een grote standaardfout (1,11). Voor zeven valuta's verwerpt
de toets
$\beta = 1$
op het 5%-niveau. De gepoolde helling is $-0{,}62$, met een $t$-waarde van $-4{,}2$ tegen
$\beta = 1$. In het lognormale model van [](#thm-wisselkoersen-helling) hoort daarbij een
$b$ van ongeveer min een derde, binnen het vereiste bereik tussen $-\tfrac12$ en nul.

Tegen $\beta = 0$ haalt echter geen enkele valuta $|t| > 2$, en de yen komt met $-1{,}96$
het
dichtst bij. Het renteverschil verklaart minder dan één procent van de maandelijkse
variantie
van wisselkoersen. Vijftig jaar data zijn dus genoeg om UIP te verwerpen, maar nauwelijks
om het
teken vast te leggen. Dat is [de standaardfout van 2%](#00-01-rendementen) in valutavorm,
want
een klein gemiddeld effect naast veel ruis is slecht te meten. Toch zegt de puntschatting
via [](#thm-wisselkoersen-decompositie) iets scherps, namelijk dat de premie volatieler
dan de verwachte
depreciatie en er negatief mee gecorreleerd is, en dat carry $1{,}62$ keer het
renteverschil verdient.

### Carry-portefeuilles

Elke maand sorteren we de beschikbare valuta's, minstens zes, op $i^*_t - i_t$ in drie
gelijkgewogen portefeuilles. HML$_{FX}$ is P3 min P1, en het rendement is
[](#eq-wisselkoersen-rx).

```{code-cell} ipython3
def sort_portfolios(signal, returns_next, n_groups=3, min_assets=6):
    """Equal-weighted portfolios sorted on a signal at t; returns earned t -> t+1, indexed at t+1."""
    ranks = signal.where(returns_next.notna()).rank(axis=1, method="first")
    count = ranks.notna().sum(axis=1)
    group = np.ceil(ranks.mul(n_groups).div(count, axis=0))  # group g: rank share in ((g-1)/n, g/n]
    out = pd.DataFrame({f"P{g}": returns_next.where(group == g).mean(axis=1) for g in range(1, n_groups + 1)})
    out = out[count >= min_assets].copy()
    out["HML"] = out[f"P{n_groups}"] - out["P1"]
    out.index = out.index + pd.offsets.MonthEnd(1)
    return out


def portfolio_table(frame):
    """Annualised statistics with the standard error of the mean and of the Sharpe ratio."""
    stats = hap.stats.summary_stats(frame).astype({"nobs": int})
    years = stats["nobs"] / 12
    sharpe = stats["sharpe_ann"].astype(float)
    return pd.DataFrame({
        "gem. (%/jr)": 100 * stats["mean_ann"], "SE gem.": 100 * stats["se_mean_ann"],
        "vol. (%/jr)": 100 * stats["std_ann"], "Sharpe": sharpe,
        "SE Sharpe": np.sqrt((1 + sharpe**2 / 2) / years),
        "scheefheid": stats["skew"], "slechtste maand (%)": 100 * stats["min"],
        "maanden": stats["nobs"],
    }).astype(float)


carry = sort_portfolios(rate_diff, rx_next)
print(f"carry-portefeuilles {carry.index[0]:%Y-%m} t/m {carry.index[-1]:%Y-%m}")
portfolio_table(carry).round(2)
```

De portefeuilles beginnen in februari 1979, de eerste maand met zes valuta's, en de
rangorde is monotoon, want het gemiddelde rendement stijgt van P1 naar P3. HML$_{FX}$ haalt
een Sharpe-ratio van 0,44 met een standaardfout van 0,15, en de overige waarden staan in de
tabel. De negatieve scheefheid van HML$_{FX}$ komt van de hoge-rentekant, want P3 is links
scheef en P1 rechts. De volgende cel
kijkt naar de crisis van 2008 en naar de slechtste maanden.

```{code-cell} ipython3
carry_crisis = carry.loc["2008-08":"2008-12"]
hml_dd = hap.stats.drawdowns(np.expm1(carry.loc["2007-06":"2009-12", "HML"]))
worst = carry["HML"].nsmallest(5)
print(f"HML_FX aug-dec 2008: {100 * carry_crisis['HML'].sum():.1f}% (log, cumulatief)")
print(f"grootste drawdown 2007-06 t/m 2009-12: {100 * hml_dd.attrs['max_drawdown']:.1f}%, "
      f"dal in {hml_dd.attrs['trough']:%Y-%m}")
print(f"grootste drawdown volledige steekproef: {100 * hap.stats.drawdowns(np.expm1(carry['HML'])).attrs['max_drawdown']:.1f}%")
(100 * worst).round(1).rename("vijf slechtste maanden HML_FX (%)").to_frame().T
```

Van augustus tot en met december 2008 verloor HML$_{FX}$ 26,6% in logs, en tot januari 2009
liep de drawdown op tot 28%. Oktober 2008 was met $-11{,}2\%$ de slechtste maand, gelijk met
juli 1986, en ook oktober 1987 staat in de lijst. Een handvol maanden bepaalt zo het
risicoprofiel van 47 jaar. In de figuur gaat het om de dikke lijn van HML$_{FX}$ in het
grijze
najaar van 2008.

```{code-cell} ipython3
:label: cel-wisselkoersen-carry
:tags: [hide-input]

fig, ax = plt.subplots()
labels = {"P1": "P1 (lage rente)", "P2": "P2", "P3": "P3 (hoge rente)", "HML": "HML$_{FX}$"}
for k, col in enumerate(["P1", "P2", "P3", "HML"]):
    ax.plot(carry.index, 100 * carry[col].cumsum(), color=hap.plotting.COLORS[k], label=labels[col],
            lw=2.2 if col == "HML" else 1.4)
ax.axvspan(pd.Timestamp("2008-08-01"), pd.Timestamp("2008-12-31"), color="grey", alpha=0.25, lw=0)
ax.axhline(0, color="black", lw=0.8)
hap.plotting.timeline_axis(ax)
ax.set_xlabel("Jaar")
ax.set_ylabel("Cumulatief log overrendement (%)")
ax.set_title("Carry-portefeuilles van G10-valuta's tegenover de dollar")
ax.legend()
plt.show()
```

:::{figure} #cel-wisselkoersen-carry
:label: fig-wisselkoersen-carry
:width: 90%

Cumulatieve log overrendementen van drie portefeuilles gesorteerd op renteverschil.
Lage-rentevaluta's verliezen gestaag en hoge-rentevaluta's winnen gestaag, maar in het grijze
najaar van 2008 gaat een groot deel van het verschil in een paar maanden verloren. Zo zijn de
trap en de lift uit de intuïtie in de data terug te zien.
:::

### Brandt, Cochrane en Santa-Clara op G10-data

We nemen de Sharpe-ratio van de Amerikaanse markt als grens voor beide SDF's, zetten die met
[](#eq-wisselkoersen-logbound) om en berekenen [](#eq-wisselkoersen-rhomin) per valuta. Ter
controle doen we dat ook met de Sharpe-ratio min twee standaardfouten, en met de maximale
Sharpe-ratio van de 25 portefeuilles en de markt, die in de steekproef overschat is.

```{code-cell} ipython3
ff3 = hap_data.french("F-F_Research_Data_Factors").loc["1976":"2025"]
ff25 = hap_data.french("25_Portfolios_5x5").loc["1976":"2025"]
excess_25 = ff25.sub(ff3["RF"], axis=0).join(ff3["Mkt-RF"])
mu_vec = excess_25.mean().to_numpy()
max_sharpe = np.sqrt(12 * mu_vec @ np.linalg.solve(excess_25.cov().to_numpy(), mu_vec))

years_eq = len(ff3) / 12
sr_market = float(hap.stats.sharpe(ff3["Mkt-RF"]))
se_sr = np.sqrt((1 + sr_market**2 / 2) / years_eq)
bounds = {"markt": sr_market, "markt - 2 SE": sr_market - 2 * se_sr, "max. 25 + markt": max_sharpe}
print(f"Sharpe-ratio markt 1976-2025: {sr_market:.2f} (SE {se_sr:.2f}); "
      f"maximale Sharpe-ratio 25 portefeuilles + markt: {max_sharpe:.2f}")

fx_vol = np.sqrt(12) * log_spot.diff().loc["1976":"2025"].std()
bcs_table = pd.DataFrame({"vol. wisselkoers": fx_vol})
for name, sr in bounds.items():
    bcs_table[f"grens ({name})"] = implied_corr(sr, fx_vol)
bcs_table.loc["gem. G10"] = bcs_table.mean()
bcs_table.round(3)
```

Met de Sharpe-ratio van de markt over 1976–2025 ligt de grens per valuta tussen 0,975 voor
de Nieuw-Zeelandse en 0,991 voor de Canadese dollar. Een Sharpe-ratio die twee
standaardfouten lager ligt, trekt de grens omlaag, en de maximale Sharpe-ratio duwt hem
dichter naar één. In alle drie de kolommen blijft het G10-gemiddelde boven de 0,9.

Eén grens voor beide landen is verdedigbaar. Brandt, Cochrane en Santa-Clara vonden lokale
Sharpe-ratio's van 0,26 (Japan) tot 0,63 (VS), maar minimum-variantie-SDF's van
vergelijkbare
volatiliteit, doordat alle beleggers in wezen dezelfde activa kunnen kopen. Het resultaat is
robuust omdat de wisselkoersvariantie klein is ten opzichte van de SDF-variantie, zoals de
simulatie al liet zien.

### Momentum en value in valuta

Momentum is het cumulatieve carry-rendement over maand $t-11$ tot en met $t-1$, zoals de
12-1-regel van [](#04-19-momentum). Value is minus de verandering van de reële wisselkoers
over vijf jaar, omdat een munt die reëel goedkoper is geworden als ondergewaardeerd geldt,
net als bij Asness, Moskowitz en Pedersen. We laten de hele reële wisselkoers drie
maanden achterlopen, zodat de prijsindices op dat moment gepubliceerd zijn.

```{code-cell} ipython3
CPI_CODES = {"USD": "USACPIALLMINMEI", "GBP": "GBRCPIALLMINMEI", "JPY": "JPNCPIALLMINMEI",
             "CHF": "CHECPIALLMINMEI", "CAD": "CANCPIALLMINMEI", "AUD": "AUSCPIALLQINMEI",
             "NZD": "NZLCPIALLQINMEI", "NOK": "NORCPIALLMINMEI", "SEK": "SWECPIALLMINMEI",
             "EUR": "DEUCPIALLMINMEI"}


def log_cpi(code):
    """Log CPI at month end; quarterly series are carried forward within the quarter."""
    series = hap_data.fred(code)[code]
    series = series[series > 0].resample("ME").last()
    return np.log(series).ffill(limit=2)


cpi = pd.DataFrame({c: log_cpi(code) for c, code in CPI_CODES.items()}).reindex(MONTHS)
real_fx = log_spot + cpi[CURRENCIES].sub(cpi["USD"], axis=0)

momentum_signal = rx_next.shift(2).rolling(11, min_periods=11).sum()
value_signal = -(real_fx.shift(3) - real_fx.shift(63))

momentum = sort_portfolios(momentum_signal, rx_next)
value = sort_portfolios(value_signal, rx_next)
factors = pd.DataFrame({"carry": carry["HML"], "momentum": momentum["HML"], "value": value["HML"]}).dropna()
factors["50/50 momentum-value"] = 0.5 * (factors["momentum"] + factors["value"])
factors["gelijk gewogen, drie"] = factors[["carry", "momentum", "value"]].mean(axis=1)
print(f"gemeenschappelijke steekproef {factors.index[0]:%Y-%m} t/m {factors.index[-1]:%Y-%m}")
print("correlaties:")
print(factors[["carry", "momentum", "value"]].corr().round(2).to_string())
portfolio_table(factors).round(2)
```

Over 1981–2025 haalt value de hoogste Sharpe-ratio van de drie kenmerken, terwijl momentum
vrijwel niets doet. Momentum en value zijn negatief gecorreleerd, en carry hangt met beide
nauwelijks samen. Een gelijkgewogen mix van de drie haalt daardoor met 0,52 een hogere
Sharpe-ratio dan elk kenmerk alleen. De crash van carry verdwijnt niet, want de scheefheid
blijft $-0{,}71$, maar hij wordt verdund. Barroso en Santa-Clara bouwen precies zo'n
portefeuille uit kenmerken die elk een ander risico dragen.

### Vergelijking met de originelen

De tabel zet de belangrijkste getallen naast de gepubliceerde waarden. Voor de Fama-helling
geeft de eerste rij alleen het teken uit het origineel, omdat Fama per valuta rapporteerde.

```{code-cell} ipython3
carry_stats, factor_stats = portfolio_table(carry), portfolio_table(factors)
comparison = pd.DataFrame(
    {"origineel": [np.nan, 0.54, 0.98, 0.44, 0.32],
     "hier": [fama_table.loc["gepoold", "helling"], carry_stats.loc["HML", "Sharpe"],
              bcs_table.loc["gem. G10", "grens (markt)"],
              factor_stats.loc["value", "Sharpe"], factor_stats.loc["momentum", "Sharpe"]],
     "SE hier": [fama_table.loc["gepoold", "SE"], carry_stats.loc["HML", "SE Sharpe"], np.nan,
                 factor_stats.loc["value", "SE Sharpe"], factor_stats.loc["momentum", "SE Sharpe"]]},
    index=["Fama-helling, gepoold (Fama 1984: onder nul)", "Sharpe-ratio HML_FX (Lustig e.a., tabel 1)",
           "grens voor de index (Brandt e.a., tabel 2)",
           "Sharpe-ratio value (Asness e.a., tabel I)", "Sharpe-ratio momentum (Asness e.a., tabel I)"],
)
comparison.round(2)
```

**Geslaagd.** De data gedragen zich zoals we vooraf verwachtten. De hellingen liggen onder
één en zijn op één na negatief, de carry-portefeuilles zijn monotoon, en HML$_{FX}$ verloor
van augustus tot en met december 2008 26,6%. Voor elke valuta ligt de grens boven de 0,9.
Momentum blijft als enige achter bij het origineel, maar het verschil is kleiner dan twee
keer de standaardfout van 0,15.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** De identiteit [](#eq-wisselkoersen-identiteit) koppelt het
SDF-raamwerk rechtstreeks aan data. Ze verklaart waarom rentes, wisselkoersen en
risicopremies
samenhangen, en waarom de munt van een land met volatiel marginaal nut een lage rente
heeft en
in crises stijgt. Ook een UIP-helling onder nul wordt zo een mogelijke risicopremie in
plaats
van irrationaliteit. De uitspraak van Brandt, Cochrane en Santa-Clara over risk sharing
komt op
onze G10-data terug met hetzelfde getal, 0,98.

**Waar het breekt.** Het model breekt op dezelfde data. De gepoolde Fama-helling is
$-0{,}62$
in plaats van één, en HML$_{FX}$ verloor in het najaar van 2008 ruim een kwart, waarna de
Sharpe-ratio zakte naar 0,13
(derde oefening). Het lognormale model geeft dat teken alleen als de rente daalt met de
SDF-variantie, en dat kost volgens Backus, Foresi en Telmer negatieve rentes of
asymmetrische
landen. Een SDF-correlatie van 0,98 staat bovendien haaks op consumptiedata. De theorie
voorspelde het feit dus niet, maar maakte er achteraf ruimte voor.

**Risico of vergissing?** In de Chicago-lezing is carry een beloning voor wereldwijd
risico. Hoge-rentevaluta's verliezen als de wereldwijde volatiliteit onverwacht stijgt
{cite}`MenkhoffSarnoSchmelingSchrimpf2012a`, laden op één gemeenschappelijke factor
{cite}`LustigRoussanovVerdelhan2011`, en hun peso problem is een toestand waarin een dollar
extreem veel waard is {cite}`BurnsideEichenbaumKleshchelskiRebelo2011`. In de Yale-lezing
is de winst een vergissing die blijft bestaan door *limits of arbitrage* (arbitrageurs met
beperkt kapitaal kunnen niet alles corrigeren). Valutamomentum komt dan uit onder- en
overreactie {cite}`MenkhoffSarnoSchmelingSchrimpf2012b`, crashes uit gedwongen afbouw
{cite}`BrunnermeierNagelPedersen2008` en de winst deels uit schaars speculatief kapitaal
{cite}`BarrosoSantaClara2015b`. Om de kampen te scheiden
is de
SDF in zeldzame crisistoestanden nodig, en die is met een handvol crises niet te meten.

**Wat er daarna kwam.** Barroso en Santa-Clara pasten op valuta's de methode toe die het
sorteren op
één kenmerk vervangt door gewichten die rechtstreeks als functie van kenmerken worden
geschat. Die parametrische
portefeuilles zijn het onderwerp van [](#05-31-portfolio-choice).

## Oefeningen

:::{exercise}
:label: ex-wisselkoersen-1

**Instap: een rustiger frank.** Neem het toy-voorbeeld, maar met $m^* = (0{,}90;\ 1{,}10)$ in
plaats van $(0{,}88;\ 1{,}08)$.

1. Bereken met de hand de twee rentes, de wisselkoersveranderingen en het verwachte
   carry-rendement.
2. De rentes zijn nu gelijk. Waarom levert de frankbelegging toch een premie op, en hoe goed
   is de lognormale benadering [](#eq-wisselkoersen-premie)?
:::

:::{solution} ex-wisselkoersen-1
:class: dropdown

**(1)** Nu is $\E[m^*] = 1{,}00$, dus $R^{f*} = R^f = 1{,}00$. De frank stijgt met factor
$0{,}90/0{,}80 = 1{,}125$ in de goede toestand en daalt tot $1{,}10/1{,}20 = 0{,}9167$ in de
slechte. Het carry-rendement is daardoor $+12{,}5\%$ of $-8{,}33\%$, gemiddeld $+2{,}08\%$.

```{code-cell} ipython3
m_calm = np.array([0.90, 1.10])
Rf_calm = 1 / (prob @ m_calm)
fx_calm = m_calm / m_home
excess_calm = Rf_calm * fx_calm - Rf
pd.Series({
    "R^f*": Rf_calm, "S'/S goed": fx_calm[0], "S'/S slecht": fx_calm[1],
    "E[carry]": prob @ excess_calm,
    "log-premie (exact)": np.log(Rf_calm / Rf) + prob @ np.log(fx_calm),
    "log-premie (lognormaal)": 0.5 * (pvar(np.log(m_home)) - pvar(np.log(m_calm))),
}).round(4)
```

**(2)** De premie komt uit de covariantie met de Amerikaanse SDF en niet uit het
renteverschil. De frank daalt nog steeds in de slechte toestand, omdat marginaal nut in
Zwitserland daar minder stijgt dan in de VS. De lognormale benadering geeft 0,0155 tegen een
exacte log-premie van 0,0154. Een renteverschil is dus een symptoom en geen oorzaak, want de
premie hoort bij het verschil in SDF-volatiliteit.
:::

:::{exercise}
:label: ex-wisselkoersen-2

**De ondergrens voor de SDF-correlatie.** Laat $\SD(\log m) = \sigma \geq a$ en
$\SD(\log m^*) = \sigma^* \geq a$, en noem $\Var(\Delta s) = V$.

1. Laat met [](#eq-wisselkoersen-bcs) zien dat
   $\Corr(\log m, \log m^*) = 1 + \big((\sigma - \sigma^*)^2 - V\big)/(2\sigma\sigma^*)$, en leid
   [](#eq-wisselkoersen-rhomin) af. Wanneer geldt gelijkheid?
2. Reken het voorbeeld van Brandt, Cochrane en Santa-Clara na ($\SD(\Delta s) = 0{,}10$,
   $a = 0{,}5$) en bereken hoe volatiel wisselkoersen bij ongecorreleerde SDF's zouden zijn.
3. Welke Sharpe-ratio geeft volgens [](#eq-wisselkoersen-logbound) bij de gemiddelde
   G10-wisselkoersvolatiliteit uit de replicatie een grens van een half?
:::

:::{solution} ex-wisselkoersen-2
:class: dropdown

**(1)** Uit [](#eq-wisselkoersen-bcs) volgt $\Corr = (\sigma^2 + \sigma^{*2} - V)/(2\sigma\sigma^*)$,
en $\sigma^2 + \sigma^{*2} = (\sigma - \sigma^*)^2 + 2\sigma\sigma^*$. De eerste term is
niet-negatief, dus $\Corr \geq 1 - V/(2\sigma\sigma^*) \geq 1 - V/(2a^2)$, omdat
$\sigma\sigma^* \geq a^2$. Gelijkheid geldt precies bij $\sigma = \sigma^* = a$.

**(2) en (3)** De cel rekent het voorbeeld van Brandt, Cochrane en Santa-Clara na en zoekt
de Sharpe-ratio die bij de gemiddelde G10-volatiliteit een grens van een half geeft.

```{code-cell} ipython3
V_bcs, a_bcs = 0.10**2, 0.5
print(f"grens BCS-voorbeeld: {1 - V_bcs / (2 * a_bcs**2):.2f}")
print(f"wisselkoersvolatiliteit bij correlatie nul: {np.sqrt(2) * a_bcs:.3f}")
vol_g10 = float(bcs_table.loc["gem. G10", "vol. wisselkoers"])
a2_needed = vol_g10**2 / (2 * (1 - 0.5))
print(f"G10-vol {vol_g10:.3f}: grens 0.5 vraagt log-SDF-vol {np.sqrt(a2_needed):.3f}, "
      f"dus een Sharpe-ratio van {np.sqrt(np.expm1(a2_needed)):.3f}")
```

Ongecorreleerde SDF's vragen wisselkoersen die met 71% per jaar schommelen. Een grens van een
half vraagt een Sharpe-ratio van ongeveer 0,1 per jaar. De conclusie van Brandt, Cochrane en
Santa-Clara volgt dus uit de orde van grootte van twee getallen en niet uit randgevallen van
hun aannames.
:::

:::{exercise}
:label: ex-wisselkoersen-3

**Voor en na 2008.** Gebruik `panel`, `carry` en `portfolio_table` uit de replicatie. Schat de
gepoolde Fama-helling apart voor formatiedata 1979–2007 en 2008–2025, en bereken voor dezelfde
periodes de statistieken van HML$_{FX}$. Wat had een onderzoeker eind 2007 geconcludeerd?
:::

:::{solution} ex-wisselkoersen-3
:class: dropdown

De cel schat de gepoolde helling en de statistieken van HML$_{FX}$ voor beide periodes.

```{code-cell} ipython3
def pooled_fama(frame):
    """Pooled UIP slope with currency fixed effects and month-clustered standard errors."""
    dm = frame - frame.groupby(level=1).transform("mean")
    fit = sm.OLS(dm["ds"], dm[["fwd"]]).fit(
        cov_type="cluster", cov_kwds={"groups": dm.index.get_level_values(0).factorize()[0]}
    )
    return fit.params.iloc[0], fit.bse.iloc[0]


dates = panel.index.get_level_values(0)
split_rows = {}
for label, (start, end) in {"1979-2007": ("1979-01-01", "2007-12-31"),
                            "2008-2025": ("2008-01-01", "2025-12-31")}.items():
    b_sub, se_sub = pooled_fama(panel[(dates >= start) & (dates <= end)])
    hml_stats = portfolio_table(carry.loc[start:end, ["HML"]]).iloc[0]
    split_rows[label] = {"Fama-helling": b_sub, "SE": se_sub, "t (helling = 1)": (b_sub - 1) / se_sub,
                         **hml_stats[["gem. (%/jr)", "SE gem.", "Sharpe", "SE Sharpe", "scheefheid",
                                      "slechtste maand (%)"]].to_dict()}
pd.DataFrame(split_rows).T.round(2)
```

Eind 2007 zag carry eruit als een gevestigde regelmaat. De gepoolde helling was $-1{,}01$, bijna
het dubbele renteverschil uit [](#thm-wisselkoersen-decompositie), en de Sharpe-ratio 0,60
(standaardfout 0,20). Na 2008 is de helling positief (1,39, standaardfout 1,38), in een periode
waarin de renteverschillen binnen de G10 jarenlang bijna nul waren, en de Sharpe-ratio is 0,13
(standaardfout 0,24). Een premie die met dertig jaar data zeker leek, is na één crash dus niet
meer aantoonbaar. Dat past bij een uitbetaalde risicopremie en bij een weggearbitreerde
anomalie, want met deze standaardfouten zijn de twee niet uit elkaar te houden.
:::

:::{exercise}
:label: ex-wisselkoersen-4

**Een parametrische valutaportefeuille.** Standaardiseer elke maand carry, momentum en value
over de valuta's waarvoor alle drie beschikbaar zijn, en neem
$w_{i,t} = \boldsymbol{\theta}'\mathbf{z}_{i,t}/N_t$.

1. Laat zien dat het portefeuillerendement $\boldsymbol{\theta}'\mathbf{F}_{t+1}$ is, met
   $F_{k,t+1} = \frac{1}{N_t}\sum_i z_{k,i,t}\, rx_{i,t+1}$, en dat de $\boldsymbol{\theta}$ die
   $\E[r_p] - \tfrac{\gamma}{2}\Var(r_p)$ maximaliseert, evenredig is met
   $\boldsymbol{\Sigma}_F^{-1}\boldsymbol{\mu}_F$.
2. Schat $\boldsymbol{\theta}$ op 1981–2002 en evalueer op 2003–2025, tegenover alleen carry en
   gelijke gewichten.
:::

:::{solution} ex-wisselkoersen-4
:class: dropdown

**(1)** Er geldt $r_{p,t+1} = \sum_i w_{i,t}\, rx_{i,t+1} = \boldsymbol{\theta}'\mathbf{F}_{t+1}$,
dus $\E[r_p] - \tfrac{\gamma}{2}\Var(r_p) = \boldsymbol{\theta}'\boldsymbol{\mu}_F -
\tfrac{\gamma}{2}\boldsymbol{\theta}'\boldsymbol{\Sigma}_F\boldsymbol{\theta}$. De
eerste-ordevoorwaarde geeft $\boldsymbol{\theta} = \gamma^{-1}\boldsymbol{\Sigma}_F^{-1}\boldsymbol{\mu}_F$,
zodat het een mean-variance-probleem met drie kenmerkportefeuilles is.

**(2)** De cel schat de gewichten in de eerste helft en evalueert ze in de tweede.

```{code-cell} ipython3
signals = {"carry": rate_diff, "momentum": momentum_signal, "value": value_signal}
available = rx_next.notna()
for sig in signals.values():
    available &= sig.notna()
n_avail = available.sum(axis=1)


def cross_section_z(signal):
    """Cross-sectional z-score over currencies with all signals and a next-month return."""
    x = signal.where(available)
    return x.sub(x.mean(axis=1), axis=0).div(x.std(axis=1), axis=0)


char_returns = pd.DataFrame(
    {k: (cross_section_z(sig) * rx_next).sum(axis=1, min_count=1) / n_avail for k, sig in signals.items()}
)[n_avail >= 6].dropna()
char_returns.index = char_returns.index + pd.offsets.MonthEnd(1)

train, test = char_returns.loc["1981":"2002"], char_returns.loc["2003":"2025"]
theta = np.linalg.solve(train.cov().to_numpy(), train.mean().to_numpy())
policies = {"optimaal (geschat in de steekproef)": theta, "alleen carry": np.array([1.0, 0.0, 0.0]),
            "gelijke gewichten": np.ones(3)}
rows_pp = {}
for name, th in policies.items():
    scale = 0.10 / (np.sqrt(12) * (train @ th).std())                 # 10% volatility in the training sample
    for label, sample in {"1981-2002": train, "2003-2025": test}.items():
        r_p = scale * (sample @ th)
        rows_pp[(name, label)] = {"Sharpe": float(hap.stats.sharpe(r_p)), "vol. (%/jr)": 100 * np.sqrt(12) * r_p.std(),
                                  "scheefheid": r_p.skew()}
print("theta (genormeerd):", dict(zip(char_returns.columns, (theta / np.abs(theta).sum()).round(2))))
pd.DataFrame(rows_pp).T.round(2)
```

In de schattingsperiode legt de optimale portefeuille het meeste gewicht op value, met een
Sharpe-ratio van 1,02. Buiten de steekproef is dat 0,24, iets onder gelijke gewichten (0,26) en
boven carry alleen (0,18). Dat is het bekende effect uit [](#01-04-markowitz), waarbij
$\boldsymbol{\Sigma}_F^{-1}\boldsymbol{\mu}_F$ de schattingsfout in $\boldsymbol{\mu}_F$
versterkt. De winst zit dus in het combineren van kenmerken met verschillend risico, en
geschatte gewichten helpen pas als de schattingsfout wordt ingetoomd, zoals in
[](#05-31-portfolio-choice).
:::
