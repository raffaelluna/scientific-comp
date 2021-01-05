# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:01:05 2018

@author: Usuário
"""

from math import pi, sin, exp

def f(t, A=1, a=1, omega = 2*pi):    
    return A*exp(-a*t)*sin(omega*t)

print(f(A=9, t=0.2))