# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:19:47 2018

@author: Usuário
"""

def yfunc(t, v0):
    g =  9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

y = yfunc(0.1, 9)
print(y)

y = yfunc(v0=9, t=0.1)
print(y)

v0 = 5
t = 0.6
y = yfunc(t, 3)
print(y)
print(v0)

position, velocity = yfunc(0.6, 3)
print(position)
print(velocity)