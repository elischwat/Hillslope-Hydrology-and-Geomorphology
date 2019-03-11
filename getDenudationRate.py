#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:42:20 2018

@author: elischwat
"""
import numpy as np
from parameters import *

# Returns Denudation rate in Meters per Second (m/s)
def getDenudationRate(As, Ds, dz, M, ralb, rho, R_dis):
    return dz*ralb*As*R_dis*M/(Ds**3*rho)
