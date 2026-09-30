STATUS 05_33_fama_vs_shiller F6c words=5985 prose=PASS open=1 cijfer=9,1 min=9,0

**Eindcijfer van record: 9,1** (F6c). Verloop: eerste herziening (§12): F1, F23, F4T, F6 8,9 -> F6c 9,1.

# Eindbeoordeling 05_33_fama_vs_shiller

## Eerste herziening (workflow §12)

Eerste herziening. Er is geen vorig cijfer. Gelezen: kaart-rollen, rubriek, STYLE §11.12,
het college (.md, eenmaal volledig), notes/taal-05_33, de celuitvoer via `tools/nb_outputs.py`
en de feitentabel (ter controle van de externe getallen: CAPE-record 1999, Martin 2017).
`prose_stats --check`: PASS (5.839 woorden, zinnen gemiddeld 17,0, p90 26, geen zin > 40,
alinea gemiddeld 53, dubbele punt 0,2 per 1000, motiefnamen 1, para_one 6).

## De drie verbeteringen met het meeste effect

1. **Helderheid: φ consequent persistentie noemen en de losse symbolen benoemen** (→ helderheid
   9,2). In het toy keert de premie "met snelheid $\phi = 0{,}5$" terug (r. 149, 152), terwijl
   $\phi$ de persistentie is: oefening 1 noemt $\phi = 0{,}75$ terecht "trager" en de simulatie
   (r. 495) spreekt van persistentie. Een lezer die "snelheid" leest, verwacht dat een grotere
   $\phi$ sneller terugkeert. Tegelijk: $p^{*}_t$ benoemen (fundamentele prijs, r. 151), één
   naam voor de decompositie ("schema" naast "decompositie", r. 256, 478, 791) en voor de
   derde term ("restterm" r. 249 naast "eindterm" elders).
2. **Replicatie: admonition inkorten en getallen uit de oordeelalinea's naar tabellen**
   (→ replicatie 9,1). De admonition telt 286 woorden (norm ≤ 250). De Geslaagd-alinea's van
   (1) en (3) (r. 779–784, 969–978) dragen samen een tiental getallen in lopende tekst, en
   geen van de drie oordelen verwijst met zoveel woorden naar de verwachte afwijking uit de
   admonition (r. 713–718).
3. **Taal: vier zinnen die hardop haperen** (→ taal 9,2): de komma tussen onderwerp en
   persoonsvorm (r. 422), de routekaart met drievoudige weglating (r. 218–221), "Langs
   dezelfde lijn ordenen we" (r. 415) en de bijstelling op r. 924–925. Daarbij de uitvoer van
   de regressiecel (r. 855–867), die als vier brokken met NaN-kolommen verschijnt (→ code en
   figuren 9,1).

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,9

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 |
| 2 | Opbouw en rode draad | 20% | 9,1 |
| 3 | Taal | 20% | 8,9 |
| 4 | Toy-voorbeeld | 10% | 9,2 |
| 5 | Code en figuren | 10% | 8,8 |
| 6 | Replicatie en empirie | 10% | 8,6 |
| 7 | Oefeningen | 5% | 9,2 |
| | **Gewogen** | | **8,92 → 8,9** |

Geen deelcijfer onder 8,5; taal boven 8, dus niet geblokkeerd. Wel onder de 9,0.

### 1. Helderheid van de uitleg: 8,8

*Goed.*
- Intuïtie: het kernargument krijgt meteen een exemplaar dat werkt: "Een aandeel dat in
  slechte tijden weinig uitbetaalt, is even weinig waard voor een belegger die slechte tijden
  waarschijnlijk vindt als voor een belegger die ze erg vindt." (r. 85–87).
- Theorie, "Het kernresultaat": $\xi$ krijgt naam, betekenis en een getal ($\xi = 2$ bij een
  verdubbelde recessiekans, r. 304–305); "In deze subsectie is $p_t$ de prijs zelf" (r. 298)
  voorkomt verwarring met de logs.
- H4 en H12 zijn goed ingelost: de populatiehelling 0,525 staat naast de formule met de reden
  (meetfout bijna even groot als de variantie van de verwachting, r. 411–413), en het teken
  dat de intuïtie voorspelde wordt op r. 401–403 in een gewone zin ingelost.

