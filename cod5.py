# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:50:32 2018

@author: Usuário
"""

from math import sinh, exp, e, pi

x = 2*pi
r1 = sinh(x)
r2 = 0.5*(exp(x)-exp(-x))
r3 = 0.5*(e**x-e**(-x))

print('%.16f %.16f %.16f' %(r1,r2,r3))d


