STATUS 03_14_roll F6c words=5708 prose=PASS open=1 cijfer=9,0 min=9

# Ronde 9+

Vorige ronde: 8,9

Eindbeoordeling (F6) van `lectures/03_14_roll.md` na de taalredactie (fase T). Gewichten van
ronde 9+: helderheid 25, opbouw 20, taal 20, toy 10, code en figuren 10, replicatie 10,
oefeningen 5. Bij twijfel het lagere cijfer. Cijfers nagerekend tegen
`tools/nb_outputs.py` (celuitvoer) en met de hand.

## De drie verbeteringen met het meeste effect

1. **Taal (8,5 → 9).** De zinnen die de hardop-toets niet halen herschrijven: de
   motiefnaam als handelend onderwerp op r. 638 ("Hier keert de standaardfout van 2% om"),
   de stijve formule "In de termen van theorie of feit" (r. 60 en r. 1119), "De
   steekproefkolommen overstemmen dat verschil" (r. 754), de oneigenlijke "zodat" op r. 696,
   de dubbele betrekkelijke bijzin met vooruitblik in de verleden tijd op r. 28–29, en de
   titel "critique" tegenover "kritiek" (r. 16, r. 55). Plus "scalars" (r. 135). De term
   "rand" tegenover STYLE §3 "grens" boekbreed beslissen (zie Taal).
2. **Opbouw (8,5 → 9).** Het $R^2$-deel aan dezelfde getallen hangen als de rest: bij
   [](#eq-roll-decompositie) één uitgerekend getal uit de wereld van honderd activa
   (bèta 1, $\sigma_m \approx 4{,}7\%$, $\sigma_\varepsilon \approx 10\%$ per maand geeft
   $R^2 \approx 0{,}0022/(0{,}0022 + 0{,}01) \approx 0{,}18$), en de terugverwijzing op
   r. 589–590 laten kloppen met wat de Intuïtie werkelijk voorspelde.
3. **Helderheid (9 blijft 9, maar wordt robuust).** De afspraak dat "efficiënt" hier ook de
   onderste tak van de minimum-variantierand omvat, al in het Overzicht of bij r. 71 laten
   staan, en de overclaim "vlak voor elke waarneembare proxy" (r. 1121) inperken tot de
   gangbare indices.

## Eindcijfer: 8,8

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,25 + 1,70 + 1,70 + 0,90 + 0,90 + 0,90 + 0,45 = 8,80, dus **8,8**, laagste
deelcijfer 8,5. Lengte 5.566 woorden volgens `prose_stats` (PASS, zinsgemiddelde 15,6,
dubbele punt 4,7 per 1000). Het verschil met 8,9 komt door de nieuwe weging (taal 20%) en
het strengere hardop-oordeel, niet door achteruitgang: de redactie heeft het college beter
gemaakt.

## 1. Helderheid van de uitleg: 9

*Goed*
- Toy-voorbeeld en Theorie: de lijn tegenover de randportefeuille wordt met getallen
  voorgerekend (λ = 0,368, μ_z = 3,39%, helling 6,61%) en in de stelling en het bewijs
  teruggenoemd (r. 296).
- Bijna-efficiënte proxy's: het lemma krijgt meteen een getal (correlatie 0,9 geeft 90% van
  de Sharpe-ratio, r. 412), en $\rho^{*}$ krijgt een richting en een reden (r. 481–484).
- Opzet: de minimum-variantierand wordt gedefinieerd, en de afspraak dat ook de onderste
  tak "efficiënt" heet, staat er expliciet (r. 256–262). De stelling zelf noemt de
  minimum-variantierand, dus geen stelling wordt door de termkeuze onjuist.

*Aanmerkingen*
- Overzicht, r. 38–40: "Een lineaire relatie tussen verwacht rendement en bèta is
  wiskundig hetzelfde als efficiëntie van de portefeuille waartegen de bèta's gemeten
  zijn." Met de gewone betekenis van efficiënt (bovenste tak) is dat te sterk: ook een
  portefeuille op de onderste tak geeft een exacte lijn, met negatieve helling. De afspraak
  die dit rechtzet, komt pas op r. 261.
