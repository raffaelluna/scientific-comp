# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:58:32 2018

@author: Usuário
"""
n = 4
Cdegrees = []
Fdegrees = []

#for i in range(n):
#    Cdegrees.append(-5 + i*0.5)
#    Fdegrees.append(9.0/5*Cdegrees[i]+32)
#    print(Cdegrees)
#    print(Fdegrees)
 
Cdegrees = [-5 + i*0.5 for i in range(n)]
Fdegrees = [9.0/5*C + 32 for C in Cdegrees]

for i in range(len(Cdegrees)):
    print(Cdegrees[i],Fdegrees[i])
   
print(Cdegrees)
print(Fdegrees)


print('_'*10)