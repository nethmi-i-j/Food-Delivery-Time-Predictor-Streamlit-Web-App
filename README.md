# Food-Delivery-Time-Predictor

A supervised machine learning project that predicts food delivery times (in minutes) using regression models trained on delivery order data.

## Problem Statement

Accurate delivery time estimates are critical for customer satisfaction in food delivery platforms. This project builds a regression pipeline that predicts delivery duration based on distance, preparation time, courier experience, weather, traffic, time of day and vehicle type.

## About the Dataset

Dataset : Food_Delivery_Times.CSV from Kaggle.

1000 rows and 9 columns.

Features : 

  * Numerical features - Order_ID, Distance_KM, Preparation_Time_min , Courier_Experience_yrs

  * Categorical features - Weather, Traffic_Level, Time_of_Day, Vehicle_Type

  * Target : Delivery_Time_min

## Project Workflow

Data Loading → EDA → Preprocessing → Model Selection → Hyperparameter Tuning → Final Evaluation → Deploy

## Exploratory Data Analysis

* Histogram and count plot for identify data distribution and boxplots for outlier analysis.

* Correlation heatmap to identify numerical feature relationships.

## Data Preprocessing

Built a preprocessing pipeline (imputation for missing values handeling  + feature scaling + one-hot encoding) using scikit-learn to prevent data leakage.

## Model Selection and Optimization

* LinearRegression model used as the baseline model.

* Perfomed cross validation through 5 models LinearRegression, Lasso, Ridge, RandomForestRegressor, GradientBoostingRegressor.

* According to the cross validation results, Ridge model got the lowest root mean squared error.

* Tuned Ridge Regression with GridSearchCV (best alpha = 10).

* Final Model (Tuned Ridge) Test Performance : RMSE : 10.535, MAE : 6.844, r2 : 0.769.

## Streamlit Web App

An interactive web app built with Streamlit for real-time delivery time predictions.

Features:

* Input order details (distance, weather, traffic, courier experience, etc.)
  
* Instant predicted delivery time
  
* Clean, user-friendly interface
  

  




   






