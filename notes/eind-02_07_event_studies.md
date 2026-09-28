STATUS 02_07_event_studies F6c words=5443 prose=PASS open=0 cijfer=9,0 min=9,0

# Ronde 9+

Vorige ronde: 8,9

Eindbeoordeling F6 met verse ogen van `lectures/02_07_event_studies.md` (De event study),
na de taalredactie. Gewichten van ronde 9+: helderheid 25, opbouw 20, taal 20, toy 10,
code en figuren 10, replicatie 10, oefeningen 5. `prose_stats --check`: PASS (5323 woorden,
zinnen gemiddeld 17,7, één zin boven 40, twee "Wie"-openingen, motief 0).

Het lagere cijfer tegenover de vorige ronde (8,9) komt niet door de taalredactie. Die heeft
het college vloeiender gemaakt. Het komt door de strengere lat: §11.12 laat regeltaal en
werkmeldingen nu meetellen, en taal weegt 20% in plaats van 15%.

## De drie verbeteringen met het meeste effect

1. **Regeltaal en werkmeldingen uit de lopende tekst halen, en de ene zin boven 40 woorden
   splitsen** (taal 8,5 → 9,0). Het gaat om "openden het tijdvak" (r. 57), "de theorie
   leidt deze formule als eerste af" (r. 165), "Volgens de notatietabel" (r. 260), de
   melding dat FFJR niet te verifiëren was (r. 767–768 en 771–772), "de voorwaarden uit de
   verwachte afwijking" (r. 971) en "laat "Wat er brak" open" (r. 981). De zin van 45
   woorden staat op r. 522–524.
2. **De tegenspraak tussen simulatie en oefening 3 oplossen** (helderheid 8,5 → 9,0). Op
   r. 739–740 is de simulatie "optimistischer dan echte rendementen", maar oefening 3
   (r. 1144–1149) vindt op onze echte data juist meer kracht (69% tegen 63%). Wat verschilt,
   is de steekproef: Brown en Warner trokken willekeurige aandelen, wij nemen grote aandelen
   met 1,8% residuele volatiliteit. Maak daarnaast de factor 0,95 op r. 523–524 precies
   (die geldt voor de variantie, de standaarddeviatie krimpt met $\sqrt{0{,}95} \approx 0{,}97$).
   Definieer de halfwaardetijd ook bij het eerste gebruik (r. 110) en niet pas op r. 475.
3. **Replicatie: het oordeel in eigen woorden en de kanttekeningen in de tabel**
   (replicatie 8,5 → 9,0). Schrijf "vonden" in plaats van "voorspelden" (r. 962). Schrap de
   werkmelding (zie punt 1), laat het oordeel op r. 971 zeggen welke drie verwachtingen
   uitkomen, en zet KP 4,47 en $\hat{\bar\rho}$ als kolom of rij in de tabel in plaats van
   in de derde kanttekening (r. 996–998).

Na alle drie: 9,0·0,25 + 9,0·0,20 + 9,0·0,20 + 9,0·0,10 + 9,0·0,10 + 9,0·0,10 + 9,0·0,05 = 9,0.

## Eindcijfer: 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9,0 |

8,5·0,25 + 9·0,20 + 8,5·0,20 + 9·0,10 + 9·0,10 + 8,5·0,10 + 9·0,05 = 2,125 + 1,8 + 1,7 +
0,9 + 0,9 + 0,85 + 0,45 = 8,725 → **8,7**. Laagste deelcijfer 8,5. Taal ≥ 8, dus niet
blokkerend. Het doel (≥ 9,0, geen deelcijfer onder 8,5) wordt nog niet gehaald.

## 1. Helderheid van de uitleg (8,5)

*Goed*
- **Het kernresultaat.** De propositie benoemt haar termen ("fout in $\hat\alpha_i$",
  "fout in $\hat\beta_{i,m}$"), en r. 402–405 geeft er getallen bij (8% bij $L_2 = 21$,
  50% bij het jaarvenster van de replicatie).
- **Wat het voorspelt.** Elke formule heeft een getal: $\delta = 2{,}24$ en 61%, 1,29 en
  25% (r. 468–470), en MacKinlay's 0,965% met $J_1 = 9{,}28$ (r. 432–434).
