STATUS 04_22_risk_management F4 open=0 punten=15

**Werkwijze.** Notebook offline gedraaid (`nb_numbers.py`, `nb_outputs.py`); alle 38 door
`nb_numbers.py` gemelde getallen nagelopen tegen de celuitvoer of nagerekend. Externe bronnen
opgehaald voor de zeven open punten uit `notes/rapport-04_22_risk_management.md` §F1:
`references.bib` (citatiegegevens), BCBS1996b (echte pdf via de link op bis.org/publ/bcbs22.htm,
niet de htm-pagina zelf), het PWG-rapport (`home.treasury.gov/system/files/236/hedgfund.pdf`,
tekst via `pdftotext`) en de Santa-Clara LinkedIn-post.

## Toy-voorbeeld (regel 148–264)

Alle 16 in `hand` vastgelegde getallen (σ_p, VaR's, ES'en, drempels, spiraalronden) staan
letterlijk in de output van cel 2 en komen overeen met de "code"-kolom op afronding na, precies
zoals de tekst zelf meldt ("op de afronding van de spiraal na", regel 266). **Oordeel: juist**
(16 rijen samengevat).

## Theorie (regel 271–702)

| nr | regel | bewering | oordeel | bron/cel | correctie |
|---|---|---|---|---|---|
| 1 | 343–345 | ES-factor 2,665 (α=0,99) en 2,338 (α=0,975); VaR-factor 2,326 | juist | nagerekend: φ(z)/(1−α) met z=Φ⁻¹(α) | — |
| 2 | 517, 1048 | Kupiec-kritieke waarde 3,84 | juist | χ²₁ 95%-kwantiel = 3,841 | — |
| 3 | 582–587 | Basel-tabel: 95,88% bij 5, 99,99% bij 10; Kupiec verwerpt alleen bij 0 of ≥7 | juist | cel 3 (0,9588; 0,9999; LR_pof 5,03/…/5,50) | — |
| 4 | 585 | "model dat 98% dekt, blijft met kans 44% groen" | juist | cel 3, P(X≤4\|p=2%)=1−0,5613=0,4387 | — |
| 5 | 591–592 | standaardfout 0,63 procentpunt bij p=1%, T=250 | juist | nagerekend √(0,01×0,99/250)=0,00629 | — |
| 6 | 1019 | GARCH a=0,092, b=0,905, persistentie 0,997 | juist | cel 10 (0,0921; 0,9047; som 0,9968→0,997) | — |
| 7 | 676–677 | θ=0,625; lineair 33,3 tegen werkelijk 22,0 | juist | nagerekend en cel 2 (spiraal totaal 21,99) | — |

Alle overige toy-samengevatte cijfers uit Theorie (40/80 bp, 160/200 bp bij hefboom 10,
z_{0,99}=2,3263) herhalen het toy-voorbeeld en zijn daar al geverifieerd.

## Simulatie (regel 704–966)

Elk in de tekst genoemd percentage is teruggevonden in cel 4 (8,8%; 46% ≈ 0,458; 15% ≈ 0,152),
cel 6 (Sharpe 0,58; scheefheid −21,5; 27%; mediane Sharpe 0,88/0,66) en cel 7/8 (ruïne 0,2%→11,3%
zonder prijsdruk; 11,3%→23,6% met prijsdruk bij hefboom 25; mediaan eindvermogen 1,57/2,56).
**Oordeel: juist** (12 rijen samengevat).

## Replicatie: VaR-backtest 1990–2026 (regel 968–1143)

| nr | regel | bewering | oordeel | bron/cel | correctie |
|---|---|---|---|---|---|
| 8 | 1048–1053 | Markdown-tabel (3,26/1,63/1,98/2,15; rode jaren 11/2/2/1; LR_ind 27,3/23,9/6,0/4,2) | juist, maar overbodig | letterlijk gelijk aan cel 11 | dit is geen feitenfout maar een §11.9-achtige herhaling van cel 11; overweeg de tabel te laten vervallen of cel 11 als `hide-input` te tonen (stijlpunt, zie lezerrapport) |
| 9 | 1059 | "9211 × 0,0326² ≈ 9,8" tegen 29 waargenomen dagen op rij | juist | cel 11 (9211 dagen, 3,257% fractie, 29,0 dagen twee op rij); nagerekend 9211×0,0326²=9,79 | — |
| **10** | **1073** | **"maar in 2020 zijn juist EWMA en GARCH rood"** | **onjuist** | **cel 12: in 2020 heeft ook "normaal, constant" 23 overschrijdingen (≥10, dus rood) — meer dan EWMA (12) en GARCH (11). Alleen "historisch 250d" (8) is niet rood.** | Herformuleer, bijvoorbeeld: "maar in 2020 worden ook EWMA en GARCH rood, en het statische model nog sterker" — of vermeld expliciet dat het statische model in 2020 eveneens rood is. |
| 11 | 1107–1109 | figuurbijschrift: "Het statische normale model is rood rond 2000 en in 2008" | juist, maar onvolledig | cel 11: "jaren rood" = 11 van de 36 (ook 1998, 1999, 2007, 2009, 2011, 2020, 2022 volgens cel 12) | Geen feitenfout (geen getal genoemd), wel een precisiepunt: zie lezerrapport punt 8. |
| 12 | 1107–1110 | historisch rood in 2008/2022; EWMA in 2007/2020; GARCH in 2020 | juist | cel 12: historisch (15;10), EWMA (10;12), GARCH (11) zijn exact de enige rode jaren per model (cel 11: jaren rood 2/2/1) | — |

