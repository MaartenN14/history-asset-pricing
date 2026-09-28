STATUS 03_17_termijnstructuur_real_options F2 open=0

# Feitencontrole 03_17_termijnstructuur_real_options

Methode: `uv run python tools/nb_outputs.py lectures/03_17_termijnstructuur_real_options.ipynb`
(HAP_OFFLINE=1) tegen elk getal in de tekst; elke `{cite}`-key tegen `references.bib`;
de vijf open punten van de schrijver tegen de primaire bron (PDF's van Brennan-Schwartz
1985, Vasicek 1977 (via secundaire samenvatting), Longstaff-Schwartz 2001 en Litterman-
Scheinkman 1991, alle drie opgehaald en gelezen); elke cross-ref tegen het label en de
bewering in de doellecture (`03_16_vroege_anomalieen.md`, `04_18_fama_french.md`,
`05_28_termijnstructuur_premies.md`, `02_09_black_scholes.md`, `03_11_apt_no_arbitrage.md`,
`00_01_rendementen.md`, volledig gelezen waar het de buurlecture betreft).

## De vijf open punten van de schrijver

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Real options: de mijn | Tabel "grootheid / Brennan en Schwartz": 15 jaar, 10 mln pond/jaar, 50 dollarcent/pond; convenience yield 1%, variantie 8%, rente 10%/jaar; openen/sluiten/opgeven bij 76/44/20 cent; keuze om te sluiten bij 50 cent = $0,89 mln, 12% van een mijn die altijd produceert | Brennan & Schwartz 1985, *Evaluating Natural Resource Investments*, JoB 58(2), Table 1 (p. 148) en Table 2 (p. 149) | ok | Table 1: output rate 10 mln lb/yr, inventory 150 mln lb ("given an inventory equal to 15 years production"), cost $0,50/lb, convenience yield (κ) 1%/yr, price variance (σ²) 8%/yr, interest rate (ρ) 10%/yr. Tekst p.148: "not optimal to incur the cost of opening the mine until the price of copper rises to 76 [cents]... not optimal to close it down until the copper price drops to 44 cents... abandoned if the price drops below 20 cents." Table 2, rij $0,50: kolom 5 (Value of Closure Option) = 0,89; tekst p.149: "it amounts to 12% of the value of the fixed-output-rate mine". Alle getallen exact bevestigd. |
| Opzet en notatie | "Vasiceks $\alpha$, $\gamma$ en $q$ heten hier $\kappa$, $\theta$ en $\lambda$." | Vasicek 1977, *An Equilibrium Characterization of the Term Structure*, JFE 5(2) | ok | Secundaire bronnen (o.a. samenvattingen van het model) bevestigen $\mathrm{d}r = \alpha(\gamma - r)\,\mathrm{d}t + \sigma\,\mathrm{d}z$ met $\alpha$ de mean-reversionsnelheid, $\gamma$ het langetermijngemiddelde, en een marktprijs van risico genoteerd $q(t,r)$. De hernoeming $\alpha\to\kappa$, $\gamma\to\theta$, $q\to\lambda$ is dus correct; $\sigma$ blijft ongewijzigd, zoals de tekst ook niet claimt. |
| Real options: de mijn (LSM staat los, maar dit getal hoorde bij hetzelfde open punt) | Getal $-1{,}813$ uit een LSM-rekenvoorbeeld | Longstaff & Schwartz 2001, RFS 14(1), sectie 1 (p. 117) | n.v.t. | Het rekenvoorbeeld van acht paden (regressie $E[Y\mid X] = -1{,}070 + 2{,}983X - 1{,}813X^2$) is in F1 uit de lecture geschrapt (zie rapport, sectie "Geschrapt"). Het getal $-1{,}813$ komt in de huidige tekst niet meer voor (`grep` op "1,813" en "1{,}813": geen treffers). Ter volledigheid: het originele artikel (p. 117, gelezen als PDF) geeft zelf $-1{,}813$, niet het $-1{,}814$ dat een eerder rapport noemde — maar dit is nu niet meer relevant omdat de passage weg is. Geen actie nodig. |
| Wat het voorspelt: paden en curves | "De oneindig lange yield is 7,5% bij Vasicek en 5,2% bij CIR, vooral omdat de prijs van risico bij CIR $\lambda\sqrt i$ is: bij 5% maar $0{,}3\cdot 0{,}22=0{,}067$." | `nb_outputs` cel 5 (`long_yield`: Vasicek 0,0750, CIR 0,0516) | ok | Nagerekend: zonder premie ($\lambda=0$) geeft CIR $y_\infty=4{,}58\%$ (convexiteitseffect $-0{,}42$ pp t.o.v. $\theta=5\%$); met $\lambda=0{,}3$ komt daar via $\kappa^{*}=\kappa-\lambda\sigma_C=0{,}1299$ ongeveer $+0{,}58$ pp bij, per saldo $5{,}16\%\approx 5{,}2\%$. Bij Vasicek is de premie $+3$ pp en het convexiteitseffect $-0{,}5$ pp. Het verschil tussen de twee modellen (7,5% − 5,2% = 2,3 pp) komt dus voor ruim 2 pp uit het kleinere premie-effect (3 pp tegen 0,58 pp) en voor minder dan 0,1 pp uit het iets kleinere convexiteitseffect (0,5 tegen 0,42 pp). De bewering "vooral omdat de prijs van risico klein is" klopt kwantitatief; het getal $0,3\times0,2236=0,067$ is correct gerekend. De tekst noemt het convexiteitsverschil niet expliciet, maar dat verschil is inderdaad klein (< 0,1 pp), dus dat is geen fout, alleen een detail dat de tekst weglaat. |
| Toy-voorbeeld, stap 3 | "$p(0,2) = \tfrac12(1/1{,}08 + 1/1{,}02)/1{,}05 = 0{,}907771$" | `nb_outputs` cel 2: rij "p(0,2)", met de hand 0,907771, code 0,907771 | ok | Rekent kloppend na: $1/1{,}08=0{,}925926$, $1/1{,}02=0{,}980392$, som/2 $=0{,}953159$, $/1{,}05=0{,}907771$. Code (`bond2_t0`) geeft exact hetzelfde. |
| Oefening 3, uitwerking | "Dat zijn verschillen van $-1{,}15$ en $-2{,}86$ standaardfouten." | `nb_outputs` cel 20: "verschil in kappa: -0.1799, in standaardfouten: -1.15" / "verschil in theta: -0.0543, in standaardfouten: -2.86" | ok | Zelf nagerekend met een los script op de FRED/GSW-cache (HAP_OFFLINE=1): $\hat\kappa_{1971\text{-}1999}=0{,}2794$, $\hat\kappa_{2000\text{-}2026}=0{,}0995$, verschil $-0{,}1799$; $\hat\theta_{1971\text{-}1999}=0{,}06752$ (6,8%), $\hat\theta_{2000\text{-}2026}=0{,}01321$ (1,3%), verschil $-0{,}05432$. Gedeeld door de gepoolde standaardfouten geeft exact $-1{,}15$ en $-2{,}86$. Ook $\hat\kappa=0{,}28$/$0{,}10$, SE $0{,}14$/$0{,}07$, $\hat\theta=6{,}8\%$/$1{,}3\%$ en $\hat\sigma=2{,}0\%$/$0{,}65\%$ uit de lopende tekst kloppen tot op de laatste cijfer. |

