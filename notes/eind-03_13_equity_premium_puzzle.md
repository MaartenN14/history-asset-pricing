STATUS 03_13_equity_premium_puzzle F6c words=5354 prose=PASS open=0 cijfer=8,6 min=8

# Eindbeoordeling: Mehra-Prescott en Hansen-Jagannathan (F6)

## De drie verbeteringen met het meeste effect

1. **De tabel met vereiste $\gamma$ corrigeren en na de replicatie zetten** (feitelijke fout 1; criteria 1 en 2, 8 → 9). De rij "Euler-vergelijking met GMM | 1959–1978 | ongeveer 75" geeft een verkeerde methode op. De tabel staat bovendien vóór Samengevat en haalt vier getallen aan die de simulatie en de replicatie pas later uitrekenen.
2. **Het replicatieblok binnen de vorm brengen en het tweede oordeel laten kloppen met de verwachting** (criterium 6, 8 → 9). "Wat" heeft drie zinnen, "Verschil" drie, "Verwachte afwijking" vier; STYLE §11.7 staat er twee per onderdeel toe. De verwachte afwijking voorspelt al dat consumptie vanaf 1929 gladder is, en toch luidt het oordeel "Gedeeltelijk geslaagd" omdat "de consumptiemomenten van Mehra en Prescott" niet gehaald worden.
3. **De tweede Hansen-Jagannathan-stelling lichter maken** (criterium 1, 8 → 9). Met meerdere activa komen $v$, $m^*_v$ en de V-vorm er in één alinea bij, zonder getal. Eén getal (de grens bij $v = 1/(1+R^f)$ voor markt en T-bill) zou de lezer houvast geven.

## Cijfers

| nr | criterium | gewicht | cijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |
| | **Eindcijfer** | | **8,2** |

(0,3·8 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·8 + 0,05·9 = 8,15, afgerond 8,2.)

## 1. Helderheid van de uitleg (8)

*Goed.*
- Elk resultaat krijgt een getal met kalibratie: 0,25 procentpunt bij $\gamma = 2$ ("vrijwel de 0,26 van het toy-voorbeeld"), 0,362% uit het rooster tegen 0,35%, $\sigma(m)/\E[m] = 0{,}07$ bij $\gamma = 2$, "een vijfde van wat de grens eist".
- Wat het voorspelt: de lezer krijgt uitgelegd waarom de simulatie een andere $\gamma$ geeft dan de boom ("Een echt aandeel beweegt niet perfect met consumptie mee, maar is wel veel volatieler"), en de simulatie rekent het na (27,2 tegen 47,6).
- Symbolen uit het artikel worden vertaald: "Mehra en Prescott schrijven $\alpha$, $\lambda_i$ en $w_i$ waar wij $\gamma$, $g_i$ en $\mathrm{PD}_i$ schrijven", en de keuze voor $P$ in plaats van $\phi$ wordt verklaard.

*Aanmerkingen.*
- Waarom de rente de uitweg afsluit, de tabel met maatstaven: "Euler-vergelijking met GMM | 1959–1978 | ongeveer 75". Zie feitelijke fout 1.
- Hoe het getoetst wordt: "Bij elke kandidaatwaarde $v$ hoort dan een minimale schommeling, en de discontofactor die haar haalt is een lineaire combinatie van de rendementen". De tweede stelling voert $v$, $m^*_v$ en $\boldsymbol{\Sigma}^{-1}$ in zonder getal; de lezer ziet de grens pas in de replicatie.
- Samengevat: "consumptie haalt dat pas bij $\gamma \approx 10$". De cel erboven toont bij $\gamma = 10$ een verhouding van 0,34, onder de 0,37, en de replicatie vindt 15.
- Waarschuwing bij de grens: "Het kwadraat van die Sharpe-ratio ligt ongeveer $N/T$ te hoog." Geleend resultaat zonder bron of één regel uitleg.

*Beter uitleggen.* Wat $v$ economisch is: de prijs van een zekere euro, dus $1/(1+R^f)$ als er een risicovrij activum is. Eén zin met die vertaling maakt de V-vorm leesbaar.

*Voor een 9.* De maatstaventabel corrigeren. Bij de tweede stelling één getal. "Pas bij $\gamma \approx 10$" vervangen door "net boven 10".

## 2. Opbouw en rode draad (8)

