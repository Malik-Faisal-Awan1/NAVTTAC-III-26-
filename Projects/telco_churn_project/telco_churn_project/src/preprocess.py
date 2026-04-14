from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


@dataclass
class PreprocessArtifacts:
    train_df: pd.DataFrame
    valid_df: pd.DataFrame
    test_df: pd.DataFrame
    feature_cols: list[str]
    numeric_cols: list[str]
    categorical_cols: list[str]
    target_col: str


def clean_telco_data(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data.columns = [c.strip() for c in data.columns]
    if "TotalCharges" in data.columns:
        data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    data = data.drop_duplicates()
    data = data.dropna(subset=["Churn"])
    data["Churn"] = data["Churn"].map({"Yes": 1, "No": 0}).astype(int)
    return data


def split_data(data: pd.DataFrame, target_col: str = "Churn") -> PreprocessArtifacts:
    feature_cols = [c for c in data.columns if c not in [target_col, "customerID"]]
    numeric_cols = data[feature_cols].select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = [c for c in feature_cols if c not in numeric_cols]

    train_df, temp_df = train_test_split(
        data, test_size=0.3, random_state=42, stratify=data[target_col]
    )
    valid_df, test_df = train_test_split(
        temp_df, test_size=0.5, random_state=42, stratify=temp_df[target_col]
    )

    return PreprocessArtifacts(
        train_df=train_df,
        valid_df=valid_df,
        test_df=test_df,
        feature_cols=feature_cols,
        numeric_cols=numeric_cols,
        categorical_cols=categorical_cols,
        target_col=target_col,
    )


def save_splits(artifacts: PreprocessArtifacts, processed_dir: Path) -> None:
    processed_dir.mkdir(parents=True, exist_ok=True)
    artifacts.train_df.to_csv(processed_dir / "train.csv", index=False)
    artifacts.valid_df.to_csv(processed_dir / "valid.csv", index=False)
    artifacts.test_df.to_csv(processed_dir / "test.csv", index=False)
