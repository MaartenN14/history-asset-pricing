STATUS 04_20_voorspelbaarheid F6c words=5853 prose=PASS open=0 cijfer=9,0 min=8,5

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6
8,7 -> F6c 9,0.

# Eerste herziening (workflow §12)

Eindbeoordeling F6 van `lectures/04_20_voorspelbaarheid.md` (alleen de .md gelezen;
getallen nagerekend tegen `tools/nb_outputs.py` en met één eigen controle op de
Goyal-Welch-data in `$TEMP/F6-04_20_voorspelbaarheid-chk.py`).

## De drie verbeteringen met het meeste effect

1. **Drie feitelijke fouten in de uitleg rechtzetten** (helderheid 8,5 → 9,0; opbouw blijft 9,0).
   (a) :675, de schuine wolk komt niet doordat een te lage $\hat\phi$ "beide hellingen"
   opdrijft. Een lage $\hat\phi$ drijft alleen $\hat b_r$ op. De dividendhelling
   verschuift nauwelijks, zoals :985–987 zelf uitrekent (bias 0,003). De wolk ligt schuin
   omdat dezelfde dividendschok via $\varepsilon^r = \varepsilon^d - \rho\varepsilon^{dp}$
   in beide hellingen terechtkomt, en de identiteit $\hat b_r = \hat b_d + 1 - \rho\hat\phi$
   laat $\hat\phi$ de wolk alleen horizontaal verschuiven.
   (b) :1180, "Met 60 tot 80 jaar data is dat te verwachten" past niet bij de echte toets,
   want de Goyal-Welch-regressie schat vanaf 1872. Bij de eerste voorspelling (1965) liggen
   er dus al 93 jaar data en in totaal 154 jaar. In de simulatie (cel 6) is de kans op
   verlies bij $T = 150$ nog 0,26 en niet "de helft". De zin moet het echte getal noemen.
   (c) :1183, "Dat de ratio beweegt, is dus uitstekend gemeten" is een betekenisverschuiving
   uit de redactie (HEAD: "Het tweede moment van $dp$ is uitstekend gemeten"). Dat de ratio
   beweegt is triviaal. De bewering die het college bewijst, is dat de ratio door
   verwachte rendementen beweegt.
2. **Replicatie-oordelen en getallen in proza** (replicatie 8,5 → 9,0). Alleen de som van
   de delen (:1155) opent met "Geslaagd". Fama en French (:887), Cochrane (:955) en Goyal en
   Welch (:1056) geven hun oordeel zonder het woord en zonder verwijzing naar de verwachte
   afwijking in het admonition (:801–806). :1155–1164 en :1056–1062 dragen elk vijf of meer
   getallen, die al in de tabellen staan.
3. **Eén naam per begrip en twee onverklaarde termen** (taal 8,5 → 9,0, helderheid mee).
   "dividendopbrengst" (:37) en "dividendrendement" (:813) naast "dividend-prijsratio";
   "het VAR" (:314, :372, :1241) wordt nergens benoemd; de "gecorrigeerde" $R^2_{OOS}$
   (:1056, kolom "idem, gecorrigeerd") wordt niet uitgelegd; hardop-zinnen hieronder.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,5 |
| | **gewogen** | | **8,7** (8,70) |

Geen deelcijfer onder 8,5; taal blokkeert niet. De streefwaarde van 9,0 is niet gehaald.

### 1. Helderheid (8,5)

*Goed.* De Campbell-Shiller-identiteit wordt in één regel herhaald, met $\rho = 25/26$ en
een uitgerekende benaderingsfout van 0,005 (Theorie, :264–267). Bij bijna elke formule
staat het getal: $b_r^{(5)}$, $R^2(k)$ van 15,7% en 23,7%, de Stambaugh-bias van 0,044 en
de 76 jaar die nodig zijn voor $t = 2$. Het argument van de hond die niet blafte wordt
kwantitatief gemaakt met de nulhypothese $b_d = -0{,}093$ (:351–358).

*Aanmerkingen.*
- Simulatie, "Onder de nulhypothese": "De wolk ligt schuin, omdat een toevallig te lage
  $\hat\phi$ beide hellingen tegelijk opdrijft" (:675). Dat klopt niet, zie verbetering 1a.
- Wat er brak, "Waar het breekt": "Met 60 tot 80 jaar data is dat te verwachten." (:1180)
  Zie 1b.
- Wat er brak: "Dat de ratio beweegt, is dus uitstekend gemeten, maar de helling waarmee
  hij rendementen voorspelt niet." (:1183) Zie 1c.
