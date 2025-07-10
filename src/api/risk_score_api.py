from fastapi import APIRouter
from pydantic import BaseModel
from src.models.risk_score import predict_risk, FEATURES

router = APIRouter()

class RiskScoreInput(BaseModel):
    budget_variance: float
    schedule_slippage: float
    vendor_history_score: float
    missing_docs: int
    variation_orders: int
    country: str
    project_type: str
    category: str

@router.post("/predict_risk_score", tags=["ML"])
def predict_risk_score(input: RiskScoreInput):
    result = predict_risk(input.dict())
    return result