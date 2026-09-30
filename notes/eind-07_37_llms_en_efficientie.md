STATUS 07_37_llms_en_efficientie F6c words=5801 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,6 -> F6c 9,0.

Eindbeoordeling F6 van `lectures/07_37_llms_en_efficientie.md` (1215 regels), na F1, F23 en
F4T. Getallen nagerekend tegen `$TEMP/F6-07_37_llms_en_efficientie-out.txt` (17 cellen) en
met de hand (toy, bewijzen, oefeningen). Alle in de proza aangehaalde celgetallen kloppen;
de fouten hieronder zijn fouten van formulering, eenheid of vakterm.

## De drie verbeteringen met het meeste effect

1. **Drie feitelijke onzuiverheden herstellen** (helderheid 8,5 → 9,0, replicatie 8,5 → 9,0).
   Het Samengevat-punt over $\omega$ zegt dat relatieve prijzen efficiënter worden naarmate
   $\omega$ stijgt (07_37:583-584). De liquiditeitshandelaren worden toegeschreven aan De
   Long e.a., wier noise traders op een verkeerde overtuiging handelen (07_37:332-333). De
   replicatietabel zet 0,4% per dag naast 0,15% over elf dagen (07_37:946).
2. **De twee losse eindjes van de rode draad vastknopen** (opbouw 8,5 → 9,0). Zeg in één
   zin waarom de ChatGPT-event study bij de theorie hoort, want geen van de drie proposities
   voorspelt een koerseffect op bedrijfswaarden (07_37:53, 07_37:818-822). Geef de voorspelde
   slechtere staart van advies één getal (07_37:567-572).
3. **Taal: vier zinnen herschrijven en één Samengevat-punt splitsen** (taal 8,5 → 9,0). Het gaat om
   07_37:63-65, 07_37:99-100, 07_37:1061-1064, het samengeplakte punt in 07_37:585-587 en de
   formule-opening in 07_37:594.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |
| | **gewogen** | | **8,6** (8,625) |

### 1. Helderheid (8,5)

*Goed.*
- Opzet en aannames, en het kernresultaat. Elke aanname staat genummerd bij de stap die
  haar gebruikt ("Zonder de ruis van aanname 3 ..."). Het bewijs heeft stapkoppen die zeggen
  wat ze opleveren, en de toy-getallen (restvariantie 1,5 en 1,2 tegen 1) staan naast de
  onverschilligheidsvoorwaarde (07_37:272-277). Ik heb alle drie de stappen nagerekend en ze
  kloppen.
- Wat het voorspelt. Elke uitkomst heeft een richting en een economische reden: meer ruis
  trekt meer geïnformeerden aan en laat $\rho^2$ gelijk. De grens $1/(1+\nu) \approx 0{,}86$
  wordt verklaard doordat risicoaversie en $\sigma^2_\varepsilon$ niet dalen.
- Gedeelde modelfouten. De propositie krijgt een handvoorbeeld met vier arbitrageurs en een
  tabel. De slotzin zegt wat het getal betekent: even nauwkeurig, maar de kans op de grootste
  daling stijgt van 1/16 naar 1/2.

*Aanmerkingen.*
- Samengevat: "Een gedeelde fout blijft in het gemiddelde staan ([](#eq-llms-en-efficientie-mono)), zodat relatieve prijzen wel en het marktniveau niet efficiënter worden naarmate $\omega$ stijgt."
  Letterlijk gelezen worden relatieve prijzen efficiënter als $\omega$ stijgt. Dat klopt niet
  (zie Feitelijke fouten).
- Advies als portefeuillekeuze: "Ze drukken allebei de mediane uitkomst, omdat bij samengestelde groei het log rendement telt en variantie daarin rendement kost."
  De reden geldt alleen voor spreiding. Handel kost via $\kappa\tau$ en niet via variantie.
- Gedeelde modelfouten: "De marktportefeuille houdt fout $\bar\beta g$, zoals de tweede oefening laat uitrekenen."
  $\bar\beta$ en $w_j$ krijgen geen naam of orde van grootte (H2).
- Advies als portefeuillekeuze: "Omdat het nut van de klant rond zijn optimum vlak is, groeit het verlies met het kwadraat van de duw, zodat een kleine duw bijna niets kost en een grote veel."
  Er staat geen getal naast (H4), terwijl de slechtere staart de helft van de adviesvoorspelling
  uit de Intuïtie is.
