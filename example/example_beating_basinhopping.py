#!/usr/bin/env python3

# fit to a1*sin(w1 * x + f1) + a2*sin(w2 * x + f2)
import sys
sys.path.append('.')

import numpy as np
from matplotlib import pyplot as plt
from curve_fit import annealing

def f(x,p):
    return p[0]*np.sin(p[1]*x + p[2]) + p[3]*np.sin(p[4]*x+p[5])


xdata = np.linspace(-100,100,1000)
ydata = f(xdata, [1, 1, 0, 1, 0.9, 0])

plt.plot(xdata, ydata, label='data')
result = annealing.curve_fit(f, xdata, ydata, method='basinhopping', x0=np.zeros(6))

pres = result.x
ydata_res = f(xdata, pres)
plt.plot(xdata, ydata_res, label='fit')
plt.legend()
plt.grid()

plt.show()