*Goed.*
- Het Overzicht geeft vraag en antwoord met getallen (0,35 tegen 6,18). De routekaart wijst de toelaatbare regio als kern aan, en de kop "Het kernresultaat: de toelaatbare regio" bevestigt dat.
- De toy-getallen keren overal terug: 0,26 bij de covariantie en de lognormale premie, 0,9589 als $\E[m]$ in de HJ-controle, $\delta = 0{,}036$ in de simulatie, 0,26 in oefening 1.
- De drie verwachtingen uit de intuïtie worden ingelost ("Zoals de intuïtie voorspelde, tilt meer risicoaversie premie en rente samen op", "Zoals de intuïtie voorspelde, is de premie klein omdat consumptie glad is").

*Aanmerkingen.*
- De tabel met vereiste $\gamma$ staat aan het eind van Theorie en haalt vier uitkomsten aan uit Simulatie en Replicatie ("ook de maatstaven die de simulatie en de replicatie nog uitrekenen"). De simulatie verwijst daarna terug ("De tabel vóór *Samengevat* ... zet deze maatstaf naast de andere"). De lezer leest conclusies voor de berekening.
- Theorie bevat twee HJ-stellingen, een rentesectie met een cel en de maatstaventabel. De grens met meerdere activa wordt pas in de replicatie gebruikt.
- De replicatie heeft drie delen met drie oordelen; het middelste deel (RRA(1) en RRA(2)) zit tussen de twee geciteerde artikelen in.

*Voor een 9.* De maatstaventabel naar het eind van de replicatie of naar Wat er brak. De tweede HJ-stelling kort houden en in de replicatie inzetten.

## 3. Taal (8)

*Goed.* Gemiddeld 15,0 woorden per zin, geen verboden woorden of calques volgens `prose_stats`. De intuïtie is concreet ("Een slecht jaar is een jaar met iets minder groei, geen jaar waarin het eten op is").

*Aanmerkingen.*
- Wat er brak: "Kwalitatief alles wat het moest verklaren." en "Op getallen die we zelf hebben nagerekend." Telegramstijl (§11.1).
- Replicatie: "de equity premium puzzle" (HJ-oordeel). Het Overzicht voerde "premie" in als Nederlandse naam; de Engelse puzzelnaam komt zonder inleiding terug.
- Rentesectie: "Die $\psi$ heet de *elasticity of intertemporal substitution* (EIS, intertemporele substitutie-elasticiteit: ...)". Drie namen in één zin; daarna wordt geen ervan meer gebruikt.
- "discontofactor" betekent hier $m$ (Stap 1, HJ-sectie), terwijl de vorige lecture hetzelfde woord voor $\beta$ gebruikt (zie het naaddocument).

*Voor een 9.* De twee telegramzinnen in Wat er brak volledig maken. "Equity premium puzzle" alleen in het Overzicht als alias.

## 4. Toy-voorbeeld (9)

*Goed.* Opzettabel met $g^{-1}$ en $g^{-2}$ al uitgerekend, vijf stappen van één regel, één codecel, tabel hand/code met negen gelijke rijen, slotzin met wat de lezer weet ("De discontofactor verschilt maar 0,14 tussen de toestanden"). Eén formule die de theorie als eerste afleidt (de premie als covariantie), expliciet als controle aangeduid.

*Aanmerkingen.* De slotzin "De lezer weet nu waar de kleine premie vandaan komt." zegt het, maar herhaalt dan drie getallen; één zin volstaat.

## 5. Code en figuren (8)

*Goed.* `mp_economy` volgt de propositie met een zichtbare dubbele lus voor $R_{ij}$. `iid_economy` noemt in commentaar de stap van het toy-voorbeeld per regel. Vóór elke figuur staat waarop te letten ("Let in de figuur op de gestreepte lijn bij $\gamma = 10$").

*Aanmerkingen.*
- Figuur van de regio: `upper = np.array([prem_grid[admissible][bins == k].max() if np.any(bins == k) else np.nan for k in range(80)])`. Een meerregelige comprehension met conditie, in een cel van circa 33 regels.
- Het rooster van 400 × 400 draait `mp_economy` 160.000 keer met eigenwaarden per punt; de tekst noemt de keuze, maar niet waarom zo fijn.
- Oefening 3: `first_gamma` rekent met `gc[..., None] ** (-gamma_ex3)` en `hit.argmax(axis=-1)` over willekeurige assen. Leesbaar alleen voor wie broadcasting kent.

*Voor een 9.* De grensberekening voor de figuur als benoemde functie met een lus over de bins, los van de plotcel.

