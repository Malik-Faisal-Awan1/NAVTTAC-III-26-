from __future__ import annotations

from pathlib import Path

import pandas as pd


def resolve_dataset_path(project_root: Path) -> Path:
    preferred = project_root / "data" / "raw" / "Telco-Customer-Churn.csv"
    fallback = project_root.parent / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    if preferred.exists():
        return preferred
    if fallback.exists():
        return fallback
    raise FileNotFoundError(
        "Dataset not found. Place it at data/raw/Telco-Customer-Churn.csv "
        "or at workspace root as WA_Fn-UseC_-Telco-Customer-Churn.csv."
    )


def load_telco_data(project_root: Path) -> pd.DataFrame:
    dataset_path = resolve_dataset_path(project_root)
    return pd.read_csv(dataset_path)
