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

# Define the input and output interfaces for the Streamlit app
st.title("Item Price Prediction App")

# Page 1: Welcome Page
def welcome_page():
    # Add a header and description
    st.header("Welcome!")
    st.write("This app predicts the price of items based on user input.")

    # Add an image
    image = Image.open(r":\"C:\Users\BuzzJengz\Documents\Store.jpg"")
    st.image(image)