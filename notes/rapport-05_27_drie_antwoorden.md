STATUS 05_27_drie_antwoorden F4T words=5636 prose=PASS open=4 cijfer=- min=-

# Rapport 05_27_drie_antwoorden (L27)

**Kern.** Welke consumptie-SDF verklaart de aandelenpremie? Gewoonte, langetermijnrisico
en rampen doen het elk, maar elk leunt op een parameter die honderd jaar data niet
vastleggen, zodat de data niet tussen de modellen kiezen (observationele equivalentie).

## F0

Nulmeting (`prose_stats --check`, vóór wijziging):
`words=6096 sent_mean=20.3 sent_p90=35 sent_gt40=16 para_mean=63 dash=22 semicol=41 motief=4 u_form=3 calque=10 engquote=10 colon_mid=12.1 para_one=20 telegram=1 tmpl=7` → FAIL op 15 drempels.

Vijf grootste problemen:
1. Structuur: imports-cel in Overzicht (r.66); toy met twee mechanismen (Rietz-Barro én Epstein-Zin, r.111–235); geen routekaart of Samengevat in Theorie; numerieke oplossing Campbell-Cochrane (cc_solve) in Simulatie (r.789).
2. Taal: 41 puntkomma's, 22 gedachtestreepjes, 16 zinnen > 40 woorden, "Waarom zou dit waar zijn" 7×, u-vorm in Intuïtie (r.89), "motief 3"/"2%-motief" (r.54, 107, 986, 1159), "beprijsd", "Cochrane's".
3. Replicatie: blok ~450 woorden met getallenlijsten (r.1010–1060); "Wat de replicatie laat zien" is getallenbrij zonder oordeel Geslaagd/Gedeeltelijk (r.1142–1174).
4. Werkmeldingen in de tekst ("hebben we niet kunnen nalezen/inzien", r.346, 751, 1044, 1301) en tien Engelse citaten (Santa-Clara, Beeler-Campbell, Gabaix, "dog that did not bark").
5. Oefeningen: geen instap op het toy; naadfouten (r.26 "in de dertig", r.671 `pd_t` vs `dp_t` van 04_20).

Schraplijst (schraptoets §11.11; eis 2 gecontroleerd: geen enkel intern label van dit college wordt elders aangehaald, alleen `05-27-drie-antwoorden` zelf):

| passage | kopje | ~woorden | eis niet gehaald |
|---|---|---|---|
| bewijs Bansal-Yaron (dropdown) | Theorie/BY | 200 | 1, 2, 3 (afleiding staat in de bron) |
| EZ-bewijs, uitgeschreven tussenstappen | Theorie/EZ | 100 | 1, 2 |
| Wachter zero-coupon, Hansen-Heaton-Li, CDK-alinea | Theorie | 150 | 1, 2 |
| 0,9989-rentekalibratie, 6,69% 1947–1995, 0,36 tot 1998, 1-jaars-percentielen, data-rente | Replicatie | 180 | 1, 2 |
| replicatieblok: lijsten met bronwaarden (staan al in de tabel) | Replicatie | 230 | 1 |
| Engelse citaten en werkmeldingen | diverse | 120 | 1 |

Verwachte lengte na schrappen ≈ 5.100, plus routekaart, Samengevat, celzinnen en instap ≈ 5.500. Geen splitsing nodig.

## F1

**Eindmeting.** `words=5527 sent_mean=17.9 sent_p90=27 sent_gt40=0 para_mean=47 dash=0 semicol=5 motief=0 calque=0 engquote=0 colon_mid=1.3 para_one=7 tmpl=2` → PASS. rewrap 1280 → 1330 regels. Uitvoering offline zonder fouten.

