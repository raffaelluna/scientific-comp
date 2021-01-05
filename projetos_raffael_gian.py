# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:27:21 2018

@author: Raffael
"""
# Importa os pacotes
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def j_up(l, x):
    matriz_jup = np.zeros((l+1,len(x)))
    
    matriz_jup[0] = np.sin(x)/x
    matriz_jup[1] = np.sin(x)/x**2 - np.cos(x)/x

    for n in range(1,l):
        n = int(n)
        matriz_jup[n+1] = ((2.*n+1.)/x)*matriz_jup[n] - matriz_jup[n-1]
    return matriz_jup

def j_down(l, x):
    matriz_jdown = np.zeros((l+1,len(x)))
    
    matriz_jdown[l] = 1
    matriz_jdown[l-1] = 1

    for k in range(l-1,-1,-1):
        k = int(k)
        matriz_jdown[k-1] = ((2.*k+1.)/x)*matriz_jdown[k] - matriz_jdown[k+1]
        
    matriz_jdown = matriz_jdown*(np.sin(x)/x)/matriz_jdown[0]
    return matriz_jdown

def j_ref(l, x):
    matriz_ref = np.zeros((l+1,len(x)))
    
    for i in range(l+1):
        matriz_ref[i] = special.spherical_jn(i,x)
    return matriz_ref

l = 50
x = np.linspace(0, 10, num=1001)


matriz_jup = j_up(l, x)
matriz_ref = j_ref(l, x)
matriz_jdown = j_down(l, x)

for k in range(l+1):
    matriz_jup[k][0] = matriz_ref[k][0]
    matriz_jdown[k][0] = matriz_ref[k][0]

#for i in range(5):
#    plt.plot(x,matriz_ref[i], label='l=%d' %i)
#    
#plt.axis([0, 10, -0.25, 1.])
#plt.grid()
#plt.legend()
#plt.title('Bessel Functions')
#plt.savefig('bessel.pdf')    


valores_up = np.zeros((3,l+1))
valores_down = np.zeros((3,l+1))
valores_ref = np.zeros((3,l+1))
x_erro = np.zeros(l+1)

for n in range(l+1):
    for k in range(3):
        valores_up[k][n] = matriz_jup[n][10**(k+1)]
        valores_down[k][n] = matriz_jdown[n][10**(k+1)]
        valores_ref[k][n] = matriz_ref[n][10**(k+1)]

    x_erro[n] = n

erro01up = np.log10(np.abs(valores_up[0] - valores_ref[0]))
erro1up = np.log10(np.abs(valores_up[1] - valores_ref[1]))
erro10up = np.log10(np.abs(valores_up[2] - valores_ref[2]))

erro01down = np.log10(np.abs((valores_down[0] - valores_ref[0])))
erro1down = np.log10(np.abs((valores_down[1] - valores_ref[1])))
erro10down = np.log10(np.abs((valores_down[2] - valores_ref[2])))

erro01rel = np.abs(valores_up[0] - valores_down[0])/(np.abs(valores_up[0])+ \
                   np.abs(valores_down[0]))
erro1rel = np.abs(valores_up[1] - valores_down[1])/(np.abs(valores_up[1])+ \
                  np.abs(valores_down[1]))
erro10rel = np.abs(valores_up[2] - valores_down[2])/(np.abs(valores_up[2])+ \
                   np.abs(valores_down[2]))

plt.plot(x_erro, erro01down, 'black', label='x = 0.1')
plt.plot(x_erro, erro1down, 'r--', label='x = 1')
plt.plot(x_erro, erro10down,'b', label='x = 10')
plt.legend()
plt.title('Down Method Error')
plt.xlabel('Order of Bessel Function')
plt.ylabel('Down Error')
plt.axis([0, 25,-80, 50])
plt.grid()
plt.savefig('errodown.pdf')