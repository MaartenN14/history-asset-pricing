STATUS 05_28_termijnstructuur_premies F6c words=5735 prose=PASS open=1 cijfer=9,0 min=8,5

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

# Eindbeoordeling 05_28_termijnstructuur_premies

## Eerste herziening (workflow §12)

Eerste herziening; er is geen vorig cijfer. `prose_stats --check`: PASS (5.552 woorden,
zinnen gemiddeld 17,7, geen zin > 40, alinea gemiddeld 45, 2 "Wie"-zinnen, 1 sjabloon).
`open=4`: drie nieuwe feitelijke onnauwkeurigheden (hieronder) plus het uit F4 overgebleven
onzekere punt over `SantaClara2026` (feiten, rij 12).

## De drie verbeteringen met het meeste effect

1. **De drie feitelijke onnauwkeurigheden en de termverschuiving herstellen** (helderheid
   8,5 → 9,0). (a) lectures/05_28_termijnstructuur_premies.md:551–552 "De volatiliteit van
   de rentes is identiek": alleen de schokken in de toestand zijn gelijk, de ladingen $B_n$
   hangen van $\boldsymbol\Phi^{\mathbb Q}$ af, zodat de volatiliteit van de yields
   verschilt. (b) :793 "liggen binnen één standaardfout van één": over 1964–2026 is de
   helling bij $n=2$ 0,721 met SE 0,274, dus net erbuiten. (c) :1087 "als de tent hoog
   staat": de tent is de vorm van de gewichten $\boldsymbol\gamma$, niet de waarde van de
   factor $\hat x_t = \hat{\boldsymbol\gamma}'\mathbf f_t$; bedoeld is "als de factor hoog
   staat". Daarnaast :1019 "de 0,08 uit de theorie": 0,08 was in de Theorie een gekozen
   illustratie (:461), geen voorspelling, dus de vergelijking met de gefitte 0,075 wekt een
   verkeerde indruk.
2. **Vier stroeve zinnen herschrijven** (taal 8,5 → 9,0): :136, :650–653, :434–435 en
   :708 (zie Taal en de hardop-toets). Tegelijk de bronregels die na de taalredactie
   halverwege afbreken opnieuw laten wrappen met `tools/rewrap.py` (:42, :63, :177, :312,
   :352, :701, :758, :851, :918, :1057); dat verandert het gerenderde college niet, maar
   houdt de bron leesbaar.
3. **Code en figuren opschonen** (code en figuren 8,5 → 9,0): de `describe`-tabel
   vermenigvuldigt ook `count` met 100 (cel bij :754 toont 78.300 waarnemingen in plaats
   van 783); `lags=max(steps, 1) - 1 + 1` (:953) is een omweg voor `steps`; de
   correlatiefiguur (:1021) heeft vooraf geen zin die zegt waarop te letten, want de alinea
   ervoor (:1016–1019) beoordeelt de tabel.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Eindcijfer** (gewogen) | | **8,7** (8,725) |

### 1. Helderheid van de uitleg: 8,5

*Goed.*
- "Het kernresultaat: de spread is premie plus renteverandering": de identiteit staat
  vooraan, het bewijs is drie regels, en het toygetal (1,77 = −0,48 + 2 × 1,12) staat er
  direct naast (:260–262).
- "Waarom de premie niet in de PCA hoeft te zitten": het recessievoorbeeld (:398–400) wordt
  in deel (ii) van de propositie exact gemaakt en daarna met het getal voor $n=5$ (een
  kwart) uitgewerkt (:426–428). Abstractie en exemplaar staan bij elkaar.
- "Caps en swaptions": de ongelijkheid [](#eq-termijnstructuur-premies-swaption) krijgt
  meteen een richting en een getal (6,4% duurder, :491).

*Aanmerkingen.*
- Simulatie, :551–552: "De volatiliteit van de rentes is identiek, en alleen de prijzen
  veranderen." Onjuist: de ladingen verschillen tussen de twee modellen (zie Feitelijke
  fouten).
- Wat er brak, :1087: "Een belegger die lange obligaties koopt als de tent hoog staat" —
  "tent" is hier een alias voor de factor geworden (H7), terwijl het elders de vorm van de
  gewichten is (:391, :1076).
- Replicatie, "Forward-veranderingen", :1018–1019: "De gefitte $\kappa$ van 0,075 ligt dicht
  bij de 0,08 uit de theorie." De 0,08 was een illustratieve keuze (:461).
- Simulatie, :708: "Toch heeft een helling na veertig jaar nog een standaardfout van
  ongeveer een derde." Een derde van wat? Bedoeld is 0,33 in absolute termen, bij een
  helling rond één.
