STATUS 04_18_fama_french F4T words=5651 prose=PASS open=0 cijfer=- min=-

# Rapport 04_18_fama_french (L18)

**Kern.** Vraag: welke kenmerken blijven over als ze tegelijk naast bèta staan, en is daar
een model van te maken? Antwoord: grootte en B/M; het driefactormodel (markt, SMB, HML)
brengt de prijsfouten van de 25 size/BM-portefeuilles terug van ongeveer een kwart naar een
tiende procent per maand, maar een goede fit op dezelfde sorteringen zegt niet of risico
of het kenmerk wordt beloond.

## F0

`prose_stats`: words 5730, sent_mean 22,1, sent_p90 37, sent_gt40 21, para_mean 74,
semicol 52, motief 4, je_form 3, calque 6, engquote 8, colon_mid 11,3, para_one 16,
telegram 1, tmpl 6 (Waarom zou 6), repeat 1. FAIL op 14 drempels; words haalt de grens.

**Vijf grootste problemen**

1. Taal, hele college: 52 puntkomma's, 21 zinnen boven 40 woorden, alinea's gemiddeld 74
   woorden (Theorie r219-245, r438-449; Simulatie r563-576; Replicatie r895-904).
2. Regeltaal en jargon: "epistemische status ... motief 3" (Overzicht r48), "motief 1"
   (Simulatie r715, Replicatie r1010), "lecture" (r103, r550), je-vorm in "Welke vraag
   staat open" (r30-31), "beprijst/beprijsd" (r32, r1101), "equal-weighted" (r237),
   "het hart van" (r272), zes keer "Waarom zou dit waar zijn".
3. Structuur: imports-cel in Overzicht (r68); geen routekaart en geen Samengevat in
   Theorie; "Wat we al weten" verwijst naar vier colleges; intuïtie zonder voorspelling.
4. Getallenbrij: r714-726, r895-904, r938-945, r998-1007, r1065-1070 met vier tot twaalf
   getallen per alinea; replicatieblok ~330 woorden; geen tabel origineel/hier en geen
   oordeel "Geslaagd / Gedeeltelijk / Niet geslaagd".
5. Toy en oefeningen: toy-cel eindigt met prints, geen tabel hand/code (r199-206);
   oefening 1 is geen instap; oefeningen als link in de tekst (r723, r1085).

**Schraplijst (STYLE §11.11).** Elders aangehaalde labels (grep lectures/):
`04-18-fama-french`, `thm-fama-french-sdf`, `prop-fama-french-mechanisch`,
`eq-fama-french-factoren`, `ex-fama-french-3` (05_26, momentumoefening). Geen passage
hieronder bevat er een.

| passage | kopje, regels | woorden nu → straks | eis die ze niet haalt |
|---|---|---|---|
| citatiereeks gevolgen | Overzicht r48-58 | 150 → 60 | 1: dubbel met Theorie en Wat er brak |
| constructiekeuzes (Compustat, splitsingen) | Theorie r234-245 | 170 → 90 | 1 |
| Kothari-Shanken-Sloan en Black | Theorie r279-284 | 90 → 50 | 1 |
| vier aanbevelingen LNS | Theorie r438-449 | 170 → 80 | 1 |
| ### Risico of vergissing: nood en extrapolatie | Theorie r526-552 | 330 → 0 | 1 en 3: dubbel met Wat er brak |
| tabel III in Theorie | r264-270 | 60 → 0 | verhuist als origineel/hier naar Replicatie |
| replicatieblok | r820-861 | 330 → 200 | §11.7: ≤ 250 woorden |
| getallenalinea's | r714-726, r895-1070 | 700 → 550 | §11.5: ≤ 3 getallen per alinea |

Erbij: routekaart, Samengevat, instap-oefening, voorspelling in de intuïtie, oordelen.
Verwachte lengte ≈ 5.230 woorden. Geen splitsing nodig.

## F1

**Eindmeting.** words 5516, sent_mean 16,4, p90 24, >40 0, para_mean 50, semicol 7 (lijst
en formules), motief 0, calque 0, engquote 1, colon_mid 0,9, para_one 6, tmpl 2: PASS.
`rewrap` gedraaid (1290 → 1318 regels; rewrap wijzigde codecellen, die zijn uit de
versie vóór rewrap teruggezet), `jupytext --sync` en `nbconvert --execute` offline zonder fout.

