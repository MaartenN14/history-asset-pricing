STATUS deel-5 naad open=1

# Naadcontrole Deel V na de eerste herziening (L26 t/m L33, workflow §12)

Werkwijze: alleen .md, via grep en korte sed-uitsneden (budget 30 aanroepen). Een script controleerde alle 268 linkregels (143 verschillende doelen) vanuit `05_*.md`, ook de `{prf:ref}`-doelen: elk doellabel bestaat (0 ontbrekend), en geen enkele link gaat naar een `ex-*`-label. Alle 106 regels vanuit Deel V naar 00_00, 00_01 en Deel I–IV zijn doorgelopen; inhoudelijk nagelopen op de doelplek: 00_00 (Santa-Clara, 2,2% in februari 2009), 01_03 (log CAPE tot 2015), 01_04 (1/N, schattingsfout), 02_06 (elk patroon heeft een SDF), 02_09 (VRP, smirk), 03_17 (drie factoren), 04_18 (klein-groei, derde oefening), 04_20 ($\phi = 0{,}941$, $\rho = 0{,}9638$), 04_21 (leverage-effect), 04_23 (`prop-behavioral-joint`), 04_25 (factorpremies te koop). Alle 78 regels in de rest van het boek die naar Deel V linken, verwijzen naar een bestaand label (ook na het verwijderen van de dertien figuren, cellen en stellingen); de beweringen over Deel V in 03_13, 03_17, 04_20, 04_23, 04_25, 06_34–06_36 en de getallen in 08_38/08_39 zijn nagelopen.

## Naadpunten

### Verwijzingen en beweringen over andere colleges

1. **Linkdoelen en oefeningslabels.**
   - Plek: alle `05_*.md`; `05_26_sdf_unificatie.md:974`.
   - Wat: 0 ontbrekende doelen, 0 `ex-*`-links. Naad 3 uit Deel IV is opgelost: 05_26:974 schrijft nu "de derde oefening van [](#04-18-fama-french)". Inkomende links naar verwijderde labels (cel-sdf-unificatie-sim-hj, thm-wisselkoersen-sprongen enz.) komen nergens voor.
   - Oordeel: opgelost.

2. **"Het effect van Michaud uit 01_04".**
   - Plek: `05_30_wisselkoersen.md:1389`, "Dat is het effect van Michaud uit [](#01-04-markowitz)".
   - Wat: 01_04 noemt Michaud nergens (grep: 0 treffers); het beschrijft wel de schattingsfout in $\boldsymbol\mu$ (`01_04:721–751`). De lezer zoekt in 01_04 een naam die er niet staat.
   - Oordeel: open.
   - Voorstel: schrijf "Dat is de schattingsfout uit [](#01-04-markowitz), waarbij $\boldsymbol{\Sigma}_F^{-1}\boldsymbol{\mu}_F$ de fout in $\boldsymbol{\mu}_F$ versterkt".

3. **Wie de parametrische portefeuille bedacht.**
   - Plek: `05_30_wisselkoersen.md:1196–1198` ("Barroso en Santa-Clara vervingen het sorteren op één kenmerk door gewichten die rechtstreeks als functie van kenmerken worden geschat. Die parametrische portefeuilles zijn het onderwerp van [](#05-31-portfolio-choice)").
   - Wat: 05_31 schrijft de methode toe aan Brandt, Santa-Clara en Valkanov (2009) (`05_31:52–54`), en 05_30 zelf past de regel al toe (`05_30:1332`). De vooruitwijzing suggereert dat Barroso en Santa-Clara (2015) de methode invoerden en dat 05_31 later komt.
   - Oordeel: open.
   - Voorstel: schrijf "Barroso en Santa-Clara pasten daarvoor een methode toe die gewichten rechtstreeks als functie van kenmerken schat; waar die parametrische portefeuilles vandaan komen, is het onderwerp van [](#05-31-portfolio-choice)".

