"""
pgramplots.py
Created on Tue Sep  9 22:55:01 2025
@author: chantanelle.nava
"""

import numpy as np
import matplotlib.pyplot as plt
from pgram import pgram
from peak_find import peak_find

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
    
#Output: 
    
    #Scatter plots for RV vs various activity indicators -
    #within each, various subsets of the data indicated with diff colors.

def pgramplots(dat_arr, dat_err, pltlabs, subinds, sublabs, colors, Pmax_plt, fapr, savepath):
    
    nplt = dat_arr.shape[1] - 1
    nsub = len(subinds)
    
    fig1 = plt.figure(figsize = (12,3*(nplt+1)))  #maybe 3 needs = pmax_arr
    
    Pmin = 1.5
    
    pkx = [None] * nsub
    Pmax_arr = np.zeros(nsub+1)# was 3 but changed for more seasons
     
    for i in range(nplt):
        
        ax =  fig1.add_subplot(nplt+1, 1, i+1)
        
        for j in range(nsub):
            
            dat_temp = dat_arr[subinds[j], :] 
            dat_terr = dat_err[subinds[j], :] 
            
            ttemp = dat_temp[:, 0]
            ytemp = dat_temp[:, i+1]
            yterr = dat_terr[:, i]
            
            Pmax = np.max(ttemp) - np.min(ttemp) 
            
            
            
            freq, pow, fap = pgram(ttemp, ytemp, yterr, Pmin, Pmax, fapr, x='freq')
            #print(freq)
            #print(pow)
            #log = np.log10(freq)  #GET RID OF THIS VARIABLE, NOT NECESSARY
            #print(log)
            #pers = 1./freq  #UNSURE THIS IS NECESSARY WITH THE WAY IT IS CURRENTLY STRUCTURED.
            
           
            ############################################ NEW AXIS ########################
            
            def val1(x):
                
                val = 1. / (10**x) # cant divide by 0 
                print(x)
                #for i in val:
                    #if i ==0:
                        #val + .00001
                    #else:
                        #val = val
                return val
            
                #return 1. / (x) # cant divide by 0
            #USE ONE OVER INSTEAD OF VAL1 FUNCTION IN THIS.
            def one_over(x):
                """Vectorized 1/x, treating x==0 manually"""
                x = np.array(x, float)
                near_zero = np.isclose(x, 0)
                x[near_zero] = np.inf
                x[~near_zero] = 1 / x[~near_zero]
                return x
            
            #non_zero = [i for i in data val1(x) !=0]
            # i think now that there is negatives the orginal additional method of adding breaks it 
            
            ax2 = ax.secondary_xaxis('top', functions = (one_over, one_over))
        
            ax2.set_xlabel('Period (d)')
        
            #ax2.set_xlim(ax.get_xlim())
            ax2.set_xticks([0, 50, 25, 16.6, 12.5,10])
            #ax2.set_xticks(np.logspace(freq[-1], freq[0], num=1)) #XX need to change THIS NEW VERSION WORKS BETTER, BUT IT NEEDS TWEAKING
            #THE XTICKS ARE OVERLAPPING, MAY WANT TO TAKE THIS OUT OF THE FOR LOOP. SEE DOCUMENTATION FOR NP.LOGSPACE FOR MORE INFO.
            ax2.tick_params(axis='x', which='major')
            
            
            ###############################################################################
   
            
            #color = colors[j]
            
            plt.plot(freq, pow, color = colors[j], label = sublabs[j])  #CHANGE THIS TO FREQ INSTEAD OF LOG
           
            
           
     
           
            plt.axhline(y = fap, linestyle = ':', color = colors[j])
            
            #################################################################################################
            
            plt.xlim([0.008, Pmax_plt])   # Break the code Axis limits cannot be NaN or Inf when at 0 for start
            
            #################################################################################################
            
            
            if (i == 0):
                pkx[j], pkpow = peak_find(freq, pow, fap)  #CHANGE THIS TO FREQ, NOT LOG
                Pmax_arr[j] = Pmax
                plt.legend(loc=('lower right'), bbox_to_anchor=(1.16,-.05))

            for k in range(pkx[j].size):
                plt.axvline(x=pkx[j][k], color = colors[j], linestyle = ':')  
            
        
        plt.ylabel(pltlabs[i])
    #print(f"Pgram_x {pkx}")
    #Calculate windowfunctions for diff subsets and add to bottom plot
    ax =  fig1.add_subplot(nplt+1, 1, nplt+1)
    
    for j in range(nsub):
        
        dat_temp = dat_arr[subinds[j], :] 
        dat_terr = dat_err[subinds[j], :]
        
        wx, wpow, wfap = pgram(dat_temp[:,0], dat_temp[:,1], dat_terr[:,0], Pmin, Pmax_arr[j], fapr, wind=1, x='freq')
        plt.plot(wx, wpow, color = colors[j]) #TAKE AWAY THE NP.LOG10 AND LEAVE WX IN ITS PLACE
        plt.xlim([0.008, .1]) 
        
        
        
        
            ########################################  GET 2ND AXIS #########################################################
            
        def one_over(x):
                """Vectorized 1/x, treating x==0 manually"""
                x = np.array(x, float)
                near_zero = np.isclose(x, 0)
                x[near_zero] = np.inf
                x[~near_zero] = 1 / x[~near_zero]
                return x
            
            #non_zero = [i for i in data val1(x) !=0]
            # i think now that there is negatives the orginal additional method of adding breaks it 
            
        ax2 = ax.secondary_xaxis('top', functions = (one_over, one_over))
        
        ax2.set_xlabel('Period (d)')
        
            #ax2.set_xlim(ax.get_xlim())
        ax2.set_xticks([0, 50, 25, 16.6, 12.5,10])
            #ax2.set_xticks(np.logspace(freq[-1], freq[0], num=1)) #XX need to change THIS NEW VERSION WORKS BETTER, BUT IT NEEDS TWEAKING
            #THE XTICKS ARE OVERLAPPING, MAY WANT TO TAKE THIS OUT OF THE FOR LOOP. SEE DOCUMENTATION FOR NP.LOGSPACE FOR MORE INFO.
        ax2.tick_params(axis='x', which='major')
        
        
        
        
        
            ######################################################################################################################
        
        
        for k in range(pkx[j].size):
            plt.axvline(x=pkx[j][k], color = colors[j], linestyle = ':') 
    
    plt.ylabel('Window Fn')
    plt.xlabel('Frequency (Hz)')
    


    #Final plot formatting    
    plt.tight_layout() 
    plt.savefig(savepath)       
    plt.show()
