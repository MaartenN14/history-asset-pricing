# Rapport L4 01_04_markowitz (taak 0, A, B; niet gecommit, niet gebouwd)

**1. Meting (prose_stats)**
- Vóór: `words 6360 | sent_mean 20.4 | p90 37 | gt40 18 | para 65 | dash 59 | semicol 25 | motief 3 | u 27 | je 2 | stopw 9 | calque 1 | engquote 16` (13× FAIL)
- Na: `words 6140 | sent_mean 14.0 | p90 23 | gt40 0 | para 39 | dash 0 | semicol 12 | motief 0 | u 0 | je 0 | stopw 0 | calque 0 | engquote 0` → alleen `FAIL: words=6140`. `--where`: geen treffers.
- Reden voor words: de regels vragen nieuwe tekst (handstappen toy en tangent, aannamelijst, lees-zinnen, routekaart, Samengevat, instap-oefening, vier keer "Wat dit leert:", ca. 700 woorden). Dropdowns tellen mee. Verder inkorten lukt alleen door inhoud te schrappen. Netto 220 woorden minder dan vóór.

**2. Top-5 uit taak 0 en wat ermee gebeurde**
1. Toy (§3.7): drie formules vooruit (min-var, rand, tangent), drie cellen, geen tabel hand/code. Nu één mechanisme (veiligste portefeuille, recept w ∝ Σ⁻¹1, noemer 41), vijf stappen, één cel, tabel hand/code. Theorie leidt het recept als eerste af (λ = 0 in eq-markowitz-foc). A, B, C, D, rand bij 10%, tangent en de figuur staan nu als illustratie in Theorie (H11), met eigen tabellen hand/code.
2. Taal (§3.1/§3.2): 27× u, 59 streepjes, 18 zinnen boven 40 woorden. Alles herschreven.
3. Projectjargon/citaten (§3.3/§3.4): "motief 1" 3×, "epistemische status", "praktijkmotief", 16 lange aanhalingen. Nu de vaste namen; Friedman als blokcitaat met Nederlandse inleiding; Markowitz 1999, DGU-abstract en "de markt is de optimale portefeuille" geparafraseerd.
4. Overzicht/structuur (§3.13): geschiedenis vooraan, imports in het Overzicht, 7 theorie-subsecties, geen routekaart of Samengevat. Nu vraag+antwoord, lijst, één alinea geschiedenis, alinea theorie of feit. Imports bij het toy. Routekaart, 5 subsecties (Opzet → Kernresultaat → Tobin/Roy → Wat het voorspelt → Hoe het toegepast wordt), Samengevat.
5. Replicatie (§3.5/§3.8): blok van ca. 400 woorden met DGU-getallen inline; oordeel na 180 woorden getallen. Blok nu onder 250 woorden, tabel origineel/hier (nieuwe cel), oordeel "Geslaagd" + voorbehoud (SE 0,04).

**3. Verplaatst (niets geschrapt)**
- Bewijs twee-fondsenstelling → `{prf:proof}` dropdown; bewijsidee in hoofdtekst.
- Cauchy-Schwarz (D > 0) → note-dropdown. Notatie E/V van Markowitz → note-dropdown. Tobin liquidity preference → note-dropdown. Friedman-anekdote → note-dropdown. Markowitz' erkenning van Roy, kritieke lijn en semi-variantie → note-dropdown.
- Roy-subsectie samengevoegd met Tobin ("Een risicovrij activum: Tobin en Roy"); eq-markowitz-roy blijft in de hoofdtekst.
- DGU-getallen uit het replicatieblok → tabel origineel/hier. Breakeven "N = 50: meer dan 6000 maanden" → opgave oefening 2.
- Toy-getallen voor rand en tangent → Theorie (zie 2.1). Aannames nu genummerd in Opzet en aangeroepen waar ze werken (H5).
- Nieuwe instap `ex-markowitz-instap` (correlatie A–B op nul; 9/49, 4/49, 36/49; σ = 8,57%). `ex-markowitz-1` (zero-beta, door de CAPM-lecture aangehaald) staat nu tweede, met dezelfde inhoud.
- Vooruitverwijzing CAPM in de covariantiesectie is weggelaten (belofte staat al in het Overzicht). Twee vooruitverwijzingen blijven: CAPM (Overzicht) en SDF/HJ.

