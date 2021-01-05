# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:11:12 2018

@author: Raffael
"""


from matplotlib.pyplot import *
from numpy import *

def f1(t):
    return t*2*exp(-t**2)

def f2(t):
    return t**2*f1(t)

t = linspace(0,3,100)
y1 = f1(t)
y2 = f2(t)

plot(t,y1) 
hold('on')
plot(t,y2)

show()
