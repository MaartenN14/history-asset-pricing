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

(index)=

# Geschiedenis van asset pricing

Dit is een reeks lectures over de geschiedenis van de asset pricing, van
Regnault in 1863 tot de taalmodellen van vandaag. De volgorde is chronologisch,
maar het is geen kroniek: elk tijdvak wordt behandeld als een samenhangend
antwoord op de vraag *waarom kosten sommige beleggingen meer dan andere?* — en
elk antwoord wordt uitgewerkt tot op de vergelijking, geïmplementeerd in Python,
en getoetst aan data die u zelf kunt downloaden.

De aanleiding is een terugblik van Pedro Santa-Clara,
[*What I learned about asset pricing*](https://www.linkedin.com/pulse/what-i-learned-asset-pricing-pedro-santa-clara-apjce/)
(2026). Die tekst leest als een reisverslag van iemand die het vak van binnenuit
heeft meegemaakt. Deze reeks is de uitgewerkte versie ervan: dezelfde route,
maar met de afleidingen, de data en de code erbij.

## Wat dit is

Elke lecture behandelt één onderwerp — het CAPM, Black-Scholes, de equity
premium puzzle, momentum, de factor zoo — en bevat:

- een afleiding op PhD-niveau, waarbij elke stap begint met de vraag *waarom zou
  dit waar zijn?* voordat er wordt gerekend;
- een replicatie van het kernresultaat van één of twee originele papers, op
  gratis data (Kenneth French, Shiller, FRED, Goyal-Welch, GSW, Open Source
  Asset Pricing, Yahoo Finance) of via simulatie waar geen data bestaat;
- twee tot vier oefeningen op problem-set-niveau, met uitwerkingen in
  opklapbare blokken.

Alle data komen uit het `hap`-pakket dat bij deze reeks hoort. De loaders cachen
lokaal, dus na één keer draaien werkt alles offline.

## De rode draad

Drie motieven lopen door de hele reeks.

**De standaardfout van 2%.** Het gemiddelde rendement van de aandelenmarkt is
met een eeuw data nog steeds slecht gemeten: bij een volatiliteit van 20% per
jaar is de standaardfout van het gemiddelde over honderd jaar ongeveer twee
procentpunt. De variantie daarentegen is uitstekend meetbaar. Dat ene feit
verklaart verrassend veel: waarom volatiliteit voorspelbaar is en rendement
nauwelijks, waarom de equity premium een puzzel blijft die niemand kan
wegschieten, en waarom er honderden gepubliceerde factoren zijn.

**Risico versus vergissing.** Aandelen zijn goedkoop in een recessie. Chicago
zegt: omdat beleggers dan een hogere vergoeding eisen — de discontovoet
varieert. Yale zegt: omdat beleggers bang zijn en de prijs ernaast zit. Beide
kampen zijn het eens over de *feiten*; ze verschillen over de interpretatie. In
2013 kregen Fama en Shiller samen de Nobelprijs, en dat was geen compromis maar
een nauwkeurige beschrijving van de stand van zaken.

**Van theorie-met-tests naar feiten-met-concurrerende-theorieën.** Het vak
begon met één model dat werd getoetst (het CAPM), ging via een raamwerk waarin
alle modellen een uitspraak over dezelfde grootheid zijn (de stochastic discount
factor), naar machine learning die voorspelt zonder te verklaren, en naar
vraagsystemen waarin prijzen bewegen omdat er geld in of uit stroomt.

En daaronder ligt de praktische les die Santa-Clara zelf trekt: *"Everything I
made that lasted came from bearing risk that was priced. Everything I lost came
from thinking I knew something the price did not."*

## Hoe te lezen

De reeks is geschreven om van voren naar achteren te lezen. Elke lecture opent
met **"Waar we zijn in het verhaal"** (het jaartal, wat we al weten, welke vraag
open staat) en sluit met **"Wat er brak, en wat daarna kwam"** — de barst in de
theorie die het volgende tijdvak in gang zette. Wie springt, mist de barsten, en
de barsten zijn het verhaal.

Wilt u toch selectief lezen: Deel 0 (toolkit en rendementsstatistiek) is nodig
voor alles, en de lecture over $p = \E[mx]$ in Deel V is het scharnier waar de
hele eerste helft in terugkomt.

Elke lecture is zowel een webpagina als een notebook. Klik op het
download-icoon om het `.ipynb`-bestand te krijgen, of open het rechtstreeks uit
de map `lectures/`. De tekst is Nederlands; code, variabelenamen en docstrings
zijn Engels, en vaktermen blijven Engels waar een vertaling gekunsteld wordt —
de eerste keer met een korte toelichting.

## Voorkennis

Waarschijnlijkheidsrekening en statistiek op masterniveau, wat lineaire algebra,
en genoeg Python om een `pandas`-DataFrame te lezen. Stochastische analyse
(Itô's lemma) wordt gebruikt maar telkens ter plekke uitgelegd. Wie de
Python-kant wil bijspijkeren, kan terecht bij de reeks van Sargent en Stachurski
waar deze lectures qua vorm op zijn gebaseerd:
[Advanced Quantitative Economics with Python](https://python-advanced.quantecon.org).

```{tableofcontents}
```
