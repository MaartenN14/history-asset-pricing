# STYLE.md — stijlgids voor bouw-agents

`PLAN.md` regelt de **inhoud** (welke lecture, welk onderwerp, welke replicatie).
Dit document regelt de **vorm**. Wijk er niet van af zonder overleg; de reeks
moet als één boek lezen, niet als veertig losse notebooks.

Werk altijd vanuit `lectures/_template.md`. Kopieer dat bestand naar de slug uit
PLAN.md §3, vul het in, en verwijder de instructieve placeholder-tekst.

---

## 1. Vaste lecture-opbouw

De kopjes hieronder liggen vast, inclusief bewoording en volgorde. Subkopjes
(`###`) zijn vrij.

```
frontmatter (jupytext + kernelspec)
(label)=
# Titel van de lecture
{admonition} Waar we zijn in het verhaal          ← :class: important
## Overzicht                                      ← vraag, lijst, geschiedenis (§11.7)
## Intuïtie: waarom zou dit waar zijn?
## Toy-voorbeeld: <korte beschrijving>            ← begint met de imports-cel (§11.7)
## Theorie
## Simulatie: <korte beschrijving>                ← laag 2 van de trap
## Replicatie op echte data                       ← laag 3 van de trap
## Wat er brak, en wat daarna kwam
## Oefeningen
(referenties verschijnen automatisch — géén eigen kopje)
```

### Waar we zijn in het verhaal

Een `{admonition}` met `:class: important`, direct onder de titel, met precies
drie vetgedrukte onderdelen:

- **Jaartal.** Het tijdvak dat deze lecture beslaat.
- **Wat we al weten.** Twee tot vier zinnen: de theorie, de machine (data) en de
  barst uit de vorige lecture. Met een cross-ref naar die lecture.
- **Welke vraag staat open.** Eén zin, één vraag. Die vraag beantwoordt deze
  lecture.

### Overzicht

Vraag en antwoord, lijst, één alinea geschiedenis (§11.7); geen code. Noem de hoofdreferentie
met `{cite}` en zeg in één zin waarom dat werk het tijdvak definieert. Zeg ook
welk resultaat aan het eind wordt gerepliceerd.

### Intuïtie: waarom zou dit waar zijn?

Het mechanisme in gewone taal, zonder één symbool. Wie alleen deze sectie leest
moet het resultaat kunnen navertellen. Historische anekdotes horen hier, mits ze
het argument dienen.

### De didactische trap: toy → simulatie → data

**Verplicht in elke lecture.** Drie lagen, in deze volgorde, elk met een eigen
`##`-kopje:

**Laag 1 — `## Toy-voorbeeld: <beschrijving>`.** Het kleinste voorbeeld waarin
het mechanisme al zichtbaar is, en dat de lezer met pen en papier kan
narekenen. Eerst uitgewerkt in de tekst (met de getallen erbij), daarna een
korte codecel die **exact dezelfde getallen** reproduceert. Passende voorbeelden
per soort lecture:

| Onderwerp | Toy-voorbeeld |
|---|---|
| No-arbitrage, SDF, APT | twee toestanden, drie activa (het derde volgt uit de eerste twee) |
| Optieprijzen | binomiale boom van drie stappen, replicerende portefeuille per knoop |
| Lucas-boom, CCAPM | twee dividendtoestanden, Euler-vergelijking handmatig opgelost |
| Factormodellen | vijf aandelen, twee factoren, bèta's uit een 5×2-matrix |
| Microstructuur | Kyle-markt met één insider, één noise trader, één marktmaker |
| Voorspelbaarheid | drie observaties, één regressor, OLS met de hand |
| Mean-variance | drie activa, 3×3 covariantiematrix, frontier analytisch |

De codecel eindigt met een zichtbare controle dat code en handberekening
overeenkomen. Dat is geen ceremonie: het is de reden dat de lezer de rest van je
code mag vertrouwen.

**Laag 2 — `## Simulatie: <beschrijving>`.** Hetzelfde model, maar op schaal:
duizenden paden, honderden activa, of tienduizend steekproeven. Laat zien wat er
in *steekproeven* gebeurt en niet in de populatie: schattingsfout, bias
(Stambaugh, survivorship, look-ahead), datamining, de verdeling van de schatter.
Minstens één figuur. Dit is de plek waar het motief "de standaardfout van 2%" bijna altijd terugkomt.

**Laag 3 — `## Replicatie op echte data`.** Pas hier komt `hap.data` in beeld.
Begin met het replicatieblok (§6).

Waarom deze volgorde: de lezer weet na laag 1 wat *waar* is, na laag 2 wat
*meetbaar* is, en pas dan kan hij beoordelen wat een tabel op echte data
betekent. Een lecture die meteen met een regressie op French-data begint, leert
de lezer een procedure in plaats van een mechanisme.

### Theorie

Zit tussen laag 1 en laag 2. **Elke afleiding begint met een cursieve regel
"*Waarom zou dit waar zijn?*"** gevolgd door het economische argument in twee tot
vijf zinnen, en pas daarna de wiskunde. Niveau: PhD. Sla geen stappen over, maar
zeg bij elke stap waarom je hem zet.

Stellingen in `{prf:theorem}`, bewijzen in `{prf:proof}`. Een bewijs dat langer
dan een halve pagina is, hoort in een `{prf:proof}` met `:class: dropdown`.

### Wat er brak, en wat daarna kwam

Twee tot vier alinea's, met deze vier elementen expliciet:

1. **Wat het model verklaart.** Wees genereus — het heeft niet voor niets een
   tijdvak gedomineerd.
2. **Waar het breekt.** Eén concreet, meetbaar feit. Bij voorkeur het feit dat
   je hierboven zelf hebt gerepliceerd.
3. **Risico of vergissing?** Geef beide lezingen (§2). Kies niet voor
   de lezer.
4. **Wat er daarna kwam.** Eén zin, met een cross-ref naar de volgende lecture.

### Oefeningen

Twee tot vier, op problem-set-niveau: een concrete vraag met een numeriek of
analytisch antwoord, niet "denk eens na over". Bij voorkeur is er één
afleidingsoefening en één die de replicatie uitbreidt (andere steekproef, andere
sortering, robuuste standaardfouten). Elke oefening krijgt een uitwerking in een
`{solution}` met `:class: dropdown`, inclusief code én één zin die zegt wat de
oefening over het hoofdargument leert.

