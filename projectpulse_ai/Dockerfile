# syntax=docker/dockerfile:1

FROM python:3.11-slim

# Install system dependencies for OCR, PDF, and audio processing
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        poppler-utils \
        tesseract-ocr \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["bash", "-c", "uvicorn src.main:app --host 0.0.0.0 --port 8000 & streamlit run src/dashboard/app.py --server.port 8501 --server.headless true"]