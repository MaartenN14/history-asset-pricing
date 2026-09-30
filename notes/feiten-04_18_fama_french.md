STATUS 04_18_fama_french F4 open=0 punten=15

# Feiten 04_18_fama_french (F23)

`nb_numbers.py` meldt 14 getallen die niet letterlijk in een celuitvoer staan; alle 14 zijn
"origineel"-kolomwaarden uit Fama en French (1992/1993) of eenvoudige tussenstappen. Alle
overige aangehaalde getallen (elke "hier"-kolom, alle simulatie- en toy-uitkomsten) zijn
nagerekend tegen `nb_outputs.py` (16 cellen) en kloppen exact.

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | r147 | SMB-tussenstap "3,333 − 2,000 = 1,333%" | juist | cel 2 (rekenkundig: (2+3+5)/3=3,333; celuitvoer SMB=1,333) | - |
| 2 | r278 | "t = 0,46" (bèta alleen) en "t-waarde van 5,71" (B/M alleen), Fama-MacBeth 1963-1990 | onzeker → opgelost F4: {cite}`FamaFrench1992` bij eerste vermelding (Theorie, FF1992) en 'In hun tabel III' | bron FamaFrench1992, geen cel; extern geprobeerd (WebSearch/WebFetch op de originele PDF), niet machineleesbaar binnen budget; wel intern consistent met tabel III "origineel" r1041/r1043 | citaat toevoegen bij eerste vermelding, of markeren als vooruitgrijpend op tabel III |
| 3 | r255-256 | "3616 van de 4797 aandelen" en "ongeveer 8% van de marktwaarde" (1991) | juist | extern bevestigd via WebSearch (samenvatting van FamaFrench1993: "3616 out of 4797" aandelen, "about 8%" van de gecombineerde waarde in 1991) | - |
| 4 | r272 | "gemiddeld 2267 aandelen" (Fama-MacBeth juli 1963-dec 1990) | onzeker → opgelost F4: {cite}`FamaFrench1992` bij 2267 aandelen | bron FamaFrench1992, geen cel; extern niet gevonden binnen budget | citaat toevoegen of als schatting markeren |
| 5 | r972-977 | Tabel origineel/hier: FF3-alpha klein-groei −0,34(−3,16), groot-groei 0,21(3,27); GRS FF3 1,56(kansniveau 0,961); GRS CAPM 1,91(kansniveau 0,996) — kolom "origineel" | onzeker → afgewezen F4: geciteerde bron (FamaFrench1993, tabel 9a/9c), tekst vermeldt de scan; STYLE staat getallen uit een geciteerde bron toe | bron FamaFrench1993 tabel 9a/9c, tekst zegt zelf "uit een scan overgenomen" (r930); extern niet te verifiëren binnen budget (PDF niet machineleesbaar); kolom "hier" volledig bevestigd tegen cel 9/10 | - (tekst erkent al dat het een scan is) |
| 6 | r1041-1045 | Tabel III origineel-kolom: 0,15(0,46); −0,15(−2,58); 0,50(5,71); −0,37(−1,21); −0,17(−3,41) | onzeker → afgewezen F4: geciteerde bron; tabelinleiding kreeg {cite}`FamaFrench1992` | bron FamaFrench1992 tabel III, gescand; extern niet te verifiëren binnen budget; intern consistent met r278 | - |
| 7 | r924-927, r1138-1139 | "ruim dertig jaar" i.p.v. eerdere "over twintig jaar"; alpha klein-groei −0,47% (t=−5,09), GRS F=3,63 over 1963-2026 | juist | cel 9: periode 1993-01 t/m 2026-07 telt 403 maanden (33,6 jaar); FF3 1963-2026: alpha klein-groei −0,468→−0,47, t=−5,093→−5,09, GRS=3,629→3,63 | - |
| 8 | r980-982 | "Bij het CAPM stijgen de alpha's in bijna elke groottegroep met B/M" (correctie van "elke") | juist | cel 10: groottegroep "4" is niet monotoon (−0,04→−0,10 vóór de stijging), de overige vier rijen wel; "bijna elke" klopt beter dan "elke" | - |
| 9 | r1113-1117 | Figuurbijschrift: "SMB wisselt van teken, met de jaren dertig als sterkste decennium" | onzeker → opgelost F4: bijschrift zegt nu 'van sterk negatief in de onvolledige jaren twintig (vanaf juli 1926) naar positief in de jaren dertig' | cel 12: SMB gem. 1920-1929 = −1,045 (grootste absolute waarde, maar een onvolledig decennium van 42 maanden), 1930-1939 = 0,835 | noem 1930-1939 als sterkste volledige decennium, of vermeld het gedeeltelijke cijfer 1920-1929 apart |
| 10 | r1154-1156 | "Daniel en Titman en Davis, Fama en French kwamen tot tegengestelde conclusies" | juist | intern consistent: r526-528 (Daniel-Titman: kenmerk verklaart, niet de meebeweging) tegenover r530-531 (Davis-Fama-French: het driefactormodel verklaart de premie beter dan het kenmerk) | - |
| 11 | toy (r116-224), Theorie-vergelijkingen, Simulatie (cellen 1-8), Replicatie (cellen 9-16, incl. alle "hier"-kolommen), Oefeningen 1-3 (cellen 14-16) | alle overige aangehaalde cijfers | juist | cel 1 t/m 16 van `nb_outputs.py`: elk getal in r161-220, r608-664 (kalibratietabel, exact gelijk aan code), r688-704, r803-810, r913-918, r949-962 ("hier"), r972-973 ("hier"), r1017-1033 ("hier"), r1041-1045 ("hier"), r1083, r1120-1125, r1184-1186, r1232-1245, r1289-1299 klopt exact met de celuitvoer | - |

**Open = onjuist(0) + onzeker(5) + niet herleidbaar(0) = 5**, rijen 2, 4, 5, 6, 9.

**Na F4: open=0** (rijen 2, 4, 9 opgelost; 5, 6 afgewezen als geciteerde bron).

**Open punten uit rapport §F1, afgehandeld.**
1. Tabel- en Theoriegetallen uit de artikelen: zie rijen 2, 4, 5, 6 hierboven (allemaal onzeker,
   niet machineleesbaar binnen budget); rij 3 (3616/4797/8%) wel extern bevestigd.
2. "Ruim dertig jaar (403 maanden)" en "bijna elke groottegroep": beide juist (rijen 7, 8).
3. Tegengestelde conclusies Daniel-Titman/Davis-Fama-French: juist (rij 10).
4. Nederlandse docstrings: geen getal, geen feitenpunt; buiten scope F23.