### Referenties

Géén eigen kopje en géén `{bibliography}`-directive. MyST zet de lijst met
geciteerde bronnen automatisch onderaan de pagina.

---

## 2. De drie rode-draadmotieven

Uit PLAN.md §2. Ze hoeven niet alle drie in elke lecture, maar wél waar ze
relevant zijn — en dat is vaker dan je denkt.

**Motief 1 — de standaardfout van 2%.** Bij $\sigma \approx 20\%$ per jaar is de
standaardfout van het gemiddelde over een eeuw ongeveer 2 procentpunt; de
variantie is daarentegen goed meetbaar. *Waar het thuishoort:* in de
simulatielaag, altijd. Elke keer dat een lecture een gemiddeld rendement schat,
staat de standaardfout erbij. Elke keer dat een lecture beweert dat iets
"voorspelbaar" is, staat erbij hoeveel data er nodig was om dat te zien. Het
verklaart de equity premium puzzle, de factor zoo, en waarom volatiliteit wél en
rendement niet te voorspellen is.

**Motief 2 — risico versus vergissing.** Chicago (tijdvariërende discontovoeten)
tegenover Yale (mispricing en limits of arbitrage). *Waar het thuishoort:* in
"Wat er brak", verplicht. Geef beide lezingen van hetzelfde feit, geef aan welke
data de kampen zou kunnen scheiden, en zeg eerlijk dat die data er meestal niet
is. Kies niet voor de lezer; de reeks kiest pas in L33 en dan nog niet echt.

**Motief 3 — van theorie-met-tests naar feiten-met-concurrerende-theorieën.**
CAPM → SDF-pluralisme → machine learning zonder theorie → flows en inelastische
markten. *Waar het thuishoort:* in "Waar we zijn in het verhaal" en in
"Overzicht". Benoem telkens wat de *epistemische* status van het model is: is dit
een theorie die getoetst wordt, of een feit dat op een verklaring wacht?

**Praktijkmotief (Santa-Clara).** *"Everything I made that lasted came from
bearing risk that was priced. Everything I lost came from thinking I knew
something the price did not."* Roep dit aan waar een lecture over een strategie
gaat: is dit een risicopremie of een vermeend inzicht?

---

## 3. Notatie

Alle lectures delen deze notatie. Wijk er niet van af; als het originele paper
andere symbolen gebruikt, vertaal je naar deze tabel en zeg je dat in één zin.

| Symbool | Betekenis |
|---|---|
| $m_{t+1}$ | stochastic discount factor (SDF), $m_{t+1} = \beta u'(c_{t+1})/u'(c_t)$ |
| $R_{t+1}$ | bruto rendement, $R = 1 + r$ |
| $r_{t+1}$ | netto rendement; **kleine letter = log** waar dat is aangekondigd |
| $R^{e}_{t+1}$ | excess rendement, $R^{e} = R - R^{f}$ |
| $R^{f}_{t+1}$ | bruto risicovrij rendement, bekend op $t$ |
| $p_t$ | prijs op $t$ |
| $x_{t+1}$ | payoff op $t+1$; $R_{t+1} = x_{t+1}/p_t$ |
| $d_t$ | dividend |
| $c_t$ | consumptie |
| $u(\cdot)$ | periodenutsfunctie; $u'$ marginaal nut |
| $\gamma$ | relatieve risicoaversie |
| $\beta$ | subjectieve discontofactor |
| $\beta_{i,f}$ | bèta van activum $i$ op factor $f$ (met index, altijd) |
| $\lambda_f$ | prijs van risico van factor $f$ |
| $\alpha_i$ | pricing error / Jensen-alpha |
| $f_{t+1}$ | factor(rendement) |
| $\mathrm{PD}_t = p_t/d_t$ | prijs-dividend-ratio; $\mathrm{DP}_t$ het omgekeerde |
| $\mu, \sigma$ | verwachting en standaarddeviatie van rendementen |
| $\E_t[\cdot]$ | verwachting gegeven informatie op $t$ |
| $\Var, \Cov, \Corr$ | variantie, covariantie, correlatie |

**Tijdsindexering.** Consequent $t \to t+1$: prijzen en informatie op $t$,
payoffs en rendementen op $t+1$. Dus $p_t = \E_t[m_{t+1} x_{t+1}]$, nooit
$p_t = \E[m_t x_t]$. Een rendement met subscript $t+1$ is *verdiend* tussen $t$
en $t+1$ en is op $t$ nog onbekend.

**Vet en hoofdletters.** Vectoren vet en klein ($\mathbf{r}$, $\boldsymbol{\beta}$),
matrices vet en hoofdletter ($\boldsymbol{\Sigma}$, $\mathbf{X}$). Scalairs
gewoon cursief.

**Log-variabelen.** Kleine letters voor logs: $r = \log R$, $p = \log P$,
$d = \log D$. Omdat $p_t$ ook de prijs is in de niveauvergelijkingen, kondig je
per sectie aan welke conventie geldt zodra je overstapt op logs. Bij
Campbell-Shiller: één zin ("vanaf hier zijn kleine letters logs").

**Beschikbare LaTeX-macro's** (gedefinieerd in `myst.yml`, werken overal):
`\E`, `\Var`, `\Cov`, `\Corr`, `\SD`, `\plim`. Definieer geen eigen macro's die
een bestaand LaTeX-commando overschrijven (`\Re`, `\Im`, `\Pr`) — KaTeX breekt
daarop.

### Nederlands versus Engels

De lecturetekst is Nederlands. Code, variabelenamen, functienamen en docstrings
zijn Engels.

Een vakterm blijft Engels als de Nederlandse vertaling gekunsteld is of
niemand hem gebruikt. **De eerste keer in elke lecture:** cursief, gevolgd door
een korte uitleg tussen haakjes.

> ... de *stochastic discount factor* (SDF, stochastische disconteringsfactor:
> de willekeurige variabele waarmee je toekomstige payoffs verdisconteert) ...

> ... een *carry trade* (lenen in een valuta met lage rente, uitzetten in een
> valuta met hoge rente) ...

Daarna gewoon de Engelse term, zonder cursief. Engels blijven onder meer:
stochastic discount factor, momentum, carry, value, size, hedge, spread,
mispricing, limits of arbitrage, event study, sorts, factor zoo, smart beta,
market maker, order flow. Nederlands wordt in elk geval: rendement (niet
*return*), rente, prijs, dividend, consumptie, risicoaversie, discontovoet,
verwachting, standaardfout, steekproef, schatter, regressie, portefeuille.

