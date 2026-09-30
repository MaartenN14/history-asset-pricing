STATUS 06_34_factor_zoo F4 open=0

# Feiten 06_34_factor_zoo (F23)

Celuitvoer: `nb_outputs` (cel 1 t/m 18) en `nb_numbers` (49 getallen zonder celmatch; allemaal handberekeningen of bronnen, hieronder nagelopen). Externe bronnen opgehaald: HLZ 2016 (pdf, Duke), HXZ 2020 (abstract), McLean-Pontiff 2016 (abstract), ICI Fact Book 2020 (via zoekresultaat), Santa-Clara 2026 (LinkedIn, letterlijk), JKP 2023 (abstract), Chen-Zimmermann (FEDS-pdf). Eigen hercontrole: helling figuur 0,605 (afgerond 0,61 ok).

## Open punten (onjuist, onzeker, niet herleidbaar)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie | status F4 |
|---|---|---|---|---|---|---|
| 1 | 114 | "vier nulsignalen een t boven 2,2 halen" | onjuist | toy-tabel: E heeft t = 2,20, dus niet boven 2,2 | "een t van 2,2 of meer" | opgelost: "een $t$ van 2,2 of meer" |
| 2 | 1017 | "verklaren 7 tot 9% van de daling van 40%" | onzeker (dubbelzinnig) | cel 12 (0,089) en cel 13 (0,067) zijn voorspelde dalingen in procent van het niveau in de steekproef; als aandeel van de daling is het 17 tot 22% | "voorspellen een daling van 7 tot 9%, tegen 40% waargenomen" | opgelost: "voorspellen een daling van 7 tot 9%, tegen 40% waargenomen" |
| 3 | 1113 | publicatieselectie verklaart van de 57% daling "hoogstens een tiende" | onjuist | 6,7 en 8,9 procentpunt van 57,1 is 12 tot 16% (van de 40,5% in de tussenperiode: 17 tot 22%) | "hoogstens een zesde" of "7 tot 9 van de 57 procentpunten" | opgelost: "7 tot 9 van die 57 procentpunten" |
| 4 | 1270-1271 | 57 jaar data is "meer dan de Amerikaanse boekhouddata lang zijn" | onjuist | de OSAP-steekproef in dit college loopt 1963-2024, ruim 60 jaar; CRSP begint in 1926 | "vrijwel de hele lengte van de Amerikaanse boekhouddata sinds 1963" of schrappen | opgelost: "bijna de hele lengte ... sinds 1963" |
| 5 | 1213 | vijfjaarsperioden "1926-1930, 1931-1935" | onjuist (klein) | cel 17: `year // 5 * 5` geeft 1925-1929, 1930-1934 | "1925-1929, 1930-1934, ..." | opgelost: 1925–1929, 1930–1934 |
| 6 | 970 | "zodat de krimpfactor gemiddeld 0,94 is en de gemiddelden maar 9% krimpen" | onzeker | cel 12: gem. krimpfactor 0,935, voorspelde daling 0,089; gemiddeld 0,935 geeft 6,5% krimp, de 9% is de daling van het gemiddelde (ruwe schattingen met hoge waarden krimpen harder); "zodat" klopt dus niet | "0,94 ... en het gemiddelde rendement krimpt met 9%" zonder "zodat" | opgelost: "zodat" weg, twee losse beweringen |
| 7 | 509 | "Daarover verschillen Harvey, Liu en Zhu van Jensen, Kelly en Pedersen" (prior uit gepubliceerde signalen) | onzeker | JKP-abstract bevestigt Bayesiaans tegenover het frequentistische meervoudig toetsen van HLZ, niet specifiek dat het om de prior uit gepubliceerde signalen gaat | herformuleren naar "Bayesiaans of frequentistisch" of met paginaverwijzing | opgelost: frequentistisch (hogere drempel) tegenover Bayesiaans (prior) |
| 8 | 585-586 | FGX vinden "de meeste nieuwe factoren overbodig, maar winstgevendheid niet" | onzeker | FGX 2020 niet opgehaald (geen cel, geen citaat); qua strekking plausibel | bron nakijken of "maar enkele blijven over" | opgelost: "op enkele na", winstgevendheid geschrapt |
| 9 | 1064-1066 | gemiddelde alpha 0,42% "ligt nauwelijks onder het ruwe rendement" (1963-2024) | niet herleidbaar | geen cel met het ruwe gemiddelde over 1963-2024; eigen hercontrole: gemiddeld maandrendement van alle 212 portefeuilles in 1963-2024 is 0,51%, dus de alpha ligt 18% lager | rendementsrij aan cel 14 toevoegen, of "ligt iets onder" | opgelost: vergelijking met ruw rendement geschrapt |
| 10 | 1072 | "De meeste portefeuilles zijn gelijkgewogen" | onzeker | geen cel. Chen-Zimmermann: hoofdportefeuilles volgen de oorspronkelijke artikelen, en ze noemen equal-weighting de gebruikelijke implementatie (r.219-224 in FEDS 2021-037), zonder aantal | telling uit `signaldoc` toevoegen, of "veel portefeuilles" | opgelost: "Veel portefeuilles" |
| 11 | 1107-1108 | "Vijf of zes factoren ... beschrijven een groot deel van de cross-sectie" | onzeker | geen cel; cel 14: 167 van 212 signalen houden een significante alpha tegen FF5 plus momentum, dat is geen groot deel | herformuleren ("verklaren een deel") of schrappen | opgelost: "verklaren een deel ..., al houden de meeste signalen een alpha" |