- Simulatie, :701–702: "een vertekening zoals die van Stambaugh in
  [](#eq-voorspelbaarheid-stambaugh)." Het geleende resultaat wordt niet in één regel
  herhaald (H2): waarom ligt de mediaan onder nul?

*Beter uitleggen.* Het mechanisme achter de negatieve mediaan onder de EH (persistente
regressor, innovaties die met het rendement samenhangen) in één bijzin; bij "normaal model"
(:479) de naam van het model met normaal verdeelde renteveranderingen en waarom de prijs dan
evenredig is met $\sigma_S$; bij :434–435 zeggen waarom een optieprijs een model in
continue tijd vraagt, zonder het onbepaalde "dan".

*Voor een 9.* lectures/05_28_termijnstructuur_premies.md:551–552 (schokken in plaats van
rentes), :1087 (factor in plaats van tent), :1019 (0,08 als illustratie benoemen), :708
(eenheid), :701–702 (één regel Stambaugh).

### 2. Opbouw en rode draad: 9,0

*Goed.*
- Overzicht stelt de vraag en geeft meteen het antwoord ("Het antwoord is nee", :41), met
  een routekaart die de vier delen van het college volgt.
- De intuïtie voorspelt twee tekens (hoog extra rendement bij een steile curve, dalende
  correlatie met de afstand, :93–95), en beide worden ingelost: :353–354 en :1016.
- Toygetallen keren terug in Theorie (:261), Simulatie (5%, :540–541) en oefening 1;
  5.552 woorden, ruim onder 6.000.

*Aanmerkingen.* Geen die het cijfer drukken. Kleinigheid: de derde alinea van de intuïtie
(de verborgen factor, :82–85) doet geen voorspelling die in :93–95 terugkomt, terwijl de
Theorie haar wel inlost (:394–430).

*Beter uitleggen.* De slotzin van de intuïtie kan de verborgen factor als derde
verwachting meenemen, zodat de PCA-replicatie (:915) ook op een voorspelling antwoordt.

### 3. Taal: 8,5

*Goed.*
- Verband met voegwoorden is overal zichtbaar ("terwijl", "want", "omdat"); geen
  telegramzinnen, geen dubbele punt als lijm.
- Vaste termen volgens STYLE §3; motiefnaam één keer, correct met link (:704).
- De redactie heeft de vaste formule "In de figuur gaat het om" volledig weggewerkt.

*Aanmerkingen.*
- Toy-voorbeeld, stap 3, :136: "De identiteit sluit dus, want op de onafgeronde getallen
  is $-0{,}4773\% + 2 \times 1{,}1236\% = 1{,}7700\%$." "Dus" en "want" in één zin trekken
  tegen elkaar in.
- Simulatie, :652–653: "Links in de figuur telt de afstand tussen de blauwe verdeling en
  nul, rechts de plaats van hun 0,35 naast die verdeling." Elliptisch, en "die verdeling"
  heeft rechts geen eenduidig antecedent.
- Theorie, "Van eindig veel factoren naar een string", :434–435: "Voor de prijs van een
  renteoptie zijn regressies op jaarrendementen niet genoeg, want dan moet de hele curve in
  continue tijd bewegen." "Dan" verwijst nergens naar.
- Simulatie, :708: "Toch heeft een helling na veertig jaar nog een standaardfout van
  ongeveer een derde."

*Beter uitleggen.* Geen inhoudelijk gat; het zijn zinnen die hardop haperen.

*Voor een 9.* De vier zinnen hierboven herschrijven (:136, :652–653, :434–435, :708);
bronregels opnieuw wrappen.

### 4. Toy-voorbeeld: 9,0

*Goed.*
- Met de hand na te rekenen: drie prijzen, vier stappen, één identiteit; recept vooraf,
  tabel hand/code erna (cel bij :147, alle tien waarden gelijk).
- De slotzin zegt wat het getal betekent en waarom één jaar niets bewijst (:178–179).
- Oefening 1 draait het teken van de renteverandering om, met hetzelfde recept.

*Aanmerkingen.* Stap 4 (:140–143) voegt de EH-prijs toe; dat is een tweede vraag naast de
identiteit, maar ze gebruikt dezelfde getallen en wordt in de slotalinea benut. Geen aftrek
daarvoor. Wel de zin in stap 3 (zie Taal).

*Beter uitleggen.* Niets wezenlijks.

### 5. Code en figuren: 8,5

*Goed.*
- De simulatiecode leest als de wiskunde: `bond_loadings` is de recursie voor $A_n, B_n$,
  `simulate_log_prices` een zichtbare lus met burn-in, en de Hansen-Hodrick-som staat
  uitgeschreven.
- Elke replicatietabel zet origineel en hier naast elkaar; figuurbijschriften zeggen wat
  te zien is.
- De controle van de Svensson-formule tegen `SVENY05` (afwijking 5e-07) is een goed
  gebruik van een `print`.

*Aanmerkingen.*
- De data, :754: `(100 * yields[[1, 2, 5, 10]].describe()).round(2)` vermenigvuldigt ook
  `count`; de tabel toont 78300 waarnemingen.
- Campbell en Shiller, :953: `lags=max(steps, 1) - 1 + 1` is een omweg voor `lags=steps`.
- Forward-veranderingen, :1016–1021: vóór de correlatiefiguur staat geen zin die zegt
  waarop te letten; de alinea ervoor beoordeelt de tabel.
- Campbell en Shiller, :982: de kolomnaam `"SE (HH) "` met een spatie aan het eind is een
  truc om een dubbele naam te vermijden.

*Beter uitleggen.* Vóór de correlatiefiguur één zin met wat links (de matrix) en rechts
(twee rijen tegen de string) te vergelijken valt.

*Voor een 9.* lectures/05_28_termijnstructuur_premies.md:754 (`count` buiten de
vermenigvuldiging houden), :953, :982 (een MultiIndex of duidelijke namen), :1019–1021
(leeswijzer vóór de figuur).

### 6. Replicatie en empirie: 9,0

*Goed.*
- De admonition noemt bron, wat, data, verschil en verwachte afwijking kort, en de
  verwachte afwijking (gladde curve, geëxtrapoleerde korte rente) wordt in de oordelen
  daadwerkelijk gebruikt (:849, :917–921, :987–990).
- Elk oordeel begint met Geslaagd, Gedeeltelijk geslaagd of Niet geslaagd, en "Niet
  geslaagd" voor de PCA-toets is eerlijk en inhoudelijk verklaard.
- Tabellen naast de gepubliceerde waarden voor CP tabel 1, 2, 4 en CS tabel 1b.

*Aanmerkingen.*
- Fama en Bliss, :793: "Alle hellingen zijn positief en liggen binnen één standaardfout van
  één" — niet voor $n=2$ over 1964–2026 (0,721, SE 0,274).
- Cochrane en Piazzesi, :836: "het gewicht op de éénjaarsrente negatief en het midden
  positief" — $f^{(3)}$ is 0,15 en $f^{(4)}$ −0,90; het bijschrift (:880) zegt het preciezer
  (top bij $f^{(2)}$).

*Beter uitleggen.* Niets wezenlijks; de twee zinnen preciezer maken.

### 7. Oefeningen: 9,0

*Goed.* Instap op het toy (oefening 1), afleiding met controle op machineprecisie
(oefening 2), uitbreiding van de replicatie met een toets buiten de steekproef (oefening
3) en een rekenoefening die de swaptionclaim uit de Theorie levert (oefening 4). Elke
uitwerking eindigt met wat ze leert.

*Aanmerkingen.* Geen.

## Feitelijke fouten

Nagerekend tegen `$TEMP/F6-05_28_termijnstructuur_premies-out.txt`. Alle toygetallen,
simulatiegetallen (−1,7 tot +0,6; 0,23; 14%; 0,45 tot 1,76; 1,05), Fama-Bliss-,
Cochrane-Piazzesi-, PCA-, Campbell-Shiller- en correlatiegetallen, de oefeningsgetallen
(2,8749%, −0,5525; 0,24→0,26; −1,17; −1,9% en +0,6%; 6,4%, 2,9%, 94%) en
$e^{-0{,}72} \approx 0{,}49$ en $0{,}75/\sqrt{660} \approx 0{,}03$ kloppen.

1. :551–552 "De volatiliteit van de rentes is identiek" — onjuist. $\boldsymbol\Sigma$ en
   $\boldsymbol\Phi^{\mathbb P}$ zijn gelijk, maar $B_n$ volgt uit
   $\boldsymbol\Phi^{\mathbb Q} = \boldsymbol\Phi^{\mathbb P} - \boldsymbol\Sigma\boldsymbol\lambda_1$
   (code: `bond_loadings(PHI_P - D)`), dus de yieldladingen en daarmee de
   yieldvolatiliteit verschillen. Correctie: "de schokken in de toestand zijn identiek".
2. :793 "liggen binnen één standaardfout van één" — onjuist voor 1964–2026, $n=2$:
   |0,721 − 1| = 0,279 > 0,274. Correctie: "op één na binnen één standaardfout" of "rond
   één".
3. :1087 "als de tent hoog staat" — termverschuiving: de tent is de vorm van
   $\boldsymbol\gamma$, niet de waarde van de factor. Correctie: "als de factor hoog staat".
4. (overgenomen uit F4, onzeker) :64 de parafrase van `SantaClara2026` is niet extern
   gecontroleerd.

Kleiner, geen fout maar misleidend: :1019 "de 0,08 uit de theorie" (illustratieve keuze);
:836 "het midden positief" ($f^{(4)}$ is negatief).

## Navertelling in vijf zinnen

De expectations hypothesis zegt dat de rentecurve alleen verwachte korte rentes
weerspiegelt, en een exacte identiteit laat zien dat dit gelijkstaat aan een constant
verwacht extra rendement op obligaties. Fama en Bliss vonden dat de forward spread het extra
rendement voorspelt met een helling rond één, en Campbell en Shiller dat de lange rente bij
een steile curve daalt in plaats van stijgt, wat via dezelfde identiteit één feit is.
Cochrane en Piazzesi vonden één tentvormige combinatie van forwards die de extra rendementen
van alle looptijden voorspelt, en een factor kan dat doen terwijl ze de curve zelf
nauwelijks beweegt. Het string-model geeft elke looptijd een eigen schok, zodat correlaties
met de afstand dalen en swaptions goedkoper zijn dan een eenfactormodel zegt. Op GSW-data
houden de tekens stand, maar de tent en de hoge $R^2$ zijn fragiel: ze verdwijnen op een
gladde curve en falen buiten de steekproef.

Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college op het niveau van natuurlijk gesproken academisch Nederlands
gebracht: verband met voegwoorden, geen sjablonen, geen regeltaal, geen gedachtestreepjes.
Er is geen vakterm van betekenis veranderd door de redactie (de meldingen in
notes/taal-05_28_termijnstructuur_premies.md betreffen alleen zinsbouw), met één
uitzondering die inhoudelijk telt: "de tent" wordt in :1087 als naam voor de factor
gebruikt. Of dat van de redactie komt of ouder is, is uit de notitie niet op te maken.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. :136 "De identiteit sluit dus, want op de onafgeronde getallen is
   $-0{,}4773\% + 2 \times 1{,}1236\% = 1{,}7700\%$."
   Herschrijving: "Op de onafgeronde getallen is $-0{,}4773\% + 2 \times 1{,}1236\% =
   1{,}7700\%$, precies de spread, zodat de identiteit sluit."
2. :652–653 "Links in de figuur telt de afstand tussen de blauwe verdeling en nul, rechts
   de plaats van hun 0,35 naast die verdeling."
   Herschrijving: "Let links op hoe ver de blauwe verdeling van nul af ligt, en rechts op
   waar de 0,35 van Cochrane en Piazzesi valt ten opzichte van de blauwe verdeling."
3. :434–435 "Voor de prijs van een renteoptie zijn regressies op jaarrendementen niet
   genoeg, want dan moet de hele curve in continue tijd bewegen."
   Herschrijving: "Regressies op jaarrendementen zijn niet genoeg om een renteoptie te
   prijzen, want daarvoor moet het model de hele curve in continue tijd laten bewegen."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Gelezen: plannen/kaart-rollen.md (§4, §5, §6, §8), dit bestand volledig, notes/rapport-05_28_termijnstructuur_premies.md
sectie "R9-1 (F6b, ronde 9+)", en het college (lectures/05_28_termijnstructuur_premies.md) volledig, één keer.
Getallen gecontroleerd tegen `tools/nb_outputs.py` (`$TEMP/F6c-05_28_termijnstructuur_premies-out.txt`) en tegen
`prose_stats.py --check`: FB-tabel 1964–2026, $n=2$: helling 0,721, SE 0,274 (|0,721−1| = 0,279 > 0,274, dus
net erbuiten; $n=3,4,5$ wel binnen één SE) — klopt met ":793 op de tweejaarsobligatie tot 2026 na"; hellingen
0,72 tot 1,20 en $t$-waarden 2,6 tot 2,9 kloppen. `describe`-tabel: count 783 (niet 78300) voor kolommen 1, 2,
5; gemiddelden 4,81% en 5,96% kloppen met de proza. `kappa_fit` = 0,075, klopt met ":1021 De gefitte κ van
0,075". `prose_stats --check`: PASS, 5.735 woorden (was 5.552). Geen nieuw of verslechterd getal gevonden.

**Feitelijke fouten (F6).**
1. :551–552 "volatiliteit identiek": **opgelost**. Nu "de schokken in de toestand zijn identiek, maar via
   $\boldsymbol\Phi^{\mathbb Q}$ veranderen de prijzen en daarmee ook hoe sterk elke yield op die schokken
   reageert" — correct: alleen $\boldsymbol\Sigma$ en $\boldsymbol\Phi^{\mathbb P}$ zijn gelijk.
2. :793 "binnen één standaardfout van één": **opgelost**. Nu "op de tweejaarsobligatie tot 2026 na, binnen
   één standaardfout van één"; nagerekend (zie boven) dat dit voor $n=2$ inderdaad net niet geldt en voor
   $n=3,4,5$ wel.
3. :1087 "tent hoog staat": **opgelost**. Nu "als de factor hoog staat".
4. SantaClara2026 (parafrase, overgenomen uit F4, onzeker): **niet opgelost**. Bron is een LinkedIn-post,
   offline niet te controleren; de schrijver benoemt dit expliciet als open in het rapport. Geen feitelijke
   fout aangetoond, blijft staan.

**Drie verbeteringen.**
1. Drie feitelijke onnauwkeurigheden en de termverschuiving (helderheid 8,5 → 9,0): **opgelost**, plus
   :1019 "0,08 uit de theorie" nu "de 0,08 die de Theorie ter illustratie koos" (illustratie i.p.v.
   voorspelling, correct).
2. Vier stroeve zinnen herschrijven (taal 8,5 → 9,0): **opgelost**. :136 en :652–653 vrijwel letterlijk de
   voorgestelde herformulering uit de hardop-toets; :434–435 legt nu uit waarom een optieprijs continue tijd
   vraagt zonder het onbepaalde "dan"; :708 vermijdt het niet-herleidbare "een derde" en herformuleert met
   een vergelijking binnen de tekst zelf (de band 0,45–1,76 is breder dan de populatiewaarde 1,05). Bronregels
   opnieuw gewrapt (rapport); gerenderde tekst ongewijzigd.
3. Code en figuren opschonen (code en figuren 8,5 → 9,0): **opgelost**. :754 `(100 * yields[...]).describe()`
   geeft nu count 783 (nagerekend); :953 is nu `lags=steps`; :1021 heeft nu een leeswijzer vóór de
   correlatiefiguur ("Links in de figuur daalt de correlatie ..., en rechts dalen de twee rijen ...").

**Voor een 9, per criterium.**
- Helderheid: :551–552, :1087, :1019, :708, :701–702 (Stambaugh in één bijzin, nu "want de spread is
  persistent en zijn schokken hangen samen met het gerealiseerde rendement") — alle vijf **opgelost**.
- Taal: :136, :652–653, :434–435, :708 — alle vier **opgelost**.
- Code en figuren: :754, :953, :982 (nu kolommen "SE t/m 1987" en "SE t/m 2026", geen spatietruc),
  :1019–1021 (leeswijzer) — alle vier **opgelost**.

**Aanmerkingen zonder "Voor een 9".** Opbouw (derde verwachting bij de verborgen factor, :91–94) is
toegevoegd en ingelost bij de PCA-tabel (:916–922); dit criterium stond al op 9,0 en blijft dat (plafond).
Replicatie, :836 "midden positief": aangepast naar "dat op $f^{(2)}$ en $f^{(3)}$ positief" (0,81 en 3,00,
correct, $f^{(4)}$ niet meer genoemd); dit criterium stond al op 9,0 en blijft dat (plafond). :479 normaal
model: nu "het normale model van Bachelier" met de reden dat de swaprente dan evenredig is met haar
standaardafwijking; ook onder Helderheid "Beter uitleggen", geen apart deelcijferpunt.

**Hardop-toets.** Alle drie geciteerde zinnen herschreven, :136 en :652–653 vrijwel letterlijk de
voorgestelde herformulering, :434–435 in dezelfde geest maar met een eigen formulering.

Geen verslechtering en geen nieuwe feitelijke fout gevonden. Alle "Voor een 9"-punten van de drie
criteria met een concreet actiepunt zijn opgelost; alleen de onzekere SantaClara-parafrase (feitelijke
fout 4, structureel niet na te gaan) blijft open en raakt geen van de zeven criteria rechtstreeks.

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
| | **Eindcijfer (gewogen)** | | **9,0** |

Geen deelcijfer onder 8,5; taal blokkeert niet. Streefcijfer 9,0 gehaald.
