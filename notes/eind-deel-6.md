STATUS deel-6 naad open=3

# Naadcontrole Deel VI na de eerste herziening (L34 t/m L36, workflow §12)

Werkwijze: alleen .md, via grep en korte sed-uitsneden (budget 25 aanroepen). Een script controleerde alle 87 linkregels (50 verschillende doelen, ook `{prf:ref}`) vanuit `06_*.md`: elk doellabel bestaat (0 ontbrekend), en geen enkele link gaat naar een `ex-*`-label. Alle 21 regels vanuit Deel VI naar 00_01 en Deel I–V zijn inhoudelijk nagelopen op de doelplek: 03_16:543–545 (gezocht kenmerk, grote $t$ in de steekproef en daarbuiten geen), 04_25:551–557 (`thm-industrie-bh` veronderstelt onafhankelijke p-waarden), 04_25:84–87 (ICI2020, indexfondsen eind 2019 evenveel als actieve fondsen), 04_20:40/63 (buiten de steekproef zelden beter dan het historische gemiddelde), 05_26 (`prop-sdf-unificatie-b-lambda`), 05_33 (equivalentie, risico of vergissing), 01_03 (DDM; *clean surplus* wordt in 06_34 terecht aan Fama-French toegeschreven), 02_07 (de 50 aandelen van de splitsingenstudie, 02_07:625/851). Alle 23 regels in de rest van het boek die naar Deel VI linken, verwijzen naar een bestaand label; naar de verwijderde cellen en figuren (cel-/fig-factor-zoo-eb, cel-/fig-machine-learning-sim-kmz) verwijst niets meer. De oefeningverwijzingen in de tekst kloppen met de nieuwe nummering (06_34:377 → oefening 2, :425/:1048 → oefening 3; 06_35:304 → 3, :687 → 4; 06_36:868 → 3).

## Naadpunten

### Verwijzingen en beweringen over andere colleges

1. **Linkdoelen, oefeningslabels en hernummering.**
   - Plek: alle `06_*.md`; inkomend 03_16:545, 04_24:1232, 05_33:438/1035, 07_37:24/27/423/620, 08_38:676/953/1110, 08_39:247/575/617/627/696/717/724/732/1111–1114.
   - Wat: 0 ontbrekende doelen, 0 `ex-*`-links. Getallen die andere colleges aan Deel VI toeschrijven, staan er: 0,69% per maand (06_34:819), vijf dollar (06_36:31/95), 7,3 met $t = 2{,}8$ (06_36:863), multiplier tussen 2 en 8 (06_36:738/984), 7,4% in de jaren negentig en de Russell-herindeling (06_36:892–893), McLean-Pontiff (06_34:56/417).
   - Oordeel: opgelost.

2. **Beweringen in 08_39 die 06_36 niet draagt.**
   - Plek: `08_39_wat_we_niet_weten.md:717` ("In [](#06-36-inelastische-markten) daalde ook de marktvolatiliteit in 2010–2019 terwijl passief groeide") en `:696` (informatiewaarde van prijzen met BenDavidFranzoniMoussawi2018).
   - Wat: 06_36 noemt nergens een dalende marktvolatiliteit in 2010–2019 (grep op 2010/2019/daalde) en citeert Ben-David, Franzoni en Moussawi niet; 06_36:1003 stelt alleen de vraag wie prijzen nog informatief maakt.
   - Oordeel: open (bij de herziening van Deel VIII).
   - Voorstel: laat 08_39:717 alleen het verdwijnende inclusie-effect (06_36:892, :970) aan 06_36 toeschrijven en de volatiliteitsbewering zelf staven of schrappen, en zet bij :696 de link achter de vraag, niet achter het citaat.

