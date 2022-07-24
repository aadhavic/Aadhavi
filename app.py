import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    Nr = st.number_input("Nr",min_value=0.0,max_value=2000000.0)
    Dr = st.number_input("Dr",min_value=0.0,max_value=2000000.0)
    
    data = {'Nr': Nr,
            'Dr': Dr,
           }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())
st.subheader('Division')
if Dr == 0:
    st.write('Invalid input, cannot divide by 0')
else:
    st.write('Nr/Dr')
