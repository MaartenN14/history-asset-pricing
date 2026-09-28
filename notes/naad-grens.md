# Naad: efficiënte grens en minimum-variantierand (na ronde 9+)

Scripts: `$TEMP/naad-grens-<slug>.py` (exacte vervangingen, elk met `count == 1`-assert).
Na afloop komt "rand" in de drie colleges alleen nog voor in "minimum-variantierand".
Controles: prose_stats `--check` PASS (alle drie), nb_numbers alleen regelverschuivingen
(02_08 +2, 03_14 +1, geen nieuwe meldingen), `jupytext --sync` gedaan. 01_04 offline
opnieuw uitgevoerd: in nb_outputs verschillen alleen het tabellabel
("standaarddeviatie op de grens bij 10%", met een kolom breder) en de PNG (legenda en titel).

## 01_04_markowitz (25 vervangingen)

- **Efficiënte grens**: Doelen (r47), kopje "Het kernresultaat: de efficiënte grens"
  (r276, geen verwijzingen naar het kopje gevonden), de keuze van de belegger (r279, r283),
  "veilige portefeuilles op de efficiënte grens" (r540), "kapitaalmarktlijn boven de
  efficiënte grens" (r613), Roys punt (r656), de waarschuwing "De geschatte efficiënte grens" (r760).
  Tabellabel in code: "standaarddeviatie op de grens bij 10%" (10% ligt boven B/A = 5,51%).
- **Minimum-variantierand ingezet** (hele parabool): definitie r97 (nu: laagste variantie per
  rendement = minimum-variantierand, het bovenste deel is de *efficiënte grens*, *efficient
  frontier*), "de minimum-variantierand is een parabool" (r234 en Samengevat r774),
  r283 (de ruil stopt op de minimum-variantierand, de smaak kiest het punt op de efficiënte grens),
  "Om de minimum-variantierand te tekenen" (r334; het grid 2–16% loopt onder de
  minimum-variantieportefeuille door), tweefondsenstelling (r427–428, α ∈ ℝ) en
  "Welke twee portefeuilles van de minimum-variantierand" (r435), bewijsstap 2 (r462),
  figuurproza, legenda en titel (r568–609; de getekende curve is de hele parabool),
  oefening zero-beta (r1276, r1279: μ_z = R^f = 2% ligt onder 5,51%, dus op het ondoelmatige
  deel) en uitwerking r1327.

## 02_08_capm (11 vervangingen, 12 treffers)

- Alias "(hierna kortweg de rand)" op r43 geschrapt.
- **Efficiënte grens**: kopje r346 "Wat het voorspelt: de markt ligt op de efficiënte grens",
  theorema van Black r394 (elke belegger houdt een portefeuille op de efficiënte grens),
  r407 (gemiddelde van grensportefeuilles ligt op de efficiënte grens), bewijsstap 1 (kop en
  r416), stap 2 (r421), GRS r514 en r1065, GRS-bewijsstap 1 r525.
- **Minimum-variantierand**: bestaande treffers r395, r408, r421 (eerste-ordevoorwaarde),
  r431, r433 ongewijzigd; in stap 1 ingezet (tweefondsenstelling geeft de minimum-variantierand).
- **Controle zero-beta**: stap 1 zei eerst alleen "op de rand" via de tweefondsenstelling.
  Toegevoegd: omdat de gewichten positief zijn, is het verwachte rendement van de markt een
  gemiddelde van rendementen boven dat van de minimum-variantieportefeuille, dus ligt de markt
  op de efficiënte grens. Daarmee is de premisse van stap 3 ("de markt ligt op het doelmatige
  deel") onderbouwd. Stap 3 en het theorema plaatsen z op de minimum-variantierand, op het
  ondoelmatige deel onder de minimum-variantieportefeuille: klopt.
- Let op: r512–514 gebruiken "grens" ook voor de kritieke waarde van de F-toets; de
  efficiënte grens is daar altijd voluit geschreven.

## 03_14_roll (22 vervangingen)

- **Afspraak** Overzicht (r40–42): uitgebreid met "zodat de efficiënte grens hier de hele
  minimum-variantierand is". Opzet (r263–264): "heet elke portefeuille op de
  minimum-variantierand efficiënt, ook het deel onder de minimum-variantieportefeuille,
  zodat de grens de hele parabool is". "De grens" en "grensportefeuille" betekenen in dit
  college dus bewust de hele parabool, in lijn met 01_04 en 02_08 via deze expliciete afspraak.
- **Grens / grensportefeuille** (hele parabool volgens de afspraak): r140, r145, r151, r227,
  r260, r270, r272, r276, r297, r302, r304 ("grensvorm"), bewijsstappen 1 en 2 (kop en tekst),
  r368, r428 (Roll en Ross, "binnen de grens"), r812.
- **Minimum-variantierand ingezet** waar de stelling zelf wordt geformuleerd: r138 (A, B, C, D
  leggen de minimum-variantierand vast), Theorie-intro r233, conclusie van het bewijs r330,
  Samengevat r657. Bestaande treffers r40, r45, r72, r258, r282 (de stelling van Roll) ongewijzigd.
- **Controle Roll**: de stelling (μ_p ≠ B/A, p op de minimum-variantierand ⇔ exacte lijn met
  b ≠ 0) geldt op beide takken; overal waar ze wordt samengevat staat nu minimum-variantierand
  of "de grens" onder de afspraak. Klopt.

## Open punt

STYLE.md §3 (r248) noemt als voorkeur ook "minimum-variantiegrens" in plaats van
"minimum-variantierand". Op instructie is "minimum-variantierand" overal blijven staan als eigen
begrip; STYLE.md en de colleges spreken elkaar hierin dus nog tegen.
