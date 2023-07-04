# Draw the running track from track.csv
#
# - Sample data to a minute interval
# - Markers should be blue if the height is below 100 meter, otherwise red

# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
    )

df.info()

# %%
import folium

m = folium.Map(
    location=center,
    zoom_start=15,
)


def add_marker(row):
    loc = tuple(row[['lat', 'lng']])
    marker = folium.CircleMarker(
        loc,
        radius=5,
        color='blue' if row['height'] < 100 else 'red',
        popup=row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

df.apply(add_marker, axis=1)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)
min_df = df.resample('min').mean()
min_df.apply(add_marker, axis=1)
m
