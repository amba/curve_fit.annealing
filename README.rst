curve_fit.annealing
===============================

Most curve fitting algorithms rely on local optimization routines. These demand good estimates of the fit parameters.

Instead, this module allows to use  **global optimization** routines of
scipy.optimize_ to minimize the squared deviation function.

Installation
------------------------
               
This module can be installed from PyPI ::

    pip3 install curve_fit.annealing

Example
---------------

Let us fit a beat signal with two sinus functions, with a total of 6 free parameters.

By default, the ``curve_fit`` function of this module will use the scipy.optimize.dual_annealing_ method to find the global optimum of the curve fitting problem. The dual annealing algorithm requires bounds for the fitting parameters.
Other global optimization methods like scipy.optimize.basinhopping_ require an initial guess of the parameters instead.


::
   
 import numpy as np
 from matplotlib import pyplot as plt
 from curve_fit import annealing
 
 def f(x,p):
       # Sum of two sinus functions
       return p[0]*np.sin(p[1]*x + p[2]) + p[3]*np.sin(p[4]*x+p[5])
   
   
   xdata = np.linspace(-100,100,1000)
   ydata = f(xdata, [1, 1, 0, 1, 0.9, 0])
   
   plt.plot(xdata, ydata, label='data')
   bounds=[[0,2],[0,2],[0,2*np.pi],[0,2],[0,2],[0,2*np.pi]]
   
   result = annealing.curve_fit(f, xdata, ydata, bounds=bounds)
   
   p_opt = result.x # optimal fit parameters
   ydata_res = f(xdata, p_opt)
   plt.plot(xdata, ydata_res, label='fit')
   plt.legend()
   plt.grid()
   
   plt.show()
  

Or use scipy.optimize.basinhopping_ ::

 result = annealing.curve_fit(f, xdata, ydata, method='basinhopping', x0=np.zeros(6))


API
-----

``curve_fit(f, xdata, ydata, [method='dual_annealing', args, kwargs])``

Fit function ``f`` to data with selectable optimization method
from ``scipy.optimize``.

Parameters:
 f: callable
  The model function, ``f(xdata, p)``. The second argument holds the
  fitting parameters.
 xdata : array_like or object
  The independent variable where the data is measured.
  Should usually be an M-length sequence or an (k,M)-shaped array for
  functions with k predictors, but can actually be any object.
 ydata : array_like
  The dependent data, a length M array - nominally ``f(xdata, ...)``.
 method : str
  scipy.optimize method to use for non-linear least squares minimization.
  Default is 'dual_annealing'.
 args, kwargs : tuple and dict, optional
  Additional arguments passed to the optimization method.

Returns:
 Return ``OptimizeResult`` object. The ``x`` attribute holds the fitting
 parameters. 


.. _scipy.optimize: https://docs.scipy.org/doc/scipy/reference/optimize.html
.. _scipy.optimize.dual_annealing: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html#scipy.optimize.dual_annealing
.. _scipy.optimize.basinhopping: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.basinhopping.html#scipy.optimize.basinhopping