## Extra bronverificatie (niet expliciet gevraagd, wel relevant voor toeschrijvingen)

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Replicatie, LSM tegen een binomiale boom | "De eerste rij van tabel 1: [...] origineel 4,478 / 3,844 / 4,472 / 0,010" en "100.000 (50.000 plus 50.000 antithetisch) paden" | Longstaff & Schwartz 2001, RFS 14(1), Table 1 (p. 127) | ok | Tabel 1, eerste rij ($S=36,\sigma=0{,}20,T=1$): Finite difference American 4,478; Closed form European 3,844; Simulated American 4,472; (s.e.) (,010). Bijschrift: "the strike price of the put is 40, the short-term interest rate is .06", "exercisable 50 times per year", "100,000 (50,000 plus 50,000 antithetic) paths". Alle vier getallen en de steekproefopzet exact bevestigd. Ook Proposition 1 (LSM als ondergrens) staat letterlijk zo in het artikel (p. 124), met hetzelfde bewijsidee. |
| Replicatie, Vasicek en CIR op de driemaandsrente | "tabel 2 van Litterman en Scheinkman: drie factoren verklaren gemiddeld 98,4% van de variantie" en factor 1/2/3 = 89,5/8,5/2,0 | Litterman & Scheinkman 1991, *Common Factors Affecting Bond Returns*, JFI 1(1), Table 2 (p. 58) | ok | Tabel 2 ("Implied Zeroes: Relative Importance of Factors"), rij "Average": Total Variance Explained 98,4; Factor 1 89,5; Factor 2 8,5; Factor 3 2,0. Exact gelijk aan de aangehaalde getallen. De naamgeving "slope" voor de tweede factor wijkt af van het origineel ("steepness"), een bewuste, in het rapport genoemde woordkeuze (geen feitelijke fout: dezelfde factor). De vormbeschrijving (level bijna parallel; slope wisselt van teken rond 4-5 jaar; curvature een piek/dal onder twintig jaar) komt overeen met de tekst van het artikel: "essentially a parallel change in yields" (factor 1), "lowers the yields of zeros up to five years, and raises the yields for longer maturities" (factor 2), "increases the curvature [...] below twenty years; the effect [...] tails off above twenty years" (factor 3). |
| Overzicht, slotzin | "voor Santa-Clara de UCLA-lijn van zijn mentoren Brennan en Schwartz" en (impliciet) het LSM- en real-options-werk van dat duo | Santa-Clara 2026, LinkedIn-post *What I Learned About Asset Pricing* | ok | Post bevat letterlijk: "I learned more at that table, from Roll, Michael Brennan and Eduardo Schwartz, than in my doctorate" (mentorschap), "with Longstaff again in 2001, the least-squares Monte Carlo method that made American-style options priceable by simulation" en "their 1985 paper on natural resource investments founded the real-options literature by treating a mine as an option to extract." Sluit precies aan bij wat deze lecture behandelt. Het citaat "Everything I made that lasted came from bearing risk that was priced..." (Intuïtie-sectie in STYLE, motief) staat er ook letterlijk in. |
| McDonald en Siegel | "Zo vonden McDonald en Siegel dat wachten tot de baten twee keer de kosten zijn bij redelijke parameters optimaal is" | McDonald & Siegel 1986, *The Value of Waiting to Invest*, QJE 101(4) | ok | Secundaire samenvattingen van het artikel bevestigen letterlijk: "for reasonable parameter values it is optimal to wait until benefits are twice the investment costs" — een centraal, veelgeciteerd resultaat van dit artikel. |
| `references.bib` | Auteurs, titel, tijdschrift, jaar van Vasicek1977, CoxIngersollRoss1985, BrennanSchwartz1979, BrennanSchwartz1985, LongstaffSchwartz1992, LongstaffSchwartz2001, DuffieKan1996, McDonaldSiegel1986, HoLee1986, LittermanScheinkman1991, GurkaynakSackWright2007, SantaClara2026 | `references.bib` | ok | Alle twaalf entries bestaan met correcte auteur(s), titel, tijdschrift, jaargang en paginanummers (gecontroleerd tegen de hierboven gelezen PDF's en tegen bekende gegevens; DOI's aanwezig waar van toepassing). |

