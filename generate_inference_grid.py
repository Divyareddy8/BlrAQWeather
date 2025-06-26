import pandas as pd
import numpy as np

# Define Bangalore grid ranges
lats = np.arange(12.85, 13.20, 0.005)
lons = np.arange(77.45, 77.80, 0.005)

# Fill dummy (reasonable) values for features
data = []
for lat in lats:
    for lon in lons:
        data.append({
            "latitude": lat,
            "longitude": lon,
            "temperature": 27,
            "precip": 0.1,
            "tmax": 32,
            "tmin": 22,
            "day": 15,
            "month": 6,
            "hour": 14
        })

df = pd.DataFrame(data)

# Save both years (they can be identical if you don't have different data)
df.to_csv("data/blr_2019_inference.csv", index=False)
df.to_csv("data/blr_2022_inference.csv", index=False)

print(" Grid CSVs generated successfully.")
