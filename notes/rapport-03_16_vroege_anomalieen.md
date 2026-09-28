STATUS 03_16_vroege_anomalieen F6b words=5276 prose=PASS open=0 cijfer=- min=-

# Rapport 03_16_vroege_anomalieen (workflow-herziening)

## F0

**Nulmeting.** `03_16_vroege_anomalieen.md  words 5593  sent_mean 20.7  sent_p90 35  sent_gt40 15  para_mean 60  dash 0  semicol 40  motief 5  Lnum 0  deel 0  u_form 0  je_form 2  taboo 0  stopw 9  calque 3  engquote 16`. FAIL op words, sent_mean, sent_p90, sent_gt40, para_mean, semicol, motief, je_form, stopw, calque, engquote. `--where`: r. 50 "epistemische status", r. 171 "Twee dingen", r. 1126 "Dat is de reden dat". Met de hand: "motief 1/3" (r. 53, 301, 478, 634), overal "alfa" in plaats van "alpha", `$R^f - 1 = 1\%$` en kolom `$R - 1$` in het toy (setup: $R^f$ netto, $r$ netto simpel), symbool $g$ tweemaal (conditionele verwachting $g(z)$ en groeivoet $g$), $\hat\beta_{i,t}$ met één index. Nulmeting uitvoer: `$TEMP/voor-03_16_vroege_anomalieen.txt` (170 regels).

**Vijf grootste problemen.**
1. *Taal*, overal: zinnen van gemiddeld 20,7 woorden, 15 boven 40, alinea's van 60 woorden, 40 puntkomma's, getallenalinea's met zes tot tien getallen (Simulatie, Replicatie, Januari).
2. *Structuur*: imports-cel in Overzicht; Overzicht zonder vraag-antwoord en lijst; geen voorspelling aan het eind van Intuïtie; geen routekaart en geen Samengevat in Theorie; toy zonder opzet-tabel met recept, stappen en tabel hand/code; vier proposities/stellingen met open bewijs (max drie), bewijzen van Berk (15 regels) en snooping (12 regels) open.
3. *Replicatie*: blok ≈ 450 woorden met reekscodes en datums; kernbevindingen als getallenbrij in één alinea; geen tabel origineel/hier en geen oordeel "Geslaagd"; figuurbijschrift noemt getallen (−0,50%, t = −2,7; 0,92%, t = 3,1) die alleen in de figuur staan, niet in een celuitvoer.
4. *Theorie te breed*: BARRA-subsectie (283 woorden, eigen vergelijking) is geschiedenis naast de vraag; proposities met twee beweringen (Berk (1) en (2)); Fama-MacBeth-helling heet $\gamma_1$ in de propositie en $\gamma_2$ in de regressie ervoor.
5. *Code en oefeningen*: `argsort(argsort())` en `group[np.argsort(...)] = ...` (§11.8), replicatiecel van 49 regels; oefening 1 is geen instap maar een afleiding, geen uitwerking eindigt met "Wat dit leert:", "Controleer je antwoord"; `[](#ex-vroege-anomalieen-1)` als linkdoel.

**Eis 2 (grep in `lectures/`).** Elders aangehaald: paginalabel `03-16-vroege-anomalieen` (03_15, 03_17, 04_18, 04_19, 04_25, 06_34, 08_39) en `prop-vroege-anomalieen-fm` (04_18 r. 251: "Fama-MacBeth-helling van een kenmerk is het rendement van een long-short-portefeuille met blootstelling één aan dat kenmerk en nul aan de andere regressoren"). Die inhoud moet in de propositie blijven. 04_18 r. 83 "de drie bevindingen" (E/P, size, B/M) en 03_15 "goedkoop ten opzichte van winst of boekwaarde" blijven gedekt. Geen `thm-`, `eq-`, `fig-`, `cel-` of `ex-`-label elders aangehaald.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Waar we zijn | CRSP-verwijzing en tweede vraag | 35 | hoogstens twee verwijzingen, één vraag |
| Overzicht | "We bouwen de methode van onderaf op"-alinea naar lijst; "motief 3"-zinnen | 80 | dubbel met Theorie; jargon |
| Intuïtie | Nicholson-details (tijdschrift, lengte), Berk/Lo-MacKinlay-zin | 60 | kleur; komt terug als voorspelling |
| Toy | "Twee dingen vallen op"-alinea ingekort | 50 | dubbel met stap 4 |
| Theorie, sortering | "partitieschatter", "Het vak koos sorteringen"-alinea | 90 | nevenresultaat |
| Theorie, LS-alpha | propositie + bewijs naar lopende tekst met één regel afleiding | 70 | vierde propositie; afleiding van twee regels |
| Theorie, BARRA | subsectie tot één alinea in Fama-MacBeth, zonder vergelijking | 190 | geschiedenis; alleen het eerste/tweede-moment-argument draagt de standaardfout van 2% |
| Theorie, Berk | bewijs naar dropdown en ingekort, stelling tot één bewering | 100 | bewijs > 6 regels, H3 |
| Theorie, snooping | bewijs naar dropdown, alinea over Lo-MacKinlay ingekort | 110 | bewijs > 6 regels |
| Simulatie | getallenalinea's ingekort, kalibratie naar tabel | 200 | getallen in proza |
| Replicatie | blok naar ≤ 250 woorden, reekscodes naar de cel | 220 | te lang |
| Replicatie | kernalinea naar tabel origineel/hier plus oordeel; bijschrift zonder figuurgetallen | 250 | getallen in proza; niet herleidbaar |
| Januari, FM | getallen ingekort | 80 | getallen in proza |
| Wat er brak | Bhandari-zin, "Risico of vergissing" ≤ 120 woorden | 120 | te lang, Bhandari staat in Overzicht |
| Oefeningen | uitwerkingen ex-2 en ex-3 ingekort | 120 | uitweidingen |
| **totaal** | | **≈ 1.775** | |

