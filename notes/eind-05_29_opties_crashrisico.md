STATUS 05_29_opties_crashrisico F6c words=5994 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,8 -> F6c 9,0.
# Eerste herziening (workflow §12)

Eindbeoordeling met verse ogen van `lectures/05_29_opties_crashrisico.md` na F1, F23 en F4T.
Getallen nagerekend tegen de celuitvoer (`tools/nb_outputs.py`) en, voor één bewering zonder
cel, tegen `hap.data.market_monthly()`.

## De drie verbeteringen met het meeste effect

1. **Twee feitelijke fouten in de replicaties herstellen** (replicatie 8,5 → 9,0, helderheid
   mee omhoog). (a) `05_29_opties_crashrisico.md:1342` en het bijschrift op `:1368–1369`
   zeggen dat de PutWrite-index "in beide crises bijna even diep" valt als de S&P 500, maar de
   eigen tabel (`:1333`) geeft $-32\%$ tegen $-51\%$ voor 2007–2009. Alleen voor 2020 klopt het.
   (b) `:1260–1262` zegt dat na oktober 2008 "juist hoge rendementen" volgden, maar de markt
   verloor daarna $7{,}7\%$, $13{,}7\%$ en $6{,}8\%$ over 1, 3 en 6 maanden, precies de
   horizonnen van de regressie. Alleen maart 2020 past bij de zin.
