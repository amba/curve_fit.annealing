#!/usr/bin/env python3
import sys
sys.path.append('.')

import numpy as np
from matplotlib import pyplot as plt
from fit import anneal

def f(x,p):
    res = np.zeros(x.shape)
    for i in range(3):
        res += p[3*i]*np.exp(-((x-p[3*i+1])/p[3*i+2])**2)
    return res


xdata = np.linspace(-30,30,1000)
ydata = f(xdata, [1, -25, 1, 1, 0, 1, -1, 25, 1])

plt.plot(xdata, ydata, label='data')

bounds=list(zip([-30]*9,[30]*9))
print(bounds)
result = anneal.curve_fit(f, xdata, ydata, bounds=bounds, maxiter=1000, )
print(result)
pres = result.x
ydata_res = f(xdata, pres)
plt.plot(xdata, ydata_res, label='fit')
plt.legend()
plt.grid()

plt.show(block=False)
import code
code.interact()
