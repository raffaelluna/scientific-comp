# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:59:31 2018

@author: Usuário
"""

def double(x):
    return 2*x

def test_double():
    x = 4
    expected = 8
    computed = double(x)
    sucess = expected == computed
    msg = 'computed %s, expected %s' % (computed, expected)
    assert sucess, msg
    
test_double()