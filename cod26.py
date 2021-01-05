# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:10:18 2018

@author: Raffael
"""

from numpy import *
from matplotlib.pyplot import *

formula = sys.argv[1]
xmin = eval(sys.argv[2])
xmax = eval(sys.argv[3])

x = linspace(xmin, xmax, 101)
y = eval(formula)

plot(x,y)
title(formula)
show()