**4. nb_outputs-diff (vóór ↔ na)**: alle getallen gelijk, drie figuren byte-gelijk (63132/41776/77112).
- Bedoeld: toy-cel en theorie-cellen tonen nu tabellen "met de hand / code" in plaats van de twee oude tabellen (zelfde waarden, 4 decimalen). Nieuwe cel: tabel origineel/hier DGU. Nieuwe cel: instap-oefening. Kolomnamen voluit Nederlands in de Sharpe-tabel en de positietabel. Celnummers verschoven.
- rng-volgorde ongewijzigd: nieuwe cellen trekken geen random getallen.
- Tussenstand A: `$TEMP/01_04_markowitz-na-A.txt`. Verschil A→B: één handwaarde 0,1560 → 0,1559 (was afgerond) en `.astype(float)` op de DGU-tabel, zodat die op 4 decimalen toont.
- Execute-log (laatste regels): `[jupytext] Executing notebook with kernel python3` / `[jupytext] Warning: Notebook is not trusted` / `[jupytext] Writing lectures/01_04_markowitz.ipynb (destination file replaced ...)`, exit 0. Geen stderr of errors in de cellen. De enige waarschuwing is de IPKernel-TCP-melding van de omgeving.

**5. Afvinklijst §11.9**: alles voldoet, behalve:
- words (zie 1).
- H11: de toy-getallen komen terug in Theorie en Replicatie (min-var), niet in de Simulatie. Dat kan niet zonder de uitvoer te veranderen.
- Oefeningen: vier in plaats van drie (instap, afleiding, simulatie, replicatie). Er is geen oefening geschrapt.
- Overige punten: ok.
- Tekstcorrecties: bijschrift simulatie zei "tienduizend-en-een steekproeven", het zijn er 2000. DGU-recept: "rendement van maand t+1" → "maand t", zoals de code doet.

**8. Open punten**
- `words` blijft boven 5500. Beslissing eigenaar: drempel voor deze lecture accepteren of stof naar een andere lecture verplaatsen.
- Santa-Clara-parafrase in "Risico of vergissing" heeft geen `{cite}` (had hij vóór ook niet). Er is geen bib-key toegevoegd.
- Tijdens het werk heeft een ander proces `tools/prose_stats.py` aangepast (motief-regex). Die wijziging is niet van mij en ik heb niets teruggedraaid.
- Taak A en B zijn in één schrijfronde uitgevoerd. De structuur stond vast vóór het polijsten. De tussenstand van de uitvoer na A is bewaard.

## Lezersronde (taak C)

