STATUS 02_09_black_scholes F2 words=5239 prose=PASS open=2 cijfer=- min=-

# Feitencontrole 02_09_black_scholes (F2)

Gelezen: de lecture, `nb_outputs` van het notebook (19 cellen, drie figuren als PNG bekeken), L8 (`02_08_capm.md`, stand van nu), L10 (`03_10_merton_icapm.md`), de aangehaalde plekken in L1, L2, `00_00_setup` (notatietabel), `STYLE.md` §3, `references.bib` en `notes/`. Handberekeningen nagerekend met `uv run python -c`. Statussen: ok, fout, niet herleidbaar, onnauwkeurig (telt niet mee in `open=`).

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Waar we zijn / Overzicht | jaartallen 1961–1973, Sprenkle 1961, Boness 1964, Samuelson 1965, BS en Merton 1973, CBOE april 1973, "binnen enkele jaren" (Black 1989), aankondiging boom van drie stappen, SPY, VIX | `references.bib`; vorige versie (26 april 1973, citaat Black) | ok | – |
| Waar we zijn | "Waarom juist die verwachting de prijs is, kon hij niet zeggen." | L2 r. 422–427: Bachelier onderbouwt de verwachting met de martingaalconditie (de speculant wint gemiddeld niets) | onnauwkeurig | L2 geeft wel een reden (eerlijk spel); hooguit: hij kon niet zeggen waarom de verwachting zonder risicocorrectie de prijs is. |
| Intuïtie | vijftig cent per dollar, twee calls tegen één aandeel | Black 1989 (vorige versie citeerde hem letterlijk); rekenkundig consistent (hedge ratio 0,5) | ok | – |
| Intuïtie | "die fout is gemiddeld nul, ongeacht de drift" | cel 8: gemiddelde wekelijks −0,0097 (SE 0,0041, t ≈ −2,4), maandelijks −0,0194 (SE 0,0083, t ≈ −2,3) | onnauwkeurig | Economisch nul (< 0,5% van de premie), statistisch bij N = 13 en N = 3 niet; zie ook bijschrift hedgefout. |
| Toy-voorbeeld | opzettabel, $S_3$ = 133,1/108,9/89,1/72,9, payoffs 33,1/8,9/0/0; stap 1–3 ($\Delta$ = 1; $B$ = −98,0392; 22,9608; 0,4495; 5,2353; 0,8057; 15,5594; 0,2908; 3,0796); $\Delta_0$ = 0,6240, $B_0$ = −52,0388; stap 5 ($q$ = 0,6; 0,216·33,1 + 0,432·8,9; 10,3603); stap 6 (7,475; 7,0439; 20,3648; 19,1902; 1,2527); tabel hand/code | nagerekend; cel 2 | ok | – |
| Toy-voorbeeld, stap 4 | "$C_0 = 62{,}40 - 52{,}0388 = 10{,}3603$" | nagerekend: 62,40 − 52,0388 = 10,3612; $\Delta_0 S_0$ = 62,3991 | fout | "$C_0 = 62{,}3991 - 52{,}0388 = 10{,}3603$" (of $\Delta_0 = 0{,}62399$). |
| Theorie, opzet | "de aandelenkoers heet $S_t$, zoals in de optieliteratuur en in [](#01-02-bachelier)" | L2 r. 425–450: de koers heet daar $P_t$ (ook in Bacheliers optieformule) | fout | "zoals in de optieliteratuur" (verwijzing naar L2 schrappen), of: "in [](#01-02-bachelier) heette ze $P_t$". |
| Theorie, opzet | GBM, reparatie van Osborne en Samuelson, koers blijft positief | L2 r. 1121–1123 (Osborne 1959 naar log-prijs); bib Samuelson1965b | ok | – |
| Theorie, Itô | Regnaults wet: uitslag van orde $\sqrt{h}$ | L2 r. 293 | ok | – |
| Theorie, Itô | bewijs: $\Var((\Delta W_k)^2) = 2h^2$, $\Var(Q_n) = 2th$; $\tfrac12\sigma^2$ = twee procentpunt bij 20%; rekenkundig/meetkundig uit L1 | nagerekend; L1 r. 42, 131–133 | ok | – |
| Theorie, delta-hedge / formule / pariteit / P&L | PDE, Feynman-Kac, formule, $\Phi(d_2)$ = 0,648 en delta 0,624 in de boom, $\beta_C = (SC_S/C)\beta_S$ (inhoud), ondergrens $\max(0, S-Ke^{-r\tau})$, put-formule, Greeks-tabel, $\Theta + rS\Delta + \tfrac12\sigma^2S^2\Gamma = rV$, afleiding hedge-P&L | nagerekend (afleidingen en tekens kloppen) | ok | – |
| Theorie, note CAPM | "Black en Scholes vonden de vergelijking eerst via het CAPM" | L8 r. 1117–1119 ("gebruikten het in een van hun afleidingen") | ok | – |
| Theorie, voorbeeld | call 4,49, delta 0,56, vega 19,7, "ongeveer twintig cent", pariteit/PDE nul, $\sigma$ = 0,20 terug; Samengevat (0,624; 4,49) | cel 5 | ok | – |
| Simulatie, intro | "Bij de call uit de vorige cel en dagelijks hedgen ($N = 63$) geeft de regel $0{,}44$ euro" | nagerekend: 0,4405; cel 8 | ok | – |
| Simulatie, intro | "met een standaardfout van ongeveer $\sigma/\sqrt{2N}$. Maal de vega is dat de hedgefout." | nagerekend: $\nu\sigma/\sqrt{2N}$ = 0,351 bij $N$ = 63, de regel geeft 0,4405 (factor $\sqrt{\pi/2} \approx 1{,}25$) | onnauwkeurig | "Maal de vega is dat, op een factor $\sqrt{\pi/2}$ na, de hedgefout." |
| Simulatie, intro | Boyle en Emanuel "als eersten", "Hun tabellen hebben we niet kunnen raadplegen" | bib BoyleEmanuel1980; geen getallen uit de bron in de tekst | ok | – |
| Simulatie, controle DK | "tabel 1 van Derman en Kamal: een at-the-money call op één maand ($S_0 = K = 100$, $r = 5\%$, $\sigma = 20\%$) … $N = 21$ en $N = 84$"; gepubliceerde SD $0{,}41$ en $0{,}20$ (tekst en kolom "Derman-Kamal SD") | alleen bib (url); niets in `notes/`; getallen komen uit de vorige tekstversie | niet herleidbaar | Tegen DK (1999) houden; vastleggen in `notes/`. |
| Simulatie, controle DK | "De vuistregel geeft exact hun $0{,}443$ en $0{,}222$" (en de regel [](#eq-black-scholes-dk) zelf, met $\sqrt{\pi/4}$) | cel 7 geeft 0,4432 en 0,2216; dat DK die getallen en die constante noemen, staat nergens in het project | niet herleidbaar | Tegen DK (1999) houden. |
| Simulatie, controle DK | vijf à tien procent boven 0,41/0,20; SE van de SD 0,001; 0,4295/0,2190 = 1,96; 0,41/0,20 = 2,05; gemiddelde binnen 1,5 SE; callpremie 2,512 | cel 7; nagerekend (+4,8%, +9,5%; 0,00136; 1,961; t = −1,37 en +0,8) | ok | – |
| Simulatie, controle DK | oordeel "Gedeeltelijk geslaagd" | cel 7: regel komt overeen, gesimuleerde SD wijkt 5 en 10% af, verhouding en gemiddelde kloppen | ok | Oordeel past bij de tabel (mits de DK-getallen kloppen, zie hierboven). |
| Simulatie, controle DK | "Een andere telling van de hedgemomenten waarschijnlijk wel" | nagerekend: $N+1$ intervallen geeft 0,4295·√(21/22) = 0,420 (nog +2%) maar 0,2190·√(84/85) = 0,218 (nog +9%); de vorige versie stelde zelf vast dat $N+1$ "$N = 84$ ongemoeid" laat | fout | "Een andere telling verklaart hooguit het verschil bij $N = 21$, niet dat bij $N = 84$; de oorzaak is niet vastgesteld." |
| Simulatie, frequenties | 1,86 / 0,92 / 0,43; vuistregel overschat bij kleine $N$; −0,002 (SE 0,002); −0,019 ($t \approx -2{,}3$); < 0,5% van 4,49; 5%-kwantiel −3,25, "bijna driekwart" | cel 8; nagerekend (t = −2,34; 0,43%; 72%) | ok | – |
| Simulatie, figuur hedgefout | "ruim veertig procent van de premie", "bijna twee decaden", helling $-0{,}48$ | cel 8 (1,8609/4,4852 = 41,5%); log10(252/3) = 1,92; titel figuur cel 9 | ok | – |
| Simulatie, figuur hedgefout | "de hedgefout is bij elke frequentie gemiddeld nul … De drift van 10% per jaar is nergens terug te zien" | cel 8: wekelijks t ≈ −2,4, maandelijks t ≈ −2,3 | onnauwkeurig | "gemiddeld vrijwel nul (minder dan een half procent van de premie)". |
| Simulatie, standaardfout | vega × 0,01 = 0,20; 0,43/√120 = 0,04; $t \approx 5$; 1,86/√120 = 0,17 | nagerekend (0,197; 0,0393; 5,0; 0,170) | ok | – |
| Replicatie smirk, blok | Rubinstein JF 1994, Derman-Kani 1994, CJP 2008 over de smirk sinds 1987; "bijna veertig jaar later"; 28 expiraties | bib; vorige versie (citaat CJP) | ok | – |
| Replicatie smirk, blok en tabel | "Derman en Kani tonen 47-daagse opties van 31 januari 1994, met ongeveer 18% bij 90% van de spot en 8% bij 102%"; kolom "origineel" 47 / 0,18 / 0,08 / 0,10 | alleen bib (url); niets in `notes/`; komt uit de vorige tekstversie | niet herleidbaar | Tegen DK (1994) houden; vastleggen in `notes/`. |
| Replicatie smirk | 4521 opties over 28 expiraties; "elke rij daalt van links naar rechts"; vier kortste zonder put op 90%; ATM 7 tot 12%; weekend (waardering vrijdag 11-09-2026, eerste expiratie maandag); 49 dagen 22,1% → 11,0%; 19 van 19; 21 punten bij een week, 3 bij een jaar | cel 10, 11, 12 | ok | – |
| Replicatie smirk, figuur | "Alle krommen dalen, het steilst bij de kortste looptijd" | figuur cel 13: de kromme van 2026-10-09 loopt rechts van ≈ 104% weer op, die van 2026-12-18 rechts van ≈ 108% | onnauwkeurig | "Alle krommen dalen links van de termijnkoers, …". |
| Replicatie VRP | Whaley JPM 2000, Carr-Wu RFS 2009; "we noemen er geen getallen uit" (klopt: geen Carr-Wu-getal in de tekst); VIX 30 kalenderdagen, 21 handelsdagen | bib; cel 14 | ok | – |
| Replicatie VRP | 9188 dagen; 19,5% en 15,5%; 4,0 punten; $t = 12{,}8$; 85%; grootste negatieve maanden 2020 en 2008; figuur en bijschrift | cel 14, 15, 16 | ok | – |
| Replicatie VRP | $t = 0{,}06\sqrt{36}/0{,}20 = 1{,}8$; "bijna dertien"; standaardfout van 2% uit L1 | nagerekend; L1 r. 45–46, label `sec-rendementen-standaardfout` | ok | – |
| Replicatie VRP | label `fig-black-scholes-vrp` bestaat (r. 1065), aangehaald in 04_21 r. 502, 05_29 r. 340 en 646; 05_29 r. 23 "gemiddeld vier volatiliteitspunten" en 04_21 r. 28 kloppen met 0,0399 | grep `lectures/` | ok | – |
| Wat er brak | 19 expiraties, 21 → 3 punten, "corporate liabilities", CJP mispricing, verwijzing naar L10 | cel 11; bib-titels; L10 r. 23–56 | ok | – |
| Oefening 1 | $C_0 = 0{,}216 \cdot 23{,}1/1{,}061208 = 4{,}7018$; fout 0,33 bij $n = 3$, halve cent bij 200, ≈ $1/n$, tekenwisseling | cel 17; nagerekend | ok | – |
| Oefening 2 | $\pm 0{,}99$; −0,98 à −1,00; +1,00; 0,43; 0,61 en 0,55 | cel 18 | ok | – |
| Oefening 3 | 4,85 ($t$ = 15,0), 3,15 ($t$ = 6,1), een derde jaar en twee jaar, 43 jaar | cel 19 | ok | – |
| Cross-refs | alle labels bestaan: `00-01-rendementen`, `01-02-bachelier`, `02-08-capm`, `03-10-merton-icapm`, zes `eq-black-scholes-*`; inhoud L1, L8, L10 op de aangehaalde plek klopt (behalve $S_t$ in L2, zie boven) | grep `lectures/` | ok | – |
| Consistentie L8 | $R^f$: L8 r. 112 en 205 netto ("Rendementen zijn netto"), L9 r. 125 bruto per stap; beide expliciet, L9 volgt de notatietabel | L8; `00_00_setup` r. 157 | ok | Geen actie; verschil wordt in beide lectures benoemd. |
| Consistentie L8 / notatie | "$\beta_C = (SC_S/C)\,\beta_S$" | STYLE §3 en L8: bèta "met index, altijd" ($\beta_{i,m}$) | fout | $\beta_{C,m} = (SC_S/C)\,\beta_{S,m}$. |
| Consistentie L10 | L10 r. 282: "met $Z_t$ een standaard Brownse beweging zoals in [](#02-09-black-scholes)" | L9 noemt de Brownse beweging $W_t$ (en $Z$ een standaardnormale variabele); L10 gebruikt $W_t$ voor vermogen | fout | In L10 "zoals in L9" schrappen of het symboolverschil benoemen; L9 hoeft niet te veranderen. |
| Consistentie L10 | L9 r. 220 "geometrische Brownse beweging", L10 r. 275 "meetkundige Brownse beweging" | L9, L10 | onnauwkeurig | Eén naam kiezen. |
| Consistentie L10 | $r$ continu en constant; $R^{f} = e^{rT/n}$ (oef. 1); L10: $r = \log R^{f}$; $\mu$, $\sigma$ zelfde betekenis; L10 "Merton bracht Itô binnen" past bij L9 r. 330 | L10 r. 270–280 | ok | – |
| Dubbele symbolen | $\Pi$: r. 303 $\Pi = C - \Delta S$ (optie gekocht), r. 490–520 $\Pi_T = X_T - V_T$ (optie verkocht) | L9 | fout | Tweede ander symbool geven (bv. $\mathrm{PL}_T$) of het teken benoemen. |
| Dubbele symbolen | $\Delta$: hedge-ratio (boom, theorie) en aangroei $\Delta X_k$, $\Delta W_k$ (bewijs Itô) | L9 | onnauwkeurig | Aangroei bv. $W_k - W_{k-1}$ uitschrijven. |
| Dubbele symbolen | $u$: stijgfactor (boom, oef. 1) en tijdsvariabele ($S_u$, $\mathrm{d}u$, $M_u$ in Feynman-Kac en hedge-P&L) | L9 | onnauwkeurig | Tijdsvariabele bv. $s$. |
| Dubbele symbolen | $d$: daalfactor naast $d_1$, $d_2$ (en $\mathrm{d}$) | L9 | onnauwkeurig | – |
| Dubbele symbolen | $X$: proces $X_t$ in Itô's lemma en hedgeportefeuille $X$ in het P&L-bewijs; $t$: tijd en $t$-waarde; $\sigma_r$ (werkelijk) naast rente $r$ | L9 | onnauwkeurig | – |

## Diff 1

Gecontroleerd: `git diff --no-index` van de schrijversversie tegen `lectures/02_09_black_scholes.md`, met `nb_outputs` van het notebook (21 cellen) en handberekeningen via `uv run python -c`. Statussen: ok, fout, niet herleidbaar, onnauwkeurig (telt niet mee in `open=`).

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Toy-voorbeeld, stap 2–3 (nieuw) | $B$ bij $S_2=99$: $-39{,}2647$; bij $S_1=110$: $-73{,}0681$; bij $S_1=90$: $-23{,}0969$ | nagerekend met de knoopwaarden één stap verder ($V_{99}=5{,}2353$, $V_{121}=22{,}9608$, $V_{81}=0$) | ok | – |
| Theorie, opzet (nieuw) | "We wijken op drie punten af": $S_t$ i.p.v. $p_t$; $R^f$ in de boom bruto (1,02), niet de netto rente; $r$ hier continu samengesteld, niet een netto rendement | `00_00_setup.md` r. 172–190: notatietabel definieert $R^{f}_{t+1}$ en $r_{t+1}$ als netto | ok | – |
| Voorbeeld, controletabel (nieuw) | "de drie controlerijen onderaan tonen dat pariteit en PDE-residu nul zijn en dat de inverse $\sigma=0{,}20$ terugvindt" | cel 5: pariteitsresidu −0,0000, PDE-residu 0,0000, teruggevonden sigma 0,2000 (put-kolom NaN) | ok | – |
| Simulatie, controle DK (herzien) | "Dit is een controle van de code, geen replicatie: de getallen van Derman en Kamal zijn niet tegen de bron te houden"; dk-tabel met kolommen callpremie/vega | cel 7: callpremie 2,5121, vega/vp 0,1146 | ok | Verbetering t.o.v. eerdere "Gedeeltelijk geslaagd"-claim; sluit aan bij bestaande "niet herleidbaar"-rij hierboven. |
| Simulatie, frequentietabel (nieuw) | grid-tabel met SD P&L/vuistregel per $N$; "De helling is $-0{,}48$, dicht bij de $-0{,}5$" | cel 9: helling log-log −0,4773 | ok | – |
| Label `cel-black-scholes-hedgefout` (verplaatst) | label staat nu op de cel die de figuur maakt, niet op de cel die het grid berekent | grep `lectures/`: r. 781 (label), r. 804 (`:::{figure} #cel-black-scholes-hedgefout`) | ok | – |
| Replicatie smirk, termijnkoerstabel (nieuw) | rijen 0/9/18/27 van `forwards`; "bij ruim twee jaar bijna 9% hoger" | cel 11: 2028-12-15, F/spot−1 = 0,0867 | ok | – |
| Replicatie smirk, log-moneyness (nieuw) | "$k=\log(K/F)$ … 90% van de termijnkoers is $k=\log 0{,}9\approx -0{,}105$" | nagerekend: $\log(0{,}9)=-0{,}10536$ | ok | – |
| Symbool $k$ (nieuw, tweede betekenis) | $k$ wordt hier "log-moneyness" | L9 r. 282/287 gebruikt $k$ al als sommatie-index in het Itô-bewijs ($Q_n=\sum_k(\delta W_k)^2$) | onnauwkeurig | Ver uit elkaar in de tekst, laag verwarringsrisico; desnoods de index in het Itô-bewijs anders noemen. |
| Replicatie smirk, figuurbijschrift (herzien) | "Van diepe puts naar de termijnkoers dalen alle krommen, het steilst bij de kortste looptijd" | smile_table (cel 13): skew 90%-ATM > 0 voor alle 19 expiraties tot 1 jaar | ok | Herstelt de eerder gevonden onnauwkeurigheid (curves rechts van de termijnkoers lopen weer op; bewering is nu tot links van de termijnkoers beperkt). |
| Replicatie smirk, "Verwachte afwijking" (nieuw) | "Amerikaanse puts maken de helling eerder iets steiler dan vlakker" | geen berekening of bron in het project die Amerikaans/Europees vergelijkt | niet herleidbaar | Bron vastleggen of bewering schrappen. |
| Replicatie VRP, blok (nieuw) | "Dertig kalenderdagen zijn ongeveer 21 handelsdagen" | nagerekend: 30 × 5/7 ≈ 21,4 | ok | – |
| Replicatie VRP, "Verwachte afwijking" (nieuw) | "De hele markt beweegt iets harder dan de S&P 500, dus ons verschil ligt eerder iets onder dan boven de premie op de index" | geen vergelijking van de volatiliteit van de Franse marktfactor met de S&P 500 in het project | niet herleidbaar | Bron of berekening vastleggen, of bewering schrappen. |
| Replicatie VRP, Newey-West (nieuw) | "Opeenvolgende dagen delen 20 van de 21 dagen … we nemen 42 vertragingen, twee keer de overlap" | code r. 1055: `lags=42`; $2\times20=40\neq42$ | fout | "twee keer de vensterlengte (21)" i.p.v. "twee keer de overlap", of `lags=40`. |
| Replicatie VRP, resultatentabel (herzien) | tabel met periode, handelsdagen, gemiddelde VIX/RV, verschil, NW SE/t, fractie, meest negatieve maandeinden | cel 16: 1990-01-02 t/m 2026-07-01, 9188 dagen, 0,1945, 0,1546, 0,0399, 0,0031, 12,805, 0,85, 0,011, "2020-02, 2008-09, 2008-08, 2025-03" | ok | – |
| Replicatie VRP, slotalinea (herzien) | "Met $t=12{,}8$ …"; "meest negatieve maandeinden zijn februari 2020, september en augustus 2008 en maart 2025" | cel 16: NW-t 12,805; nsmallest(4) in dezelfde volgorde | ok | – |
| Oefening 1 (nieuw) | "De fout blijft binnen de stippellijnen $\pm1/n$" | code r. 1198 (`ls="--", label=r"$\pm 1/n$"`); nagerekend: 0,3328<0,333; 0,0199<0,02; 0,00498<0,005 | ok | – |

## Diff 2

Gecontroleerd: `git diff --no-index` van de schrijversversie tegen
`lectures/02_09_black_scholes.md`, met `nb_outputs` van het notebook (21 cellen)
en handberekeningen via `uv run python -c`. De nog openstaande fout/niet
herleidbaar-rijen uit F2 en Diff 1 zijn tegen de huidige tekst gehouden: rij 14
(C₀-rekenfout), 15 ($S_t$/L2-verwijzing), 25–26 en 35 (DK-tabelgetallen als
feit), 29 ($N+1$-telling), 48 ($\beta$ zonder index), 52 (dubbele $\Pi$), 74 en
76 (niet-herleidbare beweringen smirk/VRP) en 77 (Newey-West-lags) staan er niet
meer zo in — status "opgelost", telt niet meer mee in `open=`. Rij 49 ($Z_t$ in
L10 waar L9 $W_t$ heeft, `03_10_merton_icapm.md` r. 282) staat nog open.
Statussen: ok, fout, niet herleidbaar, onnauwkeurig (telt niet mee in `open=`).

| vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
|---|---|---|---|---|
| Toy-voorbeeld, knooptabel (nieuw) | koersen per stap 110/90; 121/99/81; 133,1/108,9/89,1/72,9; payoff 33,1/8,9/0/0 | nagerekend $100\cdot1{,}1^{j}\cdot0{,}9^{3-j}$ voor $j=0..3$ per stap; cel 2 | ok | – |
| Theorie, opzet (nieuw) | "Ook $d$ is in de boom de daalfactor, niet het dividend; een dividend heet hier $\delta$, als rendement op de koers" | `00_00_setup.md` r. 178 ($d_t$ = dividend in de reeks); L9 r. 460 ($\delta$ als dividendrendement, ongewijzigd) | ok | – |
| Theorie, opzet (ongewijzigd, nu inconsistent) | "We wijken op drie punten af van de notatietabel van de reeks" | dezelfde alinea somt na deze wijziging vier afwijkingen op: $S_t$/$p_t$; $R^f$ bruto/netto; $r$ continu/netto; $d$/dividend | fout | "op vier punten af" |
| Theorie, note CAPM (herzien) | "de bèta van de optie is $\beta_{C,\text{mkt}} = (SC_S/C)\,\beta_{S,\text{mkt}}$, met 'mkt' de markt (de letter $m$ is in de reeks de SDF)" | `00_00_setup.md` r. 177 ($m_{t+1}$ = SDF); STYLE §3 (bèta altijd met twee indices) | ok | Lost rij 48 hierboven op ($\beta_C$ zonder index). |
| Theorie, risiconeutrale maat (nieuw) | "Het is de maat $Q$ uit [](#thm-efficiente-markten-martingaal): prijzen zijn martingalen na verdisconteren met de rente" | `02_06_efficiente_markten.md` r. 411–420: label bestaat; de stelling zegt precies dit (onder $Q$ is verdisconteerde prijs plus dividend een martingaal) | ok | – |
| Replicatie VRP, slotalinea (herzien) | "Elke verwachting uit het replicatieblok komt uit: de VIX ligt gemiddeld ruim boven de daarna gerealiseerde volatiliteit, met een $t$-waarde ver boven twee, op de meeste dagen, en het verschil slaat om in 2008 en 2020" | cel 17: verschil 0,0399 (>0), Newey-West-$t$ 12,805 (>2), fractie VIX>RV 0,85 (meerderheid), meest negatieve maandeinden 2020-02/2008-09/2008-08/2025-03 | ok | – |
| Wat er daarna kwam (herzien) | "Merton had dezelfde wiskunde in continue tijd al vanaf 1969 gebruikt voor de portefeuillekeuze van beleggers. In 1973 leidde hij er het evenwicht van de hele markt mee af" | `03_10_merton_icapm.md` r. 40–56: Merton1969 (continue tijd, portefeuillekeuze, augustus 1969), in 1973 Merton1973b (marktevenwicht/ICAPM) | ok | – |
| Symbool $\delta$ (nieuw, tweede betekenis) | opzet definieert $\delta$ nu expliciet als "dividend, als rendement op de koers" | L9 r. 284–291 (ongewijzigd): daar is $\delta$ de generieke aangroei in het bewijs van Itô's lemma, $(\delta X_j)^2$, $\delta W_j$ | onnauwkeurig | Laag verwarringsrisico (bewijs staat los van de dividend-toepassing); niet opgenomen in de "dubbele symbolen"-lijst hierboven. |
