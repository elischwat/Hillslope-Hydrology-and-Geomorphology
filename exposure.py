#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Plot exposure times for various hillslopes after rainstorm and subseqeunt 
drainage.
Uses:
    plotWaterTable.py
Created on Tue Jan 16 20:34:08 2018
@author: elischwat
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:11:07 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from plotWaterTable import plotWaterTable
from plotWaterTablePlanar import plotWaterTablePlanar
from parameters import *


def exposure(hilltype, curvature):
    exposure = np.zeros(xRes)
    lastVal = 0
    lowZero = 0
    hiZero = 0
    for step in range(0,tResWater):
        if curvature == 'planar':
            xdrain, hdrain, lowZero, hiZero = plotWaterTablePlanar(hilltype,step*dtWater)
        else:
        #get new water table, returns limits of values above 0
            xdrain, hdrain, lowZero, hiZero = plotWaterTable(hilltype,curvature,step*dtWater) 
        # increase exposure times at appropriate points
        exposure[int(np.ceil(lowZero)) : int(np.ceil(hiZero))] += dtWater
    return exposure

#f, axarr = plt.subplots(3, 2)
                        
#convex
#a = -0.01
#B = -0.01
#expoConVex = exposure('con')
#axarr[0, 0].plot(np.linspace(0,L,xRes),expoConVex)
#expoDivVex = exposure('div')
#axarr[1, 0].plot(np.linspace(0,L,xRes),expoDivVex)
#expoUniVex = exposure('uni')
#axarr[2, 0].plot(np.linspace(0,L,xRes),expoUniVex)

#concave
#a = 0.01
#B = -2.01 
#expoConCave = exposure('con')
#axarr[0, 1].plot(np.linspace(0,L,xRes),expoConCave)
#expoDivCave = exposure('div')
#axarr[1, 1].plot(np.linspace(0,L,xRes),expoDivCave)
#expoUniCave = exposure('uni')
#axarr[2, 1].plot(np.linspace(0,L,xRes),expoUniCave)
#plt.plot(np.linspace(0,L,xRes),smooth(expo,1))

