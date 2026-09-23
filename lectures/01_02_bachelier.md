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

**Wat we al weten.** [](#00-00-setup) legde de gereedschapskist klaar, met één
feit dat de hele reeks draagt: het gemiddelde rendement is slecht meetbaar, de
variantie goed. [](#00-01-rendementen) leidde daaruit de $\sqrt{t}$-regel af,
onder de aanname dat rendementen onafhankelijk zijn. Deze lecture draait dat
om: de regel werd in 1863 gemeten, veertig jaar voordat een theorie hem
verklaarde.

**Welke vraag staat open.** Als de spreiding van de koers met $\sqrt{t}$ groeit, welk
model van de prijs past daarbij, en hoe toetst men dat model op data?
```

## Overzicht

Hoe beweegt een koers als niemand de volgende stap kan voorspellen? Als een
*random walk* (een som van onafhankelijke schokken), zodat de spreiding groeit
met de wortel van de tijd en een optie te prijzen is uit die spreiding alleen.
Over het niveau van de koers zegt het model niets: het is een theorie van de
ruis, niet van de waarde. In deze lecture:

- tellen we in een wandeling van vier stappen na dat de variantie lineair
  groeit en de spreiding met de wortel van het aantal stappen;

- leiden we af dat een random walk in de limiet een Brownse beweging wordt, met
  twee gevolgen: de kans om een niveau te raken en Bacheliers optieformule;

- laten we zien dat de variance ratio de $\sqrt{t}$-wet als toets opschrijft;

- simuleren we hoeveel jaren data nodig zijn om een kleine afwijking van de
  random walk te zien;

- repliceren we Regnaults $\sqrt{t}$-wet op Shillers maandreeks vanaf 1871, en
  de autocorrelaties en variance ratios van Kendall en van Lo en MacKinlay
  {cite}`LoMacKinlay1988` op French-data.

In 1863 schreef Jules Regnault, beambte aan de Parijse beurs, dat de
spreiding van de koers recht evenredig is met de wortel van de verstreken tijd
{cite}`Regnault1863`. Louis Bachelier construeerde in 1900 de Brownse beweging
als limiet van een random walk {cite}`Bachelier1900`. Hij schreef de
diffusievergelijking op, vijf jaar vóór Einstein, en leidde er de eerste
optieformule mee af. Daarna kwamen de empirici. Cowles liep de voorspellers na
{cite}`Cowles1933`, Working stelde de random walk voor als
nulhypothese {cite}`Working1934`, en Kendall vond in tweeëntwintig prijsreeksen een
samenhang die te zwak was om mee te voorspellen {cite}`Kendall1953`.

Bachelier definieert het tijdvak. Alleen hij leverde een model waaruit het feit
volgt, en uit datzelfde model volgden meteen ook optieprijzen. Maar zijn
proefschrift bleef een halve eeuw ongelezen. Bij elk model in deze reeks stellen we de vraag *theorie of
feit*: is dit een theorie die getoetst wordt, of een feit dat op een verklaring
wacht? De random walk begint als het tweede: een meting zonder verklaring. Pas
in 1965 bewees Samuelson dat correct geanticipeerde prijzen willekeurig moeten
fluctueren {cite}`Samuelson1965`.

## Intuïtie: waarom zou dit waar zijn?

Denk aan iemand die elke dag een munt opgooit. Bij kop zet hij een stap naar
rechts, bij munt een stap naar links. Na honderd dagen staat hij gemiddeld op
zijn beginpunt, want de stappen heffen elkaar op. Toch staat hij er vrijwel
zeker niet. Hoe ver is hij er doorgaans vandaan?

De afstand kan niet evenredig met het aantal dagen groeien, want dan liep hij
altijd dezelfde kant op. Hij kan ook niet gelijk blijven, want dan kwam hij
nooit ver. Zijn de stappen onafhankelijk, dan tellen hun varianties op. De
afstand groeit dan met de wortel van de tijd: twee keer zo lang wachten geeft
ongeveer anderhalf keer zo veel spreiding.

Meer zegt Regnaults wet niet. Hij drukte haar in 1863 in hoofdletters af:
*l'écart des cours est en raison directe de la racine carrée des temps*, de
gemiddelde absolute afwijking van de koers is recht evenredig met de wortel van de tijd
{cite}`Regnault1863`. Hij gaf er de praktische vertaling bij. De afwijking over
een hele periode is 1,41 keer die over de helft ervan, 1,73 keer die over een
derde en 2 keer die over een kwart. Wie de afwijking wil verdubbelen, moet dus
vier keer zo lang wachten.

Regnault schreef over de Franse 3%-rente, maar het mechanisme is dat van de
muntworp: een koersverandering vandaag zegt niets over die van morgen. Het
economische argument werd pas veel later expliciet. Wist iedereen dat de koers
morgen stijgt, dan wilde vandaag niemand verkopen, en steeg de koers vandaag al.
Onvoorspelbaarheid is dus een eigenschap van een prijs waarover wordt
onderhandeld, niet van bedrijven of van de economie.

Bachelier maakte van dit feit een model. Maak de schokken oneindig klein en
oneindig frequent, dan ontstaat de Brownse beweging: continue paden, normaal
verdeelde aangroeiingen. Daarmee valt meer uit te rekenen dan de spreiding,
zoals de kans dat de koers ooit een niveau raakt, of de waarde van een optie.

Wat verwachten we dus?

- De spreiding van koersveranderingen groeit met de wortel van de horizon.

- Een optie op de huidige koers betaalt alleen bij uitschieters naar boven. Haar
  waarde is dus evenredig met de spreiding van de koers op de vervaldag, en
  groeit met de wortel van de looptijd: een vier keer zo lange looptijd kost het
  dubbele. De evenredigheidsfactor, ongeveer 0,4, leidt de theorie af.

- Elke autocorrelatie van koersveranderingen is nul.

```{note}
Bachelier verdedigde zijn proefschrift in 1900 bij Henri Poincaré. Die gaf het
*honorable* en niet *très honorable*: goed, maar geen begin van een loopbaan.
De wiskunde van 1900 had nog geen taal voor een stochastisch proces, want
Kolmogorovs axioma's kwamen pas in 1933. Zijn beoordelaars konden dus niet zien
of zijn constructie sluitend was. Het werk bleef ongelezen, tot Leonard Savage
het eind jaren vijftig herontdekte en Paul Samuelson erop wees.
```

## Toy-voorbeeld: een random walk van vier stappen

De $\sqrt{t}$-wet is al zichtbaar in een wandeling van vier stappen. De cel
hieronder laadt de pakketten. Het is de enige cel met imports in deze lecture.

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

**Opzet.** Op elk tijdstip $k = 1, \dots, 4$ zet de wandelaar een stap
$\varepsilon_k$ van $+1$ of $-1$, elk met kans $\tfrac12$, onafhankelijk van de
andere stappen. Zijn positie is $S_n = \varepsilon_1 + \dots + \varepsilon_n$,
met $S_0 = 0$. Er zijn $2^4 = 16$ even waarschijnlijke paden. De eindpositie
hangt alleen af van het aantal keer kop $j$: $S_4 = 2j - 4$. We rekenen twee
grootheden uit: de variantie, die het mechanisme laat zien, en de gemiddelde
absolute afwijking, die Regnault mat.

| $S_4$ | $-4$ | $-2$ | $0$ | $2$ | $4$ |
|---|---|---|---|---|---|
| aantal paden | 1 | 4 | 6 | 4 | 1 |
| kans | $1/16$ | $4/16$ | $6/16$ | $4/16$ | $1/16$ |

**Stap 1: de variantie.** De tabel laat zien dat de paden zich rond het
beginpunt ophopen: zes van de zestien eindigen op nul. De verwachting is nul,
want de verdeling is symmetrisch. De variantie is het kansgewogen kwadraat van de eindpositie:

$$
\Var(S_4) = \frac{16 \cdot 1 + 4 \cdot 4 + 0 \cdot 6 + 4 \cdot 4 + 16 \cdot 1}{16}
          = \frac{64}{16} = 4 .
$$

**Stap 2: de regel achter het getal.** Elke stap heeft variantie 1 en de stappen
zijn ongecorreleerd, dus $\Var(S_n) = n$, exact en voor elke $n$. De
standaarddeviatie is $\sqrt{n}$. Dat is Regnaults wet in zijn kaalste vorm:
zonder limiet, zonder normale verdeling, zonder continue tijd.

**Stap 3: de gemiddelde absolute afwijking.** Regnault sprak niet over de
standaarddeviatie maar over de *écart*, de gemiddelde absolute afwijking. In de
rest van de lecture heet $\E|\cdot|$ zo, en "spreiding" is de
standaarddeviatie.

$$
\E|S_4| = \frac{4 \cdot 1 + 2 \cdot 4 + 0 \cdot 6 + 2 \cdot 4 + 4 \cdot 1}{16}
        = \frac{24}{16} = 1{,}50 .
$$

Op dezelfde manier is $\E|S_1| = 1$. Na twee stappen staat de wandelaar op
$-2$, $0$ of $2$ met kansen $\tfrac14$, $\tfrac12$, $\tfrac14$, dus
$\E|S_2| = (2 + 0 + 2)/4 = 1$. Na drie stappen staat hij op $\pm 1$ met kans
$\tfrac68$ en op $\pm 3$ met kans $\tfrac28$, dus
$\E|S_3| = (6 \cdot 1 + 2 \cdot 3)/8 = 1{,}50$.

**Stap 4: de verhouding tot de wortel.** $\E|S_n|/\sqrt{n}$ loopt van $1{,}000$
via $0{,}707$ en $0{,}866$ naar $0{,}750$. Ze schommelt, want de wandeling is nog
grof.

**Het recept.** Voor lange wandelingen nadert die verhouding
$\sqrt{2/\pi} \approx 0{,}798$; de theorie leidt dat als eerste af. De absolute
afwijking volgt $\sqrt{n}$ dus pas op den duur, de variantie volgt $n$ meteen.
Een verhouding tussen twee horizonnen kan dus toevallig afwijken. Daarom
schatten we in de replicatie één helling over vier horizonnen.

De code telt alle zestien paden na en zet de getallen met de hand ernaast.

```{code-cell} ipython3
paths = np.array(list(product([-1, 1], repeat=4)))   # 16 paden van 4 stappen
positions = paths.cumsum(axis=1)                     # kolom n-1 bevat S_n
final = positions[:, -1]                             # eindpositie S_4

n = np.arange(1, 5)
var_by_code = positions.var(axis=0)
mean_abs_by_code = np.abs(positions).mean(axis=0)

toy = pd.DataFrame(
    {
        "Var(S_n) met de hand": [1, 2, 3, 4],
        "Var(S_n) code": var_by_code,
        "E|S_n| met de hand": [1.0, 1.0, 1.5, 1.5],
        "E|S_n| code": mean_abs_by_code,
        "E|S_n| / sqrt(n)": mean_abs_by_code / np.sqrt(n),
    },
    index=pd.Index(n, name="n"),
)
toy.round(4)
```

De kolommen met de hand en code zijn gelijk. De lezer weet nu dat de variantie
van een som van onafhankelijke stappen lineair groeit, en de spreiding dus met
de wortel van het aantal stappen.

## Theorie

We leiden vier dingen af. Eerst dat een random walk in de limiet een Brownse
beweging wordt, waarvan de gemiddelde absolute afwijking met de wortel van de
horizon groeit; dat is de kern, en het recept uit het toy-voorbeeld. Daarna
twee toepassingen van dat model: de kans om een niveau te raken en Bacheliers
optieprijs. Ten slotte vertalen we "onvoorspelbaar" in drie toetsen, waarvan de
variance ratio de belangrijkste is. Simulatie en replicatie toetsen daarna
alleen de kern: zijn koersveranderingen ongecorreleerd, en groeit de spreiding
met de wortel van de tijd? Bewijzen en nevenresultaten staan ingeklapt.

### Opzet en aannames

De nulhypothese van deze lecture is de random walk in log-prijzen. Laat $P_t$ de
prijs zijn op tijdstip $t$ en $r_{t+1} = \log P_{t+1} - \log P_t$ het
log-rendement over $[t, t+1]$. *Vanaf hier zijn kleine letters logs*:
$p_t = \log P_t$. Onder de nulhypothese zijn de $r_{t+1}$ onderling
ongecorreleerd, met verwachting $\mu$ en variantie $\sigma^2$. Voor
maandrendementen op de Amerikaanse markt is $\mu$ ongeveer 1% en $\sigma$
ongeveer 5%. De toetsen gebruiken alleen varianties en autocorrelaties, dus
$\mu$ speelt verder geen rol. Een "koersverandering" is in deze lecture het
log-rendement $r_{t+1}$; alleen in Bacheliers optieformule is het een absolute
verandering.

Het symbool $\sigma$ is steeds een standaarddeviatie per tijdseenheid, maar van
drie verschillende grootheden. In de toetsen is het die van een log-rendement per
maand, ongeveer 5%. In de limietstelling is het die van één stap. In Bacheliers
optieformule is het die van een prijsverandering, in euro per
$\sqrt{\text{jaar}}$: bij een aandeel van 100 ongeveer 20 euro.

Bachelier werkte niet met logs maar met niveaus. Zijn proces heet nu
*aritmetische Brownse beweging*: de absolute prijsveranderingen zijn normaal
verdeeld. In de geometrische Brownse beweging zijn dat de relatieve
veranderingen. Waar we zijn optieformule afleiden, volgen we zijn conventie en
schrijven we $S_t$ voor het prijsniveau. Elders werken we in logs.

### Het kernresultaat: van random walk naar Brownse beweging

Worden de stappen kleiner en talrijker, dan wordt de wandeling een Brownse
beweging, welke verdeling de stappen ook hebben.

*Waarom zou dit waar zijn?* Een belegger houdt een aandeel een maand vast. Zijn
maandrendement is de som van twintig dagrendementen. De uitschieters van
afzonderlijke dagen middelen weg, en zijn maandrendement wordt normaal verdeeld,
hoe scheef de dagrendementen zelf ook zijn. Houdt hij langer vast, dan stijgt de
spreiding van zijn resultaat, maar met de wortel van de looptijd, want de
varianties tellen op. Wie de dag opknipt in uren en minuten, verandert daar
niets aan: alleen de schaal verschuift. Daarom is het model iets waard: elke
schok met eindige variantie volstaat, niet alleen een muntworp.

We herschalen de wandeling in de ruimte met $\sqrt{n}$ en in de tijd met $n$,
met $\sigma$ de standaarddeviatie van één stap (voor maandrendementen de 5% uit
de Opzet):

```{math}
:label: eq-bachelier-donsker
W^{(n)}(u) \;=\; \frac{1}{\sigma\sqrt{n}}\,S_{\lfloor n u \rfloor},
\qquad u \in [0,1].
```

In woorden: $W^{(n)}(u)$ is de positie na een fractie $u$ van de $n$ stappen,
gemeten in standaarddeviaties van de hele wandeling.

:::{prf:theorem} Invariantieprincipe (Donsker)
:label: thm-bachelier-donsker

Laat $\varepsilon_1, \varepsilon_2, \dots$ onafhankelijk en identiek verdeeld
zijn met $\E[\varepsilon] = 0$ en $\Var(\varepsilon) = \sigma^2 < \infty$, en
$S_n = \sum_{k \le n}\varepsilon_k$. Dan convergeert het proces
$W^{(n)}$ uit [](#eq-bachelier-donsker) in verdeling naar de standaard Brownse
beweging $W$ op $[0,1]$.
:::

In woorden: bij veel kleine stappen is de herschaalde wandeling niet meer van
een Brownse beweging te onderscheiden, welke stapverdeling er ook onder ligt.
De stelling vraagt meer dan de nulhypothese uit de Opzet: onafhankelijke, gelijk
verdeelde stappen met verwachting nul. Voor log-rendementen trekken we daarom
eerst $\mu$ af, zoals de replicatie doet. Formeel gaat het om convergentie van
de verdeling van het hele pad, dus ook van grootheden als het maximum, en dat
apparaat bestond in 1900 niet. Donskers stelling is van 1951.
De eindig-dimensionale kant, de gezamenlijke verdeling op een paar vaste
tijdstippen zoals na een kwart en na de helft van de wandeling, is kort te laten
zien en volstaat voor deze lecture.

:::{prf:proof}
:class: dropdown

*Schets: de eindig-dimensionale verdelingen.* Voor één tijdstip $u$ geldt

$$
W^{(n)}(u) = \frac{1}{\sigma\sqrt{n}} \sum_{k \le \lfloor nu\rfloor} \varepsilon_k
= \sqrt{\frac{\lfloor nu \rfloor}{n}} \cdot
  \frac{1}{\sigma\sqrt{\lfloor nu\rfloor}}\sum_{k \le \lfloor nu\rfloor}\varepsilon_k
\;\Rightarrow\; \sqrt{u}\cdot Z, \qquad Z \sim \mathcal{N}(0,1),
$$

door de centrale limietstelling, en dus $W^{(n)}(u) \Rightarrow \mathcal{N}(0,u)$.
Voor twee tijdstippen $u < v$ zijn $W^{(n)}(u)$ en $W^{(n)}(v) - W^{(n)}(u)$ sommen
over disjuncte blokken en dus onafhankelijk. In de limiet is dat de definiërende
eigenschap van de Brownse beweging: onafhankelijke, normaal verdeelde
aangroeiingen met $\Var(W_v - W_u) = v - u$. $\square$
:::

Daarmee is Regnaults wet een stelling geworden in plaats van een meting:

$$
\SD(W_{t+h} - W_t) = \sqrt{h}, \qquad \E|W_{t+h} - W_t| = \sqrt{2h/\pi}.
$$

Zoals de intuïtie voorspelde, groeit de spreiding met de wortel van de horizon.
Bij $h = 4$ geeft de tweede formule $\sqrt{8/\pi} \approx 1{,}60$, tegen $1{,}50$
in het toy-voorbeeld: vier stappen zitten nog 6% onder de limiet.

De figuur hieronder toont veertig herschaalde wandelingen van 2000 stappen. Let
op de bundel, niet op één pad.

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
[](#eq-bachelier-donsker). Geen enkel pad is glad, maar de bundel heeft een
scherpe omhullende: de rode krommen zijn $\pm\sqrt{u}$, één standaarddeviatie.
Wie naar één pad kijkt, ziet patronen. Wie naar de bundel kijkt, ziet
$\sqrt{t}$.
:::

:::{note} De diffusievergelijking, vijf jaar vóór Einstein
:class: dropdown

Dezelfde limiet laat zich ook bekijken via de dichtheid in plaats van via de
paden. De kansdichtheid van de positie volgt uit één boekhoudkundige eis. Wie op $t+s$
op plaats $x$ staat, was op $t$ ergens en legde daarna het verschil af. Optellen
over alle tussenposities geeft een convolutie. Bij een kleine tussenstap is die
convolutie een middeling van de dichtheid over de directe omgeving. Een
dichtheid die naar haar omgeving toe middelt, gedraagt zich als warmte in een
staaf: pieken vlakken af met een snelheid evenredig aan hun kromming.

Schrijf $p(x,t)$ voor de dichtheid van $S_t$ met $S_0 = 0$ (in deze note is $p$
een dichtheid, geen log-prijs). Onafhankelijke aangroeiingen geven de
Chapman-Kolmogorov-vergelijking

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

Trek $p(x,t)$ af, deel door $s$ en laat $s$ naar nul gaan:

```{math}
:label: eq-bachelier-diffusie
\frac{\partial p}{\partial t} \;=\; \frac{\sigma^2}{2}\,
\frac{\partial^2 p}{\partial x^2}.
```

In woorden: de dichtheid verandert in de tijd evenredig met haar kromming. Een
piek zakt, een dal vult zich. [](#eq-bachelier-diffusie) is de
warmtevergelijking uit de natuurkunde. Met beginvoorwaarde
$p(x,0) = \delta(x)$, een puntmassa in nul (de wandeling start met zekerheid in
het beginpunt), is de oplossing de normale dichtheid
$p(x,t) = \varphi(x/(\sigma\sqrt{t}))/(\sigma\sqrt{t})$.

Bachelier leidde deze vergelijking in 1900 af voor beurskoersen. Einstein kwam in
1905 langs dezelfde weg tot dezelfde vergelijking voor stuifmeeldeeltjes. De
$\sqrt{t}$ zit erin: de vergelijking verandert niet onder $x \mapsto \lambda x$,
$t \mapsto \lambda^2 t$, dus elke oplossing volgt die schaling.

[](#eq-bachelier-diffusie) gaat over de *kansdichtheid*, niet over de prijs van
een contract. De waarde van een claim als functie van koers en resterende
looptijd voldoet aan dezelfde operator, $\tfrac12\sigma^2$ maal de tweede
afgeleide naar de koers, met een omgekeerd tijdsteken. Samen zijn
dat de Kolmogorov-vergelijkingen: de voorwaartse beschrijft waar het proces
vanaf een vast begin heen gaat, de achterwaartse wat een vaste uitbetaling op de
vervaldag vandaag waard is. Daarom gaat ook de
vergelijking van Black en Scholes {cite}`BlackScholes1973` na één substitutie
over in de warmtevergelijking.
:::

### Wat het voorspelt: de kans om een niveau te raken

De kans dat de koers vóór een bepaalde datum ooit een niveau $a$ raakt, is
ongeveer twee keer de kans dat hij op die datum boven $a$ staat.

*Waarom zou dit waar zijn?* Een belegger legt een verkooporder neer op een
niveau $a$ boven de huidige koers. Wie alleen naar de eindkoers kijkt,
onderschat hoe vaak die order wordt uitgevoerd: de paden die $a$ raken en
daarna terugzakken, tellen niet mee. Na de aanraking is een stap omhoog even
waarschijnlijk als een stap omlaag. Voor elk pad dat terugzakt is er dus een
even waarschijnlijk pad dat verder stijgt en boven $a$ eindigt. De kans dat de
order wordt uitgevoerd, is daardoor ongeveer twee keer de kans dat de koers
boven $a$ eindigt.

:::{prf:theorem} Reflectieprincipe
:label: thm-bachelier-reflectie

Laat $S_n$ een symmetrische random walk zijn met stappen $\pm 1$ en
$M_n = \max_{k \le n} S_k$. Voor $a \ge 1$ geldt

```{math}
:label: eq-bachelier-reflectie
P(M_n \ge a) \;=\; P(S_n = a) \,+\, 2\,P(S_n > a).
```
:::

In woorden: de kans om $a$ ooit te raken is de kans om er precies op te eindigen,
plus twee keer de kans om erboven te eindigen. Het bewijs maakt van de spiegeling
een één-op-één-koppeling tussen paden en staat ingeklapt. Een hoger niveau is
moeilijker te halen en een langere horizon geeft meer tijd, dus de raakkans daalt
met $a$ en stijgt met de horizon. De factor twee blijft, omdat de spiegeling op
elk niveau werkt.

:::{prf:proof}
:class: dropdown

Zij $\kappa = \min\{k : S_k = a\}$ het eerste raaktijdstip. Op $\{\kappa \le n\}$
definiëren we het gespiegelde pad $\tilde S_k = S_k$ voor $k \le \kappa$ en
$\tilde S_k = 2a - S_k$ voor $k > \kappa$. Omdat de stappen na $\kappa$
onafhankelijk en symmetrisch zijn, heeft $\tilde S$ dezelfde kans als $S$. De
afbeelding is een involutie op $\{\kappa \le n\}$ (twee keer spiegelen geeft het
oorspronkelijke pad terug), dus een bijectie.

Ze beeldt $\{\kappa \le n,\ S_n < a\}$ af op $\{\kappa \le n,\ S_n > a\}$ en
omgekeerd. Dus $P(\kappa \le n,\ S_n < a) = P(S_n > a)$, waarbij rechts de
conditie $\kappa \le n$ mag vervallen: een pad dat boven $a$ eindigt, heeft $a$
noodzakelijk geraakt. Splitsen naar de eindwaarde geeft

$$
P(M_n \ge a) = P(\kappa \le n)
 = \underbrace{P(S_n > a)}_{\text{eindigt boven}} + \underbrace{P(S_n = a)}_{\text{eindigt op}}
 + \underbrace{P(\kappa \le n,\ S_n < a)}_{= P(S_n > a)},
$$

en dat is [](#eq-bachelier-reflectie). $\square$
:::

In de Brownse limiet, met $S_T \sim \mathcal{N}(0, \sigma^2 T)$, is de kans om
exact op $a$ te eindigen nul. Er blijft
$P(\max_{t \le T} S_t \ge a) = 2\,P(S_T \ge a)$ over. Een voorbeeld: een
verkooporder 10 euro boven een koers van 100, bij $\sigma = 20$ euro per
$\sqrt{\text{jaar}}$. Na een jaar eindigt de koers in 31% van de gevallen boven
de order, en de order wordt in 62% van de gevallen uitgevoerd.

In het toy-voorbeeld is $n = 4$ en $a = 2$. De stelling geeft
$P(S_4 = 2) + 2P(S_4 > 2) = 4/16 + 2 \cdot 1/16 = 0{,}375$. De code telt dat na
op de zestien paden van het toy-voorbeeld.

```{code-cell} ipython3
touches_two = positions.max(axis=1) >= 2             # raakt het pad ooit +2?
by_counting = touches_two.mean()
by_reflection = (np.sum(final == 2) + 2 * np.sum(final > 2)) / 16

pd.Series(
    {"met de hand": 0.375, "geteld over 16 paden": by_counting,
     "reflectieprincipe": by_reflection},
    name="P(max S_k >= 2)",
).round(4)
```

Tellen en spiegelen geven allebei $0{,}375$. Bachelier gebruikte het principe
voor zijn *options à prime* (premieopties) en voor wat nu *barrièreopties*
heten: opties die vervallen of pas ontstaan als de koers een grens raakt, zoals
een call die waardeloos wordt zodra de koers 20% daalt. Het is ook de kortste
route naar de verdeling van de grootste koersval in een periode, de *maximale
drawdown*.


### Wat het voorspelt: Bacheliers optieprijs

Volgt de koers een aritmetische Brownse beweging, dan is een calloptie haar
verwachte uitbetaling waard. Op het geld is dat ongeveer $0{,}4\,\sigma\sqrt{\tau}$.
Hier is $\sigma$ een bedrag in euro per $\sqrt{\text{jaar}}$.

*Waarom zou dit waar zijn?* Bachelier nam aan dat *l'espérance mathématique du
spéculateur est nulle*: de speculant wint gemiddeld niets. Die aanname is de
random walk uit de Opzet met verwachting nul, nu in prijsniveaus. Wij noemen dat de
*martingaalconditie*: de verwachte koers op de vervaldag is de koers van
vandaag, $\E_t[S_T] = S_t$, zoals in een eerlijk kansspel de verwachte stand na
de volgende ronde de huidige stand is. Een koper die meer
betaalt dan de verwachte uitbetaling, verliest dan gemiddeld, en een verkoper
die minder vraagt ook. De optieprijs is dus de verwachte uitbetaling. Hoe breder
de verdeling van de koers op de vervaldag, hoe meer de optie waard is: ze
verdient aan uitschieters naar boven en verliest niets aan die naar beneden.

De formule rust dus op één aanname, de martingaalconditie. Voor Bachelier was
dat een billijkheidsregel. Black, Scholes en Merton gaven er later een betere
grond voor. Een optie die met aandeel en kas na te maken is, kost evenveel als
die portefeuille. De kosten van die portefeuille hangen niet af van de verwachte
koerswinst. Welke verwachte koerswinst men ook invult, de optieprijs blijft
dezelfde, en dus mag men de eenvoudigste kiezen: nul.

:::{prf:theorem} Bacheliers optieprijs
:label: thm-bachelier-optie

Zij $S_T = S_t + \sigma (W_T - W_t)$ met $W$ een standaard Brownse beweging, dus
$S_T \mid \mathcal{F}_t \sim \mathcal{N}\!\left(S_t, \sigma^2 \tau\right)$ met
$\mathcal{F}_t$ de informatie op $t$ en $\tau = T - t$ de looptijd. Onder de
martingaalconditie is de waarde van een calloptie met uitoefenprijs $K$, bij een
rente van nul,

```{math}
:label: eq-bachelier-call
C_t \;=\; (S_t - K)\,\Phi(d) \;+\; \sigma\sqrt{\tau}\,\varphi(d),
\qquad d \;=\; \frac{S_t - K}{\sigma\sqrt{\tau}},
```

met $\Phi$ en $\varphi$ de verdelings- en dichtheidsfunctie van de
standaardnormale verdeling.
:::

In woorden: de optie is de intrinsieke waarde $S_t - K$ waard, gewogen met een
kans die met $d$ oploopt, plus een term die groeit met de spreiding
$\sigma\sqrt{\tau}$ van de koers op de vervaldag. Ligt de uitoefenprijs ver onder
de koers (diep *in het geld*), dan nadert de waarde $S_t - K$, omdat uitoefenen
vrijwel zeker is. Ligt hij ver erboven (*uit het geld*), dan nadert ze nul. Voor
een aandeel van 100 met 20% volatiliteit per jaar is $\sigma \approx 20$ euro per
$\sqrt{\text{jaar}}$. Het bewijs schrijft de
verwachte uitbetaling als integraal over de normale dichtheid en staat ingeklapt.

:::{prf:proof}
:class: dropdown

Schrijf $s = \sigma\sqrt{\tau}$ en $x = S_t - K$. Onder de martingaalconditie is
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

want $\varphi$ is even. Samen geeft dit [](#eq-bachelier-call). $\square$
:::

Voor een optie op de huidige koers, *op het geld* ($K = S_t$, dus $d = 0$),
blijft alleen de tweede term over:

```{math}
:label: eq-bachelier-atm
C_t \;=\; \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}} \;\approx\; 0{,}3989\,\sigma\sqrt{\tau}.
```

In woorden: de optie is vier tiende van de spreiding van de koers op de
vervaldag waard. Bij $\sigma = 20$ en een looptijd van een jaar is dat 7,98
euro. Aan deze formule is het volgende af te lezen.

- De prijs is lineair in de volatiliteit en evenredig met $\sqrt{\tau}$. Dat is
  Regnaults wet als handelsregel, zoals de intuïtie voorspelde: wie de looptijd
  verviervoudigt, betaalt het dubbele.
- Er staat geen voorkeursparameter in: geen risicoaversie, geen verwacht
  rendement. De hele optietheorie rust op die observatie, en Bachelier had haar
  in 1900.
- Er wordt niet verdisconteerd, omdat Bachelier met termijnkoersen werkte. Een
  termijnkoers is een prijs die nu wordt afgesproken voor betaling later.
  Vandaag gaat er geen geld over tafel, dus er valt niets te verdisconteren.

:::{note} Bacheliers eigen notatie en zijn eigen toets
:class: dropdown

Bachelier schreef [](#eq-bachelier-atm) niet met het getal $0{,}3989$ maar als
$a = k\sqrt{t}$. Zijn $k$ is de *coefficient d'instabilité ou de nervosité*: de
volatiliteit, zestig jaar voordat het woord bestond. Zijn dichtheid is
$p = (1/2\pi a)\,e^{-x^2/(4\pi a^2)}$, waaruit $\sigma\sqrt{t} = a\sqrt{2\pi}$
volgt. Zijn $a = \sigma\sqrt{t}/\sqrt{2\pi}$ is dus onze formule.

Hij toetste zijn model ook. Op de rente 3% over 1894–1898 kalibreerde hij
$k = 5$ centimes per $\sqrt{\text{dag}}$. Daarmee voorspelde hij voor een maand
een *écart probable* (waarschijnlijke afwijking) van $\pm 46$ centimes: een grens
die per constructie in de helft van de maanden niet wordt overschreden, dus een
mediaan en geen gemiddelde. Het getal is na te rekenen. De standaarddeviatie per
dag is $k\sqrt{2\pi} \approx 12{,}5$ centimes, over een maand van dertig dagen
$12{,}5 \cdot \sqrt{30} \approx 69$ centimes. De mediaan van de absolute
afwijking van een normale verdeling is $0{,}6745$ maal de standaarddeviatie:
$0{,}6745 \cdot 69 \approx 46$ centimes. Hij telde na:

> Pendant les 60 derniers mois, 33 fois la variation a été circonscrite entre ces
> limites et 27 fois elle les a dépassées.

Zijn tabellen met *calculée* naast *observée* voor de uitoefenkansen van primes
lopen tot op één honderdste gelijk. Het proefschrift eindigt met een zin die het
tijdvak samenvat: de markt gehoorzaamt, zonder het te weten, aan de wet van de
waarschijnlijkheid.

> le marché, à son insu, obéit à une loi qui le domine : la loi de la probabilité.
:::

Het verschil met Black en Scholes {cite}`BlackScholes1973` zit niet in de
wiskunde maar in het proces. Bachelier laat de *absolute* prijsverandering
normaal verdeeld zijn, Black en Scholes de *relatieve*. Daaruit volgen drie
verschillen.

- De Bachelier-prijs kan negatief worden. Voor een aandeel is dat onzinnig, voor
  een spread (het verschil tussen twee prijzen, zoals de olieprijs voor
  levering in mei en in juni) of een termijncontract op een grondstof juist
  gewenst. Toen de termijnprijs van ruwe olie in april 2020 negatief werd, kwam
  de formule daarom weer in gebruik.
- De Bachelier-volatiliteit $\sigma$ is een bedrag per $\sqrt{\text{tijd}}$, de
  Black-Scholes-volatiliteit is dimensieloos. De vertaling is
  $\sigma_{\text{Bach}} \approx \sigma_{\text{BS}} \cdot S$.
- Bij korte looptijden en rond het geld vallen de formules vrijwel samen.

Het derde verschil volgt uit de Black-Scholes-prijs van een optie op de huidige
koers bij rente nul:

$$
C^{\text{BS}} = S\left[\Phi\!\left(\tfrac{\sigma_{\text{BS}}\sqrt{\tau}}{2}\right)
 - \Phi\!\left(-\tfrac{\sigma_{\text{BS}}\sqrt{\tau}}{2}\right)\right]
\;\approx\; S\,\sigma_{\text{BS}}\sqrt{\tau}\,\varphi(0)
= 0{,}3989\, S\,\sigma_{\text{BS}}\sqrt{\tau}.
$$

Dat is [](#eq-bachelier-atm) met $\sigma_{\text{Bach}} = \sigma_{\text{BS}} S$.
We komen op Black en Scholes terug in [](#02-09-black-scholes). De cel hieronder
rekent beide formules uit voor een aandeel van 100 met een
Black-Scholes-volatiliteit van 20% per jaar, voor drie looptijden en drie
uitoefenprijzen.

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

Bij een looptijd van een maand verschillen de twee prijzen hooguit drie cent.
Bij een jaar en tien procent uit het geld is het verschil 0,34 euro, op een
optie van ongeveer vier euro. Op het geld geeft de tabel bij een jaar 7,98, zoals
[](#eq-bachelier-atm) voorspelde. Wie in 1900 met deze formule had gehandeld, had
voor korte looptijden een model gehad dat nauwelijks van dat van 1973 verschilt.

Toetsen kunnen we de optieformule hier niet: daarvoor zijn historische
optieprijzen nodig, en die zijn niet gratis. Wat we wel kunnen toetsen, is de
aanname eronder, dat koersveranderingen onvoorspelbaar zijn. Daarover gaat de
rest van de lecture.

### Hoe het getoetst wordt: wat "onvoorspelbaar" betekent

Een toets van de random walk kijkt naar koersveranderingen, niet naar het
koersniveau, en de variance ratio is daarbij de hoofdtoets.

Working wees er in 1934 op dat een random walk er bedrieglijk gestructureerd
uitziet {cite}`Working1934`. Hij noemde zo'n reeks een *random-difference
series*: ze vertoont trends en schijnbare cycli. Volgens Working beschrijven die
alleen het verloop over een voorbije periode. Ze zijn geen norm, en geen basis om ook maar
de kortste volgende periode te voorspellen.

Iedereen kan de slotkoers van morgen met een kleine fout voorspellen: het is
ongeveer de koers van vandaag. Bijna niemand gelooft dat hij de
koers*verandering* van morgen kan voorspellen. Wie het niveau toetst, toetst dus
niets. De random walk doet drie toetsbare uitspraken over de log-rendementen, en
elke generatie empirici koos er één.

**Autocorrelatie.** Onder de nulhypothese is $\rho_k = \Corr(r_t, r_{t-k}) = 0$
voor elke $k \ge 1$. De steekproefautocorrelatie heeft dan bij benadering
standaardfout $1/\sqrt{T}$, met $T$ het aantal waarnemingen: $0{,}029$ bij een
eeuw maanddata. Cowles en Jones, en later Kendall, rekenden deze grootheid uit.

**Runs.** Een *run* is een aaneengesloten reeks rendementen met hetzelfde teken.
Met $n_1$ positieve en $n_2$ negatieve waarnemingen en $n = n_1 + n_2$ is het
verwachte aantal runs onder de aanname dat de tekens onafhankelijk zijn (sterker
dan ongecorreleerde rendementen) $\E[R] = 2n_1n_2/n + 1$, met variantie

$$
\Var(R) = \frac{2n_1 n_2 (2n_1n_2 - n)}{n^2 (n-1)} .
$$

Te weinig runs betekent positieve autocorrelatie: opeenvolgende rendementen
hebben vaak hetzelfde teken. Bij de 26 296 dagrendementen uit de replicatie verwacht de
nulhypothese ongeveer 12 900 runs, met een standaardfout van ongeveer 80.
Duizend runs te weinig is dan dertien standaardfouten. De
runs-test neemt niets aan over de verdeling. In 1953, met dikke staarten en
handrekenwerk, woog dat zwaarder dan nu.

**Variance ratio.** De derde toets is de $\sqrt{t}$-wet in één getal.

```{math}
:label: eq-bachelier-vr
VR(q) \;=\; \frac{\Var\!\left(r_t + r_{t-1} + \dots + r_{t-q+1}\right)}
                  {q\,\Var(r_t)} .