**Per H-regel (opgelost / afgewezen)**
- H1 5/1. Opgelost: Roy (Intuïtie), kernresultaat, twee fondsen, Tobin en 1/N; elk waarom beschrijft nu een handeling met een richting. Afgewezen: de Roy-zin in het Overzicht. Dat is geschiedenis, geen waarom-alinea.
- H2 11/0. De standaardfout van 2% staat nu in één regel in het Overzicht en in de 2%-sectie, met verwijzing naar de lecture over rendementen. Verder uitgelegd: de bèta-vorm van het CAPM; $m$ (SDF); bruto of netto (toy en $R^f$ zijn netto); $\Phi$; $\beta_{i,p}$; de risicotolerantie van 50; Bayes-Stein; Santa-Clara (wiens terugblik de reeks volgt); Chicago- en Yale-lezing.
- H3 2/0. "Twee fondsen volstaan" staat nu buiten de stelling. De bewijsstappen hebben een kop. De omgekeerde richting blijft in de stelling, omdat het CAPM-bewijs zich via thm-markowitz-tweefonds op precies die richting beroept.
- H4 5/0. Toy-getallen toegevoegd voor $\lambda$ en $\delta$ (0,368 en −0,0125) en voor de Roy-grens (17% tegen 0,8% onder normaliteit). Verder: $N/T = 0{,}083$ tegen $S^2 = 0{,}021$, de betekenis van de risicotolerantie, en de bias in de simulatie ($N/T = 10/120$).
- H5 5/0. Aanname 4 toegevoegd (onbeperkt lenen en uitlenen). Aanname 2 staat bij de tangent en bij de uniciteit. Homogene verwachtingen zijn benoemd, en "onafhankelijke jaren" staat bij $\sigma/\sqrt{T}$.
- H6 3/0. Nu in beide richtingen gelezen: $R^f$ stijgt of daalt (7,24% bij $R^f = 0$, 8,22% bij 2%), de correlatie stijgt of daalt, en $\sqrt{T}$ en $N/T$ staan in Samengevat.
- H7 9/1. Eén naam per begrip: rand, minimum-variantieportefeuille (alias één keer ingevoerd), premie, turnover, risicovrij activum, idiosyncratisch risico (alias eigen risico), mean-variance-portefeuille, 1/N. Risico/volatiliteit/standaarddeviatie is één keer gelijkgesteld; ware optimum is gedefinieerd. Afgewezen: "raakpunt" en "efficient frontier" blijven, als meetkundige omschrijving en als eenmalig ingevoerde vakterm.
- H8 5/0. "Dat" vervangen door het ding zelf: de kern, de verhoudingen, de rangorde, de bias bij één $N/T$, de schade in de posities.
- H9 6/0. Elke `###` opent nu met een bewering. Na de opzettabel van het toy en na de parametertabel van de simulatie staat eerst wat de tabel laat zien.
- H10 7/0. Voorbeelden toegevoegd bij: tweede-orde benadering (Taylor), $D$ = 0 bij gelijke $\mu$, de richting van $\Sigma^{-1}\mathbf{1}$ in het toy, semi-variantie, impliciete prior, risk parity en beprijsd risico.
- H11 1/1. De replicatie noemt nu 8,83% tegen 10%. Afgewezen: een toy-getal in de simulatiekalibratie, omdat dat de uitvoer zou veranderen.
- H12 2/0. De eerste voorspelling wordt in de Theorie expliciet ingelost. "Wat het voorspelt" verwijst terug naar de intuïtie.

**Navertel-afwijkingen**
- *Het kernresultaat*: de lezer zag de parabool en de twee fondsen als kern. Bedoeld was de eerste-ordevoorwaarde: in het optimum is de covariantie met de portefeuille evenredig met het verwachte rendement. Veranderd:
  - de routekaart noemt die voorwaarde als kern;
  - de subsectie opent met die bewering;
  - de tekst noemt eq-markowitz-foc nu "het kernresultaat";
  - vóór $A, B, C, D$ staat een schakelzin: de voorwaarde zegt hoe een optimum eruitziet, en voor de rand moeten $\lambda$ en $\delta$ nog vast;
  - Samengevat begint met deze voorwaarde.
- *De standaardfout van 2%*: de lezer zag alleen 6,3 procentpunt. Bedoeld was de naam uit de lecture over rendementen: $20/\sqrt{100} = 2$ procentpunt over honderd jaar. Die regel staat nu in het Overzicht en in de sectie. De 6,3 staat daarna als toepassing op tien jaar.
- Spoor 3 (Risico of vergissing): er staat nu een brugzin. Markowitz heeft geen evenwicht, maar zijn schattingsprobleem vraagt waarom geschatte gemiddelden zo weinig opleveren; daarvoor zijn de twee vaste lezingen.

