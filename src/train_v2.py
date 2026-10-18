# import json
from pathlib import Path

# import joblib
# import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

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

    # Create the improved v0.2 model using Ridge Regression
    model = Ridge(alpha=0.1)

    # Train the model
    model.fit(X_train, y_train)

    # Return the trained model and test data for evaluation
    return model, X_test, y_test


# Alvaro's parts below
def evaluate_and_save(model, X_test, y_test):
    # TODO: Make predictions on the test data

    # TODO: Calculate held-out RMSE

    # TODO: Save the trained model to MODEL_PATH

    # TODO: Save evaluation metrics to METRICS_PATH

    # TODO: Compare v0.2 RMSE with v0.1 RMSE

    pass


if __name__ == "__main__":
    model, X_test, y_test = train_model()
    evaluate_and_save(model, X_test, y_test)
