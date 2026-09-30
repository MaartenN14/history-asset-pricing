STATUS 05_29_opties_crashrisico F4T words=5859 prose=PASS open=0 cijfer=- min=-

# Rapport 05_29_opties_crashrisico (L29)

**Kern.** Wat kost verzekering tegen een crash? Optieprijzen geven een crash een risiconeutrale
kans die een veelvoud is van de werkelijke, zodat een flink deel van de aandelenpremie
crashpremie is, terwijl de winst van wie die verzekering verkoopt in rendementsdata niet te meten is.

## F0

`words=6070 sent_mean=21.6 sent_p90=36 sent_gt40=15 semicol=50 motief=6 je_form=1 calque=5
engquote=31 colon_mid=10.4 para_one=26 telegram=1 tmpl=7 connect=17` → FAIL op 14 drempels.

Vijf grootste problemen:
1. Overal (Theorie, Replicatie, Wat er brak): 31 Engelse citaten midden in Nederlandse zinnen
   (o.a. r. 249–252 Jackwerth, r. 339–342 BTZ, r. 450–458 Santa-Clara en Yan, r. 553–559 Saretto).
2. Theorie: zeven keer "*Waarom zou dit waar zijn?*" (r. 220–519); geen routekaart, geen Samengevat;
   vier stellingen/proposities met open bewijs.
3. Toy (r. 109–203): drie opties plus premie plus VRP, codecel eindigt met prints en een tabel
   zonder hand/code-vergelijking.
4. Simulatie (r. 563–931): twee simulaties ((a) Merton + BL-ruis, (b) puts verkopen); motief 1
   bij nummer (r. 101, 458, 872, 1195); getallenalinea's (r. 721–735, 846–869, 924–931).
5. Replicatie (r. 1119–1124, 1183–1195, 1293–1301): gepubliceerde getallen en uitkomsten in
   proza in plaats van tabel origineel/hier; geen "Geslaagd"-oordelen; Overzicht met
   imports-cel en "definieert het tijdvak" (r. 47).

Schraplijst (eis 2: geen enkel label van dit college wordt buiten het college aangehaald, grep op
`opties-crashrisico` in lectures/):

| passage | ≈ woorden | eis niet gehaald |
|---|---|---|
| Coval-Shumway-bewijs (dropdown), vervangen door bewijsidee | −190 | 1, 2 |
| Merton- en momentenbewijs (dropdown), vervangen door één zin | −170 | 1, 2 |
| Engelse citaten → korte parafrase (31 stuks) | −350 | 1 |
| Oefening straddle (oud 3) met uitwerking | −200 | 1, 2 |
| Jackwerth-, Bates-, Pan-, BCJ-, Israelov-details | −150 | 1 |
| Getallenalinea's simulatie en replicatie → tabellen | −250 | 1 |
| Toy: at-the-money-put, prints | −60 | 1 |
| Toevoegingen: routekaart, Samengevat, instap-oefening, tabellen-inleiding | +450 | – |

Verwachte lengte: 6070 − 1370 + 450 ≈ 5150 à 5800. Geen splitsing nodig.

## F1

Eindmeting: `words=5778 sent_mean=17.5 sent_p90=26 sent_gt40=0 para_mean=44 dash=0 semicol=10
motief=0 calque=0 engquote=0 colon_mid=1.6 para_one=11 telegram=0 tmpl=2 wie_open=3 connect=29` → PASS.
Boven het doel van 5.500; F4 moet elke toevoeging met schrappen betalen.

Geschrapt of verplaatst:
- Bewijzen Coval-Shumway, Merton, momenten: vervangen door één alinea bewijsidee (dropdown telt mee).
- Simulatie (a) → Theorie "### Numerieke oplossing" (één simulatie over, één steekproefvraag).
- Oefening straddle geschrapt (nevenresultaat); nieuwe instap-oefening op het toy (ex-1).
- Israelov 2019 en IsraelovNielsen2015a-citaten, Carr-Wu-toelichting, BTZ-citaat, "4% tot 6,9%"
  transactiekosten, SCY 5,8%/70%/12,8 jaar, SPY exces-kurtosis-kanttekening: niet nodig voor de vraag.
