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

(01-04-markowitz)=

# Markowitz, Roy en Tobin

```{admonition} Waar we zijn in het verhaal
:class: important

**Jaartal.** 1952–1959.

**Wat we al weten.** Uit [](#01-03-williams-ddm) komt een theorie van het
*niveau* van een prijs: de contante waarde van de dividenden, verdisconteerd
tegen een voet $r$. De replicatie daar liet zien dat prijzen vooral bewegen
doordat $r$ beweegt. Maar Williams had geen theorie van $r$. Hij bekeek
bovendien elk aandeel apart, alsof een belegger één ding koopt.

**Welke vraag staat open.** Wat is het risico van een belegging: de schommeling
van dat ene stuk papier, of wat het toevoegt aan de portefeuille die de belegger
al heeft?
```

## Overzicht

Welke portefeuille hoort een belegger te houden, en hoe riskant is één activum
daarin? Het antwoord van Markowitz: een activum is zo riskant als zijn
covariantie met de rest van de portefeuille, en de beste portefeuille volgt uit
de verwachte rendementen $\boldsymbol{\mu}$ en de covariantiematrix
$\boldsymbol{\Sigma}$ alleen. In deze lecture:

- leiden we de efficiënte rand af, met de minimum-variantieportefeuille en de
  twee-fondsenstelling;

- voegen we met Tobin een risicovrij activum toe en vinden we de
  tangentportefeuille, die voor elke belegger dezelfde is;

- laten we zien waarom in een grote portefeuille alleen covariantie overblijft;

- simuleren we wat er van de optimale portefeuille overblijft als
  $\boldsymbol{\mu}$ en $\boldsymbol{\Sigma}$ geschat moeten worden;

- repliceren we {cite:t}`DeMiguelGarlappiUppal2009` op French-data: de
  gelijkgewogen portefeuille (hierna 1/N) verslaat de mean-variance-portefeuille
  (de tangentportefeuille uit geschatte momenten).

Markowitz publiceerde in maart 1952, als promovendus in Chicago, veertien
pagina's in *The Journal of Finance*: vier grafieken, geen data
{cite}`Markowitz1952`. In juli kwam A. D. Roy in *Econometrica* bij bijna
dezelfde meetkunde uit {cite}`Roy1952`. Zijn principe was een ander: houd de
kans op een ramp klein. Tobin voegde in 1958 het risicovrije activum toe
{cite}`Tobin1958`, en in 1959 volgde het boek van Markowitz met rekenrecepten
{cite}`Markowitz1959`. Dit werk definieert het tijdvak omdat het de vraag
verplaatst: van wat een aandeel waard is naar welke portefeuille een belegger
wil houden.

