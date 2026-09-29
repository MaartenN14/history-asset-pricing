STATUS 01_02_bachelier F6c words=5884 prose=PASS open=0 cijfer=9,0 min=9

**Eindcijfer van record: 9,0** (F6c). Verloop: Vorig: 8,6. Ronde 9+: T, F6 8,6 -> F6c 9,0. Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Ronde 9+

Vorige ronde: 8,6

Eindbeoordeling (F6) van `lectures/01_02_bachelier.md` na de taalredactie. Gelezen: de
.md één keer volledig; celuitvoer nagerekend door het college in een tijdelijke map uit
te voeren (`$TEMP/F6-01_02_bachelier-out.md`). `prose_stats --check`: PASS (5.824
woorden, zinnen gemiddeld 16,4, p90 27, dubbele punt 1,7 per 1000, twee "zinnen" boven 40
woorden, waarvan één de opsomming in het Overzicht).

## De drie verbeteringen met het meeste effect

1. **Het kernresultaat laten zeggen wat nieuw is aan Donsker** (helderheid 8,5 → 9). De
   beleggersalinea onder "Het kernresultaat" (lectures/01_02_bachelier.md:247–252) legt
   de centrale limietstelling uit (één maandrendement wordt normaal), terwijl het nieuwe
   aan Donsker het hele pad is, en dat komt pas in r. 282–284. De alinea hoort het pad en
   het maximum als voorbeeld te nemen, of weg te vallen. [onderzoek C, D1] Daarbij de
   twee verwijzingen met een onduidelijk "dat" (r. 493–494, r. 1334–1336) scherp maken.
2. **De zes zinnen uit de hardop-toets en de regeltaal herschrijven** (taal 8,5 → 9):
   r. 117–119, 238–239, 493–494, 556–558, 1000–1001 en 1334–1336 (zie het taaloordeel
   onderaan). Het gaat om herschrijven van bestaande zinnen, niet om zinnen erbij.
3. **Getallen uit de lopende tekst naar tabellen** (replicatie 8,5 → 9, opbouw helpt mee).
   Het oordeel van de Regnault-replicatie (r. 898–911) heeft negen getallen in één
   alinea, "Waar het breekt" (r. 1141–1150) zeven, de uitwerking van oefening 3
   (r. 1331–1336) vijf. [onderzoek C, D5] De getallen die het oordeel dragen staan al in
   de uitvoertabellen; de tekst kan ernaar wijzen en er één per bewering noemen.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,70 + 1,70 + 0,90 + 0,90 + 0,85 + 0,45 = 8,625, dus **8,6**; laagste
deelcijfer 8,5. De taalredactie heeft het ritme duidelijk verbeterd (geen telegramzinnen,
geen dubbele punten als lijm, motiefnamen binnen de grens), maar niet genoeg om taal naar
9 te tillen, en de inhoudelijke punten over Donsker en de getallendichtheid staan nog.
Doel (≥ 9,0, geen deelcijfer onder 8,5) niet gehaald; taal blokkeert niet (8,5 ≥ 8).

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- Symbolen krijgen naam, betekenis en orde van grootte: $\mu$ ongeveer 1% en $\sigma$
  ongeveer 5% per maand, $v$ als bedrag van ongeveer 20 euro bij een aandeel van 100
  (Opzet en aannames).
- Bij elke formule staat een getal: $\sqrt{8/\pi} \approx 1{,}60$ tegen 1,50 uit het toy
  (Het kernresultaat), 62% bij de verkooporder (raakkans), 7,98 euro (optieprijs),
  $VR(4) = 1{,}15$ bij $\rho_1 = 0{,}1$ (variance ratio).
- De aanname staat bij de stap: "De stelling vraagt wel meer dan de nulhypothese, namelijk
  onafhankelijke stappen met verwachting nul, en daarom trekt de replicatie eerst het
  gemiddelde af."

*Aanmerkingen*
- Het kernresultaat: "Neem een belegger die een aandeel een maand vasthoudt. Zijn
  maandrendement is de som van twintig dagrendementen." De alinea illustreert de centrale
  limietstelling, niet het invariantieprincipe.
