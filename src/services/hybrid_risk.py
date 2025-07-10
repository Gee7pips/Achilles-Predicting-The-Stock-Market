from typing import Dict, Any

def compute_composite_risk(
    risk_probability: float = None,
    doc_risk_flags: int = None,
    voice_risk_class: str = None,
    anomaly_score: float = None,
    fraud_flags: int = None,
    delay_probability: float = None,
    weights: Dict[str, float] = None
) -> Dict[str, Any]:
    # Default weights
    default_weights = {
        "risk_probability": 0.25,
        "doc_risk_flags": 0.15,
        "voice_risk_class": 0.15,
        "anomaly_score": 0.15,
        "fraud_flags": 0.15,
        "delay_probability": 0.15
    }
    if weights:
        default_weights.update(weights)
    # Normalize weights
    total = sum(default_weights.values())
    for k in default_weights:
        default_weights[k] /= total
    # Map voice_risk_class to numeric
    voice_map = {"urgent": 1.0, "problem": 0.7, "on_track": 0.0}
    voice_score = voice_map.get(voice_risk_class, 0.0) if voice_risk_class else 0.0
    # Compose features
    features = {
        "risk_probability": risk_probability if risk_probability is not None else 0.0,
        "doc_risk_flags": min(doc_risk_flags or 0, 3) / 3.0,  # scale 0-1
        "voice_risk_class": voice_score,
        "anomaly_score": max(0.0, min(1.0, 1 - (anomaly_score or 0))),  # higher anomaly = higher risk
        "fraud_flags": min(fraud_flags or 0, 3) / 3.0,  # scale 0-1
        "delay_probability": delay_probability if delay_probability is not None else 0.0
    }
    # Weighted sum
    composite = sum(features[k] * default_weights[k] for k in features)
    return {"composite_risk_score": composite, "breakdown": features, "weights": default_weights}