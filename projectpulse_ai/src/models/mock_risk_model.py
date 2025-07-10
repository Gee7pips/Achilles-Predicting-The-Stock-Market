"""Generate a mock logistic regression model and persist it so the placeholder is available."""
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

MODEL_PATH = Path(__file__).resolve().parent / "mock_risk_model.pkl"


def _generate_model() -> None:
    X = np.random.rand(200, 5)
    y = np.random.randint(0, 2, size=200)
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)


if not MODEL_PATH.exists():
    _generate_model()