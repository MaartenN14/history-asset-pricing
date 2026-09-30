STATUS 06_36_inelastische_markten F4T words=5674 prose=PASS open=2 cijfer=- min=-

# Rapport 06_36_inelastische_markten

**Kern.** Hoeveel beweegt de prijs van de aandelenmarkt als er één dollar extra in stroomt?
Volgens Gabaix en Koijen ongeveer vijf dollar, omdat de vraag naar aandelen inelastisch is
($\zeta \approx 0{,}2$, multiplier $M = 1/\zeta$), maar die multiplier is moeilijk te meten:
OLS is vertekend en GIV is op een kwart eeuw kwartaaldata onnauwkeurig.

## F0

`words=5758 sent_mean=22.0 sent_p90=39 sent_gt40=21 para_mean=66 semicol=36 motief=4 deel=2
calque=4 engquote=33 colon_mid=10.4 para_one=21 telegram=1 tmpl=5` — FAIL op 13 drempels.

Vijf grootste problemen:

1. Overzicht r. 38–80 en hele college: 33 Engelse citaten midden in Nederlandse zinnen
   (Overzicht, Intuïtie, Koijen-Yogo r. 345–413, passief r. 505–515, Wat er brak).
2. Structuur: imports-cel in Overzicht (r. 69), geen routekaart en geen "Samengevat" in
   Theorie, vijf stellingen met open bewijs (max drie), twee simulaties (a) en (b).
3. Replicatieblok r. 741–796 ≈ 480 woorden (max 250), reekscodes in het blok; oordelen
   zonder tabel origineel/hier en zonder "Geslaagd/Gedeeltelijk/Niet geslaagd" (r. 877, 961, 987).
4. Taal: 21 zinnen boven 40 woorden, 36 puntkomma's, 21 eenregelalinea's, motiefjargon
   ("motief 3", "het 2%-motief", "praktijkmotief"), "Deel 4/Deel 3" (r. 469–472), "lecture".
