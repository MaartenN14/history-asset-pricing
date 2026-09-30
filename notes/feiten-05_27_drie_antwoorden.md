STATUS 05_27_drie_antwoorden F4T open=4 punten=15

# Feitencontrole 05_27_drie_antwoorden (F23)

`nb_numbers.py`: 53 getallen zonder celuitvoer, allemaal handberekeningen (toy, EZ-toy,
instap) of brongetallen met citatie. Alle 53 hieronder per sectie samengevat (rijen
17–25); geen ervan is fout. `nb_outputs.py`: 18 cellen, geen fout, geen crash.

## A. Naadpunt R^f: bruto/netto (van de orchestrator)

`plannen/kaart-rollen.md` §3: "$R^f$ de netto risicovrije rente". Bevestigd in
`lectures/00_00_setup.md` r.202-203: "een rendement $R$ is bruto (1,08 bij 8%), terwijl de
risicovrije rente $R^f$ netto is (0,02 bij 2%). Het bruto risicovrije rendement is dus
$1 + R^f$." En in `lectures/03_12_consumptie_capm.md` r.155 ($1+R^f_i=1/\E_i[m]$), r.275
($1+R^f_{t+1}=1/\E_t[m_{t+1}]$), r.406-407 ($\log(1+R^f)=...$) en r.419
($1/(1+R^f)=\beta\E[(g^c)^{-\gamma}]$). Dit college gebruikt op meerdere plekken $R^f$ zelf
als bruto grootheid, in strijd met die conventie. De getallen zelf kloppen (zie B);
alleen het label/de definitie moet veranderen.

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | r.130 | "het bruto risicovrije rendement is $R^f = 1/\E[m]$" | opgelost F4 (was onjuist) | kaart-rollen §3; setup r.202-203; 03_12 r.155,275 | "$1 + R^f = 1/\E[m]$" (R^f netto) |
| 2 | r.136 | "Bij $p=0$ is $R^f = 1/m_n = 1{,}1380$, een rente van 13,8%" | opgelost F4 (was onjuist) | idem | "$1 + R^f = 1/m_n = 1{,}1380$"; de rente 13,8% zelf is al correct (= R^f netto) |
| 3 | r.141 | "dus $R^f = 1{,}00901$ en een rente van 0,9%" | opgelost F4 (was onjuist) | idem | "$1 + R^f = 1{,}00901$"; rente 0,9% blijft staan |
| 4 | r.166, r.169 | dict-sleutel `"R^f"` met brutowaarde (resp. `rf`, 1,00901) in de toy-tabel | opgelost F4 (was onjuist) | idem; vergelijk r.811 waar `E[R^f]` wél netto is | sleutel hernoemen naar `"1+R^f"`; getallen ongewijzigd |
| 5 | r.206 | "$r^f = \log R^f$, met $R^f$ het bruto risicovrije rendement" | opgelost F4 (was onjuist) | idem | "$r^f = \log(1+R^f)$, met $R^f$ de netto risicovrije rente" |
| 6 | r.421, r.423 | "$\log R^f = -\log\beta + \frac{\mu}{\psi} - ...$" en "$\log\frac{\E[R_w]}{R^f} = \gamma\sigma^2$" | opgelost F4 (was onjuist) | idem; vgl. 03_12 r.406-407 die hetzelfde met $\log(1+R^f)$ schrijft | "$\log(1+R^f) = ...$" resp. "$\log\dfrac{\E[R_w]}{1+R^f} = \gamma\sigma^2$" |
| 7 | r.429, r.431 | handuitwerking "$\log R^f = 0{,}020203 + ... = 0{,}030336$" (2×) | opgelost F4 (was onjuist) | idem | label "$\log(1+R^f)$"; getallen ongewijzigd (kloppen, zie cel 4) |
| 8 | r.447, r.456 | code-sleutel `"log R^f"` en print "log R^f uit simulatie = ..." | opgelost F4 (was onjuist) | cel 4 (nb_outputs) | label "log(1+R^f)"; waarden ongewijzigd |
| 9 | r.811, r.940, r.1011, r.1043 | `E[R^f]`, `sd(R^f)`, $\E[r^f]$ e.d. in simulatie-/replicatietabellen | opgelost F4 (was onjuist) | cel 10, 12, 13 (nb_outputs): E[R^f] voor CC = 0,009 = 0,94% netto, gelijk aan de parametertabel r.299 | hier hoeft niets te veranderen (al netto); wel bij de eerste definitie (r.130/206) expliciet maken dat R^f overal netto is, zodat het college zichzelf niet tegenspreekt (H7) |

r.648 ("De log van het bruto risicovrije rendement is $r^f = -\log\E[m]$") is wél juist:
hier wordt $r^f$ correct beschreven als log van de bruto grootheid, zonder die bruto
grootheid zelf "$R^f$" te noemen.

