import streamlit as st
import requests
import pandas as pd

# Define the URL for the Flask API
url = "http://127.0.0.1:5000/predict"

# Define the form fields for user input
st.header("California Housing Price Prediction")
med_inc = st.number_input("Median Income")
house_age = st.number_input("House Age")
ave_rooms = st.number_input("Average Rooms")
ave_bedrms = st.number_input("Average Bedrooms")
population = st.number_input("Population")
ave_occup = st.number_input("Average Occupancy")
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")

# Define the payload to be sent to the Flask API
data = {
    "MedInc": med_inc,
    "HouseAge": house_age,
    "AveRooms": ave_rooms,
    "AveBedrms": ave_bedrms,
    "Population": population,
    "AveOccup": ave_occup,
    "Latitude": latitude,
    "Longitude": longitude
}

# Make a POST request to the Flask API with the user input data
response = requests.get(url, json=data)

# If the response is successful (status code 200), display the predicted values
if response.status_code == 200:
    predicted_values = pd.read_html(response.text)[0]
    st.table(predicted_values)
else:
    st.write("Error predicting values. Please try again later.")
