from typing import Dict, Any

def compute_risk_signals(project_data: Dict[str, Any]) -> Dict[str, Any]:
    # Simple rules for demo
    risks = []
    if project_data.get("budget", 0) > 900000:
        risks.append("High budget - possible overrun")
    if "Phase 2" not in project_data.get("milestones", []):
        risks.append("Missing milestone: Phase 2")
    # Mock ML risk score
    risk_score = 0.7 if risks else 0.2
    return {"risks": risks, "risk_score": risk_score}