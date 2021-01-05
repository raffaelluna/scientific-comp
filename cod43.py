# -*- coding: utf-8 -*-
"""
Created on Wed May 09 17:49:02 2018

@author: Raffael
"""
import os, glob, sys
import random, numpy
from scitools.std import plot

def random_walk_2D(np, ns, plot_step):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    moves = numpy.random.random_integers(1, 4, size=ns*np)
    moves.shape = (ns, np)
    
    xymax = 3*numpy.sqrt(ns)
    xymin = -xymax
    
    NORTH = 1; SOUTH = 2; WEST = 3; EAST = 4
    
    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == NORTH, 1, 0)
        ypositions -= numpy.where(this_move == SOUTH, 1, 0)
        xpositions += numpy.where(this_move == EAST, 1, 0)
        xpositions -= numpy.where(this_move == WEST, 1, 0)
        
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[xymin, xymax, xymin, xymax],
                 title='%d particles after %d steps' %(np, step+1),
                 savefig='tmp_%03d.jpg' %(step+1))
    return xpositions, ypositions

numpy.random.seed(11)

np = 10
ns = 1000
plot_step = 10
x, y = random_walk_2D(np, ns, plot_step)
os.system('convert -delay 20 tmp_*.jpg movierw.gif')

for name in glob.glob('tmp_*.jpg'):
    os.remove(name)
