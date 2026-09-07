"""Parquet cache for the data loaders in :mod:`hap.data`.

The cache lives in ``data/cache/`` at the repository root (located relative to
``hap.__file__``) and holds one parquet file per loader call signature.  The
files are committed to the repository, so a fresh clone can reproduce every
lecture without touching the network.

Environment variables
---------------------
``HAP_OFFLINE=1``
    Never download.  A cache miss raises :class:`CacheMissError`.
``HAP_REFRESH=1``
    Always download, ignoring whatever is in the cache.

Default behaviour (neither variable set) is to download only when the parquet
file is missing, or when it is older than ``max_age_days`` if the loader passes
one.  Cached snapshots therefore never go stale silently.
"""

from __future__ import annotations

import datetime as dt
import functools
import inspect
import os
import re
from collections.abc import Callable
from pathlib import Path
from typing import ParamSpec

import pandas as pd

__all__ = [
    "CACHE_DIR",
    "RAW_DIR",
    "REPO_ROOT",
    "CacheMissError",
    "cache_path",
    "cached",
    "is_offline",
    "load_cached",
]

P = ParamSpec("P")

REPO_ROOT: Path = Path(__file__).resolve().parents[2]
"""Repository root, i.e. the directory containing ``pyproject.toml``."""

CACHE_DIR: Path = REPO_ROOT / "data" / "cache"
"""Directory holding the committed parquet snapshots."""

RAW_DIR: Path = REPO_ROOT / "data" / "raw"
"""Directory for manually downloaded source files (git-ignored)."""


class CacheMissError(FileNotFoundError):
    """Raised when a snapshot is missing and downloading is not allowed."""


def is_offline() -> bool:
    """Return ``True`` when ``HAP_OFFLINE`` is set to a truthy value."""
    return os.environ.get("HAP_OFFLINE", "") not in ("", "0", "false", "False")


def _refresh_requested() -> bool:
    return os.environ.get("HAP_REFRESH", "") not in ("", "0", "false", "False")


def _slug(value: object) -> str:
    """Turn an argument into a short filesystem-safe token."""
    text = ",".join(map(str, value)) if isinstance(value, (list, tuple)) else str(value)
    text = re.sub(r"[^0-9A-Za-z._+-]+", "-", text).strip("-")
    return text[:60] if text else "none"


def cache_key(name: str, *args: object, **kwargs: object) -> str:
    """Build the cache key for a loader call.

    Parameters
    ----------
    name : str
        Base name of the dataset, e.g. ``"french"``.
    *args, **kwargs
        Loader arguments; each is slugified and appended to the key.

    Returns
    -------
    str
        Key such as ``"french__F-F_Research_Data_Factors__monthly"``.
    """
    parts = [_slug(a) for a in args]
    parts += [f"{k}-{_slug(v)}" for k, v in sorted(kwargs.items())]
    return "__".join([name, *parts]) if parts else name


def cache_path(key: str) -> Path:
    """Return the parquet path for a cache key."""
    return CACHE_DIR / f"{key}.parquet"


def _age_days(path: Path) -> float:
    modified = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.UTC)
    return (dt.datetime.now(tz=dt.UTC) - modified).total_seconds() / 86400.0


def load_cached(
    key: str,
    builder: Callable[[], pd.DataFrame],
    max_age_days: float | None = None,
) -> pd.DataFrame:
    """Read ``key`` from the parquet cache, downloading via ``builder`` if needed.

    Parameters
    ----------
    key : str
        Cache key, see :func:`cache_key`.
    builder : callable
        Zero-argument function that downloads and parses the data.  Only called
        when the cache cannot be used.
    max_age_days : float, optional
        Re-download when the cached file is older than this.  ``None`` (the
        default) means the snapshot never expires.

    Returns
    -------
    pandas.DataFrame

    Raises
    ------
    CacheMissError
        When ``HAP_OFFLINE=1`` and the snapshot is missing.
    """
    path = cache_path(key)
    if is_offline():
        if not path.exists():
            raise CacheMissError(
                f"HAP_OFFLINE=1 but no cached snapshot at {path}. "
                f"Unset HAP_OFFLINE (and optionally set HAP_REFRESH=1) to download it."
            )
        return _read(path)

    stale = max_age_days is not None and path.exists() and _age_days(path) > max_age_days
    if path.exists() and not stale and not _refresh_requested():
        return _read(path)

    frame = builder()
    _write(frame, path)
    return frame


def _read(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path)


def _write(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = frame.copy()
    out.columns = [str(c) for c in out.columns]
    out.to_parquet(path, compression="zstd")


def cached(
    name: str, max_age_days: float | None = None
) -> Callable[[Callable[P, pd.DataFrame]], Callable[P, pd.DataFrame]]:
    """Decorate a loader so its result is stored in ``data/cache/``.

    The cache key is derived from ``name`` plus the call arguments, so each
    distinct argument combination gets its own parquet file.

    Parameters
    ----------
    name : str
        Base name of the dataset.
    max_age_days : float, optional
        Passed through to :func:`load_cached`.

    Examples
    --------
    >>> @cached("fred")  # doctest: +SKIP
    ... def fred(series: str) -> pd.DataFrame:
    ...     ...
    """

    def decorator(func: Callable[P, pd.DataFrame]) -> Callable[P, pd.DataFrame]:
        signature = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> pd.DataFrame:
            # Bind defaults so french("X") and french("X", "monthly") share a key.
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            key = cache_key(name, *bound.arguments.values())
            return load_cached(key, lambda: func(*args, **kwargs), max_age_days)

        wrapper.uncached = func  # type: ignore[attr-defined]
        return wrapper

    return decorator


def cache_size_mb() -> float:
    """Total size of ``data/cache/`` in megabytes."""
    if not CACHE_DIR.exists():
        return 0.0
    return sum(p.stat().st_size for p in CACHE_DIR.glob("*.parquet")) / 1e6


def require_raw(filename: str, instructions: str) -> Path:
    """Return the path to a manually downloaded file in ``data/raw/``.

    Parameters
    ----------
    filename : str
        Name of the expected file inside ``data/raw/``.
    instructions : str
        Human-readable download instructions shown when the file is missing.

    Returns
    -------
    pathlib.Path

    Raises
    ------
    CacheMissError
        When the file is absent.
    """
    path = RAW_DIR / filename
    if not path.exists():
        raise CacheMissError(f"Missing {path}.\n{instructions}")
    return path
