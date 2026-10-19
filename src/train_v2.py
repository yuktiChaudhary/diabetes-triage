import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

from src.data import X, y

MODEL_PATH = Path("models") / "model_v0_2.joblib"
METRICS_PATH = Path("metrics") / "metrics_v0_2.json"
V1_METRICS_PATH = Path("metrics") / "metrics.json"


def train_model():
    # Use the same split as v0.1 so that we have a fair comparison
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    # Create the improved v0.2 model using Ridge Regression
    model = Ridge(alpha=0.1)

    # Train the model
    model.fit(X_train, y_train)

    # Return the trained model and test data for evaluation
    return model, X_test, y_test



def evaluate_and_save(model, X_test, y_test):

    # Make predictions on the held-out test set
    predictions = model.predict(X_test)

    # Calculate held-out RMSE (same formula as v0.1)
    rmse = float(np.sqrt(np.mean((y_test - predictions) ** 2)))
    print("Model version: v0.2")
    print(f"RMSE: {rmse:.4f}")

    # Save the trained model to MODEL_PATH
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to: {MODEL_PATH}")

    metrics = {"model_version": "v0.2", "rmse": round(rmse, 4)}

    # Compare v0.2 RMSE with v0.1 RMSE (if the v0.1 metrics file exists)
    if V1_METRICS_PATH.exists():
        v1_rmse = json.loads(V1_METRICS_PATH.read_text())["rmse"]
        metrics["v0_1_rmse"] = v1_rmse
        metrics["rmse_change_vs_v0_1"] = round(rmse - v1_rmse, 4)
        print(f"v0.1 RMSE: {v1_rmse:.4f}")
        print(f"Change vs v0.1: {rmse - v1_rmse:+.4f}")
    else:
        print("v0.1 metrics not found, skipping comparison")

    # Save evaluation metrics to METRICS_PATH
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics
   


if __name__ == "__main__":
    model, X_test, y_test = train_model()
    evaluate_and_save(model, X_test, y_test)
