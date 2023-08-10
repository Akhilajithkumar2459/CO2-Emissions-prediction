# -*- coding: utf-8 -*-
"""


"""



import pandas as pd
import streamlit as st 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from pickle import dump
from pickle import load

st.title('Co2 emissions prediction')

st.sidebar.header('User Input Parameters')

def user_input_features():
    make = st.slider("Input the vehicle make", min_value=0, max_value=38)
    vehicle_class =st.slider("Input the vehicle class", min_value=0, max_value=15)
    cylinders = st.sidebar.number_input("Input the number of cylinders")
    transmission = st.sidebar.number_input("Input the transmission type")
    fuel_type = st.sidebar.number_input("input the fuel type")
    fuel_consumption_hwy = st.sidebar.number_input("input the fuel consumption in highway")
    fuel_comb_l = st.sidebar.number_input("Input the fuel_comb_l")
    
    data = {
        'make': make,
        'vehicle_class': vehicle_class,
        'cylinders':cylinders,
        'transmission': transmission,
        'fuel_type': fuel_type,
        'fuel_consumption_hwy': fuel_consumption_hwy,
        'fuel_comb_l':fuel_comb_l
        
    }
    
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('model3.pkl', 'rb'))

prediction = loaded_model.predict(df)
st.subheader('Co2 Emissions')
st.write(prediction)

