STATUS deel-2a F6 lectures=00_00_setup,02_05_crsp_tape,02_07_event_studies naadpunten=9

# Naadcontrole Deel II, groep A: setup, L5 en L7

Eindbeoordelaar A. Tegenspraken tussen de drie lectures onderling en met de notatie van
de setup (r netto simpel, R = 1 + r bruto, R^f netto, p_t en d_t niveaus, ℓ logrendement,
logs aangekondigd), en met de "Waar we zijn" en "Wat er brak" van de buren (L1, L4, L6,
L8). Regelnummers verwijzen naar de `.md`-bestanden in `lectures/`.

Eén kalibratie voor de drie lectures: setup 8,6 (min 8,5), L5 8,1 (min 8), L7 8,6
(min 8,5).

## Naadpunten

| nr | onderwerp | vindplaats 1 | vindplaats 2 | tegenspraak | ernst |
|---|---|---|---|---|---|
| 1 | $R$ bruto of netto | setup r. 165–167 en 173: "Wijkt een origineel paper daarvan af, dan vertalen we naar de tabel hieronder"; $R$ is bruto | L7 r. 264–266: "in de notatietabel van de reeks is $R$ bruto, hier is het met MacKinlay het netto rendement" | L7 kondigt de afwijking aan, maar neemt de notatie van het paper over in plaats van te vertalen, zoals de setup voorschrijft. In de reeksnotatie zou het $r_{i,\tau}$ zijn (L7 gebruikt zelf al $\mathbf{r}_i$ voor de vector). | middel |
| 2 | betekenis van $\alpha_i$ | setup r. 182: "$\alpha_i$ \| pricing error, oftewel Jensen-alpha" | L7 r. 276–283: $\alpha_i$ is het intercept van het marktmodel op netto rendementen, "een statistisch filter, geen theorie over verwachte rendementen" | Het L7-intercept op ruwe rendementen is geen pricing error en geen Jensen-alpha (die vraagt excess rendementen en een prijsmodel). Eén zin in L7 volstaat. | laag |
| 3 | symbool $x$ | setup r. 172: "$x_{t+1}$ \| payoff op $t+1$"; r. 213–215: logs krijgen een eigen symbool of een aankondiging "vanaf hier zijn kleine letters logs" | L5 r. 322–323: $X_t$ is de "log-afstand tot de schrappingsdrempel"; r. 490: "Elk aandeel heeft een log-marktwaarde $x_{i,t}$" | $x$ krijgt in L5 twee logbetekenissen die botsen met de payoff van de setup. Lokaal wel aangekondigd, maar niet met de afgesproken zin. | laag |
| 4 | symbool $D$ | setup r. 367 en 415: "$D/P$ in niveaus", "$\log(D/P)$" ($D$ = dividend) | L5 r. 255 en 268: "$D$ het netto rendement van een geschrapt aandeel" | Hoofdletter $D$ is in de setup het dividend, in L5 een netto rendement. | laag |
| 5 | symbool $\tau$ | L5 r. 334: "$\tau$ het moment van schrappen" (stoptijd) | L7 r. 144 en 255: $\tau$ is eventtijd, "de dag van het event" | Twee opeenvolgende lectures, twee betekenissen; de setup legt $\tau$ niet vast. | laag |
| 6 | inhoud van de Yahoo-cache | setup r. 647–651: "De cache bevat [...] slotkoersen van vijf ETF's, en één momentopname van de optieketen van SPY. [...] Een lecture vraagt daarom alleen op wat al in de cache staat." | L7 r. 824: `hap_data.yahoo(tickers, start="2002-01-01", end="2026-08-01")` voor 50 afzonderlijke aandelen | Volgens de setup bestaan die koersen niet in de cache; `data/cache/` bevat ze wel, plus fondsen, indexreeksen en twee optie-snapshots. De setupzin is verouderd (feitelijke fout 1 in `eind-00_00_setup.md`). | middel |
| 7 | standaardfout bij Fisher en Lorie | L1 r. 746–747: de 9,0% is "een meetkundig gemiddelde"; L1 "Wat er brak": "Het rekenkundig gemiddelde marktrendement was 11,7% over 1926–1960, met een standaardfout van 3,9 procentpunt" | L5 r. 26–28: "de 9,0% per jaar van Fisher en Lorie. Over hun 35 jaar data had dat gemiddelde een standaardfout van bijna vier procentpunt." | L5 hangt de SE van het rekenkundige gemiddelde aan het meetkundige getal. Het getal is ongeveer goed (de setup zegt r. 914–915 dat beide even slecht gemeten zijn), de toeschrijving niet. | laag |
| 8 | naam voor wie blijft | setup r. 710: "meet een onderzoeker alleen de overlevenden" | L5 r. 45, 76, 143 e.v.: "overlevers" | Eén begrip, twee namen. | laag |
| 9 | naam van het vak | setup r. 208: "in de empirische finance" | L7 r. 1008: "van de empirische financiering" | Twee namen; "financiering" is een calque van *finance* en betekent *financing*. | laag |

