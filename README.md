
# Virtual Diabetes Clinic Triage

This is our MLOps assignment project. We're using the scikit-learn diabetes dataset to train a regression model and make predictions through a FastAPI API.

We've also added Docker, automated tests and GitHub Actions for CI/CD.

## 1. Model and dataset

We're using the diabetes regression dataset from scikit-learn. It has 442 samples and 10 features:

`age`, `sex`, `bmi`, `bp`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`

### Version 0.1

For our first version, we're using:

- StandardScaler to scale the features
- LinearRegression as the baseline model
- A fixed train/test split so the results are reproducible
- RMSE to evaluate the predictions

**v0.1 test RMSE: 53.8534**

The trained model is saved in `models/model_v0_1.joblib`, and the results are in `metrics/metrics.json`.

### Version 0.2

For our second version, we decided to use Ridge Regression to improve the baseline model.

We tried different approaches, including Ridge, Random Forest, feature scaling and PCA, to compare their performance.

We chose Ridge Regression with alpha=0.1 because it performed well in our experiments, improved on the baseline, and kept the model simple.

Both versions use the same 80/20 train/test split with random_state=42 so we can compare their results.

| Model | Held-out test RMSE |
|---|---|
| v0.1 - Linear Regression | 53.8534 |
| v0.2 - Ridge Regression | 53.4461 |
| Random Forest | 53.4527 |
| Ridge + StandardScaler + PCA | 53.6901 |

Ridge improved the held-out RMSE by approximately 0.76% compared with v0.1.

The v0.2 training code is in `src/train_v2.py`. The trained model is saved in `models/model_v0_2.joblib`, and the evaluation results are saved in `metrics/metrics_v0_2.json`.

## 2. Run with Docker

Docker is the easiest way to run the API since the image already includes the code, model and dependencies.

### Build and run locally

First, clone the repo:

```bash
git clone https://github.com/yuktiChaudhary/diabetes-triage.git
cd diabetes-triage
```

To build the v0.1 image:

```bash
docker build -t diabetes-triage:v0.1 .
```

Run it:

```bash
docker run --rm -p 80:80 diabetes-triage:v0.1
```

To build the v0.2 image:

```bash
docker build --build-arg MODEL_VERSION=v0.2 -t diabetes-triage:v0.2 .
```

Run it:

```bash
docker run --rm -p 80:80 diabetes-triage:v0.2
```

Only run one version at a time when using port 80.

Once it's running, you can check the API here:

http://localhost:80/health

You can also use FastAPI's interactive docs to test the endpoints:

http://localhost:80/docs

The `/health` endpoint shows which model version is currently running.

### Published Docker images

Once both versions are published to GitHub Container Registry (GHCR), they can be pulled directly instead of building them locally.

For v0.1:

```bash
docker pull ghcr.io/yuktichaudhary/diabetes-triage:v0.1
docker run --rm -p 80:80 ghcr.io/yuktichaudhary/diabetes-triage:v0.1
```

For v0.2:

```bash
docker pull ghcr.io/yuktichaudhary/diabetes-triage:v0.2
docker run --rm -p 80:80 ghcr.io/yuktichaudhary/diabetes-triage:v0.2
```

## 3. API endpoints

We have two endpoints.

### GET /health

Checks if the API is running and shows which model version is being used.

Example response for v0.1:

```json
{
  "status": "ok",
  "model_version": "v0.1"
}
```

When running v0.2, the model version will be `"v0.2"` instead.

To test it:

```bash
curl http://localhost:80/health
```

### POST /predict

Takes the 10 diabetes features and returns a prediction.

Example request:

```json
{
  "age": 0.02,
  "sex": -0.044,
  "bmi": 0.06,
  "bp": -0.03,
  "s1": -0.02,
  "s2": 0.03,
  "s3": -0.02,
  "s4": 0.02,
  "s5": 0.02,
  "s6": -0.001
}
```

Example response:

```json
{
  "prediction": 210.5
}
```

The prediction value above is just an example. The actual value depends on the model version and input features.

You can try it through http://localhost:80/docs or use curl:

```bash
curl -X POST http://localhost:80/predict \
  -H "Content-Type: application/json" \
  -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

### Input validation

We're using Pydantic to check the input before making predictions.

If a required feature is missing, the API returns HTTP 422 with a JSON error showing which field is missing.

For example, leaving out `s6` returns an error similar to:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "s6"],
      "msg": "Field required"
    }
  ]
}
```

The actual error response also includes an `input` field containing the submitted request data.

The `loc` field identifies the missing feature.

The API also rejects non-numeric values and extra features with HTTP 422.

## 4. Reproducing the training

If you want to run the training yourself, you can use Python 3.12 or 3.13.

From the project folder, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Then train the v0.1 model:

```bash
python -m src.train
```

This saves:

- `models/model_v0_1.joblib` - trained model
- `metrics/metrics.json` - evaluation results

We use a fixed train/test split, so running it again should give the same RMSE.

### Training v0.2

The v0.2 model uses Ridge Regression with alpha=0.1.

To train both versions:

```bash
python -m src.train
python -m src.train_v2
```

Both models use the same dataset and train/test split (`test_size=0.2`, `random_state=42`).

The v0.2 training script saves:

- `models/model_v0_2.joblib` - trained Ridge model
- `metrics/metrics_v0_2.json` - evaluation results and comparison with v0.1

The v0.2 RMSE is **53.4461**, compared with **53.8534** for v0.1.

## 5. Testing

We use pytest for API tests and Ruff for linting and formatting.

Make sure both models have been trained before running the tests.

Run all tests:

```bash
python -m pytest -v
```

We have separate API tests for both versions:

- `tests/test_api.py` - tests v0.1
- `tests/test_api_v2.py` - tests v0.2

Both versions are tested for:

- Correct model version from `/health`
- Valid numeric predictions from `/predict`
- Missing features returning HTTP 422
- Non-numeric values returning HTTP 422
- Extra features returning HTTP 422

The v0.2 tests run in a separate Python process with `MODEL_VERSION=v0.2`, so the correct model is loaded.

All 6 pytest tests passed locally. The v0.2 test contains five API checks.

To check linting and formatting:

```bash
python -m ruff check .
python -m ruff format --check .
```

## 6. CI/CD

We're using GitHub Actions to automate testing and releases.

### CI workflow

The CI workflow runs whenever we push changes or open a pull request.

It:

- Installs the dependencies
- Runs Ruff linting and formatting checks
- Trains both v0.1 and v0.2
- Runs the automated tests
- Uploads the model and metrics files for both versions as artifacts

### Release workflow

The release workflow is set up to run when we push a version tag like `v0.1` or `v0.2`.

It:

- Trains the model for the selected version
- Builds the Docker image for that version
- Runs the container and tests the API
- Pushes the image to GitHub Container Registry (GHCR)
- Creates a GitHub Release with the changelog and metrics

The Docker image is tagged with the same version as the Git tag.
