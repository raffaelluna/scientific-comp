# -*- coding: utf-8 -*-
"""
Created on Wed May 09 16:27:12 2018

@author: Raffael
"""

import numpy as np

N = 10000
eyes = np.random.randint(1,7,N)
sucess = eyes == 6
six = np.sum(sucess)

print 'No of six %d' % six
print 'Probability: %.4f' %(float(six)/N)