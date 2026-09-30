STATUS 05_27_drie_antwoorden F6c words=5856 prose=PASS open=1 cijfer=9,0 min=8,8

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,8 -> F6c 9,0.

# Eindbeoordeling 05_27_drie_antwoorden

## Eerste herziening (workflow §12)

Eerste herziening; er is geen vorig cijfer. `prose_stats --check`: PASS (5.636 woorden,
zinnen gemiddeld 18,1, p90 28, geen zin > 40, alinea gemiddeld 46, 8 alinea's van één zin,
2 sjablonen, 0 "Wie"-zinnen aan het begin). Motiefnamen: "de standaardfout van 2%" twee
keer (:100, :988), "risico of vergissing" één keer als kop (:1166). `open=2`: twee
feitelijke fouten over het teken van $\theta - 1$ en $\lambda_e$ in Epstein-Zin/Bansal-Yaron
(hieronder). Alle overige getallen in de proza zijn nagerekend tegen de celuitvoer
(`$TEMP/F6-05_27_drie_antwoorden-out.txt`) en kloppen, net als de handstappen van het
toy-voorbeeld, de Epstein-Zin-toy (:431–435), de Barro-formules (:678–680 met de hand:
$r^f = 0{,}0101$, premie $0{,}0586$, PD $20{,}68$) en de afleiding in oplossing 2
(:1231–1239). De vier onzekere feitenrijen uit F23 (bronnen Wachter 2005, Santa-Clara,
Beeler-Campbell niet raadpleegbaar) zijn geen fouten en tellen hier niet als open.

Termcontrole na de taalredactie: "de grens van Hansen en Jagannathan" (:190–192) is de
HJ-ondergrens voor $\sigma(m)/\E[m]$ en wordt correct gebruikt; "elk via een ander
mechanisme" (:1166–1167), "Zo krijgt nieuws ..." (:414) en de herschreven
Bansal-Yaron-opening (:470–476) behouden de betekenis. Geen vakterm is door de redactie van
betekenis veranderd. De fout op :413 staat in een zin die de redacteur niet meldt.

## De drie verbeteringen met het meeste effect

