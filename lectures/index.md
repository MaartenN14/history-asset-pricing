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

Dit is een reeks lectures over de geschiedenis van asset pricing, van Regnault in
1863 tot de taalmodellen van vandaag. De volgorde is chronologisch, maar het is
geen kroniek. Elk tijdvak wordt behandeld als een samenhangend antwoord op één
vraag: *waarom kosten sommige beleggingen meer dan andere?* Elk antwoord wordt
uitgewerkt tot op de vergelijking, geïmplementeerd in Python en getoetst aan data
die vrij te downloaden is.

De aanleiding is een terugblik van Pedro Santa-Clara,
[*What I learned about asset pricing*](https://www.linkedin.com/pulse/what-i-learned-asset-pricing-pedro-santa-clara-apjce/)
(2026). Die tekst leest als een reisverslag van iemand die het vak van binnenuit
heeft meegemaakt. Deze reeks volgt dezelfde route, met de afleidingen, de data en
de code erbij.

## Wat dit is

Elke lecture behandelt één onderwerp: het CAPM, Black-Scholes, de equity premium
puzzle, momentum, de factor zoo. Elke lecture bevat:

- een afleiding op PhD-niveau, waarbij elke stap begint met de vraag *waarom zou
  dit waar zijn?* voordat er wordt gerekend;
- een klein voorbeeld dat met pen en papier na te rekenen is, en een simulatie die
  laat zien wat er in een steekproef van dat voorbeeld overblijft;
- een replicatie van het kernresultaat van één of twee originele papers, op
  gratis data (Kenneth French, Shiller, FRED, Goyal-Welch, GSW, He-Kelly-Manela, Open Source Asset
  Pricing, Yahoo Finance) of via simulatie waar geen data bestaat;
- twee tot vier oefeningen, met uitwerkingen in opklapbare blokken.

Alle data komen uit het `hap`-pakket dat bij deze reeks hoort. De loaders slaan
lokaal op, dus na één keer draaien werkt alles offline.

## De rode draad

Drie thema's lopen door de hele reeks. Ze hebben een vaste naam en komen onder
die naam in elke lecture terug.

**De standaardfout van 2%.** Het gemiddelde rendement van de aandelenmarkt is met
een eeuw data nog steeds slecht gemeten. Bij een volatiliteit van 20% per jaar is
de standaardfout van het gemiddelde over honderd jaar ongeveer twee procentpunt.
De variantie daarentegen is uitstekend meetbaar. Dat ene feit verklaart veel:
waarom volatiliteit voorspelbaar is en rendement nauwelijks, waarom de equity
premium een puzzel blijft, en waarom er honderden gepubliceerde factoren zijn.

**Risico of vergissing.** Aandelen zijn goedkoop in een recessie. Chicago zegt:
omdat beleggers dan een hogere vergoeding eisen, dus de discontovoet varieert.
Yale zegt: omdat beleggers bang zijn en de prijs ernaast zit. Beide kampen zijn
het eens over de *feiten*; ze verschillen over de uitleg. In 2013 kregen Fama en
Shiller samen de Nobelprijs. Dat was geen compromis maar een nauwkeurige
beschrijving van de stand van zaken.

**Theorie of feit.** Het vak begon met één model dat werd getoetst, het CAPM.
Daarna kwam een raamwerk waarin alle modellen een uitspraak zijn over dezelfde
grootheid, de stochastic discount factor. Daarna machine learning, dat voorspelt
zonder te verklaren. En ten slotte vraagsystemen waarin prijzen bewegen omdat er
geld in of uit stroomt. Bij elk model stellen we de vraag: is dit een theorie
die getoetst wordt, of een feit dat op een verklaring wacht?

Daaronder ligt de praktische les die Santa-Clara zelf trekt. Alles wat hij
verdiende en behield, kwam uit het dragen van risico dat werd beloond; alles wat
hij verloor, kwam uit de gedachte iets te weten wat de prijs niet wist. In zijn
woorden:

> Everything I made that lasted came from bearing risk that was priced.
> Everything I lost came from thinking I knew something the price did not.

## Hoe te lezen

De reeks is geschreven om van voren naar achteren te lezen. Elke lecture opent
met **"Waar we zijn in het verhaal"**: het jaartal, wat we al weten, welke vraag
open staat. Elke lecture sluit met **"Wat er brak, en wat daarna kwam"**: de
barst in de theorie die het volgende tijdvak in gang zette. Wie springt, mist de
barsten, en de barsten zijn het verhaal.

Wie toch selectief wil lezen: de eerste twee lectures (opzet en de statistiek van
rendementen) zijn nodig voor alles wat volgt, en de lecture over $p = \E[mx]$,
[](#05-26-sdf-unificatie), is het scharnier waar de hele eerste helft in
terugkomt.

Elke lecture is zowel een webpagina als een notebook. Het download-icoon geeft
het `.ipynb`-bestand; het staat ook in de map `lectures/`. De tekst is
Nederlands. Code, variabelenamen en docstrings zijn Engels. Vaktermen blijven
Engels waar een vertaling gekunsteld wordt, met de eerste keer een korte
toelichting.

## Voorkennis

Waarschijnlijkheidsrekening en statistiek op masterniveau, wat lineaire algebra,
en genoeg Python om een `pandas`-DataFrame te lezen. Stochastische analyse
(Itô's lemma) wordt gebruikt maar telkens ter plekke uitgelegd. Wie de
Python-kant wil bijspijkeren, kan terecht bij de reeks van Sargent en Stachurski
waarop deze lectures qua vorm zijn gebaseerd:
[Advanced Quantitative Economics with Python](https://python-advanced.quantecon.org).

```{tableofcontents}
```
