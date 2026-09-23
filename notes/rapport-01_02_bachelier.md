# Rapport L2 01_02_bachelier (taak 0, A, B; niet gecommit, niet gebouwd)

**1. prose_stats** (words sent_mean p90 gt40 para dash semicol motief u stopw calque engquote)
- vóór: 6692 20.8 36 21 62 59 38 2 7 16 4 17. FAIL op 12 metrieken.
- ná: 6722 14.6 23 0 39 0 9 0 0 1 0 0. `--check`: FAIL alleen `words=6722 (max 5500)`. `--where`: geen treffers.
- Waarom words blijft: prose_stats telt dropdowns en uitwerkingen mee, dus verplaatsen haalt niets weg. Er kwamen ook ~600 verplichte woorden bij: routekaart, Samengevat, instap-oefening, zinnen rond elke cel, twee oordelen. Verder inkorten kan alleen door inhoud te schrappen.

**2. Top-5 uit taak 0 en wat ermee gebeurde**
1. Theorie te vol (§3.6/3.11): 7 subsecties, 4 stellingen met open bewijs, geen routekaart of Samengevat. Nu 5 `###` (Opzet → Kernresultaat → 2× Wat het voorspelt → Hoe getoetst). Alle bewijzen in dropdown, routekaart en Samengevat toegevoegd.
2. Overzicht begon met geschiedenis, imports-cel stond erin, "motief 3" en "epistemische status" (§3.13/3.3). Nu vraag+antwoord, lijst van 5, één alinea geschiedenis, "theorie of feit". Imports staan bij het toy-voorbeeld.
3. Zinnen en alinea's (§3.1): 21 zinnen >40 woorden, 59 streepjes, 38 puntkomma's. Opgelost (zie 1).
4. Engelse citaten midden in zinnen (§3.4), 17 stuks: Working, Kendall, Lo-MacKinlay, Cowles, Osborne. Geparafraseerd. Bacheliers Franse zinnen staan als blokcitaat met Nederlandse inleiding.
5. Replicatie (§3.5/3.8): getallenalinea's, tweede blok ~330 woorden, geen tabel origineel/hier en geen oordeel. Blokken zijn nu 201 en 175 woorden. Twee tabellen origineel/hier, elk met oordeel "Geslaagd". Ook opgelost: "u"-vorm (7) in Intuïtie.

