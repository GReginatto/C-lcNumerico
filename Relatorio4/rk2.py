import numpy as np
import math
import matplotlib.pyplot as plt

def rkDois(a, b, y0, m):
    h = (b - a) / m
    xt = a
    yt = y0
    VetX = [0] * (m + 1)
    VetY = [0] * (m + 1)
    VetX[0] = xt
    VetY[0] = yt

    for i in range(0, m):
        k1 = f(xt, yt)
        k2 = f(xt + h, yt + h * k1)

        yt = yt + (h / 2) * (k1 + k2)
        xt = xt + h

        VetX[i + 1] = xt
        VetY[i + 1] = yt

    return VetX, VetY
