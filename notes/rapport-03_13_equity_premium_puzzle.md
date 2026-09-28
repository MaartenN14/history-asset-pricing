STATUS 03_13_equity_premium_puzzle F6b words=5354 prose=PASS open=0 cijfer=- min=-

# Rapport 03_13_equity_premium_puzzle (workflow-herziening)

## F0

**Nulmeting.** `words 4896  sent_mean 20.6  sent_p90 35  sent_gt40 12  para_mean 61  dash 33  semicol 33  motief 3  u_form 0  je_form 5  taboo 0  stopw 5  calque 3  engquote 25`. `--where`: r. 914 "in de taal van", r. 968 "Noteer", "epistemisch". Lengte is niet het probleem; zinnen, streepjes, puntkomma's en vooral 25 Engelse citaten wel.

**Vijf grootste problemen.**
1. *Taal*, overal: zinnen van gemiddeld 20,6 woorden, 12 boven 40, alinea's van 61, 33 streepjes, 33 puntkomma's, vijf keer "je". Zwaarst in *Theorie* (r. 294–304, 492–510), *Simulatie* (r. 653–663) en *Replicatie* (r. 906–923).
2. *Engelse citaten midden in de zin* (25): Santa-Clara r. 59, MP r. 300, Weil r. 504, Kocherlakota r. 509 en 662, HJ r. 372 en 920, Campbell/Siegel-Thaler r. 934–960, MP r. 970.
3. *Structuur*: imports-cel in *Overzicht* (r. 72); Overzicht zonder vraag-antwoord en lijst; geen routekaart, geen *Samengevat*; bewijzen van zes regels en langer open (r. 280, 358, 424); twee simulaties, waarvan de toelaatbare regio een numerieke oplossing van het model is (hoort in *Theorie*, §11.7).
4. *Toy-voorbeeld* niet in vijf minuten na te rekenen: 2×2-stelsel met zes decimalen, determinant 0,03, twee waarden van $\gamma$ (r. 151–192), print-regel in plaats van tabel hand/code (r. 235).
5. *Notatie en jargon*: $R^f$ bruto (setup: netto), $x_{t+1}$ voor groei (setup: payoff), $\log R$ zonder $\ell$; "2%-motief" r. 654 en 1071, "epistemisch" r. 52 en 968; replicatieblok ≈ 360 woorden; getallen in proza zonder tabel origineel/hier en zonder "Geslaagd" (r. 755–762, 906–916); oefening 1 is geen instap, geen "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `03-13-equity-premium-puzzle` (12 lectures), `thm-equity-premium-puzzle-frontier` (05_26), `eq-equity-premium-puzzle-eis` (05_27), `eq-equity-premium-puzzle-hj` (05_27, 05_30), `eq-equity-premium-puzzle-lognormaal` (05_27). Inhoudelijk: "$\gamma = 15$ bij een rente van dertig procent" (05_26 r. 1031). Niet aangehaald: `prf-...-mp`, `eq-...-pd`, `eq-...-frontier`, alle `fig-`, `cel-` en `ex-`labels.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | Santa-Clara-citaat, beschrijving toy/theorie/simulatie in proza | 110 | wordt de lijst; citaat geparafraseerd |
| Intuïtie | Mehra-anekdote "six more years" | 60 | anekdote, geen mechanisme |
| Intuïtie | Fischer Black, curvatuur 55 | 60 | nevenzaak; de $\gamma$ in de dertig/veertig staat in Theorie |
| Toy | Cramer met zes decimalen, $\gamma = 10$ | 250 | niet handrekenbaar; wordt iid-toy, $\gamma = 10$ naar Theorie |
| Theorie | MP-citaat p. 156, vier toestanden 0,39% | 60 | citaat; nevenresultaat |
| Theorie | Campbell 20,9/10,4/246,6/47,6 in proza | 70 | naar replicatietabel (alleen 20,9/10,4) |
| Theorie | HJ figuur 1-zin, positiviteitsrestrictie | 70 | detail; één bijzin in het replicatieblok |
| Theorie | citaten Weil en Kocherlakota | 70 | parafrase in één zin |
| Simulatie | Kocherlakota "for all values of α ≤ 8,5" | 40 | citaat; dubbelt de conclusie |
| Replicatie | blok van 360 naar 230 woorden; Mehra 2003 6,9/8,0/7,8 | 170 | blok > 250; getallen uit geen cel |
| Replicatie | HJ-proza (twee alinea's) naar tabel en oordeel | 120 | getallenbrij |
| Wat er brak | Campbell 2003, Siegel-Thaler-citaten; epistemische slotalinea | 190 | citaten; slotalinea naar *theorie of feit* in Overzicht |
| Oefeningen | ex-3 (ramp in de keten) | 200 | vierde oefening; plaats nodig voor instap |
| **totaal** | | **≈ 1.470** | |

**Verwachte lengte.** 4.896 − 1.470 ≈ 3.430; erbij komen vraag-antwoord en lijst, routekaart, *Samengevat*, lees-zinnen, zinnen rond cellen, drie oordelen onder tabellen, een instapoefening en "Wat dit leert" (≈ 1.100). Verwacht 4.500 tot 4.900. Geen splitsing.

## F1

**Eindmeting.** `words 4786  sent_mean 15.2  sent_p90 24  sent_gt40 0  para_mean 43  dash 0  semicol 15  motief 0  je_form 0  stopw 1  calque 0  engquote 2` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings in de uitvoer.

**Geschrapt of verplaatst.** Mehra-anekdote en Fischer Black (anekdote/nevenzaak); Santa-Clara, MP p. 156/158, Weil, Kocherlakota (2×), HJ, Campbell, Siegel-Thaler: Engelse citaten geparafraseerd of geschrapt; vier toestanden 0,39% (nevenresultaat); Campbell 246,6/47,6 (niet nodig, 20,9/10,4 staan nu in de replicatietabel); Mehra 2003 6,9/8,0/7,8 (uit geen cel); epistemische slotalinea (wordt *theorie of feit* in Overzicht); oud ex-3 (ramp in de keten, en daarmee `Barro2006` en een vooruitverwijzing) geschrapt voor de instap. Toelaatbare regio van *Simulatie* naar *Theorie* (numerieke oplossing, §11.7). Replicatieblok van ≈ 360 naar 184 woorden.

**Toegevoegd.** Vraag-antwoord en lijst; H12-voorspelling aan eind van *Intuïtie*; nieuw toy: iid-economie met twee toestanden (MP-kalibratie, $\phi = \tfrac12$, $\gamma = 2$): vijf stappen, één cel, tabel hand/code, premie 0,26 pp, controle via covariantie; nieuwe `eq-equity-premium-puzzle-cov` als eerste afleiding (recept van het toy); routekaart, lees-zin bij elke vergelijking, *Samengevat*; toy-getallen terug in theorie (0,9589, 0,25 vs 0,26) en simulatie ($\delta = 3{,}57$); oordelen "Geslaagd" onder drie replicatietabellen; Campbell-rij in de consumptietabel; instapoefening ($\delta = 0{,}072$, premie ×3,97); "Wat dit leert" bij elke uitwerking.

**Notatie.** $R^f$ netto overal ($1 + R^f$ bruto, $\log(1+R^f)$), groei $g$ in plaats van $x$ (payoff), $\ell = \log R$ aangekondigd, $\mu_c, \sigma_c$ met één zin vertaald naar $\mu, \sigma$ van L12; "hefboom één" zonder het symbool $\phi$ van L12, omdat $\phi$ hier de overgangskans is. Standaardfout van 2% wijst naar `#00-01-rendementen`.

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- oude cel 2 (MP-keten, $\gamma = 2, 10$) → nieuwe toy-cel (iid, tabel hand/code) + functiecel + keten-tabel; waarden PD 36,9916/36,6706, E[R] 1,0458/1,1579, premie 0,2869/2,6886 identiek; rente nu netto in % (4,2973/13,1043 = 1,043/1,131 bruto).
- oude cel 3 (SDF-momenten): identiek, rente in % en kolom Sharpe 0,3707 (was print 0,371).
- Weil-cel: variabelen hernoemd, uitvoer identiek.
- rooster: print → Series, 0,362 / 2,419 / 0,999 / 3,990 / 99,9% identiek.
- simulatie, Tabel 1, consumptie, HJ, bootstrap: identiek (kolomnamen Nederlands; Campbell-rij 20,9/10,4 toegevoegd; HJ-cel in data- en grenscel gesplitst). `rng`-volgorde behouden.
- mes-oefening identiek (kolom "rente (%)"); nieuw: instap (0,0312 / 0,9774 / 0,0104 / 3,9701); rampcel verdwenen.

**Afvinklijst §11.9, wat niet voldoet.** Na de imports-cel volgt direct de opzet (zoals in de template). Theorie heeft vijf `###`-delen met een tweede *Waarom* voor de frontier binnen het HJ-deel. Overige: ok.

**Labels.** Alle labels van HEAD bestaan nog; nieuw `eq-equity-premium-puzzle-cov`. `ex-...-1/2/3` hebben andere inhoud (instap, mes, bootstrap); nergens anders aangehaald.

**Open punten.**
1. "Het verschil van een honderdste procentpunt" (0,362 tegen 0,35): oorzaak niet vastgesteld, de tekst claimt er ook geen.
2. Campbell 20,9/10,4, Kocherlakota 0,00219/0,0274/0,00127, Mehra 2003 p. 13–15 en tabel 4: uit de vorige tekst, F2 moet ze tegen de bron houden.
3. De 8,3% van setup "uit maandrendementen sinds 1926": gecontroleerd tegen L1 r. 96, niet tegen de setup-cel.

## F4

**Meting.** `words 4914  sent_mean 15.1  sent_p90 24  sent_gt40 0  para_mean 43  dash 0  semicol 14  stopw 1  engquote 2` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings. De labelset is gelijk aan die van F1.

**Feitenlijst (1 onjuist, 1 onzeker): opgelost.**
- Rij 12, Kocherlakota: de tekst zegt nu dat 0,37 de correlatie met het *totale* aandelenrendement is. Met het excess rendement is het ongeveer 0,33, en 0,37 is de voorzichtige keuze (een lagere correlatie geeft een hogere $\hat\gamma$). De simulatie is ongewijzigd, dus alle aangehaalde getallen zijn gelijk.
- Rij 18, Campbell 20,9/10,4: niet te verifiëren, dus de Campbell-rij is uit de consumptietabel en "dezelfde orde als Campbell" uit het oordeel. De methode (RRA(1)/RRA(2), `Campbell1999`) blijft staan.

**Lezerspunten.**
- *Opgelost (13).* 1: Sharpe-ratio benoemd in Intuïtie, met 16,67 als std van de premie. 2: in de propositie staat alleen PD, rendement en rente volgen ongenummerd. In de frontier staat alleen de variantiegrens, $m^*_v$ in de lees-zin (de labels blijven). 3: de zin met twee keer "haat" is herschreven. 4: het geleende resultaat van L12 in één zin herhaald. 5: 6,22 als eigen replicatie, naast 6,18. 6: zin over $\gamma = 25$ (0,71, 9,6%). 7: lees-zin rendement verbeterd. 8: overgangszin naar meerdere activa. 9: rol van $\beta$ voor de grenzen met T-bill. 10: $\mathbf{1}$ gedefinieerd. 12: "vrijwel de $\delta = 3{,}6$". 13: bijzin bij de $g^{-1}$/$g^{-2}$-kolommen. 15: "figuur 4 van hun paper".
- *Afgewezen (2).* 11: het timingvoorbeeld van Shiller kost woorden en draagt de vraag niet. 14: de overgangsmatrix staat al in de code direct na de propositie.

**Navertel-toets.** Het lezerbestand bevat geen navertelsectie, alleen de vijftien punten. Er is dus geen afwijkende sectie te melden.

**`nb_outputs`-diff tegen F1.** Alleen de consumptietabel is veranderd: de Campbell-rij is weg, de overige waarden zijn identiek.

**Betaald met schrappen.** Geschrapt: "De functie werkt ook voor een heel rooster" en "weinig veeleisend … robuust" (Wat er brak), samen ≈ 30 woorden, plus de Campbell-vergelijking. Netto +128 woorden, ruim onder 5.500.

## F5-1

**Meting.** `words 5234  sent_mean 15.0  sent_p90 23  sent_gt40 0  para_mean 45  semicol 8  stopw 1  engquote 1` → PASS. Sync en uitvoeren met `HAP_OFFLINE=1` zonder fouten of warnings. De rastercel duurt nu ongeveer 33 s (eerst gemeten 54 s; $\pi$ wordt daarom één keer berekend). Aangehaalde getallen in de `nb_outputs`-diff: alle gelijk.

**Feitelijke fouten, alle gedaan.**
1. Bijschrift: "nergens boven 0,36 procentpunt"; onderkant 2,66 "ruim een factor zeven" in plaats van "orde van grootte".
2. Simulatie: de tabel heeft nu de kolommen relatieve spreiding van premie en covariantie (0,292/0,307 bij 6%, 0,581/0,309 bij 3%). De tekst zegt: bij 6% beide ongeveer 30%, bij 3% domineert het gemiddelde.
3. HJ: "de curve keert rond $\gamma = 25$ om", de rente is het hoogst tussen 20 en 30 (ongeveer 35%).
4. "Nog groter" vervangen: een aandeel is volatieler dan consumptie, de simulatie rekent uit welke kant wint.

**Drie verbeteringen.**
- *$\gamma$ recht gezet.* De simulatie zegt nu dat zij premie/cov schat met een echt aandeel: 4,7 keer zo volatiel, cov 0,0022 > 0,00125, ware $\gamma$ 27,2 en niet 47,6. Een brugtabel koppelt 47,6 / 27,2 / 22,0 / 15 / 42 / ≈ 75 (L12, GMM 1959–1978) aan hun maatstaf. De symboolbotsing is weg: $\phi$ heet nu $P_{ij}$, met een zin over de hefboom $\phi$ in L12. $\delta$ staat overal als 0,036 (3,6%). $\lim_{k\to\infty}\mathbf{A}^k$.
- *Replicatie.* Het consumptie-oordeel is nu "Gedeeltelijk geslaagd", met sd 2,58 tegen 3,57 en autocorrelatie +0,49 tegen −0,14. Het blok noemt RRA onder "Wat" en geeft er een verwachting voor. Bij de HJ-grens staat een tabel origineel/verwacht tegen hier (Sharpe 0,37/0,43; drempels 15/42/43), met de zin dat HJ zelf geen drempel rapporteren.
- *Code.* `mp_economy` werkt nu per $(\gamma,\beta)$ met een zichtbare lus voor $R_{ij}$; het rooster is een lus eromheen; `stationary` en de zin over $\pi$ staan erbij. In de tekst staan de wortelformule ($\beta = 1$ invullen) en $13{,}8 = \mu_c/\sigma_c^2$ (maximum van de benodigde $\beta$). Oefening 3 wordt als float afgerond. Kolomnamen staan voluit (Mehra-Prescott, standaarddeviatie, grens markt en T-bill, …), en `[::13]` heeft commentaar.

**Overige aanmerkingen, gedaan.**
- Warning met $N/T = 25/96 = 0{,}26$ tegen $0{,}43^2 = 0{,}18$.
- "Mes" vervangen door "op het scherp van de snede", met de verklaring bij eerste gebruik (ook in de titel en vraag van oefening 2).
- Santa-Clara-zin geschrapt (onduidelijke $\gamma$).
- De risicovrije-rentepuzzel staat bij het rooster nu als verwijzing naar de laatste subsectie.
- Puntkomma's gesplitst (blok twee keer, bijschrift HJ, Wat er daarna kwam, "47,6 nodig").
- "consumptie-CAPM"; stelling "Hansen-Jagannathan-grens met meerdere activa", en "grens" ook in de tekst.
- "beleggers met verliesaversie".
- Oefening 2 (2): de afleiding is genoemd.
- Toy-opzettabel: rij met $\beta$ en $\gamma$.

**Afgewezen.** Geen.

**Lengte.** Netto +320 woorden (brugtabelzinnen, HJ-tabel, oordelen, wortelformule), onder 5.500. Geschrapt: de Santa-Clara-zin.

## F5-2

De tabel met de maatstaven voor $\gamma$ staat nu aan het eind van *Theorie*, vlak vóór *Samengevat*, met één inleidende zin. In de *Simulatie* verwijst één brugzin ernaar terug. `prose_stats` geeft PASS (5268 woorden). Sync en uitvoeren met `HAP_OFFLINE=1` foutloos, `nb_outputs` identiek aan F5-1.

## F6-1

**Meting.** `words 5354 … semicol 8 stopw 1 engquote 1` → PASS. Sync en uitvoeren met `HAP_OFFLINE=1` zonder fouten of warnings. `nb_outputs` identiek aan F5-2; alleen de tekst is veranderd.

**Feitelijke fout (naadpunt 1), gedaan.** De rij met 75 heet nu "premie alleen: gewogen excess rendement nul".

**Drie verbeteringen, gedaan.**
1. De γ-tabel staat nu aan het eind van de replicatie, onder "### Alle maatstaven voor de vereiste risicoaversie", en haalt dus geen getallen vooruit. De brugzin in de Simulatie verwijst ernaar.
2. Replicatieblok: elk onderdeel heeft hoogstens twee zinnen. De verwachte afwijking voorspelt nu voor consumptie dat de momenten afwijken én dat de risicoaversie boven tien ligt. Het oordeel is daarom "Geslaagd", met beide delen getoetst.
3. Tweede HJ-grens: $v$ uitgelegd als de prijs van een zekere euro, met één getal. Bij $v = 1/(1+R^f)$ valt de grens samen met de Sharpe-grens: $0{,}37/1{,}008 = 0{,}37$.

**Overig uit het eindbestand.** Samengevat zegt nu "net boven $\gamma = 10$". De warning legt $N/T$ in één bijzin uit.

**Naadpunten.**
- 2: $m$ heet overal "stochastische discontofactor" (25×, ook in Waar we zijn en in toy stap 1), $\beta$ heet "subjectieve discontofactor".
- 3: de bewering over de reeksconventie is geschrapt. Nu: "om ze te onderscheiden van de momenten van rendementen in deze lecture".
- 4: bijzin toegevoegd dat L12 met 1,8% en 3,5% op 14,7 uitkomt, en dat het verschil de kalibratie is.
- 7, 10, 11: niet gewijzigd, volgens de opdracht.

**Lengte.** Netto +86 woorden, onder 5.500.
