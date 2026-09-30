STATUS deel-4 naad open=2

# Naadcontrole Deel IV na de eerste herziening (L18 t/m L25, workflow §12)

Werkwijze: alleen .md, via grep en korte sed-uitsneden (budget 30 aanroepen). Een script controleerde alle 96 verschillende linkdoelen vanuit `04_*.md`: elk doellabel bestaat in een `.md` onder `lectures/` (0 ontbrekend). Alle 117 regels in Deel I–III en V–VIII die naar Deel IV linken zijn op hun doellabel gecontroleerd (0 ontbrekend, ook na het verwijderen van fig-momentum-sim-b, def-risk-management-es, prop-risk-management-horizon enz.). Inhoudelijk gecontroleerd: alle links vanuit Deel IV naar 00-01 en naar Deel I–III (circa 40), alle acht links uit Deel I–III naar Deel IV, tien links uit Deel V–VI naar Deel IV, en de "Wat we al weten"- en "Wat er daarna kwam"-paragrafen van alle acht colleges plus 03_17 -> 04_18 en 04_25 -> 05_26.

## Naadpunten

### Verwijzingen en beweringen over andere colleges

1. **Vereiste risicoaversie in 03_13 verkeerd samengevat.**
   - Plek: `04_23_behavioral.md:322`, "bij gewoon verwacht nut een risicoaversie van vijftien of meer vroeg".
   - Wat: 03_13 noemt $\gamma = 47{,}6$ (`03_13:476`, `:653`), 42 (`:1006`) en 27,2 bij 6% premie (`:716`); "vijftien" komt daar niet voor. `05_27:26` zegt weer "in de dertig". Drie colleges, drie getallen.
   - Oordeel: open.
   - Voorstel: schrijf in 04_23 "een risicoaversie van rond de vijftig vroeg ($\gamma = 47{,}6$)" en laat 05_27 bij de herziening van Deel V hetzelfde getal gebruiken.

2. **"Small en value ook na 1994" als beginfeit van 04_18.**
   - Plek: `03_14_roll.md:1311–1313`, "het overwegen van kleine en goedkope aandelen (small en value) ook na 1994 loonde, het feit waarmee [](#04-18-fama-french) begint".
   - Wat: 04_18 begint met de te vlakke SML na 1963 en de kenmerken van Basu, Banz en Rosenberg (`04_18:24–28`), en laat juist zien dat SMB na publicatie 0,04% per maand is met $t = 0{,}25$ (`04_18:1154`). De koppeling "na 1994" botst dus met de size-helft van het feit.
   - Oordeel: open (Deel III is vast, maar dit is een naadfout).
   - Voorstel: vervang door "dat het overwegen van goedkope aandelen ook na 1994 loonde; waarom kleine en goedkope aandelen meer opleveren dan het CAPM toestaat, is de vraag waarmee [](#04-18-fama-french) begint".

3. **Oefeningslabel als linkdoel vanuit Deel V.**
   - Plek: `05_26_sdf_unificatie.md:949`, "negatieve HML-lading ([](#ex-fama-french-3))".
   - Wat: na de hernummering in 04_18 gaat ex-fama-french-3 nog steeds over winnaars min verliezers en hun lading (`04_18:1292–1300`), dus de inhoud klopt nog. Kaart §3 zegt wel dat `ex-*` geen linkdoel is.
   - Oordeel: open (bij de herziening van Deel V).
   - Voorstel: vervang door "(derde oefening van [](#04-18-fama-french))".

4. **Beweringen die alleen in de uitvoer te controleren zijn.**
   - Plek: `04_18_fama_french.md:25` ("intercept 1,16% per maand", 02_08 noemt in het proza alleen $F = 4{,}20$ op `02_08:514`) en `04_18:411` ("ruim 1,1% per maand", 03_11 noemt op `:1008` alleen "een constante ver boven nul").
   - Oordeel: blijft. De richting klopt; de getallen staan in de tabeluitvoer van 02_08 en 03_11, die buiten deze controle (alleen .md) valt.
   - Voorstel: laat de bouwer bij de volgende build nagaan of de tabellen 1,16 en ruim 1,1 tonen.

5. **Gecontroleerd en in orde.** 04_18:69 (Basu, Stattman/Rosenberg, Banz; `03_16:60–68`), 04_18:281 en 544 (bèta en grootte samen, meetfout in bèta; `02_08:1080`, `:607–675`), 04_19:25 (filterregels; `02_06:589`), 04_20:127–263 ($dp_t$ en de identiteit van 03_15), 04_20:458 (Stambaugh-bias in `fig-merton-icapm-steekproef`), 04_21:73 (0,30; `00_01:965`), 04_21:470 (VRP-figuur bestaat), 04_21:479 (Merton-portefeuille; `03_10:360`), 04_24:24 (Grossman en Stiglitz; `02_06:591`), 04_24:938 (vijftig aandelen via 03_14 uit 02_07, 2002–2026), 04_25:24 (zeven fondsen die overleefden; `02_06:1043–1045`). Inkomend: 01_03:588, 01_04:1211, 02_08:1292, 03_15:553 (decompositie geschat, `04_20:330`), 03_16:101 (De Bondt en Thaler, `04_23:941`), 03_17:1244, 05_26:28–29 en 951–953, 05_26:1231 (`prop-fama-french-mechanisch`), 05_27:28 (78% uit rendementen, `04_20:346`), 05_29:548 en 05_32:205 (haircut $h$ en hefboom $L$ zoals in 04_22:618–657). Openings- en slotparagrafen: alle acht terug- en vooruitwijzingen kloppen met de colleges zoals ze nu zijn, ook 03_17 -> 04_18 en 04_25 -> 05_26; de "driekwart in drie maanden" in 04_22 klopt met 73,8% maart–mei 2009 (`04_19:1013`).
   - Oordeel: opgelost.

