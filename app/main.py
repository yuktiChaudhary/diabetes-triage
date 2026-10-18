
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from src.data import DiabetesFeatures

MODEL_PATH = Path("models") / "model_v0_1.joblib"
MODEL_VERSION = "v0.1"

app = FastAPI(title="Virtual Diabetes Clinic Triage")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}


@app.post("/predict")
def predict(features: DiabetesFeatures):
    if not MODEL_PATH.exists():
        from fastapi import HTTPException

        raise HTTPException(
            status_code=503,
            detail="Model file not found. Please train the model first.",
        )

    model = joblib.load(MODEL_PATH)
    input_data = pd.DataFrame(
    [[
        features.age,
        features.sex,
        features.bmi,
        features.bp,
        features.s1,
        features.s2,
        features.s3,
        features.s4,
        features.s5,
        features.s6,
    ]],
    columns=[
        "age", "sex", "bmi", "bp", "s1",
        "s2", "s3", "s4", "s5", "s6",
    ],
)

    prediction = float(model.predict(input_data)[0])
    return {"prediction": prediction}
