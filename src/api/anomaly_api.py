from fastapi import APIRouter
from pydantic import BaseModel
from src.models.anomaly import predict_anomaly, FEATURES

router = APIRouter()

class AnomalyInput(BaseModel):
    budget_variance: float
    schedule_slippage: float
    vendor_history_score: float
    missing_docs: int
    variation_orders: int
    country: str
    project_type: str
    category: str

@router.post("/detect_anomaly", tags=["ML"])
def detect_anomaly(input: AnomalyInput):
    result = predict_anomaly(input.dict())
    return result