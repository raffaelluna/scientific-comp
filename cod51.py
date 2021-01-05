# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:33:22 2018

@author: Raffael
"""

class Complex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)