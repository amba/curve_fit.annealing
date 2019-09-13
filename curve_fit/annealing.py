from scipy import optimize

def curve_fit(f, xdata, ydata, method='dual_annealing', *args, **kwargs):
    def minimize_func(p):
        res = f(xdata, p)- ydata
        return res.dot(res)
    return getattr(optimize, method)(minimize_func, *args, **kwargs)