Decimalen in de lopende tekst met een komma (`8{,}5\%` binnen wiskunde, "8,5%"
in tekst); in code en in tabeluitvoer laat je de Engelse punt staan.

---

## 4. MyST-conventies

Geverifieerd werkend in Jupyter Book 2.1.6 (mystmd). Gebruik niets wat hier niet
staat zonder het eerst te bouwen.

### Frontmatter

```yaml
---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```

Direct daarna het paginalabel en de titel:

```markdown
(02-08-capm)=

# Het CAPM
```

### Labels — vaste conventie

| Soort | Patroon | Voorbeeld |
|---|---|---|
| pagina | `<deel>-<nr>-<slug>` | `(02-08-capm)=` |
| vergelijking | `eq-<slug>-<naam>` | `eq-capm-sml` |
| stelling e.d. | `thm-<slug>-<naam>` | `thm-capm-tweefonds` |
| figuur | `fig-<slug>-<naam>` | `fig-capm-sml` |
| codecel | `cel-<slug>-<naam>` | `cel-capm-sml` |
| oefening | `ex-<slug>-<nr>` | `ex-capm-1` |
| tabel | `tab-<slug>-<naam>` | `tab-capm-ff25` |

`<slug>` is de lecture-slug zonder deelnummer en zonder onderstrepingstekens:
`02_08_capm.md` → `capm`. **Gebruik koppeltekens, geen dubbele punten.** MyST
normaliseert labels naar kleine letters met koppeltekens; een `:` in een label
werkt niet betrouwbaar in cross-refs.

### Vergelijkingen

Genummerd, met label:

````markdown
```{math}
:label: eq-capm-sml
\E[R_i] - R^{f} = \beta_{i,m}\left(\E[R_m] - R^{f}\right)
```
````

Verwijzen: `[](#eq-capm-sml)` → rendert als "(3)". Wil je eigen tekst:
`[vergelijking %s](#eq-capm-sml)`. Ongenummerde tussenstappen in een afleiding
zet je in `$$ ... $$` zonder label.

### Stellingen en bewijzen

`prf:`- en `proof:`-varianten werken allebei; gebruik `prf:`.

````markdown
:::{prf:theorem} Bèta-representatie
:label: thm-capm-beta

Als $1 = \E[mR^i]$ voor elk activum $i$ ...
:::

:::{prf:proof}
Uit $1 = \E[mR^i]$ volgt ...  $\square$
:::
````

Beschikbaar: `prf:theorem`, `prf:lemma`, `prf:corollary`, `prf:proposition`,
`prf:definition`, `prf:axiom`, `prf:remark`, `prf:example`, `prf:observation`,
`prf:algorithm`, `prf:proof`. De Nederlandse naam zet je in het argument
(het thema zet er "Theorem 1 (...)" omheen — dat is een themabeperking, niet iets
wat je met een optie oplost).

### Admonitions

`{note}`, `{tip}`, `{warning}`, `{important}`, `{seealso}`, `{caution}`,
`{danger}`, en `{admonition} Eigen titel` met `:class: <soort>`.

| Directive | Waarvoor |
|---|---|
| `{admonition} ... :class: important` | "Waar we zijn in het verhaal" |
| `{admonition} Replicatie :class: seealso` | het replicatieblok (§6) |
| `{note}` | terzijdes: historische voetnoot, alternatieve afleiding |
| `{tip}` | praktisch implementatie-advies |
| `{warning}` | valkuilen die geld of een verkeerde conclusie kosten |

`:class: dropdown` maakt een blok inklapbaar.

### Oefeningen en oplossingen

````markdown
:::{exercise}
:label: ex-capm-1

**Titel.** Opgave ...
:::

:::{solution} ex-capm-1
:class: dropdown

Uitwerking, inclusief codecellen.
:::
````

Het argument van `{solution}` is het **label van de oefening**, niet een eigen
label. `:class: dropdown` is verplicht op elke oplossing.

### Citaties

`{cite}`Key`` → "(Lucas, 1978)"; `[@Key]` doet hetzelfde. Voor een citaat in de
zin: `` {cite:t}`Lucas1978` `` → "Lucas (1978)". Meerdere keys met komma's:
`` {cite}`FamaFrench1993,FamaFrench1992` ``. Elke key moet in `references.bib`
staan; een onbekende key geeft een buildfout.

### Figuren

Een matplotlib-figuur uit een codecel wordt een genummerde figuur door de cel te
labelen en er een `{figure}` naar te laten verwijzen:

````markdown
```{code-cell} ipython3
:tags: [hide-input]
:label: cel-capm-sml

fig, ax = plt.subplots()
...
plt.show()
```

:::{figure} #cel-capm-sml
:label: fig-capm-sml
:width: 90%

Bijschrift dat de figuur *interpreteert* — niet herhaalt wat de aslabels al
zeggen.
:::
````

Verwijzen: `[](#fig-capm-sml)` → "Figuur 2". Een figuur zonder bijschrift en
zonder label mag, maar dan verwijs je er ook niet naar.

### Cross-refs naar andere lectures

Binnen dezelfde pagina en tussen pagina's werkt hetzelfde patroon:
`[](#02-08-capm)` gebruikt de titel van die pagina als linktekst,
`[het CAPM](#02-08-capm)` gebruikt je eigen tekst. Gebruik **geen** paden of
bestandsnamen — labels zijn projectbreed uniek.

### Tabellen

Markdown-pipe-tabellen voor korte, handgeschreven tabellen (zoals het
toy-voorbeeld). Alles wat uit data komt, is een `DataFrame` als laatste
expressie van een codecel.

---

## 5. Code-conventies

**Eén imports-cel**, aan het begin van `## Toy-voorbeeld` (§11.7). Daarna wordt er nergens
meer geïmporteerd.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm          # alleen als je hem gebruikt
from scipy import stats               # idem

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

Regels:

- **Willekeur.** Altijd `rng = np.random.default_rng(seed)` in de imports-cel,
  met een vaste seed. Nooit `np.random.seed`, nooit `np.random.normal` zonder
  `rng`. Kies de seed één keer en verander hem niet omdat het resultaat mooier
  wordt; wijkt de simulatie af van de asymptotische waarde, dan bespreek je dat
  in de tekst.
