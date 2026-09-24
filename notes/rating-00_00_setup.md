STATUS 00_00_setup F5c words=4998 prose=PASS open=0 cijfer=8,9 min=8,5

# Beoordeling 00_00_setup: Opzet, data en conventies

Toolkit-lecture zonder eigen onderwerp; de eigen kopjes in plaats van de acht vaste tellen
niet mee. Criterium 4 (toy) en 6 (replicatie) zijn beoordeeld op "Een eerste meting": de
formule $\sigma/\sqrt{T}$ met één gesimuleerde eeuw als toy, de echte markt (11,6%, 1,8
procentpunt) als replicatie. Alle zeven criteria zijn van toepassing; geen herweging.

## Eindcijfer: 7,5

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 7,5 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld (eerste meting) | 10% | 7 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie (eerste meting op echte data) | 10% | 6 |
| 7 | Oefeningen | 5% | 7 |

Gewogen: 0,3·7,5 + 0,2·8 + 0,15·8 + 0,1·7 + 0,1·8 + 0,1·6 + 0,05·7 = 7,50.

## 1. Helderheid van de uitleg (7,5)

*Goed*
- "De rode draad": het motief de standaardfout van 2% krijgt meteen zijn rekensom
  ($20/\sqrt{100} = 2$) en drie concrete gevolgen, elk met een getal (één op twintig
  factoren boven 1,96).
- "Een eerste meting": de *Waarom zou dit waar zijn?*-alinea geeft de orde van grootte
  (18 procentpunt spreiding tegen 11% midden) vóór de formule, en de formule krijgt
  direct haar getal.
- Elke databron krijgt een getal uit de eigen tabel in de lopende tekst (CAPE 18,5 naar
  40,2; VIX-mediaan 17,6; eenjaarsrente 15,7% en 0,13%).

*Aanmerkingen*
- "Notatie": "$R^{f}_{t+1}$ | risicovrij rendement, netto (2% is 0,02)" naast "$R_{t+1}$ |
  bruto rendement, $R = 1 + r$". De hoofdletter betekent in de ene regel bruto, in de
  volgende netto; "$R^{e} = r - R^{f}$" mengt daarna beide. De tabel die "verder nergens
  herhaald" wordt, is juist hier dubbelzinnig.
- "Een eerste meting": "Het geschatte gemiddelde hangt alleen af van de begin- en
  eindkoers, en dus van de lengte van de periode." Dat geldt voor het gemiddelde
  logrendement, niet voor het rekenkundig gemiddelde dat de lecture schat (zie
  Feitelijke fouten). De lezer krijgt hier de verkeerde reden voor de asymmetrie.
- "Goyal-Welch", figuurtekst: "Daardoor is in regressies met deze voorspeller de helling
  in kleine steekproeven naar boven vertekend, en is de $t$-waarde te groot." Geleend
  resultaat zonder de regel waarom (persistentie alleen geeft geen bias; de correlatie
  tussen de schokken in $D/P$ en in het rendement doet dat) en zonder naam.
- "De rode draad": "De equity premium puzzle verdwijnt niet met meer data." De term
  krijgt nergens in de lecture een zin uitleg, terwijl "Nederlands en Engels" belooft dat
  vaktermen de eerste keer een korte uitleg krijgen.
- "De gereedschapskist": "met een $t$-waarde van 0,95 op honderd jaarobservaties". De
  lezer heeft net gelezen dat Goyal-Welch vanaf 1871 loopt en in de figuur 155 jaar
  gezien; waarom de regressie er honderd heeft (`equity_premium` begint in 1926), staat
  er niet.

*Beter uitleggen*
- De asymmetrie gemiddelde/variantie: één zin dat het argument "alleen begin- en
  eindkoers" voor logrendementen geldt, en dat het rekenkundig gemiddelde er dicht bij
  ligt.
- De vertekening van de helling: een naam (Stambaugh) en één regel mechanisme.
- De equity premium puzzle: één zin wat de puzzel is (premie te hoog voor redelijke
  risicoaversie).

