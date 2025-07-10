import pandas as pd
import os
import json
from typing import Dict, Any
from prophet import Prophet
import joblib

MODEL_PATH = "data/mock_delay_model.pkl"
DATA_PATH = "data/progress_logs.csv"

# For MVP, forecast project completion date and delay days

def train_and_save_model():
    df = pd.read_csv(DATA_PATH)
    # For Prophet: ds=date, y=progress_percent
    df = df[df["project_id"] == 1]  # MVP: train on project 1
    df = df[["date", "progress_percent"]].rename(columns={"date": "ds", "progress_percent": "y"})
    model = Prophet()
    model.fit(df)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_and_save_model()
    return joblib.load(MODEL_PATH)

model = load_model()

def forecast_delay(input_path: str) -> Dict[str, Any]:
    ext = os.path.splitext(input_path)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(input_path)
    elif ext == ".json":
        with open(input_path, "r") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    else:
        raise ValueError("Unsupported file format")
    # For MVP: forecast for the next 30 days
    last_date = pd.to_datetime(df["date"].max())
    future = pd.DataFrame({"ds": pd.date_range(last_date, periods=30, freq="D")})
    forecast = model.predict(future)
    # Find when yhat crosses 100 (project complete)
    complete = forecast[forecast["yhat"] >= 100]
    if not complete.empty:
        completion_date = complete.iloc[0]["ds"]
        planned_date = last_date + pd.Timedelta(days=15)  # MVP: assume planned +15d
        delay_days = (completion_date - planned_date).days
        delay_prob = float(delay_days > 0)
    else:
        completion_date = None
        delay_days = None
        delay_prob = 1.0
    return {
        "forecasted_completion_date": str(completion_date) if completion_date is not None else None,
        "delay_days": delay_days,
        "delay_probability": delay_prob
    }