## 6. Replicatie en empirie (8)

*Goed.* Tabel 1 wordt met paginanummer en rekenwijze (jaargemiddelde prijzen, p. 148) nagebouwd en komt tot op honderdsten uit. Elk deel heeft een tabel origineel/hier en een oordeel dat met Geslaagd of Gedeeltelijk geslaagd begint. De verwachte afwijking heeft een foutsignaal ("Valt er een met $\gamma \le 5$ binnen, dan zit er een fout in de code").

*Aanmerkingen.*
- Replicatieblok: "Wat" (drie zinnen), "Verschil met het origineel" (drie) en "Verwachte afwijking" (vier) zijn langer dan de twee zinnen per onderdeel.
- Consumptie en de vereiste risicoaversie: "**Gedeeltelijk geslaagd.** ... De consumptiemomenten van Mehra en Prescott halen we niet." De verwachte afwijking zei al "Consumptie vanaf 1929 is gladder dan die van 1889–1978". Het oordeel volgt dus niet uit de verwachting.
- In de HJ-tabel staat "boven 10 (lognormaal, correlatie één)" als origineel; de tekst zegt direct eronder dat Hansen en Jagannathan geen drempel rapporteren.

*Voor een 9.* Het blok inkorten tot twee zinnen per onderdeel. Het tweede oordeel "Geslaagd" of de verwachte afwijking aanpassen. In de HJ-tabel de kolom "verwacht" noemen in plaats van "origineel of verwacht".

## 7. Oefeningen (9)

*Goed.* Oefening 1 is een instap op het toy-voorbeeld met dubbele schommelingen en toont de kwadratische schaal (factor 3,97). Oefening 2 is een afleiding met de gevoeligheid van ruim vier procentpunt per eenheid $\gamma$. Oefening 3 breidt de HJ-replicatie uit met deelperioden en bootstrap. Elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen.* Oefening 3: "Het interval van de vereiste $\gamma$ is even breed" is vaag; de tabel toont 10 tot 26.

## Feitelijke fouten

1. Waarom de rente de uitweg afsluit, tabel met maatstaven: "Euler-vergelijking met GMM | 1959–1978 | ongeveer 75 | [](#03-12-consumptie-capm)". In de lecture over het consumptie-CAPM is 75 de $\gamma$ waarbij het met $g^{-\gamma}$ gewogen excess rendement nul is ("Wat het aandelenrendement alleen vraagt"). Dat is een exact opgelost moment, geen GMM-schatting van de Euler-vergelijking. De GMM-schattingen over 1959–1978 zijn daar 0,57 (T-bill), −2,02 (markt) en −0,02 (beide).

Nagerekend en correct: toy-voorbeeld (0,9488, 0,9002, 1,0183, 1,0370; 0,8912 en 1,0266; 15%; 0,9589 en 4,29%; $k = 0{,}9737$, PD ≈ 37; 1,0825, 1,0085, 1,0455; 0,26; covariantie −0,0025), $2 \cdot 0{,}43 - 1 = -0{,}14$, keten (0,29 en 4,3%; 2,7 en 13,1%), rooster 0,362%, factor zeven (2,66 tegen 0,36), $\sigma_c^2 = 0{,}00125$ en $\mu_c = 0{,}0172$, 0,25 en 1,25 procentpunt, $6{,}18/16{,}67 = 0{,}37$, HJ-controle (0,07; 0,34 en 12,8%; 0,71 en 9,6%), $25/96 = 0{,}26$ en $0{,}43^2 = 0{,}18$, wortels 0,47 en 27,1, maximum bij 13,8, $\beta = 0{,}55$ bij 47,6, ruim vier procentpunt, correlatie 0,37 uit Kocherlakota, 4,7 keer, 0,0022, simulatie (2,6 tot 9,5; 10 tot 71; 30% en 58%; twee derde boven tien; 13,6 en 27,2), tabel 1 (6,22 en 0,75; SE 1,77 en 0,61; 6,92 en 1,34), 8,3% in de setup, RRA(1) 22,0 en RRA(2) 13,0, 2,58 en +0,49, Sharpe-ratio 0,43, $\gamma = 15$ bij 30%, 42 en 43, rente rond 35% en van +15,8 naar −15,6%, oefening 1 (0,8333, 1,1062 met de afgeronde 1,1174, 3,12%, 0,9774, 1,0104; factor 3,97; $\sqrt{6{,}18/0{,}26} = 4{,}9$), oefening 2 (−0,042; 47,6 en 0,546), oefening 3 (0,34 en 11; 0,56 en 27; 0,25 tot 0,64).