- Imports-cel naar begin Toy; Waar we zijn nu met twee eerdere colleges (02-09, 05-27).

nb_outputs-diff (overig identiek, ook alle rng-afhankelijke cellen):
- cel 2 (toy): prints en tabel vervangen door één tabel "met de hand / code", zelfde getallen;
  de at-the-money-put (0,0795; 0,3081) en de q/p-kolom verdwenen (niet aangehaald).
- cel 18 nieuw: instap-oefening (0,9051; 0,0827; 0,0225; 0,1336), klopt met handberekening.
- cellen 18–19 oud → 19–20; oude cel 20 (straddle) verdwenen.

Afvinklijst §11.9 (alleen wat niet voldoet):
- words 5778 boven doel 5.500 (onder grens 6.000).
- Replicatieblokken hebben elk één-zinsonderdelen (para_one binnen drempel).
- Simulatie toont ook de margetabel (bijproduct van dezelfde paden, geen tweede vraag).
- Overige: ok.

Labels: geen verdwenen. Oefeningslabels hernummerd: nieuw ex-1 (instap), oud ex-1 → ex-2,
oud ex-2 → ex-3, oud ex-3 (straddle) weg; verwijzingen in de tekst nu als "oefening 3".

Open punten voor de feitencontroleur:
1. Standaardfout Sharpe-ratio gecorrigeerd: √((1 + 1,85²/2)/20) = 0,368 → "0,37" (was 0,35).
2. SCY-tabel (werkdocument SantaClaraYan2004, tabel 3/4, §5.3): 18,3% is "gemiddelde
   volatiliteit"; nagaan of dat diffusie of totaal is; ook 2,9%, 10,1%, −31,6%, −2,2%.
3. Saretto–Santa-Clara werkdocument: 59,1% per maand en scheefheid −11,06 niet nagekeken.
4. Bakshi-Kapadia-Madan: tabellen niet ingezien; replicatie toetst alleen het teken.
5. "VIX gemiddeld vier volatiliteitspunten boven de latere volatiliteit" en de VRP rond vier
   punten: controleren tegen 02_09_black_scholes.

## F4

Feitenrijen:
- Rij 11/punt 15 (Sharpe 0,33 tegen 0,36), Simulatie: gedaan, nu 0,326 tegen 0,355 uit cel 7.
- Punt 14 (SCY 18,3%), Crashpremie-tabel: gedaan, SCY-kolom "18,3% diffusie".
Lezerspunten:
- 1 = feitenpunt 14, gedaan. 2 (sprongpremie/crashpremie), Crashpremie: accoladelabel en kop oefening 2 nu "crashpremie"; de print in codecel 3 blijft (code).
- 3 (telegramzin), Replicatie SPY: gedaan, één zin met persoonsvorm.
- 4 (link motief), Crashpremie: gedaan; tweede vermelding in Simulatie zonder motiefnaam herschreven.
- 5 = feitenpunt 15, gedaan. 6 (orde van η), Crashpremie: gedaan met ση = 3,5% bij σ = 15% (geen nieuw getal).
- 7 (dollar die uitbetaalt), Intuïtie: gedaan. 8 (asymmetrie put/call), Toy: beide nu bruto rendement plus gemiddeld verlies/winst.
- 9 (brug naar Saretto), Marges: gedaan, scheefheid gekoppeld aan de ruïnedrempel.
- 10 (dichte alinea), Overzicht: chronologisch herschreven, alinea niet gesplitst (volgorde vast).
- 11 (δ = 0), Merton: zin geschrapt. 12 (data spreken tegen), Merton: samengevoegd met "maar".
- 13 afgewezen: het getal (vier volatiliteitspunten) staat er al (H2 voldaan).
- 14 (VRP-weerlegging), BTZ: gedaan, zegt nu welke bewering overeind blijft.
- 15 afgewezen: de alinea zegt al wat de lezingen zou scheiden (de SDF in crashtoestanden); herschrijven, niet toevoegen (§11.12).
Verder: "haar" voor de markt (Toy), "in-the-money" → "in het geld", "ondergrens" kreeg een antecedent,
één zin en één Samengevat-bullet (vooruitwijzing) geschrapt ter betaling.
Navertel-toets: geen sectie week af (koude lezer: alle secties "klopt"); spoor-kwijt-plekken 1–3 behandeld via punten 1/2, 9 en 10.

