# Final Report - Telco Churn Prediction

## 1) Dataset Understanding
- Dataset: IBM Telco Customer Churn
- Target variable: `Churn` (Yes/No -> 1/0)
- ID column: `customerID` (excluded from training)
- Numerical features include: `tenure`, `MonthlyCharges`, `TotalCharges`
- Categorical features include contract details, service types, payment method, and demographics.

## 2) EDA Summary
- Included checks: shape, dtypes, missing values, duplicates, class balance.
- Included plots:
  - Churn count
  - Tenure vs churn
  - Monthly/Total charges vs churn
  - Contract vs churn
  - Payment method vs churn
  - Internet service vs churn
  - Correlation heatmap for numerical features
- See exported outputs in `outputs/figures/` and `outputs/metrics/eda_summary.txt`.

## 3) Preprocessing
- `customerID` removed from model features.
- `TotalCharges` converted to numeric with invalid values handled as missing.
- Duplicate rows removed.
- Categorical variables encoded using one-hot encoding.
- Numeric columns imputed (median) and standardized.
- Train/validation/test split ratio: 70/15/15 with stratification.

## 4) Machine Learning Experiments
Tested models:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- SVM (RBF)
- KNN

Model selection is based on validation ROC-AUC. Final ML test metrics are in `outputs/metrics/ml_metrics.json`.

## 5) Deep Learning Experiment
- A feedforward MLP (PyTorch) with:
  - Input layer
  - Two hidden layers (ReLU + Dropout)
  - Output layer for binary classification
- Trained with BCEWithLogitsLoss and class weighting.
- Curves saved:
  - `outputs/figures/dl_loss_curve.png`
  - `outputs/figures/dl_accuracy_curve.png`

## 6) Final Comparison
- Compare best ML model against the DL model using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC
- Final comparison JSON: `outputs/metrics/final_comparison.json`

## 7) Conclusion (Fill After Running)
- Most important churn factors:
- Best performing model:
- Biggest preprocessing challenge:
- Key learning from project:
