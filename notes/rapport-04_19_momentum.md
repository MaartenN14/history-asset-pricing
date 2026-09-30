STATUS 04_19_momentum F4T words=5654 prose=PASS open=6 cijfer=- min=-

Kern: is de voortzetting van relatieve rendementen (momentum) een beloning voor risico of een vergissing? Het feit staat vast (ongeveer 1% per maand, niet verklaard door het driefactormodel), een verklaring ontbreekt, maar het risico is voorspelbaar, zodat schalen met voorspelde volatiliteit de Sharpe-ratio bijna verdubbelt.

## F0

prose_stats (voor): words=5359 sent_mean=21,2 sent_p90=37 sent_gt40=18 para_mean=64 semicol=40 motief=6 u=1 je=1 calque=3 colon_mid=10,6 para_one=31 telegram=1 tmpl=3 -> FAIL op 13 drempels (niet op words).

Vijf grootste problemen:
1. Taal overal: 18 zinnen > 40 woorden, 40 puntkomma's, 31% alinea's van één zin, dubbele punt als lijm (o.a. Intuïtie r. 101-109, Replicatie r. 821-831, 1045-1056).
2. Twee simulaties (Simulatie (a) r. 523 en (b) r. 627) in plaats van één steekproefvraag.
3. Getallenbrij in proza: JT-alinea r. 218-225, JT2001 r. 331-338, DM r. 419-424, replicatie-oordelen r. 821-831 en 1045-1056; geen tabel origineel/hier bij JT en DM, geen "Geslaagd".
4. Structuur: imports-cel in Overzicht, geen routekaart, geen Samengevat, bewijzen open (drie > 6 regels), toy met drie mechanismen en zonder tabel hand/code, oefening 1 geen instap.
5. Motiefjargon ("motief 1" 5x, "motief 3"), "u"/"je", "alfa", "excess rendement", "beprijsd", "lecture", Engelse citaten midden in zinnen, "haar" voor zaken.

Schraplijst (schraptoets §11.11; labels gegrept in lectures/, alleen `eq-momentum-carhart` en `04-19-momentum` worden elders aangehaald):
| passage | woorden | eis niet gehaald |
|---|---|---|
| Simulatie (b) GARCH-schalen, proza + bijschrift | ~300 | 1, 2 (fig-momentum-sim-b niet aangehaald), 3 (motief al in schalen/JT-replicatie) |
| Oefening ex-momentum-3 (σ_μ) | ~290 | 1, 2; kern (1% vraagt 12% spreiding, CAPM 1,8%) als twee zinnen naar Simulatie |
| JT tabel I details (6/6 met/zonder week, event time 9,5%/4%) | ~60 | 1 |
| JT2001 12,17%/−0,44% en 1,17% | ~30 | 1 |
| Carhart PR1YR-constructie, 1892 fondsen, industrie-verwijzing | ~70 | 1 |
| DM-getallen in Theorie (dubbel met replicatie) | ~50 | 1 |
| Wat er brak: Rouwenhorst >1%, MG 10,2%/t=7,71, AMP −0,60/1,45, citaten | ~90 | 1 |
| 12-0-vergelijking uit toy -> oefening (instap) | ~0 netto | verplaatst |
Verwachte lengte na schrappen en toevoegingen (routekaart, Samengevat, lijst, tabellen): ~5.300-5.600. Geen splitsing nodig.

## F1

Eindmeting: words=5578 sent_mean=17,5 sent_p90=28 sent_gt40=0 para_mean=49 semicol=8 motief=0 colon_mid=0,7 para_one=8 tmpl=2 -> PASS. (Boven het doel van 5.500, onder de grens.)

Geschrapt of verplaatst:
- Simulatie (b) GARCH-schalen met cellen en figuur: tweede simulatie; de grootte-orde van de winst staat al in de e^{…}-tabel van Theorie, het oordeel in de BSC-replicatie verwijst nu naar geval 1-3.
- Oefening σ_μ (ex-momentum-3 oud): kern als handberekening in Simulatie; `optimize`-import vervalt.
- 12-0-regel uit het toy -> nieuwe instapoefening `ex-momentum-toy`.
- Bewijzen van de drie proposities en van cor-momentum-schalen in dropdown; factormodeldeel van de decompositie apart als `cor-momentum-factor` (H3).
- Detailgetallen JT, JT2001, Carhart, DM (Theorie) en Wat er brak: getallenbrij, niet nodig voor de vraag.
- Vooruitverwijzing naar 04-23-behavioral en 04-25-industrie geschrapt (niet nodig).
Toegevoegd: routekaart, Samengevat, lijst in Overzicht, tabel hand/code in het toy, markdown-tabellen origineel/hier bij JT en DM met oordeel "Geslaagd".

