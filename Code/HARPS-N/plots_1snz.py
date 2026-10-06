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
datfile = '/Users/jameshoenstine/Desktop/Research/Pyorbit/all_seasons/1/1szn.csv'  ##### 12 SEASONS #####
datsep = ','
head = 0 

#Read in data
dat = pd.read_csv(datfile, sep = datsep, header = head) 
t = dat['bjd']
#Calculate errors that are missing for activity indicators
#No missing errors

#Determine seasonal indices
S12splt = float('57417.1')
S1inds = np.where(t < S12splt)[0]
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

subinds = [allinds, S1inds]
sublabs = [None, 'Season 1']
colrs = ['darkslateblue', 'cyan']

scattplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, 'scattplot_ex.png')


##################################
####### CORRELATION PLOTS ########

corrplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, '/Users/jameshoenstine/Desktop/Research/corr_plot/corrplot_ex.png')


##################################
######### PERIODOGRAMS ##########

Pmax_plt = 150.
fapr = 0.01
sublabs = ['Full Dataset', 'Season 1']
pgramplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colrs, Pmax_plt, fapr, 'pgramplots_ex.png')

