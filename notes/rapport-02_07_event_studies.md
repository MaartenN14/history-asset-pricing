STATUS 02_07_event_studies F6b words=4910 prose=PASS open=0 cijfer=8,6 min=8,5

# Rapport 02_07_event_studies (workflow-herziening)

## F0

**Nulmeting.** `02_07_event_studies.md  words 5098  sent_mean 19.8  sent_p90 35  sent_gt40 12  para_mean 56  dash 23  semicol 28  motief 4  Lnum 0  deel 0  u_form 0  je_form 3  taboo 1  stopw 7  calque 2  engquote 8`. `--where`: r. 72 "epistemisch", r. 871 "Fisher's". Words haalt de grens; bijna alle andere taalmaten falen.

Woorden per sectie: top 112, Overzicht 387, Intuïtie 544, Toy 324, Theorie 1552 (eventtijd 99, marktmodel 143, AR 151, CAR 187, aggregatie 286, toetskracht 132, clustering 223, lange horizon 193, halfwaardetijd 138), Simulatie 520, Replicatie 759, Wat er brak 422, Oefeningen 478.

**Vijf grootste problemen.**
1. *Taal overal* (r. 38–60, 111–118, 572–591, 1033–1058): stapelzinnen (12 boven 40 woorden), alinea's van gemiddeld 56 woorden, 23 gedachtestreepjes, 28 puntkomma's, 3× je-vorm (r. 32, 117), "verrassend" (r. 1088).
2. *Overzicht* (r. 36–90): geen vraag en antwoord vooraf, geen lijst; één alinea van 213 woorden mengt geschiedenis, definitie en telling; imports-cel staat aan het eind van Overzicht (r. 80). *Theorie* (r. 267) zonder routekaart en zonder "Samengevat"; de intuïtie eindigt niet met een voorspelling die de theorie inlost.
3. *Twee simulaties* (r. 642–845): toetskracht én clustering, tegen STYLE §11.7. De clusteringsimulatie draagt geen aangehaald resultaat.
4. *Replicatie* (r. 847–1059): replicatieblok ≈ 390 woorden (> 250); resultaten als getallenalinea (r. 1033–1041) zonder tabel origineel/hier en zonder oordeel "Geslaagd/…"; drie kanttekeningen als lopende tekst.
5. *Projectjargon en citaten*: "2%-motief" (r. 124, 536, 1047), "epistemische status" (r. 72), acht Engelse citaten midden in een Nederlandse zin (r. 47, 141, 587, 634, 1048, …); oefeningen zonder instap en zonder "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** Aangehaald elders: `02-07-event-studies` (02_06, 02_08, 03_14, 04_24, 06_36, 07_37, 08_38, 08_39), `thm-eventstudies-cluster` (07_37 r. 408). Inhoudelijk leunen andere lectures op: de vijftig aandelen van de replicatie (03_14, 06_36, 08_39), de halfwaardetijd die met de meetlat kromp (04_24 r. 27), Busse en Green binnen minuten (08_38 r. 501), het marktmodel als "normaal" rendement (02_08 r. 27, 109). Niet aangehaald: alle overige `eq-`, `fig-`, `cel-`, `ex-`-labels.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | Kothari-Warner-telling, Dolley-details (57/26), methodenlijst in proza | 110 | geschiedenis-detail; lijst vervangt proza |
| Intuïtie | pizza-zin, dubbele uitleg signaal/ruis, Santa-Clara-inleiding ingekort | 110 | herhaling |
| Marktmodel | BW-vergelijking marktmodel/mean-adjusted (80,4 vs 75,6) | 45 | nevenresultaat |
| Aggregatie | MacKinlays slecht-nieuwsgetallen; Patell-factor-uitweiding ingekort | 70 | nevenresultaat |
| Clustering | Kolari-Pynnönen- en Kothari-Warner-citaat, laatste alinea | 90 | propositie blijft (eis 2), citaten niet nodig |
| Lange horizon | Barber-Lyon-biases ingekort tot één zin | 50 | nevenresultaat |
| Simulatie | clusteringsimulatie (twee cellen, figuur, alinea) | 200 | tweede simulatie (§11.7), niet aangehaald |
| Simulatie | Brown-Warner-studieopzet in proza ingekort | 50 | herhaling van Theorie |
| Replicatie | replicatieblok van 390 naar ≤ 250; datumdetails naar code | 140 | §11.7 |
| Wat er brak | Eisfeldt-getallen, instrument-verhuizing ingekort | 80 | kleur, geen element |
| Oefeningen | oefening 3 (bad model) geheel; oefening 1 deel 3 | 260 | Theorie geeft de formule en het getal al |
| **totaal** | | **≈ 1.205** | |

