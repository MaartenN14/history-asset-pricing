STATUS 04_20_voorspelbaarheid F4 open=0 punten=15

# Feitencontrole 04_20_voorspelbaarheid (F23)

Gecontroleerd met `tools/nb_numbers.py` (34 handberekeningen, geen in celuitvoer, allemaal
nagerekend met de hand hieronder) en `tools/nb_outputs.py` (19 cellen, gediffd tegen de
proza). Externe bronnen alleen geraadpleegd voor de open punten uit rapport §F1
(Cochrane 2008, Campbell-Thompson NBER 11468, Ferreira-Santa-Clara 2011, Fama-French 1988).
PDF's van Cochrane (2008) waren niet met tekst te doorzoeken (structuurdata i.p.v. tekst);
waar dat de verificatie blokkeerde staat het hieronder als "onzeker".

## Juiste rijen, per sectie samengevat

| nr | regel | bewering | oordeel | bron of cel |
|---|---|---|---|---|
| 1 | 78 | dp schommelt sinds 1926 tussen ~1% en 8% | juist | cel 8 (dp min −4,4668, max −2,5183 ⇒ 1,15%–8,05%) |
| 2 | 80 | afwijking na tien jaar nog voor ruim de helft aanwezig | juist | $\phi^{10}=0{,}941^{10}\approx0{,}539$ |
| 3 | 89 | $4^2/20^2=4\%$ | juist | rekenkundig (illustratief, geen brongetal) |
| 4 | 144-202 | toy-stappen 1–4 (rendementen, hellingen, identiteit, verdeling, 78%/22%) | juist | cel 2, identiek aan handberekening |
| 5 | 264-266 | $\rho=25/26=0{,}96$; tweede-ordeterm $=0{,}005$ | juist | rekenkundig ($0{,}5\times0{,}96\times0{,}04\times0{,}25=0{,}0048$) |
| 6 | 286, 347-348 | $\phi\approx0{,}94$/$0{,}941$; nulhypothese-rij $0$, $-0{,}093$, $0{,}941$, $0$ | juist | cel 3-constanten ($b_d=\rho\phi-1=-0{,}0931$) |
| 7 | 347 | Cochrane (2008): $b_r=0{,}097$ ($t$=1,92), $b_d=0{,}008$ ($t$=0,18), $\phi=0{,}941$ (SE 0,047), $b_r^{lr}=1{,}09$ (SE 0,44) | juist | extern bevestigd (meerdere onafhankelijke bronnen citeren $b_r^{lr}=1{,}09$, SE 0,44 en $\phi=0{,}941$; Cochrane-PDF zelf niet doorzoekbaar) |
| 8 | 350, 360 | $1-\rho\phi=0{,}093$; $1/\rho\approx1{,}04$ | juist | rekenkundig |
| 9 | 379-396 | $b_r^{(5)}=0{,}4435$, $b_r^{(10)}=0{,}7690$, oneindig $1{,}667$, verdisconteerd $1{,}0246$; $R^2(5)=15{,}7\%$, $R^2(10)=23{,}7\%$ | juist | rekenkundig, alle vijf nagerekend |
| 10 | 464-465, 980-981 | $\sigma_{uv}/\sigma_v^2=-0{,}90$; bias $=0{,}044$ / $0{,}07$ en $0{,}003$ (naoorlogs) | juist | rekenkundig, matcht cel 5 (Stambaugh-formule 0,0439) en cel 12 |
| 11 | 524-525 | Sharpe-ratio sinds 1871 $=0{,}108$, dus $S^2=1{,}2\%$ | juist | extern bevestigd (Campbell & Thompson, NBER WP 11468: "monthly Sharpe ratio for stocks is 0.108") |
| 12 | 530-532 | $\sigma_{dp}\approx0{,}45$, $T\approx76$ | juist | rekenkundig, consistent met SD_DP=0,153 en $\phi$=0,941 (cel 3) |
| 13 | 564-568 | $\rho=0{,}9638$, $\phi=0{,}941$, $T=78$, $b_d=-0{,}0931$; schokken 15,3%/14,0%/corr 7,5% | juist | cel 3 (letterlijke constanten in de code) |
| 14 | 622-626 | "1 op de 5" (>0,097), "<2%" (>0,008 en >1,09) | juist | cel 3 (0,2236; 0,0178; 0,0132) |
| 15 | 685 | bias-simulatie $\approx0{,}05$ vs. formule $0{,}044$ | juist | cel 5 (0,0492 vs. 0,0439) |
| 16 | 692-693 | $b_d=0{,}10+\rho\phi-1=0{,}007$; ware $R^2\approx5\%$ | juist | cel 6 (print "ware een-jaars R^2: 5,07%") |
| 17 | 731-732 | 60–80 jaar: "ongeveer de helft" (geschat), 5–8% (ware helling) | juist | cel 6 (0,503/0,442 resp. 0,076/0,051) |
| 18 | 835-838 | reëel logrendement 1926-2025: gem. 7%, sd 19%; dp-sd 0,47 | juist | cel 8 (0,0695; 0,1928; 0,4741) |
| 19 | 881-886, 900-903 | $R^2$ 0,16→0,64 (1941-1986); Hansen-Hodrick $t$ naar 6,1, Hodrick-1B daalt naar 2,4; tot 2025 $R^2=0{,}06$, $t=1{,}3$; naoorlogs $t<2$ vanaf 3 jaar | juist | cellen 9-10, exact |
| 20 | 948, 973-988 | replicatie binnen ~1/5 SE van Cochrane; $b_r^{lr}=0{,}98$; Stambaugh-correctie −0,04 (bijna helft); tot 2025 $b_r=0{,}062$ ($t=1{,}57$), $\phi\to0{,}96$ | juist | cellen 11-12, exact |
| 21 | 1049-1055 | 15/16 negatief (1965-2005); $R^2_{OOS}=-4{,}2\%$ (dp, 1965-2025); alleen `ik` en `svar` CW-$t$>1,65 | juist | cel 13, exact |
| 22 | 1070-1071 | Campbell-Thompson: e/p-verlies halveert, b/m slinkt | juist | cel 14 (−4,15→−1,89; −11,33→−10,01) |
| 23 | 1085, 1098 | oliecrisis 1973-1975 gemarkeerd | juist | code `axvspan(1973, 1975)` |
| 24 | 1148-1157 | SOP 1948-2007 matcht F-SC (1,32% maand, 12,08% jaar); CW-$t$>1,65; halveert tot 2025; Sharpe-winst 0,3 | juist | cel 16 (exact) + extern bevestigd (Ferreira & Santa-Clara: "Sharpe ratio gain of 0.3") |
| 25 | 1164-1171 | replicatie 1927-2004: $b_d\approx0$, $b_r\approx0{,}10$; 1965-2025 $R^2\approx-4\%$ | juist | cellen 11, 13 |
| 26 | 1210-1229 (oefening 1) | $\ell_3=-0{,}0836$; $\hat b_d=-0{,}25$; $\hat b_r=-0{,}018$; $b_r^{lr}=-0{,}0776$; $b_d^{lr}=-1{,}0776$ | juist | cel 17, exact |
| 27 | 1271-1300 (oefening 2) | $R^2$-formule vs. simulatie binnen enkele tienden procentpunt | juist | cel 18 (grootste verschil 0,52pp bij $k=10$) |
| 28 | 1317-1341 (oefening 3) | $\phi=0{,}978$; $b_r=0{,}075$ ($t=1{,}88$); $P(\hat b_d>\cdot)\approx2\%$; Stambaugh-correctie ongeveer halveert; $\rho\phi\approx0{,}95$ | juist | cel 19, exact |
| 29 | 799-802 (replicatie-admonition) | verwachte $R^2>0{,}5$ (FF), $b_r\in[0{,}07;0{,}13]$, $b_d$ binnen 0,05 van 0, GW negatief, som-van-de-delen positief | juist | cellen 9, 11, 13, 16 komen allemaal uit |
| 30 | 228-229 | tekenconventie $dp_t=-pd_t$, expliciet gekoppeld aan $pd_t=p_t-d_t$ van 03_15 | juist (notatie-check) | intern consistent door hele college; geen naadprobleem |

