STATUS 01_04_markowitz F6c words=5889 prose=PASS open=0 cijfer=9,3 min=9,0
Cijfer van record 9,3: F6c gaf 9,4 met code en replicatie op 9,5 zonder F6-punt; met die twee op 9 (plafond §11.3) is het gewogen cijfer 9,3.

# Eindbeoordeling (F6): Markowitz, Roy en Tobin

## Ronde 9+

Vorige ronde: 8,7

Gelezen: `lectures/01_04_markowitz.md` (na taalredactie), `prose_stats --check` PASS
(5.777 woorden, zinnen gemiddeld 16,8, alinea gemiddeld 46, geen zin > 40, 12 alinea's
van één zin, 3 "Wie"-openingen, dubbele punt 2,1 per 1000). Getallen nagerekend tegen de
hand (toy, Roy, diversificatie, oefeningen) en tegen de celuitvoer zoals vastgelegd in
`notes/feiten-01_04_markowitz.md` (open=0, max. geleverde Sharpe in de nabouw 0,468 <
0,4722 voor 1/N).

## De drie verbeteringen met het meeste effect

1. **Vier taalfouten die een lezer hardop hoort, herschrijven** (taal 8,5 → 9). De
   woordvolgorde in de bijzin van het Overzicht (lectures/01_04_markowitz.md:58-60), "het
   het best" (:1051-1052), het projectwoord "replicatieblok" (:1084-1085) en de
   aangeplakte motiefzin "In de termen van theorie of feit (…)" (:69-72) [onderzoek E].
   Samen kosten ze het halve punt; elk is met één herschreven zin op te lossen.
2. **De vergelijkende uitspraak over $R^{f}$ een grens en een richting geven**
   (helderheid 9 → 9,5). "Stijgt $R^{f}$ … Daalt $R^{f}$, dan schuift ze terug naar de
   minimum-variantieportefeuille" (:536-539) geldt alleen voor $R^{f} < B/A = 5{,}51\%$,
   en de minimum-variantieportefeuille wordt pas bereikt als $R^{f}$ naar min oneindig
   gaat; bij $R^{f} = 0$ ligt de tangent nog op 7,24%. Eén bijzin met "zolang $R^{f}$
   onder 5,51% blijft" volstaat (H6).
3. **De √12-opmerking naar de eerste replicatietabel verplaatsen** (opbouw 9 → 9,5).
   "Om deze maandcijfers met de simulatie te vergelijken, moeten ze met $\sqrt{12}$
   worden vermenigvuldigd." (:1101-1103) komt pas nadat de lezer twee maandtabellen
   met de jaarlijkse 0,50 en 0,47 uit de simulatie heeft vergeleken; ze hoort bij de
   eerste tabel met Sharpe-ratio's (:1030-1032).

## Eindcijfer: 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9,5 |

Gewogen: 2,25 + 1,80 + 1,70 + 0,95 + 0,90 + 0,90 + 0,475 = 8,975, afgerond 9,0.
Laagste deelcijfer 8,5 (taal), dus niet blokkerend en op de ondergrens. Lengte 5.777
woorden, onder de 6.000.

## Per criterium

### 1. Helderheid van de uitleg (9)

*Goed.*
- Theorie, "Het kernresultaat": elke formule krijgt direct het toy-getal ($A = 128{,}125$,
  $D = 15{,}625$ tegen $AC = 65{,}5$, $\lambda = 0{,}368$, $\delta = -0{,}0125$,
  $\sigma = 15{,}6\%$ bij 10%), zodat H4 overal is ingelost.
