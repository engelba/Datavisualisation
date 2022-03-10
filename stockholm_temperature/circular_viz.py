from matplotlib import projections
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np
import imageio


import utils

all_temp_df = utils.data_load()

all_time_max_temp = all_temp_df.max().max()
all_time_min_temp = all_temp_df.min(axis=None).min()


# r = np.random.rand(365,1) * max_temp - min_temp 
theta = np.linspace(0, 2*np.pi, 365)

images = []
sns.set_style("white")
with plt.ion():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    start_year = 2010
    end_year = 2021
    for year in range(start_year, end_year+1):

        ax.set_rlim(bottom=-50, top=30)
        ax.set_rticks([-50, 0, 30])

        ax.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))

        ax.set_xticklabels(['janv', 'fev', 'mars', 'avril', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'])

        ax.set_thetalim(0, 2*np.pi)

        ax.grid(True)
        ax.set_title(f"{year}", va='bottom', y=0.455, x=1.2)

        fig.suptitle(f'Temperature evolution in Stockholm through years from {start_year} to {end_year}.')

        max_temps = all_temp_df["max_temp"]
        min_temps = all_temp_df["min_temp"]

        year_temp = all_temp_df[str(year)]

        ax.plot(theta, max_temps, label='Max. temp', color= sns.color_palette("Reds")[-2], alpha=0.7, linewidth=1)
        ax.plot(theta, min_temps, label='Min. temp', color= sns.color_palette("Blues")[-2], alpha=0.7, linewidth=1)
        ax.legend( loc="lower left", bbox_to_anchor=(0.9,0.9))
        

        plt.xticks(alpha=0.5)
        plt.yticks(alpha=0.5)

        for previous_year in range(year-5, year):
            try:
                previous_year_temp = all_temp_df[str(previous_year)]
                ax.plot(theta, previous_year_temp, color= sns.color_palette("Greys")[-2], alpha=0.7, linewidth=0.2)
            except:
                pass
        
        
        for day in range(0,365, 29):
            ax.plot(theta[day:day+39], year_temp[day:day+39], color= sns.color_palette("Greens")[-2], alpha=0.7, linewidth=1)
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

            images.append(image)
            plt.pause(0.001)
       
        plt.cla()

imageio.mimsave('./result/temp_evolution.gif', images, fps=15)
