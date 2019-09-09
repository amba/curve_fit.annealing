"""
===================
curve_fit.annealing
===================

Most curve fitting algorithms rely on local optimization routines. These demand good estimates of the fit parameters.

Instead, this module allows to use  **Global Optimization** routines of [scipy.optimize] to minimize the squared deviation function.
"""

from scipy import optimize

def curve_fit(f, xdata, ydata, method='dual_annealing', *args, **kwargs):
    """Fit function f to data with selectable optimization method
       from `scipy.optimize`.

    Parameters
    ----------
    f: callable
        The model function, f(xdata, p). The second argument holds the fitting
        parameters.
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

    Returns
    -------
    res: OptimizeResult
    `OptimizeResult` object. The ``x`` attribute holds the fitting parameters.
    """
    def minimize_func(p):
        res = f(xdata, p)- ydata
        return res.dot(res)
    return getattr(optimize, method)(minimize_func, *args, **kwargs)





