#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:03:22 2026

@author: jameshoenstine
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as munits
from Keplerian import Keplerian

df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/1 Observation/ 2015-2017.csv')

df2015 = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/1 Observation/ Season 1.csv')

df2016 = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/1 Observation/ Season 2.csv')





x = df['bjd']
y = df['rv'] *1000
y_err = df['rv_err'] * 1000


plt.ylabel('RV (m/s)')
plt.xlabel('Date (BJD)')
plt.title('RV Per Time 2015-2017')
plt.xticks(fontsize=7)
plt.xticks
plt.errorbar(x, y, yerr=y_err, fmt = 'o', color = "black", markersize = 2, elinewidth = 1, label = 'Stellar Signal',zorder=0)

x1 = df2015['bjd']
y1 = df2015['rv'] *1000
y1_err = df2015['rv_err'] * 1000

x2 = df2016['bjd']
y2 = df2016['rv'] *1000
y2_err = df2016['rv_err'] * 1000

#plt.errorbar(x1, y1, yerr=y1_err, fmt='o', color="fuchsia", markersize = 3, elinewidth=1, label = "Season 1")
#plt.errorbar(x2, y2, yerr=y2_err, fmt='o', color="crimson", markersize = 3, elinewidth=1, label = "Season 2")

plt.legend()




df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/1 Observation/ 2015-2017.csv')

#t  = np.linspace(0,502,num=502)

t = df['bjd']

K = 1.0
P = 80.0
e = 0.0
arg = 30.0
tp = 15.0

rv = Keplerian(t, K, P, e, arg, tp)

plt.scatter(t,rv,color= 'red', s=4,label = 'Keplerian Signal')
plt.title(label = 'Overlayed Signals')
plt.ylabel('RV (m/s)')
plt.xlabel('Date (BJD)')
plt.legend()