- Het voorbehoud bij $\lambda$ ("Deze $\lambda$ is dus een Lagrange-multiplicator en niet
  de prijs van risico $\lambda_f$") en de uitleg van $D$ als maat voor spreiding in
  verwachte rendementen voorkomen twee klassieke verwarringen.
- "Waar het strandt": de drie redenen staan elk met een getal (6,3 procentpunt; $-6{,}25$;
  $N/T = 0{,}083$ tegen 0,021), en het geleende resultaat uit 00_01 wordt in één regel
  herhaald.

*Aanmerkingen.*
- Theorie, "Een risicovrij activum: Tobin en Roy": "Daalt $R^{f}$, dan schuift ze terug
  naar de minimum-variantieportefeuille." Zonder grens klopt dit niet letterlijk (zie
  verbetering 2).
- Theorie, "Een risicovrij activum: Tobin en Roy": "Zo liggen de tangentportefeuille uit
  het toy-voorbeeld (8,22%, standaarddeviatie 11,76%) en een ramp van $r_{\min} = -20\%$
  2,4 standaarddeviaties uit elkaar." De rekensom illustreert de grens, maar de lezer kan
  denken dat Roys belegger met $r_{\min} = -20\%$ deze portefeuille kiest; die kiest een
  andere randportefeuille.

*Beter uitleggen.* Bij Roy één bijzin die zegt dat het getal alleen de grootte van de
Tsjebysjev-grens toont (17% tegen 0,8%) en niet Roys keuze bij $-20\%$. Bij $R^{f}$ het
kantelpunt $B/A$ noemen.

*Voor een 9.* Gehaald. Voor een 9,5: lectures/01_04_markowitz.md:536-539 (grens
$R^{f} < B/A$) en :645-650 (rol van het Roy-getal).

### 2. Opbouw en rode draad (9)

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord, inclusief de minimum-variantie-uitkomst
  die de replicatie later bevestigt.
- De twee voorspellingen uit de intuïtie (:108-110) worden ingelost bij :329-330 en
  :530-534, en het wegdiversifiëren bij :708-710.
- Toy-getallen keren terug in de theorie, de figuur, de tangent, Roy en de oefeningen;
  de simulatie ijkt op 0,50 tegenover de 0,529 van het toy.

*Aanmerkingen.*
- Replicatie op echte data: "Om deze maandcijfers met de simulatie te vergelijken, moeten
  ze met $\sqrt{12}$ worden vermenigvuldigd." Deze zin komt te laat (verbetering 3).

*Beter uitleggen.* Geen inhoudelijk gat; alleen de volgorde van de omrekening.

*Voor een 9.* Gehaald. Voor een 9,5: :1101-1103 naar :1030-1032.

### 3. Taal (8,5)

*Goed.*
- De Theorie-alinea's lopen hardop goed, met voegwoorden in plaats van knippen
  ("Hij ruilt om, en bij elke ruil daalt zijn variantie terwijl…", :279-282).
- De oude vaste wendingen uit onderzoek E zijn weg: geen "De bewering:", één
  "In woorden:" (:510), geen "zoals de intuïtie voorspelde", "zij" voor de portefeuille
  vervangen, "maakt de afgeleide eenvoudiger" (:295), "Hoeveel van die Sharpe-ratio
  haalt …" (:785).
- Motiefnamen elk hoogstens één keer bij naam, en "risico of vergissing" zegt ter plekke
  wat het hier betekent (Chicago- en Yale-lezing, :1189-1199).

*Aanmerkingen.*
- Overzicht: "waarin de gelijkgewogen portefeuille (hierna 1/N) verslaat de
  mean-variance-portefeuille (de tangentportefeuille uit geschatte momenten)." Fout in
  de woordvolgorde: in de bijzin hoort het werkwoord achteraan.
- Overzicht: "In de termen van theorie of feit (is dit een theorie die getoetst wordt,
  of een feit dat op een verklaring wacht?) is het een *theorie van keuze* …" Klinkt nog
  steeds aangeplakt [onderzoek E, MW:69 en alinea over de motiefzin].
- Replicatie op echte data: "In beide datasets verliest mean-variance van 1/N, en doet
  minimum-variantie het het best." [onderzoek E, "het het"].