**Geschrapt of verplaatst.**
- ### Risico of vergissing (Theorie): dubbel met Wat er brak; kern (Chan-Chen, FF1995, LSV) staat daar nu.
- Tabel III: uit Theorie naar Replicatie als tabel origineel/hier; Theorie noemt twee $t$-waarden.
- Constructiekeuzes, Kothari/Black, LNS-aanbevelingen, citatiereeks Overzicht: ingekort (eis 1).
- Tweede tijdreeks/cross-sectie-### samengevoegd tot "### Wat een goede fit bewijst".
- Oefening LNS/industrieën (was ex-2, met cel) geschrapt: lengte; aanbeveling 1 staat in Theorie.
- Bewijzen van de SDF-stelling en de Daniel-Titman-propositie in dropdown.
- Nieuw: routekaart, Samengevat, voorspelling aan eind Intuïtie, instap-oefening ex-1 (toy
  met C = 8%), tabellen origineel/hier met oordeel, kalibratietabel simulatie.

**nb_outputs-diff (voor 15 cellen, na 16).** Cel 2 (toy): prints en 2×3-tabel vervangen door
tabel hand/code, zelfde waarden. Simulatiecel 3 gesplitst (parameters zonder uitvoer +
portefeuilles), waarden gelijk. Kolom- en rijnamen: "alfa" → "alpha", "karakteristiekwereld"
→ "kenmerkwereld", alleen de kolombreedte verschuift. Nieuwe cel ex-1 (1,333 → 2,333; 2,5 →
4,0; 1,5 → 1,53). Cel industrieën (oude ex-2) weg. Tien sleutelgetallen nagelopen (R² 0,8641,
premie/gem. 15,78, GRS-verwerping 0,978, DT −0,1216, 0,261/0,647, klein-groei −0,468/−5,093,
GRS 3,629, HML vóór FF 0,450, bèta+ME −1,08, momentum 1,003/5,558): identiek.

**Code.** Toy-cel met functie `ff_factors` (hergebruikt in ex-1); `dt_w` via benoemde
functie `dt_long_short` in plaats van dubbele mediaanexpressie; docstrings Nederlands.

**§11.9, wat niet voldoet.** Simulatie heeft twee delen onder één vraag (GRS/Daniel-Titman
en nepfactoren); bewust behouden omdat beide `prop-fama-french-mechanisch` en
`prop-fama-french-karakteristiek` illustreren. Overige: ok.

**Labels.** Geen label verdwenen dat elders wordt aangehaald. `ex-fama-french-1` is nu de
instap (was Daniel-Titman), `ex-fama-french-2` is Daniel-Titman (was LNS),
`ex-fama-french-3` blijft momentum; oude LNS-oefening zonder label weg. Verwijzingen naar
oefeningen in de tekst zijn nu gewone tekst.

**Open punten voor de feitencontroleur.**
1. De getallen in de tabellen origineel/hier (tabel 9a/9c en tabel III) en in Theorie
   (2267 aandelen, 3616 van 4797, 8%) komen uit de artikelen, niet uit een cel; nakijken.
2. Twee correcties: "over twintig jaar" na publicatie werd "ruim dertig jaar" (403 maanden);
   "bij het CAPM stijgen de alpha's in elke groottegroep" werd "bijna elke" (groep 4:
   −0,04 en −0,10).
3. Wat er brak zegt nu dat Daniel en Titman en Davis, Fama en French tot tegengestelde
   conclusies kwamen; controleren tegen beide samenvattingen.
4. De opdracht vroeg Nederlandse docstrings; STYLE §3 zegt Engels. Opdracht gevolgd.

## F4

