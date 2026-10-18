#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""           
               Gabe Hoensitne - May 13 2026
                
This code is used to create a foe planet and inject the radial velocity 
from said planet into radial velocity data from HARPS-N ten year survey.


The output will let you either create full seasons with all parameters you want.
Or you can create a working .dat file for Pyorbit runs

"""

from Keplerian import Keplerian
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd



df = pd.read_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/Full_szn_min_air.csv') # Import the min airmass data frame

############ HARPS-N data is in km and we want in m ############

df['rv'] = df['rv']*1000
df['rv_err'] = df['rv_err'] * 1000
df['bis_span'] = df['bis_span'] * 1000
df['bis_span_err'] = df['bis_span_err'] * 1000
df['fwhm'] = df['fwhm'] * 1000
df['fwhm_err'] = df['fwhm_err'] * 1000

t  = df['bjd']
K = 1.0
P = 80.0
e = 0.0
arg = 30.0
tp = 15.0

rv = Keplerian(t, K, P, e, arg, tp)

kep = pd.DataFrame(rv, columns=['rv'])
#kep.to_csv('/Users/jameshoenstine/Desktop/Research/Data sheets/1 Observation/rv_kep.csv')
# plt.xlabel("Time (BJD)")
# plt.ylabel("RV (m/s)")
# plt.title("Two Season Simulated RVs")
# plt.scatter(t,rv,color="red")


df['rv'] = df['rv'] + kep['rv'] # combines the foe rv and solar rv

#df['jitter'] = 0 # Used for creating Pyorbit .dat file
#df['offset'] = 0 # Used for creating Pyorbit .dat file

df = df[['bjd', 'rv', 'rv_err', 'fwhm', 'fwhm_err', 'bis_span', 'bis_span_err', 'smw', 'smw_err', 'contrast', 'contrast_err']] # USE FOR REGULAR SEASONS
#df = df[['bjd', 'rv', 'rv_err', 'jitter' , 'offset']] ##### USE FOR .DAT FILE FOR PYORBIT #####


########################## CREATE SEASONS ########################## 
"""
The Seasons are not consistently the same six month span. Due to some seasons would
have considerably less days then others. Season 3,5,6,9 are all shifted to gain
more data samples.

"""

df.set_index('bjd') 

season1 = df[df['bjd'].between(float('57233'), float('57417.1'))]
season2 = df[df['bjd'].between(float('57599'), float('57779.1'))]
season3 = df[df['bjd'].between(float('57887'), float('58069'))]
season4 = df[df['bjd'].between(float('58329'), float('58513.1'))]
season5 = df[df['bjd'].between(float('58630'), float('58814.1'))]
season6 = df[df['bjd'].between(float('59031'), float('59215'))]
season7 = df[df['bjd'].between(float('59425'), float('59609.1'))]
season8 = df[df['bjd'].between(float('59790'), float('59966.1'))]
season9 = df[df['bjd'].between(float('60112'), float('60295'))]
season10 = df[df['bjd'].between(float('60523'), float('60705.1'))]



################## CREATES COMBINED SEASONS ##################

szn12 = pd.concat([season1,season2],ignore_index=True, sort=False)
szn123 = pd.concat([season1,season2,season3],ignore_index=True, sort=False)
szn1234 = pd.concat([season1,season2,season3,season4],ignore_index=True, sort=False)
szn12345 = pd.concat([season1,season2,season3,season4,season5],ignore_index=True, sort=False)
szn123456 = pd.concat([season1,season2,season3,season4,season5,season6],ignore_index=True, sort=False)
szn1234567 = pd.concat([season1,season2,season3,season4,season5,season6,season7],ignore_index=True, sort=False)
szn12345678 = pd.concat([season1,season2,season3,season4,season5,season6,season7,season8],ignore_index=True, sort=False)
szn123456789 = pd.concat([season1,season2,season3,season4,season5,season6,season7,season8,season9],ignore_index=True, sort=False)
szn12345678910 = pd.concat([season1,season2,season3,season4,season5,season6,season7,season8,season9,season10],ignore_index=True, sort=False)





################## SAVES COMBINED SEASONS AS CSV ##################



szn12.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12.csv')
szn123.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123.csv')
szn1234.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn1234.csv')
szn12345.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345.csv')
szn123456.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123456.csv')
szn1234567.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn1234567.csv')
szn12345678.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345678.csv')
szn123456789.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123456789.csv')
szn12345678910.to_csv('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345678910.csv')



################## USE FOR .DAT CREATION FOR PYORBIT ##################



np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season1.dat', season1, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season2.dat', season2, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season3.dat', season3, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season4.dat', season4, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season5.dat', season5, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season6.dat', season6, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season7.dat', season7, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season8.dat', season8, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season9.dat', season9, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/season10.dat', season10, fmt='  %.6f',delimiter='   ',)




################## CREATES COMBINED SEASONS FOR .DAT FILES FOR PYORBIT  ##################



np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12.dat', szn12, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123.dat', szn123, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn1234.dat', szn1234, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345.dat', szn12345, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123456.dat', szn123456, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn1234567.dat', szn1234567, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345678.dat', szn12345678, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn123456789.dat', szn123456789, fmt='  %.6f',delimiter='   ',)
np.savetxt('/Users/jameshoenstine/Desktop/Research/Code/HARPS_Code/10_szn_1ms/szn12345678910.dat', szn12345678910, fmt='  %.6f',delimiter='   ',)






