STATUS 01_02_bachelier F6b words=5457 prose=PASS open=1 cijfer=8,3 min=8

# Rapport L2 01_02_bachelier

## F0

**prose_stats (vóór):** words 8092, sent_mean 15.3, p90 24, gt40 0, para 45, dash 0,
semicol 13, motief 0, Lnum 0, deel 0, u 0, je 0, taboo 0, stopw 1, calque 0, engquote 3.
`--check`: FAIL alleen op `words=8092 (max 5500)`. `--where`: geen treffers.

**Vijf grootste problemen**
1. Lengte: 8092 woorden, vier dropdown-notes (diffusie, Bacheliers notatie, Cowles, Osborne:
   samen ~1.050) en een tweede toetsfamilie (runs) die geen kernvraag draagt (§11.11).
2. *Wat er brak*: "pas na dertig jaar weekdata zichtbaar" volgt niet uit de eigen getallen
   (feiten 18; H4, §11.11 Feiten).
3. *Waar we zijn* / *Overzicht*: "veertig jaar", "spreiding" voor Regnaults écart, en de
   verklaring in 1900 tegenover 1965 spreken elkaar tegen (feiten 1–3; H7).
4. *Replicatie Kendall/Lo-MacKinlay* (~840 woorden): runs, drie steekproeven, kwintielen en
   de gelijkgewogen index in lopende tekst, getallen in proza (§11.5), ongetoetste claims
   (tekenwissel na 1985, feiten 17).
