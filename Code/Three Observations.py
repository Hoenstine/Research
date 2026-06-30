#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:53:30 2026

@author: jameshoenstine
"""

import numpy as np
import pandas as pd


df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/2015-2025/harpn_sun_release_timeseries_2015-2025.csv')

mean = df['rv'].mean()
std = df['rv'].std() 

five = (std * 5) + mean

df = df[df['rv'] < five]

df = df[df['airmass']<= 1.8]

df['Date'] = df['file_root'].str.replace('HARPN.','').str.replace('T','-')

df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%d-%H-%M-%S.%f")

times = df[["Date","night","bjd","airmass", "rv", "rv_err", 'smw', 'smw_err', 'bis_span', 'bis_span_err']].copy()


times['night'] = pd.to_datetime(times['night'])


dates = times.groupby(['night'])['airmass'].idxmin()

min_airmass = df.loc[dates, ["Date","night","bjd","airmass", "rv", "rv_err", 'smw', 'smw_err', 'bis_span', 'bis_span_err']].reset_index(drop=True)

min_airmass.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Min_airmass_Hours_3.csv')
#times.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Full_hours.csv')
#%%
"""
This step will need to be repeated twice.
Once for the plus two hours and once for the minus two hours.
Changing varibles acordingly.
"""

df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Min_airmass_Hours_3.csv')
df1 = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Full_hours.csv')

#Make sure in date time formate
df['Date'] = pd.to_datetime(df['Date'])
df1['Date'] = pd.to_datetime(df1['Date'])


#Create the time difference
df['Date'] = df['Date'] - pd.Timedelta(hours=2)

#Data coloumn of specific coloumns from full data set
plus = df["Date"]


#New data frame which locates nearest value of Date coloumn
v1 = pd.merge_asof(plus, df1, on='Date', direction='nearest')

#Convert and save to a csv on computer
v1.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/minus_2_Hoursv2.csv')

#%%
#load in all new data frames
reg = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Min_airmass_Hours_3.csv')

plus = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/plus_2_Hoursv2.csv')

minus = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/minus_2_Hoursv2.csv')

#Create a data frame of all them
full = pd.concat([reg, plus, minus])

#Sort the data by Date
sorted_full = full.sort_values(by='Date')


#Convert and save to a csv on computer
sorted_full.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/3_airmass_OBS_New.csv')