- Figuur `fig-voorspelbaarheid-hond`: "de lange-termijncoëfficiënt telt precies die hoek"
  (:671). $b_r^{lr}$ weegt beide hellingen via $\hat\phi$ en telt niet precies de hoek
  (1,3% tegen 1,8%).
- Theorie, "Het kernresultaat": "In het VAR voorspelt $dp_t$ het rendement" (:314). Het
  woord VAR valt hier voor het eerst en wordt nergens uitgelegd.

*Beter uitleggen.* Waarom de wolk schuin ligt (de gedeelde dividendschok). Wat de correctie
in "idem, gecorrigeerd" is: Goyal en Welch rapporteren een voor vrijheidsgraden
gecorrigeerde $R^2$, en die zin ontbreekt (:1056). Waarom Hodrick-1B met een trage
regressor in kleine steekproeven wel het juiste niveau heeft, terwijl Hansen-Hodrick dat
niet heeft (:415–417, geen getal of reden).

*Voor een 9.* :675 herschrijven naar het echte mechanisme; :1180 met de werkelijke lengte
(93 jaar schatten, 154 jaar totaal) en de kans uit cel 6; :1183 terug naar de
discontovoet; VAR benoemen bij :274 ("vectorautoregressie, VAR"); :1056 één bijzin over de
correctie.

### 2. Opbouw en rode draad (9,0)

*Goed.* Het Overzicht stelt de vraag en geeft het antwoord in drie zinnen (:36–43). De
intuïtie voorspelt teken en zwakke prestaties buiten de steekproef (:100–103), en beide
worden ingelost (:356, :777). De routekaart (:213–220) en Samengevat zijn er; $\rho =
0{,}96$ en de 78/22-verdeling uit het toy keren terug in Theorie (:265, :340) en Simulatie
(:570). Lengte 5.620 woorden.

*Aanmerkingen.*
- Intuïtie: "dan verklaart de voorspeller per jaar hooguit $4^2/20^2 = 4\%$" (:91) en
  Theorie "Bij $R^2(1) = 4\%$" (:396), maar Simulatie "De ware éénjaars-$R^2$ is dan
  ongeveer 5%" (:698–699) en oefening 2 5,07%. Twee kalibraties van dezelfde grootheid.
- Wat er brak: de koppeling van de echte toets aan de simulatie loopt via een verkeerde
  steekproeflengte (:1180).

*Beter uitleggen.* De brug van de simulatie ("met 60 tot 80 jaar is het kruis of munt") naar
de replicatie: hoe lang was de schattingsperiode van de echte toets, en welke kans hoort
daarbij?

*Voor een 9.* Staat op 9,0; hoger door één $R^2(1)$ door het hele college (:91, :396, :699).

### 3. Taal (8,5)

*Goed.* Zinnen gemiddeld 17,3 woorden, geen zin boven 40, geen gedachtestreepjes; motiefnamen
elk hoogstens één keer en telkens uitgelegd (:41, :532, :1185). De intuïtie leest als
gesproken uitleg (:71–95).

*Aanmerkingen.*
- Overzicht en Replicatie: "de dividend-prijsratio (de dividendopbrengst $D/P$)" (:36–37)
  en "Cochrane, die het dividendrendement afleidt" (:813–814). Drie namen voor één begrip.
- Theorie, buiten de steekproef: "Een mean-variance-belegger met risicoaversie $\gamma$, die
  hieronder uit de verhouding wegvalt, kiest" (:513–515). "Die" kan op de belegger slaan.
- Replicatie, Ferreira en Santa-Clara: "Een voorspelling zonder geschatte helling ontloopt
  de schattingsfout die de regressie in de simulatie de das omdeed." (:1116–1117)
- Wat er brak: "De variantie van de dividend-prijsratio moet ergens heen" (:1170).
  Bedoeld is "ergens vandaan komen".
- "log rendement" (:847), "logrendement" (:125) en "log totaalrendement" (:812) naast
  elkaar.

*Beter uitleggen.* Geen inhoudelijk punt.

*Voor een 9.* Eén naam (:37, :813), de drie hardop-zinnen hieronder, :1170 en de
spelling van logrendement gelijktrekken.

### 4. Toy-voorbeeld (9,0)

*Goed.* Vier jaar, drie hellingen, alles met de hand in vijf minuten (:139–171); tabel hand
naast code (cel 2, alles identiek); slotzin zegt wat 78% betekent (:206–209).

