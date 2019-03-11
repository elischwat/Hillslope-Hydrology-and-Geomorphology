#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:56:13 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from plotWaterTable import plotWaterTable
from plotWaterTablePlanar import plotWaterTablePlanar
from parameters import *
from exposure import exposure
from getDenudationRate import getDenudationRate
from DefaultParams import DenudationParameters

plt.figure(figsize=figDimSmall)

x = np.linspace(0,L,xRes)
#convert from 1 storm long exposure time to annual denudation (in meters)
timeLength = 1 #year
def convert(exp):
    return stormsPerYear*(exp + Tr)*getDenudationRate(*(DenudationParameters.kwargs_array))*timeLength

plt.subplot(3,1,1)
yCon = convert(exposure('con','convex'))
plt.plot(x,yCon,color='k', linestyle='--', label='Actual')
m,b = np.polyfit(x,yCon,1)
plt.plot(x,m*x+b, color='k', linestyle='-', label='Linear Fit')
print('Convergent: m = ' + str(m) + ' and b = ' + str(b))
plt.annotate('Convergent', xy=(100,0), fontsize=fontSmall,
             horizontalalignment='right', verticalalignment='bottom')
plt.xticks([])
plt.legend(frameon=False, ncol=2, fontsize=fontXSmall)

plt.subplot(3,1,2)
yUni = convert(exposure('uni','convex'))
plt.plot(x,yUni,color='k', linestyle='--')
m,b = np.polyfit(x,yUni,1)
plt.plot(x,m*x+b, color='k', linestyle='-')
print('Uniform: m = ' + str(m) + ' and b = ' + str(b))
plt.annotate('Uniform', xy=(100,0), fontsize=fontSmall,
             horizontalalignment='right', verticalalignment='bottom')
plt.xticks([])
plt.ylabel('Denudation by Dissolution (mm)', fontsize=fontSmall)

plt.subplot(3,1,3)
yDiv = convert(exposure('div','convex'))
plt.plot(x,yDiv,color='k', linestyle='--')
m,b = np.polyfit(x,yDiv,1)
plt.plot(x,m*x+b, color='k', linestyle='-')
print('Divergent: m = ' + str(m) + ' and b = ' + str(b))
#for i in range(0,3):
#    plt.subplot(3,1,i)
#    plt.xlabel('Denudation by Dissolution (m)')
plt.annotate('Divergent', xy=(100,0), fontsize=fontSmall,
             horizontalalignment='right', verticalalignment='bottom')
plt.xticks([0,50,100],[0,50,100],fontsize=fontSmall)

for i in range(1,4):
    plt.subplot(3,1,i)
    ax = plt.gca()    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.yticks([0.0,0.001],[0,1], fontsize=fontSmall)
    plt.xlim(-2,L+2)
    plt.ylim(0.0,0.001)
    

plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)
#plt.suptitle('Estimated Chemical Denudation over ' + str(timeLength) + 
#             ' Year on \nConvex Hillslopes ' + 
#             'with Linear Approximations', fontsize=fontSmall)
plt.savefig('images/3_convex_annual_denudation_w_linear_fits.png')
plt.show()