STATUS 05_31_portfolio_choice F4 open=0 punten=15

# Feitencontrole 05_31_portfolio_choice (F23)

Gecontroleerd met `tools/nb_numbers.py` (getallen in de prozategen tegen de
celuitvoer) en `tools/nb_outputs.py` (celuitvoer van het huidige notebook), plus
handmatige narekening van de zes open punten uit `notes/rapport-05_31_portfolio_choice.md`
§F1 en van de vijf citaten zonder cel. Externe bronnen alleen opgehaald voor die
zes open punten (drie NBER-werkpapers, één Yale-PDF, één RFS-PDF); twee daarvan
leverden door PDF-codering geen leesbare tabel op.

## Juiste rijen (samengevat per sectie)

| nr | sectie | bewering | oordeel | bron/cel |
|---|---|---|---|---|
| 1 | Toy (a), r. 128-164 | Alle getallen van de tabel (0,0404; 0,05), de conditionele gewichten (0,09901; 0,40), $\theta$ (0,24950; 0,15050), de matrix (0,0452/0,0048), de determinant (0,00202) en het verwacht nut (0,010495; 0,007965; 0,2655; 0,007965) | juist | cel 2 ("met de hand" = "code" op alle rijen) |
| 2 | Toy (b), r. 213-260 | Marktgewichten, momentum, $\hat x_i$, rendementen, CRRA-nut (−0,25; −0,20964), $r^x=3\%$, $\theta^\ast=0,2167$ | juist | cel 3 |
| 3 | r. 585-586 | "0,36% per jaar" (premie) en "42% idiosyncratische volatiliteit per jaar" | juist | rekenbaar uit LAMBDA=0,0003 en SIG_EPS=0,12 in cel 4 (zichtbare code, niet hide-input): 0,0003·12=0,0036; 0,12·√12=0,4157≈42% |
| 4 | r. 443-450 | "12/√500 ≈ 0,54%" en "factor driehonderd" | juist (afgerond) | rekenbaar uit SIG_EPS=0,12, N=500, N=1000/K=3 in cel 4 |
| 5 | r. 664-667 | Mediane SR MV "tussen 0,09 en 0,15"; N/T "tussen 0,8 en 4" | juist | cel 5 (SR MV: 0,094–0,152; N/T=500/T voor T∈{120,240,360,600}=4,17–0,83, hier ruim afgerond) |
| 6 | r. 704-708 | T=120: P(BSV>1/N)≈helft (0,550), SD θ_size=3,7; T=600: SD θ_size=1,7, BSV wint op SR én CE | juist | cel 5 (SD theta size 3,727/1,684; CE BSV 240=-0,008 vs 1/N -0,002 nvt, T=600: CE BSV 0,008 > CE 1/N 0,003) |
| 7 | r. 821-824 | "$t=-1,8$", size "niet op 5% significant", momentum "ongeveer een halve standaardfout erboven", B/M "1,6 standaardfout erboven", size "verdwijnt"/momentum "blijft" op size-mom | juist | cel 8 (t=-1,798; (2,178-1,772)/0,746=0,54 SE; (4,997-3,606)/0,861=1,62 SE; 25 size/mom: log ME t=-0,132, momentum t=4,164) |
| 8 | r. 882-888 | "bijna drie keer" Sharpe, "180% short", "negen keer" omzet, $\hat\theta=(2,38;19,24;5,31)$ | juist | cel 9 (1,106/0,388=2,85; som neg. w -1,797≈-180%; omzet 8,988≈9,0; theta long-only [2,381 19,243 5,306]) |
| 9 | r. 975-986 (kolom "hier") | Alle tien cijfers van de vergelijkingstabel (θ's, Sharpe/CE in- en buiten steekproef, gewichten, omzet) | juist | cel 8, 9, 11 (elk cijfer rondt exact op de celwaarde) |
| 10 | r. 823, 998 | "standaardfout van ongeveer 0,21" | juist | cel 11, kolom "SE Sharpe" 2003-eind = 0,206 |
| 11 | r. 993-999 | Na 2002: Sharpe 0,62 tegen 0,72; CE 0,9%; 23% vol; 14% overrendement | juist (lost open punt F1 #2 op) | cel 11, "2003-eind, 100 size/BM": parametrisch Sharpe 0,623, CE 0,941, vol 23,105, overrendement 14,399; VW-benchmark Sharpe 0,723 |
| 12 | r. 1074-1075 | "gemiddeld 59% van $V_t$", "autocorrelatie van 0,74" | juist | cel 14 (0,589; 0,741) |
| 13 | r. 1263-1268 | "0,048" omzet benchmark per maand, "0,79%" break-even | juist (lost open punt F1 #6 op) | cel 18: "gem. omzet per maand: policy 0.810, benchmark 0.048"; "break-evenkosten ...: 0.79%" |
| 14 | r. 21 (Jaartal-admonition), r. 50, 52 | "Brandt en Santa-Clara (2006)", "Brandt, Santa-Clara en Valkanov (2009)" | juist (lost open punt F1 #4 op) | references.bib: BrandtSantaClara2006 year=2006, BrandtSantaClaraValkanov2009 year=2009 |
| 15 | r. 543-547 | HKLV: "5,4% per jaar meer" | juist | websearch bevestigt letterlijk "5.4% per year higher" voor laagste-CIV-beta-kwintiel t.o.v. hoogste (Herskovic, Kelly, Lustig, Van Nieuwerburgh 2016) |
| 16 | r. 1288-1345 (oefening 4) | PHI_V=0,74, CORR_RV=-0,31 "ongeveer zoals op de industriedata gemeten" | juist | cel 14: AR(1)=0,741→0,74; corr=-0,309→-0,31 |
| 17 | r. 1300 | `# TODO: naar hap.stats` bij lokale `slope_tstats` | telt niet mee | kaart-rollen §4.6 (vaste uitzondering bij lokale implementatie) |

## Open punten (onjuist / onzeker / niet herleidbaar)

| nr | regel | bewering | oordeel | bron of cel | voorgestelde correctie |
|---|---|---|---|---|---|
| 1 | 969 | Bijschrift fig-portfolio-choice-bsv: "size blijft tot 2003 tussen −1,0 en −1,4 en kruipt daarna naar −0,30, B/M loopt op tot rond 5 en zakt naar 2,7, en momentum blijft tussen 2,2 en 3,2" | onzeker | cel 10 toont maar 5 van de ~53 jaren (1974, 1982, 1990, 2003, 2026); die vijf passen bij de bereiken, maar het volledige pad (dat wél in de figuur staat) is niet uit de celuitvoer te controleren | de printcel uitbreiden met `oos_bm["theta"].agg(["min","max"])` zodat het bijschrift direct herleidbaar is |
| 2 | 348 | "Op elk tijdstip $t$ zijn er $N_t$ aandelen, in het artikel gemiddeld 3.680 per maand" | niet herleidbaar | geen `{cite}`-tag op deze zin, geen cel; context impliceert BrandtSantaClaraValkanov2009 maar dat staat niet in de zin zelf | citatie toevoegen aan de zin, of het getal expliciet aan tabel/tekst van BSV (2009) koppelen |
| 3 | 543-544 | Ang, Hodrick, Xing en Zhang: "een verschil in FF3-alpha van −1,31% per maand ... (werkpaperversie, tabel VI)" | onzeker | NBER-werkpaper w10852 kon niet machine-leesbaar op Tabel VI doorzocht worden (PDF-codering); een losse zoekopdracht suggereert dat "−1,31% per maand" mogelijk uit het latere internationale vervolgartikel van dezelfde auteurs komt (23 markten), niet uit tabel VI van de hier aangehaalde werkpaperversie | de werkpaperversie handmatig nazoeken op tabel VI, of de precisering "tabel VI" laten vallen als het cijfer niet daar staat |
| 4 | 526-528 | Campbell, Lettau, Malkiel en Xu: "de bedrijfsspecifieke component tussen 1962 en 1997 meer dan verdubbelde, terwijl markt- en industriecomponent met ongeveer een derde stegen" | onzeker | NBER-werkpaper w7590 (gedeeltelijk leesbaar): std.dev. individuele aandelen 23%→49% (klopt met "meer dan verdubbeld"), marktvolatiliteit 15%→18% (≈+20% in std.dev., losser bij "een derde"); industriecomponent niet apart te kwantificeren uit de extractie | exacte cijfers (variantie vs. standaarddeviatie) in het artikel nazoeken voordat "een derde" gehandhaafd blijft |
| 5 | 484-486 | Brandt, Santa-Clara en Valkanov: "kosten van 0,5% raken het certainty equivalent nauwelijks" | onzeker | RFS-PDF opgehaald maar niet machine-leesbaar op deze passage (encoding); niet onafhankelijk bevestigd | passage handmatig nazoeken in het artikel (transactiekosten-sectie) |
| 6 | 530 | Goyal en Santa-Clara: "idiosyncratisch risico bijna 85% van de gemiddelde aandeelvariantie" | onzeker, waarschijnlijk juist | directe download van het Yale-PDF mislukte (verbindingsfout); een secundaire bron citeert "idiosyncratic risk ... constitutes 80-85% ... (Goyal & Santa-Clara, 2003)", wat aansluit bij "bijna 85%" | bij gelegenheid het originele artikel alsnog raadplegen ter bevestiging |

## Status na F4 (2026-09-30)

| nr | status | wat |
|---|---|---|
| 1 | opgelost | bijschrift beperkt tot de vijf jaren die cel 10 toont (size −1,0 tot −1,4, 2026 −0,30; B/M 3,5 → 5,2 → 2,7; momentum 2,2–3,2); geen codewijziging |
| 2 | opgelost | `{cite}` BrandtSantaClaraValkanov2009 op de zin met 3.680 |
| 3 | opgelost | precisering "(werkpaperversie, tabel VI)" geschrapt, cijfer aan AHXZ (2006) gelaten |
| 4 | opgelost | "met ongeveer een derde" vervangen door de relatieve bewering "veel sterker steeg dan de markt- en de industriecomponent" |
| 5 | opgelost | kostenbewering vervangen door wat mechanisch volgt: met kosten in het doel kiest de schatter minder omzet en maximaliseert hij het CE na kosten |
| 6 | behouden | secundaire bron geeft 80–85%, sluit aan bij "bijna 85%"; geen correctie nodig |

open = 0.