- Replicatie op echte data: "De ordening is dezelfde als bij DGU en als we in het
  replicatieblok verwachtten." "Replicatieblok" is projecttaal (STYLE §11.12).
- Intuïtie: "De portefeuilles die niet te verslaan zijn, vormen de *efficient frontier*
  (efficiënte rand: de laagste variantie bij elk verwacht rendement)." De Engelse term
  staat in de lopende zin en de Nederlandse als alias, omgekeerd aan H7, met een dubbele
  punt binnen de haakjes.
- De inlossing van de intuïtie staat drie keer in bijna dezelfde vorm: "dat bevestigt de
  eerste verwachting uit de intuïtie" (:330), "Ook de tweede verwachting uit de intuïtie
  komt dus uit." (:533-534), "daarmee klopt ook wat de intuïtie zei" (:710). Eén keer kan
  zonder het woord "intuïtie" (STYLE §11.12, vaste wendingen).
- Kleine resten: "mandje" naast "portefeuille" (:103-106) [onderzoek E, MW:101]; "wij
  ruim twintig jaar later" naast overal "we" (:948) [onderzoek E]; "het mechanisme van
  punt 2 in de theorie" (:1161) verwijst naar een lijstnummer in plaats van naar het
  mechanisme.

*Beter uitleggen.* Niet van toepassing; alle punten zijn herschrijvingen van bestaande
zinnen.

*Voor een 9.* :58-60 woordvolgorde; :69-72 motiefzin; :1051-1052 "het het";
:1084-1085 "replicatieblok"; :97-99 term en alias omdraaien; :533-534 of :710 anders
formuleren. De eerste vier samen zijn genoeg voor een 9.

### 4. Toy-voorbeeld (9,5)

*Goed.*
- Vijf handstappen met exacte breuken (7/41, 2/41, 32/41) en een controle in stap 5 dat
  alle covarianties met de portefeuille gelijk zijn: in vijf minuten na te rekenen.
- Eén mechanisme (mengsel veiliger dan het veiligste activum), tabel hand/code, slotzin
  die zegt wat het getal betekent.
- Het recept wordt vooraf als "het eerste wat de theorie afleidt" aangekondigd, zodat de
  ene nog niet afgeleide formule verantwoord is.

*Aanmerkingen.* Geen.

*Beter uitleggen.* Niets nodig.

### 5. Code en figuren (9)

*Goed.*
- Elke tabelcel heeft kolommen "met de hand" en "code"; variabelen volgen de wiskunde
  (`Sinv_1`, `Sinv_mu`, `w_tan`, `sharpe_true`).
- De simulatielus is zichtbaar, met commentaar per stap (trekken, schatten,
  optimaliseren); `rolling_oos` toont met `values[t - window:t]` dat er geen toekomstige
  informatie in zit.
- Vóór elke figuur staat waar op te letten (afstand tot de rand, raakpunt; afstand tussen
  de verdelingen en de zwarte lijn; onrust van de mean-variance-lijn), en het bijschrift
  zegt wat te zien is.

*Aanmerkingen.*
- Toy-voorbeeld: de importcel (:119-129) wordt gevolgd door "**Opzet.**" zonder zin die
  de cel afsluit; licht, omdat de zin ervoor zegt dat de cel de pakketten laadt.
- Replicatie op echte data: "De figuur toont de cumulatieve overrendementen van de drie
  strategieën, en daarin valt vooral op hoe onrustig de mean-variance-lijn is." De
  leeswijzer geeft het antwoord al in plaats van waarop te letten.

*Beter uitleggen.* Bij de positiecel (:1139-1153) staat de definitie van brutopositie en
omzet pas na de tabel (:1156-1158); vóór de cel helpt de lezer de kolommen te lezen.

*Voor een 9.* Gehaald. Voor een 9,5: :1156-1158 vóór de cel zetten.

### 6. Replicatie en empirie (9)

