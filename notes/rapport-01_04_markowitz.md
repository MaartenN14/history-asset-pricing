STATUS 01_04_markowitz F6b words=5387 prose=PASS open=1 cijfer=- min=-

# Rapport 01_04_markowitz (workflow-herziening)

## F0

**Nulmeting.** `01_04_markowitz.md  words 7510  sent_mean 14.7  sent_p90 24  sent_gt40 0  para_mean 45  dash 0  semicol 13  motief 0  Lnum 0  deel 0  u_form 0  je_form 0  taboo 0  stopw 1  calque 0  engquote 0`. `--where`: geen treffers. Enige overschrijding: words (7510 > 5500).

Woorden per sectie (prose_stats-telling): top 87, Overzicht 301, Intuïtie 638, Toy 303, Theorie-intro 86, Opzet 325, Kernresultaat 1128, Risicovrij activum 1052, Wat het voorspelt 303, Hoe toegepast 582, Simulatie 449, Replicatie 926, Wat er brak 360, Oefeningen 970.

**Vijf grootste problemen.**
1. Lengte 7510 woorden; de zwaarste blokken zijn *Het kernresultaat* (r. 333–571), *Een risicovrij activum* (r. 573–811, drie dropdown-notes), *Oefeningen* (r. 1435–1698) en *Replicatie* (r. 1120–1393).
2. *Replicatie*, r. 1139–1144 en 1281–1295: de tekst beschrijft DGU's Industry-dataset, de tabel toont hun S&P-sectoren; "geen verschil groter dan twee SE" klopt niet; "ver boven 1/N" klopt niet voor de industrieën (feiten 2–4).
3. *Intuïtie*, r. 99–145: geschiedenis (bibliotheek, Friedman, Roys oorlogsverleden, Tobin) en mechanisme door elkaar; de voorspellingen komen pas op r. 147.
4. *Theorie*, r. 409–442 e.v.: $A,B,C$ zijn zowel activa als scalars; ook $d$ naast $D$ en $\delta$, $a$ (dosis) naast $a_i$ (intercept) (feit 12).
5. Onherleidbare of foute beweringen: 14 pagina's en vier grafieken (r. 57), Roy in de oorlog (r. 126), Sharpe noemde de ratio (r. 591), marktsharpe 0,4 (r. 660), Hansen-Jagannathan-note (r. 635), "maximum-Sharpefondsen niet" (r. 1302), Bayes-Stein (r. 1384), Santa-Clara-parafrase (r. 1425) (feiten 5–9, 13, 15–17). Daarnaast code: einsum drie keer, rollende lus dubbel, `tail(3)`-cel zonder functie.

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `01-04-markowitz` (tien lectures), `eq-markowitz-foc` (02_08, 03_14), `eq-markowitz-tangent` (02_08, 05_26), `eq-markowitz-abcd` en `eq-markowitz-probleem` (03_14), `thm-markowitz-tweefonds`, `cor-markowitz-separatie`, `ex-markowitz-1` (02_08). Niet aangehaald: `eq-markowitz-1n/-frontier/-roy/-sharpe`, alle `fig-`/`cel-`, `ex-markowitz-instap/-2/-3`. 02_08 gebruikt de activa A, B, C (zelfde toy) en 03_14 de scalars $A,B,C,D$; beide namen blijven dus.

