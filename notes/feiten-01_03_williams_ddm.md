# Feitencontrole: 01_03_williams_ddm

Bronnen: `lectures/01_03_williams_ddm.md`, notebookuitvoer (`tools/nb_outputs.py`),
eigen herberekening op `hap.data.shiller()` (maandreeks 1871-01 t/m 2026-09,
decemberwaarnemingen 1871–2025), en de lectures 00_00, 00_01, 01_02, 01_04, 03_15,
03_16, 04_20, 05_33.

| nr | kopje | zin (letterlijk) | wat er staat | wat klopt (met berekening of bron) | ernst |
|---|---|---|---|---|---|
| 1 | Hoe het getoetst wordt: de prijs-dividend-ratio | "in de Amerikaanse data van 9,9 in december 1917 tot 85,6 in december 1999." | maximum PD = 85,6 in dec 1999 | 85,6 is het maximum van het regressiepanel (t/m 2015; exp(4,4497) = 85,6). In de volledige decemberreeks die het notebook laadt, is het maximum 86,2 in **december 2025** (80,3 in 2024). Het minimum 9,86 in dec 1917 klopt. Het Overzicht ("van 10 tot 86") klopt met 9,9–86,2. | fout |
| 2 | Simulatie | "Met een halve eeuw data zit een analist er dus tot een factor drie naast, zonder iets fout te doen." | fout t.o.v. de waarheid tot factor 3 | Bij T = 50: 5e pct 12,51, 95e pct 40,75, waarheid 19,50. Fout naar boven 40,75/19,50 = 2,09; naar beneden 19,50/12,51 = 1,56. Factor ≈3 (40,75/12,51 = 3,26) is de breedte van het interval, niet de afstand van een analist tot de waarheid. (Bevestigt rating2.) | fout |
| 3 | Theorie, tip na Campbell-Shiller | "Het dividendrendement van de Amerikaanse markt daalde sinds 1990 van ruim 3% naar rond 1,5%. Onder Williams' lezing is $g$ dan met anderhalf procentpunt gestegen." | D/P 1990 ≈ 3%, nu ≈ 1,5%; daling 1,5 pp | Shiller-data: dec 1990 3,68% (jaar 1990: 3,24–3,88%); dec 2025 1,16%, 2026 1,10–1,21%. Daling ≈ 2,5 procentpunt, niet 1,5. "Rond 1,5%" gold rond 2020–2023, niet aan het eind van de reeks. | fout |
| 4 | Waar we zijn in het verhaal | "Cowles liet zien dat beleggingsadviseurs de markt niet verslaan, Kendall dat weekkoersen geen patroon hebben." | Kendall: geen patroon | L2 (01_02_bachelier, r. 1235–1238): "Dat Kendall nulcorrelaties vond, is een hardnekkig misverstand: zijn waarden liepen van −0,013 (olie) tot 0,301 (beleggingsfondsen)", gemiddeld ≈ 0,13; hij schreef alleen dat ze te zwak waren om mee te voorspellen (ook L2 r. 64–65). (Bevestigt rating2.) | inconsistent |
| 5 | Replicatie, warning | "de log-prijs-dividend-ratio van het ene jaar hangt met een autocorrelatie van 0,91 samen met die van het volgende." | AR(1) = 0,91 | Niet in het notebook. Nagerekend: 0,908 op de volledige decemberreeks 1871–2025, maar 0,885 op 1871–2015, de steekproef van de regressie waar de warning over gaat. | onherleidbaar |
| 6 | Hoe het getoetst wordt, note Campbell-Shiller | "rond de gemiddelde prijs-dividend-ratio, die ongeveer 26 is." | gemiddelde PD ≈ 26 | Niet in het notebook. Decemberreeks 1871–2025: rekenkundig gemiddelde 29,7, meetkundig (exp van gem. log) 26,2, mediaan 23,7; regressiesteekproef 1871–2015: 27,4 resp. 24,7. Alleen het meetkundig gemiddelde over de hele reeks geeft 26. ρ = 26/27 = 0,963 ≈ 0,96 klopt dan (en sluit aan bij 04_20, ρ = 0,96). | onherleidbaar |
| 7 | Simulatie | "Toch loopt het interval tussen het 5e en het 95e percentiel van ongeveer 13 tot ongeveer 40" | 13 tot 40 | Uitvoer 12,508 en 40,752; 40,75 rondt af op 41, niet 40. Twee alinea's later staan dezelfde getallen als 12,5 en 40,8. (Bevestigt rating2.) | inconsistent |
| 8 | Wat er brak, en wat daarna kwam | "Ook de scheefheid uit de simulatie speelt in dat debat mee: in [](#03-15-shiller-excess-volatility) is zij een verweer tegen Shillers variantiegrenzen." | 03-15 gebruikt de scheefheid als verweer | 03_15 bevat geen scheefheid of convexiteit (grep op "scheef", "convex", "skew", "hyperbool": geen treffers). De drie kritieken daar zijn Flavin (kleine steekproeven), Kleidon (niet-stationariteit) en Marsh-Merton (dividend smoothing). | inconsistent |
| 9 | Opzet en aannames | "$R$ is bruto en $r$ netto, zoals in de notatie van de [inleiding](#index)." | notatie staat in index | `index.md` bevat geen notatietabel; de tabel ($R$ bruto, $r$ netto) staat in `00_00_setup.md` (label `00-00-setup`), r. 158–170. | inconsistent |
| 10 | Opzet en aannames | "Voor Amerikaanse aandelen ligt hij rond 7% per jaar, reëel." | discontovoet = verwacht netto rendement ≈ 7% | 7% is het log-gemiddelde (6,82%). De lecture definieert $r$ als verwacht *netto* (simpel) rendement en zegt zelf in de Simulatie dat dat ≈ 8,4% is (6,82 + 17,6²/200). | inconsistent |
| 11 | Replicatie, figuurbijschrift en zin erna | "De linkerwolk heeft geen richting" / "links geen helling, rechts een duidelijk dalende." | geen helling in het dividendpaneel | Coëfficiënt +0,015 (t = 1,63); de tekst zegt zelf (r. 998): "Het teken van de dividendcoëfficiënt wijst wel de kant op die Williams nodig heeft", en op 5 jaar is hij significant (t = 2,02). "Zwakke, niet-significante positieve helling" klopt; "geen helling" niet. | inconsistent |
| 12 | Theorie (inleiding en Opzet), Wat er brak | "daaruit met één aanname het model van Williams" (r. 233) / "Het model van Williams voegt er twee aannames aan toe" (r. 255) / "Het *model van Williams* voegt de aanname van een constante discontovoet toe" (r. 297) | aantal aannames van het model | Overzicht, Opzet (r. 255) en Samengevat noemen twee aannames (constante $r$ én transversaliteit); r. 233, r. 297 en r. 1145 ("voegt er een constante $r$ aan toe") noemen er één. De vaste naam "model van Williams" dekt zo niet steeds hetzelfde. | inconsistent |
| 13 | Intuïtie, note | "Het boek werd in de jaren vijftig herontdekt, toen Gordon en Shapiro de oneindige som tot één breuk samentrokken." | de gesloten vorm is van Gordon en Shapiro | Williams (1938) gaf zelf al gesloten vormen voor een eeuwig constant groeiend dividend; de gangbare toeschrijving is dat Gordon het model populariseerde, niet dat hij de breuk als eerste afleidde. Ook "Williams verkocht in 1938 nauwelijks exemplaren" staat zonder bron. Niet te controleren met de bronnen in het project; te verifiëren in Williams (1938). | onherleidbaar |
| 14 | Intuïtie | "Over de discontovoet schreef hij vrijwel niets: hij nam hem als gegeven." | Williams zweeg over de discontovoet | Williams (1938) besteedt zover ik weet hoofdstukken aan de rente en haar verwachte verloop, en bespreekt een risico-opslag (die hij bij spreiding overbodig achtte). "Nam hem als gegeven in de waardering" klopt; "schreef vrijwel niets" is waarschijnlijk te sterk. Geen citatie; te verifiëren. | onherleidbaar |
| 15 | Wat er brak, en wat daarna kwam | "De PVGO liet zien dat groei en waarde niet hetzelfde zijn, een onderscheid dat in [](#03-16-vroege-anomalieen) empirisch terugkomt." | 03-16 behandelt het PVGO-onderscheid | 03_16 noemt PVGO niet; het gebruikt het Gordon-model uit deze lecture (Berk: marktwaarde als maat voor de discontovoet) en E/P- en B/M-portefeuilles. Het value-effect komt terug, het PVGO-mechanisme niet. | inconsistent |

