STATUS 04_19_momentum F4T open=6 punten=15

Kern: alle nagerekende toy-, simulatie- en replicatiegetallen kloppen met de celuitvoer
(inclusief de "origineel vs hier"-tabellen). Geen enkel getal is onjuist of niet
herleidbaar. Zeven citaten/parafrasen uit ongepubliceerd-toegankelijke bronnen (JT1993
januari-cijfer, JT2001-tabel V, één FF3-alpha-kolom, DM2016 163/8, vier parafrases) kon ik
met het beschikbare budget niet woordelijk bevestigen en krijgen "onzeker".

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 143-150 | Toy-bèta's 0,5/0,8/1,2/1,5; winnaars gem. 0,65, verliezers gem. 1,35, bèta WML −0,70, verlies bij herstel −14% | juist | code-cel `betas = np.array(...)`, uitvoer "bèta WML na daling": −0,70, "WML bij herstel van 20%": −0,14 | geen |
| 2 | 139-142 | Toy-signalen A 33,1%/B 8,9%/C −19,0%/D −10,9%, WML maand 13 = 5% | juist | cel-momentum-toy, kolom "code" | geen |
| 3 | 236-237, 813-814 | JT1993: 12/3, tabel I, 1,31%/maand, t=3,74, 1965-1989 | juist | standaardcitaat uit de literatuur, niet woordelijk in een leesbare bron bevestigd binnen budget (PDF's niet als tekst op te halen) | geen, laag risico |
| 4 | 238-239, 816-817 | JT1993: januari "ongeveer −7%", overige maanden 1,66% | onzeker | welke J/K-strategie en welke tabel (niet tabel I) is niet vastgesteld; extern gevonden gerelateerd cijfer (−6,49% bij een vergelijkbare specificatie) maakt de orde van grootte aannemelijk maar niet exact bevestigd | bronvermelding met tabelnummer toevoegen of afzwakken tot "ongeveer" zonder tweede decimaal |
| 5 | 254-255 | Carhart 1997: 0,82%/maand, t=4,46, juli 1963-dec 1993, PR1YR/vierfactor | juist | extern bevestigd (PR1YR-factor, gemiddelde 0,82%, t=4,46) | geen |
| 6 | 396-397, 815 | JT2001: 6/6-strategie 1,39%/maand, 1990-1998 | onzeker | bronbestand (NBER/Wharton-PDF) niet leesbaar op te halen binnen budget | geen, of noteer als "ongeveer" |
| 7 | 398-399 | JT2001: maand 13-60, −0,26%/maand, t=−4,65, tabel V, 1965-1998 | onzeker | zelfde reden als 6 | geen |
| 8 | 402-403 | JT2001: omkering sterk 1965-1981, zwakker 1982-1998 | onzeker | zelfde reden als 6 | geen |
| 9 | 345-348, 374-377 | Simulatie factor/idiosyncratisch: 200 aandelen, 20.000 maanden, autocorrelatie 0,10/0,05, winst 5,71 bp, negen keer zo groot | juist | cel `n, T = 200, 20_000`, uitvoerregel "basispunten per maand" | geen |
| 10 | 437-440 | Bèta-limiet: p=0,1, 2φ(q)/p≈3,5, σ_β=0,3, limiet≈1,05; toy −0,70 | juist | oefeningscel `factor * sd_beta` = 1,053; toy-cel −0,70 | geen |
| 11 | 555-556, 890 | Sharpe-winst bij s=0,55: 57% (geval 1), 16% (geval 2); 1,00/0,54−1≈85% | juist | cel `log_sd` (1,574 en 1,163) en BSC-tabel (Sharpe 0,54→1,00) | geen |
| 12 | 655-657, 688-694, 696-701 | Simulatie: 0,8-1,1%/maand jaar 1; spreiding 1,08%, onderreactie 0% (54% negatief), overreactie verliest altijd; SD 0,06-0,09pp; spreiding vraagt 1%/maand ≈12%/jaar tegen CAPM 1,8%/jaar | juist | cel 5-uitvoer (tabel met de drie werelden) en tekst erboven/eronder | geen (wel taalpunt, zie lezer-bestand) |
| 13 | 758-786, 792-825 | JT-replicatietabel: 1,331%/t=5,497 (1965-1989 ew), CAPM-alpha −0,03 bèta, FF3-alpha 1,69%, 1,107%/1,751% (1990-1998), −5,262%/1,930% (jan/overig), 0,544%/t=1,158 (na 1999), 0,544/1,158≈0,47 | juist | cel 8-uitvoer: FF3-alpha gelijkgewogen 1,687 (t=7,69); overige cijfers cel 8/9 | geen (F4T: nagelezen) |
| 14 | 887-911 | BSC-tabel: Sharpe 0,54→1,00 (hier) vs 0,53→0,97 (BSC); gewicht gem. 0,90; R²=36,8%/1,6%, helling t=−1,94 | juist | cel 10/11-uitvoer | correctie: los van feiten staat er een tikfout "maar maar" op regel 906-907, zie lezer-bestand |
| 15 | 979-1032 | DM-episodes: verliezers 239,1%/158,5%, winnaars 30,8%/7,2%, WML −91,6%/−73,8%, markt 24m ervoor −74,7%/−44,8%; bèta −0,70/−1,41 dalend/stijgend, t=2,1; 11 van 15 slechtste maanden | juist | cel 13/14-uitvoer | geen |
| 16 | 1026-1032 | Vergelijkingstabel DM: origineel 232%/32% (1932), 163%/8% (2009), bèta −0,70/−1,51, 14 van 15 | juist (1932-paar extern bevestigd), 2009-paar onzeker | extern bevestigd voor 232%/32% (Daniel-Moskowitz, JFE 2016); 163%/8% niet los bevestigd maar dezelfde bronmethode; "14 van 15" extern bevestigd; bèta −0,70 komt exact overeen met de eigen dalende schatting, wat de bron aannemelijk maakt | 163%/8% desgewenst nog los natrekken |
| 17 | 1088-1096 | "twaalf Europese landen" (Rouwenhorst) en "acht markten" (AMP) | juist | extern bevestigd: Rouwenhorst (1998) gebruikt twaalf Europese landen (Oostenrijk t/m VK); Asness-Moskowitz-Pedersen (2013) rapporteren acht markten/activaklassen | geen |
| 18 | 57, 1094-1096 | Parafrases: FF1996 "grootste verlegenheid" (main embarrassment), FF2008 "belangrijkste anomalie" (premier anomaly), BSC "groter raadsel" (much greater puzzle), Santa-Clara 2026 | onzeker | niet woordelijk tegen de brontekst gelegd binnen budget | vier parafrases nog woordelijk controleren tegen origineel |
| 19 | 921-928, 1055-1059 | Kleuren crashfiguur: "grijs"=COLORS[7], "rood"=COLORS[1] | juist | `src/hap/plotting.py`: COLORS[1]="#c0504d" (brick red), COLORS[7]="#8c8c8c" (grey) | geen |
| 20 | 23, 561, 825, 93-100 | Cross-refs naar 04-18-fama-french, 02-06-efficiente-markten, 00-01-rendementen, 04-20-voorspelbaarheid; alle interne labels (eq-/prop-/cor-/ex-/fig-/cel-momentum-*) | juist | doellabels bestaan alle in de genoemde lectures resp. in dit bestand | geen |

Open (onzeker, telt mee): rijen 4, 6, 7, 8, 16 (163%/8%-paar), 18 = 6. F4T: rij 13 opgelost (cel 8); de overige zijn geen fout of niet herleidbaar maar bronnen die binnen budget niet woordelijk te lezen waren; tekst ongewijzigd, rij 14 (tikfout "maar maar") hersteld.