Op de vraag theorie of feit is het antwoord: een *theorie van keuze*. Markowitz
zegt wat een belegger zou moeten doen bij gegeven $\boldsymbol{\mu}$ en
$\boldsymbol{\Sigma}$, niet wat de markt doet. Een uitspraak over prijzen wordt
het pas in [het CAPM](#02-08-capm). De theorie is exact, maar de invoer moet
geschat worden, en daar slaat de standaardfout van 2% hard toe: het gegeven uit
[de lecture over rendementen](#00-01-rendementen) dat het gemiddelde rendement
over honderd jaar een standaardfout van ongeveer 2 procentpunt heeft.

## Intuïtie: waarom zou dit waar zijn?

Neem een belegger met één aandeel die een tweede overweegt. Vóór 1952 luidde de
vraag: hoe riskant is dat tweede aandeel? Markowitz vroeg iets anders: hoe
riskant wordt de portefeuille? Dat zijn twee verschillende vragen, en het
verschil is groter dan het lijkt.

Denk aan twee aandelen die even hard op en neer gaan, maar nooit tegelijk. Elk
apart is riskant. Half om half is de portefeuille veel rustiger, want waar de
een verliest, wint de ander vaak. Denk nu aan twee aandelen die even hard
bewegen en dat altijd tegelijk doen. Samen zijn ze even riskant als elk apart.

Wie alleen de afzonderlijke aandelen bekijkt, ziet tussen die twee gevallen geen
verschil. Het verschil zit in hoe ze samen bewegen. Diversificatie is dus meer
dan spreiden: *diversificatie is het beheer van covariantie*. Honderd aandelen
van banken die op elkaar lijken, zijn niet gespreid. Drie activa die niets met
elkaar te maken hebben, zijn dat wel.

Daaruit volgt het inzicht dat de rest van deze reeks draagt. In een goed gespreide
portefeuille hangt het risico van een extra aandeel alleen af van zijn
covariantie met wat er al is. Zijn *idiosyncratische risico* (het eigen risico,
dat met de rest niets te maken heeft) verdwijnt in de massa. En voor
risico dat verdwijnt, hoeft niemand betaald te worden.

Markowitz kreeg het idee in de bibliotheek van de business school in Chicago,
met het boek van Williams in handen {cite}`Markowitz1999`. Als alleen verwachte
dividenden tellen, stopt een belegger alles in het aandeel met het hoogste
verwachte rendement. Dat doet niemand, en dat wijst op een gat in de theorie: er
ontbreekt een tweede grootheid.

Die werd de variantie. Met twee grootheden ontstaat een afruil, en een
verzameling portefeuilles die niet te verslaan zijn: de *efficient frontier*
(efficiënte rand: de laagste variantie bij elk verwacht rendement).

```{note} Friedman bij de promotie
:class: dropdown

In de heruitgave van zijn boek uit 1959 vertelt Markowitz wat Milton Friedman
bij zijn promotie zei. Friedman vond geen fouten, maar ook geen economie:

> I've read your dissertation and can't find any mistakes in it. There is just
> one problem: this is not a dissertation in economics. We cannot award you a
> Ph.D. in economics for a dissertation that is not economics.

Markowitz kreeg de graad diezelfde dag {cite}`KleinDazaMead2013`. De anekdote is
meer dan kleur. Portefeuillekeuze wás in 1952 geen economie: geen markt, geen
evenwicht, geen prijs, alleen een beslissingsprobleem. Economie werd het pas in
het decennium daarna.
```

Roy kwam via een andere deur binnen. Zijn belegger vreest ondergang: hij wil de
kans klein houden dat zijn rendement onder een rampniveau $d$ zakt. Roy had in
de oorlog gediend en schreef, naar eigen zeggen, voor mensen voor wie een
slechte uitkomst het einde is.

Zonder de verdeling te kennen kan zo'n belegger die kans begrenzen. De grens
wordt kleiner naarmate het verwachte rendement verder boven de ramp ligt,
gemeten in standaarddeviaties. De theorie werkt die grens uit. Roys belegger zoekt
dus een hoger verwacht rendement of een kleinere standaarddeviatie: dezelfde
meetkunde, vanuit een andere beweegreden. Voorzichtigheid en nutsmaximalisatie eindigen in hetzelfde punt,
en daarom is de uitkomst zo lang blijven staan.

Tobin voegde de laatste steen toe. Met een risicovrij activum, zoals schatkistpapier,
kiest een belegger eerst de beste verhouding tussen premie en risico (de
*Sharpe-ratio*)
onder de risicovolle activa. Pas daarna kiest hij hoeveel geld daarin gaat. Wie
voorzichtig is, houdt meer van het risicovrije activum. Wie durft, leent bij.

Het risicovolle mandje is voor beiden hetzelfde. Dat is de
*separatiestelling*, en zonder haar heeft de uitspraak dat de markt de optimale
portefeuille is geen betekenis.

De intuïtie doet dus twee voorspellingen die de theorie moet inlossen. Een
mengsel van activa kan veiliger zijn dan het veiligste activum, omdat de delen
niet samen bewegen. En een activum dat met de rest meebeweegt, krijgt weinig
gewicht, ook als het veel oplevert.

## Toy-voorbeeld: de minimum-variantieportefeuille van drie activa

Het kleinste voorbeeld heeft drie activa, met jaarcijfers, te lezen als aandelen
(A), kleine aandelen (B) en obligaties (C). We volgen met de hand één
mechanisme: een mengsel van riskante activa kan veiliger zijn dan het veiligste
activum. De imports-cel staat hier, bij de eerste code van de lecture.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import hap
from hap import data as hap_data
hap.plotting.setup()

rng = np.random.default_rng(20240101)
```

**Opzet.**

| Activum | $\mu_i$ | $\sigma_i$ | $\Corr$ met A | $\Corr$ met B | $\Corr$ met C |
|---|---|---|---|---|---|
| A (aandelen) | 10,0% | 20,0% | 1 | 1/3 | 0 |
| B (kleine aandelen) | 14,0% | 30,0% | 1/3 | 1 | 0 |
| C (obligaties) | 4,0% | 10,0% | 0 | 0 | 1 |

C is het veiligste activum, en A en B bewegen deels samen. De rendementen zijn
netto: 10% is 0,10.

**Het recept.** De *minimum-variantieportefeuille* (de portefeuille met de
laagste variantie) heeft gewichten
evenredig met $\boldsymbol{\Sigma}^{-1}\mathbf{1}$: de inverse covariantiematrix
maal een vector van enen, daarna geschaald zodat de gewichten optellen tot één.
De theorie leidt dit recept als eerste af.

**Stap 1: de covariantiematrix.** Elke covariantie is
$\Sigma_{ij} = \rho_{ij}\sigma_i\sigma_j$, dus
$\Sigma_{AB} = (1/3)(0{,}20)(0{,}30) = 0{,}02$:

$$
\boldsymbol{\mu} =
\begin{pmatrix} 0{,}10 \\ 0{,}14 \\ 0{,}04 \end{pmatrix},
\qquad
\boldsymbol{\Sigma} =
\begin{pmatrix}
0{,}04 & 0{,}02 & 0 \\
0{,}02 & 0{,}09 & 0 \\
0 & 0 & 0{,}01
\end{pmatrix}.
$$

**Stap 2: de inverse.** C correleert met niets, dus $\boldsymbol{\Sigma}$ valt
uiteen in een $2\times2$-blok en een getal. Het blok heeft determinant
$0{,}04 \cdot 0{,}09 - 0{,}02^2 = 0{,}0032$. De inverse van een
$2\times2$-matrix ontstaat door de diagonaal te wisselen, het teken van de
andere twee om te draaien en alles door de determinant te delen. Zo is
$0{,}09/0{,}0032 = 28{,}125$ en $-0{,}02/0{,}0032 = -6{,}25$. Voor C is het
$1/0{,}01 = 100$:

$$
\boldsymbol{\Sigma}^{-1} =
\begin{pmatrix}
28{,}125 & -6{,}25 & 0 \\
-6{,}25 & 12{,}5 & 0 \\
0 & 0 & 100
\end{pmatrix}.
$$

Buiten de diagonaal staat een *negatief* getal waar de covariantie positief is.
Daar zit de hele theorie in: de optimalisatie zet twee activa die samen bewegen
tegen elkaar in.

**Stap 3: de rijsommen.** $\boldsymbol{\Sigma}^{-1}\mathbf{1} = (21{,}875;\;
6{,}25;\; 100)'$, met som $128{,}125$.

**Stap 4: de gewichten.** Delen door die som geeft
$\mathbf{w}_{\mathrm{mv}} = (7/41;\; 2/41;\; 32/41)' = (0{,}1707;\; 0{,}0488;\;
0{,}7805)'$.

**Stap 5: het risico.** Elke rij van $\boldsymbol{\Sigma}\mathbf{w}_{\mathrm{mv}}$
is de covariantie van een activum met de portefeuille, en die is voor alle drie
gelijk: $(0{,}04 \cdot 7 + 0{,}02 \cdot 2)/41 = (0{,}02 \cdot 7 + 0{,}09 \cdot 2)/41
= 0{,}01 \cdot 32/41 = 0{,}32/41$. Omdat de gewichten optellen tot één, is
$\sigma^2_{\mathrm{mv}} = \mathbf{w}'\boldsymbol{\Sigma}\mathbf{w} = 0{,}32/41 =
0{,}0078$, dus $\sigma_{\mathrm{mv}} = 8{,}83\%$.

Obligaties alleen hebben 10,0% standaarddeviatie. Het mengsel met 22% in twee
aandelenposities heeft 8,83%. Riskante activa toevoegen maakt het geheel
rustiger, omdat ze niet met C meebewegen. De codecel rekent dezelfde getallen na.

```{code-cell} ipython3
mu = np.array([0.10, 0.14, 0.04])
sd = np.array([0.20, 0.30, 0.10])
corr = np.array([[1.0, 1 / 3, 0.0],
                 [1 / 3, 1.0, 0.0],
                 [0.0, 0.0, 1.0]])
Sigma = corr * np.outer(sd, sd)
ones = np.ones(3)

Sinv_1 = np.linalg.solve(Sigma, ones)        # Sigma^{-1} 1, stap 3
w_mv = Sinv_1 / Sinv_1.sum()                 # stap 4
sigma_mv = np.sqrt(w_mv @ Sigma @ w_mv)      # stap 5

pd.DataFrame(
    {"met de hand": [0.1707, 0.0488, 0.7805, 0.0883],
     "code": [w_mv[0], w_mv[1], w_mv[2], sigma_mv]},
    index=["gewicht A", "gewicht B", "gewicht C", "standaarddeviatie"],
).round(4)
```

De twee kolommen zijn gelijk. De minimum-variantieportefeuille is veiliger dan
het veiligste activum, en de covariantiematrix alleen bepaalt hoeveel.

## Theorie

We leiden vier dingen af. (1) De efficiënte rand en de twee-fondsenstelling:
alle efficiënte portefeuilles liggen op één parabool, en elk ervan is een mengsel
van twee vaste fondsen. Dat is de kern. De weg ernaartoe loopt via de
eerste-ordevoorwaarde, en daaruit volgt als eerste het recept uit het
toy-voorbeeld. (2) Met een risicovrij
activum de tangentportefeuille en Tobins separatiestelling, met Roy als variant.
(3) Waarom in een grote portefeuille alleen covariantie overblijft. (4) Waarom
de theorie in de praktijk strandt op de schatting van $\boldsymbol{\mu}$.

### Opzet en aannames

We leggen eerst de notatie en vier aannames vast. Er zijn $N$ risicovolle
activa met netto rendementen $\mathbf{R}_{t+1}$ (10% is 0,10),
verwachting $\boldsymbol{\mu} = \E[\mathbf{R}_{t+1}]$ en covariantiematrix
$\boldsymbol{\Sigma} = \Var(\mathbf{R}_{t+1})$. Een portefeuille is een
gewichtsvector $\mathbf{w} \in \mathbb{R}^N$ met $\mathbf{w}'\mathbf{1} = 1$.
Haar rendement is $R_{p,t+1} = \mathbf{w}'\mathbf{R}_{t+1}$, met

$$
\mu_p = \mathbf{w}'\boldsymbol{\mu}, \qquad
\sigma_p^2 = \mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}
= \sum_{i}\sum_{j} w_i w_j \Cov(R_i, R_j).
$$

De variantie van de portefeuille is dus een gewogen som van alle covarianties,
met de varianties als het geval $i = j$. Risico betekent hier standaarddeviatie;
volatiliteit is hetzelfde woord voor hetzelfde getal. Ook de risicovrije rente
$R^{f}$ is netto (2% is 0,02). Met bruto rendementen (één plus netto) zouden
$\boldsymbol{\Sigma}$ en $A$ gelijk blijven, maar $B$ en $C$ veranderen en de
hele rand één omhoog schuiven. De aannames:

1. **Alleen $\mu_p$ en $\sigma_p^2$ tellen.** Een belegger wil meer verwachting
   en minder variantie, en geeft om niets anders.

2. **$\boldsymbol{\Sigma}$ is positief definiet.** Geen activum is een exacte
   combinatie van de andere, dus $\boldsymbol{\Sigma}^{-1}$ bestaat.

3. **Short gaan mag.** Gewichten mogen negatief zijn, zodat de optimalisatie geen
   ongelijkheden kent.

4. **Lenen en uitlenen tegen $R^{f}$ mag onbeperkt.** Deze aanname is pas nodig
   vanaf Tobin.

Aanname 1 is de zwakste. Er zijn twee rechtvaardigingen. Ofwel de rendementen
zijn multivariaat normaal verdeeld, zodat twee momenten de hele verdeling van
$R_p$ vastleggen. Ofwel het nut is kwadratisch, $u(W) = W - \tfrac{b}{2}W^2$,
zodat $\E[u]$ alleen van de eerste twee momenten afhangt.

Geen van beide is onschuldig. Normaliteit is empirisch onjuist (dikke
staarten). Kwadratisch nut is theoretisch onaangenaam: de absolute
risicoaversie stijgt met het vermogen. Er is een derde, algemenere lezing:
mean-variance is een tweede-orde benadering van elk nut, een Taylor-reeks rond het verwachte vermogen die na de
variantie stopt en scheefheid en dikke staarten negeert. Die benadering volstaat
zolang de verdeling niet te scheef is.

```{note} Notatie van Markowitz
:class: dropdown

Markowitz schrijft $E$ en $V$ waar wij $\mu_p$ en $\sigma_p^2$ schrijven. Hij
werkt, net als wij, met netto (enkelvoudige) rendementen. Een constante van alle
rendementen aftrekken laat de covariantiematrix ongemoeid, dus de keuze tussen
bruto en netto verandert de gewichten op de rand niet, alleen de ligging van
de rand.
```

### Het kernresultaat: de efficiënte rand

De bewering: elke belegger die aanname 1 volgt, kiest een portefeuille op één
vaste rand, en elke portefeuille op die rand is een mengsel van twee vaste
fondsen.

*Waarom zou dit waar zijn?* Een belegger die een portefeuille ziet met hetzelfde
verwachte rendement en minder variantie, ruilt om. Bij elke ruil daalt zijn
variantie en blijft zijn verwachte rendement gelijk. Hij stopt pas als zo'n ruil
niet meer bestaat. Zijn keuze ligt dus op de rand: de laagste variantie bij elk
verwacht rendement. Welk punt van de rand hij kiest, hangt van zijn smaak af.
Dat hij op de rand eindigt, volgt al uit aanname 1.

Het probleem is

```{math}
:label: eq-markowitz-probleem
\min_{\mathbf{w}} \ \tfrac12\,\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}
\quad\text{onder}\quad
\mathbf{w}'\boldsymbol{\mu} = \mu_p,
\quad \mathbf{w}'\mathbf{1} = 1 .
```

In woorden: zoek de gewichten met de kleinste variantie, onder de eis dat het
verwachte rendement $\mu_p$ is en dat de gewichten optellen tot één. De factor
$\tfrac12$ houdt alleen de afgeleide schoon. Omdat short gaan mag (aanname 3), is
een Lagrangiaan genoeg:

$$
\mathcal{L} = \tfrac12\,\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}
- \lambda\left(\mathbf{w}'\boldsymbol{\mu} - \mu_p\right)
- \delta\left(\mathbf{w}'\mathbf{1} - 1\right).
$$

De eerste-ordevoorwaarde is
$\boldsymbol{\Sigma}\mathbf{w} - \lambda\boldsymbol{\mu} - \delta\mathbf{1} = 0$.
Omdat $\boldsymbol{\Sigma}$ inverteerbaar is (aanname 2), volgt

```{math}
:label: eq-markowitz-foc
\mathbf{w} = \boldsymbol{\Sigma}^{-1}
\left(\lambda\boldsymbol{\mu} + \delta\mathbf{1}\right).
```

Deze eerste-ordevoorwaarde is de stap naar de rand, en ze heeft zelf al
economische inhoud. De $i$-de rij van
$\boldsymbol{\Sigma}\mathbf{w}$ is $\Cov(R_i, R_p)$, de helft van
$\partial \sigma_p^2/\partial w_i$. In woorden: in het optimum is de covariantie
van elk activum met de portefeuille een vaste lineaire functie van zijn
verwachte rendement. De eigen variantie van activum $i$ telt alleen mee via die
covariantie, met gewicht $w_i$. Stijgt het verwachte rendement van één activum,
dan krijgt het meer gewicht, tot zijn covariantie met de portefeuille weer in
verhouding is.

Herschrijf [](#eq-markowitz-foc) als
$\boldsymbol{\mu} = (1/\lambda)\boldsymbol{\Sigma}\mathbf{w} - (\delta/\lambda)\mathbf{1}$
en er staat een bèta-vorm: verwacht rendement is een constante plus een vaste
factor maal de covariantie met één portefeuille. [Het CAPM](#02-08-capm) geeft
die vorm later een economische betekenis. Hier ontbreekt nog het argument waarom
$\mathbf{w}$ de marktportefeuille zou zijn.

Het eerste bijproduct is het recept uit het toy-voorbeeld. Laat de eis op het
verwachte rendement vallen, zodat $\lambda = 0$. Dan zegt [](#eq-markowitz-foc)
dat $\mathbf{w} \propto \boldsymbol{\Sigma}^{-1}\mathbf{1}$, en de normalisatie
geeft $\mathbf{w}_{\mathrm{mv}} = \boldsymbol{\Sigma}^{-1}\mathbf{1}/
\mathbf{1}'\boldsymbol{\Sigma}^{-1}\mathbf{1}$. Er staat geen $\boldsymbol{\mu}$
in. De minimum-variantieportefeuille is een uitspraak over covarianties alleen,
en op dat feit draait de tweede helft van deze lecture. In het toy-voorbeeld is
zij met 8,83% veiliger dan het veiligste activum (10%). Zo lost de theorie de
eerste voorspelling van de intuïtie in.

De rest van de subsectie gaat van de eerste-ordevoorwaarde naar de kern. De voorwaarde zegt hoe elk
optimum eruitziet. Om de rand zelf te tekenen, moeten we $\lambda$ en $\delta$
nog vastleggen voor elk vereist rendement $\mu_p$. Daarvoor zijn vier getallen
nodig:

```{math}
:label: eq-markowitz-abcd
A = \mathbf{1}'\boldsymbol{\Sigma}^{-1}\mathbf{1},\quad
B = \mathbf{1}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu},\quad
C = \boldsymbol{\mu}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu},\quad
D = AC - B^2 .
```

In woorden: $A$, $B$ en $C$ zijn de drie manieren om $\mathbf{1}$ en
$\boldsymbol{\mu}$ met $\boldsymbol{\Sigma}^{-1}$ te combineren. $D$ meet hoe
sterk de verwachte rendementen uiteenlopen, in de maat van
$\boldsymbol{\Sigma}^{-1}$: hadden alle activa hetzelfde verwachte rendement,
dan was $D$ nul. In het toy-voorbeeld is $A = 128{,}125$, de som uit stap 3, en
$D = 15{,}625$ tegen $AC = 65{,}5$: de verwachte rendementen lopen daar duidelijk
uiteen.

Invullen van [](#eq-markowitz-foc) in de twee restricties geeft het stelsel
$\lambda B + \delta A = 1$ en $\lambda C + \delta B = \mu_p$. Met de regel van
Cramer volgt

$$
\lambda = \frac{A\mu_p - B}{D},
\qquad
\delta = \frac{C - B\mu_p}{D} .
$$

In woorden: hoe hoger het vereiste rendement, hoe zwaarder de richting
$\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}$ weegt en hoe lichter de richting
$\boldsymbol{\Sigma}^{-1}\mathbf{1}$ van de minimum-variantieportefeuille. In het
toy-voorbeeld wijst die laatste vooral naar obligaties: $(21{,}875;\; 6{,}25;\;
100)'$. De eerste, $(1{,}94;\; 1{,}13;\; 4)'$, weegt A en B relatief zwaarder. Bij $\mu_p = 10\%$ is $\lambda = (12{,}8125 - 7{,}0625)/15{,}625 = 0{,}368$
en $\delta = (0{,}51125 - 0{,}70625)/15{,}625 = -0{,}0125$. De helling van de
variantie naar $\mu_p$ is $2\lambda$: een procentpunt extra rendement kost bij
10% ongeveer $2 \cdot 0{,}368 \cdot 0{,}01 = 0{,}0074$ extra variantie.

```{note} Waarom $D$ positief is
:class: dropdown

