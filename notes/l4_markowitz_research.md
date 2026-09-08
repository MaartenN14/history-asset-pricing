# Onderzoeksnotitie L4 (Markowitz/Roy/Tobin) — geverifieerde bronnen

Opgeleverd door een research-subagent van de (gestopte) L4-bouwagent, 2026-09-07. Bedoeld voor hergebruik bij het
hervatten van L4. Alles hieronder is via Crossref of primaire PDF's geverifieerd tenzij gemarkeerd **ONGEVERIFIEERD**.

## Bib-entries (geverifieerd)

```bibtex
@article{Markowitz1952, author={Markowitz, Harry}, title={Portfolio Selection}, journal={The Journal of Finance}, volume={7}, number={1}, pages={77--91}, year={1952}, doi={10.1111/j.1540-6261.1952.tb01525.x}}
@book{Markowitz1959, author={Markowitz, Harry M.}, title={Portfolio Selection: Efficient Diversification of Investments}, publisher={John Wiley \& Sons}, series={Cowles Foundation Monograph No. 16}, year={1959}}
@article{Roy1952, author={Roy, A. D.}, title={Safety First and the Holding of Assets}, journal={Econometrica}, volume={20}, number={3}, pages={431--449}, year={1952}, doi={10.2307/1907413}}
@article{Tobin1958, author={Tobin, James}, title={Liquidity Preference as Behavior Towards Risk}, journal={The Review of Economic Studies}, volume={25}, number={2}, pages={65--86}, year={1958}, doi={10.2307/2296205}}
@article{Michaud1989, author={Michaud, Richard O.}, title={The {M}arkowitz Optimization Enigma: Is 'Optimized' Optimal?}, journal={Financial Analysts Journal}, volume={45}, number={1}, pages={31--42}, year={1989}, doi={10.2469/faj.v45.n1.31}}
@article{DeMiguelGarlappiUppal2009, author={DeMiguel, Victor and Garlappi, Lorenzo and Uppal, Raman}, title={Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?}, journal={The Review of Financial Studies}, volume={22}, number={5}, pages={1915--1953}, year={2009}, doi={10.1093/rfs/hhm075}}
@article{JobsonKorkie1980, author={Jobson, J. D. and Korkie, B.}, title={Estimation for Markowitz Efficient Portfolios}, journal={Journal of the American Statistical Association}, volume={75}, number={371}, pages={544--554}, year={1980}, doi={10.1080/01621459.1980.10477507}}
@article{JobsonKorkie1981, author={Jobson, J. D. and Korkie, Robert M.}, title={Putting {M}arkowitz theory to work}, journal={The Journal of Portfolio Management}, volume={7}, number={4}, pages={70--74}, year={1981}, doi={10.3905/jpm.1981.408816}}
@article{BestGrauer1991, author={Best, Michael J. and Grauer, Robert R.}, title={On the Sensitivity of Mean-Variance-Efficient Portfolios to Changes in Asset Means: Some Analytical and Computational Results}, journal={The Review of Financial Studies}, volume={4}, number={2}, pages={315--342}, year={1991}, doi={10.1093/rfs/4.2.315}}
@article{ChopraZiemba1993, author={Chopra, Vijay Kumar and Ziemba, William T.}, title={The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice}, journal={The Journal of Portfolio Management}, volume={19}, number={2}, pages={6--11}, year={1993}, doi={10.3905/jpm.1993.409440}}
@article{Markowitz1999, author={Markowitz, Harry M.}, title={The Early History of Portfolio Theory: 1600--1960}, journal={Financial Analysts Journal}, volume={55}, number={4}, pages={5--16}, year={1999}, doi={10.2469/faj.v55.n4.2281}}
```

## DeMiguel-Garlappi-Uppal 2009 — cijfers uit de primaire tekst

- Abstract: "Of the fourteen models ... across seven empirical datasets, none is consistently better than the 1/N rule" (Sharpe, CEQ, turnover).
- Benodigde schattingsvenster om 1/N te verslaan (gekalibreerd op VS): N=25 → >3000 maanden; N=50 → >6000 maanden; in de praktijk M=120 (robuustheid M=60).
- Tabel 3 Sharpe-ratio's (1/N | mv in-sample | mv out-of-sample): S&P Sectors N=11: 0,1876 | 0,3848 | 0,0794. International N=9: 0,1277 | 0,2090 | −0,0719. FF-4-factor N=24: 0,1753 | 0,5364 | −0,0031.
- Zeven datasets: S&P sectors (N=11, 1981-01–2002-12), Industry (N=11, 1963-07–2004-11), International (N=9, 1970-01–2001-07), MKT/SMB/HML (N=3), FF-1/3/4-factor (N=21/23/24, 1963-07–2004-11, French-website).

## Chopra-Ziemba 1993

- Goed bevestigd via twee onafhankelijke secundaire bronnen: bij risicotolerantie 50 zijn cash-equivalent-verliezen ~11× gevoeliger voor fouten in gemiddelden dan in varianties, ~21× dan in covarianties.
- **ONGEVERIFIEERD**: de decimale tabel (RT25: 3,22/5,38/1,67; RT50: 10,98/22,50/2,05; RT75: 21,42/56,84/2,68) — alleen uit een AI-zoekantwoord; niet citeren zonder de originele tabel te checken.

## Roy 1952

- Safety-first: minimaliseer P(R < d); via Bienaymé-Tchebycheff-ongelijkheid reduceert dat tot maximaliseren van (E[R]−d)/σ. Mechanisme goed bevestigd; letterlijke notatie uit Econometrica niet gezien.
- Prioriteit: Markowitz JF maart 1952, Roy Econometrica juli 1952. Markowitz 1999 (FAJ): "Roy (1952) can claim an equal share of this honor" — via twee secundaire bronnen, niet primair geverifieerd.

## Tobin 1958

- Separatiestelling: samenstelling van de risicovolle portefeuille onafhankelijk van risicoaversie; alleen de verdeling veilig/risicovol verschilt. Letterlijke formulering niet uit primaire tekst.

## Friedman-anekdote (geverifieerd)

Klein, Daza & Mead, *Econ Journal Watch* 10(3), 2013, pp. 440–443, citeert Markowitz (1991 herdruk van 1959, Blackwell, p. 382): Friedman: "I've read your dissertation and can't find any mistakes in it. There is just one problem: this is not a dissertation in economics. We cannot award you a Ph.D. in economics for a dissertation that is not economics." Markowitz kreeg de graad die dag. Bernstein's *Capital Ideas*-versie ("it's not even business administration") is een **ongeverifieerde** parafrase — niet gebruiken.
