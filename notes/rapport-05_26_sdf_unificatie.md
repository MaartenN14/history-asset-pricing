STATUS 05_26_sdf_unificatie F4T words=5542 prose=PASS open=0 cijfer=- min=-

# Rapport 05_26_sdf_unificatie

**Kern.** Zijn CAPM, consumptie-CAPM, APT en Fama-French verschillende theorieën? Nee: het
zijn keuzes voor één discontofactor $m$ in $p = \E[mx]$, zodat bèta, frontier en SDF
hetzelfde zeggen en modellen met één maat (de HJ-afstand, en $b$ in plaats van $\lambda$)
te vergelijken zijn.

## F0

`05_26_sdf_unificatie.md 4667 17.6 31 7 50 1 41 7 0 2 0 3 0 1 17 17 9.9 29 1 7 3 21 0 4/5`
FAIL: sent_p90=31, sent_gt40=7, semicol=41, motief=7, deel=2, je_form=3, calque=17,
engquote=17, colon_mid=9.9, para_one=29, telegram=1, tmpl=7 ("Waarom zou" 7×).

Vijf grootste problemen:
1. Taal (hele college): 41 puntkomma's, 17 Engelse citaten midden in zinnen (Overzicht
   r.59–64, Theorie r.548, r.597, r.620, replicatieblok r.857), 17 calques
   (prijst/beprijsd, Cochrane's, in-sample), 29 alinea's van één zin, 7× "Waarom zou dit waar
   zijn?" als vast etiket in Theorie (r.259–609).
2. Structuur: imports-cel in Overzicht (r.74); Theorie zonder routekaart (r.244) en zonder
   "Samengevat" (na r.621); bewijzen van 10–18 regels open (Stelling 1 r.286, corollarium
   r.395, HJ r.578).
3. Twee simulaties met twee vragen (r.625 $b$ tegenover $\lambda$, r.773 HJ-afstand).
4. Projectjargon: "Deel IV/V" (r.24, r.1030), "motief 3/1", "2%-motief", "epistemische
   status" (r.55, 470, 546, 770, 839, 913); oefeningslabels als linkdoel (r.242, 621, 949).
5. Toy en replicatie: toy rekent na $x^*$ ook $R^*$ en de bèta met nog niet afgeleide
   formules (r.170–194) en eindigt zonder tabel hand/code; replicatieblok ≈ 330 woorden
   (r.849–886), en het oordeel (r.946) staat in een getallenalinea zonder tabel
   verwacht/hier en zonder "Geslaagd".

Schraplijst (eis 2 gecontroleerd met grep: van buiten aangehaald zijn alleen de pagina,
`prop-sdf-unificatie-b-lambda` en `eq-sdf-unificatie-b-lambda`):

| passage | kopje | woorden | eis niet gehaald | actie |
|---|---|---|---|---|
| Engelse citaten HJ, KRS | Overzicht | −40 | 1, 3 (bewoording niet nodig) | parafraseren |
| efficiëntiedebat Kan-Zhou / Jagannathan-Wang 2002 | GMM | −45 | 1, 2, 3 | schrappen |
| conditionering als `###` | Theorie | −80 | 1, 2 (alleen oefening 2) | korte dropdown-note |
| simulatie (b), figuur en bijschrift | Simulatie | −90 | tweede simulatie | dropdown-note, figuur weg |
| replicatieblok | Replicatie | −90 | §11.7 ≤ 250 | inkorten |
| deel (3) van oefening 1 ($w$ voor $R^f$) | Oefeningen | −50 | 1, 2, 3 | schrappen |
| $R^*$ en bèta in toy | Toy | 0 | tweede mechanisme | naar Theorie als illustratie |

Toevoegingen: routekaart +60, Samengevat +80, tabel verwacht/hier +70, lees-zinnen +80,
voegwoorden +150. Verwachte lengte ≈ 4667 − 395 + 440 ≈ 4.700 woorden. Geen splitsing.

## F1

Eindmeting: `5456 15.4 24 0 46 0 5 0 0 0 0 0 0 0 0 0 4.4 6 0 2 0 31 0 0/4` PASS. Rewrap,
jupytext --sync en nbconvert --execute (HAP_OFFLINE=1) zonder fouten.

Geschrapt of verplaatst:
- Engelse citaten (HJ 1997 ×2, KRS, JW 1996, JW 2002, FF 2015): geparafraseerd; geen bewoording nodig.
- Kan-Zhou/Jagannathan-Wang 2002 over efficiëntie van de SDF-methode: geschrapt (eis 1–3).
- `### Conditionering`: dropdown-note van ≈ 90 woorden; alleen oefening 2 steunt erop.
- Simulatie (b) HJ-afstand: dropdown-note met de rekencel; plotcel en figuur geschrapt. De
  rekencel blijft omdat oefening 3 dezelfde `rng`-stroom gebruikt (getallen gelijk).
- $R^*$ en bèta uit de toy naar Theorie (na het corollarium) als illustratie (H11).
- Oefening 1 deel 3 ($w$ voor $R^f$) en de bijbehorende print: geschrapt.
- "Waar we zijn" terug naar twee verwijzingen (03-13, 04-25); "Deel IV/V" weg.

nb_outputs-diff (alleen presentatie, geen aangehaald getal veranderd):
- cel 2 (toy): print + Series vervangen door tabel "met de hand / code"; alle waarden gelijk.
- plotcel sim (b) (oud cel 7) weg.
- momentumcel: kolom "gem. excess" → "gem. overrendement"; waarden gelijk.
- grenscel: rij "(in-sample)" → "(binnen de steekproef)"; waarden gelijk.
- oefening 1: printregel $w$ voor $R^f$ weg.
- `rng.chisquare(1, size=...)` → positioneel (zelfde trekkingen; uitvoer identiek).

Afvinklijst §11.9, niet (volledig) voldaan:
- Eén simulatie: de tweede staat als ingeklapte note met code (zie boven).
- Replicatietabel heet "verwachting / hier": er zijn geen gepubliceerde getallen om naast te zetten.
- 34 nb_numbers-meldingen zijn getoonde handberekeningen (toy, $R^*$, bèta, 0,71, 0,17%), nagerekend.
- Overige: ok.

Labels: weg `cel-sdf-unificatie-sim-hj`, `fig-sdf-unificatie-sim-hj` (nergens aangehaald).
Links naar `ex-sdf-unificatie-1/2` en `ex-fama-french-3` vervangen door tekst.

Open punten voor de feitencontroleur:
1. Code-cel binnen `:::{note}` met dropdown heeft geen precedent in lectures/; build nagaan.
2. Parafrase FamaFrench2015 (HML overbodig met RMW/CMA) en JagannathanWang1996
   ("groot deel van de spreiding") tegen de abstracts.
3. Parafrase HansenJagannathan1997: afstand beloont geen ruisige kandidaat-SDF.
4. `rem-apt-no-arbitrage-sdf`: negatieve SDF geeft opties een negatieve prijs, niet nagekeken.
5. `prop-fama-french-mechanisch`: hoge $R^2$ met vrij intercept bij verkeerde premies, niet nagekeken.
6. Deel IV nagekeken: `thm-fama-french-sdf` ($\mathbf{b} = \Sigma_f^{-1}\E\mathbf{f}$, dus
   $\lambda = \E\mathbf{f}$), klein-groei in 04-18, derde oefening 04-18 (winnaars HML-lading
   −0,24), 04-25 (DFA/AQR verkopen factorblootstelling): kloppen. 03-13 $\gamma = 15$ en
   dertig procent rente: klopt (r.1003).

## F4

Eindmeting na F4T: words=5542, prose_stats `--check` PASS (sent_gt40 0, tmpl 1), nb_numbers
34 meldingen, dezelfde als vóór F4T; geen code gewijzigd, dus geen herexecutie.

Feitenrijen 1–17: juist, niets te doen. Rij 18 (code-cel in dropdown-note): n.v.t., precedent
in 04_24, uitvoer foutloos. open=0.

Lezerspunten (alle vijftien gedaan):
- 1 Stelling 3, premie als covariantiegewogen som over alle $\mathbf b$ herschreven.
- 2 Stelling 3, "op een schaal na, gelijk aan bèta's".
- 3 Stelling 1, conjunctief "Als er ... bestond, zou ...".
- 4 GMM, "waarbij we $\hat\Sigma_f$ als bekend behandelen".
- 5 Toy/recept, vooruitverwijzing als eigen zin.
- 6 Opzet, $L^2$-definitie in twee zinnen; Cochrane "neemt ze over".
- 7 Intuïtie, "richtingen die bij geen enkel verhandeld activum de prijs veranderen".
- 8 en 14 Simulatie en Replicatie (2), figuuraankondigingen gevarieerd en als aankondiging.
- 9 Stelling 4, eerste zin van de asymptotiek zegt waarom de ruisbodem nodig is.
- 10 Stelling 3, "zegt steeds minder over $\mathbf b$", samengevoegd met de reden.
- 11 Oefening 2, staccato met "terwijl" verbonden.
- 12 Replicatie (2), annualisering in de vorige zin opgenomen.
- 13 Stelling 2, vulzin weg; toy-illustratie begint direct met $p(x^*)$.
- 15 Replicatie (2), "geen economische inhoud" vervangen door wat ontbreekt (herschreven, niet toegevoegd).

Navertel-toets: geen sectie week af van de bedoeling (lezer-bestand bevestigt alle secties).

## R9-1 (F6b, ronde 9+)

- **Feitelijke fouten.** (1) Oplossing 3: "23 procentpunt" wordt "26 procentpunt die UMD in de puntschatting toevoegt" (0,758 − 0,496). (2) Figuuronderschrift: "de factor-SDF's die halen, FF3 en FF3+UMD ruim". (3) Corollarium: $\gamma$ wordt de nulbèta-rente $R^0$ (ook in bewijs en toy); tabelregel consumptie-CAPM noemt nu "risicoaversie $\gamma$" en "tijdsvoorkeur" zonder $\beta$.
- **Helderheid.** Sprong :302 gedicht (elk rendement kost één, Cauchy-Schwarz, norm van $R^*$); ruisbodem gedicht ($\mathbf S \approx \mathbf G$, gewichten rond één, $\E[T\hat\delta^2] \approx N-K$); twee fondsen nu $R^*$ en $R^* + R^{e*}$; Santa-Clara bij naam met verwijzing naar de setup; "verzekering" concreet (keert het meest uit waar het aandeel het minst oplevert); correctieterm in $\mathbf h_t$ klein genoemd; toy stap 5 wijst vooruit naar de HJ-grens.
- **Opbouw.** GMM-sectie zegt waar de schatter terugkomt; laatste punt van Samengevat is nu een resultaat (GMM als gewogen regressie, $J \sim \chi^2(N-K)$); simulatie zegt waarom de kalibratie niet uit het toy komt.
- **Taal.** :90–93, :476–478, :515, :862–864 (motief niet meer als oorzaak, zin < 40), :1268 ("het conditionele CAPM") herschreven; hybriden "frontier-rendement" en "frontierportefeuille" vervangen; bronregels opnieuw gewrapt (gebroken alinea's samengevoegd, alleen regeleinden veranderd, tokens identiek), daarna `rewrap.py`.
- **Code en figuren.** `sd_m_consumption` benoemd en in tabel en figuur gebruikt; rijnaam ingekort tot "HJ-grens, 35 portefeuilles + 4 factoren" (niet meer afgekapt); commentaar bij de gesimuleerde $p$-waarde. Uitgevoerd offline; alleen de rijnaam verschilt in de uitvoer.
- **Replicatie.** Toelichting tabel (1) noemt alleen 0,41 → 0,36 en verklaart $p = 0{,}02$ op 25 tegen 0,00 op 35 (momentum maakt de toets strenger); toelichting tabel (3) herhaalt de $t$-waarden uit de verwachtingentabel niet meer. Afgewezen: getallen uit de originele artikelen, want die staan niet in een cel of geciteerde bron in het college (kaart §6).
- **Oefeningen.** Oefening 2 deel 1 vraagt nu welke momenten erbij komen met geschaalde payoffs; de uitwerking noemt $\E[m_{t+1}z_tR^e_{t+1}] = 0$ en dat de code de 35 portefeuilles houdt.
- **Woorden:** 5.725 (was 5.542); prose_stats PASS, geen zin > 40; nb_numbers geen nieuwe meldingen.
