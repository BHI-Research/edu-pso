import numpy as np

################################################################

def fn1(x):
    res = 0
    for i in range(len(x)):
        res += x[i]**2
    return res

################################################################

def fn2(x):
    return np.sum(np.power(x, 2))

################################################################