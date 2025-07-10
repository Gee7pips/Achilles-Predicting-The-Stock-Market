from fastapi import APIRouter, UploadFile, File
from src.services.voice_risk import analyze_voice_note
import os

router = APIRouter()

@router.post("/voice_note_risk", tags=["NLP"])
def voice_note_risk_endpoint(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    result = analyze_voice_note(file_path)
    return result