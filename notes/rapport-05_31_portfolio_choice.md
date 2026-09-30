STATUS 05_31_portfolio_choice F4T words=5834 prose=PASS open=0 cijfer=- min=-

# Rapport 05_31_portfolio_choice (L31)

**Kern.** Hoe zet een belegger een handvol slecht gemeten feiten om in portefeuillegewichten? Door niet duizenden verwachte rendementen te schatten maar een paar coëfficiënten die de gewichten aan kenmerken en voorspellers koppelen; dat dempt de schattingsfout van Markowitz (ruis van orde K in plaats van N), maar de regel ziet niet of de premie van gisteren morgen nog bestaat, en welk risico de markt beloont (Goyal en Santa-Clara) bleef niet overeind.

## F0

Nulmeting op HEAD (de herschreven versie stond al in de werkkopie; F0 is achteraf gedaan op `git show HEAD:`).

```
words 6016  sent_mean 21.8  sent_p90 40  sent_gt40 28  para_mean 62  dash 19  semicol 55  motief 2  deel 1  taboo 1  calque 4  engquote 35  colon_mid 11.5  para_one 25  tmpl 4  connect 18
FAIL: words, sent_mean, sent_p90, sent_gt40, para_mean, dash, semicol, motief, deel, taboo, calque, engquote, colon_mid, para_one, tmpl, connect
```

Vijf grootste problemen (HEAD):

1. Drie replicaties (r. 866–1418, samen ~1.630 woorden), waarvan "Managed portfolios op de markt" (r. 1191) getallen citeert die niet in het gepubliceerde artikel te vinden waren (r. 1203–1204).
2. Twee simulaties (r. 623–866), terwijl §11.9 één simulatie met één steekproefvraag vraagt; (b) "Gemiddelde variantie zonder informatie" (r. 769) hoort bij de toets van GSC, niet bij de parametrische regel.
3. Zinsbouw: 55 puntkomma's, 28 zinnen boven 40 woorden, 19 gedachtestreepjes, 25% alinea's van één zin (bv. r. 1088–1101, getallenbrij met "(paper: …)").
4. Engels: 35 Engelse citaten en termen ("policy" in kop r. 209, "paper", "in-sample"), vier calques; sjabloon "Waarom zou dit waar zijn?" vier keer (r. 276, 360, 460, 540).
5. Geen "Samengevat" aan het eind van Theorie; theorie versnipperd over vijf subsecties, met "Beperkingen: short posities, kosten en tijdsvariatie" (r. 503) als los aanhangsel.

Schraplijst (afgeleid uit `git diff HEAD --stat` en de koppen; eis 2 met grep op labels in lectures/: geen van de betrokken labels wordt elders aangehaald):

| passage (HEAD) | woorden | eis die ze niet haalt |
|---|---|---|
| Replicatie "Managed portfolios op de markt" (r. 1191) | ~306 | 1 en 3: de vraag is met BSV en GSC beantwoord; getallen niet verifieerbaar |
| Simulatie (b) "Gemiddelde variantie zonder informatie" (r. 769) | ~220 | 1: wordt oefening 4 (overlap en persistentie) |
| "Beperkingen: short posities, kosten en tijdsvariatie" (r. 503) | ~219 → ~80 | 1: long-only en kosten blijven (nodig voor replicatie en oef. 3), tijdsvariatie weg |
| "Waarom drie parameters…" (r. 458) | ~213 → in "Wat het voorspelt" | samengevoegd, herhaling weg |
| Getallenbrij "(paper: …)" in replicatietekst (r. 1088–1101, 1175–1182) | ~150 | 1: staat al in de tabel origineel/hier |

Verwachte lengte na schrappen: 6.016 − ~900 + Samengevat, routekaart en oefening 4 (~+700) ≈ 5.800.

## F1

**Staat bij start.** Een eerdere agent had het college al herschreven (5.965 woorden, FAIL op sent_gt40=3 en para_one=19). Ik heb het één keer volledig gelezen en alleen hersteld wat niet deugde.

**Eindmeting.** words 5832, sent_mean 17.8, p90 27, gt40 2, para_mean 47, dash 0, semicol 5, engquote 3, colon_mid 0.3, para_one 10, tmpl 1, connect 28: PASS.