- Intuïtie, r. 71: "Neem een portefeuille op de efficiënte rand." Derde naam naast
  "minimum-variantierand" en "de rand", vóór de definitie (H7).
- Numerieke uitwerking, r. 589–590: "De intuïtie voorspelde de eerste stijging en de
  nulhelling bij hoge correlatie." De Intuïtie (r. 92–106) voorspelt geen stijging; die
  staat pas op r. 421–422. En 0,62 is geen hoge correlatie.
- Wat er brak, r. 1120–1121: "Er blijft een feit over dat op een verklaring wacht, namelijk
  dat de lijn vlak is voor elke waarneembare proxy." De in-sample tangentportefeuille is
  waarneembaar en geeft een steile lijn; buiten de steekproef is de helling 0,98.

*Beter uitleggen*
- Wat "efficiënt" in dit college betekent, moet de lezer weten vóór de eerste bewering
  erover; één bijzin in het Overzicht volstaat.
- Bij "bijna-efficiënt" (r. 381, 416) wordt "bijna" gemeten in correlatie; de getallen 0,62
  (model) en 0,885 (data) laten zien dat "bijna" hier ruim is. Eén zin die dat benoemt
  voorkomt dat de lezer "sterk gecorreleerd" (r. 46, 95) als 0,95 leest.

## 2. Opbouw en rode draad: 8,5

*Goed*
- Overzicht stelt de vraag en geeft het antwoord in de eerste twee zinnen (r. 37–41).
- Het toy keert terug in Theorie (r. 253, 296), in de Simulatie (r. 801–802) en in
  oefening 1 ($\rho^{*} = 0{,}785$), en de wereld van honderd activa verbindt Theorie en
  Simulatie.
- Routekaart aan het begin van Theorie (r. 229–235) en Samengevat aan het eind.

*Aanmerkingen*
- De tweede vraag, r. 594: "Als de lijn niet te toetsen is, wat verklaren markt en
  industrie dan wel?" De koppeling staat er, maar het $R^2$-deel heeft geen enkel getal uit
  toy of modelwereld; het staat als tweede college in het college.
- Intuïtie, r. 103: "We verwachten dus drie dingen." Identiek aan 03_10 (ME:100)
  [onderzoek E].
- Numerieke uitwerking, r. 589–590 (zie Helderheid): de terugverwijzing naar de intuïtie
  klopt niet met de Intuïtie-sectie.

*Beter uitleggen*
- De lezer ziet niet dat de wereld van honderd activa zelf al een $R^2$ voor losse activa
  heeft; die ene berekening maakt van Rolls tweede vraag een voortzetting in plaats van
  een aanhangsel.

