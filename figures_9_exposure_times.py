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
plt.figure(figsize=figDimLarge)

##          convergent, uniform, divergent
## concave
## planar
## convex
plotXMin = -3
plotXMax = L
plotYMin = 0
plotYMax = 3*3600*24

x = np.linspace(0,L,L)

def prettify():
    plt.xlim(plotXMin,plotXMax); plt.ylim(plotYMin,plotYMax)
    plt.yticks([0, 1.5*3600*24, 3*3600*24], [0, 1.5, 3], fontsize=fontSmall)
    plt.xticks([0,50,100], [0,50,100], fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
        
plt.subplot(3,3,1)
plt.plot(x, exposure('con', 'concave'), color='k')
prettify()
plt.xticks([])
plt.annotate('1', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')

plt.subplot(3,3,2)
plt.plot(x, exposure('uni', 'concave'), color='k')
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('2', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')

plt.subplot(3,3,3)
plt.plot(x, exposure('div', 'concave'), color='k')
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('3', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')

plt.subplot(3,3,4)
plt.plot(x, exposure('con', 'planar'), color='k')
prettify()
plt.xticks([])    
plt.annotate('4', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')
plt.ylabel('Exposure Time (days)', fontsize=fontSmall)

plt.subplot(3,3,5)
plt.plot(x, exposure('uni', 'planar'), color='k')
prettify()
plt.yticks([])
plt.xticks([]) 
plt.annotate('5', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top') 

plt.subplot(3,3,6)
plt.plot(x, exposure('div', 'planar'), color='k')
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('6', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')

plt.subplot(3,3,7)
plt.plot(x, exposure('con', 'convex'), color='k')
prettify()
plt.annotate('7', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')

plt.subplot(3,3,8)
plt.plot(x, exposure('uni', 'convex'), color='k')
prettify()
plt.yticks([])
plt.annotate('8', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')
plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)

plt.subplot(3,3,9)
plt.plot(x, exposure('div', 'convex'), color='k')
prettify()
plt.yticks([])
plt.annotate('9', xy=(0,plotYMax), fontsize=fontLarge, verticalalignment='top')
        
#plt.suptitle('Exposure Time on the Soil-Saprolite Interface on 9 Hillslopes', fontsize=fontSmall)
plt.tight_layout()
plt.savefig('images/9_exposure_times.png')
plt.show()

