"""Train and save a small educational Iris classifier."""
from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "iris_model.joblib"

def main() -> None:
    iris = load_iris()
    model = RandomForestClassifier(
        n_estimators=200, random_state=42, min_samples_leaf=2
    )
    model.fit(iris.data, iris.target)
    joblib.dump(
        {"model": model, "target_names": iris.target_names.tolist()},
        MODEL_PATH
    )
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    main()