1. **De twee tekenfouten in Epstein-Zin en Bansal-Yaron herstellen** (helderheid 8,5 →
   9,0). (a) :413 "Bij $\gamma > 1/\psi$ is $\theta - 1 < 0$" klopt alleen als ook
   $\psi > 1$: $\theta - 1 = (1/\psi - \gamma)/(1 - 1/\psi)$, dus bij $\gamma = 10$,
   $\psi = 0{,}5$ is $\theta = 9$. Schrijf "Bij $\gamma > 1$ en $\psi > 1$ is
   $\theta < 0$". (b) :555–556 "bij $\psi < 1$ dalen prijzen bij goed groeinieuws en draait
   het teken van $\lambda_e$ om": invullen geeft
   $\lambda_e = (\gamma - 1/\psi)\kappa_1\varphi_e/(1 - \kappa_1\rho)$, positief zodra
   $\gamma > 1/\psi$, ongeacht $\psi$. Wat bij $\psi < 1$ omdraait is $A_1$ (de
   vermogensprijs daalt bij goed nieuws); de marktprijs reageert pas verkeerd als
   $\phi < 1/\psi$. Herschrijf de bullet zo dat de reden voor $\psi > 1$ de richting van de
   prijsreactie is, niet het teken van $\lambda_e$. Definieer daarbij in één bijzin
   $\kappa_{1,m}$ en $A_{2,m}$, die in [](#eq-drie-antwoorden-by-premie) (:543–545)
   staan maar nergens in de tekst worden ingevoerd.
2. **De vijf stroeve zinnen uit de hardop-toets herschrijven** (taal 8,5 → 9,0):
   "dezelfde handvol momenten" (:720, "hetzelfde handvol"), "geen van drie" (:1137,
   :1158), "tussen ze kiezen" (:41), de dubbele ontkenning in de Yale-zin (:1171–1173) en
   de gesplitste "wijst niet op ..., want ..., maar op" (:1124–1126). Ruim ook de
   rewrap-resten op (losse regel met één woord: :61, :143, :786, :1125, :1136, :1153,
   :1167, :1169), die in de .md het lezen hinderen.
3. **De percentielen uit de lopende tekst van de dataplaatsing halen** (replicatie 8,5 →
   9,0). :1128–1147 noemt in vier bullets veertien getallen die al in de plaatsingstabel
   van cel 13 staan. Laat de bullets per moment het oordeel geven (binnen/buiten welke
   band) en verwijs naar de tabel; houd alleen 8,3% met SE 2,0 en 0,51 tegen 0,24 in de
   tekst.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,8

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,5 |
| | **Eindcijfer** (gewogen) | | **8,8** (8,75) |

Geen deelcijfer onder 8,5; taal ≥ 8, dus niet geblokkeerd. Het eindcijfer haalt de 9,0
niet.

### 1. Helderheid (8,5)

*Goed.*
- Theorie, "Drie uitwegen": één zin per model zegt waar het de HJ-grens haalt
  (vermenigvuldiger vergroten, nieuws over alle jaren prijzen, een staart toevoegen), met
  de tabel "vrije, moeilijk meetbare parameter" als rode draad.
- Campbell-Cochrane: het getal staat naast de formule (twintig keer $\gamma$ bij de marge
  van 5% op :218, Sharpe-ratio 0,51 op :289, $\bar S = 0{,}057$ op :364).
- Observationele equivalentie: formele definitie gevolgd door een gewone zin en de
  afhankelijkheid van $T$ met getal (duizend tegen honderd jaar).

*Aanmerkingen.*
- Epstein-Zin (:413): "Bij $\gamma > 1/\psi$ is $\theta - 1 < 0$, zodat een slecht
  rendement op vermogen de SDF verhoogt." Onjuist zonder $\psi > 1$ (zie feitelijke
  fouten).
- Bansal-Yaron (:555–556): "want bij $\psi < 1$ dalen prijzen bij goed groeinieuws en
  draait het teken van $\lambda_e$ om." Het teken van $\lambda_e$ draait niet om.
- Bansal-Yaron, propositie (:543–545): "$\lambda_w\,\kappa_{1,m}A_{2,m}\,\sigma^2_w$" —
  $\kappa_{1,m}$ en $A_{2,m}$ worden nergens ingevoerd; de lezer moet ze uit de code
  (:592–593) halen.
- Waarom de prijs-dividendratio beweegt (:697–698): "maar alleen in het habit-model loopt
  die beweging volledig via de premie." De Gabaix-variant, die in de simulatie meedoet,
  wordt niet ingedeeld.

*Beter uitleggen.* Waarom $\psi > 1$ nodig is: de lezer krijgt nu een verkeerde reden. Eén
zin met de richting (bij $\psi > 1$ stijgt de vermogensprijs bij goed groeinieuws, zodat
het vermogen een slechte hedge tegen slecht nieuws is) en het getal $\lambda_e = 17{,}9$
uit cel 5 zou het mechanisme dragen. Bij $A_2$ en $\lambda_w$: in één bijzin wat een
volatiliteitsschok met de prijs doet (daalt) en waarom dat maar 0,2% premie oplevert
($\sigma_w$ is klein).

*Voor een 9.* Herstel :413 en :555–556 (verbetering 1); voer $\kappa_{1,m}$ en $A_{2,m}$
in bij :515–516; plaats op :713–715 de Gabaix-variant in één bijzin (de ratio beweegt via
de gevoeligheid van het dividend voor de ramp, dus via premie én verwachte groei).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Het toy-getal loopt door: 13,8% → 0,9% keert terug in Rietz-Barro (:622–623), $p = 1{,}7\%$
  op :667–668, en 5,67 tegen 4,92 procentpunt in de dataplaatsing (:1133).