Toe te voegen: routekaart en Samengevat (≈ 130), instap-oefening (≈ 150), tabel origineel/hier met oordeel (≈ 60), lees-zinnen, "Wat dit leert" en H11-koppelingen (≈ 150). **Verwachte lengte:** 5.098 − 1.205 + 490 ≈ 4.380 tot 4.800. Ruim onder 6.000: geen splitsing.

## F1

**Eindmeting.** `words 4285  sent_mean 14.5  sent_p90 24  sent_gt40 0  para_mean 40  dash 0  semicol 10  motief 0  je_form 0  taboo 0  stopw 0  calque 0  engquote 2` — PASS. Onder het doel van 4.500; ruimte voor F4/F5.

**Geschrapt (reden).**
- Clusteringsimulatie (2 cellen, figuur, alinea): tweede simulatie (§11.7); propositie `thm-eventstudies-cluster` blijft (aangehaald in 07_37).
- Patell-toets $J_2$ (`eq-eventstudies-j2`) uit theorie en toy: niet nodig voor de vraag; Patell blijft als bron van de standaardisering in BMP. Toy heeft nu één niet-afgeleide formule.
- Oude oefening 3 (bad model): Theorie geeft formule en getal al. Oude oefening 1 deel 3 (simulatiecontrole): herhaling.
- Kothari-Warner-telling (565 artikelen), Dolley-details, KP- en KW-citaten, MacKinlays slecht-nieuwsgetallen, BW-vergelijking marktmodel/mean-adjusted, Barber-Lyon-biaslijst, Eisfeldt-getallen: nevenresultaten of kleur.
- Replicatieblok 390 → 183 woorden; bronvermelding van de splitsingslijst naar een codecommentaar.

**Toegevoegd.** Vraag/antwoord en lijst in Overzicht; imports naar Toy; toy als recept + vijf stappen + één cel met tabel hand/code; routekaart en Samengevat; lees-zin bij elke genummerde vergelijking; H11-koppelingen (4,9 tegen 3 en CAAR 2% in theorie en simulatie); tabel origineel/hier met oordeel "Geslaagd"; nieuwe instap-oefening (dag 0: factor 1,3, $J_1 = 4{,}628$, handberekening in de tekst); "Wat dit leert:" bij elke uitwerking. Symboolbotsing opgelost: de dagelijkse modelfout heet nu $\eta$ (was $\delta$, ook de niet-centraliteit in de krachtformule).

**Correctie.** Intuïtie: "signaal-ruisverhouding honderd keer gunstiger" klopte niet met de eigen getallen (0,02 tegen 0,5 = 25×); nu "vijfentwintig keer". Theorie: "venster van 250 dagen … de helft" behouden (was juist).

**`nb_outputs`-diff.** Alle aangehaalde getallen gelijk: toy CAAR 2,0 / $J_1$ 2,509 / naïef 3,207; krachttabel identiek (62,9%, 99,2%, 3,5–6%); replicatietabel identiek (14,9%, 3,7, 4,0, 4,7, −0,08%, −0,40, −2,9%, −1,84, −1,18); fits 495 / 1,078 / 0,018. Bedoelde verschillen: toy-cellen samengevoegd tot één tabel hand/code (per-aandeel-tabel en $J_2$ weg); clusteringcellen weg; functies `fit_market_model`/`car_variance` naar een eigen cel in de replicatie; nieuwe cel oefening 1; oefening 2 als Series (zelfde 0,092/0,071/0,060); oefening 3 (was 2): verwerping zonder effect 0,053 → 0,043 en kracht 0,687 → 0,690, doordat de verwijderde clusteringcellen de rng-toestand niet meer verbruiken. De tekst noemt die twee getallen niet letterlijk ("dicht bij 5%", "iets hoger dan 63%"), dus blijft kloppen. Figuren kracht en CAAR byte-gelijk van grootte.

**Afvinklijst §11.9 (alleen wat niet voldoet).** Imports-cel heeft geen zin ervóór (staat direct onder het toy-kopje, zoals `_template.md`). Overige: ok.

**Labels.** Verdwenen: `eq-eventstudies-j2`, `cel-eventstudies-clustering`, `fig-eventstudies-clustering` (nergens aangehaald). Alle overige labels blijven, inclusief `thm-eventstudies-cluster`.

