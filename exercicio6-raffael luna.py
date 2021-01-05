# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:25:05 2018

@author: Raffael
"""
from scitools.std import linspace, zeros, plot
import numpy as np
import matplotlib.pyplot as plt


N = linspace(1,100,100)

soma1_vetor = zeros(len(N))
soma3_vetor = zeros(len(N))
vetor_erro = zeros(len(N))

for n in range(1,len(N)+1):
    soma_1 = 0
    soma_3 = 0
    for n1 in range(1,2*n+1):
        n1 = float(n1)
        soma_1 += ((-1)**n1)*(n1/(n1+1))

    soma1_vetor[n-1] = soma_1
    
    for n3 in range(1,n+1):
        n3 = float(n3)
        soma_3 += 1./(2*n3*(2*n3+1))
    
    soma3_vetor[n-1] = soma_3
            
vetor_erro = np.abs((soma1_vetor-soma3_vetor)/soma3_vetor)   

vetor_erro[1] = 2.5e-16        
vetor_erro_log = np.log10(vetor_erro)
eixo_x = np.log10(N)
plt.plot(eixo_x,vetor_erro_log)