- De intuïtie voorspelt de richting per model en de theorie lost dat in gewone zinnen in
  (:476, :664–665); de verwachting "de getallen scheiden de modellen niet" (:95–97) wordt
  in de simulatie en de replicatie getoetst.
- Routekaart (:184–188), Samengevat met richting en reden per parameter, 5.636 woorden.

*Aanmerkingen.*
- Overzicht (:59–62): "Volgens Santa-Clara past elk model op de data, leunt elk op een
  parameter die niet onafhankelijk te controleren is, en zijn de modellen op de
  beschikbare data niet te onderscheiden." Herhaalt vrijwel letterlijk :39–41.
- Theorie, Bansal-Yaron: de propositie met $A_1$, $A_2$, $A_{1,m}$, twee prijzen van risico
  en twee kanalen is de zwaarste stap van het college, terwijl het tweede kanaal minder dan
  4% van de premie levert (cel 5: 0,20 van 5,54).

*Beter uitleggen.* Zeg bij de propositie dat het volatiliteitskanaal klein is vóór de
lezer $A_2$ moet ontcijferen, zodat duidelijk is welke helft ertoe doet.

### 3. Taal (8,5)

*Goed.*
- Zinsritme is gevarieerd (gemiddeld 18,1, p90 28) en verband loopt via voegwoorden
  ("omdat", "zodat", "want"), bijvoorbeeld in Intuïtie en Samengevat.
- Geen telegramzinnen vóór codecellen; elke cel wordt met een volledige zin aangekondigd.
- Motiefnamen binnen de grens en nergens als handelend onderwerp.

*Aanmerkingen.*
- Observationele equivalentie (:719–720): "Drie modellen die elk één moeilijk meetbare
  parameter op dezelfde handvol momenten afstellen" — "handvol" is een het-woord:
  "hetzelfde handvol".
- Prijs-dividendratio (:1136–1137): "De modellen verklaren dus dat de ratio beweegt, maar
  geen van drie hoeveel" en Waar het breekt (:1158): "Geen van drie haalt de volatiliteit"
  — "geen van de drie".
- Overzicht (:41): "zodat de data niet tussen ze kiezen" — spreektaal; "er niet tussen
  kunnen kiezen".
- Risico of vergissing (:1171–1173): "In de Yale-lezing verklaart een model met een
  parameter die niet te controleren is niets wat een gedragsmodel met extrapolerende of
  angstige beleggers niet ook verklaart." Dubbele ontkenning, moet twee keer gelezen worden.
- Gedeeltelijk geslaagd (:1124–1126): "Die ene band wijst niet op een codefout, want de
  modellen reproduceren hun bronnen, maar op een hoge Amerikaanse premie." De tegenstelling
  "niet op ... maar op" wordt door de want-zin uit elkaar getrokken.
- Toy, stap 5 (:152–153): "Een steekproef zonder ramp toont dan een hoog rendement zonder
  het risico dat het verdient" — "het" kan het rendement of de steekproef zijn.
- Rewrap-resten (regels met één of twee woorden): :61 "beschikbare", :143 "het", :786
  "blijft elk", :1125 "op een", :1136, :1153, :1167 "een", :1169 "een".

*Beter uitleggen.* Geen inhoudelijk punt; de zinnen hierboven zijn stroef, niet onduidelijk.

*Voor een 9.* Herschrijf de zes geciteerde zinnen (:41, :720, :1124–1126, :1137, :1158,
:1171–1173, :152–153) en rewrap de alinea's met losse restregels.

### 4. Toy-voorbeeld (9,5)

*Goed.*
- Vijf handstappen met zes decimalen, alle nagerekend (bv. $\E[m] = 0{,}991069$,
  $k = 0{,}961772$, premie 4,92), en een tabel hand/code met de wereld zonder ramp als
  derde kolom.
- Eén mechanisme (een zeldzame ramp maakt de SDF groot in één toestand); het
  peso-probleem volgt uit dezelfde getallen.
