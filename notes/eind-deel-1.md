STATUS deel-1 F6c naadpunten=10 open=0

# Naadcontrole Deel I (F6)

Gelezen: `00_01_rendementen`, `01_02_bachelier`, `01_03_williams_ddm`,
`01_04_markowitz` volledig; van `00_00_setup` het Overzicht, de rode draad (drie
motieven) en de Notatie; van `02_05_crsp_tape` "Waar we zijn" en "Wat er brak".
Eén kalibratie voor het hele deel: 8,4 / 8,3 / 8,3 / 8,4, laagste deelcijfer
overal 8.

## Zware naadpunten (een lezer die beide plekken leest, krijgt tegenstrijdige informatie)

1. **Kleine letters: niveaus of logs.**
   - `00_00_setup`, Notatie: "Zonder aankondiging zijn alle grootheden niveaus, en
     is $r$ het netto simpele rendement. Een logrendement krijgt een eigen symbool,
     bijvoorbeeld $\ell = \log R$."
   - `00_01_rendementen`, Theorie, "Opzet: twee soorten rendement": "De notatie van
     [](#00-00-setup) reserveert kleine letters voor log-grootheden."
   - De bewering in L1 over de setup is onjuist. (L2 zegt correct "Vanaf hier zijn
     kleine letters logs" en volgt daarmee de aankondigingsregel.)

2. **Prijs en dividend: $p_t, d_t$ of $P_t, D_{t+1}$.**
   - `00_00_setup`, Notatie: "$p_t$ | prijs op tijdstip $t$", "$d_t$, $c_t$ |
     dividend, consumptie".
   - `00_01_rendementen`, Theorie, "Opzet": "Laat $P_t$ de prijs zijn en $D_{t+1}$
     het dividend", zonder aankondiging van de afwijking.
   - `01_03_williams_ddm`, Theorie, "Opzet en aannames": $p_t$ en $d_t$ als bedragen,
     zoals de setup. L1 en L3 schrijven dus hetzelfde object verschillend. (L2
     gebruikt $P_t$ voor het niveau en $p_t = \log P_t$, maar kondigt dat aan.)

3. **$R$ bruto of netto.**
   - `00_00_setup`, Notatie: "$R_{t+1}$ | bruto rendement, $R = 1 + r$".
   - `00_01_rendementen` [](#eq-rendementen-simpel) en `01_03_williams_ddm`
     [](#eq-williams-ddm-rendement): $R$ bruto.
   - `01_04_markowitz`, Theorie, "Opzet en aannames": "$N$ risicovolle activa met
     netto rendementen $\mathbf{R}_{t+1}$ (10% is 0,10, terwijl $R$ in
     [](#00-01-rendementen) bruto was)". L4 noemt het verschil met L1, niet dat het
     van de reeksafspraak afwijkt; L3 volgt die afspraak wel.

4. **$R^f$ bruto in "andere lectures".**
   - `00_00_setup`, Notatie: "de risicovrije rente $R^f$ is netto (0,02 bij 2%)", voor
     de hele reeks.
   - `01_04_markowitz`, Theorie, "Opzet en aannames": "andere lectures schrijven
     $R^{f}$ soms bruto (1,02)." Geen lecture in dit deel doet dat, en de setup
     verbiedt het.

5. **De omvang van de equity premium.**
   - `00_00_setup`, rode draad, "De standaardfout van 2%": "de gemeten premie op
     aandelen, ongeveer 8% per jaar, ... {cite}`MehraPrescott1985`".
   - `00_01_rendementen`, Intuïtie: "de *equity premium* ... ongeveer 6%:
     {cite:t}`MehraPrescott1985` vonden 6,18% over 1889–1978"; ook Theorie, "Het
     kernresultaat": "Rond een geschatte premie van 6%".
   - Zelfde bron, twee getallen. Mehra en Prescott rapporteren 6,18%.

## Lichte naadpunten (notatie of nuance)

6. **$T$: jaren of waarnemingen.**
   - `00_01_rendementen`, {prf:ref}`thm-rendementen-merton`: "$T$ jaar op $n$
     tijdstippen per jaar, dus met $N = nT$ waarnemingen".
   - `01_02_bachelier`, "Opzet en aannames": "$T$ het aantal waarnemingen".
   - `01_04_markowitz`, "Waar het strandt": "Met $T$ jaren data" (punt 1) en "Bij
     tien activa en 120 maanden is $N/T = 0{,}083$" (punt 3); de simulatie rekent met
     "$T$ (maanden)". Bovendien is $N$ in L1 het aantal waarnemingen en in L4 het
     aantal activa.

7. **$\kappa$.**
   - `00_01_rendementen`, "Dikke staarten": $\kappa$ is de kurtosis.
   - `01_02_bachelier`, bewijs van {prf:ref}`thm-bachelier-reflectie`: "Zij
     $\kappa = \min\{k : S_k = a\}$ het eerste raaktijdstip."

8. **$\lambda$.**
   - `00_00_setup`, Notatie: "$\lambda_f$ | prijs van risico van factor $f$".
   - `01_04_markowitz`, "Het kernresultaat": "$\lambda$ de schaduwprijs van de
     rendementseis" (Lagrange-multiplicator), zonder vermelding van de afwijking.

9. **Theorie of feit: welk model werd als eerste getoetst.**
   - `00_00_setup`, rode draad, "Theorie of feit": "Het vak begon met één model dat
     werd getoetst, het CAPM."
   - `01_03_williams_ddm`, Wat er brak: "Williams leverde ... een model met een
     constante $r$ dat toetsbaar is en verworpen." Ook L2 toetst de random walk.
     Geen harde tegenspraak (de setup vat samen), maar een lezer die de status per
     model bijhoudt, ziet twee getoetste modellen vóór het CAPM.

10. **Hoeveel $r$ van de beweging verklaart.**
    - `01_03_williams_ddm`, replicatie: rendement 0,38, dividend 0,15, latere ratio
      0,47 van één log-punt; $R^2$ 12% tegen 5%. Wat er brak: "verklaart het grootste
      deel van de beweging".
    - `01_04_markowitz`, Waar we zijn: "De replicatie daar liet zien dat prijzen
      vooral bewegen doordat $r$ beweegt."
    - L4 herhaalt de te sterke formulering uit L3; ten opzichte van de dividenden
      klopt "vooral", ten opzichte van het geheel niet (zie feitelijke fout 1 in
      `notes/eind-01_03_williams_ddm.md`).

## Gecontroleerd en consistent

- 11,6% met standaardfout 1,8 pp: setup-Overzicht, L1 "Waar we zijn" en "Wat er
  brak".
- 9,0% van Fisher en Lorie, standaardfout 3,9 pp over 1926–1960: L1 en
  `02_05_crsp_tape` "Waar we zijn" ("bijna vier procentpunt", "35 jaar" voor 34,5).
- Regnault 1863, "37 jaar vóór Bachelier": setup, L1 en L2.
- Cowles en Kendall: L2 en L3 "Waar we zijn" zeggen hetzelfde.
- CRSP-tape in 1964: setup, L1, L4 "Wat er daarna kwam" en `02_05_crsp_tape`.
- De standaardfout van 2% ($20/\sqrt{100}$) wordt in L1, L2, L3 en L4 met dezelfde
  getallen en dezelfde betekenis aangeroepen; de drie motieven dragen overal hun
  vaste naam en de Chicago/Yale-lezing volgt de setup.
- $r$ heeft drie betekenissen in drie lectures (simpel rendement in L1,
  logrendement in L2, constante discontovoet in L3), maar L2 en L3 kondigen de
  wissel aan zoals de setup voorschrijft. Geen tegenspraak.


## Controle (F6c)

Gecontroleerd in de lectures, met de setup zoals die nu is als maatstaf.

| nr | naadpunt | status | vindplaats |
|---|---|---|---|
| 1 | kleine letters: niveaus of logs | opgelost | L1 Opzet: "Zoals in [](#00-00-setup) is $r$ het netto simpele rendement" |
| 2 | $p_t, d_t$ tegen $P_t, D_{t+1}$ | opgelost | L1 schrijft $p_t$, $d_{t+1}$ als niveaus; L3 idem; L2 kondigt logs aan |
| 3 | $R$ bruto of netto | opgelost | L4 Opzet: rendementen heten $r$ (netto), $R = 1 + r$ bruto, volgens de setup |
| 4 | $R^f$ bruto in "andere lectures" | opgelost | bijzin in L4 geschrapt |
| 5 | omvang van de equity premium | opgelost | L1 Intuïtie: 6% als kalibratie, Mehra-Prescott 6,18%, setup 8,3% op French-data sinds 1926. Buiten dit deel: de setup (rode draad) koppelt "ongeveer 8%" nog aan {cite}`MehraPrescott1985`, dat 6,18% rapporteert |
| 6 | $T$ en $N$ | opgelost | L1: $T$ jaren, $N$ waarnemingen; L2 noemt de wissel; L4: $T$ waarnemingen, $N$ activa, beide in de Opzet gedefinieerd |
| 7 | $\kappa$ | opgelost | $\kappa$ is uit L2 verdwenen |
| 8 | $\lambda$ | opgelost | L4: "deze $\lambda$ is een Lagrange-multiplicator, niet de prijs van risico" |
| 9 | eerste getoetste model | opgelost | L3: "Zo getoetst en verworpen werd het pas decennia later, na het CAPM" |
| 10 | hoeveel $r$ verklaart | opgelost | L3: "ruim twee keer zoveel ... als de dividendgroei"; L4 Waar we zijn: "meer van de prijsbeweging ... dan de dividenden" |

Open naadpunten: 0. Eén aanwijzing voor de setup-lecture (buiten dit deel): de
premie van ongeveer 8% bij de Mehra-Prescott-citatie in "De standaardfout van 2%".