- Bacheliers optieprijs: "In de formule staan geen risicoaversie en geen verwacht
  rendement, maar dat volgt hier alleen uit de aangenomen martingaalconditie." Waar "dat"
  naar wijst (het ontbreken, of de formule) is niet eenduidig (H8).
- Oefeningen, uitwerking 3: "Dat is [](#eq-bachelier-power) in omgekeerde richting, want
  de afwijking lijkt verdwenen, terwijl het verschil statistisch niet van nul te
  onderscheiden is." Wat "omgekeerde richting" betekent, moet de lezer zelf bedenken.
- Opzet en aannames: "$T$ het aantal waarnemingen, dat in [](#00-01-rendementen) nog $N$
  heette, terwijl $T$ daar het aantal jaren was." De notatiewissel is correct gemeld, maar
  de zin laat de lezer twee betekenissen van $T$ tegelijk vasthouden.
- Figuur bij de replicatie: "Links liggen de variance ratios die Lo en MacKinlay vonden
  boven één". Het paneel toont onze schatting op hun steekproef, niet hun getallen.

*Beter uitleggen*
- Het invariantieprincipe: de lezer moet meekrijgen waarom het *pad* ertoe doet vóór hij
  bij de raakkans komt. Een voorbeeld met het maximum van de wandeling (bijvoorbeeld de
  0,375 uit het toy naast de Brownse 62%) maakt het verschil met de centrale
  limietstelling zichtbaar.
- $z_2$ (Hoe het getoetst wordt): het woord "robuust" krijgt een reden, maar geen getal;
  één zin met hoeveel de gewone $z$ te hoog uitvalt, maakt het concreet.

*Voor een 9*
- lectures/01_02_bachelier.md:247–252: de beleggersalinea vervangen door een voorbeeld
  over het pad of het maximum, of schrappen; r. 282–284 zegt al wat nodig is. [onderzoek C]
- lectures/01_02_bachelier.md:493–494 en 1334–1336: het verwijswoord vervangen door het
  ding zelf.
- lectures/01_02_bachelier.md:238–239: de wissel van $T$ in twee heldere zinnen.
- lectures/01_02_bachelier.md:1124: "die Lo en MacKinlay vonden" wordt "op de steekproef
  van Lo en MacKinlay".

### 2. Opbouw en rode draad (8,5)

*Goed*
- Het Overzicht stelt de vraag en geeft het antwoord in de eerste twee zinnen, en de
  routekaart in Theorie zegt welke resultaten getoetst worden en welke niet.
- De intuïtie voorspelt drie dingen (wortelwet, optieprijs evenredig met spreiding,
  autocorrelaties nul) en elk wordt ingelost: r. 316–318, r. 491 en r. 1000.
- Toygetallen keren terug: 1,50 tegen 1,60 in Theorie, 0,375 bij de raakkans, de zestien
  paden in de instapoefening.

*Aanmerkingen*
- Intuïtie: "De theorie levert de evenredigheidsfactor, ongeveer 0,4." De tweede
  verwachting is een uitgewerkte uitkomst, geen voorspelling van teken of richting, en
  vraagt kennis die pas in Theorie komt.
- Lengte: 5.824 woorden, binnen de 6.000, maar 364 meer dan de vorige ronde, met vier
  resultaten en twee replicatieblokken. De aandacht wordt dun verdeeld over raakkans en
  optieprijs, die niet op data getoetst worden.

*Beter uitleggen*
- De raakkans staat tussen het kernresultaat en de optieprijs zonder dat de rest van het
  college haar gebruikt. Eén zin in de routekaart over waarom ze erin staat (het pad
  telt, dus Donsker is meer dan de centrale limietstelling) zou haar plaats verklaren.

*Voor een 9*
- lectures/01_02_bachelier.md:107–111: de optieverwachting inkorten tot richting en
  evenredigheid ("vier keer zo lang kost het dubbele"); de factor 0,4 hoort bij de
  stelling. [onderzoek C, D3]
- lectures/01_02_bachelier.md:1141–1150 en 898–911: minder getallen in lopende tekst,
  wat ook woorden scheelt. [onderzoek C, D5]

### 3. Taal (8,5)

