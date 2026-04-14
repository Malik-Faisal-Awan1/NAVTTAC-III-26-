from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.evaluate import (
    calculate_metrics,
    plot_confusion_matrix,
    plot_roc_curve,
    save_classification_report,
)
from src.feature_engineering import build_preprocessor


def _predict_proba_or_score(model: Pipeline, x_data: pd.DataFrame) -> np.ndarray | None:
    if hasattr(model, "predict_proba"):
        return model.predict_proba(x_data)[:, 1]
    if hasattr(model, "decision_function"):
        raw_scores = model.decision_function(x_data)
        return 1.0 / (1.0 + np.exp(-raw_scores))
    return None


def train_and_evaluate_ml(
    train_df: pd.DataFrame,
    valid_df: pd.DataFrame,
    test_df: pd.DataFrame,
    feature_cols: list[str],
    target_col: str,
    numeric_cols: list[str],
    categorical_cols: list[str],
    outputs_dir: Path,
) -> dict:
    models = {
        "logistic_regression": LogisticRegression(max_iter=1000, class_weight="balanced"),
        "decision_tree": DecisionTreeClassifier(random_state=42, class_weight="balanced"),
        "random_forest": RandomForestClassifier(
            n_estimators=300, random_state=42, class_weight="balanced"
        ),
        "gradient_boosting": GradientBoostingClassifier(random_state=42),
        "svm_rbf": SVC(probability=True, class_weight="balanced", random_state=42),
        "knn": KNeighborsClassifier(n_neighbors=15),
    }

    x_train, y_train = train_df[feature_cols], train_df[target_col].values
    x_valid, y_valid = valid_df[feature_cols], valid_df[target_col].values
    x_test, y_test = test_df[feature_cols], test_df[target_col].values

    metrics = {}
    best_model_name = ""
    best_auc = -1.0
    best_pipeline = None

    for model_name, estimator in models.items():
        preprocessor = build_preprocessor(numeric_cols, categorical_cols)
        pipeline = Pipeline([("preprocessor", preprocessor), ("model", estimator)])
        pipeline.fit(x_train, y_train)

        y_valid_pred = pipeline.predict(x_valid)
        y_valid_prob = _predict_proba_or_score(pipeline, x_valid)
        valid_metrics = calculate_metrics(y_valid, y_valid_pred, y_valid_prob)
        metrics[f"{model_name}_valid"] = valid_metrics

        if valid_metrics["roc_auc"] > best_auc:
            best_auc = valid_metrics["roc_auc"]
            best_model_name = model_name
            best_pipeline = pipeline

    if best_pipeline is None:
        raise RuntimeError("No ML model was trained successfully.")

    y_test_pred = best_pipeline.predict(x_test)
    y_test_prob = _predict_proba_or_score(best_pipeline, x_test)
    metrics["best_ml_test"] = calculate_metrics(y_test, y_test_pred, y_test_prob)
    metrics["best_ml_name"] = {"name": best_model_name}

    model_dir = outputs_dir / "models"
    metrics_dir = outputs_dir / "metrics"
    figures_dir = outputs_dir / "figures"
    predictions_dir = outputs_dir / "predictions"
    for d in [model_dir, metrics_dir, figures_dir, predictions_dir]:
        d.mkdir(parents=True, exist_ok=True)

    with (model_dir / "best_ml_model.pkl").open("wb") as fp:
        pickle.dump(best_pipeline, fp)

    predictions = test_df.copy()
    predictions["prediction"] = y_test_pred
    if y_test_prob is not None:
        predictions["probability"] = y_test_prob
    predictions.to_csv(predictions_dir / "ml_test_predictions.csv", index=False)

    save_classification_report(
        y_test, y_test_pred, metrics_dir / f"{best_model_name}_classification_report.txt"
    )
    plot_confusion_matrix(
        y_test,
        y_test_pred,
        figures_dir / f"{best_model_name}_confusion_matrix.png",
        f"{best_model_name} - Confusion Matrix",
    )
    if y_test_prob is not None:
        plot_roc_curve(
            y_test,
            y_test_prob,
            figures_dir / f"{best_model_name}_roc_curve.png",
            f"{best_model_name} - ROC Curve",
        )

    return metrics
