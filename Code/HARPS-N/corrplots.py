"""
corrplots.py
Created on Tue Sep  9 20:20:45 2025
@author: chantanelle.nava
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

#Inputs:
    
    #dat_arr:      2d data array, dims are N obs times x N activity 
    #              indicators + 2 (for time and RV columns)
    #
    #dat_err:      2d error array, dims are N obs times x N activity 
    #              indicators + 1 (for RV column)
    #labels:       list of strings of labels desired for RVs and activity 
    #              indicators
    #
    #analyzeinds : list of arrays - each array contains the indices of 
    #              desired analysis set (ex list: all inds, S1 only, S2 only)
    #
    #colors:       list of colors desired for each sub-analysis 
    #              (same number list elements as analyzeinds)
    #              tip: set colors[0] rel. dark for nice error bar contrast
    
#Output: 
    
    #Correlation plots for RV vs various activity indicators -
    #within each, various subsets of the data with listed spearman r value
    #and associated p-value



def corrplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colors, savepath):
    
    nplt =  len(pltlabs) - 1

    #Set # rows and columns based on total number of plots
    if nplt < 4:
        nc = 1     

    if ((nplt <= 8) & (nplt >= 4)):
        nc = 2
        
    if nplt > 9:
        nc = 3
   
    nr = int(np.ceil(nplt/nc))
    
    #open figure and scale size by numbers of columns and rows
    fig1 = plt.figure(figsize = (6*nc,6*nr))   
    
    
    for i in range(nplt):
        
        #open ith plot in figure
        ax =  fig1.add_subplot(nr, nc, i+1)
        
        #Remove numeric axis labels
        ax.axes.xaxis.set_ticks([])
        ax.axes.yaxis.set_ticks([])
        
        for j in range(len(subinds)):
            
            #cut down to just desired indices in ith plot
            dat_temp = dat_arr[subinds[j], :] 
            dat_terr = dat_err[subinds[j], :] 
            
            #establish temp vars for calculation and plotting
            xtemp = dat_temp[:, 1]
            ytemp = dat_temp[:,i+2]
            xterr = dat_terr[:, 0]
            yterr = dat_terr[:, i+1]
            
            #calculate current spearman r value for jth subset in ith plot
            r_temp = spearmanr(xtemp, ytemp)
            
            #errorbars before main plot so they dont cover points
            plt.errorbar(xtemp, ytemp, xerr = xterr, yerr = yterr, 
                         linestyle = 'None', color= colors[0], 
                         label = None)
            
            r_strnum = str(np.round(r_temp[0],2))
            p_strnum = str((r_temp[1]))
            #final plot of subset  - label in legend has r- and p-vals
            
            #####################################################
            
            #print(f'x max {xtemp.max()} and y min {ytemp.max()}')
            
            if i == 0:
                xmin = None
                xmax = None
                ymin = 55.8
                ymax = 56.4795
            
            if i == 1:
                xmin = None#-6
                xmax = None#19
                ymin = 7070
                ymax = 7122

            if i == 2:
                xmin = None#-7
                xmax = None#18
                ymin = -80
                ymax = -55
                
            if i == 3:
                xmin = None#-6
                xmax = None#18
                ymin = 0.146
                ymax = 0.1815
                
                
                            
                
            plt.xlim(xmin,xmax) 
            plt.ylim(ymin,ymax)
            #####################################################
                
                

            
            plt.plot(xtemp, ytemp, color = colors[j], 
                     label = r'$r_{s}$ = ' + f'{float(r_strnum)}' + 
                     ', p = ' + f'{float(p_strnum):.2e}', 
                     linestyle = 'None', marker = '.', markersize =  18)
            
        
        #Only put x label on bottom row
        if nc == 1:
            if i+1 == nr:
                plt.xlabel(pltlabs[0])
        else:
            if (i+1) > nr:
                plt.xlabel(pltlabs[0])
        plt.ylabel(pltlabs[i+1])
        
        plt.legend( ncol=2) 
        
    plt.tight_layout() 
    plt.savefig(savepath)       
    plt.show()
        
        
        