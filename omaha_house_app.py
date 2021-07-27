import streamlit as st
import pandas as pd
import numpy as np
import json
import streamlit.components.v1 as components


#title
st.write("""
# Omaha House Price Prediction App
Linear Regression model trained using data collected for single-family homes, condos, 
townhomes and multi-family homes (all existing homes and not foreclosures) listed on 
Realtor.com on July 2021. 
""")
st.write('---')

#import model
PATH = 'omaha_real_estate_model.pickle'
model = pd.read_pickle(PATH)

#import columns
with open("columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        zip_codes = data_columns[4:] #locations start on 5th column

#sidebar
st.sidebar.header('Specify Input Parameters')

def user_input():
    beds = st.sidebar.number_input('Beds', min_value=1, max_value=12, value=2, step=1)
    baths = st.sidebar.number_input('Baths', min_value=1, max_value=10, value=1, step=1)
    sqft = st.sidebar.slider('Squre Feet', min_value=500, max_value=10000, value=2500, step=100)
    sqftlot = st.sidebar.slider('Squre Feet of Lot', min_value=1000, max_value=30000, value=9000, step=100)
    input_zip_code = st.sidebar.selectbox('ZIP Code',(zip_codes))

    #array of zeros length of columns in dataframe    
    x = np.zeros(len(data_columns))

    #assign user input to respective index
    x[0] = beds
    x[1] = baths
    x[2] = sqft
    x[3] = sqftlot
    
    #assign "1" to respective ZIP code index
    zip_index = data_columns.index(input_zip_code)
    x[zip_index] = 1
    return x
    
house_details = user_input()

#prediction
prediction = round(model.predict([house_details])[0],2)
st.write("## Predicted price:", prediction)
st.write('---')

#load map html
with open('map/counts_map.html', 'r') as f:
        page = f.read()
        components.html(page, width=700,height=500)
