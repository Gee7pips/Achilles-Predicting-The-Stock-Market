from pydantic import BaseModel
from typing import Dict

class Document(BaseModel):
    filename: str
    fields: Dict[str, str]
    doc_type: str
    ocr_used: bool