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
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder

class Featureengineering :

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

    def get_clean_data(self) :
        df = Featureengineering().clean_data()
        #Covert Categorical column to numerical column using OneHotEncoder
        ohe = OneHotEncoder()
        df_1 = ohe.fit_transform(df[['Cloud_Cover','Season','Location']]).toarray()
        df_new = pd.concat([df.drop(columns=['Cloud_Cover','Season','Location','WeatherType'], axis=1), pd.DataFrame(df_1, columns=ohe.get_feature_names_out(['Cloud_Cover','Season','Location']))], axis=1)

        scaler = StandardScaler()
        df_update = scaler.fit_transform(df_new)
        scaled_df = pd.DataFrame(df_update, columns=df_new.columns)

        #Use labelencoder for output column
        le = LabelEncoder()
        y = le.fit_transform(df['WeatherType'])
        labeled = pd.DataFrame(y,columns=['WeatherType'])
        return pd.concat([scaled_df,labeled],axis=1)
        
