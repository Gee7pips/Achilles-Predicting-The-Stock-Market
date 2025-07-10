# ProjectPulse.AI – MVP

ProjectPulse.AI is an AI-powered project monitoring and oversight platform designed for Development Finance Institutions (DFIs) such as DBSA, AfDB, and municipalities.

## Features (MVP)

1. Upload & parse project documents (PDF, Word, Excel, scanned)
2. Risk signal engine (rule-based + ML placeholder)
3. Interactive dashboard built with Streamlit
4. AI summarisation & voice note parser (OpenAI placeholder)
5. Admin panel
6. Dockerised deployment

## Quick start

### Prerequisites
- Docker + Docker Compose **OR**
- Python 3.11+

### 1. Clone & install

```bash
git clone <repo>
cd projectpulse_ai
pip install -r requirements.txt
```

### 2. Run locally

```bash
uvicorn src.main:app --reload
# In a separate terminal
streamlit run src/dashboard/app.py
```

### 3. Run with Docker

```bash
docker compose up --build
```

The FastAPI app is served at http://localhost:8000  
The Streamlit dashboard is served at http://localhost:8501  

## Folder structure
```
├── config/               # YAML & environment configs
├── data/                 # Sample data & uploaded docs
├── src/
│   ├── api/              # FastAPI routers
│   ├── services/         # Business logic
│   ├── models/           # ML models & helpers
│   └── dashboard/        # Streamlit app
└── notebooks/            # Exploration notebooks
```

## Environment variables
See `config/config.yaml`.

## License
MIT