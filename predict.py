import pandas as pd
import joblib

model = joblib.load('Food_delivery_ridge_model.joblib')

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
    print(f'Predicted Delivery Time: {predict_time} minutes')

predict_delivery_time(
    distance_km=5.0,
    preparation_time_min=10,
    courier_experience_yrs=3,
    weather='Clear',
    traffic_level='Medium',
    time_of_day='Evening',
    vehicle_type='Bike'
)