STATUS 05_30_wisselkoersen F4 open=7 punten=15

Methode: `tools/nb_numbers.py` en `tools/nb_outputs.py` gedraaid (output in
`$TEMP/f23-05_30_wisselkoersen-{nums,out}.txt`); elk gemeld getal nagekeken tegen de
celuitvoer. Cross-refs gecontroleerd met `grep -n "(<label>)="` in `lectures/*.md` en, waar
de bewering inhoudelijk specifiek was, met een korte `grep` in het aangehaalde college.
Voor de twee zwaarst wegende open punten (Burnside e.a., Lustig-Roussanov-Verdelhan) is
de NBER-werkpapierversie opgehaald (WebSearch + WebFetch); de PDF's zijn niet machinaal
leesbaar te doorzoeken op tabelinhoud, dus de cijfers blijven onzeker.

## Juiste rijen, samengevat per sectie

| sectie | getallen gecontroleerd | oordeel |
|---|---|---|
| Toy-voorbeeld (r.140-216) | alle 14 waarden in "met de hand"/"code"-tabel (R^f, S'/S, carry, SD's, index 0,8048) | juist, exact gelijk aan cel 2 |
| Theorie, Hoe glad (r.291-358) | a=0,47 bij SR=0,5; index 0,98 en 71% in BCS-rekenvoorbeeld (interne formule, niet de bronvermelding zelf) | juist (wiskundig, hand na te rekenen) |
| Theorie, lognormaal (r.461-509) | v=0,0411, v*=0,0105, premie 0,0153 vs exacte log-premie 0,0152 | juist, consistent met toy (cel 2) |
| Simulatie (r.642-726) | ware ondergrens 0,978; 30/50/100 jaar percentielen; P(grens<0,9)=93%; grens bij SR=0,2 -> 0,87, SR=0,1 -> 0,50, SR<0,07 negatief | juist, exact gelijk aan cel 3 (percentages met de hand nagerekend) |
| Simulatie, peso-note (r.727-810) | P(geen crash) 37%/0,369; theorie 0,115; P(t>2\|geen crash) 8,5%; π=0,0106; (1-π)^360≈2% | juist, exact gelijk aan cel 5 |
| Replicatie, data (r.839-895) | vol. 7% (Canada) tot 12% (Nieuw-Zeeland) | juist (6,89% en 11,67% afgerond) |
| Replicatie, Fama-regressie (r.897-943) | 8/9 hellingen negatief (SEK positief); 7 valuta's verwerpen β=1; gepoold -0,62, t=-4,2; geen \|t\|>2 tegen β=0, JPY -1,96 dichtst bij; R²<1%; carry 1,62x renteverschil | juist, exact gelijk aan cel 8 |
| Replicatie, carry-portefeuilles (r.945-1026) | start feb. 1979, monotoon; P1 -1,9%, P3 1,8%; HML 3,67% (SE 1,22), Sharpe 0,44 (SE 0,15), scheefheid -0,86; crisis -26,6% aug-dec, drawdown -28% (dal jan. 2009); okt. 2008 -11,2% gelijk met juli 1986, okt. 1987 in top 5 | juist, exact gelijk aan cel 9-10 |
| Replicatie, BCS op G10 (r.1038-1080) | SR markt 0,56; index gem. 0,98 (0,975 NZD - 0,991 CAD); SR-2SE -> 0,91; max. SR 1,56 -> 0,996 | juist, exact gelijk aan cel 12 |
| Replicatie, momentum/value (r.1082-1129) | steekproef 1981-2025; Sharpe value 0,47, carry 0,36, momentum 0,07; mom/value corr -0,29; drie gelijk gewogen Sharpe 0,52, vol 4,9%, scheefheid -0,71 | juist, exact gelijk aan cel 13 |
| Replicatie, vergelijkingstabel + "Geslaagd" (r.1130-1153) | 0,54/0,44; 0,98/0,98; 0,44/0,47; 0,32/0,07; hellingen <1, op 1 na negatief; index >0,9 voor elke valuta | juist, exact gelijk aan cel 14 |
| Oefening 1 (r.1206-1240) | Rf*=1,00; +12,5%/-8,33%, gem. +2,08%; log-premie 0,0154 (exact) vs 0,0155 (lognormaal) | juist, exact gelijk aan cel 15 |
| Oefening 2 (r.1242-1281) | index BCS 0,98; 71% bij correlatie nul; SR≈0,1 voor index 0,5 bij G10-vol | juist, exact gelijk aan cel 16 |
| Oefening 3 (r.1283-1323) | 1979-2007: helling -1,01, Sharpe 0,60 (SE 0,20); 2008-2025: helling 1,39 (SE 1,38), Sharpe 0,13 (SE 0,24) | juist, exact gelijk aan cel 17 |
| Oefening 4 (r.1325-1392) | theta grootste gewicht op value; Sharpe train 1,02, test 0,24 vs 0,26 (gelijk) vs 0,18 (alleen carry) | juist, exact gelijk aan cel 18 |
| Cross-refs | `#03-13-equity-premium-puzzle`, `#05-29-opties-crashrisico`, `#04-20-voorspelbaarheid`, `#00-01-rendementen`, `#04-18-fama-french`, `#04-19-momentum`, `#04-22-risk-management`, `#01-04-markowitz`, `#05-31-portfolio-choice` | juist: alle labels bestaan; inhoud van het aangehaalde college komt overeen (HJ-grens in 03-13, putverkoop-crashpremie in 05-29, overlappende waarnemingen in 04-20, "standaardfout van 2%" exact zoals kaart §3 voorschrijft, margin call/verliesspiraal in 04-22, 12-1-regel in 04-19, schattingsfout Σ⁻¹μ (het "Michaud-effect", niet bij naam genoemd in 01-04 maar het mechanisme staat er wel) in 01-04 |

## Open punten (onzeker, met reden)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 355 | "wisselkoersvolatiliteiten van 11,5 tot 12,9% (tabel 1) en indices van 0,98 of hoger (tabel 2)" en lokale Sharpe-ratio's 0,26-0,63 (r.1076) | onzeker (F4: blijft open) | BrandtCochraneSantaClara2006, werkpapierversie 2002; gepubliceerde versie niet ingezien | citeer als "werkpapierversie" of haal de gepubliceerde JF-versie op vóór publicatie |
| 2 | 557-560 | "483 basispunten per jaar meer, met een Sharpe-ratio van 0,54 (tabel 1)... verklaart ongeveer 70%" | onzeker (F4: blijft open) | LustigRoussanovVerdelhan2011, NBER wp14082; poging tot verificatie (WebSearch + WebFetch van de NBER-PDF) leverde geen leesbare tabelinhoud op (PDF niet machinaal doorzoekbaar) | markeer als ongeverifieerd of haal de RFS-gepubliceerde tabel 1 handmatig op |
| 3 | 550-553 | "verschil van tot vijf procentpunt per jaar... risicoaversie rond 100" | onzeker (F4: blijft open) | LustigVerdelhan2007, NBER-werkpapier | zelfde behandeling als 1-2 |
| 4 | 565 | "verklaart meer dan 90% van de verschillen tussen vijf carry-portefeuilles" | onzeker (F4: blijft open) | MenkhoffSarnoSchmelingSchrimpf2012a, werkpapierversie | zelfde behandeling |
| 5 | 600 | "Sharpe-ratio van 0,911 (tabel 2)" | onzeker (F4: blijft open) | BurnsideEichenbaumKleshchelskiRebelo2011, NBER wp14054; poging tot verificatie (WebSearch + WebFetch) leverde geen leesbare tabelinhoud op | zelfde behandeling; dit is de hoogste Sharpe-ratio in het college en verdient prioriteit bij een latere controle |
| 6 | 624 | "Sharpe-ratio van hun portefeuilles gemiddeld met een half" | onzeker (F4: blijft open) | BarrosoSantaClara2015b, uit het abstract; steekproef en tabellen niet ingezien | zelfde behandeling |
| 7 | 593 | "R² van 81% tussen gemiddelde scheefheid en gemiddeld renteverschil (hun figuur 2)" | onzeker (F4: blijft open) | BrunnermeierNagelPedersen2008; parafrase zelf is intern consistent, het cijfer is niet geverifieerd | zelfde behandeling |

Geen onjuiste of niet-herleidbare getallen gevonden. Alle 30 meldingen van
`nb_numbers.py` zijn getoetst: het zijn ofwel statische toy-invoerwaarden (r.145-146, ook
als code-array `m_home`/`m_foreign`) ofwel handberekeningen uit wel-geprinte celgetallen
(bijv. r.1220: 12,5%/-8,33% uit `fx_calm` in cel 15) - beide toegestaan onder H2/H11.

## F4 (2026-09-30)

Geen rij had status fout of niet herleidbaar; de zeven onzekere rijen zijn geen fout en
blijven open tot iemand de gepubliceerde tabellen handmatig naslaat.
- Rij 1 (BCS): tekst scheidt nu het rekenvoorbeeld (0,98/71%) van "hun eigen schattingen"
  (11,5-12,9%, indices >= 0,98); cijfers ongewijzigd, bron nog niet ingezien.
- Rij 2 (LRV): 483 basispunten en "(tabel 1)" geschrapt; Sharpe 0,54 (ook in de
  vergelijkingstabel, codecel) en "ongeveer 70%" blijven onzeker.
- Rijen 3-7: ongewijzigd, onzeker.
