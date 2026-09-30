STATUS 04_21_volatiliteit F4T words=5639 prose=PASS open=1 cijfer=- min=-

# Rapport 04_21_volatiliteit (L21)

**Kern.** Hoe is volatiliteit te voorspellen, en is een goed gemeten variantie genoeg om de
risico-rendementsrelatie te zien? Volatiliteit is met GARCH en HAR goed voorspelbaar
(tientallen procenten $R^2$ buiten de steekproef), maar haar prijs in het verwachte rendement
is zelfs met de ware variantie pas na zeventig jaar vaker wel dan niet significant, en op de
French-data slaagt de MIDAS-replicatie niet.

## F0

`04_21_volatiliteit.md 5802 words, sent_mean 20.6, sent_p90 35, sent_gt40 14, para_mean 53, dash 20, semicol 51, motief 2, je_form 1, calque 7, engquote 6, colon_mid 9.7, para_one 30, telegram 2, tmpl 8, connect 16` — FAIL op 14 drempels (words PASS).

Vijf grootste problemen:
1. Taal overal: 51 puntkomma's, 14 zinnen > 40 woorden, 30% eenzinsalinea's, 20 gedachtestreepjes,
   8× "*Waarom zou dit waar zijn?*" (Theorie r205–506), 6 Engelse citaten (Overzicht r50, GJR r368,
   FSS r518), "motief 1" en "het 2%-motief" (Theorie r552, Simulatie r840), "je" in de open vraag (r34).
2. Overzicht (r41–77) begint met Santa-Clara in plaats van vraag en antwoord, geen lijst, regeltaal
   ("definieert het tijdvak", "Epistemisch"), imports-cel aan het eind van Overzicht (r79).
3. Theorie zonder routekaart en zonder Samengevat; vier bewijzen > 6 regels open (prop-arma r244,
   thm-voorspelling r289, thm-rv r400, thm-vix r488); EGARCH als nevenresultaat (r349–356).
4. Codecellen zonder tekst ertussen: Simulatie r626–681, Replicatie r876–937, r989–1051,
   r1107–1230; cellen > 25 regels (r720–767, r1107–1172); toy eindigt met prints, geen tabel hand/code.
5. Naad: $\mu_m - r = \gamma\sigma_m^2$ toegeschreven aan "het ICAPM" (Overzicht r61–64, Theorie
   r506–516), terwijl 03_10 (r402) het afleidt uit de Merton-portefeuille bij constante
   beleggingskansen. Getallen zonder cel of bron: S&P −20,47% en Dow −22,6% (r118), φ tussen 0,97
   en 0,995 (r302).

Schraplijst (eis 2 met grep: buiten dit college worden alleen `04-21-volatiliteit` en
`thm-volatiliteit-vix` aangehaald):

| passage | kopje | woorden | eis niet gehaald |
|---|---|---|---|
| Nobelcitaat en "definieert het tijdvak" (r49–52) | Overzicht | −40 | 1, 2, 3 |
| Realized/VIX-alinea tot lijstpunt, Santa-Clara-opening | Overzicht | −90 | 1 (dubbel met lijst) |
| 1987: Leland/Rubinstein-details, Brady-commissie, smirk | Intuïtie | −60 | 1 |
| EGARCH-vergelijking en Nelson (r349–356) | Theorie | −50 | 1, 2, 3 |
| QML-scorealinea samenvoegen (r336–339) | Theorie | −30 | 1 |
| ABDL-geschiedenis, Andersen-Bollerslev 1998, microstructuurwaarschuwing | Theorie | −70 | 1 |
| Whaley/VXO-geschiedenis (r465–469) | Theorie | −35 | 1; thm-vix blijft (eis 2) |
| Exp-Almon versus Beta-detail MIDAS, JFE-zin | Theorie | −40 | 1 |
| Artikeltitels in drie replicatieblokken | Replicatie | −60 | 1 |
| Oefening VIX-formule narekenen (oude ex-3) | Oefeningen | −230 | 1, 2 |
| Risico of vergissing tot ≤ 120 woorden | Wat er brak | −90 | 1 |

Verwachte lengte na toevoegingen (routekaart, Samengevat, celzinnen, instap-oefening, tabel
origineel/hier) ≈ 5.500. Geen splitsing.

## F1

