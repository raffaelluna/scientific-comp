# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:04:31 2018

@author: Usuário
"""

from sympy import *

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y,t)

print('velocity:', dydt)
print('acelleration:', diff(dydt,t))
print('position:', integrate(dydt,t))

roots = solve(y,t)
print(roots)

x, y = symbols('x y')
f = -sin(x)*sin(y) + cos(x)*cos(y)
print(simplify(f))