**Verwachte lengte.** 5.593 − 1.775 ≈ 3.820; erbij komen vraag-antwoord en lijst, voorspelling in Intuïtie, toy-opzet met recept en stappen, routekaart, bewijsideeën, Samengevat, zinnen rond gesplitste cellen, tabel origineel/hier met oordeel, instapoefening en vier keer "Wat dit leert:" (≈ 1.000). Verwacht 4.800 tot 5.100, onder 5.500 zonder de kern te raken. Geen splitsing.

## F1

**Eindmeting.** `03_16_vroege_anomalieen.md  words 5287  sent_mean 15.8  sent_p90 25  sent_gt40 0  para_mean 42  dash 0  semicol 14  motief 0  Lnum 0  deel 0  u_form 0  je_form 0  taboo 0  stopw 0  calque 0  engquote 0` → PASS. Sync en `HAP_OFFLINE=1`-uitvoering foutloos, geen warnings in de uitvoer.

**Geschrapt (reden).** Waar we zijn: CRSP-verwijzing en tweede vraag (max. twee verwijzingen, één vraag). Overzicht: methode-alinea (nu lijst), Rosenberg-risicomodelzin (staat in Theorie), "motief 3". Intuïtie: tijdschrift/lengte Nicholson (kleur). Theorie: "partitieschatter" en "Het vak koos sorteringen" (nevenresultaat); propositie standaardfout → lopende tekst met één regel afleiding, `eq-...-se` blijft (vierde propositie); BARRA-subsectie met `eq-vroege-anomalieen-barra` → één alinea in Fama-MacBeth die het eerste/tweede-moment-argument draagt; Berk tot één bewering (oude deel 1 is het geval $\hat k$ constant), bewijzen Berk, FM en snooping in dropdown met bewijsidee in de hoofdtekst. Replicatie: blok 450 → 202 woorden, reekscodes en datums naar de cel; getallenalinea → tabel origineel/hier + oordeel; figuurgetallen uit het bijschrift (niet in een celuitvoer). Wat er brak: Bhandari-zin (staat in Overzicht), elk element ≤ 120 woorden. Oefeningen: uitweidingen in uitwerkingen.

**Toegevoegd.** Vraag-antwoord + lijst in Overzicht; drie verwachtingen aan het eind van Intuïtie, ingelost in Berk en snooping; toy met opzet, recept, stap 1–4 en tabel hand/code; routekaart en Samengevat; lees-zin bij elke genummerde vergelijking; kalibratietabel simulatie (a); tabel origineel/hier met **Geslaagd**; instapoefening (bredere sortering, ex-1); "Wat dit leert:" in elke uitwerking. Oefeningen hernummerd: oud 1 → 2, 2 → 3, 3 → 4; verwijzingen als platte tekst ("de tweede oefening").

**Notatie en termen.** "alfa" → "alpha" overal, ook in kolomnamen en figuurlabels; toy $r$ netto, $R^f = 1\%$ netto; $g(z)$ → $\mu(z)$ (botste met groeivoet $g$); $\hat\beta_{i,t}$ → $\hat\beta_{i,m}$; FM-helling in de propositie $\hat\gamma_{z,t+1}$ (was $\gamma_1$, naast $\gamma_2$ in de regressie). Elke "standaardfout van 2%" (vier keer) linkt naar `00-01-rendementen`. Geen logs, dus geen aankondiging nodig.

