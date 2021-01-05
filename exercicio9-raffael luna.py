# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:51:05 2018

@author: Raffael
"""

class IntervalArit(object):
    def __init__(self, a, b=None):
        self.a = float(a)
        self.b = float(b)
        if b == None:
            self.b = self.a
        
    def __add__(self, other):
        return (IntervalArit(self.a + other.a, self.b + other.b))
    
    def __sub__(self, other):
        return (IntervalArit(self.a - other.b, self.b - other.a))
    
    def __rsub__(self, other):
        return IntervalArit(other - self.a, other - self.b)
    
    def __mul__(self, other):
        return (IntervalArit(min(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b), max(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b)))
    
    def __rmul__(self, other):
        return IntervalArit(other * self.a, other * self.b)
    
    def __neg__(self):
        return IntervalArit(-self.a, -self.b)
    
    def __div__(self, other):
        if other.a == 0 or other.b == 0:
            print 'erro: divisão por zero'
        else:
            return (IntervalArit(min(self.a / other.a, self.a / other.b, self.b / other.a, self.b / other.b), max(self.a / other.a, self.a / other.b, self.b / other.a, self.b / other.b)))
    
    def __pow__(self, other):
        if other > 0:
            power = self
            for i in range(abs(other-1)):
                power *= self
            return power
        else:
            power = IntervalArit(1,1)/self
            for i in range(abs(other)-1):
                power /= self
            return power
    
    def __str__(self):
        return '[%g, %g]' % (self.a, self.b)
    
    def __repr__(self):
        return 'Interval Math ' + str(self)
    
    def __float__(self):
        return (self.a + self.b)/2
    
a = IntervalArit(-3, -2)
b = IntervalArit(4, 5)
print 'a = %s' %(a)
print 'b = %s' %(b)
print 'a+b = %s'%(a+b)
print 'a-b = %s' %(a-b)
print 'a*b = %s' %(a*b)
print 'a/b = %s' %(a/b)
print '-'*20

v0 = IntervalArit(4,5)
t = 0.6
g = 9.81
print 'v0 = %s' %(v0)
print 't = %s' %(t)
print 'g = %s' %(g)
print 'v0*t - 0.5*g*t**2 = %s' %(-(0.5*g*t**2 - t*v0))
print '-'*20

y0 = IntervalArit(0.99, 1.01)
t = IntervalArit(0.44, 0.46)
print 'y0 = %s' %(y0)
print 't = %s' %(t)
print 'g = %s' %(2*y0*t**-2)
print 'mean g = %s' %(float(2*y0*t**-2))
print '-'*20

R = IntervalArit(5.4, 6.6)
print 'R = %s' %(R)
print 'V = %s' %((4./3)*pi*R**3)


       
        
        
        