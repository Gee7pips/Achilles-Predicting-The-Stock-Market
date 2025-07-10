"""Voice note parsing service (placeholder).

Uses SpeechRecognition to transcribe WAV/MP3 files. For unsupported formats, will return empty string.
"""
from pathlib import Path

import speech_recognition as sr
from pydub import AudioSegment


def _convert_to_wav(path: Path) -> Path:
    """Convert audio file to WAV if needed and return new path (may be same)."""
    if path.suffix.lower() == ".wav":
        return path
    wav_path = path.with_suffix(".wav")
    audio = AudioSegment.from_file(str(path))
    audio.export(str(wav_path), format="wav")
    return wav_path


def transcribe_voice(path: Path) -> str:
    """Return transcribed text using local recognizer (Sphinx) as placeholder."""
    recognizer = sr.Recognizer()
    wav_path = _convert_to_wav(path)
    with sr.AudioFile(str(wav_path)) as source:
        audio_data = recognizer.record(source)
    try:
        # Using pocketsphinx (offline) if installed, else Google (requires internet)
        try:
            return recognizer.recognize_sphinx(audio_data)
        except sr.RequestError:
            return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return ""