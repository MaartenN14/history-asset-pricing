STATUS 03_13_equity_premium_puzzle F6c words=5651 prose=PASS open=1 cijfer=9,0 min=8,8

# Ronde 9+

Vorige ronde: 8,6

Eindbeoordeling (F6) van `lectures/03_13_equity_premium_puzzle.md`, gelezen na de taalredactie.
Getallen zijn nagerekend tegen `nb_outputs` (18 cellen) en met de hand. Verwijzingen naar
[](#03-12-consumptie-capm) (14,7 en "ongeveer 75") kloppen met 03_12:424 en 03_12:976.

## De drie verbeteringen met het meeste effect

1. **Hardop-zinnen en getallenalinea's herschrijven** (taal, 8,5 → 9). Het gaat om de zes
   zinnen onder criterium 3, en om alinea's met vijf of zes getallen in lopende tekst
   (03_13:127–133, 465–469, 689–699, 770–774, 907–912, 1044–1046) [onderzoek D]. Daarnaast
   moet de tweede "standaardfout van 2%" (03_13:773) een link naar `#00-01-rendementen` krijgen.
2. **Eén woord per begrip bij "grens", en de routekaart met een eenduidig verwijswoord**
   (helderheid, 8,5 → 9). "Grens" betekent nu vijf dingen: de HJ-grens, de Sharpe-grens, de
   efficiënte grens (589), de bovengrens $\gamma \le 10$ (750, 1237) en de grenzen van het
   $\gamma$-gebied (638). In de routekaart (202–204) is niet duidelijk waar "dat" naar verwijst.
3. **Het tweede replicatieoordeel laten kloppen met de cijfers, en het Engelse figuurlabel
   vertalen** (replicatie 8,5 → 9, code en figuren 8,5 → 9). De zin "Gladdere consumptie maakt de
   vereiste risicoaversie hoger dan bij Mehra en Prescott" (911) klopt voor RRA(2)
   (13,0 tegen 10,4 op de MP-momenten), maar niet voor RRA(1): 22,0 ligt onder de 27,2 van de
   simulatie op de MP-momenten. Het label "Sharpe-grens: excess marktrendement" (1011) is
   Engels.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,7** |

(0,25·8,5 + 0,2·9 + 0,2·8,5 + 0,1·9 + 0,1·8,5 + 0,1·8,5 + 0,05·9 = 8,675, afgerond 8,7.
Taal is minstens 8, dus er is geen blokkade. Het doel van 9,0 is niet gehaald.)

## 1. Helderheid van de uitleg (8,5)

*Goed.*
- Toy-voorbeeld en Theorie: elke formule krijgt een getal. De lognormale premie komt op 0,25
  tegen 0,26 in het toy-voorbeeld, het rooster op 0,362 tegen 0,35, en $\sigma(m)/\E[m]$ is
  0,07, "een vijfde van wat de grens eist".
- Hoe het getoetst wordt: $v$ krijgt een economische betekenis ("Economisch is $v$ de prijs van
  een zekere euro") en een getal (0,37/1,008). Daarmee is de kritiek van vorige ronde opgelost.
- Wat het voorspelt: de alinea over "Een echt aandeel beweegt niet perfect met consumptie mee,
  maar is wel veel volatieler" verklaart vooraf waarom de simulatie 27,2 geeft en de boom 47,6.

*Aanmerkingen.*
- Theorie, routekaart: "Ten slotte bevestigen twee toetsen dat zonder het hele model, namelijk
  de grens van Hansen en Jagannathan en de rente die de uitweg via een hoge $\gamma$ afsluit."
  (202–204). Het verwijswoord "dat" wijst terug naar een zin over de lognormale premie, en de
  rentesectie is geen toets zonder model (H8).
- Hoe het getoetst wordt: "Zit er een risicovrij activum in $\mathbf{R}$, dan moet
  $v = 1/(1 + R^f)$ zijn" (561–562). De stelling eist een niet-singuliere $\boldsymbol{\Sigma}$,
  en dat sluit een echt risicovrij activum uit. De smalle V ontstaat omdat de reële T-bill bijna
  risicovrij is. Die ene bijzin ontbreekt.
- Meerdere plekken: "grens" voor vijf begrippen (H7), bijvoorbeeld "De grenzen van dat gebied
  volgen door $\beta = 1$ in te vullen" (638) vlak na twee HJ-grenzen.
- Consumptie en de vereiste risicoaversie: "Gladdere consumptie maakt de vereiste
  risicoaversie hoger dan bij Mehra en Prescott" (911). Waarmee wordt vergeleken? De tabel
  heeft voor Mehra en Prescott geen RRA.

*Beter uitleggen.* Eén bijzin in de tweede HJ-stelling zou zeggen dat de T-bill in de
replicatie bijna, maar niet helemaal, risicovrij is. Voor de V-vorm is dat genoeg.

*Voor een 9.* 03_13:202–204 laten verwijzen naar "dat de premie klein is". Bij 03_13:561 de
bijna-risicovrije T-bill noemen. Voor de bovengrens van $\gamma$ (750, 1237) en voor de wortels
(638) een ander woord dan "grens" kiezen. Bij 03_13:911 zeggen met welk getal wordt vergeleken.

## 2. Opbouw en rode draad (9)

*Goed.*
- Overzicht: vraag en antwoord met getallen (0,35 tegen 6,18). De routekaart en "Samengevat"
  omsluiten Theorie.
- De maatstaventabel staat nu aan het eind van de replicatie (1052–1067), na de berekeningen.
  Dat was vorige ronde het grootste opbouwpunt.
- De voorspellingen uit de intuïtie komen in gewone zinnen uit: "zoals we in de intuïtie al
  verwachtten" (352), "Zoals verwacht is de premie klein" (475). De toy-getallen keren terug in
  0,9589 (529), $\delta = 0{,}036$ (692) en 0,26 (1133).

*Aanmerkingen.*
- Hoe het getoetst wordt: "Tot hier ging het om één overrendement. Met meerdere activa wordt de
  eis strenger, en daarvoor is een tweede stelling nodig." (534–535). De tweede stelling met
  bewijs is zwaar voor een resultaat dat alleen de replicatie gebruikt. Dat is acceptabel, maar
  het is het zwaarste stuk van het college.

*Beter uitleggen.* Niets essentieels. 5.526 woorden, dus binnen de grens.

## 3. Taal (8,5)

*Goed.* De telegramzinnen, regeltaal ("De lezer weet nu") en vaste wendingen zijn weg. Gemiddeld
15,9 woorden per zin, geen zin boven 40, en de motiefnamen staan elk hoogstens twee keer. De
intuïtie leest als gesproken taal ("Een slecht jaar is een jaar met iets minder groei, geen jaar
waarin het eten op is"). De redactie heeft geen vakterm van betekenis veranderd. "Overrendement"
voor *excess return* en "grens" voor *bound* zijn juist. "Aan de rand" (382) betekent de rand
van het rooster en is geen alias.

*Aanmerkingen.*
- Overzicht: "Het schat niets. Het kalibreert een Lucas-economie op de Amerikaanse consumptie"
  (59). Geknipt, en dit punt stond al open [onderzoek D, E:58].
- Het kernresultaat: "De oplossing is gesloten omdat CRRA-nut alleen naar verhoudingen kijkt,
  zodat een belegger die twee keer zo rijk is, een procentuele schommeling hetzelfde
  beoordeelt." (248–249)
- Wat het voorspelt: "Zoals verwacht is de premie klein omdat consumptie glad is, met een
  factor $\gamma$ ervoor." (475–476)
- Waarom de rente de uitweg afsluit: "als beleggers zo ongaarne consumptie over de tijd
  verschuiven" (655–656). Het woord is ouderwets.
- Wat er brak: "Mehra merkte op dat de rente dan tegen die kans in zou moeten bewegen" (1091).
- Simulatie: "In dat verschil zit de standaardfout van 2%" (773) staat zonder link naar
  `#00-01-rendementen` (rolkaart §3).
- Veel alinea's met meer dan drie getallen in lopende tekst: 127–133, 465–469, 689–699,
  770–774, 907–912 en 1044–1046 [onderzoek D]. `prose_stats` telt 11 alinea's van één zin.

*Beter uitleggen.* Niet van toepassing.

*Voor een 9.* De vijf geciteerde zinnen herschrijven (zie de hardop-toets). Getallen uit
03_13:689–699 en 907–912 naar de tabel verplaatsen of verdelen over zinnen. Bij 03_13:773 de
link toevoegen. Eenzinsalinea's die geen overgang zijn, bij de buuralinea voegen [onderzoek D].

## 4. Toy-voorbeeld (9)

*Goed.* Vijf stappen die met de hand na te rekenen zijn, en een tabel die hand en code gelijk
laat zien. Er is één nog niet afgeleide formule, en die is als controle aangekondigd. De
slotzin (192–194) zegt waar de kleine premie vandaan komt: 0,14 maal 7,4 gedeeld door vier.

*Aanmerkingen.*
- Opzet: de tabelrij "| voorkeuren | $\beta = 0{,}99$ | $\gamma = 2$ | | |" (139) staat in
  kolommen die kans en groei heten.

*Beter uitleggen.* Niets.

## 5. Code en figuren (8,5)

*Goed.* Elke cel heeft een zin ervoor en erna. `iid_economy` en `mp_economy` volgen de
stapnummers en de propositie, met een zichtbare lus voor $R_{ij}$. Vóór elke figuur staat
waarop te letten ("Let in de figuur hieronder op de schaal", "op de gestreepte lijn bij
$\gamma = 10$").

*Aanmerkingen.*
- HJ-figuur: `label="Sharpe-grens: excess marktrendement"` (1011). Figuurteksten horen in het
  Nederlands, en de proza zegt "overrendement".
- Regiofiguur: `upper = np.array([prem_grid[admissible][bins == k].max() if np.any(bins == k)
  else np.nan for k in range(80)])` (394). Een compacte truc, al staat hij in een verborgen cel.
- De HJ-tabel (cel 14) heeft acht kolommen en elf rijen. Voor de tekst zijn drie kolommen nodig.

*Beter uitleggen.* Niets.

*Voor een 9.* In 03_13:1011 "overrendement van de markt" schrijven. Regel 394–395 als lus of
`groupby` schrijven. In 03_13:968–972 de tabel beperken tot de kolommen die de tekst gebruikt.

## 6. Replicatie en empirie (8,5)

*Goed.* Het blok telt ongeveer 205 woorden en twee zinnen per onderdeel. Er is een tabel
origineel/hier voor tabel 1 en voor de drempels. Elk oordeel begint met **Geslaagd** en verwijst
naar de verwachte afwijking. De omslag bij $\gamma = 40$–50 wordt uitgelegd als een eigenschap
van de steekproef, met een verwijzing naar Hansen en Jagannathan (p. 250) en Rietz.

*Aanmerkingen.*
- Consumptie en de vereiste risicoaversie: "Gladdere consumptie maakt de vereiste
  risicoaversie hoger dan bij Mehra en Prescott, en tot 2024 wordt ze nog gladder." (911–912)
  Zie feitelijke fout 1.
- Hetzelfde oordeel: "door de Depressie en de oorlog is onze standaarddeviatie 2,58 tegen 3,57
  en de autocorrelatie $+0{,}49$ tegen $-0{,}14$" (908–909). Dat zijn zes getallen in lopende
  tekst die ook in de tabel erboven staan.

*Voor een 9.* In 03_13:907–912 alleen de richting noemen en naar de tabel verwijzen. De
vergelijking met Mehra en Prescott expliciet maken (RRA(2): 13,0 tegen 10,4 op hun momenten).

## 7. Oefeningen (9)

*Goed.* De drie soorten zijn er: een instap op het toy, een afleiding (op het scherp van de
snede) en een uitbreiding van de replicatie (deelperioden en bootstrap). Elke uitwerking eindigt
met een les, bijvoorbeeld "dat hij bestaat, hangt er niet van af". Alle getallen kloppen met
de celuitvoer.

*Aanmerkingen.*
- Oefening 3: "Het interval van de vereiste $\gamma$ is even breed" (1236–1237). "Even breed"
  als wat? Relatief (10–26 tegen 0,25–0,64) klopt het, maar dat staat er niet.

## Feitelijke fouten

Nagerekend: alle getallen in toy, theorie (0,00125; 0,0172; 47,6; 0,47 en 27,1; 13,8; 0,546;
±4,2 pp), simulatie (27,2; 13,6; 2,6–9,5; 10–71; 0,34; 0,29 en 0,58), replicatie (6,22; 0,75;
1,77; 6,92; 1,34; 22,0; 13,0; 0,43; 15, 42 en 43; 35% en ±15%) en oefeningen. Ze kloppen met de
celuitvoer. Ook 14,7 en "ongeveer 75" uit 03_12 kloppen.

1. **Onzeker** (03_13:911): "Gladdere consumptie maakt de vereiste risicoaversie hoger dan bij
   Mehra en Prescott". Op de MP-momenten (simulatie, correlatie 0,37) is RRA(1) 27,2 en RRA(2)
   $0{,}0618/(0{,}0357 \cdot 0{,}1667) = 10{,}4$. Hier is RRA(1) 22,0, lager, en RRA(2) 13,0,
   hoger. De bewering geldt dus alleen voor RRA(2), omdat de hogere correlatie (0,59) het effect
   van gladdere consumptie op RRA(1) meer dan compenseert. Correctie: "RRA(2) ligt hoger dan op
   de momenten van Mehra en Prescott (13,0 tegen 10,4), RRA(1) niet, omdat de correlatie hier
   0,59 is".
2. Kleine onnauwkeurigheid, geen fout (03_13:561–562): een echt risicovrij activum maakt
   $\boldsymbol{\Sigma}$ singulier, tegen de aanname van de stelling in. Zie criterium 1.

## Navertelling in vijf zinnen

Een Lucas-economie met CRRA-nut en de Amerikaanse consumptie van 1889–1978 levert bij
$\gamma \le 10$ en een rente tussen nul en vier procent hoogstens 0,35 procentpunt premie, tegen
6,18 gemeten. De reden is dat de premie ongeveer $\gamma$ maal de variantie van consumptiegroei
is, en die variantie is klein. Hansen en Jagannathan zeggen hetzelfde zonder voorkeuren: de
stochastische discontofactor moet minstens de Sharpe-ratio van 0,37 schommelen, en consumptie
haalt dat pas bij $\gamma$ boven tien, tegen een absurd hoge rente (Weils rentepuzzel). De
premie zelf is slecht gemeten (standaardfout 1,76), maar ook bij een ware premie van 3% blijft
de vereiste $\gamma$ in twee derde van de steekproeven boven tien. De replicatie op Shiller-,
FRED- en French-data tot 2025 bevestigt dit met drempels van 15 tot 43. Dat komt overeen met
het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk natuurlijker gemaakt en geen betekenis verschoven.
Wat overblijft, zijn losse zinnen en getallenrijen. Hardop-toets, drie zinnen:

1. "De oplossing is gesloten omdat CRRA-nut alleen naar verhoudingen kijkt, zodat een belegger
   die twee keer zo rijk is, een procentuele schommeling hetzelfde beoordeelt." (248–249)
   → "Er is een gesloten oplossing, omdat een belegger met CRRA-nut een schommeling van een
   procent even erg vindt, hoe rijk hij ook is."
2. "Ten slotte bevestigen twee toetsen dat zonder het hele model, namelijk de grens van Hansen
   en Jagannathan en de rente die de uitweg via een hoge $\gamma$ afsluit." (202–204)
   → "Ten slotte laten de grens van Hansen en Jagannathan en de rente zien dat een hoge
   $\gamma$ de puzzel niet oplost, ook zonder het hele model."
3. "Zoals verwacht is de premie klein omdat consumptie glad is, met een factor $\gamma$
   ervoor." (475–476) → "De premie is dus klein, zoals verwacht, omdat ze de variantie van een
   gladde consumptiereeks maal $\gamma$ is."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Controle van R9-1 (F6b), na de taalredactie. Getallen nagerekend tegen
`nb_outputs` (cel 12, consumptietabel; cel 9, simulatietabel).

**Feitelijke fouten.**
1. **Opgelost.** 911: RRA(2) 13,0 tegen 10,4 (hoger, gladdere consumptie),
   RRA(1) 22,0 tegen 27,2 (lager, correlatie 0,59). Nagerekend: `nb_outputs`
   geeft RRA(1) 21,97 en RRA(2) 12,96 over 1929–1978 (afgerond 22,0 en 13,0),
   correlatie groei/premie 0,590 (afgerond 0,59), en 27,249 als "ware gamma"
   bij 6% in de simulatietabel (afgerond 27,2). De 10,4 komt uit geen cel:
   $0{,}0618/(0{,}0357 \cdot 0{,}1667) = 10{,}38$ (afgerond 10,4) is een
   handberekening op tabel 1 van Mehra en Prescott, expliciet als zodanig
   ingeleid met "Op de momenten van Mehra en Prescott" en met de =-teken in de
   tekst zelf, niet in een cel. De vergelijking klopt nu voor beide RRA's en
   zegt waarom ze tegengesteld bewegen.
2. **Opgelost.** 561–562: de bijzin over het singuliere $\boldsymbol{\Sigma}$
   bij een echt risicovrij activum staat er, met de bijna-risicovrije T-bill
   als reden voor de smalle V.

**Drie verbeteringen.**
1. **Deels.** Hardop-zinnen: 248–249, 202–204 en 475–476 herschreven (248 en
   475 vrijwel woordelijk de voorgestelde tekst, 202 anders geformuleerd maar
   lost dezelfde verwijzing op); 655–656 "ongaarne" vervangen. 1091 niet
   herschreven; de schrijver verantwoordt dit omdat de hardop-toets zelf geen
   herschrijving voor deze zin gaf, terwijl "Voor een 9" vijf zinnen noemde.
   De zin ("Mehra merkte op dat de rente dan tegen die kans in zou moeten
   bewegen") is op zichzelf gewoon Nederlands, dus dit is een klein open punt,
   geen fout. Getallenalinea's 127, 465, 689, 770, 907 en 1044 zijn wel alle
   herschreven (voorkeuren apart, tussenrekening eruit, Kocherlakota als
   display, "hoge/lage premie" in plaats van herhaalde percentages, sd en
   autocorrelatie alleen als richting).
2. **Opgelost.** "Grens" wordt nu voor vijf begrippen vermeden: 589 "efficiënte
   portefeuilles"/minimum-variantieportefeuille, 638 "de twee waarden van
   gamma waarbij beta precies één is", 750/1237 "het maximum van Mehra en
   Prescott". De routekaart (202–204) verwijst nu ondubbelzinnig naar wat HJ en
   de rente laten zien, zonder het probleemgevoelige "dat".
3. **Opgelost.** Het replicatieoordeel bij 911 klopt nu met de cijfers (zie
   feitelijke fout 1). Het label is vertaald naar "Sharpe-grens: overrendement
   van de markt" (bevestigd in de tekst, cel voor de HJ-figuur).

**Overige "Voor een 9"-punten.** Link bij 773 toegevoegd
(`[de standaardfout van 2%](#00-01-rendementen)`). Toy-tabel: rij "voorkeuren"
verwijderd, $\beta$ en $\gamma$ staan in de tekst. Regiocel (394) nu een lus.
HJ-tabel toont drie kolommen, de drempels 15/42/43 staan in de print.
Oefening 3 (1237): "naar verhouding even breed, want ook daar is de bovenkant
ruim twee keer de onderkant" lost de eerdere ambiguïteit op. Opbouw (534) bleef
ongewijzigd, zoals de vorige beoordeling toestond.

**Nieuwe punten.** Geen; geen verslechtering of nieuwe feitelijke fout
gevonden.

## Cijfers (Controle 1)

| nr | criterium | gewicht | vorig | nieuw |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 | 9 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 |
| 3 | Taal | 20% | 8,5 | 8,8 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8,5 | 9 |
| 6 | Replicatie en empirie | 10% | 8,5 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 |
| | **Eindcijfer** | | 8,7 | **9,0** |

(0,25·9 + 0,2·9 + 0,2·8,8 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 8,96, afgerond
9,0. Taal blijft op 8,8 door het ene niet-herschreven punt (1091); alle andere
deelcijfers bereikten het in het vorige rapport genoemde plafond. Geen
deelcijfer onder 8,5. Doel gehaald.)