```

In woorden: de variantie van een rendement over $q$ perioden, gedeeld door $q$
keer de variantie over één periode. Onder de random walk is $VR(q) = 1$ voor
elke $q$, want de variantie groeit lineair in de tijd. Boven één is er
positieve autocorrelatie, onder één negatieve: opeenvolgende rendementen hebben
vaak een tegengesteld teken.

:::{prf:theorem} Variance ratio als gewogen som van autocorrelaties
:label: thm-bachelier-vr

Voor een covariantie-stationaire reeks (gemiddelde, variantie en
autocovarianties veranderen niet in de tijd, zoals bij het proces
$r_t = \rho\, r_{t-1} + e_t$ met $|\rho| < 1$) geldt

```{math}
:label: eq-bachelier-vr-rho
VR(q) \;=\; 1 + 2\sum_{j=1}^{q-1}\left(1 - \frac{j}{q}\right)\rho_j .
```
:::

In woorden: $VR(q)$ is één plus een gewogen som van de eerste $q - 1$
autocorrelaties, met gewichten die lineair aflopen. Een voorbeeld: is alleen
$\rho_1 = 0{,}1$ en zijn de andere nul, dan is
$VR(4) = 1 + 2 \cdot \tfrac34 \cdot 0{,}1 = 1{,}15$. Het bewijs telt de
covarianties in de variantie van een som en staat ingeklapt.

:::{prf:proof}
:class: dropdown

Schrijf $\gamma_j = \Cov(r_t, r_{t-j})$, dus $\rho_j = \gamma_j/\gamma_0$. De
variantie van de som van $q$ opeenvolgende termen telt $q$ keer $\gamma_0$, en
voor elke $j \ge 1$ telt ze $2(q-j)$ keer $\gamma_j$: er zijn $q - j$ paren op
afstand $j$ en elk paar telt twee keer mee.

$$
\Var\Bigl(\sum_{i=0}^{q-1} r_{t-i}\Bigr)
 = q\gamma_0 + 2\sum_{j=1}^{q-1}(q-j)\gamma_j .
$$

Delen door $q\gamma_0$ geeft [](#eq-bachelier-vr-rho). $\square$
:::

Uit de stelling volgt dat $VR(2) - 1 = \rho_1$, exact: de eenvoudigste variance
ratio is de eerste autocorrelatie. De variance ratio is om twee redenen de
hoofdtoets van deze lecture.

- Ze bundelt. Voor grotere $q$ telt $VR(q)$ veel kleine autocorrelaties op. Is de
  afhankelijkheid over veel vertragingen uitgesmeerd, dan verdwijnt elke $\rho_j$ apart
  in de ruis, maar hun gewogen som niet. Daarom kozen Lo en MacKinlay deze toets.

- Ze gebruikt alleen varianties, en die zijn goed te meten. Dat is de
  standaardfout van 2% uit [](#00-01-rendementen), van de andere kant bekeken: bij een
  jaarvolatiliteit van 20% heeft een gemiddeld rendement over een eeuw een
  standaardfout van $20\%/\sqrt{100} = 2$ procentpunt, maar een variantie is
  over dezelfde eeuw veel nauwkeuriger bekend. Een toets die op een verhouding
  van varianties steunt, kan met de beschikbare data dus wel iets zeggen.

Onder de nulhypothese en bij constante variantie is de standaardfout van
$VR(q)$ gelijk aan $\sqrt{2(2q-1)(q-1)/(3qT)}$ {cite}`LoMacKinlay1988`. Voor
$q = 2$ is dat $1/\sqrt{T}$. Bij de 1216 weken van Lo en MacKinlay is ze
$0{,}029$, $0{,}054$, $0{,}085$ en $0{,}126$ voor $q = 2, 4, 8, 16$: bij lange
horizonnen is de toets veel minder scherp.

De functie `hap.variance_ratio` geeft naast $VR(q)$ de toetsgrootheid
$z_1$, die constante variantie aanneemt, en de robuuste $z_2$; Lo en MacKinlay noemen die laatste
$z^{*}$. Wij gebruiken $z_2$: volatiliteit clustert, en dat alleen al zou $z_1$
te groot maken.

De derde voorspelling uit de intuïtie, dat elke autocorrelatie nul is, is dus
de nulhypothese van alle drie de toetsen.

```{admonition} Samengevat
:class: tip

