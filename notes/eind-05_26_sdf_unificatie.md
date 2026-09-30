STATUS 05_26_sdf_unificatie F6c words=5725 prose=PASS open=1 cijfer=9,1 min=9,0

**Eindcijfer van record: 9,1** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,8 -> F6c 9,1.

## Eerste herziening (workflow §12)

Eerste herziening; er is geen vorig cijfer. `prose_stats --check`: PASS (5.542 woorden,
zinnen gemiddeld 15,8, p90 25, geen zin > 40, alinea gemiddeld 47, 6 alinea's van één zin,
1 sjabloon, 0 "Wie"-zinnen). Motiefnamen elk één keer (:60, :863, :1176). `open=3`: twee
feitelijke onnauwkeurigheden en één symboolbotsing die een formule dubbelzinnig maakt
(hieronder). Alle overige getallen in de proza komen overeen met de celuitvoer; de
handstappen van het toy-voorbeeld en de bèta-illustratie (:406–428) zijn nagerekend en
kloppen.

Termcontrole na de taalredactie: "mean-variance-frontier" wordt op :300 één keer vertaald
als "minimum-variantierand, met bij elk gemiddelde de kleinste variantie". Dat is de juiste
betekenis (beide takken, niet alleen de efficiënte grens), en Stelling 2 ("$R$ ligt op de
frontier dan en slechts dan als $n = 0$") is met die betekenis correct. Geen vakterm is
door de redactie van betekenis veranderd.

## De drie verbeteringen met het meeste effect

1. **De symboolbotsing $\gamma$/$\beta$ en de twee onnauwkeurigheden herstellen**
   (helderheid 8,5 → 9,0). (a) :373 definieert $\gamma = \E[R^{*2}]/\E[R^*]$ (en :382
   bewijst $\gamma = R^f$), maar de tabel op :502 zegt voor het consumptie-CAPM
   "$b = \gamma$, $a$ uit $\beta$ en $R^f$", waar $\gamma$ de risicoaversie en $\beta$ de
   tijdsvoorkeur is, en :1047, :1061, :1071, :1096 en :1105 gebruiken $\gamma = 10$ en
   $\gamma = 15$ weer als risicoaversie. Een lezer die de tabel naast het corollarium legt,
   leest "$b = R^f$". Geef het corollarium een ander symbool (bijvoorbeeld $\gamma_0$ of
   direct $R^f$ met de voetnoot "als $\mathbf 1 \in \underline X$") en noem op :502 wat
   $\gamma$ en $\beta$ daar zijn. (b) :1319–1320 "de 23 procentpunt die UMD toevoegt":
   de puntschatting is 0,758 − 0,496 = 0,26 (de zin ervoor noemt 0,50 en 0,76); 0,230 is
   de bootstrapmediaan. (c) :1096–1097 "terwijl de factor-SDF's die ruim halen": de
   CAPM-SDF haalt 0,492 tegen een marktsharpe van 0,466, dus nauwelijks.
2. **Vijf stroeve zinnen herschrijven** (taal 8,5 → 9,0): :90–93, :476–478, :515, :862–864
   en :1268 (zie Taal en de hardop-toets). Tegelijk de bronregels die na de redactie
   halverwege afbreken opnieuw wrappen met `tools/rewrap.py` (:68–72, :78, :201–202,
   :216, :225–226, :237–239, :300–306, :440–441, :493, :509, :516–519, :550, :599–600,
   :609, :656, :970–971, :992–993, :999–1000, :1062, :1104, :1162, :1177–1185); dat
   verandert het gerenderde college niet, maar houdt de bron leesbaar.
3. **Twee sprongen in de uitleg dichten** (helderheid, samen met punt 1 naar 9,0–9,5):
   :302–304 (waarom het kortste element $x^*$ het rendement met het kleinste tweede
   moment geeft: $R^* = x^*/\E[x^{*2}]$ en elk rendement heeft $\E[x^*R] = 1$, dus
   Cauchy-Schwarz) en :666–667 (waarom de ruisbodem bij $\sqrt{(N-K)/T}$ ligt: als
   $\mathbf S \approx \mathbf G$ zijn de $N-K$ gewichten ongeveer één, zodat
   $\E[T\hat\delta^2] \approx N - K$). Telkens een bijzin in de bestaande zin, geen nieuwe
   alinea.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,8

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **gewogen** | | **8,8** (8,825) |

### 1. Helderheid van de uitleg: 8,5

*Goed*
- Toy-voorbeeld en Theorie delen één object: $x^* = (0{,}75;\ 0{,}95;\ 1{,}15)$ keert terug
  als gewichten $(1{,}35;\ -0{,}40)$ onder Stelling 1 (:263–264), als
  $\underline X^\perp$ = veelvouden van $\varepsilon$ (:291–293) en als uitgerekende
  bèta-representatie met $-2{,}5625 \cdot (-0{,}022821) = 0{,}0585$ (:406–428). H4 en H11
  zijn hier voorbeeldig.
- Elke bewijsstap heeft een kop die zegt wat hij oplevert ("Uniciteit: het verschil heeft
  norm nul", "Stap 3: de frontier is $n = 0$"), en de aannames A1/A2 worden bij de stap
  genoemd die ze gebruikt (:272–274).
- De HJ-afstand krijgt een getal naast de formule: 0,3 in maanddata is 1,5% per maand bij
  5% volatiliteit (:653–655); de ruisbodem krijgt 0,2 voor 35 portefeuilles en 757 maanden.

*Aanmerkingen*
- Stelling 2, corollarium (:373): "Definieer $\gamma = \E[R^{*2}]/\E[R^*]$." tegenover
  Stelling 3, tabel (:502): "$b = \gamma$, $a$ uit $\beta$ en $R^f$". Twee betekenissen van
  $\gamma$ (en $\beta$ naast de bèta's) in één college (H7).
- Stelling 2 (:365–367): "want elke frontierportefeuille combineert twee vaste fondsen,
  hier het rendement van de SDF en de richting die het gemiddelde verhoogt." $R^{e*}$ is
  een overrendement, geen fonds; de lezer die de twee-fondsenstelling van Markowitz kent,
  zoekt een tweede rendement.
- Stelling 2 (:302–304): "Omdat $x^*$ het kortste element is dat alle prijzen goed geeft,
  heeft het rendement ervan het kleinste tweede moment van alle rendementen." Het
  "omdat" is niet te volgen zonder de normalisatie $p(R) = 1$.
- Stelling 4 (:666–667): "De ruisbodem ligt ongeveer bij $\sqrt{(N-K)/T}$" volgt niet uit
  de zin ervoor (gewogen som van $\chi^2(1)$) zonder de aanname dat de gewichten rond één
  liggen.
- Wat er brak (:1187): "Voor een belegger blijft de vraag van Santa-Clara" noemt Santa-Clara
  zonder één regel wie hij is of waar zijn les staat (H2).

*Beter uitleggen*
- Waarom $R^*$ een "verzekering" is (:406): één getal uit het toy (in toestand 3, de slechte
  toestand voor het aandeel, keert $R^*$ 1,2466 uit) maakt het woord concreet.
- De correctieterm in $\mathbf h_t$ (:585–594): een halve zin over hoe groot die correctie is
  (klein, omdat $\bar{\mathbf R}^e$ klein is ten opzichte van de rendementen) helpt de lezer
  te beslissen of hij ertoe doet.

*Voor een 9*
- lectures/05_26_sdf_unificatie.md:373 en :502: $\gamma$ en $\beta$ ontdubbelen.
- :302–304 en :666–667: de twee sprongen met een bijzin dichten.
- :365–367: "twee vaste fondsen" vervangen door "$R^*$ en een fonds dat $R^{e*}$ bij
  $R^*$ optelt", of de fondsen correct benoemen.
- :1319–1320 en :1096–1097: zie Feitelijke fouten.

### 2. Opbouw en rode draad: 9,0

*Goed*
- Het Overzicht stelt de vraag en geeft meteen het antwoord ("Nee, want elk model is een
  keuze voor ... $m$", :37–40); de routekaart op :207–211 en Samengevat op :682–697
  omsluiten Theorie.
- De twee voorspellingen van de Intuïtie (:88–93) worden ingelost: de eerste bij het toy
  (:199–200), de tweede bij de propositie over $b$ en $\lambda$ (:548–550), en de replicatie
  toont hetzelfde patroon op HML (:1134–1141).
- De dropdown over de HJ-afstand door toeval (:868–908) verbindt de ruisbodem uit Stelling 4
  met de replicatie, en "Wat er brak" gebruikt de eigen replicatiegetallen.

*Aanmerkingen*
- Simulatie (:703–720): de kalibratie komt niet uit het toy; alleen de rol van $u$ als
  "$\varepsilon$ uit het toy-voorbeeld" legt het verband. Dat is verdedigbaar (een
  drietoestandseconomie kan geen GMM dragen), maar H11 wordt maar half ingelost.
- Samengevat, laatste punt (:695–696): "De simulatie vraagt hoe vaak een overbodige factor
  ..." is een vooruitblik, geen resultaat van de Theorie.

*Beter uitleggen*
- Bij de GMM-sectie (:554) ontbreekt een zin die zegt waar de lezer die schatter straks
  terugziet (de simulatie en tabel (1)); nu komt hij als losse techniek binnen.

### 3. Taal: 8,5

*Goed*
- Het Overzicht en "Wat er brak" lezen als gesproken academisch Nederlands; zinnen als
  "Prijzen verklaren en prijzen begrijpen zijn zo twee verschillende projecten geworden."
  (:1173–1174) dragen de conclusie.
- Geen gedachtestreepjes, geen "Wie"-zinnen, motiefnamen elk één keer, weinig dubbele punten
  (4,3 per 1000 woorden).
- Het verband loopt via voegwoorden ("want", "terwijl", "zodat") in plaats van knippen.

*Aanmerkingen*
- Intuïtie (:90–93): "Ten tweede krijgt een factor die meebeweegt met een factor uit de
  discontofactor een premie, ook als hij er zelf niets aan toevoegt. Die premie stijgt met
  de samenhang, terwijl zijn eigen gewicht nul blijft" ("factor uit de discontofactor" is
  wringend; "zijn" volgt op "Die premie" en verwijst dus niet eenduidig, H8).
- Stelling 3 (:476–478): "hangt de premie van een factor af van alle gewichten in
  $\mathbf{b}$ samen, elk gewogen met de covariantie tussen die factor en de factor van het
  gewicht." (tongbreker).
- $b$ tegenover $\lambda$ (:515): "Premie en gewicht meten iets anders, en een voorbeeld
  laat zien wat."
- Simulatie (:862–864): "komt door de standaardfout van 2% in maandtermen" ("in
  maandtermen" is een calque; het motief staat als oorzaak waar de zin zelf de uitleg al
  geeft).
- Oefening 2 (:1268): "Het geschaalde model verlaagt de gemiddelde prijsfout nauwelijks"
  ("geschaald" is Cochranes *scaled factors*, hier niet ingevoerd; bedoeld is "het
  conditionele CAPM").
- Engels vakjargon "payoff", "frontier" en "mean-variance-frontier" staat naast Nederlandse
  omschrijvingen; consistent gebruikt, dus geen aftrek, maar "frontierportefeuille" (:366)
  en "frontier-rendement" (:55) zijn hybride.

*Beter uitleggen*
- Niet van toepassing buiten de genoemde zinnen.

*Voor een 9*
- lectures/05_26_sdf_unificatie.md:90–93, :476–478, :515, :862–864, :1268 herschrijven
  (herschrijvingen onder "Taal na de redactie").
- Bronregels opnieuw wrappen (zie verbetering 2).

### 4. Toy-voorbeeld: 9,5

*Goed*
- In vijf minuten met de hand na te rekenen: vijf stappen met koppen, $\mathbf G^{-1}$ met
  gehele getallen, controle van beide prijzen (:130–160).
- Eén mechanisme (projectie op de payoff-ruimte), tabel hand/code (:191–196) en een slotzin
  die zegt wat het getal betekent en waarom de optieprijs niet vastligt (:199–203).
- Enige vooruitgegrepen formule is $\mathbf c = \mathbf G^{-1}\mathbf p$, en die wordt
  expliciet aangekondigd (:127–128).

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Stap 5 (:157–160): $\sigma(x^*)/\E[x^*] = 0{,}1489$ krijgt pas op :428 zijn betekenis
  (de Sharpe-ratio van het aandeel); een halve zin hier ("dit is straks de HJ-grens")
  sluit de lus eerder.

### 5. Code en figuren: 9,0

*Goed*
- `linear_sdf_gmm` volgt de wiskunde regel voor regel (`C`, `estimate`, `spectral` als
  $\mathbf h_t$ uit :589–591), met een docstring die de normalisatie noemt.
- Elke cel heeft een aankondiging en een lees-zin; beide figuren hebben een leeswijzer
  vooraf (:833, :1063–1064) en een onderschrift dat zegt wat te zien is.
- Het toy telt met `assert` na dat $\varepsilon$ loodrecht staat en de bèta-vorm klopt (:189).

*Aanmerkingen*
- Replicatie (2), cel op :1047 en :1072: de consumptie-SDF staat twee keer hard als
  `10 * 0.036` en `0.36`; één benoemde variabele houdt tabel en figuur gelijk.
- Dezelfde cel: de indexnaam "HJ-grens: 35 portefeuilles + 4 factoren (binnen de
  steekproef)" wordt in de uitvoer afgekapt ("(binnen..."), zodat de tabel een halve
  rijnaam toont.

*Beter uitleggen*
- Bij `CHI2_DRAWS[:, :N] @ weights` (:770) een commentaar dat de $p$-waarde van de
  HJ-afstand zo door simulatie ontstaat (:664–666 zegt het wel in de proza).

### 6. Replicatie en empirie: 9,0

*Goed*
- De admonition heeft bron, wat, data, verschil en verwachte afwijking in ruim 200 woorden;
  de verwachtingen zijn toetsbaar geformuleerd ($p < 0{,}01$, $t(b) > 2$, "boven 0,8 maar
  onder de grens").
- Tabel verwachting/hier (:1147–1153) en een oordeel dat met **Geslaagd** begint en naar
  de vijf verwachtingen verwijst.
- De $b$/$\lambda$-tabel met FF5+UMD laat het mechanisme van de propositie op echte data
  zien, inclusief het omgekeerde oordeel van Fama-MacBeth over CMA (:1142–1144).

*Aanmerkingen*
- Tabel (1) toelichting (:991–1001) en tabel (3) toelichting (:1134–1142) herhalen zes tot
  acht getallen in lopende tekst die al in de tabel en in de verwachtingentabel staan.
- De tabel vergelijkt met verwachtingen, niet met het origineel; waar het origineel een
  getal heeft (de HJ-afstanden van Hansen en Jagannathan, of de $t$-waarde van HML bij
  Fama en French 2015), ontbreekt het.

*Beter uitleggen*
- Waarom $J$ met FF3+UMD op de 25 portefeuilles alleen $p = 0{,}02$ geeft maar op 35
  weer $p = 0{,}00$: één zin dat momentum de toets strenger maakt.

### 7. Oefeningen: 9,0

*Goed*
- Instap op het toy (put met payoff $(0;\ 0;\ 0{,}5)$), een afleiding met uitbreiding
  (conditioneel CAPM) en een uitbreiding van de replicatie (Kan, Robotti en Shanken).
- Elke uitwerking eindigt met wat ze leert (:1229–1231, :1271–1273, :1322–1324).

*Aanmerkingen*
- Oplossing 3 (:1319–1320): "zodat de 23 procentpunt die UMD toevoegt" (zie Feitelijke
  fouten).
- Oplossing 2 (:1268): "Het geschaalde model" (zie Taal).

*Beter uitleggen*
- Oefening 2, deel 1 is een regel algebra; de afleiding kan ook vragen welke momenten er
  bijkomen ($\E[m\, z_t R^e]$), wat de koppeling met de note op :669–680 zichtbaar maakt.

## Feitelijke fouten

Nagerekend tegen `$TEMP/F6-05_26_sdf_unificatie-out.txt` en met de hand.

1. lectures/05_26_sdf_unificatie.md:1319–1320, "de 23 procentpunt die UMD toevoegt": de
   puntschattingen in dezelfde alinea zijn 0,496 en 0,758, een verschil van 26
   procentpunt; 0,230 is de bootstrapmediaan. Correctie: "de 26 procentpunt" of
   "de mediane 23 procentpunt in de bootstrap".
2. :1096–1097, "terwijl de factor-SDF's die ruim halen": de CAPM-SDF heeft 0,492 tegen een
   marktsharpe van 0,466, dus haalt hij hem nauwelijks; alleen FF3 (0,621) en FF3+UMD
   (1,036) halen hem ruim. Correctie: "terwijl de factor-SDF's die halen, FF3 en FF3+UMD
   ruim".
3. :373 tegenover :502 (en :1047, :1061, :1105): $\gamma$ is in het corollarium
   $\E[R^{*2}]/\E[R^*] = R^f$ en elders de risicoaversie. De tabelregel "$b = \gamma$" is
   daardoor letterlijk gelezen onjuist ($b = R^f$). Correctie: ander symbool in het
   corollarium.

Gecontroleerd en juist: alle toy-getallen (:130–160, :406–428, oplossing 1), $b \approx
(3{,}5;\ 0{,}65;\ 4{,}9)$ (:494), simulatie 6%, de helft, 4,4% (:829–832), correlatie
0,71 en $4{,}2/\sqrt{600} \approx 0{,}17$ (:719, :865), HJ-populatie 0,14 en mediaan 0,31
en een op de zes (:904–906), ruisbodem 0,20–0,21 bij $T = 757$, HJ 0,41/0,39/0,36, fout
0,264 → 0,124 met $t = 4{,}59$, SMB 0,32 tegen 0,19, SDF-volatiliteit 1,036 en grens 1,738,
minimum in 1976-01 en maximum in 2001-01, FF5+UMD $t$-waarden 3,08/2,72/0,68 en RMW 3,0,
oefening 2 ($J$ 127 → 55, $t(b_1) = 2{,}3$), $\gamma = 15$ en dertig procent rente
(03_13:1003–1004).

## Navertelling in vijf zinnen

1. Zodra prijzen lineair zijn (wet van één prijs), bestaat er precies één SDF $x^*$ die
   zelf een portefeuille is; alle andere SDF's zijn $x^*$ plus ruis die geen prijs raakt en
   hebben dus een hogere volatiliteit.
2. Het rendement $R^*$ van die SDF ligt op de minimum-variantierand, en daaruit volgt een
   bèta-representatie zonder evenwicht, zodat SDF, frontier en bèta drie vormen van
   hetzelfde zijn.
3. Een SDF die lineair is in factoren is een bèta-model met $\boldsymbol\lambda =
   \boldsymbol\Sigma_f\mathbf b$, zodat CAPM, consumptie-CAPM, APT en Fama-French alleen
   verschillen in wat er in $m$ mag staan, en een overbodige factor wel een premie maar
   geen gewicht krijgt.
4. GMM en de HJ-afstand meten hoe fout zo'n model is met één meetlat, maar de afstand heeft
   een ruisbodem rond $\sqrt{(N-K)/T}$ en de afstanden van CAPM, FF3 en FF3+UMD liggen
   dicht bij elkaar.
5. Een factor-SDF haalt de HJ-grens moeiteloos maar heeft geen economische betekenis,
   terwijl de consumptie-SDF die betekenis heeft maar de grens niet haalt; het raamwerk
   meet modellen, maar beslist niet tussen risico en vergissing.

Dat komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijk gemaakt: de staccato-reeksen zijn verdwenen, de
vaste etiketten ("Waarom zou dit waar zijn?") zijn vervangen en de enige termkeuze die
riskant was (frontier/minimum-variantierand) is juist gebleven. Wat overblijft zijn
enkele zinnen die de inhoud te dicht op elkaar stapelen, en veel bronregels die na de
redactie halverwege afbreken (niet zichtbaar in de gerenderde tekst).

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. :476–478 "Volgens [...] hangt de premie van een factor af van alle gewichten in
   $\mathbf{b}$ samen, elk gewogen met de covariantie tussen die factor en de factor van het
   gewicht."
   Herschrijving: "Volgens [...] is de premie van een factor een gewogen som van alle
   gewichten in $\mathbf b$, met als weging de covariantie van die factor met elk van de
   andere."
2. :90–93 "Ten tweede krijgt een factor die meebeweegt met een factor uit de
   discontofactor een premie, ook als hij er zelf niets aan toevoegt. Die premie stijgt met
   de samenhang, terwijl zijn eigen gewicht nul blijft, ..."
   Herschrijving: "Ten tweede krijgt een factor die meebeweegt met een van de factoren in
   de discontofactor een premie, ook als hij zelf niets toevoegt. Hoe sterker hij
   meebeweegt, hoe hoger die premie, terwijl zijn eigen gewicht nul blijft, ..."
3. :862–864 "Dat ze maar in de helft van de steekproeven significant is, komt door de
   standaardfout van 2% in maandtermen, want bij een factorvolatiliteit van 4,2% ..."
   Herschrijving: "Dat ze maar in de helft van de steekproeven significant is, is
   [de standaardfout van 2%](#00-01-rendementen) per maand uitgedrukt: bij een
   factorvolatiliteit van 4,2% ..."

Bij volledige oplossing van alle punten: 9,1

## Controle 1

Uitgangspunt: F6 8,8 (eindbeoordelaar, noemde 9,1 bij volledige oplossing). Getallencontrole tegen
`nb_outputs` van het notebook: de toegevoegde of gewijzigde getallen zijn herleidbaar (HJ 0,41 naar 0,36,
$p = 0{,}02$ op 25 portefeuilles en 0,00 op 35, SMB 0,32 tegen 0,19, SDF-volatiliteit 1,036, CAPM 0,492
tegen marktsharpe 0,466, bootstrapverschil 0,080 tot 0,418, $R^2$ 0,496 en 0,758 geeft 26 procentpunt,
ruisbodem 0,20 tot 0,21). Geen niet-herleidbaar getal.

**Feitelijke fouten.** (1) 26 procentpunt: opgelost. (2) "de factor-SDF's die halen, FF3 en FF3+UMD ruim":
opgelost. (3) $\gamma$ wordt $R^0$ in corollarium, bewijs en toy, en de tabelregel noemt risicoaversie
$\gamma$: opgelost, geen nieuwe botsing.

**Drie verbeteringen.** Alle drie opgelost: symbolen en fouten hersteld; vijf stroeve zinnen herschreven
(:86-89, :457-459, :494, :838-841, :1239 gelezen als natuurlijk; de bronregels zijn grotendeels gewrapt);
beide sprongen (:289-292 met Cauchy-Schwarz, :637-640 met $\E[T\hat\delta^2] \approx N-K$) met een bijzin
gedicht.

**Voor een 9, Aanmerkingen, Beter uitleggen.** Opgelost: twee-fondsen-zin, Santa-Clara met verwijzing,
"verzekering" concreet, correctieterm klein, toy stap 5 wijst naar de HJ-grens, GMM-sectie zegt waar de
schatter terugkomt, laatste punt Samengevat is een resultaat, kalibratie-uitleg simulatie, hybriden
vervangen, `sd_m_consumption` benoemd, rijnaam ingekort, commentaar bij de $p$-waarde, toelichtingen
tabel (1) en (3) ingekort, momentum-uitleg voor $p = 0{,}02$, oefening 2 deel 1 met momenten.
Deels: geen getallen uit de originele artikelen (afgewezen met verwijzing naar kaart §6, aanvaard).
Niet opgelost maar klein: het figuuronderschrift (:1070-1072) en oplossing 2 (:1239) hebben nog een
overlange bronregel (alleen bron, niet zichtbaar). Hardop-toets: de drie herschrijvingen klinken natuurlijk.
Verslechterd: niets.

## Eindcijfer van record (F6c): 9,1

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,2 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,5 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |
| | **gewogen** | | **9,1** (9,10) |
