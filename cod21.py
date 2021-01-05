# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:12:17 2018

@author: Usuário
"""

s = v0 = 0; a = t = 1
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--v0','--initial velocity', type=float, default = 0.0, help='initial velocity', metavar='v')


parser.add_argument('--s0','--initial position', type=float, default = 0.0, help='initial position', metavar='s')


parser.add_argument('--a','--aceleration', type=float, default = 1.0, help='aceleration', metavar='a')


parser.add_argument('--t','--time', type=float, default = 1.0, help='time', metavar='t')

args = parser.parse_args()
s0 = args.s0; v0 = args.v0; a=args.a; t = args.t
s = s0 + v0*t + 0.5*a*t**2
print('''
      position s=%g with velocity %s and aceleration %g is found at s=%g''' % (s0, v0, a, s))