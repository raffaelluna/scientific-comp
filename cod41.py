# -*- coding: utf-8 -*-
"""
Created on Wed May 09 17:00:22 2018

@author: Raffael
"""

import random
import numpy as np

def MCint_area(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    below = np.sum(y < f(x))
    area = (below/float(n))*m*(b - a)
    return area

def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 100000000; fmax = f1(b)
I = MCint_area(f1, a, b, n, fmax)
print I