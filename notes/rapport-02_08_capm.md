STATUS 02_08_capm F6b words=5367 prose=PASS open=0 cijfer=8,3 min=8

# Rapport 02_08_capm (workflow-herziening)

## F0

**Nulmeting.** `02_08_capm.md  words 6389  sent_mean 20.3  sent_p90 35  sent_gt40 20  para_mean 59  dash 38  semicol 57  motief 3  Lnum 5  deel 0  u_form 3  je_form 0  taboo 1  stopw 16  calque 2  engquote 16`. `--where`: "tot vandaag" (r. 56, 688), "Jensen's" (r. 1064, docstring, telt niet).

Woorden per sectie: top 103, Overzicht 283, Intuïtie 350, Toy 419, Opzet 159, Tangent→markt 308, Bèta-representatie 188, Prestatiematen 128, Jensens alfa/GRS 479, Fama-MacBeth 358, EIV 488, Black 363, Simulatie 420, Replicatie 1214, Wat er brak 507, Oefeningen 622.

**Vijf grootste problemen.**
1. *Replicatie* (r. 950–1242): 1214 woorden; replicatieblok ~450 woorden met alle gepubliceerde getallen in proza; getallenalinea's r. 1141–1169 en 1232–1242 zonder tabel origineel/hier en zonder oordeel "Geslaagd/…".
2. *Taal* overal: sent_mean 20,3, 20 zinnen boven 40 woorden, alinea's gemiddeld 59 woorden, 38 gedachtestreepjes, 57 puntkomma's, 16 stopwoorden, u-vorm (r. 598, 600, 1408), "L4" vijfmaal (r. 131, 170, 187, 298, 450), "motief 1/3" (r. 52, 888, 1092).
3. *Structuur*: imports-cel in Overzicht (r. 68); Overzicht zonder vraag/antwoord en lijst; geen routekaart en geen Samengevat in Theorie; toy met drie codecellen en een figuur, geen tabel hand/code; zes vooruitverwijzingen buiten "Wat er daarna kwam" (03-13, 03-14 tweemaal, 05-26, 04-25, 04-18).
4. *Code*: `argsort(argsort())` en `np.eye(n)[idx]` (r. 821–822); Fama-MacBeth in de simulatie gevectoriseerd met `lstsq`, geen zichtbare lus per maand (r. 796–799, STYLE §11.8); losse globale parameters.
5. *Stellingen en feiten*: `thm-capm-capm` en `thm-capm-grs` bevatten twee beweringen (H3); open bewijzen boven zes regels (`thm-capm-capm`, `thm-capm-zerobeta`); de alfa 0,21% ($t = 2{,}53$) van het laagste bèta-deciel (r. 1260, aangehaald door 08_38) staat in geen celuitvoer; "$R^2$ 60 tot 90%" (r. 1253) past niet bij de tabel (0,81–0,93).

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `02-08-capm` (14 lectures), `eq-capm-tijdreeks` (03_16), `prop-capm-beta` (03_14, 04_18, 05_26), `thm-capm-grs` (04_18, verwijst naar de meetkunde in het bewijs), `thm-capm-zerobeta` (03_14). Inhoudelijk aangehaald: attenuatie door geschatte bèta's (03_14, 04_18), $\hat\gamma_{1,t}$ als portefeuille met bèta één en kosten nul (03_16), bèta en size vallen samen (04_18), 25 size/BM intercept 1,16% en helling −0,37% (04_18, 03_14), alfa laagste bèta-deciel 0,21% met $t = 2{,}53$ (08_38). Niet aangehaald: overige `eq-`, `fig-`, `cel-`, `ex-capm-*`, `thm-capm-capm`, `prop-capm-eiv`.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | biografie Sharpe, tijdschriftnamen, dubbele opsomming methodologie | 120 | geschiedenisdetail |
| Intuïtie | instrument-alinea ingekort | 50 | herhaling |
| Toy | holdingsproza, figuur en bijschrift | 90 | tweede weergave van dezelfde getallen |
| Opzet | zin prijs/verwacht rendement | 30 | nevenzaak |
| Kernresultaat | uitweiding $c = 1$, vooruitblik equity premium | 60 | nevenzaak, vooruitverwijzing |
| Bèta-representatie | SDF-alinea (05-26) | 45 | inhoud uit latere lecture |
| Prestatiematen | hele subsectie Sharpe/Treynor | 128 | niet nodig voor de vraag, niet aangehaald |
| Jensens alfa | fondsgetallen, alinea zuivere schatter GRS, 04-25 | 130 | nevenresultaat |
| Fama-MacBeth | Shanken-warning tot één zin | 110 | verfijning, niet aangehaald |
| EIV | zin "niet geverifieerd", herhaling | 80 | geen functie |
| Black | inkorten | 60 | herhaling |
| Simulatie | Shanken-dekking, herhalingen | 100 | tweede vraag |
| Replicatie | blok naar ≤ 250; getallenalinea's naar tabel origineel/hier | 550 | proza dubbelt tabel |
| Wat er brak | elk element ≤ 120 | 130 | te lang |
| Oefeningen | ex-3 (GRS-meetkunde) weg, instap erbij (netto) | 200 | niet aangehaald; §11.7 |
| **totaal** | | **≈ 1.880** | |

