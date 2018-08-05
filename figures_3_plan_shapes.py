#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:28:19 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from parameters import *
plt.figure(figsize=figDimSmall)

x = np.linspace(0,L,xRes)

#CONVERGENT
plt.subplot(3,1,1)
c = -0.2
bL = bmid + c*L/2
b0 = bmid - c*L/2
w1 = 0.5*(bL - b0) - (c/2)*x + 10
w2 = (0.5*(bL - b0)+b0) + (c/2)*x + 10
plt.plot(x,w1, color='k')
plt.plot(x,w2, color='k')
plt.annotate('Convergent', xy=(0,14), fontsize=fontSmall)
plt.xticks([])

#UNIFORM
plt.subplot(3,1,2)
w1 = np.full(xRes, 5)
w2 = np.full(xRes, 25)
plt.plot(x,w1, color='k')
plt.plot(x,w2, color='k')
plt.annotate('Uniform', xy=(0,14), fontsize=fontSmall)
plt.ylabel('Distance along Stream Channel (m)', fontsize=fontSmall)
plt.xticks([])

#DIVERGENT
plt.subplot(3,1,3)
c = 0.2
bL = bmid + c*L/2
b0 = bmid - c*L/2
w1 = 0.5*(bL - b0) - (c/2)*x
w2 = (0.5*(bL - b0)+b0) + (c/2)*x
plt.plot(x,w1, color='k')
plt.plot(x,w2, color='k')
plt.annotate('Divergent', xy=(0,14), fontsize=fontSmall)
plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)
plt.xticks([0,50,100],[0,50,100],fontsize=fontSmall)
    
for i in range(1,4):
    plt.subplot(3,1,i)
    plt.ylim(-5,35)
    plt.xlim(-2,L+2)
    plt.yticks([-5,5,15,25,35],[])
    plt.xticks(fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

#plt.suptitle('Contour Width Functions for Three Hillslope Plan Shapes',
#             fontsize=fontSmall)
#plt.savefig('images/3_plan_shapes.jpeg')
plt.show()