*Goed*
- Het ritme is gesproken Nederlands: zinnen van gemiddeld 16 woorden met afwisseling,
  verband met "want", "zodat", "omdat" in plaats van knippen (Intuïtie, Theorie).
- Motiefnamen binnen de grens: "theorie of feit" één keer, "risico of vergissing" twee keer
  (waarvan één als kopverwijzing), "de standaardfout van 2%" één keer en daar met wat het
  hier betekent. Geen u/je, geen gedachtestreepjes, twee "Wie …"-zinnen.
- De vaste wending "zoals de intuïtie voorspelde" staat één keer (r. 491).

*Aanmerkingen*
- Toy-voorbeeld: "De cel hieronder laadt eerst alle pakketten, want verderop in het
  college staan geen imports meer." Regeltaal (STYLE §11.12 noemt "de imports-cel").
- Hoe het getoetst wordt: "De slotkoers van morgen is immers met een kleine fout te
  voorspellen, want die ligt dicht bij de koers van vandaag, maar de koers*verandering*
  van morgen is dat niet." Het slot "is dat niet" hangt los.
- Replicatie: "De verwachting uit de intuïtie, autocorrelaties van nul, houdt dus bijna
  stand, want de autocorrelaties zijn niet precies nul, maar wel te klein om mee te
  voorspellen." "Want" geeft een reden die de bewering tegenspreekt, en "de verwachting
  uit de intuïtie" als onderwerp klinkt als werkwijze.
- Het kernresultaat: "Donsker bewees het resultaat in 1951, maar de schets behandelt
  alleen de verdeling op vaste tijdstippen." Twee losse mededelingen met "maar" als lijm.
- Replicatieblok Regnault: "In zijn eigen toets (§83–84) geeft een maandafwijking van
  ongeveer 2,73 frank, maal $\sqrt{3}$ en $\sqrt{12}$, de waarden 4,73 en 9,46, tegen
  waargenomen ongeveer 4,74 en 9,50." Zes getallen in een zin met ingeschoven bepalingen.
- Plus de drie zinnen uit de hardop-toets onderaan.

*Beter uitleggen*
- Geen inhoudelijk punt; de taalpunten zijn herschrijvingen.

*Voor een 9*
- lectures/01_02_bachelier.md:117–119, 238–239, 493–494, 556–558, 1000–1001, 285–286,
  804–806 en 1334–1336 herschrijven, zonder zinnen toe te voegen. [onderzoek C: de
  voorstellen voor B:474 en B:239 zijn na de redactie nog niet overgenomen]
- lectures/01_02_bachelier.md:102: "Wat verwachten we dus?" plakt als losse vraag aan het
  eind van een alinea over Bachelier; een aankondigende zin in dezelfde gedachte past
  beter. [onderzoek C]

### 4. Toy-voorbeeld (9)

*Goed*
- Vier stappen, zestien paden, alles met de hand na te rekenen; de tabel hand/code is
  gelijk (nagerekend).
- Stap 3 en 4 laten zien dat de absolute afwijking schommelt (1; 1; 1,50; 1,50) terwijl de
  variantie meteen lineair is: een echte les, geen herhaling.
- De slotzin zegt wat het getal betekent.

*Aanmerkingen*
- Toy-voorbeeld, "Het recept": "Voor lange wandelingen nadert die verhouding
  $\sqrt{2/\pi} \approx 0{,}798$, en dat getal leidt de theorie als eerste af." De ene
  nog niet afgeleide formule die mag; wel wordt hetzelfde getal in Theorie opnieuw
  verteld. [onderzoek C, D2, grotendeels opgelost: Theorie verwijst nu met het toygetal]

*Beter uitleggen*
- Niets dat de lezer mist.

### 5. Code en figuren (9)

*Goed*
- Elke cel heeft een zin ervoor en erna; de figuren hebben een leeswijzer ervoor en een
  bijschrift dat zegt wat te zien is.
- De code leest als de wiskunde: `by_counting` naast `by_reflection`, `ar1_paths` met een
  zichtbare lus, `expected_z = rho * np.sqrt(T)` met commentaar, `compare()` per rij.

*Aanmerkingen*
- Toy-voorbeeld (tekst vóór de eerste cel): "De cel hieronder laadt eerst alle pakketten,
  want verderop in het college staan geen imports meer." Telt bij taal.
