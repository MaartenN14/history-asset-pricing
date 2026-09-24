STATUS 00_00_setup F6 words=5014 prose=PASS open=2 cijfer=8,6 min=8,5

# Eindbeoordeling F6: 00_00_setup (Opzet, data en conventies)

Eindbeoordelaar A, Deel II. Cijfer van record volgens `plannen/rubriek-didactiek.md`.
De setup heeft bewust eigen kopjes. Criterium 4 (toy-voorbeeld) is n.v.t.; de overige
zes gewichten zijn herwogen naar 100% (deling door 0,90).

## Eindcijfer: 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | n.v.t. |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 8,5 |

(8,5·30 + 8,5·20 + 8,5·15 + 8,5·10 + 9·10 + 8,5·5) / 90 = 8,56 → 8,6. Laagste deelcijfer 8,5.

## Feitelijke fouten

1. **De data → Yahoo Finance.** "De cache bevat de dagelijkse, voor splitsingen en
   dividenden gecorrigeerde slotkoersen van vijf ETF's, en één momentopname van de
   optieketen van SPY." `data/cache/` bevat negen Yahoo-snapshots: behalve de vijf
   ETF's ook de 50 aandelen van L7, twee fondsenreeksen, `GSPC-PUT-BXM`, `SP500TR` en
   twee optie-snapshots van SPY (`yahoo_options__SPY__6` en `__28`). De zin klopt niet
   meer, en L7 laadt koersen die volgens deze zin niet bestaan (zie naad 6 in
   `eind-deel-2a.md`).
2. **Oefeningen → uitwerking ex-setup-2.** "De data kan dus niet uitmaken of de equity
   premium na de oorlog is veranderd." De steekproef is gesplitst in 1926–1975 en
   1976–2026, niet rond 1945. Het verschil is dat tussen de eerste en de tweede halve
   eeuw.

Nagerekend en correct (ter controle): 11,6% en SE 1,8 pp (`Mkt`); interval 8–15%;
83,7% terugval in juni 1932; CAPE 18,5 → 40,2 en gemiddelde 17,8; `dp` 4,3% → 1,1%;
VIX 9266 dagen, mediaan 17,6, max 82,7; GSW 15,7% en 0,13%; 212 signalen, mediane
$t$ 4,0; HKM-dieptepunt 2,2% in februari 2009; QQQ − TLT = 12,5 pp; helling 0,042,
SE 0,044, $t$ 0,95, 100 jaarwaarnemingen; simulatie 8,5% [4,5; 12,4]; 2,0 en 1,4 pp;
relatieve fout 25% en 7%; Newey-West 2,0; 2,7 pp, 3,7, 2,8, $t$ < 1; SE 3,0 en 2,2;
$t = -0{,}2$; 1350, 675 en 56 jaar; 39 andere lectures (40 in `lectures/`).

## 1. Helderheid van de uitleg (8,5)

*Goed*
- **De rode draad.** Het motief "de standaardfout van 2%" krijgt meteen zijn rekensom
  ($20/\sqrt{100} = 2$) en drie gevolgen, elk met een getal (6,18% en 8,3%, één op de
  twintig factoren).
- **Notatie.** De dubbele conventie (R bruto, $R^f$ netto) wordt uitgelegd met 1,08
  en 0,02, en er staat dat het excess rendement in beide schrijfwijzen hetzelfde getal is.
- **Een eerste meting.** "Waarom zou dit waar zijn?" voorspelt een SE die een flink
  deel van het gemiddelde is; formule, simulatie en data lossen dat in met dezelfde
  getallen.

*Aanmerkingen*
- **Goyal-Welch, bijschrift.** "Omdat de persistentie in een korte steekproef te laag
  wordt geschat, is de helling naar boven vertekend en de $t$-waarde te groot." Twee
  stappen (negatieve correlatie tussen de schokken, onderschatte persistentie) worden
  in één zin samengeperst tot een teken.
- **Gürkaynak-Sack-Wright.** "`SVENFnn` (instantane forward)": de term krijgt geen
  betekenis en wordt nergens gebruikt.
- **He-Kelly-Manela.** "We tonen de laatste drie maanden van de vier kolommen." Drie
  van de vier kolommen (`risk_factor`, `value_weighted_investment_return`,
  `leverage_ratio_squared`) krijgen geen uitleg.
