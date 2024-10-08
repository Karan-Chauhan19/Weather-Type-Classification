'''
Author       : Karan Chauhan
github       : @karan190806
Email        : kc879022@gmail.com
Organization : L.J University
'''

#feature Engineering
#Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import StandardScaler,OneHotEncoder

class Featureengineering :
    def __init__(self,df) :
        self.df = df

    def clean_data(self) :
        #Load data
        data = pd.read_csv('/home/karan-chauhan/WorkStation/Project/Project/Data/weather_classification_data.csv')
        
        #Rename column name
        data.rename(columns={'Wind Speed':'Wind_Speed','Cloud Cover':'Cloud_Cover','Atmospheric Pressure':'Atmospheric_Pressure'
                   ,'UV Index':'UV_Index','Weather Type':'WeatherType'},inplace=True)
        
        #Replace outliers from Temperature and Atmospheric pressure column using capping method
        upper_limit = data['Temperature'].mean() + 3*data['Temperature'].std()
        lower_limit = data['Temperature'].mean() - 3*data['Temperature'].std()
        data['Temperature'] = np.where(data['Temperature']>upper_limit,upper_limit
                             ,np.where(data['Temperature']<lower_limit,lower_limit,data['Temperature']))
        
        data['Atmospheric_Pressure'] = np.where(data['Atmospheric_Pressure']>1100,1085,
                                      np.where(data['Atmospheric_Pressure']<870,885,data['Atmospheric_Pressure']))
        

        return data

    def get_clean_data(self,df) :
        df = Featureengineering().clean_data()
        #Covert Categorical column to numerical column using OneHotEncoder
        ohe = OneHotEncoder()
        df_new = ohe.fit_transform(df[['Cloud_Cover','Season','Location']])

        scaler = StandardScaler()
        df_update = scaler.fit_transform(df.drop(columns='WeatherType'))

        df1 = pd.DataFrame(df_update,columns=['Temperature','Humidity','Wind_Speed','Precipitation (%)','Cloud_Cover',
                                              'Atmospheric_Pressure','UV_Index','Season','Visibility (km)','Location'])
        return df1,df['WeatherType']
        