- Figuur van de paden: "die de rode krommen $\pm\sqrt{u}$ volgt". Een kleur in het
  bijschrift hangt af van het palet; "de getrokken krommen" is robuuster.

*Beter uitleggen*
- Niets dat de lezer mist.

### 6. Replicatie en empirie (8,5)

*Goed*
- Beide blokken hebben bron, wat, data, verschil en verwachte afwijking, met een
  falsifieerbare eis (factor twee; de rangorde van klein naar groot).
- De oordelen beginnen met Geslaagd / Gedeeltelijk geslaagd en verwijzen naar de
  verwachte afwijking; de ontleding van de 11,5% (twee derde autocorrelatie, een derde
  dikke staarten) klopt met de uitvoer.
- De tabel origineel/hier voor Kendall en Lo en MacKinlay.

*Aanmerkingen*
- Oordeel Regnault: "Regnaults overeenstemming van een half procent halen we niet, want
  voor French voorspelt de maandwaarde maal $\sqrt{12}$ een jaarwaarde die ruim tien
  procent te laag is." De alinea heeft negen getallen; de rubriek vraagt getallen in
  tabellen.
- Waar het breekt: "De week-$\rho_1$ van 0,030 vraagt $(1{,}96/0{,}030)^2 \approx 4270$
  weken, en onze 5223 weken volstaan net." Drie berekeningen in lopende tekst in een
  sectie die afsluit.

*Beter uitleggen*
- "Volstaan net" (r. 1148): bij $T^*$ is het onderscheidend vermogen 50% (r. 735); bij
  5223 weken is de verwachte $z$ ongeveer 2,2. Eén woord over wat "net" betekent, voorkomt
  dat de lezer denkt dat de afwijking zeker zichtbaar is.

*Voor een 9*
- lectures/01_02_bachelier.md:898–911: het oordeel met twee of drie getallen, de rest
  verwijst naar de tabellen. [onderzoek C, D5]
- lectures/01_02_bachelier.md:1141–1150: één getal per bewering.

### 7. Oefeningen (9)

*Goed*
- Instap (scheve munt, variatie op het toy), afleiding (AR(1) in gesloten vorm),
  uitbreiding van de replicatie (kwintielen na 1985): precies de drie soorten.
