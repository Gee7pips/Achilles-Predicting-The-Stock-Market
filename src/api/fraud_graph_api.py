from fastapi import APIRouter, UploadFile, File
from src.services.fraud_graph import analyze_vendor_network
import os

router = APIRouter()

@router.post("/detect_fraud", tags=["GraphML"])
def detect_fraud_endpoint(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    result = analyze_vendor_network(file_path)
    return result