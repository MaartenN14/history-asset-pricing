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

(01-02-bachelier)=

# Regnault, Bachelier en de random walk

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1863–1959.

**Wat we al weten.** Uit [](#00-00-setup) komt de gereedschapskist: acht gratis
databronnen, één notatie, en het motief dat de hele reeks draagt — het
gemiddelde rendement is slecht meetbaar, de variantie uitstekend. In
[](#00-01-rendementen) is dat uitgewerkt tot de statistiek van rendementen: log
versus simpel, annualisatie, de standaardfout van het gemiddelde, en de
$\sqrt{t}$-regel die volgt zodra rendementen onafhankelijk zijn. Die regel is
daar afgeleid uit een aanname. Nu draaien we het om: hij werd in 1863 als
*meting* gevonden, veertig jaar voordat er een theorie was die hem verklaarde.

**Welke vraag staat open.** Als de koersuitslag met $\sqrt{t}$ groeit — welk
model van de prijs is daarmee verenigbaar, en hoe toetst men dat model op data?
```

## Overzicht

Deze lecture behandelt de eerste eeuw waarin iemand de beurs als een
kansexperiment beschreef. Ze begint bij Jules Regnault, een employé aan de
Parijse beurs die in 1863 in *Calcul des chances et philosophie de la bourse*
{cite}`Regnault1863` opschreef dat de koersafwijking recht evenredig is met de
wortel van de verstreken tijd. Ze loopt via Louis Bachelier, wiens proefschrift
*Théorie de la spéculation* {cite}`Bachelier1900` de Brownse beweging
construeerde als limiet van een random walk, de diffusievergelijking voor de
kansdichtheid opschreef vijf jaar voordat Einstein hetzelfde deed voor stuifmeel,
en daarmee de eerste optieformule van de geschiedenis afleidde. En ze eindigt bij
de empirici die de bewering toetsten: Cowles, die de voorspellers naliep
{cite}`Cowles1933`, Working, die een reeks van willekeurige verschillen als
nulmodel voorstelde {cite}`Working1934`, en Kendall, die in 1953 in
tweeëntwintig prijsreeksen serieafhankelijkheid vond die te zwak was om iets mee
te voorspellen {cite}`Kendall1953`.

Bachelier definieert het tijdvak omdat hij als enige niet alleen een feit
beschreef maar een *model* leverde waaruit dat feit volgt — en waaruit meteen ook
optieprijzen volgen. Dat het proefschrift een halve eeuw ongelezen bleef, is
geen anekdote maar de reden dat de literatuur van 1900 tot 1960 grotendeels uit
metingen zonder theorie bestaat. De epistemische status is hier dus omgekeerd aan
wat men zou verwachten (motief 3): de random walk begint als een *feit op zoek
naar een theorie*. Regnault meet, Bachelier modelleert maar wordt niet gelezen,
Cowles en Kendall meten opnieuw en kunnen alleen zeggen dát er geen
afhankelijkheid van betekenis is, niet waarom. Pas in 1965 draait Samuelson het om
en bewijst dat correct geanticipeerde prijzen wíllekeurig móeten fluctueren
{cite}`Samuelson1965` — de theorie komt zes decennia na het feit. In
[](#02-06-efficiente-markten) wordt dat de efficiënte-markthypothese; hier blijft
het bij de statistiek.

Het toy-voorbeeld is een random walk van vier stappen. De theorie is de
limietovergang naar Brownse beweging, het reflectieprincipe, de
diffusievergelijking en Bacheliers optieformule, met een korte vergelijking met
Black-Scholes. De simulatie beantwoordt de vraag die de rest van de reeks
achtervolgt: hoeveel data heeft men nodig om een afwijking van de random walk te
zién? En de replicatie herhaalt twee resultaten op echte data — Regnaults
$\sqrt{t}$-wet op Shillers maandreeks vanaf 1871, en de autocorrelaties en
variance ratios van Kendall en van Lo & MacKinlay {cite}`LoMacKinlay1988` op de
dag-, week- en maandreeksen van Kenneth French.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product
from scipy import stats
from scipy.optimize import brentq

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

## Intuïtie: waarom zou dit waar zijn?

Stel dat u elke dag een munt opgooit en bij kop een stap naar rechts zet, bij
munt een stap naar links. Waar bent u na honderd dagen? Gemiddeld op uw
beginpunt, want de stappen heffen elkaar op — maar u bent er vrijwel zeker niet,
en de vraag is hoe ver u er doorgaans vandaan bent. Het antwoord kan niet
"evenredig met het aantal dagen" zijn, want dan zou u altijd dezelfde kant op
lopen; het kan ook niet "onafhankelijk van het aantal dagen" zijn, want dan zou u
nooit ver komen. Ertussenin ligt precies één mogelijkheid die dwingend is zodra
de stappen onafhankelijk zijn: varianties tellen op, en dus groeit de afstand met
de wortel van de tijd. Twee keer zo lang wachten geeft niet twee keer zo veel
afwijking maar ongeveer anderhalf keer zo veel.

Dat is de hele inhoud van Regnaults wet. Hij drukte haar in 1863 in hoofdletters
af: *l'écart des cours est en raison directe de la racine carrée des temps* — de
koersafwijking is recht evenredig met de wortel van de tijd
{cite}`Regnault1863`. Een paar regels eerder had hij de praktische vertaling al
gegeven: halveert men de periode, dan verhoudt de afwijking zich "comme 1 est à
1,41"; neemt men een derde, dan als 1 tot 1,73; een kwart, dan als 1 tot 2. En
omgekeerd: wie zijn afwijking wil verdubbelen moet vier keer zo lang wachten, wie
haar wil verdrievoudigen negen keer. Zijn formulering ging over de Franse
3%-rente op de Parijse beurs, maar het mechanisme is dat van de muntworp: een
koersverandering vandaag zegt niets over die van morgen, dus tellen de
varianties op en niet de uitslagen zelf.

Er zit een economisch argument achter dat pas veel later expliciet werd gemaakt.
Stel dat iedereen wist dat de koers morgen zou stijgen. Dan zou niemand vandaag
willen verkopen en iedereen willen kopen, en de koers zou vandaag al stijgen, net
zolang tot de voorspelbare stijging eruit is. De onvoorspelbaarheid is dus geen
eigenschap van bedrijven of van de economie; ze is een eigenschap van een prijs
waar over onderhandeld wordt.

Wat Bachelier daaraan toevoegde is de stap van het feit naar het model. Laat men
de schokjes oneindig klein en oneindig frequent worden, dan ontstaat er een
limietproces met continue paden en normaal verdeelde aangroeiingen: de Brownse
beweging. Zodra men dat proces heeft, kan men méér dan de spreiding uitrekenen.
Men kan vragen wat de kans is dat de koers ooit een bepaald niveau raakt — het
reflectieprincipe — en wat een contract waard is dat uitbetaalt wat de koers
boven een afgesproken niveau uitkomt. Dat laatste is een optie, en Bachelier gaf
er in 1900 de eerste formule voor. Zijn antwoord voor een optie precies op de
huidige koers is van een verbluffende eenvoud: de waarde is ongeveer vier tiende
maal de volatiliteit maal de wortel van de looptijd. De $\sqrt{t}$ van Regnault
zit er rechtstreeks in.

```{note}
Bachelier verdedigde zijn proefschrift in 1900 bij Henri Poincaré, die het
beoordeelde met *honorable* en niet met *très honorable* — het verschil tussen
een goed proefschrift en een proefschrift dat een loopbaan opent. Dat is meer dan
een curiositeit: de wiskunde van 1900 had geen maattheoretische taal voor een
stochastisch proces, want Kolmogorovs axioma's kwamen pas in 1933. Bachelier
beschreef een object waarvoor het begrippenapparaat nog niet bestond, en de
beoordelaars konden niet zien of zijn constructie sluitend was. Daarom bleef het
werk ongelezen tot Leonard Savage het eind jaren vijftig herontdekte en Paul
Samuelson erop wees.
```

## Toy-voorbeeld: een random walk van vier stappen

Neem de kleinste wandeling waarin alles al zichtbaar is. Op elk tijdstip
$k = 1,2,3,4$ zet de wandelaar een stap $\varepsilon_k \in \{-1,+1\}$, elk met
kans $\tfrac12$, onafhankelijk van de andere. De positie is
$S_n = \sum_{k \le n} \varepsilon_k$, met $S_0 = 0$. Er zijn $2^4 = 16$ paden,
allemaal even waarschijnlijk, en we kunnen ze uitschrijven.

De eindpositie $S_4$ is bepaald door het aantal kopworpen $j$: $S_4 = 2j - 4$,
en $j$ is binomiaal met $n = 4$, $p = \tfrac12$. Dat geeft de verdeling

| $S_4$ | $-4$ | $-2$ | $0$ | $2$ | $4$ |
|---|---|---|---|---|---|
| aantal paden | 1 | 4 | 6 | 4 | 1 |
| kans | $1/16$ | $4/16$ | $6/16$ | $4/16$ | $1/16$ |

De verwachting is nul, want de verdeling is symmetrisch. De variantie is

$$
\Var(S_4) = \frac{16 \cdot 1 + 4 \cdot 4 + 0 \cdot 6 + 4 \cdot 4 + 16 \cdot 1}{16}
          = \frac{64}{16} = 4 .
$$

Dat is geen toeval en het is ook geen benadering: $\Var(S_n) = n$ voor elke $n$,
exact, omdat $\Var(\varepsilon_k) = 1$ en de stappen ongecorreleerd zijn. De
standaarddeviatie is dus $\sqrt{n}$ — Regnaults wet in zijn kaalste vorm, zonder
enige limietovergang, zonder normale verdeling, zonder continue tijd.

Regnault sprak echter niet over de standaarddeviatie maar over de *écart*, de
doorsnee-afwijking. Neem daarvoor de gemiddelde absolute positie:

$$
\E|S_4| = \frac{4 \cdot 1 + 2 \cdot 4 + 0 \cdot 6 + 2 \cdot 4 + 4 \cdot 1}{16}
        = \frac{24}{16} = 1{,}50 .
$$

Op dezelfde manier vindt men $\E|S_1| = 1$, $\E|S_2| = 1$ en $\E|S_3| = 1{,}50$.
De verhouding $\E|S_n|/\sqrt{n}$ loopt dan van $1{,}000$ via $0{,}707$ en
$0{,}866$ naar $0{,}750$: zij schommelt, want de wandeling is nog grof, maar zij
convergeert naar $\sqrt{2/\pi} \approx 0{,}798$. De absolute afwijking volgt
$\sqrt{n}$ dus pas asymptotisch; de *variantie* volgt $n$ meteen. Daarom schatten
we in de replicatie de log-log-helling van de absolute afwijking en vergelijken we
niet naïef twee horizons.

Nog één grootheid, waarmee Bachelier zijn optieformule zou controleren: de kans
dat de wandeling ooit het niveau $+2$ raakt. Het reflectieprincipe — hieronder
bewezen — zegt dat $P(\max_{k \le 4} S_k \ge 2) = P(S_4 = 2) + 2P(S_4 > 2)$, dus
$4/16 + 2 \cdot 1/16 = 0{,}375$. De code telt alle zestien paden en controleert
alle vier de getallen.

```{code-cell} ipython3
paths = np.array(list(product([-1, 1], repeat=4)))     # 16 paden van 4 stappen
positions = paths.cumsum(axis=1)                       # S_1 .. S_4 per pad
final = positions[:, -1]

hand = pd.DataFrame(
    {
        "Var(S_n)": [positions[:, n - 1].var() for n in range(1, 5)],
        "E|S_n|": [np.abs(positions[:, n - 1]).mean() for n in range(1, 5)],
        "E|S_n| / sqrt(n)": [
            np.abs(positions[:, n - 1]).mean() / np.sqrt(n) for n in range(1, 5)
        ],
    },
    index=pd.Index(range(1, 5), name="n"),
).round(4)

reflection = (positions.max(axis=1) >= 2).mean()
print(f"P(max S_k >= 2) geteld    : {reflection:.4f}")
print(f"P(max S_k >= 2) reflectie : {(np.sum(final == 2) + 2 * np.sum(final > 2)) / 16:.4f}")
hand
```

De vier varianties zijn exact $1, 2, 3, 4$, de absolute afwijkingen exact
$1{,}00$, $1{,}00$, $1{,}50$, $1{,}50$, en beide manieren om de raakkans te
bepalen geven $0{,}375$. Handberekening en code vallen samen; vanaf hier mag de
code vertrouwd worden.

## Theorie

### Opzet en notatie

Laat $P_t$ de prijs zijn op tijdstip $t$ en $r_{t+1} = \log P_{t+1} - \log P_t$
het log-rendement over $[t, t+1]$. *Vanaf hier zijn kleine letters logs*, tenzij
anders vermeld: $p_t = \log P_t$. De nulhypothese van deze lecture is de
**random walk**: de $r_{t+1}$ zijn onderling ongecorreleerd met verwachting $\mu$
en variantie $\sigma^2$.

Bachelier zelf werkte niet met logs maar met niveaus, en zijn proces is wat wij
nu *arithmetische Brownse beweging* noemen (absolute prijsveranderingen zijn
normaal verdeeld, in tegenstelling tot de geometrische Brownse beweging waarin de
*relatieve* veranderingen dat zijn). Waar we zijn optieformule afleiden, houden
we zijn conventie aan en schrijven we $S_t$ voor het prijsniveau; overal elders
werken we in logs.

### Van de random walk naar de Brownse beweging

*Waarom zou dit waar zijn?* Als de wandelaar zijn stappen kleiner en talrijker
maakt, verandert er iets aan de schaal maar niets aan de logica: varianties
tellen nog steeds op, de aangroeiingen zijn nog steeds onafhankelijk. De enige
vraag is welke verdeling overblijft als er per tijdseenheid oneindig veel
stapjes zijn. De centrale limietstelling geeft daar precies één antwoord — de
normale verdeling — en zij geeft het bovendien onafhankelijk van de verdeling van
de afzonderlijke stapjes. Dat laatste is de reden dat het model iets waard is:
de wandelaar hoeft geen munt op te gooien, hij mag elke schok met eindige
variantie hebben.

Herschaal de wandeling in de ruimte met $\sqrt{n}$ en in de tijd met $n$:

```{math}
:label: eq-bachelier-donsker
W^{(n)}(u) \;=\; \frac{1}{\sigma\sqrt{n}}\,S_{\lfloor n u \rfloor},
\qquad u \in [0,1].
```

:::{prf:theorem} Invariantieprincipe (Donsker)
:label: thm-bachelier-donsker

Laat $\varepsilon_1, \varepsilon_2, \dots$ onafhankelijk en identiek verdeeld
zijn met $\E[\varepsilon] = 0$ en $\Var(\varepsilon) = \sigma^2 < \infty$, en
$S_n = \sum_{k \le n}\varepsilon_k$. Dan convergeert het proces
$W^{(n)}$ uit [](#eq-bachelier-donsker) in verdeling naar de standaard Brownse
beweging $W$ op $[0,1]$.
:::

Formeel vraagt dit convergentie van maten op de ruimte van continue functies, en
dat apparaat bestond in 1900 niet; Donskers stelling is van 1951. Wat wél in twee
regels te zien is, is de eindig-dimensionale kant, en die volstaat voor alles wat
we hier doen. Voor één tijdstip $u$ geldt

$$
W^{(n)}(u) = \frac{1}{\sigma\sqrt{n}} \sum_{k \le \lfloor nu\rfloor} \varepsilon_k
= \sqrt{\frac{\lfloor nu \rfloor}{n}} \cdot
  \frac{1}{\sigma\sqrt{\lfloor nu\rfloor}}\sum_{k \le \lfloor nu\rfloor}\varepsilon_k
\;\Rightarrow\; \sqrt{u}\cdot Z, \qquad Z \sim \mathcal{N}(0,1),
$$

door de centrale limietstelling, en dus $W^{(n)}(u) \Rightarrow \mathcal{N}(0,u)$.
Voor twee tijdstippen $u < v$ zijn $W^{(n)}(u)$ en $W^{(n)}(v) - W^{(n)}(u)$ sommen
over disjuncte blokken en dus onafhankelijk, wat in de limiet de definiërende
eigenschap van de Brownse beweging is: onafhankelijke, normaal verdeelde
aangroeiingen met $\Var(W_v - W_u) = v - u$.

Daarmee is Regnaults wet een stelling geworden in plaats van een meting:
$\SD(W_{t+h} - W_t) = \sqrt{h}$, en $\E|W_{t+h} - W_t| = \sqrt{2h/\pi}$.

```{code-cell} ipython3
:label: cel-bachelier-paden
:tags: [hide-input]

n_steps, n_shown = 2000, 40
steps = rng.choice([-1.0, 1.0], size=(n_shown, n_steps)) / np.sqrt(n_steps)
walks = steps.cumsum(axis=1)
grid = np.arange(1, n_steps + 1) / n_steps

fig, ax = plt.subplots()
ax.plot(grid, walks.T, lw=0.7, color=hap.plotting.COLORS[0], alpha=0.35)
for sign in (-1, 1):
    ax.plot(grid, sign * np.sqrt(grid), color=hap.plotting.COLORS[1], lw=1.8,
            label=r"$\pm\sqrt{u}$" if sign == 1 else None)
ax.set_title("Veertig herschaalde random walks van 2000 stappen")
ax.set_xlabel("Herschaalde tijd $u$")
ax.set_ylabel("Positie $W^{(n)}(u)$")
ax.legend()
plt.show()
```

:::{figure} #cel-bachelier-paden
:label: fig-bachelier-paden
:width: 90%

Veertig paden van een symmetrische random walk, herschaald volgens
[](#eq-bachelier-donsker). Geen enkel pad is glad, maar de *bundel* heeft een
scherp omhullende vorm: de rode krommen zijn $\pm\sqrt{u}$, één standaarddeviatie.
Wie naar één pad kijkt ziet patronen; wie naar de bundel kijkt ziet
$\sqrt{t}$.
:::

### Het reflectieprincipe

*Waarom zou dit waar zijn?* Vraag naar de kans dat de wandeling ooit het niveau
$a > 0$ raakt. Splits de paden die $a$ raken in twee groepen: die welke boven $a$
eindigen, en die welke er weer onder zakken. Spiegel nu het stuk ná de eerste
aanraking in de lijn $y = a$. Omdat de stappen symmetrisch en onafhankelijk zijn,
is elk gespiegeld pad precies even waarschijnlijk als het origineel. De
spiegeling ruilt dus de tweede groep om met de eerste, één op één. Daarmee is de
lastige gebeurtenis "raakt ooit $a$" teruggebracht tot de eenvoudige gebeurtenis
"eindigt boven $a$", die alleen de eindverdeling gebruikt.

:::{prf:theorem} Reflectieprincipe
:label: thm-bachelier-reflectie

Laat $S_n$ een symmetrische random walk zijn met stappen $\pm 1$ en
$M_n = \max_{k \le n} S_k$. Voor $a \ge 1$ geldt

```{math}
:label: eq-bachelier-reflectie
P(M_n \ge a) \;=\; P(S_n = a) \,+\, 2\,P(S_n > a).
```

In de Brownse limiet met $S_T \sim \mathcal{N}(0, \sigma^2 T)$ wordt dit
$P(\max_{t \le T} S_t \ge a) = 2\,P(S_T \ge a)$.
:::

:::{prf:proof}
Zij $\tau = \min\{k : S_k = a\}$ het eerste raaktijdstip. Op $\{\tau \le n\}$
definiëren we het gespiegelde pad $\tilde S_k = S_k$ voor $k \le \tau$ en
$\tilde S_k = 2a - S_k$ voor $k > \tau$. Omdat de stappen na $\tau$ onafhankelijk
en symmetrisch zijn, heeft $\tilde S$ dezelfde kans als $S$, en de afbeelding is
een involutie op $\{\tau \le n\}$, dus een bijectie.

Ze beeldt $\{\tau \le n,\ S_n < a\}$ af op $\{\tau \le n,\ S_n > a\}$ en omgekeerd.
Dus $P(\tau \le n,\ S_n < a) = P(S_n > a)$, waarbij rechts de conditie
$\tau \le n$ mag vervallen: een pad dat boven $a$ eindigt heeft $a$ noodzakelijk
geraakt. Splitsen naar de eindwaarde geeft

$$
P(M_n \ge a) = P(\tau \le n)
 = \underbrace{P(S_n > a)}_{\text{eindigt boven}} + \underbrace{P(S_n = a)}_{\text{eindigt op}}
 + \underbrace{P(\tau \le n,\ S_n < a)}_{= P(S_n > a)},
$$

wat [](#eq-bachelier-reflectie) is. In continue tijd is $P(S_T = a) = 0$ en
blijft $P(\max \ge a) = 2P(S_T \ge a)$ over. $\square$
:::

In het toy-voorbeeld is $n = 4$, $a = 2$: de stelling geeft
$4/16 + 2 \cdot 1/16 = 0{,}375$, en de telling van alle zestien paden gaf
hetzelfde. Bachelier gebruikte dit principe om de prijs te bepalen van wat hij
*options à prime* en van wat wij barrièreopties zouden noemen; het is ook de
kortste route naar de verdeling van de maximale drawdown.

### De diffusievergelijking, vijf jaar voor Einstein

*Waarom zou dit waar zijn?* De kansdichtheid van de positie moet aan één
boekhoudkundige eis voldoen: om op tijdstip $t+s$ op plaats $x$ te zijn, moet men
op $t$ ergens zijn geweest en daarna het verschil hebben afgelegd. Optellen over
alle tussenposities geeft een convolutie. Zodra de tussenstap klein is, is die
convolutie niets anders dan een middeling van de dichtheid over de directe
omgeving — en een dichtheid die naar zijn eigen omgeving toe middelt, gedraagt
zich als warmte in een staaf: pieken vlakken af met een snelheid evenredig aan
hun kromming.

Schrijf $p(x,t)$ voor de dichtheid van $S_t$ met $S_0 = 0$. Onafhankelijke
aangroeiingen geven de Chapman-Kolmogorov-vergelijking

$$
p(x, t+s) \;=\; \int_{-\infty}^{\infty} p(y, t)\, q(x - y, s)\, \mathrm{d}y,
$$

met $q(\cdot,s)$ de dichtheid van de aangroei over een interval $s$. Neem $s$
klein, met $\int q = 1$, $\int z\, q(z,s)\,\mathrm{d}z = 0$ en
$\int z^2 q(z,s)\,\mathrm{d}z = \sigma^2 s$, en ontwikkel $p(x - z, t)$ naar $z$:

$$
p(x,t+s) = \int \left[p(x,t) - z\,\partial_x p + \tfrac12 z^2 \partial_{xx} p
 + O(z^3)\right] q(z,s)\,\mathrm{d}z
 = p(x,t) + \tfrac12 \sigma^2 s\, \partial_{xx} p + o(s).
$$

Aftrekken van $p(x,t)$, delen door $s$ en $s \downarrow 0$ nemen geeft

```{math}
:label: eq-bachelier-diffusie
\frac{\partial p}{\partial t} \;=\; \frac{\sigma^2}{2}\,
\frac{\partial^2 p}{\partial x^2},
```

de warmtevergelijking, met als oplossing bij beginvoorwaarde $p(x,0) = \delta(x)$
de normale dichtheid $p(x,t) = \varphi(x/(\sigma\sqrt{t}))/(\sigma\sqrt{t})$.
Bachelier leidde [](#eq-bachelier-diffusie) in 1900 af voor beurskoersen; Einstein
kwam in 1905 langs dezelfde weg tot dezelfde vergelijking voor stuifmeeldeeltjes.
De $\sqrt{t}$ zit er zichtbaar in: de vergelijking is invariant onder
$x \mapsto \lambda x$, $t \mapsto \lambda^2 t$, en elke oplossing moet die
schaling dus respecteren.

```{note}
[](#eq-bachelier-diffusie) is de vergelijking voor de *kansdichtheid*, niet voor
de prijs van een contract. De tweede vergelijking die Bachelier nodig had — de
waarde van een claim als functie van koers en resterende looptijd — voldoet aan
dezelfde operator met een omgekeerd tijdsteken. Dat is precies het paar
voorwaartse en achterwaartse Kolmogorov-vergelijkingen, en het is ook de reden
dat de Black-Scholes-PDE in [](#02-09-black-scholes) na één substitutie in de
warmtevergelijking overgaat.
```

### Bacheliers optieformule

*Waarom zou dit waar zijn?* Bachelier ging uit van wat hij *l'espérance
mathématique du spéculateur est nulle* noemde: de beurs is zo geprijsd dat de
verwachte winst van de speculant nul is. Dat is de moderne martingaalconditie in
negentiende-eeuwse taal. Aanvaardt men die, dan is de waarde van elk contract de
verwachte uitbetaling, en is de prijs van een optie een integraal over de
normale verdeling — meer is er niet aan. Wat Bachelier miste, en wat pas
Black, Scholes en Merton zouden leveren, is het argument *waarom* men die
verwachting onder juist deze verdeling mag nemen: niet uit billijkheid, maar
omdat de optie met de onderliggende waarde te repliceren is.

:::{prf:theorem} Bacheliers optieprijs
:label: thm-bachelier-optie

Zij $S_T = S_t + \sigma (W_T - W_t)$ met $W$ een standaard Brownse beweging, dus
$S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(S_t, \sigma^2 \tau\right)$ met
$\tau = T - t$. Onder de martingaalconditie is de waarde van een calloptie met
uitoefenprijs $K$, bij een rente van nul,

```{math}
:label: eq-bachelier-call
C_t \;=\; (S_t - K)\,\Phi(d) \;+\; \sigma\sqrt{\tau}\,\varphi(d),
\qquad d \;=\; \frac{S_t - K}{\sigma\sqrt{\tau}},
```

met $\Phi$ en $\varphi$ de verdelings- en dichtheidsfunctie van de
standaardnormale verdeling. Voor een optie op de huidige koers ($K = S_t$, dus
$d = 0$) reduceert dit tot

```{math}
:label: eq-bachelier-atm
C_t \;=\; \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}} \;\approx\; 0{,}3989\,\sigma\sqrt{\tau}.
```
:::

:::{prf:proof}
Schrijf $s = \sigma\sqrt{\tau}$ en $x = S_t - K$. Onder de martingaalmaat is
$S_T = S_t + sZ$ met $Z \sim \mathcal{N}(0,1)$, dus

$$
C_t = \E\!\left[(S_T - K)^{+}\right]
 = \int_{-x/s}^{\infty} (x + sz)\,\varphi(z)\,\mathrm{d}z .
$$

De eerste term is $x\left[1 - \Phi(-x/s)\right] = x\,\Phi(x/s)$. Voor de tweede
gebruiken we $z\varphi(z) = -\varphi'(z)$:

$$
s\int_{-x/s}^{\infty} z\,\varphi(z)\,\mathrm{d}z
= s\Bigl[-\varphi(z)\Bigr]_{-x/s}^{\infty} = s\,\varphi(-x/s) = s\,\varphi(x/s),
$$

want $\varphi$ is even. Samen geeft dit [](#eq-bachelier-call). Bij $x = 0$ blijft
$s\,\varphi(0) = s/\sqrt{2\pi}$ over. $\square$
:::

Drie dingen zijn aan [](#eq-bachelier-atm) opmerkelijk. De prijs van een
at-the-money optie is *lineair* in de volatiliteit en evenredig met
$\sqrt{\tau}$ — Regnaults wet als handelsregel: wie de looptijd verviervoudigt
betaalt het dubbele. Er staat geen enkele voorkeursparameter in: geen
risicoaversie, geen verwacht rendement. Dat de prijs van een risicovol contract
niet van het verwachte rendement van de onderliggende waarde afhangt, is de
observatie waar de hele optietheorie op rust, en Bachelier had haar in 1900. En
discontering ontbreekt, omdat hij met termijnkoersen werkte.

```{note}
Bachelier schreef [](#eq-bachelier-atm) zelf niet met het getal $0{,}3989$ maar
als $a = k\sqrt{t}$, waarbij $k$ zijn *coefficient d'instabilité ou de nervosité*
is — de volatiliteit, zestig jaar voordat het woord bestond. Zijn dichtheid is
$p = (1/2\pi a)\,e^{-x^2/(4\pi a^2)}$, waaruit $\sigma\sqrt{t} = a\sqrt{2\pi}$
volgt; $a = \sigma\sqrt{t}/\sqrt{2\pi}$ is dus precies onze formule. En hij toetste
zijn model. Op de rente 3% over 1894–1898 kalibreerde hij $k = 5$ centimes per
$\sqrt{\text{dag}}$, en voorspelde daarmee voor een maand een probabele uitslag
van $\pm 46$ centimes: "Pendant les 60 derniers mois, 33 fois la variation a été
circonscrite entre ces limites et 27 fois elle les a dépassées" — bij constructie
dertig om dertig. Zijn tabellen met *calculée* naast *observée* voor de
uitoefenkansen van primes lopen tot op één honderdste gelijk. Het proefschrift
eindigt met de zin die het tijdvak samenvat: "le marché, à son insu, obéit à une
loi qui le domine: la loi de la probabilité."
```

### Vergelijking met Black-Scholes

Het verschil met {cite}`BlackScholes1973` zit niet in de wiskunde maar in de
aanname over het proces. Bachelier laat de *absolute* prijsverandering normaal
zijn, Black en Scholes de *relatieve*. Daaruit volgen drie verschillen. De
Bachelier-prijs kan negatief worden, wat voor een aandeel onzinnig is maar voor
een spread of een termijncontract op een grondstof juist gewenst — de formule
werd daarom in april 2020 onder brede aandacht weer in gebruik genomen toen de
termijnprijs van ruwe olie negatief werd. De Bachelier-volatiliteit $\sigma$
heeft de eenheid van een prijs per $\sqrt{\text{tijd}}$, de
Black-Scholes-volatiliteit is dimensieloos; de vertaling is
$\sigma_{\text{Bach}} \approx \sigma_{\text{BS}} \cdot S$. En de formules vallen
bij korte looptijden en rond de huidige koers vrijwel samen, want de
Black-Scholes-prijs van een at-the-money optie is bij rente nul

$$
C^{\text{BS}} = S\left[\Phi\!\left(\tfrac{\sigma_{\text{BS}}\sqrt{\tau}}{2}\right)
 - \Phi\!\left(-\tfrac{\sigma_{\text{BS}}\sqrt{\tau}}{2}\right)\right]
\;\approx\; S\,\sigma_{\text{BS}}\sqrt{\tau}\,\varphi(0)
= 0{,}3989\, S\,\sigma_{\text{BS}}\sqrt{\tau},
$$

precies [](#eq-bachelier-atm) met $\sigma_{\text{Bach}} = \sigma_{\text{BS}} S$.
De cel hieronder rekent beide formules uit voor een aandeel van 100 met een
Black-Scholes-volatiliteit van 20% per jaar.

```{code-cell} ipython3
def bachelier_call(S, K, sigma_abs, tau):
    """Bachelier (1900) call price under arithmetic Brownian motion, zero rate."""
    s = sigma_abs * np.sqrt(tau)
    d = (S - K) / s
    return (S - K) * stats.norm.cdf(d) + s * stats.norm.pdf(d)


def bs_call(S, K, sigma, tau):
    """Black-Scholes (1973) call price, zero rate."""
    d1 = (np.log(S / K) + 0.5 * sigma**2 * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    return S * stats.norm.cdf(d1) - K * stats.norm.cdf(d2)


S0, sigma_bs = 100.0, 0.20
rows = []
for tau in (1 / 12, 0.5, 1.0):
    for K in (90.0, 100.0, 110.0):
        rows.append(
            {
                "looptijd (jaar)": tau,
                "K": K,
                "Bachelier": bachelier_call(S0, K, sigma_bs * S0, tau),
                "Black-Scholes": bs_call(S0, K, sigma_bs, tau),
            }
        )
table = pd.DataFrame(rows)
table["verschil"] = table["Bachelier"] - table["Black-Scholes"]
table.round(4)
```

Bij een looptijd van een maand zijn de twee prijzen tot op enkele centen gelijk,
en op het geld tot op een tiende cent; bij een jaar en tien procent uit het geld
loopt het verschil op tot $0{,}34$ à $0{,}37$ euro op een optie van vier euro. De
at-the-money-prijs bij $\tau = 1$ is
$0{,}3989 \times 20 = 7{,}98$ volgens [](#eq-bachelier-atm), en de tabel bevestigt
dat. Wie in 1900 met deze formule had gehandeld, had een model gehad dat voor
korte looptijden nauwelijks van het model van 1973 te onderscheiden is.

### Wat "onvoorspelbaar" statistisch betekent

Voordat men toetst, moet men weten waarnaar men kijkt. Working wees er in 1934 op
dat een reeks die ontstaat door toevalsgetallen op te tellen — een
*random-difference series* — er bedrieglijk gestructureerd uitziet
{cite}`Working1934`: zij vertoont opvallende trends en schijnbare cycli, die "must
be regarded merely as generalized descriptions of the course of the series over a
certain period, not as norms, nor as bases for predicting the future course of
the series over even the briefest subsequent period". Iedereen kan de slotkoers
van morgen voorspellen met een verwaarloosbare fout; bijna niemand gelooft dat men
de koers*verandering* van morgen kan voorspellen. Wie het niveau toetst, toetst
dus niets.

De random walk doet drie toetsbare uitspraken over de log-rendementen, en elke
generatie empirici koos er één.

**Autocorrelatie.** Onder de nulhypothese is $\rho_k = \Corr(r_t, r_{t-k}) = 0$
voor elke $k \ge 1$, en de steekproefautocorrelatie heeft bij benadering
standaardfout $1/\sqrt{T}$. Dit is wat Cowles en Jones, en later Kendall,
uitrekenden.

**Runs.** Tel het aantal aaneengesloten reeksen van gelijke tekens. Met $n_1$
positieve en $n_2$ negatieve waarnemingen is het verwachte aantal runs
$\E[R] = 2n_1n_2/n + 1$ met $n = n_1 + n_2$, en

$$
\Var(R) = \frac{2n_1 n_2 (2n_1n_2 - n)}{n^2 (n-1)} .
$$

Te weinig runs betekent dat tekens plakken, dus positieve afhankelijkheid. De
runs-test heeft als voordeel dat hij niets over de verdeling aanneemt, wat in
1953 met dikke staarten en handrekenwerk zwaarder woog dan nu.

**Variance ratio.** De krachtigste toets is tegelijk de eenvoudigste, en hij is
precies de gekwantificeerde $\sqrt{t}$-wet. Definieer

```{math}
:label: eq-bachelier-vr
VR(q) \;=\; \frac{\Var\!\left(r_t + r_{t-1} + \dots + r_{t-q+1}\right)}
                  {q\,\Var(r_t)} .
```

Onder de random walk is $VR(q) = 1$ voor elke $q$: variantie groeit lineair in de
tijd, standaarddeviatie dus met $\sqrt{q}$.

:::{prf:theorem} Variance ratio als gewogen som van autocorrelaties
:label: thm-bachelier-vr

Voor een covariantie-stationaire reeks geldt

```{math}
:label: eq-bachelier-vr-rho
VR(q) \;=\; 1 + 2\sum_{j=1}^{q-1}\left(1 - \frac{j}{q}\right)\rho_j .
```
:::

:::{prf:proof}
Schrijf $\gamma_j = \Cov(r_t, r_{t-j})$, dus $\rho_j = \gamma_j/\gamma_0$. De
variantie van de som van $q$ opeenvolgende termen telt $q$ keer $\gamma_0$ en
voor elke $j \ge 1$ precies $2(q-j)$ keer $\gamma_j$, want er zijn $q - j$ paren
op afstand $j$ en elk paar telt twee keer mee:

$$
\Var\Bigl(\sum_{i=0}^{q-1} r_{t-i}\Bigr)
 = q\gamma_0 + 2\sum_{j=1}^{q-1}(q-j)\gamma_j .
$$

Delen door $q\gamma_0$ geeft [](#eq-bachelier-vr-rho). $\square$
:::

Twee gevolgen zijn belangrijk. Ten eerste is $VR(2) - 1 = \rho_1$ exact: de
eenvoudigste variance ratio is de eerste autocorrelatie in vermomming. Ten tweede
— en dat is de reden dat Lo en MacKinlay hem verkozen — bundelt $VR(q)$ voor
grotere $q$ vele kleine autocorrelaties met aflopende gewichten: als de
afhankelijkheid over veel lags is uitgesmeerd, is elke $\rho_j$ afzonderlijk
onzichtbaar in de ruis terwijl hun gewogen som dat niet is. Onder de nulhypothese
en homoskedasticiteit is de standaardfout van $VR(q)$ gelijk aan
$\sqrt{2(2q-1)(q-1)/(3qT)}$, wat voor $q = 2$ neerkomt op $1/\sqrt{T}$
{cite}`LoMacKinlay1988`. `hap.stats.variance_ratio` geeft naast $VR(q)$ ook de
homoskedastische toetsgrootheid $z_1$ en de heteroskedasticiteitsrobuuste $z_2$;
die laatste is de relevante, want volatiliteit clustert en dat alleen al zou
$z_1$ te groot maken.

Hier verschijnt motief 1 in zijn zuiverste vorm. Het gemiddelde rendement is met
een eeuw data niet te schatten; de variantie wél. De variance ratio is een
verhouding van *varianties*, en daarom de enige klasse toetsen waarmee men met de
beschikbare data überhaupt iets over voorspelbaarheid kan zeggen.

## Simulatie: hoeveel data om een afwijking te zien?

De theorie zegt dat $VR(q) = 1$ in de populatie. De vraag die telt is hoe
$\widehat{VR}$ zich in een *steekproef* gedraagt, en hoe ver de waarheid van één
moet afwijken voordat een onderzoeker dat merkt. We nemen als maat de steekproef
van Lo en MacKinlay: $T = 1216$ weekrendementen, ruim drieëntwintig jaar. Eerst de
nulverdeling, uit duizenden i.i.d.-paden, naast de asymptotische benadering
$\mathcal{N}(1, 1/T)$.

```{code-cell} ipython3
n_paths, T_lm = 2000, 1216
iid_paths = rng.normal(0.0, 0.02, size=(n_paths, T_lm))
vr_null = np.array([hap.variance_ratio(pd.Series(p), 2)["vr"] for p in iid_paths])

pd.DataFrame(
    {
        "waarde": [
            vr_null.mean(),
            vr_null.std(ddof=1),
            1 / np.sqrt(T_lm),
            np.mean(np.abs(vr_null - 1) > 1.96 / np.sqrt(T_lm)),
        ]
    },
    index=["gemiddelde VR(2)", "std.dev. van VR(2)", "asymptotische SE",
           "verwerpingsfractie bij 5%"],
).round(4)
```

De simulatie geeft een gemiddelde van vrijwel precies één en een spreiding die
tot in de derde decimaal met $1/\sqrt{T}$ overeenkomt ($0{,}0281$ tegen
$0{,}0287$). De toets houdt ruwweg zijn omvang: $4{,}3$ procent van de
i.i.d.-steekproeven wordt onterecht verworpen, iets onder de nominale vijf, wat
past bij een schatter die in eindige steekproeven een fractie te weinig spreiding
heeft.

Nu het alternatief. Het eenvoudigste afwijkingsmodel is een AR(1) in
log-rendementen, $r_t = \rho\, r_{t-1} + e_t$, want daarvoor is $\rho_1 = \rho$
en dus $VR(2) = 1 + \rho$ volgens [](#eq-bachelier-vr-rho). Een positieve $\rho$
betekent dat trends zich voortzetten — de lezing die Lo en MacKinlay voor de
weekdata zouden vinden.

```{code-cell} ipython3
def ar1_paths(rho, n_paths, T, sigma=0.02, burn=200):
    """Simulate AR(1) log-return paths, discarding a burn-in."""
    e = rng.normal(0.0, sigma, size=(n_paths, T + burn))
    x = np.empty_like(e)
    x[:, 0] = e[:, 0]
    for t in range(1, T + burn):
        x[:, t] = rho * x[:, t - 1] + e[:, t]
    return x[:, burn:]


rows = []
for rho in (0.05, 0.10, 0.20):
    for T in (260, 1040, 4160):
        stats_ = [hap.variance_ratio(pd.Series(p), 2) for p in ar1_paths(rho, 1000, T)]
        rows.append(
            {
                "rho": rho,
                "jaren weekdata": T // 52,
                "gemiddelde VR(2)": np.mean([s["vr"] for s in stats_]),
                "onderscheidend vermogen": np.mean(
                    [abs(s["z2"]) > 1.96 for s in stats_]
                ),
                "analytisch": stats.norm.sf(1.96 - rho * np.sqrt(T))
                + stats.norm.cdf(-1.96 - rho * np.sqrt(T)),
            }
        )
power = pd.DataFrame(rows)
power.round(3)
```

De gemiddelde $\widehat{VR}(2)$ is in alle negen gevallen vrijwel exact
$1 + \rho$, zoals de theorie voorschrijft: de schatter is nagenoeg zuiver, ook bij
$T = 260$. Het onderscheidend vermogen
is een ander verhaal. Omdat $VR(2) - 1 = \rho$ en de standaardfout $1/\sqrt{T}$
is, geldt $z = \rho\sqrt{T}$ en dus

```{math}
:label: eq-bachelier-power
T^{*} \;=\; \left(\frac{1{,}96}{\rho}\right)^{2}
```

waarnemingen voor een verwachte $z$-waarde van $1{,}96$ — en dat is nog maar
vijftig procent kans om te verwerpen. Voor $\rho = 0{,}20$ zijn dat 96 weken; voor
$\rho = 0{,}05$ zijn het 1537 weken, bijna dertig jaar; voor $\rho = 0{,}02$ zijn
het 9604 weken, ruim honderdvierentachtig jaar — langer dan de beurs bestaat
waarop men zou willen meten. Simulatie en formule komen tot op steekproefruis
overeen, dus de vuistregel mag gebruikt worden.

```{code-cell} ipython3
:label: cel-bachelier-power
:tags: [hide-input]

T_grid = np.arange(52, 10_400, 52)

fig, ax = plt.subplots()
for i, rho in enumerate((0.02, 0.05, 0.10, 0.20)):
    z = rho * np.sqrt(T_grid)
    ax.plot(T_grid / 52, stats.norm.sf(1.96 - z) + stats.norm.cdf(-1.96 - z),
            color=hap.plotting.COLORS[i], label=rf"$\rho = {rho:.2f}$")
ax.scatter(power["jaren weekdata"], power["onderscheidend vermogen"],
           color="black", s=18, zorder=3, label="simulatie")
ax.axhline(0.5, color="black", ls="--", lw=0.9)
ax.axvline(23.4, color=hap.plotting.COLORS[7], lw=1.2)
ax.text(24.5, 0.05, "Lo-MacKinlay (23 jaar)", fontsize=9)
ax.set_xscale("log")
ax.set_title("Kans om een afwijking van de random walk te verwerpen")
ax.set_xlabel("Jaren weekdata (log-schaal)")
ax.set_ylabel("Onderscheidend vermogen bij 5%")
ax.legend()
plt.show()
```

:::{figure} #cel-bachelier-power
:label: fig-bachelier-power
:width: 90%

Het onderscheidend vermogen van de variance-ratio-toets tegen een AR(1), als
functie van de lengte van de steekproef. De zwarte punten zijn de gesimuleerde
waarden uit de tabel hierboven. Bij de drieëntwintig jaar weekdata van Lo en
MacKinlay is een autocorrelatie van 0,20 zo goed als zeker zichtbaar en een van
0,02 zo goed als onzichtbaar. Wie beweert dat een markt "efficiënt" is, zegt dus
altijd *met de data die ik heb*.
:::

```{warning}
Deze rekensom heeft een onaangename keerzijde. Dezelfde $T$ die te klein is om
een echte $\rho$ van 0,02 te vinden, is groot genoeg om ruis van 0,06 te
produceren. Wie vijftig markten, tien horizons en drie frequenties nakijkt, vindt
met zekerheid ergens een $z$-waarde boven twee zonder dat er iets te vinden is.
Dat is hetzelfde selectieprobleem dat in [](#06-34-factor-zoo) de factor zoo
verklaart, en het is de reden dat de onderzoeken van na 1990 hun steekproef vooraf
vastleggen.
```

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Jules Regnault, *Calcul des chances et philosophie de la bourse*, Paris
1863 {cite}`Regnault1863`.

**Wat.** Zijn centrale empirische wet, in hoofdletters afgedrukt: *l'écart des
cours est en raison directe de la racine carrée des temps*. En zijn eigen toets
ervan (§83–84): hij mat een gemiddelde maandelijkse uitslag van $2{,}73$ frank
(na correctie voor coupon en report) en vermenigvuldigde die met
$\sqrt{3} = 1{,}73$ en $\sqrt{12} = 3{,}46$, wat $4{,}73$ voor het kwartaal en
$9{,}45$ voor het jaar gaf, tegen waargenomen $4{,}74$ en $9{,}50$. Wij herhalen
die vergelijking en schatten daarnaast de helling $b$ in
$\log \E|p_{t+h} - p_t| = a + b \log h$ over $h = 1, 3, 12, 60$ maanden.

**Data hier.** Shillers maandreeks van de reële S&P-prijs, 1871-01 t/m 2026-09,
via `hap.data.shiller()`; ter controle de maandelijkse marktfactor van Kenneth
French vanaf 1926-07 via `hap.data.market_monthly()`.

**Verschil met het origineel.** Regnault werkte met de maandelijkse hoogste en
laagste koers van de Franse 3%-rente à comptant, van de uitgifte in mei 1825 tot
eind 1862, in francs; wij gebruiken een Amerikaanse aandelenindex en log-prijzen.
Zijn *écart* houden we aan als gemiddelde absolute verandering. Shillers
maandprijs is bovendien het gemiddelde van de dagelijkse slotkoersen binnen de
maand en niet de koers op maandeinde — een middeling die de gemeten variantie op
de kortste horizon indrukt.

**Verwachte afwijking.** De helling moet dicht bij $0{,}5$ liggen en ver van $1$;
dat laatste is de falsifieerbare eis, want evenredigheid met $t$ zelf zou een
trendmarkt betekenen. Wij verwachten voor de French-reeks $b$ binnen $0{,}05$ van
$0{,}5$, en voor Shiller een hogere waarde door de maandmiddeling. De verhouding
$\E|p_{t+h}-p_t|/\sqrt{h}$ moet over de vier horizons binnen een factor twee
blijven — bij een lineaire wet zou hij een factor acht oplopen. Regnaults eigen
overeenstemming van een half procent tussen theorie en waarneming halen wij niet:
één maand extrapoleren naar twaalf is gevoelig voor de meetconventie, en wij
werken bovendien met een aandelenindex in plaats van met staatspapier.
```

```{code-cell} ipython3
def deviation_scaling(log_level, horizons=(1, 3, 12, 60)):
    """Mean absolute and standard deviation of h-period changes, demeaned."""
    rows = []
    for h in horizons:
        dev = (log_level.shift(-h) - log_level).dropna()
        dev = dev - dev.mean()
        rows.append({"h": h, "nobs": len(dev), "E|dev|": dev.abs().mean(),
                     "SD(dev)": dev.std(ddof=1)})
    out = pd.DataFrame(rows).set_index("h")
    out["Regnault: E|dev|(1)*sqrt(h)"] = out["E|dev|"].iloc[0] * np.sqrt(out.index)
    out["E|dev| / sqrt(h)"] = out["E|dev|"] / np.sqrt(out.index)
    return out


shiller = hap_data.shiller()
p_shiller = np.log(shiller["real_price"].dropna())
p_french = np.log1p(hap_data.market_monthly()["Mkt"]).cumsum()

regnault = pd.concat(
    {"Shiller 1871-2026": deviation_scaling(p_shiller),
     "French 1926-2026": deviation_scaling(p_french)},
    names=["reeks"],
)
regnault.round(4)
```

```{code-cell} ipython3
slopes = {
    name: np.polyfit(np.log(block.index.get_level_values("h")),
                     np.log(block["E|dev|"]), 1)[0]
    for name, block in regnault.groupby(level="reeks")
}
pd.DataFrame({"helling b": slopes}).round(3)
```

De hoofduitkomst staat in die tweede tabel. Voor de French-reeks is de geschatte
helling $0{,}511$ — Regnaults wet tot op één honderdste. Voor Shillers reeks is ze
$0{,}577$, en de verklaring staat in het replicatieblok: zijn maandprijs is een
gemiddelde van dagkoersen binnen de maand, en middelen onderdrukt variantie op de
kortste horizon meer dan op de langste. Laat men $h = 1$ weg, dan zakt de helling
naar ongeveer $0{,}54$, en tussen twaalf en zestig maanden is ze $0{,}475$ — iets
*onder* de halve, wat op milde terugkeer naar het gemiddelde wijst; dat
verschijnsel krijgt in [](#04-20-voorspelbaarheid) een eigen lecture.

De falsifieerbare eis is ruim gehaald: de verhouding $\E|{\cdot}|/\sqrt{h}$ loopt
over een factor zestig in horizon met minder dan een factor anderhalf op, terwijl
een lineaire wet een factor bijna acht zou geven. Regnaults eigen presentatie
staat in de kolom `Regnault`, en die is eerlijker over de marge dan de helling:
voor de French-reeks voorspelt de maanduitslag van $0{,}0373$ een jaaruitslag van
$0{,}129$ tegen $0{,}146$ waargenomen, dertien procent te laag, waar hij zelf
$9{,}45$ tegen $9{,}50$ rapporteerde. Zijn rente was dan ook een staatsobligatie
met een stabielere volatiliteit dan een aandelenindex waarin de jaren dertig en
2008 zitten.

```{code-cell} ipython3
:label: cel-bachelier-regnault
:tags: [hide-input]

fig, ax = plt.subplots()
for i, (name, block) in enumerate(regnault.groupby(level="reeks")):
    h = block.index.get_level_values("h").to_numpy(float)
    ax.plot(h, block["E|dev|"], "o-", color=hap.plotting.COLORS[i], label=name)
reference = regnault.loc["French 1926-2026", "E|dev|"].iloc[0] * np.sqrt([1, 3, 12, 60])
ax.plot([1, 3, 12, 60], reference, ls="--", color="black", lw=1.2,
        label=r"referentie $\propto\sqrt{h}$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_title("Regnaults wet: gemiddelde absolute koersafwijking per horizon")
ax.set_xlabel("Horizon $h$ (maanden, log-schaal)")
ax.set_ylabel("$E|p_{t+h} - p_t|$ (log-schaal)")
ax.legend()
plt.show()
```

:::{figure} #cel-bachelier-regnault
:label: fig-bachelier-regnault
:width: 90%

Op dubbellogaritmische schaal is Regnaults wet een rechte lijn met helling
$\tfrac12$. Beide reeksen volgen die lijn over een bereik van vijf jaar tot één
maand; de lichte knik bij de kortste horizon in de Shiller-reeks komt van de
maandmiddeling in zijn prijsreeks en niet van de markt.
:::

```{admonition} Replicatie
:class: seealso

**Bron.** Maurice Kendall, *The Analysis of Economic Time-Series — Part I:
Prices*, JRSS-A 1953 {cite}`Kendall1953`; en Andrew Lo & Craig MacKinlay, *Stock
Market Prices Do Not Follow Random Walks*, Review of Financial Studies 1988
{cite}`LoMacKinlay1988`.

**Wat.** Kendalls tabel 3, de eerste-orde-seriecorrelaties van negentien
wekelijkse Britse industrie-aandelenindices over 1928–1938: zij lopen van
$-0{,}013$ (Oil) tot $+0{,}301$ (Investment Trusts), met een gemiddelde van
ongeveer $0{,}13$, en zijn volgens hem "so weak as to dispose at once of any
possibility of being able to use them for prediction". En de tabellen 1a en 2 van
Lo en MacKinlay: variance ratios boven één op weekbasis, stelselmatig groter voor
portefeuilles van kleine ondernemingen.

**Data hier.** De dagelijkse marktfactor van Kenneth French
(`hap.data.market_daily()`), geaggregeerd tot weekrendementen van vrijdag op
vrijdag, en de maandelijkse marktfactor en op marktwaarde gesorteerde
kwintielportefeuilles (`hap.data.french("Portfolios_Formed_on_ME", "monthly")`).
De steekproef van Lo en MacKinlay loopt van 6 september 1962 tot en met
26 december 1985.

**Verschil met het origineel.** Kendall gebruikte tweeëntwintig reeksen:
negentien Britse industrie-aandelenindices uit het interbellum (wekelijks, 486
waarnemingen elk), tarwe in Chicago en katoen in New York; wij gebruiken de
Amerikaanse markt. Lo en MacKinlay gebruikten de CRSP-indices, gelijkgewogen én
marktwaardegewogen, met weekrendementen van woensdag op woensdag; wij hebben
alleen de marktwaardegewogen index (French publiceert geen gelijkgewogen
dagreeks) en aggregeren op vrijdag. Hun kwintielen zijn wekelijks en gelijkgewogen
binnen het kwintiel; de onze zijn maandelijks en marktwaardegewogen, wat de
afwijkingen kleiner maakt.

**Verwachte afwijking.** Lo en MacKinlay rapporteren voor de marktwaardegewogen
index over de volle 1216 weken $VR(2) = 1{,}08$ ($z^{*} = 2{,}33$),
$VR(4) = 1{,}16$ ($2{,}31$), $VR(8) = 1{,}22$ ($2{,}07$) en $VR(16) = 1{,}22$
($1{,}38$); voor hun gelijkgewogen index is $VR(2) = 1{,}30$ met
$z^{*} = 7{,}51$. Onze marktwaardegewogen reeks moet daar dichtbij komen — wij
verwachten $VR(q)$ binnen $0{,}05$ van hun waarden en $z$-waarden rond de twee. De
falsifieerbare eis zit in de *rangorde*: hun kwintielen geven $1{,}42$ (kleinst),
$1{,}28$ (midden) en $1{,}14$ (grootst), dus de variance ratio moet bij ons
monotoon dalen van het kleinste naar het grootste kwintiel. Wijkt dát af, dan zit
de fout in de code, niet in de data.
```

```{code-cell} ipython3
daily = np.log1p(hap_data.market_daily()["Mkt"])
weekly = daily.resample("W-FRI").sum()
monthly = np.log1p(hap_data.market_monthly()["Mkt"])

kendall = pd.DataFrame(
    {
        name: {
            "nobs": len(s),
            "SE onder H0": 1 / np.sqrt(len(s)),
            **{f"rho_{k}": s.autocorr(k) for k in range(1, 6)},
        }
        for name, s in [("dagelijks", daily), ("wekelijks", weekly),
                        ("maandelijks", monthly)]
    }
).T
kendall.round(4)
```

Dit is Kendalls resultaat, en het houdt in orde van grootte stand. De grootste
autocorrelatie is de eerste-orde van maandrendementen, $0{,}085$, tegen een
standaardfout van $0{,}029$ — significant, en tegelijk zo klein dat hij zeven
tienden van een procent van de variantie van het volgende maandrendement
verklaart. Onze weekwaarde $0{,}030$ ligt onder Kendalls gemiddelde van ongeveer
$0{,}13$, wat niet verbaast: zijn reeksen zijn sectorindices van dun verhandelde
Britse aandelen uit het interbellum, en die plakken meer dan de totale
Amerikaanse markt. Het is overigens een hardnekkig misverstand dat Kendall
nulcorrelaties vond; zijn hoogste was $0{,}301$. Wat hij schreef, is dat de
correlatie "so weak" is dat er niets mee te voorspellen valt.

De runs-test kijkt naar hetzelfde vanuit een andere hoek en is gevoeliger voor
het plakken van tekens.

```{code-cell} ipython3
def runs_test(r):  # TODO: naar hap.stats
    """Wald-Wolfowitz runs test on the signs of a return series."""
    signs = np.sign(r.to_numpy())
    signs = signs[signs != 0]
    n_pos, n_neg = int((signs > 0).sum()), int((signs < 0).sum())
    n = n_pos + n_neg
    observed = 1 + int((signs[1:] != signs[:-1]).sum())
    expected = 2 * n_pos * n_neg / n + 1
    variance = 2 * n_pos * n_neg * (2 * n_pos * n_neg - n) / (n**2 * (n - 1))
    return {"positief": n_pos, "negatief": n_neg, "runs": observed,
            "verwacht": expected, "z": (observed - expected) / np.sqrt(variance)}


pd.DataFrame(
    {name: runs_test(s) for name, s in
     [("dagelijks", daily), ("wekelijks", weekly), ("maandelijks", monthly)]}
).T.round(3)
```

Op dagbasis zijn er ruim duizend runs minder dan de random walk voorspelt, met een
$z$-waarde van $-13{,}1$. Tekens plakken dus. Dat de runs-test hier zoveel
scherper oordeelt dan de autocorrelatie, komt doordat hij 26 296 waarnemingen
gebruikt en ongevoelig is voor de dikke staarten die de gewone
correlatiecoëfficiënt vertroebelen.

Nu de variance ratios, op de steekproef van Lo en MacKinlay en op de periode die
er na hun publicatie bij is gekomen.

```{code-cell} ipython3
def vr_table(series, horizons=(2, 4, 8, 16)):
    """Variance ratios with heteroskedasticity-robust z-statistics."""
    out = {"nobs": len(series)}
    for q in horizons:
        result = hap.variance_ratio(series, q)
        out[f"VR({q})"] = result["vr"]
        out[f"z({q})"] = result["z2"]
    return out


samples = {
    "1962-09 t/m 1985-12": weekly.loc["1962-09-06":"1985-12-26"],
    "1986-01 t/m heden": weekly.loc["1986-01-01":],
    "Kendall-periode 1928-1938": weekly.loc["1928":"1938"],
}
pd.DataFrame({k: vr_table(v) for k, v in samples.items()}).T.round(3)
```

Op de exacte steekproef van Lo en MacKinlay — 1216 weekrendementen, precies hun
aantal — vinden wij $VR(2) = 1{,}066$, $VR(4) = 1{,}150$, $VR(8) = 1{,}219$ en
$VR(16) = 1{,}211$, met robuuste $z$-waarden tussen $1{,}2$ en $2{,}0$. Zij
rapporteerden voor hun marktwaardegewogen index $1{,}08$, $1{,}16$, $1{,}22$ en
$1{,}22$, met $z^{*}$ van $2{,}33$, $2{,}31$, $2{,}07$ en $1{,}38$. Alle vier de
puntschattingen liggen binnen $0{,}02$ van de gepubliceerde waarden, en het
patroon over $q$ — oplopend tot $q = 8$, daarna vlak — is identiek. Hun veel
scherpere resultaat kwam van de gelijkgewogen index, die kleine ondernemingen
zwaarder weegt: daar was $VR(2) = 1{,}30$ met $z^{*} = 7{,}51$, "which implies
that the first-order autocorrelation for weekly returns is approximately 30
percent". Die reeks hebben wij op weekbasis niet.

De tweede rij is het interessantste getal van deze lecture. Op de veertig jaar
die *na* hun publicatie kwamen is $VR(2) = 0{,}950$: niet alleen verdwenen, maar
omgeslagen. De derde rij is Kendalls eigen tijdvak op de Amerikaanse markt, en
daar is de afwijking het grootst van alle drie: $VR(16) = 1{,}507$ met
$z = 2{,}17$, op nog geen elf jaar data.

```{code-cell} ipython3
size = hap_data.french("Portfolios_Formed_on_ME", "monthly").loc["1962-09":"1985-12"]
quintiles = ["Lo 20", "Qnt 2", "Qnt 3", "Qnt 4", "Hi 20"]

size_table = pd.DataFrame(
    {q: vr_table(np.log1p(size[q].dropna()), horizons=(2, 4, 8)) for q in quintiles}
).T
size_table.index = ["1 (kleinst)", "2", "3", "4", "5 (grootst)"]
size_table.round(3)
```

Dit is de falsifieerbare eis uit het replicatieblok, en hij wordt gehaald: van het
kleinste naar het grootste kwintiel daalt $VR(2)$ monotoon van $1{,}205$ via
$1{,}162$, $1{,}147$ en $1{,}106$ naar $1{,}016$, met $z = 3{,}36$ bij de
kleinste en $z = 0{,}21$ bij de grootste, en hetzelfde patroon staat in de
kolommen voor $q = 4$ en $q = 8$. Lo en MacKinlay vonden op weekbasis $1{,}42$,
$1{,}28$ en $1{,}14$, met $z^{*}$ van $8{,}81$, $7{,}38$ en $3{,}82$. Onze
niveaus liggen lager — maandrendementen middelen de weekafhankelijkheid weg, en
onze kwintielen zijn marktwaardegewogen terwijl de hunne gelijkgewogen zijn — maar
de *rangorde* is exact de hunne.

```{code-cell} ipython3
:label: cel-bachelier-vr
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))

for i, (name, series) in enumerate(list(samples.items())[:2]):
    qs = np.array([2, 4, 8, 16])
    vrs = [hap.variance_ratio(series, q)["vr"] for q in qs]
    axes[0].plot(qs, vrs, "o-", color=hap.plotting.COLORS[i], label=name)
axes[0].axhline(1.0, color="black", lw=1.0, ls="--")
axes[0].set_title("Variance ratio van weekrendementen")
axes[0].set_xlabel("Horizon $q$ (weken)")
axes[0].set_ylabel("$VR(q)$")
axes[0].legend()

axes[1].bar(range(5), size_table["VR(2)"], color=hap.plotting.COLORS[0])
axes[1].axhline(1.0, color="black", lw=1.0, ls="--")
axes[1].set_xticks(range(5), size_table.index)
axes[1].set_title("$VR(2)$ per grootte-kwintiel, 1962-1985")
axes[1].set_xlabel("Kwintiel op marktwaarde")
axes[1].set_ylabel("$VR(2)$")
plt.show()
```

:::{figure} #cel-bachelier-vr
:label: fig-bachelier-vr
:width: 95%

Links: de variance ratios die Lo en MacKinlay vonden liggen boven één en lopen op
met de horizon; op de veertig jaar ná hun publicatie liggen ze eronder. Rechts:
de systematiek die hun artikel zijn kracht gaf — hoe kleiner de onderneming, hoe
groter de afwijking van de random walk. Beide panelen laten open of dat een
prijsfout was of een eigenschap van hoe kleine aandelen verhandeld worden.
:::

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Buitengewoon veel, voor buitengewoon weinig
aannames. Uit één zin — opeenvolgende koersveranderingen zijn ongecorreleerd —
volgen de $\sqrt{t}$-wet die Regnault in 1863 mat en die wij hierboven met een
helling van $0{,}51$ terugvonden, de normale limietverdeling, de
diffusievergelijking, de kans om een niveau te raken, en een optieformule die voor
korte looptijden nauwelijks van Black-Scholes te onderscheiden is. Het model
verklaart bovendien waarom de beroepsgroep die van voorspellen leeft er
collectief niet in slaagt: als
er niets te voorspellen valt, is het gemiddelde advies per definitie waardeloos.
Dat is precies wat Cowles in 1933 vaststelde {cite}`Cowles1933`. Hij verzamelde
ongeveer 7500 aanbevelingen van zestien beleggingsadviesdiensten over de
vierenhalf jaar tot juli 1932 en vond dat hun gemiddelde $1{,}43$ procent per jaar
slechter was dan het gemiddelde aandeel; twintig brandverzekeraars bleven over
1928–1931 gemiddeld $1{,}20$ procent per jaar bij de markt achter; en
vierentwintig financiële publicaties bleven "by 4 per cent per annum" achter bij
het gemiddelde van alle uitkomsten die met louter toeval bereikbaar waren — een
vergelijking die hij maakte door vierentwintig toevalsportefeuilles met een
kaartspel samen te stellen.

**Waar het breekt.** Op twee plaatsen, en de eerste is de belangrijkste. De
random walk is een uitspraak over *veranderingen* en zegt niets over het
*niveau*. Zij is verenigbaar met elke prijs vandaag: of de markt op twintig of op
veertig keer de winst staat, in beide gevallen is de verandering van morgen
onvoorspelbaar. Er is dus een theorie van de ruis en geen theorie van de waarde —
het gat waar de volgende lecture in springt. De tweede breuk is empirisch en
kleiner, maar wij hebben hem zelf gemeten: de runs-test op dagdata geeft
$z = -13{,}1$, de eerste autocorrelatie van maandrendementen is $0{,}085$ met een
standaardfout van $0{,}029$, en de variance ratios over 1962–1985 liggen boven één
met een strikt monotoon patroon over de grootte-kwintielen. Wat de simulatie
daaraan toevoegt is de maat: deze afwijkingen zijn zo klein dat er dertig jaar
weekdata nodig is om er twee standaardfouten van te halen, en dat koppelt de vraag
of ze *bestaan* bijna los van de vraag of iemand er iets aan heeft.

Bachelier breekt bovendien op een technisch punt: arithmetische Brownse beweging
laat negatieve prijzen toe en maakt de volatiliteit van een aandeel van honderd
euro even groot als die van een aandeel van één euro. Osborne herstelde dat in
1959 door de Brownse beweging naar de logaritme te verplaatsen
{cite}`Osborne1959`, en dat is de vorm waarin het model in
[](#02-09-black-scholes) terugkeert. Hij deed ook Regnaults meting nog eens over,
op de Cowles-index van 1831 tot 1936 en over intervallen van twintig minuten tot
twaalf jaar, en concludeerde dat de data "follow a slope $\tfrac12$, or
square-root-of-time diffusion law very nicely indeed".

**Risico of vergissing?** De variance ratios boven één, oplopend naarmate de
ondernemingen kleiner zijn, laten beide lezingen toe en de data van deze lecture
kan er niet tussen kiezen. De Chicago-lezing: dit is geen voorspelbaarheid maar
een meetartefact plus een risicopremie. Kleine aandelen worden niet elke dag
verhandeld, dus de vastgelegde koers loopt achter op de informatie, wat
mechanisch positieve autocorrelatie in indexrendementen veroorzaakt; wat
overblijft is de vergoeding voor het risico van een illiquide onderneming. De
Yale-lezing: informatie sijpelt langzaam door in aandelen die weinig analisten
volgen, de prijs past zich te traag aan, en wie dat weet kan er geld aan
verdienen — een vergissing dus, en een die weggearbitreerd zou moeten worden. Dat
$VR(2)$ ná 1985 onder één zakt past bij beide: de arbitrageurs hebben de
mispricing weggenomen, óf de handelsinfrastructuur is veranderd en het
meetartefact is verdwenen. Wie de kampen wil scheiden, heeft data nodig over wie
er handelde en met welke vertraging, en die is er voor 1985 niet. In
[](#02-06-efficiente-markten) krijgt de spanning haar formele naam, de *joint
hypothesis*.

**Wat er daarna kwam.** Eerst het gat, niet de barst. Voordat iemand kon zeggen of
een prijs *fout* was, moest er een theorie zijn van wat een prijs *hoort* te
zijn — en die schreef John Burr Williams in 1938 op: zie
[](#01-03-williams-ddm).

## Oefeningen

:::{exercise}
:label: ex-bachelier-1

**De variance ratio van een AR(1).** Laat $r_t = \rho\,r_{t-1} + e_t$ met
$|\rho| < 1$ en $e_t$ wit ruis.

1. Toon aan dat $\rho_j = \rho^{\,j}$ en leid met [](#eq-bachelier-vr-rho) een
   gesloten uitdrukking af voor $VR(q)$.
2. Bereken $VR(2)$, $VR(4)$, $VR(8)$ en $VR(16)$ voor $\rho = 0{,}10$, en bepaal
   $\lim_{q \to \infty} VR(q)$.
3. Controleer (2) met een simulatie van één lang pad. Welke horizon $q$ geeft de
   grootste $z$-waarde bij $T = 1216$, en waarom is dat niet de horizon met de
   grootste $VR(q)$?
:::

:::{solution} ex-bachelier-1
:class: dropdown

**(1)** Voor een AR(1) is $\Cov(r_t, r_{t-j}) = \rho^{\,j}\sigma_r^2$, dus
$\rho_j = \rho^{\,j}$. Invullen in [](#eq-bachelier-vr-rho) geeft

$$
VR(q) = 1 + 2\sum_{j=1}^{q-1}\Bigl(1-\frac{j}{q}\Bigr)\rho^{\,j}
      = 1 + \frac{2\rho}{1-\rho}
        \left[1 - \frac{1-\rho^{\,q}}{q\,(1-\rho)}\right],
$$

na sommatie van de meetkundige reeks en van $\sum j\rho^j$. Voor $q \to \infty$
verdwijnt de tweede term en blijft $VR(\infty) = (1+\rho)/(1-\rho)$ over.

**(2) en (3)**

```{code-cell} ipython3
rho_ex = 0.10


def vr_ar1(rho, q):
    """Population variance ratio of an AR(1) at horizon q."""
    j = np.arange(1, q)
    return 1 + 2 * np.sum((1 - j / q) * rho**j)


path = pd.Series(ar1_paths(rho_ex, 1, 1216)[0])
rows = []
for q in (2, 4, 8, 16):
    result = hap.variance_ratio(path, q)
    rows.append({"q": q, "VR theoretisch": vr_ar1(rho_ex, q),
                 "VR geschat": result["vr"], "z": result["z2"]})

pd.DataFrame(rows).set_index("q").round(4)
```

```{code-cell} ipython3
print(f"limiet (1+rho)/(1-rho) = {(1 + rho_ex) / (1 - rho_ex):.4f}")
```

De theoretische waarden zijn $1{,}100$, $1{,}161$, $1{,}191$ en $1{,}207$, met
limiet $1{,}222$: $VR(q)$ stijgt monotoon maar met sterk afnemende opbrengst. De
geschatte waarden liggen er in dit ene pad boven ($1{,}13$ tot $1{,}42$), wat
toont hoe groot de steekproefruis bij grote $q$ is. De grootste $z$-waarde valt
bij de *kleinste* horizon ($4{,}51$ tegen $3{,}29$), omdat de standaardfout van
$VR(q)$ ruwweg met $\sqrt{q}$ meegroeit terwijl $VR(q) - 1$ na $q = 4$ nauwelijks
meer toeneemt. Wie afhankelijkheid zoekt, kiest de horizon waarop het *signaal*
groeit, niet waarop de statistiek het grootst oogt.
:::

:::{exercise}
:label: ex-bachelier-2

**Bachelier tegen Black-Scholes.**

1. Leid uit [](#eq-bachelier-call) de Bachelier-prijs van een putoptie af met de
   pariteit $C - P = S_t - K$ (die bij rente nul geldt), en controleer dat de
   put-prijs nooit negatief is.
2. Neem $S = 100$, $\sigma_{\text{BS}} = 20\%$ en $\tau = 1$. Bepaal voor
   uitoefenprijzen van 70 tot 130 de *impliciete Bachelier-volatiliteit*: de
   $\sigma_{\text{Bach}}$ waarvoor [](#eq-bachelier-call) exact de
   Black-Scholes-prijs geeft. Teken die als functie van de uitoefenprijs.
3. Wat betekent de vorm van die kromme voor de bewering dat de twee modellen
   "ongeveer hetzelfde" zeggen?
:::

:::{solution} ex-bachelier-2
:class: dropdown

**(1)** Uit pariteit volgt
$P_t = C_t - (S_t - K) = (S_t-K)\left[\Phi(d) - 1\right] + \sigma\sqrt{\tau}\varphi(d)
= (K - S_t)\Phi(-d) + \sigma\sqrt{\tau}\varphi(d)$, met $d = (S_t-K)/(\sigma\sqrt{\tau})$.
Beide termen zijn niet-negatief als $K \ge S_t$; voor $K < S_t$ is $-d < 0$ en
domineert de tweede term, zodat $P_t > 0$ blijft.

**(2) en (3)**

```{code-cell} ipython3
strikes = np.arange(70.0, 131.0, 5.0)
implied = [
    brentq(lambda sig: bachelier_call(S0, K, sig, 1.0) - bs_call(S0, K, sigma_bs, 1.0),
           1e-4, 200.0)
    for K in strikes
]
implied_series = pd.Series(implied, index=pd.Index(strikes, name="K"),
                           name="impliciete sigma_Bachelier")
implied_series.round(3)
```

```{code-cell} ipython3
:tags: [hide-input]

fig, ax = plt.subplots()
ax.plot(strikes, implied_series, "o-")
ax.axhline(sigma_bs * S0, color=hap.plotting.COLORS[1], ls="--",
           label=r"$\sigma_{BS}\cdot S = 20$")
ax.set_title("Impliciete Bachelier-volatiliteit van Black-Scholes-prijzen")
ax.set_xlabel("Uitoefenprijs $K$")
ax.set_ylabel(r"$\sigma_{\mathrm{Bach}}$ (prijs-eenheden per $\sqrt{\mathrm{jaar}}$)")
ax.legend()
plt.show()
```

De kromme is niet vlak: op het geld ligt de impliciete Bachelier-volatiliteit op
$19{,}97$, vrijwel precies $\sigma_{\text{BS}} \cdot S = 20$, maar zij loopt
monotoon op van $16{,}79$ bij $K = 70$ tot $22{,}83$ bij $K = 130$ — een
scheefheid die volgt uit het feit dat de log-normale verdeling naar rechts
uitloopt en de normale symmetrisch is. Dat is dezelfde figuur die in
[](#02-09-black-scholes) terugkomt als de *volatility smile*, met de rollen
omgedraaid: hier is Black-Scholes de markt en Bachelier het model. "Ongeveer
hetzelfde" is dus een uitspraak over een gebied en niet over een formule — de twee
modellen zijn uitwisselbaar rond het geld en onderscheidbaar precies daar waar de
staarten ertoe doen.
:::

:::{exercise}
:label: ex-bachelier-3

**De replicatie uitgebreid: is de afwijking verdwenen?** Lo en MacKinlay
publiceerden in 1988 op data tot eind 1985.

1. Herhaal de variance-ratio-tabel voor de grootte-kwintielen op de periode
   1986-01 tot heden en vergelijk hem met de tabel uit de replicatie. Blijft de
   rangorde over de kwintielen bestaan?
2. Bereken per kwintiel het verschil in $VR(2)$ tussen de twee periodes. Hoe
   groot is dat verschil vergeleken met de standaardfout van $VR(2)$ in elke
   periode afzonderlijk?
3. Twee verklaringen liggen voor de hand: de anomalie is weggearbitreerd, of de
   handelsinfrastructuur is veranderd. Welke meting zou de twee kunnen scheiden,
   en hebben wij die?
:::

:::{solution} ex-bachelier-3
:class: dropdown

```{code-cell} ipython3
size_late = hap_data.french("Portfolios_Formed_on_ME", "monthly").loc["1986-01":]
late_table = pd.DataFrame(
    {q: vr_table(np.log1p(size_late[q].dropna()), horizons=(2, 4, 8))
     for q in quintiles}
).T
late_table.index = size_table.index
late_table.round(3)
```

```{code-cell} ipython3
comparison = pd.DataFrame(
    {
        "VR(2) 1962-1985": size_table["VR(2)"],
        "VR(2) 1986-heden": late_table["VR(2)"],
        "SE 1962-1985": 1 / np.sqrt(size_table["nobs"].astype(float)),
        "SE 1986-heden": 1 / np.sqrt(late_table["nobs"].astype(float)),
    }
)
comparison["verschil"] = comparison["VR(2) 1962-1985"] - comparison["VR(2) 1986-heden"]
comparison["t van het verschil"] = comparison["verschil"] / np.sqrt(
    comparison["SE 1962-1985"] ** 2 + comparison["SE 1986-heden"] ** 2
)
comparison.round(3)
```

De rangorde over de kwintielen blijft na 1985 bestaan — $1{,}143$, $1{,}066$,
$1{,}053$, $1{,}049$, $1{,}017$ — maar het hele profiel is naar beneden geschoven,
en alleen het kleinste kwintiel houdt met $z = 2{,}50$ nog significantie over; bij
$q = 8$ is er van het patroon niets meer over.

Het tweede blok is het antwoord op vraag (2), en het is ontnuchterend: geen van de
vijf verschillen haalt twee standaardfouten, de hoogste $t$-waarde is $1{,}28$.
Dat is [](#eq-bachelier-power) van de andere kant bekeken. Met 280 respectievelijk
487 maandwaarnemingen is de standaardfout van $VR(2)$ $0{,}060$ en $0{,}045$, dus
die van het *verschil* $0{,}075$ — en de verschuiving die wij zien is $0{,}06$ tot
$0{,}10$. De afwijking is dus zichtbaar verdwenen en tegelijk statistisch niet te
onderscheiden van "er is niets veranderd". Wie beweert dat een anomalie na
publicatie verdwijnt, zegt iets wat per signaal niet hard te maken is; in
[](#06-34-factor-zoo) gebeurt het daarom op tweehonderd signalen tegelijk.

Om de twee verklaringen te scheiden zou men willen weten hoe vaak de aandelen in
het kleinste kwintiel daadwerkelijk verhandeld werden. Komt de autocorrelatie van
niet-synchrone handel, dan moet ze verdwijnen zodra de handelsfrequentie stijgt —
en die is sinds 1985 met ordes van grootte toegenomen. Komt ze van trage
informatieverwerking, dan moet ze verdwijnen zodra er meer analisten en meer
arbitragekapitaal zijn — wat ook is gebeurd. De twee verklaringen voorspellen hier
hetzelfde, en de enige data die ze zou scheiden — handelsfrequentie per aandeel
vóór 1985 — zit in CRSP en hebben wij niet. Dit is de eerste keer in deze reeks
dat een vraag niet op de data stukloopt maar op het ontbreken ervan.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
