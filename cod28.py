# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:30:18 2018

@author: Raffael
"""

from scitools.std import plot
import matplotlib.pyplab import show

def H(x):
    return (0 if x<0 else 1)

x = linspace(-10, 10, 5)
y = H(x)