5. Notatie en naad: CARA-stelling r. 297–323 gebruikt $R^f$ bruto (project: netto);
   eq-volatiliteit gebruikt $r$ voor het log rendement (project: $\ell$); "Wat we al weten"
   noemt vier colleges en beweert dat passief in [](#04-25-industrie) "de grootste
   beleggersgroep" werd, terwijl 04_25 r. 22/84 zegt: evenveel als actieve fondsen (15%).

Label-check (eis 2): van dit college wordt in `lectures/` alleen het paginalabel
`06-36-inelastische-markten` aangehaald (05_33, 06_35, 07_37, 08_39); geen vergelijking,
stelling of figuur. Eis 2 redt dus geen passage.

Schraplijst (kopje, geschatte woorden, eis die niet gehaald wordt):

| passage | woorden | reden |
|---|---|---|
| Waar we zijn: 04-25 en extra verwijzingen | −30 | geen van 1–3; max twee eerdere colleges |
| Overzicht: citaten, epistemische alinea herschreven tot vraag/antwoord, lijst, geschiedenis | −80 | vorm §11.7 |
| Intuïtie: citaten Shleifer, Wurgler-Zhuravskaya, GK parafraseren | −30 | taal |
| Koijen-Yogo: paginaverwijzingen, "0,64 naar 0,22"-zin (werkmelding) | −150 | 1, 2, 3 niet |
| Passief: ETF-volatiliteit Ben-David e.a. | −50 | 1, 2, 3 niet; hoorde bij replicatie (3) |
| Inkoop eigen aandelen: rekenwerk staat in oefening 1 | −40 | 1 niet |
| Simulatie (a) → dropdown-note in Theorie, tekst ingekort | −60 | één simulatie |
| Replicatieblok van 480 naar ≈ 240 | −240 | §11.7 |
| Replicatie (3) passief en volatiliteit, met cel | −150 | 1, 2, 3 niet; twee momentopnamen toetsen niets |
| Tekst rond de gepubliceerde inclusietabel | −40 | getallen staan in de tabel |
| Wat er brak: herhaalde getallen | −60 | ≤ 120 woorden per element |
| Toevoegingen: routekaart, Samengevat, tabellen origineel/hier, lees-zinnen | +270 | vereist |

Verwachte lengte: 5758 − 930 + 270 ≈ 5.100 woorden. Geen splitsing nodig.

## F1

Eindmeting: `words=5587 sent_mean=16.9 sent_p90=25 sent_gt40=1 para_mean=53 semicol=0 motief=0
calque=0 engquote=0 colon_mid=0.5 para_one=5 tmpl=1 wie_open=1` — PASS op alle drempels.
Rewrap 814 → 1075 regels; jupytext --sync en nbconvert --execute (HAP_OFFLINE=1) foutloos.

Geschrapt of verplaatst:
- Imports-cel van Overzicht naar begin Toy-voorbeeld (§11.7).
- Simulatie (a) flows/volatiliteit → dropdown-note in Theorie ("Wat een lage elasticiteit
  verandert"), celvolgorde en rng-volgorde ongewijzigd; Simulatie heeft nu één vraag (OLS vs GIV).
- Replicatie (3) passief en volatiliteit met cel: twee ICI-momentopnamen toetsen niets (eis 1–3 niet).
- Ben-David/Franzoni/Moussawi (ETF-volatiliteit) en KRY-herwaardering 38,9→32,8%: nevenresultaat.
- Koijen-Yogo "0,64 naar 0,22"-zin en "vonden we geen getal" (werkmelding); paginaverwijzingen.
- σ_ε-substituutalinea bij CARA (nevenresultaat); Santa-Clara-citaat "excess/discount rates" uit Overzicht.
- Alle 33 Engelse citaten geparafraseerd; replicatieblok ≈ 480 → ≈ 230 woorden, reekscodes in de cel.
- Toegevoegd: routekaart, Samengevat, opzet-tabel toy, tabel hand/code, twee tabellen origineel/hier
  met oordeel (Gedeeltelijk geslaagd / Geslaagd), lees-zinnen bij elke genummerde vergelijking,
  zin voor en na elke cel; alle bewijzen in dropdown; GIV-stelling van vier naar twee beweringen.
- Notatie: CARA-stelling nu met $R^f$ netto ($1+R^f$ bruto); eq-volatiliteit met $\ell$ voor het log
  rendement; zin dat $P$ hoofdletter is omdat kleine letters hier logveranderingen zijn.

nb_outputs-diff (voor → na): alleen (1) toy-tabel anders opgemaakt (kolommen hand/code, rijnamen
"geval 1/2"), getallen identiek; (2) cel 5 begint nu met `def demean` (lambda vervangen);
(3) `L7_TICKERS` → `EVENT_TICKERS`; (4) cel 13 (realized_vol, replicatie 3) verwijderd, daardoor
nummering 14–16 → 13–15. Alle simulatie-, regressie- en eventgetallen ongewijzigd.
nb_numbers: 12 meldingen, alle toy-handstappen (40,32; 50,4; 87,5 ...) of geciteerde GK-getallen (7,08; 5,28; 1,86).

Afvinklijst §11.9, wat niet voldoet: woorden 5587 net boven het doel 5.500 (grens 6.000 gehaald);
Theorie is ≈ 43% van de tekst (richtlijn 35%); de tweede simulatie staat als dropdown in Theorie.
Overige: ok.

Labels: geen label verdwenen of verhuisd. Alleen `06-36-inelastische-markten` wordt elders aangehaald.
Naad Deel IV/V: 04-23, 04-25, 05-32, 05-33 en `prop-fama-vs-shiller-equivalentie` bestaan. Bewering
over 04_25 gecorrigeerd: niet "grootste beleggersgroep" maar "evenveel als actieve fondsen" (04_25 r. 22, 84).

Open punten voor de feitencontroleur:
1. ICI2020: indexfondsen eind 2019 evenveel van de beurs als actieve fondsen (was cel met 15/15).
2. HaddadHuebnerLoualiche2025: "only counteracts two-thirds" gelezen als "compenseert twee derde".
3. KoijenRichmondYogo2024: elasticiteiten "tussen nul en één", hedgefondsen "ongeveer een half".
4. KoijenYogo2019: 81% / 12% als variantie van rendementen tussen aandelen; 68% en \$100 miljoen.
5. HarrisGurel1986-parafrase (meer dan 3%, binnen twee weken bijna terug).
6. CARA-stelling na omzetting naar netto $R^f$ en "absolute risicoaversie $\gamma$" narekenen.
7. Build niet gedraaid: dropdown-note met code-cellen en geneste `{figure}` (4-dubbelepunt-fence) controleren.
8. Notatie: $c_t$ (cumulatieve flow) botst met consumptie, $S$ met $S_i$ (al in origineel);
   bib-keys BenDavidFranzoniMoussawi2018 en de KRY-herwaardering worden hier niet meer aangehaald.

## F4

Feitenrijen:
- 1 (Simulatie-figuur): bijna 24%. 2 (Simulatie): OLS-mediaan 0,013 bij Zipf, 0,0001 bij bijna gelijk.
- 3 (GIV, Simulatie): 3 tot 8. 4 en 12 (Replicatie): duidelijkste helling; herbalanceren "past bij", niet significant.
- 5, 6, 7, 13 (Koijen-Yogo): 81/12, 68% en "drie keer" geschrapt; KRY "ver onder twintig", hedgefondsen ~0,5.
- 8 (Overzicht): Santa-Clara verzacht. 9 (Intuïtie): Shleifer als tijdreeks na 1976, ~3% uit eigen tabel.
- 10, 11 (inclusietabel, code): open, geen bron ingezien, geen tegenbewijs; ongewijzigd.
- Harris-Gurel-zin (rapport F1 open punt 5) geschrapt: niet geverifieerd en de tabel draagt het verhaal.
Lezerspunten:
- 1, 3, 5, 6, 13: als feitenrijen 2, 4, 1, 3, 12.
- 2 (Replicatie): oordeel noemt nu 7,3 tot 16,4 afhankelijk van de periode. 4: als feitenrij 5.
- 7 (GIV): alinea na de kansgrens legt uit dat $z_t = -f_{E,t}$ door het vaste aanbod.
- 8 (GIV): exemplaar (iedereen tegelijk optimistisch) staat nu vóór de formule; "groter dan verwacht" wordt "factor ruim vijftien".
- 9 (CARA): "De waarde 20 geldt alleen ..." met reden waarom de horizon telt.
- 10 (Toy): elasticiteit verwijst naar de definitie in Intuïtie; recept als bijzin.
- 11 (H7): "geldstroom" overal "flow"; "instroom" blijft voor een positieve flow.
- 12 (Oefening 2): "eigen schokken van grote spelers, niet met de gemeenschappelijke vraag verbonden".
- 14: docstring en aslabel naar $\ell$; nbconvert opnieuw, alleen figuurbytes verschillen.
- 15 (Replicatie): oordeel zegt dat het over teken en ontbreken van groot effect gaat.
- H2 $c_t$ versus consumptie: afgewezen, wiskunde niet wijzigen in F4T.
Navertel-toets week af in Theorie (GIV-instrument) en Replicatie (oordeel bij 16,4); beide herschreven.

## R9-1 (F6b, ronde 9+)

Woorden 5.877 (was 5.674), prose_stats PASS (één zin > 40), nb_numbers dezelfde 12 meldingen (alleen regelverschuiving).
- **Feitelijke fout 1 / verbetering 1 (OLS-mechanisme, r. 459):** herschreven, bij vast aanbod koopt per saldo niemand, gemeten flow $f_E = u_E - u_S$, regressie ziet prijsbeweging zonder flow.
- **Feitelijke fout 2 (toy-slot, r. 216):** multiplier vijf vraagt geen mandaat voor iedereen, wel een even inelastische actieve belegger.
- **Opzet-notatie (r. 236):** bijzin dat $f_{i,t}$ en $c_t$ fracties zijn, geen logs.
- **Flow-betekenissen (r. 308):** toy-getallen erbij (1 in fonds, 0,8 vraagverschuiving, markt koopt per saldo niets).
- **GIV-bewijs:** stap 2, 3 en 4 elk een eigen alinea; stap 4 noemt $\Cov(u_S,u_E)=\sigma_u^2/N$ uit stap 2.
- **Samengevat:** vooruitblik vervangen door de kansgrens 0,013 en schijnbare multiplier bijna 80.
- **Opbouw, Overzicht:** "zoals de simulatie in dit college laat zien" bij twee tot acht.
- **Opbouw, dropdown-simulatie in Theorie:** niet verplaatst; beoordelaar noemt het verdedigbaar, geen STYLE-regel eist het.
- **Toy stap 3:** multiplier per dollar vraagverschuiving, niet per dollar in het fonds.
- **Leeswijzers figuren:** flowsim (linkerpaneel benoemd), GIV-figuur (volledige zin), FoF-figuur vóór en na (rechterpaneel: fondsen nemen koperrol over van pensioenfondsen, ondernemingen kopen in, huishoudens verkopen; kwalitatief, gecontroleerd op de FRED-cache, geen getallen in de tekst).
- **Code:** `naive_researcher` krijgt tussenresultaat `r2_news`; nbconvert offline, nb_outputs voor/na identiek.
- **Replicatie:** admonition koppelt negatief teken aan aankondigingsrendement bij inclusies; 7,3 ($t$ = 2,8) uit lopende tekst (staat in tabel); t-waarden 1,8 en -1,55 en 4,0% geschrapt, 3,1% blijft als getal voor het oordeel.
- **Taal:** "haar" → "de uitkomst" (r. 1042); SDF-zin herschreven; inclusie-inleiding en oordeel volgens hardop-voorstel; spatie r. 853 en dubbele spatie r. 959 weg.
- open: 0.
