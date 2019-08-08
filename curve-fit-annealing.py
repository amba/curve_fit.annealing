#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

import scipy.optimize


def curve_fit_dual_annealing(f, xdata, ydata, *args, **kwargs):
    def minimize_func(p):
        return np.linalg.norm(f(xdata, p)- ydata)
    return scipy.optimize.dual_annealing(minimize_func, *args, **kwargs)



#if __name__ == "__main__":


def f(x,p):
    res = np.zeros(x.shape)
    for i in range(3):
        res += p[3*i]*np.exp(-((x-p[3*i+1])/p[3*i+2])**2)
    return res


xdata = np.linspace(-10,10,1000)
ydata = f(xdata, [1, -8, 1, 1, 0, 1, -1, 8, 1])

plt.plot(xdata, ydata, label='data')

bounds=list(zip([-10]*9,[10]*9))
print(bounds)
result = curve_fit_dual_annealing(f, xdata, ydata, bounds=bounds, maxiter=3000, initial_temp=100000)
print(result)
pres = result.x
ydata_res = f(xdata, pres)
plt.plot(xdata, ydata_res, label='fit')
plt.legend()

plt.show(block=False)
import code
code.interact()