**Code.** `argsort(argsort())` en `group[np.argsort()] =` → `stats.rankdata`; `np.bincount`-gemiddelden → `groupby`; replicatiecel (49 regels) gesplitst in data + schatting; `january_split` met benoemd tussenresultaat. Cellen met `rng` staan in dezelfde volgorde, dus alle simulatiegetallen zijn gelijk.

**nb_outputs-diff** (`$TEMP/voor-…` tegen `$TEMP/na-…`). Vanaf cel 4 geen enkel getal veranderd (controle op alle decimalen). Verschillen: cel 2 toont nu een tabel hand/code (marktrendement, marktbèta, marktgewogen alpha, alpha H/L, bèta, excess en alpha H − L) in plaats van `sorted_toy` en twee prints; cel 3 kolommen "gewicht uit OLS"/"formule" plus een print van de sommen; kolomnamen "alfa" → "alpha", "corr met log ME" → "correlatie met log ME", "in-sample/out-of-sample" → "in de steekproef/erna"; cel 10 gesplitst (celnummers +1); nieuwe cel 15 (instap: H = C,D,E). Figuren: alleen labels.

**Labels.** Weg: `eq-vroege-anomalieen-barra`, `prop-vroege-anomalieen-se`; geen van beide elders aangehaald (grep). `prop-vroege-anomalieen-fm` behoudt de inhoud die 04_18 aanhaalt.

**Afvinklijst §11.9, niet voldaan.** Replicatie-schattingscel 27 regels (> 25). Modelparameters simulatie blijven losse globals (`lam_m`, `sd_m`, …), niet omgezet naar dict: raakt elke simulatiecel. Overige: ok.

**Open punten voor F2.**
1. Inhoudelijke correctie: "Waar het breekt" zei dat ook kleine aandelen een long-short-bèta rond nul of negatief hadden; de size-bèta in Banz' periode is +0,60/+0,56. Nu alleen voor goedkope aandelen (E/P, B/M).
2. "De markt verklaart het grootste deel van de variantie" (niet herleidbaar) vervangen door de B/M-alpha over de volle eeuw (0,14%, $t$ = 0,83).
3. Niet in primaire bron nagelezen (ongewijzigd): Nicholsons tabellen, Lo-MacKinlay-formules, tabelwaarden Basu/Banz/RRL; AFI 2018 $t$ = 1,82 en Barra 1975 uit citatie.
4. H11: toy-getallen komen terug in Theorie (FM-gewichten, stap 4), niet in de simulatiekalibratie.
5. Simulatie heeft twee werelden onder één vraag (a/b, één figuur); een lezer kan dat als twee simulaties zien. Woordruimte voor F4: ≈ 210.

## F4

**Meting.** words 5275, sent_mean 16.1, sent_p90 25, sent_gt40 1, para_mean 44, semicol 14 → PASS. Sync en `HAP_OFFLINE=1`-uitvoering foutloos. nb_outputs tegen F1: alleen cel 18 (simulatie van oefening 4) weg; cellen 1–17 identiek, dus alle aangehaalde getallen gelijk aan de nulmeting.

**Feitenrij (open=1).** "K = 513,4" (nagerekend 513,1): opgelost doordat oefening 4 is geschrapt (lezerspunt 14: herhaalt de formule $1 - \Phi(c)^K$ uit de hoofdtekst; schraptoets). Geen verwijzing naar die oefening elders.