**Open punten.**
1. 08_38 r. 950 schrijft de dagautocorrelatie 0,29 → −0,04 mede toe aan deze lecture; dat getal staat hier niet (en stond er ook niet). Voor de feitencontrole van 08_38.
2. FFJR-tabel 2-waarden nog steeds niet geverifieerd; de replicatie vergelijkt daarom alleen de vorm.

## F4

**Meting.** `words 4636  sent_mean 15.0  sent_p90 25  sent_gt40 0  para_mean 43  dash 0  semicol 10  calque 0  engquote 2` — PASS; `--where` leeg. Sync + execute met `HAP_OFFLINE=1` foutloos; `nb_outputs`-diff tegen `voor-` gelijk aan die na F1 (geen enkel getal veranderd in F4).

**Feitenlijst (5 open, alle opgelost).**
1. "vijfentwintig keer": nu 0,024% per dag, "ruim twintig keer gunstiger", $21^2 \approx 440$ keer minder waarnemingen.
2. Simulatieruis: "op één cel na binnen … bij twintig cellen is één uitschieter te verwachten".
3. "Stijging vooraf groter dan bij FFJR": geschrapt in het oordeel en in de verwachte afwijking ("het niveau vergelijken we niet, want niet geverifieerd").
4. "Hun figuur 2": nu "hun figuur" (blok en tabelkop).
5. Vensterwaarden 120–250 en 1–21: nu "gebruikelijk vele malen meer dan het eventvenster" en "gebruikelijk kort rond het event".
Dubbele betekenissen ook opgelost: toy nu $\hat\sigma^2_{\varepsilon_i}$; CAR-variantie heet $\sigma^2_{\text{CAR},i}$; krachts- en horizonformule $\sigma_\varepsilon$; clusterpropositie $v$; $\theta_1$ weg (MacKinlays 9,28 nu als $J_1$); bewijsvector $(g_1, g_2)$.

**Lezerspunten (15 van 15).** 1 schattingsfout/modelfout: in Overzicht en Intuïtie gedefinieerd en gescheiden, $\eta$ heet "de modelfout". 2 σ: zie boven. 3 ex-datum: gedefinieerd in de Intuïtie, waar de voorspelling staat (aankondiging, dan ex-datum). 4–5 de 2%-alinea herschreven met een herhaling in één regel van wat die 2% was en een expliciete vergelijking. 6 schattingsvenster vóór én na: reden in de replicatie. 7 BMP-noemer: koppeling met de tweede formule en de richting uitgeschreven, 0,95 bij $\bar\rho = 0{,}05$. 8 KP-getallen (ρ ≤ 0,0012; 4,74 → 4,47) in de kanttekening. 9 "8% bovenop de ruisterm". 10 $H$ vervangen door $L_2$. 11 θ: zie boven. 12 Chicago/Yale met één regel uitleg. 13 τ tegenover $t \to t+1$ uitgelegd. 14 "theorie of feit" uitgelegd in de zin. 15 onze kracht bij $N = 50$ (94,7%) naast Brown-Warner (80,4%). Daarnaast: leeswijzer onder de toy-datatabel (H9); de aanname van onafhankelijkheid over de tijd genoemd in het bewijs (H5); $\beta$-term toegevoegd aan Samengevat (H6).

**Navertel-toets.** Afwijking in de Intuïtie, alinea over de standaardfout van 2%: de lezer wist niet wat die 2% was en waar "dezelfde wortel" op sloeg. Die alinea opent nu met de herhaling (20% volatiliteit, honderd jaar, 2 pp) en vergelijkt twee verhoudingen (0,024 tegen 0,5).

**Naadpunten voor andere lectures (niet hier op te lossen).** L8 r. 440 noemt het CAPM "het marktmodel uit 02-07 plus een restrictie", terwijl het marktmodel hier netto rendementen gebruikt. 08_38 r. 950 en r. 454, en 07_37 r. 501 ("binnen minuten"; hier "binnen seconden").

## F5-1

**Meting.** `words 4885  sent_mean 15.0  sent_p90 25  sent_gt40 0  para_mean 44  semicol 11  engquote 3` — PASS, `--where` leeg. Sync + execute (`HAP_OFFLINE=1`) foutloos. `nb_outputs`-diff tegen F4: alleen presentatie (twee `print`-cellen nu Series, TODO-tekst weg, een nieuwe zichtbare cel CAAR/SE met −1: 0,1493 / 0,0373, gelijk aan de toetstabel). Alle aangehaalde getallen en beide figuren zijn ongewijzigd.

