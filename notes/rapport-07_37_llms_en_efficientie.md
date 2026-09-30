STATUS 07_37_llms_en_efficientie F4T words=5592 prose=PASS open=0 cijfer=- min=-

# Rapport 07_37_llms_en_efficientie

**Kern.** Maakt bijna gratis informatie (het taalmodel) beleggingsadvies beter en prijzen
efficiënter? Advies: betere mediaan, slechtere staart; efficiëntie: goedkopere informatie
maakt prijzen informatiever maar nooit volledig (Grossman-Stiglitz), en omdat gedeelde
modelfouten niet wegmiddelen, worden relatieve prijzen efficiënter en het marktniveau niet.

## F0

`prose_stats`: words=5786 sent_mean=20.7 sent_p90=37 sent_gt40=19 para_mean=55 semicol=42
motief=3 deel=3 calque=2 engquote=21 colon_mid=10.7 para_one=25 telegram=1 tmpl=7 connect=17
→ FAIL op 13 drempels (niet op words; de opdracht noemde 8.900, gemeten is 5.786).

Vijf grootste problemen:
1. Engelse citaten midden in de zin (21), vooral Theorie "Crowding" (r. 435–450), "Machines
   die lezen" (r. 508–523), "Advies als portefeuillekeuze" (r. 554–574) en de replicatie.
2. Lange zinnen en puntkomma's (19 zinnen > 40 woorden, 42 puntkomma's), overal; getallenbrij
   in Simulatie (c) (r. 891–910), Lopez-Lira (r. 510–523) en Replicatie (r. 1077–1084, 1136–1143).
3. Structuur: imports-cel in Overzicht (r. 79), admonition "Epistemische status" met "motief 3"
   (r. 64–77), geen routekaart en geen Samengevat in Theorie, drie simulaties, vier stellingen
   met open bewijs, GS-propositie met drie beweringen (r. 268–305, H3), toy met twee mechanismen.
4. Notatie: $m$ in GS botst met de stochastische discontofactor, $\rho$ betekent zowel
   $\Corr^2$ als fractie gedeeld model (H7), $r_t$ i.p.v. $\ell$ voor het log rendement
   (r. 468), $R^f - 1$ in eq-groei (r. 546) terwijl $R^f$ netto is.
5. Replicatie: blok ~430 woorden (max 250), geen tabel origineel/hier, geen oordeel
   "Geslaagd/…"; getallen voor 2020 los en rangcorrelatie (r. 1141–1143) en "ongeveer 7% in
   januari 2023" (r. 1083) staan in geen cel.

Schraplijst (eis 2 gecontroleerd met grep: buiten dit college wordt alleen het paginalabel
`07-37-llms-en-efficientie` aangehaald, door 02_07, 06_36, 08_38, 08_39):

| passage | kopje | woorden | eis niet gehaald / actie |
|---|---|---|---|
| admonition Epistemische status | Overzicht | ~110 | 1–3; "motief 3"/"epistemisch" verboden; één zin in Overzicht |
| simulatie (c) advies, 2 cellen, figuur | Simulatie | ~430 | 1 (advies volgt uit eq-groei en empirie), 2 (cel/fig-advies nergens aangehaald), 3 (motief ook in replicatie); schrappen |
| propositie engagement + bewijs + citaat | Theorie | ~200 | 1, 2; vierde open stelling; wordt twee zinnen |
| joint hypothesis (intuïtie + subsectie) | Intuïtie, Theorie | ~150 | 1; één zin in Wat er brak |
| Lopez-Lira getallen | Theorie | ~250 → 110 | getallenbrij; kern blijft |
| crowding en Khandani-Lo met citaten | Theorie | ~230 → 90 | inkorten, parafraseren |
| replicatieblok | Replicatie | ~430 → 230 | §11.7; tickers staan al in de cel |
| citaten D'Acunto, Barber-Odean, Robinhood | Theorie | ~180 → 110 | parafraseren |
| GS-propositie drie delen | Theorie | ~60 | één bewering, rest naar bewijs |

Toevoegingen: routekaart (~70), Samengevat (~110), opzet-tabel toy, twee oordelen onder
tabellen origineel/hier (~120). Verwachte lengte: 5.786 − ~1.450 + ~350 ≈ 4.700–5.200
(met extra voegwoorden). Geen splitsing nodig.

## F1

Eindmeting: words=5509 sent_mean=16.7 sent_p90=25 sent_gt40=0 para_mean=53 semicol=0 dash=0
engquote=0 colon_mid=0.9 para_one=10 telegram=0 tmpl=2 connect=32 → PASS op alle drempels.
Offline uitgevoerd zonder fouten of warnings; rewrap en jupytext --sync gedaan.

