from fastapi import FastAPI
from app.schemas import PatientFeatures, PredictionOut
from app.predict import predict_one, load_artifacts

app = FastAPI(title="Hospital Readmission Risk API")

@app.get("/health")
def health():
    load_artifacts()
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOut)
def predict(features: PatientFeatures):
    proba, pred, thr = predict_one(features.model_dump())
    return PredictionOut(
        readmission_probability=proba,
        predicted_readmission=pred,
        threshold=thr
    )
