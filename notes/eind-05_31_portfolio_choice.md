STATUS 05_31_portfolio_choice F6c words=6000 prose=PASS open=2 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,8 -> F6c 9,0.
# Eerste herziening (workflow §12)

Eindbeoordeling F6 van `lectures/05_31_portfolio_choice.md`, gelezen na F1, F23 en F4T.
Getallen nagerekend tegen `$TEMP/F6-05_31_portfolio_choice-out.txt` (nb_outputs) en met de
hand (toy (a) en (b), 12/√500, 1000/3, √(1/23), alle verhoudingen in de replicatie).

## De drie verbeteringen met het meeste effect

1. **Helderheid (8,5 → 9,0): de long-only-schatting benoemen en de losse beweringen over
   $\hat\theta$ rechtzetten.** Regel 891 noemt "De schatting $\hat\theta = (2{,}38;\ 19{,}24;\ 5{,}31)$"
   zonder te zeggen dat dit de long-only-schatting is, direct na een tabel met
   $(-1{,}37;\ 5{,}00;\ 2{,}18)$; de lezer denkt dat de regel zelf bedoeld is en mist dat
   size van teken wisselt. Regel 925 ("in de buurt van hun waarden in de steekproef") klopt
   niet voor 1974 (B/M 3,53 tegen 5,00, momentum 3,15 tegen 2,18). Regel 471 ("bevat weinig
   ruisende rendementen") is dubbelzinnig. Het figuurbijschrift op regel 705 ("bij vijftig
   jaar niet meer") moet tegen de histogram worden gecontroleerd.
2. **Replicatie (8,5 → 9,0): de getallen na 2002 uit de lopende tekst in de tabel.** Regels
   997–1004 dragen zes getallen in proza (0,62; 0,72; 0,9%; 23%; 14%; 0,21). Een rij of
   kolom "2003–2026" in de tabel origineel/hier (regel 979) houdt het oordeel in woorden en
   de getallen in de tabel, zoals de rubriek vraagt.
3. **Code en figuren (8,5 → 9,0): de twee compacte trucs in de simulatiecel zichtbaar
   maken.** De Woodbury-inversie op regels 645–646 en de AR(1) via `signal.lfilter` met `zi`
   op regels 607–609 staan nergens in de proza; één zin vóór de cel (of een zichtbare lus
   voor de AR(1)) maakt de code leesbaar als de wiskunde.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,8

| criterium | gewicht | deelcijfer |
|---|---|---|
| 1 Helderheid van de uitleg | 25% | 8,5 |
| 2 Opbouw en rode draad | 20% | 9,0 |
| 3 Taal | 20% | 9,0 |
| 4 Toy-voorbeeld | 10% | 9,0 |
| 5 Code en figuren | 10% | 8,5 |
| 6 Replicatie en empirie | 10% | 8,5 |
| 7 Oefeningen | 5% | 9,0 |
| **gewogen** | | **8,775 → 8,8** |

### 1 Helderheid van de uitleg (8,5)

*Goed*
- Theorie, BSC: het bewijs krijgt een zin die zegt waarom het werkt (indicatoren knippen het
  probleem op) en het toy keert terug met $\mathbf{A}$ en $\theta_0 = 0{,}24950$ (regels 329–334).
- "Wat het voorspelt": elke formule krijgt een getal (12/√500 ≈ 0,54%, factor ruim
  driehonderd; regels 446–453), en $\gamma$ krijgt een richting (regel 472).
- Theorie, BSV-GMM: de momentvoorwaarde krijgt een economische lezing als $p = \E[mx]$ met
  terugverwijzing (regels 426–429).

*Aanmerkingen*
- Replicatie BSV: "De schatting $\hat\theta = (2{,}38;\ 19{,}24;\ 5{,}31)$ lijkt niet op die uit het artikel, maar Sharpe-ratio en certainty equivalent liggen er dicht bij." (regel 891) Welke schatting? Het is de long-only-$\theta$ uit de `print`, niet de regel uit de tabel.
- Replicatie BSV: "Tot 2003 blijven de drie coëfficiënten in de buurt van hun waarden in de steekproef, en daarna kruipt size naar nul en zakt B/M." (regel 925) In 1974 is B/M 3,53 en momentum 3,15 tegen 5,00 en 2,18; het bijschrift (regel 973) zegt terecht dat B/M eerst stijgt.
- "Wat het voorspelt": "De matrix is $K\times K$ en bevat weinig ruisende rendementen, in plaats van de $N\times N$-matrix van [](#01-04-markowitz)." (regel 471) "Weinig ruisende" leest als "weinig, ruisende" of als "niet erg ruisende".
- Toy (a): "met relatieve risicoaversie $\gamma = 5$" (regel 122–123). Bij kwadratisch nut is $\gamma$ de coëfficiënt in het nut, geen relatieve risicoaversie; die hangt van de uitkomst af.

*Beter uitleggen*
- Waarom de long-only-schatting zo anders uitvalt (size positief, B/M bijna vier keer zo groot) terwijl de prestaties dicht bij het artikel liggen: één zin dat afkappen de schaal van $\theta$ niet meer vastlegt.
- De notatie $R_{i,t+1}$ wisselt tussen bruto (regel 370), overrendement (regel 436) en $R^e$ (regel 575); één zin bij regel 436 dat hier overrendementen bedoeld zijn.

*Voor een 9*
- lectures/05_31_portfolio_choice.md:891 schatting als long-only benoemen, met het tekenverschil bij size.
- lectures/05_31_portfolio_choice.md:925 "in de buurt" vervangen door wat de cel toont.
- lectures/05_31_portfolio_choice.md:471 herschrijven (zie taal).
- lectures/05_31_portfolio_choice.md:123 "relatieve risicoaversie" → "risicoaversiecoëfficiënt".

### 2 Opbouw en rode draad (9,0)

*Goed*
- Overzicht stelt de vraag, geeft het antwoord in twee zinnen en noemt de vier stappen (regels 30–46).
- De drie voorspellingen uit de Intuïtie (regels 92–96) worden ingelost in de simulatie (regel 711), de theorie over $K/T$ en de GSC-replicatie en "Waar het breekt".
- Routekaart (regel 270) en Samengevat (regel 558) staan goed; 5.834 woorden.

*Aanmerkingen*
- Simulatie: "De verwachting uit de intuïtie komt dus uit, maar pas bij een steekproef die langer is dan de meeste beleggers hebben." (regel 711–712) De Intuïtie voorspelde winst tegen "de markt"; de simulatie meet tegen 1/N. Eén woord in regel 92 of 711 maakt dat gelijk.

*Beter uitleggen*
- De simulatie gebruikt van het toy alleen $\gamma = 5$; dat volstaat, maar de premies van 0,03% zouden in het toy of in "Wat het voorspelt" al een keer als getal kunnen staan.

### 3 Taal (9,0)

*Goed*
- Zinnen gemiddeld 17,8 woorden, alinea's gemiddeld 47, geen gedachtestreepjes; `--check` PASS.
- Motiefnamen elk één keer (regels 61, 1145), twee "Wie"-zinnen, geen regeltaal.
- De redacteur heeft geen vakterm van betekenis veranderd; "managed portfolios", "certainty equivalent" en "mean-variance" zijn consequent.

*Aanmerkingen*
- Toy (a): "Er is maar één recept nodig, de optimale positie bij kwadratisch nut, $w = \mu/(\gamma s)$, en in matrixvorm $\boldsymbol{\theta} = …$. De theorie leidt die formule als eerste af." (regels 133–136)
- Theorie, BSC: "Een vaste mix over vaste reeksen kiezen is het probleem van Markowitz, en als de regel elke toestand apart kan behandelen, verliest de belegger daar niets bij." (regels 282–284)
- "Wat het voorspelt": regel 471 (zie helderheid).

*Beter uitleggen* — geen inhoudelijk punt; de drie zinnen hieronder bij de hardop-toets.

### 4 Toy-voorbeeld (9,0)

*Goed*
- Beide delen met de hand na te rekenen; alle tussenstappen kloppen (determinant 0,00202, $\theta = (0{,}24950;\ 0{,}15050)$, nut 0,010495 tegen 0,007965, $\theta^\ast = 0{,}2167$).
- Tabel hand/code bij beide delen, met identieke uitkomsten in de celuitvoer.
- Slotzin (a) geeft de betekenis: een kwart van het nut komt van de voorspeller (0,241).

*Aanmerkingen*
- Toy (b): "Bij één periode stijgt het nut daarom onbeperkt in $\theta$ zolang $r^x > 0$." (regel 229) CRRA-nut met $\gamma = 5$ is begrensd door nul; het stijgt monotoon, niet onbeperkt.
- Toy (b): "kiest de belegger een kleine positieve $\theta^{\ast} = 0{,}2167$." (regel 265–266) De slotzin zegt niet wat 0,2167 betekent (bijvoorbeeld: gewicht op aandeel 3 stijgt van 0,20 tot 0,27).

*Beter uitleggen*
- Deel (b) voegt CRRA-nut toe naast het kwadratische nut van (a); één bijzin dat (b) CRRA gebruikt omdat BSV dat doen, voorkomt de vraag waarom het nut wisselt.

*Voor een 9* — is 9; voor hoger: lectures/05_31_portfolio_choice.md:229 en :265.

### 5 Code en figuren (8,5)

*Goed*
- Elke cel heeft een aankondiging en een zin erna; beide figuren hebben een leeswijzer vóór en een bijschrift dat zegt wat te zien is (regels 673–674, 705, 944–945, 973).
- De toy-cellen lezen als de wiskunde, met benoemde tussenresultaten.

*Aanmerkingen*
- Simulatie: `Dm, Db = m_hat / s2, b / s2                       # Woodbury inverse of vf*bb' + diag(s2)` (regel 645) en de regel erna: een inversieformule die de proza nergens noemt.
- Simulatie: `signal.lfilter([np.sqrt(1 - RHO_X[k] ** 2)], [1, -RHO_X[k]], noise[:, :, k], axis=0, zi=RHO_X[k] * x0[None, :, k])[0]` (regel 608–609): een AR(1) als filtertruc, waar een zichtbare lus het proces toont.
- Replicatie: `characteristic_panel` (regels 755–776) is dicht; de zin erna (regel 790) zegt niets over de standaardisatie per maand.

*Beter uitleggen*
- Eén zin vóór de simulatiecel: "Markowitz gebruikt een éénfactormodel, waarvan de inverse met de Woodbury-formule in gesloten vorm te schrijven is."

*Voor een 9*
- lectures/05_31_portfolio_choice.md:592–594 zin over éénfactormodel en Woodbury uitbreiden.
- lectures/05_31_portfolio_choice.md:607–609 AR(1) als zichtbare lus of met één regel commentaar.

### 6 Replicatie en empirie (8,5)

*Goed*
- Beide admonitions volledig en kort; tabellen origineel/hier (regels 979–990 en 1112–1118).
- Oordelen beginnen met "Gedeeltelijk geslaagd" en "Niet geslaagd" en verwijzen naar de verwachte afwijking (tekens, omzet, weggemiddelde bedrijfsvariantie).
- Na 2002 wordt de verwachting ("kleiner voordeel of geen") eerlijk getoetst met de standaardfout 0,21.

*Aanmerkingen*
- Replicatie BSV: "Op de 100 size/BM-portefeuilles haalt de regel een Sharpe-ratio van 0,62 tegen 0,72 voor de benchmark. Zijn certainty equivalent zakt tot 0,9% per jaar, omdat 23% volatiliteit voor 14% overrendement voor een belegger met $\gamma = 5$ een slechte ruil is." (regels 998–1001) Getallen in lopende tekst die niet in de tabel staan.
- Replicatie GSC: "De replicatie laat wel zien dat industriespecifieke onzekerheid het marktrendement niet voorspelt" (regel 1124). De regressie is op $V_t$ (59% afwijkingsterm), niet op de afwijkingsterm zelf.

*Beter uitleggen*
- Waarom de omzet tien keer zo hoog is als bij BSV staat op regel 889; dat de long-only-omzet (1,37) wel in de buurt komt, staat alleen in de celuitvoer en hoort in de tabel.

*Voor een 9*
- lectures/05_31_portfolio_choice.md:979–990 rij(en) "na 2002" toevoegen; 997–1001 inkorten tot het oordeel.
- lectures/05_31_portfolio_choice.md:1124 "industriespecifieke onzekerheid" → "de gemiddelde industrievariantie".

### 7 Oefeningen (9,0)

*Goed*
- Instap (oefening 1, variatie op toy (a)), afleiding (oefening 2), twee uitbreidingen van de replicatie (3 en 4).
- Elke uitwerking eindigt met een les (regels 1186, 1215, 1272, 1351); alle getallen kloppen met de celuitvoer.

*Aanmerkingen*
- Oefening 2(2): "Dezelfde stap werkt met $\E[(R_p - 1)^2] = …$" (regel 1204). De eerste-ordevoorwaarde zelf ontbreekt; de lezer moet hem invullen.

## Feitelijke fouten

Nagerekend tegen de celuitvoer; alle andere getallen in proza, bijschriften en tabellen
kloppen (toy (a) en (b), simulatie 0,09–0,15, 55%, 3,7 en 1,7; replicatie 98 van 100,
$t = -1{,}8$, 1,6 en een halve standaardfout, 2,85×, −180%, 9,0, 0,62/0,72, 0,9%, 23%/14%;
bijschrift −1,0 tot −1,4, −0,30, 3,5–5,2–2,7, 2,2–3,2; GSC-tabel, 59%, 0,74; oefeningen
0,048/0,81, 0,67/0,29, 0,84/0,53, 0,79%, 2,8/3,6/18,8/6,7/25,8%, 2,44/2,70/1,60/1,53, 1,83).

| nr | regel | bewering | oordeel | toelichting |
|---|---|---|---|---|
| 1 | 925 | "Tot 2003 blijven de drie coëfficiënten in de buurt van hun waarden in de steekproef" | onjuist | 1974: B/M 3,53 en momentum 3,15 tegen 5,00 en 2,18 in 2003. |
| 2 | 229 | nut "stijgt onbeperkt in $\theta$" | onjuist | CRRA met $\gamma = 5$ is begrensd door 0; wel monotoon stijgend. |
| 3 | 1124 | replicatie toont dat "industriespecifieke onzekerheid" niet voorspelt | onjuist (te sterk) | Regressor is $V_t$, niet de afwijkingsterm. |
| 4 | 705 | $\hat\theta_{\text{size}}$ loopt "bij vijftig jaar niet meer" over nul | onzeker | Met $\lambda = -0{,}03\%$ en $\Var(r^x) \approx 0{,}12^2/500$ is de ware $\theta \approx -2{,}1$; bij SD 1,68 ligt naar schatting ruim 10% van de werelden boven nul. Tegen de histogram controleren. |
| – | 671 | "$N/T$ tussen 0,8 en 4" | juist, afgerond | Werkelijk 0,83 tot 4,17. |
| – | 123 | "relatieve risicoaversie $\gamma$" bij kwadratisch nut | naamgeving | Zie helderheid; geen rekenfout. |

Geen vakterm door de taalredactie van betekenis veranderd.

## Navertelling in vijf zinnen

Een portefeuilleregel die lineair op signalen reageert, is een vaste mix van geschaalde
rendementsreeksen, zodat een dynamisch of cross-sectioneel probleem een klein
Markowitz-probleem wordt. Brandt, Santa-Clara en Valkanov schatten zo drie coëfficiënten
voor duizenden aandelen met GMM, en hun ruis groeit met $K/T$ in plaats van $N/T$. In de
simulatie verslaat de regel 1/N pas bij een steekproef van decennia, terwijl Markowitz op
500 gemiddelden kansloos is. Op French-portefeuilles lukt de replicatie tot 2002 wel, maar
daarna blijft de regel achter en krijgt hij dus de premie van gisteren niet meer. Het
resultaat dat de gemiddelde variantie de markt voorspelt, is op industriedata en na 1999
niet terug te vinden. Dit sluit aan bij het Overzicht.

## Taal na de redactie

De taal is na F4T natuurlijk en gevarieerd; de statistieken zitten ruim binnen de norm en
er zijn geen sjabloonzinnen of regeltaal. Hardop-toets, drie zinnen die nog niet
natuurlijk klinken:

1. Regels 133–136: "Er is maar één recept nodig, de optimale positie bij kwadratisch nut, $w = \mu/(\gamma s)$, en in matrixvorm $\boldsymbol{\theta} = …$. De theorie leidt die formule als eerste af."
   → "We hebben één formule nodig, de optimale positie bij kwadratisch nut, $w = \mu/(\gamma s)$, of in matrixvorm $\boldsymbol{\theta} = …$, en die leidt de theorie straks als eerste af."
2. Regel 471: "De matrix is $K\times K$ en bevat weinig ruisende rendementen, in plaats van de $N\times N$-matrix van [](#01-04-markowitz)."
   → "De matrix die de regel inverteert, is maar $K\times K$ en bevat rendementen waaruit de ruis grotendeels is weggemiddeld, terwijl Markowitz de $N\times N$-matrix van [](#01-04-markowitz) inverteert."
3. Regels 282–284: "Een vaste mix over vaste reeksen kiezen is het probleem van Markowitz, en als de regel elke toestand apart kan behandelen, verliest de belegger daar niets bij."
   → "Een vaste mix van vaste reeksen kiezen is precies het probleem van Markowitz, en zolang de regel elke toestand apart kan behandelen, kost die omweg de belegger niets."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Getallencontrole: de vijf nieuwe rijen 2003–2026 (SR 0,62/0,72; CE 0,9/6,6; 14/23; long-only 0,64/4,3; size/momentum 0,65/0,74), long-only-omzet 1,37, en premie 0,03% tegen 0,54% (12/√500 ≈ 0,537) kloppen met nb_outputs resp. de tekst. Geen niet-herleidbaar getal.

| punt | status |
|---|---|
| Feit 1 (r. 925 "in de buurt") | opgelost: tekens, size gelijk, B/M stijgt, momentum zakt |
| Feit 2 (toy b "onbeperkt") | opgelost |
| Feit 3 (GSC "industriespecifieke") | opgelost |
| Feit 4 (bijschrift "niet meer over nul") | opgelost, bewering weg |
| Verbetering 1 (long-only benoemd, r. 471, γ, overrendement) | opgelost |
| Verbetering 2 (tabel 2003–2026) | opgelost; alinea draagt alleen nog het oordeel |
| Verbetering 3 (Woodbury, AR(1)) | grotendeels: Woodbury in proza; AR(1) alleen als commentaar, geen zichtbare lus |
| Opbouw (1/N als markt, premies in "Wat het voorspelt") | opgelost |
| Toy (CRRA-bijzin, betekenis θ*) | opgelost |
| Oefening 2(2) eerste-ordevoorwaarde | opgelost |
| Hardop 1–3 | opgelost |
| `characteristic_panel`-zin | opgelost |
| Aanmerking notatie $R_{i,t+1}$ bruto (r. 370) | niet, klein |

Nieuwe punten: geen verslechtering, geen feitelijke fout. Open (klein): Woodbury-formule zelf staat niet uitgeschreven; "zakt het diepst" (CE) is niet in de tabel voor size/momentum gecontroleerd.

## Eindcijfer van record (F6c): 9,0

| criterium | gewicht | deelcijfer |
|---|---|---|
| 1 Helderheid van de uitleg | 25% | 9,0 |
| 2 Opbouw en rode draad | 20% | 9,0 |
| 3 Taal | 20% | 9,0 |
| 4 Toy-voorbeeld | 10% | 9,0 |
| 5 Code en figuren | 10% | 9,0 |
| 6 Replicatie en empirie | 10% | 9,0 |
| 7 Oefeningen | 5% | 9,0 |
| **gewogen** | | **9,0** |
