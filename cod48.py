# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:30:38 2018

@author: Raffael
"""

class SelfExplorer:
    def __init__(self, a):
        self.a = a
        print 'init: a=%g, id(self)=%d' %(self.a, id(self))
    def value(self, x):
        print 'value: a=%g, id(self)=%d' % (self.a, id(self))
        return self.a*x