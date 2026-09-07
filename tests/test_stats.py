"""Tests for :mod:`hap.stats`, against simulations and cached French data."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
import statsmodels.api as sm

import hap
from hap import stats


@pytest.fixture(scope="module")
def ff3():
    return hap.french("F-F_Research_Data_Factors").loc["1963-07":]


@pytest.fixture(scope="module")
def p25(ff3):
    portfolios = hap.french("25_Portfolios_5x5").loc["1963-07":]
    return portfolios.sub(ff3["RF"], axis=0).dropna()


def test_newey_west_recovers_slope():
    rng = np.random.default_rng(0)
    x = pd.Series(rng.normal(size=500))
    y = 1.0 + 0.5 * x + pd.Series(rng.normal(size=500))
    res = stats.newey_west(y, x, lags=4)
    assert res.params.iloc[1] == pytest.approx(0.5, abs=0.1)
    assert res.cov_type == "HAC"
    # HAC standard errors differ from OLS but stay in the same ballpark.
    ols = sm.OLS(y, sm.add_constant(pd.DataFrame(x))).fit()
    assert 0.5 < res.bse.iloc[1] / ols.bse.iloc[1] < 2.0


def test_newey_west_default_lag_runs():
    rng = np.random.default_rng(1)
    y = pd.Series(rng.normal(size=300))
    res = stats.newey_west(y, pd.DataFrame(index=y.index))
    assert res.params.shape == (1,)


def test_variance_ratio_iid_is_one():
    rng = np.random.default_rng(2)
    r = pd.Series(rng.normal(size=20_000))
    for q in (2, 4, 12):
        out = stats.variance_ratio(r, q)
        assert out["vr"] == pytest.approx(1.0, abs=0.06)
        assert abs(out["z1"]) < 3.0
        assert abs(out["z2"]) < 3.0


def test_variance_ratio_detects_positive_autocorrelation():
    rng = np.random.default_rng(3)
    e = rng.normal(size=20_000)
    x = np.zeros_like(e)
    for t in range(1, len(e)):
        x[t] = 0.3 * x[t - 1] + e[t]
    out = stats.variance_ratio(pd.Series(x), 4)
    assert out["vr"] > 1.2
    assert out["z2"] > 3.0
    assert out["pvalue"] < 0.01


def test_variance_ratio_requires_q_at_least_two():
    with pytest.raises(ValueError, match="at least 2"):
        stats.variance_ratio(pd.Series([0.1, 0.2, 0.3]), 1)


def test_grs_on_ff3_and_the_25_portfolios(ff3, p25):
    out = stats.grs_test(p25, ff3[["Mkt-RF", "SMB", "HML"]])
    assert out["df1"] == 25
    assert out["df2"] == len(p25) - 25 - 3
    assert 1.0 < out["grs"] < 10.0  # FF3 is rejected on the 25 portfolios
    assert out["pvalue"] < 0.05
    assert out["mean_abs_alpha"] < 0.01  # under 1% per month
    assert out["sh2_alpha"] > 0


def test_grs_zero_alpha_is_not_rejected():
    rng = np.random.default_rng(4)
    T, N = 600, 10
    f = pd.DataFrame(rng.normal(0.005, 0.04, size=(T, 1)), columns=["f"])
    beta = rng.uniform(0.5, 1.5, size=N)
    R = pd.DataFrame(
        f["f"].to_numpy()[:, None] * beta + rng.normal(0, 0.05, size=(T, N)),
        columns=[f"p{i}" for i in range(N)],
    )
    out = stats.grs_test(R, f)
    assert out["pvalue"] > 0.01


def test_grs_needs_enough_observations():
    frame = pd.DataFrame(np.random.default_rng(5).normal(size=(10, 25)))
    with pytest.raises(ValueError, match="T > N \\+ K"):
        stats.grs_test(frame, frame.iloc[:, :1])


def test_fama_macbeth_prices_market_beta(ff3, p25):
    window = 60
    betas = pd.DataFrame(index=p25.index, columns=p25.columns, dtype=float)
    market = ff3["Mkt-RF"].reindex(p25.index)
    for column in p25.columns:
        cov = p25[column].rolling(window).cov(market)
        betas[column] = (cov / market.rolling(window).var()).shift(1)

    table = stats.fama_macbeth(p25, {"beta": betas})
    assert list(table.index) == ["const", "beta"]
    assert table.loc["beta", "n_periods"] > 600
    # The estimated price of beta risk is a plausible monthly premium.
    assert -0.01 < table.loc["beta", "estimate"] < 0.02
    assert table.loc["beta", "se"] > 0
    assert table.attrs["gammas"].shape[1] == 2


def test_fama_macbeth_recovers_a_known_premium():
    rng = np.random.default_rng(6)
    T, N = 800, 40
    z = pd.DataFrame(
        np.tile(rng.normal(size=N), (T, 1)), columns=[f"a{i}" for i in range(N)]
    )
    gamma = 0.004
    R = z * gamma + pd.DataFrame(rng.normal(0, 0.03, size=(T, N)), columns=z.columns)
    table = stats.fama_macbeth(R, {"z": z})
    assert table.loc["z", "estimate"] == pytest.approx(gamma, abs=0.001)
    assert table.loc["z", "tstat"] > 3.0


def test_fama_macbeth_accepts_a_bare_frame():
    rng = np.random.default_rng(7)
    R = pd.DataFrame(rng.normal(size=(50, 5)))
    table = stats.fama_macbeth(R, R.shift(1))
    assert list(table.index) == ["const", "x"]


def test_long_horizon_regression_on_shiller():
    shiller = hap.shiller()
    dp = np.log(shiller["dividend"] / shiller["price"]).dropna()
    total = shiller["real_total_return_price"]
    ret = np.log(total).diff().dropna()
    table = stats.long_horizon_regression(ret, dp, horizons=(1, 12, 60))
    assert list(table.index) == [1, 12, 60]
    # Slope is positive: a high dividend yield forecasts high returns...
    assert (table["beta"] > 0).all()
    # ...and both slope and R-squared grow with the horizon.
    assert table["beta"].is_monotonic_increasing
    assert table.loc[60, "r2"] > table.loc[1, "r2"]


def test_long_horizon_regression_methods_agree_on_the_slope():
    rng = np.random.default_rng(8)
    x = pd.Series(rng.normal(size=400))
    y = 0.3 * x.shift(1) + pd.Series(rng.normal(size=400))
    nw = stats.long_horizon_regression(y, x, (1, 6), "newey-west")
    hh = stats.long_horizon_regression(y, x, (1, 6), "hansen-hodrick")
    pd.testing.assert_series_equal(nw["beta"], hh["beta"])
    assert (nw["se"] > 0).all()


def test_hansen_jagannathan_bound(ff3):
    gross = 1.0 + ff3[["Mkt-RF"]].add(ff3["RF"], axis=0)
    bound = stats.hansen_jagannathan_bound(gross)
    assert list(bound.columns) == ["mean_m", "sigma_m_min"]
    assert (bound["sigma_m_min"] >= 0).all()
    # For a single asset the bound equals |E[r_e]| / sigma(r_e) at E[m] = 1/E[R].
    excess = ff3["Mkt-RF"]
    sharpe_ratio = abs(excess.mean()) / excess.std()
    at_min = bound.loc[bound["sigma_m_min"].idxmin()]
    implied = bound["sigma_m_min"] / bound["mean_m"]
    assert implied.max() > sharpe_ratio > 0
    assert at_min["sigma_m_min"] < implied.max()


def test_sharpe_matches_the_formula(ff3):
    excess = ff3["Mkt-RF"]
    manual = np.sqrt(12) * excess.mean() / excess.std()
    assert stats.sharpe(excess, "monthly") == pytest.approx(manual)
    assert stats.sharpe(excess, 12) == pytest.approx(manual)
    # Post-war monthly equity Sharpe ratio is roughly 0.4-0.6 annualised.
    assert 0.3 < manual < 0.7
    frame_result = stats.sharpe(ff3[["Mkt-RF", "SMB"]], "monthly")
    assert isinstance(frame_result, pd.Series)


def test_drawdowns(ff3):
    frame = stats.drawdowns(ff3["Mkt-RF"] + ff3["RF"])
    assert list(frame.columns) == ["wealth", "peak", "drawdown"]
    assert (frame["drawdown"] <= 1e-12).all()
    assert frame["peak"].is_monotonic_increasing
    assert frame.attrs["max_drawdown"] < -0.4  # 2008-2009 or 1973-1974
    assert frame.attrs["trough"].year in (1974, 2009)


def test_summary_stats_standard_error_of_the_mean(ff3):
    table = stats.summary_stats(ff3[["Mkt-RF", "SMB", "HML"]], "monthly")
    assert list(table.index) == ["Mkt-RF", "SMB", "HML"]
    row = table.loc["Mkt-RF"]
    assert row["se_mean"] == pytest.approx(row["std"] / np.sqrt(row["nobs"]))
    assert row["mean_ann"] == pytest.approx(12 * row["mean"])
    assert row["std_ann"] == pytest.approx(np.sqrt(12) * row["std"])
    # The 2% motive: the annualised standard error of the mean is around 2%.
    assert 0.01 < row["se_mean_ann"] < 0.03
    assert row["kurtosis"] > 0  # fat tails
    assert stats.summary_stats(ff3["Mkt-RF"]).shape[0] == 1
