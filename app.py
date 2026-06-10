import streamlit as st
import pandas as pd
import joblib

# Load Model 
model = joblib.load('Food_delivery_ridge_model.joblib')


# function for prediction 
def predict_delivery_time(
    distance_km,
    preparation_time_min,
    courier_experience_yrs,
    weather,
    traffic_level,
    time_of_day,
    vehicle_type
):
    input_data = pd.DataFrame([{
        'Distance_km': distance_km,
        'Preparation_Time_min': preparation_time_min,
        'Courier_Experience_yrs': courier_experience_yrs,
        'Weather': weather,
        'Traffic_Level': traffic_level,
        'Time_of_Day': time_of_day,
        'Vehicle_Type': vehicle_type
    }])

    prediction = model.predict(input_data)
    predict_time =  round(prediction[0], 2)
    return predict_time
    
# streamlit ui

def main():

    st.set_page_config(
        page_title='Food Delivery Time Predictor',
        layout='centered'
    
    )
    
    st.title('Food Delivery Time Predictor')
    st.image('fd_.jpg', width=300)
    

    # input fields

    distance_km = st.number_input(

        'Distance (km)', min_value=0.1, max_value=50.0, value=5.0, step=0.1
    )
    preparation_time_min = st.number_input(
        'Preparation Time (min)', min_value=1, max_value=60, value=5, step=1
    )
    courier_experience_yrs = st.number_input(
        'Courier Experience (yrs)', min_value=0, max_value=20, value=3, step=1
    )
    weather = st.selectbox(
        'Weather', ['Clear', 'Rainy', 'Foggy', 'Windy', 'Stormy']
    )
    traffic_level = st.selectbox(
        'Traffic Level', ['Low', 'Medium', 'High']
    )
    time_of_day = st.selectbox(
        'Time of Day', ['Morning', 'Afternoon', 'Evening', 'Night']
    )
    vehicle_type = st.selectbox(
        'Vehicle Type', ['Bike', 'Scooter', 'Car']
    )


    predicted_time = ''

    if st.button('Predict Delivery Time'):
        predicted_time = predict_delivery_time(
            distance_km,
            preparation_time_min,
            courier_experience_yrs,
            weather,
            traffic_level,
            time_of_day,
            vehicle_type
        )

    st.success(f'Estimated Delivery Time in minutes : {predicted_time}')
    

if __name__ == '__main__':
    main()        















    



    