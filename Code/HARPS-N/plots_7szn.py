#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:28:21 2026

@author: jameshoenstine
"""


import pandas as pd
import numpy as np
from corrplots import corrplots
from scattplots import scattplots
from pgramplots import pgramplots

#Define vars needed to read in data
#datfile = '/Users/jameshoenstine/Desktop/Research/Pyorbit/all_seasons/1/allszn.csv' ##### ALL SEASONS #####
datfile = '/Users/jameshoenstine/Desktop/Research/Pyorbit/all_seasons/1/1234567szn.csv'  ##### 1234567 SEASONS #####
datsep = ','
head = 0 

#Read in data
dat = pd.read_csv(datfile, sep = datsep, header = head) 
t = dat['bjd']
#Calculate errors that are missing for activity indicators
#No missing errors

#Determine seasonal indices
S12splt = float('57417.1')
S23splt = float('57779.01')
S34splt = float('58069')
S45splt = float('58513.1')
S56splt = float('58814')
S67splt = float('59215')
S78splt = float('59609.1')
S1inds = np.where(t < S12splt)[0]
S2inds = np.where((t > S12splt) & (t < S23splt))[0]
S3inds = np.where((t > S23splt) & (t < S34splt))[0]
S4inds = np.where((t > S34splt) & (t < S45splt))[0]
S5inds = np.where((t > S45splt) & (t < S56splt))[0]
S6inds = np.where((t > S56splt) & (t < S67splt))[0]
S7inds = np.where((t > S67splt) & (t < S78splt))[0]
allinds = np.where(t>0)[0]


##################################
######### SCATTER PLOTS ##########

#example with 4 actinds
dat_arr = dat[['bjd', 'rv', 'contrast', 'fwhm', 'bis_span', 'smw']].to_numpy()
dat_err = dat[['rv_err', 'contrast_err', 'fwhm_err', 'bis_span_err', 'smw_err']].to_numpy()
pltlabs = ['RV', 'Contrast', 'FWHM', 'BIS', 'S-Index']

#example with 3 actinds
#dat_arr = dat[['jdb', 'vrad', 'contrast', 'fwhm', 'bis_span']].to_numpy()
#dat_err = dat[['svrad', 'con_err', 'fwhm_err', 'noise']].to_numpy()
#labels = ['RV', 'Contrast', 'FWHM', 'BIS']

subinds = [allinds, S1inds, S2inds, S3inds, S4inds, S5inds, S6inds, S7inds]
sublabs = [None, 'Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6', 'Season 7']
colrs = ['darkslateblue', 'cyan', 'magenta', 'red', 'yellow', 'purple', 'Green', 'orange']

scattplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, '/Users/jameshoenstine/Desktop/Research/scatt_plot/1ms_7szn.png')


##################################
####### CORRELATION PLOTS ########

corrplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, '/Users/jameshoenstine/Desktop/Research/corr_plot/1ms_7szn.png')


##################################
######### PERIODOGRAMS ##########

Pmax_plt = 150.
fapr = 0.01
sublabs = ['Full Dataset', 'Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', ' Season 6', 'Season 7']
pgramplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, Pmax_plt, fapr, '/Users/jameshoenstine/Desktop/Research/pgram_plots/1ms_7szn.png')

