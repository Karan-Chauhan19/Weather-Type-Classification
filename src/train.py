'''
Author       : Karan Chauhan
github       : @Karan-Chauhan19
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
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import streamlit as st




class ModelTrain :
    def __init__(self) :
        pass

    

    def train_model(self) :

        data = Featureengineering()
        df,preprocessor = data.get_clean_data()
        X = df.drop(columns=['WeatherType','Location'])
        y = df.iloc[:,-1]
        # X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

        model_pipeline = Pipeline(steps=[
            ('preprocessor',preprocessor)
        ])
        model_pipeline.fit(X,y)
        transform_data = model_pipeline.named_steps['preprocessor'].transform(X)
        options = ['Random Forest Classifier','Decision Tree','Logistic Regression','SVM']
        selected_option = st.sidebar.selectbox("Select Algorithm ",options)

        Selected_Algorithm = object

        if selected_option == 'Random Forest Classifier' :
            Selected_Algorithm = RandomForestClassifier(max_features=0.2, max_samples=0.5, n_estimators=120)
            Selected_Algorithm.fit(transform_data,y)
        elif selected_option == 'Decision Tree' :
            Selected_Algorithm = DecisionTreeClassifier(max_depth=4,max_leaf_nodes=5,min_samples_split=50)
            Selected_Algorithm.fit(transform_data,y)
        elif selected_option == 'Logistic Regression' :
            Selected_Algorithm = LogisticRegression()
            Selected_Algorithm.fit(transform_data,y)
        else :
            Selected_Algorithm = SVC()
            Selected_Algorithm.fit(transform_data,y)

        return Selected_Algorithm,model_pipeline