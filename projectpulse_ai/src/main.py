import yaml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from src.api import upload, projects, admin

# Load configuration
CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "config.yaml"
with open(CONFIG_PATH, "r") as cfg_file:
    config = yaml.safe_load(cfg_file)

app = FastAPI(title="ProjectPulse.AI API", version="0.1.0")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(upload.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(admin.router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}