Buiten deze lecture, ter informatie: 04_20 r. 26 spreekt van "de identiteit van
Williams"; deze lecture houdt "boekhoudkundige identiteit" en "model van
Williams" gescheiden.

## Beoordeling van eerdere aanmerkingen (alleen feitelijk)

- rating2, Kendall: bevestigd (nr 4).
- rating2, factor drie: bevestigd (nr 2).
- rating2, 13/40 tegenover 12,5/40,8: bevestigd (nr 7).
- rating2, 0,91 niet berekend: bevestigd; het getal hoort bij de volledige reeks,
  niet bij de regressiesteekproef (nr 5).
- rating2, 0,15 + 0,38 log-punt telt niet op tot 1: geen fout. De rest zit in de
  verdisconteerde prijs-dividend-ratio na tien jaar; "ruim twee keer zoveel"
  (0,375/0,150 = 2,5) klopt.
- rating (eerste ronde): "anderhalve tiende procentpunt", de onbenoemde
  notatiewissel, de verwijzing naar L2 voor de standaardfout van 2%, "verderop in
  deze lecture" bij Campbell-Shiller, "twintig tot dertig jaar", "niet 25% maar
  100%" en de log-kalibratie zijn in de huidige tekst hersteld; ze gelden niet
  meer.

## Gecontroleerd en in orde

