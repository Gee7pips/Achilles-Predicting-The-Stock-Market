import os
from typing import Dict, Any, List

MOCK_AUDIO_TRANSCRIPT = "Project update: The contractor has completed Phase 1, but there are delays in Phase 2 due to late material delivery. Budget usage is at 60%. Recommend reviewing the timeline and engaging with the supplier to avoid further delays."

RISK_KEYWORDS = {
    "urgent": ["urgent", "immediate action", "critical"],
    "problem": ["delay", "issue", "problem", "late", "over budget", "failed"],
    "on_track": ["on track", "progressing well", "completed", "finished"]
}

BLAME_KEYWORDS = ["the contractor failed", "due to supplier", "not our fault", "because of vendor"]
EXCUSE_KEYWORDS = ["waiting for", "delayed by", "unable to", "pending"]
LACK_PROGRESS_KEYWORDS = ["no progress", "nothing done", "stalled"]


def transcribe_audio(file_path: str) -> str:
    # MVP: Return mock transcript for audio, real for txt
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext in [".wav", ".mp3"]:
        return MOCK_AUDIO_TRANSCRIPT
    else:
        return ""

def summarize_text(text: str) -> str:
    # MVP: Return first sentence or up to 20 words
    return text.split(".")[0][:120] + "."

def classify_risk(text: str) -> str:
    text_l = text.lower()
    for k, kws in RISK_KEYWORDS.items():
        if any(kw in text_l for kw in kws):
            return k
    return "on_track"

def detect_flags(text: str) -> List[str]:
    flags = []
    text_l = text.lower()
    if any(kw in text_l for kw in BLAME_KEYWORDS):
        flags.append("blame-shifting")
    if any(kw in text_l for kw in EXCUSE_KEYWORDS):
        flags.append("excuse")
    if any(kw in text_l for kw in LACK_PROGRESS_KEYWORDS):
        flags.append("lack of progress")
    return flags

def extract_action_items(text: str) -> List[str]:
    # MVP: Extract sentences with 'recommend', 'should', 'need to'
    items = []
    for sent in text.split("."):
        if any(kw in sent.lower() for kw in ["recommend", "should", "need to"]):
            items.append(sent.strip())
    return items

def analyze_voice_note(file_path: str) -> Dict[str, Any]:
    transcript = transcribe_audio(file_path)
    summary = summarize_text(transcript)
    risk_class = classify_risk(transcript)
    flags = detect_flags(transcript)
    action_items = extract_action_items(transcript)
    return {
        "transcript": transcript,
        "summary": summary,
        "risk_class": risk_class,
        "action_items": action_items,
        "flags": flags
    }