**Lezerspunten.**
1. Gedaan: simulatie (b) zegt nu wat `rng.standard_normal((n_cand, n_sn))`, `long_short_weights`, `t_in[0]` en `np.argmax(t_in)` zijn.
2. Gedaan (H11): simulatie (a) koppelt de alpha van klein min groot aan stap 4 van het toy (H − L, 5,325%, negatieve bèta).
3. Gedaan: Sharpe-ratio nu afgeleid uit de simulatiekalibratie, 0,5/4,5 = 0,11, correctieterm 1,01 (was "ongeveer 0,13", 1,02, zonder bron).
4. Gedaan: één bijzin waarom een covariantie beter gemeten is dan een gemiddelde.
5. Gedaan: "zit in dezelfde positie" vervangen door "sorteert net zo goed deels op die steekproeffout".
6. Gedaan: `prop-vroege-anomalieen-fm` is nu één bewering (elke helling: kost niets, blootstelling één aan de eigen regressor, nul aan de andere) met de formule voor één kenmerk; label en de inhoud die 04_18 aanhaalt blijven.
7. Gedaan (H12): het replicatie-oordeel zegt dat het de eerste verwachting inlost.
8. Gedaan: "het ruwe rendementsverschil van 3,45%".
9. Gedaan: simulatie (b) herhaalt de marktpremie en volatiliteit (0,5% en 4,5% per maand).
10. Gedaan: $\rho^2 = 0{,}01$, dus $\rho = 0{,}1$.
11. Afgewezen: het derde lijstpunt van het Overzicht bundelt de twee relativerende resultaten bewust; vijf punten is het maximum.
12. Gedaan: de januari-sectie opent met Keims eigen bevinding; "vier vijfde" komt pas na de tabel.
13. Gedaan: een brugzin zegt dat $\hat\gamma_{z}$ in [](#eq-vroege-anomalieen-fm) $\gamma_{2}$ is.
14. Gedaan: oefening 4 geschrapt (≈ 135 woorden); hiermee zijn de toevoegingen van 1 tot en met 13 betaald.
15. Gedaan: Santa-Clara met een cross-ref naar [](#00-00-setup).

**Navertel-toets.** Twee kleine afwijkingen. Replicatie: de lezer schrijft dat het januari-effect na 1980 "praktisch verdwenen" is, terwijl januari nog 5,6% oplevert en alleen de jaarpremie wegvalt; de tekst zegt dat al, niet veranderd. Kernresultaat: de lezer leest Berk als een puur risicoverhaal; de alinea "werkt voor elke $lpha_i$, ook bij te zware verdiscontering" staat er al, niet veranderd.

## F6-1

**Meting.** 5.276 woorden, zinnen gemiddeld 16,0, 0 zinnen boven 40, 7 puntkomma's (alleen lijsten, Bron-regel, tabellen) → PASS. Sync en `HAP_OFFLINE=1`-uitvoering foutloos, geen warnings. Labels: alleen `ex-vroege-anomalieen-4` nieuw; `prop-vroege-anomalieen-fm` blijft.

**nb_outputs tegen F4.** Toy, theorie, simulatie (a), replicatie, januari en oefeningen 1–3: identiek. De Fama-MacBeth-cel van simulatie (a) en de formulecontrole van (b) zijn uit de simulatie weg, dus de cel van (b) trekt andere toevalsgetallen. Nieuw: beste van 100 haalt $t > 1{,}96$ in 93,2% (was 92,5%) en $t > 3$ in 13,8% (was 12%); de tekst is bijgewerkt, "ruim negen op de tien" klopt nog. De Fama-MacBeth-cel staat nu in oefening 2 (4) met nieuwe getallen ($-0{,}027$, $t = -1{,}57$; met $\delta$ $t = 0{,}54$), en de uitwerking is daarop herschreven. De Banz-cel staat nu in oefening 4, met dezelfde getallen.

**Feitelijke fout.** Gedaan: "hun noemer" → "hun teller (winst, boekwaarde) schaalt mee met het kasstroomniveau".

**Drie verbeteringen.**
1. Opbouw. Gedaan: Fama-MacBeth-variant van (a) → oefening 2 deel 4; formulecontrole van (b) geschrapt (schraptoets: de hand-uitkomst $24{,}8\,\rho$ staat in Theorie); Fama-MacBeth van Banz → oefening 4 met "Wat dit leert"; Barra-alinea van zes naar drie zinnen.
2. Replicatie. Gedaan: de verwachte afwijking noemt nu ook kleinere value-weighted alpha's na publicatie en januari als grootste deel van de size-premie; het oordeel verwijst naar beide. Januari: getallen vervangen door een verwijzing naar de kolom "bijdrage januari" en één conclusie. De Fama-MacBeth-cel is met haar getallen naar oefening 4 verhuisd.
3. Taal en code. Gedaan: Barra-stapelzin gesplitst; codenamen uit de tekst van (b), naar commentaar in de cel; zeven puntkomma's in lopende tekst gesplitst; `panels`, `rows`, `january` en de tabel van oefening 3 zijn lussen; simulatieparameters in één dict `sim`.

**Aanmerkingen en "Voor een 9".**
- $h$ dubbel: gedaan, de functie in het bewijs van Berk en in oefening 2 heet nu $\psi$.
- Nicholson: gedaan, gescheiden wat de enquête vaststelde (verwachtingen) en wat de latere literatuur toeschrijft. De koppeling met het tweede verhaal is nu "de verwachting van Nicholsons analisten past in dat beeld".
- Waarom de ware coëfficiënt op log ME met $\delta$ nul is: gedaan, in oefening 2 (4) ("lineair in bèta en $\delta$").
- Code-trucs: gedaan. Decielen met `pd.qcut`, gewichten van `long_short_weights` in benoemde stappen, `out.attrs = {}` met commentaar.
- Twee werelden in één simulatie: gebleven, want ze beantwoorden één vraag (hoe vaak een significante kenmerk-alpha zonder vergissing) en delen één figuur; STYLE §11.7 eist één vraag, niet één wereld.
- Gemiddelde zinslengte 16,0: binnen de norm van `prose_stats` (≤ 17); niet verder ingekort.
