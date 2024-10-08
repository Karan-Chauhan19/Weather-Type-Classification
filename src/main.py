'''
Author       : Karan Chauhan
github       : @karan190806
Email        : kc879022@gmail.com
Organization : L.J University
'''

import pandas as pd
import numpy as np
from features.build_features import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score

data = Featureengineering()
df = data.get_clean_data()
X = df.drop(columns=['WeatherType'])
y = df.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

y_train_frame = pd.DataFrame(y_train,columns=['WeatherType'])
y_test_frame = pd.DataFrame(y_test,columns=['WeatherType'])
rf = RandomForestClassifier()
rf.fit(X_train,y_train_frame)
y_pred = rf.predict(X_test)
print(rf.predict(np.array([[23.0,38,4.5,6.0,1021.19,9,10.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0]])))
print("Accuracy Score ",accuracy_score(y_test_frame,y_pred))
print("Report ",classification_report(y_test_frame,y_pred))