- **Een eerste meting, slotalinea.** "Voor het gemiddelde logrendement is de reden
  exact. [...] Het rekenkundig gemiddelde ligt ongeveer een halve variantie hoger en
  is dus even slecht gemeten." De sprong van log naar rekenkundig is snel, en het
  argument voor de variantie ("wordt scherper met elke extra waarneming") zegt niet
  waarom waarnemingen *binnen* het jaar meetellen.

*Beter uitleggen*
- Stambaugh-bias: één zin met het mechanisme (een hoge koersschok verlaagt $D/P$
  en verhoogt het rendement, dus fouten in de persistentie lekken naar de helling).
- Fijnere data en variantie: één getal, bijvoorbeeld 12 onafhankelijke maandkwadraten
  per jaar tegen één, zoals oefening 2 al uitrekent (675 tegen 56 jaar).

## 2. Opbouw en rode draad (8,5)

*Goed*
- **Overzicht** stelt de vraag en geeft het antwoord (11,6%, SE 1,8 pp).
- **Een eerste meting** volgt de trap voorspelling → formule → simulatie → data, met
  8% en 20% als verbindende getallen, en keert terug naar de regressie uit de
  gereedschapskist (0,042 en 0,044).
- 5014 woorden, ruim onder de grens.

*Aanmerkingen*
- **Waar we zijn / Overzicht.** "Hoe is de reeks opgebouwd, en hoe goed meten we met
  haar data het gemiddelde rendement op aandelen?" Twee vragen; het Overzicht
  beantwoordt alleen de tweede met een getal.
- **Wat we niet hebben: CRSP en Compustat.** De samenvatting van de hele datasectie
  ("Uit de acht figuren nemen we drie dingen mee.") staat aan het eind van de
  CRSP-subsectie, waar ze bij CRSP lijkt te horen.
- De datasubsecties beginnen met een beschrijving van de bron, niet met hun conclusie.

*Beter uitleggen*
- Geef de datasectie een eigen slotalinea buiten "Wat we niet hebben", of zet de drie
  lessen vooraan in "De data".

## 3. Taal (8,5)

*Goed*
- Korte zinnen (gemiddeld 14,5 woorden), geen u/je, geen calques.
- Het Santa-Clara-citaat staat als blokcitaat met een Nederlandse inleiding.

*Aanmerkingen*
- **Kenneth French** en **Een eerste meting.** Wisselende namen: "volatiliteit
  (per jaar)" in de tabel, "met een standaarddeviatie van 18,3%" in de tekst direct
  eronder, en "de geschatte volatiliteit" bij $\SD(\hat\sigma)$.
- **Wat we niet hebben.** "meet een onderzoeker alleen de overlevenden"; L5 zegt
  consequent "overlevers" (zie naad 8).

*Beter uitleggen*
- Eén naam voor $\sigma$ in lopende tekst, bij voorkeur "volatiliteit".

## 4. Toy-voorbeeld (n.v.t.)

De setup heeft bewust geen toy-voorbeeld; de simulatie met 8% en 20% vervult die rol.

## 5. Code en figuren (8,5)

*Goed*
- Elke figuur heeft een vraag vooraf ("Rond welk jaar wordt de lijn steil?") en een
  bijschrift dat die vraag beantwoordt.
- De code is kort en leesbaar; `number_nl` wordt direct na de imports uitgelegd.

*Aanmerkingen*
- **Kenneth French, eerste figuur.** "De figuur hieronder toont wat die 11,6% over een
  eeuw oplevert. De verticale as is logaritmisch." Er staat niet waarop te letten; de
  diepste terugval, die de figuur annoteert, komt alleen in het bijschrift.
- **He-Kelly-Manela.** De cel toont vier kolommen, waarvan de tekst er één gebruikt.
- **Een eerste meting, laatste cel.** De rij "standaardfout, spreiding of Newey-West"
  zet twee verschillende grootheden in één rij.

*Beter uitleggen*
- Toon bij HKM alleen `intermediary_capital_ratio`, of zeg in één zin wat de andere
  kolommen zijn.

## 6. Replicatie en empirie (9)

*Goed*
- Het replicatieblok heeft bron, wat, data, verschil en verwachte afwijking (1,8
  in plaats van 2,0; band 1,5–2,5), ruim onder 250 woorden.
- Tabel simulatie/data, en een oordeel "Geslaagd" dat naar de verwachte afwijking
  verwijst.

*Aanmerkingen*
- De verwachte band "tussen 1,5 en 2,5 procentpunt" is zo breed dat de toets weinig
  kan laten mislukken; de scherpere verwachting (1,8 formule, enkele tienden erboven met
  Newey-West) staat er wel en wordt ook ingelost.

*Beter uitleggen*
- Geen.

