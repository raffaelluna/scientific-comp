# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:46:48 2018

@author: Usuário
"""

degrees = [0, 10, 20, 40, 100]
for C in degrees:
    F = 9.0/5*C + 32
    print('%d %5.1f' % (C,F))
print('_'*10)

index = 0
while index < len(degrees):
    C = degrees[index]
    F = 9.0/5*C + 32
    print(C,F)
    index +=1
    