## Toy-voorbeeld (samenvatting)

Alle tien getallen in de hand/code-tabel (p op t=1 hoge/lage knoop, p(0,2), p(0,3), yield 2 en
3 jaar, q, NCW zonder keuze, mijn met keuze, waarde van de keuze) staan letterlijk gelijk in
`nb_outputs` cel 2, kolommen "met de hand" en "code": ok. Ook de tussenstappen in de lopende
tekst (1/1,11=0,900901 enz., het convexiteitseffect van 0,114 pp, $q=0{,}625$) rekenen kloppend
na. Oefening 1 (Amerikaanse put op de obligatie, K=0,87) rekent exact gelijk aan `nb_outputs`
cel 18 (0,011999 / 0,003332 / 0,005714 / 0,005714 / 0,000000): ok.

## Theorie (samenvatting)

Alle in de tekst uitgerekende getallen zijn nagerekend en kloppen: $\theta^{*}-\sigma^2/2\kappa^2=7{,}5\%$
met $5\%+3\%-0{,}5\%$; halfwaardetijd $\log 2/0{,}15=4{,}6$ jaar; $\sigma/\sqrt{2\kappa}=2{,}7\%$;
$\eta=2$ bij $i=\delta=4\%,\sigma=20\%$ (rekenkundig geverifieerd: $\eta=0{,}5+\sqrt{0{,}25+2}=2$);
term premium $0{,}3\times5\%=1{,}5$ pp (los illustratief voorbeeld). Cross-refs
`eq-apt-no-arbitrage-martingaal` (03_11, r. 405), `thm-black-scholes-ito` (02_09, r. 262),
`eq-black-scholes-pde` (02_09, r. 328) en `thm-black-scholes-feynman-kac` (02_09, r. 370)
bestaan alle vier en de bewering bij elke verwijzing (arbitragevrije prijs is verdisconteerde
verwachting; Itô's lemma; drift verdwijnt in de Black-Scholes-PDE; Feynman-Kac geeft de
oplossing als verwachting) klopt woordelijk met de doeltekst. De risiconeutrale-kansformule
"$q=(1+R^f-d)/(u-d)$, zoals in [](#03-11-apt-no-arbitrage)" komt letterlijk overeen met
$\pi^{*}=(1+R^f-d)/(u-d)$ op regel 421 van 03_11 (ander symbool, zelfde formule): ok.

