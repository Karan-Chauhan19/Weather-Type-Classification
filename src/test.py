import pandas as pd
import numpy as np
from train import *
from sklearn.metrics import classification_report

class TestDataPreprocessing :
    def __init__(self) :
        pass
    def testing(self,user_input) :
        user_df = pd.DataFrame(user_input)
        user_input_transform = model_pipeline.named_steps['preprocessor'].transform(user_df)
        user_prediction = model_pipeline.named_steps['classifier'].predict(user_input_transform)

        print("Current weather as per your input is",''.join(user_prediction))

test = TestDataPreprocessing()
test.testing({'Temperature':[33], 'Humidity':[45], 'Wind_Speed':[8], 'Precipitation (%)':[90],
       'Cloud_Cover':['cloudy'], 'Atmospheric_Pressure':[1010], 'UV_Index':[5], 'Season':['Autumn'],
       'Visibility (km)':[10], 'Location':['inland']})