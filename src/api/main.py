from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.services import document_parser, risk_engine, summarizer
from src.models.project import Project, ProjectUploadResponse
from src.api.risk_score_api import router as risk_score_router
from src.api.doc_risk_api import router as doc_risk_router
from src.api.voice_risk_api import router as voice_risk_router
from src.api.anomaly_api import router as anomaly_router
import yaml
import os
from typing import List

app = FastAPI(title="ProjectPulse.AI API")
security = HTTPBasic()

# Load config
def get_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

config = get_config()
ADMIN_USER = config.get("admin_user", "admin")
ADMIN_PASS = config.get("admin_password", "admin123")

# Basic Auth
def admin_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_user = credentials.username == ADMIN_USER
    correct_pass = credentials.password == ADMIN_PASS
    if not (correct_user and correct_pass):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return credentials.username

app.include_router(risk_score_router)
app.include_router(doc_risk_router)
app.include_router(voice_risk_router)
app.include_router(anomaly_router)

@app.post("/admin/upload_project", response_model=ProjectUploadResponse, tags=["Admin"])
def upload_project(file: UploadFile = File(...), username: str = Depends(admin_auth)):
    """Admin uploads a new project document."""
    # Save file to /data
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    # Parse document
    project_data = document_parser.parse_document(file_path)
    # Save project metadata (placeholder)
    # ...
    return ProjectUploadResponse(filename=file.filename, parsed=project_data)

@app.post("/login", tags=["Admin"])
def login(credentials: HTTPBasicCredentials = Depends(security)):
    admin_auth(credentials)
    return {"message": "Login successful"}

@app.get("/projects", response_model=List[Project], tags=["Projects"])
def list_projects():
    # Placeholder: return all projects (mock)
    return []

@app.post("/summarize", tags=["AI"])
def summarize(file: UploadFile = File(...), stakeholder_role: str = "management"):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    summary = summarizer.summarize_document(file_path, stakeholder_role)
    return summary

@app.post("/risk_signals", tags=["AI"])
def risk_signals(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    project_data = document_parser.parse_document(file_path)
    risks = risk_engine.compute_risk_signals(project_data)
    return risks