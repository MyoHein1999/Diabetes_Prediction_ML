import pickle
from typing_extensions import Required
from numpy import require
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

    
# page title
st.title('Diabetes Prediction using ML')
    
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
    Pregnancies = st.text_input('Number of Pregnancies',placeholder="Eg.5")
        
with col2:
    Glucose = st.text_input('Glucose Level',placeholder="Eg.166")
    
with col3:
    BloodPressure = st.text_input('Blood Pressure value',placeholder="Eg.72")
    
with col1:
    SkinThickness = st.text_input('Skin Thickness value',placeholder="Eg.19")

with col2:
        Insulin = st.text_input('Insulin Level',placeholder="Eg.175")
    
with col3:
    BMI = st.text_input('BMI value',placeholder="Eg.25.8")

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',placeholder="Eg.0.587")

with col2:
        Age = st.text_input('Age of the Person',placeholder="Eg.51")
    
    
# code for Prediction
diab_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('Predict'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0] == 1):
      diab_diagnosis = 'The person is diabetic'
    else:
          diab_diagnosis = 'The person is not diabetic'
        
st.success(diab_diagnosis)
















