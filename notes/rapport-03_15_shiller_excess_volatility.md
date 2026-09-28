STATUS 03_15_shiller_excess_volatility F6b words=5425 prose=PASS open=0 cijfer=- min=-

# Rapport 03_15_shiller_excess_volatility (workflow-herziening)

## F0

**Nulmeting.** `words 4627  sent_mean 19.0  sent_p90 32  sent_gt40 10  para_mean 57  dash 0  semicol 21  motief 3  je_form 11  stopw 10  calque 2  engquote 14` → FAIL op alles behalve words. `--where`: r. 53 "epistemisch", r. 292 "Twee dingen". Lengte is niet het probleem; taal, structuur en notatie wel.

**Vijf grootste problemen.**
1. *Taal*, overal: 10 zinnen boven 40 woorden, alinea's van 57, 21 puntkomma's, 11 keer "je" (Intuïtie r. 87, Theorie r. 245, 285, 470, Wat er brak r. 934), "Het punt is" (r. 376), 14 lange aanhalingen, Engelse citaten midden in de zin (Flavin r. 371, "five to thirteen" r. 323, "puzzling results" r. 500).
2. *Structuur*: imports-cel in Overzicht (r. 69); Overzicht zonder vraag-antwoord en lijst; Intuïtie zonder voorspelling (H12); geen routekaart, geen Samengevat; bewijs van de variantiegrens (12 regels) open; stelling en propositie met twee of vier beweringen (H3); acht `###`.
3. *Notatie*: $\gamma$ als discontofactor (setup: risicoaversie), $\lambda$ als trendfactor en als vertragingsgewicht (setup: prijs van risico), hoofdletters $P_t, D_t$ voor niveaus, $r_{t+1}$ als log-rendement (setup: $\ell$), log-aankondiging "in deze subsectie"; "2%-motief" (r. 377, 876) en "epistemische status" (r. 53); "standaardfout" zonder link naar `#00-01-rendementen`.
4. *Toy en replicatie*: toy eindigt met print-regels, niet met tabel hand/code; hard gecodeerde prijs B langs het pad; replicatieblok ≈ 260 woorden met onderdelen van drie zinnen; geen oordeel "Geslaagd / Gedeeltelijk / Niet geslaagd" onder de tabel origineel/hier en onder de gevoeligheidstabel.
5. *Feiten en cellen*: "in een aparte proef ... boven de 90%" (r. 644) komt uit geen cel; "Met 75 jaar" (r. 1046) is 76 jaar; simulatiecel (36 regels) en gevoeligheidscel (43 regels) te lang, rekenwerk in een verborgen plotcel (r. 767–774); "Waar we zijn" verwijst naar vier lectures.

**Eis 2 (grep in `lectures/`).** Elders aangehaald: `03-15-shiller-excess-volatility` (03_14, 03_16, 04_20, 04_23, 05_33, 06_36, 08_39) en `eq-shiller-excess-volatility-decompositie` (04_20 r. 337). 04_20 r. 304 zegt dat Williams' PD-vergelijking hier "als variantiegrens diende": blijft waar. Andere labels niet aangehaald; alle labels blijven toch bestaan.

**Schraplijst (eis 1 vraag, 2 aangehaald, 3 motief).**