*Aanmerkingen.*
- Toy, stap 1: "Omdat alles afwijkingen van een gemiddelde zijn, betekent een negatief
  rendement hier 'onder het gemiddelde'" (:139–140). De drie rendementen zijn alle drie
  negatief (gemiddelde −0,053), dus ze zijn geen afwijkingen van hun eigen gemiddelde. Het
  rekent goed, maar de lezer die het narekent, struikelt.

*Beter uitleggen.* Dat de constante $\kappa$ en de gemiddelden bij de hellingen niet
uitmaken, omdat $\sum x = 0$; de zin staat er (:152–154), maar niet waarom de rendementen
dan niet op nul middelen.

*Voor een 9.* Staat op 9,0; hoger met één bijzin bij :139 over het niveau van de rendementen.

### 5. Code en figuren (8,5)

*Goed.* De identiteit is zichtbaar in `simulate_var` (:599–600); de Stambaugh-cel legt
formule en simulatie naast elkaar (:680–688); de drie figuren hebben een leeswijzer ervoor
en een conclusie erna, en de beschrijving van `fig-voorspelbaarheid-cumsse` (:1108–1110)
klopt met een eigen narekening (dp wint +0,05 in 1973–1975, verliest in 1995–1999, zakt na
2008).

*Aanmerkingen.*
- Simulatie: `cum = lambda a: np.cumsum(a, axis=1)[:, burn_in - 1:-1]` en de gevectoriseerde
  cumulatieve OLS in `oos_r2_sim` (:708–712) lezen niet als "schat elk jaar opnieuw".
- Tabelkoppen in het Nederlands zijn deels projectcode: "SOP maand", "Goyal-Welch
  R2-streep", "idem, gecorrigeerd" (cel 13 en 16).
- De import-cel (:107) heeft geen zin ervoor (klein).

*Beter uitleggen.* Een regel commentaar of een zin die zegt dat `beta` de OLS-helling op
alle data tot jaar $t$ is.

*Voor een 9.* `oos_r2_sim` (:704–717) met een zichtbare lus of benoemde tussenstappen;
"SOP" en "R2-streep" in de tabellen voluit ("som van de delen", "Goyal-Welch, gecorrigeerd").

### 6. Replicatie en empirie (8,5)

*Goed.* Het admonition noemt bron, wat, data, verschil en verwachte afwijking (:784–807);
elke replicatie heeft een tabel origineel naast hier; de Fama-French-$R^2$ klopt tot op
0,02 (cel 9) en de Cochrane-hellingen liggen binnen een vijfde standaardfout (cel 11).

*Aanmerkingen.*
- Fama en French: "Over 1941–1986 reproduceren we het patroon van Fama en French vrijwel
  getal voor getal" (:887). Geen oordeelswoord, geen verwijzing naar de verwachting "boven
  0,5".
- Cochrane: "Op de steekproef van Cochrane liggen onze hellingen binnen een vijfde
  standaardfout van de zijne" (:955). Idem.
- Goyal en Welch: "Het teken klopt, want over 1965–2005 is de gecorrigeerde $R^2_{OOS}$ bij
  15 van de 16 voorspellers negatief" (:1056–1057). Idem.
- Ferreira en Santa-Clara: "het tijdschriftartikel rapporteert een winst in Sharpe-ratio
  van 0,3" (:1164). Geen cel, geen paginaverwijzing.

*Beter uitleggen.* Welke verwachting uit het admonition bij welk oordeel hoort.

*Voor een 9.* Oordeelswoord plus verwijzing naar de verwachting bij :887, :955, :1056;
getallen uit :1155–1164 en :1056–1062 naar de tabel laten verwijzen.

### 7. Oefeningen (9,5)

*Goed.* Instap als variatie op het toy (ex-1, nagerekend: −0,0836, −0,25, −0,018,
−0,0776, −1,0776), een afleiding met simulatiecontrole (ex-2) en een uitbreiding van de
replicatie (ex-3). Elke uitwerking eindigt met wat ze leert (:1233–1235, :1303–1307,
:1346–1349).

*Aanmerkingen.* Geen.

*Beter uitleggen.* Geen.

## Feitelijke fouten

