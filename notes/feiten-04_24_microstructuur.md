STATUS 04_24_microstructuur F4 open=1 punten=15

Feitencontrole van lectures/04_24_microstructuur.md tegen celuitvoer (`nb_outputs.py` op de
.ipynb) en tegen de vier open punten uit notes/rapport-04_24_microstructuur.md §F1.
`nb_numbers.py` meldde 8 getallen zonder cel: 0,9984 (×2), 7,5, 1,32, −0,121, −0,94, 0,764,
7,5 — alle acht zijn hetzij een handberekening die intern klopt, hetzij een gesourced getal
(zie rijen 3, 8, 15, 16 hieronder).

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie | status |
|---|---|---|---|---|---|---|
| 1 | r.121–146 | GM-toy hand: bid 99,60, ask 100,40, spread 0,80; na koop π=0,6, ask1 100,77, bid1 100,00; volgende prijs 100,40 | juist | cel-microstructuur-hand_vs_code (GM-rijen, code komt overeen op afronding ask1 na) | — | ok |
| 2 | r.157–169 | Kyle-toy hand: β=2500, λ=0,0002, prijs 50,70; winsten insider 17.250, noise traders −9.200, market maker −8.050, som 0 | juist | zelfde cel (Kyle-rijen) | — | ok |
| 3 | r.293–296 | GM-noemer 0,9984 bij π=0,6, spread 0,77 na één koop | juist | handafleiding uit [](#eq-microstructuur-gm-spread), intern consistent (1−0,04·0,04=0,9984; 0,768/0,9984≈0,7692) | — | ok |
| 4 | r.389–397 | insiderwinst 20.000 euro, variantie van v van 16 naar 8 | juist | thm-microstructuur-kyle: 0,5·4·10.000=20.000; Σ0=σv²=16, Σ1=Σ0/2=8 | — | ok |
| 5 | r.480–495 | Kyle-recursietabel: λ, Σ_N/Σ_0 en insiderwinst voor N=1,4,10,50 (o.a. λ=0,5 en helft variantie bij N=1; winst 0,95 bij N=50) | juist | cel 3 (`kyle_recursion`) — 0,5000/0,5000/0,5000; N=50: λ_eerste 0,9563, Σ_N/Σ_0 0,0267, winst 0,9506 | — | ok |
| 6 | r.518–527 | restvariantie na 25 ronden 0,528 vs 0,531 theorie; winst gemiddeld 0,950, sd 1,024; t≈4,1 | juist | cel 4 — exacte match; √20·0,950/1,024≈4,15, tekst zegt "ongeveer 4,1" | — | ok |
| 7 | r.679–685 | Roll: spread 0,80 → autocovariantie −0,16; bij 1bp spread/1,5% volatiliteit is ρ1 van orde 10⁻⁵ | juist | handafleiding uit [](#eq-microstructuur-roll): −0,80²/4=−0,16; ρ1≈−1,1·10⁻⁵ | — | ok |
| 8 | r.724–725 | "in de werkversie van Amihuds artikel" verklaren microstructuurschattingen van λ en vaste kosten samen 30% (R²) van de variantie van ILLIQ | **onzeker** | Amihud, werkdocument 2000, p. onbekend; niet ingezien. Externe check: gepubliceerde JFM-versie (Amihud2002, cis.upenn.edu/~mkearns/finread/amihud.pdf) bevat deze regressie/R² niet | schrappen, of expliciet als "werkdocument, niet gepubliceerd, niet nagerekend" merken | opgelost: 30%-claim geschrapt; ILLIQ-alinea zegt nu alleen waarom het ruisende signaal bruikbaar is |
| 9 | r.838–841 | ρ1=−0,16/1,32=−0,121; Φ(−√60·0,121)=Φ(−0,94)≈0,17 | juist | handafleiding, intern consistent (1+0,32=1,32; √60·0,121=0,937≈0,94; Φ(−0,94)≈0,174) | — | ok |
| 10 | r.864–867 | bij s/σe=0,01 is de autocovariantie in 46% (kwartaal) en 48% (jaar) van de steekproeven positief | juist | cel 8 (`roll_positive_share`): 0,456 en 0,482 | — | ok |
| 11 | r.965–975 | 427 van 1168 aandeel-jaren (36,6%) Roll ongedefinieerd, ruim een derde; AAPL/TSLA/AMZN diepst, SMCI ondiepst, ruim twee ordes van grootte ertussen; spreads 60–170bp waar ze bestaat | juist | cel 10 — 427/1168=36,6%; ILLIQ AAPL 0,010 vs SMCI 6,210 (factor 621≈2,8 ordes); Roll-spreads getoonde extremen 62,4–168,4bp | — | ok |
| 12 | r.988–991 | hoogste mediane Roll-spread in 2020 en 2008; mediane ILLIQ daalt ca. een factor dertig | juist | cel 11 — 2020: 248,17; 2008: 186,87 (hoogste twee); ILLIQ 2002 4,133 → 2026 0,143 (factor 28,9≈dertig) | — | ok |
| 13 | r.1013–1025 | AR(1)-helling marktilliquiditeit 0,986; g2=−0,135 (t=−7,87, "ruim 13 procentpunt", "bijna −8"); g1=−0,002 (t=−1,19), klein/negatief/niet-significant | juist | cel 12 — ar1 vertraagd 0,986; innovatie −0,1348 (t=−7,8672); illiq vertraagd −0,0023 (t=−1,1941) | — | ok |
| 14 | r.1098–1102 | laagste liquiditeitsmaanden: okt. 1987 (#1), nov. 1973 (#2), sep. 1998 (#5); correlatie 0,35 (1966–1999) vs 0,36 werkdocument; correlatie −0,23 met eigen Amihud-innovatie | juist | cel 14 — nsmallest: 1987-10, 1973-11, 2008-12, 2002-10, 1998-09 (exact rang 1/2/5); print bevestigt 0,35/0,36 en −0,23 | — | ok |
| 15 | r.1162 | AR(1)-helling illiquiditeit 0,764 per jaar (Amihud, p. 19) | **onzeker** | Amihud, werkdocument 2000, p. 19; niet ingezien; niet in de gepubliceerde JFM-versie teruggevonden (zelfde check als rij 8) | schrappen of "(werkversie)" toevoegen aan de tabelrij | opgelost: 0,764 geschrapt, tabelrij zegt 'hoog, jaarlijkse AR(1)' |
| 16 | r.774, r.1166 | Pástor-Stambaugh-alpha 7,5% per jaar (voorspelde bèta's, 1966–1999) | juist (extern bevestigd) | PastorStambaugh2003 (JPE, juni 2003): secundaire bron bevestigt "7.5% annually" over een periode van 34 jaar, wat overeenkomt met 1966–1999 | — | ok |
| 17 | r.790–791 | Acharya-Pedersen: liquiditeitsrisico draagt ca. 1,1% per jaar bij aan het verschil meest/minst illiquide (1963–1999), grootste deel via Cov(c_i,r_m) | **onzeker** | AcharyaPedersen2005 / NBER w10814, p. 4–5; PDF's (Stern-kopie) niet goed doorzoekbaar binnen dit budget, getal niet zelfstandig geverifieerd | laten staan met bronvermelding; bij twijfel expliciet als ongeverifieerd merken | afgewezen: laten staan met {cite}`AcharyaPedersen2005`, zoals voorgesteld; regeltaal over verificatie hoort niet in de tekst (STYLE §11.12); blijft open |
| 18 | r.1220–1254 | Oefening 1: π3=27/28=0,9643; spread onder 0,10 na 9 kooporders | juist | cel 17 — exacte match (0,9643; "9 kooporders op rij") | — | ok |
| 19 | r.1273–1300 | Oefening 2: bij σu=20.000 is β=5000, λ=0,0001, winst 40.000, Var(v\|p)=8; t≈2,6 | juist | cel 18 — sim. winst 39.903 (theorie 40.000), Var 7,995≈8, t 2,576/2,595≈2,6 | — | ok |
| 20 | r.1329–1338 | Oefening 3: 20% van de vensters boven nul; residuele volatiliteit 12,6%; 71 jaar nodig; intervallen ca. 15pp breed | juist | cel 19 — "fractie vensters... 20%", "12.6%... jaren nodig... 71" | — | ok |
| 21 | diverse | 10 cross-ref-labels (02-06-efficiente-markten, 04-23-behavioral, 04-22-risk-management, 00-01-rendementen, 03-10-merton-icapm, 06-34-factor-zoo, 04-20-voorspelbaarheid, 04-25-industrie, 02-05-crsp-tape, 03-14-roll) bestaan als anchor; LTCM 1998 klopt met 04_22 (r.63,90); McLean-Pontiff klopt met 06_34 (r.52); "dezelfde vijftig" tickers kloppen met 03_14_roll | juist | grep op doelbestanden | — | ok |
| 22 | diverse | 10 citatiesleutels (GlostenMilgrom1985, Kyle1985, Roll1984b, PastorStambaugh2003, SantaClara2026, OHara1995, AmihudMendelson1986, AcharyaPedersen2005, BudishCramtonShim2015, Amihud2002) | juist | aanwezig in references.bib | — | ok |
| 23 | r.1062–1074 | "hap.data mist een loader voor de Pástor-Stambaugh-reeks" | juist | grep in hap/ op "pastor"/"stambaugh": geen match, TODO-comment aanwezig in de cel | — | ok |

Na F4: rijen 8 en 15 opgelost, rij 17 blijft onzeker (bron geciteerd). Open = 1.
aangehaald getal is ofwel exact terug te rekenen uit de celuitvoer, ofwel gesourced (ook als
de bron zelf niet volledig na te trekken was binnen budget).
