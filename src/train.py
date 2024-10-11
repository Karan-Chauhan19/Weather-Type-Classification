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
from sklearn.pipeline import Pipeline


data = Featureengineering()
df,preprocessor = data.get_clean_data()
X = df.drop(columns=['WeatherType'])
y = df.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model_pipeline = Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('classifier',RandomForestClassifier(n_estimators=20,max_samples=0.5,max_features=0.6,max_depth=8))
])

model_pipeline.fit(X_train,y_train)