nb_outputs-diff (voor -> na):
- cel toy: print-regels vervangen door tabel "met de hand / code" (zelfde getallen); 12-0-uitvoer verhuisd naar oplossing instapoefening (identiek).
- cellen 7-8 oud (GARCH + figuur) verwijderd; celnummers verschoven.
- JT-tabel: kolommen "CAPM-alfa"/"FF3-alfa" -> "CAPM-alpha"/"FF3-alpha", waarden gelijk.
- BSC-cel: `TARGET = 0.12` nu daar gedefinieerd; uitvoer gelijk.
- crashfiguur: nieuwe titel en x-label (png-grootte anders).
- oefening bèta: Monte Carlo −0,357 -> −0,349 (rng-stroom verschoven door weggevallen GARCH-cel); tekst noemt alleen formule −0,36.
- simulatie (a): `argsort().argsort()` vervangen door `stats.rankdata`; uitvoer identiek.
Geen door de tekst aangehaald getal veranderd.

Afvinklijst §11.9, niet voldoend: words 5578 iets boven doel 5.500 (onder grens). Overige: ok.

Labels: weg `fig-momentum-sim-b`, `cel-momentum-sim-b`, `ex-momentum-3` (nergens aangehaald); nieuw `cor-momentum-factor`, `ex-momentum-toy`.

Open punten voor de feitencontroleur:
1. JT 1993: januari "ongeveer −7%" en "1,66% daarbuiten" - voor welke strategie (6/6?) en welke tabel.
2. Carhart 1997: 0,82% per maand, t = 4,46, juli 1963-december 1993 (tabel II).
3. JT 2001: 1,39% (6/6, 1990-1998) en −0,26% per maand in maand 13-60, t = −4,65 (tabel V); omkering sterk 1965-1981, zwakker 1982-1998.
4. DM 2016: 232/32 en 163/8, bèta −0,70/−1,51, 14 van 15 slechtste maanden.
5. Parafrasen: Fama-French 1996 "main embarrassment" -> "grootste verlegenheid"; FF 2008 "premier anomaly"; BSC "much greater puzzle"; Santa-Clara 2026.
6. Kleuren in de crashfiguur: bijschrift en tekst zeggen "rood" (COLORS[1]) en "grijs" (COLORS[7]); controleren in de build.
7. "twaalf Europese landen" (Rouwenhorst) en "acht markten" (AMP) blijven zonder getallen staan; controleren.
8. Theorie: "bij decielen 2φ(q)/p ≈ 3,5, limiet ≈ 1,05 bij σ_β = 0,3" komt uit de oefeningscel (1,053).

## F4

