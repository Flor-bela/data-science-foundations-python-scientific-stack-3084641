# %%
import matplotlib.pyplot as plt
import numpy as np

def plot_sin(limit):
    xs = np.linspace(-limit, limit, 100)
    plt.plot(xs, np.sin(xs), label='sin(x) [-%s - %s]' % (limit, limit))

plot_sin(6)
# this is static, but we want to make it interactive - - use Jupyter Widgets
# %%
from ipywidgets import interact

@interact(limit=6) # a decorator to our function
def plot_sin(limit):
    xs = np.linspace(-limit, limit, 100)
    plt.plot(xs, np.sin(xs), label='sin(x) [-%s - %s]' % (limit, limit))

# %%
from ipywidgets import IntSlider

@interact(limit=IntSlider(value=10, min=0, max=20))
def plot_sin(limit):
    xs = np.linspace(-limit, limit, 100)
    plt.plot(xs, np.sin(xs), label='sin(x) [-%s - %s]' % (limit, limit))

# %%
