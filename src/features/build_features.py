'''
author: Karan Chauhan
github: @Karan-Chauhan19
organization: L.J University
'''

import numpy as np
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder

class Featureengineering :

    def clean_data(self) :
        #Load data
        data = pd.read_csv('/home/karan-chauhan/WorkStation/Project/Project/Data/weather_classification_data.csv')
        
        #Rename column name
        data.rename(columns={'Wind Speed':'Wind_Speed','Cloud Cover':'Cloud_Cover','Atmospheric Pressure':'Atmospheric_Pressure'
                   ,'UV Index':'UV_Index','Weather Type':'WeatherType'},inplace=True)
        
        #Replace outliers in Temperature and Atmospheric pressure column using capping method
        upper_limit = data['Temperature'].mean() + 3*data['Temperature'].std()
        lower_limit = data['Temperature'].mean() - 3*data['Temperature'].std()
        data['Temperature'] = np.where(data['Temperature']>upper_limit,upper_limit
                             ,np.where(data['Temperature']<lower_limit,lower_limit,data['Temperature']))
        
        data['Atmospheric_Pressure'] = np.where(data['Atmospheric_Pressure']>1100,1085,
                                      np.where(data['Atmospheric_Pressure']<870,885,data['Atmospheric_Pressure']))
        

        return data

    def get_clean_data(self) :
        df = Featureengineering().clean_data()
        categorical_column = ['Cloud_Cover','Season']
        numerical_column = ['Temperature', 'Humidity', 'Wind_Speed', 'Precipitation (%)','Atmospheric_Pressure', 'UV_Index','Visibility (km)']
        #For feature engineering we use columntransformer
        preprocessor = ColumnTransformer(transformers=[
            ('trf1',OneHotEncoder(drop='first'),categorical_column),
            ('trf2',StandardScaler(),numerical_column)
        ])

        return df,preprocessor
        
