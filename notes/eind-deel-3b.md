STATUS deel-3b naad open=0

# Naadcontrole Deel III, groep b (L14 t/m L17)

Gelezen: `03_14_roll`, `03_15_shiller_excess_volatility`, `03_16_vroege_anomalieen`, `03_17_termijnstructuur_real_options` volledig (.md). Van `03_13_equity_premium_puzzle` en `04_18_fama_french` alleen "Waar we zijn", het slot en de aangehaalde plekken; daarnaast gerichte greps in `00_01`, `01_03`, `02_08`, `03_11`, `04_20`, `04_23`, `05_28` en `06_34` om beweringen over die colleges te controleren. De naden 7 t/m 11 van 3a (symbolen $\phi$, $\eta$, $q$, $\delta$, $\pi$) blijven projectkeuzes en worden hier niet opnieuw gemeld.

## Naadpunten

### Inhoud en verwijzingen

1. **Verwijzing naar een oefening als linkdoel.**
   - Plek: `03_14_roll.md:480`, eind van "Bijna-efficiënte proxy's": de $\rho^{*} = 0{,}785$ van het toy-voorbeeld verwijst met een cross-ref naar het label `ex-roll-1`.
   - Wat: kaart §3 zegt dat oefeningslabels geen linkdoel zijn; verwijzingen naar oefeningen zijn tekst.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: vervang de cross-ref door de tekst "(eerste oefening)".

2. **L17 noemt de risiconeutrale kans $q$ "zoals in" L11, maar L11 noemt die kans $\pi^{*}$.**
   - Plek: `03_17_termijnstructuur_real_options.md:1384` (uitwerking oefening 4); doelplek `03_11_apt_no_arbitrage.md:422` ($\pi^{*} = (1 + R^{f} - d)/(u - d)$) en `:1179` ($q_u$, $q_d$ zijn daar toestandsprijzen).
   - Wat: de formule klopt, maar de letter niet. Een lezer die L11 openslaat, vindt onder $q$ een toestandsprijs en niet een kans.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: schrijf in L17 "de risiconeutrale kans $q$, in [](#03-11-apt-no-arbitrage) $\pi^{*}$", of gebruik in oefening 4 zelf $\pi^{*}$.

3. **De equity premium van L15 heet "die uit L13", maar het getal is een ander dan het kopgetal van L13.**
   - Plek: `03_15_shiller_excess_volatility.md:907-909`: premie $0{,}0860 - 0{,}0168 = 0{,}069$, "de reële equity premium uit" L13; doelplek `03_13_equity_premium_puzzle.md:40,855,858` (6,18 over 1889–1978, 6,92% tot 2024).
   - Wat: L15 meet over 1871–2025, als reëel rendement min reële korte rente. Dat ligt dicht bij de 6,92% van L13, maar de lezer kent uit L13 vooral 6,18.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: schrijf "vrijwel de 6,92% die [](#03-13-equity-premium-puzzle) tot 2024 vond (6,18 bij Mehra en Prescott over 1889–1978)".

### Notatie en vaste termen (kaart §3)

4. **Het subscript $m$ voor de markt wordt in L16 niet aangekondigd, en in L17 is $m$ de SDF.**
   - Plek: `03_16_vroege_anomalieen.md:133,274,573` ($\beta_{i,m}$, $R^{e}_{m,t+1}$, $f_m$) zonder zin over $m$. `03_17_termijnstructuur_real_options.md:222` gebruikt $m_T/m_t$ als stochastische discontofactor. `03_14_roll.md:260-261` heeft de vereiste zin wel.
   - Wat: kaart §3 vraagt voor de markt een ander symbool of een zin dat het subscript $m$ hier de markt is. Twee opeenvolgende colleges gebruiken $m$ zonder die zin in twee betekenissen.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: voeg in L16, "Opzet: sorteren als regressie zonder vorm", de zin van L14 toe: "Het subscript $m$ staat in deze lecture voor de marktportefeuille, niet voor de SDF."

5. **"Stochastic discount factor" in het Engels, waar L11–L13 de vaste Nederlandse naam gebruiken.**
   - Plek: `03_17_termijnstructuur_real_options.md:227` (definitie van $m$) en `:1192` ("Risico of vergissing?").
   - Wat: na naad 2 van 3a heet $m$ in L11–L13 de "stochastische discontofactor" (in L13 25 keer). In L17 staat alleen de Engelse term, en dat is ook de eerste keer dat L17 het begrip noemt.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: schrijf op beide plekken "stochastische discontofactor (SDF)", met het Engels hoogstens één keer tussen haakjes.

6. **"Discontofactor" zonder bijvoeglijk naamwoord voor $\delta = 1/(1+r)$.**
   - Plek: `03_15_shiller_excess_volatility.md:230-231`: "$\delta = 1/(1+r)$ is de discontofactor".
   - Wat: na naad 2 van 3a is "discontofactor" in de reeks altijd "stochastische" ($m$) of "subjectieve" ($\beta$). In L15 is $\delta$ een derde grootheid, een vaste disconteringsfactor bij een constante discontovoet.
   - Oordeel: opgelost (orchestrator, 2026-09-28, volgens voorstel).
   - Voorstel: schrijf "de constante discontofactor", zodat de naam niet samenvalt met $m$ of $\beta$.

