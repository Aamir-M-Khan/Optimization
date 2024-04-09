import numpy as np

def ackley(x, y):
    a = x**2 + y**2
    b = 0.5 * a
    c = np.sqrt(b)
    d = 0.2 * c
    e = np.exp(-d)
    f = -20 * e

    g = 2*np.pi
    h = np.cos(g*x) + np.cos(g*y)
    i = 0.5 * h
    j = -np.exp(i)

    return f + j + e + 20 + np.exp(1) 