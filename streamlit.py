import pandas as pd
import streamlit as st
import joblib

# Give title for the Dashboard
st.title("CROP PREDECTION ANALYSIS")

# Give number input box to enter the values 
Domain=st.number_input("Domain",min_value=0)
Area=st.number_input("Area",min_value=0)
Item=st.number_input("Item",min_value=0)
Unit=st.number_input("Unit",min_value=0)
Year=st.number_input("Year",min_value=2019,max_value=2025,step=1)
Area_harvested=st.number_input("Area harvested",min_value=0.0)
Yield=st.number_input("Yield",min_value=0.0)

# load the joblib file
try:
    jb = joblib.load(r"C:\Users\Admin\Desktop\crop production ML project\model.pkl")

except:
    st.error("Error Loading Model")

#  Give Button to see the prection
if st.button("Predict Production"):

# Create the dataframe 
    input_value=pd.DataFrame([[
        Domain,
        Area,
        Item,
        Unit,
        Year,
        Area_harvested,
        Yield

# Entering all the columns in the dataset
    ]], columns=[
        'Domain',
        'Area',	
        'Item',
        'Unit',	
        'Year',	
        'Area harvested',	
        'Yield'

    ])
 

# Predict the joblib data and give the dataframe in the prediction
    production = jb.predict(input_value)[0]

    st.write(f"Predicted Production: {production.round(2)} units")

 # Display Reference Table   
st.header("REFERENCE TABLE")
df=pd.read_csv('agriculture.csv')

 # Droping the Production Column
st.dataframe(df.drop(columns=['Production'],errors='ignore'))
st.dataframe(df)



    
 