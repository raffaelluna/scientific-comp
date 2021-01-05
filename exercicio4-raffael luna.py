# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:13:33 2018

@author: Usuário
"""

from scitools.std import StringFunction
import sys
import math

funcao = StringFunction(sys.argv[1])
int_esq = float(sys.argv[2])
int_dir = float(sys.argv[3])
precisao = float(sys.argv[4])

def testa_intervalo():
    if funcao(int_esq)*funcao(int_dir)>=0:
        print('INTERVALO INVÁLIDO')
        sys.exit()

def bisec(func, int1, int2, prec):
    iterac = 0
    while abs(int1 - int2) > prec:
        m = (int1 + int2)/2.0
        if func(m)*func(int1) <= 0:
            int2 = m
        else:
            int1 = m
        iterac += 1
    return func(m), m, iterac

testa_intervalo()

resultado = bisec(funcao, int_esq, int_dir, precisao)

m = resultado[1]
iterac = resultado[2]
print('Found root x=%.9f in %i iteractions' % (m, iterac))


    
        
    
    
