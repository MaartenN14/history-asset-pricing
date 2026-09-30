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

(07-37-llms-en-efficientie)=

# LLM's, advies en efficiëntie

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 2022–2026, van de lancering van ChatGPT op 30 november 2022 tot de terugblik
van Santa-Clara.

**Wat we al weten.** [Het vorige college](#06-36-inelastische-markten) maakte aannemelijk
dat geldstromen die op een inelastische vraag stuiten, het niveau van de aandelenmarkt sterk
bewegen. Het eindigde met de vraag wie prijzen dan nog informatief maakt. Het klassieke antwoord is
de belegger die voor informatie betaalt. Al in
[het college over efficiënte markten](#02-06-efficiente-markten) bleek echter dat een prijs
niet alle informatie kan bevatten als informatie geld kost.

**Welke vraag staat open.** Wat gebeurt er met beleggingsadvies en met de efficiëntie van
prijzen als het lezen en interpreteren van informatie bijna niets meer kost?
```

## Overzicht

Santa-Clara sluit zijn geschiedenis af met twee vragen over het taalmodel
{cite}`SantaClara2026`. Krijgen particulieren beter advies nu een machine het werk van een
adviseur bijna gratis doet, en worden markten efficiënter nu machines elke jaarrekening in
seconden lezen? Hij verwacht een betere mediaan met een slechtere staart voor advies, en
efficiëntere relatieve prijzen bij een marktniveau dat niet efficiënter wordt. Dat brengt
hij zelf als verwachting, niet als bevinding.

In dit college:

- leiden we met {cite:t}`GrossmanStiglitz1980` af hoeveel beleggers zich laten informeren
  als informatie goedkoper wordt, en waarom de prijs toch nooit volledig informatief wordt
- laten we zien dat fouten die veel beleggers delen niet wegmiddelen, zodat relatieve
  prijzen wel en het marktniveau niet efficiënter worden
- rekenen we uit wat spreiding en weinig handelen een particulier over dertig jaar
  opleveren, en zetten we dat naast het werk over robo-advies en Robinhood
- simuleren we wat één jaar data laat zien van goedkopere informatie en van een gedeeld
  model
- repliceren we een event study rond de lancering van ChatGPT
  {cite}`EisfeldtSchubertZhang2023`, het ene moment waarop de kosten van informatie in één
  keer daalden, en meten we hoe snel prijzen sinds 1930 nieuws verwerken

In 1980 lieten Grossman en Stiglitz zien dat een volledig efficiënte markt onmogelijk is
als informatie geld kost, want dan betaalt niemand meer om informatie te verzamelen. De
kosten van informatie daalden daarna geleidelijk, met elektronische jaarverslagen en
internet, en met ChatGPT eind 2022 in één sprong. Sindsdien volgde empirisch werk over
ChatGPT als nieuwslezer
{cite}`LopezLiraTang2023`
en over bedrijven die voor machines schrijven {cite}`CaoJiangYangZhang2023`.

Tot nu toe toetsten we theorieën aan feiten of zochten we een verklaring bij een feit
(theorie of feit). Hier staat alleen de stelling van Grossman en Stiglitz vast, en is
gemeten dat prijzen nieuws sneller verwerken. Wat taalmodellen met advies en crashes doen,
is nog een vermoeden
waarvoor de feiten ontbreken.

## Intuïtie: waarom zou dit waar zijn?

Het standaardadvies van het vak past op een bierviltje: spreid, houd de kosten laag,
handel weinig en verkoop niet in paniek. Het ontbrak nooit aan kennis, maar aan iemand die
het advies herhaalt op het moment dat de klant in de verleiding komt. Zo'n adviseur kost
een vaste vergoeding, en die is voor een klein vermogen te hoog. Volgens Santa-Clara kost
zulk advies, waarvoor vroeger een mens nodig was, per extra klant nu vrijwel niets meer
{cite}`SantaClara2026`. Omdat
de mediane particulier te weinig spreidt en te veel handelt
([](#04-23-behavioral)), helpt zelfs een middelmatige digitale adviseur. Een app die een
klant kan afremmen, kan hem echter ook tot handel aanzetten, en een platform dat per
transactie
verdient, heeft daar belang bij.

Informatie komt in prijzen doordat beleggers ervoor betalen en dat terugverdienen met hun
handel. Als lezen goedkoper wordt, doen meer beleggers het, en dan bevat de prijs meer
informatie. Toch merkt het marktniveau daar om twee redenen weinig van. Ten eerste lijken
machines op elkaar. Tien analisten met elk hun eigen fouten middelen die fouten weg, maar
tien algoritmen die op dezelfde data zijn getraind, maken dezelfde fout tegelijk. Ten
tweede kan een arbitrageur een relatieve fout verhandelen door het goedkope aandeel te kopen
en het dure te verkopen, terwijl tegenover een gok op het marktniveau geen hedge staat.

We verwachten daarom dat goedkopere informatie het aandeel geïnformeerde beleggers doet
stijgen en de prijs informatiever maakt, maar niet volledig informatief. Een fout die veel
beleggers delen, blijft in het gemiddelde staan, hoeveel beleggers er ook meedoen. Van
goedkoop advies verwachten we dat de mediane particulier erop vooruitgaat, terwijl de
slechtste
uitkomsten slechter kunnen worden.

## Toy-voorbeeld: meer geïnformeerden als informatie goedkoper wordt

We laden eerst de pakketten en leggen het toeval vast, zodat elke uitvoering dezelfde
getallen geeft.

```{code-cell} ipython3
import itertools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

Een risicovol activum betaalt $x = s + \varepsilon$, de som van een signaal $s$ en ruis
$\varepsilon$. Een fractie $\lambda$ van de beleggers betaalt $c$ en ziet het signaal,
terwijl de rest alleen de prijs ziet. Omdat het aanbod van het activum ruist, verraadt de
prijs het signaal maar gedeeltelijk. We willen weten hoe groot $\lambda$ wordt als
informatie goedkoper wordt, bij deze getallen:

| grootheid | symbool | waarde |
|---|---|---|
| absolute risicoaversie | $a$ | 2 |
| variantie van het signaal | $\sigma^2_s$ | 1 |
| variantie van de ruis in de payoff | $\sigma^2_\varepsilon$ | 1 |
| variantie van het aanbod | $\sigma^2_z$ | 0,04 |
| informatiekosten, duur of goedkoop | $c$ | $\ln(1{,}5)/4 \approx 0{,}101$ of $\ln(1{,}2)/4 \approx 0{,}046$ |

De theorie hieronder leidt het volgende recept af.

$$
\lambda^* = \sqrt{\nu(1-k)/k}, \qquad
\nu = \frac{a^2 \sigma^4_\varepsilon \sigma^2_z}{\sigma^2_s}, \qquad
k = \frac{\sigma^2_\varepsilon}{\sigma^2_s}\left(e^{2ac} - 1\right),
$$

Hierin meet $\nu$ de aanbodruis ten opzichte van het signaal. De factor $e^{2ac}$ is in
evenwicht de restvariantie van een ongeïnformeerde gedeeld door die van een geïnformeerde,
en $k$ zet de kosten $c$ zo om naar de schaal van de varianties. Bij dit aandeel
geïnformeerden is het kwadraat van de
correlatie tussen signaal en prijs, de informativiteit, gelijk aan $\rho^2 = 1 - k$. Met
de hand gaat de berekening in vijf stappen.

1. De ruisparameter is $\nu = 2^2 \times 1 \times 0{,}04 / 1 = 0{,}16$.
2. Bij dure informatie is $e^{2ac} = e^{\ln 1{,}5} = 1{,}5$, dus $k = 0{,}5$.
3. Dan is $\lambda^* = \sqrt{0{,}16 \times 0{,}5 / 0{,}5} = 0{,}4$ en $\rho^2 = 0{,}5$.
4. Bij goedkope informatie is $e^{2ac} = 1{,}2$, dus $k = 0{,}2$.
5. Dan is $\lambda^* = \sqrt{0{,}16 \times 0{,}8 / 0{,}2} = \sqrt{0{,}64} = 0{,}8$ en
   $\rho^2 = 0{,}8$.

De codecel lost hetzelfde evenwicht op met een functie die we in de simulatie opnieuw
gebruiken, en zet de uitkomst naast de handberekening.

```{code-cell} ipython3
def gs_equilibrium(c, a, var_s, var_e, var_z):
    """Grossman-Stiglitz (1980) CARA-normal equilibrium.

    Returns the fraction of informed traders lam, price informativeness
    rho2 = Corr^2(s, p) and the gross certainty-equivalent value of the signal.
    """
    nu = a**2 * var_e**2 * var_z / var_s
    k = var_e / var_s * np.expm1(2 * a * c)
    if k >= 1:
        lam = 0.0
    elif k <= 0:
        lam = 1.0
    else:
        lam = min(1.0, np.sqrt(nu * (1 - k) / k))
    rho2 = lam**2 / (lam**2 + nu)
    value = np.log1p(var_s * (1 - rho2) / var_e) / (2 * a)
    return lam, rho2, value


a, var_s, var_e, var_z = 2.0, 1.0, 1.0, 0.04
cases = {"dure informatie": (np.log(1.5) / 4, 0.4, 0.5),
         "goedkope informatie": (np.log(1.2) / 4, 0.8, 0.8)}
rows = {}
for case, (c, lam_hand, rho2_hand) in cases.items():
    lam, rho2, value = gs_equilibrium(c, a, var_s, var_e, var_z)
    rows[case] = {"c": c,
                  "lambda met de hand": lam_hand, "lambda code": lam,
                  "rho2 met de hand": rho2_hand, "rho2 code": rho2,
                  "waarde signaal (code)": value}
toy_gs = pd.DataFrame(rows).T

assert np.allclose(toy_gs["lambda code"], toy_gs["lambda met de hand"])
assert np.allclose(toy_gs["rho2 code"], toy_gs["rho2 met de hand"])
assert np.allclose(toy_gs["waarde signaal (code)"], toy_gs["c"])
toy_gs.round(4)
```

Code en hand komen overeen, en de laatste kolom laat zien dat het signaal in beide
evenwichten precies zijn kosten waard is. Informatie die ruim de helft goedkoper wordt,
verdubbelt dus het aandeel geïnformeerde beleggers. De prijs verklaart dan 80% van de
variantie van het signaal in plaats van 50%, maar geen van beide evenwichten komt bij
100%.

## Theorie

De theorie gaat in drie stappen van het toy-voorbeeld naar de tweedeling van Santa-Clara.
Eerst leiden we het evenwicht van Grossman en Stiglitz af. Goedkopere informatie maakt de
prijs daarin informatiever, tot een grens die door risicoaversie wordt gezet en niet door
kosten. Daarna laten we zien dat gedeelde modelfouten niet wegmiddelen, zodat
relatieve prijzen wel en het marktniveau niet efficiënter worden. Tot slot meten we
snelheid met de halfwaardetijd van informatie en rekenen we uit wat advies een particulier
oplevert.

### Opzet en aannames

We volgen {cite:t}`GrossmanStiglitz1980`, maar schrijven $s$ voor het signaal en $z$ voor
het aanbod, waar zij $\theta$ en $x$ gebruiken. Het model rust op vier aannames.

1. Er is één periode, een risicovrij activum met rente nul en een risicovol activum met
   payoff $x = s + \varepsilon$, met $s \sim \mathcal{N}(\mu_s, \sigma^2_s)$ en
   $\varepsilon \sim \mathcal{N}(0, \sigma^2_\varepsilon)$ onafhankelijk.
2. Alle beleggers hebben nut $u(W) = -e^{-aW}$ met absolute risicoaversie $a$ (CARA).
3. Het aanbod per belegger is $z \sim \mathcal{N}(\bar z, \sigma^2_z)$, onafhankelijk van
   $s$ en $\varepsilon$, bijvoorbeeld aandelen die liquiditeitshandelaren (*noise traders*)
   om persoonlijke redenen verkopen.
4. Een fractie $\lambda$ betaalt $c$ en ziet $s$, de rest ziet alleen de prijs $p$.

Zonder de ruis van aanname 3 zou de prijs het signaal volledig verraden, zodat niemand voor
informatie zou betalen en er geen evenwicht bestond. Een CARA-belegger met een normaal
verdeelde payoff vraagt $D = (\E[x \mid \mathcal{I}] - p)/(a \Var(x \mid \mathcal{I}))$
stuks, en dus meer naarmate de verwachte winst per stuk groter en het risico kleiner is.
Voor een geïnformeerde is de informatie $\mathcal{I} = \{s, p\}$, zodat
$D_I = (s - p)/(a\sigma^2_\varepsilon)$, en voor een ongeïnformeerde is ze $\{p\}$.

Omdat geïnformeerden op $s$ handelen en het aanbod ruist, blijkt de prijs een lineaire
functie te zijn van $w = s - (a\sigma^2_\varepsilon/\lambda)(z - \bar z)$, het signaal
vervuild met aanbodruis. De informativiteit van de prijs is het kwadraat van de correlatie
tussen $s$ en $w$:

```{math}
:label: eq-llms-en-efficientie-rho
\rho^2(\lambda) \equiv \Corr^2(s, w) = \frac{\lambda^2}{\lambda^2 + \nu},
\qquad \nu = \frac{a^2\sigma^4_\varepsilon\sigma^2_z}{\sigma^2_s}.
```

Hoe meer geïnformeerden er zijn, hoe kleiner de ruis per eenheid signaal in $w$, en hoe
dichter de informativiteit bij 1 komt. In het toy-voorbeeld is $\nu = 0{,}16$, zodat
$\lambda = 0{,}4$ een informativiteit van 0,5 geeft.

### Het kernresultaat: het evenwicht

Steeds meer beleggers kopen het signaal, tot het precies zijn kosten waard is. Een
belegger die ervoor
betaalt, koopt meer als het signaal goed is, zodat de prijs met het signaal stijgt en er
een spoor van draagt. Omdat het aanbod ruist, weet een ongeïnformeerde niet of een hoge
prijs goed nieuws of weinig aanbod betekent. Naarmate meer beleggers betalen, wordt het
spoor duidelijker en daalt de waarde van het signaal, tot die de kosten net dekt.

:::{prf:proposition} Grossman-Stiglitz-evenwicht
:label: thm-llms-en-efficientie-gs

Stel $k = (\sigma^2_\varepsilon/\sigma^2_s)(e^{2ac} - 1)$. Dan is het evenwichtsaandeel
geïnformeerde beleggers

```{math}
:label: eq-llms-en-efficientie-lambda
\lambda^* =
\begin{cases}
0 & k \ge 1,\\
\min\Bigl\{1,\ \sqrt{\nu(1-k)/k}\Bigr\} & 0 < k < 1,
\end{cases}
```

en in een inwendig evenwicht ($0 < \lambda^* < 1$) is de informativiteit van de prijs
$\rho^2 = 1 - k$.
:::

Het bewijs vergelijkt het verwachte nut van beide typen beleggers bij een gegeven prijs.
Die verhouding blijkt niet van de prijs af te hangen, zodat onverschilligheid betekent dat
de restvariantie van een ongeïnformeerde, $\Var(x \mid w)$, precies $e^{2ac}$ keer die van
een geïnformeerde is. In het toy-voorbeeld is die restvariantie 1,5 bij dure en 1,2 bij
goedkope informatie, tegen 1 voor een geïnformeerde. Invullen in
[](#eq-llms-en-efficientie-rho) geeft $\lambda^*$.

:::{prf:proof}
:class: dropdown

*Stap 1: de prijs is lineair in $w$.* Neem als proefoplossing $p = \pi_0 + \pi_1 w$ met
$\pi_1 \neq 0$, zodat $w$ uit $p$ te berekenen is en omgekeerd. Omdat $\Cov(s, w) =
\sigma^2_s$ en $\Var(w) = \sigma^2_s + (a\sigma^2_\varepsilon/\lambda)^2\sigma^2_z$, is
$\Corr^2(s,w) = \lambda^2/(\lambda^2 + \nu)$. De normale projectie geeft $\E[x \mid w] =
\mu_s + \rho^2(w - \mu_s)$ en $\Var(x \mid w) = \sigma^2_\varepsilon + \sigma^2_s(1-\rho^2)$.
In evenwicht is de vraag gelijk aan het aanbod, $\lambda D_I + (1-\lambda) D_U = z$. Met
$\lambda s/(a\sigma^2_\varepsilon) - z = \frac{\lambda}{a\sigma^2_\varepsilon} w - \bar z$
wordt dat

$$
p\left[\frac{\lambda}{a\sigma^2_\varepsilon} + \frac{1-\lambda}{a\Var(x\mid w)}\right]
= \frac{\lambda}{a\sigma^2_\varepsilon}\,w - \bar z
+ \frac{(1-\lambda)\bigl(\mu_s + \rho^2(w - \mu_s)\bigr)}{a\Var(x\mid w)},
$$

lineair in $w$ met $\pi_1 > 0$, zodat de proefoplossing klopt.

*Stap 2: de nutsverhouding hangt niet van $w$ af.* Een geïnformeerde met beginvermogen
$W_0$ en optimale vraag heeft conditioneel op $(s, w)$ nut
$-\exp\bigl(-a(W_0 - c) - (s - p)^2/(2\sigma^2_\varepsilon)\bigr)$. We nemen de
verwachting over $s$ gegeven $w$, met $s - p \mid w \sim \mathcal{N}(\E[x\mid w] - p,
\sigma^2_s(1-\rho^2))$. Voor $Y \sim \mathcal{N}(\mu, v)$ is
$\E[e^{-Y^2/(2\sigma^2)}] = \sqrt{\sigma^2/(\sigma^2 + v)}\,e^{-\mu^2/(2(\sigma^2 + v))}$,
en de ongeïnformeerde heeft hetzelfde nut zonder de factor $e^{ac}$ en zonder de wortel.
De verhouding is dus

```{math}
:label: eq-llms-en-efficientie-ratio
\frac{\E[u(W_I) \mid w]}{\E[u(W_U) \mid w]} = e^{ac}\sqrt{\frac{\sigma^2_\varepsilon}{\Var(x \mid w)}}.
```

*Stap 3: onverschilligheid legt $\rho^2$ vast.* Beide nutten zijn negatief, dus een
verhouding boven 1 betekent dat de geïnformeerde slechter af is. Een inwendig evenwicht
vraagt verhouding 1, dus $\Var(x\mid w) = \sigma^2_\varepsilon e^{2ac}$ en $1 - \rho^2 =
k$. Invullen in [](#eq-llms-en-efficientie-rho) geeft $\lambda^2 = \nu(1-k)/k$. Is dat
groter dan 1, dan loont informatie ook als iedereen geïnformeerd is en is $\lambda^* = 1$.
Is $k \ge 1$, dan is ze zelfs bij een oninformatieve prijs de kosten niet waard en is
$\lambda^* = 0$. $\square$
:::

### Wat het voorspelt: goedkopere informatie

Goedkopere informatie maakt de prijs informatiever, zoals we verwachtten. Omdat $k$ met
$c$ stijgt, dalen $\lambda^*$ en $\rho^2 = 1 - k$ allebei als informatie duurder wordt, en
stijgen ze als ze goedkoper wordt. Het model voegt daar twee dingen aan toe.

Ten eerste bepaalt de aanbodruis hoeveel beleggers meedoen, maar niet hoe informatief de
prijs
wordt. In een inwendig evenwicht is $\rho^2 = 1 - k$, en $k$ bevat $\sigma^2_z$ niet. Meer
ruis trekt daarom meer geïnformeerden aan ($\lambda^*$ is evenredig met $\sigma_z$), en hun
extra handel compenseert de extra ruis precies. De liquiditeitshandelaren van aanname 3
zijn in dit model dus geen vijand van
efficiëntie maar de voorwaarde ervoor.

Ten tweede is er een grens. Als $c$ naar nul gaat, gaat $\lambda^*$ naar 1, maar dan is
nog altijd
$\rho^2 = 1/(1+\nu) < 1$, in het toy-voorbeeld $1/1{,}16 \approx 0{,}86$. Zelfs een
belegger die $s$ kent, handelt voorzichtig omdat $\varepsilon$ onzeker blijft, zodat de
aanbodruis zichtbaar blijft in de prijs. Een taalmodel verlaagt $c$, maar niet de
risicoaversie $a$ of de fundamentele onzekerheid $\sigma^2_\varepsilon$, en juist die
twee zetten de grens.

### Gedeelde modelfouten

Grossman en Stiglitz nemen aan dat alle geïnformeerden hetzelfde ware signaal zien, terwijl
in werkelijkheid elke belegger een eigen schatting maakt met een eigen model. Als de
modellen
verschillen, middelen hun fouten weg, en als ze op elkaar lijken, gebeurt dat niet.
Goedkopere informatie verkleint de eigen fout van elk model, maar niet de gedeelde, en die
kan door een handvol dominante taalmodellen juist groeien.

:::{prf:proposition} Variantie van de geaggregeerde fout
:label: thm-llms-en-efficientie-mono

$N$ arbitrageurs schatten een waarde, elk met een fout met variantie $\sigma^2$. Een
fractie $\omega$ gebruikt hetzelfde model en maakt dezelfde fout $f$, en de overige
$(1-\omega)N$ maken onafhankelijke fouten $u_i$. De prijsfout is het gemiddelde
$\bar e$ van alle fouten. Dan is

```{math}
:label: eq-llms-en-efficientie-mono
\Var(\bar e) = \sigma^2\left(\omega^2 + \frac{1-\omega}{N}\right).
```
:::

:::{prf:proof}
Het gemiddelde is $\bar e = \omega f + \frac1N\sum_i u_i$, met de som over de arbitrageurs
met een eigen model. De twee termen zijn onafhankelijk, dus $\Var(\bar e) =
\omega^2\sigma^2 + (1-\omega)N\sigma^2/N^2$. $\square$
:::

Als $N$ groot wordt, blijft $\omega^2\sigma^2$ over, zodat meer arbitrageurs alleen tegen
de eigen fouten helpen. Met vier arbitrageurs is dat met de hand na te gaan. Elk maakt een
fout van $+1$ of $-1$ met kans $\tfrac12$, zodat ze individueel even nauwkeurig zijn. Met
eigen modellen zijn er $2^4 = 16$ even waarschijnlijke combinaties, waarvan er één een
gemiddelde van $-1$ geeft, vier $-\tfrac12$, zes $0$, vier $+\tfrac12$ en één $+1$. Delen
twee van de vier een model, dan is het gemiddelde $(2f + u_3 + u_4)/4$, en vraagt de
grootste daling $f = u_3 = u_4 = -1$. Gebruiken alle vier hetzelfde model, dan is het
gemiddelde $\pm 1$ met kans $\tfrac12$.

| modellen | $\omega$ | variantie met de hand | kans op de grootste daling |
|---|---|---|---|
| vier eigen | 0 | $2 \cdot \tfrac1{16} + 2 \cdot \tfrac4{16} \cdot \tfrac14 = \tfrac14$ | $\tfrac1{16}$ |
| twee delen er een | $\tfrac12$ | $(4 + 1 + 1)/16 = 0{,}375$ | $\tfrac18$ |
| één gedeeld | 1 | 1 | $\tfrac12$ |

De formule geeft met $\omega = 0$, $\tfrac12$ en 1 dezelfde varianties. De code telt alle
combinaties af en zet ze naast de handberekening.

```{code-cell} ipython3
def average_error_distribution(n, n_shared):
    """Exact distribution of the mean of n +-1 errors when n_shared traders share one draw."""
    n_draws = n - n_shared + (1 if n_shared else 0)
    dist = {}
    for draws in itertools.product([-1, 1], repeat=n_draws):
        if n_shared:
            total = n_shared * draws[0] + sum(draws[1:])
        else:
            total = sum(draws)
        dist[total / n] = dist.get(total / n, 0.0) + 0.5**n_draws
    return pd.Series(dist).sort_index()


by_hand = {"vier eigen": (0, 1 / 4, 1 / 16),
           "twee delen er een": (2, 3 / 8, 1 / 8),
           "één gedeeld": (4, 1.0, 1 / 2)}
rows = {}
for label, (n_shared, var_hand, p_hand) in by_hand.items():
    dist = average_error_distribution(4, n_shared)
    omega = n_shared / 4
    rows[label] = {"variantie met de hand": var_hand,
                   "variantie code": (dist * dist.index.to_numpy() ** 2).sum(),
                   "formule omega^2 + (1-omega)/N": omega**2 + (1 - omega) / 4,
                   "P(grootste daling) met de hand": p_hand,
                   "P(grootste daling) code": dist.loc[-1.0]}
toy_mono = pd.DataFrame(rows).T

assert np.allclose(toy_mono["variantie code"], toy_mono["variantie met de hand"])
assert np.allclose(toy_mono["P(grootste daling) code"], toy_mono["P(grootste daling) met de hand"])
toy_mono.round(4)
```

Elke arbitrageur is in alle drie de gevallen even nauwkeurig. Toch stijgt de kans op de
grootste daling van 1/16 naar 1/2, omdat alleen de samenhang van de fouten verandert.

Dezelfde redenering werkt over aandelen. Schrijf de fout van een model in aandeel $j$ als
$e_j = \beta_j g + \eta_j$. Hier is $g$ een fout die alle aandelen raakt, zoals een te
optimistische kijk op de conjunctuur, en $\eta_j$ een fout in één aandeel. De fout $g$ is
wat aandelen gemeen hebben, en $\omega$ bepaalt of die fout over arbitrageurs uitmiddelt.
Een portefeuille die ondergewaardeerde aandelen koopt en overgewaardeerde verkoopt, met
gewichten $w_j$ die optellen tot nul en samen bèta nul hebben, heeft fout
$\sum_j w_j\eta_j$, en die diversifieert weg. De marktportefeuille heeft een gemiddelde
bèta $\bar\beta$ van ongeveer 1 en houdt fout $\bar\beta g$, zoals de tweede oefening laat
uitrekenen.

Santa-Clara vat de tweedeling in twee zinnen samen:

> Machines make relative prices more efficient, because relative mispricing is what a
> well-funded arbitrageur can trade. Nothing about machines makes the aggregate market
> more efficient, because the aggregate is set by flows meeting inelastic supply.
> {cite}`SantaClara2026`

De eerste zin volgt uit de alinea hierboven, want een portefeuille met bèta nul houdt
alleen de fouten per aandeel over, en die middelen weg. De tweede sluit aan bij
[het vorige college](#06-36-inelastische-markten), dat aannemelijk maakte dat een dollar
instroom de waarde van de markt met twee tot acht dollar verhoogt, met vijf als midden
{cite}`GabaixKoijen2021,KoijenYogo2019`. Als dat klopt, hangt het niveau sterk van stromen
af. Passieve
stromen, en adviseurs die klanten in dezelfde modelportefeuilles leiden, kunnen het deel van
de vraag vergroten dat niet op de prijs reageert, zodat het marktniveau gevoeliger wordt
voor stromen dan voor nieuws.

Een gedeelde fout wordt pas een crash als iedereen tegelijk moet verkopen. Volgens
{cite:t}`Stein2009` gebeurt dat als arbitrageurs niet weten hoeveel anderen dezelfde
positie hebben (*crowding*) en die positie met geleend geld financieren. Gedwongen verkopen
versterken elkaar dan. Het best gedocumenteerde voorbeeld ligt vóór de taalmodellen. In de
week van 6 augustus 2007 leden kwantitatieve aandelenfondsen met dezelfde
waarderingsfactoren grote verliezen, wat volgens
{cite:t}`KhandaniLo2011` past bij een gelijktijdige afbouw van hun posities. Een
monocultuur van taalmodellen zou dat mechanisme versterken.

### Hoe het gemeten wordt: de halfwaardetijd van informatie

Hoe snel een prijs nieuws verwerkt, is af te lezen aan de correlatie tussen het rendement
van vandaag en dat van gisteren. Als een prijs elke dag maar een deel van de afstand tot de
nieuwe waarde overbrugt, loopt de reactie op nieuws door in het rendement van morgen. Hoe
trager de aanpassing, hoe sterker die correlatie. Vanaf hier zijn kleine letters logs.

:::{prf:proposition} Gedeeltelijke aanpassing
:label: thm-llms-en-efficientie-halfwaarde

Laat de fundamentele waarde een random walk zijn, $v_t = v_{t-1} + \xi_t$, en laat de prijs
elke periode een fractie $1-\theta$ van de afstand overbruggen, $p_t = p_{t-1} +
(1-\theta)(v_t - p_{t-1})$ met $0 \le \theta < 1$. Dan volgt het log rendement $\ell_t =
p_t - p_{t-1}$ een AR(1)-proces,

```{math}
:label: eq-llms-en-efficientie-ar1
\ell_t = \theta\, \ell_{t-1} + (1-\theta)\,\xi_t,
\qquad \Corr(\ell_t, \ell_{t-1}) = \theta,
\qquad h_{1/2} = \frac{\ln 2}{-\ln\theta},
```

met $h_{1/2}$ het aantal perioden waarna de helft van een schok in de prijs zit.
:::

:::{prf:proof}
:class: dropdown

Schrijf $q_t = p_t - v_t$ voor de afstand tot de waarde. Uit de aanpassingsregel volgt $q_t
= \theta(p_{t-1} - v_t) = \theta q_{t-1} - \theta\xi_t$, dus $q_{t-1} = -\sum_{j\ge0}
\theta^{j+1}\xi_{t-1-j}$. Dan is $\ell_t = (1-\theta)(v_t - p_{t-1}) = (1-\theta)(\xi_t -
q_{t-1}) = (1-\theta)\sum_{j\ge0}\theta^j \xi_{t-j}$, een AR(1) met coëfficiënt $\theta$.
Na $h$ perioden is een fractie $1 - \theta^{h}$ van een schok verwerkt, en die is
$\tfrac12$ bij $h = \ln 2/(-\ln\theta)$. $\square$
:::

De autocorrelatie van het rendement is dus de fractie van de afstand die de prijs elke dag
laat liggen. Met $\theta = 0{,}2$ per dag is de halfwaardetijd $\ln 2/\ln 5 \approx 0{,}43$
dag, ongeveer drie handelsuren, zodat nieuws dat in minuten wordt verwerkt een dagelijkse
autocorrelatie van vrijwel nul geeft. De maat is wel indirect, want in een index van veel
aandelen geeft ook *niet-synchrone handel* positieve autocorrelatie. Dun verhandelde
aandelen hebben vaak een slotkoers van eerder op de dag, zodat de index een deel van het
nieuws van vandaag pas morgen toont, zonder dat iemand traag reageert.

Santa-Clara vat de meetgeschiedenis samen als halfwaardetijden die in 1969 dagen waren, in
2000 uren, en nu seconden {cite}`SantaClara2026`. Met maanddata konden
{cite:t}`FamaFisherJensenRoll1969` niet eens zien of het dagen waren. Later zagen
{cite:t}`BusseGreen2002` koersen binnen minuten reageren op aandelen die live op CNBC werden
besproken ([](#02-07-event-studies)).

Dat taalmodellen nieuws in koersen brengen, is inmiddels ook direct gemeten.
In het werk van {cite:t}`LopezLiraTang2023` zei ChatGPT per krantenkop of het bericht
goed, slecht of irrelevant was voor de koers. In hun eerste versie voorspelt die score het
rendement van de volgende dag met een coëfficiënt van 0,231 procentpunt ($t = 4{,}7$). Voor
kleine aandelen is het effect bijna driemaal zo sterk, terwijl oudere taalmodellen als GPT-2
en BERT niets voorspelden. In de gepubliceerde versie {cite}`LopezLiraTang2026` dalen de
rendementen van de strategie naarmate meer beleggers taalmodellen gebruiken. Goedkopere
informatie trekt dus geïnformeerden aan tot het voordeel verdwijnt, zoals
[](#eq-llms-en-efficientie-lambda) voorspelt.

De terugkoppeling loopt ook de andere kant op. Volgens {cite:t}`CaoJiangYangZhang2023`
schrijven bedrijven met veel machinale lezers hun jaarverslagen zo dat machines ze
gemakkelijk verwerken, en vermijden ze woorden die algoritmen negatief opvatten. Een
signaal waar iedereen naar kijkt, wordt dus door de afzender gestuurd, en zo'n gedeelde
vertekening middelt volgens [](#eq-llms-en-efficientie-mono) niet weg.

### Advies als portefeuillekeuze

Te weinig spreiding en te veel handel kosten een particulier samen ongeveer drie
procentpunt groei per jaar, en aan beide kan een adviseur iets doen. Ze drukken allebei de
mediane uitkomst, die bij samengestelde groei van het log rendement afhangt. Te weinig
spreiding kost daarin rendement via de variantie, en handel via spread en commissie. Stel
dat een belegger $n$ aandelen in gelijke gewichten houdt, elk met
marktbèta 1 en idiosyncratische volatiliteit $\sigma_\eta$. Hij handelt met
omloopsnelheid $\tau$ per jaar tegen kosten $\kappa$ per eenheid omloop en betaalt een
vergoeding $\phi$. Zijn log-vermogen groeit dan verwacht met $g(n,\tau)$.

```{math}
:label: eq-llms-en-efficientie-groei
g(n,\tau) = R^f + \mu^e - \tfrac12\left(\sigma^2_m + \frac{\sigma^2_\eta}{n}\right) - \kappa\tau - \phi ,
```

Hier is $R^f$ de netto risicovrije rente, $\mu^e$ de verwachte aandelenpremie en $\sigma_m$
de volatiliteit van de markt. De groei daalt met elke kostenterm en stijgt met het aantal
aandelen, omdat [spreiden volgens Markowitz](#01-04-markowitz) hetzelfde verwachte rendement
met minder variantie geeft. Met $\sigma_\eta = 35\%$ en $n = 4$ kost te weinig spreiding
$0{,}35^2/8 \approx 1{,}5$ procentpunt per jaar.

De term $\kappa\tau$ is [de rekenkunde van actief beheer](#04-25-industrie) op het niveau
van een huishouden. Bij {cite:t}`BarberOdean2000` hadden huishoudens een gemiddelde omloop
van 75% per jaar. Met kosten van 2% per eenheid omloop, voor spread en commissie, kost de
gemiddelde omloop 1,5 procentpunt per jaar.
Samen is dat drie procentpunt groei per jaar, en na dertig jaar een factor $e^{-0{,}9}
\approx 0{,}41$ op het mediane eindvermogen.

Het bewijs over robo-advies is minder eenduidig dan dit rekensommetje. Na de invoering van
een robo-adviseur hielden slecht gespreide beleggers meer aandelen, met minder volatiliteit
en betere rendementen {cite}`DAcuntoPrabhalaRossi2019`. Ze verkochten ook minder vaak
winnaars te vroeg en joegen minder trends na. Beleggers
die al goed gespreid waren, gingen daarentegen meer handelen, en alle gebruikers logden
vaker in. Advies maakt de portefeuille dus beter, maar niet vanzelf rustiger.

De andere kant laat {cite:t}`BarberHuangOdeanSchwarz2022` zien. Gebruikers van Robinhood
handelen meer op aandacht dan andere particulieren, en dat komt deels door de app zelf,
want als die uitvalt, daalt vooral de handel in aandelen met veel aandacht. De aandelen
die deze gebruikers op een dag het meest kopen, hebben
over de volgende twintig dagen een gemiddeld abnormaal rendement van $-4{,}7\%$.

Een adviseur die per transactie verdient, duwt de omloop van zijn klant boven wat de klant
zelf zou kiezen. Omdat het nut van de klant rond zijn optimum vlak is, groeit het verlies
met het kwadraat van de duw, zodat een kleine duw bijna niets kost en een grote veel. Een
platform dat de omloop van het gemiddelde naar 300% per jaar duwt, kost de klant bij
dezelfde kosten per eenheid omloop 4,5 procentpunt groei per jaar extra, drie keer wat te
weinig spreiding kost. De mediane klant van een goedkope adviseur wint dus aan spreiding,
terwijl de klant die het platform tot veel handel verleidt het meeste verliest, en in die
klanten zit de slechtere staart.

```{admonition} Samengevat
:class: tip

- Goedkopere informatie verhoogt het aandeel geïnformeerden en de informativiteit $\rho^2 =
  1 - k$ ([](#eq-llms-en-efficientie-lambda)). In het toy-voorbeeld stijgen ze van 0,4 en
  0,5 naar 0,8. Meer ruis in het aanbod trekt meer geïnformeerden aan, maar laat $\rho^2$
  gelijk.
- Ook gratis informatie laat de prijs onvolledig informatief, met $\rho^2 = 1/(1+\nu)
  \approx 0{,}86$, omdat risicoaversie en fundamentele onzekerheid blijven.
- Een gedeelde fout blijft in het gemiddelde staan ([](#eq-llms-en-efficientie-mono)), zodat
  een grotere $\omega$ de fout in het marktniveau vergroot. Relatieve prijzen worden wel
  efficiënter, omdat de fout per aandeel in een portefeuille met bèta nul wegmiddelt.
- Een hogere dagelijkse autocorrelatie $\theta$ betekent tragere prijzen, omdat de prijs
  elke dag een groter deel van de afstand laat liggen ([](#eq-llms-en-efficientie-ar1)).
- Te weinig spreiding en veel handel kosten een particulier samen ongeveer drie
  procentpunt groei per jaar ([](#eq-llms-en-efficientie-groei)), zodat goedkoop advies de
  mediaan verbetert en een platform dat tot handel aanzet de staart verslechtert.
- De simulatie meet in jaren van 250 perioden de informativiteit $\rho^2$, de handelswinst
  van geïnformeerden en de prijsfout van vijftig arbitrageurs met een gedeeld model.
```

## Simulatie: wat één jaar data laat zien

Hoeveel ziet een onderzoeker in één jaar data van goedkopere informatie en van een
gedeeld model? We simuleren telkens 2000 jaren van 250 perioden. Eerst
doen we dat in de economie van Grossman en Stiglitz met de parameters van het
toy-voorbeeld, daarna in een markt van vijftig arbitrageurs met een gedeeld model.

### Informatiekosten en handelswinst

Voor vijf waarden van $c$ simuleren we de economie uit [](#thm-llms-en-efficientie-gs) met
$\mu_s = \bar z = 1$. Per jaar schatten we de informativiteit van de prijs en meten we de
handelswinst van een geïnformeerde min die van een ongeïnformeerde, na aftrek van $c$, omdat
een onderzoeker in data die winst ziet en niet het nut.

```{code-cell} ipython3
def gs_price(lam, rho2, a, var_s, var_e, mu_s, z_bar):
    """Coefficients of the linear equilibrium price p = p0 + p1 * w (lam > 0) and Var(x | p)."""
    V = var_e + var_s * (1 - rho2)
    A = lam / (a * var_e) + (1 - lam) / (a * V)
    # p0 and p1 solve the market-clearing equation in step 1 of the proof
    p0 = (-z_bar + (1 - lam) * mu_s * (1 - rho2) / (a * V)) / A
    p1 = (lam / (a * var_e) + (1 - lam) * rho2 / (a * V)) / A
    return p0, p1, V


def simulate_gs(c, n_years=2000, T=250, mu_s=1.0, z_bar=1.0):
    """Simulate the Grossman-Stiglitz economy; per 'year' estimate rho2 and the informed trading gain."""
    lam, rho2, value = gs_equilibrium(c, a, var_s, var_e, var_z)
    s = mu_s + np.sqrt(var_s) * rng.standard_normal((n_years, T))
    x = s + np.sqrt(var_e) * rng.standard_normal((n_years, T))
    z = z_bar + np.sqrt(var_z) * rng.standard_normal((n_years, T))
    w = s - a * var_e / lam * (z - z_bar)
    p0, p1, V = gs_price(lam, rho2, a, var_s, var_e, mu_s, z_bar)
    p = p0 + p1 * w
    d_inf = (s - p) / (a * var_e)
    d_uninf = (mu_s + rho2 * (w - mu_s) - p) / (a * V)
    assert np.allclose(lam * d_inf + (1 - lam) * d_uninf, z)       # demand equals supply
    gain = (d_inf - d_uninf) * (x - p) - c
    s_dev = s - s.mean(1, keepdims=True)
    p_dev = p - p.mean(1, keepdims=True)
    rho2_hat = (s_dev * p_dev).sum(1) ** 2 / ((s_dev**2).sum(1) * (p_dev**2).sum(1))
    year_gain = gain.mean(1)
    return {"c": c,
            "aandeel geïnformeerd": lam,
            "informativiteit theorie": rho2,
            "informativiteit geschat, gemiddelde": rho2_hat.mean(),
            "informativiteit geschat, sd over jaren": rho2_hat.std(),
            "handelswinst na c, gemiddelde": year_gain.mean(),
            "handelswinst na c, sd over jaren": year_gain.std(),
            "aandeel jaren met verlies": (year_gain < 0).mean()}


sim_gs = pd.DataFrame([simulate_gs(c) for c in [0.01, 0.03, 0.06, 0.10, 0.15]]).set_index("c")
sim_gs.round(4)
```

De geschatte informativiteit ligt gemiddeld binnen 0,003 van de theoretische waarde, met
een spreiding over jaren van 0,016 tot 0,045. Eén jaar data volstaat dus om de
informativiteit te meten.
Bij $c = 0{,}01$ en $0{,}03$ is iedereen geïnformeerd en staat de informativiteit op de
grens
van 0,86 uit de theorie. De figuur toont links de drempel waaronder iedereen
geïnformeerd is, en rechts het teken van de handelswinst.

```{code-cell} ipython3
:label: cel-llms-en-efficientie-gs
:tags: [hide-input]

c_grid = np.linspace(0.001, 0.2, 400)
curves = pd.DataFrame([gs_equilibrium(c, a, var_s, var_e, var_z) for c in c_grid],
                      index=c_grid, columns=["lambda", "rho2", "value"])

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(c_grid, curves["lambda"], label="aandeel geïnformeerd $\\lambda^*$")
axes[0].plot(c_grid, curves["rho2"], label="informativiteit prijs $\\rho^2$")
axes[0].plot(c_grid, curves["value"] / c_grid, label="bruto waarde signaal / $c$")
axes[0].set_ylim(0, 3)
axes[0].set_xlabel("Informatiekosten $c$")
axes[0].set_ylabel("Niveau")
axes[0].set_title("Evenwicht als functie van de informatiekosten")
axes[0].legend()
axes[1].errorbar(sim_gs.index, sim_gs["handelswinst na c, gemiddelde"],
                 yerr=1.96 * sim_gs["handelswinst na c, sd over jaren"],
                 fmt="o", capsize=4, label="gemiddelde en 95% van de jaren")
axes[1].axhline(0, color="black", lw=0.8)
axes[1].set_xlabel("Informatiekosten $c$")
axes[1].set_ylabel("Handelswinst geïnformeerd − ongeïnformeerd, na $c$")
axes[1].set_title("Gemeten handelswinst is geen informatierente")
axes[1].legend()
plt.show()
```

:::{figure} #cel-llms-en-efficientie-gs
:label: fig-llms-en-efficientie-gs
:width: 100%

Links staat het evenwicht. Onder een drempel van $c$ is iedereen geïnformeerd en is
informatie meer waard dan ze kost, en daarboven is de bruto waarde van het signaal precies
$c$. Rechts verdienen geïnformeerden na aftrek van $c$ elk jaar meer, vanaf $c = 0{,}03$
meer naarmate informatie duurder is, ook waar ze in nut niet beter af zijn.
:::

De handelswinst is geen informatierente. In alle 2000 jaren verdient een geïnformeerde na
aftrek van $c$ meer dan een ongeïnformeerde, en vanaf $c = 0{,}03$ groeit dat voordeel met
de kosten, tot 2,59 per periode bij $c = 0{,}15$. Toch is in een inwendig evenwicht
niemand in nut beter af, omdat de geïnformeerde grotere
posities neemt en meer risico draagt. Een onderzoeker die in de winst van professionele
beleggers een informatierente ziet, meet dus een vergoeding voor kosten en risico. Een
voordeel dat krimpt als informatie goedkoper wordt, is dan een kenmerk van het evenwicht en
geen verdwenen ontdekking.

### Een gedeeld model onder vijftig arbitrageurs

Nu schalen we [](#thm-llms-en-efficientie-mono) op. Vijftig arbitrageurs schatten elke dag
de waarde van een activum, elk met een fout met variantie 1. De fouten hebben dikke
staarten (een Student-$t$-verdeling met vier vrijheidsgraden), en de prijsfout is hun
gemiddelde. Een
fractie $\omega$ deelt één model en dus één fout per dag. We kijken naar de dagelijkse
prijsfout en naar de slechtste dag van elk jaar, omdat een risicomanager precies dat in één
jaar data ziet.

```{code-cell} ipython3
def t_unit(size, df=4):
    """Unit-variance Student-t draws."""
    return rng.standard_t(df, size) * np.sqrt((df - 2) / df)


N_ARB, N_DAYS, N_YEARS = 50, 250, 2000
mono_rows, mono_errors = [], {}
for share in [0.0, 0.1, 0.3, 0.6, 1.0]:
    n_shared = int(round(share * N_ARB))
    err = n_shared * t_unit((N_YEARS, N_DAYS))
    for start in range(0, N_YEARS, 250):                          # chunks keep memory small
        stop = min(start + 250, N_YEARS)
        err[start:stop] += t_unit((stop - start, N_DAYS, N_ARB - n_shared)).sum(-1)
    err /= N_ARB
    worst = err.min(axis=1)
    mono_errors[share] = err
    mono_rows.append({"fractie gedeeld": share,
                      "sd theorie": np.sqrt(share**2 + (1 - share) / N_ARB),
                      "sd simulatie": err.std(),
                      "0,1%-kwantiel": np.quantile(err, 0.001),
                      "slechtste dag (mediaan jaar)": np.median(worst),
                      "slechtste dag (1 op 20 jaar)": np.quantile(worst, 0.05),
                      "kurtosis": stats.kurtosis(err, axis=None)})
mono = pd.DataFrame(mono_rows).set_index("fractie gedeeld")
mono.round(3)
```

De standaarddeviatie volgt [](#eq-llms-en-efficientie-mono) op hoogstens 0,006 na, van
0,14 zonder gedeeld model tot 0,61 bij 60% gedeeld. De staart groeit sneller. De kurtosis
is het hoogst in een gemengde markt, omdat de onafhankelijke fouten daar meestal wegmiddelen
en het gedeelde model af en toe een uitschieter maakt. Rechts laat de figuur zien hoe snel
de
slechtste dag van een jaar daalt als het gedeelde deel groeit.

```{code-cell} ipython3
:label: cel-llms-en-efficientie-mono
:tags: [hide-input]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
bins = np.linspace(-4, 4, 161)
for share, err in mono_errors.items():
    axes[0].hist(err.ravel(), bins=bins, density=True, histtype="step", lw=1.4,
                 label=f"gedeeld = {share:.0%}")
axes[0].set_yscale("log")
axes[0].set_xlabel("Dagelijkse prijsfout (in sd van één arbitrageur)")
axes[0].set_ylabel("Dichtheid (log-schaal)")
axes[0].set_title("Verdeling van de prijsfout")
axes[0].legend()
axes[1].plot(mono.index, mono["slechtste dag (mediaan jaar)"], marker="o", label="mediaan jaar")
axes[1].plot(mono.index, mono["slechtste dag (1 op 20 jaar)"], marker="o", label="1 op 20 jaar")
axes[1].plot(mono.index, -3 * mono["sd theorie"], color="black", ls="--", lw=1, label="$-3 \\times$ sd theorie")
axes[1].set_xlabel("Fractie arbitrageurs met hetzelfde model $\\omega$")
axes[1].set_ylabel("Slechtste dagelijkse prijsfout in een jaar")
axes[1].set_title("De staart groeit met het gedeelde model")
axes[1].legend()
plt.show()
```

:::{figure} #cel-llms-en-efficientie-mono
:label: fig-llms-en-efficientie-mono
:width: 100%

Elke arbitrageur is in alle scenario's even nauwkeurig, maar hoe groter het gedeelde deel,
hoe breder de verdeling van de prijsfout en hoe dikker de staarten. De slechtste dag van
een jaar volgt de gedeelde fout.
:::

Het verraderlijke zit in de mediaan. De slechtste dag van een gewoon jaar zakt bij 10%
gedeeld maar van $-0{,}41$ naar $-0{,}51$. De slechtste dag die eens in twintig jaar
voorkomt, ligt bij 30% gedeeld daarentegen op $-2{,}44$, ruim vier keer zo diep als zonder
gedeeld model.
Een beginnende monocultuur is in één jaar data dus meestal niet te zien, en wanneer ze wel
zichtbaar wordt, gebeurt dat in een zeldzaam jaar. Een zeldzame uitkomst laat zich met
weinig jaren niet meten, en daarmee keert [de standaardfout van 2%](#00-01-rendementen)
hier terug.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** (1) Eisfeldt, Schubert en Zhang, *Generative AI and Firm Values*, NBER-werkdocument
31222, 2023 {cite}`EisfeldtSchubertZhang2023`. (2) De halfwaardetijd van informatie volgens
Santa-Clara {cite}`SantaClara2026`, gemeten met de toetsen uit
[het college over efficiënte markten](#02-06-efficiente-markten) {cite}`LoMacKinlay1988`.

**Wat.** (1) Het meerrendement van bedrijven met een hoge blootstelling aan generatieve AI
ten opzichte van bedrijven met een lage na de lancering van ChatGPT, volgens hun
samenvatting 0,4% per dag. (2) De dagelijkse autocorrelatie van het marktrendement per
decennium.

**Data hier.** (1) Koersen van 50 grote Amerikaanse aandelen via `hap.data.yahoo`, vooraf
ingedeeld in acht bedrijven met vooral code-, tekst- en datawerk (*hoog*), acht chip- en
hardwarebedrijven, twintig met fysiek werk (*laag*) en veertien die niet eenduidig in te
delen zijn. (2) Dagelijkse marktrendementen van French, 1930 tot juli 2026.

**Verschil met het origineel.** Zij meten blootstelling per bedrijf uit beroepen en taken,
terwijl wij 28 aandelen naar sector indelen die bovendien nu groot zijn. De vroege
marktindex bevat veel dun verhandelde aandelen, wat de autocorrelatie opdrijft.

**Verwachte afwijking.** (1) Hoog min laag heeft over dag 0 tot en met 10 een positief
abnormaal rendement van enkele procenten, al is een $t$-waarde onder 2 hier normaal. (2) De autocorrelatie is vóór 1990 het hoogst en
ligt na 2000 in elk decennium binnen 0,1 van nul.
```

### De lancering van ChatGPT als event

De lancering van ChatGPT is het ene moment waarop de kosten van informatie in één keer
zichtbaar daalden, en de event study vraagt of de markt dat meteen in de koersen van
blootgestelde bedrijven verwerkte. Een markt die nieuws in uren verwerkt, zou die
herwaardering binnen elf handelsdagen moeten tonen. De eerste cel laadt de koersen en
bouwt gelijkgewogen portefeuilles, met een eigen groep voor chips en hardware, omdat hun
blootstelling via het product loopt en niet via het personeel.

```{code-cell} ipython3
GROUPS = {
    "hoog": ["ADBE", "CRM", "NOW", "PANW", "FTNT", "GOOGL", "MA", "V"],
    "hardware": ["AAPL", "ANET", "APH", "AVGO", "LRCX", "NVDA", "QCOM", "SMCI"],
    "laag": ["CMG", "CPRT", "CSX", "CTAS", "CVX", "DE", "FAST", "KO", "MNST", "NKE",
             "ODFL", "ORLY", "PG", "ROST", "SBUX", "SHW", "TJX", "TSCO", "UNP", "WMT"],
}
OTHER = ["AMZN", "BAC", "BRK-B", "DHR", "DXCM", "EW", "GILD", "IDXX", "ISRG", "NFLX",
         "TSLA", "UNH", "WFC", "WRB"]                              # not classifiable
TICKERS = sorted(OTHER + [t for group in GROUPS.values() for t in group])
assert len(TICKERS) == 50

prices = hap_data.yahoo(TICKERS, start="2002-01-01", end="2026-08-01")
market = hap_data.market_daily()["Mkt"]
rets = prices.pct_change(fill_method=None).loc["2010-01-01":]
dates = rets.index.intersection(market.index)
rets, mkt = rets.loc[dates], market.loc[dates]

port = pd.DataFrame({g: rets[t].mean(axis=1) for g, t in GROUPS.items()})
port["hoog - laag"] = port["hoog"] - port["laag"]
EVENT = dates.searchsorted(pd.Timestamp("2022-11-30"))
print(f"dag 0 = {dates[EVENT]:%Y-%m-%d}; {len(dates)} handelsdagen {dates[0]:%Y-%m-%d} t/m {dates[-1]:%Y-%m-%d}")
```

Voor elke portefeuille schatten we een marktmodel op de dagen $-280$ tot $-31$, met 30
november 2022 als dag 0. Daarna tellen we de abnormale rendementen op over dag 0 tot en met
10.

```{code-cell} ipython3
def market_model_car(y, m, i0, lo=0, hi=10, est=(-280, -31)):  # TODO: naar hap.stats
    """CAR over [i0+lo, i0+hi] from a market model estimated on [i0+est0, i0+est1].

    The variance includes estimation error in alpha and beta (MacKinlay 1997).
    Returns CAR, its standard error, beta and the abnormal returns from est0 onwards.
    """
    e = np.arange(i0 + est[0], i0 + est[1] + 1)
    X = np.column_stack([np.ones(len(e)), m[e]])
    xtx_inv = np.linalg.inv(X.T @ X)
    coef = xtx_inv @ X.T @ y[e]
    resid = y[e] - X @ coef
    s2 = resid @ resid / (len(e) - 2)
    win = np.arange(i0 + lo, i0 + hi + 1)
    g = np.array([len(win), m[win].sum()])
    car = (y[win] - coef[0] - coef[1] * m[win]).sum()
    path = y[i0 + est[0]:] - coef[0] - coef[1] * m[i0 + est[0]:]
    return car, np.sqrt(s2 * (len(win) + g @ xtx_inv @ g)), coef[1], path


m_arr = mkt.to_numpy()
event_rows = {}
for col in port.columns:
    car, se, beta, _ = market_model_car(port[col].to_numpy(), m_arr, EVENT)
    event_rows[col] = {"CAR[0,+10]": car, "SE": se, "t": car / se, "beta": beta}
event_table = pd.DataFrame(event_rows).T
event_table.round(4)
```

Het cumulatieve abnormale rendement van hoog min laag is 0,15%, met een standaardfout van
4,1 procentpunt. Met één eventdatum klopt die standaardfout alleen als het schattingsvenster
representatief is. Daarom vergelijken we het event ook met alle niet-overlappende vensters
van elf dagen sinds 2011, elk met een eigen marktmodel.

```{code-cell} ipython3
y_ls = port["hoog - laag"].to_numpy()
first = dates.searchsorted(pd.Timestamp("2011-03-01"))
placebo_days = [i for i in range(first, EVENT - 11, 11) if np.isfinite(y_ls[i - 280:i + 11]).all()]
placebo = np.array([market_model_car(y_ls, m_arr, i)[0] for i in placebo_days])
car_event = event_table.loc["hoog - laag", "CAR[0,+10]"]
pd.Series({
    "aantal placebovensters": len(placebo),
    "sd placebo-CAR": placebo.std(ddof=1),
    "SE uit marktmodel (event)": event_table.loc["hoog - laag", "SE"],
    "CAR event / sd placebo": car_event / placebo.std(ddof=1),
    "percentiel van event in placebo": (placebo < car_event).mean(),
    "CAR[-20,-1], vóór het event": market_model_car(y_ls, m_arr, EVENT, -20, -1)[0],
}).round(4)
```

Het event valt op het 51e percentiel van 268 placebovensters met een spreiding van 3,4
procentpunt. In de vier weken vóór de lancering had hoog min laag bovendien al 8,5%
abnormaal verloren. De vraag bij de figuur is of de lijn na dag 0 de band verlaat.

```{code-cell} ipython3
:label: cel-llms-en-efficientie-chatgpt
:tags: [hide-input]

_, _, _, path = market_model_car(y_ls, m_arr, EVENT)
tau = np.arange(-280, len(path) - 280)
keep = (tau >= -20) & (tau <= 40)
cum = np.cumsum(path[keep]) - np.cumsum(path[keep])[tau[keep] == -1]      # zero at day -1
sd_day = placebo.std(ddof=1) / np.sqrt(11)
band = 1.96 * sd_day * np.sqrt(np.clip(tau[keep] + 1, 0, None))

fig, ax = plt.subplots()
ax.fill_between(tau[keep], cum - band, cum + band, alpha=0.2, label="95%-band vanaf dag 0 (placebo-spreiding)")
ax.plot(tau[keep], cum, label="cumulatief abnormaal rendement hoog − laag, nul op dag −1")
ax.axvline(0, color="black", lw=0.8)
ax.axvline(10, color="black", lw=0.8, ls="--")
ax.axhline(0, color="grey", lw=0.8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.set_xlabel("Handelsdagen ten opzichte van 30 november 2022")
ax.set_ylabel("Cumulatief abnormaal rendement")
ax.set_title("Software en data versus fysiek werk rond de lancering van ChatGPT")
ax.legend(loc="upper left")
plt.show()
```

:::{figure} #cel-llms-en-efficientie-chatgpt
:label: fig-llms-en-efficientie-chatgpt
:width: 90%

Cumulatief abnormaal rendement van acht software-, platform- en betalingsbedrijven minus
twintig bedrijven met overwegend fysiek werk, nul op de dag vóór de lancering van ChatGPT.
De band groeit met de wortel van de horizon en is geschaald op de spreiding van de
placebovensters. De gestreepte lijn markeert dag 10.
:::

De lijn blijft binnen de band, zodat ook de figuur geen koerseffect laat zien. De tabel
zet het resultaat naast het origineel.

| grootheid | origineel | hier |
|---|---|---|
| cumulatief meerrendement hoog − laag, dag 0 t/m 10 | ruim 4% (0,4% per dag uit de samenvatting) | 0,15% |
| $t$-waarde | niet vermeld voor dit venster | 0,04 |
| teken over dag 0 t/m 5 en dag 0 t/m 20 | positief | negatief |

Niet geslaagd, want over het afgesproken venster is het teken wel positief, maar met 0,15%
en $t = 0{,}04$ haalt de omvang de enkele procenten bij lange na niet. Het teken wisselt
bovendien met het venster en met de hardwareaandelen, zoals de derde oefening laat zien.
Met een ruis van 3,4 procentpunt
over elf dagen zou zelfs een effect van 4% een $t$-waarde van ruim 1 geven, en dat is [de standaardfout van 2%](#00-01-rendementen)
in eventtijd. Daarnaast meten Eisfeldt,
Schubert en Zhang blootstelling per bedrijf, met grote verschillen binnen sectoren. De
replicatie zegt dus niet dat hun effect niet bestaat, maar wel dat het met gratis data van
50 aandelen niet te
zien is.

### Snellere prijzen: autocorrelatie per decennium

Voor elk decennium sinds 1930 berekenen we de autocorrelatie van het dagelijkse log
marktrendement en de variance ratio over vijf dagen met een robuuste $z$-waarde. Daarnaast
berekenen we de volatiliteit en de halfwaardetijd die [](#eq-llms-en-efficientie-ar1) bij
die autocorrelatie geeft, met 6,5 handelsuur per dag.

```{code-cell} ipython3
r_daily = np.log1p(hap_data.market_daily()["Mkt"])
decade_rows = []
for start in range(1930, 2030, 10):
    x = r_daily.loc[f"{start}-01-01":f"{start + 9}-12-31"]
    rho1 = x.autocorr(1)
    vr = hap.stats.variance_ratio(x, 5)
    decade_rows.append({
        "decennium": f"{start}s", "dagen": len(x), "rho1": rho1, "SE": 1 / np.sqrt(len(x)),
        "VR(5)": vr["vr"], "z VR(5) robuust": vr["z2"],
        "vol (jaar)": x.std() * np.sqrt(252),
        "halfwaardetijd (uur)": 6.5 * np.log(2) / -np.log(rho1) if rho1 > 0 else np.nan,
    })
decades = pd.DataFrame(decade_rows).set_index("decennium")
decades.round(3)
```

De autocorrelatie is in de eerste zeven decennia positief en significant en piekt in de
jaren zeventig op 0,29. Daarna daalt ze, tot onder nul in deze eeuw. De figuur laat zien
welke decennia na 1990 buiten hun interval rond nul vallen.

```{code-cell} ipython3
:label: cel-llms-en-efficientie-autocorr
:tags: [hide-input]

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(decades.index, decades["rho1"], yerr=1.96 * decades["SE"], capsize=3, color=hap.plotting.COLORS[0])
ax.axhline(0, color="black", lw=0.8)
ax.set_xlabel("Decennium")
ax.set_ylabel("Eerste-orde-autocorrelatie, dagrendement")
ax.set_title("De dagelijkse autocorrelatie van de Amerikaanse markt, 1930–2026")
plt.show()
```

:::{figure} #cel-llms-en-efficientie-autocorr
:label: fig-llms-en-efficientie-autocorr
:width: 85%

Eerste-orde-autocorrelatie van het dagelijkse log marktrendement (French, CRSP,
waardegewogen) per decennium, met een 95%-interval onder de nulhypothese van
onafhankelijkheid. Alleen de jaren 2020 liggen meer dan 0,1 onder nul, en de jaren 2000
vallen net buiten het interval.
:::

De balk van de jaren 2020 ligt als enige meer dan 0,1 onder nul, en de volgende cel zet
2020 apart om te zien waar dat vandaan komt.

```{code-cell} ipython3
r_2020s = r_daily.loc["2020-01-01":].to_numpy()
pd.Series({
    "rho1, alleen 2020": r_daily.loc["2020-01-01":"2020-12-31"].autocorr(1),
    "rho1, 2021 t/m 2026-07": r_daily.loc["2021-01-01":].autocorr(1),
    "rangcorrelatie rho1, jaren 2020": stats.spearmanr(r_2020s[1:], r_2020s[:-1]).statistic,
}).round(3)
```

De negatieve autocorrelatie van de jaren 2020 komt vrijwel geheel uit de coronacrash,
want 2020 alleen geeft $-0{,}34$ en de jaren daarna $-0{,}02$. De tabel zet de meting naast
de samenvatting van Santa-Clara.

| grootheid | origineel (Santa-Clara) | hier |
|---|---|---|
| halfwaardetijd rond 1970 | dagen | 3,6 handelsuur (jaren zeventig) |
| halfwaardetijd rond 2000 | uren | 1,8 handelsuur (jaren negentig) |
| autocorrelatie jaren 2020 | – | $-0{,}15$, zonder 2020 $-0{,}02$ |

Gedeeltelijk geslaagd, want het maximum ligt vóór 1990, zoals verwacht, maar de jaren 2020
liggen met $-0{,}15$ verder dan 0,1 van nul, al vindt de robuuste variance-ratiotoets daar
geen significante afwijking ($z = -1{,}04$). Santa-Clara bedoelt bovendien de verwerking van
nieuws per aandeel, terwijl onze maat voor de hele markt geldt, zodat de tabel alleen de
richting vergelijkt. Onze halfwaardetijden zijn een bovengrens voor traagheid, omdat
niet-synchrone handel in de oude index precies dit patroon geeft, en de daling valt samen
met de komst van indexfutures (vanaf 1982) en ETF's (vanaf 1993). Het resultaat is dus
verenigbaar met snellere informatieverwerking, maar bewijst die niet.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Grossman en Stiglitz lossen de paradox uit
[het college over efficiënte markten](#02-06-efficiente-markten) op. Goedkopere
informatie trekt meer geïnformeerden aan, maakt prijzen informatiever en laat het gemeten
voordeel krimpen, zoals Lopez-Lira en Tang later rapporteerden. De dagelijkse autocorrelatie
van de markt daalde van 0,29 in de jaren zeventig naar onder nul in deze eeuw, in lijn met
snellere prijzen, en robo-advies leverde beter gespreide portefeuilles en minder
gedragsvertekening op.

**Waar het breekt.** Het model breekt bij het marktniveau en bij de meting. Ook met
snellere prijzen werd de markt niet rustiger. De jaarvolatiliteit van het dagrendement was
10% in de jaren vijftig en zestig, tegen 22% in het eerste decennium van deze eeuw, een
decennium dat 2008 bevat.
Grossman en
Stiglitz zeggen hoe dicht een
prijs bij het signaal ligt, maar niets over stromen die het niveau verplaatsen. Op het ene
moment waarop we precies weten wanneer de nieuwe machine kwam, meten we met 50 aandelen geen
koerseffect. Als beleggers ten slotte zelf uit honderden voorspellers leren en het ware
model niet kennen, verliest het begrip efficiëntie zijn houvast, want dat begrip
veronderstelt prijzen die verwachtingen zijn onder het ware model {cite}`MartinNagel2022`.

**Risico of vergissing?** In de Chicago-lezing, waarin de markt rationeel waardeert, is de
koersreactie op ChatGPT een
herwaardering van kasstromen en discontovoeten. Het voordeel van geïnformeerden is dan een
vergoeding voor kosten en risico, zoals in de simulatie, en het crashrisico van gedeelde
modellen is risico met een premie. In de Yale-lezing, waarin beleggers zich vergissen, is
dezelfde reactie aandacht en
geldstroom
{cite}`BarberHuangOdeanSchwarz2022`, en is de monocultuur de crowding van
{cite:t}`Stein2009`, een vergissing die niemand ziet. De posities en modellen van
AI-gedreven fondsen zouden de lezingen kunnen scheiden, net als de kasstromen van
blootgestelde bedrijven sinds de lancering. De eerste zijn echter niet openbaar, en de
tweede reeks is nog te kort.
Santa-Clara vat zijn loopbaan samen in het motto uit [](#00-00-setup): wat hij blijvend
verdiende, kwam uit het dragen van risico met een premie, en wat hij verloor, uit de
gedachte iets te weten wat de prijs niet wist. Voor taalmodellen volgt daaruit dat een
model dat krantenkoppen leest, vertelt wat de prijs al weet zodra veel beleggers dezelfde
score gebruiken.

**Wat er daarna kwam.** Hier eindigt de geschiedenis en begint de balans. Welke uitspraken
na anderhalve eeuw overeind staan, en hoe zeker we van elk ervan zijn, onderzoekt
[](#08-38-wat-we-weten).

## Oefeningen

:::{exercise}
:label: ex-llms-en-efficientie-1

**Ruis en de grens van volledige deelname.** Deze oefening varieert het toy-voorbeeld. Gebruik dezelfde parameters
($a = 2$, $\sigma^2_s = \sigma^2_\varepsilon = 1$, $\sigma^2_z = 0{,}04$).

1. Verdubbel de ruis in het aanbod naar $\sigma^2_z = 0{,}08$ bij $c = \ln(1{,}5)/4$.
   Bereken met de hand $\lambda^*$ en $\rho^2$ en leg uit waarom het ene verandert en het
   andere niet.
2. Leid af bij welke informatiekosten $c^*$ iedereen geïnformeerd wordt, en bereken $c^*$
   voor het toy-voorbeeld.
3. Controleer beide antwoorden met `gs_equilibrium`.
:::

:::{solution} ex-llms-en-efficientie-1
:class: dropdown

**(1)** Nu is $\nu = 0{,}32$ en nog steeds $k = 0{,}5$, dus $\rho^2 = 0{,}5$ blijft gelijk
en $\lambda^* = \sqrt{0{,}32} = 0{,}566$. Meer ruis maakt informatie aantrekkelijker, en er
treden beleggers toe tot de informativiteit weer op het niveau staat waar informatie precies
$c$ waard is.

**(2)** $\lambda^* = 1$ zodra $\nu(1-k)/k \ge 1$, dus zodra $k \le \nu/(1+\nu)$. Met $k =
(\sigma^2_\varepsilon/\sigma^2_s)(e^{2ac}-1)$ geeft dat
$c^* = \ln\bigl(1 + \tfrac{\sigma^2_s}{\sigma^2_\varepsilon}\tfrac{\nu}{1+\nu}\bigr)/(2a)$,
en voor $\nu = 0{,}16$ is $c^* = \ln(1{,}1379)/4 = 0{,}0323$.

```{code-cell} ipython3
print("sigma_z^2 = 0.08:", np.round(gs_equilibrium(np.log(1.5) / 4, a, var_s, var_e, 0.08)[:2], 4))
nu_toy = a**2 * var_e**2 * var_z / var_s
c_star = np.log1p(var_s / var_e * nu_toy / (1 + nu_toy)) / (2 * a)
lam_around = [round(float(gs_equilibrium(c, a, var_s, var_e, var_z)[0]), 4) for c in (c_star * 0.99, c_star * 1.01)]
print(f"c* = {c_star:.4f}; lambda net onder en boven c*: {lam_around}")
```

De oefening laat zien waarom goedkope informatie de prijs maar tot een grens informatiever
maakt. Onder $c^*$ doet iedereen al mee, en wat de prijs dan nog tegenhoudt, is
risicoaversie en geen kostprijs.
:::

:::{exercise}
:label: ex-llms-en-efficientie-2

**Relatieve en geaggregeerde fouten.** Een model maakt in elk van $K$ aandelen een fout
$e_j = g + \eta_j$, met $\Var(g) = \sigma^2_g$ (een fout die alle aandelen raakt) en
$\eta_j$ onafhankelijk met variantie $\sigma^2_\eta$. De fout $g$ is de gedeelde modelfout uit de theorie, nu over aandelen in plaats van over arbitrageurs.

1. Leid de variantie af van de fout in een gelijkgewogen marktportefeuille. Doe hetzelfde
   voor een portefeuille die de eerste helft van de aandelen koopt en de tweede helft
   verkoopt, elk met gewicht $1/(K/2)$.
2. Neem $\sigma_g = \sigma_\eta = 1$ en $K = 2, 10, 100, 1000$, en controleer de
   uitkomsten met een simulatie van 20 000 dagen.
3. Wat betekent dit voor de bewering van Santa-Clara dat machines relatieve prijzen
   efficiënter maken, maar het marktniveau niet?
:::

:::{solution} ex-llms-en-efficientie-2
:class: dropdown

**(1)** De marktportefeuille heeft fout $\bar e = g + \bar\eta$ met variantie $\sigma^2_g +
\sigma^2_\eta/K$. In de tweede portefeuille valt $g$ weg, en de fout is het verschil van twee
gemiddelden van $K/2$ onafhankelijke $\eta$'s, met variantie $4\sigma^2_\eta/K$.

**(2)** De simulatie volgt beide formules.

```{code-cell} ipython3
rows = []
for K in [2, 10, 100, 1000]:
    g = rng.standard_normal((20_000, 1))
    eta = rng.standard_normal((20_000, K))
    e = g + eta
    long_short = e[:, :K // 2].mean(1) - e[:, K // 2:].mean(1)
    rows.append({"K": K, "markt, simulatie": e.mean(1).var(), "markt, theorie": 1 + 1 / K,
                 "koop-verkoop, simulatie": long_short.var(), "koop-verkoop, theorie": 4 / K})
pd.DataFrame(rows).set_index("K").round(3)
```

**(3)** De relatieve fout gaat met $1/K$ naar nul, terwijl de geaggregeerde fout
$\sigma^2_g$ blijft. Een beter model verkleint $\sigma^2_\eta$, maar geen aantal aandelen of
arbitrageurs haalt $g$ weg. Het marktniveau wordt dus alleen efficiënter als de modellen
verschillender worden, niet als ze beter worden.
:::

:::{exercise}
:label: ex-llms-en-efficientie-3

**Hoe gevoelig is de ChatGPT-event study?** Gebruik `port`, `m_arr`, `EVENT` en
`market_model_car` uit de replicatie.

1. Bereken het cumulatieve abnormale rendement van *hoog* min *laag* over dag 0 tot en met
   5, tot en met 10 en tot en met 20. Doe hetzelfde voor dag $-5$ tot en met $-1$, als
   placebo vóór het event.
2. Herhaal het venster tot en met dag 10 met de hardwareaandelen toegevoegd aan *hoog*.
3. Vergelijk elk resultaat met de spreiding van placebovensters van dezelfde lengte. Welke
   conclusie blijft bij alle keuzes staan?
:::

:::{solution} ex-llms-en-efficientie-3
:class: dropdown

```{code-cell} ipython3
def placebo_sd(y, length):
    days = [i for i in range(first, EVENT - length, length) if np.isfinite(y[i - 280:i + length]).all()]
    return np.std([market_model_car(y, m_arr, i, 0, length - 1)[0] for i in days], ddof=1)


hoog_plus = rets[GROUPS["hoog"] + GROUPS["hardware"]].mean(axis=1) - port["laag"]
windows = [("hoog - laag", y_ls, lo, hi) for lo, hi in [(-5, -1), (0, 5), (0, 10), (0, 20)]]
windows.append(("hoog+hardware - laag", hoog_plus.to_numpy(), 0, 10))
rows = []
for name, y, lo, hi in windows:
    car, se, _, _ = market_model_car(y, m_arr, EVENT, lo, hi)
    rows.append({"portefeuille": name, "venster": f"[{lo},{hi}]", "CAR": car, "SE model": se,
                 "sd placebo": placebo_sd(y, hi - lo + 1)})
sens = pd.DataFrame(rows)
sens["CAR / sd placebo"] = sens["CAR"] / sens["sd placebo"]
sens.round(4)
```

Geen variant komt verder dan ruim een halve placebo-standaarddeviatie van nul. Het teken
wisselt met het venster, de hardwareaandelen maken het $+1{,}46\%$, en de placebo vóór het
event ($+0{,}44\%$) is niet te onderscheiden van de echte vensters. Bij alle keuzes blijft
alleen de omvang van de ruis staan, ruim drie procentpunt over elf dagen. Een event study
met één datum en een paar dozijn aandelen kan een effect van de gepubliceerde omvang dus
bevestigen noch verwerpen.
:::
