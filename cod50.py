# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:05:07 2018

@author: Raffael
"""

class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)
    