Zolang $\boldsymbol{\mu}$ geen veelvoud van $\mathbf{1}$ is, is $D > 0$. Dat
volgt uit Cauchy-Schwarz voor het inproduct
$\langle \mathbf{x},\mathbf{y}\rangle = \mathbf{x}'\boldsymbol{\Sigma}^{-1}\mathbf{y}$:
$B^2 = \langle\mathbf{1},\boldsymbol{\mu}\rangle^2 \le AC$, met gelijkheid alleen
als $\boldsymbol{\mu} \propto \mathbf{1}$. In dat geval hebben alle activa
hetzelfde verwachte rendement en is er niets te kiezen.
```

De variantie van de oplossing volgt nu snel. Uit [](#eq-markowitz-foc) is
$\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}
= \mathbf{w}'(\lambda\boldsymbol{\mu} + \delta\mathbf{1})
= \lambda\mu_p + \delta$ (in het toy-voorbeeld bij 10%: $0{,}0368 - 0{,}0125 =
0{,}0243$), dus

```{math}
:label: eq-markowitz-frontier
\sigma^2(\mu_p) = \frac{A\mu_p^2 - 2B\mu_p + C}{D} .
```

In woorden: de laagste haalbare variantie is een parabool in het vereiste
verwachte rendement, en de standaarddeviatie dus een hyperbool, de vorm in
[](#fig-markowitz-frontier). Het minimum ligt bij $\mu_p = B/A$, met variantie
$1/A$. In het toy-voorbeeld is dat een verwacht rendement van 5,51% bij een
standaarddeviatie van 8,83%: de portefeuille die we met de hand vonden.

De parabool werkt in twee richtingen. Wie meer eist dan $B/A$, betaalt met extra
variantie, omdat de gewichten naar de activa met een hoog $\mu_i$ schuiven. Wie
minder eist, betaalt ook, want onder het minimum ligt de inefficiënte tak. Daar
ligt in het toy-voorbeeld bijvoorbeeld de randportefeuille met 3% verwacht
rendement en 11,4% risico: minder rendement en meer risico dan de
minimum-variantieportefeuille.

Bij $\mu_p = 10\%$ geeft de formule in het toy-voorbeeld $\sigma = 15{,}6\%$.
Activum A alleen levert hetzelfde verwachte rendement met 20% risico. De
codecel rekent deze getallen na.

```{code-cell} ipython3
Sinv_mu = np.linalg.solve(Sigma, mu)
A = ones @ Sinv_1
B = ones @ Sinv_mu
C = mu @ Sinv_mu
D = A * C - B**2
sigma_at_10 = np.sqrt((A * 0.10**2 - 2 * B * 0.10 + C) / D)   # eq-markowitz-frontier

pd.DataFrame(
    {"met de hand": [128.125, 7.0625, 0.51125, 15.625, 0.0551, 0.0883, 0.1559],
     "code": [A, B, C, D, B / A, np.sqrt(1 / A), sigma_at_10]},
    index=["A", "B", "C", "D", "verwacht rendement minimum-variantie",
           "standaarddeviatie minimum-variantie", "standaarddeviatie op de rand bij 10%"],
).round(4)
```

De code bevestigt de handberekening. De efficiënte portefeuille met 10%
verwacht rendement heeft ruim een vijfde minder risico dan activum A alleen,
zonder dat er ergens rendement is bijverzonnen.

*Waarom zou de volgende stelling waar zijn?* Denk aan een fondsaanbieder die
klanten met verschillende rendementseisen bedient. Een klant die een procentpunt
meer eist, krijgt minder obligaties en meer aandelen, en elk volgend procentpunt
vraagt dezelfde verschuiving. Een klant met een eis tussen die van twee andere
klanten in, krijgt dus een mengsel van hun portefeuilles. Twee fondsen op de rand
volstaan dan voor iedereen.

:::{prf:theorem} Twee-fondsenstelling
:label: thm-markowitz-tweefonds

Laat $\mathbf{w}(\mu_p)$ de oplossing van [](#eq-markowitz-probleem) zijn. Dan
geldt voor elk tweetal $\mu_1 \neq \mu_2$ en elke $\alpha \in \mathbb{R}$

$$
\mathbf{w}\!\left(\alpha\mu_1 + (1-\alpha)\mu_2\right)
= \alpha\,\mathbf{w}(\mu_1) + (1-\alpha)\,\mathbf{w}(\mu_2).
$$

In woorden: de portefeuilles op de rand zijn precies de mengsels van twee
willekeurige, van elkaar verschillende portefeuilles op die rand.
:::

Het bewijsidee: vul $\lambda$ en $\delta$ in [](#eq-markowitz-foc) in. De
gewichten worden dan een vaste vector plus $\mu_p$ maal een tweede vaste vector,
een *affiene* functie van $\mu_p$ (lineair plus een constante). Een mengsel van
twee punten op zo'n rechte ligt weer op die rechte.

:::{prf:proof}
:class: dropdown

*Stap 1: de gewichten zijn affien in $\mu_p$.* Vul $\lambda$ en $\delta$ in
[](#eq-markowitz-foc) in:

$$
\mathbf{w}(\mu_p)
= \underbrace{\frac{C\,\boldsymbol{\Sigma}^{-1}\mathbf{1}
- B\,\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}}{D}}_{\displaystyle \mathbf{g}}
+ \mu_p \underbrace{\frac{A\,\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}
- B\,\boldsymbol{\Sigma}^{-1}\mathbf{1}}{D}}_{\displaystyle \mathbf{h}} ,
$$

met $\mathbf{g}$ en $\mathbf{h}$ vast, onafhankelijk van $\mu_p$. De afbeelding
$\mu_p \mapsto \mathbf{w}(\mu_p)$ is dus affien. Voor een affiene afbeelding
geldt
$\mathbf{w}(\alpha\mu_1 + (1-\alpha)\mu_2)
= \mathbf{g} + (\alpha\mu_1 + (1-\alpha)\mu_2)\mathbf{h}
= \alpha(\mathbf{g} + \mu_1\mathbf{h}) + (1-\alpha)(\mathbf{g} + \mu_2\mathbf{h})$,
omdat $\alpha + (1-\alpha) = 1$. Dat is de bewering.

*Stap 2: elk mengsel ligt op de rand.* Neem het mengsel
$\alpha\mathbf{w}(\mu_1) + (1-\alpha)\mathbf{w}(\mu_2)$. Het voldoet aan
$\mathbf{w}'\mathbf{1} = 1$ en heeft verwacht rendement
$\alpha\mu_1 + (1-\alpha)\mu_2$. Volgens stap 1 is het gelijk aan
$\mathbf{w}(\alpha\mu_1 + (1-\alpha)\mu_2)$, de minimaliserende portefeuille
bij dat verwachte rendement. Die is uniek omdat $\boldsymbol{\Sigma}$ positief
definiet is (aanname 2). De combinatie ligt dus op de rand. $\square$
:::

Twee beleggingsfondsen volstaan dus om iedere mean-variance-belegger te
bedienen. Dat heeft een praktische en een theoretische kant. Praktisch hoeft een
aanbieder geen portefeuille per klant te bouwen. Met een risicovrij activum
wordt het zelfs één risicovol fonds, zoals de volgende subsectie laat zien, en
dat ene fonds is de intellectuele rechtvaardiging van de indexfondsindustrie.

Theoretisch houdt iedereen een combinatie van dezelfde twee fondsen als alle
beleggers dezelfde $\boldsymbol{\mu}$ en $\boldsymbol{\Sigma}$ zien. Die
*homogene verwachtingen* heeft Markowitz niet nodig. Het CAPM voegt ze toe. Dan houdt de
*markt* die combinatie ook, en dat is de eerste helft van de afleiding van het
CAPM.

### Een risicovrij activum: Tobin en Roy

De bewering: met een risicovrij activum houdt iedereen dezelfde risicovolle
portefeuille, en alleen de dosis verschilt.

*Waarom zou dit waar zijn?* Een belegger verdeelt zijn geld over een activum dat
zeker $R^{f}$ oplevert en een risicovolle portefeuille $p$. Voert hij het aandeel
in $p$ op, dan stijgen verwachting en standaarddeviatie in dezelfde verhouding:
elke extra eenheid risico levert hem de premie per eenheid risico van $p$ op.

Ruilt hij $p$ in voor een portefeuille met een hogere Sharpe-ratio, dan krijgt
hij bij elk risico meer rendement. Hij blijft ruilen tot er geen betere $p$ meer
is. Dat raakpunt, de *tangentportefeuille*, hangt af van $R^{f}$,
$\boldsymbol{\mu}$ en $\boldsymbol{\Sigma}$, niet van zijn smaak.

Formeel schrijven we $\boldsymbol{\mu}^{e} = \boldsymbol{\mu} - R^{f}\mathbf{1}$
voor de verwachte overrendementen (excess rendementen, de *premies*) en
maximeren we de
*Sharpe-ratio* (de verhouding tussen premie en standaarddeviatie; Sharpe gaf hem in 1966 zijn
naam, Roy had hem in 1952 al):

```{math}
:label: eq-markowitz-sharpe
S(\mathbf{w}) = \frac{\mathbf{w}'\boldsymbol{\mu}^{e}}
{\sqrt{\mathbf{w}'\boldsymbol{\Sigma}\mathbf{w}}} .
```

In woorden: de premie per eenheid risico. $S$ verandert niet als alle gewichten met hetzelfde getal worden
vermenigvuldigd. De normalisatie $\mathbf{w}'\mathbf{1}=1$ legt dus alleen de
schaal vast, niet de richting. De afgeleide gelijk aan nul stellen geeft

$$
\frac{\partial S}{\partial \mathbf{w}}
= \frac{\boldsymbol{\mu}^{e}}{\sigma_p}
- \frac{(\mathbf{w}'\boldsymbol{\mu}^{e})\,\boldsymbol{\Sigma}\mathbf{w}}{\sigma_p^{3}}
= 0
\quad\Longrightarrow\quad
\boldsymbol{\Sigma}\mathbf{w} \propto \boldsymbol{\mu}^{e} .
$$

De premie is gemeten ten opzichte van $R^{f}$, en aanname 4 zorgt dat de
belegger die rente ook kan krijgen en betalen. Omdat $\boldsymbol{\Sigma}$
inverteerbaar is (aanname 2), is
$\mathbf{w} \propto \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}$, en na
normaliseren

```{math}
:label: eq-markowitz-tangent
\mathbf{w}_{\mathrm{tan}}
= \frac{\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}}
{\mathbf{1}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}}
= \frac{\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - R^{f}\mathbf{1})}{B - R^{f}A},
\qquad
S_{\max}^2 = (\boldsymbol{\mu}^{e})'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}
= C - 2R^{f}B + (R^{f})^2 A .
```

In woorden: de tangentportefeuille weegt elk activum met zijn premie,
gecorrigeerd voor hoe het met de andere activa meebeweegt. $S_{\max}$ is de
helling van de *kapitaalmarktlijn* (de rechte vanuit de risicovrije rente door
de tangentportefeuille), de hoogste Sharpe-ratio die deze activa kunnen halen.

```{note} Vooruitblik: de Hansen-Jagannathan-grens
:class: dropdown