*Voor een 9*: maak de notatietabel consistent (bruto/netto voor $R^f$ en $R^e$, kopje
"Notatie"); herformuleer de begin-/eindkoerszin ("Een eerste meting", alinea na
`fig-setup-se`); geef de GW-bias een naam en een regel mechanisme (figuurtekst
`fig-setup-gw`); geef de equity premium puzzle één zin uitleg ("De rode draad"); zeg bij
de regressie waarom $T = 100$ ("De gereedschapskist").

## 2. Opbouw en rode draad (8)

*Goed*
- "Overzicht" stelt de vraag en geeft het antwoord met getal (11,6%, 1,8 procentpunt);
  dat getal komt terug in de eerste tabel, in "Een eerste meting" en in de volgende
  lecture.
- De eerste meting volgt zelf de trap: intuïtie met voorspelling, formule, één eeuw,
  tienduizend eeuwen, echte data, en "Zoals verwacht" lost de voorspelling in.
- 4.502 woorden: ruim onder de grens. "Wat er daarna komt" noemt drie concrete open
  vragen die 00_01 oppakt.

*Aanmerkingen*
- "Waar we zijn in het verhaal": "**Welke vraag staat open.** Wat is een rendement, en
  hoe goed kunnen we het meten?" Het Overzicht stelt een andere vraag ("Hoe is deze
  reeks opgebouwd, en hoe goed meten we met haar data het gemiddelde rendement op
  aandelen?"), en de eerste helft ("wat is een rendement") wordt uitdrukkelijk niet
  beantwoord ("zonder te zeggen wat een rendement is").