## R9-1 (F6b, ronde 9+)

- **Feitelijke fout 1 (PutWrite even diep):** gedaan; tekst na de tabel en bijschrift zeggen nu "in 2020 even diep, in 2008 ongeveer twee derde zo diep" (cel: −0,316 tegen −0,509).
- **Feitelijke fout 2 (na oktober 2008 hoge rendementen):** gedaan; na oktober 2008 eerst verdere verliezen, na maart 2020 hoge rendementen; conclusie afgezwakt tot "kan ver naast zitten".
- **η bij eerste gebruik:** gedaan, in de propositie benoemd; dubbele definitie erna geschrapt.
- **R in momentenpropositie:** gedaan, overal $\ell = \log(S_T/F)$ (ook bij de VIX-zin); oefening 3 gebruikt geen symbool.
- **"ondergrens":** gedaan, nu ondergrens voor een markt waarin ook volatiliteitsschommelingen een premie dragen.
- **59,1% zonder grondslag:** gedaan, "van de ontvangen premie per maand" (werkdocument, zie feiten punt 3).
- **Geleend resultaat risk-management-drempel:** gedaan, in één bijzin herhaald.
- **Smirk vlakker bij een jaar:** gedaan, diffusiespreiding groeit met de looptijd, één sprong niet.
- **Overgang Verwachte optierendementen:** gedaan, eerste zin legt de band met de verkoper.
- **Hardop-toets 1–3:** gedaan, drie zinnen herschreven (de nieuwe zin 1 zonder calque "prijst").
- **Toy stap 4:** gedaan, herschaalde kansen 0,663 en 0,337 genoemd.
- **Code: tabellabels en figuurtitel:** gedaan via `.rename` bij de weergave (BTZ en PutWrite), titel "overrendement"; berekening onveranderd, uitvoer vergeleken: alleen labels verschillen.
- **Code: margelus en margin_summary:** gedaan, lus uitgeschreven met commentaar per geval (gelijkwaardig, zelfde RNG-volgorde, uitvoer identiek); `margin_summary` verhuisd naar de cel die hem toont.
- **Gepubliceerd getal in replicatietabel:** gedaan, PutWrite-tabel kreeg een rij met de scheefheid −11,06 van Saretto en Santa-Clara plus een zin waarom PUT minder scheef is. Geen BKM-getal: tabellen niet ingezien (kaart §6).
- **SPY: waarom 1926–2026:** gedaan, één zin (kwartaalscheefheid over drie decennia meet vooral het aantal crisiskwartalen).
- **Oefening 3 volatiliteit:** gedaan, 14,8% tegen 12,3% benoemd.
- **Theorie telt acht ###-secties:** niet herschikt (geen "Voor een 9"); overgangszin lost de onderbreking op.
- **Brongegevens afgebroken regels:** rewrap gedraaid.
- Ruimte gemaakt door de Theorie-inleiding, de BCJ-zin, een figuuraankondiging en de openingszin van Wat er brak in te korten.
- nb_numbers: nieuw alleen toy-handgetallen (0,65/0,98 enz.) en de geciteerde −11,06.
- Woorden: 5994 (was 5859), prose_stats PASS.
