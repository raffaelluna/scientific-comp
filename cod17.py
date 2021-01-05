# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:50:45 2018

@author: Usuário
"""

from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    elif pi < x <= 2*pi:
        return 2
    else:
        return 0
    
print(f(0.5))
print(f(1.5*pi))
print(f(5*pi))