### Blijft, projectkeuze of buiten 3b

7. **Letters die per college een andere rol hebben.** $\delta$: Lagrange-multiplicator (L14:138), discontofactor (L15:231), blootstelling aan $h$ (L16:569), convenience yield (L17:604). $\kappa$: schaal van de premies (L14:403), constante van Campbell-Shiller (L15:507), snelheid van terugtrekken (L17:196). $\rho$: correlatie $\rho^{*}$ (L14:444), loglinearisatiegewicht (L15:506), correlatie kenmerk-fout (L16:484). $\lambda$: Lagrange (L14:138), marktprijs van risico (L17:262). $\eta$: FM-residu (L16:320), elasticiteit (L17:649). Elk wordt lokaal gedefinieerd, en L15:233 en L17:196,606 verklaren hun afwijking van de bron. Oordeel: blijft, projectkeuze (zoals 3a naden 7–11).

8. **Log-notatie tussen L15 en L20.** L15:501-503 schrijft $pd_t$ en $\ell_{t+1}$ voor het logrendement (volgens kaart §3). `04_20_voorspelbaarheid.md:128-137` schrijft $dp_t$ en $r_{t+1}$ voor het logrendement, en leidt de Campbell-Shiller-benadering opnieuw af (`eq-voorspelbaarheid-cs-pv`), terwijl L15 die al heeft (`eq-shiller-excess-volatility-cs`). De belofte in L15:549 ("in L20 wordt deze decompositie geschat") klopt wel (`04_20:309-344` verwijst terug naar L15). Oordeel: blijft, buiten 3b. Voorstel voor de herziening van L20: $\ell$ voor het logrendement, het teken van $pd$ en $dp$ één keer uitleggen, en naar de afleiding in L15 verwijzen in plaats van haar te herhalen.

## Geen tegenspraak gevonden

- Labels: alle 25 externe cross-refs en `prf:ref`'s in L14–L17 bestaan (00-00, 00-01, 01-03, 01-04 ×3, 02-06, 02-07, 02-08 ×3, 02-09 ×3, 03-11 ×2, 03-13, 04-18, 04-20, 04-23, 05-28, 06-34).
- Estafette in "Wat er daarna kwam" en "Waar we zijn": L13:1095-1097 → L14:26-29 (Roll, en de voorafschaduwing in de APT-discussie uit 3a naad 6); L14:1122-1124 → L15:26-28; L15:1081-1084 → L16:25-27; L16:979-982 → L17:26-27; L17:1197-1200 → `04_18:24-28`. Alle beweringen over de buurcolleges kloppen met de doelplek.
- Grens met 04_18: "twee overhouden" (L16:979-980) past bij `04_18:83-90` (marktwaarde en B/M), Berk (L16:417) bij `04_18:94`, en Rolls tautologie (L14:221-224) bij `04_18:815`. De blijvende richting van small en value (L14:1284-1285) is het feit waarmee `04_18` opent.
- Terugverwijzingen: attenuatie van geschatte bèta's (L14:749) staat in `02_08:579-645`; FM-helling als portefeuille met bèta één en kosten nul (L16:310) in `02_08:554`; de prijs-dividend-ratio voorspelt het rendement en niet de dividendgroei (L15:1046) in `01_03:843`; Itô, de PDE en Feynman-Kac (L17:244,298,300) in L9; de martingaalstelling (L17:215) in L11.
- Vooruitverwijzingen: De Bondt en Thaler (L16:95) in `04_23:49-51`; datamining als systematisch argument (L16:532) in `06_34:27,111`; term premium (L17:1198) in `05_28:24,235`.
- De standaardfout van 2%: overal gekoppeld aan `00-01-rendementen` en met dezelfde strekking (L14:630-633, L15:395-398 en 1034-1039, L16:301 en 660, L17:801-804 en 890). L14, L16 (Barra, L16:385) en L17 gebruiken hem ook "omgekeerd" (tweede momenten zijn goed gemeten), en dat doen ze consistent.
- Het CAPM-feit: "te vlak" (L14:25) en "te vlak, maar wel positief" (L16:24) spreken elkaar niet tegen.
- Simulatiewerelden: L14 (premie 0,66% en volatiliteit 4,69% per maand) en L16 (0,5% en 4,5%) zijn apart gedefinieerd en worden niet aan elkaar gelijkgesteld.
- Termen: "size/BM" is de naam van de 25 portefeuilles (L14, `04_18`) en "B/M" het kenmerk (L16, `04_18`). Dat is consistent.
- Toy-voorbeelden: L14 hergebruikt de drie activa van L4 en herhaalt alleen de scalars, niet de afleiding. Geen toy wordt in twee colleges volledig uitgelegd.
- Opmerking binnen L15 (geen naad): L15:1015 zegt "0,55 tot 9,8" over de hele gevoeligheidstabel, L15:1061 zegt "tussen 0,55 en 9,3 over 1871–2025". Dat is verenigbaar als 9,8 de rij 1928–1979 is. Nagaan bij de feitencontrole van L15.
