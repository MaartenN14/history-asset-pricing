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

**Wat we al weten.** Uit [](#01-02-bachelier) komt een beschrijving van koersen:
prijsveranderingen zijn vrijwel onvoorspelbaar, en hun spreiding groeit met
$\sqrt{t}$. Dat is een uitspraak over *veranderingen*, niet over *niveaus*.
Cowles liet zien dat beleggingsadviseurs de markt niet verslaan, Kendall dat
weekkoersen geen patroon hebben. Niemand van hen kon zeggen waarom de koers van
vandaag is wat hij is: er was een theorie van koersveranderingen, maar geen
theorie van het koersniveau.

**Welke vraag staat open.** Wat is een aandeel waard: welke grootheid maakt van
een koers meer dan een getal waarover mensen het toevallig eens zijn?
```

## Overzicht

Wat is een aandeel waard? Williams antwoordde in 1938: de contante waarde van
alle dividenden die het ooit uitkeert, verdisconteerd tegen een vaste
discontovoet. De data verwerpen dat antwoord in die vorm: niet de verwachte
dividenden maar de discontovoet beweegt. In deze lecture:

- leiden we die som af uit de definitie van rendement plus twee aannames: een
  constant verwacht rendement $r$, en geen bel in de prijs;

- werken we hem uit tot het Gordon-groeimodel $p = d_1/(r-g)$, en laten we zien
  hoe gevoelig die breuk is voor $r$ en $g$;

- scheiden we twee dingen. De boekhoudkundige identiteit volgt uit de definitie
  van rendement en kan, net als "bezit is schuld plus eigen vermogen", niet fout
  zijn. Het model van Williams neemt een constante discontovoet aan en kan wel
  verworpen worden. De identiteit alleen is geen theorie en geen feit;

- simuleren we hoe breed een waardering uitvalt als $g$ uit historische data
  wordt geschat;

- toetsen we op Shillers data de voorspelling van het model van Williams. De
  prijs-dividend-ratio liep in de Amerikaanse geschiedenis van 10 tot 86. Bij
  constante $r$ moet een hoge prijs-dividend-ratio snelle dividendgroei
  voorspellen. We regresseren de tienjaarsgroei van dividenden en het
  tienjaarsrendement op die prijs-dividend-ratio, en kijken welke van de twee
  reageert.

In 1938 publiceerde John Burr Williams *The Theory of Investment Value*
{cite}`Williams1938`, een proefschrift dat hij bij Schumpeter in Harvard
verdedigde. De kern is één zin: de waarde van een investering is de contante
waarde van de uitkeringen die zij ooit zal doen. Voor een aandeel zijn dat de
dividenden. De gangbare praktijk was toen om de winst met een gewoontegetal te
vermenigvuldigen. Williams verving dat getal door een som, en wie het oneens was,
moest voortaan zeggen *waarover*. Gordon en Shapiro maakten er later de formule
van waarmee het de praktijk in ging {cite}`GordonShapiro1956,Gordon1959`. Het
werk definieert het tijdvak omdat voor het eerst een prijs uit een model volgt,
en niet uit een gewoonte.

## Intuïtie: waarom zou dit waar zijn?

Een aandeel is een stuk papier. Het geeft geen nut, het gaat niet stuk, en
niemand kan erin wonen. Het enige wat het ooit doet, is af en toe geld uitkeren.
Alles wat een aandeel waard is, moet dus uit die uitkeringen komen, of uit de
prijs waarvoor de eigenaar het later verkoopt.

Maar de koper van later staat voor dezelfde vraag. Ook hij kan alleen rekenen op
uitkeringen en op een nóg latere verkoopprijs. Wie die redenering doorzet, ziet
de verkoopprijs steeds verder de toekomst in schuiven, tot hij verdwijnt. Wat
overblijft, is de stroom dividenden.

Meer is de gedachte van Williams niet, en haar kracht zit in wat zij *uitsluit*.
Een aandeel ontleent geen waarde aan het feit dat anderen het willen hebben. Een
koers is niet hoog omdat hij de laatste jaren hoog was. Williams gebruikte zelf
het beeld van een boomgaard. Een belegger koopt geen koersen maar een boomgaard,
en die is de appels waard die eraan komen, ongeacht wat de buurman voor de zijne
betaalde.

Om van die gedachte een getal te maken, zijn twee dingen nodig. Het eerste is een
verwachting over de dividenden. Het tweede is een tarief waartegen een euro van
volgend jaar wordt omgerekend naar een euro van vandaag.

Williams noemde dat
tarief de *interest rate*, de moderne naam is *discontovoet*. Over de dividenden
schreef hij honderden bladzijden, met algebra over groeiende, dalende en eindige
dividendstromen en met tabellen die hij met de hand uitrekende. Over de
discontovoet schreef hij vrijwel niets: hij nam hem als gegeven.

Dat was geen slordigheid maar de stand van de wetenschap in 1938. Er bestond nog
geen theorie die zei welk tarief bij welk risico hoort. Het CAPM kwam pas
zesentwintig jaar later, en daarmee de gedachte dat er een *prijs van risico* is
die voor alle activa gelijk is. Elke eenheid marktrisico levert hetzelfde extra
verwachte rendement op, of het nu om een spoorwegaandeel gaat of om een
nutsbedrijf. Williams zag dat die theorie ontbrak, en werkte eromheen.

Zijn formule is daardoor waar zonder iets te zeggen. Met de dividendverwachtingen
en de discontovoet volgt de prijs. Met de prijs en de dividendverwachtingen volgt
de discontovoet. Er is geen derde vergelijking die de zaak vastpint.

Toch doet de gedachte een voorspelling zodra de discontovoet vastligt. Een aandeel kan
dan alleen duur zijn ten opzichte van zijn dividend omdat de markt snelle
dividendgroei verwacht. Een hoge prijs-dividend-ratio (de prijs gedeeld door het
dividend) moet dan gevolgd worden door snel stijgende dividenden. De theorie leidt
die voorspelling af, en de replicatie toetst haar.

```{note}
Williams verkocht in 1938 nauwelijks exemplaren. Het boek werd in de jaren
vijftig herontdekt, toen Gordon en Shapiro de oneindige som tot één breuk
samentrokken. Vanaf dat moment kon een analist het in twee minuten gebruiken
{cite}`GordonShapiro1956`. Zulk indikken gebeurt in dit vak vaker. Een idee wordt
pas gebruikt zodra iemand het tot een formule met drie symbolen heeft
teruggebracht, en dan ook op plaatsen waar het niet hoort.
```

## Toy-voorbeeld: drie jaar dividenden, met de hand verdisconteerd

Het kleinste voorbeeld van Williams' som is één aandeel met twee groeifasen, met
de hand verdisconteerd. Eerst de imports-cel, de enige van deze lecture.

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
straks afleidt: een stroom die volgend jaar $d$ uitkeert en daarna met $g$
groeit, is vandaag $d/(r-g)$ waard.

**Stap 1.** De eerste drie dividenden zijn $d_1 = 1{,}10$, $d_2 = 1{,}21$ en
$d_3 = 1{,}331$.

**Stap 2.** Verdisconteren gaat per jaar met een factor $1{,}10$. Omdat de groei in
deze fase *toevallig gelijk is aan de discontovoet*, is elke term gelijk aan één:
$1{,}10/1{,}10 = 1{,}21/1{,}21 = 1{,}331/1{,}331 = 1{,}00$. Samen zijn de eerste
drie dividenden $3{,}00$ waard.

**Stap 3.** Vanaf jaar 4 groeit het dividend met 5%, te beginnen bij
$d_4 = 1{,}331 \times 1{,}05 = 1{,}39755$.

**Stap 4.** Volgens het recept is die stroom op $t=3$ waard
$d_4/(r-g) = 1{,}39755/0{,}05 = 27{,}951$. Dat is de *eindwaarde*: de verwachte
verkoopprijs van het aandeel op $t=3$.

**Stap 5.** Terugrekenen naar vandaag met $1{,}10^3 = 1{,}331$ geeft
$27{,}951/1{,}331 = 21{,}00$. Dat is exact, want $1{,}331 \times 21 = 27{,}951$.

**Stap 6.** De prijs is $p_0 = 3{,}00 + 21{,}00 = 24{,}00$, en de
prijs-dividend-ratio is $\mathrm{PD}_0 = 24{,}00/1{,}00 = 24$.

De codecel rekent dezelfde stappen na en zet de handberekening ernaast.

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

De twee kolommen zijn gelijk, dus de code doet wat de handberekening doet. Van
de prijs van $24{,}00$ komt $21{,}00$ uit alles na jaar 3: 87,5%.

Dat is geen toeval van dit voorbeeld. Weeg elk dividend met zijn aandeel in de
prijs: dan ligt het zwaartepunt van deze waardering 22 jaar in de toekomst. De
theorie rekent dat getal na zodra het Gordon-model is afgeleid.
Een waardering is dus vooral een uitspraak over een periode waarover niemand iets
weet. Een kleine fout in de groeivoet van die verre toekomst weegt daardoor zwaar
in de prijs. De simulatie verderop laat zien hoe zwaar een schattingsfout in
de groeivoet weegt.

Wie het toy narekent, weet nu twee dingen: de prijs komt
vooral uit de eindwaarde, en de eindwaarde hangt af van het kleine verschil
$r - g$.

## Theorie

We leiden vier dingen af. Eerst de boekhoudkundige identiteit, die uit de
definitie van rendement volgt, en daaruit met één aanname het model van
Williams. Dat is de kern, en de
transversaliteitsvoorwaarde maakt hem af. Daarna het Gordon-model, de gesloten
vorm die het toy-voorbeeld als recept gebruikte. Dan de PVGO, die zegt wanneer
groei waarde toevoegt. Ten slotte de prijs-dividend-ratio, de enige plek waar het
model iets toetsbaars zegt.

### Opzet en aannames

Deze subsectie legt vast wat een rendement is, en welke aannames het model van
Williams daaraan toevoegt. Er is één aandeel dat op elk tijdstip $t$ een dividend
$d_t \ge 0$ uitkeert, en de prijs $p_t$ is eindig. De prijs is *ex dividend*: wie
op $t$ voor $p_t$ koopt, krijgt $d_{t+1}$ en niet $d_t$. Het bruto rendement van
$t$ naar $t+1$ is dan

```{math}
:label: eq-williams-ddm-rendement
R_{t+1} = \frac{p_{t+1} + d_{t+1}}{p_t}.
```

In woorden: het rendement is wat de koper morgen terugkrijgt, dividend plus
verkoopprijs, gedeeld door wat hij vandaag betaalde. Dit is een definitie, geen
aanname. Het model van Williams voegt er twee aannames aan toe: een constant
verwacht rendement, en verderop de transversaliteitsvoorwaarde.

De eerste aanname: er is een getal $r$ zodat voor elke periode
$\E_t[R_{t+1}] = 1 + r$. Het *verwachte* rendement is dus constant, niet het
gerealiseerde. $R$ is bruto en $r$ netto, zoals in de notatie van de
[inleiding](#index). Let op de wissel ten opzichte van [](#01-02-bachelier). Daar
waren kleine letters logs en was $r$ een logrendement. Hier zijn $p_t$ en $d_t$
gewone bedragen in euro en is $r$ de discontovoet. Logs komen pas in de
replicatie terug, en daar staat het er steeds bij. In dit model is de discontovoet $r$ hetzelfde als het
verwachte netto rendement; we noemen hem verder alleen de discontovoet.

Voor Amerikaanse aandelen ligt hij rond 7% per jaar, reëel. In 1938 was er nog niets
om deze aanname door te vervangen. De rest van de reeks doet dat wel.

### Van de definitie van rendement naar de contante waarde

De prijs van vandaag is de contante waarde van de dividenden tot een horizon $K$,
plus de verdisconteerde verkoopprijs op $K$. Dat volgt in een eerste versie uit
de definitie van rendement alleen, en in een tweede versie uit het model van
Williams.

*Waarom zou dit waar zijn?* Een koper betaalt vandaag een prijs en krijgt morgen
een dividend en een verkoopprijs. Wat hij vandaag betaalt, is dus de opbrengst van
morgen, gedeeld door het rendement. De koper van morgen doet hetzelfde met de
opbrengst van overmorgen. Zo schuift de verkoopprijs steeds verder weg, en blijven
de dividenden over. Hoe hoger de dividenden, hoe hoger de prijs; hoe hoger het
rendement waarmee ze verdisconteerd worden, hoe lager.

**De boekhoudkundige identiteit.** Schrijf [](#eq-williams-ddm-rendement) als
$p_t = (d_{t+1} + p_{t+1})/R_{t+1}$ en vul dezelfde gelijkheid in voor $p_{t+1}$,
$p_{t+2}$, enzovoort. Na $K$ stappen staat er

$$
p_t = \sum_{j=1}^{K} \frac{d_{t+j}}{R_{t+1} \cdots R_{t+j}}
      + \frac{p_{t+K}}{R_{t+1} \cdots R_{t+K}} .
$$

In woorden: de prijs is de som van de dividenden tot $K$ en de verkoopprijs op
$K$, verdisconteerd met de rendementen die werkelijk worden behaald.

We noemen dit de *boekhoudkundige identiteit*. Ze volgt uit de definitie van rendement, neemt
niets aan en kan daarom door geen enkele data worden verworpen. Het *model van
Williams* voegt de aanname van een constante discontovoet toe, en dat model kan
wel door de data worden verworpen. Dat onderscheid draagt de hele lecture: de replicatie
toetst het model, niet de identiteit.

**Het model van Williams.** Neem nu verwachtingen op $t$ in
[](#eq-williams-ddm-rendement) en gebruik $\E_t[R_{t+1}] = 1+r$:

$$
p_t = \frac{\E_t\!\left[d_{t+1} + p_{t+1}\right]}{1+r}.
$$

De prijs is de verwachte opbrengst van morgen, één periode verdisconteerd. Deze
vergelijking geldt op elk tijdstip, dus ook op $t+1$:
$p_{t+1} = \E_{t+1}[d_{t+2} + p_{t+2}]/(1+r)$. We substitueren dat in de vorige
vergelijking en gebruiken de wet van iteratieve verwachtingen,
$\E_t[\E_{t+1}[\cdot]] = \E_t[\cdot]$: wat we vandaag verwachten dat we morgen
zullen verwachten, verwachten we vandaag al.

$$
p_t = \frac{\E_t[d_{t+1}]}{1+r} + \frac{\E_t[d_{t+2}]}{(1+r)^2}
      + \frac{\E_t[p_{t+2}]}{(1+r)^2}.
$$

Nog $K-2$ keer herhalen geeft de eindige versie van het model van Williams:

```{math}
:label: eq-williams-ddm-eindig
p_t = \sum_{j=1}^{K} \frac{\E_t\!\left[d_{t+j}\right]}{(1+r)^{j}}
      + \frac{\E_t\!\left[p_{t+K}\right]}{(1+r)^{K}} .
```

In woorden: de prijs is de contante waarde van de verwachte dividenden tot $K$,
plus de verdisconteerde verwachte verkoopprijs op $K$. Die verwachte verkoopprijs
heet ook hier de *eindwaarde*. Het toy-voorbeeld is het geval $K = 3$: $3{,}00$
aan dividenden plus $21{,}00$ aan verdisconteerde eindwaarde.

### Het kernresultaat: transversaliteit en het dividend discount model

Laat de horizon $K$ naar oneindig gaan. Als de verdisconteerde eindwaarde dan
verdwijnt, is de prijs de som van alle verwachte dividenden.

*Waarom zou dit waar zijn?* Een koper die een aandeel alleen koopt om het over
$K$ jaar door te verkopen, betaalt vandaag voor de verdisconteerde eindwaarde. De
transversaliteitsvoorwaarde zegt dat die waarde naar nul gaat als $K$ groot
wordt: niemand betaalt voor doorverkopen alleen. Laat men die eis vallen, dan kan
de prijs hoger liggen dan de dividenden rechtvaardigen, omdat men verwacht dat
hij morgen nog hoger is.

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

De transversaliteitsvoorwaarde [](#eq-williams-ddm-transversaliteit) zegt dat de
verdisconteerde eindwaarde in de verre toekomst naar nul gaat.
[](#eq-williams-ddm-ddm) is dan het model van Williams in zijn definitieve vorm:
de prijs is de som van alle verwachte dividenden, elk verdisconteerd met $r$.
Met dezelfde voorwaarde, toegepast op gerealiseerde rendementen, wordt ook de
boekhoudkundige identiteit een oneindige som. [](#eq-williams-ddm-ddm) is daarvan
het bijzondere geval met een constante verwachte discontovoet.

:::{prf:proof}
Neem in [](#eq-williams-ddm-eindig) de limiet $K \to \infty$. We gebruiken de twee
eigenschappen uit de opzet: dividenden zijn niet-negatief en de prijs $p_t$ is
eindig. Door de eerste zijn de partiële sommen niet-dalend, dus de reeks
convergeert of divergeert naar $+\infty$. De verdisconteerde eindwaarde gaat naar
nul volgens [](#eq-williams-ddm-transversaliteit). Door de tweede eigenschap
convergeert het geheel. De eis $r > 0$ gebruikt het bewijs niet rechtstreeks; zij
zorgt dat verre dividenden minder wegen dan nabije. $\square$
:::

Wat gebeurt er als [](#eq-williams-ddm-transversaliteit) niet geldt? Noem de
oplossing uit [](#eq-williams-ddm-ddm) de *fundamentele waarde* $p^{f}_t$, en
bekijk $p_t = p^{f}_t + b_t$ met

$$
\E_t[b_{t+1}] = (1+r)\, b_t .
$$

Zo'n $b_t$ heet een *rationele bel* (rational bubble: een deel van de prijs dat
geen enkele uitkering vertegenwoordigt, maar toch de discontovoet als rendement
oplevert). Ook $p^f_t + b_t$ voldoet aan $p_t = \E_t[d_{t+1}+p_{t+1}]/(1+r)$:
de bel groeit in verwachting met $1+r$ en betaalt zo zijn eigen rendement. Er is
niets *irrationeels* aan, want iedereen verdient wat hij eist. Alleen draagt geen
dividend de bel, en zijn aandeel in de prijs groeit zonder grens.

Bij $r = 10\%$
verdubbelt de bel in ruim zeven jaar, terwijl een dividend dat met 5% groeit
daar veertien jaar over doet.

Williams schreef de bel weg door hem niet te noemen. Dat is verdedigbaar, want
met $b_t \neq 0$ is de prijs onbepaald en valt er niets te rekenen. Maar het is
een keuze, en veertig jaar later valt het vak erover uiteen.

Wie in 1999 zei dat
internetaandelen te duur waren, zei dat er een $b_t$ in zat. Wie zei dat ze
correct geprijsd waren, zei dat $\E_t[d_{t+j}]$ enorm was. Zonder verdere
aannames kunnen de data die twee niet scheiden. We komen daar in
[](#03-15-shiller-excess-volatility) op terug.

```{warning}
De transversaliteitsvoorwaarde is een *aanname*, geen stelling. De modellen na
deze lecture leggen hem bijna overal stilzwijgend op, ook de modellen die
kritisch tegenover Williams staan. Shillers variantiegrenzen (hoeveel een prijs
hoogstens mag bewegen gegeven hoe dividenden bewegen) en de decompositie van
Campbell en Shiller rusten er allebei op.
```

### Wat het voorspelt: het Gordon-groeimodel

Groeit het dividend in verwachting met een vaste $g < r$, dan wordt de oneindige
som één breuk: het dividend van volgend jaar gedeeld door $r - g$.

*Waarom zou dit waar zijn?* De oneindige som is onbruikbaar zolang een analist
voor elk toekomstig jaar een apart getal moet verzinnen. Gordon en Shapiro
vervingen al die getallen door één: het dividend groeit in verwachting elk jaar
met hetzelfde percentage $g$. Een analist hoeft dan nog maar twee getallen te
kiezen, $g$ en $r$. Hoe dichter hij $g$ bij $r$ legt, hoe minder elk volgend dividend door het
verdisconteren wegvalt, en hoe hoger de prijs die hij uitrekent.

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
tussen discontovoet en groei. Dit is het recept uit het toy-voorbeeld. Het
bewijsidee: met constante groei is elke term in de som de vorige maal
$(1+g)/(1+r)$, en een meetkundige reeks met die reden telt op tot de breuk. Het
volledige bewijs staat ingeklapt.

:::{prf:proof}
:class: dropdown

Vul de groeiaanname in [](#eq-williams-ddm-ddm) in:

$$
p_t = \sum_{j=1}^{\infty} \frac{d_t (1+g)^j}{(1+r)^j}
    = d_t \sum_{j=1}^{\infty} q^{j}, \qquad q \equiv \frac{1+g}{1+r} .
$$

Voor $g<r$ is $0 < q < 1$ en is $\sum_{j\ge1} q^j = q/(1-q)$. Invullen:

$$
p_t = d_t \frac{(1+g)/(1+r)}{1 - (1+g)/(1+r)}
    = d_t \frac{1+g}{(1+r)-(1+g)} = \frac{d_t(1+g)}{r-g}. \qquad \square
$$
:::

**Hoe ver weg ligt de waarde?** Weeg elk dividend met zijn aandeel in de prijs.
Het $j$-de dividend weegt dan evenredig met $q^j$, dus de gemiddelde afstand is

$$
\frac{\sum_{j\ge1} j\,q^j}{\sum_{j\ge1} q^j}
= \frac{q/(1-q)^2}{q/(1-q)} = \frac{1}{1-q} = \frac{1+r}{r-g} .
$$

In het toy-voorbeeld is dat $1{,}10/0{,}05 = 22$ jaar na $t = 3$ voor de
eindwaarde. Samen met de eerste drie jaar, die elk $1{,}00$ van de prijs dragen,
komt het zwaartepunt op $(1 + 2 + 3 + 21 \times 25)/24 \approx 22$ jaar vanaf
vandaag. Dit getal heet de *duration* (gemiddelde looptijd) van het aandeel.

Rechts in [](#eq-williams-ddm-gordon) staat dezelfde bewering, omgeschreven naar
$r$. Die vorm is in de praktijk de nuttigste: het verwachte rendement is het dividendrendement plus de
dividendgroei. Wie weet hoeveel dividend hij vandaag krijgt en hoe snel dat
groeit, weet wat hij verdient, zolang de prijs-dividend-ratio niet verandert.

De voorwaarde $g < r$ is geen randgeval maar de kern. Groeit een dividend voor
altijd sneller dan de discontovoet, dan is de contante waarde oneindig. Die oneindige waarde
is een economische uitspraak, geen wiskundig ongemak. Geen bedrijf groeit voor
altijd sneller dan de economie waarin het werkt, dus op lange termijn is $g$
begrensd door de groei van het bruto binnenlands product. Een waardering met $g$
dicht bij $r$ negeert die grens.

```{note}
$g$ is de groei van het dividend *per aandeel*, niet die van de winst of de
omzet. Bedrijven die aandelen uitgeven, laten de winst sneller groeien dan het
dividend per aandeel; bedrijven die aandelen inkopen, andersom. Sinds ongeveer
1985 keren Amerikaanse bedrijven een groeiend deel van hun geld uit via inkoop in
plaats van dividend. Daardoor is de gemeten $d_t$ te laag en de gemeten $g$ te
hoog. Bij elke replicatie op moderne data is dat een reële zorg.
```

**De gevoeligheid die alles bepaalt.** Neem de eindwaarde uit het
toy-voorbeeld als zelfstandig aandeel: $d_0 = 1{,}00$, groei $g = 5\%$ voor altijd en $r = 10\%$.
Dan is $p = 1{,}05/0{,}05 = 21{,}00$. Verschuif nu één parameter één procentpunt:

| verandering | berekening | PD | ten opzichte van 21 |
|---|---|---|---|
| geen ($r = 10\%$, $g = 5\%$) | $1{,}05/0{,}05$ | 21,00 | |
| $r = 9\%$ | $1{,}05/0{,}04$ | 26,25 | +25% |
| $g = 6\%$ | $1{,}06/0{,}04$ | 26,50 | +26,2% |
| $r = 11\%$ | $1{,}05/0{,}06$ | 17,50 | −16,7% |

Een lagere $r$ of een hogere $g$ maakt het aandeel duurder, een hogere $r$
goedkoper. De prijs hangt vrijwel alleen af van het *verschil* $r - g$, en dat
verschil is klein. Een fout van één procentpunt in $r$ of $g$ is een fout van
twintig procent in dat verschil, en de prijs is er ongeveer omgekeerd evenredig
mee. Waarderen met dit model is delen door een klein getal dat niemand kent. De
codecel rekent het hele rooster uit.

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

Langs de diagonaal van het rooster, waar $r - g$ steeds 5 procentpunt is,
verandert de prijs nauwelijks: van 20,80 naar 21,20. Daarbuiten loopt hij van
14,86 tot 35,33. Het rooster bevat ook de getallen uit de tabel.

### PVGO: wat groei toevoegt en wat het kost

Groei verhoogt de prijs alleen als het bedrijf op ingehouden winst meer verdient
dan de discontovoet. Het Gordon-model neemt $g$ als gegeven. Deze subsectie laat
zien waar $g$ vandaan komt, namelijk uit winst die het bedrijf inhoudt en
herbelegt. Zo wordt ook duidelijk waarom een hoge $g$ niet vanzelf een hoge prijs
betekent. Simulatie en replicatie werken daarna weer met $g$ als één getal.

*Waarom zou dit waar zijn?* Een bedrijf dat al zijn winst uitkeert, groeit niet.
Met een winst per aandeel $e_1$ volgend jaar is het dan een eeuwigdurende
obligatie waard: $e_1/r$. Wil het groeien, dan moet het winst inhouden, en die
euro's gaan niet naar de aandeelhouder. Verdient het bedrijf op een ingehouden
euro meer dan de discontovoet, dan stijgt de prijs door te groeien. Verdient het
minder, dan daalt de prijs.

Schrijf $e_{t+1}$ voor de winst per aandeel, $b$ voor het
*inhoudingspercentage* (retention ratio: het deel van de winst dat het bedrijf
niet uitkeert) en $\mathrm{ROE}$ voor het rendement op nieuw geïnvesteerd
vermogen. Deze $b$ is een andere dan de bel $b_t$ hierboven; we volgen de
gangbare notatie. Neem aan dat het bedrijf elk jaar hetzelfde deel $b$ inhoudt,
daarop steeds hetzelfde $\mathrm{ROE}$ verdient en geen nieuwe aandelen uitgeeft.
Dan is $d_{t+1} = (1-b)\,e_{t+1}$, en groeit de winst met
$g = b \cdot \mathrm{ROE}$. Invullen in [](#eq-williams-ddm-gordon) geeft

```{math}
:label: eq-williams-ddm-pvgo
p_t = \frac{(1-b)\,e_{t+1}}{r - b\cdot\mathrm{ROE}}
    = \underbrace{\frac{e_{t+1}}{r}}_{\text{geen groei}} + \mathrm{PVGO}.
```

In woorden: de prijs is de waarde zonder groei plus de waarde van wat het bedrijf
met ingehouden winst nog gaat doen. Dat tweede deel heet $\mathrm{PVGO}$
(*present value of growth opportunities*: de contante waarde van de
groeimogelijkheden). Trek de waarde zonder groei af van de prijs en breng alles
op één noemer:

$$
\mathrm{PVGO}
= \frac{(1-b)\,e_{t+1}}{r - b\cdot\mathrm{ROE}} - \frac{e_{t+1}}{r}
= e_{t+1}\,\frac{(1-b)\,r - (r - b\cdot\mathrm{ROE})}{r\,(r - b\cdot\mathrm{ROE})}
= \frac{b\,e_{t+1}}{r}\cdot\frac{\mathrm{ROE}-r}{r - b\cdot\mathrm{ROE}} .
$$

Het teken van $\mathrm{PVGO}$ is dus het teken van $\mathrm{ROE} - r$. Een bedrijf
dat winst inhoudt en investeert tegen minder dan de discontovoet, *vernietigt*
waarde door te groeien, hoe hard het ook groeit. Daarom is "groeiaandeel" geen
synoniem van "goede belegging". De codecel rekent een voorbeeld door met
$e_1 = 3$, $r = 10\%$, $\mathrm{ROE} = 15\%$ en $b = 1/3$.

```{code-cell} ipython3
e1, r_pvgo, roe = 3.00, 0.10, 0.15
b = 1 / 3

g_impl = b * roe
d1 = (1 - b) * e1
p_pvgo = d1 / (r_pvgo - g_impl)
no_growth = e1 / r_pvgo

roe_low = 0.08                                   # onder de discontovoet
p_low_roe = (1 - b) * e1 / (r_pvgo - b * roe_low)

print(f"g = b * ROE      : {g_impl:.4f}")
print(f"d_1 = (1-b) e_1  : {d1:.4f}")
print(f"prijs            : {p_pvgo:.2f}")
print(f"waarde zonder groei e_1/r : {no_growth:.2f}")
print(f"PVGO             : {p_pvgo - no_growth:.2f}")
print(f"PVGO bij ROE = 8% (< r)   : {p_low_roe - no_growth:.2f}")
```

Bij een $\mathrm{ROE}$ van 15% is $\mathrm{PVGO}$ gelijk aan $10$ op een prijs van
$40$: een kwart van de waarde zit in wat het bedrijf nog gaat doen. Bij een
$\mathrm{ROE}$ van 8% wordt $\mathrm{PVGO}$ negatief. Hetzelfde bedrijf levert
dezelfde groei-inspanning, en de aandeelhouder is er slechter aan toe.

### Hoe het getoetst wordt: de prijs-dividend-ratio

Waar in het model zit iets wat de data kunnen tegenspreken? Deel
[](#eq-williams-ddm-ddm) door $d_t$:

```{math}
:label: eq-williams-ddm-pd
\mathrm{PD}_t = \frac{p_t}{d_t}
  = \sum_{j=1}^{\infty} \frac{\E_t\!\left[d_{t+j}/d_t\right]}{(1+r)^{j}} .
```

In woorden: de prijs-dividend-ratio is de verwachte groei van het dividend over
alle toekomstige jaren, verdisconteerd met $r$. Hier zit de enige empirische
inhoud van het model. Links staat een grootheid die we *observeren* en die enorm
beweegt: in de Amerikaanse data van 9,9 in december 1917 tot 85,6 in december
1999. Rechts staan twee dingen die we niet observeren: verwachte dividendgroei en
de discontovoet.

Minstens één van die twee moet dus meebewegen. Een hoge prijs-dividend-ratio
betekent dan óf dat de markt hoge dividendgroei verwacht, óf dat de markt een lage
discontovoet hanteert. Een derde mogelijkheid is er alleen als de
transversaliteitsvoorwaarde wegvalt en er een bel in de prijs zit.

Williams' eigen lezing is de eerste: $r$ ligt vast, dus alle beweging in
$\mathrm{PD}_t$ komt uit $\E_t[d_{t+j}/d_t]$. Dat is een *falsifieerbare*
uitspraak, en de replicatie toetst haar. Zoals de intuïtie voorspelde, moeten
hoge prijs-dividend-ratio's dan gevolgd worden door snelle dividendgroei. Blijkt
de dividendgroei onvoorspelbaar, dan moet het *rendement* voorspelbaar zijn.

Die conclusie volgt uit de boekhoudkundige identiteit. Die geldt voor elk pad van dividenden en
rendementen, dus ook gemiddeld over alle paden: neem $\E_t$ aan beide kanten. Een
hoge prijs-dividend-ratio vandaag moet dan in verwachting gevolgd worden door
hoge dividendgroei of door lage rendementen. Komt de groei niet, dan moeten de
rendementen gemiddeld laag zijn, en is de discontovoet geen constante maar een
tijdreeks.

Hier is alleen de logica van [](#eq-williams-ddm-pd) nodig, en die vraagt geen
linearisatie: als de teller niet beweegt, moet de noemer het doen. Campbell en
Shiller {cite}`CampbellShiller1988` maakten het argument exact. De ingeklapte
note vat hun stap samen.

:::{note} Campbell en Shiller: de exacte versie
:class: dropdown

Campbell en Shiller loglineariseren de boekhoudkundige identiteit: ze vervangen
de breuk door een lineaire benadering rond de gemiddelde prijs-dividend-ratio,
die ongeveer 26 is. Dan is de log-prijs-dividend-ratio verwachte
log-dividendgroei min verwachte log-rendementen. De linearisatieconstante $\rho$
is het gewicht van de prijs van morgen ten opzichte van prijs plus dividend,
ongeveer 0,96. De bijbehorende variantiedecompositie zegt welk deel van de
schommelingen in de prijs-dividend-ratio uit verwachte groei komt en welk deel
uit verwachte rendementen. De afleiding volgt in [](#04-20-voorspelbaarheid).
:::

```{tip}
De tweede vorm van [](#eq-williams-ddm-gordon), $r = \E_t[d_{t+1}]/p_t + g$,
zegt hetzelfde in één regel. Het dividendrendement van de Amerikaanse markt
daalde sinds 1990 van ruim 3% naar rond 1,5%. Onder Williams' lezing is $g$ dan
met anderhalf procentpunt gestegen. Onder de andere lezing is $r$ met anderhalf
procentpunt gedaald. Hetzelfde getal geeft zo twee heel verschillende conclusies
over het rendement van de komende dertig jaar.
```

```{admonition} Samengevat
:class: tip

- De boekhoudkundige identiteit volgt uit de definitie van rendement en kan niet
  worden verworpen. Het model van Williams voegt een constante discontovoet en de
  transversaliteitsvoorwaarde toe: de prijs is de contante waarde van de verwachte
  dividenden, [](#eq-williams-ddm-ddm).

- Bij constante groei is de prijs $\E_t[d_{t+1}]/(r-g)$, en is het verwachte
  rendement dividendrendement plus groei, [](#eq-williams-ddm-gordon). Een hogere
  $g$ of een lagere $r$ maakt het aandeel duurder, omdat verre dividenden dan
  minder wegvallen door verdisconteren; het effect is sterk zodra $r - g$ klein
  is.

- Groei voegt alleen waarde toe als $\mathrm{ROE} > r$, [](#eq-williams-ddm-pvgo).
  Een hoger inhoudingspercentage $b$ verhoogt dan de prijs, omdat elke
  ingehouden euro meer oplevert dan de discontovoet; bij $\mathrm{ROE} < r$
  verlaagt het de prijs, om de omgekeerde reden.

- Een beweging in de prijs-dividend-ratio moet uit verwachte dividendgroei of uit
  de discontovoet komen, [](#eq-williams-ddm-pd): een hoge ratio betekent hoge
  verwachte groei of een lage discontovoet.

- De simulatie hierna vraagt: hoe breed valt de waardering uit als $g$ uit een
  steekproef wordt geschat?
```

## Simulatie: hoe de schatting van $g$ de waardering overneemt

We bouwen een wereld waarin het Gordon-model exact klopt: dividenden groeien in
verwachting met een vaste $g$, en de discontovoet $r$ is bekend. Per constructie
is er dus één ware prijs-dividend-ratio. De vraag over steekproeven: hoe breed is
de verdeling van de waardering als een analist $g$ schat uit $T$ jaar data?

Het toy-voorbeeld nam aan dat $r$ en $g$ bekend zijn. In de praktijk schat men
$g$ uit historische dividendgroei en $r$ uit een historisch gemiddeld rendement.
Zulke gemiddelden zijn slecht meetbaar: bij een volatiliteit rond 20% per jaar is
een gemiddeld rendement ook na een eeuw data maar op ongeveer twee procentpunt
nauwkeurig. Die onzekerheid heet in deze reeks de standaardfout van 2%. Zij is
afgeleid in [](#00-01-rendementen).

De simulatie isoleert één van de twee gemiddelden: de analist schat alleen $g$, en
$r$ is bekend. Zo is te zien wat onzekerheid in één gemiddelde al doet, zodra het
in de kleine noemer $r - g$ terechtkomt.

We kalibreren op Shillers jaarreeks: gemiddelde, standaarddeviatie en
standaardfout van de reële log-dividendgroei en het reële log-rendement.

```{code-cell} ipython3
shiller_raw = hap_data.shiller()
annual = shiller_raw[shiller_raw.index.month == 12]

log_dgrowth = np.log(annual["real_dividend"]).diff().dropna()
log_return = np.log(annual["real_total_return_price"]).diff().dropna()

calibration = pd.DataFrame(
    {
        "gemiddelde": [log_dgrowth.mean(), log_return.mean()],
        "std.dev.": [log_dgrowth.std(ddof=1), log_return.std(ddof=1)],
        "SE gemiddelde": [
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
met een standaarddeviatie van 11,5%. Dat gemiddelde heeft een standaardfout van
0,93 procentpunt.

Het gemiddelde reële rendement is 6,82%, met een standaardfout van 1,42
procentpunt. Die rij gebruiken we om $r$ te kiezen. In de simulatie is $r$
daarna bekend, dus de onzekerheid in $r$ blijft buiten beschouwing. De werkelijke
onzekerheid van een analist is daardoor nog groter dan wat de simulatie laat
zien.

Het ware model is dan Gordon met $g = 1{,}61\%$ en $r = 6{,}82\%$. Het verschil
$r - g$ is 5,2 procentpunt, bijna de 5 procentpunt van het toy-voorbeeld. De ware
prijs-dividend-ratio is $(1+g)/(r-g) = 1{,}0161/0{,}0521 \approx 19{,}5$.

De kalibratie gebruikt log-gemiddelden, maar de Gordon-formule vraagt strikt
genomen gewone (rekenkundige) verwachtingen, en die liggen een halve variantie hoger: voor
$g$ ongeveer $1{,}61 + 11{,}5^2/200 \approx 2{,}3\%$, voor $r$ ongeveer
$6{,}82 + 17{,}6^2/200 \approx 8{,}4\%$. Het verschil $r - g$ wordt dan 6,1
in plaats van 5,2 procentpunt, en de ware ratio ongeveer 17 in plaats van 19,5.

Voor de vraag van de simulatie, hoe breed de waardering uitvalt rond de
waarheid, maakt die keuze weinig uit. We houden daarom de log-kalibratie.

Een analist ziet $T$ jaar dividendgroei, schat $\hat g$ als het
steekproefgemiddelde, en vult dat met de juiste $r$ in het Gordon-model in.
Gemiddeld zit hij er ongeveer goed. De vraag is hoe breed de verdeling van zijn
waardering is. De codecel simuleert 20 000 analisten voor $T$ gelijk aan 20, 50
en 100 jaar.

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
            "SE van g-dak": sigma_g / np.sqrt(T),
            "PD 5e pct": np.nanpercentile(pd_hat, 5),
            "PD mediaan": np.nanpercentile(pd_hat, 50),
            "PD 95e pct": np.nanpercentile(pd_hat, 95),
            "aandeel g-dak > r": 1 - finite.mean(),
        }
    )

print(f"ware prijs-dividend-ratio: {pd_true:.2f}")
pd.DataFrame(rows).set_index("T (jaren)").round(4)
```

De waardering valt veel breder uit dan de standaardfout van $\hat g$ doet
vermoeden. Bij $T = 50$ is die standaardfout 1,6 procentpunt, een keurig getal.
Toch loopt het interval tussen het 5e en het 95e percentiel van ongeveer 13 tot
ongeveer 40, rond een waarheid van 19,5.

Met een halve eeuw data zit een analist er dus tot een factor drie naast, zonder
iets fout te doen. Hij schatte keurig een gemiddelde en vulde het keurig in.
Zelfs met een eeuw data loopt het interval nog van 14,1 tot 30,8, ruim een factor
twee.

De verdeling is ook scheef. De fout naar boven is veel groter dan die naar
beneden, omdat $1/(r-g)$ convex is in $g$. Een analist met een gunstige
steekproef zit ongeveer drie keer zo ver naast als een analist met een ongunstige:
bij $T = 50$ ligt het 5e percentiel 36% onder de waarheid ($12{,}5$ tegen
$19{,}5$), het 95e percentiel 109% erboven ($40{,}8$). In een klein deel van de steekproeven
komt $\hat g$ zelfs boven $r$ uit (de laatste kolom), en is de prijs oneindig.

Dat is geen programmeerfout. Het model meldt dan dat het buiten zijn
geldigheidsgebied is. Dezelfde steile hyperbool zit achter elke waardering die
een groei van vijftien procent doortrekt.

De figuur zet de verdeling bij $T = 50$, dezelfde 20 000 steekproeven als in de
tabel, naast de hyperbool die haar vorm verklaart. Let links op de lange staart naar rechts, en rechts op hoe steil de
hyperbool wordt vlak voor $g = r$.

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

Links: de verdeling van de prijs-dividend-ratio die volgt uit een op vijftig
jaar geschatte groeivoet, met de ware waarde als verticale lijn. De verdeling is
scheef naar rechts, met een staart die tot in het oneindige loopt. Rechts: de
verklaring. De prijs-dividend-ratio is een hyperbool in $g$, met een verticale
asymptoot op $g = r$; de gestreepte lijn is de ware groeivoet. Ver van de
asymptoot is de functie vlak en vergeeflijk, vlak ervoor explodeert hij.
Dezelfde ruis in $\hat g$ komt op beide plekken uit.
:::

Wat deze figuur over het vak zegt: de discussie of aandelen duur zijn, gaat
bijna nooit over de prijs. Ze gaat over een klein verschil tussen twee slecht
gemeten getallen, gevoerd door mensen die een van beide als vast beschouwen.

De simulatie hield $r$ vast en liet $g$ onzeker. De replicatie hierna vraagt het
omgekeerde: beweegt $r$ zelf?

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** John Burr Williams, *The Theory of Investment Value*, Harvard
University Press 1938 {cite}`Williams1938`, in de gesloten vorm van Gordon en
Shapiro, *Capital Equipment Analysis: The Required Rate of Profit*, Management
Science 1956 {cite}`GordonShapiro1956`.

**Wat.** Geen tabel, want het boek is een afleiding. We toetsen de empirische
inhoud van [](#eq-williams-ddm-pd) onder constante $r$, met regressies van de
reële dividendgroei en het reële totaalrendement over de volgende tien jaar op de
log-prijs-dividend-ratio.

**Data hier.** Shillers maandreeks vanaf 1871 via `hap.data.shiller()`,
teruggebracht tot decemberwaarnemingen: 145 overlappende waarnemingen van 1871
tot en met 2015.

**Verschil met het origineel.** Williams rekende met de hand aan afzonderlijke
bedrijven, zonder index of tijdreeks. Shillers dividendreeks negeert inkoop van
eigen aandelen, wat de gemeten $d_t$ na 1985 te laag maakt.

**Verwachte afwijking.** We verwachten het omgekeerde van Williams: een
dividendcoëfficiënt die niet significant van nul verschilt, en een negatieve,
significante rendementscoëfficiënt met een $R^2$ rond tien procent. Een
significant positieve dividendcoëfficiënt met een rendementscoëfficiënt rond nul
zou Williams' lezing juist steunen.
```

Bij Williams is er geen tabel om na te rekenen. Het boek is een afleiding, geen
empirisch onderzoek. Gordons eigen toets {cite}`Gordon1959` is een cross-sectie
over vier bedrijfstakken in 1951 en 1954, en de bedrijfsgegevens daarvan zijn
niet gratis beschikbaar. Wel toetsbaar is de empirische inhoud van
[](#eq-williams-ddm-pd) onder constante $r$. Alle variatie in de
prijs-dividend-ratio moet dan uit verwachte dividendgroei komen, en niets uit
verwachte rendementen.

De $R^2$ van de rendementsregressie hoort in de orde van tien procent te liggen,
niet van tachtig. Ook onder de andere lezing verklaart de prijs-dividend-ratio
maar een klein deel van wat er gebeurt.

We bouwen eerst het panel: de log-prijs-dividend-ratio en de gemiddelde
jaarlijkse dividendgroei en rendementen over de tien jaar erna.

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
panel.describe().round(4)
```

Het panel heeft 145 waarnemingen, van 1871 tot en met 2015. Nu de twee
regressies. Twee opeenvolgende tienjaarsperioden delen negen jaar, dus hun
residuen hangen samen. Daarom gebruiken we Newey-West-standaardfouten, die voor
zulke samenhang corrigeren, met negen vertragingen: één per gedeeld jaar. Ook
die blijven optimistisch, zoals de waarschuwing hieronder uitlegt.

```{code-cell} ipython3
results = []
for column, label in [
    ("dividendgroei", "reële dividendgroei, 10 jaar vooruit"),
    ("rendement", "reëel totaalrendement, 10 jaar vooruit"),
]:
    fit = hap.newey_west(panel[column], panel["log_pd"], lags=horizon - 1)
    results.append(
        {
            "afhankelijke variabele": label,
            "coëfficiënt": fit.params.iloc[1],
            "standaardfout": fit.bse.iloc[1],
            "t-waarde": fit.tvalues.iloc[1],
            "R2": fit.rsquared,
        }
    )

pd.DataFrame(results).set_index("afhankelijke variabele").round(4)
```

De prijs-dividend-ratio voorspelt het rendement, niet de dividendgroei. De
tabel hieronder zet die uitkomst naast wat Williams' lezing eist.

| | Williams (constante $r$) | verwacht | hier |
|---|---|---|---|
| dividendgroei: coëfficiënt | positief, significant | niet significant | 0,015 ($t = 1{,}63$) |
| dividendgroei: $R^2$ | groot | klein | 0,05 |
| rendement: coëfficiënt | nul | negatief, significant | $-0{,}038$ ($t = -2{,}21$) |
| rendement: $R^2$ | nul | rond 0,10 | 0,12 |

**Geslaagd.** De uitkomst valt zoals het replicatieblok verwachtte: de
dividendcoëfficiënt is niet significant, de rendementscoëfficiënt is negatief en
significant, en de $R^2$ van 0,12 ligt rond tien procent. Voor het model van
Williams betekent dat een verwerping: de prijs-dividend-ratio voorspelt het
rendement, en niet de dividendgroei.

Het teken van de dividendcoëfficiënt wijst wel de kant op die Williams nodig
heeft: na een hoge prijs-dividend-ratio groeien dividenden iets *sneller*. Maar
de omvang is veel te klein om de beweging in de prijs-dividend-ratio te dragen.
Bij een prijs-dividend-ratio die één log-punt hoger ligt, groeien dividenden
de tien jaar erna 1,5 procentpunt per jaar sneller. Samen is dat 0,15 log-punt,
tegen 0,38 log-punt minder rendement. Het rendement draagt dus ruim twee keer
zoveel van de beweging als de dividendgroei, en alleen het rendementsdeel is
significant.

Voor het rendement is de coëfficiënt ongeveer $-0{,}04$. Een prijs-dividend-ratio die één
log-punt hoger ligt, bijvoorbeeld 54 in plaats van 20, gaat samen met een reëel
rendement dat de volgende tien jaar bijna vier procentpunt per jaar lager is.

Volgens de boekhoudkundige identiteit moet de beweging in de
prijs-dividend-ratio dan uit de rendementen komen. Met [](#eq-williams-ddm-pd) als maatstaf is
er dus maar één conclusie mogelijk: $r$ is geen constante. Wat Williams als parameter behandelde, is een
tijdreeks.

```{warning}
Deze regressies gebruiken overlappende tienjaarsperioden: 145 waarnemingen die
samen ongeveer veertien onafhankelijke stukken data zijn. Newey-West met negen
vertragingen corrigeert daar deels voor, maar in eindige steekproeven
onvoldoende.

Bovendien is de regressor sterk persistent: de log-prijs-dividend-ratio van
het ene jaar hangt met een autocorrelatie van 0,91 samen met die van het
volgende. Dat maakt de coëfficiënt in eindige steekproeven te groot in absolute
waarde (de Stambaugh-bias {cite}`Stambaugh1999`). Een onverwachte koersstijging
verhoogt namelijk tegelijk de ratio en het rendement van dat jaar, zodat fouten
in regressor en rendement samen bewegen. Lees deze $t$-waarden als een aanwijzing voor de
richting, niet als bewijs.
```

De figuur toont beide regressies als puntenwolk. Let op de helling in het rechter
paneel.

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
totaalrendement, beide tegen de log-prijs-dividend-ratio van dat moment. De
linkerwolk heeft geen richting; de rechterwolk helt duidelijk naar beneden. Als
Williams' aanname klopte, zouden de twee panelen andersom liggen.
:::

De figuur bevestigt de tabel: links geen helling, rechts een duidelijk dalende.

Dat een prijs gedeeld door een fundamentele stroom rendementen voorspelt, werkte
Shiller uit tot een eigen maatstaf: de *cyclically adjusted price-earnings ratio*
(CAPE, de koers gedeeld door de gemiddelde reële winst over tien jaar)
{cite}`Shiller2000`.

Waarom winst? Het dividend is een onvolmaakte noemer. Het hangt
af van het uitkeringsbeleid, en inkoop van eigen aandelen telt niet mee. CAPE
gebruikt daarom winst, en middelt die over een conjunctuurcyclus zodat één slecht
jaar de noemer niet bepaalt. CAPE is een afstammeling van
[](#eq-williams-ddm-pd): een prijs gedeeld door een fundamentele stroom. Het wordt
ook om dezelfde reden gebruikt: die verhouding zegt iets over toekomstige
rendementen. De codecel herhaalt de rendementsregressie met log CAPE als
regressor.

```{code-cell} ipython3
cape_panel = pd.concat(
    [np.log(annual["cape"]).rename("log_cape"), future_return], axis=1
).dropna()
fit_cape = hap.newey_west(cape_panel["rendement"], cape_panel["log_cape"], lags=horizon - 1)

pd.DataFrame(
    {
        "coëfficiënt": [fit_cape.params.iloc[1]],
        "t-waarde": [fit_cape.tvalues.iloc[1]],
        "R2": [fit_cape.rsquared],
        "n": [int(fit_cape.nobs)],
    },
    index=["log CAPE → reëel rendement, 10 jaar vooruit"],
).round(4)
```

Met CAPE is het verband sterker dan met de prijs-dividend-ratio: de helling is
steiler en de $R^2$ twee keer zo hoog. De steekproef is korter en begint pas in
1881, omdat CAPE tien jaar winsthistorie nodig heeft. Dat sterkere verband zegt
weinig. CAPE
is met kennis van de hele reeks als voorspeller gekozen, en de standaardfouten
lijden onder dezelfde overlap. Wat telt: de richting is dezelfde, en Shillers
maatstaf komt uit dezelfde boekhoudkundige identiteit als de prijs-dividend-ratio, alleen met een andere
noemer.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Meer dan het krediet krijgt. Het dividend discount
model rust op de boekhoudkundige identiteit, en die breekt niet. Het legt vast dat een prijs
alleen beweegt als verwachte uitkeringen of discontovoeten bewegen. Zo wordt elke
waarderingsdiscussie een discussie over welke van de twee het is. Het
Gordon-model gaf de praktijk een werkbare vuistregel: verwacht rendement is
dividendrendement plus groei. In de vorm "earnings yield plus groei" wordt die nog
dagelijks gebruikt. De PVGO liet zien dat groei en waarde niet hetzelfde zijn, een
onderscheid dat in [](#03-16-vroege-anomalieen) empirisch terugkomt.

**Waar het breekt.** Niet in de boekhoudkundige identiteit maar in het model van
Williams, dat wil zeggen in de aanname van constante $r$. De
replicatie laat zien dat de prijs-dividend-ratio de tienjaarsgroei van dividenden
nauwelijks voorspelt ($R^2 \approx 5\%$, $t < 2$). Het tienjaarsrendement
voorspelt hij wel ($R^2 \approx 12\%$, coëfficiënt ongeveer $-0{,}04$ met
$t \approx -2$). Onder [](#eq-williams-ddm-pd) betekent dat dat $r$ beweegt. Het
enige symbool dat Williams als gegeven nam, doet het meeste werk. Waar die
beweging vandaan komt, is de vraag van de rest van de reeks. De correcte
behandeling van deze $t$-waarden volgt in [](#04-20-voorspelbaarheid).

**Risico of vergissing?** Beide lezingen passen bij dezelfde tabel. De
Chicago-lezing: $r$ is de vergoeding voor aandelenrisico, hoog als mensen arm en
bang zijn, laag als ze rijk zijn. In een depressie zijn aandelen goedkoop omdat
niemand dan risico wil dragen, en wie het wel doet, wordt betaald. Voorspelbare
rendementen zijn dan geen anomalie maar een goed werkende markt. De Yale-lezing:
mensen extrapoleren de laatste jaren en betalen te veel na goede jaren en te
weinig na slechte. De voorspelbaarheid is dan de trage correctie van die
vergissing. Beide voorspellen dezelfde negatieve helling, en pas een theorie over
$r$ scheidt ze. Ook de scheefheid uit de simulatie speelt in dat debat mee: in
[](#03-15-shiller-excess-volatility) is zij een verweer tegen Shillers
variantiegrenzen.

In de termen van theorie of feit verschuift er in deze lecture iets. Bachelier
leverde een *feit*, koersen als random walk, dat op een verklaring wachtte.
Williams leverde twee dingen. De boekhoudkundige identiteit is waar zonder iets
uit te sluiten. Het model van Williams voegt er een constante $r$ aan toe, en die
aanname is toetsbaar en verworpen.

Elk later model in de reeks is een scherper
antwoord op dezelfde vraag: waar komt $r$ vandaan? In 2013, toen Fama en Shiller
samen de Nobelprijs kregen, was het vak daar nog niet uit
([](#05-33-fama-vs-shiller)).

**Wat er daarna kwam.** Williams had geen theorie van $r$, maar wel het inzicht
dat er een nodig is. Markowitz verplaatste als eerste de vraag. Niet langer wat
één aandeel waard is, maar welke portefeuille een belegger moet houden en welk
risico daarbij telt: zie [](#01-04-markowitz).

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

**(1)** $d_4 = 1{,}331 \times 1{,}04 = 1{,}38424$, en de eindwaarde op $t=3$ is
$1{,}38424/0{,}06 = 23{,}0707$. Terugrekenen met $1{,}331$ geeft
$1{,}331 \times 1{,}04/(0{,}06 \times 1{,}331) = 1{,}04/0{,}06 = 17{,}3333$: de
factor $1{,}331$ valt weg, net als in het toy. De prijs is $3{,}00 + 17{,}33 = 20{,}33$, en de
eindwaarde is daarvan 85,2%.

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

**(2)** De prijs daalt met ruim 15%, van 24,00 naar 20,33. Eén procentpunt minder
groei maakt het verschil $r - g$ een vijfde groter, en de eindwaarde is
omgekeerd evenredig met dat verschil. Omdat de eindwaarde het grootste deel van de
prijs is,
werkt die daling bijna volledig door. Wat dit leert: de waardering hangt vooral
af van de groei in de verre toekomst, en juist daarover weet niemand iets.
:::

:::{exercise}
:label: ex-williams-ddm-1

**De bel die het model toestaat.** Neem $r = 8\%$, $d_0 = 2{,}00$ en constante
dividendgroei $g = 3\%$.

1. Bereken de fundamentele waarde $p^{f}_0$ en de fundamentele
   prijs-dividend-ratio.
2. Laat zien dat $p_t = p^{f}_t + b_t$ met $\E_t[b_{t+1}] = (1+r) b_t$ voldoet
   aan $p_t = \E_t[d_{t+1}+p_{t+1}]/(1+r)$.
3. Stel dat de werkelijke prijs op $t=0$ gelijk is aan $p_0 = p^{f}_0 + 10$.
   Bereken de verwachte prijs-dividend-ratio na 10, 25 en 50 jaar in dit
   belscenario, als de bel exact zijn verwachte pad volgt. Vanaf welk jaar is
   meer dan de helft van de prijs bel?
:::

:::{solution} ex-williams-ddm-1
:class: dropdown

**(1)** $p^f_0 = d_0(1+g)/(r-g) = 2{,}00 \times 1{,}03/0{,}05 = 41{,}20$, dus
$\mathrm{PD} = 20{,}6$.

**(2)** Vul in: $\E_t[d_{t+1} + p^f_{t+1} + b_{t+1}]/(1+r)
= \left(\E_t[d_{t+1}+p^f_{t+1}] + (1+r)b_t\right)/(1+r) = p^f_t + b_t$. De eerste
term geeft $p^f_t$, omdat $p^f$ per constructie aan de vergelijking voldoet. De
bel voegt dus niets toe aan de restrictie: hij is een tweede, even geldige
oplossing van dezelfde differentievergelijking.

**(3)**

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

De bel groeit met 8% per jaar en de fundamentele waarde met 3%, dus het aandeel van de
bel loopt onvermijdelijk naar één. Wat dit leert: de transversaliteitsvoorwaarde
is geen technische bijzaak. Zij is de aanname die verbiedt dat de
prijs-dividend-ratio voor altijd blijft stijgen, en dat is een aanname over
gedrag, niet over wiskunde.
:::

:::{exercise}
:label: ex-williams-ddm-2

**Groei die waarde vernietigt.** Een bedrijf verwacht volgend jaar een winst per
aandeel van $e_1 = 5{,}00$. De discontovoet is $r = 9\%$.

1. Bereken de prijs en de PVGO voor $\mathrm{ROE} \in \{6\%, 9\%, 12\%\}$ bij een
   inhoudingspercentage $b = 0{,}5$.
2. Bepaal voor elk van de drie gevallen het inhoudingspercentage $b$ dat de
   prijs maximaliseert, door $b$ over een fijn raster te laten lopen.
3. Verklaar in één zin waarom het antwoord op (2) niet van $e_1$ afhangt.
:::

:::{solution} ex-williams-ddm-2
:class: dropdown

De codecel berekent de prijs bij $b = 0{,}5$ en zoekt de beste $b$ op een raster.

```{code-cell} ipython3
e1_ex, r_ex2 = 5.00, 0.09
b_grid = np.linspace(0.0, 0.95, 191)

rows_pvgo = []
for roe in (0.06, 0.09, 0.12):
    price_half = (1 - 0.5) * e1_ex / (r_ex2 - 0.5 * roe)
    feasible = b_grid * roe < r_ex2 - 1e-9
    prices = np.full_like(b_grid, np.nan)
    prices[feasible] = (1 - b_grid[feasible]) * e1_ex / (r_ex2 - b_grid[feasible] * roe)
    rows_pvgo.append(
        {
            "ROE": roe,
            "prijs bij b=0.5": price_half,
            "PVGO bij b=0.5": price_half - e1_ex / r_ex2,
            "optimale b": b_grid[np.nanargmax(prices)],
            "prijs bij optimale b": np.nanmax(prices),
        }
    )

pd.DataFrame(rows_pvgo).set_index("ROE").round(4)
```

Bij $\mathrm{ROE} = 6\% < r$ is de PVGO $-13{,}89$ en is de optimale $b$ nul:
alles uitkeren. Bij $\mathrm{ROE} = 9\% = r$ maakt $b$ niets uit. De prijs is dan
$e_1/r = 55{,}56$ voor elk inhoudingspercentage, zodat het raster een willekeurig
punt als "optimum" aanwijst. De 0,94 in de tabel is daarom betekenisloos; alleen
de prijs ernaast telt. Dat is de irrelevantiestelling van Miller en
Modigliani {cite}`MillerModigliani1961`: onder deze voorwaarden maakt het
uitkeringsbeleid voor de waarde van het bedrijf niet uit.

Bij $\mathrm{ROE} = 12\% > r$ loopt de
optimale $b$ naar de asymptoot $b = r/\mathrm{ROE} = 0{,}75$ en explodeert de
prijs. Het model kent namelijk geen afnemende meeropbrengsten: elke ingehouden
euro verdient eeuwig 12%, tegen een discontovoet van 9%.

**(3)** De prijs is homogeen van graad één in $e_1$: $e_1$ staat als factor voor
de hele uitdrukking, dus de $b$ die de uitdrukking maximaliseert, verandert er
niet door. Wat dit leert: groei is in dit model geen aparte bron van waarde, maar
een herverpakking van $\mathrm{ROE} - r$.
:::

:::{exercise}
:label: ex-williams-ddm-3

**De replicatie op een andere steekproef.** Herhaal de twee regressies uit de
replicatie op de naoorlogse steekproef (waarnemingen vanaf december 1945) en op
een horizon van vijf jaar in plaats van tien. Rapporteer coëfficiënt,
$t$-waarde en $R^2$ voor beide afhankelijke variabelen. Verandert de *conclusie*
over welk van de twee kanalen beweegt?
:::

:::{solution} ex-williams-ddm-3
:class: dropdown

De codecel herhaalt de regressies voor vier combinaties van steekproef en horizon.

```{code-cell} ipython3
def horizon_panel(frame, h, start=None):
    """Overlapping h-year forward growth and return, against log PD."""
    sub = frame if start is None else frame.loc[start:]
    lpd = np.log(sub["real_price"] / sub["real_dividend"]).rename("log_pd")
    gro = (np.log(sub["real_dividend"].shift(-h) / sub["real_dividend"]) / h).rename(
        "dividendgroei"
    )
    ret = (
        np.log(sub["real_total_return_price"].shift(-h) / sub["real_total_return_price"])
        / h
    ).rename("rendement")
    return pd.concat([lpd, gro, ret], axis=1).dropna()


rows_ex = []
for label, h, start in [
    ("1871–, h=10", 10, None),
    ("1945–, h=10", 10, "1945"),
    ("1871–, h=5", 5, None),
    ("1945–, h=5", 5, "1945"),
]:
    frame = horizon_panel(annual, h, start)
    for kolom in ("dividendgroei", "rendement"):
        fit = hap.newey_west(frame[kolom], frame["log_pd"], lags=h - 1)
        rows_ex.append(
            {
                "steekproef": label,
                "variabele": kolom,
                "coëfficiënt": fit.params.iloc[1],
                "t-waarde": fit.tvalues.iloc[1],
                "R2": fit.rsquared,
                "n": int(fit.nobs),
            }
        )

pd.DataFrame(rows_ex).set_index(["steekproef", "variabele"]).round(4)
```

De rendementscoëfficiënt is in alle vier de varianten negatief, en naoorlogs nog
uitgesprokener: $-0{,}063$ met $t = -3{,}50$ op tien jaar. De
dividendgroeicoëfficiënt is overal klein. Alleen over de volle steekproef op vijf
jaar is hij net significant ($0{,}026$, $t = 2{,}02$).

Ook dan is het veel te weinig om het werk te doen. Over vijf jaar reageert de
dividendgroei met $5 \times 0{,}026 \approx 0{,}13$ log-punt op één log-punt
prijs-dividend-ratio, tegen $5 \times 0{,}045 \approx 0{,}22$ voor het rendement.
De conclusie verandert dus niet.

De $t$-waarden schommelen wel sterk. Met 71 naoorlogse waarnemingen op een
horizon van tien jaar zijn er nog geen acht onafhankelijke perioden. Wat dit
leert: de richting van het resultaat is robuust, de sterkte niet. Ook hier
geldt de standaardfout van 2% uit [](#00-01-rendementen): een gemiddeld
rendement is ook na een eeuw data maar op ongeveer twee procentpunt nauwkeurig. Met zo weinig
onafhankelijke perioden is een helling net zo slecht te meten.
:::