**Verwachte lengte:** 6.389 − 1.880 ≈ 4.500; met taalherziening 4.700 tot 5.100. Onder 6.000 zonder de kern te raken: geen splitsing.

## F1

**Eindmeting.** `words 5190  sent_mean 14.2  sent_p90 23  sent_gt40 0  para_mean 41  dash 0  semicol 7  motief 0  Lnum 0  u_form 0  taboo 0  stopw 1  calque 0  engquote 2`; `--check` PASS. Per sectie: Overzicht 236, Intuïtie 243, Toy 336, Theorie 2.288, Simulatie 397, Replicatie 727, Wat er brak 292, Oefeningen 508.

**Geschrapt** (schraptoets, niet aangehaald): subsectie Prestatiematen Sharpe/Treynor (nevenresultaat); Jensens fondsgetallen en alinea GRS-met-zuivere-schatter (detail); Shanken-warning met formule en Shanken-SE in simulatie en replicatie (verfijning; één zin blijft, correctie ≈ 1,02); SDF-alinea (05-26) en vooruitblikken 03-13, 04-25 (latere inhoud); zin "niet geverifieerd" bij Miller-Scholes; toy-figuur en twee van drie toy-cellen (dubbel); getallenalinea's replicatie (nu tabel origineel/hier); oude ex-3 GRS-meetkunde (niet aangehaald). Nieuw: instap ex-1 (toy met $\gamma_2 = 5$), één-regelafleiding van de vraag [](#eq-capm-vraag).

**Structuur.** Imports-cel naar Toy; Overzicht vraag/antwoord, lijst, geschiedenis met theorie of feit; routekaart en Samengevat; Theorie: Opzet → Kernresultaat → Wat het voorspelt → Zonder vrij lenen → tijdreeks/GRS → Fama-MacBeth → geschatte bèta's. Bewijzen van `thm-capm-capm`, `thm-capm-zerobeta`, `thm-capm-grs` in dropdown met stapkoppen; open alleen `prop-capm-beta`, `prop-capm-eiv`. `thm-capm-capm` bevat alleen de SML (H3). Naadpunten uit 01_04 verwerkt: rendementen en $R^f$ netto, bij eerste gebruik gezegd; geen "L4"; de scalars $A,B,D$ komen niet meer voor, dus A, B, C zijn alleen activa.

