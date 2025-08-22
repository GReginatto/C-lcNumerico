import numpy as np
import math
import matplotlib.pyplot as plt

def tridiag(x, y, n, e, f, g, r):
    f[0] = 2 * (x[1] - x[0])
    g[0] = x[1] - x[0]
    r[0] = 0

    for i in range(1, n - 1):
        e[i] = x[i] - x[i - 1]
        f[i] = 2 * (x[i + 1] - x[i - 1])
        g[i] = x[i + 1] - x[i]
        r[i] = 6 * ((y[i + 1] - y[i]) / (x[i + 1] - x[i]) -
                    (y[i] - y[i - 1]) / (x[i] - x[i - 1]))

    e[n - 1] = x[n - 1] - x[n - 2]
    f[n - 1] = 2 * (x[n - 1] - x[n - 2])
    r[n - 1] = 0


def decomp(e, f, g, n):
    for i in range(1, n):
        t = e[i-1] / g[i-1]
        g[i] = g[i] - t * f[i-1]
        e[i-1] = t

def subst(e, f, g, r, n, d2x):
    for i in range(1, n):
        r[i] = r[i] - e[i-1] * r[i-1]

    d2x[n-1] = r[n-1] / g[n-1]
    for i in range(n-2, -1, -1):
        d2x[i] = (r[i] - f[i] * d2x[i+1]) / g[i]

def interpol(x, y, n, d2x, xu, yu, dy, d2y):
    flag = 0
    i = 1
    while True:
        if xu >= x[i-1] and xu <= x[i]:
            c1 = d2x[i-1] / (6 * (x[i] - x[i-1]))
            c2 = d2x[i] / (6 * (x[i] - x[i-1]))
            c3 = y[i-1] / (x[i] - x[i-1]) - d2x[i-1] * (x[i] - x[i-1]) / 6
            c4 = y[i] / (x[i] - x[i-1]) - d2x[i] * (x[i] - x[i-1]) / 6

            t1 = c1 * (x[i] - xu)**3
            t2 = c2 * (xu - x[i-1])**3
            t3 = c3 * (x[i] - xu)
            t4 = c4 * (xu - x[i-1])
            yu[0] = t1 + t2 + t3 + t4

            t1 = -3 * c1 * (x[i] - xu)**2
            t2 =  3 * c2 * (xu - x[i-1])**2
            t3 = -c3
            t4 =  c4
            dy[0] = t1 + t2 + t3 + t4

            t1 = 6 * c1 * (x[i] - xu)
            t2 = 6 * c2 * (xu - x[i-1])
            d2y[0] = t1 + t2

            flag = 1
        else:
            i = i + 1

        if i == n or flag == 1:
            break

    if flag == 0:
        print("outside range")

def spline(x, y, xu):
    n = len(x)
    e = np.zeros(n)
    f = np.zeros(n)
    g = np.zeros(n)
    r = np.zeros(n)
    d2x = np.zeros(n)

    tridiag(x, y, n, e, f, g, r)
    decomp(e, f, g, n)
    subst(e, f, g, r, n, d2x)

    yu = [0]
    dy = [0]
    d2y = [0]

    interpol(x, y, n, d2x, xu, yu, dy, d2y)

    return yu[0], dy[0], d2y[0]