- **Hoe het faalt: de lange horizon.** Het verschil tussen modelfout en schattingsfout
  staat al in de intuïtie (r. 103–107), en de theorie maakt het concreet met 0,17 tegenover
  2,7 (r. 553–554).

*Aanmerkingen*
- **Simulatie.** "tegen hun 80,4% op echte data, zodat de simulatie optimistischer is dan
  echte rendementen." (r. 739–740). Oefening 3 vindt het omgekeerde: "Per saldo wint de
  lagere gemiddelde volatiliteit, met 69% tegen 63%." (r. 1148–1149).
- **Hoe het faalt: events op dezelfde dag.** "en die is volgens de tweede formule van de
  propositie een factor $1 - \bar\rho$ te klein, bij $\bar\rho = 0{,}05$ dus 0,95 keer de
  waarde zonder correlatie." (r. 523–524). Het woord "spreiding" roept een
  standaarddeviatie op, terwijl de factor voor de variantie geldt.
- **Intuïtie.** "Volgens Santa-Clara, die de latere literatuur samenvat, ging de
  halfwaardetijd van nieuws van dagen in 1969 via uren in 2000 naar seconden nu" (r. 110–111).
  De term staat hier zonder uitleg, want de definitie volgt pas op r. 475–476.
- **Toy-voorbeeld.** "De twee extra termen zijn de fout in de geschatte $\hat\alpha_i$ en
  $\hat\beta_{i,m}$" (r. 164–165). Het recept met vijf symbolen staat vóór elke afleiding
  [onderzoek C, D2]. De rubriek staat één niet-afgeleide formule toe, maar een zin die zegt
  waarom de $\alpha$-term met $L_2^2$ groeit, ontbreekt hier. De theorie geeft die uitleg
  pas op r. 297–300.

*Beter uitleggen*
- Het verschil tussen de 94,7% van de simulatie en de 80,4% van Brown en Warner vraagt een
  reden (hun steekproef bestond uit willekeurige, volatielere aandelen) en niet een
  algemene uitspraak over "echte rendementen".
- Bij de BMP-alinea helpt één getal voor de $t$-waarde zelf: bij $N = 50$ en
  $\bar\rho = 0{,}05$ is BMP $1{,}86/\sqrt{0{,}95} \approx 1{,}91$ keer te breed verdeeld.