## Replicatie: de spreads van 1998 (regel 1145–1237)

| nr | regel | bewering | oordeel | bron/cel | correctie |
|---|---|---|---|---|---|
| 13 | 1188–1193 | Baa +103, Aaa +84, TED +87 bp; ruim zes SD voor bedrijfsobligaties; TED blijft onder drie | juist | cel 15 (103,0; 84,0; 87,0; 6,64; 6,55; 2,94) | — |
| 14 | 68/154–156 | Verwijzing naar het PWG-rapport, p. 12: premies stegen wereldwijd, verliezen groter dan modellen uit rustiger tijden voorspelden | juist | PWG-rapport (pdftotext): "risk spreads and liquidity premiums rose sharply in markets around the world" en "suffered losses in individual markets that greatly exceeded what conventional risk models, estimated during more stable periods, suggested were probable" | — |
| 15 | 1155–1156 | PWG-rapport, p. 16: LTCM wedde dat spreads zouden dalen | juist | PWG-rapport: "It was betting in general that liquidity, credit and volatility spreads would narrow from historically high levels" | — |
| 16 | 95–98 | "Eind augustus 1998 ... meer dan 125 miljard dollar ... 4,8 miljard eigen vermogen begin dat jaar ... hefboom van meer dan 25" | juist | PWG-rapport: "the LTCM Fund's balance sheet on August 31, 1998, included over $125 billion in assets. Even using the January 1, 1998, equity capital figure of $4.8 billion, this level of assets still implies a balance-sheet leverage ratio of more than 25-to-1" | Klopt inhoudelijk; "eind augustus" is een correcte parafrase van 31 augustus. Optioneel preciezer: "31 augustus 1998". |
| 17 | 1232–1236 | 31 juli: 4,1 mld kapitaal; augustus: verlies 1,8 mld; 23 september: consortium van veertien instellingen neemt voor ~3,6 mld 90% over | juist | PWG-rapport, letterlijk: "$4.1 billion in capital" (31 juli), "$1.8 billion" (augustusverlies), "fourteen firms agreed to participate" (23 september), "invested about $3.6 billion in new equity ... received a 90 percent equity stake" | — |
| — | — | Jorion2000 omschreven als "analyse van de risicobeheersing van het fonds" | juist | `references.bib`: titel Jorion (2000) is letterlijk "Risk Management Lessons from Long-Term Capital Management" | — |
| — | — | Edwards1999: bib-entry ongebruikt | klopt (geen feitenpunt) | `grep -n Edwards1999 lectures/04_22_risk_management.md` geeft geen treffer | de auteur kan de entry laten staan (algemene bibliografie) of verwijderen; geen aftrek |
| — | — | "(p. 5)" bij "Het Comité schreef zelf dat zulke toetsen een goed model maar beperkt van een slecht model kunnen onderscheiden" (regel 544–545) | juist, citatie te verfijnen | BCBS1996b (echte pdf), letterlijk op de 5e inhoudspagina (na de ongenummerde titelpagina): "The Committee of course recognises that tests of this type are limited in their power to distinguish an accurate model from an inaccurate model." Dit staat specifiek in BCBS1996b (backtesting-kader), niet in BCBS1996a (amendement kapitaalakkoord). | De zin citeert nu gezamenlijk `{cite}`BCBS1996a,BCBS1996b`` voor de vermenigvuldigingsfactor én deze quote; overweeg de quote apart aan `{cite}`BCBS1996b`` te hangen zodat "(p. 5)" ondubbelzinnig bij het juiste document hoort. |

## Cross-referenties

Alle `[](#…)`-verwijzingen binnen dit college (eq/def/thm/prop/fig/cel-risk-management-\*) wijzen
naar labels die in het bestand zelf bestaan; niets is wees. De vier verwijzingen naar andere
colleges (`#00-01-rendementen`, `#04-19-momentum`, `#04-21-volatiliteit`, `#04-23-behavioral`)
wijzen naar bestaande lectures. **Oordeel: juist.**

## Samenvatting

- Onjuist: 1 (nr. 10, regel 1073 — de belangrijkste bevinding van deze controle).
- Onzeker: 0.
- Niet herleidbaar: 0.
- Overige ~50 gecontroleerde getallen en alle citaties/cross-refs: juist.

`open` (onjuist + onzeker) = 1.

## Status na F4 (2026-09-30)

| nr | status | wat |
|---|---|---|
| 1–7, 9, 12–15, 17, Jorion2000 | juist | ongewijzigd |
| 8 | juist, blijft | tabel hier/juist model is door rubriek (criterium 6) en STYLE §10 verplicht; waarden gelijk aan cel 11 |
| 10 | opgelost | Replicatie: "in 2020 worden ook EWMA en GARCH rood, terwijl het statische model met 23 overschrijdingen nog ver boven hen uitkomt" (cel 12) |
| 11 | opgelost | bijschrift fig-risk-management-jaren: statisch model rood in elf van de 36 jaren, vooral rond 2000, rond 2008 en in 2020 en 2022 (cel 11/12) |
| 16 | opgelost | "Op 31 augustus 1998" |
| Edwards1999 | geen actie | ongebruikte bib-entry, geen aftrek |
| BCBS p. 5 | opgelost | "(p. 5 van {cite}`BCBS1996b`)" |

open=0
