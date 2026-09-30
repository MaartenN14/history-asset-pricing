STATUS 06_35_machine_learning F6c words=5961 prose=PASS open=0 cijfer=9,0 min=8,9

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

## Eerste herziening (workflow §12)

Eerste herziening. Er is geen vorig cijfer. Gelezen: de .md volledig, de celuitvoer via
`tools/nb_outputs.py` (`$TEMP/F6-06_35_machine_learning-out.txt`), `prose_stats` (5700 woorden,
zinnen gemiddeld 17,8, p90 27, geen zin > 40, alinea gemiddeld 56, dubbele punt 0,4 per 1000).

## De drie verbeteringen met het meeste effect

1. **Replicatie (2) krijgt een tabel origineel/hier en de getallen verhuizen uit de proza**
   (vindplaats 06_35_machine_learning.md:1013–1028 en 1100–1105; oordeelzin 949). De tweede
   replicatie heeft geen tabel met de uitkomst van KNS naast die van hier, en de twee alinea's
   na de KNS-cel bevatten samen ruim tien getallen (39%, 40%, −170, 13,5, 4,3, 2,32, 2,07, 0,61,
   0,24, 0,25). Een tabel met vier rijen (cs-$R^2$ en Sharpe, volledige SDF en vier variabelen,
   KNS kwalitatief of met hun getal, hier) haalt die getallen uit de lopende tekst. Herstel
   tegelijk de onjuiste zin "Na 2005 liggen alle getallen lager" (949). Verwacht deelcijfer
   replicatie: 9,0.
