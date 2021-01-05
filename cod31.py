# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:43:13 2018

@author: Raffael
"""

import sys
import numpy as np

N = int(sys.argv[1])
x = np.zeros(N+1, np.longdouble)
x[0] = 1
x[1] = 1

for n in range(2, N+1):
    x[n] = x[n-1] + x[n-2]
    print n, x[n]