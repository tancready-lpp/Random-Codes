#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:42:35 2025

@author: tancredi
"""

# Compute the height of a cliff from the time it takes the sound of a stone dropped to reach your ear.

from math import sqrt

g = 9.81 # m/s^2 gravity
vs = 340. # m/s sound speed
T = 17. # s measuered time (fall + sound)

h = (vs/g)*(vs+g*T-sqrt(vs**2.+2.*g*vs*T))

print(f"The canyon is {h:.2f}m in standard condidions")