2. **Helderheid: één feitelijke vakterm, één onbenoemde parameter, één alias**
   (499, 437 en 1013, 72/95/254/456, 521–522). "LASSO schaalt" is onjuist: LASSO schuift met
   een vast bedrag, zoals het college zelf op 293–294 zegt. $\kappa$ krijgt nergens een
   betekenis of orde van grootte, terwijl de replicatie $\kappa = 0{,}133$ meldt. Onder de prior
   is $\E[\boldsymbol{\mu}'\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}] = \kappa^2$, dus $\kappa$ is
   de verwachte maximale Sharpe-ratio per maand, en 0,133 is ongeveer 0,46 per jaar. Die ene
   zin maakt de KNS-prior economisch leesbaar. "Kenmerken" (4 keer) en "karakteristieken"
   (33 keer) zijn hetzelfde begrip. Verwacht deelcijfer helderheid: 9,5.
3. **Taal en code: regeltaal weg, twee cellen toegelicht** (602, 804, 321, 254; 616–619;
   1030–1034). Twee zinnen gaan over het werk in plaats van over de economie ("zodat geen cel
   langer dan een minuut duurt", "dan zit de fout eerder in de code"). Tussen de twee
   niet-lineaire cellen staat geen zin. Het trucje met `X_aug`/`y_aug`, dat de
   KNS-doelfunctie in een gewone LASSO giet, wordt nergens uitgelegd. Verwachte
   deelcijfers: taal 9,0, code en figuren 9,0.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |
| | **Gewogen eindcijfer** | | **8,7** (8,675) |

### 1. Helderheid van de uitleg: 8,5

*Goed.*
- Opzet: de breuk-even-rekening naast de formule (0,5% $R^2$, 920 voorspellers, 184.000
  effectieve waarnemingen tegen 720 maanden) maakt de variantieterm voelbaar (246–251).
- Flexibiliteit: de variantie van een bos, $\rho\sigma^2 + (1-\rho)\sigma^2/B$, krijgt direct
  het getal "minstens de helft" bij $\rho = 0{,}5$ (320–322), en early stopping wordt als krimp
  herkend (329–330).
- Martin en Nagel: de benadering $1/(1 + tNg/(\sigma^2J))$ krijgt meteen 2% en 44% (483–486),
  en die getallen keren terug in de simulatie.

*Aanmerkingen.*
- Theorie, Samengevat (499): "Ridge schaalt, LASSO schaalt en selecteert, en de beste straf
  stijgt met de verhouding tussen ruis en signaal." LASSO schaalt niet, maar trekt een vast
  bedrag $\lambda_1/d$ af (293–294, 194: "de sterke met een vast bedrag krimpt"). Feitelijke fout.
- De SDF krimpen (437–438): "Hoe groter $\kappa$, hoe kleiner $\gamma$ en hoe minder de schatter
  krimpt, omdat de prior dan grotere premies toelaat." $\kappa$ heeft geen naam en geen orde van
  grootte (H2); in de replicatie (1013) staat "$\kappa = 0{,}133$" zonder betekenis.
- Intuïtie en Opzet (72, 254): "Denk aan een analist die tweehonderd kenmerken van elk aandeel
  kent." Elders heten ze "karakteristieken" (H7).
- Simulatie (521–522): "in de niet-lineaire met $(c_1^2 - \tfrac13) + c_1c_2 +
  \operatorname{sign}(c_3x_t)$". De code weegt de termen ongelijk (elke term eenheidsvariantie),
  dus "evenredig met" klopt alleen voor de lineaire wereld.
- Replicatie (2) (1030–1034): "De tweede is de elastic net op
  [](#eq-machine-learning-kns-ridge) met een oplopende straf op de absolute waarde." Hoe die
  schatter in de code tot stand komt, blijft onvermeld (zie code).

*Beter uitleggen.*
- Wat $\kappa$ is: één bijzin bij 437 ("$\kappa^2$ is de verwachte gekwadrateerde maximale
  Sharpe-ratio onder de prior") en het jaargetal bij 1013.
- De maatstaf van KNS (449–451) krijgt geen getal; een orde van grootte ("een $R^2$ van 0,4
  betekent ...") helpt, en komt pas in de replicatie.
- IPCA (370–395) is de enige theoriesubsectie zonder getal; één uitkomst van Kelly, Pruitt en
  Su (aantal factoren, $R^2$) maakt "verklaren beter" concreet.

*Voor een 9.* Herstel 06_35_machine_learning.md:499 (schuift in plaats van schaalt), geef
$\kappa$ betekenis en orde van grootte op :437 en :1013, maak "kenmerken" op :72, :95, :254
en :456 "karakteristieken", en schrijf op :521 dat elke term op eenheidsvariantie is
geschaald.

### 2. Opbouw en rode draad: 9,0

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in de tweede zin, met de twee
  voorbehouden (geen verklaring, na kosten en na 2005 kleiner) die de replicatie inlost (37–41,
  939–950).
- De routekaart van Theorie (200–206) en het Samengevat (495–503) sluiten op elkaar aan, en
  elke `###` begint met haar bewering.
- De drie verwachtingen van de Intuïtie (99–101) komen alle drie terug: flexibiliteit in de
  eerste simulatie (660–665), leren in de tweede (766–777), krimp in de GKX-tabel en oefening 4.
- 5700 woorden, onder de grens.

*Aanmerkingen.*
- Simulatie (667): "OLS faalt hier niet zoals bij GKX, omdat 40 voorspellers tegen 54.000
  trainingswaarnemingen te weinig zijn om de variantieterm te laten tellen." De hoofdvoorspelling
  van het college (krimp verslaat OLS) wordt in de eigen simulatie dus niet getoond; ridge en
  OLS liggen er binnen 0,05 procentpunt van elkaar.
- Simulatie (668): "Oefening 4 laat OLS instorten zodra $P/n_{\text{eff}}$ groeit." In de
  uitvoer stort OLS in één van drie replicaties in (−16%), in de andere twee niet (0,5 en 0,1).

*Beter uitleggen.* De toy-getallen keren terug in de Theorie (:295) en in oefening 3 (:300 en
:1242), maar niet in de kalibratie van de simulatie (H11). Dat is verdedigbaar; één zin die het
signaal van 2% tegen de ruis van 10% vertaalt in de verhouding $\sigma^2/\beta^2$ van :298–300
zou de draad sluiten.

### 3. Taal: 8,5

*Goed.*
- De zinnen lopen: gemiddeld 17,8 woorden, afwisselend, verbonden met "want", "zodat",
  "terwijl" (bijvoorbeeld 72–77, 455–458).
- Geen gedachtestreepjes, geen puntkomma's, 0,4 dubbele punt per 1000 woorden, geen
  "Wie"-zinnen, motiefnamen elk één keer en met betekenis (252–253, 1127).
- De Chicago- en Yale-lezing (1127–1137) leest als een gesproken betoog.

*Aanmerkingen.*
- Simulatie (602): "De derde lineaire replicatie staat in een eigen cel, zodat geen cel
  langer dan een minuut duurt." Regeltaal: een melding over het werk, geen economie.
- Replicatie-admonition (804): "In (2) verslaat de SDF met een handvol hoofdcomponenten een SDF
  met even weinig signalen, en wijkt die rangorde af, dan zit de fout eerder in de code."
  Regeltaal.
- Flexibiliteit (321–322): "Bij $\rho = 0{,}5$ blijft dus hoe veel bomen ook minstens de helft
  van de variantie over." Woordvolgorde en spelling ("hoeveel").
- Opzet (254–255): "Het vergaat de analist met tweehonderd kenmerken uit de intuïtie dus
  precies zo, en krimp is het antwoord." "Uit de intuïtie" verwijst naar het kopje, niet naar
  de zaak.
- Overzicht (57–59): "Daarmee verschoof de vraag van welke karakteristiek een risicopremie
  heeft naar hoeveel voorspelbaarheid een gedisciplineerde machine uit alle karakteristieken
  samen haalt." Te zwaar voor één adem.

*Beter uitleggen.* Geen inhoudelijk punt; de taalpunten zijn herschrijvingen van bestaande
zinnen.

*Voor een 9.* Herschrijf 06_35_machine_learning.md:602, :804, :321, :254 en :57 (zie
hardop-toets hieronder) en trek "kenmerken" gelijk met "karakteristieken".

### 4. Toy-voorbeeld: 9,0

*Goed.*
- Vijf regels handwerk met orthogonale kolommen, zodat elke methode in één deling uit te
  rekenen is (149–158); alle getallen kloppen ($z_1 = 16$, $z_2 = -3$, residuen, 3,5 van 30,
  88%).
- Tabel hand tegen scikit-learn is identiek in de uitvoer, en de schaalkwestie van `Lasso` wordt
  benoemd (187–188).
- Het getal $d = 10$ en de halvering komen terug in de Theorie (295) en in oefeningen 1 en 3.

*Aanmerkingen.*
- Toy (160–161): "De codecel rekent dezelfde gewichten uit met scikit-learn en schat daarnaast
  een regressieboom met één split." De boom is een tweede mechanisme naast krimp; hij verdedigt
  zich later (315), maar maakt het toy breder dan nodig.

*Beter uitleggen.* De $R^2$ van 88% in de steekproef, met twee gewichten op vijf waarnemingen,
is precies het overfit-verschijnsel van de Opzet; één bijzin in de slotalinea (193–196) zou
zeggen wat dat getal betekent.

### 5. Code en figuren: 8,5

*Goed.*
- `simulate_gkx`, `fit_validate` en `run_replication` lezen als de opzet in de tekst, met
  benoemde tussenresultaten en een zichtbare lus over maanden (532–599).
- Elke figuur heeft vooraf een leeswijzer en daarna een alinea die zegt wat te zien is
  (625–626, 660–672; 730–734, 766–777).
- `martin_nagel_economy` volgt [](#eq-machine-learning-mn) regel voor regel, met commentaar bij
  de diagonalisatie.

*Aanmerkingen.*
- Simulatie (615–619): tussen de cel `runs_nonlinear = [...]` en de volgende cel staat geen zin.
- Replicatie (2) (1049–1054): `X_aug = np.vstack([S_half, np.sqrt(gamma_star) * np.eye(H)])`
  zonder uitleg in de tekst waarom dit de doelfunctie [](#eq-machine-learning-kns-ridge) plus
  een L1-straf oplevert.
- Toy (170): "# sklearn scales the squared loss by 1/(2n): alpha = lambda / n for the L1 part"
  geldt voor `Lasso` en `ElasticNet`, niet voor `Ridge`.

*Beter uitleggen.* Eén zin vóór de sparse-cel: $\lVert \mathbf{y}_{aug} - \mathbf{X}_{aug}\mathbf{b}\rVert^2$
is precies de KNS-doelfunctie, zodat een gewone LASSO de elastic net oplost.

*Voor een 9.* 06_35_machine_learning.md:616 (zin tussen de twee cellen), :1030–1034
(augmentatie in één zin), :170 (commentaar beperken tot L1).

### 6. Replicatie en empirie: 8,5

*Goed.*
- De admonition heeft bron, wat, data, verschil en verwachte afwijking in ongeveer 225 woorden
  (781–805).
- Replicatie (1) heeft een tabel GKX tegen hier (932–937) en een oordeel dat begint met
  "Geslaagd" en past bij de verwachting van "tienden van een procentpunt" (939–942).
- De vergelijking met het historische gemiddelde (1,32 tegen 0,78) is een eerlijke en
  leerzame uitkomst (944–946).

*Aanmerkingen.*
- Replicatie (1) (949–950): "Na 2005 liggen alle getallen lager, ook de Sharpe-ratio van alle
  signalen gelijkgewogen, wat past bij het publicatieverval". Niet alle: de $R^2$ tegen het
  historische gemiddelde stijgt voor OLS, ridge en LASSO.
- Replicatie (2) (1013–1028): "In Sharpe-ratio's blijft de ongekrompen portefeuille wel voorop,
  met 13,5 tegen 4,3 in de schattingsperiode en 2,32 tegen 2,07 daarna, ..." Getallenbrij in
  lopende tekst; geen tabel origineel/hier voor (2).
- Replicatie (1) (942): "De $R^2$ ligt hier veel hoger dan bij GKX, omdat de signalen gemiddeld
  een positieve premie hebben." Half verklaard; de diversificatie van portefeuilles (veel minder
  idiosyncratische ruis dan losse aandelen) is de tweede reden.

*Beter uitleggen.* Het oordeel "Geslaagd" bij (2) (1100) noemt de verwachte uitkomst, maar niet
wat KNS zelf rapporteerden; een regel in een tabel maakt het oordeel toetsbaar.

*Voor een 9.* 06_35_machine_learning.md:949 corrigeren; :1013–1028 en :1100–1105 terugbrengen
tot drie getallen per alinea en de rest in een tabel origineel/hier.

### 7. Oefeningen: 9,0

*Goed.*
- Oefening 1 is een instap op het toy, oefening 3 een afleiding met Monte Carlo die de
  getallen van :300 inlost, en oefening 4 een uitbreiding van de simulatie.
- Elke uitwerking eindigt met een les (1166, 1221, 1253, 1280).

*Aanmerkingen.*
- Oefening 4 (1259): "Hoe verhouden de $R^2$ van OLS, van ridge en van de populatie zich in
  drie replicaties, vergeleken met de $-3{,}46\%$ van GKX?" De uitwerking vergelijkt niet met
  −3,46%, en in twee van drie replicaties stort OLS niet in.

*Beter uitleggen.* Geen oefening breidt de replicatie op echte data uit (bijvoorbeeld de
Sharpe-ratio per subperiode of een ander kwantiel); dat is geen vereiste voor een 9.

## Feitelijke fouten

Nagerekend tegen `$TEMP/F6-06_35_machine_learning-out.txt` en met de hand.

1. **:499** "LASSO schaalt en selecteert". Onjuist: volgens [](#eq-machine-learning-soft) trekt
   LASSO $\lambda_1$ van $|z_j|$ af (verschuiven), alleen ridge schaalt. Het college zegt het
   zelf goed op :194 en :293–294. Mogelijk een vakterm die in de redactie is verschoven.
2. **:949** "Na 2005 liggen alle getallen lager". De $R^2$ t.o.v. het historische gemiddelde
   stijgt na 2005: OLS 0,712 → 0,854, ridge 0,712 → 0,867, LASSO 0,714 → 0,978. Klopt wel voor
   de $R^2$ van GKX, de long-short Sharpe-ratio's en de gelijkgewogen Sharpe (2,40 → 1,55).
3. **:668** "Oefening 4 laat OLS instorten zodra $P/n_{\text{eff}}$ groeit." In de uitvoer van
   oefening 4 alleen in replicatie 0 (−16,26%); replicaties 1 en 2 geven 0,52% en 0,11%.
4. **:521–522** "evenredig met ... in de niet-lineaire met $(c_1^2 - \tfrac13) + c_1c_2 +
   \operatorname{sign}(c_3x_t)$". De code schaalt de termen verschillend (deling door
   $\sqrt{4/45}$, factor 3 op $c_1c_2$); de som zelf is niet evenredig met $g^\star$.
5. **:170** (codecommentaar) "sklearn scales the squared loss by 1/(2n)" geldt niet voor
   `Ridge`, dat de kwadratensom ongeschaald gebruikt; de getallen kloppen wel.
6. **:767** "in 55% van de economieën": de uitvoer geeft 0,54, 0,55 en 0,55. Verwaarloosbaar;
   "rond 55%" is exact.
7. **:663** "hooguit een half procent": het maximum is 0,54 (LASSO en elastic net, replicatie
   1). Verwaarloosbaar.

Nagerekend en juist: toy (alle stappen, residuen, 88%, boom −2,5 en 1,67; elastic-net-schaling
$\alpha = 3$, l1-ratio 1/3 geeft $\lambda_1 = 5$, $\lambda_2 = 10$); break-even 0,5% en 184.000;
NN3 ruim 30.000 parameters (30.145 bij 920 invoeren); 50/60 ≈ 0,83 procentpunt; GKX-tabel;
bewijs van de KNS-propositie en $\E[SR_j^2] = \kappa^2\lambda_j/\tau$; Martin-Nagel-breuk,
1/51 en 1/2,25; simulatie 1 (half procentpunt, 0,6, 1,1, 3,3–3,7, 1,4–5,0, 54.000); simulatie
2 (15%, 1,5 procentpunt, −1,8 → −50, −19, 700 economieën); replicatie 1 (134.518, januari 1990
tot november 2024, 2,00, 2,36, 0,78, 0,17, 1,32, DM-$t$ 0,71 en 0,67); replicatie 2 (0,133,
39%, 40%, −170 en $\sqrt{171} \approx 13{,}1$, 13,5, 4,3, 2,32, 2,07, 0,24, 0,25; 0,26, 0,40,
0,04, 1,72, 0,78); oefeningen 1–4 (alle getallen).

## Navertelling in vijf zinnen

Met honderden voorspellers en een zwak signaal overheerst de schattingsvariantie, zodat gewone
regressie buiten de steekproef slechter doet dan nul voorspellen. Krimp (ridge, LASSO, elastic
net, ook early stopping en middeling) ruilt een kleine vertekening in voor veel minder variantie,
en bomen en netwerken voegen alleen iets toe als de wereld echte interacties bevat. KNS
schatten de SDF als ridge op prijsfouten met een prior die premies aan variantie koppelt, zodat
een paar hoofdcomponenten de cross-sectie beter verklaren dan een paar signalen. Martin en Nagel
laten zien dat lerende beleggers voorspelbaarheid in de steekproef opleveren zonder winstkans
erbuiten. Op 212 signaalportefeuilles winnen bomen nauwelijks en alleen vóór 2005, en voegt
timing weinig toe aan het dragen van de gemiddelde anomaliepremie. Dit sluit aan bij het
Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijk laten lopen: de zinnen zijn verbonden, het betoog
leest hardop als een college, en de regeltaal is grotendeels weg. Er blijven twee zinnen over
het werk (602, 804) en één vakterm die mogelijk is verschoven (499, "LASSO schaalt").

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. :321–322 "Bij $\rho = 0{,}5$ blijft dus hoe veel bomen ook minstens de helft van de variantie
   over." Herschrijving: "Bij $\rho = 0{,}5$ blijft dus minstens de helft van de variantie over,
   hoeveel bomen er ook zijn."
2. :254–255 "Het vergaat de analist met tweehonderd kenmerken uit de intuïtie dus precies zo, en
   krimp is het antwoord." Herschrijving: "Zo vergaat het ook de analist met tweehonderd
   karakteristieken, en krimp is het antwoord."
3. :602–603 "De derde lineaire replicatie staat in een eigen cel, zodat geen cel langer dan een
   minuut duurt." Herschrijving: "Met een derde replicatie erbij geeft de tabel per replicatie
   de populatie-$R^2$ en die van elke methode, in procenten." (en de rest van de alinea laten
   vervallen)

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Gelezen: het college volledig, de hunks van F6b, en de celuitvoer (`$TEMP/F6c-06_35_machine_learning-out.txt`).

**Getallencontrole.** Alle toegevoegde of gewijzigde getallen zijn herleidbaar. $\kappa = 0{,}133$ geeft $0{,}133\sqrt{12} = 0{,}46$ per jaar en $\sum_j \kappa^2\lambda_j/\tau = \kappa^2$ klopt. De cs-$R^2$ is 0,388 in de schattingsperiode en 0,403 erna ("evenveel"). Vier PC's 0,262 tegen 0,403 (bijna twee derde), vier signalen 0,039 (een tiende). Sharpe 2,319 / 2,065 en 1,727 / 0,780 (ruim twee keer). $\sqrt{171} = 13{,}1$ en $-170{,}4$. OLS en ridge liggen in de eerste simulatie binnen 0,03 procentpunt (honderdsten). De 60%-uitleg bij 0,4 en $\sigma^2/\beta^2 = 0{,}10^2/0{,}02^2 = 25$ kloppen. Geen niet-herleidbaar getal. De KNS-kolom in de nieuwe tabel is kwalitatief en bevat geen getal.

**Feitelijke fouten (7):** :499 opgelost (schuift een vast bedrag); :949 opgelost (R^2 GKX en Sharpe dalen, alleen R^2 tegen het historisch gemiddelde stijgt, met reden); :668 opgelost ("in één van drie replicaties"); :521 opgelost (geschaald op eenheidsvariantie); :170 opgelost (commentaar noemt Ridge apart); :767 en :663 opgelost ("rond").

**Drie verbeteringen.** (1) Replicatie (2): tabel KNS/hier toegevoegd, getallen uit de proza, alinea's hebben hoogstens drie getallen, oordeel "Geslaagd" toetsbaar; opgelost. (2) Helderheid: $\kappa$ geduid (maximale Sharpe per periode, 0,46 per jaar), "karakteristieken" gelijkgetrokken, LASSO-term hersteld; opgelost. (3) Taal/code: :602, :804, :321, :254, :57 herschreven, zin tussen de niet-lineaire cellen, augmentatie met `X_aug`/`y_aug` uitgelegd; opgelost.

**Aanmerkingen en Beter uitleggen.** Opgelost: :667 (OLS en ridge gelijk, krimp-slaat-OLS niet getoond), H11 ($\sigma^2/\beta^2 = 25$), 88% geduid, boom als bouwblok, tweede reden bij :942, 60%-maat van KNS. Niet opgelost maar terecht afgewezen: een IPCA-getal (geen bron of cel, kaart §6) en een oefening op echte data (geen vereiste). Deels: de zin over de maatstaf van KNS krijgt zijn orde van grootte, maar een vergelijkbaar getal voor IPCA ontbreekt nog; dat blijft een kleine onvolledigheid, geen fout.

**Hardop-toets.** De drie zinnen (:321, :254, :602) zijn opgelost en klinken natuurlijk. Resterend: de bron heeft enkele harde regelafbrekingen midden in een zin (bijvoorbeeld :57-58, :73-75, :1147); in de weergave onzichtbaar, geen taalpunt. Niets verslechterd.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 | 9,2 |
| 2 | Opbouw en rode draad | 20% | 9,0 | 9,1 |
| 3 | Taal | 20% | 8,5 | 8,9 |
| 4 | Toy-voorbeeld | 10% | 9,0 | 9,0 |
| 5 | Code en figuren | 10% | 8,5 | 8,9 |
| 6 | Replicatie en empirie | 10% | 8,5 | 9,0 |
| 7 | Oefeningen | 5% | 9,0 | 9,0 |
| | **Gewogen eindcijfer** | | 8,7 | **9,0** (9,04) |

Geen deelcijfer onder 8,5, taal boven 8, eindcijfer onder de grens van 9,1 van de beoordelaar.
