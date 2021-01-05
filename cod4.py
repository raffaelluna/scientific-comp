# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:40:07 2018

@author: Usuário
"""

a = 0.1; b = 0.2
computed = a + b
expected = 0.3
diff = abs(computed - expected)
tol = 10e-17
correct = diff < tol

print('correct?', correct)