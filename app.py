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
    
    # Page 2: Prediction Page
def prediction_page():
    # Add custom for the background image
    image = Image.open(r"C:\Users\BuzzJengz\Documents\Store.jpg")
    st.image(image)

    # Add a header and description for the prediction page
    st.write("Enter the required information below to make a price prediction.")

    # Input fields
    st.sidebar.title("Input Features")
    city_options = ["Ambato", "Babahoyo", "Cayambe", "Cuenca", "Daule", "El Carmen", "Esmeraldas", "Guaranda",
                    "Guayaquil", "Ibarra", "Latacunga", "Libertad", "Loja", "Machala", "Manta", "Playas", "Puyo",
                    "Quevedo", "Quito", "Riobamba", "Salinas", "Santo Domingo", "unknown"]
    city = st.sidebar.selectbox("City", city_options)
    dcoilwtico = st.sidebar.number_input("Crude Oil Price")
    family_options = ["AUTOMOTIVE", "BABY CARE", "BEAUTY", "BEVERAGES", "BOOKS", "BREAD/BAKERY", "CELEBRATION",
                      "CLEANING", "DAIRY", "DELI", "EGGS", "FROZEN FOODS", "GROCERY I", "GROCERY II", "HARDWARE",
                      "HOME AND KITCHEN I", "HOME AND KITCHEN II", "HOME APPLIANCES", "HOME CARE", "LADIESWEAR",
                      "LAWN AND GARDEN", "LINGERIE", "LIQUOR,WINE,BEER", "MAGAZINES", "MEATS", "PERSONAL CARE",
                      "PET SUPPLIES", "PLAYERS AND ELECTRONICS", "POULTRY", "PREPARED FOODS", "PRODUCE",
                      "SCHOOL AND OFFICE SUPPLIES", "SEAFOOD"]
    family = st.sidebar.selectbox("Family", family_options)
    onpromotion = st.sidebar.selectbox("On Promotion", [True, False])
    sales = st.sidebar.number_input("Sales")
    store_nbr_options = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5
    }
    store_nbr = st.sidebar.selectbox("Store Number", list(store_nbr_options.keys()))
    transactions = st.sidebar.number_input("Transactions", min_value=1, max_value=10)
    #transferred = st.sidebar.selectbox("Transferred", [True, False])
    holiday_type_options = ["Normal", "Event", "Holiday", "", "Transfer"]
    holiday_type = st.sidebar.selectbox("Holiday Type", holiday_type_options)
    year = st.sidebar.number_input("Year", min_value=2000, max_value=2100)
    month = st.sidebar.number_input('Month', min_value=1, max_value=12)
    day = st.sidebar.number_input('Day', min_value=1, max_value=31)
    trans_per_oil = transactions / dcoilwtico
    
    
    # Create a DataFrame with the user input
    input_data = {
        "city": [city],
        "dcoilwtico": [dcoilwtico],
        "family": [family],
        "onpromotion": [onpromotion],
        "sales": [sales],
        "store_nbr": [store_nbr_options[store_nbr]],
        "transactions": [transactions],
        #"transferred": [transferred],
        "holiday_type": [holiday_type],
        "year": [year],
        "month": [month],
        "day": [day],
    }
    input_df = pd.DataFrame(input_data)