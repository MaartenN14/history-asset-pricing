STATUS 04_25_industrie F4 open=0

## Feitentabel

Gecontroleerd: de 6 getallen die `tools/nb_numbers.py` meldde als niet automatisch
gematcht tegen de celuitvoer, plus de vier open punten uit `notes/rapport-04_25_industrie.md`
§F1, plus de cross-refs die in de tekst worden aangehaald. Getallen die `nb_numbers.py`
al wel automatisch matchte tegen `tools/nb_outputs.py` zijn niet opnieuw nagerekend
(buiten scope van deze fase).

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 57–58 | Jensen (1968): fondsen bleven na kosten gemiddeld 1,1% per jaar achter bij de markt | juist | `{cite}`Jensen1968``; extern bevestigd (gerapporteerde gemiddelde alpha netto van kosten = −0,011) | geen |
| 2 | 143 | "dan P met zijn $3{,}9\%$" | juist | cel 2: celuitvoer marktrendement = 4,00%, kosten P = 0,1% (tabel regel 131) ⇒ 3,9%; cel toont zelf al "P netto min X en Y netto" = 0,90, consistent | geen |
| 3 | 261 | French (2008): 0,67% van de marktwaarde per jaar, 1980–2006 | juist | `{cite}`French2008``; extern bevestigd (Presidential Address JoF 2008: gemiddeld 0,67% van de marktwaarde per jaar, 1980–2006) | geen |
| 4 | 622 | "verwachte $t$-waarde $0{,}167\sqrt{240}/1{,}5 \approx 1{,}7$" | juist | rekenkundig uit celconstantes: `alpha_ann=0.02` (10% groep) / 12 = 0,167%/maand; $0{,}167\sqrt{240}/1{,}5 = 1{,}73 \approx 1{,}7$. Cel geeft gerealiseerd gem. $t$ voor "vaardig" = 1,659 (verwacht vs. gerealiseerd, geen tegenspraak) | geen |
| 5 | 949, 1033 | "$-0{,}67\%$" (herhaling van het Frans-cijfer) | juist | zie rij 3 | geen |
| 6 | 1100 | "$2{,}67 - 1 = 1{,}67\%$" | juist | rekenkundig correct; celuitvoer bevestigt de vervolgstap ("netto voorsprong op de index: 1,7667%" ⇒ tekst "1,77 procentpunt" regel 1101) | geen |
| 7 | 412–414 | Berk en Green: ongeveer 80% van de actieve beheerders verdient de eigen vergoeding terug | juist | `{cite}`BerkGreen2004``; extern bevestigd (kalibratie: ~80% van de managers genereert alpha boven de fee) | geen |
| 8 | 417–419 | Berk-Van Binsbergen, versie 2012: gemiddelde beheerder voegt ongeveer 2 miljoen dollar per jaar toe | juist | `{cite}`BerkVanBinsbergen2012`` (NBER WP 18184); extern bevestigd | geen |
| 9 | 590–592 | Barras, Scaillet en Wermers: 75% van de fondsen had na kosten een alpha van nul | **opgelost (F4)**: tekst zegt nu "ongeveer driekwart" | `{cite}`BarrasScailletWermers2010``; extern zoekresultaat gaf een iets andere uitsplitsing (~20% negatief, ~1,9% positief ⇒ impliciet ~78% nul) voor één specifieke schatting uit het artikel; dit is dicht bij 75% maar niet 1-op-1 bevestigd binnen het beurtbudget (kan een andere sub-periode of parameter $(\lambda,\gamma)$ in hetzelfde artikel zijn) | origineel artikel raadplegen op de hoofdschatting $\hat\pi_0$ (netto, volledige steekproef), of voorzichtiger formuleren ("ruim driekwart") |
| 10 | 481–482 | SE-alinea: Sharpe-ratio ≈ 0,14/maand ⇒ term $1+s \approx 1{,}02$ | juist | rekenkundig: $1+0{,}14^2 = 1{,}0196 \approx 1{,}02$ | geen |
| 11 | 24–26 | "zeven bekende fondsen die de hele periode overleefden, haalden geen significante alpha" (verwijzing naar `#02-06-efficiente-markten`) | juist | `lectures/02_06_efficiente_markten.md` (zeven grote actieve fondsen; "geen van de zeven... haalt een $t$ boven 2") | geen |
| 12 | 97–99 | Kyle-$\lambda$-verwijzing naar `#04-24-microstructuur` | juist | `lectures/04_24_microstructuur.md` (Kyle-model, regels 16–90) | geen |
| 13 | 436–437 | Label `#eq-momentum-carhart` | juist | `lectures/04_19_momentum.md` regel 263 (label bestaat) | geen |
| 14 | 863 | Label/inhoud `#02-05-crsp-tape` (survivorship) | juist | `lectures/02_05_crsp_tape.md` regel 14 (label bestaat), inhoud over overlevenden komt overeen | geen |

`open` (onjuist + onzeker + niet herleidbaar) = **0** (rij 9 in F4 voorzichtiger geformuleerd).

Rapport-punt 4 (Samuelson1974, Bogle2007, KosowskiTimmermannWermersWhite2006 niet meer
geciteerd, bib ongewijzigd) is geen feitenfout: ongebruikte bib-entries zijn toegestaan
en tellen niet mee voor `open`.
