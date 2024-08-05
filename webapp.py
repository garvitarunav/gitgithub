import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('Dragon.joblib')

st.image('flight.jpeg')

def store_credentials(id, password, filename = 'credentials.txt'):
    with open(filename, 'a') as file:
        file.write(f"{id}, {password}\n")


st.sidebar.title('Welcome to the Prediction Centre')
id = st.sidebar.text_input('Enter your Email Id')
password = st.sidebar.text_input('Enter Password')

if st.sidebar.button("Submit"):
    store_credentials(id,password)
    st.sidebar.success("You have been registered successfully")


st.title('Testing your Flight Booking Status')
num_passengers = st.number_input('Enter the number of passengers travelling')
purchase_lead = st.number_input('Enter the Purchase Lead - (number of days between travel date and booking date)')
length_of_stay = st.number_input('Fill the Length of the stay')
flight_hour = st.number_input('Enter the Flight Hours - (hour of flight departure)')
flight_duration = st.number_input('Enter the Flight Duration')

col = ['num_passengers','purchase_lead','length_of_stay','flight_hour','flight_duration']

def predict():
    row = np.array([num_passengers,purchase_lead,length_of_stay,flight_hour,flight_duration])
    x = pd.DataFrame([row], columns = col)
    prediction = model.predict(x)[0]

    if prediction == 1:
        st.success('Congratulations, Your booking must be confirmed :beer:')
    else:
        st.warning('Your flight might not be booked. Please take a check on that')

st.button('Predict',on_click=predict)