Geschrapt of verplaatst:
- admonition "Epistemische status": verboden "motief 3"; theorie of feit nu in één alinea Overzicht.
- simulatie (c) advies met cel/fig-llms-en-efficientie-advies: schraptoets eis 1–3; het
  adviesantwoord rust op eq-groei (handberekening 0,41) en de empirie.
- propositie engagement (thm-/eq-llms-en-efficientie-engagement): vierde open stelling, nergens
  aangehaald; mechanisme (kwadratisch verlies) blijft in twee zinnen.
- joint-hypothesis-subsectie: één zin in "Waar het breekt"; ChincoFos-keerzijde,
  Budish-wapenwedloop, Barber-Odean 2001, Kahneman-Tversky, Gu-Kelly-Xiu: nevenlijnen.
- vier-arbitrageurs-voorbeeld van Toy naar Theorie (bij thm-mono); toy heeft nu één mechanisme
  en één recept (eq-lambda). GS-propositie één bewering; eq-rho naar Opzet, eq-ratio in het
  dropdownbewijs; halfwaarde-bewijs in dropdown. Engelse citaten geparafraseerd, op twee
  blokcitaten van Santa-Clara na.
- Notatie: GS-parameter m → nu (botste met de discontofactor), fractie gedeeld model rho →
  omega, schok epsilon_t → xi_t, log rendement r_t → ell_t, eq-groei R^f − 1 → R^f (netto).

nb_outputs-diff, elk verschil:
- toy GS en toy monocultuur: kolommen "met de hand"/"code", nieuwe rijnamen; getallen gelijk.
- sim_gs: Nederlandse kolomnamen, getallen gelijk; monocultuur-simulatie gelijk, figuur alleen
  as-label (omega).
- oude cellen 8–9 (advies) weg; nieuwe cel na de decennia: autocorrelatie 2020 −0,336,
  2021–2026 −0,019, rangcorrelatie −0,042 (de tekst noemde −0,34 en −0,02 al zonder cel).
- oefening 2: simulatiewaarden anders (K=10 markt 1.111 → 1.096) doordat de trekkingen van de
  geschrapte adviessimulatie niet meer voorafgaan; niet in de tekst aangehaald.
- replicatie, oefening 1 en 3: gelijk (celnummers verschoven).

Afvinklijst §11.9, wat niet volledig voldoet:
- Simulatie: twee economieën onder één vraag (wat laat één jaar data zien).
- Enkele alinea's met meer dan drie getallen (Barber-Odean in Advies, "Het verraderlijke").

Labels: weg thm-/eq-llms-en-efficientie-engagement, cel-/fig-llms-en-efficientie-advies (grep:
nergens aangehaald); oefeningslabels niet meer als link. Naad: slot 06_36 opgepakt in "Wat we
al weten"; de zin die 08_38 citeert en de coronaverklaring van −0,15 blijven.

Open punten voor de feitencontroleur:
1. Lopez-Lira en Tang 2023: 0,231 (t = 4,7), kleine aandelen "bijna driemaal" (0,652), GPT-2/BERT.
2. LopezLiraTang2026: strategierendementen dalen met de adoptie van taalmodellen.
3. Barber-Odean 2000: omloop 75%, "vijfde deel dat het meest handelde" 11,4% tegen 17,9%.
4. "ongeveer vijf dollar" (GabaixKoijen2021) naast de 2–8 uit 06_36.
5. Khandani-Lo 2011: verkorte lezing (gelijktijdige afbouw, week van 6 augustus 2007).
6. D'Acunto e.a. 2019: betere rendementen, minder dispositie-effect en trendvolgen.
7. Robinhood: −4,7% over twintig dagen (BarberHuangOdeanSchwarz2022).
8. Indexfutures vanaf 1982 en ETF's vanaf 1993 staan zonder citatie.
9. Parafrases Santa-Clara (advies marginaal gratis; halfwaardetijden 1969/2000/nu).
10. Eisfeldt e.a. 0,4% per dag uit hun samenvatting; niet meer geciteerde bib-keys blijven staan.


## F4

