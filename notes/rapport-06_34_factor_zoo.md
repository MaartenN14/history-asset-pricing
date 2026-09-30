STATUS 06_34_factor_zoo F4T words=5887 prose=PASS open=0 cijfer=- min=-

# Rapport 06_34_factor_zoo (L34)

**Kern.** Hoeveel van de honderden gepubliceerde voorspellers zijn echt, en waarom verzwakken ze? De meeste doorstaan een strengere drempel en zijn te repliceren, maar ze verliezen na publicatie meer dan de helft van hun rendement, veel meer dan publicatieselectie verklaart.

## F0

prose_stats vóór: `words=5686 sent_mean=20.2 sent_p90=37 sent_gt40=19 para_mean=59 semicol=40 motief=7 calque=4 engquote=27 colon_mid=9.7 para_one=15 tmpl=6` → FAIL op 10 drempels (niet op words).

Vijf grootste problemen:
1. Overzicht: geen vraag-en-antwoord, geen lijst, "Deze lecture definieert het tijdvak", "motief 3", "epistemische status"; imports-cel aan het eind (r.49–62).
2. Engelse citaten midden in zinnen (27×), vooral Overzicht, Intuïtie, Theorie (HLZ, MP, FGX, NMV), Replicatie, Wat er brak.
3. Twee mechanismen in het toy (meervoudig toetsen + shrinkage) en twee simulaties (nulveld en EB-universa); geen hand/code-tabel.
4. Theorie: geen routekaart, geen Samengevat, 6× "*Waarom zou dit waar zijn?*", 4 stellingen met open bewijs (Holm, truncatie, shrinkage, q).
5. Replicatie: replicatieblok ~400 woorden, getallenalinea's zonder tabel origineel/hier, geen oordeel "Geslaagd/Gedeeltelijk"; "alfa" i.p.v. alpha, in-sample/out-of-sample in proza.

Schraplijst (eis 2: grep op alle labels van 06_34 in lectures/: alleen `06-34-factor-zoo` wordt elders aangehaald, geen enkel intern label):
| passage | kopje | ~woorden | eis niet gehaald |
|---|---|---|---|
| simulatie (b) EB-universa + figuur | Simulatie | −250 | 1, 2, 3 (tweede simulatie; EB komt op echte data terug) |
| bewijs BHY (dropdown) | Theorie | −170 | 1, 2 (vervangen door één zin bewijsidee) |
| FGX, Novy-Marx–Velikov, smart beta, Novy-Marx-citaat | Theorie | −120 | 1 (ingekort tot één alinea) |
| geschiedenisalinea en citaten Overzicht | Overzicht | −90 | 1 |
| replicatieblok | Replicatie | −150 | 1 (≤250 woorden) |
| getallenproza replicatie (1)–(4) | Replicatie | −100 | 1 (naar tabel) |
Verwacht: 5686 − 880 + ~500 (routekaart, Samengevat, lijst, instap-oefening, verbindingszinnen) ≈ 5.300.

## F1

Eindmeting: `words=5840 sent_mean=16.8 sent_p90=27 sent_gt40=1 para_mean=53 dash=0 semicol=0 motief=0 calque=0 engquote=1 colon_mid=0.7 para_one=6 tmpl=0 wie_open=0` → PASS. Doel 4.500–5.500 niet gehaald (5.840); F4 heeft 160 woorden ruimte tot 6.000.

Geschrapt of verplaatst:
- Simulatie (b) "Empirical Bayes herstelt de ware premies" met cellen en figuur `fig/cel-factor-zoo-eb` geschrapt: tweede simulatie (§11.7); `empirical_bayes` verhuisd naar replicatie (3).
- Shrinkage-toy (τ = 0,4%, t = 2,5) van Toy naar Theorie na de shrinkage-stelling (één mechanisme in het toy; toy-getallen keren terug, H11).
- BHY-bewijs vervangen door één zin bewijsidee; Holm- en q-bewijs naar dropdown (≤ 3 open bewijzen).
- FGX/Novy-Marx–Velikov/smart beta ingekort tot één alinea; Novy-Marx-citaat en HLZ/MP/FGX/NMV-citaten geparafraseerd.
- Wat er brak: Santa-Clara-motto als blokcitaat met Nederlandse inleiding.

