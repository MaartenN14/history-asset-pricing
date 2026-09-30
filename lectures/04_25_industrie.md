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

(04-25-industrie)=

# De industrie als financier: indexfondsen, DFA, AQR

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1968–2019, van Jensens fondsstudie tot het jaar waarin
Amerikaanse indexfondsen evenveel van de beurs bezaten als actieve fondsen.

**Wat we al weten.** In [](#02-06-efficiente-markten) presteerden
beleggingsfondsen gemiddeld slechter dan de markt, en zelfs zeven bekende fondsen
die de hele periode overleefden, haalden geen significante alpha. De factormodellen
van Fama, French en Carhart leverden daarna de meetlatten waarmee alpha sindsdien
wordt gemeten. In [](#04-24-microstructuur) zagen we bovendien dat handelen geld
kost zodra er aan de andere kant iemand staat die meer weet.

**Welke vraag staat open.** Als actief beheer gemiddeld verliest, komt dat
doordat niemand vaardig is, of doordat vaardigheid in evenwicht niet bij de
belegger aankomt?
```

## Overzicht

Verliest actief beheer omdat niemand vaardig is? Nee, want dat de gemiddelde actieve
dollar na kosten achterblijft, volgt al uit een optelsom. De vaardigheid die wel bestaat,
komt in evenwicht bij de beheerder terecht en niet bij de belegger. Een deel van dat
antwoord is bewezen en een deel gemeten, want de rekenkunde is een stelling, en dat
factoren en kosten de persistentie van fondsrendementen verklaren, is een waarneming van
Carhart. Of er daarnaast een restje vaardigheid overblijft, is een open vraag, want de
data laten meer dan één verklaring toe. In dit college

- laten we met drie beleggers en twee aandelen zien dat de actieve beleggers samen
  vóór kosten precies de markt halen;
- bewijzen we die rekenkunde van Sharpe en leiden we het evenwicht van Berk en
  Green af, waarin een vaardige beheerder groeit tot de belegger niets extra's meer
  overhoudt;
- bespreken we hoe de standaardfout van alpha, de bootstrap van Fama en French en
  de false discovery rate vaardigheid van geluk proberen te scheiden;
- simuleren we 2000 fondsen waarvan we de waarheid kennen, om te zien hoeveel
  vaardige fondsen die methoden terugvinden;
- repliceren we op 50 Amerikaanse fondsen de gemiddelde alpha, de bootstrap van
  Fama en French en de persistentie van Carhart.

Jensen vond in 1968 dat beleggingsfondsen na kosten gemiddeld 1,1% per jaar
achterbleven bij de markt {cite}`Jensen1968`. Sharpe liet in 1991 in drie
pagina's zien waarom dat vóór kosten niet anders kan {cite}`Sharpe1991`.
Intussen bouwden dezelfde academische kringen de bijbehorende industrie.
Wells Fargo begon in 1971 het eerste indexfonds voor institutionele beleggers en Vanguard
in 1976 het eerste voor particulieren. Oud-studenten van Fama richtten Dimensional Fund
Advisors (1981) en AQR (1998) op, die de factorpremies uit
[](#04-18-fama-french) en [](#04-19-momentum) als product verkochten. Santa-Clara noemt
het de eigenaardige sociologie van het vak dat juist de onderzoekers die aantoonden dat
actief beheer faalt, zelf actieve beheerders oprichtten {cite}`SantaClara2026`. Toch hadden
ze in beide rollen gelijk. Berk en
Green gaven {cite}`BerkGreen2004` die schijnbare tegenspraak
een model, en Fama en French {cite}`FamaFrench2010` en Barras, Scaillet en Wermers
{cite}`BarrasScailletWermers2010` leverden de statistiek waarmee het college eindigt.

## Intuïtie: waarom zou dit waar zijn?

Elk aandeel is van iemand. Tellen we de portefeuilles van alle beleggers op, dan
komt er precies de markt uit. Splitsen we de beleggers in twee groepen, zij die de
markt kopen en niets doen en zij die iets anders doen, dan haalt de eerste groep
het marktrendement. De tweede groep bezit samen dus de rest van de markt, en
omdat die rest dezelfde samenstelling heeft, haalt ook die groep samen het
marktrendement. Voor elke actieve belegger die de markt verslaat, blijft er dus
een andere actieve belegger evenveel achter. Trekken we daarna de kosten af, die
bij actief beheer hoger zijn, dan verliest de gemiddelde actieve dollar, zonder
dat er een model van risico aan te pas komt. Beleggers namen die rekenkunde pas laat ter
harte, want pas eind 2019 hielden indexfondsen en index-ETF's (beursgenoteerde
indexfondsen) samen 15% van de Amerikaanse beurswaarde, evenveel als actief beheerde
aandelenfondsen {cite}`ICI2020`.

Dat oud-studenten van Fama toch actieve bedrijven oprichtten, is om drie redenen geen
tegenspraak.

- De rekenkunde gaat over *alle* actieve dollars, zodat fondsen samen kunnen winnen
  van particulieren, die volgens Santa-Clara te veel handelen en de verkeerde
  aandelen houden {cite}`SantaClara2026,BarberOdean2000`.
- DFA en AQR verkochten vooral goedkope blootstelling aan premies, en voor de
  rekenkunde maakt het niet uit of zo'n premie een vergoeding voor risico is of
  een vergissing van anderen.
- Vaardigheid kan bestaan zonder dat beleggers er iets van merken.

Het derde punt vraagt om uitleg. Een goede beheerder trekt geld aan, en een groter
fonds plaatst grotere orders, die de prijs tegen het fonds in bewegen zoals de
Kyle-$\lambda$ uit [](#04-24-microstructuur) voorspelt. Het geld blijft stromen tot
het rendement voor de belegger niet meer bijzonder is, zodat de beheerder de
vergoeding krijgt en de belegger het marktrendement. We verwachten dus dat goede jaren een
fonds groter maken zonder dat het daarna beter rendeert. Vaardigheid wordt dan eerder
zichtbaar in de omvang van fondsen dan in hun rendementen. Bovendien is de standaardfout
van een alpha na twintig jaar nog ruim één procentpunt per jaar, zodat ook duizenden
fondsen zonder vaardigheid een staart van sterren opleveren. De vraag is dan niet of één
fonds goed is, maar of er meer goede fondsen zijn dan toeval oplevert.

## Toy-voorbeeld: drie beleggers en twee aandelen

We laden eerst de pakketten die in het hele college nodig zijn.

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

De markt bestaat uit twee aandelen, A met marktwaarde 60 en B met marktwaarde 40.
Over het jaar rendeert A $+10\%$ en B $-5\%$. Drie beleggers bezitten samen alles,
en de passieve belegger P betaalt minder kosten dan de actieve beleggers X en Y.

| Belegger | in A | in B | vermogen | kosten |
|---|---|---|---|---|
| passief P | 30 | 20 | 50 | $0{,}1\%$ |
| actief X | 25 | 5 | 30 | $1{,}0\%$ |
| actief Y | 5 | 15 | 20 | $1{,}0\%$ |
| **markt** | 60 | 40 | 100 | |

1. De markt rendeert $0{,}6 \times 10 + 0{,}4 \times (-5) = 4\%$, en P haalt dat ook,
   omdat hij A en B in de verhouding 60:40 houdt.
2. X zette zwaar in op A en haalt $(25 \times 10 - 5 \times 5)/30 = 7{,}5\%$.
3. Y zat vooral in B en haalt $(5 \times 10 - 15 \times 5)/20 = -1{,}25\%$.
4. X en Y bezitten samen $30$ in A en $20$ in B, weer 60:40, en halen samen
   $(30 \times 7{,}5 + 20 \times (-1{,}25))/50 = 4\%$.
5. Na $1\%$ kosten houden X en Y samen $3{,}0\%$ over, $0{,}9$ procentpunt minder
   dan P met zijn $3{,}9\%$.

De code rekent dezelfde stappen na en zet ze naast de handberekening.

```{code-cell} ipython3
holdings = pd.DataFrame(
    {"A": [30.0, 25.0, 5.0], "B": [20.0, 5.0, 15.0]},
    index=["passief P", "actief X", "actief Y"],
)
stock_ret = pd.Series({"A": 0.10, "B": -0.05})
costs = pd.Series({"passief P": 0.001, "actief X": 0.010, "actief Y": 0.010})

wealth = holdings.sum(axis=1)
gross = holdings @ stock_ret / wealth
net = gross - costs
market = holdings.sum() @ stock_ret / wealth.sum()

active = ["actief X", "actief Y"]
active_gross = wealth[active] @ gross[active] / wealth[active].sum()
active_net = wealth[active] @ net[active] / wealth[active].sum()
cost_gap = net["passief P"] - active_net
assert np.isclose(active_gross, market) and np.isclose(active_net, 0.03)

pd.DataFrame({
    "met de hand (%)": [4.0, 7.5, -1.25, 4.0, 3.0, 0.9],
    "code (%)": 100 * np.array([market, gross["actief X"], gross["actief Y"],
                                active_gross, active_net, cost_gap]),
}, index=["marktrendement", "bruto X", "bruto Y", "X en Y samen, bruto",
          "X en Y samen, netto", "P netto min X en Y netto"]).round(4)
```

Hand en code komen op alle zes regels overeen. X versloeg de markt wel, maar Y
betaalde daar precies voor, en na kosten verliezen de actieve beleggers samen
0,9 procentpunt op de passieve belegger.

## Theorie

De theorie beantwoordt de vraag uit het Overzicht in drie stappen. Eerst laten we
zien dat de gemiddelde actieve dollar vóór kosten precies de markt haalt en na
hogere kosten dus achterblijft, als identiteit en zonder model. Daarna volgt het model van
Berk en Green, waarin
vaardigheid bestaat maar de belegger in evenwicht niets extra's oplevert. Dat model
verschuift de vraag van "bestaat vaardigheid?" naar "hoe meten we die in duizenden
fondsen?". Daarom eindigen we met drie meetinstrumenten: de standaardfout
van alpha, de bootstrap en de false discovery rate.

### Sharpes rekenkunde

Het gemiddelde rendement van de actieve beleggers is vóór kosten gelijk aan het
marktrendement, in elke periode. Er zijn $N$ effecten met marktwaarden
$M_{1,t}, \dots, M_{N,t}$ en rendementen $R_{i,t+1}$ tussen $t$ en $t+1$, zodat het
marktrendement $R_{m,t+1} = \sum_i M_{i,t} R_{i,t+1} / \sum_i M_{i,t}$ is; het
subscript $m$ staat hier voor de markt. Belegger $j$ houdt op $t$ voor
$h_{i,t}^{j} \geq 0$ dollar in effect $i$, met vermogen $W^{j}_t = \sum_i h_{i,t}^{j}$
en bruto rendement $R^{j}_{t+1} = \sum_i h^{j}_{i,t} R_{i,t+1} / W^{j}_t$.

Sharpe noemt een belegger passief als hij van elk effect hetzelfde deel bezit, dus
$h_{i,t}^{j} = \theta_j M_{i,t}$ voor alle $i$ met een vaste $\theta_j > 0$
{cite}`Sharpe1991`. Elke andere belegger is actief, en de verzamelingen passieve en actieve
beleggers heten $\mathcal{P}$ en $\mathcal{A}$. De kosten $c_j$ zijn een fractie van het
vermogen, bijvoorbeeld $0{,}1\%$ voor P en $1\%$ voor X en Y.

:::{prf:proposition} De rekenkunde van actief beheer
:label: thm-industrie-sharpe

Stel dat alle effecten door iemand worden gehouden, $\sum_j h^{j}_{i,t} = M_{i,t}$ voor elke $i$, en dat $\mathcal{A}$ niet leeg is. Dan geldt voor het vermogensgewogen
gemiddelde rendement van de actieve beleggers

```{math}
:label: eq-industrie-sharpe
\frac{\sum_{j\in\mathcal{A}} W^{j}_t R^{j}_{t+1}}{\sum_{j\in\mathcal{A}} W^{j}_t}
= R_{m,t+1}
\qquad\text{en}\qquad
\frac{\sum_{j\in\mathcal{A}} W^{j}_t \left(R^{j}_{t+1} - c_j\right)}{\sum_{j\in\mathcal{A}} W^{j}_t}
= R_{m,t+1} - \bar c_{\mathcal{A}},
```

met $\bar c_{\mathcal{A}}$ de vermogensgewogen gemiddelde kosten van de actieve
beleggers.
:::

Het bewijs telt de posities op. De passieve beleggers bezitten samen een vast deel $\Theta = \sum_{j\in\mathcal{P}}\theta_j$
van elk effect. De actieve beleggers bezitten dus samen het deel $1 - \Theta$ van elk
effect, en een evenredig stuk van de
markt heeft het rendement van de markt. In het toy-voorbeeld is $\Theta = 0{,}5$,
want P bezit de helft van A en de helft van B, en dus bezitten X en Y samen ook
van elk aandeel de helft.

:::{prf:proof}
:class: dropdown

Tel de posities van de actieve beleggers in effect $i$ op en gebruik dat alles
gehouden wordt:
$\sum_{j\in\mathcal{A}} h^{j}_{i,t} = M_{i,t} - \sum_{j\in\mathcal{P}} \theta_j M_{i,t}
= (1-\Theta)\, M_{i,t}$, met $\Theta < 1$ omdat $\mathcal{A}$ iets bezit. Het
gezamenlijke vermogen van de actieve beleggers is dan
$(1-\Theta)\sum_i M_{i,t}$, en hun gezamenlijke opbrengst in dollars is

$$
\sum_{j\in\mathcal{A}} W^{j}_t R^{j}_{t+1}
= \sum_i \Big(\sum_{j\in\mathcal{A}} h^{j}_{i,t}\Big) R_{i,t+1}
= (1-\Theta) \sum_i M_{i,t} R_{i,t+1}.
$$

Delen door het gezamenlijke vermogen geeft de eerste gelijkheid. Omdat de kosten
per belegger een vaste aftrek zijn, is het gewogen gemiddelde na kosten
$R_{m,t+1} - \bar c_{\mathcal{A}}$. Een passieve belegger haalt
$R_{m,t+1} - c_j$. $\square$
:::

De eerste gelijkheid in [](#eq-industrie-sharpe) zegt dat de actieve beleggers samen
vóór kosten precies de markt halen, de tweede dat ze na kosten achterblijven zodra hun
kosten gemiddeld hoger zijn dan die van passieve beleggers. Het bewijs
gebruikt geen verwachtingen, zodat de uitspraak in élke periode geldt. Ze gaat
wel over *alle* actieve dollars, en een echte indexbelegger moet bij
indexwijzigingen en emissies handelen. Onder kosten vallen bovendien alle kosten,
van vergoedingen en spreads tot de prijsimpact uit [](#04-24-microstructuur). French telde
ze op voor de Amerikaanse beurs {cite}`French2008` en kwam over 1980–2006
uit op 0,67% van de marktwaarde per jaar. Omdat de bruto alpha's samen nul zijn,
is dat volgens hem ook wat de gemiddelde belegger per jaar had kunnen winnen door
passief te beleggen.

### Het model van Berk en Green

Vaardigheid en een nettoalpha van nul gaan samen zodra kapitaal vrij naar een
fonds kan stromen en een groter fonds per dollar meer handelskosten maakt. Biedt een fonds
na kosten meer verwacht rendement dan de index, dan verplaatsen beleggers hun geld
ernaartoe. Die instroom stopt pas wanneer het fonds zo groot is dat het extra
rendement op is. In evenwicht voorspelt het verleden daarom niets over het
rendement van de belegger, maar veel over de omvang van het fonds.

We volgen {cite:t}`BerkGreen2004`, maar noemen hun vaardigheid $a$ om verwarring
met de geschatte Jensen-alpha te voorkomen. De beheerder haalt op actief beheerd
geld een risicogecorrigeerd overrendement vóór kosten $R_{t+1} = a + e_{t+1}$, met
onafhankelijke ruis $e_{t+1} \sim N(0, \sigma^2)$ en $\sigma$ in de orde van $5\%$
per jaar. Niemand kent $a$, ook de beheerder niet. De markt begint met de *prior*
(de verdeling vóór de eerste waarneming) $a \sim N(\phi_0, \eta^2)$ en schrijft
$\gamma = 1/\eta^2$ en $\omega = 1/\sigma^2$ voor de precisies. Met de regel van Bayes
is de verwachte vaardigheid na $t$ jaar

$$
\phi_t = \E[a \mid R_1,\dots,R_t] = \frac{\gamma \phi_0 + \omega \sum_{s=1}^{t} R_s}{\gamma + t\,\omega},
$$

een gewogen gemiddelde van de prior en de waarnemingen, zodat elk goed jaar
$\phi_t$ verhoogt.

De beheerder belegt $q_{a,t}$ actief en $q_{I,t}$ in de index, samen
$q_t = q_{a,t} + q_{I,t}$. Het actieve deel kost $C(q_{a,t})$, met $C(0) = 0$ en
stijgende marginale kosten ($C' > 0$, $C'' > 0$) die op den duur elk denkbaar rendement
overtreffen ($\lim_{q\to\infty} C'(q) > 1$), zodat het fonds eindig groot blijft, en
hij rekent een vergoeding $f$ per beheerde dollar. Het rendement voor de belegger
boven de index is dan

```{math}
:label: eq-industrie-bg-rendement
r_{t+1} = \frac{q_{a,t}}{q_t} R_{t+1} - \frac{C(q_{a,t}) + f q_t}{q_t}.
```

Het eerste deel is de vaardigheid, verdund over het hele fonds, en het tweede deel
zijn de handelskosten en de vergoeding per dollar. Beleggers leveren kapitaal
zolang $\E_t[r_{t+1}] \geq 0$, en de beheerder maximaliseert zijn vergoeding
$f q_t$ onder die voorwaarde.

:::{prf:theorem} Vaardigheid zonder persistentie (Berk en Green 2004)
:label: thm-industrie-berk-green

In evenwicht is $\E_t[r_{t+1}] = 0$ voor elke historie, zodat
$\Cov(r_{t+1}, g(R_1,\dots,R_t)) = 0$ voor elke functie $g$, ook als $\Var(a) > 0$.
Zolang het fonds een indexdeel heeft ($q_{I,t} > 0$), beheert de beheerder actief tot
$C'(q_{a,t}) = \phi_t$. De omvang $q_t$ stijgt strikt in elk verleden rendement $R_s$.
:::

:::{prf:proof}
:class: dropdown

*Stap 1: de voorwaarde van de belegger is bindend.* De verwachting van
[](#eq-industrie-bg-rendement) is $(\phi_t q_{a,t} - C(q_{a,t}) - f q_t)/q_t$. De
doelfunctie $f q_t$ stijgt in $q_t$ en de voorwaarde
$\phi_t q_{a,t} - C(q_{a,t}) - f q_t \geq 0$ daalt erin, dus in het optimum geldt
gelijkheid.

*Stap 2: marginale kosten gelijk aan verwachte alpha.* De beheerder kiest $q_a$ en $q$,
met de Lagrangiaan

$$
\mathcal{L} = f q + \lambda^p\big(\phi_t q_a - C(q_a) - f q\big) + \lambda^f (q - q_a),
$$

waarin $\lambda^p$ de schaduwprijs van de participatievoorwaarde is en $\lambda^f$ die van
$q_I = q - q_a \geq 0$. De eerste-ordevoorwaarde voor $q_a$ is
$\lambda^p(\phi_t - C'(q_a)) = \lambda^f$, en die voor $q$ is $f(1 - \lambda^p) + \lambda^f = 0$.
Heeft het fonds een indexdeel, dan bindt $q_I \geq 0$ niet en is $\lambda^f = 0$
(complementariteit), zodat $\lambda^p = 1 > 0$ en $C'(q_{a,t}) = \phi_t$. Invullen in de
bindende voorwaarde geeft $q_t = (\phi_t q_{a,t} - C(q_{a,t}))/f$, en de oplossing is
inwendig zolang $q_{I,t} = q_t - q_{a,t} > 0$. Anders is $q_{I,t} = 0$ en $\lambda^f > 0$,
zodat $C'(q_{a,t}) < \phi_t$ en $q_t$ de vergelijking $\phi_t = (C(q_t) + f q_t)/q_t$ oplost.

*Stap 3: het rendement is niet te voorspellen.* De bindende voorwaarde is precies
$\E_t[r_{t+1}] = 0$. Dan is $\E[r_{t+1} g] = \E[g\,\E_t[r_{t+1}]] = 0$ en
$\E[r_{t+1}] = 0$, dus de covariantie is nul.

*Stap 4: de omvang stijgt met elk goed jaar.* In het inwendige geval geeft de
omhullende-stelling $dq_t/d\phi_t = q_{a,t}/f > 0$. In het randgeval is
$\phi_t = C(q_t)/q_t + f$, en $C(q)/q$ stijgt strikt omdat $C$ strikt convex is met
$C(0) = 0$. Ten slotte is $\partial\phi_t/\partial R_s = \omega/(\gamma + t\omega) > 0$.
$\square$
:::

Met getallen wordt het evenwicht tastbaar. Neem een verwachte vaardigheid van
$\phi = 3\%$ per jaar, kwadratische handelskosten $C(q_a) = b\, q_a^2$ met
$b = 0{,}005$ per miljard dollar, zodat de kosten per actieve dollar $b\,q_a$ zijn,
en een vergoeding $f = 1\%$.

- Mag de beheerder geen index bijmengen, dan stroomt er geld toe tot
  $\phi - b\,q - f = 0$, dus tot $q = (0{,}03 - 0{,}01)/0{,}005 = 4$ miljard, en
  verdient hij 40 miljoen per jaar.
- Mag hij het surplus in de index beleggen, dan beheert hij actief tot
  $2b\,q_a = \phi$, dus $q_a = 3$ miljard, en brengen beleggers geld tot
  $\phi\,q_a - b\,q_a^2 = f q$, dus $q = (0{,}09 - 0{,}045)/0{,}01 = 4{,}5$ miljard.
  De vergoeding van 45 miljoen is dan precies de waarde die hij toevoegt.
- Schat de markt zijn verwachte vaardigheid na een goed jaar op $\phi = 4\%$, dan groeit
  het fonds
  naar $q = (0{,}16 - 0{,}08)/0{,}01 = 8$ miljard, 78% meer dan de 4,5 miljard hierboven.

Het fonds met indexdeel is groter en deels een *closet indexer* (een fonds dat
voor actief beheer rekent maar grotendeels de index volgt). De code rekent de drie
gevallen na.

```{code-cell} ipython3
phi, b, f = 0.03, 0.005, 0.01        # expected skill, cost per $bn, fee

q_all_active = (phi - f) / b
q_active = phi / (2 * b)
q_total = (phi * q_active - b * q_active**2) / f
investor_alpha = (phi * q_active - b * q_active**2 - f * q_total) / q_total
value_added = phi * q_active - b * q_active**2

phi_new = 0.04
q_active_new = phi_new / (2 * b)
q_total_new = (phi_new * q_active_new - b * q_active_new**2) / f

print(f"versie 1: q* = {q_all_active:.2f} mld, vergoeding = {1000 * f * q_all_active:.1f} mln")
print(f"versie 2: q_a = {q_active:.2f} mld, q = {q_total:.2f} mld, "
      f"vergoeding = {1000 * f * q_total:.1f} mln")
print(f"toegevoegde waarde = {1000 * value_added:.1f} mln, nettoalpha belegger = {investor_alpha:.4%}")
print(f"na herwaardering naar phi = 4%: q = {q_total_new:.2f} mld "
      f"(instroom {q_total_new / q_total - 1:.0%})")
assert np.isclose(q_all_active, 4) and np.isclose(q_total, 4.5) and np.isclose(q_total_new, 8)
```

De belegger houdt in alle gevallen een nettoalpha van nul over, ondanks een
beheerder met een verwachte vaardigheid van drie procent. Het goede jaar brengt instroom
en geen
beter rendement, en daarmee wordt vaardigheid zichtbaar in de omvang van het fonds, zoals
we in de Intuïtie verwachtten.

Voor kwadratische kosten wordt alles expliciet, met $q_{a,t} = \phi_t/(2b)$ en
$q_t = \phi_t^2/(4bf)$ zolang $\phi_t \geq 2f$. De omvang is kwadratisch in de
verwachte vaardigheid, zodat een beheerder die twee keer zo goed wordt geacht, vier
keer zoveel geld beheert. Hogere schaalkosten $b$ maken het fonds kleiner, en een
hogere vergoeding $f$ ook, omdat de belegger dan al bij een kleiner fonds niets
extra's meer overhoudt. De vergoeding in dollars, $f q_t = \phi_t^2/(4b)$, hangt
echter niet van $f$ af, want een duurder fonds krijgt precies zoveel minder geld
dat de beheerder evenveel verdient.

### Wat het model voorspelt: geen persistentie in rendementen

Als vaardigheid bestaat en langzaam verandert, zou een naïeve lezing verwachten dat
de winnaars van vorig jaar ook dit jaar beter zijn. Carhart toetste dat
{cite}`Carhart1997` op 1892 fondsen over 1962–1993, in een steekproef zonder *survivorship
bias*
(vertekening doordat alleen overlevende fondsen in de data zitten). Hij vond dat
gemeenschappelijke factoren en kosten de persistentie vrijwel volledig verklaren.
Het eerdere "hot hands"-resultaat kwam grotendeels van *momentum* (relatieve
winnaars van het afgelopen jaar blijven een tijd winnen) in de aandelen van de fondsen
{cite}`JegadeeshTitman1993`. Alleen de slechtste fondsen bleven significant slecht.
Carhart concludeerde dat zijn resultaten het bestaan van
vaardige beheerders niet ondersteunen.

Volgens [](#thm-industrie-berk-green) is die conclusie te snel, omdat het
ontbreken van persistentie in *rendementen* precies is wat het model ook bij
vaardige beheerders voorspelt. Berk en Green kalibreerden hun model op
kapitaalstromen en overlevingskansen en vonden dat ongeveer 80% van de actieve
beheerders genoeg vaardigheid heeft om de eigen vergoeding terug te verdienen
{cite}`BerkGreen2004`. Vaardigheid moet dan in dollars worden gemeten.
Berk en Van Binsbergen vermenigvuldigden daarom de bruto alpha ten opzichte van de
goedkoopste indexfondsen met het beheerde vermogen {cite}`BerkVanBinsbergen2015`.
Volgens de werkversie van dat onderzoek uit 2012 voegde de gemiddelde beheerder op die
manier ongeveer 2 miljoen dollar per jaar toe, en die vaardigheid bleef over tien jaar
bestaan {cite}`BerkVanBinsbergen2012`.

### Alpha meten en de standaardfout

Een fonds moet niet de markt verslaan, maar een mechanische portefeuille met
dezelfde blootstellingen. Een fonds dat kleine waardeaandelen koopt en de markt
verslaat, heeft immers niets gedaan wat DFA niet goedkoper verkoopt. Voor fonds $i$
met overrendement $R^{e}_{i,t+1}$ en $K$ factorrendementen $\mathbf{f}_{t+1}$ is de
prestatieregressie

```{math}
:label: eq-industrie-regressie
R^{e}_{i,t+1} = \alpha_i + \boldsymbol{\beta}_i^\top \mathbf{f}_{t+1} + \varepsilon_{i,t+1}
```

Voor het CAPM is $\mathbf{f} = R^{e}_{m}$ {cite}`Jensen1968` en voor het driefactormodel
$\mathbf{f} = (R^{e}_{m}, \mathrm{SMB}, \mathrm{HML})$ {cite}`FamaFrench1993`. Het
vierfactormodel van Carhart {cite}`Carhart1997` voegt daar de momentumfactor UMD aan toe,
zoals in [](#eq-momentum-carhart). Omdat de factoren
overrendementen van verhandelbare portefeuilles zijn, is $\alpha_i$ het gemiddelde
rendement van het fonds min dat van de replicerende portefeuille
$\boldsymbol{\beta}_i^\top \mathbf{f}$. De vraag is dan hoe
lang we moeten kijken voordat $\hat\alpha_i$ iets zegt.

:::{prf:proposition} De standaardfout van alpha
:label: thm-industrie-se-alpha

Laat $\hat{\boldsymbol\mu}_f$ en $\hat{\boldsymbol\Sigma}_f$ het steekproefgemiddelde
en de (door $T$ gedeelde) steekproefcovariantiematrix van de factoren zijn. Onder
homoskedastische, ongecorreleerde storingen met variantie $\sigma^2_{\varepsilon}$ is
de OLS-schatter van $\alpha_i$ zuiver met

```{math}
:label: eq-industrie-se-alpha
\Var(\hat\alpha_i \mid \mathbf{F}) = \frac{\sigma^2_{\varepsilon}}{T}
\left(1 + \hat{\boldsymbol\mu}_f^\top \hat{\boldsymbol\Sigma}_f^{-1} \hat{\boldsymbol\mu}_f\right).
```
:::

:::{prf:proof}
:class: dropdown

Met $\mathbf{X} = [\mathbf{1}, \mathbf{F}]$ is
$\Var(\hat{\boldsymbol b}\mid\mathbf{F}) = \sigma^2_\varepsilon (\mathbf{X}^\top \mathbf{X})^{-1}$
en $\mathbf{X}^\top\mathbf{X}/T = \begin{pmatrix} 1 & \hat{\boldsymbol\mu}_f^\top \\
\hat{\boldsymbol\mu}_f & \hat{\boldsymbol\Sigma}_f + \hat{\boldsymbol\mu}_f\hat{\boldsymbol\mu}_f^\top \end{pmatrix}$.
Het $(1,1)$-element van de inverse is volgens de formule voor gepartitioneerde
matrices $1/(1 - \hat{\boldsymbol\mu}_f^\top(\hat{\boldsymbol\Sigma}_f +
\hat{\boldsymbol\mu}_f\hat{\boldsymbol\mu}_f^\top)^{-1}\hat{\boldsymbol\mu}_f)$.
Sherman-Morrison geeft $\hat{\boldsymbol\mu}_f^\top(\hat{\boldsymbol\Sigma}_f +
\hat{\boldsymbol\mu}_f\hat{\boldsymbol\mu}_f^\top)^{-1}\hat{\boldsymbol\mu}_f = s/(1+s)$
met $s = \hat{\boldsymbol\mu}_f^\top\hat{\boldsymbol\Sigma}_f^{-1}\hat{\boldsymbol\mu}_f$,
dus het element is $1/(1 - s/(1+s)) = 1+s$. Vermenigvuldig met
$\sigma^2_\varepsilon/T$. $\square$
:::

De term tussen haakjes in [](#eq-industrie-se-alpha) is één plus de gekwadrateerde
maximale Sharpe-ratio van de factoren per periode. Bij een Sharpe-ratio van
ongeveer 0,14 per maand is hij rond 1,02. Het probleem is daarom niet de formule maar de
ruis, net als bij
[de standaardfout van 2%](#00-01-rendementen) van een gemiddeld rendement. De *tracking
error* (de standaarddeviatie van
$\varepsilon$, het rendement dat de factoren niet verklaren) van een actief
aandelenfonds is al gauw $5\%$ per jaar. Een beheerder met een werkelijke alpha van
$1\%$ haalt na $T$ jaar dan een verwachte $t$-waarde van $1 \cdot \sqrt{T}/5$. Voor $t = 2$
zijn dan 100 jaar nodig, en bij een alpha van $2\%$ nog altijd 25 jaar.
Omdat één fonds zo niet te beoordelen is, kijkt de literatuur naar de hele
cross-sectie van fondsen.

### Geluk of vaardigheid: de bootstrap

Als geen enkel fonds vaardig is, volgen de geschatte $t$-waarden van alpha de verdeling
van de ruis, zodat alleen een staart die dikker is dan die van de ruis op vaardigheid wijst.
Fondsrendementen zijn echter niet normaal, hebben verschillende
volatiliteiten en zijn onderling sterk gecorreleerd, zodat een tabel van de
$t$-verdeling de verkeerde nulhypothese beschrijft. De *bootstrap* (herhaald trekken
uit de eigen data) maakt die nulverdeling daarom uit de data zelf. Fama en French hielden
ook de correlatie tussen fondsen vast door hele maanden te trekken {cite}`FamaFrench2010`.

:::{prf:algorithm} Bootstrap van de cross-sectie van $t(\alpha)$ (Fama en French 2010)
:label: thm-industrie-bootstrap

**Invoer.** Overrendementen $R^{e}_{i,t}$ van $M$ fondsen en factoren $\mathbf{f}_t$,
$t = 1,\dots,T$.

1. Schat [](#eq-industrie-regressie) voor elk fonds en bewaar $\hat\alpha_i$ en de
   cross-sectie $t(\hat\alpha_i)$.
2. Leg de nulhypothese op met $\tilde R_{i,t} = R^{e}_{i,t} - \hat\alpha_i$. Nu heeft
   elk fonds in de steekproef een alpha van precies nul, en houdt het zijn bèta's,
   zijn residuen en hun correlatie met andere fondsen.
3. Trek voor $b = 1,\dots,B$ een rij van $T$ maanden met teruglegging, *dezelfde
   maanden voor alle fondsen en factoren*, schat de regressie opnieuw op $\tilde R$
   en bewaar de cross-sectie $t^{(b)}(\hat\alpha_i)$.
4. Vergelijk voor elk percentiel $p$ het werkelijke percentiel van $t(\hat\alpha_i)$
   met het gemiddelde gesimuleerde percentiel, en rapporteer het aandeel simulaties
   met een lager percentiel dan het werkelijke.
:::

Omdat alle fondsen dezelfde maanden krijgen, bevat de gesimuleerde cross-sectie ook
de gemeenschappelijke schokken van de echte. Liggen de werkelijke staartpercentielen
in bijna alle trekkingen buiten de simulaties, dan zijn er meer extreme fondsen dan
geluk verklaart. Fama en French vonden dat weinig Amerikaanse aandelenfondsen genoeg
verdienen om hun kosten te dekken. Vóór kosten zagen ze in beide staarten wel sporen van
slechte en goede beheerders {cite}`FamaFrench2010`.

### Veel toetsen tegelijk: de false discovery rate

Wie 2000 fondsen toetst op een niveau van 5%, vindt zonder enige vaardigheid
honderd "significante" fondsen. De vraag is daarom niet hoe vaak een fonds zonder
vaardigheid ten onrechte wordt verworpen, maar welk deel van de verwerpingen
onterecht is. Stel dat $M$ hypothesen $H_1,\dots,H_M$ met p-waarden
$p_1,\dots,p_M$ zijn getoetst, waarvan $M_0$ waar. Met $V$ het aantal onterechte en
$R$ het totale aantal verwerpingen is de *false discovery rate* (het verwachte
aandeel onterechte ontdekkingen) $\mathrm{FDR} = \E[V/\max(R,1)]$.

:::{prf:theorem} Benjamini-Hochberg
:label: thm-industrie-bh

Orden de p-waarden $p_{(1)} \leq \dots \leq p_{(M)}$, neem
$k = \max\{j : p_{(j)} \leq q j / M\}$ en verwerp $H_{(1)},\dots,H_{(k)}$. Als de
p-waarden van de ware nulhypothesen onafhankelijk en uniform zijn, en onafhankelijk
van de andere p-waarden, dan is $\mathrm{FDR} = q\, M_0/M \leq q$
{cite}`BenjaminiHochberg1995`.
:::

:::{prf:proof}
:class: dropdown

Neem een ware nulhypothese $i$ en laat $R^{(i)}$ het aantal verwerpingen zijn als
$p_i$ door $0$ wordt vervangen, zodat $R^{(i)}$ alleen van de andere p-waarden
afhangt. De procedure heeft de eigenschap dat
$\{H_i \text{ verworpen}, R = k\} = \{p_i \leq qk/M,\ R^{(i)} = k\}$, omdat een
verworpen $p_i$ het aantal verwerpingen niet verandert als hij naar nul gaat. Dus

$$
\mathrm{FDR} = \sum_{i \in H_0} \sum_{k=1}^{M} \frac{1}{k}
\Pr\!\left(p_i \leq \tfrac{qk}{M},\ R^{(i)} = k\right)
= \sum_{i \in H_0} \sum_{k=1}^{M} \frac{1}{k}\,\frac{qk}{M}\,\Pr\!\left(R^{(i)} = k\right)
= \frac{q}{M}\sum_{i\in H_0} 1 = q\,\frac{M_0}{M},
$$

waarbij de tweede stap onafhankelijkheid en uniformiteit gebruikt en de derde dat
$R^{(i)} \geq 1$ zeker is, want $p_i = 0$ wordt altijd verworpen. $\square$
:::

Barras, Scaillet en Wermers gebruikten dezelfde uniformiteit
{cite}`BarrasScailletWermers2010` om niet te
beslissen welk fonds vaardig is, maar te schatten *hoeveel* fondsen dat zijn. Ze
delen de fondsen in drie groepen: fondsen met een alpha na kosten van nul (aandeel
$\pi_0$), onvaardige fondsen met een negatieve alpha ($\pi_A^-$) en vaardige fondsen
met een positieve alpha ($\pi_A^+$).

:::{prf:proposition} Het aandeel nul-alphafondsen
:label: thm-industrie-pi0

Als de tweezijdige p-waarden van nul-alphafondsen uniform zijn, dan is voor elke
$\lambda \in (0,1)$ de schatter
$\hat\pi_0(\lambda) = \#\{i : p_i > \lambda\} / (M(1-\lambda))$ zuiver of naar boven
vertekend, $\E[\hat\pi_0(\lambda)] \geq \pi_0$. Met
$\hat S^{+}_\gamma = \#\{i: p_i \leq \gamma,\ t_i > 0\}/M$ schat
$\hat\pi^{+}_A = \hat S^{+}_\gamma - \hat\pi_0\,\gamma/2$ het aandeel vaardige fondsen.
:::

:::{prf:proof}
Het verwachte aantal nulfondsen met $p_i > \lambda$ is $M\pi_0(1-\lambda)$, en fondsen
met een ware alpha hebben een niet-negatieve kans op $p_i > \lambda$, dus
$\E\#\{p_i > \lambda\} \geq M\pi_0(1-\lambda)$. Van de nulfondsen valt naar verwachting
een fractie $\gamma/2$ in het positieve significante gebied, en die fractie trekt de
tweede formule af. $\square$
:::

Het bewijs laat ook de zwakte zien: een vaardig fonds dat niet significant is, telt
mee als nulfonds, zodat $\hat\pi^{+}_A$ bij weinig data te laag uitvalt. Barras,
Scaillet en Wermers vonden dat ongeveer driekwart van de fondsen na kosten een alpha van
nul had,
wat past bij het evenwicht van Berk en Green. Vóór 1996 zagen ze een flink aandeel
vaardige fondsen, maar in 2006 vrijwel geen meer {cite}`BarrasScailletWermers2010`.

```{admonition} Samengevat
:class: tip

- Vóór kosten halen de actieve beleggers samen precies de markt, en na kosten
  blijven ze achter met hun gemiddelde kosten ([](#eq-industrie-sharpe)).
- In het evenwicht van Berk en Green groeit een vaardig fonds tot de belegger een
  nettoalpha van nul overhoudt, zodat vaardigheid de omvang voorspelt en niet het
  rendement ([](#eq-industrie-bg-rendement)).
- De standaardfout van alpha daalt met $\sqrt{T}$ en is bij een tracking error van
  5% na twintig jaar nog ruim één procentpunt ([](#eq-industrie-se-alpha)).
- De bootstrap en de false discovery rate beoordelen de hele cross-sectie in plaats
  van één fonds ({prf:ref}`thm-industrie-bootstrap`, {prf:ref}`thm-industrie-pi0`).
```

## Simulatie: 2000 fondsen, waarvan een paar kunnen wat ze beloven

Welk deel van de vaardige fondsen vinden de $t$-toets, de bootstrap en de false discovery
rate terug als we de waarheid kennen? Dat hangt vermoedelijk af van de lengte van de
steekproef, dus variëren we die ook. Er zijn
$M = 2000$ fondsen en $T = 240$ maanden. Van de fondsen heeft 70% een alpha na
kosten van nul, 10% een alpha van $+2\%$ per jaar en 20% een alpha van $-2\%$ per jaar.
Die laatste groep verliest twee keer de kosten van X en Y uit het toy-voorbeeld.

Elk fonds heeft een marktbèta tussen $0{,}8$ en $1{,}2$ en een tracking error van
$1{,}5\%$ per maand, ongeveer $5\%$ per jaar zoals in de theorie. De marktpremie is
$0{,}6\%$ per maand met een volatiliteit van $4{,}5\%$. Voor een vaardig fonds is de
verwachte $t$-waarde $0{,}167\sqrt{240}/1{,}5 \approx 1{,}7$, zodat zo'n fonds wel
vaardig is, maar gemiddeld niet significant. De eerste cel schat voor elk fonds de
CAPM-alpha en de $t$-waarde
ervan.

```{code-cell} ipython3
def alpha_tstats(Y, F):
    """OLS intercepts, t-statistics and slopes for every column of Y on factors F.

    Y is a (T, M) array of excess returns, F a (T, K) array of factors without a
    constant. Standard errors are homoskedastic.
    """
    # TODO: naar hap.stats (cross-sectional alpha regression)
    T = Y.shape[0]
    X = np.column_stack([np.ones(T), F])
    XtX_inv = np.linalg.inv(X.T @ X)
    coef = XtX_inv @ X.T @ Y
    resid = Y - X @ coef
    s2 = (resid**2).sum(axis=0) / (T - X.shape[1])
    se_alpha = np.sqrt(s2 * XtX_inv[0, 0])
    return coef[0], coef[0] / se_alpha, coef[1:]


def simulate_universe(n_months, rng, counts=(1400, 200, 400), alpha_ann=0.02,
                      sigma_eps=0.015):
    """Simulate fund excess returns: groups 0 = zero alpha, 1 = skilled, 2 = unskilled."""
    groups = np.repeat([0, 1, 2], counts)
    alpha = np.array([0.0, alpha_ann, -alpha_ann])[groups] / 12
    mkt = rng.normal(0.006, 0.045, n_months)
    beta = rng.uniform(0.8, 1.2, groups.size)
    eps = rng.normal(0.0, sigma_eps, (n_months, groups.size))
    return alpha + np.outer(mkt, beta) + eps, mkt[:, None], groups


Y_sim, F_sim, groups = simulate_universe(240, rng)
alpha_sim, t_sim, _ = alpha_tstats(Y_sim, F_sim)

group_names = ["nul-alpha", "vaardig", "onvaardig"]
pd.DataFrame({
    "aantal": [np.sum(groups == g) for g in range(3)],
    "gem. t(alpha)": [t_sim[groups == g].mean() for g in range(3)],
    "aandeel t > 2": [np.mean(t_sim[groups == g] > 2) for g in range(3)],
    "aandeel t < -2": [np.mean(t_sim[groups == g] < -2) for g in range(3)],
}, index=group_names).round(3)
```

De tabel laat het probleem zien. Van de 1400 nulfondsen haalt 2,0% toch $t > 2$, en
dat zijn 28 fondsen met geluk, terwijl van de 200 vaardige fondsen maar 36% die
drempel haalt. Van de honderd fondsen met $t > 2$ is daardoor iets meer dan een kwart niet
vaardig, en bijna twee derde van de vaardige fondsen blijft onzichtbaar. In de
figuur hieronder gaat het om de rechterstaart, waar de gestapelde balken van
nulfondsen en vaardige fondsen door elkaar lopen.

```{code-cell} ipython3
:label: cel-industrie-tverdeling
:tags: [hide-input]

fig, ax = plt.subplots()
bins = np.linspace(-6, 6, 61)
ax.hist([t_sim[groups == g] for g in (2, 0, 1)], bins=bins, stacked=True,
        label=["onvaardig (20%)", "nul-alpha (70%)", "vaardig (10%)"], edgecolor="white")
grid = np.linspace(-6, 6, 400)
ax.plot(grid, stats.t.pdf(grid, 238) * t_sim.size * (bins[1] - bins[0]), color="black",
        lw=1.2, label="nulverdeling, alle fondsen")
for c in (-2, 2):
    ax.axvline(c, color="black", ls="--", lw=0.8)
ax.set_xlabel("$t$-waarde van de geschatte alpha")
ax.set_ylabel("Aantal fondsen")
ax.set_title("2000 gesimuleerde fondsen over twintig jaar")
ax.legend()
plt.show()
```

:::{figure} #cel-industrie-tverdeling
:label: fig-industrie-tverdeling
:width: 90%

De cross-sectie van $t(\hat\alpha)$ is een mengsel van drie verdelingen die elkaar
grotendeels overlappen. De vaardige fondsen verschuiven de rechterstaart, maar veel
van de fondsen met $t > 2$ zijn nulfondsen met geluk, en de meeste vaardige fondsen
halen de drempel niet.
:::

Omdat de $t$-toets per fonds zo weinig vaardige fondsen vindt, passen we nu de
bootstrap toe alsof we de waarheid niet kenden, met 500 trekkingen. Fama en French
schatten zelf geen aandeel vaardige fondsen. Om de methoden toch te vergelijken, nemen we
het deel van de fondsen
boven het 90e percentiel van de bootstrapverdeling, min de 10% die daar zonder
vaardigheid verwacht wordt.

```{code-cell} ipython3
def bootstrap_t(Y, F, n_boot, rng):
    """Fama-French (2010) bootstrap: impose zero alpha, resample months jointly."""
    alpha, t_actual, _ = alpha_tstats(Y, F)
    Y_null = Y - alpha
    T = Y.shape[0]
    t_boot = np.empty((n_boot, Y.shape[1]))
    for b_i in range(n_boot):
        idx = rng.integers(0, T, T)
        t_boot[b_i] = alpha_tstats(Y_null[idx], F[idx])[1]
    return t_actual, t_boot


def compare_percentiles(t_actual, t_boot, pcts):
    """Actual cross-sectional percentiles against their bootstrap distribution."""
    actual = np.percentile(t_actual, pcts)
    simulated = np.percentile(t_boot, pcts, axis=1)          # (len(pcts), n_boot)
    return pd.DataFrame({
        "werkelijk": actual,
        "gem. simulatie": simulated.mean(axis=1),
        "% sim < werkelijk": 100 * (simulated < actual[:, None]).mean(axis=1),
    }, index=[f"p{p}" for p in pcts])


t_actual, t_boot = bootstrap_t(Y_sim, F_sim, 500, rng)
compare_percentiles(t_actual, t_boot, [1, 5, 10, 25, 50, 75, 90, 95, 99]).round(2)
```

De bootstrap ziet dat er iets aan de hand is, want links liggen de werkelijke
percentielen in alle simulaties lager en rechts vanaf het 90e percentiel hoger. Dat
is het patroon dat Fama en French beschrijven. De volgende cel zet de bootstrap,
de schatter van Barras, Scaillet en Wermers en de procedure van Benjamini en
Hochberg naast de waarheid.

```{code-cell} ipython3
def fdr_proportions(t, df, lam=0.5, gamma=0.2):
    """Barras-Scaillet-Wermers (2010) proportions of zero, unskilled and skilled funds."""
    # TODO: naar hap.stats (false discovery rate)
    p = 2 * stats.t.sf(np.abs(t), df)
    pi0 = min(1.0, np.mean(p > lam) / (1 - lam))
    significant = p <= gamma
    pi_minus = np.mean(significant & (t < 0)) - pi0 * gamma / 2
    pi_plus = np.mean(significant & (t > 0)) - pi0 * gamma / 2
    return pi0, pi_minus, pi_plus


def benjamini_hochberg(p, q):
    """Boolean mask of hypotheses rejected by the Benjamini-Hochberg step-up rule."""
    order = np.argsort(p)
    below = p[order] <= q * np.arange(1, p.size + 1) / p.size
    k = below.nonzero()[0].max() + 1 if below.any() else 0
    reject = np.zeros(p.size, dtype=bool)
    reject[order[:k]] = True
    return reject


ff_cutoff = np.percentile(t_boot, 90)
ff_plus = np.mean(t_actual > ff_cutoff) - np.mean(t_boot > ff_cutoff)
pi0, pi_minus, pi_plus = fdr_proportions(t_sim, df=238)

bh = benjamini_hochberg(stats.t.sf(t_sim, 238), q=0.10)
realised_fdp = np.mean(groups[bh] != 1) if bh.any() else np.nan

pd.DataFrame({
    "waarheid": [0.70, 0.20, 0.10, 0.10, np.nan, np.nan],
    "schatting": [pi0, pi_minus, pi_plus, ff_plus, bh.sum(), realised_fdp],
}, index=["pi0 (BSW)", "pi- (BSW)", "pi+ (BSW)", "vaardig (FF-bootstrap)",
          "BH-ontdekkingen, q = 10%", "gerealiseerd aandeel onterecht"]).round(3)
```

Om vaardige fondsen te tellen is de bootstrap zwak, want vertaald naar een aandeel vindt
hij 2%
vaardige fondsen tegen 10% in werkelijkheid. De schatter van Barras, Scaillet en
Wermers geeft $\hat\pi_0 = 0{,}80$ en $\hat\pi_A^+ = 0{,}04$, ook te laag, omdat
vaardige fondsen die niet significant zijn als nulfonds meetellen. Benjamini-Hochberg
vindt 16 vaardige fondsen zonder één onterechte ontdekking, wat betrouwbaar is, maar
het zijn er 16 van de 200.

Eén universum zegt weinig over een schatter. We herhalen de simulatie daarom
tweehonderd keer, voor steekproeven van tien, twintig en veertig jaar, en kijken naar
de verdeling van $\hat\pi_A^+$.

```{code-cell} ipython3
horizons = [120, 240, 480]
n_universes = 200
pi_plus_draws = {T: np.empty(n_universes) for T in horizons}
pi0_draws = {T: np.empty(n_universes) for T in horizons}
for T in horizons:
    for u in range(n_universes):
        Y_u, F_u, _ = simulate_universe(T, rng)
        t_u = alpha_tstats(Y_u, F_u)[1]
        pi0_draws[T][u], _, pi_plus_draws[T][u] = fdr_proportions(t_u, df=T - 2)

pd.DataFrame({
    "gem. pi0": [pi0_draws[T].mean() for T in horizons],
    "gem. pi+": [pi_plus_draws[T].mean() for T in horizons],
    "SD pi+": [pi_plus_draws[T].std(ddof=1) for T in horizons],
    "5e pct pi+": [np.percentile(pi_plus_draws[T], 5) for T in horizons],
    "95e pct pi+": [np.percentile(pi_plus_draws[T], 95) for T in horizons],
}, index=[f"{T // 12} jaar" for T in horizons]).round(3)
```

Het geschatte aandeel vaardige fondsen groeit met de lengte van de steekproef, van
gemiddeld 0,032 na tien jaar tot 0,085 na veertig jaar, terwijl de spreiding tussen
universa klein blijft. In de figuur gaat het om de afstand tussen elk histogram en
de verticale lijn bij het ware aandeel van 10%.

```{code-cell} ipython3
:label: cel-industrie-fdr
:tags: [hide-input]

fig, ax = plt.subplots()
for T in horizons:
    ax.hist(pi_plus_draws[T], bins=30, alpha=0.6, label=f"{T // 12} jaar")
ax.axvline(0.10, color="black", lw=1.2, label="ware aandeel vaardig")
ax.set_xlabel("geschat aandeel vaardige fondsen $\\hat\\pi_A^+$")
ax.set_ylabel("Aantal gesimuleerde universa")
ax.set_title("Het aandeel vaardige fondsen, geschat in 200 universa")
ax.legend()
plt.show()
```

:::{figure} #cel-industrie-fdr
:label: fig-industrie-fdr
:width: 90%

De schatter $\hat\pi_A^+$ varieert weinig tussen universa, maar is sterk vertekend:
met tien jaar data vindt hij gemiddeld een derde van de vaardige fondsen, met veertig
jaar 85%. Het probleem is gebrek aan onderscheidend vermogen, niet ruis, zodat een
laag geschat aandeel vaardige fondsen ook op te weinig data kan wijzen.
:::

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Fama en French, *Luck versus Skill in the Cross-Section of Mutual Fund
Returns*, Journal of Finance 2010 {cite}`FamaFrench2010`. Voor de persistentie gebruiken we Carhart, *On Persistence in Mutual Fund Performance*, Journal of Finance 1997
{cite}`Carhart1997`.

**Wat.** De gemiddelde nettoalpha van actieve fondsen tegen drie factormodellen,
de cross-sectie van $t(\hat\alpha)$ tegen een bootstrap zonder vaardigheid
({prf:ref}`thm-industrie-bootstrap`), en de alpha na sortering op de voorgaande
drie jaar.

**Data hier.** Maandrendementen na kosten van 50 actieve Amerikaanse
aandelenfondsen en 6 indexfondsen van Vanguard via `hap.data.yahoo(...)`, en
factoren via `hap.data.french(...)`.

**Verschil met het origineel.** De originelen gebruiken een database zonder
survivorship bias met duizenden fondsen, ook opgeheven fondsen. Wij hebben 50
fondsen die we kennen omdat ze nog bestaan en groot zijn, een steekproef van
overlevenden met de vertekening uit [](#02-05-crsp-tape) in het voordeel van de
fondsen {cite}`BrownGoetzmannIbbotsonRoss1992`.

**Verwachte afwijking.** Het totale-marktindexfonds VTSMX moet een kleine negatieve
alpha hebben, in de orde van zijn kosten; is die positief, dan zit er een fout in
de code. Door de selectie op overleven verwachten we voor de actieve fondsen een
gemiddelde alpha binnen één procentpunt van nul in plaats van de $-1{,}1\%$ van Jensen,
bootstrappercentielen boven de gesimuleerde en geen persistentie met $t > 2$.
```

```{warning}
Fondsen die sinds 1996 slecht presteerden, zijn opgeheven of opgegaan in andere
fondsen en ontbreken hier. Elke alpha in deze sectie is daarom een bovengrens voor
wat een belegger met een willekeurig fonds uit 1996 verdiende.
```

De eerste cel haalt de koersen op, zet ze om naar maandelijkse overrendementen en
houdt de fondsen met een volledige historie sinds 1996 over.

```{code-cell} ipython3
tickers = (
    "FDGRX FLPSX FEQIX FDVLX FBGRX FOCPX FTRNX FFIDX FDCAX FGRIX FMCSX FDSSX FMAGX FCNTX "
    "AGTHX AIVSX ANCFX AMCPX AWSHX AMRMX PRGFX PRNHX TRBCX PRFDX PRDGX RPMGX PRWAX TRVLX "
    "VWNDX VWNFX VWUSX VPMCX VEIPX VQNPX VEXPX VMRGX VHCOX DODGX TWCUX TWCGX JANSX SEQUX "
    "MUTHX FKGRX NYVTX OAKMX PENNX MPGFX NBGNX HACAX PRBLX LMVTX CGMFX "
    "VFINX VTSMX NAESX VIVAX VIGRX VEXMX"
).split()
index_funds = {
    "VFINX": "Vanguard 500 Index", "VTSMX": "Vanguard Total Stock Market Index",
    "NAESX": "Vanguard Small-Cap Index", "VIVAX": "Vanguard Value Index",
    "VIGRX": "Vanguard Growth Index", "VEXMX": "Vanguard Extended Market Index",
}

prices = hap_data.yahoo(tickers, "1985-01-01").resample("ME").last()
fund_ret = (prices / prices.shift(1) - 1).iloc[1:]
factors = hap_data.french("F-F_Research_Data_Factors").join(hap_data.french("F-F_Momentum_Factor"))

sample = fund_ret.index.intersection(factors.index)
sample = sample[sample >= "1996-01-01"]
excess = fund_ret.loc[sample].sub(factors.loc[sample, "RF"], axis=0).dropna(axis=1)
fac = factors.loc[sample]
active_cols = [c for c in excess.columns if c not in index_funds]

print(f"{sample[0]:%Y-%m} t/m {sample[-1]:%Y-%m}: {len(sample)} maanden, "
      f"{len(active_cols)} actieve fondsen, {excess.shape[1] - len(active_cols)} indexfondsen")
print("weggevallen (te korte historie):", sorted(set(tickers) - set(excess.columns)))
```

Er blijven 367 maanden over, van januari 1996 tot en met juli 2026, en drie fondsen
vallen af omdat hun historie te kort is. De volgende cel schat de alpha van elk
fonds tegen het CAPM, het driefactormodel en het model van Carhart.

```{code-cell} ipython3
models = {"CAPM": ["Mkt-RF"], "FF3": ["Mkt-RF", "SMB", "HML"],
          "Carhart": ["Mkt-RF", "SMB", "HML", "Mom"]}
Y_act = excess[active_cols].to_numpy()
ew_active = Y_act.mean(axis=1, keepdims=True)

rows = {}
for name, cols in models.items():
    F = fac[cols].to_numpy()
    a_act, t_act, _ = alpha_tstats(Y_act, F)
    a_ew, t_ew, _ = alpha_tstats(ew_active, F)
    a_idx, t_idx, _ = alpha_tstats(excess[list(index_funds)].to_numpy(), F)
    rows[name] = {
        "actief: gem. alpha (%/jr)": 1200 * a_act.mean(),
        "actief: mediaan t": np.median(t_act),
        "actief: aandeel t > 2": np.mean(t_act > 2),
        "actief: aandeel t < -2": np.mean(t_act < -2),
        "gelijkgewogen actief: alpha (%/jr)": 1200 * a_ew[0],
        "gelijkgewogen actief: t": t_ew[0],
        **{f"{index_funds[k]}: alpha (%/jr)": 1200 * v for k, v in zip(index_funds, a_idx)},
        "VFINX: t": t_idx[0],
    }
performance = pd.DataFrame(rows)
performance.round(2)
```

Het totale-marktindexfonds VTSMX heeft de verwachte alpha van $-0{,}19\%$ per jaar
tegen het CAPM. De small-cap- en extended-marketfondsen blijven ruim één procent
per jaar achter bij de factormodellen, terwijl het groei-indexfonds er juist boven
ligt. Dat komt niet door slechte of goede beheerders, maar doordat SMB en HML papieren
portefeuilles zonder kosten zijn die niemand kan kopen. Een fonds dat positief op die
factoren laadt, lijkt daardoor achter te blijven, en een groeifonds met een negatieve
HML-lading lijkt om dezelfde reden te winnen. Daarom meten
{cite:t}`BerkVanBinsbergen2015` vaardigheid tegen indexfondsen.

De 50 overlevende actieve fondsen doen het beter dan de fondsen van Jensen. Hun
gelijkgewogen portefeuille heeft een Carhart-alpha van $0{,}53\%$ per jaar, niet
significant, en 14% van de fondsen haalt $t > 2$ (de tabel aan het eind zet de getallen
naast de originelen). Dat ligt ruim anderhalf procentpunt boven de $-1{,}1\%$ die Jensen
na kosten vond, en zo groot kan het effect van selectie op overleven dus zijn. De
bootstrap hieronder gebruikt
2000 trekkingen en percentielen tussen het 5e en het 95e, omdat 50 fondsen geen
staart hebben.

```{code-cell} ipython3
F_c4 = fac[models["Carhart"]].to_numpy()
t_real, t_real_boot = bootstrap_t(Y_act, F_c4, 2000, rng)
compare_percentiles(t_real, t_real_boot, [5, 10, 25, 50, 75, 90, 95]).round(2)
```

Vanaf het 25e percentiel liggen de werkelijke $t$-waarden boven het gemiddelde van
de simulaties, en de mediaan ligt hoger dan in 95% van de trekkingen. In de figuur
gaat het om de zwarte lijn van de werkelijke fondsen, die als geheel rechts van het
histogram zonder vaardigheid ligt.

```{code-cell} ipython3
:label: cel-industrie-bootstrap-echt
:tags: [hide-input]

fig, ax = plt.subplots()
bins = np.linspace(-5, 5, 41)
ax.hist(t_real_boot.ravel(), bins=bins, density=True, alpha=0.5,
        label="bootstrap, alle alpha's nul")
ax.hist(t_real, bins=bins, density=True, histtype="step", lw=2, color="black",
        label=f"werkelijk, {len(active_cols)} actieve fondsen")
ax.set_xlabel("$t$-waarde van de Carhart-alpha")
ax.set_ylabel("Dichtheid")
ax.set_title("Overlevende actieve fondsen tegen een bootstrap zonder vaardigheid, 1996-2026")
ax.legend()
plt.show()
```

:::{figure} #cel-industrie-bootstrap-echt
:label: fig-industrie-bootstrap-echt
:width: 90%

De hele verdeling van werkelijke $t$-waarden ligt rechts van de bootstrap zonder
vaardigheid, met een mediaan van $0{,}74$ tegen $-0{,}03$ in de simulaties. Zo ziet
een steekproef eruit die op succes is geselecteerd, en dat hoeft geen vaardigheid te
zijn.
:::

Voor de persistentie schatten we elk jaar van 1999 tot en met 2025 de
Carhart-alpha van elk actief fonds over de voorgaande 36 maanden. Daarna delen we de
fondsen in drie groepen. Het abnormale rendement in het jaar erna meten we met de bèta's
uit de vormingsperiode, zodat er in de evaluatie niets wordt geschat.

```{code-cell} ipython3
years = range(1999, 2026)
spread, top_alpha, bottom_alpha, rank_corr_real = [], [], [], []
for year in years:
    form = (excess.index >= f"{year - 3}-01-01") & (excess.index < f"{year}-01-01")
    evaluate = (excess.index >= f"{year}-01-01") & (excess.index < f"{year + 1}-01-01")
    a_form, _, betas = alpha_tstats(Y_act[form], F_c4[form])
    abnormal = 12 * (Y_act[evaluate] - F_c4[evaluate] @ betas).mean(axis=0)
    ranks = pd.qcut(a_form, 3, labels=False)
    top_alpha.append(abnormal[ranks == 2].mean())
    bottom_alpha.append(abnormal[ranks == 0].mean())
    spread.append(top_alpha[-1] - bottom_alpha[-1])
    rank_corr_real.append(stats.spearmanr(a_form, abnormal)[0])

spread = np.array(spread)
pd.DataFrame({
    "gemiddelde": [100 * np.mean(top_alpha), 100 * np.mean(bottom_alpha), 100 * spread.mean(),
                   np.mean(rank_corr_real)],
    "SE": [100 * np.std(top_alpha, ddof=1) / np.sqrt(len(spread)),
           100 * np.std(bottom_alpha, ddof=1) / np.sqrt(len(spread)),
           100 * spread.std(ddof=1) / np.sqrt(len(spread)),
           np.std(rank_corr_real, ddof=1) / np.sqrt(len(spread))],
}, index=["hoogste terciel: alpha volgend jaar (%)", "laagste terciel: alpha volgend jaar (%)",
          "verschil hoog - laag (%)", "rangcorrelatie vorming-evaluatie"]).assign(
    t=lambda d: d["gemiddelde"] / d["SE"]).round(2)
```

Het beste derde van de fondsen haalt het jaar daarna gemiddeld $0{,}13\%$ alpha en het
slechtste derde $-0{,}37\%$. Het verschil van $0{,}51$ procentpunt heeft over 27 jaar
een standaardfout van $0{,}59$ ($t = 0{,}86$), zodat er geen persistentie te zien is.
Dat bewijst niet dat ze ontbreekt, want bij deze spreiding zou een verschil van een
half procent per jaar pas na ongeveer 145 jaar een $t$-waarde van 2 halen.

| grootheid | origineel | hier |
|---|---|---|
| gemiddelde nettoalpha actieve fondsen | $-1{,}1\%$ per jaar (Jensen) | $+0{,}53\%$, $t = 1{,}36$ |
| alpha totale-marktindexfonds | klein en negatief (verwachting) | $-0{,}19\%$ |
| mediaan $t(\hat\alpha)$ tegen bootstrap | weinig fondsen dekken hun kosten (Fama en French) | $0{,}74$ tegen $-0{,}03$ |
| persistentie, hoogste min laagste groep | alleen de slechtste fondsen (Carhart) | $0{,}51$ procentpunt, $t = 0{,}86$ |

Gedeeltelijk geslaagd. Het indexfonds en de persistentie gedragen zich zoals verwacht. Het
niveau van de alpha en de verschuiving in de bootstrap wijken af van de originelen, maar
in de richting die de selectie op overleven meebrengt. Juist daardoor
kunnen deze data
de conclusie van Fama en French niet toetsen, want een steekproef van overlevenden
laat geen fondsen zien die hun kosten niet terugverdienden.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Sharpes rekenkunde en het model van Berk en Green
verklaren samen drie hardnekkige feiten over de beleggingsindustrie. De gemiddelde
actieve dollar blijft na kosten achter, winnaars blijven geen winnaars, en toch
stroomt geld achter winnaars aan. Ze verklaren ook de sociologie, want de oprichters
van DFA en AQR hoefden de rekenkunde niet te weerleggen om een bedrijf te
bouwen. De rekenkunde zegt immers niets over wie wint, maar alles over wat het kost.

**Waar het breekt.** Het breekt bij het meten van vaardigheid zelf. In onze
simulatie met 10% vaardige fondsen vond de beste schatter met twintig jaar data er
gemiddeld 6%. Onze echte steekproef levert een bootstrap die op vaardigheid lijkt, maar door
de selectie op overleven valt die uitkomst niet te interpreteren. Barras, Scaillet en
Wermers zagen het aandeel vaardige fondsen tussen 1996 en 2006 naar bijna nul dalen. Of de
vaardigheid verdween of de toets zijn onderscheidend vermogen verloor, laten de data niet
zien.

**Risico of vergissing?** In de Chicago-lezing is kapitaal net zo concurrerend als
informatie. Vaardigheid bestaat dan en wordt beloond in vergoedingen, en DFA en AQR
verkopen een vergoeding voor risico. In de Yale-lezing jagen beleggers rendementen na die
ze niet kunnen beoordelen. Dan zijn de premies achter
DFA en AQR vergissingen van anderen, en overleven dure fondsen omdat hun klanten de
rekenkunde niet kennen. Data over de redenen waarom beleggers hun geld verplaatsen,
zouden de lezingen kunnen scheiden, maar die data zijn omstreden. Santa-Clara's
praktijkles past op
beide: wie een indexfonds koopt, draagt risico met een premie, en wie een actief
fonds koopt, denkt iets te weten wat de prijs niet weet.

**Wat er daarna kwam.** Elke alpha in dit college is gemeten tegen een
factormodel, en de keuze van dat model bepaalde het antwoord. Het volgende college,
[](#05-26-sdf-unificatie), laat zien dat elk zulk model een uitspraak is over één
*stochastic discount factor* (SDF, de stochastische factor waarmee alle payoffs
worden verdisconteerd).

## Oefeningen

:::{exercise}
:label: ex-industrie-1

**Rekenkunde met particulieren.** In een markt bezitten indexbeleggers 30%,
beleggingsfondsen 30% en particuliere actieve beleggers 40% van alle aandelen.
Particulieren halen bruto gemiddeld $2\%$ per jaar minder dan de markt, zoals in de
handelsdata van {cite:t}`BarberOdean2000`.

1. Welke gemiddelde bruto alpha moeten de fondsen dan halen?
2. Fondsen rekenen $1\%$ kosten, indexfondsen $0{,}1\%$. Wat is het verschil in
   nettorendement tussen de gemiddelde fondsbelegger en de indexbelegger?
3. Bewijs dat de gemiddelde bruto alpha van de fondsen nul is zodra de particulieren
   óók passief worden.
:::

:::{solution} ex-industrie-1
:class: dropdown

Pas {prf:ref}`thm-industrie-sharpe` toe op de actieve beleggers samen. Hun
vermogensgewogen alpha is nul, dus $0{,}4 \times (-2\%) + 0{,}3\, a_F = 0$ en
$a_F = 0{,}8/0{,}3 = 2{,}67\%$. Na kosten haalt de fondsbelegger $2{,}67 - 1 = 1{,}67\%$
boven de markt, tegen $-0{,}1\%$ voor de indexbelegger, een voorsprong van $1{,}77$
procentpunt. Worden de particulieren passief, dan bestaat $\mathcal{A}$ alleen uit
fondsen, en zegt de propositie dat hun gewogen bruto alpha nul is.

```{code-cell} ipython3
w_index, w_funds, w_retail = 0.30, 0.30, 0.40
alpha_retail = -0.02
alpha_funds = -w_retail * alpha_retail / w_funds
print(f"bruto alpha fondsen          : {alpha_funds:.4%}")
print(f"netto voorsprong op de index : {(alpha_funds - 0.01) - (-0.001):.4%}")
```

De rekenkunde verbiedt dus niet dat fondsen winnen, maar zegt wie er dan verliest.
Dat het in de data meestal de fondsbeleggers zijn, is een empirisch feit en geen
stelling.
:::

:::{exercise}
:label: ex-industrie-2

**Berk en Green met kwadratische kosten.** Neem $C(q) = b q^2$ met $b = 0{,}005$ per
miljard, $f = 1\%$, een prior $\phi_0 = 3\%$ met standaarddeviatie $\eta = 1\%$, en
ruis met $\sigma = 5\%$ per jaar.

1. Leid af dat $q_t = \phi_t^2/(4bf)$ en dat die oplossing alleen geldt als
   $\phi_t \geq 2f$.
2. Het fonds haalt in het eerste jaar $R_1 = 8\%$. Bereken $\phi_1$, de nieuwe omvang
   en de procentuele instroom.
3. Wat is het verwachte rendement voor de belegger in jaar 2, en waarom is dat niet
   in strijd met de instroom?
:::

:::{solution} ex-industrie-2
:class: dropdown

**(1)** Uit $C'(q_a) = 2bq_a = \phi_t$ volgt $q_a = \phi_t/(2b)$. De bindende
voorwaarde van de belegger geeft $f q_t = \phi_t q_a - b q_a^2 = \phi_t^2/(2b) -
\phi_t^2/(4b) = \phi_t^2/(4b)$. De indexpositie $q_t - q_a = \phi_t(\phi_t - 2f)/(4bf)$
is niet negatief als en slechts als $\phi_t \geq 2f$.

**(2)** Met $\gamma = 1/0{,}01^2 = 10\,000$ en $\omega = 1/0{,}05^2 = 400$ is
$\phi_1 = (10\,000 \times 0{,}03 + 400 \times 0{,}08)/10\,400 = 3{,}19\%$.

```{code-cell} ipython3
b_bg, f_bg, phi0, eta, sigma, R1 = 0.005, 0.01, 0.03, 0.01, 0.05, 0.08
gamma_p, omega_p = 1 / eta**2, 1 / sigma**2
phi1 = (gamma_p * phi0 + omega_p * R1) / (gamma_p + omega_p)
q0, q1 = phi0**2 / (4 * b_bg * f_bg), phi1**2 / (4 * b_bg * f_bg)
print(f"phi_1 = {phi1:.4%}, q_0 = {q0:.3f} mld, q_1 = {q1:.3f} mld, instroom = {q1 / q0 - 1:.1%}")
```

**(3)** Het verwachte rendement is nul, omdat de instroom de omvang precies zo zet
dat $\E_1[r_2] = 0$. Een rendement van vijf procentpunt boven de verwachting verhoogt
de geschatte vaardigheid met 0,19 procentpunt, en het fonds groeit van 4,5 naar 5,1
miljard dollar. Daarna is het fonds weer gewoon. Geld dat rendementen najaagt, kan dus rationeel zijn en toch
niets opleveren.
:::

:::{exercise}
:label: ex-industrie-3

**Onterechte ontdekkingen in de echte fondsen.** Gebruik de Carhart-$t$-waarden van
de 50 actieve fondsen uit de replicatie.

1. Schat $\hat\pi_0$, $\hat\pi_A^-$ en $\hat\pi_A^+$ met $\lambda = 0{,}5$ en
   $\gamma = 0{,}2$.
2. Hoeveel fondsen verwerpt Benjamini-Hochberg met $q = 10\%$ als "vaardig", met
   eenzijdige p-waarden?
3. Bereken met de simulatie voor veertig jaar de standaardfout van $\hat\pi_A^+$ bij
   2000 fondsen, en schaal die naar 50 fondsen. Wat valt er dan uit (1) te
   concluderen?
:::

:::{solution} ex-industrie-3
:class: dropdown

```{code-cell} ipython3
df_real = len(sample) - 5
pi0_r, pim_r, pip_r = fdr_proportions(t_real, df=df_real)
bh_real = benjamini_hochberg(stats.t.sf(t_real, df_real), q=0.10)
se_2000 = pi_plus_draws[480].std(ddof=1)
print(f"pi0 = {pi0_r:.2f}, pi- = {pim_r:.2f}, pi+ = {pip_r:.2f}")
print(f"BH-ontdekkingen (q = 10%): {bh_real.sum()} van {len(t_real)}")
print(f"SE pi+ bij 2000 fondsen (40 jaar): {se_2000:.3f}; "
      f"geschaald naar {len(t_real)} fondsen: {se_2000 * np.sqrt(2000 / len(t_real)):.3f}")
```

Op de overlevenden geeft de schatter $\hat\pi_0 = 0{,}60$ en $\hat\pi_A^+ = 0{,}18$,
maar Benjamini-Hochberg vindt geen enkel vaardig fonds. De standaardfout van
$\hat\pi_A^+$ is bij 50 fondsen ongeveer $0{,}05$, zes keer zo groot als bij 2000
fondsen, en de steekproef is bovendien op succes geselecteerd. Een geschat aandeel
vaardige fondsen betekent daarom alleen iets in een groot universum zonder
survivorship bias, en juist die data ontbreken hier.
:::
