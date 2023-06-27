#%%
%pwd
# %%
from time import sleep

%time sleep(0.1)
# %%
%%time
for i in range(3):
    sleep(0.1)
# %%
!ls /var/log #ls = list of files
# %%
dirname = '/var/log' #Varlog directory
files = !ls $dirname
print(f'{len(files)} files at {dirname}')

# %%
