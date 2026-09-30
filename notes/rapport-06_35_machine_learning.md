STATUS 06_35_machine_learning F4T words=5700 prose=PASS open=0 cijfer=- min=-

# Rapport 06_35_machine_learning (L35)

**Kern.** Blijft er voorspelbaarheid over als een machine alle karakteristieken tegelijk gebruikt en streng buiten de steekproef wordt beoordeeld? Ja, een kleine maar echte hoeveelheid, vooral uit niet-lineariteit, maar het is een meting en geen verklaring (risico, vergissing of leren), en na kosten en na 2005 wordt de winst klein.

## F0

`words=6112 sent_p90=29 sent_gt40=10 para_mean=66 semicol=28 motief=4 Lnum=9 je_form=2 calque=10 engquote=20 colon_mid=9.7 para_one=13 telegram=2 tmpl=9` (FAIL op 14 drempels).

Vijf grootste problemen:
1. Lengte en stofdichtheid: 6.112 woorden, drie simulaties, vier stellingdelen KNS, IPCA-oefening (Theorie, Simulatie, Oefeningen).
2. Engelse citaten midden in de zin (Santa-Clara r. 45, 102; Martin-Nagel r. 553; KMZ r. 561) en calques (in-sample/out-of-sample, prijst, beprijsd, paper, lecture, equal-/value-weighted).
3. Sjabloon- en regeltaal: 9 keer "Waarom zou dit waar zijn?", "motief 3", "het 2%-motief" (2x), "praktijkmotief", werkmeldingen in de tekst ("hebben we niet nagelezen", r. 502, 561, 575, 1266).
4. Getallenbrij in proza: GKX-resultaten (### Out-of-sample R², r. 389–398), replicatie (1) en (2) (r. 1079–1095, 1229–1249); geen tabel origineel/hier.
5. Structuur: imports-cel in Overzicht, geen routekaart of Samengevat, toy met tweede mechanisme (boomtabel), oefening 1 geen instap, bewijzen > 6 regels open; plus fout in replicatie (2): "vijf hoofdcomponenten 0,30" en "vijf PC's 0,78" staan niet in de uitvoer (0,78 hoort bij K = 4).

Schraplijst (schraptoets §11.11; eis 2 gecontroleerd met grep: geen enkel `machine-learning`-label wordt buiten dit college aangehaald, alleen de paginalabel door 06_34, 06_36, 07_37, 08_39):
| passage | ~woorden | eis niet gehaald |
|---|---|---|
| Toy: boomtabel en voorspellingen per methode | 200 | 1 (tweede mechanisme; boom blijft in één zin met handberekening) |
| PCR/PLS-sectie → twee zinnen in Krimp | 90 | 1 |
| Neurale netwerken → alinea in Flexibiliteit | 110 | 1 |
| GKX-getallenalinea → tabel | 120 | vorm (tabel) |
| KNS deel 4, Britten-Jones, Lettau-Pelger, Chen-Pelger-Zhu, niet-nagelezen-zin | 190 | 1, 2, 3 |
| IPCA-ALS-details | 90 | 1 |
| Deugd van complexiteit (### + simulatie c) → oefening 2 | 250 | 1 (tweede/derde simulatie) |
| IPCA-oefening op French 100 | 300 | 1 |
| Engelse citaten → parafrase | 120 | taal |
| Replicatie en Wat er brak inkorten | 350 | 1 |
Verwachte lengte: 6.112 − ~1.800 + ~300 (routekaart, Samengevat, instap, tabellen-zinnen) ≈ 4.600–5.500. Geen split nodig.

## F1

Eindmeting: `words=5472 sent_mean=17.6 sent_p90=28 sent_gt40=0 para_mean=54 semicol=0 motief=0 calque=0 engquote=0 colon_mid=0.5 para_one=11 tmpl=1` → PASS. Uitvoering offline zonder fouten (exit 0).

Geschrapt of verplaatst:
- Simulatie (c) double descent → oefening 2 (code en cijfers ongewijzigd; plotcel geschrapt); plaats gekozen zodat de rng-volgorde gelijk blijft.
- IPCA-oefening geschrapt (eis 1; te lang voor de woordgrens); IPCA-theorie ingekort tot model + toets.
- KNS-propositie van vier naar één bewering (posterior + PC-vorm); ridge-op-prijsfouten als eigen vergelijking `eq-machine-learning-kns-ridge`; bewijzen van beide proposities in dropdown.
- Britten-Jones, Lettau-Pelger, Chen-Pelger-Zhu, PLS, GKX-voetnoot 3,74%, turnover 110–130%, NN-regularisatielijst: geschrapt (eis 1).
- Nieuwe oefening 1 (instap, variatie op toy); oude 1 → 3, oude 2 → 4.
- Imports-cel naar begin Toy; routekaart en Samengevat toegevoegd; twee tabellen origineel/hier met oordeel "Geslaagd".

nb_outputs-diff (63+/79−), alle bedoeld: toy-cel toont nu tabel hand/scikit-learn en boomvoorspellingen i.p.v. voorspellingstabel; kmz-tabel verhuisd van cel 10 naar cel 17 (waarden identiek, o.a. −14541.674, 0.134); kmz-plot weg; tekst "voorspellingen buiten de steekproef"; KNS-kolommen hernoemd naar 1975-2004/2005-2024 (waarden identiek); nieuwe instapcel (0,4/−0,075/1,4/−0,1); IPCA-cel weg; figuurtitels vertaald. Sim (a), sim (b), MC (0.8972) en oefening 4 (−16.26 …) ongewijzigd. nb_numbers: 15 niet in uitvoer, alle bron- of handberekening (GKX-tabel, 1/2,25, SE 0,24, −3,46, 2,45).

Correctie: replicatie (2) vergelijkt nu K = 4 (PC's 0,262/0,780; signalen 0,039/1,723), wat in de uitvoer staat; de oude "vijf" was niet herleidbaar.

Afvinklijst §11.9, niet voldaan: "Eén simulatie" is formeel twee delen (GKX-wereld en Martin-Nagel) onder één vraag; oefening 3 is geen uitbreiding van de replicatie maar van de simulatie. Overige: ok.

Labels: verdwenen `fig-machine-learning-sim-kmz`, `cel-machine-learning-sim-kmz` (nergens aangehaald); `ex-machine-learning-1..4` hebben nieuwe inhoud (niet extern aangehaald); nieuw `eq-machine-learning-kns-ridge`. Naad: alle aangehaalde 04_*/05_*-labels bestaan; bewering bij `eq-sdf-unificatie-b-lambda` herschreven naar λ = −Cov(f, m) = Σb, wat daar staat; verwijzing naar 05-31 geschrapt (Waar we zijn ≤ 2 refs).

Open punten voor de feitencontroleur:
1. GKX-getallen in tabel en tekst (tabel 1 en 7, 0,16/0,40/1,35/0,61, EW 2,45 → 1,69, "minder dan zes bladeren", NN3 > 30.000 parameters, validatie 1975–1986) niet opnieuw in het artikel nagekeken.
2. KNS: schaling van de prior met τ = tr(Σ) en de uitspraak "κ² = verwachte gekwadrateerde maximale Sharpe-ratio" volgen uit de afleiding hier, niet nagelezen in het artikel.
3. IPCA-claims (vier factoren, insignificante alpha's) komen uit de samenvatting van het werkdocument.
4. Avramov, Cheng en Metzker: bewering over moeilijk verhandelbare aandelen niet nagelezen.
5. Parafrase van Santa-Clara (twee keer zo goed; zesde open vraag) tegen de bron controleren.

## F4

Feiten: nr 2 (Overzicht) "dertien" geschrapt; nr 3 (Overzicht) verdubbeling toegeschreven aan GKX-abstract; nr 4 afgewezen, parafrase van geciteerde bron zonder getal; nr 5 (IPCA) "vier" -> "een paar"; nr 15 (Flexibiliteit) "dicht bij nul"; nr 18 (Toetsen) behouden, consistent met GKX-abstract; nr 20 (Wat er brak) omzet en 2,45 -> 1,69 geschrapt, ACM-abstract ervoor in de plaats; nr 38 (Replicatie 2) `print(H)` in cel, uitvoer 158; nr 41 (Replicatie 2) verschil 0,25 "van dezelfde orde als de se van een Sharpe", daling vele malen groter.
Lezer:
1. Replicatie (2): zie feit 41, gedaan.
2. Flexibiliteit: zie feit 15, gedaan.
3. Replicatie (2): -170 geduid (prijsfoutvector ruim 13 keer zo lang als de gemiddelden, sqrt(171) = 13,1), gedaan.
4. IPCA: exemplaar (element van Gamma_beta: bèta stijgt als bedrijf kleiner is), gedaan.
5. Opzet: n_eff geduid met miljoenen aandeel-maanden tegen 720 maanden (geen verzonnen aantal), gedaan.
6. Opzet, Martin-Nagel, Simulatie: genummerde verwachtingen herschreven naar gewone zinnen, gedaan.
7. Replicatie (1) en (2): "verwachte afwijking" als onderwerp weg, gedaan.
8. Overzicht: motiefnaam weg ("Hier staat de meting het verst van de theorie af"), gedaan.
9. Wat er brak: Chicago- en Yale-lezing met bijzin uitgelegd, gedaan.
10. Toetsen: exemplaar (uitschieter van 50% tilt vijfjaarsgemiddelde bijna 1 pp per maand op), gedaan.
11. Replicatie (2): "ander verhaal" -> "blijft de ongekrompen portefeuille wel voorop", gedaan.
12. Afgewezen: STYLE §3 staat een Engelse vakterm toe als vertaling gekunsteld is; *sparse* staat cursief met uitleg.
13. Afgewezen: STYLE §3 houdt "limits of arbitrage" Engels; nu wel cursief met uitleg.
14. Replicatie (1): drie maatstaf-zinnen -> lijst van vier, gedaan.
15. Simulatie: zijspoor x2 vervangen; IS-kolom besproken (1,5 pp bij J/N = 0,4), gedaan.
Overig: H5 (risiconeutraal bij de stap), "zij/haar" voor zaken weg (Overzicht, KNS), alinea's herschikt tot volle regels.
Navertel-toets: afwijking alleen bij IPCA (formule zonder exemplaar) en Opzet (n_eff abstract); beide hersteld.
Code: alleen `print(H)` toegevoegd; nb_outputs verschilt alleen in die regel.

## R9-1 (F6b, ronde 9+)

Feitelijke fouten:
1. Samengevat (:499) "LASSO schaalt" -> "schuift elk gewicht een vast bedrag naar nul en selecteert", gedaan.
2. Replicatie (1) (:949) "alle getallen lager" -> R^2 van GKX en Sharpe-ratio's dalen, R^2 t.o.v. historisch gemiddelde stijgt omdat dat gemiddelde na 2005 slecht voorspelt, gedaan.
3. Simulatie (:668) oefening 4: "stort OLS in één van drie replicaties wel in", gedaan; vraag van oefening 4 zonder de -3,46% van GKX.
4. Simulatie (:521) "gewogen som ... elke term geschaald op eenheidsvariantie", gedaan.
5. Toy-code (:170) commentaar beperkt tot Lasso/ElasticNet ("Ridge does not"); notebook opnieuw uitgevoerd.
6-7. "rond 55%" en "rond een half procent", gedaan.
Drie verbeteringen / Voor een 9:
- Replicatie (2): tabel KNS (kwalitatief, geen herleidbare KNS-getallen, kaart §6) tegen hier (cs-R^2 volledige/ongekrompen/4 PC/4 signalen, Sharpe) vóór "Geslaagd"; de twee alinea's na de KNS-cel en de twee na de figuur hebben nu elk hoogstens drie getallen; formule-uitwerking 0,61 vervangen door verwijzing naar de formule bij (1).
- Helderheid: kappa geduid in KNS-theorie (som van kappa^2 lambda_j/tau = kappa^2, maximale Sharpe per periode, ~0,13/maand) en in de replicatie (0,46 per jaar); "kenmerken" -> "karakteristieken" (4x); orde van grootte KNS-maatstaf (0,4 = prijsfouten laten 60% over).
- Taal/regeltaal: :602 herschreven (plus zin wat populatie-R^2 is), :804 economische reden i.p.v. "fout in de code", :321, :254, :57 herschreven volgens hardop-toets.
- Code: zin tussen de twee niet-lineaire cellen; X_aug/y_aug-augmentatie uitgelegd bij (2).
Aanmerkingen / Beter uitleggen:
- Opbouw :667 OLS en ridge liggen binnen honderdsten; zin dat de simulatie "krimp verslaat OLS" niet toont; alinea gesplitst.
- H11: sigma^2/beta^2 = 25 in de simulatie tegen de getallen van de Theorie, gedaan.
- Toy: 88% geduid in slotalinea; boom als "bouwblok van de flexibele methoden", gedaan.
- Replicatie (1) :942 tweede reden (diversificatie van portefeuilles), gedaan.
- IPCA-getal afgewezen: geen getal uit cel of geciteerde bron beschikbaar (kaart §6).
- Oefening op echte data: afgewezen, geen vereiste voor een 9 (beoordelaar).
Woorden: 5961 (was 5700), prose_stats PASS, nb_numbers geen nieuwe meldingen.
