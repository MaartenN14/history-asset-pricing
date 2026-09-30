STATUS 04_19_momentum F6c words=5945 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,7 -> F6c 9,0.

# Eind-beoordeling 04_19_momentum

## Eerste herziening (workflow §12)

Eerste herziening; er is geen vorig cijfer. Gelezen: de volledige `.md`, de celuitvoer
(`$TEMP/F6-04_19_momentum-out.txt`), `notes/taal-04_19_momentum.md` en de relevante rijen
van `notes/feiten-04_19_momentum.md`. Drie slechtste WML-maanden apart nagerekend
(1932-08 −77,7%, 1932-07 −62,4%, 2009-04 −45,2%): het figuuronderschrift klopt.

Geen vakterm is door de taalredactie van betekenis veranderd. "12-1-regel" en "prior 12-2"
staan bewust naast elkaar en de alias wordt één keer uitgelegd (r. 218-220); "spreiding",
"onderreactie" en "overreactie" houden in theorie, simulatie en figuur dezelfde betekenis;
"bear market" is één keer gedefinieerd (r. 465-466, 966-968) en daarna vast.

## De drie verbeteringen met het meeste effect

1. **Januari-cijfers en het JT-signaal rechtzetten** (r. 222-223, 239-242, 820-821). De
   −7% in januari en 1,66% daarbuiten horen niet bij de 12/3-strategie van 1,31% per
   maand: (−7 + 11 · 1,66)/12 ≈ 0,94%, en dat is het gemiddelde van de 6/6-strategie. Noem
   de strategie en tabel bij die twee getallen, of zeg dat ze bij de 6/6-strategie horen.
   Jegadeesh en Titman sloegen in tabel I bovendien geen maand over (panel A) of één week
   (panel B), niet de maand $t$ uit [](#eq-momentum-signaal). Verwacht: helderheid 9,0,
   replicatie 9,0.
2. **Replicatie-oordelen scherper aan de verwachte afwijking koppelen** (r. 755-758,
   818, 891, 1040-1045). Het verschil in $t$ (3,74 tegen 5,50) staat niet in de verwachte
   afwijking en wordt nergens uitgelegd; het oordeel bij Barroso en Santa-Clara begint niet
   met "Geslaagd"; de verklaring voor 11 in plaats van 14 slechtste maanden wordt als feit
   gebracht, terwijl ze niet is nagegaan. Verwacht: replicatie 9,0.
3. **Twee redeneerstappen in Theorie en Replicatie afmaken** (r. 386-387, 915-917,
   700-702). Waarom is $\sigma^2_\mu$ "lastiger uit te sluiten omdat ze altijd positief is"?
   Waarom levert een negatieve helling van rendement op voorspelde variantie méér op dan
   geval 1? En hoeveel ruiziger zijn echte WML-rendementen (het getal 0,47 procentpunt uit
   de JT-replicatie ligt klaar)? Verwacht: helderheid 9,0.

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
| | **gewogen eindcijfer** | | **8,7** (8,675) |

Taal staat op 8,5 en blokkeert dus niet; geen deelcijfer onder 8,5.

### 1. Helderheid van de uitleg (8,5)

*Goed.*
- Theorie > Waar komt momentumwinst vandaan: decompositie, factorcorollarium en de
  simulatiecel met 200 aandelen die de drie termen naast de gesimuleerde winst zet (5,81
  tegen 5,71 basispunten) en meteen zegt waarom de idiosyncratische term bijna negen keer
  zo groot is.
- Theorie > Waarom de bèta van WML na een crash negatief is: propositie, limiet met getal
  (1,05 bij decielen en $\sigma_\beta = 0{,}3$) en de terugkoppeling naar de −0,70 van het
  toy.
- Theorie > Schalen met volatiliteit: de drie gevallen krijgen elk een getal (57%, 83%,
  16% bij $s = 0{,}55$) en de tekst zegt meteen dat voorspelbare volatiliteit alleen geen
  verdubbeling geeft.

*Aanmerkingen.*
- Theorie > Constructie: "De winst viel buiten januari, want in januari verloor de
  strategie gemiddeld ongeveer 7%, terwijl ze in de andere maanden 1,66% verdiende."
  (r. 241-242). "De strategie" is de 12/3-strategie van de vorige zin, maar de getallen
  passen daar niet bij (zie Feitelijke fouten).
- Theorie > Waar komt momentumwinst vandaan: "De spreiding $\sigma^2_\mu$ is lastiger uit te
  sluiten, omdat ze altijd positief is, en daarvoor is de lange horizon nodig."
  (r. 386-387). De reden volgt niet uit "altijd positief"; het punt is dat spreiding en
  onderreactie op korte horizon hetzelfde teken voorspellen.
- Replicatie > Barroso-Santa-Clara: "Die negatieve helling is het tegendeel van geval 3 in
  {prf:ref}`cor-momentum-schalen`, en verklaart waarom de winst groter is dan in de andere
  twee gevallen." (r. 915-917). Het mechanisme (het optimale gewicht daalt sneller dan
  $1/\sigma_t^2$, dus schalen wint meer dan in geval 1) ontbreekt, en "de winst" is hier de
  stijging van de Sharpe-ratio, niet de momentumwinst van eerder.
