STATUS 05_30_wisselkoersen F4T words=5622 prose=PASS open=7 cijfer=- min=-

Kern: een wisselkoers is de verhouding van twee SDF's; omdat wisselkoersen glad zijn, moeten
de SDF's van landen bijna perfect samenbewegen (index ongeveer 0,98), en omdat UIP faalt
verdient de carry trade een premie die als beloning voor crash- en volatiliteitsrisico of
als vergissing te lezen is.

## F0

prose_stats: words 5011, sent_mean 20.8, sent_p90 39, sent_gt40 20, para_mean 59, dash 15,
semicol 44, motief 5, deel 2, je_form 3, calque 8, engquote 26, colon_mid 8.6, para_one 20,
telegram 1, tmpl 6 (Waarom zou 6). FAIL op 14 drempels, words PASS.

Vijf grootste problemen:
1. Taal: 44 puntkomma's, 20 zinnen boven 40 woorden (Overzicht r.40-72, Theorie r.294-303,
   Replicatie r.796-804, r.882-889).
2. 26 Engelse citaten midden in Nederlandse zinnen (Theorie r.294-303, 430-436, 441-455,
   486-512; Wat er brak r.995-999).
3. Structuur: imports-cel in Overzicht (r.74); Overzicht zonder vraag/antwoord en lijst;
   Theorie zonder routekaart en Samengevat; zes keer "Waarom zou dit waar zijn".
4. Toy: drie niet-afgeleide formules (identiteit, index, lognormale premie r.150-158) en
   een print-controle in plaats van een tabel hand/code (r.189).
5. Stellingen met twee of drie beweringen (r.218-234, 359-371, 396-415), vijf proposities
   met open bewijs, twee simulaties (r.514-674), regeltaal en jargon ("motief 1/3",
   "definieert het tijdvak", "niet kunnen inzien": r.52, 59, 303, 338, 512, 582, 799, 987,
   1087); replicatie zonder tabel origineel/hier en zonder oordeel.

Schraplijst (eis 2: grep op labels in lectures/; alleen de paginalabel wordt elders aangehaald,
door 05_29, 05_31 en 08_38; carry t = 3,0 in 08_38 blijft herleidbaar):

| passage | kopje | woorden nu -> straks | eis niet gehaald |
|---|---|---|---|
| reekscodes, volledige titels in replicatieblok | Replicatie | 400 -> 220 | 1-3 (codes staan al in de cel) |
| werkpapiercitaten en tabel 3 van BCS | Theorie, Hoe glad | 170 -> 90 | 1 (alleen 0,98 is nodig) |
| citaten Backus-Foresi-Telmer, Bekaert | Theorie, lognormaal | 80 -> 50 | 1 (parafrase volstaat) |
| citaten LV, LRV, Menkhoff e.a. | Theorie, portefeuilles | 200 -> 120 | 1 |
| citaten momentum/value, BSC 2015 | Theorie, momentum | 150 -> 80 | 1 |
| werknotities "niet kunnen inzien" | Theorie | 50 -> 0 | regeltaal; naar open punten |
| sprongenpropositie met bewijs | Theorie, crash | 150 -> 80 | nevenresultaat; gewone alinea |
| simulatie (b), peso problem | Simulatie | 250 -> 230 | tweede simulatie; dropdown-note |
| toevoegingen: routekaart, Samengevat, instapoefening, vergelijkingstabel | | +350 | |

Verwachte lengte na F1: ongeveer 4.900 woorden. Geen splitsing nodig.

## F1

Eindmeting: words 5571, sent_mean 16.2, p90 25, gt40 1, para_mean 50, dash 0, semicol 5,
engquote 0, colon_mid 0.9, para_one 7, tmpl 2; `--check` PASS. Uitvoering offline zonder fout.

Geschrapt of verplaatst:
- Engelse citaten (26) geparafraseerd; werknotities over niet-ingeziene bronnen geschrapt (regeltaal).
- BCS tabel 3 (index 0,91 bij premie 4%) en SE's van SDF-volatiliteiten: niet nodig voor de vraag.
- AMP 50/50-combinatie 0,69 en LRV "developed 0,39": getallenbrij, niet nodig.
- Sprongenpropositie: nevenresultaat, nu gewone alinea met dezelfde vergelijking.
- Simulatie (b), peso problem: tweede simulatie, nu dropdown-note in Simulatie (figuurdirective weg).
- Proposities gesplitst (H3): delen 1 en 3 van de identiteit naar tekst, Fama-gevolgen naar lijst,
  Fama-helling lognormaal naar een corollary; vier bewijzen in dropdown.
