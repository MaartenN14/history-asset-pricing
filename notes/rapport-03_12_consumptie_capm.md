STATUS 03_12_consumptie_capm F6b-2 words=5211 prose=PASS open=0 cijfer=- min=-

# Rapport 03_12_consumptie_capm (workflow-herziening)

## F0

**Nulmeting.** `03_12_consumptie_capm.md  words 5822  sent_mean 19.9  sent_p90 35  sent_gt40 14  para_mean 57  dash 29  semicol 45  motief 4  Lnum 0  deel 3  u_form 3  je_form 4  taboo 1  stopw 8  calque 14  engquote 6`. `--where`: r. 34 "vastgeknoopt", r. 35 "restpost", r. 44 "bestaansobject", r. 55 "het hart van" en "epistemisch", r. 304 kop "epistemische wending", r. 325 "Dit is wat", r. 805 en 1060 "Onthoud dat", r. 910 "Drie dingen", r. 928 "omvang van de toets", r. 1060 "Leg dit naast", r. 1143 "de nul", r. 1210 "Noteer ... epistemische".

**Vijf grootste problemen.**
1. *Taal*, overal: zinnen van gemiddeld 19,9 woorden, 14 boven 40, alinea's van 57 woorden, 29 streepjes, 45 puntkomma's. u/je-vorm in *Intuïtie* (r. 88, 109), GMM (r. 568), SDF-uitleg (r. 43), bewijs consumptiebèta (r. 540). "verrassend rond" (r. 151).
2. *Projectjargon*: "epistemische wending" (r. 55, kop r. 304), "epistemische status" (r. 1210), "het 2%-motief" (r. 910), "2%-motief" (r. 1154), "Deel V" (r. 423, 553, 806).
3. *Structuur*: imports-cel in *Overzicht* (r. 73); Overzicht zonder vraag-antwoord en lijst; geen routekaart, geen *Samengevat*; toy zonder opzet-tabel, stappen en tabel hand/code (print-regels); twee simulaties, waarvan de eerste (fixed-point, r. 711) een numerieke oplossing is; celparen zonder tekst ertussen (r. 851/874).
4. *Notatie*: $R^f$ is hier bruto (r. 177–184, 293, 465, 514), de boeknotatie ([](#00-00-setup)) heeft $R^f$ netto en $1+R^f$ bruto. $\lambda$ is leverage én prijs van risico $\lambda_{\Delta c}$. De Euler-fout heet $u_{i,t+1}$, net als de nutsfunctie. $x_t$ is in de AR(1) de toestand, in de rest de payoff.
5. *Replicatie en oefeningen*: blok ≈ 310 woorden; de getallen van Hansen en Singleton staan in proza (r. 1065–1085, 1094–1099) zonder tabel origineel/hier en zonder oordeel "Geslaagd"; "$p < 10^{-5}$" (r. 1090) en "bijna tien procent daalde" (r. 1377) staan in geen cel; oefening 1 is geen instap; geen uitwerking eindigt met "Wat dit leert:".

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `03-12-consumptie-capm` (14 lectures), `thm-consumptie-capm-contractie` en `thm-consumptie-capm-beta` en `eq-consumptie-capm-lognormaal` (03_13), `eq-consumptie-capm-lognormaal` (05_27), `thm-consumptie-capm-gmm` met de optimale $\mathbf{W} = \mathbf{S}^{-1}$ (05_26). Inhoudelijk aangehaald: de toy-vergelijking $\mathrm{PD}_i = \sum_j \beta P_{ij} g_j^{1-\gamma}(1+\mathrm{PD}_j)$ (03_13 r. 152), "Hansen en Singleton: T-bill en aandelen niet tegelijk; aandelen alleen vragen $\gamma$ in de tientallen" (03_13 r. 26). Niet aangehaald: `fig-`/`cel-consumptie-capm-lucas`, `-mc`, `-excess`, `eq-consumptie-capm-contante-waarde`, `-momenten`, `-j`, `-excess`, `-cov`, `-ccapm`, alle `ex-consumptie-capm-*`.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Overzicht | "Dat laatste is de epistemische wending"-alinea, dubbel met geschiedenis | 90 | herhaling; theorie of feit in één zin |
| Intuïtie | eiland-opzet en "Het slimme"-alinea ingekort | 80 | beeld blijft, uitweiding weg |
| Theorie, opzet | Lucas' $p(y)$-notatie, prijzen ex dividend | 30 | niet gebruikt |
| Theorie, Williams | Grossman-Shiller perfect-foresight en NBER-werkversie | 120 | geschiedenis zonder rol in de vraag |
| Theorie, evenwicht | Lucas' $u'(y)p(y)$-opmerking, warning AR(1)-rooster, "Deel V" | 150 | nevenzaak; vervalt met de AR(1) |
| Theorie, contractie | bewijs (dropdown) ingekort | 80 | stelling blijft (03_13), bewijs korter |
| Theorie, CCAPM | note Rubinstein (opties, autocorrelatie), mimicking-portfolio-zin | 120 | niet aangehaald; Rubinstein naar geschiedenis |
| Theorie, GMM | bewijs (dropdown) ingekort, "In de praktijk"-alinea ingekort | 110 | stelling blijft (05_26) |
| Simulatie | fixed-point op AR(1)-rooster, cel en figuur | 290 | numerieke oplossing, tweede vraag; richting-resultaat zit al in toy en oefening 1 |
| Simulatie, GMM | drie-dingen-alinea's naar tabel plus oordeel | 110 | getallen in proza |
| Replicatie | blok naar ≤ 250 | 70 | te lang |
| Replicatie | Hansen-Singleton-getallen uit proza naar tabel | 170 | getallen in proza |
| Replicatie | exact geïdentificeerd systeem ingekort | 100 | dubbel met tabel |
| Wat er brak | slotalinea theorie of feit korter, elk element ≤ 120 | 80 | te lang |
| Oefeningen | ex-1 deel 3 (spectraalstraal-uitweiding) ingekort | 90 | nevenresultaat |
| **totaal** | | **≈ 1.620** | |

**Verwachte lengte.** 5.822 − 1.620 ≈ 4.200; erbij komen vraag-antwoord en lijst, voorspelling aan het eind van *Intuïtie*, toy-stappen, routekaart, *Samengevat*, zinnen rond cellen, twee tabellen origineel/hier met oordeel, een instap in oefening 1 en "Wat dit leert" (≈ 650). Verwacht 4.800 tot 5.100. Geen splitsing.

## F1

**Eindmeting.** `words 4816  sent_mean 14.0  sent_p90 22  sent_gt40 0  para_mean 42  dash 0  semicol 15  motief 0  deel 0  u_form 0  je_form 0  taboo 0  stopw 1  calque 0  engquote 0` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1`: foutloos, geen warnings in de uitvoer.

**Geschrapt.** Epistemische-wending-alinea (herhaling, nu één zin theorie of feit); Grossman-Shiller perfect-foresight en NBER-werkversie (geschiedenis zonder rol); Lucas' $p(y)$ en $u'(y)p(y)$ (niet gebruikt); fixed-point op het AR(1)-rooster met cel, figuur en warning (numerieke oplossing, tweede simulatievraag; richting-resultaat zit in toy en oefening 1; `SargentStachurski` niet meer geciteerd); note Rubinstein (Rubinstein staat in de geschiedenisalinea); mimicking-portfolio-zin en drie keer "Deel V" (vooruitverwijzing); bewijzen van contractie en GMM ingekort; HS-getallen uit proza naar tabel; oefening 1 zonder $\delta$ en spectraalstraal (nevenresultaat).

**Toegevoegd.** Vraag-antwoord en lijst in *Overzicht*; drie voorspellingen aan het eind van *Intuïtie* (H12), ingelost bij de lognormale boom en het consumptie-CAPM; toy met opzet-tabel, vier stappen (incl. premie met de hand, 1,38 en 1,23 bp) en tabel hand/code; routekaart; lees-zin bij elke vergelijking; toy-$\delta = 0{,}9654$ in de theorie en de toy-premie in de simulatie (H11); *Samengevat*; tabel origineel/hier met oordeel "Geslaagd"; "Wat dit leert:" bij elke uitwerking.

**Notatie.** $R^f$ is nu netto zoals in [](#00-00-setup): $1+R^f = 1/\E[m]$, $R^e = R - (1+R^f)$, ook in `eq-consumptie-capm-cov`, `-lognormaal` en `-excess`. Leverage heet $\phi$ (was $\lambda$, botste met $\lambda_{\Delta c}$). Euler-fout heet $e_{i,t+1}$ (was $u$), overig inkomen $y_t$. Logrendement in oefening 2 is $\ell^m$.

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- toy: printregels en kolommen $E[R^m]$, $E[m R^f]$ → tabel hand/code; rente netto (0,0922 en 0,0293 i.p.v. 1,0922 en 1,0293); PD en premie (1,3808 en 1,2295 bp) gelijk.
- oude cellen 4 en 5 (AR(1)-oplossing, PD 16,684179, figuur) verdwenen.
- simulatie-economie: prints → Series; rente netto 0,0859 (was 1,0859); premie 0,0148 (was 1,4809%); SD 0,1607, controles 1,0000 en 1,0002 gelijk. Parameters in een dict; volgorde van `rng`-trekkingen ongewijzigd.
- Monte-Carlo-tabel herschikt tot één kolom; alle waarden identiek (2,811; −2,865; 11,927; 4,235; 1,513; 0,286; 0,098).
- replicatie: kolom `df` heet `vrijheidsgraden`; schattingen identiek. De $\gamma$-nulpunten (75,2; NaN) nu in een eigen cel vóór de figuur. Nieuw: tabel origineel/hier.
- oefening 1: kolommen $\delta$ en spectraalstraal weg, $\mathrm{PD}_h - \mathrm{PD}_l$ identiek (nu als matrix $\gamma \times \pi$).
- oefening 2: prints → Series, erbij gemiddeld excess rendement 0,01586 en SD 0,16072 (voor het "1,6%" en "16%" in de tekst); rest identiek. Oefening 3 identiek.

**Afvinklijst §11.9, wat niet voldoet.** Na de imports-cel volgt direct de opzet, zonder eigen zin erna (zoals in de template). Overige: ok.

**Labels.** Verdwenen: `cel-consumptie-capm-lucas` en `fig-consumptie-capm-lucas`, nergens aangehaald. Alle andere labels ongewijzigd; alle cross-refs in de lecture bestaan.

**Open punten.**
1. Naad met 03_13 (r. 419–425) en 05_27 (r. 628): zij halen `eq-consumptie-capm-lognormaal` aan; die schrijft nu $\log(1+R^f)$ en hefboom $\phi$. 03_13 schrijft zelf $\log R^f$ (bruto) en praat over "leverage één". Controleren bij hun herziening.
2. HS-getallen (tabel 4, 1, 5; pagina's) komen uit de vorige versie van de tekst; F2 moet ze tegen de bron houden. Het erratum `HansenSingleton1984` wordt niet meer geciteerd.
3. De tabel origineel/hier vergelijkt hun maanddata met onze kwartaaldata 1959–1978; rij (c) origineel heeft geen $\hat\gamma$ in de tekst van de vorige versie.

## F4

**Meting.** `words 4939  sent_mean 13.9  sent_p90 22  sent_gt40 0  para_mean 42  dash 0  semicol 15  stopw 0  calque 0  engquote 0` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings; `nb_outputs` identiek aan F1. Labelset ongewijzigd; alle cross-refs bestaan.

**Feitenlijst.** Niet herleidbaar (tabel-, pagina- en NLAG-aanduidingen zonder eigen cite): de zin draagt nu zelf {cite:t}`HansenSingleton1983`. Rij (c) zonder $\hat\gamma$: de tekst zegt nu dat we voor (c) alleen de toets overnemen.

**Lezerspunten.**
1. Opgelost: de exacte covariantierelatie staat nu als stap vóór de stelling; `thm-consumptie-capm-beta` bevat alleen de consumptiebèta (03_13 haalt die zo aan).
2. Afgewezen: `eq-consumptie-capm-lognormaal` wordt door 03_13 (rente, premie) en 05_27 (PD) als één blok aangehaald; splitsen breekt die verwijzingen. De propositie is één uitspraak: de gesloten vorm van de lognormale boom.
3. Opgelost: $J$-toets is een `prf:corollary` na [](#thm-consumptie-capm-gmm); `eq-consumptie-capm-j` blijft.
4. Opgelost: één alinea onderscheidt SDF (gemeenschappelijk) en discontovoet (per activum).
5. Opgelost: voorbeeld $\hat\alpha = -0{,}931$ ↔ $\hat\gamma = 0{,}931$.
6. Opgelost: zin bij de code legt de twee kolommen van `D` uit ($-\log g$ is de afgeleide naar $\gamma$).
7. Opgelost: rente met de simulatieparameters met de hand: $0{,}0202 + 0{,}0720 - 0{,}0098 = 0{,}0824$, 8,6% (gelijk aan de cel).
8. Opgelost: één zin waarom $\gamma = 4$ en $\beta = 0{,}98$.
9. Opgelost: overgangszin $Q(s,\cdot)$ = rij van $P$, integraal = som.
10. Opgelost: hedge-motief uitgelegd met een voorbeeld (activum dat goed rendeert als de rente daalt).
11. Opgelost: "zoals de rente" als toestandsvariabele. 12. Afgewezen: Chicago en Yale zijn de vaste namen van het motief; bronnen voor beide kampen komen in 03_13 en later, en nieuwe citaties zouden bib-keys of vooruitverwijzingen vragen. 13. Opgelost: leeswijzer vóór de simulatiefiguur. 14. Opgelost: expliciete terugverwijzing naar de eerste voorspelling. 15. Opgelost: "Ten derde"-zin herschreven.

**Betaald met schrappen.** Dubbele zin "De stelling vraagt geen verdeling ..." (GMM), "$\hat\beta > 1$"-zin in de simulatie (staat in de tabel), Lucas-vraag-zinnen in *Intuïtie*, slot theorie of feit ingekort. Netto +123 woorden.

**Navertel-toets.** Geen sectie week af van de bedoeling; niets veranderd op grond daarvan.

## F5-1

**Meting.** `words 5240  sent_mean 13.9  sent_gt40 0  para_mean 43  semicol 11  calque 0` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings. `nb_outputs` t.o.v. F4: alleen de handkolom van de toy-premie (1,4 en 1,2 in plaats van 1,38 en 1,23), cel 3 zonder TODO en de simulatietabel (rij hernoemd, waarheid NaN, nieuwe rij 95e percentiel van $J$: 9,488 tegen 11,737). Alle andere getallen identiek; `einsum` geeft dezelfde momenten. Labels ongewijzigd, alle cross-refs bestaan.

**Feitelijke fouten.** (1) Gedaan: "0,25%" → $4 \cdot 0{,}035^2 = 0{,}49\%$. (2) Gedaan: "onderkant van dat interval" vervangen door "het interval rond hun 58 sluit niets uit; wat overblijft is een onaannemelijk grote puntschatting". (3) Gedaan: de rente stijgt met $\gamma$ zolang $\gamma < \mu/\sigma^2 \approx 14{,}7$. Twijfelachtig punt: "kozen daarom maanddata" → "maanddata verkleinen dat probleem".

**Helderheid.** Gedaan: dubbele $\beta$ gemeld in de stelling consumptiebèta en simulatierij "discontofactor-dak"; $\otimes$ in woorden met $N = 2$, $L = 3$, zes momenten; $K$ (aantal parameters) en $\mathbf{S}$ (langetermijncovariantie) benoemd; kritieke waarde 9,49 uit de cel in de simulatie (niet bij de vergelijking, want daar staat geen cel); mediaan 2,8 (scheef) en 29% $\hat\beta > 1$ geduid en gekoppeld aan de 1,08 van de replicatie.

**Opbouw.** Gedaan: `eq-consumptie-capm-excess` staat nu in de theorie bij de covariantiestap; de replicatie verwijst ernaar. Williams en Evenwicht beginnen met één zin over hun functie voor de vraag.

**Taal.** Gedaan: "is het het", losse regel "Dit werk", Chicago en Yale met bijzin, puntkomma's in routekaart, kernresultaat, Vergelijking met 1983, Wat er daarna kwam en Intuïtie gesplitst.

**Toy.** Gedaan: stap 2 via de regel van Cramer in plaats van de substitutie; stap 4 met vijf decimalen (1,09235 tegen 1,09221, ongeveer 1,4 bp), zonder tweede niet-afgeleide formule (STYLE §11.7); slotzin "Wat het toy-voorbeeld laat zien".

**Code.** Gedaan: TODO weg; Kronecker-stap als `einsum("tn,tl->tnl")` met commentaar; rooster plus verfijning in één zin; rij $\hat\beta > 1$ geduid.

**Replicatie.** Gedaan: getallen uit "De data" en "De schattingen" naar de tabel; oordeel met de vijf keer grotere SE bij (a) (kwartaal- en één vertraging tegen maand- en twee) en het teken van (b) (niet van nul te onderscheiden); "geen enkele $\gamma$" → "geen $\gamma$ onder 300".

**Afgewezen.** Geen.

## F5-2

Drie punten uit Controle 1, verder niets gewijzigd. (1) "klein en precies" → "klein en nauwkeurig geschat" (De schattingen). (2) "daar hier" → "hier" (Vergelijking met 1983). (3) Standaardfouten gescheiden: onze 6,2, die van Hansen en Singleton 1,57 bij een schatting van 1,51; geen van beide van nul te onderscheiden.
Meting: `words 5247`, `prose_stats --check` PASS; sync en `--execute` met `HAP_OFFLINE=1` foutloos; `nb_outputs` identiek aan F5-1.

## F6-1

**Meting.** `words 5249`, `prose_stats --check` PASS (semicol 13). Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings. Labels ongewijzigd, alle cross-refs bestaan.

**1. Toy handrekenbaar.** Gedaan: $g_l = 0{,}98 \to 0{,}96$ (rest gelijk). Gewichten 9/13, 1/4, 3/13, 3/4; stelsel oplosbaar door optellen ($y_h = 26$, $y_l = 28$), geen Cramer, noemers ≤ 27. Nieuwe toy-getallen, proza en cel gelijk: PD 25 en 27 (was 19,3125 en 20,4375), rente 7,98% en −0,31% (was 9,22% en 2,93%), premie 2,0 en 1,7 bp (code 1,9967 en 1,7068; was 1,38 en 1,23), renteverschil "ruim acht" (was "ruim zes") procentpunt, schommeling 4% (was 3%), $\delta = 0{,}9808$ (was 0,9654). Elders in het boek worden geen toy-getallen aangehaald (grep).
Oefening 1 volgt het toy ($g_l = 0{,}96$). $\gamma$-rooster $\{0{,}5; 1; 2; 3\}$ i.p.v. $\{…; 4\}$: bij $\gamma = 4$, $\pi = 0{,}9$ heeft het nieuwe stelsel geen positieve oplossing (spectraalstraal 1,014). Tabel verandert, conclusie in de uitwerking ongewijzigd.

**2. Replicatie na het oordeel.** Gedaan: 6,2 / 1,57 / 1,51 / 67 / 58 uit de proza; de tekst verwijst naar de kolommen met standaardfouten en naar rij (d).

**3. Losse eindzin en brug.** Gedaan: de zin theorie of feit staat nu in "Wat er daarna kwam", vóór Mehra-Prescott en de cross-ref. In de simulatie is "of op ruim één basispunt zoals in het toy-voorbeeld" geschrapt.

**Naadpunt 4.** Gedaan: bijzin bij $\gamma < \mu/\sigma^2$: 14,7 bij 1,8%/3,5%, 13,8 met de momenten van {cite:t}`Mehra2003` in 03_13 (bestaande key; tweede vooruitverwijzing, binnen de grens van twee). Naadpunten 7, 10, 11: niet gewijzigd (projectkeuze).

**`nb_outputs`-diff t.o.v. F5-2.** Alleen de toy-cel (bovenstaande waarden) en oefening 1 (nieuwe $g_l$ en $\gamma = 3$). Simulatie, replicatie, oefening 2 en 3 identiek.

## F6-2

**Meting.** `words 5211`, PASS; sync en `--execute` met `HAP_OFFLINE=1` foutloos; `nb_outputs` identiek aan F6-1 op de celnummering na (datacel gesplitst). Labels en cross-refs ongewijzigd.
(1) Vooruitverwijzing weg: alleen 14,7 bij 1,8%/3,5%, "een andere kalibratie geeft een andere drempel"; geen L13, geen 13,8, `Mehra2003` niet meer geciteerd.
Helderheid: GMM-alinea teruggebracht tot twee zinnen, details (β geconcentreerd, rooster plus verfijning, kolommen van `D`) als commentaar in de code; zin over "probability" vervangen door toelichting bij rij (d) (nulpunt, geen SE); hefboom: "met hefboom drie drie keer zo groot" zonder toy-vergelijking.
Opbouw: theorie-of-feit-zin sluit nu "Waar het breekt" af; kop "De discontovoet krijgt een theorie" opent met de bewering.
Taal: vergelijkingszin simulatie/replicatie in twee zinnen; consumptie-CAPM eerst, Engelse term tussen haakjes; Chicago- en Yale-zin gesplitst.
Code: Kronecker-stapeling als lus over activa met benoemde blokken; generator in `concentrated` uitgeschreven; `brentq`-conditie als if/else; datacel gesplitst in bouwen en samenvatten, met zin ervoor en erna.

## R9-1 (F6b, ronde 9+)

**Feitelijke fouten.** (1) "gewogen gemiddelde" wordt "gewogen som", met een zin dat gewichten die per toestand onder één blijven (toy: hoogstens 0,98) $T$ tot contractie maken. (2) $\delta < 1$ heet nu voldoende maar niet nodig; oneindig pas als het nut-gewogen dividend langs de keten te snel groeit. (3) Admonition: "nul tot zes lags". (4) "Waar het breekt": een kleine steekproef verklaart $J = 42$ niet (95e percentiel 11,7 bij vier tegen zes vrijheidsgraden); tijdsaggregatie maakt $J$ groter maar verklaart de $\gamma$ in de tientallen niet; "zeldzaam en zwak" geschrapt.
**Helderheid.** Nut van Hansen en Singleton als $c^{1+\alpha}/(1+\alpha)$, geen tweede $\gamma$. $R^m$ vóór de propositie benoemd als rendement op de boom (subscript = markt, niet de SDF). Rente: "lineair tegen kwadratisch" als reden voor de drempel; reparatiebijzin "andere kalibratie" geschrapt en de kalibratiezin ingekort.
**Taal.** Drie hardop-zinnen herschreven (Overzicht, celaankondiging toy, consumptiebèta). SDF-definitie in twee zinnen zonder dubbele punt. "leverage" geschrapt. Eén term "lag(s)" (STYLE §3 geeft "lags"; "vertraging" in oefening 3 wordt "lag"). "op vier decimalen nul" vijf keer vervangen door $J$-waarden of $p < 0{,}0001$. Link bij de tweede "standaardfout van 2%". Lucas-boom-opener gaat over de boom. Overzicht-opsomming als vijf volzinnen.
**Toy.** Stap 3 en 4 houden de redenering; uitkomsten per toestand in een tabel ($\E_i[m]$, $R^f_i$, $\E_i[R]$, $1+R^f_i$, premie). Eerste zin na de celtabel zegt wat die bewijst (Euler-vergelijking gehaald).
**Opbouw / figuren.** Drievoudige uitleg teruggebracht: zin vóór elke figuur zegt alleen wat erin staat; bijschrift figuur 2 herhaalt de snijpunten niet meer; slotzin simulatie wijst naar $J$ boven 11,7.
**Replicatie.** Verwachte afwijking noemt nu tijdsaggregatie (kleinere SE, grotere $J$).
**Code.** Kolom "verwerpt origineel" met decimale komma (30,08; 10,93; 366,22); opnieuw uitgevoerd, alleen die labels verschillen.
**Afgewezen.** Geen.
Woorden: 5.612 (was 5.469). prose_stats PASS; nb_numbers 18 meldingen (was 22), geen nieuwe.
