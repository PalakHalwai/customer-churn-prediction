# customer-churn-prediction
# 📊 End-to-End Customer Churn Prediction

Predicting customer churn using machine learning to enable proactive retention actions and minimize revenue loss.

## 📌 Project Overview
Customer churn is a critical metric for subscription-based businesses. This end-to-end data science project analyzes customer behavior, subscription contracts, and payment history to predict churn probability and categorize customers into actionable risk tiers.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest)
* **Version Control:** Git, GitHub

## 📂 Repository Structure
## 📈 Key Insights & Model Results
* **Overall Churn Rate:** ~26.5%
* **Key Drivers of Churn:** Month-to-month contracts, electronic check payments, and short tenure (< 12 months).
* **Model Performance:**
  * **Logistic Regression:** ROC-AUC = 0.8425 | Accuracy = 80%
  * **Random Forest:** ROC-AUC = 0.8220 | Accuracy = 79%

## 🎯 Risk Segmentation Strategy
* **Low Risk (0 - 30%):** Standard automated engagement.
* **Medium Risk (30 - 70%):** Proactive monitoring and targeted retention campaigns.
* **High Risk (70 - 100%):** Immediate human outreach, custom discounts, and long-term contract conversion offers.
