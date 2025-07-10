from fastapi import FastAPI
from src.api import upload, projects, risk, admin

app = FastAPI(title="ProjectPulse.AI")

app.include_router(upload.router, prefix="/upload", tags=["Upload & Parse"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(risk.router, prefix="/risk", tags=["Risk Engine"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])