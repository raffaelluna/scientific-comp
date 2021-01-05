from scitools.std import sqrt, pi, exp, cos, linspace, plot, movie
import time, glob, os, sys
from matplotlib.pyplot import show

for name in glob.glob('tmp_*.jpg'):
    os.remove(name)

def T(z,t):
    A = 10; t0 = 10
    k = 1e-6
    freq = 1./24
    a = sqrt(2*pi*freq/(2*k))
    temperature = t0 + A*exp(-a*z)*cos(2*pi*freq*t - a*z)

    return temperature

def anim_function(zf,time_values):
    counter = 0
    for time in time_values:
        func = T(zf,time)
        plot(zf,func,'-b',axis=[zf[0],zf[-1], 0, 20],xlabel='z',ylabel='T', legend='Time=%.0f' % time, savefig='tmp_%04d.jpg' % counter)
        show()
        counter +=1

    cmd = 'convert -delay 15 tmp_*.jpg movie-ex.gif'
    os.system(cmd)
    return


time_values = linspace(0,120,121)
zf = linspace(0,0.1,100)

anim_function(zf, time_values)
