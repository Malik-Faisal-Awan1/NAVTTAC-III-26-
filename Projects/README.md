# Telco Churn Project

End-to-end customer churn prediction project using the IBM Telco dataset with:
- Exploratory Data Analysis (EDA)
- Data preprocessing and train/validation/test split
- Multiple machine learning models
- One deep learning model (PyTorch MLP)
- Final model comparison and exportable outputs

## Project Structure

```text
telco_churn_project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── outputs/
│   ├── figures/
│   ├── metrics/
│   ├── models/
│   └── predictions/
├── report/
├── src/
├── main.py
└── requirements.txt
```

## Dataset

The pipeline auto-detects the dataset from either:
- `data/raw/Telco-Customer-Churn.csv`
- `../WA_Fn-UseC_-Telco-Customer-Churn.csv` (workspace root fallback)

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Outputs Generated

- EDA summaries and figures: `outputs/figures`, `outputs/metrics/eda_summary.txt`
- Processed splits: `data/processed/train.csv`, `valid.csv`, `test.csv`
- ML artifacts:
  - `outputs/models/best_ml_model.pkl`
  - `outputs/metrics/ml_metrics.json`
  - `outputs/predictions/ml_test_predictions.csv`
- DL artifacts:
  - `outputs/models/dl_mlp_model.pt`
  - `outputs/metrics/dl_metrics.json`
  - `outputs/predictions/dl_test_predictions.csv`
- Final comparison:
  - `outputs/metrics/final_comparison.json`

## Notes for Submission

- Accuracy is reported, but precision/recall/F1/ROC-AUC are prioritized for churn analysis.
- ID column (`customerID`) is excluded from modeling.
- `TotalCharges` is converted to numeric with invalid values handled as missing.
