STATUS 06_35_machine_learning F4 open=0 punten=15

# Feiten 06_35_machine_learning (F23)

Bronnen: celuitvoer (nb_outputs), handberekening, externe abstracts (GKX, Avramov-Cheng-Metzker). Het GKX-pdf was via WebFetch niet leesbaar; GKX-tabelgetallen zonder cel blijven dus "onzeker" of "juist (geheugen)". Alle cross-refs bestaan (onderaan).

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 21, 51-54 | GKX: bijna honderd karakteristieken, tienduizenden aandelen, 30 jaar schatten (18+12), 30 jaar testen (1987-2016) | juist | GKX (94 karakteristieken, 1957-2016); niet herlezen | - |
| 2 | 53 | dertien voorspelmethoden | opgelost F4: 'dertien' geschrapt, nu 'een reeks voorspelmethoden, van OLS tot netwerken met vijf verborgen lagen' | uit geheugen (OLS, OLS-3, PLS, PCR, ENet, GLM, RF, GBRT, NN1-5 = 13) | bevestig in GKX of schrap "dertien" |
| 3 | 54-56 | Santa-Clara: machines voorspellen twee keer zo goed als lineaire modellen, dankzij niet-lineariteit | opgelost F4: toegeschreven aan GKX-abstract ('in sommige gevallen verdubbelde'), Santa-Clara-citaat hier geschrapt | GKX-abstract zegt "doubling the performance of regression-based strategies"; Santa-Clara zelf niet op te halen | toeschrijven aan GKX of bron nalopen |
| 4 | 108-113 | Santa-Clara vraagt of voorspellingen werken na publicatie, op schaal, na kosten, bij handelende machines | afgewezen F4: parafrase van de geciteerde bron (LinkedIn-post, references.bib), geen getal; blijft als toegeschreven vraag | bron niet op te halen | nalopen |
| 5 | 67, 443-469 | KPS: vier IPCA-factoren verklaren beter dan bestaande modellen; alpha's klein en insignificant | opgelost F4: 'vier' vervangen door 'een paar IPCA-factoren' | werkdocument-samenvatting; niet nagelezen | aantal factoren in KPS (JFE 2019) controleren |
| 6 | 272-295 | bias-variantie-decompositie; OLS-variantie sigma^2 P/n; E[R2_OOS] ongeveer R2pop - (1-R2pop) P/n | juist | afleiding (benadering) | - |
| 7 | 289-292 | 0,5% per maand, P/n_eff = 0,5%; 920 voorspellers -> 184.000 | juist | 920/0,005 = 184.000; 920 = 94 x 9 + 74 | - |
| 8 | 146-186 | toy: z1 = 16, z2 = -3, X'X = 10 I, OLS 1,6/-0,3, SSR 3,5 van 30, R2 88%, ridge 0,8/-0,15, LASSO 1,1/0, EN 0,55/0 | juist | handberekening + cel 2 (asserts) | - |
| 9 | 216-222 | boom splitst op x1 <= -0,5; -2,5 en 1,67 | juist | cel 2 | - |
| 10 | 216-218 | Lasso alpha = lambda/n (alpha=1) | juist | sklearn-doelfunctie 1/(2n) | - |
| 11 | 321-344 | gesloten vorm en bewijs (soft-thresholding, ridge-factor d/(d+lambda2)) | juist | nagerekend | - |
| 12 | 353-357 | lambda* = sigma^2/beta^2; 100 bij ruis 3, gewicht 0,3 | juist | cel 18 (lambda* = 100) | - |
| 13 | 381-386 | variantie gemiddelde van B bomen = rho s^2 + (1-rho)s^2/B; bij rho 0,5 minstens de helft | juist | standaardresultaat | - |
| 14 | 392-398 | NN3 ruim 30.000 parameters; R2 piekt bij drie lagen | juist | 920x32+32+32x16+16+16x8+8+9 = 30.145; GKX Tabel 1 NN3 0,40 hoogst | - |
| 15 | 394-396 | "Early stopping is ook krimp, want de gewichten beginnen bij nul" | opgelost F4: 'beginnen dicht bij nul' | startwaarden zijn klein en willekeurig, niet nul | "beginnen dicht bij nul" |
| 16 | 364-366 | GKX: validatie 1975-1986, test 1987-2016 | juist | GKX (18/12/30 jaar) | - |
| 17 | 423-432 | GKX Tabel 1: -3,46, 0,16, 0,11, 0,26, 0,33, 0,34, 0,40, 0,39 | juist (geheugen) | GKX Tabel 1 (OLS -3,46; OLS-3 0,16; ENet 0,11; PCR 0,26; RF 0,33; GBRT 0,34; NN3 0,40; NN4 0,39); pdf niet leesbaar | - |
| 18 | 426, 432, 1084-1085 | Sharpe long-short waardegewogen OLS-3 0,61, NN4 1,35 | opgelost F4: juist (geheugen GKX tabel 7), consistent met GKX-abstract 'doubling'; 1,35/0,61 = 2,2 | geen cel; GKX Tabel 7, niet herlezen | nalopen |
| 19 | 436-437 | NN4-Sharpe "ruim twee keer" OLS-3 | juist | 1,35/0,61 = 2,2 (afhankelijk van nr 18) | - |
| 20 | 1291-1293 | netwerkportefeuilles draaien elke maand meer dan eigen omvang om; EW-Sharpe 2,45 -> 1,69 zonder kleinste aandelen | opgelost F4: omzet en 2,45 -> 1,69 geschrapt; vervangen door ACM-abstract (winst kleiner zonder kleinste aandelen) | geen cel; GKX/Avramov niet herlezen | bron en tabel noemen |
| 21 | 1294-1296 | Avramov-Cheng-Metzker: winsten zitten in moeilijk verhandelbare aandelen | juist | abstract Management Science 2023: "extract profitability from difficult-to-arbitrage stocks ... excluding microcaps ... attenuates profitability" | - |
| 22 | 1101-1104 | ACM: extra voorspelbaarheid klein waar handel goedkoop is | juist (vrije parafrase) | zelfde abstract | - |
| 23 | 475-528 | KNS: SDF, posterior (Sigma+gamma I)^-1 mu, bewijs, component-krimp lambda/(lambda+gamma) | juist | afleiding nagerekend | - |
| 24 | 534-535 | verwachte kwadratische Sharpe van component j = kappa^2 lambda_j / tau | juist | uit prior var(mu_P,j) = kappa^2 lambda_j^2/tau; kappa^2 = verwachte kwadratische max-Sharpe | - |
| 25 | 541-557 | ridge op prijsfouten; cs-R2 = 1 - e'e/mu'mu | juist | afleiding; matcht cs_r2 in cel 13 | - |
| 26 | 569-601 | Martin-Nagel: posterior = ridge, ongeleerd deel 1/(1 + tNg/(sigma^2 J)); 2% bij J=10, 44% bij J=400 | juist | 1/51 = 1,96%; 1/2,25 = 44,4%; tabel cel 8 (0,020 en 0,444) | - |
| 27 | 635-650 | sim: 500 aandelen, 180 maanden, 20 karakteristieken, P = 40, 108/36/36 | juist | code cel 3 | - |
| 28 | 792-800 | lineaire binnen half procentpunt (max 0,41), bomen tot 0,6 (0,55), NN tot 1,1 (1,08); niet-lineair hooguit half procent voor lineaire (0,18-0,54); populatie 3,3-3,7%; boosting meeste | juist | cel 4, 6 | - |
| 29 | 802-807 | 54.000 trainingswaarnemingen; populatie-R2 1,4% tot 5,0% lineair | juist | 108x500; cel 4 (1,38 en 4,96) | - |
| 30 | 907-909 | F-toets 55% tussen J/N 0,1 en 0,4; 15% bij 0,8; ongeleerd 2% -> 44% | juist | cel 8 (0,54/0,55/0,55; 0,15) | - |
| 31 | 915-918 | OLS-R2 -1,8% -> -50%; ridge tot -19%; 700 economieen, nooit ridge > 0 | juist | cel 8 (-1,79; -49,999; -19,21; fractie 0,0; 7x100) | - |
| 32 | 988 | ruim 134.000 signaal-maanden; 212 signalen | juist | cel 10 (134,518) | - |
| 33 | 1029 | voorspellingen januari 1990 - november 2024 | juist | cel 11 | - |
| 34 | 1082-1083 | R2 lineair 2,00 (OLS), beste boom 2,36 (RF); Sharpe 0,78 en 0,78 | juist | cel 12 (1,996; 2,357; 0,778; 0,776) | - |
| 35 | 1087-1092 | bomen verslaan OLS met ruim een derde procentpunt; DM-t 0,7; na 2005 onder OLS | juist | cel 12 (0,361; 0,339; DM 0,712; 2005-2024: RF 1,025 en boosting 1,062 < 1,097) | - |
| 36 | 1096-1098 | Sharpe ongeveer 0,78, se 0,17, hist. gemiddelde 1,32 | juist | cel 12 (0,763-0,779; 0,173; 1,319) | - |
| 37 | 1104-1106 | na 2005 alle getallen lager, ook EW-Sharpe | juist | cel 12 (EW 2,40 -> 1,55) | - |
| 38 | 1109-1111 | 158 signalen met volledige reeks | opgelost F4: print(H) toegevoegd aan cel 13; uitvoer 158 | geen cel drukt H of 158 af | print(H) toevoegen of getal schrappen |
| 39 | 1171-1176 | kappa 0,133; cs-R2 39% en 40%; ongekrompen -170 | juist | cel 13 (0,388; 0,403; -170,398) | - |
| 40 | 1178-1181 | Sharpe 13,5 / 4,3 / 2,32 / 2,07; se 0,24 | juist | cel 13 (13,514; 4,259; 2,319; 2,065); 0,24 nagerekend (0,2435) | - |
| 41 | 1182-1183 | verschil tussen de twee methoden is ruis (se van een enkele Sharpe als maat) | opgelost F4: 'verschil van 0,25 van dezelfde orde als de se van een enkele Sharpe; daling vele malen groter' | se van het verschil van twee sterk gecorreleerde reeksen niet berekend | "van dezelfde orde als de se van een enkele Sharpe" of het verschil berekenen |
| 42 | 1263-1268 | K=4: PC 0,26 (0,262), signalen 0,04 (0,039); Sharpe 1,72 en 0,78 | juist | cel 14 | - |
| 43 | 1263-1264 | 0,26 "bijna twee derde" van 0,40 | juist | 0,262/0,403 = 0,65 | - |
| 44 | 1283 | GKX 0,40% tegen -3,46% | juist | zie nr 17 | - |
| 45 | 1328-1352 | oefening 1: ridge 0,4/-0,075; LASSO 1,4/-0,1; drempels 3 en 16 | juist | cel 16; handberekening | - |
| 46 | 1413-1418 | oefening 2: -14.000% bij P=T (-14.541), -24% bij P/T=10, Sharpe ridge 0,06 -> 0,13 | juist | cel 17 (-14541,674; -24,297; 0,061; 0,134) | - |
| 47 | 1459-1462 | oefening 3: 10/110 = 0,09; MSE 0,90 -> 0,08 | juist | cel 18 (0,9000; 0,0818; MC 0,8972) | - |
| 48 | 1493-1497 | oefening 4: 15.000 waarnemingen; -16%, ridge -7%, LASSO -1,8%; populatie 5,4%; andere twee OLS rond nul, LASSO 2,2% en 1,2% | juist | cel 19 (-16,26; -6,99; -1,76; 5,41; 2,15; 1,21) | - |
| 49 | 1471 | vergelijking met -3,46% van GKX | juist | zie nr 17 | - |
| 50 | 1302-1308 | sterkste GKX-voorspellers: kortetermijnomkering, momentum, liquiditeit, volatiliteit | juist | GKX-abstract (momentum, liquidity, volatility; omkering uit GKX-tekst) | - |

