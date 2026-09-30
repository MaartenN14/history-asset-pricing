STATUS 04_23_behavioral F4T words=5479 prose=PASS open=0 cijfer=- min=-

# Rapport 04_23_behavioral

**Kern.** Kunnen vergissingen van beleggers prijzen blijvend verschuiven als er ook rationele
arbitrageurs zijn? Ja, omdat tegenhandelen zelf riskant is en kapitaal vraagt, maar prijzen en
rendementen alleen kunnen niet uitmaken of een voorspelbaar rendement een vergissing is of een
beloning voor risico.

## F0

**prose_stats (nulmeting).**
`04_23_behavioral.md 5141 words, sent_mean 20.7, sent_p90 36, sent_gt40 17, para_mean 60, semicol 45, motief 3, calque 2, engquote 6, colon_mid 7.6, para_one 24, telegram 1, tmpl 5`
FAIL op sent_mean, sent_p90, sent_gt40, semicol, motief, calque, engquote, para_one, telegram, tmpl.

**Vijf grootste problemen.**
1. Taal (hele college, vooral Theorie r. 382–472 en Replicatie r. 939–957): 17 zinnen boven 40
   woorden, 45 puntkomma's, 24 alinea's van één zin; "motief 3" (r. 55), "motief 1" (r. 722, 947).
2. Toy-voorbeeld (r. 114–252) heeft twee mechanismen, prospect theory en DSSW; de imports-cel
   staat in Overzicht (r. 65); Overzicht mist vraag en antwoord en de lijst.
3. Simulatie (r. 624–829) bevat twee simulaties met twee vragen (overleven van noise traders;
   meetbaarheid van $h^*$).
4. Theorie (r. 254–622): geen routekaart en geen Samengevat; vijf proposities met open bewijs
   (r. 332, 414, 457, 523, 610); vijf keer "Waarom zou dit waar zijn"; intuïtie doet geen
   voorspelling die de theorie inlost.
5. Replicatie (r. 831–1074): geen tabel origineel/hier en geen oordeel Geslaagd/Gedeeltelijk;
   BT-blok ruim 250 woorden; getallenbrij in proza (r. 939–954, 1052–1057, 1062–1073); twee
   Engelse citaten (r. 968, 1068); oefening 1 is geen instap; kolomnamen "alfa".

**Schraplijst (STYLE §11.11).** Extern aangehaald (grep in lectures/): alleen de paginalabel
en `prop-behavioral-joint` (05_33). Geen andere label van dit college wordt elders aangehaald.

| passage (kopje) | woorden nu → straks | eis die niet gehaald wordt | actie |
|---|---|---|---|
| Toy (b) DSSW-generatie | 260 → 200 | toy mag één mechanisme hebben | naar Theorie/DSSW als getallenvoorbeeld (eis 1 blijft) |
| Simulatie (a) dynastieën | 330 → 200 | tweede simulatie | naar Theorie/DSSW als illustratie "overleven"; cellen blijven op dezelfde plek in de rng-volgorde |
| Intuïtie 3Com-details, Santa-Clara-zin | 90 → 50 | eis 1–3 niet | schrappen |
| Onder- en overreactie (BSV, DHS, HS) | 150 → 120 | eis 1 deels | inkorten tot lijst |
| DSSW vier krachten | 60 → 40 | eis 1 niet | inkorten |
| Note Odean/Barber | 200 → 90 | eis 1–3 niet | tabel, zonder Engels citaat |
| Replicatieblokken DBT en BT | 560 → 420 | §11.7 (≤ 250, twee zinnen per onderdeel) | inkorten; januaridetails naar oefening |
| Risico of vergissing | 190 → 130 | §11.7 (≤ 120) | inkorten |
| Replicatieproza DBT/BT | 330 → 250 | getallenbrij | tabel + oordeel |

Toevoegingen: routekaart (70), Samengevat (110), Overzicht vraag/antwoord en lijst (90),
instapoefening (130), voorspelling in Intuïtie (60), zinnen rond cellen (80).
Schrappen ongeveer −570, toevoegen ongeveer +540: **verwachte lengte ≈ 5.100 woorden**, ruim
onder 6.000 zonder de kern te raken. Geen splitsing nodig.

## F1

**Eindmeting.** `5390 words, sent_mean 15.9, sent_p90 25, sent_gt40 0, para_mean 43, semicol 4, motief 0, calque 0, engquote 0, colon_mid 0.4, para_one 6, telegram 0, tmpl 1` PASS. rewrap, jupytext --sync en nbconvert offline zonder fouten.

