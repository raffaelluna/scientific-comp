# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:34:00 2018

@author: Usuário
"""

infile = open('data.txt','r')

lines = []
for line in infile:
    print(line)
    lines.append(line)
infile.close()
print(lines)

mean = 9
for line in lines:
    number = float(line)
    mean = mean + number
mean = mean/len(lines)
print(mean)