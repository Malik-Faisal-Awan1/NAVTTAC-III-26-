from __future__ import annotations

from pathlib import Path

from src.data_loader import load_telco_data
from src.eda import run_eda
from src.preprocess import clean_telco_data, save_splits, split_data
from src.train_dl import train_and_evaluate_dl
from src.train_ml import train_and_evaluate_ml
from src.utils import ensure_dirs, save_json, set_seed


def run_pipeline() -> None:
    set_seed(42)
    project_root = Path(__file__).resolve().parent

    data_raw = project_root / "data" / "raw"
    data_processed = project_root / "data" / "processed"
    notebooks_dir = project_root / "notebooks"
    src_dir = project_root / "src"
    outputs_figures = project_root / "outputs" / "figures"
    outputs_metrics = project_root / "outputs" / "metrics"
    outputs_predictions = project_root / "outputs" / "predictions"
    outputs_models = project_root / "outputs" / "models"
    report_dir = project_root / "report"

    ensure_dirs(
        [
            data_raw,
            data_processed,
            notebooks_dir,
            src_dir,
            outputs_figures,
            outputs_metrics,
            outputs_predictions,
            outputs_models,
            report_dir,
        ]
    )

    df_raw = load_telco_data(project_root)
    run_eda(df_raw, outputs_figures, outputs_metrics)

    df_clean = clean_telco_data(df_raw)
    artifacts = split_data(df_clean)
    save_splits(artifacts, data_processed)

    ml_metrics = train_and_evaluate_ml(
        train_df=artifacts.train_df,
        valid_df=artifacts.valid_df,
        test_df=artifacts.test_df,
        feature_cols=artifacts.feature_cols,
        target_col=artifacts.target_col,
        numeric_cols=artifacts.numeric_cols,
        categorical_cols=artifacts.categorical_cols,
        outputs_dir=project_root / "outputs",
    )
    save_json(ml_metrics, outputs_metrics / "ml_metrics.json")

    dl_metrics = train_and_evaluate_dl(
        train_df=artifacts.train_df,
        valid_df=artifacts.valid_df,
        test_df=artifacts.test_df,
        feature_cols=artifacts.feature_cols,
        target_col=artifacts.target_col,
        numeric_cols=artifacts.numeric_cols,
        categorical_cols=artifacts.categorical_cols,
        outputs_dir=project_root / "outputs",
    )
    save_json(dl_metrics, outputs_metrics / "dl_metrics.json")

    comparison = {
        "best_ml_model": ml_metrics.get("best_ml_name", {}),
        "best_ml_test_metrics": ml_metrics.get("best_ml_test", {}),
        "dl_test_metrics": dl_metrics.get("dl_test", {}),
    }
    save_json(comparison, outputs_metrics / "final_comparison.json")


if __name__ == "__main__":
    run_pipeline()
