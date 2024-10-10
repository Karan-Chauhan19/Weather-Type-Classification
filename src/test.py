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

        print(classification_report(y_test,user_prediction))

test = TestDataPreprocessing()
test.testing({'Temperature':[38], 'Humidity':[83], 'Wind_Speed':[7], 'Precipitation (%)':[82],
       'Cloud_Cover':['clear'], 'Atmospheric_Pressure':[1026.5], 'UV_Index':[7], 'Season':['Spring'],
       'Visibility (km)':[1], 'Location':['coastal']})