## Gecontroleerd en consistent

- CRSP: setup r. 705–712, L5 r. 50–56, L6 "Waar we zijn" en L7 r. 30–31 zeggen alle vier
  "maandrendementen van (alle/elk) NYSE-aandeel sinds 1926", gebouwd vanaf 1960 met geld
  van Merrill Lynch, eerste publicatie 1964.
- L4 "Wat er daarna kwam" (meting in 1964 met de CRSP-tape) sluit aan op L5 "Waar we
  zijn"; L5 "Wat er daarna kwam" (het argument van Fama) sluit aan op L6 "Waar we zijn"
  ("Wat nog ontbrak, was een economisch argument").
- L6 "Wat er daarna kwam" (FFJR 1969, de event study) en L7 "Waar we zijn" (Fama 1965 op
  dagkoersen van de dertig Dow Jones-aandelen) kloppen met L6 r. 61.
- L7 "Wat er daarna kwam" (het marktmodel mist een theorie van het verwachte rendement)
  en L8 "Waar we zijn" ("dat marktmodel is een regressie zonder economische inhoud")
  zeggen hetzelfde.
- De standaardfout van 2%: setup r. 78–82 ($20/\sqrt{100}$), L5 r. 62–63 en L7 r. 97–99
  gebruiken dezelfde definitie; L5 en L7 linken naar L1, waar de stelling staat.
- Marktrendement: setup 11,6% over 1201 maanden (r. 308), L5 11,55% over 1200 maanden
  (r. 801, eerste maand valt weg door de vertraging). Geen tegenspraak.
- $r$ netto en $R$ bruto in L5 ([](#eq-crsp-tape-totaal), [](#eq-crsp-tape-delisting),
  $\bar r$, $D$ netto) volgen de setup; $p_t$ en $d_{t+1}$ zijn niveaus.
- $\beta_{i,m}$ in L7 heeft, zoals de setup vraagt, twee indices.

## Controle (F6c)

STATUS deel-2a F6c naadpunten=9 opgelost=9 open=0

Standaard: de setup-notatie; boekconventie "alpha" en "overlevenden".

| nr | onderwerp | status | nu |
|---|---|---|---|
| 1 | $R$ bruto of netto | opgelost | L7 schrijft $r_{i,\tau}$ (netto) en noemt MacKinlays $R$ in één bijzin |
| 2 | betekenis van $\alpha_i$ | opgelost | L7: "hier een intercept op netto rendementen, geen pricing error of Jensen-alpha" |
| 3 | symbool $x$ | opgelost | L5: $Z_t$ en $z_0$ (log-afstand), $s_{i,t}$ (log-marktwaarde) |
| 4 | symbool $D$ | opgelost | L5: $r^{\text{s}}$ |
| 5 | symbool $\tau$ | opgelost | L5: de stoptijd heet $\theta$; L7 zegt dat $\tau$ eventtijd is. Er blijft een kleine overlap: L7 noemt MacKinlays toetsstatistiek $\theta_1$, maar gebruikt die naam niet in formules; geen tegenspraak |
| 6 | Yahoo-cache | opgelost | de setup beschrijft de volledige cache. Let op: de zin erna ("De cache begint in 1993") is daardoor onjuist geworden; die staat als feitelijke fout in `eind-00_00_setup.md`, niet als naad |
| 7 | SE bij Fisher en Lorie | opgelost | L5: 11,7% rekenkundig met SE 3,9 pp, naast de meetkundige 9,0%, gelijk aan L1 |
| 8 | overlevenden | opgelost | setup en L5 schrijven beide "overlevenden" |
| 9 | empirische finance | opgelost | L7 r. 1011 schrijft "empirische finance", gelijk aan de setup |

Cijfers na controle: setup 8,6 (min 8,5, één open fout), L5 8,5 (min 8), L7 8,9 (min 8,5).
