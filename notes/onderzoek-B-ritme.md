# Onderzoek B: ritme en leesvloei (L1, L6, L11, L16)

Colleges: `00_01_rendementen`, `02_06_efficiente_markten`, `03_11_apt_no_arbitrage`,
`03_16_vroege_anomalieen`. Elk één keer volledig gelezen (.md). Regelnummers verwijzen
naar de huidige `.md`. Datum 2026-09-28.

## 0. Meting

`prose_stats` (huidige drempels) en een eigen telling op dezelfde prozatekst:

| college | words | sent_mean | p90 | dash | zinnen ≤ 8 w. | reeksen ≥ 3 korte zinnen (≤ 10 w.) | verbindingswoorden per 100 zinnen* | "dus" | "In woorden:" | "*Waarom zou dit waar zijn?*" |
|---|---|---|---|---|---|---|---|---|---|---|
| L1 | 5085 | 14,3 | 22 | 0 | 21% | 8 | 14 | 17 | 9 | 6 |
| L6 | 5457 | 14,4 | 23 | 0 | 18% | 3 | 12 | 23 | 7 | 5 |
| L11 | 5419 | 14,2 | 24 | 0 | 23% | 5 | 10 | 26 | 6 | 5 |
| L16 | 5287 | 16,0 | 25 | 0 | 16% | 1 | 15 | 22 | 6 | 5 |

\* maar, want, omdat, daardoor, daarom, toch, echter, immers, bovendien, dan ook, terwijl,
zodat, hoewel, juist, wel. Een lopende Nederlandse vaktekst zit eerder rond 25 tot 35.

Drie dingen vallen op. De gemiddelde zinslengte ligt ruim onder het maximum van 17
(de schrijvers schieten door naar kort). Geen enkel gedachtestreepje in vier colleges,
terwijl er tien mogen. En twee colleges zitten op 60 tot 90 woorden van de harde grens
van 5.500. De verbindingswoorden zijn dan het goedkoopst om te schrappen.

## 1. Top-10 patronen die het lezen stroef maken

Gerangschikt op frequentie maal hinder. Per voorbeeld: vindplaats, de passage zoals hij
staat, en een herschrijving met dezelfde inhoud en ongeveer dezelfde lengte.

### 1. Vaste etiketten per stap: "In woorden:", "*Waarom zou dit waar zijn?*", "Wat dit leert:"

28 keer "In woorden:", 21 keer "*Waarom zou dit waar zijn?*" (vaak midden in een alinea,
na de bewering waarop het de vraag is), 12 keer "Wat dit leert:". Het ritme wordt een
formulier: bewering, etiket, uitleg, etiket, formule, etiket. Een lezer hoort de
invulvelden.

- **00_01:336–339**
  > Over $k$ perioden groeit het verwachte logrendement met $k$ en de standaarddeviatie met $\sqrt{k}$. *Waarom zou dit waar zijn?* Een belegger die $k$ jaar vasthoudt, ziet goede en slechte jaren elkaar deels opheffen.

  → Over $k$ perioden groeit het verwachte logrendement met $k$, maar de
  standaarddeviatie alleen met $\sqrt{k}$. Dat komt doordat goede en slechte jaren
  elkaar deels opheffen: wie $k$ jaar vasthoudt, ziet zijn verwachte opbrengst
  evenredig groeien en zijn spreiding trager.
- **00_01:394–396**
  > In woorden: de standaardfout van het gemiddelde is de volatiliteit gedeeld door de wortel van het aantal jaren. Ze geldt voor elke reeks rendementen, simpel of log, premie of totaalrendement; alleen $\sigma$ verschilt.

  → De standaardfout van het gemiddelde is dus de volatiliteit gedeeld door de wortel
  van het aantal jaren, voor elke reeks rendementen: simpel of log, premie of
  totaalrendement. Alleen $\sigma$ verschilt.
- **03_11:412–413**
  > In woorden: de prijs, gemeten in spaarrekeningen, is een *martingaal* (een reeks waarvan de beste voorspelling van morgen de waarde van vandaag is).

  → Gemeten in spaarrekeningen is de prijs een *martingaal*: de beste voorspelling
  van morgen is de waarde van vandaag.
- **02_06:1204–1208**
  > Wat dit leert: de stelling van Samuelson zegt niet alleen dat termijnprijzen onvoorspelbaar zijn, maar voorspelt ook toetsbaar hoe hun onzekerheid in de tijd verloopt.

  → De stelling van Samuelson zegt dus meer dan dat termijnprijzen onvoorspelbaar
  zijn: ze voorspelt ook, toetsbaar, hoe hun onzekerheid naar de leverdatum toe groeit.

### 2. Staccato: reeksen korte hoofdzinnen zonder verbindingswoord

16 tot 23% van de zinnen heeft acht woorden of minder, en er zijn 1 tot 8 reeksen van
drie of meer korte zinnen per college. De logische relatie (want, maar, daardoor) staat
er niet; de lezer moet haar raden.

