STATUS 06_34_factor_zoo F6c words=5998 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,9 -> F6c 9,0.
# Eindbeoordeling 06_34_factor_zoo

## Eerste herziening (workflow §12)

Eerste herziening. Er is geen vorig cijfer. Gelezen: kaart-rollen, rubriek, STYLE §11.12,
het college (.md, eenmaal volledig), notes/taal-06_34, de celuitvoer via `tools/nb_outputs.py`
(18 cellen). `prose_stats --check`: PASS (5.887 woorden, zinnen gemiddeld 17, p90 27, één zin
> 40, alinea gemiddeld 53, para_one 8, motiefnamen 0). `open` telt de vier feitelijke punten
hieronder.

Alle getallen in de lopende tekst zijn tegen de celuitvoer nagerekend en kloppen, op de
punten onder "Feitelijke fouten" na. De vaktermen zijn na de taalredactie niet van betekenis
veranderd: FWER/FDR, "tussenperiode", "krimpfactor", "inverse Mills-ratio" en "shrinkage"
worden overal in dezelfde betekenis gebruikt, en de stellingen (Holm, BHY, afknotting,
normale shrinkage, selectie-corollarium, q-propositie) zijn inhoudelijk juist.

## De drie verbeteringen met het meeste effect

1. **Toy: de drempels niet als vier onafgeleide formules invoeren, en het toy laten
   terugkeren** (→ toy 9,1, opbouw 9,2). Het toy (r. 118–150) gebruikt vóór de Theorie de
   grenzen van Bonferroni, Holm, BH en BHY, vier formules die pas in Theorie worden afgeleid;
   de rubriek staat er één toe. Laat de tabel steunen op de twee ideeën "één vergissing" en
   "aandeel vergissingen" en zeg bij elke kolom in één bijzin wat de grens beschermt. Laat
   de vier nulsignalen B–E daarna in Theorie terugkeren bij de afknotting (r. 368–376):
   hun gemiddelde $t$ van 2,54 naast de $\lambda(2) = 2{,}37$ van de formule, zodat het toy
   ook de tweede helft van de vraag (verzwakking) raakt (H11).
2. **Helderheid: symbolen en één stap in de q-propositie** (→ helderheid 9,1). $\Phi$ staat
   op r. 118 en $\varphi$ op r. 342 zonder naam; "de alpha ten opzichte van een model zonder
   premie" (r. 233) is een omweg voor "het gemiddelde rendement"; in r. 578–579 verklaart
   "omdat een onderneming met lage kapitaalkosten veel investeert" alleen de helft van de
   bewering; en "signaal" en "voorspeller" wisselen elkaar af tot in de Oordeel-tabel (H7).
3. **Code en figuren: leeswijzer vóór beide figuren** (→ code en figuren 9,1). "De figuur
   zet beide uitkomsten naast elkaar." (r. 697) en "De figuur toont beide verdelingen en het
   rendement per signaal." (r. 889) zeggen niet waarop te letten. Noem vooraf het ene ding:
   links of de histogram de afgeknotte kromme volgt, rechts waar 26% en 58% de kromme
   snijden; bij de tweede figuur de helling onder één.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,9

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,8 |
| 4 | Toy-voorbeeld | 10% | 8,7 |
| 5 | Code en figuren | 10% | 8,8 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,1 |
| | **Eindcijfer (gewogen)** | | **8,9** (8,865) |

Geen deelcijfer onder 8,5; taal ≥ 8, dus niet geblokkeerd. Het eindcijfer haalt de 9,0 niet.

### 1. Helderheid (8,8)