- De halfwaardetijd heeft bij de eerste vermelding een bijzin nodig ("de tijd waarin de
  helft van de reactie binnen is").

*Voor een 9*
- Herschrijf r. 739–740, zodat het verschil wordt toegeschreven aan de steekproef van
  Brown en Warner en niet aan echte data in het algemeen. Dan klopt het met r. 1144–1149
  (lectures/02_07_event_studies.md:739).
- Schrijf op r. 523–524 "variantie" in plaats van "spreiding", of geef de factor voor de
  standaarddeviatie (lectures/02_07_event_studies.md:523).
- Definieer de halfwaardetijd op r. 110 in de zin zelf (lectures/02_07_event_studies.md:110).
- Voeg op r. 164–165 in één bijzin het mechanisme toe (dezelfde fout op elke eventdag, dus
  $L_2$ keer geteld) en schrap in ruil daarvoor de verwijzing naar de theorie
  (lectures/02_07_event_studies.md:164) [onderzoek C, D2].

## 2. Opbouw en rode draad (9,0)

*Goed*
- **Overzicht.** De vraag staat in de eerste zin en het antwoord in de derde ("Zo gemeten
  verwerken prijzen publiek nieuws snel, en grotendeels al vóór de publicatie."). De vier
  bullets volgen de volgorde van het college.
- **Toy-getallen lopen door.** De factor 4,9 tegen 3 keert terug in Theorie (r. 373–374) en
  in de simulatie (r. 695–696, 63% tegen 0,4%). Het CAAR van 2% keert terug als effect in
  de krachttabel (r. 693–694).
- **Theorie.** Een routekaart (r. 243–247), "Samengevat" aan het eind, en 5323 woorden,
  ruim onder de 6.000.

*Aanmerkingen*
- **Intuïtie.** "Een toets vindt een effect van 1% met enkele tientallen events als de dag
  bekend is, maar niet als het venster weken beslaat." (r. 120–122). Deze voorspelling staat
  in dezelfde alinea als de voorspelling over de splitsing, dus twee verwachtingen over
  verschillende onderwerpen in één alinea [onderzoek C, D3].
- **Overzicht.** "waar een *modelfout* (een verkeerd model voor het normale rendement) zich
  opstapelt;" (r. 48). De bijzin lijkt bij beide faalplekken te horen, maar geldt alleen
  voor de lange horizon.

*Beter uitleggen*
- De intuïtie belooft een stijging "vóór en rond de aankondiging" (r. 119), terwijl de
  replicatie rond de ex-datum meet. De tweede kanttekening (r. 993–995) lost dat op, maar
  een halve zin in de intuïtie kan al zeggen dat we de aankondiging niet zien.

## 3. Taal (8,5)

*Goed*
- **Intuïtie.** De alinea's over de splitsing (r. 71–81) lezen als gesproken Nederlands, met
  verband door "Toch", "dus" en "want".
- **Wat er brak.** De twee lezingen van de drift (r. 1020–1027) zijn helder en idiomatisch,
  en "Daar wreekt de joint hypothesis zich" (r. 1015–1016) is een natuurlijke wending.
- Motiefnamen staan binnen de grens: "de standaardfout van 2%" twee keer (r. 96, 978),
  "theorie of feit" één keer en "Risico of vergissing?" één keer, en nergens als handelend
  onderwerp.

*Aanmerkingen*
- **Overzicht.** "Twee artikelen openden het tijdvak." (r. 57). "Tijdvak" is projecttaal
  (STYLE §11.12).
- **Toy-voorbeeld.** "en de theorie leidt deze formule als eerste af." (r. 165). Dit is een
  ingeplakte reparatiezin met de sectie als handelend onderwerp.
- **Opzet: eventtijd en het marktmodel.** "Volgens de notatietabel is $r_{i,\tau}$ het netto
  rendement, zonder de risicovrije rente af te trekken, waar {cite:t}`MacKinlay1997` $R$
  schrijft." (r. 259–261). "De notatietabel" is een verwijzing naar het werk, en de bijzin
  "waar MacKinlay $R$ schrijft" hangt los achteraan.
- **Replicatie.** "Het niveau vergelijken we niet, omdat de waarden van FFJR hier niet
  geverifieerd zijn." (r. 767–768) en "Omdat de exacte waarden uit tabel 2 van FFJR niet in
  een toegankelijke bron te controleren zijn, vergelijken we de vorm." (r. 771–772). Dit zijn
  meldingen over het werk, die §11.12 uit de tekst weert, en ze staan er twee keer.
- **Replicatie.** "Alle drie de voorwaarden uit de verwachte afwijking kloppen" (r. 971).
  Dit is regeltaal, want het kopje van de admonition wordt als bron aangehaald [onderzoek C].
- **Replicatie.** "Of zo'n fout plausibel is, laat "Wat er brak" open." (r. 981). Een
  sectienaam is hier handelend onderwerp.
- **Hoe het faalt: events op dezelfde dag.** "BMP lost het probleem niet op, want de
  noemer van die toets is de spreiding in de doorsnede, en die is volgens de tweede formule
  van de propositie een factor $1 - \bar\rho$ te klein, bij $\bar\rho = 0{,}05$ dus 0,95
  keer de waarde zonder correlatie." (r. 522–524). Deze zin heeft 45 woorden, de enige
  boven 40.
- **Simulatie.** "Wie de eventdag kent, heeft dus een scherp instrument, maar een
  onderzoeker die hem alleen op een week nauwkeurig kent, heeft vijf keer zoveel events
  nodig." (r. 740–741). De twee persona's in één zin maken de vergelijking zwaar
  [onderzoek C].
- **Opzet: eventtijd en het marktmodel.** "(hier een intercept op netto rendementen, geen
  pricing error of Jensen-alpha)" (r. 279). "Pricing error" staat onvertaald in de lopende
  tekst.

*Beter uitleggen*
- De alinea op r. 96–101 bevat tien getallen (6%, 0,024%, 1%, 0,024, 1%, 2%, 0,5, twintig,
  vierhonderd, 440). Dat is ruim boven de drie per alinea [onderzoek C]. Het getal voor de
  standaardfout kan in de eerste alinea blijven en de verhouding in de tweede.

*Voor een 9*
- r. 57: "Twee artikelen zetten de toon." of "Twee artikelen begonnen deze periode." (lectures/02_07_event_studies.md:57).
- r. 165: schrap de verwijzing naar de theorie en zeg wat de termen doen (lectures/02_07_event_studies.md:165).
- r. 259–261: "We schrijven $r_{i,\tau}$ voor het netto rendement, zonder aftrek van de
  risicovrije rente; MacKinlay schrijft daarvoor $R$." Het liefst zonder puntkomma, als twee
  zinnen (lectures/02_07_event_studies.md:259).
- r. 767–768 en 771–772: zeg één keer, in het replicatieblok, dat we de vorm vergelijken
  omdat FFJR alleen een figuur geven, of laat de reden weg. De melding over controleerbaarheid
  hoort in het rapport (lectures/02_07_event_studies.md:767, :771).
- r. 971: "De drie verwachtingen komen uit: …" of het oordeel direct formuleren
  (lectures/02_07_event_studies.md:971) [onderzoek C].
- r. 981: "Of zo'n fout plausibel is, is de vraag van de volgende sectie."
  (lectures/02_07_event_studies.md:981).
- r. 522–524: splits na "de spreiding in de doorsnede"
  (lectures/02_07_event_studies.md:522).
- r. 740–741: "Met een bekende eventdag is de toets dus scherp. Is de dag maar op een week
  bekend, dan zijn vijf keer zoveel events nodig." (lectures/02_07_event_studies.md:740)
  [onderzoek C].

## 4. Toy-voorbeeld (9,0)

*Goed*
- **Stap 1 tot 5.** Alle getallen zijn met de hand na te rekenen. $\hat\mu_m = 0$ maakt OLS
  triviaal, en de tabel met $\sum r_i$, $\sum r_m r_i$ en residuen laat geen stap weg.
- De tabel hand/code (r. 229–233) en de slotzin met de les ("28% te hoog", r. 238–239).
- Eén mechanisme, namelijk dat schattingsfout ruis toevoegt die de naïeve toets mist.

*Aanmerkingen*
- **Het recept.** Het recept is de enige nog niet afgeleide formule en staat vóór de vijf
  stappen (r. 154–165). Dat mag, maar het maakt het toy zwaarder dan vijf minuten
  [onderzoek C, D2].

*Beter uitleggen*
- Bij stap 4 kan één bijzin zeggen welke term het meest toevoegt (9/5, de fout in
  $\hat\alpha$, omdat $L_2^2/L_1$ bij een schattingsvenster van vijf dagen groot is).

## 5. Code en figuren (9,0)

*Goed*
- **Toy-cel.** De code volgt de vijf stappen met commentaar per stap en benoemde
  tussenresultaten (`factor`, `var_car`, `var_naive`).
- **Simulatie.** `simulate_events` en `j1_test` lezen als de formules, met `factor` gelijk
  aan het recept, en de leeswijzer vóór de figuur (r. 698–699) zegt waarop te letten.
- **Replicatie.** `car_variance` is de matrixvorm van de propositie en wordt zo benoemd
  (r. 850).

*Aanmerkingen*
- **Replicatie.** De regel `pd.DataFrame({"CAAR": caar_path, "SE": se_path}, index=pd.Index(tau, name="tau")).loc[[-121, -1, 0, 60]].round(4)`
  (r. 893) is één lange ketting van meer dan 120 tekens.
- **Replicatie.** "In de figuur gaat het om twee hellingen, die vóór dag 0 en die erna."
  (r. 896). Het bijschrift (r. 920–923) zegt hetzelfde nog eens, zodat de leeswijzer dubbel
  staat [onderzoek C, D4, grotendeels opgelost].

*Beter uitleggen*
- De gewogen correlatie in `split_tests` (r. 944–950) is de moeilijkste regel code. De zin
  ervoor (r. 926–929) zegt wat er gebeurt, maar een getal (typisch overlapaandeel) zou helpen.

## 6. Replicatie en empirie (8,5)

*Goed*
- **Replicatieblok.** Bron, wat, data, verschil en verwachte afwijking staan er in ongeveer
  170 woorden, met de selectie achteraf als eerlijk benoemde vertekening (r. 761–763).
- **Tabel.** Origineel, verwachting en uitkomst staan naast elkaar (r. 965–969), en het
  oordeel begint met **Geslaagd**.
- De $-2{,}9\%$ na de splitsing wordt niet weggepoetst, maar gekoppeld aan de lange-horizonformule
  (r. 979–981) en aan de drift in "Wat er brak".

*Aanmerkingen*
- **Replicatie.** "De tabel heeft de vorm die FFJR voorspelden." (r. 962). FFJR vonden deze
  vorm, ze voorspelden hem niet [onderzoek C].
- **Replicatie.** "Het niveau vergelijken we niet, omdat de waarden van FFJR hier niet
  geverifieerd zijn." (r. 767–768). Dit is een werkmelding in plaats van een verwachte
  afwijking (zie taal).
- **Replicatie.** "Kolari-Pynnönen verlaagt de $t$-waarde over het jaar vooraf daarom maar
  van 4,74 (BMP) naar 4,47." (r. 997–998). Getallen die in de tabel horen, staan hier in
  lopende tekst.

*Beter uitleggen*
- De vergelijking met FFJR is kwalitatief ("stijgt gestaag"). Eén getal uit hun tekst, of
  de expliciete zin dat hun figuur de maatstaf is, maakt de kolom "FFJR" steviger.

*Voor een 9*
- r. 962: "vonden" in plaats van "voorspelden" (lectures/02_07_event_studies.md:962) [onderzoek C].
- r. 767–768: vervang de werkmelding door een inhoudelijke verwachting, bijvoorbeeld een
  hoger niveau door de selectie achteraf (lectures/02_07_event_studies.md:767).
- r. 996–998: zet KP en $\hat{\bar\rho}$ als rij of kolom in de vergelijkingstabel
  (lectures/02_07_event_studies.md:996).

## 7. Oefeningen (9,0)

*Goed*
- Instap (eendaags venster op het toy), afleiding (constant-mean en het werkelijke
  significantieniveau) en uitbreiding van de replicatie (Brown en Warner op echte data):
  precies de drie soorten die de rubriek vraagt.
- Elke uitwerking eindigt met een les (r. 1066–1067, 1104–1105, 1149–1150).

*Aanmerkingen*
- **Oefening 3.** "De conclusie van Brown en Warner hangt dus niet af van de
  simulatieaannames." (r. 1149–1150). Dit is ruimer dan één steekproef van twintig events
  met grote aandelen kan dragen, en het botst met r. 739–740 (zie helderheid).

*Beter uitleggen*
- Oefening 2 kan in één zin zeggen dat $L_1 = 60$ bij beursintroducties voorkomt. Dat
  staat er (r. 1102–1103), dus hier is niets nodig.

## Feitelijke fouten

1. **r. 739–740**: "zodat de simulatie optimistischer is dan echte rendementen". Dit is
   onjuist als algemene uitspraak. Oefening 3 vindt op de echte data van dit college 69%
   kracht tegen 63% in de simulatie (r. 1145–1149). Het verschil met Brown en Warner (80,4%
   tegen 94,7% bij $N = 50$) komt door hun steekproef, niet door echte rendementen als
   zodanig. Correctie: "tegen hun 80,4% voor willekeurig gekozen, volatielere aandelen".

Nagerekend en juist:
- Toy: $\hat\alpha$ en $\hat\beta$ (0,1 en 1,0; 0 en 0,5; 0,2 en 1,5), residuen en
  $\hat\sigma^2$ (1/3; 0,5; 1/3), AR's en CAR's (2,5; 2,0; 1,5), CAAR 2,0, factor 4,9,
  varianties 1,6333 en 2,45, $J_1 = 2{,}509$, naïef 3,207, dus 28% te hoog.
- Intuïtie: 6%/250 = 0,024%, verhouding 0,5/0,024 ≈ 21, $21^2 \approx 440$, en
  $20\%/\sqrt{100} = 2$ procentpunt.
- Theorie: 21/250 ≈ 8%, 250/500 = 50%, $\delta = 2{,}24$ met kracht 61%, $\delta = 1{,}29$
  met 25%, $\sqrt{3{,}45} = 1{,}86$ en $2\Phi(-1{,}055) = 29\%$, 0,02% × 750 = 15%, en
  $\E[J_1] = 0{,}17$ en 2,7.
- Simulatie: 62,9% tegen 61%, gemist in vier van de vijf bij [−10,+10] en $N = 100$
  (formule: $\delta = 1{,}09$, kracht 19%), simulatieruis 1,4 procentpunt, 63% en 0,4%.
- Replicatie: 102 splitsingen, 50 aandelen, 6183 dagen, $L_1$ 495, bèta 1,08, 1,8%, CAAR
  14,9% (SE 3,7), $J_1$ 4,0, BMP 4,7, KP 4,47, en $\eta = -2{,}9\%/61 \approx -0{,}05\%$ per
  dag ≈ −12% per jaar ("ruim 10%").
- Oefeningen: factor 1,3, varianties 0,4333 en 0,65, gemiddelde 1,9, $J_1 = 4{,}628$, en
  het significantieniveau bij $L_1 = 60$ is $2\Phi(-1{,}96/\sqrt{1{,}35}) \approx 9{,}2\%$
  ("bijna twee keer te vaak").

Getallen die uit celuitvoer komen (6183, 495, 1,08, 14,9%, 4,74/4,47, 69%) zijn gecontroleerd
op onderlinge samenhang in de tekst. De celuitvoer zelf is niet opnieuw gedraaid.

## Navertelling in vijf zinnen

1. Een event study legt gebeurtenissen op tijd nul, trekt het normale rendement volgens een
   geschat marktmodel af en middelt de rest, zodat de ruis met de wortel van het aantal
   events krimpt en het signaal blijft.
2. De variantie van een CAR is de ruis van de eventdagen plus de fout in de geschatte
   alpha en bèta. Wie die schattingsfout vergeet, rekent met te hoge $t$-waarden, vooral bij
   lange vensters en korte schattingsperioden.
3. De toets $J_1$ vindt een effect van 1% met enkele tientallen events als de dag bekend
   is, maar een langer venster kost evenredig veel events, zoals de simulatie in de lijn
   van Brown en Warner bevestigt.
4. De toets faalt bij events op dezelfde dag, omdat gedeelde ruis niet wegmiddelt, en over
   lange horizonnen, omdat een kleine modelfout lineair groeit en de ruis alleen met de
   wortel, zodat lange event studies het model meten.
5. Op 102 recente splitsingen herhaalt het patroon van FFJR zich (een stijging vóór de
   ex-datum, niets op de dag zelf en geen significante drift daarna), maar of de drift
   risico of vergissing is, kan de event study zelf niet beslissen.

Deze navertelling komt overeen met het Overzicht.

## De taal na de redactie

De redactie heeft gewerkt. Zinnen lopen door met voegwoorden, de dubbele punten als lijm
zijn verdwenen, "Waarom zou dit waar zijn?" staat nog maar twee keer in Theorie, en de
meeste punten uit onderzoek C zijn opgelost (r. 100, 243, 431, 816, 926, 977–979, 1016).
Wat overblijft, is regeltaal en werkmelding (r. 57, 165, 260, 767, 771, 971, 981), plus
één te lange zin. Dat is het verschil tussen 8,5 en 9.

Hardop-toets: drie zinnen die nog niet natuurlijk klinken.

1. r. 26–27: "Elke toets daarvan toetst tegelijk een model voor het "normale" rendement,
   en die koppeling heet de *joint hypothesis* (gezamenlijke hypothese)."
   Herschrijving: "Een toets van die theorie is altijd ook een toets van een model voor het
   "normale" rendement, en die koppeling heet de *joint hypothesis* (gezamenlijke hypothese)."
2. r. 99–100: "Een premie van 6% per jaar is per dag 0,024%, tegen een dagelijkse marktruis
   van 1%, een verhouding van 0,024 tussen signaal en ruis."
   Herschrijving: "Een premie van 6% per jaar is 0,024% per dag, en tegen een dagelijkse
   marktruis van 1% geeft dat een verhouding tussen signaal en ruis van 0,024."
3. r. 164–165: "De twee extra termen zijn de fout in de geschatte $\hat\alpha_i$ en
   $\hat\beta_{i,m}$, en de theorie leidt deze formule als eerste af."
   Herschrijving: "De twee extra termen komen van de fout in de geschatte $\hat\alpha_i$ en
   $\hat\beta_{i,m}$, die op elke dag van het eventvenster dezelfde is en daardoor zwaarder
   telt naarmate het venster langer is."

## Controle 1

Controle van record (F6c, ronde 9+) op `notes/rapport-02_07_event_studies.md`, sectie
"R9-1". Getallencontrole met `uv run python tools/nb_outputs.py
lectures/02_07_event_studies.ipynb`: de vergelijkingstabel (r. 1009-1013) klopt exact met
de celuitvoer van `split_tests` — [-250,-1] CAAR 0,1493/SE 0,0373/$J_1$ 4,0024/BMP
4,7388/$\hat{\bar\rho}$ 0,0012/KP 4,4678; [0,0] -0,0008/-0,3994/0,0000/0,0544; [0,60]
-0,0292/0,0159/-1,8369/-1,1846/0,0003/-1,1641. Ook `fit_table` (L1 495,0; bèta 1,078;
sigma 0,018) en 6183 handelsdagen komen overeen. De handberekeningen 1,86 en 1,91 (r.
545-553) staan niet in de celuitvoer maar rekenen kloppend na uit de tekst zelf:
$\sqrt{1+49\times0{,}05}=\sqrt{3{,}45}=1{,}86$ en $1{,}86/\sqrt{0{,}95}\approx1{,}91$.

**Feitelijke fout** — opgelost. De simulatie-alinea (was r. 739-740) zegt nu dat het
verschil met Brown en Warner in hun steekproef van willekeurig gekozen, volatielere
aandelen zit, niet in "echte rendementen" in het algemeen; dat klopt nu met oefening 3
("... en die verklaart ook waarom Brown en Warner met willekeurige aandelen minder vonden
dan onze simulatie.").

**De drie verbeteringen**
1. Regeltaal, werkmeldingen, zin > 40 woorden — opgelost. r. 57, 165, 260, 767-768,
   771-772, 971, 981 zijn herschreven zoals voorgesteld, en de BMP-zin is gesplitst
   (`prose_stats --check`: sent_gt40 = 0, 5443 woorden, PASS).
2. Tegenspraak simulatie/oefening 3, factor 0,95, halfwaardetijd — opgelost. Het
   steekproefverschil is benoemd, "spreiding" is "variantie" geworden met de expliciete
   factor voor de $t$-waarde (1,86 → 1,91), en de halfwaardetijd is gedefinieerd bij het
   eerste gebruik.
3. Replicatie-oordeel in eigen woorden en kanttekeningen in de tabel — opgelost.
   "vonden" in plaats van "voorspelden", het oordeel noemt de drie verwachtingen, en
   $\hat{\bar\rho}$ en KP staan als kolom in de vergelijkingstabel.

**Voor een 9, per criterium**
- Helderheid: alle vier punten opgelost (feitelijke fout, "spreiding" → "variantie",
  halfwaardetijd bij r. 110, mechanismezin bij r. 164-165).
- Taal: alle acht punten opgelost (r. 57, 165, 259-261, 767-768/771-772, 971, 981,
  522-524, 740-741), plus "pricing error" vertaald naar "afwijking van een
  evenwichtsmodel".
- Replicatie: alle drie punten opgelost (r. 962, 767-768, 996-998).

**Overige aanmerkingen/beter uitleggen (geen plafond, ter info)**
- Opbouw: de modelfout-bijzin in het Overzicht hoort nu alleen bij de lange horizon, en de
  twee voorspellingen in de intuïtie (toetskracht, splitsing) staan niet meer in dezelfde
  alinea — opgelost.
- Code: de lange ketting (r. 893) is gesplitst in `caar_table = ...` en een tweede regel,
  en de leeswijzer vóór de CAAR-figuur herhaalt het bijschrift niet meer — opgelost.
- Taal, beter uitleggen (tien getallen in één alinea, r. 106-110): **niet opgelost**. Het
  rapport meldt een knip in twee alinea's, maar de tekst staat nog altijd in één alinea
  met dezelfde tien getallen (6%, 0,024%, 1%, 0,024, 1%, 2%, 0,5, twintig, vierhonderd,
  440). Geen "Voor een 9"-punt, dus geen plafondeffect, maar wel nog open voor een
  volgende ronde.
- Replicatie, beter uitleggen (kwalitatieve FFJR-vergelijking): deels. Alleen de zin dat
  hun figuur de maatstaf is voor de vorm, is toegevoegd; geen getal uit hun tekst.

**Verslechtering of nieuwe feitelijke fout**: geen gevonden.

### Eindcijfer: 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |

9,0 × 1,00 = **9,0**. Laagste deelcijfer 9,0, ruim boven 8,5. Taal 9,0, dus niet
blokkerend. Het doel (eindcijfer ≥ 9,0, geen deelcijfer onder 8,5) is gehaald.
