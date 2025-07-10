import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import os

MODEL_PATH = "data/mock_anomaly_model.pkl"
DATA_PATH = "data/mock_structured_data.csv"

FEATURES = [
    "budget_variance",
    "schedule_slippage",
    "vendor_history_score",
    "missing_docs",
    "variation_orders",
    "country",
    "project_type",
    "category"
]

CATEGORICAL = ["country", "project_type", "category"]
NUMERIC = ["budget_variance", "schedule_slippage", "vendor_history_score", "missing_docs", "variation_orders"]

def train_and_save_model():
    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]
    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)
    ], remainder="passthrough")
    pipeline = Pipeline([
        ("pre", preprocessor),
        ("clf", IsolationForest(contamination=0.2, random_state=42))
    ])
    pipeline.fit(X)
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_and_save_model()
    return joblib.load(MODEL_PATH)

model = load_model()

def predict_anomaly(input_data: dict) -> dict:
    X = pd.DataFrame([input_data])[FEATURES]
    score = model.decision_function(X)[0]
    is_anomaly = int(model.predict(X)[0] == -1)
    return {"anomaly_score": float(score), "is_anomaly": bool(is_anomaly)}