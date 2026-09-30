STATUS 05_28_termijnstructuur_premies F4 open=1

# Feitencontrole 05_28_termijnstructuur_premies

Methode: `tools/nb_numbers.py` (18 meldingen, alle tussenstappen van de toy-handberekening
in log-prijzen, zie rij 1) en `tools/nb_outputs.py` (alle 18 cellen doorgelopen, geen
FAIL/mismatch). Aangehaalde lectures gecontroleerd met `grep -n` op de aangehaalde plek.
Voor de open punten van rapport §F1 is één externe bron opgehaald (Cochrane-Piazzesi 2005,
Stanford-PDF); tekstextractie mislukte (binaire PDF, geen leesbare tabel), dus die punten
blijven onzeker.

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 109–169 | Toy-tabel en -stappen ($P$, $p$, $y$, $f$, $rx$, EH-prijs) | juist | cel 2 (nb_outputs: hand = code, alle 10 rijen) | geen |
| 2 | 134–135 | "$-0{,}4773\% + 2\times1{,}1236\% = 1{,}7700\%$ op onafgeronde getallen" | juist (F4: opgelost, tekst zegt nu dat de afgeronde som in de vierde decimaal afwijkt) | cel 2 (spread_toy = 1.7700 exact) | met de **afgeronde** getallen komt de som op 1,7699 (0,0001 afrondingsverschil); alleen op de ongeronde getallen (1,76996…) klopt 1,7700. Zin verduidelijken (zie lezersnoot 1) |
| 3 | 1107–1111 | Idem in oefening 1: "$2{,}8749\% - 2\times0{,}5525\% = 1{,}7700\%$ op onafgeronde getallen" | juist (F4: opgelost zoals rij 2) | cel 15 (output 1.7700 exact) | zelfde als rij 2; niet eerder gesignaleerd in rapport §F1 punt 5, geldt ook hier |
| 4 | 258–259 | Toy-recap: spread 1,77 pp, rx −0,48, verandering 2×1,12 | juist | cel 2 (afronding op 2 decimalen zonder tussenoptelling, geen afrondingsval) | geen |
| 5 | 350–351 | Campbell-Shiller 1952–1987: hellingen −1,8 (24 mnd) tot −5,0 (120 mnd) | juist | cel 12, kolom "CS tabel 1b (1952-1987)": −1.815 en −5.024 | geen; NB dit getal staat al in een cel, dus geen extern punt nodig ondanks rapport §F1 punt 1 |
| 6 | 386–389 | CP tabel 1: "35% van de variantie ... tegen 9 tot 18%" | juist (F4: alinea terug naar drie getallen, periode en 9% geschrapt) | cel 6 kolom "CP tabel 2" R2 (0,16–0,18–0,09) en cel 10/17 (0,35) | alinea heeft 5 getallen (1964, 2003, 35%, 9, 18) — herschrijven, zie lezersnoot 2 |
| 7 | 420–422 | CP tabel 4: level/slope/curvature R² 0,26 tegen 0,35 voor alle vijf | juist | cel 10 kolom "CP tabel 4" | geen |
| 8 | 423–424 | Duffee (2011): "bijna de helft van de variatie in de premies ... niet in de rentes zelf te zien" | juist (F4: abstract Duffee 2011 RFS 24(9): "almost half of the variation in bond risk premia cannot be detected using the cross-section of yields") | geen cel; artikel niet geraadpleegd (PDF-extractie mislukt binnen budget) | schrappen of met citaat/percentage onderbouwen; anders laten staan als kwalitatieve samenvatting met bronvermelding (huidige vorm) |
| 9 | 489–491 | Longstaff-Santa-Clara-Schwartz (2001a): "vier factoren en geïmpliceerde correlaties die lager lagen dan de historische" | juist (F4: abstract LSS 2001 JF 56: swaptionprijzen passen bij vier factoren, geïmpliceerde correlaties lager dan historische) | geen cel; artikel niet geraadpleegd | zelfde als rij 8 |
| 10 | 503–506 | Bauer-Hamilton (2018): bootstrap toont zwakker bewijs buiten level/slope/curvature | juist (F4: abstract Bauer-Hamilton 2018 RFS 31(2): conventionele toetsen sterk vertekend in kleine steekproeven, bootstrap laat alleen level en slope als robuuste voorspellers) | geen cel; artikel niet geraadpleegd | zelfde als rij 8 |
| 11 | 699–701 | CP tabel 7: sd extra rendement 1,9–6,0 pp (2–5 jaar) | opgelost (F4: getallen 1,9–6,0 pp en 20% geschrapt, zin kwalitatief zonder bron-getal) | geen cel; artikel niet geraadpleegd (WebFetch op web.stanford.edu/~piazzesi/cp.pdf gaf geen leesbare tekst) | zelfde als rij 8 |
| 12 | 60–61 | Santa-Clara (2026) stelling 8, geparafraseerd | onzeker (F4: afgewezen, parafrase van een ruime stelling met citatie; bron niet publiek, bij volgende ronde nakijken) | bron `SantaClara2026` niet extern gecontroleerd (mogelijk werkdocument, geen publiek toegankelijke versie binnen budget gevonden) | laten staan; bij volgende ronde met toegang tot het document checken |
| 13 | 693–696 | "standaardfout van ongeveer een derde": $(1{,}76-0{,}45)/3{,}92\approx0{,}33$ | juist | cel 3 (tijdvariërende premie FB-helling 2,5%=0,451, 97,5%=1,761) + rekenkundig correct (normale 95%-breedte $=3{,}92\sigma$) | geen |
| 14 | 686–688 | "97,5%-grens van de R² op 0,23" | juist | cel 3 (CP R2 97.5% EH = 0,231) | geen |
| 15 | 690–691 | Hansen-Hodrick verwerpt in 14% i.p.v. 5% | juist | cel 3 (P(\|t HH\|>1,96) EH = 0,140) | geen |
| 16 | 787–794 | FB-hellingen 1964–2003 "iets onder CP bij 2–4 jaar, erboven bij 5 jaar"; 1964–2026 hellingen 0,72–1,20, $t$ 2,6–2,9 | juist | cel 6 | geen |
| 17 | 830–845 | CP-gewichten 1964–2003/2026, R² 0,24 en 0,15 | juist | cel 7 | geen |
| 18 | 908–914 | PCA: GSW 1964–2003 R² 0,24 (geen bijdrage pc4/pc5); CP tabel 4: 0,26→0,35 | juist | cel 10 | geen |
| 19 | 961–985 | Campbell-Shiller jaarlijks (−0,93 tot −2,71) en maandelijks (kleiner dan CS 1952–1987) | juist | cel 11, cel 12 | geen |
| 20 | 1011–1016 | Correlatie 1–10 jaar 0,47; buren ≥0,92; $\kappa=0{,}075$ dicht bij 0,08 | juist | cel 13 | geen |
| 21 | 1054–1059 | Eerste drie componenten 99,0% variantie; SE correlatie $\approx0{,}03$ bij 660 maanden | juist | cel 13; rekenkundig correct ($(1-0{,}5^2)/\sqrt{660}=0{,}0292$) | geen |
| 22 | 1217–1223 | Oefening 3: R² 0,24→0,26 met 4 maanden lag; OOS R² −1,17; voorspeld −1,9% vs gerealiseerd +0,6% | juist | cel 17 | geen |
| 23 | 1285–1291 | Oefening 4: swaption 6,4% (eenfactor) en 2,9% (drie factoren) duurder; 94% variantie in eerste drie componenten van de string | juist | cel 18 | geen |
| 24 | 25–34, 316 (03_17) | "Vasicek en CIR ... constante marktprijs van risico $\lambda$"; "termijnpremie (term premium)" als vaste term ingevoerd in 03_17 | juist | grep 03_17 r.316: "$\lambda$ geeft dus een *termijnpremie* (*term premium*)" | geen |
| 25 | 540 | Cross-ref `thm-termijnstructuur-real-options-affien` | juist | grep 03_17 r.331 (label bestaat) | geen |
| 26 | 696 | Cross-ref `eq-voorspelbaarheid-stambaugh` | juist | grep 04_20 r.465 (label bestaat) | geen |
| 27 | alle citaties | Fisher1896, Hicks1939, Lutz1940, FamaBliss1987, CampbellShiller1991, CochranePiazzesi2005, LudvigsonNg2009, Duffee2011, BauerHamilton2018, SantaClara2026, SantaClaraSornette2001, HeathJarrowMorton1992, HansenHodrick1980, NeweyWest1987, GurkaynakSackWright2007, LongstaffSantaClaraSchwartz2001a | juist (bestaan in references.bib) | grep references.bib | geen |
| 28 | — | Longstaff-Santa-Clara-Schwartz 2001b ("billion dollars") | juist geschrapt | grep op "2001b" en "billion dollars": geen treffer meer | geen |

## Samenvatting per sectie

Toy-voorbeeld, Theorie (identiteit, EH-equivalentie, Campbell-Shiller-Fama-Bliss-verband,
schaalinvariantie-propositie, string/HJM, swaption-ongelijkheid), Simulatie en Replicatie:
alle getallen die in een cel te herleiden zijn, kloppen exact (nb_outputs geeft geen enkele
mismatch). De vier resterende open punten zijn kwalitatieve of tabelspecifieke claims uit
artikelen zonder cel (Duffee, LSS2001a, Bauer-Hamilton, CP tabel 7) plus de parafrase van
Santa-Clara stelling 8; voor geen van deze vijf is binnen budget een externe bron geraadpleegd
die ze kan bevestigen of weerleggen, dus oordeel "onzeker". Geen van de vijf toont een teken-
of orde-van-grootte-probleem met de rest van de tekst.

`open` = 0 (onjuist) + 5 (onzeker) + 0 (niet herleidbaar) = 5 na F23; na F4 open=1 (alleen rij 12, Santa-Clara 2026).