**Code.** Simulatie: parameters in `CapmWorld` (dataclass); `argsort(argsort())` en `np.eye(n)[idx]` vervangen door `np.array_split(np.argsort(...))`; Fama-MacBeth stap 2 is een zichtbare lus per maand (`fama_macbeth_gammas`), met de gewichten $(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'$ uit de theorie; rng-volgorde ongewijzigd. Replicatie: functiecel en laadcel gesplitst; `sml_test` zonder Shanken, met alfa van de laagste-bèta-portefeuille; nieuwe tabel origineel/hier (BJS tabel 4 en subperiodes, FM tabel 3). `HAP_OFFLINE=1`: foutloos, geen warnings; hele notebook ca. 120 s, de lus zelf 1,6 s (per cel niet gemeten).

**`nb_outputs`-diff.** Alle aangehaalde getallen gelijk. (1) Toy: drie tabellen en figuur → één tabel met de hand/code met dezelfde waarden. (2) Simulatie: kolom "theorie (prop. EIV)" → "theorie (attenuatie)"; precisietabel nu Series zonder Shanken-rij, rest identiek; figuur byte-identiek. (3) `sml_table`: "t(gamma_1) Shanken" weg, "t(gamma_1) FM" → "t(gamma_1)", nieuwe kolommen alfa laagste bèta; French-decielen 0,207 met $t = 2{,}530$, het getal dat 08_38 aanhaalt en dat eerder in geen enkele cel stond. (4) Nieuwe vergelijkingstabel. (5) Oefeningen: nieuwe instapcel, oude GRS-cel weg, EIV- en industrietabel gelijk. Celnummers verschoven.

**Afvinklijst §11.9, wat niet voldoet.** De functiecel `beta_sorted_portfolios` heeft geen eigen zin erna; de volgende alinea leidt de laadcel in.

**Labels.** Weg: `cel-capm-toy`, `fig-capm-toy` (nergens aangehaald). Nieuw: `eq-capm-vraag`. Alle elders aangehaalde labels bestaan nog, met de inhoud die 03_14, 03_16, 04_18 en 08_38 aanhalen. Vooruitverwijzingen buiten "Wat er daarna kwam": 03-14 (Theorie) en 04-18 (ex-3).

**Open punten.** (1) Build niet gedraaid (grens); nieuwe/gewijzigde refs: `eq-capm-vraag`, `cor-markowitz-separatie`, `eq-markowitz-tangent`, `eq-markowitz-foc`, `thm-markowitz-tweefonds`, `ex-markowitz-1`. (2) Looptijd per cel niet gemeten; de replicatiecellen met `hap.stats.fama_macbeth` zijn het traagst.

## F4

**Meting.** `words 5475  sent_mean 14.2  sent_p90 23  sent_gt40 0  para_mean 43  dash 0  semicol 7  stopw 1  calque 0`; `--check` PASS. Sync en uitvoering met `HAP_OFFLINE=1` foutloos en zonder warnings. `nb_outputs`-diff tegen `voor`: dezelfde verschillen als in F1, plus rijlabel `gamma_m` → `theta_m` (toy, ex-1) en een nieuwe kolom "GRS-grens 5%" in `sml_table` (1,52 bij 25 size/BM, 1,84–1,93 elders). Alle aangehaalde getallen zijn gelijk.

**Feitenlijst (7, alle opgelost).** (1) Het marktmodel: "hier in excess rendementen"; in de ruwe rendementen van L7 is de restrictie $\alpha_i = (1-\beta_{i,m})R^f$. (2) Risicoaversie heet nu $\theta_k$, $\theta_m$ (met één zin waarom), zodat $\gamma_0,\gamma_1$ alleen voor Fama-MacBeth staan; 03_16 haalt $\hat\gamma_{1,t}$ aan, dus die notatie blijft. (3) De constante in het CAPM-bewijs heet nu $\phi$; $\kappa$ is alleen de attenuatiefactor. (4) De residucovariantie heet $\hat{\boldsymbol\Sigma}_\varepsilon$, en $\hat{\mathbf V}$ wordt benoemd. (5) De scalaire fractie heet $s_k = \mathbf 1'\mathbf a_k$. (6) "Na 1963" is nu "na BJS: vanaf 1963 bij French, vanaf 1966 bij onze eigen reeks", ook in Wat er brak. (7) BJS-tabelnummers weggelaten.

**Lezerspunten.**
1–2: $\gamma$ en $\kappa$ ontdubbeld (zie hierboven).
3: in toy stap 3 is (1,5; 1; 2) de oplossing van $\Sigma x = \mu^e$; $1/\theta_1$ en de lening $1{,}25\cdot150$ staan erbij.
4: onze helling in 1957–1965 (−0,76 tegen −0,12 bij BJS) en over 1931–1965 (1,06 tegen een premie van 0,93) staat in de tekst; "verkeerd teken" is nu "bij allebei negatief waar het CAPM een positieve helling voorspelt".
5: de 0,48% van Fama en MacBeth is $\bar\gamma_0 - \bar R^f$, dus excess; ons intercept is 0,27%.
6: $\E[R_z]$ ligt tussen de uitleen- en de leenrente, met beide richtingen (H6).
7: de standaardfout van 2% is in één regel herhaald; de onjuiste "ook dat" in de replicatie is weg.
8: risico of vergissing aangescherpt (een correcte prijs voor een beperking tegenover een foute prijs door overschatting of benchmarkprikkels).
9: de grensjaren staan bij de laadtabel en in het oordeel.
10: de GRS-grens komt uit een cel.
11: de eerste-ordevoorwaarde uit L4 is in één regel uitgelegd.
12: het waarom van "Wat het voorspelt" is nu een handeling.
13: $\gamma$ op portefeuilles is 0,59 en 0,02.
14: Jensen −1,1% per jaar na kosten (getal uit de vorige versie, citatie Jensen1968).
15: 0,6/4,5 heet nu de Sharpe-ratio.

**Naad L4.** Het toy noemt de activa "aandelen, kleine aandelen en obligaties, hier kort A, B en C"; geen verwijzing meer naar "activa A, B, C uit Markowitz".

**Navertel-toets, afwijkingen en wijzigingen.** Overzicht: theorie of feit is nu uitgelegd. Toy: stap 3 (zie punt 3). Zero-beta: punten 1 en 6. Replicatie: subperiodes, teken en grensjaren (punten 4, 5 en 9). Wat er brak: het onderscheid tussen de twee lezingen (punt 8).

**Betaald met.** Treynor-bijzin en een zin over kostenvoet/fondsbeheerders in Wat er brak geschrapt. Words blijft ≤ 5.500 (5.475), maar de ruimte voor F5 is klein.

## F5-1

**Meting.** `words 5495  sent_mean 14.4  para_mean 42  semicol 11`; `--check` PASS. Sync en uitvoering met `HAP_OFFLINE=1` foutloos en zonder warnings. `nb_outputs`: alle aangehaalde getallen gelijk, ook 0,207 met $t = 2{,}530$ (08_38) en 1,164/−0,370 (04_18). BJS-portefeuilles identiek.

**Verbetering 1, code.** `beta_sorted_portfolios` gebruikt nu een eigen `pre_ranking_betas` en een benoemde rangorde (`rank`, 1 = hoogste bèta), een benoemde `qcut` in tien gelijke groepen en een dict per groep in plaats van groupby-transpose; de tekst ervoor legt de stappen uit. De rollende Fama-MacBeth en daarmee de `attrs`-omweg zijn geschrapt (schraptoets: nergens aangehaald, geen nieuwe conclusie). De lokale `stats` heet nu `estimates`. `sml_table` (9×15) is vervangen door twee smalle tabellen: tot en met 1965 origineel/hier (8 kolommen) en na BJS (10 kolommen, drie rijen). Presentatielabels zijn leesbaar (γ0, σ_m/√T, "% per maand"). Oefening 2 zonder de misleidende simulatiekolommen.

**Verbetering 2, replicatie.** Eén oordeelsblok "Gedeeltelijk geslaagd" met per periode een label: na BJS geslaagd, 1948–1965 geslaagd, 1939–1948 niet (γ0 −0,39 tegen +0,44 benoemd), jaren dertig/1931–1965 niet, FM-periode gedeeltelijk. De premieafwijking 0,93 tegen 1,42 staat in de verwachte afwijking (gelijk- tegenover waardegewogen index). Getallen na 1963 staan in een tabel.

**Verbetering 3, helderheid.** Het Overzicht zegt nu "eerste evenwichtstheorie van verwachte rendementen". Bij GRS: ML (delen door $T$) en de $F$-verdeling als eindige-steekproefvorm van een $\chi^2$-toets, met een getal (grens 1,52, gevonden 4,20). In de zero-beta-stelling staat waarom beleggers op de rand zitten (aanname 1). Bij Frazzini-Pedersen staat welke strategie (lage bèta met hefboom, hoge bèta short).

**Overige aanmerkingen.** De simulatie opent met haar conclusie. Toy stap 3 lost het stelsel met de hand op. Het slot van het toy heeft geen metazin meer. De routekaartzin is herschreven. "Frontier" is overal "rand". "value-weighted" is "waardegewogen", size/BM is één keer uitgeschreven en pre-ranking uitgelegd.

**Afgewezen.** Geen.

**Betaald met.** De rollende Fama-MacBeth (tekst en cel), de dubbele oordeelsalinea's en de getallenalinea na 1963. Het resultaat is 5.495 woorden.

## F6-1

**Meting.** words 5367; `--check` PASS. Sync en uitvoering met `HAP_OFFLINE=1` foutloos en zonder warnings. Aangehaalde getallen zijn gelijk: 0,207 met $t = 2{,}530$, 1,164, −0,370 en GRS 4,196/1,521. De labels uit L4 blijven aangehaald.

**Feitelijke fout.** De bewering "netto zoals L4, anders dan de bruto conventie van L1" is geschrapt, ook in het toy. L8 volgt nu de setup: $r$ netto, $R^f$ netto, $R^{e} = r - R^{f}$, met een cross-ref naar [](#00-00-setup). Alle ruwe rendementen $R_i, R_m, R_z, R_p, R_j$ en $\mathbf R$ zijn nu $r$; de excess rendementen blijven $R^{e}$.

**Naadpunten.** De $m$ voor de markt wordt in de Opzet benoemd: "het subscript $m$ staat hier voor de marktportefeuille, niet voor de SDF". "alfa" is overal "alpha" (setup/STYLE §3), ook in de tabellabels. Bij Jensen staat een terugverwijzing naar [](#02-06-efficiente-markten). De schaduwprijzen $\lambda_m,\delta_m$ zijn gemarkeerd als "niet de prijs van risico". Marktvolatiliteit: de schatting van $\theta_m$ gebruikt nu de kalibratie van de simulatie (0,6% en 4,5% per maand, 15,6% per jaar): $\theta_m = 0{,}006/0{,}002025 \approx 3{,}0$ in plaats van 1,5 met 20%. Daarmee heeft de lecture nog maar één waarde voor de volatiliteit.

**Drie verbeteringen.** (1) Notatie, zie hierboven. (2) Het oordeel staat nu in een tabel periode/verwacht/hier/oordeel in plaats van vijf bullets, met de hoofdsteekproef gemarkeerd. (3) De Shanken-alinea is ingekort tot één zin (variantie ≈ 2% te klein); de replicatie noemt de hoofdsteekproef (na BJS: langste reeks, grootste bèta-spreiding).

**Niet in L8 op te lossen.** De naadpunten die alleen L6 of L9 raken (L6 $r$ als log, $M$ in L6, $\mathbb Q$ tegen $Q$, $d$ in L9, Merton-chronologie).

**Na controle F6.** Jensen-zin gecorrigeerd: L6 paste Jensens regressie toe op hedendaagse fondsen, niet op Jensens fondsen; prose_stats PASS, gesynct.
