from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("xgb_model.pkl")

class Customer(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def home():
    return {"status": "ok", "message": "Churn API running"}

@app.post("/predict")
def predict(data: Customer):
    features = np.array([[
        data.gender, data.SeniorCitizen, data.Partner, data.Dependents,
        data.tenure, data.PhoneService, data.MultipleLines,
        data.InternetService, data.OnlineSecurity, data.OnlineBackup,
        data.DeviceProtection, data.TechSupport, data.StreamingTV,
        data.StreamingMovies, data.Contract, data.PaperlessBilling,
        data.PaymentMethod, data.MonthlyCharges, data.TotalCharges
    ]])
    pred  = int(model.predict(features)[0])
    proba = float(model.predict_proba(features)[0][1])
    prob  = round(proba * 100, 1)
    risk  = "High" if proba > 0.65 else "Medium" if proba > 0.35 else "Low"
    return {"churn": pred, "probability": prob, "risk": risk}