Open (onjuist + onzeker + niet herleidbaar): nr 2, 3, 4, 5, 15, 18, 20, 38, 41 zijn onzeker; nr 4 en 3 tellen als een bronpunt (Santa-Clara), zodat open = 8 (2, 3+4, 5, 15, 18, 20, 38, 41). Onjuist: geen.

## Cross-refs

| ref | status |
|---|---|
| #06-34-factor-zoo (r. 24, 1107, 1280) | bestaat; 06_34 bespreekt verval na publicatie (r. 38, 58) |
| #04-20-voorspelbaarheid (r. 26) | bestaat |
| #00-01-rendementen (r. 293) | bestaat |
| #05-26-sdf-unificatie (r. 476) | bestaat |
| eq-voorspelbaarheid-oos (r. 404, 1033) | bestaat (04_20 r. 489); noemer is het historische gemiddelde, zoals de tekst zegt |
| eq-voorspelbaarheid-ct (r. 1417) | bestaat (04_20 r. 530); "kleine R2 is veel waard bij kleine Sharpe" klopt |
| eq-sdf-unificatie-b-lambda (r. 494) | bestaat (05_26 r. 509); mu = -Cov(F,m) = Sigma b sluit aan op lambda = -Cov(f,m) |
| #06-36-inelastische-markten (r. 1321) | bestaat |
| interne eq-/prop-/fig-labels | alle gedefinieerd in dit college |
| citekeys | GuKellyXiu2020, SantaClara2026, AvramovChengMetzker2023, KellyMalamudZhou2024 staan in references.bib; overige niet gecontroleerd |

Na F4: alle open rijen opgelost of afgewezen (nr 4 met reden); open = 0.
