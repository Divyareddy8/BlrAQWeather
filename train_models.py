import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import joblib
import os

# Ensure models/ directory exists
os.makedirs("models", exist_ok=True)

# Load preprocessed data
df = pd.read_csv("data/preprocessed_data.csv", parse_dates=["Date"])

# Create datetime column manually
df["datetime"] = pd.to_datetime(df["Date"]) + pd.to_timedelta(df["hour"], unit="h")

# ------------------------
# 🔹 Model 1: Predict NO2
# ------------------------
X_no2 = df[['temperature', 'precip', 'tmax', 'tmin', 'day', 'month', 'hour']]
y_no2 = df['NO2']

X_train_no2, X_test_no2, y_train_no2, y_test_no2 = train_test_split(
    X_no2, y_no2, test_size=0.2, random_state=42
)

model_no2 = RandomForestRegressor()
model_no2.fit(X_train_no2, y_train_no2)

# Save NO2 model
joblib.dump(model_no2, "models/model_no2.pkl")
print(" model_no2.pkl saved!")


# -----------------------------------------------
# 🔹 Model 2: Predict Next Day's Temperature
# -----------------------------------------------
df['target_temp'] = df['temperature'].shift(-1)
df_temp = df.dropna()

X_temp = df_temp[['temperature', 'precip', 'tmax', 'tmin', 'day', 'month']]
y_temp = df_temp['target_temp']

X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(
    X_temp, y_temp, test_size=0.2, random_state=42
)

model_temp = XGBRegressor()
model_temp.fit(X_train_temp, y_train_temp)

# Save temperature model
joblib.dump(model_temp, "models/model_temp.pkl")
print(" model_temp.pkl saved!")
