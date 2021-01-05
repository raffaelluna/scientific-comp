# -*- coding: utf-8 -*-
"""
Created on Wed May 09 18:03:33 2018

@author: Raffael
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def x1(x, p, M, m, x0, p0, N):
    x[0] = x0
    p[0] = p0

    for i in range(1,(len(x))):   
        x[i] = x[i-1] + (p[i-1]/1200.)*x[i-1]
        
        r1 = np.random.randint(1,M+1)
        r2 = np.random.randint(1,3)
        
        if r1 == 1 and r2 == 1:
            p[i] = p[i-1] + m
            
        if r1 == 1 and r2 == 2:
            p[i] = p[i-1] - m
            
        elif r1 != 1:
            p[i] = p[i-1]
    return x, p

x0 = 1
p0 = 5
N = 10*12
M = 3
n = 1000
m = 0.5
x = np.zeros(N)
p = np.zeros(N)
num_sim = 0
num_sim1 = 0

eixox = np.array(range(N))

plt.figure(1)
while num_sim < 10:
    x1(x, p, M, m, x0, p0, N)
    plt.subplot(121)
    plt.plot(eixox, x)
    plt.title('sample paths of investment')
    plt.subplot(122)
    plt.plot(eixox, p)
    plt.title('sample paths of interest rate')
    num_sim += 1
   
matriz_x = np.zeros((n,N))
matriz_p = np.zeros((n,N))
for i in range(n):
    matriz_x[i,:], matriz_p[i,:] = x1(x, p, M, m, x0, p0, N)

mean_x = np.zeros(N)
mean_p = np.zeros(N)
for k in range(N):   
    for i in range(n):
        mean_x[k] += matriz_x[i,k]
        mean_p[k] += matriz_p[i,k]
        
mean_x = mean_x/1000.
mean_p = mean_p/1000.

std_x = np.zeros(N)
std_p = np.zeros(N)
for i in range(N):      
    std_x[i] = np.std(matriz_x[:,i])
    std_p[i] = np.std(matriz_p[:,i])

#std_x = np.sqrt(std_x/1000.)
#std_p = np.sqrt(std_p/1000.)
plt.figure(2)
plt.subplot(121)
plt.plot(eixox, mean_x)
plt.plot(eixox, mean_x - std_x)
plt.plot(eixox, mean_x + std_x)
plt.title('Mean +/- 1 st.dev. of investment')

plt.subplot(122)
plt.plot(eixox, mean_p)
plt.plot(eixox, mean_p - std_p)
plt.plot(eixox, mean_p + std_p)
plt.title('Mean +/- 1 st.dev. of annual interest rate')
plt.show()

