# -*- coding: utf-8 -*-
"""
Created on Wed May 09 16:47:38 2018

@author: Raffael
"""

combinations = [(black, green)
                for black in range(1,7)
                for green in range(1,7)]
sucess = [black < green for black, green in combinations]
M = sum(sucess)
print 'Probability:', float(M)/len(combinations) 