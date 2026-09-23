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

(00-01-rendementen)=

# Rendementen en hun statistiek

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1926–2026. Dit is geen tijdvak maar een meetlat, waarmee we de rest
van de reeks wegen.

**Wat we al weten.** [De vorige lecture](#00-00-setup) zette de gereedschapskist
neer: acht gratis databronnen, een notatie en een handvol schatters. Ze eindigde
met één getal: het rekenkundig gemiddelde marktrendement over honderd jaar is 11,6% per jaar,
met een standaardfout van 1,8 procentpunt. Daar hebben we rendementen opgeteld en
gemiddeld zonder te zeggen wat een rendement is.

**Welke vraag staat open.** Wat meten we als we een gemiddeld rendement
uitrekenen, en hoe nauwkeurig is die meting?
```

## Overzicht

Wat meten we als we een gemiddeld rendement uitrekenen, en hoe nauwkeurig? We
schatten het verwachte rendement, en dat heeft na een eeuw data nog een
standaardfout van twee procentpunt: een 95%-interval van ongeveer vier
procentpunt naar weerszijden. De volatiliteit ligt dan al bijna exact vast. In
deze lecture:

- leggen we het verschil vast tussen simpele rendementen en logrendementen, en
  tussen het rekenkundig en het meetkundig gemiddelde;

- leiden we af dat het meetkundig gemiddelde een halve variantie lager ligt, de
  *variance drag* (de rem die schommelingen op de groei van een vermogen zetten);

- leiden we de standaardfout van het gemiddelde af, en daarmee
  [de standaardfout van 2%](#sec-rendementen-standaardfout): bij 20% volatiliteit
  per jaar is de standaardfout van het gemiddelde na een eeuw twee procentpunt;

- laten we met de stelling van Merton zien dat vaker meten daar niets aan
  verandert;

- simuleren we tweeduizend eeuwen, die we jaarlijks tot dagelijks bekijken;

- repliceren we het eerste gemeten gemiddelde rendement op aandelen, en zetten
  we er de standaardfout bij.

Wat hier staat, was in 1926 al bekend bij statistici. {cite:t}`Merton1980` gaf
het de scherpe vorm: de precisie van een geschatte drift hangt alleen af van de
kalenderlengte van de steekproef. Het Center for Research in Security Prices
(CRSP) zette in de jaren zestig de koersen van alle NYSE-aandelen vanaf 1926 op
magneetband. Op die verse tape rapporteerden Lawrence Fisher en James Lorie in
1964 het gemiddelde rendement op Amerikaanse aandelen over 1926–1960
{cite}`FisherLorie1964`. Hun 9,0% per jaar was de eerste betrouwbare meting van
die grootheid en staat nog altijd in leerboeken.

Bijna elke controverse in de empirische finance gaat over een grootheid waarvan
deze lecture de standaardfout uitrekent. Voorbeelden zijn de equity premium
puzzle (de premie is te hoog voor redelijke risicoaversie) en de factor zoo
(honderden gepubliceerde rendementsfactoren). Door de hele reeks loopt ook de
vraag theorie of feit: is een model een theorie die getoetst wordt, of een feit
dat op een verklaring wacht? Deze lecture is daarop een uitzondering. Er staat
geen theorie in die getoetst wordt, want de stellingen zijn wiskundig waar. Toch
bepalen ze welke latere theorieën toetsbaar zijn, en dat zijn er minder dan het
vak lief is.

## Intuïtie: waarom zou dit waar zijn?

Denk aan iemand die wil weten hoe hard het gemiddeld waait op een bepaalde plek.
Ze zet er een meetpaal neer en kan twee vragen stellen. Hoeveel lucht is er in
totaal langsgekomen? En hoe hard schommelt de wind?

Voor de eerste vraag maakt het niet uit hoe vaak ze meet. Wie elke seconde meet
in plaats van elk uur, krijgt 3600 keer zoveel getallen over dezelfde lucht. Het
totaal van het jaar ligt vast zodra het jaar voorbij is. Een beter gemiddelde
vraagt meer jaren, niet meer metingen per jaar.

Voor de tweede vraag ligt het omgekeerd. De schommeling zit *in* de metingen:
elke extra waarneming zegt iets over hoe hard het schommelt. Met metingen per
seconde ligt de schommeling van dat ene jaar bijna exact vast. Eén jaar
secondedata zegt meer over de schommeling dan een eeuw jaardata.

Voor een aandeel werkt het net zo. De totale hoeveelheid lucht is hier de totale
koersverandering, en die hangt alleen af van begin- en eindkoers. Het gemiddelde
rendement is die totale verandering gedeeld door de tijd. Dagelijks meten geeft
250 keer zoveel getallen, maar niet meer informatie over het gemiddelde. De
*volatiliteit* (de standaarddeviatie van het rendement, per jaar) wordt
daarentegen bij elke verfijning scherper.

Daar komt een tweede ongelijkheid bij, die niet met meten te maken heeft maar
met rekenen. Een verlies van 20% en een winst van 25% heffen elkaar op in
*niveaus*: $0{,}80 \times 1{,}25 = 1$. In *gemiddelden* doen ze dat niet: het
rekenkundig gemiddelde is $+2{,}5\%$, terwijl het vermogen gelijk bleef.
Rendementen vermenigvuldigen zich en gemiddelden tellen op. Het verschil tussen
die twee groeit met de variantie. Bij 20% volatiliteit is het een halve variantie,
$0{,}20^2/2 = 2$ procentpunt per jaar. Over een eeuw is dat een factor
$1{,}02^{100} \approx 7{,}2$ in eindvermogen.

Beide observaties zijn oud. Ze worden pas belangrijk met de getallen van de
echte wereld. De volatiliteit van aandelen is ongeveer 20% per jaar, de *equity
premium* (het extra rendement van aandelen boven de risicovrije rente, hierna de
premie) ongeveer 6%. De ruis, de volatiliteit, is dus ruim drie keer zo groot als
het signaal, de premie, en alleen verstrijkende tijd maakt het signaal
zichtbaar. Sinds Fisher en Lorie is de steekproef bijna drie keer zo lang
geworden. Toch is de premie nog altijd maar op een paar procentpunt na bekend.

We verwachten dus drie dingen. Vaker meten maakt de volatiliteit scherper, maar
het gemiddelde niet. Het meetkundig gemiddelde ligt onder het rekenkundige,
verder naarmate de schommelingen groter zijn. En omdat de ruis zo veel groter is
dan het signaal, blijft het gemiddelde ook na een eeuw onzeker, met een fout van
enkele procentpunten.

## Toy-voorbeeld: drie jaar rendement, met de hand

Eerst laden we de pakketten die de hele lecture gebruikt.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.** Een belegging doet in drie jaar het volgende:

| jaar | netto rendement $r$ | bruto rendement $R = 1 + r$ |
|---|---|---|
| 1 | $+0{,}25$ | $1{,}25$ |
| 2 | $-0{,}20$ | $0{,}80$ |
| 3 | $+0{,}10$ | $1{,}10$ |

Het mechanisme van dit voorbeeld is één ongelijkheid: het rekenkundig gemiddelde
ligt boven het meetkundige, en het verschil is ongeveer een halve variantie.
Stap 1 tot en met 4 laten dat zien. Stap 5 is een voorproef op de tweede vraag
van de lecture: hoe zeker is zo'n gemiddelde?

**Het recept.** Eén formule leiden we pas in de theorie af: het meetkundig
gemiddelde is ongeveer het rekenkundig gemiddelde min een halve variantie.

**Stap 1: het rekenkundig gemiddelde.** Optellen en delen door drie:

$$
\bar r = \frac{0{,}25 - 0{,}20 + 0{,}10}{3} = \frac{0{,}15}{3} = 0{,}05 .
$$

Dat is vijf procent per jaar.

**Stap 2: het meetkundig gemiddelde.** Het product van de bruto rendementen is
$1{,}25 \times 0{,}80 \times 1{,}10 = 1{,}10$. Eén euro is na drie jaar dus
$1{,}10$ euro geworden, en het meetkundig gemiddelde is

$$
\bar R_g = 1{,}10^{1/3} = 1{,}032280, \qquad \text{dus } 3{,}2280\% \text{ per jaar.}
$$

Het verschil met het rekenkundig gemiddelde is $5 - 3{,}2280 = 1{,}772$
procentpunt. Dat is geen afrondingsfout. Over dertig jaar is het het verschil
tussen $1{,}05^{30} = 4{,}32$ en $1{,}0323^{30} = 2{,}59$, bijna een factor twee.

**Stap 3: de logrendementen.** Ze zijn $\log 1{,}25 = 0{,}223144$,
$\log 0{,}80 = -0{,}223144$ en $\log 1{,}10 = 0{,}095310$. De eerste twee vallen
tegen elkaar weg. Meer zit er niet achter de vuistregel dat 20% verlies pas met
25% winst is goedgemaakt. De som is $0{,}095310$, het gemiddelde $0{,}031770$, en

$$
e^{0{,}031770} - 1 = 0{,}032280 .
$$

Dat is exact het meetkundig gemiddelde. Het gemiddelde logrendement *is* het
meetkundig gemiddelde, in een andere schrijfwijze.

**Stap 4: de variance drag.** De afwijkingen van $\bar r = 0{,}05$ zijn $0{,}20$,
$-0{,}25$ en $0{,}05$. Hun kwadraten tellen op tot
$0{,}04 + 0{,}0625 + 0{,}0025 = 0{,}105$. Gedeeld door drie is dat
$\hat\sigma^2 = 0{,}035$, en de halve variantie is $0{,}0175$. Het recept geeft

$$
0{,}05 - 0{,}0175 = 0{,}0325 ,
$$

tegen de exacte $0{,}032280$. Het klopt tot op twee honderdste procentpunt, bij
slechts drie waarnemingen.

**Stap 5, een voorproef: de standaardfout.** Hoe zeker is die 5%? De
standaardfout van een gemiddelde is $s/\sqrt{T}$, met $s$ de standaarddeviatie
en $T$ het aantal jaren; [de vorige lecture](#00-00-setup) gebruikte hem al, en
de theorie bewijst hem hieronder. In stap 4 deelden we door $T = 3$, omdat de drag
over deze drie jaren zelf gaat. Nu schatten we de schommeling van het proces
waaruit de jaren komen. Het gemiddelde is dan zelf geschat, en delen door
$T - 1 = 2$ corrigeert daarvoor. Dat geeft $s^2 = 0{,}0525$ en $s = 0{,}229129$,
en

$$
\SD(\bar r) = \frac{s}{\sqrt{T}} = \frac{0{,}229129}{\sqrt{3}} = 0{,}132288 .
$$

De $t$-waarde is $0{,}05 / 0{,}132288 = 0{,}377964$. Met drie jaar data is vijf
procent per jaar statistisch niet van nul te onderscheiden. Bij $T = 3$ is dat te
verwachten. De onaangename ontdekking van deze lecture is dat het bij $T = 100$
nauwelijks beter wordt.

De codecel rekent alle getallen na en zet ze naast de handberekening.

```{code-cell} ipython3
r = np.array([0.25, -0.20, 0.10])
gross = 1 + r

arith = r.mean()
geom = gross.prod() ** (1 / len(r)) - 1
log_returns = np.log(gross)
geom_via_log = np.exp(log_returns.mean()) - 1
drag_approx = arith - r.var(ddof=0) / 2
se = r.std(ddof=1) / np.sqrt(len(r))

rows = ["rekenkundig gemiddelde", "meetkundig gemiddelde",
        "via gemiddeld logrendement", "benadering: gem. - sigma^2/2",
        "variance drag (exact)", "standaarddeviatie (ddof=1)",
        "standaardfout van het gemiddelde", "t-waarde"]
by_hand = [0.05, 0.032280, 0.032280, 0.0325, 0.017720, 0.229129, 0.132288, 0.377964]
by_code = [arith, geom, geom_via_log, drag_approx, arith - geom,
           r.std(ddof=1), se, arith / se]

pd.DataFrame({"met de hand": by_hand, "code": by_code}, index=rows).round(6)
```

De twee kolommen zijn gelijk. De meetkundige route en de logroute geven tot op
de laatste decimaal hetzelfde, en het recept zit er 0,00022 naast. Wie dit
narekent, weet nu dat het meetkundig gemiddelde een halve variantie onder het
rekenkundige ligt, dat logrendementen optellen, en dat drie jaar niets zegt over
het gemiddelde.

## Theorie

We leiden drie resultaten af. Eerst de variance drag: het meetkundig gemiddelde
ligt een halve variantie onder het rekenkundige. Dan de standaardfout van het
gemiddelde, en daarmee
[de standaardfout van 2%](#sec-rendementen-standaardfout). Dat is de kern. Ten
slotte de stelling van Merton, die zegt waarom vaker meten die standaardfout
niet verkleint. Onderweg zijn de definities en de wortel-$t$-regel nodig, en aan
het eind kijken we wat er overblijft bij autocorrelatie en dikke staarten.

### Opzet: twee soorten rendement

Welk rendement tellen we op? Dat hangt ervan af of we over de tijd optellen of
over activa. Laat $P_t$ de prijs zijn en $D_{t+1}$ het dividend dat tussen $t$ en
$t+1$ wordt uitgekeerd. Het *simpele* netto rendement en het bruto rendement zijn

```{math}
:label: eq-rendementen-simpel
r_{t+1} = \frac{P_{t+1} + D_{t+1}}{P_t} - 1,
\qquad
R_{t+1} = 1 + r_{t+1} = \frac{P_{t+1} + D_{t+1}}{P_t} .
```

In woorden: het bruto rendement is wat een ingelegde euro na één periode waard
is, koers en dividend samen.

Het *logrendement* is de logaritme daarvan. De notatie in [](#00-00-setup)
reserveert kleine letters voor log-grootheden waar dat is aangekondigd. Deze
lecture zet beide soorten echter steeds naast elkaar. Daarom blijft $r$ het
simpele rendement, en schrijven we

```{math}
:label: eq-rendementen-log
\ell_{t+1} \equiv \log R_{t+1} = \log\!\left(1 + r_{t+1}\right).
```

In woorden: $\ell$ is het groeitempo dat, continu doorgerekend, dezelfde euro
oplevert. Bij kleine rendementen liggen $\ell$ en $r$ dicht bij elkaar.

Voor de standaarddeviaties maken we hetzelfde onderscheid. In deze lecture is
$\sigma$ altijd de standaarddeviatie van het simpele rendement en $\sigma_\ell$
die van het logrendement. Bij een volatiliteit van 20% per jaar schelen ze
hooguit twee procentpunt, en in de benaderingen hieronder wisselen we ze uit.

*Waarom zou dit waar zijn?* Definities hoeven niet waar te zijn. De vraag is
waarom er twee nodig zijn. Een belegger telt op twee manieren op: over de jaren
waarin hij belegd blijft, en over de aandelen in zijn portefeuille. Geen enkele
definitie kan beide. Wie simpele rendementen over de tijd optelt, overschat wat
hij overhoudt. Wie logrendementen over aandelen middelt, onderschat het
portefeuillerendement.

Over de **tijd** vermenigvuldigen bruto rendementen zich. Het rendement over
twee perioden is $R_{t+1}R_{t+2}$, niet $R_{t+1}+R_{t+2}$. Logaritmen maken van
dat product een som:

```{math}
:label: eq-rendementen-additief
\ell_{t \to t+k} = \sum_{j=1}^{k} \ell_{t+j} .
```

In woorden: het logrendement over $k$ perioden is de som van de logrendementen
per periode. Annualiseren, horizonnen, de wortel-$t$-regel en variance ratios
(is de variantie van jaarrendementen twaalf keer die van maandrendementen?) zijn
daarom natuurlijk in logs.

Over de **activa** tellen simpele rendementen op. Een portefeuille met gewichten
$w_i$ die optellen tot één heeft rendement $r_p = \sum_i w_i r_i$. Rendement is
een fractie van de ingelegde euro's, en euro's tellen op. Voor logrendementen
geldt dat niet: $\log(1+\sum_i w_i r_i)$ is geen som van $\log(1+r_i)$. Bèta's
(hoe sterk een aandeel met de markt meebeweegt), factoren (bijvoorbeeld het
rendement van kleine min grote aandelen) en mean-variance (portefeuillekeuze op
gemiddelde en variantie) zijn daarom natuurlijk in simpele rendementen.

```{warning}
De twee zijn niet uitwisselbaar, en het verschil is van de tweede orde, niet van
de derde. Uit $\log(1+x) = x - x^2/2 + O(x^3)$ volgt dat een maandrendement van
10% een logrendement van 9,53% geeft: een verschil van bijna een halve
procentpunt in één maand. Wie een eeuw lang elke maand 10% simpel als 10% log
boekt, overschat het eindvermogen met een factor $e^{0{,}0047 \times 1200}
\approx 280$. Wie een regressie op logrendementen leest als een regressie op
simpele rendementen, vindt zo makkelijk een alpha (een rendement dat het model
niet verklaart) die er niet is, of mist er een.
```

### Meetkundig, rekenkundig en de variance drag

Hoeveel lager ligt het meetkundig gemiddelde dan het rekenkundige? *Waarom zou
dit waar zijn?* Een belegger die jaar na jaar zijn vermogen laat staan, verdient
geen gemiddelde maar een product. Verlies doet dan onevenredig veel pijn: na een
daling van 50% is een stijging van 100% nodig om terug te zijn. Het rekenkundig
gemiddelde ziet dat niet, want het behandelt $-50\%$ en $+100\%$ als een
symmetrisch paar. Hoe groter de schommelingen, hoe verder wat hij overhoudt
achterblijft bij wat hij gemiddeld verdient. Dat gat groeit dus met de variantie,
en het blijkt een halve variantie te zijn.

:::{prf:theorem} Variance drag
:label: thm-rendementen-drag

Zij $\ell_{t+1} = \log R_{t+1}$ normaal verdeeld met gemiddelde $\nu$ en
variantie $\sigma_\ell^2$, onafhankelijk en gelijk verdeeld over de tijd. Dan is het verwachte
simpele bruto rendement

```{math}
:label: eq-rendementen-lognormaal
\E[R_{t+1}] = \exp\!\left(\nu + \tfrac{1}{2}\sigma_\ell^{2}\right),
```

en dus geldt voor het *verwachte* simpele netto rendement $\mu_a$ en het
meetkundige groeitempo $\mu_g = e^{\nu}-1$ de relatie

```{math}
:label: eq-rendementen-drag
\log(1+\mu_a) = \log(1+\mu_g) + \tfrac{1}{2}\sigma_\ell^{2},
\qquad\text{ofwel}\qquad
\mu_g \approx \mu_a - \tfrac{1}{2}\sigma^{2} .
```
:::

In woorden: het verwachte rendement ligt een halve variantie boven het
meetkundige groeitempo. Een gevolg: het gerealiseerde meetkundig gemiddelde over
$T$ perioden convergeert bijna zeker naar $\mu_g$ en niet naar $\mu_a$, dus een
lang pad groeit met het lagere tempo. Het bewijs gebruikt de momentgenererende
functie van de normale verdeling en de wet van de grote aantallen. Het staat
ingeklapt.

Over de namen: het *meetkundig gemiddelde* is het gerealiseerde groeitempo van
een vermogen, en $\mu_g$ is waar het naartoe convergeert. In tabellen heet het
ook samengesteld rendement. Het gemiddelde logrendement $\nu$ is hetzelfde op
logschaal, want $\mu_g = e^{\nu}-1$. In continue tijd heet $\nu$ de drift.

:::{prf:proof}
:class: dropdown

De momentgenererende functie van een normale variabele geeft
$\E[e^{\ell}] = e^{\nu + \sigma_\ell^2/2}$, wat
[](#eq-rendementen-lognormaal) is. Logaritme nemen van beide zijden levert
$\log \E[R] = \nu + \sigma_\ell^2/2$. Omdat $\E[R] = 1+\mu_a$ en
$e^{\nu} = 1+\mu_g$, is dat [](#eq-rendementen-drag). De benadering volgt uit
$\log(1+x)\approx x$ voor kleine $x$ en $\sigma_\ell \approx \sigma$.

Voor het gevolg: het gerealiseerde meetkundig gemiddelde is
$\exp\!\big(T^{-1}\sum_t \ell_t\big)-1$. Omdat de $\ell_t$ volgens de aanname
onafhankelijk en gelijk verdeeld zijn, geeft de sterke wet van de grote
aantallen $T^{-1}\sum_t \ell_t \to \nu$ bijna zeker. $\square$
:::

Het toy-voorbeeld liet het al zien: $5\% - 1{,}75\% = 3{,}25\%$, tegen exact
$3{,}23\%$. Zoals de intuïtie voorspelde, groeit het gat met de schommelingen.
Een kleinere variantie maakt het gat kleiner, een grotere maakt het groter.

Welk van de twee gemiddelden is dan het juiste? Het rekenkundig gemiddelde is de
zuivere schatter van $\E[R_{t+1}]$. Dat is de grootheid die in elke
waarderingsvergelijking van deze reeks staat. Die vergelijking,
$p_t = \E_t[m_{t+1}x_{t+1}]$, zegt dat een prijs de verwachte payoff $x$ is
(bij een aandeel: koers plus dividend volgend jaar), gewogen met een
discontofactor $m$ (hoog in slechte tijden, als een euro extra veel waard is).
Ze gaat over verwachtingen en niet over gerealiseerde groeipaden. Maar het
rekenkundig gemiddelde is *niet* wat een belegger na dertig jaar overhoudt.
Beide getallen zijn goed, alleen beantwoorden ze verschillende vragen. Bij
$\sigma = 20\%$ schelen ze $0{,}20^2/2 = 2$ procentpunt per jaar, en over een
eeuw is dat de factor $1{,}02^{100} \approx 7{,}2$ uit de intuïtie.

```{note}
De lognormale aanname in [](#thm-rendementen-drag) is een gemak, geen
noodzaak. Voor elke verdeling geldt via Jensens ongelijkheid
$\E[\log R] \le \log \E[R]$, met gelijkheid alleen als $R$ vastligt. De halve
variantie is de tweede-ordeterm van die ongelijkheid. Normaliteit voegt alleen
toe dat alle hogere termen exact nul zijn.
```

### Annualisatie en de wortel-$t$-regel

Hoe groeien verwachting en standaarddeviatie met de horizon? *Waarom zou dit waar
zijn?* Een belegger die een aandeel $k$ jaar vasthoudt, ziet goede en slechte
jaren elkaar deels opheffen. Zijn verwachte opbrengst groeit mee met het aantal
jaren, maar zijn standaarddeviatie groeit trager, met de wortel ervan. Twee
muntworpen geven om dezelfde reden niet twee keer zoveel standaarddeviatie als één, maar
$\sqrt2$ keer zoveel.

Zij $\ell_{t+1}$ onafhankelijk en identiek verdeeld met gemiddelde $\nu$ en
variantie $\sigma_\ell^2$ per periode. Uit [](#eq-rendementen-additief) volgt
dan

```{math}
:label: eq-rendementen-wortelt
\E\!\left[\ell_{t\to t+k}\right] = k\,\nu,
\qquad
\Var\!\left(\ell_{t\to t+k}\right) = k\,\sigma_\ell^{2},
\qquad
\SD\!\left(\ell_{t\to t+k}\right) = \sqrt{k}\,\sigma_\ell .
```

In woorden: over $k$ perioden groeien de verwachting en de variantie met $k$, de
standaarddeviatie met $\sqrt{k}$. Met $n$ perioden per jaar ($n = 12$ voor
maanddata, $252$ voor dagdata) zijn de geannualiseerde grootheden dus
$n\bar\ell$ en $\sqrt{n}\,\hat\sigma_\ell$. Dat is de conventie van
`hap.summary_stats` en van de hele literatuur.

Het gemiddelde wordt met $n$ vermenigvuldigd, de standaarddeviatie met
$\sqrt{n}$. Uit die asymmetrie volgt de rest van de lecture. Een maat die haar
zichtbaar maakt, is de *Sharpe-ratio*: verwacht rendement gedeeld door
standaarddeviatie, hier $\nu\sqrt{k}/\sigma_\ell$ over $k$ perioden. Die groeit
met $\sqrt{k}$. Op dagbasis is de verwachte beweging van de markt ongeveer 0,04%
en de standaarddeviatie ruim 1%, een Sharpe-ratio van ongeveer 0,04. Op
jaarbasis is dat $0{,}04 \times \sqrt{252} \approx 0{,}6$. Over een dag is het
signaal dus een dertigste van de ruis, over een jaar ruim de helft.

```{warning}
De $\sqrt{k}$-regel volgt uit onafhankelijkheid en is geen natuurwet. Bij
positieve autocorrelatie groeit de variantie sneller dan lineair, bij negatieve
langzamer. Dat meet de variance-ratiotoets. Daarom is de bewering dat tijd risico
wegdiversifieert een onbewezen stelling en geen rekensom.
```

(sec-rendementen-standaardfout)=

### Het kernresultaat: de standaardfout van 2%

Hoe goed is een gemiddeld rendement te schatten? *Waarom zou dit waar zijn?* Een
onderzoeker die $T$ jaren middelt, laat de toevallige goede en slechte jaren
tegen elkaar wegvallen. De standaardfout van zijn gemiddelde daalt daardoor met
$\sqrt{T}$, niet met $T$. In de finance knelt dat, omdat de volatiliteit groot
is, de premie klein, en het aantal jaren begrensd door de geschiedenis.

:::{prf:theorem} De standaardfout van het gemiddelde rendement
:label: thm-rendementen-se

Zij $r_1,\dots,r_T$ onafhankelijk en identiek verdeeld met gemiddelde $\mu$ en
standaarddeviatie $\sigma$. Dan is $\bar r = T^{-1}\sum_t r_t$ zuiver en

```{math}
:label: eq-rendementen-se
\SD(\bar r) = \frac{\sigma}{\sqrt{T}} .
```
:::

:::{prf:proof}
$\Var(\bar r) = T^{-2}\sum_t \Var(r_t) = \sigma^2/T$ wegens onafhankelijkheid.
$\square$
:::

Een gevolg: de $t$-waarde van het gemiddelde is $\mu\sqrt{T}/\sigma$. Stel die
gelijk aan $t$ en los op naar $T$. Het aantal perioden dat nodig is om $\mu$ met
$t$ standaardfouten van nul te onderscheiden, is dan

```{math}
:label: eq-rendementen-jaren
T^{*} = \left(\frac{t\,\sigma}{\mu}\right)^{2} .
```

Om twee hypothesen $\mu_1 > \mu_0$ van elkaar te onderscheiden, vervangt men
$\mu$ door $\mu_1 - \mu_0$.

In woorden: [](#eq-rendementen-se) zegt dat het gemiddelde met de wortel van het
aantal jaren nauwkeuriger wordt. [](#eq-rendementen-jaren) zegt hoeveel jaren
nodig zijn: kwadratisch meer naarmate het te vinden verschil kleiner is.

Vul de Amerikaanse getallen in. Met $\sigma = 20\%$ per jaar en $T = 100$ jaar is
$\SD(\bar r) = 20/\sqrt{100} = 2$ procentpunt. Dat is de standaardfout van 2%,
het getal waar deze reeks omheen is gebouwd. De naam zegt 2%; bedoeld is een
standaardfout van twee procentpunt op een gemiddeld rendement. In het
toy-voorbeeld was de standaardfout 13 procentpunt na drie jaar. Een eeuw brengt
hem terug tot twee, en niet verder.

Een tweezijdig 95%-interval is ongeveer twee standaardfouten naar weerszijden.
Om een geschatte premie van 6% loopt het dus van 2% tot 10%. Dat is het verschil
tussen een markt die risico nauwelijks beloont en een markt die dat royaal doet,
en de data kunnen niet kiezen.

[](#eq-rendementen-jaren) maakt dat concreet, en het antwoord heeft twee kanten.
Om een premie van 6% met $t = 2$ van *nul* te onderscheiden, zijn
$(2 \times 0{,}20/0{,}06)^2 \approx 44$ jaar nodig. Dat valt mee. Daarom
betwijfelt vrijwel niemand dat er een premie is. Maar geen interessante vraag
gaat over nul. Concurrerende verklaringen van de premie voorspellen meestal
waarden tussen 4% en 6%. Om die twee te scheiden, zijn
$(2 \times 0{,}20/0{,}02)^2 = 400$ jaar nodig, en om de premie op één
procentpunt na te kennen ook. Of er een premie is, valt te beantwoorden. Hoe
groot hij is, valt binnen het bestaan van beurzen niet te beantwoorden.

De tabel rekent [](#eq-rendementen-jaren) uit voor vijf vragen, bij
$\sigma = 20\%$.

```{code-cell} ipython3
sigma = 0.20
targets = pd.DataFrame(
    {
        "vraag": [
            "premie van 6% onderscheiden van 0 (t=2)",
            "premie van 6% onderscheiden van 4% (t=2)",
            "premie van 6% onderscheiden van 5% (t=2)",
            "standaardfout van 1 procentpunt",
            "standaardfout van 0,5 procentpunt",
        ],
        "verschil (pp)": [6.0, 2.0, 1.0, np.nan, np.nan],
        "benodigde jaren": [
            (2 * sigma / 0.06) ** 2,
            (2 * sigma / 0.02) ** 2,
            (2 * sigma / 0.01) ** 2,
            (sigma / 0.01) ** 2,
            (sigma / 0.005) ** 2,
        ],
    }
).set_index("vraag")
targets.round(0)
```

Alleen de eerste vraag past binnen een eeuw. Voor elke vraag over de *grootte*
van de premie zijn honderden tot duizenden jaren nodig.

### Merton (1980): waarom fijner meten niet helpt

Helpt het om vaker te kijken? *Waarom zou dit waar zijn?* Een onderzoeker die het
jaar opknipt in maanden, weken of minuten, verdeelt hetzelfde totale
logrendement over meer stukjes. Wegens [](#eq-rendementen-additief) is de som
van die stukjes het logrendement van begin tot eind, en dat verandert niet. De
volatiliteit meet hij daarentegen met de som van de *kwadraten* van de stukjes.
Hoe fijner hij knipt, hoe meer kwadraten, en hoe nauwkeuriger de schatting.

Dat is het argument van {cite:t}`Merton1980`, en in continue tijd is het exact.
In de stelling is $W_t$ een standaard Brownse beweging: een random walk in
continue tijd met $\Var(W_t) = t$. De drift $\nu$ is het verwachte logrendement
per jaar. De $\sigma$ in de stelling is de volatiliteit van het logrendement per
jaar, in de notatie hierboven $\sigma_\ell$; we laten de index weg omdat er in
deze stelling alleen logrendementen voorkomen.

:::{prf:theorem} Merton (1980): frequentie versus kalenderlengte
:label: thm-rendementen-merton

Zij de logprijs een Brownse beweging met drift,
$d\ell_t = \nu\,dt + \sigma\,dW_t$, waargenomen over een kalenderperiode van
lengte $T$ jaar op $n$ tijdstippen per jaar, dus met stapgrootte
$\Delta = 1/n$ en $N = nT$ waarnemingen. Dan geldt voor de
maximum-likelihoodschatters:

```{math}
:label: eq-rendementen-merton
\hat\nu = \frac{\ell_{T} - \ell_{0}}{T},
\qquad
\Var(\hat\nu) = \frac{\sigma^{2}}{T},
\qquad
\Var\!\left(\hat\sigma^{2}\right) = \frac{2\sigma^{4}}{N} = \frac{2\sigma^{4}}{nT} .
```
:::

De stelling doet één bewering: een hogere frequentie $n$ maakt de
variantieschatter nauwkeuriger, tot nul fout als $n\to\infty$, maar de
driftschatter niet, want die hangt alleen van de kalenderlengte $T$ af.

In woorden: de geschatte drift is het totale logrendement gedeeld door het
aantal jaren, en de stapjes daartussen vallen tegen elkaar weg. Daarom hangt zijn
variantie alleen van $T$ af, en die van $\hat\sigma^2$ van $N$. Het bewijs staat
ingeklapt.

:::{prf:proof}
:class: dropdown

De increments $\ell_i = \ell(i\Delta)-\ell((i-1)\Delta)$ zijn onafhankelijk en
$N(\nu\Delta, \sigma^2\Delta)$. De ML-schatter van de drift is het gemiddelde
increment gedeeld door $\Delta$:

$$
\hat\nu = \frac{1}{N\Delta}\sum_{i=1}^{N}\ell_i
        = \frac{1}{T}\left(\ell_T - \ell_0\right),
$$

want de increments telescoperen. Alleen het begin- en eindpunt komen erin voor;
alle tussenliggende waarnemingen vallen weg. De variantie is
$\Var(\ell_T-\ell_0)/T^2 = \sigma^2 T/T^2 = \sigma^2/T$, onafhankelijk van $n$.

Voor de variantie: $\hat\sigma^2 = (N\Delta)^{-1}\sum_i (\ell_i - \bar\ell)^2$.
Omdat de increments normaal zijn (dat gebruikt de Brownse beweging),
is $\sum_i(\ell_i-\bar\ell)^2/(\sigma^2\Delta) \sim \chi^2_{N-1}$. Omdat een
$\chi^2_{N-1}$ variantie $2(N-1)$ heeft, is
$\Var(\hat\sigma^2) = 2\sigma^4(N-1)/N^2 \approx 2\sigma^4/N$. $\square$
:::

De drift is een eigenschap van het *pad als geheel*. Een dataset van 26 296
dagrendementen bevat daarover evenveel informatie als twee koersen: die van juli
1926 en die van juli 2026. Alles daartussen zegt iets over de variantie. Bij
100 jaarwaarnemingen is de relatieve standaardfout van de variantie
$\sqrt{2/100} = 14\%$, bij 25 200 dagwaarnemingen 0,9%.

Zo lost de stelling de eerste voorspelling uit de intuïtie in. Net als bij de
windmeter verandert vaker meten niets aan het totaal, en alles aan wat we over de
schommeling weten.

```{note}
Dat de variantie goed te meten is en de drift niet, verklaart waarom het vak zich
zo asymmetrisch heeft ontwikkeld. Volatiliteit blijkt bovendien voorspelbaar. Dat
maakte een groot onderzoeksprogramma mogelijk: ARCH en GARCH (de volatiliteit van
morgen hangt af van de schokken van vandaag), realized volatility (de som van
gekwadrateerde intradagrendementen) en de VIX (de volatiliteit die optieprijzen
impliceren). Verwachte rendementen zijn slecht te meten. Elke uitspraak erover
blijft daarom een uitspraak over een model, niet over een meting.
```

### Wanneer de aannames niet gelden: autocorrelatie en dikke staarten

Wat blijft er over als rendementen niet onafhankelijk of niet normaal zijn? Het
antwoord vooraf: [de standaardfout van 2%](#sec-rendementen-standaardfout) blijft vrijwel staan. Autocorrelatie
maakt hem iets groter, dikke staarten laten hem ongemoeid en kosten alleen
precisie in de variantie.

**Autocorrelatie.** *Waarom zou dit waar zijn?* Een belegger die een jaar
vasthoudt, ziet goede en slechte maanden elkaar deels opheffen. Volgt op een
goede maand vaak weer een goede, dan versterken de schokken elkaar, en wordt de
standaarddeviatie over een jaar groter dan de wortel-$t$-regel zegt. Volgt op
goed vaak slecht, dan wordt ze kleiner.

Formeel is de variantie van een som de som van de varianties plus twee keer alle
covarianties. Laat $\rho_j = \Corr(\ell_t,\ell_{t-j})$ de autocorrelatie bij lag
$j$ zijn: de correlatie tussen een rendement en dat van $j$ perioden eerder. Voor
de som van $q$ opeenvolgende logrendementen geldt

```{math}
:label: eq-rendementen-vr
\Var\!\left(\sum_{j=0}^{q-1}\ell_{t-j}\right)
= q\,\sigma_\ell^{2}
  \left[1 + 2\sum_{j=1}^{q-1}\left(1-\frac{j}{q}\right)\rho_j\right] .
```

In woorden: de variantie over $q$ perioden is $q$ keer de variantie per periode,
maal een correctie voor autocorrelatie. Die correctie tussen haken is de
*variance ratio* $VR(q)$. Paren die verder uit elkaar liggen, tellen minder
zwaar, omdat er in een venster van lengte $q$ minder van passen. Onder een random
walk is $VR(q)$ één. Positieve autocorrelatie (momentum) geeft $VR > 1$,
negatieve (mean reversion) $VR < 1$. De bijbehorende toets is van
{cite:t}`LoMacKinlay1988` en zit in `hap.variance_ratio`. We gebruiken hem
hieronder, en uitvoerig in [](#01-02-bachelier).

Dezelfde correctie geldt voor de standaardfout van het gemiddelde. Met $T$
waarnemingen op één frequentie, en $\sigma$ en $VR$ op diezelfde frequentie,
wordt hij $\sigma\sqrt{VR(T)}/\sqrt{T}$ in plaats van $\sigma/\sqrt{T}$.
Positieve autocorrelatie maakt het probleem van [](#thm-rendementen-se) dus
erger, negatieve iets minder erg.

Een getal: bij Amerikaanse aandelen is de autocorrelatie van maandrendementen bij
lag 1 ongeveer $0{,}09$. Voor een maandreeks van honderd jaar, met alleen die ene
autocorrelatie, is $VR(T) \approx 1 + 2 \times 0{,}09 = 1{,}18$. De standaardfout
van het gemiddelde groeit dan met $\sqrt{1{,}18} \approx 1{,}09$, van 2,0 naar
ongeveer 2,2 procentpunt. Die correctie verandert de conclusie niet. Een
autocorrelatie van 0,09 is wel groot genoeg voor een hele literatuur over
voorspelbaarheid op korte termijn.

**Dikke staarten.** Rendementen zijn niet normaal verdeeld.
{cite:t}`Mandelbrot1963` en {cite:t}`Fama1965` lieten zien dat dagelijkse
prijsveranderingen veel te veel massa in de staarten hebben. Uitslagen van vijf
standaarddeviaties komen veel vaker voor dan de eens in de tienduizend jaar die
normaliteit voorspelt. De *kurtosis* $\kappa = \E[(\ell-\nu)^4]/\sigma^4$ (het
vierde gestandaardiseerde moment, onder normaliteit gelijk aan drie) van
dagelijkse marktrendementen is in onze data ruim negentien. De *excess kurtosis*
is de kurtosis min drie: nul onder normaliteit en ruim zestien voor
dagrendementen. Tabellen rapporteren meestal die.

Bij dikke staarten zijn de formules van Merton benaderingen. De variantieschatter
is een gemiddelde van $N$ gekwadrateerde afwijkingen. Eén zo'n kwadraat heeft
variantie $\E[(\ell-\nu)^4] - \sigma^4 = (\kappa - 1)\sigma^4$, dus het gemiddelde
van $N$ stuks heeft variantie $\sigma^4(\kappa-1)/N$. Onder normaliteit is
$\kappa = 3$, en dan staat er de $2\sigma^4/N$ van Merton. De conclusie over de
drift blijft staan: geen enkele schatter haalt uit de tussenliggende koersen
informatie die er niet in zit.

Voor deze lecture valt het gevolg mee. Vergelijk de twee standaardfouten:

$$
\Var(\bar r) = \frac{\sigma^{2}}{T},
\qquad
\Var(\hat\sigma^{2}) = \frac{\sigma^{4}(\kappa-1)}{N} .
$$

De eerste hangt alleen van $\sigma$ af en blijft gelijk, hoe dik de staarten ook
zijn, zolang de variantie eindig is. De tweede hangt wél van de kurtosis af. Bij
$\kappa \approx 19$ is de standaardfout van de variantieschatting
$\sqrt{18/2} = 3$ keer zo groot als onder normaliteit. Dikke staarten kosten dus
alleen precisie in de grootheid die we al goed kenden.

```{warning}
Eén uitzondering doet er echt toe. Mandelbrot stelde oorspronkelijk een stabiele
Paretiaanse verdeling voor met staartindex $\alpha < 2$. De staartindex zegt hoe
snel de kans op een uitschieter afneemt: $P(|r| > x)$ daalt als $x^{-\alpha}$, dus
hoe kleiner $\alpha$, hoe dikker de staart. Bij $\alpha < 2$ *bestaat* de
variantie niet, en werkt de centrale limietstelling niet meer. Met veel meer
data is de consensus nu dat de staartindex van aandelenrendementen rond de drie
tot vier ligt: dikke staarten, maar een eindige variantie.
[](#thm-rendementen-se) blijft dus geldig. De convergentie naar normaliteit is
wel traag, zodat $t$-waarden in kleine steekproeven te optimistisch zijn.
```

```{admonition} Samengevat
:class: tip

- Het meetkundig gemiddelde ligt een halve variantie onder het rekenkundige,
  [](#eq-rendementen-drag).

- Over de tijd tellen logrendementen op, [](#eq-rendementen-additief). Daardoor
  groeit de standaarddeviatie met $\sqrt{k}$, [](#eq-rendementen-wortelt).

- De standaardfout van het gemiddelde is $\sigma/\sqrt{T}$,
  [](#eq-rendementen-se). Bij $\sigma = 20\%$ en een eeuw data is dat
  [de standaardfout van 2%](#sec-rendementen-standaardfout).

- Die precisie hangt alleen af van de kalenderlengte, die van de variantie ook
  van de frequentie, [](#eq-rendementen-merton).

- De simulatie hierna vraagt: wat gebeurt er met beide standaardfouten als we
  dezelfde honderd jaar steeds fijner bekijken?
```

## Simulatie: de frequentie van waarnemen

We bouwen een wereld waarin logprijzen een Brownse beweging volgen met een drift
van 8% en een volatiliteit van 20% per jaar. Dat is de kalibratie van
[de standaardfout van 2%](#sec-rendementen-standaardfout). De drift is een
totaalrendement, geen premie. Per constructie kennen we beide parameters. De
vraag over steekproeven: wat gebeurt er met de twee schatters als we dezelfde
honderd jaar steeds fijner bekijken?

We genereren tweeduizend paden van honderd jaar op dagbasis, met 252 stappen per
jaar, en bekijken elk pad jaarlijks, per kwartaal, per maand en per dag. Alleen
de waarnemingsfrequentie verschilt. Per frequentie schatten we het
geannualiseerde gemiddelde en de variantie. De stappen zijn logrendementen, dus
het geschatte gemiddelde is de geschatte drift. De cel simuleert in acht blokken,
om geheugen te sparen.

```{code-cell} ipython3
n_paths, n_years, per_year = 2000, 100, 252
nu, sigma_true = 0.08, 0.20
freqs = {"jaarlijks": 1, "kwartaal": 4, "maandelijks": 12, "dagelijks": 252}

means = {name: [] for name in freqs}
variances = {name: [] for name in freqs}

for block in np.array_split(np.arange(n_paths), 8):
    steps = rng.normal(
        nu / per_year, sigma_true / np.sqrt(per_year),
        size=(len(block), n_years, per_year),
    )
    for name, k in freqs.items():
        # tel per blok van per_year // k dagen de logrendementen op
        agg = steps.reshape(len(block), n_years * k, per_year // k).sum(axis=2)
        means[name].append(agg.mean(axis=1) * k)
        variances[name].append(agg.var(axis=1, ddof=1) * k)

means = {name: np.concatenate(v) for name, v in means.items()}
variances = {name: np.concatenate(v) for name, v in variances.items()}
```

Per frequentie hebben we nu tweeduizend geschatte gemiddelden en varianties. De
tabel zet hun standaarddeviatie naast de theorie.

```{code-cell} ipython3
frequency = pd.DataFrame(
    {
        "waarnemingen": [n_years * k for k in freqs.values()],
        "SD(gemiddelde), pp": [means[n].std(ddof=1) * 100 for n in freqs],
        "theorie: sigma/sqrt(T), pp": [sigma_true / np.sqrt(n_years) * 100] * 4,
        "SD(variantie)/variantie": [
            variances[n].std(ddof=1) / sigma_true**2 for n in freqs
        ],
        "theorie: sqrt(2/N)": [
            np.sqrt(2 / (n_years * k)) for k in freqs.values()
        ],
    },
    index=list(freqs),
)
frequency.round(4)
```

Het aantal waarnemingen groeit met een factor 252, maar de standaardfout van het
gemiddelde staat stil op twee procentpunt. Hij is niet *ongeveer* gelijk maar
exact gelijk. Volgens [](#eq-rendementen-merton) is de schatter bij elke
frequentie dezelfde functie van het pad: eindpunt min beginpunt, gedeeld door
honderd.

De relatieve fout van de variantieschatting daalt intussen van 14% naar 0,9%,
zoals $\sqrt{2/N}$ voorspelt. Met de 23% volatiliteit van het toy-voorbeeld zou
de standaardfout van het gemiddelde $23/\sqrt{100} = 2{,}3$ procentpunt zijn in
plaats van 2,0. De figuur laat beide kolommen zien voor de twee uitersten,
jaarlijks en dagelijks. Let op de breedte van de histogrammen links en rechts.

```{code-cell} ipython3
:label: cel-rendementen-frequentie
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=False)

axes[0].hist(means["jaarlijks"] * 100, bins=50, alpha=0.65,
             label="jaarlijks (100 obs.)", edgecolor="white")
axes[0].hist(means["dagelijks"] * 100, bins=50, alpha=0.65,
             label="dagelijks (25 200 obs.)", edgecolor="white")
axes[0].axvline(nu * 100, color="black", lw=1.4)
axes[0].set_title("Geschat gemiddelde")
axes[0].set_xlabel("Geschatte drift (procent per jaar)")
axes[0].set_ylabel("Aantal paden")
axes[0].legend()

axes[1].hist(np.sqrt(variances["jaarlijks"]) * 100, bins=50, alpha=0.65,
             label="jaarlijks (100 obs.)", edgecolor="white")
axes[1].hist(np.sqrt(variances["dagelijks"]) * 100, bins=50, alpha=0.65,
             label="dagelijks (25 200 obs.)", edgecolor="white")
axes[1].axvline(sigma_true * 100, color="black", lw=1.4)
axes[1].set_title("Geschatte volatiliteit")
axes[1].set_xlabel("Geschatte volatiliteit (procent per jaar)")
axes[1].set_ylabel("Aantal paden")
axes[1].legend()

fig.tight_layout()
plt.show()
```

:::{figure} #cel-rendementen-frequentie
:label: fig-rendementen-frequentie
:width: 100%

Tweeduizend keer honderd jaar, twee keer bekeken. Links: de verdeling van het
geschatte gemiddelde rendement is bij jaarlijkse en dagelijkse waarneming
dezelfde; de twee histogrammen liggen exact over elkaar. Rechts: de verdeling
van de geschatte volatiliteit krimpt bij dagelijkse waarneming tot een streep.
Dezelfde paden krijgen 250 keer zoveel getallen, en alle extra informatie gaat
naar de variantie.
:::

De figuur bevestigt de tabel: links blijft de verdeling van het gemiddelde even
breed, rechts krimpt die van de volatiliteit. Betere methoden nemen deze
asymmetrie niet weg. Wie een verwacht rendement wil kennen, heeft geschiedenis
nodig, en die komt op één snelheid binnen.

```{warning}
Een verleidelijke fout: met 25 200 waarnemingen zou $t = 2$ al $p < 0{,}05$
betekenen. Voor een uitspraak over een gemiddeld rendement is de effectieve
steekproefomvang echter het aantal *jaren*, niet het aantal waarnemingen. Wie
een $t$-waarde op dagrendementen zonder die kanttekening rapporteert, geeft de
onzekerheid van iets anders dan hij beweert te meten.
```

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Lawrence Fisher & James H. Lorie, *Rates of Return on Investments in
Common Stocks*, The Journal of Business 37(1), 1964, 1–21
{cite}`FisherLorie1964`.

**Wat.** Het hoofdresultaat: een belastingvrije belegger die in januari 1926 een
gelijk bedrag in elk NYSE-aandeel stak en dividenden herbelegde, haalde tot en
met december 1960 een meetkundig gemiddelde van 9,0% per jaar. Het getal zonder
herbelegging, 6,9%, repliceren we niet.

**Data hier.** De maandelijkse value-weighted markt en de equal-weighted
size-decielen uit de Kenneth French Data Library, juli 1926 tot en met december
1960.

**Verschil met het origineel.** French begint zes maanden later en herbalanceert
maandelijks, terwijl Fisher en Lorie gelijke bedragen kochten en vasthielden. Wij
erven bovendien de constructiekeuzes van French, zoals de behandeling van
delistings (aandelen die van de beurs verdwijnen, bijvoorbeeld na een
faillissement).

**Verwachte afwijking.** De value-weighted markt moet binnen ongeveer één
procentpunt van 9,0% uitkomen: dezelfde beurs, dezelfde periode, dezelfde
CRSP-bron. De equal-weighted variant moet *hoger* uitkomen, omdat kleine aandelen
het in deze periode beter deden. Komt hij lager uit, dan zit er een fout in de
code.
```

We laden de twee reeksen. Reekscodes en de verschillen in steekproef staan in
het commentaar.

```{code-cell} ipython3
# Value-weighted markt: Mkt = Mkt-RF + RF uit de French-factoren.
# Equal-weighted: gemiddelde van de tien equal-weighted size-decielen
# (Portfolios_Formed_on_ME). French begint in 1926-07, Fisher en Lorie in 1926-01:
# 414 in plaats van 420 maanden. Maandelijks herbalanceren van kleine aandelen
# verhoogt het gemeten rendement (bid-ask bounce, rebalanceringspremie).
deciles = ["Lo 10", "2-Dec", "3-Dec", "4-Dec", "5-Dec", "6-Dec",
           "7-Dec", "8-Dec", "9-Dec", "Hi 10"]
size_ew = hap_data.french("Portfolios_Formed_on_ME", "monthly", table="Equal-Weight")

sample = slice("1926-07", "1960-12")
value_weighted = hap_data.market_monthly()["Mkt"].loc[sample]
equal_weighted = size_ew[deciles].loc[sample].mean(axis=1)
```

Per reeks berekenen we het meetkundig en het rekenkundig gemiddelde per jaar, de
volatiliteit en de standaardfout van het gemiddelde. De kolom
"samengesteld (meetk.)" is het meetkundig gemiddelde.

```{code-cell} ipython3
def annual_summary(returns: pd.Series) -> dict[str, float]:
    """Compounded and arithmetic annual return with the standard error."""
    n_months = len(returns)
    years = n_months / 12
    sd_ann = returns.std(ddof=1) * np.sqrt(12)
    return {
        "maanden": n_months,
        "samengesteld (meetk.)": (1 + returns).prod() ** (1 / years) - 1,
        "rekenkundig": 12 * returns.mean(),
        "volatiliteit": sd_ann,
        "SE van het gemiddelde": sd_ann / np.sqrt(years),
    }


fisher_lorie = pd.DataFrame(
    {
        "value-weighted markt": annual_summary(value_weighted),
        "equal-weighted (10 size-decielen)": annual_summary(equal_weighted),
    }
).T
fisher_lorie.round(4)
```

De standaardfout van het gemiddelde is 3,9 procentpunt voor de value-weighted
reeks en 5,5 voor de equal-weighted reeks. Die standaardfouten veronderstellen
onafhankelijke maandrendementen. Met een autocorrelatie van 0,09 bij lag 1 zouden
ze ongeveer 9% groter zijn.

De volatiliteit van de value-weighted markt is 22,9%, bijna exact de 23% van het
toy-voorbeeld. Het verschil tussen rekenkundig en meetkundig gemiddelde, ruim
twee procentpunt, is de variance drag uit de theorie: in de orde van de halve
variantie, $0{,}229^2/2 \approx 2{,}6$ procentpunt.

Welke reeks is de tegenhanger van de 9,0%? Fisher en Lorie kochten gelijke
bedragen en hielden vast. Zonder herbalanceren groeien de winnaars uit tot grote
posities, zodat zo'n portefeuille na enkele jaren meer op de value-weighted markt
lijkt dan op een maandelijks herbalanceerde equal-weighted portefeuille. De
value-weighted reeks is daarom de replicatie, zoals het replicatieblok
aankondigde. De equal-weighted reeks controleert het teken. De tabel hieronder
zet het meetkundig gemiddelde van beide naast het gepubliceerde getal.

```{code-cell} ipython3
published = 0.090    # Fisher en Lorie (1964), met herbelegde dividenden
replicated = fisher_lorie["samengesteld (meetk.)"]

pd.DataFrame(
    {"origineel": published, "hier": replicated, "verschil": replicated - published}
).round(4)
```

**Geslaagd.** De value-weighted markt geeft een meetkundig gemiddelde van 9,46%,
tegen de gepubliceerde 9,0%. Het replicatieblok verwachtte een verschil van
hooguit één procentpunt; het is een halve procentpunt, bij een periode die zes
maanden korter is en een andere weging. Het blok verwachtte ook dat de
equal-weighted variant hoger zou uitkomen. Met 12,9% is dat zo.

Die 12,9% ligt bijna vier procentpunt boven wat Fisher en Lorie met gelijke
bedragen vonden. Dat is geen meetfout maar het effect van maandelijks
herbalanceren in het kleinste deciel. Bij kleine aandelen springt de slotkoers
tussen bied- en laatprijs (bid-ask bounce). Herbalanceren naar gelijke gewichten
koopt na elke daling bij en verkoopt na elke stijging, en boekt die sprongen als
rendement: de rebalanceringspremie. Dat verschil van vier procentpunt is een
vroege waarschuwing dat equal-weighted geen eenduidige instructie is.

Dan de onzekerheid die in 1964 niet werd gerapporteerd. De standaardfout van 3,9
procentpunt hoort bij het rekenkundig gemiddelde van de value-weighted reeks,
11,7%. Het 95%-interval daaromheen loopt van ongeveer 4% tot 19%. Het meetkundig
gemiddelde ligt een vaste halve variantie lager en is even onzeker, dus ook het
beroemde 9,0% was op ongeveer acht procentpunt na bekend. De eerste betrouwbare
meting van het aandelenrendement zei dus weinig meer dan dat het positief was.

De figuur toont het pad van één dollar over dezelfde periode. Let op waar de twee
lijnen eindigen ten opzichte van de stippellijn, en op de val van 1929–1932.

```{code-cell} ipython3
:label: cel-rendementen-fisherlorie
:tags: [hide-input]

cumulative = pd.DataFrame(
    {"value-weighted": (1 + value_weighted).cumprod(),
     "equal-weighted": (1 + equal_weighted).cumprod()}
)

fig, ax = plt.subplots()
for column, color in zip(cumulative.columns, hap.plotting.COLORS):
    ax.plot(cumulative.index, cumulative[column], label=column, color=color)
ax.set_yscale("log")
ax.axhline(1.09 ** (len(value_weighted) / 12), color="black", ls="--", lw=1.0,
           label="Fisher-Lorie: 9,0% per jaar")
ax.set_title("Eén dollar in Amerikaanse aandelen, juli 1926 - december 1960")
ax.set_xlabel("Jaar")
ax.set_ylabel("Waarde (log-schaal)")
ax.legend()
hap.plotting.timeline_axis(ax)
plt.show()
```

:::{figure} #cel-rendementen-fisherlorie
:label: fig-rendementen-fisherlorie
:width: 90%

De periode die Fisher en Lorie bekeken. De stippellijn markeert het eindvermogen
dat bij hun 9,0% per jaar hoort. De value-weighted reeks eindigt er vlak boven,
de equal-weighted reeks ver erboven. De crash van 1929–1932, een terugval van
meer dan 80%, zit er volledig in. Daarom vonden tijdgenoten het resultaat
opzienbarend: zelfs met de Grote Depressie erbij was het langetermijnrendement
op aandelen ruim positief.
:::

### Dezelfde eeuw, maand- en dagdata

Dagdata verbeteren de standaardfout van het gemiddelde nauwelijks, zoals de
stelling van Merton voorspelt. We nemen de volledige French-reeks van juli 1926
tot juli 2026, één keer op maandbasis en één keer op dagbasis, en zetten de
geannualiseerde grootheden naast elkaar.

```{code-cell} ipython3
market_monthly = hap_data.market_monthly()["Mkt"].rename("markt, maandelijks")
market_daily = hap_data.market_daily()["Mkt"].rename("markt, dagelijks")

comparison = pd.concat(
    [
        hap.summary_stats(market_monthly, "monthly"),
        hap.summary_stats(market_daily, "daily"),
    ]
)[["nobs", "mean_ann", "std_ann", "se_mean_ann", "skew", "kurtosis"]]
comparison.round(4)
```

De kolommen zijn het aantal waarnemingen (`nobs`), het geannualiseerde
rekenkundig gemiddelde (`mean_ann`), de volatiliteit (`std_ann`), de
standaardfout van het gemiddelde (`se_mean_ann`), de scheefheid (`skew`) en de
excess kurtosis (`kurtosis`).

De dagreeks heeft tweeëntwintig keer zoveel waarnemingen, maar de standaardfout
van het gemiddelde daalt alleen van 1,83 naar 1,67 procentpunt. Dat komt niet van
het aantal waarnemingen maar van de geschatte volatiliteit.

Die valt op dagbasis lager uit, 17,1% tegen 18,3%, omdat de maandreeks positieve
autocorrelatie bevat. Het verschil is van dezelfde orde als de correctie uit
[](#eq-rendementen-vr): klein, maar zichtbaar. De informatie over het gemiddelde
is dezelfde.

De excess kurtosis springt intussen van 7,4 naar 16,1. De dagreeks vertelt veel
meer over de staarten en niets meer over het midden.

### Wat er wél in de data zit: clustering en de random walk

Het rendement zelf heeft nauwelijks geheugen, de volatiliteit wel. We laten dat
zien met twee diagnoses: de autocorrelatie van het rendement, en die van de
volatiliteit, gemeten als het absolute rendement.

```{code-cell} ipython3
log_daily = np.log1p(hap_data.market_daily()["Mkt"].dropna())
log_monthly = np.log1p(hap_data.market_monthly()["Mkt"].dropna())

diagnostics = pd.DataFrame(
    {
        "autocorr. rendement (dag)": [log_daily.autocorr(k) for k in range(1, 7)],
        "autocorr. |rendement| (dag)": [log_daily.abs().autocorr(k) for k in range(1, 7)],
        "autocorr. rendement (maand)": [log_monthly.autocorr(k) for k in range(1, 7)],
    },
    index=pd.Index(range(1, 7), name="lag"),
)
diagnostics.round(3)
```

De rendementen zelf zijn nauwelijks gecorreleerd, de absolute rendementen sterk.
De variance ratios toetsen het eerste formeel, voor horizonnen tot vijf jaar.

```{code-cell} ipython3
variance_ratios = pd.DataFrame(
    [hap.variance_ratio(log_monthly, q) for q in (2, 3, 6, 12, 24, 60)],
    index=pd.Index([2, 3, 6, 12, 24, 60], name="horizon q (maanden)"),
)[["vr", "z2", "pvalue"]]
variance_ratios.round(3)
```

Geen enkele variance ratio wijkt significant van één af: alle $p$-waarden liggen
boven 0,05. In de tabel is `vr` de variance ratio, `z2` de toetsgrootheid van Lo
en MacKinlay die robuust is voor wisselende volatiliteit, en `pvalue` de
bijbehorende tweezijdige $p$-waarde.

Beide tabellen wijzen dezelfde kant op: het rendement zelf heeft nauwelijks
geheugen. De autocorrelatie van het rendement is bij elke lag kleiner dan 0,09,
en bij de meeste kleiner dan 0,03. De variance ratios liggen tussen 0,97 en 1,20.
Het rendement gedraagt zich als een random walk, zoals
[](#eq-rendementen-wortelt) aanneemt.

De autocorrelatie van de *absolute* rendementen is daarentegen ongeveer 0,30,
bij lag 1 en nog steeds bij lag 6. Volatiliteit klontert, dag na dag, en dat
verdwijnt niet. Daarmee staat de asymmetrie tussen gemiddelde en variantie nog
één keer in de data. De grootheid die we goed kunnen meten, is ook voorspelbaar.
De grootheid die we slecht kunnen meten, vertoont geen patroon.

### Honderdvijftig jaar, met dezelfde conclusie

Anderhalve eeuw data brengt de standaardfout van het gemiddelde niet verder dan
1,45 procentpunt, en bevestigt de variance drag. Shillers reeks gaat terug tot
1871 en bevat de consumentenprijsindex, zodat we naar *reële* totaalrendementen
kunnen kijken.

```{code-cell} ipython3
real_index = hap_data.shiller()["real_total_return_price"].dropna()
annual_real = real_index.resample("YE").last().pct_change().dropna()
annual_real = annual_real[annual_real.index.year <= 2025]

long_run = pd.DataFrame(
    {
        "waarde": [
            len(annual_real),
            annual_real.mean(),
            (1 + annual_real).prod() ** (1 / len(annual_real)) - 1,
            annual_real.std(ddof=1),
            annual_real.std(ddof=1) ** 2 / 2,
            annual_real.std(ddof=1) / np.sqrt(len(annual_real)),
            annual_real.kurtosis(),
            annual_real.autocorr(1),
        ]
    },
    index=["aantal jaren", "rekenkundig gemiddelde", "meetkundig gemiddelde",
           "standaarddeviatie", "halve variantie", "standaardfout van het gemiddelde",
           "excess kurtosis", "autocorrelatie lag 1"],
).round(4)
long_run
```

Honderdvierenvijftig jaar reëel totaalrendement bevestigen
[](#thm-rendementen-drag). Het rekenkundig gemiddelde is 8,64%, het meetkundig
gemiddelde 7,06%. Hun verschil van 1,58 procentpunt ligt drie honderdste
procentpunt van de halve variantie in de tabel.

De excess kurtosis is 0,01. *Jaarlijkse* rendementen zijn vrijwel normaal
verdeeld, omdat de dikke staarten van de dagreeks bij aggregatie uitmiddelen. De
autocorrelatie is verwaarloosbaar. De standaardfout van het gemiddelde is na
anderhalve eeuw nog 1,45 procentpunt.

## Wat er brak, en wat daarna kwam

**Wat de meetlat oplevert.** Een compleet en sluitend apparaat. Met
[](#eq-rendementen-additief), [](#eq-rendementen-wortelt) en
[](#eq-rendementen-se) wordt elke bewering over gemiddelde rendementen een
uitspraak met een standaardfout erbij. Die vertaling vraagt geen model, geen
aanname over voorkeuren en geen theorie. Elke grootheid die het vak gebruikt, is
hier gedefinieerd, en van elke schatter is de precisie bekend. Weinig
vakgebieden kunnen dat van hun meetlat zeggen.

**Waar het breekt.** Juist waar het instrument scherp genoeg is om zijn eigen
grenzen te tonen. De replicatie gaf over 1926–1960 een meetkundig gemiddeld
marktrendement van 9,46% met een standaardfout van 3,9 procentpunt, en over de
hele eeuw een rekenkundig gemiddelde van 11,6% met 1,8 procentpunt. Geen
methode, frequentie of dataset verbetert dat, want volgens
[](#thm-rendementen-merton) zit de informatie over de drift alleen in de
kalenderlengte. Het verwachte rendement, de $\E[R]$ in elke
waarderingsvergelijking, is dus niet nauwkeuriger te meten dan op een paar
procentpunt. Alles wat in de empirische finance een puzzel heet, is uiteindelijk
een bewering over dat getal.

**Risico of vergissing?** Dat is de vaste vraag van de reeks: komt een afwijkend
rendement van risico of van een vergissing? Deze lecture laat zien waarom die
vraag zo hardnekkig is. Stel dat de markt in 1932 goedkoop was. Volgens de
Chicago-lezing (Fama en zijn school: prijzen zijn juist, het verwachte rendement
varieert met het risico) eisten beleggers een hogere vergoeding, zodat het
verwachte rendement hoger was dan normaal. Volgens de Yale-lezing (Shiller en
zijn school: prijzen kunnen ernaast zitten) waren beleggers in paniek, en zat de
prijs ernaast. Om die twee te scheiden, moet het verwachte rendement van 1932
apart *gemeten* worden. Volgens [](#eq-rendementen-jaren) kost een verschil van
twee procentpunt vierhonderd jaar, en een crisis duurt er hooguit een paar. De
kampen zijn het over de data niet oneens. De data zijn alleen te dun om tussen
hen te kiezen. Waar een lecture in deze reeks toch kiest, kiest ze op grond van
een model, want een meting is er niet.

**Wat er daarna kwam.** De formules van deze lecture komen niet uit een
statistiekboek maar van een handelsvloer. In 1863 publiceerde een Parijse
beursemployé de observatie dat de koersuitslag met de wortel van de tijd groeit,
de regel van [](#eq-rendementen-wortelt). Dat was 37 jaar vóór Bachelier en 42
jaar vóór Einstein. Daarover gaat [](#01-02-bachelier): de wortel-$t$-wet als
empirisch feit, de Brownse beweging als model erachter, en de eerste toetsen of
koersen geheugenloos zijn.

## Oefeningen

:::{exercise}
:label: ex-rendementen-instap

**Instap: het toy-voorbeeld gevarieerd.**

1. Zet de drie rendementen in omgekeerde volgorde: $+10\%$, $-20\%$, $+25\%$.
   Welke getallen uit het toy-voorbeeld veranderen?

2. Vervang $-20\%$ door $-30\%$. Bereken het rekenkundig en het meetkundig
   gemiddelde en de halve variantie. Wordt het verschil tussen de twee
   gemiddelden groter of kleiner, en waarom?
:::

:::{solution} ex-rendementen-instap
:class: dropdown

**(1)** Geen enkel getal. De som, het product en de variantie hangen niet af van
de volgorde. Alleen waar de euro begon en waar hij eindigde telt.

**(2)** Het rekenkundig gemiddelde is $(0{,}25 - 0{,}30 + 0{,}10)/3 = 0{,}016667$.
Het product van de bruto rendementen is $1{,}25 \times 0{,}70 \times 1{,}10 =
0{,}9625$, dus het meetkundig gemiddelde is $0{,}9625^{1/3} - 1 = -0{,}012660$.
De afwijkingen van het gemiddelde zijn $0{,}233333$, $-0{,}316667$ en
$0{,}083333$. Hun kwadraten tellen op tot $0{,}161667$. Gedeeld door drie is dat
$0{,}053889$, en de halve variantie is $0{,}026944$. De cel rekent het na.

```{code-cell} ipython3
r_alt = np.array([0.25, -0.30, 0.10])
arith_alt = r_alt.mean()
geom_alt = (1 + r_alt).prod() ** (1 / len(r_alt)) - 1
half_var_alt = r_alt.var(ddof=0) / 2

pd.Series({
    "rekenkundig gemiddelde": arith_alt,
    "meetkundig gemiddelde": geom_alt,
    "halve variantie": half_var_alt,
    "variance drag (exact)": arith_alt - geom_alt,
}).round(6)
```

Het verschil groeit van 1,77 naar 2,93 procentpunt, omdat het grotere verlies
de variantie vergroot. Het rekenkundig gemiddelde is nog positief, maar de
belegger heeft geld verloren.
Wat dit leert: een positief gemiddeld rendement zegt nog niets over het vermogen
aan het eind.
:::

:::{exercise}
:label: ex-rendementen-1

**De twee standaardfouten, met de hand en met de computer.**

1. Leid [](#eq-rendementen-merton) opnieuw af, maar nu zonder continue tijd.
   Neem $N = nT$ onafhankelijke increments $\ell_i \sim N(\nu/n, \sigma^2/n)$ en
   toon aan dat de geannualiseerde schatter van het gemiddelde,
   $\hat\nu = (n/N)\sum_i \ell_i$, variantie $\sigma^2/T$ heeft, ongeacht $n$.

2. Een onderzoeker beweert dat de premie 6% is, een ander 4%. Hoeveel jaar data
   is nodig om die twee hypothesen met $t = 2$ te scheiden, bij $\sigma = 20\%$?
   En bij $\sigma = 15\%$?

3. Simuleer 20 000 steekproeven van 100 jaarlijkse rendementen met
   $\mu = 6\%$ en $\sigma = 20\%$. In welke fractie is de geschatte premie
   negatief? En in welke fractie haalt hij $t > 2$?
:::

:::{solution} ex-rendementen-1
:class: dropdown

**(1)** De som $\sum_{i=1}^{N}\ell_i$ heeft gemiddelde $N\nu/n = T\nu$ en
variantie $N\sigma^2/n = T\sigma^2$. De geannualiseerde schatter is
$\hat\nu = (1/T)\sum_i \ell_i$, dus $\E[\hat\nu] = \nu$ en
$\Var(\hat\nu) = T\sigma^2/T^2 = \sigma^2/T$. In het antwoord staat geen $n$.
Elk increment is $n$ keer kleiner en $n$ keer minder variabel, maar er zijn er
$n$ keer zoveel.

**(2)** Vul [](#eq-rendementen-jaren) in met $t = 2$ en $\mu_1 - \mu_0 = 0{,}02$:
$T^{*} = (2 \times 0{,}20/0{,}02)^2 = 400$ jaar bij $\sigma = 20\%$ en
$T^{*} = (2 \times 0{,}15/0{,}02)^2 = 225$ jaar bij $\sigma = 15\%$.

**(3)** De cel rekent (2) uit en simuleert (3).

```{code-cell} ipython3
n_sim, n_obs, mu_ex, sigma_ex = 20_000, 100, 0.06, 0.20
draws = rng.normal(mu_ex, sigma_ex, size=(n_sim, n_obs))
sample_mean = draws.mean(axis=1)
sample_t = sample_mean / (draws.std(axis=1, ddof=1) / np.sqrt(n_obs))

pd.DataFrame(
    {
        "waarde": [
            (2 * 0.20 / 0.02) ** 2,
            (2 * 0.15 / 0.02) ** 2,
            float(np.mean(sample_mean < 0)),
            float(np.mean(sample_t > 2)),
        ]
    },
    index=["jaren nodig bij sigma=20%", "jaren nodig bij sigma=15%",
           "fractie met negatieve geschatte premie", "fractie met t > 2"],
).round(4)
```

Nodig zijn 400 jaar bij $\sigma = 20\%$ en 225 bij $\sigma = 15\%$. Geen van
beide bestaat. In ongeveer 0,2% van de eeuwen
concludeert een onderzoeker met een perfect gespecificeerd model dat aandelen
minder opbrengen dan niets. In ongeveer 85% haalt hij $t > 2$. Dat is het
onderscheidend vermogen van de toets of de premie nul is, en dat is behoorlijk.
Alleen is dat niet de vraag waar iemand het antwoord op wil weten. Wat dit
leert: óf er een premie is, is met een eeuw data te beantwoorden, hoe groot hij
is niet.
:::

:::{exercise}
:label: ex-rendementen-2

**Fisher-Lorie op andere steekproeven.** Herhaal de replicatie voor drie
perioden: 1926-07 t/m 1960-12 (de originele), 1961-01 t/m 1993-12, en 1994-01
t/m 2026-07.

1. Rapporteer per periode het meetkundig en het rekenkundig gemiddelde per jaar
   van de value-weighted markt, de volatiliteit en de standaardfout van het
   gemiddelde.

2. Toets of het gemiddelde rendement van de eerste periode verschilt van dat van
   de derde. Gebruik de standaardfout van het verschil onder de aanname dat de
   perioden onafhankelijk zijn. Die aanname is hier redelijk, anders dan bij
   gelijktijdige reeksen.

3. Wat zou er waargenomen moeten worden om te concluderen dat de premie sinds
   Fisher en Lorie is veranderd?
:::

:::{solution} ex-rendementen-2
:class: dropdown

Eerst de samenvatting per periode.

```{code-cell} ipython3
periods = {
    "1926-07 / 1960-12": slice("1926-07", "1960-12"),
    "1961-01 / 1993-12": slice("1961-01", "1993-12"),
    "1994-01 / 2026-07": slice("1994-01", "2026-07"),
}
market = hap_data.market_monthly()["Mkt"]

by_period = pd.DataFrame(
    {name: annual_summary(market.loc[window]) for name, window in periods.items()}
).T
by_period.round(4)
```

Dan het verschil tussen de eerste en de laatste periode.

```{code-cell} ipython3
first, last = by_period.index[0], by_period.index[-1]
difference = by_period.loc[first, "rekenkundig"] - by_period.loc[last, "rekenkundig"]
se_difference = np.sqrt(
    by_period.loc[first, "SE van het gemiddelde"] ** 2
    + by_period.loc[last, "SE van het gemiddelde"] ** 2
)

pd.DataFrame(
    {"waarde": [difference, se_difference, difference / se_difference,
                (2 * by_period["volatiliteit"].mean() / abs(difference)) ** 2]},
    index=["verschil in rekenkundig gemiddelde", "standaardfout van het verschil",
           "t-waarde", "jaren per periode voor t=2 bij dit verschil"],
).round(4)
```

De uitkomst is opmerkelijker dan verwacht. De *rekenkundige* gemiddelden van de
drie perioden zijn 11,67%, 11,43% en 11,61%. Tussen de eerste en de laatste
periode scheelt dat zeven honderdste procentpunt, met een $t$-waarde van 0,01.

Het *meetkundig* gemiddelde loopt wél uiteen: van 9,46% naar 10,73% en
10,92%. Dat komt volledig uit [](#thm-rendementen-drag). De volatiliteit daalde
van 22,9% naar ruim 15%, en een kleinere halve variantie geeft ruim één
procentpunt meer groei bij hetzelfde verwachte rendement. Wie de twee soorten
gemiddelde door elkaar haalt, ziet hier een stijgende premie die er niet is.

Het antwoord op (3) is ontnuchterend. Bij het waargenomen verschil zou elke
periode driehonderdduizend jaar moeten duren om $t = 2$ te halen, en voor twee
procentpunt nog enkele honderden. Met rendementsdata alleen valt niet te zeggen
of de premie sinds 1964 is veranderd. Daarom benaderen latere lectures hem via *prijzen*
(waarderingsratio's) in plaats van via gerealiseerde rendementen. Wat dit leert:
een veranderd meetkundig gemiddelde is nog geen veranderde premie.
:::

:::{exercise}
:label: ex-rendementen-3

**Aggregatie en staarten.** Neem de dagelijkse marktreeks uit
`hap_data.market_daily()`.

1. Bereken de excess kurtosis van logrendementen geaggregeerd over 1, 5, 21 en
   252 handelsdagen, in niet-overlappende blokken. Wat gebeurt er?

2. Bereken voor elke horizon de relatieve standaardfout van de
   variantieschatting, één keer onder normaliteit ($\sqrt{2/N}$) en één keer met
   de waargenomen kurtosis ($\sqrt{(\kappa-1)/N}$). Hoeveel kost de dikke staart?

3. Bereken voor dezelfde horizonnen de standaardfout van het geannualiseerde
   gemiddelde. Verklaar de uitkomst met [](#thm-rendementen-merton).
:::

:::{solution} ex-rendementen-3
:class: dropdown

De cel aggregeert de dagreeks per horizon en berekent de drie grootheden.

```{code-cell} ipython3
daily_log = np.log1p(hap_data.market_daily()["Mkt"].dropna())
by_horizon = {}
for horizon in (1, 5, 21, 252):
    blocks = daily_log.to_numpy()[: len(daily_log) // horizon * horizon]
    aggregated = pd.Series(blocks.reshape(-1, horizon).sum(axis=1))
    n_obs = len(aggregated)
    excess_kurtosis = aggregated.kurtosis()
    years = n_obs * horizon / 252
    by_horizon[f"{horizon} dagen"] = {
        "waarnemingen": n_obs,
        "excess kurtosis": excess_kurtosis,
        "rel. SE variantie, normaal": np.sqrt(2 / n_obs),
        # kappa - 1 = (excess kurtosis + 3) - 1 = excess kurtosis + 2
        "rel. SE variantie, waargenomen": np.sqrt((excess_kurtosis + 2) / n_obs),
        "SE gemiddelde (pp per jaar)": (
            aggregated.std(ddof=1) * np.sqrt(252 / horizon) / np.sqrt(years) * 100
        ),
    }
pd.DataFrame(by_horizon).T.round(4)
```

De excess kurtosis daalt van 17,0 op dagbasis naar 8,5, 6,6 en 4,4 op
jaarbasis. De centrale limietstelling werkt, maar langzaam: ook op jaarbasis
zijn de staarten nog dikker dan normaal. De Shiller-reeks gaf op 154 jaar een
excess kurtosis van 0,01, maar dat is geen tegenspraak. Een kurtosis uit
ongeveer honderd waarnemingen is zeer onnauwkeurig: één 1931 of één 2008 bepaalt
hem grotendeels. Daarom rust de conclusie hieronder op de horizonnen van 1 en 5
dagen, met duizenden waarnemingen. De rij voor 252 dagen is een ruwe schatting.

De dikke staarten kosten alleen precisie in de variantie. Op dagbasis is de
relatieve standaardfout van de variantieschatting 2,7% in plaats van de 0,9% die
bij normaliteit hoort. Dat is een factor drie, gelijk aan $\sqrt{(\kappa-1)/2}$.

De standaardfout van het geannualiseerde *gemiddelde* blijft bij alle horizonnen
tussen 1,7 en 2,0 procentpunt. De lichte stijging komt van de geschatte
volatiliteit, die op jaarbasis hoger uitvalt door positieve autocorrelatie. Dat
is
[](#thm-rendementen-merton) in tabelvorm: 253 keer minder data, van 26 296 naar
104 waarnemingen, en de precisie van het gemiddelde verandert met een vijfde.
Wat dit leert: dikke staarten kosten precisie in de variantie en niet in het
gemiddelde.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