| kopje | passage | ≈ woorden | haalt geen eis omdat |
|---|---|---|---|
| Waar we zijn | consumptiemodellen 03-12/03-13 | 30 | derde en vierde verwijzing; niet nodig voor de vraag |
| Overzicht | slotalinea in proza (toy, kritieken, simulatie, replicatie) | 110 | wordt de lijst |
| Theorie, grens | "Meetkundig ... projectie" | 30 | tweede beeld van hetzelfde argument |
| Theorie, grens | "Twee dingen staan er niet in" (normaliteit, kurtosis) | 75 | nevenresultaat; stationariteit staat al in Intuïtie en Kleidon |
| Theorie, eindwaarde | Gordon-eindwaarden uit de Nobellezing (5,1%, 1292, 669) | 60 | nevenresultaat, getallen uit geen cel |
| Theorie, Kleidon | propositie-items 1, 2 en 4 als losse beweringen | 60 | H3; blijven als bewijsstappen in dropdown |
| Theorie, Marsh-Merton | eigen `###`, "niet volledig kunnen inzien" | 70 | drie zinnen in de Kleidon-subsectie volstaan |
| Theorie, logs | gecointegreerde VAR, "puzzling results" | 30 | citaat; parafrase in één bijzin |
| Simulatie | "aparte proef ... boven de 90%" | 35 | uit geen cel |
| Replicatie | blok van ≈ 260 naar ≈ 210 | 50 | blok > 250, onderdelen > 2 zinnen |
| Wat er brak | Risico of vergissing van ≈ 210 naar ≈ 120; herhaalde getallen | 90 | elk element ≤ 120 woorden |
| **totaal** | | **≈ 640** | |

**Verwachte lengte.** 4.627 − 640 ≈ 3.990; erbij komen vraag-antwoord en lijst, H12-voorspelling, routekaart, *Samengevat*, notatiezin, lees-zinnen, zinnen rond gesplitste cellen, twee oordelen en "Wat dit leert" (≈ 650). Verwacht 4.550 tot 4.750. Geen splitsing.

## F1

**Eindmeting.** `words 5173  sent_mean 15.3  sent_p90 23  sent_gt40 0  para_mean 40  dash 0  semicol 2  motief 0  je_form 0  stopw 0  calque 0  engquote 1` → PASS. `--where`: geen treffers. Sync en `--execute` met `HAP_OFFLINE=1` foutloos, geen warnings in de uitvoer. Lengte hoger dan het F0-plan (4.550–4.750): de H12-lijst, de stappenlijst van het toy en de zinnen rond zes gesplitste cellen kostten meer dan geschat; binnen het doel van 5.300.

**Geschrapt.** Consumptiemodellen in *Waar we zijn* (derde/vierde verwijzing); Overzicht-slotalinea (wordt lijst); projectie-beeld en "Twee dingen staan er niet in" (nevenresultaat); Gordon-eindwaarden 5,1%/1292/669 (uit geen cel); Marsh-Merton als eigen `###` en de zin "niet volledig kunnen inzien" (drie zinnen in de Kleidon-subsectie); propositie-items 1, 2, 4 als beweringen (nu bewijsstappen); "aparte proef ... boven de 90%" (uit geen cel); Santa-Clara-zin in *Risico of vergissing* (geen strategie-lecture; element ≤ 120 woorden); Engelse citaten Flavin, "five to thirteen", "puzzling results" (geparafraseerd).

**Toegevoegd.** Vraag-antwoord en lijst; *theorie of feit* als eigen alinea; H12-voorspelling (drie punten) aan eind van *Intuïtie*, ingelost in de variantiegrens en de decompositie; toy als opzet-tabel, recept, zes stappen, hulpfunctie-cel, toy-cel met tabel hand/code; routekaart; conclusiezin vooraan elke `###`; lees-zin bij elke genummerde vergelijking; bewijsidee in de hoofdtekst, beide bewijzen in dropdown met stapkoppen; H4/H6 bij Kleidon ($\sqrt{1+2/r}$: 6,5 bij 4,8%, 4,6 bij 10%); *Samengevat*; oordelen **Geslaagd** onder beide replicatietabellen; knoppen als lijst; "Wat dit leert:" bij elke uitwerking.

**Notatie.** $\gamma \to \delta = 1/(1+r)$ (één zin vertaling Shiller; $\gamma$ is risicoaversie); Kleidon-ratio herschreven als $\sqrt{1+2/r}$ (algebraïsch gelijk, zelfde getallen); $\lambda$ weg (trend $e^{b(t-T)}$, Marsh-Merton zonder symbool); niveaus in kleine letters, logs aangekondigd met "Vanaf hier zijn kleine letters logs", log-rendement $\ell_{t+1}$; beide "standaardfout van 2%" linken naar `#00-01-rendementen` en zeggen wat het motief hier betekent.

