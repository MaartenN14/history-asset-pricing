STATUS 03_16_vroege_anomalieen F2-diff open=0

Feitencontrole van `lectures/03_16_vroege_anomalieen.md` tegen de uitvoer van
`uv run python tools/nb_outputs.py lectures/03_16_vroege_anomalieen.ipynb` (HAP_OFFLINE=1),
`lectures/03_15_shiller_excess_volatility.md`, `lectures/03_17_termijnstructuur_real_options.md`,
de aangehaalde plekken in `02_08_capm.md`, `01_03_williams_ddm.md`, `00_01_rendementen.md`,
`04_18_fama_french.md`, `04_23_behavioral.md`, `06_34_factor_zoo.md`, `references.bib`, en
waar toegankelijk secundaire bronnen over de primaire artikelen (websearch; de eigenlijke
JF/JFE/JPM/RFS-teksten zijn paywalled en niet ingezien, zoals de lecture zelf al meldt).

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Waar we zijn in het verhaal | "Jaartal. 1960–1993, met het zwaartepunt tussen 1977 en 1985"; cross-refs naar [](#02-08-capm) en [](#03-15-shiller-excess-volatility) | jaartallen kloppen met Basu1977–Black1993; labels bestaan, doellecture zegt wat hier beweerd wordt (SML te vlak maar positief in 02_08; excess volatility van de index in 03_15) | ok | — |
| Overzicht | "Tussen 1977 en 1985 verschenen vier artikelen": Basu1977 (P/E), Banz1981 (ME), Reinganum1981 (beide), RosenbergReidLanstein1985 (B/M); plus Keim1983, Bhandari1988, LoMacKinlay1990, Black1993 | references.bib (auteurs, jaartallen, tijdschriften kloppen); telling van "vier" klopt | ok | — |
| Intuïtie | "In juli 1960 vroeg S. Francis Nicholson ... koers boven 25 keer de winst, of die onder 12 keer ... bijna tien tegen één in het voordeel van de dure aandelen" | Nicholson1960, FAJ 16(4); secundaire bron (Semantic Scholar-samenvatting) bevestigt exact "25 vs. 12" en "nearly ten-to-one in favor of the high multiples" | ok (extern bevestigd; primaire FAJ-tekst zelf niet ingezien, zoals de lecture al aangeeft) | — |
| Intuïtie | cross-ref "van De Bondt en Thaler in [](#04-23-behavioral)" bij het extrapolatieverhaal | 04_23_behavioral.md regel 49-51: De Bondt en Thaler (1985) vinden dat verliezers van 3-5 jaar de winnaars daarna verslaan | ok, label bestaat en onderwerp klopt | — |
| Toy-voorbeeld | alle getallen (marktgewichten, marktrendement 6,0%, marktbèta 1,000, alpha's A–E, H/L/H−L-tabel, alpha H−L 5,325%) | cel 2 van nb_outputs | ok, exact gelijk aan celuitvoer | — |
| Toy-voorbeeld | Fama-MacBeth-gewichten toy: gemiddelde E/P 7%, afwijkingen, kwadratensom 0,005, gewichten (−8,−4,−2,4,10) | cel 3 | ok, exact gelijk | — |
| Theorie — alpha long-short | "Sharpe-ratio per maand ongeveer 0,13 ... correctieterm 1,02"; "5/√480 ≈ 0,23% per maand, bijna 3% per jaar" | handrekening: 1+0,13²=1,0169≈1,02; 5/√480=0,2282; 0,2282×12=2,74% (annualisering ×12, consistent met project-conventie elders in de lecture) | ok | — |
| Theorie — alpha long-short | "Basu (veertien jaar) en ... Rosenberg, Reid en Lanstein (twaalf jaar)" | Basu-periode in repliceerblok 1957-04/1971-03 = 168 maanden = exact 14 jaar; RRL-periode 1973-01/1984-09 = 141 maanden ≈ 11,75 jaar, rondt af op 12; secundaire bron bevestigt RRL-steekproef "January 1973 to September 1984" | ok | — |
| Theorie — Fama-MacBeth | "In [](#02-08-capm) was de maandelijkse Fama-MacBeth-helling op bèta het rendement van een portefeuille die niets kost en bèta één heeft" | 02_08_capm.md regel 554-557: "rendement van een portefeuille met bèta één en kosten nul" | ok, label bestaat en bewering klopt | — |
| Theorie — Fama-MacBeth | "Rosenbergs bedrijf Barra, dat in 1975 het eerste commerciële multifactor-risicomodel voor Amerikaanse aandelen uitbracht" | secundaire bronnen (MSCI/Barra-geschiedenis): Barr Rosenberg richtte Barra op in 1975, met het eerste multifactor-risicomodel (USE1) voor de VS | ok | — |
| Theorie — kernresultaat Berk | Gordon-model $p=d_1/(r-g)$ uit [](#01-03-williams-ddm); correlatie −0,19 (vooruitverwijzing naar simulatie) | 01_03_williams_ddm.md regel 45: zelfde formule; simulatiecel 4 geeft −0,193 | ok, label en getal kloppen | — |
| Theorie — data snooping | Lo-MacKinlay 1990: "liet met berekeningen, simulaties en twee empirische voorbeelden zien dat dit effect groot kan zijn" | secundaire bron (samenvatting): "analytical calculations, Monte Carlo simulations, and two empirical examples" | ok (extern bevestigd; primaire RFS-tekst niet ingezien, zoals de lecture al aangeeft) | — |
| Theorie — data snooping | $\varphi(1{,}2816)/0{,}1=1{,}755$; $\E[t]\approx 24{,}8\,\rho$; bij $\rho=0{,}1$ dan $t\approx2{,}5$; bij $K=20$ kans 40% | handrekening nagerekend: $\Phi^{-1}(0,9)=1,2816$, $\varphi(1,2816)=0,1755$, $\sqrt{200}\times1,755=24,82$; $1-0,975^{20}=0,397$ | ok | — |
| Theorie — data snooping | cross-ref "systematische versie ... is [](#06-34-factor-zoo)" | 06_34_factor_zoo.md: label bestaat, bespreekt t>3-drempel en Bonferroni voor factor-datamining | ok | — |
| Simulatie (a) | correlatie log ME met k/bèta/delta (−0,193/−0,123/−0,150); gem. verwacht rendement 12,6%; CAPM-alpha 0,076% vs theorie 0,079%, fractie t>1,96 18,6% (CAPM) en 2,4% (tweefactor); FM-coëfficiënten −0,069% (t=−4,18) en −0,031% (t=−2,24) | cel 4, 5, 6 | ok, alle getallen exact gelijk aan celuitvoer | — |
| Simulatie (b) | "beste van honderd haalt ... 92,5% ... t>1,96 en ... 12% ... t>3"; formule-toets bij ρ=0,10 t=2,36 vs 2,48, erna binnen 0,15 van nul | cel 7, 8 | ok, exact gelijk (grenswaarde 0,150 bij ρ=0,20 is de afgeronde celuitvoer zelf) | — |
| Replicatie — repliceerblok en tabel | zes VW/EW-alpha's en t-waarden voor E/P (Basu), B/M (RRL) en size (Banz), oorspronkelijk en na publicatie | cel 11 | ok, alle twaalf getallen exact gelijk aan celuitvoer | — |
| Replicatie — "Geslaagd"-alinea, **open punt 1** | "De long-short-bèta van E/P en B/M is in de oorspronkelijke steekproef negatief" en in "Wat er brak": "Goedkope aandelen ... terwijl hun long-short-bèta rond nul of negatief lag" | cel 11: E/P bèta VW −0,054/EW −0,261; B/M bèta VW −0,043/EW −0,348; size bèta VW 0,596/EW 0,563 | ok — de bewering is expliciet beperkt tot "goedkope aandelen" (E/P, B/M) en klopt; size wordt hier terecht niet meegenomen, want de long-short-bèta van size is +0,60/+0,56, dus positief, niet "rond nul of negatief" | — |
| "Wat er brak", **open punt 2** | "Over de volle eeuw verklaart het CAPM de value-weighted B/M-premie grotendeels, met een alpha van 0,14% ($t=0{,}83$)" en in "Geslaagd": "... alpha van 0,14% en een long-short-bèta van 0,44" | cel 11, B/M volledig 1926/2026 VW: alpha 0,144 (t 0,829), bèta 0,436 | ok, klopt exact (0,144→0,14; 0,829→0,83; 0,436→0,44) | — |
| Replicatie — figuurbijschrift decielen | kwalitatieve patronen: E/P "van rond nul ... naar duidelijk positief"; B/M "vrijwel monotoon van negatief naar positief"; size "alleen het kleinste deciel eruit, met een foutbalk die nul bevat" | zelf herberekend (zelfde CAPM-regressie per deciel, dezelfde perioden en gewichten als cel 12) | ok, patroon klopt in alle drie de sorteringen; size Lo-10: alpha 0,234 (t 0,79), foutbalk ±0,59 bevat nul | — |
| Replicatie — januari-effect | Keim-periode: "10,3%" januari (EW), "vier vijfde"/"82%" bijdrage, "meer dan bij Keim"; "Keim zelf vond over 1963–1979 bijna vijftig procent, waarvan meer dan de helft in de eerste handelsweek" | cel 13 (10,298; bijdrage EW 0,782, VW 0,817); secundaire bron over Keim1983: "nearly fifty percent ... due to January", "more than fifty percent ... first week of trading" | ok, zowel de eigen cijfers als de toeschrijving aan Keim kloppen | — |
| Replicatie — na 1980 | "5,6% ... $-0{,}49\%$ per maand, $t=-2{,}57$" | cel 13, EW jan 5,611; feb-dec −0,489 (t −2,574) | ok | — |
| Replicatie — Fama-MacBeth bèta/size | "$-0{,}11\%$ per maand ($t=-1{,}55$)"; "0,73% per maand zonder size naar $-0{,}12\%$ met size" | cel 14: −0,106 (−1,552); 0,728 → −0,119 | ok | — |
| Wat er brak | "Reinganum las zijn resultaten ... als een verkeerd gespecificeerd evenwichtsmodel, niet als inefficiëntie, omdat de abnormale rendementen minstens twee jaar aanhielden" | secundaire bron over Reinganum1981: "abnormal returns persist for at least two years ... indicate the equilibrium pricing model is misspecified" | ok, extern bevestigd | — |
| Wat er brak | cross-ref "in [](#03-17-termijnstructuur-real-options)" | 03_17: "Waar we zijn" citeert letterlijk "[Basu, Banz en Rosenberg](#03-16-vroege-anomalieen) vonden kenmerken die rendementen voorspelden buiten het CAPM om" | ok, label bestaat, wederzijds consistent | — |
| Oefening 1 | H=(C,D,E)/L=(A,B): bèta, excess, alpha van H en H−L | cel 15 | ok, exact gelijk | — |
| Oefening 2 | benaderingsformule en getallen bij SD log C = 1,5 en 0,75 | cel 16 | ok, exact gelijk | — |
| Oefening 3 | januari-aandeel E/P/B/M 1963-1984 en 1985-2026: "65%", "67%", "24%", "45%", "0,78% ($t=4{,}17$)" | cel 17 | ok, exact gelijk (0,647→65%; 0,670→67%; 0,240→24%; 0,451→45%; 0,775→0,78, 4,172→4,17) | — |
| Oefening 4 | "(1) ... Voor $c=1{,}96$ is $\Phi(c)=0{,}975$ en $K=27{,}4$, dus 28 kandidaten. Voor $c=3$ is $\Phi(c)=0{,}99865$ en $K=513{,}4$, dus 514." | nagerekend: $\log 0{,}5/\log 0{,}975=27{,}38$ (klopt, ≈27,4); $\log 0{,}5/\log 0{,}99865=513{,}10$ (niet 513,4); met de volledige $\Phi(3)=0{,}9986501...$ ook 513,13 | **fout** | $K\approx513{,}1$ in plaats van 513,4 (de afgeronde uitkomst "dus 514" blijft juist, want $\lceil513{,}1\rceil=\lceil513{,}4\rceil=514$) |
| Oefening 4 | cel 18: K=28,0/514,0 en gesimuleerde kans 0,504/0,502 bij 20.000 onderzoekers | cel 18 | ok, exact gelijk aan celuitvoer (en bevestigt dat het eindantwoord 514 klopt) | — |
| Symbolen | $q_j$ (breekpunten van een kenmerk) versus $q_p=\Phi^{-1}(1-p)$ (kwantiel van de standaardnormale) | eigen lezing van de hele tekst | geen dubbelzinnigheid: beide zijn kwantielen, met duidelijk verschillende subscript en expliciete definitie bij eerste gebruik | — |
| Notatie | $R^e$, $R^f$, $\beta_{i,f}$, $\alpha_i$, tijdsindexering $z_{i,t}\to R^{e}_{i,t+1}$ | STYLE.md §3 / 00_00_setup.md sectie Notatie | ok, conform | — |
| Bib (nevenbevinding, geen "getal in de tekst") | `RosenbergMcKibben1973` in `references.bib` heeft `pages = {317}` zonder eindpagina | references.bib regel 2507-2515 | onvolledig bib-veld, niet gecontroleerd tegen de lecturetekst zelf (geen "TODO verify"-markering); geen invloed op enige bewering in de lecture | niet opgelost, buiten scope van deze feitencontrole |

## Diff na F4/F6b

Diffcontrole van de wijzigingen sinds de eerste feitencheck hierboven (workflow §3.1
stap 6 / §9 punt 5). Gelezen: `notes/rapport-03_16_vroege_anomalieen.md` §F4 en §F6-1
(alleen die secties), de huidige `lectures/03_16_vroege_anomalieen.md`, `uv run python
tools/nb_numbers.py lectures/03_16_vroege_anomalieen.md` en de celuitvoer via
`uv run python tools/nb_outputs.py lectures/03_16_vroege_anomalieen.ipynb` (HAP_OFFLINE=1).
De lecture zelf is niet gewijzigd; wel is `--sync` en `--execute --to ipynb` gedraaid om de
celuitvoer te verversen (deterministisch, dezelfde seed en dezelfde `.md`-inhoud als
daarvoor — geen inhoudelijke wijziging, alleen serialisatie van het notebook).
`tools/nb_numbers.py` meldde 23 getallen "niet in de celuitvoer gevonden"; dit zijn
stuk voor stuk handrekening-tussenstappen of externe citatiegetallen (bijv. 1,82 van
Asness e.a.) die al in de eerdere controle zijn nagerekend, geen nieuwe fouten.

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Theorie — alpha long-short (nieuw) | "Met de marktpremie van de simulatie hieronder, 0,5% per maand bij 4,5% volatiliteit, is die Sharpe-ratio 0,11 en de correctieterm 1,01" | handrekening: 0,5/4,5=0,111≈0,11; 1+0,111²=1,0123≈1,01; simulatieparameters `sim["lam_m"]=0.005`, `sim["sd_m"]=0.045` (cel 6) | ok | — |
| Theorie — Fama-MacBeth (herschreven) | `prop-vroege-anomalieen-fm` nu als één bewering: "niets kost, blootstelling één ... en blootstelling nul aan de andere" | 04_18_fama_french.md regel 251: citeert exact deze bewering (long-short-portefeuille, blootstelling één, nul aan de andere regressoren) | ok, label en aanhaling blijven consistent | — |
| Theorie — kernresultaat Berk | teller/noemer-correctie: "E/P en B/M zijn betere thermometers, want hun teller (winst, boekwaarde) schaalt mee met het kasstroomniveau en haalt zo een deel van die ruis weg" (was: "hun noemer haalt een deel van die ruis weg") | economische redenering: $E,\,BE\propto C$, dus $E/P,\,BE/P\propto (k-g)$, wat de $C$-schaal wegdeelt; consistent met het Gordon-model [](#eq-vroege-anomalieen-gordon) | ok, de nieuwe redenering klopt en is preciezer dan de oude | — |
| Kernresultaat Berk — symbool | $h(x)=\log(x-g)$ hernoemd naar $\psi(x)$, ook in oefening 2 (1) | vergeleken met simulatie (a), waar $h$ al de naam is van de tweede beprijsde factor ($f_h$, $\delta_i$) | ok, dit lost een symboolbotsing op die in de eerdere controle over het hoofd is gezien | — |
| Intuïtie — Nicholson (herschreven) | "Bijna tien tegen één verwachtten ze meer van de dure aandelen. Meer stelde zijn enquête niet vast. De latere literatuur citeert Nicholson daarnaast als vroeg bewijs dat juist de goedkope het beter deden. Zijn tabellen hebben we niet kunnen inzien, dus die uitkomst nemen we niet over" | zelfde Nicholson1960-citaat; secundaire bron bevestigt nog steeds alleen de verwachting (analisten favoriseerden dure aandelen), niet een uitspraak over gerealiseerd rendement | ok, preciezer dan de vorige versie: scheidt wat de enquête vaststelde van wat latere literatuur eraan toeschrijft, en neemt de tweede claim expliciet niet over | — |
| Simulatie (b) (nieuwe getallen) | "Het beste van honderd haalt in de steekproef in 93,2% van de gevallen $t > 1{,}96$ en in 13,8% zelfs $t > 3$" | cel 6: fractie t>1,96 = 0,932; fractie t>3 = 0,138 (was 0,925/0,12 vóór het herschikken van cellen, correct bijgewerkt) | ok, exact gelijk aan de nieuwe celuitvoer | — |
| Oefening 2 (4) (nieuw) | "$-0{,}027\%$ per maand per standaarddeviatie ($t=-1{,}57$), en met $\delta$ vrijwel nul ($t=0{,}54$)" | cel 14: log ME zonder $\delta$: −0,027 (t −1,569); met $\delta$: 0,008 (t 0,540) | ok, exact gelijk (−1,569→−1,57; 0,540→0,54; 0,008% is "vrijwel nul") | — |
| Oefening 2 (4) | "Met $\delta$ erbij is de ware coëfficiënt op $\log \mathrm{ME}$ nul, want het verwachte rendement is lineair in bèta en $\delta$" | simulatie-opzet: $k_i = 3\% + 12(0{,}5\%\beta_i + 0{,}4\%\delta_i)$, exact lineair in $\beta_i,\delta_i$ zonder ME-term | ok, correcte modelbewering | — |
| Oefening 4 (verplaatst, geen nieuwe getallen in de tekst) | "coëfficiënt op de log relatieve omvang negatief, het teken van Banz, maar niet significant. De helling op bèta zakt van positief zonder size naar negatief met size. Na 1982 is de size-coëfficiënt positief en niet significant" | cel 16: log relatieve size −0,106 (t −1,552); bèta 0,728→−0,119; na 1982 log relatieve size 0,038 (t 1,140) | ok, alle drie de kwalitatieve beweringen kloppen met de celuitvoer (zelfde cijfers als vóór de verhuizing naar de oefening) | — |
| Oefening 4 — label | `ex-vroege-anomalieen-4` hergebruikt voor nieuwe inhoud (oude K-oefening geschrapt in F4) | `grep -rn "ex-vroege-anomalieen-4" lectures/` | ok, geen andere lecture verwijst naar dit label, dus geen gebroken cross-ref | — |
| Eerder gemelde fout (oefening 4, "K = 513,4") | — | F4-rapport regel 70: "opgelost doordat oefening 4 is geschrapt" | opgelost (oefening met dat getal bestaat niet meer) | — |
| Replicatie — verwachte afwijking / Geslaagd (herschreven) | "Na publicatie verwachten we kleinere value-weighted alpha's, en in Keims periode het grootste deel van de size-premie in januari"; "in beide wegingen ongeveer vier vijfde van de jaarpremie in januari" | cel 9 (VW-alpha's na publicatie kleiner dan origineel voor alle drie) en cel 11 (bijdrage januari Keim VW 0,817, EW 0,782) | ok | — |
| Overige gecontroleerde cellen (toy, theorie-formules, simulatie (a), replicatietabel, januari-tabel, oefeningen 1 en 3) | ongewijzigd t.o.v. de eerste controle, bevestigd door het rapport ("identiek") en opnieuw gecontroleerd tegen de ververste celuitvoer | cellen 1–5, 8–13, 15 | ok, exact gelijk aan de eerdere controle | — |

Geen nieuwe fouten of onzekere beweringen gevonden. Het enige eerder gemelde punt
(oefening 4, "K = 513,4") is verdwenen doordat de oefening is geschrapt, niet doordat
het getal is gecorrigeerd; er is dus niets meer om na te rekenen. Herteld tegen de
huidige tekst: open=0.

Primaire bronnen die niet zijn ingezien, ook na deze controle: de exacte tabellen van
Basu1977, Banz1981 en RosenbergReidLanstein1985 (JF/JFE/JPM zijn paywalled; twee directe
pogingen om Banz' PDF te openen faalden op verbindingsfouten). De lecture citeert daar zelf
geen getallen uit over, alleen een kwalitatieve samenvatting in de kolom "origineel"; die
samenvattingen zijn via secundaire bronnen (websearch) inhoudelijk bevestigd voor Banz
(NYSE, 1936–1975, effect geconcentreerd in de allerkleinste bedrijven) en voor Basu (NYSE,
steekproef rond 1957–1971, lagere K/W geeft hoger risico-gecorrigeerd rendement).