- **Geen `!pip`, geen `%pip`, geen `conda`.** Alles wat je nodig hebt staat in
  `pyproject.toml`. Mist er iets, meld het; installeer het niet in een cel.
- **Geen downloads buiten `hap.data`.** Geen `requests`, `urlopen`,
  `pd.read_csv("http://...")`, geen `yfinance` rechtstreeks. Alle data komt via
  `hap.data.french / shiller / fred / goyal_welch / gsw / osap / hkm / yahoo`.
  Die loaders cachen naar `data/cache/*.parquet`.
- **HAP_OFFLINE-compatibel.** De lecture moet volledig draaien met
  `HAP_OFFLINE=1` zodra de cache gevuld is. Draai je lecture één keer met
  `HAP_OFFLINE=1` voordat je hem oplevert, en commit de cachebestanden die je
  gebruikt.
- **Figuurstijl.** `hap.plotting.setup()` in de imports-cel zet de projectstijl.
  Zet daarna geen `rcParams` en geen `plt.style.use` meer. Elke figuur krijgt een
  `set_title`, `set_xlabel` en `set_ylabel`, **in het Nederlands**. Eindig elke
  plotcel met `plt.show()`. Meerdere reeksen in één figuur: `ax.legend()` met
  Nederlandse labels.
- **Tabellen.** Als `DataFrame`, met Nederlandse kolomnamen wanneer het een
  presentatietabel is, en `.round(3)` of `.round(4)` zodat er geen ruis in de
  output staat. Laat de DataFrame de laatste expressie van de cel zijn; gebruik
  geen `print(df)`.
- **Geen warnings in de output.** Los de oorzaak op (een deprecated argument,
  een `SettingWithCopyWarning`, een gedeelde `NaN`). Onderdruk warnings niet met
  `warnings.filterwarnings("ignore")` — dat verbergt alleen dat je code fout is.
- **Looptijd.** Elke cel draait in minder dan 60 seconden op een gewone laptop.
  Duurt een simulatie langer, verklein hem of vectoriseer hem. Numba mag als het
  helpt, maar meestal is het antwoord "minder paden".
- **Celgrootte.** Eén cel doet één ding. Een cel van dertig regels met een klasse
  erin is prima; een cel die drie onafhankelijke resultaten berekent niet.
- **Verborgen cellen.** `:tags: [hide-input]` voor plotcode die de lezer niet
  hoeft te lezen, `[hide-output]` voor lange output. Gebruik `[remove-cell]`
  nooit: wat de lezer niet mag zien, hoort er niet te staan.

Het `hap`-pakket wordt door een andere agent onderhouden. Raak `src/hap/` niet
aan. Mist een loader of een statistiekfunctie die je nodig hebt
(`hap.stats.newey_west`, `hap.stats.fama_macbeth`, `hap.stats.grs`), meld dat in
je rapport en gebruik voorlopig een lokale implementatie in de lecture met een
duidelijke `# TODO: naar hap.stats`-opmerking.

---

## 6. Het replicatieblok

Elke gerepliceerd paperresultaat begint met dit blok, direct onder
`## Replicatie op echte data`. De vorm ligt vast:

````markdown
```{admonition} Replicatie
:class: seealso

**Bron.** Fama & French, *Common Risk Factors in the Returns on Stocks and
Bonds*, Journal of Financial Economics 1993 {cite}`FamaFrench1993`.

**Wat.** Tabel 9a, de alpha's en $t$-waarden van de 25 size/BM-portefeuilles op
het driefactormodel.

**Data hier.** Kenneth French Data Library, maandelijkse 25 portefeuilles en
FF3-factoren, 1963-07 t/m heden, via `hap.data.french(...)`.

**Verschil met het origineel.** Het paper gebruikt CRSP + Compustat met een
steekproef die eindigt in 1991-12; wij gebruiken de kant-en-klare
French-portefeuilles tot heden. French heeft de constructie sinds 1993 op enkele
punten aangepast (behandeling van negatieve boekwaardes, delistings).

**Verwachte afwijking.** Alpha's binnen ongeveer 0,05% per maand van de
gepubliceerde waarden op de overlappende periode; over de volledige steekproef
liggen de $t$-waarden hoger omdat er dertig jaar data bij is gekomen. De
*rangorde* van de portefeuilles en het teken van de alpha's moeten identiek zijn
— wijkt dát af, dan zit er een fout in de code, niet in de data.
```
````

De vijf onderdelen zijn verplicht. **Verwachte afwijking** is de belangrijkste:
noem één grootheid die identiek moet zijn (een teken, een rangorde, een orde van
grootte) zodat de lezer — en de review-agent — kan zien of de replicatie
geslaagd is. Een replicatie zonder falsifieerbare verwachting is geen replicatie.

Als je het gepubliceerde getal in de tekst noemt, noem het letterlijk en zeg
waar het staat. Repliceer je met simulatie omdat de data niet gratis is, zeg dat
dan expliciet in **Data hier** en leg uit welke eigenschap van de echte data je
in de simulatie hebt nagebootst.

---

## 7. Lengte en toon

**Lengte.** 4000–6000 woorden lopende tekst, exclusief code en output. Dat is
lang; het is ook de reden dat de reeks bestaat. Verdeling bij benadering:
overzicht en intuïtie 15%, toy-voorbeeld 10%, theorie 35%, simulatie 10%,
replicatie 15%, "wat er brak" 10%, oefeningen 5%.

**Toon.** Rustig en precies. Geen hype, geen uitroeptekens, geen "verrassend
genoeg", geen "revolutionair". Het materiaal is interessant genoeg; als je het
moet aanprijzen, heb je het niet goed uitgelegd.

- Schrijf in de tegenwoordige tijd voor wiskunde ("de Euler-vergelijking zegt"),
  in de verleden tijd voor geschiedenis ("Fama en MacBeth schatten in 1973").
- Spreek de lezer aan met "u" noch "je" waar het kan; gebruik "we" voor de
  gezamenlijke afleiding ("we delen beide kanten door $p_t$"). In oefeningen mag
  de gebiedende wijs ("simuleer", "schat", "vergelijk").
- Historische anekdotes zijn welkom als ze het argument dienen. Dat Bachelier
  een matige beoordeling kreeg is aardig; het wordt relevant zodra je uitlegt
  dat de wiskunde van 1900 nog geen taal had voor wat hij deed. Anekdotes die
  alleen kleur geven, schrap je.
