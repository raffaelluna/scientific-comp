# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:54:25 2018

@author: Raffael
"""

Cdegrees = [-30 + i*10 for i in range(3)]
Fdegrees = [9./5 * C + 32 for C in Cdegrees]

table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]

print table

from numpy import array
table2 = array(table)
print table2