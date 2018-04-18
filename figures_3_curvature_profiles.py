#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:07:15 2018

@author: elischwat
"""
import numpy as np
import matplotlib.pyplot as plt
from parameters import *
plt.figure(figsize=figDimSmall)

x = np.linspace(0,L,xRes)

#Convex
plt.subplot(3,1,1)
plt.plot(x, 50 + B_vex*x + a_vex*x**2, color = 'k')
plt.annotate('Convex', xy=(0,0), horizontalalignment='left', 
             verticalalignment='bottom', fontsize=fontSmall)
plt.xticks([])

#Planar
plt.subplot(3,1,2)
plt.plot(x, 50 + B_planar*x, color = 'k')
plt.annotate('Planar', xy=(0,0), horizontalalignment='left', 
             verticalalignment='bottom', fontsize=fontSmall)
plt.xticks([])
plt.ylabel('Land Surface Elevation (m)', fontsize=fontSmall)

#Concave
plt.subplot(3,1,3)
plt.plot(x,50 + B_cave*x + a_cave*x**2, color='k')
plt.annotate('Concave', xy=(0,0), horizontalalignment='left', 
             verticalalignment='bottom', fontsize=fontSmall)
plt.xticks([0,50,100],[0,50,100])
plt.xlabel('Distance from Ridge (m)', fontsize=fontSmall)
    
for i in range(1,4):
    plt.subplot(3,1,i)
#    plt.ylim(-5,35)
    plt.xlim(-2,L+2)
    plt.yticks([0,25,50],[0,25,50], fontsize=fontSmall)
    plt.xticks(fontsize=fontSmall)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

#plt.suptitle('Contour Width Functions for Three Hillslope Plan Shapes',
#             fontsize=fontSmall)
plt.savefig('images/3_curvature_profiles.jpeg')
#plt.tight_layout()
plt.show()


