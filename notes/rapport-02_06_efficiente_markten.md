STATUS 02_06_efficiente_markten F6b words=5457 prose=PASS open=1 cijfer=- min=-

# Rapport 02_06_efficiente_markten (workflow-herziening)

## F0

**Nulmeting.** `02_06_efficiente_markten.md  words 5421  sent_mean 20.5  sent_p90 34  sent_gt40 14  para_mean 57  dash 24  semicol 46  motief 5  Lnum 0  deel 2  u_form 0  je_form 0  taboo 0  stopw 8  calque 2  engquote 35`. `--where`: r. 51 "epistemisch", r. 699 "omvang van de toets". "deel=2" zijn "Deel 3"/"Deel 2" van een stelling (r. 419, 425). Words haalt de grens al; alle andere taalmaten falen.

Woorden per sectie: top 118, Overzicht 319, Intuïtie 407, Toy 358, Drie woorden 295, Samuelson 234, Martingaal 215, Elke SDF 326, Filterregel 150, Drie vormen/Jensen 200, Grossman-Stiglitz 131, Simulatie 437, Replicatie 1272, Wat er brak 409, Oefeningen 569.

**Vijf grootste problemen.**
1. *Engelse citaten* (engquote 35, max 5): midden in Nederlandse zinnen in Intuïtie (r. 86–91, 115–117, note r. 120–126), Theorie (r. 275, 469–473, 512–514, 521, 532–533, 542–545) en Replicatie (r. 844–846, 923–924, 1029–1030).
2. *Zinsbouw*: 14 zinnen boven 40 woorden, 46 puntkomma's, 24 gedachtestreepjes, alinea's van 57 woorden gemiddeld; ergst in Simulatie r. 710–728 en Replicatie r. 835–846, 878–886, 955–964.
3. *Structuur (STYLE §11.6–11.7)*: imports-cel in Overzicht (r. 71); Overzicht opent met geschiedenis in plaats van vraag en antwoord; geen routekaart en geen Samengevat in Theorie; toy zonder tabel hand/code (een `print`); "Waar we zijn" verwijst naar drie lectures; intuïtie eindigt niet met een voorspelling (H12).
4. *Replicatie* (1.272 woorden): twee blokken, het eerste ruim boven 250 woorden met getallen; drie deelreplicaties (Fama-Blume, deelperiodes, Alexander/Shiller) plus Jensen; getallenbrij in proza (r. 835–846, 878–886, 955–964, 1024–1035), geen tabel origineel/hier, geen oordeel "Geslaagd/Gedeeltelijk".
5. *Projectjargon en calques*: "motief 1/2/3" en "het 2%-motief" (r. 51, 704, 710, 1035), "epistemische status", "omvang van de toets"; oefening 1 is geen instap (de toy-variant staat als oefening 2).

**Eis 2 (grep in `lectures/`).** Elders aangehaald: de paginalabel (elf lectures) en `thm-efficiente-markten-elke-sdf` (05_33). Inhoudelijk leunen andere lectures op: filterregels na kosten (04_19), Samuelson-stelling (04_24), Grossman-Stiglitz (04_24, 06_36, 07_37), zeven overlevende fondsen zonder significante alpha (04_25, 08_38), niet-synchrone handel als meetartefact (08_38), joint hypothesis (02_07, 05_33, 08_39). Geen enkel `eq-`, `fig-`, `cel-` of `ex-`label wordt elders aangehaald.