Feiten: geen rij fout of niet herleidbaar. Rij 13 (FF3-alpha 1,69) opgelost via cel 8 (1,687). Rij 14: tikfout "maar maar" hersteld (Replicatie > BSC). Rijen 4, 6, 7, 8, 16, 18 blijven onzeker: citaten uit bronnen die niet als tekst leesbaar waren; geen aanwijzing voor een fout, tekst ongewijzigd (rij 4 staat al als "ongeveer 7%").
Lezerspunten:
1. gedaan (Replicatie > BSC): "maar maar" wordt "tegen slechts 1,6%".
2. gedaan (Replicatie > JT): dubbele ontkenning herschreven, puntkomma weg.
3. gedaan (Simulatie): CAPM-vergelijking herschreven tot één zin met de conclusie vooraan; 1%/maand en 0,3·6% geschrapt.
4. gedaan (Theorie > Bèta): 3,5 en p=0,1 geschrapt, toy-callback eigen zin.
5. gedaan (Simulatie): 8% en 6% als standaarddeviaties van nieuws en ruis in één bijzin; 25/500 bleven in de vraagzin.
6. gedaan (Theorie > Waar komt): zin gesplitst.
7. gedaan (Simulatie): "0,06 tot 0,09 procentpunt" geschrapt, dubbele punt weg.
8. gedaan (Theorie > Constructie): zin over het vierfactormodel herschreven.
9. gedaan (Replicatie > DM): figuuraankondiging ingekort, uitleg staat in het bijschrift.
10. gedaan (Theorie > Waar komt): orde van grootte bij gamma ("in de praktijk klein").
11. gedaan: BSC-alinea opent nu met "Ook deze replicatie slaagt".
12. gedaan (Replicatie > DM): bijzin dat 1,66% toevallig gelijk is aan JT buiten januari.
13. gedaan (Oefeningen): look-ahead cursief met uitleg.
14. gedaan (Replicatie > JT): "We verwachten" in Verwachte afwijking.
15. gedaan (Theorie > Bèta): DM-alinea opent met het loslaten van de vaste bèta's (herschreven, niet toegevoegd).
Extra: "CRSP-data verschuiven de rangorde" gecorrigeerd naar French- versus CRSP-decielen (11 in plaats van 14); motief standaardfout niet langer handelend onderwerp (Schalen).
Navertel-toets: geen sectie week af (lezer-bestand); in Simulatie verdween de hoofdconclusie tussen de cijfers, nu vooraan.

## R9-1 (F6b, ronde 9+)

- **Feitelijke fouten 1-2 (JT-signaal, januari).** Gedaan: JT sorteerden zonder overgeslagen maand (variant: één week); −7%/1,66% nu bij de 6/6-strategie (ongeveer 0,95%, geciteerd); tabel toont (12/3) en (6/6) per getal.
- **Feitelijke fout 3 (oefening c).** Gedaan: constante $c$ neutraal voor regel 2, niet voor regel 3 (plafond bindt), kleine look-ahead.
- **Feitelijke fout 4 / DM 11 tegen 14.** Gedaan: als vermoeden gebracht met twee mogelijke oorzaken (rangschikking French/CRSP, bear-definitie), "Minder goed klopt de telling".
- **Replicatie JT, $t$ 3,74 tegen 5,50.** Gedaan: in verwachte afwijking aangekondigd (NW, $K = 1$) en in het oordeel besproken.
- **Replicatie BSC.** Gedaan: oordeel begint met "Geslaagd"; gewicht 0,90 niet meer als "klopt" (artikelgetal niet beschikbaar), nu uitgelegd als gemiddelde blootstelling.
- **Helderheid.** Gedaan: reden lange horizon (spreiding en onderreactie voorspellen in jaar 1 hetzelfde); mechanisme negatieve helling (optimaal gewicht daalt sneller dan $1/\sigma_t^2$, dus meer dan geval 1); $q$ in eq-momentum-schalen wordt $\bar g$; $q_{p,t}$ bij JT vervangen door 90e/10e percentiel; orde van grootte $\mu_i$ en $\gamma_{ii}$ uit de simulatiecel; "ruiziger" nu 0,06-0,09 tegen 0,47 procentpunt.
- **Opbouw.** Gedaan: laatste bullet Samengevat is nu een samenvatting (lange horizon scheidt). H11: simulatiebèta's (SD 0,4) gekoppeld aan het toy.
- **Toy.** Gedaan: stap 4-5 gebruiken dezelfde aandelen A-D zonder nieuws.
- **Taal.** Gedaan: hardop-zinnen r. 789, 1042, figuurtitel ("slechts één"), Overzicht r. 61; eenzinsalinea's r. 731 en 811 aangevuld met inhoud. Lange zinnen opgesplitst (p90 28).
- **Code en figuren.** Gedaan: print van tabeltitels (r. 727) verwijderd; DM-cel met benoemd tussenresultaat `market_24m`; figuur DM krijgt waarop te letten (knik rode wolk bij nul). Na herberekening offline verschillen alleen de figuurtitel-png, de weggevallen print en de celkop.
- **Deels.** $p$ blijft fondsindex in Carhart (standaardnotatie) en fractie in de bètapropositie; kwantielbetekenis is weg.
- Woorden: 5.945 (prose_stats PASS); nb_numbers: nieuwe meldingen alleen geciteerde bronnen (0,95; 3,74 JT1993) en het berekende 0,47.