*Voor een 9*
- lectures/03_14_roll.md:616–620: bij [](#eq-roll-decompositie) het getal uit de
  modelwereld (bèta 1, $\sigma_m \approx 4{,}7\%$, $\sigma_\varepsilon$ 8–12% per maand,
  dus $R^2$ tussen ongeveer 0,13 en 0,26), zodat de lezer Rolls 0,20–0,35 herkent.
- lectures/03_14_roll.md:589–590: de zin laten verwijzen naar de redenering op r. 421–422
  en "hoge" vervangen door het getal.
- lectures/03_14_roll.md:103: de aankondiging "We verwachten dus drie dingen" anders
  formuleren dan in 03_10 [onderzoek E].

## 3. Taal: 8,5

*Goed*
- De redactie heeft de regeltaal weggehaald ("De imports-cel", "de steekproefvraag", "zoals
  de verwachte afwijking eiste") en "haar/diens" voor zaken vervangen; zinsgemiddelde 15,6
  met afwisseling, geen gedachtestreepjes, "In woorden" en "Waarom zou dit waar zijn" elk
  twee keer.
- "Overrendement" staat nu overal in de lopende tekst (STYLE §3); verbanden lopen via
  want, zodat en terwijl.
- Wat er brak leest als gesproken tekst ("Roll maakte niet het CAPM kapot, maar een manier
  van lezen").

*Aanmerkingen*
- Theorie, r. 638: "Hier keert [de standaardfout van 2%](#00-01-rendementen) om." Motief als
  handelend onderwerp (STYLE §11.12) [onderzoek E].
- Overzicht, r. 59–61, en Wat er brak, r. 1119: "In de termen van theorie of feit was het
  CAPM een theorie met toetsen" en "In de termen van theorie of feit is het CAPM geen
  getoetste theorie meer". Twee keer dezelfde stijve formule [onderzoek E].
- Simulatie, r. 754: "De steekproefkolommen overstemmen dat verschil." Kolommen overstemmen
  niets [onderzoek E].
- Simulatie, r. 696: "De nulhelling bij 0,62 valt buiten dit bereik, zodat de schade hier in
  het intercept zit." "zodat" suggereert een oorzaak die er niet is.
- Waar we zijn, r. 28–29: "Het bezwaar dat de markt niet waarneembaar is, dat in de
  APT-discussie terugkwam, begint hier." Twee betrekkelijke bijzinnen, en een verleden tijd
  voor iets dat later komt [onderzoek E].
- Titel, r. 16: "Roll: de critique en de R²" tegenover "kritiek" op r. 55; Toy, r. 135: "de
  vier scalars" [onderzoek E].
- Replicatie, r. 1100: "Die omkering hadden we vooraf al onzeker genoemd." Een omkering
  noem je niet onzeker.
- Termen, r. 44, 71, 135–142, 256 en verder: "minimum-variantierand", "efficiënte rand",
  "randportefeuille", "op de rand". STYLE §3 schrijft "grens" voor [onderzoek E].

*Beter uitleggen*
- Het oordeel over "rand". De redacteur liet "rand" staan omdat 01_04 en 02_08 het ook
  gebruiken. Dat klopt half: 01_04 zegt "efficiënte rand" (en bedoelt daarmee de hele
  parabool, 01_04:97), maar 02_08:43 zegt "de efficiënte grens van Markowitz (hierna
  kortweg de rand)" en gebruikt daarna "minimum-variantierand". Inhoudelijk is dit college
  consistent: de minimum-variantierand is hier nergens een alias voor de efficiënte grens,
  en de stelling noemt de minimum-variantierand. Het lokaal omzetten naar "grens" zou alleen
  een nieuw verschil met 01_04 maken; de omzetting (minimum-variantiegrens, efficiënte grens
  voor de bovenste tak) hoort boekbreed te gebeuren, in 01_04, 02_08 en 03_14 tegelijk.
  Daarbij moet 02_08:43 de alias "hierna kortweg de rand" kwijt, want daar wordt de
  efficiënte grens wel gelijkgesteld aan de rand die later de minimum-variantierand is.

*Voor een 9*
- lectures/03_14_roll.md:638: herschrijven zonder de motiefnaam als onderwerp [onderzoek E].
- lectures/03_14_roll.md:59–61 en 1119: één keer de motiefnaam, de andere keer zeggen wat
  het betekent [onderzoek E].
- lectures/03_14_roll.md:754, 696, 28–29, 1100: de zinnen uit de hardop-toets hieronder.
- lectures/03_14_roll.md:16 en 135: "kritiek" en "getallen" [onderzoek E].
- Boekbreed (01_04, 02_08, 03_14): "rand" → "grens" volgens STYLE §3, in één ronde.

## 4. Toy-voorbeeld: 9

*Goed*
- Vijf stappen met de hand, elk met een uitkomst; de tabel "met de hand / code" is
  identiek (λ 0,368, δ −0,0125, bèta's 1,6053 en 0,0921, $R^2$ 0,9868).
- De slotzin zegt wat het getal betekent: een $R^2$ van 0,9868 zegt niet hoe ver de proxy
  van de rand ligt (r. 222–225).
- Oefening 1 zet het toy voort met een risicovrije rente en hergebruikt de afwijkingen uit
  stap 5 (r. 1161).

*Aanmerkingen*
- Toy, r. 135: "Uit [](#01-04-markowitz) kennen we de vier scalars die de rand vastleggen".
  Vier geleende getallen plus twee geleende formules (r. 148–150); met de hand is het net
  geen vijf minuten.

*Beter uitleggen*
- Geen inhoudelijk gat; de lezer die A, B, C wil narekenen heeft de blokinverse nodig, die
  in 01_04 staat.

## 5. Code en figuren: 9

*Goed*
- Elke cel heeft een zin ervoor en erna; `tilt_to_corr` legt de kwadratische vergelijking
  in commentaar uit en kiest de wortel met benoemde maskers.
- Vóór elke figuur staat waarop te letten (r. 554–555, 766–767, 895–896, 1042), erna wat te
  zien is.
- `sml_fit`, `population_sml` en `adjusted_r2` lezen als de wiskunde; de simulatielus is
  zichtbaar.

*Aanmerkingen*
- Tabel- en figuurlabels, r. 854, 876, 911–912, 1088: "in-sample tangentportefeuille",
  "gemiddeld excess rendement (% per maand)", "R2", en in de figuurtitel "R² = 1.000" met
  decimale punt. Tabellen en figuurteksten zijn Nederlands (STYLE §3: "in de steekproef",
  "overrendement") [onderzoek E].

*Beter uitleggen*
- De labels zijn het enige wat de lezer van de code ziet in de tabellen; ze zouden dezelfde
  termen moeten dragen als de proza eromheen.

## 6. Replicatie en empirie: 9

*Goed*
- Admonition met bron, wat, data, verschil en verwachte afwijking, binnen 250 woorden; de
  onzekere rangorde van dag en maand staat vooraf genoemd (r. 829–831).
- Tabel origineel/hier (cel 17), en een oordeel dat begint met "Geslaagd … gedeeltelijk
  geslaagd" en aan de verwachting gekoppeld is (r. 1094–1105).
- De getallen staan in tabellen; de proza verwijst naar rijen en kolommen.

*Aanmerkingen*
- Replicatie, r. 893: "De laatste rij is de vlakke lijn van [](#02-08-capm)." De helling is
  −0,37% per maand; "vlak" onderschat het (klein punt).

*Beter uitleggen*
- Waarom de gelijkgewogen portefeuille een helling van 0,05 heeft terwijl de CRSP-index
  negatief is, blijft onbesproken; één bijzin volstaat.

## 7. Oefeningen: 9

*Goed*
- Instap (toy met risicovrije rente), afleiding ($R^2$ en $\sigma_m$) en uitbreiding van de
  replicatie (tautologie buiten de steekproef): precies de drie soorten.
- Elke uitwerking eindigt met wat ze leert; oefening 3 laat zien dat de perfecte lijn een
  eigenschap van de steekproef is (0,37 buiten tegen 1 binnen).

*Aanmerkingen*
- Oefening 3, r. 1298: "Dat wijst op een blijvende richting van small en value". "Small en
  value" zonder uitleg en "richting" is vaag [onderzoek E].

*Beter uitleggen*
- Welke "richting" bedoeld is (overwegen van kleine en goedkope aandelen) in één
  woordgroep noemen.

## Feitelijke fouten

Nagerekend tegen de celuitvoer en met de hand. Correct: het toy (A, B, C, D; λ = 0,368,
δ = −0,01248; covarianties en bèta's; μ_z = 3,39%, 14,00% en 4,00%; gelijkgewogen 9,33%,
rijgemiddelden, variantie 0,02, bèta's, helling 8,33/1,389 = 6,0%, intercept 3,33%,
residuen, $R^2$ = 0,9868); de bewijzen van stelling, lemma, propositie en gevolg; de
kwadratische vergelijking in `tilt_to_corr`; de modelwereld (0,66%, 4,69%, 0,49, 0,62; 1,7
bij 0,75; nul bij 0,62); de simulatie (0,08% en −0,34%; 12 × 0,338 ≈ 4,1%; band 0,22–1,0;
4,69/√600 = 0,19; sd 0,14–0,20; mediaan 0,05 → −0,11 en 0,14; −0,11 binnen één sd); de
replicatie (1963-07 t/m 2026-07; correlatie 0,885 = 1,233/1,393; $R^2$ CRSP 0,08;
portefeuille-$R^2$ boven 0,5; 0,349 en 0,411; 35–40%); oefening 1 (tangent
(1/3, 2/9, 4/9); **d** en Σ**d**; c* = 4,718; ρ* = 0,785; w*; intercept 0,07333); oefening 2
(0,15 in 2017 tot 0,56 in 2020; volgorde 2020, 2011, 2022, 2008; 24–40%; 0,82); oefening 3
(0,37; 0,74; 0,98; 2,55; 0,11; 0,88 tegen 0,62). Labels [](#eq-markowitz-probleem),
[](#eq-markowitz-foc), [](#eq-markowitz-abcd), `prop-capm-beta`, `thm-capm-zerobeta`
bestaan. De termkeuze "rand" maakt geen stelling onjuist.

| nr | regel | bewering | oordeel | correctie |
|---|---|---|---|---|
| 1 | 1120–1121 | "dat de lijn vlak is voor elke waarneembare proxy" | onjuist als algemene bewering: de in-sample tangentportefeuille geeft helling 2,34, de vaste tangentportefeuille buiten de steekproef 0,98 | "voor elke gangbare marktindex" |

Onnauwkeurig, geen fout: r. 589–590 ("nulhelling bij hoge correlatie", terwijl het 0,62 is)
en r. 38–40 (lijn ≡ efficiëntie vóór de afspraak op r. 261).

## Navertelling in vijf zinnen

1. Een exacte lijn tussen verwacht rendement en bèta bestaat dan en slechts dan als de
   portefeuille waartegen de bèta's gemeten zijn op de minimum-variantierand ligt, en dat
   geldt ook met steekproefmomenten.
2. Daarom toetst een CAPM-toets alleen of de gekozen index efficiënt is, en omdat de ware
   markt onwaarneembaar is, is elke verwerping een gezamenlijke hypothese.
3. Een proxy die minder belegt in activa met een hoge premie kan, met een nog behoorlijke
   correlatie met de markt (0,62 in de modelwereld, 0,885 in de data), een helling van nul
   geven, en met vijftig jaar data ziet de onderzoeker dat niet.
4. Op de 25 size/BM-portefeuilles geeft de achteraf efficiënte portefeuille een perfecte
   lijn en de CRSP-index bijna geen, zonder dat de data zeggen waarom.
5. Markt en industrie verklaren maar zo'n 35–40% van de variantie van losse aandelen, een
   getal dat anders dan gemiddelde rendementen scherp gemeten is.

Dat komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk natuurlijker gemaakt: geen regeltaal meer, geen
lijm-dubbelepunten, verbanden met voegwoorden. Wat overblijft zijn een handvol zinnen die
je zo niet tegen een collega zegt.

- r. 638: "Hier keert de standaardfout van 2% om." → "Bij varianties ligt het andersom dan
  bij [de standaardfout van 2%](#00-01-rendementen), want gemiddelde rendementen zijn slecht
  gemeten en varianties goed."
- r. 754: "De steekproefkolommen overstemmen dat verschil." → "In de geschatte waarden
  verdwijnt dat verschil in de ruis."
- r. 696: "De nulhelling bij 0,62 valt buiten dit bereik, zodat de schade hier in het
  intercept zit." → "De nulhelling ligt pas bij 0,62, dus in dit bereik zit de schade niet
  in de helling maar in het intercept."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Nagerekend tegen `tools/nb_outputs.py` (uitvoer in `$TEMP/F6c-03_14_roll-out.txt`) en met
de hand, tegen R9-1 in het rapport.

**Feitelijke fout.** r. 1120–1121 "vlak voor elke waarneembare proxy" → "vlak voor elke
gangbare marktindex": *opgelost* (nu r. 1132).

**Drie verbeteringen.**
1. Taal: *opgelost*, op "rand" → "grens" na (zie Taal hieronder).
2. Opbouw: *opgelost*. Bij [](#eq-roll-decompositie) staat nu
   "$0{,}0469^2/(0{,}0469^2+\sigma_\varepsilon^2)$, dus tussen 0,13 en 0,26" (r. 624–627).
   Nagerekend: $0{,}0469^2/(0{,}0469^2+0{,}08^2) = 0{,}256 \to 0{,}26$ en
   $0{,}0469^2/(0{,}0469^2+0{,}12^2) = 0{,}133 \to 0{,}13$, klopt. 4,69% staat in de
   celuitvoer (marktvolatiliteit 4,6931), 8–12% staat al in de Opzet: herleidbaar, geen
   nieuwe feitelijke claim.
3. Helderheid: *opgelost*. Overzicht geeft de afspraak (r. 40) vóór het eerste gebruik
   van "efficiënt"; Opzet verwijst terug (r. 262–264); Intuïtie r. 72 zegt nu
   "minimum-variantierand" i.p.v. "efficiënte rand".

**Voor een 9.**
- Opbouw (3/3 *opgelost*): $R^2$-getal (zie boven); terugverwijzing r. 589–590 verwijst nu
  naar de redenering bij de bijna-efficiënte proxy's ("eerst krimpt de spreiding van de
  bèta's, daarna verdwijnt de covariantie met de premies") zonder "hoge correlatie" als
  kwalificatie van 0,62 — de ene overblijvende "hoge correlatie" (r. 235) is een algemene
  zin in de Theorie-inleiding, geen herhaling van de fout; "We verwachten dus drie dingen"
  → "Uit dit alles volgen drie verwachtingen" (r. 105).
- Taal (4/5 *opgelost*): r. 646 motief niet meer als onderwerp; "theorie of feit" één keer
  bij naam (Wat er brak, r. 1130), in Overzicht omschreven zonder de term (r. 60–61);
  r. 754/696/28–29/1100 herschreven zoals in "Taal na de redactie" voorgesteld; titel
  "kritiek" (r. 16), "getallen" (r. 137). *Niet opgelost*: "rand" → "grens" boekbreed
  (r. 44, 71, 256 e.v.) — expliciet uitgesteld naar een boekbrede ronde (01_04, 02_08,
  03_14 tegelijk) op aanwijzing van de orkestrator, in lijn met de eigen aanbeveling
  hierboven dat lokaal omzetten een nieuw verschil met 01_04 zou maken. Geen taalgebrek
  van dit college; blokkeert het deelcijfer niet.

**Aanmerkingen en Beter uitleggen (overig), alle *opgelost*.**
- Helderheid: Overzicht r. 38–41 met de afspraak direct erna; "bijna-efficiënt" ruim
  genoemd bij $\rho^{*}=0{,}62$ (r. 533); "sterk gecorreleerd" → "duidelijk" (r. 47).
- Code en figuren: labels in het Nederlands ("tangentportefeuille in de steekproef",
  "gemiddeld overrendement (% per maand)", "R²"); decimale komma in de figuurtitel via
  `.replace(".", ",")` (r. 922).
- Replicatie: r. 893 "vlak" → "te vlakke, hier zelfs licht dalende lijn" (r. 904); bijzin
  over de gelijkgewogen portefeuille (r. 902–903).
- Oefeningen: oefening 3 "richting van small en value" → "het overwegen van kleine en
  goedkope aandelen (small en value)" (r. 1310–1311).
- Toy: geen wijziging nodig, terecht (geen inhoudelijk gat); "scalars" via Taal opgelost.

**Hardop-toets.** De drie herschreven zinnen (r. 646, r. 763, r. 705) staan letterlijk
zoals voorgesteld in "Taal na de redactie" en lezen nu als gesproken tekst.

**Getallencontrole.** Tegen `nb_outputs.py`: marktvolatiliteit 4,6931 (r. 532, 626),
$\rho^{*}$/correlatie bij nulhelling 0,6225/0,623 (r. 533, 590), R² tangent 1,000
(r. 1106), R² aandelen maand 0,349→0,35 en dag 0,411→0,41 (r. 1107–1108); oefening 3: R²
0,367→0,37, intercept 0,743→0,74, helling 0,976→0,98, gemiddeld overrendement
2,547→2,55, Sharpe 0,878→0,88 (r. 1302–1309); oefening 2: R² 2017 0,152→0,15, 2020
0,564→0,56, correlatie 0,815→0,82, volatiliteitsband 24,2–40,0 → "24 tot 40%"
(r. 1255–1258). Alles klopt. Het getal 0,13–0,26 is een handberekening uit twee al
bevestigde grootheden (cel + Opzet), geen niet-herleidbaar getal.

Geen verslechtering, geen nieuwe feitelijke fout gevonden.

## Deelcijfers na Controle 1

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,00, dus **eindcijfer 9,0**,
laagste deelcijfer 9. Het enige nog open punt ("rand" → "grens") is boekbreed en
blokkeert dit deelcijfer niet.
