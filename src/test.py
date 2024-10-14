import pandas as pd
import numpy as np
from train import *
import streamlit as st

class TestDataPreprocessing :
    def __init__(self) :
        pass
    def testing(self,user_input) :
        user_df = pd.DataFrame([user_input])
        user_input_transform = model_pipeline.named_steps['preprocessor'].transform(user_df)
        user_prediction = model_pipeline.named_steps['classifier'].predict(user_input_transform)

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