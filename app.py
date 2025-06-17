import streamlit as st
import pandas as pd
import joblib
import os

# Load base models
model_no2 = joblib.load("models/model_no2.pkl")
model_temp = joblib.load("models/model_temp.pkl")

# Load optional models
def load_optional_model(name):
    path = f"models/{name}"
    return joblib.load(path) if os.path.exists(path) else None

model_pm25 = load_optional_model("model_pm25.pkl")
model_pm10 = load_optional_model("model_pm10.pkl")
model_co = load_optional_model("model_co.pkl")

# Set Streamlit page settings
st.set_page_config(page_title="EnviroCast", layout="wide")
st.title("🌤️ EnviroCast: Weather & Air Quality Dashboard - Bangalore")

# Upload section
uploaded = st.file_uploader("📂 Upload your dataset (CSV)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("📊 Data Preview", df.head())
    st.write("✅ Columns in uploaded file:", df.columns.tolist())

    # Plotting
    st.subheader("📈 Visualize Trends")
    col = st.selectbox("Choose a parameter to plot", df.columns)
    st.line_chart(df[col])
else:
    st.info("⬆️ Upload a CSV file to get started.")

# -----------------------
# 🔮 Prediction Section
# -----------------------
st.subheader("🧠 Make Predictions")

# Inputs
temp = st.slider("Temperature (°C)", 10, 45, 25)
precip = st.slider("Precipitation (mm)", 0.0, 5.0, 0.1)
tmax = st.slider("Max Temperature (°C)", 20, 50, 35)
tmin = st.slider("Min Temperature (°C)", 5, 30, 20)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)
hour = st.slider("Hour", 0, 23, 12)

# Prepare inputs
input_features = {
    "temperature": temp,
    "precip": precip,
    "tmax": tmax,
    "tmin": tmin,
    "day": day,
    "month": month,
    "hour": hour
}

input_no2_df = pd.DataFrame([input_features])
input_temp_df = pd.DataFrame([{
    "temperature": temp,
    "precip": precip,
    "tmax": tmax,
    "tmin": tmin,
    "day": day,
    "month": month
}])

# Base predictions
pred_no2 = model_no2.predict(input_no2_df)
pred_temp = model_temp.predict(input_temp_df)

st.success(f"🔬 **Predicted Nitrogen Dioxide (NO₂)**: {pred_no2[0]:.2f} µg/m³")
st.success(f"🌡️ **Forecasted Temperature (next hour)**: {pred_temp[0]:.2f} °C")

# Optional pollutants
if model_pm25:
    pred_pm25 = model_pm25.predict(input_no2_df)
    st.success(f"🧪 **Predicted Particulate Matter 2.5 (PM2.5)**: {pred_pm25[0]:.2f} µg/m³")

if model_pm10:
    pred_pm10 = model_pm10.predict(input_no2_df)
    st.success(f"🧪 **Predicted Particulate Matter 10 (PM10)**: {pred_pm10[0]:.2f} µg/m³")

if model_co:
    pred_co = model_co.predict(input_no2_df)
    st.success(f"🧪 **Predicted Carbon Monoxide (CO)**: {pred_co[0]:.2f} ppm")
