STATUS 03_11_apt_no_arbitrage F6b-2 words=5419 prose=PASS open=0 cijfer=- min=-

# Rapport 03_11_apt_no_arbitrage (workflow-herziening)

## F0

**Nulmeting.** `words 6453  sent_mean 19.4  sent_p90 35  sent_gt40 13  para_mean 59  dash 31  semicol 44  motief 3  Lnum 0  deel 1  u_form 0  je_form 29  taboo 1  stopw 24  calque 1  engquote 24`. `--where`: r. 61 "epistemisch".

**Vijf grootste problemen.**
1. *Lengte en stofdichtheid*: zeven theorie-subsecties en drie simulaties. De CRR-naar-Black-Scholes-limiet (stelling, bewijs, simulatie, figuur, oefening 2b) en de PCA-simulatie bij vaste $T$ zijn nevenresultaten naast de kern (APT).
2. *Structuur*: imports-cel in *Overzicht* (r. 78); Overzicht zonder vraag-antwoord en lijst; geen routekaart en geen *Samengevat*; toy in drie cellen zonder tabel hand/code; drie simulatievragen; cellen zonder zin ervoor of erna (r. 224, 239, 830, 923, 1013, 1176, 1180, 1221, 1245).
3. *Taal*: 29 keer "je", 44 puntkomma's, 31 gedachtestreepjes, 13 zinnen boven 40 woorden, 24 stopwoorden (vooral "precies"); "epistemische status", "het 2%-motief" (r. 957, 1054), "Deel V" (r. 65).
4. *Notatie*: $R^f$ is in het boek netto, hier overal bruto (toy $R^f = 1{,}1111$, [](#eq-apt-no-arbitrage-drie-namen), $B_t$, $\lambda_0 = R^f$, boom $R = e^{r\Delta}$). *Waar we zijn* verwijst naar drie lectures. Santa-Clara-citaat in het Engels midden in de zin (r. 39); Roll-Ross-citaat in het replicatieblok (r. 1071).
5. *Replicatie en helderheid*: blok ≈ 330 woorden; getallenbrij in proza (r. 1260–1279) zonder tabel origineel/hier en zonder oordeel. Waarom-alinea's zijn bewijsschetsen ("hypervlak", "meetkunde", r. 312–320; H1). Intuïtie doet geen voorspelling (H12); toy-getallen komen niet terug in de APT (H11).

**Eis 2 (grep in `lectures/`).** Elders aangehaald: paginalabel (10 lectures), `thm-apt-no-arbitrage-fundamenteel` en `thm-apt-no-arbitrage-uniek` (05_26), `eq-apt-no-arbitrage-martingaal` (03_17), `rem-apt-no-arbitrage-sdf` (05_26). Inhoudelijk: $q = (R-d)/(u-d)$ (03_17 r. 186), FM-constante "ruim 1,1%" en negatieve marktpremie op de 25 portefeuilles (04_18 r. 389), PCA als decompositie (06_35), Arrow-Debreu-claims (05_29), FM en GRS op de 25 (03_14). Niet aangehaald: `lem-…-scheiding`, `thm-…-crr-bs`, `eq-…-crr`, `eq-…-ck`, `cel-/fig-…-crr`, `cel-/fig-…-pca`.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Intuïtie | Ross-Roll-vermogensbeheerder | 45 | anekdote |
| Intuïtie | note Dybvig-Ross in *Palgrave* | 70 | nevenresultaat; citatie blijft in Overzicht |
| Overzicht | inhoudsalinea en dubbele geschiedenis | 110 | wordt lijst |
| Theorie | lemma scheidend hypervlak, bewijs ingekort | 90 | lemma in het bewijs opgenomen |
| Theorie | note Stiemke/Farkas | 90 | nevenresultaat |
| Theorie | waarom-alinea's complete markten en Harrison-Kreps ingekort | 150 | bewijsschets, geen handeling |
| Theorie | binomiale boom → Black-Scholes: stelling, bewijs, tekst | 250 | nevenresultaat; alleen de één-stapskans blijft (03_17) |
| Theorie | Connor-Korajczyk $T\times T$-afleiding [](#eq-apt-no-arbitrage-ck) | 130 | methode niet gebruikt in de replicatie |
| Theorie | Huberman: inleiding en rij-economieën ingekort | 80 | herhaling |
| Simulatie | boom naar Black-Scholes (tekst, figuur) | 125 | tweede simulatievraag |
| Simulatie | PCA bij vaste $T$ (tekst, figuur) | 240 | derde simulatievraag |
| Replicatie | blok 330 → 240, citaat geparafraseerd | 90 | blok > 250 |
| Replicatie | getallenalinea's → tabel + oordeel | 150 | getallen in proza |
| Wat er brak | Shanken/Dybvig-Ross ingekort | 60 | > 120 per element |
| Oefeningen | ex-1 deel 4, ex-2 deel 2 (convergentie) | 150 | nevenresultaat |
| **totaal** | | **≈ 1.830** | |

**Verwachte lengte.** 6.453 − 1.830 ≈ 4.620; erbij komen vraag-antwoord en lijst, voorspelling in Intuïtie, routekaart, *Samengevat*, lees-zinnen, toy-APT-illustratie, zinnen rond cellen, tabel en oordeel in de replicatie, "Wat dit leert" (≈ 350). Verwacht 4.900 tot 5.100. Geen splitsing.

## F1

**Eindmeting.** `words 5176  sent_mean 14.0  sent_p90 23  sent_gt40 0  para_mean 43  dash 0  semicol 2  motief 0  deel 0  je_form 0  taboo 0  stopw 1  calque 0  engquote 1` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen stderr-uitvoer. Looptijd ≈ 33 s.

**Geschrapt.** Alles uit de F0-schraplijst: Ross-Roll-anekdote en Palgrave-note (anekdote, nevenresultaat); Stiemke-note; lemma scheidend hypervlak (nu één stap in het bewijs); CRR→Black-Scholes-stelling, bewijs, simulatie en figuur (nevenresultaat, niet aangehaald; de één-stapskans [](#eq-apt-no-arbitrage-crr-q) blijft voor 03_17); Connor-Korajczyk-afleiding (methode niet gebruikt); PCA-simulatie bij vaste $T$ (derde simulatievraag); ex-1 deel 4 en ex-2 convergentie (nevenresultaat); Engelse citaten geparafraseerd; replicatieblok ≈ 330 → ≈ 230 woorden.

**Toegevoegd.** Vraag-antwoord en lijst in *Overzicht*, *theorie of feit*-alinea; drie verwachtingen aan het eind van *Intuïtie* (H12), ingelost bij de fundamentele stelling, de exacte APT en Huberman; toy als opzet-tabel, zes stappen, één cel met tabel hand/code; routekaart, lees-zin bij elke vergelijking, handelende waarom-alinea's (H1); toy-getallen terug in de theorie (H11): $\mathbf{q}$, $\pi^* = 0{,}4444$ uit [](#eq-apt-no-arbitrage-crr-q), en de call als exacte APT met één factor (bèta 2,6875, $\lambda_1 = 0{,}1447$); *Samengevat*; parametertabel en handberekening $0{,}08/\sqrt{120}$ in de simulatie; vergelijkingstabel origineel/verwacht/hier met oordeel "Geslaagd"; "Wat dit leert" bij elke uitwerking.

**Notatie.** $R^f$ is nu netto (setup): toy $1 + R^f = 1{,}1111$, $\E^*[x]/(1+R^f)$, $\pi^*_s = q_s(1+R^f)$, $B_t = \prod(1+R^f_j)$, $\lambda_0 = 1 + R^f$, $a = 1/(1+R^f)$, boom $d < 1 + R^f < u$. Geen logs meer nodig. Twee sectieverwijzingen in *Waar we zijn* (02_09, 03_10).

**`nb_outputs`-diff, elk verschil bedoeld.**
- Toy-cellen 2–4 → één cel met tabel hand/code; alle waarden gelijk (q 0,4/0,5; 1+R^f 1,1111; call 0,16 via drie routes; θ −0,3/0,5; m 0,6667/1,25; π* 0,4444; arbitrage 0,04/0/0). Rij "R^f" heet nu "1 + R^f".
- CRR-tabel en -figuur, PCA-simulatie en -figuur, ex-2-cel (CRR-fouten) verdwenen.
- Pricing-simulatie: kolommen vernederlandst, alle waarden identiek (`rng`-volgorde onveranderd).
- Replicatiecellen identiek. Nieuw: vergelijkingstabel (0,833; 0,926; 0,920; 0,893; 3; "0, 2, 1, 1, 3").
- Ex-1 en ex-3 identiek.

**Labels.** Verdwenen, nergens elders aangehaald: `lem-…-scheiding`, `thm-…-crr-bs`, `eq-…-crr`, `eq-…-ck`, `cel-/fig-…-crr`, `cel-/fig-…-pca`. Alle elders aangehaalde labels bestaan nog; ook FM-constante ruim 1,1% en negatieve marktpremie (04_18) staan er.

**Afvinklijst §11.9, wat niet voldoet.** H11 alleen in de theorie: de simulatie is niet op toy-getallen gekalibreerd (zou nieuwe getallen vragen). Overige: ok.

**Open punten.**
1. De claim "alleen HML significant" in het driefactormodel was nergens herleidbaar en is geschrapt; wie hem terug wil, moet $t$-waarden van `fm_ff3` tonen.
2. F2: de Roll-Ross-details (1260 aandelen, 42 groepen) komen via {cite}`ConnorKorajczyk1995` uit de vorige versie; tegen de bron houden.

## F4

**Meting.** `words 5245  sent_mean 14.1  sent_p90 24  sent_gt40 0  para_mean 43  dash 0  semicol 2  stopw 1  calque 0  engquote 1` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen stderr. `nb_outputs` identiek aan F1 (ook de TODO-cel). Nieuw label `cor-apt-no-arbitrage-grenzen`; geen label verdwenen.

**Feitenlijst (1 onjuist, 2 onzeker): opgelost.**
- 3: stap 5 zegt nu "Vermenigvuldig de toestandsprijzen $q_g$ en $q_s$ met $1 + R^f$".
- 7: bij de boom staat nu dat $d$ de daalfactor is, niet het dividend uit [](#eq-apt-no-arbitrage-martingaal); $d_t$ blijft dividend volgens de setup.
- 8: toy-tabel en ex-1 zeggen "uitoefenprijs 1" in plaats van $K = 1$; $K$ is alleen nog het aantal factoren.

**Lezerspunten: alle 15 behandeld.**
1. Zie feit 3. 2. Tabel rendement/verwachting/afwijking voor aandeel en call, met de regel "bèta 1 op de eigen schok" en de deling $1{,}0000/0{,}3721$. 3. $x_i$ ingevoerd als toevalsvariabele met waarden $X_{s,i}$. 4. Deels: de TODO blijft omdat STYLE §5 hem voorschrijft, ingekort tot `# TODO: naar hap.stats`; de docstring noemt de reden (snelheid). 5. "Laagste en hoogste $\mathbf{q}'\mathbf{y}$" en de dualiteitsstelling als grond, met verwijzing naar oefening 1. 6. Geschiedenisalinea ingekort tot Santa-Clara, Ross 1976 en Dybvig-Ross 1987; Cox-Ross-Rubinstein staat nu bij de boom, Cox-Ross bij het toy en Harrison-Kreps-Pliska bij hun stelling. 7. Zin toegevoegd: $K$ blootstellingen plus het budget op nul vraagt $K+1$ activa. 8. Zin toegevoegd: de $T \times T$-matrix is kleiner zodra $N > T$ en geeft dezelfde componenten. 9. Definitie 4 herschreven met "Is er een risicovrij activum ..., dan heet". 10. Stelling gesplitst: uniciteit in de stelling, het interval in `{prf:corollary}`. 11. "Wortel van het aantal maanden $T$". 12. "757 maanden" vervangen door "de volle steekproef". 13. "Dat portefeuilles goed geprijsd zijn en losse aandelen niet, is de derde verwachting". 14. $\mathbf{p} \in \mathbb{R}^N$ bij de eerste keer. 15. Voorbeeld van een testactivum in dezelfde zin.

**Betaald met schrappen.** De geschiedenisalinea (Cox, Rubinstein, Harrison, Kreps, Pliska) is ingekort. Netto +69 woorden (5176 → 5245).

**Navertel-toets.** Het lezersbestand bevat geen navertel-sectie, dus er is geen afwijking te melden.

**Open.** H11 in de simulatie (feitencontrole, open punt 2): niet aangepast, want kalibreren op het toy vraagt nieuwe getallen.

## F5-1

**Meting.** `words 5250  sent_mean 14.1  sent_p90 23  sent_gt40 0  stopw 1  calque 0` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen stderr. De `nb_outputs`-diff tegen F4 toont alleen bedoelde verschillen: rijen m, π* en E[m x] zijn uit de toy-tabel (staan nu als handberekening bij [](#eq-apt-no-arbitrage-drie-namen)); de K=1..5-tabel is verhuisd naar ex-3 (4) met identieke waarden; de eindtabel is gesplitst, met komma's en de cross-sectierij voor K = 3 (1). Alle andere getallen zijn identiek, ook na de lus in `two_pass`.

**Feitelijke fout.** Gedaan: "$K+1$ voorwaarden, dus vanaf $K+2$ activa".

**1 Helderheid.** Gedaan: de grootste eigenwaarde heet $\omega_{\max}$ en de spaarrekening $A_t$. Eén naam per begrip: "factorbèta's" (alias *factor loadings*), en "pricing errors" met als alias alpha en $\eta_i$. Bij $\sqrt{c/N}$ staat het getal 0,45% per maand ($c = 0{,}002$, $N = 100$). Niet gedaan: een getal bij "eigenwaarden groeien met $N$" (geen "voor een 9"-punt, en na het schrappen van de PCA-simulatie is er geen bron voor dat getal).
**2 Opbouw.** Gedaan: Harrison-Kreps ingekort tot drie zinnen plus [](#eq-apt-no-arbitrage-martingaal) (aangehaald in 03_17), de rest is de CRR-knoop. De Connor-Korajczyk-zin is geschrapt. Na de GRS-tabel staat een brug naar de simulatie: 25 is ver van oneindig, en een alpha van 0,09% is met 757 maanden meetbaar. Eén lijn: de tabel met K = 1..5 is naar ex-3 (4) verhuisd.
**3 Taal.** Gedaan: "mispricing" → "verkeerde prijs", "size en value" → "omvang en waarde" (ook in het figuurbijschrift), Chicago en Yale elk met een bijzin, "het punt van" → "wat hun critici aanvoerden". De geschiedeniszin "De bewijzen volgden ..." is geschrapt.
**4 Toy.** Gedaan: de SDF en de risiconeutrale kansen staan nu in de theorie bij [](#eq-apt-no-arbitrage-drie-namen), met handberekening en de lees-zin over de risicopremie. Het toy telt vijf stappen en één mechanisme. De slotalinea eindigt met wat de lezer nu weet.
**5 Code.** Gedaan:
- de TODO staat in de docstring (STYLE §5 vraagt hem, maar niet meer als regel in de cel);
- de tweede stap van `two_pass` is een zichtbare lus over maanden;
- de `np.r_`-schaling is uitgeschreven in drie benoemde regels;
- de $R^2$-tabel wordt met een gewone lus gebouwd;
- de simulatieparameters staan in een dict `sim`;
- de eindtabel gebruikt komma's.

**6 Replicatie.** Gedaan: de getallen na beide premietabellen zijn vervangen door "De tabel laat zien ..." plus één conclusie; alleen de 2%-per-jaar-motiefzin houdt een getal. De eindtabel heeft kolommen origineel / verwacht / hier. Afgewezen: een getal uit de tabellen van Roll en Ross. Die bron is niet ingezien, en STYLE §11.11 (feiten) laat geen getal toe zonder verifieerbare bron. De kolom origineel houdt hun "3 à 4" uit de samenvatting.
**7 Oefeningen.** Ex-3 heeft een deel 4 (K = 1..5) met "Wat dit leert".
**Rubriek-naleesronde.** Het overzicht noemt nu "twee manieren" (toy), de verwijzing "stap 6" is "stap 5" geworden, en "alleen factorblootstelling" is "alleen de factorbèta's" geworden.

## F5-2

1. Feitelijke fout in de brugzin na de GRS-tabel opgelost. In de Huberman-grens is $N$ het aantal aandelen per portefeuille; met $c = 0{,}002$ en 200 aandelen staat de grens $\sqrt{c/N} = 0{,}32\%$ per maand toe, ruim boven de gevonden 0,09%.
2. De docstring van `two_pass` zegt nu "without statsmodels" in plaats van "much faster here".
3. Telegramzinnen uitgeschreven: "Daarna volgt de kern", "Nu schatten we de premies".
Sync, uitvoering met HAP_OFFLINE=1 en `nb_outputs` zijn identiek aan F5-1; prose_stats PASS.

## F6-1

**Meting.** words 5311, prose_stats PASS. Sync en uitvoering met HAP_OFFLINE=1 foutloos, geen stderr; nb_outputs identiek aan F5-1 (alleen tekst gewijzigd). Replicatieblok 221 woorden.

1. **"200 aandelen per portefeuille" (feitelijke fout): opgelost zonder niet-herleidbaar getal.** Het aantal aandelen per portefeuille staat niet in de gecachte data (tabel 4 van French is niet gecachet, en downloaden mag niet). De brugzin rekent daarom terug. Een alpha van 0,09% overschrijdt $\sqrt{c/n}$ pas bij $n > 0{,}002/0{,}0009^2 \approx 2469$ aandelen per portefeuille, dus bij ongeveer 61.700 aandelen in de hele markt. Beide getallen zijn een getoonde handberekening.
2. **Eén kern.** De routekaart noemt de fundamentele stelling het kernresultaat, zoals de kop. De APT is nu "wat de stelling voor verwachte rendementen voorspelt".
3. **Eén naam voor de pricing error.** In de theorie heet ze "pricing error" ($\eta_i$). De simulatie opent met "een pricing error, in de simulatie zoals gebruikelijk $\alpha_i$ of alpha genoemd (de $\eta_i$ van de theorie)". De symbolen blijven ongewijzigd, zoals opgedragen.
4. **Replicatie oordeelt over de vraag van Roll en Ross.** De verwachte afwijking zegt nu dat het aantal geprijsde componenten mag afwijken van hun drie à vier, omdat onze testactiva gesorteerd zijn. Het oordeel is "Gedeeltelijk geslaagd": de vier drempels worden gehaald, maar in de cross-sectie is één component geprijsd tegen drie à vier. De zin over "het punt van de critici" noemt nu het ding zelf.
5. **Naadpunt 6.** Dybvig en Ross: het CAPM staat er niet beter voor, "omdat de marktportefeuille waarop het steunt niet waarneembaar is" {cite}`Roll1977`, zonder link naar 03_14.
6. **Kleine punten uit "Voor een 9".** Congruentie hersteld ("tellen alleen de factorbèta's"). De definitie noemt eerst "toestandsprijzen" en dan *state prices*.
7. **Niet gedaan (geen van de gevraagde punten), ongewijzigd gelaten:** de SDF-opmerking narekenen, de PCA-cel splitsen, lege cellen in de tabel origineel/hier, de TODO in de docstring. De TODO blijft omdat STYLE §5 hem vraagt.

## F6-2

1. Pricing error, één naam in de theorie: "ook alpha genoemd" is geschrapt uit "De APT met ruis". De alias alpha/$\alpha_i$ staat alleen bij de eerste zin van de simulatie.
2. Tabel origineel/hier zonder lege cellen, gesplitst in twee tabellen. De eerste zet de vier drempels uit de verwachte afwijking naast hier, met de zin dat Roll en Ross geen componenten en geen FF-factoren rapporteerden, dus hier geen origineel bestaat. De tweede is een echte origineel/hier-tabel voor het aantal geprijsde factoren (3 à 4 tegen 3 en 1).
3. Voor een 9, gedaan:
   - De SDF-opmerking is nagerekend op het toy-voorbeeld: $b = 0{,}6271$ geeft exact $m = 0{,}6667$ en $1{,}25$. Boven een factorschok van $0{,}9/0{,}6271 = 1{,}435$ wordt $m$ negatief.
   - De PCA-cel is gesplitst in rekenwerk en tabel.
   - Vóór de GRS-tabel staat nu dat de alpha's een tweede vraag zijn.

   Niet gedaan: "Veel perioden" verder inkorten, want het bevat alleen nog de martingaalvergelijking (aangehaald in 03_17) en de CRR-knoop. De TODO in de docstring blijft, want STYLE §5 vraagt hem.
4. Verificatie: sync en uitvoering met HAP_OFFLINE=1 foutloos, geen stderr, prose_stats PASS (5419 woorden). In `nb_outputs` zijn alle getallen gelijk; alleen de celindeling en de tabelvorm zijn veranderd.

## R9-1 (F6b, ronde 9+)

- **Feitelijke fout 1, martingaal (Veel perioden)**: gedaan. "Zonder dividend is de prijs, gemeten in spaarrekeningen, dus een martingaal onder $\pi^*$", met dividend de waarde van aandeel plus herbelegde dividenden; "onder die kansen" in de volgzin.
- **Verbetering 1, labels**: gedaan. Simulatietabel "verworpen, verkeerd/juist gewaardeerd", legenda "alpha van een verkeerd gewaardeerd aandeel (waar)", vergelijkingstabel "componenten met een premie, tijdreeks / cross-sectie (K = 3)". Notebook offline uitgevoerd; `nb_outputs` voor/na verschilt alleen in labels (en pngbytes).
- **Verbetering 3 / hardop-toets (taal)**: gedaan. Wie-zin (Huberman) herschreven tot "laat dus toe … maar niet dat veel aandelen het tegelijk zijn"; $R^2$-zin met onderwerp vooraan; metazin over de vorige cel geschrapt ("De tabel hieronder zet de eigenwaarden en hun aandeel …"); Overzicht "Of iets theorie of feit is, hangt hier af van het soort uitspraak"; "{cite:t}`Huberman1982` bewijst dat door … te schalen".
- **Helderheid, "hij" in Wat het voorspelt**: gedaan ("koopt de handelaar").
- **Helderheid, SDF twee keer gedefinieerd**: gedaan; in de definitie alleen nog "Een SDF (stochastische discontofactor) is een $m$ met …".
- **Beter uitleggen, Intuïtie "hoog"**: gedaan ("Lag zijn verwachte rendement toch boven de rente, dan kochten handelaars die portefeuille tot het verschil verdween").
- **Opbouw, routekaart Theorie**: gedaan; de alinea noemt nu de fundamentele stelling als fundament en de APT als belangrijkste gevolg, in plaats van een opsomming van vier stappen.
- **Opbouw, oefeningslabels als link**: gedaan; "de eerste oefening laat dat met getallen zien" en "zoals de derde oefening laat zien".
- **Code en figuren, leeswijzer**: gedaan; de conclusie over de standaardfout staat nu in een eigen alinea die met de tabel opent ("De tabel laat zien dat …") en de portefeuillekant noemt; de leeswijzer is een aparte overgangsalinea vóór de figuur.
- **Replicatie, $c$-argument**: gedaan; de alinea zegt eerst dat $c$ onbekend is en dat de grens voor 25 portefeuilles daarom geen enkele eindige alpha verbiedt, en gebruikt de simulatie-$c$ alleen nog als "zelfs"-voorbeeld (2469 per portefeuille); 61 700 geschrapt.
- Afgewezen: geen.
- Controles: `prose_stats --check` PASS (5.763 woorden), `nb_numbers` geen nieuwe meldingen (alleen de regel met 0,00000081 veranderd van ">" naar "="), `rewrap` en `jupytext --sync` gedraaid.
