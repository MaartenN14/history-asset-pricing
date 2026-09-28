STATUS deel-1-3-r9 naad open=0
Naden 1, 2, 3 en 5 opgelost door de orchestrator op 2026-09-29 (L10 oefeningslink, L0 motieflink, overrendement in L11/L12 incl. tabellabels met herhaalde uitvoer, L13 'verklaren'). Naad 4 ('gedetrendeerd') blijft: projectkeuze, als bijvoeglijk naamwoord toegestaan naast 'de trend verwijderen' (oordeel F6 L15).

# Naadcontrole Deel I–III na ronde 9+ (L0 t/m L17)

Werkwijze: alleen .md, via grep en korte sed-uitsneden. Een script controleerde alle cross-refs in `00_00` t/m `03_17`: elk doellabel bestaat (0 ontbrekend). Inhoudelijk gecontroleerd zijn alle links naar 00-00 (15) en 00-01 (37), alle links tussen colleges (circa 60) en de openings- en slotparagrafen van alle achttien colleges. De omzetting rand naar grens (notes/naad-grens.md) is alleen op restanten gecontroleerd.

## Naadpunten

### Verwijzingen

1. **Oefeningslabel als linkdoel.**
   - Plek: `03_10_merton_icapm.md:481`, "(oefening [](#ex-merton-icapm-1))".
   - Wat: kaart §3 zegt dat oefeningslabels geen linkdoel zijn. Dit is de enige `ex-*`-link in Deel I–III.
   - Oordeel: open.
   - Voorstel: vervang de verwijzing door de tekst "(eerste oefening)", zoals in L14 is gedaan.

2. **"De standaardfout van 2%" in de setup zonder link.**
   - Plek: `00_00_setup.md:75`, eerste noemen van het motief. De eerste link naar 00-01 staat pas op `:1024`.
   - Wat: in alle andere zeventien colleges staat de link bij het eerste gebruik of binnen één regel daarna (gecontroleerd per college). Kaart §3 zegt "altijd met link".
   - Oordeel: open.
   - Voorstel: maak op `:75` van "De standaardfout van 2%" de link `[De standaardfout van 2%](#00-01-rendementen)`.

3. **Beweringen over andere colleges.** Steekproef: 00_01:24 (11,6% met SE 1,8 en acht databronnen; klopt met 00_00:39, 323, 47), 00_01:100 (6,18% en 8,3%; klopt met 00_00:93–94), 01_03:1028 (CAPM als eerste getoetste model; klopt met 00_00:116), 01_04:1212 en 03_16:999 (de les van Santa-Clara; klopt met 00_00:121–127), 01_04:23 en 03_12:205 (r beweegt volgens de replicatie van L3; klopt met 01_03:1004–1007), 02_08:150–152 (10%, 14% en 4% bij $R^f$ = 2%; klopt met 01_04:156 en 519), 03_14:139 (A, B, C; klopt met 01_04:1273), 02_05:231 en 787 (6,9% en 9,0%; klopt met 00_01:759 en 841), 03_15:929 (6,92%; klopt met 03_13:877), 03_17:310–312 (PDE en Feynman-Kac in L9).
   - Oordeel: opgelost, geen afwijkingen gevonden.

### Vaste termen (STYLE §3)

4. **"excess rendement" in plaats van "overrendement".**
   - Plek: `03_11_apt_no_arbitrage.md:495, 834, 849, 950`; `03_12_consumptie_capm.md:476, 512, 790, 897, 918, 962, 1074, 1213`, plus de getoonde tabellabels `:914` ("excess rendement") en `:1204–1205`.
   - Wat: STYLE §3 zegt "overrendement". L12 heeft één $R^e$-begrip onder twee namen naast L8 en L14.
   - Oordeel: open.
   - Voorstel: vervang in beide colleges "excess rendement(en)" door "overrendement(en)", ook in de tabellabels die in de uitvoer staan (het label `eq-consumptie-capm-excess` blijft).

5. **"gedetrendeerd" in plaats van "zonder trend".**
   - Plek: `03_15_shiller_excess_volatility.md:322, 326, 356, 468, 591, 673, 779, 819, 912, 963, 966, 1017, 1056, 1092`, plus de figuurtitels `:944` en `:954`.
   - Wat: STYLE §3 geeft voor "detrenden" de vorm "de trend verwijderen". L15 gebruikt het voltooid deelwoord zestien keer. Code en docstrings (`detrend=`) vallen erbuiten.
   - Oordeel: open.
   - Voorstel: schrijf "zonder trend" ("de reeksen zonder trend", "het niveau zonder trend") en "met trend" voor "niet gedetrendeerd"; de code blijft ongewijzigd.

