import json
import joblib
import pandas as pd
import os

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths to artifacts
MODEL_PATH = os.path.join(BASE_DIR, "..", "artifacts", "model.pkl")
THRESH_PATH = os.path.join(BASE_DIR, "..", "artifacts", "threshold.json")

_model = None
_threshold = None

def load_artifacts():
    global _model, _threshold
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _threshold is None:
        with open(THRESH_PATH, "r") as f:
            _threshold = float(json.load(f)["threshold"])
    return _model, _threshold

def predict_one(features: dict):
    model, threshold = load_artifacts()
    X = pd.DataFrame([features])
    proba = float(model.predict_proba(X)[:, 1][0])
    pred = int(proba >= threshold)
    return {
        "readmission_probability": proba,
        "predicted_readmission": pred,
        "threshold": threshold
    }
