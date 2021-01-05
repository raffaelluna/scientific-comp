# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:02:04 2018

@author: Raffael
"""

import sys

N = int(sys.argv[1])
xnm1 = 1
xnm2 = 1
n = 2

while n<=N:
    xn = xnm1 + xnm2
    print 'x_%d = %d' %(n,xn)
    xnm2 = xnm1
    xnm1 = xn
    n += 1