**Geschrapt of verplaatst.**
- Imports-cel → begin Toy; toy (b) Epstein-Zin + cel → Theorie/Epstein-Zin (rng-volgorde ongewijzigd); `cc_solve`-cel → Theorie/Campbell-Cochrane (numerieke oplossing hoort in Theorie).
- BY-bewijs → één zin met verwijzing naar BansalYaron2004 (nevenresultaat); EZ-bewijs ingekort tot schets.
- Wachter zero-coupon, Hansen-Heaton-Li, CDK-alinea in Theorie (CDK blijft in Overzicht): niet nodig voor de vraag.
- Replicatie: rentekalibratie 0,9989, 6,69% 1947–1995, 0,36 tot 1998, 1-jaars-percentielen, data-rente 0,3%/3,8%: nevenresultaten, getallenbrij.
- Engelse citaten geparafraseerd; werkmeldingen naar open punten.
- Nieuw: routekaart, Samengevat, parametertabellen CC en BY, instapoefening (oude 1–3 → 2–4), oordelen Geslaagd / Gedeeltelijk geslaagd, toy als genummerde stappen + tabel hand/code.

**nb_outputs-diff** (28 regels, alle bedoeld): (1) toy-cel toont nu tabel met kolommen "met de hand / code / zonder ramp (p = 0)" in plaats van twee print-regels + tabel, zelfde getallen; (2) S-bar/r^f-uitvoer schuift naar voren (cel verplaatst), identiek; (3) print "excess rendement" → "overrendement"; (4) nieuwe cel instapoefening (`rietz_toy(0.01)`: R^f 1.05839, P/D 14.78318, premie 3.14067, gelijk aan de handberekening); (5) png-groottes van beide figuren (legendalabel "Gemiddeld overrendement"). Alle simulatie-, replicatie- en oefeningtabellen byte-identiek: geen aangehaald getal veranderd.

**§11.9, niet voldaan.** Oplossingen 3 en 4 beginnen direct met de codecel (geen aankondigende zin); "Welke vraag staat open" is één zin van 34 woorden; het toy-recept leent drie formules uit 03_12 (afgeleid daar, niet nieuw). Overige: ok.

**Labels.** Niets verwijderd. Nieuw: `ex-drie-antwoorden-4`; inhoud ex-1..3 verschoven (niet extern aangehaald, grep). Naden: (1) r.26 nu γ = 47,6 zoals 03_13 r.476; (2) `pd_t = -dp_t` bij `eq-voorspelbaarheid-cs-pv`; (3) r^f overal log van bruto R^f, Barro-bewijs expliciet `r^f = -log E[m]`; (4) 04_20-labels `eq-voorspelbaarheid-cs-pv`, `-cs-rendement` en de hond die niet blafte (04_20 r.84) bestaan; κ₁ benoemd als de ρ van 04_20.

**Open punten voor de feitencontroleur.**
1. Dividendclaim Campbell-Cochrane (vol 11,2%, correlatie 0,2): correlatie niet in de bron teruggevonden.
2. Kalibratie CC overgenomen uit Wachter (2005) tabel 1; CC-tabel 1 zelf niet geraadpleegd.
3. Waarom Wachters grofste rooster 6,6% geeft en het onze lager: niet nagegaan.
4. Notatie: kaart-rollen §3 noemt R^f netto, STYLE §3 bruto; dit college gebruikt bruto R^f en r^f = log R^f, 03_13 schrijft log(1+R^f).
5. Parafrase Santa-Clara (SantaClara2026) en Beeler-Campbell (naoorlogse autocorrelatie, Grote Depressie) nakijken.
6. √(2 × 0,13) ≈ 0,51 is een jaarbenadering; de code rekent maandelijks.
7. `HansenHeatonLi2008` niet meer geciteerd in dit college.
8. nb_numbers: 53 getallen zonder celuitvoer, alle uit handberekeningen (toy, EZ, instap) of bronnen (Barro 7,69/4,05; verwachte afwijking 3,5–4,5).

## F4

**Meting.** `words=5636 sent_mean=18.1 sent_p90=28 colon_mid=1.2 tmpl=2 wie_open=0` → PASS; nb_numbers: dezelfde 53 getallen, geen nieuwe melding; nb_outputs: alleen labels anders (`1+R^f`, `log(1+R^f)`, `R^f =`).

**Feitenrijen.**
- 1–9 (R^f bruto/netto), gedaan: toy stap 2–3 en recept `1 + R^f = 1/E[m]` met "R^f zoals overal in dit college de netto rente" (rij 9); notatie Theorie `r^f = log(1 + R^f)`; EZ-formules en handuitwerking `log(1 + R^f)`, `E[R_w]/(1 + R^f)`; oefening 1–2 idem; codesleutels `1+R^f`, `log(1+R^f)`, print `R^f = Rf_d - 1`.
- 10, 11, 12, 14 (onzeker, bronnen niet raadpleegbaar): tekst ongewijzigd, blijven open.