2. **Notatie en ontbrekende definities in Theorie** (helderheid 8,5 → 9,0). $\eta$ wordt in
   [](#prop-opties-crashrisico-premie) gebruikt (`:426`) en pas op `:445` benoemd; $R$ staat
   in [](#prop-opties-crashrisico-momenten) voor het log rendement (`:297`), terwijl
   Coval-Shumway (`:484`) en de setup $R$ als bruto rendement gebruiken (setup: $\ell$). Verder
   is "een ondergrens" (`:877`) zonder "van wat" en "59,1% per maand" (`:547`) zonder
   grondslag (premie? marge?).
3. **Presentatietabellen en figuurteksten in het Nederlands** (code en figuren 8,5 → 9,0). De
   PutWrite-tabel toont `mean_ann`, `std_ann`, `sharpe_ann`, `skew` (`:1320–1321`), de
   BTZ-tabel `beta`, `se`, `tstat`, `r2`, `nobs` (`:1204`), en de figuurtitel luidt
   "Voorspelt de VRP het excess rendement?" (`:1243`).

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,8

| criterium | gewicht | deelcijfer |
|---|---|---|
| 1. Helderheid | 25% | 8,5 |
| 2. Opbouw | 20% | 9,0 |
| 3. Taal | 20% | 9,0 |
| 4. Toy-voorbeeld | 10% | 9,0 |
| 5. Code en figuren | 10% | 8,5 |
| 6. Replicatie en empirie | 10% | 8,5 |
| 7. Oefeningen | 5% | 9,0 |
| **Eindcijfer** | | **8,8** (8,775) |

### 1. Helderheid — 8,5

*Goed*
- Toy-voorbeeld en Theorie: de factor $7{,}7$ uit het toy keert terug als continue SDF
  $q(s)/p(s)$ (`:268–269`), de $0{,}0332$ bij de VRP (`:350`) en $50{,}9\%$/$86{,}6\%$ bij
  Coval-Shumway (`:501–503`); H11 is sterk ingelost.
- Intuïtie → Theorie → Simulatie: de drie voorspellingen (puts onder de rente, VRP positief,
  rustige steekproef overdrijft) worden elk bij het resultaat ingelost (`:349`, `:501`, `:966`).
- Ruïnedrempel: formule, voorbeeld ($L=5$, $24\%$) en simulatie ($58\%$ bij $L=1{,}8$) staan
  naast elkaar (H4).

*Aanmerkingen*
- Hoeveel van de aandelenpremie is crashpremie?: "Onder $\mathbb Q$ geldt dezelfde vorm met
  $r$, $W^{\mathbb Q}_t = W^{\mathbb P}_t + \eta t$," — $\eta$ krijgt pas twintig regels later
  een naam (H2).
- Modelvrije momenten: "Met $R = \log(S_T/F)$ zijn dus ook de eerste drie momenten prijzen" —
  $R$ is in de setup en op `:484` het bruto rendement (H7/notatie).
- Simulatie: "is die Sharpe-ratio van de verkoper een ondergrens." — ondergrens van welke
  grootheid (de Sharpe-ratio in een markt waar ook diffusierisico duurder is onder Q?) staat
  er niet.
- Marges en de verkoper van puts: "verdient een verkochte put op 10% onder de koers gemiddeld
  $59{,}1\%$ per maand" — zonder grondslag is het getal niet te plaatsen.
- Verkopers van puts in het echt: "De figuur laat zien dat de PutWrite-index in beide crises
  bijna even diep valt als de S&P 500." — tegengesproken door de tabel erboven.

*Beter uitleggen*
- Waarom de smirk bij een jaar vlakker is (`:647–649`, "middelt ... uit tegen de diffusie"):
  één zin dat de diffusievariantie met $\tau$ groeit terwijl één sprong vast blijft, zodat het
  Poisson-mengsel naar een normale verdeling schuift.
- De verwijzing naar [](#prop-risk-management-drempel) (`:542`) herhaalt het geleende
  resultaat niet in één regel (H2).

*Voor een 9*: $\eta$ bij eerste gebruik benoemen (`:426`); $R$ in de momentenpropositie
vervangen door het setupsymbool (`:297–300`, ook oefening 3); "ondergrens" preciseren
(`:877`); grondslag van $59{,}1\%$ noemen (`:547`); de fout op `:1342` herstellen.

### 2. Opbouw — 9,0

*Goed*
- Overzicht, Intuïtie en Toy bouwen dezelfde vraag op (wat kost verzekering, en is dat te
  meten) en Wat er brak beantwoordt precies die vraag (`:1394–1395`).
- Numerieke oplossing verbindt Theorie en Simulatie: de kalibratie van Santa-Clara en Yan
  voedt zowel de smirk als de putverkoper.
- Drie replicaties in de volgorde van de theorie: dichtheid, VRP, putverkoper.

*Aanmerkingen*
- Theorie: acht `###`-secties; "Verwachte optierendementen" staat tussen crashpremie en
  marges en onderbreekt de lijn premie → verkoper, al is het resultaat nodig voor het toy.

*Beter uitleggen*
- Een overgangszin aan het begin van "Verwachte optierendementen" die zegt waarom de
  ordening nu nodig is (de verkoper van puts ontvangt precies het verlies van de koper).

*Voor een 9*: —

### 3. Taal — 9,0

*Goed*
- Zinslengte gemiddeld 18,4, p90 28, geen zin boven 40; geen telegramzinnen, geen u/je.
- Motiefnamen elk één keer; "Risico of vergissing?" als alinea-etiket in Wat er brak.
- Bewijsschetsen in lopende zinnen (Merton `:396–399`, Coval-Shumway `:494–499`).

*Aanmerkingen*
- Intuïtie: "maar een onderzoeker die de hoge Sharpe-ratio van een rustige periode voor
  kennis houdt, meent meer te weten dan de optieprijs" — zie hardop-toets.
- Overzicht: "wacht nog op een theorie die het beslist." — zie hardop-toets.
- Marges: "bij een crash die veel kleiner is dan de daling die zijn verplichting volledig
  opeist." — zie hardop-toets.
- Brongegevens: tien puntkomma's (vooral in lijsten, toegestaan) en in de bron nog veel
  afgebroken regels ("een\n$\mathbb Q$", "de\ndrift"); onzichtbaar na renderen, wel `rewrap`.

*Beter uitleggen*: n.v.t.

*Voor een 9*: —

### 4. Toy-voorbeeld — 9,0

*Goed*
- Zes stappen, elk met de hand na te rekenen; alle getallen kloppen (nagerekend).
- Tabel hand/code en een slotzin die zegt wat de getallen betekenen (`:202–204`).
- Oefening 1 varieert het toy en leert iets nieuws ($1/m_{\text{crash}}$).

*Aanmerkingen*
- Stap 4: "Zonder crashtoestand, met de andere kansen herschaald, geeft dezelfde rekensom
  $2{,}44\%$." — de enige uitkomst zonder handstap, terwijl de slotzin ("ruim twee derde van
  de aandelenpremie") erop rust.

*Beter uitleggen*
- Bij $2{,}44\%$ de twee herschaalde kansen ($0{,}663$, $0{,}337$) noemen, zodat de lezer het
  kan narekenen.

*Voor een 9*: —

### 5. Code en figuren — 8,5

*Goed*
- Elke cel heeft een zin ervoor en erna; elke figuur heeft een leeswijzer en een bijschrift.
- `merton_price` en `breeden_litzenberger` lezen als de formules.
- De BL-foutentabel (`:687`) maakt het ruisargument zichtbaar in één blik.

*Aanmerkingen*
- Verkopers van puts in het echt: de tabel toont `mean_ann`, `std_ann`, `sharpe_ann`,
  `skew`, `kurtosis` als rijlabels (`:1320–1321`).
- De variance risk premium als voorspeller: kolommen `beta`, `se`, `tstat`, `r2`, `nobs`
  (`:1204`); figuurtitel "(b) Voorspelt de VRP het excess rendement?" (`:1243`).
- Simulatie: de margelus `equity = np.where(alive & ~call & (day == DAYS_M), marked, equity)`
  (`:822–824`) comprimeert drie gevallen in twee regels.
- Simulatie: `margin_summary` wordt in de Sharpe-cel berekend maar pas in de volgende cel
  getoond (`:867–871`, `:886`).

*Beter uitleggen*
- In de margelus een commentaarregel per geval (einde maand, margin call, doorlopen).

*Voor een 9*: rij- en kolomlabels van de twee tabellen vertalen (`:1204`, `:1320–1321`);
"excess" → "over-" in `:1243`; de margelus uitschrijven (`:818–824`).

### 6. Replicatie en empirie — 8,5

*Goed*
- BTZ: tabel origineel/hier met helling, $t$ en $R^2$, een oordeel dat aan de verwachte
  afwijking vastzit, en de uitbreiding na 2007 als echte bevinding.
- SPY: de verwachte afwijking noemt een codefout-signaal (positieve scheefheid, negatieve
  dichtheid) en de tabel toetst precies dat.
- PutWrite: standaardfout van de Sharpe-ratio in de tabel, zodat het oordeel "niet te
  onderscheiden" onderbouwd is.

*Aanmerkingen*
- Verkopers van puts in het echt: "De figuur laat zien dat de PutWrite-index in beide crises
  bijna even diep valt als de S&P 500." en in het bijschrift "valt in de crisismaanden van
  2008 en 2020 bijna even diep" — onjuist voor 2008 ($-32\%$ tegen $-51\%$).
- De variance risk premium als voorspeller: "In oktober 2008 en maart 2020 ... werd de premie
  diep negatief en volgden er juist hoge rendementen." — onjuist voor oktober 2008.
- SPY en PutWrite: de tabellen zetten verwachting naast uitkomst, maar geen origineel getal
  (BKM-scheefheid, Saretto-Santa-Clara-rendement) naast het onze.

*Beter uitleggen*
- Bij SPY waarom 1926–2026 en niet 1990–2026 de maatstaf is, nu de 3-maandsscheefheid over
  1990–2026 ($-1{,}33$) even negatief is als onder $\mathbb Q$.

*Voor een 9*: de twee fouten herstellen (`:1260–1262`, `:1342`, `:1368–1369`); in de
SPY- of PutWrite-tabel één kolom met het gepubliceerde getal.

### 7. Oefeningen — 9,0

*Goed*
- Instap (toy met halve crashkans), afleiding (machtsfunctie-SDF → $\lambda^{\mathbb Q}$),
  uitbreiding van de replicatie (modelvrije momenten): precies de drie soorten.
- Elke uitwerking eindigt met wat ze leert (`:1445–1447`, `:1485–1488`, `:1524–1526`).

*Aanmerkingen*
- Oefening 3 vraagt "Vergelijk volatiliteit en scheefheid", maar de uitwerking bespreekt
  alleen de scheefheid ($0{,}148$ tegen $0{,}123$ blijft onbenoemd).

*Beter uitleggen*: n.v.t.

*Voor een 9*: —

## Feitelijke fouten

Alle toy-getallen, de ruïnedrempels ($24\%$, $58\%$), de Merton-kalibratie, de BL-foutentabel,
de simulatietabellen, de SPY-momenten, de BTZ-tabel (kolom "hier") en de PutWrite-tabel
kloppen met de celuitvoer. Wiskunde nagerekend: Breeden-Litzenberger, spanning-momenten,
VRP-teken, Mertonformule, ontbinding van de premie (teken van $\eta$ klopt), ruïnedrempel,
oefening 2.

| nr | regel | bewering | oordeel | bron | correctie |
|---|---|---|---|---|---|
| 1 | 1342, 1368–1369 | PUT valt in beide crises bijna even diep als de S&P 500 | onjuist | cel 16: $-0{,}316$ tegen $-0{,}509$ (2007–09); $-0{,}198$ tegen $-0{,}196$ (2020) | "in 2020 even diep en in 2008 twee derde zo diep" |
| 2 | 1260–1262 | na oktober 2008 en maart 2020 volgden hoge rendementen | onjuist voor 2008 | `market_monthly`: na okt 2008 $-7{,}7\%$, $-13{,}7\%$, $-6{,}8\%$ over 1/3/6 mnd; na mrt 2020 $+13{,}6\%$, $+22{,}9\%$, $+34{,}9\%$ | alleen maart 2020 noemen, of "na oktober 2008 eerst verdere verliezen" |

## Navertelling in vijf zinnen

Optieprijzen bevatten de hele risiconeutrale verdeling, en die geeft crashes een veel grotere
kans dan de werkelijke, omdat een dollar in een crash veel waard is. Daaruit volgen een
positieve variance risk premium, een smirk die Mertons sprongen verklaren, en een
crashpremie die een flink deel (in de kalibratie ruim twee vijfde) van de aandelenpremie
uitmaakt. Wie die verzekering verkoopt, verdient een premie met extreme negatieve
scheefheid, en met hefboom wordt hij uitgeschud lang vóór ruïne. Een steekproef van twintig
jaar meet vooral of er een crash in zat, zodat de Sharpe-ratio van de verkoper sterk
overschat kan worden en de echte PutWrite-index niet van de markt te onderscheiden is. De
optiemarkt meet dus de prijs van crashrisico goed, maar niet of die prijs een beloning of
een vergissing is. Dit sluit aan bij het Overzicht.

## Taal na de redactie

De redactie heeft goed gewerkt: de regeltaal en de H8-gevallen die `notes/taal-...` noemt zijn
weg, zinnen lopen met voegwoorden, en geen vakterm is van betekenis veranderd ("smirk",
"variance risk premium", "risiconeutrale kans", "notionele hefboom", "uitgeschud" en
"crashpremie" betekenen overal hetzelfde; "linkerstaart" is geen alias voor iets anders).
Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. `:92–94` "maar een onderzoeker die de hoge Sharpe-ratio van een rustige periode voor kennis
   houdt, meent meer te weten dan de optieprijs" → "maar een onderzoeker die de hoge
   Sharpe-ratio van een rustige periode als bewijs neemt, denkt meer te weten dan de markt
   die de optie prijst".
2. `:62–64` "wacht nog op een theorie die het beslist." → "..., daarover heeft nog geen
   theorie het laatste woord."
3. `:514–515` "bij een crash die veel kleiner is dan de daling die zijn verplichting volledig
   opeist." → "bij een crash die veel kleiner is dan de daling waarbij hij het volle
   notionele bedrag moet betalen."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Uitgangspunt: F6b-verantwoording (rapport, "R9-1"), college eenmaal volledig gelezen, getallen
gecontroleerd tegen `tools/nb_outputs.py` en tegen de tekst. `prose_stats --check`: PASS, 5994
woorden, zinnen gemiddeld 18,6, p90 28, geen zin boven 40, alinea gemiddeld 46.

### Getallencontrole

Alles wat de schrijver toevoegde of wijzigde is herleidbaar: $0{,}663$ en $0{,}337$
($0{,}65/0{,}98$, $0{,}33/0{,}98$); PUT $-32\%$ tegen $-51\%$ (2007-09: $-0{,}316$ tegen $-0{,}509$)
en $-19{,}8\%$ tegen $-19{,}6\%$ (2020); hefboom $0{,}9$ en $1{,}8$ met $0{,}5\%$ en $80\%$
uitgeschud; scheefheid $-2{,}14$/$-2{,}26$ tegen $-1{,}23$/$-1{,}30$ en volatiliteit $14{,}8\%$
tegen $12{,}3\%$ (cel 20); PUT-scheefheid $-1{,}66$ en $-11{,}06/-1{,}66 \approx 6{,}7$ ("ruim zes
keer"); $t = 0{,}6$ bij drie maanden over 1990-2026 ($0{,}597$). Het geciteerde $-11{,}06$ en
$59{,}1\%$ zijn gesourced in `notes/feiten-05_29_opties_crashrisico.md` (punt 3). De
herschreven margelus en het verplaatste `margin_summary` geven dezelfde uitvoer. Geen
niet-herleidbaar getal, geen nieuwe feitelijke fout.

### Per punt

| punt | oordeel |
|---|---|
| Feitelijke fout 1 (PutWrite "even diep") | opgelost: tekst en bijschrift zeggen 2020 even diep, 2008 twee derde; klopt met tabel |
| Feitelijke fout 2 (na okt. 2008 hoge rendementen) | opgelost: "eerst verdere verliezen", alleen maart 2020 hoog; conclusie afgezwakt |
| Verbetering 2: $\eta$, $R$, "ondergrens", $59{,}1\%$ | opgelost: $\eta$ in de propositie benoemd, $\ell$ overal, grondslag en ondergrens genoemd |
| Verbetering 3: tabellabels, figuurtitel | opgelost: `.rename` bij BTZ en PutWrite, "overrendement" |
| Voor een 9 helderheid (alle vijf) | opgelost |
| Beter uitleggen: smirk bij een jaar | opgelost (diffusie groeit met looptijd, één sprong niet) |
| Beter uitleggen: geleend resultaat drempel | opgelost (bijzin herhaalt het resultaat) |
| Opbouw: overgang Verwachte optierendementen | opgelost (eerste zin legt de band met de verkoper); acht `###` blijft, geen punt voor 9 |
| Hardop-toets 1-3 | opgelost, drie zinnen lopen natuurlijk |
| Taal: afgebroken regels in de bron | opgelost (rewrap); onzichtbaar na renderen |
| Toy stap 4 | opgelost (herschaalde kansen genoemd) |
| Code: margelus, `margin_summary` | opgelost (commentaar per geval, tabel bij de cel die hem toont) |
| Replicatie: gepubliceerd getal | opgelost voor PUT (rij met $-11{,}06$ en uitleg); BKM-getal niet, bronnen niet ingezien, geen bezwaar |
| SPY: waarom 1926-2026 | opgelost (één zin) |
| Oefening 3: volatiliteit | opgelost ($14{,}8\%$ tegen $12{,}3\%$) |

Verslechterd: niets. Nieuwe punten: geen.

## Eindcijfer van record (F6c): 9,0

Plafondregel toegepast: alleen criteria met een punt stijgen, en niet boven het in het
vooruitzicht gestelde cijfer (9,0).

| criterium | gewicht | F6 | F6c |
|---|---|---|---|
| 1. Helderheid | 25% | 8,5 | 9,0 |
| 2. Opbouw | 20% | 9,0 | 9,0 |
| 3. Taal | 20% | 9,0 | 9,0 |
| 4. Toy-voorbeeld | 10% | 9,0 | 9,0 |
| 5. Code en figuren | 10% | 8,5 | 9,0 |
| 6. Replicatie en empirie | 10% | 8,5 | 9,0 |
| 7. Oefeningen | 5% | 9,0 | 9,0 |
| **Eindcijfer** | | 8,8 | **9,0** |

Taal is 9,0 (niet onder 8), geen deelcijfer onder 8,5. Open: niets.