- Overzicht: "De kosten van informatie bleven daarna veertig jaar hoog, tot ze met ChatGPT eind 2022 zichtbaar daalden."
  Dit is te stellig, want EDGAR, internet en datavendors verlaagden die kosten al eerder.

*Beter uitleggen.* De lezer ziet niet waarom $\omega$ de efficiëntie van relatieve prijzen
niet raakt. De stap van "gedeelde fout over arbitrageurs" ($\omega$) naar "gemeenschappelijke
fout over aandelen" ($g$) moet in één zin: $g$ is de fout die over aandelen gemeen is en
$\omega$ bepaalt of die over arbitrageurs uitmiddelt. Daarnaast ontbreekt één getal voor de
duw van een platform, bijvoorbeeld omloop 300% in plaats van 75% met $\kappa = 2\%$.

*Voor een 9.*
- 07_37:583-584: schrijf dat een grotere $\omega$ de fout in het marktniveau vergroot, en dat
  relatieve prijzen efficiënter worden omdat de fout per aandeel wegmiddelt.
- 07_37:528-530: splits de reden (variantie voor spreiding, directe kosten voor handel).
- 07_37:427-432: noem $w_j$ (gewichten die optellen tot nul, bèta nul) en $\bar\beta \approx 1$.
- 07_37:567-572: één getal voor de staart, uit de al gebruikte $\kappa$ en $\tau$.
- 07_37:56-58: "bleven hoog" verzachten (zie Feitelijke fouten 4).

### 2. Opbouw en rode draad (8,5)

*Goed.*
- Het Overzicht stelt de vraag van Santa-Clara en geeft zijn antwoord (betere mediaan en
  slechtere staart, efficiëntere relatieve prijzen en een marktniveau dat niet efficiënter
  wordt). Het zegt ook eerlijk wat vaststaat en wat een vermoeden is (07_37:63-66).
- De toy-getallen keren terug in Theorie (07_37:241-242, 275, 338), in de Simulatie (dezelfde
  parameters, grens 0,86 bij $c = 0{,}01$ en $0{,}03$) en in oefening 1. De routekaart en
  Samengevat staan waar ze horen.
- 5592 woorden, onder de grens.

*Aanmerkingen.*
- Overzicht: "repliceren we een event study rond de lancering van ChatGPT {cite}`EisfeldtSchubertZhang2023`"
  Nergens staat welke voorspelling uit de theorie deze event study toetst. De proposities
  gaan over informativiteit, gedeelde fouten en halfwaardetijd, niet over bedrijfswaarden.
- Intuïtie: "Van goedkoop advies verwachten we dat de mediane particulier erop vooruitgaat, terwijl de slechtste uitkomsten slechter kunnen worden."
  De mediaan wordt ingelost met 3 procentpunt en de factor 0,41. De staart wordt alleen in
  woorden ingelost (07_37:567-572).
- Overzicht: "simuleren we wat één jaar data van beide mechanismen laat zien"
  "Beide" verwijst naar twee mechanismen, terwijl de Theorie er drie of vier behandelt.

*Beter uitleggen.* Maak in de inleiding van de replicatie de brug: de lancering is het enige
moment waarop $c$ zichtbaar sprong, en dan vraagt de event study of de markt dat meteen
prijsde. Zo hoort de event study bij het verhaal en is ze geen losse empirie.

*Voor een 9.*
- 07_37:53 en 07_37:818-822: één zin over wat de event study meet en waarom hier.
- 07_37:567-572: het getal uit punt H hierboven lost ook de staartvoorspelling in.
- 07_37:52: "beide mechanismen" vervangen door de twee namen (informatiekosten, gedeeld model).

### 3. Taal (8,5)

*Goed.*
- De statistiek is schoon: gemiddeld 17,6 woorden per zin, geen zin boven 40, alinea's van
  gemiddeld 55 woorden, geen gedachtestreepjes of puntkomma's, geen stopwoorden, geen
  "Wie ..."-zinnen. De motiefnamen staan elk hoogstens twee keer.
- Het verband loopt via voegwoorden, zoals in "Ten eerste lijken machines op elkaar. Tien
  analisten ...". Het Engelse citaat van Santa-Clara wordt ingeleid en direct uitgelegd, en
  het motto is een Nederlandse parafrase.
- De vaste namen "informativiteit" en "aanbodruis" blijven overal dezelfde.

