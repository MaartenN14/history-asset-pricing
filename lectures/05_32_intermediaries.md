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

(05-32-intermediaries)=

# 2008 en intermediary asset pricing

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 2007–2017, van de run op de repomarkt tot de kapitaalratio van de *primary dealers* (de banken die rechtstreeks met de Federal Reserve in staatsobligaties handelen) als risicofactor. In die jaren verschoof de marginale belegger in de modellen van het huishouden naar de bank.

**Wat we al weten.** Elk prijsmodel is een uitspraak over de stochastic discount factor, en in [](#05-31-portfolio-choice) zagen we hoe een belegger die de schattingsfout in gemiddelden serieus neemt, zijn portefeuille kiest. Uit [LTCM](#04-22-risk-management) weten we dat een gehefboomde arbitrageur kan omvallen voordat zijn gelijk uitbetaalt. Wat nog ontbrak, was de stap van één fonds naar de prijzen van alle activa.

**Welke vraag staat open.** Als de marginale belegger geen huishouden is maar een gefinancierde intermediair, bepaalt de balans van die intermediair dan de verwachte rendementen, en waarom explodeerden de risicopremies in 2008?
```

## Overzicht

Dit college vraagt of de balans van gefinancierde intermediairs, zoals dealerbanken, de
risicopremies in alle markten bepaalt. Het antwoord is een voorzichtig ja: als hun
kapitaal schaars wordt, stijgt de premie sneller dan evenredig, en schokken in hun
kapitaalratio krijgen een positieve prijs, al is die kapitaalratio moeilijk te meten.

- We rekenen met de hand na hoe één intermediair na een prijsdaling van 2% zijn balans
  afbouwt en daarmee de daling versterkt.
- We leiden af waarom markt- en financieringsliquiditeit elkaar versterken, en waarom de
  premie omgekeerd evenredig is met de kapitaalratio.
- We simuleren hoe vaak een factortoets op vijftig jaar kwartaaldata een ware prijs van
  intermediairrisico ziet.
- We repliceren de kapitaalratio en de cross-sectionele toets van
  {cite:t}`HeKellyManela2017`, de broker-dealer-leverage van {cite:t}`AdrianEtulaMuir2014`
  en de voorspellende kracht van de kapitaalratio.

De theorie lag voor een deel klaar toen de crisis kwam. Zo hadden
{cite:t}`ShleiferVishny1997` en {cite:t}`GrombVayanos2002` arbitrageurs met beperkt
kapitaal gemodelleerd, en {cite:t}`BrunnermeierPedersen2009` lieten zien dat markt- en
financieringsliquiditeit elkaar versterken. Na de crisis bouwden
{cite:t}`HeKrishnamurthy2013` een evenwichtsmodel met de kapitaalratio van de intermediair
als toestandsvariabele. Daarna maakten {cite:t}`AdrianEtulaMuir2014` en
{cite:t}`HeKellyManela2017` van die balans een factor in de cross-sectie, en daarmee begon
een tijdvak waarin een theorie weer het teken van een prijs van risico voorspelt. Voor de
vraag theorie of feit is dat een stap terug naar de theorie. Santa-Clara vat de
verschuiving samen als een nieuwe opvatting over de marginale belegger, die niet meer de
representatieve consument is maar een gehefboomde intermediair {cite}`SantaClara2026`.

## Intuïtie: waarom zou dit waar zijn?

In de herfst van 2008 schoten de spreads op krediet en financiering omhoog, en de grote
verliezen zaten niet bij huishoudens maar bij de dealers die de markten maakten. Dat past
slecht bij de consumptiemodellen van [](#03-12-consumptie-capm), waarin het marginale nut
van huishoudens de prijzen bepaalt.

Zo'n dealerbank koopt obligaties met een klein beetje eigen geld en veel geleend geld. De
geldgever houdt een *haircut* in (het deel van de waarde dat de bank met eigen vermogen
moet financieren). Bij een haircut van 10% mag de balans dus hoogstens tien keer het eigen
vermogen zijn, een *leverage* (activa gedeeld door eigen vermogen) van tien.

Daalt de prijs 2%, dan verliest zo'n bank een vijfde van het eigen vermogen en moet ze
verkopen. Als veel banken tegelijk verkopen, daalt de prijs verder en dwingt het nieuwe
verlies tot nieuwe verkopen, wat de *verliesspiraal* heet. Wanneer de geldgevers bovendien
hun haircuts verhogen, moet de balans ook zonder nieuw verlies krimpen, en dat is de
*margespiraal*. Volgens {cite:t}`GortonMetrick2012` steeg het gemiddelde haircut op
onderpand dat geen staatsobligatie was, van nul begin 2007 tot bijna 50% eind 2008.

Als de dealer de marginale belegger is, bepaalt zijn marginale nut de stochastic discount
factor. Een dollar is voor hem het meest waard als zijn kapitaal schaars is. Een activum
dat juist dan slecht rendeert, moet daarom gemiddeld meer opleveren. Volgens
Santa-Clara zegt de aandelenpremie misschien minder over de risicoaversie van
huishoudens dan over wie het risico mag dragen {cite}`SantaClara2026`.

We verwachten dus twee dingen. De risicopremie stijgt als de kapitaalratio van de
intermediairs daalt, en wel sneller dan evenredig, omdat de spiralen ook de volatiliteit
opdrijven. Bovendien is de prijs van het risico dat die kapitaalratio daalt positief, en
omdat dealers in bijna elke markt handelen, hoort in elke activaklasse dezelfde prijs te
gelden.

## Toy-voorbeeld: één intermediair, één schok, twee rondes verkopen

Alle cellen van dit college gebruiken dezelfde pakketten en één toevalsgenerator met een
vaste seed.

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

Het voorbeeld draait om één intermediair die precies aan zijn financieringsgrens zit. De
tabel geeft zijn balans en de markt waarop hij moet verkopen.

| grootheid | symbool | waarde |
|---|---|---|
| eigen vermogen | $E$ | 10 |
| activa, tegen prijs $p = 1$ | $A$ | 100 |
| leverage | $L = A/E$ | 10 |
| kapitaalratio | $\eta = E/A$ | 10% |
| haircut, met restrictie $E \ge hA$ | $h$ | 10% |
| vermogen van buitenstaanders | $W$ | 1000 |
| vraagelasticiteit van buitenstaanders | $\varepsilon$ | 2 |

De enige formule die we nog niet hebben afgeleid, is het recept voor de prijsimpact. Een
verkoop ter waarde $S$ moet door de buitenstaanders worden opgenomen en drukt de prijs
daardoor met $S/(\varepsilon W) = S/2000$.

1. **Schok.** De prijs daalt 2%, dus het verlies is $0{,}02 \times 100 = 2$, met $E = 8$
   en $A = 98$. De kapitaalratio daalt tot $8/98 = 8{,}16\%$.
2. **Eerste verkoop.** Met $E = 8$ mag de balans hoogstens $8/0{,}10 = 80$ zijn, dus de
   intermediair verkoopt $S_1 = 98 - 80 = 18$. De prijs daalt $18/2000 = 0{,}9\%$, wat op de
   resterende 80 een verlies van $0{,}72$ geeft.
3. **Tweede verkoop.** Na dat verlies is het eigen vermogen $7{,}28$ en de balans $79{,}28$.
   De toegestane balans is dan $72{,}8$, dus $S_2 = 79{,}28 - 72{,}8 = 6{,}48$.
4. **Waarom het ophoudt.** Elke dollar verlies dwingt $(1-h)/h = 9$ dollar verkoop af. Op
   een balans van ongeveer 80 is elke ronde daardoor ongeveer $80 \times 9/2000 = 0{,}36$
   keer zo groot als de vorige.
5. **Margespiraal.** Stijgt de haircut na de schok naar 12,5%, dan mag de balans hoogstens
   $8/0{,}125 = 64$ zijn. De eerste verkoop is dan $S_1 = 98 - 64 = 34$, die de prijs
   $34/2000 = 1{,}7\%$ drukt, met een verlies van $64 \times 0{,}017 = 1{,}088$. Het eigen
   vermogen is dan $6{,}91$ en de balans $62{,}91$, zodat de toegestane balans
   $6{,}91/0{,}125 = 55{,}30$ is
   en de tweede verkoop $62{,}91 - 55{,}30 = 7{,}61$.

De code rekent beide spiralen af tot er niets meer verkocht hoeft te worden, en zet de
handstappen naast de uitkomsten van de code.

```{code-cell} ipython3
:label: cel-intermediaries-toy

def deleverage(E, A, h, absorb, shock, h_after=None):
    """Loss (and margin) spiral of one intermediary that starts at its constraint E = h A.

    A fundamental price shock hits the assets. The intermediary then sells until
    E = h_after * A; a sale of S depresses the price by S / absorb, which is a new
    loss on the assets it still holds. Returns the capital ratio right after the
    shock, the table of selling rounds and the final price.
    """
    loss = shock * A
    E, A = E - loss, A - loss
    eta_on_impact = E / A
    h = h if h_after is None else h_after
    price, rounds = 1.0 - shock, []
    while (sale := A - E / h) > 1e-12:
        impact = sale / absorb
        kept = A - sale
        loss = impact * kept
        E, A = E - loss, kept - loss
        price *= 1.0 - impact
        rounds.append({"verkoop": sale, "prijsimpact (%)": 100 * impact, "verlies": loss, "E": E, "A": A})
    return eta_on_impact, pd.DataFrame(rounds), price


E0, A0, H0, EPS, W_OUT, SHOCK = 10.0, 100.0, 0.10, 2.0, 1000.0, 0.02
eta_impact, const_rounds, const_price = deleverage(E0, A0, H0, EPS * W_OUT, SHOCK)
_, margin_rounds, margin_price = deleverage(E0, A0, H0, EPS * W_OUT, SHOCK, h_after=0.125)

for name, rounds, price in [("haircut 10%", const_rounds, const_price), ("haircut 10% → 12,5%", margin_rounds, margin_price)]:
    final_equity, final_assets = rounds["E"].iloc[-1], rounds["A"].iloc[-1]
    print(f"{name}: {len(rounds)} rondes, eigen vermogen na afloop {final_equity:.3f}, "
          f"leverage na afloop {final_assets / final_equity:.1f}, prijsdaling {100 * (1 - price):.3f}%")

steps = ["kapitaalratio na de schok", "verkoop ronde 1", "verlies ronde 1", "verkoop ronde 2",
         "verkoop ronde 1, haircut 12,5%", "verlies ronde 1, haircut 12,5%", "verkoop ronde 2, haircut 12,5%"]
by_hand = [8 / 98, 18.0, 0.72, 6.48, 34.0, 1.088, 7.616]
by_code = [eta_impact, const_rounds.loc[0, "verkoop"], const_rounds.loc[0, "verlies"], const_rounds.loc[1, "verkoop"],
           margin_rounds.loc[0, "verkoop"], margin_rounds.loc[0, "verlies"], margin_rounds.loc[1, "verkoop"]]
pd.DataFrame({"met de hand": by_hand, "code": by_code}, index=steps).round(4)
```

Code en handberekening komen op elke stap overeen. Bij een vaste haircut is de prijs na
afloop 3,35% gedaald, zodat de eigen verkopen 1,35 procentpunt aan de schok toevoegen. Het
eigen vermogen is dan 31% lager dan vóór de schok.

Bij de hogere haircut daalt de prijs 4,12%, en daalt de leverage na afloop tot 8, tegen 10
bij een vaste haircut. Dezelfde slechte toestand geeft dus eerst een dalende
kapitaalratio, omdat het verlies het eigen vermogen raakt, en daarna een dalende leverage,
omdat de balans krimpt. Die tegenstelling komt terug bij twee empirische factoren die
allebei een positieve prijs krijgen.

## Theorie

De theorie gaat in drie stappen van de balans van één intermediair naar de prijzen van
alle activa. Eerst laten we zien dat de twee spiralen een markt met twee evenwichten
kunnen opleveren. Daarna leiden we af dat de risicopremie omgekeerd evenredig is met de
kapitaalratio, en dat de volatiliteit dat verband versterkt. Tot slot maken we van het
marginale nut van de intermediair een factormodel. Alles draait om de gedachte dat de
prijs van risico afhangt van het kapitaal van wie het risico draagt.

### Opzet en notatie

Een intermediair heeft op $t$ eigen vermogen $E_t$, activa $A_t$ en schuld $A_t - E_t$. We
schrijven $L_t = A_t/E_t$ voor de leverage en $\eta_t = E_t/A_t = 1/L_t$ voor de
kapitaalratio, het symbool van {cite:t}`HeKellyManela2017`. Voor de primary dealers daalde
die ratio in 2009 tot ongeveer 2%. De financieringsrestrictie luidt $E_t \ge hA_t$ met
haircut $h$, in het toy-voorbeeld 10%.

De artikelen gebruiken $m$ voor de marge of voor de inbreng van huishoudens, maar hier
blijft $m_{t+1}$ de stochastic discount factor. Een verliesspiraal met vaste haircut is al
afgeleid in [](#prop-risk-management-spiraal). Nieuw is dat de haircut, en daarmee de
toegestane balans, zelf van de marktliquiditeit afhangt.

### Marktliquiditeit en financieringsliquiditeit

Markt- en financieringsliquiditeit versterken elkaar, en daardoor kan dezelfde markt
liquide of illiquide zijn. *Waarom zou dit waar zijn?* Speculanten zoals dealers vangen
tijdelijke verkoopdruk op en verdienen daarmee de prijskorting. Is de korting groot, dan
hebben ze op hun bestaande posities verloren, en vragen geldgevers bovendien een hogere
marge. Met minder kapitaal en een hogere marge kunnen ze minder opvangen, zodat de korting
verder oploopt.

We vereenvoudigen het model van {cite:t}`BrunnermeierPedersen2009` tot één periode.
Klanten bieden $z > 0$ eenheden aan van een activum met fundamentele waarde $v$.
Speculanten kopen $x \ge 0$ en buitenstaanders met vraaghelling $\varepsilon$ nemen de
rest, zodat de prijskorting $\Delta = v - p = (z - x)/\varepsilon$ is. Dat is de prijsimpact
uit het toy-voorbeeld, waarin de vraaghelling $\varepsilon W = 2000$ was, de elasticiteit
maal het vermogen van de buitenstaanders.

De speculanten zijn risiconeutraal en kopen zoveel ze mogen zolang $\Delta > 0$. Door hun
bestaande positie $x_0$ is hun kapitaal na de korting $K(\Delta) = \max\{K_0 - x_0\Delta, 0\}$.
Per eenheid storten ze een marge (de haircut uit het toy-voorbeeld) $h(\Delta) = h_0 + \theta\Delta$,
die met de korting
stijgt als $\theta > 0$. Ze kopen dus $x = \min\{z, K(\Delta)/h(\Delta)\}$, en een
evenwicht is een vast punt van

```{math}
:label: eq-intermediaries-bp-vastpunt
\Delta = G(\Delta) \equiv \max\left\{0,\; \frac{1}{\varepsilon}\left(z - \frac{K(\Delta)}{h(\Delta)}\right)\right\}.
```

Rechts staat de korting die ontstaat als de speculanten bij korting $\Delta$ zoveel
mogelijk kopen. In een evenwicht is dat dezelfde korting als die waarmee we begonnen.

:::{prf:proposition} Meervoudige evenwichten
:label: thm-intermediaries-bp

1. $\Delta = 0$ (een liquide markt) is een evenwicht dan en slechts dan als $z \le K_0/h_0$.
2. $\Delta = z/\varepsilon$ (de speculanten kopen niets meer) is een evenwicht dan en slechts dan als $z x_0/\varepsilon \ge K_0$.
3. Geldt $z x_0/\varepsilon > K_0$ en $z < K_0/h_0$, dan zijn er minstens drie evenwichten, de twee hierboven en een instabiel evenwicht ertussen.
:::

:::{prf:proof}
Punt 1 en 2 volgen door $\Delta = 0$ en $\Delta = z/\varepsilon$ in $G$ in te vullen. Voor punt 3 ligt $G$ vlak bij nul onder de 45-graden-lijn, omdat $z < K_0/h_0$. Bij $\hat\Delta = K_0/x_0 < z/\varepsilon$ is het kapitaal op en ligt $G(\hat\Delta) = z/\varepsilon$ erboven. Omdat $G$ continu is, snijdt $G$ de lijn ertussen van onder naar boven, dus met $G' \ge 1$, en daar convergeert de iteratie $\Delta_{k+1} = G(\Delta_k)$ niet. $\square$
:::

Hoe hard reageert een evenwicht op extra aanbod? Impliciet differentiëren van
[](#eq-intermediaries-bp-vastpunt) bij $0 < \Delta^* < K_0/x_0$ geeft

```{math}
:label: eq-intermediaries-bp-multiplier
\frac{\mathrm{d}\Delta^*}{\mathrm{d}z} = \frac{1/\varepsilon}{1 - G'(\Delta^*)},
\qquad
G'(\Delta) = \underbrace{\frac{x_0}{\varepsilon\, h(\Delta)}}_{\text{verliesspiraal}}
+ \underbrace{\frac{\theta\, K(\Delta)}{\varepsilon\, h(\Delta)^2}}_{\text{margespiraal}} ,
```

zolang $G'(\Delta^*) < 1$. Extra verkoopdruk verhoogt de korting dus met de directe impact
$1/\varepsilon$, vermenigvuldigd met een factor die groeit met beide spiralen. Een grotere
positie $x_0$ zet elke extra korting om in meer verlies, en een marge die met de korting
oploopt, holt de koopkracht verder uit.

In het toy-voorbeeld is $x_0$ de resterende balans van 80 en $\varepsilon$ de vraaghelling
van 2000, zodat de verliesterm $80/(2000 \times 0{,}10) = 0{,}4$ is. De factor per ronde was
daar 0,36, omdat het verlies de balans zelf al verkleint en elke dollar verlies dus
$(1-h)/h$ in plaats van $1/h$ dollar verkoop afdwingt. Met $G' \approx 0{,}36$ wordt de
eerste impact ongeveer anderhalf keer zo groot, zoals de eerste daling van 0,9% daar tot
1,35 procentpunt opliep.

In het volledige model stijgen marges omdat geldgevers een liquiditeitsschok niet van een
fundamentele schok kunnen onderscheiden. Zo verklaart het model waarom liquiditeit
plotseling en in veel effecten tegelijk opdroogt {cite}`BrunnermeierPedersen2009`. Voor de
figuur kiezen we $K_0 = 1$, $x_0 = 8$, $h_0 = 0{,}08$, $\theta = 2$ en $\varepsilon = 60$,
en tekenen we $G$ voor drie niveaus van aanbod. Elk snijpunt met de 45-graden-lijn is een
evenwicht.

```{code-cell} ipython3
:label: cel-intermediaries-bp
:tags: [hide-input]

def bp_map(delta, z, K0, x0, h0, theta, eps):
    """Right-hand side G(Delta) of the simplified Brunnermeier-Pedersen fixed point."""
    capital = np.maximum(K0 - x0 * delta, 0.0)
    return np.maximum((z - capital / (h0 + theta * delta)) / eps, 0.0)


BP = dict(K0=1.0, x0=8.0, h0=0.08, theta=2.0, eps=60.0)
grid_d = np.linspace(0.0, 0.25, 5001)
fig, ax = plt.subplots()
for i, z_supply in enumerate([7.0, 10.0, 13.0]):
    gap = bp_map(grid_d, z_supply, **BP) - grid_d
    roots = [0.0] if gap[0] == 0 else []          # Delta = 0 is an equilibrium when G(0) = 0
    for k in np.flatnonzero(np.diff(np.sign(gap)) != 0):
        if gap[k] != 0:                              # sign change between grid points k and k + 1
            root = optimize.brentq(lambda d: bp_map(d, z_supply, **BP) - d, grid_d[k], grid_d[k + 1])
            roots.append(round(float(root), 6))
    roots = sorted(set(roots))
    ax.plot(grid_d, bp_map(grid_d, z_supply, **BP), color=hap.plotting.COLORS[i], label=f"$G(\\Delta)$, aanbod $z$ = {z_supply:g}")
    ax.plot(roots, roots, "o", color=hap.plotting.COLORS[i])
    print(f"z = {z_supply:>4}: evenwichten Delta* = {roots}")
ax.plot(grid_d, grid_d, color="black", lw=0.8, ls="--", label="45-graden-lijn")
ax.set_title("Liquide en illiquide evenwichten bij hetzelfde fundament")
ax.set_xlabel("Prijskorting $\\Delta$")
ax.set_ylabel("$G(\\Delta)$")
ax.legend()
plt.show()
```

:::{figure} #cel-intermediaries-bp
:label: fig-intermediaries-bp
:width: 90%

Bij $z = 7$ en $z = 10$ liggen een liquide en een illiquide evenwicht naast elkaar, gescheiden door een instabiel evenwicht. Welke markt er komt, hangt dan af van verwachtingen en kleine schokken. Bij $z = 7$ geldt voorwaarde 3 van de propositie niet, want $z x_0/\varepsilon = 7 \times 8/60 < 1 = K_0$, maar die voorwaarde is voldoende en niet nodig. De margespiraal met $\theta = 2$ drukt de koopkracht daar zo ver dat er toch drie evenwichten zijn, en het illiquide evenwicht ligt op 0,11, net onder $z/\varepsilon$, omdat de speculanten nog wat kapitaal over hebben. Bij $z = 13$ is het aanbod groter dan de opvangcapaciteit $K_0/h_0 = 12{,}5$, en blijft alleen de illiquide markt over.
:::

::::{note} Twintig intermediairs: de spiraal op schaal
:class: dropdown

Hier houden twintig intermediairs met een leverage tussen 6 en 12 hetzelfde activum, en wie na een schok te groot is, verkoopt tegen afgeprijsde koersen (een *fire sale*). We vergelijken drie werelden bij dezelfde twintigduizend schokken, getrokken met een standaarddeviatie van 3%.

```{code-cell} ipython3
def fire_sale(shock, leverage, h0, theta, absorb, max_rounds=300):
    """Common-asset fire sale among intermediaries with equity 1 and the given leverage.

    shock is a vector of fundamental price declines (one scenario per entry). In every
    round each intermediary sells down to E / h with h = h0 + theta * (cumulative
    decline); total sales depress the price by sales / absorb. Returns the total price
    decline and the share of intermediaries with non-positive equity, per scenario.
    """
    assets = np.outer(1.0 - shock, leverage)
    equity = 1.0 - np.outer(shock, leverage)
    price = 1.0 - shock
    for _ in range(max_rounds):
        haircut = h0 + theta * (1.0 - price)
        sales = np.clip(assets - np.maximum(equity, 0.0) / haircut[:, None], 0.0, None)
        total = sales.sum(axis=1)
        if total.max() < 1e-10:
            break
        impact = np.minimum(total / absorb, 1.0)
        assets = assets - sales
        loss = assets * impact[:, None]
        assets, equity = assets - loss, equity - loss
        price = price * (1.0 - impact)
    return 1.0 - price, (equity <= 0).mean(axis=1)


N_INTERMEDIARIES, H0_SIM, ABSORB_SIM = 20, 0.08, 2000.0
leverage_sim = rng.uniform(6.0, 12.0, N_INTERMEDIARIES)
shocks_sim = np.abs(rng.normal(0.0, 0.03, 20_000))
worlds = {"geen prijsimpact": (0.0, np.inf), "fire sale, vaste haircut": (0.0, ABSORB_SIM),
          "fire sale + margespiraal": (1.0, ABSORB_SIM)}
declines = {name: fire_sale(shocks_sim, leverage_sim, H0_SIM, theta, absorb)[0]
            for name, (theta, absorb) in worlds.items()}

small, large = shocks_sim < 0.02, shocks_sim > 0.06
pd.DataFrame(
    {name: {"mediane daling (%)": 100 * np.median(d), "95e percentiel (%)": 100 * np.quantile(d, 0.95),
            "99e percentiel (%)": 100 * np.quantile(d, 0.99), "P(daling > 10%)": np.mean(d > 0.10),
            "versterking, schok < 2%": np.median(d[small] / shocks_sim[small]),
            "versterking, schok > 6%": np.median(d[large] / shocks_sim[large])}
     for name, d in declines.items()}
).T.round(3)
```

Kleine schokken worden met een vaste haircut nauwelijks versterkt, grote wel. De figuur toont links die knik en rechts de kans op een grote daling.

```{code-cell} ipython3
:label: cel-intermediaries-firesale
:tags: [hide-input]

shock_grid = np.linspace(0.0005, 0.12, 240)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
for i, (name, (theta, absorb)) in enumerate(worlds.items()):
    curve, _ = fire_sale(shock_grid, leverage_sim, H0_SIM, theta, absorb)
    axes[0].plot(100 * shock_grid, 100 * curve, color=hap.plotting.COLORS[i], label=name)
    tail = np.sort(declines[name])
    axes[1].plot(100 * tail, 1.0 - np.arange(tail.size) / tail.size, color=hap.plotting.COLORS[i], label=name)
axes[0].set_title("(a) Totale prijsdaling tegen fundamentele schok")
axes[0].set_xlabel("Fundamentele schok (%)")
axes[0].set_ylabel("Totale prijsdaling (%)")
axes[0].legend()
axes[1].set_yscale("log")
axes[1].set_xlim(0, None)
axes[1].set_title("(b) Kans op een daling groter dan x")
axes[1].set_xlabel("Totale prijsdaling x (%)")
axes[1].set_ylabel("P(daling > x), log-schaal")
fig.tight_layout()
plt.show()
```

De kans op een daling van meer dan 10% stijgt van 0,1% zonder prijsimpact naar 12% met de margespiraal. Een risicomodel dat alleen de fundamentele schokken kent, zit er dus twee ordes van grootte naast.
::::

### Kapitaalratio en risicopremie

Als alleen intermediairs het risicovolle activum kunnen houden, is de risicopremie
omgekeerd evenredig met hun kapitaalratio. Na verliezen krimpt het eigen vermogen van de
sector, terwijl het activum toch gehouden moet worden. Elke dollar eigen vermogen draagt
dan meer risico, en de bankiers vragen per eenheid risico een hogere premie. Het model van
{cite:t}`HeKrishnamurthy2013` reproduceert zo de sprong van de crisispremies en hun snelle
terugval, met een grens aan het eigen vermogen dat huishoudens bij intermediairs willen
inleggen.

We nemen de kern over in een lokale versie. De bankiers hebben vermogen $w_t$ en relatieve
risicoaversie $\gamma$, en halen bij huishoudens hoogstens $\chi w_t$ aan extra eigen
vermogen op, met $\chi$ de inbreng die huishoudens per dollar bankiersvermogen willen
doen. Het activum heeft waarde $p_t$, verwacht overrendement $\pi_t$ en volatiliteit
$\sigma_{R,t}$. Zolang de restrictie bindt, is de kapitaalratio $\eta_t = (1+\chi)w_t/p_t$,
en anders ligt ze op een vaste $\bar\eta$.

:::{prf:proposition} Risicopremie bij een bindende kapitaalrestrictie
:label: thm-intermediaries-hk

De intermediair kiest zijn portefeuille zoals een Merton-belegger, en vraag is gelijk aan aanbod. Dan is

```{math}
:label: eq-intermediaries-hk-premie
\pi_t = \frac{\gamma\,\sigma_{R,t}^2}{\eta_t}
\quad\text{als } \eta_t < \bar\eta,
\qquad
\pi_t = \frac{\gamma\,\sigma_{R,t}^2}{\bar\eta}
\quad\text{als de restrictie niet bindt.}
```
:::

:::{prf:proof}
Volgens de Merton-regel uit [](#03-10-merton-icapm) stopt een CRRA-belegger het deel $\pi_t/(\gamma\sigma_{R,t}^2)$ van zijn eigen vermogen in het risicovolle activum. Omdat de sector met eigen vermogen $(1+\chi)w_t$ het hele activum houdt, moet dat deel $p_t/((1+\chi)w_t) = 1/\eta_t$ zijn. Gelijkstellen geeft het resultaat, en zonder bindende restrictie geldt hetzelfde met $\bar\eta$. $\square$
:::

Bij gegeven volatiliteit is de premie in het beperkte gebied dus omgekeerd evenredig met
de kapitaalratio. Ze stijgt met $\gamma$, omdat de bankiers dan meer beloning per eenheid
risico vragen. Met $\gamma = 2$ en $\sigma_R = 12\%$ is de premie bij $\eta = 0{,}5$
gelijk aan $2 \times 0{,}0144/0{,}5 = 5{,}8\%$. Het teken uit de intuïtie klopt dus, maar
bij vaste volatiliteit groeit de premie precies evenredig met $1/\eta$.

### Numerieke oplossing: de volatiliteit versterkt de premie

Dat de premie sneller dan evenredig groeit, komt door de volatiliteit, die zelf stijgt als
de kapitaalratio daalt. Een dividendschok verlaagt de prijs, waarop de gehefboomde
intermediair een veelvoud verliest. Daardoor daalt zijn kapitaalratio en stijgt de
vereiste premie, die de prijs nog verder drukt.

Om dat uit te rekenen, nemen we een eenvoudige prijsregel. Dividenden groeien met
volatiliteit $\sigma_D$, en een hogere premie $\mathrm{d}\pi$ verlaagt de log-prijs met
$\tau\,\mathrm{d}\pi$, waarbij $\tau$ de verwachte duur van een premieschok in jaren is.
In het beperkte gebied verandert het vermogen van de bankiers met $1/\eta_t$ maal het
rendement.

:::{prf:proposition} Volatiliteitsversterking
:label: thm-intermediaries-hk-vol

In eerste-orde-benadering voldoet de rendementsvolatiliteit in het beperkte gebied aan

```{math}
:label: eq-intermediaries-hk-vol
\sigma_{R}(\eta) = \frac{\sigma_D}{1 - \tau\,\pi(\eta)\left(\frac{1}{\eta} - 1\right)},
\qquad
\pi(\eta) = \frac{\gamma\,\sigma_R(\eta)^2}{\eta}.
```

De kleinste oplossing $\sigma_R(\eta) \ge \sigma_D$ stijgt als $\eta$ daalt.
:::

:::{prf:proof}
Een daling van de log-prijs verlaagt de log-kapitaalratio met $(1/\eta - 1)$ keer zoveel, en met $\sigma_R$ lokaal vast verhoogt dat de premie met $\pi$ keer die daling. Die hogere premie verlaagt de log-prijs met $\tau$ keer zoveel. Oplossen van $\mathrm{d}\log p = \mathrm{d}\log D + \tau\pi(1/\eta - 1)\,\mathrm{d}\log p$ geeft [](#eq-intermediaries-hk-vol). De rechterkant stijgt in $\sigma_R$ en in $1/\eta$, zodat itereren vanaf $\sigma_D$ naar het kleinste vaste punt leidt, en dat punt ligt hoger naarmate $\eta$ lager is. $\square$
:::

De volatiliteit is dus de dividendvolatiliteit gedeeld door één min de lusversterking
$\tau\pi(1/\eta - 1)$. Onder een kritieke kapitaalratio is die versterking één of meer, en
bestaat er geen eindige oplossing. We lossen [](#eq-intermediaries-hk-vol) op voor $\gamma = 2$,
$\sigma_D = 12\%$ en $\tau = 0{,}25$ jaar, met een restrictie die onder $\bar\eta = 0{,}5$
gaat binden. Deze $\eta$ is het deel van de activa dat met eigen vermogen is gefinancierd,
niet de beurswaarde-ratio van de dealers, dus de vorm van de curve telt en niet het
niveau.

```{code-cell} ipython3
def hk_premium_vol(eta, gamma=2.0, sigma_d=0.12, tau=0.25, eta_bar=0.5, max_iter=5000):
    """Smallest fixed point of the first-order He-Krishnamurthy amplification (premium, volatility)."""
    eta_eff, sigma = min(eta, eta_bar), sigma_d
    for _ in range(max_iter):
        premium = gamma * sigma**2 / eta_eff
        loop_gain = tau * premium * (1.0 / eta_eff - 1.0) if eta < eta_bar else 0.0
        if loop_gain >= 1.0:
            return np.nan, np.nan
        new = sigma_d / (1.0 - loop_gain)
        if abs(new - sigma) < 1e-12:
            return gamma * new**2 / eta_eff, new
        sigma = new
    return np.nan, np.nan


eta_grid = np.linspace(0.10, 1.0, 361)
hk_curve = pd.DataFrame([hk_premium_vol(e) for e in eta_grid], index=eta_grid, columns=["premie", "volatiliteit"])
eta_crit = hk_curve["premie"].first_valid_index()
print(f"kritieke kapitaalratio (eerste eindige oplossing op het rooster): {eta_crit:.3f}")
hk_curve.iloc[[int(np.abs(eta_grid - e).argmin()) for e in (1.0, 0.5, 0.4, 0.3, 0.25, 0.2)]].round(3)
```

Onder een kapitaalratio van 0,198 bestaat er geen eindige oplossing meer. De figuur laat
zien hoe ver de getrokken premie uitstijgt boven de premie zonder versterking.

```{code-cell} ipython3
:label: cel-intermediaries-hk
:tags: [hide-input]

fig, ax = plt.subplots()
ax.plot(hk_curve.index, 100 * hk_curve["premie"], color=hap.plotting.COLORS[0], label="risicopremie $\\pi(\\eta)$")
ax.plot(hk_curve.index, 100 * hk_curve["volatiliteit"], color=hap.plotting.COLORS[1], label="volatiliteit $\\sigma_R(\\eta)$")
ax.plot(hk_curve.index, 100 * 2 * 0.12**2 / np.minimum(hk_curve.index, 0.5), color=hap.plotting.COLORS[7], ls="--",
        label="premie zonder versterking, $\\gamma\\sigma_D^2/\\eta$")
ax.axvline(0.5, color="black", lw=0.8, ls=":")
ax.axvline(eta_crit, color="black", lw=0.8, ls="--")
ax.set_ylim(0, 40)
ax.set_title("Risicopremie en volatiliteit als functie van de kapitaalratio")
ax.set_xlabel("Kapitaalratio $\\eta$ (stippel: restrictie gaat binden)")
ax.set_ylabel("Procent per jaar")
ax.legend()
plt.show()
```

:::{figure} #cel-intermediaries-hk
:label: fig-intermediaries-hk
:width: 90%

Rechts van $\bar\eta = 0{,}5$ zijn premie en volatiliteit constant. Links daarvan stijgt de premie eerst ongeveer als $1/\eta$ en daarna veel sneller, omdat de volatiliteit toeneemt. Onder de gestreepte lijn bestaat in deze benadering geen evenwicht meer, wat het model van een crash is.
:::

Halveert de kapitaalratio van $\eta = 0{,}4$ tot $0{,}2$, dan stijgt de premie van 7,6% naar
27,1%, veel meer dan de verdubbeling die bij evenredigheid hoort. De premie groeit dus
sneller dan $1/\eta$, wat {cite:t}`HeKrishnamurthy2013` de niet-lineariteit van
crisispremies noemen.

### Wat het voorspelt: een factormodel

Uit het marginale nut van de intermediair volgt een factormodel met de markt en de groei
van de kapitaalratio. *Waar komt dat vandaan?* Een intermediair die een activum koopt
dat slecht rendeert wanneer zijn vermogen krimpt, verliest op het slechtste moment. Hij
koopt het daarom alleen tegen een lagere prijs, zodat het verwachte rendement stijgt.
Omdat zijn vermogen het totale vermogen maal zijn aandeel daarin is, krijgen een daling
van het totale vermogen en een daling van dat aandeel elk een eigen beloning.

He, Kelly en Manela (hierna HKM) schrijven het vermogen van de intermediair als $\eta_t W_t$,
met $W_t$ het totale vermogen. Omdat de intermediair in het model alle activa houdt, is zijn
eigen vermogen gedeeld door de activa, de kapitaalratio $\eta_t = E_t/A_t$, ook zijn aandeel
in het totale vermogen. Met consumptie evenredig met vermogen is de SDF dan

```{math}
:label: eq-intermediaries-sdf
m_{t+1} = \beta\left(\frac{\eta_{t+1}W_{t+1}}{\eta_t W_t}\right)^{-\gamma}
\approx a - \gamma\,\frac{\Delta W_{t+1}}{W_t} - \gamma\,\eta^{\Delta}_{t+1},
```

zodat een dollar het meest waard is als de markt en de kapitaalratio allebei dalen. De
factor $\eta^\Delta_{t+1} = u_{t+1}/\eta_t$ is de innovatie uit een AR(1) voor de
kapitaalratio, gedeeld door de vorige ratio. HKM rapporteren een AR(1)-coëfficiënt van
0,94 per kwartaal. Met de bèta-representatie uit [](#02-08-capm), die een lineaire SDF
omzet in premies evenredig met bèta's, wordt [](#eq-intermediaries-sdf)

```{math}
:label: eq-intermediaries-twee-factor
\E[R^e_{i}] = \beta_{i,W}\,\lambda_W + \beta_{i,\eta}\,\lambda_\eta,
\qquad \lambda_W > 0,\ \lambda_\eta > 0 .
```

Het verwachte overrendement is dus een beloning voor de bèta op de markt plus een beloning
voor de bèta op de kapitaalratio, en beide prijzen zijn positief. Dat is de voorspelling
uit de intuïtie, met als extra eis dat $\lambda_\eta$ in elke activaklasse gelijk is.

Adrian, Etula en Muir (hierna AEM) kozen de leverage als toestandsvariabele. De
schaduwprijs van de financieringsrestrictie is volgens hen hoog wanneer de leverage laag
is, omdat intermediairs dan onder dwang hun balans hebben ingekrompen. Hun SDF is $m_{t+1} = 1 - b\,\mathrm{LevFac}_{t+1}$
met $b > 0$, waarin $\mathrm{LevFac}$ de verandering in de log-leverage van broker-dealers
is, in het laatste kwartaal van 2008 bijvoorbeeld $-0{,}35$. Ook bij hen is de prijs van
leverage-risico positief.

Hier zit een puzzel, want leverage is het omgekeerde van de kapitaalratio, en toch krijgen
schokken in allebei een positieve prijs. Twee verschillen maken de resultaten verenigbaar.
AEM meten de boekleverage uit de Flow of Funds, die volgens {cite:t}`AdrianShin2010` sterk
procyclisch is, omdat dealers hun balans laten krimpen als prijzen dalen. HKM meten het
eigen vermogen tegen beurswaarde, en die daalt in een crisis veel sneller. Bovendien bevat
de Flow of Funds alleen de broker-dealeractiviteiten, terwijl HKM de beursgenoteerde
moederbedrijven nemen. Beide maten kunnen dus in dezelfde slechte toestand dalen, net als
in het toy-voorbeeld.

```{admonition} Samengevat
:class: tip

- Markt- en financieringsliquiditeit versterken elkaar, zodat één markt liquide of illiquide kan zijn ([](#eq-intermediaries-bp-vastpunt)). De multiplier stijgt met de positie $x_0$ en de margegevoeligheid $\theta$, omdat beide een korting in minder koopkracht omzetten ([](#eq-intermediaries-bp-multiplier)).
- Bij een bindende restrictie is de premie omgekeerd evenredig met de kapitaalratio, omdat elke dollar eigen vermogen dan meer risico draagt, en ze stijgt met $\gamma$, omdat de bankiers per eenheid risico meer beloning vragen ([](#eq-intermediaries-hk-premie)).
- Omdat de volatiliteit meestijgt, groeit de premie sneller dan $1/\eta$, van 5,8% bij $\eta = 0{,}5$ tot 27,1% bij $\eta = 0{,}2$ ([](#eq-intermediaries-hk-vol)).
- De SDF van de intermediair geeft twee positieve prijzen van risico, voor de markt en de kapitaalratio ([](#eq-intermediaries-twee-factor)).
- Leverage tegen boekwaarde en kapitaalratio tegen beurswaarde kunnen in dezelfde slechte toestand allebei dalen, zodat zowel de factor van AEM als die van HKM een positieve prijs krijgt.
```

## Simulatie: ziet een factortoets de prijs van intermediairrisico?

Stel dat het model waar is. Hoe vaak geeft een tweestapstoets op vijftig jaar kwartaaldata
dan een significante $\lambda_\eta$? Zo'n toets schat eerst per portefeuille de bèta's en
regresseert daarna per kwartaal de rendementen op die bèta's, zoals bij Fama en MacBeth.
De standaardfouten van Shanken corrigeren ervoor dat de bèta's zelf geschat zijn.

We simuleren 35 portefeuilles waarvan de intermediairbèta's gemiddeld 0,07 zijn, met een
standaarddeviatie van 0,11, zoals HKM voor de 25 Fama-French-portefeuilles rapporteren.
Elke portefeuille krijgt een kleine vaste *pricing error* (een afwijking die
geen factor verklaart). We variëren de ware $\lambda_\eta$ van 0 tot 7% per kwartaal, en
voegen een *nutteloze factor* toe die met geen enkel rendement samenhangt
{cite}`KanZhang1999`.

```{code-cell} ipython3
def two_pass_arrays(R, F):
    """Two-pass OLS with intercept on arrays: prices of risk, Fama-MacBeth and Shanken (1992) standard errors."""
    # TODO: naar hap.stats (Shanken-correctie voor meerdere factoren in fama_macbeth)
    T, N = R.shape
    betas = np.linalg.lstsq(np.column_stack([np.ones(T), F]), R, rcond=None)[0][1:].T
    Z = np.column_stack([np.ones(N), betas])
    gammas = np.linalg.lstsq(Z, R.T, rcond=None)[0].T
    lam = gammas.mean(axis=0)
    V_fm = np.cov(gammas, rowvar=False) / T
    Sigma_f = np.atleast_2d(np.cov(F, rowvar=False))
    c = lam[1:] @ np.linalg.solve(Sigma_f, lam[1:])
    border = np.zeros_like(V_fm)
    border[1:, 1:] = Sigma_f / T
    V_sh = (1.0 + c) * (V_fm - border) + border
    return lam, np.sqrt(np.diag(V_fm)), np.sqrt(np.clip(np.diag(V_sh), 0.0, None)), betas, Z


def simulate_factor_test(lam_eta, n_sim=1000, T=200, N=35, useless=False):
    """Share of samples with |t| > 1.96 for the intermediary factor in a two-pass test."""
    t_stats, estimates = np.empty((n_sim, 2)), np.empty(n_sim)
    for s in range(n_sim):
        b_m, b_eta = rng.normal(1.0, 0.2, N), rng.normal(0.07, 0.11, N)
        f_m, f_eta = rng.normal(0.015, 0.09, T), rng.normal(0.0, 0.12, T)
        alpha = rng.normal(0.0, 0.005, N)
        R = alpha + 0.015 * b_m + np.outer(f_m - 0.015, b_m) + rng.normal(0.0, 0.04, (T, N))
        if not useless:
            R += lam_eta * b_eta + np.outer(f_eta, b_eta)
        lam, se_fm, se_sh, _, _ = two_pass_arrays(R, np.column_stack([f_m, f_eta]))
        estimates[s], t_stats[s] = lam[2], (lam[2] / se_fm[2], lam[2] / se_sh[2])
    return {"gem. schatting (% p.k.)": 100 * estimates.mean(), "sd schatting (% p.k.)": 100 * estimates.std(),
            "P(|t FM| > 1,96)": np.mean(np.abs(t_stats[:, 0]) > 1.96),
            "P(|t Shanken| > 1,96)": np.mean(np.abs(t_stats[:, 1]) > 1.96)}


power = {f"ware lambda {100 * lam:.0f}%": simulate_factor_test(lam) for lam in (0.0, 0.01, 0.02, 0.03, 0.05, 0.07)}
power["nutteloze factor"] = simulate_factor_test(0.0, useless=True)
power_table = pd.DataFrame(power).T
power_table.round(3)
```

De toets ziet een ware prijs pas bij enkele procenten per kwartaal betrouwbaar, en de
gestreepte lijn in de figuur laat zien dat de nutteloze factor ver boven de nominale 5%
uitkomt.

```{code-cell} ipython3
:label: cel-intermediaries-kracht
:tags: [hide-input]

true_lams = [0, 1, 2, 3, 5, 7]
fig, ax = plt.subplots()
ax.plot(true_lams, power_table["P(|t Shanken| > 1,96)"].iloc[:6], "o-", color=hap.plotting.COLORS[0],
        label="ware factor, Shanken")
ax.axhline(power_table.loc["nutteloze factor", "P(|t Shanken| > 1,96)"], color=hap.plotting.COLORS[1], ls="--",
           label="nutteloze factor, Shanken")
ax.axhline(0.05, color="black", lw=0.8, ls=":", label="nominaal 5%")
ax.set_title("Kans op een significante prijs van intermediairrisico in 50 jaar kwartaaldata")
ax.set_xlabel("Ware prijs van risico $\\lambda_\\eta$ (% per kwartaal)")
ax.set_ylabel("Fractie steekproeven met |t| > 1,96")
ax.legend()
plt.show()
```

:::{figure} #cel-intermediaries-kracht
:label: fig-intermediaries-kracht
:width: 90%

Een prijs van risico van de omvang die HKM rapporteren (7 tot 9% per kwartaal) is in vijftig jaar vrijwel altijd te zien, een prijs van 2% maar in de helft van de steekproeven. Een factor die met geen enkel rendement samenhangt, krijgt in ruim een kwart van de steekproeven toch een significante prijs.
:::

Zonder ware prijs verwerpt de toets in 10% van de steekproeven in plaats van 5%, omdat de
pricing errors de nulhypothese van een perfect model schenden. Met de standaardfouten van
Shanken is de nutteloze factor in 28% van de steekproeven significant, omdat de geschatte
bèta's pure ruis zijn en de pricing errors toevallig aan die ruis worden toegeschreven.
Hier zien we [de standaardfout van 2%](#00-01-rendementen) terug in de cross-sectie, want
de standaardfout van de prijs van een niet-verhandelde factor zegt minder dan hij lijkt.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** He, Kelly & Manela, *Intermediary Asset Pricing: New Evidence from Many Asset Classes*, Journal of Financial Economics 2017 {cite}`HeKellyManela2017`. We lazen de NBER-werkversie w21920 (januari 2016).

**Wat.** De kapitaalratio van de primary dealers (figuur 1), de tweestapstoetsen van tabel 5 over 1970Q1–2012Q4 en de voorspellende kracht van de ratio (sectie 5). Op 125 portefeuilles uit zeven activaklassen vinden HKM een prijs van risico van 9% per kwartaal met een GMM-$t$ van 2,56, en 7% voor aandelen alleen.

**Data hier.** Kapitaalratio en factor via `hap.data.hkm`, de 25 size/BM- en 10 momentumportefeuilles van Kenneth French, en vijf Treasury-portefeuilles uit de Svensson-curve van `hap.data.gsw()`. Spreads en recessies komen van FRED.

**Verschil met het origineel.** Zes van de zeven activaklassen ontbreken omdat die data niet gratis zijn, en onze obligaties komen uit een geschatte curve. We voegen momentum toe, rapporteren ook 1970–2025 en schatten de GMM-versie zonder intercept.

**Verwachte afwijking.** Het minimum van de kapitaalratio moet in februari 2009 liggen, rond 2,2% ([](#00-00-setup)), en de prijs van intermediairrisico moet op aandelen positief zijn en rond 7% per kwartaal. Een negatief teken op de Fama-French-portefeuilles betekent een fout in de code, terwijl een lagere $t$ dan 2,56 te verwachten is.
```

### De kapitaalratio in de tijd

We laden de kapitaalratio en twee spreads, en berekenen het minimum, de correlaties en de
jaargemiddelden rond de crisis.

```{code-cell} ipython3
hkm_monthly = hap_data.hkm("monthly")
hkm_quarterly = hap_data.hkm("quarterly")
eta_m = hkm_monthly["intermediary_capital_ratio"]
spreads = pd.concat([hap_data.fred(s)[s].resample("ME").mean() for s in ["BAA10Y", "TEDRATE"]], axis=1, sort=True)

print(f"minimum kapitaalratio: {eta_m.min():.2%} in {eta_m.idxmin():%B %Y}")
print(f"correlatie niveau met BAA10Y: {pd.concat([eta_m, spreads['BAA10Y']], axis=1, sort=True).dropna().corr().iloc[0, 1]:.2f},"
      f" met TED-spread: {pd.concat([eta_m, spreads['TEDRATE']], axis=1, sort=True).dropna().corr().iloc[0, 1]:.2f}")
print(f"kwartaalvolatiliteit van de factor: {hkm_quarterly['intermediary_capital_risk_factor'].std():.1%}")
eta_m.resample("YE").mean().loc["2005":"2012"].rename("gemiddelde kapitaalratio").to_frame().T.round(3)
```

Het dieptepunt ligt op 2,23% in februari 2009, zoals verwacht, en het jaargemiddelde
daalde van 8,2% in 2006 naar 4,1% in 2008. In de figuur vallen de pieken in de spreads
samen met de dalen in de kapitaalratio.

```{code-cell} ipython3
:label: cel-intermediaries-kapitaalratio
:tags: [hide-input]

fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), sharex=True)
axes[0].plot(eta_m.index, 100 * eta_m, color=hap.plotting.COLORS[0])
axes[0].annotate(f"{eta_m.min():.1%}, {eta_m.idxmin():%b %Y}", (eta_m.idxmin(), 100 * eta_m.min()),
                 xytext=(15, -5), textcoords="offset points", fontsize=8)
axes[0].set_title("Kapitaalratio van de primary dealers (He-Kelly-Manela)")
axes[0].set_ylabel("Marktwaarde eigen vermogen / activa (%)")
hap.plotting.recession_shading(axes[0])
for i, (s, name) in enumerate({"BAA10Y": "Baa-spread (Baa min 10-jaarsrente)", "TEDRATE": "TED-spread"}.items()):
    axes[1].plot(spreads.index, spreads[s], color=hap.plotting.COLORS[i + 1], label=name)
axes[1].set_title("Krediet- en financieringsspreads")
axes[1].set_ylabel("Procentpunt")
axes[1].set_xlabel("Jaar")
axes[1].legend()
hap.plotting.recession_shading(axes[1])
hap.plotting.timeline_axis(axes[1], every=5)
plt.show()
```

:::{figure} #cel-intermediaries-kapitaalratio
:label: fig-intermediaries-kapitaalratio
:width: 100%

De kapitaalratio daalt in bijna elke recessie, en nergens zo diep als in 2008–2009, toen de spreads hun hoogste niveau van de steekproef bereikten. De dip rond 1998 valt samen met LTCM, zonder recessie.
:::

Het niveau van de kapitaalratio correleert met $-0{,}33$ met de Baa-spread en met
$-0{,}14$ met de TED-spread. Lage kapitaalratio's gaan dus samen met hoge spreads, maar
het verband is niet mechanisch.

### Broker-dealer-leverage uit de Flow of Funds

```{admonition} Replicatie
:class: seealso

**Bron.** Adrian, Etula & Muir, *Financial Intermediaries and the Cross-Section of Asset Returns*, Journal of Finance 2014 {cite}`AdrianEtulaMuir2014`. We lazen Federal Reserve Bank of New York Staff Report 464 (september 2013).

**Wat.** Hun eenfactormodel verklaart de rendementen van size/BM-, momentum- en obligatieportefeuilles met een $R^2$ van 77%, tegen een aangepaste $R^2$ van 10% voor het CAPM. In de werkversie (tabel III, 1968Q1–2009Q4) is de prijs van leverage-risico 62% per jaar.

**Data hier.** Activa en schulden van Security Brokers and Dealers uit de Flow of Funds, per kwartaal via `hap.data.fred(...)`. De factor is de verandering in de log-leverage, gecorrigeerd voor kwartaalgemiddelden.

**Verschil met het origineel.** De Flow of Funds is sinds 2013 herzien. Onze seizoenscorrectie gebruikt bovendien de hele steekproef, zodat ze vooruitkijkt.

**Verwachte afwijking.** De boekleverage moet in 2008–2009 sterk dalen terwijl ook de kapitaalratio van HKM daalt, en de prijs van leverage-risico moet positief zijn. Een $R^2$ van 77% halen we waarschijnlijk niet.
```

We bouwen de boekleverage uit de Flow of Funds en zetten de crisiskwartalen naast de maten
van HKM.

```{code-cell} ipython3
assets_bd = hap_data.fred("BOGZ1FL664090005Q")["BOGZ1FL664090005Q"]
liabilities_bd = hap_data.fred("BOGZ1FL664190005Q")["BOGZ1FL664190005Q"]
book_leverage = assets_bd / (assets_bd - liabilities_bd)
book_leverage.index = book_leverage.index + pd.offsets.QuarterEnd(0)      # FRED stamps the quarter start
dlog_lev = np.log(book_leverage).diff().loc["1968":]
lev_factor = (dlog_lev - dlog_lev.groupby(dlog_lev.index.quarter).transform("mean") + dlog_lev.mean()).rename("lev")
eta_factor = hkm_quarterly["intermediary_capital_risk_factor"].rename("eta")
eta_q = hkm_quarterly["intermediary_capital_ratio"]

crisis = pd.concat([book_leverage.rename("boekleverage (FoF)"), lev_factor.rename("AEM-factor"),
                    eta_q.rename("kapitaalratio (HKM)"), (1 / eta_q).rename("marktleverage (HKM)"),
                    eta_factor.rename("HKM-factor")], axis=1, sort=True)
changes = pd.concat([np.log(book_leverage).diff(), np.log(1 / eta_q).diff()], axis=1, sort=True).dropna()
print(f"correlatie AEM-factor en HKM-factor: {crisis[['AEM-factor', 'HKM-factor']].dropna().corr().iloc[0, 1]:.2f}")
print(f"correlatie log-veranderingen boekleverage (FoF) en marktleverage (HKM): {changes.corr().iloc[0, 1]:.2f}")
crisis.loc["2007-06":"2009-12"].round(3)
```

De boekleverage van de broker-dealers halveerde van 47,0 in het eerste kwartaal van 2008
naar 22,6 eind 2009, het procyclische patroon van {cite:t}`AdrianShin2010`. De
marktleverage van de primary dealers steeg intussen van 22 naar een piek van 38 eind 2008,
bijna een verdubbeling, en viel eind 2009 terug tot 19,8.

Toch zijn beide factoren in het vierde kwartaal van 2008 sterk negatief, met $-0{,}35$
voor AEM en $-0{,}44$ voor HKM, zodat ze in het slechtste kwartaal dezelfde kant op
wijzen. Over de hele steekproef is hun correlatie met 0,06 bijna nul. Ze meten hetzelfde
begrip op een andere manier, en als factoren zijn ze toch bijna onafhankelijk.

### De cross-sectie

We schatten elk model op twee manieren, met de tweestapstoets uit de simulatie en met een
GMM-schatting van de SDF $m = 1 - (\mathbf{f} - \E\mathbf{f})^\top\mathbf{b}$ zonder
intercept. Daarin is $\boldsymbol{\lambda} = \Cov(\mathbf{f})\,\mathbf{b}$, en de
gewichten zijn van Newey-West met twee lags. De Treasury-portefeuilles zijn
houdrendementen van zero-coupon-obligaties uit de Svensson-curve. Het rendement op een
obligatie met looptijd $n$ jaar is de prijs een maand later,
$e^{-(n-1/12)\,y_{t+1}(n-1/12)}$,
gedeeld door de prijs nu, $e^{-n\,y_t(n)}$, min één.

```{code-cell} ipython3
gsw = hap_data.gsw()
svensson = gsw[["BETA0", "BETA1", "BETA2", "BETA3", "TAU1", "TAU2"]].dropna(subset=["BETA0", "TAU1"]).resample("ME").last()
svensson = svensson.fillna({"BETA3": 0.0, "TAU2": 1.0})


def svensson_yield(par, maturity):
    """Continuously compounded zero-coupon yield from Svensson parameters (decimals, maturity in years)."""
    x1, x2 = maturity / par["TAU1"], maturity / par["TAU2"]
    s1, s2 = (1 - np.exp(-x1)) / x1, (1 - np.exp(-x2)) / x2
    return par["BETA0"] + par["BETA1"] * s1 + par["BETA2"] * (s1 - np.exp(-x1)) + par["BETA3"] * (s2 - np.exp(-x2))


bond_returns = pd.DataFrame({
    f"OBL {n}j": np.exp(-(n - 1 / 12) * svensson_yield(svensson, n - 1 / 12).shift(-1) + n * svensson_yield(svensson, n)).shift(1) - 1
    for n in (1, 2, 3, 4, 5)
})

ff3 = hap_data.french("F-F_Research_Data_Factors")
momentum_factor = hap_data.french("F-F_Momentum_Factor")
size_bm = hap_data.french("25_Portfolios_5x5")
momentum_dec = hap_data.french("10_Portfolios_Prior_12_2").add_prefix("MOM ")
monthly = pd.concat([size_bm, momentum_dec, bond_returns, ff3, momentum_factor], axis=1, sort=True).dropna(subset=["RF"])


def to_quarterly(frame):
    """Compound monthly simple returns to quarters; quarters with missing months become NaN."""
    return ((1 + frame).resample("QE").prod() - 1).where(frame.resample("QE").count() == 3)


quarterly = to_quarterly(monthly)
cols_25, cols_mom, cols_bond = list(size_bm.columns), list(momentum_dec.columns), list(bond_returns.columns)
excess_q = quarterly[cols_25 + cols_mom + cols_bond].sub(quarterly["RF"], axis=0)
factors_q = pd.DataFrame({"Mkt": to_quarterly(ff3["Mkt-RF"] + ff3["RF"]) - quarterly["RF"],
                          "SMB": to_quarterly(ff3["SMB"]), "HML": to_quarterly(ff3["HML"]),
                          "Mom": to_quarterly(momentum_factor["Mom"])})
factors_q = pd.concat([factors_q, eta_factor, lev_factor], axis=1, sort=True)
print(f"correlatie HKM-factor met het marktrendement: {factors_q[['eta', 'Mkt']].dropna().corr().iloc[0, 1]:.2f}")
excess_q.loc["1970":].describe().loc[["count", "mean", "std"]].T.groupby(lambda c: c.split()[0]).mean().round(4)
```

De HKM-factor correleert met 0,76 met het marktrendement, een getal waarop we aan het eind
terugkomen. De volgende cel schat alle modellen op drie combinaties van testactiva en
steekproef.

```{code-cell} ipython3
def two_pass(excess, factors):
    """Two-pass test with intercept on DataFrames; returns prices of risk, Shanken t, R2, MAPE and pricing errors."""
    data = pd.concat([excess, factors], axis=1, sort=True).dropna()
    R, F = data[excess.columns].to_numpy(), data[factors.columns].to_numpy()
    lam, _, se_sh, _, Z = two_pass_arrays(R, F)
    errors = R.mean(axis=0) - Z @ lam
    names = ["const", *factors.columns]
    return {"T": len(R), "lam": pd.Series(lam, names), "t_shanken": pd.Series(lam / se_sh, names),
            "r2": 1 - errors.var() / R.mean(axis=0).var(), "mape": np.abs(errors).mean(),
            "mean": pd.Series(R.mean(axis=0), excess.columns), "fitted": pd.Series(Z @ lam, excess.columns)}


def gmm_sdf(excess, factors, lags=2):
    """First-stage GMM for m = 1 - (f - E f)'b with the factor means as extra moments (Cochrane 2005, ch. 13)."""
    # TODO: naar hap.stats (GMM-schatting van een lineaire SDF)
    data = pd.concat([excess, factors], axis=1, sort=True).dropna()
    R, F = data[excess.columns].to_numpy(), data[factors.columns].to_numpy()
    T, N = R.shape
    K = F.shape[1]
    F_dm = F - F.mean(axis=0)
    D, mean_R = R.T @ F_dm / T, R.mean(axis=0)
    b = np.linalg.lstsq(D, mean_R, rcond=None)[0]
    u = np.column_stack([R * (1 - F_dm @ b)[:, None], F_dm])
    u = u - u.mean(axis=0)
    S = u.T @ u / T
    for j in range(1, lags + 1):
        gamma_j = u[j:].T @ u[:-j] / T
        S += (1 - j / (lags + 1)) * (gamma_j + gamma_j.T)
    # d: Jacobian of the N pricing moments and K mean moments w.r.t. (b, E f);
    # a: first-stage selection, D' on the pricing moments and the identity on the mean moments
    d = np.block([[-D, mean_R[:, None] * b[None, :]], [np.zeros((K, K)), -np.eye(K)]])
    a = np.block([[D.T, np.zeros((K, K))], [np.zeros((K, N)), np.eye(K)]])
    ad_inv = np.linalg.inv(a @ d)
    V = ad_inv @ a @ S @ a.T @ ad_inv.T / T
    Sigma_f = np.atleast_2d(np.cov(F, rowvar=False, bias=True))
    lam = Sigma_f @ b
    se_lam = np.sqrt(np.diag(Sigma_f @ V[:K, :K] @ Sigma_f))
    errors = mean_R - D @ b
    return {"lam": pd.Series(lam, factors.columns), "t": pd.Series(lam / se_lam, factors.columns),
            "r2": 1 - (errors**2).sum() / ((mean_R - mean_R.mean())**2).sum()}


MODELS = {"CAPM": ["Mkt"], "FF3": ["Mkt", "SMB", "HML"], "Carhart": ["Mkt", "SMB", "HML", "Mom"],
          "HKM": ["Mkt", "eta"], "AEM": ["lev"]}
TEST_SETS = [("FF25, 1970–2012", "1970", "2012", cols_25),
             ("25+10+5 obl., 1970–2012", "1970", "2012", cols_25 + cols_mom + cols_bond),
             ("25+10+5 obl., 1970–2025", "1970", "2025", cols_25 + cols_mom + cols_bond)]

rows, fits = {}, {}
for label, start, end, cols in TEST_SETS:
    for model, fcols in MODELS.items():
        R_s, F_s = excess_q.loc[start:end, cols], factors_q.loc[start:end, fcols]
        tp, gm = two_pass(R_s, F_s), gmm_sdf(R_s, F_s)
        key = {"HKM": "eta", "AEM": "lev"}.get(model)
        rows[(label, model)] = {
            "kwartalen": tp["T"],
            "λ interm. (% p.k.)": 100 * tp["lam"][key] if key else np.nan,
            "t Shanken": tp["t_shanken"][key] if key else np.nan,
            "λ GMM (% p.k.)": 100 * gm["lam"][key] if key else np.nan,
            "t GMM": gm["t"][key] if key else np.nan,
            "R² twee stappen": tp["r2"], "MAPE (% p.k.)": 100 * tp["mape"], "R² GMM": gm["r2"],
        }
        fits[(label, model)] = tp
cross_section = pd.DataFrame(rows).T
cross_section.round(2)
```

In het HKM-model is de prijs van intermediairrisico in elke specificatie positief. De
tabel hieronder zet de kern naast het origineel.

| grootheid | origineel | hier |
|---|---|---|
| minimum kapitaalratio | rond 2,2%, februari 2009 | 2,23%, februari 2009 |
| $\lambda_\eta$ op FF25, GMM, 1970–2012 (% per kwartaal) | 7 (aandelen) | 6,96 ($t = 3{,}10$) |
| $\lambda_\eta$ op alle testactiva, GMM, 1970–2012 (% per kwartaal) | 9 ($t = 2{,}56$) | 4,94 ($t = 2{,}44$) |
| $R^2$ op FF25, HKM tegen CAPM | hoger dan CAPM | 0,44 tegen 0,09 |
| prijs van leverage-risico (AEM), alle testactiva | 62% per jaar | 8,79% per kwartaal (Shanken-$t$ 2,08) |
| $R^2$ van AEM | 77% | 0,41 |

De replicatie is gedeeltelijk geslaagd, want het dieptepunt ligt waar het moet liggen en
het teken is overal positief. Op aandelen komt de GMM-schatting bovendien vrijwel precies
op de 7% van HKM uit, al is de tweestapsschatting met intercept op FF25 lager, 4,98% met
een Shanken-$t$ van 1,61.

Op alle testactiva ligt onze GMM-schatting onder de 9% van HKM en is de $t$ iets lager, wat
binnen de verwachte afwijking valt, want zes activaklassen ontbreken en onze obligaties
komen uit een geschatte curve. Of obligaties dezelfde prijs krijgen als aandelen, toetsen
we niet apart, want de vijf obligatieportefeuilles zitten alleen in de gemengde testset.
Ook de AEM-factor krijgt een positieve prijs, maar lager dan de 62% per jaar van AEM, en hij haalt
maar ruim de helft van de gepubliceerde $R^2$.

De figuur zet voor drie modellen de gemiddelde rendementen uit tegen de voorspelling, en
vooral bij de momentumportefeuilles lopen de modellen uiteen.

```{code-cell} ipython3
:label: cel-intermediaries-cross
:tags: [hide-input]

fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), sharex=True, sharey=True)
groups = {"size/BM": cols_25, "momentum": cols_mom, "obligaties": cols_bond}
for ax, model in zip(axes, ["CAPM", "HKM", "Carhart"], strict=True):
    fit = fits[("25+10+5 obl., 1970–2025", model)]
    for i, (group, cols) in enumerate(groups.items()):
        ax.scatter(100 * fit["fitted"][cols], 100 * fit["mean"][cols], s=18, color=hap.plotting.COLORS[i], label=group)
    ax.plot([-0.5, 4.5], [-0.5, 4.5], color="black", lw=0.8)
    ax.set_title(f"{model}: $R^2$ = {fit['r2']:.2f}")
    ax.set_xlabel("Voorspeld (% per kwartaal)")
axes[0].set_ylabel("Gerealiseerd gemiddelde (% per kwartaal)")
axes[0].legend()
fig.tight_layout()
plt.show()
```

:::{figure} #cel-intermediaries-cross
:label: fig-intermediaries-cross
:width: 100%

Gemiddelde kwartaalrendementen 1970–2025 tegen de voorspelling van drie modellen. Het HKM-model trekt de size/BM-portefeuilles in de goede richting, maar laat de momentumportefeuilles als een verticale wolk staan. Carhart, met een factor die op momentum gesorteerd is, legt die wolk op de lijn.
:::

Met momentum- en obligatieportefeuilles erbij daalt de $R^2$ van het HKM-model over
1970–2012 naar 0,22, ver onder Carhart (0,85). Het model verklaart momentum dus niet
(oefening 3). Dat de AEM-factor het slechter doet dan in het artikel, kan aan de
obligaties liggen, aan de herziene Flow of Funds of aan de seizoenscorrectie, en met
gratis data kunnen we dat niet uitmaken.

### Voorspelt de kapitaalratio rendementen en spreads?

HKM rapporteren dat de kapitaalratio toekomstige rendementen voorspelt in vijf van de
zeven activaklassen. We regresseren het overrendement van de markt over $h$ maanden, en de
verandering in de Baa-spread, op het niveau van de kapitaalratio. Omdat de ratio
persistent is en de horizonnen overlappen, gebruiken we de standaardfouten van
{cite:t}`Hodrick1992` (variant 1B). Daarbovenop komt nog de Stambaugh-bias uit
[](#04-20-voorspelbaarheid).

```{code-cell} ipython3
def hodrick_1b(y, x, horizon):
    """Regress y_{t+1} + ... + y_{t+h} on x_t; Hodrick (1992) 1B standard errors under no predictability."""
    # TODO: naar hap.stats (method="hodrick-1b" in long_horizon_regression)
    frame = pd.concat([y.rename("y"), x.rename("x")], axis=1, sort=True).dropna()
    r, z = frame["y"].to_numpy(), frame["x"].to_numpy()
    T = len(r)
    target = np.convolve(r, np.ones(horizon), "valid")[1:]
    n = len(target)
    X = np.column_stack([np.ones(n), z[:n]])
    coef = np.linalg.lstsq(X, target, rcond=None)[0]
    shocks = r[1:] - r[1:].mean()
    cum = np.vstack([np.zeros(2), np.cumsum(np.column_stack([np.ones(T), z]), axis=0)])
    idx = np.arange(horizon - 1, T - 1)
    rolled = cum[idx + 1] - cum[idx + 1 - horizon]            # x_t + ... + x_{t-h+1}
    S = (rolled * shocks[idx, None] ** 2).T @ rolled / n
    Q_inv = np.linalg.inv(X.T @ X / n)
    V = Q_inv @ S @ Q_inv / n
    resid = target - X @ coef
    return {"helling": coef[1], "t (Hodrick 1B)": coef[1] / np.sqrt(V[1, 1]), "R²": 1 - resid.var() / target.var(),
            "waarnemingen": n}


market_m = ff3["Mkt-RF"].loc["1970":]
baa_change = spreads["BAA10Y"].diff() / 100
predict = {("marktrendement", h): hodrick_1b(market_m, eta_m, h) for h in (1, 12, 24, 36)}
predict.update({("verandering Baa-spread", h): hodrick_1b(baa_change, eta_m, h) for h in (1, 12, 24)})
pd.DataFrame(predict).T.rename_axis(["te voorspellen", "horizon (maanden)"]).round(3)
```

Het teken klopt, want een kapitaalratio die één procentpunt lager ligt, gaat samen met een
marktrendement dat over drie jaar 4,1 procentpunt hoger ligt, en met een dalende
Baa-spread. Toch haalt geen van de $t$-waarden de 1,96, want voor de markt zijn ze
$-1{,}36$ op een jaar en $-1{,}43$ op drie jaar. In 55 jaar zit maar een handvol crises,
en de voorspellende kracht rust op dezelfde paar episodes die de kapitaalratio
laag maakten.

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Intermediary asset pricing gaf 2008 een mechanisme dat
consumptiemodellen missen, met gedwongen verkopen, oplopende marges en een marginale
belegger wiens kapitaal in een paar kwartalen verdwijnt. Het verklaart waarom liquiditeit
overal tegelijk opdroogt en waarom premies niet-lineair stijgen en snel terugvallen. Ook
verklaart het waarom identieke kasstromen verschillende prijzen kregen, want bij
{cite:t}`GarleanuPedersen2011` hangt het vereiste rendement ook af van de marge. Daarnaast
beschreven {cite:t}`MitchellPulvino2012` hoe hedgefondsen na de val van hun prime brokers
gelijke activa niet meer op gelijke prijzen konden houden. In onze data heeft het model
in elk geval het teken goed.

**Waar het breekt.** Het model loopt vast op de meting. Leverage en kapitaalratio zijn
elkaars omgekeerde, maar krijgen allebei een positieve prijs, en als factoren zijn ze bijna
ongecorreleerd. De $R^2$ van AEM halen we met de huidige Flow of Funds niet,
en het HKM-model laat momentum liggen. De HKM-factor correleert bovendien met 0,76 met het
marktrendement, zodat een deel van zijn succes de bèta van dealeraandelen kan zijn. Tot
slot laat [](#fig-intermediaries-kracht) zien dat een factor zonder enige samenhang met
rendementen in ruim een kwart van de steekproeven significant lijkt.

**Risico of vergissing?** In de Chicago-lezing is het marginale nut van de intermediair de
SDF, en waren de hoge premies van 2008 de rationele prijs van risico toen kapitaal schaars
was. Wie toen kocht, werd in de termen van Santa-Clara betaald voor het dragen van risico
en niet voor een inzicht dat de markt miste. In de Yale-lezing zijn dit de limits of
arbitrage van [](#04-23-behavioral) op macroschaal, en is een prijsverschil tussen
identieke kasstromen een mispricing en geen premie. Beide lezingen zijn het eens over de
kapitaalratio en de spreads. De kampen zouden te scheiden zijn door na te gaan of
kortingen terugliepen zodra er kapitaal binnenkwam, ongeacht het risico, maar de benodigde
posities zijn grotendeels niet openbaar. Santa-Clara trekt een les die
voor beide kampen geldt: hefboom, waardering tegen marktprijzen en een deadline vormen
samen het recept voor de ondergang {cite}`SantaClara2026`.

**Wat er daarna kwam.** Als voorspelbare premies die in crises exploderen zowel een
rationele discontovoet als een tijdelijke mispricing kunnen zijn, rijst de vraag wat het
vakgebied daarmee deed toen Fama en Shiller in 2013 samen de Nobelprijs kregen. Die vraag
behandelt [](#05-33-fama-vs-shiller).

## Oefeningen

:::{exercise}
:label: ex-intermediaries-1

**Een grotere schok.** Herhaal het toy-voorbeeld met een prijsdaling van 4% in plaats van 2%. De haircut blijft vast op 10%.

1. Bereken met de hand de kapitaalratio na de schok en de eerste gedwongen verkoop.
2. Laat de code de spiraal afronden. Is de versterking, de totale prijsdaling gedeeld door de schok, groter of kleiner dan bij 2%, en wat gebeurt er met het eigen vermogen?
:::

:::{solution} ex-intermediaries-1
:class: dropdown

**(1)** Het verlies is $0{,}04 \times 100 = 4$, dus $E = 6$, $A = 96$ en $\eta = 6/96 = 6{,}25\%$. De toegestane balans is $6/0{,}10 = 60$, zodat de intermediair $S_1 = 36$ verkoopt.

```{code-cell} ipython3
eta_4, rounds_4, price_4 = deleverage(E0, A0, H0, EPS * W_OUT, 0.04)
pd.DataFrame({
    "schok 2%": {"eerste verkoop": const_rounds.loc[0, "verkoop"], "eigen vermogen na afloop": const_rounds["E"].iloc[-1],
                 "prijsdaling (%)": 100 * (1 - const_price), "versterking": (1 - const_price) / SHOCK},
    "schok 4%": {"eerste verkoop": rounds_4.loc[0, "verkoop"], "eigen vermogen na afloop": rounds_4["E"].iloc[-1],
                 "prijsdaling (%)": 100 * (1 - price_4), "versterking": (1 - price_4) / 0.04},
}).round(3)
```

**(2)** De versterking daalt licht, van 1,67 naar 1,58, omdat de balans na de eerste verkoop kleiner is. Het eigen vermogen daalt daarentegen tot 4,62, een verlies van 54% tegen 31% bij de kleine schok. Bij één intermediair aan zijn grens groeit de prijsdaling dus ongeveer evenredig met de schok, en de sterke niet-lineariteit ontstaat pas als intermediairs buffers hebben, zoals bij de twintig intermediairs in de theorie.
:::

:::{exercise}
:label: ex-intermediaries-2

**De liquiditeitsspiraal ontleed.** Neem het vereenvoudigde Brunnermeier-Pedersen-model uit de theorie. Kies $K_0 = 1$, $x_0 = 8$, $h_0 = 0{,}08$, $\varepsilon = 60$ en $z = 13$.

1. Laat zien dat de liquide markt geen evenwicht is, en los voor $\theta = 0$ het evenwicht $\Delta^*$ met de hand op. Doe hetzelfde voor $x_0 = 3$.
2. Bereken met [](#eq-intermediaries-bp-multiplier) de multiplier voor $\theta = 0$ en $\theta = 0{,}5$, en controleer hem met een eindige differentie.
3. Voor welke $x_0$ wordt het evenwicht bij $\theta = 0$ instabiel?
:::

:::{solution} ex-intermediaries-2
:class: dropdown

**(1)** Omdat $z = 13 > K_0/h_0 = 12{,}5$ is $G(0) > 0$. Bij $\theta = 0$ en bindende restrictie geldt $\Delta^*(\varepsilon - x_0/h_0) = z - K_0/h_0$. Met $x_0/h_0 = 100 > 60$ is die oplossing negatief, zodat alleen het illiquide evenwicht $\Delta^* = z/\varepsilon = 0{,}2167$ overblijft. Met $x_0 = 3$ is $x_0/h_0 = 37{,}5$ en $\Delta^* = 0{,}5/22{,}5 = 0{,}0222$.

De cel zoekt het kleinste positieve vaste punt en zet de formule naast een eindige differentie.

```{code-cell} ipython3
def bp_equilibrium(z, K0, x0, h0, theta, eps):
    """Smallest positive fixed point of the simplified Brunnermeier-Pedersen map."""
    grid = np.linspace(1e-9, z / eps, 200_001)
    gap = bp_map(grid, z, K0, x0, h0, theta, eps) - grid
    k = np.flatnonzero(np.diff(np.sign(gap)) != 0)
    return optimize.brentq(lambda d: bp_map(d, z, K0, x0, h0, theta, eps) - d, grid[k[0]], grid[k[0] + 1]) if k.size else z / eps


rows = {}
for x0_ex in (8.0, 3.0):
    for theta_ex in (0.0, 0.5):
        pars = dict(K0=1.0, x0=x0_ex, h0=0.08, theta=theta_ex, eps=60.0)
        d_star = bp_equilibrium(13.0, **pars)
        h_star, K_star = 0.08 + theta_ex * d_star, max(1.0 - x0_ex * d_star, 0.0)
        loss_part = x0_ex / (60.0 * h_star) if K_star > 0 else 0.0
        margin_part = theta_ex * K_star / (60.0 * h_star**2)
        dz = 1e-4
        numeric = (bp_equilibrium(13.0 + dz, **pars) - d_star) / dz
        rows[(x0_ex, theta_ex)] = {"Delta*": d_star, "G' verlies": loss_part, "G' marge": margin_part,
                                   "multiplier formule": (1 / 60) / (1 - loss_part - margin_part),
                                   "multiplier numeriek": numeric}
pd.DataFrame(rows).T.rename_axis(["x0", "theta"]).round(4)
```

**(2)** Bij $x_0 = 8$ ligt het evenwicht in de hoek $\Delta^* = z/\varepsilon$, waar de speculanten geen kapitaal meer hebben en niets kopen, zodat de multiplier daar voor beide $\theta$ de directe impact $1/60$ is. Bij $x_0 = 3$ en $\theta = 0$ is $G' = 3/(60 \times 0{,}08) = 0{,}625$ en de multiplier $(1/60)/0{,}375 = 0{,}044$. Met $\theta = 0{,}5$ springt het evenwicht naar een korting van 16,5%, waar de lokale multiplier lager is, omdat de speculanten weinig kapitaal over hebben. De margespiraal werkt dus vooral op het niveau van de korting, en de eindige differentie bevestigt de formule.

**(3)** Bij $\theta = 0$ is $G' = x_0/(\varepsilon h_0)$, dus het evenwicht wordt instabiel zodra $x_0 > \varepsilon h_0 = 4{,}8$. Dezelfde verkoopdruk geeft dus een kleine of een catastrofale daling, afhankelijk van de positie die de speculanten al hadden.
:::

:::{exercise}
:label: ex-intermediaries-3

**Momentum en de crisis.** Herhaal de schattingen van het HKM-model met als testactiva FF25 of FF25 plus 10 momentumportefeuilles, over 1970–2006 of 1970–2025, net als in de replicatie. Wat doet momentum met de schatting, en hangt het resultaat af van 2008?
:::

:::{solution} ex-intermediaries-3
:class: dropdown

De cel herhaalt de schattingen uit de replicatie voor de vier combinaties.

```{code-cell} ipython3
rows = {}
for label, cols in [("FF25", cols_25), ("FF25 + momentum", cols_25 + cols_mom)]:
    for start, end in [("1970", "2006"), ("1970", "2025")]:
        R_s, F_s = excess_q.loc[start:end, cols], factors_q.loc[start:end, ["Mkt", "eta"]]
        tp, gm = two_pass(R_s, F_s), gmm_sdf(R_s, F_s)
        rows[(label, f"{start}–{end}")] = {"λ (% p.k.)": 100 * tp["lam"]["eta"], "t Shanken": tp["t_shanken"]["eta"],
                                           "λ GMM (% p.k.)": 100 * gm["lam"]["eta"], "t GMM": gm["t"]["eta"],
                                           "R² twee stappen": tp["r2"]}
pd.DataFrame(rows).T.round(2)
```

Vóór de crisis is de prijs ongeveer 9 tot 11% per kwartaal, met hoge GMM-$t$-waarden. Tot 2025 zakt de tweestapsschatting met momentum tot bijna nul, terwijl de GMM-schatting zonder intercept rond 5% blijft. De momentumportefeuilles spreiden sterk in gemiddeld rendement maar weinig in $\beta_\eta$, en een vrij intercept neemt dat verschil op. Het teken blijft dus in alle vier de combinaties positief, maar het niveau hangt sterk af van de jaren na 2006, van de testactiva en van de methode {cite}`LewellenNagelShanken2010`.
:::
