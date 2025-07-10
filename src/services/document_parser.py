import os
from typing import Dict, Any

def parse_document(file_path: str) -> Dict[str, Any]:
    # Placeholder: extract fields from filename for demo
    filename = os.path.basename(file_path)
    return {
        "project_name": filename.split("_")[0] if "_" in filename else filename,
        "contractor": "ACME Corp",
        "budget": 1000000.0,
        "milestones": ["Kickoff", "Phase 1", "Phase 2", "Completion"],
        "document_type": "contract" if "contract" in filename.lower() else "report"
    }