*Aanmerkingen.*
- Overzicht: "Hier staat alleen de stelling van Grossman en Stiglitz vast, en zijn de snellere prijzen gemeten."
- Toy-voorbeeld: "Alle berekeningen in dit college gebruiken dezelfde pakketten en één vaste startwaarde voor het toeval."
  Dit is een aankondiging van de imports-cel in regeltaal.
- Wat er brak: "verliest het begrip efficiëntie, prijzen als verwachtingen onder het ware model, zijn houvast"
- Samengevat: "Een hogere dagelijkse autocorrelatie $\theta$ betekent tragere prijzen, ... en te weinig spreiding en veel handel kosten samen ongeveer drie procentpunt groei per jaar"
  Twee losse beweringen worden met "en" aan elkaar geplakt tot één punt van vijf regels.
- Simulatie: "De simulatie stelt één vraag: wat kan een onderzoeker met één jaar data van de twee mechanismen uit de theorie zien?"
  Dit is een formule-opening met een dubbele punt als lijm.
- Gedeelde modelfouten: "De liquiditeitshandelaren van {cite:t}`DeLongShleiferSummersWaldmann1990`"
  Het is een vakterm die door de redactie van betekenis is veranderd (zie Feitelijke fouten 2).

*Beter uitleggen.* Niet van toepassing.

*Voor een 9.*
- 07_37:63-65, 07_37:99-100 en 07_37:1061-1064: herschrijven, zie de hardop-toets hieronder.
- 07_37:585-587: splits het punt in twee (autocorrelatie, en advies).
- 07_37:594: zeg de vraag zonder aankondiging, bijvoorbeeld "Hoeveel van beide mechanismen
  ziet een onderzoeker in één jaar data?".

### 4. Toy-voorbeeld (9,0)

*Goed.*
- Het toy is in vijf stappen met de hand na te rekenen, heeft één mechanisme en een tabel
  met hand en code. De slotzin zegt wat het getal betekent (van 50% naar 80%, nooit 100%).
- De getallen zijn slim gekozen ($e^{2ac} = 1{,}5$ en $1{,}2$), zodat elke wortel rond uitkomt.
- De laatste kolom (waarde van het signaal = $c$) bewijst de onverschilligheid zonder dat het
  bewijs gelezen hoeft te worden.

*Aanmerkingen.*
- Toy-voorbeeld: "Hierin meet $\nu$ de aanbodruis ten opzichte van het signaal, en zet $k$ de kosten $c$ om naar de schaal van de varianties."
  Waarom de factor $e^{2ac}$ is, blijft tot het bewijs onduidelijk. Het is toegestaan als de
  ene nog niet afgeleide formule.

*Beter uitleggen.* Een halve zin dat $e^{2ac}$ de verhouding van de restvarianties is (1,5
tegen 1) zou het recept minder magisch maken.

### 5. Code en figuren (9,0)

*Goed.*
- Elke cel heeft een zin ervoor en erna. Vóór elke figuur staat waarop te letten, zoals
  "De vraag bij de figuur is of de lijn na dag 0 de band verlaat."
- De asserts toetsen hand tegen code en vraag tegen aanbod (07_37:627). De functies lezen als
  de wiskunde (`gs_equilibrium` volgt de propositie regel voor regel).
- De figuurteksten zijn Nederlands en zeggen wat er te zien is.

*Aanmerkingen.*
- Replicatie: "TICKERS = sorted(sum(GROUPS.values(), OTHER))". Het samenvoegen van lijsten met
  `sum` is een truc.
- Simulatie: `p0 = (-z_bar + (1 - lam) * mu_s * (1 - rho2) / (a * V)) / A` heeft geen verwijzing
  naar de vergelijking in stap 1 van het bewijs.

*Beter uitleggen.* Een commentaar bij `gs_price` dat p0 en p1 de coëfficiënten zijn uit de
marktruimingsvergelijking in stap 1.

### 6. Replicatie en empirie (8,5)

*Goed.*
- De admonition is volledig. Beide oordelen beginnen met Niet geslaagd of Gedeeltelijk
  geslaagd en verwijzen naar de verwachte afwijking.
- De placebovensters (268, spreiding 3,4 procentpunt) maken het ruisniveau zichtbaar. De
  coronacrash wordt apart gezet (−0,34 in 2020, −0,02 daarna).
- De bescheidenheid is terecht: niet-synchrone handel, futures en ETF's worden genoemd, en de
  conclusie luidt "verenigbaar met, bewijst niet".