## Navertelling in vijf zinnen

Mehra en Prescott kalibreerden een Lucas-economie op Amerikaanse consumptie en vonden dat die met $\gamma \le 10$ en een rente tussen nul en vier procent hooguit 0,35 procentpunt premie oplevert, tegen 6,18 in de data. De reden is dat de premie ongeveer $\gamma$ maal de variantie van consumptiegroei is, en die variantie is klein; wie $\gamma$ opvoert, drijft tegelijk de rente op, en een rente van 0,80% vraagt dan een $\beta$ boven één. Hansen en Jagannathan maakten er een grens van zonder voorkeuren: de discontofactor moet relatief minstens zoveel schommelen als de Sharpe-ratio van de markt, en de consumptie-SDF haalt dat pas bij hoge $\gamma$ en een absurde rente. Een simulatie laat zien dat de standaardfout van de premie de vereiste risicoaversie heel onzeker maakt, maar dat ook bij een ware premie van 3% de puzzel blijft. De replicatie reproduceert tabel 1 van Mehra en Prescott tot op honderdsten en vindt op data tot 2025 dat de consumptie-SDF de grens pas bij $\gamma = 15$ haalt, met een rente van dertig procent.

De navertelling komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen `rapport-03_13_equity_premium_puzzle.md` §F6-1 en de huidige lecture. `prose_stats --check`: 5.354 woorden, PASS. `nb_outputs` is identiek aan de vorige versie.

| punt | status | toelichting |
|---|---|---|
| Feitelijke fout 1 (75 als GMM) | opgelost | De rij heet "premie alleen: gewogen excess rendement nul". |
| Verbetering 1: maatstaventabel | opgelost | De tabel staat onder "### Alle maatstaven voor de vereiste risicoaversie" aan het eind van de replicatie en haalt niets meer vooruit; de simulatie verwijst ernaar. |
| Verbetering 2: replicatieblok en tweede oordeel | opgelost | Elk onderdeel heeft twee zinnen. De verwachte afwijking voorspelt afwijkende momenten én een risicoaversie boven tien; het oordeel "Geslaagd" toetst beide. |
| Verbetering 3: tweede HJ-stelling | opgelost | $v$ is "de prijs van een zekere euro", met het getal $0{,}37/1{,}008 = 0{,}37$ (nagerekend: 0,367). |
| Samengevat en de $N/T$-waarschuwing | opgelost | "net boven $\gamma = 10$"; de waarschuwing legt $N/T$ in een bijzin uit. |
| Naadpunt 2 (discontofactor) | opgelost | $m$ heet overal "stochastische discontofactor", $\beta$ "subjectieve discontofactor"; geen losse "discontofactor" meer. |
| Naadpunt 3 (reeksconventie $\mu$, $\sigma$) | opgelost | "om ze te onderscheiden van de momenten van rendementen in deze lecture". |
| Naadpunt 4 (14,7 tegen 13,8) | opgelost | Eén zin noemt de 14,7 van de vorige lecture en de kalibratie als oorzaak. |

Niet gedaan: de telegramzinnen in "Wat er brak" ("Kwalitatief alles wat het moest verklaren.", "Op getallen die we zelf hebben nagerekend."), "de equity premium puzzle" in het HJ-oordeel, de kolom "origineel of verwacht", de comprehension in de regiofiguur.

**Cijfers na controle 1 (cijfer van record)**

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 9 |
| 2 | Opbouw | 8 | 8 |
| 3 | Taal | 8 | 8 |
| 4 | Toy-voorbeeld | 9 | 9 |
| 5 | Code en figuren | 8 | 8 |
| 6 | Replicatie | 8 | 9 |
| 7 | Oefeningen | 9 | 9 |
| | **Eindcijfer** | 8,2 | **8,6** |

(0,3·9 + 0,2·8 + 0,15·8 + 0,1·9 + 0,1·8 + 0,1·9 + 0,05·9 = 8,55, afgerond 8,6.) Opbouw blijft 8: de tweede HJ-stelling staat nog in Theorie, terwijl alleen de replicatie haar gebruikt. Taal blijft 8 om de telegramzinnen. Het streefcijfer van 8,5 is gehaald, zonder deelcijfer onder 8.