**Hersteld in deze ronde.** Alinea's van één zin aangevuld of gesplitst (Waar we zijn, propositie-aannames, tabelaankondigingen, oordeel "Gedeeltelijk geslaagd", Wat er daarna kwam, opgaven 1 en 3, uitwerkingen 1 en 3); te lange zin in de geschiedenisalinea gesplitst; "ze/haar" voor de regel vervangen door "hij"; "Santa-Clara's praktijkmotief" (motiefnaam) herschreven.

**Geschrapt deze ronde (reden).**
- Santa-Clara over "wat het vak niet weet" (Theorie, GSC): herhaalt het Overzicht.
- Alinea "Ook de benchmark zelf is onzeker" (Simulatie): tweede steekproefvraag, niet nodig voor de vraag.
- No-trade-band-zin (Theorie): niet gebruikt in replicatie of oefeningen.
- Laatste Samengevat-punt over de simulatie: vooruitwijzing, geen samenvatting.
- "t boven 3"-zin in GSC-replicatieblok; herhaalde Sharpe-getallen na 2002 in "Waar het breekt"; dubbele motivatie GSC in Theorie; ingekorte figuurbijschriften.

**nb_outputs-diff (voor = HEAD-ipynb, na = nieuw).** Geen enkel aangehaald getal veranderd. Verschillen: (1) toy-cellen tonen nu één tabel "met de hand / code" in plaats van losse prints (theta0 0.249505 vs hand 0.24950, afronding); (2) kolomnamen "gem. excess" → "gem. overrendement", "turnover" → "omzet", "out-of-sample" → "buiten de steekproef"; (3) cellen van de BSC-managed-portfolio-replicatie (tabel statisch/managed) weg; (4) figuur sim-b weg; (5) overlap-simulatie (25.8%, 0.028 … 0.188) verhuisd naar oefening 4, getallen gelijk; (6) nieuwe cel oefening 1 (0.27523, 0.18712, 0.08811); (7) celnummers verschoven, png-groottes licht anders.

**Labels.** Verdwenen: `cel-portfolio-choice-sim-b`, `fig-portfolio-choice-sim-b` (nergens anders aangehaald). Nieuw: `ex-portfolio-choice-4`. Geen labels verhuisd.

**Afvinklijst §11.9, wat niet (helemaal) voldoet.**
- Lengte 5.832: onder de grens, boven het doel 4.500–5.500; verder schrappen raakt replicatie of oefeningen.
- sent_gt40=2 zijn splitsartefacten van prose_stats (getal vóór punt, `{cite:t}` aan zinsbegin).
- Drie verwijzingen naar oefeningen in de lopende tekst ("oefening 2 leidt af", "oefening 4 meet", "oefening 4 laat zien").

**Open punten voor de feitencontroleur.**
1. Bijschrift fig-portfolio-choice-bsv: "size tussen −1,0 en −1,4, daarna −0,30; B/M rond 5, zakt naar 2,7; momentum 2,2–3,2" komt uit de figuur, de cel toont maar vijf jaren.
2. Na 2002: Sharpe 0,62 tegen 0,72, CE 0,9%, 23% vol, 14% overrendement: nakijken tegen de OOS-tabel.
3. Citaties: BSV "kosten van 0,5% raken het CE nauwelijks"; Ang e.a. −1,31% (werkpaper, tabel VI); HKLV 5,4%; CLMX "meer dan verdubbeld / een derde"; GSC "bijna 85%" (kalibratie).
4. Jaartal-regel noemt 2006 en 2009 (uit de bib-sleutels).
5. `slope_tstats` in oefening 4 heeft `# TODO: naar hap.stats`: rijsgewijze Newey-West ontbreekt in hap.
6. `0,048` omzet benchmark per maand en `0,79%` break-even: uit de print-regels van oefening 3.

## F4