**Verificatie**
- prose_stats `--check`: `words 6935 | sent_mean 14.5 | p90 25 | gt40 0 | para 42 | dash 0 | semicol 15 | overige 0`. Alleen `words` faalt; die grens is door de coördinator geaccepteerd. `--where`: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0, laatste regel `[jupytext] Writing lectures/01_04_markowitz.ipynb (...)`.
- nb_outputs: na-B → na-C is leeg; er is alleen tekst veranderd, geen code. Tegen na-A staan alleen de twee bekende verschillen uit taak B: de handwaarde 0,1560 → 0,1559 en de DGU-tabel op 4 decimalen.

## Lezersronde 2

**Kern omgedraaid (coördinator).** De kern is nu de efficiënte rand met de twee-fondsenstelling. De eerste-ordevoorwaarde is de stap ernaartoe. Aangepast: de routekaart, de openingsbewering van de subsectie en de zin na eq-markowitz-foc ("de stap naar de rand"). Ook aangepast: de schakelzin vóór $A, B, C, D$ en Samengevat (eerst de kern met thm-markowitz-tweefonds, dan de weg ernaartoe). De labels zijn ongewijzigd.

**Gekozen namen (H7); de alias staat één keer tussen haakjes**
- *tangentportefeuille* (raakpunt): alle andere "raakpunt" vervangen.
- *mean-variance-portefeuille* (de tangentportefeuille uit geschatte momenten): vervangt "geschatte optimale" en "voorgeschreven portefeuille".
- *minimum-variantieportefeuille*: de alias "veiligste portefeuille" is geschrapt.
- *idiosyncratisch risico* (eigen risico): de alias staat in de Intuïtie.
- *1/N* (gelijkgewogen portefeuille).
- *Sharpe-ratio* (verhouding tussen premie en risico): vervangt "hoogste opbrengst per eenheid risico" en "meer premie per eenheid risico".
- *netto* rendement (enkelvoudig).
- *schattingsfout*: vervangt "invoerfouten".
- *efficiënte rand* / *rand* (efficient frontier).
- *verschil* in plaats van "spreiding" waar geen diversificatie bedoeld is.
- Separatiestelling uitgelegd als "de twee-fondsenstelling met één risicovrij fonds". Indexfondsen hangen nu expliciet aan dat ene fonds (ook spoor 2).

**Per H-regel (opgelost / afgewezen)**
- H1 3/0. Twee fondsen en Tobin zijn nu een handeling zonder matrixrichting of meetkunde. De kernbewering bevat alleen nog wat de waarom-alinea uitlegt.
- H2 5/0. Uitgelegd: waarom tweede momenten goed meetbaar zijn, welke les uit 00_00 bedoeld is, de betekenis van $m$ (≈ $1/R^f$) en van de HJ-grens, Santa-Clara (met ref naar 00_00) en het kritieke-lijn-algoritme.
- H3 1/0. De stelling bevat nu de formule plus één zin in woorden. Stap 2 van het bewijs is herschreven en de kapotte zin gerepareerd. De inhoud waar het CAPM op leunt, blijft staan.
- H4 3/1. Toegevoegd: $D$ tegenover $AC = 65{,}5$, $2\lambda$ als de kosten van rendement in variantie (0,0074 per procentpunt), en $S_{\max}$ 0,529 tegenover de markt (≈ 0,4). Afgewezen: of een risicotolerantie van 50 voorzichtig of agressief is. De lecture heeft geen bron om dat te kwalificeren.
- H5 2/0. Bij de tangentportefeuille staat nu aanname 4. De ε-splitsing is benoemd als definitie (projectie), niet als aanname.
- H6 3/0. Uitgelegd: waarom een hogere $R^f$ de tangentportefeuille riskanter maakt, waarom de bias groeit met $N$ (meer kansen op toevallig hoge gemiddelden), en wat er gebeurt als één $\mu_i$ stijgt.
- H7 8/1. Zie de namenlijst. Afgewezen: de legenda "tangent" en de tabelnamen "ware optimale portefeuille"/"ware optimum" in de uitvoer, omdat de uitvoer identiek moet blijven. In de tekst staat het ware optimum gedefinieerd.
- H8 3/0. "Dat" bij indexfondsen verwijst nu naar het ene fonds. "Het" is vervangen door "die rangorde". "Kern van het argument" staat nog maar één keer (bijschrift DGU).
- H9 1/0. De 2%-subsectie opent met haar bewering.
- H10 5/0. Voorbeelden toegevoegd: $\Sigma^{-1}\mu = (1{,}94; 1{,}13; 4)'$; de inefficiënte tak (3% bij 11,4%); $m$ en HJ; de kritieke lijn; het factormodel (marktbèta) en resampling.
- H11 0/1. Afgewezen: een toy-getal in de simulatiekalibratie zou de uitvoer veranderen.
- Spoor 1: de zin "eigen variantie speelt geen rol" was onjuist (de rij bevat $w_i\sigma_i^2$). Die zin is gecorrigeerd.

