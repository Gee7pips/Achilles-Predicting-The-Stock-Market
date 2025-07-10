from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    id: str
    name: str
    contractor: str
    budget: float
    milestones: List[str]
    documents: List[str]
    risk_score: float