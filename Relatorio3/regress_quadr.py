import numpy as np
import math
import matplotlib.pyplot as plt



def regress_quadratica(x, y, a2, a1, a0, syx, r2):
    n = len(x)
    x = np.array(x)
    y = np.array(y)

    Sx = np.sum(x)
    Sx2 = np.sum(x**2)
    Sx3 = np.sum(x**3)
    Sx4 = np.sum(x**4)
    Sy = np.sum(y)
    Sxy = np.sum(x * y)
    Sx2y = np.sum((x**2) * y)

    A = np.array([
        [n, Sx, Sx2],
        [Sx, Sx2, Sx3],
        [Sx2, Sx3, Sx4]
    ])
    B = np.array([Sy, Sxy, Sx2y])

    coeffs = np.linalg.solve(A, B)

    a0[0] = coeffs[0]
    a1[0] = coeffs[1]
    a2[0] = coeffs[2]

    y_est = a0[0] + a1[0] * x + a2[0] * x**2

    st = np.sum((y - np.mean(y))**2)
    sr = np.sum((y - y_est)**2)
    syx[0] = np.sqrt(sr / (n - 3))
    r2[0] = (st - sr) / st