- Geen "zoals bekend", "triviaal", "eenvoudig te zien" — als het eenvoudig is,
  schrijf je het op.
- Wees eerlijk over wat niet werkt. Een replicatie die de gepubliceerde waarde
  niet haalt, is interessanter dan een die hem haalt, mits je uitlegt waarom.

---

## 8. Bib-conventies

`references.bib` staat in de projectroot en is de enige bibliografie.

- **Key = `AuteurJaar`**, zonder spaties, zonder leestekens:
  `FamaFrench1993`, `Shiller1981`, `BlackJensenScholes1972`,
  `FamaFisherJensenRoll1969`, `GuKellyXiu2020`. Bij meer dan vier auteurs mag je
  bij de eerste drie plus jaar blijven. Twee werken van dezelfde auteurs in
  hetzelfde jaar: suffix `a`/`b` (`Merton1973a` = Rational Option Pricing,
  `Merton1973b` = ICAPM).
- **DOI verplicht waar beschikbaar.** Zoek hem op via
  `https://api.crossref.org/works?query.bibliographic=<titel+auteur>&rows=3` en
  verifieer titel, journal én jaar voordat je hem overneemt.
- **Verzin nooit een DOI.** Geen DOI gevonden? Laat het veld weg.
- **Working papers en online bronnen** krijgen `url = {...}` (NBER-nummer,
  SSRN-link, projectpagina) in plaats van een DOI, met `@techreport` of `@misc`.
- **`note = {TODO verify}`** markeert een entry waarvan titel, journal, volume of
  jaar nog niet is geverifieerd. Kom je zo'n entry tegen bij een lecture die jij
  schrijft, verifieer hem dan en haal de note weg.
- Hoofdletters die moeten blijven staan, tussen accolades:
  `title = {The {CAPM}: Theory and Evidence}`.
- Voeg een entry toe onderaan het bestand; sorteren gebeurt niet handmatig.

---

## 9. Werkwijze: sync, uitvoeren, bouwen

Jupytext-pairing staat in `pyproject.toml`:

```toml
[tool.jupytext]
formats = "ipynb,md:myst"
```

Elke `.md` in `lectures/` is dus gepaard met een `.ipynb`. **De `.md` is de
bron van waarheid voor tekst; de `.ipynb` is waar je code debugt.** Werk je in
het notebook, synchroniseer dan terug voordat je iets anders doet.

De exacte commando's, in deze volgorde:

```bash
# 1. .md en .ipynb synchroniseren (in beide richtingen; nieuwste wint)
uv run jupytext --sync lectures/02_08_capm.md

# 2. de lecture uitvoeren en de outputs in het notebook zetten
uv run jupytext --execute --to ipynb lectures/02_08_capm.md

# 3. de site bouwen (statische HTML in _build/html/)
uv run jupyter book build --html
```

Werk je liever vanuit het notebook, dan is stap 1 `uv run jupytext --sync
lectures/02_08_capm.ipynb` — hetzelfde commando, ander bestand.

De build is klaar als er geen `⛔️` en geen `⚠️` in de uitvoer staat. Warnings
zijn fouten: een onbekende citatiekey, een label waar niets naar verwijst, een
kapotte cross-ref, en een LaTeX-fout verschijnen allemaal als warning en moeten
allemaal weg voordat je oplevert.

Voeg je lecture toe aan de TOC in `myst.yml` door het commentaarteken voor de
regel met jouw bestand weg te halen (en dat van het omliggende `- title:`-blok,
als je de eerste van dat deel bent). De TOC bevat uitsluitend bestanden die
bestaan; een `file:` naar een ontbrekend bestand laat de build falen.

Live meekijken tijdens het schrijven: `uv run jupyter book start` en dan
`http://localhost:3000`.

---

## 10. Afvinklijst voor de review-agent

Per lecture. Alles moet aangevinkt zijn.

**Structuur**

- [ ] Alle vaste kopjes uit §1 aanwezig, in de juiste volgorde, met de juiste
      bewoording.
- [ ] "Waar we zijn in het verhaal" heeft jaartal, wat we al weten (met
      cross-ref naar de vorige lecture), en één open vraag.
- [ ] "Wat er brak" bevat alle vier de elementen, inclusief de risico-versus-
      vergissing-lezing en een cross-ref naar de volgende lecture.
- [ ] 4000–6000 woorden lopende tekst.

**De didactische trap**

- [ ] Er is een toy-voorbeeld dat met de hand na te rekenen is, met de getallen
      in de tekst.
- [ ] De codecel van het toy-voorbeeld reproduceert exact dezelfde getallen, en
      dat is zichtbaar in de output.
- [ ] Er is een simulatie van hetzelfde model op schaal, met minstens één
      figuur, die iets over steekproeven laat zien (schattingsfout, bias,
      datamining) en niet alleen de populatie herhaalt.
- [ ] De replicatie op echte data komt ná de simulatie, niet ervoor.

**Rode draad**

- [ ] Het motief "de standaardfout van 2%" komt terug waar rendementen worden geschat: standaardfouten
      staan erbij.
- [ ] Risico versus vergissing: beide lezingen staan er, en de tekst kiest niet
      voor de lezer.
- [ ] De epistemische status van het model is benoemd (theorie-met-tests versus
      feit-met-concurrerende-theorieën).

**Theorie**

- [ ] Elke afleiding begint met "*Waarom zou dit waar zijn?*" en een economisch
      argument, vóór de wiskunde.
- [ ] Stellingen in `{prf:theorem}`, bewijzen in `{prf:proof}`.
- [ ] Notatie conform §3; afwijkingen van het originele paper zijn benoemd.
- [ ] Elke vakterm die voor het eerst valt, staat cursief met een korte uitleg.

**Replicatie**

- [ ] Het replicatieblok heeft alle vijf onderdelen.
- [ ] **Verwachte afwijking** noemt een falsifieerbare verwachting (teken,
      rangorde, orde van grootte).
- [ ] De gerapporteerde getallen komen overeen met wat het blok belooft; zo
      niet, dan legt de tekst uit waarom.

**Code**

