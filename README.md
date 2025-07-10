# ProjectPulse.AI MVP

ProjectPulse.AI is an AI-powered project monitoring and oversight platform designed for Development Finance Institutions (DFIs) and municipalities. It enables automated document parsing, risk signal detection, AI summarization, and interactive dashboards for project oversight.

## Features
- **Upload & Parse Project Documents** (PDF, Word, Excel, OCR)
- **Risk Signal Engine** (budget overruns, delays, missing docs, suspicious vendors)
- **ML Risk Probability Score** (logistic regression placeholder)
- **Interactive Dashboard** (Streamlit)
- **AI Summarization & Voice Note Parsing** (OpenAI API or placeholder)
- **Admin Panel** (basic auth, project upload, risk dashboard)

## Project Structure
```
/src
  /api         # FastAPI endpoints
  /services    # Business logic, ML, NLP, OCR, summarization
  /models      # Pydantic models, ML models
/config        # YAML config for environment variables
/data          # Sample and uploaded data
/notebooks     # Jupyter/analysis notebooks
```

## Install & Run

### 1. Clone & Setup
```bash
git clone <repo-url>
cd ProjectPulse.AI
```

### 2. Build & Run (Docker)
```bash
docker-compose up --build
```

### 3. Local Dev (Python 3.9+)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.main:app --reload
streamlit run src/api/dashboard.py
```

## Sample Data
See `/data/` for example project documents and mock ML model.

---
For more, see inline comments and docstrings in the codebase.
