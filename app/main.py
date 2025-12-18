from fastapi import FastAPI
from app.schemas import PredictRequest, PredictResponse
from app.predict import predict_one

app = FastAPI(title="Hospital Readmission API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return predict_one(req)
