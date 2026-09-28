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

(03-12-consumptie-capm)=

# Lucas, Breeden en de SDF

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1976–1983.

**Wat we al weten.** In [](#01-03-williams-ddm) werd een prijs de contante
waarde van toekomstige dividenden. De discontovoet was daar een gegeven, en de
data lieten zien dat juist die discontovoet beweegt. In
[](#03-11-apt-no-arbitrage) bleek dat de afwezigheid van arbitrage genoeg is
voor het bestaan van een positieve stochastische discontofactor $m_{t+1}$ met $p_t = \E_t[m_{t+1} x_{t+1}]$.
Welke $m_{t+1}$ dat is, zegt die stelling niet.

**Welke vraag staat open.** Is $m_{t+1}$ te koppelen aan iets wat we kunnen
meten, zodat de theorie van de discontovoet toetsbaar wordt?
```

## Overzicht

Waar komt de discontovoet vandaan? Uit consumptie: een euro morgen is weinig
waard als morgen een goede dag is, en veel als het een slechte dag is. De
*stochastic discount factor* (SDF, stochastische discontofactor: de
willekeurige variabele waarmee we een toekomstige payoff verdisconteren) is dan
de verhouding van marginale nutten, $m_{t+1} = \beta\,u'(c_{t+1})/u'(c_t)$. Een
activum verdient dan een premie naar zijn covariantie met consumptiegroei, maar
consumptie blijkt te glad om de premies in de data te dragen. In deze lecture:

- lossen we een Lucas-boom met twee groeitoestanden met de hand op;

- leiden we de Euler-vergelijking $p_t = \E_t[m_{t+1}x_{t+1}]$ af, en daaruit de
  prijs-dividend-ratio, een gesloten vorm voor rente en premie, en de
  consumptiebèta;

- leiden we de GMM-toets van Hansen af, die de Euler-vergelijking schat zonder
  de economie op te lossen;

- simuleren we hoe nauwkeurig die toets is op zeventig jaar data uit een
  economie waarin het model waar is;

- repliceren we de schattingen van Hansen en Singleton uit 1983 op Amerikaanse
  kwartaaldata.

Rubinstein gebruikte de weging met marginaal nut in 1976 om onzekere
inkomensstromen en opties te waarderen {cite}`Rubinstein1976`. Lucas maakte er in
1978 een evenwichtsmodel van: een economie met één boom waarvan het dividend
wordt opgegeten {cite}`Lucas1978`. Breeden liet in 1979 zien dat de
toestandsvariabelen van Mertons intertemporele CAPM, zoals de rente, in continue
tijd samenvallen tot één bèta, die ten opzichte van consumptie {cite}`Breeden1979`.

Dit werk definieert het tijdvak omdat de discontovoet voor het eerst uit een
optimalisatieprobleem volgt, en daardoor fout kan zijn. Hansen ontwikkelde
daarvoor de *generalized method of moments* (GMM, gegeneraliseerde
momentenmethode) {cite}`Hansen1982`, en Hansen en Singleton toetsten er de
Euler-vergelijking mee {cite}`HansenSingleton1982,HansenSingleton1983`. Het
model heet het consumptie-CAPM (in de literatuur *consumption CAPM*: het CAPM
met consumptiegroei als enige risicofactor). In de vraag theorie of feit die de reeks
doorloopt, is dit model het zuiverste voorbeeld van theorie. Twee parameters moeten
alle rendementen verklaren, en een toets kan het model verwerpen.

## Intuïtie: waarom zou dit waar zijn?

Denk aan een eiland met één boom. Elk jaar laat de boom vruchten vallen, en die
vruchten zijn het enige voedsel. Ze bederven, dus wat niet wordt opgegeten, is
verloren. Iedereen bezit een deel van de boom, en die aandelen zijn
verhandelbaar. Wat is een aandeel waard?

De markt kiest niet hoeveel er wordt gegeten. De boom bepaalt dat. De markt kiest
alleen de prijs. Die prijs moet zo zijn dat niemand wil kopen of verkopen, want
er is niemand aan de andere kant.

De rest volgt uit één afweging. Wie vandaag een vrucht niet opeet maar belegt,
geeft vandaag nut op en krijgt morgen nut terug. Voor een hongerige is een
extra vrucht veel waard, voor een verzadigde weinig. Een belegging die vooral
uitbetaalt als het morgen toch al goed gaat, levert dus weinig nut op. Een
belegging die uitbetaalt als het misgaat, werkt als een verzekering en is veel
waard.

Wat verwachten we dus? Ten eerste een rente die stijgt met de verwachte groei.
Wie verwacht rijker te worden, wil nu lenen om vandaag meer te eten. Niemand kan
lenen, dus de rente stijgt tot die wens verdwijnt. Ten tweede een positieve
premie op aandelen in de boom. Die betalen het meest als de oogst groot is, dus
als een extra vrucht het minst waard is. De premie groeit met hoe sterk het
rendement meebeweegt met consumptie. Ten derde schommelt consumptie weinig, dus
zonder grote risicoaversie blijft die premie klein. Die derde voorspelling maakt
het model toetsbaar.

## Toy-voorbeeld: een Lucas-boom met twee groeitoestanden

We rekenen de prijs van de boom, de rente en de premie uit in een economie met
twee toestanden. De eerste cel laadt de pakketten voor de hele lecture.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize, stats

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** Consumptie is het dividend van de boom, $c_t = d_t$. De groei
$g_{t+1} = d_{t+1}/d_t$ is hoog ($g_h = 1{,}04$) of laag ($g_l = 0{,}96$). Ze
volgt een Markov-keten die neigt in dezelfde toestand te blijven. Voorkeuren zijn
CRRA, $u(c) = c^{1-\gamma}/(1-\gamma)$, met $\gamma = 2$ en $\beta = 0{,}96$.

| van \ naar | hoog | laag |
|---|---|---|
| hoog | 0,75 | 0,25 |
| laag | 0,25 | 0,75 |

**Het recept.** De prijs is de verwachte payoff gewogen met de SDF,
$p_t = \E_t[m_{t+1}x_{t+1}]$ met $m_{t+1} = \beta g_{t+1}^{-\gamma}$. De theorie
leidt dit als eerste af. Omdat de groei de toestand is en niet het niveau, hangt
de prijs-dividend-ratio $\mathrm{PD}_i = p_t/d_t$ alleen af van de toestand
$i \in \{h, l\}$. Invullen van $x_{t+1} = p_{t+1} + d_{t+1}$ en delen door $d_t$
geeft

$$
\mathrm{PD}_i = \sum_j \beta P_{ij}\, g_j^{1-\gamma} \left(1 + \mathrm{PD}_j\right).
$$

**Stap 1: de gewichten.** Bij $\gamma = 2$ is $g_j^{1-\gamma} = 1/g_j$. Dan is
$\beta P_{hh}/g_h = 0{,}72/1{,}04 = 9/13$ en $\beta P_{hl}/g_l = 0{,}24/0{,}96 = 1/4$.
Evenzo $\beta P_{lh}/g_h = 3/13$ en $\beta P_{ll}/g_l = 3/4$.

**Stap 2: de prijs-dividend-ratio.** Met $y_i = 1 + \mathrm{PD}_i$ staat er
$y_h = 1 + \tfrac{9}{13}y_h + \tfrac14 y_l$ en
$y_l = 1 + \tfrac{3}{13}y_h + \tfrac34 y_l$, of
$\tfrac{4}{13}y_h - \tfrac14 y_l = 1$ en $-\tfrac{3}{13}y_h + \tfrac14 y_l = 1$.
Optellen geeft $\tfrac{1}{13}y_h = 2$, dus $y_h = 26$. Invullen in de tweede
vergelijking geeft $\tfrac14 y_l = 1 + 6 = 7$, dus $y_l = 28$. Dan is
$\mathrm{PD}_h = 25$ en $\mathrm{PD}_l = 27$.

**Stap 3: de rente.** Een risicovrije euro kost $\E_i[m]$, dus
$1 + R^f_i = 1/\E_i[m]$. De SDF is $\beta g_h^{-2} = 0{,}96/1{,}0816 = 0{,}8876$ na
hoge groei en $\beta g_l^{-2} = 0{,}96/0{,}9216 = 25/24 = 1{,}0417$ na lage groei.
Dan is $\E_h[m] = 0{,}75 \cdot 0{,}8876 + 0{,}25 \cdot 1{,}0417 = 0{,}9261$, en
$R^f_h = 1/0{,}9261 - 1 = 7{,}98\%$. Op dezelfde manier is $\E_l[m] = 1{,}0032$ en
$R^f_l = -0{,}31\%$.

**Stap 4: de premie.** Het rendement $R_{ij} = g_j(1 + \mathrm{PD}_j)/\mathrm{PD}_i$ is
vanuit de hoge toestand $1{,}04 \cdot 26/25 = 1{,}0816$ of
$0{,}96 \cdot 28/25 = 1{,}0752$. Het verwachte rendement is
$0{,}75 \cdot 1{,}0816 + 0{,}25 \cdot 1{,}0752 = 1{,}0800$, tegen
$1 + R^f_h = 1{,}0798$: een premie van ongeveer 2 basispunt. Vanuit de lage
toestand is het verwachte rendement $(0{,}25 \cdot 1{,}04 \cdot 26 + 0{,}75 \cdot 0{,}96 \cdot 28)/27 = 0{,}99704$,
tegen $0{,}99687$: ongeveer 1,7 basispunt.

De code lost hetzelfde stelsel op en controleert de Euler-vergelijking
$\E_i[m\,R] = 1$ in beide toestanden.

```{code-cell} ipython3
beta_toy, gamma_toy = 0.96, 2.0
growth = np.array([1.04, 0.96])                 # dividend = consumption growth, states (h, l)
P = np.array([[0.75, 0.25],
              [0.25, 0.75]])

weights = beta_toy * P * growth ** (1 - gamma_toy)             # beta P_ij g_j^(1-gamma)
pd_toy = np.linalg.solve(np.eye(2) - weights, weights @ np.ones(2))
m_toy = beta_toy * growth ** (-gamma_toy)                      # m depends only on the next state j
rf_toy = 1 / (P @ m_toy) - 1                                   # net risk-free rate
R_toy = growth * (1 + pd_toy) / pd_toy[:, None]                # R_ij = g_j (1 + PD_j) / PD_i
premium_bp = ((P * R_toy).sum(axis=1) - (1 + rf_toy)) * 1e4
euler_toy = (P * m_toy * R_toy).sum(axis=1)

pd.DataFrame(
    {
        "met de hand": [25, 27, 0.0798, -0.0031, 2.0, 1.7, 1.0, 1.0],
        "code": [*pd_toy, *rf_toy, *premium_bp, *euler_toy],
    },
    index=["PD hoog", "PD laag", "rente hoog", "rente laag",
           "premie hoog (bp)", "premie laag (bp)", "E[m R] hoog", "E[m R] laag"],
).round(4)
```

De twee kolommen zijn gelijk, op de afronding van de premie na. In de hoge
toestand is de prijs-dividend-ratio
*lager*, hoewel de verwachte groei hoger is. De rente is daar ruim acht
procentpunt hoger, en bij $\gamma = 2$ wint dat rente-effect van het
groei-effect. De ratio beweegt dus omdat de discontovoet beweegt, het patroon uit
de replicatie van [](#01-03-williams-ddm), nu met een mechanisme erachter. De
premie is een paar basispunt: consumptie schommelt hier $(1{,}04 - 0{,}96)/2 = 4\%$
rond haar gemiddelde, en zo'n schommeling is bij $\gamma = 2$ bijna gratis te verzekeren.
Wat het toy-voorbeeld laat zien: de SDF prijst de boom, en een gladde consumptie
geeft een premie van bijna niets.

## Theorie

We leiden eerst de Euler-vergelijking af: de prijs is de verwachte payoff, gewogen
met de verhouding van marginale nutten. Daarna leggen we het evenwicht van de
Lucas-boom vast en bewijzen dat de prijs-dividend-ratio uniek is. Dan volgen twee
voorspellingen: een gesloten vorm voor rente en premie, en het consumptie-CAPM.
Tot slot de toets van Hansen, die de Euler-vergelijking schat zonder de economie
op te lossen. De kern is de eerste stap. De rest volgt eruit.

### Opzet en aannames

Er is één representatieve belegger met periodenut
$u(c) = c^{1-\gamma}/(1-\gamma)$. Hier is $\gamma > 0$ de relatieve
risicoaversie, bij $\gamma = 1$ is het nut $\log c$. De subjectieve
discontofactor $\beta \in (0,1)$ is in het toy-voorbeeld 0,96 en in de
simulatie 0,98 per jaar. De belegger handelt in $N$ activa. Activum $i$ kost $p_{i,t}$ en betaalt op
$t+1$ de payoff $x_{i,t+1}$, bij een aandeel $p_{i,t+1} + d_{i,t+1}$. Het bruto
rendement is $R_{i,t+1} = x_{i,t+1}/p_{i,t}$, de risicovrije rente $R^f_{t+1}$ is
netto, zoals in de rest van de reeks.

Hansen en Singleton schrijven het nut als $c^{\gamma}/\gamma$ met $\gamma < 1$ en
zetten $\alpha = \gamma - 1$. Hun $-\alpha$ is dus onze $\gamma$: een
geschatte $\hat\alpha = -0{,}931$ bij hen is $\hat\gamma = 0{,}931$ bij ons. Dat is van
belang bij het lezen van hun tabellen in de replicatie.

### Het kernresultaat: de Euler-vergelijking

*Waarom zou dit waar zijn?* Een belegger koopt vandaag een klein extra stukje
van activum $i$ en eet daarvoor vandaag iets minder. Morgen eet hij de payoff op.
Levert dat per saldo nut op, dan koopt hij meer, en de prijs stijgt. Kost het nut,
dan verkoopt hij, en de prijs daalt. De prijs staat stil als het verlies van
vandaag gelijk is aan de verwachte winst van morgen.

Formeel maximeert de belegger $\E_0 \sum_t \beta^t u(c_t)$ onder de
budgetrestrictie $c_t + \sum_i p_{i,t}\, \xi_{i,t+1} = y_t + \sum_i x_{i,t}\, \xi_{i,t}$.
Hier is $\xi_{i,t+1}$ het aantal stukken dat hij van $t$ naar $t+1$ houdt en
$y_t$ zijn overige inkomen. De hoeveelheid $\xi_{i,t+1}$ verlaagt $c_t$ met
$p_{i,t}$ en verhoogt $c_{t+1}$ met $x_{i,t+1}$. De eerste-ordevoorwaarde is

$$
0 = -\beta^t u'(c_t)\, p_{i,t} + \beta^{t+1} \E_t\!\left[u'(c_{t+1})\, x_{i,t+1}\right].
$$

Delen door $\beta^t u'(c_t)$ geeft

```{math}
:label: eq-consumptie-capm-euler
p_{i,t} = \E_t\!\left[m_{t+1}\, x_{i,t+1}\right],
\qquad
m_{t+1} = \beta \frac{u'(c_{t+1})}{u'(c_t)} = \beta \left(\frac{c_{t+1}}{c_t}\right)^{-\gamma}.
```

In woorden: de prijs is de verwachte payoff, gewogen met hoeveel een euro morgen
waard is ten opzichte van een euro vandaag. Die weging is groot als consumptie
morgen laag is. Delen door $p_{i,t}$ geeft dezelfde uitspraak voor rendementen:

```{math}
:label: eq-consumptie-capm-euler-rendement
1 = \E_t\!\left[\beta \left(\frac{c_{t+1}}{c_t}\right)^{-\gamma} R_{i,t+1}\right],
\qquad i = 1, \dots, N .
```

Elk bruto rendement, gewogen met de SDF, heeft verwachting één. Voor de
risicovrije claim is het rendement bekend op $t$, dus $1 + R^f_{t+1} = 1/\E_t[m_{t+1}]$:
stap 3 van het toy-voorbeeld.

De vergelijking geldt voor elke belegger die vrij in activum $i$ kan handelen,
wat er verder ook met zijn inkomen gebeurt {cite}`GrossmanShiller1981`. Pas
wanneer we geaggregeerde consumptie invullen, nemen we een representatieve
belegger aan. Het is de SDF uit [](#03-11-apt-no-arbitrage), nu met een naam.
Geen arbitrage zegt dat er een positieve $m_{t+1}$ is. De Euler-vergelijking zegt
welke.

### De discontovoet krijgt een theorie

De discontovoet van elk activum volgt nu uit $\beta$, $\gamma$ en consumptie, en is
daardoor toetsbaar.

*Waarom zou dit waar zijn?* De Euler-vergelijking zegt, net als Williams, dat de
prijs van vandaag de verdisconteerde prijs plus het dividend van morgen is. Wie
die stap steeds opnieuw zet, krijgt weer een contante waarde. Alleen is de
discontofactor nu hoog in slechte tijden en laag in goede.

Vul in [](#eq-consumptie-capm-euler) $x_{t+1} = p_{t+1} + d_{t+1}$ in, herhaal
dat voor $p_{t+1}$, $p_{t+2}$, enzovoort, en neem aan dat de verdisconteerde prijs
ver in de toekomst naar nul gaat. Dan is

```{math}
:label: eq-consumptie-capm-contante-waarde
p_t = \E_t \sum_{j=1}^{\infty} \beta^j \frac{u'(c_{t+j})}{u'(c_t)}\, d_{t+j} .
```

De prijs is de som van alle toekomstige dividenden, elk gewogen met het
marginale nut op het moment van uitkeren. Vergelijk dit met de formule van
Williams, [](#eq-williams-ddm-ddm), die $(1+r)^{-j}$ schreef waar hier
$\beta^j u'(c_{t+j})/u'(c_t)$ staat. De vrije parameter $r$ is vervangen door twee
voorkeursparameters en een meetbaar consumptieproces. Daarom heet dit een theorie
van de discontovoet: de discontovoet van elk activum op elk moment volgt uit
dezelfde $\beta$ en $\gamma$, en de data kunnen hem verwerpen. Let op het
verschil in namen. De SDF $m_{t+1}$ is één en dezelfde voor alle activa. De
discontovoet is het verwachte rendement dat de markt voor één activum eist, en
die verschilt per activum omdat elke payoff anders met $m_{t+1}$ samenhangt.

### Evenwicht in de Lucas-boom

Zonder een eindige, unieke prijs valt er niets te toetsen. Deze stap laat zien
wanneer de Lucas-boom die prijs heeft.

*Waarom zou dit waar zijn?* In evenwicht houdt iemand de hele boom en eet iemand
het hele dividend. Consumptiegroei is dan dividendgroei. Hoeveel een belegger
voor een euro dividend betaalt, hangt dan alleen af van wat hij over de groei van
morgen verwacht, niet van het niveau van vandaag.

Laat de groei $g_{t+1} = d_{t+1}/d_t$ afhangen van een Markov-toestand $s_t$ met
overgangskans $Q(s, \mathrm{d}s')$. In het toy-voorbeeld is $Q(s, \cdot)$ de rij
van de overgangsmatrix $P$ bij toestand $s$, en is de integraal hieronder een som
over twee toestanden. Zet $c_t = d_t$ en $p_t = \mathrm{PD}(s_t)\, d_t$ in
[](#eq-consumptie-capm-euler) en deel door $d_t$:

```{math}
:label: eq-consumptie-capm-pd
\mathrm{PD}(s) = \beta \int g(s')^{1-\gamma} \left(1 + \mathrm{PD}(s')\right) Q(s, \mathrm{d}s')
\;\equiv\; (T\,\mathrm{PD})(s) .
```

De ratio van vandaag is het gewogen gemiddelde van één plus de ratio van morgen.
Het gewicht is de kans maal $\beta g^{1-\gamma}$. De prijs-dividend-functie is dus
een vast punt van de *Lucas-operator* $T$. In het toy-voorbeeld was dit het
$2 \times 2$-stelsel van stap 2.

:::{prf:theorem} De Lucas-operator is een contractie
:label: thm-consumptie-capm-contractie

Definieer
$\delta \equiv \beta \sup_{s} \int g(s')^{1-\gamma}\, Q(s, \mathrm{d}s')$.
Als $\delta < 1$, dan is $T$ uit [](#eq-consumptie-capm-pd) een contractie met
modulus $\delta$ op de begrensde functies met de supremumnorm:
$\|Tf - Th\| \le \delta \|f - h\|$. Er is dan één begrensde
prijs-dividend-functie $\mathrm{PD}^*$, en iteratie vanuit elke startwaarde
convergeert ernaartoe met snelheid $\delta^n$.
:::

:::{prf:proof}
:class: dropdown

We gebruiken de voldoende voorwaarden van Blackwell {cite}`Blackwell1965`.
*Monotonie:* als $f \le h$, dan $Tf \le Th$, want het gewicht
$\beta g(s')^{1-\gamma} Q(s, \mathrm{d}s')$ is niet-negatief. *Verdiscontering:*
voor een constante $a \ge 0$ is $T(f + a) \le Tf + \delta a$. Nu is
$f \le h + \|f - h\|$, dus $Tf \le Th + \delta\|f-h\|$. Met de rollen verwisseld
volgt $\|Tf - Th\| \le \delta \|f - h\|$. De begrensde functies met de
supremumnorm vormen een volledige ruimte, dus de contractiestelling van Banach
geeft één vast punt en convergentie met snelheid $\delta^n$. $\square$
:::

De voorwaarde $\delta < 1$ is economisch. Het nut-gewogen dividend mag in geen
enkele toestand in verwachting sneller groeien dan $1/\beta$. Anders is
[](#eq-consumptie-capm-contante-waarde) oneindig, zoals het Gordon-model ontploft
bij $g \ge r$. In het toy-voorbeeld is $\delta$ de grootste rijsom van de
gewichten uit stap 1: $\max(9/13 + 1/4;\ 3/13 + 3/4) = 0{,}9808$.

### Wat het voorspelt: rente en premie bij lognormale groei

*Waarom zou dit waar zijn?* Als groei onafhankelijk is van het verleden, weet
een belegger op $t$ nooit meer over morgen dan op een ander moment. Dan heeft de
prijs-dividend-ratio geen reden om te bewegen. Een aandeel waarvan het dividend
sterker meebeweegt dan consumptie, valt harder in slechte tijden en moet meer
opleveren.

Laat log-consumptiegroei normaal en onafhankelijk verdeeld zijn, en laat het
dividend met een hefboom op consumptie reageren:

$$
\Delta c_{t+1} = \log\frac{c_{t+1}}{c_t} \sim N(\mu, \sigma^2), \qquad
\log g^{d}_{t+1} = \mu_d + \phi\left(\Delta c_{t+1} - \mu\right) + \sigma_d\, \varepsilon_{t+1}.
$$

Hier is $\phi$ de *leverage* (hefboom) van het dividend op consumptie en
$\varepsilon_{t+1} \sim N(0,1)$ onafhankelijk dividendrisico. De oorspronkelijke
Lucas-boom heeft $\phi = 1$, $\sigma_d = 0$ en $\mu_d = \mu$.

:::{prf:proposition} Lucas-boom met lognormale groei
:label: prf-consumptie-capm-lognormaal

Definieer $k \equiv \beta \exp\!\big(\mu_d - \gamma\mu + \tfrac12[(\phi-\gamma)^2\sigma^2 + \sigma_d^2]\big)$
en neem aan dat $k < 1$. Dan is de prijs-dividend-ratio constant, en

```{math}
:label: eq-consumptie-capm-lognormaal
\mathrm{PD} = \frac{k}{1-k}, \qquad
\log (1 + R^f) = -\log\beta + \gamma\mu - \tfrac12 \gamma^2 \sigma^2, \qquad
\log \E[R^{m}] - \log (1 + R^f) = \gamma\phi\sigma^2 .
```
:::

:::{prf:proof}
:class: dropdown

Probeer een constante $\mathrm{PD}$. Dan is $R^m_{t+1} = g^d_{t+1}(1 + \mathrm{PD})/\mathrm{PD}$,
en de Euler-vergelijking wordt $\mathrm{PD} = \E[\beta (g^c)^{-\gamma} g^d]\,(1 + \mathrm{PD})$.
De log van $(g^c)^{-\gamma} g^d$ is normaal met verwachting $\mu_d - \gamma\mu$ en
variantie $(\phi-\gamma)^2\sigma^2 + \sigma_d^2$. Met $\E[e^X] = e^{\E X + \Var X/2}$
is $\beta\E[(g^c)^{-\gamma} g^d] = k$, dus $\mathrm{PD} = k/(1-k)$. Voor de rente is
$1/(1+R^f) = \beta \E[(g^c)^{-\gamma}] = \beta \exp(-\gamma\mu + \tfrac12\gamma^2\sigma^2)$.
Voor de premie is $\E[R^m] = \E[g^d]/k$ met
$\E[g^d] = \exp(\mu_d + \tfrac12(\phi^2\sigma^2 + \sigma_d^2))$. Aftrekken van de
logs geeft $\tfrac12\sigma^2\left(\phi^2 - (\phi-\gamma)^2 + \gamma^2\right) = \gamma\phi\sigma^2$.
$\square$
:::

De rente bevat twee krachten. De term $\gamma\mu$ zegt dat verwachte groei lenen
aantrekkelijk maakt: de eerste voorspelling uit de intuïtie. De term
$-\tfrac12\gamma^2\sigma^2$ is voorzorgssparen: meer onzekerheid maakt sparen
aantrekkelijk en drukt de rente. Een hogere $\gamma$ versterkt beide. De rente
stijgt dus met $\gamma$ zolang $\gamma < \mu/\sigma^2$. Bij de kalibratie hieronder
($\mu = 1{,}8\%$, $\sigma = 3{,}5\%$) is dat $0{,}018/0{,}035^2 \approx 14{,}7$. Een andere
kalibratie geeft een andere drempel. Daarboven wint het voorzorgssparen.
Met de parameters van de simulatie hierna ($\beta = 0{,}98$, $\gamma = 4$,
$\mu = 1{,}8\%$, $\sigma = 3{,}5\%$) is $\log(1+R^f) = 0{,}0202 + 0{,}0720 - 0{,}0098 = 0{,}0824$,
een rente van 8,6%.

De premie is het product van
risicoaversie, hefboom en de variantie van consumptiegroei. Met $\gamma = 2$,
$\phi = 1$ en $\sigma = 3{,}5\%$ is dat $2 \times 0{,}035^2 = 0{,}25\%$ per jaar.
Dat is de derde voorspelling uit de intuïtie, nu met een getal: de premie is
klein en kan alleen groeien via $\gamma$ of $\phi$. Hoe klein naast de
historische premie, is het onderwerp van [](#03-13-equity-premium-puzzle).

### Wat het voorspelt: het consumptie-CAPM

*Waarom zou dit waar zijn?* Als de SDF een functie van consumptie is, wordt
alleen risico beloond dat met consumptie samenhangt. Een activum dat slecht
rendeert als consumptie daalt, verergert de klap, en beleggers kopen het alleen
tegen een premie. Een activum dat van consumptie onafhankelijk is, draagt niets
bij aan wat telt, hoe volatiel het ook is. Breeden liet zien dat dit in continue
tijd exact geldt, ook als de beleggingsmogelijkheden veranderen
{cite}`Breeden1979`. In [Mertons intertemporele CAPM](#03-10-merton-icapm) kopen
beleggers extra van een activum dat goed rendeert als de rente daalt, om hun
toekomstige beleggingskansen af te dekken. Zo'n hedge-motief zit volgens Breeden
al in consumptie, want een belegger die slechtere kansen verwacht, consumeert nu
minder.

Eerst een exacte stap. Schrijf $R^e = R - (1 + R^f)$. Trek
[](#eq-consumptie-capm-euler-rendement) voor de risicovrije claim af van die voor
activum $i$. Dan is $0 = \E_t[m R^e_i] = \E_t[m]\E_t[R^e_i] + \Cov_t(m, R^e_i)$, en
delen door $\E_t[m] = 1/(1+R^f)$ geeft

```{math}
:label: eq-consumptie-capm-cov
\E_t\!\left[R^{e}_{i,t+1}\right] = -(1+R^f_{t+1})\, \Cov_t\!\left(m_{t+1}, R^{e}_{i,t+1}\right).
```

Een activum dat hoog betaalt als $m$ hoog is, krijgt dus een lagere premie. Vul
voor de markt $m_{t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$ in. Dan valt $\beta$ weg:

```{math}
:label: eq-consumptie-capm-excess
0 = \E\!\left[\left(\frac{c_{t+1}}{c_t}\right)^{-\gamma} R^{e}_{m,t+1}\right],
\qquad R^{e}_{m,t+1} = R^m_{t+1} - (1 + R^f_{t+1}).
```

Het met $(c_{t+1}/c_t)^{-\gamma}$ gewogen excess rendement heeft verwachting nul. De
replicatie gebruikt deze vorm om de $\gamma$ te vinden die alleen de premie
verklaart. De stelling vertaalt [](#eq-consumptie-capm-cov) naar consumptie.

:::{prf:theorem} Consumptiebèta
:label: thm-consumptie-capm-beta

Laat $\Delta c_{t+1} = \log(c_{t+1}/c_t)$. De consumptiebèta $\beta_{i,\Delta c}$,
met twee indices, is een regressiecoëfficiënt; $\beta$ zonder index blijft de
subjectieve discontofactor. Met $m_{t+1} \approx \beta\left(1 - \gamma\,\Delta c_{t+1}\right)$ en
$\beta(1 + R^f_{t+1}) \approx 1$ volgt uit [](#eq-consumptie-capm-cov)

```{math}
:label: eq-consumptie-capm-ccapm
\E_t\!\left[R^{e}_{i,t+1}\right] \approx \gamma\, \Cov_t\!\left(R^{e}_{i,t+1}, \Delta c_{t+1}\right)
= \beta_{i,\Delta c}\, \lambda_{\Delta c},
\qquad
\beta_{i,\Delta c} = \frac{\Cov_t(R^{e}_{i}, \Delta c)}{\Var_t(\Delta c)},
\quad
\lambda_{\Delta c} = \gamma \Var_t(\Delta c) .
```
:::

:::{prf:proof}
De benadering geeft $\Cov_t(m, R^e_i) \approx -\beta\gamma\Cov_t(\Delta c, R^e_i)$, en
$\beta(1+R^f) \approx 1$ levert [](#eq-consumptie-capm-ccapm). $\square$
:::

[](#eq-consumptie-capm-ccapm) zegt: de premie is de consumptiebèta maal één prijs van risico,
gelijk voor alle activa. Zoals de intuïtie voorspelde, groeit de premie met de
covariantie, met $\gamma$ als factor ervoor. Een hogere $\gamma$ of een
volatielere consumptie maakt de prijs van risico groter. Met $\gamma = 2$ en
$\sigma = 3{,}5\%$ is $\lambda_{\Delta c} = 0{,}25\%$, hetzelfde getal als bij de
lognormale boom, waar de bèta van de boom één is.

De vorm is die van het CAPM uit [](#02-08-capm): een verwacht excess rendement
evenredig met een bèta. Alleen de factor is anders. Consumptie is geen
verhandelde portefeuille, dus $\lambda_{\Delta c}$ is geen gemiddeld rendement
maar $\gamma$ maal een variantie. In Breedens continue tijd, en voor
log-rendementen in de lognormale boom, is de benadering exact.

### Hoe het getoetst wordt: GMM

*Waarom zou dit waar zijn?* Wie [](#eq-consumptie-capm-pd) wil oplossen, moet de
verdeling van consumptie en dividenden kennen. De Euler-vergelijking zegt iets
wat van die verdeling onafhankelijk is. Stel dat een onderzoeker de fout
$e_{i,t+1} = \beta (c_{t+1}/c_t)^{-\gamma} R_{i,t+1} - 1$ uitrekent. Die fout heeft
verwachting nul gegeven alles wat op $t$ bekend is. Hij mag dus niet samenhangen
met wat de belegger toen wist, zoals de consumptiegroei van vorig kwartaal. Kies
$\beta$ en $\gamma$ zo dat die samenhang in de steekproef zo klein mogelijk is,
en toets of dat lukt.

Zo'n bekende variabele heet een *instrument* $z_t$, bijvoorbeeld een constante
of het rendement van vorig kwartaal. Met $L$ instrumenten, $N$ activa en
$\theta = (\beta, \gamma)$ stapelen we de momenten. Het Kronecker-product
$\otimes$ vermenigvuldigt elke Euler-fout met elk instrument. Bij $N = 2$ en
$L = 3$, zoals in de simulatie, zijn dat zes momenten:

```{math}
:label: eq-consumptie-capm-momenten
h_{t+1}(\theta) = e_{t+1}(\theta) \otimes z_t \in \mathbb{R}^{NL},
\qquad
\E\!\left[h_{t+1}(\theta_0)\right] = 0,
\qquad
\bar g_T(\theta) = \frac1T \sum_{t} h_{t+1}(\theta).
```

Elk element van $h$ is een Euler-fout maal een instrument, en in de ware
parameters $\theta_0$ is zijn verwachting nul. Dat zijn $NL$ *momentvoorwaarden*.
De GMM-schatter minimaliseert de gewogen afstand
$\bar g_T(\theta)' \mathbf{W}\, \bar g_T(\theta)$ met een weegmatrix $\mathbf{W}$.

:::{prf:theorem} Hansen (1982)
:label: thm-consumptie-capm-gmm

Stel dat $h_{t+1}(\theta)$ stationair en ergodisch is, dat $\E[h(\theta)] = 0$
alleen in $\theta_0$, dat $\mathbf{D} = \E[\partial h/\partial\theta']$ volle
kolomrang $K$ heeft (het aantal parameters, hier 2), en dat
$\sqrt{T}\,\bar g_T(\theta_0) \to N(0, \mathbf{S})$, met $\mathbf{S}$ de
langetermijncovariantiematrix van de momenten.
Dan is $\hat\theta$ consistent en asymptotisch normaal. De asymptotische variantie
is het kleinst bij $\mathbf{W} = \mathbf{S}^{-1}$ en is dan
$(\mathbf{D}'\mathbf{S}^{-1}\mathbf{D})^{-1}/T$.
:::

:::{prf:corollary} De $J$-toets
Met $\mathbf{W}_T = \hat{\mathbf{S}}^{-1}$ geldt onder de voorwaarden van
[](#thm-consumptie-capm-gmm)

```{math}
:label: eq-consumptie-capm-j
J_T = T\, \bar g_T(\hat\theta)'\, \hat{\mathbf{S}}^{-1} \bar g_T(\hat\theta) \;\to\; \chi^2(NL - K).
```
:::

:::{prf:proof}
:class: dropdown

*Schets.* Een Taylor-ontwikkeling
$\bar g_T(\hat\theta) \approx \bar g_T(\theta_0) + \mathbf{D}(\hat\theta - \theta_0)$ in de
eerste-ordevoorwaarde geeft
$\sqrt{T}(\hat\theta - \theta_0) \approx -\mathbf{A}\sqrt{T}\bar g_T(\theta_0)$ met
$\mathbf{A} = (\mathbf{D}'\mathbf{W}\mathbf{D})^{-1}\mathbf{D}'\mathbf{W}$. De
centrale limietstelling geeft normaliteit met variantie $\mathbf{A}\mathbf{S}\mathbf{A}'$.
Voor elke $\mathbf{A}$ met $\mathbf{A}\mathbf{D} = \mathbf{I}$ is het verschil met
$\mathbf{A}_0 = (\mathbf{D}'\mathbf{S}^{-1}\mathbf{D})^{-1}\mathbf{D}'\mathbf{S}^{-1}$
gelijk aan $(\mathbf{A}-\mathbf{A}_0)\mathbf{S}(\mathbf{A}-\mathbf{A}_0)' \succeq 0$.
Met $\mathbf{W} = \mathbf{S}^{-1}$ is $\mathbf{S}^{-1/2}\sqrt{T}\bar g_T(\hat\theta)$
asymptotisch een projectie van een standaardnormale vector op een ruimte van
dimensie $NL - K$, dus $J_T \to \chi^2(NL-K)$. $\square$
:::

De toets $J_T$ is de gewogen afstand van de momenten tot
nul. Met twee parameters en $NL$ momenten legt het model $NL - 2$ restricties op
die de data hadden kunnen schenden. Een grote $J_T$ betekent dat geen enkel paar
$(\beta, \gamma)$ tegelijk de rente, het aandelenrendement en hun
voorspelbaarheid kan dragen.

De code volgt de stelling in twee stappen: eerst $\mathbf{W} = \mathbf{I}$, dan
$\mathbf{W} = \hat{\mathbf{S}}^{-1}$. De implementatiedetails staan als commentaar
in de code.

```{code-cell} ipython3
def euler_moments(gamma, gc, R, Z):
    """Pieces a_t(gamma), b_t with h_t(beta, gamma) = beta * a_t - b_t.

    gc : (T,) gross consumption growth c_{t+1}/c_t
    R  : (T, N) gross returns R_{t+1}
    Z  : (T, L) instruments known at t
    """
    scaled = gc[:, None] ** (-gamma) * R                       # g^-gamma R, per asset
    a_blocks, b_blocks = [], []
    for n in range(R.shape[1]):                                # Kronecker product: asset n
        a_blocks.append(scaled[:, [n]] * Z)                    # times every instrument
        b_blocks.append(Z)
    return np.hstack(a_blocks), np.hstack(b_blocks)


def gmm_euler(gc, R, Z, gamma_grid=np.linspace(-5, 200, 411)):
    """Two-step GMM for 1 = E[beta g^-gamma R (x) z], beta concentrated out."""
    T = len(gc)
    n_mom = R.shape[1] * Z.shape[1]
    W = np.eye(n_mom)

    def concentrated(gamma, W):
        # the moments are linear in beta, so beta is solved exactly for each gamma
        a_t, b_t = euler_moments(gamma, gc, R, Z)
        a, b = a_t.mean(axis=0), b_t.mean(axis=0)
        beta = (a @ W @ b) / (a @ W @ a)
        g = beta * a - b
        return g @ W @ g, beta

    for _ in range(2):                                    # step 1: W = I, step 2: W = S^-1
        # search gamma on a grid, then refine between the neighbours of the best point
        values = np.array([concentrated(x, W)[0] for x in gamma_grid])
        i = int(np.argmin(values))
        lo, hi = gamma_grid[max(i - 1, 0)], gamma_grid[min(i + 1, len(gamma_grid) - 1)]
        gamma = optimize.minimize_scalar(
            lambda x: concentrated(x, W)[0], bounds=(lo, hi), method="bounded"
        ).x
        beta = concentrated(gamma, W)[1]
        a, b = euler_moments(gamma, gc, R, Z)
        h = beta * a - b
        S = h.T @ h / T                                   # Euler errors are an MDS under H0
        W = np.linalg.inv(S)

    g = h.mean(axis=0)
    J = T * g @ W @ g
    # D: derivative of beta g^-gamma R z to beta (a) and to gamma (-log g * beta * a)
    D = np.column_stack([a.mean(axis=0), (beta * (-np.log(gc))[:, None] * a).mean(axis=0)])
    V = np.linalg.pinv(D.T @ W @ D) / T
    dof = n_mom - 2
    return {
        "beta": beta, "gamma": gamma,
        "se_beta": np.sqrt(V[0, 0]), "se_gamma": np.sqrt(V[1, 1]),
        "J": J, "df": dof, "p": stats.chi2.sf(J, dof) if dof > 0 else np.nan,
    }
```

`gmm_euler` geeft $\hat\beta$, $\hat\gamma$, hun standaardfouten uit de stelling,
en $J_T$ met zijn $p$-waarde. De simulatie en de replicatie gebruiken deze ene
functie.

```{admonition} Samengevat
:class: tip

- De prijs is de verwachte payoff gewogen met de SDF
  $m_{t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$, [](#eq-consumptie-capm-euler); de rente
  is $1/\E_t[m] - 1$.

- In de Lucas-boom is de prijs-dividend-ratio het unieke vaste punt van
  [](#eq-consumptie-capm-pd) als $\delta < 1$, [](#thm-consumptie-capm-contractie).

- Bij lognormale groei stijgt de rente met $\gamma\mu$ en is de premie
  $\gamma\phi\sigma^2$, [](#eq-consumptie-capm-lognormaal): klein, tenzij $\gamma$
  of $\phi$ groot is.

- De premie is de consumptiebèta maal $\gamma\Var(\Delta c)$,
  [](#eq-consumptie-capm-ccapm).

- GMM schat $\beta$ en $\gamma$ uit [](#eq-consumptie-capm-momenten) en toetst de
  restricties met $J_T$, [](#eq-consumptie-capm-j). De simulatie toetst hoe
  nauwkeurig dat is op zeventig jaar data.
```

## Simulatie: GMM op zeventig jaar uit een Lucas-boom

Hoe nauwkeurig schatten Hansen en Singleton $\gamma$, en hoe vaak verwerpt hun
toets een waar model, als ze zeventig jaar data hebben? We bouwen een wereld
waarin de Euler-vergelijking exact geldt: de lognormale boom uit
[](#prf-consumptie-capm-lognormaal), met jaarparameters $\beta = 0{,}98$ en
$\gamma = 4$. Die $\gamma$ is twee keer die van het toy-voorbeeld, zodat de premie
groot genoeg is om iets te schatten. $\beta$ is hoger zodat de rente niet nog
verder oploopt. Consumptie groeit met $\mu = 1{,}8\%$ en $\sigma = 3{,}5\%$. Het
dividend heeft hefboom $\phi = 3$ en eigen risico $\sigma_d = 10\%$. Zonder die
hefboom bleef de premie steken op $4 \cdot 0{,}035^2 = 0{,}49\%$. Met hefboom drie is
ze volgens [](#eq-consumptie-capm-lognormaal) drie keer zo groot. De cel rekent de populatiewaarden uit en controleert de
Euler-vergelijking op een miljoen gesimuleerde jaren.

```{code-cell} ipython3
tree = {"beta": 0.98, "gamma": 4.0, "mu": 0.018, "sigma": 0.035, "leverage": 3.0, "sigma_d": 0.10}

k_tree = tree["beta"] * np.exp(
    tree["mu"] - tree["gamma"] * tree["mu"]
    + 0.5 * ((tree["leverage"] - tree["gamma"]) ** 2 * tree["sigma"] ** 2 + tree["sigma_d"] ** 2)
)
pd_tree = k_tree / (1 - k_tree)
rf_gross = 1 / (tree["beta"] * np.exp(-tree["gamma"] * tree["mu"] + 0.5 * tree["gamma"] ** 2 * tree["sigma"] ** 2))
premium_tree = np.exp(tree["gamma"] * tree["leverage"] * tree["sigma"] ** 2) - 1   # E[R^m]/(1 + R^f) - 1


def simulate_tree(n_years):
    """Gross consumption growth, gross stock return and gross risk-free return."""
    log_gc = rng.normal(tree["mu"], tree["sigma"], n_years)
    log_gd = tree["mu"] + tree["leverage"] * (log_gc - tree["mu"]) + tree["sigma_d"] * rng.normal(size=n_years)
    stock = (1 + pd_tree) / pd_tree * np.exp(log_gd)
    return np.exp(log_gc), stock, np.full(n_years, rf_gross)


gc_big, rm_big, rf_big = simulate_tree(1_000_000)
m_big = tree["beta"] * gc_big ** -tree["gamma"]
pd.Series(
    {
        "prijs-dividend-ratio": pd_tree,
        "rente R^f": rf_gross - 1,
        "premie E[R^m]/(1+R^f) - 1": premium_tree,
        "SD aandeelrendement": rm_big.std(),
        "E[m R^m] (moet 1 zijn)": np.mean(m_big * rm_big),
        "E[m (1+R^f)] (moet 1 zijn)": np.mean(m_big * rf_big),
    }
).round(4)
```

De premie is 1,5% per jaar bij een aandeelvolatiliteit van 16%, en beide
Euler-vergelijkingen kloppen op drie decimalen. De rente van 8,6% is absurd hoog.
Dat is geen fout in de code maar de term $\gamma\mu$ uit
[](#eq-consumptie-capm-lognormaal). Nu schatten we het model 500 keer, elk op
zeventig jaar. De instrumenten zijn een constante, de consumptiegroei van vorig
jaar en het aandeelrendement van vorig jaar. Met twee activa zijn dat zes
momenten, en heeft $J_T$ vier vrijheidsgraden.

```{code-cell} ipython3
n_years, n_rep = 70, 500
mc_rows = []
for _ in range(n_rep):
    gc, rm, rf = simulate_tree(n_years + 1)
    Z = np.column_stack([np.ones(n_years), gc[:-1], rm[:-1]])
    res = gmm_euler(gc[1:], np.column_stack([rm, rf])[1:], Z, gamma_grid=np.linspace(-20, 60, 41))
    mc_rows.append(res)
mc = pd.DataFrame(mc_rows)

pd.DataFrame(
    {
        "waarheid of nominaal": [tree["gamma"], np.nan, np.nan, np.nan, np.nan, np.nan,
                                 0.05, stats.chi2.ppf(0.95, 4)],
        "simulatie": [
            mc.gamma.median(), mc.gamma.quantile(0.05), mc.gamma.quantile(0.95),
            mc.gamma.std(), mc.se_gamma.median(), (mc.beta > 1).mean(),
            (mc.p < 0.05).mean(), mc.J.quantile(0.95),
        ],
    },
    index=["gamma-dak, mediaan", "gamma-dak, 5e percentiel", "gamma-dak, 95e percentiel",
           "gamma-dak, werkelijke spreiding (SD)", "SE(gamma-dak), mediaan van GMM",
           "aandeel discontofactor-dak > 1 (waarheid 0,98)", "aandeel J verwerpt op 5%",
           "95e percentiel van J"],
).round(3)
```

De tabel laat vier zwakke punten van de schatter zien.

- **De spreiding van $\hat\gamma$ is groot.** Tussen het 5e en 95e percentiel
  loopt $\hat\gamma$ van ongeveer $-3$ tot 12, rond een waarheid van 4. De mediaan
  van 2,8 ligt onder de waarheid, dus de schatter is ook scheef.

- **GMM onderschat die spreiding.** De mediane gerapporteerde standaardfout is
  ongeveer 1,5, de werkelijke spreiding bijna drie keer zo groot. De formule uit
  [](#thm-consumptie-capm-gmm) geldt pas bij grote $T$.

- **De toets verwerpt te vaak.** Een waar model wordt in ongeveer één op de tien
  steekproeven verworpen, twee keer de nominale 5%. Het 95e percentiel van $J_T$
  ligt boven de kritieke waarde 9,49 van $\chi^2(4)$.

- **$\hat\beta$ komt vaak boven één.** Dat gebeurt in 29% van de steekproeven,
  hoewel de ware $\beta$ 0,98 is. Een te hoge $\hat\gamma$ wordt gecompenseerd met een
  te hoge $\hat\beta$. Een $\hat\beta$ boven één in de replicatie is dus op zich geen
  teken van een fout model.

Dat $\hat\gamma$ zo slecht gemeten is, is de standaardfout van 2% uit
[](#00-01-rendementen): een gemiddeld rendement is over een mensenleven nauwelijks
te meten. Zonder voorspelbaarheid komt de informatie over $\gamma$ vooral uit
het gemiddelde excess rendement, gedeeld door zijn covariantie met consumptie. De
covariantie is goed gemeten. Het gemiddelde heeft bij 16% volatiliteit een
standaardfout van $16/\sqrt{70} \approx 1{,}9$ procentpunt, groter dan de premie
zelf. Let in de figuur links op hoe ver de schattingen van de zwarte lijn
bij 4 liggen, en rechts op hoeveel massa voorbij de gestippelde kritieke waarde
valt.

```{code-cell} ipython3
:label: cel-consumptie-capm-mc
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].hist(mc.gamma.clip(-20, 30), bins=40, edgecolor="white")
axes[0].axvline(tree["gamma"], color="black", lw=1.4)
axes[0].set_xlabel("Geschatte $\\hat\\gamma$")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].set_title("Risicoaversie uit 70 jaar data (waarheid: 4)")

j_grid = np.linspace(0, 25, 300)
axes[1].hist(mc.J, bins=40, density=True, edgecolor="white", label="gesimuleerde $J$")
axes[1].plot(j_grid, stats.chi2.pdf(j_grid, 4), color="black", lw=1.4, label="$\\chi^2(4)$")
axes[1].axvline(stats.chi2.ppf(0.95, 4), color="black", ls="--", lw=1, label="5%-kritieke waarde")
axes[1].set_xlim(0, 25)
axes[1].set_xlabel("$J$-statistiek")
axes[1].set_ylabel("Dichtheid")
axes[1].set_title("De overidentificatietoets als het model waar is")
axes[1].legend()
plt.show()
```

:::{figure} #cel-consumptie-capm-mc
:label: fig-consumptie-capm-mc
:width: 100%

Links: 500 schattingen van $\gamma$ uit zeventig jaar data, in een economie
waarin $\gamma = 4$ waar is. Wie één steekproef heeft, kan niet uitsluiten dat
beleggers risiconeutraal zijn, en evenmin dat ze drie keer zo risicomijdend zijn.
Rechts: $J_T$ ligt verder naar rechts dan $\chi^2(4)$, dus de toets verwerpt een
waar model vaker dan 5%.
:::

Een verwerping met $p = 0{,}03$ op zeventig jaar data zegt dus weinig. Een
verwerping met een $p$-waarde die op vier decimalen nul is, zegt wel iets, en die
zien we in de replicatie.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Hansen en Singleton, *Stochastic Consumption, Risk Aversion, and the
Temporal Behavior of Asset Returns*, Journal of Political Economy 1983
{cite}`HansenSingleton1983`, met de GMM-aanpak uit {cite:t}`HansenSingleton1982`.

**Wat.** $\hat\gamma$ en de toets van de restricties voor (a) alleen de T-bill,
(b) alleen aandelen en (c) beide samen, uit hun tabellen 4, 1 en 5.

**Data hier.** Reële consumptie per hoofd van niet-duurzame goederen en diensten
uit FRED, kwartaaldata, en het marktrendement en de T-bill uit Kenneth French,
beide via `hap.data`; steekproeven 1947–2019 en 1959–1978.

**Verschil met het origineel.** Zij gebruikten maanddata 1959–1978, twee tot zes
vertragingen als instrumenten en in 1983 maximum likelihood. Wij gebruiken
kwartaaldata, GMM en één vertraging van consumptiegroei, aandeelrendement en
T-bill.

**Verwachte afwijking.** Het patroon moet terugkomen: (a) een kleine, precieze
$\hat\gamma$ en verwerping; (b) een standaardfout van $\hat\gamma$ boven 2 en geen
verwerping; (c) verwerping. Draait (a) of (c) om, dan zit er een fout in de code.
```

### De data

De cel bouwt reële kwartaalgroei van consumptie, het reële marktrendement en het
reële T-bill-rendement. Reeksen en deflatie staan in de code.

```{code-cell} ipython3
def fred_series(code):
    return hap_data.fred(code)[code]

cons = pd.DataFrame(
    {
        "nondurables": fred_series("A796RX0Q048SBEA"),   # real per capita, chained 2017 dollars
        "services": fred_series("A797RX0Q048SBEA"),
        "p_nondurables": fred_series("DNDGRD3Q086SBEA"),
        "p_services": fred_series("DSERRD3Q086SBEA"),
    }
)
cons["c"] = cons.nondurables + cons.services              # adding chained dollars is an approximation
cons["deflator"] = (cons.nondurables * cons.p_nondurables
                    + cons.services * cons.p_services) / cons.c
cons.index = cons.index.to_period("Q")

market = hap_data.market_monthly()
market_q = (1 + market[["Mkt", "RF"]]).groupby(market.index.to_period("Q")).prod()

quarterly = cons[["c", "deflator"]].join(market_q, how="inner")
inflation = quarterly.deflator / quarterly.deflator.shift(1)
quarterly["gc"] = quarterly.c / quarterly.c.shift(1)
quarterly["Rm"] = quarterly.Mkt / inflation
quarterly["Rf"] = quarterly.RF / inflation
quarterly = quarterly[["gc", "Rm", "Rf"]].dropna()
main = quarterly.loc[:"2019Q4"]                             # the 2020 lockdown quarters: exercise 3
print(f"steekproef {main.index[0]} t/m {main.index[-1]}, {len(main)} kwartalen")
```

De hoofdsteekproef loopt tot en met 2019. De volgende cel vat de drie reeksen en
het excess rendement samen.

```{code-cell} ipython3
summary = pd.DataFrame(
    {
        "gemiddelde (%/kw)": main.sub([1, 1, 1]).mean() * 100,
        "std.dev. (%/kw)": main.std() * 100,
        "SE gemiddelde (%/kw)": main.std() / np.sqrt(len(main)) * 100,
        "corr. met c-groei": main.corr()["gc"],
    }
)
summary.loc["excess Rm - Rf"] = [
    (main.Rm - main.Rf).mean() * 100,
    (main.Rm - main.Rf).std() * 100,
    (main.Rm - main.Rf).std() / np.sqrt(len(main)) * 100,
    np.corrcoef(main.Rm - main.Rf, main.gc)[0, 1],
]
summary.index = ["consumptiegroei", "reëel marktrendement", "reëel T-bill-rendement", "excess rendement"]
summary.round(3)
```

De tabel bevat het hele probleem. Consumptiegroei is glad, het excess rendement
is zestien keer zo volatiel, en hun correlatie is laag. De covariantie die
volgens [](#eq-consumptie-capm-ccapm) de premie moet dragen, is dus minuscuul,
terwijl de premie zelf groot is en onnauwkeurig gemeten.

### De schattingen

We schatten de drie specificaties op de naoorlogse steekproef en op de
steekproef van Hansen en Singleton.

```{code-cell} ipython3
def estimate_table(frame):
    gc, rm, rf = frame.gc.to_numpy(), frame.Rm.to_numpy(), frame.Rf.to_numpy()
    Z = np.column_stack([np.ones(len(gc) - 1), gc[:-1], rm[:-1], rf[:-1]])
    specs = {
        "(a) T-bill": rf[1:, None],
        "(b) markt": rm[1:, None],
        "(c) markt + T-bill": np.column_stack([rm, rf])[1:],
    }
    rows = {name: gmm_euler(gc[1:], R, Z) for name, R in specs.items()}
    return pd.DataFrame(rows).T[["gamma", "se_gamma", "beta", "se_beta", "J", "df", "p"]]


tables = {
    "1947-2019": estimate_table(main),
    "1959-1978": estimate_table(quarterly.loc["1959Q2":"1978Q4"]),
}
gmm_results = pd.concat(tables, names=["steekproef", "activa"]).astype(float)
gmm_results.columns = ["gamma", "SE(gamma)", "beta", "SE(beta)", "J", "vrijheidsgraden", "p-waarde"]
gmm_results.round(4)
```

Het patroon is in beide steekproeven hetzelfde. Met alleen de T-bill is
$\hat\gamma$ klein en nauwkeurig geschat, en de toets verwerpt. Met alleen aandelen is de standaardfout groter dan de schatting, en de
toets verwerpt niet. Met beide samen verwerpt de toets, met $p$-waarden die op
vier decimalen nul zijn. Over 1947–2019 gebeurt dat met $\hat\gamma = 17$ en
$\hat\beta = 1{,}08$: de schatter verklaart de premie met hoge risicoaversie en
zet $\beta$ boven één om de lage rente te halen. Uit de simulatie weten we dat
zo'n $\hat\beta$ ook bij een waar model vaak voorkomt. De verwerping door $J_T$
weegt zwaarder.

### Wat het aandelenrendement alleen vraagt

Welke $\gamma$ is nodig om alleen de gemiddelde premie te verklaren? Volgens
[](#eq-consumptie-capm-excess) moet het met $g^{-\gamma}$ gewogen excess rendement
nul zijn. Bij $\gamma = 0$ is het gewoon de premie. Naarmate $\gamma$ stijgt, wegen kwartalen met lage
consumptiegroei zwaarder. Renderen aandelen in die kwartalen slecht, dan daalt
de gewogen premie. De cel zoekt de $\gamma$ waarbij ze nul wordt, in beide
steekproeven.

```{code-cell} ipython3
gamma_line = np.linspace(0, 300, 601)
samples = {"1947K2–2019K4": main, "1959K2–1978K4": quarterly.loc["1959Q2":"1978Q4"]}
weighted_premium, roots = {}, {}
for label, frame in samples.items():
    gc, excess = frame.gc.to_numpy(), (frame.Rm - frame.Rf).to_numpy()
    weighted_premium[label] = np.array([np.mean(gc ** (-x) * excess) for x in gamma_line]) * 100
    crossing = np.flatnonzero(np.diff(np.sign(weighted_premium[label])))
    if crossing.size:
        lo, hi = gamma_line[crossing[0]], gamma_line[crossing[0] + 1]
        roots[label] = optimize.brentq(lambda x: np.mean(gc ** (-x) * excess), lo, hi)
    else:
        roots[label] = np.nan

pd.Series(roots, name="gamma waarbij de gewogen premie nul is").round(1)
```

In 1959–1978 is $\gamma \approx 75$ nodig. In 1947–2019 bestaat er geen $\gamma$
tussen 0 en 300 die het doet. Let in de figuur op waar de lijnen de horizontale as snijden.

```{code-cell} ipython3
:label: cel-consumptie-capm-excess
:tags: [hide-input]

fig, ax = plt.subplots()
for label, curve in weighted_premium.items():
    ax.plot(gamma_line, curve, label=label)
ax.axhline(0, color="black", lw=0.8)
ax.set_xlabel("Risicoaversie $\\gamma$")
ax.set_ylabel("$E[g^{-\\gamma} R^e]$, procent per kwartaal")
ax.set_title("De gewogen aandelenpremie als functie van $\\gamma$")
ax.legend()
plt.show()
```

:::{figure} #cel-consumptie-capm-excess
:label: fig-consumptie-capm-excess
:width: 90%

De steekproefversie van [](#eq-consumptie-capm-excess). Boven nul leveren
aandelen meer op dan het risico dat ze volgens het model dragen. In 1959–1978
snijdt de lijn de as pas bij een risicoaversie in de tientallen. In 1947–2019
snijdt ze de as nergens: bij hoge $\gamma$ nemen een paar kwartalen met dalende
consumptie en stijgende koersen het gewicht over.
:::

Beide lijnen dalen eerst, zoals het consumptie-CAPM voorspelt, maar veel te
langzaam.

### Vergelijking met 1983

We zetten hun schattingen met niet-duurzame goederen plus diensten naast onze
steekproef 1959–1978. Ze komen uit tabel 4 (p. 261, NLAG = 2), tabel 1 (p. 259,
model 6, NLAG = 6) en tabel 5 (p. 262, NLAG = 4 en 0) van
{cite:t}`HansenSingleton1983`. Voor (c) nemen we alleen de toets over, geen
$\hat\gamma$; die cel blijft leeg.
Hun $\hat\alpha$ is omgerekend naar onze $\gamma = -\alpha$. In rij (d) is "hier" het
nulpunt uit de figuur, zonder standaardfout.

```{code-cell} ipython3
hs_1959 = gmm_results.loc["1959-1978"]
pd.DataFrame(
    {
        "gamma origineel": [0.931, 1.509, np.nan, 58.25],
        "SE origineel": [0.044, 1.571, np.nan, 66.57],
        "verwerpt origineel": ["ja (chi2(3) = 30.08)", "nee (chi2(11) = 10.93)", "ja (chi2(24) = 366.22)", "exact"],
        "gamma hier": [*hs_1959["gamma"], roots["1959K2–1978K4"]],
        "SE hier": [*hs_1959["SE(gamma)"], np.nan],
        "p-waarde hier": [*hs_1959["p-waarde"], np.nan],
    },
    index=["(a) T-bill", "(b) markt", "(c) markt + T-bill", "(d) alleen de premie"],
).round(4)
```

Geslaagd: de verwachte afwijking komt uit in alle drie de gevallen. De T-bill
geeft een kleine $\hat\gamma$ en verwerping. Onze standaardfout is groter dan de
hunne: kwartaaldata met één vertraging bevatten minder informatie dan maanddata
met twee. Aandelen alleen geven geen verwerping. Het teken van $\hat\gamma$
verschilt daar, maar de kolommen met standaardfouten laten zien dat geen van
beide schattingen van nul te onderscheiden is. Samen verwerpt de toets.

De premie alleen vraagt in beide studies een $\gamma$ in de tientallen (rij (d)),
met bij Hansen en Singleton een standaardfout die groter is dan de schatting. Dat
is de standaardfout van 2% in zijn scherpste vorm: de premie is slecht gemeten,
dus de risicoaversie die haar moet verklaren nog slechter. Het interval sluit
niets uit. Wat overblijft, is een puntschatting die onaannemelijk groot is. In de
simulatie verwierp de toets een waar model in één op de tien steekproeven. Hier
is de $p$-waarde op vier decimalen nul.

```{warning}
Consumptie is een kwartaalgemiddelde, rendementen lopen van punt tot punt. Die
tijdsaggregatie maakt de Euler-fout autocorrelerend, zodat onze standaardfouten
te klein en onze $J$-statistieken te groot zijn. Maanddata, zoals bij Hansen
en Singleton, verkleinen dat probleem. De aggregatie verklaart niet waarom de premie een $\gamma$ in
de tientallen vraagt.
```

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Het consumptie-CAPM gaf de discontovoet voor het
eerst een theorie. Het verklaart waarom de rente hoog is als groei wordt
verwacht, waarom een verzekering een negatief verwacht excess rendement heeft, en
waarom de prijs-dividend-ratio kan bewegen zonder dat dividenden bewegen. Het
bracht de logica van het CAPM en Mertons hedgemotieven samen in één bèta. De
Euler-vergelijking [](#eq-consumptie-capm-euler) komt terug in elk later model,
en GMM is nog altijd de standaard voor elk model dat als momentvoorwaarde te
schrijven is.

**Waar het breekt.** Eén paar $(\beta, \gamma)$ kan de rente en het
aandelenrendement niet tegelijk prijzen. Met aandelen en T-bill samen verwerpt de
toets met $p$-waarden die op vier decimalen nul zijn. De premie alleen vraagt een
$\gamma$ van 75, of is over 1947–2019 met geen $\gamma$ onder 300 te verklaren. De
simulatie laat zien dat dit geen artefact van een kleine steekproef is: als het
model waar is, zijn de schattingen onnauwkeurig, maar is een verwerping zeldzaam
en zwak. In de vraag theorie of feit is het consumptie-CAPM dus een theorie die
met één toets werd verworpen.

**Risico of vergissing?** Is de premie een beloning voor risico dat het model
slecht meet? Of betalen beleggers een prijs die niets met consumptie te maken
heeft? De Chicago-lezing ziet prijzen als rationele beloning voor
risico. Volgens haar is de theorie juist, maar de specificatie te arm. Consumptie is slecht gemeten, de meeste huishoudens
hadden geen aandelen, en CRRA-nut koppelt risicoaversie aan de bereidheid om
consumptie te verschuiven. Met gewoontes of zeldzame rampen kan de SDF wel sterk
genoeg bewegen.

De Yale-lezing ziet in prijzen ook vergissingen. Prijzen worden gezet door
beleggers met beperkte aandacht en wisselende stemmingen, en de premie is een vergoeding voor angst. De
data die de kampen zouden scheiden, consumptie van aandeelhouders over een eeuw,
bestaan niet.

**Wat er daarna kwam.** Het vak hield daarna $p = \E[mx]$ vast
en zocht een andere $m$. Mehra en Prescott maakten van de breuk een kwantitatieve
puzzel, en Hansen en Jagannathan een grens die voor elke SDF geldt; zie
[](#03-13-equity-premium-puzzle).

## Oefeningen

:::{exercise}
:label: ex-consumptie-capm-1

**Persistentie, risicoaversie en de richting van de prijs-dividend-ratio.** Neem
het toy-voorbeeld ($g_h = 1{,}04$, $g_l = 0{,}96$, $\beta = 0{,}96$) met
overgangskans $\pi = P_{hh} = P_{ll}$.

1. Laat zien dat bij $\gamma = 1$ de prijs-dividend-ratio in beide toestanden
   $\beta/(1-\beta)$ is, voor elke $\pi$.

2. Bereken $\mathrm{PD}_h - \mathrm{PD}_l$ voor $\gamma \in \{0{,}5;\ 1;\ 2;\ 3\}$
   en $\pi \in \{0{,}5;\ 0{,}75;\ 0{,}9\}$. Wanneer is de ratio hoger in de hoge
   toestand?
:::

:::{solution} ex-consumptie-capm-1
:class: dropdown

**(1)** Bij $\gamma = 1$ is $g_j^{1-\gamma} = 1$, dus
$\mathrm{PD}_i = \beta \sum_j P_{ij}(1 + \mathrm{PD}_j)$. Een constante
$\mathrm{PD} = \beta(1 + \mathrm{PD})$ lost dit op, dus $\mathrm{PD} = \beta/(1-\beta) = 24$.
Uniciteit volgt uit [](#thm-consumptie-capm-contractie) met $\delta = \beta$.

**(2)** De cel lost het stelsel van stap 2 op voor elke combinatie.

```{code-cell} ipython3
def toy_pd_gap(gamma, pi, beta=0.96, g=np.array([1.04, 0.96])):
    """PD_h - PD_l in the two-state Lucas tree with symmetric persistence pi."""
    trans = np.array([[pi, 1 - pi], [1 - pi, pi]])
    kernel = beta * trans * g ** (1 - gamma)
    pd_states = np.linalg.solve(np.eye(2) - kernel, kernel @ np.ones(2))
    return pd_states[0] - pd_states[1]


gaps = pd.DataFrame(
    {pi: [toy_pd_gap(gm, pi) for gm in (0.5, 1.0, 2.0, 3.0)] for pi in (0.5, 0.75, 0.9)},
    index=pd.Index([0.5, 1.0, 2.0, 3.0], name="gamma"),
)
gaps.columns.name = "pi"
gaps.round(4)
```

De ratio is hoger in de hoge toestand als $\gamma < 1$ en $\pi > 1/2$: dan wint
het groei-effect. Bij $\gamma > 1$ wint het rente-effect, en het verschil groeit
met de persistentie. Bij $\pi = 1/2$ is de groei onvoorspelbaar en is het
verschil nul. Wat dit leert: in een Lucas-boom zegt de richting waarin prijzen op
goed nieuws reageren iets over $\gamma$. Een ratio die met de groei meestijgt,
vraagt $\gamma < 1$ of een ander model.
:::

:::{exercise}
:label: ex-consumptie-capm-2

**Het consumptie-CAPM voor logrendementen.** Gebruik de simulatie-economie
($\beta = 0{,}98$, $\gamma = 4$, $\mu = 1{,}8\%$, $\sigma = 3{,}5\%$, $\phi = 3$,
$\sigma_d = 10\%$), en schrijf $\ell^m = \log R^m$.

1. Leid uit [](#eq-consumptie-capm-lognormaal) af dat de consumptiebèta van
   $\ell^m$ gelijk is aan $\phi$, en dat
   $\E[\ell^m] - \log(1+R^f) + \tfrac12\Var(\ell^m) = \gamma\,\Cov(\ell^m, \Delta c)$.

2. Controleer beide kanten op de miljoen gesimuleerde jaren.
3. Hoeveel jaar data is nodig om de premie met een $t$-waarde van twee van nul te
   onderscheiden?
:::

:::{solution} ex-consumptie-capm-2
:class: dropdown

**(1)** De ratio is constant, dus $\ell^m = \log\frac{1+\mathrm{PD}}{\mathrm{PD}} + \log g^d$.
Dan is $\Cov(\ell^m, \Delta c) = \phi\sigma^2$ en de bèta $\phi = 3$. Voor een
lognormale $R^m$ is $\log \E[R^m] = \E[\ell^m] + \tfrac12\Var(\ell^m)$. Invullen in
[](#eq-consumptie-capm-lognormaal) geeft de gevraagde vorm, met rechterlid
$\gamma\phi\sigma^2 = 0{,}0147$.

**(2) en (3)** De cel rekent beide kanten uit, en het aantal jaren
$T = (2\sigma_{R^e}/\E[R^e])^2$ waarbij de $t$-waarde twee is.

```{code-cell} ipython3
log_rm, log_gc = np.log(rm_big), np.log(gc_big)
lhs = log_rm.mean() - np.log(rf_gross) + 0.5 * log_rm.var()
rhs = tree["gamma"] * np.cov(log_rm, log_gc)[0, 1]
beta_c = np.cov(log_rm, log_gc)[0, 1] / log_gc.var()

excess = rm_big - rf_big
years_needed = (2 * excess.std() / excess.mean()) ** 2

pd.Series(
    {
        "consumptiebèta van log R^m (theorie 3)": beta_c,
        "linkerlid": lhs,
        "rechterlid": rhs,
        "rechterlid, theorie": tree["gamma"] * tree["leverage"] * tree["sigma"] ** 2,
        "gemiddeld excess rendement": excess.mean(),
        "SD excess rendement": excess.std(),
        "jaren nodig voor t = 2": years_needed,
    }
).round(5)
```

De bèta is 3. Het linkerlid ($0{,}0145$) en het rechterlid ($0{,}0147$) verschillen
$0{,}0002$. Dat is ruim één standaardfout van een gemiddelde over een miljoen
jaar, want $0{,}16/\sqrt{10^6} = 0{,}00016$. Met een excess volatiliteit van 16% en
een gemiddeld excess rendement van 1,6% is voor $t = 2$ ongeveer vierhonderd jaar
nodig. Wat dit leert: de consumptiebèta is scherp te meten en de premie niet,
dus $\hat\gamma$ erft de onnauwkeurigheid van de premie.
:::

:::{exercise}
:label: ex-consumptie-capm-3

**De replicatie op jaardata en met de coronakwartalen.** Herhaal specificatie (c)
(markt en T-bill, instrumenten: constante en één vertraging van alle drie de
variabelen)

1. op kwartaaldata tot en met de laatste beschikbare waarneming, dus inclusief
   2020 en later;

2. op jaardata 1948–2019, met consumptie als jaargemiddelde van de kwartaalreeks
   en rendementen samengesteld over het kalenderjaar.

Rapporteer $\hat\gamma$, $\hat\beta$, $J_T$ en de $p$-waarde. Verandert de
conclusie?
:::

:::{solution} ex-consumptie-capm-3
:class: dropdown

De cel bouwt de jaarreeks op dezelfde manier als de kwartaalreeks en schat (c)
op de drie varianten.

```{code-cell} ipython3
annual_cons = cons.loc[:"2019Q4", ["c", "deflator"]].groupby(lambda q: q.year).mean()
market_a = (1 + market[["Mkt", "RF"]]).groupby(market.index.year).prod()
annual = annual_cons.join(market_a, how="inner")
infl_a = annual.deflator / annual.deflator.shift(1)
annual["gc"] = annual.c / annual.c.shift(1)
annual["Rm"] = annual.Mkt / infl_a
annual["Rf"] = annual.RF / infl_a
annual = annual[["gc", "Rm", "Rf"]].dropna()

variants = {
    "kwartaal 1947-2019": main,
    "kwartaal incl. 2020-": quarterly,
    "jaar 1948-2019": annual,
}
rows_ex3 = {}
for name, frame in variants.items():
    table = estimate_table(frame)
    rows_ex3[name] = table.loc["(c) markt + T-bill"]
pd.DataFrame(rows_ex3).T.astype(float).round(4)
```

De puntschatting van $\gamma$ springt van ongeveer 17 naar ongeveer 2 met de
coronakwartalen erbij, en wordt negatief op jaardata. In die kwartalen daalde en
herstelde consumptie scherp, en via $g^{-\gamma}$ krijgen ze veel gewicht. De
verwerping blijft in alle drie de varianten, met een $p$-waarde die op vier
decimalen nul is. Wat dit leert: $\hat\gamma$ is niet robuust tegen frequentie,
steekproef of een paar uitschieters, de verwerping wel. De breuk zit in de
restricties zelf, niet in een detail van de meting.
:::
