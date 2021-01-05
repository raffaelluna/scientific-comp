# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:20:19 2018

@author: Raffael
"""
from scitools.std import sqrt, pi, exp, linspace, plot, movie
import time, glob, os, sys
from matplotlib.pylab import show

for name in glob.glob('tmp_*.jpg'):
    os.remove(name)

def f(x, m, s):
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

m = 0
s_max = 2
s_min = 0.2
x = linspace(m-3*s_max, m+3*s_max, 1000)
s_values = linspace(s_max, s_min, 30)

max_f = f(m,m,s_min)

counter = 0
for s in s_values:
    y = f(x, m, s)
    plot(x,y,'-r',axis=[x[0],x[-1], -0.1, max_f],xlabel='x',ylabel='f', legend='s=%4.2f' % s,savefig='tmp_%04d.jpg' % counter)
    show()
    counter += 1

cmd = 'convert -delay 20 tmp_*.jpg movie1.gif'
os.system(cmd)

for name in glob.glob('tmp_*.jpg'):
    os.remove(name) 