- Theorie > Schalen: $q$ is de grens in [](#eq-momentum-schalen) en eerder het kwantiel
  $q_p$ en $q_{0{,}9,t}$ (r. 233, 432, 492); $p$ is fractie, fondsindex en kwantielniveau
  (r. 260, 425). Twee symbolen met drie betekenissen (H7).
- Simulatie: "Echte WML-rendementen zijn veel ruiziger." (r. 701-702). Geen getal (H4).

*Beter uitleggen.* De lezer krijgt niet mee waarom de spreidingsverklaring pas op lange
horizon te scheiden is (een zin over wat spreiding en onderreactie in jaar 1 allebei
voorspellen). Bij de BSC-uitkomst van 85% ontbreekt de brug naar de theorie: een
dalend $\mu_t$ bij hoge $\sigma_t$ valt buiten de drie gevallen en maakt schalen sterker
dan geval 1. Bij $\gamma_{ij}$ en $\mu_i$ ontbreekt een orde van grootte (r. 288-289,
bijvoorbeeld $\mu_i$ een halve procent per maand zoals in de simulatiecel).

*Voor een 9.* 04_19_momentum.md:241 (januari-getallen aan de goede strategie koppelen);
:386 (reden voor de lange horizon); :915 (mechanisme van de negatieve helling);
:492 (ander symbool voor $q$); :701 (getal bij "ruiziger", bijvoorbeeld de standaardfout
van 0,47 procentpunt uit r. 827).

### 2. Opbouw en rode draad (9,0)

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord (feit staat, verklaring ontbreekt, risico
  is voorspelbaar en schalen verdubbelt de Sharpe-ratio bijna).
- Intuïtie doet drie voorspellingen (omkering alleen bij overreactie, negatieve bèta na
  daling, hogere Sharpe-ratio bij schalen) die Theorie op r. 405-407, 467-468 en 559-563
  in gewone zinnen inlost.
- Simulatie toetst precies het corollarium over de lange horizon en eindigt met de
  kanttekening over 1982-1998 die in Wat er brak terugkomt. 5.654 woorden.

*Aanmerkingen.*
- Theorie > Samengevat: "De simulatie vraagt of 25 jaar data van 500 aandelen, gevolgd tot
  vijf jaar na vorming, spreiding, onderreactie en overreactie uit elkaar houden."
  (r. 589-590). Dit is een vooruitblik, geen samenvatting van Theorie.
- Toy-voorbeeld en Simulatie delen geen getallen: de simulatie kalibreert op 8%/6%
  nieuws/ruis en 30% vertraging, niet op iets uit het toy (H11, klein).

*Beter uitleggen.* Niets wezenlijks; de rode draad (sortering, drie bronnen, lange horizon,
risico van de strategie) is na lezen in één zin te benoemen.

### 3. Taal (8,5)

*Goed.*
- Intuïtie en Overzicht lezen als gesproken Nederlands, met voegwoorden in plaats van
  knippen; gemiddelde zinslengte 17,8, geen zin boven 40.
- Motiefnamen elk hoogstens twee keer ("de standaardfout van 2%" r. 566 en 829, beide met
  een zin die zegt wat het hier betekent); geen regeltaal gevonden.
- Geen u/je, één stopwoord, geen calques.

*Aanmerkingen.*
- Replicatie > Jegadeesh-Titman: "De FF3-alpha is met 1,69% per maand hoger, omdat WML
  negatief laadt op SMB en HML, want de winnaars waren in deze periode vaker grote
  groeiaandelen." (r. 789-790). "Omdat ... want" stapelt twee redenen.
- Replicatie > Daniel-Moskowitz: "Dat hier 11 in plaats van 14 van de slechtste maanden na
  een bear market vallen, komt doordat de data van French de rangorde van die maanden iets
  anders leggen dan de CRSP-decielen." (r. 1042-1045). "De rangorde leggen" is geen
  Nederlands, en de zin is lang en zwaar vooraan.
- Simulatie, figuurtitel: "Drie werelden met momentum, maar maar één met omkering"
  (r. 677). Hardop klinkt "maar maar" als een tikfout.
- Overzicht: "Omdat geen evenwichtsmodel momentum voorspelde, is het in dit tijdvak het
  zuiverste geval van theorie of feit, een gemeten regelmaat die nog op een verklaring
  wacht." (r. 61-63). Stijf; de bijstelling na de komma hangt los.
- `prose_stats` meldt acht alinea's van één zin (para_one = 8), onder meer r. 731-732,
  811-813, 1053.

*Beter uitleggen.* Niet van toepassing.

*Voor een 9.* 04_19_momentum.md:789, :1042, :677 (zie de hardop-toets hieronder) en :61;
de losse eenzinsalinea's bij r. 731 en 811 aan de volgende alinea hangen.

### 4. Toy-voorbeeld (9,0)

*Goed.*
- Toy-voorbeeld: vier aandelen, elf maanden, in vijf minuten met de hand na te rekenen
  (33,1%, 8,9%, −19,0%, −10,9%; WML 5%); tabel hand/code klopt tot op drie decimalen.
- De slotzin zegt wat het getal betekent (−14% komt alleen uit de sortering) en geeft het
  spiegelgeval (+0,70 na een stijging).
- De −0,70 komt terug in Theorie (r. 443-444) en de overgeslagen maand in oefening 1.

*Aanmerkingen.*
- Toy-voorbeeld: "Neem nu vier andere aandelen zonder bedrijfsnieuws, met bèta's $0{,}5$,
  $0{,}8$, $1{,}2$ en $1{,}5$." (r. 146-147). Tweede, los voorbeeld met andere aandelen;
  de openingszin (r. 108-109) bindt het als één mechanisme, maar de lezer rekent twee
  toy's.

*Beter uitleggen.* Niets wezenlijks.

### 5. Code en figuren (8,5)

*Goed.*
- Simulatie: `simulate_panel` en `wml_event_returns` lezen als de beschrijving
  (responsvector met onderreactie en overschrijding, 12-1-signaal uit cumulatieve sommen).
- Figuren in Simulatie en BSC krijgen vooraf waarop te letten (stippellijn bij maand 12,
  crashes) en een onderschrift dat zegt wat te zien is.

*Aanmerkingen.*
- Replicatie (intro): `print(hap_data.french_tables("6_Portfolios_ME_Prior_12_2")[["title",
  "nobs"]].head(2).to_string())` (r. 727). De uitvoer (twee tabeltitels met 1195
  waarnemingen) wordt nergens besproken.
- Replicatie > Daniel-Moskowitz: "De figuur zet elke maand uit als punt, met de bear
  markets apart gekleurd." (r. 1053). Geen aanwijzing waarop te letten (de knik bij nul in
  de rode wolk).
