STATUS 05_32_intermediaries F4 open=0 punten=15

# Feiten 05_32_intermediaries

Gecontroleerd: alle getallen die `tools/nb_numbers.py` meldt (tegen `tools/nb_outputs.py`,
zie `$TEMP/f23-05_32_intermediaries-nums.txt` en `-out.txt`) en de zeven open punten uit
`notes/rapport-05_32_intermediaries.md` §F1. Externe bronnen alleen voor die open punten en
voor het ene getal zonder cel (r.59).

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 122–136 | Toy-stappen (schok, $E=8$/$A=98$, $\eta=8{,}16\%$, $S_1=18$, verlies $0{,}72$, $E=7{,}28$, $S_2=6{,}48$; margespiraal $S_1=34$, verlies $1{,}088$, $E=6{,}91$, balans $62{,}91$, $S_2=7{,}62$) | juist | `cel-intermediaries-toy` (tabel met de hand/code, exact gelijk) | — |
| 2 | 184–192 | Prijsdaling 3,35% en 4,12%; leverage na afloop 10 vs. 8; eigen vermogen 31% lager | juist | cel 2 output (3.347%, 4.120%, E=6.935/10=31%) | — |
| 3 | 271–273 | $G'\approx0{,}36$ (toy-voorbeeld), impact $0{,}9\%\to1{,}35\%$ | juist | interne herleiding uit toy-getallen (80×9/2000=0,36) | — |
| 4 | 314 | $K_0/h_0=12{,}5$ bij $z=13$ | juist | BP-cel, `K0=1.0, h0=0.08` | — |
| 5 | 432–434, 499–500, 529–532, 589 | HK-premiecijfers: 5,8% bij $\eta=0{,}5$; kritieke $\eta=0{,}198$; 7,6%→27,1% van $\eta=0{,}4\to0{,}2$ | juist | cel 6 output (`eta_crit=0.198`, tabelwaarden 0.058/0.076/0.271) | — |
| 6 | 554–555, 601–602 | HKM: AR(1)-coëfficiënt 0,94 per kwartaal; bèta's op FF25 gemiddelde 0,07, sd 0,11 | juist | extern bevestigd (NBER w21920/JFE-versie, meerdere onafhankelijke treffers) | — |
| 7 | 649–684 | Simulatie: $\lambda=2\%$ in de helft van de steekproeven, $\lambda=7\%$ vrijwel altijd, nutteloze factor 27,5% (~28%) vals significant, 10% i.p.v. 5% zonder ware prijs | juist | cel 8 output | — |
| 8 | 713, 720–722, 753–755 | Kapitaalratio: minimum 2,23% feb 2009; jaargemiddelde 8,2%→4,1% (2006→2008); correlatie −0,33 (Baa) / −0,14 (TED) | juist | cel 10 output | — |
| 9 | 72–73 | Gorton-Metrick: gemiddelde haircut van 0% (begin 2007) naar bijna 50% (eind 2008) | juist | extern bevestigd: "rises from zero in early 2007 to nearly 50 percent... late 2008" (Gorton & Metrick, *Securitized Banking and the Run on Repo*, NBER w15223/JFE 2012) | — (rapport-open-punt 1 opgelost) |
| 10 | 693, 699, 976 | HKM op 125 portefeuilles: 9% per kwartaal, GMM-$t$ 2,56, $R^2$ 45%; 7% voor aandelen; voorspelt in vijf van de zeven activaklassen | juist | extern bevestigd (meerdere onafhankelijke bronnen over He-Kelly-Manela 2017) | — (rapport-open-punten 2 en 5 opgelost) |
| 11 | 764, 770 | AEM: $R^2$ 77% tegen 10% (CAPM), prijs van leverage-risico 62% per jaar | juist | extern bevestigd (Adrian-Etula-Muir 2014 / NY Fed Staff Report 464) | — (rapport-open-punt 3 opgelost) |
| 12 | 750 | Figuurbijschrift: dip rond 1998 valt samen met LTCM, zonder recessie | juist | extern bevestigd (HKM-ratio toont een uitgesproken daling in 1998 rond LTCM; 1998 is geen NBER-recessie) | — (rapport-open-punt 6 opgelost) |
| 13 | 53–55, 78–79, 1049–1050 | Drie Santa-Clara-parafrases (marginale belegger huishouden→intermediair; premie zegt iets over wie het risico draagt; hefboom+marktprijs+deadline = recept voor ondergang) | juist | extern gelezen (LinkedIn-bron, drie citaten dekken de parafrases nauwkeurig) | — (rapport-open-punt 7 opgelost) |
| 14 | 795–797 | "Boekleverage halveerde van 47,0 (2008Q1) naar 22,6 (eind 2009) ... in dezelfde tijd steeg de marktleverage van 22 naar 38, bijna een verdubbeling" | **onjuist** (het tweede deel); F4: hersteld, piek 38 eind 2008 en 19,8 eind 2009 in de tekst | cel 12 output: marktleverage is 22,4 in 2008Q1 en piekt op 38,5 in 2008Q4, maar staat weer op 19,8 eind 2009 (2009Q4) — dus niet "naar 38" aan het eind van dezelfde periode | Boekleverage-zin laten staan; marktleverage-zin herschrijven, bv.: "In dezelfde tijd steeg de marktleverage van de primary dealers van 22 naar een piek van 38 eind 2008, bijna een verdubbeling, voor ze eind 2009 terugviel tot 19,8." Anders suggereert de zin een monotone stijging tot hetzelfde eindpunt als de boekleverage. |
| 15 | 59 | "In de herfst van 2008 daalde de consumptie van huishoudens maar matig" | **onzeker**; F4: bewering over consumptie geschrapt, Intuïtie opent nu met spreads en verliezen bij dealers | geen cel, geen citatie; extern wel plausibel (BEA: PCE −0,3% sept. en −1,0% dec. 2008, een orde kleiner dan de bewegingen in spreads/aandelen), maar dat is een andere maatstaf (maandmutatie, niet "de herfst") | Voeg een bron toe (bv. BEA Personal Income and Outlays 2008, of een cite naar de consumptie-CAPM-lecture) of maak concreet met een cijfer; anders blijft de bewering "niet herleidbaar" bij een strengere lezing. |
| 16 | 926–937, 968–972 | Vergelijkingstabel origineel/hier (min. $\eta$, $\lambda_\eta$ FF25 GMM 6,96/$t$3,10, $\lambda_\eta$ alle testactiva 3,44/Shanken-$t$1,94, $R^2$ FF25 0,44 vs. 0,09, $R^2$ AEM 0,41; $R^2$ met momentum 0,22 vs. Carhart 0,85) | juist | cel 14 output, regel voor regel nagerekend | — |
| 17 | 1013–1018 | Hodrick-regressies: 4,1pp marktrendement per procentpunt $\eta$ over 3 jaar; $t=-1{,}36$ (1 jaar), $t=-1{,}43$ (3 jaar) | juist | cel 16 output | — |
| 18 | 1071–1083, 1096–1130, 1142–1156 | Oefeningen 1–3: alle cijfers (schok 4%, BP-evenwichten $x_0=8/3$, momentum-cross-sectie) | juist | cel 17, 18, 19 output | — |

## Samenvatting per sectie (juiste rijen)

Overzicht, Intuïtie (op r.59 na), de rest van Theorie, Simulatie, en de rest van Replicatie
en Oefeningen bevatten geen andere getallen dan hierboven; alle kloppen met de celuitvoer of
zijn een directe, controleerbare handberekening uit cijfers die wél in de celuitvoer staan
(bijvoorbeeld $E/h=6{,}912/0{,}125=55{,}296\approx55{,}30$).

`open` na F23 = 2; na F4 (beide opgelost) = **0**.