*Aanmerkingen.*
- Toy-voorbeeld: "In economie (a) eist een rationele belegger een vereiste premie $\pi_t$
  boven het gemiddelde, die met snelheid $\phi = 0{,}5$ naar nul terugkeert" (r. 148–150) en
  "dat met dezelfde snelheid uitdooft" (r. 152). $\phi$ is de persistentie, geen snelheid
  (zie r. 385, 495 en oefening 1); de vakterm verandert hier van betekenis.
- Toy-voorbeeld: "het sentiment $s_t = p_t - p^{*}_t$" (r. 151): $p^{*}_t$ wordt nergens
  benoemd.
- Theorie, "Wat efficiënt betekent": "Die voorkeuren mogen alles zijn wat de
  Hansen-Jagannathan-grens van [](#03-13-equity-premium-puzzle) toelaat, dus elke SDF die
  minstens zo volatiel is als de Sharpe-ratio van de markt vraagt." (r. 280–282). De grens is
  een noodzakelijke voorwaarde, geen voldoende; de zin suggereert het omgekeerde.
- H7: "Het schema zegt met grote precisie dát de discontovoet beweegt" (r. 256) naast "de
  decompositie" (r. 225, 232, 721); "een restterm" (r. 249) naast "de eindterm" (r. 251, 787,
  1003); "de uitkeringsgroei uit het verleden" (r. 460) naast "dividendgroei" overal elders.
- Middenwegen, tabel: kolomkop "$\Corr(\E^{s}_t, \mathrm{PD}_t)$" (r. 464): het symbool PD
  is nieuw; elders heet dezelfde grootheid $-dp$.

*Beter uitleggen.*
- De stap van de enquêtecorollary (bruto $R$) naar de log-lineaire tekens ($r$, r. 383–387)
  gebeurt stil; één bijzin dat de log-benadering hier volstaat, helpt.
- Bij $\theta$ (r. 154) ontbreken betekenis en orde van grootte tot stap 5; zeg bij de
  eerste keer dat $\theta$ de gevoeligheid van de extrapolatoren is en in het toy op $K$ wordt
  gezet.

*Voor een 9.* $\phi$ "persistentie" in plaats van "snelheid" (05_33_fama_vs_shiller.md:149,
152); $p^{*}_t$ benoemen (:151); de HJ-zin als noodzakelijke voorwaarde formuleren (:280–282);
één naam voor decompositie en eindterm (:249, :256, :478, :791) en "dividendgroei" (:460).

### 2. Opbouw en rode draad: 9,1

*Goed.*
- Overzicht stelt de vraag en geeft het antwoord in drie zinnen (r. 39–42); de routekaart
  van Theorie (feit → onmogelijkheid → uitweg, r. 218–221) volgt het college precies.
- De toy-getallen keren terug: $\hat b_r = 1{,}34$ in de theorie (r. 259), $K = 0{,}52$ en de
  helling ±1 in de populatie (r. 405–408), en $\theta = K$ en $\rho$ bij 0,96 in de simulatie
  (r. 495–506).
- "Wat er brak" sluit de lus: feit bevestigd, formulering vastgelegd, het eerste meetinstrument
  geeft het teken van Yale, en de factor zoo als volgende vraag.

*Aanmerkingen.*
- Wat er brak: "De CFO-verwachting hangt negatief samen met $dp$ en voorspelt latere
  rendementen met een negatieve helling, zoals Greenwood en Shleifer met zes enquêtes vonden.
  Dat is het sterkste bewijs tegen de zuiver rationele lezing" (r. 999–1002). De
  voorspellingshelling is in de replicatie niet significant ($t = -0{,}94$); het sterke bewijs
  is de helling op $dp$ ($t = -3{,}7$). De conclusie leunt op het zwakke deel.
- Middenwegen (r. 431–472): vier modellen plus tabel is de langste subsectie zonder
  resultaat van het college zelf; ze is wel kort per model.

*Beter uitleggen.*
- De overgang van "Wat het voorspelt" naar de opsomming van opties, flows en consumptie
  (r. 414–429) mist een zin die zegt waarom die lijst hier staat (elk meet $\xi$ of $m$ apart,
  met een eigen aanname).

*Voor een 9 (al 9,1).* Het sterkste bewijs in "Wat er brak" op de enquêtehelling op $dp$
leggen (05_33_fama_vs_shiller.md:999–1002).

### 3. Taal: 8,9

