# Hospital Readmission Risk Modeling (30-Day) — Causal + ML + API

Production-style healthcare data science project that analyzes and predicts 30-day hospital readmissions, then serves real-time inference through a FastAPI endpoint.

## What this project answers
- Which clinical + demographic factors are associated with 30-day readmission?
- Did an intervention reduce readmission risk? (Difference-in-Differences)
- Can we predict readmission risk reliably enough to support operational workflows?
- What threshold should be used when the business goal is to minimize missed readmissions?

## Methods implemented
- Data integrity checks + exploratory analysis
- Hypothesis testing (continuous + categorical)
- Causal inference: Difference-in-Differences (logistic framework with controls)
- ML modeling: Logistic Regression baseline, Random Forest, XGBoost
- Model evaluation: ROC-AUC, Precision/Recall, threshold selection
- Explainability: SHAP (global + local)

## Key deliverable
FastAPI service that returns:
- `readmission_probability`
- `predicted_readmission` (based on a frozen business threshold)

### API
- `GET /health`
- `POST /predict`

Example request body:
```json
{
  "age": 67,
  "sex": "F",
  "race": "Black",
  "insurance_type": "Medicare",
  "glucose": 142,
  "systolic_bp": 138,
  "diastolic_bp": 84,
  "cholesterol": 205,
  "bmi": 31.2,
  "comorbidity_score": 4,
  "visit_type": "ED",
  "primary_diagnosis": "I10",
  "hospital_id": "HOSP_12",
  "treatment_group": 1,
  "period": 1
}
```
Example response:
```json
{
  "readmission_probability": 0.0824,
  "predicted_readmission": 1,
  "threshold": 0.35
}
```
Run locally
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Notes
	•	Dataset is synthetic / educational (no real patient data).
	•	Threshold is stored separately to enforce governance between probability estimation and operational decisioning.

Author
Imanuel Annoh

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/<your-username>/<your-repo>)





