STATUS deel-3a F6c naadpunten=11 open=5 (projectkeuze) cijfers=L10 8,3 / L11 8,3 / L12 8,3 / L13 8,6

# Naadcontrole Deel III, groep a (L10 t/m L13)

Gelezen: `03_10_merton_icapm`, `03_11_apt_no_arbitrage`, `03_12_consumptie_capm`, `03_13_equity_premium_puzzle` volledig; van `02_09_black_scholes` en `03_14_roll` alleen "Waar we zijn" en "Wat er brak". Eén kalibratie voor de groep: hetzelfde gebrek (een TODO in een docstring, een tabel origineel/hier met lege cellen, telegramzinnen, een kern die niet samenvalt met de kop) kost in elke lecture even veel.

## Eindcijfers

| lecture | 1 | 2 | 3 | 4 | 5 | 6 | 7 | eind | laagste |
|---|---|---|---|---|---|---|---|---|---|
| 03_10_merton_icapm | 8 | 8 | 8 | 9 | 7 | 8 | 9 | 8,1 | 7 |
| 03_11_apt_no_arbitrage | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 8,2 | 8 |
| 03_12_consumptie_capm | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 8,1 | 8 |
| 03_13_equity_premium_puzzle | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 8,2 | 8 |

Geen lecture haalt het streefcijfer van 8,5. L10 heeft een deelcijfer onder 8 (code).

## Naadpunten

Eerst de inhoudelijke tegenspraken (getal, naam, bewering over een andere lecture), daarna de notatie.

### Inhoud

1. **Bewering over de vorige lecture: waar de 75 vandaan komt.**
   - L13, "Waarom de rente de uitweg afsluit", tabel met maatstaven: "Euler-vergelijking met GMM | 1959–1978 | ongeveer 75 | [](#03-12-consumptie-capm)".
   - L12, "Wat het aandelenrendement alleen vraagt": 75 is de $\gamma$ waarbij $\E[g^{-\gamma}R^e] = 0$, een exact opgelost moment. De GMM-schattingen over 1959–1978 staan in "De schattingen": 0,57, −2,02 en −0,02. L12 zegt bovendien in het replicatieblok dat Hansen en Singleton in 1983 maximum likelihood gebruikten.
   - Correct: in L13 de rij noemen "premie alleen: gewogen excess rendement nul".

2. **Naam: "discontofactor" betekent in L12 iets anders dan in L13.**
   - L12, "Opzet en aannames": "De subjectieve discontofactor $\beta \in (0,1)$"; in de simulatietabel "aandeel discontofactor-dak > 1 (waarheid 0,98)". Daar is de discontofactor $\beta$, en heet $m$ de SDF.
   - L13, "Waar we zijn": "In [](#03-12-consumptie-capm) kreeg de discontofactor een theorie: $m_{t+1} = \beta (c_{t+1}/c_t)^{-\gamma}$"; toy-voorbeeld "Stap 1: de discontofactor. $m_h = \ldots$". Daar is de discontofactor $m$.
   - L11, "Opzet en aannames", definieert $m$ als "stochastische discontofactor". Eén naam kiezen voor $m$ (SDF) en één voor $\beta$ (subjectieve discontofactor), en die in L13 volgen.

3. **Bewering over de reeksconventie voor $\mu$ en $\sigma$.**
   - L13, "Wat het voorspelt: waarom de premie klein is": "De $\mu$ en $\sigma$ van [](#eq-consumptie-capm-lognormaal) heten hier $\mu_c$ en $\sigma_c$, omdat $\mu$ en $\sigma$ in deze reeks voor rendementen staan."
   - L12, "Wat het voorspelt: rente en premie bij lognormale groei": $\Delta c_{t+1} \sim N(\mu, \sigma^2)$, en de simulatie "Consumptie groeit met $\mu = 1{,}8\%$ en $\sigma = 3{,}5\%$". L12 volgt de conventie die L13 aan de reeks toeschrijft dus niet. L10 gebruikt $\mu$ en $\sigma$ wel voor het aandeel.

