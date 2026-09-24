STATUS 00_01_rendementen F6b words=5085 prose=PASS open=0 cijfer=8,4 min=8

# Rapport L1 00_01_rendementen

## F0

**Meting.** `words 7160 | sent_mean 13.7 | p90 22 | gt40 0 | para 43 | dash 0 | semicol 11 | overige 0` → FAIL alleen op words (max 5500). `--where`: geen treffers.

**Vijf grootste problemen**
1. *Hele lecture*: 7.160 woorden, boven 6.500 (opbouw hoogstens 7). Theorie telt 2.890 woorden, Oefeningen 984.
2. *Dezelfde eeuw, maand- en dagdata*: "Die valt op dagbasis lager uit, 17,1% tegen 18,3%, omdat de maandreeks positieve autocorrelatie bevat." Verkeerd mechanisme én 252-dagenconventie op een reeks met zaterdagen tot 1952 (feiten 3, 4).
3. *Oefening 2*: toetst het totaalrendement en concludeert over "de premie"; de jarenformule is die van één steekproef (feiten 1, 2).
4. *Toy-voorbeeld*: "Stap 5 is een voorproef". Twee mechanismen en twee niet-afgeleide formules.
5. *Getallen die elkaar tegenspreken*: kurtosis 16 / 16,1 / 17,0 / "ruim negentien"; 26 296 tegen 25 200 dagen; Sharpe 0,04 als "een dertigste"; SE 3,9 bij het meetkundige 9,46% in *Wat er brak* (feiten 5, 8, 11). Plus getallenbrij en de VW-rechtvaardiging pas ná de tabel in *Replicatie*.

**Eis 2 (grep op labels en titel in `lectures/`).** Van buiten aangehaald: `00-01-rendementen` (24×), `thm-rendementen-se` (equity premium puzzle), `thm-rendementen-merton` (volatiliteit). Inhoud die andere lectures aanhalen: de 9,0% en 6,9% van Fisher-Lorie met SE bijna 4 pp (crsp_tape); de autocorrelatie van het dagrendement ≈ 0 en van het absolute dagrendement ≈ 0,30 bij lag 1 en 6 (volatiliteit); de drag (black_scholes); Merton (markowitz, volatiliteit); "autocorrelatie en dikke staarten" als inhoud (setup). `sec-rendementen-standaardfout` blijft op opdracht.

**Schraplijst (schraptoets STYLE §11.11)**

| passage (kopje) | woorden weg | eis die ze niet haalt |
|---|---|---|
| Toy, stap 5 (SE-voorproef, T vs T−1) | 150 | 1: tweede mechanisme; het getal gaat als handberekening naar Theorie |
| Overzicht, alinea "Bijna elke controverse" ingekort, lijst gebundeld | 100 | 1–3: herhaling |
| Intuïtie, windmeter en "twee observaties zijn oud" ingekort | 100 | 1: herhaling |
| Opzet: σ vs σ_ℓ-alinea (feit 7), regressie-zin in warning | 175 | 1 |
| Drag: "Over de namen", Jensen-note, dubbele factor-7,2-zin | 175 | 1–3: nevenresultaat |
| Annualisatie: dubbele uitleg asymmetrie | 55 | 1 |
| Merton: note ARCH/GARCH/VIX, dubbele lees-zin | 120 | 1–3: nevenresultaat |
| Aannames: Mandelbrot-warning, "tienduizend jaar" (feit 14), dubbele kurtosis-uitleg | 385 | 1–3: dikke staarten raken het gemiddelde niet |
| Simulatie: 23%-zin, dubbele conclusie | 110 | 1 |
| Replicatie: getallenalinea's, codecommentaar-argument | 200 | 1 |
| Clustering: variance-ratiotabel (cel 13) | 105 | 1–3: toets hoort bij de random walk-lecture |
| Honderdvijftig jaar (Shiller, cel 14) | 104 | 1–3: drag al bevestigd in de replicatie; feit 9 vervalt |
| Wat er brak, ingekort tot ≤ 120 per element | 70 | — |
| Oefening 3 (aggregatie en staarten) geheel | 300 | 1–3: vierde oefening, geen instap/afleiding/replicatie |
| Oefeningen 1 en 2 ingekort | 120 | — |
| **totaal weg** | **≈ 2.270** | |

