# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:38:48 2018

@author: Raffael
"""

import numpy

def note(frequency, length, amplitude=1, sample_rate=44100):
    time_points = numpy.linspace(0, length, length*sample_rate)
    data = numpy.sin(2*numpy.pi*frequency*time_points)
    data = amplitude*data
    return data

import math, wave, commands, sys, os

def writesound(data, filename, sample_rate=44100):
    ofile = wave.open(filename, 'w')
    ofile.setnchannels(1)
    ofile.setsampwidth(2)
    ofile.setframerate(sample_rate)
    newdata = data.flatten()
    ofile.writeframesraw(newdata.astype(numpy.int16).tostring())
    ofile.close
    
data = note(440, 2)
max_amplitude = 2**15 - 1
data = max_amplitude*data
data = data.astype(numpy.int16)
writesound(data, 'Atone.mp3')

