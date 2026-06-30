"""
This code looks at the harps10 time series data
and returns the minimum airmass per each day.

"""

import numpy as np

import pandas as pd


#Make the data all visable when using print
pd.set_option('display.max_columns', None)

# Read and creat the data table from specific CSV
df = pd.read_csv(r'/Users/jameshoenstine/Desktop/Research/2015-2025/harpn_sun_release_timeseries_2015-2025.csv')

#Create a refined data table of specific coloumns
air_mass_date = df[["night","bjd","airmass", "rv", "rv_err"]].copy()

#Convert the night coloumn into date format
air_mass_date['night'] = pd.to_datetime(air_mass_date['night'])

#Find min airmass per each day and set the index of the row
dates = air_mass_date.groupby(['night'])['airmass'].idxmin()

#Create data set from the airmass min row index accouting for night, airmass and rv
min_airmass = df.loc[dates, ['night', 'bjd', 'airmass', 'rv', 'rv_err']].reset_index(drop=True)



#To save the data set....

min_airmass.to_csv("/Users/jameshoenstine/air_mass_min_1_OBS_v2_err.csv")

