'''
author: Karan Chauhan
github: @Karan-Chauhan19
organization: L.J University
'''

import numpy as np
from train import *
import pandas as pd
import streamlit as st

class TestDataPreprocessing :
    def __init__(self) :
        pass

    def testing(self) :
        st.sidebar.title("Select Parameter ")
        mt = ModelTrain()
        selected_algorithm,model_pipeline =  mt.train_model()

        # Create a single column on the left side
        left_col, _ = st.columns([1, 3])  # 1:3 ratio for left column vs right empty space
        with left_col:
            # User inputs for numerical data
            temperature = st.sidebar.number_input("Temperature (°C):", min_value=-50.0, max_value=60.0, value=25.0)
            humidity = st.sidebar.number_input("Humidity (%):", min_value=0, max_value=100, value=50)
            wind_speed = st.sidebar.number_input("Wind Speed (km/h):", min_value=0.0, max_value=200.0, value=10.0)
            precipitation = st.sidebar.number_input("Precipitation (%):", min_value=0, max_value=100, value=20)
            atmospheric_pressure = st.sidebar.number_input("Atmospheric Pressure (hPa):", min_value=800.0, max_value=1100.0, value=1013.0)
            uv_index = st.sidebar.number_input("UV Index:", min_value=0, max_value=11, value=5)
            visibility = st.sidebar.number_input("Visibility (km):", min_value=0.0, max_value=100.0, value=10.0)

            # Dropdown menus with a placeholder to ensure a valid selection
            cloud_cover = st.sidebar.selectbox("Cloud Cover:", ['partly cloudy', 'clear', 'overcast', 'cloudy'])
            season = st.sidebar.selectbox("Season:", ['Winter', 'Spring', 'Summer', 'Autumn'])

            st.markdown("""
            <style>
            /* Change font size for all labels */
            .stSelectbox {
                font-size: 50px !important;
            }
            </style>
            """, unsafe_allow_html=True)

            user_input = {'Temperature': temperature, 'Humidity':humidity, 'Wind_Speed':wind_speed, 'Precipitation (%)':precipitation,
            'Cloud_Cover':cloud_cover, 'Atmospheric_Pressure':atmospheric_pressure, 'UV_Index':uv_index, 'Season':season,
           'Visibility (km)':visibility}
        
        if st.sidebar.button("Submit") :

            user_df = pd.DataFrame([user_input])
            user_input_transform = model_pipeline.transform(user_df)
            user_prediction = selected_algorithm.predict(user_input_transform)

            if user_prediction == ''.join(['Sunny']) :
                output_message = "The weather is likely to be Sunny ☀️"
                st.image("/home/karan-chauhan/Downloads/sun.png",width=400, use_column_width=False)
            elif user_prediction == ''.join(['Rainy']):
                output_message = "The weather is likely to be Rainy 🌧️"
                st.image("/home/karan-chauhan/Downloads/storm.png",width=400, use_column_width=False)
            elif user_prediction == ''.join(['Cloudy']) :
                output_message = "The weather is likely to be Cloudy ☁️"
                st.image("/home/karan-chauhan/Downloads/cloudy.png",width=400, use_column_width=False)
            elif user_prediction == ''.join(['Snowy']) :
                output_message = "The weather is likely to be Snowy ❄️"
                st.image("/home/karan-chauhan/Downloads/snow.png",width=400, use_column_width=False)
            else :
                pass

            # Display the output message with bold and increased font size
            st.markdown(f"<h2>{output_message}</h2>", unsafe_allow_html=True)