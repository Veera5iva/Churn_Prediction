# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:40:35 2023

@author: Ram
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
loaded_model = pickle.load(open('Trained_model1.sav', 'rb'))


  
def map_yes_no_to_binary(value):
    return 1 if value.lower() == 'yes' else 0

# Function to make predictions
def predict_churn(PhoneService_No,InternetService_No, OnlineSecurity_No,StreamingMovies_Yes, Contract_Month_to_month,Contract_One_year,Contract_Two_year,tenure_group_1to12):
    input_data = {
        'PhoneService_No':map_yes_no_to_binary(PhoneService_No),
        'InternetService_No': map_yes_no_to_binary(InternetService_No),
        'OnlineSecurity_No': map_yes_no_to_binary(OnlineSecurity_No),
        'StreamingMovies_Yes':map_yes_no_to_binary(StreamingMovies_Yes),
        'Contract_Month_to_month': map_yes_no_to_binary(Contract_Month_to_month),
        'Contract_One_year': map_yes_no_to_binary(Contract_One_year),
        'Contract_Two_year': map_yes_no_to_binary(Contract_Two_year),
        'tenure_group_1to12': map_yes_no_to_binary(tenure_group_1to12)
        
    }
    input_df = pd.DataFrame([input_data])
    prediction = loaded_model.predict(input_df)[0]
    return prediction

# Streamlit app
def main():
    st.title("Telecom Churn Prediction")

    # User inputs using radio buttons
    PhoneService_No= st.selectbox("PhoneService: None", ["Yes", "No"])
    InternetService_No= st.selectbox("Internet Service: None", ["Yes", "No"])
    OnlineSecurity_No= st.selectbox("OnlineSecurity: None", ["Yes", "No"])
    StreamingMovies_Yes= st.selectbox("StreamingMovies:", ["Yes", "No"])
    Contract_Month_to_month= st.selectbox("Contract Duration: Monthly", ["Yes", "No"])
    Contract_One_year = st.selectbox("Contract Duration: Yearly", ["Yes", "No"])
    Contract_Two_year = st.selectbox("Contract Duration: Two Years", ["Yes", "No"])
    tenure_group_1to12=st.selectbox("tenure group:12 months",["Yes", "No"])

    if st.button("Predict"):
        prediction = predict_churn(PhoneService_No,InternetService_No, OnlineSecurity_No,StreamingMovies_Yes, Contract_Month_to_month,Contract_One_year,Contract_Two_year, tenure_group_1to12)

        if prediction == 0:
            st.success("Customer is not likely to churn")
        else:
            st.error("Customer is likely to churn")


if __name__ == '__main__':
    main()