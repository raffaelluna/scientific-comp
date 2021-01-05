# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:25:41 2018

@author: Raffael
"""

class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
        
    def value(self, t):
        return self.v0*t-0.5*self.g*t**2
    
y = Y(v0 = 3)
v = y.value(0.1)

print v