from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pathlib import Path
import shutil

from src.services.voice_parser import transcribe_audio
from src.services.summarization import summarize_text

router = APIRouter(tags=["Voice Notes"])

VOICE_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "voice_uploads"
VOICE_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/voice/upload", summary="Upload voice note and get transcription & summary")
async def upload_voice(file: UploadFile = File(...)):
    file_path = VOICE_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        transcript = transcribe_audio(file_path)
        summary = summarize_text(transcript)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process voice note: {exc}",
        )

    return {
        "filename": file.filename,
        "transcript": transcript,
        "summary": summary,
    }