## B. Overige open punten uit rapport §F1

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 10 | r.318-319 | dividendclaim met "een volatiliteit van 11,2% en een correlatie van 0,2 met consumptie" | onzeker | {cite}`Wachter2005`; PDF opgehaald (finance.wharton.upenn.edu/~jwachter/research/Wachter2005frl.pdf) maar binair/niet machineleesbaar, tabel binnen budget niet te controleren | intern consistent met CC-dict in code (`sig_w=0.112, rho_w=0.2`); bron niet onafhankelijk geverifieerd — laat staan of voeg "(kalibratie, niet uit CC zelf)" toe |
| 11 | r.291 | "we overnemen uit tabel 1 van Wachter" (niet Campbell-Cochrane 1999 zelf) | onzeker | idem (PDF-beperking) | al transparant vermeld in de tekst; geen verborgen fout, alleen ongeverifieerd |
| 12 | r.362-364 | "$\beta = 0{,}896$ per jaar, wat Wachter tot 0,90 afrondt" | onzeker (eigen rekenwerk wel juist: 0,8958→0,896/0,90) | cel 3 geeft 0,8958; bronbewering (0,90) niet bij Wachter geverifieerd (idem PDF-beperking) | laag risico, evt. ongemoeid laten |
| 13 | r.1255-1287 (ex-3) | Wachters "grofste rooster" 6,59% / 15,05 / 18,62 / 0,27 | juist | cel 17 (nb_outputs) komt exact overeen | geen |
| 14 | r.59-61, r.736-737 | parafrase Santa-Clara {cite}`SantaClara2026` en Beeler-Campbell {cite}`BeelerCampbell2012` (naoorlogse autocorrelatie, Grote Depressie) | onzeker | bronnen niet binnen budget geraadpleegd (zelfde toegankelijkheidsbeperking als 10-12) | bij gelegenheid nakijken tegen de bron; geen tegenstrijdigheid met de rest van het college gevonden |
| 15 | r.287-288 | "$\sqrt{2\times0{,}13}\approx0{,}51$", "in jaartermen" | juist | nagerekend: $\sqrt{2\times0{,}13}=\sqrt{0{,}26}=0{,}5099\approx0{,}51$; jaarparameters $\gamma=2,\phi=0{,}87$ staan in de tabel r.295-301, code herschaalt zelf naar maand | geen |
| 16 | — | `HansenHeatonLi2008` | bevestigd niet geciteerd | volledige lezing van de doorlopende tekst (geen cite-tag gevonden) | geen bewering in de tekst wordt hierdoor onjuist; bibliografie-opschoning is aan de schrijver, geen actie voor feitencontrole |

## C. nb_numbers/nb_outputs, per sectie samengevat (juist)

| nr | regel | bewering | oordeel | bron of cel |
|---|---|---|---|---|
| 17 | r.117-153 | toy-voorbeeld: $m_n=0{,}878770$, $m_d=7{,}484568$, $R^f=1{,}00901$, $P/D=25{,}16$, premie $4{,}92$, rente zonder ramp 13,8%, kans op 100 jaar zonder ramp 0,18 | juist | cel 2, kolom "met de hand", exact gelijk |
| 18 | r.426-433 | EZ-toy: $\log R^f=0{,}030336$ ($\psi=1{,}5$) en $0{,}200203$ ($\psi=0{,}1$), premie $0{,}40$ procentpunt | juist | cel 4, exact gelijk |
| 19 | r.663-688 | Barro-toy: $\E[(1-b)^{-4}]=7{,}69$, $\E[(1-b)^{-3}]=4{,}05$ {cite}`Barro2009` (footnote 10, geen cel maar wel citatie); tabel $r^f=1{,}0\%$, $r^e=6{,}9\%$, $P/D=20{,}7$ | juist | cel 6, exact gelijk aan Barro (2009) tabel 3 |
| 20 | r.1030-1055 | replicatietabel CC/BY, kolom "hier" | juist | cel 12, exact gelijk |
| 21 | r.1093-1138 | data 1930-2025: gemiddeld overrendement 8,3%, SE 2,0pp, band 4,3-12,3%, percentielen | juist | cel 13, exact gelijk (E[R^e]=0,083 in kolom "data 1930-2025") |
| 22 | r.1185-1189 | oefening 1: $\E[m]=0{,}944828$, $R^f=1{,}05839$, $P/D=14{,}78$, premie $3{,}14$ | juist | cel 15, exact gelijk |
| 23 | r.1230-1249 | oefening 2: psi-tabel (1,25/1,5/2,0) | juist | cel 16, exact gelijk |
| 24 | r.1265-1287 | oefening 3: roostervarianten 2,8/3,6/4,2% | juist | cel 17, exact gelijk |
| 25 | r.1300-1329 | oefening 4: 1947-2025 en 1930-1998 percentielen | juist | cel 18, exact gelijk |

**Open = onjuist (9, rijen 1-9) + onzeker (4, rijen 10,11,12,14) = 13.**

**Na F4 (2026-09-30):** rijen 1-9 opgelost: $R^f$ overal netto, $1+R^f = 1/\E[m]$, $r^f = \log(1+R^f)$ in proza, formules, oefening 1-2 en de sleutels `1+R^f`, `log(1+R^f)`, `R^f = Rf_d - 1` in de code; celuitvoer verschilt alleen in labels. Rij 9: definitie bij de eerste vermelding (toy en notatie in Theorie) zegt nu expliciet dat $R^f$ overal netto is. Rijen 10, 11, 12, 14 blijven onzeker (bronnen niet raadpleegbaar, geen tekst gewijzigd). **Open = 4.**