**`nb_outputs`-diff (voor → na), elk verschil bedoeld.**
- toy: print-regels → tabel "met de hand / code" (zelfde waarden; prijs B langs het pad nu berekend, niet hard gecodeerd); hulpfunctie in eigen cel.
- simulatiecel gesplitst in (a), (b)+(c), toets+tabel; `rng`-volgorde gelijk, tabel identiek (1,000 / 0,000 / 0,198; mediaan 2,629; 95e pct 4,042).
- ensemble-controle identiek (`gamma_sim` → `delta_sim`).
- replicatie: index "b = ln lambda" → "trendgroei b"; figuurcel gesplitst in rekencel en plotcel (legenda "koers $p$", png 16 bytes groter); gevoeligheidscel gesplitst (SE-print 0,0143 nu in eigen cel), tabel identiek.
- oefeningen identiek (formule als $\sqrt{1+2/r}$: 10,05 / 6,53 / 4,58; sim 6,54).

**Afvinklijst §11.9, wat niet voldoet.** Theorie heeft zeven `###` (drie kritieken apart). Overige: ok.

**Labels.** Alle labels van HEAD bestaan nog (comm leeg); geen nieuwe. Inline verwijzingen naar oefeningen: geen.

**Open punten voor F2.**
1. De deflator-verklaring voor 3,93 tegen 5,59 (WPI beweeglijker dan CPI) is niet met een cel onderbouwd; `hap` heeft geen WPI-reeks.
2. Beweringen uit Marsh en Merton (1986) en Kleidon (1986) steunen op secundaire samenvattingen; F2 graag tegen de bib/abstracts controleren.
3. "Shiller liet in zijn Nobellezing zien dat die keuze vóór 1980 nauwelijks doorwerkt" en "de benodigde discontovoet beweegt wild op momenten dat geen gemeten rente beweegt" (Shiller 2014) zijn parafrases zonder paginanummer.

## F4

**Meting.** `words 5283  sent_mean 15.4  sent_p90 23  sent_gt40 0  para_mean 41  semicol 3  stopw 1  engquote 1` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos; `nb_outputs` identiek aan F1 (zelfde bedoelde diff tegen HEAD, geen getal veranderd). Labels ongewijzigd.

**Feiten (F2, open=2).** Jaartal 1979–1988 → 1981–1988 (Shiller/LeRoy-Porter 1981 tot Campbell-Shiller/West 1988). Deflator: "komt grotendeels door" → "kan aan de deflator liggen ... met de data hier niet na te gaan".

