import streamlit as st
import pandas as pd
from src.services import summarizer

# Mock project data
data = [
    {"id": 1, "name": "Water Plant Upgrade", "contractor": "ACME Corp", "budget": 1200000, "risk_score": 0.8, "milestones": ["Kickoff", "Phase 1", "Phase 2", "Completion"], "documents": ["contract_WaterPlant.pdf", "report_WaterPlant.pdf"]},
    {"id": 2, "name": "Solar Farm", "contractor": "SunPower Ltd", "budget": 800000, "risk_score": 0.3, "milestones": ["Kickoff", "Phase 1", "Completion"], "documents": ["contract_SolarFarm.pdf"]},
]
df = pd.DataFrame(data)

st.title("ProjectPulse.AI Dashboard")
st.write("AI-powered project monitoring for DFIs and municipalities.")

st.header("Project List")
sort_by = st.selectbox("Sort by", ["risk_score", "budget", "name"])
df_sorted = df.sort_values(by=sort_by, ascending=(sort_by!="risk_score"))
st.dataframe(df_sorted[["id", "name", "contractor", "budget", "risk_score"]], use_container_width=True)

project_id = st.selectbox("Select a project to drill down", df_sorted["id"])
project = next((p for p in data if p["id"] == project_id), None)

if project:
    st.subheader(f"Project: {project['name']}")
    st.write(f"**Contractor:** {project['contractor']}")
    st.write(f"**Budget:** ${project['budget']:,.0f}")
    st.write(f"**Risk Score:** {project['risk_score']}")
    st.write(f"**Milestones:** {', '.join(project['milestones'])}")
    st.write("**Documents:**")
    for doc in project["documents"]:
        st.write(f"- {doc}")
    st.write("---")
    st.write("### Timeline of Events (Mock)")
    st.write("- 2024-01-10: Kickoff\n- 2024-02-15: Phase 1 Complete\n- 2024-03-20: Phase 2 Complete\n- 2024-04-30: Project Completion")
    st.write("### Flagged Risks (Mock)")
    if project["risk_score"] > 0.5:
        st.error("Budget overrun risk detected.")
    else:
        st.success("No major risks flagged.")
    st.write("### AI-Generated Summary (Mock)")
    summary = summarizer.summarize_document(project["documents"][0], stakeholder_role="management")
    st.info(summary["summary"])
    st.write("**Risks:**", summary["risks"])
    st.write("**Action Items:**", summary["action_items"])
    st.write("**Stakeholder Update:**", summary["stakeholder_update"])