## Cross-references (labels bestaan)

Alle aangehaalde labels zijn gecontroleerd met `grep` op de doeldefinities: `#03-15-shiller-excess-volatility`,
`#04-19-momentum`, `#03-10-merton-icapm`, `#01-03-williams-ddm`, `#05-33-fama-vs-shiller`,
`#04-21-volatiliteit`, `#00-01-rendementen`, `#eq-shiller-excess-volatility-cs`,
`#eq-shiller-excess-volatility-decompositie`, `#fig-merton-icapm-steekproef` bestaan allemaal
in het genoemde bestand. Oordeel: juist voor alle tien.

## Open (onzeker): 4, opgelost in F4 (open=0)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 31 | 402-403 | Fama-French (1988): dp verklaart <5% van maand-/kwartaalrendementen, vaak >25% van 2-4-jaarsrendementen | onzeker | citatie aanwezig ({cite}`FamaFrench1988`), maar exacte percentages niet in doorzoekbare bron gevonden; wel consistent met het bekende patroon (korte horizon laag, lange horizon hoog) en met de eigen replicatietabel (R² 0,14→0,64, maar dat is jaardata, geen maand/kwartaal) | laten staan als het orde-van-grootte-claim is; anders "ruwweg" toevoegen of schrappen |
| 32 | 775-776 | Cochrane vond in zijn simulaties in 30 tot 40% van de steekproeven een even slechte of slechtere OOS-prestatie | onzeker | citatie aanwezig, maar PDF van Cochrane (2008) niet doorzoekbaar; niet elders bevestigd | check bij volgende revisie met een doorzoekbare kopie, of relativeren tot "een aanzienlijk deel" |
| 33 | 525-526 | Campbell-Thompson: $R^2_{OOS}=0{,}25\%$ voor de winst-prijsratio → 21% hoger verwacht rendement | onzeker | $S=0{,}108$ apart extern bevestigd; het specifieke cijfer $0{,}25\%$ voor e/p kon ik niet los bevestigen (wel intern consistent: $0{,}25/1{,}2\approx21\%$) | laten staan (interne rekensom klopt, bron is genoemd), evt. voetnootverwijzing naar de tabel in NBER 11468 |
| 34 | 1051-1053 | Bij Goyal-Welch begon de `ik`-reeks twee jaar later en was toen negatief | onzeker | geen cel, citatie impliciet ("bij Goyal en Welch"); niet extern te verifiëren binnen budget | ofwel schrappen (niet essentieel voor het argument), ofwel expliciet {cite}`GoyalWelch2008` toevoegen met paginaverwijzing |

