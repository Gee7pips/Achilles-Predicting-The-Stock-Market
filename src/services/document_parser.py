async def parse_document(file):
    # Placeholder: parse file, extract fields, OCR if needed, classify type
    return {
        "filename": file.filename,
        "fields": {"project_name": "Sample Project", "contractor": "ABC Ltd.", "budget": 1000000},
        "doc_type": "contract",
        "ocr_used": False
    }