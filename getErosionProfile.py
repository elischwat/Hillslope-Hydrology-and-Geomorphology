#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Returns erosion profile in meters per year
getErosionProfile.py

Created on Mon Feb  5 01:43:20 2018

@author: elischwat 
"""
import numpy as np
from parameters import *
from exposure import exposure
from getDenudationRate import getDenudationRate
from DefaultParams import DenudationParameters

timeLength = 1 #yeara
def convert(exp):
    return stormsPerYear*(exp + Tr)*getDenudationRate(*(DenudationParameters.kwargs_array)*timeLength

## Plan = con, div, uni
## Profile = convex,parallel, concave
def getErosionProfile(plan, profile):
    x = np.linspace(0,L,xRes)
    m,b = np.polyfit(x, convert(exposure(plan, profile)), 1)
    return m*x+b #might need to round to a certain number of sigNIFICANT digits  - 
                    # DO NOT USE np.around IT CUTS OFF AFTER GIVEN NUMBER OF DECIMALS

## Plan = con, div, uni
## Profile = convex,parallel, concave
#def getErosionProfile(plan, profile):
#    return convert(exposure(plan, profile))