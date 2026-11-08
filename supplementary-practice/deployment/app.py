"""Educational FastAPI wrapper for a locally trained Iris classifier."""
from pathlib import Path
from typing import Annotated
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "iris_model.joblib"

app = FastAPI(
    title="Iris Classification API",
    description="Educational example; not intended for production deployment.",
    version="1.0.0",
)
bundle = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

class PredictionRequest(BaseModel):
    features: Annotated[list[float], Field(min_length=4, max_length=4)]

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": bundle is not None}

@app.post("/predict")
def predict(request: PredictionRequest):
    if bundle is None:
        raise HTTPException(
            status_code=503,
            detail="Model not found. Run python train_model.py first."
        )
    model = bundle["model"]
    probabilities = model.predict_proba([request.features])[0]
    class_index = int(probabilities.argmax())
    return {
        "predicted_class": bundle["target_names"][class_index],
        "class_probabilities": {
            name: float(prob) for name, prob in zip(bundle["target_names"], probabilities)
        },
    }
