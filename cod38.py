# -*- coding: utf-8 -*-
"""
Created on Wed May 09 16:47:10 2018

@author: Raffael
"""

import numpy as np
import sys

N = 10000
r = np.random.random_integers(1, 6, (2, N))

black = r[0,:]
green = r[1,:]
sucess = black > green
M = np.sum(sucess)

p = float(M)/N
print 'probability:', p