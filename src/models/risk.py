from pydantic import BaseModel

class RiskFlag(BaseModel):
    type: str
    flagged: bool

class RiskScore(BaseModel):
    project_id: str
    risk_score: float
    ml_score: float