*Goed.*
- Opzet en notatie: $\delta_i$ krijgt meteen een getal ("Een premie van 0,5% per maand met
  een standaardfout van 0,2% heeft bijvoorbeeld $\delta_i = 2{,}5$").
- Publicatieselectie: bij de formule staan de getallen $\varphi(2) = 0{,}0540$,
  $1 - \Phi(2) = 0{,}0228$, $D = 28{,}5\%$ en $1{,}4\%$ (H4), en de intuïtie wordt daar
  ingelost.
- Bayesiaanse shrinkage: het uitgewerkte voorbeeld 1% met $t = 2{,}5$ en $\tau = 0{,}4\%$
  geeft 0,5% en kans 0,961; het corollarium over selectie beantwoordt de voor de hand
  liggende tegenwerping.

*Aanmerkingen.*
- Toy-voorbeeld: "De tweezijdige p-waarde volgt uit $p = 2\,(1 - \Phi(|t|))$ met een normale
  tabel." $\Phi$ krijgt geen naam; $\varphi$ evenmin in de stelling "Verwachte $t$ na
  selectie" (r. 342).
- Opzet en notatie: "Die premie is de alpha ten opzichte van een model zonder premie, of ten
  opzichte van een factormodel als dat erbij staat." (r. 233)
- Bonferroni en Holm: "Zolang de eerste $j - 1$ verwerpingen terecht waren, zijn daarvan
  hoogstens $M - j + 1$ over" (r. 263); "daarvan" moet terugzoeken naar "ware
  nulhypothesen", en de verwerpingen waren juist *onterecht* nodig om een ware nul weg te
  halen. Hier bedoeld: zolang geen ware nul is verworpen.
- FF5 en q-factoren: "Het verwachte rendement daalt dus met de investeringsgraad en stijgt
  met de verwachte winstgevendheid, omdat een onderneming met lage kapitaalkosten veel
  investeert." (r. 578) De reden dekt alleen de investeringshelft.
- FF5 en q-factoren: "\ \text{ bij gegeven risico } \Cov_t(m_{t+1}, R_{t+1})" (r. 565) hangt
  aan een vergelijking die een identiteit is (de noemer is op $t$ bekend); de voorwaarde
  hoort bij de vergelijkende uitspraak, niet bij de formule.
- H7: "voorspeller" (Overzicht, Wat er brak) en "signaal" (Theorie, Replicatie) wisselen;
  de alias wordt pas op r. 229 gegeven, na drie keer "voorspellers".

*Beter uitleggen.* De afgeknotte schatting (r. 977–981): waarom de gerapporteerde $t$
variantie $1 + \omega^2$ heeft, verdient een halve zin (som van $\delta$ en ruis). En bij
$\hat\mu_\delta = -7{,}4$ helpt één getal: onder die prior is $\Pr(\delta < 0) \approx 0{,}89$.

*Voor een 9.* $\Phi$ en $\varphi$ bij eerste gebruik benoemen (06_34_factor_zoo.md:118, 342);
r. 233 herschrijven tot "het gemiddelde rendement, of de alpha als er een factormodel bij
staat"; r. 263 "daarvan" vervangen door het ding; r. 578–579 de reden voor winstgevendheid
toevoegen in dezelfde zin; de voorwaarde uit r. 565 naar de tekst op r. 578; de alias
signaal/voorspeller naar de eerste vermelding in het Overzicht (r. 37).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord ("Na publicatie verliezen ze echter meer
  dan de helft van hun rendement, veel meer dan publicatieselectie alleen kan verklaren").
- De intuïtie voorspelt dat een toevalstreffer alles verliest en een sterk signaal bijna
  niets, en dat de daling in de tussenperiode kleiner is dan die erna; Theorie
  (r. 373–374), Simulatie en Replicatie lossen beide in, en de Replicatie laat eerlijk zien
  waar de statistische lezing tekortschiet (r. 1022–1023).
- Routekaart aan het begin van Theorie en een Samengevat die per resultaat de richting geeft;
  5.887 woorden.

*Aanmerkingen.*
- Toy-voorbeeld: het toy dekt alleen de eerste helft van de vraag ("hoeveel zijn echt"); de
  verzwakking komt pas in Theorie. De toygetallen keren alleen terug in "net als de
  nulsignalen B tot en met E in het toy-voorbeeld" (r. 666) en in oefening 1.
- Replicatie, Shrinkage: de sectie opent met een vraag en geeft de conclusie ("7 tot 9%,
  tegen 40%") pas na twee cellen (r. 1022).

*Beter uitleggen.* De sprong van Theorie (FF5 en q-factoren) naar de Replicatie-alpha's:
waarom de alpha-toets bij dezelfde vraag hoort (verklaart een handvol factoren de daling?)
staat pas op r. 1086.

*Voor een 9.* (Staat op 9,0.) Voor hoger: toy-signalen B–E in de afknottingsalinea
(06_34_factor_zoo.md:368–376); de conclusie van de shrinkagesectie naar haar eerste zin
(r. 939).

### 3. Taal (8,8)

*Goed.*
- Intuïtie: het vakgebied met driehonderd onderzoekers leest als gesproken uitleg.
- Wat er brak: de drie lezingen staan in lopende zinnen met verband, zonder dubbele punt als
  lijm.
- De telregels zijn gehaald: geen u/je, geen gedachtestreepjes, motiefnamen 0, geen
  regeltaal gevonden.

*Aanmerkingen.*
- De decompositie van McLean en Pontiff: "Zij vonden rendementen die in de tussenperiode 26%
  en na publicatie 58% lager lagen, zodat 32% aan handel op de publicatie toe te schrijven
  is" (r. 411).
- Wat er brak: "Meervoudig toetsen, publicatieselectie en shrinkage maken van de vraag of
  een signaal significant is een vraag waarvan het antwoord van het aantal pogingen afhangt."
  (r. 1109)
- Wat er brak: "Dat is de Yale-lezing. De Chicago-lezing past even goed. Daarin meten
  kenmerken blootstelling aan risico, ..." (r. 1127–1129), drie korte zinnen achter elkaar.
- Shrinkage: "De schatting laat vooral zien hoe slecht de ligging uit een afgeknotte
  steekproef te schatten is." (r. 1017), schatting/schatten.
- Oordeel: "Ook houdt over de hele periode een meerderheid bij BH en BHY een significante
  alpha, en krimpt die pas na publicatie tot de minderheid die we verwachtten." (r. 1103);
  "die" kan de alpha of de meerderheid zijn.
- Acht alinea's van één zin (prose_stats para_one 8), o.a. r. 193, 696, 1231.

*Beter uitleggen.* n.v.t.

*Voor een 9.* De vijf zinnen hierboven herschrijven (06_34_factor_zoo.md:411, 1017, 1103,
1109, 1127); twee van de losse eenzinsalinea's aan hun buur hangen (r. 193, 696).

### 4. Toy-voorbeeld (8,7)

*Goed.*
- Tabel met tien signalen, p-waarden en vier grenskolommen; met de hand in vijf minuten na
  te rekenen, en de code bevestigt met een `assert`.
- De slotzin zegt wat het getal betekent ("één tot vijf voorspellers, afhankelijk van de
  vraag welke vergissing hij wil vermijden").

*Aanmerkingen.*
- Toy-voorbeeld: "Holm $0{,}05/(11-j)$", "BH $0{,}05\,j/10$", "BHY $0{,}05\,j/(10 \cdot
  2{,}929)$" (r. 122) zijn drie tot vier formules die pas in Theorie worden afgeleid.
- Toy-voorbeeld: "Dat vier nulsignalen een $t$ van 2,2 of meer halen, is bij onafhankelijke
  toetsen onwaarschijnlijk, maar niet bij varianten van één idee." (r. 114) De bewering
  staat er zonder getal; de verwachte aantallen (bij tien toetsen ongeveer 0,3) zouden haar
  dragen.

*Beter uitleggen.* Waarom BHY hier strenger is dan Bonferroni voor B (0,00341 tegen 0,005):
een halve zin dat de prijs van robuustheid bij kleine $M$ al zichtbaar is.

*Voor een 9.* De grenskolommen laten steunen op één zin per procedure en de afleiding naar
Theorie verwijzen (06_34_factor_zoo.md:118–150); het getal bij r. 114 toevoegen door de zin
te herschrijven.

### 5. Code en figuren (8,8)

*Goed.*
- `multiple_testing` leest als de stellingen: stap-op en stap-af zijn zichtbaar, met een
  commentaar dat de stopregel noemt.
- `simulate_field` en `mp_regression` hebben benoemde tussenresultaten (`bread`, `scores`).
- Beide figuurteksten zeggen wat te zien is, met het getal (2,1; helling 0,61).

*Aanmerkingen.*
- Simulatie: "De figuur zet beide uitkomsten naast elkaar." (r. 697)
- De verzwakking/drempels: "De figuur toont beide verdelingen en het rendement per signaal."
  (r. 889)
- Toy-voorbeeld: de importcel (r. 99) staat direct onder de kop zonder zin ervoor; r. 197,
  198, 206, 873, 878 zijn regels van ruim 110 tekens.

*Beter uitleggen.* In de alpha-cel (r. 1055) is `after_pub` een broadcast-truc; een lus of een
naam met commentaar ("maand ligt na het publicatiejaar") maakt het leesbaar.

*Voor een 9.* Leeswijzer vóór beide figuren (06_34_factor_zoo.md:697, 889); lange regels
breken (r. 197–206, 873–879).

### 6. Replicatie en empirie (9,0)

*Goed.*
- Admonition met bron, wat, data, verschil en verwachte afwijking (~180 woorden).
- Oordeel-tabel origineel/hier, en het oordeel begint met "gedeeltelijk geslaagd" en verwijst
  naar de verwachte minderheid.
- De tweede shrinkage-benadering met afknotting en het eerlijke verslag van de ongeloofwaardige
  $\hat\mu_\delta$.

*Aanmerkingen.*
- Verschil met het origineel: "met elf jaar extra data" (r. 765); ten opzichte van welk
  artikel, en tot welk jaar? Niet herleidbaar uit een cel.
- Alpha's: "Na publicatie blijft bij elke procedure een minderheid over, van 10 bij
  Bonferroni tot 62 bij BH." (r. 1084); de naïeve toets (90) valt buiten die reeks.
- De verzwakking: vijf getallen in één alinea (r. 812–816), boven de norm van drie.

*Beter uitleggen.* Waarom de "voorspelde daling door selectie" (op gerapporteerde $t$) met de
waargenomen daling van rendementen vergeleken mag worden: één zin dat de relatieve daling van
$t$ en van het gemiddelde bij gelijke standaardfout samenvallen.

*Voor een 9.* (Staat op 9,0.) Voor hoger: r. 765 en r. 1084 corrigeren.

### 7. Oefeningen (9,1)

*Goed.*
- Oefening 1 is een instap op het toy, oefening 2 een afleiding, oefening 3 breidt de
  replicatie uit en levert een echte bevinding (publicatie-effect verdwijnt).
- Elke uitwerking eindigt met wat ze leert (r. 1174–1176, 1279–1281).

*Aanmerkingen.*
- Oefening 2: "De $t$-waarden van de signalen in de steekproef zijn gemiddeld bijna vier."
  (r. 1188) Geen cel toont dat gemiddelde; de enige gemiddelde $t$ in de uitvoer is 4,69
  (gerapporteerd).

*Beter uitleggen.* n.v.t.

## Feitelijke fouten

Nagerekend tegen de celuitvoer: toy (p-waarden, Holm/BH/BHY, $c(10) = 2{,}929$), $c(316) =
6{,}33$, $\lambda(2) = 2{,}373$, $D(2) = 28{,}5\%$, $D(4) = 1{,}36\%$, shrinkage-voorbeeld
(0,5; 0,283; 0,961; 0,2), simulatie (142/137, 2,33, 0,44%), $\delta = 2{,}10$ en $1{,}07$,
periodetabel (0,69; −40%; −57%; 55 maanden; 0,48), regressie (−36%, −54%, 18%), drempels (186,
188, 0,62, 122, 85, 3,68, 66, 11, BHY 137), shrinkage (0,80; 0,19; 0,94; 9%; 181), afknotting
(183; 4,69; −7,4; 6,1; 0,97; 4,37; 7%), alpha's (167, 164, 0,42, 99, 131, 161, 10–62, 0,30),
oefeningen (3,02; ABC; 42%/41%; 319; 15,4/36/57). Alle juist. Open:

1. r. 1084 (onjuist, klein): "van 10 bij Bonferroni tot 62 bij BH" terwijl de naïeve toets na
   publicatie 90 signalen houdt (cel 14). Correctie: "van 10 bij Bonferroni tot 62 bij BH, en
   90 zonder correctie" of "na correctie ...".
2. r. 596 (onzeker): "eind 2019 bezaten indexfondsen evenveel van de Amerikaanse beurs als
   actieve aandelenfondsen". ICI 2020 meldt voor eind 2019 16% voor index-aandelenfondsen en
   -ETF's tegen 14% voor actieve (uit het geheugen; tegen de bron controleren). Correctie:
   "iets meer dan".
3. r. 1188 (niet herleidbaar): "gemiddeld bijna vier". Geen cel; laat een cel het gemiddelde
   van `t_values["in-sample"]` tonen of noem de 4,69 van de gerapporteerde $t$.
4. r. 765 (niet herleidbaar): "met elf jaar extra data". Noem het eindjaar van MP en van de
   data hier, of schrap.

Geen vakterm is door de taalredactie van betekenis veranderd.

## Navertelling in vijf zinnen

Honderden gepubliceerde voorspellers zijn het product van veel pogingen, zodat de drempel
voor significantie met het aantal pogingen moet stijgen (Bonferroni/Holm voor één vergissing,
BH/BHY voor het aandeel, HLZ komen op ongeveer 3). Selectie op $t > 2$ blaast gepubliceerde
rendementen op met $\lambda(c-\delta)$, zodat een nulsignaal na publicatie alles verliest en
een sterk signaal bijna niets; McLean en Pontiff scheiden selectie (tussenperiode) van
arbitrage (na publicatie). In de OSAP-data van Chen en Zimmermann repliceren de meeste
signalen en overleven velen een strengere drempel, maar het rendement daalt na publicatie
57%. Shrinkage en afknotting verklaren daarvan hooguit 7 tot 9%, en met vaste effecten voor
kalendertijd verdwijnt het publicatie-effect, zodat de daling niet van een algemene daling
door de tijd te scheiden is. Het kader zegt dus hoeveel we moeten wantrouwen, maar niet of de
daling arbitrage, risicodeling of datamining is. Dit stemt overeen met het Overzicht.

## De taal na de redactie

De redactie heeft het college vloeiend gemaakt: geen telegramzinnen, geen dubbele punten als
lijm, verband via voegwoorden, één zin boven 40 woorden. Wat blijft zijn enkele zinnen die
geschreven klinken. Hardop-toets:

1. "Zij vonden rendementen die in de tussenperiode 26% en na publicatie 58% lager lagen,
   zodat 32% aan handel op de publicatie toe te schrijven is." → "Volgens hen lag het
   rendement in de tussenperiode 26% lager en na publicatie 58%, zodat 32% toe te schrijven
   is aan handel op het artikel."
2. "Meervoudig toetsen, publicatieselectie en shrinkage maken van de vraag of een signaal
   significant is een vraag waarvan het antwoord van het aantal pogingen afhangt." → "Na
   meervoudig toetsen, publicatieselectie en shrinkage hangt het antwoord op de vraag of een
   signaal significant is af van het aantal pogingen."
3. "Dat is de Yale-lezing. De Chicago-lezing past even goed. Daarin meten kenmerken
   blootstelling aan risico, ..." → "Dat is de Yale-lezing, maar de Chicago-lezing past even
   goed: kenmerken meten daarin blootstelling aan risico, ..." (of met "waarin" zonder dubbele
   punt).

Bij volledige oplossing van alle punten: 9,2

## Controle 1

Gelezen: kaart-rollen, deze beoordeling, sectie R9-1, het college eenmaal volledig; celuitvoer via
`tools/nb_outputs.py` (150 regels), `prose_stats --check`: PASS (5.998 woorden, zinnen 16,4, p90 26,
> 40: 0, para_one 8, motiefnamen 0).

**Getallencontrole.** Alle toegevoegde of gewijzigde getallen zijn herleidbaar: 0,028 (p van E, tabel)
en $9 \times 0{,}028 \approx 0{,}25$; 0,00341 (BHY rang 2, tabel); 2,54 = (2,79+2,70+2,45+2,20)/4 met
$\lambda(2) = 2{,}37$; $\Phi(7{,}4/6{,}1) \approx 0{,}89$ (afgeleid uit cel 13: $-7{,}355$, $6{,}131$);
gewicht 0,97 (cel 13); 4,69 (cel 13, oefening 2); 90 zonder correctie (cel 14); 26%/58% en 2,1 (cel 6, 16).
Geen niet-herleidbaar getal. De ICI-claim is afgezwakt tot "iets meer dan" (bron niet opnieuw nagezocht).

**Per punt.**
- Feitelijke fouten 1–4 (r. 1084, ICI, oefening 2 met 4,69, "elf jaar extra data"): opgelost.
- Verbetering 1 (toy): grenskolommen zonder formule, één zin per procedure, B–E keren terug bij de
  afknotting (2,54 tegen 2,37), getal bij de "vier nulsignalen"-bewering, BHY-tegen-Bonferroni als halve zin:
  opgelost. De genummerde antwoorden onder de tabel dragen nog de drempelformules (0,05/10, 2,929); ze
  staan er als rekenstap, dus deels.
- Verbetering 2 (helderheid): $\Phi$, $\varphi$, r. 233, Holm "daarvan", q-reden voor beide helften,
  $\Cov_t$-voorwaarde: opgelost. Alias signaal/voorspeller naar het Overzicht: grotendeels; "voorspellers"
  staat nog in de Waar-we-zijn-kaart (r. 29) vóór de alias, deels.
- Verbetering 3 (figuren): leeswijzer vóór beide figuren: opgelost.
- Opbouw: shrinkage opent met de conclusie, alpha-sectie met het waarom, B–E in Theorie: opgelost.
- Taal: hardop-zinnen 1–3, r. 1017 en r. 1103: opgelost; eenzinsalinea's r. 193 en 696 aangehangen,
  maar para_one blijft 8, dus deels.
- Beter uitleggen (variantie $1+\omega^2$, $\Pr(\delta<0)$, relatieve daling): opgelost.
- Code: importcel na inleidende zin, `after_pub` via `pub_year`: opgelost; enkele coderegels blijven 115–119
  tekens, deels.
- Replicatie (vijf getallen in één alinea gesplitst): opgelost. Niet verslechterd; geen nieuwe feitelijke fouten.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 | 9,1 |
| 3 | Taal | 20% | 8,8 | 9,0 |
| 4 | Toy-voorbeeld | 10% | 8,7 | 9,0 |
| 5 | Code en figuren | 10% | 8,8 | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 | 9,0 |
| 7 | Oefeningen | 5% | 9,1 | 9,1 |
| | **Eindcijfer (gewogen)** | | 8,9 | **9,0** (9,025) |

Plafondregel gehouden: geen deelcijfer boven het in het vooruitzicht gestelde cijfer (toy 9,1, opbouw 9,2,
helderheid 9,1, code 9,1), eindcijfer onder 9,2. Geen deelcijfer onder 8,5; taal ≥ 8.