Feitenrijen (alle tien opgelost, open=0):
- 1 Simulatie, Informatiekosten: spreiding 0,016 tot 0,045. 2 idem: voordeel groeit vanaf c = 0,03 (tekst en figuurtekst).
- 3 Replicatie, ChatGPT: tabel "0,4% per dag (samenvatting)", "ruim 4%" weg. 4 idem: zin over de koersdaling van technologieaandelen geschrapt.
- 5 Waar we zijn en Gedeelde modelfouten: "maakte aannemelijk", twee tot acht dollar met vijf als midden, "kunnen vergroten" (naad 4).
- 6 Snellere prijzen: tekst, vraagzin en figuurtekst (2020s meer dan 0,1 onder nul, 2000s net buiten het interval).
- 7 Gedeelde modelfouten: Khandani-Lo als hun interpretatie. 8, 9 Wat er brak: "in lijn met", geen causale want; 2008 genoemd.
- 10 Wat er brak: Engels motto vervangen door parafrase met verwijzing naar 00-00-setup (enige vermelding).
Lezerspunten:
- 1 Wat er brak: slotzin voorwaardelijk op gedeelde scores, strookt met Lopez-Lira. 2 = feiten 5. 3 = feiten 10.
- 4 Replicatie ChatGPT: "Niet geslaagd", met 0,15% en t = 0,04. 5 Snellere prijzen: zin per aandeel tegen hele markt.
- 6 Gedeelde modelfouten: eerste zin volgt uit de alinea erboven. 7 Toy: nu en k benoemd, "dat aandeel" weg.
- 8 = feiten 8 en 9. 9 Advies: kwadratisch verlies uitgeschreven, staart aan de klant gekoppeld; geen rekenvoorbeeld (getal niet uit cel).
- 10 Simulatie: waarom handelswinst gemeten wordt, conclusie vooraan. 11 Intuïtie: bierviltje, geen aflevering/marginaal.
- 12 Halfwaardetijd: niet-synchrone handel als gewone zin. 13 Opzet/Wat het voorspelt: liquiditeitshandelaren (noise traders), daarna aanbodruis.
- 14 Overzicht: sjabloonzin herschreven. 15 "Gedeeltelijk geslaagd" en slotzin verbonden; "De lijn blijft binnen de band" blijft twee zinnen (para_one).
Verder: evenwicht zonder "Waarom zou dit waar zijn?", Advies met conclusie vooraan (H9), Samengevat bullet 4 met reden (H6), Chicago-/Yale-lezing kort uitgelegd (H2).
Betaald met: Barber-Odean 11,4/17,9 (niet nagezocht), dubbele niet-synchrone-uitleg in Replicatie, Robinhood ingekort, Overzicht-geschiedenis ingekort.
Navertel-toets week af in: Gedeelde modelfouten (koppeling eerste zin), Replicatie (oordeel eerste vergelijking), Wat er brak (slotzin); alle drie hersteld.
Code ongewijzigd; nb_numbers geen nieuwe meldingen (12 naar 10); rewrap en jupytext --sync gedaan.

## R9-1 (F6b, ronde 9+)

Woorden 5801 (was 5592), prose_stats PASS (geen zin > 40), nb_numbers 10 meldingen (gelijk aan vóór), celuitvoer na herberekening identiek.

- **Feit 1, Samengevat $\omega$**: gedaan; grotere $\omega$ vergroot de fout in het niveau, relatieve prijzen via wegmiddelen per aandeel.
- **Feit 2, DSSW**: gedaan; "de liquiditeitshandelaren van aanname 3", DSSW-verwijzing geschrapt.
- **Feit 3, replicatietabel**: gedaan; beide kolommen cumulatief over dag 0 t/m 10 (ruim 4% tegen 0,15%).
- **Feit 4, "veertig jaar hoog"**: gedaan; geleidelijke daling, met ChatGPT in één sprong.
- **Opbouw, event study**: gedaan; Overzicht en eerste alinea van de eventsectie zeggen waarom (het ene moment waarop $c$ sprong, markt die nieuws in uren verwerkt).
- **Opbouw/helderheid, staart advies**: gedaan; omloop naar 300% kost 4,5 procentpunt per jaar extra (uit $\kappa = 2\%$ en 75%).
- **Opbouw, "beide mechanismen"**: gedaan; in Overzicht en simulatie-opening bij naam.
- **Helderheid, reden spreiding/handel**: gedaan; variantie voor spreiding, spread en commissie voor handel.
- **Helderheid, $w_j$, $\bar\beta$, $g$ tegen $\omega$**: gedaan; één zin over $g$ en $\omega$, gewichten tot nul met bèta nul, $\bar\beta \approx 1$.
- **Taal, hardop-toets 1–3**: gedaan volgens voorstel (07_37:64, 99, 1061).
- **Taal, Samengevat samengeplakt**: gesplitst in autocorrelatie en advies.
- **Taal, formule-opening simulatie**: vervangen door de vraag zelf.
- **Toy, $e^{2ac}$**: gedaan; verhouding van de restvarianties in één zin.
- **Code, `sum`-truc en `gs_price`**: gedaan; lijstcomprehensie en commentaar naar stap 1 van het bewijs; uitvoer ongewijzigd.
- **Replicatie, indeling 8+8+20+14**: gedaan in "Data hier"; dubbele zin in de eventsectie geschrapt.
- Afgewezen: geen.
