def get_all_projects():
    return [
        {"id": "1", "name": "Sample Project", "risk_score": 0.2},
        {"id": "2", "name": "Demo Dam", "risk_score": 0.7}
    ]

def get_project_details(project_id):
    # Placeholder: return details for a project
    return {
        "id": project_id,
        "name": "Sample Project",
        "contractor": "ABC Ltd.",
        "budget": 1000000,
        "milestones": ["Start", "Phase 1", "Phase 2", "Complete"],
        "documents": [],
        "risk_score": 0.2
    }