| nr | regel | bewering | oordeel | nagerekend |
|---|---|---|---|---|
| 1 | 675 | een te lage $\hat\phi$ drijft beide hellingen op | onjuist | Identiteit: $\hat b_r = \hat b_d + 1 - \rho\hat\phi$; bias op $\hat b_d$ is 0,003 (:987), op $\hat b_r$ 0,049 (cel 5). Schuinte komt van de gedeelde $\varepsilon^d$. Al zo vóór de redactie. |
| 2 | 1180 | "Met 60 tot 80 jaar data is dat te verwachten" | onjuist | Echte toets schat vanaf 1872 (eigen controle): 93 jaar vóór 1965, 154 in totaal. Cel 6: $P(R^2_{OOS}<0) = 0{,}26$ bij $T = 150$. |
| 3 | 1183 | "Dat de ratio beweegt, is dus uitstekend gemeten" | onjuist (betekenis veranderd in herziening) | HEAD: "Het tweede moment van $dp$ is uitstekend gemeten". De bewering van het college is dat verwachte rendementen de beweging dragen. |
| 4 | 671 | $b_r^{lr}$ "telt precies die hoek" | onzeker | Cel 3: 0,0132 voor $b_r^{lr}$ tegen 0,0178 voor $b_d$; verwant, niet dezelfde telling. |
| 5 | 1164 | Sharpe-winst van 0,3 bij Ferreira en Santa-Clara | onzeker | Geen cel; bron niet met tabel of pagina aangewezen. |

Nagerekend en juist: toy (alle negen getallen), $\rho = 25/26$ en fout 0,005,
$1-\rho\phi = 0{,}093$, "ruim twee standaardfouten" (2,3), $b_r^{(5)}$, $b_r^{(10)}$,
1,0246, $R^2$ 15,7% en 23,7%, Stambaugh −0,90 en 0,044, $\sigma_{dp} = 0{,}45$ en 76 jaar,
Campbell-Thompson-formule en 21%, cel 3 (22%, 1,8%, 1,3%), cel 5 (0,049 tegen 0,044), cel 6
(0,50/0,44; 0,076/0,051; 0,148), cel 8 (7%, 19%, 0,47), cel 9 en 10, cel 11 en 12 (0,004;
0,98; 0,041; 0,062 en $t = 1{,}57$), cel 13 (15 van 16, −4,2%, `ik` 2,29, `svar` 1,66), cel
14, cel 16, oefeningen 1 tot 3. Geen vakterm verschoven buiten fout 3; "prijs-dividendratio"
(:259, :265) is terecht $pd$ en geen alias van $dp$.

## Navertelling in vijf zinnen

De dividend-prijsratio moet per boekhoudidentiteit toekomstige rendementen of toekomstige
dividendgroei voorspellen. Omdat dividendgroei in de data niet voorspelbaar is, moet de
beweging van de ratio vrijwel volledig uit verwachte rendementen komen, en dat bewijs is
sterker dan de rendementsregressie zelf. De $R^2$ die met de horizon groeit, voegt geen
informatie toe, en overlap en de Stambaugh-bias maken de rendementsregressie te gunstig.
Buiten de steekproef verliest een geschatte helling vaak van het gemiddelde, ook als de
voorspelbaarheid echt is, terwijl een kleine $R^2$ economisch veel waard kan zijn en de som
van de delen zonder schatten wel wint. Of de wisselende premie risico of vergissing is,
beslist dit feit niet. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college leesbaar gemaakt: gemiddelde zinslengte 17,3, alinea's
gemiddeld 52 woorden, geen dubbele-puntlijm, en het Overzicht en de Intuïtie lezen als
gesproken uitleg. Er is één betekenisverschuiving (fout 3). Hardop-toets, drie zinnen die
nog niet natuurlijk klinken:

1. :513–515 "Een mean-variance-belegger met risicoaversie $\gamma$, die hieronder uit de
   verhouding wegvalt, kiest zonder $x_t$ het gewicht …"
   → "Een mean-variance-belegger met risicoaversie $\gamma$ kiest zonder $x_t$ het gewicht
   …; $\gamma$ valt straks uit de verhouding weg."
2. :1116–1117 "Een voorspelling zonder geschatte helling ontloopt de schattingsfout die de
   regressie in de simulatie de das omdeed."
   → "Een voorspelling zonder geschatte helling heeft geen last van de schattingsfout die
   in de simulatie de regressie nekte."
3. :1170 "De variantie van de dividend-prijsratio moet ergens heen, en de data wijzen één
   kant op."
   → "De variantie van de dividend-prijsratio moet ergens vandaan komen, en de data wijzen
   één bron aan."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Controle van `notes/rapport-04_20_voorspelbaarheid.md`, sectie "R9-1 (F6b, ronde 9+)",
