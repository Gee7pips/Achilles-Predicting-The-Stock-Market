"""Risk signal engine – very light rule based + placeholder ML probability."""
from __future__ import annotations

import random
import uuid
from typing import Dict, List, Any

# In-memory store (replace with database in real implementation)
_projects: Dict[str, Dict[str, Any]] = {}


# --- Core helpers ---------------------------------------------------------

def _calculate_risk_score(features: Dict[str, str]) -> float:
    """Very naive scoring for MVP."""
    score = 0.0
    # Basic rules
    budget_text = features.get("budget", "").replace(",", "").replace("$", "")
    try:
        budget_value = float(budget_text)
        if budget_value > 1_000_000:  # arbitrary threshold
            score += 0.3
    except ValueError:
        pass

    milestones = features.get("milestones", "")
    if "delay" in milestones.lower():
        score += 0.3

    # Random element to mimic ML probability
    score += random.uniform(0, 0.4)
    return min(score, 1.0)


# --- Public API -----------------------------------------------------------

def create_project(name: str) -> str:
    project_id = str(uuid.uuid4())
    _projects[project_id] = {
        "id": project_id,
        "name": name,
        "documents": [],
        "risk_score": 0.0,
    }
    return project_id


def register_document_features(fields: Dict[str, str]):
    project_name = fields.get("project_name")
    if not project_name:
        # Cannot associate without project name
        return

    # Find project by name, else create
    project_id = None
    for pid, info in _projects.items():
        if info["name"].lower() == project_name.lower():
            project_id = pid
            break
    if project_id is None:
        project_id = create_project(project_name)

    project = _projects[project_id]
    project["documents"].append(fields)
    # Recalculate risk
    project["risk_score"] = _calculate_risk_score(fields)


def get_all_projects() -> List[Dict[str, Any]]:
    return list(_projects.values())


def get_project(project_id: str) -> Dict[str, Any] | None:
    return _projects.get(project_id)