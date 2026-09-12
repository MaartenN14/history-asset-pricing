# Voortgang lectures (stand 2026-09-12)

Bedoeld om na een onderbreking (tokenlimiet) het werk op te pakken, ook vanuit een nieuwe sessie.

## Gecommit en gecontroleerd (offline uitgevoerd)

L0, L1, L2, L3, L4, L5, L6, L7, L10.

## In bouw bij een agent op het moment van schrijven

| Lecture | Bestand | Stand op schijf |
|---|---|---|
| L8 CAPM | `lectures/02_08_capm.md` | gedeeltelijk of volledig geschreven |
| L9 Black-Scholes | `lectures/02_09_black_scholes.md` | gedeeltelijk of volledig geschreven |
| L11 APT/no-arbitrage | `lectures/03_11_apt_no_arbitrage.md` | gedeeltelijk of volledig geschreven |
| L12 Consumptie-CAPM | `lectures/03_12_consumptie_capm.md` | gedeeltelijk of volledig geschreven |
| L13 Equity premium puzzle | `lectures/03_13_equity_premium_puzzle.md` | mogelijk nog niet aanwezig |
| L14 Roll | `lectures/03_14_roll.md` | mogelijk nog niet aanwezig |
| L15 Shiller excess volatility | `lectures/03_15_shiller_excess_volatility.md` | mogelijk nog niet aanwezig |
| L16 Vroege anomalieën | `lectures/03_16_vroege_anomalieen.md` | mogelijk nog niet aanwezig |

## Hervatten

- **Zelfde sessie:** de gestopte agents worden hervat vanuit hun eigen transcript; hun bronnenonderzoek blijft behouden.
- **Nieuwe sessie:** start per lecture uit de tabel een bouw-agent met BOUW.md en de opdracht "rond af wat op schijf staat, anders bouw volgens PLAN.md §3". Controleer eerst `git status` voor ongecommitte bestanden en cachebestanden.
- Ongecommitte wijzigingen in `myst.yml`, `references.bib` en `data/cache/` horen bij deze lectures; commit ze samen met de betreffende lecture.

## Openstaande punten

- Lengte: meerdere lectures (L2, L7, L8, L10) liggen boven de richtlijn van 6000 woorden. Beslissing gebruiker nodig: inkorten of accepteren.
- Volledige sitebuild aan het eind van de batch opnieuw draaien; parallelle builds van agents botsen in `_build/`.
- Kandidaten voor `hap.stats`: runs-test (L2), event-study-toetsen (L7), VAR-schatter (L10), Sharpe-ratio-toets en rollende backtest (L4). Loader voor splitsingen/dividenden in `hap.data.yahoo` (L7).
