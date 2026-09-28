STATUS 03_17_termijnstructuur_real_options F6b-2 words=5108 prose=PASS open=0 cijfer=- min=-

# Rapport 03_17_termijnstructuur_real_options (workflow-herziening)

## F0

**Nulmeting.** `prose_stats`: `words 3034  sent_mean 20.1  sent_p90 36  sent_gt40 9  para_mean 50  dash 0  semicol 16  motief 4  deel 1  je_form 6  calque 1  engquote 2` → FAIL. Het woordtal is fout: de twee `\$` (r. 496 `\$0,89 miljoen`, r. 1196 `\$650.000`) verschuiven in `prose_stats` de koppeling van de inline-`$`, zodat alles tussen die twee als wiskunde telt. Met `\$` vervangen door "USD": `words 4726  sent_mean 19.5  sent_p90 33  sent_gt40 14  para_mean 50  semicol 33  motief 5  deel 1  je_form 6  calque 1  engquote 3`. `--where`: r. 57 "epistemisch". Lengte is dus niet het probleem; stofdichtheid, zinnen en structuur wel. (Tool-melding voor de orkestrator: `prose_stats` negeert `\$` niet.)

**Vijf grootste problemen.**
1. *Taal*, overal: gemiddelde zin 19,5 woorden, 14 zinnen boven 40, 33 puntkomma's, alinea's van 50 woorden. Zwaarst in *Theorie* (r. 419–424, 452–457, 465–470, 489–496, 531–538, 598–603), *Replicatie* (r. 1018–1022, 1120–1129) en *Wat er brak* (r. 1216–1229).
2. *Structuur*: imports-cel in *Overzicht* (r. 67); Overzicht zonder vraag-antwoord en lijst; geen routekaart, geen *Samengevat*; toy met twee cellen, drie mechanismen (obligatie, Amerikaanse obligatieput, mijn) en geen tabel hand/code; *Simulatie* met drie vragen (paden, schatting, LSM tegen boom); cellen zonder zin ervoor of erna (r. 705, 785, 1076, 1133, 1159); theorema's met open bewijs van 10 tot 12 regels (r. 291, 343).
3. *Notatie* botst met de setup: $r_t$ = korte rente (setup: netto simpel rendement), $P(t,T)$ hoofdletter, $R = 1{,}05$ bruto rente in de mijn, $\gamma$ in CIR (risicoaversie), $\beta$ bij McDonald-Siegel (discontofactor/bèta), $q$ = productie naast $q$ = risiconeutrale kans, $K$ = aantal uitoefenmomenten naast uitoefenprijs, $C(t_j)$ als kasstroom, $c$ = kosten (consumptie).
4. *Jargon*: "epistemische status (motief 3)" r. 57, kopje en tekst "Het 2%-motief" r. 749, 815, 1213, 1423, "Deel V" r. 1231, zes keer je-vorm (r. 32, 84, 86, 1365, ...), Engels citaat "risk that was priced" r. 1228; de standaardfout van 2% verwijst nergens naar [](#00-01-rendementen).
5. *Getallen in proza zonder tabel en oordeel*: r. 744–747, 815–820, 890–895, 1018–1022, 1120–1129, 1186–1190; geen "Geslaagd"; geen oefening als instap, geen "Wat dit leert:". Feit: ex-3 zegt "verschillen van 1,1 en −2,9 standaardfouten", de cel geeft −1,15 en −2,86.

**Eis 2 (grep in `lectures/`).** Elders aangehaald: paginalabel (03_16, 04_18, 05_28, 08_38), `thm-termijnstructuur-real-options-affien` (05_28). Inhoudelijk aangehaald: één factor met constante marktprijs van risico, PCA op GSW met drie factoren, "lange rente beweegt op eigen kracht" (05_28 r. 24–27), tabel van Litterman en Scheinkman (05_28 r. 840), affiene modellen (08_38). PLAN.md vraagt: affiene modellen, real options (mijn), LSM; replicatie Vasicek-fit en LSM voor een Amerikaanse put. Alle drie de onderdelen blijven dus; geen andere labels worden aangehaald.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | Santa-Clara in de dankbetuiging | 30 | anekdote; UCLA-lijn blijft in één bijzin |
| Overzicht | slotalinea (samenvatting die de lijst dubbelt) | 60 | wordt vraag-antwoord en lijst |
| Toy | Amerikaanse put op de obligatie | 110 | tweede mechanisme; wordt oefening 1 (instap) |
| Theorie | Schwartz (1997), drie grondstofmodellen, Kalman | 50 | nevenresultaat, nergens aangehaald |
| Theorie | Brennan-Schwartz 1979 / Longstaff-Schwartz 1992 | 40 | ingekort tot twee zinnen (titel) |
| Theorie | CIR-evenwicht, LSM in/out-of-sample | 60 | ingekort |
| Simulatie | paden, negatieve rentes | 80 | geen steekproefvraag; verhuist naar Theorie |
| Simulatie | LSM tegen boom | 180 | tweede vraag; verhuist naar Replicatie (PLAN) |
| Replicatie | reekscodes en data in het blok | 50 | naar de cel |
| Replicatie | duration-neutrale portefeuille, \$650.000 | 45 | anekdote |
| Wat er brak | risico of vergissing van 180 naar 120 | 60 | te lang; investeringsdrempel-zin weg |
| **totaal geschrapt** | | **≈ 485** | (verhuisd, niet meegeteld: ≈ 370) |

**Verwachte lengte.** 4.726 − 485 ≈ 4.240; erbij komen vraag-antwoord en lijst, routekaart, *Samengevat*, toy-stappen en tabel hand/code, lees-zinnen, symboolnamen met orde van grootte (H2, H4), zinnen rond cellen, tabellen verwacht/hier met oordeel, een instapoefening en "Wat dit leert" (≈ 900). Verwacht 5.000 tot 5.200. Geen splitsing.

## F1

**Eindmeting.** `words 5295  sent_mean 14.8  sent_p90 25  sent_gt40 2  para_mean 38  dash 0  semicol 7  motief 0  deel 0  je_form 0  stopw 1  calque 0  engquote 0` → PASS. `--where`: geen treffers. Geen `\$` meer in het bestand, dus de telling klopt. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings in de uitvoer.

**Geschrapt.** Santa-Clara in de dankbetuiging (anekdote, UCLA-lijn blijft in één bijzin); slotalinea Overzicht (dubbelt de lijst); Schwartz (1997) met Kalman-filter (nevenresultaat, `Schwartz1997` niet meer geciteerd); Brennan-Schwartz 1979 / Longstaff-Schwartz 1992 uit Theorie (staan in de geschiedenisalinea); CIR-evenwicht met log-nut (nevenzaak); \$650.000-portefeuille (anekdote); rekenvoorbeeld van acht paden van Longstaff-Schwartz met cel (dubbelt de replicatie van tabel 1; woordbudget); oude oefening McDonald-Siegel met boom (niet aangehaald; de drempel $2I$ staat als handberekening in Theorie).
**Verplaatst.** Amerikaanse obligatieput van toy naar oefening 1 (instap); paden en modelcurves van Simulatie naar Theorie "Wat het voorspelt"; LSM tegen boom van Simulatie naar Replicatie met eigen replicatieblok (PLAN: "LSM voor Amerikaanse put"). De volgorde van alle `rng`-trekkingen is gelijk gebleven.
**Toegevoegd.** Vraag-antwoord, lijst, geschiedenis, theorie of feit in Overzicht; vier verwachtingen aan het eind van Intuïtie (H12, ingelost bij $\lambda$, de corollary, McDonald-Siegel en LSM); toy met opzet-tabel, zes stappen, één cel, tabel hand/code; routekaart, genummerde aannames (aangeroepen in het bewijs), lees-zin bij elke vergelijking, getallen bij formules (0,114 pp convexiteit in de boom, $1{,}5$ pp premie, $y_\infty = 7{,}5\%$, $\sigma/\sqrt{2\kappa} = 2{,}7\%$, $\eta = 2$, $b = 0{,}9876$); beide richtingen bij Vasicek en McDonald-Siegel (H6); *Samengevat*; tabel verwacht/hier en origineel/hier met "Geslaagd"; "Wat dit leert" bij elke uitwerking.
**Notatie.** Korte rente $i_t$ (met reden: $r$ is netto simpel rendement), ook in de boom en voor constante rentes; nulcouponprijs $p(t,T)$ klein, partiële afgeleiden als $\partial_t p$; $R^{f} = 5\%$ netto in de mijn; CIR-constante $h$ (niet $\gamma$), McDonald-Siegel-exponent $\eta$ (niet $\beta$), productie $n$ en vaste kosten $k$ (niet $q$, $f$), kosten $a$ (niet $c$), uitoefenmomenten $t_1..t_J$ (niet $K$), kasstroom $x(t_j)$, doorgaan $G$. Elke "standaardfout van 2%" linkt naar [](#00-01-rendementen).

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- toy: twee print-cellen → één tabel hand/code; alle waarden gelijk. Obligatieput-regels verhuisd naar oefening 1 (0,011999 / 0,003332 / 0,005714 / 0, gelijk).
- LSM-rekenvoorbeeld (−1,070 + 2,983X − 1,814X², 0,1144, 0,0564) verdwenen met de cel.
- padentabel: nieuwe rij "oneindig lange yield" (0,0750 / 0,0516); overige waarden gelijk.
- simulatietabel: kolomnamen p5/p95 → 5%-/95%-kwantiel; waarden gelijk.
- LSM: print-regel boom/Europees/continu → tabel origineel/hier (4,4779 / 3,8443 / 4,4867 gelijk); LSM-tabel en herhalingen gelijk; staan nu na de datacellen.
- PCA: "steepness" → "slope", kolomkop "GSW" → "hier"; nieuw: tabel verwacht/hier (tekenwisselingen 1, fouten 2,32 en 1,79).
- oefening McDonald-Siegel verdwenen (60,3; 1,422/1,408 enz.). Monte Carlo en deelsteekproeven gelijk.

**Afvinklijst §11.9, wat niet voldoet.** Twee replicatieblokken (PLAN vraagt beide). Theorie bevat een simulatie van paden (populatie-eigenschap, geen steekproefvraag). Toy heeft twee bomen onder één recept. Overige: ok.

**Labels.** Labelset identiek aan HEAD; `thm-termijnstructuur-real-options-affien` en het paginalabel blijven. Geen oefeningslabel als linkdoel.

**Open punten voor F2.**
1. p(0,2): de oude tekst had 0,907770, de berekening geeft 0,9077705 → nu 0,907771 in tekst en tabel.
2. Oefening 3: oude tekst "1,1 en −2,9 standaardfouten", cel −1,15 en −2,86 → nu zo in de tekst.
3. Brennan-Schwartz 1985 (tabellen 1 en 2: 76/44/20 cent, \$0,89 mln, 12%, variantie 8%), Vasiceks notatie $\alpha,\gamma,q$, het artikelgetal −1,813 en "twee keer de kosten" van McDonald-Siegel zijn uit de vorige versie overgenomen en niet tegen de bron gehouden.
4. Verklaring CIR $y_\infty = 5{,}2\%$ tegen Vasicek 7,5% ("vooral omdat de prijs van risico $\lambda\sqrt{i}$ is"): het convexiteitseffect verschilt ook; nagaan.
5. `tools/prose_stats.py` telt `\$` als wiskundegrens (F0: 3.034 i.p.v. 4.726); melden bij de tooleigenaar.
6. Kandidaat om terug te zetten als F3 om een concreet LSM-exemplaar vraagt (H10): het rekenvoorbeeld van acht paden, als oefening, betaald met schrappen.

## F4

**Meting.** `words 5402  sent_mean 15.0  sent_p90 24  sent_gt40 2  semicol 7  stopw 1` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos; `nb_outputs` identiek aan F1 (alleen prozawijzigingen). Labelset ongewijzigd.

**Feitenlijst.** Geen fout of niet herleidbaar (open=0); de vijf open punten uit F1 zijn door F2 bevestigd. Symboolobservaties opgelost: bij de convenience yield staat nu dat Brennan en Schwartz haar $\kappa$ noemen maar dat die letter hier de snelheid van terugtrekken is; de vaste kosten $k$ zijn uit [](#eq-termijnstructuur-real-options-mijn) verdwenen (vereenvoudiging, genoemd in de tekst), zodat $k$ alleen de LSM-index is.

**Lezerspunten.**
1. $n$ dubbel: de yield in de toy gebruikt nu $\tau$ (looptijd in jaren, zoals in Theorie); $n$ is alleen de productie.
2. $k$ dubbel: vaste kosten weggelaten (zie boven).
3. $V$ dubbel: zin toegevoegd die McDonald-Siegel aankondigt als tweede probleem met een nieuwe $V$.
4. Vasicek-bewijs: tussenregel $\int B^2 = \kappa^{-2}\int(1 - 2e^{-\kappa s} + e^{-2\kappa s})$ toegevoegd.
5. $h$: naam (hulpgrootheid), rol (snelheid naar de limiet $2/(h+\kappa^*)$) en getal 0,16 (handberekening met $\kappa^* = 0{,}1299$, $\sigma_C = 0{,}0671$).
6. $q$: "(niet de kans uit de koperboom)" bij Vasiceks notatie.
7. $\delta$: orde van grootte 1% per jaar direct bij de definitie; $\kappa$-botsing benoemd.
8. Stap 2 en 3 heten nu "de obligatie op $t=1$" en "de obligatie vandaag".
9. Waarom bij de risiconeutrale prijs: slotzin met richting (onzekerheid maakt de obligatie duurder).
10. Waarom bij de affiene klasse: opent nu met een belegger die de obligatie houdt terwijl de rente stijgt.
11. (extra) Vasicek lost de eerste intuïtievoorspelling expliciet in ($\lambda = 0$: onder $\theta$).
12. (extra) Eén zin over de panelen 2000 en 2026 (beide modellen binnen een procentpunt, uit `fit_table`).
13–15. (extra) $\eta$ als elasticiteit van de optiewaarde; $J$ momenten en $M+1$ basisfuncties genoemd; reden voor "kleinste kwadraten = maximum likelihood" (normale schok, overal even groot). Ook: CIR in beide richtingen ($\kappa^* > \kappa$: negatieve premie).

**Betaald met schrappen.** Simulatie (motief-alinea ingekort), LSM-lezing na de propositie, "Wat de modellen verklaren", lijstpunt 2 in Overzicht (≈ 50 woorden). Netto +107 woorden, binnen 5.500.

**Navertel-toets.** Geen sectie week af van de bedoeling; alleen bij "Real options" nam de lezer de mijn- en projectwaarde als één object; opgelost met punt 3.

## F6-1

**Meting.** `prose_stats --check` PASS, words 5111 (was 5402). Sync en `--execute` met `HAP_OFFLINE=1` foutloos. Labels: `alg-`, `cel-` en `fig-termijnstructuur-real-options-lsm` verdwenen (nergens aangehaald), `ex-termijnstructuur-real-options-4` nieuw; paginalabel en `thm-…-affien` (05_28) staan er nog.

**Punten, per stuk.**
1. Feitelijke fout Duffie-Kan: gedaan. Het Overzicht noemt Brennan-Schwartz (1979) nu apart ("alleen numeriek op te lossen"), en Duffie-Kan dekken Vasicek, CIR en Longstaff-Schwartz.
2. Opbouw: gedaan. De routekaart noemt de termijnstructuur als kernlijn. Toy heeft alleen de renteboom (vier stappen); de koperboom is oefening 4, met tabel hand/code (getallen gelijk). De tabel van Brennan-Schwartz en McDonald-Siegel (stelling, korte bewijsschets, $\eta = 2$) staan in één dropdown. LSM is nu één subsectie met de vergelijking voor doorgaan, de ondergrens-stelling en één tabel in de replicatie; algoritmeblok, tweede replicatieblok en de figuur met herhalingen zijn weg. LSM zit in het ene replicatieblok (bron, wat, verwachting).
3. Replicatie: gedaan. De alinea na de schattingstabel, die na de curvetabel en de twee na de figuur verwijzen naar de tabel, met één conclusie per alinea; er blijft één getal over ($t = 0{,}1003/0{,}0608 = 1{,}6$, handberekening uit de tabel).
4. Helderheid: gedaan. Eén naam "lange yield" (ook in bijschrift en Overzicht); Laguerre-polynomen en Svensson-curve elk in één bijzin; $a$ tegen $a_0, a_1$ benoemd.
5. Taal: gedaan. Telegramzin, Santa-Clara-zin en "precies" in "Real options" herschreven; Chicago- en Yale-lezing elk met een bijzin.
6. Code: gedaan. Parameters in `vas` en `mine` (dicts); uitoefenstap in `lsm_put` in twee benoemde regels; tekenkeuze PCA in een benoemde regel; rekenwerk en presentatie van LSM gescheiden (de herhalingscel is weg).
7. Oefening 3: aandeel eerste component (0,93 → 0,91) toegevoegd.

**`nb_outputs` tegen F4.** Toy-tabel zonder koperregels; koperwaarden nu in oefening 4, gelijk. LSM-tabellen samengevoegd, waarden gelijk; "continu uitoefenbaar" (4,4867) en de herhalingstabel verdwenen. Omdat de herhalingscel `rng` gebruikte, veranderde de Monte Carlo van oefening 2: 0,82962 (0,00044) → 0,82983 (0,00043); de tekst zegt nu "0,7 standaardfout onder de gesloten vorm". Alle andere aangehaalde getallen zijn ongewijzigd.

**Niet gedaan.** Geen punt afgewezen.
**F6b-2.** "Opzet en notatie" zegt nu "(geen risiconeutrale kans)" zonder verwijzing naar de koperboom; twee puntkomma's (routekaart, Real options) gesplitst; geen code of labels geraakt.

## R9-1 (F6b, ronde 9+)

**Meting.** `prose_stats --check` PASS, 5.678 woorden (was 5.552). `nb_numbers`: geen nieuwe meldingen. Geen code, cel of label veranderd; alleen `jupytext --sync`.

**Feitelijke fout.** CIR-opener: gedaan ("Cox, Ingersoll en Ross maken de variantie evenredig met de rente", oorzaak en gevolg hersteld).

**Taal.** Termijnpremie: gedaan (r. 317, 443, 483, 1223, 1332; eerste keer met *term premium* tussen haakjes). "Het lemma van Itô": gedaan. Hardop-toets: CIR-, Santa-Clara- en "blijvend"-zin herschreven. Getallen per alinea: padenalinea in twee alinea's gesplitst, simulatie-intervallen zonder getallenreeks (de tabel staat erboven), oefening 1 op vier decimalen, oefening 3 in twee alinea's zonder standaardfouten tussen haakjes; "Wat dit leert" weg. "Verwachting uit het replicatieblok" (2x) wordt "wat we vooraf verwachtten". Level/slope/curvature: Nederlandse namen één keer tussen haakjes.

**Helderheid.** LSM boven de boom: gedaan (0,005 boven, binnen één SE; de stelling geldt voor vaste coëfficiënten, in-sample schatting vertekent licht opwaarts). Twee premies: 1,5 pp heet "premie in het verwachte rendement", 3 pp "termijnpremie in de lange yield", met een verbindende alinea ($\sigma_p = \sigma/\kappa = 10\%$, dan vallen ze samen). Obligatieprijzen: de alinea opent met het antwoord; "daarom" vervangen door verwijzing naar de prijsformule. Duration en PCA elk met een bijzin; vergelijking 1 met citatie van Longstaff en Schwartz.

**Opbouw.** Intuïtie: twee verwachtingen over de curve, mijn en LSM als toepassingen zonder eigen verwachting; de inlossingen bij de mijn en LSM herschreven zonder verwijzing naar een verwachting. Simulatie 40 jaar: niet naar 660 maanden gezet (dat verandert alle getallen en de `rng`-stroom van LSM en oefening 2), maar één zin zegt dat de replicatie 55 jaar heeft en dat de $t$-waarde daar toont dat de drift ook dan slecht gemeten blijft; "vijftig jaar" wordt "55 jaar". Terugverwijzing "De renteboom was deze formule" geschrapt.

**Toy en code.** Overbodige halve zin na de toy-tabel weg. Bijschrift curvefiguur herhaalt de jaartallen niet meer (die staan in de alinea's erna).

**Niet gedaan.** Geen punt afgewezen. 05_28 niet aangeraakt.
