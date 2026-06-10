# Food-Delivery-Time-Predictor

A supervised machine learning project that predicts food delivery times (in minutes) using regression models trained on delivery order data.

## Problem Statement

Accurate delivery time estimates are critical for customer satisfaction in food delivery platforms. This project builds a regression pipeline that predicts delivery duration based on distance, preparation time, courier experience, weather, traffic, and time of day, vehicle type.

## About the Dataset

Dataset : Food_Delivery_Times.CSV from Kaggle.

Features : 

  * 3 Numerical features - distance, preparation time, courier experience

  * 4 Categorical features - weather, traffic level, time of day, vehicle type

## Project Workflow

Data Loading → EDA → Preprocessing → Model Selection → Hyperparameter Tuning → Final Evaluation → Inference

## Exploratory Data Analysis

* Histogram and count plot for identify data distribution and boxplots for outlier analysis.

* Correlation heatmap to identify numerical feature relationships.

## Data Preprocessing

Built a preprocessing pipelines (imputation for missing values handeling  + scaling + one-hot encoding) using scikit-learn to prevent data leakage.

## Model Selection and Optimization

* LinearRegression model used as the baseline model.

* Perfomed cross validation through 5 models LinearRegression, Lasso, Ridge, RandomForestRegressor, GradientBoostingRegressor.

* According to the cross validation results, Ridge model got the lowest root mean squared error.

* Tuned Ridge Regression with GridSearchCV (best alpha = 10).

* Final Model (Tuned Ridge) Test Performance : RMSE : 10.535, MAE : 6.844, r2 : 0.769.

  




   