$S_{\max}$ is ook de belangrijkste scalair van de moderne asset pricing. In
[de lecture over de SDF](#05-26-sdf-unificatie) blijkt hij gelijk aan de
Hansen-Jagannathan-ondergrens $\sigma(m)/\E[m]$. Daarin is $m$ de
stochastische disconteringsfactor: het gewicht waarmee een euro in elke
toekomstige toestand vandaag wordt gewaardeerd, gemiddeld ongeveer
$1/(1 + R^{f})$. De grens zegt hoe sterk $m$ minstens moet schommelen om deze
Sharpe-ratio te verklaren.
```

In het toy-voorbeeld, met een risicovrije rente van 2% ($R^{f} = 0{,}02$ netto,
zoals $\boldsymbol{\mu}$), gaat dat met de hand:

- $\boldsymbol{\mu}^{e} = (0{,}08;\; 0{,}12;\; 0{,}02)'$;
- $\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e} = (28{,}125 \cdot 0{,}08 - 6{,}25
  \cdot 0{,}12;\; -6{,}25 \cdot 0{,}08 + 12{,}5 \cdot 0{,}12;\; 100 \cdot 0{,}02)'
  = (1{,}5;\; 1{,}0;\; 2{,}0)'$;
- de som is $4{,}5$, dus $\mathbf{w}_{\mathrm{tan}} = (1/3;\; 2/9;\; 4/9)'$;
- $S_{\max}^2 = 0{,}08 \cdot 1{,}5 + 0{,}12 \cdot 1{,}0 + 0{,}02 \cdot 2{,}0 = 0{,}28$,
  dus $S_{\max} = 0{,}529$;
- het verwachte rendement is $8{,}22\%$, een premie van $6{,}22$ procentpunt, en
  $\sigma_{\mathrm{tan}} = 0{,}0622/0{,}529 = 11{,}76\%$.

Een $S_{\max}$ van 0,529 ligt iets boven de ongeveer 0,4 per jaar van de
Amerikaanse aandelenmarkt over de afgelopen eeuw. Activum B heeft het hoogste
verwachte rendement en krijgt toch maar 22%, minder
dan het saaie C. Dat komt niet doordat B slecht is, maar doordat B met A
meebeweegt en weinig toevoegt aan wat A al levert. Zo lost de theorie de tweede
voorspelling van de intuïtie in.

De tangentportefeuille hangt van $R^{f}$ af, in beide richtingen. Stijgt
$R^{f}$, dan wordt het risicovrije activum aantrekkelijker dan de veilige
portefeuilles op de rand. De tangentportefeuille schuift dan langs de rand
omhoog naar riskantere portefeuilles, die genoeg premie bieden: bij $R^{f} = 0$ is het verwachte rendement $C/B = 7{,}24\%$, bij
2% is het 8,22%. Daalt $R^{f}$ ver, dan zakt de tangentportefeuille naar de
minimum-variantieportefeuille. De codecel rekent de getallen na.

```{code-cell} ipython3
rf = 0.02
w_tan = (Sinv_mu - rf * Sinv_1) / (B - rf * A)            # eq-markowitz-tangent
sharpe_max = np.sqrt(C - 2 * rf * B + rf**2 * A)
mu_tan = w_tan @ mu
sigma_tan = np.sqrt(w_tan @ Sigma @ w_tan)

pd.DataFrame(
    {"met de hand": [0.3333, 0.2222, 0.4444, 0.0822, 0.1176, 0.5292],
     "code": [w_tan[0], w_tan[1], w_tan[2], mu_tan, sigma_tan, sharpe_max]},
    index=["gewicht A", "gewicht B", "gewicht C", "verwacht rendement",
           "standaarddeviatie", "maximale Sharpe-ratio"],
).round(4)
```

Ook hier geeft de code dezelfde getallen. De figuur zet alles uit het
toy-voorbeeld bij elkaar. Let op de afstand tussen elk activum en de rand, en op
het punt waar de gestreepte lijn de rand raakt.

```{code-cell} ipython3
:tags: [hide-input]
:label: cel-markowitz-frontier

grid = np.linspace(0.02, 0.16, 400)
sigma_frontier = np.sqrt((A * grid**2 - 2 * B * grid + C) / D)
sigma_cml_end = 2 * sigma_tan                     # kapitaalmarktlijn tot 2x sigma_tan

fig, ax = plt.subplots()
ax.plot(sigma_frontier * 100, grid * 100, lw=1.8, label="efficiënte rand")
ax.plot([0, sigma_cml_end * 100],
        [rf * 100, (rf + sharpe_max * sigma_cml_end) * 100],
        ls="--", lw=1.3, color=hap.plotting.COLORS[1],
        label="kapitaalmarktlijn")
ax.scatter(sd * 100, mu * 100, zorder=3, color=hap.plotting.COLORS[2])
for name, s, m in zip(["A", "B", "C"], sd, mu):
    ax.annotate(name, (s * 100 + 0.5, m * 100 - 0.3))
ax.scatter([sigma_mv * 100], [B / A * 100], marker="s", zorder=3,
           color=hap.plotting.COLORS[3], label="minimum-variantie")
ax.scatter([sigma_tan * 100], [mu_tan * 100],
           marker="D", zorder=3, color=hap.plotting.COLORS[1], label="tangent")
ax.set_xlim(0, 32)
ax.set_ylim(0, 16)
ax.set_xlabel("Standaarddeviatie (procenten per jaar)")
ax.set_ylabel("Verwacht rendement (procenten per jaar)")
ax.set_title("De efficiënte rand van drie activa")
ax.legend()
plt.show()
```

:::{figure} #cel-markowitz-frontier
:label: fig-markowitz-frontier
:width: 90%

De drie activa (punten), de efficiënte rand en de kapitaalmarktlijn vanaf de
risicovrije rente van 2%. Elk afzonderlijk activum ligt rechts van de rand: er
is telkens een mengsel met hetzelfde verwachte rendement en minder risico. De
minimum-variantieportefeuille (vierkant) ligt met 8,83% links van het veiligste
activum, dat 10,0% heeft. De tangentportefeuille (ruit) is de enige
portefeuille op de rand die de kapitaalmarktlijn haalt.
:::

De kapitaalmarktlijn ligt overal boven de rand, behalve in de
tangentportefeuille. Wie
risico wil dragen, doet dat dus het best langs die lijn, en dat zegt Tobins
stelling.

:::{prf:corollary} Separatiestelling van Tobin
:label: cor-markowitz-separatie

Met een risicovrij activum houdt elke belegger die alleen om $\mu_p$ en
$\sigma_p$ geeft een portefeuille van de vorm
$a\,\mathbf{w}_{\mathrm{tan}}$ plus $1-a$ in het risicovrije activum, met $a$
afhankelijk van zijn risicoaversie en $\mathbf{w}_{\mathrm{tan}}$ niet.
:::

:::{prf:proof}
Elke portefeuille die de belegger overweegt, ligt op een rechte door
$(0, R^{f})$. Bij een gegeven $\sigma_p$ is zijn verwachte rendement
$R^{f} + S(\mathbf{w})\sigma_p$, stijgend in $S$. Omdat hij alleen om $\mu_p$ en
$\sigma_p$ geeft (aanname 1) en onbeperkt kan lenen en uitlenen (aanname 4),
kiest hij bij elk $\sigma_p$ de $\mathbf{w}$ die $S$
maximeert, en dat is [](#eq-markowitz-tangent). Alleen
$a = \sigma_p/\sigma_{\mathrm{tan}}$ hangt van zijn voorkeuren af. $\square$
:::

```{note} Tobin schreef over geld
:class: dropdown

Tobin schreef dit op in een artikel over *liquidity preference*. Zijn vraag was
waarom iemand geld aanhoudt dat niets oplevert. Zijn antwoord: met geld, bij hem
het risicovrije activum, doseert
een belegger het risico van zijn risicovolle portefeuille. Dat de stelling nu als
portefeuilletheorie wordt onderwezen en niet als monetaire theorie, zegt iets
over hoe het vak zich heeft ontwikkeld.
```

Roy komt langs een andere weg bij dezelfde portefeuille uit. Zijn belegger wil
$\Pr(R_p < d)$ zo klein mogelijk maken. Zonder de verdeling te kennen kan hij die
kans niet uitrekenen, maar wel begrenzen. De ongelijkheid van
Bienaymé-Tchebycheff geeft, voor $\mu_p > d$,

```{math}
:label: eq-markowitz-roy
\Pr\!\left(R_p < d\right)
\le \Pr\!\left(\left|R_p - \mu_p\right| > \mu_p - d\right)
\le \frac{\sigma_p^2}{(\mu_p - d)^2}
= \left(\frac{\mu_p - d}{\sigma_p}\right)^{-2} .
```

In woorden: de kans op een ramp is hoogstens één gedeeld door het kwadraat van
het aantal standaarddeviaties tussen het verwachte rendement en de ramp. De grens
minimaliseren is dus $(\mu_p - d)/\sigma_p$ maximaliseren, en dat is
[](#eq-markowitz-sharpe) met $d$ in de rol van $R^{f}$. Een voorbeeld: de
tangentportefeuille uit het toy-voorbeeld (8,22%, standaarddeviatie 11,76%) en
een ramp van $d = -20\%$ liggen 2,4 standaarddeviaties uit elkaar. De grens is
dan $1/2{,}4^2 = 17\%$. Onder normaliteit is de kans 0,8%: de grens is ruim.

De veiligheid-eerst-belegger (safety first) van Roy en de mean-variance-belegger van Tobin kiezen
dus dezelfde portefeuille zodra $d = R^{f}$. Onder normaliteit is de
gelijkwaardigheid zelfs exact, want dan is
$\Pr(R_p < d) = \Phi(-(\mu_p-d)/\sigma_p)$, met $\Phi$ de standaardnormale
verdelingsfunctie, en is $\Phi$ strikt stijgend.

```{note} Roy, Markowitz en de erkenning
:class: dropdown

Markowitz heeft die samenloop later ruiterlijk erkend. In zijn terugblik uit
1999 schrijft hij dat Roy een gelijk deel van de eer toekomt
{cite}`Markowitz1999`. Het verschil is dat Roy één portefeuille aanwijst en
Markowitz een hele verzameling.

Markowitz ging bovendien door. Hij schreef het boek van 1959
{cite}`Markowitz1959`. Hij ontwierp het kritieke-lijn-algoritme voor de rand
onder een verbod op short gaan. Dat rekent de rand stuk voor stuk uit, telkens
tot een nieuwe positie op nul komt. En hij voerde de semi-variantie in: de variantie van
alleen de uitkomsten onder een drempel, zoals Roys rampniveau $d$. Die maat is
voor wie de asymmetrie van Roy serieus wil nemen.
```

### Wat het voorspelt: alleen covariantie wordt beloond

De bewering: in een grote portefeuille verdwijnt het idiosyncratische risico van elk
activum, en daarom hoeft niemand ervoor betaald te worden.

*Waarom zou dit waar zijn?* Een belegger verdeelt zijn geld gelijk over $N$
activa met elk variantie $\bar{v}$ en onderling covariantie $\bar{c}$. Koopt hij
er een activum bij, dan krijgt elk activum een kleiner gewicht, en daalt het
totaal van de eigen varianties, $\bar{v}/N$, naar nul. Het totaal van de
covarianties, $(1-1/N)\bar{c}$, stijgt juist licht naar $\bar{c}$.

```{math}
:label: eq-markowitz-1n
\Var\!\left(\frac{1}{N}\sum_{i=1}^{N} R_i\right)
= \frac{1}{N^2}\sum_{i} \Var(R_i)
+ \frac{1}{N^2}\sum_{i \neq j}\Cov(R_i,R_j)
= \frac{\bar{v}}{N} + \left(1 - \frac{1}{N}\right)\bar{c}
\ \xrightarrow[N\to\infty]{}\ \bar{c} .
```

In woorden: de eigen varianties verdwijnen, de gemiddelde covariantie blijft, en
die is de bodem van de diversificatie. Neem een maandvolatiliteit van 5,5% per
aandeel en een gemiddelde correlatie van 0,25. De codecel rekent de
jaarvolatiliteit uit voor portefeuilles van 1 tot 100 aandelen.

```{code-cell} ipython3
vbar = 0.055**2                 # variantie per aandeel, per maand
cbar = 0.25 * 0.055**2          # gemiddelde covariantie, per maand
n_grid = np.arange(1, 101)
vol_ann = np.sqrt(vbar / n_grid + (1 - 1 / n_grid) * cbar) * np.sqrt(12)

shown = [1, 5, 10, 30, 100]
pd.DataFrame(
    {"aantal aandelen": shown,
     "volatiliteit (% per jaar)": vol_ann[np.array(shown) - 1] * 100,
     "ondergrens (% per jaar)": np.sqrt(cbar * 12) * 100},
).round(2)
```

Eén aandeel heeft 19,0% jaarvolatiliteit, een oneindig grote
1/N-portefeuille 9,5%. Na dertig aandelen is het meeste al bereikt. De helft van het
risico is weg te diversifiëren, de andere helft niet. Bij een hogere correlatie
stijgt de bodem mee. Bij correlatie nul verdwijnt het risico helemaal, bij
correlatie één valt er niets te spreiden.

Daaruit volgt de economische consequentie. Splits het rendement van activum $i$
in een deel dat met een grote gespreide portefeuille meebeweegt en een rest:
$R_i = a_i + \beta_{i,p} R_p + \varepsilon_i$ met $\Cov(\varepsilon_i, R_p) = 0$.
Dat is een definitie, geen aanname: $\varepsilon_i$ is wat een regressie op $R_p$
overlaat.
De bijdrage van $i$ aan de variantie van die portefeuille is
$\Cov(R_i, R_p) = \beta_{i,p}\Var(R_p)$, met $\beta_{i,p} = \Cov(R_i,R_p)/\Var(R_p)$
de bèta van $i$ ten opzichte van $p$, rond 1 voor een gemiddeld aandeel.
Daarin komt $\Var(\varepsilon_i)$ niet voor.

Wie $\varepsilon_i$ draagt, het idiosyncratische risico uit de intuïtie, draagt dus risico dat hij gratis had kunnen wegdiversifiëren.
Niemand hoeft hem daarvoor te betalen, zoals de intuïtie voorspelde:
*idiosyncratisch risico wordt niet beloond*. Markowitz zegt dat nog niet zo, want hij heeft geen
evenwicht, alleen een optimalisatieprobleem. Maar de zin staat hier klaar.

### Hoe het toegepast wordt: de standaardfout van 2% in de invoer

De bewering: in de praktijk domineert de schattingsfout in $\boldsymbol{\mu}$
alles wat de theorie belooft. Alles hierboven veronderstelt dat $\boldsymbol{\mu}$ en $\boldsymbol{\Sigma}$
bekend zijn. Dat zijn ze niet. In [de lecture over rendementen](#00-01-rendementen)
heette dat de standaardfout van 2%: bij 20% volatiliteit heeft het gemiddelde
rendement over honderd jaar een standaardfout van $20/\sqrt{100} = 2$
procentpunt. Gemiddelden zijn dus slecht meetbaar. Tweede momenten zijn goed
meetbaar, omdat een variantie scherper wordt met meer waarnemingen per jaar
(dagen in plaats van jaren) en een gemiddelde niet: de stelling van Merton in
[](#00-01-rendementen). Dat verschil slaat hier harder toe dan waar ook, om drie
redenen.

1. **De fout is groot.** Met $T$ onafhankelijke jaren data en jaarvolatiliteit
   $\sigma$ is $\SD(\hat\mu) = \sigma/\sqrt{T}$. Tien jaar data van een activum met 20%
   volatiliteit geeft $20/\sqrt{10} = 6{,}3$ procentpunt standaardfout. De
   verschillen in verwachte rendementen tussen activa zijn een paar
   procentpunt, dus de rangorde van $\hat{\boldsymbol{\mu}}$ is vrijwel ruis.
   Meer jaren helpen, maar met de wortel: vier keer zoveel data halveert de fout.

2. **$\boldsymbol{\Sigma}^{-1}$ vergroot de ruis.** De optimale gewichten zijn
   evenredig met $\boldsymbol{\Sigma}^{-1}\hat{\boldsymbol{\mu}}^{e}$, en
   $\boldsymbol{\Sigma}^{-1}$ is groot in de richtingen waarin activa sterk
   gecorreleerd zijn. Juist daar is het verschil tussen twee geschatte
   gemiddelden het slechtst bepaald. De optimalisator zoekt dus op waar hij het
   minst weet. Een kleine verandering in één verwacht rendement kan de gewichten
   volledig omgooien, soms met een orde van grootte {cite}`BestGrauer1991`.

3. **De fout is eenzijdig.** De geschatte maximale Sharpe-ratio
   $\hat{S}_{\max}^2 = \hat{\boldsymbol{\mu}}^{e\prime}\hat{\boldsymbol{\Sigma}}^{-1}
   \hat{\boldsymbol{\mu}}^{e}$ is naar boven vertekend, met
   $\E[\hat{S}^2_{\max}] \approx S^2_{\max} + N/T$. Bij tien activa en 120
   maanden is $N/T = 0{,}083$ per maand, vier keer de ware $S^2_{\max}$ van
   0,021 in de simulatie hierna. Elk extra activum is een extra kans op een
   gemiddelde dat door toeval hoog uitvalt, en de optimalisator kiest juist
   die uit. Daarom groeit de bias met het aantal activa, ook als er niets te
   verdienen valt
   {cite}`JobsonKorkie1980,JobsonKorkie1981`. Michaud noemde dat het
   *optimization enigma*: de schatter maximeert niet het verwachte rendement
   maar de schattingsfout {cite}`Michaud1989`.

Hoe zwaar de drie soorten schattingsfouten wegen, is ook gemeten. Bij een
risicotolerantie van 50 (de parameter in hun mean-variance-nut; hoe hoger, hoe
minder variantie weegt) kosten fouten in de *gemiddelden* ongeveer elf keer
zoveel als fouten in de varianties, en eenentwintig keer zoveel als fouten in de
covarianties {cite}`ChopraZiemba1993`. Die verhoudingen zijn de standaardfout
van 2%, vertaald naar portefeuillekeuze: schat $\boldsymbol{\Sigma}$ zo goed als het gaat, maar
verwacht niets van $\hat{\boldsymbol{\mu}}$.

```{warning}
Het is verleidelijk de geschatte rand te rapporteren als wat diversificatie
oplevert. Die rand is geen belegbare uitkomst. Hij gebruikt
$\hat{\boldsymbol{\mu}}$ en $\hat{\boldsymbol{\Sigma}}$ uit dezelfde waarnemingen
als het rendement dat gemeten wordt. Een vergelijking tussen strategieën hoort
uit een strikt vooruitkijkende constructie te komen, en een gerapporteerde
Sharpe-ratio hoort een standaardfout te hebben.
```

```{admonition} Samengevat
:class: tip

- De kern: de efficiënte rand is een parabool in $(\sigma^2, \mu_p)$,
  [](#eq-markowitz-frontier), en elke portefeuille erop is een mengsel van twee
  vaste fondsen, {prf:ref}`thm-markowitz-tweefonds`.

- De weg ernaartoe: in het optimum is de covariantie van elk activum met de
  portefeuille evenredig met zijn verwachte rendement, [](#eq-markowitz-foc).
  De minimum-variantieportefeuille
  $\boldsymbol{\Sigma}^{-1}\mathbf{1}/A$ gebruikt $\boldsymbol{\mu}$ niet.

- Met een risicovrij activum houdt iedereen dezelfde tangentportefeuille
  $\propto \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^{e}$, [](#eq-markowitz-tangent).
  Alleen de dosis verschilt. Een hogere $R^{f}$ schuift de tangentportefeuille
  naar riskantere portefeuilles, omdat veilige portefeuilles dan te weinig
  premie bieden.

- In een grote portefeuille blijft alleen covariantie over, [](#eq-markowitz-1n).

- In de praktijk moet $\boldsymbol{\mu}$ geschat worden, en die fout domineert.
  Ze daalt met $\sqrt{T}$; de bias in de Sharpe-ratio groeit met $N/T$.

- De simulatie hierna vraagt: hoeveel van de beloofde Sharpe-ratio blijft over
  als de belegger $\boldsymbol{\mu}$ en $\boldsymbol{\Sigma}$ moet schatten?
```

## Simulatie: de optimale portefeuille zonder kennis van $\boldsymbol{\mu}$

We bouwen een wereld met tien activa waarin we de ware momenten kennen. Per
constructie bestaat er een optimale portefeuille met een bekende Sharpe-ratio. De
vraag over steekproeven: hoeveel daarvan levert een belegger die dezelfde
portefeuille bouwt uit $T$ maanden geschatte momenten?

De wereld is een karikatuur van de tien industrieportefeuilles uit de
replicatie: hoge onderlinge correlatie, weinig verschil in gemiddelden, veel
verschil in volatiliteit. We werken direct met overrendementen, dus een
risicovrij activum is niet nodig.

| parameter | waarde |
|---|---|
| aantal activa $N$ | 10 |
| verwacht overrendement | oplopend van 0,40% tot 0,80% per maand (4,8% tot 9,6% per jaar) |
| volatiliteit | oplopend van 4,5% tot 6,5% per maand |
| correlatie tussen elk paar | 0,60 |

De premies verschillen weinig en alles beweegt sterk samen. De eerste cel bouwt die wereld en meet de ware Sharpe-ratio van twee
portefeuilles: het ware optimum (de tangentportefeuille bij de ware momenten) en
1/N.

```{code-cell} ipython3
n_assets = 10
mu_true = np.linspace(0.0040, 0.0080, n_assets)
sd_true = np.linspace(0.045, 0.065, n_assets)
corr_true = np.full((n_assets, n_assets), 0.60)
np.fill_diagonal(corr_true, 1.0)
Sigma_true = corr_true * np.outer(sd_true, sd_true)

chol = np.linalg.cholesky(Sigma_true)       # om gecorreleerde rendementen te trekken
w_star = np.linalg.solve(Sigma_true, mu_true)
w_star /= w_star.sum()                      # ware tangentportefeuille
w_naive = np.full(n_assets, 1 / n_assets)   # 1/N


def oos_sharpe(w):
    """Annualised out-of-sample Sharpe ratio under the TRUE moments."""
    w = np.atleast_2d(w)
    mean = w @ mu_true
    var = np.einsum("ij,jk,ik->i", w, Sigma_true, w)   # w' Sigma w per rij
    return np.squeeze(np.sqrt(12) * mean / np.sqrt(var))


pd.DataFrame(
    {"Sharpe (per jaar)": [float(oos_sharpe(w_star)), float(oos_sharpe(w_naive))]},
    index=["ware optimale portefeuille", "1/N"],
).round(4)
```

Het ware optimum haalt 0,50 per jaar, 1/N haalt 0,47. Dat kleine verschil is
wat optimalisatie in deze wereld hooguit kan opleveren.

In de praktijk moet de belegger schatten. Per steekproef trekken we $T$ maanden,
$\hat{\boldsymbol{\mu}}$ en $\hat{\boldsymbol{\Sigma}}$, vormen we de portefeuille
alsof die schattingen waar zijn, en meten we haar Sharpe-ratio onder de *ware*
momenten. Om te zien waar de schade vandaan komt, schatten we ook telkens maar
één van de twee: de ware $\boldsymbol{\mu}$ met een geschatte
$\boldsymbol{\Sigma}$, en omgekeerd.

```{code-cell} ipython3
def tangency(mu_hat, Sigma_hat):
    """Fully invested maximum-Sharpe weights; rows are independent samples."""
    w = np.linalg.solve(Sigma_hat, mu_hat[..., None])[..., 0]   # Sigma^{-1} mu per steekproef
    return w / w.sum(axis=-1, keepdims=True)


n_sim = 2000
horizons = [60, 120, 240, 600]
records = []

for T in horizons:
    sample = rng.standard_normal((n_sim, T, n_assets)) @ chol.T + mu_true
    mu_hat = sample.mean(axis=1)                    # gemiddelde per steekproef
    demeaned = sample - mu_hat[:, None, :]
    # Sigma_hat per steekproef: som over t van de uitproducten, gedeeld door T - 1
    Sigma_hat = np.einsum("sti,stj->sij", demeaned, demeaned) / (T - 1)

    mu_known = np.broadcast_to(mu_true, (n_sim, n_assets))
    Sigma_known = np.broadcast_to(Sigma_true, (n_sim, n_assets, n_assets))

    records.append(
        {
            "T (maanden)": T,
            "beide geschat": np.median(oos_sharpe(tangency(mu_hat, Sigma_hat))),
            "alleen Sigma geschat": np.median(oos_sharpe(tangency(mu_known, Sigma_hat))),
            "alleen mu geschat": np.median(oos_sharpe(tangency(mu_hat, Sigma_known))),
            "1/N": float(oos_sharpe(w_naive)),
            "ware optimum": float(oos_sharpe(w_star)),
        }
    )

results = pd.DataFrame(records).set_index("T (maanden)")
results.round(4)
```

Schatten kost veel meer dan optimaliseren kan opleveren. De
mean-variance-portefeuille uit geschatte momenten levert een mediane Sharpe-ratio van 0,16 bij vijf jaar data en 0,39
bij vijftig jaar. Over het hele bereik van realistische steekproeflengtes blijft
zij dus onder 1/N.

De decompositie laat zien waar de schade zit. Wie $\boldsymbol{\mu}$ kent en
$\boldsymbol{\Sigma}$ schat, verliest bijna niets. Wie $\boldsymbol{\Sigma}$ kent
en $\boldsymbol{\mu}$ schat, verliest bijna alles. Fouten in gemiddelden kosten
dus veel meer dan fouten in covarianties, net als bij
{cite:t}`ChopraZiemba1993`. Dat gemiddelden de zwakke schakel zijn en tweede
momenten niet, is de standaardfout van 2% in zijn zuiverste vorm.

De figuur vergelijkt voor $T = 120$ wat de optimalisator *in de steekproef*
(in-sample) belooft met wat hij *buiten de steekproef* (out-of-sample) levert. Let op de afstand tussen de twee verdelingen en op de ligging van de
zwarte lijn.

```{code-cell} ipython3
:tags: [hide-input]
:label: cel-markowitz-simulatie

T_plot = 120
sample = rng.standard_normal((n_sim, T_plot, n_assets)) @ chol.T + mu_true
mu_hat = sample.mean(axis=1)
demeaned = sample - mu_hat[:, None, :]
# Sigma_hat per steekproef: som over t van de uitproducten, gedeeld door T - 1
Sigma_hat = np.einsum("sti,stj->sij", demeaned, demeaned) / (T_plot - 1)

sr_oos = oos_sharpe(tangency(mu_hat, Sigma_hat))                 # geleverd
sr_ins = np.sqrt(12) * np.sqrt(                                  # beloofd
    # per steekproef mu_hat' Sigma_hat^{-1} mu_hat, de geschatte S_max^2
    np.einsum("si,sij,sj->s", mu_hat, np.linalg.inv(Sigma_hat), mu_hat)
)

fig, ax = plt.subplots()
ax.hist(sr_ins, bins=50, alpha=0.65, label="in de steekproef (beloofd)")
ax.hist(sr_oos, bins=50, alpha=0.65, label="buiten de steekproef (geleverd)")
ax.axvline(float(oos_sharpe(w_star)), color="black", lw=1.6,
           label="ware optimum")
ax.axvline(float(oos_sharpe(w_naive)), color=hap.plotting.COLORS[3], lw=1.6,
           ls="--", label="1/N")
ax.set_xlabel("Sharpe-ratio (per jaar)")
ax.set_ylabel("Aantal steekproeven")
ax.set_title("Beloofde en geleverde Sharpe-ratio, 2000 steekproeven van 120 maanden")
ax.legend()
plt.show()
```

:::{figure} #cel-markowitz-simulatie
:label: fig-markowitz-simulatie
:width: 90%

Twee verdelingen uit dezelfde 2000 steekproeven van tien jaar. De rechter is wat
de optimalisator *belooft*: de Sharpe-ratio in de steekproef van de portefeuille die hij
op zijn eigen schattingen bouwde, ruim boven het ware optimum. De linker is wat
hij *levert*: dezelfde gewichten onder de ware momenten, vrijwel altijd onder
het ware optimum en meestal onder 1/N. De afstand is geen pech maar bias: de
schatter maximaliseert mee over zijn eigen fout.
:::

De beloofde verdeling ligt niet toevallig hoger maar *systematisch*. De figuur
toont die bias bij één verhouding, $N/T = 10/120$. Dat de bias met $N/T$ groeit,
is het resultaat van {cite:t}`JobsonKorkie1980`.
Wie honderd activa optimaliseert op tien jaar data, rapporteert een
Sharpe-ratio die vrijwel volledig uit schattingsfout bestaat.

## Replicatie op echte data

```{admonition} Replicatie
:class: seealso

**Bron.** DeMiguel, Garlappi en Uppal (hierna DGU), *Optimal Versus Naive Diversification:
How Inefficient Is the 1/N Portfolio Strategy?*, Review of Financial Studies 2009
{cite}`DeMiguelGarlappiUppal2009`. Het paper maakt de waarschuwing van
{cite:t}`Michaud1989` kwantitatief.

**Wat.** Tabel 3: de Sharpe-ratio buiten de steekproef van 1/N tegenover de
mean-variance-portefeuille met steekproefmomenten, geschat op een rollend venster
van $M = 120$ maanden. Hun conclusie: geen van de veertien modellen verslaat 1/N
consequent, over zeven datasets.

**Data hier.** De tien industrieportefeuilles en de 25 size/BM-portefeuilles (gesorteerd op beurswaarde en boek-marktwaarde) van
French, als overrendement boven de risicovrije rente, vanaf juli 1963, net als
bij DGU.

**Verschil met het origineel.** DGU gebruiken elf reeksen (tien industrieën plus
de markt) tot november 2004; wij tien industrieën zonder de markt, met twintig
jaar meer data. Van hun veertien schatters nemen we er drie over: 1/N,
minimum-variantie en mean-variance met steekproefmomenten (hierna de
mean-variance-portefeuille). Als tegenhangers gelden S&P-sectoren bij de tien
industrieën en de FF-vierfactordataset bij de 25 size/BM-portefeuilles.

**Verwachte afwijking.** Het niveau wijkt af, de ordening niet: mean-variance
in de steekproef ver boven 1/N, erbuiten eronder, minimum-variantie minstens
zo goed als 1/N, en het gat tussen belofte en levering groter bij $N = 25$. Met
637 maanden buiten de steekproef is de standaardfout van een maandelijkse
Sharpe-ratio ongeveer 0,04, dus alleen teken, ordening en orde van grootte zijn
informatief.
```

De eerste cel laadt beide panelen en trekt de risicovrije rente af.

```{code-cell} ipython3
rf_monthly = hap_data.market_monthly()["RF"]    # andere naam dan de rf = 0,02 uit de theorie


def excess_panel(name, start="1963-07"):
    """French portfolio returns in excess of the risk-free rate."""
    raw = hap_data.french(name, "monthly").loc[start:]
    return raw.sub(rf_monthly, axis=0).dropna()


industry = excess_panel("10_Industry_Portfolios")   # value-weighted, maandelijks
size_bm = excess_panel("25_Portfolios_5x5")          # 25 size/BM-portefeuilles

pd.DataFrame(
    {"N": [industry.shape[1], size_bm.shape[1]],
     "maanden": [len(industry), len(size_bm)],
     "start": [industry.index[0].strftime("%Y-%m"), size_bm.index[0].strftime("%Y-%m")],
     "eind": [industry.index[-1].strftime("%Y-%m"), size_bm.index[-1].strftime("%Y-%m")]},
    index=["10 industrieën", "25 size/BM"],
)
```

Beide panelen hebben 757 maanden, van juli 1963 tot juli 2026.

Het recept van DGU gaat zo. In elke maand $t \ge M$ schatten we
$\hat{\boldsymbol{\mu}}$ en $\hat{\boldsymbol{\Sigma}}$ uit de voorgaande
$M = 120$ maanden, vormen we de gewichten, en boeken we het gerealiseerde
rendement van maand $t$. Er komt geen informatie uit de toekomst in de gewichten.

```{code-cell} ipython3
def rolling_oos(panel, window=120):
    """Out-of-sample returns of 1/N, sample mean-variance and minimum variance."""
    values = panel.to_numpy()
    n = panel.shape[1]
    ones = np.ones(n)
    out = {"1/N": [], "mean-variance": [], "minimum-variantie": []}

    for t in range(window, len(values)):
        past = values[t - window:t]                 # alleen maanden vóór t
        mu_hat = past.mean(axis=0)
        Sigma_hat = np.cov(past, rowvar=False)

        w_meanvar = np.linalg.solve(Sigma_hat, mu_hat)
        w_minvar = np.linalg.solve(Sigma_hat, ones)
        weights = {"1/N": ones / n,
                   "mean-variance": w_meanvar / w_meanvar.sum(),
                   "minimum-variantie": w_minvar / w_minvar.sum()}
        for key, w in weights.items():
            out[key].append(float(values[t] @ w))

    return pd.DataFrame(out, index=panel.index[window:])


oos_industry = rolling_oos(industry)
oos_size_bm = rolling_oos(size_bm)
oos_industry.tail(3).round(4)
```

De laatste drie maanden zijn alleen een controle dat de drie reeksen gevuld
zijn. Hoe wild de mean-variance-portefeuille beweegt, laat de volgende cel zien,
die de drie reeksen samenvat.

```{code-cell} ipython3
def in_sample_sharpe(panel):
    """Monthly maximum Sharpe ratio attainable with full-sample moments."""
    mu_hat = panel.mean().to_numpy()
    Sigma_hat = panel.cov().to_numpy()
    return float(np.sqrt(mu_hat @ np.linalg.solve(Sigma_hat, mu_hat)))


def sharpe_table(panel, oos):
    """Mean, volatility and Sharpe ratio of each out-of-sample strategy."""
    summary = hap.summary_stats(oos, "monthly")
    return pd.DataFrame(
        {
            "gemiddelde (% per maand)": summary["mean"] * 100,
            "standaarddeviatie (% per maand)": summary["std"] * 100,
            "Sharpe-ratio (per maand)": summary["mean"] / summary["std"],
            "SE van de Sharpe-ratio": 1 / np.sqrt(summary["nobs"].astype(float)),
        }
    ).assign(**{"Sharpe-ratio mean-variance in de steekproef": in_sample_sharpe(panel)})


table = pd.concat(
    {"10 industrieën": sharpe_table(industry, oos_industry),
     "25 size/BM": sharpe_table(size_bm, oos_size_bm)}
)
table.round(4)
```

In beide datasets verliest de mean-variance-portefeuille van 1/N, en wint de
minimum-variantieportefeuille van allebei. Mean-variance beweegt ook veel
wilder: bij de industrieën een standaarddeviatie van 14,5% per maand tegen 4,3%
voor 1/N. De laatste cel zet onze Sharpe-ratio's
naast die uit tabel 3 van DGU, elk origineel naast zijn tegenhanger. De
minimum-variantiegetallen van DGU zijn niet overgenomen. Die cellen blijven leeg.

```{code-cell} ipython3
dgu = pd.DataFrame(
    {"1/N": [0.1876, 0.1753, 0.1277],
     "mean-variance in de steekproef": [0.3848, 0.5364, 0.2090],
     "mean-variance buiten de steekproef": [0.0794, -0.0031, -0.0719],
     # minimum-variantie van DGU is hier niet overgenomen
     "minimum-variantie buiten de steekproef": [np.nan, np.nan, np.nan]},
    index=["origineel: S&P-sectoren (N = 11)", "origineel: FF-vierfactor (N = 24)",
           "origineel: internationaal (N = 9)"],
)                                                    # DGU (2009), tabel 3

sharpe_oos = table["Sharpe-ratio (per maand)"].unstack()
here = pd.DataFrame(
    {"1/N": sharpe_oos["1/N"],
     "mean-variance in de steekproef": [in_sample_sharpe(industry), in_sample_sharpe(size_bm)],
     "mean-variance buiten de steekproef": sharpe_oos["mean-variance"],
     "minimum-variantie buiten de steekproef": sharpe_oos["minimum-variantie"]},
)
here.index = ["hier: 10 industrieën (N = 10)", "hier: 25 size/BM (N = 25)"]

# elk origineel naast zijn tegenhanger; de internationale dataset heeft er geen
comparison = pd.concat([dgu.iloc[[0]], here.iloc[[0]], dgu.iloc[[1]], here.iloc[[1]],
                        dgu.iloc[[2]]]).astype(float)
comparison["gat: in minus buiten"] = (comparison["mean-variance in de steekproef"]
                                     - comparison["mean-variance buiten de steekproef"])
comparison.round(4)
```

**Geslaagd.** De ordening is dezelfde als bij DGU en als het replicatieblok
voorspelde. In de steekproef belooft mean-variance ver boven 1/N, erbuiten
levert zij eronder, en minimum-variantie doet het minstens zo goed als 1/N. Het
gat tussen belofte en levering (laatste kolom) groeit met $N$: van 0,10 bij de
industrieën naar 0,30 bij de 25 portefeuilles, net als bij DGU van 0,31 naar
0,54.

Buiten de steekproef blijft ons niveau positief, waar dat van DGU bij twee van
de drie datasets negatief wordt. Het replicatieblok liet het niveau open, en een
verklaring hebben we niet: het gaat om andere activa en een andere periode.

Eén voorbehoud hoort erbij. Met een standaardfout van 0,04 is geen van de
afzonderlijke verschillen in Sharpe-ratio buiten de steekproef groter dan twee
standaardfouten. De replicatie stelt een consistent teken over twee datasets
vast, geen significant verschil in één.

De minimum-variantieportefeuille, in het toy-voorbeeld 8,83% tegen 10% voor
het veiligste activum, wint hier van beide, met 0,165
bij de industrieën en 0,239 bij de 25 portefeuilles. Het verschil zit in de
invoer: haar gewichten $\boldsymbol{\Sigma}^{-1}\mathbf{1}/A$ gebruiken
$\hat{\boldsymbol{\mu}}$ niet. Zij benut als enige de covariantiestructuur zonder
op geschatte gemiddelden te jagen. Daarom bestaan minimum-variantiefondsen en
risicopariteitsfondsen (risk parity: elk activum dezelfde bijdrage aan het risico) als
productcategorie, en maximum-Sharpefondsen niet.

De figuur toont de cumulatieve overrendementen van de drie strategieën. Let op
hoe onrustig de mean-variance-lijn is.

```{code-cell} ipython3
:tags: [hide-input]
:label: cel-markowitz-cumulatief

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
for ax, (title, frame) in zip(axes, [("10 industrieën", oos_industry),
                                     ("25 size/BM-portefeuilles", oos_size_bm)]):
    for column in frame.columns:
        ax.plot(frame.index, (1 + frame[column]).cumprod(), label=column)
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel("Jaar")
    hap.plotting.timeline_axis(ax)
axes[0].set_ylabel("Waarde van 1 dollar overrendement (log-schaal)")
axes[0].legend()
plt.show()
```

:::{figure} #cel-markowitz-cumulatief
:label: fig-markowitz-cumulatief
:width: 100%

Cumulatief overrendement van de drie strategieën, gefinancierd tegen de
risicovrije rente, met een rollend schattingsvenster van 120 maanden. De
mean-variance-portefeuille is niet alleen slechter maar ook onrustiger: haar
gewichten springen elke maand mee met tien jaar geschatte gemiddelden. De
1/N-lijn loopt rustig zonder dat er één schatting in zit, en dat is de
kern van het argument van DeMiguel, Garlappi en Uppal.
:::

Waarom is mean-variance zo slecht? De volgende cel meet de posities die de
optimalisator in elk venster inneemt.

```{code-cell} ipython3
position_stats = {}
for name, panel in [("10 industrieën", industry), ("25 size/BM", size_bm)]:
    values, window = panel.to_numpy(), 120
    weight_paths = []
    for t in range(window, len(values)):
        past = values[t - window:t]
        w = np.linalg.solve(np.cov(past, rowvar=False), past.mean(axis=0))
        weight_paths.append(w / w.sum())
    weight_paths = np.array(weight_paths)             # maanden x activa

    gross_exposure = np.abs(weight_paths).sum(axis=1)
    turnover = np.abs(np.diff(weight_paths, axis=0)).sum(axis=1)
    position_stats[name] = {
        "grootste long positie": weight_paths.max(),
        "grootste short positie": weight_paths.min(),
        "gemiddelde brutopositie (som van |w|)": gross_exposure.mean(),
        "gemiddelde turnover per maand": turnover.mean(),
    }

pd.DataFrame(position_stats).T.round(3)
```

De optimalisator neemt enorme posities. Bij de tien industrieën gaat hij tot
ruim 2100% long in één portefeuille en ruim 2100% short in een andere. De
brutopositie (de som van de absolute gewichten, bruto exposure) is gemiddeld 7,5
maal het vermogen, en de turnover (omzet) is elke
maand tweemaal het vermogen.

Bij de 25 portefeuilles ontspoort het volledig. De posities lopen op tot meer dan
honderdduizend procent, de brutopositie is gemiddeld 72 maal het vermogen, en
de turnover per maand is van dezelfde orde. In de posities groeit de schade
duidelijk met $N$, ook waar het verschil in Sharpe-ratio niet significant is.

De optimalisator ziet twee sterk gecorreleerde portefeuilles met een klein
verschil in geschat gemiddelde, en concludeert dat daar een bijna risicoloze
arbitrage zit. Dat verschil is ruis. Het resultaat is hefboom op een
schattingsfout.

```{tip}
Alle bekende oplossingen komen op hetzelfde neer: houd de optimalisator weg van
$\hat{\boldsymbol{\mu}}$. Verbied short gaan of begrens elke positie. Krimp
$\hat{\boldsymbol{\mu}}$ naar het gemiddelde over alle activa (Bayes-Stein, zoals
in oefening 3). Krimp $\hat{\boldsymbol{\Sigma}}$ naar een factormodel,
bijvoorbeeld door alle covarianties via de marktbèta te laten lopen. Of gebruik
de resampling van {cite:t}`Michaud1989`: schat de rand vele keren op
gesimuleerde steekproeven en middel de gewichten. Die ingrepen zijn beter te
begrijpen als een impliciete prior op $\boldsymbol{\mu}$ dan als rekentrucs.
Krimpen naar het gemiddelde bijvoorbeeld is de overtuiging dat alle activa
ongeveer hetzelfde verwachte rendement hebben. De sterkste prior van allemaal,
niets weten over verwachte rendementen, is 1/N.
```

## Wat er brak, en wat daarna kwam

**Wat het model verklaart.** Meer dan men denkt, en het is nooit weerlegd: het is
een stelling, geen hypothese. Mean-variance-analyse legt vast dat het risico van
een belegging haar covariantie met de rest van de portefeuille is. Verder dat de
minimum-variantieportefeuille veiliger kan zijn dan het veiligste activum, dat twee
fondsen iedere belegger bedienen, en dat idiosyncratisch risico gratis weg te
diversifiëren is. Die vier uitspraken zijn nog altijd waar en zitten in de
systemen van elke institutionele belegger. De separatiestelling, de
twee-fondsenstelling met één risicovrij fonds, geeft indexbeleggen bovendien een
theoretische grond naast het kostenargument.

**Waar het breekt.** Niet in de wiskunde maar in de invoer. De replicatie laat
zien dat de mean-variance-portefeuille, geschat op tien jaar maanddata, een
lagere Sharpe-ratio haalt dan 1/N over dezelfde activa. Bij de tien
industrieportefeuilles is dat 0,081 tegen 0,158 per maand, terwijl de
optimalisatie in de steekproef 0,185 beloofde. Bij $N = 25$ zijn meer dan
drieduizend maanden data nodig, ruim 250 jaar, voordat optimaliseren loont
{cite}`DeMiguelGarlappiUppal2009`. De oorzaak is de standaardfout van
2%: $\boldsymbol{\Sigma}$ is redelijk te schatten, $\boldsymbol{\mu}$ niet, en de
optimalisator zet zijn grootste posities waar hij het minst weet.

**Risico of vergissing?** Waarom wint 1/N? Het antwoord hangt af van of prijzen
juist zijn, en daarvoor heeft deze reeks twee vaste lezingen. De Chicago-lezing:
prijzen zijn juist, dus verschillen in verwacht rendement zijn klein en vergoeden
alleen risico. Wie op geschatte gemiddelden jaagt, jaagt op ruis. De
Yale-lezing: de verschillen zijn echt en groot (waarde, momentum, kleine
aandelen), maar prijzen zitten soms ernaast en tien jaar gemiddelden tonen dat
niet. Dan faalt de *schatter*. Alleen een voorspeller die buiten de steekproef
werkt, zou de twee scheiden ([](#04-20-voorspelbaarheid),
[](#05-31-portfolio-choice)). Pedro Santa-Clara, wiens terugblik deze reeks
volgt ([](#00-00-setup)), zegt het zo: de mean-variance-portefeuille wedt erop
dat haar geschatte gemiddelden meer weten dan de prijs. De replicatie laat zien
dat die weddenschap verliest.

**Wat er daarna kwam.** Markowitz beschrijft wat één belegger zou moeten doen.
De volgende vraag is wat er met prijzen gebeurt als iedereen het doet. Het antwoord
vraagt eerst een meting van wat de markt eigenlijk heeft gedaan, en die meting
kwam er in 1964 met de CRSP-tape: zie [](#02-05-crsp-tape).

## Oefeningen

:::{exercise}
:label: ex-markowitz-instap

**Instap: het toy-voorbeeld zonder correlatie.** Neem het toy-voorbeeld, maar
laat de correlatie tussen A en B nul zijn in plaats van 1/3.

1. Bereken de gewichten en de standaarddeviatie van de
   minimum-variantieportefeuille met de hand.
2. Stijgt of daalt die standaarddeviatie ten opzichte van 8,83%, en waarom
   krijgt B meer gewicht?
:::

:::{solution} ex-markowitz-instap
:class: dropdown

**(1)** Nu is $\boldsymbol{\Sigma}$ diagonaal, dus
$\boldsymbol{\Sigma}^{-1}\mathbf{1} = (1/0{,}04;\; 1/0{,}09;\; 1/0{,}01)'
= (25;\; 11{,}11;\; 100)'$. Maal 9 geeft $(225;\; 100;\; 900)$, met som 1225, dus
$\mathbf{w}_{\mathrm{mv}} = (9/49;\; 4/49;\; 36/49)' = (0{,}1837;\; 0{,}0816;\;
0{,}7347)'$. De covariantie van elk activum met de portefeuille is weer gelijk:
$0{,}04 \cdot 9/49 = 0{,}09 \cdot 4/49 = 0{,}01 \cdot 36/49 = 0{,}36/49$. Dus
$\sigma^2_{\mathrm{mv}} = 0{,}36/49$ en $\sigma_{\mathrm{mv}} = 0{,}6/7 = 8{,}57\%$.

```{code-cell} ipython3
Sigma_uncorr = np.diag(sd**2)                     # correlatie A-B op nul
Sinv_1_uncorr = np.linalg.solve(Sigma_uncorr, ones)
w_mv_uncorr = Sinv_1_uncorr / Sinv_1_uncorr.sum()
sigma_mv_uncorr = np.sqrt(w_mv_uncorr @ Sigma_uncorr @ w_mv_uncorr)

pd.DataFrame(
    {"met de hand": [0.1837, 0.0816, 0.7347, 0.0857],
     "code": [*w_mv_uncorr, sigma_mv_uncorr]},
    index=["gewicht A", "gewicht B", "gewicht C", "standaarddeviatie"],
).round(4)
```

**(2)** De standaarddeviatie daalt van 8,83% naar 8,57%. B beweegt niet meer met
A mee, dus B voegt nu echte diversificatie toe en krijgt 8,2% in plaats van 4,9%. Wat
dit leert: minder covariantie maakt de minimum-variantieportefeuille veiliger, zonder
dat een enkel activum minder riskant wordt.
:::

:::{exercise}
:label: ex-markowitz-1

**De zero-beta-portefeuille.** Werk met het toy-voorbeeld en de getallen uit de
theorie ($A = 128{,}125$, $B = 7{,}0625$, $C = 0{,}51125$, $D = 15{,}625$).

1. Leid uit [](#eq-markowitz-frontier) af dat de covariantie tussen twee
   portefeuilles op de rand met verwachte rendementen $\mu_1$ en $\mu_2$ gelijk is
   aan $\left(A\mu_1\mu_2 - B(\mu_1+\mu_2) + C\right)/D$.
2. Bepaal daaruit het verwachte rendement $\mu_z$ van de portefeuille op de
   rand die *ongecorreleerd* is met de tangentportefeuille
   ($\mu_{\mathrm{tan}} = 0{,}0822\overline{2}$). Reken het getal met de hand uit
   en controleer het in code.
3. Dat getal heet het zero-beta-rendement. Vergelijk het met de risicovrije rente
   van 2% waarmee de tangentportefeuille werd bepaald. Wat valt op, en waarom is
   dat geen toeval?
:::

:::{solution} ex-markowitz-1
:class: dropdown

**(1)** Met $\mathbf{w}_k = \mathbf{g} + \mu_k\mathbf{h}$ uit het bewijs van
[](#thm-markowitz-tweefonds) is
$\Cov(R_1, R_2) = \mathbf{w}_1'\boldsymbol{\Sigma}\mathbf{w}_2
= \mathbf{w}_1'(\lambda_2\boldsymbol{\mu} + \delta_2\mathbf{1})
= \lambda_2\mu_1 + \delta_2$, want $\mathbf{w}_1'\boldsymbol{\mu} = \mu_1$ en
$\mathbf{w}_1'\mathbf{1}=1$. Invullen van
$\lambda_2 = (A\mu_2 - B)/D$ en $\delta_2 = (C - B\mu_2)/D$ geeft
$\left(A\mu_1\mu_2 - B\mu_1 - B\mu_2 + C\right)/D$, symmetrisch in $\mu_1$ en
$\mu_2$ zoals het hoort. Voor $\mu_1 = \mu_2$ is dit
[](#eq-markowitz-frontier).

**(2)** Nul stellen en oplossen naar $\mu_z$ geeft
$\mu_z = (B\mu_{\mathrm{tan}} - C)/(A\mu_{\mathrm{tan}} - B)$. Met
$\mu_{\mathrm{tan}} = 37/450 = 0{,}0822\overline{2}$ is de teller
$7{,}0625 \cdot 0{,}0822\overline{2} - 0{,}51125 = 0{,}580806 - 0{,}51125
= 0{,}069556$ en de noemer
$128{,}125 \cdot 0{,}0822\overline{2} - 7{,}0625 = 10{,}534722 - 7{,}0625
= 3{,}472222$, dus $\mu_z = 0{,}0200$.

```{code-cell} ipython3
mu_tan = float(w_tan @ mu)
mu_z = (B * mu_tan - C) / (A * mu_tan - B)
w_z = (np.linalg.solve(Sigma, mu) * (A * mu_z - B)
       + np.linalg.solve(Sigma, np.ones(3)) * (C - B * mu_z)) / D

pd.DataFrame(
    {"waarde": [mu_tan, mu_z, float(w_z @ Sigma @ w_tan)]},
    index=["mu van de tangentportefeuille", "zero-beta rendement",
           "covariantie met de tangentportefeuille"],
).round(8)
```

**(3)** Het zero-beta-rendement is exact 2%, gelijk aan de risicovrije rente
waarmee we de tangentportefeuille bepaalden. Dat is geen toeval. Uit
$\mathbf{w}_{\mathrm{tan}} \propto \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} -
R^{f}\mathbf{1})$ volgt voor elke portefeuille $\mathbf{v}$ met
$\mathbf{v}'\mathbf{1} = 1$ dat
$\Cov(R_v, R_{\mathrm{tan}}) \propto \mathbf{v}'(\boldsymbol{\mu} - R^{f}\mathbf{1})
= \mu_v - R^{f}$. Nulcovariantie betekent dus $\mu_v = R^{f}$. Dit is de kern van
{cite:t}`Black1972`: ook zonder risicovrij activum bestaat er een portefeuille
die de rol van $R^{f}$ speelt, en het CAPM geldt dan met $\mu_z$ in plaats van
$R^{f}$. Wat dit leert: de risicovrije rente is in de meetkunde van de rand
gewoon het rendement van de portefeuille die niet met de tangentportefeuille
meebeweegt.
:::

:::{exercise}
:label: ex-markowitz-2

**Hoeveel data is genoeg?** Herhaal de simulatie uit deze lecture, maar varieer
$N$ in plaats van alleen $T$.

1. Bouw dezelfde wereld met $N \in \{5, 10, 25\}$ activa (dezelfde bereiken voor
   $\boldsymbol{\mu}$ en $\sigma$, dezelfde correlatie 0,60). Rapporteer per $N$
   de Sharpe-ratio van 1/N, de mediane Sharpe-ratio buiten de steekproef van de
   mean-variance-portefeuille bij $T = 120$, en het kleinste
   schattingsvenster uit $\{120, 240, 480, 960, 1920, 2880, 3840\}$ waarbij
   mean-variance 1/N overtreft.
2. Vergelijk met de kalibratie van {cite:t}`DeMiguelGarlappiUppal2009`. Zij
   vinden dat bij $N = 25$ meer dan 3000 maanden nodig zijn, en bij $N = 50$ meer
   dan 6000.
3. Verklaar in één zin waarom het benodigde venster met $N$ groeit.
:::

:::{solution} ex-markowitz-2
:class: dropdown

```{code-cell} ipython3
def breakeven(n, horizons=(120, 240, 480, 960, 1920, 2880, 3840), n_sim=200):
    """Median OOS Sharpe at T=120 and the smallest T at which mv beats 1/N."""
    mu_n = np.linspace(0.0040, 0.0080, n)
    sd_n = np.linspace(0.045, 0.065, n)
    corr_n = np.full((n, n), 0.60)
    np.fill_diagonal(corr_n, 1.0)
    Sigma_n = corr_n * np.outer(sd_n, sd_n)
    chol_n = np.linalg.cholesky(Sigma_n)

    def sr(w):
        """Annualised Sharpe ratio under the true moments of this world."""
        return np.squeeze(
            np.sqrt(12) * (w @ mu_n)
            / np.sqrt(np.einsum("ij,jk,ik->i", w, Sigma_n, w))
        )

    sr_naive = float(sr(np.full((1, n), 1 / n)))
    sr_120, smallest = np.nan, np.nan
    for T in horizons:
        draws = rng.standard_normal((n_sim, T, n)) @ chol_n.T + mu_n
        mu_hat = draws.mean(axis=1)
        demeaned = draws - mu_hat[:, None, :]
        # Sigma_hat per steekproef: som over t van de uitproducten, gedeeld door T - 1
        Sigma_hat = np.einsum("sti,stj->sij", demeaned, demeaned) / (T - 1)
        w = np.linalg.solve(Sigma_hat, mu_hat[..., None])[..., 0]
        median = float(np.median(sr(w / w.sum(axis=-1, keepdims=True))))
        if T == 120:
            sr_120 = median
        if np.isnan(smallest) and median > sr_naive:
            smallest = T
    return {"Sharpe van 1/N": sr_naive, "mv bij T=120": sr_120,
            "kleinste T": smallest}


pd.DataFrame({n: breakeven(n) for n in [5, 10, 25]}).T.rename_axis("N").round(4)
```

**(1)** Bij tien jaar data levert mean-variance 0,294 bij $N = 5$, 0,230 bij
$N = 10$ en 0,149 bij $N = 25$. 1/N blijft in alle drie de gevallen rond 0,47.
De schade groeit dus met $N$ bij een vast venster: dat is de $N/T$-bias. Het
omslagvenster (het kleinste venster waarbij mean-variance 1/N verslaat) loopt
van 2880 maanden bij $N = 5$ naar 3840 bij $N = 10$ en $N = 25$. Het rooster is
te grof om de laatste twee te scheiden, en met tweehonderd herhalingen is de
mediaan zelf ook nog onrustig.

**(2)** Bij $N = 25$ komt de simulatie op 3840 maanden, 320 jaar. Dat is dezelfde
orde van grootte als de ruim 3000 maanden van DGU, terwijl onze wereld
vriendelijker is dan de hunne: gelijke correlaties, keurig oplopende waarden van
$\boldsymbol{\mu}$ en normaal verdeelde rendementen. Dat wijst erop dat de
conclusie niet aan de details van de kalibratie hangt, al bewijst één
kalibratie met tweehonderd herhalingen dat niet.

**(3)** De bias in de geschatte Sharpe-ratio schaalt met $N/T$, dus $T$ moet met
$N$ meegroeien om die bias gelijk te houden. De tabel laat de kant zien die we
goed kunnen meten: bij vast $T = 120$ zakt mean-variance van 0,294 bij $N = 5$
naar 0,149 bij $N = 25$. Het omslagvenster groeit in ons grove rooster minder
hard (van 2880 naar 3840 maanden), maar ligt al ver voorbij de geschiedenis die
bestaat. Wat dit leert: meer activa maken
optimalisatie niet makkelijker maar moeilijker, zolang $\boldsymbol{\mu}$
geschat moet worden.
:::

:::{exercise}
:label: ex-markowitz-3

**De replicatie uitbreiden: shrinkage.** Herhaal de rollende analyse buiten de
steekproef op de 25 size/BM-portefeuilles, maar krimp $\hat{\boldsymbol{\mu}}$ in
elk venster naar het gemiddelde over alle portefeuilles:
$\tilde{\boldsymbol{\mu}} = \phi\,\hat{\boldsymbol{\mu}} +
(1-\phi)\,\bar{\hat\mu}\,\mathbf{1}$, met $\phi \in \{0; 0{,}25; 0{,}5; 0{,}75; 1\}$.

1. Bereken voor elke $\phi$ de Sharpe-ratio buiten de steekproef, de gemiddelde
   brutopositie en de gemiddelde turnover.
2. Bij welke $\phi$ is het resultaat het beste, en welke portefeuille is dat bij
   $\phi = 0$?
3. Zit het probleem bij de optimalisatie of bij de invoer?
:::

:::{solution} ex-markowitz-3
:class: dropdown

```{code-cell} ipython3
def shrunk_oos(panel, phi, window=120):
    """Rolling OOS mean-variance with the mean vector shrunk towards its average."""
    values = panel.to_numpy()
    rets, paths = [], []
    for t in range(window, len(values)):
        past = values[t - window:t]
        mu_hat = past.mean(axis=0)
        mu_tilde = phi * mu_hat + (1 - phi) * mu_hat.mean()
        w = np.linalg.solve(np.cov(past, rowvar=False), mu_tilde)
        w = w / w.sum()
        rets.append(float(values[t] @ w))
        paths.append(w)
    rets, paths = np.array(rets), np.array(paths)
    return {
        "Sharpe-ratio (per maand)": rets.mean() / rets.std(ddof=1),
        "brutopositie": np.abs(paths).sum(axis=1).mean(),
        "turnover": np.abs(np.diff(paths, axis=0)).sum(axis=1).mean(),
    }


pd.DataFrame(
    {phi: shrunk_oos(size_bm, phi) for phi in [0.0, 0.25, 0.5, 0.75, 1.0]}
).T.rename_axis("phi").round(3)
```

**(1) en (2)** $\phi = 0$ wint met afstand: een Sharpe-ratio van 0,239 tegen
0,104 bij $\phi = 1$, en een brutopositie van 7,6 in plaats van 72. Bij
$\phi = 0$ is $\tilde{\boldsymbol{\mu}}$ evenredig met $\mathbf{1}$, en is de
portefeuille exact de minimum-variantieportefeuille
$\boldsymbol{\Sigma}^{-1}\mathbf{1}/A$. Die gebruikt geen enkele informatie over
verwachte rendementen.

Het tussengebied gedraagt zich niet netjes. Bij $\phi = 0{,}5$ is de Sharpe-ratio
vrijwel nul en de brutopositie ruim honderd, slechter dan bij $\phi = 1$. Dat
is geen fout maar een eigenschap van de normalisatie $\mathbf{w}/\mathbf{w}'\mathbf{1}$.
Bij tussenliggende $\phi$ komt de ongenormeerde som
$\mathbf{1}'\boldsymbol{\Sigma}^{-1}\tilde{\boldsymbol{\mu}}$ in sommige vensters
dicht bij nul, en dan explodeert de geschaalde positie. Alleen de twee uiteinden
zijn hier goed gedefinieerde strategieën. Wie het tussengebied wil gebruiken,
moet $\mathbf{w}'\mathbf{1} = 1$ vervangen door een doelvolatiliteit.

**(3)** De optimalisatie is niet het probleem. Hetzelfde kwadratische programma,
met $\hat{\boldsymbol{\mu}}$ volledig weggekrompen, levert het beste resultaat
van deze lecture: beter dan 1/N en beter dan de volledige optimalisatie. De
invoer is het probleem. Wat dit leert: het nuttigste wat een belegger over
$\hat{\boldsymbol{\mu}}$ kan weten, is hoeveel hij hem *niet* moet geloven.
Dat is de les uit [](#00-01-rendementen), dat gemiddelden slecht meetbaar zijn,
nu met geld erachter.
:::

<!-- Referenties verschijnen automatisch onderaan de pagina. -->