6. **"prijzen" als werkwoord voor waarderen.**
   - Plek: `03_13_equity_premium_puzzle.md:27`: "kon de Euler-vergelijking de T-bill en het aandelenrendement niet tegelijk prijzen".
   - Wat: STYLE §3 sluit "prijzen/prijst" in de betekenis van waarderen uit. Elders in Deel I–III komt de vorm niet meer voor (03_16:469, 559 en 763 gebruiken "correcte prijzen" als zelfstandig naamwoord; dat is goed).
   - Oordeel: open.
   - Voorstel: schrijf "kon de Euler-vergelijking de T-bill en het aandelenrendement niet tegelijk verklaren".

7. **"equity premium puzzle" in lopende tekst van de setup.**
   - Plek: `00_00_setup.md:26, 91`.
   - Wat: de puzzel heet boekbreed zo, als eigennaam (ook 04_23:90, 05_27:41 en de titel van L13). "equity premium" als los begrip staat alleen tussen haakjes (00_01:97) of in een brontitel (03_13:800).
   - Oordeel: blijft, projectkeuze (de naam van de puzzel is een eigennaam).
   - Voorstel: geen wijziging. Cursiveer eventueel bij het eerste gebruik op `:26`.

8. **value-weighted / equal-weighted.**
   - Plek: `00_01_rendementen.md:762–763`, `02_05_crsp_tape.md:136, 306`.
   - Wat: steeds als Engelse term tussen haakjes na "waardegewogen" of "gelijkgewogen". Overige treffers staan in code en docstrings.
   - Oordeel: opgelost, conform STYLE.

9. **Rest van de termenlijst.** Geen treffers in proza voor "term premium" buiten haakjes (03_17:316 staat correct tussen haakjes), "Itô's lemma" of "regel van Itô", "trendcorrectie", "afdekken", en "lecture" in lopende tekst (00_00:819–826 zijn bestandsnamen en commando's). "zich indekken" in 03_10:89, 109, 587, 1002 en 1308 is steeds wederkerend en dus toegestaan.
   - Oordeel: opgelost.

10. **Rand en grens.** Geen "efficiënte rand" meer, en geen "de rand" als alias voor de grens. De overgebleven treffers betekenen iets anders: `02_05_crsp_tape.md:694` ("aan de rand van het" decielbereik) en `03_13_equity_premium_puzzle.md:382` (maximum aan de rand van het parametergebied). "minimum-variantierand" komt voor als eigen begrip (03_14:138).
    - Oordeel: opgelost.

### Openings- en slotparagrafen

11. **Vooruitwijzingen.** Voor alle zeventien overgangen L0→L1 t/m L17→L18 past de slotparagraaf ("Wat er daarna kwam") bij de titel en de opening ("Wat we al weten") van het volgende college. Voorbeelden: 1863 en "37 jaar vóór Bachelier" (00_01:999 en 01_02:23), Merton "vanaf 1969" (02_09:1158 en 03_10:23), "zeven jaar later" Fama-French 1992 na Rosenberg 1985 (03_16:1003), en L17 sluit correct aan op 04_18. L8 (02_08:1157) wijst behalve naar L9 ook vooruit naar L14; dat is één toegestane extra vooruitwijzing.
    - Oordeel: opgelost.

12. **`$R^f$` bruto in L6.**
    - Plek: `02_06_efficiente_markten.md:131–133`.
    - Wat: wijkt af van de setup-notatie (netto), maar wordt met een zin en een link naar 00-00 aangekondigd.
    - Oordeel: blijft, projectkeuze.

### Herhaling van kerngetallen

13. **6,92 / 6,18 / 0,80 / 1,96 / 9,0% / 12,87 / 2469.** 6,18 (00_00, 00_01, 03_13) en 9,0% (00_01, 02_05) zijn overal hetzelfde getal voor hetzelfde feit. 6,22 in 03_13:1101 is de eigen replicatie en wordt als zodanig benoemd, naast 6,18. 0,80 is in L13 de reële rente, in L1, L3, L4 en L16 een ander getal zonder verband. 1,96 is overal de kritieke waarde. 12,87 komt niet voor. 2469 staat alleen in L11.
    - Oordeel: opgelost, geen tegenstrijdige getallen.
