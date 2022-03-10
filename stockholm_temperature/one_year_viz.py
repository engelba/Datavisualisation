from cProfile import label
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np

import utils

all_temp_df = utils.data_load()

# Visualisation for one year
YEAR = 2016

sns.set_style("white")

fig = plt.figure()
ax = plt.gca()

observation_dates = np.arange(0,365,1)
ax.plot(observation_dates, all_temp_df[str(YEAR)], label=f'Year {YEAR}',color= sns.color_palette("Greens")[-2], alpha=0.7, linewidth=1)
ax.plot(observation_dates, all_temp_df['mean_temp'], label='Mean temperature', color= sns.color_palette("Purples")[-2], alpha=0.7, linewidth=1)
ax.plot(observation_dates, all_temp_df['max_temp'], label='Maximal temperature', color= sns.color_palette("Reds")[-2], alpha=0.7, linewidth=1)
ax.plot(observation_dates, all_temp_df['min_temp'], label='Minimal temperature', color= sns.color_palette("Blues")[-2], alpha=0.7, linewidth=1)

ax.set_xlabel('Months')
ax.set_ylabel('Degrees (C)')

ax.set_title('Highest, lowest and mean temperature since 1756 in Stockholm.')

months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
monthsFmt = DateFormatter("%b")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)

plt.xticks(alpha=0.5)
plt.yticks(alpha=0.5)

ax.legend()

ax.fill_between(observation_dates, all_temp_df['mean_temp'], all_temp_df[str(YEAR)], where = all_temp_df['mean_temp'] < all_temp_df[str(YEAR)], facecolor=sns.light_palette("red")[4], alpha=0.1)
ax.fill_between(observation_dates, all_temp_df[str(YEAR)], all_temp_df['mean_temp'],where = all_temp_df[str(YEAR)] < all_temp_df['mean_temp'] , facecolor=sns.light_palette("blue")[4], alpha=0.1)

plt.savefig(f"./result/temp_{YEAR}")

plt.show()
