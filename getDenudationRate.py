#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:42:20 2018

@author: elischwat
"""
import numpy as np
from parameters import *

# Returns in meters per second
def getDenudationRate():
    return dz*ralb*As*R_dis*M/(Ds**3*rho)
