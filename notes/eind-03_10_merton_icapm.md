STATUS 03_10_merton_icapm F6c words=5899 prose=PASS open=0 cijfer=9,0 min=9

**Eindcijfer van record: 9,0** (F6c). Verloop: Vorig: 8,9. Ronde 9+: T, F6 8,8 (code 8, 1 feitfout) -> F6c 9,0 (gewogen 9,1, plafond §11.3). Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Eindbeoordeling: Merton, continue tijd en het ICAPM (F6)

## Ronde 9+

Vorige ronde: 8,9

Gelezen na de taalredactie (`notes/taal-03_10_merton_icapm.md`). Normen: eindcijfer ≥ 9,0,
geen deelcijfer onder 8,5, taal onder 8 blokkeert. Gewichten van ronde 9+ (helderheid 25,
opbouw 20, taal 20). `prose_stats`: 5.822 woorden, PASS; gemiddelde zinslengte 15,7, één
zin boven 40 woorden. Celuitvoer: `$TEMP/F6-03_10_merton_icapm-out.txt`.

Vaktermen na de redactie: geen betekenisverschuiving gevonden. "Marktruiming" werd
"vraag en aanbod gelijk" (r. 512, 534) en "in evenwicht" (r. 485, 525), wat hetzelfde
zegt. "Beprijsde factoren" werd "factoren met een risicopremie" (r. 574, 1298), wat
klopt. Met "overrendement" (r. 126, 659) is *excess return* goed vertaald, maar de
vervanging is niet overal doorgevoerd (zie taal). "Het lemma van Itô" (r. 326) is
hetzelfde resultaat als in 02_09.