*Aanmerkingen.*
- Replicatietabel: "| meerrendement hoog − laag, dag 0 t/m 10 | 0,4% per dag (samenvatting) | 0,15% |"
  Hier staat een grootheid per dag naast een cumulatieve over elf dagen.
- Data hier: "vooraf ingedeeld in acht bedrijven met vooral code-, tekst- en datawerk (*hoog*) en twintig met fysiek werk (*laag*)"
  De acht hardwareaandelen verschijnen pas in 07_37:820-822. Bij het lezen van de admonition
  telt 8 + 20 niet op tot 50.

*Beter uitleggen.* Geef in de tabel beide kolommen per dag (0,4% tegen ongeveer 0,01%) of
beide over elf dagen (ongeveer 4,4% tegen 0,15%). Noem de hardwaregroep en de veertien
uitgesloten aandelen al in "Data hier".

*Voor een 9.*
- 07_37:946: dezelfde eenheid in beide kolommen.
- 07_37:804-806: de indeling 8 + 8 + 20 + 14 = 50 in de admonition.

### 7. Oefeningen (9,0)

*Goed.*
- Er is een instap (het toy met dubbele ruis), een afleiding ($c^* = 0{,}0323$, nagerekend) en
  een uitbreiding van de replicatie (gevoeligheid van de event study).
- Elke uitwerking eindigt met wat ze leert. Oefening 2 zegt scherp dat het marktniveau alleen
  efficiënter wordt als modellen verschillender worden, niet beter.

*Aanmerkingen.* Geen.

*Beter uitleggen.* Niet van toepassing.

## Feitelijke fouten

Alle celgetallen in de proza kloppen na narekening, onder meer 0,003, 0,016–0,045, 2,59,
0,006, −0,41/−0,51, −2,44 (4,4 keer −0,558), 0,15%, 4,1, 51e percentiel, 268, 3,4, −8,5%,
0,29, 3,6 en 1,8 uur, −0,34/−0,02, z = −1,04, 10%/22%, +1,46%, +0,44% en 0,514. Ook het
toy, de drie bewijsstappen, het AR(1)-bewijs en oefeningen 1 en 2 kloppen.

1. **07_37:583-584 (Samengevat), onjuist.** "zodat relatieve prijzen wel en het marktniveau
   niet efficiënter worden naarmate $\omega$ stijgt". Een grotere $\omega$ maakt geen van
   beide efficiënter; ze vergroot de fout in het niveau. De tweedeling komt uit de
   decompositie $g$ tegen $\eta_j$ (07_37:427-432), niet uit $\omega$.
2. **07_37:332-333, onjuiste vakterm.** "De liquiditeitshandelaren van
   {cite:t}`DeLongShleiferSummersWaldmann1990`". De noise traders van DSSW handelen op
   verkeerde overtuigingen (sentiment), niet om liquiditeitsredenen. De redactie maakte
   "liquiditeitshandelaren" (07_37:218, de GS-aanbodruis) tot één naam. Daardoor schrijft deze
   zin het model een type belegger toe dat daar niet voorkomt. Herstel: noem DSSW's handelaren
   "noise traders die op een verkeerde overtuiging handelen", of laat de verwijzing naar DSSW
   weg en spreek van "de liquiditeitshandelaren van aanname 3".
3. **07_37:946 (replicatietabel), eenheid.** 0,4% per dag staat naast 0,15% cumulatief over
   elf dagen. Per dag is het hier ongeveer 0,014%, en de tabel onderschat het verschil
   daardoor met een factor 11.
4. **07_37:56-58, onzeker.** "De kosten van informatie bleven daarna veertig jaar hoog". EDGAR
   (1993–1996), internet en goedkope data verlaagden ze al eerder, en de tekst heeft er geen
   bron voor. Voorstel: "daalden daarna geleidelijk, en met ChatGPT eind 2022 met een sprong".

## Navertelling in vijf zinnen

