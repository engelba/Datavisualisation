from matplotlib import projections
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np

import utils

all_temp_df = utils.data_load()

all_time_max_temp = all_temp_df.max().max()
all_time_min_temp = all_temp_df.min(axis=None).min()


# r = np.random.rand(365,1) * max_temp - min_temp 
theta = np.linspace(0, 2*np.pi, 365)

sns.set_style("white")


plt.ion()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

for i in range(10):
    plt.clf()

    ax.set_rlim(bottom=-50, top=30)
    ax.set_rticks([-50, 0, 30])

    max_temps = all_temp_df["max_temp"]
    min_temps = all_temp_df["min_temp"]

    ax.plot(theta, max_temps, label='Maximal temperature', color= sns.color_palette("Reds")[-2], alpha=0.7, linewidth=1)
    ax.plot(theta, min_temps, label='Minimal temperature', color= sns.color_palette("Blues")[-2], alpha=0.7, linewidth=1)

    ax.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))

    ax.set_xticklabels(['janv', 'fev', 'mars', 'avril', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'])

    ax.set_thetalim(0, 2*np.pi)

    ax.grid(True)
    ax.set_title("Year:{}", va='bottom')

    plt.draw()
    plt.pause(0.1)
    print("Pause")
