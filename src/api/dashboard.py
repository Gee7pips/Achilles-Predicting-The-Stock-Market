import streamlit as st
import pandas as pd
from src.services import project_service, risk_engine

st.set_page_config(page_title="ProjectPulse.AI Dashboard", layout="wide")
st.title("ProjectPulse.AI - Project Risk Dashboard")

projects = project_service.get_all_projects()
df = pd.DataFrame(projects)

st.subheader("Projects")
st.dataframe(df.sort_values("risk_score", ascending=False), use_container_width=True)

project_ids = [p["id"] for p in projects]
selected_id = st.selectbox("Select a project to drill down", project_ids)

if selected_id:
    details = project_service.get_project_details(selected_id)
    st.write(f"## {details['name']}")
    st.write(f"**Contractor:** {details['contractor']}")
    st.write(f"**Budget:** ${details['budget']:,}")
    st.write(f"**Risk Score:** {details['risk_score']}")
    st.write("### Milestones")
    st.write(details['milestones'])
    st.write("### Uploaded Documents")
    st.write(details['documents'])
    st.write("### Flagged Risks")
    flags = risk_engine.get_risk_flags(selected_id)
    st.write(flags)
    st.write("### AI-Generated Summary")
    st.info("This is a placeholder for the AI-generated summary and action items.")