**Schraplijst (schraptoets STYLE §11.11; eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | pagina's/grafieken, dubbele theorie-of-feit-uitleg | 60 | detail, deels onherleidbaar |
| Intuïtie | bibliotheek-alinea (naar één zin in Overzicht) | 55 | geschiedenis, geen mechanisme |
| Intuïtie | note Friedman bij de promotie | 110 | anekdote, niet nodig voor de vraag |
| Intuïtie | Roys oorlogsverleden, Roy/Tobin ingekort | 120 | onherleidbaar; Theorie doet Roy en Tobin |
| Opzet | note Notatie van Markowitz; bruto/netto-uitweiding; derde lezing ingekort | 110 | nevenzaak |
| Kernresultaat | metazin, bèta-vorm-alinea, inefficiënte tak, note "Waarom $D$ positief is", praktisch/theoretisch-alinea's ingekort | 300 | nevenresultaten; CAPM citeert alleen de vergelijking |
| Risicovrij activum | notes Hansen-Jagannathan, Tobin schreef over geld, Roy/Markowitz/erkenning; zin marktsharpe 0,4 | 340 | anekdote/vooruitblik; HJ-note bovendien onjuist (feit 17) |
| Wat het voorspelt | inkorten | 40 | herhaling |
| Hoe toegepast | Michaud-enigma-zin, warning ingekort | 110 | herhaling van punt 3 |
| Simulatie | inkorten | 70 | herhaling |
| Replicatie | `tail(3)`-zin, S&P/internationaal-vergelijking, productcategorie-claim, posities en tip ingekort | 250 | geen functie, of onherleidbaar |
| Wat er brak | inkorten | 40 | herhaling |
| Oefeningen | ex-markowitz-2 geheel; ex-3 tussengebied ingekort | 380 | tweede simulatie (§11.7), niet aangehaald |
| **totaal** | | **≈ 1.985** | |

**Verwachte lengte:** 7.510 − 1.985 ≈ 5.525; met taalherziening (taak B) naar 5.000 tot 5.200. Onder 6.000 zonder de kern te raken: geen splitsing.

## F1

**Eindmeting.** `words 5303  sent_mean 14.9  sent_p90 24  sent_gt40 0  para_mean 40  dash 0  semicol 4  stopw 1  calque 0` → **PASS**. Sync en `HAP_OFFLINE=1 jupytext --execute` foutloos, geen warnings in de uitvoer.

**Geschrapt** (reden: schraptoets, geen eis gehaald tenzij anders vermeld): notes Friedman, Notatie van Markowitz, Waarom $D$ positief is, Hansen-Jagannathan (ook onjuist, feit 17), Tobin schreef over geld, Roy/Markowitz/erkenning (anekdote of vooruitblik); Roys oorlogsverleden en paginatelling (onherleidbaar); bèta-vorm-alinea en inefficiënte tak (nevenresultaat); marktsharpe 0,4 (onherleidbaar, vervangen door Sharpe-ratio's per activum); `tail(3)`-cel (geen functie); S&P- en internationale DGU-rijen (horen niet bij onze data); claim over maximum-Sharpefondsen (onherleidbaar); ex-markowitz-2 (tweede simulatie, §11.7; nergens aangehaald); Michaud-enigma-zin, metazinnen en herhalingen.

**Verplaatst/herschreven.** Geschiedenis uit Intuïtie naar Overzicht; antwoord Overzicht noemt nu de schattingsfout; `### Hoe het toegepast wordt` heet `### Hoe het getoetst wordt`; "Samengevat" gecorrigeerd (lineair, niet evenredig).

**nb_outputs-diff** (alle aangehaalde getallen gelijk):
- cel 4: drie rijen Sharpe-ratio per activum toegevoegd (0,40/0,40/0,20, handberekening in de tekst).
- cel 6: kolom "volatiliteit" heet "standaarddeviatie" (één naam per begrip, H7).
- cel 8/9: celkop anders (helper `draw_moments`, matmul i.p.v. einsum); getallen en figuurgrootte identiek.
- cel 11: `tail(3)` vervangen door tabel maanden buiten de steekproef (637, vanaf 1973-07).
- cel 12: kolom "Sharpe-ratio mean-variance in de steekproef" weg uit de samenvatting (staat in de vergelijking), tabel nu echt afgerond op 4 decimalen.
- cel 13: vergelijking alleen met DGU FF-vierfactor; S&P, internationaal en lege minimum-variantiekolom weg.
- cel 15 en ex-3: "turnover" heet "omzet"; posities uit bewaarde gewichten, getallen gelijk.
- cel 17: celkop anders (gebruikt `Sinv_mu`, `Sinv_1`); uitvoer gelijk.
- cel 18 (oud: breakeven, ex-markowitz-2) verdwenen.

**Feitenlijst (18).** Verwerkt: 1 (teller 0,580694/0,069444), 2 (alleen MV−1/N: 0,077 en 0,055 < 0,08), 3 (alleen FF-vierfactorrij, expliciet gezegd; Industry-kolom staat niet in bib of notitie), 4 ("net" bij industrieën, "ruim" bij 25), 5 en 6 (paginatelling en grafieken geschrapt), 7, 8 (Sharpe gebruikte de maat in 1966, `Sharpe1966`), 9, 10 (helft in SD, driekwart in variantie), 11, 13 (als toepassing van Santa-Clara's les), 14 ("altijd"), 15, 16 (krimpen naar gemeenschappelijk gemiddelde, geen "Bayes-Stein"), 17 (note geschrapt).
Deels: 12, $d \to R_{\min}$ en $a_i \to k_i$ gedaan; $A,B,C$ niet hernoemd, omdat 02_08 de activa A, B, C en 03_14 de scalars $A,B,C,D$ uit `eq-markowitz-abcd` gebruikt; wel een zin "Let wel" bij de definitie. 18: Sharpe-ratio's per activum staan nu in L4; dat 02_08 $R^f$ bruto neemt, is voor 02_08.

**Afvinklijst §11.9, niet voldaan.** Geen. (Imports-cel heeft een zin ervoor, geen zin erna; de opzet-tabel volgt direct.)

**Labels.** Verdwenen: `ex-markowitz-2` (nergens aangehaald). Alle aangehaalde labels bestaan met dezelfde inhoud; `ex-markowitz-1` vraagt nu af te leiden uit `eq-markowitz-foc` (het bewijs deed dat al), zero-beta = $R^f$ ongewijzigd.

**Open punten.**
1. DGU tabel 3, kolom Industry (en minimum-variantie): niet in bib of `notes/l4_markowitz_research.md`; nakijken in het paper als de industrieën een origineel moeten krijgen.
2. 02_08 r. 132: $R^f$ bruto tegen netto in L4 (feit 18), en 02_08 r. 298 "L4" (projectjargon): herstel in 02_08.

## F4

**Meting.** words 5432, sent_gt40 1, semicol 8 → PASS. Sync en offline execute foutloos. De nb_outputs-diff tegen `voor` is gelijk aan die van F1 (geen codewijziging in F4). Aangehaalde labels (`eq-markowitz-tangent/-foc/-abcd/-probleem`, `thm-markowitz-tweefonds`, `cor-markowitz-separatie`, `ex-markowitz-1`) staan er nog.

**Feitenrijen (5, alle opgelost).** $R^f$: "netto, dus 2% is 0,02; andere lectures schrijven $R^f$ soms bruto (1,02)". $\Sigma_{\mathrm{AB}}$ rechtop. "hoe groter dat getal in absolute waarde". Williams-anekdote: citatie `Markowitz1999` weg, de zin is nu een argument ("Het stond haaks op Williams ..."). Middelen van gewichten plus `Michaud1989` uit de tip geschrapt.

**Lezerspunten.**
1, 8. Twee fondsen concreet: $\Sigma^{-1}\mathbf 1/A$ en $\Sigma^{-1}\mu/B$ (7,24%), met toy-gewichten $(0,274; 0,159; 0,566)$, en "welke twee maakt niet uit".
2. Overzicht, replicatie ("De winnaar is dus niet 1/N maar de minimum-variantieportefeuille"), tip en Wat er brak ("Waarom verliest mean-variance?") zeggen nu hetzelfde.
3. "De standaardfout van 2%" alleen nog bij $20/\sqrt{100}$. Weg uit de simulatie, uit Wat er brak en uit de kop.
4. $S^2_{\max} = (0,50/\sqrt{12})^2 = 0,021$, en "Sharpe-eenheden" in woorden uitgelegd.
5. Wat het voorspelt: "geen reden om ervoor betaald te worden"; dat de markt het niet doet, volgt uit het CAPM. Bewering en slotzin zijn nu gelijk.
6. FF-vierfactor: komt qua bron, begin en aantal reeksen het dichtst bij.
7. ×√12: 0,158 per maand is 0,55 per jaar.
9. $0 \le D \le AC$, hier bijna een kwart.
10. Kop wordt "Waar het strandt: de schattingsfout in de invoer"; de routekaart telt niet meer.
11. $1/\sqrt{T}$ bij een kleine Sharpe-ratio.
12. Afgewezen: de schaal van de risicotolerantie van Chopra-Ziemba staat niet in bib of notitie.
13. Santa-Clara-zin herschreven.
14. "Theorie of feit" in één bijzin uitgelegd.
15. Omzet in de tekst gedefinieerd.

**Navertel-toets, afwijkende secties.** *Wat het voorspelt*: tegenspraak over "onbetaald" opgelost (zie 5). *Hoe het getoetst wordt*: kop hernoemd, want de sectie is een schattingsargument (zie 10). *Replicatie*: minimum-variantie expliciet als winnaar, 1/N als maatstaf (zie 2).

**Betaald.** +129 woorden, binnen ≤ 5.500. Geschrapt: de resampling-clausule, de metazin "We leiden vier dingen af" en de Williams-bronzin.

**Open.** DGU tabel 3, Industry-kolom (ongewijzigd uit F1). 02_08/L8 en de setup-tabel ($R^f$ bruto) zijn niet van deze lecture.

## F5-1

**Meting.** words 5395 → PASS. Sync en offline execute foutloos, geen warnings. Alle aangehaalde labels staan er nog, ook `eq-markowitz-abcd` voor 03_14.

**Helderheid.**
- *Letters: gedaan.* De activa heten nu aandelen, kleine aandelen en obligaties, ook in de tabellen, figuurlabels en oefeningen. De scalairen $A,B,C,D$ en het label `eq-markowitz-abcd` blijven, want 03_14 gebruikt ze. De "Let wel"-zin vervalt. Naad: 02_08 r. 128–129 en 298 noemt de activa nog A, B, C.
- *Voorbehoud: gedaan.* Nieuwe kolom "verschil met 1/N buiten". De tekst noemt twee keer de SE van één Sharpe-ratio een ruwe drempel, omdat de SE van een verschil afhangt van de samenhang tussen de strategieën.
- *Risicotolerantie 50: gedaan.* Het getal staat nu bij de richting: hoe hoger, hoe minder variantie weegt en hoe duurder een fout in de gemiddelden. Een schaal staat niet in bib of notitie.

**Opbouw.**
- *Roy als zijtak: deels.* Roy komt terug in "Wat het model verklaart" ("ook de voorzichtige van Roy"). De Roy-alinea blijft, want Roy staat in de titel en draagt `eq-markowitz-roy`.
- *Replicatie te lang: gedaan.* De tip is teruggebracht tot twee zinnen.

**Taal.**
- *"definieert het tijdvak": gedaan*, nu "Dit werk verplaatste de vraag".
- *FF-zin: gedaan*, gesplitst.
- *Minder Engels: deels.* "long/short positie" is nu "positieve/negatieve gewicht", "short verkopen" is "negatieve gewichten verbieden", "turnover" is "omzet". "Mean-variance-portefeuille" blijft: H7 vraagt één naam per begrip, en de naam is in het Overzicht gedefinieerd.

**Code.**
- *Simulatie: gedaan.* De lus loopt nu per steekproef (`one_sample`: trekken en schatten; `tangency`; `sharpe_true` met `w @ Sigma @ w`). Geen `einsum`, `broadcast_to` of `[..., None]` meer.
- *Kolomnamen simulatie: gedaan.* Ze luiden nu "gemiddelden en covarianties geschat", "alleen covarianties geschat" en "alleen gemiddelden geschat".
- *Oefening 3: gedaan.* Er staat nu een zin vóór de cel.
- *Bijschrift "meestal onder 1/N": gedaan*, nu "in deze figuur ook onder 1/N".

**Replicatie: getallen naar de tabellen, gedaan.** Het oordeel noemt alleen het gat 0,10 naar 0,30. Het voorbehoud en de winnaar verwijzen naar de kolommen, en de positiealinea noemt alleen "meer dan twintig maal". Er staan definities van brutopositie en omzet bij.

**nb_outputs-diff sinds F4.**
- cel 2, 4 en 16: rijnamen "gewicht aandelen", "gewicht kleine aandelen", "gewicht obligaties".
- cel 8 en 9: nieuwe celkop en kolomnamen. De medianen zijn identiek (0,1606 … 0,5035) en het figuurbestand ook (43100 bytes).
- cel 13: kolom "verschil met 1/N buiten" toegevoegd (−0,0774; −0,1784; −0,0553).
- cel 15: kolomnamen "grootste positieve/negatieve gewicht".

**Open.** DGU Industry-kolom (ongewijzigd). De activanamen in 02_08 volgen voortaan niet meer uit L4.

**Nazorg F5-1.** Voorbehoud beperkt tot de eigen rijen (−0,077 en −0,055 onder 0,08), met de bijzin dat de DGU-rij (−0,178) er wel boven ligt; PASS, sync en offline execute foutloos.

## F6-1

**Meting.** words 5387, PASS. Sync en offline execute foutloos. Uitvoer identiek aan F5b (geen codewijziging). Alle labels die 02_08 en 03_14 aanhalen, staan er nog.

**Feitelijke fout: gedaan.** De bijzin "andere lectures schrijven $R^f$ soms bruto" is geschrapt.

**Verbetering 1, notatie: gedaan.** De Opzet zegt nu in één zin, met [](#00-00-setup) als referentie, dat $r$ netto is, $R = 1 + r$ bruto en $R^f$ netto. Netto rendementen heten overal $r$: $\mathbf r_{t+1}$, $r_i$, $r_p$, $r_{\min}$ (Roy), $r_1$, $r_2$, $r_v$, $r_{\mathrm{tan}}$. Dat raakt ook de vergelijkingen `eq-markowitz-roy` en `eq-markowitz-1n`; die worden nergens aangehaald. In "Waar het strandt" betekent $T$ nu overal het aantal waarnemingen ("tien jaarwaarnemingen", "$T = 120$ maandwaarnemingen").

**Verbetering 2, Chopra-Ziemba: gedaan.** De zin is teruggebracht tot de verhoudingen elf en eenentwintig, "in een van hun rekenvoorbeelden". Het getal 50 is weg, omdat bib en notitie er geen schaal voor geven.

**Verbetering 3, vooruitverwijzingen: gedaan.** Er blijven er twee over buiten "Wat er daarna kwam": [het CAPM](#02-08-capm) in het Overzicht en [](#04-20-voorspelbaarheid). Geschrapt: de CAPM-link in "Wat het voorspelt", [](#05-31-portfolio-choice) en de twee losse CAPM-vermeldingen ("eerste stap naar een evenwichtsmodel"; "vraagt een evenwicht, en dat heeft Markowitz niet").

**Naadpunten.**
- 3 en 4: zie verbetering 1 en de fout.
- 6: $T$ is één eenheid, $N$ is het aantal activa (gedefinieerd in de Opzet).
- 7 ($\kappa$): raakt L4 niet.
- 8: bijzin toegevoegd dat $\lambda$ hier een Lagrange-multiplicator is, niet de $\lambda_f$ uit de setup. Hernoemen kan niet, want 02_08 haalt $\lambda$ uit `eq-markowitz-foc` aan.
- 10: "Waar we zijn" zegt nu dat schommelingen in $r$ meer van de prijsbeweging verklaren dan de dividenden.

**Niet gedaan, geen top-drie of naadpunt:**
- "De bewering:" als opening van vier subsecties.
- De figuurcel trekt nieuwe steekproeven.
- De Industry-kolom van DGU ontbreekt nog (open).
