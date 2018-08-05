#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
File containing parameters for all perched water table files.
Created on Wed Jan 17 10:02:55 2018
@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"


curvature = 'convex'

#SPACE:
dx = 1.0 # Space step for numerical simulation of hillslope evolution.
L = 100.0 # Horizontal extent of hillslope
xRes = int(L/dx)
#TIME:
dtGeo = 10.0 # Time step for numerical simulation of hillslope evolution.
T = 10000 # Length of hillslope evolution simulation.
tResGeo = int(T/dtGeo)


# GEOMORPH STUFF:
D = 0.01 # m^2/yr,  Soil creep diffusivity
bmid = 20 # m, Countour width at x = L/2
c = 0.2 # m/m, Magnitude of convergence/divergence rate 

# GEOCHEMISTRY STUFF
R_dis = 2* 10**-9 # mol/m^2/s Mineral dissolution rate for chem denudation estimates.
soilDensity = 1.25 * 10**3 # kg/m^3, Density of soil.
dz = 0.1 # m, Thickness of saprolite layer in which mineral dissolution is accounted for.
ralb = 0.5 # Percent of saprolite composed of mineral for which dissolution is accounted for.
Ds = .001
#As = 4*np.pi*(0.5*Ds)**2 #spherical 
As = 6*Ds**2 #cubic
M = 263.02
rho = 2.62*10**6


# WATER TABLE STUFF:
dtWater = 361
Td = 3600.0*360
tResWater = int(Td/dtWater)
k = 10**-3
Tr = 3600.0*3.0 #3 hour storm at rate of...
N = 0.01/3600 #1 cm per hour
Nd = -((0.001)/3600) # 1mm per hour or 2.7E-7 m/s
stormsPerYear = 2*52

a = 0; B = 0
if curvature == 'convex':
    a = -0.005
    B = -0.01
elif curvature == 'concave':
    a = 0.005
    B = -1.01
elif curvature == 'planar':
    a = 0
    B = -0.51
else:
    raise ValueError('Curvature in parameters.py not set right.')
    
a_vex = -0.005
B_vex = -0.01
a_cave = 0.005
B_cave = -1.01
a_planar = 0
B_planar = -0.51

fontXSmall = 15
fontSmall = 17
fontLarge = 24
figDimLarge = (10,8)
figDimSmall = (5,7)