Oordeel over wat de redacteur bewust liet staan:
- **"asset pricing" (r. 58, 1294).** Mag blijven. Het is de gangbare naam van het
  vakgebied in Nederlands academisch spraakgebruik, net als *payoff* of *posterior*, en
  STYLE §3 geeft er geen Nederlandse vaste term voor. Alleen het lidwoord in r. 58 ("omdat
  het de asset pricing dynamisch maakte") klinkt stroef. "omdat het asset pricing
  dynamisch maakte" is natuurlijker. Dat is geen voorwaarde voor een 9.
- **"In dit college:" vóór de lijst (r. 38).** Mag blijven. De dubbele punt staat vóór
  een opsomming, zoals STYLE toestaat. De lijstitems lopen grammaticaal door ("In dit
  college rekenen we ..."), en hardop klinkt dat gewoon.

## De drie verbeteringen met het meeste effect

1. **De roostercel splitsen en de leeswijzer bij de steekproeffiguur herschrijven**
   (criterium 5, 8 → 9). De cel r. 805–854 bevat `solve_rebalancing`, `normal_shocks`,
   `known`, de controlelus en de tabel in circa 48 regels. Splits haar in de functies en een
   controlecel met een zin ertussen. De leeswijzer op r. 969–971 zegt niet wat de lezer moet
   zien (zie hardop-toets).
2. **De taal op zes plekken afmaken** (criterium 3, 8,5 → 9). Gebruik één naam voor het
   overrendement: r. 1021 heeft nog "log excess rendement" en de tabelindex op r. 1095 "gem.
   log excess rendement". Maak van "die gok" (r. 376) een proefoplossing. Herschrijf ook r.
   62, 565, 971 en 1281, "Horizon-irrelevantie" (r. 278), "koop-en-houdbelegger" (r. 1277),
   de figuurtitel "moet indekken" (r. 990) en "standaardafwijkingen" in de tabel (r. 1258).
3. **Drie kleine gaten in de uitleg dichten** (criterium 1, 9 → 9,5). Beperk de bewering
   over consumptie (r. 234–235) tot constante kansen. Zeg in r. 857 dat $\gamma = 2$
   daarom niet in de tabel staat. Schrijf in r. 679 "het verwachte log-rendement" in plaats
   van "het log-rendement".

## Cijfers F6, vóór herstel (niet het eindcijfer)

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,8** |

(0,25·9 + 0,2·9 + 0,2·8,5 + 0,1·9 + 0,1·8 + 0,1·9 + 0,05·9 = 8,80.) Het eindcijfer haalt
9,0 niet, en code (8) ligt onder de ondergrens van 8,5.

## 1. Helderheid van de uitleg (9)

*Goed.*
- Toy-voorbeeld en Theorie: de getallen keren terug. $w^\ast = 0{,}7396$ tegen 0,8333 (De
  Merton-portefeuille), $q = 25/26$ in geval A (Samuelson) en geval B en B' bij het teken
  van de hedgevraag (r. 476–477).
- Numerieke oplossing: $\theta = 0{,}34$ en $\sigma_\eta = 0{,}069$ zijn met de hand
  uitgerekend (r. 685–686, nagerekend). De som $B + C\eta$ krijgt in de hoofdtekst een
  betekenis (r. 628–629).
- Het ICAPM-effect in getallen: 10,7% in plaats van 16,2%, "met een derde" (r. 756–758).

*Aanmerkingen.*
- Opzet en aannames: "Consumptie laten we weg, omdat Merton liet zien dat ze de
  portefeuilleregels hieronder niet verandert". Voor de Merton-portefeuille klopt dat.
  Voor de hedgevraag van Kim-Omberg niet: met tussentijdse consumptie wordt die een gewogen
  gemiddelde over horizonnen.
- De Merton-portefeuille: "Daarna gaan we na dat die gok de HJB-vergelijking oplost." Drie
  alinea's eerder (r. 273) en in de Intuïtie (r. 80) betekent "gok" weddenschap. Hier
  betekent het proefoplossing (H7).
- Numerieke oplossing: "Bij $\gamma = 2$ loopt de allocatie tegen de grens van 0,99 aan."
  De tabel erboven toont alleen $\gamma = 5$ en $10$. Dat dit de reden is dat
  $\gamma = 2$ ontbreekt, moet de lezer zelf bedenken.
- Numerieke oplossing: "Het verwachte simpele overrendement is het log-rendement plus
  $\tfrac12\sigma^2$". Bedoeld is het verwachte log-rendement. De formule tussen haakjes
  herstelt dat.

*Beter uitleggen.* Waarom de lezer de roostercontrole nodig heeft: één bijzin dat de
vertaling naar continue tijd een benadering is, en dat het rooster later de
replicatie draagt.

## 2. Opbouw en rode draad (9)

*Goed.*
- Het Overzicht geeft vraag en antwoord in drie zinnen. De drie verwachtingen uit de
  Intuïtie worden alle drie ingelost, telkens in een gewone zin: bij Samuelson (r.
  290–291), bij de horizonfiguur (r. 761–762) en na het ICAPM (r. 567–568).
- Eén grootheid loopt door Numerieke oplossing, Simulatie, Replicatie en Wat er brak: de
  hedgevraag bij $\gamma = 5$ op twintig jaar (0,339 in het model, 0,450 gemiddeld
  geschat, 0,223 op de data).
- 5.822 woorden, onder de grens. Routekaart (r. 223–227) en Samengevat zijn op hun plaats.

*Aanmerkingen.*
- Replicatie: het derde deel (parameteronzekerheid) is een tweede verhaal naast de
  hedgevraag. De slotalinea's (r. 1281–1289) sluiten wel aan op de simulatie. Geen
  aftrek.

## 3. Taal (8,5)

*Goed.* De redactie heeft het staccato verbonden ("daarom", "terwijl", "want", "zodat").
Stap 1 tot 5 van het toy-voorbeeld lezen als zinnen. "Zij" en "haar" voor zaken zijn weg.
Motiefnamen: "de standaardfout van 2%" staat twee keer, "theorie of feit" en "risico of
vergissing" elk één keer. "Wie …" staat twee keer. De vaste wending "Waarom zou dit waar
zijn?" staat één keer in de tekst, en de tweede keer anders geformuleerd.

*Aanmerkingen.*
- Replicatie-admonition, Wat: "het maandelijkse VAR van het log excess rendement op de
  dividendopbrengst". De tabelindex op r. 1095 zegt "a (gem. log excess rendement)", terwijl
  r. 126 en 659 "overrendement" gebruiken. Dat zijn twee namen voor één begrip (H7) [onderzoek E].
- De Merton-portefeuille: "Daarna gaan we na dat die gok de HJB-vergelijking oplost."
  [onderzoek E]
- Het kernresultaat: "levert vermogen wanneer het het minst nodig is". Het dubbele "het"
  struikelt [onderzoek E].
- Overzicht: "Op de vraag theorie of feit is het ICAPM een theorie met een open plek." De
  motiefnaam klinkt aangeplakt [onderzoek E].
- Parameteronzekerheid volgens Barberis: "Het verschil komt zelf van [de standaardfout
  van 2%]". "Komt zelf van" is geen gesproken Nederlands [onderzoek E].
- Samuelson: de stellingkop "Horizon-irrelevantie" is een gekunstelde samenstelling
  [onderzoek E].
- Parameteronzekerheid volgens Barberis: "koop-en-houdbelegger" [onderzoek E]. In de figuurtitel
  "Wat de belegger denkt dat hij moet indekken" staat "indekken" niet-wederkerend
  [onderzoek E]. In de tabel staat "D/P in standaardafwijkingen", terwijl de tekst
  "standaarddeviaties" zegt [onderzoek E].

*Voor een 9.* Vervang "excess rendement" door "overrendement" in
`lectures/03_10_merton_icapm.md:1021` en in de tabelindex op :1095. "gok" wordt
"proefoplossing" op :376. Herschrijf :62, :565, :971 en :1281 (zie hardop-toets). Maak van
:278 "Irrelevantie van de horizon", van :1277 "buy-and-hold-belegger", van de titel op :990
"waartegen de belegger denkt zich te moeten indekken" en van de tabelkolom op :1258 "D/P in
standaarddeviaties".

## 4. Toy-voorbeeld (9)

*Goed.* Een opzettabel, vijf stappen met getallen en één codecel met een tabel hand/code
die tot vier decimalen overeenkomt (nagerekend: 0,8333, 25/26, 1,5297, 0,8759, 0,7909,
1,7361). De slotzin zegt wat het getal betekent: 0,0426, ruim vijf procent, en waarom.

*Aanmerkingen.*
- Het recept: "met $q = \E[(1 + wR^{e})^{-1}]$ bij de optimale $w$ (Theorie leidt die
  vorm af)". De vorm van de waardefunctie en de gewogen eerste-ordevoorwaarde komen vóór
  hun afleiding [onderzoek A]. Dat is één geleende formule, wat de rubriek toestaat.
  Omdat stap 4 de voorwaarde uitschrijft, is de lezer niet verloren.