Feitenrijen (notes/feiten): alle zes afgehandeld, open=0.
- #1 Bijschrift fig-portfolio-choice-bsv (Replicatie): herschreven naar de vijf getoonde jaren, geen codewijziging.
- #2 3.680 aandelen (Theorie, BSV): citatie toegevoegd.
- #3 Ang e.a. (Theorie, GSC): "(werkpaperversie, tabel VI)" geschrapt.
- #4 CLMX (Theorie, GSC): "met ongeveer een derde" wordt een relatieve bewering.
- #5 BSV-kosten (Theorie, Wat het voorspelt): onbevestigd cijfer weg, mechanische bewering over omzet en CE na kosten.
- #6 GSC 85%: behouden, secundaire bron bevestigt 80–85%.
Lezerspunten:
- 1–2, 7, 8, 14: zie feitenrijen 3, 4, 2, 1, 5.
- 3 (Wat er brak): "dan enig model uit de literatuur".
- 4 (Overzicht): gestapelde "maar"-zin gesplitst.
- 5 (Theorie, BSC): standaardfout-zijspoor weg; Britten-Jones levert nu alleen dat een gewone regressie de gewichten geeft.
- 6 (Theorie, Wat het voorspelt): overgang benoemt waarom er aanpassingen komen.
- 9 (Wat er brak): "beslisregel" niet meer dubbel.
- 10 (Replicatie GSC): ontkenning niet meer dubbel.
- 11 (Toy a): eerste zin geeft de bewering; inleidende alinea ingekort ter betaling.
- 12 (Replicatie BSV): "het teken draait om" wordt "verslaat de benchmark juist de regel".
- 13 (Oefening 2): momentumzin losgemaakt; 15: "ruim driehonderd".
Geschrapt ter betaling: herhaalde zin over premie van gisteren (Waar het breekt), dubbele bronzin bij de vergelijkingstabel, toy-inleiding.
Navertel-toets: geen sectie week af van de bedoeling; de drie sporen die de lezer kwijtraakte (Overzicht, BSC-zijspoor, overgang naar de praktijk) zijn gedicht.

## R9-1 (F6b, ronde 9+)

- Feit 1 (r. 925): "in de buurt" vervangen door wat de cel toont (tekens gelijk, size stabiel, B/M eerst omhoog, momentum wat omlaag).
- Feit 2 (toy b, r. 229): "onbeperkt" wordt "stijgt met elke extra eenheid θ, al blijft het onder nul".
- Feit 3 (r. 1124): "industriespecifieke onzekerheid" wordt "de gemiddelde variantie van industrieën".
- Feit 4 (bijschrift sim): "bij vijftig jaar niet meer" wordt "bij vijftig jaar veel smaller" (geen bewering over nul meer).
- Helderheid: long-only-schatting benoemd, met tekenwissel size, B/M bijna vier keer en de reden (afkappen legt de schaal niet vast); r. 471 herschreven volgens hardop 2; γ in toy (a) "risicoaversiecoëfficiënt"; r. 436 zegt nu "overrendement" ($R^e$, als in de simulatie).
- Opbouw: 1/N speelt in de simulatie "de rol van de markt"; slotzin simulatie zegt "verslaat de markt van deze wereld". Premies 0,03% tegen 0,54% ruis staan nu in "Wat het voorspelt".
- Toy: bijzin dat (b) CRRA gebruikt omdat BSV dat doen; slotzin (b) geeft de betekenis van θ* (gewicht aandeel 3 +θ*/3, ruim zeven procentpunt; zonder nieuw decimaal getal).
- Code en figuren: nieuwe alinea vóór de simulatiecel met het éénfactormodel Σ = v_f bb' + diag(s²) en de Woodbury-formule; AR(1)-commentaar in de lus (alleen commentaar, uitvoer identiek na nbconvert); zin over standaardisatie per maand in `characteristic_panel`.
- Replicatie: vijf rijen "2003–2026" in de tabel (SR 0,62/0,72, CE 0,9/6,6, overrendement/vol 14/23, long-only 0,64/4,3, size/momentum 0,65/0,74) en long-only-omzet 1,37; de alinea na de tabel draagt alleen nog het oordeel en de standaardfout 0,21.
- Oefening 2(2): eerste-ordevoorwaarde expliciet.
- Hardop 1–3 herschreven (1 en 3 volgens voorstel; 1 in twee zinnen gehouden voor para_one).
- Ter betaling geschrapt: dubbele zin in toy (a)-inleiding, zin over "slechte ruil" (γ = 5) na 2002.
- Afgewezen: geen.
- Woorden: 6.000 (PASS); nb_numbers 71 meldingen, gelijk aan vóór F6b.