- **00_01:151–153**
  > Het verschil met het rekenkundig gemiddelde is $5 - 3{,}2280 = 1{,}772$ procentpunt. Dat is geen afrondingsfout. Over dertig jaar is het het verschil tussen $1{,}05^{30} = 4{,}32$ en $1{,}03228^{30} = 2{,}59$ euro: twee derde meer.

  → Het verschil met het rekenkundig gemiddelde, $1{,}772$ procentpunt, is geen
  afrondingsfout: over dertig jaar groeit een euro met 5% tot $4{,}32$ en met
  $3{,}228\%$ maar tot $2{,}59$, dus twee derde meer. (Ook "het het" verdwijnt.)
- **00_01:828–832**
  > Dat verschil scheidt twee effecten niet. Kleine aandelen deden het beter. En bij kleine aandelen springt de slotkoers heen en weer tussen bied- en laatkoers (*bid-ask bounce*). Maandelijks herbalanceren verkoopt na elke sprong omhoog en koopt na elke sprong omlaag, en boekt dat heen-en-weer zo als rendement.

  → In dat verschil lopen twee effecten door elkaar: kleine aandelen deden het beter,
  maar hun slotkoers springt ook heen en weer tussen bied- en laatkoers (*bid-ask
  bounce*). Wie maandelijks herbalanceert, verkoopt na elke sprong omhoog en koopt na
  elke sprong omlaag, en boekt dat heen-en-weer als rendement.
- **02_06:683–688**
  > De SDF prijst het rendement tot op de simulatieruis en is gemiddeld één. Hij is negatief in één op de honderdduizend maanden. Bij de gemiddelde premie vraagt dat een schok van [...] 7,5 standaarddeviaties, wat vrijwel nooit voorkomt. De negatieve maanden vallen daarom in toestanden met een hoge premie: [...]

  → De SDF prijst het rendement tot op de simulatieruis en is gemiddeld één. Negatief
  wordt hij maar in één op de honderdduizend maanden, want bij de gemiddelde premie
  vraagt dat een schok van 7,5 standaarddeviaties. Gebeurt het toch, dan in een maand
  met een hoge premie: [...]
- **03_11:88–91**
  > Draai het nu om. Als alle prijzen onderling kloppen, bestaat er een lijstje van twee getallen. Het eerste is de prijs van een euro alleen als het goed gaat, het tweede die van een euro alleen als het slecht gaat. Elke prijs is dan uitkering maal die toestandsprijzen. Beide moeten positief zijn.

  → Het werkt ook omgekeerd. Kloppen alle prijzen onderling, dan bestaan er twee
  getallen: de prijs van een euro die alleen uitkeert als het goed gaat, en die van een
  euro die alleen uitkeert als het slecht gaat. Elke prijs is dan de uitkering maal
  die toestandsprijzen, en beide moeten positief zijn.
- **03_11:1075–1078**
  > Het breekt op twee plekken. Shanken liet zien dat de Huberman-grens niet bestand is tegen herverpakken {cite}`Shanken1982`. Dezelfde economie kan in de ene set testactiva aan de grens voldoen en in een lineaire combinatie ervan niet. Een grens op een oneindige som is met eindige data niet te toetsen.

  → De APT breekt op twee plekken. De eerste vond Shanken: de Huberman-grens overleeft
  geen herverpakking, want dezelfde economie kan in de ene set testactiva aan de grens
  voldoen en in een lineaire combinatie ervan niet. Bovendien is een grens op een
  oneindige som met eindige data niet te toetsen.

### 3. De intuïtie wordt afgevinkt: "Dat is de tweede verwachting uit de intuïtie"

Elf keer (3/2/3/3). De zin draagt geen inhoud; hij meldt aan de beoordelaar dat H12 is
nageleefd. Op drie plaatsen in één college leest het als een checklist.

- **02_06:381–383**
  > De spotprijsverandering heeft de voorspelde helling van $-0{,}5$, de termijnprijsverandering een helling van nul. Dat is de eerste verwachting uit de intuïtie: de prijs is onvoorspelbaar, ook al is wat ze voorspelt dat niet.

  → De spotprijsverandering heeft de voorspelde helling van $-0{,}5$, de
  termijnprijsverandering een helling van nul. De termijnprijs is dus onvoorspelbaar,
  ook al is de spotprijs die ze voorspelt dat niet.
- **02_06:594–595**
  > Zolang $c > 0$ is de prijs dus nooit volledig informatief: bruto verdienen de geïnformeerden iets, netto niet. Dat is de derde verwachting uit de intuïtie.

  → Zolang informatie iets kost, is de prijs nooit volledig informatief: bruto
  verdienen de geïnformeerden iets, netto niet. De paradox uit de intuïtie is zo een
  evenwicht geworden.
- **03_11:619–622**
  > Dat portefeuilles goed geprijsd zijn en losse aandelen niet, is de derde verwachting uit de intuïtie. Voor wie één aandeel wil prijzen, zegt de APT bijna niets. Voor wie portefeuilles bouwt, zegt ze bijna alles.

  → Daarmee klopt ook het derde vermoeden uit de intuïtie: over één aandeel zegt de APT
  bijna niets, over een gespreide portefeuille bijna alles.
