#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Uses Troch's method. Parabolic hillslope.s
Created on Wed Jan 24 21:26:19 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from parameters import *

def plotWaterTable(hilltype, curvature, Td):
    b = bmid
    ci = c
    if hilltype == 'div':
        ci = c; b = bmid - ci*(L/2)
    elif hilltype == 'con':
        ci = -c; b = bmid - ci*(L/2)
    elif hilltype == 'uni':
        ci = 0; b = bmid - ci*(L/2)
    else:
        raise ValueError('plotWaterTable parameter kwarg hilltype given wrong value')
    if curvature == 'convex':
        a = a_vex; B = B_vex
    elif curvature == 'concave':
        a = a_cave; B = B_cave
    else:
        raise ValueError('plotWaterTable parameter kwarg curvature given wrong value')
    x_crit = (B/(2*a))*(np.exp(-(2*a)*k*Tr) - 1)
    
    # Domain 1:
    ep = np.linspace(0,L,xRes/2)
    x1 = (ep + B/(2*a))*np.exp(-(2*a)*k*Tr) - B/(2*a)
    h1 = (N/(k*(B + (2*a)*x1)*(b + ci*x1)))*(b*(ep-x1) + 0.5*ci*(ep**2 - x1**2))
    
    # Domain 2:
    tau = np.linspace(Tr,0,xRes/2) # flip these around so they are same order as others
    x2 = (B/(2*a))*(np.exp((2*a)*k*(tau - Tr)) - 1)
    h2 = -N*(b*x2 + 0.5*ci*x2**2)/(k*(B + (2*a)*x2)*(b + ci*x2))
    
    # Domain 3:
    x_star = np.linspace(0,x_crit,xRes/2)
    x3 = (x_star + B/(2*a))*np.exp((2*a)*k*(Tr-(Tr+Td))) - B/(2*a)
    h3 = (1/((B + (2*a)*x3)*(b + ci*x3)))*(
            (Nd/k)*(b*(x_star - x3) + 0.5*ci*(x_star**2 - x3**2)) +
            h2*(B + (2*a)*x_star)*(b + ci*x_star))
    
    # Domain 4:
    x_prime = np.linspace(x_crit,L,xRes/2)
    x4 = (x_prime + B/(2*a))*np.exp((2*a)*k*(Tr-(Tr+Td))) - B/(2*a)
    h4 = (1/((B+(2*a)*x4)*(b+ci*x4)))*(
            (Nd/k)*(b*(x_prime - x4) + 0.5*ci*(x_prime**2 - x4**2)) + 
            h1*(B + (2*a)*x_prime)*(b + ci*x_prime))
    
    xinit = np.concatenate([x2,x1])
    hinit = np.concatenate([h2,h1])
    xdrain = np.concatenate([x3,x4])
    hdrain = np.concatenate([h3,h4])
    
    zeros = [0,xRes,0]
    cntr = 0
    # if all values are less than 0, don't look for zeros!
    if np.sum(np.sign(hdrain)) == -len(hdrain):
        zeros = [0,0]
    else:
        #find first x-intercept (moving in from left)
        for i in range(0,xRes-2):
            if np.sign(hdrain[i]) !=  np.sign(hdrain[i+1]):
                zeros[cntr] = np.interp(0,[hdrain[i], hdrain[i+1]],
                                    [xdrain[i], xdrain[i+1]])
                cntr +=1

    
    return xdrain, hdrain, zeros[0], zeros[1]