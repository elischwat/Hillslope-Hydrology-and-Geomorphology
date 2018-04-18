 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:36:35 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from plotWaterTable import plotWaterTable
from plotWaterTablePlanar import plotWaterTablePlanar
from parameters import *
from exposure import exposure
from getDenudationRate import getDenudationRate
plt.figure(figsize=(10,3))

#convert from 1 storm long exposure time to annual denudation (in meters)
timeLength = 1 #year
def convert(exp):
    return stormsPerYear*(exp + Tr)*getDenudationRate()*timeLength

##          convergent, uniform, divergent
## concave
## planar
## convex
plotXMin = -3
plotXMax = L
plotYMin = 0
plotYMax = 0.0015

x = np.linspace(0,L,xRes)

def prettify():
    plt.xlim(plotXMin,plotXMax)
    plt.ylim(plotYMin,plotYMax)
    plt.xticks([0,50,100],[0,50,100] , fontsize=fontSmall)
    plt.yticks([0,plotYMax],[0,plotYMax*10**3], fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
        
#plt.subplot(3,3,1)
#y = convert(exposure('con', 'concave'))
#plt.plot(x, y, color='k')
#prettify()
#plt.xticks([])
#plt.annotate('1', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
#
#plt.subplot(3,3,2)
#y = convert(exposure('uni', 'concave'))
#plt.plot(x, y, color='k')
#prettify()
#plt.yticks([])
#plt.xticks([])    
#plt.annotate('2', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
#
#plt.subplot(3,3,3)
#y = convert(exposure('div', 'concave'))
#plt.plot(x, y, color='k')
#prettify()
#plt.yticks([])
#plt.xticks([])    
#plt.annotate('3', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)

plt.subplot(1,2,1)
y = convert(exposure('con','planar'))
plt.plot(x, y, color='k')
prettify()
plt.xticks([])    
#plt.annotate('4', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
plt.ylabel('Chemical Denudation (mm)', fontsize=fontSmall)
prettify()

#plt.subplot(3,3,5)
#y = convert(exposure('uni', 'planar'))
#plt.plot(x, y, color='k')
#prettify()
#plt.yticks([])
#plt.xticks([])    
#plt.annotate('5', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)

plt.subplot(1,2,2)
y = convert(exposure('div', 'planar'))
plt.plot(x, y, color='k')
prettify()
plt.yticks([])
plt.xticks([])    
#plt.annotate('6', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
prettify()
plt.yticks([])

#plt.subplot(3,3,7)
#y = convert(exposure('con', 'convex'))
#plt.plot(x, y, color='k')
#prettify()
#plt.annotate('7', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
#
#plt.subplot(3,3,8)
#y = convert(exposure('uni', 'convex'))
#plt.plot(x, y, color='k')
#prettify()
#plt.yticks([])
#plt.annotate('8', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)
#plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)
#
#plt.subplot(3,3,9)
#y = convert(exposure('div', 'convex'))
#plt.plot(x, y, color='k')
#prettify()
#plt.yticks([])
#plt.annotate('9', xy=(0,plotYMax), verticalalignment='top', fontsize=fontLarge)

#plt.suptitle('Estimated Chemical Denudation over ' + str(timeLength) + ' Year ' + 
#             '(Dissolution Rate ' + str(R_dis) + ')', fontsize=fontSmall)
plt.tight_layout()
plt.savefig('images/9_annual_denudation_Rd_' + str(R_dis))
plt.show()