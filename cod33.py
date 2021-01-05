    # -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:12:01 2018

@author: Raffael
"""

from scitools.std import *
from matplotlib.pylab import show

x0 = 100
M = 500
rho = 4
N = 200
index_set = range(N+1)
x = zeros(len(index_set))

x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (rho/100.9)*x[n-1]*(1 - x[n-1]/float(M))
print x
plot(index_set, x, 'r', xlabel='time units', ylabel='no of individuals', hardcopy='tmp.pdf')