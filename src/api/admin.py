from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.services import admin_service
import secrets

router = APIRouter()
security = HTTPBasic()

@router.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    if not admin_service.verify_admin(credentials.username, credentials.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful"}