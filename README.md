# 🌤️ EnviroCast: Weather & Air Quality Dashboard for Bangalore

EnviroCast is a user-friendly Streamlit dashboard that allows users to visualize, analyze, and predict **air quality** and **weather trends** in Bangalore. It combines pollution and climate datasets to generate interactive visualizations and forecasts using machine learning.

---

## 🚀 Features

### 📂 CSV Upload
- Upload your **cleaned or preprocessed dataset** (CSV format).
- Get a quick **preview** of the dataset.
- View all available **columns** and parameters.

### 📈 Trend Visualization
- Choose any column (e.g., NO₂, PM2.5, Temperature) to plot time-series **line charts**.
- Great for analyzing pollution and weather patterns over time.

### 🧠 Predictive Modeling
- Use sliders to input:
  - 🌡️ Temperature, Max/Min Temp, Precipitation
  - 📆 Day, Month, Hour of the day
- Predict:
  - 🔬 **Nitrogen Dioxide (NO₂)** level
  - 🌡️ **Temperature (next hour)**
  - 🧪 **PM2.5** – Particulate Matter < 2.5µm  
  - 🧪 **PM10** – Particulate Matter < 10µm  
  - 🧪 **CO** – Carbon Monoxide (ppm)

---

## 🧩 How to Use

### 1. 🔧 Install Dependencies

Make sure you have Python 3.10+ installed, then install dependencies using:

```bash
pip install -r requirements.txt
````

---

### 2. 📊 If You Want to Upload Your Own Data

If you have these data individually:

* **Air quality data** (`air_quality.csv`)
* **Weather data** (`weather.csv`)

Use the following workflow:

#### ✅ Merge the Datasets

Run:

```bash
python merge_datasets.py
```

This merges both datasets **on the Date column** and saves as `merged_data.csv`.

#### 🧼 Preprocess the Merged Data

Run:

```bash
python preprocess.py
```

This cleans and transforms the data, saves as `preprocessed_data.csv`.

> ✅ Now upload `preprocessed_data.csv` via the web dashboard to visualize and make predictions!

---


## 📦 Requirements

Your `requirements.txt` should include:

```txt
streamlit
pandas
scikit-learn
xgboost
matplotlib
joblib
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training (Optional)

If you want to **retrain models**, run:

```bash
python train_models.py
```

This uses `preprocessed_data.csv` and saves `.pkl` models to the `models/` folder.

---

## 💬 Credits

Developed by Divya🌱
Guided by curiosity in data + environment + visualization 🌍✨
🟢 Feel free to contribute or fork! Happy Forecasting ☁️📊

