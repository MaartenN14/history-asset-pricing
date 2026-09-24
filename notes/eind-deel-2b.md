# Naadpunten Deel II, eindbeoordelaar B (F6): L6, L8, L9

Gelezen: [](#02-06-efficiente-markten), [](#02-08-capm), [](#02-09-black-scholes)
volledig; van de buren alleen "Waar we zijn" en "Wat er brak"
([](#02-05-crsp-tape), [](#02-07-event-studies), [](#03-10-merton-icapm)); de
setup-sectie Notatie; in [](#01-04-markowitz) de labels en de notatie die L8
aanhaalt.

Kalibratie: dezelfde als in `eind-02_06_efficiente_markten.md`,
`eind-02_08_capm.md` en `eind-02_09_black_scholes.md`, geijkt op
`eind-00_01_rendementen.md` en `eind-01_03_williams_ddm.md`. Een onaangekondigde
afwijking van de setup-notatie kost bij helderheid een half punt; een onjuiste
bewering over de notatie van een andere lecture is een feitelijke fout.

## In orde

- **L8 naar L4.** Alle aangehaalde labels bestaan en zeggen wat L8 ervan zegt:
  `cor-markowitz-separatie` (separatie van Tobin), `eq-markowitz-tangent`
  (tangentportefeuille en $S_{\max}^2$, gebruikt in het GRS-bewijs),
  `thm-markowitz-tweefonds`, `eq-markowitz-foc` ($\mathbf{w} =
  \boldsymbol{\Sigma}^{-1}(\lambda\boldsymbol{\mu} + \delta\mathbf{1})$) en
  `ex-markowitz-1` (zero-beta-rendement exact 2%). Het toy van L8 neemt de
  covariantiematrix en de rendementen 10%, 14%, 4% met $R^f = 2\%$ correct over.
- **L9 naar de setup.** L9, Opzet en aannames: "We wijken op drie punten af van de
  notatietabel van de reeks. De aandelenkoers heet $S_t$ ... In de boom was $R^{f}$
  het bruto rendement per stap (1,02), niet de netto rente. En $r$ is hier de continu
  samengestelde rente". De vereiste melding staat er.
- **Motief "de standaardfout van 2%"**: L6 (Simulatie), L8 (Simulatie) en L9
  (Simulatie) gebruiken dezelfde lezing (20% volatiliteit, een eeuw, 2 pp).
- **Jensen (1968)**: L6 (Jensen-replicatie, tabel "origineel") en L8 (Theorie, "Hoe
  het getoetst wordt") geven beide 115 fondsen en $-1{,}1\%$ per jaar.
- **Overdrachten**: L5 "Wat er daarna kwam" → L6 "Wat we al weten" (het ontbrekende
  economische argument); L6 → L7 (FFJR 1969); L7 "Wat er daarna kwam" → L8 "Wat we
  al weten" (marktmodel zonder economische inhoud); L8 → L9 (CAPM-afleiding van
  Black en Scholes, bevestigd in de note van L9).

## Naadpunten

1. **$R^f$ bruto in L6, onaangekondigd.**
   L6, Toy-voorbeeld: "De rente is nul, $R^f = 1$"; Theorie,
   [](#eq-efficiente-markten-pricing): "$\frac{1}{R^{f}_{t+1}} = \E_t[m_{t+1}]$";
   [](#eq-efficiente-markten-premie): "$\E_t[R_{t+1}] - R^{f}_{t+1}$".
   Setup, Notatie: "$R^{f}_{t+1}$ | risicovrije rente, netto (2% is 0,02)" en "de
   risicovrije rente $R^f$ is netto (0,02 bij 2%)". Daarmee spreekt L6 ook L8
   ("De risicovrije rente is $R^{f} = 2\%$", netto) tegen, en L9 meldt als afwijking
   wat L6 al stilzwijgend deed.

2. **$r$ als logrendement in L6.**
   L6, Opzet, definitie 3: "Log-rendementen volgen een **random walk** als de
   $r_{t+1}$ onafhankelijk en identiek verdeeld zijn"; propositie "Van sterk naar
   zwak" (i): "Is $r_{t+1}$ i.i.d. met verwachting $\mu$".
   Setup, Notatie: "$r_{t+1}$ | netto simpel rendement" en "Een logrendement krijgt
   een eigen symbool, bijvoorbeeld $\ell = \log R$".

3. **$R$ netto in L8, met een onjuiste reden.**
   L8, Opzet en aannames: "Er zijn $N$ risicovolle activa met netto rendementen
   $\mathbf{R}$ ... Zoals in [](#01-04-markowitz) zijn rendementen netto, anders dan
   de bruto conventie van [](#00-01-rendementen)."
   L4, Opzet en aannames: "$r$ is netto (10% is 0,10), $R = 1 + r$ bruto, en de
   risicovrije rente $R^{f}$ netto". L1, Opzet: "Zoals in [](#00-00-setup) is $r$
   het netto simpele rendement", met de tabelkolom "bruto rendement $R = 1 + r$".
   Setup, Notatie: "$R_{t+1}$ | bruto rendement, $R = 1 + r$". L4 en L1 hebben dus
   dezelfde conventie; L8 wijkt af en beschrijft beide verkeerd. Ook L8, toy:
   "Rendementen zijn netto, zoals in [](#01-04-markowitz)".

4. **$m$ voor de markt tegen $m$ voor de SDF; $M$ tegen $m$.**
   L8, Theorie, [](#eq-capm-sml): "$\beta_{i,m} = \Cov(R_i, R_m)/\Var(R_m)$"; L9,
   note: "$\beta_{C,m} = (SC_S/C)\,\beta_{S,m}$, met $m$ de markt".
   Setup, Notatie: "$m_{t+1}$ | stochastic discount factor" en "$\beta_{i,f}$ | bèta
   van activum $i$ op factor $f$". L6 gebruikt $m$ door de hele theorie voor de SDF
   en schrijft de markt in de Jensen-replicatie als "$\beta_{j,M} R^{e}_{M,t+1}$".
   Twee opeenvolgende lectures noemen de markt dus $M$ en $m$, en de tweede
   hergebruikt de SDF-letter zonder melding.

5. **"alpha" tegen "alfa".**
   L6, Jensen-replicatie en Wat er brak: "de fondsalpha's van Jensen", "Een
   positieve alpha", "Geen alpha". L8, Theorie: "*Jensens alfa* $\alpha_i$", en in
   de replicatie "alfa (% p.m.)". Eén begrip, twee spellingen.

6. **Het CAPM en Jensens alfa twee keer ingevoerd.**
   L6, Jensen-replicatie: "De regressie is het CAPM: het verwachte excess rendement
   van een fonds is evenredig met zijn bèta op de markt. De alpha meet dan wat een
   beheerder daarboven verdient".
   L8, Overzicht: "Het *Capital Asset Pricing Model* is de eerste evenwichtstheorie
   van verwachte rendementen in deze reeks"; Theorie: "*Jensens alfa* $\alpha_i$ is
   de verticale afstand tot de SML ... Jensen paste de toets toe op 115
   beleggingsfondsen", zonder terugverwijzing naar de replicatie in L6. Geen
   feitelijke tegenspraak, wel een model dat vóór zijn eigen lecture wordt gebruikt
   en daarna als nieuw wordt gepresenteerd.

7. **De risiconeutrale maat twee keer ingevoerd.**
   L6, Toy, Vooruitblik: "de theorie noemt die gewichten de *risiconeutrale
   kansen*"; Theorie, stelling "Martingaal na weging met de SDF": "onder de maat $Q$
   ... geldt $\E^{Q}_t[(p_{t+1} + d_{t+1})/R^{f}_{t+1}] = p_t$", met Harrison en
   Kreps.
   L9, Wat het voorspelt: "Die wereld heet de *risiconeutrale kansmaat*
   $\mathbb{Q}$", en "Wat we al weten": Bachelier kon niet zeggen "waarom een
   verwachting zonder correctie voor risico de prijs is". Geen terugverwijzing naar
   L6; ook de schrijfwijze verschilt ($Q$ tegen $\mathbb{Q}$).

8. **$d$ als daalfactor in L9.**
   L9, Toy: "stijgfactor $u$ / daalfactor $d$"; Opzet noemt drie afwijkingen, deze
   niet. Setup, Notatie: "$d_t$, $c_t$ | dividend, consumptie". L9 gebruikt voor het
   dividend daarna $\delta$ (put-call-pariteit), zodat het dividend in deze lecture
   een andere letter heeft dan in L6 ($d_{t+1}$).

9. **$\lambda$ drie keer anders.**
   L6, "Hoe het getoetst wordt": "Een fractie $\lambda$ van de beleggers" (Grossman
   en Stiglitz). L8, bewijs zero-beta stap 2: "$\lambda_m$ en $\delta_m$ de
   schaduwprijzen", zonder de waarschuwing die L4 wel geeft ("deze $\lambda$ is een
   Lagrange-multiplicator, niet de prijs van risico $\lambda_f$"). Setup, Notatie:
   "$\lambda_f$ | prijs van risico van factor $f$".

10. **Marktvolatiliteit: 20% per jaar tegen 4,5% per maand.**
    L8, Theorie: "met een marktvolatiliteit van ongeveer 20% en een premie van
    ongeveer 6% per jaar, is $\theta_m \approx 1{,}5$" en, in dezelfde sectie
    verderop, "Met een marktvolatiliteit van 4,5% per maand en 480 maanden". L6,
    Simulatie, kalibratietabel: $\sigma$ = 4,5% per maand. 4,5% per maand is 15,6%
    per jaar; de standaardfout-van-2%-passages in L6, L8 en L9 rekenen met 20%.
    Twee "echte" waarden voor dezelfde grootheid, zonder toelichting.

11. **Chronologie Merton: L9 "daarna" tegen L10 1969.**
    L9, Wat er daarna kwam: "Merton gebruikte dezelfde wiskunde in continue tijd om
    de portefeuillekeuze van beleggers en het evenwicht van de hele markt opnieuw af
    te leiden". L10, Waar we zijn: "**Jaartal.** 1969–1973", en het Overzicht opent
    met de publicaties van augustus 1969. Mertons portefeuillekeuze in continue tijd
    ging aan Black-Scholes (1973) vooraf; "daarna" en "opnieuw" suggereren het
    omgekeerde.

12. **Begin van het tijdvak in L6 (intern).**
    L6, Waar we zijn: "**Jaartal.** 1965–1970, met uitlopers naar 1978 en 1991."
    L6, Overzicht: "In 1970 bracht Fama beide samen in een overzichtsartikel. Met
    dat artikel begint het tijdvak van deze lecture." Ook als feitelijke fout
    opgenomen in `eind-02_06_efficiente_markten.md`.

## Telling

Twaalf naadpunten. Harde tegenspraak met de setup of L4: 1, 2, 3 en 4. Tegenspraak
tussen de drie lectures onderling: 4, 5, 6, 7 en 10. Met een buur: 11. Intern: 12.
Punt 3 en 12 staan ook als feitelijke fout in de eindbeoordeling van de lecture.

## Controle (F6c)

Gecontroleerd tegen de lectures na F6-1 (L8, L9, daarna L6 na de omzetting naar
"alpha"). De standaard is de setup; boekconventie is "alpha".

| nr | naadpunt | status | vindplaats |
|---|---|---|---|
| 1 | $R^f$ bruto in L6 | opgelost | L6, toy: "Anders dan in [](#00-00-setup) is $R^f$ in deze lecture bruto." |
| 2 | $r$ als log in L6 | opgelost | L6, definitie 3 en propositie: $\ell_{t+1} = \log R_{t+1}$ |
| 3 | $R$ netto in L8 | opgelost | L8, Opzet: netto $\mathbf{r}$, $R^f$ netto, $\mathbf{R}^{e} = \mathbf{r} - R^{f}\mathbf{1}$, "zoals in [](#00-00-setup)"; de bewering over L4 en L1 is weg |
| 4 | $m$ voor de markt | opgelost | L8: "Het subscript $m$ staat hier voor de marktportefeuille, niet voor de SDF"; L9: $\beta_{C,\text{mkt}}$; L6 houdt $M$ |
| 5 | alpha/alfa | opgelost | L6 en L8 overal "alpha", ook in de celuitvoer |
| 6 | CAPM en Jensen twee keer ingevoerd | deels | L8 verwijst terug naar L6, maar met een onjuiste bewering: "Jensen, wiens fondsen [](#02-06-efficiente-markten) al gebruikte". L6 gebruikte Jensens regressie op zeven hedendaagse fondsen, niet zijn fondsen. Staat als nieuwe fout in `eind-02_08_capm.md` |
| 7 | risiconeutrale maat twee keer | opgelost | L9: "Het is de maat $Q$ uit [](#thm-efficiente-markten-martingaal)" |
| 8 | $d$ als daalfactor in L9 | opgelost | L9, Opzet: "Ook $d$ is in de boom de daalfactor, niet het dividend; een dividend heet hier $\delta$" |
| 9 | $\lambda$ | opgelost | L6: $\omega$ bij Grossman-Stiglitz; L8: schaduwprijzen "(niet de prijs van risico)" |
| 10 | 20% tegen 4,5% per maand | opgelost | L8 rekent $\theta_m$ nu met de kalibratie van de simulatie (4,5% per maand, 15,6% per jaar); 20% staat alleen nog in de lezing van het motief uit L1 |
| 11 | Merton-chronologie | opgelost | L9: "al vanaf 1969 gebruikt ... In 1973 leidde hij er het evenwicht van de hele markt mee af", in lijn met L10 |
| 12 | tijdvak L6 | opgelost | L6: "Dat artikel sluit het tijdvak af dat in 1965 begon" |

Open: één naadpunt, deels (6). Geen nieuwe naadpunten.
