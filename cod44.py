# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:18:06 2018

@author: Raffael
"""

temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}

print 'The temperature in London is', temps['London']
print 'The temperature in Oslo is', temps['Oslo']

temps['Madrid'] = 26.

for city in sorted(temps):
    print 'The %s temperature is %g' %(city, temps[city])