**Lezerspunten.**
- 1–5 (Toy, Theorie/notatie, Epstein-Zin, code): gedaan via feitenrijen 1–9.
- 6 (Epstein-Zin r.412): gedaan, "Zo krijgt nieuws ... een prijs".
- 7 (Samengevat, φ): gedaan, reden "gewoonte past zich langzamer aan".
- 8 (Samengevat, ψ): gedaan, reden voor rente en voor ongemoeide premie.
- 9 (Observationele equivalentie): gedaan, één zin in gewone taal na de definitie.
- 10 (Bansal-Yaron, H12): gedaan, openingsalinea koppelt terug naar de bescherming uit de intuïtie.
- 11 (correlatie 0,2): afgewezen, bron niet te raadplegen; geen ongeverifieerde bronvermelding toegevoegd (blijft open in feiten rij 10).
- 12–14 (parafrases, afronding 0,90): afgewezen, zelfde reden; open in feiten.
- 15 (θ = −27): gedaan, "zodat de SDF sterk op het vermogensrendement reageert".
- §11.9 uit F1: oplossingen 3 en 4 hebben nu een aankondigende zin.

**Navertel-toets.** Alleen Toy en Theorie (R^f-notatie) weken af; beide hersteld.

## R9-1 (F6b, ronde 9+)

- Feitelijke fout 1 (Epstein-Zin, :413): gedaan; nu "Bij $\gamma > 1$ en $\psi > 1$ is $\theta < 0$ en dus $\theta - 1 < 0$".
- Feitelijke fout 2 (Bansal-Yaron, bullet $\psi > 1$): gedaan; reden is nu de richting van de vermogensprijs, $\lambda_e = (\gamma - 1/\psi)\kappa_1\varphi_e/(1-\kappa_1\rho)$ positief (17,9, cel 5), bij $\psi < 1$ draait de prijsreactie om en krimpt $A_{1,m}$.
- Helderheid: $\kappa_1$, $\kappa_0$ als formule in de proza; $\kappa_{1,m}$ en $A_{1,m}$/$A_{2,m}$ ingevoerd in de propositie; vóór de propositie gezegd dat het volatiliteitskanaal (prijs daalt bij een volatiliteitsschok) maar 0,2 van ruim 5 procentpunt levert omdat $\sigma_w$ klein is; Gabaix-variant ingedeeld (:697 en de rampen-bullet).
- Opbouw: Overzicht-herhaling (Santa-Clara) herschreven tot de conclusie van het college in één zin.
- Taal: "hetzelfde handvol", "geen van de drie" (2x), :41, Yale-zin, "Die ene band ..."-zin en de peso-zin herschreven volgens de hardop-toets; rewrap-resten weggewerkt.
- Code en figuren: `cc_solve` in twee benoemde stappen (commentaar step 1 kern K, step 2 interpolatie naar rij i van M) plus een zin in de proza over rij $i$ van $\mathbf{M}$; `kappas` met formulecommentaar; docstrings bij `cc_simulate` en `by_simulate`. Berekening ongewijzigd; offline heruitgevoerd, `nb_outputs` voor/na identiek.
- Replicatie: de percentielen uit de vier bullets gehaald (oordeel per moment, verwijzing naar de tabel; 8,3%, 0,51 en 0,24 blijven); verwachting (3) nu op de drie modellen met realistische volatiliteit; bij de simulatie een bijzin waarom Barro (iid) een smalle band heeft (dividend = consumptie, rendement schommelt rond 4%, cel 10).
- Afgewezen: geen.
- Controles (na hervatting, alle punten per grep nagelopen en verwerkt bevonden): prose_stats PASS (5.856 woorden, geen zin > 40); nb_numbers geen nieuwe getallen t.o.v. ijk-2; rewrap en jupytext --sync gedraaid; nb_outputs van .ipynb identiek aan ijk-2-ipynb.
