# Supplementary FastAPI model-serving example

A minimal local API example using the Iris dataset. It trains a Random Forest model, saves it with joblib, and serves predictions through FastAPI.

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` for interactive API documentation.

## Test request

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

This example is educational. It is not hardened for production, authentication, sensitive data, high availability or adversarial inputs. The model is trained on the scikit-learn Iris sample dataset.
