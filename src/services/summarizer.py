from typing import Dict

def summarize_document(file_path: str, stakeholder_role: str = "management") -> Dict:
    # Placeholder: return a mock summary
    summary = f"Summary for {file_path} (role: {stakeholder_role})"
    risks = ["Budget overrun", "Schedule delay"]
    action_items = ["Review budget", "Update timeline"]
    stakeholder_update = f"Update for {stakeholder_role}: Focus on risks and next steps."
    return {
        "summary": summary,
        "risks": risks,
        "action_items": action_items,
        "stakeholder_update": stakeholder_update
    }