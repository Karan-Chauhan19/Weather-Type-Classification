'''
author: Karan Chauhan
github: @Karan-Chauhan19
organization: L.J University
'''

import http
import streamlit as st
from train import *
from test import *

# Centering the title using HTML and CSS
class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        st.write()
        st.write()
        
        t = TestDataPreprocessing()
        t.testing()

        st.markdown("[GitHub](https://github.com/Karan-Chauhan19/Weather-Type-Classification.git) | <a href='https://www.linkedin.com/in/karan-chauhan-a511a4293' target='_blank'>Linkedin</a>",unsafe_allow_html=True)
        
        # Add a LinkedIn profile hyperlink using HTML
        st.markdown("", unsafe_allow_html=True)

        # Add copyright notice at the bottom
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line to separate content
        st.markdown(
            "<b><p style='text-align: center; font-size: 12px;'>&copy; 2024 Karan Chauhan. All Rights Reserved.</p>", 
            unsafe_allow_html=True
        )

if  __name__ == "__main__":    
    st.markdown("<h1 style='text-align: center;'><b>Weather Type classification on Environmental Dataset</b></h1>", unsafe_allow_html=True)

    st.markdown("<p ><b> - About this project  :</b></p>",unsafe_allow_html=True)
    st.write(' - This project is a simple web application that uses a machine learning model to classify weather type using environmental data.')

    st.write(' - The model is trained on a dataset of environmental data and can be used to  predict the weather type based on environmental data.')

    run_obj = Main()
    run_obj.run()

else  : 
    print("This is a Streamlit app. Please run it using `streamlit run app.py `")  # noqa: E501