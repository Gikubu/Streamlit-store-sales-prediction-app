# Import packages
import streamlit as st
import pandas as pd
import joblib
#from sklearn.preprocessing import OrdinalEncoder
from category_encoders.binary import BinaryEncoder
from PIL import Image




#Utils


# Setup & Config
st.set_page_config(page_title="SALES PREDICTION APP")

# Load the saved model
model = joblib.load(r""C:\Users\BuzzJengz\Documents\GitHub\Streamlit - app 1\assets\ml\sales_predict.joblib"")

# App

# Add the page title and configuration
st.write("""# My First App
         This is my first app containing a form
         """)

## Form
with st.form("my_form") as form:
    name = st.text_input(label="Enter your name, please...") 
    height = st.number_input("Enter your height in centimeters, please...")
    
    submit = st.form_submit_button()

print(f"[info] Here is my name : {name}")

