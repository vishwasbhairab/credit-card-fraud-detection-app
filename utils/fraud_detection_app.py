
import pandas as pd
import numpy as np
import joblib
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Load trained model
model = joblib.load('model/fraud_detection_model.pkl')

# Load scaler and fit on known data
scaler = StandardScaler()

def preprocess_input(data):
    """ Preprocess user input """
    data[['Amount', 'Time']] = scaler.fit_transform(data[['Amount', 'Time']])
    return data

# Streamlit UI
st.title("Credit Card Fraud Detection")
st.write("Enter transaction details to check if it's fraudulent or not.")

# User input fields
amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
time = st.number_input("Time since first transaction (seconds)", min_value=0.0, format="%.2f")
v_features = [st.number_input(f"V{i}", value=0.0, format="%.4f") for i in range(1, 29)]

# Convert to DataFrame
input_data = pd.DataFrame([[time, *v_features, amount]], columns=['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount'])

if st.button("Predict Fraud"):    
    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)[0]
    
    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")
    