## Overige rijen (juist), per sectie

| sectie | regels | wat gecontroleerd | oordeel | bron of cel |
|---|---|---|---|---|
| Waar we zijn, Overzicht | 21-64 | 2011 Cochrane, 316 soorten en t > 3 (HLZ), "ruim de helft lager" (MP 58%), 452 anomalieën en meeste verdwijnen (HXZ, 65% bij waardewegingen met NYSE-breekpunten), CZ en JKP repliceren de meeste, 212 voorspellers, Santa-Clara noemt verzwakking open vraag | juist | HLZ-pdf r.16, 60; HXZ-abstract; MP-abstract; Santa-Clara LinkedIn (vraag "Why published anomalies decay" staat onder zijn open vragen) |
| Intuïtie | 68-95 | ongeveer een op de veertig (1/44 = 0,0228 eenzijdig) | juist (afgerond) | normale verdeling |
| Toy, tabel | 122-133 | alle 10 p-waarden (cel 3: gelijk aan de tabel), Holm-, BH- en BHY-grenzen (0,05/(11-j), 0,05 j/10, gedeeld door 2,929), c(10)=2,929, Bonferroni abs(t) > 2,807 | juist | cel 3 |
| Toy, stappen | 138-150 | naief ABCDE (vier onterecht), t>3: A, Bonferroni A (B 0,00527 net boven 0,005), Holm AB (C 0,00693 > 0,00625), BH ABCD (D 0,01429 <= 0,020), BHY A | juist | cel 3 |
| Toy, slot | 211-216 | BH accepteert drie nulsignalen; "een tot vijf voorspellers" | juist | cel 3 |
| Theorie, notatie | 229-255 | delta = 0,5/0,2 = 2,5; FDR <= FWER | juist | handberekening |
| Theorie, Holm en Bonferroni | 259-292 | stelling en bewijs (kleinste ware p-waarde, j* <= M-M0+1, q/M0 en vereniging) | juist | nagerekend |
| Theorie, BHY | 297-325 | c(316) = 6,33, 5%/6,33 = 0,79%, HLZ: 316 factoren uit 313 artikelen, sinds 1967, Bonferroni 1,96 naar 3,78 in 2012 (figuur 3), BHY bij 5% 2,78, vuistregel "ongeveer 2,8" en in de samenvatting 3,0, drempels zijn ondergrenzen | juist | HLZ-pdf r.1143-1180, 16-17; 3,78 = isf(0,025/316) |
| Theorie, selectie | 329-372 | phi(2) = 0,0540, 1-Phi(2) = 0,0228, lambda(2) = 2,37, D(2) = 28,5%, D(4) = 1,4%; bewijs | juist | handberekening, cel 6 en 16 (1,362%) |
| Theorie, MP | 376-417 | 26%, 58% en 32% (= 58-26), 26% als bovengrens voor datamining, 97 voorspellers (replicatieblok r.751) | juist | MP-abstract |
| Theorie, shrinkage | 422-470 | B = 0,5, E = 0,5%, SD = 0,283%, Phi(1,768) = 0,961; tau = 0,2%: B = 0,2 | juist | cel 4 |
| Theorie, JKP | 513-516 | 13 thema's, themagemiddelde naar nul getrokken | juist | JKP-abstract (153 factoren, 13 thema's) |
| Theorie, FF5 en q | 525-580 | FF2015 clean surplus, teken per grootheid, RMW en CMA, Novy-Marx 2013 als voorloper, HXZ 2015 q-model met markt, size, I/A, ROE; propositie: eerste-ordevoorwaarde en rendement nagerekend | juist | handafleiding |
| Theorie, rest | 582-592 | HML overbodig bij FF (2015), NMV 2016 transactiekosten, indexfondsen evenveel van de beurs als actieve fondsen eind 2019 | juist | ICI 2020: 15% voor index, 15% actief |
| Samengevat | 597-609 | 2,8 a 3,8 bij 316; 100% tot 1,4%; 6000 signalen en 2,37; B = 0,5 bij tau = s | juist | bovenstaande |
| Simulatie | 614-735 | 300 x 20 = 6000, 142 gepubliceerd tegen 137 (0,0228 x 6000 = 136,5), gem. t 2,33, 0,44% (0,443), tussenperiode -0,05 (SE 0,031), na 0,015 (SE 0,017), verschil formule-simulatie 0,0049, 26% bij 2,10; figuurtekst 58% bij rond 1 (1,066) | juist | cel 5, 6 |
| Replicatie, periodes | 808-853 | 0,69%, 40%, 57%, SE 0,48 (0,475) in 55 (54,6) maanden, regressie 36%, 54%, verschil 18%, t = -3,85 en -6,49 | juist | cel 8, 9 |
| Replicatie, t-waarden | 879-931 | 186 van 212 (88%), 188 gerapporteerd, rangcorrelatie 0,62, 64 valt af bij t > 3 (186-122), Bonferroni 3,68 en 85, figuurhelling 0,61 (hercontrole 0,605), 66 en 11 na publicatie | juist | cel 10, eigen hercontrole |
| Replicatie, shrinkage | 969-1023 | tau = 0,80%, SE 0,19%, 186 naar 181, 183 gerapporteerd t > 1,96, gem. 4,69, gewicht 0,97 (37,6/38,6), 4,37, 7% | juist | cel 12, 13 |
| Replicatie, alpha | 1064-1078 | 167 van 212, 164 positief, 0,42%; Bonferroni 99 (minder dan de helft), BHY 131, BH 161; na publicatie 10 tot 62, 0,30% = 0,295% | juist | cel 14 |
| Oordeel | 1085-1091 | 40 (36), 57 (54), 18, 12% (= 26/212), 3,68, 65% van 452, 3,78 bij 316 | juist | cel 8-10, HXZ, HLZ |
| Wat er brak | 1102-1135 | 88%, BHY 137, 57%, 11 van 212, MP concluderen dat beleggers over mispricing leren, Santa-Clara-citaat letterlijk | juist (tiende: zie nr 3) | cel 10; MP-abstract; LinkedIn |
| Oefening 1 | 1142-1169 | M = 20: 3,02, Holm A, BH ABC, 0,05/19 = 0,00263, 0,0075 | juist | cel 15 |
| Oefening 2 | 1175-1205 | 2,097 en 1,066, 1,362%, "gemiddeld bijna vier" (hercontrole eigen t in de steekproef: gem. 3,93) | juist | cel 16, hercontrole |
| Oefening 3 | 1233-1238 | 42% en 41%, publicatie-effect verdwijnt | juist (perioden: nr 5) | cel 17 |
| Oefening 4 | 1244-1274 | (1,96/0,5)^2 = 15,4; 36; 57,2; impliciete M = 319 ("ruim 300") | juist (slotzin: nr 4) | cel 18 |

## Cross-refs

| regel | verwijzing | status |
|---|---|---|
| 26 | #05-33-fama-vs-shiller | bestaat (05_33 r.14) |
| 29 | #03-16-vroege-anomalieen | bestaat; 03_16 r.545 verwijst terug naar dit college, r.73, 542 over datamining |
| 299 | #04-25-industrie, thm-industrie-bh | bestaan (04_25 r.14, 551) |
| 526 | #01-03-williams-ddm | bestaat |
| 540 | eq-fama-french-factoren | bestaat (04_18 r.252) |
| 577 | #05-26-sdf-unificatie | bestaat |
| 583 | prop-sdf-unificatie-b-lambda | bestaat (05_26 r.504) |
| 1135 | #06-35-machine-learning | bestaat |
| intern | eq-factor-zoo-*, thm-factor-zoo-*, cor-factor-zoo-selectie, prop-factor-zoo-q | elk label komt in het college voor; ex-labels zijn alleen tekst |
| bib | SantaClara2026, ICI2020 | bestaan in references.bib (SantaClara2026 is een LinkedIn-post; ICI2020 is de 60e editie van het Fact Book) |