- Een random walk wordt in de limiet een Brownse beweging, met
  $\E|W_{t+h} - W_t| = \sqrt{2h/\pi}$: Regnaults wet als stelling,
  [](#thm-bachelier-donsker).

- De kans om een niveau te raken is twee keer de kans om erboven te eindigen,
  [](#eq-bachelier-reflectie). Een hoger niveau is moeilijker te halen en maakt
  beide kansen kleiner, een langere horizon geeft meer tijd en maakt ze groter.

- Een optie op het geld is $0{,}4\,\sigma\sqrt{\tau}$ waard: hoger bij meer
  volatiliteit of een langere looptijd, omdat de uitschieters naar boven groter
  worden, en zonder verwacht rendement of risicoaversie, [](#eq-bachelier-atm).
  Een lagere uitoefenprijs maakt de optie meer waard, een hogere minder.

- $VR(q) - 1$ is een gewogen som van autocorrelaties: positief bij positieve
  autocorrelatie, negatief bij negatieve, [](#eq-bachelier-vr-rho).
  Bij grotere $q$ tellen meer vertragingen mee: aanhoudende positieve autocorrelatie
  laat $VR(q)$ met $q$ stijgen.

- De simulatie hierna vraagt: hoeveel jaren weekdata zijn nodig om een kleine
  autocorrelatie met $VR(2)$ te zien?
```

## Simulatie: hoeveel data om een afwijking te zien?

We bouwen een wereld van weekrendementen met 2% volatiliteit per week, eerst
zonder enige afhankelijkheid en daarna met een kleine eerste autocorrelatie
$\rho_1 = \rho$. In die wereld is $VR(2)$ per constructie één, of $1 + \rho$. De vraag over
steekproeven: hoeveel jaren data heeft een onderzoeker nodig om die afwijking
met een toets te zien?

Onder de nulhypothese geldt wat het toy-voorbeeld liet zien: de variantie groeit
lineair, dus $VR(2) = 1$. Als maat nemen we de steekproef van Lo en MacKinlay: $T = 1216$ weekrendementen,
ruim drieëntwintig jaar. De eerste cel trekt 2000 paden zonder afhankelijkheid
en vergelijkt de spreiding van $\widehat{VR}(2)$ met de asymptotische
standaardfout $1/\sqrt{T}$.

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

Onder de nulhypothese werkt de toets zoals bedoeld. Het gemiddelde is vrijwel
één, en de spreiding van $0{,}0281$ ligt dicht bij $1/\sqrt{T} = 0{,}0287$. De
toets verwerpt de ware nulhypothese in 4,3% van de steekproeven, iets onder de
nominale 5%. Dat past bij een schatter die in eindige steekproeven een fractie
te weinig spreiding heeft.

Daarna komt het alternatief. Het eenvoudigste model met afhankelijkheid is een
AR(1) in log-rendementen, $r_t = \rho\, r_{t-1} + e_t$. Daarvoor is
$\rho_1 = \rho$ en dus $VR(2) = 1 + \rho$ volgens [](#eq-bachelier-vr-rho). Een
positieve $\rho$ is positieve autocorrelatie; zo lazen Lo en MacKinlay hun
weekdata. De cel simuleert voor drie waarden van $\rho$ en drie
steekproeflengtes elk 1000 paden en telt hoe vaak de toets verwerpt.

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
        results = [hap.variance_ratio(pd.Series(p), 2) for p in ar1_paths(rho, 1000, T)]
        vr_estimates = np.array([r["vr"] for r in results])
        rejected = np.array([abs(r["z2"]) > 1.96 for r in results])
        expected_z = rho * np.sqrt(T)            # (VR(2) - 1) / SE = rho * sqrt(T)
        analytic_power = stats.norm.sf(1.96 - expected_z) + stats.norm.cdf(-1.96 - expected_z)
        rows.append({"rho": rho, "jaren weekdata": T // 52,
                     "gemiddelde VR(2)": vr_estimates.mean(),
                     "onderscheidend vermogen": rejected.mean(),
                     "analytisch": analytic_power})
power = pd.DataFrame(rows)
power.round(3)
```

De geschatte $VR(2)$ is in alle negen gevallen vrijwel $1 + \rho$, ook bij vijf
jaar data: de schatter is nagenoeg zuiver. Het *onderscheidend vermogen*, de
kans dat de toets de foute nulhypothese verwerpt, hangt
daarentegen sterk af van de lengte van de steekproef. Omdat $VR(2) - 1 = \rho$
en de standaardfout bij kleine $\rho$ ook onder het alternatief ongeveer
$1/\sqrt{T}$ is, is de verwachte $z$-waarde $\rho\sqrt{T}$.
Een verwachte $z$ van 1,96 vraagt dan

```{math}
:label: eq-bachelier-power
T^{*} \;=\; \left(\frac{1{,}96}{\rho}\right)^{2}
```

waarnemingen. In woorden: halveer de autocorrelatie en de benodigde steekproef
wordt vier keer zo lang. Ook bij $T^{*}$ is de kans om te verwerpen nog maar
vijftig procent.

| $\rho$ | $T^{*}$ (weken) | jaren |
|---|---|---|
| 0,20 | 96 | 1,8 |
| 0,05 | 1537 | 30 |
| 0,02 | 9604 | 185 |

Een autocorrelatie van 0,02 vraagt meer jaren weekdata dan er een beurs bestaat
om op te meten. Simulatie en formule komen tot op steekproefruis overeen, dus de
vuistregel is bruikbaar. De figuur zet het onderscheidend vermogen uit tegen de
lengte van de steekproef. Let op waar de lijnen de verticale lijn van Lo en
MacKinlay kruisen.

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
ax.axvline(round(T_lm / 52, 1), color=hap.plotting.COLORS[7], lw=1.2)   # 1216 weken = 23,4 jaar
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
MacKinlay is een autocorrelatie van 0,20 zo goed als zeker zichtbaar, en een van
0,02 zo goed als onzichtbaar. Wie beweert dat een markt efficiënt is, zegt dus
altijd: met de data die ik heb.
:::

```{warning}
Deze rekensom heeft een onaangename keerzijde. Dezelfde $T$ die te klein is om
een echte $\rho$ van 0,02 te vinden, laat ruis tot 0,06 toe: twee
standaardfouten van $1/\sqrt{1216} \approx 0{,}029$. Wie vijftig markten, tien
horizonnen en drie frequenties nakijkt,
vindt met zekerheid ergens een $z$-waarde boven twee, zonder dat er iets te
vinden is. Hetzelfde selectieprobleem verklaart de *factor zoo*, de honderden
"gevonden" rendementsfactoren in de literatuur, in [](#06-34-factor-zoo).
 Daarom leggen onderzoeken van na 1990 hun steekproef
vooraf vast.
```

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Jules Regnault, *Calcul des chances et philosophie de la bourse*,
Parijs 1863 {cite}`Regnault1863`.

**Wat.** Zijn wet *l'écart des cours est en raison directe de la racine carrée
des temps*, en zijn eigen toets ervan (§83–84). Een gemiddelde absolute afwijking
van 2,73 frank per maand, maal $\sqrt{3}$ en $\sqrt{12}$, gaf 4,73 en 9,45 tegen
waargenomen 4,74 en 9,50.

Wij herhalen die vergelijking en schatten de helling $b$ in
$\log \E|p_{t+h} - p_t| = a + b \log h$ over $h = 1, 3, 12, 60$ maanden.

**Data hier.** Shillers maandreeks van de reële S&P-prijs vanaf 1871 via
`hap.data.shiller()`, en ter controle de maandelijkse marktfactor van French
vanaf 1926 via `hap.data.market_monthly()`.

**Verschil met het origineel.** Regnault gebruikte de maandelijkse hoogste en
laagste koers van de Franse 3%-rente, wij een Amerikaanse aandelenindex in
log-prijzen, met de gemiddelde absolute verandering als maat. Shillers
maandprijs is een gemiddelde van dagkoersen, en die middeling drukt de variantie
op de kortste horizon.

**Verwachte afwijking.** De helling ligt dicht bij 0,5: voor French binnen 0,05,
voor Shiller hoger door de maandmiddeling. De falsifieerbare eis is dat
$\E|p_{t+h} - p_t|/\sqrt{h}$ over de vier horizonnen binnen een factor twee
blijft, waar een lineaire wet een factor acht zou geven.
```

De functie hieronder berekent per horizon de gemiddelde absolute afwijking en de
standaarddeviatie van de verandering in de log-prijs, na aftrek van het
gemiddelde. In de tabel is `E|dev|` de gemiddelde absolute afwijking, `SD(dev)`
de standaarddeviatie en `nobs` het aantal waarnemingen. De kolom `Regnault` doet
wat hij deed: de gemiddelde absolute afwijking over één maand maal $\sqrt{h}$.

```{code-cell} ipython3
# Regnault (1863, §83-84): Franse 3%-rente à comptant, maandelijkse hoogste en laagste
# koers van de uitgifte in mei 1825 tot eind 1862, in frank; écart 2,73 frank per maand na
# correctie voor coupon en report. Shiller loopt hier van 1871-01 t/m 2026-09, French
# vanaf 1926-07.
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

Beide reeksen groeien veel trager dan lineair. De laatste kolom,
$\E|\cdot|/\sqrt{h}$, blijft voor French tussen 0,037 en 0,042 over een factor
zestig in horizon. De volgende cel schat de helling en zet de uitkomst naast
Regnaults eigen toets.

```{code-cell} ipython3
slopes = {}
for name, block in regnault.groupby(level="reeks"):
    log_h = np.log(block.index.get_level_values("h"))
    slopes[name] = np.polyfit(log_h, np.log(block["E|dev|"]), 1)[0]


def predicted_over_observed(block, h):
    """One-month deviation times sqrt(h) (Regnault), divided by the observed one."""
    return block.loc[h, "Regnault: E|dev|(1)*sqrt(h)"] / block.loc[h, "E|dev|"]


french_block = regnault.loc["French 1926-2026"]
shiller_block = regnault.loc["Shiller 1871-2026"]
pd.DataFrame(
    {
        "origineel (Regnault)": [0.5, 4.73 / 4.74, 9.45 / 9.50],
        "hier: French": [slopes["French 1926-2026"],
                         predicted_over_observed(french_block, 3),
                         predicted_over_observed(french_block, 12)],
        "hier: Shiller": [slopes["Shiller 1871-2026"],
                          predicted_over_observed(shiller_block, 3),
                          predicted_over_observed(shiller_block, 12)],
    },
    index=["helling b", "kwartaal: voorspeld / waargenomen",
           "jaar: voorspeld / waargenomen"],
).round(3)
```

**Geslaagd op de helling, gedeeltelijk geslaagd op Regnaults eigen toets.** De
helling voor French is 0,511, binnen 0,05 van Regnaults 0,5, en de
falsifieerbare eis is ruim gehaald. De Shiller-helling van 0,577 ligt hoger,
zoals het replicatieblok voorspelde: middelen drukt de variantie op de kortste
horizon meer dan op de langste. Laat men de kortste horizon weg, dan zakt ze:

| horizonnen (maanden) | helling Shiller |
|---|---|
| 1, 3, 12, 60 | 0,577 |
| 3, 12, 60 | 0,54 |
| 12, 60 | 0,475 |

Tussen twaalf en zestig maanden ligt de helling iets onder een half. Dat wijst
op milde negatieve autocorrelatie op lange horizonnen.

Regnaults eigen toets is strenger dan de helling, en zijn overeenstemming van
een half procent halen we niet. Voor French voorspelt de maandwaarde maal
$\sqrt{12}$ een jaarwaarde die ruim tien procent te laag is (verhouding 0,885 in
de tabel). Extrapoleren van één naar twaalf maanden is gevoelig voor de
meetconventie. En zijn rente was een staatsobligatie, met een stabielere
volatiliteit dan een aandelenindex waarin de jaren dertig en 2008 zitten.

De figuur zet beide reeksen op dubbellogaritmische schaal, naast een
referentielijn met helling een half. Let erop dat beide reeksen evenwijdig aan
die lijn lopen, en dat alleen Shiller bij de kortste horizon afbuigt.

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
$\tfrac12$. Beide reeksen volgen die lijn van één maand tot vijf jaar. De lichte
knik bij de kortste horizon in de Shiller-reeks komt van de maandmiddeling in
zijn prijsreeks, niet van de markt.
:::

```{admonition} Replicatie
:class: seealso

**Bron.** Maurice Kendall, *The Analysis of Economic Time-Series, Part I:
Prices*, JRSS-A 1953 {cite}`Kendall1953`. Andrew Lo en Craig MacKinlay, *Stock
Market Prices Do Not Follow Random Walks*, Review of Financial Studies 1988
{cite}`LoMacKinlay1988`.

**Wat.** Kendalls tabel 3: de eerste autocorrelaties van negentien wekelijkse
Britse industrie-indices over 1928–1938. Van Lo en MacKinlay tabel 1a (variance
ratios van de marktindex over 1216 weken) en tabel 2 (per grootte-kwintiel).

**Data hier.** De dagelijkse marktfactor van French, opgeteld tot
weekrendementen, en de maandelijkse kwintielportefeuilles op marktwaarde. De
reeksen en steekproefgrenzen staan in de codecellen.

**Verschil met het origineel.** Kendall had Britse sectorindices uit het
interbellum, wij de Amerikaanse markt. Lo en MacKinlay hadden ook een
gelijkgewogen index en wekelijkse, gelijkgewogen kwintielen, wij alleen
maandelijkse, waardegewogen reeksen, wat de afwijkingen kleiner maakt.

**Verwachte afwijking.** Voor de marktindex $VR(q)$ binnen 0,05 van de
gepubliceerde waarden, met $z$-waarden rond de twee. Voor Kendall een lagere
eerste autocorrelatie, omdat de hele markt minder dun verhandeld is dan zijn
sectorindices. De falsifieerbare eis is de
rangorde: $VR(2)$ daalt van het kleinste naar het grootste kwintiel, en wijkt
dat af, dan zit de fout in de code.
```

De eerste cel berekent, zoals Kendall, de eerste vijf autocorrelaties, nu voor
dag-, week- en maandrendementen van de Amerikaanse markt.

```{code-cell} ipython3
# Kendall (1953) had 22 reeksen: 19 Britse industrie-indices (wekelijks, 486
# waarnemingen elk), tarwe in Chicago en katoen in New York.
daily = np.log1p(hap_data.market_daily()["Mkt"])
weekly = daily.resample("W-FRI").sum()               # vrijdag op vrijdag
monthly = np.log1p(hap_data.market_monthly()["Mkt"])
frequencies = {"dagelijks": daily, "wekelijks": weekly, "maandelijks": monthly}

kendall_rows = {}
for name, s in frequencies.items():
    row = {"nobs": len(s), "SE onder H0": 1 / np.sqrt(len(s))}
    for k in range(1, 6):
        row[f"rho_{k}"] = s.autocorr(k)
    kendall_rows[name] = row
kendall = pd.DataFrame(kendall_rows).T
kendall.round(4)
```

Kendalls resultaat houdt in orde van grootte stand. De grootste autocorrelatie
is die van maandrendementen op lag één: $0{,}085$, tegen een standaardfout van
$0{,}029$. Die is significant, en verklaart toch maar 0,7% van de variantie van
het volgende maandrendement. De voorspelling uit de intuïtie, autocorrelaties
van nul, houdt dus bijna stand: niet exact nul, maar te klein om mee te
voorspellen.

Onze weekwaarde van $0{,}030$ ligt onder Kendalls gemiddelde van ongeveer
$0{,}13$ over zijn negentien industrie-indices. Zijn reeksen waren
sectorindices van dun verhandelde Britse aandelen, en die zijn sterker positief
gecorreleerd dan de hele Amerikaanse markt. Dat Kendall nulcorrelaties vond, is
een hardnekkig misverstand: zijn waarden liepen van $-0{,}013$ (olie) tot $0{,}301$
(beleggingsfondsen). Hij schreef alleen dat ze te zwak waren om er iets mee te
voorspellen.

De runs-test kijkt alleen naar de tekens. Een correlatiecoëfficiënt rekent met
kwadraten, zodat een paar extreme dagen hem domineren. In de runs-test weegt zo'n
dag even zwaar als elke andere. De functie telt de runs en vergelijkt ze met de
verwachting onder de nulhypothese.

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


pd.DataFrame({name: runs_test(s) for name, s in frequencies.items()}).T.round(3)
```

Op dagbasis zijn er ruim duizend runs minder dan de random walk voorspelt, met
$z = -13{,}1$: positieve autocorrelatie in de tekens. Op dagdata oordeelt de
runs-test veel scherper dan de eerste autocorrelatie. Hij gebruikt 26 296
waarnemingen en laat extreme dagen niet zwaarder wegen dan gewone. Voor afhankelijkheid over meerdere perioden
blijft de variance ratio de hoofdtoets; die passen we hieronder toe op
weekdata.

De variance ratios berekenen we op drie steekproeven: die van Lo en MacKinlay,
de periode na hun publicatie, en Kendalls tijdvak.

```{code-cell} ipython3
def vr_table(series, horizons=(2, 4, 8, 16)):
    """Variance ratios with heteroskedasticity-robust z-statistics."""
    out = {"nobs": len(series)}
    for q in horizons:
        result = hap.variance_ratio(series, q)
        out[f"VR({q})"] = result["vr"]
        out[f"z({q})"] = result["z2"]
    return out


# Lo en MacKinlay: 6 september 1962 t/m 26 december 1985, CRSP, woensdag op woensdag.
# French publiceert geen gelijkgewogen dagreeks; wij hebben alleen de waardegewogen markt.
samples = {
    "1962-09 t/m 1985-12": weekly.loc["1962-09-06":"1985-12-26"],
    "1986-01 t/m heden": weekly.loc["1986-01-01":],
    "Kendall-periode 1928-1938": weekly.loc["1928":"1938"],
}
vr_samples = pd.DataFrame({k: vr_table(v) for k, v in samples.items()}).T
vr_samples.round(3)
```

Op de steekproef van Lo en MacKinlay, 1216 weken zoals bij hen, liggen alle
vier de ratio's boven één. Ze lopen op tot $q = 8$ en blijven daarna vlak. Het
interessantste getal van deze lecture staat in de tweede rij. Op de veertig jaar
ná hun publicatie is $VR(2) = 0{,}950$: de afhankelijkheid is niet alleen
verdwenen, ze is van teken gewisseld. In Kendalls eigen tijdvak is de afwijking
het grootst, met $VR(16) = 1{,}507$ op nog geen elf jaar data.

Dezelfde berekening per kwintiel op marktwaarde, over 1962–1985, toetst de
rangorde.

```{code-cell} ipython3
size = hap_data.french("Portfolios_Formed_on_ME", "monthly").loc["1962-09":"1985-12"]
quintiles = ["Lo 20", "Qnt 2", "Qnt 3", "Qnt 4", "Hi 20"]

size_table = pd.DataFrame(
    {q: vr_table(np.log1p(size[q].dropna()), horizons=(2, 4, 8)) for q in quintiles}
).T
size_table.index = ["1 (kleinst)", "2", "3", "4", "5 (grootst)"]
size_table.round(3)
```

$VR(2)$ daalt monotoon van 1,205 bij het kleinste kwintiel naar 1,016 bij het
grootste. Hetzelfde patroon staat in de kolommen voor $q = 4$ en $q = 8$. De
tabel hieronder zet onze waarden naast die van Kendall en van Lo en MacKinlay.

```{code-cell} ipython3
lm_sample = vr_samples.loc["1962-09 t/m 1985-12"]
market_rows = ["VR(2)", "VR(4)", "VR(8)", "VR(16)"]
quintile_rows = ["1 (kleinst)", "3", "5 (grootst)"]

# Per rij: (origineel, hier, z origineel, z hier). Originelen uit Kendall tabel 3 en
# Lo en MacKinlay tabel 1a en 2.
comparison_rows = {
    "Kendall: rho_1 week (gemiddelde)":
        (0.13, kendall.loc["wekelijks", "rho_1"], np.nan, np.nan),
    "markt: VR(2)": (1.08, lm_sample["VR(2)"], 2.33, lm_sample["z(2)"]),
    "markt: VR(4)": (1.16, lm_sample["VR(4)"], 2.31, lm_sample["z(4)"]),
    "markt: VR(8)": (1.22, lm_sample["VR(8)"], 2.07, lm_sample["z(8)"]),
    "markt: VR(16)": (1.22, lm_sample["VR(16)"], 1.38, lm_sample["z(16)"]),
    "kwintiel 1 (kleinst): VR(2)":
        (1.42, size_table.loc["1 (kleinst)", "VR(2)"], 8.81, size_table.loc["1 (kleinst)", "z(2)"]),
    "kwintiel 3: VR(2)": (1.28, size_table.loc["3", "VR(2)"], 7.38, size_table.loc["3", "z(2)"]),
    "kwintiel 5 (grootst): VR(2)":
        (1.14, size_table.loc["5 (grootst)", "VR(2)"], 3.82, size_table.loc["5 (grootst)", "z(2)"]),
}
comparison_lm = pd.DataFrame.from_dict(
    comparison_rows, orient="index", columns=["origineel", "hier", "z origineel", "z hier"]
)
comparison_lm.round(3)
```

**Geslaagd op de puntschattingen en de rangorde, gedeeltelijk op de
$z$-waarden.** Voor de marktindex liggen alle vier de schattingen binnen 0,02
van de gepubliceerde waarden, met hetzelfde patroon over $q$. De verwachting was
$z$-waarden rond de twee. Bij $q = 4$ en $q = 8$ klopt dat (2,0 en 1,8), bij
$q = 2$ en $q = 16$ liggen ze lager (1,6 en 1,2). De rangorde over de kwintielen,
de falsifieerbare eis, is die van Lo en MacKinlay. Onze niveaus liggen lager,
omdat maandrendementen de weekafhankelijkheid wegmiddelen en onze kwintielen
waardegewogen zijn. Kendalls eerste autocorrelatie komt, zoals verwacht, lager
uit dan bij hem (0,030 tegen 0,13). Beide zijn klein: zelfs 0,13 verklaart nog
geen 2% van de variantie van het volgende weekrendement.

Het scherpste resultaat van Lo en MacKinlay kwam van hun gelijkgewogen index,
die kleine ondernemingen zwaarder weegt: $VR(2) = 1{,}30$ met $z^{*} = 7{,}51$.
Dat komt volgens hen neer op een eerste autocorrelatie van weekrendementen van
ongeveer 30%. Die reeks hebben wij op weekbasis niet. De figuur vat beide
tabellen samen. Let links op het teken van de afwijking vóór en na 1985, en
rechts op de daling van klein naar groot.

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

Links: de variance ratios die Lo en MacKinlay vonden, liggen boven één en lopen
op met de horizon. Op de veertig jaar ná hun publicatie liggen ze eronder.
Rechts: hoe kleiner de onderneming, hoe groter de afwijking van de random walk.
Die systematiek gaf hun artikel zijn kracht. Beide panelen laten open of het om
een prijsfout ging of om een eigenschap van de handel in kleine aandelen.
:::

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Veel, met weinig aannames. Alles volgt uit één
zin: opeenvolgende koersveranderingen zijn ongecorreleerd. Daaruit komen de
$\sqrt{t}$-wet, die wij met een helling van 0,51 terugvonden, de normale
limietverdeling, de diffusievergelijking, de kans om een niveau te raken, en een
optieformule die voor korte looptijden nauwelijks van Black-Scholes verschilt.
Het model verklaart ook waarom beroepsvoorspellers collectief falen: valt er
niets te voorspellen, dan is het gemiddelde advies waardeloos. Cowles stelde dat
in 1933 vast {cite}`Cowles1933`.

:::{note} Cowles' telling van de voorspellers
:class: dropdown

Cowles verzamelde ongeveer 7500 aanbevelingen van zestien
beleggingsadviesdiensten, over de vierenhalf jaar tot juli 1932. Gemiddeld deden
ze het 1,43 procent per jaar slechter dan het gemiddelde aandeel. Twintig
brandverzekeraars bleven over 1928–1931 gemiddeld 1,20 procent per jaar bij de
markt achter.

Vierentwintig financiële publicaties bleven 4 procent per jaar achter bij het
gemiddelde van wat met louter toeval te bereiken was. Die toevalsportefeuilles,
ook vierentwintig, stelde Cowles samen met een kaartspel.
:::

**Waar het breekt.** Op twee plaatsen; de eerste weegt het zwaarst. De random
walk zegt iets over *veranderingen*, niets over het *niveau*. Of de markt op
twintig of op veertig keer de winst staat, de verandering van morgen blijft
onvoorspelbaar. Er is dus een theorie van de ruis en geen theorie van de waarde.
De tweede breuk is kleiner en empirisch, en in deze lecture gemeten: runs op
dagdata met $z = -13{,}1$, een maandautocorrelatie van 0,085, en variance ratios
die dalen met de grootte van de onderneming. Volgens de simulatie worden zulke
afwijkingen pas na dertig jaar weekdata zichtbaar, en dan zijn ze te klein om
binnen een beleggersleven aan te verdienen. Dat ze statistisch bestaan, zegt
weinig over hun economisch belang.

:::{note} Osborne: de Brownse beweging in logs
:class: dropdown

Bachelier breekt ook op een technisch punt. Arithmetische Brownse beweging laat
negatieve prijzen toe. Ze geeft een aandeel van honderd euro bovendien dezelfde
volatiliteit in euro's als een aandeel van één euro. Osborne herstelde dat in
1959 door de Brownse beweging naar de logaritme van de prijs te verplaatsen
{cite}`Osborne1959`. In die vorm gebruikten Black en Scholes het model.

Osborne deed ook Regnaults meting over, op de Cowles-index van 1831 tot 1936, over
intervallen van twintig minuten tot twaalf jaar. Zijn conclusie: de data volgen
heel goed een helling van een half, de diffusiewet met de wortel van de tijd.
:::

**Risico of vergissing?** De variance ratios boven één, hoger bij kleinere
ondernemingen, laten beide lezingen toe. De Chicago-lezing (Fama: prijzen
kloppen): een meetartefact plus een risicopremie. Kleine aandelen worden niet
elke dag verhandeld, hun laatste koers loopt achter, en dat maakt
indexrendementen vanzelf positief gecorreleerd. De Yale-lezing (Shiller: prijzen
kunnen ernaast zitten): in weinig gevolgde aandelen past de prijs zich te traag
aan, een vergissing die arbitrage zou moeten wegnemen. De daling van $VR(2)$ na
1985 past bij beide. Scheiden vraagt handelsdata van vóór 1985, en die zijn er
niet. Later heet dit het probleem van de gezamenlijke hypothese (*joint
hypothesis*): elke toets van efficiëntie toetst ook een model voor het verwachte
rendement.

**Wat er daarna kwam.** Geen betere toets, maar het ontbrekende stuk. Voordat
iemand kon zeggen
of een prijs *fout* was, moest er een theorie zijn van wat een prijs *hoort* te
zijn. John Burr Williams schreef die in 1938 op: zie [](#01-03-williams-ddm).

## Oefeningen

:::{exercise}
:label: ex-bachelier-instap

**Instap: een scheve munt.** Neem het toy-voorbeeld, maar laat elke stap met
kans 0,6 omhoog gaan en met kans 0,4 omlaag.

1. Bereken $\E[S_4]$ en $\Var(S_4)$ met de hand.
2. Groeit de afwijking van de wandeling nog met de wortel van het aantal stappen?
   Wat betekent dat voor de keuze in de replicatie om veranderingen eerst van hun
   gemiddelde te ontdoen?
:::

:::{solution} ex-bachelier-instap
:class: dropdown

**(1)** Eén stap heeft verwachting $0{,}6 - 0{,}4 = 0{,}2$ en variantie
$1 - 0{,}2^2 = 0{,}96$. Bij onafhankelijke stappen tellen beide op:
$\E[S_4] = 0{,}8$ en $\Var(S_4) = 3{,}84$. De code weegt de zestien paden van
het toy-voorbeeld met hun nieuwe kansen.

```{code-cell} ipython3
prob_up = 0.6
path_prob = np.prod(np.where(paths == 1, prob_up, 1 - prob_up), axis=1)   # kans per pad
mean_skewed = path_prob @ final
var_skewed = path_prob @ (final - mean_skewed) ** 2

pd.DataFrame(
    {"met de hand": [0.8, 3.84], "code": [mean_skewed, var_skewed]},
    index=["E[S_4]", "Var(S_4)"],
).round(4)
```

**(2)** De variantie groeit nog steeds lineair, als $0{,}96\,n$. De spreiding
rond het verwachte pad groeit dus met $\sqrt{n}$. Maar het verwachte pad zelf
loopt lineair weg, als $0{,}2\,n$. Vanaf ongeveer 24 stappen is de drift groter
dan de spreiding. Zonder aftrek van het gemiddelde groeit $\E|S_n|$ op lange
horizonnen dus lineair, en trekt de drift de geschatte helling naar één.

Wat dit leert: de $\sqrt{t}$-wet gaat over de afwijking rond de drift, en wie
haar toetst, moet de drift eerst verwijderen.
:::

:::{exercise}
:label: ex-bachelier-1

**De variance ratio van een AR(1).** Laat $r_t = \rho\,r_{t-1} + e_t$ met
$|\rho| < 1$ en $e_t$ witte ruis.

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
$\rho_j = \rho^{\,j}$. Invullen in [](#eq-bachelier-vr-rho) geeft, na sommatie
van de meetkundige reeks en van $\sum j\rho^j$,

$$
VR(q) = 1 + 2\sum_{j=1}^{q-1}\Bigl(1-\frac{j}{q}\Bigr)\rho^{\,j}
      = 1 + \frac{2\rho}{1-\rho}
        \left[1 - \frac{1-\rho^{\,q}}{q\,(1-\rho)}\right].
$$

Voor $q \to \infty$ verdwijnt de tweede term en blijft
$VR(\infty) = (1+\rho)/(1-\rho)$ over.

**(2) en (3)** De cel rekent de theoretische waarden uit en schat ze op één
gesimuleerd pad van 1216 weken.

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

De tabel toont één gesimuleerd pad; een ander zaad geeft andere getallen. In dit
pad liggen de geschatte waarden boven de theoretische, en daalt de $z$-waarde met
$q$. De limiet voor $q \to \infty$ volgt uit de formule onder (1).

```{code-cell} ipython3
print(f"limiet (1+rho)/(1-rho) = {(1 + rho_ex) / (1 - rho_ex):.4f}")
```

De theoretische waarden stijgen monotoon, met sterk afnemende opbrengst, naar een
limiet van 1,222. De geschatte waarden liggen in dit ene pad erboven, tot 1,42
bij $q = 16$: bij grote $q$ is de steekproefruis groot. De grootste $z$-waarde
valt bij de *kleinste* horizon: 4,51 bij $q = 2$ tegen 3,29 bij $q = 16$. De
standaardfout van $VR(q)$ groeit ongeveer met $\sqrt{q}$, terwijl $VR(q) - 1$ na
$q = 4$ nauwelijks nog toeneemt.

Wat dit leert: wie afhankelijkheid zoekt, kiest de horizon waarop het signaal
groeit, niet die waarop de statistiek het grootst oogt.
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
   ongeveer hetzelfde zeggen?
:::

:::{solution} ex-bachelier-2
:class: dropdown

**(1)** Uit de pariteit volgt
$P_t = C_t - (S_t - K) = (S_t-K)\left[\Phi(d) - 1\right] + \sigma\sqrt{\tau}\varphi(d)
= (K - S_t)\Phi(-d) + \sigma\sqrt{\tau}\varphi(d)$, met $d = (S_t-K)/(\sigma\sqrt{\tau})$.
Beide termen zijn niet-negatief als $K \ge S_t$. Voor $K < S_t$ is $-d < 0$ en
domineert de tweede term, zodat $P_t > 0$ blijft.

**(2) en (3)** De cel zoekt per uitoefenprijs de $\sigma_{\text{Bach}}$ die de
Black-Scholes-prijs reproduceert.

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

De impliciete volatiliteit stijgt monotoon met de uitoefenprijs. De figuur zet
haar uit naast de vuistregel $\sigma_{\text{BS}} \cdot S = 20$; let op waar de
kromme die lijn kruist.

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

De kromme is niet vlak. Op het geld ligt de impliciete Bachelier-volatiliteit op
19,97, vrijwel gelijk aan $\sigma_{\text{BS}} \cdot S = 20$. Maar ze loopt
monotoon op, van 16,79 bij $K = 70$ tot 22,83 bij $K = 130$. Die scheefheid komt
doordat de log-normale verdeling naar rechts uitloopt en de normale symmetrisch
is. Het is een *volatility smile* (een impliciete volatiliteit die per
uitoefenprijs verschilt, terwijl het model er één aanneemt) met de rollen
omgedraaid: hier is Black-Scholes de markt en Bachelier het model.

Wat dit leert: de twee modellen zeggen ongeveer hetzelfde in een gebied, niet
overal. Ze zijn uitwisselbaar rond het geld en te onderscheiden waar de staarten
ertoe doen.
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
   handel zelf is veranderd. Welke meting zou de twee kunnen scheiden, en hebben
   wij die?
:::

:::{solution} ex-bachelier-3
:class: dropdown

**(1)** De cel herhaalt de kwintieltabel vanaf 1986.

```{code-cell} ipython3
size_late = hap_data.french("Portfolios_Formed_on_ME", "monthly").loc["1986-01":]
late_table = pd.DataFrame(
    {q: vr_table(np.log1p(size_late[q].dropna()), horizons=(2, 4, 8))
     for q in quintiles}
).T
late_table.index = size_table.index
late_table.round(3)
```

De rangorde blijft na 1985 bestaan, van 1,143 bij het kleinste naar 1,017 bij
het grootste kwintiel. Maar het hele profiel is naar beneden geschoven. Alleen
het kleinste kwintiel houdt met $z = 2{,}50$ nog significantie over, en bij
$q = 8$ is van het patroon niets meer over.

**(2)** De volgende cel zet de twee periodes naast elkaar, met de standaardfout
$1/\sqrt{T}$ per periode.

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

Het antwoord is ontnuchterend: geen van de vijf verschillen haalt twee
standaardfouten, de hoogste $t$-waarde is 1,28. Dat geen verschil significant
is, is [](#eq-bachelier-power) van de andere kant bekeken. Met 280 en 487 maandwaarnemingen is de
standaardfout van het verschil 0,075, en de verschuiving die we zien is 0,06 tot
0,10. De afwijking lijkt verdwenen, maar het verschil met de periode ervoor is
statistisch niet van nul te onderscheiden. Wie wil aantonen dat een anomalie na
publicatie verdwijnt, heeft daarom veel signalen tegelijk nodig.

**(3)** Om de verklaringen te scheiden, zou men willen weten hoe vaak de aandelen
in het kleinste kwintiel werkelijk verhandeld werden. Komt de autocorrelatie van
niet-synchrone handel, dan verdwijnt ze zodra er vaker gehandeld wordt, en dat is
sinds 1985 met ordes van grootte gebeurd. Komt ze van trage verwerking van
nieuws, dan verdwijnt ze zodra er meer analisten en meer arbitragekapitaal zijn,
en ook dat is gebeurd. Beide verklaringen voorspellen hier hetzelfde. De data die
ze zouden scheiden, de handelsfrequentie per aandeel vóór 1985, zitten in CRSP
(de betaalde databank met Amerikaanse aandelenkoersen sinds 1926), en die
hebben wij niet.


Wat dit leert: dat een anomalie na publicatie verdwijnt, is met één reeks niet
te bewijzen, en waarom ze verdween, is met de gratis data niet te beslissen.

:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