**Navertel-afwijkingen**
- *Het kernresultaat*: de lezer twijfelde tussen de rand, de eerste-ordevoorwaarde en de twee fondsen. Nu is de kern expliciet de rand met de twee-fondsenstelling, en de voorwaarde de weg ernaartoe (zie boven).
- *Wat er brak*: de lezer begreep niet waarom Chicago/Yale hier staan en kon de Santa-Clara-zin niet terugkoppelen. Bedoeld was: waarom 1/N wint, is een vraag of prijzen juist zijn, en de replicatie toont dat een weddenschap op geschatte gemiddelden verliest. De alinea opent nu met die vraag. De Santa-Clara-zin is herschreven als "wedt erop dat haar geschatte gemiddelden meer weten dan de prijs, en de replicatie laat zien dat die weddenschap verliest", met een ref naar 00_00. De alinea heeft ongeveer 120 woorden.

**Verificatie**
- prose_stats `--check`: words 7274 | sent_mean 14.6 | p90 24 | gt40 0 | para 44 | dash 0 | semicol 14 | stopw 1 ("precies" = exact) | overige 0. Alleen `words` faalt. Dat komt door de uitleg die de lezers vroegen: +339 woorden ten opzichte van ronde 1.
- `--where`: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0.
- nb_outputs: na-C → na-D is leeg. Tegen na-A staan alleen de twee bekende verschillen uit taak B.

## Naar een 9 (na beoordeling 7,7)

**1. Helderheid**

*Gedaan:*
- **Netto of bruto.** Opzet: $\mathbf{R}$ en $R^f$ zijn nu overal netto. Er staat bij dat bruto rendementen $\Sigma$ en $A$ laten staan, maar $B$ en $C$ veranderen. De notatie-note is daarop aangepast.
- **Verwijzingen.** Twee verwijzingen naar `#00-00-setup` wijzen nu naar `#00-01-rendementen`: tweede momenten (met de stelling van Merton) en oefening 3.
- **Santa-Clara** wordt voorgesteld in een bijzin.
- **Taylor.** Het "dus" bij de Taylor-benadering is vervangen door "een derde, algemenere lezing".
- **Bèta-vorm.** Die zin wijst nu vooruit: het CAPM geeft de vorm later een economische betekenis.
- **Replicatieniveau.** De verklaring achteraf ("twintig jaar langer") is geschrapt. Nu staat er eerlijk dat het blok het niveau openliet en dat we geen verklaring hebben.
- **HJ-grens.** $E[m]$ is verbeterd tot $1/(1+R^f)$.

*Niet gedaan:* de Santa-Clara-verwijzing blijft `#00-00-setup`. Zijn terugblik staat daar, niet in 00_01. De coördinator noemde drie verwijzingen; alleen deze wijst terecht naar setup.

**2. Opbouw**