**Schraplijst (schraptoets STYLE §11.11; eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Waar we zijn | zin over Williams (derde verwijzing) | 30 | niet nodig voor de vraag; §11.7 hoogstens twee |
| Overzicht | routebeschrijving in proza (wordt lijst) | 60 | herhaling van de lijst |
| Intuïtie | note Jensen 1978 | 70 | anekdote; citatie blijft in Wat er brak |
| Intuïtie | citaat Alexander 1961 en Engelse definitie Fama 1965b (parafrase) | 60 | kleur, geen mechanisme |
| Toy | slotzinnen dubbel met de tabel | 40 | herhaling |
| Samuelson | Samuelson-effect: variantiecel en alinea | 90 | nevenresultaat; blijft als oefening 2 |
| Drie vormen | prf:definition Jensen met Engels citaat, floor-trader-uitweiding | 90 | nevenzaak; één zin "na kosten" blijft |
| Elke SDF | Fama-citaten (één blokcitaat blijft), HJ-alinea ingekort | 80 | herhaling |
| Simulatie | cijferalinea's worden tabel en kortere zinnen | 60 | herhaling van de tabel |
| Replicatie | Alexander/Shiller-deelreplicatie (Working, Mandelbrot), cel en twee alinea's | 280 | nevenmechanisme (middeling), niet aangehaald, niet nodig voor de vraag |
| Replicatie | replicatieblokken naar ≤ 250 woorden, getallen naar tabel | 120 | §11.7 |
| Wat er brak | elk element ≤ 120 woorden | 60 | herhaling van eerdere getallen |
| Oefeningen | alle drie ingekort, toy-variant wordt oefening 1 | 120 | herhaling in uitwerkingen |
| Theorie | routekaart en Samengevat (toevoeging) | −130 | verplicht (§11.6) |
| **totaal** | | **≈ 940** | |

**Verwachte lengte:** 5.421 − 940 ≈ 4.480; met kortere zinnen en de ontbrekende intuïtie-voorspelling naar ongeveer 4.700 tot 5.000. Ruim onder 6.000 zonder de kern te raken: geen splitsing.

## F1

**Eindmeting.** `02_06_efficiente_markten.md  words 5270  sent_mean 14.6  sent_p90 23  sent_gt40 0  para_mean 41  dash 0  semicol 13  motief 0  Lnum 0  deel 0  u_form 0  je_form 0  taboo 0  stopw 0  calque 0  engquote 4` → PASS. `--where`: geen treffers. Draait met `HAP_OFFLINE=1`, geen stderr in het notebook.

**Geschrapt (schraptoets).**
- Williams-zin in Waar we zijn (derde verwijzing); Jensen-1978-note in Intuïtie (anekdote; de citatie staat nu in Wat er brak); citaat Alexander 1961.
- Samuelson-effect: variantiecel en alinea (nevenresultaat; blijft als oefening 2, die de paden uit de theoriecel gebruikt). De slope-cel blijft, dus de rng-stroom en alle latere simulatiegetallen zijn gelijk.
- `prf:definition` Jensen (label `thm-efficiente-markten-jensen`, nergens aangehaald) wordt twee zinnen "na kosten" in Hoe het getoetst wordt; floor-trader-uitweiding weg.
- Fama-1991-hernoeming, HJ-alinea ingekort, verwijzingen naar 03-11, 03-12, 03-13, 04-20, 04-21, 07-37 weg (hoogstens twee vooruitverwijzingen: 02-07 en 04-25 in de tabel van de drie vormen en het Jensen-blok).
- Alexander/Shiller-deelreplicatie (Working, Mandelbrot, Alexander 1964) met cel en twee alinea's: nevenmechanisme (middeling), niet aangehaald.

**Structuur.** Imports-cel naar het begin van Toy; Overzicht = vraag/antwoord, lijst, geschiedenis, plus één alinea theorie of feit; intuïtie eindigt met drie genummerde verwachtingen die de theorie expliciet inlost; Theorie met routekaart, `###` als Opzet → Kernresultaat → Wat het voorspelt → Wat het niet verbiedt → Hoe het getoetst wordt, en Samengevat. Martingaalstelling teruggebracht tot één bewering; de premievergelijking is een gevolg met afleiding in de tekst. Open bewijzen: Samuelson, elke SDF, filter; hiërarchie en martingaal in dropdown. Toy met stappen en tabel hand/code (geen `print`). Oefening 1 is nu de toy-variant (instap), 2 de afleiding Samuelson-effect, 3 break-even. Replicatie: tabel origineel/hier voor Fama-Blume en een nieuwe tabel origineel/hier voor Jensen, beide met oordeel "Geslaagd". Symbolen ontdubbeld: GARCH-$\alpha$ → $a_1$ (botste met Jensen-alpha), $\phi$ van de simulatie → $\phi_x$, steekproeflengte $T$ → $N$ (botste met leverdatum $T$).

**`nb_outputs`-diff (alle bedoeld).**
- cel 2 (toy): `print` weg; kolommen "risiconeutraal, code" / "risicoavers, met de hand" / "risicoavers, code"; rij `E_0[m_1 p_1]` weg (gelijk aan `p_0`, staat als stap 4 in de tekst). Getallen gelijk.
- oude cel 4 (Samuelson-variantietabel) geschrapt; oude cel 11 (Alexander/Shiller) geschrapt; de figuurcel schuift daardoor een plaats op.
- Fama-Blume-tabel: kolomvoorvoegsel "hier:" en "origineel:" in plaats van "FB"; getallen gelijk.
- nieuwe cel "jensen_1968": tabel origineel/hier (115/7 fondsen, alpha −0,011/−0,003, bèta 0,840/1,009, $t<-2$: 14/1).
- oefening 1: `toy_economy((1-k, 1+k))` geeft de oude getallen plus `E_0[p_1]` en `E^Q_0[p_1]`; rijen `k` en `SD(m)/E(m)` weg (beide gelijk aan $k$, staat in de tekst).
- oefening 2: `print` wordt Series; 4 194 304 en 4 208 815 gelijk.
- simulatie, deelperiodes, fondsen, break-even: identiek.

**Nieuwe getallen in de tekst, nagerekend.** $\sigma/\mu = 4{,}5/0{,}6 = 7{,}5$ (drempel voor $m<0$ bij de gemiddelde premie); $0{,}6/4{,}5 = 0{,}13$ (conditionele Sharpe-ratio); voorsprong filter $0{,}2291-0{,}1005 = 12{,}9$ pp ("bijna 13"), na kosten $0{,}1813-0{,}1005 = 8{,}1$ ("ruim acht"); SE alpha Contrafund $1{,}4/1{,}285 = 1{,}1$ pp; premie toy $-\Cov = 0{,}0435$.

**Afvinklijst §11.9, wat niet voldoet.** Overzicht heeft naast de geschiedenisalinea een korte alinea theorie of feit (bewust, zodat het motief niet in de geschiedenis verdwijnt). Het Engelse blokcitaat van Fama 1991 blijft, met Nederlandse inleiding. Overige: ok.

**Verdwenen labels.** `thm-efficiente-markten-jensen` (nergens aangehaald). Geen verhuisde labels.

**Open punten.**
1. "84 transacties per aandeel per jaar" en "hun voetnoot 3" komen uit Fama-Blume en zijn niet in een cel herleidbaar; de 14 fondsen met $t<-2$ en bèta 0,840 bij Jensen staan alleen als citatie in de cel (ongewijzigd overgenomen uit de vorige versie).
2. Bib-entries `Alexander1964` en `Working1960` worden nu door geen enkele lecture meer geciteerd (`Mandelbrot1963` nog wel, in 00_01 en 04_21); `references.bib` niet aangeraakt.

## F4

**Meting.** `words 5395  sent_mean 14.5  sent_p90 23  sent_gt40 0  para_mean 42  dash 0  semicol 10  engquote 4` → PASS. Offline uitgevoerd, geen stderr. `nb_outputs` tegenover F1: alleen de twee figuren wijzigen (aslabel $s_t$ en $\delta$), alle getallen gelijk. Tegenover `voor-…txt`: dezelfde bedoelde verschillen als in §F1.

**Feitenlijst (9 fout).** "Volledig nummer" wordt "in zijn geheel in het januarinummer". Het verschil tussen simulatie en formule "is het grootst rond 75 jaar, zes punten". Fama-Blume: alleen "het kleinste filter verdient het meest" is gedeeld; bij hen is de voorsprong vanaf 1% weg, op de index pas vanaf 10%. Het bijschrift is aangepast (FB-reeks boven 1% ver onder buy-and-hold). "Ruim zeventig jaar volgens de formule, ongeveer tachtig in de simulatie" (ook in Simulatie). Symbolen: filtergrootte $x \to \delta$ (tekst en as), toestand $x_t \to s_t$ (tekst, tabel, figuuras, codenamen `state`, `phi_s`, `sd_s`), $q$ uit de variance-ratio-uitleg weg, spotschok $\varepsilon \to \nu$ met $\sigma_S^2$ in oefening 2. De citatiegetallen (84 transacties, voetnoot 3, Jensen 115/−0,011/0,840/14) blijven, met naam en citatiesleutel. **Niet opgelost (buiten mijn bestanden):** L7 r. 27–29 wekt de indruk dat de toetsen van L6 op de maandtape draaiden; aanpassen in `02_07_event_studies`.

**Lezerspunten (15, alle behandeld).**
1. Toy stap 2: $m$ per uitkomst benoemd (goed nieuws / meezitten); stap 4 zegt nu "goed nieuws".
2. Fair game: $\E_t[R]$ is het vereiste rendement uit een evenwichtsmodel, zonder model een tautologie.
3. De gemiddelde alpha van de actieve fondsen ($-0{,}3\%$) staat nu in het oordeel, en in Wat er brak als "gemiddeld … actieve overlevers".
4. Autocorrelatie naar winst: één zin (een stijging loopt door, een klein filter stapt direct in).
5. $Q$: de dichtheid is in het toy-voorbeeld $m$ zelf, en $\tfrac12 \cdot 0{,}8 = q$.
6. Standaardfout van 2%: één bijzin (20% volatiliteit, een eeuw, 2 pp), met verwijzing naar `#00-01-rendementen`.
7. Negatieve SDF: "strikt genomen arbitrage, maar te zelden om de toets te raken".
8. $R^2$ met de hand: $0{,}3^2/(0{,}3^2+4{,}5^2)$.
9. Replicatieblok: drie genummerde criteria; de tekst verwijst naar criterium 1, 2 en 3.
10. Yale-lezing: het verschil met niet-synchrone handel is expliciet (de werkelijke prijs, niet alleen de gemeten slotkoers). Geen naam toegevoegd, omdat er geen verifieerbare citatie is.
11. "Dit is" wordt "De propositie is".
12. "Na 0,1% per transactie nog ruim acht" staat in de replicatietekst.
13. De bias heet nu bij naam, met {cite}`Stambaugh1999` (bestaande sleutel).
14. "Model van risico" krijgt een exemplaar: de Jensen-regressie is het CAPM.
15. De "daardoor" in de routekaart heeft nu een reden. De Jensen-1978-zin in Waar het breekt is geschrapt.

**Betaald met schrappen.** Citaat 0,209/0,125 in oefening 3, de Lucas-zin, de slotzin van oefening 2, en het toy-voorbeeld en de Jensen-alinea ingekort.

**Navertel-toets, secties die afweken.** *Wat het voorspelt*: $Q$ was alleen via $q = 0{,}4$ te volgen; de dichtheid is nu in toy-termen uitgerekend (punt 5). *Replicatie*: onduidelijk of het filterfeit een meetfout is. Risico of vergissing zegt nu: op de index een meetfout, en of er in de jaren zestig iets verhandelbaars was, blijft open. Daarnaast geeft het blok genummerde criteria.

## F5-1

**Meting.** `words 5444  sent_mean 14.4  sent_gt40 0  dash 0  semicol 13  engquote 4` → PASS. Offline uitgevoerd, geen stderr. `nb_outputs` tegenover F4: Nederlandse rijlabels in de toy-, Samuelson- en deelperiodetabel; kolom "origineel: na volle commissies (niet vergelijkbaar)"; nieuwe cel `predicted_lead` (ρ₁ 0,1752, σ 0,0068, voorspeld 0,1392, gemeten 0,1286); oefening 3 met extra kolom c* alleen lang (0,0016, 0,0027, −0,0005); in de filterfiguur is buy-and-hold nu over het hele venster berekend. Alle eerder aangehaalde getallen zijn gelijk. `[](#ex-efficiente-markten-2)` (r. 383) wijst naar een bestaand label (r. 1166).

**Feitelijke fout.** m < 0: de 7,5 SD komt "vrijwel nooit" voor; de negatieve maanden vallen in toestanden met een hoge premie (bij μ_t = 1,5% is de drempel 3 SD).

**Top drie.**
1. *Helderheid*: x_t → s_t. Filteroordeel voor kosten tegen voor kosten (12,9 tegen 1,7, na 0,1% ruim acht). Eén regel CAPM bij Jensen, met de koppeling aan de sterke vorm. 0,84 benoemd als 80%-kwantiel. Autocorrelaties toetsen "een gevolg van de fair game, deel (ii)".
2. *Replicatie*: de 0,1%-resultaten van Fama en Blume per filter heb ik niet (niet in project of bib), dus de kolom is gelabeld als "niet vergelijkbaar". De tekst zegt dat ook. Criteria 2 en 3 hebben nu een oordeel "**Geslaagd**". Criterium 1 heeft een grootte, 252(ρ₁σ√(2/π) − μ), voorspeld 13,9 tegen gemeten 12,9. Het bètaverschil (1,01 tegen 0,84, "waarschijnlijk meer kas") is benoemd.
3. *Opbouw*: autocorrelatie → filterwinst en niet-synchrone handel staan nu in "Hoe het getoetst wordt", met de formule ρ₁σ√(2/π). De routekaart zegt "vijf dingen".

**Overige aanmerkingen.**
- Taal: "definieert het tijdvak" wordt "Met dat artikel begint het tijdvak". Alle "men" herschreven. Januari staat er één keer. De stelling heet "Martingaal na weging met de SDF". De naam "het constante model" wordt gebruikt vanaf de simulatie (daar ook gedefinieerd).
- Toy: stap 4 is één zin "Vooruitblik". De slotalinea zegt dat de risicocorrectie in beide gevallen 4 is.
- Code: handkolom als expliciet woordenboek; commentaar bij `idxmax`; zin over de wisselende buy-and-hold.
- Oefeningen: 2.1 eindigt met de variantiestap. 3.2 rekent c* voor de lange variant (0,16% en 0,27%).

**Afgewezen.** "De simulatie heeft geen tegenhanger op echte data": STYLE §11.7 (één simulatie; de replicatie volgt PLAN) en §11.11 (woordgrens, 58 woorden ruimte).

**Betaald met schrappen.** De "Waarom wint"-alinea is verplaatst, de Fisher-alinea en het replicatieblok zijn ingekort. Geschrapt: de zin "De drie vormen deelden …", een intuïtiezin, "Kosten maken het verschil …" en de simulatiezin in Wat er brak.
- Build-waarschuwing: de inline link `[](#ex-efficiente-markten-2)` (r. 384) is vervangen door gewone tekst "(oefening 2)"; prose_stats PASS (5445 woorden), gesynct.
- Symbool: de dagvolatiliteit in de filterformule (Hoe het getoetst wordt en replicatieblok) heet nu $\sigma_d$, bij de eerste keer uitgelegd; prose_stats PASS (5450 woorden), gesynct, geen code geraakt.

## F6-1

**Meting.** `words 5457  semicol 11  engquote 4` → PASS. Offline uitgevoerd, geen stderr. `nb_outputs` tegenover F5: in de Jensen-tabellen heten de kolommen nu "alfa" en "bèta"; alle getallen gelijk.

**Feitelijke fouten.**
1. Filter: "op de index pas vanaf 10%" wordt "op de index wordt ze vanaf 3% grillig".
2. Tijdvak: "Met dat artikel begint het tijdvak" wordt "Dat artikel sluit het tijdvak af dat in 1965 begon".

**Top drie.**
1. $R^f$ bruto wordt in het toy-voorbeeld als afwijking van [](#00-00-setup) gemeld. Logrendement $r$ wordt $\ell_{t+1} = \log R_{t+1}$ (definitie, propositie, bewijs). De filterformule krijgt een herkomst (verwachting van teken maal rendement bij twee normale variabelen) en een getal: 0,175 · 0,68% · 0,80 ≈ 0,095% per dag, ruim 24% per jaar.
2. Beide feitelijke fouten zijn opgelost. Eén brugzin: we repliceren het filter en niet de regressie, omdat het filter de joint hypothesis bijna omzeilt.
3. De deelperiodegetallen staan niet meer in de lopende tekst; die verwijst naar de tabel.

**Naadpunten die L6 raken.** (1) $R^f$ bruto: gemeld. (2) $r$ wordt $\ell$. (4) $m$ blijft de SDF, de markt blijft $M$ (setup-conventie). (5) "alpha" wordt "alfa" in tekst en tabellen; `\alpha` in formules blijft. (9) $\lambda$ bij Grossman-Stiglitz wordt $\omega$. Niet aangepast: (6) CAPM, (7) $Q$ tegen $\mathbb{Q}$ en (10) 4,5% per maand. Die raken vooral L8 en L9 of zijn in L6 een bewuste kalibratie, en de woordgrens laat geen toelichting toe.

**Overig uit de eindbeoordeling.** Grammaticafout "verdwijnt bij … gebruikt" hersteld. De puntkomma bij 0,84 is weg. Voor de filterfiguur staat nu waar de lezer op moet letten. Bij de download staat een commentaar dat alleen SPY wordt gebruikt (de tickerlijst blijft, anders mist de offline cache). Bij Jensen staat nu de soort standaardfout (heteroskedasticiteitsrobuust). Geschrapt om te betalen: LeRoy-zin, Jensen-toevalzin, Alexander-correctiezin, staart van de Grossman-Stiglitz-zin.
- Naadcorrectie: alle 17 keer "alfa" terug naar "alpha" (boekconventie), ook in de Jensen-tabellabels; prose_stats PASS (5457), gesynct, offline uitgevoerd, getallen gelijk.
- Filterformule: "ruim 24% per jaar" wordt "bijna 24% per jaar" (0,175 · 0,68% · 0,80 · 252 ≈ 23,9%); prose_stats PASS, gesynct.