- [ ] Eén imports-cel aan het begin van het toy-voorbeeld; nergens anders imports.
- [ ] `np.random.default_rng(seed)` met vaste seed; geen `np.random.seed`.
- [ ] Geen `!pip`, geen downloads buiten `hap.data`.
- [ ] Draait met `HAP_OFFLINE=1`; gebruikte cachebestanden zijn gecommit.
- [ ] `hap.plotting.setup()` aangeroepen; elke figuur heeft titel en aslabels in
      het Nederlands.
- [ ] Tabellen zijn DataFrames, afgerond.
- [ ] Geen warnings in de output; geen `filterwarnings("ignore")`.
- [ ] Elke cel draait in minder dan 60 seconden.

**Oefeningen**

- [ ] 2–4 oefeningen op problem-set-niveau, elk met een label `ex-<slug>-<nr>`.
- [ ] Elke oefening heeft een `{solution}` met `:class: dropdown`, met code én
      interpretatie.

**Techniek**

- [ ] `uv run jupytext --sync <bestand>` laat `.md` en `.ipynb` identiek achter.
- [ ] `uv run jupytext --execute --to ipynb <bestand>` draait foutloos.
- [ ] `uv run jupyter book build --html` geeft geen `⛔️` en geen `⚠️`.
- [ ] Elke `{cite}`-key staat in `references.bib`; nieuwe entries volgen §8.
- [ ] De lecture staat in de TOC in `myst.yml`, op de plek uit PLAN.md §3.
- [ ] Labels volgen §4 (koppeltekens, met de lecture-slug erin).

---

## 11. Taal en didactiek (aanvulling 2026-09-23)

Bron en toelichting: `plannen/verbeterplan-didactiek.md`. Deze paragraaf is bindend
voor nieuwe en herziene lectures. Waar zij afwijkt van §1, §5 of §7 gaat §11 voor.
`uv run python tools/prose_stats.py --check lectures/<slug>.md` meet wat meetbaar is en
moet PASS geven vóór oplevering.

### 11.1 Zinnen en alinea's

- Eén gedachte per zin. Richtlengte 12 tot 20 woorden, nooit boven 40.
- Een zin met een puntkomma wordt bijna altijd twee zinnen. Puntkomma's alleen in
  opsommingen van korte, gelijksoortige delen.
- Het gedachtestreepje is geen bindmiddel. "X — en dat is Y" wordt "X. Dat is Y."
  Hoogstens tien per lecture, alleen voor een echte terzijde.
- Een alinea heeft één idee en drie tot zes zinnen (richtwaarde 45 woorden).
- Geen telegramstijl ("Nu de econometrie.", "Terug:", "Nu rijen maal kolom:").
- Drie of meer parallelle items (kritieken, aannames, replicaties) worden een lijst.

### 11.2 Aanspreekvorm en stopwoorden

- Geen "u" en geen "je/jij/jouw" in de lopende tekst. Gebruik "we" voor de gezamenlijke
  afleiding, de onpersoonlijke vorm ("wie sorteert op bèta", "een belegger die"), of de
  zaak zelf als onderwerp. "Stel u een eiland voor" wordt "Denk aan een eiland".
- In oefeningen de gebiedende wijs: "Bereken", "Laat zien", "Simuleer".
- Verboden: verrassend, eenvoudigweg, zoals bekend, triviaal, eenvoudig te zien.
- Stopwoorden: "precies", "ruwweg", "inderdaad", "in feite", "letterlijk" samen hoogstens
  zes keer per lecture. "Precies" alleen als het "exact" betekent. Per alinea hoogstens één
  "dus".

### 11.3 Projectjargon

- De drie motieven heten in elke lecture letterlijk zo: **de standaardfout van 2%**,
  **risico of vergissing**, **theorie of feit**. Niet "motief 1/2/3", niet "het
  2%-motief", niet "epistemische status" of "epistemische wending". De zin die het motief
  aanroept zegt wat het hier betekent.
- Geen "L4", "L26", "Deel V", "de trap", "laag 1" in de tekst. Altijd een cross-ref met
  titel of omschrijving.
- Vooruitverwijzingen: hoogstens twee per lecture buiten "Wat er daarna kwam", als
  belofte in één bijzin. Geen inhoud uit een latere lecture gebruiken.

### 11.4 Vertaald Engels

Veel zinnen in de eerste versie zijn Engels gedacht en woord voor woord vertaald. Dat
leest als Nederlands maar is het niet. De lijst hieronder is niet volledig; de toets is
"zou een Nederlandse econoom dit zo zeggen?".

| niet zo (calque) | wel zo |
|---|---|
| de nul (verwerpt de nul) | de nulhypothese |
| de omvang van de toets | het werkelijke significantieniveau; hoe vaak de toets een waar model verwerpt |
| marginaal significant | net wel / net niet significant |
| Noteer dat ... | weglaten, of "Let wel:" (spaarzaam) |
| Onthoud dat ... | weglaten, of "Bedenk dat" |
| Twee dingen zijn hier te zien. / Drie dingen staan er ook. | Deze figuur laat twee dingen zien. / Er valt nog iets op. |
| Dit is de reden dat ... | Daarom ... |
| Dat is wat "een theorie van $r$" betekent | Dat betekent "een theorie van $r$" |
| in de taal van Cochrane | in de termen van Cochrane; zoals Cochrane het zegt |
| het hart van deze lecture | de kern van deze lecture |
| tot vandaag | nog altijd; tot op de dag van vandaag |
| Leg dit naast tabel 4 | Vergelijk dit met tabel 4 |
| de hele inhoud van Regnaults wet | meer zegt Regnaults wet niet |
| het punt is | waar het om gaat is |
| aan het eind van de dag | uiteindelijk |
| Les: | Wat dit leert: |
| Neem nu de data. | Kijk nu naar de data. |
| het interessante deel | daar zit het interessante |
| de vraag is of ... (als stoplap) | gewoon de vraag stellen |
| Het is X dat Y (cleft) | X Y |
| Wat X doet, is Y | X Y |
| de afwezigheid van dividendvoorspelbaarheid (nominale stijl) | dat dividenden niet voorspelbaar zijn |
| bestaansobject, restpost, vastgeknoopt | iets waarvan alleen het bestaan is bewezen; sluitpost; gekoppeld aan |
| Cochrane's, Merton's, Sharpe's | Cochranes, Mertons, Sharpes (apostrof alleen na a, i, o, u, y en na een s-klank: Santa-Clara's, Lucas') |

Beeldspraak die een Engelse vaste uitdrukking vertaalt ("de hond die niet blafte") mag
één keer, met uitleg, als eigennaam van een argument. Daarna een gewone omschrijving.

