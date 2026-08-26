# 📊 Customer Churn Prediction & Analytics

A comprehensive end-to-end data science project analyzing customer attrition patterns, building machine learning models to predict churn risk, and deploying an interactive web application.

---

## 🚀 Live Interactive Dashboard

Access the deployed Streamlit web application to test real-time customer risk predictions:
👉 **[Launch Live Churn Predictor App]https://customer-churn-prediction-ceuvdnrckyxatndjznvcfg.streamlit.app/
---

## 📓 Interactive Project Notebooks

If GitHub fails to render native `.ipynb` previews on mobile devices, use the interactive badges below to view full notebooks with pre-rendered charts and classification metrics:

### 1. Data Cleaning & Exploratory Data Analysis (EDA)
Perform data auditing, handle missing values, clean data types, and evaluate feature relationships.
* [![View on nbviewer](https://img.shields.io/badge/Render-nbviewer-orange?style=for-the-badge&logo=jupyter)](https://nbviewer.org/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/01_eda_and_cleaning.ipynb)
* [![Open In Colab](https://img.shields.io/badge/Open%20in-Colab-blue?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/01_eda_and_cleaning.ipynb)

### 2. Feature Engineering & Predictive Modeling
Feature encoding, train-test splitting, evaluating baseline and ensemble models, and building risk segments.
* [![View on nbviewer](https://img.shields.io/badge/Render-nbviewer-orange?style=for-the-badge&logo=jupyter)](https://nbviewer.org/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/02_feature_engineering_and_modeling.ipynb)
* [![Open In Colab](https://img.shields.io/badge/Open%20in-Colab-blue?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/02_feature_engineering_and_modeling.ipynb)

---

## 📌 Project Highlights & Key Findings

* **Model Performance:** Logistic Regression achieved **80% accuracy** and an **ROC-AUC score of 0.8425**.
* **Key Drivers:** Contract duration (month-to-month), customer tenure, and monthly charges emerged as top churn indicators.
* **Risk Stratification:** Implemented probability-based scoring to segment accounts into High, Medium, and Low risk tiers for targeted customer retention strategies.

---

## 🛠️ Repository File Structure

```text
customer-churn-prediction/
│── notebooks/
│   ├── 01_eda_and_cleaning.ipynb               # Data Cleaning & Analysis Notebook
│   └── 02_feature_engineering_and_modeling.ipynb # Modeling & Evaluation Notebook
│── reports/
│   ├── 01_eda_and_cleaning.html                # Static HTML Export (EDA)
│   └── 02_feature_engineering_and_modeling.html # Static HTML Export (Modeling)
│── app.py                                      # Streamlit Dashboard Source Code
│── requirements.txt                            # App Dependencies
└── README.md                                   # Project Documentation
