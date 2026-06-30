#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 08:12:17 2026

@author: jameshoenstine
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as munits


df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Airmass < 1.8 three obs.csv')

df.set_index('Date')

season1 = df[df['Date'].between('2015-07-29 11:14:28.375', '2016-01-29 15:26:31.629')]
season2 = df[df['Date'].between('2016-07-29 11:11:19.793', '2017-01-26 17:32:39.455')]
season3 = df[df['Date'].between('2017-07-29 11:14:11.207', '2018-01-18 16:20:10.645')]
season4 = df[df['Date'].between('2018-07-29 11:10:39.682', '2019-01-29 15:21:33.623')]
season5 = df[df['Date'].between('2019-07-29 11:13:29.109', '2019-11-27 12:18:06.220')]
season6 = df[df['Date'].between('2020-07-29 11:15:50.811', '2021-01-29 15:21:16.072')]
season7 = df[df['Date'].between('2021-07-29 11:14:12.839', '2022-01-29 15:58:01.143')]
season8 = df[df['Date'].between('2022-07-29 11:14:34.809', '2023-01-21 15:18:22.915')]
season9 = df[df['Date'].between('2023-07-30 11:13:12.367', '2024-01-29 15:16:59.807')]
season10 = df[df['Date'].between('2024-07-31 11:12:08.075', '2025-01-29 15:22:08.281')]



x = df['bjd']
y = df['rv'] *1000
y_err = df['rv_err'] * 1000


plt.ylabel('RV (m/s)')
plt.xlabel('Date (BJD)')
plt.title('RV Per Time 10 Seasons')
plt.xticks(fontsize=7)
plt.xticks
plt.errorbar(x, y, yerr=y_err, fmt = 'o', color = "Blue", markersize = 0, elinewidth = 0)

x1 = season1['bjd']
y1 = season1['rv'] *1000
y1_err = season1['rv_err'] * 1000

x2 = season2['bjd']
y2 = season2['rv'] *1000
y2_err = season2['rv_err'] * 1000

x3 = season3['bjd']
y3 = season3['rv'] *1000
y3_err = season3['rv_err'] * 1000


x4 = season4['bjd']
y4 = season4['rv'] *1000
y4_err = season4['rv_err'] * 1000


x5 = season5['bjd']
y5 = season5['rv'] *1000
y5_err = season5['rv_err'] * 1000


x6 = season6['bjd']
y6 = season6['rv'] *1000
y6_err = season6['rv_err'] * 1000


x7 = season7['bjd']
y7 = season7['rv'] *1000
y7_err = season7['rv_err'] * 1000


x8 = season8['bjd']
y8 = season8['rv'] *1000
y8_err = season8['rv_err'] * 1000


x9 = season9['bjd']
y9 = season9['rv'] *1000
y9_err = season9['rv_err'] * 1000

x10 = season10['bjd']
y10 = season10['rv'] *1000
y10_err = season10['rv_err'] * 1000








plt.errorbar(x1, y1, yerr=y1_err, fmt='o', color="fuchsia", markersize = 2, elinewidth=1, label = "Season 1")
plt.errorbar(x2, y2, yerr=y2_err, fmt='o', color="crimson", markersize = 2, elinewidth=1, label = "Season 2")
plt.errorbar(x3, y3, yerr=y3_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 3")
plt.errorbar(x4, y4, yerr=y4_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 4")
plt.errorbar(x5, y5, yerr=y5_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 5")
plt.errorbar(x6, y6, yerr=y6_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 6")
plt.errorbar(x7, y7, yerr=y7_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 7")
plt.errorbar(x8, y8, yerr=y8_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 8")
plt.errorbar(x9, y9, yerr=y9_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 9")

plt.errorbar(x10, y10, yerr=y10_err, fmt='o',  markersize = 2, elinewidth=1, label = "Season 2020")
plt.title(label="Ten Seasons 2015 - 2025")
plt.ylabel('RV (m/s)')
plt.xlabel('Date (BJD)')
#plt.legend()