## 5. Code en figuren (8)

*Goed.* Vóór elke tabel staat een zin en erna een lezing. `kim_omberg` heeft een
zichtbare Runge-Kutta-lus zonder broadcast-trucs. De simulatie staat in drie cellen:
functie, simulatie, tabel. Figuren hebben een bijschrift dat zegt wat te zien is.

*Aanmerkingen.*
- Numerieke oplossing: de cel met `solve_rebalancing`, `normal_shocks`, `known`, de lus
  over $\gamma$ en de controletabel beslaat circa 48 regels. Rekenwerk en presentatie
  staan daar in één cel.
- Simulatie: "Let in de figuur op waar de gestreepte lijn links ligt ten opzichte van de
  zwarte." De zin zegt niet waarop de lezer moet letten (de afstand, en welke kant op) en
  noemt het rechterpaneel niet.
- Oefening 1: "(w0 in geval B min de myopische fractie)". Een codenaam in de proza
  [onderzoek A].

*Voor een 9.* Splits `lectures/03_10_merton_icapm.md:805–854` in een cel met de functies
en een controlecel, met één zin ertussen. Laat de leeswijzer op :969–971 zeggen waar de
gestreepte lijn links ligt en wat rechts te zien is. Maak op :1339 van "w0" "de fractie in
geval B".

## 6. Replicatie en empirie (9)

