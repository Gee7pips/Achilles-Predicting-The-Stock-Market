from fastapi import APIRouter

from src.services.risk_engine import get_all_projects, get_project

router = APIRouter(tags=["Projects"])


@router.get("/projects", summary="List projects with risk scores")
def list_projects():
    return {"projects": get_all_projects()}


@router.get("/projects/{project_id}", summary="Project detail")
def project_detail(project_id: str):
    project = get_project(project_id)
    if project is None:
        return {"error": "Project not found"}
    return project