# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:37:01 2018

@author: Raffael
"""

def eval_poly_dict(poly, x):
    sum = 0.
    for power in poly:
        sum += poly[power]*x**power
    return sum

def eval_poly_dict2(poly, x):
    return sum(poly[power]*x**power for power in poly)

p = {0: -1, 2: 1., 7: 3.5}
patx = eval_poly_dict(p, 2.1)
patx2 = eval_poly_dict2(p, 2.1)

print patx
print patx2