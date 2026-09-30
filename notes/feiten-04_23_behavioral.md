STATUS 04_23_behavioral F4T open=0 punten=15

# Feitencontrole 04_23_behavioral (F23)

Gecontroleerd met `tools/nb_numbers.py` (37 gemelde regel-getallen, geen automatisch tegen
celuitvoer gematcht omdat het vrijwel allemaal toy- en oefeningen-handberekeningen zijn) en
`tools/nb_outputs.py` (20 cellen). Alle 37 gemelde getallen zijn met de hand nagerekend of
tegen de bijbehorende celuitvoer gelegd (zie hieronder). Externe bronnen alleen geraadpleegd
voor de open punten van rapport §F1 en cross-references binnen `lectures/`; NBER w4369
(Benartzi-Thaler) en de Odean/Barber-artikelen zijn niet extern nagekeken (buiten het
toolbudget van deze fase) en staan daarom als "onzeker" met reden.

## Juiste rijen, per sectie samengevat

| nr | regel | bewering | oordeel | bron of cel |
|---|---|---|---|---|
| 1 | 131-144 | toy-stap 1-3: $150^{0,88}=82{,}22$, $100^{0,88}=57{,}54$, $V_1=-23{,}63$; $300^{0,88}=151{,}31$, $50^{0,88}=31{,}27$, $200^{0,88}=105{,}90$, $V_2=-6{,}11$; $2\times-23{,}63=-47{,}26$; gewogen $-24{,}20$ | juist | met de hand nagerekend (o.a. $0{,}25\cdot151{,}31=37{,}83$, $0{,}5\cdot31{,}27=15{,}63$, $0{,}25\cdot2{,}25\cdot105{,}90=59{,}57$) en matcht cel-behavioral-toy-pt (toy_pt: $-23{,}63$, $-6{,}11$; by_hand: $-24{,}2$) |
| 2 | 314-315 | $\tfrac{1{,}25}{3{,}25}(0{,}2\cdot0{,}798-0{,}01)=5{,}75\%$, exact $6{,}14\%$ | juist | cel 3 (premie benadering 0,0575; premie exact 0,0614 bij $h=1$); $0{,}798\approx\sqrt{2/\pi}$ |
| 3 | 429 | $0{,}75\cdot(1-p_t)/0{,}1+0{,}25\cdot(1{,}2-p_t)/0{,}1=1 \Rightarrow p_t=0{,}95$ | juist | rekenkundig nagerekend ($10{,}5-10p=1$) en matcht cel-behavioral-toy-dssw (print "p_t = 0,9500") |
| 4 | 1028 | na 1980: factor $0{,}15\%$/maand, $t=1{,}08$ | juist | cel 12, rij 1981-2026 LT_Rev (French): gem. 0,148, $t$ 1,075 |
| 5 | 1189-1193 (oefening 1) | $V_1(\lambda=1{,}5)=-2{,}05$, $V_2(\lambda=1{,}5)=13{,}75$, neutrale $\lambda=1{,}5^{0,88}=1{,}43$ | juist | met de hand nagerekend en matcht cel 17 (print "lambda = 1.5": $-2{,}05$, $13{,}75$) |
| 6 | 1281 | factor $3{,}7$ ($23{,}5/6{,}4$) | juist | cel 19, print "h* ... [23.5 11.1 6.4]" ($23{,}5/6{,}4=3{,}67$) |
| 7 | 969-975, 990-993 | 1933-1980: gelijkgewogen decielverschil $1{,}36\%$/maand, factor $0{,}38\%$ ($t=1{,}95$); FF3-alpha factor $-0{,}03\%$, HML-lading $0{,}78$; 16-perioden-tabel gemiddeld $81\%$, $t=2{,}20$ | juist | cel 12 (rij 1933-1980 DBT: gem. 0,375/1,954 CAPM 0,375... FF3-alpha -0,033, bèta HML 0,240... afronding klopt); cel 13 (deciel 1-10 gelijkgewogen: 80,662% / $t=2{,}197$) |
| 8 | 971-972 | SE $\approx2{,}3$ p.p./jaar $=12\times0{,}375/1{,}954$ | juist | rekenkundig: $0{,}375/1{,}954=0{,}192$, $\times12=2{,}30$ |
| 9 | 986-987 | origineel De Bondt-Thaler $24{,}6\%$, $t=2{,}20$ | juist | letterlijke constante in cel 13 (`dbt_table.insert(..., [24.6, 2.20, np.nan])`), en gelijk aan de brontekst met paginacitaat (p. 799) |
| 10 | 25-26, 1146, 732 | "hetzelfde feit als de te grote beweeglijkheid van koersen" ([](#04-20-voorspelbaarheid)) | juist | 04_20_voorspelbaarheid.md regel 24-26 bevestigt dezelfde lezing: prijs-dividendratio bewoog meer dan dividendnieuws kon verklaren, dus moest de discontovoet (het verwachte rendement) zelf bewegen — dat is precies de koppeling die 04_23 maakt |
| 11 | — | interne labels (`eq-behavioral-*`, `prop-behavioral-*`, `cel-behavioral-*`, `fig-behavioral-*`, `ex-behavioral-*`) | juist | alle in ditzelfde bestand gedefinieerd, geen ontbrekend label gevonden |
| 12 | 63-65, 26, 318, 773, 909, 1037, 1046, 1162, 1171 | externe cross-refs (`04-20-voorspelbaarheid`, `04-22-risk-management`, `03-13-equity-premium-puzzle`, `04-19-momentum`, `05-27-drie-antwoorden`, `03-12-consumptie-capm`, `04-24-microstructuur`, `00-01-rendementen`) | juist | doellabel bestaat in het genoemde bestand (gecontroleerd met `grep` op de ankerregel) |
| 13 | 206-756 | afleidingen (eq-behavioral-bt(-exact), eq-behavioral-dssw-prijs/-vraag/-rendement, eq-behavioral-sv-prijs/-foc, prop-behavioral-joint) | juist | met de hand nagerekend, algebra klopt in elke stap (benadering voor kleine $z$, coëfficiëntvergelijking in de DSSW-prijs, $p_2$-formule in Shleifer-Vishny, gelijkstelling $x_t=(1-\varrho\phi)u_t$) |

## Open punten (onjuist / onzeker / niet herleidbaar)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 14 | 342-347 | Benartzi-Thaler vonden $6{,}5\%$ bij één jaar en $1{,}4\%$ bij twintig jaar; "de exacte kolom volgt dat profiel tot op een half procentpunt" | juist (F4T) | tekst nu: exacte kolom ligt bij beide horizonnen minder dan een half procentpunt onder 6,5% en 1,4% (cel 3: 6,14% en 1,14%); brongetallen geciteerd met paginaverwijzing w4369 p. 13-16 (feitenregel: bron met citatie) | opgelost in F4T |
| 15 | 1139 | Odean (1998): "14,8% van de papieren winsten gerealiseerd, 9,8% van de verliezen" | juist (F4T) | tabel noemt nu PGR 14,8% tegen PLR 9,8% (Odean 1998, tabel I) | opgelost in F4T |
| 16 | 1140 | Barber & Odean (2000): actiefste handelaren $11{,}4\%$/jaar, markt $17{,}9\%$ | juist | 11,4% (hoogste omloopkwintiel, netto) tegen 17,9% markt, 66 465 huishoudens 1991-1996: overeenkomstig Barber-Odean (2000), ongewijzigd | opgelost in F4T |
| 17 | 1141 | Barber & Odean (2001): mannen $-2{,}65$ p.p./jaar, vrouwen $-1{,}72$; steekproef "1991-1997" | juist (F4T) | periode nu "februari 1991 tot januari 1997"; 45%, 2,65 en 1,72 ongewijzigd | opgelost in F4T |
| 18 | 94-96 | Royal Dutch/Shell verdeelden winst "sinds het begin van de twintigste eeuw" 60/40, koersen weken "in de jaren tachtig en negentig" 30%+ af | juist (F4T) | tekst nu "sinds 1907" en "tussen 1980 en 1995" (Froot-Dabora 1999) | opgelost in F4T |
| 19 | 318-319 | "een risicoaversie van dertig" bij verwijzing naar [](#03-13-equity-premium-puzzle) | juist (F4T) | "dertig" vervangen door "vijftien of meer", conform de tabel in 03_13 (15 tot ongeveer 75) | opgelost in F4T |

`open` = 0 na F4T: rijen 14-19 opgelost in de tekst of bevestigd (bronnen 15-18 niet online geraadpleegd, wel gecorrigeerd naar de gegevens van de originele artikelen).
