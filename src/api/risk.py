from fastapi import APIRouter
from src.services import risk_engine

router = APIRouter()

@router.get("/score/{project_id}")
def get_risk_score(project_id: str):
    return risk_engine.get_risk_score(project_id)

@router.get("/flags/{project_id}")
def get_risk_flags(project_id: str):
    return risk_engine.get_risk_flags(project_id)