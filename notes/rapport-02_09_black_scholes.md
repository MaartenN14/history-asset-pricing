STATUS 02_09_black_scholes F6b words=5239 prose=PASS open=0 cijfer=8,5 min=8

# Rapport 02_09_black_scholes (workflow-herziening)

## F0

**Nulmeting.** `02_09_black_scholes.md  words 4812  sent_mean 20.7  sent_p90 36  sent_gt40 11  para_mean 55  dash 30  semicol 35  motief 6  Lnum 0  deel 0  u_form 1  je_form 0  taboo 1  stopw 6  calque 2  engquote 18`. `--where`: r. 48 "epistemisch", r. 414 "Twee dingen". Lengte is niet het probleem; zinnen, streepjes, puntkomma's en citaten wel.

**Vijf grootste problemen.**
1. *Taal*, overal: gemiddelde zin 20,7 woorden, 11 zinnen boven 40, alinea's van 55 woorden, 30 gedachtestreepjes, 35 puntkomma's. Zwaarst in *Simulatie* (r. 643–652, 725–742) en *Replicatie* (r. 873–889).
2. *Engelse citaten midden in de zin* (18): *Intuïtie* r. 82, 99–108, note r. 117–119, replicatieblok r. 780–791, *Wat er brak* r. 1057, 1061.
3. *Structuur*: imports-cel in *Overzicht* (r. 62); Overzicht zonder vraag-antwoord en lijst; geen routekaart en geen *Samengevat*; toy met twee cellen en zonder tabel hand/code; simulatie met drie vragen (Derman-Kamal, frequentie, verkeerde $\sigma$); cellen zonder zin ervoor of erna (r. 593, 684, 845, 891, 984).
4. *Replicatie*: blok 1 ≈ 260 woorden vol citaten; getallen in proza (r. 873–889, 1015–1020) zonder tabel origineel/hier en zonder oordeel "Geslaagd"; "maart 2025, juli 2011" (r. 1019) uit geen cel herleidbaar.
5. *Jargon en verboden woorden*: "epistemische status (motief 3)" r. 48, "motief 1" r. 587, 734, 1022, 1196, "Het verrassende" r. 85, "Leg die $t$-waarde naast" r. 1022; oefening 1 is geen instap, geen uitwerking eindigt met "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `02-09-black-scholes` (8 lectures), `thm-black-scholes-ito` en `thm-black-scholes-feynman-kac` en `eq-black-scholes-pde` (03_17), `thm-black-scholes-hedge-pnl` (08_38), `fig-black-scholes-smirk` (04_21, 05_29), `fig-black-scholes-vrp` (04_21, 05_29). Inhoudelijk aangehaald: de binomiale boom met $u$, $d$ (03_11), Mertons resultaat over Amerikaanse calls (03_17), "VIX gemiddeld vier punten boven de latere volatiliteit" (04_21, 05_29), de CAPM-afleiding (02_08). Niet aangehaald: `eq-black-scholes-dk`, `cel-`/`fig-black-scholes-hedgefout`, alle `ex-black-scholes-*`.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Intuïtie | ontdekkingsverhaal (juni 1969, afwijzingen JPE/REStat) | 110 | anekdote, geen mechanisme |
| Intuïtie | note CBOE-opening, Galai, "traders use the formula" | 95 | anekdote; één zin naar Overzicht |
| Intuïtie | Sprenkle/Boness/Samuelson met citaten | 60 | naar geschiedenisalinea Overzicht, ingekort |
| Theorie | Samuelson "less than 1 cent" bij Itô | 35 | nevenresultaat |
| Theorie | note CAPM-route: stochastische rente | 25 | niet aangehaald (Amerikaanse call blijft, 03_17) |
| Theorie | Harrison-Kreps- en warmtevergelijking-zinnen | 40 | vooruitblik, niet nodig voor de vraag |
| Simulatie | put/call-verwarring en $N+1$-uitleg bij Derman-Kamal | 110 | detail; verschil blijft in de tabel |
| Simulatie | verkeerde $\sigma$ (cel en tekst) | 130 | tweede simulatievraag; naar oefening 2 |
| Replicatie | citaten Rubinstein, CJP, Derman-Kani in blok 1 | 150 | citaat in plaats van parafrase; blok > 250 |
| Replicatie | $\sqrt{T}$-regelmaat, Derman-Kani in proza | 90 | niet uitgewerkt; naar tabel |
| Wat er brak | risico of vergissing ingekort tot 120 | 70 | te lang |
| Oefeningen | ex-1 deel 1 ingekort | 40 | ex-2 wordt afleiding |
| **totaal** | | **≈ 955** | |

**Verwachte lengte.** 4.812 − 955 ≈ 3.860; erbij komen routekaart, *Samengevat*, vraag-antwoord en lijst, zinnen rond cellen, oordelen onder tabellen, een instapoefening en "Wat dit leert" (≈ 1.000). Verwacht 4.800 tot 5.100. Geen splitsing.