- De slotzin zegt wat de getallen betekenen (van nul premie en 13,8% rente naar bijna 5%
  en onder 1%, bij een verwachte groei die maar 0,7 punt daalt).

*Aanmerkingen.* Geen.

*Beter uitleggen.* Niets nodig.

### 5. Code en figuren (8,5)

*Goed.*
- Elke cel heeft een zin ervoor en erna; figuren hebben een leeswijzer vooraf (:938–940,
  :1102–1103) en een conclusie erna.
- Eén plotfunctie voor simulatie en data (`plot_bands`), zodat de tweede figuur de eerste
  met datalijnen is.
- `sample_moments` bewerkt data en simulatie op precies dezelfde manier (:828–829).

*Aanmerkingen.*
- Campbell-Cochrane, cel 3 (:326–356): `cc_solve` bouwt de matrix met `np.add.at`,
  `np.broadcast_to` en een analytisch weggeïntegreerde dividendschok in één regel
  (`load`, `extra`, `K`); de code leest niet als [](#eq-drie-antwoorden-cc-pd).
- Bansal-Yaron, cel 5 (:575): `kappas = lambda z: (np.log1p(np.exp(z)) - ...)` is een
  truc zonder naam of formule in de tekst.
- Simulatie, cel 8 (:833, :851): `cc_simulate` en `by_simulate` hebben geen docstring,
  terwijl alle andere functies er een hebben.

*Beter uitleggen.* Bij `cc_solve` een zin in de tekst die zegt welke rij van $\mathbf{M}$
bij welk roosterpunt hoort; bij `kappas` de formules $\kappa_1 = e^{\bar z}/(1+e^{\bar z})$
en $\kappa_0$ in de proza (:509–510).

*Voor een 9.* Splits in `cc_solve` de kerngewichten `K` en de interpolatie in twee
benoemde stappen (:344–352); geef `kappas` een formule in de tekst (:509); docstrings bij
:833 en :851.

### 6. Replicatie en empirie (8,5)

*Goed.*
- De admonition heeft bron, wat, data, verschil en een toetsbare verwachte afwijking per
  deel, onder 250 woorden.
- Tabel origineel/hier voor Wachter en Beeler-Campbell; oordelen beginnen met
  "Geslaagd" en "Gedeeltelijk geslaagd" en verwijzen naar de verwachting.
- Het afwijkende gemiddelde log rendement (6,76 tegen 6,62) krijgt een reden.

*Aanmerkingen.*
- De Amerikaanse data in de banden (:1128–1147): "Het gemiddelde overrendement valt binnen
  de band van Bansal-Yaron (percentiel 0,93) en net boven die van Campbell-Cochrane en de
  Gabaix-variant (0,99 en 0,98)." Vier bullets met veertien getallen uit de
  plaatsingstabel.
- Verwachte afwijking (:1020–1021): "De premie van de data ligt binnen de 95%-band van ten
  minste drie modellen" — de band van Barro (iid) is 4,5–6,4% breed en kan een premie van
  8% nooit bevatten; de verwachting hield daar geen rekening mee.

*Beter uitleggen.* Waarom Barro (iid) een zo smalle band heeft (geen dividendrisico buiten
consumptie, volatiliteit 4%), in één bijzin bij de simulatie.

*Voor een 9.* Verbetering 3 (:1128–1147); stel de verwachting op :1020 in op de drie
modellen met realistische volatiliteit.

### 7. Oefeningen (9,5)

*Goed.*
- Instap is een variatie op het toy (p = 0,01) met handgetallen en code.
- Oefening 2 is een echte afleiding, nagerekend en correct, met de les dat de EIS pas bij
  voorspelbare groei op de premie werkt.
- Oefeningen 3 en 4 breiden de replicatie uit (rooster, deelsteekproeven) en eindigen elk
  met wat ze leren.

*Aanmerkingen.* Geen.

*Beter uitleggen.* Niets nodig.

## Feitelijke fouten

1. **:413** "Bij $\gamma > 1/\psi$ is $\theta - 1 < 0$". Nagerekend:
   $\theta - 1 = (1/\psi - \gamma)/(1 - 1/\psi)$; bij $\gamma = 10$, $\psi = 0{,}5$ is
   $\theta = -9/-1 = 9$ en $\theta - 1 = 8 > 0$. Juist: "bij $\gamma > 1$ en $\psi > 1$ is
   $\theta < 0$" (de kalibratie, $\theta = -27$ in cel 5, valt daaronder).
2. **:555–556** "bij $\psi < 1$ ... draait het teken van $\lambda_e$ om". Nagerekend:
   $(1-\theta) = (\gamma - 1/\psi)/(1 - 1/\psi)$ en $A_1 = (1 - 1/\psi)/(1 - \kappa_1\rho)$,
   dus $\lambda_e = (\gamma - 1/\psi)\kappa_1\varphi_e/(1 - \kappa_1\rho) > 0$ voor elke
   $\psi > 1/\gamma$; beide factoren wisselen tegelijk van teken. Wat bij $\psi < 1$
   omdraait, is $A_1$ (de vermogensprijs daalt bij goed nieuws). Controle met cel 5:
   met $1/(1 - \kappa_1\rho) = A_1/(1/3) = 43{,}7$ geeft
   $\lambda_e = (10 - 2/3) \times \kappa_1 \times 0{,}044 \times 43{,}7 \approx 17{,}9$ bij
   $\kappa_1 \approx 0{,}997$, gelijk aan de celuitvoer (17,897).

Alle overige getallen in de proza stemmen overeen met de celuitvoer (steekproef: :364,
:610–614, :690–693, :915, :984–998, :1056–1063, :1101, :1129–1146, :1258, :1297,
:1338–1343).

## Navertelling in vijf zinnen

Rond 2000 kreeg de aandelenpremie drie consumptie-antwoorden: een externe gewoonte die de
risicoaversie opdrijft als consumptie haar nadert, Epstein-Zin-voorkeuren met een kleine
persistente groeicomponent, en zeldzame rampen. Elk model haalt de HJ-grens op een eigen
manier en haalt een premie van rond 5% met een lage rente, maar leunt op één parameter
($\phi$, $\rho$, $p$) die honderd jaar data niet vastleggen. Simulaties van duizend
steekproeven van honderd jaar tonen dat de gemiddelde premie en de voorspelbaarheid de
modellen niet scheiden, omdat de standaardfout van een eeuwgemiddelde groter is dan hun
verschil. Op Amerikaanse data 1930–2025 halen ze geen van drieën de volatiliteit van de
prijs-dividendratio, en de consumptie-autocorrelatie, het moment dat het scherpst scheidt,
hangt af van de jaren van de Depressie. De modellen zijn daarom observationeel equivalent,
en de premie is een feit met concurrerende theorieën. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijk gemaakt: staccato is verdwenen, verwijswoorden
kloppen, en de BY-opening heeft nu richting. Er resteren een grammaticale fout
("dezelfde handvol"), twee elliptische "geen van drie" en een paar zinnen met een
gebroken of dubbel ontkennende bouw, plus rewrap-resten. Hardop-toets (Overzicht,
Gedeeltelijk geslaagd, Wat er brak):

1. :41 "Elk leunt echter op een parameter die honderd jaar data niet vastleggen, zodat de
   data niet tussen ze kiezen." → "Elk leunt echter op een parameter die honderd jaar data
   niet vastleggen, zodat die data er niet tussen kunnen kiezen."
2. :1124–1126 "Die ene band wijst niet op een codefout, want de modellen reproduceren hun
   bronnen, maar op een hoge Amerikaanse premie." → "Dat de premie maar in één band valt,
   komt door een hoge Amerikaanse premie en niet door een codefout, want de modellen
   reproduceren hun bronnen."
3. :1171–1173 "In de Yale-lezing verklaart een model met een parameter die niet te
   controleren is niets wat een gedragsmodel met extrapolerende of angstige beleggers niet
   ook verklaart." → "In de Yale-lezing voegt een model met een niet te controleren
   parameter niets toe, want een gedragsmodel met extrapolerende of angstige beleggers
   verklaart dezelfde feiten."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Controle van de verwerking in `notes/rapport-05_27_drie_antwoorden.md` (R9-1) tegen de stand
vóór F6b. `prose_stats --check`: PASS (5.856 woorden, zinnen gemiddeld 18,4, p90 28, geen
zin > 40).

**Getallencontrole.** Alle nieuwe of gewijzigde getallen zijn herleidbaar: 17,9 voor
$\lambda_e$ (cel 5: 17,897), 0,2 van ruim 5 procentpunt voor het volatiliteitskanaal (cel 5:
0,199 van 5,54), Barro (iid) rendementsvolatiliteit rond 4% (cel 10: 0,042 met band
0,020–0,088), banden voor $\sigma(\log \mathrm{PD})$ hoogstens 0,24 (cel 10) tegen 0,51 in
de data, en de percentielwoorden in de vier bullets (0,93; 0,57/0,59; 0,15/0,95 uit de
plaatsingstabel) kloppen met "binnen", "midden", "onderkant" en "bovenkant". Het toy-getal
5,67 tegen 4,92 is ongewijzigd. Tekens: $\gamma > 1$ en $\psi > 1$ geeft
$\theta = (1-\gamma)/(1-1/\psi) < 0$ en dus $\theta - 1 < 0$ (klopt). Geen niet-herleidbaar
getal.

**Punten uit de beoordeling.**
- Feitelijke fout 1 (:413): opgelost. Feitelijke fout 2 (bullet $\psi > 1$): opgelost; de
  reden is nu de richting van de vermogensprijs, $\lambda_e$ blijft positief.
- Verbetering 1: opgelost ($\kappa_{1,m}$, $A_{1,m}$, $A_{2,m}$ ingevoerd, $\kappa_1$ en
  $\kappa_0$ met formule, volatiliteitskanaal klein vóór de propositie, Gabaix-variant
  ingedeeld).
- Verbetering 2: grotendeels opgelost; "hetzelfde handvol", "geen van de drie", :41, Yale-zin,
  "Die ene band"-zin en peso-zin zijn herschreven, rewrap-resten weg (één rest: "schaars:
  prijzen van" voor "verzekering", onschuldig).
- Verbetering 3: opgelost; de bullets geven het oordeel per moment en verwijzen naar de tabel.
- Overzicht-herhaling: opgelost. Code (`cc_solve` in twee stappen met uitleg over rij $i$,
  `kappas` met formulecommentaar, twee docstrings): opgelost. Verwachting (3) en Barro-smalle
  band: opgelost in inhoud.

**Verslechterd (open=1).** In de simulatiebullet staat nu "Alleen Barro met onafhankelijke
rampen een smalle band heeft, omdat zijn dividend gelijk is aan consumptie ..." (ongeveer
:1003): de zin heeft geen hoofdzin ("Alleen Barro ... heeft een smalle band" of "Barro met
onafhankelijke rampen heeft een smalle band"). Dit is een nieuwe taalfout, geen feitelijke.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,8 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,5 |
| | **Eindcijfer** (gewogen) | | **9,0** (9,04) |

Taal blijft onder het plafond van 9,0 door de gebroken zin; geen deelcijfer onder 8,5, taal
niet geblokkeerd. Plafond (9,1 bij volledige oplossing) niet overschreden.

## Afhandeling open punt (orchestrator)

De zin zonder hoofdzin bij de simulatiebullet (r.1003) en de rewrap-rest "schaars: prijzen van" (r.1192) zijn door de orchestrator hersteld vóór de commit; prose_stats PASS.
