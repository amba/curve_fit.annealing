#!/usr/bin/env python3
import sys
sys.path.append('.')

import numpy as np
from matplotlib import pyplot as plt
from fit import anneal

N = 4
def f(x,p):
    return p[0]*np.sin(p[1]*x - p[2]) + p[3]*np.sin(p[4]*x-p[5]) + p[6]*(x-p[7])


xdata = np.linspace(-50,50,1000)
ydata = f(xdata, [1, 1, 1, 1, 0.8, 1, 0.03, 10])

plt.plot(xdata, ydata, label='data')
pi2 = 2*np.pi
bounds=[[0,2],[0,2],[0,2],[0,2],[0,2],[0,2],[-10,10]]
x0 = [0] * 8
print(x0)
print(bounds)
result = anneal.curve_fit(f, xdata, ydata, x0=x0# bounds=bounds
                          , method='basinhopping'# 'dual_annealing' 
)
print(result)
pres = result.x
ydata_res = f(xdata, pres)
plt.plot(xdata, ydata_res, label='fit')
plt.legend()
plt.grid()

plt.show(block=False)
import code
code.interact()
