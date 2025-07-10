def get_risk_score(project_id):
    # Placeholder: use mock ML model or rules
    return {"project_id": project_id, "risk_score": 0.2, "ml_score": 0.15}

def get_risk_flags(project_id):
    # Placeholder: return sample risk flags
    return [
        {"type": "budget_overrun", "flagged": False},
        {"type": "schedule_delay", "flagged": True}
    ]