- Replicatie > Daniel-Moskowitz: `np.expm1(np.log1p(market).rolling(24).sum()).shift(1)`
  (r. 1000) is een compacte truc voor het cumulatieve tweejaarsrendement, terwijl r. 989
  hetzelfde met `(1 + ...).prod() - 1` doet.

*Voor een 9.* 04_19_momentum.md:727 (print weg of bespreken), :1053 (waarop te letten),
:1000 (dezelfde schrijfwijze als r. 989 of een benoemd tussenresultaat).

### 6. Replicatie en empirie (8,5)

*Goed.*
- Drie replicaties met admonition, elk met een verwachte afwijking die vooraf een teken of
  bandbreedte noemt.
- Barroso-Santa-Clara: tabel hier/artikel naast elkaar, plus tot 2026, en een
  vervolgregressie die de extra winst verklaart.
- Jegadeesh-Titman: de standaardfout na 1999 (0,47 procentpunt) wordt uitgerekend en aan
  de moeilijkheid van een gemiddelde gekoppeld.

*Aanmerkingen.*
- Replicatie > Jegadeesh-Titman, tabel: "januari 1965–1989 (% per maand) | ongeveer −7 |
  −5,26" en "overige maanden 1965–1989 (% per maand) | 1,66 | 1,93" (r. 820-821). De
  originele kolom mengt twee strategieën (12/3 en 6/6).
