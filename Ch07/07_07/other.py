# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'], #parse the time column
    index_col='time' #and set it to the index
)
df = (
    df
    .resample('3min') #resample with 3 minute interval
    .mean()
    .reset_index()
)
df.head()

# %%
import plotly.express as px

fig = px.bar(
    df,
    x='time',
    y='height',
)
fig

# %%
fig.write_html('track.html')