Eindmeting: `words 5602, sent_mean 16.7, sent_p90 26, sent_gt40 0, para_mean 43, dash 0, semicol 3, calque 0, engquote 0, colon_mid 0.2, para_one 12, tmpl 2, connect 28` — PASS. Doel 5.500 net overschreden (+102), grens 6.000 gehaald.

Geschrapt of verplaatst (naast de schraplijst):
- Engelse citaten (Nobel, GJR, twee van FSS) geparafraseerd of weg; GSV-herberekening 7,809 en 5,926 weg (te veel getallen, niet nodig).
- Microstructuur-`{warning}` wordt één zin; cites `Nelson1991` en `AndersenBollerslev1998` vallen daardoor weg.
- Risico of vergissing: FSS-samenhang, praktijkmotief en RiskMetrics weg (lengte).
- Bewijzen van prop-arma, thm-voorspelling, thm-rv en thm-vix in dropdown, met één zin bewijsidee.
- Simulatie: twee delen blijven, geframed als één vraag (wat is meetbaar, variantie of prijs); deel 1 schrappen zou de rng-volgorde en alle simulatiegetallen veranderen.

nb_outputs-diff (35+/27−): (1) toy-cel geeft nu een tabel "met de hand / code" in plaats van prints,
zelfde getallen (halfwaardetijd hand 6,58, code 6,5788); (2) celnummers verschuiven door twee
splitsingen (simulatie γ: parameters | lus; MIDAS: data + `sample` | gewichten + QML); (3) oude
VIX-oefening weg, nieuwe instap-oefening met tabel 2,0096 / 1,1096 / 1,5596. Geen aangehaald getal
veranderd. Overige codewijzigingen: `horizons` → `sample_lengths`, legenda "|overrendement|",
index "GARCH (toy-voorbeeld)".

Afvinklijst §11.9, wat niet (helemaal) voldoet:
- Woorden 5.602, boven het doel van 5.500.
- HAR-replicatie heeft geen tabel origineel/hier: de originelen geven geen vergelijkbaar getal (intradag, dagelijks); het oordeel staat onder de celtabel.
- Docstrings blijven Engels (STYLE §3 en "Wat niet meetelt" 3; 03_10 doet hetzelfde), ondanks "Nederlandse docstrings" in de opdracht.

Labels: geen label verdwenen behalve inhoudelijk hergebruik van `ex-volatiliteit-1..4`
(1 = nieuwe instap op het toy, 2 = oude 1 momenten, 3 = oude 2 Student-t, 4 = oude 4 FSS; oude 3 VIX
geschrapt). Geen `ex-`-label wordt buiten dit college aangehaald. `thm-volatiliteit-vix` blijft (05_29).

Naad met 03_10: $\mu_m - r = \gamma\sigma_m^2$ staat nu als Merton-portefeuille bij constante
beleggingskansen met een representatieve belegger (zoals 03_10 r402, inclusief 8% bij γ = 2 en
σ = 20%); het ICAPM voegt een hedgingterm toe die de toetsen weglaten. Overzicht noemt het ICAPM niet
meer als bron van de relatie.

Open punten voor de feitencontroleur:
1. Intuïtie: "19 oktober 1987 verloor de Amerikaanse markt meer dan een vijfde" zonder cel of cite (French-reeks −17,4%; S&P −20,5%).
2. Overzicht/Theorie: GSV-getallen (2,606, t 6,710, −0,349 over 1928–1984, 31% op de eerste maand) uit het werkdocument; 31% klopt met de cel (0,307).
3. Intuïtie: autocorrelatie 0,30 van het absolute dagrendement, overgenomen uit 00-01 (niet nagekeken in 00-01).
4. Theorie VIX: "de eerste VIX middelde Black-Scholes-volatiliteiten" op `Whaley2000`.
5. Figuurbijschrift MIDAS: het profiel op French-data 1928–2000 wijkt af (niet met een getal gecontroleerd).

## F4

Feitenrijen: 1 en 3–10 juist, geen actie. Rij 2 (GSV −0,349, onzeker) behouden met citatie; de zin noemt nu de schatter (vorige-maandvariantie), tabelnummer niet toegevoegd omdat het niet te verifiëren is. open=1.