tegen het college en tegen `uv run python tools/nb_outputs.py
lectures/04_20_voorspelbaarheid.ipynb`.

**Feitelijke fouten.**
1. :675, wolk schuin door lage $\hat\phi$ — opgelost. R. 682–688 wijst de schuinte nu aan
   de gedeelde schok $\varepsilon^r = \varepsilon^d - \rho\varepsilon^{dp}$ toe en laat
   $\hat\phi$ de wolk alleen naar rechts schuiven, via de identiteit.
2. :1180, "60 tot 80 jaar" — opgelost. R. 1203–1206 noemt de jaren 1870 en "ongeveer 150
   jaar data" met verlieskans "een kwart"; cel 6 geeft bij $T=150$
   $P(R^2_{OOS}<0)=0{,}262$, gelijk aan "een kwart".
3. :1183, betekenisverschuiving — opgelost. Nu "Dat de discontovoet beweegt, is dus
   uitstekend gemeten" (r. 1208).
4. :671, bijschrift "telt precies die hoek" — opgelost. Nu "vat $\hat b_r$ en $\hat\phi$
   samen in één getal" (r. 679).
5. :1164, Sharpe-winst 0,3 zonder bron — opgelost. Zin geschrapt, niet meer aanwezig.

**Drie verbeteringen.**
1. Helderheid — opgelost. Alle vier punten uit "Voor een 9" staan er: :675 herschreven,
   :1180 met echte lengte en kans, :1183 terug naar discontovoet, VAR benoemd bij de
   eerste keer ("vectorautoregressie (VAR)", r. 280) en :1056 met de zin over de
   correctie (r. 1074–1075).
2. Replicatie — opgelost. Fama-French, Cochrane, Goyal-Welch en de som van de delen
   openen nu alle vier met "Geslaagd" plus een verwijzing naar de vooraf gestelde
   verwachting (r. 903, 972, 1076, 1177). De getallen 0,16, 1,32 en −4,2% zijn uit de
   proza gehaald; alleen tabelwaarden en het afgeronde "−4%" (r. 1201) blijven.
3. Taal — opgelost. Eén naam "dividend-prijsratio" (dividendopbrengst en
   dividendrendement weg, met grep gecontroleerd), de drie hardop-zinnen herschreven (r.
   522–527, 1137–1138, 1192–1193) en "logrendement" overal dezelfde spelling.

**Overige "Voor een 9"-punten.**
- Opbouw: deels. Alleen de simulatiezin (r. 708–709) noemt nu 5% naast de 4% van
  intuïtie en theorie; die twee blijven bewust op 4%, gemotiveerd in het rapport (kaart
  §6: geen nieuw getal zonder cel). Geen hoger cijfer dan de bestaande 9,0 was beloofd,
  dus blijft 9,0.
- Toy: opgelost. Stap 1 (r. 142–145) legt nu uit dat de drie rendementen negatief zijn
  omdat $dp$ elk jaar stijgt (de markt werd goedkoper). Was al 9,0 zonder hoger cijfer in
  het vooruitzicht, blijft 9,0.
- Code en figuren: opgelost. `oos_r2_sim` heeft nu `mean_up_to_t` met docstring en
  commentaar (r. 721–723) in plaats van de lambda; tabelkoppen voluit ("som van de
  delen", "Goyal-Welch, gecorrigeerd", r. 1063–1064, 1168); de import-cel heeft een zin
  ervoor (r. 107).

**Beter-uitleggen (geen plafond, toch gedaan).** De reden waarom Hodrick-1B in kleine
steekproeven het juiste niveau heeft en Hansen-Hodrick niet, staat er nu (r. 421–424,
447–448).

**Hardop-toets.** Alle drie zinnen herschreven zoals voorgesteld — opgelost.

**Nieuwe punten.** Geen. Eigen controle van elk toegevoegd of gewijzigd getal
(`tools/nb_numbers.py`, `tools/nb_outputs.py`) vindt geen niet-herleidbaar getal onder de
wijzigingen van R9-1; de 33 meldingen van `nb_numbers.py` zijn dezelfde handrekenstappen
(toy, Stambaugh, $b_r^{(k)}$) die in de F6-beoordeling al als "juist" zijn nagerekend en
die R9-1 niet heeft aangeraakt. Geen verslechtering gevonden.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,5 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,475 = 9,025 -> 9,0. Geen deelcijfer
onder 8,5; taal blokkeert niet. Binnen het plafond van 9,1 uit F6.
