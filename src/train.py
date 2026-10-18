from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import json


from data import X, y

MODEL_PATH = Path("models") / "model_v0_1.joblib"
METRICS_PATH = Path("metrics")/"metrics.json"


def train_model():
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("regressor", LinearRegression()),
        ]
    )
    
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    rmse = float(np.sqrt(np.mean((y_test - predictions) ** 2))) 
    
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    
    metrics = {
        "model_version": "v0.1",
        "rmse": f"{rmse:.4f}"
    }
    
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)
    
    print("Model version: v0.1")
    print(f"RMSE: {rmse:.4f}")
    print(f"Saved model to {MODEL_PATH}")

    return metrics


if __name__ == "__main__":
    train_model()