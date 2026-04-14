from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def run_eda(df: pd.DataFrame, figures_dir: Path, metrics_dir: Path) -> None:
    figures_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir.mkdir(parents=True, exist_ok=True)

    summary_lines: list[str] = []
    summary_lines.append(f"Shape: {df.shape}")
    summary_lines.append("\nDtypes:\n" + df.dtypes.to_string())
    summary_lines.append("\nMissing values:\n" + df.isna().sum().to_string())
    summary_lines.append(f"\nDuplicate rows: {df.duplicated().sum()}")
    summary_lines.append("\nSummary statistics:\n" + df.describe(include="all").transpose().to_string())
    (metrics_dir / "eda_summary.txt").write_text("\n".join(summary_lines), encoding="utf-8")

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(6, 4))
    sns.countplot(x="Churn", data=df)
    plt.title("Churn Distribution")
    plt.tight_layout()
    plt.savefig(figures_dir / "churn_count.png", dpi=300)
    plt.close()

    numeric_for_corr = df.select_dtypes(include=["number"]).copy()
    if not numeric_for_corr.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_for_corr.corr(), cmap="coolwarm", annot=False)
        plt.title("Numerical Feature Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(figures_dir / "correlation_heatmap.png", dpi=300)
        plt.close()

    plot_pairs = [
        ("tenure", "Tenure vs Churn", "tenure_vs_churn.png"),
        ("MonthlyCharges", "Monthly Charges vs Churn", "monthly_charges_vs_churn.png"),
        ("TotalCharges", "Total Charges vs Churn", "total_charges_vs_churn.png"),
    ]
    for feature, title, filename in plot_pairs:
        if feature in df.columns:
            plt.figure(figsize=(7, 4))
            sns.boxplot(x="Churn", y=feature, data=df)
            plt.title(title)
            plt.tight_layout()
            plt.savefig(figures_dir / filename, dpi=300)
            plt.close()

    cat_plots = [
        ("Contract", "Contract Type vs Churn", "contract_vs_churn.png"),
        ("PaymentMethod", "Payment Method vs Churn", "payment_method_vs_churn.png"),
        ("InternetService", "Internet Service vs Churn", "internet_service_vs_churn.png"),
    ]
    for feature, title, filename in cat_plots:
        if feature in df.columns:
            plt.figure(figsize=(8, 4))
            sns.countplot(x=feature, hue="Churn", data=df)
            plt.xticks(rotation=20, ha="right")
            plt.title(title)
            plt.tight_layout()
            plt.savefig(figures_dir / filename, dpi=300)
            plt.close()
