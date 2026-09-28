STATUS 03_11_apt_no_arbitrage F2 open=3

# Feitencontrole 03_11_apt_no_arbitrage

Methode: gelezen `lectures/03_11_apt_no_arbitrage.md` volledig, `tools/nb_outputs.py
lectures/03_11_apt_no_arbitrage.ipynb` (uitvoer in `$TEMP/f2-03_11-outputs.txt`),
`lectures/03_10_merton_icapm.md` en `lectures/03_12_consumptie_capm.md` volledig, en van
elke andere aangehaalde lecture (`02_09_black_scholes`, `00_01_rendementen`, `02_08_capm`,
`references.bib`) de aangehaalde plek. Voor de Roll-Ross-details is de brontekst van
Connor & Korajczyk (1995) zelf opgehaald (werkpaperversie,
kellogg.northwestern.edu/faculty/korajczy/ftp/wp139.pdf) en nagelezen.

Let op: `lectures/03_10_merton_icapm.md`, `03_12_consumptie_capm.md` en `03_14_roll.md`
werden tijdens deze controle gelijktijdig door een andere agent bewerkt (mtimes
22:14–22:29 vandaag). 03_10 en 03_12 zijn als momentopname gecontroleerd; 03_14's
verwijzing naar 03_11 is buiten deze controle gelaten omdat het bestand halverwege een
bewerking bleek (inhoud veranderde tussen twee greps binnen dezelfde sessie).

