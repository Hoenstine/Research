
""" 
                           Gabe Hoenstine

The purpose of this is to find the min airmass from the HARPS-N
for each day. While exluding outlier samples.

"""

import numpy as np
import pandas as pd


df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/2015-2025/harpn_sun_release_timeseries_2015-2025.csv') # FULL HARPS DATA


mean = df['rv'].mean() # Find the mean radial velocity
std = df['rv'].std()   # Find the standard devation of radial velocity

#### Find a 3 and a half sigma, giving .9995 confidence interval ####

three_half_plus = ( std * 3.5) + mean  # Upper limit
three_half_minus = mean - ( std * 3.5) # Lower limit

df = df[df['rv'] <= three_half_plus]   # Upper limit
df = df[three_half_minus <= df['rv']]  # Lower limit

df = df[df['airmass']<= 1.8] # Creating a max airmass of 1.8, which corresponds 2 sigma detection

df['Date'] = df['file_root'].str.replace('HARPN.','').str.replace('T','-') # clean up the file root

df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%d-%H-%M-%S.%f") # Create date time object

times = df[["Date","night","bjd","airmass", "rv", "rv_err", 'smw', 'smw_err', 'bis_span', 'bis_span_err', 'fwhm', 'fwhm_err', 'contrast','contrast_err']].copy() # Creates data frame we want


times['night'] = pd.to_datetime(times['night']) # Creates a date time object


dates = times.groupby(['night'])['airmass'].idxmin() # indexes the min airmass per night

min_airmass = df.loc[dates, ["Date","night","bjd","airmass", "rv", "rv_err", 'smw', 'smw_err', 'bis_span', 'bis_span_err', 'fwhm', 'fwhm_err', 'contrast','contrast_err']].reset_index(drop=True)# creates array of the min airmass index

min_airmass.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Full_szn_min_air.csv') # saves as a csv