### 11.5 Citaten, vaktermen en getallen

- Een Engels citaat staat niet midden in een Nederlandse zin. Parafraseer in het
  Nederlands met de bron erbij. Alleen als de bewoording ertoe doet (Santa-Clara, Fama,
  een beroemde formulering): één Nederlandse zin die zegt wat er staat, dan het citaat
  als blokcitaat (`> ...`).
- Vaktermen volgens §3; dat geldt ook voor Nederlandse termen die een PhD-student niet
  vanzelf kent (affiene combinatie, harmonisch gemiddelde, MA(4)-proces, Wishart-verdeeld).
- Hoogstens drie getallen per alinea in lopende tekst. Meer getallen horen in een tabel.
  Elke vergelijking origineel/hier is een tabel met kolommen "origineel", "hier" en waar
  zinvol "verschil" of "SE". Het oordeel eronder begint met "Geslaagd", "Gedeeltelijk
  geslaagd" of "Niet geslaagd" en verwijst naar de "verwachte afwijking".

### 11.6 Afleidingen

- `## Theorie` begint met een routekaart van drie tot vijf regels: wat we afleiden, in
  welke volgorde, en wat de kern is.
- Vast ritme per stap: één of twee zinnen waarom we de stap zetten, de vergelijking, één
  zin die de vergelijking in woorden leest. Twee vergelijkingen direct achter elkaar alleen
  als de tweede een herschrijving van de eerste is.
- "*Waarom zou dit waar zijn?*" is een economisch beeld van twee tot vijf zinnen, geen
  samenvatting van de bewijsstappen. Toets: wie de wiskunde overslaat, moet het teken en
  de richting van het resultaat kunnen raden.
- Hoogstens drie `{prf:theorem}`/`{prf:proposition}` met open bewijs. Elk bewijs langer
  dan zes regels gaat in `{prf:proof}` met `:class: dropdown`; de hoofdtekst houdt de
  stelling en één alinea bewijsidee.
- Nevenresultaten worden een `{note}` met `:class: dropdown` en sprekende titel, of een
  oefening.
- Na de laatste theorie-subsectie, vóór `## Simulatie`, staat een blok
  `{admonition} Samengevat` met `:class: tip`: drie tot vijf regels, één per resultaat,
  met het label van de vergelijking; de laatste regel zegt wat de simulatie hierna toetst.

### 11.7 Structuur binnen de vaste kopjes

De kopjes van §1 blijven. Binnen de kopjes geldt:

- **Overzicht** heeft een vaste micro-opbouw: (1) de vraag en het antwoord van deze
  lecture in twee zinnen; (2) een lijst van drie tot vijf punten met wat we afleiden,
  simuleren en repliceren; (3) één alinea geschiedenis: wie, wanneer, waarom dit werk het
  tijdvak definieert, met de citaties. Geen code.
- **De imports-cel** staat aan het begin van `## Toy-voorbeeld`, niet meer aan het eind
  van `## Overzicht` (wijzigt §1 en §5). De eerste drie secties zijn dan lopende tekst.
- **Theorie** volgt waar mogelijk deze `###`-volgorde: Opzet en aannames → Het
  kernresultaat → Wat het voorspelt → Hoe het getoetst wordt. Een numerieke oplossing van
  het model hoort in Theorie ("### Numerieke oplossing"), niet in Simulatie.
- **Toy-voorbeeld**: hoogstens één formule die nog niet is afgeleid, gegeven als recept
  in woorden en symbolen; Theorie leidt precies die formule als eerste af. Vorm: opzet in
  een tabel, stappen met getallen (één regel per stap), één codecel, een tabel "met de
  hand / code" als laatste expressie, één zin die zegt wat de lezer nu weet. Handrekenbaar
  betekent: geen matrixinversie boven 2×2, geen noemers boven 100.
- **Simulatie** beantwoordt één vraag over steekproeven. Een tweede simulatie wordt een
  oefening of een dropdown-note.
- **Replicatieblok**: hoogstens 250 woorden, elk van de vijf onderdelen hoogstens twee
  zinnen. Reekscodes en datumdetails horen in de codecel.
- **Waar we zijn in het verhaal**: "Wat we al weten" verwijst naar hoogstens twee eerdere
  lectures.
- **Oefeningen**: oefening 1 is een instap (varieer het toy-voorbeeld, één of twee
  deelvragen); oefening 2 een afleiding; oefening 3 een uitbreiding van de replicatie.
  Elke uitwerking eindigt met een zin die begint met "Wat dit leert:".

### 11.8 Code en cellen

- Elke codecel krijgt één zin ervoor (wat we gaan doen) en één zin erna (wat we zien).
  Geen drie cellen achter elkaar zonder tekst.
- Leesbaar boven kort: geen `argsort(argsort())`, geen `np.eye(n)[idx]`-trucs, geen
  meerregelige comprehensions om een tabel te bouwen. Tussenresultaten krijgen een naam
  die zegt wat ze zijn. Rekenwerk en presentatie in aparte cellen. Cel boven 25 regels
  splitsen, tenzij het één functie is.
- Lussen die de lezer moet zien (fixed-point-iteratie, Fama-MacBeth per maand, expanding
  window) blijven lussen.
- Modelparameters in een kleine `dataclass` of dict met benoemde velden, niet als losse
  globale variabelen met suffixen.
- Kolomnamen in presentatietabellen Nederlands en volledig.

### 11.9 Aanvulling op de afvinklijst van §10

- [ ] `tools/prose_stats.py --check` geeft PASS (words mag met reden in het rapport).
- [ ] Geen "u", "je", "motief N", "L<nr>", "Deel <n>", "epistemisch".
- [ ] Geen calque uit de tabel in §11.4; "precies" en co hoogstens zes keer.
- [ ] Elk Engels citaat geparafraseerd of als blokcitaat met Nederlandse inleiding.
- [ ] Overzicht: vraag en antwoord, lijst, één alinea geschiedenis; imports-cel bij het
      toy-voorbeeld.
- [ ] Routekaart aan het begin van Theorie; "Samengevat" aan het eind.
- [ ] Elke genummerde vergelijking heeft een lees-zin.
- [ ] ≤ 3 stellingen met open bewijs; bewijzen boven zes regels in dropdown.
- [ ] Toy: opzet-tabel, stappen, één cel, tabel hand/code, hoogstens één niet-afgeleide
      formule.
