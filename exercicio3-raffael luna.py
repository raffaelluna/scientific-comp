# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 18:12:42 2018

@author: Usuário
"""

from math import sin, pi, cos, tan

def Simpson(f, a, b, n=500):
    a = float(a)
    b = float(b)
    h = (b - a)/n
    soma1 = 0
    soma2 = 0
    for i in range(1,int(n/2)+1):
        soma1 += f(a + (2*i-1)*h)
    for k in range(1,int(n/2)):
        soma2 += f(a + 2*k*h)
    return ((b - a)/(3*n))*(f(a) + f(b) + 4*soma1 + 2*soma2)
    
def g(x):
    return (3.0/2)*sin(x)**3

def table(x):
    print('Integral of 1.5*sin^3 from 0 to pi:')
    for n in [2, 6, 12, 100, 500]:
        integral = Simpson(x, 0, pi, n)
        error = 2 - integral
        print('n=%4d, approx= %.15f, error= %8.2e' % (n, integral, error))
    
table(g)

def test_integral():
    g = lambda x: x
    expected = 50
    computed = Simpson(g,0,10)
    epsilon = abs(computed - expected)
    sucess =  epsilon < 1e-6
    msg = 'computed %s, expected %s' % (computed, expected)
    assert sucess, msg
    
test_integral()

    