Santa-Clara vraagt wat bijna gratis informatieverwerking met advies en marktefficiëntie
doet. Met Grossman en Stiglitz leidt het college af dat goedkopere informatie meer beleggers
laat meedoen en prijzen informatiever maakt, maar nooit volledig, omdat risicoaversie en
fundamentele onzekerheid een grens zetten. Als veel beleggers hetzelfde model gebruiken,
middelt hun fout niet weg. Daardoor worden relatieve prijzen efficiënter en het marktniveau
niet, en groeit de staart van de prijsfout zonder dat één jaar data dat laat zien. Goedkoop
advies verbetert de mediane particulier via spreiding en minder handel, maar een platform
dat aan transacties verdient, maakt de slechtste uitkomsten slechter. Empirisch is de
ChatGPT-lancering met gratis data niet in koersen terug te zien, en daalde de dagelijkse
autocorrelatie van de markt, wat past bij snellere prijzen maar het niet bewijst.
Dit wijkt niet af van het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijk gemaakt. De tekst leest als gesproken academisch
Nederlands, met voegwoorden, conclusies vooraan en geen zichtbare sjablonen. Er is één
vakterm van betekenis veranderd ("liquiditeitshandelaren" voor de noise traders van DSSW,
Feitelijke fouten 2). "Grens", "informativiteit" en "aanbodruis" houden elk één betekenis.
Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. 07_37:64-65, "Hier staat alleen de stelling van Grossman en Stiglitz vast, en zijn de
   snellere prijzen gemeten." → "Hier staat alleen de stelling van Grossman en Stiglitz vast,
   en is gemeten dat prijzen nieuws sneller verwerken."
2. 07_37:99-100, "Alle berekeningen in dit college gebruiken dezelfde pakketten en één vaste
   startwaarde voor het toeval." → "We laden eerst de pakketten en leggen het toeval vast,
   zodat elke uitvoering dezelfde getallen geeft."
3. 07_37:1061-1064, "... verliest het begrip efficiëntie, prijzen als verwachtingen onder het
   ware model, zijn houvast" → "Als beleggers ten slotte zelf uit honderden voorspellers leren
   en het ware model niet kennen, verliest het begrip efficiëntie zijn houvast, want dat begrip
   veronderstelt prijzen die verwachtingen zijn onder het ware model {cite}`MartinNagel2022`."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Woorden 5801, prose_stats PASS (geen zin > 40). Getallencontrole tegen `nb_outputs` en berekening: 50 = 8 + 8 + 20 + 14 (GROUPS en OTHER in de cel); 4,5 = (300% - 75%) x 2%, en 3 x 1,5 = 4,5 (1,5 uit de tekst); ruim 4% = 11 x 0,4% = 4,4%; 0,15% ongewijzigd uit de celuitvoer. Geen niet-herleidbaar getal, geen celuitvoer veranderd.

| punt | uitkomst |
|---|---|
| Feit 1, Samengevat $\omega$ (583-584) | opgelost: $\omega$ vergroot de fout in het niveau, relatieve prijzen middelen per aandeel weg |
| Feit 2, DSSW-liquiditeitshandelaren (332) | opgelost: "de liquiditeitshandelaren van aanname 3", verwijzing geschrapt |
| Feit 3, eenheid replicatietabel (946) | opgelost: beide kolommen cumulatief over dag 0 t/m 10 |
| Feit 4, "veertig jaar hoog" (56-58) | opgelost: geleidelijke daling, sprong met ChatGPT |
| Verbetering 2, event study hoort bij de theorie | opgelost: Overzicht en eerste alinea van de eventsectie (het ene moment waarop $c$ sprong) |
| Verbetering 2, getal voor slechtere staart | opgelost: omloop 300% kost 4,5 procentpunt extra, herleidbaar |
| "Beide mechanismen" (52, 594) | opgelost: bij naam |
| Verbetering 3 en hardop-toets 1-3 (64, 99, 1061) | opgelost volgens voorstel |
| Samengevat samengeplakt (585-587) | opgelost: twee punten |
| Formule-opening simulatie (594) | opgelost: de vraag zelf |
| Reden spreiding en handel (528-530) | opgelost: variantie tegen spread en commissie |
| $w_j$, $\bar\beta$, $g$ tegen $\omega$ (427-432) | opgelost |
| Toy, herkomst $e^{2ac}$ | opgelost: verhouding van restvarianties |
| Code, `sum`-truc en `gs_price`-commentaar | opgelost, uitvoer ongewijzigd |
| Replicatie, indeling 8+8+20+14 | opgelost in "Data hier" |

Nog open: niets wezenlijks. Verslechterd: niets. Kleinigheid (geen aftrek): "de omloop van het gemiddelde naar 300%" leest iets stug, en de 4,5 is een directe kostenterm, geen kwadratische verlies; de tekst zegt dit niet fout.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **gewogen** | | **9,0** |

Plafond: elk deelcijfer is hoogstens het vooruitzicht van de beoordelaar (9,0) en het eindcijfer hoogstens 9,0 bij volledige oplossing.
