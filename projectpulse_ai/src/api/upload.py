from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import List
from pathlib import Path
import shutil

from src.services.document_parser import parse_document, classify_document
from src.services.risk_engine import register_document_features

router = APIRouter(tags=["Upload & Parse"])

UPLOAD_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", summary="Upload project documents")
async def upload_documents(files: List[UploadFile] = File(...)):
    responses = []
    for file in files:
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Parse & classify
        try:
            content, fields = parse_document(file_path)
            doc_type = classify_document(content)
            # Register with risk engine
            register_document_features(fields)
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to parse {file.filename}: {exc}",
            )

        responses.append(
            {
                "filename": file.filename,
                "document_type": doc_type,
                "extracted_fields": fields,
            }
        )
    return {"uploaded": responses}