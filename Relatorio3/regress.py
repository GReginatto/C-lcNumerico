import numpy as np
import math
import matplotlib.pyplot as plt

def regress(x, y, n, al, a0, syx, r2):
    n = len(x)
    sumx = 0
    sumxy = 0
    st = 0
    sumy = 0
    sumx2 = 0
    sr = 0

    for i in range(n):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i]*y[i]
        sumx2 += x[i]*x[i]

    xm = sumx / n
    ym = sumy / n

    al[0] = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx*sumx)
    a0[0] = ym - al[0] * xm

    for i in range(n):
        st += (y[i] - ym)**2
        sr += (y[i] - al[0]*x[i] - a0[0])**2

    syx[0] = (sr / (n - 2))**0.5
    r2[0] = (st - sr) / st



