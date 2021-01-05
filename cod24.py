# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:48:02 2018

@author: Usuário
"""

import sys

def read_C():
    try:
        C = float(sys.argv[1])
    except IndexError:
            print('value not provided')
            sys.exit(1)
    except ValueError:
            print('Only number')
            sys.exit(1)

    if C < -273.15:
        raise ValueError('não físico')
    return C

try:
    C = read_C()
except (IndexError, ValueError) as e:
    print(e)
    sys.exit(1)
    
F = (9./5)*C + 32
print(F)