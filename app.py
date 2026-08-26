import streamlit as st
import pandas as pd
import numpy as np

# Title and Layout Setup
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a customer is likely to churn and assign risk tiers.")

# Sidebar Inputs
st.sidebar.header("Customer Profile Input")
tenure = st.sidebar.slider("Tenure (Months)", 1, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", 18.0, 120.0, 65.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.sidebar.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Prediction Logic (Simplified Rule-Based Threshold for Demo)
# In production, load your trained model: joblib.load('churn_model.pkl')
churn_prob = min(max((monthly_charges / 120) * 0.5 + (1 - tenure / 72) * 0.4, 0.05), 0.95)

if contract == "Month-to-month":
    churn_prob = min(churn_prob + 0.15, 0.95)

# Display Results
st.subheader("Predictive Risk Assessment")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Predicted Churn Probability", value=f"{churn_prob:.1%}")

with col2:
    if churn_prob >= 0.6:
        st.error("Risk Tier: HIGH CHURN RISK")
    elif churn_prob >= 0.3:
        st.warning("Risk Tier: MEDIUM CHURN RISK")
    else:
        st.success("Risk Tier: LOW CHURN RISK")

# Recommended Action
st.subheader("Retention Recommendation")
if churn_prob >= 0.6:
    st.write("👉 Offer a long-term contract discount or personalized loyalty perks.")
elif churn_prob >= 0.3:
    st.write("👉 Send targeted engagement emails and customer satisfaction surveys.")
else:
    st.write("👉 Customer is stable. Consider upselling premium services.")