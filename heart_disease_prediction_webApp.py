#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:43:35 2024

@author: drish
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('/home/drish/Heart Disease Prediction/trained_model.sav','rb'))


# creating a function for prediction

def heart_prediction(input_data):
    

# change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    


def heart_prediction(input_data):
    if prediction[0] == 0:
        return 'The Person does not have a Heart Disease'
    else:
        return 'The Person has a Heart Disease'



def main():
    
    #title for webpage
    st.title('Heart Disease Prediction Web App')
    
    #getting input from user
    age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal

age = st.text_input('Age')
sex = st.text_input('Gender')
cp = st.text_input('Chest Pain')
trestbps = st.text_input('Trestbps')
chol = st.text_input('Cholesterol')
fbs = st.text_input('Fasing Blood sugar levels')
restecg = st.text_input('Rest ECG')
thalach = st.text_input('Maximum heart rate')
exang = st.text_input('Exercise Induced Angina')
oldpeak = st.text_input('Oldpeak')
slope = st.text_input('Slope')
ca = st.text_input('Coronary artery disease')
thal = st.text_input('Thalium stress result')

# code for prediction
diagnosis =  ''

#creating a button for prediction

if st.button('Heart Disease Test Result'):
    diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])


st.success(diagnosis)




if __name__ == '__main__':
    main()










