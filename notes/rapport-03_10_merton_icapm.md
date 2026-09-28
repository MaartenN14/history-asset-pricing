STATUS 03_10_merton_icapm F6b-2 words=5497 prose=PASS open=0 cijfer=- min=-

# Rapport 03_10_merton_icapm (workflow-herziening)

## F0

**Nulmeting.** `03_10_merton_icapm.md  words 7354  sent_mean 20.1  sent_p90 35  sent_gt40 17  para_mean 66  dash 32  semicol 41  motief 2  Lnum 0  deel 0  u_form 1  je_form 2  taboo 0  stopw 17  calque 2  engquote 14`. `--where`: r. 568 "Noteer", r. 1189 "Twee dingen". (`--where` breekt op de console-codering bij "−"; gedraaid met `PYTHONIOENCODING=utf-8`.)

**Vijf grootste problemen.**
1. *Lengte*: 7.354 woorden, ruim boven 5.500. Zwaartepunten: Oefeningen (≈ 740), Intuïtie (≈ 520), Toy (≈ 510), Wat er brak (≈ 500), Theorie met zeven `###` (≈ 2.430) en een simulatie van drie subsecties (≈ 990).
2. *Structuur*: imports-cel in *Overzicht* (r. 83); Overzicht zonder vraag-antwoord en lijst, met een "epistemisch"-alinea en een vooruitverwijzing naar 04_18 (r. 58–66); geen routekaart, geen *Samengevat*; de numerieke Kim-Omberg-oplossing en de roostercontrole staan in *Simulatie* (§11.7: numerieke oplossing hoort in Theorie); drie simulatievragen; cellen zonder zin ervoor of erna (r. 227, 1044, 1295, 1305).
3. *Replicatie*: blok ≈ 424 woorden met Engelse citaten en getallen; tabelgetallen herhaald in proza (r. 859–867, 968–974, 1084–1093, 1185–1193, 1235–1246, 1352–1358); geen tabel origineel/hier voor de horizonallocaties en geen oordeel "Geslaagd/Gedeeltelijk/Niet".
4. *Notatie* (setup, sectie Notatie): $R^{f} = 1$ als bruto (r. 154, 321); $m(x_t)$ als drift van de toestand botst met de SDF $m$ (r. 490); $r^{e}_{t+1}$ als log-rendement met "kleine letters logs" (r. 773–785; boek: $\ell$); "$Z_t$ zoals in [](#02-09-black-scholes)" terwijl die lecture $W_t$ gebruikt en hier $W$ het vermogen is (r. 282); $\lambda_t$ is hier de Sharpe-ratio en in het ICAPM de prijs van risico; "$A$" voor risicoaversie in r. 1128 en 1529.
5. *Taal en jargon*: 17 zinnen > 40 woorden, 32 streepjes, 41 puntkomma's, alinea's van 66 woorden; "motief 1" r. 1084 en 1359, "u" r. 1397, "je" r. 151 en 1420; 14 Engelse citaten midden in de zin (r. 73, 133, 1123–1128); oefening 1 is geen instap, geen uitwerking eindigt met "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** `03-10-merton-icapm` wordt aangehaald in 02_09, 03_11, 04_18, 04_20 (twee keer), 04_21 (drie keer), 04_24, 05_26, 05_31 (drie keer), 05_32. Label `fig-merton-icapm-steekproef` in 04_20 (Stambaugh-simulatie). Inhoudelijk aangehaald: Barberis' VAR met $t$ rond twee (04_20), hedgevraag op een helling met $t$ rond één (05_31), Merton-portefeuille $\pi/(\gamma\sigma^2)$ bij constante kansen (05_32), toestandsvariabelen in het ICAPM (04_24, 05_26, 04_18), marktpremie stijgt met risicoaversie maal variantie (04_21). Geen andere `eq-`, `thm-`, `ex-` of `fig-`labels worden elders aangehaald.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Waar we zijn | Itô- en optiezin ingekort | 45 | niet nodig voor de vraag |
| Overzicht | "epistemisch"-alinea, vooruitverwijzing 04_18 | 110 | wordt één zin *theorie of feit* |
| Overzicht | Engelse citaten, detail Campbell-Viceira-boek | 60 | citaat; blijft als parafrase |
| Intuïtie | note over de twee artikelen van 1969 (nummer, pagina's) | 90 | anekdote, niemand haalt aan |
| Intuïtie | log-nutzin, dubbele formuleringen, Engels citaat | 70 | herhaalt Theorie |
| Toy | continue-tijdvergelijking tussen haakjes, proza bij q | 90 | wordt stappen en tabel |
| Theorie | Opzet: consumptie-uitleg, Mertons notatie | 60 | één zin volstaat |
| Theorie | Samuelson: slotalinea (Merton 1971, consumptie) | 100 | nevenresultaat |
| Theorie | note consumptie en HARA (Merton 1971) | 155 | nevenresultaat, niet aangehaald |
| Theorie | Merton-portefeuille: "geen benadering maar stelling" | 70 | ingekort tot één zin |
| Theorie | Kim-Omberg: bewijs (dropdown) tot schets | 160 | dropdown telt; oefening 2 draagt de afleiding |
| Theorie | Breeden-subsectie tot twee zinnen | 65 | vooruitblik op 03_12 |
| Simulatie | Kim-Omberg-tabel en roostercontrole: proza met getallen | 230 | naar Theorie "Numerieke oplossing", getallen in tabel |
| Simulatie | Barberis-alinea na de steekproef, getallenproza | 150 | herhaalt tabel; Barberis naar Replicatie |
| Replicatie | blok van 424 naar ≤ 250 (citaten, VAR-getallen) | 180 | §11.7; getallen staan in de tabel |
| Replicatie | proza bij VAR, horizon en onzekerheid | 180 | getallen in tabel met oordeel |
| Wat er brak | elk element ≤ 120 woorden | 100 | te lang |
| Oefeningen | drie uitwerkingen ingekort, volgorde instap/afleiding/replicatie | 290 | herhaling van tekst en tabel |
| **totaal** | | **≈ 2.155** | |

**Verwachte lengte.** 7.354 − 2.155 ≈ 5.200; erbij komen routekaart, *Samengevat*, vraag-antwoord en lijst, zinnen rond cellen, oordelen onder tabellen en "Wat dit leert" (≈ 250), af door strakkere zinnen overal (≈ 300). Verwacht 5.000 tot 5.300. De kern (Samuelson, HJB, Merton-portefeuille, hedgevraag, ICAPM) blijft volledig. Geen splitsing.

## F1

**Eindmeting.** `words 5296  sent_mean 14.0  sent_p90 23  sent_gt40 0  para_mean 41  dash 0  semicol 5  motief 0  u_form 0  je_form 0  taboo 0  stopw 0  calque 0  engquote 0` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1`: foutloos, geen warnings in de uitvoer.

**Geschrapt of verplaatst (schraplijst F0 uitgevoerd).** "Epistemisch"-alinea en vooruitverwijzing 04_18 (wordt één zin *theorie of feit*); note over de artikelen van 1969 (anekdote); note consumptie en HARA, slotalinea Samuelson over Merton 1971 (nevenresultaat; `Merton1971` en `Wachter2002` niet meer geciteerd); Kim-Omberg-bewijs tot schets in dropdown; Breeden tot twee zinnen; alle Engelse citaten geparafraseerd; replicatieblok van ≈ 424 naar ≈ 200 woorden; getallenproza vervangen door verwijzing naar de tabel plus oordeel; drie uitwerkingen ingekort. De Kim-Omberg-tabel, figuur en roostercontrole staan nu in Theorie ("Numerieke oplossing", §11.7); *Simulatie* heeft één vraag (een eeuw data en de hedgevraag).

**Toegevoegd.** Vraag-antwoord en lijst in *Overzicht*; drie voorspellingen aan het eind van *Intuïtie* (H12), ingelost bij de hedgevraag en het ICAPM; toy als opzet-tabel, vijf stappen, één cel met tabel hand/code; routekaart en *Samengevat*; lees-zin bij elke genummerde vergelijking; toy-getallen terug in Theorie ($q = 25/26$, 0,7396 tegen 0,8333, geval B' 0,7909); marktpremie $\gamma\sigma_m^2$ (8% bij $\gamma=2$, $\sigma_m=20\%$, voor 04_21); twee fondsen / drie-fondsenstelling expliciet; oordelen "Geslaagd" (VAR, horizon) en "Gedeeltelijk geslaagd" (parameteronzekerheid); "Wat dit leert:" bij elke uitwerking.

**Notatie.** $R^{f}$ netto (toy $R^f = 0$, $W_{t+1} = W_t(1+R^f+wR^e)$); $r$ als continu samengestelde rente aangekondigd zoals in 02_09; Brownse beweging blijft $Z_t$ met de zin dat 02_09 haar $W_t$ noemt en $W$ hier het vermogen is (naadpunt); drift van de toestand $\mu_x$, $\sigma_x$ (was $m$, $s$; $m$ is de SDF); log excess rendement $\ell^{e}$ met "vanaf hier zijn kleine letters logs"; Sharpe-ratio $\eta$ (was $\lambda$, botste met prijs van risico); index $m$ expliciet "de markt, zoals in 02_08"; "$A$" voor risicoaversie verdwenen.

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- cel 2 (toy): kolom "met de hand" toegevoegd, kolomnamen anders; alle waarden gelijk.
- cel 7: `print` → `pd.Series`; 55.5% → 0.555 en 0.1% → 0.001 (zelfde getallen).
- oude cellen 13 en 14 samengevoegd (één cel, zelfde `rng`-volgorde); tabel identiek.
- oefeningen 1 en 2 van plaats gewisseld (instap eerst); uitvoer identiek.
- Alle andere uitvoer (Kim-Omberg, rooster, steekproef, VAR's, posterior, figuren) byte-gelijk.

**Afvinklijst §11.9, wat niet voldoet.** Na de imports-cel volgt direct de opzet-tabel (zoals in de template). Overige: ok.

**Labels.** Geen verdwenen labels. `ex-merton-icapm-1` is nu de instap (toy), `-2` de afleiding ($C_\infty$); geen van beide wordt buiten deze lecture aangehaald. `fig-merton-icapm-steekproef` (04_20) blijft.

**Open punten.**
1. `--where` breekt op de Windows-console bij "−" (UnicodeEncodeError); werkt met `PYTHONIOENCODING=utf-8`. Tool niet aangepast.
2. 04_21 r. 506 schrijft het ICAPM de risico-rendementsrelatie van de markt toe; die staat nu als één zin bij de Merton-portefeuille ($\mu_m - r = \gamma\sigma_m^2$), niet als stelling.

## F4

**Eindmeting.** `words 5307  sent_mean 14.1  sent_p90 23  sent_gt40 0  para_mean 41  dash 0  semicol 4` en de rest 0 → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings.

**Feitenlijst (F2), beide open punten opgelost.** Rij 1: "uitloop naar 2002" wordt "uitloop naar 2000" (Barberis 2000 is de jongste bron). Rij 2: "vergelijking (12) van Merton1969" wordt "de vermogensvergelijking van Merton1969" (zonder nummer).

**Lezerspunten (F3).** Opgelost: 1 (fout in het Kim-Omberg-bewijs: $w^\ast = [\eta + (g_\eta/g)\rho\sigma_\eta]/(\gamma\sigma)$), 2 (stap $J = \max\E_t[J(W_{t+dt},t+dt)]$ ⇒ $0 = \max\E_t[dJ]$ toegevoegd), 3 (bijzin "Theorie leidt die vorm af"), 4 (= F2 rij 1), 5 (zin over de gelijke stationaire variantie $\sigma_z^2/(2\kappa) = \SD(\varepsilon_2)^2/(1-\phi^2)$), 6 ($\delta = -0{,}8$ bij $\gamma = 5$), 7 ("ruim vijf procent meer dan de myopische fractie"), 8 (kolommen heten nu "myopische vraag" en "hedgevraag"), 9 (de opgave zegt hoe de hedgevraag uit `toy_table` volgt), 10 ($\E[e^\ell] = e^{\E[\ell]+\sigma^2/2}$ in één bijzin), 11 ("hoeveel gewicht de belegger daaraan hecht"), 12 (zin in *Intuïtie* herschreven), 14 ("zoals onder de stelling vastgesteld"), 15 (puntkomma in het replicatieblok wordt twee zinnen).
Afgewezen: 13, want de TODO-regel `# TODO: naar hap.stats` is volgens STYLE §5 verplicht bij een lokale implementatie die in `hap` ontbreekt.

**Navertel-toets.** De lezer meldde geen sectie waarvan de navertelling afweek van de bedoeling. Punt 4 (het jaartal) kwam uit de navertelling van *Wat er brak*; dat is opgelost.

**Betaald met schrappen (≈ 45 woorden erbij, ≈ 35 eraf).** Uit *Intuïtie*: "Die zin opende de deur voor elk meerfactormodel". Uit *Wat het model verklaart*: de zin over Itô en HJB als taal van de latere literatuur. Uit *Parameteronzekerheid*: "Ook dat getal hangt aan een helling met een $t$-waarde van één" (dat zegt *Waar het breekt* al).

**`nb_outputs`-diff (F1 → F4).** Alleen andere kolomnamen in cel 3 en cel 11 ("myopisch/hedge" wordt "myopische vraag/hedgevraag"). Alle waarden zijn gelijk.

**Open punten.** Geen.


## F5-1

**Meting.** `words 5475  sent_mean 14.1  sent_p90 23  sent_gt40 0  para_mean 41  semicol 4`, rest 0 → PASS. Sync en uitvoering met `HAP_OFFLINE=1` foutloos, geen warnings.

- **Fout $\lambda_x$: gedaan.** Het vaste teken hoort bij de covariantiepremie $b_x = -\bar H/\bar T$; een zin erbij zegt dat $\lambda_x$ bij $\rho<0$ geen vast teken heeft.
- **Helderheid: gedaan.** De botsingen $T_k$ (tegen horizon $T$) en $\mathbf B$ (tegen $B(\tau)$) worden gemeld, en de notatie $J_t, J_W, J_{WW}$ wordt genoemd. Het bijschrift van de horizonfiguur klopt nu met de tabel: bijna rechtlijnig tot twintig jaar, op vijftig jaar nog onder de grens van oefening 2. Het ICAPM krijgt één getal: $\mu_m-r=\gamma\sigma^2(1-h)=0{,}162\cdot0{,}661=10{,}7\%$ tegen $16{,}2\%$.
- **Opbouw: gedaan.** De routekaart zegt "vijf resultaten", met de kern bij de vierde stap. De kopjes zijn gewisseld ("De hedgevraag", "Het kernresultaat: het intertemporele CAPM"). Het Overzicht heeft één zin dat de empirie de vraagkant toetst. De eerste voorspelling van de intuïtie wordt bij Samuelson ingelost. De tekst na de roostercontrole is twee zinnen; de cel blijft, want de replicatie gebruikt `solve_rebalancing`.
- **Taal: gedaan.** De drie telegramzinnen zijn volledige zinnen geworden. Chicago en Yale krijgen elk een bijzin, en "die toets kiest nog niet" is "de data van deze lecture beslissen dat niet".
- **Toy: gedaan.** Het recept verwijst naar stap 4.
- **Code.** Gedaan: `einsum` is vervangen door benoemde stappen met dezelfde trekkingen in dezelfde volgorde, plus een zin over de matrix-normale trekking; de vijf lambda's zijn benoemde functies. Afgewezen: de TODO, omdat STYLE §5 `# TODO: naar hap.stats` voorschrijft. `np.broadcast` in `kim_omberg` blijft, want de simulatie heeft de vectorisatie nodig.
- **Replicatie: gedaan.** Er zijn tabellen origineel/hier voor Campbell-Viceira (tot 2 tegen 1,499 en 1,943) en voor Barberis (overallocatie 0,045 tegen > 30%). De Barberis-tabel neemt ook de getallen van de laatste twee alinea's op (0,019; 0,032; D/P −1,864 sd; 0,483), en de proza verwijst ernaar. De verwachte afwijking zegt nu "de helling over de hele eeuw is zwakker dan over 1952–1995", en oefening 3 legt uit waarom $t=2{,}60$ voor 1996–2025 daar niet mee botst.
- **Oefeningen: gedaan.** Oefening 3 noemt dat de grens van 0,99 bij tien jaar bindt.
- **Lengte.** Er kwamen ≈ 170 woorden bij en er gingen ≈ 50 af (roostertekst, eind-2025-alinea, een dubbele zin in *Simulatie*). Het resultaat, 5.475, blijft onder 5.500.
- **`nb_outputs`-diff (F4 → F5).** Twee nieuwe tabelcellen. Alle bestaande uitvoer is gelijk, ook de posterior en oefening 3 na de `einsum`-herschrijving; alleen de celnummers verschuiven.
- **Herlezing met de rubriek.** Geen nieuwe punten.

## F5-2

Onder de Barberis-tabel staat nu één zin: onze 4,5% geldt voor $\gamma = 5$ met jaarlijkse herbalancering, tegenover Barberis' koop-en-houdbelegger met risicoaversie 10, dus de vergelijking geeft alleen een orde van grootte. Betaald door uit *Wat het model verklaart* de zin over de levenscyclusliteratuur en pensioenfondsen te schrappen. Het resultaat is 5.483 woorden, PASS. De `nb_outputs`-uitvoer is identiek aan F5-1.

## F6-1

**Meting.** `words 5493  sent_mean 14.1  sent_p90 23  sent_gt40 0  para_mean 40  semicol 4`, rest 0 → PASS. Sync en uitvoering met `HAP_OFFLINE=1` foutloos, geen warnings.

- **Feitelijke fout: gedaan.** Een nieuwe tabel geeft per beginstand het kleinste en grootste verschil: 0,019–0,032 vanaf gemiddeld, 0,012–0,019 vanaf eind 2025. De tekst zegt "twee à drie procentpunt vanaf een gemiddelde dividendopbrengst, vanaf eind 2025 ruim één à twee".
- **Code (7 → ≥ 8): gedaan.**
  - `kim_omberg` gebruikt geen `np.broadcast` en `np.broadcast_to` meer, maar benoemde stappen: één $B$ en $C$ per parameterset, en de myopische vraag die op elke horizon gelijk is. De functie blijft gevectoriseerd, want de simulatie lost 1000 parametersets op.
  - De simulatiecel is gesplitst in `ols_var`, de simulatie met schatting, en de tabel, met een zin tussen de cellen.
  - De TODO staat als commentaarregel boven `ols_var` en niet meer in de docstring. STYLE §5 vraagt de regel zelf.
  - `transpose(0, 2, 1)` heet nu `L_sigma_t`, met commentaar.
- **Kim-Omberg met getal en beeld: gedaan.** Onder de VAR-tabel staan de handberekeningen $\theta = 0{,}34$ en $\sigma_\eta = 0{,}069$. Eén zin in de hoofdtekst zegt dat $B + C\eta$ meet hoe de waarde van de toekomst meebeweegt met de Sharpe-ratio. "Hoe groot is het effect?" (10,7% tegen 16,2%) staat nu na de Kim-Omberg-tabel, zodat $h = 0{,}339$ niet meer vooruitgeleend wordt.
- **Replicatietabellen: gedaan.** De Campbell-Viceira-tabel heeft nog één rij met origineel. De Barberis-vergelijking heeft alleen de rij met origineel (> 30% tegen 0,045). De verschillen en eind 2025 staan in een aparte tabel zonder kolom "origineel".
  Afgewezen: het getal van Campbell en Viceira bij een vergelijkbare $\gamma$ noemen. Het artikel is hier niet geverifieerd, en STYLE §11.11 "Feiten" eist dat elk getal herleidbaar is.
- **Naadpunt 5: gedaan.** "Waar we zijn" zegt nu: in 02-09 leverde de stochastische calculus de prijs van een optie; Merton gebruikte die wiskunde al vanaf 1969 voor de portefeuillekeuze, het onderwerp van deze lecture.
- **Naadpunten 7–10:** zoals opgedragen niet gewijzigd.
- **Betaald met schrappen.**
  - De tekst rond de roostercontrole is ingekort tot één zin voor en één zin na de cel, zoals het eind-bestand bij opbouw vroeg.
  - Geschrapt: "Op die ene $t$-waarde rust de hele literatuur" (retorische overdrijving, taal).
  - Geschrapt: "Beide soorten werelden ondermijnen…".
- **`nb_outputs`-diff (F5-2 → F6).** Nieuwe celgrenzen in de simulatie. De Campbell-Viceira-tabel mist de rij 1,499; de Barberis-tabel is gesplitst in twee tabellen. Alle overige waarden zijn identiek, ook Kim-Omberg na de herschrijving.

## F6-2

- **$J_t$ met twee betekenissen: gedaan.** De waardefunctie in discrete tijd (Samuelson-bewijs) heet nu $V_t(W)$, met één zin dat $J_t$ verderop een afgeleide is.
- **Opening "Dat getal" (H8): gedaan.** De alinea begint nu met "De hedgevraag van 0,339 bij $\gamma = 5$ op twintig jaar bepaalt ook hoe groot het ICAPM-effect is."
- **Overige punten uit Controle 1: gedaan.** De tweede voorspelling wordt ingelost bij de horizonfiguur. De kommazin in stap 4 is gesplitst. "Vergunning" is vervangen door "grond". "Kortweg de kansen" is één keer ingevoerd als alias van "beleggingskansen".
- **Betaald met schrappen.** Weg zijn de openingsvraag van *Numerieke oplossing*, de zin "Hij heeft in het beste geval een eeuw jaarcijfers" (samengevoegd met de vraag erna), "Gesloten vorm en numerieke oplossing vallen samen" (oefening 2), en een deel van de slotzin van het toy. Het resultaat is 5.497 woorden, PASS.
- **Verificatie.** Sync en uitvoering met `HAP_OFFLINE=1` foutloos. De `nb_outputs`-uitvoer is identiek aan F6-1.

## R9-1 (F6b, ronde 9+)

- **Feitelijk, r. 234–235 (consumptie).** Gedaan: beperkt tot constante kansen (Merton-portefeuille), plus dat tussentijdse consumptie de hedgevraag tot een gewogen gemiddelde over horizonnen maakt (teken blijft, grootte verandert).
- **Code, roostercel.** Gedaan: gesplitst in een functiecel (`solve_rebalancing`, `normal_shocks`) en een controlecel, met één zin ertussen; RNG-volgorde ongewijzigd. Na uitvoering (offline) verschillen in `nb_outputs` alleen celnummers en labels.
- **Beter uitleggen, roostercontrole.** Gedaan: bijzin dat de continue vertaling een benadering is en dat het rooster later de replicatie draagt.
- **Numerieke oplossing, $\gamma = 2$.** Gedaan: zin zegt nu dat de tabel $\gamma = 2$ weglaat vanwege de grens 0,99.
- **Numerieke oplossing, log-rendement.** Gedaan: "het verwachte log-rendement".
- **Overrendement (H7).** Gedaan: admonition "log overrendement", tabelindex "a (gem. log overrendement)".
- **"die gok" (r. 376).** Gedaan: "die proefoplossing".
- **Hardop-toets r. 62, 971, 1281.** Gedaan: "Is het ICAPM theorie of feit? Het is een theorie met een open plek, want ..."; leeswijzer noemt linkerpaneel (gestreepte lijn rechts van de zwarte) en rechterpaneel (breedte); "Ook dit verschil volgt uit de standaardfout van 2%, want ...".
- **"het het" (r. 565).** Gedaan: "wanneer de belegger dat het minst nodig heeft".
- **Stellingkop, r. 278.** Gedaan: "Irrelevantie van de horizon".
- **koop-en-houd (r. 1277, 1283).** Gedaan: "buy-and-hold-belegger", "buy-and-hold-getal".
- **Figuurtitel r. 990.** Gedaan: "Waartegen de belegger denkt zich te moeten indekken".
- **Tabelkolom r. 1258.** Gedaan: "D/P in standaarddeviaties".
- **Oefening 1, "w0".** Gedaan: "de fractie in geval B".
- **r. 58 (niet vereist).** Gedaan: "omdat het asset pricing dynamisch maakte".
- Controles: `prose_stats --check` PASS, 5.899 woorden; `nb_numbers` geen nieuwe meldingen; `rewrap` en `jupytext --sync` gedraaid.
