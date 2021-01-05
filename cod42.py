# -*- coding: utf-8 -*-
"""
Created on Wed May 09 17:26:59 2018

@author: Raffael
"""

import os, glob
import random, numpy
from scitools.std import plot

np = 4
ns = 20

positions = numpy.zeros(np)
y = numpy.zeros(np)
HEAD = 1; TAIL = 2

xmin = -3*numpy.sqrt(ns)
xmax = 3*numpy.sqrt(ns)

for step in range(ns):
    for p in range(np):
        coin = random.randint(1,2)
        if coin == HEAD:
            positions[p] += 1
        elif coin == TAIL:
            positions[p] -= 1
    plot(positions, y, '7', 
         axis=[xmin, xmax, -0.2, 0.2],
         title='%d particles after %d steps' %(np, step+1),
         savefig='tmp_%03d.jpg' %(step+1))
    
os.system('convert -delay 20 tmp_*.jpg movie9.gif')
for name in glob.glob('tmp_*.jpg'):
    os.remove(name)