- Replicatie > Jegadeesh-Titman: "$t$-waarde 1965–1989 | 3,74 | 5,50" (r. 818). Het
  verschil staat niet in de verwachte afwijking en wordt niet besproken.
- Replicatie > Barroso-Santa-Clara: "Ook deze replicatie slaagt." (r. 891). Het oordeel
  begint niet met Geslaagd / Gedeeltelijk / Niet geslaagd.
- Replicatie > Barroso-Santa-Clara: "Ook het gemiddelde gewicht van 0,90 klopt" (r. 893-894).
  Er staat niet waarmee het klopt; het artikelgetal staat niet in de tabel.
- Replicatie > Daniel-Moskowitz: de verklaring voor 11 tegen 14 (r. 1042-1045) is
  onbewezen, en het verschil (11 tegen 14, −1,41 tegen −1,51) stond niet in de verwachte
  afwijking; "Geslaagd" is daarmee ruim.

*Voor een 9.* 04_19_momentum.md:820 (juiste strategie in de originele kolom), :755
(verschil in $t$ door NW-standaardfouten en $K = 1$ aankondigen), :891 (oordeelwoord
vooraan), :893 (artikelgetal noemen), :1042 (verklaring als vermoeden brengen of
"Gedeeltelijk" op de telling).

### 7. Oefeningen (9,0)

*Goed.*
- Instap (12-0-regel op het toy), afleiding (halve limiet van de bèta met Monte Carlo) en
  uitbreiding van de replicatie (drie schalingsregels, ook voor UMD): precies de drie
  soorten.
- Elke uitwerking eindigt met wat ze leert (r. 1157-1160, 1209-1210, 1258-1260).

*Aanmerkingen.*
- Oefening "Welke schaling?", uitwerking: "De keuze van $c$ gebruikt de hele steekproef,
  maar een constante schaalfactor verandert Sharpe-ratio en scheefheid niet, en alleen de
  drawdown hangt ervan af." (r. 1256-1258). Voor regel 3 (plafond op 2) klopt dat niet: de
  afkapping volgt na de schaling met $c$, dus $c$ bepaalt hoe vaak het plafond bindt en
  daarmee ook Sharpe-ratio en scheefheid.

*Beter uitleggen.* Niets wezenlijks naast het punt hierboven.

## Feitelijke fouten

1. **Januari-effect bij de verkeerde strategie** (r. 239-242, 820-821). De −7% in januari
   en 1,66% daarbuiten geven samen (−7 + 11 · 1,66)/12 ≈ 0,94% per maand, niet de 1,31% van
   12/3. Ze horen bij de 6/6-strategie van Jegadeesh en Titman (gemiddeld ongeveer 0,95%).
   Feitenbestand rij 4 noteerde al "welke J/K-strategie ... niet vastgesteld" (onzeker);
   de rekensom maakt de toeschrijving aan 12/3 onjuist.