3. **Low-beta $t = 1{,}35$ in de tabel van 08_38.**
   - Plek: `08_38_wat_we_weten.md:953`.
   - Wat: de rij linkt naar [](#06-34-factor-zoo) en [](#02-08-capm), maar geen van beide bevat low-beta of $t = 1{,}35$ (grep). Dit hoort bij naad 4 van `eind-deel-5.md` (carry $t = 3{,}0$).
   - Oordeel: open (bij de herziening van Deel VIII).
   - Voorstel: herleid het getal naar de plek in het proza of haal 06_34 uit de bronkolom van die rij.

4. **Overgang 06_36 → 07_37.**
   - Plek: `07_37_llms_en_efficientie.md:24–27` en `:423`.
   - Wat: 06_36 sluit (`:995–1006`) af met een open vraag, een multiplier die ergens tussen 2 en 8 ligt, een niet-causale OLS-helling en de puzzel van het verdwijnende inclusie-effect; 07_37:24–26 vat dat samen als "liet zien dat het geaggregeerde aandelenniveau wordt gezet door geldstromen … niet door een arbitrageur". Beide plekken schrijven bovendien "lecture" (STYLE §3: college). De vooruitwijzing 06_36:1003–1006 (Santa-Clara over machines en het geaggregeerde niveau) past wel bij het citaat op 07_37:418–421, en 07_37:27 ("machine learning … zonder te zeggen waarom") past bij 06_36:23.
   - Oordeel: open (bij de herziening van Deel VII).
   - Voorstel: schrijf op 07_37:24 "Het vorige college ([](#06-36-inelastische-markten)) maakte aannemelijk dat geldstromen op een inelastische vraag het niveau van de markt mede zetten, met een multiplier die de data tussen 2 en 8 laten" en vervang "lecture" op :24 en :423 door "college".

5. **Overige Waar-we-zijn- en slotparagrafen.**
   - Plek: 05_33:1033–1035 → 06_34:24–28; 06_34:1162–1164 → 06_35:24–28; 06_35:1181–1182 → 06_36:23.
   - Wat: elke vooruitwijzing en terugverwijzing klopt met wat het doelcollege nu doet (factor zoo van honderden kenmerken; machines die ruisige signalen combineren; wie koopt en hoe prijsgevoelig).
   - Oordeel: opgelost.

### Vaste termen (STYLE §3)

6. **Verboden vormen.**
   - Plek: alle `06_*.md`.
   - Wat: 0 treffers op "excess rendement", "equity premium", "value-/equal-weighted", "lecture ", "prijst/geprijsd/beprijs", "term premium", "Itô's lemma", "afdek", "efficiënte rand", "stochastic discount factor", "overlevers", "alfa". De SDF heet overal "stochastische discontofactor" (06_34:526, 06_35:45, 06_36:37 met $m$).
   - Oordeel: opgelost.

7. **"Karakteristieken" in 06_35 tussen "kenmerken" in 06_34 en 06_36.**
   - Plek: `06_35_machine_learning.md:37`, `:51`, … (37 keer), o.a. `:1155` ("Honderden karakteristieken, in [](#06-34-factor-zoo) nog …"); 06_34 (3×) en 06_36 (5×) schrijven "kenmerk", net als 05_30/05_31 en 05_33:1034.
   - Wat: elk college is intern consistent, maar de lezer krijgt in drie opeenvolgende colleges voor hetzelfde begrip afwisselend twee woorden, en 06_35:1155 verwijst met het andere woord terug naar 06_34. Buiten 06_35 komt "karakteristiek" alleen nog in 04_18 (3×) en 08_39 (2×) voor.
   - Oordeel: open.
   - Voorstel: vervang in 06_35 "karakteristiek(en)" door "kenmerk(en)" (en "karakteristiekfactoren" op :459 door "kenmerkfactoren"), zodat Deel V–VI één term houden.

### Notatie (kaart §3)

8. **$R^f$, bruto, $\ell$, niveaus.**
   - Plek: 06_36:333–349 ($R^f$ netto, $1+R^f$ als brutovoet), 06_36:337 ($R_{t+1}$ bruto), 06_34:532 ($R_{t+1}$ "bruto rendement"), 06_36:501 ("Vanaf hier is $\ell_{t+1}$ het log rendement"), 06_36:241 (kleine letters als procentuele veranderingen, aangekondigd).
   - Oordeel: opgelost.

9. **Symbolen met twee betekenissen.**
   - Plek: $\kappa$ = Campbell-Shiller-constante (04_20:142), aanpassingskosten (06_34:559), priorschaal/verwachte maximale Sharpe-ratio (06_35:422, $\kappa = 0{,}133$ op :1039); $M$ = aantal toetsen (04_25:546, 06_34:259) en multiplier $M = 1/\zeta$ (06_36:48); $\lambda$ = factorpremie (05_26:205), inverse Mills-ratio (06_34:344) en ridge-straf (06_35:303); $\gamma$ = absolute risicoaversie bij CARA (06_36:333) tegenover relatieve elders.
   - Wat: elk symbool wordt ter plekke gedefinieerd; $\zeta$ en $M$ als multiplier komen in Deel V niet voor, dus geen botsing met Deel V. $\phi$ als AR(1)-persistentie in 06_36:504 sluit aan bij 04_20. 06_34:595 linkt naar `prop-sdf-unificatie-b-lambda` zonder $\lambda$ zelf te gebruiken, dus geen botsing met de Mills-ratio.
   - Oordeel: blijft, projectkeuze (lokaal gedefinieerde symbolen; "absolute" staat bij $\gamma$ expliciet).

### Herhaling en getallen

10. **Kerngetallen over colleges heen.**
    - Plek: 06_34:56/328/611/1122/1278 ($t$ boven 3 als afronding van 2,8; Bonferroni 3,78 bij 316), 06_34:55/232/324 (316), :58/:1121 (452), 06_34:1117 (26% origineel tegenover 40% hier, gelabeld), 06_35:366/:369/:1157 (NN3 0,40% per maand), 06_36:31/95 en 07_37:423 en 08_39:575 (vijf dollar), 03_16:722 ($t > 3$ in 13,8% van de gezochte gevallen, simulatie, geen tegenspraak).
    - Oordeel: opgelost (geen zelfde feit met een ander getal).

11. **Twee keer 0,40 met verschillende eenheid in 06_35.**
    - Plek: `06_35_machine_learning.md:1134` (cs-$R^2$ 0,40 als fractie) tegenover `:366`, `:369`, `:1157` ($R^2_{OOS}$ van GKX 0,40% per maand).
    - Wat: hetzelfde getal voor twee verschillende maatstaven in één college, eenmaal als fractie en eenmaal in procenten; een lezer die bij :1157 de slotsom leest, kan de tabel van :1134 voor dezelfde grootheid houden.
    - Oordeel: open.
    - Voorstel: schrijf in de tabel op :1134–1136 de cs-$R^2$ in procenten (40%, $-17\,000$%, 26%) of zet "(fractie)" in de kolomkop.

12. **Het citaat van Santa-Clara en de parafrases van SantaClara2026.**
    - Plek: `06_34_factor_zoo.md:1157–1160`; ook 00_00:127, 07_37:1177, 08_38:56, 08_39:1149.
    - Wat: de parafrases spreken elkaar niet tegen (06_34:61 open vraag waarom anomalieën verzwakken; 06_35:93–96 na publicatie, op schaal, na kosten; 06_35:1178 en 06_34:1156 "vermeend inzicht"; 06_36:64 wat de markt beweegt als open vraag; 06_36:1003–1005 en het citaat in 07_37:418–421; 04_25:1091 en 05_31:1159–1160). Maar 06_34 brengt het motto uit [](#00-00-setup) opnieuw volledig, ingeleid als nieuw ("Santa-Clara vat het verschil vanuit de praktijk samen"), en daarna herhalen 07_37, 08_38 en 08_39 het nog drie keer volledig.
    - Oordeel: open.
    - Voorstel: schrijf op 06_34:1157 "Dat is de praktijkles van Santa-Clara uit [](#00-00-setup)" en laat de herziening van Deel VII–VIII het volledige citaat nog hoogstens één keer (in 08_38 of 08_39) herhalen.

## Samenvatting

Open: 6 (naden 2, 3, 4, 7, 11, 12), waarvan 2 bij Deel VIII, 1 bij Deel VII en 3 binnen Deel VI. Blijft, projectkeuze: 1 (naad 9). Opgelost: 5.

## Afhandeling (orchestrator, 2026-09-30)

Opgelost in dezelfde commit: naad 7 (06_35: "karakteristiek(en)" is in het proza overal "kenmerk(en)" geworden, 37 plekken; de twee aslabels in de code blijven, omdat de figuur anders opnieuw moet draaien), naad 11 (06_35: de kolomkop van de KNS-tabel zegt nu "$R^2$ als fractie"), naad 12 (06_34: het citaat wordt aangekondigd als het motto uit [](#00-00-setup); de herhalingen in 07_37, 08_38 en 08_39 gaan mee in de herziening van Deel VII en VIII). Woorden: 06_34 5.999, 06_35 5.961, beide PASS; code en uitvoer ongewijzigd.

Open voor Deel VII en VIII (gaan als naadnotitie mee in de lopende herziening): naad 2 (08_39:717/:696), naad 3 (08_38:953), naad 4 (07_37:24–26, :423).