| nr | regel | bewering | oordeel | bron | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 60–70 | Geschiedenisketen: Ross 1976, Cox-Ross 1976, Cox-Ross-Rubinstein 1979, Harrison-Kreps 1979, Harrison-Pliska 1981, Dybvig-Ross 1987 (namen, jaartallen, "fundamentele stelling") | juist | `references.bib` (Ross1976, CoxRoss1976, CoxRossRubinstein1979, HarrisonKreps1979, HarrisonPliska1981, DybvigRoss1987): titels en jaren kloppen | geen |
| 2 | 145–166 | Toy-voorbeeld stap 1–4 en 6: $q_g=0{,}40$, $q_s=0{,}50$, $1+R^f=1{,}1111$, call $=0{,}16$, $\theta_a=0{,}5$, $\theta_b=-0{,}3$, arbitrage $0{,}04$ | juist | `nb_outputs` cel 2 (tabel "met de hand"/"code" is overal gelijk) | geen |
| 3 | 160–162 | Stap 5: "Deel de toestandsprijzen door de kansen: $m_g=0{,}6667$, $m_s=1{,}25$. Vermenigvuldig **ze** met $1+R^f$: $\pi^*_g=0{,}4444$, $\pi^*_s=0{,}5556$." | onjuist | Letterlijk gelezen wijst "ze" naar $m_g,m_s$ (net ervoor gedefinieerd); $m_g\cdot(1+R^f)=0{,}7407$ en $m_s\cdot(1+R^f)=1{,}3888$, niet $0{,}4444$/$0{,}5556$. De juiste stap is $q_g\cdot(1+R^f)$ en $q_s\cdot(1+R^f)$, zoals [](#eq-apt-no-arbitrage-drie-namen) ($\pi^*_s=q_s(1+R^f)$) en de code (`q_rn = q * gross_rf`, cel 2) laten zien | "ze" vervangen door "de toestandsprijzen $q_g$ en $q_s$ (stap 1)", zodat de instructie naar $q$ i.p.v. $m$ wijst |
| 4 | 223–651 | Alle labels in Theorie (def-apt-no-arbitrage-begrippen, thm-…-fundamenteel, thm-…-uniek, thm-…-exact, thm-…-huberman, def-…-asymptotisch, rem-…-sdf en alle eq-labels) bestaan en de erbij horende beweringen kloppen wiskundig | juist | interne label-grep; geen dubbele of ontbrekende labels | geen |
| 5 | 499–508 | Exacte APT op de toy: call-bèta $2{,}6875$, $\lambda_1=0{,}1447$, $\E[R_{\text{call}}]=1{,}50$ | juist | met de hand nagerekend op exacte breuken: afwijking aandeel $16/43=0{,}372093$, afwijking call $1{,}00$, bèta $=43/16=2{,}6875$ exact; $1{,}1111+2{,}6875\times0{,}1447=1{,}4997\approx1{,}50$ | geen |
| 6 | 421–438 | CRR-kans in de boom: $u=1{,}6279$, $d=0{,}6977$, $\pi^*=0{,}4444$ | juist | handberekening: $1{,}40/0{,}86=1{,}62791$, $0{,}60/0{,}86=0{,}69767$, $(1{,}1111-0{,}6977)/(1{,}6279-0{,}6977)=0{,}44442$ | geen |
| 7 | 409–428 | Symbool $d$: dividend $d_{t+1}$ in [](#eq-apt-no-arbitrage-martingaal) versus daalfactor $d$ in [](#eq-apt-no-arbitrage-crr-q), enkele zinnen verderop in dezelfde subsectie | onzeker | STYLE-check op dubbele symboolbetekenis; `lectures/02_09_black_scholes.md` r. 226 vermeed dit expliciet door het dividend daar $\delta$ te noemen ("Ook $d$ is in de boom de daalfactor, niet het dividend; een dividend heet hier $\delta$") — 03_11 haalt de boom uit 02_09 aan maar niet die naamgeving | dividend in de martingaalvergelijking $\delta_{t+1}$ noemen (zoals 02_09), of de zin met $d_{t+1}$ schrappen (het is de enige plek waar dividend in deze lecture voorkomt) |
| 8 | 132, 138, 445, 936, 1057 | Symbool $K$: uitoefenprijs in het toy-voorbeeld en oefening 2 ($K=1$) versus aantal factoren in Theorie/Simulatie/Replicatie ($K=1$ tot en met 5) | onzeker | STYLE-check op dubbele symboolbetekenis; door de context ("uitoefenprijs" resp. "factoren/componenten") vrijwel niet verwarrend, maar wel dezelfde letter | optioneel: geen apart symbool voor de uitoefenprijs invoeren (alleen "uitoefenprijs 1" in tekst en tabel) |
| 9 | 23–24, 421–422 | [](#02-09-black-scholes): BSM repliceert een optie uit aandeel en obligatie zonder voorkeuren; de boom gebruikt $u$/$d$ voor stijg-/daalfactor | juist | `lectures/02_09_black_scholes.md` r. 40 (Overzicht), r. 99–175 (toy: $u=1{,}1$, $d=0{,}9$, $\Delta$/$B$-replicatie) | geen |
| 10 | 25–27, 1045–1047 | [](#03-10-merton-icapm): Merton gaf het CAPM meer factoren uit hedgebehoeften die de nutsfunctie vereisen; 03_10 zelf sluit af met "Ross liet in 1976 zien dat een factormodel ook zonder voorkeuren volgt… zie 03-11-apt-no-arbitrage" | juist | `lectures/03_10_merton_icapm.md` r. 1226–1228 ("Wat er daarna kwam"); wederzijds consistent | geen |
| 11 | 1045–1047 | [](#03-12-consumptie-capm): Lucas en Breeden bonden $m$ aan consumptie | juist | `lectures/03_12_consumptie_capm.md` r. 23–28 ("Waar we zijn": "In [](#03-11-apt-no-arbitrage) bleek dat de afwezigheid van arbitrage genoeg is voor het bestaan van een positieve SDF") en r. 271 ("Het is de SDF uit [](#03-11-apt-no-arbitrage), nu met een naam") | geen |
| 12 | 759–761 | [de standaardfout van 2%](#00-01-rendementen): een gemiddelde wordt nauwkeuriger met de wortel van de periode | juist | `lectures/00_01_rendementen.md` r. 366–404 (thm-rendementen-se, $\SD(\bar r)=\sigma/\sqrt{T}$) | geen |
| 13 | 962–964 | Security market line via [](#02-08-capm) | juist | `lectures/02_08_capm.md` r. 41 (SML expliciet ingevoerd) | geen |
| 14 | 656–774 | Simulatie: parametertabel, $\sum\alpha_i^2=0{,}002$, SE $\approx0{,}75\%$, "ruim een kwart" verworpen (25,6–28,4%), "ongeveer 5%" (5,1–5,8%), $3180\times0{,}052\approx166$, $20\times0{,}284\approx5{,}7$, RMS $0{,}89\%\to0{,}08\%$, $0{,}08/\sqrt{120}=0{,}0073$ | juist | `nb_outputs` cel 3: alle kolommen (`som alpha^2`, `SE alpha per aandeel`, `verworpen, fout/goed geprijsd`, `RMS alpha`) matchen exact | geen |
| 15 | 782–849, 885–917 | Replicatie: steekproef 1963-07–2026-07 (757 maanden), PC1 83%/PC1-3 93% variantie, correlatie PC1-Mkt 0,93/0,926, alle zes $R^2$'s boven 0,89 | juist | `nb_outputs` cel 5, 6, 8, 9 | geen |
| 16 | 929–988 | Replicatie: PC1 0,76%/SE 0,19%/"ruim 2% per jaar"; PC1–PC3 significant, PC4–5 niet; K=1..5-tabel "0, 2, 1, 1, 3"; PC1-3-model constante 0,84%, alleen PC3 significant; FF3 constante "ruim 1,1%", negatieve marktpremie; gem. \|alpha\| 0,09% beide modellen; GRS $p<0{,}001$ beide | juist | `nb_outputs` cel 10 (t-waarden), 11 (K=1..5), 12 (fm_pc3/fm_ff3: constante 1,155% → "ruim 1,1%" is de gangbare beschrijving, ook zo geciteerd in `04_18_fama_french.md` r. 389) | geen |
| 17 | 992–1014 | Eindtabel replicatie en oordeel "Geslaagd": vier drempels gehaald (>0,75; >0,9; >0,85 tweemaal), tijdreeks 3, cross-sectie "0, 2, 1, 1, 3" | juist | `nb_outputs` cel 13 | geen |
| 18 | 796–798 | Open punt 1 (schrijver): "Roll en Ross gebruikten 1260 aandelen in 42 groepen van dertig, factoranalyse en GLS {cite}`ConnorKorajczyk1995`" | juist | Connor & Korajczyk (1995), werkpaperversie: "Roll and Ross (1980) estimate factor risk premia and test the APT restrictions with a sample of daily returns on **1260 firms** over the period from July 1962 to December 1972. Due to computational considerations, they divide the cross-sectional sample into **42 groups of thirty firms** each... they use **maximum likelihood factor analysis**... Roll and Ross (1980) use **generalized least squares** in the cross-sectional regressions rather than OLS." — citaat en cijfers exact bevestigd, correct toegeschreven aan CK1995 (die refereert Roll-Ross 1980), niet aan Roll-Ross zelf | geen; citaat is correct |
| 19 | 984–988 | Open punt 3 (schrijver): restant van de geschrapte bewering "alleen HML significant" | juist (geen restant) | grep op "HML" en "significant" in het hele bestand: geen bewering meer over aparte factorsignificantie in het driefactormodel | geen |
| 20 | 1052–1184 | Oefeningen 1–3: interval toestandsprijzen $(0;0{,}80;0{,}10)$–$(0{,}40;0;0{,}50)$, callprijsinterval $(0;0{,}16)$, linprog-uitvoer, boomafleiding, 49-industrieën-PCA (55%/92%/17%/3%) | juist | `nb_outputs` cel 14, 15 | geen |
| 21 | 1027–1043 | "Wat er brak": Shanken 1982, Dybvig-Ross 1985, Roll 1977; herhaalde cijfers 93%/0,84% per maand | juist | `references.bib` (Shanken1982, DybvigRoss1985, Roll1977); interne consistentie met sectie Replicatie | geen |

## Open punt 2 (schrijver): simulatie niet gekalibreerd op de toy-getallen

Dit is een **didactisch** punt, geen feitelijke fout. Geen enkel getal in de
simulatiesectie is onjuist of niet-herleidbaar: alle waarden (20 aandelen, alpha 1%,
$T=120$, drie factoren met eigen volatiliteit en premie) komen rechtstreeks uit de
code-cel en kloppen tegen de uitvoer (rij 14 hierboven). De simulatie gebruikt bewust
andere, eigen parameters dan het toy-voorbeeld (dat twee toestanden en één factor heeft,
geen 20 van de $N$ aandelen met een aparte alpha). STYLE §11 H11 vraagt dat toy-getallen
terugkomen in theorie én simulatie als kalibratie; dat gebeurt hier alleen in de theorie
(de call als exacte APT met bèta 2,6875), niet in de simulatie. Dat is een
opbouw/rode-draad-kwestie (rubriek criterium 2), niet iets dat binnen de feitencontrole
(geen didactisch oordeel, STYLE §11.11 feitenregel) als fout te noteren is.
