import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.data import X, y

MODEL_PATH = Path("models") / "model_v0_2.joblib"
METRICS_PATH = Path("metrics") / "metrics_v0_2.json"


def train_model():
    # Use the same split as v0.1 so that we have a fair comparison
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    # TODO: Create the improved v0.2 model

    # TODO: Train the model

    # TODO: Make predictions
   

    # TODO: Calculate RMSE


    # TODO: Save the v0.2 model


    # TODO: Save v0.2 metrics

    # TODO: Compare the v0.2 RMSE with v0.1

    pass


if __name__ == "__main__":
    train_model()