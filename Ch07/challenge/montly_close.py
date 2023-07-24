"""
Using the stock data from stocks.csv, draw a bar chart were:
- The x axis is the month
- The y axis is the median closing price
- Each stock should have it's own chart
"""

# %%
import pandas as pd

df = pd.read_csv('stocks.csv',
                 parse_dates=['Date'],
                 index_col='Date')

df.head()
# %%
df_pivot = (
    df
    .pivot(
        columns='Symbol',
        values='Close',  
    )
    .resample('M') # month
    .median()    
)

# %%
from calendar import month_abbr

ax = df_pivot.plot.bar(
    title='Median Montly Close', 
    rot=0
)

ax.set_xticklabels(
    [month_abbr[i+1] for i in ax.get_xticks()]
    )

ax.set_xlabel('Month')
ax.set_ylabel('Closing price') 

# %%
# Or:
import pandas as pd

df = pd.read_csv('stocks.csv',
                 parse_dates=['Date']
                 )

df.head()
    
# %%
df['Month']  = df['Date'].dt.month

df.head()

# %%
mdf = df.pivot_table(
    columns='Symbol', #groups/legend 
    index='Month', #groupby
    values='Close', 
    aggfunc='median'
)

mdf

# %%
ax = mdf.plot.bar(
    title='Median Monthly Close',
    rot=0
)

from calendar import month_abbr

ax.set_xticklabels(
    [month_abbr[i+1] for i in ax.get_xticks()]
)

ax.set_ylabel('Closing price')
# %%
