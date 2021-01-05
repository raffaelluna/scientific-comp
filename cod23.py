# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:41:55 2018

@author: Usuário
"""

data = [[11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]]

outfile = open('tmp_lab.dat','w')

for row in data:
    for column in row:
        outfile.write('%10.2f' % (column))
    outfile.write('\n')
    
outfile.close()