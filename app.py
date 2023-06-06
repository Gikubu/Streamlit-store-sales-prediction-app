# Import packages
import streamlit as st

#Utils


# Setup & Config


# App

## Header
st.write("""# My First App
         This is my first app containing a form
         """)

## Form
with st.form("my_form") as form:
    name = st.text_input(label="Enter your name, please...") 
    height = st.number_input("Enter your height in centimeters, please...")
    
    submit = st.form_submit_button()

print(f"[info] Here is my name : {name}")