Toevoegingen: handberekening toy-SE in Theorie (+40), VW-argument in replicatieblok (+30), naam Regnault (+5). **Verwachte lengte ≈ 4.970 woorden**, onder 6.000 zonder de kern te raken: geen split.

## F1

**Eindmeting.** `words 4754 | sent_mean 14.2 | p90 22 | gt40 0 | para 40 | dash 0 | semicol 5 | stopw 1 | overige 0` → PASS. Sync en execute met HAP_OFFLINE=1 foutloos, geen warnings.

**Geschrapt** (reden: schraptoets, geen eis gehaald tenzij anders vermeld)
- Toy stap 5 (SE-voorproef): tweede mechanisme. Getal (s = 22,9%, SE 13,2 pp) staat nu als handberekening bij de kernstelling.
- Opzet: σ vs σ_ℓ "hooguit twee procentpunt" (feit 7, fout) en regressie-zin in de warning.
- Drag: "Over de namen", Jensen-note. Merton: note ARCH/GARCH/VIX. Aannames: Mandelbrot-warning, "tienduizend jaar" (feit 14), tweede kurtosis-uitleg.
- Variance-ratiotabel (cel 13): de toets hoort bij de random walk-lecture. Shiller-sectie (cel 14): drag al bevestigd in de replicatie (feit 9 vervalt).
- Oefening 3 (aggregatie en staarten): vierde oefening, geen instap/afleiding/replicatie; had dezelfde 252-dagenfout.
- Overzicht "in 1926 al bekend bij statistici" (feit 16, geen bron).

**nb_outputs-diff** (cel 5, simulatie, byte-identiek ondanks herschreven code)
- Cel 2 (toy): drie SE-rijen weg, rijnamen "recept…", "verschil rekenkundig − meetkundig"; waarden gelijk.
- Cel 7/8: commentaar ingekort; `annual_summary` krijgt `per_year`, kolommen "maanden" → "waarnemingen", "samengesteld (meetk.)" → "meetkundig"; waarden gelijk.
- Cel 10: figuur met groeipad van 9% in plaats van horizontale lijn (bytes 86780 → 93912).
- Cel 11: nieuwe tabel via `annual_summary` met werkelijke handelsdagen (262,7/jaar): dagvol 17,10 → 17,46%, SE 1,67 → 1,75 pp, dag-rekenkundig 10,84 → 11,30%; kurtosis nu excess op logs (6,50 / 16,99) in plaats van simpel (7,38 / 16,12). Bedoeld: feiten 3, 4, 8. Maandwaarden (11,57%, 18,34%, 1,83) gelijk.
- Cel 12: laadt uit cel 11, waarden gelijk. Cel 13, 14, 19 (oud) weg; cel 15–17 hernummerd, rijnaam aangepast, waarden gelijk.
- Cel 18 → 16: rij "jaren … bij dit verschil" 301 976 vervangen door "… bij 2 pp verschil" 763,9 met de formule voor twee steekproeven (feit 2).

**Feitenlijst (16).** Verwerkt: 1 (oefening zegt totaalrendement, niet premie), 2, 3, 4 (dagautocorrelatie binnen de maand, VR ≈ 1,10), 5 (vijfentwintigste), 6 (twee derde meer), 7 en 9, 14, 16 (geschrapt), 8 (één kurtosis: log, 17 / κ ≈ 20, uit cel 11), 10 (twee effecten niet gescheiden), 11, 12 (≈ in stelling), 15 (nu hypothetisch: "stel dat twee verklaringen 4% en 6% voorspellen").
Afgewezen: 13 — de 6,9% blijft als citatie: crsp_tape haalt hem aan; narekenen tegen het paper kan niet met repo-bronnen.

