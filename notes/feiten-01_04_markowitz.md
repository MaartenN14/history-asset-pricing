# Feitencontrole: 01_04_markowitz (Markowitz, Roy en Tobin)

Bronnen: `lectures/01_04_markowitz.md`, uitvoer van het uitgevoerde notebook (via
`tools/nb_outputs.py`), `lectures/00_00_setup.md`, `lectures/00_01_rendementen.md`,
`lectures/01_03_williams_ddm.md`, `lectures/02_08_capm.md`, `references.bib`,
`notes/l4_markowitz_research.md`. Handberekeningen nagerekend met `uv run python`.

| nr | kopje | zin (letterlijk) | wat er staat | wat klopt (met berekening of bron) | ernst |
|---|---|---|---|---|---|
| 1 | Oefeningen, uitwerking ex-markowitz-1 (2) | "de teller $7{,}0625 \cdot 0{,}0822\overline{2} - 0{,}51125 = 0{,}580806 - 0{,}51125 = 0{,}069556$" | teller 0,580806 en 0,069556 | $7{,}0625 \times 37/450 = 0{,}580694$, dus de teller is $0{,}069444$. Met de getoonde 0,069556 komt $0{,}069556/3{,}472222 = 0{,}02003$ uit, niet 0,0200. Met de juiste teller is $\mu_z = 0{,}069444/3{,}472222 = 0{,}020000$ exact, zoals de code geeft. | fout |
| 2 | Replicatie op echte data (oordeel) | "Met een standaardfout van 0,04 is geen van de afzonderlijke verschillen in Sharpe-ratio buiten de steekproef groter dan twee standaardfouten." | geen verschil > 2 SE (= 0,08) | Uit de tabel: minimum-variantie min mean-variance = 0,1653 − 0,0807 = 0,085 (industrieën) en 0,2393 − 0,1037 = 0,136 (25 size/BM); minimum-variantie min 1/N bij 25 size/BM = 0,2393 − 0,1590 = 0,080 > 2 × 0,0396 = 0,079. Alleen de verschillen tussen mean-variance en 1/N (0,077 en 0,055) blijven onder 0,08. | fout |
| 3 | Replicatie (blok "Verschil met het origineel" en vergelijkingstabel) | "DGU gebruiken elf reeksen (tien industrieën plus de markt) tot november 2004 [...] Als tegenhangers gelden S&P-sectoren bij de tien industrieën" | de beschreven DGU-dataset is Industry (N = 11), de vergeleken rij is S&P-sectoren | DGU hebben beide: *Industry* (10 industrieën + markt, 1963-07–2004-11) en *S&P sectors* (N = 11, 1981-01–2002-12) (`notes/l4_markowitz_research.md`, r. 27). De tekst beschrijft de ene en de tabel toont de getallen (0,1876 / 0,3848 / 0,0794) van de andere. Ook "vanaf juli 1963, net als bij DGU" klopt niet voor S&P-sectoren. De directe tegenhanger is DGU's Industry-kolom van tabel 3 (uit het hoofd 0,1353 / 0,2124 / 0,0679, **eerst in het paper nakijken**). Daarmee verandert ook "net als bij DGU van 0,31 naar 0,54" (met Industry: 0,14 naar 0,54). | inconsistent |
| 4 | Replicatie (verwachte afwijking en oordeel) | "In de steekproef belooft mean-variance ver boven 1/N, erbuiten levert zij eronder" | "ver boven" | Industrieën: 0,1848 tegenover 0,1581, een verschil van 0,027, minder dan één SE (0,04). Alleen bij 25 size/BM (0,4022 tegenover 0,1590) is het "ver boven". Het oordeel past niet bij de tabel voor de industrieën. | inconsistent |
| 5 | Overzicht | "Markowitz publiceerde in maart 1952 [...] veertien pagina's in *The Journal of Finance*" | 14 pagina's | `references.bib`: pages 77--91, dat zijn 15 pagina's (91 − 77 + 1). | fout |
| 6 | Overzicht | "vier grafieken, geen data" | vier figuren | Nergens gestaafd (niet in de onderzoeksnotitie). Tellen in het origineel. | onherleidbaar |
| 7 | Intuïtie | "Roy had in de oorlog gediend en schreef, naar eigen zeggen, voor mensen voor wie een slechte uitkomst het einde is." | biografisch feit plus "naar eigen zeggen" | Geen citatie, niet in de onderzoeksnotitie. "Naar eigen zeggen" vraagt om een vindplaats in Roy (1952). (Bevestigt de aanmerking in rating2.) | onherleidbaar |
| 8 | Theorie, Een risicovrij activum | "Sharpe gaf hem in 1966 zijn naam, Roy had hem in 1952 al" | Sharpe noemde de ratio in 1966 | Sharpe (1966) sprak van de *reward-to-variability ratio*; de naam "Sharpe-ratio" kwam later van anderen. Geen citatie voor 1966. Juist is bijvoorbeeld "Sharpe gebruikte hem in 1966; later kreeg hij diens naam". | fout |
| 9 | Theorie, toy tangentportefeuille | "Een $S_{\max}$ van 0,529 ligt iets boven de ongeveer 0,4 per jaar van de Amerikaanse aandelenmarkt over de afgelopen eeuw." | Sharpe-ratio van de markt ≈ 0,4 per jaar | Geen uitvoer en geen citatie. [](#00-01-rendementen) noemt juist "ongeveer 0,6" op jaarbasis (0,04 × √252, r. 450–453, totaal rendement, geen premie). Met de cijfers van L1 (rekenkundig 11,7%, volatiliteit 22,9%) en een T-bill-rendement van rond 3% komt de premie-Sharpe op ≈ 0,37, dus 0,4 is plausibel, maar het getal is hier onherleidbaar en botst zonder uitleg met L1's 0,6. | onherleidbaar |
| 10 | Wat het voorspelt | "De helft van het risico is weg te diversifiëren, de andere helft niet." | de helft | Klopt in standaarddeviatie (19,05% naar 9,53%, factor $\sqrt{0{,}25} = 0{,}5$). In variantie, de maat van [](#eq-markowitz-1n), is 75% weg te diversifiëren en blijft 25% (= $\bar c/\bar v$). De maat wordt niet genoemd. (Bevestigt rating2.) | inconsistent |
| 11 | Theorie, Samengevat | "in het optimum is de covariantie van elk activum met de portefeuille evenredig met zijn verwachte rendement" | evenredig | De theorie zegt terecht "een vaste lineaire functie": $\Cov(R_i,R_p) = \lambda\mu_i + \delta$, en $\delta \neq 0$ (toy bij 10%: $\delta = -0{,}0125$). Evenredig geldt alleen bij $\delta = 0$ of in overrendementen. | inconsistent |
| 12 | Theorie (vanaf eq-markowitz-abcd), oefening ex-markowitz-1 | "$A = \mathbf{1}'\boldsymbol{\Sigma}^{-1}\mathbf{1},\ B = \dots,\ C = \dots$" naast "Activum A alleen levert hetzelfde verwachte rendement met 20% risico" en "$(1{,}94;\; 1{,}13;\; 4)'$, weegt A en B relatief zwaarder" | A, B, C zijn zowel scalars als activa | Twee betekenissen per letter in dezelfde alinea's (ook "$\boldsymbol{\Sigma}^{-1}\mathbf{1}/A$" in de replicatie). Kleiner: $a$ (dosis in de separatiestelling) naast $a_i$ (intercept), $d$ (rampniveau) naast $D$ en $\delta$. $u$ komt maar één keer voor (nut) en botst niet. (Bevestigt rating2.) | inconsistent |
| 13 | Wat er brak, Risico of vergissing? | "Pedro Santa-Clara [...] zegt het zo: de mean-variance-portefeuille wedt erop dat haar geschatte gemiddelden meer weten dan de prijs." | uitspraak van Santa-Clara over mean-variance | [](#00-00-setup) (r. 116–118) citeert alleen "Everything I lost came from thinking I knew something the price did not." De toepassing op de mean-variance-portefeuille is een parafrase van de lecture, niet van Santa-Clara. Formuleren als toepassing van zijn les. | onherleidbaar |
| 14 | Simulatie, bijschrift fig-markowitz-simulatie | "dezelfde gewichten onder de ware momenten, vrijwel altijd onder het ware optimum" | vrijwel altijd | Per constructie *altijd*: onder de ware momenten haalt geen enkele $\mathbf{w}$ een hogere Sharpe-ratio dan $S_{\max}$ (Cauchy-Schwarz, dezelfde redenering als de note "Waarom $D$ positief is"). | inconsistent |
| 15 | Replicatie, na het oordeel | "Daarom bestaan minimum-variantiefondsen en risicopariteitsfondsen [...] als productcategorie, en maximum-Sharpefondsen niet." | er bestaan geen maximum-Sharpe-fondsen | Geen bron; een absolute uitspraak over de fondsenmarkt. Afzwakken of staven. | onherleidbaar |
| 16 | Wat er brak, tip | "Krimp $\hat{\boldsymbol{\mu}}$ naar het gemiddelde over alle activa (Bayes-Stein, zoals in oefening 3)." | Bayes-Stein = krimpen naar het doorsnedegemiddelde | De Bayes-Stein-schatter van Jorion (1986) krimpt naar het verwachte rendement van de *minimum-variantieportefeuille*, niet naar het eenvoudige gemiddelde over de activa. Oefening 3 krimpt naar het doorsnedegemiddelde (James-Stein-achtig). Geen citatie. | fout |
| 17 | Een risicovrij activum, note Hansen-Jagannathan | "blijkt hij gelijk aan de Hansen-Jagannathan-ondergrens $\sigma(m)/\E[m]$ [...] gemiddeld ongeveer $1/(1 + R^{f})$" | $\sigma(m)/\E[m]$ is de ondergrens; $\E[m] \approx 1/(1+R^f)$ | De grens is $\sigma(m)/\E[m] \geq S_{\max}$: $S_{\max}$ is de ondergrens *van* $\sigma(m)/\E[m]$ (05_26 r. 962: "met gelijkheid"). Met een risicovrij activum is $\E[m] = 1/(1+R^{f})$ exact, niet "ongeveer". | inconsistent |
| 18 | (andere lecture) 02_08_capm, toy | "een risicovrije rente van $R^{f} - 1 = 2\%$" (02_08 r. 132) en "C had in L4 de slechtste Sharpe-ratio (0,20 tegen 0,40 voor A en B)" (02_08 r. 298) | CAPM neemt $R^f$ bruto en schrijft L4 Sharpe-ratio's per activum toe | L4 definieert $R^{f}$ netto ("2% is 0,02") en $\boldsymbol{\mu}^{e} = \boldsymbol{\mu} - R^{f}\mathbf{1}$ met netto $\boldsymbol{\mu}$; in 02_08 is $R^f$ bruto. Dezelfde letter wisselt dus tussen de twee lectures. De Sharpe-ratio's per activum (0,08/0,20 = 0,40; 0,12/0,30 = 0,40; 0,02/0,10 = 0,20) kloppen, maar L4 rekent ze nergens uit. Herstellen in 02_08 of in L4 vermelden. | inconsistent |

## Aanmerkingen uit de beoordelingen

- `rating2`: scalars/activa (nr. 12), "de helft van het risico" (nr. 10) en het
  ontbreken van een bron voor Roys oorlogsverleden (nr. 7) bevestigd. De
  opmerking dat 0,165 tegenover 0,158 "een vijfde van de standaardfout" is, klopt
  (0,0072/0,0396 = 0,18). De opmerking dat $R$ in L1 bruto is, klopt (00_01 r. 143),
  maar L4 zegt nu expliciet dat hier netto geldt; zie nr. 18 voor de botsing met 02_08.
- `rating` (eerste ronde): de aanmerkingen over bruto/netto in de Opzet, de
  verwijzing naar [](#00-00-setup) voor Merton, "vijf keer zoveel geschiedenis"
  in oefening 2 en "past bij een twintig jaar langere steekproef" zijn in de
  huidige tekst hersteld en gelden niet meer. De opmerking dat de tabel geen
  gelijke cellen vergelijkt, blijft deels staan en is aangescherpt in nr. 3.

## Gecontroleerd en in orde

- Toy, stap 1–5: $\Sigma_{AB} = 0{,}02$; determinant 0,0032; inverse 28,125 /
  −6,25 / 12,5 / 100; rijsommen (21,875; 6,25; 100), som 128,125 = 41 × 3,125;
  gewichten 7/41, 2/41, 32/41 = 0,1707 / 0,0488 / 0,7805; covarianties allemaal
  0,32/41; $\sigma_{\mathrm{mv}} = \sqrt{0{,}32/41} = 8{,}83\%$; 9/41 = 22% in aandelen.
- $A = 128{,}125$, $B = 7{,}0625$, $C = 0{,}51125$, $D = 15{,}625$, $AC = 65{,}50$;
  $\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu} = (1{,}9375;\ 1{,}125;\ 4)'$; $B/A = 5{,}51\%$.
- Bij $\mu_p = 10\%$: $\lambda = 0{,}368$, $\delta = -0{,}01248$, variantie 0,0243,
  $\sigma = 15{,}59\%$ (22% onder de 20% van A), helling $2\lambda \cdot 0{,}01 = 0{,}0074$.
  Bij 3%: $\sigma = 11{,}39\%$.
- Tangent: $\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^e = (1{,}5;\ 1{,}0;\ 2{,}0)'$, som 4,5,
  gewichten 1/3, 2/9, 4/9; $S_{\max}^2 = 0{,}28$, $S_{\max} = 0{,}529$; $\mu = 8{,}22\%$
  (= 37/450), $\sigma = 11{,}76\%$; $C/B = 7{,}24\%$ bij $R^f = 0$.
- Roy: $(0{,}0822 + 0{,}20)/0{,}1176 = 2{,}40$; grens $1/2{,}4^2 = 17\%$; $\Phi(-2{,}4) = 0{,}8\%$.
- Bruto tegenover netto: $\boldsymbol{\Sigma}$ en $A$ blijven gelijk, $B$ en $C$ veranderen, de rand schuift één op; klopt.
- 1/N-tabel: 5,5% × √12 = 19,05%; bodem $\sqrt{0{,}25} \times 19{,}05 = 9{,}53\%$; na 30 aandelen 9,99%.
- Schattingsfout: $20/\sqrt{100} = 2$ en $20/\sqrt{10} = 6{,}3$ procentpunt;
  $N/T = 10/120 = 0{,}083$ is ≈ 3,9 × de ware $S^2_{\max} = (0{,}5035/\sqrt{12})^2 = 0{,}0211$.
- Chopra-Ziemba 11× en 21× bij risicotolerantie 50: bevestigd in de onderzoeksnotitie.
- Simulatie: 0,50 en 0,47; 0,16 (T = 60) en 0,39 (T = 600 = 50 jaar), overal onder 1/N;
  premies 4,8–9,6% per jaar.
- Replicatie: 757 maanden 1963-07–2026-07; 637 = 757 − 120 maanden buiten de
  steekproef; SE $1/\sqrt{637} = 0{,}0396$; 14,5% tegen 4,3% per maand; 0,081 / 0,158 /
  0,185; 0,165 en 0,239; gat 0,10 en 0,30; DGU-getallen 0,1876 / 0,3848 / 0,0794,
  0,1753 / 0,5364 / −0,0031 en 0,1277 / 0,2090 / −0,0719 gelijk aan de onderzoeksnotitie;
  DGU "twee van de drie negatief" klopt voor de getoonde rijen; 14 modellen, 7 datasets;
  3000/6000 maanden bij N = 25/50.
- Posities: 2103% long, 2122% short, brutopositie 7,5 en 72, turnover 2,0 en 71,7;
  1158 = meer dan 100.000%.
- Oefeningen: instap 9/49, 4/49, 36/49, $\sigma = 0{,}6/7 = 8{,}57\%$, B 8,2% tegen 4,9%;
  zero-beta exact 2% (code); ex-2: 0,294 / 0,230 / 0,149, 1/N 0,46–0,48, 2880 / 3840 /
  3840 maanden, 3840 = 320 jaar; ex-3: 0,239 tegen 0,104, brutopositie 7,6 en 72,
  $\phi = 0{,}5$ Sharpe 0,000 en brutopositie 102.
- Friedman-citaat en "graad diezelfde dag": geverifieerd via KleinDazaMead2013
  (citeert de heruitgave van 1959, p. 382). Markowitz 1999 "equal share": ook in de notitie.
  Roy juli 1952 in Econometrica 20(3): klopt.
- Verwijzingen: alle labels bestaan (01-03-williams-ddm, 00-01-rendementen,
  00-00-setup, 02-08-capm, 05-26-sdf-unificatie, 04-20-voorspelbaarheid,
  05-31-portfolio-choice, 02-05-crsp-tape). L3 zegt inderdaad dat de discontovoet
  beweegt en dat Williams geen theorie van $r$ had; L1 bevat de standaardfout van
  twee procentpunt en de stelling van Merton, zoals hier beweerd. De labels die
  02_08 aanhaalt (cor-markowitz-separatie, eq-markowitz-tangent,
  thm-markowitz-tweefonds, eq-markowitz-foc met $\lambda_m = (A\mu_m - B)/D$,
  ex-markowitz-1 met zero-beta = $R^f$, bias $S^2 + N/T$) bestaan en dragen die inhoud;
  de marktgewichten 1/3, 2/9, 4/9 in 02_08 zijn de tangentgewichten van L4.
