# ChurnSense — Customer Churn Prediction

&lt;p align="center"&gt;
  &lt;img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python"&gt;
  &lt;img src="https://img.shields.io/badge/XGBoost-3.2+-orange.svg" alt="XGBoost"&gt;
  &lt;img src="https://img.shields.io/badge/FastAPI-0.100+-green.svg" alt="FastAPI"&gt;
  &lt;img src="https://img.shields.io/badge/License-MIT-purple.svg" alt="License"&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;b&gt;ML-powered customer churn predictor&lt;/b&gt; built with XGBoost, FastAPI, and a modern dark-themed web UI.
  &lt;br&gt;
  &lt;a href="#-live-demo"&gt;Live Demo&lt;/a&gt; • &lt;a href="#-features"&gt;Features&lt;/a&gt; • &lt;a href="#-tech-stack"&gt;Tech Stack&lt;/a&gt; • &lt;a href="#-getting-started"&gt;Getting Started&lt;/a&gt;
&lt;/p&gt;

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