**Drie hoofdpunten.**
1. Code: de vier `# TODO: naar hap.stats` zijn weg. `rho` blijft (zonder hem verschuift de rng en veranderen 62,9/99,2/94,7%), maar tekst en DGP-tabel leggen hem nu uit, samen met de blokken van 250, de vorm `(r, 1, T)` en de drift van 0,03% per dag (commentaar + tabelrij). De overlap is een zichtbare lus met benoemde tussenresultaten. De band wordt in een zichtbare cel berekend met `car_variance` (lus per dag); de figuurcel tekent alleen. `print` is vervangen door Series.
2. Opbouw: de simulatie opent met haar uitkomst (63% bij 20 events; 21 dagen mist in vier van de vijf). De open vraag is nu "zit nieuws al in de prijs, of loopt de prijs erachteraan", passend bij wat de replicatie meet. Het Overzicht is daarop aangepast. De halfwaardetijd krijgt een getal voor onze eigen data (binnen een dag), ook in Samengevat. De −2,9% is gekoppeld aan de lange-horizonformule: $\eta \approx -0{,}05\%$ per dag, ruim 10% per jaar.
3. Replicatie en helderheid: de tabel heeft aparte kolommen FFJR / verwachting / hier. Er is geen FFJR-getal toegevoegd, want die zijn niet geverifieerd (feitenregel F4). $R_{i,\tau}$ als netto rendement is gemeld als afwijking van de notatietabel, $\theta_1$ is genoemd, en bij 1,8% staat de herkomst (de replicatiesteekproef).

**Overige aanmerkingen.** Toy: een tabel met $\sum R_i$, $\sum R_m R_i$, residuen en $\hat\sigma^2$ voor A, B en C. De puntkomma-zin en de theorie-of-feit-zin zijn geknipt, "men" → "we". Oefening 3 zegt nu welke kracht wint (69% tegen 63%).

**Naadpunt L6.** "Waar we zijn" zegt nu dat de toetsen daar dagkoersen van de dertig Dow Jones-aandelen gebruikten {cite}`Fama1965,FamaBlume1966` (bestaande keys). De CRSP-tape staat nu als databron voor studies over honderden aandelen.

**Afgewezen.** Geen.
- Restpunt controle 1: openingszin Overzicht nu "vóór of nadat het nieuws bekend wordt"; check PASS, sync gedaan.

## F6-1

**Meting.** words 4927, `--check` PASS, `--where` leeg. Sync + execute (`HAP_OFFLINE=1`) foutloos. `nb_outputs` is identiek aan F5 (alleen proza gewijzigd). `thm-eventstudies-cluster` staat er nog.

**Naadpunten.** (1) Notatie vertaald naar de reeks: $r_{i,\tau}$ en $r_{m,\tau}$ (ook in toy en oefeningen) zijn netto; één zin zegt dat MacKinlay $R$ schrijft. (2) $\alpha_i$: één bijzin dat het hier een intercept op netto rendementen is, geen pricing error of Jensen-alpha. $\tau$: één zin dat het hier eventtijd is, niet het moment van schrappen uit de CRSP-lecture.

**Eindbestand, drie verbeteringen.** (1) Het lijstpunt over de replicatie in het Overzicht scheidt nu "vóór de ex-datum" (replicatie) van het moment van publicatie (Ball en Brown). De halfwaardetijd-alinea is korter: de Budish-zin is geschrapt, 08_38 citeert Budish zelf. (2) De parametervector heet $\mathbf{b}_i$ (was $\boldsymbol\theta_i$), zodat $\theta_1$ alleen MacKinlays naam is. Eén zin zegt waarom BMP hoger uitkomt dan $J_1$ (4,7 tegen 4,0): standaardiseren geeft de volatiele aandelen minder gewicht. (3) "empirische financiering" → "empirische finance"; overal "het CAR" en "het CAAR" (met "zijn").

**Opmerking.** Mijn hulpscript `scratchpad/f6.py` is na gebruik overschreven door de agent van 02_08. Dat had geen gevolg voor deze lecture.
- Naadcorrectie: "alfa" → "alpha" (3×), zoals in Deel I en L8; check PASS, sync gedaan.
- Diffcontrole: de bijzin over τ als "moment van schrappen" in L5 geschrapt (L5 gebruikt nu θ); de vorige zin zegt al dat τ eventtijd is. Check PASS, sync gedaan.
