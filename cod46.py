# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:45:41 2018

@author: Raffael
"""

infile = open('data.dat', 'r')
lines = infile.readlines()
infile.close()

data = {}
first_line = lines[0]
properties = first_line.split()

for p in properties:
    data[p] = {}

for line in lines[1:]:
    words = line.split()
    i = int(words[0])
    values = words[1:]
    for p, v in zip(properties, values):
        if v != 'no':
            data[p][i] = float(v)
            
for p in data:
    values = data[p].values()
    data[p]['mean'] = sum(values)/len(values)
    
for p in sorted(data):
    print 'Mean values of property %s = %g' %(p, data[p]['mean'])
    
import scitools.pprint2
scitools.pprint2.pprint(data)