*Goed.*
- Admonition met bron, wat, data, verschil en verwachte afwijking, gekoppeld aan een
  expliciete verwachting (ordening wel, niveau niet; SE 0,04).
- Tabel origineel/hier met de kolommen "verschil met 1/N buiten" en "gat: in minus
  buiten"; het oordeel begint met **Geslaagd.** en verwijst naar de verwachting.
- Eerlijk voorbehoud: eigen verschillen (−0,077 en −0,055) onder 2 × 0,04, en de
  opmerking dat de SE van een verschil van de correlatie afhangt.

*Aanmerkingen.*
- Replicatie op echte data: "**Geslaagd.** De ordening is dezelfde als bij DGU en als we
  in het replicatieblok verwachtten." Oordeel juist, woordkeus zie taal.
- Admonition, "Verschil met het origineel": "Hun FF-vierfactordataset, 24 reeksen van de
  French-website vanaf juli 1963, ligt het dichtst bij onze 25 portefeuilles, terwijl we
  voor de industrieën geen getallen van hen hebben." Twee beweringen in één zin met een
  onlogisch "terwijl" [onderzoek E, MW:938-940, deels opgelost].

*Beter uitleggen.* Waarom de FF-vierfactorrij (20 portefeuilles plus 4 factoren) een
redelijke vergelijking is met 25 size/BM-portefeuilles, in één bijzin.

*Voor een 9.* Gehaald. Voor een 9,5: :950-952 splitsen en de vergelijkbaarheid noemen.

### 7. Oefeningen (9,5)

*Goed.*
- Instap is een variatie op het toy (correlatie nul) met hand, code en les ("minder
  covariantie maakt de portefeuille veiliger zonder dat een activum minder riskant
  wordt").
- De zero-beta-oefening leidt een nieuw resultaat af, rekent het uit op het toy (exact 2%)
  en legt het verband met Black (1972).
- De krimpoefening breidt de replicatie uit en eindigt met de les dat het probleem in de
  invoer zit.

*Aanmerkingen.* Geen.

*Beter uitleggen.* Bij de krimpoefening zegt "De tussenwaarden doen het slechter"
(:1366-1368) niet of ze ook slechter zijn dan $\phi = 1$; één getal erbij volstaat.

## Feitelijke fouten

Geen. Nagerekend en in orde: $\boldsymbol\Sigma^{-1}$ en $\boldsymbol\Sigma^{-1}\mathbf{1}
= (21{,}875;\,6{,}25;\,100)'$, gewichten 7/41, 2/41, 32/41, 8,83%; $A, B, C, D$
(128,125; 7,0625; 0,51125; 15,625; $D/AC = 0{,}24$); $\boldsymbol\Sigma^{-1}\boldsymbol\mu
= (1{,}9375;\,1{,}125;\,4)'$; $\lambda = 0{,}368$, $\delta = -0{,}0125$, 15,6% (22%
minder dan 20%); $C/B = 7{,}24\%$; tangent (1/3; 2/9; 4/9; 8,22%; 0,529; 11,76%); Roy
((0,0822 + 0,20)/0,1176 = 2,40; 1/5,76 = 17%; $\Phi(-2{,}4) = 0{,}8\%$); diversificatie
(19,05%; 9,53%; bij 30 aandelen 10,0%); $N/T = 0{,}083 \approx 4 \times 0{,}021$;
757 maanden (1963-07 t/m 2026-07) en 637 buiten de steekproef, $1/\sqrt{637} = 0{,}040$;
replicatiegetallen, posities (21; 1158) en simulatie (0,50; 0,47; 0,16; 0,39) volgens de
celuitvoer in `notes/feiten-01_04_markowitz.md`; oefeningen (9/49, 4/49, 36/49; 8,57%;
$\mu_z = 0{,}0200$; 0,239 tegen 0,104; 7,6 tegen 72).

Onnauwkeurig, geen fout: lectures/01_04_markowitz.md:536-539 (zie helderheid).

## Navertelling in vijf zinnen

