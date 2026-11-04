###############################
#pgram.py
#Calculate Lomb-Scargle periodogram of
#a dataset.
###############################

import numpy as np
from astropy.timeseries import LombScargle


###########  PGRAM CALC  ############

def pgram(t, y, dy, minper, maxper, faprate, strat = 'auto', x = 'pers', wind = 0):

    #####  INPUTS  #####
    
    ### t : observation times
    ### y : observation values (Fluxes, RVs, etc.)
    ### dy : observation errors
    ### minper : min period for range of pers in pgram calc.
    ### maxper : max period ''
    ### faprate : false alarm probability (FAP) rate cutoff (if 1%, set 0.01)
    
    ### x = 'pers' returns periods and pgram powers
      #    x = 'freq' reeturns frequencies and pgram powers
      
    ### stat = 'auto' uses astropy's auto frequency generator
      #     with 'samples_per_peak' set to 10 to make freq array,
      #     OTHERWISE strat = integer # of elements desired in frequency array

    #####  RETURNS  #####

    ### per/freq: period or frequency array depending on input 'x'
    ### power: associated pgram power array
    ### fap: power associated with input FAP rate cutoff

    #####  CODE  #####

    if wind == 0:
        ls = LombScargle(t, y, dy)     ###Generalized Lomb-Scargle

    if wind == 1:
        y = np.ones(t.size, dtype=np.longdouble)
        dy = 0.

        ls = LombScargle(t, y, dy, center_data=False, fit_mean=False)
        

    if strat == 'auto':
        if wind == 0:
            freq, power = ls.autopower(minimum_frequency=1/maxper, \
                                   maximum_frequency=1/minper, \
                                   samples_per_peak=1000)
        if wind == 1:
            freq, power = ls.autopower(minimum_frequency=1/maxper, \
                                   maximum_frequency=1/minper, \
                                   samples_per_peak=10, method = 'scipy')

    else:
        freq = 1. / np.linspace(maxper, minper, strat)

        if wind == 0:
            power = ls.power(freq)
            
        if wind == 1:
            power = ls.power(freq, method = 'scipy')

    if wind == 0:
        fap = ls.false_alarm_level([faprate])   #require 1% fap rate
    else:
        fap = 0.

    if x == 'pers':
        per = 1/freq
        order = np.argsort(per)
        per = per[order]
        power = power[order]

        return per, power, fap

    else:
        return freq, power, fap




