STATUS 05_26_sdf_unificatie F4 open=0 (18 rijen: 17 juist, 1 n.v.t.; geen correctie nodig)

# Feitencontrole 05_26_sdf_unificatie

Methode: `tools/nb_numbers.py` (34 meldingen, geen enkele in celuitvoer) en
`tools/nb_outputs.py` (15 cellen) gedraaid met `HAP_OFFLINE=1`; elk aangehaald getal
regel voor regel vergeleken met celuitvoer of met een handberekening die zelf is
nagerekend. De twee interne cross-refs uit rapport §F1 zijn opgezocht in hun
bronlecture; de drie externe citaties zijn gecontroleerd tegen samenvattingen van de
oorspronkelijke artikelen.

## Tabel

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 111–201 | Toy: $\mathbf{G}=\begin{pmatrix}1&1\\1&1{,}125\end{pmatrix}$, $\mathbf{G}^{-1}=\begin{pmatrix}9&-8\\-8&8\end{pmatrix}$, $\mathbf{c}=(1{,}35;-0{,}40)$, $x^*=(0{,}75;0{,}95;1{,}15)$, $R^f=1{,}0526$, $\Var(x^*)=0{,}02$, $\sigma(x^*)/\E[x^*]=0{,}1489$, $k\in(-0{,}75;0{,}95)$ | juist | handberekening nagerekend (geen cel; alle 34 nb_numbers-meldingen betreffen deze en de volgende rij, intern consistent en algebraïsch correct) | geen |
| 2 | 402–425 | $R^*=(0{,}8130;1{,}0298;1{,}2466)$, $\E[R^*]=1{,}0298$, $\beta_{a,R^*}=-2{,}5625$, overrendement $0{,}0585$, Sharpe $=0{,}1489=$ HJ-grens | juist | matcht cel 2 ("met de hand"/"code") exact | geen |
| 3 | 489 | simulatie geeft $b\approx(3{,}5;0{,}65;4{,}9)$ | juist | cel 4: `ware b (FF3) = [3.49 0.65 4.94]` | geen |
| 4 | 710–711 | correlatie $g$ met HML $=0{,}71$, $\lambda_g=0{,}35\%$/mnd | juist | handberekening $0{,}03/\sqrt{0{,}03^2+0{,}03^2}=0{,}71$; `mu_f[2]=0.0035` | geen |
| 5 | 820–823 | $b_g$ verworpen in ~6%, $\lambda_g$ significant in ~helft (beide methoden), $J$ verwerpt ware model in 4,4% | juist | cel 4: fractie $\lvert t\rvert>1{,}96$ voor $b_g=0{,}058$; $\lambda_g$ GMM$=0{,}494$, FM$=0{,}518$; "J verwerpt het ware model (5%) in 4.4%" | geen |
| 6 | 852–857 | mediane $t(b_g)\approx0$, $t(\lambda_g)\approx2$; SE $=4{,}2/\sqrt{600}\approx0{,}17\%$, helft van de premie | juist | cel 4 medianen $0{,}010$/$1{,}949$/$2{,}003$; handberekening $4{,}2/24{,}49=0{,}171$ | geen |
| 7 | 895–898 | populatie-HJ CAPM $=0{,}14$, alpha $0{,}7\%$/mnd; mediane afstand na 20 jaar $0{,}31$; CAPM verworpen in 1 op 6 | juist | cel 6: `HJ CAPM = 0.142`; $T{=}240$: mediaan HJ FF3 $=0{,}309$, verwerpt CAPM $=0{,}160$ | geen |
| 8 | 928–957 | decielverschil $>1$pp, SE $0{,}23$–$0{,}31$pp; ruisbodem $0{,}20$–$0{,}21$ | juist | cel 7: Lo $=-0{,}031/0{,}306$, Hi $=1{,}162/0{,}228$; ruisbodem $0{,}202$–$0{,}212$ | geen |
| 9 | 982–1009 | HJ $0{,}41/0{,}39/0{,}36$; fout FF3 25$=0{,}110$, 35$=0{,}121$, mom.$=0{,}264>$CAPM $0{,}242$; UMD $t(b)=4{,}6$ halveert naar $0{,}124$; SMB-premie $0{,}32\%$ vs gem. $0{,}19\%$ | juist | cel 8 en 9, exacte match | geen |
| 10 | 1044–1054 | extremen jan. 2001/jan. 1976; FF3+UMD-SDF $1{,}04$/jr onder grens $1{,}738$; consumptie-SDF $0{,}36<$ markt-Sharpe $0{,}466$ | juist | cel 10, exacte match | geen |
| 11 | 1123–1142 | FF3+UMD-significanties; FF5+UMD: $t(\lambda_{\mathrm{HML}})=3{,}1$ (GMM)/$2{,}7$ (FM), $t(b_{\mathrm{HML}})=0{,}7$, $t(b_{\mathrm{RMW}})=3{,}0$; alle vijf replicatie-verwachtingen | juist | cel 9 en 12; tabel "verwachting/hier" exact | geen |
| 12 | 1213–1215, 1252–1264, 1296–1310 | oefeningen: put-prijzen $0{,}05/0{,}14375/0{,}2625$; cond. CAPM $J$: $127\to55$, $t(b_1)=2{,}3$; $R^2=0{,}11/0{,}50/0{,}76$, bootstrap 8/23/40pp | juist | cel 13, 14, 15 exact ("23pp" is de bootstrapmediaan, niet het puntverschil 26pp — bewust en correct zo gebruikt, want de tekst bespreekt de spreiding) | geen |
| 13 | 1099 | cross-ref `rem-apt-no-arbitrage-sdf`: negatieve SDF geeft diep-out-of-the-money optie een negatieve prijs | juist | `03_11_apt_no_arbitrage.md` r.520–533: "kan een diep uit-het-geld optie op de factor een negatieve prijs geven" — letterlijk dezelfde claim | geen (open punt 4 opgelost) |
| 14 | 1313 | cross-ref `prop-fama-french-mechanisch`: hoge $R^2$ met vrij intercept kan samengaan met verkeerde premies | juist | `04_18_fama_french.md` r.417–421: propositie laat precies zien dat een zwak gecorreleerde proxyfactor toch een goede fit geeft | geen (open punt 5 opgelost) |
| 15 | 908–909 | FamaFrench2015: HML overbodig zodra winstgevendheid (RMW) en investeringen (CMA) in het model staan | juist | extern geverifieerd: kernbevinding van het artikel is dat HML redundant wordt, "fully captured by its exposures to RMW and CMA" | geen (open punt 2 opgelost) |
| 16 | 668–669 | JagannathanWang1996: menselijk kapitaal verklaart een groot deel van de spreiding in gemiddelde rendementen | juist | extern geverifieerd: "significantly improves the fit"; "performs well in explaining the cross-section of expected returns" | geen (open punt 2 opgelost) |
| 17 | 648–649 | HansenJagannathan1997: de HJ-afstand beloont geen ruisige kandidaat-SDF | juist | extern geverifieerd: "measures of model performance do not reward variability of discount factor proxies" | geen (open punt 3 opgelost) |
| 18 | 859–899 | (open punt 1, geen bewering in de tekst) code-cel binnen `:::{note}` dropdown — bouwrisico? | n.v.t. | `nb_outputs.py` toont foutloze uitvoer voor die cel; bovendien bestaat wél een precedent (`04_24_microstructuur.md` heeft ook een code-cell in een `:::{note}` dropdown), dus rapports "geen precedent" klopt niet, maar dat staat niet in de collegetekst zelf | geen correctie aan het college nodig |

## Samenvatting per sectie (juiste rijen)

Overzicht, Intuïtie, Theorie (Stelling 1–4, GMM), "Wat er brak" en de admonities
("Waar we zijn", Replicatie) bevatten geen aangehaalde getallen buiten de bovenstaande
rijen; de overige cross-refs naar 00-01, 01-04, 02-08, 03-10, 03-12, 03-13, 04-18,
04-25 en 05-27 herhalen een geleend resultaat in één zin (H2) zonder cijfer dat apart
te controleren is, en zijn niet tegengesproken door de bronlectures.

`open` = onjuist(0) + onzeker(0) + niet herleidbaar(0) = **0**.