**Ook opgelost uit rating2:** "een half procentpunt", "increments" → stappen, meetlat-metafoor, $t$-waarde krijgt eigen symbool τ, naam Regnault, VW-argument in het replicatieblok, figuur-leeswijzer "één histogram zichtbaar", één naam "meetkundig gemiddelde" (kolom ook), analytische Φ(−3) ≈ 0,13% naast 0,16%, 26 296 vs 25 200 (nu 100 × 252 uitgeschreven).

**Afvinklijst §11.9, niet voldaan:** elk getal herleidbaar — de dagcijfers bij de Sharpe-ratio (0,04%, ruim 1%) staan in geen cel (feitencontrole rekende ze na: 0,043% / 1,077%). Overige: ok.

**Labels.** Weg: `ex-rendementen-3` (nergens aangehaald). `thm-rendementen-se`, `thm-rendementen-merton`, `sec-rendementen-standaardfout` en alle andere blijven.

**Open punten**
1. Sharpe-dagcijfers niet in een cel (zie boven); toevoegen kost een cel, of de getallen uit de tabel van cel 11 afleiden.
2. 6,9% van Fisher-Lorie alleen via citatie.
3. `hap.summary_stats(…, "daily")` annualiseert met 252 dagen; de French-dagreeks telt tot 1952 ~300 dagen per jaar. Raakt andere lectures die dagdata annualiseren (melden aan onderhouder `hap`).

## F4

**Meting.** `words 4979 | sent_mean 14.4 | p90 22 | gt40 1 | para 42 | semicol 6 | stopw 1 | overige 0` → PASS. Sync en execute offline foutloos; nb_outputs identiek aan F1 (alleen tekst gewijzigd), diff tegen voor-bestand dus zoals in §F1.

**Feiten (open=2 → 0).** Premie 6%: gehouden als kalibratie en onderbouwd met citatie `MehraPrescott1985` (6,18% over 1889–1978, gelijk aan de equity-premium-lecture); 44 jaar, cel 3 en "ruim drie keer" blijven daardoor gelijk. 1,0323^30 → 1,03228^30 = 2,59.
Inconsistenties: Sharpe — de tekst noemt nu "verhouding op het totaalrendement; op excess heet ze Sharpe-ratio", getallen afgeleid uit cel 11 (11,3/263 = 0,043%, 17,5/√263 = 1,08%, √263 → 0,65 in plaats van √252 → 0,6). ℓ bij Merton → log P_t. σ in de aannamensectie → σ_ℓ, Var(ℓ̄). P_t in de waarderingsvergelijking met "(elders in de reeks p_t)". Setup-notatie en ℓ tegenover r in de Bachelier-lecture: niet aangepast (andere lectures).

**Lezerspunten (15, alle opgelost).** 1 ℓ als logprijs → log P_t in stelling en bewijs. 2 frequentie: T = 1200 maanden, σ_ℓ en VR op één frequentie, en de 1,10 in de replicatie als dezelfde formule toegepast op dagen binnen de maand. 3 het 1932-argument: beide lezingen voorspellen hoge rendementen, het verschil ligt tussen het verwachte rendement volgens een risicomodel en wat volgde. 4 VW-argument: een aandeel dat verdubbelt, weegt dubbel. 5 EW: 12,9%, bijna vier pp boven 9,0%. 6 1,83 als gemeten tegenhanger van de 2% (18,3% in plaats van 20%). 7 de stelling geldt voor elke reeks, alleen σ verschilt. 8 8% = drift ν van het logrendement. 9 Merton-stelling geformuleerd als één bewering (precisie hangt af van T en van N). 10 convergentie uit het drag-bewijs gehaald, in woorden met de wet van de grote aantallen. 11 stap 4 (18,7%) tegenover s = 22,9% benoemd. 12 onafhankelijkheid in het staartstuk genoemd. 13 de vraag theorie of feit in één regel. 14 "tweede ongelijkheid" → "tweede asymmetrie"; "die asymmetrie tussen k en √k". 15 size-decielen = portefeuilles gesorteerd op marktwaarde. Verder: ML-schatter uitgelegd, VR onder één bij negatieve autocorrelatie, zin na tabel in oefening 2 (H9).
Betaald: +225 woorden, ruim binnen 5.500; niets extra geschrapt.

