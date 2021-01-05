# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 21:54:44 2018

@author: Raffael
"""

import numpy as np
import matplotlib.pyplot as plt

def rw2d(num_steps):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    
    r = np.zeros(num_steps)
    for i in range(num_steps):
        if i == 0:
            x[i] = 0
            y[i] = 0
        else:
            dx = (np.random.random_sample() - .5)*2
            dy = (np.random.random_sample() - .5)*2   
            
            dx /= np.sqrt(dx**2 + dy**2)
            dy /= np.sqrt(dx**2 + dy**2)
            
            x[i] = x[i-1] - dx
            y[i] = y[i-1] - dy
            
            r[i] = np.sqrt(x[i]**2 + y[i]**2)
    return x, y, r

num_steps = 10000
pts = int(np.sqrt(num_steps))
r = [[0 for x in range(num_steps)] for y in range(pts)]

for plots in range(5):
    for i in range(pts):
#        np.random.seed(i+17)
        x, y, r[i][:] = rw2d(num_steps)
    
    sum = np.zeros(num_steps)    
    for step in range(num_steps):
        for pt in range(pts):
            sum[step] += r[pt][step]
            
    sum /= pts
    eixoy = np.sqrt(range(1,num_steps+1))
    plt.figure(1)
    plt.plot(x,y)
    plt.figure(2)
    plt.plot(sum,eixoy)
    print sum[num_steps-1]

plt.savefig('projfig1.jpg')