**Geschrapt of verplaatst.**
- Toy (b) DSSW-generatie → Theorie/DSSW als getallenvoorbeeld (toy houdt één mechanisme).
- Simulatie (a) dynastieën → Theorie/DSSW als illustratie van overleven, ingekort; cellen in dezelfde rng-volgorde, dus alle getallen gelijk.
- Imports-cel van Overzicht naar begin Toy; Overzicht nu vraag/antwoord, lijst, één alinea geschiedenis.
- Alle vijf bewijzen in dropdown, met een bewijsidee in de hoofdtekst; routekaart en Samengevat toegevoegd.
- 3Com/Palm-anekdote, Santa-Clara-zin in Intuïtie, vier krachten van DSSW, tussenwaarden van het BT-profiel (4,65, 3,0, 2,0%), januaricijfers in het DBT-blok: geschrapt (eis 1–3 niet).
- Note Odean/Barber → tabel, Engels citaat weg; BT-citaat "always between 9 and 12 months" geparafraseerd.
- Nieuwe instapoefening (λ = 1,5 op het toy).

**nb_outputs-diff (alle bedoeld, geen getal veranderd).** Toy-tabel heeft nu kolommen met de hand/code (zelfde waarden); DSSW-voorbeeldcel staat na de BT-cel; dynastiecellen voor de SV-cel; kolommen "CAPM-alfa/FF3-alfa" heten "-alpha"; DBT-driejaarstabel getransponeerd met kolom origineel (24,6; 2,20); BT-tabel heeft kolom "h* origineel (maanden)"; nieuwe cel ex-behavioral-1 (1,429; −2,05; 13,75). Alle overige uitvoer identiek, ook rng-afhankelijke tabellen.

**§11.9, niet (helemaal) voldaan.**
- "Eén simulatie": de dynastie-Monte-Carlo staat nu als illustratie in Theorie; strikt genomen een tweede simulatie.
- H3: `prop-behavioral-dssw-rendement` en `prop-behavioral-sv` bevatten elk twee beweringen (formule + voorwaarde).
- Overige: ok.

**Labels.** Geen label verdwenen. Oefeningen hernummerd: nieuw `ex-behavioral-1` (instap); oude 1, 2, 3 → `ex-behavioral-2`, `-3`, `-4`. Nergens in lectures/ aangehaald; de link naar `ex-behavioral-3` in Wat er brak is tekst geworden. Link naar `03-15-shiller-excess-volatility` uit "Waar we zijn" gehaald (hoogstens twee eerdere colleges).

