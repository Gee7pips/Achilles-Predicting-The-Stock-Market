from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from pathlib import Path
import yaml

from src.services.risk_engine import create_project

router = APIRouter(tags=["Admin"])
security = HTTPBasic()

# Load config
CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "config.yaml"
with open(CONFIG_PATH, "r") as cfg_file:
    config = yaml.safe_load(cfg_file)

ADMIN_USERNAME = config.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = config.get("ADMIN_PASSWORD", "admin123")


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.post("/admin/projects", summary="Create new project", dependencies=[Depends(verify_credentials)])
def admin_create_project(name: str):
    project_id = create_project(name)
    return {"project_id": project_id, "name": name}