5. *Bacheliers optieprijs*: de vergelijking met Black-Scholes (tekst, tabel, oefening 2)
   neemt ~650 woorden stof over die [](#02-09-black-scholes) behandelt (§11.11 eis 1).

**Eis 2 (grep op labels in `lectures/`):** buiten deze lecture wordt alleen het paginalabel
`01-02-bachelier` aangehaald (02_06, 02_09, 08_39, 00_01, 01_03). Geen `eq-`, `thm-`, `fig-`,
`ex-bachelier-*` elders. Inhoudelijk leunen 02_09 op Bacheliers optieformule en Regnaults wet,
02_06 op autocorrelaties, variance ratios en $z_2$; die blijven.

**Schraplijst (schraptoets §11.11)**

| kopje / passage | woorden | eis die ze niet haalt |
|---|---|---|
| note Diffusievergelijking | 320 | 1, 2, 3: niet nodig voor de vraag; label nergens aangehaald |
| note Bacheliers eigen notatie en toets | 230 | 1, 2: historisch detail, geen kernstap |
| BS-vergelijking na de optieformule (drie verschillen, BS-afleiding) → 1 alinea | 180 | 1: stof van 02_09 |
| oefening 2 Bachelier tegen Black-Scholes + uitwerking | 246 | 1: stof van 02_09; oefening 2 wordt de AR(1)-afleiding |
| note Cowles' telling | 190 | 1: één zin met citatie volstaat |
| note Osborne | 120 | 1: 02_09 noemt Osborne zelf; één zin volstaat |
| note Poincaré (Intuïtie) → één zin in Overzicht | 70 | 1 |
| runs-test (theorie + replicatie + cel) | 300 | 1: VR en autocorrelatie dragen de toets; 02_06 citeert runs niet |
| Working-alinea (Hoe getoetst) → één zin | 60 | 1 |
| Shiller-hellingtabel zonder cel + uitleg | 100 | 1; bovendien niet herleidbaar (feiten 12) |
| Lo-MacKinlay: getallen in proza, gelijkgewogen-alinea, dubbele oordeelzinnen | 150 | 1 |
| inkorten Overzicht, Intuïtie, Theorie-zijpaden, oefeningen, simulatietekst | 450 | 1 (herhaling) |
| **totaal geschrapt** | **~2.420** | |

**Verwachte lengte:** 8092 − 2420 ≈ 5.670 na schrappen; taak B (taal) haalt daar naar
verwachting nog 400–600 af, doel ≈ 5.100–5.300.

**Oordeel:** schrappen volstaat. De kern (random walk → √t → Brownse beweging, raakkans,
optieprijs, variance ratio, replicaties Regnault, Kendall, Lo-MacKinlay) blijft volledig;
alleen randstof en een tweede toetsfamilie gaan eruit. Geen splitsvoorstel.

## F1

**Eindmeting.** words 5279, sent_mean 15.1, p90 24, gt40 0, para 39, dash 0, semicol 13, stopw 1,
calque 0, engquote 1. `--check`: PASS. `--where`: geen treffers. Sync en `--execute` met
HAP_OFFLINE=1 foutloos, geen warnings in de uitvoer.

**Geschrapt** (zie F0-lijst): note diffusievergelijking (nevenresultaat, label nergens aangehaald);
note Bacheliers notatie en toets (historisch detail); BS-vergelijking ingekort tot één alinea
(stof van 02_09); oefening 2 Bachelier tegen BS (idem); notes Cowles, Osborne, Poincaré (elk één
zin in de tekst); runs-test in theorie en replicatie (tweede toetsfamilie, draagt de kern niet);
Working-alinea (één zin); Shiller-hellingtabel (niet herleidbaar); warning-zin over factor zoo
(vooruitverwijzing); print-cel limiet ex-1 (nu handberekening 1,1/0,9).

**nb_outputs-diff.** Alle aangehaalde getallen gelijk. Verschillen: cel 8 png 83900→83904 bytes
(tekstpositie label via `lm_years * 1.05` i.p.v. vaste 24.5); celkoppen 9 en 12 (commentaar
ingekort); runs-cel weg; print-cel ex-1 weg; ex-2 (impliciete σ, figuur) weg; celnummers
verschoven. `brentq`-import vervallen.

**Feitenpunten.** Verwerkt: 1 (37 jaar), 2 (1900 model, 1965 economische verklaring), 3 (gemiddelde
absolute afwijking), 4 (1,41), 5 (stuifmeel weg, "zwevende deeltjes"), 6 (Cowles-Jones-zin weg),
7 (runs weg), 8 (note weg), 9 (simulatie wijkt bij vijf jaar iets af, gezegd), 10 (185 jaar tegen
155 jaar Shiller, 1868 maanden), 12 (tabel weg), 13 (aantal "22" weg), 14 ("486" weg), 16 (elf
jaar), 17 (geen tekenwissel, z = −1,2), 18 (handberekening: kwintiel 1 ≈ 91 maanden ≈ 8 jaar,
week-ρ₁ ≈ 4270 weken), 19 (CRSP betaald, niet afwezig), 20 (vier kleinste kwintielen),
21 (Samengevat: discrete vorm plus "in de limiet exact twee"), 23 (Osborne-data weg).
Afgewezen of open: 11 (9,45 staat nu als "volgens hem"; tegen de bron nagaan, code blijft 9,45);
15 (bereik −0,013 tot 0,301 nu "in zijn tabel 3"; niet in de repo te controleren);
22 (L3 zegt "Kendall dat weekkoersen geen patroon hebben"; fout zit in 01_03, niet in mijn bestanden).

**STYLE §11.9, wat niet voldoet.** Elk getal herleidbaar: behalve 9,45 (punt 11) en Kendalls
bereik (punt 15). Overige: ok. Vooruitverwijzingen buiten "Wat er daarna kwam": één (02-09).

**Labels.** Verdwenen: `eq-bachelier-diffusie`, `ex-bachelier-2` (beide nergens in `lectures/`
aangehaald). Alle overige labels blijven; niets verhuisd.

**Open punten.**
1. Feit 11: Regnaults gedrukte 9,45 (of 9,46) nagaan in Regnault 1863 §83–84.
2. Feit 15: Kendall 1953 tabel 3, bereik en gemiddelde 0,13 nagaan.
3. Feit 22: 01_03 r. 26–27 spreekt deze lecture tegen (orkestrator/naadcontrole).
4. Kendall-periode 1928–1938 is ons venster, niet zeker het zijne (feit 14).
5. Werkmap bevat ook wijzigingen in 00_01, 01_03, 01_04 en hun rapporten; die zijn niet van mij.

## F4

**Meting.** words 5407, `--check` PASS. Sync en execute met HAP_OFFLINE=1 foutloos. Diff tegen
voor: als F1, plus de rij "Kendall-periode 1928-1938", die nu "interbellum 1928-1938" heet. De
Regnault-kolom komt uit de eigen rekensom 2,73·√k; de uitvoer blijft 0,998 en 0,995.

**Fouten (4/4).** "na hun publicatie" wordt "na hun steekproef" (twee plekken); de z-waarden
"tussen 1,2 en 2,0, het laagst bij q = 16"; het bijschrift zegt "lopen op tot q = 8"; bij de
simulatie staat "bij vijf jaar tot drie procentpunt af".
**Niet herleidbaar (5).** Regnault: "ongeveer 2,73 … geeft 4,73 en 9,46 [rekensom] tegen ongeveer
4,74 en 9,50"; 9,45 is weg. Het codecommentaar 1825–1862 is weg. Kendall: "tabel 3", "negentien"
en het bereik zijn weg; "ongeveer 0,13" blijft staan. Het venster heet nu "interbellum, ongeveer
de tijd van Kendalls reeksen".

**Lezerspunten 1–10.** 1: de Bachelier-volatiliteit heet nu v, het prijsniveau P_t, de
vervaldag t+τ; σ, S_n en T hebben elk één betekenis. De raakkans staat in W, met de
handberekening 1−Φ(0,5). 2: het Regnault-mechanisme met tabelgetallen (SD 0,183 tegen 0,199;
E|·|/SD 0,71 en 0,73 tegen 0,80). 3: de standaardfout van 2% met de grootheid erbij. 4: de
definitie van de Brownse beweging staat vóór de stelling. 5: E|Z| = 2φ(0) = √(2/π). 6: "geen
risicoaversie" als gevolg van de martingaalconditie. 7: wat Regnault mat staat in het blok.
8: de LM-index is waardegewogen. 9: de Kendall-alinea begint met de week. 10: 5223 weken
volstaan net, en 1,205 staat in de tekst. Ook 11–13 en deels 14. Afgewezen: 15 (de middeling
staat al in het blok). Betaald met een kortere routekaart, een kortere simulatie-opening en
oefening 3(3).
**Navertel-toets.** De afwijking zat in Replicatie (Regnault). De zin over de staatsobligatie is
vervangen door de twee oorzaken met getallen uit de eerste tabel.
**Open (1).** Feit 22 zit in 01_03 r. 26–27, buiten mijn bestanden.

## F5-1

**Meting.** words 5453, 0 puntkomma's, `--check` PASS. Sync en execute met HAP_OFFLINE=1
foutloos. Diff tegen voor: geen aangehaald getal veranderd. Nieuw zijn de handkolom
E|S_n|/√n in het toy en de kolom "gem. abs. afw. / SD" in de Regnault-tabel (0,7048 en
0,7340). Kolomnamen zijn nu Nederlands (Regnault, Kendall, vr_table).

**Feitelijke fouten.** 1 gedaan: 0,70 in plaats van 0,71, nu uit de nieuwe tabelkolom.
2 gedaan: "bij benadering normaal" geldt alleen bij onafhankelijke dagrendementen;
clusterende volatiliteit vertraagt dat.
**Helderheid.** Gedaan:
- de Regnault-redenering loopt nu tot het eind: de verhouding stijgt van 0,70 naar 0,73, de
  lage maandverhouding gaat mee naar de jaarhorizon, dus de jaarwaarde valt te laag uit;
- "afwijking" betekent alleen nog E|·| en "spreiding" de standaarddeviatie, in Overzicht,
  Intuïtie, toy, Kernresultaat, replicatieblok en instapoefening.
**Opbouw.** Gedaan:
- reflectie korter (waarom-alinea, barrièrezin weg) en met een rol: het eerste resultaat dat
  de verdeling van het hele pad vraagt, en daarom meer dan de CLT;
- "Hoe het getoetst wordt" opent met de conclusie.
Afgewezen: de twee replicaties inkorten. STYLE §1 en §6 schrijven het replicatieblok voor,
en de opdracht noemt Regnault, Kendall en Lo-MacKinlay als kern.
**Taal.** Gedaan: "definieert het tijdvak" wordt "Zonder Bachelier was Regnaults regel een
meting gebleven"; "Vooral hier:" is weg; alle 15 puntkomma's zijn weg.
**Code.** Gedaan: Nederlandse kolomnamen in de Regnault- en Kendall-tabel; de
vergelijkingscel bouwt nu vier benoemde lijsten in plaats van tupels.
**Replicatie.** Gedaan: minder getallen in proza. Kendall 0,030, SE 0,029 en VR 0,950/z −1,2
staan alleen nog in de tabel; Regnault 0,183/0,199 zijn weg, E|·|/SD staat als tabelkolom.
**Toy.** Gedaan: handkolom voor E|S_n|/√n.
**Open (1).** Feit 22, over 01_03 r. 26–27, valt buiten mijn bestanden.
- F5-1 vervolg: `{cite}`Kendall1953`` in de zinnen over "ongeveer 0,13" en "1928–1938, ongeveer de tijd van Kendalls reeksen"; --check PASS, execute ok.

## F6-1

**Meting.** words 5460, `--check` PASS. Sync en execute met HAP_OFFLINE=1 foutloos, uitvoer gelijk aan F5.
**Verbetering 1 (opbouw), gedaan.** Het bewijs van het reflectieprincipe is weggehaald; er staat
nu een bewijsidee van drie zinnen. Daarmee verdwijnt ook κ. De routekaart noemt nu de variance
ratio als doel, en zegt welke twee resultaten de replicatie toetst en welke niet.
**Verbetering 2 (helderheid), gedaan.** De Opzet noemt nu de wissel van T tegenover 00_01
(daar N waarnemingen, T jaren). De MAD/SD-uitleg bij Regnault opent met 0,70 / 0,73 tegen 0,80.
**Verbetering 3 (replicatie), gedaan.** De verwachte afwijking in het Regnault-blok zegt nu dat
zijn verhouding van bijna één niet te verwachten is. Het Lo-MacKinlay-oordeel luidt nu
"gedeeltelijk geslaagd voor de z-waarden (1,2 tot 2,0, onder de verwachte twee)". Het tweede
blok is ingekort.
**Overig, gedaan.** "Hij" in het Overzicht wordt "Bachelier". De martingaalaanname heeft nu een
regel met de BS-reden. De vergelijkingscel werkt met een helper `compare()` per benoemde rij.
De Working-herhaling in "Hoe getoetst" is geschrapt; Working blijft geciteerd in het Overzicht.
**Naadpunten.** 1 en 2: L2 klopt al met de setup (P_t in niveaus, overgang naar logs
aangekondigd). Er staat nu één zin bij dat r in de setup het simpele rendement is en hier een
logrendement. 3: R komt in L2 niet voor. 6: T-wissel genoemd (zie boven). 7: κ is weg.
9: geen wijziging nodig. L2 noemt de random walk "een feit met een statistisch model, maar
zonder economische verklaring", en dat spreekt de setup ("één model dat werd getoetst, het
CAPM") niet tegen.
**Afgewezen.** "Kendall en post-1985 in lopende tekst": elk staat al in een tabel, en de tekst
noemt alleen de getallen die het oordeel dragen (STYLE §11.5).
- F6-1 vervolg: ontbinding Regnault-kloof gecorrigeerd: ongeveer 2/3 door SD sneller dan √h (log 0,922 = −0,081), 1/3 door MAD/SD 0,70 → 0,73 (log = −0,041), samen log 0,885 = −0,122.
