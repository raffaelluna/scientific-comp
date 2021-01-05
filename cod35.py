# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:03:15 2018

@author: Raffael
"""
import numpy, math, wave, commands, sys, os
from scitools.sound import *
import matplotlib.pyplot as plt

def note(frequency, length, amplitude=1, sample_rate=44100):
    time_points = numpy.linspace(0, length, length*sample_rate)
    data = numpy.sin(2*numpy.pi*frequency*time_points)
    data = amplitude*data
    return data

def writesound(data, filename, sample_rate=44100):
    ofile = wave.open(filename, 'w')
    ofile.setnchannels(1)
    ofile.setsampwidth(2)
    ofile.setframerate(sample_rate)
    newdata = data.flatten()
    ofile.writeframesraw(newdata.astype(numpy.int16).tostring())
    ofile.close

def oscillations(N):
    x = numpy.zeros(N+1)
    for n in range(N+1):
        x[n] = numpy.exp(-4*n/float(N))*numpy.sin(8*numpy.pi*n/float(N))
    return x

def logistic(N):
    x = numpy.zeros(N+1)
    x[0] = 0.01
    q = 2
    for n in range(1, N+1):
        x[n] = x[n-1] + q*x[n-1]*(1 - x[n-1])
    return x

def make_sound(N, seqtype):
    filename = 'tmp1.wav'
    x = eval(seqtype)(N)
    freqs = 440 + x*200
    tones = []
    duration = 30.0/N
    max_amplitude = 2**15 - 1
    for n in range(N+1):
        tones.append(max_amplitude*note(freqs[n],duration, 1))
    data = numpy.concatenate(tones)
    writesound(data, filename)
#    play(data)
    
if __name__ == '__main__':
    try:
        seqtype = sys.argv[1]
        N = int(sys.argv[2])
    except IndexError:
        print 'Usage: %s oscillations|logistic N' % sys.argv[0]
        sys.exit(1)
    make_sound(N,seqtype)
    x = eval(seqtype)(N)
    freqs = 440 + x*400
    numb = range(N+1)
    print x
    print freqs
    plt.plot(freqs)
    plt.title(seqtype)
    plt.show()
    raw_input('Press enter to exit')
    

    