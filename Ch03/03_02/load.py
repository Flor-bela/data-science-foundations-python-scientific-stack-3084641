# %% File size
from pathlib import Path

kb = 2**10

csv_file = Path('track.csv')
csv_file.stat().st_size / kb #st_size is in bytes
#The result is in kilobyte
# %%
!ls -lh $csv_file #only works on Linus or Mac not on windows

# %% First few lines & line count
count = 0
with csv_file.open() as fp:
    for lnum, line in enumerate(fp, 1):
        count += 1
        if lnum <= 5:
            print(line, end='')
print(f'{count} lines')

# %% First few lines
!head -5 $csv_file

# %% Line count
!wc -l $csv_file

# %% Load to data frame
import pandas as pd

df = pd.read_csv(csv_file)
len(df)

# %%
df.columns
# %%
df.info()
# %%
df.describe()

# %%
