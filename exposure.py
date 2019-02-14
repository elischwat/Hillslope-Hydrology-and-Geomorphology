#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Get fluid exposure times as a function of x.
Given a hilltype and curvature type, calculate
how long the perched water table remains above
the soil-saprolite interface, which is equivalent
to how long the soil-saprolite interface is
exposed to rainwater solution.

Uses:
    plotWaterTable.py
    plotWaterTablePlaner.py
    parameters.py

Parameters:
    hilltype    - hillslope planform type, valid arguments include "con", "div", and "uni"
    curvature   - hillslope profile type, valid arguments include "planar","convex", and "concave"

Returns:
    exposure - an array of time values for each discrete value of x along the hillslope (see variables dx and L in
                parameters.py) representing the amount of time that point on the soil-saprolite interface is exposed to
                rainfall solution after a storm of given intensity and length (see variables Tr and N in parameters.py)

Created on Tue Jan 16 20:34:08 2018
@author: elischwat
"""

import numpy as np
from plotWaterTable import plotWaterTable
from plotWaterTablePlanar import plotWaterTablePlanar
from parameters import *


def exposure(hilltype, curvature):
    exposure = np.zeros(xRes)
    for step in range(0,tResWater):
        if curvature == 'planar':
            xdrain, hdrain, lowZero, hiZero = plotWaterTablePlanar(hilltype,step*dtWater)
        else:
        #get new water table, returns limits of values above 0
            xdrain, hdrain, lowZero, hiZero = plotWaterTable(hilltype,curvature,step*dtWater) 
        # increase exposure times at appropriate points
        exposure[int(np.ceil(lowZero)) : int(np.ceil(hiZero))] += dtWater
    return exposure