Structuur: Overzicht vraag/antwoord + lijst + geschiedenis; imports-cel begint het toy; toy met stappenlijst en tabel "met de hand / code"; routekaart en Samengevat in Theorie; intuïtie voorspelt (toevalstreffer verliest alles, sterk signaal niets, tussenperiode < na publicatie), ingelost in de truncatie-subsectie en bijgesteld in replicatie (3); replicatie eindigt met tabel origineel/hier en oordeel "Gedeeltelijk geslaagd". Oefeningen: nieuwe instap ex-1 (toy met M = 20), oud 1→2, 2→3, 3→4. Verwijzingen naar oefeningen zijn tekst. Symbolen: aanpassingskosten q-model a→κ, marktwaarde M_t→V_t, interne rente r→k, steekproefdata τ^e/τ^p geschrapt (botsten met τ, a, M, r). Holm-code: cumprod-truc vervangen door zichtbare lus (zelfde uitkomst).

nb_outputs-diff (106+/104−): alleen presentatie. Toy-tabel vervangen door hand/code-tabel; "alfa"→"alpha" in kolomnamen; periode-index in-sample/oos/post → in de steekproef/tussenperiode/na publicatie (nulveld, periodetabel, MP-regressie, drempeltabel, oefening 3); kolom "t.o.v. in-sample"→"t.o.v. steekproef"; printregel "in-sample t"→"t in de steekproef"; EB-simulatietabel en -figuur weg; nieuwe cel oefening 1 (Bonferroni 3,023; Holm A; BH ABC). Figuur selectie 86140→85996 bytes (legendetekst). Geen aangehaald getal veranderd.

Afvinklijst §11.9, niet voldaan: lengte boven het doel van 5.500 (wel ≤ 6.000). Overige: ok.

Labels: verdwenen `cel-factor-zoo-eb`, `fig-factor-zoo-eb` (nergens aangehaald); nieuw `ex-factor-zoo-4`. Aangehaalde labels in 01/03/04/05/06 bestaan (grep); `thm-industrie-bh` veronderstelt onafhankelijkheid, klopt met de tekst; 03_16 r.545 verwijst naar dit college voor de systematische versie van datamining, "Waar we zijn" herhaalt dat argument in één zin.

Open punten voor de feitencontroleur:
1. HLZ-getallen (316 factoren, 313 artikelen, sinds 1967, Bonferroni 1,96→3,78 in 2012, BHY 5% 2,78, vuistregel 2,8) en JKP "13 thema's": alleen tegen de artikelen te controleren.
2. "De meeste portefeuilles zijn gelijkgewogen" (replicatie (4)) heeft geen cel; oude bewering "184 signalen gelijkgewogen" is geschrapt als niet herleidbaar.
3. Santa-Clara-blokcitaat en ICI 2019 (index = actief) letterlijk tegen {cite}`SantaClara2026`/{cite}`ICI2020` controleren.
4. Lengte 5.840: F4 moet elke toevoeging met schrappen betalen.

## F4

Feitenrijen (alle 11 opgelost):
- 1 (Toy): "$t$ van 2,2 of meer". 2, 3 (Replicatie shrinkage, Wat er brak): "voorspellen 7 tot 9%, tegen 40%" en "7 tot 9 van die 57 procentpunten". 4 (Oefening 4): "bijna de hele lengte sinds 1963". 5 (Oefening 3): 1925–1929, 1930–1934.
- 6 (Replicatie shrinkage): "zodat" weg. 7 (Theorie shrinkage): frequentistisch tegenover Bayesiaans. 8 (Theorie FF5): "op enkele na", winstgevendheid geschrapt. 9 (Replicatie alpha): vergelijking met ruw rendement geschrapt. 10: "Veel portefeuilles". 11 (Wat er brak): "verklaren een deel, al houden de meeste signalen een alpha".
Lezerspunten:
- 1, 2, 3, 6, 7, 8, 12: gedaan via feitenrijen 3, 4, 2, 1, 6, 11, 9.
- 4 (Replicatie shrinkage): 26% expliciet aan McLean en Pontiff gekoppeld, de 40% vergt nog zwakkere signalen; de drie verklaringen zijn nu een lijst.
- 5 (Theorie FF5): symbolen niet hernoemd (werkwijze: geen wiskunde wijzigen); in plaats daarvan één zin aan het begin van de FF5-subsectie dat $V_t$, $B_t$, $R_{t+1}$ hier marktwaarde, boekwaarde en bruto rendement zijn.
- 9 (Replicatie shrinkage): $\hat\mu_\delta = -7{,}4$, $\hat\omega = 6{,}1$ (cel 13) genoemd, met de reden waarom dat ongeloofwaardig is.
- 10 (Theorie BHY): telescopische som en de stap naar $q\,c(M)/M$ uitgeschreven.
- 14 (Toy): samen met rij 1 herschreven. 15 (Wat er brak): datamining als derde lezing met werkwoord, kocht-kocht weg, staccato-slot herbouwd.
- 11 en 13 niet gedaan (buiten de verplichte tien; woordbudget).
- Extra: Oordeel-inleiding zegt nu wat de tabel toont (H9), "Bovendien/de verwachte minderheid" herschreven (H8), "replicatieblok" als regeltaal weg.
Navertel-toets: Theorie wijkt nog iets af (FF5 en q blijven de losste stap); Replicatie shrinkage leest nu als voorspelling tegen waarneming plus drie verklaringen.
Code en uitvoer ongewijzigd (nb_outputs identiek); nb_numbers geen nieuwe meldingen. Woorden 5.887: onder 6.000, boven het streefgetal 5.500.

