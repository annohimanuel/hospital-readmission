from pydantic import BaseModel

class PatientFeatures(BaseModel):
    age: float
    sex: str
    race: str
    insurance_type: str
    glucose: float
    systolic_bp: float
    diastolic_bp: float
    cholesterol: float
    bmi: float
    comorbidity_score: float
    visit_type: str
    primary_diagnosis: str
    hospital_id: str

class PredictionOut(BaseModel):
    readmission_probability: float
    predicted_readmission: int
    threshold: float