- [ ] Eén simulatie, één steekproefvraag.
- [ ] Replicatieblok ≤ 250 woorden; oordeel begint met "Geslaagd" / "Gedeeltelijk
      geslaagd" / "Niet geslaagd" en staat onder een tabel origineel/hier.
- [ ] Elke codecel heeft een zin ervoor en erna.
- [ ] Oefening 1 is een instap; elke uitwerking eindigt met "Wat dit leert:".
- [ ] Hoogstens twee vooruitverwijzingen buiten "Wat er daarna kwam".

### 11.10 Helderheidsregels (H1 tot H12)

De regels hierboven maken de tekst leesbaar; deze twaalf maken de uitleg helder. Ze
gelden voor de schrijver, en de koude lezer van taak C (plan §5) vinkt ze af. Elke regel
heeft een controlevraag die de lezer beantwoordt met een lijst van vindplaatsen.

**H1. Het waarom is een handeling, geen bewijsschets.** Elke "*Waarom zou dit waar
zijn?*" beschrijft iemand die iets doet (een belegger koopt een klein beetje extra; een
onderzoeker sorteert op bèta) en wat er daardoor met een prijs of rendement gebeurt, met
een richting: stijgt, daalt, blijft gelijk. Woorden als "lineair", "meetkunde", "stap 3"
en "matrix" horen er niet in.
*Controle:* heeft de alinea een handelend onderwerp en een richting? Is na de alinea het
teken van het resultaat te raden?

**H2. Elk symbool en elk geleend resultaat wordt hier uitgelegd.** Een symbool krijgt
bij de eerste keer een naam, een betekenis en een orde van grootte ("$\rho$, ongeveer
0,96 bij een gemiddelde prijs-dividendratio van 25"). Een resultaat uit een eerdere
lecture wordt in één regel herhaald, niet alleen aangehaald: "iedereen houdt dezelfde
risicoportefeuille, de separatiestelling uit [](#01-04-markowitz)".
*Controle:* lijst van symbolen en cross-refs waarvoor de lezer een andere lecture zou
moeten openen.

**H3. Eén stelling, één bewering.** Een `{prf:theorem}` bevat één uitspraak die in één
zin is samen te vatten. Een tweede uitspraak wordt een gevolg of een opmerking.
Bewijsstappen hebben een kop die zegt wat de stap oplevert ("*Stap 2: de markt ligt op
de rand*"), niet alleen een nummer.
*Controle:* vat elke stelling in één zin samen. Lukt dat niet, dan is de stelling te vol.

**H4. Het getal staat naast de formule.** Elke formule waarvan de betekenis van de
grootte afhangt (een bias, een standaardfout, een premie, een $R^2$) krijgt in de tekst
direct één uitgerekend getal met de kalibratie erbij, niet alleen in code.
*Controle:* lijst van formules waarvan niet duidelijk is of ze groot of klein uitpakken.

**H5. Aannames worden genoemd waar ze werken.** Bij de bewijsstap die een aanname
gebruikt staat welke ("volgens aanname 2, homogene verwachtingen"). Een aanname die
nergens wordt aangeroepen, hoort niet in de lijst.
*Controle:* bij welke stappen is niet te zeggen welke aanname is gebruikt?

**H6. Elk vergelijkend resultaat wordt in beide richtingen gelezen.** Als een parameter
stijgt: wat gebeurt er, en waarom, in economische termen. "Bij $\gamma > 1$ daalt de
ratio, omdat het rente-effect wint van het groei-effect."
*Controle:* is voor elke parameter in "Samengevat" te zeggen wat er gebeurt als hij
stijgt, en waarom?

**H7. Eén naam per begrip per lecture.** Dividend-prijsratio, dividendopbrengst, $dp$ en
$D/P$ zijn niet vier dingen. De eerste keer staat de alias tussen haakjes; daarna één
naam. Hetzelfde voor excess rendement, premie, risicopremie en marktpremie.
*Controle:* lijst van woorden die volgens de lezer hetzelfde betekenen.

**H8. "Dat", "dit", "die vorm" en "het patroon" verwijzen naar de vorige zin, of worden
vervangen door het ding zelf.** "Dat is precies het patroon" wordt "Een te vlakke lijn
met een te hoog intercept is precies het patroon".
*Controle:* bij elke zin die met "Dat is" of "Dit is" begint: wat is "dat"?

**H9. De conclusie staat vooraan.** De eerste zin na een tabel of figuur zegt wat erin
te zien is; de zin vóór een figuur zegt waar de lezer op moet letten (welke lijn, welke
richting). De eerste zin van elke `###` is de vraag die de subsectie beantwoordt of de
bewering die zij bewijst. Bewijs volgt na de conclusie.
*Controle:* zegt de eerste zin na elke tabel wat de tabel laat zien? Is van elke `###`
alleen op grond van de eerste zin te zeggen waar hij over gaat?

**H10. Abstracties krijgen een exemplaar.** Elke abstracte term (instrument, factor,
toestandsvariabele, momentvoorwaarde, testactivum) krijgt bij de eerste keer één concreet
voorbeeld in dezelfde zin: "een instrument $z_t$, bijvoorbeeld de consumptiegroei van
vorig kwartaal".
*Controle:* lijst van abstracte termen zonder voorbeeld.

**H11. De toy-getallen komen terug.** Minstens één getal uit het toy-voorbeeld keert
terug in de theorie (als illustratie) en in de simulatie (als kalibratie), zodat de drie
lagen aan elkaar geknoopt zijn.
*Controle:* welke toy-getallen zag de lezer terug, en waar?

**H12. De intuïtie doet een voorspelling die de theorie inlost.** De intuïtiesectie
eindigt met wat we dus verwachten (teken, richting). De theorie zegt expliciet waar die
verwachting wordt bevestigd of verfijnd ("zoals de intuïtie voorspelde, maar met een
factor $\gamma$ ervoor").
*Controle:* wat voorspelde de intuïtie, en waar werd dat ingelost?

**De navertel-toets.** Naast de twaalf controles schrijft de koude lezer na elke
`##`-sectie (en in Theorie na elke `###`) in twee of drie zinnen op wat hij heeft
geleerd en wat de sectie beweert. Wijkt die samenvatting af van wat de schrijver
bedoelde, dan was de uitleg niet helder, ongeacht de regels.
