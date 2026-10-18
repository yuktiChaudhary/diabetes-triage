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

- Model changes: ?

According to the assignment it can be improved by: 

"try Ridge/RandomForestRegressor or better preprocessing (feature scaling/selection), plus calibration of the score if you convert to a “high-risk” flag (e.g., threshold on predicted progression)" 

- RMSE: TBD
- Improvement over v0.1: TBD