- "De data": acht bronnen achter elkaar zonder tussentijdse samenvatting; de rode draad
  (de standaardfout van 2%) keert alleen terug bij French, FRED, OSAP en Yahoo. Bij GSW
  en HKM eindigt de sectie met een losse bewering die nergens terugkomt ("De vorm van de
  curve draagt, naast het niveau, informatie over toekomstige rendementen.").
- "De gereedschapskist": de regressie op $\mathrm{dp}$ is een tweede meting midden in de
  gereedschapsbeschrijving; ze staat los van "Een eerste meting", terwijl ze hetzelfde
  motief illustreert.

*Beter uitleggen*
- Laat de vraag in "Waar we zijn" en in het Overzicht dezelfde zijn.
- Eén zin na de bronnentabel of aan het eind van "De data" die zegt wat de lezer uit de
  acht figuren moet meenemen.

*Voor een 9*: gelijke open vraag in "Waar we zijn" en "Overzicht"; bij elke databron
één zin die de figuur aan een motief koppelt (vooral GSW en HKM); verwijs vanuit
"Een eerste meting" terug naar de regressie in "De gereedschapskist" als tweede geval
van hetzelfde motief.

## 3. Taal (8)

*Goed*
- Korte zinnen (gemiddeld 14,2 woorden, één zin boven 40); geen u/je.
- De Engelse Santa-Clara-uitspraak staat als blokcitaat na een Nederlandse parafrase
  ("De rode draad").
- Vaste namen consequent: "de standaardfout van 2%", "risico of vergissing",
  "theorie of feit".

*Aanmerkingen*
- "Notatie": "De standaard is niveaus: $r$ is het netto simpele rendement." Vertaald
  Engels ("the default is levels").
- "De rode draad": "De opzet is dat ze in elke lecture waar ze spelen onder dezelfde naam
  terugkomen." Projecttaal over de reeks zelf, in plaats van wat de lezer eraan heeft.
- "Let op" opent zeven leeswijzers ("Let op de verticale as", "Let op hoe lang",
  "Let op: in deze dataset", "Let in de figuur op", "Let op de vorm", "Let op het jaar",
  "Let op hoe ver"); de herhaling wordt een tic.
- "Een eerste meting": "een waar gemiddeld excess rendement", en in tabel en legenda
  "waar gemiddelde": "waar" leest eerst als voegwoord.

*Beter uitleggen*
- Geen inhoudelijke stap die door taal verloren gaat; de punten zijn polijstwerk.

*Voor een 9*: herschrijf "De standaard is niveaus" ("Notatie"); schrap of herformuleer
de opzet-zin in "De rode draad"; varieer de leeswijzers; vervang "waar gemiddelde" door
"ware gemiddelde" of "werkelijk gemiddelde" ("Een eerste meting", tabel en legenda).

## 4. Toy-voorbeeld: de eerste meting (7)

*Goed*
- Eén mechanisme ($\SD(\bar r) = \sigma/\sqrt{T}$), met de hand in één regel na te
  rekenen: $0{,}20/\sqrt{100} = 2$ procentpunt.
- Eén gesimuleerde eeuw geeft 2,03 procentpunt; de tekst noemt het getal en het
  interval.

*Aanmerkingen*
- "Een eerste meting": geen tabel hand/code. De handwaarde (2,0) en de codewaarde (0,0203)
  staan in verschillende alinea's; ook $\sigma/\sqrt{2T} = 1{,}4$ tegen 0,0142 wordt alleen
  in proza vergeleken ("zoals de tabel laat zien").
- $\SD(\hat\sigma) \approx \sigma/\sqrt{2T}$ is een tweede, niet afgeleide formule; ze
  wordt als gegeven gebruikt en in oefening 2 opnieuw.
- Er is geen zin "wat de lezer nu weet" direct na het toy; die conclusie komt pas na het
  histogram ("Zoals verwacht is het gemiddelde na een eeuw nog slecht bekend").

*Beter uitleggen*
- Een regel waarom $\sigma/\sqrt{2T}$ (variantie van $\hat\sigma^2$ is $2\sigma^4/T$,
  deltamethode), of de expliciete opmerking dat dit in 00_01 wordt afgeleid.

*Voor een 9*: zet na de simulatiecel een kleine tabel met twee rijen (gemiddelde,
volatiliteit) en kolommen formule/simulatie (2,0 tegen 2,00; 1,4 tegen 1,42); geef
$\sigma/\sqrt{2T}$ één regel herkomst; sluit het toy af met één zin wat de lezer nu weet.

## 5. Code en figuren (8)

*Goed*
- Bijna elke cel heeft een zin ervoor en erna; vóór elke figuur staat waarop te letten
  ("Let op de verticale as: die is logaritmisch").
- Simulatiecode leest als de wiskunde: `mean_hat`, `se_hat`, `means`, `sds` als benoemde
  tussenresultaten.
- Figuurteksten zeggen wat te zien is en zetten het getal erbij (83,7% in juni 1932;
  laagste kapitaalratio 2,2% in februari 2009).

*Aanmerkingen*
- "Kenneth French" en de oefeningen: presentatietabellen tonen Engelse kolomnamen
  (`nobs`, `mean_ann`, `se_mean_ann`, `sharpe_ann`), terwijl de regressietabel wel
  Nederlands is ("coëfficiënt", "standaardfout"). De eerste tabel van de reeks is
  daarmee voor de lezer het minst leesbaar.
- `cel-setup-french`, `cel-setup-hkm`, `cel-setup-osap`:
  `f"...{worst_drop:.1%}".replace(".", ",")` is een truc in een figuurcel, drie keer
  herhaald.
- "Gürkaynak-Sack-Wright": `maturities` wordt in de tabelcel gedefinieerd maar pas in de
  volgende cel gebruikt, zonder dat de tekst dat zegt.
- `fig-setup-yahoo`: de leeswijzer vraagt naar de eindpunten ("Let op hoe ver de
  eindpunten uiteenlopen"), de figuurtekst redeneert over verschillen in gemiddeld
  rendement; bovendien is de bewering daar feitelijk onjuist (zie Feitelijke fouten).

*Beter uitleggen*
- Bij de eerste tabel één zin wat `mean_ann`, `std_ann`, `se_mean_ann` betekenen, of de
  kolommen hernoemen.

*Voor een 9*: Nederlandse kolomnamen in de tabellen van `summary_stats` ("Kenneth
French", oefeningen); de komma-opmaak niet als `.replace` in drie figuurcellen;
`maturities` naar de figuurcel; leeswijzer en figuurtekst bij Yahoo op dezelfde
grootheid laten slaan.

## 6. Replicatie en empirie: de eerste meting op echte data (6)

*Goed*
- De echte markt wordt tegen de formule gelegd: $18{,}3/\sqrt{100} \approx 1{,}8$, gelijk
  aan de standaardfout uit de tabel ("Een eerste meting", slotalinea).
- De verwachting staat vooraf: "We verwachten dus een standaardfout die na een eeuw nog
  een flink deel van het gemiddelde zelf is."

*Aanmerkingen*
- "Een eerste meting", slotalinea: "De echte markt gaf hierboven 11,6% gemiddeld, met een
  standaardfout van 1,8 procentpunt over 1201 maanden. De formule geeft met 18,3%
  volatiliteit hetzelfde". Getallen in lopende tekst, geen tabel formule/simulatie/data.
- Geen oordeel in de vorm Geslaagd / Gedeeltelijk / Niet geslaagd, en geen verwachte
  afwijking (bijvoorbeeld: maanddata met lichte autocorrelatie en dikke staarten, dus
  een kleine afwijking van $\sigma/\sqrt{T}$).
- De simulatie zegt dicht bij `Mkt-RF` te liggen (8,3%/18,4%), de replicatie gebruikt
  `Mkt` (11,6%/18,3%). De vergelijking wisselt ongemerkt van reeks.

*Beter uitleggen*
- Welke reeks wordt gerepliceerd (`Mkt` of `Mkt-RF`), en waarom.

*Voor een 9*: sluit "Een eerste meting" af met een tabel van drie kolommen (formule,
simulatie, data) voor gemiddelde, volatiliteit en standaardfout, op één reeks
(`Mkt-RF`, die de simulatie nabootst); voeg één zin verwachte afwijking en een oordeel
toe.

## 7. Oefeningen (7)

*Goed*
- Oefening 1 laat de lezer een loader en `summary_stats` gebruiken en toont het verschil
  tussen een ongecorreleerde en een gepaarde standaardfout; de uitwerking eindigt met
  "Wat dit leert".
- Oefening 2 is een directe variatie op de eerste meting (hoeveel jaar voor 0,5
  procentpunt) en een uitbreiding op echte data (twee helften).

*Aanmerkingen*
- Geen afleidingsoefening: $\sigma/\sqrt{2T}$ wordt in oefening 2.3 gegeven in plaats van
  gevraagd.
- Uitwerking oefening 2: "Met fijnere data daalt dat getal nog sterk, want de variantie
  profiteert van metingen binnen het jaar en het gemiddelde niet." Bewering zonder getal,
  terwijl het met maanddata in één regel uit te rekenen is.

*Voor een 9*: voeg een korte afleiding toe (variantie van $\bar r$, of van $\hat\sigma$
via de deltamethode); geef in de uitwerking van oefening 2.3 het aantal jaren met
maanddata (ongeveer $675/12 \approx 56$ jaar bij onafhankelijke maandrendementen).

## Feitelijke fouten

1. **`fig-setup-yahoo`**: "Bij 18% volatiliteit en twintig jaar data is de standaardfout
   van het gemiddelde $18/\sqrt{20} \approx 4$ procentpunt. Dat is groter dan bijna elk
   verschil in deze figuur." Nagerekend op de cache (2005–2026, dagrendementen,
   geannualiseerd): gemiddeld QQQ 16,5%, SPY 12,2%, GLD 12,1%, IWM 11,3%, TLT 4,0%. Van
   de tien paarsgewijze verschillen zijn er zeven groter dan 4 procentpunt (QQQ–TLT 12,5).
   Alleen de verschillen binnen SPY/GLD/IWM vallen eronder. Bovendien loopt de
   volatiliteit van 14,5% (TLT) tot 24% (IWM), niet één 18%.
2. **"Een eerste meting", alinea na `fig-setup-se`**: "Het geschatte gemiddelde hangt
   alleen af van de begin- en eindkoers". Waar voor het gemiddelde logrendement
   ($\bar\ell = (\log p_T - \log p_0)/T$); niet voor het rekenkundig gemiddelde van
   simpele rendementen, dat de lecture schat (11,6%) en simuleert. Dat hangt van het
   pad af.

Nagerekend en correct: 11,6% / 18,3% / 1,8 pp en `Mkt-RF` 8,3% / 18,4%; interval 8–15%;
drawdown 83,7% (juni 1932); CAPE-gemiddelde 17,8; VIX 9266 dagen, mediaan 17,6, max
82,7; GSW-yields; 212 signalen, mediane $t$ 4,0; HKM-minimum 2,2% (feb. 2009);
regressie 0,042, $t$ 0,95, 100 observaties; simulatie 8,5% / 2,0 / 4,5–12,4%; relatieve
fouten 25% en 7%; oefening 1 (Enrgy–Telcm 2,7; 3,7; 2,8; $t$ 0,99); oefening 2 (3,0 en
2,2; $t$ −0,2; 1350 en 675 jaar); 39 overige lectures.

## De drie verbeteringen met het meeste effect

1. **Eerste meting als echte replicatie** ("Een eerste meting"): tabel formule /
   simulatie / data op `Mkt-RF`, verwachte afwijking, oordeel. Replicatie 6 → 8; toy
   7 → 8 als dezelfde tabel de hand/code-vergelijking draagt.
2. **Helderheid op vier plekken**: notatietabel $R^f$/$R^e$, begin-/eindkoerszin,
   GW-bias met naam en mechanisme, equity premium puzzle in één zin. Helderheid
   7,5 → 8,5.
3. **Yahoo-figuurtekst corrigeren en de leeswijzer laten aansluiten**, plus Nederlandse
   kolomnamen in de `summary_stats`-tabellen. Code en figuren 8 → 9; samen met punt 2
   zijn beide feitelijke fouten weg.

## Navertelling in vijf zinnen

De reeks vertelt de geschiedenis van asset pricing als een opeenvolging van theorie,
nieuwe data en een feit dat de theorie niet aankan, met drie vaste motieven. Er is één
notatie ($p_t = \E_t[m_{t+1}x_{t+1}]$, payoffs op $t+1$) en alle data is gratis, gecachet
en offline te draaien via acht loaders in `hap`. CRSP en Compustat ontbreken, en dat
kost analyses op aandeelniveau. Het gemiddelde marktrendement over een eeuw is 11,6%
met een standaardfout van 1,8 procentpunt, precies wat $\sigma/\sqrt{T}$ voorspelt, terwijl
de volatiliteit veel scherper bekend is. Wat een rendement precies is, volgt in 00_01.
Dit komt overeen met het Overzicht; alleen de open vraag in "Waar we zijn" ("wat is een
rendement") wordt hier bewust niet beantwoord.

## Controle 1

Gecontroleerd op de versie na F5-1 (4.998 woorden, `--check` PASS). Alleen de eigen
punten; uitvoer van de gewijzigde cellen nagekeken in het notebook.

**Feitelijke fouten**
1. Yahoo-figuurtekst: **opgelost**. De cel toont nu per ETF gemiddelde, volatiliteit en
   standaardfout (2005–); SPY/GLD/IWM 12,2 / 12,1 / 11,3 (binnen één punt), QQQ–TLT
   12,5, standaardfouten 3,1 tot 5,2. Tekst en figuurtekst kloppen daarmee.
2. Begin-/eindkoers: **opgelost**. Het argument geldt nu uitdrukkelijk voor het
   gemiddelde logrendement, met de halve variantie naar het rekenkundig gemiddelde.

**1. Helderheid**
- Notatie $R^f$/$R^e$: **opgelost** (alinea "Twee conventies ... bewust";
  $R^e = R - (1+R^f) = r - R^f$).
- Begin-/eindkoerszin: **opgelost**.
- Goyal-Welch-bias: **opgelost** (Stambaugh, met het mechanisme in twee zinnen).
- Equity premium puzzle: **opgelost** (één zin, Mehra en Prescott).
- Waarom $T = 100$: **opgelost**.

**2. Opbouw**
- Open vraag gelijk aan het Overzicht: **opgelost**.
- Bronnen zonder samenvatting, GSW en HKM los: **opgelost** (slotalinea "Uit de acht
  figuren ..."; GSW en HKM aan risico of vergissing gekoppeld).
- Regressie los van de eerste meting: **opgelost** (terugverwijzing "een tweede geval
  van hetzelfde motief").

**3. Taal**
- "De standaard is niveaus": **opgelost**.
- Opzet-zin: **opgelost**.
- "Let op"-tic: **opgelost** (twee over).
- "waar gemiddelde": **opgelost** ("werkelijk gemiddelde").
- Nieuw, verslechtering: `fig-setup-gsw`, "Of dat een vergoeding voor risico is of een
  vergissing van de markt, is risico of vergissing in de obligatiemarkt." De zin zegt
  twee keer hetzelfde en leest als een tautologie.

**4. Toy**
- Tabel hand/code: **opgelost** (formule/simulatie 0,0200/0,0200 en 0,0141/0,0142).
- Herkomst $\sigma/\sqrt{2T}$: **opgelost** (vooruitwijzing naar oefening 2, afleiding daar).
- Zin wat de lezer nu weet: **opgelost** ("op een paar procent na ... op een kwart na").

**5. Code en figuren**
- Engelse kolomnamen: **opgelost** (`columns_nl` in alle `summary_stats`-tabellen).
- `.replace`-truc: **deels**. Eén helper `number_nl`, maar die staat in de verborgen
  figuurcel `cel-setup-french` en wordt later in `cel-setup-osap` en `cel-setup-hkm`
  gebruikt; de lezer ziet de definitie niet.
- `maturities`: **opgelost**.
- Yahoo leeswijzer/figuurtekst: **opgelost**.

**6. Replicatie**
- Getallen in proza, geen tabel: **opgelost** (tabel simulatie/data).
- Oordeel en verwachte afwijking: **opgelost** (blok met vijf onderdelen, "Geslaagd",
  1,84 en Newey-West 1,97 binnen 1,5–2,5).
- Wissel van reeks: **opgelost** (alles op `Mkt-RF`, met één zin over `Mkt`).

**7. Oefeningen**
- Geen afleiding: **opgelost** (oefening 2.3, deltamethode).
- Fijnere data zonder getal: **opgelost** (56 jaar met maanddata, nagerekend 56,25).

**Nieuwe cijfers**

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 7,5 | 9 |
| 2 | Opbouw | 20% | 8 | 9 |
| 3 | Taal | 15% | 8 | 8,5 |
| 4 | Toy | 10% | 7 | 9 |
| 5 | Code en figuren | 10% | 8 | 8,5 |
| 6 | Replicatie | 10% | 6 | 9 |
| 7 | Oefeningen | 5% | 7 | 9 |

Eindcijfer: 0,3·9 + 0,2·9 + 0,15·8,5 + 0,1·9 + 0,1·8,5 + 0,1·9 + 0,05·9 = 8,88, afgerond
**8,9**. Laagste deelcijfer 8,5. Streefcijfer (≥ 8,5, niets onder 8) gehaald.

Wat nog ontbreekt voor een 9 op taal en code: de GSW-zin herschrijven, en `number_nl`
in een zichtbare cel zetten (bijvoorbeeld direct na de imports).
