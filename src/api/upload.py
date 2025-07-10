from fastapi import APIRouter, File, UploadFile, Form
from src.services import document_parser
from typing import List

router = APIRouter()

@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    result = await document_parser.parse_document(file)
    return result