4. **Getal: dezelfde drempel, twee waarden zonder uitleg.**
   - L12, lognormale groei: "De rente stijgt dus met $\gamma$ zolang $\gamma < \mu/\sigma^2$, bij de parameters hieronder $0{,}018/0{,}035^2 \approx 14{,}7$."
   - L13, "Waarom de rente de uitweg afsluit": "De benodigde $\beta$ is het grootst bij $\gamma = \mu_c/\sigma_c^2 = 13{,}8$."
   - Beide kloppen voor hun eigen kalibratie (L12 1,8%/3,5%, L13 de lognormale momenten van Mehra 2003). Geen van beide lectures zegt dat; een lezer die beide naast elkaar legt, ziet twee getallen voor één uitdrukking.

5. **Bewering over de buurlecture Black-Scholes.**
   - L10, "Waar we zijn": "In [](#02-09-black-scholes) bracht Merton de stochastische calculus de financiering binnen."
   - L9, "Wat er daarna kwam": "Merton had dezelfde wiskunde in continue tijd al vanaf 1969 gebruikt voor de portefeuillekeuze van beleggers." Volgens L9 gebeurde het binnenbrengen in 1969, in het werk dat L10 zelf behandelt, niet in de optielecture.

6. **Inhoud uit een latere lecture en de bewering daarover in die lecture.**
   - L11, "Wat er brak": "Dybvig en Ross antwoordden {cite}`DybvigRoss1985` dat het CAPM, met de onwaarneembare markt van {cite:t}`Roll1977`, er niet beter voor staat." Rolls kritiek wordt gebruikt zonder cross-ref naar [](#03-14-roll).
   - L14, "Waar we zijn": "Wat een toets van het CAPM eigenlijk toetst, had nog niemand gevraagd." Historisch klopt dat voor 1977, maar de lezer heeft de onwaarneembare markt drie lectures eerder al als bekend argument gelezen. Of een cross-ref in L11, of in L14 een bijzin dat de kritiek al in de APT-discussie opdook.

### Notatie (symbolen met een andere betekenis in buurlectures)

Elke lecture definieert haar eigen symbool, dus binnen een lecture is er geen fout. Een lezer die de groep achter elkaar leest, ontmoet wel dezelfde letter in een andere rol, terwijl L10 en L13 zelf uitdrukkelijk een reeksconventie aanroepen ("die letter is in deze reeks een prijs van risico", "omdat $\phi$ in [](#03-12-consumptie-capm) de hefboom is").

7. **$\phi$.** L10, "Numerieke oplossing": $\phi$ is de persistentie van de dividendopbrengst in het VAR (0,92). L12, lognormale groei: $\phi$ is de hefboom van het dividend op consumptie. L13, "Opzet": "We schrijven $P$ en niet de $\phi$ van Mehra en Prescott, omdat $\phi$ in [](#03-12-consumptie-capm) de hefboom is." L13 beroept zich op L12, maar L10 gebruikt dezelfde letter anders.

8. **$\eta$.** L10, "Wat het voorspelt": $\eta_t$ is de Sharpe-ratio ("Kim en Omberg schrijven $\lambda$, maar die letter is in deze reeks een prijs van risico"). L11, "De APT met ruis": $\eta_i$ is de pricing error.

9. **$q$.** L10, toy-voorbeeld: $q$ is de waarde van de toekomst ($-q/W_1$). L11, toy-voorbeeld: $q_s$ is de toestandsprijs.

10. **$\delta$.** L10, Kim-Omberg: $\delta = (1-\gamma)/\gamma$. L12, "Evenwicht in de Lucas-boom": $\delta$ is de modulus van de contractie. L13, toy-voorbeeld: $\delta = 0{,}036$ is de afwijking van de groei.

11. **$\pi$.** L11: $\pi_s$ zijn de fysieke kansen, $\pi^\ast$ de risiconeutrale. L12, oefening 1: $\pi = P_{hh} = P_{ll}$ is de persistentie. L13, "Opzet": $\pi$ is de stationaire verdeling.

## Geen tegenspraak gevonden

- Rente-notatie: $R^f$ netto en $1 + R^f$ bruto in L10 (discrete tijd), L11, L12 en L13; $r$ continu in L10 zoals in L9.
- Prijs van risico $\lambda$: $\lambda_m$, $\lambda_x$ (L10), $\lambda_k$ (L11), $\lambda_{\Delta c}$ (L12).
- Breeden 1979 (L10 "voegde alle toestandsvariabelen samen tot één, de consumptiegroei"; L12 "samenvallen tot één bèta, die ten opzichte van consumptie").
- Brownse beweging $W_t$ in L9 en $Z_t$ in L10, met de verklaring in L10.
- Premie bij $\gamma = 2$: 0,25 procentpunt in L12 ($\sigma = 3{,}5\%$) en in L13 ($\sigma_c^2 = 0{,}00125$).
- Doorverwijzingen in "Wat er daarna kwam": L9 → L10 (Merton 1973), L10 → L11 (Ross 1976), L11 → L12 (Lucas en Breeden), L12 → L13 (Mehra-Prescott, Hansen-Jagannathan), L13 → L14 (Roll 1977). L14 "Waar we zijn" verwijst correct naar L13.
- De standaardfout van 2%: overal met dezelfde betekenis en hetzelfde doel (`00-01-rendementen`).
- 6,18% (L13) en 8,3% (setup): L13 legt het verschil uit, en de setup noemt beide.

## Controle 1 (F6c)

Nagekeken in de huidige lectures, na de aanpassingen van §F6-1. Cijfers van record: L10 8,3 (laagste 8), L11 8,3 (8), L12 8,3 (8), L13 8,6 (8).

| nr | naadpunt | status | vindplaats nu |
|---|---|---|---|
| 1 | 75 als GMM-schatting | opgelost | L13, "Alle maatstaven voor de vereiste risicoaversie": "premie alleen: gewogen excess rendement nul". |
| 2 | "discontofactor" voor $\beta$ en voor $m$ | opgelost | L13 noemt $m$ overal "stochastische discontofactor" en $\beta$ "subjectieve discontofactor", zoals L11 en L12. |
| 3 | reeksconventie $\mu$, $\sigma$ | opgelost | L13, "Wat het voorspelt": "om ze te onderscheiden van de momenten van rendementen in deze lecture". |
| 4 | 14,7 tegen 13,8 | opgelost | L12 en L13 noemen beide het getal van de ander en de kalibratie als oorzaak. Kanttekening: L12 haalt de 13,8 uit L13 naar voren, wat STYLE §11.3 verbiedt ("geen inhoud uit een latere lecture"); de uitleg in L13 alleen volstaat. |
| 5 | Merton en de stochastische calculus | opgelost | L10, "Waar we zijn": in L9 leverde de calculus de optieprijs; Merton gebruikte haar al vanaf 1969 voor de portefeuillekeuze. Strookt met L9. |
| 6 | Roll 1977 vóór de Roll-lecture | opgelost | L11 citeert Roll 1977 als citatie, zonder cross-ref; L14, "Waar we zijn": "Het bezwaar dat de markt niet waarneembaar is, dat in de APT-discussie terugkwam, begint hier." |
| 7 | $\phi$ | blijft, projectkeuze | Elk symbool is lokaal gedefinieerd. |
| 8 | $\eta$ | blijft, projectkeuze | idem |
| 9 | $q$ | blijft, projectkeuze | idem |
| 10 | $\delta$ | blijft, projectkeuze | idem |
| 11 | $\pi$ | blijft, projectkeuze | idem |

Nieuwe tegenspraken door de aanpassingen: geen. De herkalibratie van het toy-voorbeeld van L12 ($g_l = 0{,}96$, PD 25 en 27) raakt geen andere lecture; L13 haalt geen toy-getal van L12 aan.