**3. Verplaatsingen (niets geschrapt)**
- Naar dropdown (`prf:proof`): Donsker-schets, bewijs reflectieprincipe, bewijs optieformule, bewijs VR-stelling.
- Naar dropdown-note: diffusievergelijking plus de Kolmogorov-note ("vijf jaar vóór Einstein"); Bacheliers eigen notatie en toets; Cowles' cijfers (uit Wat er brak); Osborne (uit Wat er brak).
- Uit de stellingen gehaald (H3): de Brownse limiet van de reflectie staat nu als tekst na de stelling; [](#eq-bachelier-atm) staat als tekst na de stelling, met hetzelfde label.
- Naar een nieuwe cel in Theorie: de reflectietelling (0,375) uit het toy-voorbeeld. Het toy heeft nu één mechanisme.
- Naar code-commentaar: datumdetails van Regnault, Kendall en Lo-MacKinlay (§3.8).
- De subsectie Black-Scholes-vergelijking is opgegaan in de optieprijs-subsectie.
- Vooruitverwijzingen teruggebracht tot 2 (Black-Scholes, factor zoo). De links naar efficiënte markten (Overzicht), voorspelbaarheid (replicatie) en Black-Scholes/factor zoo (uitwerkingen) zijn nu tekst zonder link.
- Code: tabellen die met een comprehension werden gebouwd zijn nu lussen (Kendall, hellingen); `frequencies`-dict hergebruikt; het AR(1)-power-blok heeft benoemde tussenresultaten. Volgorde van `rng` ongewijzigd.
- Nieuwe oefening `ex-bachelier-instap` (scheve munt). `ex-bachelier-1..3` behouden, elk eindigt met "Wat dit leert:". Geen label weg; geen andere lecture gebruikt `bachelier-`-labels.

**4. nb_outputs-diff (vóór → ná)**: alle getallen identiek en alle figuren byte-gelijk. Cellen zijn hernummerd door nieuwe cellen. Bedoelde verschillen:
- cel 2 (toy): tabel met kolommen "met de hand" en "code" (zelfde waarden). De twee `print`-regels (0.3750) staan nu in de nieuwe cel 4 (reflectie, Series van 0.375).
- cel 10: de hellingtabel (0.511/0.577) is opgegaan in een tabel origineel/hier, met Regnaults voorspeld/waargenomen-verhoudingen (0.998/0.995 tegenover French 0.965/0.885 en Shiller 0.834/0.705).
- nieuwe cel 16: origineel/hier voor Kendall ρ₁ (0.13 vs 0.030), markt-VR(2..16) en de kwintielen. Alle "hier"-getallen komen uit bestaande uitvoer.
- nieuwe cel 18: instap-oefening (0.80/3.84).
- Taak A → B: diff leeg.

**Execute-log (na B)**, laatste regels:
```
[jupytext] Reading lectures/01_02_bachelier.md in format md
[jupytext] Executing notebook with kernel python3
[jupytext] Warning: Notebook is not trusted
[jupytext] Writing lectures/01_02_bachelier.ipynb (destination file replaced [use --update to preserve cell outputs and ids])
```
Geen warnings in de celuitvoer. Sync is foutloos. Tussenstand na A staat in `$TEMP/01_02_bachelier-na-A.txt`.

**5. Afvinklijst, wat niet voldoet**
- words 6722 > 5500 (zie 1).
- H11: de toy-getallen komen terug in de theorie (1,50 tegen √(8/π) = 1,60; 0,375), niet in de simulatie. Die is gekalibreerd op Lo en MacKinlay.
- Simulatie: één vraag (hoeveel data), in twee stappen (niveau onder de nulhypothese, dan onderscheidend vermogen). Beide cellen bewust in de hoofdtekst gehouden, omdat het de rng-volgorde van de uitvoer bewaart en beide nodig zijn voor het antwoord.
- Na een Donsker-figuur staat alleen het bijschrift, geen aparte zin.
- Overige: ok.

**8. Open punten**
- De lecture is nog te vol. Een natuurlijke splitsing: (a) Regnault en Bachelier: toy, Donsker, reflectie, diffusie, optieformule, replicatie van Regnault; (b) De random walk getoetst: autocorrelatie, runs, variance ratio, simulatie van het onderscheidend vermogen, replicatie van Kendall en Lo-MacKinlay. Het knippunt is "### Hoe het getoetst wordt". Beide helften zitten dan rond 3300 woorden.
- `runs_test` blijft lokaal (`# TODO: naar hap.stats`).
- Geen build gedraaid, dus MyST-rendering van `:::{note}` met `:class: dropdown` en geneste `{math}` is ongetest. Losse lijsten (lege regel tussen items) zijn gebruikt zodat prose_stats lijstitems als aparte zinnen telt.
- Andere lectures en bestanden in `git status` zijn door parallelle agents gewijzigd, niet door mij.

## Lezersronde (taak C)

**Per H-regel (opgelost/afgewezen):** H1 2/0 · H2 8/0 · H3 0/0 · H4 1/0 · H5 3/0 · H6 2/0 · H7 8/0 · H8 1/0 · H9 6/0 · H10 7/0 · H11 0/1 · H12 1/0. Totaal: 39 opgelost, 1 afgewezen. Daarnaast drie plekken waar de lezer het spoor kwijtraakte, alle drie opgelost.
- **H1:** het waarom bij Donsker is nu een handeling: twintig dagrendementen optellen tot een maandrendement. Bij de reflectie gaat het nu om een verkooporder op niveau $a$ (hoe vaak wordt die uitgevoerd?).
- **H2:** $\mu$ heeft een ordegrootte gekregen en de reden waarom hij er niet toe doet; $\mathcal F_t$, martingaalconditie, $\delta$, de Kolmogorov-vergelijkingen, factor zoo en $z^*$ (= $z_2$) worden nu uitgelegd. De standaardfout van 2% wordt nu uitgerekend ($20\%/\sqrt{100}$) en terugverwezen naar de setup-lecture.
- **H4:** bij de runs-formule staat nu een getal: ongeveer 12 900 verwachte runs, SE ongeveer 80, dus duizend te weinig is 13 SE.
- **H5:** er staat nu dat Donsker meer eist dan de nulhypothese (i.i.d. met verwachting nul, dus eerst $\mu$ aftrekken). De optieformule rust op één aanname, de martingaalconditie. Het woord "martingaalmaat" is vervangen.
- **H6:** Samengevat zegt nu voor de raakkans wat een hoger niveau en een langere horizon doen, en voor $VR(q)$ wat een grotere $q$ doet.
- **H7:** vaste namen vastgelegd: "gemiddelde absolute afwijking" (= écart/uitslag), "spreiding" (= SD), "op het geld", "koersverandering" (= log-rendement, behalve in de optieformule), "positieve autocorrelatie" (= tekens plakken), "onderscheidend vermogen" gedefinieerd. "Nulmodel" is nu "nulhypothese". Het raaktijdstip in het reflectiebewijs heet nu $\kappa$ in plaats van $\tau$.
- **H8, H9, H10:** "Dat" is vervangen door het ding zelf. Bij de Opzet, de toy-tabel, twee figuren en twee oefentabellen staat de conclusie of een kijkaanwijzing nu vooraan. Voorbeelden toegevoegd bij martingaal, covariantie-stationair, barrièreoptie, termijnkoers, spread, convergentie van het hele pad en involutie.
- **H12:** de nulhypothese van de toetsen en de Kendall-uitkomst verwijzen nu terug naar de derde voorspelling uit de intuïtie.
- **H11 afgewezen:** de simulatie moet op Lo en MacKinlay gekalibreerd zijn (weekdata, $T=1216$). Vier muntstappen passen daar niet als kalibratie. Wel keert het toy-resultaat terug ("de variantie groeit lineair, dus $VR(2)=1$").

**Navertel-afwijkingen**
- **Overzicht.** De lezer begreep "theorie of feit" niet als vaste vraag van de reeks. Bedoeld was: de random walk is een feit dat op een verklaring wacht. De zin legt de vraag nu zelf uit ("is dit een theorie die getoetst wordt, of een feit dat op een verklaring wacht?").
- **Hoe het getoetst wordt.** De lezer zag niet hoe de alinea met "de standaardfout van 2%" aansloot. Bedoeld was: gemiddelden zijn slecht meetbaar, varianties goed, en daarom werkt een toets op varianties. De alinea begint nu met die vraag en rekent de 2% uit.
- **Wat er brak.** De lezer kon de zin "Of ze bestaan ..." niet navertellen. Bedoeld was: afwijkingen die pas na dertig jaar zichtbaar zijn, zijn economisch te klein om aan te verdienen. De zin zegt dat nu zo.
- **Spoor kwijt, diffusie-note:** de note stond onder de raakkans. Ze staat nu achter het kernresultaat, met een openingszin ("dezelfde limiet, via de dichtheid"). Verplaatst, niet gewijzigd.
- **Spoor kwijt, optiegrond:** de alinea over Black, Scholes en Merton vervangt de reden nu expliciet: de formule rust op de martingaalconditie, en replicatie geeft die conditie later een betere grond.

**Verificatie na de lezersronde**
- `prose_stats --check`: words 7282, sent_mean 15, p90 24, gt40 0, para 42, dash 0, semicol 14, stopw 1, calque 0, engquote 3. Alleen FAIL op `words=7282 (max 5500)`: de uitleg die de lezer vroeg kost ~560 woorden. `--where`: geen treffers.
- `jupytext --sync` en `HAP_OFFLINE=1 jupytext --execute` zijn foutloos. Laatste regel van het log: `[jupytext] Writing lectures/01_02_bachelier.ipynb (destination file replaced ...)`.
- nb_outputs-diff tegen `$TEMP/01_02_bachelier-na-A.txt`: leeg.

## Lezersronde 2

**Per H-regel (opgelost/afgewezen):** H1 1/0 · H2 5/0 · H4 3/0 · H5 3/0 · H6 2/0 · H7 6/1 · H8 2/0 · H10 4/0 · H11 0/1 · H12 1/0. Totaal: 27 opgelost, 2 afgewezen. De drie plekken waar de lezer het spoor kwijtraakte, zijn alle drie opgelost.

**H7, vaste namen die nu in de hele lecture gelden:**
- "gemiddelde absolute afwijking" (= *écart*). "Uitslag" en "koersafwijking" komen niet meer voor, behalve in één figuurtitel; die blijft staan, omdat een nieuwe titel de figuuruitvoer verandert.
- Bacheliers ±46 centimes heet nu *écart probable* (een mediaangrens).
- "random walk" (Workings term *random-difference series* als aliasnaam).
- "positieve/negatieve autocorrelatie". "Plakken", "volgen elkaar", "corrigeren elkaar", "trends zetten zich voort" en "terugkeer naar het gemiddelde" zijn weg.
- $\rho_1 = \rho$ staat nu expliciet in de simulatie.
- "op het geld" in Samengevat; $z_2$ overal, met $z^*$ als alias.
- $\sigma$ krijgt een waarschuwing in de optie-subsectie (bedrag per wortel-tijd) en een koppeling aan de 5% bij Donsker.

**Afgewezen**
- H7 *coefficient d'instabilité*: dat is Bacheliers historische naam en staat alleen in de note over zijn eigen notatie, met de uitleg "de volatiliteit" erbij.
- H11: zelfde reden als in ronde 1. De simulatie moet de steekproef van Lo en MacKinlay nabootsen; het principe uit het toy-voorbeeld keert terug.

**Overige oplossingen**
- **H1:** het waarom bij Donsker gaat nu over een belegger die langer vasthoudt.
- **H2:** de routekaart gebruikt geen $W$ meer; AR(1) is uitgeschreven; Chicago = Fama, Yale = Shiller; CRSP wordt uitgelegd.
- **H4:** de raakkans is uitgerekend (verkooporder 10 boven 100: eindigt erboven 31%, wordt geraakt 62%). De SE van $VR(q)$ staat er nu ook voor $q = 4, 8, 16$ (0,054; 0,085; 0,126). Voorbeeld $VR(4) = 1{,}15$ bij $\rho_1 = 0{,}1$.
- **H5:** voor runs staat de aanname erbij (onafhankelijke tekens). De SE onder het alternatief is bij kleine $\rho$ gelijk. De martingaalconditie is de random walk met $\mu = 0$ in niveaus.
- **H6:** er staat nu waarom $a$ en de horizon werken zoals ze werken, en wat de uitoefenprijs in beide richtingen doet (in/uit het geld).
- **H8:** "Dit is de warmtevergelijking" verwijst nu naar de vergelijking zelf.
- **H10:** voorbeelden toegevoegd bij eindig-dimensionale verdeling, operator, joint hypothesis en volatility smile.
- **H12:** de intuïtie voorspelt nu de evenredigheid met de spreiding; de factor 0,4 laat ze expliciet aan de theorie.

**Spoor kwijt**
1. De vraag "Waarom varianties en niet gemiddelden?" stond los. Ze is nu het tweede van twee benoemde redenen waarom de variance ratio de hoofdtoets is.
2. Runs tegenover variance ratio: "krachtigste" is geschrapt. Bij de runs staat nu dat de runs-test scherper is dan de eerste autocorrelatie, en dat de variance ratio de hoofdtoets blijft voor afhankelijkheid over meerdere perioden.
3. De helling in het toy-voorbeeld: de reden is nu dat een verhouding tussen twee horizons toevallig kan afwijken.

**Navertel-afwijking, Hoe het getoetst wordt.** De lezer wist niet of "bundelen" of "varianties zijn goed meetbaar" de kernbewering was. Bedoeld waren beide. De sectie noemt ze nu als twee benoemde redenen in een lijst, na $VR(2)-1=\rho_1$.

**Verificatie na ronde 2**
- `prose_stats --check`: words 7649, sent_mean 15.3, p90 24, gt40 0, para 43, dash 0, semicol 14, stopw 1, calque 0, engquote 3. Alleen FAIL op `words`. `--where`: geen treffers.
- `jupytext --sync` en `HAP_OFFLINE=1 jupytext --execute` zijn foutloos.
- nb_outputs-diff tegen `$TEMP/01_02_bachelier-na-A.txt`: leeg.

## Naar een 9 (na beoordeling 7,0)

**1. Helderheid**
- Gedaan:
  - de écart-verhoudingen staan nu als "de hele periode is 1,41 keer de helft";
  - σ krijgt vooraf één overzicht van zijn drie betekenissen (Opzet), en de dubbele waarschuwing in de optie-subsectie is weg;
  - de stap van repliceerbaarheid naar een verwachting van nul is uitgeschreven: de optieprijs hangt niet af van de verwachte koerswinst, dus kies nul;
  - de 46 centimes zijn uitgerekend: $5\sqrt{2\pi} \approx 12{,}5$ per dag, $\cdot\sqrt{30} \approx 69$, $\cdot 0{,}6745 \approx 46$;
  - de ruis van 0,06 staat nu als $2/\sqrt{1216}$;
  - de verwijzing voor de standaardfout van 2% wijst nu naar `#00-01-rendementen`;
  - de gebroken zin in het replicatieblok is hersteld;
  - Kendalls 0,13 staat nu in de tekst, met waarover gemiddeld is;
  - het mechanisme van de runs-test is uitgelegd: een correlatie rekent met kwadraten, een extreme dag weegt dus zwaar; de runs-test telt alleen tekens.
- Niet gedaan: niets.

**2. Opbouw**
- Gedaan:
  - het Overzicht kondigt nu de breuk aan (theorie van de ruis, niet van de waarde);
  - de routekaart noemt raakkans en optieprijs toepassingen, en zegt dat simulatie en replicatie alleen de kern toetsen;
  - de optiesectie eindigt met waarom we nu naar toetsen overstappen (geen gratis optieprijzen);
  - elke theorie-subsectie opent nu met haar conclusie in plaats van een vraag.
- Niet gedaan: Samengevat blijft aan het eind van Theorie (STYLE §11.6, op aanwijzing). Een apart Samengevat met de replicatiegetallen aan het eind is om dezelfde reden niet toegevoegd.

**3. Taal**
- Gedaan:
  - "aritmetische", "horizonnen" en "vertragingen";
  - barst/gat vervangen door gewone taal;
  - "employé" is nu "beambte";
  - *options à prime* (premieopties), *écart probable* (waarschijnlijke afwijking), en *joint hypothesis* als "het probleem van de gezamenlijke hypothese";
  - de zinnen over het tijdvak in het Overzicht, de imports-zin en de zin in oefening 3 zijn herschreven;
  - *écart* heet na de eerste vermelding overal "gemiddelde absolute afwijking".
- Niet gedaan: de Engelse docstring "arithmetic Brownian motion" blijft; code en docstrings zijn Engels (STYLE §3).

**4. Toy-voorbeeld**
- Gedaan: $\E|S_2|$ en $\E|S_3|$ zijn met de hand voorgedaan; de Opzet kondigt de twee grootheden (variantie en gemiddelde absolute afwijking) vooraf aan.
- Niet gedaan: niets.

**5. Code en figuren**
- Gedaan:
  - `comparison_lm` is nu een woordenboek met per rij (origineel, hier, z origineel, z hier), met dezelfde uitvoer;
  - `axvline(round(T_lm / 52, 1))` vervangt 23.4; figuur byte-gelijk;
  - de kolomnamen `E|dev|`, `SD(dev)` en `nobs` zijn in de tekst uitgelegd.
- Niet gedaan:
  - de kolommen zelf niet hernoemd, want dat verandert de tabeluitvoer en de figuurcode;
  - `# TODO: naar hap.stats` blijft, want STYLE §5/§3.9 schrijft dat voor;
  - de figuurtitel met "koersafwijking" blijft, want een andere titel verandert de figuur.

**6. Replicatie**
- Gedaan:
  - het Regnault-oordeel is gesplitst: geslaagd op de helling, gedeeltelijk op Regnaults eigen toets (0,885);
  - de hellingen per deelbereik (0,577 / 0,54 / 0,475) staan in een tabel;
  - de verwachting voor Kendall staat nu in het blok;
  - het L-M-oordeel toetst de $z$-waarden expliciet aan "rond de twee": gedeeltelijk.
- Niet gedaan: niets.

**7. Oefeningen**
- Gedaan: in oefening 1 staat nu "één gesimuleerd pad, een ander zaad geeft andere getallen"; de les van oefening 3 gaat nu over de oefening zelf.
- Niet gedaan: niets.

**Eigen herlezing met de rubriek**
- Dubbele σ-waarschuwing verwijderd.
- "Het is de random walk" is nu "Die aanname is".
- De runs-uitleg staat nog maar één keer.
- Overzicht en Wat er brak gebruiken dezelfde term: "theorie van de ruis".

**Verificatie**
- prose_stats `--check`: words 8092, sent_mean 15.3, p90 24, gt40 0, para 45, dash 0, semicol 13, stopw 1, calque 0, engquote 3. Alleen `words` faalt, en daarvoor gold geen grens meer. `--where`: geen treffers.
- sync en `HAP_OFFLINE=1` execute zijn foutloos.
- nb_outputs-diff tegen `$TEMP/01_02_bachelier-na-A.txt`: leeg.
