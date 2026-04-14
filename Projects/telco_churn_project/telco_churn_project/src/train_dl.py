from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.utils.class_weight import compute_class_weight
from torch.utils.data import DataLoader, TensorDataset

from src.evaluate import calculate_metrics, plot_confusion_matrix, plot_roc_curve
from src.feature_engineering import build_preprocessor


class ChurnMLP(nn.Module):
    def __init__(self, input_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def _to_dense_float32(matrix) -> np.ndarray:
    if hasattr(matrix, "toarray"):
        matrix = matrix.toarray()
    return np.asarray(matrix, dtype=np.float32)


def train_and_evaluate_dl(
    train_df: pd.DataFrame,
    valid_df: pd.DataFrame,
    test_df: pd.DataFrame,
    feature_cols: list[str],
    target_col: str,
    numeric_cols: list[str],
    categorical_cols: list[str],
    outputs_dir: Path,
    epochs: int = 30,
    batch_size: int = 128,
) -> dict:
    x_train_raw, y_train = train_df[feature_cols], train_df[target_col].values
    x_valid_raw, y_valid = valid_df[feature_cols], valid_df[target_col].values
    x_test_raw, y_test = test_df[feature_cols], test_df[target_col].values

    preprocessor = build_preprocessor(numeric_cols, categorical_cols)
    x_train = _to_dense_float32(preprocessor.fit_transform(x_train_raw))
    x_valid = _to_dense_float32(preprocessor.transform(x_valid_raw))
    x_test = _to_dense_float32(preprocessor.transform(x_test_raw))

    y_train_t = torch.tensor(y_train.reshape(-1, 1), dtype=torch.float32)
    y_valid_t = torch.tensor(y_valid.reshape(-1, 1), dtype=torch.float32)
    y_test_t = torch.tensor(y_test.reshape(-1, 1), dtype=torch.float32)

    train_loader = DataLoader(
        TensorDataset(torch.tensor(x_train), y_train_t), batch_size=batch_size, shuffle=True
    )
    valid_loader = DataLoader(
        TensorDataset(torch.tensor(x_valid), y_valid_t), batch_size=batch_size, shuffle=False
    )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ChurnMLP(input_dim=x_train.shape[1]).to(device)

    class_weights = compute_class_weight(
        class_weight="balanced", classes=np.array([0, 1]), y=y_train
    )
    pos_weight = torch.tensor([class_weights[1] / class_weights[0]], dtype=torch.float32).to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    history = {"train_loss": [], "valid_loss": [], "train_acc": [], "valid_acc": []}

    for _ in range(epochs):
        model.train()
        train_losses: list[float] = []
        train_correct = 0
        train_total = 0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()
            train_losses.append(loss.item())
            preds = (torch.sigmoid(logits) >= 0.5).float()
            train_correct += (preds == yb).sum().item()
            train_total += yb.numel()

        model.eval()
        valid_losses: list[float] = []
        valid_correct = 0
        valid_total = 0
        with torch.no_grad():
            for xb, yb in valid_loader:
                xb, yb = xb.to(device), yb.to(device)
                logits = model(xb)
                loss = criterion(logits, yb)
                valid_losses.append(loss.item())
                preds = (torch.sigmoid(logits) >= 0.5).float()
                valid_correct += (preds == yb).sum().item()
                valid_total += yb.numel()

        history["train_loss"].append(float(np.mean(train_losses)))
        history["valid_loss"].append(float(np.mean(valid_losses)))
        history["train_acc"].append(float(train_correct / train_total))
        history["valid_acc"].append(float(valid_correct / valid_total))

    model.eval()
    with torch.no_grad():
        test_logits = model(torch.tensor(x_test).to(device)).cpu()
    test_probs = torch.sigmoid(test_logits).numpy().reshape(-1)
    test_preds = (test_probs >= 0.5).astype(int)

    metrics = calculate_metrics(y_test, test_preds, test_probs)

    model_dir = outputs_dir / "models"
    figure_dir = outputs_dir / "figures"
    metrics_dir = outputs_dir / "metrics"
    predictions_dir = outputs_dir / "predictions"
    for d in [model_dir, figure_dir, metrics_dir, predictions_dir]:
        d.mkdir(parents=True, exist_ok=True)

    torch.save(model.state_dict(), model_dir / "dl_mlp_model.pt")
    torch.save(preprocessor, model_dir / "dl_preprocessor.pt")

    pd.DataFrame(
        {
            "actual": y_test_t.numpy().reshape(-1).astype(int),
            "prediction": test_preds,
            "probability": test_probs,
        }
    ).to_csv(predictions_dir / "dl_test_predictions.csv", index=False)

    plt.figure(figsize=(8, 4))
    plt.plot(history["train_loss"], label="Train Loss")
    plt.plot(history["valid_loss"], label="Valid Loss")
    plt.title("DL Training and Validation Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.tight_layout()
    plt.savefig(figure_dir / "dl_loss_curve.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(history["train_acc"], label="Train Accuracy")
    plt.plot(history["valid_acc"], label="Valid Accuracy")
    plt.title("DL Training and Validation Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(figure_dir / "dl_accuracy_curve.png", dpi=300)
    plt.close()

    plot_confusion_matrix(y_test, test_preds, figure_dir / "dl_confusion_matrix.png", "DL Confusion Matrix")
    plot_roc_curve(y_test, test_probs, figure_dir / "dl_roc_curve.png", "DL ROC Curve")

    return {"dl_test": metrics}
