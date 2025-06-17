import pandas as pd

# Load merged data
df = pd.read_csv("merged_data.csv", parse_dates=["Date"])

# Rename for consistency
df.rename(columns={
    'AvgTemp': 'temperature',
    'Precipitation': 'precip',
    'MaxTemp': 'tmax',
    'MinTemp': 'tmin'
}, inplace=True)

# 🌟 Feature Engineering
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year

# Optional: Add 'hour' as 0 if not present
df['hour'] = 0

# 🧹 Handle missing values
df.dropna(inplace=True)

# ✅ Save preprocessed file
df.to_csv("preprocessed_data.csv", index=False)
print("✅ Preprocessing complete! Saved as preprocessed_data.csv")