### Vaste termen (STYLE §3)

6. **"overlevers" in plaats van "overlevenden".**
   - Plek: `04_24_microstructuur.md:942, 947, 1054`.
   - Wat: kaart §3 noemt "overlevenden" als vaste term; 02_06 en 04_25 gebruiken die vorm. Geen andere verboden vormen in Deel IV ("excess rendement", "equity premium", "value-/equal-weighted", "lecture", "prijst/geprijsd", "term premium", "Itô's lemma", "afdekken", "efficiënte rand": 0 treffers, op één boektitel na op `04_23:1075`). Het motief "de standaardfout van 2%" staat in alle acht colleges met link.
   - Oordeel: open.
   - Voorstel: vervang "overlevers" drie keer door "overlevenden".

7. **SDF onder twee namen en als nieuw begrip.**
   - Plek: `04_23_behavioral.md:791` ("de stochastic discount factor uit 03-12") en `04_25_industrie.md:1098–1100` ("*stochastic discount factor* (SDF, de stochastische factor waarmee alle payoffs worden verdisconteerd)").
   - Wat: de setup en `04_18:338` zeggen "stochastische discontofactor $m$". 04_25 introduceert het begrip alsof het nieuw is, terwijl 03_12, 04_18 (`thm-fama-french-sdf`) en 04_23 het al gebruikten.
   - Oordeel: open.
   - Voorstel: schrijf in 04_23 "de stochastische discontofactor $m$ uit [](#03-12-consumptie-capm)" en in 04_25 "een uitspraak is over één stochastische discontofactor $m$ (SDF)".

### Notatie (kaart §3)

8. **Log rendement als $r_{t+1}$ in 04_23.**
   - Plek: `04_23_behavioral.md:745` ("zodat $r_{t+1}$ het log rendement is"), met gebruik op `:763`, `:773–777`.
   - Wat: kaart §3 en 04_20 (`:128`, `eq-voorspelbaarheid-cs-rendement`) gebruiken $\ell_{t+1}$; 04_23 zegt zelf de notatie van 04_20 te volgen. $dp_t$ spoort wel met 04_20.
   - Oordeel: open.
   - Voorstel: vervang in 04_23:745–777 $r_{t+1}$ door $\ell_{t+1}$ (en $r_{t+1+j}$ door $\ell_{t+1+j}$).

9. **$pd_t$ in 05_27 bij een vergelijking in $dp_t$.**
   - Plek: `05_27_drie_antwoorden.md:670–688`, "Volgens [](#eq-voorspelbaarheid-cs-pv) beweegt $pd_t$ ...".
   - Wat: `eq-voorspelbaarheid-cs-pv` staat in $dp_t = -pd_t$ (`04_20:253`). Voor "beweegt" maakt het teken niet uit, maar 05_27 noemt de relatie nergens. 05_26 en 05_28 gebruiken geen $dp_t$ of $pd_t$.
   - Oordeel: open (bij de herziening van Deel V).
   - Voorstel: schrijf op 05_27:671 "beweegt $pd_t = -dp_t$".

10. **$\gamma$ als precisie in 04_25.**
    - Plek: `04_25_industrie.md:282–286`, "$\gamma = 1/\eta^2$ en $\omega = 1/\sigma^2$ voor de precisies".
    - Wat: in Deel IV is $\gamma$ overal de risicoaversie (04_21:479, 04_23, 03_10, 03_13). $\phi_t$ voor de verwachte vaardigheid botst met $\phi$ als persistentie in 04_20 en 04_23, maar is lokaal gedefinieerd en volgt Berk en Green; 04_18 gebruikt $\rho$, geen $\phi$.
    - Oordeel: $\gamma$ open; $\phi_t$ blijft, projectkeuze (notatie van het origineel).
    - Voorstel: schrijf $\tau_0 = 1/\eta^2$ en $\tau = 1/\sigma^2$ in 04_25:282–286.

### Herhaling

11. **Kerngetallen.** 1,31 (04_19 JT; 05_31 is een andere grootheid, een FF3-alpha), 0,95 (steeds andere grootheden), 6,92 en 0,80 (alleen 03_13), 2469 (alleen 03_11), 12,87 en 1,96 (niet in proza), SMB en HML (04_18:1090–1154, 05_26:954 andere grootheid). De premies 6% (04_23:271), 4,87% in logs en 6,7% rekenkundig over 1926–1990 (04_23:863–864) passen bij 03_13 (6,18 over 1889–1978, 6,92 tot 2024), omdat de periode steeds genoemd wordt. De standaardfout 2,55 (04_23:1148) past bij "ongeveer twee procentpunt over een eeuw" (04_23:813) voor een kortere reeks.
    - Oordeel: opgelost, geen tegenstrijdige getallen.

Open: 1, 2, 3, 6, 7, 8, 9, 10 ($\gamma$). Naad 3 en 9 horen bij de herziening van Deel V.

## Afhandeling (orchestrator, 2026-09-30)

Opgelost in dezelfde commit: naad 1 (04_23: "tientallen" in plaats van "vijftien of meer"), 2 (03_14: value na 1994 loonde; small als vraag van 04_18), 4 (04_24: overlevenden), 5 (04_23 en 04_25: stochastische discontofactor m), 6 (04_23: ell voor het logrendement in het DSSW-blok), 8 (04_25: tau voor de precisie van de prior). Open voor de herziening van Deel V: naad 3 (05_26 linkt naar een oefeningslabel) en 7 (05_27 schrijft pd_t bij een vergelijking in dp_t). Bouwcontrole: twee nieuwe waarschuwingen, beide de bekende exercise/solution-klasse (labels bestaan).