## 7. Oefeningen (8,5)

*Goed*
- Beide uitwerkingen eindigen met "Wat dit leert".
- Oefening 2 combineert een afleiding (deltamethode) met een toepassing op data.

*Aanmerkingen*
- **Uitwerking ex-setup-2.** "Eerst de afleiding." De afleiding staat ná de codecel
  en beslaat één regel.
- Zie feitelijke fout 2 ("na de oorlog").
- Geen oefening die de replicatie uitbreidt (bijvoorbeeld Newey-West met andere
  vertragingen).

*Beter uitleggen*
- Zet de deltamethode vóór de cel, met de tussenstap $\Var(\hat\sigma^2) = 2\sigma^4/T$.

## De drie verbeteringen met het meeste effect

1. Stambaugh-mechanisme in één extra zin en de slotalinea over fijnere data met het
   getal uit oefening 2 (helderheid 8,5 → 9).
2. Twee vragen terugbrengen tot één, of beide in het Overzicht beantwoorden, en de
   drie lessen van de datasectie een eigen plek geven (opbouw 8,5 → 9).
3. De Yahoo-zin en "na de oorlog" corrigeren, en één naam voor $\sigma$ (feiten naar 0,
   taal 8,5 → 9).

## Navertelling in vijf zinnen

De reeks vertelt ruim 160 jaar asset pricing als een opeenvolging van theorie, nieuwe data
en een feit dat de theorie niet aankan, met drie motieven die steeds terugkeren. Alle
lectures delen één notatie, met $R$ bruto, $r$ en $R^f$ netto en de tijdsregel
$p_t = \E_t[m_{t+1}x_{t+1}]$. Acht gratis bronnen, offline gecachet, vervangen CRSP en
Compustat, ten koste van analyses op het niveau van het individuele aandeel. Het
gemiddelde marktrendement over een eeuw is 11,6% met een standaardfout van 1,8
procentpunt, precies wat $\sigma/\sqrt{T}$ voorspelt, terwijl de volatiliteit tot op
een paar procent bekend is. Die asymmetrie, de standaardfout van 2%, keert in de hele
reeks terug. De navertelling komt overeen met het Overzicht.

## Controle

STATUS 00_00_setup F6c words=5028 prose=PASS open=1 cijfer=8,6 min=8,5

Gecontroleerd tegen `rapport-00_00_setup.md` §F6-1 en de lecture zelf.

| punt | status | toelichting |
|---|---|---|
| Fout 1 / naad 6, Yahoo-cache | opgelost | de zin noemt nu vijf ETF's, vijftig aandelen, fondsen en indexreeksen en twee optie-snapshots; dat klopt met de negen `yahoo*`-bestanden |
| Fout 2, "na de oorlog" | opgelost | "tussen de eerste en de tweede halve eeuw" |
| Naad 8, overlevenden | opgelost | "overlevenden", gelijk aan L5 en de boekconventie |
| Naad 9, "empirische finance" | opgelost | de setup hield haar vorm; L7 is gelijkgezet |
| Verbetering 1, Stambaugh en fijnere data | niet | bijschrift Goyal-Welch en slotalinea ongewijzigd |
| Verbetering 2, twee vragen en de plaats van de drie lessen | niet | "Hoe is de reeks opgebouwd, en hoe goed meten we [...]" en "Uit de acht figuren [...]" in de CRSP-subsectie ongewijzigd |
| Verbetering 3, één naam voor $\sigma$ | niet | "met een standaarddeviatie van 18,3%" naast "volatiliteit (per jaar)" |

**Nieuwe feitelijke fout, ontstaan bij de herschrijving.** Yahoo Finance, de alinea na de
cachebeschrijving: "De cache begint in 1993, maar pas vanaf eind 2004 bestaan alle vijf de
ETF's." Nu de zin ervoor de hele cache beschrijft, klopt "De cache begint in 1993" niet
meer: de fondsenreeksen beginnen in 1980 en 1985, de indexreeksen in 1986. Bedoeld is
de ETF-reeks.

De deelcijfers zijn ongewijzigd, omdat de drie verbeteringen niet zijn uitgevoerd:

| nr | criterium | gewicht | nu |
|---|---|---|---|
| 1 | Helderheid | 30% | 8,5 |
| 2 | Opbouw | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | — | n.v.t. |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie | 10% | 9 |
| 7 | Oefeningen | 5% | 8,5 |

Eindcijfer **8,6** (herwogen over 90%), laagste deelcijfer 8,5. Open: één feitelijke fout.
