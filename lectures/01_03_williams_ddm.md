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

(01-03-williams-ddm)=

# Williams en het dividend discount model

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1938–1959.

**Wat we al weten.** Uit [](#01-02-bachelier) komt een beschrijving van koersen
waarin prijsveranderingen vrijwel onvoorspelbaar zijn en hun spreiding met
$\sqrt{t}$ groeit. Cowles liet zien dat beleggingsadviseurs de markt niet
verslaan, en Kendall vond dat de samenhang tussen opeenvolgende koersveranderingen
te zwak is om mee te voorspellen. Al die uitspraken gaan over *veranderingen*,
zodat er wel een theorie van de ruis bestond, maar geen theorie van het koersniveau.

**Welke vraag staat open.** Wat is een aandeel waard? Welke grootheid maakt van
een koers meer dan een getal waarover mensen het toevallig eens zijn?
```

## Overzicht

Wat is een aandeel waard? Volgens Williams, in 1938, is dat de contante waarde van
alle dividenden die het ooit uitkeert, verdisconteerd tegen een vaste
discontovoet. In die vorm houdt het antwoord geen stand, want in de data beweegt
niet de verwachting van de dividenden maar de discontovoet. In dit college:

- leiden we uit de definitie van rendement een *boekhoudkundige identiteit* af.
  Die kan niet fout zijn, net zo min als "bezit is schuld plus eigen vermogen";
- voegen we de aanname van Williams toe, een constante discontovoet $r$. Dat
  *model van Williams* kan wel fout zijn;
- werken we het uit tot het Gordon-groeimodel $p = d_1/(r-g)$, en laten we met de
  PVGO zien wanneer groei waarde toevoegt;
- simuleren we hoe breed een waardering uitvalt als $g$ uit historische data
  wordt geschat;
- toetsen we op Shillers data waar het model toetsbaar is: bij constante $r$ moet
  op een hoge prijs-dividend-ratio snelle dividendgroei volgen.

In 1938 publiceerde John Burr Williams *The Theory of Investment Value*
{cite}`Williams1938`, een proefschrift dat hij bij Schumpeter in Harvard
verdedigde. De kern past in één zin, namelijk dat een investering de contante
waarde waard is van de uitkeringen die ze ooit zal doen. In de praktijk
vermenigvuldigde men de winst toen met een getal dat uit gewoonte was ontstaan.
Williams verving dat getal door een som, zodat wie het oneens was voortaan moest
zeggen *waarover*. Gordon en Shapiro brachten het idee in de jaren vijftig met een
gesloten formule de praktijk in {cite}`GordonShapiro1956,Gordon1959`. Omdat een
prijs met Williams voor het eerst uit een model volgt en niet uit een gewoonte,
begint de moderne waarderingstheorie bij hem.

## Intuïtie: waarom zou dit waar zijn?

Een aandeel is een stuk papier dat geen nut geeft, niet stukgaat en waar niemand
in kan wonen. Het keert alleen af en toe geld uit. Alles wat een aandeel waard is,
moet dus uit die uitkeringen komen, of uit de prijs waarvoor de eigenaar het later
verkoopt.

Maar de koper van later staat voor dezelfde vraag, want ook hij kan alleen rekenen
op uitkeringen en op een nóg latere verkoopprijs. Als we die redenering doortrekken,
schuift de verkoopprijs steeds verder de toekomst in, tot hij verdwijnt en alleen
de stroom dividenden overblijft.

De kracht van die gedachte zit in wat ze *uitsluit*. Een aandeel ontleent geen
waarde aan het feit dat anderen het willen hebben, en een koers is niet hoog omdat
hij de laatste jaren hoog was. Williams gebruikte zelf het beeld van een
boomgaard, die de appels waard is die eraan komen, zodat wat een ander ooit voor
die boomgaard betaalde, er in zijn redenering niet toe doet.

Om er een getal van te maken, zijn twee dingen nodig: een verwachting over de
dividenden en een tarief dat een euro van volgend jaar omrekent naar een euro van
vandaag. Dat tarief heet de *discontovoet*. Williams werkte de dividenden in
honderden bladzijden uit, met tabellen die hij met de hand uitrekende, maar de
discontovoet nam hij in zijn waarderingen als gegeven. Een theorie
die zegt welk tarief bij welk risico hoort, kwam pas een kwarteeuw later, met het
CAPM.

Zonder zo'n theorie zegt de som op zichzelf weinig, want uit dividendverwachtingen
en discontovoet volgt de prijs, maar uit prijs en dividendverwachtingen volgt net
zo goed de discontovoet. Pas zodra de discontovoet vastligt, doet de gedachte een
voorspelling. Een aandeel kan dan alleen duur zijn ten opzichte van zijn dividend
omdat de markt snelle dividendgroei verwacht.

We verwachten dus dat op een hoge prijs-dividend-ratio (de prijs gedeeld door het
dividend) snel stijgende dividenden volgen. De theorie leidt die voorspelling af,
en de replicatie toetst ze op Shillers data.

## Toy-voorbeeld: drie jaar dividenden, met de hand verdisconteerd

Het kleinste voorbeeld van Williams' som is één aandeel met twee groeifasen. Voordat
we gaan rekenen, laden we de pakketten die het hele college gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** Een bedrijf heeft zojuist een dividend van $d_0 = 1{,}00$ per aandeel
uitgekeerd. De discontovoet is $r = 10\%$.

| periode | groei van het dividend | discontovoet |
|---|---|---|
| jaar 1 tot en met 3 | 10% per jaar | 10% |
| vanaf jaar 4, voor altijd | 5% per jaar | 10% |

**Het recept.** De prijs is de som van de verdisconteerde dividenden. Voor het
deel dat voor altijd met $g$ groeit, gebruiken we één formule die de theorie
straks afleidt, namelijk dat een stroom die volgend jaar $d$ uitkeert en daarna
met $g$ groeit, vandaag $d/(r-g)$ waard is.

**Stap 1.** De eerste drie dividenden zijn $d_1 = 1{,}10$, $d_2 = 1{,}21$ en
$d_3 = 1{,}331$.

**Stap 2.** Verdisconteren gaat per jaar met een factor $1{,}10$. Omdat de groei in
deze fase gelijk is aan de discontovoet, is elke term één:
$1{,}10/1{,}10 = 1{,}21/1{,}21 = 1{,}331/1{,}331 = 1{,}00$. Samen zijn de eerste
drie dividenden $3{,}00$ waard.

**Stap 3.** Vanaf jaar 4 groeit het dividend met 5%, te beginnen bij
$d_4 = 1{,}331 \times 1{,}05 = 1{,}39755$.

**Stap 4.** Volgens het recept is die stroom op $t=3$ waard
$d_4/(r-g) = 1{,}39755/0{,}05 = 27{,}951$. Die waarde heet de *eindwaarde*, de
verwachte verkoopprijs van het aandeel op $t=3$.

**Stap 5.** Terugrekenen naar vandaag met $1{,}10^3 = 1{,}331$ geeft
$27{,}951/1{,}331 = 21{,}00$. Die deling gaat precies op, want $1{,}331 \times 21 = 27{,}951$.

**Stap 6.** De prijs is $p_0 = 3{,}00 + 21{,}00 = 24{,}00$, en de
prijs-dividend-ratio is $\mathrm{PD}_0 = 24{,}00/1{,}00 = 24$.

In Python lopen we dezelfde zes stappen door en zetten we de handberekening
ernaast.

```{code-cell} ipython3
d0, r, g_early, g_late, n = 1.00, 0.10, 0.10, 0.05, 3

years = np.arange(1, n + 1)
dividends = d0 * (1 + g_early) ** years          # d_1, d_2, d_3
discounted = dividends / (1 + r) ** years       # contante waarde per jaar

d_next = dividends[-1] * (1 + g_late)           # d_4
terminal = d_next / (r - g_late)                # eindwaarde op t = 3 (het recept)
terminal_pv = terminal / (1 + r) ** n           # eindwaarde teruggerekend naar t = 0
price = discounted.sum() + terminal_pv

hand = pd.Series({
    "d_1": 1.10, "d_2": 1.21, "d_3": 1.331,
    "contante waarde d_1 t/m d_3": 3.00,
    "d_4": 1.39755,
    "eindwaarde op t=3": 27.951,
    "eindwaarde op t=0": 21.00,
    "prijs p_0": 24.00,
    "aandeel eindwaarde": 0.875,
})
code = pd.Series({
    "d_1": dividends[0], "d_2": dividends[1], "d_3": dividends[2],
    "contante waarde d_1 t/m d_3": discounted.sum(),
    "d_4": d_next,
    "eindwaarde op t=3": terminal,
    "eindwaarde op t=0": terminal_pv,
    "prijs p_0": price,
    "aandeel eindwaarde": terminal_pv / price,
})
pd.DataFrame({"met de hand": hand, "code": code}).round(5)
```

Omdat de twee kolommen gelijk zijn, doet de code wat de handberekening doet. Van
de prijs van $24{,}00$ komt $21{,}00$, ofwel 87,5%, uit alles na jaar 3.

De prijs komt dus vooral uit de eindwaarde, en die eindwaarde ontstaat door te
delen door een klein getal, $r - g = 5$ procentpunt. Een waardering is daardoor
vooral een uitspraak over een verre toekomst waarover niemand iets weet.

## Theorie

De afleiding begint bij de boekhoudkundige identiteit, die uit de definitie van
rendement volgt, en maakt daar met één aanname, een constante discontovoet, het
model van Williams van. De transversaliteitsvoorwaarde maakt van dat model een
oneindige som, en die som is de kern van dit college. Daarna volgen het
Gordon-model, de gesloten vorm die het toy-voorbeeld als recept gebruikte, en de
PVGO, die zegt wanneer groei waarde toevoegt. Ten slotte laten we zien dat het
model pas in de prijs-dividend-ratio toetsbaar wordt.

### Opzet en aannames

We leggen eerst vast wat een rendement is en welke aanname Williams daaraan
toevoegt. Er is één aandeel dat op elk tijdstip $t$ een dividend $d_t \ge 0$
uitkeert, en de prijs $p_t$ is eindig. De prijs is *ex dividend*, zodat een koper
die op $t$ voor $p_t$ koopt, $d_{t+1}$ krijgt en niet $d_t$. Het bruto rendement
van $t$ naar $t+1$ is dan

```{math}
:label: eq-williams-ddm-rendement
R_{t+1} = \frac{p_{t+1} + d_{t+1}}{p_t}.
```

Het rendement is dus wat de koper morgen terugkrijgt, dividend plus
verkoopprijs, gedeeld door wat hij vandaag betaalde. Omdat dat een definitie is en
geen aanname, kan de vergelijking niet fout zijn.

Williams neemt aan dat er een getal $r$ bestaat zodat voor elke periode
$\E_t[R_{t+1}] = 1 + r$, met $\E_t$ de verwachting op grond van wat op $t$ bekend
is. Constant is alleen het *verwachte* rendement, niet het gerealiseerde. In dit
model is de discontovoet $r$ hetzelfde als het verwachte netto rendement, en we
noemen hem verder alleen de discontovoet.

Voor Amerikaanse aandelen is de discontovoet reëel ongeveer 6,8% per jaar als
gemiddeld logrendement in Shillers data, waarop de simulatie kalibreert, en ongeveer
8,4% als gewoon gemiddelde, dat een halve variantie hoger ligt (de simulatie rekent
beide uit). Het toy-voorbeeld rekent met het ronde getal 10%.

De notatie is die van [](#00-00-setup): $R = 1 + r$ is bruto, $r$ netto en simpel,
en $p_t$ en $d_t$ zijn niveaus in euro. Daarmee wijken we af van
[](#01-02-bachelier), waar kleine letters logs waren, omdat de som van Williams
bedragen optelt en geen logs. Logs komen pas in de replicatie terug, en daar
staat er steeds bij dat het om logs gaat.

### Van de definitie van rendement naar de contante waarde

De prijs van vandaag is de contante waarde van de dividenden tot een horizon $K$,
plus de verdisconteerde verkoopprijs op $K$. Dat volgt eerst uit de definitie van
rendement alleen, en daarna, met verwachte waarden, uit het model van Williams.

Een koper betaalt vandaag een prijs en krijgt daarvoor morgen een dividend en een
verkoopprijs, zodat zijn prijs van vandaag gelijk is aan de opbrengst van morgen,
gedeeld door het rendement. De koper van morgen doet hetzelfde met de opbrengst van
overmorgen. Zo schuift de verkoopprijs steeds verder weg, en blijven de dividenden
over. Hoe hoger de dividenden, hoe hoger de prijs, en hoe hoger het rendement
waarmee ze verdisconteerd worden, hoe lager de prijs.

**De boekhoudkundige identiteit.** We schrijven [](#eq-williams-ddm-rendement) als
$p_t = (d_{t+1} + p_{t+1})/R_{t+1}$ en vullen dezelfde gelijkheid in voor $p_{t+1}$,
$p_{t+2}$, enzovoort. Na $K$ stappen staat er

$$
p_t = \sum_{j=1}^{K} \frac{d_{t+j}}{R_{t+1} \cdots R_{t+j}}
      + \frac{p_{t+K}}{R_{t+1} \cdots R_{t+K}} .
$$

De prijs is dus de som van de dividenden tot $K$ en de verkoopprijs op $K$,
verdisconteerd met de rendementen die werkelijk worden behaald. Omdat de
identiteit niets aanneemt, kan geen enkele dataset ermee in strijd zijn, maar met het
model van Williams wel. Om dat onderscheid draait het hele
college, want de replicatie toetst het model en niet de identiteit.

**Het model van Williams.** We nemen de verwachting op $t$ van
[](#eq-williams-ddm-rendement) en gebruiken $\E_t[R_{t+1}] = 1+r$:

$$
p_t = \frac{\E_t\!\left[d_{t+1} + p_{t+1}\right]}{1+r}.
$$

De prijs is de verwachte opbrengst van morgen, één periode verdisconteerd. Omdat
deze vergelijking op elk tijdstip geldt, dus ook op $t+1$, substitueren we
$p_{t+1} = \E_{t+1}[d_{t+2} + p_{t+2}]/(1+r)$ en gebruiken we de wet van iteratieve
verwachtingen, $\E_t[\E_{t+1}[\cdot]] = \E_t[\cdot]$. Die wet zegt dat onze
verwachting van vandaag over wat we morgen zullen verwachten, gelijk is aan wat we
vandaag al verwachten. Na $K$ stappen volgt de eindige versie van het model:

```{math}
:label: eq-williams-ddm-eindig
p_t = \sum_{j=1}^{K} \frac{\E_t\!\left[d_{t+j}\right]}{(1+r)^{j}}
      + \frac{\E_t\!\left[p_{t+K}\right]}{(1+r)^{K}} .
```

Volgens deze vergelijking bestaat de prijs uit de contante waarde van de verwachte
dividenden tot $K$, plus de verdisconteerde verwachte verkoopprijs op $K$, de
eindwaarde. Het toy-voorbeeld is het geval $K = 3$, met $3{,}00$ aan dividenden en
$21{,}00$ aan verdisconteerde eindwaarde.

### Het kernresultaat: transversaliteit en het dividend discount model

Wat gebeurt er met de prijs als we de horizon $K$ naar oneindig laten gaan? Als de
verdisconteerde eindwaarde dan verdwijnt, is de prijs de som van alle verwachte
dividenden.

*Waarom zou dit waar zijn?* Een koper die een aandeel over $K$ jaar
doorverkoopt, betaalt vandaag ook voor de verdisconteerde eindwaarde. Groeit de
verwachte verkoopprijs trager dan $r$, zoals in het toy-voorbeeld met 5% tegen
10%, dan krimpt dat deel naarmate $K$ groeit, en blijven alleen de dividenden over.
De transversaliteitsvoorwaarde legt precies dat krimpen vast. Verwacht een koper
daarentegen dat de prijs zelf in het tempo $r$ blijft stijgen, dan krimpt het deel
niet, en betaalt hij meer dan de dividenden rechtvaardigen.

:::{prf:theorem} Dividend discount model
:label: thm-williams-ddm-ddm

Als $\E_t[R_{t+1}] = 1+r$ voor alle $t$ met $r > 0$, en als de
transversaliteitsvoorwaarde

```{math}
:label: eq-williams-ddm-transversaliteit
\lim_{K \to \infty} \frac{\E_t\!\left[p_{t+K}\right]}{(1+r)^{K}} = 0
```

geldt, dan is

```{math}
:label: eq-williams-ddm-ddm
p_t = \sum_{j=1}^{\infty} \frac{\E_t\!\left[d_{t+j}\right]}{(1+r)^{j}} .
```
:::

Volgens [](#eq-williams-ddm-transversaliteit) gaat de verdisconteerde eindwaarde in
de verre toekomst naar nul. Met die voorwaarde krijgt het model van Williams in
[](#eq-williams-ddm-ddm) zijn definitieve vorm, waarin de prijs de som is van alle
verwachte dividenden, elk verdisconteerd met $r$. De voorwaarde hoort bij het
model, terwijl we de identiteit alleen met een eindige horizon $K$ gebruiken,
zodat die niets aanneemt.

:::{prf:proof}
Neem in [](#eq-williams-ddm-eindig) de limiet $K \to \infty$. Omdat dividenden
niet-negatief zijn, zijn de partiële sommen niet-dalend, zodat de reeks convergeert
of naar $+\infty$ divergeert. De verdisconteerde eindwaarde gaat naar nul volgens
[](#eq-williams-ddm-transversaliteit). Omdat $p_t$ eindig is, convergeert de reeks
dan naar $p_t$. $\square$
:::

Wat gebeurt er als [](#eq-williams-ddm-transversaliteit) niet geldt? We noemen de
som [](#eq-williams-ddm-ddm) de *fundamentele waarde* $p^{f}_t$ en bekijken
$p_t = p^{f}_t + B_t$ met

$$
\E_t[B_{t+1}] = (1+r)\, B_t .
$$

Zo'n $B_t$ heet een *rationele bel* (*rational bubble*, een deel van de prijs dat
geen enkele uitkering vertegenwoordigt, maar toch de discontovoet als rendement
oplevert). Ook $p^f_t + B_t$ voldoet aan $p_t = \E_t[d_{t+1}+p_{t+1}]/(1+r)$,
want de bel groeit in verwachting met $1+r$ en betaalt zo zijn eigen rendement.
Er is niets irrationeels aan, want iedereen verdient wat hij eist. Alleen staat er
geen dividend tegenover de bel, en het aandeel van de bel in de prijs groeit
zonder grens. Bij $r = 10\%$
verdubbelt de bel in ruim zeven jaar ($\ln 2/\ln 1{,}10 = 7{,}3$), een dividend
dat met 5% groeit pas in veertien ($\ln 2/\ln 1{,}05 = 14{,}2$).

Williams liet de bel weg door hem niet te noemen, en dat is verdedigbaar, omdat
bij elke $B_0 > 0$ een andere prijs hoort die aan dezelfde vergelijking voldoet.
Zonder de voorwaarde legt het model de prijs dus niet vast, maar het weglaten van
de bel blijft een keuze.

Een belegger die in 1999 zei dat internetaandelen te duur waren, beweerde
eigenlijk dat er een $B_t$ in de prijs zat. Een belegger die ze juist goed
gewaardeerd vond, beweerde dat $\E_t[d_{t+j}]$ enorm was. Zonder verdere
aannames zijn die twee lezingen in de data niet van elkaar te onderscheiden.

### Wat het voorspelt: het Gordon-groeimodel

Groeit het dividend in verwachting met een vaste $g < r$, dan wordt de oneindige
som één breuk. Daarin staat het dividend van volgend jaar in de teller en het
verschil $r - g$ in de noemer.

In de praktijk is de oneindige som onbruikbaar zolang een analist voor elk
toekomstig jaar een apart getal moet verzinnen. Gordon en Shapiro vervingen al die
getallen door één, door aan te nemen dat het dividend elk jaar met hetzelfde
percentage $g$ groeit. De analist kiest dan nog maar twee getallen, $g$ en $r$, en
hoe dichter hij $g$ bij $r$ legt, hoe minder elk volgend dividend door het
verdisconteren wegvalt en hoe hoger de prijs die hij uitrekent.

:::{prf:proposition} Gordon-Shapiro
:label: prf-williams-ddm-gordon

Als $\E_t[d_{t+j}] = d_t (1+g)^{j}$ met $g < r$, dan geldt

```{math}
:label: eq-williams-ddm-gordon
p_t = \frac{d_t (1+g)}{r - g} = \frac{\E_t[d_{t+1}]}{r-g},
\qquad\text{equivalent}\qquad
r = \frac{\E_t[d_{t+1}]}{p_t} + g .
```
:::

In woorden: de prijs is het dividend van volgend jaar, gedeeld door het verschil
tussen discontovoet en groei, en dat is precies het recept uit het toy-voorbeeld.
De rechterkant zegt hetzelfde, maar dan omgeschreven naar $r$, namelijk dat het
verwachte rendement gelijk is aan het *dividendrendement* (dividend gedeeld door
prijs) plus de dividendgroei. Het bewijs berust erop dat bij constante groei elke
term in de som gelijk is aan de vorige maal $(1+g)/(1+r)$, en een meetkundige reeks
met die reden telt op tot de breuk.

:::{prf:proof}
:class: dropdown

Vul de groeiaanname in [](#eq-williams-ddm-ddm) in:

$$
p_t = \sum_{j=1}^{\infty} \frac{d_t (1+g)^j}{(1+r)^j}
    = d_t \sum_{j=1}^{\infty} q^{j}, \qquad q \equiv \frac{1+g}{1+r} .
$$

Voor $g<r$ is $0 < q < 1$ en is $\sum_{j\ge1} q^j = q/(1-q)$. Als we dat invullen,
volgt

$$
p_t = d_t \frac{(1+g)/(1+r)}{1 - (1+g)/(1+r)}
    = d_t \frac{1+g}{(1+r)-(1+g)} = \frac{d_t(1+g)}{r-g}. \qquad \square
$$
:::

De voorwaarde $g < r$ is geen randgeval, want groeit een dividend voor altijd
sneller dan de discontovoet, dan is de contante waarde oneindig. Geen bedrijf
groeit voor altijd sneller dan de economie waarin het werkt, zodat $g$ op lange
termijn begrensd is door de groei van het bruto binnenlands product. Een waardering met $g$
dicht bij $r$ negeert die grens.

**De gevoeligheid die alles bepaalt.** Neem de eindwaarde uit het toy-voorbeeld
als zelfstandig aandeel: $d_0 = 1{,}00$, groei $g = 5\%$ voor altijd en
$r = 10\%$. Dan is $p = 1{,}05/0{,}05 = 21{,}00$. In de tabel verschuift telkens
één parameter één procentpunt:

| verandering | berekening | PD | ten opzichte van 21 |
|---|---|---|---|
| geen ($r = 10\%$, $g = 5\%$) | $1{,}05/0{,}05$ | 21,00 | |
| $r = 9\%$ | $1{,}05/0{,}04$ | 26,25 | +25% |
| $g = 6\%$ | $1{,}06/0{,}04$ | 26,50 | +26,2% |
| $r = 11\%$ | $1{,}05/0{,}06$ | 17,50 | −16,7% |

Een lagere $r$ of een hogere $g$ maakt het aandeel duurder en een hogere $r$ maakt
het goedkoper, omdat de prijs vrijwel alleen afhangt van het *verschil* $r - g$, en
dat verschil is klein. Een fout van één procentpunt in $r$ of $g$ is daardoor een
fout van twintig procent in dat verschil, en de prijs is er ongeveer omgekeerd
evenredig mee. Waarderen met dit model komt dus neer op delen door een klein getal
dat niemand kent. Het rooster hieronder geeft de prijs voor alle negen combinaties
van $r$ en $g$.

```{code-cell} ipython3
def gordon(d0, r, g):
    """Gordon growth price of a claim on a dividend growing at g forever."""
    return d0 * (1 + g) / (r - g)


r_values = [0.09, 0.10, 0.11]
g_values = [0.04, 0.05, 0.06]
grid = pd.DataFrame(
    index=pd.Index(r_values, name="discontovoet r"),
    columns=pd.Index(g_values, name="groeivoet g"),
    dtype=float,
)
for r_val in r_values:
    for g_val in g_values:
        grid.loc[r_val, g_val] = gordon(1.00, r_val, g_val)

grid.round(2)
```

Langs de diagonaal, waar $r - g$ steeds 5 procentpunt is, verandert de prijs
nauwelijks, van 20,80 naar 21,20, terwijl hij daarbuiten van 14,86 tot 35,33
loopt. Het rooster bevat ook de getallen uit de tabel hierboven.

### PVGO: wat groei toevoegt en wat het kost

Groei verhoogt de prijs alleen als het bedrijf op ingehouden winst meer verdient
dan de discontovoet. Het Gordon-model neemt $g$ als gegeven, maar hier laten we
zien waar $g$ vandaan komt en waarom een hoge $g$ niet vanzelf een hoge prijs
betekent.

Een bedrijf dat al zijn winst uitkeert, groeit niet, en is met een winst per
aandeel $e_1$ volgend jaar evenveel waard als een eeuwigdurende obligatie, $e_1/r$.
Wil het groeien, dan moet het winst inhouden, en die euro's gaan niet naar de
aandeelhouder. Verdient het bedrijf op een ingehouden euro meer dan de
discontovoet, dan stijgt de prijs door de groei. Verdient het minder, dan daalt de
prijs juist.

Schrijf $e_{t+1}$ voor de winst per aandeel, $b$ voor het
*inhoudingspercentage* (*retention ratio*, het deel van de winst dat het bedrijf
niet uitkeert) en $\mathrm{ROE}$ voor het rendement op nieuw geïnvesteerd
vermogen. Houdt het bedrijf elk jaar hetzelfde deel $b$ in, verdient het
daarop steeds hetzelfde $\mathrm{ROE}$ en geeft het geen nieuwe aandelen uit, dan
is $d_{t+1} = (1-b)\,e_{t+1}$ en groeit de winst met $g = b \cdot \mathrm{ROE}$.
Invullen in [](#eq-williams-ddm-gordon) geeft

```{math}
:label: eq-williams-ddm-pvgo
p_t = \frac{(1-b)\,e_{t+1}}{r - b\cdot\mathrm{ROE}}
    = \underbrace{\frac{e_{t+1}}{r}}_{\text{geen groei}} + \mathrm{PVGO}.
```

De prijs bestaat dus uit de waarde zonder groei plus de waarde van wat het bedrijf
met ingehouden winst nog gaat doen. Dat tweede deel heet $\mathrm{PVGO}$
(*present value of growth opportunities*, de contante waarde van de
groeimogelijkheden). Als we de waarde zonder groei aftrekken en alles op één
noemer brengen, krijgen we

$$
\mathrm{PVGO}
= \frac{(1-b)\,e_{t+1}}{r - b\cdot\mathrm{ROE}} - \frac{e_{t+1}}{r}
= \frac{b\,e_{t+1}}{r}\cdot\frac{\mathrm{ROE}-r}{r - b\cdot\mathrm{ROE}} .
$$

Het teken van $\mathrm{PVGO}$ is dus het teken van $\mathrm{ROE} - r$. Een bedrijf
dat investeert tegen minder dan de discontovoet, *vernietigt* waarde door te
groeien, hoe hard het ook groeit. Neem als voorbeeld $e_1 = 3$, $r = 10\%$,
$\mathrm{ROE} = 15\%$ en $b = 1/3$. Dan is $g = 5\%$, $d_1 = 2$ en
$p = 2/0{,}05 = 40$, tegen $e_1/r = 30$ zonder groei: $\mathrm{PVGO} = 10$. Bij
$\mathrm{ROE} = 8\%$ is $g = 2{,}67\%$ en $p = 2/0{,}0733 = 27{,}27$, dus
$\mathrm{PVGO} = -2{,}73$.

```{code-cell} ipython3
e1, r_pvgo, b = 3.00, 0.10, 1 / 3
no_growth = e1 / r_pvgo                          # waarde zonder groei, e_1/r

pvgo_code = {}
for roe in (0.15, 0.08):
    g_impl = b * roe
    d1 = (1 - b) * e1
    p_pvgo = d1 / (r_pvgo - g_impl)
    pvgo_code[roe] = [g_impl, d1, p_pvgo, no_growth, p_pvgo - no_growth]

labels = ["g = b ROE", "d_1 = (1-b) e_1", "prijs", "waarde zonder groei", "PVGO"]
pd.DataFrame(
    {
        "ROE 15%, met de hand": [0.05, 2.00, 40.00, 30.00, 10.00],
        "ROE 15%, code": pvgo_code[0.15],
        "ROE 8%, met de hand": [0.0267, 2.00, 27.27, 30.00, -2.73],
        "ROE 8%, code": pvgo_code[0.08],
    },
    index=labels,
).round(4)
```

Hand en code komen op twee decimalen overeen. Bij een $\mathrm{ROE}$ van 15% zit
een kwart van de prijs in wat het bedrijf nog gaat doen, terwijl hetzelfde bedrijf
bij 8% dezelfde groei-inspanning levert en de aandeelhouder er slechter van wordt.

### Hoe het getoetst wordt: de prijs-dividend-ratio

Het model wordt toetsbaar in de prijs-dividend-ratio, omdat bij constante $r$ op
een hoge ratio snelle dividendgroei moet volgen. Om dat te zien, delen we
[](#eq-williams-ddm-ddm) door $d_t$:

```{math}
:label: eq-williams-ddm-pd
\mathrm{PD}_t = \frac{p_t}{d_t}
  = \sum_{j=1}^{\infty} \frac{\E_t\!\left[d_{t+j}/d_t\right]}{(1+r)^{j}} .
```

De prijs-dividend-ratio is dus de verwachte groei van het dividend over
alle toekomstige jaren, verdisconteerd met $r$. Links staat een grootheid die we
*observeren* en die enorm beweegt, in Shillers decemberreeks van 9,9 in 1917 tot
86,2 in 2025 (de replicatie berekent beide). Rechts staan de verwachte
dividendgroei en de discontovoet, twee grootheden die we niet observeren.

Een belegger betaalt veel per euro dividend alleen
als hij verwacht dat dat dividend hard gaat groeien, of als hij genoegen neemt met
een laag rendement. Ligt $r$ vast, dan valt de tweede reden weg, zodat op een
hoge ratio snelle dividendgroei moet volgen, precies wat we aan het begin van het
college verwachtten.

Die uitspraak is *falsifieerbaar*, en de replicatie toetst ze. Wat er moet gelden
als de dividendgroei uitblijft, volgt uit de boekhoudkundige identiteit. Daarvoor
delen we de identiteit door $d_t$ en schrijven we
$p_{t+K}/d_t = \mathrm{PD}_{t+K}\, d_{t+K}/d_t$:

$$
\mathrm{PD}_t = \sum_{j=1}^{K} \frac{d_{t+j}/d_t}{R_{t+1} \cdots R_{t+j}}
      + \frac{(d_{t+K}/d_t)\,\mathrm{PD}_{t+K}}{R_{t+1} \cdots R_{t+K}} .
$$

Op een hoge prijs-dividend-ratio volgt dus snelle dividendgroei, of volgen lage
rendementen, of blijft de ratio over $K$ jaar hoog, want de groei staat in de
tellers en de rendementen in de noemers. Omdat de identiteit geldt voor elk pad
dat werkelijk komt, geldt ze ook gemiddeld. Komt de groei niet, dan zijn de
rendementen voorspelbaar laag, en is de discontovoet geen constante maar een
tijdreeks. Blijft de ratio voor altijd hoog, dan zit er een bel in de prijs.

Campbell en Shiller {cite}`CampbellShiller1988` maakten hiervan een
variantiedecompositie, die meet welk deel van de schommelingen in de
log-prijs-dividend-ratio uit verwachte dividendgroei komt en welk deel uit
verwachte rendementen. De afleiding volgt in [](#04-20-voorspelbaarheid).

```{admonition} Samengevat
:class: tip

- De boekhoudkundige identiteit volgt uit de definitie van rendement en kan niet
  worden verworpen. Het model van Williams voegt een constante discontovoet toe.
  Met de transversaliteitsvoorwaarde is de prijs de contante waarde van de
  verwachte dividenden, [](#eq-williams-ddm-ddm).

- Bij constante groei is de prijs $\E_t[d_{t+1}]/(r-g)$,
  [](#eq-williams-ddm-gordon). Een hogere $g$ of een lagere $r$ maakt het aandeel
  duurder, omdat verre dividenden minder wegvallen door verdisconteren. Een lagere
  $g$ of hogere $r$ maakt het goedkoper. Het effect is sterk zodra $r - g$ klein is.

- Groei voegt alleen waarde toe als $\mathrm{ROE} > r$, [](#eq-williams-ddm-pvgo).
  Een hoger inhoudingspercentage $b$ verhoogt dan de prijs, omdat elke ingehouden
  euro meer oplevert dan de discontovoet. Bij $\mathrm{ROE} < r$ verlaagt het de
  prijs, om de omgekeerde reden.

- Een hoge prijs-dividend-ratio betekent hoge verwachte dividendgroei of een lage
  discontovoet, een lage ratio het omgekeerde, [](#eq-williams-ddm-pd). Bij
  constante $r$ blijft alleen de dividendgroei over.

- De simulatie hierna gaat na hoe breed de waardering uitvalt als $g$ uit een
  steekproef van $T$ jaar wordt geschat.
```

## Simulatie: hoe de schatting van $g$ de waardering overneemt

Zelfs in een wereld waarin het Gordon-model exact klopt, valt een waardering met
een geschatte $g$ veel breder uit dan de standaardfout van die schatting doet
vermoeden. In die wereld groeien dividenden in verwachting met een vaste $g$ en is
de discontovoet $r$ bekend. Er is dus één ware prijs-dividend-ratio, en we meten
hoe breed de verdeling van de waardering is als een analist $g$ schat uit $T$ jaar
data.

Die breedte is van belang voor het hoofdargument, want een onderzoeker die vindt
dat de prijs-dividend-ratio niet bij de dividenden past, moet eerst weten hoeveel
ruis er al zit in een waardering waarin alleen $g$ onbekend is. Hier komt de
standaardfout van 2% terug, want bij een volatiliteit van 20% per jaar is het
gemiddelde van een eeuw jaarrendementen maar op $20/\sqrt{100} = 2$ procentpunt
nauwkeurig, zoals [](#00-01-rendementen) afleidde. Voor de dividendgroei hieronder
is die standaardfout 0,93 procentpunt, en de simulatie laat zien wat zo'n
onnauwkeurigheid doet zodra ze in de kleine noemer $r - g$ terechtkomt.

We kalibreren op Shillers jaarreeks en berekenen daarvoor het gemiddelde, de
standaarddeviatie en de standaardfout van de reële log-dividendgroei en het reële
log-rendement.

```{code-cell} ipython3
shiller_raw = hap_data.shiller()
annual = shiller_raw[shiller_raw.index.month == 12]

log_dgrowth = np.log(annual["real_dividend"]).diff().dropna()
log_return = np.log(annual["real_total_return_price"]).diff().dropna()

calibration = pd.DataFrame(
    {
        "gemiddelde": [log_dgrowth.mean(), log_return.mean()],
        "standaarddeviatie": [log_dgrowth.std(ddof=1), log_return.std(ddof=1)],
        "standaardfout gemiddelde": [
            log_dgrowth.std(ddof=1) / np.sqrt(len(log_dgrowth)),
            log_return.std(ddof=1) / np.sqrt(len(log_return)),
        ],
        "n": [len(log_dgrowth), len(log_return)],
    },
    index=["reële dividendgroei (log)", "reëel totaalrendement (log)"],
).round(4)

calibration
```

Over 154 jaarwaarnemingen groeit het reële dividend gemiddeld 1,61% per jaar,
met een standaarddeviatie van 11,5% en een standaardfout van 0,93 procentpunt.
Het gemiddelde reële logrendement is 6,82% (standaardfout 1,42 procentpunt), en
dat getal nemen we als $r$. Omdat $r$ in de simulatie bekend is, onderschat ze de
werkelijke onzekerheid van een analist.

In het ware model geldt dus Gordon met $g = 1{,}61\%$ en $r = 6{,}82\%$. Het verschil
$r - g$ is 5,2 procentpunt, bijna de 5 procentpunt van het toy-voorbeeld. De ware
prijs-dividend-ratio is $(1+g)/(r-g) = 1{,}0161/0{,}0521 \approx 19{,}5$.

Strikt genomen vraagt de Gordon-formule gewone gemiddelden, die een halve
variantie boven de log-gemiddelden liggen: $1{,}61 + 11{,}5^2/200 \approx 2{,}3\%$
voor $g$ en $6{,}82 + 17{,}6^2/200 \approx 8{,}4\%$ voor $r$. De ware ratio wordt
dan ongeveer 17, maar voor de breedte van de verdeling maakt dat weinig uit.

Een analist ziet $T$ jaar dividendgroei, schat $\hat g$ als het
steekproefgemiddelde en vult dat met de juiste $r$ in het Gordon-model in. We
laten dat 20 000 analisten doen, voor $T$ gelijk aan 20, 50 en 100 jaar.

```{code-cell} ipython3
g_true, sigma_g, r_true = 0.0161, 0.115, 0.0682
n_sim = 20_000

pd_true = (1 + g_true) / (r_true - g_true)
rows = []
pd_hat_by_T = {}                                 # bewaard voor de figuur
for T in (20, 50, 100):
    growth = rng.normal(g_true, sigma_g, size=(n_sim, T))
    g_hat = growth.mean(axis=1)
    finite = g_hat < r_true                      # anders: oneindige prijs
    pd_hat = np.where(finite, (1 + g_hat) / (r_true - g_hat), np.nan)
    pd_hat_by_T[T] = pd_hat
    rows.append(
        {
            "T (jaren)": T,
            "standaardfout geschatte g": sigma_g / np.sqrt(T),
            "PD 5e percentiel": np.nanpercentile(pd_hat, 5),
            "PD mediaan": np.nanpercentile(pd_hat, 50),
            "PD 95e percentiel": np.nanpercentile(pd_hat, 95),
            "aandeel geschatte g > r": 1 - finite.mean(),
        }
    )

print(f"ware prijs-dividend-ratio: {pd_true:.2f}")
pd.DataFrame(rows).set_index("T (jaren)").round(4)
```

De waardering valt veel breder uit dan de standaardfout van $\hat g$ doet
vermoeden. Bij $T = 50$ is die standaardfout 1,6 procentpunt, een keurig getal.
Toch loopt het interval tussen het 5e en het 95e percentiel van 12,5 tot 40,8,
rond een waarheid van 19,5. Een analist die niets fout doet, zit er dan naar
boven tot een factor twee naast ($40{,}8/19{,}5 = 2{,}1$). Met een eeuw data
loopt het interval nog van 14,1 tot 30,8.

De verdeling is ook scheef, omdat $1/(r-g)$ convex is in $g$. Bij $T = 50$ ligt
het 5e percentiel 36% onder de waarheid en het 95e percentiel 109% erboven, zodat
de fout naar boven ongeveer drie keer zo groot is. In een klein deel van de
steekproeven komt $\hat g$ zelfs boven $r$ uit (de laatste kolom). De prijs is
dan oneindig, een teken dat het model buiten zijn geldigheidsgebied wordt gebruikt.

De figuur zet de verdeling bij $T = 50$, dezelfde 20 000 steekproeven als in de
tabel, naast de hyperbool die de vorm ervan verklaart. Links gaat het om de lange
staart naar rechts, en rechts om hoe steil de hyperbool wordt vlak voor $g = r$.
Het rechterpaneel toont drie waarden van $r$, en omdat de asymptoot met $r$
meeschuift, doet een onzekere $r$ hetzelfde als een onzekere $g$.

```{code-cell} ipython3
:label: cel-williams-ddm-verdeling
:tags: [hide-input]

T_plot = 50
pd_hat = pd_hat_by_T[T_plot]                     # dezelfde steekproeven als in de tabel

fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))

axes[0].hist(pd_hat[np.isfinite(pd_hat) & (pd_hat < 120)], bins=60, edgecolor="white")
axes[0].axvline(pd_true, color="black", lw=1.4)
axes[0].set_xlabel("Geïmpliceerde prijs-dividend-ratio")
axes[0].set_ylabel("Aantal steekproeven")
axes[0].set_title(f"Waardering uit $\\hat g$ over {T_plot} jaar")

g_grid = np.linspace(-0.02, 0.06, 400)
for r_val, label in [(0.06, "$r = 6\\%$"), (0.0682, "$r = 6{,}82\\%$"), (0.08, "$r = 8\\%$")]:
    visible = g_grid < r_val - 0.002
    ratio = np.full_like(g_grid, np.nan)
    ratio[visible] = (1 + g_grid[visible]) / (r_val - g_grid[visible])
    axes[1].plot(g_grid * 100, ratio, lw=1.6, label=label)
axes[1].axvline(g_true * 100, color="black", lw=1.0, ls="--")
axes[1].set_ylim(0, 120)
axes[1].set_xlabel("Groeivoet $g$ (procent per jaar)")
axes[1].set_ylabel("Prijs-dividend-ratio")
axes[1].set_title("De hyperbool $ (1+g)/(r-g) $")
axes[1].legend()

plt.show()
```

:::{figure} #cel-williams-ddm-verdeling
:label: fig-williams-ddm-verdeling
:width: 100%

Links staat de verdeling van de prijs-dividend-ratio die volgt uit een op vijftig
jaar geschatte groeivoet, met de ware waarde als verticale lijn. De verdeling is
scheef naar rechts. Rechts staat de verklaring, want de prijs-dividend-ratio is een
hyperbool in $g$ met een verticale asymptoot op $g = r$. De gestreepte lijn is de
ware groeivoet. Ver van de asymptoot is de hyperbool vlak en doet een kleine
schattingsfout weinig, vlak ervoor schiet hij omhoog.
:::

De simulatie hield $r$ vast en liet $g$ onzeker. In de replicatie gaat het om het
omgekeerde, want daar is de vraag of $r$ zelf beweegt.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** John Burr Williams, *The Theory of Investment Value*, Harvard
University Press 1938 {cite}`Williams1938`, in de gesloten vorm van Gordon en
Shapiro, Management Science 1956 {cite}`GordonShapiro1956`.

**Wat.** Het boek bevat geen tijdreekstoets die we kunnen herhalen. We toetsen de empirische inhoud
van [](#eq-williams-ddm-pd) onder constante $r$, met regressies van de reële
dividendgroei en het reële rendement over tien jaar op de log-prijs-dividend-ratio.

**Data hier.** Shillers maandreeks vanaf 1871 via `hap.data.shiller()`,
teruggebracht tot decemberwaarnemingen.

**Verschil met het origineel.** Williams rekende met de hand aan afzonderlijke
bedrijven, zonder index of tijdreeks. Gordons eigen toets {cite}`Gordon1959` is
een cross-sectie waarvan de data niet gratis zijn. Shillers dividendreeks negeert
inkoop van eigen aandelen, wat de gemeten $d_t$ na 1985 te laag maakt.

**Verwachte afwijking.** Volgens Williams volgt op een hoge ratio snelle
dividendgroei, dus een positieve, significante dividendcoëfficiënt met een grote
$R^2$ en een rendementscoëfficiënt van nul. Wij verwachten een dividendcoëfficiënt
die niet significant van nul verschilt, met een kleine $R^2$, en een negatieve,
significante rendementscoëfficiënt met een $R^2$ rond tien procent.
```

De eerste cel bouwt het panel met de log-prijs-dividend-ratio en de gemiddelde
jaarlijkse dividendgroei en rendementen over de tien jaar erna. Ze meldt ook de
uitersten van de prijs-dividend-ratio en de autocorrelatie van de regressor.

```{code-cell} ipython3
# real_price, real_dividend (voortschrijdend twaalfmaands dividend, gedefleerd) en
# real_total_return_price (cum-dividend reële totaalrendementsindex), december.
horizon = 10

pd_ratio = (annual["real_price"] / annual["real_dividend"]).rename("PD")
log_pd = np.log(pd_ratio).rename("log_pd")

future_growth = (
    np.log(annual["real_dividend"].shift(-horizon) / annual["real_dividend"]) / horizon
).rename("dividendgroei")
future_return = (
    np.log(
        annual["real_total_return_price"].shift(-horizon)
        / annual["real_total_return_price"]
    )
    / horizon
).rename("rendement")

panel = pd.concat([log_pd, future_growth, future_return], axis=1).dropna()
print(f"steekproef: {panel.index[0]:%Y} t/m {panel.index[-1]:%Y}, "
      f"{len(panel)} overlappende jaarwaarnemingen")
print(f"PD hele reeks: laagst {pd_ratio.min():.1f} ({pd_ratio.idxmin():%Y}), "
      f"hoogst {pd_ratio.max():.1f} ({pd_ratio.idxmax():%Y})")
print(f"autocorrelatie log PD in het panel: {panel['log_pd'].autocorr():.3f}")
panel.describe().round(4)
```

Het panel heeft 145 waarnemingen, van 1871 tot en met 2015. Twee opeenvolgende
tienjaarsperioden delen negen jaar, zodat hun residuen samenhangen. De regressies
gebruiken daarom Newey-West-standaardfouten (`hap.newey_west`), die voor zulke
samenhang corrigeren, met negen lags, één per gedeeld jaar. De helling is de
parameter van de regressor, `log_pd`.

```{code-cell} ipython3
fits = {
    column: hap.newey_west(panel[column], panel["log_pd"], lags=horizon - 1)
    for column in ("dividendgroei", "rendement")
}

results = pd.DataFrame(
    {
        "coëfficiënt": [fit.params["log_pd"] for fit in fits.values()],
        "standaardfout": [fit.bse["log_pd"] for fit in fits.values()],
        "t-waarde": [fit.tvalues["log_pd"] for fit in fits.values()],
        "R2": [fit.rsquared for fit in fits.values()],
    },
    index=["reële dividendgroei, 10 jaar vooruit", "reëel totaalrendement, 10 jaar vooruit"],
)
results.round(4)
```

De tabel laat zien dat de prijs-dividend-ratio het rendement voorspelt en de
dividendgroei niet. De figuur toont beide regressies als puntenwolk, en daarin
gaat het om het verschil in helling tussen het linker- en het rechterpaneel.

```{code-cell} ipython3
:label: cel-williams-ddm-scatter
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharex=True)

for ax, column, title in [
    (axes[0], "dividendgroei", "Reële dividendgroei"),
    (axes[1], "rendement", "Reëel totaalrendement"),
]:
    ax.scatter(panel["log_pd"], panel[column] * 100, s=14, alpha=0.6)
    slope, intercept = np.polyfit(panel["log_pd"], panel[column] * 100, 1)
    grid_x = np.linspace(panel["log_pd"].min(), panel["log_pd"].max(), 50)
    ax.plot(grid_x, intercept + slope * grid_x, color="black", lw=1.4)
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel("log prijs-dividend-ratio")
    ax.set_ylabel("Procent per jaar")
    ax.set_title(f"{title}, 10 jaar vooruit")

plt.show()
```

:::{figure} #cel-williams-ddm-scatter
:label: fig-williams-ddm-scatter
:width: 100%

Elk punt is één decemberwaarneming tussen 1871 en 2015. Links de gerealiseerde
reële dividendgroei over de volgende tien jaar, rechts het gerealiseerde reële
totaalrendement, beide tegen de log-prijs-dividend-ratio van dat moment. Links
stijgt de lijn zwak en niet significant, rechts daalt ze duidelijk. Als
Williams' aanname klopte, zouden de twee panelen andersom liggen.
:::

De figuur bevestigt de tabel. De rendementswolk helt naar beneden, terwijl de
dividendwolk nauwelijks helt.

Shiller werkte dezelfde gedachte uit tot een eigen maatstaf: de *cyclically
adjusted price-earnings ratio* (CAPE, de koers gedeeld door de gemiddelde reële
winst over tien jaar) {cite}`Shiller2000`. Winst is een betere noemer dan
dividend, omdat ze niet van het uitkeringsbeleid afhangt, en middelen over tien
jaar voorkomt dat één slecht jaar de noemer bepaalt. Herhalen we de
rendementsregressie met log CAPE als regressor, dan verwachten we dezelfde richting,
een negatieve helling, en een hogere $R^2$, omdat de noemer minder ruis bevat.

```{code-cell} ipython3
cape_panel = pd.concat(
    [np.log(annual["cape"]).rename("log_cape"), future_return], axis=1
).dropna()
fit_cape = hap.newey_west(cape_panel["rendement"], cape_panel["log_cape"], lags=horizon - 1)

pd.DataFrame(
    {
        "coëfficiënt": [fit_cape.params["log_cape"]],
        "t-waarde": [fit_cape.tvalues["log_cape"]],
        "R2": [fit_cape.rsquared],
        "n": [int(fit_cape.nobs)],
    },
    index=["log CAPE → reëel rendement, 10 jaar vooruit"],
).round(4)
```

Die verwachting komt uit, want de helling is negatief en de $R^2$ is twee keer zo
hoog. De steekproef begint pas in 1881, omdat CAPE tien jaar winst nodig heeft.
Toch bewijst het sterkere verband weinig, want CAPE is met kennis van de hele
reeks als voorspeller gekozen.

Wat betekent één log-punt? Het is het verschil tussen een prijs-dividend-ratio van
54 en een van 20 ($20 \times 2{,}72 \approx 54$). De identiteit in logs zegt waar dat
log-punt
heen moet. Bij benadering is de log-ratio van vandaag de som van tien jaar
log-dividendgroei, min de som van tien jaar log-rendementen, plus de log-ratio
over tien jaar. Regresseren we elk van die drie op de log-ratio van vandaag, dan
tellen de hellingen op tot ongeveer één. De tabel rekent de jaarhellingen om naar
tien jaar.

| deel van het log-punt | berekening | log-punt |
|---|---|---|
| snellere dividendgroei | $10 \times 0{,}015$ | 0,15 |
| lager rendement | $10 \times 0{,}0375$ | 0,38 |
| hogere ratio over tien jaar (rest) | $1 - 0{,}15 - 0{,}38$ | 0,47 |
| totaal | | 1 |

Het rendement verklaart ruim twee keer zoveel als de dividendgroei, en de ratio
blijft lang hoog. De optelling is bij benadering, want de exacte log-vorm van Campbell
en Shiller weegt latere jaren met een factor iets onder één en bevat een kleine
term voor het dividendrendement. De 0,47 is dus een orde van grootte.

```{warning}
De 145 overlappende waarnemingen zijn samen ongeveer veertien onafhankelijke
tienjaarsperioden. Newey-West corrigeert daar in eindige steekproeven maar
gedeeltelijk voor.

Bovendien is de regressor sterk persistent, met een autocorrelatie van de
log-prijs-dividend-ratio in het panel van 0,89. In een korte steekproef wordt die
persistentie te laag geschat, bij 145 jaren gemiddeld met ongeveer
$(1 + 3 \times 0{,}89)/145 \approx 0{,}025$. Een onverwachte koersstijging verhoogt
tegelijk de ratio en het rendement van dat jaar, zodat de schokken in regressor en
rendement bijna één op één samen bewegen. Via die samenhang lekt de te lage
persistentie in de helling, zodat de rendementshelling van een jaarregressie
ongeveer evenveel negatiever uitvalt dan de ware (de Stambaugh-bias
{cite}`Stambaugh1999`). Die vertekening is van dezelfde orde als de geschatte
helling zelf, zodat deze $t$-waarden een aanwijzing voor de richting zijn, geen
bewijs.
```

De laatste cel zet de uitkomst voor de prijs-dividend-ratio naast wat er volgens
Williams' lezing zou moeten gelden en wat we vooraf verwachtten.

```{code-cell} ipython3
growth_fit, return_fit = results.iloc[0], results.iloc[1]
pd.DataFrame(
    {
        "Williams (constante r)": ["positief, significant", "groot", "nul", "nul"],
        "verwacht": ["niet significant", "klein", "negatief, significant", "rond 10%"],
        "hier": [
            f"{growth_fit['coëfficiënt']:.3f} (t = {growth_fit['t-waarde']:.2f})",
            f"{growth_fit['R2']:.2f}",
            f"{return_fit['coëfficiënt']:.3f} (t = {return_fit['t-waarde']:.2f})",
            f"{return_fit['R2']:.2f}",
        ],
    },
    index=["dividendgroei: coëfficiënt", "dividendgroei: R2",
           "rendement: coëfficiënt", "rendement: R2"],
)
```

**Geslaagd.** Alle drie de verwachtingen komen uit, want de dividendcoëfficiënt is
niet significant, de rendementscoëfficiënt is negatief en significant, en de $R^2$
ligt rond tien procent (tabel hierboven). Alleen het teken van de
dividendcoëfficiënt past bij Williams, en toch is de uitkomst voor zijn model een
verwerping, omdat $r$ geen constante blijkt maar een tijdreeks.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Het dividend discount model verklaart veel. Het rust
op een identiteit die niet breekt, en legt vast dat een prijs alleen beweegt als
verwachte uitkeringen of discontovoeten bewegen, zodat elke waarderingsdiscussie
een discussie wordt over welke van de twee het is. Het Gordon-model gaf de praktijk
een werkbare vuistregel, namelijk dat het verwachte rendement gelijk is aan
dividendrendement plus groei, en de PVGO liet zien dat groei en waarde niet
hetzelfde zijn.

**Waar het breekt.** Het model breekt niet in de boekhoudkundige identiteit, maar
in de aanname van Williams dat $r$ constant is. De prijs-dividend-ratio voorspelt de
tienjaarsgroei van dividenden nauwelijks ($R^2 \approx 5\%$) en het
tienjaarsrendement wel ($R^2 \approx 12\%$). Volgens [](#eq-williams-ddm-pd)
beweegt $r$ dus. Ruis in de schatting van $g$ verklaart dat niet. De simulatie
liet waarderingen zien die tot een factor twee naast zitten, terwijl de ratio van
10 tot 86 liep, en de beweging van die ratio voorspelt rendementen en geen
dividenden. De discontovoet $r$, het enige getal dat Williams als gegeven nam,
verklaart ruim twee keer zoveel van de beweging als de dividendgroei.

**Risico of vergissing?** Beide lezingen passen bij dezelfde tabel. In de
Chicago-lezing is $r$ de vergoeding voor aandelenrisico, hoog als mensen arm en
bang zijn en laag als ze rijk zijn, zodat voorspelbare rendementen passen bij een
goed werkende markt. In de Yale-lezing extrapoleren mensen de laatste jaren,
betalen ze te veel na goede jaren en te weinig na slechte, en is de
voorspelbaarheid de trage correctie van die vergissing. Omdat beide dezelfde
negatieve helling voorspellen, kan pas een theorie over $r$ ze scheiden. In 2013, toen
Fama en Shiller samen de
Nobelprijs kregen, was het vak daar nog niet uit ([](#05-33-fama-vs-shiller)).

**Theorie of feit?** Bij elke bijdrage vragen we of ze een theorie levert die
getoetst kan worden, of een feit dat nog op een verklaring wacht.
Bachelier leverde een *feit*, koersen als random walk, terwijl Williams een
identiteit leverde die waar is zonder iets uit te sluiten, en een model met een
constante $r$ dat toetsbaar is. Dat model werd pas decennia later zo getoetst en
verworpen, na het CAPM, dat in [](#00-00-setup) het eerste getoetste model van het
vak heet.

**Wat er daarna kwam.** Williams had geen theorie van $r$, maar wel het inzicht
dat er een nodig is. Markowitz verplaatste de vraag van wat één aandeel waard is
naar welke portefeuille een belegger moet houden en welk risico daarbij telt, in
[](#01-04-markowitz).

## Oefeningen

:::{exercise}
:label: ex-williams-ddm-instap

**Instap: het toy-voorbeeld gevarieerd.** Neem het toy-voorbeeld, maar laat het
dividend vanaf jaar 4 met 4% groeien in plaats van 5%.

1. Bereken met de hand de eindwaarde op $t=0$, de prijs $p_0$ en het aandeel van
   de eindwaarde in de prijs.
2. Met hoeveel procent daalt de prijs, en waarom zoveel?
:::

:::{solution} ex-williams-ddm-instap
:class: dropdown

**(1)** De eindwaarde op $t=3$ is $1{,}331 \times 1{,}04/0{,}06 = 23{,}0707$.
Terugrekenen met $1{,}331$ laat die factor wegvallen: $1{,}04/0{,}06 = 17{,}3333$.
De prijs is $3{,}00 + 17{,}33 = 20{,}33$, en de eindwaarde is daarvan 85,2%.

```{code-cell} ipython3
g_late_alt = 0.04
terminal_instap = dividends[-1] * (1 + g_late_alt) / (r - g_late_alt)
terminal_pv_instap = terminal_instap / (1 + r) ** n
price_instap = discounted.sum() + terminal_pv_instap

pd.Series({
    "eindwaarde op t=0": terminal_pv_instap,
    "prijs p_0": price_instap,
    "aandeel eindwaarde": terminal_pv_instap / price_instap,
    "verandering prijs": price_instap / price - 1,
}).round(4)
```

**(2)** De prijs daalt met ruim 15%, van 24,00 naar 20,33. De eindwaarde daalt
17,5%, van 21,00 naar 17,33, omdat één procentpunt minder groei $r - g$ een vijfde
groter maakt en $d_4$ iets kleiner. Omdat de eindwaarde het grootste deel van de
prijs is, werkt die daling bijna volledig door. De waardering hangt dus vooral af
van de groei in de verre toekomst, en juist daarover weet niemand iets.
:::

:::{exercise}
:label: ex-williams-ddm-1

**De bel die het model toestaat.** Neem $r = 8\%$, $d_0 = 2{,}00$ en constante
dividendgroei $g = 3\%$.

1. Bereken de fundamentele waarde $p^{f}_0$ en de fundamentele
   prijs-dividend-ratio.
2. Laat zien dat $p_t = p^{f}_t + B_t$ met $\E_t[B_{t+1}] = (1+r) B_t$ voldoet
   aan $p_t = \E_t[d_{t+1}+p_{t+1}]/(1+r)$.
3. Stel dat $p_0 = p^{f}_0 + 10$ en dat de bel exact zijn verwachte pad volgt.
   Bereken de prijs-dividend-ratio na 10, 25 en 50 jaar. Vanaf welk jaar is meer
   dan de helft van de prijs bel?
:::

:::{solution} ex-williams-ddm-1
:class: dropdown

**(1)** $p^f_0 = d_0(1+g)/(r-g) = 2{,}00 \times 1{,}03/0{,}05 = 41{,}20$. Gedeeld door het dividend van
vandaag geeft dat $\mathrm{PD} = 20{,}6$.

**(2)** Vul in: $\E_t[d_{t+1} + p^f_{t+1} + B_{t+1}]/(1+r)
= \left(\E_t[d_{t+1}+p^f_{t+1}] + (1+r)B_t\right)/(1+r) = p^f_t + B_t$, omdat
$p^f$ per constructie aan de vergelijking voldoet. De bel is een tweede, even
geldige oplossing van dezelfde differentievergelijking.

**(3)** We volgen fundament en bel jaar voor jaar en zoeken het eerste jaar
waarin de bel groter is.

```{code-cell} ipython3
r_ex, d0_ex, g_ex, b0 = 0.08, 2.00, 0.03, 10.0

t_grid = np.array([0, 10, 25, 50])
d_t = d0_ex * (1 + g_ex) ** t_grid
p_f = d_t * (1 + g_ex) / (r_ex - g_ex)
b_t = b0 * (1 + r_ex) ** t_grid

bubble = pd.DataFrame(
    {
        "jaar": t_grid,
        "fundamenteel": p_f,
        "bel": b_t,
        "prijs": p_f + b_t,
        "PD-ratio": (p_f + b_t) / d_t,
        "aandeel bel": b_t / (p_f + b_t),
    }
).set_index("jaar").round(3)

crossing_year = None
for year in range(200):
    bubble_value = b0 * (1 + r_ex) ** year
    fundamental_value = d0_ex * (1 + g_ex) ** (year + 1) / (r_ex - g_ex)
    if bubble_value > fundamental_value:           # bel groter dan fundament
        crossing_year = year
        break

print(f"de bel is meer dan de helft van de prijs vanaf jaar {crossing_year}")
bubble
```

De prijs-dividend-ratio loopt van 25,6 via 28,6 en 37,0 naar 74,1 na vijftig
jaar, en vanaf jaar 30 is meer dan de helft van de prijs bel. De bel groeit met
8% per jaar en het fundament met 3%, zodat het aandeel van de bel naar één loopt.
De transversaliteitsvoorwaarde is daarmee de aanname die uitsluit dat de
prijs-dividend-ratio voor altijd blijft stijgen, en dat is een aanname over
gedrag, niet over wiskunde.
:::

:::{exercise}
:label: ex-williams-ddm-2

**Groei die waarde vernietigt.** Een bedrijf verwacht volgend jaar een winst per
aandeel van $e_1 = 5{,}00$. De discontovoet is $r = 9\%$.

1. Bereken de prijs en de PVGO voor $\mathrm{ROE} \in \{6\%, 9\%, 12\%\}$ bij een
   inhoudingspercentage $b = 0{,}5$.
2. Het bedrijf verhoogt $b$ naar $0{,}6$. Voor welke $\mathrm{ROE}$ stijgt de
   prijs, en waarom?
:::

:::{solution} ex-williams-ddm-2
:class: dropdown

We passen [](#eq-williams-ddm-pvgo) toe bij beide inhoudingspercentages.

```{code-cell} ipython3
e1_ex, r_ex2 = 5.00, 0.09

rows_pvgo = []
for roe in (0.06, 0.09, 0.12):
    price_half = (1 - 0.5) * e1_ex / (r_ex2 - 0.5 * roe)
    price_more = (1 - 0.6) * e1_ex / (r_ex2 - 0.6 * roe)
    rows_pvgo.append(
        {
            "ROE": roe,
            "prijs bij b = 0,5": price_half,
            "PVGO bij b = 0,5": price_half - e1_ex / r_ex2,
            "prijs bij b = 0,6": price_more,
        }
    )

pd.DataFrame(rows_pvgo).set_index("ROE").round(4)
```

**(1)** Zonder groei is het bedrijf $e_1/r = 55{,}56$ waard. Bij
$\mathrm{ROE} = 6\%$ is de prijs $2{,}50/0{,}06 = 41{,}67$ en de PVGO $-13{,}89$;
bij 9% is de prijs $55{,}56$ en de PVGO nul; bij 12% is de prijs
$2{,}50/0{,}03 = 83{,}33$ en de PVGO $27{,}78$.

**(2)** Meer inhouden verhoogt de prijs alleen bij $\mathrm{ROE} = 12\% > r$
(naar 111,11) en verlaagt hem bij 6% (naar 37,04). Bij $\mathrm{ROE} = r$ maakt $b$
niets uit, want een investering tegen de discontovoet heeft een netto contante
waarde van nul. Dat lijkt op de stelling van Miller en Modigliani
{cite}`MillerModigliani1961` (bij gegeven investeringen raakt het uitkeringsbeleid
de waarde niet), maar het is niet hetzelfde, omdat $b$ hier juist de investering
verandert. Groei is in dit model dus geen aparte bron van waarde, maar een
herverpakking van $\mathrm{ROE} - r$.
:::

:::{exercise}
:label: ex-williams-ddm-3

**De replicatie op een andere steekproef.** Herhaal de twee regressies uit de
replicatie op de naoorlogse steekproef (waarnemingen vanaf december 1945) en op
een horizon van vijf jaar in plaats van tien. Rapporteer coëfficiënt,
$t$-waarde en $R^2$ voor beide afhankelijke variabelen. Verandert de conclusie
over welk van de twee kanalen beweegt?
:::

:::{solution} ex-williams-ddm-3
:class: dropdown

Voor vier combinaties van steekproef en horizon herhalen we de twee regressies.

```{code-cell} ipython3
def horizon_panel(frame, h, start=None):
    """Overlapping h-year forward growth and return, against log PD."""
    sub = frame if start is None else frame.loc[start:]
    lpd = np.log(sub["real_price"] / sub["real_dividend"]).rename("log_pd")
    growth_h = (np.log(sub["real_dividend"].shift(-h) / sub["real_dividend"]) / h).rename(
        "dividendgroei"
    )
    return_h = (
        np.log(sub["real_total_return_price"].shift(-h) / sub["real_total_return_price"])
        / h
    ).rename("rendement")
    return pd.concat([lpd, growth_h, return_h], axis=1).dropna()


rows_ex = []
for label, h, start in [
    ("1871–, h=10", 10, None),
    ("1945–, h=10", 10, "1945"),
    ("1871–, h=5", 5, None),
    ("1945–, h=5", 5, "1945"),
]:
    sample = horizon_panel(annual, h, start)
    for column in ("dividendgroei", "rendement"):
        fit = hap.newey_west(sample[column], sample["log_pd"], lags=h - 1)
        rows_ex.append(
            {
                "steekproef": label,
                "variabele": column,
                "coëfficiënt": fit.params.iloc[1],
                "t-waarde": fit.tvalues.iloc[1],
                "R2": fit.rsquared,
                "n": int(fit.nobs),
            }
        )

pd.DataFrame(rows_ex).set_index(["steekproef", "variabele"]).round(4)
```

De rendementscoëfficiënt is in alle vier de varianten negatief, en naoorlogs
sterker: $-0{,}063$ met $t = -3{,}50$ op tien jaar. De dividendcoëfficiënt is
overal klein en alleen over de volle steekproef op vijf jaar net significant
($0{,}026$, $t = 2{,}02$). Ook dan reageert de dividendgroei over vijf jaar met
$5 \times 0{,}026 \approx 0{,}13$ log-punt op één log-punt prijs-dividend-ratio,
tegen $5 \times 0{,}045 \approx 0{,}22$ voor het rendement. De conclusie verandert
niet.

De $t$-waarden schommelen wel sterk, want 71 naoorlogse waarnemingen op tien jaar
zijn nog geen acht onafhankelijke perioden. Wat dit leert: de richting van het
resultaat is robuust en de sterkte niet, omdat een helling met zo weinig
onafhankelijke perioden net zo slecht te meten is als een gemiddeld rendement.
:::