Kleine, onschadelijke symboolobservatie (geen fout, geen didactisch oordeel): $\kappa$ betekent
in deze lecture overal "snelheid van terugtrekken" (Vasicek/CIR), behalve in de aangehaalde
tabel van Brennan-Schwartz waar $\kappa$ hun eigen symbool voor de convenience yield is — dat
is expliciet zo aangekondigd ("bij Brennan en Schwartz $\kappa$") en dus geen stille dubbele
betekenis. Het symbool $k$ wordt gebruikt voor de vaste kosten van de mijn en, los daarvan, als
tijdsindex in het LSM-algoritme ($t_k$); beide gebruiken staan ver uit elkaar en scheppen geen
aantoonbare verwarring in context.

## Simulatie (samenvatting)

Alle percentages (58% van de Vasicek-paden ooit negatief, 4,7% van de maanden, laagste rente
$-6{,}7\%$, geen CIR-pad negatief, oneindig lange yield 7,5%/5,2%, 90%-interval $\hat\kappa$
0,10–0,54, $\hat\sigma$ 1,43%–1,59%, lange yield 4,2%–9,8%, mediaan $\hat\kappa=0{,}24$) staan
letterlijk in `nb_outputs` cellen 5 en 7: ok (zie ook de aparte rij hierboven over de
CIR-5,2%-verklaring).

## Replicatie op echte data (samenvatting)