*Gedaan:*
- De HJ-vooruitblik staat nu in een dropdown-note.
- Roy in de Intuïtie is ingekort; Tchebycheff staat alleen nog in de Theorie.

*Niet gedaan:* Samengevat blijft aan het eind van Theorie. Dat volgt uit STYLE §11.6 en de instructie van de coördinator.

**3. Taal**

*Gedaan:*
- **Roy-zin in het Overzicht** gesplitst.
- **Chopra-Ziemba-fragment** herschreven tot twee gewone zinnen.
- **Nederlandse termen**, met de Engelse term één keer tussen haakjes:

  | was | nu |
  |---|---|
  | in-sample / out-of-sample | in / buiten de steekproef |
  | bruto exposure | brutopositie |
  | excess rendement | overrendement |
  | breakeven-venster | omslagvenster |
  | risk parity | risicopariteitsfondsen |
  | safety-first-belegger | veiligheid-eerst-belegger |

- "snapshot" vervangen door "juli 2026".
- Trema's hersteld in de zichtbare uitvoer: "efficiënte rand" in legenda en titel, "10 industrieën" in alle tabellen en figuren.

*Niet gedaan:* labels zonder trema blijven zoals ze zijn.

**4. Toy**

*Gedaan:*
- De accolades in de opzettabel zijn weg ("10,0%").
- De regel voor de 2×2-inverse staat erbij, met twee uitgerekende elementen: 28,125 en −6,25.

**5. Code en figuren**

*Gedaan:*
- **Commentaar bij elke `einsum`:** in de simulatie, de figuur en oefening 2.
- **rf.** De replicatie gebruikt nu `rf_monthly`, zodat de `rf = 0,02` uit de theorie niet meer wordt overschreven.
- **NaN-kolom.** Die is verklaard in code-commentaar en in de tekst: de minimum-variantiegetallen van DGU zijn niet overgenomen.
- **"Wilder".** De uitspraak steunt nu op de standaarddeviaties in de volgende tabel (14,5% tegen 4,3% per maand).

*Niet gedaan:* `tail(3)` blijft staan. Een andere maat zou nieuwe getallen in de uitvoer geven. De tekst noemt de drie rijen nu alleen een controle.

**6. Replicatie**

*Gedaan:*
- Het blok noemt de tegenhangers: S&P-sectoren ↔ 10 industrieën, FF-vierfactor ↔ 25 size/BM.
- De vergelijkingstabel zet elk origineel naast zijn tegenhanger en heeft een nieuwe kolom "gat: in minus buiten". Die toont 0,10 en 0,30 tegen DGU 0,31 en 0,54.
- Het oordeel verwijst naar die kolom.

**7. Oefeningen**

*Gedaan:*
- Oefening 2, les (3): steunt nu op de $N/T$-bias bij vaste $T$ (0,294 → 0,149). De onjuiste bewering "vijf keer zoveel data" is eruit.
- Oefening 2, (2): de robuustheidsclaim is afgezwakt.
- Oefening 3: verwijzing hersteld.

**Eigen leesronde:** twee kleine formuleringen verbeterd ("het inzicht dat", "werkt die grens uit").

**Verificatie**
- prose_stats `--check`: words 7510 | sent_mean 14.7 | p90 24 | gt40 0 | para 45 | dash 0 | semicol 13 | stopw 1 | overige 0. Alleen `words` faalt; daarvoor geldt geen grens meer. `--where`: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0.
- nb_outputs tegen na-A: alle getallen gelijk. Er zijn alleen bedoelde verschillen:
  - kolom- en indexnamen (trema's, Nederlandse termen);
  - de vergelijkingstabel is anders geordend en heeft de gat-kolom;
  - de drie figuren zijn van grootte veranderd (tekst in legenda, titel en as);
  - de broncoderegel van cel 10 (`rf_monthly`);
  - de twee bekende verschillen uit taak B.