**Navertel-toets, afwijkingen.** *Wat er brak* (1932): argument herschreven, zie punt 3. *Wanneer de aannames niet gelden* (frequentie 0,085 en VR): zie punt 2. *Overzicht* (welke vraag theorie of feit): punt 13. *Replicatie* (waarom VW de replicatie is): punt 4.

## F5-1

**Meting.** `words 4967 | sent_mean 14.2 | p90 22 | gt40 0 | para 42 | semicol 5 | stopw 1` → PASS. Sync en execute offline foutloos. nb_outputs: alle eerder aangehaalde getallen gelijk; alleen kolomnamen en nieuwe kolommen (zie hieronder).

**Feitelijke fouten:** geen gemeld.

**Criterium 1**
- Zin met $P_t = \E_t[m x]$ in de variance-drag-slotalinea: gedaan, vervangen door "Een prijs is een verwachte uitkering, dus elke waarderingsformule in deze reeks gebruikt het rekenkundige" (geen nieuwe symbolen).
- Eenheden bij de kurtosisformules: gedaan (links gemiddelde per jaar over T jaar, σ per jaar; rechts variantie per waarneming uit N waarnemingen).
- Eén afspraak voor σ: gedaan. In de Opzet: vanaf hier is σ de volatiliteit van het logrendement; σ_ℓ bestaat niet meer. De "we laten de index weg"-zin en "σ_ℓ ≈ σ" in het drag-bewijs zijn vervallen.

**Criterium 2**
- Signaal/ruis-alinea in Annualisatie als zijstap: gedaan. De rekensom is naar de dagtabel verhuisd (nieuwe rijen "signaal/ruis per waarneming" 0,0399 en "per jaar" 0,6471); de alinea noemt alleen 0,04 en 0,65.
- Clustering-subsectie maakt het slot langer: afgewezen, STYLE §11.11 eis 2. De volatiliteitslecture haalt de 0,30 bij lag 1 en 6 uit deze subsectie aan.

**Criterium 3**
- Lange zin variance drag: gedaan (zie criterium 1).
- "excess rendement" → "premie": gedaan ("Voor de premie heet deze verhouding de Sharpe-ratio").
- Zin over stap 4: gedaan, gesplitst in "Stap 4 deelde door drie en gaf 18,7%. Daar ging het om de drie jaren zelf, hier om het proces waaruit ze komen."

**Criterium 4.** De wrijving tussen /3 en /(T−1): gedaan met dezelfde twee zinnen in het kernresultaat.

**Criterium 5**
- Kolomnamen simulatietabel: gedaan ("standaardfout gemiddelde (pp)", "theorie gemiddelde (pp)", "relatieve fout variantie", "theorie variantie").
- Slice: gedaan, `step = per_year // k` benoemd, en de tekst zegt "elke $252/k$-ste dagkoers".
- Kurtosiskolom aangeplakt: gedaan, nu via `describe_frequency` in één tabel (getransponeerd: statistieken als rijen). De naam "excess kurtosis (log)" blijft: vakterm die cursief is ingevoerd (STYLE §3, Engelse vakterm).