Vasicek/CIR-fit op TB3MS ($\hat\kappa=0{,}10$, SE 0,06, $t=1{,}6$; $\hat\theta=4{,}2\%$, SE 2,0
pp; $\hat\sigma=1{,}5\%$; CIR $\hat\kappa=0{,}05$, Feller-ratio 1,03), modelcurve-fit ($\lambda=0{,}35$,
RMSE 115 bp, lange yield 8,3%; $\kappa^{*}=-0{,}02$, RMSE 124 bp; fouten van 2,3/1,8 pp in
1981/2021 voor Vasicek, 1,5/1,9 pp in 1981/2008 voor CIR) en de PCA-tabel (correlatie 1-10 jaar
0,69; 91,7/7,3/0,9/99,9 en 89,0/7,7/2,3/98,9 voor de twee eigen vensters) staan letterlijk in
`nb_outputs` cellen 9, 10, 12 en 14: ok. De vergelijking met Litterman-Scheinkman (89,5/8,5/2,0/98,4)
is apart geverifieerd tegen de bron, zie boven.

## Cross-refs naar buurlectures en 05_28 (volledig gelezen)

`03_16_vroege_anomalieen.md` (vorige) eindigt in "Wat er brak, en wat daarna kwam" met: "Eerst
wendde de theorie zich naar een ander prijsprobleem, waarin toestandsvariabelen de rol van
kenmerken overnemen: de rente en de waarde van flexibiliteit, in
[](#03-17-termijnstructuur-real-options)." Dat is precies consistent met 03_17's eigen "Waar we
zijn" ("Die barst blijft hier even liggen"): geen tegenspraak, label bestaat en klopt.

`04_18_fama_french.md` (volgende) opent met: "[](#03-17-termijnstructuur-real-options) keek naar
de prijs van de tijd; hier keren we terug naar de cross-sectie van aandelen," wat letterlijk
aansluit bij 03_17's eigen slotzin ("Eerst keert het vak terug naar de cross-sectie, [...]:
[](#04-18-fama-french)"). Verder geen vermeldingen van termijnstructuur, Vasicek, CIR of
Brennan-Schwartz in 04_18 (`grep` op deze termen): geen tegenspraak mogelijk.

`05_28_termijnstructuur_premies.md` opent met: "In [](#03-17-termijnstructuur-real-options)
prijsden Vasicek en CIR de hele rentecurve met één factor en een constante marktprijs van
risico. Een principale-componentenanalyse op de GSW-curve vond daar drie factoren, en de lange
rente bleek op eigen kracht te bewegen." Dat komt letterlijk overeen met 03_17's eigen
bevindingen (één factor, constante $\lambda$; drie PCA-componenten; figuurbijschrift "de
waargenomen lange rente beweegt trager en op eigen kracht"). Het label
`thm-termijnstructuur-real-options-affien` bestaat (regel 350) en wordt in 05_28 (regel 600)
gebruikt om te zeggen dat de log-prijzen in een driefactor-Gaussisch affien model "affien" zijn
"zoals in [](#thm-termijnstructuur-real-options-affien)" — dat is precies de generalisatie die
03_17 zelf al aankondigt na de stelling ({cite:t}`DuffieKan1996` bewezen dit voor een vector
factoren): geen tegenspraak, correcte cross-ref.

## Notatie (00_00_setup, sectie Notatie)

De lecture wijkt bewust af van de standaardtabel door de korte rente $i_t$ te noemen in plaats
van $r$, met de reden er expliciet bij ("want $r$ is in de reeks het netto simpele
rendement"). Dat is precies de eis uit STYLE §3 ("vertaal je naar deze tabel en zeg je dat in
één zin"). $R^f$ wordt, net als in de setup, als netto rente gebruikt (5% = 0,05, bruto
$1+R^f$): consistent. Geen ander symbool uit de lecture botst met de setuptabel.

STATUS 03_17_termijnstructuur_real_options F2 open=0
