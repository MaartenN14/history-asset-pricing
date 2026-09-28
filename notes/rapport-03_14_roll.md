STATUS 03_14_roll F6b words=5419 prose=PASS open=0 cijfer=- min=-

# Rapport 03_14_roll (workflow-herziening)

## F0

**Nulmeting.** `03_14_roll.md  words 6117  sent_mean 20.3  sent_p90 36  sent_gt40 13  para_mean 63  dash 32  semicol 31  motief 4  Lnum 2  deel 0  u_form 0  je_form 1  taboo 0  stopw 12  calque 1  engquote 9`. `--where`: r. 49 "epistemische status". Verder met de hand: "motief 3" (r. 50), "motief 1" (r. 598, 757), "uit L4" (r. 143, 165), "alfa" (r. 750).

**Vijf grootste problemen.**
1. *Taal*, overal: zinnen van gemiddeld 20,3 woorden, 13 boven 40, alinea's van 63 woorden, 32 streepjes, 31 puntkomma's, 12 stopwoorden ("precies" als versterker).
2. *Notatie* (Toy, Theorie): de drie activa heten A, B, C, terwijl $A, B, C, D$ ook de scalars uit [](#eq-markowitz-abcd) zijn ("$\beta_{A,p}$" naast "$A\mu_p - B$"); L4 noemt ze nu aandelen, kleine aandelen, obligaties. Rendementen heten bruto $\mathbf{R}$ met $\mu = 0{,}10$; de setup wil netto $r$. Subscript $m$ is de markt zonder de zin die haar van de SDF scheidt.
3. *Structuur*: imports-cel in *Overzicht*; Overzicht zonder vraag-antwoord en lijst; geen routekaart, geen *Samengevat*; toy zonder opzet-tabel en tabel hand/code (brede DataFrame plus print); *Simulatie* stelt twee vragen (steekproef én populatiepad met gevoeligheid in $N$); "Waar we zijn" verwijst naar vier lectures en stelt twee vragen.
4. *Replicatie*: blok ≈ 370 woorden; getallen in proza (tautologie, $R^2$) zonder tabel origineel/hier en zonder oordeel "Geslaagd / Gedeeltelijk geslaagd".
5. *Theorie te vol*: bewijs van Rolls stelling (≈ 20 regels) open; "Wat de literatuur ermee deed" (Stambaugh, Shanken, Jagannathan-Wang) is geschiedenis zonder rol in de afleiding; propositie-bespreking met formule voor $\Cov(R_m, R_d)$ en "langs het pad"-alinea; sinaasappelsap-alinea met paginanummers uit secundaire bron. Oefeningen: geen instap, geen "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** Elders aangehaald: alleen het paginalabel `03-14-roll` (02_08, 03_13, 03_15, 04_18, 04_21, 04_24, 08_39). Inhoudelijk: menselijk kapitaal in de ware markt (08_39 r. 976), "dezelfde vijftig aandelen" (04_24 r. 1002), "Rolls tautologie" (04_18 r. 815), "verwerping treft alleen de index" (04_18 r. 25). 04_21 r. 430 schrijft "efficiënte prijs plus een fout $u$ (bid-ask bounce), zoals in [](#03-14-roll)"; die inhoud staat niet in deze lecture (Rolls spread-schatter uit 1984 hoort bij 04_24). Geen `thm-`, `eq-`, `fig-` of `ex-roll`-label wordt elders aangehaald.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Waar we zijn | vier verwijzingen, twee vragen, "Maar niemand had"-zin | 50 | herhaling; hoogstens twee verwijzingen |
| Overzicht | drie alinea's naar vraag-antwoord, lijst, geschiedenis | 60 | dubbel met Intuïtie |
| Intuïtie | note "Roll kwam uit Chicago" | 55 | anekdote zonder rol in het argument |
| Intuïtie | "Zou een index die bijna ..."-alinea en $R^2$-alinea ingekort | 60 | herhaald in Theorie |
| Theorie, stelling | bewijs naar dropdown en ingekort, drie conclusies als lijst | 240 | bewijs > 6 regels; conclusies dubbel met Intuïtie |
| Theorie | "Wat de literatuur ermee deed" tot korte `{note}` | 150 | geschiedenis; Shanken en JW blijven in "Wat er brak" |
| Theorie, propositie | "twee dingen"-alinea met $\Cov(R_m,R_d)$-formule, "langs het pad"-alinea | 190 | nevenresultaat; het pad staat in de figuur |
| Theorie, $R^2$ | sinaasappelsap met paginanummers, motief-alinea | 180 | niet gerepliceerd; één zin volstaat |
| Simulatie | willekeurige-kantelingen-wolk en gevoeligheid in $N$ (25, 500) | 170 | tweede vraag; populatiepad naar Theorie |
| Simulatie | getallenalinea's naar tabel plus oordeel | 150 | getallen in proza |
| Replicatie | blok naar ≤ 250 woorden | 120 | te lang |
| Replicatie | tautologie- en $R^2$-alinea's naar tabel origineel/hier | 150 | getallen in proza |
| Wat er brak | elk element ≤ 120 woorden | 60 | te lang |
| Oefeningen | ex-1 deel 3, uitweidingen in uitwerkingen | 130 | nevenresultaat |
| **totaal** | | **≈ 1.765** | |

**Verwachte lengte.** 6.117 − 1.765 ≈ 4.350; erbij komen vraag-antwoord en lijst, voorspelling aan het eind van *Intuïtie*, toy-opzet en stappen, routekaart, *Samengevat*, zinnen rond gesplitste cellen, twee tabellen origineel/hier met oordeel, "Wat dit leert:" (≈ 600). Verwacht 4.900 tot 5.100, onder 5.500 zonder de kern te raken. Geen splitsing.

## F1

**Eindmeting.** `words 5260  sent_mean 14.4  sent_p90 22  sent_gt40 0  para_mean 42  dash 0  semicol 5  motief 0  Lnum 0  deel 0  u_form 0  je_form 0  taboo 0  stopw 0  calque 0  engquote 0` → PASS. `--where`: geen treffers. `jupytext --sync` en `--execute` met `HAP_OFFLINE=1`: foutloos, geen warnings in de uitvoer.

**Geschrapt.** Note "Roll kwam uit Chicago" (anekdote); "Wat de literatuur ermee deed" → dropdown-note Stambaugh/Shanken, Jagannathan-Wang alleen in "Wat er brak" (geschiedenis); bewijs stelling naar dropdown met stapkoppen, steekproefversie als gevolg `cor-roll-steekproef` (H3); "twee dingen"-alinea met $\Cov(R_m,R_d)$-formule en "langs het pad"-alinea (nevenresultaat, nu één alinea met H6); sinaasappelsap-paginanummers (secundaire bron, niet gerepliceerd); willekeurige-kantelingen-wolk en gevoeligheid $N = 25/500$ ($\rho^* = 0{,}72/0{,}34$) (tweede vraag; de willekeurige kanteling staat al in de simulatietabel); getallenalinea's in simulatie en replicatie ingekort; replicatieblok ≈ 200 woorden; ex-1 deel 3 en uitweidingen.

**Toegevoegd/verplaatst.** Vraag-antwoord en lijst in Overzicht, imports-cel naar Toy; drie voorspellingen aan het eind van Intuïtie, ingelost in Theorie (H12); toy met opzet-tabel, recept, vijf stappen en tabel hand/code; routekaart; lees-zin bij elke vergelijking; populatiepad (wereld + pad + figuur) van Simulatie naar Theorie "### Numerieke uitwerking" (§11.7), zodat Simulatie één steekproefvraag heeft; *Samengevat*; tabel origineel/hier met oordeel "Geslaagd … gedeeltelijk geslaagd"; ex-2 is nu een afleiding ($R^2$-formule) plus data; "Wat dit leert:" bij elke uitwerking.

**Notatie.** Activa heten aandelen, kleine aandelen, obligaties (was A, B, C, botste met de scalars $A$–$D$). Netto rendementen $r$, $\beta_{i,p} = \Cov(r_i,r_p)/\Var(r_p)$, excess $R^e_i = r_i - R^f$ (setup). Expliciete zin: subscript $m$ = marktportefeuille, niet de SDF. "alfa" → "alpha"; "overlevenden" in het blok.

**`nb_outputs`-diff, elk verschil bedoeld.**
- toy: brede tabel plus print → tabel "met de hand / code"; alle aangehaalde waarden gelijk (0,368; −0,01248; 1,6053; 0,0921; 0,0339; 0,0661; 1,8333; 0,06; 0,0333; 0,9868). Gewichten (0,44; 0,336; 0,224) niet meer getoond.
- nieuw: padsamenvatting (hoogste helling/premie 1,715 bij correlatie 0,748; nulhelling 0,623) en padfiguur zonder wolk.
- simulatiecel gesplitst in lus (geen uitvoer) en tabel; tabel identiek. `rng`-volgorde ongewijzigd (wereld → steekproeven).
- oude cel "gevoeligheid in $N$" verdwenen (0,718; 0,623; 0,344).
- tautologie gesplitst in proxy-cel (print identiek) en tabel (identiek). Industrie-indeling in eigen verborgen cel; $R^2$-tabellen identiek.
- nieuw: tabel origineel/hier (1,000; 0,000; 0,349; 0,411).
- ex-1: indexnamen A/B/C → aandelen, kleine aandelen, obligaties; waarden identiek. ex-2 en ex-3 identiek. $R^2$-figuur: andere jitter (rng-stand), geen getal.

**Correctie.** De oude tekst zei "eerst steiler, tot bijna driemaal de ware premie, tussen correlatie 1 en ongeveer 0,8"; de nieuwe cel geeft 1,7 keer bij correlatie 0,75. Tekst volgt de cel.

**Afvinklijst §11.9, wat niet voldoet.** Toy-codecel ≈ 40 regels (één toy-cel is voorgeschreven); na de imports-cel volgt direct de opzet (zoals de template). Overige: ok.

**Labels.** Geen verdwenen. Nieuw: `cor-roll-steekproef`. Alle cross-refs in de lecture bestaan.

**Open punten.**
1. Naad: `04_21_volatiliteit.md` r. 430 schrijft "efficiënte prijs plus een fout $u$ (bid-ask bounce) … zoals in [](#03-14-roll)"; dat staat niet in deze lecture (Rolls spread-schatter hoort bij 04_24).
2. F2: Roll 1988 (0,35/0,20, nieuwsdagen) en Roll 1984 (via Boudoukh e.a.) komen uit de vorige tekst; tegen de bron houden. Ook Shanken (0,7) en Stambaugh (een tiende).
3. Oefeningen: ex-1 is als instap nog vrij rekenintensief (vijf grootheden met de hand).

## F4

**Meting.** `words 5404  sent_mean 14.6  sent_p90 23  sent_gt40 0  para_mean 43  dash 0  semicol 5`, overige 0 → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings; `nb_outputs`-diff tegen F1: geen verschil.

**F2 (open=1).** Oplossing (a): in "De tweede vraag" twee zinnen over Rolls spreadschatter {cite}`Roll1984b` (bid-ask bounce, microstructuurruis, negatieve autocorrelatie). De verwijzing in 04_21 r. 430 klopt daarmee weer; 04_21 niet gewijzigd. Bib-key bestond al.

**Lezerspunten.**
1. Stap 5: $R^2$ nu als kwadratensommen uitgeschreven. 2. ex-1: met de hand alleen $\mathbf{d}$ en $\boldsymbol{\Sigma}\mathbf{d}$ (koppeling aan stap 5), rest met code. 3. H11: slotzin Simulatie verwijst naar de toy-$R^2$ 0,9868. 4. H3: propositie gesplitst, punt 2 is nu `cor-roll-rhostar` (verwijzingen in Simulatie, Replicatie en ex-1 aangepast). 5. Bewijsstap 2 krijgt een aankondigende zin. 6. Bijzin bij `thm-capm-zerobeta`. 7. Attenuatie in één bijzin uitgelegd. 8. H1: beleggers handelen op nieuws. 9. H12: zin na het gevolg "eerste voorspelling van de intuïtie". 10. Overgang in Intuïtie: "Los van die kritiek stelde Roll later een tweede vraag".
11. Correlaties (1 en 0,90) in de zin gezet. 12. Richting van $\rho^*$ in Samengevat. 13. "strikt convex, omdat Σ positief definiet is". 14. Eén zin over teller en noemer langs het pad. 15. Deels: SML wordt nu ingevoerd bij de propositie en daarna zo genoemd; "de lijn" blijft als algemene term in Intuïtie en Overzicht (lezer zonder symbolen).

**Betaald met.** Dropdown-note Stambaugh/Shanken geschrapt (≈ 85 woorden; geschiedenis, niet aangehaald; Shanken blijft in "Wat er brak"); handberekening van $\Var(R_d)$, $\Cov$, $c^*$, $\rho^*$ in ex-1 (≈ 50) naar de code.

**Navertel-toets.** Afwijking bij "Bijna-efficiënte proxy's": de lezer las "minstens zo sterk met de markt correleert". Door de splitsing staat de maximale correlatie $\rho^*$ nu in een apart gevolg met sprekende titel. Andere secties kwamen overeen met de bedoeling.

**Labels.** Nieuw: `cor-roll-rhostar`. Geen verdwenen. Stambaugh1982 wordt niet meer geciteerd.

## F6-1

**Meting.** `words 5402  sent_mean 14.7  sent_p90 23  sent_gt40 0  para_mean 43  semicol 8  engquote 1` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings. `nb_outputs`-diff tegen F4: alleen kolom-, index- en celnummers (presentatie); alle waarden identiek, `rng`-volgorde ongewijzigd.

**Feitelijke fouten.** Geen gemeld. Twijfelpunt ("Dat had de intuïtie voorspeld" tegenover een pad dat eerst stijgt) opgelost, zie opbouw.

**Verbetering 1, opbouw: gedaan.** Het $R^2$-deel begint in Intuïtie en in Theorie met een vraag die aan de kritiek vastzit ("Als de lijn niet te toetsen is, wat verklaren markt en industrie dan wel?"). Sinaasappelsap en bid-ask zijn samen teruggebracht tot twee zinnen, zonder werknotitie; de zin met {cite}`Roll1984b` (microstructuurruis, bid-ask bounce, spread $2\sqrt{-\Cov(\Delta p_t,\Delta p_{t-1})}$) blijft voor 04_21. `BoudoukhRichardsonShenWhitelaw2007` wordt niet meer geciteerd. Het "Waarom" bij de bijna-efficiënte proxy's zegt nu dat de helling eerst kan stijgen; de zin na de padfiguur zegt wat de intuïtie wel en niet voorspelde.
**Verbetering 2, code: gedaan.** `tilt_to_corr` in een eigen cel, met een zin ervoor (kwadratische vergelijking in $c$, kleinste positieve wortel) en de wortel via benoemde maskers in plaats van een comprehension; de simulatielus in een eigen cel; `adjusted_r2` met benoemde `r2`; de portefeuilletabel met gewone lussen; kolom- en indexnamen voluit (geen "pop.", "q05", "sd", "gem.", "SE", "p.m.", "p.j.", "ind.", "in-sample tangent"), ook in de wereld-cel en oefeningen 2 en 3.
**Verbetering 3, replicatie: gedaan.** De alinea's na de tautologietabel en na beide $R^2$-tabellen verwijzen naar rijen en kolommen in plaats van de getallen te herhalen. Het oordeel onder de tabel origineel/hier noemt de vergeleken waarden nog.

**Aanmerkingen en "voor een 9".**
- Simulatie, waarom $\rho \ge 0{,}90$: gedaan, één zin (de ware helling ligt daar rond of boven de premie; de nulhelling bij 0,62 valt buiten dit bereik; de schade zit in het intercept).
- GLS-zin: geschrapt (schraptoets, zonder vervolg). Bid-ask: formule toegevoegd in plaats van een getal (geen data in `hap.data`).
- "stochastic discount factor" in Opzet → "SDF". Werknotitie over de secundaire bron: geschrapt.
- Toy stap 1: zin toegevoegd dat [](#01-04-markowitz) de formules voor $\lambda$ en $\delta$ afleidt uit [](#eq-markowitz-foc) en de restricties (daar hebben ze geen label).
- Afgewezen: een toy en simulatie voor het $R^2$-deel. STYLE §11.7: het toy heeft één mechanisme en de simulatie beantwoordt één vraag; een tweede simulatie gaat volgens de schraptoets weg of wordt een oefening. Oefening 2 speelt die rol al.
- Naadpunt deel 3a punt 6: "Waar we zijn" zegt nu dat in 1977 nog niemand de vraag had gesteld en dat het bezwaar dat later in de APT-discussie terugkwam hier begint; geen code geraakt.
