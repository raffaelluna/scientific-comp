# -*- coding: utf-8 -*-
"""
Created on Wed May 02 17:22:32 2018

@author: Raffael
"""
import numpy as np
import matplotlib.pyplot as plt
import random

def mcl(a, c, M, r1):
    vetor_r = np.zeros(500)
    vetor_r[0] = r1
    
    for k in range(1, len(vetor_r)):
        vetor_r[k] = (a*vetor_r[k-1]+c) % M
    
    return vetor_r

vetor_r = mcl(57, 1, 256, 10)

for k in range(len(vetor_r)-1):
    plt.scatter(vetor_r[k], vetor_r[k+1])

seed = vetor_r[0]
counter = 1

while vetor_r[counter] != seed:
        counter += 1
        
        
vetor_r1 = np.zeros(10000)
for k in range(len(vetor_r1)):
    vetor_r1[k] = random.random()
    
#for k in range(len(vetor_r1)-1):
#    plt.scatter(vetor_r1[k], vetor_r1[k+1])
 
soma = 0    
for k in range(len(vetor_r1)):
    soma += vetor_r1[k]**7

soma = soma/10000

a = np.abs(soma - 0.125)
    
    