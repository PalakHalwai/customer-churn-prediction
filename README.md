# 📊 Customer Churn Prediction & Analytics

A comprehensive end-to-end data science project analyzing customer attrition patterns and building machine learning models to predict churn risk.

---

## 📓 Interactive Project Notebooks

If GitHub fails to render the native `.ipynb` previews on mobile devices, tap the interactive badges below to view the full notebooks with pre-rendered visual charts, code outputs, and classification reports:

### 1. Data Cleaning & Exploratory Data Analysis (EDA)
Perform data auditing, handle missing values, clean data types, and run bivariate EDA.
* [![View on nbviewer](https://img.shields.io/badge/Render-nbviewer-orange?style=for-the-badge&logo=jupyter)](https://nbviewer.org/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/01_eda_and_cleaning.ipynb)
* [![Open In Colab](https://img.shields.io/badge/Open%20in-Colab-blue?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/01_eda_and_cleaning.ipynb)

### 2. Feature Engineering & Modeling
Feature encoding, dataset splitting, training baseline & ensemble models, and evaluating classification metrics.
* [![View on nbviewer](https://img.shields.io/badge/Render-nbviewer-orange?style=for-the-badge&logo=jupyter)](https://nbviewer.org/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/02_feature_engineering_and_modeling.ipynb)
* [![Open In Colab](https://img.shields.io/badge/Open%20in-Colab-blue?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/PalakHalwai/customer-churn-prediction/blob/main/notebooks/02_feature_engineering_and_modeling.ipynb)

---

## 📌 Project Workflow Overview

### 🔍 Phase 1: Data Cleaning & Exploratory Data Analysis
* **Data Type Rectification:** Coerced `TotalCharges` into numeric values and handled missing records gracefully.
* **Class Imbalance Check:** Identified target distribution imbalance between Churn vs. Non-Churn customers.
* **Feature Relationships:** Analyzed customer tenure, contract types (Month-to-month vs. Two-year), internet service types, and payment methods against churn rates.

### ⚙️ Phase 2: Feature Engineering & Predictive Modeling
* **Preprocessing:** Applied One-Hot Encoding / Label Encoding to categorical variables.
* **Model Training:** Built and compared classification models (Logistic Regression, Decision Trees, Random Forest, AdaBoost).
* **Performance Evaluation:** Evaluated models using Precision, Recall, F1-Score, and ROC-AUC metrics.

---

## 🛠️ Repository File Structure

```text
customer-churn-prediction/
│── notebooks/
│   ├── 01_eda_and_cleaning.ipynb               # Raw Notebook 1 (EDA & Cleaning)
│   └── 02_feature_engineering_and_modeling.ipynb # Raw Notebook 2 (Feature Eng & Modeling)
│── reports/
│   ├── 01_eda_and_cleaning.html                # Exported Static HTML Output
│   └── 02_feature_engineering_and_modeling.html # Exported Static HTML Output
└── README.md                                   # Project documentation
