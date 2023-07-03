# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data


# %%
import pandas as pd
df = pd.read_parquet(out_file)
df.info()

# %%
df['tpep_pickup_datetime']

# %%
df['tpep_dropoff_datetime']

# %%
#This step is important to remove the cases that do not fit
mask = df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']
df = df[mask]
df

# %%
time = df['tpep_dropoff_datetime']- df['tpep_pickup_datetime']
time_hours = time / pd.Timedelta(1, 'hour')
speed = df['trip_distance']/time_hours


# %%
speed.mean()
