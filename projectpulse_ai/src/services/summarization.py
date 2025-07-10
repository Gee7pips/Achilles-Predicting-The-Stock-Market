"""Summarization service using OpenAI placeholder."""
from pathlib import Path
import yaml
from typing import Dict

CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "config.yaml"
with open(CONFIG_PATH, "r") as cfg_file:
    config = yaml.safe_load(cfg_file)


def summarize_text(text: str) -> str:
    """Placeholder summarisation – replace with OpenAI call."""
    # In real life you would do:
    # import openai
    # openai.api_key = config["OPENAI_API_KEY"]
    # response = openai.ChatCompletion.create(...)
    # return response.choices[0].message.content
    words = text.split()
    snippet = " ".join(words[:60]) + ("..." if len(words) > 60 else "")
    return f"Summary (mock): {snippet}"


def summarize_document(path: Path) -> Dict[str, str]:
    from src.services.document_parser import parse_document, classify_document

    content, _ = parse_document(path)
    summary = summarize_text(content)
    return {"summary": summary, "document_type": classify_document(content)}