- Imports-cel naar het toy-voorbeeld; routekaart, Samengevat, vergelijkingstabel + oordeel toegevoegd.

nb_outputs-diff (alleen presentatie, geen aangehaald getal veranderd):
- toy: print-controle + Series -> tabel "met de hand / code" (zelfde 14 waarden; twee lognormale
  rijen weg, die staan nu als handberekening in Theorie).
- simulatie: Nederlandse kolomnamen (Sharpe-ratio, vol. wisselkoers, grens), zelfde getallen.
- peso: rij "gem. SR" -> "gem. Sharpe-ratio"; ex-4: "in-sample" -> "geschat in de steekproef".
- nieuw: vergelijkingstabel origineel/hier (0,54/0,44; 0,98/0,98; 0,44/0,47; 0,32/0,07) en de
  cel van de nieuwe instapoefening (1,125; 0,9167; 0,0208; 0,0154; 0,0155).

Afvinklijst §11.9, wat niet (helemaal) voldoet:
- 5571 woorden: boven het doel van 5500, onder de grens van 6000.
- Tweede simulatie blijft als dropdown-note; "Risico of vergissing?" is ongeveer 150 woorden (>120).
- Toy-stappen en BCS-alinea hebben meer dan drie getallen per alinea (handberekening).
- Toy gebruikt naast het recept het geleende resultaat premie = -Cov(m, R)/E[m] (in één regel herhaald).
- overige: ok.

Labels: weg `thm-wisselkoersen-sprongen` (vergelijking `eq-wisselkoersen-sprongen` blijft) en
`fig-wisselkoersen-sim-peso` (cel-label blijft); nieuw `thm-wisselkoersen-helling` en
`ex-wisselkoersen-4`. Oefeningen hernummerd: nieuw ex-1 (instap), oud 1->2, 2->3, 3->4; geen
van de ex-labels wordt buiten dit college aangehaald. `05-30-wisselkoersen` ongewijzigd.

Open punten voor de feitencontroleur:
1. BCS: rekenvoorbeeld 0,98 en 71%, volatiliteiten 11,5-12,9% (tabel 1), indices >= 0,98
   (tabel 2), lokale Sharpe-ratio's 0,26-0,63 komen uit de werkpapierversie (2002); de
   gepubliceerde versie is niet ingezien.
2. LRV 2011: 483 bp, Sharpe 0,54 (tabel 1), "ongeveer 70%" uit het NBER-werkpapier; LV 2007
   "tot vijf procentpunt" en risicoaversie rond 100 uit het NBER-werkpapier.
3. Menkhoff e.a. 2012a: "meer dan 90%" uit de werkpapierversie.
4. Burnside e.a.: Sharpe 0,911 (tabel 2, NBER wp 14054), periode 1976-01 tot 2009-07.
5. Barroso en Santa-Clara 2015: "Sharpe-ratio gemiddeld een half hoger" uit het abstract;
   steekproef en tabellen niet ingezien. Fama 1984: afzonderlijke schattingen niet ingezien.
6. Engel 1996 en BNP 2008 (R^2 81%, figuur 2) nu geparafraseerd; parafrase nakijken.

## F4

