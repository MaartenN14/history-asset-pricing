STATUS 04_21_volatiliteit F4T words=5639 prose=PASS open=1 cijfer=- min=-

# Feiten 04_21_volatiliteit (F23)

Gecontroleerd: alle getallen die `tools/nb_numbers.py` meldde (10 stuks), de vijf open
punten uit `notes/rapport-04_21_volatiliteit.md` §F1, alle 20 aangehaalde citatiesleutels
tegen `references.bib`, en de cross-references naar 00_01, 03_10, 02_09, 03_14, 04_22.
Verder is elk getal in Theorie/Simulatie/Replicatie/Oefeningen naast `nb_outputs.py` gelegd;
juiste rijen zijn per sectie samengevat.

## Losse getallen (`nb_numbers.py`-meldingen en open punten §F1)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 143, 148 | $\sqrt{0{,}5}=0{,}71\%$, $\sqrt{1{,}5596}=1{,}25\%$ | juist | handrekening (0,7071 → 0,71; 1,2488 → 1,25), geen cel nodig | geen |
| 2 | 495, 1436 | GSV geven over 1928–1984 $\gamma=-0{,}349$ (werkdocument) | onzeker (F4T: behouden met citatie) | {cite}`GhyselsSantaClaraValkanov2004`; extern gecontroleerd (NBER w10913, JFE 2005): headline $\gamma\approx2{,}6$ over de volledige steekproef bevestigd, PDF van de working paper was niet machineleesbaar zodat het subperiode-cijfer $-0{,}349$ niet paginagewijs is nagekeken; geen tegenspraak gevonden | bij twijfel het cijfer expliciet aan Table 2 (1928–1984, RV-vorige-maand-schatter) koppelen |
| 3 | 894, 899, 858 | "persistentie tussen 0,97 en 1" (origineel-kolom) | juist | algemene karakterisering uit Bollerslev (1986) / Glosten-Jagannathan-Runkle (1993), geen los cijfer geclaimd; consistent met bekende GARCH-literatuur | geen |
| 4 | 900 | $\alpha+\delta=0{,}149$ | juist | cel 10: alpha 0,0363 + delta 0,1130 = 0,1493 → 0,149 | geen |
| 5 | 1320 | $0{,}80\cdot0{,}762=0{,}6096$ (tussenstap) | juist | handrekening, bevestigd door cel 21 (eindresultaten 2,0096/1,1096) | geen |
| 6 | 1389 | $\phi^2+2\alpha^2=0{,}91$ | juist | $0{,}95^2+2\cdot0{,}05^2=0{,}9075\to0{,}91$ | geen |
| 7 | r89–90 (open punt 1) | "19 oktober 1987 ... meer dan een vijfde van haar waarde" | juist | extern, algemeen erkend (S&P 500 −20,5%, DJIA −22,6% op Zwarte Maandag); geen cel of citatie in de tekst, maar geen precies getal wordt beweerd | optioneel: citatie toevoegen voor de volledigheid |
| 8 | r75–76 (open punt 3) | "autocorrelatie van het absolute dagrendement ongeveer 0,30" | juist | `lectures/00_01_rendementen.md` r965: "Die van het absolute rendement is ongeveer 0,30, bij lag 1" | geen |
| 9 | r432–433 (open punt 4) | "de eerste VIX middelde nog Black-Scholes-volatiliteiten" | juist | {cite}`Whaley2000`; extern bevestigd: de VIX van 1993 (VXO) werd berekend uit de impliciete volatiliteiten van acht bijna-atm OEX-opties met het Black-Scholes/Merton-model | geen |
| 10 | r1258–1260 (open punt 5) | MIDAS-gewichtsprofiel wijkt af op 1928–2000, lijkt meer op het gepubliceerde over 1964–2000 | juist | indirect bevestigd door cel 18, kolom "gewicht 1e maand": 1928–2000 0,233 vs GSV-gewicht 0,307 (cel 19); 1964–2000 0,319, dicht bij 0,307 | geen |

## Samengevat per sectie (juiste rijen)

- **Toy-voorbeeld** (r125–180): alle acht getallen in de hand/code-tabel (cel 2) kloppen exact
  (h_1..h_5, E4[h6], Var4, halfwaardetijd).
- **Theorie, kernresultaat** (r296–297): $\phi=0{,}989$, halfwaardetijd 61 dagen — cel 10
  (persistentie 0,9888, halfwaardetijd 61,44).
- **Theorie, RV-meetfout** (r402–403): relatieve standaardfout bij 21 dagen $\sqrt{2/21}\approx31\%$ — nagerekend, klopt.
- **Theorie, risico-rendement** (r524–528): rekenvoorbeeld 700 maanden / bijna 60 jaar bij
  $\sigma=5\%$, $\gamma=2{,}5$, $\mathrm{SD}(V)=0{,}0015$ — nagerekend: $(2\cdot0{,}05/(2{,}5\cdot0{,}0015))^2\approx711\to$ "≈700", $700/12\approx58$ jaar → "bijna zestig jaar", klopt.
