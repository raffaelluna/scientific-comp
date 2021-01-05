# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:35:49 2018

@author: Raffael
"""

from scitools.std import *
from matplotlib.pylab import show

x0 = 100
p = 5
r = p/360.0

import datetime 

date1 = datetime.date(2007, 8, 3)
date2 = datetime.date(2011, 8, 3)
diff = date2 - date1
N = diff.days

index_set = range(N+1)

x = zeros(len(index_set))

x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (r/100.0)*x[n-1]
print x
plot(index_set, x, 'ro', xlabel='days', ylabel='amount')
