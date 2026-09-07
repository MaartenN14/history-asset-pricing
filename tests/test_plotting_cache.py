"""Tests for :mod:`hap.plotting` and :mod:`hap.cache`."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

import hap  # noqa: E402
from hap import cache, plotting  # noqa: E402


def test_setup_applies_the_style():
    plotting.setup()
    assert plt.rcParams["figure.figsize"] == [9.0, 5.0]
    assert plt.rcParams["figure.dpi"] == 110
    assert plt.rcParams["axes.prop_cycle"].by_key()["color"][0] == plotting.COLORS[0]
    plotting.setup(**{"figure.dpi": 90})
    assert plt.rcParams["figure.dpi"] == 90
    plotting.setup()


def test_timeline_axis_and_recession_shading():
    plotting.setup()
    market = hap.market_monthly()["Mkt"].loc["1990":]
    fig, ax = plt.subplots()
    ax.plot(market.index, (1 + market).cumprod())
    plotting.timeline_axis(ax, every=5)
    before = ax.get_xlim()
    plotting.recession_shading(ax)
    assert ax.get_xlim() == before
    # 2001, 2008-09 and 2020 recessions inside the window.
    assert len(ax.patches) >= 3
    assert ax.xaxis.get_major_formatter().fmt == "%Y"
    plt.close(fig)


def test_cache_paths_are_inside_the_repository():
    assert cache.CACHE_DIR == cache.REPO_ROOT / "data" / "cache"
    assert (cache.REPO_ROOT / "pyproject.toml").exists()
    assert cache.CACHE_DIR.exists()
    assert cache.cache_size_mb() > 1.0


def test_cache_key_normalises_defaults():
    assert cache.cache_key("fred", "USREC", None) == "fred__USREC__None"
    assert cache.cache_key("yahoo", ["SPY", "TLT"]) == "yahoo__SPY-TLT"


def test_default_arguments_hit_the_same_snapshot():
    pd.testing.assert_frame_equal(
        hap.french("F-F_Research_Data_Factors"),
        hap.french("F-F_Research_Data_Factors", "monthly", 0, None),
    )


def test_offline_flag_is_active_in_the_test_suite():
    assert cache.is_offline()
    with pytest.raises(cache.CacheMissError):
        cache.load_cached("definitely_not_cached", lambda: pd.DataFrame())


def test_require_raw_explains_the_manual_step():
    with pytest.raises(cache.CacheMissError, match="do this"):
        cache.require_raw("no_such_file.csv", "do this")