**Open punten voor de feitencontroleur.**
1. Toy stap 2: oud 300^0,88 = 151,33 en 50^0,88 = 31,25 waren fout; nu 151,31 en 31,27 (nagerekend), V2 = −6,11 ongewijzigd.
2. BT-profiel "6,5% bij één jaar, 1,4% bij twintig jaar, exacte kolom tot op een half procentpunt" en "9 tot 13 maanden", "8 maanden": uit NBER w4369, niet nagekeken.
3. Odean-tabel: PGR 0,148 en PLR 0,098 weergegeven als 14,8% en 9,8% "gerealiseerd"; BarberOdean2001-periode samengevat als 1991–1997 (bron: feb 1991–jan 1997).
4. Royal Dutch/Shell: "sinds begin twintigste eeuw" (bron 1907) en "jaren tachtig en negentig" (bron 1980–1995).
5. "Risicoaversie van dertig" bij [](#03-13-equity-premium-puzzle) en "hetzelfde feit als de te grote beweeglijkheid" bij [](#04-20-voorspelbaarheid): consistentie met die colleges.
6. $t = 1{,}08$ voor de factor na 1980 is 1,075 afgerond; SE 2,3 pp per jaar = 12 × 0,375/1,954.

## F4

**Feitenrijen.** 14 (Benartzi-Thaler, Theorie/Myopic loss aversion): vergelijking herschreven naar "minder dan een half procentpunt onder die waarden", herleidbaar uit cel 3 (6,14 en 1,14%); brongetallen blijven geciteerd. 15 (Odean, tabel in Replicatie): PGR/PLR genoemd. 16: juist, ongewijzigd. 17: periode februari 1991 tot januari 1997. 18 (Intuïtie): "sinds 1907", "tussen 1980 en 1995". 19 (Theorie/Myopic loss aversion): "risicoaversie van dertig" wordt "vijftien of meer", conform de tabel in 03_13. Bronnen 15-18 niet online geraadpleegd; gecorrigeerd naar de gegevens van de originele artikelen.

**Lezerspunten.**
1. DSSW: "precies zoals de intuïtie voorspelde" herschreven (het tweede vermoeden uit de intuïtie klopt).
2. Overzicht: laatste bullet kondigt de handelsstudies van Odean en Barber aan.
3-7. Zie feitenrijen 18, 14, 15, 17, 19.
8. DSSW: overstap naar dynastieën legt nu uit waarom het meetkundige gemiddelde lager ligt bij meer schommeling.
9. DSSW-opzet: $\mu$ is "het aandeel noise traders in elke generatie".
10. DSSW-opzet: orde van grootte van $2\gamma$ (2,5 in het voorbeeld, 120 in de simulatie, beide uit cellen).
11. DSSW: "Om te zien of ... is dus meer geschiedenis nodig".
12. Joint hypothesis: "Elke toets van efficiëntie is tegelijk een toets van een model".
13. Shleifer-Vishny: *performance-based arbitrage* krijgt omschrijving in de eerste alinea.
14. Samengevat: premie-bullet noemt de reden (minder vaak verlies).
15. Replicatie/DBT: twee zinnen na de figuur samengevoegd met "omdat".

**Navertel-toets.** Geen sectie week af; H3 (twee beweringen in `prop-behavioral-dssw-rendement` en `prop-behavioral-sv`) blijft een bewuste keuze uit F1.

**Controle.** prose_stats PASS (5479 woorden), nb_numbers geen nieuwe meldingen, nb_outputs identiek (geen code gewijzigd), rewrap en jupytext --sync gedraaid.

## R9-1 (F6b, ronde 9+)

- **Feitelijke fout 1 ("exact")** gedaan: Verschil-regel zegt nu "op 20 000 getrokken reeksen per horizon".
- **Feitelijke fout 2 (momenten simulatie)** gedaan: nagerekend dat 9,35/20,32/4,48/7,53% de log-momenten van Goyal-Welch 1926–1990 (CRSP_SPvw, ltr) zijn; de tekst noemt die bron.
- **Feitelijke fout 3 (9–13 en 8 maanden)** open: niet na te gaan zonder de pdf van w4369; onveranderd.
- **Verbetering 1, symbolen** gedaan: DSSW-opzet kondigt $\lambda^{j}_t$ als positie (niet de verliesaversie) en $r$ als dividend = risicovrije rente aan; joint hypothesis zegt dat $r_{t+1}$ daar het log rendement is.
- **Verbetering 1, drie premies** gedaan: na de eerste simulatiecel een alinea die 4,87% (log) aan 6,7% (rekenkundig, replicatie) koppelt en zegt waarom $h^{*}$ toch korter is dan het jaar uit de theorie (risicovolle obligatie, volledige CPT).
- **Verbetering 2, getallen in replicatieproza** gedaan: DBT-alinea en beide BT-alinea's hebben nu hoogstens drie getallen; "9,6 maanden" (nominaal) bij de reële waarde vervangen door een verwijzing naar de kolom $\lambda = 2{,}5$.
- **Verbetering 3, terugverwijzingen** gedaan: vier verschillende vormen zonder nummer (Myopic, DSSW-toy, SV, joint); intuïtie en resultaat bij Shleifer-Vishny gaan nu beide over de snelheid waarmee inleggers vluchten ($a$).
- **Helderheid 311–312** gedaan; **$\phi$ en $(1-\varrho\phi)$** gedaan met Cochrane (2008): 0,9638, 0,941, 0,093 (geciteerd, zelfde waarden als in 04_20).
- **Taal 64–66, 1160–1161, 200–201, 466–468** gedaan (herschreven, geen zinnen toegevoegd).
- **Toy kansweging** gedaan: bijzin dat de formule pas in de theorie komt.
- **Code** gedaan: DBT-cel gesplitst in `months`, `window`, `compound`; SV-tabel via `sv_grid`, `sv_table`; commentaar bij de vorm van `x` in `cpt_lognormal` en bij `boot_idx`; alinea vóór de bootstrapcel legt de modulo-truc uit. Uitvoer voor/na identiek (alleen de celkop van cel 13 verschilt).
- **Replicatie, maatstaf "Geslaagd"** gedaan: bijzin dat De Bondt en Thaler gelijk wogen, en dat de waardegewogen factor minder haalt.
- **Oefening 3** gedaan: vraag 3 vraagt nu een voorspelling met (2) en vergelijking met de benadering; uitwerking (3) apart met factor 4 tegen 3,7.
- Woorden: 5479 → 5757; prose_stats PASS; nb_numbers alleen nieuw: 0,9638, 0,941, 0,093 (geciteerd).
