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

1. System packages (for OCR & PDF):
   - Ubuntu / Debian
     ```bash
     sudo apt update && sudo apt install -y poppler-utils tesseract-ocr ffmpeg
     ```
   - macOS (Homebrew)
     ```bash
     brew install poppler tesseract ffmpeg
     ```

2. Docker + Docker Compose **OR** Python 3.11+

3. (Optional) A Google API-key if you want SpeechRecognition to use Google Cloud Speech.

### 1. Clone & install

```bash
git clone <repo>
cd projectpulse_ai
pip install -r requirements.txt
# generate mock model (optional)
python -c "import src.models"
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

## Sample data
The `data/samples/` directory includes placeholder files:

* `sample_invoice.txt` – mimics an invoice document
* `sample_contract.txt` – mimics a contract document
* `sample_voice_note.txt` – sample voice-note transcript

Upload these via the `/api/upload` or `/api/upload/voice` endpoints (or add your own files in PDF/DOCX/XLSX/WAV format).

### API endpoints (selection)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload one or more project documents |
| POST | `/api/upload/voice` | Upload voice notes (WAV/MP3) |
| GET  | `/api/projects` | List projects + risk scores |
| GET | `/api/projects/{id}` | Project detail |
| POST | `/api/admin/projects` | Create project (Basic Auth) |

### Environment variables / Config

`config/config.yaml` holds default values:

```yaml
OPENAI_API_KEY: "your_api_key_here"
ADMIN_USERNAME: "admin"
ADMIN_PASSWORD: "admin123"
MODEL_PATH: "src/models/mock_risk_model.pkl"
```

You can either edit this file or export environment variables of the same names to override.