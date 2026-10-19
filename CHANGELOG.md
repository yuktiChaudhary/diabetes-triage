# Changelog

This file documents changes between versions of the Virtual Diabetes Clinic Triage ML service. 

## v0.1 — Baseline

### Model
- Algorithm: `StandardScaler` + `LinearRegression`
- Dataset: scikit-learn Diabetes regression dataset (442 samples, 10 features)
- Evaluation: Held-out train/test split with a fixed random seed
- **RMSE: 53.8534**

### Implementation
- Implemented model training and saved the trained model to `models/model_v0_1.joblib`.
- Saved evaluation metrics to `metrics/metrics.json`.
- Implemented FastAPI endpoints:
  - `GET /health` — returns service status and model version.
  - `POST /predict` — returns a continuous progression prediction.
- Added input validation with HTTP 422 JSON responses for invalid requests.
- Added automated API tests covering successful predictions and invalid inputs.
- Created a self-contained Docker image with the trained model included.

### Verification
- Model training completed successfully.
- All 5 API tests passed.
- Docker image built and ran successfully.
- Health, prediction, and missing-feature validation endpoints were verified inside the running container.


## v0.2 — Improvement

   

 ### What changed
 - Model: `Ridge(alpha=0.1)` (L2-regularised linear regression) instead of `StandardScaler` + `LinearRegression`. No extra preprocessing: scikit-learn's diabetes features are already standardised.
 - Same data, features and train/test split (`test_size=0.2`, `random_state=42`) as v0.1, so the comparison is fair.
 - New training script `src/train_v2.py`; outputs `models/model_v0_2.joblib` and `metrics/metrics_v0_2.json`.
 - The API loads the model matching the `MODEL_VERSION` environment variable, and the release workflow trains and publishes the model for the git tag.

 ### Metrics (held-out test set)
 | Version | Model | RMSE |
 |---|---|---|
 | v0.1 | StandardScaler + LinearRegression | 53.8534 |
 | v0.2 | Ridge(alpha=0.1) | 53.4461 |
 | Change | | -0.4073 (-0.76 %) |
- RMSE: TBD
- Improvement over v0.1: TBD