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

(05-27-drie-antwoorden)=

# Habit, long-run risk en rampen

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1988–2013. Dit college volgt de literatuur van Rietz (1988) via Campbell en Cochrane (1999), Bansal en
Yaron (2004) en Barro (2006) tot Gabaix (2012) en Wachter (2013).

**Wat we al weten.** In [](#03-13-equity-premium-puzzle) haalde de consumptie-SDF
$m_{t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$ de aandelenpremie pas met een risicoaversie van
bijna vijftig ($\gamma = 47{,}6$), en bij zo'n risicoaversie wordt de rente absurd hoog.
Bovendien voorspelt de prijs-dividendratio vooral toekomstige rendementen, zodat de
discontovoet door de tijd moet bewegen. [](#05-26-sdf-unificatie) maakte van elk
waarderingsmodel een uitspraak over één object, de stochastische discontofactor
$m_{t+1}$.

**Welke vraag staat open.** Welke $m_{t+1}$, gebouwd uit consumptie, geeft tegelijk een
hoge premie, een lage en stabiele rente en een prijs-dividendratio die beweegt en
rendementen voorspelt, en kunnen de data tussen de kandidaten kiezen?
```

## Overzicht

Welke consumptie-SDF verklaart de aandelenpremie? Drie modellen doen het elk, met een
gewoonte, met langetermijnrisico of met zeldzame rampen. Elk leunt echter op een parameter
die honderd jaar data niet vastleggen, zodat die data er niet tussen kunnen kiezen. In dit
college:

- leiden we voor elk model de SDF, de premie en de rente af, en de reden dat de
  prijs-dividendratio beweegt,
- laten we zien dat Epstein-Zin-voorkeuren de rente van de premie loskoppelen, maar pas
  een premie opleveren als de groei voorspelbaar is,
- simuleren we elk model duizend keer over honderd jaar en kijken we welke
  steekproefmomenten de modellen nog onderscheiden,
- repliceren we kerngetallen van Wachter {cite}`Wachter2005`, Beeler en Campbell
  {cite}`BeelerCampbell2012` en Barro {cite}`Barro2009`, en leggen we de Amerikaanse
  data over 1930–2025 in de simulatiebanden.

Rond de eeuwwisseling kreeg de puzzel van de aandelenpremie drie antwoorden. Campbell en
Cochrane {cite}`CampbellCochrane1999` gaven beleggers een gewoonte, en Bansal en Yaron
{cite}`BansalYaron2004` combineerden de voorkeuren van Epstein en Zin
{cite}`EpsteinZin1989` met een kleine, persistente groeicomponent. Barro {cite}`Barro2006`
maakte, voortbouwend op Rietz {cite}`Rietz1988`, van de premie een vergoeding voor
zeldzame rampen. Santa-Clara {cite}`SantaClara2026` ziet in die drie antwoorden het moment
waarop de aandelenpremie van een getoetste theorie een feit met concurrerende theorieën
werd, omdat ze op de beschikbare data niet te onderscheiden zijn. Chen, Dou en Kogan
{cite}`ChenDouKogan2024` gaven in 2024 een maat voor hoe zwaar een model op zulke
parameters leunt, de *dark matter* (donkere materie) van het model.

## Intuïtie: waarom zou dit waar zijn?

De puzzel uit [](#03-13-equity-premium-puzzle) heeft twee helften. Consumptie schommelt
te weinig voor een grote premie, tenzij beleggers extreem risicomijdend zijn, en zulke
beleggers willen bij groeiende consumptie niet sparen, zodat de rente hoog zou moeten
zijn. Een antwoord moet de discontofactor dus in slechte toestanden veel groter maken
zonder hem gemiddeld te verlagen, en de drie modellen doen dat elk op een andere plaats.

**Gewoonte.** Een huishouden dat 100 besteedt en aan 95 gewend is, verliest bij een
daling met 2 bijna de helft van zijn marge boven de gewoonte. Hoe dichter het bij die
gewoonte zit, hoe risicomijdender het wordt, zodat de premie hoog is in slechte tijden en
een lage prijs hoge rendementen voorspelt. Omdat zo'n huishouden dan ook meer uit
voorzorg spaart, kan de rente constant blijven.

**Langetermijnrisico.** Stel dat consumptiegroei een kleine component heeft die jaren
aanhoudt, bijvoorbeeld een tiende procentpunt meer groei, tien jaar lang. In jaardata
verdwijnt die component in de ruis, maar een aandeel is een claim op alle toekomstige
dividenden, en een blijvend lagere groei treft ze allemaal. Met Epstein-Zin-voorkeuren
betalen beleggers veel voor bescherming tegen zulk nieuws, omdat die voorkeuren de
risicoaversie loskoppelen van de bereidheid om consumptie door de tijd te verschuiven.

**Rampen.** Stel dat de economie elk jaar een kleine kans heeft op een oorlog of
depressie waarin consumptie met een kwart of meer daalt. Aandelen storten dan in terwijl
obligaties gewoon uitbetalen, en een euro is enorm veel waard. Een kans van anderhalf
procent per jaar volstaat voor een premie van een paar procent, en omdat iedereen zich
tegen de ramp wil indekken, is de rente laag. In honderd jaar Amerikaanse data zit zo'n
ramp niet, zodat de premie te groot lijkt voor het risico dat we zagen.

Alle drie de verhalen passen dus op dezelfde getallen: de gemiddelde premie, de
volatiliteit, de lage rente en de beweeglijke prijs-dividendratio. We verwachten daarom
dat die getallen de modellen niet scheiden. Het verschil zit dan in wat slecht te meten
is, namelijk de snelheid van een gewoonte, de persistentie van een onzichtbare
groeicomponent en de frequentie van rampen die in de steekproef ontbraken. Als een
gemiddeld rendement na een eeuw al [de standaardfout van 2%](#00-01-rendementen) heeft,
zijn zulke grootheden nog veel slechter gemeten.

## Toy-voorbeeld: een ramp met de hand

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

We rekenen een Lucas-boom met twee toestanden door, zoals Rietz en Barro dat doen.
Consumptie is het dividend en groeit elk jaar met 2,5%, of krimpt in een ramp met 40%,
onafhankelijk door de tijd. Volgens Barro geeft bij $\gamma = 4$ een vaste daling van
ongeveer 40% dezelfde premie als de gemeten verdeling van rampgroottes. De rampkans is
zijn frequentie van 60 rampen in 35 landen in een eeuw {cite}`Barro2009`.

| | normaal jaar | rampjaar |
|---|---|---|
| kans | $1 - p = 0{,}983$ | $p = 0{,}017$ |
| bruto consumptiegroei $g$ | $g_n = 1{,}025$ | $g_d = 0{,}60$ |
| voorkeuren | CRRA, $\gamma = 4$, $\beta = 0{,}97$ | idem |

Het recept komt uit [](#03-12-consumptie-capm). De SDF is $m = \beta g^{-\gamma}$ en het
bruto risicovrije rendement $1 + R^f = 1/\E[m]$, met $R^f$ zoals overal in dit college de
netto rente. Bij onafhankelijke groei is de prijs-dividendratio $k/(1-k)$ met $k = \beta\,\E[g^{1-\gamma}]$.

1. **De SDF.** Met $1{,}025^4 = 1{,}103813$ is $m_n = 0{,}97/1{,}103813 = 0{,}878770$, en
   met $0{,}6^4 = 0{,}1296$ is $m_d = 0{,}97/0{,}1296 = 7{,}484568$. In een ramp is een
   euro dus achtenhalf keer zoveel waard.
2. **Zonder ramp.** Bij $p = 0$ is $1 + R^f = 1/m_n = 1{,}1380$, een rente van 13,8% en
   precies de rentepuzzel van [](#eq-equity-premium-puzzle-eis). Met
   $k = 0{,}97 \times 1{,}025^{-3} = 0{,}97 \times 0{,}928599 = 0{,}900741$ is de
   prijs-dividendratio 9,07, en omdat er geen risico is, is de premie nul.
3. **Met ramp.** Nu is $\E[m] = 0{,}983 \times 0{,}878770 + 0{,}017 \times 7{,}484568 = 0{,}991069$,
   dus $1 + R^f = 1{,}00901$ en een rente van 0,9%. Met $0{,}6^{-3} = 4{,}629630$ is voor
   het aandeel $k = 0{,}97\,(0{,}983 \times 0{,}928599 + 0{,}017 \times 4{,}629630) = 0{,}961772$,
   zodat de ratio stijgt naar 25,16.
4. **De premie.** Het verwachte bruto rendement is
   $\E[g]/k = 1{,}017775/0{,}961772 = 1{,}05823$, dus de premie is
   $5{,}823 - 0{,}901 = 4{,}92$ procentpunt.
5. **Een eeuw zonder ramp.** In een jaar zonder ramp verdient het aandeel
   $g_n/k = 1{,}025/0{,}961772 = 1{,}06574$, 5,67 procentpunt boven de rente en meer dan
   de ware premie. Honderd jaar zonder ramp hebben kans $0{,}983^{100} = 0{,}18$. Een
   steekproef zonder ramp toont dan een hoog rendement zonder het risico waarvoor dat
   rendement een vergoeding is, en dat heet het peso-probleem.

De codecel rekent dezelfde getallen na, met in de laatste kolom de wereld zonder ramp.

```{code-cell} ipython3
beta_a, gamma_a, g_n, b_toy, p_toy = 0.97, 4.0, 1.025, 0.40, 0.017
growth_toy = np.array([g_n, 1 - b_toy])

def rietz_toy(p):
    """Two-state iid Lucas tree: SDF, gross risk-free return, P/D, expected return and premium."""
    prob = np.array([1 - p, p])
    m = beta_a * growth_toy ** -gamma_a
    k = beta_a * prob @ growth_toy ** (1 - gamma_a)
    rf = 1 / (prob @ m)
    er = (prob @ growth_toy) / k
    return {"m_n": m[0], "m_d": m[1], "1+R^f": rf, "P/D": k / (1 - k), "E[R]": er,
            "premie (%)": 100 * (er - rf), "R zonder ramp": g_n / k}

hand = {"m_n": 0.878770, "m_d": 7.484568, "1+R^f": 1.00901, "P/D": 25.16, "E[R]": 1.05823,
        "premie (%)": 4.92, "R zonder ramp": 1.06574, "kans op 100 jaar zonder ramp": 0.18}
code = {**rietz_toy(p_toy), "kans op 100 jaar zonder ramp": (1 - p_toy) ** 100}
pd.DataFrame({"met de hand": hand, "code": code, "zonder ramp (p = 0)": rietz_toy(0.0)}).round(5)
```

Code en handberekening komen overeen. Bij dezelfde risicoaversie maakt een kleine rampkans
van een wereld zonder premie en met een rente van 13,8% een wereld met een premie van
bijna 5% en een rente onder 1%. De verwachte consumptiegroei daalt daarbij maar van 2,5%
naar 1,8%, omdat de ramp zelden komt.

## Theorie

De drie modellen zijn drie stochastische discontofactoren. Voor de gewoonte,
Epstein-Zin met langetermijnrisico en de rampen halen we uit de SDF de premie, de rente
en de toestandsvariabele die de prijs-dividendratio beweegt. Omdat elk model de premie
haalt met één slecht meetbare parameter, maakt de laatste subsectie daar een toetsbare
definitie van.

### Drie uitwegen uit de grens van Hansen en Jagannathan

Een consumptie-SDF kan de grens van Hansen en Jagannathan op drie manieren halen, en elk
model kiest er één. Volgens [](#eq-equity-premium-puzzle-hj) moet $\sigma(m)/\E[m]$
minstens de Sharpe-ratio van de markt zijn, ongeveer 0,4, terwijl CRRA
$\sigma(\log m) = \gamma\,\sigma(\Delta c)$ geeft bij een consumptie die maar een paar
procent schommelt. Een model kan dus de vermenigvuldiger van $\Delta c$ in slechte tijden
vergroten (gewoonte). Het kan ook $m$ laten reageren op nieuws over alle toekomstige jaren
(langetermijnrisico), of $\Delta c$ een staart geven die de steekproef niet toont
(rampen).

| | SDF $m_{t+1}$ | prijs van risico | vrije, moeilijk meetbare parameter |
|---|---|---|---|
| Campbell-Cochrane | $\beta\,(S_{t+1}C_{t+1}/S_tC_t)^{-\gamma}$ | $\gamma\,\sigma\,(1 + \lambda(s_t))$ | persistentie $\phi$ van de gewoonte |
| Bansal-Yaron | $\beta^\theta G_{t+1}^{-\theta/\psi} R_{w,t+1}^{\theta-1}$ | $\gamma$, $\lambda_e$, $\lambda_w$ | persistentie $\rho$ van $x_t$ |
| Rietz-Barro | $\beta\, G_{t+1}^{-\gamma}$ met sprongen | $\gamma\sigma$ plus sprongterm | rampkans $p$ en -grootte $b$ |

We schrijven $G_{t+1} = C_{t+1}/C_t$ voor bruto consumptiegroei, $\Delta c_{t+1} = \log G_{t+1}$
en $r^f = \log(1 + R^f)$, met $R^f$ de netto risicovrije rente. Barro schrijft $\rho$ voor
de tijdsvoorkeur, met $\beta = e^{-\rho}$, terwijl $\rho$ bij Bansal-Yaron de persistentie
van $x_t$ is.

### Campbell-Cochrane: de surplusratio

Een gewoonte maakt beleggers risicomijdender naarmate hun consumptie dichter bij die
gewoonte komt, zonder dat $\gamma$ groot hoeft te zijn. Neem aan dat nut afhangt van $C_t - X_t$,
met $X_t$ een gewoonte die door de consumptie van anderen wordt bepaald (*external habit*,
externe gewoonte). Dan is de kromming ten opzichte van $C_t$ gelijk aan
$\gamma C_t/(C_t - X_t)$. Bij de marge van 5% uit de intuïtie is dat twintig keer
$\gamma$.

Met de *surplus consumption ratio* $S_t = (C_t - X_t)/C_t$ (surplusratio) en
$s_t = \log S_t$ is marginaal nut $(S_tC_t)^{-\gamma}$, want de gewoonte is extern. De
SDF is dan

```{math}
:label: eq-drie-antwoorden-cc-sdf
m_{t+1} = \beta\left(\frac{S_{t+1}C_{t+1}}{S_t C_t}\right)^{-\gamma},
\qquad
\log m_{t+1} = \log\beta - \gamma\,(\Delta s_{t+1} + \Delta c_{t+1}),
```

en die is hoog als het surplus daalt, ook als consumptie nauwelijks beweegt. De lokale
risicoaversie is $\gamma/S_t$. Consumptiegroei is $\Delta c_{t+1} = g + v_{t+1}$ met
$v \sim N(0, \sigma^2)$, en het log surplus volgt

```{math}
:label: eq-drie-antwoorden-cc-s
s_{t+1} = (1-\phi)\,\bar s + \phi\, s_t + \lambda(s_t)\, v_{t+1} .
```

Het surplus keert dus met snelheid $1-\phi$ terug naar $\bar s$, en een consumptieschok
werkt erop in met gewicht $\lambda(s_t)$, de *sensitivity function*
(gevoeligheidsfunctie). Campbell en Cochrane kozen die functie zo dat de rente constant is
en $X_t$ onder $C_t$ blijft.

:::{prf:proposition} Constante rente in het habit-model
:label: prf-drie-antwoorden-cc-rente

Met [](#eq-drie-antwoorden-cc-sdf), [](#eq-drie-antwoorden-cc-s) en

```{math}
:label: eq-drie-antwoorden-cc-lambda
\lambda(s_t) = \frac{1}{\bar S}\sqrt{1 - 2(s_t - \bar s)} - 1 \quad (s_t \leq s_{\max}),
\qquad
\bar S = \sigma\sqrt{\frac{\gamma}{1-\phi}},
\qquad
s_{\max} = \bar s + \tfrac12(1 - \bar S^2),
```

en $\lambda = 0$ boven $s_{\max}$ is de log risicovrije rente constant. Ze is gelijk aan

```{math}
:label: eq-drie-antwoorden-cc-rf
r^f = -\log\beta + \gamma g - \tfrac12\gamma(1-\phi) .
```
:::

:::{prf:proof}
:class: dropdown

Uit [](#eq-drie-antwoorden-cc-sdf) en [](#eq-drie-antwoorden-cc-s) volgt
$\log m_{t+1} = \log\beta - \gamma g - \gamma(1-\phi)(\bar s - s_t) - \gamma(1 + \lambda(s_t))v_{t+1}$,
en dat is voorwaardelijk normaal. De log risicovrije rente is daarom

$$
r^f_t = -\log\E_t[m_{t+1}] = -\log\beta + \gamma g + \gamma(1-\phi)(\bar s - s_t)
- \tfrac12\gamma^2\sigma^2(1 + \lambda(s_t))^2 .
$$

Invullen van $(1 + \lambda)^2 = (1 - 2(s_t - \bar s))/\bar S^2$ en
$\bar S^2 = \gamma\sigma^2/(1-\phi)$ geeft
$\tfrac12\gamma^2\sigma^2(1+\lambda)^2 = \tfrac12\gamma(1-\phi)(1 - 2(s_t - \bar s))$. Daardoor vallen de termen in $s_t$ tegen elkaar weg. $\square$
:::

Een laag surplus zal naar verwachting herstellen, zodat beleggers willen lenen en de
rente zou stijgen, maar tegelijk is de SDF dan volatiel en willen ze uit voorzorg sparen.
De functie [](#eq-drie-antwoorden-cc-lambda) laat die twee effecten precies tegen elkaar
wegvallen. De maximale Sharpe-ratio $\gamma\sigma(1+\lambda(s_t))$ is bij het gemiddelde
surplus $\sqrt{\gamma(1-\phi)}$, in jaartermen $\sqrt{2 \times 0{,}13} \approx 0{,}51$, en
in recessies nog hoger.

Campbell en Cochrane simuleerden maandelijks met de jaarparameters in de tabel, die we
overnemen uit tabel 1 van Wachter {cite}`Wachter2005`. De persistentie $\phi$ draagt de
kalibratie, want ze is gekozen om de persistentie van de prijs-dividendratio na te
bootsen en niet gemeten aan hoe snel gewoontes zich aanpassen.

| parameter | waarde | betekenis |
|---|---|---|
| $g$ | 1,89% | gemiddelde consumptiegroei per jaar |
| $\sigma$ | 1,50% | volatiliteit van consumptiegroei per jaar |
| $r^f$ | 0,94% | constante log risicovrije rente |
| $\phi$ | 0,87 | persistentie van het surplus per jaar |
| $\gamma$ | 2 | kromming van het nut in $C_t - X_t$ |

Omdat $s_t$ de enige toestandsvariabele is, hangt de prijs-consumptieratio alleen van het
surplus af. Die functie $\mathrm{PC}(s)$ lost de Euler-vergelijking op:

```{math}
:label: eq-drie-antwoorden-cc-pd
\mathrm{PC}(s_t) = \E_t\!\left[m_{t+1}\, G_{t+1}\,\big(1 + \mathrm{PC}(s_{t+1})\big)\right].
```

De prijs van vandaag is dus de verdisconteerde waarde van het dividend en de prijs van
morgen. Er is geen gesloten vorm, en Wachter {cite}`Wachter2005` liet zien dat de
numerieke oplossing gevoelig is voor het rooster. Omdat
[](#eq-drie-antwoorden-cc-pd) lineair is in $\mathrm{PC}$, lossen we hem op een rooster in
één keer op als lineair stelsel $(\mathbf{I} - \mathbf{M})\,\mathbf{pc} = \mathbf{M}\mathbf{1}$,
met $\mathbf{M}$ de kwadratuur- en interpolatiegewichten. Rij $i$ van $\mathbf{M}$ hoort
bij roosterpunt $s_i$ en verdeelt de verdisconteerde groei $m\,G$ van elk kwadratuurpunt
over de twee roosterpunten rond het bijbehorende $s_{t+1}$.

De cel doet dat voor de consumptieclaim en voor een dividendclaim met een volatiliteit van
11,2% en een correlatie van 0,2 met consumptie, die we in de simulatie gebruiken.

```{code-cell} ipython3
CC = dict(g=0.0189, sig=0.015, gamma=2.0, phi=0.87, rf=0.0094, sig_w=0.112, rho_w=0.2)   # annual

def cc_solve(g, sig, gamma, phi, rf, sig_w=0.0, rho_w=0.0, n_nodes=20, lower=80.0, n_low=400, n_high=600):
    """Campbell-Cochrane price-dividend function on a grid in s, solved as one linear system (monthly model)."""
    gm, sm, phim, rfm, swm = g / 12, sig / np.sqrt(12), phi ** (1 / 12), rf / 12, sig_w / np.sqrt(12)
    S_bar = sm * np.sqrt(gamma / (1 - phim))
    s_bar = np.log(S_bar)
    s_max = s_bar + 0.5 * (1 - S_bar**2)
    log_beta = gamma * gm - 0.5 * gamma * (1 - phim) - rfm                 # eq. cc-rf solved for beta
    lam = lambda s: np.where(s <= s_max, np.sqrt(np.maximum(1 - 2 * (s - s_bar), 0.0)) / S_bar - 1, 0.0)
    s = np.concatenate([np.linspace(s_bar - lower, s_bar - 1.5, n_low, endpoint=False),
                        np.linspace(s_bar - 1.5, s_max, n_high)])
    nodes, weights = np.polynomial.hermite_e.hermegauss(n_nodes)
    v = sm * nodes
    L = lam(s)[:, None]
    s_next = np.clip((1 - phim) * s_bar + phim * s[:, None] + L * v, s[0], s_max)
    base = log_beta - gamma * gm - gamma * (1 - phim) * (s_bar - s)[:, None]
    # dividend growth gm + w, w = rho_w (swm/sm) v + sqrt(1 - rho_w^2) swm eps, eps integrated out analytically
    load = rho_w * swm / sm if sig_w > 0 else 1.0
    extra = 0.5 * (1 - rho_w**2) * swm**2 if sig_w > 0 else 0.0
    # step 1: kernel K[i, q] = quadrature weight x m x dividend growth, from grid point s_i at node q
    K = weights / weights.sum() * np.exp(base + gm + extra + (load - gamma * (1 + L)) * v)
    rf_check = -np.log((weights / weights.sum() * np.exp(base - gamma * (1 + L) * v)).sum(axis=1))
    # step 2: split each K[i, q] over the two grid points around s_next[i, q] (linear interpolation) -> row i of M
    n = len(s)
    j = np.clip(np.searchsorted(s, s_next) - 1, 0, n - 2)
    w_hi = (s_next - s[j]) / (s[j + 1] - s[j])
    M = np.zeros((n, n))
    rows = np.broadcast_to(np.arange(n)[:, None], j.shape)
    np.add.at(M, (rows, j), K * (1 - w_hi))
    np.add.at(M, (rows, j + 1), K * w_hi)
    pd_grid = np.linalg.solve(np.eye(n) - M, K.sum(axis=1))
    return dict(s=s, pd=pd_grid, s_bar=s_bar, s_max=s_max, S_bar=S_bar, beta=np.exp(12 * log_beta), lam=lam,
                gm=gm, sm=sm, phim=phim, rfm=rfm, swm=swm, rho_w=rho_w,
                rf_check=12 * rf_check[s <= s_max])

cc_cons = cc_solve(**{**CC, "sig_w": 0.0, "rho_w": 0.0})
cc_div = cc_solve(**CC)
print(f"S-bar = {cc_div['S_bar']:.4f}, S_max = {np.exp(cc_div['s_max']):.4f}, beta (jaar) = {cc_div['beta']:.4f}")
print(f"r^f op het rooster: {cc_div['rf_check'].min():.5f} tot {cc_div['rf_check'].max():.5f}  (doel 0.0094)")
```

De code geeft $\bar S = 0{,}057$, $S_{\max} = 0{,}094$ en $\beta = 0{,}896$ per jaar, wat
Wachter tot 0,90 afrondt. De rente is op het hele rooster 0,94%, zoals
[](#prf-drie-antwoorden-cc-rente) belooft.

### Epstein-Zin en de SDF

Epstein-Zin-voorkeuren scheiden de afkeer van risico van de afkeer van schommelingen door
de tijd, en daardoor telt in de SDF naast consumptie ook het rendement op vermogen.
Epstein en Zin {cite}`EpsteinZin1989` en Weil {cite}`Weil1989` definieerden het nut
recursief, met een risicoaversie $\gamma$ en een intertemporele
substitutie-elasticiteit $\psi$ (EIS) als aparte parameters:

```{math}
:label: eq-drie-antwoorden-ez-nut
U_t = \left[(1-\beta)\,C_t^{1-1/\psi} + \beta\left(\E_t\!\left[U_{t+1}^{1-\gamma}\right]\right)^{\frac{1-1/\psi}{1-\gamma}}\right]^{\frac{1}{1-1/\psi}} .
```

Het nut van vandaag middelt dus consumptie nu en het zekerheidsequivalent van het nut
morgen. Daarbij bepaalt $\gamma$ hoe zwaar risico telt en $\psi$ hoe gemakkelijk
consumptie door de tijd verschuift.

:::{prf:proposition} De Epstein-Zin-SDF
:label: prf-drie-antwoorden-ez-sdf

Laat $R_{w,t+1}$ het rendement zijn op de claim op de hele consumptiestroom en
$\theta = (1-\gamma)/(1-1/\psi)$. Dan is

```{math}
:label: eq-drie-antwoorden-ez-sdf
m_{t+1} = \beta^\theta\, G_{t+1}^{-\theta/\psi}\, R_{w,t+1}^{\theta - 1} .
```

Bij $\gamma = 1/\psi$ is $\theta = 1$, en dan is dit de CRRA-SDF. 
:::

:::{prf:proof}
:class: dropdown

*Schets.* Homogeniteit geeft $U_t = \Phi_t W_t$, en de eerste-ordevoorwaarde met de
envelopstelling geeft
$m_{t+1} = \beta G_{t+1}^{-1/\psi}(U_{t+1}/\mathcal{R}_t)^{1/\psi - \gamma}$, met
$\mathcal{R}_t = (\E_t[U_{t+1}^{1-\gamma}])^{1/(1-\gamma)}$ het zekerheidsequivalent van
het vervolgnut. De Euler-vergelijking voor het vermogensrendement geeft
$(U_{t+1}/\mathcal{R}_t)^{1-1/\psi} = \beta\, G_{t+1}^{-1/\psi} R_{w,t+1}$
{cite}`EpsteinZin1989,Weil1989`. Verheffen tot de macht $\theta - 1$ en invullen geeft
[](#eq-drie-antwoorden-ez-sdf). $\square$
:::

In logs is $\log m_{t+1} = \theta\log\beta - (\theta/\psi)\Delta c_{t+1} + (\theta-1)r_{w,t+1}$.
Bij $\gamma > 1$ en $\psi > 1$ is $\theta < 0$ en dus $\theta - 1 < 0$, zodat een slecht
rendement op vermogen de SDF verhoogt. Zo krijgt nieuws over de hele toekomstige
consumptiestroom een prijs, ook als
het de consumptie van dit jaar niet raakt.

Bij onafhankelijke lognormale groei, $\Delta c_{t+1} \sim N(\mu, \sigma^2)$, is de
verhouding van vermogen tot consumptie constant en $r_{w,t+1} = \Delta c_{t+1} + \kappa$.
De helling van $\log m$ op $\Delta c$ is dan $-\theta/\psi + \theta - 1 = -\gamma$, en
uitwerken (oefening 2) geeft

$$
\log(1 + R^f) = -\log\beta + \frac{\mu}{\psi} - \tfrac12\sigma^2\gamma\Big(1 + \frac1\psi\Big) + \frac{\sigma^2}{2\psi},
\qquad
\log\frac{\E[R_w]}{1 + R^f} = \gamma\sigma^2 .
$$

Met $\beta = 0{,}98$, $\mu = \sigma = 0{,}02$ en $\gamma = 10$ komt daar het volgende
uit:

- bij $\psi = 1{,}5$ is $\log(1 + R^f) = 0{,}020203 + 0{,}013333 - 0{,}003333 + 0{,}000133 = 0{,}030336$,
  een rente van 3,0%;
- bij $\psi = 1/\gamma = 0{,}1$, het CRRA-geval, is $\log(1 + R^f) = 0{,}020203 + 0{,}2 - 0{,}022 + 0{,}002 = 0{,}200203$,
  een rente van 20%;
- in beide gevallen is de premie $\gamma\sigma^2 = 10 \times 0{,}0004 = 0{,}40$ procentpunt.

De cel rekent dezelfde formules uit, ook voor $\gamma = 5$, en controleert met een
Monte-Carlo-steekproef dat de SDF de claim op consumptie op één waardeert.

```{code-cell} ipython3
def ez_iid(beta, mu, sigma, gamma, psi):
    """Log risk-free rate and log premium on the wealth claim, iid lognormal growth."""
    log_rf = -np.log(beta) + mu / psi - 0.5 * sigma**2 * gamma * (1 + 1 / psi) + 0.5 * sigma**2 / psi
    return log_rf, gamma * sigma**2

toy_b = {}
for gamma_b, psi_b in [(10, 1.5), (10, 0.1), (5, 1.5), (5, 0.2)]:
    log_rf, prem = ez_iid(0.98, 0.02, 0.02, gamma_b, psi_b)
    toy_b[f"gamma = {gamma_b}, psi = {psi_b}"] = {"log(1+R^f)": log_rf, "log premie": prem}

# check the closed form against a brute-force Euler equation with the SDF above
theta = (1 - 10) / (1 - 1 / 1.5)
z = rng.standard_normal(2_000_000)
dc = 0.02 + 0.02 * z
kappa = -np.log(0.98) - ((1 - 10) * 0.02 + 0.5 * (1 - 10) ** 2 * 0.02**2) / theta
log_m = theta * np.log(0.98) - theta / 1.5 * dc + (theta - 1) * (dc + kappa)
print(f"E[m R_w] = {np.mean(np.exp(log_m + dc + kappa)):.4f}  (moet 1 zijn)")
print(f"log(1+R^f) uit simulatie = {-np.log(np.mean(np.exp(log_m))):.4f}  (met de hand: 0.0303)")
pd.DataFrame(toy_b).T.round(6)
```

De eerste twee rijen geven de handgetallen, en bij $\gamma = 5$ halveert de premie
terwijl de rente vooral met $\psi$ beweegt. Een hogere $\psi$ verlaagt de rente, omdat
beleggers dan minder vergoeding vragen om consumptiegroei af te wachten, maar de premie
blijft $\gamma\sigma^2$, even klein als bij CRRA. Pas als groei voorspelbaar is, krijgt
$\psi$ invloed op de premie, en dat is de bijdrage van Bansal en Yaron.

### Bansal-Yaron: langetermijnrisico

Een kleine, persistente groeicomponent maakt de SDF hoog wanneer het vermogen daalt door
slecht nieuws over de verre toekomst, mits $\psi > 1$. Een schok in $x_t$ die per maand
met factor $\rho$ uitdooft, weegt in de waarde van een claim op alle toekomstige
consumptie ongeveer $1/(1-\rho)$ keer, bij $\rho = 0{,}979$ bijna vijftig keer. Bij
$\psi > 1$ wint het groei-effect van het rente-effect, zodat het vermogensrendement daalt
als de vooruitzichten verslechteren. Omdat $\theta - 1 < 0$ is, stijgt de SDF dan, en daarom
betalen beleggers, zoals de intuïtie al zei, veel voor bescherming tegen slecht groeinieuws.

Bansal en Yaron schrijven, per maand,

```{math}
:label: eq-drie-antwoorden-by-proces
\begin{aligned}
\Delta c_{t+1} &= \mu + x_t + \sigma_t\eta_{t+1}, &
x_{t+1} &= \rho x_t + \varphi_e\sigma_t e_{t+1}, \\
\Delta d_{t+1} &= \mu_d + \phi x_t + \varphi_d\sigma_t u_{t+1}, &
\sigma^2_{t+1} &= \bar\sigma^2 + \nu_1(\sigma^2_t - \bar\sigma^2) + \sigma_w w_{t+1},
\end{aligned}
```

met onafhankelijke standaardnormale schokken, zodat consumptie- en dividendgroei een trage
component $x_t$ delen, waarop dividenden $\phi$ keer zo sterk reageren. De volatiliteit
beweegt zelf langzaam, en de kalibratie komt uit tabel I van Beeler en Campbell
{cite}`BeelerCampbell2012`, die de parameters van Bansal en Yaron overnemen.

| parameter | waarde | betekenis |
|---|---|---|
| $\beta$, $\gamma$, $\psi$ | 0,998 / 10 / 1,5 | discontofactor per maand, risicoaversie, EIS |
| $\mu = \mu_d$ | 0,0015 | gemiddelde groei per maand |
| $\rho$, $\varphi_e$ | 0,979 / 0,044 | persistentie en schokgrootte van $x_t$ |
| $\bar\sigma$, $\nu_1$, $\sigma_w$ | 0,0078 / 0,987 / 0,0000023 | niveau, persistentie en schok van de volatiliteit |
| $\phi$, $\varphi_d$ | 3 / 4,5 | hefboom en eigen volatiliteit van dividenden |

De halfwaardetijd van $x_t$ is $\ln 2/(-\ln 0{,}979) = 33$ maanden, en zijn
standaarddeviatie $\varphi_e\bar\sigma/\sqrt{1-\rho^2} = 0{,}0017$ per maand is in
jaardata onzichtbaar klein. Voor de oplossing gebruiken we de Campbell-Shiller-benadering
[](#eq-voorspelbaarheid-cs-rendement) uit [](#04-20-voorspelbaarheid), nu voor de claim op
consumptie, en vanaf hier zijn kleine letters logs. Dan is
$r_{w,t+1} = \kappa_0 + \kappa_1 z_{t+1} - z_t + \Delta c_{t+1}$, met $z_t$ de log
prijs-consumptieratio en $\kappa_1 = e^{\bar z}/(1 + e^{\bar z})$ net onder één, de $\rho$
van dat college. De constante $\kappa_0 = \log(1 + e^{\bar z}) - \kappa_1\bar z$ hoort
erbij, en beide hangen af van de gemiddelde ratio $\bar z$, die de oplossing zelf bepaalt.
De oplossing heeft twee kanalen, groeinieuws via $A_1$ en onzekerheidsnieuws via $A_2$.
Het tweede kanaal, waarin een volatiliteitsschok de prijs verlaagt, levert bij deze
kalibratie maar 0,2 van de ruim 5 procentpunt premie, omdat $\sigma_w$ zo klein is. Vooral
$A_1$ en $A_{1,m}$ doen er dus toe.

:::{prf:proposition} Oplossing van het long-run-risksmodel
:label: prf-drie-antwoorden-by

Stel $z_t = A_0 + A_1 x_t + A_2\sigma^2_t$ en, voor de log prijs-dividendratio,
$z_{m,t} = A_{0,m} + A_{1,m}x_t + A_{2,m}\sigma^2_t$, zodat $A_{1,m}$ en $A_{2,m}$ zeggen hoe
sterk die ratio op $x_t$ en $\sigma^2_t$ reageert, en laat $\kappa_{1,m}$ de constante
$\kappa_1$ van de markt zijn, in de gemiddelde $\bar z_m$. De Euler-vergelijkingen voor $R_w$
en $R_m$ zijn tot op de loglinearisering exact vervuld met

```{math}
:label: eq-drie-antwoorden-by-A
A_1 = \frac{1 - 1/\psi}{1 - \kappa_1\rho},
\qquad
A_2 = \frac{\tfrac12\big[(1-\gamma)^2 + (\theta\kappa_1 A_1\varphi_e)^2\big]}{\theta(1 - \kappa_1\nu_1)},
\qquad
A_{1,m} = \frac{\phi - 1/\psi}{1 - \kappa_{1,m}\rho},
```

en de innovatie in de SDF is

```{math}
:label: eq-drie-antwoorden-by-sdf
m_{t+1} - \E_t m_{t+1} = -\gamma\,\sigma_t\eta_{t+1} - \lambda_e\,\sigma_t e_{t+1} - \lambda_w\,\sigma_w w_{t+1},
\qquad
\lambda_e = (1-\theta)\kappa_1 A_1\varphi_e,
\quad
\lambda_w = (1-\theta)\kappa_1 A_2 .
```

en het verwachte log overrendement op de markt, inclusief de Jensen-term, is

```{math}
:label: eq-drie-antwoorden-by-premie
\E_t[r_{m,t+1} - r^f_t] + \tfrac12\Var_t(r_{m,t+1})
= \underbrace{\lambda_e\,\kappa_{1,m}A_{1,m}\varphi_e\,\sigma^2_t}_{\text{langetermijnrisico}}
\;+\; \underbrace{\lambda_w\,\kappa_{1,m}A_{2,m}\,\sigma^2_w}_{\text{volatiliteitsrisico}} .
```
:::

Het bewijs zet de proefoplossing in de Euler-vergelijking $\E_t[e^{m+r_w}] = 1$ en eist dat
de coëfficiënten van $x_t$ en $\sigma^2_t$ afzonderlijk nul zijn {cite}`BansalYaron2004`.
De premie [](#eq-drie-antwoorden-by-premie) is dan een vergoeding voor nieuws over de
groei plus een vergoeding voor nieuws over de onzekerheid. Drie gevolgen zijn voor de rest
van het college van belang.

- $A_1 > 0$ vereist $\psi > 1$. Alleen dan stijgt de vermogensprijs bij goed groeinieuws,
  zodat het vermogen juist bij slecht nieuws verliest en een slechte verzekering is. De
  prijs van langetermijnrisico, $\lambda_e = (\gamma - 1/\psi)\kappa_1\varphi_e/(1 - \kappa_1\rho)$,
  is positief zodra $\gamma > 1/\psi$ en is bij deze kalibratie 17,9. Bij $\psi < 1$ draait
  dus niet $\lambda_e$ om maar de reactie van de vermogensprijs, en de premie krimpt omdat
  $A_{1,m}$ kleiner wordt. Die hoge EIS ligt boven de meeste macro-econometrische
  schattingen, die Bansal en Yaron als vertekend door tijdvariërende volatiliteit
  beschouwen.
- De premie is groot, omdat $A_{1,m}$ een factor $1/(1-\kappa_{1,m}\rho) \approx 40$ bevat
  en dividenden met $\phi = 3$ drie keer zo sterk op $x_t$ reageren als consumptie.
- De persistentie $\rho$ bepaalt vrijwel alles, terwijl honderd jaar jaardata die
  persistentie nauwelijks vastleggen, omdat $x_t$ niet waarneembaar is.

De cel lost het model op en splitst de premie in de twee kanalen.

```{code-cell} ipython3
BY = dict(beta=0.998, gamma=10.0, psi=1.5, mu=0.0015, rho=0.979, phi_e=0.044, sig=0.0078, nu1=0.987,
          sig_w=0.0000023, mu_d=0.0015, phi=3.0, phi_d=4.5)          # monthly, Beeler-Campbell (2012) Table I

def by_solve(p):
    """Log-linear solution of Bansal-Yaron (2004) with endogenous linearisation constants."""
    beta, gamma, psi, mu, rho = p["beta"], p["gamma"], p["psi"], p["mu"], p["rho"]
    pe, s2, nu, sw = p["phi_e"], p["sig"] ** 2, p["nu1"], p["sig_w"]
    theta = (1 - gamma) / (1 - 1 / psi)
    # Campbell-Shiller constants at mean log ratio z: kappa_0 = log(1 + e^z) - kappa_1 z, kappa_1 = e^z / (1 + e^z)
    kappas = lambda z: (np.log1p(np.exp(z)) - np.exp(z) / (1 + np.exp(z)) * z, np.exp(z) / (1 + np.exp(z)))

    def wealth(z):
        k0, k1 = kappas(z)
        A1 = (1 - 1 / psi) / (1 - k1 * rho)
        A2 = 0.5 * ((1 - gamma) ** 2 + (theta * k1 * A1 * pe) ** 2) / (theta * (1 - k1 * nu))
        A0 = (np.log(beta) + k0 + k1 * A2 * s2 * (1 - nu) + (1 - 1 / psi) * mu + 0.5 * theta * (k1 * A2 * sw) ** 2) / (1 - k1)
        return k0, k1, A0, A1, A2

    z = optimize.brentq(lambda z: wealth(z)[2] + wealth(z)[4] * s2 - z, 0.5, 15)
    k0, k1, A0, A1, A2 = wealth(z)
    lam_e, lam_w = (1 - theta) * k1 * A1 * pe, (1 - theta) * k1 * A2
    m0 = theta * np.log(beta) - theta / psi * mu + (theta - 1) * (k0 + k1 * A0 + k1 * A2 * s2 * (1 - nu) - A0 + mu)
    ms = (theta - 1) * A2 * (k1 * nu - 1)

    def market(z):
        k0m, k1m = kappas(z)
        A1m = (p["phi"] - 1 / psi) / (1 - k1m * rho)
        A2m = (ms + 0.5 * (gamma**2 + p["phi_d"] ** 2 + (k1m * A1m * pe - lam_e) ** 2)) / (1 - k1m * nu)
        A0m = (m0 + k0m + k1m * A2m * s2 * (1 - nu) + p["mu_d"] + 0.5 * sw**2 * (k1m * A2m - lam_w) ** 2) / (1 - k1m)
        return k0m, k1m, A0m, A1m, A2m

    zm = optimize.brentq(lambda z: market(z)[2] + market(z)[4] * s2 - z, 0.5, 15)
    k0m, k1m, A0m, A1m, A2m = market(zm)
    return dict(p=p, theta=theta, A1=A1, A2=A2, k1=k1, A0m=A0m, A1m=A1m, A2m=A2m, k0m=k0m, k1m=k1m,
                lam_e=lam_e, lam_w=lam_w, m0=m0, mx=-1 / psi, ms=ms)

by = by_solve(BY)
prem_lrr = by["lam_e"] * by["k1m"] * by["A1m"] * BY["phi_e"] * BY["sig"] ** 2
prem_vol = by["lam_w"] * by["k1m"] * by["A2m"] * BY["sig_w"] ** 2
pd.Series({"theta": by["theta"], "A_1": by["A1"], "A_1,m": by["A1m"], "kappa_1,m": by["k1m"],
           "lambda_e": by["lam_e"], "premie via x_t (%/jaar)": 1200 * prem_lrr,
           "premie via sigma_t (%/jaar)": 1200 * prem_vol}).round(3)
```

Bij deze kalibratie is $\theta = -27$, zodat de SDF sterk op het vermogensrendement
reageert, en $A_{1,m} \approx 93$, zodat een stijging van
$x_t$ met één standaarddeviatie de log prijs-dividendratio met 0,16 verhoogt. Vrijwel de
hele premie van ruim 5% per jaar komt uit het langetermijnkanaal, want het
volatiliteitskanaal levert minder dan een tiende daarvan.

### Rietz-Barro: CRRA met sprongen

Met rampen is de premie een verzekeringspremie, het product van de kans, het verlies en
de waarde van een euro in de ramp. Een aandeel verliest in een ramp een fractie $b$ van
zijn waarde en een obligatie niets, zodat een aandeelhouder rampbescherming verkoopt en
daarvoor betaald wil worden. De rente daalt, omdat de wens om zich te verzekeren de vraag
naar veilige activa opdrijft, zoals in het toy-voorbeeld, waar ze van 13,8% naar 0,9%
zakte.

Barro {cite}`Barro2006,Barro2009` schrijft
$\log C_{t+1} - \log C_t = g + u_{t+1} + \log(1-b_{t+1})\,\mathbb{1}\{\text{ramp}\}$, met
$u \sim N(0, \sigma^2)$ en rampkans $p$ per jaar. Met CRRA en een dividend gelijk aan
consumptie volgt, zoals in [](#03-12-consumptie-capm) maar met de ramp als extra
toestand, de volgende propositie.

:::{prf:proposition} Rente en premie met rampen
:label: prf-drie-antwoorden-barro

We gebruiken de continue-tijdsbenadering en laten termen van orde $p^2$ en $p\sigma^2$ weg. Dan geldt

```{math}
:label: eq-drie-antwoorden-barro
\begin{aligned}
r^f &= \rho + \gamma g - \tfrac12\gamma^2\sigma^2 - p\,\big(\E[(1-b)^{-\gamma}] - 1\big), \\
\log\E[R] - r^f &= \gamma\sigma^2 + p\,\E\big[(1-b)^{-\gamma} - (1-b)^{1-\gamma} - b\big]
= \gamma\sigma^2 + p\,\E\big[b\,\big((1-b)^{-\gamma} - 1\big)\big], \\
\mathrm{PD} &= \Big[\rho + (\gamma-1)g - \tfrac12(\gamma-1)^2\sigma^2 - p\,\big(\E[(1-b)^{1-\gamma}] - 1\big)\Big]^{-1}.
\end{aligned}
```
:::

:::{prf:proof}
:class: dropdown

Met $m = e^{-\rho}G^{-\gamma}$ en $G = e^{g+u}(1-b)^{D}$, waarbij $D = 1$ met kans $p$, is
$\E[G^{-\gamma}] = e^{-\gamma g + \frac12\gamma^2\sigma^2}\,(1 - p + p\E[(1-b)^{-\gamma}])$.
De log van het bruto risicovrije rendement is $r^f = -\log\E[m]$, en met
$\log(1 + p(\cdot)) \approx p(\cdot)$ volgt de eerste regel. Voor de boom geeft
[](#eq-consumptie-capm-lognormaal) een constante ratio $\mathrm{PD} = k/(1-k)$ met
$k = e^{-\rho}\E[G^{1-\gamma}]$, dus $1/\mathrm{PD} \approx -\log k$, de derde regel. Het
verwachte rendement is $\E[G]/k$ met $\log\E[G] \approx g + \tfrac12\sigma^2 - p\E[b]$, en
aftrekken van de rente geeft de tweede regel. $\square$
:::

De premie is dus de CRRA-term $\gamma\sigma^2$ uit
[](#eq-equity-premium-puzzle-lognormaal) plus een rampterm. Die rampterm is het product
van een kans die in één land nauwelijks te meten is en een gewogen verlies
$\E[b(1-b)^{-\gamma}]$ dat door
de grootste rampen wordt bepaald. Een hogere rampkans verlaagt de rente en verhoogt de
premie, in de richting die het rampverhaal in de intuïtie verwachtte.

Barro telde 60 dalingen van het BBP per hoofd van minstens 15% in 35 landen over de
twintigste eeuw, wat een rampkans van 1,7% per jaar geeft, dezelfde als in het
toy-voorbeeld. Bij $\gamma = 4$ geven die dalingen $\E[(1-b)^{-4}] = 7{,}69$ en
$\E[(1-b)^{-3}] = 4{,}05$ {cite}`Barro2009`. De cel zet de drie regels van
[](#eq-drie-antwoorden-barro), met $g = 0{,}025$, $\sigma = 0{,}02$ en $\rho = 0{,}027$,
naast tabel 3 van Barro (2009).

```{code-cell} ipython3
gamma_b, g_b, sigma_b, p_b, rho_b = 4.0, 0.025, 0.02, 0.017, 0.027
EB_g, EB_1g, E_b = 7.69, 4.05, 0.29                         # Barro (2009), footnote 10

rf_barro = rho_b + gamma_b * g_b - 0.5 * gamma_b**2 * sigma_b**2 - p_b * (EB_g - 1)
prem_barro = gamma_b * sigma_b**2 + p_b * (EB_g - EB_1g - E_b)
pd_barro = 1 / (rho_b + (gamma_b - 1) * g_b - 0.5 * (gamma_b - 1) ** 2 * sigma_b**2 - p_b * (EB_1g - 1))
pd.DataFrame(
    {"hier": [rf_barro, rf_barro + prem_barro, prem_barro, pd_barro],
     "Barro (2009), tabel 3": [0.010, 0.069, np.nan, 20.7],
     "zonder rampen (p = 0)": [rho_b + gamma_b * g_b - 0.5 * gamma_b**2 * sigma_b**2, np.nan, gamma_b * sigma_b**2,
                               1 / (rho_b + (gamma_b - 1) * g_b - 0.5 * (gamma_b - 1) ** 2 * sigma_b**2)]},
    index=["r^f", "r^e", "premie", "P/D"],
).round(4)
```

De formules reproduceren de rij $\gamma = \theta = 4$ van Barro (2009) op drie decimalen,
met een prijs-dividendratio van 20,7, een rente van 1,0% en een verwacht rendement van
6,9%. Zonder rampen zou de rente 12,4% zijn en de premie 0,16 procentpunt, en dan is de
puzzel van Mehra en Prescott terug.

### Waarom de prijs-dividendratio beweegt

Elk model laat de prijs-dividendratio bewegen via een langzame toestandsvariabele, maar
alleen in het habit-model loopt die beweging volledig via de premie, terwijl ze in
Bansal-Yaron vooral en in de Gabaix-variant deels via verwachte dividendgroei loopt. Volgens
[](#eq-voorspelbaarheid-cs-pv) beweegt $pd_t = -dp_t$ alleen als verwachte rendementen of
verwachte dividendgroei bewegen, zodat een model dat rendementsvoorspelbaarheid wil
verklaren een trage toestandsvariabele nodig heeft die de premie verschuift.

- **Habit.** De toestand is $s_t$, en de voorwaardelijke Sharpe-ratio
  $\gamma\sigma(1 + \lambda(s_t))$ daalt in $s_t$. Na een reeks slechte jaren is de premie
  hoog en de prijs laag, en volgen hoge rendementen. Omdat de rente constant is, is alle
  beweging in $pd_t$ beweging in de premie, en dividendgroei is niet voorspelbaar, precies
  de hond die niet blafte uit [](#04-20-voorspelbaarheid).
- **Langetermijnrisico.** De premie [](#eq-drie-antwoorden-by-premie) hangt alleen van
  $\sigma^2_t$ af, terwijl $x_t$ de ratio via verwachte dividendgroei beweegt. Omdat de
  volatiliteitscomponent weinig variantie draagt, voorspelt het model zwakke
  rendementsvoorspelbaarheid en sterke dividendgroeivoorspelbaarheid, het omgekeerde van
  wat [](#04-20-voorspelbaarheid) in de data vond.
- **Rampen.** Met een constante $p$ en onafhankelijke $b$ is $pd_t$ constant. Gabaix
  {cite}`Gabaix2012` laat daarom variëren hoeveel het dividend in een ramp daalt, zodat de
  ratio beweegt met de premie én met de verwachte dividendgroei. Wachter
  {cite}`Wachter2013` laat de rampkans zelf variëren, met Epstein-Zin-nut en $\psi = 1$.

### Observationele equivalentie

Drie modellen die elk één moeilijk meetbare parameter op hetzelfde handvol momenten
afstellen, reproduceren die momenten per constructie en verschillen pas in momenten die
we slecht meten. Een kalibratie kiest de vrije parameters immers zo dat de gemiddelde
premie, de volatiliteit, de rente en de persistentie van de prijs-dividendratio kloppen.

:::{prf:definition} Observationele equivalentie op een steekproef
:label: prf-drie-antwoorden-equivalentie

Laat $\mathbf{h}_T$ een vector van steekproefmomenten over $T$ jaar zijn, bijvoorbeeld de
gemiddelde premie en de volatiliteit van de prijs-dividendratio, en $F^{(k)}_T$ de
verdeling van $\mathbf{h}_T$ onder model $k$. Modellen $k$ en $l$ heten *observationeel
equivalent op $\mathbf{h}_T$* als aan twee voorwaarden is voldaan. (i) De gerealiseerde $\mathbf{h}_T$ valt onder geen van beide in het kritieke gebied van een toets met significantieniveau $\alpha$. (ii) Elke toets met significantieniveau $\alpha$ van $F^{(k)}_T$ tegen $F^{(l)}_T$ heeft een onderscheidingsvermogen dat niet wezenlijk boven $\alpha$ ligt.
:::

Gewoon gezegd passen de data bij beide modellen, en onderscheidt geen toets met $T$ jaar ze
beter dan toeval. Die equivalentie hangt dus af van $T$, want met duizend jaar data zijn
de modellen te scheiden en met honderd niet. Ze hangt ook af van de momenten in
$\mathbf{h}$, en twee soorten
momenten zouden de modellen kunnen scheiden.

- **Consumptievoorspelbaarheid op lange horizon.** Volgens Bansal-Yaron is
  consumptiegroei op veel lags positief autogecorreleerd, volgens habit en rampen niet.
  Beeler en Campbell vonden naoorlogs geen autocorrelatie boven wat tijdsaggregatie al
  oplevert. Ze concludeerden dat het bewijs voor een persistente component staat of valt
  met de data uit de Grote Depressie {cite}`BeelerCampbell2012`.
- **Optieprijzen.** Rampen zitten in de linkerstaart, die in honderd jaar rendementen
  onzichtbaar is maar wel in de prijs van putopties ver uit het geld zit. Santa-Clara en
  Yan {cite}`SantaClaraYan2010` haalden uit S&P 500-opties de sprongrisico's die
  beleggers vrezen, en [](#05-29-opties-crashrisico) werkt dat programma uit.

```{admonition} Samengevat
:class: tip

- Gewoonte, [](#eq-drie-antwoorden-cc-sdf): een lager surplus verhoogt de risicoaversie
  $\gamma/S_t$ en dus de premie, terwijl de rente constant blijft
  ([](#eq-drie-antwoorden-cc-rf)); een hogere $\phi$ maakt het surplus en de
  prijs-dividendratio trager, omdat de gewoonte zich dan langzamer aan de consumptie aanpast.
- Epstein-Zin, [](#eq-drie-antwoorden-ez-sdf): een hogere $\psi$ verlaagt de rente, omdat
  beleggers minder vergoeding vragen om consumptie uit te stellen, en laat bij onafhankelijke
  groei de premie $\gamma\sigma^2$ ongemoeid, omdat alleen $\gamma$ de prijs van een
  consumptieschok bepaalt.
- Langetermijnrisico, [](#eq-drie-antwoorden-by-premie): een hogere $\psi$ of $\rho$
  vergroot $A_{1,m}$ en dus de premie, omdat nieuws over $x_t$ langer in de prijs
  doorwerkt.
- Rampen, [](#eq-drie-antwoorden-barro): een hogere rampkans $p$ verlaagt de rente en
  verhoogt de premie, omdat de vraag naar verzekering stijgt.
- De simulatie meet hoe breed de verdelingen van de gemiddelde premie en van
  $\sigma(\log \mathrm{PD})$ zijn in steekproeven van honderd jaar, en of ze de modellen
  uit elkaar houden.
```

## Simulatie: honderd jaar, duizend keer, vier modellen

Houden steekproeven van honderd jaar de modellen uit elkaar? We simuleren elk model
duizend keer over honderd jaar en berekenen per steekproef, jaarlijks en reëel, dezelfde
momenten als in de data:

- het gemiddelde overrendement en de volatiliteit van het marktrendement,
- gemiddelde en volatiliteit van de reële rente,
- de gemiddelde prijs-dividendratio en de volatiliteit van de log-ratio,
- de $R^2$ van één- en vijfjaarsvoorspellingen met die ratio, zoals in
  [](#04-20-voorspelbaarheid),
- de autocorrelatie van jaarlijkse consumptiegroei.

De modellen zijn Campbell-Cochrane met de dividendclaim uit de theorie, Bansal-Yaron,
Barro met onafhankelijke rampen, en een variant in de geest van Gabaix. In die variant
wordt het dividend in een ramp met $F_t \in \{0{,}2;\ 0{,}9\}$ vermenigvuldigd. Het regime
blijft elk jaar met kans 0,9 bestaan en de dividendvolatiliteit is 11%. Die getallen kozen
we zelf voor een realistische rendementsvolatiliteit, zodat ook deze variant op een
ongemeten parameter leunt.

De eerste cel zet maandreeksen om in jaarcijfers en berekent de momenten, voor simulatie
en data op dezelfde manier.

```{code-cell} ipython3
def annualize(r, dc, dd, lpd, rf):
    """Monthly (T x N) log series -> annual real simple returns, log P/D at year end, annual consumption growth."""
    T, N = r.shape
    Y = T // 12
    by_year = lambda a: a[: Y * 12].reshape(Y, 12, N)
    cum_c = np.cumsum(dc, axis=0)
    cum_d = np.cumsum(dd, axis=0)
    cons = by_year(np.exp(cum_c - cum_c[0])).sum(axis=1)                # time-aggregated annual consumption
    divs = by_year(np.exp(cum_d - cum_d[0]))
    lpd_a = by_year(lpd)[:, -1, :] + np.log(divs[:, -1, :]) - np.log(divs.sum(axis=1))  # December price / annual dividends
    return dict(rm=np.expm1(by_year(r).sum(axis=1))[1:], rf=np.expm1(by_year(rf).sum(axis=1))[1:],
                lpd=lpd_a[1:], dc=np.diff(np.log(cons), axis=0))

def colcorr(a, b):
    """Column-wise correlation; zero where either column is constant."""
    a, b = a - a.mean(axis=0), b - b.mean(axis=0)
    denom = np.sqrt((a * a).sum(axis=0) * (b * b).sum(axis=0))
    return np.divide((a * b).sum(axis=0), denom, out=np.zeros(a.shape[1]), where=denom > 1e-14)

def sample_moments(rm, rf, lpd, dc):
    """Moments per simulated sample (columns) or for the data (one column)."""
    lex = np.log1p(rm) - np.log1p(rf)
    cum = np.vstack([np.zeros((1, lex.shape[1])), np.cumsum(lex, axis=0)])
    out = {"E[R^e]": (rm - rf).mean(axis=0), "sd(R)": rm.std(axis=0, ddof=1),
           "E[R^f]": rf.mean(axis=0), "sd(R^f)": rf.std(axis=0, ddof=1),
           "E[P/D]": np.exp(lpd).mean(axis=0), "sd(log P/D)": lpd.std(axis=0, ddof=1)}
    for h in (1, 5):
        future = cum[1 + h:] - cum[1:-h]                                # sum of log excess returns t+1..t+h
        out[f"R2 {h} jaar"] = colcorr(lpd[: len(future)], future) ** 2
    out["AC1(dc)"] = colcorr(dc[1:], dc[:-1])
    return out
```

Data en simulatie krijgen zo precies dezelfde bewerking, ook de optelling van
maandconsumptie tot jaarconsumptie. De volgende cel loopt maand voor maand door de modellen
van Campbell-Cochrane en Bansal-Yaron.

```{code-cell} ipython3
def cc_simulate(sol, n_years, n_paths, burn=50):
    """Simulate the monthly Campbell-Cochrane economy on the solved grid; returns annual series via annualize."""
    s = np.full(n_paths, sol["s_bar"])
    T = (n_years + burn + 1) * 12
    out = {k: np.empty((T, n_paths)) for k in ("r", "dc", "dd", "lpd")}
    pd_old = np.interp(s, sol["s"], sol["pd"])
    for t in range(T):
        v = sol["sm"] * rng.standard_normal(n_paths)
        eps = rng.standard_normal(n_paths)
        s = np.clip((1 - sol["phim"]) * sol["s_bar"] + sol["phim"] * s + sol["lam"](s) * v, sol["s"][0], sol["s_max"])
        pd_new = np.interp(s, sol["s"], sol["pd"])
        w = v if sol["swm"] == 0 else sol["rho_w"] * sol["swm"] / sol["sm"] * v + np.sqrt(1 - sol["rho_w"] ** 2) * sol["swm"] * eps
        out["dc"][t], out["dd"][t] = sol["gm"] + v, sol["gm"] + w
        out["r"][t] = np.log((1 + pd_new) / pd_old) + out["dd"][t]
        out["lpd"][t], pd_old = np.log(pd_new), pd_new
    keep = slice(burn * 12, None)
    return annualize(out["r"][keep], out["dc"][keep], out["dd"][keep], out["lpd"][keep],
                     np.full((T - burn * 12, n_paths), sol["rfm"]))

def by_simulate(sol, n_years, n_paths, burn=20):
    """Simulate the monthly Bansal-Yaron economy with the log-linear solution; returns annual series via annualize."""
    p = sol["p"]
    T = (n_years + burn + 1) * 12
    x, var = np.zeros(n_paths), np.full(n_paths, p["sig"] ** 2)
    zm = sol["A0m"] + sol["A1m"] * x + sol["A2m"] * var
    out = {k: np.empty((T, n_paths)) for k in ("r", "dc", "dd", "lpd", "rf")}
    for t in range(T):
        e, eta, u, w = rng.standard_normal((4, n_paths))
        sd = np.sqrt(var)
        out["rf"][t] = -(sol["m0"] + sol["mx"] * x + sol["ms"] * var) - 0.5 * (
            (p["gamma"] ** 2 + sol["lam_e"] ** 2) * var + sol["lam_w"] ** 2 * p["sig_w"] ** 2)
        out["dc"][t] = p["mu"] + x + sd * eta
        out["dd"][t] = p["mu_d"] + p["phi"] * x + p["phi_d"] * sd * u
        x = p["rho"] * x + p["phi_e"] * sd * e
        var = np.maximum(p["sig"] ** 2 + p["nu1"] * (var - p["sig"] ** 2) + p["sig_w"] * w, 1e-12)   # as in BY
        zm_new = sol["A0m"] + sol["A1m"] * x + sol["A2m"] * var
        out["r"][t] = sol["k0m"] + sol["k1m"] * zm_new - zm + out["dd"][t]
        out["lpd"][t], zm = zm_new, zm_new
    keep = slice(burn * 12, None)
    return annualize(*(out[k][keep] for k in ("r", "dc", "dd", "lpd", "rf")))
```

De rampeconomie simuleren we per jaar, met een rampgrootte op vier punten tussen 15% en
64% die de momenten van Barro reproduceert, inclusief zijn gemiddelde daling van 29%. De
cel drukt de kansen af en de exacte rente en ratio van die verdeling.

```{code-cell} ipython3
b_support = np.array([0.15, 0.30, 0.45, 0.64])          # Barro's range 15%-64%
b_moments = np.vstack([np.ones(4), b_support, (1 - b_support) ** -4.0, (1 - b_support) ** -3.0])
b_prob = np.linalg.solve(b_moments, [1.0, 0.29, 7.69, 4.05])
beta_d = np.exp(-rho_b)
EBg_d, EB1g_d = b_prob @ (1 - b_support) ** -gamma_b, b_prob @ (1 - b_support) ** (1 - gamma_b)
Rf_d = 1 / (beta_d * np.exp(-gamma_b * g_b + 0.5 * gamma_b**2 * sigma_b**2) * (1 - p_b + p_b * EBg_d))
k_d = beta_d * np.exp((1 - gamma_b) * g_b + 0.5 * (1 - gamma_b) ** 2 * sigma_b**2) * (1 - p_b + p_b * EB1g_d)
GABAIX = dict(F=np.array([0.2, 0.9]), P=np.array([[0.9, 0.1], [0.1, 0.9]]), sig_d=0.11)
print("kansen op b = 15/30/45/64%:", b_prob.round(4), f"| discreet exact: R^f = {Rf_d - 1:.4f}, P/D = {k_d / (1 - k_d):.2f}")

def disaster_simulate(n_years, n_paths, variant=None, burn=20):
    """Annual Barro economy; variant=GABAIX lets the dividend recovery F in a disaster follow a Markov regime."""
    T = n_years + burn
    u = sigma_b * rng.standard_normal((T, n_paths))
    hit = rng.random((T, n_paths)) < p_b
    b = b_support[rng.choice(4, size=(T, n_paths), p=b_prob)]
    dc = g_b + u + np.where(hit, np.log1p(-b), 0.0)
    if variant is None:
        pd_path = np.full((T, n_paths), k_d / (1 - k_d))
        r = dc + np.log((1 + pd_path) / pd_path)
    else:
        F, P = variant["F"], variant["P"]
        a = beta_d * np.exp((1 - gamma_b) * g_b + 0.5 * (1 - gamma_b) ** 2 * sigma_b**2) * (1 - p_b + p_b * EBg_d * F)
        pd_states = np.linalg.solve(np.eye(len(F)) - a[:, None] * P, (a[:, None] * P).sum(axis=1))
        regime = np.zeros((T + 1, n_paths), dtype=int)
        regime[0] = rng.integers(0, len(F), n_paths)
        draws = rng.random((T, n_paths))
        for t in range(T):
            regime[t + 1] = (draws[t][:, None] > np.cumsum(P, axis=1)[regime[t]]).sum(axis=1)
        eps = variant["sig_d"] * rng.standard_normal((T, n_paths)) - 0.5 * variant["sig_d"] ** 2
        dd = g_b + u + eps + np.where(hit, np.log(F[regime[:-1]]), 0.0)
        pd_path = pd_states[regime[1:]]
        r = dd + np.log((1 + pd_path) / pd_states[regime[:-1]])
    keep = slice(burn, None)
    return dict(rm=np.expm1(r[keep]), rf=np.full((n_years, n_paths), Rf_d - 1), lpd=np.log(pd_path[keep]), dc=dc[keep])
```

De kansen zijn positief, en de exacte rente van 1,6% en ratio van 19,65 wijken iets af van
de benadering in de theorie, omdat hier geen termen wegvallen. De volgende cel draait de
vier modellen elk duizend keer en geeft per moment de mediaan, met tussen haken het 2,5e
en het 97,5e percentiel.

```{code-cell} ipython3
N_YEARS, N_SAMPLES = 100, 1000
simulated = {
    "Campbell-Cochrane": sample_moments(**cc_simulate(cc_div, N_YEARS, N_SAMPLES)),
    "Bansal-Yaron": sample_moments(**by_simulate(by, N_YEARS, N_SAMPLES)),
    "Barro (iid)": sample_moments(**disaster_simulate(N_YEARS, N_SAMPLES)),
    "Barro-Gabaix (variabel)": sample_moments(**disaster_simulate(N_YEARS, N_SAMPLES, GABAIX)),
}
MOMENTS = list(simulated["Bansal-Yaron"])

def band(values):
    lo, med, hi = np.percentile(values, [2.5, 50, 97.5])
    return f"{med:.3f} [{lo:.3f}, {hi:.3f}]"

sim_table = pd.DataFrame({model: {k: band(v) for k, v in mom.items()} for model, mom in simulated.items()})
sim_table
```

De tabel laat vooral voor de gemiddelde premie brede banden zien. De figuur toont zes van
deze verdelingen als dozen, en het paneel linksboven, waar de dozen van de premie over
elkaar heen liggen, is het belangrijkste.

```{code-cell} ipython3
:label: cel-drie-antwoorden-banden
:tags: [hide-input]

SHOW = {"E[R^e]": "Gemiddeld overrendement", "sd(R)": "Volatiliteit van het rendement",
        "sd(log P/D)": "Volatiliteit van log P/D", "R2 5 jaar": "$R^2$ vijfjaarsvoorspelling",
        "E[R^f]": "Gemiddelde reële rente", "AC1(dc)": "Autocorrelatie consumptiegroei"}

def plot_bands(data=None):
    """Box plots of simulated 100-year sample moments per model; optional data values as vertical lines."""
    names = list(simulated)
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.5))
    for i, (ax, (key, title)) in enumerate(zip(axes.flat, SHOW.items())):
        ax.boxplot([simulated[name][key] for name in names], whis=(2.5, 97.5), showfliers=False,
                   orientation="horizontal", widths=0.6)
        ax.set_yticks(range(1, len(names) + 1))
        ax.set_yticklabels(names if i % 3 == 0 else [""] * len(names))
        if data is not None:
            ax.axvline(data[key], color=hap.plotting.COLORS[1], lw=1.6, label="VS 1930–2025")
        ax.set_title(title)
        ax.set_xlabel("waarde in een steekproef van 100 jaar")
        ax.set_ylabel("model" if i % 3 == 0 else "")
    if data is not None:
        axes[0, 0].legend(loc="lower right")
    plt.tight_layout()
    plt.show()

plot_bands()
```

:::{figure} #cel-drie-antwoorden-banden
:label: fig-drie-antwoorden-banden
:width: 100%

Verdeling van zes momenten over duizend gesimuleerde steekproeven van honderd jaar
(doos: 25e–75e percentiel, snorharen: 2,5e–97,5e percentiel). De gemiddelde premie van de
vier modellen overlapt breed, en de scheiding zit in momenten die de modellen verschillend
voorspellen maar die in de data slecht meetbaar zijn.
:::

Uit tabel en figuur volgen drie conclusies, in volgorde van belang.

- **De premie scheidt niets.** De medianen liggen tussen 5,3 en 5,8%, en de 95%-banden van
  de drie modellen met een realistische volatiliteit zijn vijf tot zeven procentpunt
  breed. Alleen Barro met onafhankelijke rampen heeft een smalle band, omdat zijn dividend
  gelijk is aan consumptie en het rendement daardoor maar rond 4% per jaar schommelt. Bij
  een rendementsvolatiliteit van 16 tot 19% heeft een honderdjarig gemiddelde
  een standaardfout van 1,6 tot 1,9 procentpunt, meer dan de verschillen tussen de
  modellen. Zo ziet de standaardfout van 2% er hier uit.
- **Tweede momenten scheiden op kenmerken die in de bouw zitten.** De rente is constant
  behalve in Bansal-Yaron. Consumptiegroei is in de maandmodellen autogecorreleerd,
  ongeveer 0,25 door tijdsaggregatie en 0,5 in Bansal-Yaron, tegen rond nul in de
  jaarlijkse rampenmodellen. Barro met onafhankelijke rampen heeft een
  prijs-dividendratio die niet beweegt.
- **Voorspelbaarheid scheidt zwak.** De band van de vijfjaars-$R^2$ begint bij nul en loopt
  tot 0,18 bij Bansal-Yaron en tot 0,36 en 0,43 bij de andere twee. De medianen
  verschillen wel, 0,02 tegen 0,11 en 0,09, omdat de ratio in Bansal-Yaron vooral door
  verwachte dividendgroei beweegt. Toch verwerpt een $R^2$ van 0,1 in honderd jaar data
  geen van de drie.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** Campbell en Cochrane {cite}`CampbellCochrane1999` in de numerieke uitwerking van Wachter {cite}`Wachter2005`, en Bansal en Yaron {cite}`BansalYaron2004` in die van Beeler en Campbell {cite}`BeelerCampbell2012`. Barro {cite}`Barro2006` volgen we in zijn samenvatting van 2009 {cite}`Barro2009`.

**Wat.** (1) Wachter (2005), tabel 2, de consumptieclaim van Campbell-Cochrane, en (2)
Beeler en Campbell (2012), tabel II, de populatiemomenten van Bansal-Yaron; tabel 3 van
Barro staat al in de theorie. (3) Waar liggen de Amerikaanse data in de simulatiebanden?

**Data hier.** Voor (1) en (2) simuleren we met de parameters uit de bronnen. Voor (3) gebruiken we jaardata 1930–2025 uit `hap.data.goyal_welch` en reële consumptie per hoofd uit
`hap.data.fred`.

**Verschil met het origineel.** Wij delen de decemberprijs door de dividenden van het hele
jaar, terwijl Beeler en Campbell de maandratio gebruiken. De vergelijking met Wachter
doen we op de consumptieclaim, zodat onze eigen dividendclaim niet meespeelt.

**Verwachte afwijking.** (1) Een premie tussen 3,5 en 4,5% en een volatiliteit onder 10%;
(2) $\E[p-d]$, $\E[r^f]$, $\sigma(r^f)$, $\sigma(\Delta c)$ en $\mathrm{AC1}(\Delta c)$
binnen 0,05 van tabel II. (3) De premie van de data ligt binnen de 95%-band van de drie
modellen met een realistische rendementsvolatiliteit en $\sigma(\log \mathrm{PD})$ boven alle banden. Valt de premie buiten alle
banden of $\sigma(\log \mathrm{PD})$ erbinnen, dan zit er een fout in de code.
```

### Campbell-Cochrane en Bansal-Yaron naast hun bronnen

De cel simuleert beide modellen over 2000 jaar maal 50 paden en zet de momenten naast de
gepubliceerde waarden.

```{code-cell} ipython3
pop_cc = cc_simulate(cc_cons, 2000, 50)
lex_cc = np.log1p(pop_cc["rm"]) - np.log1p(pop_cc["rf"])
pop_by = by_simulate(by, 2000, 50)
z_month = by["A0m"] + by["A1m"] * 0 + by["A2m"] * BY["sig"] ** 2
sd_z = np.sqrt(by["A1m"] ** 2 * (BY["phi_e"] * BY["sig"]) ** 2 / (1 - BY["rho"] ** 2)
               + by["A2m"] ** 2 * BY["sig_w"] ** 2 / (1 - BY["nu1"] ** 2))

replication = pd.DataFrame(
    {
        "hier": [100 * (pop_cc["rm"] - pop_cc["rf"]).mean(), 100 * (pop_cc["rm"] - pop_cc["rf"]).std(),
                 np.exp(pop_cc["lpd"].mean()), pop_cc["lpd"].std(),
                 100 * np.log1p(pop_by["rm"]).mean(), 100 * np.log1p(pop_by["rm"]).std(),
                 100 * np.log1p(pop_by["rf"]).mean(), 100 * np.log1p(pop_by["rf"]).std(),
                 z_month - np.log(12), sd_z, 100 * pop_by["dc"].std(),
                 sample_moments(**pop_by)["AC1(dc)"].mean()],
        "bron": [3.90, 8.25, 34.52, 0.13, 6.62, 16.88, 2.56, 1.30, 3.00, 0.16, 2.92, 0.51],
    },
    index=pd.MultiIndex.from_tuples(
        [("CC consumptieclaim (Wachter 2005, tabel 2)", m) for m in ("E[R^e] %", "sd(R^e) %", "exp E[p-d]", "sd(p-d)")]
        + [("BY (Beeler-Campbell 2012, tabel II)", m) for m in
           ("E[r] %", "sd(r) %", "E[r^f] %", "sd(r^f) %", "E[p-d]", "sd(p-d), maandratio", "sd(dc) %", "AC1(dc)")]),
)
replication.round(3)
```

**Geslaagd.** De consumptieclaim van Campbell-Cochrane geeft een premie van 4,20% met een
volatiliteit van 8,40%, binnen de verwachte band en dicht bij Wachters fijnste rooster.
Dat we drie tiende procentpunt boven dat rooster uitkomen, valt binnen wat een
roosterkeuze doet, want oefening 3 laat zien dat de ondergrens van het rooster de premie
met meer dan een procentpunt verschuift. Voor Bansal-Yaron liggen de vijf beloofde
momenten binnen 0,05 van tabel II. Alleen het gemiddelde log rendement ligt met 6,76%
iets boven hun 6,62%, wat we toeschrijven aan het optellen van gelineariseerde
maandrendementen.

### De Amerikaanse data in de banden

De volgende cel bouwt de reële jaarreeksen en plaatst elk datamoment in de verdeling van
elk model, zodat de modelkolommen percentielen zijn.

```{code-cell} ipython3
def fred_annual(code):
    series = hap_data.fred(code)[code]
    series.index = series.index.year
    return series

real_cons = (fred_annual("PCNDA") / fred_annual("DNDGRG3A086NBEA")
             + fred_annual("PCESVA") / fred_annual("DSERRG3A086NBEA")) / fred_annual("B230RC0A052NBEA")
gw = hap_data.goyal_welch("annual")
gw.index = gw.index.year
data_real = pd.DataFrame(
    {
        "rm": (1 + gw["CRSP_SPvw"]) / (1 + gw["infl"]) - 1,
        "rf": (1 + gw["Rfree"]) / (1 + gw["infl"]) - 1,
        "lpd": np.log(gw["Index"] / gw["D12"]),
        "dc": np.log(real_cons).diff(),
    }
).loc[1930:2025].dropna()
data_moments = {k: float(v[0]) for k, v in sample_moments(*(data_real[c].to_numpy()[:, None]
                                                              for c in ("rm", "rf", "lpd", "dc"))).items()}
T_data = len(data_real)
se_premium = (data_real["rm"] - data_real["rf"]).std() / np.sqrt(T_data)
print(f"{data_real.index[0]}-{data_real.index[-1]}, {T_data} jaar; SE van het gemiddelde overrendement = {se_premium:.3f}")

placement = pd.DataFrame(
    {model: {k: np.mean(mom[k] <= data_moments[k]) for k in MOMENTS} for model, mom in simulated.items()}
)
placement.insert(0, "data 1930-2025", pd.Series(data_moments))
placement.round(3)
```

Het gemiddelde overrendement over 1930–2025 is 8,3% met een standaardfout van 2,0
procentpunt. De figuur legt de datawaarden als verticale lijn over de banden, en het gaat
vooral om de panelen van de premie en van de volatiliteit van log P/D.

```{code-cell} ipython3
:label: cel-drie-antwoorden-data
:tags: [hide-input]

plot_bands(data_moments)
```

:::{figure} #cel-drie-antwoorden-data
:label: fig-drie-antwoorden-data
:width: 100%

De simulatiebanden uit [](#fig-drie-antwoorden-banden) met de Amerikaanse jaardata
1930–2025 als verticale lijn. De gemiddelde premie ligt aan de bovenkant en alleen binnen
de band van Bansal-Yaron, terwijl de volatiliteit van de prijs-dividendratio ver buiten
alle banden ligt.
:::

**Gedeeltelijk geslaagd.** De volatiliteit van de prijs-dividendratio ligt zoals verwacht
boven alle banden, maar de premie ligt binnen de band van één model in plaats van drie.
Dat de premie maar in één band valt, komt door een hoge Amerikaanse premie en niet door
een codefout, want de modellen reproduceren hun bronnen. De percentielen staan in de
tabel, en per moment ziet het beeld er zo uit.

- **Premie.** Het gemiddelde overrendement valt binnen de band van Bansal-Yaron en net
  boven die van Campbell-Cochrane en de Gabaix-variant. Twee standaardfouten rond 8,3%
  bevatten de mediaan van elk model, zodat de onzekerheid in twee richtingen werkt. Voor
  Barro is een hoog Amerikaans gemiddelde zelfs een voorspelling, want zonder ramp ligt het
  gerealiseerde rendement boven de ware premie, in het toy-voorbeeld 5,67 tegen 4,92
  procentpunt.
- **Prijs-dividendratio.** De volatiliteit van de log-ratio is in de data 0,51, ver boven
  de band van elk model, die hoogstens tot 0,24 loopt. De modellen verklaren dus dat de
  ratio beweegt, maar geen van de drie hoeveel, en oefening 4 laat zien dat dat ook tot
  1998 geldt.
- **Voorspelbaarheid en volatiliteit.** De vijfjaars-$R^2$ ligt midden in de banden van
  Campbell-Cochrane en de Gabaix-variant en aan de bovenkant van die van Bansal-Yaron, en
  de rendementsvolatiliteit valt binnen de banden van Bansal-Yaron en de Gabaix-variant. Op
  deze momenten zijn de modellen observationeel equivalent in de zin van
  [](#prf-drie-antwoorden-equivalentie).
- **Consumptie.** De autocorrelatie van consumptiegroei ligt aan de onderkant van de band
  van Bansal-Yaron en aan de bovenkant van die van Campbell-Cochrane, zodat beide modellen
  die waarde toelaten. De jaarlijks gesimuleerde rampenmodellen missen de tijdsaggregatie
  die al ongeveer 0,25 oplevert, en oefening 4 laat zien hoe sterk dit moment van de
  steekproef afhangt.

## Wat er brak, en wat daarna kwam

**Wat de modellen verklaren.** Twintig jaar na Mehra en Prescott lieten drie modellen zien
dat een consumptie-SDF een premie van ruim 5% kan dragen. Ze combineerden die met een
rendementsvolatiliteit van 16 tot 19%, een lage rente en een prijs-dividendratio die
rendementen voorspelt. De
puzzel verschoof daarmee van onmogelijk met redelijke voorkeuren naar mogelijk met één
extra parameter.

**Waar het breekt.** Geen van de drie haalt de volatiliteit van de log prijs-dividendratio,
die in de data 0,51 is, tegen hoogstens 0,24 in de modellen. Omgekeerd halen ze de
momenten die ze wel halen allemaal tegelijk, zodat honderd jaar data ze niet scheiden. De
parameters die dat wel zouden doen ($\phi$, $\rho$, $p$) zijn met dezelfde data niet te
meten. Zelfs één model is kwetsbaar, want dezelfde kalibratie van
Campbell-Cochrane geeft 6,6% of 3,9% premie, afhankelijk van het rooster
{cite}`Wachter2005`.

**Risico of vergissing?** In de Chicago-lezing zeggen de drie modellen hetzelfde, elk via
een ander mechanisme. De premie is dan een beloning voor risico dat een prijs heeft, en wie
in een crisis aandelen koopt, verkoopt verzekering aan beleggers die er op dat moment het
hardst behoefte aan hebben. In de Yale-lezing voegt een model met een niet te controleren
parameter niets toe, want een gedragsmodel met extrapolerende of angstige beleggers
verklaart dezelfde feiten. Het deel van de prijsbeweging dat geen van de drie verklaart,
is dan de vergissing. De data die de lezingen zouden scheiden, bestaan wel maar zijn
schaars: prijzen van verzekering tegen de staart en directe metingen van wat beleggers
verwachten.

**Wat er daarna kwam.** De aandelenpremie is sindsdien een feit met concurrerende
theorieën. De volgende stap zocht de scheiding in activa waarvan de looptijd vastligt, in
de termijnstructuur van rentes en de risicopremies op obligaties, in
[](#05-28-termijnstructuur-premies).

## Oefeningen

:::{exercise}
:label: ex-drie-antwoorden-1

**Instap: een kleinere rampkans.** Neem het toy-voorbeeld, maar met $p = 0{,}01$ in plaats van 0,017. Alle andere getallen blijven gelijk.

1. Bereken met de hand $\E[m]$, $R^f$, $k$, de prijs-dividendratio en de premie.
2. In welke richting bewegen rente en premie als $p$ stijgt, en waarom?
:::

:::{solution} ex-drie-antwoorden-1
:class: dropdown

**(1)** Nu is $\E[m] = 0{,}99 \times 0{,}878770 + 0{,}01 \times 7{,}484568 = 0{,}944828$, dus
$1 + R^f = 1{,}05839$. Verder is
$k = 0{,}97\,(0{,}99 \times 0{,}928599 + 0{,}01 \times 4{,}629630) = 0{,}936641$, wat een
prijs-dividendratio van 14,78 geeft, en $\E[g]/k = 1{,}020750/0{,}936641 = 1{,}08980$,
zodat de premie $8{,}980 - 5{,}839 = 3{,}14$ procentpunt is.

```{code-cell} ipython3
pd.Series(rietz_toy(0.01)).round(5)
```

**(2)** Een grotere rampkans verlaagt de rente en verhoogt de premie. Beleggers willen zich
sterker verzekeren, zodat ze meer betalen voor de obligatie en een hogere vergoeding
vragen voor het aandeel, dat in de ramp instort. Beide getallen reageren dus sterk op een
kans die in één land nauwelijks te meten is.
:::

:::{exercise}
:label: ex-drie-antwoorden-2

**Wanneer telt de EIS voor de premie?** Neem Epstein-Zin-voorkeuren. De vraag is of de EIS alleen de rente verschuift of ook de premie.

1. Laat voor een onafhankelijke lognormale economie zien dat
   $\log m_{t+1} = c - \gamma\,\Delta c_{t+1}$, bepaal $\kappa$ uit $\E[m R_w] = 1$, en leid
   de formules voor $\log(1 + R^f)$ en $\log(\E[R_w]/(1 + R^f))$ uit de theorie af.
2. Bereken met `ez_iid` en de jaarversie van de Bansal-Yaron-kalibratie ($\beta^{12}$,
   $12\mu$, $\sqrt{12}\,\bar\sigma$, $\gamma = 10$) de rente en premie bij onafhankelijke
   groei voor $\psi$ gelijk aan 1,25, 1,5 en 2.
3. Bereken met `by_solve` voor dezelfde $\psi$ de premie via het langetermijnkanaal uit
   [](#eq-drie-antwoorden-by-premie). Waarom hangt de premie hier wél van $\psi$ af?
:::

:::{solution} ex-drie-antwoorden-2
:class: dropdown

**(1)** Met $r_w = \Delta c + \kappa$ is
$\log m = \theta\log\beta + (\theta-1)\kappa + (-\theta/\psi + \theta - 1)\Delta c$, met
coëfficiënt $\theta(1-1/\psi) - 1 = -\gamma$. De Euler-vergelijking
$\E[e^{\log m + r_w}] = 1$ geeft
$\theta\log\beta + \theta\kappa + (1-\gamma)\mu + \tfrac12(1-\gamma)^2\sigma^2 = 0$, dus
$\kappa = -\log\beta - [(1-\gamma)\mu + \tfrac12(1-\gamma)^2\sigma^2]/\theta$. De constante
in $\log m$ is dan $c = \log\beta - (1/\psi - \gamma)[\mu + \tfrac12(1-\gamma)\sigma^2]$, en
$\log(1 + R^f) = -c + \gamma\mu - \tfrac12\gamma^2\sigma^2$ werkt uit tot de formule in de tekst.
Voor de premie geldt $\log\E[R_w] - \log(1 + R^f) = -\Cov(\log m, r_w) = \gamma\sigma^2$.

**(2) en (3)**

```{code-cell} ipython3
psi_rows = {}
for psi in (1.25, 1.5, 2.0):
    sol_psi = by_solve({**BY, "psi": psi})
    log_rf_iid, prem_iid = ez_iid(BY["beta"] ** 12, 12 * BY["mu"], np.sqrt(12) * BY["sig"], BY["gamma"], psi)
    psi_rows[psi] = {
        "iid: log(1+R^f)": log_rf_iid,
        "iid: log premie": prem_iid,
        "BY: A_1,m": sol_psi["A1m"],
        "BY: premie via x_t (%/jaar)": 1200 * sol_psi["lam_e"] * sol_psi["k1m"] * sol_psi["A1m"] * BY["phi_e"] * BY["sig"] ** 2,
    }
pd.DataFrame(psi_rows).T.rename_axis("psi").round(4)
```

Bij onafhankelijke groei verschuift $\psi$ alleen de rente, en de premie is voor elke
$\psi$ gelijk aan $\gamma\sigma^2 = 0{,}73\%$. In Bansal-Yaron bepaalt $\psi$ via $A_{1,m}$ hoe sterk de prijs op nieuws over $x_t$ reageert. Via $\theta$ en $A_1$ bepaalt $\psi$ hoe zwaar dat
nieuws in de SDF weegt, zodat een hogere EIS beide vergroot. De ontkoppeling van Epstein
en Zin lost dus de rentepuzzel op, maar de premie komt pas als de toekomst voorspelbaar
is, en daarmee hangt het model af van $\rho$.
:::

:::{exercise}
:label: ex-drie-antwoorden-3

**Het rooster als donkere materie.** Wachter {cite}`Wachter2005` liet zien dat de getallen
van Campbell en Cochrane van het rooster afhangen. Los de consumptieclaim op met roosters
tot $\bar s - 8$, $\bar s - 20$ en $\bar s - 80$, en met een grof rooster van dertig punten
tot $\bar s - 8$. Simuleer telkens 2000 jaar maal 50 paden en zet premie, volatiliteit,
$\exp\E[p-d]$ en $\sigma(p-d)$ naast Wachters fijnste en grofste rooster.
:::

:::{solution} ex-drie-antwoorden-3
:class: dropdown

De cel lost de consumptieclaim op vier roosters op en zet Wachters twee roosters eronder.

```{code-cell} ipython3
grid_variants = {
    "tot s-bar - 8": dict(lower=8.0),
    "tot s-bar - 20": dict(lower=20.0),
    "tot s-bar - 80 (hoofdtekst)": dict(lower=80.0),
    "grof: 30 punten tot s-bar - 8": dict(lower=8.0, n_low=10, n_high=20),
}
grid_rows = {}
for label, kw in grid_variants.items():
    sim = cc_simulate(cc_solve(**{**CC, "sig_w": 0.0, "rho_w": 0.0}, **kw), 2000, 50)
    excess = sim["rm"] - sim["rf"]
    grid_rows[label] = {"E[R^e] %": 100 * excess.mean(), "sd(R^e) %": 100 * excess.std(),
                        "exp E[p-d]": np.exp(sim["lpd"].mean()), "sd(p-d)": sim["lpd"].std()}
grid_rows["Wachter (2005), fijnste rooster"] = {"E[R^e] %": 3.90, "sd(R^e) %": 8.25, "exp E[p-d]": 34.52, "sd(p-d)": 0.13}
grid_rows["Wachter (2005), grofste rooster"] = {"E[R^e] %": 6.59, "sd(R^e) %": 15.05, "exp E[p-d]": 18.62, "sd(p-d)": 0.27}
pd.DataFrame(grid_rows).T.round(3)
```

Hoe verder het rooster naar lage waarden van het surplus doorloopt, hoe hoger de premie (2,8%, 3,6% en 4,2%) en de volatiliteit. Een rooster dat afkapt, knipt juist de
slechtste toestanden weg die in dit model de premie dragen. Het aantal punten doet er minder toe dan de ondergrens. Wachters grofste rooster gaf met 6,6% zelfs een hogere
premie, wat erop wijst dat haar roosters de staart anders behandelden dan de onze. Als de premie uit
zeldzame, extreme toestanden komt, is ook de numerieke oplossing een parameter die niemand
in de data kan controleren.
:::

:::{exercise}
:label: ex-drie-antwoorden-4

**Andere steekproeven.** Herhaal de plaatsing van de data in de simulatiebanden voor
1947–2025 en voor 1930–1998, het einde van de steekproef van Bansal en Yaron, met
simulaties van dezelfde lengte. Doe dat voor het gemiddelde overrendement,
$\sigma(\log \mathrm{PD})$, de vijfjaars-$R^2$ en de autocorrelatie van consumptiegroei.
Welke conclusies uit de hoofdtekst veranderen?
:::

:::{solution} ex-drie-antwoorden-4
:class: dropdown

De functie herhaalt de plaatsing voor een deelsteekproef, met simulaties van dezelfde lengte.

```{code-cell} ipython3
def placement_for(first, last, n_samples=300):
    """Data moments for first..last and their percentile in simulations of the same length."""
    sub = data_real.loc[first:last]
    T = len(sub)
    data_m = {k: float(v[0]) for k, v in sample_moments(*(sub[c].to_numpy()[:, None]
                                                         for c in ("rm", "rf", "lpd", "dc"))).items()}
    sims = {"Campbell-Cochrane": sample_moments(**cc_simulate(cc_div, T, n_samples)),
            "Bansal-Yaron": sample_moments(**by_simulate(by, T, n_samples)),
            "Barro-Gabaix (variabel)": sample_moments(**disaster_simulate(T, n_samples, GABAIX))}
    keys = ["E[R^e]", "sd(log P/D)", "R2 5 jaar", "AC1(dc)"]
    rows = {"data": {k: data_m[k] for k in keys}}
    rows.update({name: {k: np.mean(mom[k] <= data_m[k]) for k in keys} for name, mom in sims.items()})
    return pd.DataFrame(rows)

pd.concat({"1947-2025": placement_for(1947, 2025), "1930-1998": placement_for(1930, 1998)},
          names=["steekproef", "moment"]).round(3)
```

De volatiliteit van log PD ligt in beide steekproeven boven alle banden (0,47 en 0,37). De premie ligt naoorlogs alleen binnen de band van Bansal-Yaron, terwijl ze tot 1998
ook net binnen die van de Gabaix-variant valt.

De consumptieconclusie draait wel om. Naoorlogs is de autocorrelatie van consumptiegroei
0,17, op het 0,3e percentiel van Bansal-Yaron, zodat het model op deze steekproef wordt
verworpen. Tot 1998 is ze 0,49, op de mediaan van Bansal-Yaron en boven de band van
Campbell-Cochrane. Het moment dat de modellen het scherpst scheidt, hangt dus af van een handvol jaren uit de Depressie, zoals Beeler en Campbell al zagen. Daarom blijven de
modellen op de volledige steekproef observationeel equivalent.
:::