*Goed.*
- Zinnen gemiddeld 17 woorden met afwisseling, geen zin boven 40, alinea's gemiddeld 53.
- Chicago en Yale als vaste namen voor de twee lezingen houden de draad; motiefnaam één keer
  (kop r. 1006), geen "Wie …"-zinnen, geen regeltaal.
- Veel alinea's lezen als gesproken academisch Nederlands (Intuïtie r. 73–98, Wat er brak).

*Aanmerkingen.*
- Theorie, "Wat het voorspelt": "Gegevens over wie koopt en wie verkoopt, meten de vraag van
  afzonderlijke groepen beleggers." (r. 422). Komma tussen onderwerp en persoonsvorm.
- Theorie: "Het feit is de decompositie waarover beide kampen het eens zijn, de
  onmogelijkheid het bewijs dat prijzen alleen het product van overtuigingen en marginaal nut
  vastleggen, en de uitweg het teken van een enquête." (r. 218–221). Drie weglatingen achter
  elkaar; hardop verliest de luisteraar het werkwoord.
- Theorie: "Langs dezelfde lijn ordenen we de andere bronnen van extra data." (r. 414–415).
  Vaag ("langs welke lijn?") en een opgeplakte overgang.
- Replicatie (2): "Aan de enquêtekant is het bewijs dus sterk, met bijna honderd kwartalen,
  precies de meetbaarheid die de simulatie beloofde." (r. 924–925). Bijstelling na
  bijstelling.
- Figuur CFO, aslabel "Log prijs-dividend-ratio" (r. 882) naast "prijs-dividendratio" in de
  tekst.

*Beter uitleggen.* Geen inhoudelijk punt; het zijn zinnen die herschreven moeten worden.

*Voor een 9.* De vier zinnen hierboven herschrijven (05_33_fama_vs_shiller.md:218–221, :415,
:422, :924–925) en het aslabel gelijktrekken (:882).

### 4. Toy-voorbeeld: 9,2

*Goed.*
- Vijf genummerde stappen, alle met de hand na te rekenen (nagerekend: 0,120; 0,086;
  −0,148; 1,34; 0,52; ±2,58), met een tabel hand/code die exact overeenkomt.
- Eén mechanisme (dezelfde identiteit op hetzelfde pad) en een slotzin die zegt wat het
  getal betekent (r. 212–214).
- $\rho = 0{,}96$ krijgt een betekenis (prijs 24 keer dividend, r. 138).

*Aanmerkingen.*
- Stap 3: "Herhaald invullen geeft de meetkundige reeks $dp_t = \pi_t(1 + \rho\phi + (\rho\phi)^2 + \dots)$"
  (r. 165–166). Dit is de ene nog niet afgeleide formule; hij is kort, maar veronderstelt
  stil dat de verwachte dividendgroei nul is (afwijkingen van het gemiddelde).

*Beter uitleggen.* Het pad van $dp$ volgt de AR(1) met $\phi = 0{,}5$ niet (0,10 → 0,00 →
−0,10); één bijzin dat $\phi$ alleen de verwachting bepaalt en het pad een realisatie is,
voorkomt een verwarde lezer.

### 5. Code en figuren: 8,8

*Goed.*
- De simulatiefuncties lezen als het model: zichtbare lussen voor de AR(1), benoemde
  tussenresultaten, docstrings die zeggen wat de economieën delen (r. 520–551).
- Vóór beide figuren staat waarop te letten (r. 613–615, 870–872), erna wat te zien is
  (bijschriften en r. 660–662).
- Replicatiecellen zetten origineel en hier naast elkaar (Cochrane tabel II, GS tabel 4).

*Aanmerkingen.*
- Replicatie (2): de regressiecel (r. 855–867) geeft `pd.DataFrame(reg_rows).T`, dat in de
  uitvoer in vier brokken met veel NaN-kolommen uiteenvalt. Na de cel volgt "De regressies
  laten het teken van extrapolatie zien." (r. 870), zonder te zeggen waar in de tabel.
- Replicatie (1): "Cochrane tabel III (1947-2010)" in de print (r. 771), terwijl de tekst
  1947–2009 zegt (r. 250, 689).
- De eerste regel van cel 7 print een dict met tuples (b, t, R2) naast een platte string;
  een tabel origineel/hier voor de eenjaarsregressies leest beter.