- **Theorie, MIDAS** (r545–546): $\gamma=2{,}606$, $t=6{,}710$, 31% op eerste maand — hardgecodeerd
  in cel 18/19 als gepubliceerde GSV-waarden; 31% matcht cel 19 (0,307); headline $\gamma\approx2{,}6$
  extern bevestigd (zie rij 2).
- **Simulatie, GARCH-tracking** (r574–575, 608–609, 636–638): $\rho_1=0{,}277$ theorie vs 0,213
  steekproef, SD($\alpha,\beta$) 0,012/0,015, MSE-fractie GARCH 0,0021 vs rollend-22d 0,0461
  (ratio ≈22×) — alle cel 3/4.
- **Simulatie, γ meten** (r757–758, 827–836): SD ware maandvariantie 0,00148≈0,0015, AR(1)
  RV 0,45, $\hat\gamma_{73j}$ 1,7/2,0/2,2 voor RV/MIDAS22/MIDAS66, RMSE ≈1,3 voor alle vier,
  significant in 46% (73j) en 77% (150j) met ware variantie — alle cel 7/8.
- **Replicatie GARCH/GJR** (r894–901, 911–922): persistentie 0,989/0,983, halfwaardetijd
  61/41 dagen, $\alpha+\delta=0{,}149$ (4× groter dan 0,036), crashdag-vol 2,1%/2,4%,
  rendement −17,4%, z-score −7,2, hoogste vol 7,1% op 1987-10-20 — alle cel 10/11.
- **Replicatie HAR-RV** (r1039–1046): OOS $R^2$ 16–24% (niveau) en 41–48% (log), GJR-GARCH
  wint op alle drie de maten, "vorige maand" enige negatieve OOS-$R^2$ (−0,161) — cel 14.
- **Replicatie GSV** (r1202, 1228–1235, 1264–1265): $\gamma=0{,}19$ ($t=0{,}2$) over 1928–2000,
  rollend 1 mnd 0,45 en 2–6 mnd 0,75–1,0 (alle $t<1$), met GSV-gewichten 0,83 ($t=0{,}8$),
  1964–2000 $\gamma=2{,}85$ ($t=1{,}5$), 1928–1963 negatief (−0,99), zonder 1929–1933
  $\gamma=1{,}97$ ($t=1{,}6$) — alle cel 18/19.
- **Oefeningen 1–4**: alle getallen (2,0096/1,1096; kurtosis 3,162 vs 3,166; $\rho_1,\rho_5$;
  loglik-verschil ≈858, $\nu\approx5{,}94$, kans-ratio 10 miljard → 56 jaar; $\gamma$
  0,51/0,64/1,28/2,06, 11 crisismaanden = 895−884) kloppen exact met cel 21–24.

## Cross-references en citaties

- Ankers geverifieerd: `00-01-rendementen` (r14), `thm-rendementen-merton` (r489 in 00_01),
  `03-10-merton-icapm` (r14 in 03_10), `fig-black-scholes-vrp` (r1113 in 02_09),
  `03-14-roll` (r14 in 03_14), `04-22-risk-management` (r14 in 04_22) — allemaal aanwezig.
- 03_10 r401–403 geeft $\mu_m-r=\gamma\sigma_m^2$, "8% bij $\gamma=2$ en $\sigma_m=20\%$" woordelijk
  zoals in 04_21 r480–481 — naad met 03_10 klopt (representatieve belegger bij constante
  beleggingskansen, geen ICAPM-hedgingterm).
- Alle 20 gecontroleerde citatiesleutels (Engle1982, Bollerslev1986, beide
  AndersenBollerslevDieboldLabys, FrenchSchwertStambaugh1987, GlostenJagannathanRunkle1993,
  beide GhyselsSantaClaraValkanov, Mandelbrot1963, Fama1965, Black1976, RubinsteinLeland1981,
  BollerslevWooldridge1992, Corsi2009, CarrMadan2001, DemeterfiDermanKamalZou1999,
  Whaley2000, BarndorffNielsenShephard2002, GhyselsPlazziValkanov2016, SantaClara2026)
  bestaan in `references.bib`.

`open` = 1 (rij 2, onzeker). F4T: het getal staat met citatie (feitenregel voldaan); de zin noemt nu de schatter ("de variantie van de vorige maand", lezerpunt 13), zodat het cijfer aan één specificatie hangt. Tabelnummer niet toegevoegd omdat het niet paginagewijs te controleren is. Rijen 1 en 3–10: juist, geen actie.
