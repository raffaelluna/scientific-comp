# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:12:56 2018

@author: Usuário
"""
n = 40
Cdegrees = []
Fdegrees = []

Cdegrees = [-5 + i*5 for i in range(n)]
Fdegrees = [9.0/5*C + 32 for C in Cdegrees]


table = [[C, F] for C, F  in zip(Cdegrees, Fdegrees)]
#print(table)

for C, F in table[Cdegrees.index(10):Cdegrees.index(35)]:
    print('%5.0f %5.1f' % (C, F))