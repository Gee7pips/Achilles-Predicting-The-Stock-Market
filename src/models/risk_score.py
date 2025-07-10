import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
import joblib
import os

MODEL_PATH = "data/mock_risk_model.pkl"
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
    y = df["label"]
    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL)
    ], remainder="passthrough")
    pipeline = Pipeline([
        ("pre", preprocessor),
        ("clf", LogisticRegression(solver="liblinear"))
    ])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Risk Score Model Accuracy: {acc:.2f}")
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_and_save_model()
    return joblib.load(MODEL_PATH)

model = load_model()

def predict_risk(input_data: dict) -> dict:
    X = pd.DataFrame([input_data])[FEATURES]
    prob = model.predict_proba(X)[0][1]
    pred = model.predict(X)[0]
    return {"risk_probability": float(prob), "risk_class": int(pred)}