2. **Signaal van Jegadeesh en Titman** (r. 222-223). "Zij sorteerden ... op
   [](#eq-momentum-signaal)", maar die vergelijking slaat maand $t$ over; het 12/3-getal
   van 1,31% (tabel I, panel A) komt uit een sortering zonder overgeslagen periode (panel
   B slaat één week over). Klein, maar de tekst schrijft de 12-1-conventie van French aan
   hen toe.
3. **Uitwerking oefening "Welke schaling?"** (r. 1256-1258): constante $c$ is niet
   neutraal voor de regel met plafond (zie criterium 7).
4. **Onzeker: oorzaak van 11 tegen 14** (r. 1042-1045). Als feit gebracht, niet
   nagegaan; kan ook door het verschil tussen de bear-definitie hier (Mkt-RF + RF uit
   French) en die van Daniel en Moskowitz komen.

Nagerekend en juist: toy (signalen, WML 5%, bèta −0,70, −14%), 12-0-oefening (11,08%,
13,4%, −15,35%, 0%), decompositiesimulatie (5,81 tegen 5,71, binnen 1,6 standaardfout;
verhouding 4,99/0,58 ≈ 8,6), bètalimiet 1,053 en halve limiet 0,64, −0,36 bij $F = −0{,}4$,
schaalfactoren $e^{3s^2/2}$, $e^{2s^2}$, $e^{s^2/2}$ en 1,574/1,831/1,163 bij $s = 0{,}55$,
spreidingswereld 12% per jaar tegen CAPM 0,3 · 6% = 1,8%, JT-tabel (1,33; 5,50; 1,11; 1,75;
−5,26; 1,93; 1,69), standaardfout 0,54/1,16 ≈ 0,47, BSC (0,54→1,00, 85%, gewicht 0,90,
$R^2$ 0,368/0,016, $t = −1{,}94$), DM-episodes en bèta's, −0,85/1,66 in en buiten bear
markets, drie slechtste WML-maanden (1932-08, 1932-07, 2009-04) als in het onderschrift.

## Navertelling in vijf zinnen

Winnaars kopen en verliezers verkopen verdiende sinds 1965 ongeveer een procent per maand,
en het driefactormodel maakt dat raadsel groter in plaats van kleiner. Die winst kan uit
spreiding in verwachte rendementen, onderreactie of overreactie komen, en alleen de
rendementen twee tot vijf jaar na vorming scheiden die drie, waarbij de omkering na 1982
zwak is. Omdat de sortering na een marktdaling op lage bèta selecteert, krijgt WML dan een
negatieve bèta die in een herstel extra negatief wordt, wat de crashes van 1932 en 2009
verklaart. Die crashes komen in perioden van hoge momentumvolatiliteit, dus schalen naar
een vaste doelvolatiliteit verdubbelt ongeveer de Sharpe-ratio, meer dan de theorie bij
constant verwacht rendement belooft, omdat het verwachte rendement dan ook daalt. De data
beslissen niet tussen risico en vergissing. Dit valt samen met het Overzicht.

## Taal na de redactie

De redactie heeft het college natuurlijker gemaakt: de Intuïtie en Theorie lezen vlot, de
motiefnamen zijn geen handelend onderwerp meer en de getallenzinnen in Simulatie zijn
gesplitst met de conclusie vooraan. Geen vakterm is van betekenis veranderd. Wat rest zijn
enkele zinnen in Replicatie en een figuurtitel. Hardop-toets, drie zinnen:

1. r. 789-790: "De FF3-alpha is met 1,69% per maand hoger, omdat WML negatief laadt op SMB
   en HML, want de winnaars waren in deze periode vaker grote groeiaandelen."
   Herschrijving: "De FF3-alpha is met 1,69% per maand zelfs hoger. De winnaars waren in
   deze periode vaker grote groeiaandelen, zodat WML negatief laadt op SMB en HML."
2. r. 1042-1045: "Dat hier 11 in plaats van 14 van de slechtste maanden na een bear market
   vallen, komt doordat de data van French de rangorde van die maanden iets anders leggen
   dan de CRSP-decielen."
   Herschrijving: "Van de vijftien slechtste maanden vallen er hier 11 na een bear market,
   tegen 14 bij Daniel en Moskowitz, waarschijnlijk omdat de decielen van French die
   maanden iets anders rangschikken dan die van CRSP."
3. r. 677: "Drie werelden met momentum, maar maar één met omkering"
   Herschrijving: "Drie werelden met momentum, maar slechts één met omkering".

Bij volledige oplossing van alle punten: 9,0 (alle zeven deelcijfers op 9,0)

## Controle 1

**Feitelijke fouten (F6).**
1. Januari-effect bij verkeerde strategie: opgelost. −7%/1,66% staan nu expliciet bij de
   6/6-strategie (≈0,95%, geciteerd), tabel toont (12/3)/(6/6) per getal (r. 244-246,
   830-837).
2. JT-signaal: opgelost. De tekst zegt nu dat JT maand $t$ niet oversloegen, expliciet
   in tegenstelling tot [](#eq-momentum-signaal) (r. 224-226).
3. Oefening "Welke schaling?": opgelost. $c$ is neutraal voor regel 2, niet voor regel 3
   (plafond bindt, kleine look-ahead) (r. 1277-1281).
4. DM 11 tegen 14: opgelost. Nu als vermoeden met twee mogelijke oorzaken (rangschikking
   French/CRSP, bear-definitie); oordeel "Minder goed klopt de telling" (r. 1060-1065).

**Drie verbeteringen met het meeste effect.**
1. Januari/JT-signaal (zie feitelijke fouten 1-2): opgelost.
2. Replicatie-oordelen scherper: opgelost. Het verschil in $t$ (3,74 tegen 5,50) staat nu
   in de verwachte afwijking (NW, $K=1$, r. 771-772) en wordt besproken (r. 841-842);
   BSC-oordeel begint met "Geslaagd" (r. 908); 11-tegen-14 als vermoeden gebracht.
3. Twee redeneerstappen afgemaakt: opgelost. Reden lange horizon (r. 392-394: spreiding
   en onderreactie voorspellen in jaar 1 hetzelfde); mechanisme negatieve helling
   (r. 932-935: optimaal gewicht daalt sneller dan $1/\sigma_t^2$); "ruiziger" heeft nu
   een getal (r. 710-712: 0,06-0,09 tegen 0,47 procentpunt).

**Overige "Voor een 9"-punten.**
- Helderheid :492 ($q$ in eq-momentum-schalen vervangen door $\bar g$): opgelost.
- Taal :789, :1042 (hardop-zinnen herschreven), :677 ("slechts één"), :61 (Overzicht):
  opgelost. Eenzinsalinea's r. 731 en 811 aangevuld met inhoud: opgelost.
- Code en figuren :727 (print verwijderd), :1053 (knik van de rode wolk bij nul benoemd),
  :1000 (market_24m als benoemd tussenresultaat): opgelost.
- Replicatie :820 (strategie-labels in de tabel), :893 (gewicht 0,90 niet meer als
  "klopt", nu uitgelegd als gemiddelde blootstelling): opgelost.
- Toy (Aanmerking, niet in de "Voor een 9"-lijst): stap 4-5 gebruiken nu dezelfde
  aandelen A-D zonder nieuws (r. 146-151); verbetert ook H11.

**Nieuwe punten:** geen. De getallencontrole tegen
`$TEMP/F6c-04_19_momentum-out.txt` bevestigt elk aangepast of nieuw geciteerd getal:
1,33/5,50 (gelijkgewogen 1965-1989), 1,11/1,75 (1990-1998), −5,26/1,93 (januari/overig),
FF3-alpha 1,69, 0,54/1,16≈0,47, BSC 0,54→1,00 en gewicht 0,90, $R^2$ 0,368/0,016 met
$t=-1{,}94$, DM-episodes 239,1/30,8/−91,6/158,5/7,2/−73,8, bèta's −0,70/−1,41 met
$t$-verschil 2,1, 11 van de 15 slechtste maanden, en −0,85/1,66 in/buiten bear markets.
Geen niet-herleidbaar getal aangetroffen.

**Deels (blijft staan, stond niet in de "Voor een 9"-lijst):** $p$ blijft fondsindex in
Carhart en fractie in de bètapropositie.

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
| | **gewogen eindcijfer** | | **9,0** |

Geen deelcijfer onder 8,5; taal op 9,0 blokkeert niet. Plafond (§11.3) bereikt: dit is het
cijfer dat de eindbeoordelaar in het vooruitzicht stelde "bij volledige oplossing van alle
punten".
