# %%
import pandas as pd

df = pd.read_csv(
    'stocks.csv',
    parse_dates=['Date'],
    index_col='Date'
)
df.head()

# %%
# Check msft (microsoft) price over time 
msft = df.query('Symbol == "MSFT"') # show only the rows with msft
msft['Close'].plot()

# %%
msft['Close'].plot.kde()

# %%
(
    df
    .pivot(
        columns='Symbol', 
        values='Volume' 
    )
    .resample('M') # By month
    .sum() 
    .plot.bar(xticks=range(12), rot=0)
)
# %%