Markowitz maakte van risico een eigenschap van de portefeuille: een activum is zo riskant
als zijn covariantie met de rest, en een mengsel kan veiliger zijn dan het veiligste
activum. Wie alleen op verwachting en variantie let, kiest op een parabolische rand
waarvan elk punt een mengsel is van twee vaste fondsen. Met Tobins risicovrije activum
houdt iedereen dezelfde tangentportefeuille en verschilt alleen de dosis; Roys
veiligheid-eerst-belegger komt bij dezelfde portefeuille uit. In een grote portefeuille
blijft alleen covariantie over, zodat idiosyncratisch risico niet beloond hoeft te
worden. In de praktijk maakt de schattingsfout in $\boldsymbol\mu$ de geschatte optimale
portefeuille slechter dan 1/N, en wint de minimum-variantieportefeuille, die
$\boldsymbol\mu$ niet gebruikt. Dit komt overeen met het Overzicht.

## Oordeel over de taal na de redactie

De redactie heeft de sjabloonzinnen uit de vorige ronde grotendeels weggewerkt en de
Theorie leest nu als gesproken Nederlands. Wat overblijft zijn losse fouten, geen
patroon, maar één ervan (de woordvolgorde) staat op het eerste scherm. De telling van
twaalf alinea's van één zin bestaat grotendeels uit overgangen vóór een codecel en is
geen punt.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. :58-60 "waarin de gelijkgewogen portefeuille (hierna 1/N) verslaat de
   mean-variance-portefeuille (de tangentportefeuille uit geschatte momenten)."
   Herschrijving: "waarin de gelijkgewogen portefeuille (hierna 1/N) de
   mean-variance-portefeuille, de tangentportefeuille uit geschatte momenten, verslaat."
2. :69-72 "In de termen van theorie of feit (is dit een theorie die getoetst wordt, of
   een feit dat op een verklaring wacht?) is het een *theorie van keuze* en geen
   uitspraak over prijzen, want die uitspraak komt pas met het CAPM."
   Herschrijving: "Markowitz levert zo een *theorie van keuze*: hij zegt wat een belegger
   hoort te kiezen, niet wat prijzen doen, en een toetsbare uitspraak over prijzen komt
   pas met het CAPM."
3. :1051-1052 "In beide datasets verliest mean-variance van 1/N, en doet
   minimum-variantie het het best."
   Herschrijving: "In beide datasets verliest mean-variance van 1/N, en haalt
   minimum-variantie de hoogste Sharpe-ratio."

## Controle 1

Gecontroleerd tegen R9-1 (F6b) in `notes/rapport-01_04_markowitz.md` en het college
zoals het nu op de schijf staat: 5.889 woorden, `prose_stats --check` PASS
(sent_mean 17, geen zin > 40, para_one 11, geen motief/Lnum/deel/u_form/je_form/
taboo/stopw/calque/engquote-treffers).

**Drie verbeteringen.**
1. Vier taalfouten herschreven: **opgelost**. Woordvolgorde 1/N-bijzin (:58-60),
   motiefzin nu "Markowitz levert daarmee een *theorie van keuze* …" (:68-71),
   "het het best" is nu "haalt … de hoogste Sharpe-ratio" (:1065-1066),
   "replicatieblok" is nu "vooraf" (:1099). Alle vier letterlijk of gelijkwaardig
   aan de voorgestelde herschrijving.
2. $R^{f}$ een grens en een richting geven: **opgelost**. "zolang $R^{f}$ onder het
   rendement $B/A = 5{,}51\%$ … blijft" en "die bereikt ze pas als $R^{f}$ naar min
   oneindig gaat" (:540-546), en dezelfde grens staat nu ook in Samengevat (:781).
3. √12-opmerking verplaatst: **opgelost**. Ze staat nu vóór de eerste Sharpe-tabel
   (:1042-1046, "Alle Sharpe-ratio's hierna zijn per maand …") en niet meer bij de
   winnaar-alinea.