- Elke uitwerking eindigt met wat ze leert ("De $\sqrt{t}$-wet gaat dus over de spreiding
  rond de drift"; "Tegen een AR(1) is de kortste horizon dus de scherpste toets").

*Aanmerkingen*
- Uitwerking 3: "Dat is [](#eq-bachelier-power) in omgekeerde richting, want de afwijking
  lijkt verdwenen, terwijl het verschil statistisch niet van nul te onderscheiden is."
  (zie helderheid).

*Beter uitleggen*
- Niets dat de lezer mist.

## Feitelijke fouten

Geen. Nagerekend tegen de uitgevoerde cellen:
- toy: $\Var(S_n) = n$, $\E|S_n|$ = 1; 1; 1,5; 1,5, verhoudingen 1; 0,707; 0,866; 0,750;
  $\sqrt{8/\pi} = 1{,}596$ (6% boven 1,50); raakkans 0,375 (tabel); $2(1-\Phi(0{,}5)) = 61{,}7\%$;
- optietabel: hooguit 0,027 bij een maand, 0,336 bij een jaar en $K = 110$, 7,979 op het
  geld;
- Lo-MacKinlay-standaardfouten 0,029; 0,054; 0,085; 0,126; $T^*$ = 96, 1537, 9604 weken;
  simulatie 0,9998, 0,0281, 0,0287, 4,3%; afwijking bij vijf jaar hooguit 2,8 pp;
- Regnault: helling 0,511 en 0,577; French 0,0373 tot 0,0421; jaarverhouding 0,885;
  MAD/SD 0,705 en 0,734; ontleding twee derde / een derde; Shiller t/m 2026-09 (155 jaar);
- Kendall-tabel: maand-$\rho_1$ 0,0853 (significant), week-$\rho_1$ 0,0304, 5223 weken;
- VR: 1,066; 1,150; 1,219; 1,211 binnen 0,02 van Lo-MacKinlay; $z$ 1,22 tot 2,00; na 1985
  alle vier onder één en niet significant; interbellum het grootst; kwintielen 1,205
  tot 1,016, monotoon ook bij $q = 4$ en 8; $(1{,}96/0{,}205)^2 = 91$;
- oefeningen: 0,8 en 3,84; 24 stappen; 1,222; 1,42 bij $q=16$; $z$ 4,51 en 3,29; 1,143 en
  1,017, $z = 2{,}50$; $t$ hoogstens 1,28; verschillen 0,057 tot 0,096; 0,075.

Onnauwkeurig, geen fout: het bijschrift "Na 1985 liggen ze er net onder" (r. 1125) terwijl
$VR(16) = 0{,}871$. Niet na te gaan met de beschikbare bronnen: Kendalls "ongeveer 0,13" en
Regnaults 4,74 en 9,50.

## Navertelling in vijf zinnen

Regnault mat in 1863 dat de gemiddelde koersafwijking met de wortel van de tijd groeit, en
Bachelier gaf daar in 1900 een model voor: de random walk, die in de limiet een Brownse
beweging wordt. Uit dat model volgen de wortelwet met factor $\sqrt{2/\pi}$, een raakkans
die twee keer de eindkans is en een optie op het geld die ongeveer 0,4 keer de spreiding
waard is. De variance ratio bundelt kleine autocorrelaties tot één toets, maar een
autocorrelatie van een paar procent is pas na decennia data te zien. Op Amerikaanse data
houdt de wortelwet stand (helling 0,51), en de variance ratios van Lo en MacKinlay laten
zich repliceren, met een afwijking die groter is bij kleine aandelen en na 1985 verdwijnt.
Het model zegt niets over het niveau van de prijs, en of de afwijking een prijsfout of een
handelseffect was, is met gratis data niet te beslissen. Dat komt overeen met het
Overzicht.

## Taal na de redactie

De redactie heeft gewerkt: het college leest nu grotendeels als gesproken academisch
Nederlands, met voegwoorden waar eerder punten stonden en zonder zichtbare sjablonen. Wat
overblijft zijn losse zinnen waarin een verwijswoord of voegwoord de logica niet draagt,
en één regeltaalzin. Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. r. 238–239: "... en $T$ het aantal waarnemingen, dat in [](#00-01-rendementen) nog $N$
   heette, terwijl $T$ daar het aantal jaren was."
   → "... en $T$ het aantal waarnemingen. In [](#00-01-rendementen) heette dat aantal nog
   $N$ en stond $T$ voor het aantal jaren."
2. r. 493–494: "In de formule staan geen risicoaversie en geen verwacht rendement, maar dat
   volgt hier alleen uit de aangenomen martingaalconditie."
   → "Risicoaversie en verwacht rendement ontbreken in de formule, maar alleen omdat we de
   martingaalconditie hebben aangenomen."
3. r. 1000–1001: "De verwachting uit de intuïtie, autocorrelaties van nul, houdt dus bijna
   stand, want de autocorrelaties zijn niet precies nul, maar wel te klein om mee te
   voorspellen."
   → "We verwachtten autocorrelaties van nul, en dat klopt bijna: ze zijn niet precies
   nul, maar te klein om mee te voorspellen."

## Controle 1

Controle van R9-1 (F6b, notes/rapport-01_02_bachelier.md) tegen `lectures/01_02_bachelier.md`,
één keer volledig gelezen. Het rapport meldt alleen wijzigingen aan proza en bijschriften, geen
code; de celuitvoer staat dus vast en is niet opnieuw uitgevoerd.

### De drie verbeteringen

1. **Donsker (helderheid), opgelost.** De beleggersalinea onder "Het kernresultaat" gebruikt nu
   het pad: verkooporder, hoogste punt in de maand, CLT tegenover Donsker, en de toygetallen zes
   tegen vijf van de zestien paden (r. 246–253). De alinea na de stelling noemt het hoogste punt
   van het pad, en de 1951-zin verbindt nu met "en" in plaats van "maar" (r. 280–285).
2. **Hardop-toets en regeltaal (taal), opgelost.** Alle acht aangewezen plekken zijn herschreven
   zonder zinnen toe te voegen: de imports-zin, de $T$/$N$-wissel, "maar dat volgt", "is dat
   niet" (nu "lukt dat niet"), "De verwachting uit de intuïtie" (nu "We verwachtten"), de
   Regnault-"Wat"-zin (van zes naar drie getallen), de 1951-zin en "Dat is … in omgekeerde
   richting" bij uitwerking 3. Ook "Wat verwachten we dus?" is opgenomen in de vorige zin. Geen
   van de drie letterlijke citaten onder "Taal na de redactie" staat nog in de tekst.
3. **Getallen naar tabellen (replicatie, opbouw helpt mee), opgelost.** Het Regnault-oordeel telt
   nu twee getallen (0,511 en 0,80) over twee alinea's in plaats van negen in één. "Waar het
   breekt" noemt nog drie getallen (acht jaar, 4270, 5223 weken), elk bij een andere bewering, en
   "onze 5223 weken liggen daar maar net boven" is nu uitgelegd ("iets vaker wel dan niet
   gevonden"). Uitwerking 3 mist nu 1,28, 280, 487 en de wortelformule; "omgekeerde richting" is
   vervangen door wat [](#eq-bachelier-power) hier zegt.

### Voor een 9, per criterium

- Helderheid: r. 247–252 opgelost; r. 493–494 en 1334–1336 opgelost (verwijswoord vervangen door
  het ding zelf); r. 238–239 opgelost; r. 1124 opgelost ("op de steekproef van Lo en MacKinlay").
- Opbouw: r. 107–111 opgelost (factor 0,4 weg uit Intuïtie, alleen richting en evenredigheid
  over); r. 1141–1150 en 898–911 opgelost.
- Taal: alle acht plekken opgelost; r. 102 opgelost.
- Replicatie: r. 898–911 opgelost; r. 1141–1150 opgelost.

### Aanmerkingen en Beter uitleggen

- Helderheid, *Beter uitleggen*: de uitleg waarom het pad ertoe doet vóór de raakkans is opgelost
  via de herschreven Donsker-alinea's. Het $z_2$-punt is *deels*: de zin zegt nu concreet wat de
  gewone $z$ fout doet (te vaak significant door clusterende volatiliteit), maar zonder getal,
  wat terecht is, want er is geen cel of bron voor een getal (feitenregel, kaart-rollen §6).
- Opbouw, *Beter uitleggen*: de plaats van de raakkans in de routekaart is opgelost ("die laat
  zien dat de limiet over het hele pad gaat en niet alleen over de eindpositie").
- Code en figuren, *Aanmerkingen*: de regeltaalzin bij de imports is opgelost (zelfde
  herschrijving als taalpunt 1); "rode krommen" is opgelost naar "dikke krommen"
  (kleuronafhankelijk).
- Replicatie, *Beter uitleggen*: "volstaan net" is opgelost.
- Toy-voorbeeld en Oefeningen: geen openstaande punten; ongewijzigd.

### Feitelijke fouten

Geen nieuwe. Een steekproef van tien aangehaalde getallen (0,511; 7,98; 0,375; $VR(4)=1{,}15$ bij
$\rho_1=0{,}1$; 4270; 5223; 0,085; 2,73/4,74/9,50; $T^*$-tabel 96/1537/9604; kwintielen 1,205 tot
1,016) staat ongewijzigd tegenover F6; het rapport bevestigt dat er geen code is aangepast.

### Hardop-toets

Drie alinea's opnieuw hardop gelezen (Intuïtie, muntworp; de raakkans, verkooporder; Waar het
breekt, eerste alinea): geen zin die niet tegen een collega gezegd zou worden. De drie eerder
geciteerde zinnen (T/N-wissel, "maar dat volgt hier alleen uit", "De verwachting uit de
intuïtie … houdt dus bijna stand") staan niet meer letterlijk in de tekst.

### Nieuwe punten

Geen. Geen verslechtering en geen feitelijke fout aangetroffen.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 9 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,00, dus **9,0**; laagste deelcijfer 9.
Doel (≥ 9,0, geen deelcijfer onder 8,5) gehaald; taal blokkeert niet (9 ≥ 8).
