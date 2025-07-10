from fastapi import APIRouter
from src.services import project_service

router = APIRouter()

@router.get("/")
def list_projects():
    return project_service.get_all_projects()

@router.get("/{project_id}")
def get_project(project_id: str):
    return project_service.get_project_details(project_id)