**Overige punten uit "Voor een 9" / "Voor een 9,5" / "Beter uitleggen".**
- Helderheid, Roy: het getal toont nu expliciet alleen de grootte van de grens,
  "ook al kiest Roys belegger bij een ramp van $r_{\min} = -20\%$ een ander punt op
  de rand" (:655-656). **Opgelost.**
- Taal, :97-99 term/alias omgedraaid: **opgelost**, "*efficiënte rand* (*efficient
  frontier*)" met de Nederlandse term in de lopende zin (:97).
- Taal, drievoudige inlossing van "intuïtie": **opgelost**, nu twee keer met het
  woord (:332, :719) en één keer zonder (:537-538, "Zo komt ook de tweede
  verwachting uit").
- Taal, kleine resten ("mandje", "wij ruim twintig jaar later", "punt 2 in de
  theorie"): **opgelost**. "Mandje" komt niet meer voor, "wij" is "onze data"
  (:960), en de verwijzing bij de replicatie noemt nu het mechanisme zelf in
  plaats van een lijstnummer: "$\boldsymbol{\Sigma}^{-1}$ juist de ruis tussen
  gecorreleerde activa uitvergroot" (:1175-1176).
- Code en figuren, definitie brutopositie/omzet vóór de cel: **opgelost**
  (:1150-1153, vóór de celcode op :1156).
- Code en figuren, leeswijzer cumulatieve figuur gaf de uitkomst weg: **opgelost**,
  nu "het gaat vooral om het verloop van de mean-variance-lijn naast dat van de
  andere twee" (:1119-1120).
- Replicatie, admonition-zin met onlogisch "terwijl": **opgelost**, gesplitst in
  twee zinnen met de reden van vergelijkbaarheid (twintig size/BM-reeksen plus vier
  factoren, :961-964).
- Oefeningen, tussenwaarden krimpoefening zonder vergelijking met $\phi=1$: buiten
  het plafond (deelcijfer was al 9,5), maar toch **opgelost**: "Sharpe-ratio van nul
  bij $\phi = 0{,}5$" (:1382-1384).
- Code en figuren, "**Opzet.**" na de importcel zonder afsluitende zin: buiten het
  plafond, toch **opgelost** (nu een gewone zin, :130).

**Feitelijke fouten.** Geen nieuwe. De eerder gemelde onnauwkeurigheid bij $R^{f}$
(§ hierboven) is met de grens $B/A$ opgelost.

**Hardop-toets.** Alle drie geciteerde zinnen herschreven zoals voorgesteld of
gelijkwaardig (:58-60, :68-71, :1065-1066); bij het herlezen geen nieuwe zinnen
opgevallen die niet hardop klinken.

**Verslechtering.** Geen gevonden; geen nieuwe punten toegevoegd.

**Deelcijfers (plafondregel §11.3).**

| nr | criterium | vorig | plafond | nu |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 9 | 9,5 | 9,5 |
| 2 | Opbouw en rode draad | 9 | 9,5 | 9,5 |
| 3 | Taal | 8,5 | 9 | 9 |
| 4 | Toy-voorbeeld | 9,5 | — (geen punt) | 9,5 |
| 5 | Code en figuren | 9 | 9,5 | 9,5 |
| 6 | Replicatie en empirie | 9 | 9,5 | 9,5 |
| 7 | Oefeningen | 9,5 | — (geen punt) | 9,5 |

Gewogen: 0,25·9,5 + 0,20·9,5 + 0,20·9 + 0,10·9,5 + 0,10·9,5 + 0,10·9,5 + 0,05·9,5
= 2,375 + 1,90 + 1,80 + 0,95 + 0,95 + 0,95 + 0,475 = 9,40.

**Eindcijfer: 9,4.** Laagste deelcijfer 9,0 (taal), boven de ondergrens van 8,5 en
niet blokkerend. Lengte 5.889 woorden, onder de 6.000.