- Toy: $d_1..d_3$ = 1,10 / 1,21 / 1,331; contante waarde 3,00; $d_4$ = 1,39755;
  eindwaarde 27,951 (t=3) en 21,00 (t=0, exact: 1,331 × 21 = 27,951);
  $p_0$ = 24,00; aandeel 87,5%. Alles gelijk aan de uitvoer.
- Duration: $(1+r)/(r-g)$ = 1,10/0,05 = 22; $(1+2+3+21\times25)/24$ = 22,1 ≈ 22.
- Gevoeligheidstabel: 21,00; 26,25 (+25%); 26,50 (+26,2%); 17,50 (−16,7%); een
  fout van 1 pp is 20% van $r-g$ = 5 pp. Rooster: diagonaal 20,80–21,00–21,20,
  bereik 14,86–35,33 (uitvoer).
- Bel: ln 2/ln 1,10 = 7,3 jaar ("ruim zeven"); ln 2/ln 1,05 = 14,2 ("veertien").
- CAPM "zesentwintig jaar later": 1938 + 26 = 1964 (Sharpe).
- PVGO: $g$ = 5%, $d_1$ = 2, prijs 40, $e_1/r$ = 30, PVGO 10 = een kwart; bij
  ROE 8%: −2,73.
- Kalibratie: 154 waarnemingen, 1,61% (sd 11,5%, SE 0,93 pp), 6,82% (SE 1,42 pp);
  $r-g$ = 5,21 pp; PD = 1,0161/0,0521 = 19,50. Rekenkundige correctie:
  1,61 + 0,66 = 2,27 ≈ 2,3; 6,82 + 1,55 = 8,37 ≈ 8,4; verschil 6,10; ratio
  1,0227/0,061 = 16,8 ≈ 17.
- Standaardfout van 2%: 20/√100 = 2 pp, zoals afgeleid in 00_01 (r. 465–509).
- Simulatie: SE van $\hat g$ bij T = 50 = 1,63 pp; T = 100: 14,10–30,77 ("14,1
  tot 30,8", verhouding 2,18 = "ruim een factor twee"); scheefheid 35,9% onder
  tegen 109% boven (verhouding 3,0).
- Replicatie: 145 waarnemingen 1871–2015; dividendgroei 0,0150 (t = 1,63,
  R² 0,054); rendement −0,0375 (t = −2,21, R² 0,117); tabel en tekst (0,015; 0,05;
  −0,038; 0,12; R² ≈ 5% en 12%) kloppen. 10 × 0,015 = 0,15 en 10 × 0,0375 = 0,375
  log-punt; 20 × e = 54,4; 145/10 ≈ 14 en 71/10 ≈ 7 onafhankelijke perioden.
- Oordeel "Geslaagd": de verwachting (dividend niet significant, rendement
  negatief en significant, R² rond 0,10) komt uit.
- CAPE: −0,0592, t = −4,52, R² 0,240 (2,06 × die van de PD-regressie), n = 135,
  dus start 1881.
- Oefeningen: instap 17,3333 / 20,3333 / 85,2% / −15,3%; $r-g$ van 0,05 naar
  0,06 is een vijfde groter. Bel: $p^f_0$ = 41,20, PD 20,6; kruising in jaar 30
  (10 × 1,08³⁰ = 100,6 > 99,0; jaar 29: 93,2 < 96,1). PVGO: −13,89; $e_1/r$ =
  55,56; asymptoot $b$ = 0,09/0,12 = 0,75 (raster 0,745). Oefening 3: −0,063
  (t = −3,50), 0,026 (t = 2,02), 5 × 0,026 = 0,13 en 5 × 0,0446 = 0,22.
- Verwijzingen: de labels 01-02-bachelier, 00-01-rendementen,
  03-15-shiller-excess-volatility, 03-16-vroege-anomalieen,
  04-20-voorspelbaarheid, 05-33-fama-vs-shiller, 01-04-markowitz en index
  bestaan. 01_02 gebruikt kleine letters als logs en $r$ als logrendement
  (r. 244), zoals hier staat. 04_20 bevat de Campbell-Shiller-afleiding
  (ρ = 0,96) en de kritiek op de $t$-waarden (Stambaugh, Hodrick, Valkanov).
  05_33: Nobelprijs oktober 2013 voor Fama, Hansen en Shiller. 01_04 zegt, net
  als deze lecture, dat prijzen vooral bewegen doordat $r$ beweegt, en dat
  Williams elk aandeel apart bekeek.
- Gordon (1959): cross-sectie van vier bedrijfstakken in 1951 en 1954; klopt
  met de gangbare beschrijving van het artikel.
