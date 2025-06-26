# 🌤️ EnviroCast: Weather & Air Quality Dashboard for Bangalore

**EnviroCast** is a user-friendly **Streamlit dashboard** that allows users to **visualize**, **analyze**, and **predict** both **air quality** and **weather trends** in Bangalore.  
It merges pollution and weather datasets, applies machine learning models, and generates interactive charts and forecasts — now with **custom NO₂ heatmap generation** using grid-level uploaded CSVs!

---

## 🛠️ Tech Stack

- 🐍 Python 3.10+
- 📊 Pandas, Matplotlib
- 🤖 scikit-learn, XGBoost, Joblib
- 🌐 Streamlit for web dashboard
- 🧹 Custom Python scripts for preprocessing & merging

---

## 🚀 Features

### 📂 CSV Upload
- Upload your **cleaned or preprocessed dataset** (`.csv`) for trend visualization.
- Upload a separate **NO₂ heatmap grid-level dataset** (e.g., `blr_2022_inference.csv`) for geospatial rendering.

### 📈 Trend Visualization
- Select any column (e.g., NO₂, PM2.5, Temperature) to generate a **time-series chart**.
- Easily visualize trends in **pollution and climate over time**.

### 🧠 Predictive Modeling
- Use sliders to input:
  - 🌡️ Temperature, Max Temp, Min Temp, Precipitation
  - 📅 Day, Month, Hour
- Predict:
  - 🔬 **Nitrogen Dioxide (NO₂)** in µg/m³  
  - 🌡️ **Temperature (next hour)** in °C  
  - 🧪 **PM2.5** – Particulate Matter < 2.5µm  
  - 🧪 **PM10** – Particulate Matter < 10µm  
  - 🧪 **Carbon Monoxide (CO)** in ppm

### 🗺️ NO₂ Heatmap
- Upload a **grid-level CSV file** (`blr_2022_inference.csv` or your custom file) containing lat/lon and weather columns.
- Choose between **Folium** or **Plotly** map rendering.
- Adjust driving features (temperature, precip, tmax, etc.).
- Get an **interactive NO₂ prediction map** across Bangalore!

---

## 🧩 How to Use

### 1. 🔧 Install Requirements

Ensure Python 3.10+ is installed. Then:

```bash
pip install -r requirements.txt
````

---

### 2. ▶️ Start the App

```bash
streamlit run app.py
```

Access the dashboard via browser.

---

### 3. 📊 Upload Your Dataset

If you have two datasets like:

* `air_quality.csv`
* `weather.csv`

Merge them first:

```bash
python merge_datasets.py
```

Then clean the merged file:

```bash
python preprocess.py
```

This creates `preprocessed_data.csv` for trend analysis & predictions.

---

### 4. 🌍 Upload for Heatmap (NEW 🔥)

You can now upload a **grid-level dataset** (e.g., `blr_2022_inference.csv`) with latitude, longitude, temperature, etc., to render a **city-wide NO₂ heatmap**.

Example structure:

```csv
latitude,longitude,temperature,precip,tmax,tmin,day,month,hour
12.97,77.59,27.0,0.1,32,22,15,6,10
...
```

---

## 🔁 Model Training (Optional)

Train models from your processed dataset:

```bash
python train_models.py
```

This generates `.pkl` model files in `/models`.

---

## 📦 Requirements

`requirements.txt` includes:

```txt
streamlit
pandas
scikit-learn
xgboost
matplotlib
joblib
plotly
folium
branca
```

Install via:

```bash
pip install -r requirements.txt
```

---

## ✨ Contribute & Explore

Feel free to fork, raise issues, or enhance features!

🌀 Built with care to help Bangalore breathe better.
📊 Forecast wisely. Breathe consciously.