**Feiten.** Rij 2 (Theorie, Fama en French 1992): citaat bij de $t$-waarden en "In hun tabel III".
Rij 4 (idem): citaat bij 2267 aandelen. Rij 9 (Replicatie, bijschrift decennia): SMB gaat van sterk
negatief in de onvolledige jaren twintig naar positief in de jaren dertig. Rijen 5 en 6 afgewezen:
getallen uit een geciteerde bron, de tekst noemt de scan; tabelinleiding tabel III kreeg het citaat.
**Lezer.**
1. Replicatie, na tabel 9a: nieuwe oriëntatiezin over de uitvoer (alpha's, $t$, $R^2$). Gedaan.
2. Replicatie, na Fama-MacBeth: zin over zes specificaties en twee periodes. Gedaan.
3. = feitenrij 9. Gedaan.
4. Theorie, GRS: de uitkomst 1,43 wordt nu gelezen als "intercepten krimpen zo ver dat de toets
   het model niet verwerpt", zonder vaste formule. Gedaan.
5. Toy, verwijzing naar `prop-fama-french-mechanisch`: de kern stond er al sinds F1. Gedaan (niets nodig).
6. Simulatie, nepfactoren: kern van de propositie in één zin herhaald. Gedaan.
7. Replicatie, overstap naar Fama-MacBeth als andere, cross-sectionele toets benoemd. Gedaan.
8. Theorie, FF1992: helling-als-portefeuille herschreven. Gedaan.
9. Replicatie: calque "in op grootte gesorteerde" herschreven. Gedaan.
10. Overzicht: "dat het paste" wordt "omdat het de gemiddelde rendementen goed beschreef". Gedaan.
11. Afgewezen: $-2{,}58$ naar Theorie zou een nieuwe nb_numbers-melding geven; staat in tabel III.
12. Theorie, GRS: de noemer groeit met de Sharpe-ratio en maakt de toets milder (voorstel van de
    lezer, "strenger", had de richting verkeerd). 13. Samengevat: reden (bèta's opschalen). 14. Theorie:
    gesplitst met "Ook dat bleef betwist, want". 15. Wat er brak: "sterk verleden van winstgroei". Gedaan.
**Navertel-toets.** Geen sectie week af; de drie sporen van de lezer zijn gedicht via punten 5, 6, 7.
**Code.** Alleen docstrings terug naar Engels (13); nb_outputs voor/na identiek. Twee Nederlandse
commentaarregels (toy-cel) en de TODO-regel bleven staan, want de opdracht stond alleen docstrings toe.
Woorden 5499 → 5651; betaald met Samengevat-bullet over de simulatie, een bijschriftzin en inkortingen.

## R9-1 (F6b, ronde 9+)

Een eerdere F6b-agent werd afgebroken; zijn wijzigingen zijn nagelopen tegen de kopie van vóór F6b en kloppen, op één na (hieronder).
**Feitelijke fouten.** (1) Toy-slotzin noemt nu de twee echte lessen (C weegt een derde van de kleine kant van SMB; met $T = K$ is elke alpha nul). Gedaan. (2) r. 930 omgezet: de krimpende standaardfout verklaart de $t$-waarde, niet de alpha. Gedaan. (3) $\boldsymbol{\mu}_H = \rho\mathbf{Z}_H\boldsymbol{\lambda}$, en gezegd dat de rijen van $\mathbf{B}_H$ en $\mathbf{Z}_H$ de factorportefeuilles zijn. Gedaan. (4) `solve(H_loadings, ...)`; uitvoer $-0{,}1177 \to -0{,}1176$, tekst noemt $-0{,}12$. Gedaan. (5) Het gedeelde feit is nu de hogere opbrengst van kleine en waardeaandelen met zwakke winsten. Gedaan.
**Verbetering 1 / opbouw.** Overzicht zegt "kleine alpha's" en beschrijft de propositie als cross-sectionele $R^2$ met vrije premies; Theorie-routekaart noemt de twee soorten fit; Wat er brak noemt beide zwaktes juist (kleine alpha's passen bij beide werelden; hoge $R^2$ voor bijna elke meebewegende factor). Gedaan.
**Verbetering 2 / toy.** Stap 4-5 expliciet aangekondigd als los tweede voorbeeld dat alleen het vrijheidsgradenpunt toont. Gedaan.
**Verbetering 3 / notatie.** Lading $\ell_i \to \beta_i$, $\mathbf{L}_H \to \mathbf{B}_H$ in Theorie, oefening 2 en het printlabel. Gedaan. Scalaire alpha niet meer vet. Gedaan.
**Helderheid.** SDF-zin nu in termen van $\mathbf{b}'\mathbf{f}$ en $\mathbf{b} = \boldsymbol{\Sigma}_f^{-1}\E[\mathbf{f}]$. Gedaan. Getal $S_f$ tegenover Sharpe-ratio markt: afgewezen, geen cel of geciteerde bron levert het (kaart §6), en de code mag hier niet uitgebreid worden.
**Taal.** Hardop-toets r. 75, 930, 1169-1171 herschreven volgens de voorstellen; "in maandvorm" vervangen door een standaardfout per decennium die ongeveer even groot is als de premie. Gedaan. Losse woorden in de bronregel: twaalf alinea's met stompe regels opnieuw gevouwen (alleen witruimte). Gedaan.
**Code.** `size_q`/`value_q`/`small`/`value_3` uitgeschreven met commentaar; commentaar bij `noise_root` plus een zin in de tekst; `as_panel` als benoemde stap in `fama_macbeth_fast`. Gedaan. nbconvert offline gedraaid; uitvoer voor/na gelijk op labels en de vierde decimaal van punt (4) na.
**Replicatie.** Oordeel tabel III nu "gedeeltelijk geslaagd" (grootte naast B/M $t = -1{,}38$), verwachte afwijking noemt de kleinere hellingen al; rij bèta+ME+B/M toegevoegd. Gedaan. Correctie op de vorige agent: "De tekens kloppen" was onjuist voor alleen-bèta (0,15 tegen $-0{,}37$), nu "De tekens van grootte en B/M kloppen". Vier getallen in lopende tekst: $p = 0{,}086$ weggelaten (staat in de tabel), de rest draagt het argument. Gedaan.
**Controles.** prose_stats PASS; nb_numbers 14 ongevonden (alle gepubliceerde waarden, eerder 15), geen nieuwe; rewrap en jupytext --sync gedraaid.
Woorden 5651 → 5936.
