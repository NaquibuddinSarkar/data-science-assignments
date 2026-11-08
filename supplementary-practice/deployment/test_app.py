"""Basic endpoint checks for the educational FastAPI example."""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "train_model.py")],
    check=True,
    cwd=HERE,
)

sys.path.insert(0, str(HERE))
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health_reports_loaded_model():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict_returns_class_and_probabilities():
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["predicted_class"] in {"setosa", "versicolor", "virginica"}
    assert abs(sum(payload["class_probabilities"].values()) - 1.0) < 1e-6


def test_predict_rejects_wrong_number_of_features():
    response = client.post("/predict", json={"features": [5.1, 3.5]})
    assert response.status_code == 422