Feitenrijen (geen fout of niet herleidbaar; zeven onzeker, blijven open):
- Rij 1 (BCS-tabellen), Hoe glad: rekenvoorbeeld en eigen schattingen van BCS nu gescheiden (= lezerspunt 11).
- Rij 2 (LRV), Carry-portefeuilles: 483 bp en "(tabel 1)" geschrapt; 0,54 en 70% blijven onzeker.
- Rijen 3-7 (LV, Menkhoff 2012a, Burnside, BSC, BNP): afgewezen voor nu, bron-PDF's niet leesbaar; geen fout.
Lezerspunten:
- 1 (letter p), Identiteit: prijs in het bewijs heet nu $P^*_t$ (frankprijs); zin over $p_t$ ingekort.
- 2 (twee beweringen), Lognormaal: tweede formule als corollary `thm-wisselkoersen-brutopremie` (ongenummerd), bewijs dekt beide.
- 3 (getallenbrij), Carry-portefeuilles: LRV-alinea van vijf naar drie getallen; drie alinea's waren al gescheiden.
- 4 (twee Menkhoff-artikelen), Momentum en value: "In een tweede artikel".
- 5 (koopkrachtpariteit/reële wisselkoers), Momentum en value + Replicatie: één naam met alias; minteken uitgelegd.
- 6 ($b$ zonder getal), Fama-regressie: $-0,62$ geeft $b$ van ongeveer min een derde, binnen het bereik.
- 7 (carry-winst), Toy: "carry-rendement".
- 8 (bullets abstract), Fama-decompositie: gepoolde schatting $-0,62$ tussen $\beta=0$ en $\beta=-1$ geplaatst.
- 9 ($b$ zonder naam), Lognormaal: zin vóór de corollary zegt wat $b$ meet.
- 10 (Risico of vergissing >120 woorden): Yale-lezing samengevoegd, limits of arbitrage in één bijzin.
- 11 gedaan (zie rij 1). 12 gedaan ("de peso-simulatie aan het eind van de Simulatie").
- 13 gedaan (0,16, standaardfout 1,11). 15 gedaan (standaardfout 0,15 genoemd).
- 14 afgewezen: de reden (in de steekproef overschat) staat al in de aankondiging van die cel (H2 voldaan).
Verder: BCS-notatiezin ($e$, $m^d$, $m^f$) geschrapt ter betaling; note-titel zonder regeltaal ("steekproefvraag").
Navertel-toets: geen sectie week af (koude lezer: overal "klopt"); spoor-kwijt 1-3 via punten 1/8, 3 en 6.
Controle: prose `--check` PASS (sent_gt40 0), nb_numbers zelfde meldingen als vooraf, geen code gewijzigd.

## R9-1 (F6b, ronde 9+)

Feitelijke fouten:
- 1 (2008-getal), Vergelijking + Wat er brak: "aug t/m dec 2008 26,6%" (cel 10) en "ruim een kwart".
- 2 (value-vertraging), Momentum en value: "hele reële wisselkoers drie maanden achter".
- 3 (rustiger SDF, hogere rente), Toy stap 1: $\E[m^*]$ lager gekozen; algemeen via $b$.
Helderheid:
- Index vs grens, Hoe glad: zin dat $1-V/(2a^2)$ index en correlatie begrenst, gelijk bij $\sigma=\sigma^*=a$, toy (corr 1, index 0,8048) als voorbeeld; daarna overal "grens" (proza, simulatiekop en -titel, tabelkolommen, vergelijkingsrij, oefening 2).
- Fama-propositie: drie gevolgen in de propositie, bewijs met kopjes Gevolg 1-3; lijst erna geschrapt.
- VOL_EQ: aandelenvolatiliteit 16% en haar rol in de Simulatie-zin.
- r.249 "geen waarde los van": herschreven (wisselkoersverandering ligt vast).
Toy: recept zegt dat de identiteit de enige nog niet afgeleide formule is; index in stap 6 als definitie van BCS.
  Twee mechanismen in één toy: niet gesplitst (geen Voor-een-9-punt; stap 6 is nu kort).
Taal: r.55, r.62, r.84, r.1126, r.1147, r.1150 herschreven (hardop-voorstellen 1-3 overgenomen);
  getallenalinea's carry, BCS en momentum/value naar hoogstens drie getallen, rest in de tabel.
Replicatie: rij Fama-helling gepoold (hier -0,62, SE 0,38) in de vergelijkingstabel; origineel NaN met
  label "onder nul", want Fama's afzonderlijke schattingen zijn niet ingezien (kaart §6). Verwachte
  afwijking noemt nu momentum en value (binnen twee SE van Asness e.a.); oordeel zonder regeltaal.
Code: commentaar bij de groepsindeling in `sort_portfolios`; zin vóór de cellen van oefening 2 en 3.
Oefeningen: oefening 1 "frankbelegging" in plaats van "carry trade".
Opbouw (drie literatuur-###): niet gewijzigd, geen Voor-een-9-punt.
Controle: uitvoer voor/na verschilt alleen in labels en de nieuwe Fama-rij; nb_numbers zelfde 30
  meldingen (alleen regelnummers); prose --check PASS; woorden 5.836.