**Criterium 6**
- Getallen in "Dezelfde eeuw": gedaan. Twee alinea's; alleen de twee standaardfouten (1,83 en 1,75) en de factor 22 staan nog in de tekst; 17,5/18,3, 0,047, VR 1,10 en 6,5/17,0 verwijzen naar de tabellen.
- 95%-interval: gedaan, als kolommen "95%-interval, onder/boven" in de tabel origineel/hier (1,96 × SE rond het meetkundig gemiddelde: VW 1,81%–17,12%). De tekst zegt nu "ongeveer 2% tot 17%" in plaats van het interval rond het rekenkundige (4%–19%); de conclusie blijft.

**Criterium 7.** Geen aanmerkingen.

**Nalezing met de rubriek.** Alinea na de kurtosisformules gesplitst (was zeven zinnen). Geen verdere punten.

## F6-1

**Meting.** `words 5085 | sent_mean 14.3 | gt40 0 | semicol 5` → PASS. Sync en offline execute foutloos. nb_outputs: alleen een nieuwe rij "volatiliteit logrendement" (0,1832 / 0,1749) in de dagtabel; alle aangehaalde getallen gelijk. Labels ongewijzigd.

**Feitelijke fout (setup-notatie):** gedaan. "Reserveert kleine letters voor logs" → "Zoals in [](#00-00-setup) is $r$ het netto simpele rendement, en krijgt het logrendement een eigen symbool".

**Drie verbeteringen uit het eindbestand**
1. Notatie: gedaan (zie hierboven). Prijs en dividend nu als setup: $p_t$, $d_{t+1}$ in niveaus ("beide als niveaus, zoals in de hele reeks"); bij Merton $\log p_t$ als logprijs, logrendement blijft $\ell$.
2. σ met één getal: gedaan (maandreeks 18,34% simpel tegen 18,32% log, uit de nieuwe tabelrij). ν, μ_g, μ_a, μ naast elkaar in één zin in de variance-drag-sectie.
3. Maand- en dagtabel: gedaan, aangekondigd als illustratie van [](#thm-rendementen-merton) met een eigen verwachting (standaardfout gemiddelde nauwelijks beter, volatiliteit en staarten sterk).
Ook: koploze simulatiezin hersteld; "Daarna wordt er nergens meer geïmporteerd" weg; EW-getallen uit de tekst (staan in de tabel); bid-ask bounce met één zin mechanisme; toy eindigt met de brug naar de standaardfout.
Afgewezen: blokverwerking in de simulatiecel (STYLE §5, looptijd en geheugen: één cel onder 60 s; het commentaar zegt wat het is).

**Naadpunten**
1 en 2: gedaan (zie feitelijke fout en punt 1; $P_t$, $D_{t+1}$ → $p_t$, $d_{t+1}$ volgens de correctie van de orkestrator). 3 ($R$ bruto): L1 volgt al de setup, niets te doen. 5 (premie): gedaan. Eén zin in de Intuïtie: 6% is een kalibratie (Mehra-Prescott 6,18% over 1889–1978); de setup meet 8,3% op French-data sinds 1926; het verschil komt van de periode, en voor de standaardfout doet het er niet toe. 6 ($T$ jaren of waarnemingen): gedaan, in L1 is $T$ nu overal jaren en $N$ waarnemingen (autocorrelatie: $\sigma\sqrt{VR(N)}/\sqrt{N}$, $N = 1200$ maanden). 7 ($\kappa$): de dubbele betekenis zit in de Bachelier-lecture; L1 niet aangepast. 4 en 8–10 raken L1 niet.

**Verificatie na de correctie ($p_t$, $d_{t+1}$).** Geen $P_t$ of $D_{t+1}$ meer in de lecture. `--check` PASS (5085 woorden), sync en HAP_OFFLINE=1-execute foutloos, geen warnings. nb_outputs identiek aan de stand vóór de correctie; tegen het voor-bestand alleen de verschillen uit §F1, §F5-1 en de rij "volatiliteit logrendement". Alleen `ex-rendementen-3` is weg (nergens aangehaald); `thm-rendementen-se`, `thm-rendementen-merton` en `sec-rendementen-standaardfout` bestaan.
