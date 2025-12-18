from fastapi import FastAPI
from app.schemas import PatientFeatures, PredictionOut
from app.predict import predict_one

app = FastAPI(title="Hospital Readmission API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOut)
def predict(req: PatientFeatures):
    return predict_one(req)
