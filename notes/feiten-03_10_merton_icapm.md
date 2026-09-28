STATUS 03_10_merton_icapm F2 open=2

# Feitencontrole 03_10_merton_icapm

Controle van `lectures/03_10_merton_icapm.md` tegen `uv run python tools/nb_outputs.py
lectures/03_10_merton_icapm.ipynb` (HAP_OFFLINE=1), tegen `references.bib`, tegen
`lectures/02_09_black_scholes.md` (vorige), `lectures/03_11_apt_no_arbitrage.md`
(volgende), en tegen de plekken in `01_04_markowitz.md`, `02_08_capm.md`,
`00_01_rendementen.md`, `03_12_consumptie_capm.md`, `04_20_voorspelbaarheid.md` en
`04_21_volatiliteit.md` die naar deze lecture verwijzen of erdoor aangehaald worden.
Voor Barberis (2000) is de originele PDF geraadpleegd (p. 242-256) om de
replicatie-admonition en de p.246-claim te verifiëren.

| nr | regel (kopje) | bewering, letterlijk | oordeel | bron | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | Waar we zijn in het verhaal | "Jaartal. 1969–1973, met een uitloop naar 2002." | onjuist | grep op `{cite}` en op jaartallen in de hele lecture: geen enkele geciteerde bron of gebeurtenis in deze lecture dateert van 2002 (jongste citatie is Barberis 2000, Journal of Finance) | "1969–1973, met een uitloop naar 2000" (Barberis 2000), of het jaartal van de bedoelde gebeurtenis noemen als 2002 iets anders moest zijn |
| 2 | Theorie, Opzet en aannames | "Dit is vergelijking (12) van {cite:t}\`Merton1969\`, in onze symbolen." | onzeker | Merton (1969), *Lifetime Portfolio Selection under Uncertainty: The Continuous-Time Case*, R.E.Stat. 51(3): het artikel bestaat en de titel/jaar/auteur kloppen (references.bib), en de continue-tijd vermogensvergelijking staat er structureel in vroeg in het artikel, maar het exacte vergelijkingnummer (12) is niet te verifiëren zonder toegang tot de volledige (achter betaalmuur staande) tekst | laten staan als de schrijver het nummer tegen een eigen kopie van het artikel heeft nagerekend; anders "vergelijking (12) van Merton1969" vervangen door "de continue-tijd vermogensvergelijking van Merton1969" (zonder nummer) |
| 3 | Overzicht: Samuelson/Merton 1969, ICAPM 1973 | "In 1969 verschenen twee artikelen ... Samuelson loste het op in discrete tijd, zijn student Merton in continue tijd. ... In 1973 liet Merton de beleggingskansen zelf bewegen en leidde hij het ICAPM af." | juist | references.bib: Samuelson1969 (R.E.Stat. 51(3), 1969), Merton1969 (R.E.Stat. 51(3), 1969), Merton1973b (Econometrica 41(5), 1973, "An Intertemporal Capital Asset Pricing Model"); Merton was inderdaad Samuelsons promovendus (algemeen bekend, MIT) | — |
| 4 | Overzicht/Theorie | "Merton schreef het in zijn abstract: verwachte rendementen kunnen van de rente afwijken, ook zonder enig marktrisico {cite}\`Merton1973b\`." | juist | Econometric Society-samenvatting van Merton (1973): "expected returns on risky assets may differ from the riskless rate even when they have no systematic or market risk" — dekt de parafrase | — |
| 5 | Overzicht | "{cite:t}\`KimOmberg1996\` en {cite:t}\`CampbellViceira1999\` de hedgevraag uit." + latere claim "de hedgevraag kan de vraag naar aandelen verdubbelen" | juist | Kim & Omberg (1996), RFS 9(1), "Dynamic Nonmyopic Portfolio Behavior"; Campbell & Viceira (1999), QJE 114(2): samenvatting bevestigt letterlijk "intertemporal hedging motives greatly increase, and may even double, the average demand for stocks by investors whose risk-aversion coefficients exceed one" | — |
| 6 | Toy-voorbeeld (hele sectie: tabel, stappen 1-5, code) | Alle getallen: E[excess]=10%, SD=26%, w=0,8333 / 0,8759 / 0,7909, q=25/26 en 1, k=1,5297 en 1,4709, verschil 0,0426 | juist | handmatig nagerekend (zie werk hierboven) en cel 2 van `nb_outputs.py`: tabel "met de hand" = "code, gamma = 2" op 4 decimalen, gamma=1-kolom geeft overal 1,7361 | — |
| 7 | Theorie: Merton-portefeuille | $w^\ast = (\mu-r)/(\gamma\sigma^2)$, "0,10/(2·0,0676)=0,7396"; "$\mu_m-r=\gamma\sigma_m^2$, 8% bij $\gamma=2$ en $\sigma_m=20\%$" | juist | 0,10/(2×0,26²)=0,10/0,1352=0,7396 klopt; 2×0,20²=0,08=8% klopt; theorema en corollarium consistent met [](#01-04-markowitz) (separatiestelling, "twee fondsen", normaliteit-of-kwadratisch-nut) en met 04_21's aanhaling van dezelfde relatie als één zin | — |
| 8 | Theorie: hedgevraag en ICAPM | Tekens van de hedgevraag ($\gamma>1$, $\rho<0$ ⇒ positief), drie-fondsenstelling, $\mu_i-r=\beta_{i,m}\lambda_m+\beta_{i,x}\lambda_x$ | juist | intern consistent met toy-voorbeeld (geval B/B', 0,7909 < 0,8333) en met oefening 1 (gamma=0,5 geeft omgekeerd teken); Breeden (1979), JFE 7(3) samenvoeging tot consumptiegroei is de gangbare beschrijving | — |
| 9 | Numerieke oplossing (Kim-Omberg-tabel en tekst) | $\kappa=-\log 0{,}92=0{,}083$, halfwaardetijd $\approx 8$ jaar; gamma=1 hedge 0; gamma=5 myopisch 0,378, hedge (20j) 0,339; gamma=10 hedge(50j) > myopisch | juist | cel 3 van `nb_outputs.py`: exacte match op alle genoemde getallen; $-\ln(0{,}92)=0{,}0834$, $\ln2/0{,}0834=8{,}31\approx 8$ | — |
| 10 | Rooster vs. Kim-Omberg (vergelijking) | "grootste verschil is 1,6 procentpunt, bij $\gamma=10$ op twintig jaar (0,385 tegen 0,401)" | juist | cel 5: rooster gamma=10, H=20: 0,385; Kim-Omberg: 0,401; verschil 0,016 = 1,6pp; grootste verschil in de tabel | — |
| 11 | Simulatie (Stambaugh-bias) | "ware waarde 0,339 ... tussen 0,143 en 0,850 ... gemiddeld 0,450"; "55,5% significant"; "vrijwel geen" negatieve hedgevraag; figuur `fig-merton-icapm-steekproef` | juist | cel 6 en 7: exacte match (waarheid 0,339; 5%/95% kwantiel 0,143/0,850; gemiddelde 0,450; t(b)>1,96 fractie 0,555; hedge<0 fractie 0,001); label bestaat en caption komt overeen met wat 04_20 eraan aanhaalt (Stambaugh-bias, figuur `fig-merton-icapm-steekproef`) | — |
| 12 | Replicatie: Barberis' VAR | Tabel met Barberis (2000) tabel II [0,5118; 0,2129; 0,9774; 0,0091; 0,0017; -0,9351] vs. eigen OLS; "0,5 standaardfout onder"; "t=2,4" | juist | cel 9: exacte match van de "hier (OLS)"-kolom; (0,5118-0,4058)/0,2129=0,498≈0,5; 0,5118/0,2129=2,40≈2,4 | — |
| 13 | Replicatie: horizonallocaties eeuw | $t$-waarde 1,07; persistentie 0,924; correlatie -0,856; gamma=5, H=20 totaal/myopisch=1,5; gamma=10, H=50 =1,94; halfwaardetijd $\approx$8,8 jaar | juist | cel 10 en 11: exacte match (t=1,0727; phi=0,9239; rho=-0,8561; totaal/myopisch 1,499 en 1,943); $\ln2/(-\ln 0{,}924)=0{,}693/0{,}0790=8{,}77\approx8{,}8$ | — |
| 14 | Replicatie: parameteronzekerheid | "14,1% helling negatief"; "4,2% phi>1"; allocaties H=1..20 met/zonder onzekerheid; "twee procentpunt lager (0,440 tegen 0,459)"; "drie (0,635 tegen 0,668)"; Barberis "meer dan dertig procent" op tien jaar, p. 246 | juist | cel 12 en 13: exacte match (kans<0 =0,141; kans>1=0,042; tabelwaarden); 0,459-0,440=0,019 (≈2pp, afronding zoals elders in het boek); 0,668-0,635=0,033 (≈3pp); Barberis (2000) p. 246, geverifieerd in het origineel: "ignoring this uncertainty can lead to an overallocation to stocks of more than 30 percent at a 10-year horizon" (buy-and-hold, $A=10$) | — |
| 15 | Replicatie: steekproefperiodes | "Barberis' dynamische figuur 5 gebruikt de tienjaarssteekproef 1986–1995, en zijn koop-en-houdgetal komt uit 44 jaar maanddata" | juist | Barberis (2000) p. 253, Figuur 5-onderschrift: "The model is estimated over the 1986 to 1995 sample period"; het koop-en-houdgetal (Figuur 2, p. 246) gebruikt "the full data sample from 1952 to 1995" (p. 243) = circa 44 jaar maanddata | — |
| 16 | Oefeningen 1-3 | Alle getallen: $w=1{,}7361$ bij log-nut; hedgevraag/myopisch stijgend in $\gamma$; $C_\infty=-9{,}6283$, hedgevraag oneindig 0,6088 vs. RK 200j 0,6087; 1996-2025: $b=0{,}358$, $t=2{,}60$, $\phi=0{,}647$; verschil 0,168 (17pp) en 0,011 (1pp) | juist | cellen 15, 16, 17: exacte match op elk genoemd getal | — |
| 17 | Cross-ref notatie | "In [](#02-09-black-scholes) heette zij $W_t$, maar hier is $W$ het vermogen." | juist | `02_09_black_scholes.md` gebruikt overal $\mathrm{d}W_t$ voor de Brownse beweging (regels 242-365); geen tegenspraak | — |
| 18 | Cross-ref notatie | "Kim en Omberg schrijven $\lambda$, maar die letter is in deze reeks een prijs van risico." | juist | `00_00_setup.md` Notatie-tabel: $\lambda_f$ = "prijs van risico van factor $f$" | — |
| 19 | Cross-ref 01-04-markowitz | "Dat is de separatiestelling ... Markowitz had daarvoor normaliteit of kwadratisch nut nodig" | juist | `01_04_markowitz.md`: label `cor-markowitz-separatie`, "twee fondsen" (r. 48, 461, 605), "normaal verdeelde rendementen of kwadratisch nut" (r. 260-261) | — |
| 20 | Cross-ref 02-08-capm | "In het CAPM ... houdt iedereen dezelfde risicoportefeuille, en is de marktbèta de enige maat voor risico." | juist | `02_08_capm.md` Overzicht: "als alle beleggers dezelfde tangentportefeuille houden ... is het verwachte excess rendement van elk aandeel evenredig met één getal: zijn bèta met de markt" | — |
| 21 | Cross-ref 03-11-apt-no-arbitrage | "Ross liet in 1976 zien dat een factormodel ook zonder voorkeuren volgt, alleen uit de afwezigheid van arbitrage." | juist | `03_11_apt_no_arbitrage.md`: "Stephen Ross maakte er in 1976 een theorie van ... Dit werk definieert het tijdvak omdat het prijzen losmaakt van voorkeuren" (r. 61-68); en diens eigen "Waar we zijn"-blok noemt expliciet dat Merton (03-10) het CAPM meer factoren gaf | — |
| 22 | Cross-ref 03-12-consumptie-capm | "Of die ene factor de prijzen draagt, komt aan bod in [](#03-12-consumptie-capm)." | juist | `03_12_consumptie_capm.md` gaat over Lucas, Breeden en de SDF, met consumptiegroei als enige factor | — |
| 23 | Cross-ref 00-01-rendementen (2x) | "Dit is [de standaardfout van 2%](#00-01-rendementen) in dynamische vorm."; "Het verschil is zelf [de standaardfout van 2%]." | juist | label `00-01-rendementen` bestaat; zelfde linkconventie (naar de hele lecture, niet naar het sub-label `sec-rendementen-standaardfout`) wordt ook gebruikt in `02_05_crsp_tape.md` en `03_11_apt_no_arbitrage.md`, dus consistent met de rest van het boek | — |
| 24 | Externe cross-ref vanuit 04_20 | "We hebben dit in [](#03-10-merton-icapm) al gesimuleerd (figuur [](#fig-merton-icapm-steekproef))" bij de Stambaugh-bias | juist | label bestaat in 03_10 en de figuur (cel-merton-icapm-steekproef) toont precies de Stambaugh-bias in $\hat b$ over 1000 steekproeven, zoals 04_20 beweert | — |
| 25 | Externe cross-ref vanuit 04_21 | 04_21 schrijft $\mu_m-r=\gamma\,\Var_t(R^e)$ toe aan "het ICAPM van [](#03-10-merton-icapm)" | juist | in 03_10 staat exact deze relatie als één zin na het Merton-portefeuille-corollarium ("Houdt één representatieve belegger de hele markt ... dan zegt [] dat $\mu_m-r=\gamma\sigma_m^2$"), en 04_21 zegt zelf "zonder hedgingmotieven is dat de hele relatie" — geen tegenspraak, wel bewust vereenvoudigd tot het niet-hedgende geval | — |

## Samenvatting per sectie

- Toy-voorbeeld, Theorie (Samuelson, Merton-portefeuille, hedgevraag, ICAPM,
  Kim-Omberg, numerieke oplossing), Simulatie, Replicatie (Barberis' VAR,
  horizonallocaties, parameteronzekerheid), Wat er brak, en de drie oefeningen:
  alle getallen kloppen met `nb_outputs.py` of met een handberekening (rijen 3, 6-16).
- Alle citaties (Samuelson1969, Merton1969, Merton1973b, KimOmberg1996,
  CampbellViceira1999, Barberis2000, Breeden1979, Merton1980, Stambaugh1999) kloppen
  qua auteur, titel en jaar met `references.bib`; de twee kwantitatieve claims uit
  Barberis (2000) (p. 246 overallocatie >30%, Figuur 5 op 1986-1995) zijn geverifieerd
  tegen de originele PDF (rijen 14-15).
- Alle cross-refs (02-09, 01-04, 02-08, 03-11, 03-12, 00-01-rendementen, en de externe
  verwijzingen vanuit 04_20 en 04_21) kloppen met wat in de doellecture staat (rijen
  17-25).
- Enige twee open punten: het jaartal "2002" in de "Waar we zijn"-admonition (rij 1,
  onjuist) en het vergelijkingnummer "(12)" bij Merton1969 (rij 2, onzeker, niet te
  verifiëren zonder de volledige tekst achter de betaalmuur).

STATUS 03_10_merton_icapm F2 open=2
