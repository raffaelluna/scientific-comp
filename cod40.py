# -*- coding: utf-8 -*-
"""
Created on Wed May 09 16:51:47 2018

@author: Raffael
"""

import numpy as np

r = np.random.random_integers(1, 6, size=(2,N))

money = 10 - N
black = r[0,:]
green = r[1,:]
sucess = black > green
M = np.sum(sucess)
money += 2*M

print 'Net profit per game in the long run', (money - 10)/float(N)