4. **Getallen in Deel VIII die niet in Deel V terug te vinden zijn.**
   - Plek: `08_38_wat_we_weten.md:953` (carry $t = 3{,}0$ bij [](#05-30-wisselkoersen)) en `:954` (std. 3,3% → 0,8%, kurtosis 18 → 33, slechtste maand 2020-03, met [](#05-29-opties-crashrisico)).
   - Wat: geen van deze getallen staat in het proza van 05_30 of 05_29 (grep op `3{,}0`, `3,3%`, `kurtosis`, `2020-03`). De overige beweringen over Deel V kloppen: 08_38:777 en :955 (simulatie en hellingen 0,72–1,20, $t$ 2,6–2,9 staan op `05_28:527`, `:795–799`), 08_39:236/1109 (eigen simulatie van 08_39), 08_39:958 (05_31 staaft alleen de ontleding; de perioden 1927–1962 komen uit 08_39 zelf), 06_34:24, 06_35:27–29, 06_36:27/335.
   - Oordeel: open (bij de herziening van Deel VIII).
   - Voorstel: laat de herziening van 08_38 elk getal in de tabel naar de plek in het proza van het genoemde college herleiden of het college uit de kolom halen.

### Vaste termen (STYLE §3)

5. **"Stochastic discount factor" in proza.**
   - Plek: `05_26_sdf_unificatie.md:38`, `05_29_opties_crashrisico.md:127`, `05_30_wisselkoersen.md:24`, `05_32_intermediaries.md:23` en `:214`.
   - Wat: kaart §3, 03_13 (22×), 04_18, 04_23 en de slotzin van 04_25 (`:1101`, "*stochastische discontofactor* $m$ (SDF, ...)") gebruiken de Nederlandse term; 05_27 ook. 05_26 opent direct daarna met de Engelse term, en 05_32 gebruikt hem onverklaard in lopende tekst. STYLE r.222 en r.229 noemen nog de Engelse term (en "disconteringsfactor"), dus de projectregel spreekt zichzelf tegen.
   - Oordeel: open.
   - Voorstel: schrijf op de vijf plekken "stochastische discontofactor" (bij eerste gebruik met "(*stochastic discount factor*, SDF)") en pas STYLE r.222/229 aan de kaart aan.

6. **Overige verboden vormen.**
   - Plek: alle `05_*.md`.
   - Wat: geen "excess rendement", "value-weighted", "lecture ", "Itô's lemma", "afdekken", "efficiënte rand", "overlevers" of "alfa" in proza. "equity premium" en "Equal-weighted" alleen in code (`05_29:633`, `05_30:962`); "term premium" eenmaal tussen haakjes (`05_28:26`); "afgeprijsde koersen" (`05_32:333`) is geen "prijst" voor waarderen.
   - Oordeel: opgelost.

### Notatie

7. **Bruto risicovrije rente als $R^f$.**
   - Plek: `05_26_sdf_unificatie.md:143` ($R^f = 1/\E[x^*] = 1{,}0526$), `05_29_opties_crashrisico.md:133` ($R^f = 1/\E[m]$), `05_30_wisselkoersen.md:154` ($R^f = 1/\E[m] = 1{,}00$, $R^{f*} = 1{,}0204$) en `:1217`, `05_33_fama_vs_shiller.md:340` ($1/R^f_{t+1}$).
   - Wat: STYLE r.177 en kaart §3: $R^f$ is netto, bruto is $1 + R^f = 1/\E[m]$. 05_27 is hersteld; 05_28, 05_31 en 05_32 gebruiken $R^f$ niet in formules.
   - Oordeel: open.
   - Voorstel: schrijf $1 + R^f = 1/\E[x^*] = 1{,}0526$, $1 + R^f = 1/\E[m]$, $1 + R^f = 1{,}00$ en $1 + R^{f*} = 1{,}0204$ (ook 05_30:1217) en $1/(1 + R^f_{t+1})$.

8. **Log rendement als $r$ in 05_33.**
   - Plek: `05_33_fama_vs_shiller.md:135` ($r_{t+1} = dp_t - \rho\,dp_{t+1} + \Delta d_{t+1}$), `:392` ("het bruto rendement $R$ door het log rendement $r$ vervangen"), `:397`, `:407`, `:410`, `:1081`, `:1095`.
   - Wat: 04_20 schrijft dezelfde Campbell-Shiller-benadering in $\ell$ (`04_20:150`, 34×) en 04_23 is in Deel IV naar $\ell$ omgezet. In heel Deel V komt $\ell$ alleen in 05_29 voor (`:297`). 05_31:119 gebruikt $r_{t+1}$ voor een lokaal gedefinieerd overrendement (notatie van Brandt); dat blijft.
   - Oordeel: open.
   - Voorstel: vervang in 05_33 $r_{t+1}$ door $\ell_{t+1}$ (135, 392–410, 1081, 1095) en schrijf op 392 "het log rendement $\ell$".

9. **$pd_t$ tegenover $dp_t$, en de risicoaversie uit 03_13.**
   - Plek: `05_27_drie_antwoorden.md:714`, `:26`; `05_33_fama_vs_shiller.md:128`.
   - Wat: 05_27 schrijft nu "beweegt $pd_t = -dp_t$" (naad 9 uit Deel IV opgelost) en "bijna vijftig ($\gamma = 47{,}6$)"; "in de dertig" komt in Deel V niet meer voor. 05_33 gebruikt alleen $dp_t = d_t - p_t$, na "Vanaf hier zijn kleine letters logs", zoals 04_20. $\phi = 0{,}941$ en $\rho = 0{,}9638$ (`05_33:506`) zijn gelijk aan `04_20:357`.
   - Oordeel: opgelost.

10. **Symbolen met een tweede betekenis.**
    - Plek: `05_28_termijnstructuur_premies.md:366` ($\boldsymbol\gamma'\mathbf f_t$ als gewichten van de Cochrane-Piazzesi-factor); verder $\theta$ (05_26:688 lading, 05_31:134 regelcoëfficiënten, 05_32:236 helling van de haircut, 05_33:155 extrapolatiegewicht), $\kappa$ (05_27:420 constante, 05_28:457 correlatieverval, 05_29:367 gemiddelde sprong), $\eta$ (05_27:485 consumptieschok, 05_29:427 Girsanov-drift, 05_32:114 kapitaalratio, 05_33:399 meetfout), $\phi$ (05_27 gewoonte, 05_33:149 persistentie van de premie), $r$ als risicovrije rente in 05_29:367 (notatie van 02_09).
    - Wat: in Deel IV–V is $\gamma$ overal de risicoaversie (05_27, 05_29:118, 05_31:123, 05_32:419); in Deel IV is een zelfde botsing (04_25, $\gamma$ als precisie) al opgelost. De andere symbolen zijn lokaal gedefinieerd en botsen niet met de eerste definitie in 04_20/04_25 ($\phi$ is ook daar persistentie; 04_25 gebruikt nu $\tau$).
    - Oordeel: $\gamma$ in 05_28 open; de overige blijven, projectkeuze (lokaal gedefinieerd, notatie van het origineel).
    - Voorstel: schrijf in 05_28 vanaf r.366 $\boldsymbol\delta'\mathbf f_t$ (of $\mathbf a'\mathbf f_t$) voor de factorgewichten, met één zin dat Cochrane en Piazzesi hier $\gamma$ schrijven.

### "Wat we al weten" en "Wat er daarna kwam"

11. **Bruggen 04_25 → 05_26 → … → 05_33 → 06_34.**
    - Plek: openings- en slotparagraaf van alle acht colleges plus 04_25:1098–1101 en 06_34:24–30.
    - Wat: elke vooruitwijzing noemt het onderwerp dat het volgende college in zijn "Wat we al weten" oppakt (rampen/gewoonte/LRR → 05_27; obligatiepremies → 05_28; crashrisico in opties → 05_29; carry → 05_30; intermediairs → 05_32; Fama-Shiller 2013 → 05_33; factor zoo → 06_34). De terugverwijzingen kloppen: 05_26:27 (04_25:64 noemt Dimensional en AQR die factorpremies verkopen), 05_28:24–29 (PCA met drie factoren staat in 03_17:39 en :858), 05_29:24–25 (VRP 4,85 en 3,15 punten in 02_09:1294–1295, "gemiddeld vier" is een eerlijke samenvatting). Alleen de toeschrijving in 05_30 wringt (naad 3).
    - Oordeel: opgelost (op naad 3 na).

### Herhaling

12. **Kerngetallen en Santa-Clara.**
    - Plek: `05_27:26` (47,6), `05_31:554` (1,31), `05_29:1353`/`05_30:936`/`05_31:1009` (0,62), `05_30:604` (0,911), `05_33:429`, `:1025` (Martin).
    - Wat: 47,6 staat alleen in 05_27 en klopt met 03_13; 6,92, 0,80 (als premie), 4,87, 6,7 (als premie) en 483 komen in Deel V niet voor; 1,31 in 05_31 is een FF3-alpha van IVOL-kwintielen, een andere grootheid dan in 04_19; 0,62 is drie keer een andere grootheid; 0,911 alleen in 05_30; Martin wordt zonder getal genoemd. HJ "ongeveer een half per jaar" (05_30:26) past bij $a = 0{,}47$ (05_30:348). De parafrases van SantaClara2026 (00_00:121–127, 05_26:1155, 05_30:116–118, 05_31:53, 05_32:79, 05_32:1076, 06_34 slot) spreken elkaar niet tegen: steeds "risico met een premie of denken iets te weten wat de prijs niet weet", plus de LTCM-les (hefboom, mark-to-market, deadline) die ook 08_38:957 noemt.
    - Oordeel: opgelost, geen tegenstrijdige getallen.

Open: 2, 3, 4, 5, 7, 8, 10 ($\gamma$ in 05_28). Naad 4 hoort bij de herziening van Deel VIII; naad 5 vraagt ook een aanpassing van STYLE r.222/229.

## Afhandeling (orchestrator, 2026-09-30)

Opgelost in dezelfde commit: naad 2 (05_30: "het bekende effect uit 01_04" in plaats van Michaud), 3 (05_30: Barroso en Santa-Clara pasten de methode toe; herkomst bij 05_31), 5 (05_26, 05_29, 05_30, 05_32: stochastische discontofactor in proza; STYLE §3 gelijkgetrokken: voorbeeld en Engels-lijst aangepast, rij in de tabel), 8 (05_33: ell voor het log rendement, 1 + R^f bruto), 10 (05_28: CP-gewichten heten omega met een zin over de notatie van Cochrane en Piazzesi; delta was al bezet). Naad 7 (R^f als bruto rendement in 05_26, 05_29 en 05_30): projectkeuze, net als dp_t in 04_20: de toy-secties en hun code gebruiken R^f als bruto grootheid en zeggen dat nu bij de eerste keer expliciet ("kortheidshalve ... 1 + R^f in de notatie van de setup"); 05_33 is wel omgezet. Open voor de herziening van Deel VIII: naad 4 (08_38 r.953-954 noemt carry-getallen die niet in 05_29 of 05_30 staan). Bouwcontrole na Deel V: 99 unieke waarschuwingen tegen 104 vóór Deel V, geen fouten, geen nieuwe klasse.