Lezerspunten:
1. Gedaan (Simulatie, Replicatie): alle vijf "In de figuur gaat het ..." herschreven, elk in een andere vorm.
2. Gedaan (Replicatie): "Geslaagd, want" / "Niet geslaagd." gevarieerd in alle drie de blokken.
3. Gedaan (Simulatie, γ): 46%/77% worden "minder dan de helft" / "ruim driekwart"; de t = 6,7-vergelijking is een eigen zin.
4. Gedaan (Simulatie, γ): MIDAS-schatters in een eigen zin.
5. Gedaan (HAR-RV tegen GARCH): niveau en logaritme in twee zinnen.
6. Gedaan (GARCH en GJR): crashcijfers verdeeld over twee alinea's zonder de alinea-volgorde te wijzigen.
7. Gedaan (Simulatie, GARCH): "tot op één à twee honderdste" geschrapt.
8. Gedaan (Wat er brak): "Scheiden vraagt ..." wordt een hele zin.
9. Gedaan (Simulatie, γ): "In deze simulatie geldt ... per constructie."
10. Gedaan (Theorie, Opzet): "is dat de GARCH-vergelijking".
11. Gedaan (GSV): kaal "daar" weg, "draagt" (calque) wordt "bepaalt".
12. Gedaan (Theorie, VIX): *smirk* cursief met uitleg (STYLE §3 houdt de term Engels).
13. Gedaan (Theorie, risico en rendement): "de schatter met de variantie van de vorige maand".
14. Gedaan (Intuïtie): "en dan nog pas na tientallen jaren", zonder nieuw getal.
15. Afgewezen: een VIX-niveau als voorbeeld komt niet uit een cel of geciteerde bron (feitenregel).

Extra: kapotte zin in het toy-voorbeeld ("Eén dag van −3% ... verdrievoudigt") hersteld; betalen voor toevoegingen met twee overbodige zinnen na bewijzen. Woorden 5.602 → 5.639.
Navertel-toets: geen sectie week af (lezer en eigen lezing).

## R9-1 (F6b, ronde 9+)

Uitgangspunt: eind 8,8. Een vorige agent deed het meeste; nagelopen tegen de ijkkopie en alles klopt.
Feitelijke fouten:
1. Gedaan (Theorie VIX, Samengevat): "het kwadraat van de VIX" is de risiconeutrale verwachte variantie; VIX als volatiliteit op jaarbasis in procenten.
2. Gedaan (Overzicht): *gerealiseerde variantie* als som van kwadraten, realized volatility als wortel.
3. Gedaan (Oefening 4): het negatieve teken komt uit de herberekening door GSV met de FSS-schatter; FSS zelf vonden een positief verband.
4. Gedaan (Wat er brak): Merton toonde dat de variantie scherper te meten is dan het gemiddelde, niet dat ze voorspelbaar is.
Drie verbeteringen / Voor een 9:
- Gedaan (Taal, HAR-RV): ontbrekende punt; figuurtitel "haar" wordt "twee voorspellingen" (code-cel, alleen label; notebook offline opnieuw uitgevoerd, uitvoer gelijk).
- Gedaan (Replicatie): oordelen "Geslaagd" (GARCH/GJR), "Gedeeltelijk geslaagd" (HAR-RV, met "vorige maand" boven HAR-RV in niveau en log), "Niet geslaagd" (MIDAS, getallen uit de proza naar de tabel, alleen rangorde en teken).
- Gedaan (Theorie RV, HAR): één naam "gerealiseerde variantie" voor de variantiemaat.
- Gedaan (Theorie VIX): variance risk premium in één zin uitgelegd (VIX² boven de latere gerealiseerde variantie, verzekeringspremie).
- Gedaan (Overzicht, vuistregel, Simulatie): zestig tegen zeventig jaar verbonden (vuistregel met normale ruis; simulatie trager omdat de gewogen schatter de extreme maanden weinig gewicht geeft).
- Gedaan (Toy): "als eerste invoert" in plaats van "afleidt".
- Gedaan (Simulatie): zin vóór de cel over de ware maandvariantie (verwachte $s$ maal de som van 22 dagvarianties, meetkundige daling).
Hardop-toets: alle drie de zinnen (oefening 3 log-likelihood, "schiet twee keer tekort", "$\gamma$ pas na meer dan zeventig jaar") herschreven volgens het voorstel.
Extra: rafelige regelafbreking uit eerdere rondes in 20 alinea's hersteld (woorden ongewijzigd).
Controles: prose_stats PASS; nb_numbers 10 meldingen, alle al vóór F6b aanwezig (toy, oefeningen, GSV −0,349, 0,97/0,149); rewrap en jupytext --sync gedraaid.
Woorden 5.639 → 5.796. open=0.
