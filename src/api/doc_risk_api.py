from fastapi import APIRouter, UploadFile, File
from src.services.doc_risk_extractor import extract_doc_risks
import os

router = APIRouter()

@router.post("/extract_doc_risks", tags=["NLP"])
def extract_doc_risks_endpoint(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    result = extract_doc_risks(file_path)
    return result