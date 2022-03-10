from tokenize import String
import pandas as pd
import numpy as np

def data_load(path: String = "./data/stockholm_daily_mean_temperature.csv" ) -> pd.DataFrame:
    # Dataset loading
    df_temp = pd.read_csv("./data/stockholm_daily_mean_temperature.csv")
    df_temp['date'] = pd.to_datetime(df_temp['date'], infer_datetime_format=True)
    df_temp = df_temp.sort_values("date").drop(['raw', 'adjust', 'site'], axis=1)

    first_year = df_temp["date"][0].year
    last_year = df_temp["date"][len(df_temp)-1].year

    # Dataset of mean value for each day of the year
    observation_dates = np.arange(f'{1756}-01-01', f'{1756+1}-01-01', dtype="datetime64[D]")
    year_df = df_temp[df_temp['date']<observation_dates[-1]]
    year_df = year_df[year_df['date']>=observation_dates[0]].reset_index().drop('index', axis=1)

    years_val_dict = {'1756':year_df.drop( 59, axis=0 ).reset_index().drop('index', axis=1)["homo"].rename(str(1756))}

    # We separate all values year by year and store each DF in a dictionnary indexed by year
    for year in range(first_year+1, last_year+1):
        
        observation_dates = np.arange(f'{year}-01-01', f'{year+1}-01-01', dtype="datetime64[D]")

        year_df = df_temp[df_temp['date']<observation_dates[-1]]
        year_df = year_df[year_df['date']>=observation_dates[0]].reset_index().drop('index', axis=1)

        if len(year_df) == 365: # Leap year
            year_df = year_df.drop( 59, axis=0 ).reset_index().drop('index', axis=1)

        years_val_dict[str(year)] = year_df["homo"].rename(str(year))

    # We create a dataset containing all temperatures for each day and for each year.
    all_temp_df = pd.DataFrame(years_val_dict, index=[i for i in range(0,365)])

    all_temp_df['mean_temp'] = all_temp_df.mean(axis=1)
    all_temp_df['max_temp'] = all_temp_df.max(axis=1)
    all_temp_df['min_temp'] = all_temp_df.min(axis=1)
    all_temp_df['std_temp'] = all_temp_df.std(axis=1)

    return all_temp_df
