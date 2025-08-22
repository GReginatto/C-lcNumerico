import numpy as np
import math
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2

def euler(a, b, y0, m):
    h = (b - a) / m
    x = a
    y = y0

    VetX = [0] * (m + 1)
    VetY = [0] * (m + 1)

    VetX[0] = x
    VetY[0] = y

    fxy = f(x, y)

    for i in range(1, m + 1):
        x = x + h
        y = y + h * fxy
        fxy = f(x, y)

        VetX[i] = x
        VetY[i] = y

    return VetX, VetY