**Lezerspunten.**
1. gedaan: in de Simulatie staat nu dat (a) hetzelfde mechanisme heeft, maar geometrisch met drift en op gedetrendeerde niveaus is, dus mediaan 2,6 onder $\sqrt{1+2/0{,}07} = 5{,}4$.
2. gedaan: "de helling" herhaald (PD voorspelde tienjaarsrendement, niet dividendgroei).
3. gedaan: regeleinde tussen (b) en (c).
4. gedaan: tussenstap bij de decompositie (links $\Var(pd_t)$, constante valt weg, sommen worden covarianties).
5. afgewezen: de H12-inlossing staat al in de conclusiezin vooraan de Kleidon-subsectie; een tweede zin is herhaling.
6. gedaan: richting toegevoegd aan beide *Waarom*-alinea's (eindwaarde: ratio daalt; logs: verhouding blijft gelijk).
7. gedaan: $p_t = d_t/r$ uit de propositie (staat in bewijsstap 1 en bewijsidee).
8. gedaan: één zin waarom de simulatie andere getallen dan het toy gebruikt (koppeling via stap 4 en 6 bestond al).
9. gedaan: premie gekoppeld aan [](#03-13-equity-premium-puzzle).
10. gedaan: herkomst van $\sigma(d)/\sqrt{2\bar r}$ in één zin (maximum over informatiestructuren).
11. gedaan: transversaliteit met getal ($\delta^{100}$ < 1%). 12 gedaan: Samengevat geeft beide richtingen. 13 gedaan: bewering vooraan in de eindwaarde-subsectie. 14 gedaan: "dat dat" → "die volgorde". 15 afgewezen: correlatie is een diagnose in de replicatie, geen stap in het argument; kost woorden zonder dat de vraag ervan afhangt.

**Betaald met schrappen.** De `{warning}` over de eindwaarde van $pd^*$ (≈ 60 woorden): herhaalt het eindwaardepunt uit de Theorie en de gevoeligheidstabel.

**Navertel-toets.** Geen sectie wijkt inhoudelijk af. Het Overzicht las de lezer als "de factor is grotendeels een artefact": dat klopt met de bedoeling ("hangt sterk af van keuzes"), dus niets veranderd.

## F6-1

**Meting.** `words 5425  sent_mean 15.5  sent_p90 23  sent_gt40 0  semicol 2  stopw 1` → PASS. Sync en `--execute` met `HAP_OFFLINE=1` foutloos. `nb_outputs`: alle aangehaalde getallen gelijk; verschillen alleen in presentatie (toy-tabel op 2 decimalen, Nederlandse overzichtstabel i.p.v. `describe()`, kolomnamen "5e/95e percentiel", tabel origineel/hier met rij 1928–1979 (9,83 tegen Dows 13,28) en kolom "verwachting", `ex_post_price` naar de Simulatie). Labels ongewijzigd.

**Feitelijke fouten.** Geen gemeld. De twee twijfelgevallen zijn verholpen: Kleidon 6,5 tegen 5,59 (zie 2); "volgt de koers slecht (0,59)" → "maar matig" / "maar deels samen" (Wat er brak, gevoeligheid, bijschrift).

**Drie verbeteringen.**
1. Code, gedaan: `shiller_test` met benoemde stappen, OLS-trend via `np.polyfit` in een lus, correlatie in een lus, if/else in plaats van inline-conditionals; simulatie- en gevoeligheidstabel via een lus; `describe()` → Nederlandse tabel; `sliding_window_view` → zichtbare lus over de 400 termen; zin vóór de imports-cel.
2. Helderheid, gedaan: bij Kleidon "verhouding van *veranderingen*, Shillers 5,59 van gedetrendeerde *niveaus*"; $\sigma(d)/\sqrt{2\bar r}$ in woorden gelezen. Campbell-Shiller 1987 en West 1988 kregen een concreet resultaat, geen getal: een getal dat niet in de bib of een cel staat, zou STYLE §11.11 (Feiten) schenden.
3. Replicatie, gedaan: 1928–1979 naast Shillers Dow in de tabel origineel/hier, rangorde als verwachting in het replicatieblok, oordeel zonder getallen in de tekst.

**Overige punten.**
- Gedaan: "knoppen" → "keuzes met het grootste effect"; "definieert" → "bepaalde"; Flavin in *Samengevat*; tabel in "Wat Shiller mat" weg (definitie en één getal, de rest in de replicatie); toy één cel (stap 1 met de hand in de cel, `ex_post_price` naar de Simulatie); hand- en codekolom op 2 decimalen; oefening 2 kreeg een afleidingsdeel (ondergrens van LeRoy en Porter) in plaats van de uitlegvraag; effectieve discontovoet in niveaus (8,6%) bij de simulatie genoemd.
- Afgewezen: twee mechanismen in het toy. Stap 6 is het toy-anker voor de kritiek van Kleidon (STYLE §11.10 H11) en draagt de kern "de grens gaat over toestanden, de meting over de tijd". Zeven `###` blijven, omdat elke kritiek een eigen *Waarom* heeft (STYLE §1: subkopjes zijn vrij).
