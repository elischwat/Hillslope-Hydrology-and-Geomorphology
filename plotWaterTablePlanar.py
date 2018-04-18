#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Uses Troch's method. Planar Hillslope.
Created on Tue Jan 30 22:01:29 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from parameters import *

def plotWaterTablePlanar(hilltype, Td):
    B = B_planar
    b = bmid
    ci = c
    if hilltype == 'div':
        ci = c; b = bmid - ci*(L/2)
    elif hilltype == 'con':
        ci = -c; b = bmid - ci*(L/2)
    elif hilltype == 'uni':
        ci = 0; b = bmid - ci*(L/2)
            
    x_crit = - k*B*Tr
    
    # Domain 1:
    ep = np.linspace(0,L,xRes/2)
    x1 = ep - k*B*Tr
    h1 = (N/(k*B*(b + ci*x1)))*(b*(ep-x1) + 0.5*ci*(ep**2 - x1**2))
    
    # Domain 2:
    tau = np.linspace(Tr,0,xRes/2) # flip these around so they are same order as others
    x2 = k*B*(tau-Tr)
    h2 = -N*(b*x2 + 0.5*ci*x2**2)/(k*B*(b + ci*x2))
    
    # Domain 3:
    x_star = np.linspace(0,x_crit,xRes/2)
    x3 = k*B*(Tr-(Tr+Td)) + x_star
    h3 = Nd*(b*(x_star - x3) + 0.5*ci*(x_star**2 - x3**2))/(B*k*(b+ci*x3)) + h2*(b + ci*x_star)/(b + ci*x3)
    
    # Domain 4:
    x_prime = np.linspace(x_crit,L,xRes/2)
    x4 = k*B*(Tr-(Tr+Td)) + x_prime
    h4 = Nd*(b*(x_prime - x4) + 0.5*ci*(x_prime**2 - x4**2))/(B*k*(b+ci*x4)) + h1*(b + ci*x_prime)/(b + ci*x4)
#    9
    xinit = np.concatenate([x2,x1])
    hinit = np.concatenate([h2,h1])
    xdrain = np.concatenate([x3,x4])
    hdrain = np.concatenate([h3,h4])    
    
    zeros = [0,xRes]
    cntr = 0
    # if all values are less than 0, don't look for zeros!
    if np.sum(np.sign(hdrain)) == -len(hdrain):
        zeros = [0,0]
    else:
        #find first x-intercept (moving in from left)
        for i in range(0,xRes-1):
            if np.sign(hdrain[i]) !=  np.sign(hdrain[i+1]):
                zeros[cntr] = np.interp(0,[hdrain[i], hdrain[i+1]],[xdrain[i], xdrain[i+1]])
                cntr +=1

    
    return xdrain, hdrain, zeros[0], zeros[1]