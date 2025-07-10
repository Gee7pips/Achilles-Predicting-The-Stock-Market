"""Streamlit dashboard for ProjectPulse.AI MVP."""
import streamlit as st
import requests

API_URL = "http://localhost:8000/api"

st.set_page_config(page_title="ProjectPulse.AI Dashboard", layout="wide")

st.title("📊 ProjectPulse.AI – Risk Dashboard")

# Fetch projects with refresh
def fetch_projects():
    with st.spinner("Fetching projects..."):
        try:
            resp = requests.get(f"{API_URL}/projects", timeout=5)
            resp.raise_for_status()
            return resp.json().get("projects", [])
        except requests.exceptions.ConnectionError:
            st.error("API server unreachable. Is FastAPI running?")
        except requests.exceptions.Timeout:
            st.error("Request timed out while contacting API.")
        except Exception as exc:
            st.error(f"Could not fetch projects: {exc}")
        return []


# Refresh button
if st.button("🔄 Refresh"):
    st.experimental_rerun()

projects = fetch_projects()

# Table view
st.subheader("Projects")
if projects:
    st.dataframe(
        [{"ID": p["id"], "Name": p["name"], "Risk Score": p["risk_score"]} for p in projects],
        use_container_width=True,
    )
else:
    st.info("No projects available.")

# Drill-down selector
project_options = {p["name"]: p for p in projects}
selection = st.selectbox("Select a project to view details", list(project_options.keys())) if project_options else None

if selection:
    project = project_options[selection]
    st.header(f"Project: {project['name']}")
    risk_score = project.get("risk_score", 0)
    st.metric("Risk Score", f"{risk_score:.2f}")
    st.progress(risk_score)

    st.subheader("Documents")
    for doc in project.get("documents", []):
        st.markdown(f"- **{doc.get('document_type', 'doc')}** – extracted fields: {doc}")