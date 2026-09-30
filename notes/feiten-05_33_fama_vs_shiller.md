STATUS 05_33_fama_vs_shiller F4 open=0 punten=15

# Feitencontrole 05_33_fama_vs_shiller

Gecontroleerd met `tools/nb_numbers.py` (8 meldingen, alle handberekeningen of
kalibratieconstanten die letterlijk in de code staan) en `tools/nb_outputs.py` (15 cellen,
alle uitvoer bekeken). Cross-refs gecontroleerd met `grep -n` in de aangehaalde lectures.
Externe bronnen geraadpleegd voor de vijf open punten uit rapport §F1.

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 160–217 | Toy-voorbeeld: $r_1=0{,}120$, $r_2=0{,}086$, $r_3=-0{,}148$, helling $\hat b_r=1{,}34$, $\pi_0=5{,}2$pp, helling enquête $\pm0{,}52$, helling $r$ op enquête $\pm2{,}58$ | juist | cel 2 (exacte match op alle acht getallen) | – |
| 2 | 400–423 | $K\approx0{,}52$ in het toy-model, populatiehelling $r$ op enquête $+1$/$-1$ zonder meetfout | juist | volgt rekenkundig uit $a=K$ resp. $a=-\theta$ in [](#eq-fama-vs-shiller-tekens); geen cel nodig | – |
| 3 | 514–605 | Simulatiekalibratie $\phi=0{,}941$, $\rho=0{,}9638$, sd($dp$)=15,3%, sd($d$)=14,0%, corr=7,5%, meetfout=4pp, $K\approx0{,}093$ | juist | cel 3–4 (constantes letterlijk in de code, $K$-print 0,093) | – |
| 4 | 603–612 | gemiddelde $\hat b_r=0{,}132$ in beide economieën, sd helling enquête 0,012, helling $\pm0{,}093$, populatie $\beta$ $\pm0{,}525$ | juist | cel 4, exacte match | – |
| 5 | 632–633 | enquête van 30 jaar: 85% juiste teken; rendementsregressie na 100 jaar: "twee van de drie" | juist | cel 5: jaren=30 geeft 0,855/0,851; jaren=100 geeft 0,659 (≈2/3, afgerond in proza) | – |
| 6 | 681–685 | 80% juiste teken bij enquête na 20–30 jaar; rendementsregressie heeft meer dan een eeuw nodig | juist | cel 5: 0,642 (20j) tot 0,855 (30j) omsluit 80%; rendementen 0,659 (100j) tot 0,844 (150j) omsluit 80% pas na 100 jaar | – |
| 7 | 259–260, 801–814 | Cochrane-decompositie: eenjaarshellingen binnen 1 SE van tabel III; $b_r^{(15)}=1{,}16$, $b_d^{(15)}=-0{,}01$; directe rijen op 0,01 na tot 1, VAR-rijen op 0,03 na; $\rho\hat\phi=0{,}92$ vs 0,90 geeft ruim een kwart groter; tot 2025 $b_r^{(15)}=0{,}73$, eindterm 0,17 (een zesde) | juist | cel 7, alle getallen exact (1,164; -0,010; sommen 0,990/0,989/0,985; $\rho\phi=0{,}9205$; 12,56 vs 10 = +25,6%; 0,732; 0,168) | – |
| 8 | 933–945 | CFO: corr(enquête,$dp$) = -0,55 (2001–2011), -0,41 (volle steekproef), tegen -0,443 bij Greenwood-Shleifer; helling enquête op $dp$ ≈3pp ($t=-3{,}7$); helling rendement op enquête -1,4 ($t=-0{,}9$); toets $b=1$: $t=-1{,}6$ | juist | cel 8–9, exacte match (-0,545; -0,411; -0,443 hardcoded; -0,029/t=-3,733; -1,396/t=-0,941; t=-1,61) | – |
| 9 | 994–1003 | CAPE-helling $-0{,}075$ ($t=-6{,}6$) tot 2006, blijft negatief tot 2016; gemiddelde fout 2007–2015 = 7pp, steeds aan de lage kant; CAPE 2007 voorspelde 2,3%, leverde 6,6%; huidige CAPE 40,6, voorspeld 0,6%/jaar, residu-sd 4,5pp | juist | cel 11: -0,0745 (afgerond -0,075, al verklaard in rapport F1), -0,0632; +0,071; alle 9 jaren 2007–2015 hebben voorspeld < gerealiseerd; 2007-rij 0,023/0,066; print 40,6 / 0,59% / 4,5% | – |
| 10 | 1000–1001 | "Van alle decemberwaarden sinds 1881 lag alleen die van 1999 hoger" (dan 40,6) | juist, extern bevestigd | webzoekopdracht: Shiller CAPE piekte in december 1999 op 44,19–44,2, nog steeds het record; berichtgeving van eind september 2026 noemt het huidige niveau "highest since the dot-com bubble", dus geen decemberwaarde ertussenin hoger dan 40,6 | – |
| 11 | 434–437 | "Martins optiegrens... liep in de crisis van 2008 op tot boven 20% ([](#05-29-opties-crashrisico))" | **opgelost F4** (was onjuist: kruisverwijzing) | het getal zelf klopt extern (Martin 2017, QJE: de SVIX-ondergrens op de premie kwam in de crisis van 2008 boven ~21% uit), maar `lectures/05_29_opties_crashrisico.md` bevat geen enkele vermelding van Martin, SVIX of een 20%-grens (gecontroleerd met `grep -ni "martin\|svix"` en met `grep "2008\|20%"`; Martin2017 wordt in de hele map alleen in 05_33 geciteerd) | verwijder de link naar 05_29 of vervang door een rechtstreekse verwijzing naar `{cite}`Martin2017`` zonder interne kruisverwijzing; voeg desnoods een zin toe in 05_29 die dit cijfer noemt, of laat de link weg |
| 12 | 728–729 | "Cochrane gebruikt de hele CRSP-markt en wij de S&P 500... die met $1/(1-\rho\phi)$ worden opgeblazen" | juist | logische consequentie van de decompositie-formule, geen apart getal | – |
| 13 | 241–243, 360, 280–281 | Kruisverwijzingen `eq-voorspelbaarheid-lr` (04_20), `prop-behavioral-joint` (04_23), `thm-efficiente-markten-elke-sdf` (02_06) | juist | labels bestaan op de aangehaalde plek (`grep -n` in elk bestand) | – |
| 14 | 442, 1044 | Vooruitverwijzingen `06-36-inelastische-markten` en `06-34-factor-zoo` | juist | beide bestanden en labels bestaan al (Deel VI is al geschreven) | – |
| 15 | 718–724, 848 (bib) | Bronvermeldingen `CFOSurvey2026` (URL, auteurs) en de CFO-loader in de code | juist | `references.bib` regel 4361 en de URL in `CFO_URL` (regel 823–824) zijn woordelijk gelijk | – |
| 16 | 53–58, 1539 (bib) | `SantaClara2026`: LinkedIn-post van Pedro Santa-Clara, geparafraseerd als "beide kampen... over bijna elk feit eens... over bijna geen interpretatie" | **opgelost F4** (was onzeker: de bron draagt nu alleen "goede weergave van het vak"; de feiten/interpretatie-zin staat als eigen bewering ná de citatie) | bib-entry bestaat en ziet er intern consistent uit (juiste auteur, jaar, URL-vorm), maar de parafrase van de post zelf is niet extern geverifieerd (LinkedIn niet opgehaald binnen het beurtbudget) | volgende ronde: LinkedIn-URL uit de bib-entry opvragen en de parafrase tegen de brontekst leggen |
| 17 | 525–529 | "meetfout van 4 procentpunt, ongeveer het dubbele van de spreiding van de herschaalde enquêtes bij Greenwood en Shleifer" | **opgelost F4** (was onzeker: bijzin over het dubbele van de GS-spreiding geschrapt, vervangen door verwijzing naar oefening 4) | webzoekopdracht op de GS-paper (2014) leverde geen cijfer op voor de standaarddeviatie van hun herschaalde enquêtereeksen; niet in een cel hier | volgende ronde: tabel 4/5 of de Internet Appendix van Greenwood-Shleifer (2014) raadplegen voor de spreiding van de zes herschaalde reeksen |

**Samenvatting.** Van de ruim vijftig getallen die in de tekst worden aangehaald, komt vrijwel
alles exact overeen met de celuitvoer of met een eenvoudige handberekening (rijen 1–9, 12–15).
Twee open punten uit rapport §F1 zijn met een externe bron opgelost (CAPE-record 1999, rij
10; Martins ondergrens van "boven 20%" klopt inhoudelijk, rij 11), maar de kruisverwijzing
naar 05_29 bij dat laatste cijfer is zelf onjuist: die lecture bespreekt Martins grens
nergens. Twee andere open punten (SantaClara2026-parafrase, GS-spreiding) blijven onzeker bij
gebrek aan toegang tot de brontekst. Het CFO-loader-punt (`# TODO: naar hap.data`) is conform
STYLE §4.6/§5 en telt niet mee.

**open = onjuist(1) + onzeker(2) = 3.**

**F4 (2026-09-30).** Rij 11: link naar 05_29 weg, cijfer staat op {cite}`Martin2017`. Rij 16 en 17 opgelost door herformuleren/schrappen. open = 0.