*Voor een 9.* De regressie-uitvoer als één smalle tabel (rijen = regressie, kolommen = b, t,
R2, N) en de zin erna laten wijzen naar de cel $-0{,}029$ met $t = -3{,}7$
(05_33_fama_vs_shiller.md:855–870); de eenjaarsregressies als tabel (:768–771).

### 6. Replicatie en empirie: 8,6

*Goed.*
- Drie replicaties met elk een oordeel dat met "Geslaagd" begint, en een tabel
  origineel/hier voor (1) en (2).
- De CAPE-update is eerlijk opgezet (schatten tot 2006, voorspellen 2007–2015, zonder
  vooruit te kijken) en de interpretatie laat beide lezingen aan het woord (r. 980–986).
- De voorzichtigheid aan het eind van (2) (r. 925–928) koppelt het resultaat terug aan de
  theorie: iemand extrapoleert, maar niet noodzakelijk de marginale belegger.

*Aanmerkingen.*
- Replicatie-admonition: 286 woorden (norm ≤ 250).
- Replicatie (1): "**Geslaagd.** De éénjaarshellingen liggen binnen één standaardfout van
  Cochranes tabel III, en de directe decompositie over vijftien jaar legt de hele beweging bij
  de verwachte rendementen ($b_r^{(15)} = 1{,}16$, $b_d^{(15)} = -0{,}01$)." (r. 779–781) en
  (3) "**Geslaagd.** Op beginjaren tot 2006 is de helling $-0{,}075$ ($t = -6{,}6$) …"
  (r. 969–973): getallen in lopende tekst die al in de tabel staan.
- Replicatie (3): het oordeel "Geslaagd" dekt alleen het teken; dat de voorspellingen elk jaar
  gemiddeld zeven procentpunt te laag lagen, valt buiten de verwachte afwijking (r. 718) en
  verdient een expliciete zin dat dit niet voorzien was.
