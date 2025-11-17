# 📘 PeakLoadNet – Energy Demand Prediction

This project predicts **National Energy Demand** using Machine Learning techniques.  
It includes complete data preprocessing, model training, evaluation, and deployment as a real-time API using Flask and Render.

---


## 🚀 Project Overview

This project builds predictive models for electricity demand using two datasets: an hourly dataset (detailed regional hourly demands with timestamps) and a monthly aggregated dataset. The workflow includes data cleaning, datetime handling, feature engineering from regional demand columns, and careful prevention of data leakage during train/test splitting. Multiple models were trained and evaluated (Linear Regression and Random Forest / ExtraTrees experiments). Because of deployment size limits, the lightweight Linear Regression model was exported and deployed as a REST API for real-time inference, while tree-based models were retained locally or compressed for experimentation.

---

## 🧠 Machine Learning Models Used

### ✔ Linear Regression *(Final deployed model)*  
- Lightweight  
- Fast inference  
- Very small file size (<200 KB)  
- Ideal for cloud deployment (Render)

### ❌ Random Forest (Not deployed due to size limits)  
A Random Forest model was also trained, but model file size exceeded Render’s 20MB free limit.  
Therefore, Linear Regression was selected for deployment.

---

## 📊 Key Features

- Performed full dataset cleaning and preprocessing  
- Resolved data leakage issues  
- Converted datetime column and extracted usable features  
- Created train/test split (80/20)  
- Trained and evaluated multiple ML models  
- Generated Actual vs Predicted comparison visualizations  
- Calculated regression metrics (MAE, MSE, RMSE, R² Score)  
- Exported final model using `.joblib` format  
- Built a Flask backend for prediction  
- Deployed API on Render Cloud Platform  

---

## 🌐 Live API URL

 backend is live and publicly accessible at:
 
https://aicte-energy-peakloadnet-neural-network-5juq.onrender.com/
