# 🌤️ EnviroCast: Weather & Air Quality Dashboard for Bangalore

**EnviroCast** is a user-friendly **Streamlit dashboard** that allows users to **visualize**, **analyze**, and **predict** both **air quality** and **weather trends** in Bangalore.  
It merges pollution and weather datasets, applies machine learning models, and generates interactive charts and forecasts.

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
- Upload your **cleaned or preprocessed dataset** (`.csv`).
- View a quick **preview** and list of **columns** detected.

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

---

## 🧩 How to Use

### 1. 🔧 Install Requirements

Make sure you have Python 3.10+ installed. Then install the required packages:

```bash
pip install -r requirements.txt
````

---

### 2. ▶️ Start the App

To launch the dashboard locally:

```bash
streamlit run app.py
```

It will open in your browser 

---

### 3. 📊 Upload Your Own Dataset

If you have two separate CSV files:

* **`air_quality.csv`**
* **`weather.csv`**

Follow this process:

#### ✅ Step 1: Merge the Datasets

Merge based on the common `Date` column:

```bash
python merge_datasets.py
```

This creates `merged_data.csv`.

#### 🧼 Step 2: Preprocess the Data

Clean the merged data for modeling:

```bash
python preprocess.py
```

This creates `preprocessed_data.csv` — which you can **upload on the dashboard**.

---

## 🔁 Model Training (Optional)

If you want to retrain or update your models:

```bash
python train_models.py
```

This reads `preprocessed_data.csv` and saves ML models (e.g., `model_no2.pkl`, `model_temp.pkl`) to the `/models` folder.

---

## 📦 Requirements

Contents of `requirements.txt`:

```txt
streamlit
pandas
scikit-learn
xgboost
matplotlib
joblib
```

Install using:

```bash
pip install -r requirements.txt
```

---

## ✨ Contribute & Explore

Feel free to fork the repo, open issues, or contribute enhancements!

🌀 Built with care to help Bangalore breathe better.
📊 Forecast wisely. Breathe consciously.