- **03_16:458**
  > Dit lost de tweede verwachting uit de intuïtie in, met een verfijning.

  → De stelling bevestigt zo de tweede verwachting, maar met een kanttekening.
- **00_01:454–456**
  > Alleen de eerste vraag past binnen een eeuw. Of er een premie is, valt te beantwoorden. Hoe groot hij is, vraagt honderden tot duizenden jaren. Zo lost de theorie de derde voorspelling uit de intuïtie in.

  → Alleen de eerste vraag past binnen een eeuw: of er een premie is, valt te
  beantwoorden, maar hoe groot hij is, vraagt honderden tot duizenden jaren.

### 4. Het motief als slotetiket: "Dat is de standaardfout van 2% uit ..."

Twaalf keer "standaardfout van 2%" (6/2/1/3), meestal als losse slotzin "Dat is X uit
[](#...)", plus een vaste motief-alinea aan het eind van elk Overzicht ("Op de vraag
theorie of feit ..."). Het motief wordt een stempel in plaats van een gedachte.

- **02_06:800–802**
  > Dit is de standaardfout van 2% uit [](#00-01-rendementen): bij 20% volatiliteit is een gemiddeld jaarrendement na een eeuw maar op 2 procentpunt nauwkeurig. Hier geldt dat voor een gemiddelde dat in de tijd beweegt.

  → Hetzelfde probleem troffen we bij het gemiddelde marktrendement, dat na een eeuw
  maar op 2 procentpunt bekend is ([de standaardfout van 2%](#00-01-rendementen)). Hier
  treft het een gemiddelde dat in de tijd beweegt.
- **03_11:782–784**
  > Dat is [de standaardfout van 2%](#00-01-rendementen) in een andere gedaante: een gemiddelde wordt nauwkeuriger met de wortel van het aantal maanden $T$, en meer aandelen helpen een los aandeel niet.

  → Meer aandelen helpen een los aandeel dus niet. Alleen meer maanden helpen, en dan
  nog met de wortel van $T$: de standaardfout van 2% in een andere gedaante.
- **03_16:660–661**
  > Een correct beprijsd verschil van bijna een procentpunt per jaar blijft na veertig jaar dus meestal onzichtbaar: de standaardfout van 2% uit [](#00-01-rendementen).

  → Een correct beprijsd verschil van bijna een procentpunt per jaar blijft zo na
  veertig jaar meestal onzichtbaar, om dezelfde reden waarom het gemiddelde
  marktrendement na een eeuw nog onzeker is.
- **03_16:385–387**
  > [...] niet het slecht gemeten gemiddelde, maar de goed gemeten covariantiematrix: de standaardfout van 2% uit [](#00-01-rendementen) in omgekeerde richting.

  → [...] niet het gemiddelde, dat slecht te meten is, maar de covariantiematrix, die
  goed te meten is.
- **02_06:70–73** (motief-alinea)
  > Op de vraag theorie of feit (is dit een theorie die getoetst wordt, of een feit dat op een verklaring wacht?) is het antwoord hier ongewoon. De efficiënte-markthypothese is een theorie, maar ze verbiedt pas iets als er een model van risico naast staat.

  → Is efficiëntie een theorie of een feit? Een theorie, maar een ongewone: ze
  verbiedt pas iets als er een model van risico naast staat.

  Hetzelfde sjabloon in 00_01:63–66, 03_11:67–72 en 03_16:69–71.

### 5. Definities en apposities tussen haakjes midden in de zin

Elke nieuwe term krijgt ter plekke een haakje met uitleg, vaak twee per zin (patroon
`*term* (definitie)` 12 keer, plus losse apposities). De hoofdzin breekt en de lezer
verliest het werkwoord.

- **03_11:670–673**
  > Twintig aandelen hebben een pricing error, in de simulatie zoals gebruikelijk $\alpha_i$ of alpha genoemd (de $\eta_i$ van de theorie), van 1% per maand, alle andere een alpha van nul, ongeacht $N$.

  → Twintig aandelen zijn fout geprijsd, met een pricing error van 1% per maand. In
  de simulatie heet die fout zoals gebruikelijk alpha; in de theorie was het $\eta_i$.
  Alle andere aandelen hebben een alpha van nul, hoe groot $N$ ook is.
- **02_06:289–293**
  > De toetsen uit [](#01-02-bachelier), autocorrelaties en variance ratios (de variantie over meerdere perioden gedeeld door het aantal perioden maal de eenperiodevariantie), meten eerste en tweede momenten. Ze toetsen dus een gevolg van de fair game, deel (ii): ongecorreleerdheid met de koersgeschiedenis.

  → De toetsen uit [](#01-02-bachelier), autocorrelaties en variance ratios, kijken
  alleen naar eerste en tweede momenten. Ze toetsen dus deel (ii), ongecorreleerdheid
  met de koersgeschiedenis. (De definitie van de variance ratio hoort in één eigen zin,
  of volstaat met de verwijzing naar [](#eq-rendementen-vr).)
- **02_06:1114–1118**
  > Dan was er echte winst te halen, en waren kosten de *limits of arbitrage* (grenzen aan wat arbitrageurs kunnen wegwerken, omdat handelen geld en risico kost) die de vergissing tot na 1990 lieten bestaan.

  → Dan was er echte winst te halen, maar hielden de kosten van handelen de vergissing
  tot na 1990 in stand. Zulke grenzen aan wat arbitrageurs kunnen wegwerken heten
  *limits of arbitrage*.
- **03_11:1085–1088**
  > De Chicago-lezing, die prijzen als rationeel ziet: SMB en HML zijn dominante richtingen van covariantie, dus niet weg te diversifiëren risico, en een premie daarop is wat de APT voorspelt. De Yale-lezing, die ruimte laat voor vergissingen van beleggers: [...]

  → Wie prijzen als rationeel ziet (de Chicago-lezing), leest SMB en HML als dominante
  richtingen van covariantie: risico dat niet weg te diversifiëren is, met precies de
  premie die de APT voorspelt. Wie ruimte laat voor vergissingen (de Yale-lezing), wijst
  erop dat [...]
- **00_01:92–95**
  > De volatiliteit van aandelen is ongeveer 20% per jaar, de *equity premium* (het extra rendement van aandelen boven de risicovrije rente, hierna de premie) ongeveer 6%.

  → De volatiliteit van aandelen is ongeveer 20% per jaar. Het extra rendement boven de
  risicovrije rente, de *equity premium* of kortweg de premie, is ongeveer 6%.

### 6. De verplichte handelende persoon

Elke waarom-alinea opent met "Een belegger die ...", "Een onderzoeker die ...", "Een
handelaar ...", of "Wie ...". Soms werkt dat; vaak is de persoon een stoplap en staan er
vier personen in vier zinnen.

- **00_01:237–242**
  > Een belegger die zijn vermogen twee jaar laat staan, krijgt het product van twee bruto rendementen, $R_{t+1}R_{t+2}$. Wie simpele rendementen over de tijd optelt, overschat dus wat hij overhoudt. Een belegger die zijn euro's over aandelen verdeelt, krijgt de gewogen som van hun simpele rendementen, want euro's tellen op. Wie daar logrendementen middelt, onderschat het portefeuillerendement.

  → Over de tijd vermenigvuldigen rendementen zich: twee jaar beleggen levert
  $R_{t+1}R_{t+2}$ op, en wie simpele rendementen optelt, overschat het eindvermogen.
  Over aandelen tellen euro's gewoon op: een portefeuille verdient de gewogen som van
  de simpele rendementen, en wie daar logrendementen middelt, onderschat haar rendement.
- **00_01:371–373**
  > *Waarom zou dit waar zijn?* Een onderzoeker die $T$ jaren middelt, laat toevallige goede en slechte jaren tegen elkaar wegvallen, maar dat gaat langzaam.

  → Bij het middelen vallen toevallig goede en slechte jaren tegen elkaar weg, maar
  dat gaat langzaam.
- **03_11:626–630**
  > Een onderzoeker die de covariantiematrix ontbindt, ziet bij veel aandelen dus $K$ richtingen boven de rest uitsteken, en die richtingen zijn de factoren.

  → In de covariantiematrix van veel aandelen steken dan $K$ richtingen boven de rest
  uit, en die richtingen zijn de factoren.
- **03_11:260–262**
  > Stel dat een claim op een euro alleen in de slechte toestand niets kost. Een handelaar koopt er dan onbeperkt van, want hij kan er alleen aan verdienen.

  → Kostte een euro die alleen in de slechte toestand uitkeert niets, dan kocht
  iedereen er onbeperkt van, want er valt alleen aan te verdienen.

### 7. Telegramstijl en fragmenten bij overgangen

Ondanks het verbod in §11.1 staan vooral in replicatie en "Wat er brak" zinnen zonder
werkwoord of met een losgezongen bijzin.

- **03_11:1025** "Eerst de drempels uit de verwachte afwijking." → "We toetsen eerst de
  drempels uit de verwachte afwijking."
- **03_11:1042–1043** "Alle vier liggen boven hun ondergrens. Dan de vergelijking met het
  origineel: het aantal geprijsde factoren." → "Alle vier liggen boven hun ondergrens.
  Blijft de vergelijking met het origineel: hoeveel factoren dragen een premie?"
- **02_06:1089–1090** "**Wat het model verklaart.** Veel, met één kleine aanname:
  concurrentie om informatie maakt voorspelbare winst na kosten onmogelijk." → "Met één
  kleine aanname, dat concurrentie om informatie voorspelbare winst na kosten wegneemt,
  verklaart het model veel."
- **02_06:1098** "**Waar het breekt.** Op een eigenschap die we hebben bewezen:" → "Het
  model breekt op een eigenschap die we zelf hebben bewezen:"
- **03_16:953** "**Wat het CAPM verklaart.** Nog steeds veel." → "Het CAPM verklaart nog
  steeds veel."
- **03_11:545–546** "Wie dat uitsluit, sluit niet uit dat één aandeel fors verkeerd
  geprijsd is. Alleen dat veel aandelen het allemaal zijn." → "Wie dat uitsluit, laat nog
  toe dat één aandeel fors verkeerd geprijsd is, maar niet dat veel aandelen het
  tegelijk zijn."

### 8. Mechanische routekaarten: "Eerst ... Dan ... Daarna ... Ten slotte"

Elke Theorie opent met een opsomming die leest als een inhoudsopgave in zinnen, met
herhaalde "Daarna" en soms een scheve tijdsvolgorde ("Eerst is een sortering ...").

- **02_06:233–239**
  > We leiden vijf dingen af. Eerst geven we drie woorden voor onvoorspelbaar een scherpe betekenis. Dan volgt de kern, [...]. Daarna laten we zien wat dat voor aandelen betekent: [...]. Omdat die SDF vrij te kiezen is, past vervolgens elk patroon [...]. Ten slotte laten we zien hoe het getoetst wordt: [...]

  → De kern is de stelling van Samuelson: een prijs die een voorwaardelijke verwachting
  is, verandert onvoorspelbaar. Daarvoor geven we drie woorden voor onvoorspelbaar een
  scherpe betekenis. Voor aandelen geldt de stelling pas na weging met de SDF, en omdat
  die vrij te kiezen is, past elk patroon van voorspelbaarheid erbij. We sluiten af met
  de toetsen: de drie vormen van Fama, de filterregel en de kosten van informatie.
- **03_11:190–195**
  > Eerst de fundamentele stelling: [...]. Dat is het recept van het toy-voorbeeld. Daarna wanneer die prijzen uniek zijn, en hoe de stelling naar veel perioden gaat. Daarna volgt wat de stelling voor verwachte rendementen voorspelt: [...]

  → De kern is de fundamentele stelling, het recept uit het toy-voorbeeld: geen
  arbitrage dan en slechts dan als er positieve toestandsprijzen zijn. Daarna kijken we
  wanneer die prijzen uniek zijn en hoe de stelling zich over veel perioden uitstrekt.
  Wat ze voor verwachte rendementen betekent, volgt uit de APT van Ross, eerst exact en
  dan met ruis.
- **03_16:222–224**
  > Eerst is een portefeuillesortering een regressie zonder vorm, met voor hoog min laag een Jensen-alpha en een eigen standaardfout. Dan blijkt een Fama-MacBeth-helling op een kenmerk een long-short-portefeuille.

  → We laten eerst zien dat een portefeuillesortering een regressie zonder vorm is, met
  voor hoog min laag een Jensen-alpha en een eigen standaardfout, en daarna dat een
  Fama-MacBeth-helling op een kenmerk het rendement van een long-short-portefeuille is.

### 9. Engels gedachte of scheve formuleringen buiten de calquelijst

`calque = 0` in alle vier, maar de lijst vangt alleen vaste woorden. Cleft-zinnen, "X
definieert het tijdvak", en vreemde collocaties glippen erdoor.

- **03_11:1060–1062** "Dat het aantal geprijsde factoren van de toets en de testactiva
  afhangt, is wat de critici van Roll en Ross aanvoerden." → "Juist dat voerden de
  critici van Roll en Ross aan: het aantal geprijsde factoren hangt af van de toets en
  de testactiva."
- **03_11:64–65** "Dit werk definieert het tijdvak omdat het prijzen losmaakt van
  voorkeuren." → "Met dit werk begint een nieuw tijdvak, omdat het prijzen losmaakt van
  voorkeuren." (Idem 03_16:69 "Deze artikelen definiëren het tijdvak omdat ...")
- **00_01:92** "Met de getallen van de echte wereld worden beide observaties knellend."
  → "Met realistische getallen gaan beide asymmetrieën knellen."
- **02_06:926** "Gedeeld met Fama en Blume is alleen dat het kleinste filter het meest
  verdient." → "Met Fama en Blume hebben we alleen gemeen dat het kleinste filter het
  meest verdient."
- **03_11:283–284** "Dat (2) arbitrage uitsluit, is de laatste zin van het waarom." →
  "Dat positieve toestandsprijzen arbitrage uitsluiten, zagen we al in het waarom."
- **03_11:425–426** "Die kans ligt tussen nul en één, dus de knoop is arbitragevrij, dan
  en slechts dan als $d < 1 + R^{f} < u$." → "De knoop is arbitragevrij dan en slechts
  dan als die kans tussen nul en één ligt, dus als $d < 1 + R^{f} < u$."
- **02_06:1001–1002** "Ook een moderne index is dus iets trager dan een fonds dat
  werkelijk wordt verhandeld." → "Ook een moderne index loopt dus iets achter op een
  fonds dat werkelijk verhandeld wordt."

### 10. "dus"-inflatie en "Dat is"/"Dit is"-openers

17 tot 26 keer "dus" per college, soms twee in één alinea (de regel staat in §11.1, de
check ontbreekt). "Dat" of "Dit" opent 10 tot 14 zinnen per college. Beide zijn het
directe gevolg van zinnen die in tweeën zijn geknipt: de tweede helft moet terugwijzen.

- **03_11:531–533** twee keer "dus" in opeenvolgende zinnen: "Een lineaire SDF prijst
  dus de activa waarop ze geschat is, maar kan [...] een negatieve prijs geven. De APT is
  dus zwakker dan [...]" → "Een lineaire SDF prijst wel de activa waarop ze geschat is,
  maar kan [...] een negatieve prijs geven. Daarom is de APT zwakker dan [...]"
- **03_11:443–445** "Heeft ze een positief verwacht rendement, dan koopt hij er
  onbeperkt van tot dat rendement nul is. Dus stijgt het verwachte rendement lineair met
  de bèta op elke factor." → "Heeft die portefeuille een positief verwacht rendement,
  dan kopen handelaars haar tot dat rendement verdwenen is. Daarom kunnen verwachte
  rendementen alleen via de factorbèta's verschillen, en wel lineair."
- **02_06:90–91** "Na een daling is het verwachte rendement dan hoger dan na een
  stijging. Dat is voorspelbaarheid, en toch vergist niemand zich." → "Na een daling is
  het verwachte rendement dan hoger dan na een stijging: voorspelbaar, zonder dat iemand
  zich vergist."
- **02_06:226–229** "Dat is de *joint hypothesis* (gezamenlijke hypothese: elke toets van
  efficiëntie is tegelijk een toets van een model van het vereiste rendement) in het
  klein." → "Het toy-voorbeeld toont zo in het klein de *joint hypothesis*: elke toets
  van efficiëntie is tegelijk een toets van een model van het vereiste rendement."

## 2. Oorzaakhypothesen

| patroon | vermoedelijke oorzaak | geciteerde regel |
|---|---|---|
| 1 "In woorden:" | STYLE §11.6 en §11.9 schrijven een lees-zin per vergelijking voor; het etiket is de goedkoopste manier om de afvinker te laten zien dat hij er is. | §11.6: "Vast ritme per stap: één of twee zinnen waarom we de stap zetten, de vergelijking, één zin die de vergelijking in woorden leest." §11.9: "Elke genummerde vergelijking heeft een lees-zin." |
| 1 "Waarom zou dit waar zijn?" | De kop uit §1 is in §11.6 een verplicht blok per resultaat geworden. | §11.6: "'*Waarom zou dit waar zijn?*' is een economisch beeld van twee tot vijf zinnen" |
| 1 "Wat dit leert:" | Letterlijk voorgeschreven, en via de calquelijst ook als vervanging van "Les:". | §11.7: "Elke uitwerking eindigt met een zin die begint met 'Wat dit leert:'." prose_stats CALQUES `(?m)^Les:` → "Wat dit leert:" |
| 2 staccato, 10 "Dat is"-openers | De zinsregel stuurt naar kort, en de streepjesregel schrijft "X. Dat is Y." zelfs voor. De maximumdrempels geven geen ondergrens, dus korter is altijd veilig. | §11.1: "Eén gedachte per zin. Richtlengte 12 tot 20 woorden"; "Een zin met een puntkomma wordt bijna altijd twee zinnen"; "'X — en dat is Y' wordt 'X. Dat is Y.'" prose_stats: `sent_mean: 17`, `sent_p90: 28` (alleen maxima). Gemeten: 14,2 tot 16,0 en 0 streepjes. |
| 2, 7 staccato en telegram | De harde woordgrens met "elk toevoegen betaal je met schrappen": verbindingswoorden, bijzinnen en overgangszinnen zijn het goedkoopst te schrappen. L6 en L11 zitten op 5.457 en 5.419. | §11.11: "De drempel van 5.500 woorden is bindend". workflow §2.4 en §9.2: "Elk toevoegen betaal je met schrappen elders"; "words blijft ≤ 5.500". |
| 3 inlos-zinnen | H12 vraagt dat de theorie de intuïtie "expliciet" inlost; de rubriek zet het onder criterium 2. | H12: "De theorie zegt expliciet waar die verwachting wordt bevestigd of verfijnd". Rubriek crit. 2: "De intuïtie doet een voorspelling die de theorie inlost." |
| 4 motief-etiket | De beoordelaar trekt af als het motief er niet staat of niet wordt uitgelegd; dus zet de schrijver het er vaak en met uitleg in. | §11.3: "De zin die het motief aanroept zegt wat het hier betekent." Rubriek, Wat niet meetelt 2: "Wel aftrek als de zin ter plekke niet zegt wat het motief hier betekent." |
| 5 haakjes | H2 en H10 eisen de uitleg "bij de eerste keer" en "in dezelfde zin". | H2: "Een symbool krijgt bij de eerste keer een naam, een betekenis en een orde van grootte". H10: "één concreet voorbeeld in dezelfde zin". |
| 6 handelende persoon | H1 eist een handelend onderwerp in elke waarom-alinea. | H1: "beschrijft iemand die iets doet (een belegger koopt ...; een onderzoeker sorteert ...)"; controle: "heeft de alinea een handelend onderwerp". |
| 8 routekaarten | De routekaart is verplicht en beschreven als volgorde. | §11.6: "`## Theorie` begint met een routekaart van drie tot vijf regels: wat we afleiden, in welke volgorde". |
| 9 "definieert het tijdvak" | Letterlijk overgenomen uit de opbouwregel. | §11.7: "één alinea geschiedenis: wie, wanneer, waarom dit werk het tijdvak definieert" |
| alle | Geen enkele fase leest op gehoor. De schrijver sluit af met de rubriek ernaast, F6b mag een punt alleen afwijzen "met een regel uit STYLE", en §10 beperkt tot 30 toolaanroepen en "één keer lezen". Een herleesronde op ritme past niet in het budget en wordt door niemand gevraagd. | workflow §2.1: "Lees tot slot je eigen lecture één keer met de rubriek ernaast". §9.2: "Wijs een punt alleen af met een regel uit STYLE of 'Wat niet meetelt'." §10.2: "Schrijver ≤ 30 toolaanroepen"; §10.3: "Het college één keer volledig". |

Kern: de regels zijn allemaal per zin of per element afvinkbaar, en elke regel is los
redelijk. Samen dwingen ze een tekst af die per zin klopt en per alinea hapert. Er is
geen regel, geen meting en geen fase die het geheel beoordeelt.

## 3. Overige verbeterpunten

- **Dubbele openingsvraag.** De vraag uit "Welke vraag staat open" wordt vrijwel woordelijk
  herhaald als eerste zin van het Overzicht: 00_01:30 en :36, 02_06:31 en :37, 03_16:29 en
  :36. Laat het Overzicht met het antwoord beginnen.
- **Te veel getallen per alinea** (§11.5, max drie): 00_01:92–100 (20%, 6%, 6,18%,
  1889–1978, 8,3%, 1926), 02_06:568–577 (0,175; 0,68%; 0,80; 0,095%; 24%), 03_11:1011–1023
  (c, 0,09%, 2469, 61 700, 757).
- **Onderzoekslog in de lezerstekst**: 03_16:79–81 ("Zijn tabellen hebben we niet kunnen
  inzien"), :474–477 en :764–766. Eerlijk, maar één keer in het replicatieblok volstaat;
  in de intuïtie onderbreekt het het verhaal.
- **03_16:58–67**: zes artikelen in één prozaalinea met zes citaties. Maak er een lijst of
  een kleine tabel van (jaar, auteur, kenmerk), zoals §11.1 voor drie of meer parallelle
  items vraagt.
- **03_11:1011–1023**: het argument dat een alpha van 0,09% "de APT niet schendt" gebruikt
  de willekeurige $c = 0{,}002$ uit de simulatie op echte data. Dat is logisch zwak; zeg
  liever dat de grens zonder bekende $c$ niets verbiedt.
- **03_11:37 en :219**: SDF wordt twee keer volledig gedefinieerd. **03_11:871** "De cel
  hierboven rekent alleen." is een metazin. **03_11:975** "TODO: naar hap.stats" staat in
  een zichtbare docstring.
- **02_06**: twee replicatieblokken (Fama-Blume en Jensen) in een college op 5.457
  woorden; Jensen zou een oefening kunnen worden, wat ruimte geeft voor verbindingswoorden.
  02_06:979: `yahoo([... "TLT", "GLD", "QQQ", "IWM"])` met commentaar "only SPY is used" is
  een cachetruc die de lezer verwart. 02_06:1106–1107 "zeventig (formule) tot tachtig jaar
  (simulatie)" hoort in een zin, niet in haakjes.
- **00_01:396–401**: de alinea over $s$ met deler 2 tegen 3 (22,9% tegen 18,7%) is te
  dicht; twee standaarddeviaties van dezelfde drie getallen verdienen een tabelregel in
  het toy.
- **03_16:204**: `print` in de toy-cel naast een tabel; beter een extra rij in de tabel.
- **03_16:558–750**: de simulatie heeft twee werelden, (a) en (b). Inhoudelijk sterk,
  maar §11.7 vraagt één steekproefvraag; de overgang tussen (a) en (b) mist een zin die
  zegt waarom ze samen horen (die staat pas in het figuurbijschrift, :749).
- **Figuren**: de leeswijzers vóór figuren zijn goed ("Let op ..."), maar staan vaak
  achter een alinea met een andere conclusie (02_06:728–731, 03_11:736–739), zodat "Let op"
  in dezelfde alinea een nieuwe gedachte opent.

## 4. Aanbevelingen

### STYLE.md

1. **§11.1** vervang "Eén gedachte per zin. Richtlengte 12 tot 20 woorden" door "Wissel
   korte en lange zinnen af. Een zin mag twee gedachten dragen als een verbindingswoord
   (want, maar, omdat, daardoor) hun verband uitdrukt." Schrap het voorschrift "'X — en dat
   is Y' wordt 'X. Dat is Y.'" en schrijf: "wordt een bijzin of een zin met 'wat' of
   'zodat'".
2. **§11.6** de lees-zin is verplicht, het etiket "In woorden:" niet; hoogstens drie keer
   per college. "*Waarom zou dit waar zijn?*" alleen bij de intuïtiekop en bij het
   kernresultaat, altijd vóór de stelling, nooit midden in een alinea.
3. **H12** de inlossing staat één keer, in "Samengevat" of in de slotzin van Theorie.
   Verbied "de eerste/tweede/derde verwachting uit de intuïtie" in de lopende tekst.
4. **§11.3** het motief hoogstens drie keer bij naam per college, en nooit als losse
   slotzin "Dat is de standaardfout van 2% uit ...". Schrap het vaste sjabloon "Op de vraag
   theorie of feit ..." aan het eind van het Overzicht; één zin in de geschiedenisalinea
   volstaat.
5. **H1, H2, H10** H1: "een handelend onderwerp óf een economisch mechanisme met een
   richting". H2/H10: "bij de eerste keer, in dezelfde of de volgende zin; hoogstens één
   haakje per zin".
6. **§11.7** vervang "waarom dit werk het tijdvak definieert" door "waarom dit werk een
   tijdvak opent of afsluit"; "Wat dit leert:" mag, maar de slotzin mag ook zonder etiket.
7. **Nieuw §11.12 Voorleestoets**: "Lees elke `##`-sectie na het herschrijven één keer
   hardop, zonder rubriek. Herschrijf elke alinea die u zo niet zou uitspreken. Bij een
   conflict tussen een meetregel en een natuurlijke zin wint de natuurlijke zin, mits
   `--check` nog PASS geeft."

### tools/prose_stats.py

1. **Ondergrens zinslengte**: `sent_mean` wordt een band 15–19 (nu alleen max 17; gemeten
   14,2–16,0).
2. **Nieuw `short_run`**: reeksen van drie of meer opeenvolgende zinnen van hoogstens tien
   woorden; max 3 per college (gemeten 1–8).
3. **Nieuw `connect`**: verbindingswoorden per 100 zinnen, minimum 20 (gemeten 10–15).
   Lijst als in §0.
4. **Nieuw `dus_para`**: aantal alinea's met meer dan één "dus", max 0 (regel bestaat in
   §11.1 zonder check); `dus` totaal max 15.
5. **Nieuw `template`**: "In woorden:" max 3, "verwachting uit de intuïtie|voorspelling uit
   de intuïtie" max 1, "standaardfout van 2%" max 3, "definie\w+ het tijdvak" max 0.
6. **Nieuw `opener`**: drie opeenvolgende zinnen met hetzelfde eerste woord, of meer dan
   8% van de zinnen die met "Dat is"/"Dit is" beginnen, rapporteren (drempel 0 resp. 8%).
7. **CALQUES** uitbreiden met cleft-vormen `\bis wat\b`, `\bwas de vraag van\b`, en
   `(?m)^(Eerst|Dan|Nu) de\b` (telegram).
8. **`words`** naar 5.800, of dropdown-uitwerkingen voor de helft laten tellen. Ongeveer 300
   woorden verbindingswoord en overgangszin is wat de vier colleges tekortkomen.
9. Kleine meetfout: de zinssplitser splitst alleen voor een hoofdletter, niet voor `$` of
   een cijfer; zinnen die met een formule beginnen, plakken aan de vorige. Voeg `\$` en
   `\d` toe aan de lookahead.

### Rubriek

1. Splits criterium 3 in **3a Taal** (10%: correct, geen calques, één naam per begrip) en
   **3b Ritme en leesvloei** (10%: "een 10 leest hardop als een goed Nederlands leerboek:
   afwisselende zinslengte, verbanden uitgedrukt, geen herhaalde etiketten"); haal de 5%
   uit criterium 1.
2. De beoordelaar citeert bij 3b de drie stroefste alinea's met een herschrijving, zodat de
   schrijver een voorbeeld heeft in plaats van een regel.
3. Voeg aan "Wat niet meetelt" toe: een ontbrekend etiket ("In woorden:", "Wat dit leert:",
   "de tweede verwachting") is geen aanmerking als de inhoud er staat.

### Schrijversprompt (workflow §2.1, §9.2)

1. Voeg na de verificatie toe: "Lees het college tot slot één keer op ritme, zonder rubriek,
   en herschrijf de tien stroefste alinea's. Reserveer daar drie toolaanroepen voor."
2. In §9.2: "Wijs een punt ook af als het de zin onnatuurlijk maakt; noem de alinea."
3. Laat de F23-lezer naast de vijftien lezerspunten vijf "stroeve alinea's" melden (vindplaats
   plus één regel waarom).

### Schatting

Van de ongeveer 490 prozaalinea's in deze vier colleges leest naar mijn schatting een
kwart (120 à 130) op minstens één plek stroef: een etiket, een staccatoreeks, een
haakjesstapel of een motiefstempel. Ongeveer één op de tien (circa 50) hindert echt,
zodat de lezer terug moet. L11 en L6 scoren het slechtst (meeste korte zinnen, minste
verbindingswoorden), L16 het best.