*Goed.* De admonition heeft alle vijf onderdelen en een toetsbare verwachting ("Een
negatieve helling of een positieve correlatie is een fout in de code"). Er zijn drie
tabellen origineel/hier met alleen rijen die een origineel hebben. Elk oordeel begint met
Geslaagd of Gedeeltelijk geslaagd en verwijst naar de verwachting. De afwijking van
Barberis wordt in standaardfouten uitgedrukt (0,5).

*Aanmerkingen.*
- Parameteronzekerheid volgens Barberis: "Die 4,5% geldt wel voor $\gamma = 5$ met
  jaarlijkse herbalancering, zodat de vergelijking alleen een orde van grootte geeft." De
  tabel zet ongelijke gevallen naast elkaar [onderzoek A]. De tekst zegt dat eerlijk, dus
  er gaat hier niets af voor een 9. Voor een 10 zou $\gamma = 10$ uitgerekend worden.

## 7. Oefeningen (9)

*Goed.* De instap varieert op het toy-voorbeeld, de afleiding van $C_\infty$ en
$B_\infty$ heeft een numerieke controle (0,6088 tegen 0,6087), en de uitbreiding past de
replicatie toe op 1996–2025. Elke uitwerking eindigt met een gewone zin over wat ze
leert.

*Aanmerkingen.* Oefening 1: "(w0 in geval B min de myopische fractie)", zie code.

## Feitelijke fouten

1. **Onnauwkeurig (open).** `lectures/03_10_merton_icapm.md:234–235`: "Consumptie laten we
   weg, omdat Merton liet zien dat ze de portefeuilleregels hieronder niet verandert
   {cite}`Merton1969`." Dat geldt bij constante beleggingskansen, dus voor
   [](#eq-merton-icapm-merton). De Kim-Omberg-hedgevraag hieronder verandert wel met
   tussentijdse consumptie: die wordt een gemiddelde over horizonnen. Voorstel: "... dat ze
   de Merton-portefeuille niet verandert, en de hedgevraag alleen in grootte." Of beperk
   de zin tot constante kansen.

Nagerekend tegen de celuitvoer en correct: het toy-voorbeeld (0,8333; 25/26 = 0,9615;
1,5297; 0,8759; 0,7909; 0,0426; 1,7361; $q = 1{,}0833$ bij $\gamma = 0{,}5$; de
hedgeverhouding groeit met $\gamma$: 0,051, 0,078, 0,086), $w^\ast = 0{,}7396$, 8%
marktpremie, $\kappa = 0{,}083$ en 8 jaar, $\delta = -0{,}8$, $\theta = 0{,}34$,
$\sigma_z = 0{,}156$, $\sigma_\eta = 0{,}069$, 0,378 en 0,339 ("bijna verdubbelt"),
$\gamma = 10$ op vijftig jaar (0,372 > 0,189), 10,7% tegen 16,2% en "met een derde", het
grootste roosterverschil van 1,6 pp ($\gamma = 10$, $H = 20$), $\gamma = 2$ boven 0,99
(0,944 plus de hedgevraag), de simulatie (0,143–0,850; 0,450; 55,5%; 0,1% negatief; $\hat b$
0,124 > 0,08; $\hat\phi$ 0,880 < 0,92; "minder dan de helft tot tweeënhalf keer"),
Barberis 0,4058, 0,5 en 2,4, $t = 1{,}07$, 0,924, −0,856, 8,8 jaar, 1,943 bij $\gamma = 10$
en $H = 50$, de posterior (0,042 tegen 0,040; 14,1%; 4,2%), de verschillen 0,019–0,032 en
0,012–0,019, 4,5%, −1,86 sd, "half zo groot" (0,222 tegen 0,459), 0,223, $C_\infty$ en de
oneindige hedgevraag 0,609 boven de myopische 0,378 en boven 0,546 op vijftig jaar, en
oefening 3 (0,358; 2,60; 0,647; 0,990; 0,649 tegen 0,817, "zeventien procentpunt"; op de
eeuw 0,261 tegen 0,250, "ruim één procentpunt"). De tekens van de hedgevraag
($g_x < 0$, $\rho < 0$) en van $b_x = -\bar H/\bar T$ zijn opnieuw afgeleid en kloppen.

## Navertelling in vijf zinnen

Samuelson en Merton lieten in 1969 zien dat de horizon niet uitmaakt voor een
CRRA-belegger zolang rendementen onafhankelijk zijn. Hij kiest dan elk jaar hetzelfde
percentage, in continue tijd $(\mu - r)/(\gamma\sigma^2)$. Zijn rendementen voorspelbaar,
dan houdt een belegger die risicomijdender is dan iemand met log-nut er een hedgevraag bij
in activa die stijgen als de beleggingskansen verslechteren. Bij aandelen en de
dividendopbrengst is die hedgevraag positief, en ze groeit met de horizon tot een grens.
Tel die vraag op over alle beleggers, en het verwachte rendement beloont naast de
marktbèta de bèta op elke toestandsvariabele. Dat is het ICAPM, dat niet zegt welke
variabelen het zijn. In het model kan de hedgevraag de vraag naar aandelen bijna
verdubbelen, maar een eeuw data meet haar slecht, en op de Goyal-Welch-data is ze positief
en kleiner dan een verdubbeling, terwijl parameteronzekerheid de allocatie maar een paar
procentpunt drukt.

De navertelling komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft gewerkt. De gemiddelde zinslengte ging van 14,4 naar 15,7 woorden, het
aandeel eenzinsalinea's van 19% naar 12% en het aandeel zinnen met een verbindingswoord
van 16% naar 29%. Calques en sjabloonzinnen zijn vrijwel verdwenen. Wat overblijft zijn
losse plekken, geen patroon. Eén ervan heeft de redactie zelf veroorzaakt:
"overrendement" is niet overal doorgevoerd.

Hardop-toets (drie zinnen die nog niet natuurlijk klinken):
1. r. 62: "Op de vraag theorie of feit is het ICAPM een theorie met een open plek." →
   "Is het ICAPM theorie of feit? Het is een theorie met een open plek: het zegt welke
   vorm een prijsvergelijking heeft, maar niet welke variabelen erin horen."
2. r. 969–971: "Let in de figuur op waar de gestreepte lijn links ligt ten opzichte van de
   zwarte." → "Let in het linkerpaneel op de gestreepte lijn, die rechts van de zwarte
   ligt, en rechts op de breedte van de verdeling."
3. r. 1281: "Het verschil komt zelf van de standaardfout van 2%, want hoe korter de
   steekproef, hoe breder de posterior." → "Ook dit verschil is een gevolg van de
   standaardfout van 2%: hoe korter de steekproef, hoe breder de posterior."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Gelezen: R9-1 in `notes/rapport-03_10_merton_icapm.md`, het hele college opnieuw, en
`nb_outputs.py` opnieuw gedraaid (offline) tegen `$TEMP/F6c-03_10_merton_icapm-out.txt`.

**Feitelijke fout**
1. r. 234–237 (consumptie): **opgelost.** Beperkt tot constante kansen voor de
   Merton-portefeuille, met een aparte zin dat tussentijdse consumptie de hedgevraag tot
   een gewogen gemiddelde over horizonnen maakt (teken blijft, grootte verandert).

**De drie verbeteringen**
1. Roostercel splitsen (criterium 5): **opgelost.** Functiecel met `solve_rebalancing` en
   `normal_shocks` (r. 811–840), dan een zin (r. 842–843), dan de controlecel met `known`,
   de lus en de tabel (r. 846–865). Celuitvoer ongewijzigd: de tabel rooster/Kim-Omberg
   voor $\gamma = 5$ en $10$ geeft nog altijd het grootste verschil van 1,6 pp bij
   $\gamma = 10$, $H = 20$ (0,401 tegen 0,385 in `nb_outputs`); de RNG-volgorde is niet
   geraakt.
2. Taal op zes plekken (criterium 3): **opgelost.** "Overrendement" nu overal (admonition
   en tabelindex r. 1107 "a (gem. log overrendement)"), "proefoplossing" i.p.v. "gok"
   (r. 378), r. 62, 567–568, 981–983 en 1293 herschreven zoals voorgesteld,
   "Irrelevantie van de horizon" (r. 280), "buy-and-hold-belegger"/"buy-and-hold-getal"
   (r. 1289, 1295), figuurtitel r. 1002, "D/P in standaarddeviaties" (r. 1270). Geen
   restanten van de oude vormen gevonden (gecontroleerd met grep).
3. Drie kleine gaten in de uitleg (criterium 1): **opgelost.** Consumptie beperkt (zie
   feitelijke fout), de reden voor het ontbreken van $\gamma = 2$ staat er nu (r. 868–869),
   "het verwachte log-rendement" (r. 682).

**Overige aanmerkingen**
- Leeswijzer bij de steekproeffiguur (r. 981–983): **opgelost**, noemt nu linker- en
  rechterpaneel met wat erin te zien is.
- Oefening 1, "w0" (r. 1351): **opgelost**, "de fractie in geval B".

Geen nieuwe punten: geen verslechtering en geen nieuwe feitelijke fout gevonden.

**Getallencontrole.** Alle in de tekst aangehaalde en gewijzigde getallen zijn nagerekend
tegen `nb_outputs.py` (opnieuw gedraaid, offline) of tegen een berekening uit de tekst; ze
kloppen. De celsplitsing bij de roostercontrole verandert alleen de indeling: de
uitkomsten (rooster vs. Kim-Omberg voor $\gamma = 5$ en $10$, grootste verschil 1,6 pp)
zijn identiek aan F6.

**Cijfers**

| nr | criterium | gewicht | F6 | Controle 1 |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 | 9,5 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 |
| 3 | Taal | 20% | 8,5 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8 | 9 |
| 6 | Replicatie en empirie | 10% | 9 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |
| | **Eindcijfer** | | 8,8 | **9,0** |

(0,25·9,5 + 0,2·9 + 0,2·9 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 9,125. De F6-plafondregel zegt
dat het eindcijfer hoogstens het cijfer is dat "bij volledige oplossing van alle punten"
werd genoemd, hier 9,0; het gewogen gemiddelde van 9,125 wordt daarop afgetopt.) Geen
deelcijfer onder 8,5, taal (9) ruim boven de ondergrens van 8. Norm gehaald.
