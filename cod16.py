# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:33:05 2018

@author: Usuário
"""

def diff2(f, x, h=1e-6):
    r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
    return r

def g(t):
    return t**(-6)

dgdt = diff2(lambda t: t**(-6),2)
print(dgdt)


for k in range(1,14):
    h = 10**(-k)
    print('h=%.0e: %.5f' % (h, diff2(g, 1, h)))