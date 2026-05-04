
readme_content = """# ChurnSense — Customer Churn Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/XGBoost-3.2+-orange.svg" alt="XGBoost">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/License-MIT-purple.svg" alt="License">
</p>

<p align="center">
  <b>ML-powered customer churn predictor</b> built with XGBoost, FastAPI, and a modern dark-themed web UI.
  <br>
  <a href="#-live-demo">Live Demo</a> • <a href="#-features">Features</a> • <a href="#-tech-stack">Tech Stack</a> • <a href="#-getting-started">Getting Started</a>
</p>

---

## Overview

**ChurnSense** predicts whether a telecom customer is likely to churn based on 19 behavioral and demographic features. The project includes a complete ML pipeline — from data preprocessing and model training to a REST API and an interactive frontend.

- **Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (7,032 customers)
- **Algorithm:** XGBoost Classifier
- **Model Accuracy:** ~81% (10-fold CV mean: 80%, max: 82%)
- **Precision:** 81% (weighted)

---

## Features

- **Real-time Predictions** — Enter customer details via a sleek web UI and get instant churn probability
- **Risk Classification** — Results categorized as Low, Medium, or High risk with actionable retention messages
- **19 Input Features** — Covers profile, services, billing, and contract data
- **Responsive Design** — Works seamlessly on desktop and mobile
- **REST API** — FastAPI backend with `/predict` endpoint for easy integration

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **ML / Data** | Python, Pandas, NumPy, Scikit-learn, XGBoost |
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Deployment** | Render (API), Vercel (Frontend) |
| **Model Format** | Pickle (`.pkl`) |

---

## Project Structure

```
churnsense/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── xgb_model.pkl        # Trained XGBoost model
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # ChurnSense UI
├── notebook/
│   └── churn_model.ipynb    # EDA + training pipeline
└── README.md
```

---

## Model Details

### Preprocessing Pipeline
- **Categorical Encoding:** Manual label encoding for all categorical variables
  - `gender`: Female=0, Male=1
  - `Contract`: Two year=0, One year=1, Month-to-month=2
  - `InternetService`: No=0, DSL=1, Fiber optic=2
  - `PaymentMethod`: Auto (Bank/Card)=0, Mailed check=1, Electronic check=2
  - Binary features (Yes/No) mapped to 1/0
- **Data Cleaning:** Converted `TotalCharges` to numeric, dropped 11 missing rows, removed duplicates
- **Train/Test Split:** 80/20 with `random_state=42`

### XGBoost Configuration
```python
XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    eval_metric='logloss',
    random_state=42
)
```

### Performance
| Metric | Score |
|--------|-------|
| Accuracy | 81% |
| Precision (weighted) | 81% |
| CV Mean Accuracy | 80% |
| CV Max Accuracy | 82% |

**Confusion Matrix:**
```
[[949  133]
 [135  185]]
```

---

## API Reference

### `POST /predict`

Predict churn probability for a single customer.

**Request Body:**
```json
{
  "gender": 0,
  "SeniorCitizen": 0,
  "Partner": 0,
  "Dependents": 0,
  "tenure": 12,
  "PhoneService": 1,
  "MultipleLines": 0,
  "InternetService": 2,
  "OnlineSecurity": 0,
  "OnlineBackup": 0,
  "DeviceProtection": 0,
  "TechSupport": 0,
  "StreamingTV": 0,
  "StreamingMovies": 0,
  "Contract": 0,
  "PaperlessBilling": 0,
  "PaymentMethod": 2,
  "MonthlyCharges": 65.00,
  "TotalCharges": 780.00
}
```

**Response:**
```json
{
  "churn": 1,
  "probability": 78,
  "risk": "High"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `churn` | int | 0 = Not likely, 1 = Likely to churn |
| `probability` | int | Churn probability percentage (0-100) |
| `risk` | string | Low / Medium / High |

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/churnsense.git
cd churnsense
```

### 2. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`

### 3. Launch the frontend
Open `frontend/index.html` directly in your browser, or serve it with:
```bash
npx serve frontend
```

> **Note:** Update the `API_URL` in `index.html` to point to your local backend (`http://localhost:8000`) during development.

---

## Deployment

### Backend (Render)
1. Push code to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Update `API_URL` in the frontend to your Render URL

### Frontend (Vercel)
1. Import your GitHub repo on [Vercel](https://vercel.com)
2. Set framework preset to **Other**
3. Set output directory to `frontend`
4. Deploy

---

## Screenshots

*(Add screenshots of your UI here)*

<p align="center">
  <img src="assets/screenshot.png" alt="ChurnSense UI" width="800">
</p>

---

## Future Improvements

- [ ] Add SHAP/LIME explain
