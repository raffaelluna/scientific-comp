# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:00:30 2018

@author: Usuário
"""

def F(C):
    return (9.0/5*C + 32)

print(F(10))

Fdegrees = [F(C) for C in [0, 20, 40]]
print(Fdegrees)