- Geen van de drie oordelen noemt de verwachte afwijking bij naam of getal (bijv. "binnen
  twee standaardfouten, zoals verwacht").

*Voor een 9.* Admonition naar ≤ 250 woorden (05_33_fama_vs_shiller.md:676–719); oordelen
(1) en (3) laten verwijzen naar de verwachte afwijking en de getallen naar de tabel laten
wijzen (:779–784, :969–978); voor (3) het niveau-verschil als onvoorzien benoemen.

### 7. Oefeningen: 9,2

*Goed.*
- Precies de gevraagde trap: instap op het toy (1), afleiding plus simulatie (2), uitbreiding
  van de replicatie (3) en van de simulatie (4); alle getallen kloppen met de celuitvoer.
- Elke uitwerking eindigt met een les (r. 1051–1053, 1106–1110, 1141–1144, 1179–1184).

*Aanmerkingen.*
- Oefening 4: "Bij een ruis van 8 procentpunt heeft ook een enquête driekwart eeuw nodig, en
  verdwijnt het voordeel van de enquête op de rendementsregressie grotendeels." (r. 1181–1183).
  De rendementsregressie haalt 80% pas bij ongeveer 150 jaar; de enquête is dan nog twee keer
  zo snel.

## Feitelijke fouten

Nagerekend tegen de celuitvoer: toy (alle acht getallen), simulatie (0,132; 0,062/0,061;
p = 0,758; ±0,093; sd 0,012; 0,525; 0,547; 85%; 0,659; 80% tussen 20 en 30 jaar),
Cochrane-decompositie (1,164; −0,010; sommen; 0,73; 0,17; $\rho\hat\phi = 0{,}9205$),
CFO (96 kwartalen; −0,545/−0,411; −0,029 met $t = -3{,}73$; $t(b=1) = -1{,}61$),
CAPE (−0,0745; +0,071; 2,3%/6,6%; 40,6; 0,59%; 4,5%), oefeningen (0,28; 4,79; 0,656; 0,437;
0,458/0,468/0,195; 15/30/75). Alles juist. Open:

1. r. 149, 152: "snelheid $\phi$". Vakterm met verkeerde betekenis: $\phi$ is de
   persistentie (hogere $\phi$ = tragere terugkeer, oefening 1). **Onjuist.**
2. r. 280–282: de HJ-grens als voldoende voorwaarde ("mogen alles zijn wat … toelaat, dus
   elke SDF die …"). De grens is noodzakelijk, niet voldoende. **Onjuist (overschatting).**
3. r. 999–1002: het "sterkste bewijs" steunt mede op een voorspellingshelling met
   $t = -0{,}94$. **Overclaim**; het bewijs is de enquêtehelling op $dp$.
4. r. 1181–1183: "verdwijnt het voordeel … grotendeels" terwijl de enquête bij 8 pp nog
   twee keer zo weinig jaren nodig heeft (75 tegen ruim 100–150). **Overclaim.**
5. r. 771 (code-print): "Cochrane tabel III (1947-2010)" tegenover 1947–2009 in r. 250 en
   689. **Onzeker/inconsistent**; één periode kiezen.
6. r. 339: "Welke $\tilde m$ we ook kiezen … er bestaan overtuigingen die de waargenomen
   prijzen precies verklaren": geldt voor $c_t\tilde m$, dus op een schaalfactor na (zo staat
   het ook in de propositie). **Klein precisiepunt.**
7. Uit F23 nog onzeker: de parafrase van SantaClara2026 (r. 56) is niet tegen de bron gelegd.

## Navertelling in vijf zinnen

Fama en Shiller zijn het eens dat bijna alle variatie in de prijs-dividendratio variatie in
verwachte rendementen is, zoals Cochranes decompositie laat zien en de replicatie tot 2009
bevestigt. Waarom de discontovoet varieert, kunnen koersen niet beslissen, omdat prijzen alleen
het product van overtuigingen en marginaal nut vastleggen: bij elke keuze van SDF bestaan
overtuigingen die dezelfde prijzen en rendementen geven. Een enquête over verwachtingen meet
de overtuigingen apart en krijgt in de rationele economie een negatief en in de extrapolerende
economie een positief verband met de prijs-dividendratio, en de simulatie toont dat dertig jaar
enquête daarvoor volstaat waar koersen meer dan een eeuw vragen. De CFO-enquête geeft, net als
bij Greenwood en Shleifer, het teken van extrapolatie, al bewijst dat niet dat de respondenten
de prijs zetten. Het debat is zo een meetprobleem geworden, en de CAPE-update en de eindterm
tot 2025 laten zien dat ook de feiten zelf schuiven. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft goed werk gedaan: geen calques, geen regeltaal, geen je-vorm, dubbele punten
zeldzaam, verband met voegwoorden. Er is geen vakterm door de redactie van betekenis veranderd
voor zover na te gaan; "snelheid $\phi$" (r. 149) is wel zo'n betekenisverschuiving, maar het
taalrapport meldt het toy alleen op stap 3 en 5, dus de herkomst is onduidelijk. "Uitkeringsgroei"
(r. 460) en "restterm" (r. 249) zijn aliassen die de redacteur had kunnen gelijktrekken.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. "Gegevens over wie koopt en wie verkoopt, meten de vraag van afzonderlijke groepen
   beleggers." (r. 422)
   → "Gegevens over wie koopt en wie verkoopt meten de vraag van afzonderlijke groepen
   beleggers."
2. "Het feit is de decompositie waarover beide kampen het eens zijn, de onmogelijkheid het
   bewijs dat prijzen alleen het product van overtuigingen en marginaal nut vastleggen, en de
   uitweg het teken van een enquête." (r. 218–221)
   → "Het feit is de decompositie waarover beide kampen het eens zijn. De onmogelijkheid is
   dat prijzen alleen het product van overtuigingen en marginaal nut vastleggen, en de uitweg
   is het teken van een enquête."
3. "Aan de enquêtekant is het bewijs dus sterk, met bijna honderd kwartalen, precies de
   meetbaarheid die de simulatie beloofde." (r. 924–925)
   → "Aan de enquêtekant is het bewijs dus sterk: bijna honderd kwartalen volstaan, zoals de
   simulatie beloofde."

Bij volledige oplossing van alle punten: 9,2

## Controle 1

Gelezen: het college (eenmaal volledig), R9-1 in het rapport, celuitvoer via `tools/nb_outputs.py`
en `prose_stats --check` (PASS, 5.985 woorden, zinnen 17,3, p90 26, geen zin > 40, alinea 55).

### Per punt

| punt | stand | toelichting |
|---|---|---|
| Feit 1, "snelheid φ" (r. 149, 152) | opgelost | nu "persistentie φ = 0,5 ... de helft blijft over" en "dezelfde persistentie" (r. 148-154) |
| Feit 2, HJ-grens (r. 280-282) | opgelost | "alleen een ondergrens ... noodzakelijk, niet voldoende" (r. 285-288) |
| Feit 3, sterkste bewijs (r. 999-1002) | opgelost | steunt nu op de significante enquêtehelling; rendementshelling "niet significant" (r. 1015-1018; t = -3,73 en -0,94 in cel 9) |
| Feit 4, oefening 4 | opgelost | "twee keer zo snel" klopt: 75 jaar tegen 100-150 (cel 5: 0,659 bij 100, 0,844 bij 150; cel 15: 75) |
| Feit 5, periode tabel III | opgelost | print en tabel zeggen 1947-2009 (cel 7) |
| Feit 6, schaalfactor | opgelost | "op de schaalfactor c_t na" (r. 345-347) |
| Feit 7, SantaClara2026 | open | bron niet opgehaald; niet verslechterd |
| Verbetering 1 (p*_t, θ, één naam, PD) | opgelost | p*_t fundamentele prijs, θ gevoeligheid, "decompositie"/"eindterm"/"dividendgroei" consequent (grep), tabelkop -dp |
| Verbetering 2 (admonition, getallen naar tabel) | grotendeels opgelost | admonition nu 258 woorden inclusief opmaak en verwijzingen (proza ruim onder 250 volgens het rapport: ~205); oordelen (1) en (3) verwijzen naar de verwachte afwijking en de tabel, (3) noemt het niveauverschil "niet voorzien" |
| Verbetering 3 (vier zinnen, aslabel, regressietabel) | opgelost | r. 223-226, 433, 940-941 herschreven; aslabel 897; regressie-uitvoer is één tabel (cel 9) met verwijzing naar -0,029, t = -3,7 |
| Bruto R naar log r, overgang opties/flows | opgelost | bijzin r. 391-393 en overgangszin r. 424-426 |
| Toy: stap 3 en het pad | opgelost | verwachte dividendgroei nul, pad is een realisatie (r. 165-170) |
| Hardop-toets, drie zinnen | opgelost | alle drie herschreven zoals voorgesteld of beter |

### Getallencontrole

Alle toegevoegde of gewijzigde getallen zijn herleid: 1,34/0,52/±2,58 (cel 2), 0,525 en 0,093
(cel 4), -0,029 en t = -3,7 en -0,94 en t(b=1) = -1,61 (cel 9), 1947-2009 (cel 7), 0,71 =
zeven procentpunt fout (cel 11), 80% bij 150 jaar en 75 jaar bij 8 pp (cel 5 en 15), 96 kwartalen
(cel 8). Geen niet-herleidbaar getal, geen verslechtering.

### Resterende, kleine punten (geen deelcijfer eronder)

- De bewerkingen zijn niet opnieuw gerewrapt: halve regels op r. 169-171, 288-289, 795-796,
  941-942, 1018-1019, een dubbele lege regel op r. 259-260 en een regel van ruim 100 tekens op
  r. 1200. Zichtbaar in de bron, niet in het boek.
- r. 148-150 "een rationele belegger een vereiste premie" herhaalt "eist ... vereiste"; stap 3
  (r. 165-173) is dicht, 63 woorden in één alinea met een zin van ongeveer 40 woorden.
- Feit 7 (SantaClara2026) blijft onzeker.

## Eindcijfer van record (F6c): 9,1

Plafond: deelcijfers stijgen alleen bij een punt en hoogstens tot het genoemde cijfer.

| nr | criterium | gewicht | F6 | F6c |
|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 | 9,1 |
| 2 | Opbouw en rode draad | 20% | 9,1 | 9,1 |
| 3 | Taal | 20% | 8,9 | 9,1 |
| 4 | Toy-voorbeeld | 10% | 9,2 | 9,2 |
| 5 | Code en figuren | 10% | 8,8 | 9,1 |
| 6 | Replicatie en empirie | 10% | 8,6 | 9,0 |
| 7 | Oefeningen | 5% | 9,2 | 9,2 |
| | **Gewogen** | | 8,92 | **9,105 -> 9,1** |

Geen deelcijfer onder 8,5; taal boven 8, dus niet geblokkeerd. Eindcijfer hoogstens 9,2 (volledige oplossing).
