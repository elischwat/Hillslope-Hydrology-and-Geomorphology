#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:48:43 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from getErosionProfile import *


# Set up initial conditions
zBottom = 0
zTop = -L*B - L**2*a
initX = np.linspace(0,L,xRes)
# Parabola initial condition:
initZ = zTop + B*initX + a*initX**2
# River terrace (angular) initial condition:
#initZ = np.concatenate([np.full(xRes/4, 20), np.linspace(20,0,xRes/2),
#                        np.full(xRes/4, 0)])

def geomorphModel_chem(hilltype, curvature, init, T_):
    init = np.append([init[1]], init) # prepare init for Neumann boundary condition
    b0 = 0; ci = 0
    if hilltype == 'div':
        ci = c; b0 = bmid - ci*(L/2)
    elif hilltype == 'con':
        ci = -c; b0 = bmid - ci*(L/2)
    elif hilltype == 'uni':
        ci = 0; b0 = bmid - ci*(L/2)
    # get Ec for uniform for curvature for all three hillslopes B.C.s
    Ec = -getErosionProfile('uni', curvature) 
    print('Chemical Denudation at x = L (using uniform info): ' + str(Ec[-1]) + ' m/yr')
    x = np.linspace(-1,L,xRes+1) # extra value for Neumann boundary  #101
    b = b0 + c*x # initialize array of b values                      #101
    newZ = init # extra value for Neumann boundary       #101
    massLostByDiffusion = 0
    for step in range(0,int(T_/dtGeo)):
        diffTerm1 = 0.5*(b[2:] + b[1:-1])*(1/dx)*(init[2:] - init[1:-1])
        diffTerm2 = 0.5*(b[1:-1] + b[:-2])*(1/dx)*(init[1:-1] - init[:-2])
        Diff = (D/(b[1:-1]*dx))*(diffTerm1 - diffTerm2)
        newZ[1:-1] = init[1:-1] + dtGeo*Diff
    #Boundary condition at x = 0 (Neumann Condition):
        newZ[0] = newZ[2] # Nuemann
#        newZ[0] = newZ[0] # fixed
    #Boundary condition at x = L :
        newZ[-1] = newZ[-1] + dtGeo*Ec[-1] # move with Ec
#        newZ[-1] = newZ[-1] # fixed
        #estimate slope at x = L
        S = (newZ[-1] - newZ[-2])/dx
        massLostByDiffusion += S*D*b[-1]*soilDensity*dtGeo
        init = newZ
    print('Total Area Lost By Diffusion:' + str(massLostByDiffusion))
    return newZ[1:]

## PRETTIFY:
def prettify():
    plt.legend(frameon=False, fontsize=fontXSmall)
    plt.xticks([0,100],[0,100], fontsize=fontSmall)
    plt.yticks([0,50], [0,50], fontsize=fontSmall)
    plt.ylim(-12,52)
    plt.xlim(-1,101)
    plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)
#    plt.ylabel('Land Surface Elevation (m)', fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_aspect('equal')    


plt.figure(figsize=figDimLarge)
plt.plot(initX,initZ, color = 'k', label='Initial')

con_morph = geomorphModel_chem('con', curvature, initZ, T)
plt.plot(initX, con_morph, label='Convergent', color='tab:orange', linestyle='--')
div_morph = geomorphModel_chem('div', curvature, initZ, T)
plt.plot(initX, div_morph, label='Divergent', color='tab:orange', linestyle = ':')
#uni_morph = geomorphModel_chem('uni', curvature, initZ, T)    
#plt.plot(initX, uni_morph, label='Uniform',
#                 color='tab:gray')    

prettify()
#plt.title('Hillslope Surface Elevation Eroding ' + str(T) + ' Years', fontsize=fontSmall)
plt.tight_layout()
plt.savefig('hillslope_eroding_10000_years.png', bbox_inches='tight')
plt.show()
