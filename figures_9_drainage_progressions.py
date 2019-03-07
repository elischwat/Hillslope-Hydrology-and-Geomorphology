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
plt.figure(figsize=(10,3))

# PARAMETERS:
timeArray = [0, 6*3600, 12*3600, 24*3600]
# timeArray = [24*3600]
plotXMin = -3
plotXMax = L
plotYMin = 0
plotYMax = 0.06


# concave
concaveCon = []
concaveUni = []
concaveDiv = []
planarCon = []
planarUni = []
planarDiv = []
convexCon = []
convexUni = []
convexDiv = []
for drainTime in timeArray:
    concaveCon.append(plotWaterTable('con', 'concave', drainTime)[0:2])
    concaveUni.append(plotWaterTable('uni', 'concave', drainTime)[0:2])
    concaveDiv.append(plotWaterTable('div', 'concave', drainTime)[0:2])
    planarCon.append(plotWaterTablePlanar('con', drainTime)[0:2])
    planarUni.append(plotWaterTablePlanar('uni', drainTime)[0:2])
    planarDiv.append(plotWaterTablePlanar('div', drainTime)[0:2])
    convexCon.append(plotWaterTable('con', 'convex', drainTime)[0:2])
    convexUni.append(plotWaterTable('uni', 'convex', drainTime)[0:2])
    convexDiv.append(plotWaterTable('div', 'convex', drainTime)[0:2])



##          convergent, uniform, divergent
## concave
## planar
## convex

def prettify():
    plt.xlim(plotXMin,plotXMax); plt.ylim(plotYMin,plotYMax)
    plt.yticks([0.0,0.03,0.06], [0,3,6],fontsize=fontSmall)
    plt.xticks([0,50,100], [0,50,100], fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

for i in range(0,len(timeArray)):
    line = ''; col = '';
    if i == 0:
        line = '-'; col = 'k'
    elif i == 1:
        line = '-'; col = 'tab:gray'
    elif i == 2:
        line = '--'; col = 'tab:gray'
    elif i == 3:
        line = ':'; col = 'tab:gray'
        
plt.subplot(3,3,1)
plt.plot(concaveCon[i][0], concaveCon[i][1], color = col, linestyle=line)
prettify()
plt.xticks([])
plt.annotate('1', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)

plt.subplot(3,3,2)
plt.plot(concaveUni[i][0], concaveUni[i][1], color = col, linestyle=line)
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('2', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)

plt.subplot(3,3,3)
plt.plot(concaveDiv[i][0], concaveDiv[i][1], color = col, linestyle=line,
label=str(timeArray[i]/3600) + ' hrs')
prettify()
plt.yticks([])
plt.xticks([])
plt.legend(frameon=False, ncol=2, fontsize=fontXSmall)    
plt.annotate('3', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
#    
plt.subplot(3,3,4)
plt.plot(planarCon[i][0], planarCon[i][1], color = col, linestyle=line)
prettify()
plt.xticks([])    
plt.annotate('4', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
plt.ylabel('Water Table Height (cm)', fontsize=fontSmall)
#    
plt.subplot(3,3,5)
plt.plot(planarUni[i][0], planarUni[i][1], color = col, linestyle=line)
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('5', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
#    
plt.subplot(3,3,6)
plt.plot(planarDiv[i][0], planarDiv[i][1], color = col, linestyle=line)
prettify()
plt.yticks([])
plt.xticks([])    
plt.annotate('6', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
#    
plt.subplot(3,3,7)
plt.plot(convexCon[i][0], convexCon[i][1], color = col, linestyle=line)
prettify()
plt.annotate('7', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)	
plt.ylabel('Water Table Height (cm)', fontsize=fontSmall)

plt.subplot(3,3,8)
plt.plot(convexUni[i][0], convexUni[i][1], color = col, linestyle=line)
prettify()
plt.yticks([])
plt.annotate('8', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)

plt.subplot(3,3,9)
plt.plot(convexDiv[i][0], convexDiv[i][1], color = col, linestyle=line)
prettify()
plt.yticks([])
plt.annotate('9', xy=(0,0.06), verticalalignment='top', fontsize=fontLarge)
        
#plt.suptitle('Drainage of a Perched Water Table on 9 Hillslopes after X Number of Hours', fontsize=fontSmall)
plt.tight_layout()
plt.savefig('images/9_drainage_sequences_24hrs.png')
plt.show()