## R9-1 (F6b, ronde 9+)

Afgemaakt na een afgebroken eerdere run; per punt uit notes/eind-06_34 nagegaan (diff tegen ijkkopie, grep).
- **Feitelijke fouten.** 1 r. 1084: "tegen 90 zonder correctie" toegevoegd. 2 ICI: "iets meer dan". 3 oefening 2: "gemiddeld 4,69" (de gerapporteerde $t$, cel). 4 "elf jaar extra data" vervangen door "recentere data".
- **Verbetering 1 (toy).** Grenskolommen zonder formules; één zin per procedure wat ze beschermt, afleiding naar Theorie. B–E keren terug bij de afknotting ($2{,}54$ tegen $\lambda(2) = 2{,}37$). Getal bij r. 114 (0,028, $9 \times 0{,}028 \approx 0{,}25$). BHY strenger dan Bonferroni bij rang 2 als halve zin.
- **Verbetering 2 (helderheid).** $\Phi$ en $\varphi$ benoemd; r. 233 "het gemiddelde rendement, of de alpha"; Holm "nog geen ware nulhypothese verworpen"; q-reden voor beide helften; voorwaarde $\Cov_t$ uit de formule naar de tekst; alias signaal/voorspeller in het Overzicht, daarna overal "signaal".
- **Verbetering 3 (figuren).** Leeswijzer vóór beide figuren (histogram/kromme en snijpunten 26%/58%; verschuiving langs drempels en helling onder één).
- **Opbouw.** Shrinkage-sectie opent met de conclusie (7 tot 9% tegen 40%); alpha-sectie opent met waarom de toets bij de vraag hoort.
- **Taal.** Hardop-zinnen 1–3 (r. 411, 1109, 1127) herschreven; r. 1017 (schatting/schatten) en r. 1103 ("die") herschreven; eenzinsalinea's r. 193 en 696 aan de buur gehangen.
- **Beter uitleggen.** Variantie $1 + \omega^2$ als som van ware $t$ en ruis; $\Pr(\delta < 0) = \Phi(7{,}4/6{,}1) \approx 0{,}89$; relatieve daling $t$ = relatieve daling rendement bij gelijke standaardfout.
- **Replicatie.** Alinea met vijf getallen (r. 812–816) in twee gesplitst.
- **Code.** Importcel na de inleidende zin; lange regels gebroken (`by_hand`, drempelcel met `t_ours`, `rank_corr`); `after_pub` via `pub_year` met commentaar. Offline uitgevoerd; nb_outputs gelijk aan de ijkkopie op één celkop na (regelbreuk in de bron).
- **Woordbudget.** Om onder 6.000 te blijven: herhaling na de toy-code, de tussenperiode-zin bij McLean en Pontiff en enkele omwegen geschrapt; lange zinnen gesplitst (p90 29 → 26, > 40: 2 → 0; twee zinnen herschreven omdat prose_stats "10. "/"69. " als lijstnummer las).
- nb_numbers: drie nieuwe meldingen, alle met de hand herleidbaar (0,00341 uit de toytabel, 2,54 als gemiddelde van vier tabelwaarden, 4,69 in oefening 2 zoals al in de replicatietekst). Geen afwijzingen.
Woorden 5.998 (prose_stats PASS). open=0.
