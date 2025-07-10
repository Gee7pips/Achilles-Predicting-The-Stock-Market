import os
from typing import Dict, Any, List
import spacy
import re

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None
try:
    import docx
except ImportError:
    docx = None

nlp = spacy.load("en_core_web_sm")

RISKY_CLAUSES = [
    r"subject to",
    r"may be delayed",
    r"penalty waived",
    r"no tender required"
]

MISSING_ITEMS = ["signature", "payment", "insurance"]

def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf" and PyPDF2:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif ext == ".docx" and docx:
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def extract_entities(text: str) -> List[Dict[str, Any]]:
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

def flag_risky_clauses(text: str) -> List[str]:
    found = []
    for clause in RISKY_CLAUSES:
        if re.search(clause, text, re.IGNORECASE):
            found.append(clause)
    return found

def check_missing_items(text: str) -> List[str]:
    missing = []
    for item in MISSING_ITEMS:
        if item not in text.lower():
            missing.append(item)
    return missing

def extract_doc_risks(file_path: str) -> Dict[str, Any]:
    text = extract_text(file_path)
    entities = extract_entities(text)
    flagged_clauses = flag_risky_clauses(text)
    missing_items = check_missing_items(text)
    return {
        "entities": entities,
        "flagged_clauses": flagged_clauses,
        "missing_items": missing_items
    }