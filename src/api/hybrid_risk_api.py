from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, Dict
from src.services.hybrid_risk import compute_composite_risk

router = APIRouter()

class HybridRiskInput(BaseModel):
    risk_probability: Optional[float] = Field(None)
    doc_risk_flags: Optional[int] = Field(None)
    voice_risk_class: Optional[str] = Field(None)
    anomaly_score: Optional[float] = Field(None)
    fraud_flags: Optional[int] = Field(None)
    delay_probability: Optional[float] = Field(None)
    weights: Optional[Dict[str, float]] = Field(None)

@router.post("/composite_risk_score", tags=["Meta"])
def composite_risk_score(input: HybridRiskInput):
    result = compute_composite_risk(**input.dict())
    return result