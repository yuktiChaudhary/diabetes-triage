import os
import subprocess
import sys


# testing the v0.2 model separately
def test_v2_api():
    code = """
import math
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

payload = {
    "age": 0.02,
    "sex": -0.044,
    "bmi": 0.06,
    "bp": -0.03,
    "s1": -0.02,
    "s2": 0.03,
    "s3": -0.02,
    "s4": 0.02,
    "s5": 0.02,
    "s6": -0.001,
}

# check the model version
response = client.get("/health")
assert response.status_code == 200
assert response.json() == {"status": "ok", "model_version": "v0.2"}

# check if prediction works
response = client.post("/predict", json=payload)
assert response.status_code == 200
prediction = response.json()["prediction"]
assert isinstance(prediction, (int, float))
assert math.isfinite(prediction)

# check missing feature
missing_payload = payload.copy()
missing_payload.pop("s6")

response = client.post("/predict", json=missing_payload)
assert response.status_code == 422
assert any(e["loc"][-1] == "s6" for e in response.json()["detail"])

# check wrong data type
wrong_payload = payload.copy()
wrong_payload["bmi"] = "not-a-number"

response = client.post("/predict", json=wrong_payload)
assert response.status_code == 422

# check extra feature
extra_payload = payload.copy()
extra_payload["unexpected"] = 123

response = client.post("/predict", json=extra_payload)
assert response.status_code == 422
"""

    env = os.environ.copy()
    env["MODEL_VERSION"] = "v0.2"

    result = subprocess.run(
        [sys.executable, "-c", code],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