Geen "onjuist" en geen "niet herleidbaar" gevonden: elk aangehaald getal komt overeen met een
celuitvoer, een handberekening die zelf klopt, of een bron met citatie.

## Bijvangst (geen aftrek, ter info)

- Regel 444: "zoals Kendall liet zien" heeft geen {cite}-sleutel; het resultaat zelf (de
  AR(1)-bias $-(1+3\phi)/T$) staat wel expliciet in [](#eq-voorspelbaarheid-stambaugh) en cel 5,
  dus inhoudelijk gedekt. Alleen relevant als de eindbeoordelaar bronvermelding wil bij elke
  naam.

## F4-afhandeling

| nr | status | wat |
|---|---|---|
| 31 | opgelost | "minder dan 5%" geschrapt ("maar een klein deel"); "vaak meer dan 25% van twee- tot vierjaarsrendementen" blijft, staat in de samenvatting van Fama-French (1988) |
| 32 | opgelost | "30 tot 40%" geschrapt; zin zegt nu kwalitatief dat zo'n slechte prestatie in Cochranes simulaties geen uitzondering is |
| 33 | opgelost | toeschrijving "0,25% voor de winst-prijsratio" geschrapt; 0,25% is nu een illustratieve rekensom (zoals rij 3) naast de gesourcete $S = 0{,}108$ |
| 34 | opgelost | "twee jaar later" geschrapt; "Goyal en Welch rapporteren een negatieve waarde" steunt op cel 13 (kolom GW, ik = −1,77) |