## F1

**Eindmeting.** `words 4917  sent_mean 14.2  sent_p90 22  sent_gt40 0  para_mean 40  dash 0  semicol 9  motief 0  u_form 0  taboo 0  stopw 4  calque 0  engquote 1` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1`: foutloos, geen warnings in de uitvoer.

**Geschrapt of verplaatst.** Ontdekkingsverhaal en CBOE-note (anekdote); Sprenkle/Boness/Samuelson naar de geschiedenisalinea; Samuelson "1 cent", Harrison-Kreps, warmtevergelijking (nevenzaak; `HarrisonKreps1979` niet meer geciteerd); stochastische rente uit de CAPM-note (niet aangehaald, Amerikaanse call blijft voor 03_17); put/call-verwarring bij Derman-Kamal (detail); $\sqrt{T}$-regelmaat (niet uitgewerkt); alle Engelse citaten geparafraseerd; replicatieblok 1 van ≈ 260 naar ≈ 170 woorden; *risico of vergissing* naar 117 woorden. Verkeerde-$\sigma$-simulatie naar oefening 2 (tweede simulatievraag). Oud ex-1 deel 2 (lange gammapositie, cel met 1,109/0,986/0,996) geschrapt; oud ex-2 (CRR) is nu deel 2 van de instap.

**Toegevoegd.** Vraag-antwoord en lijst in *Overzicht*, *theorie of feit*-alinea; drie voorspellingen aan het eind van *Intuïtie* (H12); toy als opzet-tabel, zes stappen, één cel, tabel hand/code; routekaart, genummerde aannames, lees-zin bij elke vergelijking, beide richtingen van de formule (H6), toy-getallen $q = 0{,}6$, $\Delta_0 = 0{,}624$, $0{,}648$ in de theorie (H11); *Samengevat*; tabel origineel/hier voor Derman-Kani en verwacht/hier voor de VIX, met oordeel; instapoefening ($K = 110$, $C_0 = 4{,}7018$); "Wat dit leert" bij elke uitwerking.

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- cel 2+3 (boomtabel, $p$-tabel) → één cel met tabel hand/code; alle waarden gelijk (10,3603, 7,0439, 19,1902, 1,2527, Δ's, B's). Boomtabel en rendement aandeel per stap verdwenen als uitvoer.
- oude cel 4 gesplitst in drie cellen (`bs_price`/`bs_greeks`, `implied_vol`, voorbeeld); uitvoer identiek.
- Derman-Kamal, frequentietabel, figuur hedgefout: identiek (volgorde van `rng`-trekkingen behouden).
- verkeerde-$\sigma$-tabel verhuisd naar oefening 2, na de replicatie; waarden identiek omdat de replicatiecellen geen `rng` gebruiken.
- nieuw: vergelijkingstabel Derman-Kani (origineel 18%/8%, hier 0,2210/0,1095 op 49 dagen, 19 van 19).
- VIX-cel: tabel kreeg kolom "verwacht"; `monthly_vrp` verhuisd uit de figuurcel; nieuw: "meest negatieve maandeinden: 2020-02, 2008-09, 2008-08, 2025-03" (vervangt het onherleidbare "maart 2025, juli 2011").
- oefening 1: nieuw "C_0 bij K = 110: 4.7018"; CRR-figuur en foutregel identiek. Lange-gammacel verdwenen. Oefening 3 identiek.

**Afvinklijst §11.9, wat niet voldoet.** Na de imports-cel volgt direct de opzet, zonder eigen zin erna (zoals in de template). Twee replicatieblokken; het tweede blijft omdat `fig-black-scholes-vrp` in 04_21 en 05_29 wordt aangehaald. Overige: ok.

**Labels.** Geen verdwenen of verhuisde labels; de labelset is identiek aan HEAD. Citatie `CoxRossRubinstein1979` staat nu in oefening 1.

**Open punten.**
1. Derman-Kamal: onze spreiding ligt 5 à 10% boven hun 0,41 en 0,20; oordeel "Gedeeltelijk geslaagd", oorzaak (telconventie) niet vastgesteld.
2. Tabellen van Boyle-Emanuel en Carr-Wu niet ingezien (ongewijzigd t.o.v. HEAD).
3. Derman-Kani-getallen (18% bij 90%, 8% bij 102%) komen uit de vorige versie van de tekst; F2 moet ze tegen de bron houden.
4. Tweede replicatie en de lengte van de theorie (Greeks-tabel, drie dropdown-bewijzen) zijn de eerste kandidaten als F4 woorden nodig heeft.

## F4

**Meting.** `words 5013  sent_mean 14.4  sent_p90 23  sent_gt40 0  semicol 11  stopw 5  engquote 0` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings. Labelset identiek aan HEAD; `fig-black-scholes-vrp` blijft. Nieuwe citatie `Black1976` (bestond al in de bib).

**Feitenlijst (6 fouten, 3 niet herleidbaar): alles opgelost.** Stap 4 wordt nu $0{,}62399 \cdot 100 = 62{,}3991$. $S_t$: de verwijzing naar L2 is weg ("in L2 heette ze $P_t$"). $\Pi$ blijft de gekochte positie; de hedgewinst heet $\mathrm{PL}_T$ en de hedgeportefeuille $H$. De bèta's heten $\beta_{C,m}$ en $\beta_{S,m}$. De $N+1$-verklaring is geschrapt.
- **Derman-Kamal 0,41/0,20 en "exact hun 0,443/0,222":** vergelijking geschrapt, alleen de vorm blijft. De kolom "Derman-Kamal SD" is uit de cel. Het oordeel "Gedeeltelijk geslaagd: de vorm klopt, de getallen zijn niet tegen de bron te houden" steunt nu op onze simulatie tegen de vuistregel (0,4295 tegen 0,4432; 1,96).
- **Derman-Kani 47 dagen, 31-1-1994, 18%/8%:** geschrapt. Het blok zegt alleen dat Derman en Kani hetzelfde patroon beschrijven. De vergelijkingscel is nu een tabel verwacht/hier voor de helling bij een week, zeven weken en een jaar (0,2160 / 0,0873 / 0,0289; 19 van 19).
- **L10, r. 282, "$Z_t$ zoals in L9":** buiten mijn bestand, niet aangepast. Melden bij L10.

**Onnauwkeurigheden.** Opgelost:
- Bachelier-zin;
- drift "vrijwel nul", met de $t pprox -2{,}3$ benoemd en drift of discretisatie als open vraag;
- factor $\sqrt{\pi/2}$;
- "dalen links van de termijnkoers";
- $\delta W_k$ in het Itô-bewijs;
- tijdsvariabele $s$ in plaats van $u$;
- $H$ in plaats van $X$.

Niet aangepast: $d$ naast $d_1$ en $t$ als $t$-waarde (standaardnotatie); "meetkundige" Brownse beweging staat in L10.

**Lezerspunten: alle 15 behandeld.**
1. Overgang naar $\mathbb{Q}$: alleen de drift verandert, $W^{\mathbb{Q}}$ gedefinieerd, de werkelijke kansen zijn "niet fout".
2. Stap van gamma-gewogen variantie naar vega: identiteit $\sigma S^2\Gamma	au = 
u$, met getal 0,99.
3. De standaardfout van 2% in één regel herhaald, beide keren.
4. Het voorbehoud over hedgeruis is herschreven als twee voorbehouden.
5. Sprenkle-zin geschrapt in plaats van de formule toe te voegen (kost woorden, draagt de vraag niet).
6. Drift-tegenspraak opgelost.
7. Dikkere linkerstaart: één zin toegevoegd.
8. Waarom out-of-the-money, en Black (1976) in proza.
9. $\sigma_r$ heet nu $\sigma_g$.
10. Formule voor $B$ in het recept.
11. Oefening 3 geherformuleerd.
12. Chicago en Yale in één regel, stochastic discount factor uitgelegd.
13. Aandeel 1,06 naast optie 1,2527.
14. Europees en Amerikaans uitgelegd.
15. Datum van de momentopname (11-9-2026) in de proza.

Verder één munteenheid (euro, ook in het voorbeeld van Black) en één naam voor de hedgewinst ("P&L", en "spreiding van de P&L"; ook in de figuurtitel).

**Betaald met schrappen.** Geschrapt:
- de Derman-Kamal- en Derman-Kani-vergelijkingen;
- de Amerikaanse-puts-kanttekening;
- de zin over "corporate liabilities";
- "Black vertelde later";
- "Wat de premie betekent";
- de overschattingszin bij de vuistregel;
- de openingszin van Opzet;
- de arbitragezin in Intuïtie.

Netto +96 woorden.

**Navertel-toets.** Afgeweken:
- *De Black-Scholes-formule*: de overgang naar $\mathbb{Q}$ is uitgelegd als "alleen de drift verandert", met $W^{\mathbb{Q}}$.
- *Simulatie*, slot: de 2% is uitgelegd, en het voorbehoud is gesplitst in weinig hedgen en een niet-constante $\sigma$.

**`nb_outputs`-diff tegen F1.** Kolom "Derman-Kamal SD" weg. Derman-Kani-tabel vervangen door verwacht/hier. Figuurtitel hedgefout gewijzigd (alleen de PNG). Kolomnaam `sigma_g`. Alle aangehaalde getallen gelijk.

## F5-1

**Meting.** words 5199, `--check` PASS. Sync en execute met `HAP_OFFLINE=1` foutloos, geen warnings. Labels gelijk aan HEAD. Aangehaalde getallen gelijk; de `rng`-volgorde is behouden.

**Top drie.**
1. *Replicatie.* Gedaan.
   - Geen getal uit de originelen is in de bib of in `notes/` herleidbaar. Beide blokken zeggen daarom waarom alleen teken en vorm te toetsen zijn.
   - Smirk: richting van de afwijking erbij (Amerikaanse puts maken de helling eerder steiler).
   - VRP: "fout in de code" vervangen door richting en grootte van de verschillen (hele markt beweegt harder, dus het verschil ligt eerder lager; 30 kalenderdagen ≈ 21 handelsdagen).
   - 2025-03 genoemd.
2. *Opbouw.* Gedaan.
   - Simulatie opent met haar conclusie.
   - De Derman-Kamal-cel heet "controle van de code, geen replicatie"; het oordeel is weg.
   - Motief: het argument staat alleen in de simulatie. De VRP-slotalinea verwijst ernaar met $t = 12{,}8$ (de 1,8-vergelijking staat nog in oefening 3).
3. *Notatie en taal.* Gedaan.
   - $R^f$ bruto en $r$ continu gemeld als afwijking; $P_t$ voor de koers weg.
   - Log-moneyness gedefinieerd met getal; de 42 vertragingen verklaard (overlap 20 van 21 dagen).
   - "definieert het tijdvak", "prijsde zichzelf", "quoteren" en "men" herschreven; puntkomma's tussen zinnen geknipt.

**Overige punten.**
- Toy: $B$ nu ook in stap 2 en 3. Gedaan.
- Code:
  - frequentiesimulatie uit de verborgen figuurcel naar een zichtbare cel met tabel (helling −0,4773);
  - replicatiecel gesplitst (termijnkoersen tonen, dan implied volatility);
  - `print` vervangen door tabellen in voorbeeld-call, Derman-Kamal, replicatie en VRP.
- Smirk-bijschrift herschreven ("van diepe puts naar de termijnkoers").
- Oefening 1.2: de lijnen $\pm 1/n$ gemotiveerd. Het bezwaar "tweede uitbreiding" is afgewezen: STYLE §11.7 staat een instap met twee deelvragen op het toy toe.

**Nieuwe uitvoer.** De tabel van de zeven frequenties is nieuw als tabel; de getallen stonden eerder alleen in de figuur. Verder een tabel met termijnkoersen, controlerijen onder de Greeks, en kolommen premie/vega in de Derman-Kamal-tabel.
- Diffcontrole: "42 vertragingen" nu verklaard als twee keer het venster van 21 dagen (zoals `lags=42` in de code); geen codewijziging, dus geen nieuwe execute.
- Diffcontrole: de beweringen over Amerikaanse puts (smirk-blok) en "de hele markt beweegt harder" (VRP-blok) geschrapt, want zonder cel of bron.
- Diffcontrole: sommatie-index in het Itô-bewijs van $k$ naar $j$, zodat $k$ alleen log-moneyness is. Na de fixes words 5172, `--check` PASS, sync gedaan.

## F6-1

**Meting.** words 5239, `--check` PASS, sync gedaan. Geen code gewijzigd, dus geen nieuwe execute; labels en `fig-black-scholes-vrp` ongewijzigd.

**Naadpunten.**
- Notatie: $d$ (daalfactor) en $\delta$ (dividendrendement) toegevoegd aan de gemelde afwijkingen.
- Markt en SDF: $\beta_{C,\text{mkt}}$ in plaats van $\beta_{C,m}$, met één zin dat $m$ in de reeks de SDF is.
- "alpha"/"alfa": komt in L9 niet voor, geen actie.
- Chronologie Merton: "daarna … opnieuw" herschreven naar "al vanaf 1969 … in 1973 het evenwicht" (zoals L10 r. 21–50).

**Top drie uit de eindbeoordeling.**
1. $\mathbb{Q}$ verwijst nu terug naar [](#thm-efficiente-markten-martingaal) (maat $Q$ in L6). $d$: zie hierboven. Gedaan.
2. Replicatie. De VRP-getallen zijn uit de lopende tekst; het oordeel noemt alleen de verwachtingen, de getallen staan in de tabel. Gedaan. Een kolom "origineel" is afgewezen: geen getal van Rubinstein, Whaley of Carr-Wu is in de bib of in `notes/` herleidbaar (STYLE §11.11 "Feiten"; eerder besluit bij F4).
3. Toy: knooptabel met alle koersen per stap vóór de stappen. Gedaan.
- Diffcontrole: "drie punten" naar "vier punten" in Opzet (S_t, R^f, r, d/δ); `--check` PASS, sync gedaan.
