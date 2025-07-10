from pydantic import BaseModel
from typing import List, Dict, Any

class Project(BaseModel):
    id: int
    name: str
    contractor: str
    budget: float
    milestones: List[str]
    risk_score: float
    documents: List[str]

class ProjectUploadResponse(BaseModel):
    filename: str
    parsed: Dict[str, Any]