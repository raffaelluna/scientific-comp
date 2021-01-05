# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:37:50 2018

@author: Usuário
"""

def L(x,n):
    x = float(x)
    s = 0
    for i in range(1,n+1):
        s += (1.0/i)*(x/(1+x))**i
        
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1+x))**(n+1)
    
    from math import log
    
    exact_error = log(1+x) - value_of_sum
    
    return value_of_sum, first_neglected_term, exact_error

def table(x):
    from math import log
    print('\nx=%g, ln(1+x)=%g' % (x, log(1+x)))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L(x,n)
        print('n=%-d %-g (next term %8.2e) error %8.2e' % (n, value, next, error))
    
table(10)