import streamlit as st
import requests
from datetime import datetime
'''
# TaxiFareModel front
'''


#url = 'https://taxifare.lewagon.ai/predict'
url = 'https://taxifare-280745122697.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


data = {
        "pickup_latitude": 40.747,
        "pickup_longitude": -72.989,
        "dropoff_latitude": 40.802,
        "dropoff_longitude": -73.956,
        "passenger_count": 6,
        "pickup_datetime": "2024-02-02 10:00:00"
      }


with st.form("taxi_form"):
    # Input fields for pickup and dropoff latitude/longitude
    pickup_latitude = st.number_input("Pickup Latitude", value=40.747)
    pickup_longitude = st.number_input("Pickup Longitude", value=-72.989)
    dropoff_latitude = st.number_input("Dropoff Latitude", value=40.802)
    dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.956)

    # Input field for passenger count
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=6)

    # Input field for pickup datetime
    pickup_datetime = st.text_input("Pickup Datetime", value="2024-02-02 10:00:00")

    # Submit button for the form
    submitted = st.form_submit_button("Submit")

    # Handle form submission
    if submitted:
        try:
            # Validate and parse the pickup datetime
            parsed_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

            # Create a dictionary with the user input
            ride_parameters = {
                "pickup_latitude": pickup_latitude,
                "pickup_longitude": pickup_longitude,
                "dropoff_latitude": dropoff_latitude,
                "dropoff_longitude": dropoff_longitude,
                "passenger_count": passenger_count,
                "pickup_datetime": parsed_datetime.strftime("%Y-%m-%d %H:%M:%S")
            }

            # Display the dictionary
            st.write("Submitted Ride Parameters:")
            st.json(ride_parameters)

            try:
                # Make the API request
                response = requests.get(url, params=ride_parameters)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Display the JSON response from the API
                    st.json(response.json())
                else:
                    st.error(f"Error: {response.status_code} - {response.reason}")

            except Exception as e:
                st.error(f"An error occurred: {e}")

        except ValueError:
            st.error("Invalid datetime format. Please use YYYY-MM-DD HH:MM:SS format.")

#if st.button("Make API Request"):
