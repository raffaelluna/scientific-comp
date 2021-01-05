# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:20:34 2018

@author: Usuário
"""

from math import *

x = 0.5
y0 = 1
teta = 60
v0 = 15
g = 9.81

y = x*tan(teta*pi/180) - (1/(2*(v0/3.6)**2))*(g*x**2/(cos(teta*pi/180)*cos(teta*pi/180))) + y0

print('position y: %.2f' %(y) )

