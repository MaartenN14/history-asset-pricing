"""Standard asset-pricing estimators used throughout the lectures.

Everything here works on plain :mod:`pandas` objects and returns either a
:class:`pandas.DataFrame` or a small dataclass-like ``dict``.  Return inputs are
assumed to be **decimals per period** (see :mod:`hap.data`); ``freq`` arguments
give the number of periods per year (12 for monthly, 252 for daily).
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats as scipy_stats

__all__ = [
    "PERIODS_PER_YEAR",
    "drawdowns",
    "fama_macbeth",
    "grs_test",
    "hansen_jagannathan_bound",
    "long_horizon_regression",
    "newey_west",
    "sharpe",
    "summary_stats",
    "variance_ratio",
]

PERIODS_PER_YEAR: dict[str, int] = {
    "daily": 252,
    "weekly": 52,
    "monthly": 12,
    "quarterly": 4,
    "annual": 1,
}
"""Annualisation factors keyed by frequency name."""


def _periods(freq: str | int) -> int:
    """Resolve a frequency name or an explicit integer to periods per year."""
    if isinstance(freq, str):
        return PERIODS_PER_YEAR[freq]
    return int(freq)


def _align(y: pd.Series, X: pd.DataFrame | pd.Series) -> tuple[pd.Series, pd.DataFrame]:
    X = pd.DataFrame(X)
    frame = pd.concat([pd.Series(y, name="_y"), X], axis=1, sort=False).dropna()
    return frame["_y"], frame.drop(columns="_y")


def newey_west(
    y: pd.Series,
    X: pd.DataFrame | pd.Series,
    lags: int | None = None,
    add_constant: bool = True,
) -> sm.regression.linear_model.RegressionResults:
    r"""OLS with Newey-West (Bartlett-kernel HAC) standard errors.

    The HAC covariance estimator is

    .. math::

        \hat S = \hat\Gamma_0
            + \sum_{j=1}^{L}\Bigl(1-\tfrac{j}{L+1}\Bigr)
              \bigl(\hat\Gamma_j + \hat\Gamma_j'\bigr),
        \qquad
        \hat\Gamma_j = \tfrac{1}{T}\sum_t u_t u_{t-j} x_t x_{t-j}',

    and :math:`\operatorname{Var}(\hat\beta) = (X'X)^{-1}\hat S T (X'X)^{-1}`.

    Parameters
    ----------
    y : pandas.Series
        Left-hand side variable.
    X : pandas.DataFrame or pandas.Series
        Regressors, *without* an intercept unless ``add_constant=False``.
    lags : int, optional
        Bartlett truncation lag :math:`L`.  ``None`` uses the Newey-West rule of
        thumb :math:`L = \lfloor 4 (T/100)^{2/9} \rfloor`.
    add_constant : bool, default True
        Prepend a column of ones.

    Returns
    -------
    statsmodels.regression.linear_model.RegressionResults
        Fitted results whose ``bse``/``tvalues``/``pvalues`` are HAC-based.

    Examples
    --------
    >>> import numpy as np, pandas as pd
    >>> rng = np.random.default_rng(0)
    >>> x = pd.Series(rng.normal(size=200))
    >>> y = 1.0 + 0.5 * x + pd.Series(rng.normal(size=200))
    >>> res = newey_west(y, x, lags=3)
    >>> bool(abs(res.params.iloc[1] - 0.5) < 0.2)
    True
    """
    y_a, X_a = _align(y, X)
    if add_constant:
        X_a = sm.add_constant(X_a, has_constant="add")
    if lags is None:
        lags = int(np.floor(4 * (len(y_a) / 100.0) ** (2.0 / 9.0)))
    return sm.OLS(y_a, X_a).fit(cov_type="HAC", cov_kwds={"maxlags": max(lags, 0)})


def fama_macbeth(
    returns: pd.DataFrame,
    characteristics: dict[str, pd.DataFrame] | pd.DataFrame,
    lags: int | None = None,
) -> pd.DataFrame:
    r"""Fama-MacBeth (1973) two-pass cross-sectional regression.

    For each date :math:`t` run the cross-sectional OLS

    .. math:: r_{i,t} = \gamma_{0,t} + \sum_k \gamma_{k,t} z_{k,i,t} + e_{i,t},

    then report the time-series average :math:`\bar\gamma_k` with a
    Newey-West standard error of that mean (i.e. HAC on a regression of
    :math:`\gamma_{k,t}` on a constant).  With ``lags=0`` this reduces to the
    classic :math:`\operatorname{se}(\bar\gamma) = \sigma_\gamma/\sqrt{T}`.

    Parameters
    ----------
    returns : pandas.DataFrame
        ``T x N`` panel of test-asset returns (decimals), dates on the index.
    characteristics : dict of str -> pandas.DataFrame, or pandas.DataFrame
        Right-hand-side variables.  Each value is a ``T x N`` panel aligned with
        ``returns`` (e.g. rolling betas, log size).  A single DataFrame is
        treated as one characteristic named ``"x"``.  Time-invariant
        characteristics can be passed as a one-row frame; it is broadcast.
    lags : int, optional
        Newey-West lag for the second stage.  ``None`` uses the rule of thumb.

    Returns
    -------
    pandas.DataFrame
        One row per regressor (``const`` first) with columns ``estimate``
        (average slope per period), ``se``, ``tstat``, ``pvalue`` and
        ``n_periods``.  The per-period slopes are attached as
        ``frame.attrs["gammas"]``.

    Notes
    -----
    Dates with fewer valid assets than regressors are skipped.
    """
    if isinstance(characteristics, pd.DataFrame):
        characteristics = {"x": characteristics}
    names = list(characteristics)

    panels = {}
    for name in names:
        panel = characteristics[name].reindex(columns=returns.columns)
        if len(panel) == 1:
            panel = pd.DataFrame(
                np.repeat(panel.to_numpy(), len(returns), axis=0),
                index=returns.index,
                columns=returns.columns,
            )
        panels[name] = panel.reindex(index=returns.index)

    rows = []
    for date in returns.index:
        block = pd.DataFrame({"ret": returns.loc[date]})
        for name in names:
            block[name] = panels[name].loc[date]
        block = block.dropna()
        if len(block) <= len(names):
            continue
        design = sm.add_constant(block[names], has_constant="add")
        rows.append(
            pd.Series(sm.OLS(block["ret"], design).fit().params, name=date)
        )
    if not rows:
        raise ValueError("No cross-section had enough valid observations.")
    gammas = pd.DataFrame(rows)

    out = []
    for column in gammas.columns:
        series = gammas[column].dropna()
        res = newey_west(series, pd.DataFrame(index=series.index), lags=lags)
        out.append(
            {
                "estimate": float(res.params.iloc[0]),
                "se": float(res.bse.iloc[0]),
                "tstat": float(res.tvalues.iloc[0]),
                "pvalue": float(res.pvalues.iloc[0]),
                "n_periods": int(len(series)),
            }
        )
    frame = pd.DataFrame(out, index=gammas.columns)
    frame.attrs["gammas"] = gammas
    return frame


def grs_test(excess_returns: pd.DataFrame, factors: pd.DataFrame) -> dict[str, float]:
    r"""Gibbons-Ross-Shanken (1989) test that all alphas are jointly zero.

    Estimate :math:`r_{i,t} = \alpha_i + \beta_i' f_t + \varepsilon_{i,t}` and test
    :math:`H_0:\alpha = 0` with

    .. math::

        \mathrm{GRS} = \frac{T-N-K}{N}
            \bigl(1 + \bar f' \hat\Omega^{-1} \bar f\bigr)^{-1}
            \hat\alpha' \hat\Sigma^{-1} \hat\alpha
        \;\sim\; F(N,\;T-N-K),

    where :math:`\hat\Sigma` is the residual covariance matrix and
    :math:`\hat\Omega` the factor covariance matrix (both ML, divisor ``T``).

    Parameters
    ----------
    excess_returns : pandas.DataFrame
        ``T x N`` test-asset **excess** returns (decimals).
    factors : pandas.DataFrame
        ``T x K`` factor returns (excess or long-short), same index.

    Returns
    -------
    dict
        ``grs`` (statistic), ``pvalue``, ``df1`` = N, ``df2`` = T-N-K,
        ``mean_abs_alpha`` (per period) and ``sh2_alpha``
        (:math:`\hat\alpha'\hat\Sigma^{-1}\hat\alpha`, the squared Sharpe
        ratio of the alpha-implied portfolio).

    Notes
    -----
    Requires ``T > N + K``; with the French 25 portfolios and FF3 this holds
    comfortably for any post-1963 monthly sample.
    """
    data = pd.concat([excess_returns, factors], axis=1, sort=False).dropna()
    R = data[excess_returns.columns].to_numpy(float)
    F = data[factors.columns].to_numpy(float)
    T, N = R.shape
    K = F.shape[1]
    if T <= N + K:
        raise ValueError(f"GRS needs T > N + K; got T={T}, N={N}, K={K}.")

    X = np.column_stack([np.ones(T), F])
    coef, *_ = np.linalg.lstsq(X, R, rcond=None)
    alpha = coef[0]
    resid = R - X @ coef
    Sigma = resid.T @ resid / T
    f_bar = F.mean(axis=0)
    Omega = np.cov(F, rowvar=False, bias=True).reshape(K, K)

    sh2_alpha = float(alpha @ np.linalg.solve(Sigma, alpha))
    sh2_f = float(f_bar @ np.linalg.solve(Omega, f_bar))
    grs = (T - N - K) / N * sh2_alpha / (1.0 + sh2_f)
    return {
        "grs": grs,
        "pvalue": float(scipy_stats.f.sf(grs, N, T - N - K)),
        "df1": N,
        "df2": T - N - K,
        "mean_abs_alpha": float(np.abs(alpha).mean()),
        "sh2_alpha": sh2_alpha,
    }


def long_horizon_regression(
    y: pd.Series,
    x: pd.Series,
    horizons: list[int] | tuple[int, ...] = (1, 3, 12, 24, 60),
    method: str = "hansen-hodrick",
) -> pd.DataFrame:
    r"""Overlapping long-horizon predictive regressions.

    For each horizon :math:`h` regress the cumulative future value
    :math:`y_{t+1} + \dots + y_{t+h}` on :math:`x_t`.  Overlapping windows make
    the residuals MA(h-1), so standard errors use ``h - 1`` lags:

    ``"hansen-hodrick"``
        Hansen-Hodrick (1980): unweighted (rectangular kernel) HAC, the classic
        choice in Fama-French (1988).  Can be non-positive-definite.
    ``"newey-west"``
        Bartlett-weighted HAC, always positive semi-definite.

    Parameters
    ----------
    y : pandas.Series
        Variable being cumulated, e.g. monthly excess returns (decimals).
    x : pandas.Series
        Predictor observed at ``t``, e.g. the log dividend-price ratio.
    horizons : sequence of int, default (1, 3, 12, 24, 60)
        Horizons :math:`h` in periods of ``y``.
    method : {"hansen-hodrick", "newey-west"}, default "hansen-hodrick"

    Returns
    -------
    pandas.DataFrame
        Indexed by horizon, with columns ``beta``, ``se``, ``tstat``, ``r2``
        and ``nobs``.

    Notes
    -----
    Slope and :math:`R^2` typically rise roughly linearly with :math:`h`, which
    is mostly an artefact of overlap rather than independent evidence; see the
    Stambaugh-bias and Boudoukh-Richardson-Whitelaw discussion in the lecture on
    return predictability.
    """
    kernel = {"hansen-hodrick": "uniform", "newey-west": "bartlett"}[method]
    rows = []
    for h in horizons:
        cumulative = y.rolling(h).sum().shift(-h)
        frame = pd.concat(
            [cumulative.rename("y"), x.rename("x")], axis=1, sort=False
        ).dropna()
        design = sm.add_constant(frame[["x"]], has_constant="add")
        fit = sm.OLS(frame["y"], design).fit(
            cov_type="HAC",
            cov_kwds={"maxlags": max(h - 1, 0), "kernel": kernel, "use_correction": True},
        )
        rows.append(
            {
                "beta": float(fit.params.iloc[1]),
                "se": float(fit.bse.iloc[1]),
                "tstat": float(fit.tvalues.iloc[1]),
                "r2": float(fit.rsquared),
                "nobs": int(fit.nobs),
            }
        )
    return pd.DataFrame(rows, index=pd.Index(list(horizons), name="horizon"))


def variance_ratio(r: pd.Series, q: int, overlapping: bool = True) -> dict[str, float]:
    r"""Lo-MacKinlay (1988) variance ratio test.

    .. math::

        VR(q) = \frac{\operatorname{Var}(r_t + \dots + r_{t-q+1})}
                      {q\,\operatorname{Var}(r_t)} .

    Under a random walk :math:`VR(q) = 1`.  With overlapping observations and
    the unbiased estimators of Lo-MacKinlay, the homoskedastic test statistic is

    .. math::

        z_1 = \frac{VR(q)-1}{\sqrt{\tfrac{2(2q-1)(q-1)}{3qT}}},

    and the heteroskedasticity-robust version replaces the denominator by
    :math:`\sqrt{\sum_{j=1}^{q-1}\bigl(2(q-j)/q\bigr)^2 \hat\delta_j}` with

    .. math::

        \hat\delta_j = \frac{\sum_t (r_t-\hat\mu)^2 (r_{t-j}-\hat\mu)^2}
                               {\bigl(\sum_t (r_t-\hat\mu)^2\bigr)^2}.

    Parameters
    ----------
    r : pandas.Series
        Log returns (the test is defined for a random walk in logs).
    q : int
        Aggregation horizon, ``q >= 2``.
    overlapping : bool, default True
        Use overlapping ``q``-period sums (the efficient Lo-MacKinlay version).

    Returns
    -------
    dict
        ``vr``, ``z1`` (homoskedastic), ``z2`` (heteroskedasticity-robust),
        ``pvalue`` (two-sided, based on ``z2``) and ``nobs``.

    Examples
    --------
    An i.i.d. series has a variance ratio near one:

    >>> import numpy as np, pandas as pd
    >>> r = pd.Series(np.random.default_rng(1).normal(size=5000))
    >>> bool(abs(variance_ratio(r, 4)["vr"] - 1) < 0.1)
    True
    """
    if q < 2:
        raise ValueError("q must be at least 2.")
    x = pd.Series(r).dropna().to_numpy(float)
    T = len(x)
    mu = x.mean()
    var_1 = ((x - mu) ** 2).sum() / (T - 1)

    if overlapping:
        sums = np.convolve(x, np.ones(q), mode="valid")
        m = q * (T - q + 1) * (1 - q / T)
        var_q = ((sums - q * mu) ** 2).sum() / m
    else:
        n_blocks = T // q
        sums = x[: n_blocks * q].reshape(n_blocks, q).sum(axis=1)
        var_q = ((sums - q * mu) ** 2).sum() / (q * (n_blocks - 1))

    vr = var_q / var_1
    z1 = (vr - 1) / np.sqrt(2.0 * (2 * q - 1) * (q - 1) / (3.0 * q * T))

    dev2 = (x - mu) ** 2
    denom = dev2.sum() ** 2
    theta = 0.0
    for j in range(1, q):
        delta = (dev2[j:] * dev2[:-j]).sum() * T / denom
        theta += (2.0 * (q - j) / q) ** 2 * delta
    z2 = (vr - 1) / np.sqrt(theta / T) if theta > 0 else np.nan
    return {
        "vr": float(vr),
        "z1": float(z1),
        "z2": float(z2),
        "pvalue": float(2 * scipy_stats.norm.sf(abs(z2))),
        "nobs": T,
    }


def hansen_jagannathan_bound(
    returns: pd.DataFrame, mean_m: np.ndarray | None = None
) -> pd.DataFrame:
    r"""Hansen-Jagannathan (1991) bound on the volatility of the SDF.

    Any stochastic discount factor that prices the gross returns :math:`R` must
    satisfy, for a given mean :math:`E[m]`,

    .. math::

        \sigma(m) \;\ge\;
        \sqrt{\bigl(\mathbf 1 - E[m]\,E[R]\bigr)'\,\Sigma_R^{-1}\,
               \bigl(\mathbf 1 - E[m]\,E[R]\bigr)},

    with :math:`\Sigma_R` the covariance matrix of the gross returns.  For a
    single excess return this collapses to the familiar
    :math:`\sigma(m)/E[m] \ge |E[r^e]|/\sigma(r^e)`, the Sharpe ratio bound.

    Parameters
    ----------
    returns : pandas.DataFrame
        ``T x N`` **gross** returns (i.e. ``1 + r``), decimals.
    mean_m : numpy.ndarray, optional
        Grid of candidate :math:`E[m]`.  Default: 50 points spanning roughly
        one over the gross return range, which brackets plausible discount
        factors.

    Returns
    -------
    pandas.DataFrame
        Columns ``mean_m`` and ``sigma_m_min``, one row per grid point.

    Notes
    -----
    Divide ``sigma_m_min`` by ``mean_m`` to read the bound as a maximum Sharpe
    ratio, the form used in the Mehra-Prescott equity premium lecture.
    """
    R = returns.dropna().to_numpy(float)
    ER = R.mean(axis=0)
    Sigma = np.cov(R, rowvar=False, bias=False).reshape(R.shape[1], R.shape[1])
    if mean_m is None:
        centre = 1.0 / ER.mean()
        mean_m = np.linspace(0.90 * centre, 1.05 * centre, 50)
    ones = np.ones(R.shape[1])
    inv = np.linalg.pinv(Sigma)
    sigma = [
        float(np.sqrt(max((ones - m * ER) @ inv @ (ones - m * ER), 0.0)))
        for m in mean_m
    ]
    return pd.DataFrame({"mean_m": np.asarray(mean_m, float), "sigma_m_min": sigma})


def sharpe(r: pd.Series | pd.DataFrame, freq: str | int = "monthly") -> Any:
    r"""Annualised Sharpe ratio of an **excess** return series.

    .. math:: SR = \sqrt{f}\;\frac{\bar r}{\hat\sigma(r)},

    with :math:`f` periods per year.  The :math:`\sqrt{f}` scaling assumes
    i.i.d. returns; with autocorrelation it overstates (positive AR) or
    understates (negative AR) the true annual Sharpe ratio.

    Parameters
    ----------
    r : pandas.Series or pandas.DataFrame
        Excess returns per period, decimals.
    freq : str or int, default "monthly"
        Key of :data:`PERIODS_PER_YEAR` or an explicit number of periods.

    Returns
    -------
    float or pandas.Series
        Scalar for a Series, one value per column for a DataFrame.
    """
    periods = _periods(freq)
    return np.sqrt(periods) * r.mean() / r.std()


def drawdowns(r: pd.Series) -> pd.DataFrame:
    r"""Cumulative wealth, running peak and drawdown of a return series.

    With :math:`W_t = \prod_{s\le t}(1+r_s)` and :math:`M_t = \max_{s\le t} W_s`,
    the drawdown is :math:`D_t = W_t/M_t - 1 \le 0`.

    Parameters
    ----------
    r : pandas.Series
        Simple returns per period, decimals.

    Returns
    -------
    pandas.DataFrame
        Columns ``wealth``, ``peak`` and ``drawdown``, same index as ``r``.
        The worst drawdown and its date are in
        ``frame.attrs["max_drawdown"]`` and ``frame.attrs["trough"]``.
    """
    series = pd.Series(r).dropna()
    wealth = (1.0 + series).cumprod()
    peak = wealth.cummax()
    frame = pd.DataFrame({"wealth": wealth, "peak": peak, "drawdown": wealth / peak - 1.0})
    frame.attrs["max_drawdown"] = float(frame["drawdown"].min())
    frame.attrs["trough"] = frame["drawdown"].idxmin()
    return frame


def summary_stats(
    df: pd.DataFrame | pd.Series, freq: str | int = "monthly"
) -> pd.DataFrame:
    r"""Descriptive statistics for return series, per period and annualised.

    The standard error of the mean is :math:`\hat\sigma/\sqrt{T}`; annualised
    it is :math:`\hat\sigma\sqrt{f}/\sqrt{T}` — the "2% standard error" that
    runs through these lectures.

    Parameters
    ----------
    df : pandas.DataFrame or pandas.Series
        Returns per period, decimals.
    freq : str or int, default "monthly"
        Key of :data:`PERIODS_PER_YEAR` or an explicit number of periods.

    Returns
    -------
    pandas.DataFrame
        One row per column of ``df``, with columns:
        ``nobs``, ``mean``, ``std``, ``se_mean`` (per period);
        ``mean_ann`` (:math:`f\bar r`), ``std_ann`` (:math:`\sqrt f \hat\sigma`),
        ``se_mean_ann``, ``sharpe_ann``; ``skew``, ``kurtosis`` (excess),
        ``min``, ``max``, ``start`` and ``end``.
    """
    frame = df.to_frame() if isinstance(df, pd.Series) else df
    periods = _periods(freq)
    rows = {}
    for name in frame.columns:
        series = frame[name].dropna()
        n = len(series)
        mean, std = series.mean(), series.std()
        se = std / np.sqrt(n) if n else np.nan
        rows[name] = {
            "nobs": n,
            "mean": mean,
            "std": std,
            "se_mean": se,
            "mean_ann": periods * mean,
            "std_ann": np.sqrt(periods) * std,
            "se_mean_ann": periods * se,
            "sharpe_ann": np.sqrt(periods) * mean / std if std else np.nan,
            "skew": series.skew(),
            "kurtosis": series.kurtosis(),
            "min": series.min(),
            "max": series.max(),
            "start": series.index.min(),
            "end": series.index.max(),
        }
    return pd.DataFrame(rows).T
