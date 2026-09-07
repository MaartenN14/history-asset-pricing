"""Force every test to read from the committed parquet cache."""

from __future__ import annotations

import os

os.environ["HAP_OFFLINE"] = "1"
os.environ.pop("HAP_REFRESH", None)
