curve_fit.annealing
===================

Most curve fitting algorithms rely on local optimization routines. These demand good estimates of the fit parameters.

Instead, this module allows to use  **global optimization** routines of ``scipy.optimize`` to minimize the squared deviation function.

Installation
------------

.. highlight:: none
               
This module can be installed from PyPI ::

    pip3 install curve_fit.annealing

Example
-------

Let us fit a beat signal with two sinus functions, with a total of 6 free parameters.

By default, the ``curve_fit`` function of this module will use the ``scipy.optimize.dual_annealing`` method to find the global optimum of the curve fitting problem. The dual annealing algorithm requires bounds for the fitting parameters.
Other global optimization methods like ``scipy.optimize.basinhopping`` require an initial guess of the parameters instead.


.. highlight:: python

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
  

Or use ``scipy.optimize.basinhopping`` ::

 result = annealing.curve_fit(f, xdata, ydata, method='basinhopping', x0=np.zeros(6))