'''
Author       : Karan Chauhan
github       : @Karan-Chauhan19
Email        : kc879022@gmail.com
Organization : L.J University
'''
import streamlit as st
from test import *
from train import *
import time

# Centering the title using HTML and CSS
st.markdown("<h1 style='text-align: center;'>Weather Type Prediction Based on Environmental Data</h1>", unsafe_allow_html=True)

class main :
    def __init__(self)  -> None :
        pass

    def run(self) :
        
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

            t = TestDataPreprocessing()

            if st.sidebar.button("Predict Weather Type") :
                with st.spinner("Processing..."):  # Show spinner with a message
                    time.sleep(2)
                t.testing(user_input)
            else :
                pass

m = main()
m.run()
        




